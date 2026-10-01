# -*- coding: utf-8 -*-
"""Punten, vectoren en afstanden in de ruimte.

Het eerste stuk van het onderdeel "Analytische ruimtemeetkunde" van fiche G3:
alles wat je met vectoren zelf doet. De vergelijkingen van rechten en vlakken
staan in het volgende thema.

Deel 1 is de vector: vrije vector en puntvector, coördinaten, norm, optellen
en vermenigvuldigen met een getal, ontbinden in componenten.
Deel 2 is het scalair product en wat je ermee berekent: loodrechte stand,
hoeken, afstanden, het midden van een lijnstuk en zwaartepunten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een vrije vector?",
        opties=[
            "een richting, een zin en een lengte, zonder vast beginpunt",
            "een pijl die vertrekt vanuit de oorsprong van het assenstelsel",
            "een punt in de ruimte dat je met drie coördinaten beschrijft",
            "een getal dat de afstand tussen twee punten weergeeft",
        ],
        antwoord=0,
        uitleg="Je mag hem overal in de ruimte neerleggen; het blijft dezelfde vector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een puntvector?",
        opties=[
            "de vector van de oorsprong naar een punt",
            "de vector tussen twee willekeurig gekozen punten",
            "een vector die maar één enkele coördinaat heeft",
            "een vector met een lengte die gelijk is aan één",
        ],
        antwoord=0,
        uitleg="Zijn coördinaten zijn precies die van het punt zelf.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel coördinaten heeft een vector in de ruimte? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Eén per as. In het vlak zijn het er twee.",
    ),
    dict(
        type="waarofniet",
        vraag="In een orthonormaal assenstelsel staan de assen loodrecht op elkaar en zijn de eenheden even lang.",
        antwoord=True,
        uitleg="Alleen dan kloppen de formules voor de norm, de afstand en de hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de coördinaten van de vector van A naar B?",
        opties=[
            "de coördinaten van B min die van A",
            "de coördinaten van A min die van B",
            "de coördinaten van A en B bij elkaar opgeteld",
            "het gemiddelde van de coördinaten van A en B",
        ],
        antwoord=0,
        uitleg="Eindpunt min beginpunt. Draai je het om, dan krijg je de tegengestelde vector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de norm van een vector?",
        opties=[
            "zijn lengte",
            "zijn richting in het assenstelsel",
            "zijn grootste coördinaat van de drie",
            "de som van zijn drie coördinaten samen",
        ],
        antwoord=0,
        uitleg="Je berekent ze met de wortel uit de som van de kwadraten van de coördinaten.",
    ),
    dict(
        type="waarofniet",
        vraag="De norm van een vector kan negatief zijn.",
        antwoord=False,
        uitleg="Een lengte is nooit negatief. Alleen de nulvector heeft norm nul.",
    ),
    dict(
        type="invultekst",
        vraag="Een vector heeft als coördinaten drie, nul en vier. Hoe groot is zijn norm? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg="De wortel uit negen plus nul plus zestien, dus de wortel uit vijfentwintig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe tel je twee vectoren op in coördinaten?",
        opties=[
            "coördinaat per coördinaat",
            "door hun normen bij elkaar op te tellen",
            "door de coördinaten kruiselings te vermenigvuldigen",
            "door de grootste coördinaten van beide te nemen",
        ],
        antwoord=0,
        uitleg="De eerste bij de eerste, de tweede bij de tweede, de derde bij de derde.",
    ),
    dict(
        type="waarofniet",
        vraag="De optelling van vectoren is commutatief.",
        antwoord=True,
        uitleg="De volgorde maakt niets uit. Grafisch zie je dat aan de parallellogramregel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het neutraal element voor de optelling van vectoren?",
        opties=[
            "de nulvector",
            "de vector met overal een één als coördinaat",
            "de vector die een lengte van precies één heeft",
            "de tegengestelde van de vector die je optelt",
        ],
        antwoord=0,
        uitleg="Alle coördinaten nul, en optellen verandert dan niets.",
    ),
    dict(
        type="invultekst",
        vraag="Je vermenigvuldigt de vector met coördinaten twee, min één en drie met het getal twee. Wat is de eerste coördinaat van het resultaat? Schrijf het cijfer.",
        antwoord=["4", "vier"],
        uitleg="Elke coördinaat afzonderlijk maal twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het symmetrisch element van een vector bij de optelling?",
        opties=[
            "de tegengestelde vector",
            "de vector met dezelfde lengte en dezelfde zin",
            "de vector die er loodrecht op staat in de ruimte",
            "de nulvector, want die verandert niets eraan",
        ],
        antwoord=0,
        uitleg="Alle coördinaten van teken veranderd. Samen geven ze de nulvector.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vector vermenigvuldigen met een negatief getal keert zijn zin om.",
        antwoord=True,
        uitleg="De richting blijft dezelfde, de pijl wijst de andere kant op en de lengte verandert met de grootte van dat getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een richtingsvector van een rechte?",
        opties=[
            "een vector die evenwijdig is met die rechte",
            "een vector die loodrecht op die rechte staat",
            "een vector die begint in de oorsprong en eindigt op de rechte",
            "de vector tussen de twee snijpunten met de assen",
        ],
        antwoord=0,
        uitleg="Hij geeft de richting aan waarin de rechte loopt. Elk veelvoud ervan is ook een richtingsvector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat je een vector ontbindt in zijn componenten?",
        opties=[
            "je schrijft hem als een som van vectoren langs de assen",
            "je deelt hem in gelijke stukken op langs zijn eigen richting",
            "je berekent zijn lengte uit de drie gegeven coördinaten",
            "je zoekt alle vectoren die er loodrecht op staan",
        ],
        antwoord=0,
        uitleg="Elke coördinaat is de lengte van één component. Dat kan grafisch en door te rekenen.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee pijlen met dezelfde coördinaten maar met een ander beginpunt stellen verschillende vrije vectoren voor.",
        antwoord=False,
        uitleg="Het is net dezelfde vrije vector. Het beginpunt doet er niet toe, enkel richting, zin en lengte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe ver liggen de punten met coördinaten één, twee, drie en één, twee, acht uit elkaar? Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg="Alleen de derde coördinaat verschilt, en acht min drie is vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe tel je twee vectoren grafisch op?",
        opties=[
            "je legt de staart van de tweede aan de kop van de eerste",
            "je legt de twee koppen tegen elkaar en meet ertussen",
            "je legt ze evenwijdig naast elkaar en telt de lengtes op",
            "je tekent de vector die er loodrecht tussen past",
        ],
        antwoord=0,
        uitleg="De somvector loopt van de eerste staart naar de laatste kop. Met de parallellogramregel krijg je hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een voorwerp werken twee krachten tegelijk. Hoe vind je de resulterende kracht?",
        opties=[
            "door de twee krachtvectoren op te tellen",
            "door de twee grootten van de krachten op te tellen",
            "door het verschil van de twee krachten te nemen",
            "door de grootste van de twee krachten te kiezen",
        ],
        antwoord=0,
        uitleg="Een kracht heeft een grootte én een richting, dus je telt op als vectoren. Enkel de getallen optellen klopt alleen als ze dezelfde kant op wijzen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat levert het scalair product van twee vectoren op?",
        opties=[
            "een getal",
            "een vector die op beide loodrecht staat",
            "een vector die evenwijdig met de eerste loopt",
            "de hoek tussen de twee vectoren in graden",
        ],
        antwoord=0,
        uitleg="Daarom heet het scalair: de uitkomst is een scalair, geen vector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het scalair product in coördinaten?",
        opties=[
            "je telt de producten van de overeenkomstige coördinaten op",
            "je telt alle coördinaten van beide vectoren bij elkaar op",
            "je vermenigvuldigt de normen van de twee vectoren",
            "je trekt de coördinaten van elkaar af en telt die op",
        ],
        antwoord=0,
        uitleg="Eerste maal eerste, plus tweede maal tweede, plus derde maal derde.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken het scalair product van de vectoren met coördinaten één, twee, drie en twee, nul, één. Schrijf het cijfer.",
        antwoord=["5", "vijf"],
        uitleg="Twee plus nul plus drie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het scalair product van twee vectoren die loodrecht op elkaar staan, is nul.",
        antwoord=True,
        uitleg="Dat is net het criterium voor loodrechte stand, en het werkt ook omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je na of twee rechten loodrecht op elkaar staan?",
        opties=[
            "je berekent het scalair product van hun richtingsvectoren",
            "je berekent de som van hun twee richtingsvectoren",
            "je vergelijkt de normen van hun richtingsvectoren",
            "je kijkt of hun richtingsvectoren toevallig evenwijdig zijn",
        ],
        antwoord=0,
        uitleg="Komt daar nul uit, dan staan ze loodrecht, tenminste in een orthonormaal assenstelsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Het scalair product is commutatief.",
        antwoord=True,
        uitleg="De volgorde van de twee vectoren verandert niets aan de uitkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de hoek tussen twee vectoren?",
        opties=[
            "uit het scalair product gedeeld door het product van de normen",
            "uit de som van de normen gedeeld door het scalair product",
            "uit het verschil van de coördinaten van de twee vectoren",
            "uit het scalair product vermenigvuldigd met de twee normen",
        ],
        antwoord=0,
        uitleg="Die breuk is de cosinus van de hoek. Met de inverse cosinus vind je de hoek zelf.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe ver ligt het punt met coördinaten twee, drie, zes van de oorsprong? Schrijf het cijfer.",
        antwoord=["7", "zeven"],
        uitleg="De wortel uit vier plus negen plus zesendertig, dus de wortel uit negenenveertig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het midden van een lijnstuk?",
        opties=[
            "je neemt het gemiddelde van de coördinaten van de twee uiteinden",
            "je telt de coördinaten van de twee uiteinden gewoon op",
            "je trekt de coördinaten van de twee uiteinden van elkaar af",
            "je deelt de coördinaten van het verste punt door twee",
        ],
        antwoord=0,
        uitleg="Coördinaat per coördinaat optellen en door twee delen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het zwaartepunt van een driehoek is het gemiddelde van de coördinaten van de drie hoekpunten.",
        antwoord=True,
        uitleg="Je telt de drie hoekpunten coördinaat per coördinaat op en deelt door drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je het zwaartepunt van een viervlak?",
        opties=[
            "je deelt de som van de vier hoekpunten door vier",
            "je deelt de som van de vier hoekpunten door drie",
            "je neemt het midden van de langste ribbe ervan",
            "je neemt het zwaartepunt van het grondvlak alleen",
        ],
        antwoord=0,
        uitleg="Hetzelfde recept als bij de driehoek, maar met vier punten in plaats van drie.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de eerste coördinaat van het midden van het lijnstuk tussen de punten twee, vier, zes en vier, acht, tien? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Twee plus vier is zes, gedeeld door twee is drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een normaalvector van een vlak?",
        opties=[
            "een vector die loodrecht op dat vlak staat",
            "een vector die volledig in dat vlak ligt",
            "een vector met een lengte die gelijk is aan één",
            "een vector van de oorsprong naar dat vlak toe",
        ],
        antwoord=0,
        uitleg="Zijn coördinaten lees je af uit de cartesische vergelijking van het vlak.",
    ),
    dict(
        type="waarofniet",
        vraag="Het scalair product van een vector met zichzelf is gelijk aan zijn norm.",
        antwoord=False,
        uitleg="Het is het kwadraat van zijn norm. De norm zelf krijg je er pas uit na worteltrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zie je aan de coördinaten dat twee vectoren evenwijdig zijn?",
        opties=[
            "de ene is een veelvoud van de andere",
            "hun scalair product is gelijk aan nul",
            "ze hebben allebei dezelfde norm gekregen",
            "hun coördinaten tellen samen op tot nul",
        ],
        antwoord=0,
        uitleg="Alle coördinaten verschillen dan met dezelfde factor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de afstand tussen twee punten in de ruimte?",
        opties=[
            "als de norm van de vector tussen die twee punten",
            "als de som van de verschillen van hun coördinaten",
            "als het scalair product van hun twee puntvectoren",
            "als het verschil van de normen van hun puntvectoren",
        ],
        antwoord=0,
        uitleg="Eerst de vector van het ene naar het andere punt, dan zijn lengte.",
    ),
    dict(
        type="waarofniet",
        vraag="Is het scalair product van twee vectoren negatief, dan is de hoek ertussen scherp.",
        antwoord=False,
        uitleg="Dan is de hoek stomp. Bij een scherpe hoek is het scalair product positief, bij een rechte hoek nul.",
    ),
    dict(
        type="invultekst",
        vraag="De drie hoekpunten van een driehoek hebben als eerste coördinaat nul, drie en zes. Wat is de eerste coördinaat van het zwaartepunt? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Nul plus drie plus zes is negen, gedeeld door drie is drie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een drone vliegt eerst drie meter naar het oosten en dan vier meter naar het noorden. Hoe vind je zijn verplaatsing?",
        opties=[
            "als de som van de twee verplaatsingsvectoren",
            "als de som van de twee afgelegde afstanden",
            "als het verschil van de twee verplaatsingen",
            "als het scalair product van de twee richtingen",
        ],
        antwoord=0,
        uitleg="De verplaatsing is vijf meter, niet zeven. De afgelegde weg is wel zeven meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt het scalair product als criterium voor loodrechte stand?",
        opties=[
            "omdat de cosinus van negentig graden nul is",
            "omdat de norm van een vector nooit negatief wordt",
            "omdat loodrechte vectoren altijd dezelfde lengte hebben",
            "omdat de coördinaten van loodrechte vectoren nul zijn",
        ],
        antwoord=0,
        uitleg="Het scalair product is het product van de normen maal die cosinus, en bij een rechte hoek valt alles weg.",
    ),
]
