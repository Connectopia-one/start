"""Rechten en vlakken in de ruimte — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, DONKER, GROEN

KUBUS = "ruimte-kubus-bey"
_P = {"A": (0, 0, 0), "B": (2, 0, 0), "C": (2, 2, 0), "D": (0, 2, 0), "E": (0, 0, 2), "F": (2, 0, 2), "G": (2, 2, 2), "H": (0, 2, 2)}
_RIBBEN = ["AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"]
_VERBORGEN = {"CD", "DA", "DH"}


def _xy(p):
    x, y, z = p
    return 290 + x * 170 + y * 85, 540 - z * 170 - y * 70


def _kubus():
    d = []
    for r in _RIBBEN:
        x1, y1 = _xy(_P[r[0]])
        x2, y2 = _xy(_P[r[1]])
        streep = ' stroke-dasharray="10 8"' if r in _VERBORGEN else ""
        d.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GROEN}" stroke-width="3"{streep}/>')
    verschuif = {"A": (-22, 24), "B": (18, 24), "C": (22, 10), "D": (-24, -6), "E": (-24, -6), "F": (20, 24), "G": (22, -8), "H": (-20, -12)}
    for n, p in _P.items():
        x, y = _xy(p)
        d.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{DONKER}"/>')
        dx, dy = verschuif[n]
        d.append(s_tekst(x + dx, y + dy, n, 28, vet=True))
    return d


def _punt(n):
    x, y = _xy(_P[n])
    return pix_zone(x - 32, y - 32, 64, 64)


def _ribbe(r):
    x1, y1 = _xy(_P[r[0]])
    x2, y2 = _xy(_P[r[1]])
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return pix_zone(mx - 45, my - 35, 90, 70)


GRAFIEKEN = [dict(naam=KUBUS, titel="Een kubus ABCDEFGH", eigen=_kubus)]
PRENTEN = [dict(bestand=f"{KUBUS}.svg", zelf=True, wat="kubus ABCDEFGH met verborgen ribben in stippellijn", vragen="klikvragen over onderlinge ligging van rechten en vlakken")]

VRAGEN = [
    klik(
        "Klik op het midden van de ribbe door G die evenwijdig is met AB.",
        f"{KUBUS}.svg",
        [_ribbe("GH")],
        "GH ligt recht boven DC, en DC is evenwijdig met AB.",
    ),
    klik(
        "Klik op het hoekpunt dat samen met A, C en G in één vlak ligt.",
        f"{KUBUS}.svg",
        [_punt("E")],
        "Het diagonaalvlak ACGE staat verticaal door de diagonaal AC.",
    ),
    met_prent(f"{KUBUS}.svg", tabel(
        "Kijk naar de kubus. Wat is de onderlinge ligging?",
        [("AB en CG", "kruisend"), ("AC en BD", "snijdend"), ("EH en BC", "evenwijdig"), ("EF en CD", "evenwijdig"), ("BF en DH", "evenwijdig"), ("AE en BC", "kruisend")],
        "Kruisende rechten zijn niet evenwijdig en snijden niet; ze liggen niet in één vlak.",
        kolommen=["snijdend", "evenwijdig", "kruisend"],
    )),
    met_prent(f"{KUBUS}.svg", tabel(
        "Kijk naar de kubus. Juist of fout?",
        [("De rechte AE is evenwijdig met het vlak BCGF.", J), ("De rechte BH snijdt het grondvlak ABCD.", J), ("Het vlak ABFE en het vlak DCGH zijn evenwijdig.", J), ("De rechte EG ligt in het vlak ABCD.", F)],
        "AE is evenwijdig met BF, en BF ligt in BCGF. EG ligt in het bovenvlak.",
        kolommen=["Juist", "Fout"],
    )),
    mk(
        r"De rechte \(r\) gaat door \(P(1, 2, 3)\) met richtingsvector \(\vec{v}(2, -1, 1)\). Welk punt ligt op \(r\)?",
        [r"\((5, 0, 5)\)", r"\((3, 1, 3)\)", r"\((2, -1, 1)\)", r"\((5, 0, 4)\)"],
        0,
        r"Met \(t = 2\): \((1 + 4,\ 2 - 2,\ 3 + 2)\).",
    ),
    mk(
        r"Wat is de vergelijking van het vlak door \((1, 0, 2)\) met normaalvector \(\vec{n}(2, -1, 3)\)?",
        [r"\(2x - y + 3z - 8 = 0\)", r"\(x + 2z - 8 = 0\)", r"\(2x - y + 3z = 0\)", r"\(2x - y + 3z + 8 = 0\)"],
        0,
        r"\(2x - y + 3z + d = 0\) en het punt invullen: \(2 + 6 + d = 0\).",
    ),
    inv(
        r"Bereken de afstand van \(P(1, 2, 3)\) tot het vlak \(2x + y - 2z + 1 = 0\). Schrijf het antwoord als breuk.",
        ["1/3"],
        r"\(\tfrac{|2 + 2 - 6 + 1|}{\sqrt{4 + 1 + 4}} = \tfrac{1}{3}\).",
    ),
    inv(
        r"Bereken de afstand tussen de vlakken \(x + 2y + 2z = 3\) en \(x + 2y + 2z = 9\).",
        ["2", "twee"],
        r"Ze zijn evenwijdig: \(\tfrac{|9 - 3|}{\sqrt{1 + 4 + 4}} = \tfrac{6}{3}\).",
    ),
    casus(
        r"De rechte \(r\) heeft parametervergelijkingen \(x = t,\ y = 1 + t,\ z = 2t\). Het vlak \(\alpha\) is \(x + y + z = 9\).",
        [
            mk(r"Waarom snijden \(r\) en \(\alpha\) elkaar in één punt?", [r"omdat \(\vec{v} \cdot \vec{n} \neq 0\)", r"omdat \(\vec{v} \cdot \vec{n} = 0\)", r"omdat \(\vec{v} = \vec{n}\) voor deze rechte", r"omdat de oorsprong op de rechte \(r\) ligt"], 0, r"\((1, 1, 2) \cdot (1, 1, 1) = 4\): de rechte is niet evenwijdig met het vlak."),
            inv("Welke waarde van t hoort bij het snijpunt?", ["2", "twee"], r"\(t + 1 + t + 2t = 9\)."),
            inv(r"Wat is het snijpunt? Schrijf als \((x, y, z)\).", ["(2,3,4)", "(2, 3, 4)"], r"Vul de gevonden \(t\) in."),
        ],
    ),
    inv(
        r"Bereken de hoek in graden tussen de vlakken \(x + y = 0\) en \(x + z = 0\).",
        ["60", "zestig"],
        r"\(\vec{n_{1}}(1, 1, 0)\), \(\vec{n_{2}}(1, 0, 1)\): \(\cos\theta = \tfrac{1}{2}\).",
    ),
    mk(
        r"Wat is de onderlinge ligging van de rechte \(x = 1 + 2t,\ y = t,\ z = 3 - t\) en het vlak \(x - y + z = 0\)?",
        ["evenwijdig, zonder gemeenschappelijk punt", "de rechte ligt volledig in het vlak", "snijdend in precies één punt", "loodrecht op het vlak, door één punt"],
        0,
        r"\((2, 1, -1) \cdot (1, -1, 1) = 0\), maar \((1, 0, 3)\) ligt niet in het vlak: \(1 + 3 \neq 0\).",
    ),
    sorteer(
        "Wat is de onderlinge ligging van de twee vlakken?",
        ["Samenvallend", "Strikt evenwijdig", "Snijdend"],
        [(r"\(2x - 4y + 6z = 2\) en \(x - 2y + 3z = 1\)", "Samenvallend"), (r"\(x + y + z = 1\) en \(x + y + z = 5\)", "Strikt evenwijdig"), (r"\(x + y = 1\) en \(x - y = 1\)", "Snijdend"),
         (r"\(z = 0\) en \(z = 3\)", "Strikt evenwijdig"), (r"\(x = 0\) en \(y = 0\)", "Snijdend"), (r"\(3x - 3z = 6\) en \(x - z = 2\)", "Samenvallend")],
        "Vergelijk eerst de normaalvectoren, daarna de hele vergelijking.",
    ),
    tabel(
        "Juist of fout?",
        [("Twee rechten die loodrecht op hetzelfde vlak staan, zijn evenwijdig.", J), ("Twee vlakken die loodrecht op hetzelfde vlak staan, zijn evenwijdig.", F), ("Twee kruisende rechten hebben afstand nul.", F), ("Door een punt buiten een vlak gaat precies één vlak evenwijdig met dat vlak.", J)],
        "Twee muren staan allebei loodrecht op de vloer en snijden elkaar toch in een hoek van de kamer.",
        kolommen=["Juist", "Fout"],
    ),
    koppel(
        "Verbind de voorwaarde met de ligging.",
        [(r"\(\vec{v} \parallel \vec{n}\)", "rechte loodrecht op het vlak"), (r"\(\vec{v} \perp \vec{n}\)", "rechte evenwijdig met het vlak of erin"), (r"\(\vec{n_{1}} \perp \vec{n_{2}}\)", "vlakken loodrecht op elkaar"), (r"\(\vec{n_{1}} \parallel \vec{n_{2}}\)", "vlakken evenwijdig of samenvallend")],
        ["rechten kruisend"],
        "Bij een rechte en een vlak vergelijk je de richtingsvector met de normaalvector.",
    ),
    inv(
        r"Ligt \((3, 1, 2)\) op de rechte \(x = 1 + 2t,\ y = t,\ z = 3 - t\)? Geef de waarde van \(t\) die erbij hoort.",
        ["1", "een", "één"],
        r"Alle drie de vergelijkingen geven \(t = 1\).",
    ),
    mk(
        r"Welk vlak bevat de x-as en de z-as?",
        [r"\(y = 0\)", r"\(x = 0\)", r"\(z = 0\)", r"\(x + z = 0\)"],
        0,
        "Op beide assen is de y-coördinaat 0.",
    ),
    volgorde(
        r"Zet de stappen om de afstand van \(P\) tot het vlak \(\alpha\) te berekenen in volgorde.",
        [r"schrijf \(\alpha\) als \(ax + by + cz + d = 0\)", r"vul de coördinaten van \(P\) in het linkerlid in", "neem de absolute waarde", r"deel door \(\sqrt{a^{2} + b^{2} + c^{2}}\)"],
        "Delen door de norm van de normaalvector geeft een echte afstand.",
    ),
    keuze(
        r"Een rechte in de ruimte heeft [[*twee|één|drie]] cartesische vergelijkingen nodig. Een vlak heeft er [[*één|twee|drie]].",
        "Een rechte is de snijlijn van twee vlakken.",
    ),
    mk(
        r"Welke vector is een richtingsvector van de snijlijn van \(z = 0\) en \(x = 0\)?",
        [r"\((0, 1, 0)\)", r"\((1, 0, 0)\)", r"\((0, 0, 1)\)", r"\((1, 0, 1)\)"],
        0,
        "Beide vlakken bevatten de y-as.",
    ),
    tabel(
        r"Het vlak \(\alpha\) is \(x - 2y + 2z - 4 = 0\). Ligt het punt in \(\alpha\)?",
        [(r"\((4, 0, 0)\)", J), (r"\((0, 0, 2)\)", J), (r"\((0, 2, 0)\)", F), (r"\((2, 1, 2)\)", J)],
        r"Vul in: \(0 - 4 + 0 - 4 \neq 0\) voor \((0, 2, 0)\).",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"In \(ax + by + cz + d = 0\) is \((a, b, c)\) een [[normaalvector]]. Die staat [[loodrecht]] op elke richtingsvector van het vlak.",
        ["richtingsvector", "evenwijdig"],
        "Daarom volstaat één punt en een normaalvector om een vlak vast te leggen.",
    ),
    mk(
        r"Twee rechten hebben richtingsvectoren \((1, 2, 0)\) en \((2, 4, 0)\) en geen gemeenschappelijk punt. Wat is hun ligging?",
        ["strikt evenwijdig", "kruisend, want ze snijden niet", "snijdend in één punt", "samenvallend"],
        0,
        "Evenwijdige richtingsvectoren en geen gemeenschappelijk punt.",
    ),
    inv(
        r"Voor welke \(k\) staat het vlak \(2x + ky + z = 1\) loodrecht op het vlak \(x + y - 4z = 0\)?",
        ["2", "twee"],
        r"\(\vec{n_{1}} \cdot \vec{n_{2}} = 2 + k - 4 = 0\).",
    ),
    mk(
        "Hoe vind je een vergelijking van het vlak door drie punten A, B en C?",
        [r"met \(\overrightarrow{AB}\) en \(\overrightarrow{AC}\) als richtingsvectoren door \(A\)", r"met \(\overrightarrow{OA}\) en \(\overrightarrow{OB}\) als richtingsvectoren door de oorsprong", r"door de normaalvectoren in A, B en C bij elkaar op te tellen", r"door de middens van \([AB]\) en \([BC]\) met elkaar te verbinden"],
        0,
        "De punten mogen niet op één rechte liggen.",
    ),
    inv(
        r"Bereken de afstand van de oorsprong tot het vlak \(2x + 3y + 6z = 14\).",
        ["2", "twee"],
        r"\(\tfrac{|0 - 14|}{\sqrt{4 + 9 + 36}} = \tfrac{14}{7}\).",
    ),
    mk(
        r"Welke cartesische vergelijkingen horen bij \(x = 1 + 2t,\ y = 3 - t,\ z = t\)?",
        [r"\(\dfrac{x - 1}{2} = \dfrac{y - 3}{-1} = z\)", r"\(\dfrac{x + 1}{2} = \dfrac{y + 3}{-1} = z\)", r"\(\dfrac{x - 2}{1} = \dfrac{y + 1}{3} = z\)", r"\(x - 1 = y - 3 = z\)"],
        0,
        r"Los elke vergelijking op naar \(t\) en stel ze gelijk.",
    ),
    mk(
        r"Een rechte door \((1, 1, 1)\) staat loodrecht op het vlak \(3x - y + 2z = 5\). Welke parametervergelijkingen heeft ze?",
        [r"\(x = 1 + 3t,\ y = 1 - t,\ z = 1 + 2t\)", r"\(x = 3 + t,\ y = -1 + t,\ z = 2 + t\)", r"\(x = 1 + t,\ y = 1 + 3t,\ z = 1 + 2t\)", r"\(x = 1 - 3t,\ y = 1 - t,\ z = 1 - 2t\)"],
        0,
        "De normaalvector van het vlak is een richtingsvector van de loodrechte.",
    ),
    inv(
        r"Een vlak gaat door \((2, 0, 0)\), \((0, 3, 0)\) en \((0, 0, 6)\). Het heeft de vorm \(3x + 2y + z + d = 0\). Hoeveel is \(d\)?",
        ["-6", "−6", "min 6"],
        r"Vul \((2, 0, 0)\) in: \(6 + d = 0\). Controleer met de andere twee punten.",
    ),
]
