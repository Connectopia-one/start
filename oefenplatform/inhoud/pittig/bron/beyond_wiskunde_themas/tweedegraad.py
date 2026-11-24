"""Tweedegraadsfuncties en transformaties — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("tweedegraad-drie-parabolen-bey", -5, 5, -4, 6)

GRAFIEKEN = [
    dict(naam=GRAF, titel="Drie parabolen f, g en h",
         krommen=[(lambda x: x * x, "groen", "f", (-2.4, 2.4)), (lambda x: -(x - 2) ** 2 + 3, "blauw", "g", (-0.6, 4.6)), (lambda x: 0.5 * (x + 2) ** 2 - 2, "oranje", "h", (-5, 1.4))],
         labelplek={"f": (-2.2, 5.5), "g": (4.3, -1.5), "h": (-4.8, 2.8)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="parabolen x², −(x − 2)² + 3 en ½(x + 2)² − 2", vragen="klikvragen over top, nulwaarden en transformaties")]

VRAGEN = [
    klik(
        "Klik op de top van de bergparabool.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2, 3)],
        r"g opent naar beneden en heeft haar top in \((2, 3)\): \(g(x) = -(x - 2)^{2} + 3\).",
    ),
    klik(
        r"De parabool \(h\) ontstaat uit \(f\) door te verschuiven en te vervormen. Klik op de top van \(h\).",
        f"{GRAF}.svg",
        [punt_zone(GRAF, -2, -2)],
        r"\(h(x) = \tfrac{1}{2}(x + 2)^{2} - 2\): twee naar links en twee naar beneden, en breder door de factor \(\tfrac{1}{2}\).",
    ),
    klik(
        r"Klik op de grootste nulwaarde van \(g\).",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2 + 3 ** 0.5, 0)],
        r"\((x - 2)^{2} = 3\) geeft \(x = 2 \pm \sqrt{3}\). De grootste is ongeveer \(3{,}73\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de drie parabolen. Welk voorschrift hoort bij welke grafiek?",
        [(r"\(y = x^{2}\)", "f"), (r"\(y = -(x - 2)^{2} + 3\)", "g"), (r"\(y = \tfrac{1}{2}(x + 2)^{2} - 2\)", "h")],
        "Kijk naar de top en de opening.",
        kolommen=["f", "g", "h"],
    )),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de drie parabolen. Juist of fout?",
        [("Het bereik van g is ]−∞, 3].", J), ("h is breder dan f.", J), ("g heeft geen nulwaarden.", F), ("De symmetrieas van h is x = −2.", J), ("h snijdt de y-as in (0, −2).", F)],
        r"\(h(0) = \tfrac{1}{2}\cdot 4 - 2 = 0\): h gaat door de oorsprong.",
        kolommen=["Juist", "Fout"],
    )),
    mk(
        r"Wat is de top van \(f(x) = 2x^{2} - 12x + 7\)?",
        [r"\((3, -11)\)", r"\((-3, 61)\)", r"\((3, 7)\)", r"\((6, 7)\)"],
        0,
        r"\(x = -\tfrac{b}{2a} = 3\) en \(f(3) = 18 - 36 + 7 = -11\).",
    ),
    mk(
        r"Een parabool heeft nulwaarden \(-1\) en \(5\) en gaat door \((0, 10)\). Wat is haar top?",
        [r"\((2, 18)\)", r"\((2, 9)\)", r"\((2, -18)\)", r"\((3, 16)\)"],
        0,
        r"\(y = a(x + 1)(x - 5)\) met \(a \cdot (-5) = 10\), dus \(a = -2\). Top bij \(x = 2\): \(-2 \cdot 3 \cdot (-3) = 18\).",
    ),
    koppel(
        r"Hoe ontstaat de grafiek uit die van \(f\)?",
        [(r"\(f(x - 3)\)", "3 naar rechts"), (r"\(f(x) - 3\)", "3 naar beneden"), (r"\(3f(x)\)", "verticaal uitrekken met factor 3"), (r"\(-f(x)\)", "spiegelen om de x-as"), (r"\(f(-x)\)", "spiegelen om de y-as")],
        ["3 naar links"],
        r"Wat bij \(x\) binnen de haakjes gebeurt, werkt horizontaal en omgekeerd. Wat buiten \(f\) staat, werkt verticaal.",
    ),
    inv(
        r"Voor welke \(k\) raakt de rechte \(y = 2x + k\) de parabool \(y = x^{2}\)?",
        ["-1", "−1"],
        r"\(x^{2} - 2x - k = 0\) moet één oplossing hebben: \(D = 4 + 4k = 0\), dus \(k = -1\).",
    ),
    casus(
        r"Een fontein spuit water. De hoogte in meter is \(h(x) = -0{,}5x^{2} + 2x + 1\), met \(x\) de horizontale afstand in meter.",
        [
            inv("Hoe hoog spuit het water maximaal, in meter?", ["3", "3 m"], r"Top bij \(x = -\tfrac{2}{2 \cdot (-0{,}5)} = 2\): \(h(2) = -2 + 4 + 1 = 3\)."),
            mk("Op welke afstand valt het water op de grond, afgerond op cm?", ["4,45 m", "4 m", "2 m", "5,45 m"], 0, r"\(-0{,}5x^{2} + 2x + 1 = 0\) geeft \(x = 2 + \sqrt{6} \approx 4{,}45\)."),
            mk("Wat stelt de 1 in het voorschrift voor?", ["de hoogte van de spuitmond", "de hoogste stand van het water", "de afstand tot de grond", "de steilheid van de straal"], 0, "Bij x = 0 is h = 1: het water vertrekt op 1 m hoogte."),
        ],
    ),
    tabel(
        r"Wat weet je over \(f(x) = ax^{2} + bx + c\)?",
        [(r"\(a > 0\) en \(D < 0\)", "altijd positief"), (r"\(a < 0\) en \(D < 0\)", "altijd negatief"), (r"\(a > 0\) en \(D = 0\)", "nooit negatief"), (r"\(a < 0\) en \(D > 0\)", "positief tussen de nulwaarden")],
        "De opening en het aantal nulwaarden bepalen samen het tekenverloop.",
        kolommen=["altijd positief", "altijd negatief", "nooit negatief", "positief tussen de nulwaarden"],
    ),
    mk(
        r"Welke parabool heeft top \((-1, 4)\) en gaat door \((1, -4)\)?",
        [r"\(y = -2(x + 1)^{2} + 4\)", r"\(y = 2(x + 1)^{2} + 4\)", r"\(y = -2(x - 1)^{2} + 4\)", r"\(y = -(x + 1)^{2} + 4\)"],
        0,
        r"\(-4 = a(1 + 1)^{2} + 4\) geeft \(4a = -8\), \(a = -2\).",
    ),
    sorteer(
        "Verandert deze transformatie de nulwaarden van een parabool?",
        ["Nulwaarden blijven", "Nulwaarden veranderen"],
        [(r"\(3f(x)\)", "Nulwaarden blijven"), (r"\(-f(x)\)", "Nulwaarden blijven"), (r"\(f(x) + 1\)", "Nulwaarden veranderen"), (r"\(f(x + 2)\)", "Nulwaarden veranderen"), (r"\(\tfrac{1}{2}f(x)\)", "Nulwaarden blijven")],
        r"Bij \(k \cdot f(x)\) met \(k \neq 0\) blijft \(f(x) = 0\) gelijk aan \(k f(x) = 0\). Verschuiven verplaatst de nulwaarden.",
    ),
    inv(
        r"Een rechthoekige tuin langs een muur krijgt 24 m draad aan drie kanten. Wat is de grootste oppervlakte, in m²?",
        ["72", "72 m²"],
        r"Breedte \(x\), lengte \(24 - 2x\): \(A = x(24 - 2x)\). Top bij \(x = 6\): \(6 \cdot 12 = 72\).",
    ),
    keuze(
        r"In \(f(x) = a(x - p)^{2} + q\) bepaalt \(a\) de [[*opening en breedte|top|symmetrieas]]. De top is [[*\((p, q)\)|\((-p, q)\)|\((q, p)\)]].",
        "Deze vorm heet de topvorm.",
    ),
    mk(
        r"Voor welke \(m\) heeft \(f(x) = mx^{2} + 4x + m\) geen nulwaarden en ligt ze helemaal boven de x-as?",
        [r"\(m > 2\)", r"\(-2 < m < 2\)", r"\(m < -2\)", r"\(m > 0\)"],
        0,
        r"Nodig: \(m > 0\) en \(D = 16 - 4m^{2} < 0\), dus \(m^{2} > 4\). Samen \(m > 2\).",
    ),
    tabel(
        r"De parabool \(y = x^{2}\) ondergaat de transformatie. Wat is de nieuwe top?",
        [("2 naar links, dan 3 omhoog", "(−2, 3)"), ("spiegelen om de x-as, dan 1 naar rechts", "(1, 0)"), ("verticaal uitrekken met 4, dan 5 omlaag", "(0, −5)")],
        "Uitrekken en spiegelen om de x-as laten de top (0, 0) op zijn plaats. Verschuivingen verplaatsen hem.",
        kolommen=["(−2, 3)", "(1, 0)", "(0, −5)"],
    ),
    sleep(
        r"Als een parabool de \(x\)-as raakt, is de discriminant [[nul]] en ligt de top [[op]] de \(x\)-as.",
        ["positief", "boven"],
        r"Eén nulwaarde: \(x = -\tfrac{b}{2a}\), en dat is precies de top.",
    ),
    mk(
        r"De som van twee getallen is 14. Wat is hun grootste mogelijke product?",
        ["49", "48", "196", "14"],
        0,
        r"\(x(14 - x)\) is een bergparabool met top bij \(x = 7\): \(7 \cdot 7 = 49\).",
    ),
    volgorde(
        r"Zet de stappen om \(x^{2} - 4x + 1\) in topvorm te schrijven in volgorde.",
        [r"\(x^{2} - 4x\) aanvullen tot een kwadraat", r"\(x^{2} - 4x + 4 - 4 + 1\) schrijven", r"\((x - 2)^{2} - 3\) noteren", r"top \((2, -3)\) aflezen"],
        "Kwadraatafsplitsen: tel de helft van de coëfficiënt van x in het kwadraat op en trek het weer af.",
    ),
    tabel(
        "Juist of fout?",
        [("Elke parabool heeft precies één top.", J), ("Een parabool met a < 0 heeft een minimum.", F), ("Twee parabolen met dezelfde top zijn gelijk.", F), ("Een parabool snijdt de y-as precies één keer.", J)],
        r"Met dezelfde top kan \(a\) nog verschillen. Elke parabool \(y = ax^{2} + bx + c\) snijdt de y-as in \((0, c)\).",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"De parabool \(y = x^{2} + bx + 8\) heeft haar top bij \(x = 3\). Hoeveel is \(b\)?",
        ["-6", "−6"],
        r"\(-\tfrac{b}{2} = 3\) geeft \(b = -6\).",
    ),
    mk(
        r"Een bal volgt \(h(t) = -5t^{2} + 20t + 25\). Wanneer raakt hij de grond?",
        [r"na \(5\) s", r"na \(2\) s", r"na \(1\) s", r"na \(4\) s"],
        0,
        r"\(-5(t^{2} - 4t - 5) = -5(t - 5)(t + 1) = 0\): \(t = 5\). Negatieve tijd valt weg.",
    ),
    tabel(
        r"Welke uitspraak past bij \(f(x) = -3(x + 1)^{2} + 6\)?",
        [("bergparabool", J), ("symmetrieas x = 1", F), ("maximum 6", J), ("twee nulwaarden", J), ("snijpunt met de y-as (0, 6)", F)],
        r"De symmetrieas is \(x = -1\). \(f(0) = -3 + 6 = 3\). \(-3(x + 1)^{2} = -6\) geeft \((x + 1)^{2} = 2\): twee nulwaarden.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Welke transformatie brengt de grafiek van \(y = x^{2}\) naar die van \(y = x^{2} + 6x + 5\)?",
        ["3 naar links en 4 naar beneden", "3 naar rechts en 5 naar boven", "6 naar links en 5 naar boven", "3 naar links en 5 naar boven"],
        0,
        r"\(x^{2} + 6x + 5 = (x + 3)^{2} - 4\).",
    ),
    inv(
        r"Hoeveel snijpunten hebben \(y = x^{2} - 2x\) en \(y = -x^{2} + 4\)?",
        ["2", "twee"],
        r"\(2x^{2} - 2x - 4 = 0\) geeft \(x^{2} - x - 2 = 0\): \(x = 2\) of \(x = -1\).",
    ),
    tabel(
        r"Wat is het bereik?",
        [(r"\(y = (x - 1)^{2} + 2\)", r"\(\left[2, +\infty\right[\)"), (r"\(y = -x^{2} + 5\)", r"\(\left]-\infty, 5\right]\)"), (r"\(y = 2x^{2} - 8\)", r"\(\left[-8, +\infty\right[\)")],
        "Het bereik begint of eindigt bij de y-coördinaat van de top.",
        kolommen=[r"\(\left[2, +\infty\right[\)", r"\(\left]-\infty, 5\right]\)", r"\(\left[-8, +\infty\right[\)"],
    ),
    keuze(
        r"De grafiek van \(f(2x)\) is die van \(f\) [[*horizontaal samengedrukt|horizontaal uitgerekt|verticaal uitgerekt]] met factor 2.",
        r"Wat bij \(x\) gebeurt, werkt omgekeerd: \(f(2x)\) bereikt dezelfde waarden al bij de helft van \(x\).",
    ),
]
