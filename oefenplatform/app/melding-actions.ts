"use server";

import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";

/**
 * Onthoudt dat iemand het bedankje voor zijn melding(en) weggeklikt heeft,
 * bij de melding zelf in Supabase (kolom gezien_op, zie
 * supabase/melding-gezien.sql). Zo komt het op geen enkel toestel terug.
 *
 * Enkel de eigen meldingen van de ingelogde persoon worden aangepast. Faalt
 * altijd stil: het bedankje is in de browser toch al weg.
 */
export async function meldingGezien(ids: string[]): Promise<void> {
  try {
    const schoon = ids.filter((id) => typeof id === "string").slice(0, 20);
    if (schoon.length === 0) return;

    const supabase = await createClient();
    const {
      data: { user },
    } = await supabase.auth.getUser();
    if (!user) return;

    const admin = createAdminClient();
    await admin
      .from("meldingen")
      .update({ gezien_op: new Date().toISOString() })
      .in("id", schoon)
      .eq("profile_id", user.id)
      .is("gezien_op", null);
  } catch {
    // Stil: de browser onthoudt het intussen ook nog.
  }
}
