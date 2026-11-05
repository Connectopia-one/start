"use server";

import { redirect } from "next/navigation";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { leesEnquete } from "@/inhoud/enquete";

/**
 * Een gezin stuurt de enquête in, of past ze aan.
 *
 * Eén enquête per account (unieke index in supabase/enquete-en-reviews.sql).
 * Opnieuw insturen werkt de bestaande bij, zodat niemand dubbel meetelt.
 * Er gebeurt verder niets vanzelf: de gratis toegang komt pas als Kim in
 * Beheer op "Goedkeuren" klikt.
 */
export async function stuurEnqueteIn(formData: FormData) {
  const session = await getSessionProfile();
  if (!session) {
    redirect("/login?fout=" + encodeURIComponent("Log eerst in om de enquête in te vullen."));
  }

  const { antwoorden, ontbreekt } = leesEnquete(formData);
  if (ontbreekt.length > 0) {
    redirect(
      "/enquete?fout=" +
        encodeURIComponent(`Nog niet alles is ingevuld: ${ontbreekt.join(" · ")}`),
    );
  }

  const supabase = await createClient();
  const { error } = await supabase.from("enquetes").upsert(
    {
      profile_id: session.userId,
      antwoorden,
      bijgewerkt_op: new Date().toISOString(),
    },
    { onConflict: "profile_id" },
  );

  if (error) {
    console.error("enquête insturen mislukt:", error.message);
    redirect(
      "/enquete?fout=" +
        encodeURIComponent(`Het insturen lukte niet. De melding luidt: ${error.message}`),
    );
  }

  redirect("/enquete?melding=bedankt");
}
