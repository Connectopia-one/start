/*
  Een woordje bij een vak, boven de hoofdstukken.

  Alles hier is gewone tekst. Wil je iets aanpassen of er een noot bij zetten
  voor een ander vak, dan hoef je geen code te kennen: pas de zinnen hieronder
  aan, of zet er een blok bij in dezelfde vorm. De sleutel is de categorie en
  de slug van het vak zoals ze in het webadres staan, bijvoorbeeld
  /niveaus/start/engels wordt "start/engels".

  Staat er voor een vak niets, dan toont de pagina gewoon geen kadertje.

  Kim op 29 september 2026, over Engels bij 🌱 Start: "bij engels start moet er
  mss een tekst bij dat dit niet bij de onderwijsdoelen hoort maar dat we dit
  zelf graag hebben, en een goede basis op jongere leeftijd geen kwaad kan,
  zeker in de tijd dat kinderen sneller in aanraking komen met Engels."
*/


/*
  Kelly, een mama uit de testgroep, op 20 oktober 2026: haar zoon is niet
  sterk in Frans en begon bij de eerste oefening, een tekst. Die was te hoog
  gegrepen, en omdat ze bovenaan stond dacht hij dat het daarna nog moeilijker
  werd. De volgorde volgt de vakfiche van de Examencommissie, niet de
  moeilijkheid. Dat zeggen we nu boven Frans.
*/
const fransVolgorde =
  "De hoofdstukken staan in de volgorde van de vakfiche van de " +
  "Examencommissie, niet van makkelijk naar moeilijk. Een tekst lezen staat " +
  "bovenaan, maar is voor veel jongeren net het moeilijkste. Is Frans niet " +
  "je sterkste vak, begin dan gerust bij de woordenschat of de grammatica, " +
  "en kom later terug naar de teksten.";

export const vaknoten: Record<string, string> = {
  "start/engels":
    "Engels hoort niet bij de minimumdoelen van het lager onderwijs. Wij zetten " +
    "het er zelf bij, omdat we het graag aanbieden: kinderen komen vandaag veel " +
    "vroeger met Engels in aanraking, en een goede basis op jonge leeftijd kan " +
    "geen kwaad. Oefen dus gerust mee, maar weet dat je kind hier op school nog " +
    "niet op beoordeeld wordt.",

  "boost-doorstroom/natuurwetenschappen":
    "Dit is het vak voor de richtingen die hun wetenschappen in één examen " +
    "afleggen: economische wetenschappen, humane wetenschappen, moderne talen " +
    "en Latijn. Zit je in natuurwetenschappen, dan heb je de drie aparte vakken " +
    "biologie, chemie en fysica nodig in plaats van dit vak.",

  "boost-doorstroom/biologie":
    "Dit vak is er voor de richting natuurwetenschappen, die haar wetenschappen " +
    "in drie aparte examens aflegt: biologie, chemie en fysica. Volg je een " +
    "andere richting met één examen wetenschappen, dan heb je het vak " +
    "natuurwetenschappen nodig in plaats van dit vak.",

  "boost-doorstroom/chemie":
    "Dit vak is er voor de richting natuurwetenschappen, die haar wetenschappen " +
    "in drie aparte examens aflegt: biologie, chemie en fysica. Volg je een " +
    "andere richting met één examen wetenschappen, dan heb je het vak " +
    "natuurwetenschappen nodig in plaats van dit vak.",

  "boost-doorstroom/fysica":
    "Dit vak is er voor de richting natuurwetenschappen, die haar wetenschappen " +
    "in drie aparte examens aflegt: biologie, chemie en fysica. Volg je een " +
    "andere richting met één examen wetenschappen, dan heb je het vak " +
    "natuurwetenschappen nodig in plaats van dit vak.",

  "beyond-doorstroom/natuurwetenschappen":
    "Dit is het vak voor de richtingen die hun wetenschappen in één examen " +
    "afleggen, zoals economie-moderne talen, humane wetenschappen, Latijn en " +
    "moderne talen. Zit je in natuurwetenschappen of een andere richting met " +
    "drie examens wetenschappen, dan heb je de aparte vakken biologie, chemie " +
    "en fysica nodig in plaats van dit vak.",


  "beyond-doorstroom/biologie":
    "Dit vak is er voor de richtingen die hun wetenschappen in drie aparte " +
    "examens afleggen: biologie, chemie en fysica. Volg je een richting met één " +
    "examen wetenschappen, dan heb je het vak natuurwetenschappen nodig in " +
    "plaats van dit vak.",
  "beyond-doorstroom/chemie":
    "Dit vak is er voor de richtingen die hun wetenschappen in drie aparte " +
    "examens afleggen: biologie, chemie en fysica. Volg je een richting met één " +
    "examen wetenschappen, dan heb je het vak natuurwetenschappen nodig in " +
    "plaats van dit vak.",
  "beyond-doorstroom/statistiek":
    "Statistiek is een apart examen voor humane wetenschappen. Volg je een " +
    "andere richting, dan zit de statistiek die jij nodig hebt gewoon in " +
    "wiskunde gevorderd.",

  "beyond-doorstroom/wiskunde":
    "Dit vak is voor economie-wiskunde, Latijn-wiskunde-wetenschappen en " +
    "wetenschappen-wiskunde. Het dekt de drie wiskunde-examens van die " +
    "richtingen samen. Examen G1 (analyse) zit in de eerste tien thema's, van " +
    "machten en logaritmen tot rijen. Examen G2 zit in de integralen, de " +
    "complexe getallen, de telproblemen, het kansrekenen en de statistiek. " +
    "Examen G3 zit in de matrices, de stelsels, de groepen, de ruimtemeetkunde " +
    "en het programmeren. Volg je een domeingebonden richting zoals " +
    "welzijnswetenschappen of bedrijfswetenschappen, dan is je eigen wiskunde " +
    "nog in de maak. Voor welzijnswetenschappen staat het vak " +
    "natuurwetenschappen welzijnswetenschappen er wel al.",

  "beyond-doorstroom/fysica":
    "Dit vak is er voor de richtingen die hun wetenschappen in drie aparte " +
    "examens afleggen: biologie, chemie en fysica. Volg je een richting met één " +
    "examen wetenschappen, dan heb je het vak natuurwetenschappen nodig in " +
    "plaats van dit vak.",

  "spark/frans": fransVolgorde,

  "boost-doorstroom/frans": fransVolgorde,

  "boost-dubbele-finaliteit/frans": fransVolgorde,

  "beyond-doorstroom/frans": fransVolgorde,

  "beyond-dubbele-finaliteit/frans": fransVolgorde,
};

