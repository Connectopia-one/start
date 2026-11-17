"use server";

import { getSessionProfile } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Een bedankje voor een melding wegklikken, en dat voor altijd.

  Kim, 17 november 2026: "de meldingen van een maand geleden blijven terug
  komen." Het kruisje werd enkel in die ene browser onthouden. Op een andere
  computer, een andere browser of na het wissen van de browsergeschiedenis
  stonden dezelfde bedankjes er dus weer. Nu zetten we in de databank het
  moment dat de melder het gezien heeft (kolom gezien_op, zie
  supabase/melding-gezien.sql), en dan komt het nergens meer terug.

  Enkel bij je éigen melding: de admin-sleutel gaat pas aan het werk na de
  controle dat deze melding van wie ingelogd is. Er wordt niets gewist.
*/
export async function meldingGezien(id: string) {
  const session = await getSessionProfile();
  if (!session || typeof id !== "string" || !id) return;

  const admin = createAdminClient();
  // Bestaat de kolom nog niet (SQL nog niet gedraaid), dan lukt dit niet en
  // onthoudt enkel de browser het, zoals vroeger. Geen foutmelding voor ouders.
  await admin
    .from("meldingen")
    .update({ gezien_op: new Date().toISOString() })
    .eq("id", id)
    .eq("profile_id", session.userId)
    .is("gezien_op", null);
}
