/*
  De winactie van het oefenplatform, op www.connectopia.one/winactie.

  Een aantal gezinnen mag het volledige oefenplatform gratis testen. Wie na
  de testperiode een evaluatie indient, krijgt gratis toegang tot het einde
  van het schooljaar.

  Wat kan je hier aanpassen?
    open        zet op false als de inschrijvingen gesloten zijn; dan
                verdwijnt het formulier en staat er de zin bij "gesloten"
    plaatsen    hoeveel gezinnen mogen meedoen; het getal komt vanzelf
                overal in de teksten
    stappen     de drie stappen, met de data erin
    niveaus     wat er op het platform te testen valt
    velden      de vragen op het inschrijfformulier
*/

import type { Veld } from "@/content/formulier";

const plaatsen = 10;

export const winactie = {
  open: true,

  label: "Winactie",
  titel: "Test ons oefenplatform gratis",
  handgeschreven: `${plaatsen} gezinnen gezocht!`,
  tekst: `Help ons het oefenplatform nog beter te maken. ${plaatsen} gezinnen mogen alles gratis uittesten, en wie ons daarna vertelt wat ze ervan vinden, krijgt het volledige schooljaar gratis toegang. Inschrijven kan tot en met zaterdag 26 september.`,

  stappenTitel: "Zo werkt het",
  stappen: [
    {
      titel: "Test het volledige platform",
      tekst:
        "Van 27 september tot en met 31 oktober 2026 heb je gratis toegang tot alles: alle niveaus, alle vakken en alle leerbundels.",
    },
    {
      titel: "Vertel ons wat je ervan vindt",
      tekst:
        "Na de testperiode vul je een korte evaluatie in. Wat werkt goed, wat mist er, wat kan beter?",
    },
    {
      titel: "Krijg een gratis licentie",
      tekst:
        "Heb je je evaluatie ingediend, dan houd je gratis toegang tot het einde van het schooljaar 2026-2027.",
    },
  ],

  niveausTitel: "Wat kan je testen?",
  niveaus: [
    {
      icoon: "🌱",
      naam: "Start",
      voorWie: "5de en 6de leerjaar",
    },
    {
      icoon: "✨",
      naam: "Spark",
      voorWie: "1ste graad middelbaar",
    },
  ],

  /* Tot wanneer je kan inschrijven en hoe de gezinnen gekozen worden. */
  plaatsenTekst: `Inschrijven kan tot en met zaterdag 26 september. Daarna loten we de ${plaatsen} testgezinnen uit alle inschrijvingen, en iedereen hoort per mail of ze erbij zijn. De testgezinnen krijgen meteen ook te horen hoe ze toegang krijgen.`,

  formulierTitel: "Schrijf je gezin in",
  onderwerp: "Inschrijving winactie oefenplatform via de website",
  gesloten:
    "De inschrijvingen voor deze winactie zijn afgesloten. Bedankt aan iedereen die meedeed!",
};

export const winactieVelden: Veld[] = [
  {
    naam: "Naam van de ouders",
    label: "Naam van de ouder of ouders",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "E-mailadres",
    label: "E-mailadres",
    soort: "email",
    verplicht: true,
    hulp: "Hierop bezorgen we je de toegang tot het platform.",
  },
  {
    naam: "Gsm-nummer",
    label: "Gsm-nummer",
    soort: "telefoon",
    verplicht: true,
  },
  {
    naam: "Gemeente",
    label: "Gemeente waar jullie wonen",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Naam van het kind",
    label: "Naam van je kind of kinderen",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Leerjaar",
    label: "In welk leerjaar zitten ze?",
    soort: "tekst",
    verplicht: true,
    hulp: "Bijvoorbeeld 6de leerjaar of 1ste middelbaar.",
  },
  {
    naam: "Waarom willen jullie meedoen",
    label: "Waarom willen jullie meedoen?",
    soort: "lang",
    hulp: "Mag ook leeg blijven.",
  },
];
