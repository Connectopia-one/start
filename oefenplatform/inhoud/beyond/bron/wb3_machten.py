# -*- coding: utf-8 -*-
"""Machtswortels, machten met rationale exponent en logaritmen.

Wiskunde basis, derde graad. De fiche vraagt: n-de machtswortels, machten met
rationale exponent, het verband tussen machtsverheffing en worteltrekking,
logaritmen met willekeurig grondtal, met grondtal 10 en de natuurlijke
logaritme ln, het verband tussen macht en logaritme, en de rekenregels
(product, quotiënt, macht, veranderen van grondtal). Met getallen en met
letters. Geen logaritmische functies: die staan niet in deze fiche.

Deel 1: machtswortels en machten met rationale exponent.
Deel 2: logaritmen.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag=r"Bereken \(\sqrt[3]{64}\). Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\(4^{3} = 4 \cdot 4 \cdot 4 = 64\), dus de derdemachtswortel van \(64\) is \(4\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\sqrt[4]{81}\). Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(3^{4} = 81\). Een vierdemachtswortel is altijd positief, dus het antwoord is \(3\) en niet \(-3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sqrt[3]{-125}\)?",
        opties=[r"\(-5\)", r"\(5\)", r"\(-25\)", r"Die wortel bestaat niet in \(\mathbb{R}\)."],
        antwoord=0,
        uitleg=r"\((-5)^{3} = -125\). Een oneven machtswortel van een negatief getal bestaat wel: het resultaat is negatief.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt[4]{-16}\) is een reëel getal.",
        antwoord=False,
        uitleg=r"Een even macht van een reëel getal is nooit negatief. Een even machtswortel van een negatief getal bestaat daarom niet in \(\mathbb{R}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke macht is gelijk aan \(\sqrt[5]{x^{3}}\) (met \(x > 0\))?",
        opties=[r"\(x^{\frac{3}{5}}\)", r"\(x^{\frac{5}{3}}\)", r"\(x^{15}\)", r"\(x^{-2}\)"],
        antwoord=0,
        uitleg=r"\(\sqrt[n]{a^{m}} = a^{\frac{m}{n}}\): de exponent onder het wortelteken komt boven de breukstreep, de wortelexponent eronder.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe schrijf je \(7^{\frac{2}{3}}\) als machtswortel?",
        opties=[r"\(\sqrt[3]{7^{2}}\)", r"\(\sqrt[2]{7^{3}}\)", r"\(\dfrac{7^{2}}{3}\)", r"\(\dfrac{2}{3} \cdot 7\)"],
        antwoord=0,
        uitleg=r"De noemer van de exponent wordt de wortelexponent, de teller blijft de exponent van \(7\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(8^{\frac{2}{3}}\). Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\(8^{\frac{2}{3}} = \left(\sqrt[3]{8}\right)^{2} = 2^{2} = 4\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(16^{-\frac{1}{2}}\). Schrijf het antwoord als breuk, bijvoorbeeld 1/5.",
        antwoord=["1/4", "0,25", "0.25"],
        uitleg=r"Een negatieve exponent geeft het omgekeerde: \(16^{-\frac{1}{2}} = \dfrac{1}{16^{\frac{1}{2}}} = \dfrac{1}{\sqrt{16}} = \dfrac{1}{4}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Vereenvoudig \(a^{\frac{1}{2}} \cdot a^{\frac{1}{3}}\) (met \(a > 0\)).",
        opties=[r"\(a^{\frac{5}{6}}\)", r"\(a^{\frac{1}{6}}\)", r"\(a^{\frac{2}{5}}\)", r"\(a^{\frac{1}{5}}\)"],
        antwoord=0,
        uitleg=r"Bij een product van machten met hetzelfde grondtal tel je de exponenten op: \(\tfrac{1}{2} + \tfrac{1}{3} = \tfrac{3}{6} + \tfrac{2}{6} = \tfrac{5}{6}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Vereenvoudig \(\left(x^{\frac{3}{4}}\right)^{2}\) (met \(x > 0\)).",
        opties=[r"\(x^{\frac{3}{2}}\)", r"\(x^{\frac{11}{4}}\)", r"\(x^{\frac{9}{16}}\)", r"\(x^{\frac{3}{8}}\)"],
        antwoord=0,
        uitleg=r"Een macht van een macht: je vermenigvuldigt de exponenten. \(\tfrac{3}{4} \cdot 2 = \tfrac{6}{4} = \tfrac{3}{2}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Vereenvoudig \(\dfrac{b^{\frac{5}{2}}}{b^{\frac{1}{2}}}\) (met \(b > 0\)).",
        opties=[r"\(b^{2}\)", r"\(b^{3}\)", r"\(b^{5}\)", r"\(b^{\frac{5}{4}}\)"],
        antwoord=0,
        uitleg=r"Bij een quotiënt trek je de exponenten af: \(\tfrac{5}{2} - \tfrac{1}{2} = \tfrac{4}{2} = 2\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor \(a > 0\) geldt: \(\sqrt{a} \cdot \sqrt[3]{a} = \sqrt[6]{a^{5}}\).",
        antwoord=True,
        uitleg=r"\(a^{\frac{1}{2}} \cdot a^{\frac{1}{3}} = a^{\frac{5}{6}} = \sqrt[6]{a^{5}}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt{9 + 16} = \sqrt{9} + \sqrt{16}\).",
        antwoord=False,
        uitleg=r"Links staat \(\sqrt{25} = 5\), rechts \(3 + 4 = 7\). Een wortel van een som is niet de som van de wortels.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt[3]{2} \cdot \sqrt[3]{4} = 2\).",
        antwoord=True,
        uitleg=r"Machtswortels met dezelfde wortelexponent mag je samennemen: \(\sqrt[3]{2 \cdot 4} = \sqrt[3]{8} = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welk getal is het grootst?",
        opties=[r"\(27^{\frac{2}{3}}\)", r"\(4^{\frac{3}{2}}\)", r"\(32^{\frac{2}{5}}\)", r"\(125^{\frac{1}{3}}\)"],
        antwoord=0,
        uitleg=r"\(27^{\frac{2}{3}} = 3^{2} = 9\), \(4^{\frac{3}{2}} = 2^{3} = 8\), \(32^{\frac{2}{5}} = 2^{2} = 4\) en \(125^{\frac{1}{3}} = 5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een kubus heeft een inhoud van \(343\ \text{cm}^{3}\). Hoeveel centimeter is een ribbe? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg=r"De ribbe is \(\sqrt[3]{343} = 7\) cm, want \(7^{3} = 343\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken met je rekentoestel \(\sqrt[5]{200}\), afgerond op twee cijfers na de komma.",
        opties=[r"\(2{,}89\)", r"\(3{,}17\)", r"\(2{,}51\)", r"\(40{,}00\)"],
        antwoord=0,
        uitleg=r"\(\sqrt[5]{200} = 200^{\frac{1}{5}} \approx 2{,}885\), afgerond \(2{,}89\). Controle: \(2{,}89^{5} \approx 201\). Wie \(200 : 5\) rekent, vindt \(40\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Schrijf \(\dfrac{1}{\sqrt[4]{x^{3}}}\) als één macht van \(x\) (met \(x > 0\)).",
        opties=[r"\(x^{-\frac{3}{4}}\)", r"\(x^{-\frac{4}{3}}\)", r"\(x^{\frac{3}{4}}\)", r"\(x^{-12}\)"],
        antwoord=0,
        uitleg=r"\(\sqrt[4]{x^{3}} = x^{\frac{3}{4}}\), en één gedeeld door een macht geeft een negatieve exponent.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\left(\sqrt[3]{5}\right)^{3} = 5\).",
        antwoord=True,
        uitleg=r"Worteltrekken en machtsverheffen met dezelfde exponent heffen elkaar op: \(\left(5^{\frac{1}{3}}\right)^{3} = 5^{1} = 5\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(2^{\frac{1}{2}} = \dfrac{1}{2^{2}}\).",
        antwoord=False,
        uitleg=r"\(2^{\frac{1}{2}} = \sqrt{2} \approx 1{,}41\). Een breuk als exponent betekent een wortel, geen omgekeerde.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent \(\log_{a} x = y\)?",
        opties=[r"\(a^{y} = x\)", r"\(x^{y} = a\)", r"\(y^{a} = x\)", r"\(a \cdot y = x\)"],
        antwoord=0,
        uitleg=r"De logaritme is de exponent: \(\log_{a} x\) is het getal waartoe je \(a\) moet verheffen om \(x\) te krijgen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\log_{2} 32\). Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg=r"\(2^{5} = 32\), dus \(\log_{2} 32 = 5\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\log 1000\). Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg=r"\(\log\) zonder grondtal heeft grondtal \(10\), en \(10^{3} = 1000\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\log_{3} \dfrac{1}{9}\). Schrijf het getal.",
        antwoord=["-2", "−2", "min 2"],
        uitleg=r"\(3^{-2} = \dfrac{1}{9}\), dus \(\log_{3} \dfrac{1}{9} = -2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\log_{5} 1\)?",
        opties=[r"\(0\)", r"\(1\)", r"\(5\)", r"Dat bestaat niet."],
        antwoord=0,
        uitleg=r"Elk toegelaten grondtal tot de nulde macht is \(1\): \(5^{0} = 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\log_{2}(-8)\) bestaat niet in \(\mathbb{R}\).",
        antwoord=True,
        uitleg=r"Een positief grondtal tot eender welke macht blijft positief. Je kan dus geen logaritme nemen van een negatief getal of van \(0\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welk getal is \(e\)?",
        opties=[
            r"het grondtal van de natuurlijke logaritme, ongeveer \(2{,}718\)",
            r"het grondtal van de gewone logaritme, precies \(10\)",
            r"de verhouding van omtrek en middellijn van een cirkel, ongeveer \(3{,}14\)",
            r"de oplossing van \(x^{2} = 2\), ongeveer \(1{,}414\)",
        ],
        antwoord=0,
        uitleg=r"\(\ln x\) betekent \(\log_{e} x\), met \(e \approx 2{,}718\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(\ln e^{4}\). Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\(\ln\) heeft grondtal \(e\), en \(e\) tot de vierde is \(e^{4}\). De logaritme is dus \(4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke rekenregel is juist (met \(a, x, y\) toegelaten)?",
        opties=[
            r"\(\log_{a}(x \cdot y) = \log_{a} x + \log_{a} y\)",
            r"\(\log_{a}(x + y) = \log_{a} x \cdot \log_{a} y\)",
            r"\(\log_{a}(x \cdot y) = \log_{a} x \cdot \log_{a} y\)",
            r"\(\log_{a}(x + y) = \log_{a} x + \log_{a} y\)",
        ],
        antwoord=0,
        uitleg=r"De logaritme van een product is de som van de logaritmen. Voor een som bestaat geen eenvoudige regel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke regel geldt voor de logaritme van een quotiënt (met \(a, x, y\) toegelaten)?",
        opties=[
            r"\(\log_{a} \dfrac{x}{y} = \log_{a} x - \log_{a} y\)",
            r"\(\log_{a} \dfrac{x}{y} = \dfrac{\log_{a} x}{\log_{a} y}\)",
            r"\(\log_{a} \dfrac{x}{y} = \log_{a} y - \log_{a} x\)",
            r"\(\log_{a} \dfrac{x}{y} = \log_{a}(x - y)\)",
        ],
        antwoord=0,
        uitleg=r"De logaritme van een quotiënt is de logaritme van de teller min de logaritme van de noemer.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken zonder rekentoestel \(\log_{6} 4 + \log_{6} 9\). Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"\(\log_{6} 4 + \log_{6} 9 = \log_{6} 36 = 2\), want \(6^{2} = 36\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken zonder rekentoestel \(\log_{2} 48 - \log_{2} 3\). Schrijf het getal.",
        antwoord=["4", "vier"],
        uitleg=r"\(\log_{2} 48 - \log_{2} 3 = \log_{2} \dfrac{48}{3} = \log_{2} 16 = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe kan je \(\log_{a} x^{5}\) ook schrijven (met \(x > 0\))?",
        opties=[r"\(5 \log_{a} x\)", r"\(\left(\log_{a} x\right)^{5}\)", r"\(\log_{a} 5x\)", r"\(\log_{a} x + 5\)"],
        antwoord=0,
        uitleg=r"De logaritme van een macht: de exponent komt als factor voor de logaritme.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\log 2 + \log 5 = 1\).",
        antwoord=True,
        uitleg=r"\(\log 2 + \log 5 = \log 10 = 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\dfrac{\log 8}{\log 2} = \log 4\).",
        antwoord=False,
        uitleg=r"Met de regel voor het veranderen van grondtal is \(\dfrac{\log 8}{\log 2} = \log_{2} 8 = 3\). Een quotiënt van logaritmen is geen logaritme van een quotiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke formule bereken je \(\log_{3} 20\) op een rekentoestel dat enkel \(\log\) en \(\ln\) kent?",
        opties=[r"\(\dfrac{\log 20}{\log 3}\)", r"\(\dfrac{\log 3}{\log 20}\)", r"\(\log 20 - \log 3\)", r"\(3 \cdot \log 20\)"],
        antwoord=0,
        uitleg=r"Veranderen van grondtal: \(\log_{b} x = \dfrac{\log_{a} x}{\log_{a} b}\). Met \(a = 10\) krijg je \(\dfrac{\log 20}{\log 3}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bereken \(\log_{3} 20\) met je rekentoestel, afgerond op twee cijfers na de komma.",
        opties=[r"\(2{,}73\)", r"\(0{,}37\)", r"\(6{,}67\)", r"\(1{,}30\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{\log 20}{\log 3} \approx \dfrac{1{,}3010}{0{,}4771} \approx 2{,}73\). Controle: \(3^{2{,}73} \approx 20\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Los op: \(2^{x} = 10\). Welke uitdrukking geeft \(x\)?",
        opties=[r"\(x = \log_{2} 10\)", r"\(x = \log_{10} 2\)", r"\(x = \dfrac{10}{2}\)", r"\(x = \sqrt{10}\)"],
        antwoord=0,
        uitleg=r"Het verband tussen macht en logaritme: \(2^{x} = 10 \iff x = \log_{2} 10 \approx 3{,}32\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Voor \(x > 0\) geldt: \(\ln x^{2} = 2 \ln x\).",
        antwoord=True,
        uitleg=r"Dat is de regel voor de logaritme van een macht, ook voor \(\ln\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\log_{4} 2 = 2\).",
        antwoord=False,
        uitleg=r"\(4^{2} = 16\), niet \(2\). Wel is \(4^{\frac{1}{2}} = \sqrt{4} = 2\), dus \(\log_{4} 2 = \tfrac{1}{2}\).",
    ),
]
