/*
  Febe meldde op 5 oktober 2026 dat het scherm zichzelf tegensprak. Bij de
  stelling "Het jaar 2000 was het eerste jaar van de 21ste eeuw" antwoordde ze
  terecht niet waar. Bovenaan kwam "Juist!" te staan, want haar antwoord klopte,
  en daar meteen onder "Niet juist.", want zo begon de uitleg over de stelling.
  Twee keer hetzelfde woord, twee keer over iets anders.

  Het woordje vooraan de uitleg is een oordeel over de stelling, en dat oordeel
  staat al op het scherm. Dus halen we het weg, maar alleen als het een eigen
  zin is: "Niet juist. Het jaar 2000 hoorde nog bij de 20ste eeuw" wordt
  "Het jaar 2000 hoorde nog bij de 20ste eeuw". Staat er een komma of een
  dubbele punt achter, dan loopt de zin door ("Klopt, want dan kan je zelf gaan
  kijken") en zou weghalen de zin stukmaken; die laten we staan.
*/

const OORDEEL =
  /^(niet juist|niet waar|dat klopt niet|klopt niet|dat klopt|klopt|juist|waar|correct|inderdaad)[.!]\s+(?=[A-ZÀ-ÖØ-Þ“"'(0-9])/i;

/** De uitleg zonder het oordeel vooraan, dat elders al op het scherm staat. */
export function zonderOordeel(uitleg: string): string {
  const schoon = uitleg.replace(OORDEEL, "");
  // Nooit een lege uitleg teruggeven: dan stond er iets anders dan een oordeel.
  return schoon.trim() === "" ? uitleg : schoon;
}

/** Wat er over de stelling zelf waar is, in één zin. */
export function stellingZin(antwoord: boolean): string {
  return antwoord ? "De stelling is waar." : "De stelling is niet waar.";
}
