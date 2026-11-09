# -*- coding: utf-8 -*-
"""Vergelijkingen grafisch oplossen.

Wiskunde basis, derde graad. De fiche vraagt: het verband tussen de
oplossingen van f(x) = 0 en de nulwaarden van f, en tussen f(x) = g(x) en de
gemeenschappelijke punten van twee grafieken; veeltermvergelijkingen,
exponentiële vergelijkingen die te herleiden zijn tot b·a^x + c = 0 en
goniometrische vergelijkingen die te herleiden zijn tot a·sin b(x − c) + d = 0.
Grafisch oplossen met ICT, de oplossingenverzameling noteren en het
resultaat in de context formuleren. Algebraïsch oplossen van exponentiële of
goniometrische vergelijkingen vraagt deze fiche niet.

Deel 1: het grafisch verband. Deel 2: vraagstukken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat zijn de oplossingen van \(f(x) = 0\) op de grafiek van \(f\)?",
        opties=[
            r"de \(x\)-coördinaten van de snijpunten met de \(x\)-as",
            r"de \(y\)-coördinaat van het snijpunt met de \(y\)-as",
            r"de \(x\)-coördinaten van de toppen",
            r"de \(y\)-coördinaten van de snijpunten met de \(x\)-as",
        ],
        antwoord=0,
        uitleg=r"De oplossingen van \(f(x) = 0\) zijn de nulwaarden van \(f\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe los je \(f(x) = g(x)\) grafisch op?",
        opties=[
            r"Je tekent beide grafieken en leest de \(x\)-coördinaten van hun snijpunten af.",
            r"Je tekent beide grafieken en leest de \(y\)-coördinaten van hun snijpunten af.",
            r"Je zoekt de nulwaarden van \(f\) en die van \(g\).",
            r"Je zoekt de toppen van beide grafieken.",
        ],
        antwoord=0,
        uitleg=r"In een snijpunt is \(f(x) = g(x)\). De oplossing is de \(x\)-waarde van dat punt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke notatie gebruik je voor de oplossingenverzameling?",
        opties=[r"\(V\)", r"\(\text{dom}\)", r"\(\text{ber}\)", r"\(D\)"],
        antwoord=0,
        uitleg=r"Volgens de afspraken van de Examencommissie noteer je de oplossingenverzameling als \(V\), bijvoorbeeld \(V = \{1, 4\}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafieken van \(f\) en \(g\) snijden elkaar in \((-1, 3)\) en \((2, 6)\). Wat is de oplossingenverzameling van \(f(x) = g(x)\)?",
        opties=[r"\(V = \{-1, 2\}\)", r"\(V = \{3, 6\}\)", r"\(V = \{(-1, 3), (2, 6)\}\)", r"\(V = \{-1, 2, 3, 6\}\)"],
        antwoord=0,
        uitleg=r"De oplossingen zijn \(x\)-waarden. De \(y\)-waarden zijn de gemeenschappelijke functiewaarden.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als twee grafieken elkaar niet snijden, dan is \(V = \varnothing\) voor \(f(x) = g(x)\).",
        antwoord=True,
        uitleg=r"Geen gemeenschappelijk punt betekent geen \(x\) waarvoor beide functiewaarden gelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je wil \(x^{3} - 2x = 1\) grafisch oplossen. Welke twee grafieken kan je tekenen?",
        opties=[r"\(y = x^{3} - 2x\) en \(y = 1\)", r"\(y = x^{3}\) en \(y = 1\)", r"\(y = x^{3} - 2x\) en \(y = 0\)", r"\(y = -2x\) en \(y = 1\)"],
        antwoord=0,
        uitleg=r"Linkerlid en rechterlid worden elk een functie. Je kan ook \(y = x^{3} - 2x - 1\) tekenen en de nulwaarden zoeken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \(x^{3} - 2x = 1\) heeft dezelfde oplossingen als de nulwaarden van \(h(x) = x^{3} - 2x - 1\).",
        antwoord=True,
        uitleg=r"Breng alles naar één kant: \(x^{3} - 2x - 1 = 0\), dus \(h(x) = 0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel oplossingen heeft \(2^{x} = -3\)?",
        opties=[r"geen", r"één", r"twee", r"oneindig veel"],
        antwoord=0,
        uitleg=r"De grafiek van \(2^{x}\) ligt helemaal boven de \(x\)-as en kan de rechte \(y = -3\) dus niet snijden.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel oplossingen heeft \(\sin x = \dfrac{1}{2}\) op \([0, 2\pi]\)?",
        opties=[r"twee", r"één", r"geen", r"oneindig veel"],
        antwoord=0,
        uitleg=r"De rechte \(y = \tfrac{1}{2}\) snijdt één golf van de sinus twee keer: in \(\dfrac{\pi}{6}\) en in \(\dfrac{5\pi}{6}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De vergelijking \(\sin x = 2\) heeft oplossingen.",
        antwoord=False,
        uitleg=r"Het bereik van \(\sin x\) is \([-1, 1]\). De rechte \(y = 2\) ligt erboven.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Op heel \(\mathbb{R}\) heeft \(\sin x = 0{,}3\) oneindig veel oplossingen.",
        antwoord=True,
        uitleg=r"De sinus is periodiek: elke periode \(2\pi\) levert opnieuw twee oplossingen op.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke vergelijking is te herleiden tot de vorm \(b \cdot a^{x} + c = 0\)?",
        opties=[r"\(3 \cdot 2^{x} = 24\)", r"\(x^{2} = 24\)", r"\(3 \sin x = 2\)", r"\(3x + 2 = 24\)"],
        antwoord=0,
        uitleg=r"\(3 \cdot 2^{x} - 24 = 0\): grondtal \(2\), \(b = 3\), \(c = -24\). De oplossing is \(x = 3\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Lees af of reken na: voor welke \(x\) is \(3 \cdot 2^{x} = 24\)? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(2^{x} = 8 = 2^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rekenapp toont: de grafiek van \(f(x) = x^{3} - 4x\) snijdt de \(x\)-as in \(-2\), \(0\) en \(2\). Wat is \(V\) van \(x^{3} - 4x = 0\)?",
        opties=[r"\(V = \{-2, 0, 2\}\)", r"\(V = \{-2, 2\}\)", r"\(V = \{0\}\)", r"\(V = \{-4, 0, 4\}\)"],
        antwoord=0,
        uitleg=r"Elke nulwaarde is een oplossing, ook \(0\). Controle: \(x(x^{2} - 4) = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een veeltermvergelijking van de derde graad heeft altijd precies drie oplossingen.",
        antwoord=False,
        uitleg=r"Ze kan er één, twee of drie hebben. \(x^{3} = 8\) heeft er maar één: \(x = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De grafiek van \(f(x) = x^{2} - 4x + 3\) en de rechte \(y = 3\) snijden elkaar in \(x = 0\) en \(x = 4\). Wat is dan \(V\) van \(x^{2} - 4x = 0\)?",
        opties=[r"\(V = \{0, 4\}\)", r"\(V = \{1, 3\}\)", r"\(V = \{3\}\)", r"\(V = \{-4, 0\}\)"],
        antwoord=0,
        uitleg=r"\(x^{2} - 4x + 3 = 3 \iff x^{2} - 4x = 0\): het is dezelfde vergelijking.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat doe je met een oplossing die een rekenapp geeft als \(x \approx 1{,}7320508\)?",
        opties=[
            r"Je rondt af zoals de opgave vraagt, bijvoorbeeld \(1{,}73\).",
            r"Je schrijft altijd alle cijfers op die de app toont.",
            r"Je rondt altijd af op een geheel getal: \(2\).",
            r"Je laat de oplossing weg omdat ze niet exact is.",
        ],
        antwoord=0,
        uitleg=r"Grafisch oplossen geeft benaderingen. Je werkt zo nauwkeurig mogelijk en rondt pas op het einde af.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een vergelijking grafisch oplossen geeft soms een benadering in plaats van een exacte waarde.",
        antwoord=True,
        uitleg=r"Een rekenapp toont een afgeronde coördinaat. Daarom noteer je hoe nauwkeurig je afrondt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel oplossingen heeft \(2 \sin x + 1 = 0\) op \([0, 2\pi]\)?",
        opties=[r"twee", r"één", r"drie", r"geen"],
        antwoord=0,
        uitleg=r"\(\sin x = -\tfrac{1}{2}\). Die rechte snijdt één golf twee keer, in het derde en het vierde kwadrant.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(5 \cdot 3^{x} + 2 = 0\) heeft een oplossing.",
        antwoord=False,
        uitleg=r"\(5 \cdot 3^{x} > 0\), dus \(5 \cdot 3^{x} + 2 > 2\). De grafiek raakt de \(x\)-as nooit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Je hebt \(1000\) euro tegen \(4\%\) per jaar. Na hoeveel jaar heb je \(1500\) euro? Welke vergelijking los je grafisch op?",
        opties=[r"\(1000 \cdot 1{,}04^{t} = 1500\)", r"\(1000 + 1{,}04t = 1500\)", r"\(1000 \cdot 0{,}04^{t} = 1500\)", r"\(1500 \cdot 1{,}04^{t} = 1000\)"],
        antwoord=0,
        uitleg=r"Snijd de grafiek van \(1000 \cdot 1{,}04^{t}\) met de rechte \(y = 1500\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het snijpunt van \(y = 1000 \cdot 1{,}04^{t}\) en \(y = 1500\) ligt bij \(t \approx 10{,}34\). Hoe formuleer je het antwoord?",
        opties=[
            r"Na \(11\) jaar staat er voor het eerst meer dan \(1500\) euro op de rekening.",
            r"Na \(10\) jaar staat er precies \(1500\) euro op de rekening.",
            r"Na \(10{,}34\) euro is het bedrag \(1500\) jaar.",
            r"Het bedrag wordt nooit \(1500\) euro.",
        ],
        antwoord=0,
        uitleg=r"De intrest komt er per jaar bij. Na \(10\) jaar is het nog te weinig (\(\approx 1480\) euro), na \(11\) jaar genoeg.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een plant is \(h(t) = 2 \cdot 1{,}5^{t}\) cm hoog na \(t\) weken. Na hoeveel weken is ze \(13{,}5\) cm? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(2 \cdot 1{,}5^{t} = 13{,}5 \iff 1{,}5^{t} = 6{,}75 = 1{,}5^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee gsm-abonnementen: A kost \(10 + 0{,}05x\) euro en B kost \(4 + 0{,}10x\) euro voor \(x\) minuten. Bij hoeveel minuten kosten ze evenveel?",
        opties=[r"\(120\)", r"\(60\)", r"\(140\)", r"\(200\)"],
        antwoord=0,
        uitleg=r"\(10 + 0{,}05x = 4 + 0{,}10x \iff 6 = 0{,}05x \iff x = 120\). Grafisch: het snijpunt van twee rechten.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij de abonnementen van de vorige vraag is A goedkoper als je meer dan \(120\) minuten belt.",
        antwoord=True,
        uitleg=r"Na het snijpunt ligt de rechte van A onder die van B, omdat A minder per minuut kost.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De temperatuur in een stad is \(T(m) = 8 \sin\left(\dfrac{\pi}{6}(m - 4)\right) + 12\), met \(m\) de maand. Hoe vind je de maanden waarin het gemiddeld \(16\) graden is?",
        opties=[
            r"Je snijdt de grafiek van \(T\) met de rechte \(y = 16\).",
            r"Je zoekt de nulwaarden van \(T\).",
            r"Je zoekt het maximum van \(T\).",
            r"Je berekent \(T(16)\).",
        ],
        antwoord=0,
        uitleg=r"De vraag is \(T(m) = 16\). Grafisch zijn dat de \(x\)-waarden van de snijpunten met \(y = 16\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij die temperatuur \(T(m) = 8 \sin\left(\dfrac{\pi}{6}(m - 4)\right) + 12\): wat is de hoogste gemiddelde temperatuur?",
        opties=[r"\(20\) graden", r"\(12\) graden", r"\(8\) graden", r"\(16\) graden"],
        antwoord=0,
        uitleg=r"Evenwichtslijn plus amplitude: \(12 + 8 = 20\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een medicijn: \(M(t) = 400 \cdot 0{,}5^{t}\) mg na \(t\) uur. Na hoeveel uur is er \(50\) mg over? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(0{,}5^{t} = \dfrac{50}{400} = \dfrac{1}{8} = 0{,}5^{3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een doos zonder deksel uit een karton van \(20\) bij \(20\) cm heeft inhoud \(I(x) = x(20 - 2x)^{2}\). Een rekenapp geeft voor \(I(x) = 500\) de oplossingen \(x \approx 1{,}91\), \(x = 5\) en \(x \approx 13{,}09\). Welke oplossingen passen in de context?",
        opties=[r"\(1{,}91\) en \(5\)", r"alle drie", r"enkel \(13{,}09\)", r"enkel \(5\)"],
        antwoord=0,
        uitleg=r"Je snijdt aan elke kant \(x\) cm weg, dus \(x < 10\). De oplossing \(13{,}09\) valt buiten het praktisch domein \(]0, 10[\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een vraagstuk hoort elke oplossing van de vergelijking ook bij het antwoord.",
        antwoord=False,
        uitleg=r"Je controleert of de oplossing in het praktisch domein ligt, zoals een positieve tijd of een mogelijke lengte.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vijver raakt vol algen: \(A(t) = 5 \cdot 1{,}2^{t}\) m² na \(t\) dagen. De vijver is \(60\) m². Welke vergelijking geeft het moment waarop hij vol is?",
        opties=[r"\(5 \cdot 1{,}2^{t} = 60\)", r"\(5 + 1{,}2t = 60\)", r"\(60 \cdot 1{,}2^{t} = 5\)", r"\(5 \cdot 1{,}2 \cdot t = 60\)"],
        antwoord=0,
        uitleg=r"Vol betekent een oppervlakte van \(60\) m²: \(A(t) = 60\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(5 \cdot 1{,}2^{t} = 60\) toont de rekenapp het snijpunt bij \(t \approx 13{,}63\). Wat is het antwoord?",
        opties=[r"na ongeveer \(13{,}6\) dagen", r"na ongeveer \(60\) dagen", r"na \(12\) dagen", r"na ongeveer \(5\) dagen"],
        antwoord=0,
        uitleg=r"De \(x\)-coördinaat van het snijpunt is de tijd. De \(y\)-coördinaat \(60\) is de oppervlakte.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Om \(f(x) = 5\) grafisch op te lossen, mag je de rechte \(y = 5\) tekenen en de snijpunten met de grafiek van \(f\) zoeken.",
        antwoord=True,
        uitleg=r"Dat is \(f(x) = g(x)\) met \(g(x) = 5\), een horizontale rechte.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De hoogte van een bakje in een reuzenrad is \(h(t) = 15 \sin\left(\dfrac{\pi}{4} t\right) + 17\) m. Hoe vaak is het bakje tijdens één toer op \(17\) m hoogte?",
        opties=[r"twee keer", r"één keer", r"vier keer", r"nooit"],
        antwoord=0,
        uitleg=r"\(17\) m is de evenwichtslijn. Tijdens één periode gaat de grafiek er twee keer door: één keer omhoog, één keer omlaag.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(h(t) = 15 \sin\left(\dfrac{\pi}{4} t\right) + 17\): hoeveel minuten duurt één toer? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg=r"Periode \(= \dfrac{2\pi}{\pi/4} = 8\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bedrijf heeft kosten \(K(q) = 0{,}5q^{2} + 400\) en opbrengst \(O(q) = 30q\). Hoe vind je grafisch bij welke aantallen kosten en opbrengst gelijk zijn?",
        opties=[
            r"Je zoekt de snijpunten van de grafieken van \(K\) en \(O\).",
            r"Je zoekt de top van \(K\).",
            r"Je zoekt de nulwaarden van \(O\).",
            r"Je zoekt waar \(K\) de \(y\)-as snijdt.",
        ],
        antwoord=0,
        uitleg=r"Gelijk betekent \(K(q) = O(q)\): de snijpunten. Daartussen ligt de opbrengst boven de kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(0{,}5q^{2} + 400 = 30q\): welke aantallen zijn de oplossingen?",
        opties=[r"\(20\) en \(40\)", r"\(10\) en \(50\)", r"\(30\)", r"\(15\) en \(45\)"],
        antwoord=0,
        uitleg=r"\(0{,}5q^{2} - 30q + 400 = 0 \iff q^{2} - 60q + 800 = 0 \iff (q - 20)(q - 40) = 0\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee exponentiële functies \(2^{x}\) en \(3^{x}\) hebben één gemeenschappelijk punt.",
        antwoord=True,
        uitleg=r"Ze snijden elkaar enkel in \((0, 1)\). Voor \(x > 0\) ligt \(3^{x}\) erboven, voor \(x < 0\) eronder.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een populatie vissen: \(N(t) = 2000 \cdot 0{,}9^{t}\). Wanneer zakt ze onder de \(1000\)? De rekenapp geeft het snijpunt met \(y = 1000\) bij \(t \approx 6{,}58\).",
        opties=[r"in het zevende jaar", r"na \(6{,}58\) vissen", r"na \(1000\) jaar", r"in het tiende jaar"],
        antwoord=0,
        uitleg=r"Tussen \(t = 6\) en \(t = 7\) zakt de grafiek onder de rechte \(y = 1000\): in het zevende jaar.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een grafiek die de rechte \(y = 4\) raakt zonder ze te snijden, levert voor \(f(x) = 4\) geen oplossing op.",
        antwoord=False,
        uitleg=r"Een raakpunt is ook een gemeenschappelijk punt. De \(x\)-waarde ervan is een oplossing.",
    ),
]
