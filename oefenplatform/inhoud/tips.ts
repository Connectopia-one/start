/*
  De pagina "Zo gebruiken wij het" — /tips

  Geen uitleg over welk knopje wat doet. Dit is hoe wíj met het platform
  werken, als richtlijn. Iedereen is vrij om er zijn eigen manier van te
  maken, en dat staat er ook uitdrukkelijk bij.

  Alles op deze pagina is tekst, dus je mag hier gewoon in schrijven zonder
  dat er iets stuk kan. Een stap bijzetten of weghalen doe je in de lijst
  `stappen`: elke stap heeft een korte kop en een stukje uitleg. De nummers
  komen er vanzelf bij op de pagina.
*/

export const tipsTekst = {
  label: "Zo gebruiken wij het",
  titel: "Tips om met het platform te werken",
  intro:
    "Dit is geen handleiding met knopjes. Het is hoe wij zelf met het platform werken, als richtlijn. Gebruik het als een draad om aan vast te houden, maar iedereen is vrij om te kiezen hoe hij ermee omgaat. Werkt een andere volgorde beter voor jouw kind, doe dat dan.",
  stappen: [
    {
      kop: "Kies een vak en open een hoofdstuk",
      tekst:
        "We beginnen met één vak en daarin één hoofdstuk. Niet drie vakken door elkaar: één hoofdstuk afwerken geeft veel meer rust en het gevoel dat er iets vooruitgaat.",
    },
    {
      kop: "Ga eerst door de tocht",
      tekst:
        "Bij elk hoofdstuk hoort een tocht: de leerstof in kleine haltes, met een opdrachtje tussendoor. Daar beginnen we, nog voor er één oefening gemaakt is.",
    },
    {
      kop: "Neem zelf notities tijdens de tocht",
      tekst:
        "Wij schrijven per onderdeeltje mee op. Zo heb je achteraf een eigen samenvatting, in je eigen woorden, en die blijft veel beter hangen dan een tekst die je enkel gelezen hebt.",
    },
    {
      kop: "Zoek de moeilijke stukken meteen uit",
      tekst:
        "Snap je een stukje niet goed, dan zoeken we het ter plekke verder op in plaats van door te gaan. Per onderdeeltje bijzoeken werkt beter dan achteraf nog eens het hele hoofdstuk herbekijken.",
    },
    {
      kop: "Maak een lijstje met moeilijke woorden",
      tekst:
        "Wij houden voor onszelf een woordenlijst bij met wat nieuw of lastig is. Die lijst is vaak het nuttigste blaadje van het hele hoofdstuk, en je gebruikt ze later opnieuw.",
    },
    {
      kop: "De lesbundel afdrukken mag, moeten hoeft niet",
      tekst:
        "Neem je graag notities op papier, dan kan je de lesbundel van het hoofdstuk afdrukken en erin schrijven. Werkt je kind liever op het scherm, dan laat je dat gewoon.",
    },
    {
      kop: "Daarna de oefeningen van deel 1",
      tekst:
        "Pas als de tocht gedaan is, maken we deel 1. Fouten horen erbij: bij elke vraag staat uitleg, en die lezen is een deel van het leren.",
    },
    {
      kop: "Zit deel 1 goed, dan naar deel 2",
      tekst:
        "Deel 2 is iets moeilijker dan deel 1. We gaan er pas naartoe als deel 1 echt gekend is, anders wordt het alleen maar lastig in plaats van uitdagend.",
    },
    {
      kop: "Rond af met de oefenbundel",
      tekst:
        "Is het hoofdstuk af, dan test je het nog eens met de oefenbundel die je kan afdrukken. Daarin staan andere vragen dan online, dus het is echt extra oefening bij dat hoofdstuk.",
    },
    {
      kop: "Sluit af met het examen over het hele vak",
      tekst:
        "Zijn alle hoofdstukken van een vak gedaan, dan maken we onderaan de vakpagina het examen over het hele vak. Daarin komen vragen uit alle hoofdstukken samen, en die worden elke keer opnieuw gekozen. Zo heb je telkens een andere versie van het examen en kan je het gerust een paar keer maken.",
    },
  ],
  /* Extra briefjes op het bord, na de stappen en zonder stapnummer. Kim,
     7 november 2026: liever een post-it die iets uitlegt dan een klein
     zinnetje onder het bord. Een briefje weghalen doe je hier in de lijst. */
  briefjes: [
    {
      label: "Goed om te weten",
      kop: "Deel 1 en deel 2 delen één oefenbundel",
      tekst:
        "Sommige hoofdstukken zijn online gesplitst in \"deel 1\" en \"deel 2\". Dat is enkel omdat er zoveel vragen zijn: het blijft één onderwerp, met één leerbundel en één oefenbundel. Bij deel 1 en bij deel 2 zie je dus dezelfde oefenbundel staan. Je maakt hem één keer, als je beide delen gedaan hebt.",
    },
    {
      label: "Tip bij dyslexie",
      kop: "Gaat lezen nog moeilijk? Laat voorlezen",
      tekst:
        "Zet in Mijn account bij je kind het vinkje voor voorlezen aan. Dan staat er bij elke vraag en bij de uitleg een knopje 🔊 Lees voor. De computer of tablet leest voor met zijn eigen stem. Dit is nog een uitprobeersel: het klinkt het best in Google Chrome op een computer, en bij formules en vreemde woorden kan de uitspraak eens mislopen.",
    },
  ],
  /* Blok voor gezinnen uit Nederland, onder het bord. Kim, 10 november 2026,
     na een review van een Nederlandse ouder die zocht welk niveau bij haar
     zoon paste. Wij blijven een Belgisch platform: Belgische woorden blijven
     staan, dit blok helpt enkel de weg vinden. Zet op null om het te
     verbergen: nederland: null, */
  nederland: {
    kop: "Kom je uit Nederland?",
    intro:
      "Welkom! Wij zijn een Belgisch platform en volgen de Vlaamse leerstof, met Belgische woorden en leerjaren in plaats van groepen. Een Vlaams kind begint in het 1ste leerjaar op zes jaar, net als in groep 3. Zo vind je ongeveer het juiste niveau:",
    tabelKoppen: ["Bij ons", "Vlaanderen", "Nederland, ongeveer"],
    tabel: [
      ["🧱 Basis", "herhaling, voor elk niveau", "herhaling, voor elk niveau"],
      ["🌱 Start", "5de en 6de leerjaar", "groep 7 en 8"],
      ["✨ Spark", "1ste en 2de middelbaar", "klas 1 en 2, vooral havo en vwo"],
      ["🚀 Boost", "3de en 4de middelbaar", "klas 3 en 4 havo of vwo"],
      ["🌍 Beyond", "5de en 6de middelbaar", "havo 5, vwo 5 en 6"],
    ],
    vakken: [
      {
        kop: "Past goed",
        tekst:
          "Wiskunde, Nederlands, Engels en wetenschap en techniek. Dat is grotendeels dezelfde leerstof, met dezelfde spelling en hetzelfde metrieke stelsel. Engels is in Nederland zelfs een vak op de basisschool.",
      },
      {
        kop: "Typisch Belgisch",
        tekst:
          "Frans is bij ons verplicht in het 5de en 6de leerjaar, in Nederland niet. Bij aardrijkskunde en geschiedenis gaat een deel over België; de algemene hoofdstukken, zoals kaartlezen, Europa en de tijdlijn, zijn wel bruikbaar.",
      },
      {
        kop: "In het middelbaar",
        tekst:
          "Spark sluit nog vrij goed aan bij de brugklas. Boost en Beyond volgen de Vlaamse studierichtingen en zijn niet gemaakt voor de Nederlandse eindexamens, al kunnen losse hoofdstukken wiskunde of wetenschappen wel helpen.",
      },
      {
        kop: "Twijfel je?",
        tekst:
          "Begin dan met Basis of met een paar oefeningen van Start. Na een handvol vragen zie je snel of het te makkelijk of te moeilijk is.",
      },
    ],
  } as {
    kop: string;
    intro: string;
    tabelKoppen: string[];
    tabel: string[][];
    vakken: { kop: string; tekst: string }[];
  } | null,
  /* De knop onderaan. Laat de link leeg om de knop te verbergen. */
  oproepTekst: "Naar de vakken",
  oproepLink: "/",
};
