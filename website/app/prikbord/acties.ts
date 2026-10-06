"use server";

import { redirect } from "next/navigation";
import { borden } from "@/content/prikbord";
import { bewaarBriefje, meldBriefje } from "@/lib/prikbord-db";

/*
  Wat er gebeurt als iemand op "Ophangen" of op "Melden" klikt.

  Beide werken ook zonder javascript: het zijn gewone formulieren die naar
  de server gaan. Na afloop stuurt de server je terug naar het bord, met
  een kort bericht bovenaan.
*/

const MAX_TEKST = 600;

function terug(pad: string, bericht: string): never {
  redirect(`${pad}?melding=${bericht}`);
}

/*
  Waar iemand na het ophangen of melden weer terechtkomt. Wie op het
  overzicht bezig was, blijft op het overzicht; wie op een bord bezig was,
  blijft op dat bord. Het formulier zegt dat in een verborgen veldje, en we
  aanvaarden alleen die twee adressen.
*/
function waarheen(formulier: FormData, bord: string) {
  const gevraagd = String(formulier.get("terug") ?? "");
  if (gevraagd === "/prikbord") return "/prikbord";
  return `/prikbord/${bord}`;
}

export async function briefjeOphangen(formulier: FormData) {
  const bord = String(formulier.get("bord") ?? "");
  if (!borden.some((b) => b.slug === bord)) redirect("/prikbord");
  const pad = waarheen(formulier, bord);

  /*
    Een verborgen veld dat een mens nooit invult. Vult een robot het wel in,
    dan doen we alsof alles goed ging en hangen we niets op.
  */
  if (String(formulier.get("adres") ?? "").trim() !== "") {
    terug(pad, "opgehangen");
  }

  const tekst = String(formulier.get("tekst") ?? "").trim();
  const naam = String(formulier.get("naam") ?? "").trim();
  const volledigeNaam = String(formulier.get("volledigeNaam") ?? "").trim();
  const contact = String(formulier.get("contact") ?? "").trim();
  const wanneer = String(formulier.get("wanneer") ?? "").trim();

  if (tekst.length < 2 || tekst.length > MAX_TEKST) terug(pad, "tekst");
  if (naam.length < 2 || naam.length > 60) terug(pad, "naam");
  if (volledigeNaam.length < 2 || volledigeNaam.length > 120)
    terug(pad, "naam");
  if (!contact.includes("@") || contact.length > 120) terug(pad, "mail");

  const { fout } = await bewaarBriefje({
    bord,
    tekst,
    naam,
    volledigeNaam,
    contact,
    wanneer: wanneer || null,
  });
  if (fout) terug(pad, "mislukt");

  terug(pad, "opgehangen");
}

export async function briefjeMeldenActie(formulier: FormData) {
  const bord = String(formulier.get("bord") ?? "");
  const briefjeId = String(formulier.get("briefjeId") ?? "");
  const reden = String(formulier.get("reden") ?? "")
    .trim()
    .slice(0, 400);

  if (!borden.some((b) => b.slug === bord) || !briefjeId) redirect("/prikbord");
  const pad = waarheen(formulier, bord);

  const { fout } = await meldBriefje(briefjeId, reden);
  if (fout) terug(pad, "mislukt");

  terug(pad, "gemeld");
}
