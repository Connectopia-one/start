/*
  Ons aanbod. Elk traject is één blok hieronder.
  Een traject toevoegen of aanpassen doe je hier; de pagina past zich vanzelf aan.
*/

import type { Veld } from "@/content/formulier";

export type Traject = {
  /* Kort kenmerk voor het webadres van het aanvraagformulier. Alleen kleine letters en streepjes. */
  slug: string;
  naam: string;
  ondertitel: string;
  kleur: "green" | "orange" | "purple" | "blue";
  icoon: string;
  leeftijd: string;
  prijs?: string;
  prijsWas?: string;
  regels: { label: string; waarde: string }[];
  tekst: string;
  punten?: string[];
  /*
    De foto boven het traject. Zet het bestand in  public/fotos/
    en vul hier alleen de bestandsnaam in. Laat weg als je geen foto wil.
  */
  foto?: { bestand: string; beschrijving: string };
  /* Extra instapmomenten: zo zien ouders dat later starten ook kan. */
  instappen?: {
    tekst: string;
    data?: string[];
  };
  /*
    Vragen die alleen bij dít traject op het aanvraagformulier komen, boven
    het vakje "Je vraag of boodschap". Bij de kampen vragen we zo meteen om
    welke dagen het gaat; zonder die vraag moet je dat achteraf per mail
    navragen. Dezelfde vorm als de gewone vragen in content/formulier.ts.
  */
  extraVragen?: Veld[];
  /*
    Knoppen naar een andere website, onderaan het traject naast de gewone
    knoppen. Ze openen in een nieuw tabblad.
  */
  links?: { tekst: string; link: string }[];
  /*
    Schrijf je voor dit traject in op een andere website, zet dat adres dan
    hier. De knop "Inschrijven" gaat dan daarheen in plaats van naar ons
    eigen formulier.
  */
  inschrijvenLink?: string;
};

/*
  Onze eigen Young Engineers-site (Demerland), aangepast aan Connectopia.
  Kim gaf beide adressen door op 21 oktober 2026.
*/
export const youngEngineers = {
  site: "https://www.demerland.e2youngengineers.com/",
  inschrijven: "https://www.demerland.e2youngengineers.com/inschrijven/",
};

/* Het blok over de gratis proefles, bovenaan de aanbodpagina. */
export const proefles = {
  titel: "Kom gerust eerst een keertje gratis meedoen",
  tekst:
    "Je kind mag vrijblijvend een keertje gratis meedoen. Zo voelt het zelf of de groep en de manier van werken passen, voor je iets vastlegt.",
  knopTekst: "Kom een keertje gratis meedoen",
};

/*
  De voorbehouden plaatsen voor gezinnen met een verhoogde tegemoetkoming.

  Kim op 14 oktober 2026: "we zouden bij de kampen en de lessen die we
  aanbieden ergens een stukje moeten inzetten dat we een paar plaatsjes vrij
  houden voor personen met een VT statuut (korting 50%)". Op 11 oktober zei ze
  nog dat dit enkel in gesprek ging; op 14 oktober mag het wel op de website,
  maar bewust niet op de posters en de flyers, want die verwijzen toch naar
  de site.

  Het bedrag staat er niet in cijfers bij, zodat deze tekst klopt blijft als
  een tarief verandert. Eén papier is er wel nodig: het attest.
*/
export const voorbehouden = {
  titel: "Een paar plaatsen houden we vrij",
  tekst:
    "Bij elk kamp en elke werking houden we een aantal plaatsen vrij voor gezinnen met een verhoogde tegemoetkoming. Die plaatsen kosten de helft. Vraag er gerust naar bij je aanvraag, dan kijken we samen of er nog een vrij is. Het enige wat we nodig hebben is je attest van de verhoogde tegemoetkoming.",
};

export const aanbodTekst = {
  label: "Ons aanbod",
  titel: "Samen ontdekken, leren, creëren en groeien",
  tekst:
    "Alles wat we zelf organiseren, op één pagina. Voor nieuwsgierige kinderen die net dat beetje extra uitdaging, begrip of ruimte nodig hebben.",
  tariefNota:
    "Vanaf schooljaar 2026–2027 zijn we officieel een vzw en verlagen we onze prijzen.",
  inschrijvenTekst: "Interesse of inschrijven?",
};

