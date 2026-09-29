# -*- coding: utf-8 -*-
"""De vragen voor "De economische kringloop" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik maak deel uit van een
economische kringloop" (20 % van het examen), het deel over de gezinnen en de
bedrijven. Het deel over de overheid staat in [[se_overheid]].

Deel 1 gaat over de kringloop zelf (de drie spelers, de goederen- en
dienstenstromen en de geldstromen) en over wat er binnen een bedrijf gebeurt.
Deel 2 gaat over de vier sectoren, de soorten goederen en bedrijven, en over de
inkomsten en uitgaven van een gezin.

De fiche vraagt uitdrukkelijk dat je van een gegeven stroom kan aanwijzen bij
welke speler die begint en bij welke speler die eindigt. Daarom staan hier
zoveel vragen met een concreet voorbeeld in plaats van met een definitie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit welke spelers bestaat de eenvoudige economische kringloop?",
        opties=[
            "De gezinnen",
            "De bedrijven",
            "De overheid",
            "De banken uit het buitenland",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eenvoudige economische kringloop heeft drie spelers: de gezinnen, de bedrijven en de overheid. Tussen hen lopen de stromen van geld, goederen en diensten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een goederenstroom?",
        opties=[
            "Het verplaatsen van een product van de ene speler naar de andere",
            "Het geld dat van de ene speler naar de andere speler overgaat",
            "Het aantal mensen dat in een bedrijf komt werken",
            "De volgorde waarin een bedrijf zijn taken afwerkt",
        ],
        antwoord=0,
        uitleg="Een goederenstroom is het product zelf dat van speler naar speler gaat. Loopt er geld, dan spreken we van een geldstroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je koopt brood bij de bakker. Waar begint en waar eindigt de geldstroom?",
        opties=[
            "Ze begint bij het gezin en eindigt bij het bedrijf",
            "Ze begint bij het bedrijf en eindigt bij het gezin",
            "Ze begint bij de overheid en eindigt bij het gezin",
            "Ze begint bij het gezin en eindigt bij de overheid",
        ],
        antwoord=0,
        uitleg="Jij betaalt, dus het geld vertrekt bij het gezin en komt bij de bakker terecht. Het brood zelf is de goederenstroom, en die loopt net omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vader krijgt zijn loon van zijn werkgever. Waar begint en waar eindigt die geldstroom?",
        opties=[
            "Ze begint bij het bedrijf en eindigt bij het gezin",
            "Ze begint bij het gezin en eindigt bij het bedrijf",
            "Ze begint bij de overheid en eindigt bij het bedrijf",
            "Ze begint bij het bedrijf en eindigt bij de overheid",
        ],
        antwoord=0,
        uitleg="Het bedrijf betaalt het loon uit, dus het geld vertrekt daar en komt bij het gezin terecht. In ruil levert het gezin arbeid.",
    ),
    dict(
        type="waarofniet",
        vraag="Gezinnen leveren arbeid aan de bedrijven en krijgen daar loon voor terug.",
        antwoord=True,
        uitleg="Klopt. Dat is een van de belangrijkste verbindingen in de kringloop: arbeid in de ene richting, loon in de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin betaalt belasting op zijn inkomen. Waar eindigt die geldstroom?",
        opties=[
            "Bij de overheid",
            "Bij het bedrijf waar iemand werkt",
            "Bij een ander gezin in de straat",
            "Bij de bank van het gezin",
        ],
        antwoord=0,
        uitleg="Belastingen zijn een geldstroom van de gezinnen naar de overheid. Daarmee betaalt de overheid haar uitgaven.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij elke goederenstroom loopt er in de omgekeerde richting meestal een geldstroom.",
        antwoord=True,
        uitleg="Klopt. Wie iets krijgt, betaalt er meestal voor. Daarom draaien de twee stromen als een kringloop rond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een consument in de economie?",
        opties=[
            "Wie goederen en diensten koopt om zelf te gebruiken",
            "Wie goederen maakt en daarna verkoopt aan anderen",
            "Wie belastingen int bij de gezinnen en de bedrijven",
            "Wie arbeid inkoopt om er producten mee te maken",
        ],
        antwoord=0,
        uitleg="De gezinnen zijn de consumenten: zij kopen om te gebruiken. De bedrijven zijn de producenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn kernactiviteiten in een bedrijf?",
        opties=[
            "De aankoop",
            "De boekhouding",
            "De marketing",
            "Het bezoek van de inspectie",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt de aankoop, de algemene directie, de boekhouding, het magazijn, de marketing, het onthaal, de productie en de verkoop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke afdeling van een bedrijf zorgt ervoor dat de grondstoffen binnenkomen?",
        opties=[
            "De aankoop",
            "De verkoop",
            "De marketing",
            "Het onthaal",
        ],
        antwoord=0,
        uitleg="De aankoopafdeling koopt de grondstoffen en het materiaal in. De verkoop doet het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke afdeling houdt bij wat er binnenkomt en buitengaat aan geld?",
        opties=[
            "De boekhouding",
            "Het magazijn van het bedrijf",
            "De algemene directie of zaakvoerder",
            "De afdeling marketing en reclame",
        ],
        antwoord=0,
        uitleg="De boekhouding houdt alle inkomsten en uitgaven bij. Zo weet het bedrijf of het winst of verlies maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de afdeling marketing?",
        opties=[
            "Ze zorgt dat klanten het product leren kennen en willen kopen",
            "Ze bewaart de producten in het magazijn tot ze verzonden worden",
            "Ze betaalt de facturen die binnenkomen op tijd",
            "Ze ontvangt de bezoekers die aan de balie aanmelden",
        ],
        antwoord=0,
        uitleg="Marketing maakt het product bekend en aantrekkelijk. Het magazijn bewaart, de boekhouding betaalt en het onthaal ontvangt.",
    ),
    dict(
        type="waarofniet",
        vraag="In een klein bedrijf mag één persoon niet meer dan één kernactiviteit doen.",
        antwoord=False,
        uitleg="In een eenmanszaak doet de zaakvoerder vaak de aankoop, de verkoop en de boekhouding zelf. De taken bestaan allemaal, maar de mensen zijn dezelfde.",
    ),
    dict(
        type="waarofniet",
        vraag="De algemene directie of zaakvoerder staat in voor het opslaan van de voorraad.",
        antwoord=False,
        uitleg="Dat is het magazijn. De directie of zaakvoerder neemt de grote beslissingen en stuurt het geheel aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in het magazijn van een bedrijf?",
        opties=[
            "De producten en grondstoffen worden er bewaard tot ze nodig zijn",
            "De klanten worden er ontvangen als ze langskomen",
            "De reclamecampagnes worden er uitgedacht, gemaakt en opgevolgd",
            "De lonen van het personeel worden er berekend",
        ],
        antwoord=0,
        uitleg="Het magazijn is de opslag. Ontvangen doet het onthaal, reclame de marketing, en lonen de boekhouding.",
    ),
    dict(
        type="waarofniet",
        vraag="De overheid hoort niet thuis in de economische kringloop, want ze verkoopt niets.",
        antwoord=False,
        uitleg="De overheid hoort er wel bij. Ze int belastingen, betaalt uitkeringen en lonen, en koopt zelf goederen en diensten aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf betaalt belasting op zijn winst. Tussen welke twee spelers loopt die geldstroom?",
        opties=[
            "Van het bedrijf naar de overheid",
            "Van de overheid naar het bedrijf",
            "Van het bedrijf naar de gezinnen",
            "Van de gezinnen naar het bedrijf",
        ],
        antwoord=0,
        uitleg="Belasting op de bedrijfswinst gaat van het bedrijf naar de overheid, net zoals de inkomstenbelasting van de gezinnen komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stromen lopen tussen een gezin en een bedrijf?",
        opties=[
            "Arbeid van het gezin naar het bedrijf",
            "Loon van het bedrijf naar het gezin",
            "Goederen en diensten van het bedrijf naar het gezin",
            "Uitkeringen van het bedrijf naar het gezin",
        ],
        antwoord=[0, 1, 2],
        uitleg="Arbeid, loon, en goederen en diensten lopen tussen gezin en bedrijf. Uitkeringen komen van de overheid, niet van een bedrijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder de gezinnen zouden de bedrijven geen arbeidskrachten en geen klanten hebben.",
        antwoord=True,
        uitleg="Klopt. De gezinnen leveren het werk en kopen het resultaat. Daarom is het een kringloop en geen rechte lijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de beweging van geld, goederen en diensten tussen gezinnen, bedrijven en overheid?",
        antwoord=["de economische kringloop", "economische kringloop", "de kringloop"],
        uitleg="De economische kringloop laat zien hoe de drie spelers met elkaar verbonden zijn.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke sectoren onderscheiden we in de economie?",
        opties=[
            "De primaire sector",
            "De secundaire sector",
            "De tertiaire en de quartaire sector",
            "De commerciële en de niet-commerciële sector",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vier sectoren zijn de primaire, de secundaire, de tertiaire en de quartaire. Commercieel en niet-commercieel is een andere indeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de primaire sector?",
        opties=[
            "Grondstoffen worden uit de natuur gehaald",
            "Grondstoffen worden verwerkt tot afgewerkte producten",
            "Diensten worden verkocht aan klanten die ervoor betalen",
            "Diensten worden geleverd zonder dat er winst mee bedoeld is",
        ],
        antwoord=0,
        uitleg="De primaire sector wint grondstoffen: landbouw, visserij, bosbouw en mijnbouw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke sector behoort een fabriek die meubels maakt uit hout?",
        opties=[
            "De secundaire sector",
            "De primaire sector van de grondstoffen",
            "De tertiaire sector van de diensten",
            "De quartaire sector van de zorg",
        ],
        antwoord=0,
        uitleg="De secundaire sector verwerkt grondstoffen tot producten. De boswachter die het hout kapt, zit in de primaire sector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze bedrijven horen bij de tertiaire sector?",
        opties=[
            "Een kapsalon",
            "Een supermarkt",
            "Een transportbedrijf",
            "Een openbare school",
        ],
        antwoord=[0, 1, 2],
        uitleg="De tertiaire sector levert diensten waarvoor betaald wordt. Een openbare school hoort bij de quartaire sector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de quartaire sector?",
        opties=[
            "Er worden diensten geleverd zonder winstoogmerk",
            "Er worden grondstoffen uit de natuur gehaald",
            "Er worden producten in een fabriek gemaakt",
            "Er worden goederen doorverkocht met winst",
        ],
        antwoord=0,
        uitleg="De quartaire sector zijn de niet-commerciële diensten: onderwijs, zorg, welzijn en het openbaar bestuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ziekenhuis en een school horen allebei bij de quartaire sector.",
        antwoord=True,
        uitleg="Klopt. Het zijn diensten die er niet in de eerste plaats zijn om winst te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een landbouwer die melk levert aan een zuivelfabriek hoort bij de secundaire sector.",
        antwoord=False,
        uitleg="De landbouwer zit in de primaire sector. De zuivelfabriek die er yoghurt van maakt, zit in de secundaire.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een investeringsgoed?",
        opties=[
            "Een goed dat een bedrijf gebruikt om iets mee te maken",
            "Een goed dat een gezin koopt om zelf op te gebruiken",
            "Een goed dat een winkel met korting verkoopt",
            "Een goed dat na één keer gebruiken weg is",
        ],
        antwoord=0,
        uitleg="Een oven in een bakkerij is een investeringsgoed: het bedrijf produceert ermee. Een brood is een consumentengoed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn consumentengoederen?",
        opties=[
            "Een paar schoenen dat je koopt",
            "Een brood uit de winkel",
            "Een gsm die je zelf gebruikt",
            "Een vrachtwagen van een transportbedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Consumentengoederen koop je om zelf te gebruiken. De vrachtwagen van een bedrijf is een investeringsgoed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een consumentendienst?",
        opties=[
            "Een dienst die je koopt voor jezelf, zoals een knipbeurt",
            "Een machine die een bedrijf koopt om mee te kunnen werken",
            "Een product dat je in de winkel kan meenemen",
            "Een grondstof die een fabriek nog moet verwerken",
        ],
        antwoord=0,
        uitleg="Bij een dienst krijg je geen voorwerp maar een prestatie: knippen, verzekeren, vervoeren, herstellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een handelsbedrijf?",
        opties=[
            "Het koopt producten in en verkoopt ze zonder ze te bewerken",
            "Het maakt zelf producten uit grondstoffen en materialen",
            "Het levert alleen diensten en verkoopt geen producten",
            "Het deelt producten gratis uit zonder er winst op te maken",
        ],
        antwoord=0,
        uitleg="Een handelsbedrijf koopt en verkoopt, zoals een supermarkt. Een productiebedrijf maakt zelf, een dienstenbedrijf levert diensten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een non-profitorganisatie heeft winst maken niet als doel.",
        antwoord=True,
        uitleg="Klopt. Een vzw of een ziekenfonds mag wel geld overhouden, maar dat gaat terug naar de werking en niet naar de eigenaars.",
    ),
    dict(
        type="waarofniet",
        vraag="Een profitbedrijf mag geen personeel in dienst nemen.",
        antwoord=False,
        uitleg="Natuurlijk wel. Het verschil met een non-profitorganisatie zit in het doel, niet in wie er werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn terugkerende inkomsten van een gezin?",
        opties=[
            "Inkomsten die regelmatig binnenkomen, zoals een loon",
            "Inkomsten die je maar één keer in je leven krijgt",
            "Inkomsten die je alleen in de zomermaanden krijgt",
            "Inkomsten waarvan je het bedrag niet op voorhand kent",
        ],
        antwoord=0,
        uitleg="Een loon, een pensioen, een uitkering of het groeipakket komen telkens terug. Daar kan een gezin op rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn toevallige inkomsten?",
        opties=[
            "Een erfenis",
            "De opbrengst van iets dat je tweedehands verkoopt",
            "Een prijs die je wint",
            "Het maandloon van je moeder",
        ],
        antwoord=[0, 1, 2],
        uitleg="Toevallige inkomsten komen onverwacht en niet elke maand terug. Een maandloon is een terugkerend inkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vaste uitgave?",
        opties=[
            "Een uitgave die telkens hetzelfde bedrag kost, zoals de huur",
            "Een uitgave die elke maand weer een ander bedrag blijkt te kosten",
            "Een uitgave die je helemaal niet had zien aankomen",
            "Een uitgave die maar heel zelden voorkomt",
        ],
        antwoord=0,
        uitleg="Huur, een abonnement of een verzekering zijn vaste uitgaven: ze komen terug en het bedrag ligt vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="De wasmachine gaat stuk en moet vervangen worden. Wat voor uitgave is dat?",
        opties=[
            "Een onvoorziene uitgave",
            "Een vaste uitgave van het gezin",
            "Een variabele uitgave van het gezin",
            "Een terugkerende uitgave van het gezin",
        ],
        antwoord=0,
        uitleg="Een onvoorziene uitgave zie je niet aankomen. Daarom houden gezinnen best een buffer opzij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn variabele uitgaven?",
        opties=[
            "De boodschappen van de week",
            "De brandstof voor de auto",
            "De huur van het appartement",
            "De verzekering van de auto",
        ],
        antwoord=[0, 1],
        uitleg="Bij boodschappen en brandstof verschilt het bedrag telkens. Huur en verzekering liggen vast.",
    ),
    dict(
        type="waarofniet",
        vraag="Een nieuwe keuken kopen is een onvoorziene uitgave.",
        antwoord=False,
        uitleg="Het is een uitzonderlijke uitgave: groot en zeldzaam, maar je ziet ze aankomen en je kan ervoor sparen. Onvoorzien is wat je niet zag komen, zoals een stuk wasmachine.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we een goed dat een bedrijf koopt om er zelf mee te produceren?",
        antwoord=["een investeringsgoed", "investeringsgoed"],
        uitleg="Een machine, een oven of een vrachtwagen van een bedrijf is een investeringsgoed.",
    ),
]
