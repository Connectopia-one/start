# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Licht: weerkaatsing, breking en lenzen.

Hoort bij "optica" van de vakfiche fysica 2de graad doorstroomfinaliteit, een
onderdeel van 10 % en daarmee één thema.

Deel 1 gaat over het stralenmodel en de weerkaatsing: een lichtstraal als
rechte met een pijl, het verschil tussen een ondoorschijnend, doorschijnend en
doorzichtig voorwerp, de terugkaatsingswetten met de invallende straal, het
invalspunt, de normaal, de invalshoek en de weerkaatsingshoek, het verschil
tussen regelmatige en diffuse weerkaatsing, het beeld bij een vlakke spiegel en
de schaduwvorming met kern- en bijschaduw. Deel 2 gaat over de breking tussen
twee middenstoffen, de schijnbare verhoging van een voorwerp onder water, en
het beeld bij een dunne bolle lens.

De vragen beschrijven elke situatie in woorden, want de constructie zelf doet
een kind op het examen met een geodriehoek op papier.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe stel je een lichtstraal grafisch voor?",
        opties=[
            "als een rechte met een pijl erop",
            "als een golvende lijn",
            "als een stippellijn zonder pijl",
            "als een cirkel om de bron",
        ],
        antwoord=0,
        uitleg="De rechte toont de weg van het licht en de pijl de zin waarin het zich voortplant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een doorschijnend voorwerp?",
        opties=[
            "het laat licht door, maar je ziet er niet scherp door",
            "het laat alle licht scherp door",
            "het laat helemaal geen licht door",
            "het kaatst alle licht terug",
        ],
        antwoord=0,
        uitleg="Matglas is doorschijnend: er komt licht door, maar het wordt verstrooid. Doorzichtig laat je wel scherp zien, ondoorschijnend laat niets door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de tweede terugkaatsingswet?",
        opties=[
            "de invalshoek is gelijk aan de weerkaatsingshoek",
            "de invalshoek is groter dan de weerkaatsingshoek",
            "de normaal staat langs het spiegeloppervlak",
            "de weerkaatste straal gaat door het spiegeloppervlak",
        ],
        antwoord=0,
        uitleg="Beide hoeken meet je ten opzichte van de normaal, de lijn loodrecht op de spiegel in het invalspunt. Ze zijn altijd even groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de normaal in een constructie van weerkaatsing?",
        opties=[
            "de lijn loodrecht op het oppervlak in het invalspunt",
            "de invallende lichtstraal",
            "de weerkaatste lichtstraal",
            "de lijn langs het oppervlak",
        ],
        antwoord=0,
        uitleg="Normaal betekent loodrecht. De invalshoek en de weerkaatsingshoek meet je altijd ten opzichte van die lijn, niet ten opzichte van de spiegel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een regelmatige en een diffuse weerkaatsing?",
        opties=[
            "bij een regelmatige weerkaatsing is het oppervlak glad en vlak",
            "bij een diffuse weerkaatsing is het oppervlak glad en vlak",
            "bij een diffuse weerkaatsing geldt de terugkaatsingswet niet",
            "bij een regelmatige weerkaatsing gaat het licht door het oppervlak",
        ],
        antwoord=0,
        uitleg="Op een spiegel of stil water blijven de stralen netjes samen. Op een ruw oppervlak, zoals papier, kaatst elke straal een andere kant op, maar de wet geldt ook daar in elk punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft het beeld van een voorwerp bij een vlakke spiegel? Kruis alles aan wat juist is.",
        opties=["het is virtueel", "het is even groot als het voorwerp", "het staat omgekeerd", "het is kleiner"],
        antwoord=[0, 1],
        uitleg="Het beeld lijkt achter de spiegel te liggen en is even groot en rechtopstaand. Je kan het niet op een scherm opvangen, dus is het virtueel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ver lijkt het beeld in een vlakke spiegel achter de spiegel te liggen?",
        opties=[
            "even ver als het voorwerp ervoor staat",
            "twee keer zo ver",
            "half zo ver",
            "dat hangt van de grootte van de spiegel af",
        ],
        antwoord=0,
        uitleg="De beeldafstand is gelijk aan de voorwerpsafstand. Sta je 1 m voor de spiegel, dan lijkt je beeld 1 m erachter, dus 2 m van jou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een virtueel beeld?",
        opties=[
            "een beeld dat je niet op een scherm kan opvangen",
            "een beeld dat je wel op een scherm kan opvangen",
            "een beeld dat altijd omgekeerd staat",
            "een beeld dat altijd kleiner is",
        ],
        antwoord=0,
        uitleg="De stralen komen er niet echt samen, ze lijken er enkel uit te komen. Een reëel beeld vang je wel op, zoals het beeld van een projector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat er een kernschaduw achter een voorwerp?",
        opties=[
            "daar komt helemaal geen licht van de bron",
            "daar komt licht van een deel van de bron",
            "daar komt licht van heel de bron",
            "daar wordt het licht gebroken",
        ],
        antwoord=0,
        uitleg="In de kernschaduw zie je geen enkel deel van de bron. In de bijschaduw zie je er wel een deel van, dus is het er minder donker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een zonsverduistering?",
        opties=[
            "de maan staat tussen de zon en de aarde",
            "de aarde staat tussen de zon en de maan",
            "de zon staat tussen de aarde en de maan",
            "de aarde draait sneller dan de maan",
        ],
        antwoord=0,
        uitleg="De maan werpt dan haar schaduw op de aarde. Staat de aarde ertussen, dan krijg je een maansverduistering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de omkeerbaarheid van de stralengang zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "licht volgt dezelfde weg terug als je de zin omkeert",
            "ze geldt bij weerkaatsing en bij breking",
            "ze geldt enkel bij een vlakke spiegel",
            "ze geldt enkel in lucht",
        ],
        antwoord=[0, 1],
        uitleg="Kaats je een straal terug langs de weerkaatste straal, dan komt hij langs de invallende straal uit. Dat geldt ook bij een breking en bij een lens.",
    ),
    dict(
        type="waarofniet",
        vraag="Het licht plant zich in een doorzichtige stof rechtlijnig voort.",
        antwoord=True,
        uitleg="Daarom kan je het met rechten tekenen. Pas aan een grensvlak met een andere stof verandert de richting.",
    ),
    dict(
        type="waarofniet",
        vraag="Je ziet je spiegelbeeld in een ruw vel papier even goed als in een spiegel.",
        antwoord=False,
        uitleg="Op papier kaatst het licht diffuus terug, in alle richtingen. Daardoor komt er geen beeld tot stand, al zie je het papier zelf wel.",
    ),
    dict(
        type="waarofniet",
        vraag="De invalshoek meet je tussen de invallende straal en het spiegeloppervlak.",
        antwoord=False,
        uitleg="Je meet die hoek tussen de invallende straal en de normaal, dus de loodlijn. Een straal die er schuin op valt onder 20° met de spiegel, heeft dus een invalshoek van 70°.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kleine lichtbron geeft een scherpere schaduw dan een grote lichtbron.",
        antwoord=True,
        uitleg="Bij een puntbron is er bijna geen bijschaduw. Een grote bron, zoals een tl-balk, geeft een brede bijschaduw en dus een vage rand.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ondoorschijnend voorwerp laat een beetje licht door.",
        antwoord=False,
        uitleg="Ondoorschijnend betekent dat er geen licht doorkomt. Een voorwerp dat wat licht doorlaat zonder scherp beeld, is doorschijnend.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het punt waar een invallende lichtstraal het spiegeloppervlak raakt?",
        antwoord=["invalspunt", "het invalspunt"],
        uitleg="Het invalspunt. Daar zet je de normaal op om de hoeken te meten.",
    ),
    dict(
        type="invultekst",
        vraag="Een lichtstraal valt onder een invalshoek van 35° op een spiegel. Hoe groot is de weerkaatsingshoek? Schrijf het getal in graden.",
        antwoord=["35", "35°", "35 graden"],
        uitleg="De twee hoeken zijn altijd gelijk, dus 35°.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het donkerste deel van de schaduw, waar geen licht van de bron komt?",
        antwoord=["kernschaduw", "de kernschaduw", "kern"],
        uitleg="De kernschaduw. Eromheen ligt de bijschaduw, waar je een deel van de bron nog ziet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een beeld dat je op een scherm kan opvangen?",
        antwoord=["reëel", "reeel", "een reëel beeld"],
        uitleg="Een reëel beeld. Daar komen de lichtstralen echt samen, zoals achter een bolle lens.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een lichtstraal die schuin van lucht in water gaat?",
        opties=[
            "hij buigt naar de normaal toe",
            "hij buigt van de normaal weg",
            "hij gaat rechtdoor",
            "hij kaatst volledig terug",
        ],
        antwoord=0,
        uitleg="Water is optisch dichter dan lucht, dus buigt de straal naar de normaal toe. De brekingshoek is dan kleiner dan de invalshoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een straal gaat van glas naar lucht. Wat geldt?",
        opties=[
            "de brekingshoek is groter dan de invalshoek",
            "de brekingshoek is kleiner dan de invalshoek",
            "de twee hoeken zijn gelijk",
            "er is geen breking",
        ],
        antwoord=0,
        uitleg="Van optisch dicht naar optisch ijl buigt de straal van de normaal weg, dus wordt de hoek groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lichtstraal valt loodrecht op een grensvlak tussen lucht en water. Wat gebeurt er?",
        opties=[
            "hij gaat rechtdoor zonder te breken",
            "hij buigt naar de normaal toe",
            "hij buigt van de normaal weg",
            "hij kaatst helemaal terug",
        ],
        antwoord=0,
        uitleg="Bij een invalshoek van 0° valt de straal al langs de normaal, dus is er niets om naartoe of weg te buigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijkt een stok die schuin in het water staat, geknikt?",
        opties=[
            "het licht breekt aan het wateroppervlak",
            "het licht kaatst op het water terug",
            "het water vergroot het beeld",
            "de stok buigt echt door het water",
        ],
        antwoord=0,
        uitleg="De stralen van het ondergedompelde deel veranderen van richting aan het oppervlak. Je oog trekt die stralen rechtdoor door, dus zie je dat deel op een andere plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijkt de bodem van een zwembad minder diep dan hij is?",
        opties=[
            "de stralen uit het water breken van de normaal weg",
            "de stralen uit het water breken naar de normaal toe",
            "het water kaatst het licht volledig terug",
            "het licht gaat sneller door water",
        ],
        antwoord=0,
        uitleg="Bij het verlaten van het water buigen de stralen van de normaal weg. Je oog volgt ze rechtdoor en komt zo op een punt hoger dan de echte bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het brandpunt van een bolle lens?",
        opties=[
            "het punt waar stralen parallel met de as samenkomen",
            "het punt waar de lens het dikst is",
            "het punt midden in de lens",
            "het punt waar het voorwerp staat",
        ],
        antwoord=0,
        uitleg="Stralen die parallel met de optische as invallen, gaan na de lens door het brandpunt F. De afstand van de lens tot F heet de brandpuntsafstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stralen zijn kenmerkende stralen bij een dunne bolle lens? Kruis alles aan wat juist is.",
        opties=[
            "een straal parallel met de optische as",
            "een straal door het optisch middelpunt",
            "een straal langs de rand van de lens",
            "een straal loodrecht op de optische as",
        ],
        antwoord=[0, 1],
        uitleg="De parallelle straal gaat na de lens door het brandpunt, de straal door het optisch middelpunt gaat rechtdoor. Met een straal door het brandpunt vóór de lens erbij heb je drie kenmerkende stralen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp staat verder van een bolle lens dan het dubbele van de brandpuntsafstand. Welk beeld krijg je?",
        opties=[
            "reëel, omgekeerd en kleiner",
            "reëel, rechtopstaand en groter",
            "virtueel, rechtopstaand en groter",
            "virtueel, omgekeerd en kleiner",
        ],
        antwoord=0,
        uitleg="Ver van de lens krijg je een reëel, omgekeerd en verkleind beeld. Zo werkt een fototoestel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp staat tussen een bolle lens en haar brandpunt. Welk beeld krijg je?",
        opties=[
            "virtueel, rechtopstaand en groter",
            "reëel, omgekeerd en groter",
            "reëel, rechtopstaand en kleiner",
            "virtueel, omgekeerd en kleiner",
        ],
        antwoord=0,
        uitleg="Dat is net wat een loep doet: je ziet een vergroot, rechtopstaand beeld dat je niet op een scherm kan opvangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bepaal je de vergrotingsfactor van een beeld bij een bolle lens?",
        opties=[
            "als de verhouding van de beeldgrootte tot de voorwerpsgrootte",
            "als het verschil tussen de beeldgrootte en de voorwerpsgrootte",
            "als het product van de twee groottes",
            "als de helft van de brandpuntsafstand",
        ],
        antwoord=0,
        uitleg="Die verhouding is even groot als de verhouding van de beeldafstand tot de voorwerpsafstand. Dat volgt uit de gelijkvormigheid van de driehoeken in de constructie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de optische as van een lens zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze gaat door het optisch middelpunt",
            "ze staat loodrecht op de lens",
            "ze loopt langs de rand van de lens",
            "ze gaat door het krommingsmiddelpunt niet",
        ],
        antwoord=[0, 1],
        uitleg="De optische as gaat loodrecht door de lens, door het optisch middelpunt en door de twee brandpunten en krommingsmiddelpunten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een breking blijft de invallende straal, de gebroken straal en de normaal in hetzelfde vlak liggen.",
        antwoord=True,
        uitleg="Dat is de eerste brekingswet. Hetzelfde geldt bij een weerkaatsing.",
    ),
    dict(
        type="waarofniet",
        vraag="Een optisch dichtere stof buigt een straal naar de normaal toe.",
        antwoord=True,
        uitleg="Ga je van ijl naar dicht, bijvoorbeeld van lucht naar glas, dan wordt de hoek met de normaal kleiner.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bolle lens kan enkel reële beelden maken.",
        antwoord=False,
        uitleg="Staat het voorwerp binnen de brandpuntsafstand, dan is het beeld virtueel, rechtopstaand en groter. Dat is het geval bij een loep.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bolle lens is in het midden dikker dan aan de rand.",
        antwoord=True,
        uitleg="Daardoor buigt ze de stralen naar elkaar toe en kunnen die in het brandpunt samenkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een bolle lens hoort een voorwerp dat verder weg staat, bij een beeld dat verder van de lens ligt.",
        antwoord=False,
        uitleg="Het is net omgekeerd: hoe verder het voorwerp, hoe dichter het beeld bij het brandpunt komt. Een voorwerp heel ver weg geeft een beeld precies in het brandpunt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de hoek tussen de gebroken straal en de normaal?",
        antwoord=["brekingshoek", "de brekingshoek"],
        uitleg="De brekingshoek. Bij een overgang naar een optisch dichtere stof is die kleiner dan de invalshoek.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor het brandpunt van een lens?",
        antwoord=["F"],
        uitleg="F. Een dunne bolle lens heeft er twee, een aan elke kant, even ver van de lens.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het punt in het midden van een dunne lens, waar een straal rechtdoor gaat? Schrijf de twee woorden.",
        antwoord=["optisch middelpunt", "het optisch middelpunt", "optisch midden"],
        uitleg="Het optisch middelpunt. Een straal die daardoor gaat, verandert niet van richting.",
    ),
    dict(
        type="invultekst",
        vraag="Een beeld is drie keer zo groot als het voorwerp. Hoe groot is de vergrotingsfactor? Schrijf het getal.",
        antwoord=["3", "3x", "drie"],
        uitleg="De vergrotingsfactor is de verhouding van de beeldgrootte tot de voorwerpsgrootte, dus 3.",
    ),
]
