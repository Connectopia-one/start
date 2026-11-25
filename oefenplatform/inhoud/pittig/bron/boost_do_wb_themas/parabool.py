"""De tweedegraadsfunctie en haar parabool — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_parabool: opening, top, symmetrieas, nulwaarden, snijpunt
met de y-as, topvorm en transformaties, stijgen en dalen, extremum en
tekenonderzoek. Met een zelfgetekende grafiek van vier parabolen."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import venster, punt_zone, pix_zone, px, py

G = venster("vier-parabolen-genummerd", -5, 6, -4, 8)
LBL = {"1": (5, 2), "2": (-3.6, -2.76), "3": (4.6, 7.58), "4": (-0.4, 5.12)}
GRAFIEKEN = [dict(naam=G, titel="",
                  krommen=[(lambda x: (x - 3) ** 2 - 2, "blauw", "1", (0.3, 5.8)), (lambda x: -(x + 1) ** 2 + 4, "oranje", "2", (-4.6, 2.6)),
                           (lambda x: 0.5 * x * x - 3, "paars", "3", (-4.6, 4.6)), (lambda x: 2 * (x + 2) ** 2 + 1, "groen", "4", (-4.1, 0.1))],
                  labelplek=LBL)]
U = f"{G}.svg"


def _lz(l):
    x, y = LBL[l]
    return [pix_zone(px(G, x) - 30, py(G, y) - 56, 60, 60)]


R6 = math.sqrt(6)

VRAGEN = [
    klik(r"Klik op het nummer van de parabool met voorschrift \(f(x) = (x - 3)^{2} - 2\).", U, _lz("1"),
         r"De basisparabool \(3\) naar rechts en \(2\) omlaag: top in \((3, -2)\)."),
    klik("Klik op de top van de enige parabool met een maximum.", U, [punt_zone(G, -1, 4)],
         r"Parabool 2 opent naar onder (\(a < 0\)). Haar top \((-1, 4)\) is het hoogste punt."),
    klik(r"Klik op het nummer van de parabool met \(a = 2\).", U, _lz("4"), r"\(a = 2 > 1\) maakt de parabool smaller dan de basisparabool."),
    klik(r"Klik op een nulwaarde van \(f(x) = 0{,}5x^{2} - 3\).", U, [punt_zone(G, R6, 0), punt_zone(G, -R6, 0)],
         r"\(0{,}5x^{2} = 3\) geeft \(x^{2} = 6\), dus \(x = \pm\sqrt{6} \approx \pm 2{,}45\)."),
    klik(r"Klik op de top van \(f(x) = 0{,}5x^{2} - 3\).", U, [punt_zone(G, 0, -3)], r"Geen \(x\)-term: de top ligt op de \(y\)-as, in \((0, -3)\)."),
    mk(r"Waar ligt de top van \(f(x) = 2x^{2} + 8x + 5\)?",
       [r"\((-2, -3)\)", r"\((2, -3)\)", r"\((-2, 5)\)", r"\((-2, -27)\)"], 0,
       r"\(x = \frac{-8}{4} = -2\) en \(f(-2) = 8 - 16 + 5 = -3\)."),
    inv(r"Wat is de \(x\)-waarde van de top van \(f(x) = -3x^{2} + 12x - 1\)?", ["2", "twee"], r"\(\frac{-b}{2a} = \frac{-12}{-6} = 2\)."),
    mk(r"Hoe schrijf je \(f(x) = x^{2} + 6x + 4\) in topvorm?",
       [r"\((x + 3)^{2} - 5\)", r"\((x - 3)^{2} - 5\)", r"\((x + 3)^{2} + 4\)", r"\((x + 6)^{2} - 32\)"], 0,
       r"De top ligt bij \(x = -3\), en \(f(-3) = 9 - 18 + 4 = -5\)."),
    tabel(r"Hoe verschuift dit voorschrift de basisparabool \(y = x^{2}\)?",
          [(r"\(y = (x + 5)^{2}\)", "naar links"), (r"\(y = x^{2} - 5\)", "omlaag"), (r"\(y = (x - 0{,}5)^{2}\)", "naar rechts"), (r"\(y = x^{2} + \frac{1}{2}\)", "omhoog")],
          "Binnen de haakjes werkt het omgekeerd: plus schuift naar links.",
          kolommen=["naar links", "naar rechts", "omhoog", "omlaag"]),
    inv(r"Wat is de grootste nulwaarde van \(f(x) = (x - 1)^{2} - 9\)?", ["4", "vier"], r"\((x - 1)^{2} = 9\), dus \(x - 1 = \pm 3\): \(4\) of \(-2\)."),
    mk(r"Waar is \(f(x) = -x^{2} + 2x + 3\) positief?",
       [r"\(\left]-1, 3\right[\)", r"\(\left]-\infty, -1\right[ \cup \left]3, +\infty\right[\)", r"\(\left]-3, 1\right[\)", r"\(\left[-1, 3\right]\)"], 0,
       r"Nulwaarden \(-1\) en \(3\). De parabool opent naar onder, dus ze ligt tussen de nulwaarden boven de \(x\)-as. In de nulwaarden zelf is \(f\) nul, niet positief."),
    keuze(r"Een parabool met top \((2, -5)\) die naar boven opent, heeft [[*twee|geen|één]] nulwaarden.", "De top ligt onder de x-as en de armen gaan omhoog."),
    keuze(r"Bij \(f(x) = -2(x - 1)^{2} + 3\) is \(3\) het [[*maximum|minimum]].", r"\(a < 0\): de top is het hoogste punt."),
    sorteer("Heeft deze functie een minimum of een maximum?", ["minimum", "maximum"],
            [(r"\(f(x) = 3x^{2} - 1\)", "minimum"), (r"\(f(x) = -0{,}5x^{2} + x\)", "maximum"), (r"\(f(x) = (x - 4)^{2}\)", "minimum"),
             (r"\(f(x) = -(x + 2)^{2} + 7\)", "maximum"), (r"\(f(x) = 5 - x^{2}\)", "maximum")],
            r"Enkel het teken van \(a\) telt. Bij \(5 - x^{2}\) is \(a = -1\)."),
    casus("De baan van een bal is \\(h(x) = -0{,}05x^{2} + x + 1{,}5\\). Daarin is \\(x\\) de horizontale afstand en \\(h\\) de hoogte, allebei in meter.", [
        inv("Op welke horizontale afstand is de bal het hoogst, in m?", ["10", "tien"], r"\(\frac{-1}{2 \cdot (-0{,}05)} = 10\)."),
        inv("Hoe hoog is de bal daar, in m?", ["6,5", "6.5"], r"\(-0{,}05 \cdot 100 + 10 + 1{,}5 = 6{,}5\)."),
        keuze("h(0) = 1,5 is de hoogte [[*waar de bal vertrekt|waar de bal landt|van de top]].", "Bij x = 0 is de bal nog niet vooruit gegaan."),
        mk(r"Waarom is \(a\) hier negatief?",
           ["de baan opent naar onder", "de bal vertrekt van de grond", "de bal gaat naar links", "de afstand is altijd negatief"], 0,
           "Een worp stijgt eerst en daalt dan: een parabool met een maximum."),
    ]),
    mk(r"Waar daalt \(f(x) = (x + 2)^{2} - 1\)?",
       [r"\(\left]-\infty, -2\right]\)", r"\(\left[-2, +\infty\right[\)", r"\(\left]-\infty, 2\right]\)", r"\(\left]-\infty, -2\right] \cup \left[2, +\infty\right[\)"], 0,
       r"Een dalparabool daalt links van de top, en de top ligt bij \(x = -2\)."),
    tabel("Klopt dit over parabolen?",
          [("Elke parabool heeft precies één symmetrieas.", J), ("De nulwaarden van een parabool liggen symmetrisch rond de symmetrieas.", J),
           (r"Bij \(a < 0\) is de functie links van de top dalend.", F), ("Twee parabolen met dezelfde top zijn altijd gelijk.", F)],
          r"Bij \(a < 0\) stijgt de functie tot aan de top. Met een andere \(a\) is de vorm anders, ook met dezelfde top.",
          kolommen=["Juist", "Fout"]),
    inv("Een parabool heeft de nulwaarden 1 en 7. Wat is de x-waarde van haar top?", ["4", "vier"], "De symmetrieas ligt midden tussen de nulwaarden."),
    mk("Welk voorschrift hoort bij de basisparabool, 3 naar links en 2 omlaag geschoven?",
       [r"\((x + 3)^{2} - 2\)", r"\((x - 3)^{2} - 2\)", r"\((x - 2)^{2} + 3\)", r"\((x + 3)^{2} - 2x\)"], 0, r"Naar links: \(+3\) binnen de haakjes."),
    sleep(r"Bij \(f(x) = 3(x - 2)^{2} + 1\) ligt de top in [[\((2, 1)\)]], is de parabool [[smaller]] dan de basisparabool en heeft ze [[geen]] nulwaarden.",
          [r"\((-2, 1)\)", "breder", "twee"], "De top ligt boven de x-as en de parabool opent naar boven."),
    inv(r"Van \(f(x) = x^{2} + bx + 5\) ligt de top bij \(x = 3\). Wat is \(b\)?", ["-6", "min 6", "min zes"], r"\(\frac{-b}{2} = 3\), dus \(b = -6\)."),
    koppel("Verbind elk voorschrift met de top van zijn parabool.",
           [(r"\(x^{2} - 4\)", r"\((0, -4)\)"), (r"\((x - 4)^{2}\)", r"\((4, 0)\)"), (r"\(-(x + 4)^{2}\)", r"\((-4, 0)\)"), (r"\(4 - (x - 1)^{2}\)", r"\((1, 4)\)")],
           [r"\((-4, 4)\)"], "Lees elk voorschrift als een verschuiving van de basisparabool."),
    open_(r"Onderzoek \(f(x) = x^{2} - 2x - 8\): geef de nulwaarden, de top, waar de functie stijgt en daalt, en waar ze negatief is.",
          r"\((x - 4)(x + 2) = 0\): nulwaarden \(-2\) en \(4\). Top bij \(x = 1\), \(f(1) = -9\): top \((1, -9)\), een minimum. Dalend voor \(x \leq 1\), stijgend voor \(x \geq 1\). Negatief tussen de nulwaarden: \(\left]-2, 4\right[\)."),
    mk(r"Waar snijdt \(f(x) = -2(x - 1)^{2} + 5\) de \(y\)-as?",
       [r"\((0, 3)\)", r"\((0, 5)\)", r"\((0, 7)\)", r"\((0, -2)\)"], 0, r"\(f(0) = -2 \cdot 1 + 5 = 3\)."),
    inv(r"Hoeveel nulwaarden heeft \(f(x) = -(x - 3)^{2}\)? Een getal.", ["1", "een", "één"], r"De top \((3, 0)\) ligt op de \(x\)-as."),
    tabel(r"Ligt het punt op de parabool van \(f(x) = x^{2} - 2x\)?",
          [(r"\((3, 3)\)", "ja"), (r"\((-1, 3)\)", "ja"), (r"\((1, 1)\)", "nee"), (r"\((2, 0)\)", "ja")],
          r"\(f(1) = 1 - 2 = -1\), niet \(1\). \((3, 3)\) en \((-1, 3)\) liggen symmetrisch rond \(x = 1\).",
          kolommen=["ja", "nee"]),
    keuze(r"Schuif je \(f(x) = x^{2} - 1\) vijf eenheden omhoog, dan heeft de nieuwe parabool [[*geen|twee|één]] nulwaarden.",
          r"\(x^{2} + 4\) blijft altijd boven de \(x\)-as."),
]
