/*
  Blogberichten.
  Een nieuw bericht schrijven? Voeg onderaan een blok toe.
  De nieuwste datum komt vanzelf bovenaan.

  datum: schrijf als "2026-09-20" (jaar-maand-dag)
  auteur: "Connectopia" of de naam van de partner die het schreef
*/

export type Bericht = {
  slug: string;
  titel: string;
  datum: string;
  auteur: string;
  samenvatting: string;
  tekst: string[];
};

export const blogTekst = {
  label: "Blog, tips en meer",
  titel: "Wat we leren, delen we",
  tekst:
    "Artikels van ons team en van externe partners, over opvoeden, school, diagnoses en alles wat ouders bezighoudt.",
  leegTekst: "Het eerste bericht staat er binnenkort aan te komen.",
};

export const berichten: Bericht[] = [
  {
    slug: "officieel-een-vzw",
    titel: "Officieel een vzw, en dat vieren we samen met jullie",
    datum: "2026-09-04",
    auteur: "Connectopia",
    samenvatting:
      "Vanaf schooljaar 2026–2027 zijn we niet alleen officieel een vzw, we verlagen ook onze prijzen.",
    tekst: [
      "Vanaf schooljaar 2026–2027 zijn we niet alleen officieel een vzw, we verlagen ook onze prijzen. Zo maken we plaats voor nog meer nieuwsgierige kinderen die net dat beetje extra uitdaging, begrip of ruimte nodig hebben.",
      "De plusklas kost voortaan 50 euro per dag in plaats van 60, een pluswerking 25 euro per drie uur in plaats van 30, en een les Young Engineers 20 euro in plaats van 25.",
      "Bedankt aan iedereen die dit mee mogelijk maakt. Samen bouwen we aan een toekomst vol mogelijkheden.",
    ],
  },
];

export const berichtenOpDatum = [...berichten].sort((a, b) =>
  b.datum.localeCompare(a.datum),
);
