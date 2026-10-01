"use server";

import { redirect } from "next/navigation";
import { kanalen } from "@/content/inkijker";
import { bewaarPost } from "@/lib/inkijker-db";

/*
  Wat er gebeurt als iemand zijn bericht instuurt.

  Het werkt ook zonder javascript: het is een gewoon formulier dat naar de
  server gaat. Na afloop sta je terug op de pagina, met een kort bericht
  bovenaan. Het ingestuurde bericht is nog niet zichtbaar; dat gebeurt pas
  als wij het goedkeuren in het ouderportaal.
*/

const MAX_TEKST = 600;

function terug(bericht: string): never {
  redirect(`/in-de-kijker?melding=${bericht}#insturen`);
}

export async function postInsturen(formulier: FormData) {
  /*
    Een verborgen veld dat een mens nooit invult. Vult een robot het wel in,
    dan doen we alsof alles goed ging en bewaren we niets.
  */
  if (String(formulier.get("adres") ?? "").trim() !== "") {
    terug("gelukt");
  }

  const link = String(formulier.get("link") ?? "").trim();
  const tekst = String(formulier.get("tekst") ?? "").trim();
  const van = String(formulier.get("van") ?? "").trim();
  const titel = String(formulier.get("titel") ?? "").trim();
  const kanaal = String(formulier.get("kanaal") ?? "anders").trim();
  const volledigeNaam = String(formulier.get("volledigeNaam") ?? "").trim();
  const contact = String(formulier.get("contact") ?? "").trim();

  if (!link.startsWith("https://") || link.length > 400) terug("link");
  if (tekst.length < 2 || tekst.length > MAX_TEKST) terug("tekst");
  if (van.length < 2 || van.length > 80) terug("naam");
  if (volledigeNaam.length < 2 || volledigeNaam.length > 120) terug("naam");
  if (!contact.includes("@") || contact.length > 120) terug("mail");

  const { fout } = await bewaarPost({
    titel: titel ? titel.slice(0, 120) : null,
    tekst,
    van,
    kanaal: kanaal in kanalen ? kanaal : "anders",
    link,
    volledigeNaam,
    contact,
  });
  if (fout) terug("mislukt");

  terug("gelukt");
}
