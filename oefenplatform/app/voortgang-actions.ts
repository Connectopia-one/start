"use server";

import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import type { SupabaseClient } from "@supabase/supabase-js";
import { LEGE_TELLING, type Telling } from "@/lib/badges";

/** Geeft de admin client terug enkel als de ingelogde gebruiker dit kind mag beheren, anders null. */
async function kindEigenaarOfNull(
  kindId: string,
): Promise<SupabaseClient | null> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return null;

  const admin = createAdminClient();
  const { data: kind } = await admin
    .from("kinderen")
    .select("id, profile_id")
    .eq("id", kindId)
    .maybeSingle();
  if (!kind || kind.profile_id !== user.id) return null;

  return admin;
}

/**
 * Registreert één beantwoorde vraag voor een kind. Wordt rechtstreeks vanuit
 * de Quiz-client-component aangeroepen (geen formulier) — faalt altijd stil,
 * zodat een opslagprobleem nooit de oefenervaring van het kind onderbreekt.
 */
export async function registreerAntwoord(
  kindId: string,
  vraagId: string,
  // Het hoofdstuk wordt er apart bij bewaard. Vervangt Kim later de vragen van
  // dit hoofdstuk door een nieuw bestand, dan verdwijnt de vraag maar blijft
  // dit antwoord meetellen. Zonder die kolom stond elk kind na zo'n import
  // weer op nul.
  hoofdstukId: string | null,
  correct: boolean,
  // Een lijstje nummers hoort bij een meerkeuzevraag met meer dan één juist
  // antwoord; zie lib/antwoord.ts. De kolom is jsonb, dus dat past gewoon.
  gegevenAntwoord: string | number | boolean | number[] | null,
  // Welke beurt van een spellingvraag met wisselende woorden dit was: 0 is de
  // vraag zelf. Zonder dat nummer zou een ouder die meekijkt de vraag over
  // 'man' zien staan met het antwoord 'kinderen' eronder. Zie
  // lib/spellingvariant.ts.
  variant: number = 0,
) {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin) return;
  const rij = {
    kind_id: kindId,
    vraag_id: vraagId,
    hoofdstuk_id: hoofdstukId,
    correct,
    gegeven_antwoord: gegevenAntwoord,
  };
  const { error } = await admin
    .from("voortgang")
    .insert(variant > 0 ? ({ ...rij, variant } as typeof rij) : rij);
  // Zolang supabase/spellingvarianten.sql nog niet gedraaid is, bestaat de
  // kolom "variant" niet. Dan gaat het antwoord er zonder in: liever de
  // wisselende woorden kwijt dan de voortgang van het kind.
  if (error && variant > 0) await admin.from("voortgang").insert(rij);
}

/**
 * Kent een "sticker" toe voor een hoofdstuk dat volledig correct afgewerkt werd.
 * De unique-regel op (kind_id, hoofdstuk_id) zorgt dat dit maar één keer telt,
 * ook al maakt het kind het hoofdstuk later nog eens perfect.
 */
export async function registreerSticker(kindId: string, hoofdstukId: string) {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin) return;
  await admin
    .from("stickers")
    .upsert(
      { kind_id: kindId, hoofdstuk_id: hoofdstukId },
      { onConflict: "kind_id,hoofdstuk_id", ignoreDuplicates: true },
    );
}

/** Wat een kind met één hoofdstuk al gedaan heeft. */
export type HoofdstukStatus = {
  hoofdstukId: string;
  /** Het kind beantwoordde hier al minstens één vraag. */
  gemaakt: boolean;
  /** Het hoofdstuk werd ooit volledig juist afgewerkt (er hangt een sticker aan). */
  perfect: boolean;
  /** Wanneer het kind hier voor het laatst aan werkte. */
  laatst: string | null;
};

/**
 * Haalt voor één kind op welke van deze hoofdstukken het al gemaakt heeft.
 *
 * Wordt vanuit de lijsten aangeroepen, niet vanuit een formulier: de keuze van
 * het actieve kind staat in de browser (zie lib/actiefkind.ts), dus de server
 * kan ze niet zelf weten. Een kind mag een hoofdstuk zo vaak opnieuw maken als
 * het wil — we tonen alleen dát het gemaakt is, niet hoeveel keer, zodat
 * herkansen nooit als iets slechts voelt.
 */
export async function haalHoofdstukStatus(
  kindId: string,
  hoofdstukIds: string[],
): Promise<HoofdstukStatus[]> {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin || !hoofdstukIds.length) return [];
  // Eén niveau telt hooguit enkele tientallen hoofdstukken; een langere lijst
  // is nooit een echte pagina en zou alleen het webadres opblazen.
  const ids = hoofdstukIds.slice(0, 200);

  const [{ data: stickers }, { data: rijen }] = await Promise.all([
    admin
      .from("stickers")
      .select("hoofdstuk_id")
      .eq("kind_id", kindId)
      .in("hoofdstuk_id", ids),
    admin
      .from("voortgang")
      .select("beantwoord_op, hoofdstuk_id")
      .eq("kind_id", kindId)
      .in("hoofdstuk_id", ids),
  ]);

  const perfect = new Set(
    (stickers ?? []).map((s) => s.hoofdstuk_id as string),
  );
  const laatste = new Map<string, string>();
  for (const rij of (rijen ?? []) as unknown as {
    beantwoord_op: string;
    hoofdstuk_id: string | null;
  }[]) {
    const id = rij.hoofdstuk_id;
    if (!id) continue;
    const huidige = laatste.get(id);
    if (!huidige || rij.beantwoord_op > huidige)
      laatste.set(id, rij.beantwoord_op);
  }

  return ids.map((id) => ({
    hoofdstukId: id,
    gemaakt: laatste.has(id) || perfect.has(id),
    perfect: perfect.has(id),
    laatst: laatste.get(id) ?? null,
  }));
}