/*
  Wat er bij de prijs inbegrepen zit, en wat dus níét apart aangerekend
  wordt. Kim gaf dat door op 28 september 2026, nadat bleek dat andere
  aanbieders die dingen als extra's verkopen terwijl het bij ons in het
  dagtarief zit. Het stond nergens op de site, en wie het niet weet,
  vergelijkt enkel bedragen.

  Dit gaat over de plusklas en de pluswerking; bij een kamp, de Ontdekclub
  of een les Young Engineers hoort geen schooloverleg. Titel zoals op het
  drukwerk van 19 oktober 2026.
*/
export const inbegrepen = {
  titel: "Bij de plusklas en de pluswerking zit ook inbegrepen:",
  tekst:
    "Je betaalt bij ons het dagtarief, en verder niets. Wat andere organisaties apart aanrekenen, zit bij ons in de prijs.",
  punten: [
    "Al het materiaal waarmee de kinderen werken",
    "Gesprekken met de school van je kind, gratis",
    "Verschillende overlegmomenten met jou als ouder",
    "Een keertje gratis meedoen voor je iets vastlegt",
  ],
};

export const trajecten: Traject[] = [
  {
    slug: "externe-plusklas",
    naam: "Externe plusklas",
    ondertitel: "De hele dag ontdekken in Hasselt",
    kleur: "green",
    icoon: "🚀",
    leeftijd: "6 tot 15 jaar",
    prijs: "€50 per dag",
    prijsWas: "€60",
    regels: [
      { label: "Wanneer", waarde: "Dinsdag, 9u – 15u" },
      {
        label: "Waar",
        waarde: "Atheneum Hasselt, Kleine-Breemstraat 33, 3500 Hasselt",
      },
    ],
    foto: {
      bestand: "externe-plusklas-geschiedenis.jpg",
      beschrijving:
        "Een dinsdag in de plusklas: op de tafels liggen boeken over geschiedenis, op het grote scherm staan grotschilderingen en de kinderen werken in kleine groepjes.",
    },
    tekst:
      "Onze plusklas is meer dan extra uitdaging. Het is een veilige haven waar gelijkgestemde kinderen samen een diepgaand leertraject aangaan, met aandacht voor het proces, de samenwerking en het plezier in leren.",
    punten: [
      "Brainstorm: samen ideeën bedenken en nieuwsgierigheid prikkelen",
      "Bijleren: nieuwe dingen ontdekken en kennis vergroten",
      "Uitwerken: ideeën omzetten in echte projecten en oplossingen",
      "Afgestemd op de noden en talenten van hoogbegaafde kinderen",
      "Regelmatig overleg met de school van je kind",
    ],
    instappen: {
      tekst:
        "Instappen kan altijd. Je kind kan op eender welke dinsdag starten.",
    },
  },
  {
    slug: "pluswerking-woensdag",
    naam: "Pluswerking woensdag",
    ondertitel: "Voorbereiding op de examencommissie",
    kleur: "purple",
    icoon: "🎓",
    leeftijd: "6 tot 15 jaar",
    prijs: "€25 per 3 uur",
    prijsWas: "€30",
    regels: [
      { label: "Wanneer", waarde: "Woensdagvoormiddag, 9u – 12u" },
      { label: "Waar", waarde: "Genk T2 Campus, Thor Park 8040, 3600 Genk" },
    ],
    foto: {
      bestand: "pluswerking-woensdag-oefenplatform.jpg",
      beschrijving:
        "Kinderen van de pluswerking op woensdag in een klaslokaal van T2 Campus, met een vraag uit het oefenplatform op het grote scherm.",
    },
    tekst:
      "Meer schoolse uitdaging en voorbereiding op de examencommissie, zowel voor kinderen die schoolgaand zijn als voor kinderen in thuisonderwijs.",
    punten: [
      "Kleine groepjes met persoonlijke begeleiding",
      "Inhoud op maat",
      "Voorbereiden, oefenen en begrijpen",
    ],
    instappen: {
      tekst:
        "Instappen kan altijd. Je kind kan op eender welke woensdag starten.",
    },
  },
  /*
    De Ontdekclub vervangt sinds 19 oktober 2026 de pluswerking op zaterdag.
    Young Engineers is er één van de hoeken; de aparte les Young Engineers
    loopt op hetzelfde moment in een eigen lokaal (zie hieronder).
    Oude links naar pluswerking-zaterdag sturen door, zie next.config.ts.
  */
  {
    slug: "ontdekclub",
    naam: "De Ontdekclub",
    ondertitel: "Bouwen, knutselen, spelen en elkaar ontmoeten",
    kleur: "orange",
    icoon: "🧩",
    leeftijd: "6 tot 15 jaar",
    prijs: "€25 per keer",
    prijsWas: "€30",
    regels: [
      {
        label: "Zaterdag",
        waarde: "9u – 12u, Level X 28, Vilderstraat 28, 3500 Hasselt",
      },
      {
        label: "Woensdag",
        waarde: "13u – 16u, T2 Campus, Thor Park 8040, 3600 Genk",
      },
      { label: "Ouders", waarde: "Je mag gratis blijven, in onze ouderruimte" },
    ],
    foto: {
      bestand: "pluswerking-zaterdag.jpg",
      beschrijving:
        "Een kind houdt een groene ballon boven een tekening tijdens een proefje met statische elektriciteit.",
    },
    tekst:
      "In de Ontdekclub kiest je kind zelf waar het aan werkt. Er is ruimte voor wie graag praat en voor wie liever stil bezig is. De groep is klein, de ruimte is prikkelarm, en elk kind vindt er kinderen die op dezelfde golflengte zitten. En jij mag blijven: drink een koffie met andere ouders, doe mee aan een spel of werk rustig aan je laptop. Thuiswerken mag hier ook.",
    punten: [
      "Bouwen en techniek, samen met Young Engineers: robots, proefjes en bouwpakketten",
      "Crea: verven, knippen, plakken en bouwen met karton",
      "Spellen: schaken en gezelschapsspellen, ook voor twee",
      "Een stille hoek om even rustig te lezen of te puzzelen",
    ],
    instappen: {
      tekst:
        "Instappen kan altijd. Je kind kan op eender welke zaterdag of woensdag starten.",
    },
    links: [
      { tekst: "Meer over Young Engineers", link: youngEngineers.site },
    ],
  },
  {
    slug: "young-engineers",
    naam: "Young Engineers",
    ondertitel: "Bouwen, programmeren en uitvinden",
    kleur: "blue",
    icoon: "⚙️",
    leeftijd: "6 tot 15 jaar",
    prijs: "€20 per les",
    prijsWas: "€25",
    regels: [
      {
        label: "Zaterdag",
        waarde: "10u – 11u30, Level X 28, Vilderstraat 28, Hasselt",
      },
      {
        label: "Woensdag",
        waarde: "13u30 – 14u45, T2 Campus, Thor Park 8040, Genk",
      },
      {
        label: "Samen met",
        waarde: "Op hetzelfde moment als de Ontdekclub, in een eigen lokaal",
      },
    ],
    foto: {
      bestand: "young-engineers.jpg",
      beschrijving:
        "Een zelfgebouwde constructie van lego met een motor, een tandwiel en twee bakjes die op en neer gaan.",
    },
    tekst:
      "Ontdekken, experimenteren, bouwen en vooral plezier maken. Met LEGO® en techniek echte uitdagingen aangaan, samenwerken en trots zijn op je werk. De les loopt tegelijk met de Ontdekclub, dus broers en zussen kunnen op hetzelfde moment komen.",
    instappen: {
      tekst:
        "Instappen kan altijd. Je kiest zelf of je op zaterdag of woensdag start.",
    },
    inschrijvenLink: youngEngineers.inschrijven,
    links: [{ tekst: "Naar onze Young Engineers-site", link: youngEngineers.site }],
  },
  {
    slug: "vakantiekampen",
    naam: "Vakantiekampen",
    ondertitel: "Tijdens elke schoolvakantie",
    kleur: "green",
    icoon: "🏕️",
    leeftijd: "6 tot 15 jaar",
    prijs: "€40 per dag",
    regels: [
      { label: "Uren", waarde: "Elke dag van 9u tot 15u" },
      {
        label: "Herfstvakantie, Hasselt",
        waarde:
          "Maandag 2 en dinsdag 3 november 2026 bij Level X 28, Vilderstraat 28, thema Young Engineer Held",
      },
      {
        label: "Herfstvakantie, Genk",
        waarde:
          "Woensdag 4 en donderdag 5 november 2026 op T2 Campus, thema Creatieve duizendpoot: van techniek tot design",
      },
      {
        label: "Kerstvakantie, Hasselt",
        waarde:
          "Maandag 21 tot en met woensdag 23 december 2026 en maandag 28 tot en met woensdag 30 december 2026, in de Vilderstraat 28. Deze kampen gaan door als er genoeg inschrijvingen zijn, dus laat gerust nu al weten welke dagen je zou willen.",
      },
      {
        label: "Daarna",
        waarde: "Krokus-, paas- en zomervakantie",
      },
      { label: "Plaatsen", waarde: "Beperkt, reserveer tijdig je plaatsje" },
    ],
    foto: {
      bestand: "vakantiekampen.jpg",
      beschrijving:
        "Een kind drukt op een knop bij een proefopstelling met een gele onderzeeër in een waterbak.",
    },
    extraVragen: [
      {
        naam: "Herfstvakantie welke dagen",
        label: "Herfstvakantie — welke dagen wil je erbij zijn?",
        soort: "keuzes",
        hulp: "Je mag er zoveel aankruisen als je wil. Elke dag is een volledige dag van 9u tot 15u.",
        keuzes: [
          {
            naam: "Hasselt maandag 2 november",
            label: "Hasselt, maandag 2 november — Young Engineer Held",
          },
          {
            naam: "Hasselt dinsdag 3 november",
            label: "Hasselt, dinsdag 3 november — Young Engineer Held",
          },
          {
            naam: "Genk woensdag 4 november",
            label: "Genk, woensdag 4 november — Creatieve duizendpoot",
          },
          {
            naam: "Genk donderdag 5 november",
            label: "Genk, donderdag 5 november — Creatieve duizendpoot",
          },
        ],
      },
      {
        naam: "Kerstvakantie welke dagen",
        label: "Kerstvakantie — welke dagen zou je willen?",
        soort: "keuzes",
        hulp: "Deze kampen gaan door in Hasselt, in de Vilderstraat 28, als er genoeg inschrijvingen zijn. Kruis gerust nu al aan wat jullie zou passen, dan weten we of we ze kunnen laten doorgaan.",
        keuzes: [
          { naam: "Kerst maandag 21 december", label: "Maandag 21 december" },
          { naam: "Kerst dinsdag 22 december", label: "Dinsdag 22 december" },
          { naam: "Kerst woensdag 23 december", label: "Woensdag 23 december" },
          { naam: "Kerst maandag 28 december", label: "Maandag 28 december" },
          { naam: "Kerst dinsdag 29 december", label: "Dinsdag 29 december" },
          { naam: "Kerst woensdag 30 december", label: "Woensdag 30 december" },
        ],
      },
      {
        naam: "Later kamp",
        label: "Nog geen van deze?",
        soort: "keuzes",
        keuzes: [
          {
            naam: "Een latere vakantie",
            label: "Hou me op de hoogte van een volgend kamp",
          },
        ],
      },
    ],
    tekst:
      "Een vakantie vol nieuwsgierigheid, creativiteit, techniek en uitdaging. Nieuwe kampen en thema's maken we telkens bekend via de website en de sociale media.",
    punten: [
      "Ontdekken: nieuwe dingen onderzoeken en vragen stellen",
      "Maken en experimenteren: van een idee naar iets dat écht werkt",
      "Creatief denken: eigen oplossingen bedenken en uitproberen",
      "Hun brein uitdagen: spelen, denken, bouwen en leren combineren",
      "Samen groeien: in kleine groepen en met aandacht voor ieder kind",
    ],
  },
];
