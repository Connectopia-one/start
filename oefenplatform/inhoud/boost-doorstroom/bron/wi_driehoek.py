# -*- coding: utf-8 -*-
"""De vragen voor "Sinusregel, cosinusregel en vectoren".

Uit de bouwsteen Meetkunde en metend rekenen: de som van de hoeken in een
driehoek, de sinusregel en de cosinusregel in een willekeurige driehoek en het
oplossen van zo'n driehoek, en daarnaast de vectoren: richting, zin en grootte,
de nulvector en de tegengestelde vector, de som, het verschil en de
vermenigvuldiging met een reëel getal, het verband met verschuivingen,
coördinaten in een orthonormaal assenstelsel, de norm, de formule van
Chasles-Möbius en de ontbinding in componenten.

Deel 1 is de willekeurige driehoek. Deel 2 zijn de vectoren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel graden is de som van de hoeken in elke driehoek?",
        opties=["180", "360", "90", "dat hangt af van de vorm"],
        antwoord=0,
        uitleg="Daarom volgt de derde hoek altijd vanzelf zodra je er twee kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je de cosinusregel?",
        opties=[
            "als je twee zijden en de ingesloten hoek kent, of alle drie de zijden",
            "als je twee hoeken en één zijde kent",
            "alleen als de driehoek ergens een rechte hoek bevat, en anders nooit",
            "als je enkel de drie hoeken kent",
        ],
        antwoord=0,
        uitleg="De cosinusregel is de algemene versie van Pythagoras, met een correctieterm voor de hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer gebruik je de sinusregel?",
        opties=[
            "als je een zijde kent met de hoek ertegenover, en nog een hoek of zijde",
            "als je alle drie de zijden kent maar nog geen enkele hoek berekend hebt",
            "als je twee zijden kent met de hoek ertussen",
            "alleen in een gelijkbenige driehoek",
        ],
        antwoord=0,
        uitleg="De sinusregel koppelt een zijde aan de hoek die ertegenover ligt, telkens per paar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over de sinusregel klopt?",
        opties=[
            "de verhouding van een zijde tot de sinus van de hoek ertegenover is voor alle drie de paren gelijk",
            "de som van de drie zijden gedeeld door de som van de drie sinussen is altijd gelijk aan één",
            "de sinus van een hoek is de zijde ertegenover gedeeld door de omtrek",
            "de sinusregel geldt enkel in een scherphoekige driehoek",
        ],
        antwoord=0,
        uitleg="Die gelijke verhouding is precies de diameter van de omgeschreven cirkel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar moet je bij de sinusregel op letten in een stomphoekige driehoek?",
        opties=[
            "je rekenmachine geeft de scherpe hoek terug, terwijl de stompe hoek de juiste kan zijn",
            "de sinusregel geldt dan niet meer en je moet altijd overschakelen op de cosinusregel",
            "je moet de zijden eerst van groot naar klein ordenen",
            "de som van de hoeken is dan geen 180 graden meer",
        ],
        antwoord=0,
        uitleg="Supplementaire hoeken hebben dezelfde sinus, dus stem je uitkomst af op de gegevens van de opgave.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een driehoek zijn twee hoeken 40 en 65 graden. Hoe groot is de derde?",
        opties=["75", "105", "85", "55"],
        antwoord=0,
        uitleg="180 min 40 min 65 is 75.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat wordt de cosinusregel als de ingesloten hoek recht is?",
        opties=[
            "de stelling van Pythagoras, want de cosinus van 90 graden is nul",
            "de sinusregel, want dan zijn alle verhoudingen gelijk",
            "een gelijkheid die altijd klopt, welke drie zijden je ook invult",
            "onbruikbaar, want je mag geen rechte hoek invullen",
        ],
        antwoord=0,
        uitleg="De correctieterm valt weg en er blijft a kwadraat is b kwadraat plus c kwadraat over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent van een driehoek de zijden 7 en 9 en de hoek van 40 graden ertussen. Wat bereken je eerst?",
        opties=[
            "de derde zijde met de cosinusregel",
            "de tweede hoek met de sinusregel",
            "de oppervlakte met basis maal hoogte",
            "de omtrek door de zijden op te tellen",
        ],
        antwoord=0,
        uitleg="Twee zijden met de hoek ertussen is precies het geval waarvoor de cosinusregel gemaakt is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent van een driehoek alle drie de zijden. Hoe vind je een hoek?",
        opties=[
            "met de cosinusregel, omgevormd naar de cosinus van die hoek",
            "met de sinusregel, want die werkt altijd",
            "met de stelling van Pythagoras op de twee kleinste zijden",
            "dat kan niet zonder minstens één gegeven hoek",
        ],
        antwoord=0,
        uitleg="Je vormt de formule om zodat de cosinus alleen komt te staan, en neemt dan de omgekeerde functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'een driehoek oplossen'?",
        opties=[
            "alle drie de zijden en alle drie de hoeken bepalen",
            "de oppervlakte en de omtrek berekenen",
            "nagaan of de driehoek rechthoekig is",
            "de driehoek in twee even grote delen verdelen",
        ],
        antwoord=0,
        uitleg="Met drie geschikte gegevens liggen de andere drie vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee landmeters staan 200 meter uit elkaar en meten elk de hoek naar dezelfde boom. Wat kunnen ze berekenen?",
        opties=[
            "de afstand van elke landmeter tot de boom, met de sinusregel",
            "enkel de hoogte van de boom, en niet de afstand",
            "niets, want ze kennen geen enkele zijde van de driehoek",
            "alleen de oppervlakte van de driehoek die ze vormen",
        ],
        antwoord=0,
        uitleg="Ze kennen een zijde en de twee hoeken die erop staan, dus ligt de derde hoek en de rest vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke driehoek ligt de langste zijde?",
        opties=[
            "tegenover de grootste hoek",
            "tegenover de kleinste hoek",
            "tussen de twee grootste hoeken in",
            "dat ligt niet vast",
        ],
        antwoord=0,
        uitleg="Dat is meteen een goede controle op een uitkomst: een lange zijde bij een kleine hoek klopt niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Kan een driehoek zijden 3, 4 en 9 hebben?",
        opties=[
            "nee, want 3 plus 4 is kleiner dan 9",
            "ja, want alle drie de getallen zijn verschillend",
            "ja, maar dan is hij stomphoekig",
            "dat hangt af van de hoeken",
        ],
        antwoord=0,
        uitleg="Twee zijden samen moeten langer zijn dan de derde, anders raken de uiteinden elkaar niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De cosinusregel is een uitbreiding van de stelling van Pythagoras naar elke driehoek.",
        antwoord=True,
        uitleg="Bij een rechte hoek valt de extra term weg en blijft Pythagoras over.",
    ),
    dict(
        type="waarofniet",
        vraag="De sinusregel werkt alleen in rechthoekige driehoeken.",
        antwoord=False,
        uitleg="Ze geldt in elke driehoek. Daarvoor is ze gemaakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee hoeken van een driehoek kennen volstaat om de derde te kennen.",
        antwoord=True,
        uitleg="De som is altijd 180 graden.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je enkel de drie hoeken van een driehoek kent, liggen de zijden vast.",
        antwoord=False,
        uitleg="Dan ligt alleen de vorm vast. Er zijn oneindig veel gelijkvormige driehoeken met die hoeken.",
    ),
    dict(
        type="invultekst",
        vraag="Twee hoeken van een driehoek zijn 55 en 72 graden. Hoeveel graden is de derde?",
        antwoord=["53", "53 graden"],
        uitleg="180 min 55 min 72.",
    ),
    dict(
        type="invultekst",
        vraag="Welke regel gebruik je bij twee zijden en de ingesloten hoek?",
        antwoord=["cosinusregel", "de cosinusregel"],
        uitleg="Bij een zijde met de hoek ertegenover neem je de sinusregel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de cosinus van 90 graden?",
        antwoord=["0", "nul"],
        uitleg="Daarom wordt de cosinusregel dan gewoon Pythagoras.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie kenmerken heeft een vector?",
        opties=[
            "richting, zin en grootte",
            "lengte, breedte en hoogte",
            "beginpunt, middelpunt en eindpunt",
            "x-waarde, y-waarde en hoek",
        ],
        antwoord=0,
        uitleg="De richting is de stand van de rechte, de zin is welke kant op, en de grootte is de lengte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de richting en de zin van een vector?",
        opties=[
            "de richting is de stand van de rechte, de zin is welke van de twee kanten op",
            "de richting is de lengte, de zin is het beginpunt",
            "de richting geldt in het vlak, de zin enkel in de ruimte",
            "er is geen verschil tussen de twee, het zijn gewoon twee woorden voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Twee tegengestelde vectoren hebben dezelfde richting en dezelfde grootte, maar een tegengestelde zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de nulvector?",
        opties=[
            "de vector met grootte nul, zonder richting of zin",
            "de vector die op de oorsprong begint",
            "de vector met coördinaten 1 en 0",
            "de vector die loodrecht op de x-as staat en op nul begint",
        ],
        antwoord=0,
        uitleg="Tel je een vector op bij zijn tegengestelde, dan krijg je de nulvector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een eenheidsvector?",
        opties=[
            "een vector met grootte één",
            "een vector die langs de x-as ligt",
            "een vector met coördinaten 1 en 1",
            "een vector die bij elke verschuiving hoort",
        ],
        antwoord=0,
        uitleg="Handig om enkel een richting aan te duiden, zonder iets over de grootte te zeggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vector heeft coördinaten (3, 4). Wat is zijn norm?",
        opties=["5", "7", "12", "ongeveer 3,5"],
        antwoord=0,
        uitleg="De norm is de lengte, en die bereken je met Pythagoras: wortel uit 9 plus 16.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vector heeft coördinaten (min 6, 8). Wat is zijn norm?",
        opties=["10", "2", "14", "min 10"],
        antwoord=0,
        uitleg="De kwadraten maken het teken onbelangrijk: 36 plus 64 is 100.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe tel je twee vectoren met coördinaten op?",
        opties=[
            "de x-waarden bij elkaar en de y-waarden bij elkaar",
            "de x van de ene bij de y van de andere",
            "de normen bij elkaar en daarna de hoek",
            "de vectoren eerst even lang maken en dan optellen",
        ],
        antwoord=0,
        uitleg="(2, 1) plus (3, 5) geeft (5, 6).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de formule van Chasles-Möbius over de vector van A naar B?",
        opties=[
            "hij is de puntvector van B min de puntvector van A",
            "hij is de puntvector van A min de puntvector van B",
            "hij is de som van de puntvectoren van A en B",
            "hij is het gemiddelde van de puntvectoren van A en B",
        ],
        antwoord=0,
        uitleg="Eindpunt min beginpunt, net zoals je een verschil berekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="A ligt op (1, 2) en B op (4, 7). Wat zijn de coördinaten van de vector van A naar B?",
        opties=["(3, 5)", "(5, 9)", "(min 3, min 5)", "(4, 14)"],
        antwoord=0,
        uitleg="4 min 1 is 3, en 7 min 2 is 5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als je een vector met min 2 vermenigvuldigt?",
        opties=[
            "hij wordt twee keer zo lang en keert van zin om",
            "hij wordt twee keer zo lang en houdt dezelfde zin",
            "hij wordt half zo lang en keert van zin om",
            "hij blijft even lang maar draait 90 graden",
        ],
        antwoord=0,
        uitleg="Het getal bepaalt de lengte, het teken bepaalt de zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe teken je de som van twee vectoren?",
        opties=[
            "je legt de tweede met zijn beginpunt op het eindpunt van de eerste",
            "je legt allebei de beginpunten op elkaar en tekent de verbinding",
            "je legt de eindpunten op elkaar en meet de afstand",
            "je telt de lengtes op en tekent één vector van die lengte",
        ],
        antwoord=0,
        uitleg="De som loopt dan van het beginpunt van de eerste tot het eindpunt van de tweede. Dat heet de kop-staartmethode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee krachten van 3 en 4 newton werken loodrecht op elkaar. Hoe groot is de resulterende kracht?",
        opties=["5 newton", "7 newton", "1 newton", "12 newton"],
        antwoord=0,
        uitleg="Loodrecht betekent Pythagoras. Werkten ze in dezelfde zin, dan was het wel 7.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een vector ontbinden in zijn componenten?",
        opties=[
            "hem schrijven als de som van een horizontale en een verticale vector",
            "hem in twee even lange stukken verdelen",
            "hem delen door zijn norm",
            "hem vervangen door zijn tegengestelde",
        ],
        antwoord=0,
        uitleg="Zo wordt een schuine kracht een kracht vooruit en een kracht omhoog, en die kan je apart bekijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee vectoren zijn gelijk als ze dezelfde richting, zin en grootte hebben, ook als ze elders in het vlak liggen.",
        antwoord=True,
        uitleg="Dat is wat een vrije vector betekent: het beginpunt doet er niet toe.",
    ),
    dict(
        type="waarofniet",
        vraag="De norm van een vector kan negatief zijn.",
        antwoord=False,
        uitleg="De norm is een lengte, en die is altijd positief of nul.",
    ),
    dict(
        type="waarofniet",
        vraag="De som van twee vectoren is altijd langer dan elk van de twee.",
        antwoord=False,
        uitleg="Werken ze tegen elkaar in, dan is de som korter. Zijn ze tegengesteld, dan is de som de nulvector.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vector met een reëel getal vermenigvuldigen verandert zijn richting niet.",
        antwoord=True,
        uitleg="De richting blijft, alleen de grootte verandert en bij een negatief getal ook de zin.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de norm van de vector met coördinaten (5, 12)?",
        antwoord=["13"],
        uitleg="25 plus 144 is 169.",
    ),
    dict(
        type="invultekst",
        vraag="A ligt op (2, 3) en B op (7, 3). Wat is de norm van de vector van A naar B?",
        antwoord=["5"],
        uitleg="De y-waarden zijn gelijk, dus de vector ligt horizontaal en is 5 lang.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de vector met grootte nul?",
        antwoord=["nulvector", "de nulvector"],
        uitleg="Hij heeft geen richting en geen zin.",
    ),
]
