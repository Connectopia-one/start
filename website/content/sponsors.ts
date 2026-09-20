/*
  Sponsors en samenwerkingen op de startpagina.

  soort: "sponsor" of "partner". Sponsors en samenwerkingen krijgen elk hun
         eigen rijtje, met een kopje erboven.

  Een logo toevoegen: zet het bestand in de map  public/sponsors/
  en vul hieronder de bestandsnaam in bij "logo". Heb je nog geen logo?
  Laat "logo" weg, dan toont de site gewoon de naam.

  toelichting is optioneel en komt in het klein onder de naam te staan.
*/

export type Sponsor = {
  naam: string;
  soort: "sponsor" | "partner";
  logo?: string;
  link?: string;
  toelichting?: string;
};

export const sponsorsTekst = {
  label: "Mogelijk gemaakt door",
  titel: "Onze sponsors en samenwerkingen",
  tekst:
    "De organisaties, scholen en bedrijven die Connectopia mee mogelijk maken. Staat er een logo met een link bij, dan kom je op hun eigen pagina terecht.",
  kopSponsors: "Sponsors",
  kopPartners: "Samenwerkingen",
  oproep: "Samenwerken met Connectopia?",
  oproepLink: "/contact",
};

export const sponsors: Sponsor[] = [
  {
    naam: "Noduss Events",
    soort: "sponsor",
    logo: "noduss-events.png",
  },
  {
    naam: "Velleman",
    soort: "sponsor",
    logo: "velleman.jpg",
    link: "https://www.velleman.eu",
  },
  {
    naam: "Atheneum Hasselt",
    soort: "partner",
    logo: "atheneum-hasselt.png",
  },
  {
    naam: "Level X 28",
    soort: "partner",
    logo: "level-x28.png",
    toelichting: "Hasselt",
  },
  {
    naam: "T2 Campus",
    soort: "partner",
    logo: "t2-campus.png",
    toelichting: "Genk",
  },
  {
    naam: "Technologiebende",
    soort: "partner",
    logo: "technologiebende.png",
  },
  {
    naam: "Educathor",
    soort: "partner",
    logo: "educathor.png",
  },
];

export const sponsorsPerSoort = (soort: Sponsor["soort"]) =>
  sponsors.filter((s) => s.soort === soort);