/** De noot bij dit vak in deze categorie, of niets. */
/*
  Een opvallend groen kader bovenaan een vak, eventueel met een knop.

  Kim op 8 november 2026, over natuurwetenschappen welzijnswetenschappen: "dat
  moet er wel duidelijk bijstaan! anders gaan ze dit niet door hebben." En
  daarna: zet die hoofdstukken gewoon in het vak natuurwetenschappen, met een
  eigen kleur, "want zo staat er 1 vak natuurwetenschappen dat je kan
  aanpassen als het nodig is". Een leerling welzijnswetenschappen legt één
  examen af, en die vakfiche bevat alles van de gewone fiche 3DO plus een blok
  over het menselijk lichaam. Nagekeken lijn per lijn op Kims usb-stick. Zie
  ook lib/welzijn.ts.
*/
export type Wegwijzer = {
  titel: string;
  tekst: string;
  knop?: { label: string; href: string };
  /* true: bovenaan de keuze "Ik leer voor ..." (zie lib/leerrichting.ts). */
  richtingKeuze?: boolean;
  /* Mag weg: een uitklapbaar lijstje, bv. per hoofdstuk wat je mag overslaan. */
  lijstKop?: string;
  lijst?: { kop: string; tekst: string }[];
};

const wegwijzers: Record<string, Wegwijzer> = {

  /*
    Kim, 9 november 2026: één vak geschiedenis voor heel Beyond doorstroom,
    met duidelijk erbij wat bedrijfs- en welzijnswetenschappen niet nodig
    hebben. Zij volgen de vakfiche 3DDG, de anderen 3DDO. Vergeleken regel per
    regel met Kims werkdocument geschiedenis 3de graad. Geen enkel hoofdstuk
    valt helemaal weg, daarom een lijstje per hoofdstuk.
  */
  "beyond-doorstroom/geschiedenis": {
    titel: "Volg je bedrijfswetenschappen of welzijnswetenschappen? Dan heb je niet alles nodig.",
    tekst:
      "Jouw examen geschiedenis is wat lichter dan dat van de andere richtingen. " +
      "Je hebt elk hoofdstuk nodig, maar in de meeste hoofdstukken valt een stuk " +
      "weg. Kies hieronder voor welke richting je leert: dan krijg je enkel de vragen die je nodig hebt, ook in het examen. Je examen " +
      "duurt 150 minuten en de moderne tijd weegt bij jou iets zwaarder door.",
    richtingKeuze: true,
    lijstKop: "Wat mag ik overslaan? Bekijk het per hoofdstuk",
    lijst: [
      { kop: "Het historisch referentiekader", tekst: "niets, je hebt alles nodig." },
      { kop: "Restauratie, revolutie en het ontstaan van België", tekst: "verbindend en ontbindend nationalisme, het ontstaan van de Vlaamse beweging, de eenmaking van Duitsland en Bismarck." },
      { kop: "Industrialisatie en de sociale kwestie", tekst: "economisch liberalisme en kapitalisme als apart onderdeel, de geïndustrialiseerde regio's in België, hoe het kapitalisme ongelijkheid vergroot, hoe marxisme, sociaaldemocratie en christendemocratie opkwamen (hun ideeën ken je wel), het stemrecht in België, plattelandsvlucht, pendel- en seizoensarbeid, en coöperatie tegenover vakbond." },
      { kop: "Modern imperialisme, Congo en China", tekst: "het imperialisme in Azië, de VS, Japan en Rusland in Azië, de oprichting van de Congo-Vrijstaat, Stanley, de rol van leger, kerk en staat, en de binnenlandse problemen van China." },
      { kop: "De Eerste Wereldoorlog en de Russische revoluties", tekst: "de Volkenbond, het Veertienpuntenplan, het verloop in detail en alle Russische revoluties. Je kent wel de aanleiding en oorzaken, de overgang naar de loopgravenoorlog, de kantelpunten van 1917, het einde, de Duitse opmars in België en de Vrede van Versailles." },
      { kop: "Interbellum: totalitarisme en crisis", tekst: "de crisis van 1929 en de New Deal, de Mars op Rome, de opkomst van de NSDAP, de Conferentie van München en de appeasementpolitiek. De totalitaire regimes van Stalin, Mussolini en Hitler en het niet-aanvalspact ken je wel." },
      { kop: "De Tweede Wereldoorlog en de Holocaust", tekst: "het einde van de oorlog op de verschillende fronten en de Duitse opmars in België. Collaboratie en verzet ken je wel." },
      { kop: "Een nieuwe wereldorde: VN, Koude Oorlog en Europa", tekst: "de duurzame ontwikkelingsdoelen, de sterktes en zwaktes en de actuele uitdagingen van de VN, het verloop van de Koude Oorlog in detail (blokkade van Berlijn, Hongaarse opstand, bouw van de Muur, Brezjnev, Praagse Lente, SALT en SDI), de fasen van de Europese eenmaking en hoe de Europese instellingen werken. Wat ze mogen beslissen ken je wel." },
      { kop: "Dekolonisatie en de wereld van vandaag", tekst: "de dekolonisatie in Afrika en Azië in het algemeen, de gevolgen van de dekolonisatie, het verband met de Koude Oorlog, wat dekolonisatie vandaag nog betekent, en de vraag of Rusland-Oekraïne een nieuwe Koude Oorlog is. Congo, Israël-Palestina en de machtsverhoudingen sinds 1990 ken je wel." },
      { kop: "België na 1945", tekst: "het sociaal pact, de verzorgings- en welvaartsstaat, Leuven Vlaams, de staatshervormingen stap voor stap en de actuele debatten. De breuklijnen, de koningskwestie, de verzuiling en de bestuursniveaus ken je wel." },
      { kop: "Denken, kunst en emancipatie", tekst: "abolitionisme, sociaal darwinisme, eugenetica, de emancipatie van de vrouw, de jongerencultuur en de actuele protestbewegingen. De seksuele revolutie, holebi- en transrechten, de strijd tegen rassenscheiding in de VS en de kunststromingen ken je wel." },
      { kop: "Redeneren met historische bronnen", tekst: "zelf een onderzoeksvraag maken, representativiteit, de bewerking en presentatie van een bron, en bronnen met elkaar vergelijken. Bruikbaarheid en betrouwbaarheid ken je wel." },
      { kop: "Beeldvorming, vergelijken en verleden-heden-toekomst", tekst: "enkel een paar vergelijkingspunten: (neo)kolonialisme, wij-zij-denken, levensbeschouwing en economische systemen." },
      { kop: "De Volksrepubliek China: van Mao tot Xi", tekst: "de gevolgen van de machtsovername van Mao en China in Afrika." },
      { kop: "De Israëlisch-Palestijnse kwestie", tekst: "niets, je hebt alles nodig." },
      { kop: "Denkstromingen en kunststromingen van de 19de en 20ste eeuw", tekst: "abolitionisme, sociaal darwinisme en eugenetica. De andere denkstromingen en de kunststromingen ken je wel." },
      { kop: "Kunst en cultuur analyseren met het stappenplan", tekst: "niets, je hebt alles nodig." },
    ],
  },
  "beyond-doorstroom/natuurwetenschappen": {
    titel: "Volg je welzijnswetenschappen? Maak dan ook de blauwe hoofdstukken onderaan.",
    tekst:
      "Jouw examen natuurwetenschappen bevat alles van dit vak, plus een extra " +
      "deel over het menselijk lichaam: enzymen, spijsvertering, uitscheiding, " +
      "bloed, hart en bloedsomloop, bloeddruk en lymfe, en ademhaling. Die " +
      "hoofdstukken staan onderaan in het blauw, met het label Enkel " +
      "welzijnswetenschappen. Bij jou weegt biologie zwaarder door: 50 procent, " +
      "chemie 15, fysica 25 en onderzoek 10. Volg je een andere richting, dan " +
      "sla je de blauwe hoofdstukken over.",
    knop: { label: "Examen voor welzijnswetenschappen", href: "examen?welzijn=1" },
  },
};

export function vindWegwijzer(niveau: string, vak: string): Wegwijzer | undefined {
  return wegwijzers[`${niveau}/${vak}`];
}

export function vindVaknoot(niveau: string, vak: string): string | undefined {
  return vaknoten[`${niveau}/${vak}`];
}
