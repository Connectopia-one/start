"""Het functiebegrip en de eerstegraadsfunctie — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_functies: functie, beeld, origineel, domein, bereik,
nulwaarde, voorstellingen, de eerstegraadsfunctie met a en b, stijgen en
dalen, recht evenredig verband. Met twee zelfgetekende prenten: vier kleine
grafieken en vier rechten in een assenstelsel."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, s_lijn, pix_zone, venster, px, py

VG = "functie-of-niet"
PANELEN = [("A", (60, 70)), ("B", (530, 70)), ("C", (60, 360)), ("D", (530, 360))]
PB, PH = 410, 260


def _kromme(punten, kleur="#3b6fa0"):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in punten)
    return f'<polyline points="{p}" fill="none" stroke="{kleur}" stroke-width="5"/>'


def _vier():
    d = []
    for letter, (x0, y0) in PANELEN:
        d.append(s_vak(x0, y0, PB, PH, vul="#ffffff", rand="#b9b29c", dikte=2, rond=10))
        cx, cy = x0 + PB / 2, y0 + PH / 2
        d.append(s_lijn(x0 + 15, cy, x0 + PB - 15, cy, kleur="#24331b", dikte=2))
        d.append(s_lijn(cx, y0 + 12, cx, y0 + PH - 12, kleur="#24331b", dikte=2))
        if letter == "A":
            d.append(f'<circle cx="{cx+20}" cy="{cy-10}" r="80" fill="none" stroke="#3b6fa0" stroke-width="5"/>')
        elif letter == "B":
            d.append(_kromme([(cx + dx, cy + 90 - 0.0089 * dx * dx) for dx in range(-150, 151, 5)]))
        elif letter == "C":
            d.append(_kromme([(cx - 100 + 0.9 * (t * 12) ** 2 / 12 * 0.25, cy + t * 12) for t in [i / 4 for i in range(-36, 37)]]))
        else:
            d.append(_kromme([(x0 + 30, cy + 80), (cx - 60, cy - 40), (cx + 40, cy + 20), (x0 + PB - 30, cy - 90)]))
        d.append(f'<circle cx="{x0+30}" cy="{y0+30}" r="20" fill="#ffffff" stroke="#24331b" stroke-width="2"/>')
        d.append(s_tekst(x0 + 30, y0 + 37, letter, 20, vet=True))
    return d


def _pz(*letters):
    pos = dict(PANELEN)
    return [pix_zone(pos[l][0], pos[l][1], PB, PH) for l in letters]


G = venster("vier-rechten-pqrs", -4, 6, -4, 7)
LBL = {"p": (1.6, 4.2), "q": (-3, 4.5), "r": (4.5, 3), "s": (5.4, 0.7)}
GRAFIEKEN = [dict(naam=VG, titel="Vier grafieken", eigen=_vier),
             dict(naam=G, titel="", krommen=[(lambda x: 2 * x + 1, "blauw", "p", (-2.5, 3)), (lambda x: -0.5 * x + 3, "oranje", "q", (-4, 6)),
                                             (lambda x: 3 + 0 * x, "paars", "r", (-4, 6)), (lambda x: 0.5 * x - 2, "groen", "s", (-4, 6))],
                  labelplek=LBL)]
UV, UG = f"{VG}.svg", f"{G}.svg"


def _lz(l):
    x, y = LBL[l]
    return [pix_zone(px(G, x) - 30, py(G, y) - 56, 60, 60)]


VRAGEN = [
    klik("Klik op een grafiek die geen functie voorstelt.", UV, _pz("A", "C"),
         "Een verticale lijn snijdt de cirkel en de liggende parabool in twee punten: één x met twee beelden."),
    klik("Klik op de grafiek van een functie die een gebroken lijn is.", UV, _pz("D"),
         "Elke verticale lijn snijdt ze maar één keer, dus het is wel een functie."),
    klik("Klik op het label van de dalende rechte.", UG, _lz("q"), r"Enkel \(q\) zakt van links naar rechts: \(a < 0\)."),
    klik("Klik op het label van de rechte met richtingscoëfficiënt 2.", UG, _lz("p"),
         r"\(p\) stijgt \(2\) per stap naar rechts en gaat door \((0, 1)\)."),
    klik("Klik op het label van de rechte met nulwaarde 4.", UG, _lz("s"), r"\(s\) snijdt de \(x\)-as in \(4\): \(0{,}5 \cdot 4 - 2 = 0\)."),
    inv(r"Voor \(f(x) = -3x + 5\), wat is \(f(-2)\)?", ["11", "elf"], r"\(-3 \cdot (-2) + 5 = 6 + 5 = 11\)."),
    inv(r"Voor welke \(x\) is \(f(x) = 2x - 4\) gelijk aan \(10\)?", ["7", "zeven"], r"\(2x - 4 = 10\), dus \(x = 7\). Dat is het origineel van \(10\)."),
    mk(r"Wat is de richtingscoëfficiënt van de rechte door \((-1, 4)\) en \((3, -4)\)?",
       [r"\(-2\)", r"\(2\)", r"\(-\frac{1}{2}\)", r"\(\frac{1}{2}\)"], 0, r"\(a = \frac{-4 - 4}{3 - (-1)} = \frac{-8}{4} = -2\)."),
    mk(r"Welk voorschrift hoort bij de rechte met \(a = 4\) die de \(y\)-as snijdt in \(-3\)?",
       [r"\(f(x) = 4x - 3\)", r"\(f(x) = -3x + 4\)", r"\(f(x) = 4x + 3\)", r"\(f(x) = 3x - 4\)"], 0, r"\(a\) staat bij \(x\), \(b\) is het snijpunt met de \(y\)-as."),
    inv(r"Een rechte gaat door \((2, 5)\) en \((4, 9)\). Wat is \(b\) in \(f(x) = ax + b\)?", ["1", "een", "één"],
        r"\(a = \frac{9 - 5}{4 - 2} = 2\). Dan \(5 = 2 \cdot 2 + b\), dus \(b = 1\)."),
    tabel("Is de functie stijgend, dalend of constant?",
          [(r"\(f(x) = -x + 2\)", "dalend"), (r"\(f(x) = 0{,}1x - 100\)", "stijgend"), (r"\(f(x) = 5\)", "constant"), (r"\(f(x) = -\frac{2}{3}x\)", "dalend")],
          r"Enkel het teken van \(a\) beslist. \(b\) speelt geen rol.",
          kolommen=["stijgend", "dalend", "constant"]),
    tabel("Is dit een functie?",
          [(r"\(x\): 1, 2, 3 met \(y\): 4, 4, 4", "ja"), (r"\(x\): 1, 1, 2 met \(y\): 3, 5, 6", "nee"),
           ("elke leerling krijgt zijn geboortedatum", "ja"), ("elke datum krijgt de leerlingen die toen geboren zijn", "nee")],
          "Bij een functie krijgt elke x precies één beeld. Hetzelfde beeld voor verschillende x mag wel.",
          kolommen=["ja", "nee"]),
    mk(r"Wat is het domein van \(f(x) = \frac{1}{x - 2}\)?",
       [r"\(\mathbb{R} \setminus \{2\}\)", r"\(\mathbb{R}\)", r"\(\left[2, +\infty\right[\)", r"\(\mathbb{R} \setminus \{-2\}\)"], 0,
       r"De noemer mag niet nul zijn: \(x \neq 2\)."),
    inv(r"Wat is het kleinste getal in het domein van \(f(x) = \sqrt{x + 3}\)?", ["-3", "min 3", "min drie"],
        r"Onder de wortel mag niets negatiefs staan: \(x + 3 \geq 0\), dus \(x \geq -3\)."),
    casus("Een taxirit kost \\(3\\) euro instap plus \\(1{,}80\\) euro per kilometer.", [
        mk("Welk voorschrift geeft de prijs voor x km?",
           [r"\(k(x) = 1{,}8x + 3\)", r"\(k(x) = 3x + 1{,}8\)", r"\(k(x) = 4{,}8x\)", r"\(k(x) = 1{,}8x + 3x\)"], 0, "Per km 1,80 euro, en één keer 3 euro."),
        inv("Wat kost een rit van 10 km, in euro?", ["21"], r"\(1{,}8 \cdot 10 + 3 = 21\)."),
        inv("Hoeveel km rijd je voor 39 euro?", ["20", "twintig"], r"\(1{,}8x + 3 = 39\), dus \(x = 20\)."),
        keuze("Het getal 3 is op de grafiek het [[*snijpunt met de y-as|nulpunt|hellingsgetal]].", r"\(k(0) = 3\): je betaalt al bij nul km."),
    ]),
    sorteer("Recht evenredig of niet?", ["recht evenredig", "niet recht evenredig"],
            [(r"\(f(x) = 4x\)", "recht evenredig"), (r"\(f(x) = 4x + 1\)", "niet recht evenredig"), ("de prijs van appels aan 2 euro per kg", "recht evenredig"),
             ("een taxiprijs met een instapprijs", "niet recht evenredig"), ("de omtrek van een vierkant en zijn zijde", "recht evenredig")],
            r"Recht evenredig: \(b = 0\), de grafiek gaat door de oorsprong."),
    keuze(r"Schuif je de rechte \(y = 2x + 1\) drie eenheden naar boven, dan verandert [[*enkel b|enkel a|a en b]].", "De helling blijft gelijk."),
    sleep(r"Bij \(f(x) = -\frac{1}{2}x + 3\) is de functie [[dalend]] en snijdt de grafiek de \(y\)-as in [[\(3\)]]. De nulwaarde is [[\(6\)]].",
          ["stijgend", r"\(-6\)"], r"\(-\frac{1}{2}x + 3 = 0\) geeft \(x = 6\)."),
    inv(r"\(f(x) = ax + 5\) heeft nulwaarde \(2\). Wat is \(a\)?", ["-2,5", "-2.5", "min 2,5"], r"\(2a + 5 = 0\), dus \(a = -2{,}5\)."),
    mk(r"Hoe liggen de rechten \(y = 3x - 1\) en \(y = 3x + 4\) ten opzichte van elkaar?",
       ["evenwijdig", r"snijdend in \((0, 3)\)", "samenvallend", "loodrecht op elkaar"], 0, r"Dezelfde \(a\), een andere \(b\)."),
    tabel("Klopt dit over functies?",
          [("Elke rechte is de grafiek van een functie.", F), (r"Het bereik van \(f(x) = x^{2}\) is \(\left[0, +\infty\right[\).", J),
           ("Een functie heeft altijd minstens één nulwaarde.", F), (r"Bij \(f(x) = ax + b\) met \(a \neq 0\) is er precies één nulwaarde.", J)],
          r"Een verticale rechte is geen functie. \(f(x) = 5\) heeft geen nulwaarde.",
          kolommen=["Juist", "Fout"]),
    inv(r"Een tabel geeft \(x\): 0, 1, 2, 3 en \(f(x)\): 5, 8, 11, 14. Wat is \(f(10)\)?", ["35"],
        r"Per stap komt er \(3\) bij en \(f(0) = 5\): \(f(x) = 3x + 5\), dus \(f(10) = 35\)."),
    open_(r"Leg uit hoe je zonder rekenen ziet of \(f(x) = -0{,}5x + 2\) stijgt of daalt, en waar de grafiek de \(y\)-as snijdt. Bereken ook de nulwaarde.",
          r"\(a = -0{,}5 < 0\), dus dalend. \(b = 2\), dus de grafiek snijdt de \(y\)-as in \((0, 2)\). Nulwaarde: \(-0{,}5x + 2 = 0\), dus \(x = 4\)."),
    mk(r"Voor \(f(x) = x^{2} - 4\): welke \(x\)-waarden hebben beeld \(0\)?",
       [r"\(2\) en \(-2\)", r"enkel \(2\)", r"geen enkele \(x\)-waarde", r"\(4\) en \(-4\)"], 0, r"\(x^{2} = 4\): twee originelen met hetzelfde beeld."),
    inv(r"Een recht evenredig verband gaat door \((4, 6)\). Wat is \(f(10)\)?", ["15", "vijftien"], r"\(a = \frac{6}{4} = 1{,}5\), dus \(f(10) = 15\)."),
    keuze("Een rechte met a = 0 is [[*horizontaal|verticaal|stijgend]].", r"\(f(x) = b\): elk beeld is hetzelfde."),
    inv(r"Wat is de nulwaarde van \(f(x) = 2x + 1\)?", ["-0,5", "-0.5", "min 0,5"], r"\(2x + 1 = 0\) geeft \(x = -\frac{1}{2}\)."),
]
