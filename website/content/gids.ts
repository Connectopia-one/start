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
  /*
    De bestandsnaam van hun logo. Zet het bestand in de map  public/gids/
    en vul hier alleen de naam in, bijvoorbeeld  bekina.png
    Heb je nog geen logo? Laat deze regel gewoon weg, dan zet de site
    de naam van de organisatie in het vakje.
  */
  logo?: string;
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
  /*
    Onder welk kopje een organisatie komt die iemand via het formulier
    aanbracht en die jij in het ouderportaal goedkeurde.
  */
  categorieAangebracht: "Partners die we kennen",
  /* Het formulier onderaan de gids. Teksten op het formulier zelf. */
  formulier: {
    titel: "Een organisatie aanbrengen",
    tekst:
      "Ken je iemand die hier hoort, of wil je er zelf in staan? Vul het hieronder in. We bekijken het eerst, dus het staat er niet meteen op.",
    wieLabel: "Wie breng je aan?",
    wieZelf: "Mezelf of mijn eigen praktijk",
    wieIemand: "Iemand anders",
    naamLabel: "Naam van de organisatie of de persoon",
    omschrijvingLabel: "Wat doen ze?",
    omschrijvingUitleg:
      "Een of twee zinnen, zoals bij de andere kaartjes. We passen ze zo nodig aan, zodat elke omschrijving even lang is.",
    regioLabel: "Waar?",
    regioUitleg: "Een gemeente, een provincie, of online.",
    linkLabel: "Website",
    linkUitleg: "Mag leeg blijven.",
    jouwNaamLabel: "Jouw volledige naam",
    mailLabel: "Jouw e-mailadres",
    privacy:
      "Je naam en je e-mailadres komen niet op de website. Ze blijven bij ons, zodat we je kunnen bereiken als we iets willen vragen.",
    knopTekst: "Insturen",
    nogNiet:
      "Aanbrengen kan hier binnenkort. Laat het ons tot dan weten via de contactpagina.",
    /* Wat er boven het formulier staat nadat iemand op Insturen klikte. */
    gelukt:
      "Bedankt! We bekijken het en zetten het erbij, meestal binnen een paar dagen.",
    mislukt:
      "Dat is niet gelukt. Probeer het later nog eens, of laat het ons weten via de contactpagina.",
    foutNaam: "Vul de naam van de organisatie of de persoon in.",
    foutOmschrijving: "Schrijf in een of twee zinnen wat ze doen.",
    foutLink: "Die website lijkt niet te kloppen.",
    foutJouwNaam: "Vul je eigen volledige naam in.",
    foutMail: "Vul een e-mailadres in waarop we je kunnen bereiken.",
  },
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
    logo: "samen-slimmer-groeien.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Testing, opvoedingsadvies en studiecoaching rond hoogbegaafdheid, thuis en op school. Ook groeigroepen voor kinderen en jongeren.",
    regio: "Heel Vlaanderen en online",
    link: "https://samenslimmergroeien.be",
  },
  {
    naam: "Exentra",
    logo: "exentra.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Expertisecentrum rond hoogbegaafdheid, voor kinderen en ouders, jongeren, volwassenen, scholen en CLB. Met een eigen online academy.",
    regio: "Vlaanderen en Nederland",
    link: "https://exentra.be",
  },
  {
    naam: "Hoogbegaan",
    logo: "hoogbegaan.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Adviesgesprekken voor ouders en individuele begeleiding van hoogbegaafde kinderen en tieners. Kan mee op gesprek op school, en geeft lezingen.",
    regio: "Pelt en online",
    link: "https://hoogbegaan.be",
  },
  {
    naam: "Cleverlab studiebegeleiding",
    logo: "cleverlab.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Bijles en studiebegeleiding in wiskunde en wetenschappen, en begeleiding bij hoogbegaafdheid. Ook trajecten voor de examencommissie en toelatingsexamens.",
    regio: "Diepenbeek",
  },
  {
    naam: "Bekina",
    logo: "bekina.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Vereniging voor hoogbegaafde kinderen en jongeren en hun (groot)ouders, leerkrachten en professionals. Met activiteiten, kampen, lezingen en publicaties.",
    regio: "West- en Oost-Vlaanderen",
    link: "https://bekina.org",
  },
  {
    naam: "Charlotte Vanneste",
    logo: "charlotte-vanneste.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Psychotherapie en coaching, diagnostisch onderzoek, kerntalentenanalyse en supervisie. Voor kinderen, jongeren en volwassenen.",
    regio: "Alken",
    link: "https://www.charlottevanneste.com",
  },
  {
    naam: "Katrien Volckaert",
    logo: "katrien-volckaert.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Oudercoach bij neurodiversiteit, met expertise in gecamoufleerd autisme bij cognitieve begaafdheid en in PDA. Geeft ook webinars, lezingen en workshops.",
    link: "https://www.katrienvolckaert.be",
  },
  /* Doorgegeven door Kim op 16 oktober 2026. */
  {
    naam: "Lore Dewulf",
    logo: "lore-dewulf.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Begaafdheidsonderzoek dat verder gaat dan een IQ-test, met advies op maat, voor kinderen vanaf 4 jaar en volwassenen. Ook een online opleiding en lezingen.",
    regio: "Gent",
    link: "https://loredewulf.be/begaafdheidsonderzoek/",
  },
  {
    naam: "Het Lampje",
    logo: "het-lampje.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Begeleiding bij autisme en hoogbegaafdheid, ook bij dubbel bijzondere kinderen. Onderzoek naar autistisch denken van 7 tot 17 jaar, opleidingen en webinars.",
    regio: "Heverlee en online",
    link: "https://www.hetlampje.be",
  },
  {
    naam: "Snelle Hoofdjes",
    logo: "snelle-hoofdjes.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Plusgroepen vanaf de derde kleuterklas, mindsettraining in groep en individueel, en advies voor ouders en scholen, door een mama die ervaringsdeskundige is.",
    regio: "Oostakker",
    link: "https://www.snellehoofdjes.be",
  },
  {
    naam: "De Groeitrap",
    logo: "de-groeitrap.png",
    categorie: "Partners die we kennen",
    omschrijving:
      "Kindercentrum met IQ-testing door een psycholoog of orthopedagoog, van 0 tot 21 jaar. Ook logopedie, kinesitherapie, psychologie en coaching.",
    regio: "Wilsele en Bertem",
    link: "https://www.degroeitrap.be",
  },
];

