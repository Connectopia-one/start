# -*- coding: utf-8 -*-
"""De vragen voor "Hoe een bevolking verandert" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "bevolking" (20 % van het
examen, samen met [[ak_wonen]]). Dit thema neemt het tweede stuk:
bevolkingsevolutie, demografische transitie en demografische processen.

Deel 1 gaat over de kengetallen en over het leeftijdshistogram: geboortecijfer,
sterftecijfer, natuurlijke aangroei, vruchtbaarheidscijfer, immigratie,
emigratie en migratiesaldo, en hoe je met die getallen en met een
leeftijdshistogram de structuur en de evolutie van een bevolking uitlegt.
Deel 2 gaat over de demografische transitie en de processen erachter:
vergrijzing, braindrain en braingain, migratie met push- en pullfactoren, en de
factoren die de verschillen tussen landen verklaren.

Twee afspraken die in de vragen consequent gehouden worden. Geboorte- en
sterftecijfers zijn altijd per duizend inwoners per jaar, het
vruchtbaarheidscijfer is altijd het gemiddeld aantal kinderen per vrouw. En
waar een land genoemd wordt, wordt het als voorbeeld genoemd met het cijfer
erbij in de vraag zelf, nooit als iets dat een kind uit het hoofd moet weten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarop slaat het geboortecijfer van een land?",
        opties=[
            "Het aantal geboorten per duizend inwoners per jaar",
            "Het aantal kinderen dat een vrouw gemiddeld krijgt",
            "Het aantal geboorten in dat land in één jaar tijd",
            "Het aandeel kinderen in de bevolking van dat land",
        ],
        antwoord=0,
        uitleg="Het geboortecijfer is een verhoudingsgetal per duizend inwoners, zodat je grote en kleine landen kan vergelijken. Het gemiddeld aantal kinderen per vrouw is het vruchtbaarheidscijfer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land heeft een geboortecijfer van 14 ‰ en een sterftecijfer van 9 ‰. Hoe groot is de natuurlijke aangroei?",
        opties=[
            "5 ‰",
            "23 ‰",
            "1,5 ‰",
            "0,64 ‰",
        ],
        antwoord=0,
        uitleg="Natuurlijke aangroei is het geboortecijfer min het sterftecijfer: 14 min 9 is 5 per duizend inwoners. Migratie zit daar niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="De natuurlijke aangroei van een land kan negatief zijn.",
        antwoord=True,
        uitleg="Als er meer mensen sterven dan er geboren worden, is de aangroei negatief. Dat gebeurt in verschillende Europese landen; hun bevolking krimpt dan, tenzij migratie dat opvangt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het migratiesaldo van een land?",
        opties=[
            "De immigratie min de emigratie",
            "De immigratie plus de emigratie",
            "De emigratie min de natuurlijke aangroei",
            "De immigratie gedeeld door de bevolking",
        ],
        antwoord=0,
        uitleg="Komen er meer mensen binnen dan er vertrekken, dan is het saldo positief. Vertrekken er meer dan er komen, dan is het negatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kengetallen heb je nodig om de totale bevolkingsgroei van een land te kennen? (meerdere antwoorden mogelijk)",
        opties=[
            "Het geboortecijfer van dat land",
            "Het sterftecijfer van dat land",
            "Het migratiesaldo van dat land",
            "De oppervlakte van dat land",
            "De Human Development Index van dat land",
        ],
        antwoord=[0, 1, 2],
        uitleg="Totale groei is de natuurlijke aangroei plus het migratiesaldo. Oppervlakte en HDI zeggen daar niets over, al hangt de HDI er wel mee samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land waar de natuurlijke aangroei negatief is, kan toch in bevolking groeien.",
        antwoord=True,
        uitleg="Dat kan als het migratiesaldo positief genoeg is. In verschillende West-Europese landen komt de groei vandaag bijna helemaal van migratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een vruchtbaarheidscijfer van 1,4?",
        opties=[
            "Vrouwen krijgen er gemiddeld 1,4 kinderen",
            "Er worden er 1,4 kinderen per duizend inwoners geboren",
            "1,4 procent van de bevolking is kind",
            "De bevolking groeit er met 1,4 procent per jaar",
        ],
        antwoord=0,
        uitleg="Het vruchtbaarheidscijfer is het gemiddeld aantal kinderen per vrouw. Onder ongeveer 2,1 krimpt een bevolking op termijn vanzelf, zonder migratie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we het vertrekken van inwoners uit hun eigen land?",
        antwoord=["emigratie", "de emigratie"],
        uitleg="Emigratie is vertrekken, immigratie is aankomen. Dezelfde persoon is emigrant in het land dat hij verlaat en immigrant in het land waar hij aankomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leeftijdshistogram heeft een heel brede basis en loopt snel smal toe. Wat zegt dat?",
        opties=[
            "Er zijn veel kinderen en weinig ouderen",
            "Er zijn veel ouderen en weinig kinderen",
            "De bevolking is gelijk over de leeftijden verdeeld",
            "Er wonen meer mannen dan vrouwen in dat land",
        ],
        antwoord=0,
        uitleg="De balken onderaan zijn de jongste leeftijdsgroepen. Een brede basis wijst op een hoog geboortecijfer, en het snel toelopen op een levensverwachting die nog laag ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leeftijdshistogram is bovenaan even breed als in het midden, en smaller onderaan. Wat lees je daaruit?",
        opties=[
            "De bevolking vergrijst",
            "De bevolking verjongt sterk",
            "Er is veel immigratie van kinderen",
            "Het sterftecijfer is er zeer hoog",
        ],
        antwoord=0,
        uitleg="Weinig jonge kinderen en veel ouderen: het aandeel ouderen in de bevolking stijgt. Dat is vergrijzing, en je ziet het aan de vorm van het histogram.",
    ),
    dict(
        type="waarofniet",
        vraag="Een inkeping halverwege een leeftijdshistogram kan wijzen op een oorlog of een crisis van vroeger.",
        antwoord=True,
        uitleg="Wie in zo'n periode geboren had moeten worden, ontbreekt. Die groep blijft zijn hele leven als een deuk in het histogram meeschuiven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet men een leeftijdshistogram in balken per leeftijdsgroep in plaats van per jaar?",
        opties=[
            "Zo blijft de vorm van de bevolking overzichtelijk",
            "Zo worden de cijfers per leeftijd nauwkeuriger",
            "Zo hoeft men de mannen en vrouwen niet te scheiden",
            "Zo wordt de bevolking automatisch kleiner voorgesteld",
        ],
        antwoord=0,
        uitleg="Meestal gaat het per vijf jaar. Met honderd smalle balken zie je alleen ruis, met twintig bredere zie je de vorm en dus de structuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens staan er op een gewoon leeftijdshistogram? (meerdere antwoorden mogelijk)",
        opties=[
            "De leeftijdsgroepen van de bevolking",
            "De verdeling tussen mannen en vrouwen",
            "Het aandeel of aantal per groep",
            "Het inkomen per leeftijdsgroep",
            "De woonplaats van elke groep",
        ],
        antwoord=[0, 1, 2],
        uitleg="Links de mannen, rechts de vrouwen, van jong onderaan naar oud bovenaan, met per balk een aantal of een percentage. Inkomen en woonplaats staan er niet op.",
    ),
    dict(
        type="waarofniet",
        vraag="Het sterftecijfer van een land is laag als de gezondheidszorg goed is, en dat geldt altijd.",
        antwoord=False,
        uitleg="Een land met heel veel ouderen kan een hoger sterftecijfer hebben dan een land met een jonge bevolking en slechtere zorg. Het ruwe sterftecijfer hangt dus ook van de leeftijdsstructuur af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt twee landen met een tabel van kengetallen. Wat maakt die vergelijking eerlijk?",
        opties=[
            "Dat het cijfers per duizend inwoners zijn",
            "Dat beide landen even groot zijn in oppervlakte",
            "Dat beide landen in dezelfde klimaatzone liggen",
            "Dat beide landen evenveel inwoners tellen",
        ],
        antwoord=0,
        uitleg="Juist doordat het verhoudingsgetallen zijn, kan je India met België vergelijken. Absolute aantallen zouden altijd naar het grootste land wijzen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geboortecijfer min het sterftecijfer van een land?",
        antwoord=["natuurlijke aangroei", "de natuurlijke aangroei"],
        uitleg="De natuurlijke aangroei telt alleen geboorten en sterften mee. Wil je de totale groei, dan tel je het migratiesaldo erbij.",
    ),
    dict(
        type="waarofniet",
        vraag="Immigratie verandert niets aan de vorm van een leeftijdshistogram.",
        antwoord=False,
        uitleg="Wie migreert is vaak jongvolwassen. Een land met veel immigratie krijgt daardoor bredere balken rond de twintig tot veertig jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een land daalt het geboortecijfer al twintig jaar en stijgt de levensverwachting. Wat verwacht je over twintig jaar?",
        opties=[
            "Een groter aandeel ouderen in de bevolking",
            "Een groter aandeel kinderen in de bevolking",
            "Een gelijkblijvende leeftijdsstructuur",
            "Een snel stijgend sterftecijfer bij jongeren",
        ],
        antwoord=0,
        uitleg="Minder geboorten onderaan en mensen die langer leven bovenaan: samen tilt dat het aandeel ouderen omhoog. Dat is precies wat vergrijzing is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beïnvloedende factoren kunnen het geboortecijfer van een land laag houden? (meerdere antwoorden mogelijk)",
        opties=[
            "Vrouwen die lang naar school gaan en werken",
            "Een geboortebeleid dat grote gezinnen ontmoedigt",
            "Hoge kosten voor huisvesting en kinderopvang",
            "Een hoge kindersterfte in dat land",
            "Een groot aandeel landbouw in de economie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onderwijs, beleid en kosten drukken het geboortecijfer. Hoge kindersterfte en een landbouweconomie duwen het juist omhoog, want dan zijn kinderen handen op het veld en een zekerheid voor later.",
    ),
    dict(
        type="waarofniet",
        vraag="Het migratiesaldo van de hele wereld samen is nul.",
        antwoord=True,
        uitleg="Wie ergens vertrekt, komt elders aan. Wereldwijd heffen immigratie en emigratie elkaar dus op; alleen per land is er een saldo.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat beschrijft het model van de demografische transitie?",
        opties=[
            "Hoe geboorte- en sterftecijfer van een land in fasen veranderen",
            "Hoe mensen zich binnen een land van dorp naar stad verplaatsen",
            "Hoe de bevolkingsdichtheid over de wereld verdeeld is",
            "Hoe de ontwikkelingsgraad van landen gemeten wordt",
        ],
        antwoord=0,
        uitleg="Het model zet het verloop van beide cijfers naast elkaar in een aantal fasen. Het is een model: echte landen volgen het niet perfect, maar het maakt vergelijken mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke fase van de demografische transitie zijn zowel het geboortecijfer als het sterftecijfer hoog en groeit de bevolking nauwelijks?",
        opties=[
            "De eerste fase",
            "De tweede fase",
            "De derde fase",
            "De vierde fase",
        ],
        antwoord=0,
        uitleg="In de eerste fase worden er veel kinderen geboren, maar sterven er ook veel mensen. De twee cijfers liggen dicht bij elkaar, dus blijft de bevolking ongeveer gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom groeit de bevolking het snelst in de tweede fase van de transitie?",
        opties=[
            "Het sterftecijfer daalt terwijl het geboortecijfer hoog blijft",
            "Het geboortecijfer stijgt terwijl het sterftecijfer gelijk blijft",
            "Beide cijfers dalen, maar het sterftecijfer daalt trager",
            "Beide cijfers stijgen, maar het geboortecijfer stijgt sneller",
        ],
        antwoord=0,
        uitleg="Betere voeding, drinkwater en gezondheidszorg doen de sterfte snel zakken. Gewoonten rond kinderen krijgen veranderen veel trager, dus loopt het gat tussen beide cijfers wijd open.",
    ),
    dict(
        type="waarofniet",
        vraag="In de vierde fase van de demografische transitie liggen geboorte- en sterftecijfer allebei laag.",
        antwoord=True,
        uitleg="De bevolking groeit dan weer traag, maar met een heel andere structuur dan in de eerste fase: veel meer ouderen en veel minder kinderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land heeft een geboortecijfer van 34 ‰ en een sterftecijfer van 9 ‰. In welke fase zit het waarschijnlijk?",
        opties=[
            "De tweede fase",
            "De eerste fase",
            "De vierde fase",
            "Na de vierde fase",
        ],
        antwoord=0,
        uitleg="De sterfte is al sterk gedaald maar de geboorten nog niet: dat is precies het beeld van de tweede fase, met een natuurlijke aangroei van 25 per duizend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent vergrijzing?",
        opties=[
            "Het aandeel ouderen in de bevolking neemt toe",
            "Het aantal inwoners van een land neemt af",
            "Het aantal geboorten per vrouw neemt toe",
            "Het aandeel mensen in de stad neemt toe",
        ],
        antwoord=0,
        uitleg="Vergrijzing gaat over de verhouding, niet over het totaal. Ze komt van een dalend geboortecijfer en een stijgende levensverwachting samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen heeft sterke vergrijzing voor een land? (meerdere antwoorden mogelijk)",
        opties=[
            "Meer uitgaven aan pensioenen",
            "Meer vraag naar zorg voor ouderen",
            "Minder mensen op de arbeidsmarkt",
            "Een sterk stijgend geboortecijfer",
            "Een groeiend tekort aan scholen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meer ouderen en minder werkenden zetten pensioenen, zorg en arbeidsmarkt onder druk. Scholen komen juist leeg te staan, en het geboortecijfer stijgt er niet vanzelf van.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het vertrek van hoogopgeleide mensen uit een land naar het buitenland?",
        antwoord=["braindrain", "brain drain"],
        uitleg="Braindrain betekent letterlijk het wegvloeien van hersenen. Het land dat die mensen ontvangt, spreekt van braingain.",
    ),
    dict(
        type="waarofniet",
        vraag="Braindrain is voor het land van vertrek vooral een voordeel, want er zijn minder monden te voeden.",
        antwoord=False,
        uitleg="Het land verliest net de artsen, ingenieurs en leerkrachten die het zelf heeft opgeleid en die het hard nodig heeft. Wat er soms tegenover staat, is het geld dat die mensen naar huis sturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn pushfactoren bij migratie?",
        opties=[
            "Redenen om te vertrekken uit het eigen gebied",
            "Redenen om ergens anders naartoe te trekken",
            "De kosten van de reis naar het nieuwe land",
            "De regels die een land aan nieuwkomers stelt",
        ],
        antwoord=0,
        uitleg="Push duwt je weg: oorlog, armoede, droogte, werkloosheid, vervolging. Pull trekt je aan: werk, veiligheid, onderwijs, familie die er al woont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn pullfactoren? (meerdere antwoorden mogelijk)",
        opties=[
            "Kans op werk in het land van aankomst",
            "Familie die daar al enkele jaren woont",
            "Goed onderwijs voor de kinderen daar",
            "Aanhoudende droogte in het eigen gebied",
            "Een gewapend conflict in de eigen streek",
        ],
        antwoord=[0, 1, 2],
        uitleg="Werk, familie en onderwijs trekken mensen naar een plaats toe. Droogte en oorlog duwen mensen weg en zijn dus pushfactoren.",
    ),
    dict(
        type="waarofniet",
        vraag="De meeste mensen die migreren, blijven binnen hun eigen wereldregio.",
        antwoord=True,
        uitleg="Wie vlucht, komt meestal in een buurland terecht: de reis is korter, de taal vaak dichterbij en er wonen al bekenden. Migratie over grote afstand is de uitzondering, niet de regel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren verklaren waarom demografische processen tussen landen verschillen? (meerdere antwoorden mogelijk)",
        opties=[
            "De welvaart en het welzijn in het land",
            "De politieke en de oorlogssituatie",
            "Het geboortebeleid van de overheid",
            "De geografische lengte van het land",
            "De kleur op de kaart in de atlas",
        ],
        antwoord=[0, 1, 2],
        uitleg="Welvaart, politiek en beleid grijpen rechtstreeks in op geboorten, sterfte en migratie. Daarnaast spelen ook klimaat, reliëf, bodemkwaliteit en armoede mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land voerde jarenlang een beleid dat gezinnen tot één kind beperkte. Wat verwacht je nu in het leeftijdshistogram?",
        opties=[
            "Smalle balken bij de leeftijdsgroepen uit die periode",
            "Brede balken bij de leeftijdsgroepen uit die periode",
            "Een histogram dat bovenaan smaller is geworden",
            "Een histogram dat over alle leeftijden gelijk is",
        ],
        antwoord=0,
        uitleg="Wie toen niet geboren werd, ontbreekt nu in die leeftijdsgroepen. Dat gat schuift jaar na jaar mee omhoog en zorgt later voor snelle vergrijzing.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie door droogte of overstroming wegtrekt, steekt meestal meteen een oceaan over.",
        antwoord=False,
        uitleg="Klimaat is wel degelijk een pushfactor, maar de meeste mensen verhuizen eerst binnen hun eigen land, vaak van het platteland naar de stad. Een verre reis kost geld dat ze net niet hebben.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de aankomst van hoogopgeleide mensen in een land, het omgekeerde van braindrain?",
        antwoord=["braingain", "brain gain"],
        uitleg="Braingain is de winst van het ontvangende land: het krijgt kennis binnen waarvoor het de opleiding niet betaald heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom volgt niet elk land de demografische transitie op dezelfde manier?",
        opties=[
            "Beleid, oorlog, welvaart en cultuur verlopen overal anders",
            "Het model geldt alleen voor landen op het noordelijk halfrond",
            "Het model geldt alleen voor landen met een hoge HDI",
            "Het model werd opgesteld voordat er cijfers bestonden",
        ],
        antwoord=0,
        uitleg="Het model is een samenvatting van wat in West-Europa gebeurde. Elders ging de daling van de sterfte veel sneller, of hield beleid of oorlog het verloop tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom daalt het sterftecijfer meestal vóór het geboortecijfer?",
        opties=[
            "Betere zorg werkt sneller dan gewoonten veranderen",
            "Het geboortecijfer kan pas dalen als de bevolking krimpt",
            "Artsen meten eerst de sterfte en pas later de geboorten",
            "Het geboortecijfer daalt alleen door een overheidsbeleid",
        ],
        antwoord=0,
        uitleg="Schoon drinkwater, inentingen en betere voeding redden meteen levens. Hoeveel kinderen mensen willen, hangt vast aan onderwijs, werk en zekerheid, en dat verandert over generaties.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land in de vierde fase van de transitie heeft dezelfde leeftijdsstructuur als een land in de eerste fase.",
        antwoord=False,
        uitleg="In beide fasen groeit de bevolking traag, maar de vorm verschilt volledig: in de eerste fase veel kinderen en weinig ouderen, in de vierde fase net omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land heeft een negatief migratiesaldo en veel vertrek van jonge, opgeleide mensen. Welke gevolgen verwacht je?",
        opties=[
            "De bevolking veroudert en er verdwijnt kennis uit het land",
            "De bevolking verjongt en de arbeidsmarkt wordt krapper",
            "De bevolkingsdichtheid stijgt en de HDI stijgt mee",
            "Het geboortecijfer stijgt en de vergrijzing neemt af",
        ],
        antwoord=0,
        uitleg="Wie vertrekt is meestal jong en opgeleid. De achterblijvende bevolking wordt dus gemiddeld ouder, en het land verliest mensen die het net nodig heeft.",
    ),
]
