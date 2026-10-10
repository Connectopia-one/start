# -*- coding: utf-8 -*-
"""Punten, vectoren en afstanden in de ruimte.

Het eerste stuk van het onderdeel "Analytische ruimtemeetkunde" van fiche G3:
alles wat je met vectoren zelf doet. De vergelijkingen van rechten en vlakken
staan in het volgende thema.

Een vector schrijven we \\(\\vec{v}\\), de vector van A naar B
\\(\\overrightarrow{AB}\\), en de norm \\(\\|\\vec{v}\\|\\).

Deel 1 is de vector: vrije vector en puntvector, coördinaten, norm, optellen
en vermenigvuldigen met een getal, ontbinden in componenten.
Deel 2 is het scalair product en wat je ermee berekent: loodrechte stand,
hoeken, afstanden, het midden van een lijnstuk en zwaartepunten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is een vrije vector?",
        opties=[
            r"een richting, een zin en een lengte, zonder vast beginpunt",
            r"een pijl die vertrekt vanuit de oorsprong van het assenstelsel",
            r"een punt in de ruimte dat je met drie coördinaten beschrijft",
            r"een getal dat de afstand tussen twee punten weergeeft",
        ],
        antwoord=0,
        uitleg=r"Je mag hem overal in de ruimte neerleggen; het blijft dezelfde vector.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de puntvector van een punt \(P\)?",
        opties=[
            r"\(\overrightarrow{OP}\), de vector van de oorsprong naar \(P\)",
            r"de vector tussen twee willekeurig gekozen punten",
            r"een vector die maar één enkele coördinaat heeft",
            r"een vector met \(\|\vec{v}\| = 1\)",
        ],
        antwoord=0,
        uitleg=r"Zijn coördinaten zijn precies die van het punt zelf.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel coördinaten heeft een vector in de ruimte? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"Eén per as. In het vlak zijn het er twee.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een orthonormaal assenstelsel staan de assen loodrecht op elkaar en zijn de eenheden even lang.",
        antwoord=True,
        uitleg=r"Alleen dan kloppen de formules voor de norm, de afstand en de hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de coördinaten van \(\overrightarrow{AB}\)?",
        opties=[
            r"\(\overrightarrow{AB} = (x_{B} - x_{A},\ y_{B} - y_{A},\ z_{B} - z_{A})\)",
            r"\(\overrightarrow{AB} = (x_{A} - x_{B},\ y_{A} - y_{B},\ z_{A} - z_{B})\)",
            r"\(\overrightarrow{AB} = (x_{A} + x_{B},\ y_{A} + y_{B},\ z_{A} + z_{B})\)",
            r"het gemiddelde van de coördinaten van \(A\) en \(B\)",
        ],
        antwoord=0,
        uitleg=r"Eindpunt min beginpunt. Draai je het om, dan krijg je \(\overrightarrow{BA} = -\overrightarrow{AB}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de norm \(\|\vec{v}\|\) van een vector?",
        opties=[
            r"zijn lengte",
            r"zijn richting in het assenstelsel",
            r"zijn grootste coördinaat van de drie",
            r"de som van zijn drie coördinaten samen",
        ],
        antwoord=0,
        uitleg=r"Je berekent ze als \(\|\vec{v}\| = \sqrt{v_{1}^{2} + v_{2}^{2} + v_{3}^{2}}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De norm van een vector kan negatief zijn.",
        antwoord=False,
        uitleg=r"Een lengte is nooit negatief: \(\|\vec{v}\| \ge 0\). Alleen \(\vec{0}\) heeft norm nul.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\|\vec{v}\|\) voor \(\vec{v}(3, 0, 4)\). Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg=r"\(\sqrt{9 + 0 + 16} = \sqrt{25} = 5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe tel je twee vectoren op in coördinaten?",
        opties=[
            r"\(\vec{u} + \vec{v} = (u_{1} + v_{1},\ u_{2} + v_{2},\ u_{3} + v_{3})\)",
            r"door hun normen bij elkaar op te tellen",
            r"door de coördinaten kruiselings te vermenigvuldigen",
            r"door de grootste coördinaten van beide te nemen",
        ],
        antwoord=0,
        uitleg=r"Coördinaat per coördinaat: de eerste bij de eerste, en zo verder.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\vec{u} + \vec{v} = \vec{v} + \vec{u}\).",
        antwoord=True,
        uitleg=r"De optelling van vectoren is commutatief. Grafisch zie je dat aan de parallellogramregel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het neutraal element voor de optelling van vectoren?",
        opties=[
            r"de nulvector \(\vec{0}\)",
            r"de vector \((1, 1, 1)\)",
            r"een vector met \(\|\vec{v}\| = 1\)",
            r"de tegengestelde van de vector die je optelt",
        ],
        antwoord=0,
        uitleg=r"Alle coördinaten nul, en \(\vec{v} + \vec{0} = \vec{v}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken de eerste coördinaat van \(2 \cdot \vec{v}\) voor \(\vec{v}(2, -1, 3)\). Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg=r"Elke coördinaat afzonderlijk maal \(2\), dus \(2 \cdot 2 = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het symmetrisch element van \(\vec{v}\) bij de optelling?",
        opties=[
            r"\(-\vec{v}\), de tegengestelde vector",
            r"de vector met dezelfde lengte en dezelfde zin",
            r"de vector die er loodrecht op staat in de ruimte",
            r"de nulvector \(\vec{0}\), want die verandert niets eraan",
        ],
        antwoord=0,
        uitleg=r"Alle coördinaten van teken veranderd, en \(\vec{v} + (-\vec{v}) = \vec{0}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In \(k \cdot \vec{v}\) met \(k < 0\) keert de zin van de vector om.",
        antwoord=True,
        uitleg=r"De richting blijft dezelfde, de pijl wijst de andere kant op, en \(\|k \cdot \vec{v}\| = |k| \cdot \|\vec{v}\|\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een richtingsvector van een rechte?",
        opties=[
            r"een vector die evenwijdig is met die rechte",
            r"een vector die loodrecht op die rechte staat",
            r"een vector die begint in de oorsprong en eindigt op de rechte",
            r"de vector tussen de twee snijpunten met de assen",
        ],
        antwoord=0,
        uitleg=r"Hij geeft de richting aan waarin de rechte loopt. Elk veelvoud \(k \cdot \vec{v}\) met \(k \neq 0\) is ook een richtingsvector.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent het dat je een vector ontbindt in zijn componenten?",
        opties=[
            r"je schrijft hem als \(\vec{v} = v_{1}\vec{e_{x}} + v_{2}\vec{e_{y}} + v_{3}\vec{e_{z}}\)",
            r"je deelt hem in gelijke stukken op langs zijn eigen richting",
            r"je berekent \(\|\vec{v}\|\) uit de drie gegeven coördinaten",
            r"je zoekt alle vectoren die er loodrecht op staan",
        ],
        antwoord=0,
        uitleg=r"Elke coördinaat is de lengte van één component langs een as. Dat kan grafisch en door te rekenen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee pijlen met dezelfde coördinaten maar met een ander beginpunt stellen verschillende vrije vectoren voor.",
        antwoord=False,
        uitleg=r"Het is net dezelfde vrije vector. Het beginpunt doet er niet toe, enkel richting, zin en lengte.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe ver liggen \(A(1, 2, 3)\) en \(B(1, 2, 8)\) uit elkaar? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg=r"\(\overrightarrow{AB} = (0, 0, 5)\), dus \(\|\overrightarrow{AB}\| = 5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe tel je twee vectoren grafisch op?",
        opties=[
            r"je legt de staart van de tweede aan de kop van de eerste",
            r"je legt de twee koppen tegen elkaar en meet ertussen",
            r"je legt ze evenwijdig naast elkaar en telt de lengtes op",
            r"je tekent de vector die er loodrecht tussen past",
        ],
        antwoord=0,
        uitleg=r"De somvector loopt van de eerste staart naar de laatste kop. Met de parallellogramregel krijg je hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op een voorwerp werken twee krachten tegelijk. Hoe vind je de resulterende kracht?",
        opties=[
            r"als \(\vec{F_{1}} + \vec{F_{2}}\)",
            r"door de twee grootten van de krachten op te tellen",
            r"als \(\vec{F_{1}} - \vec{F_{2}}\)",
            r"door de grootste van de twee krachten te kiezen",
        ],
        antwoord=0,
        uitleg=r"Een kracht heeft een grootte én een richting, dus je telt op als vectoren. Enkel de getallen optellen klopt alleen als ze dezelfde kant op wijzen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat levert het scalair product \(\vec{u} \cdot \vec{v}\) op?",
        opties=[
            r"een getal",
            r"een vector die op beide loodrecht staat",
            r"een vector die evenwijdig met de eerste loopt",
            r"de hoek tussen de twee vectoren in graden",
        ],
        antwoord=0,
        uitleg=r"Daarom heet het scalair: de uitkomst is een scalair, geen vector.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je \(\vec{u} \cdot \vec{v}\) in coördinaten?",
        opties=[
            r"\(\vec{u} \cdot \vec{v} = u_{1}v_{1} + u_{2}v_{2} + u_{3}v_{3}\)",
            r"je telt alle coördinaten van beide vectoren bij elkaar op",
            r"\(\vec{u} \cdot \vec{v} = \|\vec{u}\| \cdot \|\vec{v}\|\)",
            r"je trekt de coördinaten van elkaar af en telt die op",
        ],
        antwoord=0,
        uitleg=r"Eerste maal eerste, plus tweede maal tweede, plus derde maal derde.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\vec{u} \cdot \vec{v}\) voor \(\vec{u}(1, 2, 3)\) en \(\vec{v}(2, 0, 1)\). Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg=r"\(1 \cdot 2 + 2 \cdot 0 + 3 \cdot 1 = 2 + 0 + 3 = 5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0\).",
        antwoord=True,
        uitleg=r"Dat is net het criterium voor loodrechte stand, en het werkt in de twee richtingen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ga je na of twee rechten loodrecht op elkaar staan?",
        opties=[
            r"je berekent het scalair product van hun richtingsvectoren",
            r"je berekent de som van hun twee richtingsvectoren",
            r"je vergelijkt de normen van hun richtingsvectoren",
            r"je kijkt of hun richtingsvectoren toevallig evenwijdig zijn",
        ],
        antwoord=0,
        uitleg=r"Komt daar \(0\) uit, dan staan ze loodrecht, tenminste in een orthonormaal assenstelsel.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}\).",
        antwoord=True,
        uitleg=r"Het scalair product is commutatief: de volgorde verandert niets aan de uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de hoek \(\theta\) tussen twee vectoren?",
        opties=[
            r"\(\cos \theta = \dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \cdot \|\vec{v}\|}\)",
            r"\(\cos \theta = \dfrac{\|\vec{u}\| + \|\vec{v}\|}{\vec{u} \cdot \vec{v}}\)",
            r"uit het verschil van de coördinaten van de twee vectoren",
            r"\(\cos \theta = \vec{u} \cdot \vec{v} \cdot \|\vec{u}\| \cdot \|\vec{v}\|\)",
        ],
        antwoord=0,
        uitleg=r"Met \(\theta = \arccos\) van die breuk vind je de hoek zelf.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe ver ligt \(P(2, 3, 6)\) van de oorsprong? Schrijf het cijfer.",
        antwoord=["7", "zeven"],
        uitleg=r"\(\sqrt{4 + 9 + 36} = \sqrt{49} = 7\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je het midden \(M\) van het lijnstuk \([AB]\)?",
        opties=[
            r"\(M\left(\dfrac{x_{A} + x_{B}}{2},\ \dfrac{y_{A} + y_{B}}{2},\ \dfrac{z_{A} + z_{B}}{2}\right)\)",
            r"je telt de coördinaten van de twee uiteinden gewoon op",
            r"je trekt de coördinaten van de twee uiteinden van elkaar af",
            r"je deelt de coördinaten van het verste punt door \(2\)",
        ],
        antwoord=0,
        uitleg=r"Coördinaat per coördinaat optellen en door twee delen: het gemiddelde dus.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het zwaartepunt van een driehoek is het gemiddelde van de coördinaten van de drie hoekpunten.",
        antwoord=True,
        uitleg=r"Je telt de drie hoekpunten coördinaat per coördinaat op en deelt door \(3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe vind je het zwaartepunt van een viervlak?",
        opties=[
            r"je deelt de som van de vier hoekpunten door \(4\)",
            r"je deelt de som van de vier hoekpunten door \(3\)",
            r"je neemt het midden van de langste ribbe ervan",
            r"je neemt het zwaartepunt van het grondvlak alleen",
        ],
        antwoord=0,
        uitleg=r"Hetzelfde recept als bij de driehoek, maar met vier punten in plaats van drie.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de eerste coördinaat van het midden van \([AB]\) met \(A(2, 4, 6)\) en \(B(4, 8, 10)\)? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"\(\dfrac{2 + 4}{2} = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een normaalvector van een vlak?",
        opties=[
            r"een vector die loodrecht op dat vlak staat",
            r"een vector die volledig in dat vlak ligt",
            r"een vector met \(\|\vec{n}\| = 1\)",
            r"een vector van de oorsprong naar dat vlak toe",
        ],
        antwoord=0,
        uitleg=r"Zijn coördinaten lees je af uit de cartesische vergelijking van het vlak.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Er geldt \(\vec{v} \cdot \vec{v} = \|\vec{v}\|\).",
        antwoord=False,
        uitleg=r"Het is \(\vec{v} \cdot \vec{v} = \|\vec{v}\|^{2}\). De norm zelf krijg je er pas uit na worteltrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe zie je aan de coördinaten dat twee vectoren evenwijdig zijn?",
        opties=[
            r"\(\vec{u} = k \cdot \vec{v}\) voor een getal \(k\)",
            r"\(\vec{u} \cdot \vec{v} = 0\)",
            r"\(\|\vec{u}\| = \|\vec{v}\|\)",
            r"hun coördinaten tellen samen op tot \(0\)",
        ],
        antwoord=0,
        uitleg=r"Alle coördinaten verschillen dan met dezelfde factor \(k\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bereken je de afstand \(|AB|\) tussen twee punten in de ruimte?",
        opties=[
            r"\(|AB| = \|\overrightarrow{AB}\|\)",
            r"als de som van de verschillen van hun coördinaten",
            r"als het scalair product van hun twee puntvectoren",
            r"als \(\|\overrightarrow{OB}\| - \|\overrightarrow{OA}\|\)",
        ],
        antwoord=0,
        uitleg=r"Eerst de vector van het ene naar het andere punt, dan zijn lengte.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Is \(\vec{u} \cdot \vec{v} < 0\), dan is de hoek tussen de twee vectoren scherp.",
        antwoord=False,
        uitleg=r"Dan is de hoek stomp. Bij een scherpe hoek is \(\vec{u} \cdot \vec{v} > 0\), bij een rechte hoek \(0\).",
    ),
    dict(
        type="invultekst",
        vraag=r"De eerste coördinaten van de drie hoekpunten van een driehoek zijn \(0\), \(3\) en \(6\). Wat is de eerste coördinaat van het zwaartepunt? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg=r"\(\dfrac{0 + 3 + 6}{3} = 3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een drone vliegt eerst \(3\) meter naar het oosten en dan \(4\) meter naar het noorden. Hoe vind je zijn verplaatsing?",
        opties=[
            r"als de som van de twee verplaatsingsvectoren",
            r"als de som van de twee afgelegde afstanden",
            r"als het verschil van de twee verplaatsingen",
            r"als het scalair product van de twee richtingen",
        ],
        antwoord=0,
        uitleg=r"De verplaatsing is \(\sqrt{9 + 16} = 5\) meter, niet \(7\). De afgelegde weg is wel \(7\) meter.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom werkt het scalair product als criterium voor loodrechte stand?",
        opties=[
            r"omdat \(\cos 90^{\circ} = 0\)",
            r"omdat de norm van een vector nooit negatief wordt",
            r"omdat loodrechte vectoren altijd dezelfde lengte hebben",
            r"omdat de coördinaten van loodrechte vectoren nul zijn",
        ],
        antwoord=0,
        uitleg=r"Er geldt \(\vec{u} \cdot \vec{v} = \|\vec{u}\| \cdot \|\vec{v}\| \cdot \cos \theta\), en bij een rechte hoek valt alles weg.",
    ),
]
