"""Machtswortels, machten en logaritmen — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

PRENTEN = []

VRAGEN = [
    mk(
        r"Hoeveel is \(\left(\sqrt[3]{8}\right)^{2} + 16^{\frac{3}{4}}\)?",
        [r"\(12\)", r"\(10\)", r"\(16\)", r"\(20\)"],
        0,
        r"\(\sqrt[3]{8} = 2\), dus \(2^{2} = 4\). \(16^{\frac{3}{4}} = \left(\sqrt[4]{16}\right)^{3} = 2^{3} = 8\). Samen \(4 + 8 = 12\).",
    ),
    mk(
        r"Welke uitdrukking is gelijk aan \(\sqrt[5]{a^{3}}\) (met \(a > 0\))?",
        [r"\(a^{\frac{3}{5}}\)", r"\(a^{\frac{5}{3}}\)", r"\(a^{15}\)", r"\(a^{-2}\)"],
        0,
        r"De exponent onder de wortel komt in de teller, de wortelexponent in de noemer: \(\sqrt[n]{a^{m}} = a^{\frac{m}{n}}\).",
    ),
    tabel(
        r"Bestaat de uitdrukking in \(\mathbb{R}\)?",
        [
            (r"\(\sqrt[3]{-27}\)", J),
            (r"\(\sqrt[6]{-64}\)", F),
            (r"\((-8)^{\frac{1}{3}}\) als derdemachtswortel gelezen", J),
            (r"\(\log_{2} 0\)", F),
            (r"\(\log 0{,}001\)", J),
            (r"\(\ln(-1)\)", F),
        ],
        "Een even machtswortel van een negatief getal bestaat niet. Een logaritme bestaat enkel van een strikt positief getal, ook als het kleiner is dan 1.",
        kolommen=["Bestaat", "Bestaat niet"],
    ),
    inv(
        r"Schrijf \(\dfrac{\sqrt{x} \cdot \sqrt[3]{x}}{x}\) als één macht van \(x\) (met \(x > 0\)). Geef enkel de exponent als breuk, bijvoorbeeld 2/7.",
        ["-1/6", "−1/6", "-1 / 6"],
        r"\(x^{\frac{1}{2}} \cdot x^{\frac{1}{3}} = x^{\frac{5}{6}}\). Delen door \(x^{1}\) geeft \(x^{\frac{5}{6} - 1} = x^{-\frac{1}{6}}\).",
    ),
    mk(
        r"Een leerling schrijft: \(\sqrt{9 + 16} = \sqrt{9} + \sqrt{16} = 7\). Wat klopt?",
        [
            r"Fout: \(\sqrt{25} = 5\). Een wortel van een som is niet de som van de wortels.",
            r"Juist: wortels mag je altijd over een som verdelen.",
            r"Fout: het antwoord moet \(\pm 7\) zijn.",
            r"Juist, maar enkel omdat \(9\) en \(16\) kwadraten zijn.",
        ],
        0,
        r"Over een product mag je een wortel verdelen (\(\sqrt{ab} = \sqrt{a}\sqrt{b}\)), over een som niet.",
    ),
    koppel(
        "Koppel elke uitdrukking aan haar waarde.",
        [
            [r"\(27^{\frac{2}{3}}\)", r"\(9\)"],
            [r"\(32^{-\frac{1}{5}}\)", r"\(\frac{1}{2}\)"],
            [r"\(\log_{3} 81\)", r"\(4\)"],
            [r"\(\log_{2} \frac{1}{8}\)", r"\(-3\)"],
        ],
        [r"\(-\frac{1}{2}\)"],
        r"\(\sqrt[3]{27} = 3\) en \(3^{2} = 9\). \(\sqrt[5]{32} = 2\), negatieve exponent: \(\frac{1}{2}\). \(3^{4} = 81\). \(2^{-3} = \frac{1}{8}\).",
    ),
    mk(
        r"Als \(\log_{a} b = 3\), hoeveel is dan \(\log_{a} b^{2} - \log_{a} \sqrt{b}\)?",
        [r"\(4{,}5\)", r"\(7{,}5\)", r"\(1{,}5\)", r"\(6\)"],
        0,
        r"\(\log_{a} b^{2} = 2 \cdot 3 = 6\) en \(\log_{a} \sqrt{b} = \frac{1}{2} \cdot 3 = 1{,}5\). Verschil: \(4{,}5\).",
    ),
    tabel(
        r"Juist of fout (met \(a, x, y > 0\) en \(a \neq 1\))?",
        [
            (r"\(\log_{a}(xy) = \log_{a} x + \log_{a} y\)", J),
            (r"\(\log_{a}(x + y) = \log_{a} x \cdot \log_{a} y\)", F),
            (r"\(\log_{a} x^{5} = 5 \log_{a} x\)", J),
            (r"\(\dfrac{\log_{a} x}{\log_{a} y} = \log_{a} x - \log_{a} y\)", F),
        ],
        "De rekenregels gaan over het product, het quotiënt en de macht binnen de logaritme. Een som binnen of een quotiënt van twee logaritmen heeft geen eigen regel.",
    ),
    inv(
        r"Bereken zonder rekenmachine: \(\log_{6} 4 + \log_{6} 9\).",
        "2",
        r"\(\log_{6} 4 + \log_{6} 9 = \log_{6} 36 = 2\), want \(6^{2} = 36\).",
    ),
    mk(
        r"Welke uitdrukking geeft \(\log_{3} 20\) met de toetsen \(\log\) of \(\ln\) van een rekenmachine?",
        [r"\(\dfrac{\log 20}{\log 3}\)", r"\(\dfrac{\log 3}{\log 20}\)", r"\(\log 20 - \log 3\)", r"\(\log \dfrac{20}{3}\)"],
        0,
        r"Veranderen van grondtal: \(\log_{a} x = \dfrac{\log x}{\log a}\). Met \(\ln\) werkt het op dezelfde manier.",
    ),
    mk(
        r"Tussen welke twee gehele getallen ligt \(\log_{2} 50\)?",
        [r"\(5\) en \(6\)", r"\(4\) en \(5\)", r"\(6\) en \(7\)", r"\(24\) en \(26\)"],
        0,
        r"\(2^{5} = 32\) en \(2^{6} = 64\). Omdat \(32 < 50 < 64\), ligt \(\log_{2} 50\) tussen \(5\) en \(6\).",
    ),
    keuze(
        "De logaritme met grondtal 10 schrijf je [[*log|ln|lg2]], de natuurlijke logaritme schrijf je [[*ln|log|nl]] en heeft als grondtal het getal [[*e|10|2]].",
        "log zonder grondtal betekent grondtal 10, ln betekent grondtal e (ongeveer 2,718).",
    ),
    volgorde(
        r"Zet van klein naar groot.",
        [r"\(\log_{2} \frac{1}{4}\)", r"\(\log 0{,}5\)", r"\(\ln 1\)", r"\(8^{\frac{1}{3}}\)", r"\(\log_{3} 27\)"],
        r"\(\log_{2} \frac{1}{4} = -2\), \(\log 0{,}5 \approx -0{,}30\), \(\ln 1 = 0\), \(8^{\frac{1}{3}} = 2\), \(\log_{3} 27 = 3\).",
    ),
    inv(
        r"Los op: \(\log_{x} 125 = 3\). Geef \(x\).",
        "5",
        r"\(\log_{x} 125 = 3\) betekent \(x^{3} = 125\), dus \(x = 5\).",
    ),
    mk(
        r"Los op: \(\log_{2}(x - 1) = 4\).",
        [r"\(x = 17\)", r"\(x = 9\)", r"\(x = 15\)", r"\(x = 5\)"],
        0,
        r"\(x - 1 = 2^{4} = 16\), dus \(x = 17\).",
    ),
    tabel(
        r"Vereenvoudig (met \(x > 0\)). Welk resultaat hoort bij welke uitdrukking?",
        [
            (r"\(x^{\frac{1}{2}} \cdot x^{\frac{1}{2}}\)", r"\(x\)"),
            (r"\(\left(x^{\frac{2}{3}}\right)^{3}\)", r"\(x^{2}\)"),
            (r"\(\dfrac{x^{\frac{1}{4}}}{x^{\frac{1}{4}}}\)", r"\(1\)"),
            (r"\(\sqrt{x^{6}}\)", r"\(x^{3}\)"),
        ],
        "Bij een product tel je exponenten op, bij een macht van een macht vermenigvuldig je ze, bij een quotiënt trek je ze af.",
        kolommen=[r"\(1\)", r"\(x\)", r"\(x^{2}\)", r"\(x^{3}\)"],
    ),
    sorteer(
        "Is het resultaat positief of negatief?",
        ["Positief", "Negatief"],
        [
            [r"\(\log 0{,}2\)", "Negatief"],
            [r"\(\log_{5} 7\)", "Positief"],
            [r"\(\ln 0{,}9\)", "Negatief"],
            [r"\(4^{-\frac{1}{2}}\)", "Positief"],
            [r"\(\sqrt[3]{-0{,}5}\)", "Negatief"],
            [r"\(\log_{2} 1{,}5\)", "Positief"],
        ],
        "Een logaritme met grondtal groter dan 1 is negatief voor getallen tussen 0 en 1. Een macht met positief grondtal is altijd positief, ook met een negatieve exponent.",
    ),
    mk(
        r"Een leerling zegt: \(2^{-3}\) is negatief, want de exponent is negatief. Wat klopt?",
        [
            r"Fout: \(2^{-3} = \frac{1}{8}\), en dat is positief.",
            r"Juist: \(2^{-3} = -8\).",
            r"Juist: \(2^{-3} = -6\).",
            r"Fout: \(2^{-3} = 8\).",
        ],
        0,
        "Een negatieve exponent betekent het omgekeerde nemen, niet het teken veranderen.",
    ),
    inv(
        r"Schrijf \(\sqrt[3]{x^{2}} \cdot \sqrt[6]{x^{2}}\) als één macht van \(x\) (met \(x > 0\)). Geef enkel de exponent.",
        "1",
        r"\(x^{\frac{2}{3}} \cdot x^{\frac{1}{3}} = x^{1}\). Het resultaat is gewoon \(x\).",
    ),
    mk(
        r"Welk getal is gelijk aan \(e^{\ln 7}\)?",
        [r"\(7\)", r"\(\ln 7\)", r"\(e^{7}\)", r"\(1\)"],
        0,
        r"Macht en logaritme met hetzelfde grondtal heffen elkaar op: \(a^{\log_{a} x} = x\).",
    ),
    mk(
        r"Als \(\log 2 \approx 0{,}301\), hoeveel is dan ongeveer \(\log 8000\)?",
        [r"\(3{,}903\)", r"\(2{,}408\)", r"\(0{,}903\)", r"\(24{,}08\)"],
        0,
        r"\(8000 = 2^{3} \cdot 1000\). Dus \(\log 8000 = 3 \log 2 + \log 1000 \approx 0{,}903 + 3 = 3{,}903\).",
    ),
    tabel(
        "Juist of fout?",
        [
            (r"\(\log_{a} 1 = 0\) voor elk toegelaten grondtal \(a\)", J),
            (r"\(\log_{a} a = a\)", F),
            (r"\(\log_{\frac{1}{2}} 4 = -2\)", J),
            (r"\(\sqrt[n]{a} = a^{n}\)", F),
        ],
        r"\(a^{0} = 1\) en \(a^{1} = a\), dus \(\log_{a} a = 1\). \(\left(\frac{1}{2}\right)^{-2} = 4\). Een \(n\)-de machtswortel is de macht met exponent \(\frac{1}{n}\).",
    ),
    sleep(
        "Het verband tussen macht en logaritme: als a tot de macht y gelijk is aan x, dan is y de [[logaritme]] van x met [[grondtal]] a. De bewerking die bij een macht het grondtal zoekt, is [[worteltrekking]].",
        ["exponent", "breuk"],
        "Bij een macht zoek je de uitkomst, bij een logaritme de exponent, bij een wortel het grondtal.",
    ),
    mk(
        r"Welke uitdrukking is gelijk aan \(2\log_{a} x - 3\log_{a} y\) (met \(x, y > 0\))?",
        [r"\(\log_{a} \dfrac{x^{2}}{y^{3}}\)", r"\(\log_{a} (x^{2} - y^{3})\)", r"\(\dfrac{\log_{a} x^{2}}{\log_{a} y^{3}}\)", r"\(\log_{a} \dfrac{2x}{3y}\)"],
        0,
        r"Eerst de getallen als exponent binnen brengen, dan wordt het verschil een quotiënt.",
    ),
    inv(
        r"Hoeveel is \(\log_{4} 8\)? Schrijf als kommagetal.",
        ["1,5", "1.5", "3/2"],
        r"\(4^{1{,}5} = \left(\sqrt{4}\right)^{3} = 2^{3} = 8\). Of: \(\log_{4} 8 = \frac{\log_{2} 8}{\log_{2} 4} = \frac{3}{2}\).",
    ),
    mk(
        r"Welke \(x\) voldoet aan \(x^{\frac{3}{2}} = 27\)?",
        [r"\(9\)", r"\(18\)", r"\(3\)", r"\(\sqrt{27}\)"],
        0,
        r"Verhef beide leden tot de macht \(\frac{2}{3}\): \(x = 27^{\frac{2}{3}} = 3^{2} = 9\). Controle: \(9^{\frac{3}{2}} = 3^{3} = 27\).",
    ),
    open_(
        r"Leg uit waarom \(\log_{2} 10\) geen geheel getal is, en schat de waarde tot op één cijfer na de komma zonder rekenmachine.",
        r"\(2^{3} = 8\) en \(2^{4} = 16\), en \(10\) ligt daartussen, dus de logaritme ligt tussen \(3\) en \(4\). \(10\) ligt dichter bij \(8\) dan bij \(16\), dus ongeveer \(3{,}3\) (exact \(3{,}32\ldots\)).",
        "Zoek de twee machten van 2 waartussen 10 ligt.",
    ),
    casus(
        r"Een geluid van \(L\) decibel heeft een intensiteit die je vindt met \(L = 10 \cdot \log \dfrac{I}{I_{0}}\). Daarbij is \(I_{0}\) de zwakste intensiteit die je nog hoort.",
        [
            mk(
                r"Een geluid is \(1000\) keer zo intens als \(I_{0}\). Hoeveel decibel is dat?",
                [r"\(30\)", r"\(3\)", r"\(1000\)", r"\(10\,000\)"],
                0,
                r"\(10 \cdot \log 1000 = 10 \cdot 3 = 30\) decibel.",
            ),
            mk(
                "Een geluid wordt 100 keer zo intens. Met hoeveel decibel stijgt het?",
                [r"\(20\)", r"\(100\)", r"\(2\)", r"\(1000\)"],
                0,
                r"\(10 \cdot \log(100 \cdot x) = 10 \cdot (2 + \log x)\): er komt \(20\) decibel bij.",
            ),
            mk(
                "Een fluistergesprek is 20 decibel. Hoeveel keer zo intens als het zwakste hoorbare geluid is dat?",
                [r"\(100\)", r"\(20\)", r"\(200\)", r"\(2\)"],
                0,
                r"\(10 \cdot \log x = 20\), dus \(\log x = 2\) en \(x = 10^{2} = 100\).",
            ),
        ],
    ),
]
