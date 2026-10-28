"use server";

import { redirect } from "next/navigation";
import { bewaarAanvragen, type NieuweAanvraag } from "@/lib/aanvragen-db";
import { kampRegels } from "@/content/kampen";
import { berekenPrijs, euro, kampVanDag } from "@/lib/kampprijs";

/*
  Een kampinschrijving van /kampen/inschrijven.

  Elk kind wordt een eigen aanvraag in de databank, met dezelfde vragen als
  het gewone inschrijfformulier ("Naam van het kind", "Hasselt maandag 2
  november": "ja"). Zo staat elk kind apart op de lijsten in het
  ouderportaal, met enkel zijn eigen dagen, en hoeft daar niets aan te
  veranderen. Wat voor het hele gezin geldt (het bedrag, de mededeling, de
  broers en zussen) staat bij elk kind.
*/

type KindIn = {
  voornaam?: string;
  achternaam?: string;
  leeftijd?: string;
  dagen?: string[];
};

const kort = (waarde: unknown, max = 200) =>
  String(waarde ?? "").trim().slice(0, max);

export async function kampInschrijven(formulier: FormData) {
  /* Het lokvakje voor robots: doen alsof alles lukte. */
  if (kort(formulier.get("adres")) !== "") redirect("/kampen/bedankt");

  let ruw: KindIn[] = [];
  try {
    const gelezen = JSON.parse(String(formulier.get("kinderen") ?? "[]"));
    if (Array.isArray(gelezen)) ruw = gelezen.slice(0, 8);
  } catch {
    redirect("/kampen/bedankt?fout=1");
  }

  const kinderen = ruw
    .map((k) => ({
      voornaam: kort(k.voornaam, 80),
      achternaam: kort(k.achternaam, 80),
      leeftijd: kort(k.leeftijd, 20),
      dagen: [...new Set((k.dagen ?? []).map((d) => kort(d)))].filter((d) =>
        kampVanDag(d),
      ),
    }))
    .filter((k) => k.voornaam && k.dagen.length > 0);

  const ouder = kort(formulier.get("ouder"));
  const email = kort(formulier.get("email"));
  const gsm = kort(formulier.get("gsm"), 40);
  if (!kinderen.length || !ouder || !email || !gsm) {
    redirect("/kampen/bedankt?fout=1");
  }

  const vt = formulier.get("vt") === "ja";
  const fotos = kort(formulier.get("fotos"), 40);
  const gemeente = kort(formulier.get("gemeente"), 80);
  const boodschap = kort(formulier.get("boodschap"), 2000);

  /* Wat nu betaald moet worden, en wat pas na bevestiging. */
  const nuKiezen = (bevestigen: boolean) =>
    kinderen.map((k) => ({
      dagen: k.dagen.filter(
        (d) => Boolean(kampVanDag(d)?.bevestigen) === bevestigen,
      ),
    }));
  const nu = berekenPrijs(nuKiezen(false), vt);
  const later = berekenPrijs(nuKiezen(true), vt);
  const wachtlijst = kinderen.some((k) =>
    k.dagen.some((d) => kampVanDag(d)?.volzet),
  );

  /* Een nummer, geen naam: de mededeling gaat ook in het webadres van de
     bedanktpagina, en daar hoort geen naam van een kind in. In Beheer zoek
     je de inschrijving terug op dit nummer. */
  const mededeling = `Kamp ${Math.floor(10000 + Math.random() * 90000)}`;

  const namen = kinderen.map((k) => `${k.voornaam} ${k.achternaam}`.trim());

  const rijen: NieuweAanvraag[] = kinderen.map((kind, i) => {
    const gegevens: Record<string, string> = {
      "Naam van het kind": namen[i],
      "Leeftijd van het kind": kind.leeftijd,
      "Naam van de ouders": ouder,
      Gemeente: gemeente,
      "Gsm-nummer": gsm,
      "E-mailadres": email,
      Aanbod: "Vakantiekampen",
      "Soort aanvraag": "Inschrijving",
    };
    for (const dag of kind.dagen) {
      gegevens[dag] = "ja";
      if (kampVanDag(dag)?.volzet) gegevens[`Wachtlijst ${dag}`] = "ja";
    }
    if (namen.length > 1) {
      gegevens["Broers en zussen in deze inschrijving"] = namen
        .filter((_, j) => j !== i)
        .join(", ");
    }
    if (vt) gegevens["Verhoogde tegemoetkoming"] = "ja, attest volgt";
    if (fotos) gegevens["Foto's"] = fotos;
    if (boodschap) gegevens["Vraag of boodschap"] = boodschap;
    gegevens["Te betalen voor het gezin"] = euro(nu.totaal);
    if (later.totaal > 0) {
      gegevens["Na bevestiging te betalen"] = euro(later.totaal);
    }
    gegevens["Mededeling"] = mededeling;
    gegevens["Akkoord met het gebruik van de gegevens"] = "ja";
    for (const sleutel of Object.keys(gegevens)) {
      if (!gegevens[sleutel]) delete gegevens[sleutel];
    }
    return { onderwerp: kampRegels.onderwerp, soort: "Inschrijving", gegevens };
  });

  const { fout } = await bewaarAanvragen(rijen);
  if (fout) redirect("/kampen/bedankt?fout=1");

  const zoek = new URLSearchParams({ bedrag: String(nu.totaal), code: mededeling });
  if (later.totaal > 0) zoek.set("later", String(later.totaal));
  if (wachtlijst) zoek.set("wacht", "1");
  if (vt) zoek.set("vt", "1");
  redirect(`/kampen/bedankt?${zoek.toString()}`);
}
