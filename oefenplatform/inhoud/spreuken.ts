/**
 * De spreuken die onderaan elke pagina staan.
 *
 * Aanpassen vraagt geen code: zet een regel bij, haal er een weg, of verander
 * de tekst. `van` mag je weglaten als er geen bron bij hoort.
 *
 * Welke spreuk op welke pagina komt, volgt uit het adres van die pagina. Zo
 * staat op elke pagina een andere, en blijft ze daar ook staan — geen tekst
 * die onder je ogen verspringt terwijl je aan het lezen bent.
 *
 * Dezelfde lijst staat ook in de website, in website/content/spreuken.ts.
 * Wie hier iets verandert, verandert het daar dus best ook.
 */

export type Spreuk = {
  tekst: string;
  van?: string;
};

export const SPREUKEN: Spreuk[] = [
  { tekst: "Ik heb het nog nooit gedaan, dus ik denk dat ik het wel kan." },
  { tekst: "Als je niet weet waar je heen gaat, brengt elke weg je er wel." },
  { tekst: "Het lijkt altijd onmogelijk, tot het gedaan is." },
  {
    tekst:
      "Onderwijs is niet het leren van feiten, maar het trainen van de geest om na te denken.",
    van: "Albert Einstein",
  },
  { tekst: "Het is wat we denken al te weten dat ons ervan weerhoudt om bij te leren." },
  { tekst: "Leren put de geest nooit uit.", van: "Leonardo da Vinci" },
];
