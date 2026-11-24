"""Reële getallen, wortels en machten — pittig (🚀 Boost doorstroom)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import getallenas

AS = "reele-as-do"
_AS, _ZONES = getallenas(-2, 3, 0.5, [("A", -math.sqrt(3)), ("B", -1 / 3), ("C", 0.75), ("D", math.sqrt(5)), ("E", 2.7)], ijk=[-2, -1, 0, 1, 2, 3])
# E ligt op 2,7: dat is een eindige decimale vorm, dus rationaal.

GRAFIEKEN = [dict(naam=AS, titel="Vijf punten op de getallenas", eigen=lambda: _AS)]
PRENTEN = [dict(bestand=f"{AS}.svg", zelf=True, wat="getallenas van -2 tot 3 met vijf punten", vragen="klikvragen over wortels, breuken en verzamelingen")]

VRAGEN = [
    klik(
        r"Klik op het punt dat \(-\sqrt{3}\) voorstelt.",
        f"{AS}.svg",
        [_ZONES["A"]],
        r"\(\sqrt{3} \approx 1{,}73\), dus \(-\sqrt{3} \approx -1{,}73\): links van \(-1{,}5\), maar nog niet bij \(-2\).",
    ),
    klik(
        r"Klik op het punt dat \(\sqrt{5}\) voorstelt.",
        f"{AS}.svg",
        [_ZONES["D"]],
        r"\(2^{2} = 4\) en \(3^{2} = 9\), dus \(\sqrt{5}\) ligt tussen \(2\) en \(3\), dicht bij \(2\): \(\sqrt{5} \approx 2{,}24\).",
    ),
    klik(
        r"Klik op het punt dat \(-\tfrac{1}{3}\) voorstelt.",
        f"{AS}.svg",
        [_ZONES["B"]],
        r"\(-\tfrac{1}{3} = -0{,}333\ldots\): tussen \(-0{,}5\) en \(0\).",
    ),
    met_prent(f"{AS}.svg", tabel(
        "Punt E ligt op 2,7. Behoren de getallen bij deze punten tot ℚ?",
        [
            ("punt A", "Nee"),
            ("punt B", "Ja"),
            ("punt C", "Ja"),
            ("punt D", "Nee"),
            ("punt E", "Ja"),
        ],
        r"B is \(-\tfrac{1}{3}\), C is \(0{,}75 = \tfrac{3}{4}\), E is \(2{,}7 = \tfrac{27}{10}\): allemaal breuken. A en D zijn \(-\sqrt{3}\) en \(\sqrt{5}\), irrationaal.",
        kolommen=["Ja", "Nee"],
    )),
    klik(
        r"Klik op het punt dat \(75\%\) voorstelt.",
        f"{AS}.svg",
        [_ZONES["C"]],
        r"\(75\% = 0{,}75 = \tfrac{3}{4}\): tussen \(0{,}5\) en \(1\), precies halfweg.",
    ),
    mk(
        r"Welk punt op de getallenas ligt het dichtst bij \(\sqrt[3]{20}\)?",
        ["A", "C", "D", "E"],
        3,
        r"\(\sqrt[3]{20} \approx 2{,}71\), want \(2{,}7^{3} \approx 19{,}7\). Punt E ligt op \(2{,}7\). D is \(\sqrt{5} \approx 2{,}24\).",
    ),
    inv(
        r"Vereenvoudig \(\sqrt{75}\). Typ bijvoorbeeld 2√5.",
        ["5√3", "5 √3", "5 wortel 3", "5wortel3"],
        r"\(\sqrt{75} = \sqrt{25 \cdot 3} = 5\sqrt{3}\).",
    ),
    mk(
        r"Hoeveel is \(\dfrac{2^{5} \cdot 2^{-3}}{2^{-1}}\)?",
        [r"\(2\)", r"\(4\)", r"\(8\)", r"\(\tfrac{1}{2}\)"],
        2,
        r"\(2^{5 - 3 - (-1)} = 2^{3} = 8\).",
    ),
    sorteer(
        "Welke decimale vorm heeft dit getal?",
        ["Begrensd", "Onbegrensd repeterend", "Onbegrensd niet-repeterend"],
        [
            (r"\(\tfrac{7}{8}\)", "Begrensd"),
            (r"\(\tfrac{5}{11}\)", "Onbegrensd repeterend"),
            (r"\(\sqrt{7}\)", "Onbegrensd niet-repeterend"),
            (r"\(\tfrac{2}{3}\)", "Onbegrensd repeterend"),
            (r"\(\pi\)", "Onbegrensd niet-repeterend"),
            (r"\(\sqrt{0{,}25}\)", "Begrensd"),
        ],
        r"\(\tfrac{7}{8} = 0{,}875\), \(\tfrac{5}{11} = 0{,}4545\ldots\), \(\tfrac{2}{3} = 0{,}666\ldots\), \(\sqrt{0{,}25} = 0{,}5\). \(\sqrt{7}\) en \(\pi\) zijn irrationaal.",
    ),
    tabel(
        "Klopt deze uitspraak over de getalverzamelingen?",
        [
            (r"\(-4 \in \mathbb{Z}\)", J),
            (r"\(\tfrac{12}{4} \in \mathbb{N}\)", J),
            (r"\(\sqrt{16} \notin \mathbb{Q}\)", F),
            (r"\(0{,}1010010001\ldots\) (telkens een nul meer) is rationaal", F),
            (r"Elk getal uit \(\mathbb{Q}\) zit ook in \(\mathbb{R}\)", J),
        ],
        r"\(\tfrac{12}{4} = 3\) en \(\sqrt{16} = 4\) zijn natuurlijke getallen. Een decimale vorm die nooit gaat herhalen, is irrationaal.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Hoeveel is \(\sqrt{12} + \sqrt{27}\)?",
        [r"\(\sqrt{39}\)", r"\(5\sqrt{3}\)", r"\(6\sqrt{3}\)", r"\(13\sqrt{3}\)"],
        1,
        r"\(\sqrt{12} = 2\sqrt{3}\) en \(\sqrt{27} = 3\sqrt{3}\). Samen \(5\sqrt{3}\). Een wortel splitst niet over een som, dus \(\sqrt{39}\) is fout.",
    ),
    mk(
        r"Hoeveel is \(\sqrt{8} \cdot \sqrt{18}\)?",
        [r"\(\sqrt{26}\)", r"\(12\)", r"\(6\sqrt{2}\)", r"\(144\)"],
        1,
        r"\(\sqrt{8 \cdot 18} = \sqrt{144} = 12\).",
    ),
    mk(
        r"Maak de noemer wortelvrij: \(\dfrac{6}{\sqrt{3}}\)",
        [r"\(2\sqrt{3}\)", r"\(\dfrac{6}{3}\)", r"\(3\sqrt{6}\)", r"\(\dfrac{\sqrt{3}}{6}\)"],
        0,
        r"\(\dfrac{6}{\sqrt{3}} \cdot \dfrac{\sqrt{3}}{\sqrt{3}} = \dfrac{6\sqrt{3}}{3} = 2\sqrt{3}\).",
    ),
    tabel(
        "Klopt deze rekenregel? (a en b zijn positief)",
        [
            (r"\(a^{3} \cdot a^{5} = a^{8}\)", J),
            (r"\(\left(a^{2}\right)^{4} = a^{6}\)", F),
            (r"\(a^{-2} = \dfrac{1}{a^{2}}\)", J),
            (r"\((ab)^{3} = a^{3}b^{3}\)", J),
            (r"\(a^{2} + a^{3} = a^{5}\)", F),
            (r"\(\dfrac{a^{3}}{a^{7}} = a^{-4}\)", J),
        ],
        r"Macht van een macht: exponenten vermenigvuldigen, dus \(a^{8}\). Een som van machten kan je niet samenvoegen.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Schrijf \(\dfrac{a^{5} \cdot a^{-2}}{a^{4}}\) als één macht van \(a\). Typ bijvoorbeeld a^3.",
        ["a^-1", "a^(-1)", "1/a"],
        r"\(a^{5 - 2 - 4} = a^{-1} = \dfrac{1}{a}\).",
    ),
    mk(
        r"Hoeveel is \(\left(\tfrac{2}{3}\right)^{-2}\)?",
        [r"\(\tfrac{4}{9}\)", r"\(-\tfrac{4}{9}\)", r"\(\tfrac{9}{4}\)", r"\(-\tfrac{9}{4}\)"],
        2,
        r"Een negatieve exponent keert de breuk om: \(\left(\tfrac{3}{2}\right)^{2} = \tfrac{9}{4}\). Het teken wordt niet negatief.",
    ),
    inv(
        r"Hoeveel is \(\sqrt[3]{-8}\)?",
        ["-2", "−2", "min 2"],
        r"\((-2)^{3} = -8\). Een derdemachtswortel van een negatief getal bestaat wel, een vierkantswortel niet.",
    ),
    mk(
        r"Welk getal ligt tussen \(\sqrt{30}\) en \(\sqrt{40}\)?",
        [r"\(5\)", r"\(7\)", r"\(6\)", r"\(4{,}5\)"],
        2,
        r"\(6^{2} = 36\) ligt tussen \(30\) en \(40\). \(5^{2} = 25\) en \(7^{2} = 49\) liggen erbuiten.",
    ),
    koppel(
        "Verbind elke berekening met de eigenschap die gebruikt wordt.",
        [
            (r"\(7 \cdot 13 = 13 \cdot 7\)", "commutativiteit"),
            (r"\((4 \cdot 25) \cdot 9 = 4 \cdot (25 \cdot 9)\)", "associativiteit"),
            (r"\(6 \cdot 98 = 6 \cdot 100 - 6 \cdot 2\)", "distributiviteit"),
        ],
        ["wortelvrij maken"],
        "Wisselen van volgorde, anders groeperen, en een vermenigvuldiging over een som of verschil verdelen.",
    ),
    inv(
        r"Bereken handig met de distributiviteit: \(12 \cdot 99\)",
        ["1188"],
        r"\(12 \cdot (100 - 1) = 1200 - 12 = 1188\).",
    ),
    casus(
        r"Een vierkante tuin heeft een oppervlakte van \(50\) m\(^{2}\). Een kubusvormige bak heeft een inhoud van \(64\) liter, dat is \(64\) dm\(^{3}\).",
        [
            mk("Hoe lang is een zijde van de tuin, exact?",
               [r"\(25\) m", r"\(5\sqrt{2}\) m", r"\(2\sqrt{5}\) m", r"\(10\sqrt{5}\) m"], 1,
               r"\(\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2} \approx 7{,}07\) m."),
            mk("Is die zijde een rationaal getal?",
               ["ja, want het is een lengte die je kan meten",
                r"nee, want \(\sqrt{2}\) is irrationaal en \(5\sqrt{2}\) dus ook",
                "ja, want je kan ze afronden tot 7,07",
                r"nee, want \(50\) is geen kwadraat van een even getal"], 1,
               r"Een afronding is niet de exacte waarde. \(5\sqrt{2}\) kan je niet als breuk schrijven."),
            inv("Hoe lang is een ribbe van de bak in dm?",
                ["4", "4 dm"],
                r"\(\sqrt[3]{64} = 4\), want \(4 \cdot 4 \cdot 4 = 64\)."),
        ],
    ),
    mk(
        r"Welke uitdrukking is gelijk aan \(\sqrt{a^{2} b^{4}}\) voor positieve \(a\) en \(b\)?",
        [r"\(ab^{2}\)", r"\(a^{2}b\)", r"\(ab\)", r"\(a b^{4}\)"],
        0,
        r"\(\sqrt{a^{2}} = a\) en \(\sqrt{b^{4}} = b^{2}\).",
    ),
    keuze(
        r"\(0{,}75\) is gelijk aan de breuk [[*\(\tfrac{3}{4}\)|\(\tfrac{7}{5}\)]] en aan [[*\(75\%\)|\(7{,}5\%\)]]. Het is een [[*rationaal|irrationaal]] getal.",
        r"\(0{,}75 = \tfrac{75}{100} = \tfrac{3}{4} = 75\%\). Een eindige decimale vorm is altijd rationaal.",
    ),
    tabel(
        "Ligt het getal tussen 2 en 3?",
        [
            (r"\(\sqrt{8}\)", J),
            (r"\(\sqrt[3]{20}\)", J),
            (r"\(\sqrt{10}\)", F),
            (r"\(\tfrac{17}{6}\)", J),
            (r"\(2^{-1}\)", F),
        ],
        r"\(\sqrt{8} \approx 2{,}83\), \(\sqrt[3]{20} \approx 2{,}71\), \(\tfrac{17}{6} \approx 2{,}83\). \(\sqrt{10} \approx 3{,}16\) en \(2^{-1} = 0{,}5\) liggen erbuiten.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Schrijf \(0{,}000\,8\) als macht van tien maal een geheel getal: \(8 \cdot 10^{n}\). Wat is \(n\)?",
        ["-4", "−4"],
        r"\(0{,}000\,8 = \dfrac{8}{10\,000} = 8 \cdot 10^{-4}\).",
    ),
    mk(
        r"Een leerling schrijft \(\sqrt{16 + 9} = 4 + 3 = 7\). Wat is de juiste uitkomst?",
        [r"\(7\)", r"\(5\)", r"\(25\)", r"\(\sqrt{7}\)"],
        1,
        r"Eerst de som: \(\sqrt{25} = 5\). Een wortel mag je niet over een som splitsen.",
    ),
    sleep(
        "Een getal dat je als breuk van twee gehele getallen kan schrijven, heet [[rationaal]]. Zijn decimale vorm is begrensd of [[repeterend]]. Een getal zoals √2 heet [[irrationaal]].",
        ["natuurlijk", "negatief"],
        "Rationaal, repeterend, irrationaal.",
    ),
    mk(
        r"Hoeveel is \((-2a^{2})^{3}\)?",
        [r"\(-8a^{6}\)", r"\(-6a^{5}\)", r"\(8a^{6}\)", r"\(-8a^{5}\)"],
        0,
        r"\((-2)^{3} = -8\) en \(\left(a^{2}\right)^{3} = a^{6}\).",
    ),
]
