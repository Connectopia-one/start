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
    datum: "12 november 2026",
    titel: "Foutenspeurder duidelijker",
    tekst:
      "Bij de foutenspeurder staan nu bij elke opgave twee uitwerkingen: één juiste en één foute. Je tikt de juiste aan en leest waarom de andere fout is. Vroeger stonden de stappen onder elkaar, en na een foute stap was de volgende ook fout. Dat was verwarrend. Er kwam ook een nieuwe opgave bij.",
    opVraag: true,
    link: { tekst: "Naar de foutenspeurder", href: "/extras/foutenspeurder" },
  },
  {
    datum: "11 november 2026",
    titel: "Begrippenarena wiskunde ook voor statistiek",
    tekst:
      "In de begrippenarena wiskunde kies je nu ook statistiek van Beyond: ruim zeventig begrippen, van telregels en de normale verdeling tot hypothesen toetsen en correlatie.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Begrippenarena geschiedenis ook voor Boost",
    tekst:
      "In de begrippenarena geschiedenis kies je nu ook Boost, met ruim honderdveertig begrippen van de Franken tot de industriële revolutie, ook voor de dubbele finaliteit. Beyond geldt voortaan ook voor Beyond dubbele finaliteit.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Begrippenarena economie ook voor toegepaste economie",
    tekst:
      "In de begrippenarena economie kies je nu ook toegepaste economie van Boost dubbele finaliteit: bijna honderdveertig begrippen, van de balans, het MAR en de btw tot het rekenblad, printen en databanken.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Begrippenarena natuurwetenschappen ook voor Boost en Beyond",
    tekst:
      "In de begrippenarena natuurwetenschappen kies je nu ook Boost of Beyond, met de begrippen uit biologie, chemie, fysica en natuurwetenschappen van dat niveau, ook voor de dubbele finaliteit. Spark en welzijnswetenschappen blijven zoals ze waren.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Woordenarena Engels voor alle niveaus",
    tekst:
      "De woordenarena Engels was er alleen voor Spark. Nu kies je bovenaan ook Start, Boost of Beyond, telkens met de woorden uit de leerbundels van dat niveau. Boost en Beyond gelden ook voor de dubbele finaliteit.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Nieuwe begrippenarena: uitdagingshoek",
    tekst:
      "Bij de educatieve spellen staat nu ook een begrippenarena voor de uitdagingshoek, met vier thema's: de ruimte, coderen en computers, de geschiedenis van België, en paradoxen en weetjes. Je oefent de begrippen in met een quiz, memory, raketgalgje, flitskaarten of bingo. In het sorteerspel kies je bijvoorbeeld tussen planeet en maan, of tussen feit en fabel.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Nieuwe begrippenarena: mens en samenleving",
    tekst:
      "Bij de educatieve spellen staat nu een begrippenarena voor de vakken over mens en samenleving: samenleving en economie, sociale en gedragswetenschappen, kunstbeschouwing en filosofie, gezondheid, zorg en welzijn, ontwikkeling en pedagogisch handelen, en filosofie en recht. Nieuw is het sorteerspel: je legt een uitspraak of voorbeeld in de juiste bak, zoals het juiste stadium van Piaget of de juiste macht.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Nieuwe begrippenarena: techniek",
    tekst:
      "Bij de educatieve spellen staat nu ook een begrippenarena techniek, voor wetenschap en techniek in Start en voor techniek in Spark. Je oefent de begrippen uit de leerbundels in met een quiz, memory, galgje, flitskaarten of bingo. Nieuw is de sorteerband: er komt een voorwerp voorbij en jij kiest de juiste bak, zoals geleider of isolator, sensor of actuator.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Nieuwe woordenarena: Frans",
    tekst:
      "Bij de educatieve spellen staat nu ook een woordenarena Frans, voor Basis, Start, Spark, Boost en Beyond. Je oefent de Franse woorden uit de leerbundels in met een quiz, memory, galgje, flitskaarten of bingo. Nieuw is le of la?: je ziet een Frans woord en kiest of het mannelijk of vrouwelijk is.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Nieuwe begrippenarena: Nederlands",
    tekst:
      "Bij de educatieve spellen staat nu ook een begrippenarena Nederlands, voor Basis, Start, Spark, Boost en Beyond. Je oefent de taalwoorden uit de leerbundels in met een quiz, memory, galgje, flitskaarten of bingo. Nieuw is de zinsdelenjager: je krijgt een zin en tikt zelf de persoonsvorm, het onderwerp of een ander zinsdeel aan.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Nieuwe begrippenarena: aardrijkskunde",
    tekst:
      "Bij de educatieve spellen staat nu ook een begrippenarena aardrijkskunde, voor Start, Spark, Boost en Beyond. Je oefent de begrippen uit de leerbundels in met een quiz, memory, galgje, flitskaarten of bingo, alleen of met de hele klas. Nieuw is fotoraden: je ziet een echte foto van bijvoorbeeld de toendra, de polders of een vulkaan en kiest het juiste begrip.",
    link: { tekst: "Naar de spellen", href: "/extras/spellen" },
  },
  {
    datum: "11 november 2026",
    titel: "Vier nieuwe uitdagingen in Spark, zoals op het examen",
    tekst:
      "Aardrijkskunde, Engels, samenleving en economie en techniek in Spark hebben nu ook een uitdagingshoofdstuk: telkens 30 vragen over alle hoofdstukken door elkaar, in de vormen van het examen van de Examencommissie. Je vult een tabel in, kiest uit keuzelijsten, sleept woorden, koppelt, sorteert, leest een casus, klikt op een prent en schrijft een kort antwoord.",
    link: { tekst: "Naar Spark", href: "/niveaus/spark" },
  },
  {
    datum: "11 november 2026",
    titel: "Frans in Start: pittige hoofdstukken en een uitdaging",
    tekst:
      "Frans in Start heeft nu, net als de andere vakken van Start, bij zes hoofdstukken een pittig broertje met 20 moeilijkere vragen, en een uitdagingshoofdstuk waarin alles door elkaar komt. Geen nieuwe leerstof: wel vragen met twee stappen, een fout die er juist uitziet of een Frans zinnetje om goed te lezen.",
    link: { tekst: "Naar Frans Start", href: "/niveaus/start/frans" },
  },
  {
    datum: "11 november 2026",
    titel: "Duidelijkere uitleg bij verzamelingen",
    tekst:
      "Bij verzamelingen staat nu uitgelegd dat de schuine streep door het teken voor 'is geen element van' erbij hoort en 'niet' betekent. Bij de doorsnede van de even getallen en de veelvouden van 3 staat het kleinste gemeenschappelijk veelvoud nu in gewone woorden uitgelegd.",
    opVraag: true,
  },
  {
    datum: "11 november 2026",
    titel: "Nieuw hoofdstuk: werken met Geopunt",
    tekst:
      "Bij aardrijkskunde Spark staat een nieuw hoofdstuk over Geopunt, de online kaart van Vlaanderen. In 26 vragen leer je een adres zoeken, kaartlagen aanzetten en afstanden meten. Bij een aantal vragen klik je zelf op de juiste knop in een echt Geopunt-scherm.",
    link: { tekst: "Naar aardrijkskunde Spark", href: "/niveaus/spark/aardrijkskunde" },
  },
  {
    datum: "11 november 2026",
    titel: "Pittige hoofdstukken bij economie in Beyond",
    tekst:
      "Bij elk van de twintig onderwerpen van algemene economie in Beyond doorstroom staat nu ook een pittig hoofdstuk met 30 moeilijkere vragen, zoals op het examen: klikken op een grafiek van vraag en aanbod, het juiste vak in een uitbetalingsmatrix aanduiden, rekenen met surplus, elasticiteit en de multiplicator, samenvattende tabellen invullen en casussen met meerdere vragen. Alle grafieken zijn zelf getekend.",
    link: { tekst: "Naar economie", href: "/niveaus/beyond-doorstroom/economie" },
  },
  {
    datum: "11 november 2026",
    titel: "Eén leerbundel per vak in Basis",
    tekst:
      "Bij Frans, Nederlands en wiskunde in Basis staat nu één leerbundel die alle onderwerpen van dat vak samenzet. Loop je vast bij een oefening, dan zoek je het onderwerp op en vind je er kort de uitleg en een voorbeeld. Je vindt de bundel bij elk hoofdstuk van het vak.",
  },
  {
    datum: "11 november 2026",
    titel: "Pittige hoofdstukken bij wiskunde basis",
    tekst:
      "Bij elk onderwerp van wiskunde basis voor Beyond doorstroom staat nu ook een pittig hoofdstuk met 30 moeilijkere vragen, zoals op het examen: klikken op een grafiek, een kansboom of een kruistabel, een samenvattende tabel invullen, en casussen met meerdere vragen. Ook de onderwerpen voor bedrijfswetenschappen kregen er een. Alle grafieken zijn zelf getekend. En in de Begrippenarena Wiskunde staat een nieuw niveau wiskunde basis, met ruim tachtig begrippen om spelend te herhalen.",
    link: { tekst: "Naar wiskunde basis", href: "/niveaus/beyond-doorstroom/wiskunde-basis" },
  },
  {
    datum: "11 november 2026",
    titel: "Leerbundels en oefenbundels voor drie vakken in Beyond",
    tekst:
      "In Beyond doorstroom krijgen economie, wiskunde basis en bedrijfswetenschappen en recht bij elk hoofdstuk een leerbundel, een oefenbundel met een antwoordblad achteraan en een klikbare leerbundel om stap voor stap door te nemen. Alle bundels hebben een witte achtergrond, zodat ze thuis makkelijk af te drukken zijn.",
  },
  {
    datum: "11 november 2026",
    titel: "Klikbare leerbundels bij wiskunde, en meer oefenbundels",
    tekst:
      "Bij wiskunde in Boost en Beyond doorstroom stonden de klikbare leerbundels wel klaar, maar je kon ze niet openen. Nu staat bij elk hoofdstuk de knop naar de leerbundel. We zetten ook oefenbundels op papier bij Nederlands in Spark, aardrijkskunde en biologie in Boost, en Frans en welzijnswetenschappen in Beyond.",
  },
  {
    datum: "10 november 2026",
    titel: "Na een fout zie je nu altijd wat juist was",
    tekst:
      "Bij een meerkeuzevraag met één juist antwoord stond na een fout niet altijd welk antwoord wel juist was. Nu staat dat er bij elke meerkeuzevraag. In de uitleg verwijzen we ook niet meer naar \"de laatste optie\" of \"het derde antwoord\", want de opties staan bij iedereen in een andere volgorde. Bij de reële getallen en bij economie zijn een paar vragen duidelijker gemaakt, en bij invulvragen rekenen we nu ook 37.5 % en 3 √2 goed.",
    opVraag: true,
  },
  {
    datum: "10 november 2026",
    titel: "Vier dingen rechtgezet na jullie meldingen",
    tekst:
      "Bij techniek rekenen we bij het schema met pijlen nu ook stroomschema, flowdiagram en processchema als juist. Bij de vraag over inox staat de uitleg nu in correct Nederlands. Bij mengsels en zuivere stoffen verraadt de vraag over het koken het antwoord niet meer. En in de leerstof over de reële getallen staat nu uitgelegd wat een periode is, en zijn de titels die vreemde tekens toonden weer gewoon leesbaar.",
    opVraag: true,
  },
  {
    datum: "10 november 2026",
    titel: "Hele cursus downloaden geeft de nieuwe lesbundel",
    tekst:
      "Heeft een vak al een nieuwe lesbundel met foto's over het hele vak, dan krijg je die nu als je op \"Hele cursus downloaden\" klikt. Bij geschiedenis Spark is dat een bundel van 27 bladzijden met 26 foto's. Vakken die nog geen nieuwe lesbundel hebben, geven gewoon de vertrouwde cursus.",
    link: { tekst: "Naar geschiedenis Spark", href: "/niveaus/spark/geschiedenis" },
  },
  {
    datum: "10 november 2026",
    titel: "Extra bundels over het hele vak",
    tekst:
      "Op de pagina van een vak staat nu, onder de hoofdstukken, een plek voor extra bundels die over het hele vak gaan: bijvoorbeeld een examen op papier om af te drukken, of een lesbundel met afbeeldingen. Als eerste staan er bij geschiedenis Spark een examen in drie versies en een lesbundel van 26 bladzijden met foto's over het hele vak. De verbetersleutels openen ouders met hun ouderpincode, zodat de oplossingen niet zomaar voor het grijpen liggen.",
    link: { tekst: "Naar geschiedenis Spark", href: "/niveaus/spark/geschiedenis" },
  },
  {
    datum: "9 november 2026",
    titel: "Pittige hoofdstukken bij bedrijfswetenschappen en recht",
    tekst:
      "Bij elk onderwerp van bedrijfswetenschappen en recht staat nu ook een pittig hoofdstuk met 30 moeilijkere vragen, zoals op het examen: rekenen met een aanslagbiljet of een factuur, een opzegtermijn aflezen in de wettelijke tabel, klikken op een break-evengrafiek of in een databank, en casussen met meerdere vragen. Alle prenten zijn zelf getekend.",
    link: { tekst: "Naar bedrijfswetenschappen en recht", href: "/niveaus/beyond-doorstroom/bedrijfswetenschappen-en-recht" },
  },
  {
    datum: "9 november 2026",
    titel: "Bedrijfswetenschappen en recht voor Beyond doorstroom",
    tekst:
      "Volg je bedrijfswetenschappen? Dan heb je nu ook je richtingsvak bedrijfswetenschappen en recht. Er zijn 40 hoofdstukken met 800 vragen: ondernemingsvormen en belastingen, boekhouden, kerncijfers en financiering, strategie en marketing, de arbeidsovereenkomst, logistiek, personeelsbeleid, kostprijs en databanken. In de begrippenarena economie staat er een niveau bij voor bedrijfswetenschappen.",
    link: { tekst: "Naar bedrijfswetenschappen en recht", href: "/niveaus/beyond-doorstroom/bedrijfswetenschappen-en-recht" },
  },
  {
    datum: "9 november 2026",
    titel: "Nieuw spel: de begrippenarena economie",
    tekst:
      "Er is een begrippenarena economie, met een niveau voor Boost en een niveau voor Beyond. Je oefent de begrippen in zes spellen, alleen, met het gezin of met de hele klas.",
    link: { tekst: "Naar de educatieve spellen", href: "/extras/spellen" },
  },
  {
    datum: "9 november 2026",
    titel: "Natuurwetenschappen Beyond: kies je richting",
    tekst:
      "Ook bij natuurwetenschappen in Beyond doorstroom kies je nu bovenaan voor welke richting je leert, net als bij wiskunde basis en geschiedenis. Kies je welzijnswetenschappen, dan krijg je de extra blauwe hoofdstukken over het menselijk lichaam erbij, ook in het examen. Kies je een andere richting, dan laten we ze weg.",
    link: { tekst: "Naar natuurwetenschappen", href: "/niveaus/beyond-doorstroom/natuurwetenschappen" },
  },
  {
    datum: "9 november 2026",
    titel: "Algemene economie voor Beyond doorstroom",
    tekst:
      "Beyond doorstroom heeft nu algemene economie, voor economie-wiskunde en bedrijfswetenschappen. Er zijn 40 hoofdstukken met 800 vragen, van de economische kringloop en de markt tot geld, inflatie, internationale handel en economisch onderzoek.",
    link: { tekst: "Naar economie", href: "/niveaus/beyond-doorstroom/economie" },
  },
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
