/*
  Sponsors en samenwerkingen op de startpagina.

  Een logo toevoegen: zet het bestand in de map  public/sponsors/
  en voeg hieronder een regel toe met de bestandsnaam.
  Heb je nog geen logo? Laat "logo" weg, dan toont de site de naam in tekst.
*/

export type Sponsor = {
  naam: string;
  logo?: string;
  link?: string;
};

export const sponsorsTekst = {
  label: "Mogelijk gemaakt door",
  titel: "Onze sponsors en samenwerkingen",
  tekst:
    "De organisaties, scholen en bedrijven die Connectopia mee mogelijk maken. Elk logo linkt door naar hun eigen pagina.",
  oproep: "Samenwerken met Connectopia?",
  oproepLink: "/over-ons#contact",
};

export const sponsors: Sponsor[] = [
  {
    naam: "Noduss Events",
    logo: "noduss-events.png",
    // link: "https://www.noduss.be",
  },
  {
    naam: "Velleman",
    logo: "velleman.jpg",
    link: "https://www.velleman.eu",
  },
];
