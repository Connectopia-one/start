/*
  Het prikbord voor ouders.

  Het prikbord bestaat uit vijf borden. Elk bord heeft zijn eigen pagina
  met briefjes erop, zoals sticky notes op een echt prikbord.

  EEN BRIEFJE OPHANGEN
  Zoek hieronder het bord waar het briefje bij hoort en voeg bovenaan in
  de lijst "briefjes" een blokje toe. Het nieuwste briefje hangt bovenaan.

    {
      tekst: "Wat er op het briefje staat.",
      van: "Wie het ophing, bv. een voornaam of Connectopia",
      datum: "2026-09-21",                       jaar-maand-dag
      wanneer: "Woensdag 8 oktober, 20u, online",         optioneel
      label: "Gezocht",                          optioneel woordje bovenaan
      link: { tekst: "Bekijken", href: "https://..." },   optioneel
      foto: { bestand: "naam.jpg", beschrijving: "..." }, optioneel
    }

  Een foto bij een briefje: zet het bestand in  public/prikbord/
  en vul hier alleen de bestandsnaam in.

  De briefjes die er nu op hangen zijn voorbeelden van ons, zodat een
  leeg bord er niet kaal uitziet. Haal ze weg zodra er echte briefjes zijn.
*/

import type { Kleur } from "@/components/ui";

export type Briefje = {
  tekst: string;
  /* Wanneer iets doorgaat, bv. "Woensdag 8 oktober, 20u, online". */
  wanneer?: string;
  van?: string;
  datum?: string;
  label?: string;
  link?: { tekst: string; href: string };
  foto?: { bestand: string; beschrijving: string };
};

export type Bord = {
  slug: string;
  naam: string;
  ondertitel: string;
  icoon: string;
  kleur: Kleur;
  uitleg: string;
  /* De drie voorbeelden die op de overzichtspagina onder het bord staan. */
  waarvoor: string[];
  briefjes: Briefje[];
};

export const prikbord = {
  label: "Prikbord voor ouders",
  titel: "Vijf borden, één plek om te delen",
  handgeschreven: "Jouw zoektocht mag minder eenzaam zijn.",
  tekst:
    "Hang een briefje op, lees wat anderen ophingen en vind elkaar. Kies hieronder het bord waar jouw briefje thuishoort.",

  /* De zin bovenaan een bord dat nog geen briefjes heeft. */
  leegTekst: "Dit bord is nog leeg. Hang jij het eerste briefje op?",

  spelregels: {
    titel: "Hoe het werkt",
    punten: [
      "Je briefje komt eerst bij ons toe. We hangen het op zodra we het gelezen hebben.",
      "Zet er geen achternaam, adres of school van een kind in. Een voornaam volstaat.",
      "Reageren doe je via ons, dan geven we je vraag door aan wie het briefje ophing.",
      "Past een briefje niet op een bord, dan zoeken we samen de juiste plek.",
    ],
  },

  formulier: {
    titel: "Hang je briefje op",
    tekst:
      "Schrijf hieronder wat er op je briefje moet komen. We lezen het na en hangen het op.",
    knopTekst: "Versturen",
    briefjeLabel: "Wat komt er op je briefje?",
    naamLabel: "Je naam of voornaam",
    mailLabel: "Je e-mailadres",
    privacy:
      "We gebruiken je e-mailadres alleen om je te bereiken over dit briefje. Het komt niet op het prikbord te staan.",
  },
};

