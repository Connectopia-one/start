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
  gegevenAntwoord: string | number | boolean | null
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
