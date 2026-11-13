"""Functies en de rechte — pittig (🚀 Boost DF)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("functies-grafiek-f", -1, 11, -3, 8)
KNOPEN = [(0, 2), (2, 6), (5, 6), (8, 0), (10, -2)]


def _f(x):
    for (x0, y0), (x1, y1) in zip(KNOPEN, KNOPEN[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return None


RECHTEN = venster("functies-twee-rechten", -2, 9, -3, 7)

GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f", krommen=[(_f, "groen", "", (0, 10))],
         punten=[(0, 2, ""), (10, -2, "")]),
    dict(naam=RECHTEN, titel="De rechten p en q",
         krommen=[(lambda x: 2 * x - 1, "blauw", "p", (-1, 4)), (lambda x: -0.5 * x + 4, "oranje", "q", (-2, 9))],
         labelplek={"p": (3.6, 6.2), "q": (8.5, -0.25)}),
]
PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen en aflezen") for g in GRAFIEKEN]

VRAGEN = [
    klik(
        "Klik op het punt van de grafiek waar f een nulwaarde heeft.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 8, 0)],
        r"De grafiek snijdt de \(x\)-as in \((8, 0)\): daar is \(f(x) = 0\).",
    ),
    klik(
        r"Klik op het punt waar \(f(x) = 4\) en de grafiek stijgt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 1, 4)],
        r"Op hoogte \(4\) snijdt de grafiek twee keer: in \((1, 4)\), waar ze stijgt, en in \((6\tfrac{2}{3}, 4)\), waar ze daalt.",
    ),
    met_prent(f"{GRAF}.svg", mk(
        "Wat zijn het domein en het bereik van f?",
        [
            r"\(\text{dom} f = [0, 10]\) en \(\text{ber} f = [-2, 6]\)",
            r"\(\text{dom} f = [-2, 6]\) en \(\text{ber} f = [0, 10]\)",
            r"\(\text{dom} f = [0, 10]\) en \(\text{ber} f = [0, 6]\)",
            r"\(\text{dom} f = [-1, 11]\) en \(\text{ber} f = [-3, 8]\)",
        ],
        0,
        r"Het domein lees je op de \(x\)-as: van \(0\) tot \(10\). Het bereik op de \(y\)-as: van \(-2\) tot \(6\). Het venster van de tekening is niet het domein.",
    )),
    met_prent(f"{GRAF}.svg", tabel(
        "Juist of fout over f?",
        [
            (r"\(f(5) = 6\)", J),
            (r"\(f(3) > f(2)\)", F),
            (r"\(f(9) < 0\)", J),
            (r"Er zijn drie \(x\)-waarden met \(f(x) = 6\).", F),
        ],
        r"Tussen \(x = 2\) en \(x = 5\) is de grafiek horizontaal, dus \(f(3) = f(2) = 6\), en niet drie maar oneindig veel \(x\)-waarden geven \(6\). Bij \(x = 9\) ligt de grafiek onder de as.",
    )),
    met_prent(f"{GRAF}.svg", inv(
        r"Hoeveel is \(f(4) - f(10)\)?",
        ["8"],
        r"\(f(4) = 6\) en \(f(10) = -2\): \(6 - (-2) = 8\).",
    )),
    klik(
        "Klik op het snijpunt van de rechte q met de x-as.",
        f"{RECHTEN}.svg",
        [punt_zone(RECHTEN, 8, 0)],
        r"\(-\tfrac{1}{2}x + 4 = 0\) geeft \(x = 8\).",
    ),
    met_prent(f"{RECHTEN}.svg", koppel(
        "Koppel elke rechte aan haar voorschrift.",
        [["p", r"\(y = 2x - 1\)"], ["q", r"\(y = -\tfrac{1}{2}x + 4\)"]],
        [r"\(y = -2x + 4\)", r"\(y = \tfrac{1}{2}x - 1\)"],
        r"p snijdt de \(y\)-as in \(-1\) en stijgt \(2\) per stap naar rechts. q snijdt de \(y\)-as in \(4\) en daalt \(1\) per \(2\) stappen.",
    )),
    met_prent(f"{RECHTEN}.svg", mk(
        "In welk punt snijden p en q elkaar?",
        [r"\((2, 3)\)", r"\((3, 2)\)", r"\((2, 5)\)", r"\((1{,}5;\ 3)\)"],
        0,
        r"\(2x - 1 = -\tfrac{1}{2}x + 4\) geeft \(2{,}5x = 5\), \(x = 2\) en \(y = 3\).",
    )),
    mk(
        r"Wat is de richtingscoëfficiënt van de rechte door \((-2, 7)\) en \((4, -2)\)?",
        [r"\(-\tfrac{3}{2}\)", r"\(-\tfrac{2}{3}\)", r"\(\tfrac{5}{2}\)", r"\(-\tfrac{9}{2}\)"],
        0,
        r"\(\dfrac{-2 - 7}{4 - (-2)} = \dfrac{-9}{6} = -\tfrac{3}{2}\). Verschil in \(y\) over verschil in \(x\), niet omgekeerd.",
    ),
    inv(
        r"Geef het voorschrift van de rechte door \((2, 1)\) en \((6, 9)\). Typ bijvoorbeeld y = 3x + 4.",
        ["y = 2x - 3", "y=2x-3", "y = 2x -3", "y=2x - 3", "f(x) = 2x - 3", "f(x)=2x-3", "2x - 3", "2x-3"],
        r"Richtingscoëfficiënt \(\tfrac{9 - 1}{6 - 2} = 2\). Dan \(1 = 2 \cdot 2 + b\), dus \(b = -3\).",
    ),
    sorteer(
        "Is het verband recht evenredig, lineair maar niet recht evenredig, of niet lineair?",
        ["recht evenredig", "lineair, niet recht evenredig", "niet lineair"],
        [
            ["de prijs van appels aan 2,50 euro per kg", "recht evenredig"],
            ["een taxirit met 4 euro opstap en 2 euro per km", "lineair, niet recht evenredig"],
            ["de oppervlakte van een vierkant en zijn zijde", "niet lineair"],
            ["de omtrek van een vierkant en zijn zijde", "recht evenredig"],
            ["het water in een bad dat leegloopt aan 8 liter per minuut, vanaf 150 liter", "lineair, niet recht evenredig"],
        ],
        "Recht evenredig: een rechte door de oorsprong. Lineair: een rechte, met een begin- of vast bedrag. De oppervlakte van een vierkant groeit met het kwadraat.",
    ),
    tabel(
        "Kan deze tabel bij een eerstegraadsfunctie horen?",
        [
            (r"\(x\): \(0, 1, 2, 3\) en \(y\): \(5, 8, 11, 14\)", J),
            (r"\(x\): \(0, 2, 4, 6\) en \(y\): \(1, 2, 3, 4\)", J),
            (r"\(x\): \(1, 2, 3, 4\) en \(y\): \(2, 4, 8, 16\)", F),
            (r"\(x\): \(0, 1, 3, 4\) en \(y\): \(10, 8, 4, 2\)", J),
        ],
        r"Bij een rechte is de verandering van \(y\) gedeeld door de verandering van \(x\) altijd dezelfde. In de derde tabel verdubbelt \(y\): de stappen worden groter. In de laatste: \(-2\) per eenheid, ook over de sprong van \(1\) naar \(3\).",
    ),
    casus(
        r"Een kaars van \(30\) cm brandt op. Na \(2\) uur is ze \(26\) cm, na \(5\) uur nog \(20\) cm. Ze brandt gelijkmatig.",
        [
            mk(
                r"Welk voorschrift geeft de lengte \(L\) na \(t\) uur?",
                [r"\(L = 30 - 2t\)", r"\(L = 30 - 4t\)", r"\(L = 26 - 2t\)", r"\(L = 2t + 30\)"],
                0,
                r"In \(3\) uur gaat er \(6\) cm af: \(2\) cm per uur. Begin bij \(30\) cm.",
            ),
            inv(
                "Na hoeveel uur is de kaars helemaal opgebrand?",
                ["15", "15 uur"],
                r"\(30 - 2t = 0\) geeft \(t = 15\) uur.",
            ),
            mk(
                "Wat is het domein van deze functie, in de context?",
                [r"\(\mathbb{R}\)", r"\(\left[0, 15\right]\)", r"\(\left[0, 30\right]\)", r"\(\left[0, +\infty\right[\)"],
                1,
                "Een negatieve tijd of een negatieve lengte heeft geen zin: de functie geldt van het aansteken tot de kaars op is.",
            ),
        ],
    ),
    keuze(
        r"Bij \(f(x) = -3x + 6\) is de richtingscoëfficiënt [[*\(-3\)|\(6\)|\(3\)]], de rechte [[*daalt|stijgt]] en snijdt ze de \(y\)-as in [[*\((0, 6)\)|\((2, 0)\)|\((0, -3)\)]].",
        r"In \(y = ax + b\) is \(a\) de richtingscoëfficiënt en \(b\) het snijpunt met de \(y\)-as. Een negatieve \(a\) betekent dalen.",
    ),
    mk(
        r"Welk verband is geen functie van \(x\)?",
        [
            "bij elke leerling (x) zijn of haar geboortedatum (y)",
            "bij elk getal (x) zijn kwadraat (y)",
            "bij elke leeftijd in jaren (x) de leerlingen van die leeftijd in een klas (y)",
            "bij elk tijdstip (x) de temperatuur op één plaats (y)",
        ],
        2,
        r"Bij een functie hoort bij elke \(x\) hoogstens één \(y\). Bij \(15\) jaar horen meerdere leerlingen.",
    ),
    tabel(
        r"Is dit de grafiek van een functie?",
        [
            ("een verticale rechte", F),
            ("een horizontale rechte", J),
            ("een cirkel", F),
            ("een dalende rechte", J),
        ],
        r"Een verticale lijn en een cirkel geven bij één \(x\) meerdere \(y\)-waarden. Een horizontale rechte geeft bij elke \(x\) dezelfde ene \(y\): dat mag.",
    ),
    mk(
        r"Een rechte is evenwijdig met \(y = -4x + 1\) en gaat door \((1, 2)\). Wat is haar voorschrift?",
        [r"\(y = -4x + 6\)", r"\(y = -4x - 2\)", r"\(y = \tfrac{1}{4}x + \tfrac{7}{4}\)", r"\(y = 4x - 2\)"],
        0,
        r"Evenwijdig: dezelfde richtingscoëfficiënt \(-4\). Dan \(2 = -4 + b\), dus \(b = 6\).",
    ),
    casus(
        r"Een drukkerij rekent \(45\) euro opstartkosten en \(0{,}30\) euro per flyer. Een tweede drukkerij rekent geen opstartkosten, maar \(0{,}75\) euro per flyer.",
        [
            mk(
                "Vanaf hoeveel flyers is de eerste drukkerij goedkoper?",
                [r"vanaf \(60\) flyers", r"vanaf \(101\) flyers", r"vanaf \(150\) flyers", r"vanaf \(46\) flyers"],
                1,
                r"\(45 + 0{,}30n = 0{,}75n\) geeft \(n = 100\): dan kosten ze evenveel. Vanaf \(101\) flyers is de eerste goedkoper.",
            ),
            sleep(
                "Bij de eerste drukkerij is de kost een [[lineair]] verband met het aantal flyers. Bij de tweede is de kost [[recht evenredig]] met het aantal flyers.",
                ["omgekeerd evenredig", "kwadratisch"],
                "Een vast bedrag erbij maakt een lineair verband dat niet door de oorsprong gaat.",
            ),
        ],
    ),
    inv(
        r"Voor \(f(x) = \tfrac{1}{2}x - 3\): voor welke \(x\) is \(f(x) = 4\)?",
        ["14"],
        r"\(\tfrac{1}{2}x - 3 = 4\) geeft \(\tfrac{1}{2}x = 7\), dus \(x = 14\).",
    ),
    mk(
        r"Wat is het domein van \(f(x) = \sqrt{x - 3}\)?",
        [r"\(\left[3, +\infty\right[\)", r"\(\left]3, +\infty\right[\)", r"\(\mathbb{R}\)", r"\(\left[0, +\infty\right[\)"],
        0,
        r"Onder een vierkantswortel mag geen negatief getal staan: \(x - 3 \geq 0\), dus \(x \geq 3\). \(\sqrt{0} = 0\) bestaat wel.",
    ),
    volgorde(
        "Zet deze rechten van de steilst dalende naar de steilst stijgende.",
        [r"\(y = -3x + 1\)", r"\(y = -x + 5\)", r"\(y = 2\)", r"\(y = \tfrac{1}{2}x - 4\)", r"\(y = 4x\)"],
        "Je kijkt enkel naar de richtingscoëfficiënt: -3, -1, 0, 1/2, 4. Het snijpunt met de y-as speelt geen rol.",
    ),
    mk(
        r"Een machine kost \(24\,000\) euro en wordt lineair afgeschreven: na \(8\) jaar is ze nog \(4000\) euro waard. Hoeveel is ze na \(3\) jaar waard?",
        [r"\(9000\) euro", r"\(16\,500\) euro", r"\(15\,000\) euro", r"\(18\,000\) euro"],
        1,
        r"Per jaar \(\tfrac{24\,000 - 4000}{8} = 2500\) euro minder. Na \(3\) jaar: \(24\,000 - 7500 = 16\,500\) euro.",
    ),
    open_(
        "Leg uit wat het verschil is tussen een lineair en een recht evenredig verband, met een voorbeeld van elk uit het dagelijks leven.",
        "Beide hebben een rechte als grafiek. Bij recht evenredig gaat die rechte door de oorsprong: twee keer zoveel kopen kost twee keer zoveel, zoals brood aan een vaste prijs per stuk. Bij lineair kan er een vast bedrag bij komen, zoals een taxi met een opstapprijs: twee keer zo ver rijden kost dan niet het dubbele.",
    ),
    mk(
        r"De rechte \(y = ax + 2\) gaat door \((4, -6)\). Hoeveel is \(a\)?",
        [r"\(-2\)", r"\(-1\)", r"\(2\)", r"\(-\tfrac{1}{2}\)"],
        0,
        r"\(-6 = 4a + 2\) geeft \(4a = -8\), dus \(a = -2\).",
    ),
    inv(
        r"Voor \(f(x) = x^{2} - 2x\): hoeveel is \(f(-3)\)?",
        ["15"],
        r"\((-3)^{2} - 2 \cdot (-3) = 9 + 6 = 15\). Haakjes rond het negatieve getal voorkomen een tekenfout.",
    ),
    mk(
        r"Een rechte heeft richtingscoëfficiënt \(3\) en snijdt de \(x\)-as in \(x = 2\). Wat is haar voorschrift?",
        [r"\(y = 3x + 2\)", r"\(y = 3x - 6\)", r"\(y = 2x + 3\)", r"\(y = 3x - 2\)"],
        1,
        r"De rechte gaat door \((2, 0)\): \(0 = 3 \cdot 2 + b\), dus \(b = -6\). Bij \(y = 3x + 2\) is \(2\) het snijpunt met de \(y\)-as.",
    ),
    keuze(
        r"Het domein van \(f(x) = \dfrac{5}{x - 2}\) is \(\mathbb{R}\) zonder [[*\(2\)|\(0\)|\(-2\)|\(5\)]], want daar zou je delen door [[*nul|twee|vijf]].",
        r"Bij \(x = 2\) wordt de noemer \(0\), en delen door nul kan niet.",
    ),
]
