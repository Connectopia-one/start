/*
  De observatielijst: het blad dat ouders zelf invullen en meenemen naar
  school, het CLB, de psycholoog of een andere specialist.

  Opbouw van dit bestand
    observatieTekst   de kop, de uitleg en de waarschuwing bovenaan
    gegevens          de invulvakjes bovenaan het blad (naam, klas, datum ...)
    onderdelen        de hoofdstukken met de vragen
    openVragen        de vragen waar je zelf een antwoord bij schrijft
    overlap           de uitleg over wat op wat lijkt, onderaan
    slot              het groene blok helemaal onderaan

  Een vraag toevoegen? Zet er een regel bij in de lijst "vragen" van het
  juiste onderdeel. Een vraag weghalen? Verwijder die regel. Meer moet niet.
*/

import type { Kleur } from "@/content/site";

export type Vraag = {
  tekst: string;
  /* Een korte verduidelijking tussen haakjes, alleen als de vraag die nodig heeft. */
  toelichting?: string;
};

export type ObservatieOnderdeel = {
  nummer: string;
  titel: string;
  kleur: Kleur;
  icoon: string;
  inleiding: string;
  vragen: Vraag[];
};

export const observatieTekst = {
  label: "Gratis observatielijst",
  titel: "Wat zie jij bij je kind?",
  handgeschreven: "Een blad om in te vullen en mee te nemen.",
  tekst:
    "Een uitgebreide lijst met kenmerken die voorkomen bij hoogbegaafdheid, uitzonderlijke hoogbegaafdheid, autisme en ADHD. Vul in wat je herkent, schrijf erbij wat je opvalt, en neem het blad mee naar de leerkracht, het CLB, de psycholoog of de specialist. Zo begint het gesprek niet bij nul.",

  /* De belangrijkste zin van de pagina. Die staat in een opvallend kader. */
  waarschuwing:
    "Dit is geen test en geen diagnose. Deze lijst zegt niet wat je kind heeft en sluit niets uit. Het is een gratis observatieblad, gemaakt om je gedachten te ordenen en je gesprek concreter te maken. Alleen een deskundige kan een diagnose stellen.",

  /* De praktische uitleg boven de lijst. Elke regel wordt een punt. */
  hoeInvullen: [
    "Vul in wat je de voorbije maanden echt gezien hebt, niet wat je vreest of hoopt.",
    "Kruis aan hoe vaak je iets ziet: soms, vaak of bijna altijd. Zie je het niet, laat de regel dan gewoon leeg.",
    "Veel vinkjes in veel onderdelen is heel normaal. De kenmerken van hoogbegaafdheid, autisme en ADHD overlappen sterk, en een kind is nooit één lijstje.",
    "Onder elk onderdeel is plaats om te noteren of je het vooral thuis ziet, vooral op school, of allebei. Dat verschil is vaak het belangrijkste stuk informatie.",
    "Schrijf gerust voorbeelden op. Eén concrete situatie zegt een specialist meer dan tien vinkjes.",
    "Laat het blad ook eens invullen door iemand anders: je partner, de leerkracht, een grootouder. Twee blikken naast elkaar leveren het rijkste gesprek op.",
    "Neem het ingevulde blad mee naar je gesprek. Print het af, of vul het op je scherm in en druk het af via het menu van je browser.",
  ],

  /* Deze zin staat bij de vinkjes zelf. */
  kolommen: ["soms", "vaak", "bijna altijd"],
  plaatsVraag: "Waar zie je dit vooral?",
  plaatsOpties: ["vooral thuis", "vooral op school", "allebei"],
  notitieVraag: "Wat valt jou nog op bij dit onderdeel?",

  afdrukken:
    "Deze pagina is gemaakt om af te drukken. Gebruik het afdrukmenu van je browser (Ctrl+P op Windows, Cmd+P op een Mac, of Delen en dan Afdrukken op je telefoon). De vinkjes die je op je scherm zet, komen mee op papier.",

  slot: {
    titel: "Wil je dat we meekijken?",
    tekst:
      "Heb je de lijst ingevuld en weet je niet goed wat je ermee moet? Stuur ons gerust een bericht, of vraag een gratis telefonisch gesprek aan. We denken met je mee, en we kunnen ook mee op gesprek gaan bij school of bij een dienst.",
    knopTekst: "Neem contact op",
    knopLink: "/contact",
  },
};

