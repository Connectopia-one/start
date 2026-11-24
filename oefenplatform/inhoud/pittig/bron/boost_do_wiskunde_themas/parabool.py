"""De parabool, transformaties en functiekenmerken — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("parabool-f-do", -1, 7, -5, 6)


def _f(x):
    return (x - 3) ** 2 - 4


GRAFIEKEN = [
    dict(naam=GRAF, titel="De parabool f", krommen=[(_f, "groen", "f", (-0.2, 6.2))], labelplek={"f": (6.3, 5)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="parabool met top (3, −4) en nulwaarden 1 en 5", vragen="klikvragen over top, nulwaarden en tekenverloop")]

VRAGEN = [
    klik(
        "Klik op de top van de parabool.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3, -4)],
        r"De top is het laagste punt: \((3, -4)\). Het voorschrift is \(f(x) = (x - 3)^{2} - 4\).",
    ),
    klik(
        "Klik op het snijpunt van de parabool met de y-as.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0, 5)],
        r"\(f(0) = 9 - 4 = 5\): het punt \((0, 5)\).",
    ),
    klik(
        "Klik in de strook van de x-waarden waarvoor f(x) negatief is.",
        f"{GRAF}.svg",
        [strook_zone(GRAF, 1.2, 4.8)],
        "Tussen de nulwaarden 1 en 5 ligt de parabool onder de x-as.",
    ),
    klik(
        "Klik op de grootste nulwaarde van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 5, 0)],
        r"\((x - 3)^{2} = 4\) geeft \(x - 3 = \pm 2\): \(x = 1\) of \(x = 5\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de parabool. Juist of fout?",
        [(r"De symmetrieas is \(x = 3\).", J),
         (r"Het bereik is \(\left[-4, +\infty\right[\).", J),
         (r"f stijgt op \(\left]-\infty, 3\right]\).", F),
         (r"\(f(2) = f(4)\)", J),
         (r"f heeft een maximum.", F),
         (r"\(f(x) = (x - 1)(x - 5)\)", J)],
        r"De parabool opent naar boven: dalend tot de top, dan stijgend, met een minimum. \(2\) en \(4\) liggen symmetrisch rond \(3\). \((x - 1)(x - 5) = x^{2} - 6x + 5 = (x - 3)^{2} - 4\).",
        kolommen=["Juist", "Fout"],
    )),
    koppel(
        r"Hoe ontstaat de grafiek uit die van \(y = x^{2}\)?",
        [(r"\(y = (x + 4)^{2}\)", "4 naar links schuiven"),
         (r"\(y = x^{2} + 4\)", "4 naar boven schuiven"),
         (r"\(y = -x^{2}\)", "spiegelen om de x-as"),
         (r"\(y = 4x^{2}\)", "verticaal uitrekken met factor 4"),
         (r"\(y = (x - 4)^{2}\)", "4 naar rechts schuiven")],
        ["4 naar beneden schuiven"],
        r"Wat binnen de haakjes bij \(x\) staat, schuift horizontaal en met het omgekeerde teken. Wat erbuiten staat, schuift verticaal.",
    ),
    mk(
        r"Wat is de top van \(f(x) = -2(x + 1)^{2} + 8\)?",
        [r"\((-1, 8)\)", r"\((1, 8)\)", r"\((-1, -8)\)", r"\((-2, 8)\)"],
        0,
        r"In \(a(x - p)^{2} + q\) is \(p = -1\) en \(q = 8\).",
    ),
    mk(
        r"Welke parabool heeft top \((2, -3)\) en gaat door \((0, 5)\)?",
        [r"\(y = 2(x - 2)^{2} - 3\)", r"\(y = (x - 2)^{2} - 3\)", r"\(y = 2(x + 2)^{2} - 3\)", r"\(y = -2(x - 2)^{2} - 3\)"],
        0,
        r"\(y = a(x - 2)^{2} - 3\). Invullen in \((0, 5)\): \(5 = 4a - 3\), dus \(a = 2\).",
    ),
    tabel(
        "Hoeveel nulwaarden heeft de functie?",
        [(r"\(f(x) = (x - 3)^{2} + 1\)", "geen"), (r"\(f(x) = -(x - 3)^{2} + 1\)", "twee"), (r"\(f(x) = 2(x + 5)^{2}\)", "één"), (r"\(f(x) = x^{2} - 7\)", "twee"), (r"\(f(x) = -x^{2} - 2\)", "geen")],
        "Kijk naar de top en de opening. Top boven de x-as en opening naar boven: geen. Top op de x-as: één. Top boven de x-as en opening naar beneden: twee.",
        kolommen=["geen", "één", "twee"],
    ),
    inv(
        r"Een parabool gaat door \((-3, 0)\) en \((7, 0)\). Bij welke x ligt haar top?",
        ["2", "x = 2", "x=2"],
        r"De top ligt midden tussen de nulwaarden: \(\tfrac{-3 + 7}{2} = 2\).",
    ),
    casus(
        r"Een bal wordt vanaf de grond geschopt. Zijn hoogte in meter na \(t\) seconden is \(h(t) = -5(t - 2)^{2} + 20\).",
        [
            inv("Hoe hoog komt de bal maximaal, in meter?", ["20", "20 m"], "De top is (2, 20): na 2 seconden is hij 20 m hoog."),
            inv("Na hoeveel seconden komt hij terug op de grond?", ["4", "4 s"], r"\(-5(t - 2)^{2} + 20 = 0\) geeft \((t - 2)^{2} = 4\), \(t = 0\) of \(t = 4\)."),
            mk("Wat is een zinvol domein?", [r"\(\left[0, 4\right]\)", r"\(\mathbb{R}\)", r"\(\left[0, 20\right]\)", r"\(\left[-2, 2\right]\)"], 0, "Van het schot tot de landing."),
        ],
    ),
    sorteer(
        "Hoort het voorschrift bij een parabool die naar boven of naar beneden opent?",
        ["Naar boven", "Naar beneden"],
        [(r"\(y = 3 - x^{2}\)", "Naar beneden"), (r"\(y = (2 - x)^{2}\)", "Naar boven"), (r"\(y = -(x + 1)^{2} + 9\)", "Naar beneden"),
         (r"\(y = 0{,}1x^{2} - 50\)", "Naar boven"), (r"\(y = -2x(x - 4)\)", "Naar beneden"), (r"\(y = (x - 1)(x - 3)\)", "Naar boven")],
        r"Werk uit en kijk naar het teken voor \(x^{2}\). \((2 - x)^{2} = x^{2} - 4x + 4\): positief. \(-2x(x - 4) = -2x^{2} + 8x\): negatief.",
    ),
    keuze(
        r"De parabool \(f(x) = -(x - 1)^{2} + 9\) [[*stijgt|daalt]] op \(\left]-\infty, 1\right]\) en heeft een [[*maximum|minimum]] gelijk aan [[*9|1|−9]].",
        "Een parabool die naar beneden opent, stijgt tot de top en daalt daarna. De top is het hoogste punt.",
    ),
    mk(
        r"Wat is het bereik van \(f(x) = -3(x - 2)^{2} + 5\)?",
        [r"\(\left]-\infty, 5\right]\)", r"\(\left[5, +\infty\right[\)", r"\(\left]-\infty, 2\right]\)", r"\(\mathbb{R}\)"],
        0,
        "De parabool opent naar beneden, dus 5 is de grootste waarde.",
    ),
    mk(
        r"Welk voorschrift hoort bij een parabool met nulwaarden \(-1\) en \(3\) die door \((0, 6)\) gaat?",
        [r"\(y = -2(x + 1)(x - 3)\)", r"\(y = 2(x + 1)(x - 3)\)", r"\(y = (x + 1)(x - 3)\)", r"\(y = -2(x - 1)(x + 3)\)"],
        0,
        r"\(y = a(x + 1)(x - 3)\). Bij \(x = 0\): \(a \cdot 1 \cdot (-3) = 6\), dus \(a = -2\).",
    ),
    tabel(
        r"Over \(f(x) = \tfrac{12}{x}\). Juist of fout?",
        [(r"\(f(3) = 4\)", J), (r"Als \(x\) verdubbelt, halveert \(f(x)\).", J), (r"\(f\) heeft nulwaarde \(0\).", F), (r"Het domein is \(\mathbb{R} \setminus \{0\}\).", J), (r"De grafiek is een parabool.", F)],
        "Dit is een omgekeerd evenredig verband. De grafiek is een hyperbool, die de assen nooit raakt.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Vier vrienden huren een chalet en betalen elk 150 euro. Hoeveel betaalt elk als ze met zes zijn, bij dezelfde totaalprijs?",
        ["100", "100 euro"],
        r"De totaalprijs is \(600\) euro. Prijs per persoon is omgekeerd evenredig: \(\tfrac{600}{6} = 100\).",
    ),
    volgorde(
        r"Zet deze waarden van \(f(x) = (x - 3)^{2} - 4\) van klein naar groot.",
        [r"\(f(3)\)", r"\(f(2)\)", r"\(f(0{,}5)\)", r"\(f(-1)\)"],
        r"Hoe verder van de top, hoe groter: \(f(3) = -4\), \(f(2) = -3\), \(f(0{,}5) = 2{,}25\), \(f(-1) = 12\).",
    ),
    sleep(
        r"In \(f(x) = a(x - p)^{2} + q\) is de top [[\((p, q)\)]]. Als \(a\) [[negatief]] is, opent de parabool naar beneden. Hoe groter \(|a|\), hoe [[smaller]] de parabool.",
        [r"\((q, p)\)", "positief", "breder"],
        "a bepaalt de opening en hoe smal of breed ze is. p en q bepalen waar de top ligt.",
    ),
    mk(
        r"Een boer heeft 40 m draad om een rechthoekige weide langs een rivier af te sluiten (de kant aan de rivier krijgt geen draad). De oppervlakte is \(A(x) = x(40 - 2x)\). Voor welke x is ze maximaal?",
        ["x = 10", "x = 20", "x = 13,3", "x = 5"],
        0,
        r"De nulwaarden zijn \(0\) en \(20\), dus de top ligt bij \(x = 10\). Dan is de oppervlakte \(10 \cdot 20 = 200\) m\(^{2}\).",
    ),
    inv(
        r"Wat is de kleinste waarde van \(f(x) = x^{2} - 6x + 11\)?",
        ["2"],
        r"\(x^{2} - 6x + 9 + 2 = (x - 3)^{2} + 2\). De top is \((3, 2)\).",
    ),
    tabel(
        r"Welk voorschrift past bij de parabool met top \((3, -4)\) en nulwaarden 1 en 5?",
        [(r"\(y = (x - 3)^{2} - 4\)", J), (r"\(y = x^{2} - 6x + 5\)", J), (r"\(y = (x + 3)^{2} - 4\)", F), (r"\(y = -(x - 1)(x - 5)\)", F)],
        "Dezelfde parabool kan in topvorm, standaardvorm en productvorm staan. Met een minteken ervoor zou ze naar beneden openen.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Waar snijdt de parabool \(y = (x - 2)(x + 6)\) de y-as?",
        [r"\((0, -12)\)", r"\((0, 12)\)", r"\((2, 0)\)", r"\((0, 4)\)"],
        0,
        r"\(x = 0\) invullen: \((-2) \cdot 6 = -12\).",
    ),
    inv(
        r"De parabool \(y = x^{2}\) schuift 2 naar rechts en 3 naar beneden. Wat is de y-waarde bij \(x = 0\)?",
        ["1"],
        r"Het nieuwe voorschrift is \(y = (x - 2)^{2} - 3\). Bij \(x = 0\): \(4 - 3 = 1\).",
    ),
    mk(
        r"Welke functie heeft dezelfde nulwaarden als \(f(x) = x^{2} - 4\), maar opent naar beneden?",
        [r"\(g(x) = 4 - x^{2}\)", r"\(g(x) = -x^{2} - 4\)", r"\(g(x) = x^{2} + 4\)", r"\(g(x) = -(x - 4)^{2}\)"],
        0,
        r"\(4 - x^{2} = -(x^{2} - 4)\): gespiegeld om de x-as. De nulwaarden \(-2\) en \(2\) blijven liggen.",
    ),
    tabel(
        r"Tekenverloop van \(f(x) = -(x + 2)(x - 4)\). Wat is het teken?",
        [(r"bij \(x = -5\)", "negatief"), (r"bij \(x = 0\)", "positief"), (r"bij \(x = 4\)", "nul"), (r"bij \(x = 10\)", "negatief")],
        "De parabool opent naar beneden, dus ze ligt enkel tussen de nulwaarden −2 en 4 boven de x-as.",
        kolommen=["positief", "nul", "negatief"],
    ),
    inv(
        r"De parabool \(y = a x^{2}\) gaat door het punt \((2, 12)\). Hoeveel is \(a\)?",
        ["3"],
        r"\(12 = a \cdot 4\), dus \(a = 3\).",
    ),
    keuze(
        r"De grafiek van \(y = (x + 3)^{2} - 1\) ontstaat uit \(y = x^{2}\) door 3 naar [[*links|rechts]] en 1 naar [[*beneden|boven]] te schuiven.",
        r"\(x + 3 = x - (-3)\), dus \(p = -3\): naar links.",
    ),
]
