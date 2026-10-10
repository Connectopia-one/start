# -*- coding: utf-8 -*-
"""De vragen voor "De parabool, transformaties en functiekenmerken".

Uit de bouwsteen Relaties en verandering: de tweedegraadsfunctie met haar
nulwaarden, top en symmetrieas, het opbouwen van \\(g(x) = a(x - p)^{2} + q\\)
vanuit \\(f(x) = x^{2}\\) met verschuiven, spiegelen, uitrekken en
samendrukken, en het aflezen van de functiekenmerken: domein, bereik,
nulwaarden, tekenverloop, stijgen en dalen, extrema en symmetrie.

Achteraan komt het overzicht van de voorschriften die de fiche noemt:
\\(f(x) = ax + b\\), \\(ax^{2}\\), \\(ax^{2} + bx + c\\),
\\(a(x - p)^{2} + q\\), \\(a(x - x_{1})(x - x_{2})\\) en \\(f(x) = \\frac{c}{x}\\)
met haar hyperbool.

Deel 1 is de parabool zelf en de transformaties. Deel 2 zijn de
functiekenmerken en de soorten voorschriften.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe heet de grafiek van een tweedegraadsfunctie?",
        opties=["een parabool", "een hyperbool", "een rechte", "een cirkelboog"],
        antwoord=0,
        uitleg="De grafiek van \\(f(x) = \\frac{c}{x}\\) heet wel een hyperbool.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer opent een parabool met voorschrift \\(f(x) = ax^{2} + bx + c\\) naar boven?",
        opties=["als \\(a > 0\\)", "als \\(a < 0\\)", "als \\(c > 0\\)", "als \\(b = 0\\)"],
        antwoord=0,
        uitleg="Het teken van \\(a\\) bepaalt de opening. Bij \\(a < 0\\) opent ze naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nulwaarde van een functie?",
        opties=[
            "een \\(x\\)-waarde waarvoor f(x) gelijk is aan nul",
            "de \\(y\\)-waarde waar de grafiek de verticale as snijdt",
            "de \\(x\\)-waarde van de top van de parabool",
            "de waarde die de functie nooit aanneemt",
        ],
        antwoord=0,
        uitleg="Op de grafiek zijn dat de snijpunten met de \\(x\\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel nulwaarden heeft \\(f(x) = x^{2} - 9\\)?",
        opties=["twee", "één", "geen", "oneindig veel"],
        antwoord=0,
        uitleg="\\(x^{2} = 9\\) geeft \\(x = 3\\) en \\(x = -3\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel nulwaarden heeft \\(f(x) = x^{2} + 4\\)?",
        opties=["geen", "één", "twee", "drie"],
        antwoord=0,
        uitleg="\\(x^{2} + 4\\) is altijd groter dan nul, dus de parabool raakt de \\(x\\)-as niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de top van de parabool \\(g(x) = (x - 3)^{2} + 5\\)?",
        opties=["\\((3, 5)\\)", "\\((-3, 5)\\)", "\\((5, 3)\\)", "\\((3, -5)\\)"],
        antwoord=0,
        uitleg="Bij \\(a(x - p)^{2} + q\\) is de top het punt \\((p, q)\\). Let op het minteken in de haakjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de top van de parabool \\(g(x) = (x + 2)^{2} - 7\\)?",
        opties=["\\((-2, -7)\\)", "\\((2, -7)\\)", "\\((-2, 7)\\)", "\\((2, 7)\\)"],
        antwoord=0,
        uitleg="\\(x + 2\\) is hetzelfde als \\(x - (-2)\\), dus \\(p = -2\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de q in \\(g(x) = a(x - p)^{2} + q\\) met de grafiek van \\(x^{2}\\)?",
        opties=[
            "ze schuift de grafiek verticaal op",
            "ze schuift de grafiek horizontaal op",
            "ze maakt de grafiek smaller of breder",
            "ze spiegelt de grafiek om de \\(x\\)-as",
        ],
        antwoord=0,
        uitleg="De \\(p\\) schuift horizontaal, de \\(a\\) rekt uit of spiegelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de parabool \\(y = x^{2}\\) als je er \\(y = -x^{2}\\) van maakt?",
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
        vraag="Wat doet een \\(a > 1\\) met de parabool \\(y = x^{2}\\)?",
        opties=[
            "ze wordt smaller, de grafiek rekt verticaal uit",
            "ze wordt breder, de grafiek wordt samengedrukt",
            "ze schuift naar rechts over a eenheden",
            "ze schuift omhoog over a eenheden",
        ],
        antwoord=0,
        uitleg="Bij \\(0 < a < 1\\) wordt ze juist breder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de symmetrieas van de parabool met top \\((4, -1)\\)?",
        opties=["de verticale rechte \\(x = 4\\)", "de horizontale rechte \\(y = 4\\)", "de verticale rechte \\(x = -1\\)", "de horizontale rechte \\(y = -1\\)"],
        antwoord=0,
        uitleg="De symmetrieas loopt altijd verticaal door de top.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een parabool heeft nulwaarden \\(-2\\) en \\(6\\). Waar ligt haar symmetrieas?",
        opties=["bij \\(x = 2\\)", "bij \\(x = 4\\)", "bij \\(x = 8\\)", "bij \\(x = -4\\)"],
        antwoord=0,
        uitleg="Precies in het midden tussen de twee nulwaarden: \\(\\frac{-2 + 6}{2} = 2\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar snijdt de parabool \\(f(x) = x^{2} - 2x - 8\\) de verticale as?",
        opties=["in \\((0, -8)\\)", "in \\((0, -2)\\)", "in \\((-8, 0)\\)", "in \\((0, 8)\\)"],
        antwoord=0,
        uitleg="Vul \\(x = 0\\) in, dan houd je de \\(c\\) over.",
    ),
    dict(
        type="waarofniet",
        vraag="Een parabool is symmetrisch om een verticale rechte door haar top.",
        antwoord=True,
        uitleg="Twee punten met dezelfde \\(y\\)-waarde liggen even ver van die as.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke parabool snijdt de \\(x\\)-as in twee punten.",
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
        vraag="De grafiek van \\(y = (x - 5)^{2}\\) ligt vijf eenheden links van \\(y = x^{2}\\).",
        antwoord=False,
        uitleg="Ze ligt vijf eenheden rechts. Een min in de haakjes schuift naar rechts.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de \\(x\\)-waarde van de top van \\(g(x) = (x - 6)^{2} + 2\\)?",
        antwoord=["6"],
        uitleg="Bij \\(a(x - p)^{2} + q\\) is \\(p\\) de \\(x\\)-waarde van de top.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de grafiek van een tweedegraadsfunctie?",
        antwoord=["parabool", "een parabool"],
        uitleg="Bij \\(f(x) = \\frac{c}{x}\\) heet ze een hyperbool.",
    ),
    dict(
        type="invultekst",
        vraag="Een parabool heeft nulwaarden \\(1\\) en \\(9\\). Bij welke \\(x\\) ligt haar symmetrieas?",
        antwoord=["5"],
        uitleg="Het midden tussen \\(1\\) en \\(9\\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van \\(f(x) = x^{2}\\)?",
        opties=[
            "alle reële getallen groter dan of gelijk aan nul: \\(\\left[0, +\\infty\\right[\\)",
            "alle reële getallen kleiner dan of gelijk aan nul: \\(\\left]-\\infty, 0\\right]\\)",
            "alle reële getallen zonder uitzondering: \\(\\mathbb{R}\\)",
            "alle reële getallen behalve de nul zelf: \\(\\mathbb{R} \\setminus \\{0\\}\\)",
        ],
        antwoord=0,
        uitleg="Een kwadraat is nooit negatief, dus de parabool komt niet onder de \\(x\\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van \\(g(x) = (x - 1)^{2} + 4\\)?",
        opties=[
            "alle reële getallen groter dan of gelijk aan 4: \\(\\left[4, +\\infty\\right[\\)",
            "alle reële getallen groter dan of gelijk aan 1: \\(\\left[1, +\\infty\\right[\\)",
            "alle reële getallen kleiner dan of gelijk aan 4: \\(\\left]-\\infty, 4\\right]\\)",
            "alle reële getallen zonder enige beperking: \\(\\mathbb{R}\\)",
        ],
        antwoord=0,
        uitleg="De top ligt op hoogte 4 en de parabool opent naar boven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van elke veeltermfunctie, dus ook van een parabool?",
        opties=[
            "alle reële getallen: \\(\\mathbb{R}\\)",
            "alle positieve reële getallen: \\(\\left]0, +\\infty\\right[\\)",
            "alle reële getallen behalve nul: \\(\\mathbb{R} \\setminus \\{0\\}\\)",
            "enkel de gehele getallen: \\(\\mathbb{Z}\\)",
        ],
        antwoord=0,
        uitleg="Je kan elk getal invullen. Bij \\(f(x) = \\frac{c}{x}\\) valt de nul wél weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont het tekenverloop van een functie?",
        opties=[
            "voor welke \\(x\\)-waarden de functiewaarde positief, nul of negatief is",
            "voor welke \\(x\\)-waarden de functie stijgt of daalt",
            "hoeveel toppen de grafiek van de functie heeft",
            "welke \\(y\\)-waarden de functie allemaal aanneemt",
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
            "welke \\(x\\)-waarden je mag invullen",
        ],
        antwoord=0,
        uitleg="De pijlen wijzen omhoog waar ze stijgt en omlaag waar ze daalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar daalt de functie \\(f(x) = x^{2} - 4x\\)?",
        opties=[
            "links van \\(x = 2\\)",
            "rechts van \\(x = 2\\)",
            "overal waar \\(x > 0\\)",
            "nergens, ze stijgt overal",
        ],
        antwoord=0,
        uitleg="De top ligt bij \\(x = 2\\) en de parabool opent naar boven, dus daalt ze eerst en stijgt ze daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een extremum van een functie?",
        opties=[
            "een grootste of kleinste functiewaarde op een stuk van de grafiek",
            "een \\(x\\)-waarde waarvoor de functie geen waarde heeft",
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
            "\\(f(x) = a(x - x_{1})(x - x_{2})\\)",
            "\\(f(x) = a(x - p)^{2} + q\\)",
            "\\(f(x) = ax^{2} + bx + c\\)",
            "\\(f(x) = ax + b\\)",
        ],
        antwoord=0,
        uitleg="Een product is nul zodra één factor nul is, dus \\(x_{1}\\) en \\(x_{2}\\) zijn de nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk voorschrift lees je de top het snelst af?",
        opties=[
            "\\(f(x) = a(x - p)^{2} + q\\)",
            "\\(f(x) = a(x - x_{1})(x - x_{2})\\)",
            "\\(f(x) = ax^{2} + bx + c\\)",
            "\\(f(x) = \\frac{c}{x}\\)",
        ],
        antwoord=0,
        uitleg="De top is meteen het punt \\((p, q)\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorschrift hoort bij een parabool met nulwaarden \\(2\\) en \\(5\\)?",
        opties=[
            "\\(f(x) = (x - 2)(x - 5)\\)",
            "\\(f(x) = (x + 2)(x + 5)\\)",
            "\\(f(x) = (x - 2)^{2} + 5\\)",
            "\\(f(x) = (2x + 5) \\cdot x\\)",
        ],
        antwoord=0,
        uitleg="Vul \\(2\\) of \\(5\\) in en één factor wordt nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de grafiek van \\(f(x) = \\frac{6}{x}\\) eruit?",
        opties=[
            "een hyperbool met twee takken",
            "een parabool die naar boven opent",
            "een rechte door de oorsprong",
            "een rechte evenwijdig met de \\(x\\)-as",
        ],
        antwoord=0,
        uitleg="Een tak ligt bij de positieve \\(x\\)-waarden, een tak bij de negatieve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband bij \\(f(x) = \\frac{6}{x}\\)?",
        opties=[
            "omgekeerd evenredig: verdubbelt \\(x\\), dan halveert \\(y\\)",
            "recht evenredig: verdubbelt \\(x\\), dan verdubbelt \\(y\\)",
            "lineair, maar niet recht evenredig",
            "kwadratisch, want de grafiek is gebogen",
        ],
        antwoord=0,
        uitleg="Het product van \\(x\\) en \\(y\\) blijft telkens \\(6\\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is \\(x = 0\\) geen deel van het domein van \\(f(x) = \\frac{6}{x}\\)?",
        opties=[
            "omdat je niet door nul mag delen",
            "omdat \\(\\frac{6}{0}\\) gelijk is aan nul",
            "omdat de functie daar twee waarden zou hebben",
            "omdat de grafiek daar de \\(x\\)-as snijdt",
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
        vraag="Het bereik van elke tweedegraadsfunctie is de verzameling \\(\\mathbb{R}\\) van alle reële getallen.",
        antwoord=False,
        uitleg="De top begrenst het bereik aan één kant, boven of onder.",
    ),
    dict(
        type="waarofniet",
        vraag="De functie \\(f(x) = \\frac{c}{x}\\) heeft een nulwaarde.",
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
        vraag="Wat is de kleinste functiewaarde van \\(g(x) = (x - 3)^{2} + 2\\)?",
        antwoord=["2"],
        uitleg="De \\(q\\) van de top.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de grafiek van \\(f(x) = \\frac{c}{x}\\)?",
        antwoord=["hyperbool", "een hyperbool"],
        uitleg="Ze heeft twee takken.",
    ),
]