/* De invulvakjes bovenaan het blad. */
export const gegevens = [
  "Naam van het kind",
  "Geboortedatum",
  "Leeftijd",
  "School en klas of leerjaar",
  "Ingevuld door",
  "Datum van invullen",
  "Voor welk gesprek neem je dit mee?",
];

export const onderdelen: ObservatieOnderdeel[] = [
  {
    nummer: "1",
    titel: "Leren en denken",
    kleur: "green",
    icoon: "🧠",
    inleiding:
      "Hoe je kind nieuwe dingen oppikt, en wat er gebeurt als de stof te makkelijk of net te moeilijk is.",
    vragen: [
      { tekst: "Pikt nieuwe leerstof heel snel op en heeft weinig herhaling nodig." },
      { tekst: "Kon al lezen, rekenen of klokkijken voor het op school aan bod kwam." },
      { tekst: "Stelt veel en diepe vragen, ook over dingen die ver buiten zijn leeftijd liggen." },
      { tekst: "Legt uit zichzelf verbanden tussen dingen die niets met elkaar lijken te maken hebben." },
      { tekst: "Heeft een opvallend goed geheugen voor details, feiten of gebeurtenissen van lang geleden." },
      { tekst: "Verveelt zich zichtbaar in de klas, of zegt dat school saai is." },
      { tekst: "Wil weten waarom iets zo is, en neemt geen genoegen met 'dat is nu eenmaal zo'." },
      { tekst: "Slaat tussenstappen over en komt toch bij het juiste antwoord, maar kan niet uitleggen hoe." },
      { tekst: "Denkt in beelden of in het geheel, eerder dan stap voor stap." },
      { tekst: "Wil iets pas doen als het meteen goed lukt, en begint er anders niet aan.", toelichting: "perfectionisme" },
      { tekst: "Is bang om fouten te maken, of raakt van slag door één fout." },
      { tekst: "Zet zich af tegen herhalingsoefeningen, invulbladen of huiswerk dat het al kan." },
      { tekst: "Heeft moeite met dingen die wel oefening vragen, zoals handschrift, tafels of schoenveters." },
      { tekst: "Presteert op school duidelijk minder dan je op basis van thuis zou verwachten.", toelichting: "onderpresteren" },
    ],
  },
  {
    nummer: "2",
    titel: "Taal en communicatie",
    kleur: "purple",
    icoon: "💬",
    inleiding:
      "Hoe je kind praat, en hoe het aankomt wat anderen zeggen.",
    vragen: [
      { tekst: "Gebruikt woorden en zinnen die je bij kinderen van die leeftijd zelden hoort." },
      { tekst: "Praat graag en lang over onderwerpen die het interesseren." },
      { tekst: "Neemt uitdrukkingen letterlijk, of raakt in de war van grapjes en sarcasme." },
      { tekst: "Heeft moeite om een gesprek te beginnen, of net om het te stoppen." },
      { tekst: "Praat eerder over een onderwerp dan met de andere persoon." },
      { tekst: "Merkt niet altijd aan een gezicht of een toon hoe iemand zich voelt." },
      { tekst: "Kijkt weinig aan tijdens het praten, of net heel intens." },
      { tekst: "Herhaalt zinnen, woorden of stukjes uit filmpjes." },
      { tekst: "Praat druk en snel, valt anderen in de rede of praat door hen heen." },
      { tekst: "Verliest de draad van een verhaal en springt van de hak op de tak." },
      { tekst: "Zwijgt op school bijna volledig, terwijl het thuis honderduit praat." },
      { tekst: "Corrigeert volwassenen als die iets onjuist of onzorgvuldig zeggen." },
    ],
  },
  {
    nummer: "3",
    titel: "Aandacht en concentratie",
    kleur: "orange",
    icoon: "🎯",
    inleiding:
      "Waar de aandacht naartoe gaat, en of je kind ze kan sturen.",
    vragen: [
      { tekst: "Is snel afgeleid door geluid, beweging of door eigen gedachten." },
      { tekst: "Begint aan van alles, maar maakt weinig af." },
      { tekst: "Raakt spullen kwijt, vergeet boeken, brooddozen of afspraken." },
      { tekst: "Lijkt niet te luisteren als je iets rechtstreeks zegt." },
      { tekst: "Dagdroomt, staart voor zich uit of zit 'in zijn eigen wereld'." },
      { tekst: "Kan zich juist uren aan één stuk vastbijten in iets dat het boeit.", toelichting: "hyperfocus" },
      { tekst: "Is dan nauwelijks los te krijgen van die bezigheid." },
      { tekst: "Heeft moeite om aan een taak te beginnen, ook als het wil.", toelichting: "uitstel" },
      { tekst: "Maakt slordige fouten in werk dat het eigenlijk goed beheerst." },
      { tekst: "Heeft veel meer tijd nodig voor huiswerk dan de leerkracht inschat." },
      { tekst: "Werkt beter met een volwassene naast zich dan alleen." },
      { tekst: "Vergeet in een reeks van drie opdrachten de tweede en de derde." },
    ],
  },
  {
    nummer: "4",
    titel: "Beweging, impuls en rem",
    kleur: "blue",
    icoon: "⚡",
    inleiding:
      "Hoeveel je kind beweegt, en hoe goed het op de rem kan gaan staan.",
    vragen: [
      { tekst: "Wiebelt, friemelt, kantelt met de stoel of staat voortdurend recht." },
      { tekst: "Heeft moeite om stil te zitten aan tafel of in de klas." },
      { tekst: "Flapt antwoorden eruit voor de vraag af is." },
      { tekst: "Heeft het moeilijk om zijn beurt af te wachten." },
      { tekst: "Doet eerst en denkt daarna." },
      { tekst: "Neemt risico's zonder het gevaar te zien: klimmen, oversteken, springen." },
      { tekst: "Botst, stoot of laat dingen vallen, lijkt onhandig in de ruimte." },
      { tekst: "Beweegt met het hele lijf als het blij of boos is: springen, fladderen, wiegen." },
      { tekst: "Is 's avonds nog even druk als 's morgens." },
      { tekst: "Heeft veel beweging nodig om zich daarna te kunnen concentreren." },
      { tekst: "Is net opvallend rustig en stil, en valt daardoor nergens op." },
    ],
  },
  {
    nummer: "5",
    titel: "Prikkels en zintuigen",
    kleur: "green",
    icoon: "👂",
    inleiding:
      "Hoe hard de wereld binnenkomt: geluid, licht, geur, smaak en aanraking.",
    vragen: [
      { tekst: "Schrikt of lijdt onder harde geluiden: de refter, een handdroger, een alarm." },
      { tekst: "Hoort geluiden die anderen niet opmerken: een zoemende lamp, een klok." },
      { tekst: "Houdt de handen op de oren, of wil een koptelefoon." },
      { tekst: "Heeft last van fel licht, tl-lampen of veel visuele drukte." },
      { tekst: "Klaagt over labels, naden, sokken, of wil altijd dezelfde kleren." },
      { tekst: "Is kieskeurig met eten: structuur, kleur, temperatuur of dingen die elkaar raken." },
      { tekst: "Ruikt dingen die anderen niet ruiken, of walgt van bepaalde geuren." },
      { tekst: "Houdt niet van onverwachte aanraking, knuffels of kammen en nagels knippen." },
      { tekst: "Zoekt juist veel prikkels op: harde muziek, stevig knuffelen, draaien, botsen." },
      { tekst: "Merkt pijn, honger, kou of aandrang pas heel laat op." },
      { tekst: "Is helemaal op na een drukke dag, een feest of een uitstap." },
      { tekst: "Heeft een eigen plekje nodig om tot rust te komen." },
    ],
  },
  {
    nummer: "6",
    titel: "Emoties en gevoeligheid",
    kleur: "orange",
    icoon: "❤️",
    inleiding:
      "Hoe groot gevoelens binnenkomen, en wat je kind ermee kan.",
    vragen: [
      { tekst: "Voelt alles intens: heel blij, heel verdrietig, heel boos, weinig ertussen." },
      { tekst: "Heeft een sterk rechtvaardigheidsgevoel en kan niet tegen oneerlijkheid." },
      { tekst: "Trekt zich het verdriet van anderen sterk aan." },
      { tekst: "Ligt wakker van het nieuws, van oorlog, van dieren of van het klimaat." },
      { tekst: "Denkt na over de dood, over zin en over hoe alles in elkaar zit.", toelichting: "existentiële vragen" },
      { tekst: "Kan van klein naar heel groot gaan in enkele seconden." },
      { tekst: "Heeft lang nodig om weer rustig te worden na een woede of een verdriet." },
      { tekst: "Kan moeilijk benoemen wat het voelt." },
      { tekst: "Heeft veel angsten, piekert of vraagt voortdurend om geruststelling." },
      { tekst: "Is bang om te falen of durft nieuwe dingen niet te proberen.", toelichting: "faalangst" },
      { tekst: "Houdt zich op school de hele dag groot en ontploft thuis." },
      { tekst: "Praat hard over zichzelf: 'ik kan niets', 'ik ben dom', 'niemand wil met mij spelen'." },
    ],
  },
  {
    nummer: "7",
    titel: "Contact met andere kinderen",
    kleur: "purple",
    icoon: "🧩",
    inleiding:
      "Hoe het gaat op de speelplaats, in de klasgroep en bij vriendjes thuis.",
    vragen: [
      { tekst: "Sluit makkelijker aan bij oudere kinderen of bij volwassenen dan bij leeftijdsgenoten." },
      { tekst: "Vindt de spelletjes van klasgenoten kinderachtig of saai." },
      { tekst: "Wil graag meedoen maar weet niet goed hoe het moet beginnen." },
      { tekst: "Neemt in een spel meteen de leiding en bepaalt de regels." },
      { tekst: "Kan slecht verliezen, of stopt liever dan te verliezen." },
      { tekst: "Speelt liever alleen, en lijkt daar ook gelukkig bij." },
      { tekst: "Heeft één vriend of vriendin en verder niemand." },
      { tekst: "Wordt buitengesloten, geplaagd of gepest." },
      { tekst: "Past zich helemaal aan om erbij te horen, en verliest zichzelf daarin.", toelichting: "maskeren" },
      { tekst: "Begrijpt ongeschreven regels van een groep niet meteen." },
      { tekst: "Botst met klasgenoten over eerlijkheid, regels of de juiste manier." },
      { tekst: "Bloeit helemaal open zodra het bij kinderen zit die hetzelfde denken." },
    ],
  },
  {
    nummer: "8",
    titel: "Structuur, verandering en routine",
    kleur: "blue",
    icoon: "🔄",
    inleiding:
      "Hoe je kind omgaat met wat er komt, en met wat er plots anders loopt.",
    vragen: [
      { tekst: "Wil vooraf weten wat er gaat gebeuren, en hoe laat." },
      { tekst: "Raakt van slag als een plan verandert, ook bij een leuke verandering." },
      { tekst: "Heeft vaste routines en gewoontes die niet doorbroken mogen worden." },
      { tekst: "Heeft het moeilijk met overgangen: stoppen met spelen, naar bed, naar school." },
      { tekst: "Heeft moeite met een vervangleerkracht, een andere plaats in de klas of een uitstap." },
      { tekst: "Kan een grote opdracht niet opsplitsen in stappen." },
      { tekst: "Heeft weinig besef van tijd: hoe lang iets duurt, of wanneer het moet beginnen." },
      { tekst: "Heeft een chaotische boekentas, kamer of bureau." },
      { tekst: "Werkt veel beter met een lijstje, een pictogram of een duidelijk schema." },
      { tekst: "Stelt steeds dezelfde vragen over wat er gaat komen." },
      { tekst: "Ordent en sorteert graag: op kleur, op grootte, op systeem." },
    ],
  },
  {
    nummer: "9",
    titel: "Interesses en spel",
    kleur: "green",
    icoon: "🔭",
    inleiding:
      "Waar je kind vanzelf naartoe gaat als het mag kiezen.",
    vragen: [
      { tekst: "Heeft één of twee onderwerpen waar het alles over wil weten." },
      { tekst: "Gaat daarin veel dieper dan je bij die leeftijd zou verwachten." },
      { tekst: "Praat daar met iedereen over, ook als de ander niet meer luistert." },
      { tekst: "Verzamelt, sorteert of ordent dingen volgens een eigen systeem." },
      { tekst: "Herhaalt graag hetzelfde spel, hetzelfde filmpje of hetzelfde boek." },
      { tekst: "Speelt uitgebreide fantasiespelen met eigen werelden, talen of regels." },
      { tekst: "Bouwt, knutselt of programmeert liever zelf iets dan mee te doen met een spel." },
      { tekst: "Wisselt snel van interesse en laat begonnen dingen liggen." },
      { tekst: "Kiest liever iets moeilijks dan iets dat het al kan." },
      { tekst: "Vindt het lastig om zomaar te spelen zonder doel." },
    ],
  },
  {
    nummer: "10",
    titel: "School en schoolwerk",
    kleur: "purple",
    icoon: "🏫",
    inleiding:
      "Wat je ziet van de schooldag, van de rapporten en van het huiswerk.",
    vragen: [
      { tekst: "Wil 's morgens niet naar school, klaagt over buikpijn of hoofdpijn." },
      { tekst: "Zegt dat school saai is, of dat het toch niets nieuws leert." },
      { tekst: "Heeft resultaten die sterk schommelen van vak tot vak of van maand tot maand." },
      { tekst: "Krijgt opmerkingen over werkhouding, tempo of slordigheid." },
      { tekst: "Krijgt opmerkingen over storend gedrag of praten in de klas." },
      { tekst: "Doet op school niets en thuis wel, of net omgekeerd." },
      { tekst: "Huiswerk loopt uit op een dagelijkse strijd." },
      { tekst: "Doet expres minder dan het kan om niet op te vallen." },
      { tekst: "Gaat sinds een bepaald moment duidelijk achteruit." },
      { tekst: "De leerkracht herkent het kind dat jij thuis ziet niet." },
      { tekst: "Kreeg al maatregelen of een traject aangeboden.", toelichting: "verrijking, versnelling, zorgtraject" },
    ],
  },
  {
    nummer: "11",
    titel: "Thuis en op school: het verschil",
    kleur: "orange",
    icoon: "🎭",
    inleiding:
      "Veel kinderen houden zich de hele schooldag groot en laten pas thuis zien hoe zwaar het was. Dit onderdeel gaat precies over dat verschil, en het is vaak het onderdeel waar een specialist het meest aan heeft.",
    vragen: [
      { tekst: "Is op school rustig en aangepast, en thuis boos, verdrietig of explosief." },
      { tekst: "Ontlaadt meteen na schooltijd, in de auto of aan de deur." },
      { tekst: "Is op vrijdagavond en in vakanties een duidelijk ander kind." },
      { tekst: "Doet op school precies na wat anderen doen om niet op te vallen." },
      { tekst: "Vertelt thuis niets over de schooldag." },
      { tekst: "Zegt op school dat alles goed gaat terwijl het thuis huilt." },
      { tekst: "Heeft na een schooldag uren nodig om te bekomen." },
      { tekst: "Toont zijn interesses en zijn humor alleen thuis." },
      { tekst: "Je krijgt van school te horen dat er niets aan de hand is, terwijl jij je zorgen maakt." },
      { tekst: "Je twijfelt zelf of je overdrijft." },
    ],
  },
  {
    nummer: "12",
    titel: "Slaap, eten en lichaam",
    kleur: "blue",
    icoon: "🌙",
    inleiding:
      "Het lichaam vertelt vaak mee wat er aan de hand is.",
    vragen: [
      { tekst: "Komt 's avonds moeilijk tot rust of ligt lang wakker met een hoofd vol gedachten." },
      { tekst: "Wordt 's nachts wakker, heeft nachtmerries of komt naar je bed." },
      { tekst: "Slaapt duidelijk minder dan leeftijdsgenoten." },
      { tekst: "Is overdag moe, of net oververmoeid en daardoor druk." },
      { tekst: "Heeft vaak buikpijn of hoofdpijn zonder dat er iets gevonden wordt." },
      { tekst: "Eet heel weinig of heel eenzijdig." },
      { tekst: "Vergeet te eten of te drinken als het ergens in opgaat." },
      { tekst: "Heeft moeite met zindelijkheid, ook op een leeftijd waarop dat voorbij zou zijn." },
      { tekst: "Heeft een moeilijk handschrift, of schrijven vermoeit snel." },
      { tekst: "Beweegt houterig, of leerde fietsen en veters strikken later dan anderen." },
    ],
  },
  {
    nummer: "13",
    titel: "Zelfbeeld en welbevinden",
    kleur: "green",
    icoon: "🪞",
    inleiding:
      "Hoe je kind over zichzelf praat. Dit onderdeel is klein maar weegt zwaar: neem het zeker mee naar je gesprek.",
    vragen: [
      { tekst: "Zegt dat het dom is, anders is, of niet deugt." },
      { tekst: "Zegt dat het nergens bij hoort of dat niemand het begrijpt." },
      { tekst: "Is streng voor zichzelf en legt de lat onhaalbaar hoog." },
      { tekst: "Durft niets nieuws meer te proberen uit angst om te mislukken." },
      { tekst: "Is somber, futloos of heeft nergens meer zin in." },
      { tekst: "Trekt zich terug, ook van dingen die het vroeger graag deed." },
      { tekst: "Is sinds een bepaalde periode duidelijk veranderd." },
      { tekst: "Doet zichzelf pijn, of praat over niet meer willen leven." },
    ],
  },
];

