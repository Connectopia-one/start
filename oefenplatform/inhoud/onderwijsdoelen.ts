/*
  De pagina "Waarop is dit gebaseerd?" — /onderwijsdoelen

  Alles op deze pagina is gewone tekst. Wil je iets aanpassen, bijkomen of
  weghalen, dan hoef je geen code te kennen: pas de zinnen hieronder aan, of
  zet er een blok bij in dezelfde vorm.

  De officiële adressen (`bron`) staan er met opzet niet allemaal in. Vul ze
  aan zodra je ze bij de hand hebt; laat je een `bron` weg, dan toont de pagina
  gewoon geen link en klopt er nog altijd alles.
*/

export const doelenTekst = {
  label: "Waarop is dit gebaseerd?",
  titel: "De doelen achter onze oefeningen",
  intro:
    "De oefeningen maken we zelf, maar de leerstof verzinnen we niet. Voor elk niveau vertrekken we van de officiële doelen van de Vlaamse overheid en van de vakfiches van de Examencommissie. Hieronder staat per niveau waar we ons precies op baseren, zodat je kan nakijken of het oefenen aansluit bij wat er van je kind verwacht wordt.",
  /* Staat onderaan, onder de lijst. */
  eigenWoordenKop: "In onze eigen woorden",
  eigenWoorden:
    "De officiële teksten zijn geschreven voor scholen en inspecteurs, niet voor kinderen of ouders. Wij lezen ze en schrijven de leerstof in gewone taal om. De oefeningen en de leerbundels zijn dus van ons; de doelen erachter zijn van de overheid en van de Examencommissie. Waar we een officiële tekst samenvatten, staat erbij waar die vandaan komt.",
  foutKop: "Iets gevonden dat niet klopt?",
  foutTekst:
    "Merk je dat een hoofdstuk iets mist of iets bevat dat er niet in hoort? Laat het ons weten, dan kijken we het na.",
  foutMail: "info@matmgroep.com",
  /* Staat boven de documenten, en legt uit waarom we ze zelf bewaren. */
  bestandenUitleg:
    "Hieronder staat bij elk vak het officiële document waarop we ons gebaseerd hebben. We bewaren daar met opzet onze eigen kopie van, met de datum erbij. Op de site van de Examencommissie staan namelijk honderden fiches, en dan weet je nog niet welke wij precies gebruikt hebben. Zie je dat een document verouderd is, laat het ons dan weten.",
  /* Wijst door naar de pagina met de overige links. */
  materiaalTekst:
    "Op onze pagina met handig materiaal staan daarnaast nog naslagwerken en oefensites. Die is ook voor iedereen te bekijken, zonder account.",
};

export type DoelenBlok = {
  /* De korte naam van het niveau: start, spark, boost of beyond. Daarmee
     zoekt de pagina de opgeladen fiches bij het juiste blok. */
  slug: "start" | "spark" | "boost" | "beyond";
  /* Het niveau waar dit over gaat, zoals het op de startpagina staat. */
  niveau: string;
  emoji: string;
  /* Waar de doelen vandaan komen, in één zin. */
  herkomst: string;
  /* Een officieel webadres. Laat leeg als je het nog niet hebt. */
  bron?: string;
  bronTekst?: string;
  /* Per vak: wat we gebruiken, en hoe ver we ermee staan. */
  vakken: { naam: string; doelen: string; stand?: string }[];
};

