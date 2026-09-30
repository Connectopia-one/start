# -*- coding: utf-8 -*-
"""De vragen voor "De parabool, transformaties en functiekenmerken".

Uit de bouwsteen Relaties en verandering: de tweedegraadsfunctie met haar
nulwaarden, top en symmetrieas, het opbouwen van g(x) is a(x min p) kwadraat
plus q vanuit f(x) is x kwadraat met verschuiven, spiegelen, uitrekken en
samendrukken, en het aflezen van de functiekenmerken: domein, bereik,
nulwaarden, tekenverloop, stijgen en dalen, extrema en symmetrie.

Achteraan komt het overzicht van de voorschriften die de fiche noemt:
f(x) is ax plus b, ax kwadraat, ax kwadraat plus bx plus c,
a(x min p) kwadraat plus q, a(x min x1)(x min x2) en f(x) is c op x met haar
hyperbool.

Deel 1 is de parabool zelf en de transformaties. Deel 2 zijn de
functiekenmerken en de soorten voorschriften.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe heet de grafiek van een tweedegraadsfunctie?",
        opties=["een parabool", "een hyperbool", "een rechte", "een cirkelboog"],
        antwoord=0,
        uitleg="De grafiek van f(x) is c op x heet wel een hyperbool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer opent een parabool met voorschrift f(x) is ax kwadraat plus bx plus c naar boven?",
        opties=["als a groter is dan nul", "als a kleiner is dan nul", "als c groter is dan nul", "als b gelijk is aan nul"],
        antwoord=0,
        uitleg="Het teken van a bepaalt de opening. Bij a kleiner dan nul opent ze naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nulwaarde van een functie?",
        opties=[
            "een x-waarde waarvoor f(x) gelijk is aan nul",
            "de y-waarde waar de grafiek de verticale as snijdt",
            "de x-waarde van de top van de parabool",
            "de waarde die de functie nooit aanneemt",
        ],
        antwoord=0,
        uitleg="Op de grafiek zijn dat de snijpunten met de x-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel nulwaarden heeft f(x) is x kwadraat min 9?",
        opties=["twee", "één", "geen", "oneindig veel"],
        antwoord=0,
        uitleg="x kwadraat is 9 geeft x is 3 en x is min 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel nulwaarden heeft f(x) is x kwadraat plus 4?",
        opties=["geen", "één", "twee", "drie"],
        antwoord=0,
        uitleg="x kwadraat plus 4 is altijd groter dan nul, dus de parabool raakt de x-as niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de top van de parabool g(x) is (x min 3) kwadraat plus 5?",
        opties=["(3, 5)", "(min 3, 5)", "(5, 3)", "(3, min 5)"],
        antwoord=0,
        uitleg="Bij a(x min p) kwadraat plus q is de top het punt (p, q). Let op het minteken in de haakjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de top van de parabool g(x) is (x plus 2) kwadraat min 7?",
        opties=["(min 2, min 7)", "(2, min 7)", "(min 2, 7)", "(2, 7)"],
        antwoord=0,
        uitleg="x plus 2 is hetzelfde als x min (min 2), dus p is min 2.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de q in g(x) is a(x min p) kwadraat plus q met de grafiek van x kwadraat?",
        opties=[
            "ze schuift de grafiek verticaal op",
            "ze schuift de grafiek horizontaal op",
            "ze maakt de grafiek smaller of breder",
            "ze spiegelt de grafiek om de x-as",
        ],
        antwoord=0,
        uitleg="De p schuift horizontaal, de a rekt uit of spiegelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de parabool y is x kwadraat als je er y is min x kwadraat van maakt?",
        opties=[
            "ze spiegelt om de horizontale as",
            "ze spiegelt om de verticale as",
            "ze schuift één eenheid omlaag",
            "er verandert niets aan de grafiek",
        ],
        antwoord=0,
        uitleg="Elke functiewaarde wordt haar tegengestelde, dus de parabool opent naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een a groter dan 1 met de parabool y is x kwadraat?",
        opties=[
            "ze wordt smaller, de grafiek rekt verticaal uit",
            "ze wordt breder, de grafiek wordt samengedrukt",
            "ze schuift naar rechts over a eenheden",
            "ze schuift omhoog over a eenheden",
        ],
        antwoord=0,
        uitleg="Bij a tussen nul en één wordt ze juist breder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de symmetrieas van de parabool met top (4, min 1)?",
        opties=["de verticale rechte x is 4", "de horizontale rechte y is 4", "de verticale rechte x is min 1", "de horizontale rechte y is min 1"],
        antwoord=0,
        uitleg="De symmetrieas loopt altijd verticaal door de top.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een parabool heeft nulwaarden min 2 en 6. Waar ligt haar symmetrieas?",
        opties=["bij x is 2", "bij x is 4", "bij x is 8", "bij x is min 4"],
        antwoord=0,
        uitleg="Precies in het midden tussen de twee nulwaarden: min 2 plus 6 gedeeld door 2.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar snijdt de parabool f(x) is x kwadraat min 2x min 8 de verticale as?",
        opties=["in (0, min 8)", "in (0, min 2)", "in (min 8, 0)", "in (0, 8)"],
        antwoord=0,
        uitleg="Vul x is nul in, dan houd je de c over.",
    ),
    dict(
        type="waarofniet",
        vraag="Een parabool is symmetrisch om een verticale rechte door haar top.",
        antwoord=True,
        uitleg="Twee punten met dezelfde y-waarde liggen even ver van die as.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke parabool snijdt de x-as in twee punten.",
        antwoord=False,
        uitleg="Ze kan de as ook raken in één punt of er helemaal naast liggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een parabool die naar beneden opent, is de top het hoogste punt.",
        antwoord=True,
        uitleg="Dat is dan het maximum van de functie.",
    ),
    dict(
        type="waarofniet",
        vraag="De grafiek van y is (x min 5) kwadraat ligt vijf eenheden links van y is x kwadraat.",
        antwoord=False,
        uitleg="Ze ligt vijf eenheden rechts. Een min in de haakjes schuift naar rechts.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de x-waarde van de top van g(x) is (x min 6) kwadraat plus 2?",
        antwoord=["6"],
        uitleg="Bij a(x min p) kwadraat plus q is p de x-waarde van de top.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grafiek van een tweedegraadsfunctie?",
        antwoord=["parabool", "een parabool"],
        uitleg="Bij f(x) is c op x heet ze een hyperbool.",
    ),
    dict(
        type="invultekst",
        vraag="Een parabool heeft nulwaarden 1 en 9. Bij welke x ligt haar symmetrieas?",
        antwoord=["5"],
        uitleg="Het midden tussen 1 en 9.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van f(x) is x kwadraat?",
        opties=[
            "alle reële getallen groter dan of gelijk aan nul",
            "alle reële getallen kleiner dan of gelijk aan nul",
            "alle reële getallen zonder uitzondering",
            "alle reële getallen behalve de nul zelf",
        ],
        antwoord=0,
        uitleg="Een kwadraat is nooit negatief, dus de parabool komt niet onder de x-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van g(x) is (x min 1) kwadraat plus 4?",
        opties=[
            "alle reële getallen groter dan of gelijk aan 4",
            "alle reële getallen groter dan of gelijk aan 1",
            "alle reële getallen kleiner dan of gelijk aan 4",
            "alle reële getallen zonder enige beperking",
        ],
        antwoord=0,
        uitleg="De top ligt op hoogte 4 en de parabool opent naar boven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van elke veeltermfunctie, dus ook van een parabool?",
        opties=[
            "alle reële getallen",
            "alle positieve reële getallen",
            "alle reële getallen behalve nul",
            "enkel de gehele getallen",
        ],
        antwoord=0,
        uitleg="Je kan elk getal invullen. Bij f(x) is c op x valt de nul wél weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont het tekenverloop van een functie?",
        opties=[
            "voor welke x-waarden de functiewaarde positief, nul of negatief is",
            "voor welke x-waarden de functie stijgt of daalt",
            "hoeveel toppen de grafiek van de functie heeft",
            "welke y-waarden de functie allemaal aanneemt",
        ],
        antwoord=0,
        uitleg="Stijgen en dalen lees je af in het verloopschema, niet in het tekenverloop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont het verloopschema van een functie?",
        opties=[
            "waar de functie stijgt en waar ze daalt",
            "waar de functiewaarde positief en waar ze negatief is",
            "waar de grafiek de verticale as snijdt",
            "welke x-waarden je mag invullen",
        ],
        antwoord=0,
        uitleg="De pijlen wijzen omhoog waar ze stijgt en omlaag waar ze daalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar daalt de functie f(x) is x kwadraat min 4x?",
        opties=[
            "links van x is 2",
            "rechts van x is 2",
            "overal waar x groter is dan nul",
            "nergens, ze stijgt overal",
        ],
        antwoord=0,
        uitleg="De top ligt bij x is 2 en de parabool opent naar boven, dus daalt ze eerst en stijgt ze daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een extremum van een functie?",
        opties=[
            "een grootste of kleinste functiewaarde op een stuk van de grafiek",
            "een x-waarde waarvoor de functie geen waarde heeft",
            "het punt waar de grafiek de verticale as snijdt",
            "de afstand tussen de twee nulwaarden",
        ],
        antwoord=0,
        uitleg="Bij een parabool is de top het enige extremum: een minimum of een maximum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk voorschrift lees je de nulwaarden het snelst af?",
        opties=[
            "f(x) is a(x min x1)(x min x2)",
            "f(x) is a(x min p) kwadraat plus q",
            "f(x) is ax kwadraat plus bx plus c",
            "f(x) is ax plus b",
        ],
        antwoord=0,
        uitleg="Een product is nul zodra één factor nul is, dus x1 en x2 zijn de nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk voorschrift lees je de top het snelst af?",
        opties=[
            "f(x) is a(x min p) kwadraat plus q",
            "f(x) is a(x min x1)(x min x2)",
            "f(x) is ax kwadraat plus bx plus c",
            "f(x) is c gedeeld door x",
        ],
        antwoord=0,
        uitleg="De top is meteen het punt (p, q).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorschrift hoort bij een parabool met nulwaarden 2 en 5?",
        opties=[
            "f(x) is (x min 2)(x min 5)",
            "f(x) is (x plus 2)(x plus 5)",
            "f(x) is (x min 2) kwadraat plus 5",
            "f(x) is 2x plus 5 keer x",
        ],
        antwoord=0,
        uitleg="Vul 2 of 5 in en één factor wordt nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de grafiek van f(x) is 6 op x eruit?",
        opties=[
            "een hyperbool met twee takken",
            "een parabool die naar boven opent",
            "een rechte door de oorsprong",
            "een rechte evenwijdig met de x-as",
        ],
        antwoord=0,
        uitleg="Een tak ligt bij de positieve x-waarden, een tak bij de negatieve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband bij f(x) is 6 op x?",
        opties=[
            "omgekeerd evenredig: verdubbelt x, dan halveert y",
            "recht evenredig: verdubbelt x, dan verdubbelt y",
            "lineair, maar niet recht evenredig",
            "kwadratisch, want de grafiek is gebogen",
        ],
        antwoord=0,
        uitleg="Het product van x en y blijft telkens 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is x is nul geen deel van het domein van f(x) is 6 op x?",
        opties=[
            "omdat je niet door nul mag delen",
            "omdat 6 op nul gelijk is aan nul",
            "omdat de functie daar twee waarden zou hebben",
            "omdat de grafiek daar de x-as snijdt",
        ],
        antwoord=0,
        uitleg="De grafiek nadert de verticale as wel, maar raakt hem nooit.",
    ),
    dict(
        type="waarofniet",
        vraag="Een parabool die naar boven opent, heeft een minimum maar geen maximum.",
        antwoord=True,
        uitleg="Ze loopt aan beide kanten onbeperkt omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit de grafiek van een parabool kan je haar voorschrift afleiden.",
        antwoord=True,
        uitleg="Lees de top af voor p en q, en gebruik één ander punt om a te vinden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bereik van elke tweedegraadsfunctie is de verzameling van alle reële getallen.",
        antwoord=False,
        uitleg="De top begrenst het bereik aan één kant, boven of onder.",
    ),
    dict(
        type="waarofniet",
        vraag="De functie f(x) is c op x heeft een nulwaarde.",
        antwoord=False,
        uitleg="Een breuk met een teller die niet nul is, wordt nooit nul.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het schema dat toont waar een functie stijgt en waar ze daalt?",
        antwoord=["verloopschema", "het verloopschema"],
        uitleg="Het tekenverloop toont iets anders: waar de functiewaarde positief of negatief is.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de kleinste functiewaarde van g(x) is (x min 3) kwadraat plus 2?",
        antwoord=["2"],
        uitleg="De q van de top.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de grafiek van f(x) is c op x?",
        antwoord=["hyperbool", "een hyperbool"],
        uitleg="Ze heeft twee takken.",
    ),
]
