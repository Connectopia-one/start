/*
  De wegwijzer voor ouders: de roadmap bij een vermoeden of een diagnose.

  Elke stap is één blok hieronder.
    punten   de lijst met concrete tips
    nadruk   de zin of alinea die je wil laten opvallen, in een gekleurd kader
    tip      een kadertje met een knop, bijvoorbeeld om contact op te nemen
  Laat nadruk of tip gerust weg als een stap ze niet nodig heeft.
*/

export type Stap = {
  nummer: string;
  titel: string;
  kleur: "green" | "orange" | "purple" | "blue";
  icoon: string;
  samenvatting: string;
  punten: string[];
  nadruk?: string;
  tip?: { tekst: string; knopTekst: string; knopLink: string };
};

export const wegwijzerTekst = {
  label: "Wegwijzer voor ouders",
  titel: "Vermoeden of diagnose? Dit is je route.",
  handgeschreven: "Jouw zoektocht mag wat korter en minder eenzaam zijn.",
  tekst:
    "Een echte roadmap bij ASS, ADHD, hoogbegaafdheid en uitzonderlijke hoogbegaafdheid. Van het eerste vermoeden tot ver na de diagnose: bij wie begin je, wie doet wat, wat verandert er op school, en wat bestaat er aan ondersteuning.",
  nota:
    "Wij zijn geen diagnostici of klinisch psychologen. We zijn ervaringsdeskundigen met een zorgvuldig opgebouwd netwerk van wél-specialisten, en we delen hier wat we zelf geleerd hebben.",
  /*
    Het blok onder het stappenplan dat naar de observatielijst verwijst.
    Wil je het weg? Zet observatieblok op null.
  */
  observatieblok: {
    label: "Gratis en zonder inschrijven",
    titel: "Neem een ingevuld blad mee naar je gesprek",
    tekst:
      "We maakten een uitgebreide observatielijst met kenmerken van hoogbegaafdheid, uitzonderlijke hoogbegaafdheid, autisme en ADHD. Je vult aan wat je herkent, schrijft je eigen voorbeelden erbij en drukt het af. Zo start je gesprek met de leerkracht, het CLB of de specialist niet bij nul. Het is geen test en geen diagnose, gewoon een blad dat je gedachten ordent.",
    knopTekst: "Naar de observatielijst",
    knopLink: "/observatielijst",
  },

  slot: {
    titel: "Kom je er niet uit?",
    tekst:
      "Stel je vraag gerust. We denken met je mee en verwijzen je door naar wie je verder kan helpen.",
    knopTekst: "Neem contact op",
    knopLink: "/contact",
  },
};

