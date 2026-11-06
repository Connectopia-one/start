"use server";

import { redirect } from "next/navigation";
import { bewaarAanvraag } from "@/lib/aanvragen-db";
import { SPAM_REDEN, SPAM_VOORVOEGSEL, spamRedenen } from "@/lib/spamcheck";

/*
  Wat er gebeurt als iemand een formulier van de website verstuurt.

  Dit is een gewoon formulier dat naar de server gaat, dus het werkt ook
  zonder javascript en zonder mailprogramma. Na afloop belandt de bezoeker
  op /bedankt.

  De antwoorden gaan als één geheel de databank in. De namen van de vakjes
  op het formulier zijn de vragen zoals de bezoeker ze gelezen heeft
  ("Naam van het kind"), dus wat hier bewaard wordt leest als een gesprek
  en niet als een tabel met codes.
*/

/*
  Vakjes die er wel op het formulier staan maar niet tussen de antwoorden
  thuishoren: het lokvakje voor robots, en de twee die in een eigen kolom
  belanden. "Soort aanvraag" is het verborgen vakje dat al op het formulier
  stond en dat zegt waarover het gaat ("Terugbelverzoek", "Professional").
*/
const NIET_BEWAREN = new Set([
  "adres",
  "website",
  "onderwerp",
  "soort",
  "Soort aanvraag",
]);

const MAX_LENGTE = 2000;

export async function aanvraagVersturen(formulier: FormData) {
  /*
    Een verborgen vakje dat een mens nooit invult. Vult een robot het wel in,
    dan doen we alsof alles goed ging en bewaren we niets.
  */
  if (String(formulier.get("adres") ?? "").trim() !== "") {
    redirect("/bedankt");
  }

  const onderwerp = String(formulier.get("onderwerp") ?? "").trim();
  const soort =
    String(formulier.get("soort") ?? "").trim() ||
    String(formulier.get("Soort aanvraag") ?? "").trim() ||
    "aanvraag";
  if (!onderwerp) redirect("/bedankt?fout=1");

  const gegevens: Record<string, string> = {};
  for (const [naam, waarde] of formulier.entries()) {
    if (typeof waarde !== "string") continue;
    if (NIET_BEWAREN.has(naam)) continue;
    const schoon = waarde.trim().slice(0, MAX_LENGTE);
    if (schoon) gegevens[naam.slice(0, 200)] = schoon;
  }

  if (!Object.keys(gegevens).length) redirect("/bedankt?fout=1");

  /*
    Lijkt het op reclame van een robot (zie lib/spamcheck.ts), dan bewaren we
    het toch, maar als "spam: ..." met de reden erbij. Het ouderportaal zet
    het op het tabblad Spam, weg van de echte aanvragen. Zo gaat er nooit
    een echte aanvraag verloren, en krijgt de bezoeker gewoon /bedankt.
  */
  const redenen = spamRedenen(gegevens, String(formulier.get("website") ?? ""));
  const isSpam = redenen.length > 0;
  if (isSpam) gegevens[SPAM_REDEN] = redenen.join("; ");

  const { fout } = await bewaarAanvraag({
    onderwerp,
    soort: isSpam ? (SPAM_VOORVOEGSEL + soort).slice(0, 40) : soort,
    gegevens,
  });
  if (fout) redirect("/bedankt?fout=1");

  redirect("/bedankt");
}
