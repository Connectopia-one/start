import "server-only";
import { createClient } from "@/lib/supabase/server";

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
  voortgang: { id: string; correct: boolean }[];
  stickers: { id: string }[];
};

export type Groep = {
  /** De code zelf, of ZONDER_GROEP voor de gezinnen zonder code. */
  sleutel: string;
  /** Wat er groot op het kaartje staat. */
  naam: string;
  /** Het woordje dat jij bij de code zette, bijvoorbeeld "plusklas Hasselt". */
  label: string | null;
  actief: boolean;
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

  const [{ data: kinderenData }, { data: codesData }] = await Promise.all([
    supabase
      .from("kinderen")
      .select(
        "id, naam, profiles(id, full_name, is_plusklas, plusklas_code), voortgang(id, correct), stickers(id)",
      )
      .order("naam"),
    supabase
      .from("plusklas_codes")
      .select("code, label, actief")
      .order("created_at", { ascending: false }),
  ]);

  const kinderen = ((kinderenData ?? []) as unknown as KindRij[]).filter(
    (k) => k.profiles?.is_plusklas,
  );

  const perSleutel = new Map<string, KindRij[]>();
  for (const kind of kinderen) {
    const sleutel = kind.profiles?.plusklas_code ?? ZONDER_GROEP;
    const rij = perSleutel.get(sleutel);
    if (rij) rij.push(kind);
    else perSleutel.set(sleutel, [kind]);
  }

  const telGezinnen = (rijen: KindRij[]) =>
    new Set(rijen.map((k) => k.profiles?.id).filter(Boolean)).size;

  const groepen: Groep[] = (codesData ?? []).map((c) => {
    const rijen = perSleutel.get(c.code) ?? [];
    return {
      sleutel: c.code,
      naam: c.code,
      label: c.label ?? null,
      actief: c.actief,
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
      kinderen: zonder,
      gezinnen: telGezinnen(zonder),
    });
  }

  return groepen;
}

/** De codes zoals ze in het keuzelijstje op een fiche staan. */
export async function haalCodes(): Promise<
  { code: string; label: string | null; actief: boolean }[]
> {
  const supabase = await createClient();
  const { data } = await supabase
    .from("plusklas_codes")
    .select("code, label, actief")
    .order("created_at", { ascending: false });
  return (data ?? []) as { code: string; label: string | null; actief: boolean }[];
}
