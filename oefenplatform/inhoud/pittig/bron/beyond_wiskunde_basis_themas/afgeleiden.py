"""Afgeleiden: helling en raaklijn — pittig (🌍 Beyond, wiskunde basis).

Zonder rekenregels: afgeleiden komen uit een grafiek, een raaklijn of een tabel.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

F_GRAF = venster("afgeleiden-f", -3, 5.5, -6, 9, 1, 1)
R_GRAF = venster("afgeleiden-raaklijn", -1, 5, -2, 10, 1, 1)
H_GRAF = venster("afgeleiden-hellinggrafiek", -4, 5, -5, 4, 1, 1)


def _f(x):
    return x ** 3 / 3 - x ** 2 - 3 * x + 5


def _g(x):
    return x * x / 2


def _fa(x):
    return -0.5 * (x + 2) * (x - 3)


PUNTEN = {"A": -2, "B": -1, "C": 1, "D": 3, "E": 4.5}

GRAFIEKEN = [
    dict(naam=F_GRAF, titel="De grafiek van f",
         krommen=[(_f, "groen", "", (-3, 5.3))],
         punten=[(x, _f(x), n) for n, x in PUNTEN.items()]),
    dict(naam=R_GRAF, titel="De grafiek van g met de rechten r en s",
         krommen=[(_g, "groen", "g", (-1, 4.4)), (lambda x: 2 * x - 2, "blauw", "r", (-0.5, 5)), (lambda x: 3 * x - 4, "oranje", "s", (0.7, 4.6))],
         labelplek={"g": (-0.6, _g(-0.6)), "r": (4.7, 7.4), "s": (3.3, 5.9)},
         punten=[(2, 2, "P", True), (4, 8, "Q", True)]),
    dict(naam=H_GRAF, titel="De hellinggrafiek: de grafiek van f′",
         krommen=[(_fa, "paars", "f′", (-4, 5))], labelplek={"f′": (4.6, _fa(4.6))}),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over helling, raaklijn en hellinggrafiek") for g in GRAFIEKEN]


def _pf(n):
    return punt_zone(F_GRAF, PUNTEN[n], _f(PUNTEN[n]), 30)


VRAGEN = [
    klik(
        "Klik op het punt waar de grafiek van f het steilst daalt.",
        f"{F_GRAF}.svg",
        [_pf("C")],
        r"Tussen de top en het dal daalt de grafiek. In C is de daling het sterkst: de raaklijn heeft daar de meest negatieve richtingscoëfficiënt.",
    ),
    klik(
        "Klik op het punt waar f een lokaal maximum heeft en de raaklijn dus horizontaal is.",
        f"{F_GRAF}.svg",
        [_pf("B")],
        r"In B gaat de grafiek over van stijgen naar dalen. De raaklijn is daar horizontaal: \(f'\) is \(0\).",
    ),
    met_prent(f"{F_GRAF}.svg", mk(
        "Wat is het teken van het differentiequotiënt van f tussen A en E?",
        ["Positief", "Nul", "Negatief", "Dat kan je niet weten zonder voorschrift"],
        2,
        r"Het differentiequotiënt is de richtingscoëfficiënt van de snijlijn AE. E ligt lager dan A, dus die snijlijn daalt.",
    )),
    met_prent(f"{R_GRAF}.svg", mk(
        r"Wat is het differentiequotiënt van g op \([2, 4]\)?",
        [r"\(6\)", r"\(3\)", r"\(2\)", r"\(1{,}5\)"],
        1,
        r"\(\frac{g(4) - g(2)}{4 - 2} = \frac{8 - 2}{2} = 3\): de richtingscoëfficiënt van de snijlijn s door P en Q.",
    )),
    met_prent(f"{R_GRAF}.svg", mk(
        "De rechte r raakt de grafiek van g in P. Welke vergelijking heeft r?",
        [r"\(y = 3x - 4\)", r"\(y = 2x + 2\)", r"\(y = 2x\)", r"\(y = 2x - 2\)"],
        3,
        r"r gaat door \((2, 2)\) en \((0, -2)\): richtingscoëfficiënt \(\frac{2 - (-2)}{2} = 2\), snijpunt met de \(y\)-as \(-2\). Dus ook \(g'(2) = 2\).",
    )),
    met_prent(f"{R_GRAF}.svg", mk(
        "Wat gebeurt er met de rechte s als je Q over de grafiek naar P laat schuiven?",
        [
            "Ze draait en nadert de raaklijn r",
            "Ze schuift evenwijdig omhoog",
            "Ze wordt horizontaal",
            "Ze blijft dezelfde rechte",
        ],
        0,
        r"De snijlijnen door P en een punt dat steeds dichter bij P komt, naderen de raaklijn. Hun richtingscoëfficiënten naderen \(g'(2)\).",
    )),
    klik(
        "Je ziet de grafiek van f′. Klik op het punt van deze grafiek dat aangeeft waar f het snelst stijgt.",
        f"{H_GRAF}.svg",
        [punt_zone(H_GRAF, 0.5, _fa(0.5), 34)],
        r"De helling van f is het grootst waar \(f'\) het grootst is: in de top van de hellinggrafiek, bij \(x = 0{,}5\).",
    ),
    met_prent(f"{H_GRAF}.svg", mk(
        "Je ziet de grafiek van f′. Op welk interval is f stijgend?",
        [r"\(]-\infty, -2] \cup [3, +\infty[\)", r"\([0, 3]\)", r"\(]-\infty;\ 0{,}5]\)", r"\([-2, 3]\)"],
        3,
        r"f stijgt waar \(f' \geq 0\), dus waar de hellinggrafiek boven of op de \(x\)-as ligt.",
    )),
    met_prent(f"{H_GRAF}.svg", inv(
        r"Je ziet de grafiek van f′. Hoe groot is de richtingscoëfficiënt van de raaklijn aan f in \(x = 0\)?",
        "3",
        r"Die richtingscoëfficiënt is \(f'(0)\). Lees af op de hellinggrafiek: \(3\).",
    )),
    mk(
        r"Voor \(f(x) = 2^x\) bereken je het differentiequotiënt op \([1;\ 1 + h]\): voor \(h = 0{,}1\) is het \(1{,}4355\), voor \(h = 0{,}01\) is het \(1{,}3911\) en voor \(h = 0{,}001\) is het \(1{,}3868\). Wat is de beste schatting van \(f'(1)\)?",
        [r"\(1{,}4355\)", r"\(2\)", r"\(1{,}386\)", r"\(1\)"],
        2,
        r"Hoe kleiner h, hoe dichter het differentiequotiënt bij de afgeleide komt. De waarden naderen ongeveer \(1{,}386\).",
    ),
    inv(
        r"s(t) is de afgelegde weg (km) van een auto na t uur, met \(s(0) = 40\) en \(s(2) = 190\). Wat is het differentiequotiënt van s op \([0, 2]\), in km/h?",
        "75",
        r"\(\frac{190 - 40}{2 - 0} = 75\).",
    ),
    tabel(
        "Juist of fout over raaklijnen en afgeleiden?",
        [
            (r"\(f'(a)\) is de richtingscoëfficiënt van de raaklijn aan de grafiek van f in \((a, f(a))\).", J),
            ("Een snijlijn door twee punten van de grafiek is altijd ook een raaklijn.", F),
            (r"Als \(f'(a) = 0\), heeft f zeker een extremum in a.", F),
            ("Een raaklijn kan de grafiek verderop nog in een ander punt snijden.", J),
        ],
        r"Denk aan \(f(x) = x^3\): \(f'(0) = 0\), maar de functie blijft stijgen. Bij een derdegraadsfunctie snijdt een raaklijn de grafiek vaak nog ergens anders.",
    ),
    mk(
        r"Wat gebeurt er met het differentiequotiënt van f op \([a, a + h]\) als h naar 0 gaat?",
        [r"Het wordt \(0\)", r"Het nadert \(f(a)\)", r"Het wordt oneindig groot", r"Het nadert \(f'(a)\)"],
        3,
        "De afgeleide in a is precies die limiet: de gemiddelde verandering over een steeds kleiner interval wordt de verandering in het punt zelf.",
    ),
    mk(
        r"Van een functie f weet je \(f(3) = 5\) en \(f'(3) = -2\). Welke vergelijking heeft de raaklijn in \(x = 3\)?",
        [r"\(y = -2x + 5\)", r"\(y = -2x + 11\)", r"\(y = 5x - 2\)", r"\(y = -2x - 1\)"],
        1,
        r"\(y - 5 = -2(x - 3)\), dus \(y = -2x + 6 + 5\).",
    ),
    inv(
        r"De raaklijn aan de grafiek van f in \(x = 1\) heeft vergelijking \(y = 4x - 7\). Hoeveel is \(f(1)\)?",
        "-3",
        r"De raaklijn gaat door het raakpunt: \(4 \cdot 1 - 7 = -3\).",
    ),
    keuze(
        "Als f′ positief is op een interval, dan is f daar [[*stijgend|dalend|constant]]. Als f′ in a van teken wisselt van plus naar min, heeft f in a een [[*lokaal maximum|lokaal minimum|nulwaarde]].",
        "Positieve helling: de grafiek gaat omhoog. Eerst omhoog, dan omlaag: een top.",
    ),
    sorteer(
        r"Is \(f'(a)\) positief of negatief?",
        [r"\(f'(a) > 0\)", r"\(f'(a) < 0\)"],
        [
            ["De raaklijn in a daalt van links naar rechts", r"\(f'(a) < 0\)"],
            ["f is de hoeveelheid water in een vat dat op tijdstip a leegloopt", r"\(f'(a) < 0\)"],
            ["f is de temperatuur, die op tijdstip a aan het oplopen is", r"\(f'(a) > 0\)"],
            [r"De raaklijn in a heeft richtingscoëfficiënt \(0{,}5\)", r"\(f'(a) > 0\)"],
            ["f is de snelheid van een auto die op tijdstip a remt", r"\(f'(a) < 0\)"],
            ["f is de hoogte van een plant die op tijdstip a groeit", r"\(f'(a) > 0\)"],
        ],
        "De afgeleide zegt hoe snel en in welke richting de grootheid op dat moment verandert.",
    ),
    volgorde(
        "Zet de stappen om de raaklijn in x = a op te stellen in de goede volgorde.",
        [
            r"Bereken \(f(a)\)",
            r"Bepaal \(f'(a)\) met een tabel, de grafiek of ICT",
            r"Vul in: \(y - f(a) = f'(a)(x - a)\)",
            r"Werk uit tot de vorm \(y = mx + q\)",
        ],
        "Je hebt een punt en een richtingscoëfficiënt nodig, daarna de vergelijking van een rechte door een punt.",
    ),
    koppel(
        "Koppel het begrip aan zijn betekenis.",
        [
            ["Differentiequotiënt", "De gemiddelde verandering over een interval"],
            ["Afgeleide in a", "De ogenblikkelijke verandering in a"],
            ["Raaklijn in a", "De rechte door (a, f(a)) met dezelfde helling als de grafiek"],
            ["Hellinggrafiek", "De grafiek van f′"],
        ],
        ["De grafiek van f, gespiegeld om de x-as"],
        "Van gemiddeld (over een interval) naar ogenblikkelijk (in één punt).",
    ),
    sleep(
        "Als s(t) de afgelegde weg in km is na t uur, dan is s′(t) de [[snelheid]] in [[km/h]]. Het differentiequotiënt van s op [1, 3] is de [[gemiddelde]] snelheid tussen uur 1 en uur 3.",
        ["versnelling", "km", "grootste"],
        "Weg gedeeld door tijd geeft snelheid. Over een interval is die gemiddeld, in één punt ogenblikkelijk.",
    ),
    mk(
        r"f is een bergparabool met top \((2, 5)\). Hoe ziet de hellinggrafiek eruit?",
        [r"Een stijgende rechte door \((2, 0)\)", r"Een parabool met top \((2, 5)\)", r"Een dalende rechte door \((2, 0)\)", r"De horizontale rechte \(y = 5\)"],
        2,
        r"Links van de top stijgt f (\(f' > 0\)), rechts daalt f (\(f' < 0\)), in de top is \(f' = 0\). De helling neemt gelijkmatig af.",
    ),
    mk(
        r"Je rekentoestel geeft bij \(\frac{dy}{dx}\) in \(x = 1{,}5\) de waarde \(-0{,}75\). Wat betekent dat?",
        [
            r"Dat \(f(1{,}5) = -0{,}75\)",
            r"Dat de raaklijn in \(x = 1{,}5\) richtingscoëfficiënt \(-0{,}75\) heeft",
            r"Dat f van \(0\) tot \(1{,}5\) met \(0{,}75\) daalt",
            r"Dat f in \(x = 1{,}5\) een minimum heeft",
        ],
        1,
        r"\(\frac{dy}{dx}\) is de afgeleide: de helling van de grafiek in dat punt.",
    ),
    tabel(
        "Juist of fout over de hellinggrafiek?",
        [
            ("Bij een constante functie valt de hellinggrafiek samen met de x-as.", J),
            ("Bij een eerstegraadsfunctie is de hellinggrafiek een horizontale rechte.", J),
            ("Een lokaal maximum van f is ook een lokaal maximum van f′.", F),
            ("Waar f′ negatief is, ligt de grafiek van f onder de x-as.", F),
        ],
        "Een rechte heeft overal dezelfde helling. f′ zegt iets over de helling van f, niet over de hoogte van f.",
    ),
    open_(
        "Leg uit waarom je de raaklijn in een punt P kan zien als de limiet van snijlijnen.",
        r"Neem een tweede punt Q op de grafiek en teken de snijlijn PQ. Schuif Q steeds dichter naar P. De snijlijnen draaien en naderen één rechte: de raaklijn. Hun richtingscoëfficiënten (differentiequotiënten) naderen de afgeleide in P.",
        "Snijlijn: twee punten. Raaklijn: wat overblijft als het tweede punt samenvalt met het eerste.",
    ),
    mk(
        r"Het differentiequotiënt van f op \([1, 4]\) is \(0\). Wat weet je zeker?",
        [r"\(f(1) = f(4)\)", r"f is constant op \([1, 4]\)", r"\(f'(x) = 0\) voor elke x in \([1, 4]\)", r"f heeft een nulwaarde in \([1, 4]\)"],
        0,
        r"\(\frac{f(4) - f(1)}{3} = 0\) betekent enkel dat begin- en eindwaarde gelijk zijn. Daartussen kan f stijgen en dalen.",
    ),
    mk(
        "Om 8 uur is het 12 °C, om 14 uur 21 °C. Wat is de gemiddelde temperatuursverandering?",
        [r"\(9\) °C per uur", r"\(1{,}5\) °C per uur", r"\(0{,}67\) °C per uur", r"\(3\) °C per uur"],
        1,
        r"\(\frac{21 - 12}{14 - 8} = \frac{9}{6} = 1{,}5\).",
    ),
    mk(
        r"Voor een functie f geldt \(f'(x) > 0\) voor elke reële x. Hoeveel nulwaarden heeft f hoogstens?",
        [r"Geen", r"Twee", r"Eén", r"Oneindig veel"],
        2,
        r"Een functie die overal stijgt, kan de \(x\)-as maar één keer kruisen. Ze kan er ook helemaal boven of onder blijven.",
    ),
    casus(
        r"Een ballon wordt opgeblazen. Het volume V (liter) na t seconden: \(V(2) = 3\), \(V(2{,}1) = 3{,}205\), \(V(2{,}01) = 3{,}02005\) en \(V(2{,}001) = 3{,}0020005\).",
        [
            inv(
                r"Bereken het differentiequotiënt van V op \([2;\ 2{,}1]\).",
                "2,05",
                r"\(\frac{3{,}205 - 3}{0{,}1} = 2{,}05\).",
            ),
            mk(
                r"Wat is de beste schatting voor \(V'(2)\)?",
                [r"\(2{,}05\)", r"\(3\)", r"\(1{,}5\)", r"\(2\)"],
                3,
                r"De differentiequotiënten zijn \(2{,}05\), \(2{,}005\) en \(2{,}0005\): ze naderen \(2\).",
            ),
            mk(
                r"Wat betekent \(V'(2)\) in deze context?",
                [
                    "Het volume na 2 seconden, in liter",
                    "Hoe snel het volume op t = 2 s toeneemt, in liter per seconde",
                    "De gemiddelde toename van het volume in de eerste 2 seconden",
                    "Na hoeveel seconden de ballon 2 liter groot is",
                ],
                1,
                "De afgeleide is een ogenblikkelijke verandering: liter per seconde, op dat ene moment.",
            ),
        ],
    ),
]
