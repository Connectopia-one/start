"""Stelsels en tweedegraadsvergelijkingen — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone

GRAF = venster("stelsels-drie-rechten-do", -2, 6, -3, 8)

GRAFIEKEN = [
    dict(naam=GRAF, titel="De rechten p, q en r",
         krommen=[(lambda x: x + 1, "groen", "p", (-2, 6)), (lambda x: -2 * x + 7, "blauw", "q", (-0.5, 5)), (lambda x: x - 2, "oranje", "r", (-1, 6))],
         labelplek={"p": (5.4, 7.6), "q": (-0.2, 7.4), "r": (5.5, 2.6)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="drie rechten p, q en r; p en r evenwijdig", vragen="klikvragen over stelsels grafisch oplossen")]

VRAGEN = [
    klik(
        "Klik op het punt dat de oplossing is van het stelsel met de vergelijkingen van p en q.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2, 3)],
        r"\(x + 1 = -2x + 7\) geeft \(x = 2\) en \(y = 3\). Grafisch is dat het snijpunt van p en q.",
    ),
    klik(
        "Klik op het snijpunt van q en r: de oplossing van hun stelsel.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3, 1)],
        r"\(-2x + 7 = x - 2\) geeft \(3x = 9\), \(x = 3\) en \(y = 1\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de rechten. Welk soort stelsel vormen ze?",
        [("p en q", "één oplossing"), ("p en r", "strijdig"), ("q en r", "één oplossing"), ("p en p", "onbepaald")],
        "p en r hebben dezelfde richtingscoëfficiënt 1 maar een ander snijpunt met de y-as: evenwijdig, dus geen oplossing.",
        kolommen=["één oplossing", "strijdig", "onbepaald"],
    )),
    mk(
        r"Los op: \(\left\{\begin{array}{l} 3x + 2y = 16 \\ 5x - 2y = 0 \end{array}\right.\)",
        [r"\((2, 5)\)", r"\((5, 2)\)", r"\((4, 2)\)", r"\((2, 10)\)"],
        0,
        r"Optellen: \(8x = 16\), dus \(x = 2\). Dan \(6 + 2y = 16\), \(y = 5\). Controle: \(10 - 10 = 0\).",
    ),
    inv(
        r"Los op: \(\left\{\begin{array}{l} y = 4x - 3 \\ y = x + 6 \end{array}\right.\) Wat is \(y\)?",
        ["9"],
        r"Gelijkstellen: \(4x - 3 = x + 6\), \(x = 3\), \(y = 9\).",
    ),
    sorteer(
        "Hoeveel oplossingen heeft het stelsel?",
        ["Eén", "Geen", "Oneindig veel"],
        [(r"\(y = 2x + 1\) en \(y = 2x - 4\)", "Geen"),
         (r"\(y = 2x + 1\) en \(4x - 2y = -2\)", "Oneindig veel"),
         (r"\(y = 2x + 1\) en \(y = -2x + 1\)", "Eén"),
         (r"\(x + y = 5\) en \(2x + 2y = 7\)", "Geen"),
         (r"\(x = 3\) en \(y = -1\)", "Eén")],
        r"Schrijf beide als \(y = mx + q\). Andere \(m\): één oplossing. Zelfde \(m\), andere \(q\): strijdig. Alles gelijk: onbepaald.",
    ),
    casus(
        "In een theater kost een ticket voor een volwassene 12 euro en voor een kind 7 euro. Er werden 150 tickets verkocht voor 1450 euro.",
        [
            mk("Welk stelsel past, met v volwassenen en k kinderen?",
               [r"\(v + k = 150\) en \(12v + 7k = 1450\)", r"\(v + k = 1450\) en \(12v + 7k = 150\)", r"\(12v = 7k\) en \(v + k = 150\)", r"\(v - k = 150\) en \(12v - 7k = 1450\)"], 0,
               "Eén vergelijking telt de tickets, de andere het geld."),
            inv("Hoeveel volwassenen kochten een ticket?", ["80"], r"\(k = 150 - v\): \(12v + 1050 - 7v = 1450\), \(5v = 400\), \(v = 80\)."),
            inv("Hoeveel kinderen?", ["70"], r"\(150 - 80 = 70\). Controle: \(960 + 490 = 1450\)."),
        ],
    ),
    koppel(
        "Welke methode kies je het best?",
        [(r"\(y = 3x + 1\) en \(y = -x + 5\)", "gelijkstelling"),
         (r"\(2x + 3y = 7\) en \(4x - 3y = 5\)", "combinatie"),
         (r"\(x = 2y\) en \(3x + y = 14\)", "substitutie")],
        ["discriminant"],
        "Staat y twee keer alleen, stel gelijk. Valt een onbekende weg door optellen, combineer. Staat één onbekende al alleen, vul ze in.",
    ),
    mk(
        r"Wat is de discriminant van \(2x^{2} - 3x - 5 = 0\)?",
        ["49", "−31", "−49", "31"],
        0,
        r"\(D = (-3)^{2} - 4 \cdot 2 \cdot (-5) = 9 + 40 = 49\).",
    ),
    inv(
        r"Los op: \(2x^{2} - 3x - 5 = 0\). Geef de positieve oplossing als decimaal getal.",
        ["2,5", "2.5", "5/2"],
        r"\(x = \dfrac{3 \pm 7}{4}\): \(x = 2{,}5\) of \(x = -1\).",
    ),
    tabel(
        "Hoeveel reële oplossingen heeft de vergelijking?",
        [(r"\(x^{2} + 4x + 5 = 0\)", "geen"), (r"\(x^{2} - 6x + 9 = 0\)", "één"), (r"\(x^{2} - x - 12 = 0\)", "twee"), (r"\(3x^{2} + 1 = 0\)", "geen"), (r"\(x^{2} - 2x = 0\)", "twee")],
        r"Bereken \(D\): \(16 - 20 < 0\), \(36 - 36 = 0\), \(1 + 48 > 0\). \(3x^{2} = -1\) kan niet. \(x(x - 2) = 0\) geeft \(0\) en \(2\).",
        kolommen=["geen", "één", "twee"],
    ),
    mk(
        r"Welke ontbinding is juist voor \(x^{2} - 2x - 15\)?",
        [r"\((x - 5)(x + 3)\)", r"\((x + 5)(x - 3)\)", r"\((x - 15)(x + 1)\)", r"\((x - 5)(x - 3)\)"],
        0,
        r"Zoek twee getallen met product \(-15\) en som \(-2\): \(-5\) en \(3\).",
    ),
    tabel(
        "Juist of fout?",
        [(r"\(x^{2} = 2x\) heeft als oplossingen \(0\) en \(2\).", J),
         (r"Uit \(x^{2} = 2x\) volgt door te delen door \(x\) dat \(x = 2\) de enige oplossing is.", F),
         (r"\((x - 1)^{2} = 0\) heeft één oplossing.", J),
         (r"\(x^{2} = -9\) heeft als oplossingen \(3\) en \(-3\).", F),
         (r"Als \(a\) en \(c\) een verschillend teken hebben, is \(D\) zeker positief.", J)],
        r"Delen door \(x\) mag niet als \(x = 0\) kan: zo verlies je een oplossing. Bij tegengestelde tekens is \(-4ac > 0\), dus \(D > 0\).",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "Een tuin is rechthoekig. De lengte is 4 m meer dan de breedte en de oppervlakte is 96 m².",
        [
            mk("Welke vergelijking hoort erbij als x de breedte is?", [r"\(x(x + 4) = 96\)", r"\(x + x + 4 = 96\)", r"\(2x + 2(x + 4) = 96\)", r"\(4x = 96\)"], 0, "Oppervlakte is lengte maal breedte."),
            inv("Hoe breed is de tuin, in meter?", ["8", "8 m"], r"\(x^{2} + 4x - 96 = 0\), \(D = 16 + 384 = 400\), \(x = \dfrac{-4 + 20}{2} = 8\)."),
            mk("Waarom laat je de andere oplossing vallen?", ["omdat ze negatief is en een breedte niet negatief kan zijn", "omdat ze te groot is voor een gewone tuin in de stad", "omdat de discriminant nul is en er dus maar één telt", "omdat ze geen geheel getal is en je dat niet kunt meten"], 0,
               r"De andere oplossing is \(-12\)."),
        ],
    ),
    mk(
        r"Wat is de oplossingenverzameling van \(x^{2} - 4 \geq 0\)?",
        [r"\(\left[-2, 2\right]\)", r"\(\left]-\infty, -2\right] \cup \left[2, +\infty\right[\)", r"\(\left[2, +\infty\right[\)", r"\(\left]-2, 2\right[\)"],
        1,
        r"De parabool \(y = x^{2} - 4\) ligt boven de x-as buiten de nulwaarden \(-2\) en \(2\).",
    ),
    keuze(
        r"Bij \(x^{2} + bx + 16 = 0\) is er precies één oplossing als \(b\) gelijk is aan [[*8 of −8|4 of −4|16]]. Dan is de discriminant [[*nul|negatief|positief]].",
        r"\(b^{2} - 64 = 0\) geeft \(b = \pm 8\). Dan is \(x^{2} \pm 8x + 16\) een volkomen kwadraat.",
    ),
    volgorde(
        r"Zet de stappen om \(x^{2} + 3x = 10\) op te lossen in de goede volgorde.",
        [r"herleiden op nul: \(x^{2} + 3x - 10 = 0\)", r"discriminant: \(D = 9 + 40 = 49\)", r"formule: \(x = \tfrac{-3 \pm 7}{2}\)", r"oplossingen: \(x = 2\) of \(x = -5\)", r"controle in de opgave"],
        "Eerst moet één lid nul zijn, anders klopt de formule niet.",
    ),
    sleep(
        r"Een stelsel met twee [[snijdende]] rechten heeft één oplossing. Bij twee [[evenwijdige]] rechten is het stelsel strijdig. Bij [[samenvallende]] rechten is het onbepaald.",
        ["loodrechte", "kruisende"],
        "Het aantal gemeenschappelijke punten van de rechten is het aantal oplossingen.",
    ),
    inv(
        "Het product van twee opeenvolgende positieve gehele getallen is 156. Wat is het kleinste getal?",
        ["12"],
        r"\(x(x + 1) = 156\) geeft \(x^{2} + x - 156 = 0\), \(D = 625\), \(x = \tfrac{-1 + 25}{2} = 12\).",
    ),
    mk(
        r"Voor welke waarde van \(k\) heeft \(\left\{\begin{array}{l} 2x + 3y = 5 \\ 4x + ky = 1 \end{array}\right.\) geen oplossing?",
        [r"\(k = 6\)", r"\(k = 3\)", r"\(k = 1{,}5\)", r"\(k = -6\)"],
        0,
        r"Met \(k = 6\) is de tweede vergelijking links het dubbel van de eerste, maar rechts geen \(10\): evenwijdige rechten.",
    ),
    tabel(
        r"Is het koppel een oplossing van \(\left\{\begin{array}{l} x + 2y = 7 \\ 3x - y = 7 \end{array}\right.\)?",
        [(r"\((3, 2)\)", J), (r"\((1, 3)\)", F), (r"\((7, 0)\)", F), (r"\((2, -1)\)", F)],
        r"Een koppel moet in allebei de vergelijkingen kloppen. \((1, 3)\) en \((7, 0)\) kloppen enkel in de eerste, \((2, -1)\) enkel in de tweede.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Een bal wordt opgegooid. De hoogte na \(t\) seconden is \(h = -5t^{2} + 20t\). Na hoeveel seconden valt de bal terug op de grond?",
        ["2 s", "4 s", "5 s", "20 s"],
        1,
        r"\(-5t^{2} + 20t = 0\) geeft \(-5t(t - 4) = 0\): \(t = 0\) (vertrek) of \(t = 4\).",
    ),
    inv(
        r"Los op: \(\left\{\begin{array}{l} 2x - y = 1 \\ x + 3y = 11 \end{array}\right.\) Wat is \(x\)?",
        ["2"],
        r"\(y = 2x - 1\) invullen: \(x + 6x - 3 = 11\), \(x = 2\), \(y = 3\).",
    ),
    mk(
        r"De som van twee getallen is \(20\) en hun verschil is \(6\). Wat is hun product?",
        ["91", "120", "84", "14"],
        0,
        r"\(x + y = 20\) en \(x - y = 6\) geven \(x = 13\), \(y = 7\). Het product is \(91\).",
    ),
    inv(
        r"Los op: \((x - 3)^{2} = 25\). Geef de negatieve oplossing.",
        ["-2", "−2"],
        r"\(x - 3 = 5\) of \(x - 3 = -5\): \(x = 8\) of \(x = -2\). Vergeet de negatieve wortel niet.",
    ),
    tabel(
        r"Welk getal is de discriminant?",
        [(r"\(x^{2} + x + 1\)", "−3"), (r"\(x^{2} - 4x + 1\)", "12"), (r"\(-x^{2} + 2x + 3\)", "16"), (r"\(4x^{2} - 4x + 1\)", "0")],
        r"\(D = b^{2} - 4ac\). Bij \(-x^{2} + 2x + 3\): \(4 - 4 \cdot (-1) \cdot 3 = 16\).",
        kolommen=["−3", "12", "16", "0"],
    ),
]
