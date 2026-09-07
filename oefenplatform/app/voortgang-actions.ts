"use server";

import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Registreert één beantwoorde vraag voor een kind. Wordt rechtstreeks vanuit
 * de Quiz-client-component aangeroepen (geen formulier) — faalt altijd stil,
 * zodat een opslagprobleem nooit de oefenervaring van het kind onderbreekt.
 */
export async function registreerAntwoord(kindId: string, vraagId: string, correct: boolean) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return;

  const admin = createAdminClient();
  const { data: kind } = await admin
    .from("kinderen")
    .select("id, profile_id")
    .eq("id", kindId)
    .maybeSingle();
  if (!kind || kind.profile_id !== user.id) return;

  await admin.from("voortgang").insert({ kind_id: kindId, vraag_id: vraagId, correct });
}
