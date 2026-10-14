/**
 * Bij welke vakken hoort er een rekenmachine bij het examen?
 *
 * Kim meldde op 14 oktober 2026: "is er ook geen rekenmachine beschikbaar bij
 * de examens. Wat ook hinderlijk is." Op het examen van de Examencommissie
 * mag er voor de rekenvakken een rekenmachine op de tafel liggen, dus hoort
 * er hier ook een. Bij Frans of geschiedenis staat ze alleen maar in de weg.
 *
 * De vergelijking gaat op de volledige slug of op het stuk voor het eerste
 * streepje, zodat wiskunde-basis en wiskunde-gevorderd meekomen zonder dat ze
 * hier apart moeten staan.
 */
const REKENVAKKEN = [
  "wiskunde",
  "natuurwetenschappen",
  "fysica",
  "chemie",
  "biologie",
  "statistiek",
  "economie",
  "toegepaste-economie",
  "economie-en-bedrijfswetenschappen",
  "samenleving-en-economie",
  "sociale-en-gedragswetenschappen",
  "gezondheid-zorg-en-welzijn",
  "aardrijkskunde",
  "techniek",
];

export function isRekenvak(slug: string | null | undefined): boolean {
  if (!slug) return false;
  const kaal = slug.toLowerCase();
  return REKENVAKKEN.some((vak) => kaal === vak || kaal.startsWith(vak + "-"));
}
