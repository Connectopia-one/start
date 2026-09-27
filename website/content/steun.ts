/*
  De pagina "Steun ons": hoe iemand Connectopia vzw kan helpen.

  Kim vroeg die op 27 september 2026. We zijn een vzw die met eigen middelen
  werkt, en steun is veel breder dan geld: oud schoolmateriaal, boeken die nog
  in goede staat zijn, vrijwilligers, en mensen die hun kennis komen delen.

  Wat kan je hier aanpassen?
    steun         alle teksten op de pagina
    steun.rekening  het rekeningnummer; zolang dat leeg is, zegt de pagina
                  dat we de gegevens op vraag bezorgen
    steunVelden   de vragen op het formulier onderaan
*/

import type { Veld } from "@/content/formulier";

export const steun = {
  label: "Steun ons",
  titel: "Help je ons mee vooruit?",
  handgeschreven: "Alles helpt, echt alles",
  tekst:
    "Connectopia is een vzw en we werken met eigen middelen. Alles wat we doen, van de plusklassen tot de kampen en het oefenplatform, bouwen we zelf op. Wil je ons een duwtje geven? Dat kan op veel meer manieren dan met geld alleen.",

  /*
    Het rekeningnummer van de vzw, bij Belfius. Doorgegeven door Kim op
    27 september 2026 en nagerekend: zowel de IBAN-controle als de Belgische
    controlegetallen kloppen. Maak je het ooit leeg, dan zegt de pagina vanzelf
    weer dat we de gegevens bezorgen aan wie erom vraagt.
  */
  rekening: "BE61 0689 6047 3617",

  manierenTitel: "Zo kan je helpen",
  manieren: [
    {
      titel: "Met een centje",
      tekst:
        "Elk bedrag gaat rechtstreeks naar materiaal voor de kinderen. Groot of klein maakt niet uit, het telt allemaal mee.",
      icoon: "💛",
      kleur: "orange" as const,
    },
    {
      titel: "Met schoolmateriaal",
      tekst:
        "Heb je nog materiaal liggen dat niet meer gebruikt wordt en nog in goede staat is? Wij geven het een tweede leven in onze werkingen en op onze kampen.",
      icoon: "✂️",
      kleur: "green" as const,
    },
    {
      titel: "Met boeken",
      tekst:
        "Schoolboeken, naslagwerken, leesboeken, strips: wij houden van alle soorten boeken. Zolang ze nog in goede staat zijn, zijn ze welkom.",
      icoon: "📚",
      kleur: "purple" as const,
    },
    {
      titel: "Met je handen",
      tekst:
        "Vrijwilligers zijn altijd welkom, voor een dag, een kamp of het hele jaar. Je hoeft geen diploma te hebben, wel graag tussen kinderen te staan.",
      icoon: "🙋",
      kleur: "green" as const,
    },
    {
      titel: "Met je kennis",
      tekst:
        "Kom je vertellen over je beroep of je bedrijf? Ben je leerkracht en wil je je inzichten delen? Voor deze kinderen is een namiddag met iemand die echt weet waarover hij praat goud waard.",
      icoon: "💡",
      kleur: "orange" as const,
    },
    {
      titel: "Met wie je bent",
      tekst:
        "Ben je zelf autistisch en wil je als vrijwilliger mee op kamp? Stel je gerust voor. Je begrijpt onze kinderen op een manier die wij niet kunnen uitleggen, en dat is precies wat ze nodig hebben.",
      icoon: "🧩",
      kleur: "purple" as const,
    },
  ],

  /* Het kader onderaan, voor wie twijfelt of zijn idee wel meetelt. */
  breed: {
    titel: "Twijfel je of het de moeite is?",
    tekst:
      "Doe maar. We zijn blij met alles, ook met een doos oude leesboeken of een halve dag van je tijd. Vertel ons gewoon wat je in gedachten hebt, dan bekijken we samen of het past.",
  },

  /* Wat er met geld gebeurt. Kort en concreet, geen grote woorden. */
  waarheenTitel: "Waar het naartoe gaat",
  waarheen: [
    "Materiaal voor de plusklassen, de pluswerkingen en de kampen",
    "Boeken en naslagwerken voor de kinderen",
    "De plaatsen waar we samenkomen",
    "Het oefenplatform, dat we zelf bouwen en onderhouden",
  ],

  /*
    Voor bedrijven. Een bedrijf dat ons steunt en er zichtbaarheid voor
    terugkrijgt, doet geen gift maar koopt reclame: daar hoort een document
    voor de boekhouding bij. Wat er precies op dat document komt te staan,
    hangt af van de vzw; daarom noemt de tekst het "een document" en geen
    factuur of onkostennota.
  */
  bedrijven: {
    label: "Voor bedrijven",
    titel: "Sponsoren in ruil voor zichtbaarheid",
    tekst:
      "Steunt je bedrijf ons met een bedrag, dan zetten we je naam en je logo op onze flyers en hier op de website. Je krijgt daar een document voor, zodat je boekhouder het bedrag als reclamekost kan inbrengen. Wat je precies terugkrijgt spreken we samen af: het hangt af van het bedrag en van wat er op dat moment gedrukt wordt.",
    punten: [
      "Je naam en logo op onze flyers",
      "Je naam en logo bij de sponsors op deze website",
      "Een document voor je boekhouding",
      "In overleg: zichtbaarheid op een kamp of een evenement",
    ],
  },

  /*
    Eerlijk zijn over wat een particulier er fiscaal aan heeft: niets, en dat
    verandert pas als de erkenning er is. Zet er geen jaartal bij zolang dat
    niet zeker is.
  */
  attesten: {
    titel: "En als particulier?",
    tekst:
      "Doneren mag natuurlijk altijd, en we zijn er heel blij mee. Alleen kunnen we je er voorlopig geen fiscaal attest voor geven: daar is een erkenning voor nodig die we aanvragen, maar die laat nog een hele tijd op zich wachten. Je gift is dus niet fiscaal aftrekbaar. We zeggen het liever meteen dan dat je er achteraf achterkomt.",
  },

  formulierTitel: "Laat het ons weten",
  formulierTekst:
    "Vink aan wat je in gedachten hebt, meerdere dingen mogen. We nemen contact op om het verder af te spreken.",
  onderwerp: "Aanbod om te steunen via de website",

  privacy:
    "We gebruiken deze gegevens enkel om contact met je op te nemen over je aanbod. We geven ze niet door aan anderen. Wil je dat we ze verwijderen, laat het dan weten.",
};

