import "server-only";
import { createClient } from "@/lib/supabase/server";
import { alleRijen } from "@/lib/allerijen";

/**
 * De groepen van de opvolging — /begeleiding
 *
 * Een gezin registreert met een plusklascode, en die code bepaalt bij welke
 * groep het hoort. Zo loopt de plusklas van Hasselt niet meer door de
 * testgezinnen. Zie supabase/groepen.sql.
 *
 * Gezinnen die registreerden voor die kolom bestond hebben nog geen code. Die
 * verzamelen we onder de sleutel ZONDER_GROEP, zodat ze niet uit beeld vallen.
 */

export const ZONDER_GROEP = "zonder-groep";

export type KindRij = {
  id: string;
  naam: string;
  profiles: {
    id: string;
    full_name: string;
    is_plusklas: boolean;
    plusklas_code: string | null;
  } | null;
  /** Hoeveel vragen dit kind al beantwoordde, en hoeveel daarvan juist waren. */
  aantal: number;
  juist: number;
  sterren: number;
  /** Wanneer het voor het laatst oefende, of null als het nog niets deed. */
  laatst: string | null;
};

/** De cijfers van één kind, zoals de databank ze zelf telt. */
export type Cijfers = {
  aantal: number;
  juist: number;
  sterren: number;
  laatst: string | null;
};

/**
 * Per kind de aantallen, door de databank geteld.
 *
 * Dit haalde vroeger élk antwoord van élk kind op om er de lengte van te
 * nemen. Dat is zwaar, en boven de duizend rijen geeft de databank niet alles
 * terug, dus de cijfers klopten niet meer bij een kind dat veel oefent. Zie
 * supabase/volledige-opvolging.sql, en lib/allerijen.ts voor dezelfde les.
 *
 * Staat die functie er nog niet, dan tellen we het zelf, met alle rijen in
 * blokken. De regels van de databank gelden in beide gevallen: je krijgt enkel
 * de kinderen die je mag zien.
 */
export async function haalCijfers(): Promise<Map<string, Cijfers>> {
  const supabase = await createClient();
  const uit = new Map<string, Cijfers>();

  const { data, error } = await supabase.rpc("opvolging_per_kind");
  if (!error && Array.isArray(data)) {
    for (const rij of data as {
      kind_id: string;
      aantal: number | string;
      juist: number | string;
      sterren: number | string;
      laatst: string | null;
    }[])
      uit.set(rij.kind_id, {
        aantal: Number(rij.aantal ?? 0),
        juist: Number(rij.juist ?? 0),
        sterren: Number(rij.sterren ?? 0),
        laatst: rij.laatst ?? null,
      });
    return uit;
  }

  const rijen = await alleRijen<{
    kind_id: string;
    correct: boolean;
    beantwoord_op: string;
  }>((van, tot) =>
    supabase
      .from("voortgang")
      .select("kind_id, correct, beantwoord_op")
      .order("id")
      .range(van, tot),
  );
  for (const rij of rijen) {
    const vorig = uit.get(rij.kind_id) ?? {
      aantal: 0,
      juist: 0,
      sterren: 0,
      laatst: null,
    };
    vorig.aantal += 1;
    if (rij.correct) vorig.juist += 1;
    if (!vorig.laatst || rij.beantwoord_op > vorig.laatst)
      vorig.laatst = rij.beantwoord_op;
    uit.set(rij.kind_id, vorig);
  }
  const sterren = await alleRijen<{ kind_id: string }>((van, tot) =>
    supabase.from("stickers").select("kind_id").order("id").range(van, tot),
  );
  for (const rij of sterren) {
    const vorig = uit.get(rij.kind_id) ?? {
      aantal: 0,
      juist: 0,
      sterren: 0,
      laatst: null,
    };
    vorig.sterren += 1;
    uit.set(rij.kind_id, vorig);
  }
  return uit;
}

export type Groep = {
  /** De code zelf, of ZONDER_GROEP voor de gezinnen zonder code. */
  sleutel: string;
  /** Wat er groot op het kaartje staat. */
  naam: string;
  /** Het woordje dat jij bij de code zette, bijvoorbeeld "plusklas Hasselt". */
  label: string | null;
  actief: boolean;
  /**
   * Volgt Kim deze groep in detail op? Dan is er een fiche per kind, met de
   * opgeloste testen, opmerkingen en werk van thuis. Staat dit af, dan blijft
   * het bij de tabel met de voortgang hieronder. Kim op 14 oktober 2026: "de
   * andere is het leuk om zo in een tabel de voortgang te zien maar daar moet
   * geen zware opvolging bij zitten."
   */
  volledigeOpvolging: boolean;
  kinderen: KindRij[];
  gezinnen: number;
};

