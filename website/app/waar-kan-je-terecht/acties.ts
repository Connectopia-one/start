"use server";

import { redirect } from "next/navigation";
import { bewaarAanmelding } from "@/lib/gids-db";

/*
  Wat er gebeurt als iemand een organisatie aanbrengt voor de gids.

  Het werkt ook zonder javascript: het is een gewoon formulier dat naar de
  server gaat. Na afloop sta je terug op de pagina, met een kort bericht
  boven het formulier. De organisatie staat nog niet in de gids; dat gebeurt
  pas als wij ze goedkeuren in het ouderportaal.
*/

function terug(bericht: string): never {
  redirect(`/waar-kan-je-terecht?melding=${bericht}#aanbrengen`);
}

export async function organisatieAanbrengen(formulier: FormData) {
  /* Een verborgen veld dat een mens nooit invult. */
  if (String(formulier.get("adres") ?? "").trim() !== "") {
    terug("gelukt");
  }

  const naam = String(formulier.get("naam") ?? "").trim();
  const omschrijving = String(formulier.get("omschrijving") ?? "").trim();
  const regio = String(formulier.get("regio") ?? "").trim();
  let link = String(formulier.get("link") ?? "").trim();
  const wie = formulier.get("wie") === "iemand" ? "iemand" : "zelf";
  const volledigeNaam = String(formulier.get("volledigeNaam") ?? "").trim();
  const contact = String(formulier.get("contact") ?? "").trim();

  /* Wie "www.iets.be" intypt, bedoelt https://www.iets.be. */
  if (link && !/^https?:\/\//i.test(link)) link = `https://${link}`;
  link = link.replace(/^http:\/\//i, "https://");

  if (naam.length < 2 || naam.length > 120) terug("naam");
  if (omschrijving.length < 10 || omschrijving.length > 400) terug("omschrijving");
  if (link.length > 400) terug("link");
  if (volledigeNaam.length < 2 || volledigeNaam.length > 120) terug("jouwnaam");
  if (!contact.includes("@") || contact.length > 120) terug("mail");

  const { fout } = await bewaarAanmelding({
    naam,
    omschrijving,
    regio: regio ? regio.slice(0, 80) : null,
    link: link || null,
    wie,
    volledigeNaam,
    contact,
  });
  if (fout) terug("mislukt");

  terug("gelukt");
}
