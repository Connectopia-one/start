/*
  De pagina "Handig materiaal" — /materiaal

  Een gratis verzamelplek voor links naar bestaand online materiaal: vakfiches,
  naslagwerken, interactieve tabellen, oefensites. Iedereen kan die pagina zien,
  ook wie geen account heeft en wie niet betaald heeft. Dat is met opzet: het is
  een extra dienst, geen onderdeel van het betalende aanbod.

  Een link toevoegen doe je hieronder, en je hoeft er geen code voor te kennen.
  Zet een nieuwe regel bij de juiste groep:

      { titel: "Naam van de site", link: "https://...", omschrijving: "Wat je er vindt." },

  Alleen titel en link zijn verplicht. Een groep zonder links verdwijnt vanzelf
  van de pagina, dus je mag een lege groep gerust laten staan tot je ze vult.

  Een nieuwe groep maken mag ook: kopieer een blok met kop, uitleg en linken.
*/

export type MateriaalLink = {
  titel: string;
  /* De volledige webstek, dus mét https:// ervoor. */
  link: string;
  /* Eén zin over wat je er vindt. Mag je weglaten. */
  omschrijving?: string;
  /* Zet dit op true als de link enkel over één niveau gaat, bv. "vanaf 1ste middelbaar". */
  opmerking?: string;
};

export type MateriaalGroep = {
  kop: string;
  /* Eén zin onder de kop. Mag je weglaten. */
  uitleg?: string;
  linken: MateriaalLink[];
};

export const materiaalTekst = {
  label: "Handig materiaal",
  titel: "Links die we zelf gebruiken",
  intro:
    "Hier verzamelen we online materiaal dat ons en onze kinderen verder helpt: officiële vakfiches, naslagwerken, interactieve tabellen en oefensites. Alles op deze pagina is gratis te gebruiken en staat los van een account of een abonnement.",
  nota:
    "Deze lijst groeit mee. Ken je iets wat hier thuishoort, of werkt een link niet meer? Laat het ons weten, dan zetten we het erbij.",
  /* Wat er staat zolang een groep nog geen enkele link heeft. */
  leegTekst: "Hier komt binnenkort materiaal bij.",
  /* De knop onderaan. Laat de link leeg om de knop te verbergen. */
  oproepTekst: "Een link doorgeven",
  oproepLink: "https://www.connectopia.one/contact",
  /* Waarschuwing bij het verlaten van ons platform. */
  externNota:
    "Deze links brengen je naar websites van anderen. Wij maken of beheren dat materiaal niet, en er kan reclame op staan.",
};

export const materiaalGroepen: MateriaalGroep[] = [
  {
    kop: "Officiële leerstof",
    uitleg: "Wat de overheid en de examencommissie zelf publiceren: wat moet je kennen en kunnen.",
    linken: [],
  },
  {
    kop: "Wiskunde",
    linken: [],
  },
  {
    kop: "Wetenschap en techniek",
    uitleg: "Onder meer de interactieve periodieke tabel.",
    linken: [],
  },
  {
    kop: "Talen",
    linken: [],
  },
  {
    kop: "Mens en maatschappij",
    uitleg: "Geschiedenis, aardrijkskunde en burgerschap.",
    linken: [],
  },
  {
    kop: "Oefenen en spelen",
    uitleg: "Sites waar je gewoon aan de slag kan.",
    linken: [],
  },
];
