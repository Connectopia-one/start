# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: verloop van een functie en optimaliseren.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED): het verloop
van een functie met de eerste en tweede afgeleide (stijgen/dalen, extrema,
hol/bol, buigpunten, samenvattende tabel) en extremumproblemen oplossen
(veranderlijke kiezen, voorschrift opstellen, extrema berekenen, tweede
afgeleide test, praktisch domein, antwoord formuleren).

Deel 1: verloop met eerste en tweede afgeleide. Deel 2: extremumproblemen.
"""

DEEL1 = [
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(x) > 0\) op een interval, dan stijgt \(f\) op dat interval.",
        antwoord=True,
        uitleg=r"Een positieve afgeleide betekent een positieve helling.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Gegeven \(f(x) = x^{3} - 3x\). Waar heeft \(f\) een relatief maximum?",
        opties=[r"bij \(x = -1\)", r"bij \(x = 1\)", r"bij \(x = 0\)", r"bij \(x = \sqrt{3}\)"],
        antwoord=0,
        uitleg=r"\(f'(x) = 3x^{2} - 3 = 0\) bij \(x = \pm 1\). Het teken van \(f'\) gaat van \(+\) naar \(-\) bij \(x = -1\): daar is een maximum.",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = x^{3} - 3x\). Wat is de waarde van het relatief minimum?",
        antwoord=["-2", "−2", "min 2"],
        uitleg=r"Het minimum ligt bij \(x = 1\): \(f(1) = 1 - 3 = -2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een tabel van het waardenverloop gaat het teken van \(f'\) bij \(x = a\) van \(-\) naar \(+\). Wat heeft \(f\) daar?",
        opties=[r"een relatief minimum", r"een relatief maximum", r"een buigpunt", r"een verticale asymptoot"],
        antwoord=0,
        uitleg=r"Eerst dalen, dan stijgen: een dal.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(a) = 0\), dan heeft \(f\) altijd een extremum in \(a\).",
        antwoord=False,
        uitleg=r"Neem \(f(x) = x^{3}\): \(f'(0) = 0\), maar \(f\) stijgt links en rechts van \(0\). Het teken van \(f'\) moet wisselen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat zegt \(f''(x) > 0\) op een interval over de grafiek van \(f\)?",
        opties=[r"de grafiek is hol (dalparabool-vorm)", r"de grafiek is bol (bergparabool-vorm)", r"de functie stijgt", r"de functie is positief"],
        antwoord=0,
        uitleg=r"Als \(f''\) positief is, neemt de helling toe: de grafiek buigt naar boven, hol.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is een buigpunt?",
        opties=[
            r"een punt waar de grafiek van hol naar bol gaat of omgekeerd",
            r"een punt waar de functie het grootst is",
            r"een punt waar de raaklijn horizontaal is",
            r"een snijpunt met de \(x\)-as",
        ],
        antwoord=0,
        uitleg=r"Bij een buigpunt wisselt het teken van \(f''\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = x^{3} - 6x^{2} + 5\). Bij welke \(x\) ligt het buigpunt?",
        antwoord=["2", "twee", "x = 2", "x=2"],
        uitleg=r"\(f''(x) = 6x - 12 = 0\) bij \(x = 2\), en het teken van \(f''\) wisselt daar.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Gegeven \(f(x) = x^{3} - 6x^{2} + 5\). Waar is de grafiek bol?",
        opties=[r"voor \(x < 2\)", r"voor \(x > 2\)", r"voor \(0 < x < 4\)", r"nergens"],
        antwoord=0,
        uitleg=r"\(f''(x) = 6x - 12 < 0\) als \(x < 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een functie kan stijgen en tegelijk bol zijn.",
        antwoord=True,
        uitleg=r"Dan stijgt ze steeds trager: afnemende stijging. Denk aan \(\sqrt{x}\) of \(\ln x\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"\(f' > 0\) en \(f'' < 0\) op een interval. Hoe noem je dat stuk van de grafiek?",
        opties=[r"afnemende stijging", r"toenemende stijging", r"afnemende daling", r"toenemende daling"],
        antwoord=0,
        uitleg=r"\(f\) stijgt (\(f' > 0\)), maar de helling wordt kleiner (\(f'' < 0\)).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke onderdelen horen in een samenvattende tabel?",
        opties=[
            r"het teken van \(f'\) en \(f''\), stijgen/dalen, hol/bol, extrema en buigpunten",
            r"enkel de nulwaarden van \(f\)",
            r"enkel het teken van \(f\)",
            r"de waarden van \(f\) in gehele getallen",
        ],
        antwoord=0,
        uitleg=r"Alles uit de eerste en tweede afgeleide staat samen in één tabel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Gegeven \(f(x) = x^{4} - 2x^{2}\). Welke \(x\)-waarden zijn kandidaat-extrema?",
        opties=[r"\(-1\), \(0\) en \(1\)", r"enkel \(0\)", r"\(-\sqrt{2}\), \(0\) en \(\sqrt{2}\)", r"\(-1\) en \(1\)"],
        antwoord=0,
        uitleg=r"\(f'(x) = 4x^{3} - 4x = 4x(x - 1)(x + 1)\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(f(x) = x^{4} - 2x^{2}\) is \(x = 0\) een relatief minimum.",
        antwoord=False,
        uitleg=r"Het teken van \(f'\) gaat bij \(0\) van \(+\) naar \(-\): een relatief maximum. De minima liggen bij \(x = \pm 1\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op de grafiek van \(f'\) zie je een nulpunt in \(x = 3\), met \(f'\) positief links en negatief rechts. Wat weet je over \(f\)?",
        opties=[r"\(f\) heeft een maximum in \(x = 3\)", r"\(f\) heeft een minimum in \(x = 3\)", r"\(f\) heeft een buigpunt in \(x = 3\)", r"\(f(3) = 0\)"],
        antwoord=0,
        uitleg=r"\(f\) stijgt tot \(3\) en daalt daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f'\) heeft een top in \(x = 1\). Wat heeft \(f\) dan in \(x = 1\)?",
        opties=[r"een buigpunt", r"een maximum", r"een minimum", r"een nulpunt"],
        antwoord=0,
        uitleg=r"Een extremum van \(f'\) betekent dat \(f''\) daar van teken wisselt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Gegeven \(f(x) = 2x^{3} - 3x^{2} - 12x\). Bij welke \(x\) ligt het relatief minimum?",
        antwoord=["2", "twee", "x = 2", "x=2"],
        uitleg=r"\(f'(x) = 6x^{2} - 6x - 12 = 6(x - 2)(x + 1)\). Bij \(x = 2\) gaat het teken van \(-\) naar \(+\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een tweedegraadsfunctie heeft nooit een buigpunt.",
        antwoord=True,
        uitleg=r"\(f''\) is een constante en wisselt dus nooit van teken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het bereik van \(f(x) = x^{2} - 4x + 1\) is ...",
        opties=[r"\([-3, +\infty[\)", r"\(]-\infty, -3]\)", r"\([2, +\infty[\)", r"\(\mathbb{R}\)"],
        antwoord=0,
        uitleg=r"\(f'(x) = 2x - 4 = 0\) bij \(x = 2\), en \(f(2) = -3\) is het absolute minimum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f''(a) = 0\), dan is er zeker een buigpunt in \(a\).",
        antwoord=False,
        uitleg=r"Bij \(f(x) = x^{4}\) is \(f''(0) = 0\), maar de grafiek blijft hol. Het teken van \(f''\) moet wisselen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de eerste stap bij een extremumprobleem?",
        opties=[
            r"een veranderlijke kiezen en het voorschrift opstellen",
            r"de tweede afgeleide berekenen",
            r"het antwoord gokken en controleren",
            r"de nulwaarden van de functie zoeken",
        ],
        antwoord=0,
        uitleg=r"Daarna: afgeleide, nulwaarden, controleren of het een maximum of minimum is, antwoord in een zin.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met \(40\) m hekwerk maak je een rechthoekige weide. Noem één zijde \(x\). Welke functie geeft de oppervlakte?",
        opties=[r"\(A(x) = x(20 - x)\)", r"\(A(x) = x(40 - x)\)", r"\(A(x) = 2x + 40\)", r"\(A(x) = x^{2}\)"],
        antwoord=0,
        uitleg=r"\(2x + 2y = 40\), dus \(y = 20 - x\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij die weide \(A(x) = x(20 - x)\): hoe lang moet \(x\) zijn voor de grootste oppervlakte? Schrijf het getal in meter.",
        antwoord=["10", "10 m", "tien"],
        uitleg=r"\(A'(x) = 20 - 2x = 0\) bij \(x = 10\). De weide wordt een vierkant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het praktisch domein van \(A(x) = x(20 - x)\) bij die weide?",
        opties=[r"\(]0, 20[\)", r"\(\mathbb{R}\)", r"\([0, 40]\)", r"\(]0, +\infty[\)"],
        antwoord=0,
        uitleg=r"Beide zijden moeten positief zijn: \(x > 0\) en \(20 - x > 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(a) = 0\) en \(f''(a) < 0\), dan heeft \(f\) een maximum in \(a\).",
        antwoord=True,
        uitleg=r"Dat is de tweede afgeleide test: horizontale raaklijn en bol, dus een top.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als \(f'(a) = 0\) en \(f''(a) > 0\), dan heeft \(f\) een maximum in \(a\).",
        antwoord=False,
        uitleg=r"\(f''(a) > 0\) betekent hol: dat is een minimum.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De winst van een bedrijf is \(W(q) = -2q^{2} + 160q - 1200\) euro, met \(q\) het aantal stuks. Bij welk aantal is de winst het grootst?",
        opties=[r"\(40\) stuks", r"\(80\) stuks", r"\(160\) stuks", r"\(20\) stuks"],
        antwoord=0,
        uitleg=r"\(W'(q) = -4q + 160 = 0\) bij \(q = 40\), en \(W''(q) = -4 < 0\): een maximum.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij die winstfunctie \(W(q) = -2q^{2} + 160q - 1200\): hoeveel euro is de grootste winst?",
        antwoord=["2000", "2 000", "2.000", "2000 euro"],
        uitleg=r"\(W(40) = -3200 + 6400 - 1200 = 2000\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Uit een vierkant stuk karton van \(12\) cm zijde knip je in elke hoek een vierkantje met zijde \(x\) weg en plooi je een open doos. Welke functie geeft de inhoud?",
        opties=[r"\(V(x) = x(12 - 2x)^{2}\)", r"\(V(x) = x(12 - x)^{2}\)", r"\(V(x) = (12 - 2x)^{2}\)", r"\(V(x) = 12x^{2}\)"],
        antwoord=0,
        uitleg=r"De bodem is een vierkant met zijde \(12 - 2x\), de hoogte is \(x\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij die doos \(V(x) = x(12 - 2x)^{2}\): bij welke \(x\) is de inhoud het grootst? Schrijf het getal in cm.",
        antwoord=["2", "2 cm", "twee"],
        uitleg=r"\(V'(x) = (12 - 2x)^{2} - 4x(12 - 2x) = (12 - 2x)(12 - 6x)\). Nul bij \(x = 6\) (geen doos) en \(x = 2\). In \(]0, 6[\) is \(x = 2\) het maximum.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij de doos valt de oplossing \(x = 6\) weg omdat ze buiten het praktisch domein ligt.",
        antwoord=True,
        uitleg=r"Bij \(x = 6\) is de bodem \(0\) cm breed: er is geen doos.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom controleer je bij een extremumprobleem of het gevonden punt een maximum of een minimum is?",
        opties=[
            r"omdat \(f' = 0\) alleen zegt dat de raaklijn horizontaal is",
            r"omdat de afgeleide soms fout is",
            r"omdat er altijd twee antwoorden zijn",
            r"dat hoeft niet, het is altijd een maximum",
        ],
        antwoord=0,
        uitleg=r"Een horizontale raaklijn kan bij een maximum, een minimum of geen van beide horen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De gemiddelde kost per stuk is \(G(q) = q + \dfrac{400}{q}\) euro (\(q > 0\)). Bij welk aantal stuks is die het laagst?",
        opties=[r"\(20\)", r"\(400\)", r"\(40\)", r"\(10\)"],
        antwoord=0,
        uitleg=r"\(G'(q) = 1 - \dfrac{400}{q^{2}} = 0\) bij \(q = 20\). \(G''(q) = \dfrac{800}{q^{3}} > 0\): een minimum.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(G(q) = q + \dfrac{400}{q}\): wat is de laagste gemiddelde kost per stuk in euro?",
        antwoord=["40", "40 euro"],
        uitleg=r"\(G(20) = 20 + 20 = 40\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een extremumprobleem met een praktisch domein \([a, b]\) kan het grootste resultaat ook in een grenspunt \(a\) of \(b\) liggen.",
        antwoord=True,
        uitleg=r"Vergelijk daarom ook de functiewaarden in de grenzen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee positieve getallen hebben als som \(30\). Hun product moet zo groot mogelijk zijn. Welke getallen?",
        opties=[r"\(15\) en \(15\)", r"\(10\) en \(20\)", r"\(1\) en \(29\)", r"\(5\) en \(25\)"],
        antwoord=0,
        uitleg=r"\(P(x) = x(30 - x)\), \(P'(x) = 30 - 2x = 0\) bij \(x = 15\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een functie \(f(x) = x \cdot e^{-x}\) met \(x \ge 0\). Waar ligt het maximum?",
        opties=[r"bij \(x = 1\)", r"bij \(x = 0\)", r"bij \(x = e\)", r"er is geen maximum"],
        antwoord=0,
        uitleg=r"\(f'(x) = e^{-x} - x e^{-x} = (1 - x)e^{-x}\). Nul bij \(x = 1\), teken van \(+\) naar \(-\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een extremumprobleem volstaat het om de \(x\)-waarde te geven; een antwoord in een zin is niet nodig.",
        antwoord=False,
        uitleg=r"Je formuleert altijd een antwoord op de vraag, met eenheden, bijvoorbeeld \"De weide is een vierkant van \(10\) m op \(10\) m.\"",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een blikje moet \(500\) cm³ bevatten: \(\pi r^{2} h = 500\). Waarom druk je \(h\) uit in \(r\)?",
        opties=[
            r"zodat de te minimaliseren oppervlakte maar van één veranderlijke afhangt",
            r"omdat \(h\) altijd groter is dan \(r\)",
            r"om de inhoud groter te maken",
            r"dat hoeft niet, je mag twee veranderlijken laten staan",
        ],
        antwoord=0,
        uitleg=r"Je kan enkel een functie van één veranderlijke afleiden en op nul zetten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De opbrengst is \(O(p) = p(100 - 2p)\) euro bij een prijs \(p\). Bij welke prijs is de opbrengst het grootst?",
        opties=[r"\(25\) euro", r"\(50\) euro", r"\(100\) euro", r"\(20\) euro"],
        antwoord=0,
        uitleg=r"\(O'(p) = 100 - 4p = 0\) bij \(p = 25\).",
    ),
]
