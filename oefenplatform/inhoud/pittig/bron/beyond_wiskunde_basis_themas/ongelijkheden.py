"""Bedrijfswetenschappen: ongelijkheden oplossen — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, strook_zone

FG_GRAF = venster("ongelijkheden-fg", -3, 5, -7, 5, 1, 1)
SIN_GRAF = venster("ongelijkheden-sinus", 0, 2 * math.pi, -2.5, 2.5, math.pi / 6, 0.5)
EX_GRAF = venster("ongelijkheden-exp", 0, 10, 0, 3.5, 1, 0.5)


def _f(x):
    return -x * x + 2 * x + 3


def _g(x):
    return x - 3


_PI = {1: "π/6", 2: "π/3", 3: "π/2", 4: "2π/3", 5: "5π/6", 6: "π", 7: "7π/6", 8: "4π/3", 9: "3π/2", 10: "5π/3", 11: "11π/6", 12: "2π"}

GRAFIEKEN = [
    dict(naam=FG_GRAF, titel="De grafieken van f en g",
         krommen=[(_f, "groen", "f", (-2.6, 4.4)), (_g, "blauw", "g", (-3, 5))],
         labelplek={"f": (-0.6, _f(-0.6)), "g": (4.6, _g(4.6))}),
    dict(naam=SIN_GRAF, titel="De grafiek van f(x) = 2 sin x",
         krommen=[(lambda x: 2 * math.sin(x), "oranje", "", (0, 2 * math.pi))],
         ijk_x=math.pi / 6, ijk_y=1, xnamen={k * (math.pi / 6): v for k, v in _PI.items()}),
    dict(naam=EX_GRAF, titel="De grafiek van f(x) = 3 · 0,8ˣ",
         krommen=[(lambda x: 3 * 0.8 ** x, "paars", "", (0, 10))], stippel=[("h", 1)], ijk_x=1, ijk_y=0.5),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over ongelijkheden") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        r"Klik boven een x-waarde waarvoor \(f(x) < g(x)\).",
        f"{FG_GRAF}.svg",
        [strook_zone(FG_GRAF, -3, -2.08), strook_zone(FG_GRAF, 3.08, 5)],
        r"De grafiek van f ligt onder die van g links van \(x = -2\) en rechts van \(x = 3\), de x-waarden van de snijpunten.",
    ),
    met_prent(f"{FG_GRAF}.svg", mk(
        r"Wat is de oplossingenverzameling van \(f(x) \geq 0\)?",
        [r"\(]-1, 3[\)", r"\([-1, 3]\)", r"\(]-\infty, -1] \cup [3, +\infty[\)", r"\([0, 4]\)"],
        1,
        r"f ligt boven of op de x-as tussen de nulwaarden \(-1\) en \(3\). Bij \(\geq\) horen de grenzen erbij.",
    )),
    met_prent(f"{FG_GRAF}.svg", mk(
        r"Wat is de oplossingenverzameling van \(f(x) > 3\)?",
        [r"\(]0, 2[\)", r"\([0, 2]\)", r"\(]-1, 3[\)", r"\(]1, 4[\)"],
        0,
        r"De rechte \(y = 3\) snijdt f in \(x = 0\) en \(x = 2\). Daartussen ligt f erboven. Strikt groter: open grenzen.",
    )),
    klik(
        r"Klik boven een x-waarde in \([0, 2\pi]\) waarvoor \(2 \sin x < -1\).",
        f"{SIN_GRAF}.svg",
        [strook_zone(SIN_GRAF, 7 * math.pi / 6 + 0.05, 11 * math.pi / 6 - 0.05)],
        r"\(2 \sin x = -1\) in \(\frac{7\pi}{6}\) en \(\frac{11\pi}{6}\). Daartussen ligt de grafiek onder \(y = -1\).",
    ),
    met_prent(f"{SIN_GRAF}.svg", mk(
        r"Los op in \([0, 2\pi]\): \(2 \sin x \geq 1\).",
        [r"\(\left[\frac{\pi}{6}, \frac{5\pi}{6}\right]\)", r"\(\left[\frac{\pi}{3}, \frac{2\pi}{3}\right]\)", r"\(\left]\frac{\pi}{6}, \frac{5\pi}{6}\right[\)", r"\(\left[0, \pi\right]\)"],
        0,
        r"\(\sin x \geq \frac{1}{2}\) vanaf \(\frac{\pi}{6}\) tot \(\frac{5\pi}{6}\), grenzen inbegrepen.",
    )),
    met_prent(f"{EX_GRAF}.svg", mk(
        r"Voor welke \(x \geq 0\) is \(3 \cdot 0{,}8^x \leq 1\)? Lees af op de grafiek.",
        [r"\(]-\infty;\ 4{,}9]\)", r"\([0;\ 4{,}9]\)", r"Ongeveer \([4{,}9;\ +\infty[\)", r"\([3;\ +\infty[\)"],
        2,
        r"De dalende grafiek zakt onder de stippellijn \(y = 1\) bij ongeveer \(x = 4{,}9\) en blijft er daarna onder.",
    )),
    tabel(
        r"Wat is het teken van \(2x^2 - 8\) op elk interval?",
        [
            (r"\(]-\infty, -2[\)", "+"),
            (r"\(]-2, 2[\)", "−"),
            (r"\(]2, +\infty[\)", "+"),
        ],
        r"Nulwaarden \(\pm 2\). Een dalparabool (\(a = 2 > 0\)) is negatief tussen de nulwaarden en positief erbuiten.",
        kolommen=["+", "−", "0"],
    ),
    mk(
        r"Los op: \(x^2 - 7x + 10 < 0\).",
        [r"\(]-\infty, 2[ \cup ]5, +\infty[\)", r"\([2, 5]\)", r"\(]2, 5[\)", r"\(]-5, -2[\)"],
        2,
        r"Nulwaarden \(2\) en \(5\). Negatief tussen de nulwaarden, en strikt: open grenzen.",
    ),
    mk(
        r"Los op: \(-x^2 + 4x \geq 0\).",
        [r"\([0, 4]\)", r"\(]-\infty, 0] \cup [4, +\infty[\)", r"\(]0, 4[\)", r"\([-4, 0]\)"],
        0,
        r"\(-x(x - 4)\) heeft nulwaarden \(0\) en \(4\). Een bergparabool is positief tussen de nulwaarden.",
    ),
    mk(
        r"Los op: \(x^2 + 2x + 5 > 0\).",
        [r"\(\varnothing\)", r"\(]-1, +\infty[\)", r"\(\mathbb{R}\)", r"\(]-5, 1[\)"],
        2,
        r"\(D = 4 - 20 < 0\): geen nulwaarden. De dalparabool ligt volledig boven de x-as.",
    ),
    mk(
        r"Los op: \(x^2 - 6x + 9 \leq 0\).",
        [r"\(\{3\}\)", r"\(\varnothing\)", r"\(]-\infty, 3]\)", r"\(\mathbb{R}\)"],
        0,
        r"\((x - 3)^2 \leq 0\). Een kwadraat is nooit negatief, dus enkel \(x = 3\) voldoet.",
    ),
    tabel(
        "Juist of fout over ongelijkheden?",
        [
            ("De oplossing van een ongelijkheid noteer je meestal als interval of als unie van intervallen.", J),
            ("Een tweedegraadsongelijkheid heeft altijd twee intervalgrenzen.", F),
            ("Bij een strikte ongelijkheid zijn de grenzen bij de nulwaarden open.", J),
            (r"De oplossingenverzameling van \(x^2 < 0\) is \(\{0\}\).", F),
        ],
        r"Zonder nulwaarden is de oplossing \(\mathbb{R}\) of \(\varnothing\). \(0^2 = 0\) is niet kleiner dan 0.",
    ),
    keuze(
        r"Bij een dalparabool \(ax^2 + bx + c\) (\(a > 0\)) met twee nulwaarden is de uitdrukking [[*negatief|positief|nul]] tussen de nulwaarden en [[*positief|negatief|nul]] erbuiten.",
        "Een dalparabool hangt met haar top onder de x-as.",
    ),
    sorteer(
        "Hoort het getal 3 bij de verzameling?",
        ["3 hoort erbij", "3 hoort er niet bij"],
        [
            [r"\([-1, 3]\)", "3 hoort erbij"],
            [r"\(]-1, 3[\)", "3 hoort er niet bij"],
            [r"\([3, +\infty[\)", "3 hoort erbij"],
            [r"\(]-\infty, 3[\)", "3 hoort er niet bij"],
            [r"\([2, 5]\)", "3 hoort erbij"],
            [r"\(]3, 7]\)", "3 hoort er niet bij"],
        ],
        "Een vierkant haakje naar het getal toe: erbij. Een haakje dat van het getal wegdraait: niet erbij.",
    ),
    volgorde(
        "Zet de stappen om een tweedegraadsongelijkheid op te lossen in de goede volgorde.",
        [
            r"Breng alles naar één lid: \(ax^2 + bx + c\) tegenover \(0\)",
            "Bereken de nulwaarden",
            "Maak een tekenverloop",
            "Lees de gevraagde intervallen af en noteer de oplossingenverzameling",
        ],
        "Eerst nul aan één kant, dan nulwaarden, dan tekens.",
    ),
    koppel(
        "Koppel de ongelijkheid aan haar oplossingenverzameling.",
        [
            [r"\(x^2 - 1 > 0\)", r"\(]-\infty, -1[ \cup ]1, +\infty[\)"],
            [r"\(x^2 - 1 \leq 0\)", r"\([-1, 1]\)"],
            [r"\(x^2 + 1 < 0\)", r"\(\varnothing\)"],
            [r"\(x^2 + 1 > 0\)", r"\(\mathbb{R}\)"],
        ],
        [r"\(]-1, 1[\)"],
        r"\(x^2 - 1\) wisselt van teken in \(\pm 1\). \(x^2 + 1\) is altijd positief.",
    ),
    mk(
        r"De winst van een bedrijf is \(W(q) = -2q^2 + 40q - 150\) (q in honderden stuks). Voor welke q maakt het bedrijf winst?",
        [r"\([5, 15]\)", r"\(]0, 20[\)", r"\(]-\infty, 5[ \cup ]15, +\infty[\)", r"\(]5, 15[\)"],
        3,
        r"\(W(q) > 0\) geeft \(q^2 - 20q + 75 < 0\), nulwaarden \(5\) en \(15\). Winst strikt tussen beide.",
    ),
    mk(
        r"Een bal wordt opgeschoten: \(h(t) = -5t^2 + 30t\) (m, t in s). Wanneer is de bal hoger dan 40 m?",
        [r"Tussen \(2\) s en \(4\) s", r"Na \(4\) s", r"Tussen \(0\) s en \(6\) s", r"Enkel op \(3\) s"],
        0,
        r"\(-5t^2 + 30t > 40\) geeft \(t^2 - 6t + 8 < 0\), nulwaarden \(2\) en \(4\).",
    ),
    inv(
        "Abonnement A kost 10 euro plus 0,05 euro per belminuut. Abonnement B kost vast 18 euro. Vanaf hoeveel belminuten is B goedkoper? Geef het aantal minuten waarboven dat geldt.",
        "160",
        r"\(10 + 0{,}05x > 18\) geeft \(0{,}05x > 8\), dus \(x > 160\).",
    ),
    mk(
        r"Een kapitaal groeit volgens \(K(t) = 500 \cdot 1{,}04^t\) (t in jaar). Vanaf welk volle jaar is het meer dan 800 euro?",
        [r"Vanaf jaar \(8\)", r"Vanaf jaar \(12\)", r"Vanaf jaar \(15\)", r"Vanaf jaar \(10\)"],
        1,
        r"Snij \(y_1 = 500 \cdot 1{,}04^x\) met \(y_2 = 800\): \(x \approx 11{,}98\). Na 12 jaar ligt de grafiek erboven.",
    ),
    sleep(
        r"\(f(x) > 0\) betekent dat de grafiek van f [[boven]] de x-as ligt. \(f(x) \leq g(x)\) betekent dat de grafiek van f [[onder]] of [[op]] die van g ligt.",
        ["naast", "links", "rechts"],
        "Een ongelijkheid vergelijkt hoogtes van grafieken.",
    ),
    open_(
        r"Leg uit waarom je bij \(x^2 - 4 < 0\) niet mag schrijven \(x < \pm 2\).",
        r"\(x^2 < 4\) geldt voor alle getallen tussen \(-2\) en \(2\), dus \(]-2, 2[\). 'x < ±2' zou ook getallen als \(-5\) toelaten, en daar is \(x^2 = 25\) niet kleiner dan 4. Met een tekenverloop zie je dat het teken tussen de nulwaarden negatief is.",
        "Denk aan een getal als −5.",
    ),
    mk(
        r"Los op: \((x - 1)(x + 3) \geq 0\).",
        [r"\([-3, 1]\)", r"\(]-\infty, -3] \cup [1, +\infty[\)", r"\(]-\infty, -1] \cup [3, +\infty[\)", r"\(]-3, 1[\)"],
        1,
        r"Nulwaarden \(-3\) en \(1\). Een dalparabool is positief buiten de nulwaarden.",
    ),
    mk(
        r"Voor welke waarden van c is de oplossingenverzameling van \(x^2 + c > 0\) gelijk aan \(\mathbb{R}\)?",
        [r"\(c < 0\)", r"\(c = 0\)", r"\(c > 0\)", r"Voor elke c"],
        2,
        r"Bij \(c = 0\) valt \(x = 0\) weg, bij \(c < 0\) zijn er nulwaarden met een negatief stuk ertussen.",
    ),
    mk(
        r"Los op: \(-2x + 6 \leq 0\).",
        [r"\(]-\infty, 3]\)", r"\([-3, +\infty[\)", r"\(]-\infty, -3]\)", r"\([3, +\infty[\)"],
        3,
        r"\(-2x \leq -6\). Delen door \(-2\): \(x \geq 3\).",
    ),
    mk(
        r"Los op in \([0, 2\pi]\): \(\sin x > 0\).",
        [r"\(]0, \pi[\)", r"\([0, \pi]\)", r"\(]\pi, 2\pi[\)", r"\(\left]0, \frac{\pi}{2}\right[\)"],
        0,
        r"De sinus is positief in het eerste en tweede kwadrant. In \(0\) en \(\pi\) is ze \(0\).",
    ),
    mk(
        r"Los grafisch op: \(x^3 - 4x > 0\).",
        [r"\(]-\infty, -2[ \cup ]0, 2[\)", r"\(]2, +\infty[\)", r"\(]-2, 0[ \cup ]2, +\infty[\)", r"\(]-2, 2[\)"],
        2,
        r"Nulwaarden \(-2\), \(0\) en \(2\). Een derdegraadsfunctie met positieve hoofdcoëfficiënt is helemaal rechts positief en wisselt bij elke enkelvoudige nulwaarde van teken.",
    ),
    casus(
        r"Een bedrijf maakt q stuks per dag (\(0 \leq q \leq 40\)). De kosten zijn \(K(q) = q^2 + 20q + 100\) euro, de opbrengst \(O(q) = 50q\) euro.",
        [
            mk(
                "Welke ongelijkheid moet je oplossen om te weten wanneer er winst is?",
                [r"\(50q < q^2 + 20q + 100\)", r"\(50q > q^2 + 20q + 100\)", r"\(50q = q^2 + 20q + 100\)", r"\(q^2 + 20q + 100 > 0\)"],
                1,
                "Winst betekent: de opbrengst is groter dan de kosten.",
            ),
            mk(
                "Bij welke aantallen stuks per dag is er winst?",
                [r"Van \(4\) tot en met \(26\) stuks", r"Van \(3\) tot en met \(27\) stuks", r"Van \(10\) tot en met \(20\) stuks", r"Vanaf \(4\) stuks"],
                0,
                r"\(q^2 - 30q + 100 < 0\), nulwaarden \(15 \pm \sqrt{125} \approx 3{,}8\) en \(26{,}2\). q is een geheel aantal.",
            ),
            mk(
                "Bij hoeveel stuks per dag is de winst het grootst?",
                [r"\(26\)", r"\(40\)", r"\(15\)", r"\(4\)"],
                2,
                r"De winst \(-q^2 + 30q - 100\) is een bergparabool met top bij \(q = \frac{30}{2}\).",
            ),
        ],
    ),
]
