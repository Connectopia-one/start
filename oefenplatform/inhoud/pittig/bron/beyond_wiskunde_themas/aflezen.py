"""Een functie aflezen van haar grafiek — pittig (🌍 Beyond doorstroom)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("aflezen-derdegraad-bey", -2.5, 2.5, -4, 4, 0.5, 1)
INV = venster("aflezen-inverse-bey", -2, 5, -2, 5)


def _f(x):
    return x ** 3 - 3 * x


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f", krommen=[(_f, "groen", "f", (-2.2, 2.2))], labelplek={"f": (2.2, 3.6)}),
    dict(naam=INV, titel="De grafiek van f en van haar inverse",
         krommen=[(lambda x: 2 ** x, "groen", "f", (-2, 2.3)), (lambda x: math.log2(x), "blauw", "g", (0.25, 5)), (lambda x: x, "#9a9a9a", "", (-2, 5))],
         labelplek={"f": (1.6, 4.4), "g": (4.6, 1.8)}, stippel=[]),
]
PRENTEN = [
    dict(bestand=f"{GRAF}.svg", zelf=True, wat="grafiek van x³ − 3x met maximum, minimum en buigpunt", vragen="klikvragen over extrema, buigpunt en tekenverloop"),
    dict(bestand=f"{INV}.svg", zelf=True, wat="2^x en log₂ x gespiegeld om y = x", vragen="klikvragen over de inverse functie"),
]

VRAGEN = [
    klik(
        "Klik op het lokaal maximum van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, -1, 2)],
        r"In \((-1, 2)\) gaat f van stijgen naar dalen. Het is geen absoluut maximum: rechts wordt f nog groter.",
    ),
    klik(
        "Klik op het buigpunt van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0, 0)],
        "In de oorsprong gaat de grafiek van bol (hol naar beneden) over in hol (naar boven).",
    ),
    klik(
        r"Klik in de strook van de \(x\)-waarden waar f daalt.",
        f"{GRAF}.svg",
        [strook_zone(GRAF, -0.9, 0.9)],
        r"Tussen het maximum in \(x = -1\) en het minimum in \(x = 1\) daalt de grafiek.",
    ),
    klik(
        "Klik op de grootste nulwaarde van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, math.sqrt(3), 0)],
        r"\(x^{3} - 3x = x(x^{2} - 3)\): nulwaarden \(0\) en \(\pm\sqrt{3} \approx \pm 1{,}73\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafiek. Juist of fout?",
        [("f is een oneven functie.", J),
         (r"\(f(x) > 0\) voor \(x \in \left]-\sqrt{3}, 0\right[\)", J),
         ("f heeft een absoluut minimum.", F),
         (r"\(f(x) = 1\) heeft drie oplossingen.", J),
         ("Op het interval [1, 2] is f stijgend.", J),
         (r"\(f(x) = 3\) heeft drie oplossingen.", F)],
        r"De grafiek is symmetrisch om de oorsprong. De horizontale rechte \(y = 1\) ligt tussen \(-2\) en \(2\) en snijdt drie keer; \(y = 3\) ligt boven het lokaal maximum en snijdt maar één keer.",
        kolommen=["Juist", "Fout"],
    )),
    klik(
        r"Het punt \((0, 1)\) ligt op f. Klik op het punt dat erbij hoort op de grafiek van de inverse.",
        f"{INV}.svg",
        [punt_zone(INV, 1, 0)],
        r"Bij de inverse wisselen \(x\) en \(y\): \((0, 1)\) wordt \((1, 0)\).",
    ),
    klik(
        r"Klik op het punt van g dat hoort bij het punt \((2, 4)\) van f.",
        f"{INV}.svg",
        [punt_zone(INV, 4, 2)],
        r"\(g = f^{-1} = \log_{2}\): \(\log_{2}4 = 2\), dus \((4, 2)\).",
    ),
    met_prent(f"{INV}.svg", tabel(
        "Kijk naar de twee grafieken. Juist of fout?",
        [(r"\(\text{dom}\,g = \text{ber}\,f = \left]0, +\infty\right[\)", J),
         ("g heeft een horizontale asymptoot.", F),
         ("f en g snijden elkaar op de rechte y = x.", F),
         ("De grijze rechte is de spiegelas.", J)],
        r"g heeft een verticale asymptoot \(x = 0\), zoals f een horizontale \(y = 0\) heeft. \(2^{x}\) ligt altijd boven \(y = x\), dus ze snijden niet.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        "Even, oneven of geen van beide?",
        [(r"\(f(x) = x^{4} - 2x^{2}\)", "even"), (r"\(f(x) = x^{3} + x\)", "oneven"), (r"\(f(x) = \cos x\)", "even"), (r"\(f(x) = x^{2} + x\)", "geen van beide"), (r"\(f(x) = \sin x\)", "oneven"), (r"\(f(x) = e^{x}\)", "geen van beide")],
        r"Vul \(-x\) in. Even: \(f(-x) = f(x)\). Oneven: \(f(-x) = -f(x)\).",
        kolommen=["even", "oneven", "geen van beide"],
    ),
    mk(
        r"Wat is de inverse van \(f(x) = \dfrac{3x + 2}{5}\)?",
        [r"\(f^{-1}(x) = \dfrac{5x - 2}{3}\)", r"\(f^{-1}(x) = \dfrac{5}{3x + 2}\)", r"\(f^{-1}(x) = \dfrac{5x + 2}{3}\)", r"\(f^{-1}(x) = \dfrac{3x - 2}{5}\)"],
        0,
        r"\(y = \tfrac{3x + 2}{5}\) geeft \(5y - 2 = 3x\), dus \(x = \tfrac{5y - 2}{3}\). Wissel dan de letters.",
    ),
    sorteer(
        "Is de functie inverteerbaar op het gegeven domein?",
        ["Inverteerbaar", "Niet inverteerbaar"],
        [(r"\(x^{2}\) op \(\mathbb{R}\)", "Niet inverteerbaar"), (r"\(x^{2}\) op \(\left]-\infty, 0\right]\)", "Inverteerbaar"), (r"\(x^{3}\) op \(\mathbb{R}\)", "Inverteerbaar"),
         (r"\(\sin x\) op \(\left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right]\)", "Inverteerbaar"), (r"\(\cos x\) op \(\left[0, 2\pi\right]\)", "Niet inverteerbaar"), (r"\(y = 5\) op \(\mathbb{R}\)", "Niet inverteerbaar")],
        "Een functie is inverteerbaar als elke horizontale rechte de grafiek hoogstens één keer snijdt.",
    ),
    mk(
        r"Wat is het domein van \(f(x) = \dfrac{\sqrt{x + 2}}{x - 1}\)?",
        [r"\(\left[-2, 1\right[ \cup \left]1, +\infty\right[\)", r"\(\left]-2, +\infty\right[\)", r"\(\left[-2, +\infty\right[\)", r"\(\mathbb{R} \setminus \{1\}\)"],
        0,
        r"\(x + 2 \geq 0\) en \(x \neq 1\).",
    ),
    casus(
        r"De functie \(f(x) = \dfrac{3x - 6}{x + 1}\).",
        [
            inv("Welke x-waarde hoort bij de verticale asymptoot?", ["-1", "−1"], "De noemer is nul bij x = −1, de teller niet."),
            inv("Welke y-waarde hoort bij de horizontale asymptoot?", ["3"], r"Voor grote \(|x|\) is \(f(x) \approx \tfrac{3x}{x} = 3\)."),
            mk("Wat is het nulpunt?", [r"\((2, 0)\)", r"\((0, -6)\)", r"\((-1, 0)\)", r"\((0, 2)\)"], 0, "Een nulpunt is een punt op de x-as: de teller is nul bij x = 2."),
        ],
    ),
    keuze(
        r"Voor een inverteerbare functie geldt \(\text{dom}\,f^{-1} = \) [[*\(\text{ber}\,f\)|\(\text{dom}\,f\)|\(\mathbb{R}\)]] en de grafiek van \(f^{-1}\) is het spiegelbeeld om [[*\(y = x\)|de \(y\)-as|de oorsprong]].",
        "x en y wisselen van rol, dus ook domein en bereik.",
    ),
    tabel(
        r"Een functie heeft periode \(4\) en \(f(1) = 3\), \(f(2) = -1\). Wat is de waarde?",
        [(r"\(f(5)\)", "3"), (r"\(f(-2)\)", "−1"), (r"\(f(13)\)", "3"), (r"\(f(10)\)", "−1")],
        r"Tel of trek veelvouden van \(4\) af: \(5 = 1 + 4\), \(-2 = 2 - 4\), \(13 = 1 + 12\), \(10 = 2 + 8\).",
        kolommen=["3", "−1"],
    ),
    mk(
        "Een functie stijgt op het hele domein, maar de stijging neemt af. Hoe ziet de grafiek eruit?",
        ["stijgend en bol, zoals een wortelfunctie", "stijgend en hol, zoals een exponentiële groei", "dalend en hol", "een rechte"],
        0,
        r"Afnemende stijging: de grafiek wordt minder steil, zoals \(\sqrt{x}\) of \(\ln x\).",
    ),
    koppel(
        "Verbind de beschrijving met het begrip.",
        [("punt waar hol overgaat in bol", "buigpunt"), ("grootste waarde in een omgeving", "lokaal maximum"), ("snijpunt met de x-as", "nulpunt"), ("rechte die de grafiek op oneindig nadert", "asymptoot")],
        ["periode"],
        "Een nulpunt is een punt, een nulwaarde het getal x.",
    ),
    inv(
        r"\(f(x) = x^{3} + 1\). Hoeveel is \(f^{-1}(28)\)?",
        ["3"],
        r"\(x^{3} + 1 = 28\) geeft \(x = 3\).",
    ),
    tabel(
        "Over het aflezen van grafieken: juist of fout?",
        [("Een even functie is nooit inverteerbaar op een domein dat een getal én zijn tegengestelde bevat.", J),
         ("Een oneven functie gaat door de oorsprong als 0 in het domein zit.", J),
         ("Elke strikt dalende functie is inverteerbaar.", J),
         ("Een functie kan twee verschillende horizontale asymptoten hebben.", J),
         ("Een functie kan twee verschillende waarden hebben bij dezelfde x.", F)],
        r"Even: \(f(-a) = f(a)\), dus twee x'en met dezelfde y. Oneven: \(f(0) = -f(0)\), dus \(f(0) = 0\). Bij \(\arctan\) zijn er twee horizontale asymptoten.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Wat is het bereik van \(f(x) = 2 - \sqrt{x - 1}\)?",
        [r"\(\left]-\infty, 2\right]\)", r"\(\left[2, +\infty\right[\)", r"\(\left[1, +\infty\right[\)", r"\(\mathbb{R}\)"],
        0,
        r"\(\sqrt{x - 1}\) neemt alle waarden \(\geq 0\) aan, dus \(2 - \sqrt{x - 1} \leq 2\).",
    ),
    sleep(
        r"De verticale-rechtetest controleert of een grafiek een [[functie]] is. De horizontale-rechtetest controleert of die functie [[inverteerbaar]] is.",
        ["periodiek", "even"],
        "Bij een functie hoort bij elke x hoogstens één y. Bij een inverteerbare functie hoort bij elke y hoogstens één x.",
    ),
    volgorde(
        r"Zet de stappen om de inverse van \(f(x) = 2x - 3\) te vinden in volgorde.",
        [r"schrijf \(y = 2x - 3\)", r"los op naar \(x\): \(x = \tfrac{y + 3}{2}\)", r"wissel \(x\) en \(y\)", r"noteer \(f^{-1}(x) = \tfrac{x + 3}{2}\)"],
        "Oplossen naar x en de letters wisselen geeft hetzelfde als spiegelen om y = x.",
    ),
    mk(
        r"Hoeveel is \(\arcsin\left(\tfrac{1}{2}\right)\)?",
        [r"\(\tfrac{\pi}{6}\)", r"\(\tfrac{\pi}{3}\)", r"\(\tfrac{5\pi}{6}\)", r"\(30\)"],
        0,
        r"\(\arcsin\) geeft een hoek in \(\left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right]\). \(\sin\tfrac{\pi}{6} = \tfrac{1}{2}\). \(\tfrac{5\pi}{6}\) ligt buiten dat interval.",
    ),
    inv(
        r"Een functie is even en \(f(3) = 7\). Hoeveel is \(f(-3)\)?",
        ["7"],
        r"Even: \(f(-x) = f(x)\).",
    ),
    mk(
        r"Een oneven functie heeft een lokaal minimum in \((2, -5)\). Wat weet je zeker?",
        [r"ze heeft een lokaal maximum in \((-2, 5)\)", r"ze heeft een lokaal minimum in \((-2, -5)\)", r"ze heeft een lokaal maximum in \((2, 5)\)", r"ze gaat door \((0, -5)\)"],
        0,
        "Spiegelen om de oorsprong maakt van een dal een top.",
    ),
    mk(
        r"Welke functie heeft zowel een verticale asymptoot \(x = 2\) als een horizontale asymptoot \(y = -1\)?",
        [r"\(f(x) = \dfrac{-x + 5}{x - 2}\)", r"\(f(x) = \dfrac{x + 5}{x - 2}\)", r"\(f(x) = \dfrac{-x + 5}{x + 2}\)", r"\(f(x) = \dfrac{x - 2}{-x + 5}\)"],
        0,
        r"Noemer nul bij \(x = 2\), en de verhouding van de hoogste coëfficiënten is \(\tfrac{-1}{1} = -1\).",
    ),
    inv(
        r"Hoeveel snijpunten met de \(x\)-as heeft \(f(x) = x^{3} - 3x - 3\)? Denk aan de grafiek van \(x^{3} - 3x\).",
        ["1", "één", "een"],
        r"Je schuift \(x^{3} - 3x\) drie naar beneden. Het lokaal maximum \((-1, 2)\) komt op \((-1, -1)\), onder de x-as: nog maar één snijpunt.",
    ),
    tabel(
        r"De grafiek van \(f\) gaat door \((1, 4)\), \((3, 0)\) en \((0, -2)\). Welk punt ligt zeker op de grafiek van \(f^{-1}\)?",
        [(r"\((4, 1)\)", J), (r"\((0, 3)\)", J), (r"\((-2, 0)\)", J), (r"\((1, 4)\)", F)],
        "Wissel bij elk punt de coördinaten.",
        kolommen=["Juist", "Fout"],
    ),
]
