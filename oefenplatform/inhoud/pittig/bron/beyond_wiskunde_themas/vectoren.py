"""Punten, vectoren en afstanden in de ruimte — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_lijn, DONKER, GROEN

BALK = "vectoren-balk-bey"
_P = {"O": (0, 0, 0), "A": (4, 0, 0), "B": (4, 3, 0), "C": (0, 3, 0), "D": (0, 0, 2), "E": (4, 0, 2), "F": (4, 3, 2), "G": (0, 3, 2)}
_RIBBEN = ["OA", "AB", "BC", "CO", "DE", "EF", "FG", "GD", "OD", "AE", "BF", "CG"]
_VERBORGEN = {"OA", "CO", "OD"}


def _xy(p):
    x, y, z = p
    return 430 + y * 125 - x * 55, 400 - z * 120 + x * 42


def _plek(n):
    return _xy(_P[n])


def _balk():
    d = []
    # assen
    for eind, naam in (((5.6, 0, 0), "x"), ((0, 4.4, 0), "y"), ((0, 0, 3.0), "z")):
        x2, y2 = _xy(eind)
        d.append(s_lijn(*_xy((0, 0, 0)), x2, y2, kleur="#9a9a9a", dikte=2))
        d.append(s_tekst(x2 + (14 if naam != "x" else -14), y2 + (6 if naam != "z" else -8), naam, 24, kleur="#7a7a6a", vet=True))
    for r in _RIBBEN:
        x1, y1 = _plek(r[0])
        x2, y2 = _plek(r[1])
        streep = ' stroke-dasharray="10 8"' if r in _VERBORGEN else ""
        d.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GROEN}" stroke-width="3"{streep}/>')
    verschuif = {"O": (-24, -10), "A": (-26, 22), "B": (16, 26), "C": (20, 22), "D": (-26, -8), "E": (-26, -6), "F": (20, -8), "G": (16, -12)}
    for n in _P:
        x, y = _plek(n)
        d.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{DONKER}"/>')
        dx, dy = verschuif[n]
        d.append(s_tekst(x + dx, y + dy, n, 26, vet=True))
    return d


def _zone(n):
    x, y = _plek(n)
    return pix_zone(x - 32, y - 32, 64, 64)


GRAFIEKEN = [dict(naam=BALK, titel="Een balk van 4 bij 3 bij 2 in een orthonormaal assenstelsel", eigen=_balk)]
PRENTEN = [dict(bestand=f"{BALK}.svg", zelf=True, wat="balk OABCDEFG met O in de oorsprong, OA = 4, OC = 3, OD = 2", vragen="klikvragen over coördinaten en vectoren")]

VRAGEN = [
    klik(
        r"De balk heeft \(|OA| = 4\), \(|OC| = 3\) en \(|OD| = 2\), met \(A\) op de x-as, \(C\) op de y-as en \(D\) op de z-as. Klik op het hoekpunt met coördinaat \((4, 3, 2)\).",
        f"{BALK}.svg",
        [_zone("F")],
        "Vier naar voren, drie naar rechts en twee omhoog.",
    ),
    klik(
        r"Klik op het hoekpunt \(P\) waarvoor \(\overrightarrow{OP} = \overrightarrow{OC} + \overrightarrow{OD}\).",
        f"{BALK}.svg",
        [_zone("G")],
        r"\((0, 3, 0) + (0, 0, 2) = (0, 3, 2)\).",
    ),
    met_prent(f"{BALK}.svg", tabel(
        r"Kijk naar de balk met \(A(4, 0, 0)\), \(C(0, 3, 0)\) en \(D(0, 0, 2)\). Juist of fout?",
        [(r"\(\overrightarrow{AG} = (-4, 3, 2)\)", J), (r"\(\overrightarrow{OB} = \overrightarrow{DF}\)", J), (r"\(|OF| = 9\)", F), (r"Het midden van \([OF]\) is \((2;\ 1{,}5;\ 1)\).", J), (r"\(\overrightarrow{OA} \cdot \overrightarrow{OC} = 12\)", F)],
        r"\(|OF| = \sqrt{16 + 9 + 4} = \sqrt{29}\). Twee ribben langs verschillende assen staan loodrecht: scalair product 0.",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{BALK}.svg", inv(
        r"Bereken in de balk \(\overrightarrow{AE} \cdot \overrightarrow{AG}\).",
        ["4", "vier"],
        r"\(\overrightarrow{AE} = (0, 0, 2)\) en \(\overrightarrow{AG} = (-4, 3, 2)\): \(0 + 0 + 4\).",
    )),
    mk(
        r"Wat is de afstand tussen \(A(1, -2, 3)\) en \(B(3, 1, 9)\)?",
        ["7", "49", r"\(\sqrt{13}\)", "11"],
        0,
        r"\(\overrightarrow{AB} = (2, 3, 6)\) en \(\sqrt{4 + 9 + 36} = 7\).",
    ),
    mk(
        r"Welke vector heeft dezelfde richting en zin als \(\vec{u}(1, 2, 2)\) en lengte 1?",
        [r"\(\left(\tfrac{1}{3}, \tfrac{2}{3}, \tfrac{2}{3}\right)\)", r"\(\left(\tfrac{1}{5}, \tfrac{2}{5}, \tfrac{2}{5}\right)\)", r"\(\left(-\tfrac{1}{3}, -\tfrac{2}{3}, -\tfrac{2}{3}\right)\)", r"\((1, 0, 0)\)"],
        0,
        r"\(\|\vec{u}\| = 3\): deel elke coördinaat door 3.",
    ),
    inv(
        r"Bereken de hoek in graden tussen \(\vec{u}(1, 0, 1)\) en \(\vec{v}(0, 1, 1)\).",
        ["60", "zestig"],
        r"\(\cos\theta = \tfrac{1}{\sqrt{2} \cdot \sqrt{2}} = \tfrac{1}{2}\).",
    ),
    inv(
        r"Voor welke \(k\) staat \(\vec{u}(2, k, 1)\) loodrecht op \(\vec{v}(1, 3, -5)\)?",
        ["1", "een", "één"],
        r"\(2 + 3k - 5 = 0\).",
    ),
    tabel(
        r"Is \(\vec{v}\) evenwijdig met \(\vec{u}(2, -4, 6)\)?",
        [(r"\(\vec{v}(-1, 2, -3)\)", J), (r"\(\vec{v}(1, 2, 3)\)", F), (r"\(\vec{v}(3, -6, 9)\)", J), (r"\(\vec{v}(4, -8, 10)\)", F)],
        r"Evenwijdig als \(\vec{v} = k\vec{u}\) voor één getal \(k\) in alle drie de coördinaten.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Bepaal het zwaartepunt van de driehoek met \(A(1, 0, 2)\), \(B(3, 4, 0)\) en \(C(2, -1, 4)\). Schrijf als \((x, y, z)\).",
        ["(2,1,2)", "(2, 1, 2)"],
        r"Het gemiddelde van de coördinaten: \(\left(\tfrac{6}{3}, \tfrac{3}{3}, \tfrac{6}{3}\right)\).",
    ),
    casus(
        r"\(ABCD\) is een parallellogram met \(A(1, 2, 0)\), \(B(3, 1, 1)\) en \(C(4, 3, 2)\).",
        [
            mk(r"Welke vectoren zijn gelijk?", [r"\(\overrightarrow{AB} = \overrightarrow{DC}\)", r"\(\overrightarrow{AB} = \overrightarrow{CD}\)", r"\(\overrightarrow{AC} = \overrightarrow{BD}\)", r"\(\overrightarrow{AD} = \overrightarrow{CB}\)"], 0, "Overstaande zijden hebben dezelfde richting, zin en lengte."),
            inv(r"Bepaal \(D\). Schrijf als \((x, y, z)\).", ["(2,4,1)", "(2, 4, 1)"], r"\(D = A + C - B\)."),
            inv(r"Bereken de eerste coördinaat van het snijpunt van de diagonalen. Geef een decimaal getal.", ["2,5", "2.5"], r"Het midden van \([AC]\): \(\tfrac{1 + 4}{2}\)."),
        ],
    ),
    sorteer(
        "Is de hoek tussen de vectoren scherp, recht of stomp?",
        ["Scherp", "Recht", "Stomp"],
        [(r"\((1, 2, 0)\) en \((2, 1, 0)\)", "Scherp"), (r"\((1, -1, 2)\) en \((2, 2, 0)\)", "Recht"), (r"\((1, 0, 0)\) en \((-3, 1, 0)\)", "Stomp"),
         (r"\((3, 1, -1)\) en \((1, 0, 3)\)", "Recht"), (r"\((1, 1, 1)\) en \((-1, -1, 0)\)", "Stomp"), (r"\((0, 2, 5)\) en \((1, 1, 1)\)", "Scherp")],
        "Kijk naar het teken van het scalair product.",
    ),
    tabel(
        "Juist of fout voor alle vectoren?",
        [(r"\(\vec{v} \cdot \vec{v} = \|\vec{v}\|^{2}\)", J), (r"\((\vec{u} + \vec{v}) \cdot (\vec{u} - \vec{v}) = \|\vec{u}\|^{2} - \|\vec{v}\|^{2}\)", J), (r"\(\|\vec{u} + \vec{v}\| = \|\vec{u}\| + \|\vec{v}\|\)", F), (r"\(\|k\vec{v}\| = k\|\vec{v}\|\) voor elk reëel getal \(k\)", F)],
        r"Voor negatieve \(k\) is \(\|k\vec{v}\| = |k|\,\|\vec{v}\|\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Op een voorwerp werken \(\vec{F_{1}}(3, 0, 0)\) en \(\vec{F_{2}}(0, 4, 0)\), in newton. Hoe groot is de resulterende kracht?",
        ["5 N", "7 N", "12 N", "1 N"],
        0,
        r"\(\|(3, 4, 0)\| = 5\).",
    ),
    koppel(
        "Verbind de vraag met de berekening.",
        [("afstand tussen twee punten", r"\(\|\overrightarrow{AB}\|\)"), ("staan twee vectoren loodrecht?", r"\(\vec{u} \cdot \vec{v} = 0\)"), ("hoek tussen twee vectoren", r"\(\dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\)"), ("zijn twee vectoren evenwijdig?", r"\(\vec{u} = k\vec{v}\)")],
        [r"\(\vec{u} + \vec{v} = \vec{0}\)"],
        "Elke vraag over de ligging heeft zijn eigen rekenregel.",
    ),
    keuze(
        r"Het scalair product van twee vectoren is een [[*getal|vector]]. Is het negatief, dan is de hoek [[*stomp|scherp|recht]].",
        r"\(\cos\theta < 0\) bij een hoek tussen \(90^\circ\) en \(180^\circ\).",
    ),
    inv(
        r"Bereken \(\|\vec{v}\|\) voor \(\vec{v}(2, -1, 2)\).",
        ["3", "drie"],
        r"\(\sqrt{4 + 1 + 4}\).",
    ),
    volgorde(
        r"Zet de stappen om de hoek tussen \(\vec{u}\) en \(\vec{v}\) te berekenen in volgorde.",
        [r"bereken \(\vec{u} \cdot \vec{v}\)", r"bereken \(\|\vec{u}\|\) en \(\|\vec{v}\|\)", r"deel het scalair product door het product van de normen", r"neem de boogcosinus"],
        "De formule komt uit de definitie van het scalair product.",
    ),
    mk(
        r"Het midden van \([AB]\) is \(M(2, 0, 5)\) en \(A(1, -3, 4)\). Wat is \(B\)?",
        [r"\((3, 3, 6)\)", r"\((1{,}5;\ -1{,}5;\ 4{,}5)\)", r"\((1, 3, 1)\)", r"\((3, -3, 6)\)"],
        0,
        r"\(B = 2M - A\).",
    ),
    sleep(
        r"De puntvector van \(P\) is de vector van [[de oorsprong]] naar \(P\). Twee pijlen met dezelfde coördinaten stellen [[dezelfde]] vrije vector voor.",
        ["het punt A", "een andere"],
        "Een vrije vector heeft geen vast beginpunt.",
    ),
    tabel(
        r"Liggen de drie punten op één rechte?",
        [(r"\((0, 0, 0)\), \((1, 2, 3)\), \((2, 4, 6)\)", J), (r"\((1, 1, 1)\), \((2, 3, 4)\), \((3, 5, 7)\)", J), (r"\((1, 0, 0)\), \((0, 1, 0)\), \((0, 0, 1)\)", F)],
        r"Ga na of \(\overrightarrow{AB}\) en \(\overrightarrow{AC}\) evenwijdig zijn.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Wat is \(\vec{u} \cdot \vec{v}\) als \(\|\vec{u}\| = 4\), \(\|\vec{v}\| = 3\) en de hoek \(120^\circ\) is?",
        ["−6", "6", "12", r"\(-6\sqrt{3}\)"],
        0,
        r"\(4 \cdot 3 \cdot \cos 120^\circ = 12 \cdot \left(-\tfrac{1}{2}\right)\).",
    ),
    inv(
        "Een drone vliegt 6 m naar het oosten, 2 m naar het noorden en 3 m omhoog. Hoeveel meter ligt hij van zijn vertrekpunt?",
        ["7", "zeven"],
        r"\(\sqrt{36 + 4 + 9}\).",
    ),
    mk(
        r"Welk punt ligt op gelijke afstand van \(A(0, 0, 0)\) en \(B(4, 0, 0)\)?",
        [r"\((2, 5, -1)\)", r"\((1, 0, 0)\)", r"\((4, 2, 0)\)", r"\((3, 3, 3)\)"],
        0,
        "Reken na: elk punt met x = 2 ligt even ver van A als van B.",
    ),
    inv(
        r"Bereken de derde coördinaat van \(3\vec{u} - 2\vec{v}\) met \(\vec{u}(1, 0, 2)\) en \(\vec{v}(0, 1, 4)\).",
        ["-2", "−2", "min 2"],
        r"\(3 \cdot 2 - 2 \cdot 4\).",
    ),
    mk(
        r"Bereken \(\vec{u} \cdot \vec{v}\) voor \(\vec{u}(1, -2, 3)\) en \(\vec{v}(4, 1, -1)\).",
        ["−1", "1", "9", r"\((4, -2, -3)\)"],
        0,
        r"\(4 - 2 - 3\). Het scalair product is een getal, geen vector.",
    ),
    inv(
        r"Bepaal het zwaartepunt van het viervlak met hoekpunten \((0, 0, 0)\), \((4, 0, 0)\), \((0, 4, 0)\) en \((0, 0, 4)\). Schrijf als \((x, y, z)\).",
        ["(1,1,1)", "(1, 1, 1)"],
        "Tel de vier hoekpunten op en deel door 4.",
    ),
    mk(
        r"Welke vector staat loodrecht op zowel \((1, 0, 0)\) als \((0, 1, 1)\)?",
        [r"\((0, 1, -1)\)", r"\((0, 1, 1)\)", r"\((1, 1, 0)\)", r"\((1, -1, 1)\)"],
        0,
        r"Beide scalaire producten moeten 0 zijn: \(0 = 0\) en \(1 - 1 = 0\).",
    ),
]
