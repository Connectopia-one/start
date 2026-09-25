# -*- coding: utf-8 -*-
"""De vragen voor "Meetkunde" (✨ Spark, wiskunde).

De vakfiche zet onder meetkunde: de bouwstenen (punt, rechte, hoek), soorten
hoeken, driehoeken en vierhoeken, de merkwaardige lijnen, de hoekensom, de
hoeken bij twee evenwijdige rechten en een snijlijn, de congruentiekenmerken
ZZZ, ZHZ, HZH, ZHH en ZZ90°, de transformaties en de symmetrie.

Metend rekenen (omtrek, oppervlakte, volume, eenheden) staat apart, in
metend_rekenen.py. De fiche zet die twee samen, maar het zijn in het platform
twee hoofdstukken, want samen zou het één lange brok worden.

Deel 1 gaat over herkennen en benoemen. Deel 2 vraagt redeneren: hoeken
uitrekenen uit eigenschappen, en congruentie verantwoorden.

Bij de meeste vragen staat achteraan een tekening tussen dubbele accolades,
bijvoorbeeld {{hoek 130}} of {{vierhoek trapezium}}. Het platform tekent die
zelf; de lijst van alles wat kan staat in components/Tekeningen.tsx. De
vraagtekst blijft zo geschreven dat ze ook zonder de tekening te begrijpen is,
want op de pagina waar ouders meekijken staat alleen de tekst.

Een tekening mag het antwoord niet verklappen. Daarom staat er {{hoek 90 ?}} in
plaats van {{hoek 90}} bij "welke hoek maken twee loodrechte rechten", en
{{merkwaardig bissectrice stil}} in plaats van de versie met het woord erbij.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noem je een hoek die precies past in de hoek van een blad papier? {{hoek 90 ?}}",
        opties=["Een rechte hoek", "Een scherpe hoek", "Een stompe hoek"],
        antwoord=0,
        uitleg="De hoek van een blad is 90°, en dat heet een rechte hoek. Kleiner dan 90° is scherp, groter dan 90° is stomp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hoek van 130° is een … {{hoek 130}}",
        opties=["stompe hoek", "scherpe hoek", "gestrekte hoek"],
        antwoord=0,
        uitleg="Stomp is meer dan 90° en minder dan 180°. Een gestrekte hoek is precies 180°, dus een rechte lijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden is een gestrekte hoek? {{hoek 180 ?}}",
        antwoord="180",
        uitleg="Een gestrekte hoek is 180°: de twee benen liggen in elkaars verlengde en vormen samen een rechte lijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van de hoeken van een driehoek, in graden? {{driehoek ongelijkbenig}}",
        antwoord="180",
        uitleg="In elke driehoek is de hoekensom 180°, of hij nu scherp, recht of stomp is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee hoeken van een driehoek zijn 50° en 60°. Hoe groot is de derde? {{driehoek 50-60-?}}",
        opties=["70°", "80°", "110°"],
        antwoord=0,
        uitleg="180 − 50 − 60 = 70°. De hoekensom van een driehoek is altijd 180°.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van de hoeken van een vierhoek, in graden? {{vierhoek trapezium}}",
        antwoord="360",
        uitleg="360°. Je kan elke vierhoek met één diagonaal in twee driehoeken verdelen: 2 × 180° = 360°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je een driehoek met drie gelijke zijden? {{driehoek gelijkzijdig}}",
        opties=["Gelijkzijdig", "Gelijkbenig", "Ongelijkbenig"],
        antwoord=0,
        uitleg="Gelijkzijdig: drie gelijke zijden, en dus ook drie gelijke hoeken van 60°. Gelijkbenig heeft er twee gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden is elke hoek van een gelijkzijdige driehoek? {{driehoek gelijkzijdig}}",
        antwoord="60",
        uitleg="De drie hoeken zijn even groot en samen 180°, dus elk 180 : 3 = 60°.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een gelijkbenige driehoek heet de hoek tussen de twee gelijke zijden de … {{driehoek gelijkbenig}}",
        opties=["tophoek", "basishoek", "buitenhoek"],
        antwoord=0,
        uitleg="De twee gelijke zijden heten de benen, de hoek ertussen is de tophoek. De twee andere hoeken liggen op de basis en heten de basishoeken; die zijn even groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de langste zijde van een rechthoekige driehoek? {{driehoek rechthoekig}}",
        opties=["De schuine zijde", "De rechthoekszijde", "De basis"],
        antwoord=0,
        uitleg="De schuine zijde ligt tegenover de rechte hoek en is altijd de langste. De twee andere zijden heten rechthoekszijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vierhoek waarvan beide paren overstaande zijden evenwijdig zijn, heet een … {{vierhoek parallellogram}}",
        opties=["parallellogram", "trapezium", "ruit"],
        antwoord=0,
        uitleg="Een parallellogram heeft twee paar evenwijdige zijden. Een trapezium heeft er maar één paar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ruit heeft vier even lange zijden. {{vierhoek ruit}}",
        antwoord=True,
        uitleg="Juist. Een ruit is een parallellogram met vier gelijke zijden. De hoeken hoeven niet recht te zijn; zijn ze dat wel, dan is het een vierkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de lijn van het middelpunt van een cirkel naar de rand? {{cirkeldeel straal stil}}",
        opties=["De straal", "De diameter", "De koorde"],
        antwoord=0,
        uitleg="De straal gaat van het middelpunt naar de rand. De diameter gaat helemaal door de cirkel via het middelpunt en is dus dubbel zo lang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cirkel heeft een straal van 6 cm. Hoe lang is de diameter? {{maat cirkel straal 6}}",
        opties=["12 cm", "3 cm", "6 cm"],
        antwoord=0,
        uitleg="De diameter is twee keer de straal: 2 × 6 = 12 cm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee rechten staan loodrecht op elkaar. Welke hoek maken ze? {{hoek 90 ?}}",
        opties=["90°", "45°", "180°"],
        antwoord=0,
        uitleg="Loodrecht betekent een hoek van 90°.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee evenwijdige rechten snijden elkaar nooit.",
        antwoord=True,
        uitleg="Juist, dat is precies wat strikt evenwijdig betekent: ze houden overal dezelfde afstand en komen elkaar nooit tegen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel symmetrieassen heeft een vierkant? {{vierhoek vierkant}}",
        antwoord="4",
        uitleg="Vier: de twee middelloodlijnen van de zijden en de twee diagonalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel symmetrieassen heeft een gewone rechthoek die geen vierkant is? {{vierhoek rechthoek}}",
        opties=["2", "4", "1"],
        antwoord=0,
        uitleg="Twee: de lijnen door het midden van de overstaande zijden. De diagonalen zijn bij een rechthoek géén symmetrieassen, anders zou hij een vierkant zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een figuur schuift een eindje opzij, zonder te draaien of te spiegelen. Welke transformatie is dat? {{beweging translatie}}",
        opties=["Een translatie", "Een rotatie", "Een spiegeling"],
        antwoord=0,
        uitleg="Een translatie is een verschuiving over een vector: elk punt schuift even ver in dezelfde richting.",
    ),
    dict(
        type="waarofniet",
        vraag="Na een spiegeling is de figuur even groot als daarvoor. {{beweging spiegeling}}",
        antwoord=True,
        uitleg="Juist. Translatie, rotatie en spiegeling behouden alle drie de lengtes en de hoeken. Het beeld is dus congruent met de oorspronkelijke figuur.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Twee rechten snijden elkaar. Eén hoek is 70°. Hoe groot is de hoek er recht tegenover? {{snijlijn 70}}",
        opties=["70°", "110°", "20°"],
        antwoord=0,
        uitleg="Overstaande hoeken zijn even groot. De hoek ernaast is de nevenhoek en is 180 − 70 = 110°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hoek is 70°. Hoe groot is zijn nevenhoek? {{snijlijn 70 neven}}",
        opties=["110°", "20°", "70°"],
        antwoord=0,
        uitleg="Twee nevenhoeken vormen samen een gestrekte hoek: 180 − 70 = 110°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee evenwijdige rechten worden gesneden door een derde rechte. Wat weet je over de overeenkomstige hoeken? {{evenwijdig 65}}",
        opties=["Ze zijn even groot", "Ze zijn samen 180°", "Ze zijn samen 90°"],
        antwoord=0,
        uitleg="Bij evenwijdige rechten zijn overeenkomstige hoeken gelijk, en verwisselende binnenhoeken ook. Binnenhoeken aan dezelfde kant van de snijlijn zijn samen 180°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee evenwijdige rechten, een snijlijn, en een binnenhoek van 65°. Hoe groot is de binnenhoek aan dezelfde kant van de snijlijn? {{evenwijdig 65 binnen}}",
        opties=["115°", "65°", "25°"],
        antwoord=0,
        uitleg="Binnenhoeken aan dezelfde kant zijn samen 180°: 180 − 65 = 115°.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een gelijkbenige driehoek is de tophoek 40°. Hoe groot is elke basishoek? {{driehoek gelijkbenig}}",
        opties=["70°", "40°", "140°"],
        antwoord=0,
        uitleg="De twee basishoeken zijn even groot en samen 180 − 40 = 140°, dus elk 70°.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een gelijkbenige driehoek is een basishoek 50°. Hoe groot is de tophoek? {{driehoek gelijkbenig}}",
        opties=["80°", "50°", "130°"],
        antwoord=0,
        uitleg="Beide basishoeken zijn 50°, samen 100°. De tophoek is 180 − 100 = 80°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie hoeken van een vierhoek zijn 90°, 100° en 85°. Hoe groot is de vierde? {{vierhoek trapezium}}",
        opties=["85°", "95°", "75°"],
        antwoord=0,
        uitleg="De hoekensom van een vierhoek is 360°: 360 − 90 − 100 − 85 = 85°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de lijn uit een hoekpunt die de hoek in twee gelijke stukken verdeelt? {{merkwaardig bissectrice stil}}",
        opties=["De bissectrice", "De hoogtelijn", "De zwaartelijn"],
        antwoord=0,
        uitleg="De bissectrice deelt een hoek middendoor. De hoogtelijn staat loodrecht op de overstaande zijde, de zwaartelijn gaat naar het midden van die zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke merkwaardige lijn staat loodrecht op een zijde en gaat door het midden van die zijde? {{merkwaardig middelloodlijn stil}}",
        opties=["De middelloodlijn", "De hoogtelijn", "De bissectrice"],
        antwoord=0,
        uitleg="De middelloodlijn van een zijde: loodrecht én door het midden. Ze hoeft niet door een hoekpunt te gaan, en daarin verschilt ze van de hoogtelijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee driehoeken hebben drie paar even lange zijden. Welk congruentiekenmerk is dat?",
        opties=["ZZZ", "ZHZ", "HZH"],
        antwoord=0,
        uitleg="ZZZ: zijde-zijde-zijde. Zijn de drie zijden gelijk, dan liggen de hoeken ook vast en zijn de driehoeken congruent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee driehoeken hebben twee even lange zijden en dezelfde ingesloten hoek. Welk kenmerk is dat?",
        opties=["ZHZ", "ZZZ", "ZHH"],
        antwoord=0,
        uitleg="ZHZ: zijde-hoek-zijde. Let erop dat de hoek tússen de twee zijden ligt; ligt hij ergens anders, dan geldt dit kenmerk niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee driehoeken met drie gelijke hoeken zijn altijd congruent.",
        antwoord=False,
        uitleg="Nee. Twee gelijkzijdige driehoeken met zijden van 2 cm en van 5 cm hebben alle drie de hoeken van 60°, maar ze zijn niet even groot. Gelijke hoeken geven dezelfde vorm, niet dezelfde grootte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat mag je besluiten als je aantoont dat twee driehoeken congruent zijn?",
        opties=[
            "Alle overeenkomstige zijden en hoeken zijn gelijk",
            "Enkel de zijden zijn gelijk",
            "Ze hebben dezelfde oppervlakte maar niet dezelfde vorm",
        ],
        antwoord=0,
        uitleg="Congruent betekent volledig gelijk van vorm én grootte. Daarom gebruik je congruentie net om aan te tonen dat twee zijden even lang of twee hoeken even groot zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een figuur draait een kwartslag rond een punt. Welke transformatie is dat? {{beweging rotatie}}",
        opties=["Een rotatie over 90°", "Een translatie", "Een puntspiegeling"],
        antwoord=0,
        uitleg="Een rotatie rond een centrum over een hoek. Een kwartslag is 90°, een halve draai is 180° en dat is hetzelfde als een spiegeling om dat punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap blijft NIET noodzakelijk behouden bij een spiegeling om een rechte? {{beweging spiegeling}}",
        opties=[
            "De draairichting waarin je de hoekpunten leest",
            "De lengte van elk lijnstuk",
            "De grootte van elke hoek",
        ],
        antwoord=0,
        uitleg="Lengtes, hoeken en evenwijdigheid blijven, maar een spiegeling keert de richting om: wat met de klok mee gelezen werd, lees je nadien tegen de klok in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel symmetrieassen heeft een gelijkzijdige driehoek? {{driehoek gelijkzijdig}}",
        antwoord="3",
        uitleg="Drie, één uit elk hoekpunt naar het midden van de overstaande zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke figuur heeft wél een symmetriemiddelpunt maar géén symmetrieas?",
        opties=[
            "Een parallellogram dat geen ruit of rechthoek is",
            "Een gelijkbenige driehoek",
            "Een vierkant",
        ],
        antwoord=0,
        uitleg="Zo'n parallellogram valt op zichzelf na een halve draai rond zijn middelpunt, maar je kan hem niet dubbelvouwen. Een gelijkbenige driehoek heeft juist wel een as en geen middelpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een parallellogram is één hoek 110°. Hoe groot is de hoek ernaast? {{vierhoek parallellogram}}",
        opties=["70°", "110°", "90°"],
        antwoord=0,
        uitleg="In een parallellogram zijn overstaande hoeken gelijk en aanliggende hoeken samen 180°: 180 − 110 = 70°.",
    ),
    dict(
        type="waarofniet",
        vraag="De diagonalen van een ruit staan loodrecht op elkaar. {{vierhoek ruit}}",
        antwoord=True,
        uitleg="Juist, en ze delen elkaar bovendien middendoor. Bij een gewoon parallellogram delen de diagonalen elkaar wel middendoor, maar staan ze niet loodrecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een driehoek heeft hoeken van 90° en 45°. Wat weet je nog meer? {{driehoek 90-45-?}}",
        opties=[
            "Hij is rechthoekig én gelijkbenig",
            "Hij is gelijkzijdig",
            "Hij is stomphoekig",
        ],
        antwoord=0,
        uitleg="De derde hoek is 180 − 90 − 45 = 45°. Twee gelijke hoeken betekent twee gelijke zijden, dus hij is rechthoekig en gelijkbenig tegelijk.",
    ),
]
