/*
  De gids "Waar kan je terecht".
  Elke organisatie is één regel. Voeg er gerust bij zodra je ze kent.

  categorie: gebruik dezelfde naam voor organisaties die bij elkaar horen,
             dan komen ze samen onder één kopje te staan.
*/

export type Organisatie = {
  naam: string;
  categorie: string;
  /* Eén of twee zinnen over wat ze doen. Laat leeg zolang je die nog niet hebt. */
  omschrijving?: string;
  regio?: string;
  link?: string;
};

export const gidsTekst = {
  label: "Waar kan je terecht",
  titel: "Diensten en organisaties die we kennen",
  tekst:
    "Van psycholoog en logopedist tot bijlesleerkracht met kennis van hoogbegaafdheid, ook bij dubbele diagnoses. We verwijzen alleen door naar mensen en organisaties waar we zelf vertrouwen in hebben.",
  nota:
    "Deze gids groeit mee. Ken je iemand die hier hoort, of wil je er zelf in staan? Laat het ons weten.",
  oproepTekst: "Een organisatie aanbrengen",
  oproepLink: "/over-ons#contact",
  leegTekst:
    "We zijn deze lijst nog aan het opbouwen. Heb je een concrete vraag? Stel ze gerust, dan verwijzen we je persoonlijk door.",
  /* Staat onder een partner waar we de omschrijving nog moeten aanvullen. */
  nogGeenOmschrijving: "Meer uitleg volgt binnenkort.",
};

export const organisaties: Organisatie[] = [
  {
    naam: "CLB van de school",
    categorie: "Eerste stap",
    omschrijving:
      "Gratis eerste aanspreekpunt bij twijfels over leren, gedrag of welbevinden. Kan screenen en doorverwijzen.",
    regio: "Overal",
  },
  {
    naam: "Huisarts",
    categorie: "Eerste stap",
    omschrijving:
      "Vertrekpunt voor doorverwijzing naar een psycholoog, kinderarts of centrum, en voor terugbetalingen.",
    regio: "Overal",
  },

  /*
    Partners die Kim doorgaf op 20 september 2026.
    De omschrijvingen en de websites moeten hier nog bij; vul ze aan zodra je
    ze hebt, dan verdwijnt de regel "Meer uitleg volgt binnenkort" vanzelf.
  */
  {
    naam: "Samen slimmer groeien",
    categorie: "Partners die we kennen",
  },
  {
    naam: "Exentra",
    categorie: "Partners die we kennen",
  },
  {
    naam: "Hoogbegaan",
    categorie: "Partners die we kennen",
  },
  {
    naam: "Cleverlab studiebegeleiding",
    categorie: "Partners die we kennen",
    omschrijving: "Studiebegeleiding.",
    regio: "Diepenbeek",
  },
  {
    naam: "Charlotte Vanneste",
    categorie: "Partners die we kennen",
    omschrijving: "Psycholoog.",
    regio: "Alken",
  },
  {
    naam: "Katrien Volckaert",
    categorie: "Partners die we kennen",
  },
];
