/*
  De pagina "Wat is er nieuw?" — /nieuw

  Kim, 8 november 2026: "een ronde knop op de beginpagina die leidt naar een
  pagina waar alle updates die we deden opkomen in aparte vakjes, zo kunnen
  mensen ook echt zien wat er nu weer aangepast is."

  Elke update is een vakje. Het nieuwste staat bovenaan: zet een nieuwe update
  dus altijd vooraan in de lijst `updates`. Per vakje:
    datum      zoals hij op de pagina moet staan, bv. "8 november 2026"
    titel      kort, in gewone woorden
    tekst      wat er veranderd is, voor ouders en kinderen
    opVraag    true als het er kwam door een melding, de enquête of een review
               (dan staat er een klein labeltje "Op jullie vraag" bij)
    link       mag weg; een knopje naar de plek waar je het ziet

  Geen namen van ouders of kinderen in deze teksten: de pagina is voor
  iedereen zichtbaar, ook zonder account.
*/

export type Update = {
  datum: string;
  titel: string;
  tekst: string;
  opVraag?: boolean;
  link?: { tekst: string; href: string };
};

export const nieuwTekst = {
  /* Het ronde knopje op de startpagina. Zet op null om het even te verbergen:
     knop: null, */
  knop: { tekst: "Wat is er nieuw?", link: "/nieuw" } as { tekst: string; link: string } | null,

  label: "Wat is er nieuw?",
  titel: "Alles wat we aanpasten",
  intro:
    "Het oefenplatform groeit elke week. Veel van wat hieronder staat, kwam er omdat jullie iets meldden, de enquête invulden of een review schreven. Dank je wel daarvoor! Het nieuwste staat bovenaan.",
  labelOpVraag: "Op jullie vraag",
};

