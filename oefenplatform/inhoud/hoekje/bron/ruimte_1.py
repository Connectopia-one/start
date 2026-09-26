# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — De ruimte, deel 1: ons zonnestelsel en de afstanden."""

VAK = "De ruimte"
BESTAND = "de-ruimte.json"
TITEL = "Sterren, planeten en afstanden"
VOLGORDE = 1

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "De ster Proxima Centauri ligt op 4,2 lichtjaar van ons. Wat betekent dat?",
        "opties": [
            "Het licht van die ster is 4,2 jaar onderweg voor het ons bereikt",
            "Die ster draait in 4,2 jaar één keer rond onze eigen zon heen",
            "Een raket van ons zou er ongeveer 4,2 jaar over doen om er te raken",
            "Die ster is 4,2 keer verder weg dan de rand van ons zonnestelsel",
        ],
        "antwoord": 0,
        "uitleg": "Een lichtjaar is een afstand, geen tijd: de weg die licht in één jaar aflegt, bijna 9500 miljard kilometer. Je kijkt dus 4,2 jaar in het verleden. Een raket zou er tienduizenden jaren over doen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Volgens de tweede wet van Kepler beweegt een planeet niet altijd even snel. Wanneer gaat hij het snelst?",
        "opties": [
            "Wanneer hij het dichtst bij de zon staat in zijn baan",
            "Wanneer hij het verst van de zon verwijderd staat",
            "Wanneer hij precies tussen de zon en een andere planeet staat",
            "Steeds even snel, want zijn baan is een volmaakte cirkel",
        ],
        "antwoord": 0,
        "uitleg": "De baan is een ellips. Dichter bij de zon is de aantrekkingskracht groter en versnelt de planeet; verder weg vertraagt hij. Kepler schreef het zo op: de lijn zon-planeet veegt in gelijke tijden gelijke oppervlakken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom zie je vanaf de aarde altijd dezelfde kant van de maan?",
        "opties": [
            "De maan draait in precies dezelfde tijd rond zichzelf als rond ons",
            "De maan draait helemaal niet rond haar eigen as, ze staat stil",
            "De achterkant ligt altijd in de schaduw en is daarom niet te zien",
            "Onze dampkring buigt het licht van de achterkant van de maan weg",
        ],
        "antwoord": 0,
        "uitleg": "Dat heet gebonden rotatie: één omwenteling om haar as duurt even lang als één rondje om de aarde, ongeveer 27 dagen. De achterkant krijgt evenveel zon als de voorkant; wij zien ze gewoon nooit.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom heeft de aarde seizoenen?",
        "opties": [
            "Haar as staat scheef, dus de zon staat niet het hele jaar even hoog",
            "Haar baan brengt haar in de zomer veel dichter bij de zon dan in de winter",
            "De zon geeft in de zomermaanden meer warmte af dan in de wintermaanden",
            "De dampkring wordt in de winter dikker en houdt meer zonlicht tegen",
        ],
        "antwoord": 0,
        "uitleg": "De as staat 23,5 graden scheef. Daardoor staat de zon in de zomer hoger en schijnt ze langer. De afstand tot de zon klopt zelfs omgekeerd: begin januari staat de aarde het dichtst bij de zon, midden in onze winter.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een astronaut in het ISS zweeft omdat er op die hoogte geen zwaartekracht meer is.",
        "antwoord": False,
        "uitleg": "Op 400 km hoogte is de zwaartekracht nog ongeveer 90 procent van die op de grond. Het station valt voortdurend naar de aarde toe, maar het gaat zo snel vooruit dat het er altijd naast valt. Dat noemen we vrije val, en in vrije val zweef je.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is Pluto sinds 2006 geen planeet meer?",
        "opties": [
            "Hij heeft de buurt van zijn baan niet leeggeruimd",
            "Hij draait niet rond de zon maar rond de planeet Neptunus",
            "Hij is te klein: een planeet moet minstens zo groot zijn als onze maan",
            "Hij bestaat uit ijs, en een echte planeet moet van steen of gas zijn",
        ],
        "antwoord": 0,
        "uitleg": "De drie voorwaarden zijn: rond de zon draaien, bolvormig zijn door je eigen zwaartekracht, en je baan schoongeveegd hebben. Pluto haalt de eerste twee wel, maar deelt zijn baan met duizenden andere ijsklompen uit de Kuipergordel.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel minuten doet het licht van de zon erover om de aarde te bereiken? Geef een getal.",
        "antwoord": "8",
        "uitleg": "Ongeveer 8 minuten en 20 seconden. Als de zon nu zou uitgaan, zou je dat hier pas acht minuten later merken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op Venus duurt één dag langer dan één jaar. Hoe kan dat?",
        "opties": [
            "Venus draait heel traag om haar as en vrij snel rond de zon",
            "Venus draait heel snel om haar as maar heel traag rond de zon",
            "Venus draait in de verkeerde richting, en dan tellen dagen dubbel",
            "De dikke wolken van Venus maken de dag daar kunstmatig langer",
        ],
        "antwoord": 0,
        "uitleg": "Venus doet 243 aardse dagen over één omwenteling om haar as, en 225 dagen over één rondje rond de zon. Ze draait bovendien achterstevoren: op Venus komt de zon in het westen op.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een ster ziet er blauwachtig uit, een andere roodachtig. Wat weet je dan?",
        "opties": [
            "De blauwe is heter aan de oppervlakte dan de rode",
            "De rode is heter aan de oppervlakte dan de blauwe",
            "De blauwe staat veel dichter bij ons dan de rode ster",
            "De rode is jonger, want jonge sterren beginnen altijd rood",
        ],
        "antwoord": 0,
        "uitleg": "Hoe heter iets gloeit, hoe blauwer het licht. Blauwe sterren zitten rond 20 000 graden, onze gele zon rond 5500, rode sterren rond 3000. Precies zoals de blauwe punt van een gasvlam heter is dan de gele.",
    },
    {
        "type": "waarofniet",
        "vraag": "Op de maan zou je een ontploffing naast je niet kunnen horen.",
        "antwoord": True,
        "uitleg": "Geluid is een trilling die door lucht, water of vaste stof reist. De maan heeft geen dampkring, dus er is niets om de trilling door te geven. Licht heeft dat niet nodig: dat zie je wel.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is Jupiter, met al zijn waterstof, nooit een ster geworden?",
        "opties": [
            "Zijn massa is te klein om kernfusie op gang te brengen",
            "Hij draait te snel om zijn as om vanbinnen warm te worden",
            "Hij staat te ver van de zon, en daar blijft het altijd te koud",
            "Hij bestaat uit de verkeerde soort waterstof om te kunnen branden",
        ],
        "antwoord": 0,
        "uitleg": "Om waterstof te laten samensmelten heb je een enorme druk in de kern nodig. Daarvoor moet een bol ongeveer 80 keer zwaarder zijn dan Jupiter. Jupiter is wel de zwaarste planeet: alle andere planeten samen wegen minder.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een steen uit de ruimte die de grond haalt, heet een meteoriet. Hoe heet de lichtstreep die je in de lucht ziet?",
        "opties": [
            "Een meteoor",
            "Een meteoroïde",
            "Een komeet",
            "Een asteroïde",
        ],
        "antwoord": 0,
        "uitleg": "Drie woorden voor drie momenten: een meteoroïde is de steen in de ruimte, een meteoor is de lichtstreep terwijl hij door de lucht schiet, een meteoriet is wat er op de grond terechtkomt. De streep komt van de gloeiend hete lucht die door de klap samengeperst wordt.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een zonsverduistering zou elke nieuwe maan plaatsvinden als de maanbaan niet scheef stond.",
        "antwoord": True,
        "uitleg": "De maanbaan staat ongeveer 5 graden scheef op de baan van de aarde rond de zon. Daardoor schuift de maan meestal net boven of net onder de zon langs. Alleen als ze precies in één lijn staan, krijg je een verduistering.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe meten sterrenkundigen de afstand tot een ster die vrij dichtbij staat?",
        "opties": [
            "Met parallax: de ster lijkt te verschuiven als de aarde verhuist",
            "Met een radarsignaal dat op de ster weerkaatst en terugkomt",
            "Door te tellen hoeveel jaar het licht van die ster oud lijkt",
            "Door te meten hoe sterk de zwaartekracht van die ster hier trekt",
        ],
        "antwoord": 0,
        "uitleg": "Kijk met één oog en dan met het andere naar je vinger: hij lijkt te verspringen. Hetzelfde doet de aarde in een half jaar, aan de andere kant van haar baan. Hoe kleiner het verspringen, hoe verder de ster. Radar is nutteloos: het signaal zou jaren onderweg zijn en veel te zwak terugkomen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat gebeurt er binnen enkele miljarden jaren met onze zon als haar waterstof op raakt?",
        "opties": [
            "Ze zwelt op tot een rode reus en laat daarna een witte dwerg achter",
            "Ze ontploft als een supernova en laat een zwart gat achter",
            "Ze dooft langzaam uit en blijft als een koude gasbol hangen",
            "Ze trekt samen tot een neutronenster ter grootte van een stad",
        ],
        "antwoord": 0,
        "uitleg": "Een supernova, een neutronenster of een zwart gat zijn weggelegd voor veel zwaardere sterren. Onze zon is daarvoor te licht: ze zwelt op tot voorbij de baan van Venus en schrompelt daarna ineen tot een gloeiend heet bolletje ter grootte van de aarde.",
    },
    {
        "type": "waarofniet",
        "vraag": "De ringen van Saturnus zijn een vaste, gesloten schijf.",
        "antwoord": False,
        "uitleg": "Het zijn miljarden losse brokken ijs en steen, van een zandkorrel tot een huis groot, die elk hun eigen rondje om Saturnus draaien. Van hier lijken ze één gladde schijf. Ze zijn ook verbazend dun: vaak maar tientallen meters dik.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe vinden sterrenkundigen de meeste planeten bij andere sterren?",
        "opties": [
            "Ze meten hoe de ster even iets minder fel wordt als de planeet ervoor schuift",
            "Ze fotograferen de planeet rechtstreeks met een heel grote telescoop",
            "Ze vangen het licht op dat de planeet zelf de ruimte in stuurt",
            "Ze luisteren naar de radiogolven die zo'n planeet voortdurend uitzendt",
        ],
        "antwoord": 0,
        "uitleg": "Dat heet de overgangsmethode. De ster wordt een fractie van een procent zwakker, telkens als de planeet ervoor passeert, en dat herhaalt zich regelmatig. Rechtstreeks fotograferen lukt maar zelden: de ster overstraalt de planeet volledig.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat veroorzaakt eb en vloed op aarde?",
        "opties": [
            "De aantrekkingskracht van vooral de maan, en in mindere mate de zon",
            "De wind die het zeewater twee keer per dag heen en weer duwt",
            "Het draaien van de aarde, waardoor het water naar de rand slingert",
            "Het smelten en weer aangroeien van het ijs op de twee polen",
        ],
        "antwoord": 0,
        "uitleg": "De maan trekt harder aan de kant van de aarde die naar haar toe ligt dan aan de andere kant. Daardoor rekt de waterlaag uit tot twee bulten, en draait de aarde er in 24 uur onderdoor. De zon trekt ook mee: staan zon en maan op één lijn, dan krijg je springtij.",
    },
    {
        "type": "invultekst",
        "vraag": "Op de maan weegt alles ongeveer een zoveelste van wat het op aarde weegt. Vul in: één ...",
        "antwoord": "zesde",
        "uitleg": "De maan is veel lichter en kleiner, dus haar zwaartekracht is ongeveer zes keer zwakker. Daarom huppelden de Apollo-astronauten: stappen lukt niet goed als je jezelf bij elke stap de lucht in duwt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is de asteroïdengordel tussen Mars en Jupiter?",
        "opties": [
            "Brokstukken die nooit tot één planeet zijn samengegroeid",
            "De resten van een planeet die daar ooit uit elkaar gespat is",
            "Een ring van stof die Jupiter uit zijn eigen dampkring blaast",
            "Kometen die in een vaste rij achter elkaar rond de zon trekken",
        ],
        "antwoord": 0,
        "uitleg": "De zwaartekracht van Jupiter roerde het daar zo hard door elkaar dat de brokken elkaar te hard raakten om samen te klitten. Alles samen wegen ze nog geen vier procent van onze maan, en de afstand tussen twee brokken is gemiddeld honderdduizenden kilometers.",
    },
]
