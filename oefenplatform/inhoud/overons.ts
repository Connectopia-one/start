/*
  De pagina "Over ons" — /over-ons

  Alles op deze pagina is gewone tekst. Wil je iets aanpassen, bijzetten of
  weghalen, dan hoef je geen code te kennen: pas de zinnen hieronder aan.
  Een lijst is een rij regels tussen vierkante haken; je mag er een regel
  bijzetten of er een weghalen, zolang elke regel tussen aanhalingstekens
  staat en er een komma achter komt.

  Eén ding staat hier met opzet níet in: de lijst met vakken die we aanbieden.
  Die stond hier tot 11 oktober 2026 met de hand getypt (vijf vakken) en was
  toen al een jaar achterhaald. De pagina telt die vakken nu zelf uit het
  platform, per categorie, dus hij kan niet meer verouderen. Zet een nieuw vak
  dus gewoon in Beheer; deze pagina volgt vanzelf.
*/

export const overOns = {
  label: "Over ons",
  titel: "📚 Over ons oefenplatform",
  aanhef: "Beste ouder, begeleider of leerling,",
  welkom:
    "Welkom op het oefenplatform van Connectopia vzw! Wij zijn een vereniging zonder winstoogmerk die zich met hart en ziel inzet voor kinderen en jongeren die net dat beetje extra nodig hebben.",

  /* Staat bovenaan, want het is de vraag waar iedereen mee binnenkomt: wat is
     dit precies? Zie de zin onder elk hoofdstuk in components/Leidraad.tsx;
     die twee moeten hetzelfde zeggen. */
  leidraad: {
    kop: "🧭 Wat dit platform is",
    alinea: [
      "Wij volgen de officiële vakfiches van de Examencommissie, vak per vak en hoofdstuk per hoofdstuk. Ga je bij ons door een vak heen, dan heb je alle leerstof gezien die op dat examen gevraagd wordt: je vinkt dezelfde lijst af.",
      "Zie het daarom als een uitgebreide leidraad, niet als je enige bron. Blijf naast het oefenen zelf genoeg lezen, opzoeken en bijschrijven, net zoals een leerkracht naast zijn handboek nog andere bronnen gebruikt.",
    ],
  },

  bijzonder: {
    kop: "🧠 Wat maakt ons bijzonder?",
    alinea1:
      "Connectopia vzw richt zich in de eerste plaats op hoogbegaafde (HB) en uitzonderlijk hoogbegaafde (UHB) kinderen, vaak met dubbele diagnoses zoals ASS (autismespectrumstoornis) of ADHD. Wij begrijpen dat deze kinderen op een andere manier leren en dat zij nood hebben aan duidelijkheid, structuur en rust.",
    alinea2: "Daarom is ons oefenplatform bewust prikkelarm opgebouwd:",
    punten: [
      "Geen overbodige animaties of afleidende kleuren.",
      "Heldere, rustige lay-out.",
      "Duidelijke instructies en overzichtelijke oefeningen.",
    ],
    slot:
      "Maar: het platform is er voor iedereen! Of je kind nu hoogbegaafd is, extra ondersteuning nodig heeft, of gewoon wat bij wil oefenen voor de examens — iedereen is welkom.",
  },

  leerstof: {
    kop: "📖 Hoe is onze leerstof samengesteld?",
    intro: "Ons oefenaanbod is niet zomaar uit de lucht gegrepen. We baseren ons op:",
    punten: [
      "de officiële vakfiches van de Examencommissie voor de 1ste, 2de en 3de graad;",
      "de minimumdoelen van het lager onderwijs voor het 5de en 6de leerjaar.",
    ],
    slot:
      "Al het materiaal wordt door ons zelf samengesteld en geredigeerd. We volgen de officiële vakfiches op de voet, zodat jouw kind gericht kan oefenen op wat écht belangrijk is.",
    link: "Bekijk per niveau en per vak welke doelen we gebruiken",
  },

  aanbod: {
    kop: "📖 Wat bieden we momenteel aan?",
    /* De cijfers en de vakken eronder worden geteld, niet getypt. */
    intro:
      "Hieronder staat wat er vandaag op het platform klaarstaat. Deze lijst komt rechtstreeks uit het platform zelf, dus hij loopt nooit achter.",
    slot:
      "Welke vakken bij welke studierichting horen, staat bovenaan de pagina van elke categorie. We breiden het aanbod verder uit.",
    leeg: "Dit onderdeel is nog in opbouw.",
  },

  voorWie: {
    kop: "👥 Voor wie is dit platform bedoeld?",
    intro: "Het platform is geschikt voor:",
    punten: [
      "kinderen en jongeren die zich voorbereiden op de examens van de Examencommissie;",
      "hoogbegaafde kinderen die extra uitdaging of oefening nodig hebben;",
      "leerlingen met ASS, ADHD of andere neurodivergente profielen die baat hebben bij een prikkelarme leeromgeving;",
      "wie thuis onderwijs volgt, of les krijgt aan huis of in een ziekenhuis;",
      "kinderen in het 5de en 6de leerjaar die alvast willen proeven van de secundaire leerstof;",
      "leerkrachten en begeleiders die oefenmateriaal zoeken bij een vakfiche.",
    ],
  },

  prijs: {
    kop: "💶 Hoeveel kost het?",
    /* Het bedrag en de tijdelijke prijs komen uit lib/prijs.ts, zodat ze maar
       op één plaats aangepast moeten worden. */
    uitleg:
      "per schooljaar voor een account. Met één account kunnen meerdere kinderen uit hetzelfde gezin gebruikmaken van het platform. Zo kan je kostenefficiënt meerdere kinderen tegelijk laten oefenen.",
    waarschuwing:
      "deel je inloggegevens niet met derden. Elk account is strikt persoonlijk en bedoeld voor gezinsgebruik.",
  },

  gratis: {
    kop: "🎁 Gratis toegang voor Connectopia-leden",
    tekst:
      "Kinderen die bij ons aangesloten zijn via een plusklas, pluswerking of ander Connectopia-traject ontvangen gratis toegang tot alle materialen op het platform. Bovendien krijgen zij ook persoonlijke begeleiding op maat. Zo zorgen we ervoor dat elke leerling de ondersteuning krijgt die hij of zij nodig heeft.",
  },

  fouten: {
    kop: "💬 Fouten ontdekt? Laat het ons weten!",
    tekst:
      "Wij zijn een vzw en maken dit materiaal uit eigen beweging en met veel enthousiasme. Toch kan het gebeuren dat er een foutje insluipt. Onderaan elk hoofdstuk staat een meldknop, en bij elke vraag een klein vlaggetje: daarmee komt het meteen bij ons terecht. Mailen mag ook:",
    mail: "info@matmgroep.com",
    slot: "Wij bekijken het zo snel mogelijk en passen het aan waar nodig.",
  },

  afsluiter: {
    dank: "🙏 Hartelijk dank voor je vertrouwen!",
    tekst:
      "Wij hopen dat jouw kind met veel plezier en succes zal oefenen op ons platform. Samen maken we leren leuk, rustig en doelgericht!",
    groet: "Met vriendelijke groeten,",
    naam: "Team Connectopia vzw",
  },
};
