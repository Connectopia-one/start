"use server";

import { redirect } from "next/navigation";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

/**
 * Een gezin schrijft een review, of past zijn review aan.
 *
 * Alleen echte reviews (Kim, 5 november 2026): insturen kan enkel met een
 * account, één per account, en niets komt op het bord voor Kim het ophangt.
 * De databank bewaakt dat zelf (supabase/enquete-en-reviews.sql). Een review
 * die al hangt, kan het gezin niet meer stilletjes veranderen.
 */
export async function stuurReviewIn(formData: FormData) {
  const session = await getSessionProfile();
  if (!session) {
    redirect("/login?fout=" + encodeURIComponent("Log eerst in om een review te schrijven."));
  }

  const tekst = String(formData.get("tekst") || "").trim();
  const sterren = Number(formData.get("sterren"));
  const naam = String(formData.get("naam_tonen") || "").trim().slice(0, 60);
  const toestemming = formData.get("toestemming") === "ja";

  if (tekst.length < 20) terug("Schrijf er wat meer bij, een paar zinnen is genoeg.");
  if (tekst.length > 1200) terug("Je review is wat lang. Hou het bij 1200 tekens.");
  if (!Number.isInteger(sterren) || sterren < 1 || sterren > 5) terug("Kies eerst een aantal sterren.");
  if (!toestemming) terug("Vink aan dat we je review op het bord mogen hangen.");

  const supabase = await createClient();
  const { data: bestaand } = await supabase
    .from("reviews")
    .select("id, goedgekeurd")
    .eq("profile_id", session.userId)
    .maybeSingle();

  if (bestaand?.goedgekeurd) {
    terug("Je review hangt al op het bord. Wil je iets veranderen? Laat het ons weten via info@matmgroep.com.");
  }

  const rij = {
    tekst,
    sterren,
    naam_tonen: naam || null,
    toestemming: true,
    niet_geplaatst: false,
    bericht: null,
  };

  const { error } = bestaand
    ? await supabase.from("reviews").update(rij).eq("id", bestaand.id).eq("profile_id", session.userId)
    : await supabase.from("reviews").insert({ ...rij, profile_id: session.userId });

  if (error) {
    console.error("review insturen mislukt:", error.message);
    terug(`Het insturen lukte niet. De melding luidt: ${error.message}`);
  }

  redirect("/reviews?melding=bedankt#jouw-review");
}

function terug(bericht: string): never {
  redirect(`/reviews?fout=${encodeURIComponent(bericht)}#schrijf`);
}
