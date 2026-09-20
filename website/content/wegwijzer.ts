/*
  De wegwijzer voor ouders: de roadmap bij een vermoeden of een diagnose.
  Elke stap is één blok. Vul de tekst aan zoals jij het aan ouders vertelt.
*/

export type Stap = {
  nummer: string;
  titel: string;
  kleur: "green" | "orange" | "purple" | "blue";
  icoon: string;
  samenvatting: string;
  punten: string[];
};

export const wegwijzerTekst = {
  label: "Wegwijzer voor ouders",
  titel: "Vermoeden of diagnose? Dit is je route.",
  handgeschreven: "Jouw zoektocht mag wat korter en minder eenzaam zijn.",
  tekst:
    "Een echte roadmap bij ASS, ADHD, hoogbegaafdheid en uitzonderlijke hoogbegaafdheid. Van het eerste vermoeden tot ver na de diagnose: bij wie begin je, wie doet wat, wat verandert er op school, en wat bestaat er aan ondersteuning en rechten.",
  nota:
    "Wij zijn geen diagnostici of klinisch psychologen. We zijn ervaringsdeskundigen met een zorgvuldig opgebouwd netwerk van wél-specialisten, en we delen hier wat we zelf geleerd hebben.",
  slot: {
    titel: "Kom je er niet uit?",
    tekst:
      "Stel je vraag gerust. We denken met je mee en verwijzen je door naar wie je verder kan helpen.",
    knopTekst: "Neem contact op",
    knopLink: "/over-ons#contact",
  },
};

export const stappen: Stap[] = [
  {
    nummer: "1",
    titel: "Ik twijfel",
    kleur: "green",
    icoon: "🔍",
    samenvatting: "Waar let je op, en bij wie begin je?",
    punten: [
      "Noteer wat je opvalt, thuis én op school, en over welke periode.",
      "Vraag de leerkracht wat zij zien in de klas.",
      "Het CLB van de school is een eerste, gratis aanspreekpunt.",
      "Twijfel is genoeg reden om te vragen. Je hoeft niet zeker te zijn.",
    ],
  },
  {
    nummer: "2",
    titel: "Het traject",
    kleur: "purple",
    icoon: "🗺️",
    samenvatting: "CLB, psycholoog of centrum: wie doet wat.",
    punten: [
      "Het CLB kan een eerste screening doen en doorverwijzen.",
      "Een zelfstandige psycholoog of een centrum doet het uitgebreide onderzoek.",
      "Vraag vooraf naar de wachttijd, de prijs en wat er precies onderzocht wordt.",
      "Bij een vermoeden van meerdere dingen tegelijk: zoek iemand met kennis van dubbele diagnoses.",
    ],
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
      "Zoek uit wat je kind zélf van de uitslag begrijpt en wil.",
      "Zoek peers: kinderen die hetzelfde meemaken, schelen enorm veel.",
    ],
  },
  {
    nummer: "4",
    titel: "Wat bestaat er",
    kleur: "blue",
    icoon: "📚",
    samenvatting: "Rechten, ondersteuning en waar je verder terecht kan.",
    punten: [
      "Ondersteuning op school via het ondersteuningsnetwerk of een individueel traject.",
      "Terugbetalingen en tegemoetkomingen via je ziekenfonds.",
      "Begeleiding buiten school: therapie, bijles, coaching of een plustraject.",
      "Onze gids met diensten en organisaties zet de mogelijkheden op een rij.",
    ],
  },
];