export const steunVelden: Veld[] = [
  {
    naam: "Naam",
    label: "Je naam",
    soort: "tekst",
    verplicht: true,
  },
  {
    naam: "Organisatie",
    label: "Bedrijf of organisatie",
    soort: "tekst",
    hulp: "Enkel als je namens een bedrijf of een vereniging schrijft.",
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
    naam: "Gemeente",
    label: "Gemeente waar je woont",
    soort: "tekst",
    hulp: "Handig als je iets wil langsbrengen of ophalen.",
  },
  {
    naam: "Waarmee",
    label: "Waarmee zou je ons willen helpen?",
    soort: "keuzes",
    hulp: "Meerdere vakjes aanvinken mag.",
    keuzes: [
      { naam: "Een gift", label: "Met een gift" },
      {
        naam: "Sponsoring als bedrijf",
        label: "Als bedrijf, in ruil voor zichtbaarheid",
      },
      { naam: "Schoolmateriaal", label: "Met schoolmateriaal" },
      { naam: "Boeken", label: "Met boeken" },
      { naam: "Vrijwilliger", label: "Als vrijwilliger bij onze werkingen" },
      { naam: "Vrijwilliger op kamp", label: "Als vrijwilliger mee op kamp" },
      {
        naam: "Vertellen over beroep of bedrijf",
        label: "Door te komen vertellen over mijn beroep of bedrijf",
      },
      {
        naam: "Inzichten delen",
        label: "Door mijn inzichten te delen als leerkracht of begeleider",
      },
      { naam: "Iets anders", label: "Iets anders" },
    ],
  },
  {
    naam: "Vertel er iets over",
    label: "Vertel er gerust iets over",
    soort: "lang",
    hulp: "Wat heb je liggen, wat zou je willen doen, wanneer past het? Dit veld mag ook leeg blijven.",
  },
];