/**
 * De cijfers achter de verzamelbadges van één kind.
 *
 * Alles wordt geteld uit `voortgang` en `stickers`, de twee tabellen die het
 * platform toch al vult. Er wordt niets bijgehouden dat alleen voor de badges
 * dient, dus een kind dat hier voor het eerst kijkt, ziet meteen wat het de
 * voorbije weken al verdiend heeft. Zie lib/badges.ts.
 */
export async function haalTelling(kindId: string): Promise<Telling> {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin) return LEGE_TELLING;

  const [gemaakt, juist, hoekje, sterrenRijen] = await Promise.all([
    admin
      .from("voortgang")
      .select("id", { count: "exact", head: true })
      .eq("kind_id", kindId),
    admin
      .from("voortgang")
      .select("id", { count: "exact", head: true })
      .eq("kind_id", kindId)
      .eq("correct", true),
    admin
      .from("voortgang")
      .select("id, hoofdstukken!inner(niveau)", { count: "exact", head: true })
      .eq("kind_id", kindId)
      .eq("correct", true)
      .eq("hoofdstukken.niveau", "hoekje"),
    // De sterren zelf zijn er hooguit enkele tientallen, dus die halen we
    // gewoon op: daaruit volgen én het aantal, én in hoeveel vakken, én of er
    // een hoofdstuk van 🧱 Basis bij zit.
    admin
      .from("stickers")
      .select("hoofdstuk_id, hoofdstukken!inner(vak_id, niveau)")
      .eq("kind_id", kindId),
  ]);

  const sterren = (sterrenRijen.data ?? []) as unknown as {
    hoofdstukken: { vak_id: string; niveau: string };
  }[];

  return {
    gemaakt: gemaakt.count ?? 0,
    juist: juist.count ?? 0,
    sterren: sterren.length,
    vakkenMetSter: new Set(sterren.map((s) => s.hoofdstukken.vak_id)).size,
    basisSter: sterren.some((s) => s.hoofdstukken.niveau === "basis"),
    hoekjeJuist: (hoekje.count ?? 0) > 0,
  };
}

/** Wat een kind met de vragen van één hoofdstuk al deed. */
export type Oefenstand = {
  /** De vragen die het al eens juist had. */
  juist: string[];
  /** Hoe vaak het elke vraag al beantwoordde, juist of fout. */
  beurten: Record<string, number>;
};

/**
 * De vragen van één hoofdstuk die dit kind al eens juist beantwoordde, en hoe
 * vaak het elke vraag al maakte.
 *
 * Het tellen dient voor de wisselende woorden bij spelling: wie een vraag voor
 * de tweede keer krijgt, krijgt het tweede woord. Zie lib/spellingvariant.ts.
 *
 * Gevraagd door een testgezin op 30 september 2026: "Telkens als je teruggaat
 * naar een hoofdstuk die je al eerder hebt gedaan, start je volledig opnieuw.
 * Zou het mogelijk zijn om enkel de vragen te krijgen die nog niet eerder
 * werden opgelost?"
 *
 * Enkel de júiste antwoorden tellen. Een vraag die een kind fout had, hoort
 * er de volgende keer weer bij; dat is net de vraag die het nog moet oefenen.
 *
 * Net als haalHoofdstukStatus wordt dit vanuit de browser aangeroepen, want
 * daar staat welk kind aan het oefenen is (zie lib/actiefkind.ts). Gaat er
 * iets mis, dan komt er een lege lijst terug en krijgt het kind gewoon alle
 * vragen: nooit minder oefenen door een fout.
 */
export async function haalOefenstand(
  kindId: string,
  hoofdstukId: string,
): Promise<Oefenstand> {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin) return { juist: [], beurten: {} };

  const { data } = await admin
    .from("voortgang")
    .select("vraag_id, correct")
    .eq("kind_id", kindId)
    .eq("hoofdstuk_id", hoofdstukId);

  const juist = new Set<string>();
  const beurten: Record<string, number> = {};
  for (const rij of (data ?? []) as unknown as {
    vraag_id: string | null;
    correct: boolean;
  }[]) {
    if (!rij.vraag_id) continue;
    if (rij.correct) juist.add(rij.vraag_id);
    beurten[rij.vraag_id] = (beurten[rij.vraag_id] ?? 0) + 1;
  }
  return { juist: [...juist], beurten };
}
