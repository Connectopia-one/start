# -*- coding: utf-8 -*-
"""De vragen voor "Waar wonen de mensen?" (🚀 Boost doorstroom, aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "bevolking" (20 % van het
examen, samen met [[ak_bevolking]]). Dit thema neemt het eerste stuk:
bevolkingsdichtheid en ontwikkelingsgraad.

Deel 1 gaat over de bevolkingsdichtheid: wat ze is, hoe je ze van een
thematische kaart of een tabel afleest, en hoe het klimaat, de bodemkwaliteit
en het reliëf ze beïnvloeden.
Deel 2 gaat over de ontwikkelingsgraad en de Human Development Index: waaruit
die is opgebouwd, hoe je hem afleest, en waarom hij tussen landen verschilt.

Bewust vermeden: exacte HDI-waarden en exacte dichtheden van landen. Die
veranderen elk jaar, en de fiche vraagt ze van de bronnen af te lezen, niet uit
het hoofd te kennen. Waar er toch een getal in staat, staat het in de bron van
de vraag zelf, zodat de vraag blijft kloppen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we precies met de bevolkingsdichtheid van een gebied?",
        opties=[
            "Het aantal inwoners per vierkante kilometer",
            "Het totale aantal inwoners van dat gebied",
            "Het aantal geboorten per duizend inwoners",
            "Het aandeel inwoners dat in een stad woont",
        ],
        antwoord=0,
        uitleg="Dichtheid zet het aantal mensen af tegen de oppervlakte. Daardoor kan een klein land met weinig inwoners toch dichter bevolkt zijn dan een groot land met veel inwoners.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land telt 12 miljoen inwoners op 30 000 km². Hoe groot is de bevolkingsdichtheid ongeveer?",
        opties=[
            "400 inwoners per km²",
            "40 inwoners per km²",
            "4 000 inwoners per km²",
            "2 500 inwoners per km²",
        ],
        antwoord=0,
        uitleg="Je deelt het aantal inwoners door de oppervlakte: 12 000 000 gedeeld door 30 000 is 400. Dat is ruwweg de orde van grootte van België.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land met veel inwoners heeft daarom nog geen hoge bevolkingsdichtheid.",
        antwoord=True,
        uitleg="Canada telt tientallen miljoenen inwoners maar is enorm groot, dus de dichtheid blijft er laag. Het gaat om de verhouding, niet om het totaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een thematische kaart van de bevolkingsdichtheid staan donkere en lichte kleuren. Wat doe je eerst?",
        opties=[
            "De legende lezen om te weten welke klasse welke kleur is",
            "De donkerste gebieden meteen als steden aanduiden",
            "De kleuren vergelijken met een andere kaart in de atlas",
            "De schaal van de kaart omrekenen naar kilometers",
        ],
        antwoord=0,
        uitleg="Zonder legende weet je niet of donker veel of weinig betekent, en al helemaal niet welke aantallen bij welke klasse horen. Kaartmakers kiezen die klassen zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fysische factoren maken dat een gebied dunbevolkt blijft? (meerdere antwoorden mogelijk)",
        opties=[
            "Een klimaat dat het grootste deel van het jaar te droog is",
            "Een bodem waarin bijna niets wil groeien",
            "Een reliëf met steile hellingen en grote hoogte",
            "Een ligging vlak bij een grote bevaarbare rivier",
            "Een vlakke kuststrook met een gematigd klimaat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Droogte, een arme bodem en ruw reliëf maken landbouw en bouwen moeilijk, dus blijven er weinig mensen wonen. Een rivier en een vlakke kust trekken mensen juist aan.",
    ),
    dict(
        type="waarofniet",
        vraag="De Sahara is dunbevolkt vooral omdat er te weinig neerslag valt.",
        antwoord=True,
        uitleg="Zonder water lukt landbouw niet en is drinkwater een probleem. Waar in de woestijn wél water is, in een oase of langs de Nijl, wonen wél veel mensen dicht op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wonen er in de Nijlvallei zoveel mensen op een smalle strook?",
        opties=[
            "Alleen daar is er water en vruchtbare grond",
            "Alleen daar is het reliëf er bergachtig genoeg",
            "Alleen daar valt er in dat land voldoende regen",
            "Alleen daar loopt er een grens met een buurland",
        ],
        antwoord=0,
        uitleg="De rivier brengt water en vroeger ook slib, waardoor je er kan telen. Daarbuiten ligt woestijn, dus de bevolking drukt zich samen langs het water.",
    ),
    dict(
        type="meerkeuze",
        vraag="In Nederland en in Vlaanderen is de dichtheid hoog. Welke factoren spelen daarin mee? (meerdere antwoorden mogelijk)",
        opties=[
            "Een vlak reliëf waarop makkelijk gebouwd kan worden",
            "Een gematigd klimaat zonder extreme droogte of kou",
            "Een vruchtbare bodem en goede verbindingen over water",
            "Een ligging ver van elke haven of bevaarbare rivier",
            "Een bodem die grotendeels uit kaal rotsgesteente bestaat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vlak land, een zacht klimaat, goede grond en water om over te varen: dat zijn samen sterke redenen om er te gaan wonen. De twee laatste opties beschrijven juist het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="Met welke eenheid drukken we de bevolkingsdichtheid uit? Vul aan: inwoners per ...",
        antwoord=["vierkante kilometer", "km²", "km2"],
        uitleg="Bevolkingsdichtheid is altijd inwoners per vierkante kilometer. Bij steden zie je soms inwoners per hectare, maar op kaarten van landen is het de vierkante kilometer.",
    ),
    dict(
        type="waarofniet",
        vraag="Reliëf speelt geen rol meer bij waar mensen wonen, omdat we tegenwoordig overal kunnen bouwen.",
        antwoord=False,
        uitleg="Technisch kan er veel, maar bouwen en aanleggen in de bergen kost veel meer. Daarom liggen ook vandaag de meeste steden in vlakke gebieden en in dalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee gebieden hebben dezelfde bevolkingsdichtheid, maar in het ene wonen alle mensen in drie steden en in het andere overal verspreid. Wat besluit je?",
        opties=[
            "Een gemiddelde dichtheid verbergt hoe mensen echt verspreid zitten",
            "De dichtheid van een van de twee gebieden is verkeerd berekend",
            "Het gebied met de drie steden heeft een hogere dichtheid",
            "Beide gebieden hebben evenveel inwoners in totaal wonen",
        ],
        antwoord=0,
        uitleg="Dichtheid is een gemiddelde over de hele oppervlakte. Dat is handig om landen te vergelijken, maar het zegt niets over het patroon binnen dat land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een tabel met per land het aantal inwoners en de oppervlakte. Wat kan je daaruit zelf berekenen?",
        opties=[
            "De bevolkingsdichtheid van elk land",
            "Het geboortecijfer van elk van die landen",
            "De Human Development Index van elk land",
            "Het migratiesaldo van elk van die landen",
        ],
        antwoord=0,
        uitleg="Inwoners gedeeld door oppervlakte geeft de dichtheid. Voor een geboortecijfer, een HDI of een migratiesaldo heb je heel andere gegevens nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaat, bodemkwaliteit en reliëf verklaren samen een groot deel van het wereldwijde bevolkingspatroon.",
        antwoord=True,
        uitleg="De dichtbevolkte gebieden liggen bijna allemaal waar water, grond en reliëf meezitten. Toch is het nooit de hele verklaring: geschiedenis, economie en politiek spelen ook mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het noorden van Canada zo dunbevolkt?",
        opties=[
            "Het is er lang koud en de grond is er weinig bruikbaar",
            "Het land is er te bergachtig om iets te kunnen bouwen",
            "Er is er te weinig zoet water om mensen te laten wonen",
            "De regering laat er niemand toe om er te gaan wonen",
        ],
        antwoord=0,
        uitleg="In de toendra is de bodem een groot deel van het jaar bevroren en groeit er nauwelijks iets. Water is er genoeg, en het reliëf is er op veel plaatsen zelfs vlak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over dichtbevolkte gebieden in de wereld klopt?",
        opties=[
            "Ze liggen vaak in rivierdalen, delta's en langs kusten",
            "Ze liggen vaak in hooggebergte boven de boomgrens",
            "Ze liggen vaak midden in de grote woestijngordels",
            "Ze liggen vaak in de poolstreken rond de poolcirkel",
        ],
        antwoord=0,
        uitleg="Water, vruchtbaar slib en transport over zee of rivier trekken mensen aan. Dat zie je aan de Ganges, de Nijl, de Rijn en langs de Chinese oostkust.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de vruchtbare vlakte die een rivier afzet waar ze in zee uitmondt?",
        antwoord=["delta", "een delta", "de delta"],
        uitleg="In een delta zet de rivier haar slib af. Die grond is heel vruchtbaar, en daarom zijn delta's zoals die van de Ganges en de Nijl vaak dichtbevolkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gebied met een hoge bevolkingsdichtheid is daarom ook een rijk gebied.",
        antwoord=False,
        uitleg="Dichtheid zegt hoeveel mensen er per vierkante kilometer wonen, niets over hun welvaart. Monaco en Bangladesh zijn allebei dichtbevolkt en verschillen enorm in inkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een kaart valt op dat de bevolking van Egypte in een smalle lijn ligt. Hoe noem je zo'n verspreiding?",
        opties=[
            "Een patroon",
            "Een proces",
            "Een schaal",
            "Een legende",
        ],
        antwoord=0,
        uitleg="Een patroon toont de verspreiding van iets in de ruimte. Een proces gaat over verandering, zoals de bevolkingsevolutie of de klimaatverandering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens heb je nodig om de dichtheid van twee provincies eerlijk te vergelijken? (meerdere antwoorden mogelijk)",
        opties=[
            "Het aantal inwoners van elke provincie",
            "De oppervlakte van elke provincie",
            "De hoofdstad van elke provincie apart",
            "Het aantal gemeenten in elke provincie",
            "De kleur die elke provincie op de kaart heeft",
        ],
        antwoord=[0, 1],
        uitleg="Dichtheid heeft precies twee gegevens nodig: inwoners en oppervlakte. Het aantal gemeenten of de hoofdstad verandert daar niets aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bodemkwaliteit heeft invloed op de bevolkingsdichtheid omdat ze bepaalt hoeveel voedsel er lokaal geteeld kan worden.",
        antwoord=True,
        uitleg="Waar de grond goed is, kan een streek meer mensen voeden. Dat verband is minder strak geworden sinds voedsel over de hele wereld verhandeld wordt, maar het is niet verdwenen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting HDI?",
        opties=[
            "Human Development Index",
            "Human Density Indicator",
            "Household Development Income",
            "Human Data Information",
        ],
        antwoord=0,
        uitleg="De Human Development Index of index van de menselijke ontwikkeling wordt door de Verenigde Naties berekend om landen te vergelijken op meer dan alleen geld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zaken zitten samen in de HDI verwerkt? (meerdere antwoorden mogelijk)",
        opties=[
            "Hoe lang mensen er gemiddeld leven",
            "Hoeveel jaar mensen er naar school gaan",
            "Hoeveel een inwoner er gemiddeld verdient",
            "Hoeveel inwoners er per vierkante kilometer wonen",
            "Hoeveel toeristen het land jaarlijks ontvangt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De HDI combineert gezondheid, onderwijs en inkomen tot één getal. Bevolkingsdichtheid en toerisme zitten er niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="De HDI van een land is een getal tussen 0 en 1.",
        antwoord=True,
        uitleg="Hoe dichter bij 1, hoe hoger de ontwikkelingsgraad. Omdat het een verhoudingsgetal is, kan je er landen van heel verschillende grootte mee vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de HDI een betere maat voor ontwikkeling dan alleen het inkomen per inwoner?",
        opties=[
            "Hij kijkt ook naar gezondheid en naar onderwijs",
            "Hij wordt elk jaar opnieuw berekend door de VN",
            "Hij houdt rekening met de oppervlakte van het land",
            "Hij wordt in dollars en niet in euro's uitgedrukt",
        ],
        antwoord=0,
        uitleg="Een land kan rijk zijn aan olie en toch weinig scholen en ziekenhuizen hebben. Door levensverwachting en onderwijs mee te tellen, komt dat verschil boven water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Land A heeft een HDI van 0,92, land B een HDI van 0,48. Wat mag je daaruit besluiten?",
        opties=[
            "In land A leven mensen gemiddeld langer en gaan ze langer naar school",
            "In land A wonen meer mensen dan in land B in totaal",
            "In land A is de bevolkingsdichtheid hoger dan in land B",
            "In land A groeit de bevolking sneller dan in land B",
        ],
        antwoord=0,
        uitleg="De HDI zegt iets over gezondheid, onderwijs en inkomen samen. Over het aantal inwoners of de groei van de bevolking zegt hij op zich niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee landen met dezelfde HDI hebben daarom ook precies dezelfde levensverwachting.",
        antwoord=False,
        uitleg="De HDI is een samengesteld getal. Het ene land kan hoger scoren op onderwijs en lager op gezondheid dan het andere, en toch op hetzelfde eindcijfer uitkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verschilt de ontwikkelingsgraad zo sterk tussen landen?",
        opties=[
            "Er spelen samen historische, politieke en economische oorzaken",
            "Het hangt bijna volledig af van het klimaat van het land",
            "Het hangt bijna volledig af van de oppervlakte van het land",
            "Het verschil komt haast alleen door het aantal inwoners",
        ],
        antwoord=0,
        uitleg="Kolonisatie, oorlog, bestuur, schulden, grondstoffen en onderwijsbeleid grijpen in elkaar. Eén enkele oorzaak aanwijzen klopt zelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke omstandigheden kunnen de HDI van een land doen dalen? (meerdere antwoorden mogelijk)",
        opties=[
            "Een langdurige oorlog op het grondgebied",
            "Scholen die jarenlang gesloten blijven",
            "Een epidemie die de levensverwachting verlaagt",
            "Een groei van het aantal inwoners van het land",
            "Een uitbreiding van het spoorwegnet van het land",
        ],
        antwoord=[0, 1, 2],
        uitleg="Oorlog, gesloten scholen en een epidemie raken rechtstreeks gezondheid, onderwijs en inkomen. Meer inwoners of meer sporen doen de HDI op zich niet dalen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke organisatie berekent en publiceert elk jaar de Human Development Index?",
        antwoord=["de verenigde naties", "verenigde naties", "vn"],
        uitleg="De Verenigde Naties publiceren de HDI in hun ontwikkelingsrapport. Daardoor worden alle landen op dezelfde manier gemeten en zijn ze onderling vergelijkbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Binnen één land kan de ontwikkelingsgraad sterk verschillen tussen streken.",
        antwoord=True,
        uitleg="Een nationale HDI is een gemiddelde. In veel landen scoort de hoofdstad veel hoger dan het platteland, en dat verschil verdwijnt in dat ene cijfer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een wereldkaart van de HDI valt een duidelijk patroon op. Welk?",
        opties=[
            "De hoogste waarden liggen samen in bepaalde wereldregio's",
            "De hoogste waarden liggen verspreid volgens de meridianen",
            "De hoogste waarden liggen altijd vlak bij de evenaar",
            "De hoogste waarden wisselen willekeurig van land tot land",
        ],
        antwoord=0,
        uitleg="Hoge waarden liggen vooral in West-Europa, Noord-Amerika, Oost-Azië en Oceanië, de laagste vooral in Centraal- en West-Afrika. Zo'n verspreiding is een patroon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel geeft per land de levensverwachting, de scholingsduur en het inkomen. Wat kan je daarmee?",
        opties=[
            "De landen rangschikken op ontwikkelingsgraad",
            "De bevolkingsdichtheid van de landen berekenen",
            "Het migratiesaldo van de landen bepalen",
            "De klimaatzone van de landen afleiden",
        ],
        antwoord=0,
        uitleg="Dat zijn precies de drie bouwstenen van de HDI. Voor dichtheid, migratie of klimaat heb je heel andere gegevens nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="De HDI meet ook hoe gelijk de welvaart binnen een land verdeeld is.",
        antwoord=False,
        uitleg="De gewone HDI werkt met gemiddelden en ziet ongelijkheid niet. Daarvoor bestaat een aparte versie die voor ongelijkheid corrigeert, en die ligt bijna altijd lager.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet men de HDI op een kaart in plaats van alleen in een tabel?",
        opties=[
            "Op een kaart zie je meteen waar de verschillen liggen",
            "Op een kaart zijn de cijfers nauwkeuriger dan in een tabel",
            "Op een kaart staan er meer landen dan in een tabel",
            "Op een kaart hoef je de legende niet meer te lezen",
        ],
        antwoord=0,
        uitleg="Een kaart maakt van een lijst getallen een ruimtelijk beeld, en dan springen de patronen in het oog. Nauwkeuriger worden de cijfers er niet van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over rijkdom en ontwikkeling klopt?",
        opties=[
            "Een land met veel grondstoffen is daarom nog niet hoog ontwikkeld",
            "Een land met veel grondstoffen heeft altijd een hoge HDI",
            "Een land zonder grondstoffen kan nooit een hoge HDI halen",
            "Grondstoffen en ontwikkelingsgraad hebben niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg="Wat een land met zijn inkomsten doet, telt evenveel als wat het in de grond heeft. Japan en Zuid-Korea hebben weinig grondstoffen en toch een hoge HDI.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord het niveau van welvaart, gezondheid en onderwijs in een land, dat de HDI probeert te meten?",
        antwoord=["ontwikkelingsgraad", "de ontwikkelingsgraad"],
        uitleg="De ontwikkelingsgraad vat samen hoe goed het met de mensen in een land gaat. De HDI is de index waarmee de VN dat in één getal vangt.",
    ),
    dict(
        type="waarofniet",
        vraag="De HDI van een land kan door de jaren heen stijgen en dalen.",
        antwoord=True,
        uitleg="Hij wordt jaarlijks herberekend. Door oorlog of een epidemie kan hij dalen, door beter onderwijs en gezondheidszorg stijgt hij over langere tijd meestal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen ontwikkelingsgraad en bevolkingsdichtheid?",
        opties=[
            "Er is geen vast verband tussen die twee",
            "Een hogere dichtheid geeft altijd een hogere HDI",
            "Een hogere dichtheid geeft altijd een lagere HDI",
            "De dichtheid wordt in de HDI meegerekend",
        ],
        antwoord=0,
        uitleg="Nederland is dichtbevolkt met een hoge HDI, Niger is dunbevolkt met een lage. Omgekeerd bestaat evengoed. De twee meten verschillende dingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet bij een bron over de HDI kritisch nakijken. Waarop let je? (meerdere antwoorden mogelijk)",
        opties=[
            "Van welk jaar de cijfers zijn",
            "Wie de cijfers verzameld heeft",
            "Welke klassen de legende gebruikt",
            "Welke kleur het mooist staat op de kaart",
            "Hoe groot de kaart is afgedrukt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Jaartal, bron en klassenindeling bepalen samen wat je uit de kaart mag besluiten. Door de klassen anders te kiezen ziet dezelfde kaart er heel anders uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land met een lage HDI is een land waar niemand rijk is.",
        antwoord=False,
        uitleg="Een lage HDI is een gemiddelde over de hele bevolking. In landen met een lage HDI is de ongelijkheid vaak juist groot, met een kleine zeer welvarende groep.",
    ),
]