/**
 * Haalt alle plusklaskinderen op en verdeelt ze over de groepen.
 *
 * De filter op is_plusklas staat er ook voor jou als beheerder: de regels in
 * de databank laten jou álle kinderen zien, en zonder deze filter kwamen de
 * betalende gezinnen hier mee op het scherm.
 */
export async function haalGroepen(): Promise<Groep[]> {
  const supabase = await createClient();

  const [{ data: kinderenData }, codes, cijfers] = await Promise.all([
    supabase
      .from("kinderen")
      .select("id, naam, profiles(id, full_name, is_plusklas, plusklas_code)")
      .order("naam"),
    haalCodes(),
    haalCijfers(),
  ]);

  const leeg = { aantal: 0, juist: 0, sterren: 0, laatst: null };
  const kinderen = ((kinderenData ?? []) as unknown as KindRij[])
    .filter((k) => k.profiles?.is_plusklas)
    .map((k) => ({ ...k, ...(cijfers.get(k.id) ?? leeg) }));

  const perSleutel = new Map<string, KindRij[]>();
  for (const kind of kinderen) {
    const sleutel = kind.profiles?.plusklas_code ?? ZONDER_GROEP;
    const rij = perSleutel.get(sleutel);
    if (rij) rij.push(kind);
    else perSleutel.set(sleutel, [kind]);
  }

  const telGezinnen = (rijen: KindRij[]) =>
    new Set(rijen.map((k) => k.profiles?.id).filter(Boolean)).size;

  const groepen: Groep[] = codes.map((c) => {
    const rijen = perSleutel.get(c.code) ?? [];
    return {
      sleutel: c.code,
      naam: c.code,
      label: c.label ?? null,
      actief: c.actief,
      volledigeOpvolging: c.volledige_opvolging,
      kinderen: rijen,
      gezinnen: telGezinnen(rijen),
    };
  });

  // Een gezin kan bij een code horen die intussen verwijderd is uit de
  // codetabel. Dan staat de code nog op het profiel maar kent de lijst ze
  // niet; die kinderen zetten we bij "nog geen groep", anders verdwijnen ze.
  const gekend = new Set(groepen.map((g) => g.sleutel));
  const wees: KindRij[] = [];
  for (const [sleutel, rijen] of perSleutel) {
    if (sleutel === ZONDER_GROEP || gekend.has(sleutel)) continue;
    wees.push(...rijen);
  }
  const zonder = [...(perSleutel.get(ZONDER_GROEP) ?? []), ...wees].sort(
    (a, b) => a.naam.localeCompare(b.naam, "nl-BE"),
  );

  if (zonder.length) {
    groepen.push({
      sleutel: ZONDER_GROEP,
      naam: "Nog geen groep",
      label: null,
      actief: true,
      /* Een gezin zonder groep weten we niets van, dus houden we het licht.
         Zet het eerst bij een groep; hoort het bij de plusklas, dan staat de
         fiche er meteen. */
      volledigeOpvolging: false,
      kinderen: zonder,
      gezinnen: telGezinnen(zonder),
    });
  }

  return groepen;
}

/** Eén code, met het vinkje voor de volle opvolging erbij. */
export type CodeRij = {
  code: string;
  label: string | null;
  actief: boolean;
  volledige_opvolging: boolean;
};

/**
 * De codes zoals ze in het keuzelijstje op een fiche staan.
 *
 * Zolang supabase/volledige-opvolging.sql niet gedraaid is, bestaat de kolom
 * "volledige_opvolging" nog niet. Dan krijgt elke groep de volle fiche, net
 * zoals vroeger: een scherm dat er al was, mag niet wegvallen omdat een
 * sql-bestand nog moet draaien.
 */
export async function haalCodes(): Promise<CodeRij[]> {
  const supabase = await createClient();
  const { data, error } = await supabase
    .from("plusklas_codes")
    .select("code, label, actief, volledige_opvolging")
    .order("created_at", { ascending: false });
  if (!error) return (data ?? []) as CodeRij[];

  const { data: zonder } = await supabase
    .from("plusklas_codes")
    .select("code, label, actief")
    .order("created_at", { ascending: false });
  return ((zonder ?? []) as Omit<CodeRij, "volledige_opvolging">[]).map(
    (c) => ({
      ...c,
      volledige_opvolging: true,
    }),
  );
}
