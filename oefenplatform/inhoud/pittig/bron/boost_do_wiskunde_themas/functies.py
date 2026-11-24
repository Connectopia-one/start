"""Functies en de rechte — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

GRAF = venster("functies-gebroken-lijn-do", -1, 9, -4, 7)
KNOPEN = [(0, 1), (2, 5), (4, 5), (6, 1), (8, -3)]


def _f(x):
    for (x0, y0), (x1, y1) in zip(KNOPEN, KNOPEN[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return None


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f op het domein [0, 8]", krommen=[(_f, "groen", "f", (0, 8))],
         punten=[(0, 1, ""), (8, -3, "")], labelplek={"f": (1.2, 5.5)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="gebroken lijn van (0, 1) over (2, 5), (4, 5), (6, 1) naar (8, −3)", vragen="klikvragen en aflezen van kenmerken")]

VRAGEN = [
    klik(
        "Klik op de nulwaarde van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 6.5, 0)],
        r"Tussen \((6, 1)\) en \((8, -3)\) daalt f met \(2\) per eenheid. Na een halve eenheid is f nul: \(x = 6{,}5\).",
    ),
    klik(
        r"Klik op een punt van de grafiek waar \(f(x) = 3\).",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 1, 3), punt_zone(GRAF, 5, 3)],
        r"De horizontale rechte \(y = 3\) snijdt de grafiek twee keer: bij \(x = 1\) en bij \(x = 5\).",
    ),
    klik(
        "Klik op het stuk van de grafiek waar f constant is.",
        f"{GRAF}.svg",
        [vak_zone(GRAF, 2, 4, 4.4, 5.6)],
        "Tussen x = 2 en x = 4 blijft de functiewaarde 5: een horizontaal stuk.",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafiek. Juist of fout?",
        [(r"Het domein is \(\left[0, 8\right]\).", J),
         (r"Het bereik is \(\left[-3, 5\right]\).", J),
         (r"\(f(0) = 0\)", F),
         (r"f stijgt op \(\left[0, 2\right]\).", J),
         (r"\(f(7) = -2\)", F),
         (r"f is negatief op \(\left]6{,}5\,;\,8\right]\).", J)],
        r"\(f(0) = 1\): het snijpunt met de y-as. \(f(7) = -1\), halfweg tussen \(1\) en \(-3\).",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{GRAF}.svg", inv(
        "Kijk naar de grafiek. Wat is de richtingscoëfficiënt van het eerste stuk, van x = 0 tot x = 2?",
        ["2"],
        r"Van \((0, 1)\) naar \((2, 5)\): \(\dfrac{5 - 1}{2 - 0} = 2\).",
    )),
    sorteer(
        "Is dit verband een functie van x?",
        ["Functie", "Geen functie"],
        [("bij elke leerling zijn geboortedatum", "Functie"),
         ("bij elke x het getal y met y² = x", "Geen functie"),
         ("bij elk uur van de dag de temperatuur", "Functie"),
         ("de verticale rechte x = 2", "Geen functie"),
         (r"\(y = x^{2}\)", "Functie"),
         ("een cirkel met middelpunt in de oorsprong", "Geen functie")],
        r"Een functie geeft bij elke \(x\) hoogstens één \(y\). Bij \(y^{2} = 4\) horen \(y = 2\) en \(y = -2\).",
    ),
    mk(
        r"Wat is het voorschrift van de rechte door \((-2, 7)\) en \((4, -2)\)?",
        [r"\(y = -1{,}5x + 4\)", r"\(y = 1{,}5x + 10\)", r"\(y = -1{,}5x + 7\)", r"\(y = -\tfrac{2}{3}x + 4\)"],
        0,
        r"\(a = \dfrac{-2 - 7}{4 - (-2)} = -1{,}5\). Invullen in \((4, -2)\): \(-2 = -6 + b\), \(b = 4\).",
    ),
    tabel(
        "Welk soort verband hoort bij de tabel?",
        [(r"x: 1, 2, 3, 4 en y: 5, 10, 15, 20", "recht evenredig"),
         (r"x: 1, 2, 3, 4 en y: 7, 9, 11, 13", "lineair, niet recht evenredig"),
         (r"x: 1, 2, 3, 4 en y: 2, 4, 8, 16", "niet lineair"),
         (r"x: 0, 1, 2, 3 en y: 0, −3, −6, −9", "recht evenredig"),
         (r"x: 1, 2, 3, 4 en y: 12, 6, 4, 3", "niet lineair")],
        "Lineair: telkens hetzelfde verschil. Recht evenredig: bovendien is y/x altijd hetzelfde, dus de rechte gaat door de oorsprong.",
        kolommen=["recht evenredig", "lineair, niet recht evenredig", "niet lineair"],
    ),
    mk(
        r"Een rechte is evenwijdig met \(y = -3x + 1\) en gaat door \((2, 0)\). Wat is haar voorschrift?",
        [r"\(y = -3x + 6\)", r"\(y = -3x - 6\)", r"\(y = \tfrac{1}{3}x - \tfrac{2}{3}\)", r"\(y = 3x - 6\)"],
        0,
        r"Evenwijdig: dezelfde \(a = -3\). \(0 = -6 + b\), dus \(b = 6\).",
    ),
    casus(
        "Een taxirit kost een vast bedrag plus een prijs per km. Een rit van 5 km kost 13 euro, een rit van 12 km kost 26,30 euro.",
        [
            mk("Hoeveel kost één kilometer?", ["1,90 euro", "2,60 euro", "2,19 euro", "13,30 euro"], 0, r"\(\dfrac{26{,}30 - 13}{12 - 5} = \dfrac{13{,}30}{7} = 1{,}90\) euro."),
            inv("Hoeveel is het vaste bedrag, in euro?", ["3,5", "3,50", "3.5", "3.50"], r"\(13 - 5 \cdot 1{,}90 = 3{,}50\) euro."),
            mk("Is de prijs recht evenredig met de afstand?", ["nee, door het vaste bedrag gaat de rechte niet door de oorsprong", "ja, want de grafiek van de prijs is een rechte lijn", "ja, want de prijs per kilometer blijft altijd even groot", "nee, want de grafiek daalt naarmate je verder rijdt"], 0,
               "Een rit van 10 km kost niet het dubbel van een rit van 5 km."),
        ],
    ),
    keuze(
        r"Bij \(f(x) = -2x + 6\) is de grafiek [[*dalend|stijgend|horizontaal]]. Ze snijdt de y-as in [[*\((0, 6)\)|\((3, 0)\)|\((0, -2)\)]] en de x-as in [[*\((3, 0)\)|\((6, 0)\)|\((-3, 0)\)]].",
        r"De richtingscoëfficiënt is negatief. \(f(0) = 6\), en \(-2x + 6 = 0\) geeft \(x = 3\).",
    ),
    koppel(
        "Verbind het voorschrift met de beschrijving van de rechte.",
        [(r"\(y = 4\)", "horizontaal, door (0, 4)"),
         (r"\(y = 4x\)", "stijgend, door de oorsprong"),
         (r"\(y = -x + 4\)", "dalend, door (0, 4)"),
         (r"\(y = 0{,}25x - 1\)", "zacht stijgend, door (4, 0)")],
        ["verticaal, door (4, 0)"],
        r"Een verticale rechte \(x = 4\) is geen functie en heeft geen voorschrift van de vorm \(y = ax + b\).",
    ),
    mk(
        r"Wat is het domein van \(f(x) = \sqrt{x - 3}\)?",
        [r"\(\left[3, +\infty\right[\)", r"\(\left]3, +\infty\right[\)", r"\(\mathbb{R}\)", r"\(\left]-\infty, 3\right]\)"],
        0,
        r"Onder de wortel mag geen negatief getal staan: \(x - 3 \geq 0\), dus \(x \geq 3\). Bij \(x = 3\) is de wortel \(0\), dat mag.",
    ),
    inv(
        r"Voor \(f(x) = 5 - 2x\): voor welke \(x\) is \(f(x) = -9\)?",
        ["7"],
        r"\(5 - 2x = -9\) geeft \(-2x = -14\), \(x = 7\).",
    ),
    tabel(
        "Juist of fout over de rechte y = ax + b?",
        [(r"Als \(a = 0\), is de rechte horizontaal.", J),
         (r"Als \(b = 0\), gaat de rechte door de oorsprong.", J),
         (r"Hoe groter \(b\), hoe steiler de rechte.", F),
         (r"Twee rechten met \(a = 2\) en \(a = -2\) zijn evenwijdig.", F),
         (r"Als \(a < 0\), daalt de rechte van links naar rechts.", J)],
        r"Enkel \(a\) bepaalt hoe steil een rechte is; \(b\) schuift haar op of neer. Evenwijdig vraagt dezelfde \(a\).",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "Een kaars is 24 cm lang en brandt 1,5 cm per uur korter.",
        [
            mk("Welk voorschrift geeft de lengte L na t uur?", [r"\(L = 24 - 1{,}5t\)", r"\(L = 1{,}5t - 24\)", r"\(L = 24t - 1{,}5\)", r"\(L = 24 + 1{,}5t\)"], 0, "Startwaarde 24, daling 1,5 per uur."),
            inv("Na hoeveel uur is de kaars op?", ["16", "16 uur"], r"\(24 - 1{,}5t = 0\) geeft \(t = 16\)."),
            mk("Wat is een zinvol domein voor deze functie?", [r"\(\left[0, 16\right]\)", r"\(\mathbb{R}\)", r"\(\left[0, 24\right]\)", r"\(\left[-16, 16\right]\)"], 0,
               "Negatieve tijd en een negatieve lengte hebben hier geen betekenis."),
        ],
    ),
    volgorde(
        "Zet de rechten van minst steil naar meest steil.",
        [r"\(y = 0{,}5x + 8\)", r"\(y = -x\)", r"\(y = 2x - 1\)", r"\(y = -3x + 2\)"],
        r"Hoe steil een rechte is, hangt af van de grootte van \(a\), zonder teken: \(0{,}5 < 1 < 2 < 3\).",
    ),
    sleep(
        "In 'de kostprijs hangt af van het aantal stuks' is het aantal stuks de [[onafhankelijke]] variabele. Die zet je op de [[horizontale]] as.",
        ["afhankelijke", "verticale"],
        "Wat je kiest, is onafhankelijk. Wat eruit volgt, is afhankelijk en staat verticaal.",
    ),
    mk(
        "Een machine kost 45 000 euro en wordt lineair afgeschreven: na 3 jaar is ze nog 36 000 euro waard. Na hoeveel jaar is ze niets meer waard?",
        ["15 jaar", "12 jaar", "9 jaar", "18 jaar"],
        0,
        r"Ze verliest \(9000 : 3 = 3000\) euro per jaar. \(45\,000 : 3000 = 15\) jaar.",
    ),
    inv(
        r"Voor welke waarde van \(k\) gaat de rechte \(y = kx - 4\) door het punt \((2, 6)\)?",
        ["5"],
        r"\(6 = 2k - 4\) geeft \(k = 5\).",
    ),
    mk(
        r"De rechte \(y = \tfrac{1}{2}x + 3\) en de rechte \(y = -x + 9\) snijden elkaar. In welk punt?",
        [r"\((4, 5)\)", r"\((6, 3)\)", r"\((2, 7)\)", r"\((4, 6)\)"],
        0,
        r"\(\tfrac{1}{2}x + 3 = -x + 9\) geeft \(1{,}5x = 6\), \(x = 4\), \(y = 5\).",
    ),
    met_prent(f"{GRAF}.svg", mk(
        "Kijk naar de grafiek. Op welk interval daalt f?",
        [r"\(\left[4, 8\right]\)", r"\(\left[2, 8\right]\)", r"\(\left[6, 8\right]\)", r"\(\left[0, 2\right]\)"],
        0,
        "Vanaf x = 4 gaat de grafiek naar beneden tot het einde van het domein. Tussen 2 en 4 is ze constant, niet dalend.",
    )),
    inv(
        r"Voor \(g(x) = x^{2} - 3x\): hoeveel is \(g(-2)\)?",
        ["10"],
        r"\((-2)^{2} - 3 \cdot (-2) = 4 + 6 = 10\).",
    ),
    tabel(
        "Hoort het punt bij de rechte y = 3x − 5?",
        [(r"\((2, 1)\)", J), (r"\((0, 5)\)", F), (r"\((-1, -8)\)", J), (r"\((3, 3)\)", F)],
        r"Vul \(x\) in en vergelijk met \(y\): \(3 \cdot 0 - 5 = -5\), niet \(5\). \(3 \cdot 3 - 5 = 4\), niet \(3\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Wat is het bereik van \(f(x) = x^{2} + 1\) met domein \(\mathbb{R}\)?",
        [r"\(\left[1, +\infty\right[\)", r"\(\mathbb{R}\)", r"\(\left[0, +\infty\right[\)", r"\(\left]1, +\infty\right[\)"],
        0,
        r"\(x^{2}\) is minstens \(0\), dus \(f(x)\) is minstens \(1\). De waarde \(1\) wordt bereikt bij \(x = 0\).",
    ),
    inv(
        "Een duiker daalt. De druk is 1 bar aan het wateroppervlak en stijgt 1 bar per 10 m. Bij hoeveel meter diepte is de druk 3,5 bar?",
        ["25", "25 m", "25 meter"],
        r"\(p = 1 + 0{,}1d\). \(1 + 0{,}1d = 3{,}5\) geeft \(d = 25\) m.",
    ),
]