export const doelenBlokken: DoelenBlok[] = [
  {
    slug: "start",
    niveau: "Start — 5de en 6de leerjaar",
    emoji: "🌱",
    herkomst:
      "De minimumdoelen van het lager onderwijs van de Vlaamse overheid, die gelden sinds 1 september 2025. Het richtpunt is wat een kind aan het einde van het zesde leerjaar moet kennen.",
    vakken: [
      {
        naam: "Wiskunde",
        doelen:
          "De zes domeinen van de minimumdoelen: getallenkennis, bewerkingen, meten en metend rekenen, meetkunde, kansrekenen en statistiek, en probleemoplossend denken en vraagstukken.",
      },
      {
        naam: "Nederlands",
        doelen:
          "De vijf domeinen: lezen, schrijven, mondeling taalgebruik, taalsysteem en taalgebruik, en literatuur. Spelling zit bij taalsysteem en taalgebruik.",
      },
      {
        naam: "Wetenschap en techniek",
        doelen: "De vier gebieden: biologie, chemie, natuurkunde en techniek.",
      },
      {
        naam: "Geschiedenis",
        doelen:
          "De doelen rond historisch bewustzijn, in drie hoofdstukken: tijd en tijdlijn, van de prehistorie tot de Romeinen, en van de middeleeuwen tot nu.",
      },
      {
        naam: "Aardrijkskunde",
        doelen:
          "De doelen rond ruimtelijk bewustzijn, in drie hoofdstukken: kaartlezen en oriëntatie, België, en Europa en de wereld.",
      },
      {
        naam: "Engels",
        doelen:
          "Woordenschat en de basis van de grammatica: jezelf voorstellen, to be en to have, de tegenwoordige tijd, en zinnen bouwen.",
      },
    ],
  },
  {
    slug: "spark",
    niveau: "Spark — 1ste en 2de middelbaar",
    emoji: "✨",
    herkomst:
      "De officiële vakfiches van de Examencommissie voor de 1ste graad A-stroom. Die fiche zegt per vak welke onderdelen er op het examen komen, en dat is precies onze indeling in hoofdstukken.",
    vakken: [
      {
        naam: "Wiskunde",
        doelen:
          "De zeven onderdelen van de fiche: probleemoplossend denken, wiskundige redeneringen en uitspraken, getallenleer, meetkunde en metend rekenen, relaties en verandering, data en onzekerheid, en verzamelingen.",
        stand: "Volledig: negen hoofdstukken, elk met een deel 1 en een deel 2, en bij elk een leerbundel.",
      },
      {
        naam: "Geschiedenis",
        doelen:
          "De onderdelen van de fiche: het historisch referentiekader, bronnen, en de periodes van de prehistorie tot nu.",
        stand: "Volledig: zes thema's, elk met een deel 1 en een deel 2, en bij elk een leerbundel.",
      },
    ],
  },
  {
    slug: "boost",
    niveau: "Boost — 3de en 4de middelbaar",
    emoji: "🚀",
    herkomst: "De vakfiches van de Examencommissie voor de 2de graad.",
    vakken: [{ naam: "Alle vakken", doelen: "In opbouw.", stand: "Nog niet beschikbaar." }],
  },
  {
    slug: "beyond",
    niveau: "Beyond — 5de en 6de middelbaar",
    emoji: "🌍",
    herkomst: "De vakfiches van de Examencommissie voor de 3de graad.",
    vakken: [{ naam: "Alle vakken", doelen: "In opbouw.", stand: "Nog niet beschikbaar." }],
  },
];

/*
  De korte uitleg op de startpagina. Vier zinnen, meer niet: wie net binnenkomt
  wil weten wat dit is, niet alles lezen. De rest staat op /onderwijsdoelen en
  op /over-ons.
*/
export const startUitleg = {
  kop: "Wat is dit?",
  punten: [
    "Wij zijn Connectopia vzw en we maken dit oefenplatform zelf.",
    "De leerstof volgt de minimumdoelen van de Vlaamse overheid en de vakfiches van de Examencommissie.",
    "Je oefent vooral met meerkeuzevragen, aangevuld met invulvragen en waar-of-niet.",
    "Bij elk hoofdstuk hoort een leerbundel met de theorie, zodat je de leerstof ook kan leren en niet enkel kan testen.",
  ],
  linkTekst: "Bekijk welke doelen we gebruiken",
  link: "/onderwijsdoelen",
};

/*
  De zin onder 🧱 Basis op de startpagina. Basis is herhaling van de
  bouwstenen, los van een leerjaar.
*/
export const basisUitleg =
  "Nog niet vlot met de komma, maten, breuken of ggd en kgv? Hier herhaal je de bouwstenen stap voor stap, met een leerbundel en oefeningen. Voor elk niveau.";
