"""Tweedegraadsfuncties — pittig (🌍 Beyond, wiskunde basis; niet voor welzijnswetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

# A: y = x², B: y = −(x − 1)² + 4 (bergparabool, top (1, 4), nulwaarden −1 en 3),
# C: y = ½(x + 3)² − 2 (dalparabool, top (−3, −2))
P_GRAF = venster("tweedegraad-parabolen", -7, 5, -5, 9)


def _a(x):
    return x * x


def _b(x):
    return -(x - 1) ** 2 + 4


def _c(x):
    return 0.5 * (x + 3) ** 2 - 2


GRAFIEKEN = [
    dict(naam=P_GRAF, titel="Drie parabolen", krommen=[
        (_a, "groen", "A", (-3, 3)), (_b, "blauw", "B", (-2.2, 4.2)), (_c, "oranje", "C", (-7, 1))],
        labelplek={"A": (2.85, 8.1), "B": (3.9, -4.4), "C": (-6.6, 4.5)}),
]

PRENTEN = [dict(bestand=f"{P_GRAF}.svg", zelf=True, wat="Drie parabolen A, B en C", vragen="klikvragen en vragen over top, nulwaarden en transformaties")]

VRAGEN = [
    klik(
        "Klik op de top van parabool B.",
        f"{P_GRAF}.svg",
        [punt_zone(P_GRAF, 1, 4)],
        r"Parabool B is een bergparabool met top \((1, 4)\): daar bereikt ze haar maximum.",
    ),
    klik(
        "Klik op de top van de dalparabool die niet door de oorsprong gaat.",
        f"{P_GRAF}.svg",
        [punt_zone(P_GRAF, -3, -2)],
        r"A en C zijn dalparabolen. A gaat door \((0, 0)\). De top van C is \((-3, -2)\).",
    ),
    klik(
        "Klik op een nulpunt van parabool B.",
        f"{P_GRAF}.svg",
        [punt_zone(P_GRAF, -1, 0), punt_zone(P_GRAF, 3, 0)],
        r"B snijdt de \(x\)-as in \((-1, 0)\) en in \((3, 0)\).",
    ),
    met_prent(f"{P_GRAF}.svg", tabel(
        "Welk voorschrift hoort bij welke parabool?",
        [
            (r"\(y = -(x - 1)^{2} + 4\)", "B"),
            (r"\(y = \frac{1}{2}(x + 3)^{2} - 2\)", "C"),
            (r"\(y = x^{2}\)", "A"),
        ],
        r"Uit \(a(x - p)^{2} + q\) lees je de top \((p, q)\) af. Een negatieve \(a\) geeft een bergparabool.",
        kolommen=["A", "B", "C"],
    )),
    met_prent(f"{P_GRAF}.svg", mk(
        "Hoe ontstaat parabool C uit parabool A?",
        [
            r"Verticaal uitrekken met factor \(\frac{1}{2}\), \(3\) naar links en \(2\) naar onder verschuiven",
            r"Verticaal uitrekken met factor \(2\), \(3\) naar rechts en \(2\) naar onder verschuiven",
            r"Spiegelen rond de \(x\)-as, \(3\) naar links en \(2\) naar onder verschuiven",
            r"Verticaal uitrekken met factor \(\frac{1}{2}\), \(3\) naar rechts en \(2\) naar boven verschuiven",
        ],
        0,
        r"In \(\frac{1}{2}(x + 3)^{2} - 2\) staat \(x + 3 = x - (-3)\): de top schuift naar \(x = -3\), dus naar links.",
    )),
    met_prent(f"{P_GRAF}.svg", tabel(
        "Juist of fout over de parabolen B en C?",
        [
            (r"De symmetrieas van B is \(x = 1\).", J),
            (r"Het bereik van C is \([-2, +\infty[\).", J),
            (r"B stijgt op \(]-\infty, 1]\).", J),
            (r"C heeft geen nulwaarden.", F),
        ],
        r"De symmetrieas gaat door de top. C is een dalparabool met top onder de \(x\)-as, dus ze snijdt de \(x\)-as twee keer.",
    )),
    inv(
        r"Wat is de \(x\)-coördinaat van de top van \(f(x) = 2x^{2} - 12x + 7\)?",
        "3",
        r"\(x_{\text{top}} = -\frac{b}{2a} = -\frac{-12}{4} = 3\).",
    ),
    mk(
        r"Wat is de top van \(f(x) = -3(x + 2)^{2} + 5\)?",
        [r"\((-2, 5)\)", r"\((2, 5)\)", r"\((-2, -5)\)", r"\((5, -2)\)"],
        0,
        r"Bij \(a(x - p)^{2} + q\) is de top \((p, q)\). Hier is \(x + 2 = x - (-2)\), dus \(p = -2\).",
    ),
    mk(
        r"Een parabool heeft nulwaarden \(-4\) en \(2\) en gaat door \((0, 4)\). Welk voorschrift past?",
        [r"\(y = -\frac{1}{2}(x + 4)(x - 2)\)", r"\(y = (x + 4)(x - 2)\)", r"\(y = \frac{1}{2}(x - 4)(x + 2)\)", r"\(y = -2(x + 4)(x - 2)\)"],
        0,
        r"Vorm \(a(x - x_{1})(x - x_{2}) = a(x + 4)(x - 2)\). In \(x = 0\): \(a \cdot 4 \cdot (-2) = 4\), dus \(a = -\frac{1}{2}\).",
    ),
    tabel(
        "Is het een bergparabool of een dalparabool?",
        [
            (r"\(y = 3 - x^{2}\)", "Bergparabool"),
            (r"\(y = (2 - x)^{2}\)", "Dalparabool"),
            (r"\(y = -\frac{1}{4}(x - 5)(x + 1)\)", "Bergparabool"),
            (r"\(y = 0{,}1x^{2} - 8x\)", "Dalparabool"),
        ],
        r"Kijk naar het teken van de coëfficiënt van \(x^{2}\). Bij \((2 - x)^{2}\) is die \(+1\), want \((2 - x)^{2} = (x - 2)^{2}\).",
        kolommen=["Bergparabool", "Dalparabool"],
    ),
    mk(
        r"De nulwaarden van een parabool zijn \(-1\) en \(7\). Wat is haar symmetrieas?",
        [r"\(x = 3\)", r"\(x = 4\)", r"\(x = 6\)", r"\(y = 3\)"],
        0,
        r"De symmetrieas ligt midden tussen de nulwaarden: \(\frac{-1 + 7}{2} = 3\).",
    ),
    koppel(
        r"Koppel de transformatie van \(y = x^{2}\) aan het nieuwe voorschrift.",
        [
            ["Spiegelen rond de x-as", r"\(y = -x^{2}\)"],
            ["4 eenheden naar rechts", r"\(y = (x - 4)^{2}\)"],
            ["4 eenheden naar boven", r"\(y = x^{2} + 4\)"],
            ["Verticaal uitrekken met factor 4", r"\(y = 4x^{2}\)"],
        ],
        [r"\(y = (x + 4)^{2}\)"],
        r"Een horizontale verschuiving naar rechts zie je als \(x - 4\) binnen het kwadraat.",
    ),
    mk(
        r"De parabool \(y = x^{2}\) wordt eerst gespiegeld rond de \(x\)-as en daarna \(3\) eenheden naar boven geschoven. Wat is het bereik?",
        [r"\(]-\infty, 3]\)", r"\([3, +\infty[\)", r"\(]-\infty, -3]\)", r"\(\mathbb{R}\)"],
        0,
        r"Je krijgt \(y = -x^{2} + 3\): een bergparabool met top \((0, 3)\). Hoger dan \(3\) komt ze niet.",
    ),
    keuze(
        "Bij y = a(x − p)² + q geeft a < 0 een [[*bergparabool|dalparabool|rechte]]. Hoe groter de absolute waarde van a, hoe [[*smaller|breder|lager]] de parabool.",
        "Het teken van a bepaalt de opening, de grootte bepaalt hoe steil de parabool is.",
    ),
    inv(
        r"Wat is de maximale waarde van \(f(x) = -x^{2} + 6x - 1\)?",
        "8",
        r"\(x_{\text{top}} = -\frac{6}{-2} = 3\), en \(f(3) = -9 + 18 - 1 = 8\).",
    ),
    mk(
        r"Een leerling zegt: de top van \(y = (x - 2)^{2} + 1\) is \((-2, 1)\). Wat is de fout?",
        [
            r"Het teken: de top is \((2, 1)\), want \(x - 2 = 0\) bij \(x = 2\).",
            r"De \(y\)-coördinaat moet \(-1\) zijn.",
            r"Er is geen fout.",
            r"De top van zo'n parabool ligt altijd op de \(y\)-as.",
        ],
        0,
        "Zoek de x waarvoor het kwadraat nul wordt: dat is de x van de top.",
    ),
    sorteer(
        r"Snijdt de parabool de \(x\)-as of niet?",
        ["Snijdt de x-as", "Snijdt de x-as niet"],
        [
            [r"\(y = (x - 1)^{2} + 2\)", "Snijdt de x-as niet"],
            [r"\(y = -(x + 3)^{2} + 1\)", "Snijdt de x-as"],
            [r"\(y = 2(x - 5)^{2} - 8\)", "Snijdt de x-as"],
            [r"\(y = -x^{2} - 4\)", "Snijdt de x-as niet"],
        ],
        "Een dalparabool met top boven de x-as en een bergparabool met top onder de x-as raken de x-as nooit.",
    ),
    volgorde(
        r"Je zet \(y = 2x^{2} - 8x + 6\) om naar de vorm \(a(x - p)^{2} + q\). Zet de stappen in de goede volgorde.",
        [
            r"\(x_{\text{top}} = -\frac{b}{2a} = 2\) berekenen",
            r"\(y_{\text{top}} = 2 \cdot 4 - 16 + 6 = -2\) berekenen",
            r"\(a = 2\) behouden",
            r"\(y = 2(x - 2)^{2} - 2\) opschrijven",
        ],
        "Eerst de top, dan het voorschrift. De a blijft dezelfde.",
    ),
    mk(
        r"Een parabool heeft top \((2, -8)\) en gaat door \((0, 0)\). Wat is het voorschrift?",
        [r"\(y = 2(x - 2)^{2} - 8\)", r"\(y = (x - 2)^{2} - 8\)", r"\(y = -2(x - 2)^{2} - 8\)", r"\(y = 2(x + 2)^{2} - 8\)"],
        0,
        r"\(y = a(x - 2)^{2} - 8\). In \((0, 0)\): \(4a - 8 = 0\), dus \(a = 2\).",
    ),
    tabel(
        r"Juist of fout over \(f(x) = -2(x - 3)(x + 5)\)?",
        [
            (r"De nulwaarden zijn \(3\) en \(-5\).", J),
            (r"De symmetrieas is \(x = -1\).", J),
            (r"\(f\) heeft een minimum.", F),
            (r"De grafiek snijdt de \(y\)-as in \((0, -30)\).", F),
        ],
        r"\(a = -2\): bergparabool, dus een maximum. \(f(0) = -2 \cdot (-3) \cdot 5 = 30\).",
    ),
    sleep(
        "Bij een tweedegraadsfunctie is de grafiek een [[parabool]]. De verticale rechte door de top heet de [[symmetrieas]].",
        ["asymptoot", "raaklijn"],
        "Een parabool is symmetrisch rond die rechte.",
    ),
    mk(
        r"Een boer zet met \(40\) meter hek een rechthoekige weide af tegen een muur (drie zijden hek). Met breedte \(x\) is de oppervlakte \(A(x) = x(40 - 2x)\). Welke breedte geeft de grootste weide?",
        [r"\(10\) m", r"\(20\) m", r"\(13{,}3\) m", r"\(5\) m"],
        0,
        r"\(A(x) = -2x^{2} + 40x\) is een bergparabool. De top ligt bij \(x = -\frac{40}{-4} = 10\).",
    ),
    inv(
        r"Bij dezelfde weide, \(A(x) = x(40 - 2x)\): hoeveel m² is de grootste oppervlakte?",
        "200",
        r"\(A(10) = 10 \cdot 20 = 200\) m².",
    ),
    mk(
        r"Een kogel volgt de baan \(h(x) = -0{,}05x^{2} + 2x + 1{,}5\) (meter). Hoe hoog komt hij maximaal?",
        [r"\(21{,}5\) m", r"\(20\) m", r"\(40\) m", r"\(1{,}5\) m"],
        0,
        r"\(x_{\text{top}} = -\frac{2}{-0{,}1} = 20\). \(h(20) = -20 + 40 + 1{,}5 = 21{,}5\) m.",
    ),
    mk(
        r"Welke parabool heeft dezelfde vorm als \(y = 3x^{2}\), maar met top \((-1, 6)\)?",
        [r"\(y = 3(x + 1)^{2} + 6\)", r"\(y = 3(x - 1)^{2} + 6\)", r"\(y = 3(x + 1)^{2} - 6\)", r"\(y = -3(x + 1)^{2} + 6\)"],
        0,
        r"Dezelfde vorm betekent dezelfde \(a\). De top \((-1, 6)\) geeft \((x + 1)\) en \(+6\).",
    ),
    mk(
        r"Het snijpunt van \(y = ax^{2} + bx + c\) met de \(y\)-as is altijd ...",
        [r"\((0, c)\)", r"\((c, 0)\)", r"\((0, a)\)", r"\(\left(-\frac{b}{2a}, 0\right)\)"],
        0,
        r"Vul \(x = 0\) in: \(y = c\).",
    ),
    open_(
        r"Leg uit waarom \(y = (x - 3)^{2}\) maar één nulwaarde heeft, en wat dat betekent voor de grafiek.",
        r"\((x - 3)^{2} = 0\) enkel voor \(x = 3\). De top \((3, 0)\) ligt op de \(x\)-as: de parabool raakt de \(x\)-as daar, zonder ze te snijden.",
        "Kijk naar de ligging van de top.",
    ),
    casus(
        r"Een theater verkoopt \(300\) tickets aan \(20\) euro. Voor elke euro prijsverlaging komen er \(20\) toeschouwers bij. Bij een verlaging van \(x\) euro is de opbrengst \(R(x) = (20 - x)(300 + 20x)\).",
        [
            mk(
                "Wat zijn de nulwaarden van R?",
                [r"\(20\) en \(-15\)", r"\(-20\) en \(15\)", r"\(20\) en \(300\)", r"\(0\) en \(20\)"],
                0,
                r"\(20 - x = 0\) geeft \(x = 20\), \(300 + 20x = 0\) geeft \(x = -15\).",
            ),
            mk(
                "Bij welke verlaging is de opbrengst het grootst?",
                [r"\(2{,}50\) euro", r"\(5\) euro", r"\(17{,}50\) euro", r"\(0\) euro"],
                0,
                r"De top ligt midden tussen de nulwaarden: \(\frac{20 + (-15)}{2} = 2{,}5\).",
            ),
            mk(
                "Hoeveel is die grootste opbrengst?",
                [r"\(6125\) euro", r"\(6000\) euro", r"\(5250\) euro", r"\(7000\) euro"],
                0,
                r"\(R(2{,}5) = 17{,}5 \cdot 350 = 6125\) euro.",
            ),
        ],
    ),
]
