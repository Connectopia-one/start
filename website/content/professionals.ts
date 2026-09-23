/*
  De pagina voor professionals: kinesisten, logopedisten, coaches,
  auticoaches, artsen, neurologen en andere begeleiders.

  Ze komen hier via de knop op de startpagina, via de voettekst of via de
  QR-code op de flyer. Niemand wordt verplicht: wie gewoon de site wil
  bekijken, klikt hier voorbij.

  Wat kan je hier aanpassen?
    professionals        alle teksten op de pagina
    professionalsVelden  de vragen op het formulier onderaan
*/

import type { Veld } from "@/content/formulier";

export const professionals = {
  label: "Voor professionals",
  titel: "Werk jij met deze kinderen?",
  handgeschreven: "Jij ziet ze in je praktijk, wij zien ze in de groep.",
  tekst:
    "Connectopia vzw brengt kinderen van 6 tot 12 jaar met hoogbegaafdheid, ASS of ADHD samen met gelijkgestemden, in Hasselt en Genk. Daarnaast helpen we hun ouders hun weg te vinden. Hieronder lees je wat je eraan hebt, en laat je achter wat we voor je mogen doen.",

  /* Het kader dat meteen duidelijk maakt wat we níet zijn. */
  nuance: {
    titel: "Wij stellen geen diagnoses en geven geen therapie",
    tekst:
      "Wij zijn ervaringsdeskundige ouders met een pedagogische achtergrond en een netwerk van specialisten. We vullen aan wat jij doet: een plek waar een kind peers vindt, en ouders die beter voorbereid bij je binnenkomen.",
  },

  puntenTitel: "Wat je eraan hebt",
  punten: [
    {
      titel: "Een plek om naar door te verwijzen",
      tekst:
        "Kleine groepjes met gelijkgestemde kinderen van 6 tot 12 jaar, in Hasselt en Genk. Voor het kind dat op school alleen staat met zijn interesses, of dat vastloopt op verveling. Een gratis proefles kan altijd.",
      icoon: "🚀",
      kleur: "green" as const,
      link: { tekst: "Bekijk ons aanbod", href: "/aanbod" },
    },
    {
      titel: "Ouders die voorbereid bij je komen",
      tekst:
        "Op onze site staat een gratis observatielijst die ouders invullen en afdrukken. Het is geen test en geen diagnose, gewoon een blad dat hun gedachten ordent. Zo begint jouw gesprek niet bij nul.",
      icoon: "📋",
      kleur: "purple" as const,
      link: { tekst: "Naar de observatielijst", href: "/observatielijst" },
    },
    {
      titel: "Een wegwijzer waar ouders jou terugvinden",
      tekst:
        "In “Waar kan je terecht” verzamelen we diensten die we kennen en vertrouwen, van psycholoog en logopedist tot bijlesleerkracht met kennis van hoogbegaafdheid. Alfabetisch en zonder voorkeur. Denk je dat je hier thuishoort? Laat het weten.",
      icoon: "🧭",
      kleur: "orange" as const,
      link: { tekst: "Bekijk de wegwijzer", href: "/waar-kan-je-terecht" },
    },
  ],

  /* Het oranje kader met wat we bezorgen. */
  bezorgenTitel: "Wat we je graag bezorgen",
  bezorgen: [
    {
      titel: "Onze folders digitaal",
      tekst: "Om door te sturen naar de ouders die je begeleidt.",
    },
    {
      titel: "Een poster",
      tekst: "Voor je wachtzaal of praktijkruimte.",
    },
    {
      titel: "Flyers op papier",
      tekst: "Om mee te geven, zoveel je er nodig hebt.",
    },
  ],
  bezorgenSlot: "Het kost je niets. Vul hieronder in wat je wil.",

  formulierTitel: "Laat je gegevens achter",
  formulierTekst:
    "Vink aan wat voor jou past, meerdere dingen mogen. We nemen contact op om het verder af te spreken.",
  onderwerp: "Aanvraag van een professional via de website",

  /* Wat er onder het formulier staat over de gegevens. */
  privacy:
    "We gebruiken deze gegevens enkel om contact met je op te nemen over je aanvraag en om je te bezorgen wat je aanvinkte. We geven ze niet door aan anderen. Wil je dat we ze verwijderen, laat het dan weten.",
};

export const professionalsVelden: Veld[] = [
  {
    naam: "Naam",
    label: "Je naam",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Praktijk of organisatie",
    label: "Praktijk of organisatie",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Beroep",
    label: "Je beroep of functie",
    soort: "tekst",
    verplicht: true,
    hulp: "Bijvoorbeeld logopedist, kinesist, coach, arts of zorgleerkracht.",
  },
  {
    naam: "E-mailadres",
    label: "E-mailadres",
    soort: "email",
    verplicht: true,
  },
  {
    naam: "Telefoonnummer",
    label: "Telefoonnummer",
    soort: "telefoon",
  },
  {
    naam: "Adres van de praktijk",
    label: "Adres van de praktijk",
    soort: "tekst",
    hulp: "Alleen nodig als je posters of flyers op papier wil.",
  },
  {
    naam: "Waarvoor",
    label: "Waarvoor mogen we je contacteren?",
    soort: "keuzes",
    hulp: "Meerdere vakjes aanvinken mag.",
    keuzes: [
      {
        naam: "Flyers op papier",
        label: "Flyers op papier om uit te delen",
        aantal: { naam: "Aantal flyers", label: "hoeveel" },
      },
      {
        naam: "Posters",
        label: "Posters voor de wachtzaal",
        aantal: { naam: "Aantal posters", label: "hoeveel" },
      },
      {
        naam: "Folders digitaal",
        label: "Onze folders digitaal, om door te sturen",
      },
      { naam: "Samenwerking", label: "Een samenwerking bespreken" },
      { naam: "Online overleg", label: "Een online overleg inplannen" },
      {
        naam: "Opname in de wegwijzer",
        label: "Opgenomen worden in “Waar kan je terecht”",
      },
      { naam: "Iets anders", label: "Iets anders" },
    ],
  },
  {
    naam: "Vraag of boodschap",
    label: "Je vraag of boodschap",
    soort: "lang",
    hulp: "Koos je “iets anders”, schrijf hier dan wat je bedoelt. Dit veld mag ook leeg blijven.",
  },
];
