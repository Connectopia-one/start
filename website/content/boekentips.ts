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
  handgeschreven: "Een kijkje in onze boekenkast.",
  tekst:
    "Dit is een kijkje in de boekenkast van Connectopia. Elk boek dat we hier tippen, hebben we zelf en wordt echt gebruikt in onze werking. Een leeftijd zetten we er bewust niet bij: onze kinderen kiezen op interesse, niet op het getal op de achterkant.",
};

export const onderwerpen = [
  "geschiedenis",
  "natuurkunde",
  "scheikunde",
  "biologie",
  "heelal",
  "naslagwerk",
  "strips",
  "wiskunde",
  "techniek",
  "puzzels",
  "weetjes",
  "voor ouders",
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
  {
    slug: "wiskunde-ann-dooms",
    titel: "Wiskunde",
    makers: "Ann Dooms",
    uitgeverij: "Nerdland, Borgerhoff & Lamberigts",
    tekst:
      "Ann Dooms neemt je mee op een wandeling door de wondere wereld van de wiskunde. Voor iedereen die wil zien dat wiskunde veel meer is dan rekenen.",
    onderwerpen: ["wiskunde"],
  },
  {
    slug: "chemie-hetty-helsmoortel",
    titel: "Chemie",
    makers: "Hetty Helsmoortel",
    uitgeverij: "Nerdland, Borgerhoff & Lamberigts",
    tekst:
      "Hetty Helsmoortel vertelt de meest verrassende verhalen uit de scheikunde. Van vuurwerk tot diamanten, en waarom stoffen doen wat ze doen.",
    onderwerpen: ["scheikunde"],
  },
  {
    slug: "blij-met-mij",
    titel: "Blij met mij!",
    makers: "Els Pronk en Elke Busschots",
    uitgeverij: "",
    tekst:
      "Hoe versterk je het talent én de veerkracht van je kind? Een warm boek voor ouders, met veel herkenning en concrete handvatten.",
    onderwerpen: ["voor ouders"],
  },
  {
    slug: "diep-gedacht-en-intens-gevoeld",
    titel: "Diep gedacht en intens gevoeld",
    makers: "",
    uitgeverij: "",
    tekst:
      "Verhalen van hoogbegaafde vrouwen, over diep denken en intens voelen. Veel ouders herkennen er niet alleen hun kind in, maar ook zichzelf.",
    onderwerpen: ["voor ouders"],
  },
  {
    slug: "hoogbegaafd-opgroeien",
    titel: "Hoogbegaafd opgroeien",
    makers: "Michelle Dewulf en Isabelle François",
    uitgeverij: "Borgerhoff & Lamberigts",
    tekst:
      "Over wat hoogbegaafd opgroeien echt betekent, voor het kind en voor wie errond staat. Een boek om met andere ogen naar je kind te kijken.",
    onderwerpen: ["voor ouders"],
  },
  {
    slug: "young-scientist-vakantieboek",
    titel: "Young Scientist vakantieboek",
    makers: "",
    uitgeverij: "New Scientist",
    tekst:
      "Van de makers van New Scientist: van het eerste wiel tot de vliegende auto, bomvol weetjes en puzzels.",
    onderwerpen: ["weetjes", "puzzels"],
  },
  {
    slug: "quizboek-voor-allesweters",
    titel: "Quizboek voor allesweters",
    makers: "",
    uitgeverij: "Naturalis",
    tekst:
      "Een quizboek vol vragen over de ruimte, de natuur, wetenschap en nog veel meer. Om alleen of samen je algemene kennis te testen.",
    onderwerpen: ["weetjes", "puzzels"],
  },
  {
    slug: "survivalgids-wat-als-je-hoogbegaafd-bent",
    titel: "Wat als je hoogbegaafd bent?",
    makers: "",
    uitgeverij: "Pelckmans",
    tekst:
      "Een survivalgids en doe-boek voor kinderen die zelf willen begrijpen wat hoogbegaafd zijn betekent. Met tips en tricks om mee aan de slag te gaan.",
    onderwerpen: ["voor ouders"],
  },
  {
    slug: "het-weer",
    titel: "Het weer",
    makers: "Bram Verbruggen, met illustraties van Isabelle Geeraerts",
    uitgeverij: "Pelckmans",
    tekst:
      "Weerman Bram Verbruggen legt alle weerelementen uit, en vooral hoe je ze zelf kunt waarnemen. Met heerlijke prenten van Isabelle Geeraerts.",
    onderwerpen: ["natuurkunde"],
  },
  {
    slug: "onbegrensd-universum",
    titel: "Onbegrensd universum",
    makers: "Govert Schilling",
    uitgeverij: "",
    tekst:
      "Govert Schilling reist met de James Webb-ruimtetelescoop door het heelal. Een groot boek vol adembenemende beelden, om lang in te verdwijnen.",
    onderwerpen: ["heelal"],
  },
  {
    slug: "zo-werkt-je-lichaam",
    titel: "Zo werkt je lichaam",
    makers: "",
    uitgeverij: "",
    tekst:
      "Een hele reeks boekjes over je lichaam, van de huid en de spieren tot het hart, de hersenen en het immuunsysteem. Elk deel over één onderwerp.",
    onderwerpen: ["biologie", "naslagwerk"],
  },
  {
    slug: "build-your-own-chain-reaction-machines",
    titel: "Build your own chain reaction machines",
    makers: "Paul Long",
    uitgeverij: "",
    tekst:
      "Kettingreactiemachines bouwen met karton, tape en alledaagse spullen. In het Engels, maar de foto's en tekeningen spreken voor zich.",
    onderwerpen: ["techniek"],
  },
  {
    slug: "een-dag-in-het-leven-van-de-ruimte",
    titel: "Een dag in het leven van...",
    makers: "",
    uitgeverij: "Deltas",
    tekst:
      "Een dag in het leven van een astronaut, de maan, Mars of zelfs een ruimtedrol. Een knotsgekke reis door de ruimte.",
    onderwerpen: ["heelal", "weetjes"],
  },
  {
    slug: "een-dag-in-het-leven-van-het-leven-op-aarde",
    titel: "Een dag in het leven van...",
    makers: "",
    uitgeverij: "Deltas",
    tekst:
      "Een dag in het leven van een mestkever, een bacterie, een vulkaan of je eigen hersenen. Knotsgekke weetjes over het leven op aarde.",
    onderwerpen: ["biologie", "weetjes"],
  },
  {
    slug: "wat-een-hond-ons-over-wiskunde-kan-leren",
    titel: "Wat een hond ons over wiskunde kan leren",
    makers: "Ben Orlin",
    uitgeverij: "Lannoo",
    tekst:
      "Ben Orlin legt limieten, differentialen en integralen uit met verhalen en grappige tekeningetjes. Voor doordenkers die verder willen kijken dan de leerstof.",
    onderwerpen: ["wiskunde"],
  },
  {
    slug: "natuurkunde-visuele-gids",
    titel: "Natuurkunde: visuele gids",
    makers: "Kurt Baker",
    uitgeverij: "Librero",
    tekst:
      "Een visuele gids met de belangrijkste basisprincipes van de natuurkunde, van veren en licht tot atomen en zwaartekracht.",
    onderwerpen: ["natuurkunde", "naslagwerk"],
  },
  {
    slug: "hoe",
    titel: "Hoe?",
    makers: "Hartog & Hartog",
    uitgeverij: "Pelckmans",
    tekst:
      "Hoe word je onzichtbaar? Hoe maak je een olifant? Antwoorden op vragen waarvan je niet wist dat je ze had.",
    onderwerpen: ["weetjes"],
  },
  {
    slug: "de-breinbrekers-van-mensa",
    titel: "De breinbrekers van Mensa",
    makers: "Gareth Moore",
    uitgeverij: "Lannoo",
    tekst:
      "Vierhonderd cijferpuzzels, logische raadsels en denkpuzzels. Voor wie nooit genoeg kan krijgen van een goede breinbreker.",
    onderwerpen: ["puzzels"],
  },
  {
    slug: "100-weetjes-over-de-ruimte",
    titel: "100 waanzinnige weetjes over de ruimte",
    makers: "",
    uitgeverij: "Deltas",
    tekst:
      "Honderd korte weetjes over planeten, raketten, sterren en de maanlanding. Ideaal om even in te duiken en telkens iets nieuws te ontdekken.",
    onderwerpen: ["heelal", "weetjes"],
  },
  {
    slug: "100-weetjes-over-wetenschap",
    titel: "100 waanzinnige weetjes over wetenschap",
    makers: "",
    uitgeverij: "Deltas",
    tekst:
      "Honderd korte weetjes over wetenschap, van vleermuizen tot Einstein. Een boeiende kijk op de wondere wereld van de wetenschap.",
    onderwerpen: ["weetjes", "natuurkunde", "biologie"],
  },
  {
    slug: "einstein-puzzelboek",
    titel: "Mr. Brein: Einstein puzzelboek",
    makers: "Gareth Moore",
    uitgeverij: "",
    tekst:
      "Breinbrekende puzzels en raadsels in de geest van Einstein. Voor wie graag lang op één probleem blijft broeden.",
    onderwerpen: ["puzzels"],
  },
  {
    slug: "321-superslimme-dingen-geschiedenis",
    titel: "321 superslimme dingen die je moet weten over geschiedenis",
    makers: "Mathilda Masters, met illustraties van Louize Perdieus",
    uitgeverij: "Lannoo",
    tekst:
      "Driehonderdeenentwintig verrassende weetjes over geschiedenis, in korte stukjes. Met prachtige prenten van Louize Perdieus.",
    onderwerpen: ["geschiedenis", "weetjes"],
  },
  {
    slug: "mijlpalen-van-de-wetenschap",
    titel: "Mijlpalen van de wetenschap",
    makers: "",
    uitgeverij: "",
    tekst:
      "Een reeks waarin elk deel één periode uit de geschiedenis van de wetenschap volgt, van Galilei en Newton tot Darwin, Marie Curie en Einstein. Wetenschap en geschiedenis in één.",
    onderwerpen: ["geschiedenis", "natuurkunde"],
  },
];