export const borden: Bord[] = [
  {
    slug: "zoekertjes",
    naam: "Zoekertjes",
    ondertitel: "Gezocht, gevonden, aangeboden",
    icoon: "🔍",
    kleur: "orange",
    uitleg:
      "Het bord voor alles wat je zoekt of net kan missen. Van een speelafspraak voor je kind tot een doos materiaal die bij jou op zolder staat.",
    waarvoor: [
      "Vriendschappen en speelafspraken",
      "Materiaal en spelletjes",
      "Een vraag om informatie",
    ],
    briefjes: [
      {
        tekst:
          "Zoek je een speelafspraak voor je kind, of net een gezin dat hetzelfde meemaakt? Schrijf kort wie je kind is, wat het graag doet en in welke buurt jullie wonen.",
        van: "Connectopia",
        label: "Voorbeeld",
      },
      {
        tekst:
          "Heb je materiaal liggen waar je kind uit gegroeid is? Bouwdozen, spelletjes, boeken: hang er een briefje over op, dan vindt het een tweede leven.",
        van: "Connectopia",
        label: "Voorbeeld",
      },
    ],
  },
  {
    slug: "samenkomen",
    naam: "Samenkomen",
    ondertitel: "Koffiekletsen, bijeenkomsten en afspraken",
    icoon: "☕️",
    kleur: "green",
    uitleg:
      "Het bord voor alles waar je samen zit. Een online koffieklets, een babbel in het echt, een wandeling met andere ouders. Wij hangen hier onze momenten op, en jij mag er zelf een organiseren.",
    waarvoor: [
      "Online koffiekletsen",
      "Bijeenkomsten voor ouders",
      "Samen ergens naartoe",
    ],
    briefjes: [
      {
        tekst:
          "Zin in een online koffieklets met andere ouders? Laat het ons weten, dan zetten we er een op de agenda en hangt de datum hier.",
        van: "Connectopia",
      },
      {
        tekst:
          "Organiseer je zelf iets? Zet op je briefje wat het is, wanneer het doorgaat, waar het is en voor wie. Wij hangen het op.",
        van: "Connectopia",
        label: "Voorbeeld",
      },
    ],
  },
  {
    slug: "aanraders",
    naam: "Aanraders",
    ondertitel: "Wat jij gevonden hebt en anderen mag weten",
    icoon: "💛",
    kleur: "purple",
    uitleg:
      "Het bord voor de mensen, plekken en accounts die jou vooruit hielpen. Een boek dat alles deed kloppen, een begeleider bij wie je kind zichzelf mocht zijn, een pagina die je elke week leest.",
    waarvoor: [
      "Sociale media die je volgt",
      "Mensen en organisaties die hielpen",
      "Boeken, podcasts en plekken",
    ],
    briefjes: [
      {
        tekst:
          "Ken je een account, een boek of een organisatie waar je iets aan had? Zet erbij wat het jou bracht, dan weet een andere ouder meteen of het ook bij hen past.",
        van: "Connectopia",
        label: "Voorbeeld",
      },
      {
        tekst:
          "Zoek je liever een dienst of begeleider in de buurt? Kijk dan ook eens bij Waar kan je terecht, daar staan de organisaties die wij kennen.",
        van: "Connectopia",
        link: {
          tekst: "Naar Waar kan je terecht",
          href: "/waar-kan-je-terecht",
        },
      },
    ],
  },
  {
    slug: "uitgezocht",
    naam: "Uitgezocht",
    ondertitel: "De zwaardere vragen, met bronnen erbij",
    icoon: "📚",
    kleur: "green",
    uitleg:
      "Het bord voor wie iets grondig uitzocht. Een diagnosetraject, rechten op school, een onderzoek dat je las. Hang op wat je te weten kwam en zet erbij waar het vandaan komt, dan kan een ander erop verder.",
    waarvoor: [
      "Wat je uitzocht over een traject",
      "Onderzoek en artikels die je las",
      "Vragen waar je zelf nog mee zit",
    ],
    briefjes: [
      {
        tekst:
          "Zocht je iets grondig uit? Schrijf kort op wat je zocht, wat je vond en waar het vandaan komt. Zo hoeft de volgende ouder niet opnieuw te beginnen.",
        van: "Connectopia",
        label: "Voorbeeld",
      },
      {
        tekst:
          "Weet je niet waar je moet beginnen met een vermoeden of een diagnose? De wegwijzer loopt de vijf stappen met je af.",
        van: "Connectopia",
        link: { tekst: "Naar de wegwijzer", href: "/wegwijzer" },
      },
    ],
  },
  {
    slug: "momenten",
    naam: "Momenten",
    ondertitel: "Een foto, een zin, een klein feest",
    icoon: "📷",
    kleur: "blue",
    uitleg:
      "Het luchtige bord. Iets dat gelukt is, een bouwwerk waar je kind trots op is, een zin die je bijbleef. Klein mag hier groot zijn.",
    waarvoor: [
      "Iets dat gelukt is",
      "Een foto van een maaksel",
      "Een zin die bleef hangen",
    ],
    briefjes: [
      {
        tekst:
          "Heeft je kind iets gemaakt waar het trots op is? Stuur de foto mee met je briefje, dan hangt ze hier.",
        van: "Connectopia",
        label: "Voorbeeld",
      },
      {
        tekst:
          "“Niet elk kind past in hetzelfde hokje. Sommige kinderen hebben gewoon een grotere speeltuin nodig.”",
        van: "Connectopia",
      },
    ],
  },
];

export const bordPerSlug = (slug: string) =>
  borden.find((bord) => bord.slug === slug);
