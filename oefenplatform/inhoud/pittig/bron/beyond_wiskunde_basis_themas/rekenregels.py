"""Bedrijfswetenschappen: afgeleiden berekenen met rekenregels — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

L_GRAF = venster("rekenregels-ln", 0, 5, -2, 2, 0.5, 0.5)
PUNTEN = {"A": 0.5, "B": 1, "C": 2, "D": 4}

GRAFIEKEN = [
    dict(naam=L_GRAF, titel="De grafiek van f(x) = ln x",
         krommen=[(math.log, "groen", "", (0.14, 5))],
         punten=[(x, math.log(x), n, *((True,) if n in "AB" else ())) for n, x in PUNTEN.items()], ijk_x=1, ijk_y=1),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over raaklijnen aan ln x") for g in GRAFIEKEN]


def _pz(n):
    return punt_zone(L_GRAF, PUNTEN[n], math.log(PUNTEN[n]), 30)


VRAGEN = [
    klik(
        r"Klik op het punt waar de raaklijn aan de grafiek evenwijdig is met \(y = 2x\).",
        f"{L_GRAF}.svg",
        [_pz("A")],
        r"Evenwijdig betekent richtingscoëfficiënt \(2\). \(f'(x) = \frac{1}{x} = 2\) geeft \(x = \frac{1}{2}\).",
    ),
    klik(
        r"Klik op het punt waar de raaklijn de vergelijking \(y = x - 1\) heeft.",
        f"{L_GRAF}.svg",
        [_pz("B")],
        r"Richtingscoëfficiënt \(1\) betekent \(\frac{1}{x} = 1\), dus \(x = 1\). Het raakpunt \((1, 0)\) ligt ook op \(y = x - 1\).",
    ),
    met_prent(f"{L_GRAF}.svg", mk(
        "Wat is de richtingscoëfficiënt van de raaklijn in D?",
        [r"\(4\)", r"\(\ln 4\)", r"\(\dfrac{1}{4}\)", r"\(2\)"],
        2,
        r"D heeft x-coördinaat \(4\), en \(f'(4) = \frac{1}{4}\).",
    )),
    mk(
        r"Wat is de afgeleide van \(f(x) = 2x^{-3}\)?",
        [r"\(-6x^{-2}\)", r"\(2x^{-4}\)", r"\(-6x^{-4}\)", r"\(-5x^{-4}\)"],
        2,
        r"\((x^n)' = n x^{n-1}\), ook voor negatieve n: \(2 \cdot (-3) x^{-4}\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = 4x^3 - \dfrac{x^2}{2} + 3x - 8\)?",
        [r"\(12x^2 - x + 3\)", r"\(12x^2 - x + 3 - 8\)", r"\(4x^2 - \dfrac{x}{2} + 3\)", r"\(12x^2 - 2x + 3\)"],
        0,
        r"Term per term: \(4 \cdot 3x^2 - \frac{2x}{2} + 3\). De constante valt weg.",
    ),
    inv(
        r"\(f(x) = x^3 - 5x\). Bereken \(f'(2)\).",
        "7",
        r"\(f'(x) = 3x^2 - 5\), dus \(f'(2) = 12 - 5 = 7\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = x^2 e^x\)?",
        [r"\(2x e^x\)", r"\((x^2 + 2x)e^x\)", r"\(x^2 e^x\)", r"\(2x e^{x-1}\)"],
        1,
        r"Productregel: \(2x \cdot e^x + x^2 \cdot e^x\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = \dfrac{2x + 1}{x - 3}\)?",
        [r"\(\dfrac{-7}{(x - 3)^2}\)", r"\(\dfrac{2}{1}\)", r"\(\dfrac{4x - 5}{(x - 3)^2}\)", r"\(\dfrac{7}{(x - 3)^2}\)"],
        0,
        r"Quotiëntregel: \(\frac{2(x - 3) - (2x + 1) \cdot 1}{(x - 3)^2} = \frac{-7}{(x - 3)^2}\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = (3x - 2)^5\)?",
        [r"\(5(3x - 2)^4\)", r"\(15(3x - 2)^4\)", r"\(15x^4\)", r"\(5 \cdot 3x^4\)"],
        1,
        r"Kettingregel: \(5(3x - 2)^4 \cdot 3\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = e^{2x}\)?",
        [r"\(e^{2x}\)", r"\(2x e^{2x-1}\)", r"\(2e^{2x}\)", r"\(e^2\)"],
        2,
        r"Kettingregel: \(e^{2x} \cdot (2x)' = 2e^{2x}\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = \ln(x^2 + 1)\)?",
        [r"\(\dfrac{1}{x^2 + 1}\)", r"\(\dfrac{2x}{x^2 + 1}\)", r"\(\dfrac{1}{2x}\)", r"\(2x \ln(x^2 + 1)\)"],
        1,
        r"\(\frac{1}{x^2 + 1} \cdot 2x\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = \dfrac{3}{x^2}\)?",
        [r"\(\dfrac{6}{x}\)", r"\(\dfrac{3}{2x}\)", r"\(-\dfrac{6}{x^3}\)", r"\(-\dfrac{3}{x^3}\)"],
        2,
        r"\(\frac{3}{x^2} = 3x^{-2}\), dus \(-6x^{-3}\).",
    ),
    tabel(
        "Juist of fout over de rekenregels?",
        [
            (r"\(f'(x)\), \(\dfrac{dy}{dx}\) en \(Df(x)\) duiden allemaal de afgeleide aan.", J),
            (r"\((f \cdot g)' = f' \cdot g'\)", F),
            (r"\((c \cdot f)' = c \cdot f'\) voor een constante c.", J),
            (r"\((f + g)' = f' \cdot g'\)", F),
        ],
        r"Bij een product heb je twee termen: \(f'g + fg'\). Bij een som tel je de afgeleiden op.",
    ),
    koppel(
        "Koppel de notatie aan de wiskundige naar wie ze genoemd is.",
        [
            [r"\(f'(x)\)", "Lagrange"],
            [r"\(\dfrac{dy}{dx}\)", "Leibniz"],
            [r"\(Df(x)\)", "Cauchy"],
        ],
        ["Laplace"],
        "Drie notaties voor dezelfde afgeleide.",
    ),
    sorteer(
        "Welke rekenregel heb je hier eerst nodig?",
        ["Productregel", "Quotiëntregel", "Kettingregel"],
        [
            [r"\(x^3 \ln x\)", "Productregel"],
            [r"\(x e^x\)", "Productregel"],
            [r"\(\dfrac{x + 1}{x^2 + 1}\)", "Quotiëntregel"],
            [r"\(\dfrac{\ln x}{x}\)", "Quotiëntregel"],
            [r"\((2x + 1)^4\)", "Kettingregel"],
            [r"\(e^{x^2}\)", "Kettingregel"],
        ],
        "Kijk naar de laatste bewerking: een product, een deling of een functie van een functie.",
    ),
    keuze(
        "De kettingregel zegt dat de afgeleide van f(g(x)) gelijk is aan [[*f′(g(x)) · g′(x)|f′(x) · g′(x)|f(g′(x))]]. De afgeleide van aˣ is [[*aˣ · ln a|x · aˣ⁻¹|aˣ]].",
        r"Eerst de buitenste functie afleiden, dan maal de afgeleide van de binnenste. \((a^x)' = a^x \ln a\).",
    ),
    volgorde(
        "Zet de stappen van de kettingregel in de goede volgorde.",
        [
            "Herken de buitenste en de binnenste functie",
            "Leid de buitenste functie af en laat de binnenste ongewijzigd staan",
            "Vermenigvuldig met de afgeleide van de binnenste functie",
            "Vereenvoudig het resultaat",
        ],
        "Van buiten naar binnen.",
    ),
    mk(
        r"Wat is de vergelijking van de raaklijn aan \(f(x) = x^2 - 3x\) in \(x = 1\)?",
        [r"\(y = -x - 1\)", r"\(y = -x - 2\)", r"\(y = 2x - 3\)", r"\(y = -x + 1\)"],
        0,
        r"\(f(1) = -2\), \(f'(x) = 2x - 3\), \(f'(1) = -1\). \(y + 2 = -(x - 1)\).",
    ),
    inv(
        r"\(f(x) = e^x (x - 1)\). Bereken \(f'(0)\).",
        "0",
        r"Productregel: \(f'(x) = e^x(x - 1) + e^x = x e^x\), dus \(f'(0) = 0\).",
    ),
    mk(
        r"De kosten om q stuks te maken zijn \(K(q) = 0{,}02q^2 + 5q + 200\) euro. Wat is de marginale kost bij \(q = 100\)?",
        [r"\(5\) euro per stuk", r"\(9{,}04\) euro per stuk", r"\(900\) euro", r"\(9\) euro per stuk"],
        3,
        r"\(K'(q) = 0{,}04q + 5\), dus \(K'(100) = 9\). Een extra stuk kost daar ongeveer 9 euro.",
    ),
    mk(
        r"Een populatie groeit volgens \(P(t) = 1000 e^{0{,}05t}\) (t in jaar). Hoe snel groeit ze op \(t = 0\)?",
        [r"\(1000\) per jaar", r"\(0{,}05\) per jaar", r"\(50\) per jaar", r"\(1050\) per jaar"],
        2,
        r"\(P'(t) = 1000 \cdot 0{,}05 e^{0{,}05t}\), dus \(P'(0) = 50\).",
    ),
    sleep(
        "Bij de productregel tel je [[twee]] termen op. Bij de quotiëntregel deel je door het [[kwadraat]] van de [[noemer]].",
        ["drie", "dubbel", "teller"],
        r"\((fg)' = f'g + fg'\) en \(\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}\).",
    ),
    tabel(
        "Juist of fout over afgeleiden van basisfuncties?",
        [
            (r"\((x^n)' = n x^{n-1}\) geldt ook voor \(n = -1\).", J),
            (r"\((\sqrt{x})' = \dfrac{1}{2\sqrt{x}}\)", J),
            (r"\((\ln 2x)' = \dfrac{1}{2x}\)", F),
            (r"\(\left(e^{x^2}\right)' = e^{x^2}\)", F),
        ],
        r"\(\sqrt{x} = x^{1/2}\). Kettingregel: \((\ln 2x)' = \frac{2}{2x} = \frac{1}{x}\) en \(\left(e^{x^2}\right)' = 2x e^{x^2}\).",
    ),
    open_(
        r"Leg uit hoe je met de kettingregel de afgeleide van \((x^2 + 1)^3\) vindt.",
        r"De buitenste functie is 'tot de derde', de binnenste is \(x^2 + 1\). Leid de buitenste af: \(3(x^2 + 1)^2\). Vermenigvuldig met de afgeleide van de binnenste: \(2x\). Resultaat: \(6x(x^2 + 1)^2\).",
        "Buitenste afleiden, binnenste laten staan, maal de afgeleide van de binnenste.",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = \dfrac{3x}{x^2 + 1}\)?",
        [r"\(\dfrac{3}{2x}\)", r"\(\dfrac{3 - 3x^2}{(x^2 + 1)^2}\)", r"\(\dfrac{9x^2 + 3}{(x^2 + 1)^2}\)", r"\(\dfrac{3x^2 - 3}{(x^2 + 1)^2}\)"],
        1,
        r"\(\frac{3(x^2 + 1) - 3x \cdot 2x}{(x^2 + 1)^2}\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = \dfrac{x^2 - 1}{x}\)?",
        [r"\(2x\)", r"\(1 - \dfrac{1}{x^2}\)", r"\(1 + \dfrac{1}{x^2}\)", r"\(\dfrac{2x - 1}{x^2}\)"],
        2,
        r"Splits eerst: \(x - \frac{1}{x}\). Afgeleide: \(1 + \frac{1}{x^2}\).",
    ),
    mk(
        r"Wat is de afgeleide van \(f(x) = \sqrt{4x + 1}\)?",
        [r"\(\dfrac{1}{2\sqrt{4x + 1}}\)", r"\(\dfrac{2}{\sqrt{4x + 1}}\)", r"\(2\sqrt{4x + 1}\)", r"\(\dfrac{4}{\sqrt{4x + 1}}\)"],
        1,
        r"\(\frac{1}{2\sqrt{4x + 1}} \cdot 4\).",
    ),
    casus(
        r"De winst van een bedrijf is \(W(q) = -0{,}5q^2 + 60q - 800\) euro, met q het aantal stuks per dag.",
        [
            mk(
                r"Wat is \(W'(q)\)?",
                [r"\(-q + 60\)", r"\(-0{,}5q + 60\)", r"\(-q + 60 - 800\)", r"\(-q^2 + 60\)"],
                0,
                r"\(-0{,}5 \cdot 2q + 60\). De constante valt weg.",
            ),
            mk(
                r"\(W'(40) = 20\). Wat betekent dat?",
                [
                    "Bij 40 stuks is de winst 20 euro",
                    "Bij 40 stuks levert één stuk extra ongeveer 20 euro extra winst op",
                    "Na 40 dagen is de winst met 20 % gestegen",
                    "Elk stuk levert 20 euro winst op",
                ],
                1,
                "De afgeleide is de ogenblikkelijke verandering: extra winst per extra stuk.",
            ),
            mk(
                r"Bij welke q is \(W'(q) = 0\)?",
                [r"\(40\)", r"\(80\)", r"\(60\)", r"\(120\)"],
                2,
                r"\(-q + 60 = 0\). Daar is de winst maximaal.",
            ),
        ],
    ),
]
