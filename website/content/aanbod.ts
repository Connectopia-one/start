/*
  Ons aanbod. Elk traject is één blok hieronder.
  Een traject toevoegen of aanpassen doe je hier; de pagina past zich vanzelf aan.
*/

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
};

/* Het blok over de gratis proefles, bovenaan de aanbodpagina. */
export const proefles = {
  titel: "Eerst eens komen proeven?",
  tekst:
    "Je kind mag vrijblijvend een gratis proefles meedoen. Zo voelt het zelf of de groep en de manier van werken passen, voor je iets vastlegt.",
  knopTekst: "Schrijf in voor een gratis proefles",
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

export const trajecten: Traject[] = [
  {
    slug: "externe-plusklas",
    naam: "Externe plusklas",
    ondertitel: "De hele dag ontdekken in Hasselt",
    kleur: "green",
    icoon: "🚀",
    leeftijd: "6 tot 12 jaar",
    prijs: "€50 per dag",
    prijsWas: "€60",
    regels: [
      { label: "Wanneer", waarde: "Dinsdag, 9u – 15u" },
      { label: "Start", waarde: "Dinsdag 15 september 2026" },
      {
        label: "Waar",
        waarde: "Atheneum Hasselt, Kleine-Breemstraat 33, 3500 Hasselt",
      },
      { label: "Opbouw", waarde: "3 trajecten van telkens 10 dagen" },
    ],
    foto: {
      bestand: "externe-plusklas.jpg",
      beschrijving:
        "Drie kinderen in de plusklas tonen trots hun zelfgemaakte schaakspel en kartonnen molen.",
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
      tekst: "Later instappen kan, ook in oktober is er nog plaats.",
      data: ["Dinsdag 6 oktober 2026"],
    },
  },
  {
    slug: "pluswerking-woensdag",
    naam: "Pluswerking woensdag",
    ondertitel: "Voorbereiding op de examencommissie",
    kleur: "purple",
    icoon: "🎓",
    leeftijd: "6 tot 12 jaar",
    prijs: "€25 per 3 uur",
    prijsWas: "€30",
    regels: [
      { label: "Wanneer", waarde: "Woensdagvoormiddag, 9u – 12u" },
      { label: "Start", waarde: "Woensdag 16 september 2026" },
      { label: "Waar", waarde: "Genk T2 Campus, Thor Park 8040, 3600 Genk" },
    ],
    foto: {
      bestand: "pluswerking-woensdag.jpg",
      beschrijving:
        "Twee kinderen spelen samen een zelfgebouwd schaakspel in de lichte hal van T2 Campus.",
    },
    tekst:
      "Meer schoolse uitdaging en voorbereiding op de examencommissie, zowel voor kinderen die schoolgaand zijn als voor kinderen in thuisonderwijs.",
    punten: [
      "Kleine groepjes met persoonlijke begeleiding",
      "Inhoud op maat",
      "Voorbereiden, oefenen en begrijpen",
    ],
    instappen: {
      tekst: "Later instappen kan, ook in oktober is er nog plaats.",
      data: ["Woensdag 7 oktober 2026"],
    },
  },
  {
    slug: "pluswerking-zaterdag",
    naam: "Pluswerking zaterdag",
    ondertitel: "Creativiteit en techniek laten samenkomen",
    kleur: "orange",
    icoon: "🎨",
    leeftijd: "6 tot 12 jaar",
    prijs: "€25 per 3 uur",
    prijsWas: "€30",
    regels: [
      { label: "Wanneer", waarde: "Zaterdagvoormiddag, 9u – 12u" },
      { label: "Start", waarde: "Zaterdag 12 september 2026" },
      { label: "Waar", waarde: "Vilderstraat 28, 3500 Hasselt" },
    ],
    foto: {
      bestand: "pluswerking-zaterdag.jpg",
      beschrijving:
        "Een kind houdt een groene ballon boven een tekening tijdens een proefje met statische elektriciteit.",
    },
    tekst:
      "Voor kinderen die extra uitdaging zoeken en een creatieve uitlaatklep nodig hebben. Verbeelding aanzetten, vaardigheden ontdekken en vooral: plezier beleven.",
    punten: [
      "Creatief denken en techniek ontdekken",
      "Experimenteren, bouwen en ontwerpen",
    ],
    instappen: {
      tekst: "Later instappen kan, ook in oktober is er nog plaats.",
      data: ["Zaterdag 3 oktober 2026"],
    },
  },
  {
    slug: "young-engineers",
    naam: "Young Engineers",
    ondertitel: "Naschoolse activiteiten rond STEM en techniek",
    kleur: "blue",
    icoon: "⚙️",
    leeftijd: "6 tot 12 jaar",
    prijs: "€20 per les",
    prijsWas: "€25",
    regels: [
      { label: "Dinsdag", waarde: "15u20 – 16u35, Atheneum Hasselt" },
      {
        label: "Woensdag",
        waarde: "13u – 14u15 of 14u15 – 15u30, Genk T2 Campus",
      },
      {
        label: "Zaterdag",
        waarde: "13u – 14u15 of 14u15 – 15u30, Vilderstraat 28 Hasselt",
      },
      { label: "Duur", waarde: "Eén les duurt 1u15" },
    ],
    foto: {
      bestand: "young-engineers.jpg",
      beschrijving:
        "Een zelfgebouwde constructie van lego met een motor, een tandwiel en twee bakjes die op en neer gaan.",
    },
    tekst:
      "Ontdekken, experimenteren, bouwen en vooral plezier maken. Met LEGO® en techniek echte uitdagingen aangaan, samenwerken en trots zijn op je werk.",
    instappen: {
      tekst: "Je kan het hele jaar door instappen, ook in oktober.",
    },
  },
  {
    slug: "vakantiekampen",
    naam: "Vakantiekampen",
    ondertitel: "Tijdens elke schoolvakantie",
    kleur: "green",
    icoon: "🏕️",
    leeftijd: "6 tot 12 jaar",
    prijs: "€40 per dag",
    regels: [
      { label: "Uren", waarde: "Elke dag van 9u tot 15u" },
      {
        label: "Herfstvakantie, Hasselt",
        waarde:
          "Maandag 2 en dinsdag 3 november 2026 bij Level X 28, thema Young Engineer Held",
      },
      {
        label: "Herfstvakantie, Genk",
        waarde:
          "Woensdag 4 en donderdag 5 november 2026 op T2 Campus, thema Creatieve duizendpoot: van techniek tot design",
      },
      {
        label: "Daarna",
        waarde: "Kerst-, krokus-, paas- en zomervakantie",
      },
      { label: "Plaatsen", waarde: "Beperkt, reserveer tijdig je plaatsje" },
    ],
    foto: {
      bestand: "vakantiekampen.jpg",
      beschrijving:
        "Een kind drukt op een knop bij een proefopstelling met een gele onderzeeër in een waterbak.",
    },
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
