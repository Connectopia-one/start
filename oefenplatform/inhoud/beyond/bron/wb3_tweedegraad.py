# -*- coding: utf-8 -*-
"""Tweedegraadsfuncties.

Wiskunde basis, derde graad (niet voor welzijnswetenschappen: hun fiche
2027_wiskunde_3DO_WEL laat dit onderdeel weg). De fiche vraagt: de
voorstellingswijzen, parabool, berg- en dalparabool, top, nulwaarden,
symmetrieas, de functiekenmerken, en de transformaties van \\(f(x) = x^{2}\\):
verticale verschuiving, verticale uitrekking, horizontale verschuiving en
spiegeling rond de x-as. De drie voorschriften uit de bijlage:
ax² + bx + c, a(x − p)² + q en a(x − x1)(x − x2).

Deel 1: grafiek, top en symmetrieas. Deel 2: transformaties en situaties.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f(x) = -2x^{2} + 3x + 1\) is een ...",
        opties=[r"bergparabool", r"dalparabool", r"rechte", r"hyperbool"],
        antwoord=0,
        uitleg=r"De coëfficiënt van \(x^{2}\) is negatief (\(a = -2\)), dus de parabool opent naar beneden: een bergparabool met een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een dalparabool heeft een minimum in haar top.",
        antwoord=True,
        uitleg=r"Bij \(a > 0\) opent de parabool naar boven. De top is dan het laagste punt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de top van de parabool \(f(x) = 3(x - 2)^{2} + 5\)?",
        opties=[r"\((2, 5)\)", r"\((-2, 5)\)", r"\((2, -5)\)", r"\((3, 5)\)"],
        antwoord=0,
        uitleg=r"In de vorm \(a(x - p)^{2} + q\) is de top \((p, q)\). Let op het minteken: \(x - 2\) geeft \(p = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de symmetrieas van \(f(x) = (x + 4)^{2} - 1\)?",
        opties=[r"\(x = -4\)", r"\(x = 4\)", r"\(y = -1\)", r"\(x = -1\)"],
        antwoord=0,
        uitleg=r"\(x + 4 = x - (-4)\), dus \(p = -4\). De symmetrieas is de verticale rechte door de top: \(x = -4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke formule vind je de \(x\)-coördinaat van de top van \(f(x) = ax^{2} + bx + c\)?",
        opties=[r"\(x = -\dfrac{b}{2a}\)", r"\(x = \dfrac{b}{2a}\)", r"\(x = -\dfrac{2a}{b}\)", r"\(x = -\dfrac{c}{a}\)"],
        antwoord=0,
        uitleg=r"De top ligt op de symmetrieas \(x = -\dfrac{b}{2a}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de \(x\)-coördinaat van de top van \(f(x) = x^{2} - 6x + 2\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(x = -\dfrac{-6}{2 \cdot 1} = 3\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is de \(y\)-coördinaat van de top van \(f(x) = x^{2} - 6x + 2\)? Schrijf het getal.",
        antwoord=["-7", "−7", "min 7"],
        uitleg=r"De top ligt bij \(x = 3\): \(f(3) = 9 - 18 + 2 = -7\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn de nulwaarden van \(f(x) = 2(x - 1)(x + 5)\)?",
        opties=[r"\(1\) en \(-5\)", r"\(-1\) en \(5\)", r"\(2\), \(1\) en \(-5\)", r"\(1\) en \(5\)"],
        antwoord=0,
        uitleg=r"In de vorm \(a(x - x_{1})(x - x_{2})\) lees je de nulwaarden af: \(x_{1} = 1\) en \(x_{2} = -5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een parabool heeft nulwaarden \(-2\) en \(6\). Wat is de \(x\)-coördinaat van de top? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"De symmetrieas ligt precies tussen de nulwaarden: \(\dfrac{-2 + 6}{2} = 2\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Waar snijdt \(f(x) = 4x^{2} - x + 7\) de \(y\)-as? Schrijf de \(y\)-coördinaat.",
        antwoord=["7", "zeven"],
        uitleg=r"\(f(0) = c = 7\). Het snijpunt met de \(y\)-as is \((0, 7)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elke tweedegraadsfunctie heeft twee nulwaarden.",
        antwoord=False,
        uitleg=r"Een parabool kan de \(x\)-as twee keer, één keer (in de top) of nooit snijden. \(f(x) = x^{2} + 1\) heeft geen nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het bereik van \(f(x) = -(x - 1)^{2} + 4\)?",
        opties=[r"\(]-\infty, 4]\)", r"\([4, +\infty[\)", r"\(]-\infty, 1]\)", r"\(\mathbb{R}\)"],
        antwoord=0,
        uitleg=r"Het is een bergparabool met top \((1, 4)\). De grootste functiewaarde is \(4\), daaronder alles.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waar stijgt \(f(x) = (x - 3)^{2}\)?",
        opties=[r"\([3, +\infty[\)", r"\(]-\infty, 3]\)", r"\(\mathbb{R}\)", r"nergens"],
        antwoord=0,
        uitleg=r"Een dalparabool daalt tot de top en stijgt daarna. De top ligt bij \(x = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De parabool \(f(x) = x^{2} + 2x + 1\) raakt de \(x\)-as in één punt.",
        antwoord=True,
        uitleg=r"\(x^{2} + 2x + 1 = (x + 1)^{2}\). Die is enkel nul voor \(x = -1\): de top ligt op de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke vorm is gelijk aan \(f(x) = (x - 2)^{2} - 9\)?",
        opties=[r"\(x^{2} - 4x - 5\)", r"\(x^{2} - 4x + 13\)", r"\(x^{2} - 2x - 5\)", r"\(x^{2} + 4x - 5\)"],
        antwoord=0,
        uitleg=r"\((x - 2)^{2} = x^{2} - 4x + 4\), en \(4 - 9 = -5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tabel van een tweedegraadsfunctie: \(f(0) = 5\), \(f(1) = 2\), \(f(2) = 1\), \(f(3) = 2\), \(f(4) = 5\). Wat is de top?",
        opties=[r"\((2, 1)\)", r"\((1, 2)\)", r"\((0, 5)\)", r"\((2, 5)\)"],
        antwoord=0,
        uitleg=r"De waarden zijn symmetrisch rond \(x = 2\) en daar het kleinst: de top is \((2, 1)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(f(x) = 0{,}1x^{2}\) is de parabool smaller dan bij \(g(x) = x^{2}\).",
        antwoord=False,
        uitleg=r"Een factor tussen \(0\) en \(1\) drukt de parabool samen in de hoogte: ze wordt breder, niet smaller.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(f(x) = x^{2}\) op \([0, +\infty[\): hoe verloopt de stijging?",
        opties=[r"toenemende stijging", r"afnemende stijging", r"constante stijging", r"afnemende daling"],
        antwoord=0,
        uitleg=r"De stappen worden groter: \(0, 1, 4, 9, 16\) stijgt met \(1, 3, 5, 7\). De stijging neemt toe.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De nulwaarden van \(f(x) = (x - 4)(x - 4)\) vallen samen.",
        antwoord=True,
        uitleg=r"Beide factoren geven \(x = 4\). Er is één nulwaarde, en die is de \(x\)-coördinaat van de top.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welk voorschrift hoort bij een parabool met top \((-1, 3)\) die door \((0, 5)\) gaat?",
        opties=[r"\(f(x) = 2(x + 1)^{2} + 3\)", r"\(f(x) = 2(x - 1)^{2} + 3\)", r"\(f(x) = 5(x + 1)^{2} + 3\)", r"\(f(x) = (x + 1)^{2} + 5\)"],
        antwoord=0,
        uitleg=r"Met top \((-1, 3)\): \(f(x) = a(x + 1)^{2} + 3\). Door \((0, 5)\): \(a + 3 = 5\), dus \(a = 2\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Je verschuift de grafiek van \(f(x) = x^{2}\) \(3\) eenheden naar boven. Welk voorschrift krijg je?",
        opties=[r"\(x^{2} + 3\)", r"\((x + 3)^{2}\)", r"\((x - 3)^{2}\)", r"\(3x^{2}\)"],
        antwoord=0,
        uitleg=r"Een verticale verschuiving \(f(x) + k\) telt \(k\) op bij elke functiewaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je verschuift de grafiek van \(f(x) = x^{2}\) \(3\) eenheden naar rechts. Welk voorschrift krijg je?",
        opties=[r"\((x - 3)^{2}\)", r"\((x + 3)^{2}\)", r"\(x^{2} - 3\)", r"\(x^{2} + 3\)"],
        antwoord=0,
        uitleg=r"Een horizontale verschuiving naar rechts is \(f(x - k)\): naar rechts geeft een minteken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie zet de grafiek van \(x^{2}\) om in die van \(-x^{2}\)?",
        opties=[r"een spiegeling rond de \(x\)-as", r"een spiegeling rond de \(y\)-as", r"een verschuiving naar beneden", r"een horizontale verschuiving"],
        antwoord=0,
        uitleg=r"Elke functiewaarde wordt haar tegengestelde: de dalparabool klapt om tot een bergparabool.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformatie zet de grafiek van \(x^{2}\) om in die van \(4x^{2}\)?",
        opties=[r"een verticale uitrekking met factor \(4\)", r"een verticale verschuiving van \(4\)", r"een horizontale verschuiving van \(4\)", r"een spiegeling rond de \(x\)-as"],
        antwoord=0,
        uitleg=r"\(k \cdot f(x)\) vermenigvuldigt elke functiewaarde met \(k\): een verticale uitrekking.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke transformaties zetten \(f(x) = x^{2}\) om in \(g(x) = 2(x + 1)^{2} - 5\)?",
        opties=[
            r"verschuiving \(1\) naar links, verticale uitrekking met factor \(2\), verschuiving \(5\) naar beneden",
            r"verschuiving \(1\) naar rechts, verticale uitrekking met factor \(2\), verschuiving \(5\) naar beneden",
            r"verschuiving \(1\) naar links, verticale uitrekking met factor \(2\), verschuiving \(5\) naar boven",
            r"verschuiving \(2\) naar links, verticale uitrekking met factor \(1\), verschuiving \(5\) naar beneden",
        ],
        antwoord=0,
        uitleg=r"\(x + 1 = x - (-1)\): \(1\) naar links. De factor \(2\) rekt uit, de \(-5\) verschuift naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je spiegelt \(f(x) = x^{2}\) rond de \(x\)-as en verschuift ze daarna \(6\) eenheden naar boven. Welk voorschrift krijg je?",
        opties=[r"\(-x^{2} + 6\)", r"\(-(x^{2} + 6)\)", r"\(-(x - 6)^{2}\)", r"\(x^{2} - 6\)"],
        antwoord=0,
        uitleg=r"Eerst spiegelen geeft \(-x^{2}\). Daarna komt er \(6\) bij: \(-x^{2} + 6\). Bij \(-(x^{2} + 6)\) gebeurt het in de omgekeerde volgorde.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De top van \(g(x) = (x - 5)^{2} + 2\) ligt \(5\) eenheden rechts en \(2\) eenheden boven de top van \(x^{2}\).",
        antwoord=True,
        uitleg=r"De top van \(x^{2}\) is \((0, 0)\), die van \(g\) is \((5, 2)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een verticale uitrekking van een parabool verandert de \(x\)-coördinaat van de top.",
        antwoord=False,
        uitleg=r"Een verticale uitrekking verandert enkel de functiewaarden. De top van \(k \cdot x^{2}\) blijft \((0, 0)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bal volgt de baan \(h(x) = -0{,}05x^{2} + x + 2\), met \(x\) de horizontale afstand en \(h\) de hoogte, beide in meter. Op welke afstand is de bal het hoogst?",
        opties=[r"\(10\) m", r"\(7\) m", r"\(20\) m", r"\(2\) m"],
        antwoord=0,
        uitleg=r"De top ligt bij \(x = -\dfrac{1}{2 \cdot (-0{,}05)} = \dfrac{1}{0{,}1} = 10\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(h(x) = -0{,}05x^{2} + x + 2\): hoeveel meter is de grootste hoogte van de bal? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg=r"\(h(10) = -0{,}05 \cdot 100 + 10 + 2 = -5 + 12 = 7\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(h(x) = -0{,}05x^{2} + x + 2\): op welke hoogte in meter vertrekt de bal? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"Bij de start is \(x = 0\): \(h(0) = 2\). Dat is het snijpunt met de \(y\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een boer zet met \(40\) m draad een rechthoekige weide af. Is de breedte \(x\) meter, dan is de oppervlakte \(A(x) = x(20 - x)\). Wat is het praktisch domein?",
        opties=[r"\([0, 20]\)", r"\([0, 40]\)", r"\(\mathbb{R}\)", r"\([0, 100]\)"],
        antwoord=0,
        uitleg=r"De lengte is \(20 - x\). Breedte en lengte kunnen niet negatief zijn, dus \(0 \le x \le 20\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(A(x) = x(20 - x)\): hoeveel vierkante meter is de grootste oppervlakte? Schrijf het getal.",
        antwoord=["100", "honderd"],
        uitleg=r"De nulwaarden zijn \(0\) en \(20\), dus de top ligt bij \(x = 10\): \(A(10) = 10 \cdot 10 = 100\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(A(x) = x(20 - x)\) is de grootste weide een vierkant.",
        antwoord=True,
        uitleg=r"Bij \(x = 10\) is de lengte \(20 - 10 = 10\): breedte en lengte zijn gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke tweedegraadsfunctie heeft geen snijpunt met de \(x\)-as?",
        opties=[r"\(f(x) = (x - 1)^{2} + 2\)", r"\(f(x) = (x - 1)^{2} - 2\)", r"\(f(x) = -(x - 1)^{2} + 2\)", r"\(f(x) = (x - 1)^{2}\)"],
        antwoord=0,
        uitleg=r"Een dalparabool met top \((1, 2)\) ligt helemaal boven de \(x\)-as.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe ziet het tekenverloop eruit van \(f(x) = (x - 1)(x - 5)\)?",
        opties=[
            r"\(+\) voor \(x < 1\), \(-\) tussen \(1\) en \(5\), \(+\) voor \(x > 5\)",
            r"\(-\) voor \(x < 1\), \(+\) tussen \(1\) en \(5\), \(-\) voor \(x > 5\)",
            r"\(+\) overal behalve in \(1\) en \(5\)",
            r"\(-\) voor \(x < 5\) en \(+\) voor \(x > 5\)",
        ],
        antwoord=0,
        uitleg=r"Het is een dalparabool (\(a = 1 > 0\)): tussen de nulwaarden onder de \(x\)-as, daarbuiten erboven.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(g(x) = (x + 2)^{2}\) ontstaat uit die van \(x^{2}\) door een verschuiving van \(2\) eenheden naar rechts.",
        antwoord=False,
        uitleg=r"\(x + 2 = x - (-2)\): de verschuiving gaat \(2\) eenheden naar links. De top is \((-2, 0)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een winkel verkoopt bij een prijs van \(p\) euro per stuk een omzet \(O(p) = -4p^{2} + 160p\). Bij welke prijs is de omzet het grootst?",
        opties=[r"\(20\) euro", r"\(40\) euro", r"\(160\) euro", r"\(10\) euro"],
        antwoord=0,
        uitleg=r"\(p = -\dfrac{160}{2 \cdot (-4)} = 20\). Het is een bergparabool, dus de top is een maximum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafiek van \(f(x) = -3x^{2}\) is een bergparabool die steiler is dan die van \(-x^{2}\).",
        antwoord=True,
        uitleg=r"De factor \(3\) rekt de grafiek verticaal uit, het minteken maakt er een bergparabool van.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een parabool heeft nulwaarden \(0\) en \(8\) en gaat door \((4, 32)\). Welk voorschrift past?",
        opties=[r"\(f(x) = -2x(x - 8)\)", r"\(f(x) = 2x(x - 8)\)", r"\(f(x) = -2x(x + 8)\)", r"\(f(x) = x(x - 8) + 32\)"],
        antwoord=0,
        uitleg=r"\(f(x) = a \cdot x(x - 8)\). In \(x = 4\): \(a \cdot 4 \cdot (-4) = -16a = 32\), dus \(a = -2\).",
    ),
]
