"use server";

import { redirect } from "next/navigation";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";

/**
 * Een kind stuurt een weetje in voor het prikbord.
 *
 * Het komt niet meteen op het bord: het wacht tot Kim het ophangt (zie
 * /beheer/weetjes). De databank bewaakt dat ook zelf — de regel "ingelogd
 * weetje insturen" in supabase/weetjes.sql laat alleen rijen toe die nog niet
 * goedgekeurd zijn.
 */
export async function stuurWeetjeIn(formData: FormData) {
  const session = await getSessionProfile();
  if (!session) {
    redirect("/login?fout=" + encodeURIComponent("Log eerst in om een weetje in te sturen."));
  }

  const tekst = String(formData.get("tekst") || "").trim();
  const voornaam = String(formData.get("voornaam") || "").trim();
  const leeftijdRuw = String(formData.get("leeftijd") || "").trim();

  if (tekst.length < 3) {
    terug("Schrijf eerst je weetje op.");
  }
  if (tekst.length > 500) {
    terug("Dat weetje is wat lang. Hou het bij 500 tekens, dan past het op een briefje.");
  }

  // Alleen een voornaam, nooit meer. Wie zijn volledige naam invult, krijgt
  // enkel het eerste woord op het bord — een prikbord dat door iedereen te
  // lezen is, hoort geen achternamen van kinderen te dragen.
  const eersteNaam = voornaam.split(/\s+/)[0]?.slice(0, 40) || null;

  const leeftijd = Number(leeftijdRuw);
  const geldigeLeeftijd =
    leeftijdRuw && Number.isInteger(leeftijd) && leeftijd >= 3 && leeftijd <= 21 ? leeftijd : null;

  const supabase = await createClient();
  const { error } = await supabase.from("weetjes").insert({
    tekst,
    voornaam: eersteNaam,
    leeftijd: geldigeLeeftijd,
    profile_id: session.userId,
  });

  if (error) {
    console.error("weetje insturen mislukt:", error.message);
    terug(`Het insturen lukte niet. De melding luidt: ${error.message}`);
  }

  redirect("/weetjes?melding=bedankt");
}

function terug(bericht: string): never {
  redirect(`/weetjes?fout=${encodeURIComponent(bericht)}`);
}
