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
  /* De tekst op de knop. Laat leeg voor "Naar hun website". */
  linkTekst?: string;
};

export const gidsTekst = {
  label: "Waar kan je terecht",
  titel: "Diensten en organisaties die we kennen",
  tekst:
    "Van psycholoog en logopedist tot bijlesleerkracht met kennis van hoogbegaafdheid, ook bij dubbele diagnoses. We verwijzen alleen door naar mensen en organisaties waar we zelf vertrouwen in hebben.",
  /* Deze zin staat bovenaan de lijst, in een gekleurd kader. */
  geenVoorkeur:
    "We trekken hier niemand voor. Elke organisatie op deze lijst doet goed werk, en welke bij jouw kind en jouw gezin past is een heel persoonlijke keuze. De lijst staat dan ook op alfabetische volgorde en is geen rangschikking. Neem gerust bij meerdere een kijkje en voel zelf waar het klikt.",
  nota:
    "Deze gids groeit mee. Ken je iemand die hier hoort, of wil je er zelf in staan? Laat het ons weten.",
  oproepTekst: "Een organisatie aanbrengen",
  oproepLink: "/over-ons#contact",
  linkTekstStandaard: "Naar hun website",
  leegTekst:
    "We zijn deze lijst nog aan het opbouwen. Heb je een concrete vraag? Stel ze gerust, dan verwijzen we je persoonlijk door.",
  /* Staat onder een partner waar we de omschrijving nog moeten aanvullen. */
  nogGeenOmschrijving: "Meer uitleg volgt binnenkort.",
};

/*
  De volgorde hieronder maakt niet uit: de site zet elke categorie zelf op
  alfabetische volgorde. Zo staat er niemand vooraan en trekken we niemand voor.
*/
export const organisaties: Organisatie[] = [
  {
    naam: "CLB van de school",
    categorie: "Eerste stap",
    omschrijving:
      "Gratis eerste aanspreekpunt bij twijfels over leren, gedrag of welbevinden. Kan screenen en doorverwijzen. Elke school hoort bij een vast CLB; via de lijst van de Vlaamse overheid vind je die van jouw school.",
    regio: "Overal",
    link: "https://www.vlaanderen.be/onderwijs-en-vorming/ondersteuning-en-begeleiding-voor-leerlingen-cursisten-en-studenten/basis-en-secundair-onderwijs/centrum-voor-leerlingenbegeleiding",
    linkTekst: "Zoek het CLB van je school",
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
    omschrijving:
      "Testing, opvoedingsadvies en studiecoaching rond hoogbegaafdheid, thuis en op school. Ook groeigroepen voor kinderen en jongeren.",
    regio: "Heel Vlaanderen en online",
    link: "https://samenslimmergroeien.be",
  },
  {
    naam: "Exentra",
    categorie: "Partners die we kennen",
    omschrijving:
      "Expertisecentrum rond hoogbegaafdheid, voor kinderen en ouders, jongeren, volwassenen, scholen en CLB. Met een eigen online academy.",
    regio: "Vlaanderen en Nederland",
    link: "https://exentra.be",
  },
  {
    naam: "Hoogbegaan",
    categorie: "Partners die we kennen",
    omschrijving:
      "Adviesgesprekken voor ouders en individuele begeleiding van hoogbegaafde kinderen en tieners. Kan mee op gesprek op school, en geeft lezingen.",
    regio: "Pelt en online",
    link: "https://hoogbegaan.be",
  },
  {
    naam: "Cleverlab studiebegeleiding",
    categorie: "Partners die we kennen",
    omschrijving:
      "Bijles en studiebegeleiding in wiskunde en wetenschappen, en begeleiding bij hoogbegaafdheid. Ook trajecten voor de examencommissie en toelatingsexamens.",
    regio: "Diepenbeek",
  },
  {
    naam: "Bekina",
    categorie: "Partners die we kennen",
    omschrijving:
      "Vereniging voor hoogbegaafde kinderen en jongeren en hun (groot)ouders, leerkrachten en professionals. Met activiteiten, kampen, lezingen en publicaties.",
    regio: "West- en Oost-Vlaanderen",
    link: "https://bekina.org",
  },
  {
    naam: "Charlotte Vanneste",
    categorie: "Partners die we kennen",
    omschrijving:
      "Psychotherapie en coaching, diagnostisch onderzoek, kerntalentenanalyse en supervisie. Voor kinderen, jongeren en volwassenen.",
    regio: "Alken",
  },
  {
    naam: "Katrien Volckaert",
    categorie: "Partners die we kennen",
    omschrijving:
      "Oudercoach bij neurodiversiteit, met expertise in gecamoufleerd autisme bij cognitieve begaafdheid en in PDA. Geeft ook webinars, lezingen en workshops.",
    link: "https://www.katrienvolckaert.be",
  },
];

/* Alfabetisch, zodat de volgorde geen rangschikking is. */
export function organisatiesPerCategorie(categorie: string) {
  return organisaties
    .filter((o) => o.categorie === categorie)
    .sort((a, b) => a.naam.localeCompare(b.naam, "nl"));
}