export const updates: Update[] = [
  {
    datum: "9 november 2026",
    titel: "Wiskunde basis voor Beyond doorstroom",
    tekst:
      "Beyond doorstroom heeft nu ook wiskunde basis, voor humane wetenschappen, moderne talen, Latijn-moderne talen, welzijnswetenschappen en bedrijfswetenschappen. Kies bovenaan het vak voor welke richting je leert. Kies je welzijnswetenschappen, dan laten we tweedegraadsfuncties en tweedegraadsvergelijkingen weg, want jouw examen vraagt ze niet. Kies je bedrijfswetenschappen, dan krijg je er 14 hoofdstukken bij, onder andere integralen, matrices en hypothesetoetsen. De uitleg over welke vakken bij welke richting horen, staat nu dichtgeklapt bovenaan Beyond doorstroom.",
    link: { tekst: "Naar wiskunde basis", href: "/niveaus/beyond-doorstroom/wiskunde-basis" },
  },
  {
    datum: "9 november 2026",
    titel: "Geschiedenis Beyond: kies je richting, wij laten weg wat je niet nodig hebt",
    tekst:
      "Volg je bedrijfswetenschappen of welzijnswetenschappen? Dan is je examen geschiedenis wat lichter. Kies bovenaan het vak geschiedenis in Beyond voor welke richting je leert: dan krijg je enkel de vragen die je nodig hebt, ook in het examen. Hoofdstukken waar een stuk wegvalt, krijgen een oranje bolletje.",
  },
  {
    datum: "9 november 2026",
    titel: "Vier rustige spellen voor de lagere school",
    tekst:
      "Bij de educatieve spellen staan vier nieuwe spellen voor de lagere school: Breukenpizza, Foutenspeurder, Tijdlijn leggen en Kaartpuzzel. Ze zijn bewust rustig gemaakt: geen klok, geen geluid, geen punten en geen ranglijst. Wie een fout maakt, krijgt een korte tip en gaat zelf verder als hij of zij er klaar voor is.",
    link: { tekst: "Naar de educatieve spellen", href: "/extras/spellen" },
  },
  {
    datum: "9 november 2026",
    titel: "Geschiedenis Beyond: pittige hoofdstukken en nieuwe onderwerpen",
    tekst:
      "Geschiedenis in Beyond heeft nu pittige hoofdstukken in de vorm van het examen. Er zijn ook nieuwe hoofdstukken over China, Israël-Palestina, de kunststromingen en kunst analyseren. De begrippenarena geschiedenis heeft nu ook een niveau Beyond.",
  },
  {
    datum: "9 november 2026",
    titel: "Leuke extra's netjes geordend",
    tekst:
      "De pagina Leuke extra's begint nu met vier grote knoppen: educatieve spellen, leuke links, afdrukbare documenten en leuke filmpjes. Achter elke knop staat alles per schoolniveau, eerst de lagere school en dan de middelbare school. Bij elke begrippenarena zie je meteen voor welk niveau ze is, en het spel opent ook meteen op dat niveau. In de begrippenarena's kan je nu ook kiezen om alleen te spelen, handig om thuis te oefenen.",
    link: { tekst: "Naar de leuke extra's", href: "/extras" },
  },
  {
    datum: "8 november 2026",
    titel: "Welzijnswetenschappen nu bij natuurwetenschappen",
    tekst:
      "De hoofdstukken voor welzijnswetenschappen staan nu gewoon in het vak natuurwetenschappen van Beyond, onderaan in het blauw met het label \"Enkel welzijnswetenschappen\". Bovenaan het vak staat duidelijk uitgelegd wie ze moet maken, en er is een apart examen voor welzijnswetenschappen. Volg je een andere richting, dan sla je de blauwe hoofdstukken over.",
  },
  {
    datum: "8 november 2026",
    titel: "Sterretjes verdienen en figuurtjes kiezen",
    tekst:
      "Voor elk hoofdstuk dat je kind helemaal afwerkt, krijgt het een sterretje. Juist of fout maakt niet uit: het gaat om het doorzetten. Met die sterretjes kiest het een figuurtje, van een vos tot een draak. Er is geen ranglijst. Je zet het per kind aan bij je account.",
    link: { tekst: "Naar je account", href: "/account" },
  },
  {
    datum: "8 november 2026",
    titel: "Makkelijker registreren met een code",
    tekst:
      "Bij registreren, inloggen en op je account zie je nu duidelijk waar je een testcode of plusklascode invult, in een lichtgroen kader. Er staat ook bij dat het oefenplatform een eigen login heeft, los van het ouderportaal.",
    opVraag: true,
  },
  {
    datum: "8 november 2026",
    titel: "Het vakkenoverzicht telt alles mee",
    tekst:
      "Bij vakken met veel hoofdstukken telde het overzicht er niet allemaal mee. Dat is rechtgezet. Er staat nu ook \"geoefend\" in plaats van \"gemaakt\", want ook een hoofdstuk met fouten is geoefend.",
    opVraag: true,
  },
  {
    datum: "8 november 2026",
    titel: "Frans in Start rechtgezet",
    tekst:
      "In de leerbundel \"Woorden voor elke dag\" stond dat Frans niet bij de minimumdoelen hoort. Dat klopte niet: Frans is verplicht in het vijfde en zesde leerjaar. Ook de datum van de nieuwe minimumdoelen staat nu juist: ze komen stap voor stap, vanaf schooljaar 2026-2027.",
    opVraag: true,
  },
  {
    datum: "8 november 2026",
    titel: "Enquête: meer dan één kind aanduiden",
    tekst:
      "Bij de vraag \"Wie oefende er?\" kan je nu meerdere antwoorden aanvinken, handig als er meer kinderen in het gezin oefenen.",
    opVraag: true,
  },
  {
    datum: "7 november 2026",
    titel: "Een rustigere startpagina en een korter menu",
    tekst:
      "Bovenaan de startpagina staan de enquête en de review nu als twee duidelijke knoppen. De uitleg over het platform is vier kleine blokjes geworden. Leuke extra's en Materiaal staan samen onder \"Extra's\", en het huisje om terug naar de start te gaan is groter.",
  },
  {
    datum: "7 november 2026",
    titel: "Meer tips om met het platform te werken",
    tekst:
      "Op de tipspagina staat een nieuwe stap: tot slot een examen over het hele vak, met vragen uit alle hoofdstukken en telkens een andere versie. Er zijn ook briefjes bij gekomen over deel 1 en deel 2 van een hoofdstuk, en over voorlezen als hulp bij dyslexie.",
    link: { tekst: "Naar de tips", href: "/tips" },
  },
  {
    datum: "6 november 2026",
    titel: "Verder waar je was",
    tekst:
      "Op de startpagina staat nu een knop die je meteen terugbrengt naar het hoofdstuk waar je kind gebleven was. Met het huisje bovenaan ga je altijd terug naar de start. En onder elk hoofdstuk staat een korte uitleg over waar het over gaat.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "Zachtere kleuren en een vriendelijker woordje bij een fout",
    tekst:
      "Wie felle kleuren te veel vindt, kiest per kind voor zachte kleuren bij juist en fout. Bij een fout antwoord verschijnt nu ook een zacht oranje zinnetje in plaats van een harde melding, ook bij de vraag van de dag.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "Voorleesknop",
    tekst:
      "Per kind kan je een voorleesknop aanzetten. Dan wordt de vraag en de uitleg voorgelezen. Handig voor wie nog niet vlot leest of dyslexie heeft. Standaard staat hij uit; je zet hem aan bij je account.",
    opVraag: true,
    link: { tekst: "Naar je account", href: "/account" },
  },
  {
    datum: "6 november 2026",
    titel: "Nog te oefenen, per kind en per vak",
    tekst:
      "Bij \"Nog te oefenen\" zie je per kind welke vragen nog eens geoefend mogen worden. Je kiest eerst het vak, met dezelfde knoppen als op de rest van het platform. Hoofdstukken waar je kind al aan werkte, krijgen een lichtgroene achtergrond.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "Pincode voor ouders",
    tekst:
      "Oefent je kind zelfstandig op jouw account? Dan kan je bij Mijn account een pincode instellen, zodat de voortgang en de lijst met foute vragen voor jou blijven. Je kan nu ook de naam van een kind aanpassen.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "Badges voor doorzetten",
    tekst:
      "Na 3, 10, 15, 25 en 50 geoefende hoofdstukken krijgt je kind een badge. Ook hier telt het oefenen, niet of alles juist was.",
  },
  {
    datum: "6 november 2026",
    titel: "Soepeler nakijken",
    tekst:
      "Een vollediger antwoord dan nodig, zoals \"Christoffel Colombus\" in plaats van \"Colombus\", telt nu als juist (behalve bij de taalvakken, waar de spelling telt). Meldt een ouder dat een antwoord toch juist was, dan kunnen wij dat nakijken en krijgt je kind alsnog zijn ster.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "Geen vastlopen meer bij snel klikken",
    tekst:
      "Wie snel na elkaar antwoordde, zag het platform soms blijven hangen. Dat is opgelost: antwoorden worden nu sneller en apart bewaard, dichter bij onze databank.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "De hele cursus van een vak in één pdf",
    tekst:
      "Bovenaan elke vakpagina staat nu een knop om de hele cursus van dat vak in één keer te downloaden, en een knop naar het examen over het hele vak.",
    opVraag: true,
  },
  {
    datum: "6 november 2026",
    titel: "Hoofdstukken voor welzijnswetenschappen",
    tekst:
      "In Beyond doorstroom kwamen er 14 hoofdstukken over het menselijk lichaam bij, voor wie de richting welzijnswetenschappen kiest. Met leerbundels, oefenbundels en ook vragen in de vorm van het examen, waaronder klikvragen op prenten.",
  },
  {
    datum: "6 november 2026",
    titel: "Begrippenarena Wiskunde",
    tekst:
      "Bij de Extra's staat een nieuwe Begrippenarena voor wiskunde, met vier niveaus (lager onderwijs, Spark, Boost en Beyond) en zes spelletjes. De Begrippenarena Natuurwetenschappen kreeg er ook een niveau bij voor welzijnswetenschappen.",
    link: { tekst: "Naar de Extra's", href: "/extras" },
  },
  {
    datum: "6 november 2026",
    titel: "Inloggen vanop de website en het ouderportaal",
    tekst:
      "Op de website van Connectopia en in het ouderportaal staat nu een knop die je rechtstreeks naar het oefenplatform brengt.",
    opVraag: true,
  },
  {
    datum: "5 november 2026",
    titel: "Enquête en reviews",
    tekst:
      "Je kan nu een korte enquête invullen en een review schrijven. Positieve en kritische reviews komen allebei op het reviewbord, zodat andere ouders een eerlijk beeld krijgen. Zo weten wij ook wat er beter kan, en veel van wat op deze pagina staat, komt daar vandaan.",
    link: { tekst: "Naar de reviews", href: "/reviews" },
  },
  {
    datum: "28 en 29 oktober 2026",
    titel: "Hoofdstukken per thema en vragen nagekeken",
    tekst:
      "Hoofdstukken die bij hetzelfde thema horen, staan nu samen onder één kopje. In Spark, Boost en Beyond hebben we de vragen nog eens nagekeken, zodat elke vraag op zichzelf te begrijpen is.",
  },
  {
    datum: "27 oktober 2026",
    titel: "Geschiedenis Spark bijgewerkt",
    tekst:
      "Geschiedenis Spark is helemaal nagekeken tegen de leerstof voor 2027, met 36 nieuwe vragen. In Start is geschiedenis nu opgebouwd rond de zeven periodes.",
  },
  {
    datum: "26 oktober 2026",
    titel: "Oefenen zoals op het echte examen",
    tekst:
      "Het platform kent nu alle vraagvormen van het examen van de Examencommissie: tabellen met juist of fout per rij, keuzelijsten in een zin, klikvragen op prenten en kaarten, en dezelfde vaste instructiezinnen. Het examen per vak bestaat voor de helft uit zulke vragen.",
  },
  {
    datum: "26 oktober 2026",
    titel: "Leuke extra's",
    tekst:
      "Een nieuwe pagina met spelletjes om te leren: de Begrippenarena Geschiedenis, de Begrippenarena Natuurwetenschappen, de Woordenarena Engels en De Wiskunde-dimensie, de game van Mats. De Uitdagingshoek kreeg ook een vijfde hoofdstuk per vak.",
    link: { tekst: "Naar de Extra's", href: "/extras" },
  },
  {
    datum: "20 en 21 oktober 2026",
    titel: "Zoeken, en mooiere formules",
    tekst:
      "Je kan nu zoeken in het hele oefenplatform. Formules in de verbetering staan er netjes getekend, in plaats van met schuine strepen. En het platform bleef soms hangen door de vraag van de dag: ook dat is opgelost.",
    opVraag: true,
  },
  {
    datum: "15 en 16 oktober 2026",
    titel: "Pittige hoofdstukken in Spark",
    tekst:
      "Alle vakken van Spark kregen pittige hoofdstukken erbij: 86 thema's en meer dan 1700 vragen. Bij invulvragen tellen woorden die in de uitleg als synoniem staan nu ook als juist.",
    opVraag: true,
  },
];
