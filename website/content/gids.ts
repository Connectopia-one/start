/*
  De gids "Waar kan je terecht".
  Elke organisatie is één regel. Voeg er gerust bij zodra je ze kent.

  categorie: gebruik dezelfde naam voor organisaties die bij elkaar horen,
             dan komen ze samen onder één kopje te staan.
*/

export type Organisatie = {
  naam: string;
  categorie: string;
  omschrijving: string;
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
];
