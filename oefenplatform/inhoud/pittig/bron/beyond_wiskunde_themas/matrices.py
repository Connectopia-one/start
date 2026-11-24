"""Matrices en hun bewerkingen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_lijn, DONKER

MAT = "matrices-drie-bij-vier-bey"
_M = [[2, -1, 0, 5], [4, 3, 7, -2], [1, 6, -3, 8]]


def _plek(i, j):
    return 340 + j * 130, 200 + i * 110


def _matrix():
    d = [s_tekst(170, 322, "M =", 40, vet=True)]
    # haken
    for x, r in ((265, 1), (735, -1)):
        d.append(s_lijn(x, 130, x, 490, kleur=DONKER, dikte=4))
        d.append(s_lijn(x, 130, x + 22 * r, 130, kleur=DONKER, dikte=4))
        d.append(s_lijn(x, 490, x + 22 * r, 490, kleur=DONKER, dikte=4))
    for i, rij in enumerate(_M):
        for j, v in enumerate(rij):
            x, y = _plek(i, j)
            d.append(s_tekst(x, y + 13, str(v).replace("-", "−"), 38, vet=True))
    return d


def _zone(i, j):
    x, y = _plek(i - 1, j - 1)
    return pix_zone(x - 55, y - 45, 110, 90)


GRAFIEKEN = [dict(naam=MAT, titel="Een matrix M met 3 rijen en 4 kolommen", eigen=_matrix)]
PRENTEN = [dict(bestand=f"{MAT}.svg", zelf=True, wat="matrix van 3 bij 4 met gehele getallen", vragen="klikvragen over de plaats van elementen")]

VRAGEN = [
    klik(
        r"Klik op het element \(m_{23}\).",
        f"{MAT}.svg",
        [_zone(2, 3)],
        r"Eerst de rij, dan de kolom: rij 2, kolom 3.",
    ),
    klik(
        r"Klik op het element van \(M\) dat in \(M^{T}\) op plaats \((1, 3)\) staat.",
        f"{MAT}.svg",
        [_zone(3, 1)],
        r"Transponeren wisselt rij en kolom: \((M^{T})_{13} = m_{31}\).",
    ),
    met_prent(f"{MAT}.svg", tabel(
        "Kijk naar de matrix M. Juist of fout?",
        [(r"\(M\) heeft dimensie \(3 \times 4\).", J), (r"\(M^{T}\) heeft dimensie \(3 \times 4\).", F), (r"Het product \(M \cdot M\) bestaat.", F), (r"Het product \(M \cdot M^{T}\) bestaat en is een \(3 \times 3\)-matrix.", J), (r"\(M\) heeft een determinant.", F)],
        "Enkel vierkante matrices hebben een determinant; bij M · M klopt het aantal kolommen niet met het aantal rijen.",
        kolommen=["Juist", "Fout"],
    )),
    casus(
        r"Neem \(A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\) en \(B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\).",
        [
            mk(r"Wat is \(A \cdot B\)?", [r"\(\begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}\)", r"\(\begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}\)", r"\(\begin{pmatrix} 0 & 2 \\ 3 & 0 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}\)"], 0, "Rechts vermenigvuldigen met B wisselt de kolommen."),
            mk(r"Wat is \(B \cdot A\)?", [r"\(\begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}\)", r"\(\begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}\)", r"\(\begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\)"], 0, "Links vermenigvuldigen met B wisselt de rijen."),
            mk("Wat toont dit?", ["dat het matrixproduct niet commutatief is", "dat B de eenheidsmatrix is, want ze heeft enen", "dat A niet inverteerbaar is, want det A < 0", "dat A symmetrisch is omdat ze vierkant is"], 0, "AB en BA zijn verschillend."),
        ],
    ),
    mk(
        r"Wat is \(\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}^{5}\)?",
        [r"\(\begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 5 & 5 \\ 0 & 5 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 & 32 \\ 0 & 1 \end{pmatrix}\)"],
        0,
        r"Het kwadraat is \(\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\); bij elke vermenigvuldiging komt er 1 bij rechtsboven.",
    ),
    mk(
        r"Wat is de inverse van \(\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\)?",
        [r"\(\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\)", r"\(\begin{pmatrix} -3 & 1 \\ 5 & -2 \end{pmatrix}\)", r"\(\begin{pmatrix} \tfrac{1}{2} & 1 \\ \tfrac{1}{5} & \tfrac{1}{3} \end{pmatrix}\)", r"\(\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}\)"],
        0,
        r"De determinant is \(6 - 5 = 1\). Wissel de diagonaal en verander het teken van de andere twee.",
    ),
    inv(
        r"Bereken \(\det\begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 0 & 1 & 4 \end{pmatrix}\).",
        ["21", "eenentwintig"],
        r"Ontwikkel naar rij 1: \(2(12 - 2) - 0 + 1(1 - 0)\).",
    ),
    tabel(
        r"\(A\) en \(B\) zijn \(2 \times 2\)-matrices met \(\det A = 3\) en \(\det B = -2\). Wat is de determinant?",
        [(r"\(\det(AB)\)", "−6"), (r"\(\det(2A)\)", "12"), (r"\(\det(A^{T})\)", "3"), (r"\(\det(A^{-1})\)", "1/3")],
        r"\(\det(AB) = \det A \cdot \det B\) en \(\det(kA) = k^{2}\det A\) bij orde 2.",
        kolommen=["−6", "12", "3", "1/3"],
    ),
    inv(
        r"Voor welke \(k\) is \(\begin{pmatrix} 1 & 2 \\ 3 & k \end{pmatrix}\) niet inverteerbaar?",
        ["6", "zes"],
        r"\(\det = k - 6 = 0\).",
    ),
    mk(
        r"Wat is de rang van \(\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}\)?",
        ["1", "2", "3", "0"],
        0,
        "De tweede rij is twee keer de eerste: na een rijoperatie blijft er één rij over die niet nul is.",
    ),
    casus(
        r"Een bakker verkoopt broden aan 5 euro en koffiekoeken aan 2 euro. Klant 1 koopt 2 broden en 3 koffiekoeken, klant 2 koopt 1 brood en 4 koffiekoeken.",
        [
            mk("Welke matrix zet je links in het product?", [r"\(\begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix}\)", r"\(\begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}\)", r"\(\begin{pmatrix} 5 & 2 \end{pmatrix}\)", r"\(\begin{pmatrix} 5 \\ 2 \end{pmatrix}\)"], 0, "Elke rij is een klant, elke kolom een product."),
            inv("Hoeveel betaalt klant 1, in euro?", ["16", "zestien"], r"\(2 \cdot 5 + 3 \cdot 2\)."),
            inv("Hoeveel betaalt klant 2, in euro?", ["13", "dertien"], r"\(1 \cdot 5 + 4 \cdot 2\)."),
        ],
    ),
    tabel(
        r"Voor vierkante matrices \(A\) en \(B\) van dezelfde orde: juist of fout?",
        [(r"\((A + B)^{2} = A^{2} + 2AB + B^{2}\)", F), (r"\((AB)^{T} = B^{T}A^{T}\)", J), (r"\(A + B = B + A\)", J), (r"\((AB)^{-1} = A^{-1}B^{-1}\)", F), (r"\(A \cdot I = A\)", J)],
        r"\((A + B)^{2} = A^{2} + AB + BA + B^{2}\), en \(AB\) is niet altijd \(BA\). Bij inverse en getransponeerde keert de volgorde om.",
        kolommen=["Juist", "Fout"],
    ),
    sorteer(
        "Bestaat het product?",
        ["Bestaat", "Bestaat niet"],
        [(r"\((2 \times 3) \cdot (3 \times 1)\)", "Bestaat"), (r"\((2 \times 3) \cdot (2 \times 3)\)", "Bestaat niet"), (r"\((1 \times 4) \cdot (4 \times 1)\)", "Bestaat"),
         (r"\((4 \times 1) \cdot (1 \times 4)\)", "Bestaat"), (r"\((3 \times 2) \cdot (3 \times 2)\)", "Bestaat niet"), (r"\((3 \times 3) \cdot (2 \times 3)\)", "Bestaat niet")],
        "Het aantal kolommen links moet gelijk zijn aan het aantal rijen rechts.",
    ),
    tabel(
        "Welke dimensie heeft het product?",
        [(r"\((2 \times 3) \cdot (3 \times 5)\)", r"\(2 \times 5\)"), (r"\((1 \times 4) \cdot (4 \times 1)\)", r"\(1 \times 1\)"), (r"\((4 \times 1) \cdot (1 \times 4)\)", r"\(4 \times 4\)")],
        "De buitenste getallen blijven over.",
        kolommen=[r"\(2 \times 5\)", r"\(1 \times 1\)", r"\(4 \times 4\)"],
    ),
    koppel(
        "Verbind de matrix met haar naam.",
        [(r"\(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\)", "eenheidsmatrix"), (r"\(\begin{pmatrix} 3 & 0 \\ 0 & -2 \end{pmatrix}\)", "diagonaalmatrix"), (r"\(\begin{pmatrix} 1 & 4 \\ 4 & 2 \end{pmatrix}\)", "symmetrische matrix"), (r"\(\begin{pmatrix} 1 \\ 5 \\ 2 \end{pmatrix}\)", "kolommatrix")],
        ["nulmatrix"],
        "Een eenheidsmatrix is ook een diagonaalmatrix, maar met enen op de diagonaal.",
    ),
    mk(
        r"Wat is de inverse van \(\begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}\)?",
        [r"\(\begin{pmatrix} \tfrac{1}{2} & 0 \\ 0 & \tfrac{1}{5} \end{pmatrix}\)", r"\(\begin{pmatrix} -2 & 0 \\ 0 & -5 \end{pmatrix}\)", r"\(\begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}\)", r"\(\begin{pmatrix} 0 & \tfrac{1}{2} \\ \tfrac{1}{5} & 0 \end{pmatrix}\)"],
        0,
        "Bij een diagonaalmatrix neem je het omgekeerde van elk diagonaalelement.",
    ),
    keuze(
        r"Als \(\det A = 0\), dan is \(A\) [[*niet inverteerbaar|inverteerbaar]] en is de rang [[*kleiner dan|gelijk aan]] de orde.",
        "Determinant nul, rang en inverteerbaarheid hangen samen.",
    ),
    volgorde(
        r"Zet de stappen om \(A^{-1}\) te vinden met rijoperaties in volgorde.",
        [r"schrijf \(\left(A \mid I\right)\)", "maak met rijoperaties links de eenheidsmatrix", r"lees rechts \(A^{-1}\) af", r"controleer met \(A \cdot A^{-1} = I\)"],
        "Wat je met A doet, doe je tegelijk met I.",
    ),
    inv(
        r"Bereken \(\det\begin{pmatrix} 3 & 7 & -1 \\ 0 & 2 & 5 \\ 0 & 0 & 4 \end{pmatrix}\).",
        ["24", "vierentwintig"],
        r"Bij een bovendriehoeksmatrix is de determinant het product van de diagonaal: \(3 \cdot 2 \cdot 4\).",
    ),
    tabel(
        "Juist of fout?",
        [(r"Twee rijen van plaats wisselen verandert het teken van de determinant.", J), (r"Een veelvoud van een rij bij een andere optellen verandert de determinant niet.", J), (r"Een rij met 3 vermenigvuldigen maakt de determinant 3 keer zo groot.", J), (r"Een matrix met een rij nullen kan determinant 1 hebben.", F)],
        "Ontwikkel naar de rij met nullen: dan is de determinant 0.",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"De cofactor is \(C_{ij} = (-1)^{i+j}\) maal de [[minor]]. Bij \(C_{12}\) is het teken [[min]].",
        ["rang", "plus"],
        r"\((-1)^{1 + 2} = -1\).",
    ),
    mk(
        r"\(A\) is een \(3 \times 3\)-matrix met \(\det A = 2\). Hoeveel is \(\det(3A)\)?",
        ["54", "6", "18", "8"],
        0,
        r"Elke rij wordt met 3 vermenigvuldigd: \(3^{3} \cdot 2\).",
    ),
    inv(
        r"Bereken \(\begin{pmatrix} 1 & 2 & 3 \end{pmatrix} \cdot \begin{pmatrix} 4 \\ 0 \\ -1 \end{pmatrix}\). Schrijf het getal.",
        ["1", "een", "één"],
        r"\(4 + 0 - 3\).",
    ),
    mk(
        r"Er geldt \(A \cdot B = O\) met \(A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\). Welke \(B\) kan dat geven?",
        [r"\(\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\)", r"\(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\)"],
        0,
        "Elke kolom van B moet optellen tot nul. Zo zie je dat AB = O kan zonder dat A of B nul is.",
    ),
    met_prent(f"{MAT}.svg", inv(
        r"Bereken het element op plaats \((1, 1)\) van \(M \cdot M^{T}\).",
        ["30", "dertig"],
        r"Rij 1 van M maal kolom 1 van \(M^{T}\), en dat is weer rij 1 van M: \(4 + 1 + 0 + 25\).",
    )),
    mk(
        "Welke bewerking is geen toegelaten rijoperatie?",
        [r"\(R_{1} \to 0 \cdot R_{1}\)", r"\(R_{1} \leftrightarrow R_{2}\)", r"\(R_{2} \to R_{2} - 3R_{1}\)", r"\(R_{3} \to -R_{3}\)"],
        0,
        "Vermenigvuldigen met 0 gooit informatie weg; de factor moet verschillen van 0.",
    ),
]
