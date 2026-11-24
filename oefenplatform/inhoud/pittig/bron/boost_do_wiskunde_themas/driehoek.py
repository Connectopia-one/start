"""Sinusregel, cosinusregel en vectoren — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import s_lijn, s_tekst, pix_zone, DONKER, GROEN

ROOS = "vectoren-rooster-do"
ROOD = "#c0522c"
PAARS = "#7a4b8c"


def X(x):
    return 120 + 80 * x


def Y(y):
    return 560 - 80 * y


PUNTEN = {"A": (1, 1), "P": (5, 4), "Q": (4, 2), "S": (3, 5), "T": (3, 0)}


def _pijl(x1, y1, x2, y2, kleur, naam, dx, dy):
    a, b, c, d = X(x1), Y(y1), X(x2), Y(y2)
    return [f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="{kleur}" stroke-width="5" marker-end="url(#pijl{naam})"/>',
            f'<defs><marker id="pijl{naam}" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{kleur}"/></marker></defs>',
            s_tekst((a + c) / 2 + dx, (b + d) / 2 + dy, naam, 28, kleur=kleur, vet=True)]


def _rooster():
    d = []
    for i in range(10):
        d.append(s_lijn(X(i), Y(0), X(i), Y(6), kleur="#d9d2bf", dikte=1))
    for j in range(7):
        d.append(s_lijn(X(0), Y(j), X(9), Y(j), kleur="#d9d2bf", dikte=1))
    d += _pijl(6, 5, 9, 6, ROOD, "u", -6, -16)
    d += _pijl(8, 1, 9, 3, PAARS, "v", -26, 0)
    for k, (x, y) in PUNTEN.items():
        d.append(f'<circle cx="{X(x)}" cy="{Y(y)}" r="8" fill="{DONKER}"/>')
        d.append(s_tekst(X(x) + 20, Y(y) - 14, k, 26, vet=True))
    return d


def _zone(k):
    x, y = PUNTEN[k]
    return pix_zone(X(x) - 30, Y(y) - 40, 64, 70)


GRAFIEKEN = [dict(naam=ROOS, titel="Rooster met de vectoren u en v en vijf punten", eigen=_rooster)]
PRENTEN = [dict(bestand=f"{ROOS}.svg", zelf=True, wat="rooster met vectoren u = (3, 1) en v = (1, 2) en punten A, P, Q, S, T", vragen="klikvragen over optellen en vermenigvuldigen van vectoren")]

VRAGEN = [
    klik(
        "Verschuif punt A over de som u + v. Klik op het punt waar je aankomt.",
        f"{ROOS}.svg",
        [_zone("P")],
        r"\(\vec{u} = (3, 1)\) en \(\vec{v} = (1, 2)\), samen \((4, 3)\). Vanuit \(A(1, 1)\) kom je in \((5, 4)\): punt P.",
    ),
    klik(
        "Trek v af van u en verschuif A over dat verschil. Klik op het punt waar je aankomt.",
        f"{ROOS}.svg",
        [_zone("T")],
        r"\(\vec{u} - \vec{v} = (2, -1)\). Vanuit \(A(1, 1)\) kom je in \((3, 0)\): punt T.",
    ),
    klik(
        "Neem de vector v twee keer en verschuif A daarover. Klik op het punt waar je aankomt.",
        f"{ROOS}.svg",
        [_zone("S")],
        r"\(2\vec{v} = (2, 4)\). Vanuit \(A(1, 1)\) kom je in \((3, 5)\): punt S.",
    ),
    met_prent(f"{ROOS}.svg", tabel(
        "Kijk naar het rooster. Juist of fout?",
        [(r"De vector van A naar Q is gelijk aan \(\vec{u}\).", J),
         (r"De vector van Q naar P is gelijk aan \(\vec{v}\).", J),
         (r"\(\|\vec{u}\| = \|\vec{v}\|\)", F),
         (r"De vector van S naar A is gelijk aan \(-2\vec{v}\).", J),
         (r"\(\vec{u}\) en \(\vec{v}\) hebben dezelfde richting.", F)],
        r"Een vector mag je verschuiven: enkel richting, zin en grootte tellen. \(\|\vec{u}\| = \sqrt{10}\) en \(\|\vec{v}\| = \sqrt{5}\).",
        kolommen=["Juist", "Fout"],
    )),
    inv(
        "Kijk naar het rooster. Wat is de norm van u + v?",
        ["5"],
        r"\(\vec{u} + \vec{v} = (4, 3)\) en \(\sqrt{16 + 9} = 5\).",
    ),
    mk(
        r"In driehoek ABC is \(a = 8\), \(\alpha = 30^\circ\) en \(\beta = 45^\circ\). Hoe lang is \(b\)?",
        [r"\(8\sqrt{2}\)", r"\(4\sqrt{2}\)", r"\(\tfrac{8\sqrt{2}}{3}\)", r"\(16\)"],
        0,
        r"Sinusregel: \(b = \dfrac{8 \cdot \sin 45^\circ}{\sin 30^\circ} = \dfrac{8 \cdot \tfrac{\sqrt{2}}{2}}{\tfrac{1}{2}} = 8\sqrt{2}\).",
    ),
    mk(
        r"Een driehoek heeft zijden \(b = 5\), \(c = 8\) en ingesloten hoek \(\alpha = 60^\circ\). Hoe lang is \(a\)?",
        [r"\(\sqrt{89}\)", r"\(7\)", r"\(\sqrt{129}\)", r"\(13\)"],
        1,
        r"\(a^{2} = 25 + 64 - 2 \cdot 5 \cdot 8 \cdot \cos 60^\circ = 89 - 40 = 49\), dus \(a = 7\).",
    ),
    inv(
        r"Een driehoek heeft zijden \(3\), \(5\) en \(7\). Hoe groot is de hoek tegenover de zijde \(7\), in graden?",
        ["120", "120°", "120 graden"],
        r"\(\cos\gamma = \dfrac{9 + 25 - 49}{2 \cdot 3 \cdot 5} = \dfrac{-15}{30} = -\tfrac{1}{2}\), dus \(\gamma = 120^\circ\).",
    ),
    sorteer(
        "Wat ken je? Welke regel gebruik je eerst?",
        ["Sinusregel", "Cosinusregel"],
        [("twee hoeken en een zijde", "Sinusregel"),
         ("drie zijden", "Cosinusregel"),
         ("twee zijden en de ingesloten hoek", "Cosinusregel"),
         ("twee zijden en de hoek tegenover één ervan", "Sinusregel"),
         ("een zijde, de hoek ertegenover en nog een hoek", "Sinusregel")],
        "De sinusregel vraagt een koppel zijde en overstaande hoek. Zonder zo een koppel begin je met de cosinusregel.",
    ),
    tabel(
        "Kan een driehoek deze drie zijden hebben?",
        [(r"\(4\), \(6\), \(9\)", J), (r"\(2\), \(3\), \(5\)", F), (r"\(5\), \(5\), \(9\)", J), (r"\(1\), \(10\), \(10\)", J), (r"\(3\), \(4\), \(8\)", F)],
        r"De som van de twee kleinste zijden moet groter zijn dan de grootste. \(2 + 3 = 5\) geeft een platte driehoek: dat is geen driehoek.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        r"Twee landmeters A en B staan \(100\) m uit elkaar. Ze kijken naar een boom C aan de overkant van een rivier. A meet een hoek van \(70^\circ\) tussen AB en AC, B meet \(50^\circ\) tussen BA en BC.",
        [
            inv("Hoe groot is de hoek in C, in graden?", ["60", "60°"], r"\(180^\circ - 70^\circ - 50^\circ = 60^\circ\)."),
            mk("Welke formule geeft de afstand van A tot de boom?",
               [r"\(\dfrac{100 \cdot \sin 50^\circ}{\sin 60^\circ}\)", r"\(\dfrac{100 \cdot \sin 70^\circ}{\sin 60^\circ}\)", r"\(\dfrac{100 \cdot \sin 60^\circ}{\sin 50^\circ}\)", r"\(100 \cdot \cos 70^\circ\)"], 0,
               "AC ligt tegenover de hoek in B (50°), en AB = 100 m ligt tegenover de hoek in C (60°)."),
            mk("Hoe ver staat A van de boom, afgerond op een meter?", ["88 m", "109 m", "113 m", "77 m"], 0,
               r"\(\dfrac{100 \cdot 0{,}766}{0{,}866} \approx 88\) m."),
        ],
    ),
    keuze(
        r"Als in de cosinusregel \(a^{2} = b^{2} + c^{2} - 2bc\cos\alpha\) de hoek \(\alpha\) stomp is, dan is \(\cos\alpha\) [[*negatief|positief|nul]] en is \(a^{2}\) [[*groter|kleiner]] dan \(b^{2} + c^{2}\).",
        "Min een negatief getal wordt plus. Tegenover een stompe hoek ligt dus een zijde langer dan bij een rechte hoek.",
    ),
    mk(
        r"Je zoekt met de sinusregel een hoek en vindt \(\sin\beta = 0{,}5\). Uit de schets weet je dat \(\beta\) stomp is. Hoe groot is \(\beta\)?",
        [r"\(30^\circ\)", r"\(150^\circ\)", r"\(120^\circ\)", r"\(60^\circ\)"],
        1,
        r"Supplementaire hoeken hebben dezelfde sinus. Het rekentoestel geeft \(30^\circ\), de stompe hoek is \(180^\circ - 30^\circ = 150^\circ\).",
    ),
    tabel(
        "Juist of fout over vectoren?",
        [
            (r"\(\vec{a} + \vec{b} = \vec{b} + \vec{a}\)", J),
            (r"\(\|\vec{a} + \vec{b}\| = \|\vec{a}\| + \|\vec{b}\|\) voor elke twee vectoren", F),
            (r"\(-\vec{a}\) heeft dezelfde richting als \(\vec{a}\) maar een andere zin", J),
            (r"\(\vec{a} - \vec{a}\) is de nulvector", J),
            (r"\(3\vec{a}\) heeft een norm die drie keer zo groot is als die van \(\vec{a}\)", J),
            (r"Twee vectoren met dezelfde norm zijn altijd gelijk", F),
        ],
        "De norm van een som is enkel de som van de normen als beide vectoren dezelfde richting en zin hebben. Gelijke vectoren hebben ook dezelfde richting en zin.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"\(A(2, -1)\) en \(B(-4, 7)\). Wat zijn de coördinaten van de vector van A naar B?",
        [r"\((-6, 8)\)", r"\((6, -8)\)", r"\((-2, 6)\)", r"\((-6, 6)\)"],
        0,
        r"Eindpunt min beginpunt: \((-4 - 2, 7 - (-1)) = (-6, 8)\).",
    ),
    inv(
        r"\(\vec{a} = (2, -3)\) en \(\vec{b} = (-1, 4)\). Wat is de x-coördinaat van \(3\vec{a} - 2\vec{b}\)?",
        ["8"],
        r"\(3 \cdot 2 - 2 \cdot (-1) = 6 + 2 = 8\). De y-coördinaat is \(-9 - 8 = -17\).",
    ),
    mk(
        "Een boot vaart met 4 m/s naar het noorden. De stroming duwt hem met 3 m/s naar het oosten. Hoe snel beweegt de boot echt?",
        ["7 m/s", "5 m/s", "1 m/s", "12 m/s"],
        1,
        r"De snelheden zijn vectoren die loodrecht op elkaar staan. \(\sqrt{16 + 9} = 5\) m/s.",
    ),
    koppel(
        "Verbind elk kenmerk van een vector met de uitleg.",
        [("richting", "de stand van de drager, zoals horizontaal of schuin"),
         ("zin", "welke van de twee kanten van de drager de pijl op wijst"),
         ("grootte", "de lengte van de pijl"),
         ("aangrijpingspunt", "het punt waar de pijl begint")],
        ["de kleur van de pijl"],
        "Richting, zin en grootte bepalen samen een vector. Het beginpunt mag verschuiven.",
    ),
    sleep(
        r"Volgens Chasles-Möbius is \(\vec{AB} = \vec{AC} +\) [[\(\vec{CB}\)]]. Met coördinaten is \(\vec{AB}\) de puntvector van [[B]] min die van [[A]].",
        [r"\(\vec{BC}\)", "C"],
        "Een omweg langs C brengt je op dezelfde plaats. Eindpunt min beginpunt.",
    ),
    volgorde(
        r"In driehoek ABC is \(\alpha = 80^\circ\), \(\beta = 35^\circ\). Zet de zijden van kort naar lang.",
        ["b", "c", "a"],
        r"\(\gamma = 65^\circ\). De kortste zijde ligt tegenover de kleinste hoek: \(b\) (\(35^\circ\)), dan \(c\) (\(65^\circ\)), dan \(a\) (\(80^\circ\)).",
    ),
    mk(
        r"Een parallellogram heeft zijden \(5\) en \(8\) en een hoek van \(120^\circ\). Hoe lang is de langste diagonaal?",
        [r"\(7\)", r"\(\sqrt{129}\)", r"\(13\)", r"\(\sqrt{89}\)"],
        1,
        r"De langste diagonaal ligt tegenover de stompe hoek: \(25 + 64 - 80 \cdot \cos 120^\circ = 89 + 40 = 129\).",
    ),
    tabel(
        r"Een vector \(\vec{v} = (6, -8)\). Klopt het?",
        [(r"\(\|\vec{v}\| = 10\)", J), (r"\(\tfrac{1}{10}\vec{v}\) is een eenheidsvector", J), (r"\(\tfrac{1}{2}\vec{v} = (3, 4)\)", F), (r"\(-\vec{v} = (-6, 8)\)", J)],
        r"\(\tfrac{1}{2}\vec{v} = (3, -4)\): ook de y-coördinaat halveer je, met haar teken.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        "Twee krachten van 6 N werken op hetzelfde punt met een hoek van 120° ertussen. Hoe groot is de resulterende kracht?",
        ["12 N", "6 N", "0 N", r"\(6\sqrt{3}\) N"],
        1,
        r"De twee pijlen vormen een ruit. De diagonaal maakt een gelijkzijdige driehoek met zijde \(6\): resultante \(6\) N.",
    ),
    inv(
        r"De hoeken van een driehoek verhouden zich als \(1 : 2 : 3\). Hoeveel graden is de grootste hoek?",
        ["90", "90°"],
        r"Samen zes delen voor \(180^\circ\): één deel is \(30^\circ\). De grootste is \(90^\circ\).",
    ),
    mk(
        r"In driehoek ABC is \(b = 6\), \(c = 10\) en \(\alpha = 90^\circ\). Wat geeft de cosinusregel voor \(a^{2}\)?",
        [r"\(136\)", r"\(16\)", r"\(64\)", r"\(256\)"],
        0,
        r"\(\cos 90^\circ = 0\), dus \(a^{2} = 36 + 100 = 136\). Dat is gewoon Pythagoras.",
    ),
    tabel(
        "Juist of fout over driehoeken?",
        [("Een driehoek kan twee stompe hoeken hebben.", F),
         ("Tegenover de grootste hoek ligt de langste zijde.", J),
         ("Twee driehoeken met dezelfde drie hoeken hebben dezelfde zijden.", F),
         ("In een gelijkzijdige driehoek is elke hoek 60°.", J)],
        "Twee stompe hoeken samen zijn al meer dan 180°. Met enkel de hoeken ken je de vorm, niet de grootte.",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Een vector \(\vec{w}\) heeft norm \(13\) en x-coördinaat \(5\). De y-coördinaat is positief. Hoeveel is ze?",
        ["12"],
        r"\(\sqrt{169 - 25} = 12\).",
    ),
    mk(
        r"Welke vector heeft dezelfde richting als \((2, 3)\) maar een tegengestelde zin?",
        [r"\((3, 2)\)", r"\((-4, -6)\)", r"\((4, 6)\)", r"\((-2, 3)\)"],
        1,
        r"\((-4, -6) = -2 \cdot (2, 3)\). Een negatief veelvoud keert de zin om.",
    ),
]
