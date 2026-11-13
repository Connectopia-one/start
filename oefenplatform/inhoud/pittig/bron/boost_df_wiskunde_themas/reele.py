"""Reële getallen, wortels en machten — pittig (🚀 Boost DF)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import getallenas

AS = "reele-getallenas"
_AS, _ZONES = getallenas(0, 2, 0.25, [("A", 0.6), ("B", 7 / 6), ("C", math.sqrt(2)), ("D", math.sqrt(3)), ("E", 1.9)], ijk=[0, 0.5, 1, 1.5, 2])

GRAFIEKEN = [dict(naam=AS, titel="Vijf punten op de getallenas", eigen=lambda: _AS)]
PRENTEN = [dict(bestand=f"{AS}.svg", zelf=True, wat="getallenas met vijf punten", vragen="klikvragen over wortels en breuken")]

VRAGEN = [
    klik(
        r"Klik op het punt dat \(\sqrt{3}\) voorstelt.",
        f"{AS}.svg",
        [_ZONES["D"]],
        r"\(\sqrt{3} \approx 1{,}73\): net voorbij \(1{,}5\) en nog voor \(2\). \(\sqrt{2} \approx 1{,}41\) ligt links ervan.",
    ),
    klik(
        r"Klik op het punt dat de breuk \(\tfrac{7}{6}\) voorstelt.",
        f"{AS}.svg",
        [_ZONES["B"]],
        r"\(\tfrac{7}{6} = 1{,}1666\ldots\): iets voorbij \(1\), nog voor \(1{,}25\).",
    ),
    met_prent(f"{AS}.svg", tabel(
        "Rationaal of irrationaal? Het getal bij elk punt:",
        [
            ("punt A", "rationaal"),
            ("punt B", "rationaal"),
            ("punt C", "irrationaal"),
            ("punt D", "irrationaal"),
        ],
        r"A is \(0{,}6 = \tfrac{3}{5}\) en B is \(\tfrac{7}{6}\): breuken, dus rationaal. C en D zijn \(\sqrt{2}\) en \(\sqrt{3}\): geen breuk geeft ze exact.",
        kolommen=["rationaal", "irrationaal"],
    )),
    sorteer(
        "In welke kleinste verzameling zit elk getal?",
        [r"\(\mathbb{N}\)", r"\(\mathbb{Z}\)", r"\(\mathbb{Q}\)", r"\(\mathbb{R}\)"],
        [
            [r"\(\sqrt{49}\)", r"\(\mathbb{N}\)"],
            [r"\(-\sqrt{16}\)", r"\(\mathbb{Z}\)"],
            [r"\(0{,}\overline{3}\)", r"\(\mathbb{Q}\)"],
            [r"\(\sqrt{8}\)", r"\(\mathbb{R}\)"],
            [r"\(\tfrac{12}{4}\)", r"\(\mathbb{N}\)"],
            [r"\(-2{,}5\)", r"\(\mathbb{Q}\)"],
        ],
        r"\(\sqrt{49} = 7\) en \(\tfrac{12}{4} = 3\) zijn natuurlijk. \(-\sqrt{16} = -4\) is geheel. \(0{,}333\ldots = \tfrac{1}{3}\) en \(-2{,}5 = -\tfrac{5}{2}\) zijn rationaal. \(\sqrt{8} = 2\sqrt{2}\) is irrationaal.",
    ),
    mk(
        r"Hoeveel is \(\sqrt{12} + \sqrt{27}\)?",
        [r"\(\sqrt{39}\)", r"\(5\sqrt{3}\)", r"\(6\sqrt{3}\)", r"\(13\sqrt{3}\)"],
        1,
        r"\(\sqrt{12} = 2\sqrt{3}\) en \(\sqrt{27} = 3\sqrt{3}\), samen \(5\sqrt{3}\). Een wortel splitst niet over een som: \(\sqrt{39}\) is fout.",
    ),
    mk(
        r"Hoeveel is \(\left(2\sqrt{5}\right)^{2}\)?",
        [r"\(10\)", r"\(20\)", r"\(4\sqrt{5}\)", r"\(100\)"],
        1,
        r"Beide factoren kwadrateren: \(2^{2} \cdot \left(\sqrt{5}\right)^{2} = 4 \cdot 5 = 20\).",
    ),
    inv(
        r"Maak de noemer wortelvrij en vereenvoudig: \(\dfrac{6}{\sqrt{3}}\). Typ bijvoorbeeld 2√5.",
        ["2√3", "2 √3", "2 wortel 3", "2wortel3"],
        r"Teller en noemer maal \(\sqrt{3}\): \(\dfrac{6\sqrt{3}}{3} = 2\sqrt{3}\).",
    ),
    koppel(
        "Koppel elke uitdrukking aan haar waarde.",
        [
            [r"\(2^{-2}\)", r"\(\tfrac{1}{4}\)"],
            [r"\(\left(-2\right)^{3}\)", r"\(-8\)"],
            [r"\(-2^{2}\)", r"\(-4\)"],
            [r"\(\left(\tfrac{1}{2}\right)^{-3}\)", r"\(8\)"],
        ],
        [r"\(4\)", r"\(-\tfrac{1}{4}\)"],
        r"Bij \(-2^{2}\) hoort het minteken niet bij het grondtal: \(-(2 \cdot 2) = -4\). Een negatieve exponent keert de breuk om: \(\left(\tfrac{1}{2}\right)^{-3} = 2^{3} = 8\).",
    ),
    mk(
        r"Vereenvoudig \(\dfrac{a^{5} \cdot a^{-2}}{a^{4}}\) (met \(a \neq 0\)).",
        [r"\(a^{-1}\)", r"\(a^{\frac{5}{2}}\)", r"\(a^{11}\)", r"\(a^{7}\)"],
        0,
        r"Teller: \(a^{5 + (-2)} = a^{3}\). Delen: \(a^{3 - 4} = a^{-1} = \tfrac{1}{a}\).",
    ),
    mk(
        r"Hoeveel is \(\left(3a^{2}b\right)^{3}\)?",
        [r"\(9a^{6}b^{3}\)", r"\(27a^{5}b^{3}\)", r"\(27a^{6}b^{3}\)", r"\(3a^{6}b^{3}\)"],
        2,
        r"Elke factor tot de derde: \(3^{3} = 27\), \(\left(a^{2}\right)^{3} = a^{6}\) en \(b^{3}\).",
    ),
    tabel(
        "Klopt deze rekenregel voor positieve getallen a en b?",
        [
            (r"\(\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}\)", J),
            (r"\(\sqrt{a} + \sqrt{b} = \sqrt{a + b}\)", F),
            (r"\(\dfrac{\sqrt{a}}{\sqrt{b}} = \sqrt{\dfrac{a}{b}}\)", J),
            (r"\(a^{2} \cdot a^{3} = a^{6}\)", F),
            (r"\(\left(a \cdot b\right)^{2} = a^{2} \cdot b^{2}\)", J),
        ],
        r"Een wortel en een macht verdelen over een product en een quotiënt, niet over een som. Bij vermenigvuldigen met hetzelfde grondtal tel je de exponenten op: \(a^{5}\).",
    ),
    inv(
        r"Hoeveel is \(\sqrt[3]{-64} + \sqrt{64}\)?",
        ["4"],
        r"\(\sqrt[3]{-64} = -4\), want \((-4)^{3} = -64\). \(\sqrt{64} = 8\). Samen \(4\).",
    ),
    mk(
        r"Welke uitspraak over \(\sqrt{-9}\) klopt?",
        [
            r"het is \(-3\)",
            r"het bestaat niet in \(\mathbb{R}\)",
            r"het is \(3\) of \(-3\)",
            r"het is een irrationaal getal",
        ],
        1,
        r"Geen enkel reëel getal geeft in het kwadraat \(-9\). Een derdemachtswortel van een negatief getal bestaat wel: \(\sqrt[3]{-27} = -3\).",
    ),
    keuze(
        r"Een getal met decimale vorm \(0{,}121212\ldots\) is [[*rationaal|irrationaal]], want de decimalen zijn [[*repeterend|niet-repeterend|begrensd]]. Een getal als \(0{,}1010010001\ldots\) is [[*irrationaal|rationaal]].",
        r"\(0{,}\overline{12} = \tfrac{12}{99} = \tfrac{4}{33}\). In \(0{,}1010010001\ldots\) komt er telkens een nul meer bij: er herhaalt zich geen vast blok.",
    ),
    inv(
        r"Schrijf \(0{,}\overline{6}\) als vereenvoudigde breuk. Typ bijvoorbeeld 3/7.",
        ["2/3"],
        r"\(0{,}666\ldots = \tfrac{6}{9} = \tfrac{2}{3}\).",
    ),
    volgorde(
        "Zet van klein naar groot.",
        [r"\(-\sqrt{5}\)", r"\(-2\)", r"\(\tfrac{3}{2}\)", r"\(\sqrt{3}\)", r"\(\sqrt[3]{27}\)"],
        r"\(-\sqrt{5} \approx -2{,}24\) ligt links van \(-2\). \(\tfrac{3}{2} = 1{,}5\), \(\sqrt{3} \approx 1{,}73\), \(\sqrt[3]{27} = 3\).",
    ),
    mk(
        r"Een vierkant heeft een oppervlakte van \(50\) cm². Hoe lang is een zijde, exact?",
        [r"\(25\) cm", r"\(5\sqrt{2}\) cm", r"\(2\sqrt{5}\) cm", r"\(12{,}5\) cm"],
        1,
        r"De zijde is \(\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2} \approx 7{,}07\) cm.",
    ),
    sleep(
        r"Bij \(3 \cdot (20 + 7) = 3 \cdot 20 + 3 \cdot 7\) gebruik je de [[distributiviteit]]. Bij \(4 \cdot 9 \cdot 25 = 4 \cdot 25 \cdot 9\) gebruik je de [[commutativiteit]]. Bij \((17 + 8) + 2 = 17 + (8 + 2)\) gebruik je de [[associativiteit]].",
        ["absorptie"],
        "Distributief: vermenigvuldigen over een som. Commutatief: de volgorde wisselen. Associatief: anders groeperen.",
    ),
    mk(
        r"Met welke eigenschap reken je \(98 \cdot 15\) het vlugst uit het hoofd?",
        [
            r"\(98 \cdot 15 = 15 \cdot 98\), de commutativiteit",
            r"\(98 \cdot 15 = 100 \cdot 15 - 2 \cdot 15\), de distributiviteit",
            r"\(98 \cdot 15 = 98 \cdot 10 \cdot 5\), de associativiteit",
            r"\(98 \cdot 15 = (98 + 15) \cdot 2\), de distributiviteit",
        ],
        1,
        r"\(1500 - 30 = 1470\). De laatste optie klopt niet: \((98 + 15) \cdot 2 = 226\). En \(10 \cdot 5 = 50\), niet \(15\).",
    ),
    inv(
        r"Hoeveel is \(\left(\sqrt{7} - 1\right)\left(\sqrt{7} + 1\right)\)?",
        ["6"],
        r"Distributief uitwerken: \(7 + \sqrt{7} - \sqrt{7} - 1 = 6\).",
    ),
    tabel(
        "Juist of fout over de verzamelingen van getallen?",
        [
            (r"Elk rationaal getal is ook een reëel getal.", J),
            (r"Er zijn gehele getallen die niet natuurlijk zijn.", J),
            (r"De som van twee irrationale getallen is altijd irrationaal.", F),
            (r"Het product van een rationaal getal (niet \(0\)) en een irrationaal getal is irrationaal.", J),
        ],
        r"\(\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}\). Tegenvoorbeeld voor de som: \(\sqrt{2} + \left(-\sqrt{2}\right) = 0\).",
    ),
    mk(
        r"Hoeveel procent is \(\tfrac{7}{8}\)?",
        [r"\(78\%\)", r"\(87{,}5\%\)", r"\(0{,}875\%\)", r"\(8{,}75\%\)"],
        1,
        r"\(7 : 8 = 0{,}875\), en dat is \(87{,}5\) honderdsten.",
    ),
    casus(
        r"Een vierkant tegeltje heeft een zijde van \(\sqrt{8}\) dm.",
        [
            inv(
                "Hoe groot is de oppervlakte van het tegeltje, in dm²?",
                ["8", "8 dm²"],
                r"\(\left(\sqrt{8}\right)^{2} = 8\).",
            ),
            mk(
                "Hoe lang is de diagonaal van het tegeltje?",
                [r"\(4\) dm", r"\(\sqrt{16}\cdot\sqrt{2}\) dm", r"\(8\) dm", r"\(2\sqrt{8}\) dm"],
                0,
                r"De diagonaal van een vierkant met zijde \(z\) is \(z\sqrt{2}\): \(\sqrt{8} \cdot \sqrt{2} = \sqrt{16} = 4\) dm.",
            ),
        ],
    ),
    mk(
        r"Hoeveel is \(\left(\tfrac{2}{3}\right)^{-2}\)?",
        [r"\(-\tfrac{4}{9}\)", r"\(\tfrac{9}{4}\)", r"\(\tfrac{4}{9}\)", r"\(-\tfrac{9}{4}\)"],
        1,
        r"Een negatieve exponent keert de breuk om: \(\left(\tfrac{3}{2}\right)^{2} = \tfrac{9}{4}\). Het resultaat wordt niet negatief.",
    ),
    open_(
        r"Een leerling schrijft: \(\sqrt{16 + 9} = 4 + 3 = 7\). Toon met een berekening aan dat dit fout is en leg uit welke regel ze verkeerd gebruikt.",
        r"\(\sqrt{16 + 9} = \sqrt{25} = 5\) en niet \(7\). Ze splitste de wortel over een som, en dat mag niet: \(\sqrt{a + b}\) is niet gelijk aan \(\sqrt{a} + \sqrt{b}\). Over een product mag het wel.",
    ),
    mk(
        r"Welk getal ligt tussen \(\sqrt{10}\) en \(\sqrt{11}\)?",
        [r"\(3{,}2\)", r"\(3{,}4\)", r"\(3{,}1\)", r"\(10{,}5\)"],
        0,
        r"\(3{,}2^{2} = 10{,}24\) ligt tussen \(10\) en \(11\). \(3{,}1^{2} = 9{,}61\) is te klein, \(3{,}4^{2} = 11{,}56\) te groot.",
    ),
    inv(
        r"Vereenvoudig \(\sqrt{75}\). Typ bijvoorbeeld 2√5.",
        ["5√3", "5 √3", "5 wortel 3", "5wortel3"],
        r"\(75 = 25 \cdot 3\), dus \(\sqrt{75} = \sqrt{25} \cdot \sqrt{3} = 5\sqrt{3}\).",
    ),
    keuze(
        r"\(\left(-3\right)^{4}\) is [[*positief|negatief]], \(-3^{4}\) is [[*negatief|positief]] en \(\left(-3\right)^{5}\) is [[*negatief|positief]].",
        r"Een negatief grondtal met een even exponent geeft een positief resultaat, met een oneven exponent een negatief. Bij \(-3^{4}\) staat het minteken buiten de macht: \(-81\).",
    ),
    mk(
        r"Welke uitdrukking is gelijk aan \(2^{3} \cdot 4^{2}\)?",
        [r"\(8^{5}\)", r"\(2^{7}\)", r"\(6^{5}\)", r"\(2^{6}\)"],
        1,
        r"Schrijf alles met grondtal \(2\): \(4^{2} = \left(2^{2}\right)^{2} = 2^{4}\), en \(2^{3} \cdot 2^{4} = 2^{7} = 128\).",
    ),
]
