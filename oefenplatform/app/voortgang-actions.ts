"use server";

import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import type { SupabaseClient } from "@supabase/supabase-js";

/** Geeft de admin client terug enkel als de ingelogde gebruiker dit kind mag beheren, anders null. */
async function kindEigenaarOfNull(kindId: string): Promise<SupabaseClient | null> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return null;

  const admin = createAdminClient();
  const { data: kind } = await admin.from("kinderen").select("id, profile_id").eq("id", kindId).maybeSingle();
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
  correct: boolean,
  // Een lijstje nummers hoort bij een meerkeuzevraag met meer dan één juist
  // antwoord; zie lib/antwoord.ts. De kolom is jsonb, dus dat past gewoon.
  gegevenAntwoord: string | number | boolean | number[] | null
) {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin) return;
  await admin
    .from("voortgang")
    .insert({ kind_id: kindId, vraag_id: vraagId, correct, gegeven_antwoord: gegevenAntwoord });
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
    .upsert({ kind_id: kindId, hoofdstuk_id: hoofdstukId }, { onConflict: "kind_id,hoofdstuk_id", ignoreDuplicates: true });
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
  hoofdstukIds: string[]
): Promise<HoofdstukStatus[]> {
  const admin = await kindEigenaarOfNull(kindId);
  if (!admin || !hoofdstukIds.length) return [];
  // Eén niveau telt hooguit enkele tientallen hoofdstukken; een langere lijst
  // is nooit een echte pagina en zou alleen het webadres opblazen.
  const ids = hoofdstukIds.slice(0, 200);

  const [{ data: stickers }, { data: rijen }] = await Promise.all([
    admin.from("stickers").select("hoofdstuk_id").eq("kind_id", kindId).in("hoofdstuk_id", ids),
    admin
      .from("voortgang")
      .select("beantwoord_op, vragen!inner(hoofdstuk_id)")
      .eq("kind_id", kindId)
      .in("vragen.hoofdstuk_id", ids),
  ]);

  const perfect = new Set((stickers ?? []).map((s) => s.hoofdstuk_id as string));
  const laatste = new Map<string, string>();
  for (const rij of (rijen ?? []) as unknown as {
    beantwoord_op: string;
    vragen: { hoofdstuk_id: string } | null;
  }[]) {
    const id = rij.vragen?.hoofdstuk_id;
    if (!id) continue;
    const huidige = laatste.get(id);
    if (!huidige || rij.beantwoord_op > huidige) laatste.set(id, rij.beantwoord_op);
  }

  return ids.map((id) => ({
    hoofdstukId: id,
    gemaakt: laatste.has(id) || perfect.has(id),
    perfect: perfect.has(id),
    laatst: laatste.get(id) ?? null,
  }));
}
