/*
  De pagina over thuisonderwijs en de Examencommissie.

  Kim op 14 oktober 2026: "ik wil absoluut niet zeggen dat thuisonderwijs
  beter is dan school. dit is echt afhankelijk van elk kind en wat hij of zij
  nodig heeft. (...) zoals onze kinderen groeien groeien ook de trajecten."
  Die lijn staat bovenaan in "waarden" en moet daar blijven staan.

  Alle regels hieronder komen van de pagina's van de Vlaamse overheid zelf,
  die onderaan als bron staan. Verandert er iets aan de regelgeving, kijk dan
  eerst die twee pagina's na voor je hier iets aanpast.
*/

export const thuisonderwijsTekst = {
  label: "Hulp, advies en tips",
  titel: "Thuisonderwijs en de Examencommissie",
  handgeschreven: "Geen enkele weg is de juiste voor élk kind.",
  tekst:
    "Veel ouders horen deze woorden voor het eerst als het op school moeilijk loopt. Hieronder staat in gewone taal wat ze betekenen, zodat je zelf kan nadenken over wat bij jouw kind past.",
};

export const waarden = [
  "Wij zeggen nergens dat thuisonderwijs beter is dan school. Dat hangt helemaal af van je kind en van wat het nú nodig heeft.",
  "Wat dit jaar werkt, kan volgend jaar niet meer werken. Zoals onze kinderen groeien, groeien ook hun trajecten.",
  "Bij die zoektocht helpen we graag mee denken, zonder je in een richting te duwen.",
];

export type Blok = {
  titel: string;
  inleiding?: string;
  /* Elk punt begint met een vetgedrukt stukje, daarna de uitleg. */
  punten?: { dik: string; tekst: string }[];
  /* Een tussentitel met eigen punten, voor lager en secundair apart. */
  delen?: { titel: string; punten: { dik: string; tekst: string }[] }[];
  slot?: string;
};

export const blokken: Blok[] = [
  {
    titel: "Wat is thuisonderwijs eigenlijk?",
    inleiding:
      "In Vlaanderen is er leerplicht van 5 tot 18 jaar, maar geen schoolplicht. Je mag je kind thuis onderwijs geven, en dat heet officieel huisonderwijs.",
    punten: [
      {
        dik: "Je meldt het elk schooljaar opnieuw",
        tekst:
          "uiterlijk de derde schooldag, via het Loket Huisonderwijs van AGODI. De melding geldt tot 31 augustus.",
      },
      {
        dik: "Je kind kan niet tegelijk ingeschreven zijn",
        tekst: "op een erkende school en in huisonderwijs.",
      },
      {
        dik: "Er zijn geen verplichte vakken, boeken of leerplannen",
        tekst: "en je hebt zelf geen diploma nodig om les te geven.",
      },
      {
        dik: "Je kiest een CLB",
        tekst: "in je provincie, en de gewone CLB-contacten blijven doorgaan.",
      },
      {
        dik: "De onderwijsinspectie komt kijken.",
        tekst:
          "Ze stelt drie data voor. Weiger je, of zijn twee bezoeken na elkaar ongunstig, dan moet je kind terug naar een erkende school.",
      },
      {
        dik: "De kosten zijn voor jezelf,",
        tekst: "er is geen schooltoeslag.",
      },
    ],
  },
  {
    titel: "De examens horen erbij",
    inleiding:
      "Een kind in huisonderwijs haalt zijn getuigschriften bij de Examencommissie. Daar hangen leeftijden aan vast, en dat is het stuk dat ouders het vaakst verrast.",
    delen: [
      {
        titel: "Lager onderwijs",
        punten: [
          {
            dik: "Inschrijven",
            tekst:
              "doe je in het schooljaar waarin je kind vóór 1 januari elf wordt.",
          },
          {
            dik: "Het getuigschrift basisonderwijs",
            tekst:
              "moet behaald zijn in het schooljaar waarin je kind vóór 1 januari dertien wordt.",
          },
          {
            dik: "Er zijn twee pogingen.",
            tekst:
              "Lukt het daarna niet, dan gaat je kind naar een erkende school.",
          },
        ],
      },
      {
        titel: "Secundair onderwijs",
        punten: [
          {
            dik: "Inschrijven",
            tekst:
              "doe je uiterlijk in het schooljaar waarin je kind vóór 1 januari vijftien wordt.",
          },
          {
            dik: "Het getuigschrift van de eerste graad",
            tekst:
              "moet behaald zijn in het schooljaar waarin je kind vóór 1 januari zestien wordt.",
          },
          {
            dik: "Vrijstelling van examens",
            tekst:
              "kan bij een ernstige leerstoornis of een mentale handicap. Alleen het CLB dat je koos, kan die geven.",
          },
        ],
      },
    ],
  },
  {
    titel: "Hoe werkt de Examencommissie secundair?",
    punten: [
      {
        dik: "Iedereen mag meedoen.",
        tekst:
          "Leeftijd, nationaliteit en vooropleiding spelen geen rol. Wie nog leerplichtig is, moet wel ofwel naar school gaan ofwel huisonderwijs volgen.",
      },
      {
        dik: "Het is zelfstudie.",
        tekst:
          "De Examencommissie neemt examens af, maar geeft zelf geen lessen, cursussen of begeleiding.",
      },
      {
        dik: "Je kiest een graad en een studierichting.",
        tekst:
          "Het inschrijvingsgeld is 41 euro per studierichting, niet per examen.",
      },
      {
        dik: "Je plant je examens zelf,",
        tekst:
          "vak per vak, op het kandidatenplatform. Aanmelden gebeurt met de eID of een digitale sleutel.",
      },
      {
        dik: "De examens zijn digitaal",
        tekst: "en gaan door in het examencentrum in Brussel.",
      },
      {
        dik: "Je punten blijven zeven jaar geldig,",
        tekst:
          "dus je mag er jaren over doen. Vak per vak bouw je zo je diploma op.",
      },
    ],
    slot: "Daarom werkt dit vaak goed bij hoogbegaafde en uitzonderlijk hoogbegaafde kinderen: ze kunnen sneller gaan waar het vlot loopt, en trager waar dat nodig is.",
  },
  {
    titel: "School en toch je eigen tempo",
    inleiding:
      "Hier bestaat veel verwarring over, dus even helder. Het statuut huisonderwijs kan je niet combineren met gewoon onderwijs: het is het een of het ander. Maar dat is iets anders dan de vraag of je kind thuis mag bijleren.",
    punten: [
      {
        dik: "Op school blijven en toch examens afleggen kan.",
        tekst:
          "Je kind mag naar school gaan, zelfs voltijds, en tegelijk ingeschreven zijn bij de Examencommissie.",
      },
      {
        dik: "Thuis bijleren mag altijd,",
        tekst:
          "in je eigen tempo en zover je kind wil gaan. Daar heb je niemand toestemming voor nodig.",
      },
      {
        dik: "In het secundair is een examen bij de Examencommissie een gewettigde afwezigheid,",
        tekst:
          "van rechtswege. Je kind mist die dag dus geen school zonder reden.",
      },
      {
        dik: "Een aangepast weekschema spreek je af met de directie.",
        tekst:
          "In het lager onderwijs bestaat daarvoor de afwezigheid om persoonlijke redenen, op school meestal de P-code genoemd. Met het akkoord van de directie is je kind dan gewettigd afwezig en kan het bijvoorbeeld tijdens de week naar een externe plusklas, of thuis verder werken.",
      },
      {
        dik: "Het is een afspraak en geen recht.",
        tekst:
          "Een school moet dat niet toestaan, dus het hangt af van je contact met de directie, de zorgleerkracht en de klasleerkracht. Een goed gesprek, waarin je uitlegt wat je kind nodig heeft en wat het die dagen doet, is dus de eerste stap.",
      },
    ],
    slot: "Dat is ook waarom wij zo vaak over een traject op maat spreken. Een kind kan verstandelijk ver vooruit zijn en tegelijk gewoon de leeftijd hebben die het heeft, met alles wat daarbij hoort. Dan is één vast model zelden het antwoord.",
  },
];

