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

  // Hetzelfde weetje een tweede keer: dat is geen nieuw briefje.
  //
  // Febe stuurde op 8 oktober 2026 eenentwintig keer dezelfde zin in, omdat ze
  // hem op het bord wou krijgen en niet zag dat hij al binnen was. Nog eens
  // sturen helpt dus niet, en we zeggen dat nu ook. De databank bewaakt het
  // daarnaast zelf met een unieke index (supabase/weetjes-dubbel.sql): een
  // slot in deze functie alleen is nooit genoeg, want twee tabbladen of een
  // trage herlaadbeurt komen er langs.
  const { data: albinnen } = await supabase
    .from("weetjes")
    .select("tekst")
    .eq("profile_id", session.userId);

  if ((albinnen ?? []).some((w) => gelijk(w.tekst) === gelijk(tekst))) {
    redirect("/weetjes?melding=dubbel");
  }

  const { error } = await supabase.from("weetjes").insert({
    tekst,
    voornaam: eersteNaam,
    leeftijd: geldigeLeeftijd,
    profile_id: session.userId,
  });

  if (error) {
    // 23505 is de unieke index die hetzelfde weetje tegenhoudt. Dat is geen
    // storing maar precies wat de bedoeling is, dus het kind krijgt de gewone
    // boodschap te zien in plaats van een foutmelding.
    if (error.code === "23505") {
      redirect("/weetjes?melding=dubbel");
    }
    console.error("weetje insturen mislukt:", error.message);
    terug(`Het insturen lukte niet. De melding luidt: ${error.message}`);
  }

  redirect("/weetjes?melding=bedankt");
}

/**
 * Twee weetjes zijn hetzelfde als enkel hoofdletters of spaties verschillen.
 *
 * Dezelfde bewerking staat in de unieke index van supabase/weetjes-dubbel.sql.
 * Verandert de ene, verander dan ook de andere, anders houdt de databank iets
 * tegen waarvan deze functie denkt dat het nieuw is.
 */
function gelijk(tekst: string) {
  return tekst.trim().replace(/\s+/g, " ").toLowerCase();
}

function terug(bericht: string): never {
  redirect(`/weetjes?fout=${encodeURIComponent(bericht)}`);
}

/**
 * Een kind verbetert zijn eigen briefje en stuurt het opnieuw in.
 *
 * Kim vroeg dit op 27 september 2026: "zodat we het samen kunnen aanpassen".
 * Een briefje dat niet geplaatst werd, is dus geen eindpunt maar een vraag om
 * het nog eens te proberen. Het gaat daarna gewoon weer op de stapel wachten.
 *
 * Ophangen blijft iets wat alleen de beheerder doet: de regel "eigen weetje
 * verbeteren" in supabase/weetjes-bericht.sql laat `goedgekeurd` niet toe om
 * van false naar true te gaan.
 */
export async function verbeterWeetje(formData: FormData) {
  const session = await getSessionProfile();
  if (!session) {
    redirect("/login?fout=" + encodeURIComponent("Log eerst in om je weetje aan te passen."));
  }

  const id = String(formData.get("id") || "");
  const tekst = String(formData.get("tekst") || "").trim();

  if (tekst.length < 3) {
    terug("Schrijf eerst je weetje op.");
  }
  if (tekst.length > 500) {
    terug("Dat weetje is wat lang. Hou het bij 500 tekens, dan past het op een briefje.");
  }

  const supabase = await createClient();
  const { error } = await supabase
    .from("weetjes")
    .update({ tekst, niet_geplaatst: false, bericht: null })
    .eq("id", id)
    // Dubbel op slot: de databank bewaakt dit ook, maar zo staat hier zwart op
    // wit dat je enkel je eigen briefje kan aanpassen.
    .eq("profile_id", session.userId)
    .eq("goedgekeurd", false);

  if (error) {
    // Hetzelfde geval als bij het insturen: de unieke index houdt tegen dat
    // dit briefje woord voor woord hetzelfde wordt als een ander van jezelf.
    if (error.code === "23505") {
      redirect("/weetjes?melding=dubbel");
    }
    console.error("weetje verbeteren mislukt:", error.message);
    terug(`Het aanpassen lukte niet. De melding luidt: ${error.message}`);
  }

  redirect("/weetjes?melding=opnieuw");
}
