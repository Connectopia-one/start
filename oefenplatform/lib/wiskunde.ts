/*
  Wiskundige notatie in een vraag, een optie, een uitleg of een leerbundel.

  Waarom dit bestaat: Enya Vermeyen, leerkracht wiskunde, keek op 10 oktober
  2026 naar het gratis hoofdstuk over machtswortels, machten en logaritmen in
  de derde graad doorstroom en schreef:

    "Inhoudelijk ziet het er op het eerste zicht wel oké uit, maar het is
     allemaal in woorden, zonder wiskundige notatie. Leerlingen moeten echter
     wiskundige notatie correct leren lezen en gebruiken. Dit is dus totaal
     ongeschikt voor mijn doeleinden als leerkracht wiskunde. (...) zal je toch
     een manier moeten vinden om formules weer te geven op je website. In de
     praktijk gebeurt dit vaak via LaTeX velden."

  Ze heeft gelijk, en niet alleen voor de leerkracht: "a tot de macht één
  derde" is geen wiskunde, het is een omschrijving van wiskunde. Een leerling
  van de derde graad moet a^(1/3) kunnen lezen.

  HOE JE HET SCHRIJFT

  Een formule staat tussen \( en \), de gewone LaTeX-markering voor een formule
  in een lopende zin:

      De vereenvoudigde vorm van \(\sqrt{50}\) is \(5\sqrt{2}\).

  Staat ze op haar eigen regel, gebruik dan \[ en \]:

      \[\log_a(x \cdot y) = \log_a x + \log_a y\]

  In een json-bestand wordt elke backslash verdubbeld, dus daar lees je
  "\\(\\sqrt{50}\\)". In een python-bronbestand schrijf je een rauwe string:
  r"\(\sqrt{50}\)". De bouwscripts zetten dat vanzelf juist in de json.

  WAAROM \( EN NIET $

  Omdat $ al in de inhoud staat: de Excel-bundels leggen uit wat $C2 en C$2
  doen. Twee van die dollartekens op één bladzijde zouden als een formule
  gelezen worden en de tekst ertussen opvreten. \( en \) komen nergens anders
  voor en zijn even standaard.

  WAT HET NIET DOET

  Een formule vervangt de zin niet. Wie de formule niet ziet — een schermlezer,
  de pagina waar een ouder meekijkt, een melding per mail — moet de vraag nog
  altijd kunnen begrijpen. Schrijf dus "Vereenvoudig \(\sqrt{50}\)" en niet
  "Vereenvoudig dit: \(\sqrt{50}\)" waarin het woordje "dit" al het werk doet.
*/

export type WisStuk =
  | { soort: "tekst"; tekst: string }
  | { soort: "formule"; latex: string; blok: boolean };

/*
  \[ ... \] eerst, anders zou \( ... \) de binnenkant van een blokformule
  kunnen oppikken. De s-vlag niet nodig: een formule mag over meerdere regels
  lopen omdat [^] alles pakt, maar we houden het bewust simpel met [\s\S].
*/
const FORMULE = /\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)/g;

/** Staat er een formule in deze tekst? Zo niet, dan hoeft KaTeX niet te laden. */
export function bevatWiskunde(tekst: string | null | undefined): boolean {
  if (!tekst) return false;
  return tekst.includes("\\(") || tekst.includes("\\[");
}

/** Hakt een tekst in stukken gewone tekst en stukken formule. */
export function splitsWiskunde(tekst: string): WisStuk[] {
  const stukken: WisStuk[] = [];
  let vorige = 0;
  for (const m of tekst.matchAll(FORMULE)) {
    if (m.index > vorige) {
      stukken.push({ soort: "tekst", tekst: tekst.slice(vorige, m.index) });
    }
    vorige = m.index + m[0].length;
    const blok = m[1] !== undefined;
    stukken.push({ soort: "formule", latex: (m[1] ?? m[2]).trim(), blok });
  }
  if (vorige < tekst.length) {
    stukken.push({ soort: "tekst", tekst: tekst.slice(vorige) });
  }
  return stukken;
}

/*
  De tekst zonder de markeringen, voor waar geen opmaak mogelijk is: een
  aria-label, de tekst van een melding, een zoekveld. De formule blijft staan
  zoals ze geschreven is, want dat is nog altijd leesbaarder dan niets.
*/
export function zonderFormules(tekst: string): string {
  return splitsWiskunde(tekst)
    .map((s) => (s.soort === "tekst" ? s.tekst : s.latex))
    .join("")
    .replace(/\s+/g, " ")
    .trim();
}
