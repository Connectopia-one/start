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
    datum: "26 november 2026",
    titel: "Sociale en gedragswetenschappen Beyond: kies humane of welzijnswetenschappen",
    tekst:
      "Humane wetenschappen en welzijnswetenschappen hebben voor sociale en gedragswetenschappen niet helemaal dezelfde leerstof. Op de vakpagina kies je nu je richting. Voor humane wetenschappen kwam er een volledig deel politiek bij: democratie en de rechtstaat, de Belgische staat, ideologieën, partijen en verkiezingen, participatie en kiesrecht, het recht in de samenleving, en globalisering met de VN en de Europese Unie. Zes onderwerpen met telkens twee delen gewone vragen en een pittig hoofdstuk met eigen schema's om op te klikken, leer- en oefenbundels om af te drukken, en een eigen niveau in de begrippenarena. Kies je welzijnswetenschappen, dan zie je de politiek niet en blijft alles zoals je gewoon bent.",
    opVraag: true,
    link: { tekst: "Naar het vak", href: "/niveaus/beyond-doorstroom/sociale-en-gedragswetenschappen" },
  },
  {
    datum: "26 november 2026",
    titel: "Nieuw: Ready voor het 3de en 4de leerjaar",
    tekst:
      "Er is een nieuwe knop 🎒 Ready, voor kinderen van het 3de en 4de leerjaar. Bij wiskunde: getallen tot 10 000, rekenen en cijferen, tafels en delen, breuken en kommagetallen, meten en geld, tijd en temperatuur, meetkunde, en vraagstukken en tabellen. Bij Nederlands: spelling, werkwoorden, woordsoorten en zinnen, lezen en woordenschat, en taal en verhalen. Elk hoofdstuk heeft een korte uitleg, twee keer 20 vragen, een leerbundel en een oefenbundel met grote letters, hoge schrijflijnen en hokjes om letters in het woord zelf in te vullen. De voorleesknop staat bij Ready altijd aan.",
  },
  {
    datum: "26 november 2026",
    titel: "Lege omzettabellen om af te drukken",
    tekst:
      "Bij Leuke extra's, onder afdrukbare documenten, staan nu zes lege omzettabellen: lengte, inhoud, gewicht, oppervlakte, volume en een tabel voor getallen en kommagetallen. Druk ze af, lamineer ze en schrijf erop met een whiteboardstift, dan kan je ze telkens opnieuw gebruiken. De nieuwe hoofdstukken voor het 6de leerjaar hebben nu ook een leerbundel en een oefenbundel, met plaats om je tussenstappen op te schrijven.",
  },
  {
    datum: "26 november 2026",
    titel: "Start: extra hoofdstukken voor het 6de leerjaar",
    tekst:
      "We legden Start naast de nieuwe officiële minimumdoelen voor het einde van het 6de leerjaar. Wat nog ontbrak, staat nu in een extra hoofdstuk \"Nog meer voor het 6de leerjaar\" bij wiskunde, Nederlands, wetenschap en techniek, aardrijkskunde, geschiedenis en Frans, telkens 40 vragen. Bijvoorbeeld ggd en kgv, ongelijknamige breuken, bruto en netto, de mediaan, hoofdzin en bijzin, het meewerkend voorwerp, dialect en tussentaal, voortplanting, eerlijke proeven, duurzaamheid, platen en de Ring van Vuur, migratie, maanfasen, de zes periodes, Rosa Parks, de grondwet, erfgoed, de passé composé en de futur proche.",
  },
  {
    datum: "25 november 2026",
    titel: "Uitdaging van 40 vragen in Boost en Beyond",
    tekst:
      "Elk vak in Boost en Beyond, zowel doorstroom als dubbele finaliteit, heeft nu een extra hoofdstuk Uitdaging: 40 vragen die alle hoofdstukken van dat vak door elkaar halen, net als op een echt examen. Je leest teksten, tabellen en grafieken, klikt op prenten, vult tabellen in, sleept woorden op hun plaats en schrijft af en toe zelf een kort antwoord. Zo oefen je of je de hele leerstof echt beheerst.",
  },
  {
    datum: "25 november 2026",
    titel: "Pittige hoofdstukken wiskunde basis in Boost doorstroom",
    tekst:
      "Wiskunde basis in Boost doorstroom heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van reële getallen, intervallen, logica en bewijzen tot ruimtemeetkunde, gelijkvormigheid en Pythagoras, van formules, vergelijkingen en stelsels tot functies en parabolen, en van tellen tot statistiek en verbanden tussen twee grootheden. Er zijn ook klikvragen op prenten, zoals getallen op een as, een kubus, twee boxplots, een boomdiagram en vier puntenwolken.",
  },
  {
    datum: "25 november 2026",
    titel: "Pittige hoofdstukken sociale en gedragswetenschappen in Boost doorstroom",
    tekst:
      "Sociale en gedragswetenschappen in Boost doorstroom heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van de fysieke, cognitieve, morele en sociale ontwikkeling, Piaget, Kohlberg, Erikson en gehechtheid tot persoonlijkheid, zelfbeeld, emoties en motivatie, en van cultuur, socialisatie en sociale instituties tot groepen, sociale rollen en kansen in de samenleving. Er zijn ook klikvragen op prenten, zoals een levenstrap, een proefje met stokjes, een weekagenda vol rollen en een maatschappelijke ladder over twee generaties.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken kunstbeschouwing en filosofie in Boost doorstroom",
    tekst:
      "Kunstbeschouwing en filosofie in Boost doorstroom heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van kunstvormen, kunst van de prehistorie tot vandaag en de middelen van vormgeving tot de eerste Griekse filosofen, de soorten vragen, de filosofische domeinen, de AUB-methode, lichaam en geest, mens en dier, de ethische stromingen en ethische vraagstukken. Er zijn ook klikvragen op prenten, zoals een tijdlijn met filosofen, zes kaartjes met waarden en normen en een discussieblad met argumenten.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Frans in Boost doorstroom",
    tekst:
      "Frans in Boost doorstroom heeft nu bij elk van de 13 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van Franse teksten lezen, tekstverbanden en schrijven over de Franstalige wereld en de woordvelden tot lidwoorden, voornaamwoorden, de trappen van vergelijking, alle tijden en de si-zinnen. Er zijn ook klikvragen op prenten, zoals een affiche, een mail aan een camping, een weerkaart, een zwembadreglement en een zin in blokjes.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken ontwikkeling en pedagogisch handelen in Boost dubbele finaliteit",
    tekst:
      "Ontwikkeling en pedagogisch handelen in Boost dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van welzijn en gezondheid over de ontwikkeling van baby tot oudere, Piaget, Kohlberg en Erikson, tot observeren, rapporteren, communiceren, feedback, spel en activiteiten voor volwassenen. Er zijn ook klikvragen op prenten, zoals een groeicurve, een speelhoek, een observatieverslag en een dagzaal vol valrisico's.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Nederlands in Boost dubbele finaliteit",
    tekst:
      "Nederlands in Boost dubbele finaliteit heeft nu bij elk van de 12 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van communicatie, samenhang en bronnen wegen over feit en mening, stelling en argument, woordsoorten, werkwoorden, zinsdelen en spelling tot betekenis, verhalen lezen en goed communiceren. Er zijn ook klikvragen op prenten, zoals een boekenplank met fictie en non-fictie, een presentatie voor de klas en een mail voor een vakantiejob.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Nederlands in Boost doorstroom",
    tekst:
      "Nederlands in Boost doorstroom heeft nu bij elk van de 12 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van communicatie, samenhang, argumenteren en bronnen wegen over taalvariatie, woordsoorten, werkwoorden, zinsdelen en spelling tot betekenis, verhalen en poëzie. Er zijn ook klikvragen op prenten, zoals een communicatiemodel, een verdacht bericht op sociale media, zinnen in blokjes en de spanningsboog van een verhaal.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken gezondheid, zorg en welzijn in Boost dubbele finaliteit",
    tekst:
      "Gezondheid, zorg en welzijn in Boost dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van de zintuigen, spieren en het zenuwstelsel over Gordon, het ICF, eerste hulp en preventie tot voeding, voedselveiligheid, boodschappen, schoonmaken, de leefomgeving en de was. Je klikt op zelfgetekende prenten, zoals een doorsnede van de huid, een koelkast, een gedekte tafel, veiligheidstekens en een onderhoudsetiket.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Frans in Boost dubbele finaliteit",
    tekst:
      "Frans in Boost dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van lezen, tekstsoorten, de Franstalige wereld, schrijven en spreken over de woordvelden mens, dagelijks leven, school en werk, en tijd en reizen, tot lidwoorden, voornaamwoorden, bijvoeglijke naamwoorden, de tijden en de zinsbouw. Met korte Franse teksten zoals een bericht van de school, een menu, een advertentie voor vakantiewerk en een stageverslag.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken toegepaste economie in Boost dubbele finaliteit",
    tekst:
      "Toegepaste economie in Boost dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van boekhouden, de balans, het MAR, aankopen, verkopen en de btw tot boeken, de proef- en saldibalans en de eindbalans, en verder tekstverwerking, het rekenblad, functies, grafieken, afdrukken en scannen, bestanden bewaren, presenteren en de databank. Met casussen, rekenvragen en klikvragen op zelfgetekende documenten zoals een verkoopfactuur, een btw-aangifte, een bankuittreksel en een databanktabel.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken economie en bedrijfswetenschappen in Boost dubbele finaliteit",
    tekst:
      "Economie en bedrijfswetenschappen in Boost dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van behoeften, nut, productie, kosten en opbrengsten over ondernemingsvormen, organisatie en afdelingen tot werving, het arbeidscontract, schorsing, het loon, marketing, het verkoopgesprek, de documenten en logistiek. Met casussen, rekenvragen en klikvragen op grafieken en zelfgetekende documenten zoals een organogram, een vacature, een loonbrief en een vrachtbrief.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken economie in Boost doorstroom",
    tekst:
      "Economie in Boost doorstroom heeft nu bij elk van de 19 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van de kringloop, het bbp en groei over nut, budgetlijn, kosten en het optimum tot de markt, de arbeidsmarkt en handel, en verder ondernemingsvormen, balans, boekhouden, facturen, strategie en marketing. Met casussen, rekenvragen en klikvragen op zelfgetekende grafieken, een balans, een factuur en een SWOT.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Engels in Boost",
    tekst:
      "Engels in Boost doorstroom (13 onderwerpen) en in Boost dubbele finaliteit (14 onderwerpen) heeft nu bij elk onderwerp een pittig hoofdstuk van 30 vragen, in examenvorm: van tekstanalyse, tekstsoorten en schrijven over de Engelstalige wereld en woordvelden tot nouns, pronouns, adjectives, de tijden en zinsbouw. In doorstroom ook de modal verbs, in dubbele finaliteit ook spreken en klank en spelling. Met leesteksten, aanvulzinnen, sleepvragen en sorteeroefeningen.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken natuurwetenschappen in Boost dubbele finaliteit",
    tekst:
      "Natuurwetenschappen in Boost dubbele finaliteit heeft nu bij elk van de 13 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van feedback en homeostase, micro-organismen en voortplanting over mengsels, reacties en atomen tot energie, warmte, krachten, druk, elektriciteit, veilig werken en onderzoek. Met casussen, rekenvragen en klikvragen op prenten, zoals een schema van de temperatuurregeling.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken aardrijkskunde in Boost",
    tekst:
      "Aardrijkskunde in Boost doorstroom en in Boost dubbele finaliteit heeft nu bij elk van de 10 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van situeren en bevolking over stad en platteland, grondstoffen, landbouw en mondialisering tot duurzaamheid, het broeikaseffect en geografisch onderzoek. Met casussen, rekenvragen en klikvragen op prenten, zoals een gradennet, leeftijdshistogrammen en een digitale kaart.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken fysica in Boost doorstroom",
    tekst:
      "Fysica in Boost doorstroom heeft nu bij elk van de 12 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van meten en eenheden over beweging, krachten, archimedeskracht en moment tot druk, gaswetten, energie, warmte, elektriciteit, licht en lenzen en onderzoek. Met rekenvragen in stappen, casussen en klikvragen op prenten, zoals een lat met draaipunt en een bolle lens.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken chemie in Boost doorstroom",
    tekst:
      "Chemie in Boost doorstroom heeft nu bij elk van de 12 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van mengsels, atomen en het periodiek systeem over bindingen, naamgeving en organische stoffen tot reacties, pH, rekenen met de mol en veilig werken. Met rekenvragen in stappen, casussen en klikvragen op prenten.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken biologie in Boost doorstroom",
    tekst:
      "Biologie in Boost doorstroom heeft nu bij elk van de 12 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van planten, zenuwstelsel, oog en oor over spieren, klieren en voortplanting tot micro-organismen, gedrag, ecosystemen, levensreddend handelen en onderzoek. Met klikvragen op prenten, zoals een nieuwe doorsnede van het oor.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Nederlands in Beyond dubbele finaliteit",
    tekst:
      "Nederlands in Beyond dubbele finaliteit heeft nu bij elk van de 21 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van tekstsoorten, bronnen en argumentatie over verhalen, spanning en genres tot spelling, zinsbouw, betekenis, schrijven en spreken. Er zitten korte fragmenten en casussen bij.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken wiskunde in Beyond dubbele finaliteit",
    tekst:
      "Wiskunde in Beyond dubbele finaliteit heeft nu bij elk van de 12 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: problemen oplossen, machten en logaritmen, grafieken aflezen, gemiddelde verandering, exponentiële functies en groeimodellen, kansen en kansbomen, steekproeven, samenhang en causaliteit, en de normale verdeling. Er zitten casussen en klikvragen op grafieken bij.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken natuurwetenschappen in Beyond dubbele finaliteit",
    tekst:
      "Natuurwetenschappen in Beyond dubbele finaliteit heeft nu bij elk van de 14 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van embryo, vruchtbaarheid, erfelijkheid en evolutie over voeding, etiketten, dosis en duurzaamheid tot magnetisme, golven, kernfysica en onderzoekend werken. Er zitten rekenvragen, casussen en klikvragen op prenten bij.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Frans in Beyond dubbele finaliteit",
    tekst:
      "Frans in Beyond dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: lezen en tekstsoorten, schrijven en spreken, de Franstalige wereld, de woordvelden van alledag tot wetenschap, en de grammatica van de lidwoorden, voornaamwoorden, bijvoeglijke naamwoorden, de tijden en de zinsbouw. Elk hoofdstuk begint met een korte Franse tekst met vragen erbij.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Engels in Beyond dubbele finaliteit",
    tekst:
      "Engels in Beyond dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: lezen en tekstsoorten, schrijven en je mening geven, de Engelstalige wereld, de woordvelden van alledag tot wetenschap, en de grammatica van de tijden, naamwoorden, voornaamwoorden, bijvoeglijke naamwoorden en zinsbouw. Elk hoofdstuk begint met een korte Engelse tekst met vragen erbij.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken aardrijkskunde in Beyond dubbele finaliteit",
    tekst:
      "Aardrijkskunde in Beyond dubbele finaliteit heeft nu bij elk van de 16 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van situeren, het heelal en het zonnestelsel over de bewegingen van de aarde, wind, neerslag en klimaat tot de bouw van de aarde, vulkanen, gesteenten, erosie, de klimaatverandering, verstedelijking en het landschap lezen. Bij veel onderwerpen klik je op een tekening, kaart of grafiek.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken statistiek in Beyond doorstroom",
    tekst:
      "Statistiek in Beyond doorstroom heeft nu bij elk van de 18 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: telproblemen en combinaties, de binomiale en de normale verdeling, steekproeven, hypothesetoetsen, p-waarden en betrouwbaarheidsintervallen, correlatie en trendlijnen, frequentietabellen, grafieken, centrum- en spreidingsmaten, en rekenen met ICT. Bij veel onderwerpen klik je op een grafiek, zoals een klokcurve, tien betrouwbaarheidsintervallen, vier puntenwolken, twee boxplots of een rekenblad.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken sociale en gedragswetenschappen in Beyond doorstroom",
    tekst:
      "Sociale en gedragswetenschappen in Beyond doorstroom heeft nu bij elk van de 20 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: ontwikkelingspsychologie van Freud en Erikson over Piaget en Vygotsky tot Bronfenbrenner, sociaal gedrag en groepen, sociale beïnvloeding, persoonlijkheid, opvoeden, communicatie, socialisatie, ongelijkheid en mobiliteit, media, en maatschappelijke vraagstukken en de onderzoekscyclus. Bij veel onderwerpen klik je op een schema of grafiek, zoals de piramide van Maslow, de ringen van Bronfenbrenner, een ijsberg van het bewustzijn of een krantenpagina.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken samenleving en economie in Beyond doorstroom",
    tekst:
      "Samenleving en economie in Beyond doorstroom heeft nu bij elk van de 20 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: identiteit, diversiteit en omgaan met elkaar, eerste hulp en reanimatie, de overheid en de sociale zekerheid, de markt, contracten, je loon en je rechten op het werk, aankopen, budget, sparen en verzekeren, en werken met Word, Excel en PowerPoint en veilig online. Bij sommige onderwerpen klik je op een grafiek, een loonbrief, een rekenblad of een verdachte mail.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken natuurwetenschappen in Beyond doorstroom",
    tekst:
      "Natuurwetenschappen in Beyond doorstroom heeft nu bij elk van de 28 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van de cel, erfelijkheid, evolutie en afweer over reactiesnelheid, evenwicht en organische stoffen tot elektriciteit, magnetisme, bewegingen, golven, straling, veilig werken en onderzoek. Ook de zeven onderwerpen voor welzijnswetenschappen (enzymen, spijsvertering, nieren, bloed, hart, bloeddruk en ademhaling) hebben er een. Bij veel onderwerpen zijn er tekeningen en grafieken waarop je moet klikken, zoals een nefron, een hart of een spirogram.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Frans in Beyond doorstroom",
    tekst:
      "Frans in Beyond doorstroom heeft nu bij elk van de 13 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: Franse teksten lezen, tekstsoorten, cultuur en literatuur, formele en gewone mails schrijven, de woordvelden van gezondheid en wonen tot werk, reizen en milieu, en de grammatica van lidwoorden en voornaamwoorden over de verleden tijden en de subjonctif tot de indirecte rede en de passieve vorm. Bij elk onderwerp lees je ook een Franse tekst, zoals een mail, een advertentie of een krantenbericht.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Engels in Beyond doorstroom",
    tekst:
      "Engels in Beyond doorstroom heeft nu bij elk van de 14 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: Engelse teksten lezen en ontleden, tekstsoorten, de woordvelden van wonen en vrije tijd tot wetenschap en politiek, en de grammatica van lidwoorden en voornaamwoorden over alle tijden tot de indirecte rede en de passieve vorm. Bij elk onderwerp lees je ook een Engelse tekst, zoals een brief, een advertentie of een krantenbericht.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken fysica in Beyond doorstroom",
    tekst:
      "Fysica in Beyond doorstroom heeft nu bij elk van de 23 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van lading, elektrische velden, stroom en magnetisme over krachten, bewegingen, energie, gassen en warmte tot trillingen, golven, licht en geluid, kwantumfysica, kernfysica en straling, meten en onderzoek. Bij elk onderwerp zijn er tekeningen, schakelingen en grafieken waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken chemie in Beyond doorstroom",
    tekst:
      "Chemie in Beyond doorstroom heeft nu bij elk van de 23 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van stofklassen, organische stoffen en atoombouw over chemisch rekenen, reactiesnelheid en evenwicht tot zuren en basen, pH, buffers, redox, batterijen, kunststoffen, nanotechnologie, duurzame chemie, veilig werken in het labo en onderzoek. Bij elk onderwerp zijn er tekeningen en grafieken waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken biologie in Beyond doorstroom",
    tekst:
      "Biologie in Beyond doorstroom heeft nu bij elk van de 21 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van de cel, enzymen en fotosynthese over afweer, voortplanting en vruchtbaarheid tot DNA, celdeling, overerving, genexpressie, mutaties, DNA-technologie, evolutie, biomoleculen, veilig werken in het labo en onderzoek. Bij elk onderwerp zijn er tekeningen, stambomen en grafieken waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Alle bundels nu op een witte achtergrond",
    tekst:
      "De oudste leer- en oefenbundels van Start (Nederlands, Engels, aardrijkskunde, wetenschap en techniek, geschiedenis) en Spark (Nederlands, Frans, geschiedenis) hadden nog een beige achtergrond. Die zijn nu allemaal vervangen door een versie op wit papier. Zo gebruik je veel minder inkt als je ze thuis afdrukt.",
    opVraag: true,
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken aardrijkskunde in Beyond doorstroom",
    tekst:
      "Aardrijkskunde in Beyond doorstroom heeft nu bij elk van de 21 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van het heelal, de seizoenen en de maan over luchtdruk, neerslag en het weer in Europa tot platentektoniek, vulkanen, gesteenten, erosie, klimaatverandering, ruimtegebruik en het landschap lezen. Bij elk onderwerp zijn er kaarten, doorsneden en grafieken waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken natuurwetenschappen in Boost doorstroom",
    tekst:
      "Natuurwetenschappen in Boost doorstroom heeft nu bij elk van de 21 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van planten, zenuwstelsel en ecosystemen over atomen, bindingen en zuren tot krachten, druk, energie, warmte en elektriciteit, en ook eerste hulp en onderzoek. Bij elk onderwerp zijn er tekeningen en grafieken waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken Nederlands in Beyond doorstroom",
    tekst:
      "Nederlands in Beyond doorstroom heeft nu bij elk van de 21 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van tekstsoorten en argumentatie tot poëzie, stijlfiguren, zinsbouw, schrijven en spreken. Je werkt met korte teksten, gedichten en toneelfragmenten. We zetten ook een vraag over het woordje 'zich' recht: dat is een wederkerend voornaamwoord, wederkerig is 'elkaar'.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken geschiedenis in Boost en Beyond dubbele finaliteit",
    tekst:
      "Geschiedenis in Boost dubbele finaliteit heeft nu bij elk van de 11 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van Rome en de middeleeuwse stad tot de driehoekshandel, de Verlichting en het werken met bronnen. Ook Beyond dubbele finaliteit heeft er nu een bij elk van de 21 onderwerpen, van het Congres van Wenen en Congo tot China, de Koude Oorlog en beeldvorming. Met tijdlijnen, kaarten en kunstwerken waarop je moet klikken.",
    opVraag: true,
  },
  {
    datum: "24 november 2026",
    titel: "Examen: na verversen ga je verder waar je was",
    tekst:
      "Viel het internet weg tijdens een examen en moest je de pagina verversen? Dan begon je vroeger opnieuw bij vraag 1. Nu krijg je dezelfde vragen terug, met je antwoorden erbij, en ga je verder bij de vraag waar je was. Wil je toch een ander examen, klik dan op Nieuw examen.",
    opVraag: true,
  },
  {
    datum: "24 november 2026",
    titel: "Zien hoe het examen ging en wat er fout was",
    tekst:
      "Bij de voortgang van je kind staat nu een lijstje met de afgelegde examens en hun score. Klik op de fouten en je ziet per vraag wat je kind antwoordde, wat het juiste antwoord is en de uitleg. Zo kan je samen gericht verder oefenen. Van examens van voor vandaag is enkel de score bewaard.",
    opVraag: true,
    link: { tekst: "Naar mijn account", href: "/account" },
  },
  {
    datum: "24 november 2026",
    titel: "Duidelijker uitleg bij vragen met meer dan één juist antwoord",
    tekst:
      "Bovenaan sommige examens en hoofdstukken stond dat er bij de keuzevragen meer dan één antwoord juist kan zijn. Dat gold niet voor de keuzelijsten in een zin, en dat was verwarrend. Nu staat er dat het gaat over de vragen met vierkante vakjes, en dat er in een keuzelijst altijd maar één antwoord juist is.",
    opVraag: true,
  },
  {
    datum: "24 november 2026",
    titel: "Black Friday: nog tot vrijdag 24u €20, daarna €50",
    tekst:
      "Het oefenplatform is zo goed als volledig: elk vak van Start tot Beyond, met leerbundels, oefenbundels, pittige hoofdstukken en examens. Daarom gaat de prijs naar €50 per schooljaar voor het hele gezin. Tot vrijdag 27 november om 24u betaal je nog €20 voor een volledig schooljaar. Had je als dank voor de enquête en een review een vaste prijs van €20? Die blijft gewoon.",
    link: { tekst: "Volledige toegang vrijgeven", href: "/betalen" },
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken wiskunde gevorderd in Beyond",
    tekst:
      "Wiskunde in Beyond doorstroom heeft nu bij elk van de 22 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van logaritmen en afgeleiden tot integralen, complexe getallen, matrices, groepen, vectoren in de ruimte en Python. Met zelfgetekende prenten zoals grafieken, een kansboom, de driehoek van Pascal, een kubus en een stukje code waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken wiskunde in Boost doorstroom",
    tekst:
      "Wiskunde in Boost doorstroom heeft nu bij elk van de 14 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: van intervallen en Pythagoras tot vectoren, parabolen en misleidende grafieken. Met zelfgetekende prenten zoals een balk, een boxplot en puntenwolken waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken filosofie en recht in Beyond",
    tekst:
      "Filosofie en recht in Beyond doorstroom heeft nu bij elk van de 20 onderwerpen een pittig hoofdstuk van 30 vragen, in examenvorm: situaties uit het echte leven, tabellen, zinnen aanvullen en tekeningen van de rechtbanken en de rechtszaal waarop je moet klikken.",
  },
  {
    datum: "24 november 2026",
    titel: "Pittige hoofdstukken wiskunde in Boost dubbele finaliteit",
    tekst:
      "Wiskunde in Boost dubbele finaliteit heeft nu bij elk van de 13 onderwerpen een pittig hoofdstuk van 30 vragen. De vragen lijken op een echt examen: met grafieken, getallenassen en tekeningen waarop je moet klikken, tabellen invullen en vragen die samen bij één situatie horen.",
  },
  {
    datum: "24 november 2026",
    titel: "Je ziet tot wanneer je toegang loopt",
    tekst:
      "Kreeg je gratis toegang als testgezin? Op je accountpagina staat nu de juiste datum tot wanneer die loopt. En wie als dank voor de enquête en een review een vaste prijs van 20 euro kreeg, betaalt die ook echt bij een volgend schooljaar, ook als de gewone prijs stijgt.",
  },
  {
    datum: "20 november 2026",
    titel: "Zeestromen duidelijker uitgelegd",
    tekst:
      "Bij aardrijkskunde in Beyond legt de vraag over de grote oceaankringen nu uit wat 'naar rechts afbuigen' betekent: rechts gezien in de richting waarin het water stroomt, niet rechts op de kaart. Wie de kring in de Atlantische Oceaan volgt, ziet zo dat ze met de klok mee draait.",
    opVraag: true,
  },
  {
    datum: "19 november 2026",
    titel: "Een spatie te veel is geen fout meer",
    tekst:
      "Typ je het juiste woord, maar met een spatie te veel of te weinig, zoals 'verbruiks goed' in plaats van 'verbruiksgoed'? Dan telt je antwoord nu als juist, en je ziet eronder hoe je het schrijft. Bij de taalvakken blijft het fout, want daar hoort de spelling bij wat je leert. Bij vier vragen is de uitleg ook duidelijker: over de geografische breedte en lengte, over de wetenschappelijke notatie bij fysica, over 'groter dan' bij een flowchart in techniek, en over het verschil tussen het eerste kwartier en de wassende maan.",
    opVraag: true,
  },
  {
    datum: "17 november 2026",
    titel: "Bedankje bij een melding blijft weg",
    tekst:
      "Klik je het bedankje voor je melding weg met het kruisje, dan komt het niet meer terug, ook niet op een andere computer of in een andere browser. Een bedankje dat ouder is dan drie weken verdwijnt ook vanzelf.",
  },
  {
    datum: "14 november 2026",
    titel: "Duidelijkere vragen in Basis",
    tekst:
      "Bij de verleden tijd in Basis Nederlands staat er nu altijd bij wie het doet, bijvoorbeeld 'ik werk', zodat je weet of het werkte of werkten moet zijn. De vraag over 't kofschip vraagt nu naar de medeklinkers. Bij het meervoud staat er een voorbeeldwoord bij woorden op -el en -er, en in plaats van 'losse klinker' staat er nu gewoon welke letters het zijn: a, i, o of u. Bij wiskundewoorden en bij Frans stond telkens een rekenvraag die niet bij het vak hoorde: die zijn vervangen door een vraag over wiskundewoorden en een Franse vraag.",
    opVraag: true,
  },
  {
    datum: "13 november 2026",
    titel: "Twee vragen duidelijker",
    tekst:
      "Bij techniek in Spark ging een vraag over het pictogram met pijlen in een driehoek, maar er bestaan twee zulke pictogrammen. De vraag zegt nu duidelijk welk je bedoelt. Bij geschiedenis in Start telt bij de vraag over de eeuw van de industriële revolutie nu ook \"19de\" of \"negentiende\" als juist.",
    opVraag: true,
  },
  {
    datum: "13 november 2026",
    titel: "Hulp voor gezinnen uit Nederland",
    tekst:
      "Op de tipspagina staat nu een blok \"Kom je uit Nederland?\". Daarin zie je welk niveau ongeveer bij welke groep of klas past (Start is bijvoorbeeld groep 7 en 8), welke vakken goed aansluiten en welke typisch Belgisch zijn.",
    opVraag: true,
    link: { tekst: "Naar de tips", href: "/tips#nederland" },
  },
  {
    datum: "13 november 2026",
    titel: "Kan u telt als juist",
    tekst:
      "Bij Nederlands in Basis stond \"Kan u mij even helpen?\" als fout antwoord, terwijl dat in Vlaanderen gewoon goed is. Die keuze is vervangen door een zin die echt fout is.",
  },
  {
    datum: "13 november 2026",
    titel: "Pittige hoofdstukken geschiedenis in Boost",
    tekst:
      "Geschiedenis in Boost heeft nu bij elk van de elf thema's een pittig hoofdstuk met dertig vragen, in de vormen van het examen van de Examencommissie: tabellen, slepen, koppelen, klikken op een kaart of tijdlijn en vragen bij echte prenten en schilderijen. Ook de juiste antwoorden bij wiskunde in Boost en bij wiskunde in Beyond dubbele finaliteit zijn niet langer vaak het langste antwoord.",
  },
  {
    datum: "13 november 2026",
    titel: "Knop naar de begrippenarena bij elk vak",
    tekst:
      "Op de pagina van elk vak staat nu bovenaan een knop naar de begrippenarena of woordenarena die erbij hoort. Het spel opent meteen op het juiste niveau, zodat je de begrippen van dat vak spelenderwijs kan oefenen.",
  },
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
    titel: "Eerlijkere antwoordkeuzes: het langste antwoord is niet meer vanzelf juist",
    tekst:
      "Slimme kinderen merkten het snel: bij veel meerkeuzevragen was het juiste antwoord bijna altijd het langste. Dan kan je gokken zonder na te denken. We hebben in de meeste vakken de foute antwoorden herschreven, zodat ze even lang en even geloofwaardig zijn. Nu moet je echt weten wat juist is. De vragen zelf en de juiste antwoorden blijven hetzelfde.",
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
