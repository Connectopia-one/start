"""Stelsels van twee vergelijkingen — pittig (🚀 Boost doorstroom, wiskunde basis).

Strikt binnen wb_stelsels: combinatie-, substitutie- en
gelijkstellingsmethode, bepaalde, strijdige en onbepaalde stelsels, de
grafische betekenis en vraagstukken. Met twee zelfgetekende prenten: vier
kleine grafieken en een grafiek met twee rechten en vier punten."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prentmaat import s_vak, s_tekst, s_lijn, pix_zone, venster, punt_zone

VK = "vier-stelsels-grafisch"
PANELEN = [("A", (60, 70), [(-0.5, 3.5, "#3b6fa0"), (1.2, -1, "#b5651d")]),
           ("B", (530, 70), [(0.8, 1.5, "#3b6fa0"), (0.8, -1.2, "#b5651d")]),
           ("C", (60, 360), [(-0.7, 2.5, "#3b6fa0"), (-0.7, 2.5, "#b5651d")]),
           ("D", (530, 360), [(1, 0, "#3b6fa0"), (-1, 1, "#b5651d")])]
PB, PH = 410, 260


def _vier():
    d = []
    for letter, (x0, y0), lijnen in PANELEN:
        d.append(s_vak(x0, y0, PB, PH, vul="#ffffff", rand="#b9b29c", dikte=2, rond=10))
        cx, cy, e = x0 + PB / 2, y0 + PH / 2, 40          # oorsprong en eenheid
        d.append(s_lijn(x0 + 15, cy, x0 + PB - 15, cy, kleur="#24331b", dikte=2))
        d.append(s_lijn(cx, y0 + 12, cx, y0 + PH - 12, kleur="#24331b", dikte=2))
        for i, (a, b, kleur) in enumerate(lijnen):
            xs = [-4.5, 4.5]
            pts = [(cx + x * e, cy - (a * x + b) * e) for x in xs]
            stip = ' stroke-dasharray="14 10"' if i == 1 and lijnen[0][:2] == lijnen[1][:2] else ""
            d.append(f'<line x1="{pts[0][0]:.1f}" y1="{pts[0][1]:.1f}" x2="{pts[1][0]:.1f}" y2="{pts[1][1]:.1f}" stroke="{kleur}" stroke-width="5" clip-path="url(#p{letter})"{stip}/>')
        d.insert(0, f'<defs><clipPath id="p{letter}"><rect x="{x0}" y="{y0}" width="{PB}" height="{PH}"/></clipPath></defs>')
        d.append(f'<circle cx="{x0+30}" cy="{y0+30}" r="20" fill="#ffffff" stroke="#24331b" stroke-width="2"/>')
        d.append(s_tekst(x0 + 30, y0 + 37, letter, 20, vet=True))
    return d


def _pz(*letters):
    pos = {l: p for l, p, _ in PANELEN}
    return [pix_zone(pos[l][0], pos[l][1], PB, PH) for l in letters]


G = venster("stelsel-twee-rechten", -2, 6, -3, 7)
GRAFIEKEN = [dict(naam=VK, titel="Vier stelsels, telkens twee rechten (bij C liggen ze op elkaar)", eigen=_vier),
             dict(naam=G, titel="", krommen=[(lambda x: 2 * x - 1, "blauw", "", (-2, 6)), (lambda x: -x + 5, "oranje", "", (-2, 6))],
                  punten=[(0, -1, "P", True), (4, 1, "Q"), (2, 3, "S"), (1, 1, "T", True)])]
UV, UG = f"{VK}.svg", f"{G}.svg"
SG = r"Op de grafiek staan \(y = 2x - 1\) (blauw) en \(y = -x + 5\) (oranje). "

VRAGEN = [
    klik("Klik op de grafiek van een strijdig stelsel.", UV, _pz("B"), "Twee evenwijdige rechten snijden nooit: geen oplossing."),
    klik("Klik op de grafiek van een onbepaald stelsel.", UV, _pz("C"), "Twee samenvallende rechten hebben alle punten gemeen."),
    klik("Klik op de grafiek van een bepaald stelsel.", UV, _pz("A", "D"), "Twee snijdende rechten: precies één snijpunt."),
    klik(SG + "Klik op het punt dat de oplossing van het stelsel is.", UG, [punt_zone(G, 2, 3)],
         r"S\((2, 3)\) ligt op beide rechten: \(2 \cdot 2 - 1 = 3\) en \(-2 + 5 = 3\)."),
    klik(SG + r"Klik op een punt dat enkel voldoet aan \(y = -x + 5\).", UG, [punt_zone(G, 4, 1)],
         r"Q\((4, 1)\): \(-4 + 5 = 1\), maar \(2 \cdot 4 - 1 = 7\)."),
    mk(r"Los op: \(\begin{cases} 3x + 2y = 16 \\ x - 2y = 0 \end{cases}\)",
       [r"\((4, 2)\)", r"\((2, 4)\)", r"\((4, -2)\)", r"\((16, 0)\)"], 0,
       r"Optellen: \(4x = 16\), dus \(x = 4\). Dan \(4 - 2y = 0\) en \(y = 2\)."),
    mk(r"Los op met substitutie: \(\begin{cases} x = 2y + 1 \\ 3x - 4y = 7 \end{cases}\)",
       [r"\((5, 2)\)", r"\((2, 5)\)", r"\((3, 1)\)", r"\((-1, -1)\)"], 0,
       r"\(3(2y + 1) - 4y = 7\) geeft \(2y = 4\), dus \(y = 2\) en \(x = 5\)."),
    tabel("Wat voor stelsel is dit?",
          [(r"\(\begin{cases} y = 2x + 1 \\ y = 2x - 3 \end{cases}\)", "strijdig"), (r"\(\begin{cases} y = -x + 4 \\ y = x \end{cases}\)", "bepaald"),
           (r"\(\begin{cases} 2x - y = 3 \\ 4x - 2y = 6 \end{cases}\)", "onbepaald"), (r"\(\begin{cases} x + 2y = 1 \\ 2x + 4y = 5 \end{cases}\)", "strijdig")],
          "Is de tweede vergelijking een veelvoud van de eerste, dan is het onbepaald. Klopt dat enkel links, dan is het strijdig.",
          kolommen=["bepaald", "strijdig", "onbepaald"]),
    keuze(r"Bij \(\begin{cases} 4x + 3y = 10 \\ 2x + 5y = 12 \end{cases}\) vermenigvuldig je best de tweede vergelijking met [[*2|3|5]] en trek je daarna af.",
          r"Dan staat er twee keer \(4x\), en valt \(x\) weg."),
    mk(r"Welk koppel voldoet aan \(x + 2y = 8\), maar niet aan \(x - y = 2\)?",
       [r"\((2, 3)\)", r"\((4, 2)\)", r"\((6, 4)\)", r"\((-2, 6)\)"], 0,
       r"\(2 + 6 = 8\), maar \(2 - 3 = -1\). \((4, 2)\) voldoet aan beide, \((6, 4)\) enkel aan de tweede."),
    casus("Een theater verkoopt kaartjes van \\(12\\) euro voor volwassenen en \\(8\\) euro voor kinderen. Op een avond zijn er \\(50\\) kaartjes verkocht, samen voor \\(520\\) euro.", [
        mk("Welk stelsel hoort bij dit verhaal?",
           [r"\(\begin{cases} v + k = 50 \\ 12v + 8k = 520 \end{cases}\)", r"\(\begin{cases} v + k = 520 \\ 12v + 8k = 50 \end{cases}\)",
            r"\(\begin{cases} v + k = 50 \\ 20v = 520 \end{cases}\)", r"\(\begin{cases} v + k = 50 \\ 12v + 8k = 520 + 50 \end{cases}\)" ], 0,
           "Eén vergelijking telt de kaartjes, de andere het geld."),
        inv("Hoeveel kaartjes voor volwassenen zijn er verkocht?", ["30", "dertig"], r"\(12v + 8(50 - v) = 520\) geeft \(4v = 120\), dus \(v = 30\)."),
        inv("Hoeveel kaartjes voor kinderen?", ["20", "twintig"], r"\(50 - 30 = 20\)."),
        keuze("Controle: 30 keer 12 plus 20 keer 8 geeft [[*520|500|540]] euro.", r"\(360 + 160 = 520\)."),
    ]),
    casus(r"Bekijk het stelsel \(\begin{cases} 2x + 3y = 13 \\ 2x - y = 1 \end{cases}\)", [
        keuze("Hier werkt het snelst de [[*combinatiemethode: aftrekken|gelijkstellingsmethode]].", r"Beide vergelijkingen hebben \(2x\)."),
        inv(r"Wat is \(y\)?", ["3", "drie"], r"Aftrekken: \(4y = 12\), dus \(y = 3\)."),
        inv(r"Wat is \(x\)?", ["2", "twee"], r"\(2x - 3 = 1\), dus \(x = 2\)."),
    ]),
    mk(r"De eerste vergelijking is \(y = 3x + 2\). Welke tweede vergelijking maakt het stelsel strijdig?",
       [r"\(y = 3x - 5\)", r"\(y = -3x + 2\)", r"\(y = 3x + 2\)", r"\(y = 2x + 3\)"], 0,
       r"Dezelfde \(a\), een andere \(b\): evenwijdige rechten."),
    inv(r"Voor welke waarde van \(a\) is \(\begin{cases} y = ax + 1 \\ y = 4x - 2 \end{cases}\) strijdig?", ["4", "vier"],
        r"Dezelfde richtingscoëfficiënt en een verschillende \(b\): \(a = 4\)."),
    inv("Twee getallen hebben som 50. Het ene is vier keer het andere. Wat is het kleinste?", ["10", "tien"],
        r"\(x + 4x = 50\), dus \(x = 10\)."),
    mk(r"Los op: \(\begin{cases} y = 2x + 7 \\ y = -3x - 8 \end{cases}\)",
       [r"\((-3, 1)\)", r"\((3, 13)\)", r"\((1, -3)\)", r"\((-15, -23)\)"], 0,
       r"Gelijkstellen: \(2x + 7 = -3x - 8\), dus \(5x = -15\) en \(x = -3\). Dan \(y = 1\)."),
    tabel("Klopt dit over stelsels?",
          [("Een stelsel van twee eerstegraadsvergelijkingen kan precies twee oplossingen hebben.", F),
           (r"Kom je bij het oplossen \(0 = 5\) uit, dan is het stelsel strijdig.", J),
           (r"Kom je \(0 = 0\) uit, dan is het stelsel onbepaald.", J),
           ("Twee rechten met een verschillende richtingscoëfficiënt snijden altijd.", J)],
          "Twee rechten snijden nul keer, één keer of overal.",
          kolommen=["Juist", "Fout"]),
    sleep(r"Bij \(\begin{cases} x + y = 7 \\ x - y = 1 \end{cases}\) tel je de vergelijkingen op: \(2x =\) [[\(8\)]]. Dus \(x = 4\) en \(y =\) [[\(3\)]].",
          [r"\(6\)", r"\(5\)"], r"\(4 + y = 7\) geeft \(y = 3\)."),
    volgorde("Zet de stappen van de substitutiemethode in de juiste volgorde.",
             [r"maak in één vergelijking \(y\) vrij", "vul die uitdrukking in de andere vergelijking in", r"los de vergelijking in \(x\) op", r"bereken \(y\) met de gevonden \(x\)"],
             "Zo hou je één vergelijking met één onbekende over."),
    inv(r"Een stelsel heeft als oplossing \((2, -1)\). De eerste vergelijking is \(3x + ky = 8\). Wat is \(k\)?", ["-2", "min 2", "min twee"],
        r"\(6 - k = 8\), dus \(k = -2\)."),
    keuze(r"Twee rechten met richtingscoëfficiënt \(2\) en \(-\frac{1}{2}\) vormen een [[*bepaald|strijdig|onbepaald]] stelsel.",
          "Een verschillende richtingscoëfficiënt geeft altijd één snijpunt."),
    inv("Een getal van twee cijfers: de som van de cijfers is 9 en het tientalcijfer is het dubbele van het eenheidscijfer. Welk getal?", ["63"],
        r"\(t + e = 9\) en \(t = 2e\), dus \(e = 3\) en \(t = 6\)."),
    inv("Op een boerderij lopen kippen en konijnen: samen 20 koppen en 56 poten. Hoeveel konijnen?", ["8", "acht"],
        r"\(k + c = 20\) en \(2k + 4c = 56\). Aftrekken na maal 2: \(2c = 16\)."),
    tabel(r"Is het koppel een oplossing van \(\begin{cases} 2x - y = 4 \\ x + y = 5 \end{cases}\)?",
          [(r"\((3, 2)\)", "ja"), (r"\((2, 0)\)", "nee"), (r"\((0, 5)\)", "nee"), (r"\((3, -2)\)", "nee")],
          r"Een oplossing moet in beide vergelijkingen kloppen. \((2, 0)\) klopt enkel in de eerste, \((0, 5)\) enkel in de tweede.",
          kolommen=["ja", "nee"]),
    open_("Taxi A vraagt 4 euro plus 1,50 euro per km. Taxi B vraagt 2 euro plus 2 euro per km. Stel een stelsel op en bereken vanaf hoeveel km A goedkoper is.",
          r"\(y = 4 + 1{,}5x\) en \(y = 2 + 2x\). Gelijkstellen: \(4 + 1{,}5x = 2 + 2x\), dus \(x = 4\). Bij \(4\) km kosten ze evenveel (\(10\) euro). Voor langere ritten is A goedkoper, want A heeft het laagste tarief per km."),
]
