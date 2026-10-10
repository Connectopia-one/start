# -*- coding: utf-8 -*-
r"""De vragen voor "Reële getallen, wortels en machten".

Uit de bouwsteen Getallenleer van de vakfiche: de invoering van de reële
getallen als vervollediging van de getallenas, natuurlijke, gehele, rationale
en irrationale getallen, de drie decimale voorstellingswijzen, de verbanden
tussen decimale vorm, wortelvorm, breuk en procent, derdemachtsworteltrekking,
de eigenschappen associativiteit, commutativiteit en distributiviteit, en het
rekenen met vierkantswortels en met machten met gehele exponenten, ook in
lettervormen.

In echte notatie geschreven, zoals de rest van wiskunde gevorderd: \(\sqrt{50}\)
in plaats van "de wortel van 50", en \(2^{-3}\) in plaats van "2 tot de macht
min 3". Zie oefenplatform/lib/wiskunde.ts. Het antwoord van een invulvraag
blijft gewone tekst, want dat typt een leerling in een invulvakje.

Deel 1 zijn de getalverzamelingen en de vormen. Deel 2 is het rekenwerk met
wortels en machten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Waarom volstaan de rationale getallen \(\mathbb{Q}\) niet om de getallenas te vullen?",
        opties=[
            r"omdat er lengtes bestaan die geen breuk zijn, zoals \(\sqrt{2}\)",
            "omdat er tussen twee breuken altijd nog een breuk ligt en het nooit stopt",
            "omdat een breuk altijd een begrensde decimale vorm heeft",
            "omdat de negatieve getallen geen plaats hebben bij de breuken",
        ],
        antwoord=0,
        uitleg=r"De schuine zijde van een rechthoekige driehoek met rechthoekszijden \(1\) meet precies \(\sqrt{2}\), en dat is geen breuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze getallen is irrationaal?",
        opties=[r"\(\sqrt{2}\)", r"\(\tfrac{7}{3}\)", r"\(0{,}125\)", r"\(-4\)"],
        antwoord=0,
        uitleg=r"\(\tfrac{7}{3}\) is een breuk, \(0{,}125 = \tfrac{1}{8}\) en \(-4\) is geheel. Alleen \(\sqrt{2}\) laat zich niet als breuk schrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Tot welke verzameling behoort \(-7\) wel, maar niet tot de kleinere ervoor?",
        opties=[
            r"\(\mathbb{Z}\), want \(-7\) is geen natuurlijk getal",
            r"\(\mathbb{N}\), want \(-7\) is een geheel aantal",
            r"de irrationale getallen, want \(-7\) is niet positief",
            r"\(\mathbb{R}\), want \(-7\) is niet als breuk te schrijven",
        ],
        antwoord=0,
        uitleg=r"\(\mathbb{N}\) begint bij \(0\) en gaat omhoog. \(\mathbb{Z}\) neemt de negatieve getallen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de decimale vorm van een rationaal getal altijd?",
        opties=[
            "begrensd of onbegrensd repeterend",
            "altijd begrensd, met hoogstens drie cijfers na de komma",
            "altijd onbegrensd en nooit repeterend",
            "afhankelijk van of de teller groter is dan de noemer",
        ],
        antwoord=0,
        uitleg=r"\(\tfrac{1}{4} = 0{,}25\) stopt. \(\tfrac{1}{3} = 0{,}333\ldots\) herhaalt. Een irrationaal getal doet geen van beide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke decimale vorm hoort bij een irrationaal getal?",
        opties=[
            "onbegrensd en niet-repeterend",
            r"onbegrensd en repeterend, zoals \(0{,}272727\ldots\)",
            "begrensd, met heel veel cijfers na de komma",
            "begrensd, maar alleen in een ander talstelsel",
        ],
        antwoord=0,
        uitleg=r"De cijfers van \(\pi\) stoppen niet en herhalen zich ook nooit in een vast patroon.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke breuk hoort bij \(0{,}75\)?",
        opties=[r"\(\tfrac{3}{4}\)", r"\(\tfrac{7}{5}\)", r"\(\tfrac{3}{5}\)", r"\(\tfrac{5}{7}\)"],
        antwoord=0,
        uitleg=r"\(0{,}75 = \tfrac{75}{100} = \tfrac{3}{4}\), en in procent is dat \(75 \%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel procent is \(\tfrac{2}{5}\)?",
        opties=[r"\(40 \%\)", r"\(25 \%\)", r"\(52 \%\)", r"\(20 \%\)"],
        antwoord=0,
        uitleg=r"\(2 : 5 = 0{,}4\), en dat is \(40 \%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sqrt[3]{27}\)?",
        opties=[r"\(3\)", r"\(9\)", r"\(\tfrac{27}{3}\)", r"ongeveer \(5{,}2\)"],
        antwoord=0,
        uitleg=r"\(3 \cdot 3 \cdot 3 = 27\). Bij \(\sqrt{27}\) zou het antwoord ongeveer \(5{,}2\) zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sqrt[3]{125}\)?",
        opties=[r"\(5\)", r"\(25\)", r"\(15\)", r"ongeveer \(11{,}2\)"],
        antwoord=0,
        uitleg=r"\(5^{3} = 125\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke eigenschap gebruik je als je \(3 \cdot (20 + 7)\) schrijft als \(3 \cdot 20 + 3 \cdot 7\)?",
        opties=[
            "de distributiviteit",
            "de associativiteit",
            "de commutativiteit",
            "de omgekeerde bewerking",
        ],
        antwoord=0,
        uitleg="Distributiviteit verdeelt de vermenigvuldiging over de optelling. Dat is precies hoe je handig hoofdrekent.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke eigenschap gebruik je als je \((2 + 8) + 5\) verandert in \(2 + (8 + 5)\)?",
        opties=[
            "de associativiteit",
            "de distributiviteit",
            "de commutativiteit",
            "de eigenschap van het neutraal element",
        ],
        antwoord=0,
        uitleg="Associativiteit verplaatst de haakjes. Commutativiteit zou de volgorde van de termen omdraaien.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke uitkomst ligt buiten \(\mathbb{Q}\) en dus alleen in \(\mathbb{R}\)?",
        opties=[
            r"de schuine zijde van een rechthoekige driehoek met zijden \(1\) en \(1\)",
            r"de oppervlakte van een rechthoek van \(3\) op \(4\) centimeter",
            "de helft van een oneven geheel getal",
            "het verschil van twee natuurlijke getallen",
        ],
        antwoord=0,
        uitleg=r"Die lengte is \(\sqrt{2}\) en dat is irrationaal. De andere drie blijven binnen \(\mathbb{Q}\) of \(\mathbb{Z}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke uitspraak over \(\pi\) klopt?",
        opties=[
            "het is irrationaal, dus geen enkele breuk geeft het exact weer",
            r"het is gelijk aan \(\tfrac{22}{7}\), maar dan afgerond",
            "het is rationaal, want je kan het tot op elk cijfer berekenen",
            "het is een geheel getal zodra je het afrondt op nul cijfers",
        ],
        antwoord=0,
        uitleg=r"\(\tfrac{22}{7}\) is een benadering, geen gelijkheid. Afronden verandert bovendien niets aan wat een getal is.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elk getal uit \(\mathbb{N}\) zit ook in \(\mathbb{Z}\).",
        antwoord=True,
        uitleg=r"De verzamelingen zitten in elkaar: \(\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Elk getal uit \(\mathbb{R}\) kan je als breuk van twee gehele getallen schrijven.",
        antwoord=False,
        uitleg=r"Dat geldt alleen voor \(\mathbb{Q}\). \(\sqrt{2}\) en \(\pi\) lukken niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het getal \(0{,}125\) is rationaal.",
        antwoord=True,
        uitleg=r"Het is \(\tfrac{1}{8}\), en de decimale vorm stopt netjes.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt{9}\) is een irrationaal getal.",
        antwoord=False,
        uitleg=r"\(\sqrt{9} = 3\), dus zelfs een natuurlijk getal. Alleen wortels die niet opgaan zijn irrationaal.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\sqrt[3]{64}\)?",
        antwoord=["4"],
        uitleg=r"\(4 \cdot 4 \cdot 4 = 64\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Schrijf \(0{,}4\) als een vereenvoudigde breuk. Typ bijvoorbeeld 3/5.",
        antwoord=["2/5"],
        uitleg=r"\(0{,}4 = \tfrac{4}{10} = \tfrac{2}{5}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel procent is \(\tfrac{3}{8}\)?",
        antwoord=["37,5", "37,5 %", "37,5 procent"],
        uitleg=r"\(3 : 8 = 0{,}375\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Hoe vereenvoudig je \(\sqrt{50}\)?",
        opties=[
            r"\(5\sqrt{2}\)",
            r"\(2\sqrt{5}\)",
            r"\(25\sqrt{2}\)",
            r"\(\sqrt{25} + \sqrt{25}\)",
        ],
        antwoord=0,
        uitleg=r"\(50 = 25 \cdot 2\) en \(\sqrt{25} = 5\). Let op: wortels mag je niet zomaar optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe vereenvoudig je \(\sqrt{72}\)?",
        opties=[
            r"\(6\sqrt{2}\)",
            r"\(8\sqrt{3}\)",
            r"\(2\sqrt{6}\)",
            r"\(3\sqrt{8}\)",
        ],
        antwoord=0,
        uitleg=r"\(72 = 36 \cdot 2\) en \(\sqrt{36} = 6\). De laatste optie klopt wel qua waarde maar is niet vereenvoudigd.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sqrt{3} \cdot \sqrt{12}\)?",
        opties=[r"\(6\)", r"\(\sqrt{15}\)", r"\(36\)", r"\(3\sqrt{4}\)"],
        antwoord=0,
        uitleg=r"Onder één wortelteken brengen mag: \(\sqrt{3 \cdot 12} = \sqrt{36} = 6\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe maak je de noemer van \(\dfrac{1}{\sqrt{5}}\) wortelvrij?",
        opties=[
            r"teller en noemer maal \(\sqrt{5}\), wat \(\dfrac{\sqrt{5}}{5}\) geeft",
            r"teller en noemer maal \(5\), wat \(\dfrac{5}{\sqrt{25}}\) geeft",
            r"de wortel weglaten, want \(\dfrac{1}{\sqrt{5}} \approx \dfrac{1}{2}\)",
            "de breuk omkeren, want dan staat de wortel in de teller",
        ],
        antwoord=0,
        uitleg=r"\(\sqrt{5} \cdot \sqrt{5} = 5\), dus de noemer wordt een gewoon getal. De waarde van de breuk verandert niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(2^{-3}\)?",
        opties=[r"\(\tfrac{1}{8}\)", r"\(-8\)", r"\(-6\)", r"\(\tfrac{1}{6}\)"],
        antwoord=0,
        uitleg=r"Een negatieve exponent keert om: \(2^{-3} = \dfrac{1}{2^{3}} = \dfrac{1}{8}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(5^{0}\)?",
        opties=[r"\(1\)", r"\(0\)", r"\(5\)", "dat is niet bepaald"],
        antwoord=0,
        uitleg=r"Elke macht met exponent \(0\) is \(1\), behalve voor het grondtal \(0\) zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(a^{4} \cdot a^{3}\)?",
        opties=[r"\(a^{7}\)", r"\(a^{12}\)", r"\(2a^{7}\)", r"\(a^{1}\)"],
        antwoord=0,
        uitleg="Bij vermenigvuldigen tel je de exponenten op. Vermenigvuldigen doe je pas bij een macht van een macht.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\left(a^{3}\right)^{2}\)?",
        opties=[r"\(a^{6}\)", r"\(a^{5}\)", r"\(2a^{3}\)", r"\(a^{9}\)"],
        antwoord=0,
        uitleg=r"Bij een macht van een macht vermenigvuldig je de exponenten: \(3 \cdot 2 = 6\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\dfrac{a^{6}}{a^{2}}\)?",
        opties=[r"\(a^{4}\)", r"\(a^{3}\)", r"\(a^{8}\)", r"\(\dfrac{1}{a^{4}}\)"],
        antwoord=0,
        uitleg=r"Bij delen trek je de exponenten af: \(6 - 2 = 4\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sqrt{3} + \sqrt{3}\)?",
        opties=[r"\(2\sqrt{3}\)", r"\(\sqrt{6}\)", r"\(\sqrt{9}\)", r"\(3\sqrt{2}\)"],
        antwoord=0,
        uitleg="Wortels optellen gaat zoals appels optellen: twee keer hetzelfde wortelteken geeft er twee van.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is er mis met \(\sqrt{9 + 16} = \sqrt{9} + \sqrt{16}\)?",
        opties=[
            r"een wortel splitst niet over een som: \(\sqrt{25} = 5\), geen \(7\)",
            r"niets, want \(9\) en \(16\) zijn allebei volkomen kwadraten",
            r"de fout zit in \(16\), want \(\sqrt{16} \neq 4\)",
            "de volgorde klopt niet: eerst worteltrekken, dan optellen",
        ],
        antwoord=0,
        uitleg="Splitsen mag bij een product en bij een quotiënt, niet bij een som of een verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \((2a)^{3}\)?",
        opties=[r"\(8a^{3}\)", r"\(2a^{3}\)", r"\(6a^{3}\)", r"\(8a\)"],
        antwoord=0,
        uitleg=r"De exponent geldt voor alles tussen de haakjes, dus ook voor de \(2\): \(2^{3} = 8\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\sqrt{a^{2}}\) als \(a < 0\)?",
        opties=[
            r"\(-a\), want het resultaat is altijd positief",
            "\\(a\\), want wortel en kwadraat heffen elkaar altijd op",
            r"\(a^{2}\), want de wortel verandert niets",
            "dat kan niet berekend worden",
        ],
        antwoord=0,
        uitleg=r"Een vierkantswortel geeft nooit een negatief getal. Is \(a = -3\), dan is \(\sqrt{a^{2}} = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}\) voor positieve \(a\) en \(b\).",
        antwoord=True,
        uitleg=r"Dat mag: \(\sqrt{4 \cdot 9} = \sqrt{4} \cdot \sqrt{9} = 2 \cdot 3 = 6\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\sqrt{a + b} = \sqrt{a} + \sqrt{b}\).",
        antwoord=False,
        uitleg=r"\(\sqrt{9 + 16} = 5\), terwijl \(3 + 4 = 7\).",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve exponent maakt van een macht een breuk met 1 in de teller.",
        antwoord=True,
        uitleg=r"\(3^{-2} = \dfrac{1}{9}\).",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het vermenigvuldigen van twee machten met hetzelfde grondtal vermenigvuldig je de exponenten.",
        antwoord=False,
        uitleg="Dan tel je ze op. Vermenigvuldigen doe je bij een macht van een macht.",
    ),
    dict(
        type="invultekst",
        vraag=r"Vereenvoudig \(\sqrt{18}\). Typ bijvoorbeeld 2√5 of 2 wortel 5.",
        antwoord=["3√2", "3 wortel 2"],
        uitleg=r"\(18 = 9 \cdot 2\) en \(\sqrt{9} = 3\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(3^{-2}\)? Typ het als breuk, bijvoorbeeld 1/4.",
        antwoord=["1/9"],
        uitleg=r"\(3^{2} = 9\), en de negatieve exponent keert om.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\sqrt{5} \cdot \sqrt{20}\)?",
        antwoord=["10"],
        uitleg=r"\(5 \cdot 20 = 100\) en \(\sqrt{100} = 10\).",
    ),
]