/*
  De vragen waar je zelf een antwoord bij schrijft.
  regels = hoeveel schrijflijntjes er onder de vraag komen.
*/
export const openVragen: { vraag: string; regels: number }[] = [
  { vraag: "Waar is je kind goed in? Waar bloeit het helemaal van op?", regels: 3 },
  { vraag: "Wanneer heb je je kind het laatst echt gelukkig gezien? Wat gebeurde er toen?", regels: 3 },
  { vraag: "Wat maakt je het meest ongerust, en sinds wanneer?", regels: 3 },
  { vraag: "Beschrijf één concrete situatie die volgens jou alles samenvat.", regels: 4 },
  { vraag: "Wat heb je zelf al geprobeerd? Wat hielp, en wat werkte niet?", regels: 3 },
  { vraag: "Wat zegt je kind er zelf over?", regels: 3 },
  { vraag: "Wat zegt de school of de opvang?", regels: 3 },
  { vraag: "Komt iets van dit alles ook voor bij broers, zussen, ouders of verder in de familie?", regels: 3 },
  { vraag: "Is er iets gebeurd dat kan meespelen?", regels: 3 },
  { vraag: "Wat wil je uit dit gesprek halen? Wat is je belangrijkste vraag?", regels: 3 },
];

/*
  De uitleg onderaan: waarom er geen diagnoses bij de vragen staan,
  en wat er zoal op elkaar lijkt.
*/
export const overlapTekst = {
  titel: "Waarom staat er geen diagnose bij de vragen?",
  inleiding:
    "Omdat dezelfde observatie naar heel verschillende dingen kan wijzen. Een kind dat niet stilzit, zijn werk niet afmaakt en door de leerkracht heen praat, kan ADHD hebben. Het kan ook een kind zijn dat zich al maanden stierlijk verveelt. Het verschil zit niet in wat je ziet, maar in waarom het gebeurt, en dat kan alleen iemand met ervaring beoordelen. Daarom zijn de vragen hierboven geordend per thema en niet per diagnose.",
  paren: [
    {
      titel: "Hoogbegaafdheid en ADHD",
      tekst:
        "Verveling en ADHD zien er van buiten bijna hetzelfde uit: druk, afgeleid, alles half af. Een verschil dat vaak meespeelt: bij verveling verdwijnt het grotendeels zodra de stof wél uitdaagt, bij ADHD blijft de moeite met aandacht en rem ook opduiken in dingen die het kind graag doet. Maar hyperfocus kan dat beeld weer vertroebelen, en beide komen ook samen voor.",
    },
    {
      titel: "Hoogbegaafdheid en autisme",
      tekst:
        "Diepe interesses, oog voor detail, een sterk rechtvaardigheidsgevoel, gevoelig voor prikkels, moeilijk aansluiting vinden: dat hoort bij allebei. Een verschil dat vaak meespeelt: botst je kind op een verschil in tempo en interesse met leeftijdsgenoten, of is het aflezen van sociale signalen zelf moeilijk, ook bij kinderen die wél passen? Dat onderscheid is subtiel en vraagt een deskundige.",
    },
    {
      titel: "Autisme en ADHD",
      tekst:
        "Moeite met overgangen, met plannen, met prikkels en met grote emoties komt bij allebei voor. Ze worden ook vaak samen vastgesteld. Een kind kan dus perfect beide profielen hebben, en dan versterken ze elkaar.",
    },
    {
      titel: "Uitzonderlijke hoogbegaafdheid",
      tekst:
        "Bij UHB is de afstand tot leeftijdsgenoten nog groter, en valt het kind nog meer uit de toon: in taal, in interesses, in wat het al doorheeft. Gewone testen lopen bovenaan tegen hun plafond aan, waardoor het beeld onvolledig blijft. Vraag daarom expliciet naar ervaring met uitzonderlijke hoogbegaafdheid.",
    },
    {
      titel: "Twee dingen tegelijk, en maskeren",
      tekst:
        "Een hoge begaafdheid kan een autisme of een ADHD jarenlang toedekken: het kind compenseert met zijn verstand tot dat niet meer lukt. Omgekeerd kan een autisme of een ADHD de begaafdheid toedekken, want dan zakken de resultaten van de test. Zo'n dubbel profiel valt bijna altijd laat op, en zelden bij een korte screening. Daarom vragen we je hierboven zo nadrukkelijk naar het verschil tussen thuis en school.",
    },
  ],
  /* Deze zin staat in een opvallend kader onder de uitleg. */
  nadruk:
    "Zelf doen wij geen diagnostische testingen. Een testing heeft het oog nodig van een deskundige die maskering en overlap kan doorprikken, en die breder kijkt dan het IQ-nummer of het gedrag dat stoort.",
};

/* Wat je doet als je je nú zorgen maakt. Dit blok staat bewust apart. */
export const hulpNu = {
  titel: "Maak je je nu zorgen over je kind?",
  tekst:
    "Doet je kind zichzelf pijn, of praat het over niet meer willen leven? Wacht dan geen traject af. Bel je huisarts, of bel Awel op het nummer 102, of de Zelfmoordlijn op 1813. Dat mag ook midden in een onderzoek of een wachtlijst.",
};
