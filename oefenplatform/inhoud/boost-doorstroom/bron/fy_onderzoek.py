# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Veilig werken, meten en onderzoek.

Hoort bij "wetenschappelijk onderzoek en STEM" van de vakfiche fysica 2de graad
doorstroomfinaliteit, een onderdeel van 10 % en daarmee één thema.

Deel 1 gaat over veilig en duurzaam werken en over het meten: goede en slechte
werkwijzen, het meetbereik en de nauwkeurigheid van een instrument
respecteren, een multimeter als ampèremeter of voltmeter instellen, en een
meetinstrument correct aflezen. Deel 2 gaat over de onderzoeksmethode: de
stappen van probleemstelling tot conclusie, de zes criteria voor een
onderzoeksvraag (open, enkelvoudig, objectief, haalbaar, onderzoekbaar en
relevant), het ontwerpen van een oplossing en de wisselwerking tussen de
STEM-disciplines en de maatschappij.

Het doel over veilig en duurzaam werken wordt op het examen niet uitgevoerd
maar uitgelegd. De vragen hier vragen dus naar het waarom van een handeling en
naar het onderscheid tussen een goede en een slechte werkwijze.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom mag je een elektrisch toestel niet met natte handen bedienen?",
        opties=[
            "water verlaagt de weerstand van je huid",
            "water verhoogt de spanning van het toestel",
            "water maakt het toestel warmer",
            "water verlaagt de spanning van de bron",
        ],
        antwoord=0,
        uitleg="Bij dezelfde spanning loopt er door een kleinere weerstand meer stroom. Nat water maakt je huid een veel betere geleider, dus stijgt het risico op elektrocutie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet een stroom die mogelijk 2 A groot is met een multimeter. Wat doe je eerst?",
        opties=[
            "het grootste meetbereik kiezen en daarna verfijnen",
            "het kleinste meetbereik kiezen voor de grootste nauwkeurigheid",
            "de multimeter op spanning zetten",
            "de multimeter parallel aansluiten",
        ],
        antwoord=0,
        uitleg="Op een te klein bereik kan het instrument overbelast raken. Je begint ruim en gaat dan een stand fijner, tot je een goed leesbare waarde hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stand van een multimeter gebruik je om een gelijkspanning te meten?",
        opties=["DCV", "DCA", "Ω", "AC"],
        antwoord=0,
        uitleg="DCV staat voor gelijkspanning, DCA voor gelijkstroom. De Ω-stand meet een weerstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen horen bij veilig en duurzaam werken? Kruis alles aan wat juist is.",
        opties=[
            "een meetinstrument uitschakelen als je niet meet",
            "de handleiding van een toestel lezen voor je het gebruikt",
            "een toestel op een te klein meetbereik laten staan",
            "afval van een experiment bij het gewone huisvuil doen",
        ],
        antwoord=[0, 1],
        uitleg="Uitschakelen spaart de batterij en voorkomt schade, en de handleiding zegt wat het toestel aankan. Een te klein bereik maakt het instrument stuk, en chemisch afval hoort niet bij het huisvuil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lees je een maatcilinder op ooghoogte af?",
        opties=[
            "anders kijk je er schuin op en lees je verkeerd af",
            "anders kan de vloeistof over de rand lopen",
            "anders zie je de streepjes op het glas niet staan",
            "anders verdampt de vloeistof veel sneller",
        ],
        antwoord=0,
        uitleg="Kijk je van boven of van onder, dan lijkt het vloeistofpeil bij een ander streepje te staan. Die afleesfout heet parallax.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar lees je het peil van een vloeistof in een maatcilinder af?",
        opties=[
            "onderaan de holle kromming van het oppervlak",
            "bovenaan de rand van de vloeistof tegen het glas",
            "in het midden tussen de twee dichtste streepjes",
            "aan de buitenkant van het glas van de cilinder",
        ],
        antwoord=0,
        uitleg="Het oppervlak van water staat hol, dus lees je het laagste punt van die meniscus af. Zo meet iedereen op dezelfde manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil een tijdsduur van ongeveer 2 s meten. Wat kies je?",
        opties=[
            "een chronometer tot op een honderdste seconde",
            "een gewone keukenklok met een secondewijzer",
            "een zandloper die één minuut lang loopt",
            "een wandklok met enkel een minutenwijzer",
        ],
        antwoord=0,
        uitleg="Bij zo'n korte tijd telt elk honderdste mee. Met een klok die enkel seconden toont, zou je meetfout even groot zijn als de helft van je meting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het meetbereik van een instrument zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is de grootste waarde die het instrument kan meten",
            "meten boven het meetbereik kan het instrument beschadigen",
            "het is hetzelfde als de nauwkeurigheid",
            "een groter meetbereik betekent altijd een fijnere aflezing",
        ],
        antwoord=[0, 1],
        uitleg="Het meetbereik zegt hoe groot een waarde mag zijn, de nauwkeurigheid hoe fijn je kan aflezen. Een groter bereik gaat meestal juist samen met grovere streepjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat er op een dynamometer een maximale waarde?",
        opties=[
            "een grotere kracht rekt de veer blijvend uit",
            "een grotere kracht geeft een negatieve waarde",
            "boven die waarde meet hij in joule",
            "boven die waarde hoef je niet meer af te lezen",
        ],
        antwoord=0,
        uitleg="De veer werkt enkel binnen haar elastisch gebied. Rek je haar verder uit, dan komt ze niet meer op haar oude lengte terug en klopt de schaal niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet een lengte vijf keer en krijgt vijf lichtjes verschillende waarden. Wat doe je?",
        opties=[
            "het gemiddelde nemen",
            "de grootste waarde nemen",
            "de kleinste waarde nemen",
            "de eerste meting nemen en de rest weggooien",
        ],
        antwoord=0,
        uitleg="Door te herhalen en het gemiddelde te nemen, verklein je de invloed van toevallige afleesfouten. Een waarde die er helemaal naast ligt, mag je wel apart bekijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort er bij een meetresultaat altijd een eenheid?",
        opties=[
            "zonder eenheid weet je niet wat het getal betekent",
            "zonder eenheid is het getal altijd fout",
            "een eenheid maakt de meting nauwkeuriger",
            "een eenheid vervangt het aantal beduidende cijfers",
        ],
        antwoord=0,
        uitleg="Een 5 kan 5 m, 5 kg of 5 s zijn. Zonder eenheid kan je twee metingen niet vergelijken en niet verder rekenen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ampèremeter mag je nooit rechtstreeks over de polen van een bron zetten.",
        antwoord=True,
        uitleg="Een ampèremeter heeft een heel kleine weerstand, dus zou je zo een kortsluiting maken. De stroom wordt dan enorm en het toestel gaat stuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag de restvloeistof van een proef altijd in de gootsteen gieten.",
        antwoord=False,
        uitleg="Dat hangt van de stof af. Wat op het etiket of in de handleiding staat, bepaalt waar het afval naartoe moet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een instrument met fijnere streepjes is altijd het beste keuze, hoe groot de te meten waarde ook is.",
        antwoord=False,
        uitleg="Past de waarde niet binnen het meetbereik, dan kan je er niets mee meten of ga je het instrument beschadigen. Je kiest eerst op bereik, dan op nauwkeurigheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderhoudsvoorschrift van een toestel hoort bij veilig en duurzaam werken.",
        antwoord=True,
        uitleg="Een toestel dat goed onderhouden is, meet betrouwbaarder en gaat langer mee. Dat is zowel veilig als duurzaam.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werktekening of een handleiding juist kunnen lezen, hoort bij het veilig gebruiken van een technisch systeem.",
        antwoord=True,
        uitleg="Daar staat in welke grenzen het systeem aankan en in welke volgorde je moet werken. Fout lezen leidt tot schade of gevaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de afleesfout die je maakt als je schuin op een meetinstrument kijkt?",
        antwoord=["parallax", "parallaxfout", "parallaxis"],
        uitleg="Een parallaxfout. Je vermijdt die door recht van voren, op ooghoogte, af te lezen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de holle kromming van een vloeistofoppervlak in een smalle buis?",
        antwoord=["meniscus", "de meniscus"],
        uitleg="De meniscus. Bij water lees je het laagste punt ervan af.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stand van een multimeter gebruik je om een gelijkstroom te meten? Schrijf de drie letters.",
        antwoord=["DCA", "dca", "A"],
        uitleg="DCA, of soms gewoon A met een rechte lijn erbij. Voor gelijkspanning is dat DCV.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het instrument waarmee je een temperatuur meet?",
        antwoord=["thermometer", "een thermometer"],
        uitleg="Een thermometer. Je laat hem lang genoeg zitten tot hij in thermisch evenwicht is met wat je meet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap van een wetenschappelijk onderzoek?",
        opties=[
            "de probleemstelling definiëren en afbakenen",
            "de data waarnemen en verzamelen",
            "de conclusie van het onderzoek formuleren",
            "het onderzoeksplan stap voor stap uitvoeren",
        ],
        antwoord=0,
        uitleg="Pas als je weet wat je precies wil onderzoeken, kan je een onderzoeksvraag en een plan maken. Zonder afbakening wordt het onderzoek te breed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "een voorlopig antwoord dat je gaat nakijken",
            "de uitkomst van al je metingen samen",
            "de vraag die je in je onderzoek stelt",
            "de conclusie op het einde van je onderzoek",
        ],
        antwoord=0,
        uitleg="Een hypothese is een verwachting die je met je onderzoek bevestigt of verwerpt. Ze mag dus ook fout blijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderzoeksvraag is open en onderzoekbaar?",
        opties=[
            "hoe hangt de valtijd af van het aantal filters?",
            "valt een koffiefilter naar beneden als je hem loslaat?",
            "hoe groot is de valversnelling in België precies?",
            "is vallen van een hoogte gevaarlijk voor een mens?",
        ],
        antwoord=0,
        uitleg="Die vraag heeft geen ja-of-nee-antwoord en je kan ze met metingen uitzoeken. De derde is een opzoekvraag en de laatste is een mening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium enkelvoudig bij een onderzoeksvraag?",
        opties=[
            "de vraag gaat over één onderwerp",
            "de vraag heeft één woord als antwoord",
            "de vraag vraagt één meting",
            "de vraag is in één zin geschreven",
        ],
        antwoord=0,
        uitleg="Je onderzoekt één probleem per vraag. Zitten er twee in, dan weet je bij het antwoord niet meer waarover het gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium objectief bij een onderzoeksvraag?",
        opties=[
            "de vraag toont geen mening of overtuiging",
            "de vraag is door iedereen te begrijpen",
            "de vraag heeft maar één juist antwoord",
            "de vraag gaat over een meetbaar voorwerp",
        ],
        antwoord=0,
        uitleg="\"Waarom is zonne-energie de beste keuze?\" zit al vol overtuiging. \"Hoeveel energie levert een zonnepaneel per maand?\" is objectief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke criteria gelden voor een goede onderzoeksvraag? Kruis alles aan wat juist is.",
        opties=["haalbaar", "relevant", "spannend", "kort"],
        antwoord=[0, 1],
        uitleg="De zes criteria zijn open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant. Hoe spannend of hoe kort de vraag is, telt niet mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium haalbaar bij een onderzoeksvraag?",
        opties=[
            "het onderzoek is uitvoerbaar met genoeg tijd en middelen",
            "het antwoord is in elk handboek makkelijk te vinden",
            "de vraag is in één les van vijftig minuten op te lossen",
            "de vraag is door iemand anders al eerder onderzocht",
        ],
        antwoord=0,
        uitleg="Een vraag over de temperatuur in de kern van de zon kan je niet zelf meten. Een vraag over de afkoeling van water in een thermos wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het ontwerpen van een oplossing? Kruis alles aan wat juist is.",
        opties=[
            "criteria opstellen waaraan de oplossing moet voldoen",
            "het probleem in deelproblemen splitsen",
            "de eerste ingeving meteen uitvoeren",
            "de oplossing achteraf niet meer bijsturen",
        ],
        antwoord=[0, 1],
        uitleg="Je definieert eerst het probleem, zet criteria, splitst waar nodig, bedenkt oplossingen en integreert ze. Daarna evalueer je en stuur je bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vier letters van STEM?",
        opties=[
            "wetenschappen, technologie, ingenieurswetenschappen, wiskunde",
            "wetenschappen, techniek, elektriciteit en de mechanica",
            "studie, techniek, energie en de materialenkennis",
            "wetenschappen, talen, economie en de wiskunde",
        ],
        antwoord=0,
        uitleg="Science, Technology, Engineering en Mathematics. Een STEM-probleem pak je vanuit die vier disciplines samen aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt hoe snel water afkoelt in verschillende bekers. Wat houd je gelijk?",
        opties=[
            "de begintemperatuur en de hoeveelheid water",
            "het soort beker waarin het water zit",
            "de tijd waarover je de temperatuur meet",
            "de eindtemperatuur die je wil bereiken",
        ],
        antwoord=0,
        uitleg="Enkel wat je onderzoekt mag verschillen, hier het soort beker. Alle andere omstandigheden houd je gelijk, anders weet je niet waardoor het verschil komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort reflecteren over je methode bij een wetenschappelijk onderzoek?",
        opties=[
            "zo zie je welke meetfouten je resultaat verklaren",
            "zo wordt je conclusie achteraf altijd juist",
            "zo hoef je het hele onderzoek niet te herhalen",
            "zo mag je je hypothese achteraf nog aanpassen",
        ],
        antwoord=0,
        uitleg="Door terug te kijken op je werkwijze zie je waar de onzekerheid zit en hoe iemand anders het beter kan doen. Je hypothese achteraf veranderen mag juist niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die door je metingen verworpen wordt, maakt je onderzoek waardeloos.",
        antwoord=False,
        uitleg="Een verworpen hypothese is ook een resultaat: je weet nu dat het anders werkt. Dat hoort gewoon bij onderzoek doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeksvraag mag geen opzoekvraag zijn.",
        antwoord=True,
        uitleg="Kan je het antwoord gewoon in een boek vinden, dan is er geen onderzoek nodig. Dat is het criterium onderzoekbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een conclusie moet een antwoord geven op de onderzoeksvraag.",
        antwoord=True,
        uitleg="Je conclusie baseert zich op je data en sluit de cirkel met de vraag waarmee je begon. Nieuwe beweringen zonder data horen er niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het analyseren van data mag je de metingen die niet in je hypothese passen, weglaten.",
        antwoord=False,
        uitleg="Dan stuur je je eigen resultaat. Een afwijkende meting noteer je en je zoekt uit waar ze vandaan komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek is een gepast model om een verband tussen twee gemeten grootheden te laten zien.",
        antwoord=True,
        uitleg="Uit de vorm van de grafiek lees je af of het verband recht evenredig, lineair, omgekeerd evenredig of kwadratisch is. Een tabel, een schets of een formule kan ook, afhankelijk van wat je wil tonen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het voorlopige antwoord dat je voor je onderzoek opstelt?",
        antwoord=["hypothese", "een hypothese", "de hypothese"],
        uitleg="Een hypothese. Je metingen bevestigen of verwerpen die daarna.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de letter M van STEM voor? Schrijf het woord in het Nederlands.",
        antwoord=["wiskunde", "de wiskunde", "mathematics"],
        uitleg="Wiskunde, van het Engelse mathematics. De andere letters staan voor wetenschappen, technologie en ingenieurswetenschappen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het plan dat je opstelt voor je begint te meten? Schrijf het woord.",
        antwoord=["onderzoeksplan", "een onderzoeksplan", "onderzoeksopzet"],
        uitleg="Een onderzoeksplan. Daarin staat wat je gaat meten, waarmee, en wat je gelijk houdt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een vraag waarop je enkel ja of nee kan antwoorden? Schrijf het woord dat het tegengestelde is van open.",
        antwoord=["gesloten", "een gesloten vraag", "dicht"],
        uitleg="Een gesloten vraag. Een onderzoeksvraag moet juist open zijn, zodat het antwoord meer is dan ja of nee.",
    ),
]
