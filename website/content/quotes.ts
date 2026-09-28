/*
  Wat ouders over ons zeggen.

  Kim vroeg dit op 28 september 2026: persoonlijke quotes doen meer dan eender
  welke tekst die wij zelf schrijven. Een ouder die twijfelt, leest liever een
  zin van een andere ouder dan onze eigen beloftes.

  Een quote bijzetten? Plak hem hieronder in de lijst, tussen accolades:

    {
      tekst: "De zin zoals de ouder hem schreef.",
      naam: "Voornaam",
      wat: "mama van een kind in de plusklas",
    },

  Drie afspraken, en die zijn belangrijk:

    1. Enkel de VOORNAAM. Nooit de volledige naam, nooit de naam van het kind,
       nooit de school. Dat is wat we de ouders beloofd hebben.
    2. Enkel met toestemming. Zet er niets in wat een ouder niet uitdrukkelijk
       heeft laten zetten. Vraagt iemand later om het weg te halen, dan schrap
       je de regels en is het meteen weg.
    3. Verander de woorden van de ouder niet. Een tikfout mag je rechtzetten en
       je mag een te lang stuk inkorten, maar herschrijven doen we niet. Precies
       omdat het niet klinkt als reclame, gelooft een lezer het.

  Staat de lijst leeg, dan verdwijnt het hele blok vanzelf van de website. Je
  hoeft dus niets uit te zetten tot je de eerste quote hebt.
*/

export type Quote = {
  tekst: string;
  naam: string;
  wat?: string;
};

export const quotesTekst = {
  label: "Wat ouders zeggen",
  titel: "In hun eigen woorden",
  tekst:
    "Ouders die hier al langer komen, vertellen het beter dan wij. Dit zijn hun woorden, met enkel hun voornaam erbij.",
};

export const quotes: Quote[] = [];
