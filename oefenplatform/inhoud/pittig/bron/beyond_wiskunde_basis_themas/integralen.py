"""Bedrijfswetenschappen: integralen en oppervlakte — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, vak_zone

R_GRAF = venster("integralen-riemann", 0, 4.4, 0, 10, 0.5, 1)
T_GRAF = venster("integralen-twee-krommen", -0.5, 4.5, -1, 5, 0.5, 0.5)
O_GRAF = venster("integralen-georienteerd", -0.5, 3.5, -5, 6, 0.5, 1)


def _r(x):
    return 0.5 * x * x + 1


def _f(x):
    return -x * x + 4 * x


def _g(x):
    return x


def _o(x):
    return x * x - 4


GRAFIEKEN = [
    dict(naam=R_GRAF, titel="De grafiek van f(x) = 0,5x² + 1 met vier rechthoeken",
         staven=[(k, 1, _r(k)) for k in range(4)],
         krommen=[(_r, "groen", "", (0, 4.3))], ijk_x=1, ijk_y=1),
    dict(naam=T_GRAF, titel="f(x) = −x² + 4x en g(x) = x",
         vlakken=[(_f, 0, 3, "#7a4b8c", _g)],
         krommen=[(_f, "groen", "f", (-0.3, 4.2)), (_g, "blauw", "g", (-0.5, 4.5))],
         labelplek={"f": (3.9, _f(3.9)), "g": (4.3, 4.3)}, ijk_x=1, ijk_y=1),
    dict(naam=O_GRAF, titel="f(x) = x² − 4 op [0, 3]",
         vlakken=[(_o, 0, 3, "#3b6fa0")],
         krommen=[(_o, "blauw", "", (-0.5, 3.3))], ijk_x=1, ijk_y=1),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over integralen en oppervlakte") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        r"Klik op de rechthoek die hoort bij het deelinterval \([2, 3]\).",
        f"{R_GRAF}.svg",
        [vak_zone(R_GRAF, 2, 3, 0, _r(2))],
        r"Elke rechthoek heeft breedte 1. Die boven \([2, 3]\) heeft hoogte \(f(2) = 3\).",
    ),
    met_prent(f"{R_GRAF}.svg", mk(
        "Is de som van de oppervlaktes van deze rechthoeken een ondersom of een bovensom?",
        ["Een bovensom", "Een ondersom", "Geen van beide", "Allebei"],
        1,
        "f stijgt en elke rechthoek neemt de hoogte links in het deelinterval: de kleinste functiewaarde. Alle rechthoeken liggen onder de grafiek.",
    )),
    met_prent(f"{R_GRAF}.svg", inv(
        "Bereken de som van de oppervlaktes van de vier rechthoeken.",
        "11",
        r"\(1 \cdot (f(0) + f(1) + f(2) + f(3)) = 1 + 1{,}5 + 3 + 5{,}5\).",
    )),
    klik(
        "Klik in het gebied dat ingesloten wordt door de grafieken van f en g.",
        f"{T_GRAF}.svg",
        [vak_zone(T_GRAF, 1, 2, 2.1, 2.9)],
        r"f en g snijden elkaar in \(x = 0\) en \(x = 3\). Daartussen ligt f boven g.",
    ),
    met_prent(f"{T_GRAF}.svg", mk(
        "Welke integraal geeft de gekleurde oppervlakte?",
        [r"\(\displaystyle\int_0^4 (-x^2 + 4x)\,dx\)", r"\(\displaystyle\int_0^3 (-x^2 + 5x)\,dx\)", r"\(\displaystyle\int_0^3 (-x^2 + 3x)\,dx\)", r"\(\displaystyle\int_0^3 (x^2 - 3x)\,dx\)"],
        2,
        r"Bovenste min onderste kromme, tussen de snijpunten: \(\int_0^3 \left((-x^2 + 4x) - x\right) dx\).",
    )),
    met_prent(f"{O_GRAF}.svg", mk(
        r"Hoeveel is \(\displaystyle\int_0^3 (x^2 - 4)\,dx\)?",
        [r"\(\dfrac{23}{3}\)", r"\(3\)", r"\(-\dfrac{16}{3}\)", r"\(-3\)"],
        3,
        r"\(\left[\frac{x^3}{3} - 4x\right]_0^3 = 9 - 12\). Het stuk onder de x-as telt negatief.",
    )),
    met_prent(f"{O_GRAF}.svg", mk(
        "Hoe groot is de werkelijke oppervlakte van het gekleurde gebied?",
        [r"\(\dfrac{23}{3}\)", r"\(3\)", r"\(\dfrac{16}{3}\)", r"\(\dfrac{7}{3}\)"],
        0,
        r"Splits bij de nulwaarde 2. Onder de x-as: \(\frac{16}{3}\). Erboven: \(\frac{7}{3}\). Samen \(\frac{23}{3} \approx 7{,}67\).",
    )),
    mk(
        r"Welke functie is een primitieve van \(f(x) = 6x^2 - 4x + 3\)?",
        [r"\(12x - 4\)", r"\(2x^3 - 2x^2 + 3x\)", r"\(6x^3 - 4x^2 + 3x\)", r"\(2x^3 - 4x^2 + 3\)"],
        1,
        r"Leid af ter controle: \((2x^3 - 2x^2 + 3x)' = 6x^2 - 4x + 3\).",
    ),
    mk(
        r"\(\displaystyle\int (x^3 - 2)\,dx = \dots\)",
        [r"\(3x^2 + C\)", r"\(\dfrac{x^4}{4} - 2 + C\)", r"\(\dfrac{x^4}{4} - 2x + C\)", r"\(x^4 - 2x + C\)"],
        2,
        r"\(\int x^n dx = \frac{x^{n+1}}{n+1} + C\) en \(\int 2\,dx = 2x + C\).",
    ),
    inv(
        r"Bereken \(\displaystyle\int_1^3 2x\,dx\).",
        "8",
        r"\(\left[x^2\right]_1^3 = 9 - 1\).",
    ),
    tabel(
        "Juist of fout over primitieven en integralen?",
        [
            ("Twee primitieven van dezelfde functie verschillen hoogstens een constante.", J),
            (r"Een primitieve van \(x^2\) is \(2x\).", F),
            (r"\(\displaystyle\int_a^a f(x)\,dx = 0\)", J),
            (r"Als \(f(x) \geq 0\) op \([a, b]\) met \(a < b\), kan \(\int_a^b f(x)\,dx\) negatief zijn.", F),
        ],
        r"\(2x\) is de afgeleide van \(x^2\), een primitieve is \(\frac{x^3}{3}\). Een interval zonder breedte geeft oppervlakte 0, en boven de x-as is de oppervlakte positief.",
    ),
    keuze(
        "In de integraal van 1 tot 4 van (2x + 5) dx is 2x + 5 de [[*integrand|primitieve|grens]], en 1 en 4 zijn de [[*integratiegrenzen|nulwaarden|coëfficiënten]].",
        "De integrand staat tussen het integraalteken en dx.",
    ),
    sorteer(
        "Is de bepaalde integraal positief, negatief of nul?",
        ["Positief", "Negatief", "Nul"],
        [
            [r"\(\int_0^2 x^2\,dx\)", "Positief"],
            [r"\(\int_{-1}^0 x^2\,dx\)", "Positief"],
            [r"\(\int_0^1 (x - 2)\,dx\)", "Negatief"],
            [r"\(\int_1^3 (-x)\,dx\)", "Negatief"],
            [r"\(\int_{-1}^1 x\,dx\)", "Nul"],
            [r"\(\int_{-2}^2 x^3\,dx\)", "Nul"],
        ],
        "Kijk waar de grafiek boven en onder de x-as ligt. Bij x en x³ op een symmetrisch interval heffen beide stukken elkaar op.",
    ),
    volgorde(
        "Zet de stappen om de werkelijke oppervlakte tussen een grafiek en de x-as te berekenen in de goede volgorde.",
        [
            "Zoek de nulwaarden van f in het interval",
            "Splits de integraal bij die nulwaarden",
            "Bereken elke deelintegraal met een primitieve",
            "Tel de absolute waarden van de deelintegralen op",
        ],
        "Stukken onder de x-as tellen anders negatief.",
    ),
    koppel(
        "Koppel de integraal aan haar betekenis in de context.",
        [
            ["De integraal van de snelheid naar de tijd", "De afgelegde weg"],
            ["De integraal van het debiet naar de tijd", "De hoeveelheid water die erbij kwam"],
            ["De integraal van de marginale kost naar q", "De variabele kost"],
            ["De integraal van de groeisnelheid van een plant naar de tijd", "De toename in hoogte"],
        ],
        ["De gemiddelde snelheid"],
        "Een integraal telt kleine veranderingen op tot een totaal.",
    ),
    mk(
        r"Een voorwerp heeft snelheid \(v(t) = 3t^2\) m/s. Welke afstand legt het af van \(t = 0\) tot \(t = 4\)?",
        [r"\(48\) m", r"\(24\) m", r"\(64\) m", r"\(192\) m"],
        2,
        r"\(\int_0^4 3t^2\,dt = \left[t^3\right]_0^4\).",
    ),
    mk(
        r"De marginale kost is \(K'(q) = 0{,}6q + 20\) euro per stuk. De vaste kost is 500 euro. Wat is de totale kost voor 100 stuks?",
        [r"\(5000\) euro", r"\(80\) euro", r"\(3500\) euro", r"\(5500\) euro"],
        3,
        r"\(\int_0^{100} (0{,}6q + 20)\,dq = \left[0{,}3q^2 + 20q\right]_0^{100} = 5000\), plus 500 euro vaste kost.",
    ),
    inv(
        r"Water stroomt in een vat met debiet \(d(t) = 40 - 2t\) liter per minuut, van \(t = 0\) tot \(t = 20\). Hoeveel liter stroomt er in totaal in?",
        "400",
        r"\(\int_0^{20} (40 - 2t)\,dt = \left[40t - t^2\right]_0^{20} = 800 - 400\).",
    ),
    sleep(
        "Hoe smaller de rechthoeken, hoe dichter de [[ondersom]] en de [[bovensom]] bij de bepaalde integraal komen. In de limiet worden ze [[gelijk]].",
        ["primitieve", "afgeleide", "nul"],
        "Zo is de bepaalde integraal gedefinieerd als limiet van sommen.",
    ),
    mk(
        r"Hoe groot is de oppervlakte tussen de grafieken van \(f(x) = x^2\) en \(g(x) = 2x\)?",
        [r"\(\dfrac{8}{3}\)", r"\(\dfrac{4}{3}\)", r"\(4\)", r"\(\dfrac{2}{3}\)"],
        1,
        r"Snijpunten in \(0\) en \(2\). \(\int_0^2 (2x - x^2)\,dx = 4 - \frac{8}{3}\).",
    ),
    mk(
        r"\(\int_0^2 f(x)\,dx = 5\) en \(\int_0^2 g(x)\,dx = 3\). Hoeveel is \(\int_0^2 \left(2f(x) - g(x)\right) dx\)?",
        [r"\(2\)", r"\(13\)", r"\(10\)", r"\(7\)"],
        3,
        r"Lineariteit: \(2 \cdot 5 - 3\).",
    ),
    mk(
        r"\(\int_0^5 f(x)\,dx = 10\) en \(\int_0^2 f(x)\,dx = 4\). Hoeveel is \(\int_2^5 f(x)\,dx\)?",
        [r"\(14\)", r"\(6\)", r"\(2{,}5\)", r"\(-6\)"],
        1,
        r"Splitsing: \(\int_0^5 = \int_0^2 + \int_2^5\).",
    ),
    open_(
        "Leg uit waarom je bij een bepaalde integraal geen integratieconstante C nodig hebt.",
        r"Je berekent \(F(b) - F(a)\). Een constante C komt in beide termen voor en valt weg: \((F(b) + C) - (F(a) + C) = F(b) - F(a)\).",
        "Kijk wat er met C gebeurt bij het aftrekken.",
    ),
    mk(
        r"F is een primitieve van \(f(x) = 2x\) met \(F(1) = 5\). Wat is \(F(x)\)?",
        [r"\(x^2 + 5\)", r"\(2x + 3\)", r"\(x^2 - 4\)", r"\(x^2 + 4\)"],
        3,
        r"\(F(x) = x^2 + C\) en \(1 + C = 5\).",
    ),
    mk(
        r"Bereken \(\displaystyle\int_{-1}^2 (3x^2 - 2x)\,dx\).",
        [r"\(2\)", r"\(4\)", r"\(10\)", r"\(6\)"],
        3,
        r"\(\left[x^3 - x^2\right]_{-1}^2 = (8 - 4) - (-1 - 1)\).",
    ),
    mk(
        r"Een fietser rijdt heen en terug met snelheid \(v(t) = 2t - 4\) m/s (\(0 \leq t \leq 4\)). \(\int_0^4 v(t)\,dt = 0\). Wat betekent dat?",
        [
            "De fietser stond de hele tijd stil",
            "De fietser is na 4 s terug op zijn vertrekpunt",
            "De fietser legde 0 m af",
            "De snelheid was altijd 0",
        ],
        1,
        r"De integraal geeft de verplaatsing: eerst 4 m achteruit (\(v < 0\)), dan 4 m vooruit. Afgelegd werd wel 8 m.",
    ),
    mk(
        r"Voor welke positieve a is \(\displaystyle\int_0^a 2x\,dx = 9\)?",
        [r"\(a = 9\)", r"\(a = 4{,}5\)", r"\(a = 3\)", r"\(a = 81\)"],
        2,
        r"\(\left[x^2\right]_0^a = a^2 = 9\).",
    ),
    casus(
        r"Een auto remt af met snelheid \(v(t) = 20 - 4t\) m/s, tot hij stilstaat.",
        [
            mk(
                "Na hoeveel seconden staat de auto stil?",
                [r"\(4\) s", r"\(5\) s", r"\(20\) s", r"\(10\) s"],
                1,
                r"\(20 - 4t = 0\).",
            ),
            mk(
                "Welke integraal geeft de remweg?",
                [r"\(\displaystyle\int_0^{20} (20 - 4t)\,dt\)", r"\(\displaystyle\int_0^5 (20 - 4t)\,dt\)", r"\(\displaystyle\int_0^5 -4\,dt\)", r"\(\displaystyle\int_0^5 (20t - 2t^2)\,dt\)"],
                1,
                "Integreer de snelheid van het begin van het remmen tot het stilstaan.",
            ),
            mk(
                "Hoe lang is de remweg?",
                [r"\(100\) m", r"\(25\) m", r"\(75\) m", r"\(50\) m"],
                3,
                r"\(\left[20t - 2t^2\right]_0^5 = 100 - 50\).",
            ),
        ],
    ),
]
