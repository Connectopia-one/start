# -*- coding: utf-8 -*-
"""De vragen voor "De overheid in de economie" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik maak deel uit van een
economische kringloop" (20 % van het examen), het deel over de overheid. De
gezinnen en de bedrijven staan in [[se_kringloop]].

Deel 1 gaat over de inkomsten en de uitgaven van de overheid, en over hoe die
keuzes doorwerken in de samenleving. Deel 2 gaat over sociale ongelijkheid, haar
oorzaken, en over de sociale zekerheid: het solidariteitsprincipe en het
verschil tussen een aanvullende en een vervangingsuitkering.

De lijsten in dit thema komen woord voor woord uit de fiche: zes inkomsten, zes
uitgaven, zes oorzaken van sociale ongelijkheid, vier aanvullende en vier
vervangingsuitkeringen. Wie hier iets bijschrijft, houdt zich aan die lijsten,
want het examen doet dat ook.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar haalt de overheid haar geld?",
        opties=[
            "Uit belastingen die gezinnen en bedrijven betalen",
            "Uit de winst die ze maakt op wat ze zelf verkoopt",
            "Uit giften die inwoners vrijwillig komen afgeven",
            "Uit het geld dat de banken haar elk jaar schenken",
        ],
        antwoord=0,
        uitleg="Belastingen zijn de belangrijkste inkomsten van de overheid. Daarmee betaalt ze alles wat ze voor de samenleving doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn inkomsten van de overheid?",
        opties=[
            "De belasting op het gezinsinkomen",
            "De belasting op de bedrijfswinst",
            "De btw op een aankoop",
            "De huur die een gezin aan zijn eigenaar betaalt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes inkomsten: belasting op gezinsinkomen, op bedrijfswinst, btw, milieubelasting, belasting op een huis of gebouw, en wegenbelasting. Huur gaat naar een particuliere eigenaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is btw?",
        opties=[
            "Een belasting die in de prijs van je aankoop zit",
            "Een belasting die je één keer per jaar apart betaalt",
            "Een belasting die alleen bedrijven onder elkaar betalen",
            "Een belasting die je pas betaalt als je iets doorverkoopt",
        ],
        antwoord=0,
        uitleg="Btw staat voor belasting over de toegevoegde waarde. Ze zit al in de prijs die op het prijskaartje staat, dus je betaalt ze bij elke aankoop mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Op alle producten is het btw-tarief in België precies hetzelfde.",
        antwoord=False,
        uitleg="Het gewone tarief is 21 procent, maar op onder meer voeding en boeken geldt een lager tarief. Zo wordt wat iedereen nodig heeft minder zwaar belast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ouders betalen elk jaar een bedrag omdat ze een auto hebben. Welke belasting is dat?",
        opties=[
            "De wegenbelasting",
            "De btw op een aankoop",
            "De milieubelasting op afval",
            "De belasting op het gezinsinkomen",
        ],
        antwoord=0,
        uitleg="De wegenbelasting is een jaarlijkse belasting op een voertuig. De btw betaalden ze eenmalig bij de aankoop van de auto.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke belasting betaalt iemand die een huis in eigendom heeft?",
        opties=[
            "De belasting op een huis of gebouw",
            "De belasting op de bedrijfswinst",
            "De wegenbelasting van de gemeente",
            "De btw op elk gebruik van het huis",
        ],
        antwoord=0,
        uitleg="Wie een huis of gebouw bezit, betaalt daar jaarlijks belasting op. Die inkomsten gaan naar de overheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een milieubelasting is een belasting die vervuilend gedrag duurder maakt.",
        antwoord=True,
        uitleg="Klopt. De overheid gebruikt zo'n belasting niet alleen om geld op te halen, maar ook om keuzes te sturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn uitgaven van de overheid?",
        opties=[
            "Onderwijs",
            "Veiligheid",
            "Milieubescherming",
            "De aankopen van een bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes uitgaven: huisvesting en infrastructuur, milieubescherming, onderwijs, recreatie, sport en cultuur, sociale bescherming, en veiligheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid legt een nieuwe brug en vernieuwt een sociale woonwijk. Onder welke uitgave valt dat?",
        opties=[
            "Huisvesting en infrastructuur",
            "Recreatie, sport en cultuur",
            "Sociale bescherming van de inwoners",
            "Veiligheid van de inwoners",
        ],
        antwoord=0,
        uitleg="Bruggen, wegen en woningen horen bij huisvesting en infrastructuur. Dat is een van de zes uitgavenposten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Onder welke uitgave valt het geld voor de politie en de brandweer?",
        opties=[
            "Veiligheid",
            "Sociale bescherming",
            "Huisvesting en infrastructuur",
            "Recreatie, sport en cultuur",
        ],
        antwoord=0,
        uitleg="Politie, brandweer en justitie horen bij veiligheid. Zo beschermt de overheid haar inwoners.",
    ),
    dict(
        type="meerkeuze",
        vraag="Onder welke uitgave valt de subsidie voor een gemeentelijk zwembad en een bibliotheek?",
        opties=[
            "Recreatie, sport en cultuur",
            "Onderwijs voor kinderen en jongeren",
            "Veiligheid van de inwoners",
            "Milieubescherming en natuurbeheer",
        ],
        antwoord=0,
        uitleg="Een zwembad, een sporthal of een bibliotheek horen bij recreatie, sport en cultuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Het geld voor de scholen en de leerkrachten is een uitgave van de overheid.",
        antwoord=True,
        uitleg="Klopt. Onderwijs is een van de grootste uitgavenposten. Daarom is school in België grotendeels gratis.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de overheid meer uitgeeft dan ze ontvangt, blijft dat zonder gevolgen.",
        antwoord=False,
        uitleg="Dan moet ze lenen en groeit haar schuld, en op die schuld betaalt ze rente. Dat geld kan ze nadien niet meer aan iets anders besteden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk dat iedereen belastingen betaalt?",
        opties=[
            "Omdat we er samen de voorzieningen mee betalen die we allemaal gebruiken",
            "Omdat de overheid dan precies weet hoeveel elk gezin per jaar verdient",
            "Omdat er anders geen bedrijven meer zouden willen investeren",
            "Omdat de banken dan lagere rente aan de overheid vragen",
        ],
        antwoord=0,
        uitleg="Wegen, scholen, ziekenhuizen en de brandweer kosten geld. Ze zijn er voor iedereen, dus draagt iedereen bij naar wat hij kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van elke 100 euro die een overheid uitgeeft, gaat er 30 euro naar onderwijs. Hoeveel procent is dat?",
        opties=[
            "30 procent",
            "3 procent",
            "70 procent",
            "13 procent",
        ],
        antwoord=0,
        uitleg="Van elke 100 euro is 30 euro precies 30 procent. Percent betekent letterlijk per honderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente heeft 8 miljoen euro inkomsten en 9 miljoen euro uitgaven. Wat is er aan de hand?",
        opties=[
            "Ze geeft 1 miljoen euro meer uit dan ze ontvangt",
            "Ze houdt 1 miljoen euro over op het einde van het jaar",
            "Haar inkomsten en uitgaven zijn precies in evenwicht",
            "Ze heeft 17 miljoen euro nodig om alles te betalen",
        ],
        antwoord=0,
        uitleg="9 min 8 is 1. De gemeente heeft een tekort van 1 miljoen euro en moet dus lenen of besparen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de overheid beslist om minder aan openbaar vervoer te besteden, merken de inwoners daar niets van.",
        antwoord=False,
        uitleg="Minder bussen en treinen betekent langer wachten of helemaal geen verbinding. Elke keuze van de overheid werkt door in het dagelijks leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan kan je zien dat de keuzes van de overheid invloed hebben op de samenleving?",
        opties=[
            "Aan hoeveel je moet betalen voor school en openbaar vervoer",
            "Aan hoeveel fietspaden en groen er in je gemeente zijn",
            "Aan hoe lang je moet wachten op een sociale woning",
            "Aan welk merk gsm de winkels in je gemeente verkopen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Schoolkosten, fietspaden en sociale woningen hangen af van wat de overheid beslist. Welke merken een winkel verkoopt, kiest de winkel zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="De overheid is naast een speler die geld int ook een speler die zelf goederen en diensten koopt.",
        antwoord=True,
        uitleg="Klopt. Ze koopt bussen, computers en bouwwerken, en ze betaalt lonen aan haar personeel. Daarom hoort ze volwaardig in de kringloop.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de belasting die in de prijs van bijna elke aankoop zit, afgekort met drie letters?",
        antwoord=["btw", "de btw"],
        uitleg="Btw staat voor belasting over de toegevoegde waarde en zit al in de prijs die je op het prijskaartje ziet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is sociale ongelijkheid?",
        opties=[
            "Mensen hebben niet dezelfde kansen en middelen in een samenleving",
            "Mensen hebben niet dezelfde mening over hoe het land bestuurd wordt",
            "Mensen wonen niet allemaal in dezelfde streek van het land",
            "Mensen kiezen niet allemaal voor dezelfde soort opleiding",
        ],
        antwoord=0,
        uitleg="Sociale ongelijkheid gaat over verschillen in kansen, inkomen, gezondheid en macht tussen groepen mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn oorzaken van sociale ongelijkheid?",
        opties=[
            "Discriminatie",
            "Inkomen en rijkdom",
            "Onderwijs en de kansen om te leren",
            "Het weer in een bepaald jaar",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes oorzaken: discriminatie, gewoontes in een cultuur, gezondheid, inkomen en rijkdom, onderwijs en kansen om te leren, en wetten en regels van de overheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook de wetten en regels van een overheid kunnen sociale ongelijkheid veroorzaken.",
        antwoord=True,
        uitleg="Klopt. Een regel die voor iedereen gelijk lijkt, kan een groep toch treffen. Daarom staat dat uitdrukkelijk in de lijst van oorzaken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kinderen met dezelfde punten gaan naar dezelfde school. Het ene heeft thuis een rustige plek en hulp bij het huiswerk, het andere niet. Wat zie je hier?",
        opties=[
            "Sociale ongelijkheid door verschil in kansen om te leren",
            "Discriminatie door de school waar ze samen naartoe gaan",
            "Een verschil in gezondheid tussen de twee kinderen",
            "Een regel van de overheid die ongelijk uitvalt",
        ],
        antwoord=0,
        uitleg="Dezelfde school, maar niet dezelfde kansen. Het verschil zit in wat er thuis mogelijk is, en dat is een oorzaak van sociale ongelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wordt niet aangenomen voor een job omwille van zijn afkomst. Welke oorzaak van sociale ongelijkheid is dat?",
        opties=[
            "Discriminatie",
            "Gezondheid van die persoon",
            "Inkomen en rijkdom van dat gezin",
            "Wetten en regels van de overheid",
        ],
        antwoord=0,
        uitleg="Iemand anders behandelen om zijn afkomst is discriminatie. Dat is verboden en het is meteen ook een oorzaak van ongelijkheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een langdurige ziekte kan iemand in een moeilijkere positie brengen dan anderen.",
        antwoord=True,
        uitleg="Klopt. Gezondheid staat in de lijst van oorzaken: wie vaak ziek is, kan minder werken en meer kosten hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het solidariteitsprincipe van de sociale zekerheid?",
        opties=[
            "Wie kan draagt bij, wie het nodig heeft wordt geholpen",
            "Iedereen krijgt precies terug wat hij zelf betaald heeft",
            "Iedereen betaalt evenveel, ongeacht wat hij verdient",
            "Iedereen kiest zelf of hij wil bijdragen of niet",
        ],
        antwoord=0,
        uitleg="Solidariteit betekent dat de sterkste schouders dragen en dat wie het nodig heeft geholpen wordt. Je krijgt dus niet per se terug wat je betaalde.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie nooit ziek of werkloos wordt, heeft voor niets bijgedragen aan de sociale zekerheid.",
        antwoord=False,
        uitleg="Je hebt intussen wel meegedragen voor anderen, en de zekerheid dat je opgevangen wordt als het misloopt. Dat is precies wat solidariteit is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vervangingsuitkering?",
        opties=[
            "Geld dat in de plaats komt van een inkomen dat weggevallen is",
            "Geld dat bovenop een inkomen komt om kosten te helpen dragen",
            "Geld dat je moet terugbetalen zodra je weer werkt",
            "Geld dat een bedrijf aan zijn werknemers uitbetaalt",
        ],
        antwoord=0,
        uitleg="Een vervangingsuitkering vervangt een loon dat wegviel, bijvoorbeeld door ziekte, werkloosheid of pensioen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vervangingsuitkeringen?",
        opties=[
            "De werkloosheidsuitkering",
            "Het rust- en overlevingspensioen",
            "De ziekte- en invaliditeitsuitkering",
            "Het groeipakket voor kinderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Werkloosheid, pensioen, ziekte en invaliditeit, en een arbeidsongeval vervangen een weggevallen inkomen. Het groeipakket is aanvullend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een aanvullende uitkering?",
        opties=[
            "Geld dat bovenop het inkomen komt om bepaalde kosten te helpen dragen",
            "Geld dat volledig in de plaats komt van een loon dat weggevallen is",
            "Geld dat je van je werkgever krijgt bovenop je maandloon",
            "Geld dat je jaarlijks van de bank krijgt op je spaarrekening",
        ],
        antwoord=0,
        uitleg="Een aanvullende uitkering komt erbij, bijvoorbeeld het groeipakket of een tegemoetkoming voor medische kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn aanvullende uitkeringen?",
        opties=[
            "Het groeipakket",
            "De ondersteuning voor mensen met een beperking",
            "De tegemoetkoming voor medische kosten",
            "Het leefloon",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het groeipakket, ondersteuning bij een beperking, een sociaal tarief en een tegemoetkoming voor medische kosten komen bovenop een inkomen. Het leefloon vervangt er een.",
    ),
    dict(
        type="waarofniet",
        vraag="Het groeipakket is een vervangingsuitkering.",
        antwoord=False,
        uitleg="Het groeipakket is aanvullend: het komt bovenop wat een gezin verdient en helpt de kosten van kinderen dragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verliest zijn werk en krijgt maandelijks geld van de overheid tot hij nieuw werk vindt. Wat is dat?",
        opties=[
            "Een werkloosheidsuitkering, en dus een vervangingsuitkering",
            "Een sociaal tarief, en dus een aanvullende uitkering erbovenop",
            "Een groeipakket, en dus een aanvullende uitkering",
            "Een tegemoetkoming, en dus een vervangingsuitkering",
        ],
        antwoord=0,
        uitleg="Het loon viel weg en wordt vervangen. Dat is precies wat een vervangingsuitkering doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin met een laag inkomen betaalt minder voor elektriciteit dan een gezin met een hoog inkomen. Wat is dat?",
        opties=[
            "Een sociaal tarief op basis van het inkomen",
            "Een vervangingsuitkering voor dat gezin",
            "Een korting die de leverancier zelf bedacht heeft",
            "Een tegemoetkoming voor medische kosten",
        ],
        antwoord=0,
        uitleg="Een sociaal tarief is een lagere prijs voor wie een laag inkomen heeft. Het is een aanvullende maatregel van de overheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een arbeidsongeval heeft en daardoor niet kan werken, krijgt daar een uitkering voor.",
        antwoord=True,
        uitleg="Klopt, de arbeidsongevallenuitkering. Ze vervangt het loon dat wegvalt zolang je door het ongeval niet kan werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee vermindert de overheid sociale ongelijkheid?",
        opties=[
            "Met uitkeringen voor wie zijn inkomen verliest",
            "Met onderwijs dat voor iedereen toegankelijk is",
            "Met een sociaal tarief voor wie weinig verdient",
            "Met hogere prijzen in de winkels van het land",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uitkeringen, toegankelijk onderwijs en sociale tarieven duwen de verschillen kleiner. Hogere prijzen doen net het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="De sociale zekerheid wordt volledig door de overheid alleen betaald.",
        antwoord=False,
        uitleg="Van elk loon gaat er een deel naar de sociale zekerheid en de werkgever legt bij. De overheid vult aan met belastinggeld, maar betaalt niet alles.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bestaat de sociale zekerheid?",
        opties=[
            "Omdat iedereen ooit ziek, werkloos of oud kan worden",
            "Omdat de overheid haar inkomsten anders niet kwijt raakt",
            "Omdat de bedrijven hun werknemers niet willen betalen",
            "Omdat er anders te veel geld op spaarrekeningen blijft staan",
        ],
        antwoord=0,
        uitleg="Niemand weet of het hem zal overkomen. Daarom draagt iedereen bij en wordt wie het nodig heeft geholpen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we een uitkering die in de plaats komt van een weggevallen loon?",
        antwoord=["een vervangingsuitkering", "vervangingsuitkering"],
        uitleg="Een werkloosheidsuitkering, een pensioen of een ziekte-uitkering zijn vervangingsuitkeringen. Wat bovenop een inkomen komt, is aanvullend.",
    ),
]
