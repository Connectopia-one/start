/*
  Wat ouders en kinderen over ons zeggen.

  Kim vroeg dit op 28 september 2026: persoonlijke quotes doen meer dan eender
  welke tekst die wij zelf schrijven. Een ouder die twijfelt, leest liever een
  zin van een andere ouder dan onze eigen beloftes. En een zin van een kind
  zelf doet nog iets anders: die laat zien hoe het voelt om hier te zijn.

  De twee staan bewust door elkaar. Zo leest een bezoeker afwisselend het
  verhaal van een ouder en dat van een kind, en dat versterkt elkaar.

  Een quote bijzetten? Plak hem hieronder in de lijst, tussen accolades:

    {
      tekst: "De zin zoals hij geschreven of gezegd is.",
      naam: "Voornaam",
      wat: "mama van een kind dat meeging op kamp",
      van: "ouder",
    },

  Bij "van" zet je "ouder" of "kind". Laat je het weg, dan gaat het over een
  ouder. Een quote van een kind krijgt vanzelf een andere kleur en een
  wolkje ervoor, zodat je meteen ziet wie aan het woord is.

  Bij "wat" zet je bij welke werking die persoon ons kent. Zo ziet een lezer
  meteen dat we meer doen dan één ding:

    Bij een ouder:
      mama van een kind dat meeging op kamp
      papa van een kind bij Young Engineers
      mama van een kind in de plusklas
      papa van een kind in de pluswerking op zaterdag
      mama van een gezin dat het oefenplatform test

    Bij een kind:
      9 jaar, was mee op kamp
      11 jaar, komt naar de plusklas
      8 jaar, bouwt bij Young Engineers

  Meng ze ook echt. Staan er straks vijf quotes over de plusklas, dan lijkt
  het alsof we enkel dat doen, terwijl er veel meer kinderen op kamp en bij
  Young Engineers komen.

  Drie afspraken, en die zijn belangrijk:

    1. Enkel de VOORNAAM. Nooit de volledige naam, nooit de naam van het kind
       van een ouder, nooit de school. Dat is wat we de ouders beloofd hebben.
       Bij een kind mag de leeftijd erbij, meer niet.
    2. Enkel met toestemming. Bij een kind geeft de ouder die toestemming, ook
       al zijn het de woorden van het kind. Vraagt iemand later om het weg te
       halen, dan schrap je de regels en is het meteen weg.
    3. Verander de woorden niet. Een tikfout mag je rechtzetten en je mag een
       te lang stuk inkorten, maar herschrijven doen we niet. Bij een kind laat
       je de kindertaal juist staan: precies daarom gelooft een lezer het.

  Staat de lijst leeg, dan verdwijnt het hele blok vanzelf van de website. Je
  hoeft dus niets uit te zetten tot je de eerste quote hebt.
*/

export type Quote = {
  tekst: string;
  naam: string;
  wat?: string;
  van?: "ouder" | "kind";
};

export const quotesTekst = {
  label: "Wat ouders en kinderen zeggen",
  titel: "In hun eigen woorden",
  tekst:
    "Ouders en kinderen die hier al langer komen, vertellen het beter dan wij. Dit zijn hun woorden, met enkel hun voornaam erbij.",
};

export const quotes: Quote[] = [];