export const stappen: Stap[] = [
  {
    nummer: "1",
    titel: "Ik twijfel",
    kleur: "green",
    icoon: "🔍",
    samenvatting: "Jij kent je kind het best. Begin bij de leerkracht.",
    punten: [
      "Een gesprek op school met de leerkracht komt op de eerste plaats.",
      "Je kan je bezorgdheden ook altijd delen met het CLB.",
      "Hou er rekening mee dat veel kinderen op school veel kunnen maskeren. Vaak komen de problemen pas thuis tot uiting, en herkent de school je verhaal niet meteen.",
      "Noteer wat je thuis opvalt en over welke periode. Dat maakt het gesprek concreter.",
    ],
    nadruk: "Onthoud altijd dat jij zelf de grootste expert bent van je kind.",
    tip: {
      tekst: "Zit je met vragen? Neem gerust contact op voor een gratis telefonisch gesprek.",
      knopTekst: "Plan een gesprek",
      knopLink: "/contact",
    },
  },
  {
    nummer: "2",
    titel: "Het traject",
    kleur: "purple",
    icoon: "🗺️",
    samenvatting: "Wie doet wat, en hoeveel weten ze van hoogbegaafdheid?",
    punten: [
      "Het CLB kan een eerste screening doen of een doorverwijzing vragen.",
      "Hou er wel rekening mee dat niet iedereen bij het CLB kennis heeft van hoogbegaafdheid. Dat kan soms een verkeerd beeld geven.",
      "Ga je naar een zelfstandige psycholoog of psychiater, of naar een diagnostisch centrum? Ga dan eerst na hoe ver hun kennis van hoogbegaafdheid reikt.",
      "Durf doorvragen naar hun ervaring en hun opleiding.",
      "Of kijk bij onze tips voor mogelijke gespecialiseerde diensten.",
    ],
    nadruk:
      "Zelf doen wij geen diagnostische testingen, omdat we dat liever aan echte professionals overlaten. Zo'n testing heeft het oog nodig van een deskundige die de maskering en de overlap van diagnoses kan doorprikken, en die breder kijkt dan enkel het IQ-nummer of het “foutieve” gedrag.",
    tip: {
      tekst: "In onze gids staan diensten en organisaties waar we zelf vertrouwen in hebben.",
      knopTekst: "Naar de gids",
      knopLink: "/waar-kan-je-terecht",
    },
  },
  {
    nummer: "3",
    titel: "En nu?",
    kleur: "orange",
    icoon: "💡",
    samenvatting: "Wat verandert er thuis, op school en in de begeleiding.",
    punten: [
      "Een verslag is een startpunt, geen eindpunt.",
      "Maak samen met de school afspraken over wat je kind nodig heeft.",
      "Je kan altijd aan de ondersteuningsdienst of aan ons vragen om mee op gesprek te gaan. Zo voel je dat je er niet alleen voor staat.",
      "Zoek uit wat je kind zélf van de uitslag begrijpt en wil.",
      "Zoek peers: kinderen die hetzelfde meemaken, schelen enorm veel.",
    ],
    tip: {
      tekst: "Wil je dat iemand van ons meegaat naar een gesprek op school? Vraag het gerust.",
      knopTekst: "Vraag ondersteuning",
      knopLink: "/contact",
    },
  },
  {
    nummer: "4",
    titel: "Wat bestaat er",
    kleur: "blue",
    icoon: "📚",
    samenvatting: "Een moeilijke stap, want er is minder dan je zou hopen.",
    punten: [
      "Bij een dubbele diagnose kom je soms in aanmerking voor verhoogde kinderbijslag.",
      "Via je mutualiteit is er soms een kleine terugbetaling voor ADHD of autisme. Dat hangt sterk af van waar je aangesloten bent.",
      "Ondersteuning op school kan via het ondersteuningsnetwerk of een individueel traject.",
      "Begeleiding buiten school: therapie, bijles, coaching of een plustraject.",
      "Onze gids met diensten en organisaties zet de mogelijkheden op een rij.",
    ],
    nadruk:
      "Heb je enkel een diagnose HB of UHB, dan heb je in België jammer genoeg geen recht op terugbetalingen. Vind je ergens toch iets, laat het ons dan zeker weten, dan delen we het verder.",
  },
  {
    nummer: "5",
    titel: "Jij en je gezin",
    kleur: "green",
    icoon: "💚",
    samenvatting: "Het mooiste traject, en het traject dat het vaakst vergeten wordt.",
    punten: [
      "Een kind met extra noden, of dat nu HB, autisme, ADHD of iets anders is, geeft je gezin een ander parcours dan je je had voorgesteld.",
      "Maak ruimte om een beetje te rouwen om het beeld dat je had van hoe je gezin en je leven eruit zouden zien. Dat mag.",
      "En dan begint er een traject dat je samen met je kind beleeft. Zo'n leven kan heel mooi zijn.",
      "Leer bij door je kind en voor je kind, en geniet. Want dat wordt nogal eens vergeten.",
      "Je bent al zover geraakt om te zoeken waar je je kind mee verder kan helpen. Dat zegt toch al heel veel.",
      "Neem nu eens de tijd om alle positieve dingen op te schrijven. Vraag je kind om dat ook over jou te doen.",
      "Doe wat jij voelt dat goed zit.",
    ],
    nadruk: "Jouw gezin en jouw kind zijn uniek.",
    tip: {
      tekst: "Andere ouders schrijven op onze blog over precies dit stuk van de weg.",
      knopTekst: "Lees mee",
      knopLink: "/blog",
    },
  },
];