/* Kims eigen stuk. Zij gaf dit zelf door op 14 oktober 2026. */
export const verhaal = {
  titel: "Bij ons thuis liepen vier kinderen vier verschillende wegen",
  alineas: [
    "Ik heb vier kinderen, en geen van hen volgde dezelfde weg. Eentje ging gewoon naar school, eentje zat een tijd volledig thuis, en bij de anderen werd het iets ertussenin.",
    "Onze Mats is bijna negen en uitzonderlijk hoogbegaafd. Hij gaat nog drie halve dagen naar school, vooral voor zijn vriendjes, en legt daarnaast al examens af bij de Examencommissie. Verstandelijk staat hij ver vooruit, emotioneel is hij gewoon acht. Een traject op maat is voor hem dus niet de mooiste optie, het is de enige die werkt.",
    "Niet omdat thuis beter zou zijn dan school, of school beter dan thuis. Omdat dit is wat hij nu nodig heeft. Volgend jaar kan dat weer anders zijn, en dan passen we het weer aan.",
  ],
  naam: "Kim",
};

export const watWijDoen = {
  titel: "Wat wij hierin doen",
  alineas: [
    "Wij kiezen niet voor jou en we stellen geen diagnoses. We denken mee, we vertellen wat we zagen bij andere gezinnen, en we verwijzen je door als iemand anders je beter kan helpen.",
    "Onze externe plusklas op dinsdag is net voor dat soort weken gemaakt: een dag waarop je kind op zijn eigen niveau werkt, terwijl het de rest van de week bij zijn klasgenootjes blijft.",
    "Wie examens aflegt bij de Examencommissie, kan oefenen op ons oefenplatform. Dat volgt de officiële vakfiches hoofdstuk per hoofdstuk, dus alle onderwerpen komen aan bod. Het is een uitgebreide leidraad en geen garantie dat je slaagt: wij stellen onze eigen vragen, het examen stelt de zijne.",
  ],
};

export const bronnen = {
  tekst:
    "Waar dit op gebaseerd is, met de regels van de Vlaamse overheid zelf:",
  links: [
    {
      tekst: "Huisonderwijs voor leerplichtige kinderen",
      adres:
        "https://www.vlaanderen.be/huisonderwijs-voor-leerplichtige-kinderen",
    },
    {
      tekst: "De Examencommissie secundair onderwijs",
      adres: "https://www.vlaanderen.be/examencommissiesecundaironderwijs",
    },
    {
      tekst: "Inschrijven voor de Examencommissie secundair onderwijs",
      adres:
        "https://www.vlaanderen.be/examencommissiesecundaironderwijs/inschrijven",
    },
  ],
};
