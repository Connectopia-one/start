/*
  De pagina Boekentips: boeken die bij ons in de kast staan en echt gebruikt
  worden. Kim op 26 oktober 2026: "als ze zo leuk zijn, dan mogen ze bij ons
  toch zeker niet ontbreken."

  Bewust zonder leeftijd. Onze kinderen kiezen op interesse: een boek dat er
  kinderlijk uitziet, zit soms vol denkstof, en een boek "voor volwassenen"
  lezen ze vaak al volop.

  Een boek bijzetten:
    1. Zet de foto van de kaft in  public/boekentips/  (jpg, rechtop, ongeveer
       480 pixels breed). De bestandsnaam is de slug hieronder plus .jpg.
    2. Voeg onderaan in de lijst een blok toe. Kies de onderwerpen uit de lijst
       onderwerpen; een nieuw onderwerp zet je daar eerst bij.
  De filterknoppen en de volgorde volgen vanzelf.
*/

export const boekentipsTekst = {
  label: "Hulp, advies en tips",
  titel: "Boekentips",
  handgeschreven: "Boeken zijn goud waard.",
  tekst:
    "Elk boek op deze pagina staat bij ons in de kast en wordt echt gebruikt in de werking. Een leeftijd zetten we er bewust niet bij: onze kinderen kiezen op interesse, niet op het getal op de achterkant.",
};

export const onderwerpen = [
  "geschiedenis",
  "natuurkunde",
  "scheikunde",
  "biologie",
  "heelal",
  "naslagwerk",
  "strips",
] as const;

export type Onderwerp = (typeof onderwerpen)[number];

export type Boek = {
  slug: string;
  titel: string;
  makers: string;
  uitgeverij: string;
  tekst: string;
  onderwerpen: Onderwerp[];
};

export const boeken: Boek[] = [
  {
    slug: "wie-waren-de-romeinen-eigenlijk",
    titel: "Wie waren de Romeinen eigenlijk?",
    makers: "Laura Cowan, met prenten van Victoria Stebleva",
    uitgeverij: "Usborne",
    tekst:
      "Hadden de Romeinen al wc's? Hoe zag een schooldag eruit? Geschiedenis aan de hand van de vragen die kinderen zelf stellen.",
    onderwerpen: ["geschiedenis"],
  },
  {
    slug: "dwars-door-tijd-en-ruimte",
    titel: "Dwars door tijd & ruimte",
    makers: "Yannick Fritschy, met tekeningen van Tjarko van der Pol",
    uitgeverij: "Nieuwezijds",
    tekst:
      "Mee op het schip van Galilei en in de trein van Einstein. Kan je reizen in de tijd? Grote ideeën, uitgelegd zonder ze kleiner te maken.",
    onderwerpen: ["natuurkunde", "heelal"],
  },
  {
    slug: "waarom-geschiedenisencyclopedie",
    titel: "Waarom? De grote geschiedenisencyclopedie",
    makers: "",
    uitgeverij: "Lannoo",
    tekst:
      "Duidelijke antwoorden op echte vragen van kinderen over geschiedenis. Om samen in te bladeren of zelf op ontdekking te gaan.",
    onderwerpen: ["geschiedenis", "naslagwerk"],
  },
  {
    slug: "de-grootste-uitslovers-ooit",
    titel: "De grootste uitslovers ooit",
    makers: "Andy Seed, met tekeningen van Sam Caldwell",
    uitgeverij: "Van Holkema & Warendorf",
    tekst:
      "De brutaalste, bijzonderste en briljantste mensen uit de geschiedenis. Een mooie herinnering voor wie zelf soms anders is: opvallen mag.",
    onderwerpen: ["geschiedenis"],
  },
  {
    slug: "britannica-kinderencyclopedie",
    titel: "De Britannica Kinderencyclopedie",
    makers: "Christopher Lloyd",
    uitgeverij: "Lannoo",
    tekst:
      "Over alles wat we (nog niet) weten: de aarde, de ruimte, geschiedenis en wetenschap, met quizzen en echte onderzoekers aan het woord.",
    onderwerpen: ["naslagwerk", "heelal", "geschiedenis"],
  },
  {
    slug: "science-met-strips-natuurkunde",
    titel: "Science met strips: Natuurkunde",
    makers: "Paul Mason en Jess Bradley",
    uitgeverij: "",
    tekst:
      "Krachten, geluid en onzichtbaar licht, elke dubbele bladzijde uitgelegd met een korte strip vol humor.",
    onderwerpen: ["natuurkunde", "strips"],
  },
  {
    slug: "science-met-strips-biologie",
    titel: "Science met strips: Biologie",
    makers: "Paul Mason en Jess Bradley",
    uitgeverij: "",
    tekst:
      "Wie is hier de baas, je brein of je hand? Het lichaam, dieren en planten in grappige strips.",
    onderwerpen: ["biologie", "strips"],
  },
  {
    slug: "science-met-strips-aarde-en-heelal",
    titel: "Science met strips: Aarde en heelal",
    makers: "Paul Mason en Jess Bradley",
    uitgeverij: "",
    tekst:
      "Waarom was een dag bij de dinosaurussen korter, en waarom is Pluto geen planeet meer? Ruimte en aarde in strips die blijven hangen.",
    onderwerpen: ["heelal", "strips"],
  },
  {
    slug: "science-met-strips-scheikunde",
    titel: "Science met strips: Scheikunde",
    makers: "Paul Mason en Jess Bradley",
    uitgeverij: "",
    tekst:
      "Stoffen, materialen en gassen, en hoe scheikunde speurders helpt om criminelen te vinden.",
    onderwerpen: ["scheikunde", "strips"],
  },
  {
    slug: "het-dikke-boek-van-ons-bijzondere-heelal",
    titel: "Het dikke boek van ons bijzondere heelal",
    makers: "Will Gater",
    uitgeverij: "Lannoo",
    tekst:
      "Planeten en manen, zwarte gaten en kleurrijke nevels, met prachtige foto's. Een boek om lang in te bladeren en bij weg te dromen.",
    onderwerpen: ["heelal"],
  },
  {
    slug: "natuurkunde-eenvoudig-uitgelegd",
    titel: "Natuurkunde eenvoudig uitgelegd",
    makers: "",
    uitgeverij: "Deltas",
    tekst:
      "Waaruit bestaat een atoom? Kan je surfen op lichtgolven? Wat betekent E=mc²? Grote vragen, helder beantwoord.",
    onderwerpen: ["natuurkunde"],
  },
];
