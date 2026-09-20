/*
  Het aanvraagformulier bij ons aanbod.

  Bij elk traject staan twee knoppen: één om info te vragen en één om in te
  schrijven. Beide openen dit formulier, met het juiste traject al ingevuld.

  Wat kan je hier aanpassen?
    verzenden   waar een ingevuld formulier naartoe gaat
    soorten     de teksten van de drie soorten aanvragen
    velden      de vragen op het formulier
    privacy     de zin over wat er met de gegevens gebeurt
*/

import { site } from "@/content/site";

/*
  WAAR GAAT EEN INGEVULD FORMULIER NAARTOE?

  Nu staat "webadres" op null. Dan opent het formulier het mailprogramma van
  de ouder met alle antwoorden er al in, klaar om naar info@matmgroep.com te
  sturen. Dat werkt meteen en er komt geen andere firma aan de gegevens.

  Wil je dat het formulier rechtstreeks verstuurt, zonder dat de ouder een
  mailprogramma nodig heeft? Dan neem je een formulierdienst en zet je het
  webadres dat je van hen krijgt hieronder tussen aanhalingstekens. Let op:
  die dienst verwerkt dan gegevens van kinderen, dus kies bewust. Zie de
  README voor de uitleg.
*/
export const verzenden = {
  webadres: null as string | null,
  mailnaar: site.email,
};

export type SoortSleutel = "info" | "inschrijven" | "proefles";

/*
  De drie soorten aanvragen.
    knop         de tekst op de knop bij het aanbod
    titel        de titel bovenaan het formulier
    label        het kleine woordje erboven
    tekst        de zin onder de titel
    onderwerp    het onderwerp van de mail die bij ons toekomt
    zonderAanbod de zin in het groene kadertje als de ouder nog geen
                 traject koos; de titel erboven staat bij geenTraject
*/
export const soorten: Record<
  SoortSleutel,
  {
    knop: string;
    titel: string;
    label: string;
    tekst: string;
    onderwerp: string;
    zonderAanbod: string;
  }
> = {
  info: {
    knop: "Info aanvragen",
    titel: "Meer info aanvragen",
    label: "Vrijblijvend",
    tekst:
      "Laat hier je gegevens achter en we bezorgen je alle praktische info. Je legt nog niets vast, en we bellen of mailen je terug.",
    onderwerp: "Infoaanvraag via de website",
    zonderAanbod: "Laat je gegevens achter, dan bekijken we samen wat past.",
  },
  inschrijven: {
    knop: "Inschrijven",
    titel: "Inschrijven",
    label: "Inschrijving",
    tekst:
      "Vul de gegevens van je kind en van jezelf in. Wij nemen contact op om de inschrijving af te ronden en om te bekijken welke groep het best past.",
    onderwerp: "Inschrijving via de website",
    zonderAanbod: "Schrijf je in en maak kennis met ons en met ons aanbod.",
  },
  proefles: {
    knop: "Gratis proefles",
    titel: "Inschrijven voor een gratis proefles",
    label: "Gratis en vrijblijvend",
    tekst:
      "Je kind mag vrijblijvend een keer meedoen. Laat je gegevens achter, dan spreken we samen een datum af.",
    onderwerp: "Aanvraag gratis proefles via de website",
    zonderAanbod: "Schrijf je in en maak kennis met ons en met ons aanbod.",
  },
};

export type Veld = {
  /* De naam die in de mail voor de vraag komt te staan. */
  naam: string;
  label: string;
  soort: "tekst" | "email" | "telefoon" | "lang";
  verplicht?: boolean;
  hulp?: string;
};

export const velden: Veld[] = [
  {
    naam: "Naam van het kind",
    label: "Naam van het kind",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Leeftijd van het kind",
    label: "Leeftijd van het kind",
    soort: "tekst",
    verplicht: true,
    hulp: "Of de geboortedatum, wat jij handiger vindt.",
  },
  {
    naam: "Naam van de ouders",
    label: "Naam van de ouder of ouders",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Gemeente",
    label: "Gemeente waar jullie wonen",
    soort: "tekst",
    verplicht: true,
    hulp: "Zo weten we welke locatie het dichtst bij jullie ligt.",
  },
  {
    naam: "Gsm-nummer",
    label: "Gsm-nummer",
    soort: "telefoon",
    verplicht: true,
  },
  {
    naam: "E-mailadres",
    label: "E-mailadres",
    soort: "email",
    verplicht: true,
  },
  {
    naam: "Vraag of boodschap",
    label: "Je vraag of boodschap",
    soort: "lang",
    hulp: "Iets dat we moeten weten? Schrijf het hier gerust. Dit veld mag ook leeg blijven.",
  },
];

export const formulierTekst = {
  /* Het kadertje bovenaan als de ouder al een traject koos. */
  trajectVraag: "Over welk aanbod gaat het?",

  /*
    Het kadertje bovenaan als de ouder nog geen traject koos.
      label   het kleine woordje bovenaan
      titel   de dikke regel
      inMail  wat er in de mail komt te staan bij "Aanbod"
    De regel onder de titel verschilt per soort aanvraag en staat
    hierboven bij "soorten", onder "zonderAanbod".
  */
  geenTraject: {
    label: "Kom kennismaken",
    titel: "Kom jij ons leren kennen?",
    inMail: "Nog geen aanbod gekozen",
  },
  verstuurKnop: "Versturen",
  terug: "Bekijk eerst het hele aanbod",
  terugLink: "/aanbod",

  /* Wat er gebeurt nadat een ouder op versturen klikt. */
  naVersturen:
    "Je mailprogramma opent met je antwoorden erin. Klik daar op versturen en het bericht komt bij ons toe. Werkt dat bij jou niet? Mail of bel ons gerust rechtstreeks.",

  privacy:
    "We gebruiken deze gegevens enkel om je te contacteren over je aanvraag en om de deelname van je kind te regelen. We geven ze niet door aan anderen. Wil je dat we ze verwijderen, laat het dan weten.",
  akkoordTekst:
    "Ik ga akkoord dat Connectopia deze gegevens hiervoor gebruikt.",

  liever: "Liever gewoon bellen of mailen?",
};

/* Het webadres van het formulier voor een bepaalde soort aanvraag en traject. */
export function aanvraagLink(soort: SoortSleutel, trajectSlug?: string) {
  return trajectSlug
    ? `/aanvraag/${soort}-${trajectSlug}`
    : `/aanvraag/${soort}`;
}
