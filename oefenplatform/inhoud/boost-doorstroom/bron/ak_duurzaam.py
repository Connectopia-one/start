# -*- coding: utf-8 -*-
"""De vragen voor "Duurzaam omgaan met de ruimte" (🚀 Boost doorstroom,
aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "duurzaamheid" (10 % van het
examen).

Deel 1 gaat over het denkkader: de vijf P's (Planet, People, Prosperity, Peace,
Partnership) en de duurzame ontwikkelingsdoelen van de Verenigde Naties, en
over hoe een hogere ontwikkelingsgraad zelf een stap naar een duurzame wereld
kan zijn.
Deel 2 gaat over het beoordelen: de gevolgen van verstedelijking, van
grondstofontginning, energieproductie en industrie, en van de landbouw op het
duurzaam ruimtegebruik, en de vraag of een gegeven bedrijf of plan duurzaam is.

De fiche zegt uitdrukkelijk dat een overzicht van de duurzame
ontwikkelingsdoelen op het examen zelf meegegeven wordt. De vragen hier vragen
dus nergens om een doel uit het hoofd te nummeren; ze vragen om met dat kader
te redeneren. Wat in [[ak_stad]] en [[ak_landbouw]] al beschreven werd, komt
hier terug als beoordeling, niet als herhaling van de beschrijving.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent duurzame ontwikkeling?",
        opties=[
            "Voorzien in de noden van nu zonder die van later onmogelijk te maken",
            "Zo weinig mogelijk grondstoffen gebruiken, wat het ook kost aan welvaart",
            "De economie van een land zo snel mogelijk laten groeien",
            "Alle natuurgebieden van een land volledig afsluiten voor mensen",
        ],
        antwoord=0,
        uitleg="De klassieke omschrijving zet de huidige generatie en de volgende naast elkaar. Daarom gaat duurzaamheid over de planeet én over mensen én over welvaart tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar staan de vijf P's van duurzame ontwikkeling voor?",
        opties=[
            "Planet, People, Prosperity, Peace en Partnership",
            "Planet, Power, Progress, Peace en Production",
            "People, Plants, Property, Peace en Policy",
            "Planet, People, Politics, Power en Production",
        ],
        antwoord=0,
        uitleg="De planeet, de mensen, de welvaart, de vrede en de samenwerking. Samen tonen ze dat duurzaamheid meer is dan milieu alleen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vrede is een van de vijf P's van duurzame ontwikkeling.",
        antwoord=True,
        uitleg="Zonder veiligheid werkt niets anders: in oorlogsgebied is er geen onderwijs, geen zorg, geen investering en geen bosbeheer. Peace staat daarom naast Planet en People.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke P hoort bij de zorg voor het milieu, het klimaat en de natuur?",
        opties=[
            "Planet",
            "People",
            "Prosperity",
            "Partnership",
        ],
        antwoord=0,
        uitleg="Planet gaat over de aarde zelf: klimaat, water, bodem, lucht en biodiversiteit. People gaat over gezondheid, onderwijs en gelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke thema's horen bij de P van People? (meerdere antwoorden mogelijk)",
        opties=[
            "Onderwijs voor iedereen",
            "Goede gezondheidszorg",
            "Het uitbannen van honger",
            "Het beschermen van de oceanen",
            "Samenwerking tussen landen",
        ],
        antwoord=[0, 1, 2],
        uitleg="People gaat over de basisvoorwaarden van een menswaardig leven. Oceanen horen bij Planet, samenwerking tussen landen bij Partnership.",
    ),
    dict(
        type="waarofniet",
        vraag="De duurzame ontwikkelingsdoelen werden door de Verenigde Naties afgesproken.",
        antwoord=True,
        uitleg="De landen van de VN keurden ze in 2015 goed, met 2030 als streefdatum. Ze gelden voor alle landen, ook voor de rijke, niet alleen voor de armere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gelden de duurzame ontwikkelingsdoelen ook voor welvarende landen?",
        opties=[
            "Ook daar zijn er armoede, ongelijkheid en milieudruk",
            "Zij zijn de enige landen die er het geld voor hebben",
            "Zij hebben de doelen in hun eentje opgesteld en ondertekend",
            "Zij moeten er de armere landen mee controleren en beoordelen",
        ],
        antwoord=0,
        uitleg="Dat is net het verschil met de oudere millenniumdoelen, die vooral op arme landen mikten. Uitstoot, afval en ongelijkheid zijn in rijke landen vaak juist het grootst.",
    ),
    dict(
        type="invultekst",
        vraag="Voor welk jaar willen de Verenigde Naties de duurzame ontwikkelingsdoelen bereikt hebben?",
        antwoord=["2030"],
        uitleg="De doelen werden in 2015 goedgekeurd met 2030 als horizon. Dat maakt ze concreet: er valt op af te rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan een hogere ontwikkelingsgraad bijdragen aan een duurzamere wereld?",
        opties=[
            "Beter onderwijs en zorg geven mensen ruimte om verder te kijken",
            "Rijkere landen verbruiken altijd minder grondstoffen dan armere",
            "Een hogere index verlaagt vanzelf de uitstoot van een heel land",
            "Ontwikkeling maakt landbouw in een land na verloop van tijd onnodig",
        ],
        antwoord=0,
        uitleg="Wie zeker is van eten, gezondheid en school, kan investeren in de lange termijn. Tegelijk stijgt met welvaart ook het verbruik, en juist dat spanningsveld is de kern van het debat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land met een hoge Human Development Index heeft daarom automatisch een kleine ecologische voetafdruk.",
        antwoord=False,
        uitleg="Vaak is het omgekeerde waar: hoge welvaart gaat samen met veel verbruik, veel vlees, veel vliegen en veel afval. Ontwikkeling en duurzaamheid lopen niet vanzelf gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat Partnership als een aparte P tussen de vijf?",
        opties=[
            "Geen enkel land lost deze problemen alleen op",
            "Alleen bedrijven kunnen de doelen bereiken",
            "Partnership vervangt de rol van regeringen",
            "Samenwerken is enkel nodig binnen Europa",
        ],
        antwoord=0,
        uitleg="Klimaat, oceanen, ziektes en handel stoppen niet aan een grens. Wie het alleen probeert, wordt ingehaald door wat elders gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de duurzame ontwikkelingsdoelen kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Ze gaan over milieu, mensen en economie samen",
            "Ze gelden voor alle landen ter wereld",
            "Ze hebben een afgesproken einddatum",
            "Ze zijn wettelijk afdwingbaar bij een rechtbank",
            "Ze gaan uitsluitend over de uitstoot van CO₂",
        ],
        antwoord=[0, 1, 2],
        uitleg="De doelen zijn breed, wereldwijd en tijdgebonden. Afdwingbaar zijn ze niet: landen rapporteren vrijwillig, en dat is meteen hun zwakke plek.",
    ),
    dict(
        type="waarofniet",
        vraag="Duurzaamheid gaat alleen over het milieu.",
        antwoord=False,
        uitleg="Armoede, onderwijs, ongelijkheid, werk en vrede staan er evengoed in. De vijf P's zijn er juist om te tonen dat die dingen aan elkaar vastzitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente legt een nieuw bedrijventerrein aan op akkerland. Vanuit welke P is dat het moeilijkst te verdedigen?",
        opties=[
            "Planet",
            "Prosperity",
            "Peace",
            "Partnership",
        ],
        antwoord=0,
        uitleg="Er verdwijnt open ruimte en er komt verharding bij, dus de planeet betaalt. Vanuit Prosperity valt er wel iets voor te zeggen: werk en inkomen voor de streek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom botsen de vijf P's soms met elkaar?",
        opties=[
            "Wat goed is voor de welvaart, is niet altijd goed voor de planeet",
            "Ze werden van bij het begin in tegenspraak met elkaar opgesteld",
            "Alleen Planet en People zijn echte doelen, de rest is versiering",
            "Elke P geldt in een ander werelddeel dan de vier andere",
        ],
        antwoord=0,
        uitleg="Een nieuwe fabriek brengt werk maar kost ruimte en uitstoot. Duurzaam beslissen betekent die afweging bewust maken in plaats van één kant te vergeten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de oppervlakte aarde die nodig is om iemands verbruik te dekken en zijn afval te verwerken?",
        antwoord=["ecologische voetafdruk", "de ecologische voetafdruk", "voetafdruk"],
        uitleg="De ecologische voetafdruk maakt verbruik meetbaar in hectare. Leefden alle mensen zoals de gemiddelde West-Europeaan, dan was er meer dan één aarde nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Duurzaam ruimtegebruik betekent dat je met dezelfde oppervlakte meer doet, in plaats van telkens nieuwe ruimte aan te snijden.",
        antwoord=True,
        uitleg="Hergebruik van een leegstaand gebouw, inbreiding, een terrein met meerdere functies: dat spaart open ruimte. Nieuwe grond aansnijden is altijd de duurste keuze voor de planeet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag stel je het eerst als je wil weten of een plan duurzaam is?",
        opties=[
            "Wat betekent dit op lange termijn voor mens én omgeving?",
            "Hoeveel winst levert dit plan het eerste jaar al op?",
            "Hoeveel vierkante meter grond beslaat dit plan in totaal?",
            "Wie heeft dit plan als eerste voorgesteld, en wanneer?",
        ],
        antwoord=0,
        uitleg="Duurzaam beoordelen is altijd in de tijd vooruitkijken en naar meerdere P's tegelijk. Winst en oppervlakte zijn onderdelen van die afweging, niet het antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen passen bij de P van Planet? (meerdere antwoorden mogelijk)",
        opties=[
            "Een braakliggend terrein omvormen tot natuur",
            "Regenwater laten insijpelen in plaats van afvoeren",
            "Gescheiden afval en hergebruik van materialen",
            "De lonen in de bouwsector stelselmatig verhogen",
            "Meer scholen bouwen in het centrum van de stad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Natuur, water en materialen horen bij Planet. Lonen horen bij Prosperity en scholen bij People; die zijn niet minder belangrijk, maar ze horen onder een andere P.",
    ),
    dict(
        type="waarofniet",
        vraag="Een duurzame keuze is altijd de goedkoopste keuze op korte termijn.",
        antwoord=False,
        uitleg="Vaak kost ze eerst meer: isoleren, hergebruiken, zuiveren. Ze verdient zich later terug, en juist daarom is de tijdshorizon zo belangrijk in de beoordeling.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom is versnippering van de open ruimte een probleem voor de natuur?",
        opties=[
            "Kleine losse stukken werken minder goed dan één groot gebied",
            "Kleine stukken natuur zijn altijd een stuk minder vruchtbaar",
            "Versnippering verandert de klimaatzone van het hele gebied",
            "Versnippering verlaagt de bevolkingsdichtheid van de streek",
        ],
        antwoord=0,
        uitleg="Dieren kunnen zich niet verplaatsen tussen de stukken, en de randen drogen uit en verstoren. Daarom bouwt men ecoducten en verbindingsstroken tussen gebieden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen van verstedelijking op het leefmilieu somt de vakfiche op? (meerdere antwoorden mogelijk)",
        opties=[
            "Versnippering van de open ruimte en verharding",
            "Het hitte-eilandeffect in de stad",
            "Luchtvervuiling en verkeersdrukte",
            "Verzilting van de landbouwgrond",
            "Het afsmelten van de gletsjers",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt versnippering, verharding, het hitte-eilandeffect, luchtvervuiling en verkeersdrukte. Verzilting hoort bij de landbouw, gletsjers bij het broeikaseffect.",
    ),
    dict(
        type="waarofniet",
        vraag="Meer groen en water in een stad verzachten het hitte-eilandeffect.",
        antwoord=True,
        uitleg="Bomen geven schaduw en verdampen water, en dat koelt. Een straat met bomen kan op een hete dag merkbaar koeler zijn dan dezelfde straat zonder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente kiest tussen een nieuwe verkaveling op akkerland en het opknappen van een leegstaande fabriekssite. Welke keuze is duurzamer, en waarom?",
        opties=[
            "De fabriekssite, want er wordt geen nieuwe open ruimte aangesneden",
            "De verkaveling, want nieuwbouw is altijd veel beter geïsoleerd",
            "De verkaveling, want er wonen dan meer mensen op één hectare",
            "De fabriekssite, want oude gebouwen zijn altijd goedkoper te kopen",
        ],
        antwoord=0,
        uitleg="Hergebruik van een bestaand terrein spaart akkerland en houdt de voorzieningen dicht bij elkaar. Of de oude site goedkoper is, hangt af van de vervuiling in de bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij industrialisatie van een streek?",
        opties=[
            "Er komt fabrieksactiviteit bij, met werk en met ruimtebeslag",
            "De fabrieken verdwijnen uit de streek, met werk en al",
            "Oude fabrieksterreinen krijgen er een heel nieuwe functie",
            "De landbouwbedrijven in de streek worden groter en moderner",
        ],
        antwoord=0,
        uitleg="Industrialisatie brengt werk, inwoners en infrastructuur, maar ook uitstoot en ruimtebeslag. Het omgekeerde is de-industrialisatie, en wat daarna met het terrein gebeurt, is reconversie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oude fabriekssite kan meteen herbouwd worden, want vervuiling verdwijnt vanzelf uit de bodem.",
        antwoord=False,
        uitleg="Zware metalen, olie en oplosmiddelen blijven decennia in de bodem zitten. De grond moet eerst gesaneerd worden, en die kost is een van de redenen waarom zo'n site soms jaren leeg blijft liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het duurzame voordeel van reconversie tegenover een nieuw terrein aansnijden?",
        opties=[
            "De grond werd al gebruikt, dus er gaat geen open ruimte verloren",
            "De grond is altijd goedkoper dan een stuk onbebouwde grond",
            "Er zijn voor zo'n terrein nooit vergunningen voor nodig",
            "De bouwwerken duren er altijd korter dan bij nieuwbouw",
        ],
        antwoord=0,
        uitleg="Ruimte die al aangesneden was, blijft aangesneden. Dat is de grootste winst, ook als de sanering en de verbouwing zelf een stuk duurder uitvallen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het schoonmaken van een vervuilde bodem voor er opnieuw gebouwd kan worden?",
        antwoord=["sanering", "saneren", "bodemsanering"],
        uitleg="Bij sanering wordt de vervuiling weggenomen of onschadelijk gemaakt. Zonder sanering mag een vervuild terrein geen woonfunctie krijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een landbouwbedrijf teelt jaar na jaar maïs op dezelfde hellende percelen, zonder groenbedekker. Hoe beoordeel je dat?",
        opties=[
            "Niet duurzaam: de bodem raakt uitgeput en spoelt weg",
            "Duurzaam: één gewas telen is efficiënter",
            "Duurzaam: maïs beschermt de bodem het hele jaar",
            "Niet te beoordelen zonder de winst van het bedrijf te kennen",
        ],
        antwoord=0,
        uitleg="Geen vruchtwisseling put de bodem uit, en een kale helling na de oogst laat de regen de bovenlaag meenemen. Allebei zijn het schoolvoorbeelden van niet-duurzaam ruimtegebruik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken zou je opsommen om een landbouwbedrijf als duurzaam te beoordelen? (meerdere antwoorden mogelijk)",
        opties=[
            "Het wisselt zijn gewassen af en dekt de bodem in de winter",
            "Het houdt hagen, bomen en bufferstroken op zijn land",
            "Het bemest en beregent niet meer dan de teelt opneemt",
            "Het vergroot zijn percelen zo veel als het maar kan",
            "Het verkoopt zijn oogst zo ver mogelijk van huis weg",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vruchtwisseling, landschapselementen en doordacht bemesten houden bodem en water gezond. Grotere percelen en verre afzet werken de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="Ontbossing voor landbouwgrond laat koolstof vrij die in het bos opgeslagen zat.",
        antwoord=True,
        uitleg="Bomen en bosbodem houden enorme hoeveelheden koolstof vast. Wordt het bos gekapt of verbrand, dan komt die koolstof als CO₂ in de lucht, bovenop het verlies aan biodiversiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is bodemdegradatie een probleem voor de lange termijn?",
        opties=[
            "Herstel duurt tientallen jaren, verlies gaat in enkele seizoenen",
            "De bodem verandert erdoor stilaan van klimaatzone",
            "De bodem wordt er na enkele jaren sneller vruchtbaar van",
            "Ze treft enkel de bodems die in de poolstreken liggen",
        ],
        antwoord=0,
        uitleg="Een centimeter vruchtbare bovengrond opbouwen vraagt honderden jaren. Daarom telt bodem in de duurzaamheidsdiscussie als een voorraad, niet als iets hernieuwbaars.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stad legt een fietssnelweg aan en verlaagt de parkeerplaatsen in het centrum. Welke problemen pakt ze daarmee aan? (meerdere antwoorden mogelijk)",
        opties=[
            "Luchtvervuiling in het centrum",
            "Verkeersdrukte in de straten",
            "Verharding door parkeerplaatsen",
            "Bodemerosie op de akkers errond",
            "Versnippering door de ringweg",
        ],
        antwoord=[0, 1, 2],
        uitleg="Minder auto's betekent minder uitstoot, minder drukte en minder asfalt. Aan erosie op akkers of aan een bestaande ringweg verandert een fietspad niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Duurzaam ruimtegebruik en economische groei sluiten elkaar altijd uit.",
        antwoord=False,
        uitleg="Hergebruik, isolatie, hernieuwbare energie en kringloop leveren ook werk en omzet op. De spanning is echt, maar ze is geen wet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is verharding een probleem bij hevige regen?",
        opties=[
            "Het water kan niet in de grond en loopt naar de riool",
            "Het water verdampt sneller dan het naar beneden valt",
            "Het water wordt onderweg vervuild door de bodem zelf",
            "Het water vult de grondwaterlagen veel te snel aan",
        ],
        antwoord=0,
        uitleg="Alles stroomt tegelijk naar dezelfde riool, die overloopt. Daardoor stijgt het overstromingsrisico stroomafwaarts, terwijl het grondwater onder de stad juist niet wordt aangevuld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het opnieuw inrichten van een oude industriesite voor een nieuw gebruik, zoals wonen of onderzoek?",
        antwoord=["reconversie", "de reconversie"],
        uitleg="Reconversie is de derde stap na industrialisatie en de-industrialisatie. Ze bepaalt of een streek na het verdwijnen van haar industrie weer op gang komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plan kan goed scoren op Prosperity en tegelijk slecht op Planet.",
        antwoord=True,
        uitleg="Dat is bijna altijd zo bij grote infrastructuurwerken. Duurzaam beoordelen betekent die twee naast elkaar leggen en de afweging uitschrijven, niet één kant weglaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt op het examen de beschrijving van een landbouwbedrijf en de lijst met duurzame ontwikkelingsdoelen. Wat wordt van je verwacht?",
        opties=[
            "Beoordelen of het bedrijf duurzaam werkt, met argumenten uit die lijst",
            "De doelen in de juiste volgorde uit het hoofd opsommen en nummeren",
            "De winst van het bedrijf voor het volgende jaar berekenen en vergelijken",
            "De geografische coördinaten van het bedrijf op de kaart aanduiden",
        ],
        antwoord=0,
        uitleg="De lijst krijg je erbij; het gaat om de redenering. Je koppelt wat je in de beschrijving leest aan een doel of aan een van de vijf P's, en je zegt waarom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk argument hoort bij het beoordelen van een windmolenpark vanuit de vijf P's?",
        opties=[
            "Het levert energie zonder uitstoot, maar neemt wel ruimte in",
            "Het is duurzaam, want windmolens zijn altijd hernieuwbaar",
            "Het is niet duurzaam, want er staan machines in het landschap",
            "Het valt niet te beoordelen zonder de coördinaten te kennen",
        ],
        antwoord=0,
        uitleg="Een goed oordeel weegt af in plaats van te kiezen. Planet wint bij de uitstoot, maar landschap, geluid en vogels staan aan de andere kant van de weegschaal.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk land kan de duurzame ontwikkelingsdoelen in zijn eentje halen, los van de andere landen.",
        antwoord=False,
        uitleg="Daarom staat Partnership als aparte P in het rijtje. Kennis, geld en regels moeten over grenzen heen bewegen, anders verschuift een probleem gewoon naar het volgende land.",
    ),
]
