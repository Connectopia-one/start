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
      titel: "Met materiaal",
      tekst:
        "Schoolmateriaal, knutselspullen, gezelschapsspellen, puzzels, bouwdozen of materiaal voor proefjes: heb je iets liggen dat niet meer gebruikt wordt en nog in goede staat is? Wij geven het een tweede leven in onze werkingen en op onze kampen.",
      icoon: "✂️",
      kleur: "green" as const,
    },
    {
      titel: "Met boeken",
      tekst:
        "Leesboeken, strips, naslagwerken, en ook oude leerboeken, werkboeken en leermaterialen: wij houden van alle soorten. Zolang ze nog in goede staat zijn, zijn ze welkom.",
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
    /* De sponsors komen uit content/sponsors.ts, net als op de startpagina. */
    voorgangers: "Zij steunen ons al",
    kopSponsors: "Sponsors",
    kopPartners: "Partners die ons onder meer met lokalen steunen",
    knop: "Ik wil sponsoren",
  },

  /*
    Voor particulieren. Kim op 15 oktober 2026: de tekst was "niet echt
    aantrekkelijk", met als kern "vele beetjes en vele handen maken een groot
    geheel". De eerlijke uitleg over het fiscaal attest blijft, maar als
    kleine noot onderaan in plaats van als hoofdboodschap. Zet er geen
    jaartal bij zolang de erkenning niet zeker is.
  */
  particulier: {
    label: "Voor iedereen",
    titel: "Elke bijdrage telt",
    handgeschreven: "Vele beetjes en vele handen maken een groot geheel",
    tekst:
      "Je hoeft geen bedrijf te zijn om een verschil te maken. Een doos stiften, een spel dat thuis niet meer gespeeld wordt, een uurtje van je tijd of een klein bedrag: samen wordt het een plusklas vol materiaal, een kamp vol proefjes en een plek waar kinderen zichzelf mogen zijn.",
    knop: "Laat weten waarmee je helpt",
    attest:
      "Goed om te weten: voorlopig kunnen we nog geen fiscaal attest geven. Daar is een erkenning voor nodig die we aanvragen, maar die laat nog even op zich wachten. Je gift is dus nog niet fiscaal aftrekbaar.",
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
      {
        naam: "Schoolmateriaal",
        label: "Met schoolmateriaal of knutselmateriaal",
      },
      {
        naam: "Spelmateriaal",
        label: "Met spelmateriaal: gezelschapsspellen, puzzels, bouwdozen",
      },
      {
        naam: "Proefjesmateriaal",
        label: "Met materiaal voor proefjes en techniek",
      },
      { naam: "Boeken", label: "Met leesboeken, strips of naslagwerken" },
      {
        naam: "Leerboeken",
        label: "Met oude leerboeken, werkboeken of leermateriaal",
      },
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
