"""Bedrijfswetenschappen: matrices, grafen en stelsels — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, GROEN, LICHT, DONKER

GRAAF = "matrices-graaf"
KNOPEN = {"A": (260, 170), "B": (740, 170), "C": (260, 500), "D": (740, 500)}
PIJLEN = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A"), ("C", "D"), ("D", "B")]
R = 42


def _pijl(a, b):
    (x1, y1), (x2, y2) = KNOPEN[a], KNOPEN[b]
    dx, dy = x2 - x1, y2 - y1
    lengte = math.hypot(dx, dy)
    ux, uy = dx / lengte, dy / lengte
    # twee pijlen tussen dezelfde knopen: elk een beetje opzij
    ox, oy = (0, 0)
    if (b, a) in PIJLEN:
        ox, oy = -uy * 16, ux * 16
    sx, sy = x1 + ux * R + ox, y1 + uy * R + oy
    ex, ey = x2 - ux * (R + 2) + ox, y2 - uy * (R + 2) + oy
    return f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{GROEN}" stroke-width="4" marker-end="url(#pijlpunt)"/>'


def _graaf():
    d = [f'<defs><marker id="pijlpunt" markerUnits="userSpaceOnUse" markerWidth="22" markerHeight="18" refX="18" refY="9" orient="auto"><path d="M0,0 L22,9 L0,18 z" fill="{GROEN}"/></marker></defs>']
    d += [_pijl(a, b) for a, b in PIJLEN]
    for n, (x, y) in KNOPEN.items():
        d.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="{LICHT}" stroke="{GROEN}" stroke-width="3"/>')
        d.append(s_tekst(x, y + 10, n, 30, kleur=DONKER, vet=True))
    return d


def _kz(n):
    x, y = KNOPEN[n]
    return pix_zone(x - R - 6, y - R - 6, 2 * R + 12, 2 * R + 12)


GRAFIEKEN = [dict(naam=GRAAF, titel="Een gerichte graaf: wegen tussen vier depots", eigen=_graaf)]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over een graaf en zijn verbindingsmatrix") for g in GRAFIEKEN]


def m(*rijen):
    """Een matrix in LaTeX."""
    return r"\begin{bmatrix} " + r" \\ ".join(" & ".join(str(x) for x in r) for r in rijen) + r" \end{bmatrix}"


def um(*rijen, k):
    """Een uitgebreide matrix met een streep voor de laatste k kolommen."""
    n = len(rijen[0]) - k
    kol = "c" * n + "|" + "c" * k
    return r"\left[\begin{array}{" + kol + "} " + r" \\ ".join(" & ".join(str(x) for x in r) for r in rijen) + r" \end{array}\right]"


VRAGEN = [
    klik(
        "Naar welk depot kan je vanuit C in precies twee stappen op twee verschillende manieren rijden? Klik erop.",
        f"{GRAAF}.svg",
        [_kz("B")],
        "C → A → B en C → D → B. Dat is ook het getal 2 op rij C, kolom B van M², met M de verbindingsmatrix.",
    ),
    klik(
        "Klik op het enige depot van waaruit een weg rechtstreeks naar A vertrekt.",
        f"{GRAAF}.svg",
        [_kz("C")],
        "Enkel de pijl C → A komt in A aan.",
    ),
    met_prent(f"{GRAAF}.svg", mk(
        "In de verbindingsmatrix M staat op rij i en kolom j een 1 als er een pijl van i naar j gaat. Welke rij hoort bij A (kolommen A, B, C, D)?",
        [r"\((1\ \ 0\ \ 1\ \ 0)\)", r"\((0\ \ 1\ \ 1\ \ 0)\)", r"\((0\ \ 1\ \ 0\ \ 1)\)", r"\((0\ \ 0\ \ 1\ \ 0)\)"],
        1,
        "Vanuit A vertrekken pijlen naar B en naar C.",
    )),
    met_prent(f"{GRAAF}.svg", mk(
        "Wat stelt de som van de getallen in één rij van de verbindingsmatrix voor?",
        [
            "Het aantal pijlen dat in dat depot aankomt",
            "Het totale aantal pijlen van de graaf",
            "Het aantal pijlen dat uit dat depot vertrekt",
            "Het aantal wegen van twee stappen",
        ],
        2,
        "Een rij hoort bij het vertrekpunt: elke 1 is een pijl die daar vertrekt.",
    )),
    mk(
        "A is een 2×3-matrix en B een 3×4-matrix. Wat is de dimensie van AB?",
        ["3×3", "2×4", "4×2", "AB bestaat niet"],
        1,
        "Het aantal kolommen van A moet gelijk zijn aan het aantal rijen van B. Het product krijgt de rijen van A en de kolommen van B.",
    ),
    mk(
        "P is een 3×2-matrix en Q een 2×2-matrix. Welk product bestaat niet?",
        [r"\(PQ\)", r"\(Q^2\)", r"\(QP\)", r"\(P^T P\)"],
        2,
        "QP: Q heeft 2 kolommen, P heeft 3 rijen. Dat past niet.",
    ),
    inv(
        r"Wat is het element op rij 2, kolom 1 van \(" + m([1, 2], [3, 4]) + r" \cdot " + m([2, 0], [1, 1]) + r"\)?",
        "10",
        r"Rij 2 van de eerste matrix maal kolom 1 van de tweede: \(3 \cdot 2 + 4 \cdot 1\).",
    ),
    mk(
        r"Bereken \(" + m([1, 2], [0, 1]) + r" \cdot " + m([1, 0], [3, 1]) + r"\).",
        [r"\(" + m([1, 0], [0, 1]) + r"\)", r"\(" + m([7, 2], [3, 1]) + r"\)", r"\(" + m([1, 2], [3, 7]) + r"\)", r"\(" + m([1, 0], [3, 1]) + r"\)"],
        1,
        r"Rij maal kolom: \(1 + 6 = 7\), \(0 + 2 = 2\), \(0 + 3 = 3\), \(0 + 1 = 1\).",
    ),
    mk(
        r"Wat is \(A^T\) als \(A = " + m([2, 0, -1], [5, 3, 7]) + r"\)?",
        [r"\(" + m([2, 5], [0, 3], [-1, 7]) + r"\)", r"\(" + m([7, 3, 5], [-1, 0, 2]) + r"\)", r"\(" + m([5, 3, 7], [2, 0, -1]) + r"\)", r"\(" + m([2, 0], [-1, 5], [3, 7]) + r"\)"],
        0,
        "Rijen worden kolommen.",
    ),
    mk(
        r"Bereken \(3 \cdot " + m([1, -2], [0, 4]) + r"\).",
        [r"\(" + m([3, -2], [0, 4]) + r"\)", r"\(" + m([4, 1], [3, 7]) + r"\)", r"\(" + m([3, -6], [0, 12]) + r"\)", r"\(" + m([3, 6], [0, 12]) + r"\)"],
        2,
        "Elk element maal 3.",
    ),
    tabel(
        "Juist of fout over rekenen met matrices?",
        [
            ("Voor matrices geldt altijd AB = BA.", F),
            (r"\((A + B)^T = A^T + B^T\)", J),
            ("Voor de eenheidsmatrix I geldt AI = A (als het product bestaat).", J),
            ("Je kan elke twee matrices bij elkaar optellen.", F),
        ],
        "Het matrixproduct is meestal niet commutatief. Optellen kan enkel bij dezelfde dimensie.",
    ),
    keuze(
        "Een matrix met evenveel rijen als kolommen heet een [[*vierkante|symmetrische|diagonaal]]matrix. Een matrix waarvoor A = Aᵀ heet [[*symmetrisch|vierkant|leeg]].",
        "Bij een symmetrische matrix is de hoofddiagonaal een spiegelas.",
    ),
    sorteer(
        "A is 2×3, B is 3×3 en C is 2×3. Bestaat de bewerking?",
        ["Bestaat", "Bestaat niet"],
        [
            [r"\(AB\)", "Bestaat"],
            [r"\(BA\)", "Bestaat niet"],
            [r"\(A + C\)", "Bestaat"],
            [r"\(A + B\)", "Bestaat niet"],
            [r"\(A C^T\)", "Bestaat"],
            [r"\(A^2\)", "Bestaat niet"],
        ],
        "Optellen: dezelfde dimensie. Vermenigvuldigen: kolommen van de eerste = rijen van de tweede.",
    ),
    mk(
        r"Bereken \(" + m([1, 1], [0, 1]) + r"^2\).",
        [r"\(" + m([1, 1], [0, 1]) + r"\)", r"\(" + m([1, 2], [0, 1]) + r"\)", r"\(" + m([2, 2], [0, 2]) + r"\)", r"\(" + m([1, 1], [0, 0]) + r"\)"],
        1,
        "Vermenigvuldig de matrix met zichzelf, rij maal kolom. Je mag niet elk element apart kwadrateren.",
    ),
    mk(
        "Van de klanten van merk X blijft 80 % trouw, 20 % stapt over naar Y. Van Y blijft 70 %, 30 % stapt over naar X. Nu heeft elk merk de helft van de klanten. Welk aandeel heeft X volgend jaar?",
        [r"\(50\) %", r"\(80\) %", r"\(55\) %", r"\(60\) %"],
        2,
        r"\(0{,}5 \cdot 0{,}8 + 0{,}5 \cdot 0{,}3 = 0{,}55\).",
    ),
    mk(
        "Bij dezelfde overstap (X houdt 80 %, Y verliest 30 % aan X): welk aandeel heeft X in de evenwichtstoestand?",
        [r"\(55\) %", r"\(50\) %", r"\(40\) %", r"\(60\) %"],
        3,
        r"In evenwicht verandert x niet: \(x = 0{,}8x + 0{,}3(1 - x)\), dus \(0{,}5x = 0{,}3\).",
    ),
    mk(
        r"Een populatie heeft twee leeftijdsklassen. Lesliematrix \(L = " + m([0, 2], ["0{,}5", 0]) + r"\) (rij 1: jongen per dier, rij 2: overleving). Nu zijn er 100 jonge en 40 oude dieren. Hoeveel zijn er na één periode?",
        ["80 jonge en 50 oude", "100 jonge en 40 oude", "200 jonge en 20 oude", "50 jonge en 80 oude"],
        0,
        r"\(L \cdot \begin{bmatrix} 100 \\ 40 \end{bmatrix} = \begin{bmatrix} 0 \cdot 100 + 2 \cdot 40 \\ 0{,}5 \cdot 100 + 0 \cdot 40 \end{bmatrix}\).",
    ),
    volgorde(
        "Zet de stappen van Gauss-Jordan in de goede volgorde.",
        [
            "Schrijf de uitgebreide coëfficiëntenmatrix",
            "Maak met rijoperaties nullen onder de eerste spil",
            "Werk verder tot de rijcanonieke vorm",
            "Lees de oplossing af en noteer ze",
        ],
        "Eerst de matrix, dan rijoperaties, dan aflezen.",
    ),
    mk(
        r"Los op: \(x + y + z = 6\), \(y + z = 5\), \(z = 3\).",
        [r"\((3, 2, 1)\)", r"\((1, 3, 2)\)", r"\((6, 5, 3)\)", r"\((1, 2, 3)\)"],
        3,
        r"Van onder naar boven: \(z = 3\), \(y = 2\), \(x = 1\).",
    ),
    mk(
        r"Een stelsel heeft rijcanonieke matrix \(" + um([1, 0, 2, 3], [0, 1, -1, 1], [0, 0, 0, 0], k=1) + r"\). Wat voor stelsel is het?",
        ["Bepaald: één oplossing", "Strijdig: geen oplossing", "Onbepaald: oneindig veel oplossingen", "Dat kan je niet zeggen"],
        2,
        "Er zijn drie onbekenden maar maar twee spillen, en geen strijdige rij. z blijft vrij te kiezen.",
    ),
    mk(
        r"Een stelsel heeft als matrix na rijoperaties \(" + um([1, 2, 3], [0, 0, 4], k=1) + r"\). Wat besluit je?",
        ["Het stelsel is bepaald", "Het stelsel is onbepaald", "Het stelsel is strijdig", "y = 4"],
        2,
        r"De tweede rij zegt \(0x + 0y = 4\): dat kan nooit.",
    ),
    koppel(
        "Koppel de bijzondere matrix aan haar kenmerk.",
        [
            ["Nulmatrix", "Alle elementen zijn 0"],
            ["Eenheidsmatrix", "Enen op de hoofddiagonaal, elders nullen"],
            ["Diagonaalmatrix", "Buiten de hoofddiagonaal staan enkel nullen"],
            ["Rijmatrix", "Ze heeft maar één rij"],
        ],
        ["Alle elementen zijn 1"],
        "Elke naam zegt wat er bijzonder is aan de elementen of aan de vorm.",
    ),
    sleep(
        "Bij Gauss-Jordan mag je twee rijen [[verwisselen]], een rij vermenigvuldigen met een getal verschillend van [[nul]], en bij een rij een [[veelvoud]] van een andere rij optellen.",
        ["kolom", "één", "kwadraat"],
        "Zo verandert de oplossingenverzameling niet.",
    ),
    inv(
        "Elk jaar verhuist 10 % van de inwoners van stad A naar stad B en 5 % van B naar A. Nu wonen er 20 000 mensen in A en 10 000 in B. Hoeveel wonen er na één jaar in A?",
        "18500",
        r"\(0{,}9 \cdot 20\,000 + 0{,}05 \cdot 10\,000 = 18\,000 + 500\).",
    ),
    open_(
        "M is de verbindingsmatrix van een graaf. Leg uit wat het getal op rij i en kolom j van M² betekent.",
        "Het is het aantal wegen van precies twee stappen van i naar j. Bij het berekenen tel je voor elke tussenknoop k het product 'pijl i → k' maal 'pijl k → j' op, en elk product is 1 als beide pijlen bestaan.",
        "Rij maal kolom loopt over alle tussenstops.",
    ),
    mk(
        r"Los op: \(" + m([2, 1], [1, 1]) + r" \cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}\).",
        [r"\(x = 1,\ y = 2\)", r"\(x = 2,\ y = 1\)", r"\(x = 3,\ y = 0\)", r"\(x = 5,\ y = 3\)"],
        1,
        r"\(2x + y = 5\) en \(x + y = 3\). Aftrekken: \(x = 2\).",
    ),
    mk(
        "In een overgangsmatrix van een Markovketen staan in elke kolom de kansen om vanuit één toestand naar elke toestand te gaan. Wat geldt dan voor elke kolom?",
        ["De som is 0", "De som is 1", "Er staat juist één 1 in", "De elementen zijn gelijk"],
        1,
        "Vanuit een toestand ga je zeker ergens naartoe: de kansen samen zijn 1.",
    ),
    casus(
        "Een atelier maakt tafels en stoelen. Een tafel vraagt 2 uur zagen en 1 uur schilderen, een stoel 1 uur zagen en 1 uur schilderen. Deze week is er 100 uur zagen en 70 uur schilderen, en alles wordt gebruikt. Noem t het aantal tafels en s het aantal stoelen.",
        [
            mk(
                "Welk stelsel past bij deze situatie?",
                [r"\(2t + s = 70\), \(t + s = 100\)", r"\(2t + s = 100\), \(t + s = 70\)", r"\(t + 2s = 100\), \(t + s = 70\)", r"\(2t + 2s = 170\)"],
                1,
                "Zaaguren: 2 per tafel en 1 per stoel. Schilderuren: 1 per tafel en 1 per stoel.",
            ),
            mk(
                "Welke uitgebreide coëfficiëntenmatrix hoort bij dat stelsel?",
                [r"\(" + um([2, 1, 100], [1, 1, 70], k=1) + r"\)", r"\(" + um([2, 1, 70], [1, 1, 100], k=1) + r"\)", r"\(" + um([1, 2, 100], [1, 1, 70], k=1) + r"\)", r"\(" + um([2, 1, 1], [1, 100, 70], k=1) + r"\)"],
                0,
                "Per rij: de coëfficiënten van t en s, en na de streep het rechterlid.",
            ),
            mk(
                "Hoeveel tafels en stoelen maakt het atelier?",
                ["40 tafels en 30 stoelen", "35 tafels en 35 stoelen", "30 tafels en 40 stoelen", "50 tafels en 20 stoelen"],
                2,
                r"Eerste rij min tweede: \(t = 30\). Dan \(s = 70 - 30\).",
            ),
        ],
    ),
]