/*
  Logo's voor organisaties die zich via het formulier aanmeldden. Die staan in
  de databank, niet in de lijst hierboven. Je kan hun logo ook in het
  ouderportaal opladen (Beheer, Gids); staat het daar, dan gaat dat voor.

  De sleutel is hun website zonder https:// en www., zodat het logo blijft
  kloppen als de naam in het beheer nog wat aangepast wordt. Het bestand
  staat in  public/gids/
*/
export const logosAangebracht: Record<string, string> = {
  "agapei.be": "agapei.png",
  "brightstarcoaching.be": "bright-star-coaching.png",
  "claro.nu": "claro.png",
  "itoswetteren.be": "itos.png",
  "nelevervaeck.be": "nele-vervaeck.png",
  "praktijkdeboomhut.be": "praktijk-de-boomhut.png",
  "spring-stof.be": "spring-stof.png",
  "talentvol.be": "talentvol.png",
};

/* "https://Www.nelevervaeck.be/x" wordt "nelevervaeck.be". */
export function logoVoorLink(link?: string | null): string | undefined {
  if (!link) return undefined;
  try {
    const host = new URL(link).hostname.toLowerCase().replace(/^www\./, "");
    return logosAangebracht[host];
  } catch {
    return undefined;
  }
}

/* Alfabetisch, zodat de volgorde geen rangschikking is. */
export function organisatiesPerCategorie(
  categorie: string,
  lijst: Organisatie[] = organisaties,
) {
  return lijst
    .filter((o) => o.categorie === categorie)
    .sort((a, b) => a.naam.localeCompare(b.naam, "nl"));
}
