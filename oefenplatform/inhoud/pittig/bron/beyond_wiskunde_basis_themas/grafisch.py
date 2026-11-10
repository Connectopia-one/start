"""Grafisch onderzoek van een functie — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone, strook_zone

# f(x) = x³/4 − 3x op [−4, 4]: oneven, maximum 4 in −2, minimum −4 in 2
F_GRAF = venster("grafisch-f", -5, 5, -6, 6)
# g(x) = 2 + 3/(x − 1): asymptoten x = 1 en y = 2, nulwaarde −1/2
G_GRAF = venster("grafisch-g", -5, 7, -6, 10)
# T(u) = 12 − 6·cos(π(u − 3)/12): temperatuur op een dag, minimum 6 °C om 3 uur, maximum 18 °C om 15 uur
T_GRAF = venster("grafisch-temperatuur", 0, 24, 0, 20, 2, 2)


def _f(x):
    return x ** 3 / 4 - 3 * x


def _g(x):
    return 2 + 3 / (x - 1)


def _t(u):
    return 12 - 6 * math.cos(math.pi * (u - 3) / 12)


GRAFIEKEN = [
    dict(naam=F_GRAF, titel="De grafiek van f", krommen=[(_f, "groen", "", (-4, 4))],
         punten=[(-4, _f(-4), ""), (4, _f(4), "")]),
    dict(naam=G_GRAF, titel="De grafiek van g", krommen=[(_g, "blauw", "", (-5, 0.999)), (_g, "blauw", "", (1.001, 7))],
         stippel=[("h", 2), ("v", 1)]),
    dict(naam=T_GRAF, titel="Temperatuur T (in °C) op een dag, u uur na middernacht",
         krommen=[(_t, "oranje", "", (0, 24))], xlabel="u", ylabel="T", ijk_x=3, ijk_y=2),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen en vragen over functiekenmerken") for g in GRAFIEKEN]

VRAGEN = [
    klik(
        "Klik op het punt waar f haar maximum bereikt.",
        f"{F_GRAF}.svg",
        [punt_zone(F_GRAF, -2, 4), punt_zone(F_GRAF, 4, 4)],
        r"De hoogste functiewaarde is \(4\). Die wordt bereikt in \((-2, 4)\) en ook in het eindpunt \((4, 4)\) van het domein.",
    ),
    klik(
        "Klik op het nulpunt van f met de grootste x-coördinaat.",
        f"{F_GRAF}.svg",
        [punt_zone(F_GRAF, math.sqrt(12), 0)],
        r"De grafiek snijdt de \(x\)-as in \(0\) en in ongeveer \(\pm 3{,}5\). Het nulpunt rechts is ongeveer \((3{,}5;\ 0)\).",
    ),
    met_prent(f"{F_GRAF}.svg", mk(
        r"Wat zijn het domein en het bereik van \(f\)?",
        [
            r"\(\text{dom} f = [-4, 4]\) en \(\text{ber} f = [-4, 4]\)",
            r"\(\text{dom} f = \mathbb{R}\) en \(\text{ber} f = \mathbb{R}\)",
            r"\(\text{dom} f = [-4, 4]\) en \(\text{ber} f = [-6, 6]\)",
            r"\(\text{dom} f = [-5, 5]\) en \(\text{ber} f = [-4, 4]\)",
        ],
        0,
        r"De grafiek loopt van \(x = -4\) tot \(x = 4\), en de functiewaarden blijven tussen \(-4\) en \(4\). Het venster van de tekening is niet het domein.",
    )),
    met_prent(f"{F_GRAF}.svg", tabel(
        r"Juist of fout over \(f\)?",
        [
            (r"\(f\) is een oneven functie.", J),
            (r"\(f\) stijgt op \([-2, 2]\).", F),
            (r"\(f\) heeft drie nulwaarden.", J),
            (r"\(f(x) > 0\) voor alle \(x\) in \(]0, 4]\).", F),
        ],
        r"De grafiek is puntsymmetrisch rond de oorsprong. Tussen \(-2\) en \(2\) daalt ze. Tussen \(0\) en ongeveer \(3{,}5\) ligt ze onder de \(x\)-as.",
    )),
    klik(
        "Klik op een stuk van de grafiek van f waar ze daalt.",
        f"{F_GRAF}.svg",
        [vak_zone(F_GRAF, -1.6, 1.6, -4.5, 4.5)],
        r"\(f\) daalt van het maximum in \(x = -2\) tot het minimum in \(x = 2\).",
    ),
    met_prent(f"{F_GRAF}.svg", tabel(
        r"Wat is het teken van \(f(x)\) op elk interval?",
        [
            (r"\(]-4;\ -3{,}5[\)", "Negatief"),
            (r"\(]-3{,}5;\ 0[\)", "Positief"),
            (r"\(]0;\ 3{,}5[\)", "Negatief"),
            (r"\(]3{,}5;\ 4[\)", "Positief"),
        ],
        "Boven de x-as is f(x) positief, eronder negatief. Het teken wisselt in elke nulwaarde.",
        kolommen=["Positief", "Negatief"],
    )),
    met_prent(f"{F_GRAF}.svg", mk(
        r"Waar stijgt \(f\) met afnemende stijging?",
        [r"Op \([-4, -2]\)", r"Op \([2, 4]\)", r"Op \([-2, 0]\)", r"Op \([0, 2]\)"],
        0,
        r"Op \([-4, -2]\) stijgt \(f\), maar de grafiek wordt minder steil naar het maximum toe. Op \([2, 4]\) stijgt ze juist steeds sneller.",
    )),
    klik(
        r"Klik op de plaats waar de grafiek van \(g\) de \(y\)-as snijdt.",
        f"{G_GRAF}.svg",
        [punt_zone(G_GRAF, 0, -1)],
        r"\(g(0) = 2 + \frac{3}{-1} = -1\). Het snijpunt met de \(y\)-as is \((0, -1)\).",
    ),
    met_prent(f"{G_GRAF}.svg", mk(
        r"Wat zijn de asymptoten van \(g\)?",
        [
            r"Verticale asymptoot \(x = 1\), horizontale asymptoot \(y = 2\)",
            r"Verticale asymptoot \(x = 2\), horizontale asymptoot \(y = 1\)",
            r"Enkel een verticale asymptoot \(x = 1\)",
            r"Verticale asymptoot \(y = 1\), horizontale asymptoot \(x = 2\)",
        ],
        0,
        "Een verticale asymptoot schrijf je als x = ..., een horizontale als y = ...",
    )),
    met_prent(f"{G_GRAF}.svg", mk(
        r"Wat is het bereik van \(g\)?",
        [r"\(\mathbb{R} \setminus \{2\}\)", r"\(\mathbb{R} \setminus \{1\}\)", r"\(\mathbb{R}\)", r"\(]2, +\infty[\)"],
        0,
        r"De grafiek komt willekeurig hoog en laag, maar haalt de waarde \(2\) nooit: dat is de horizontale asymptoot.",
    )),
    met_prent(f"{G_GRAF}.svg", keuze(
        "Als x heel groot wordt, komt g(x) steeds dichter bij [[*2|1|0]]. Net rechts van x = 1 wordt g(x) [[*heel groot|heel klein|gelijk aan 2]].",
        "Op oneindig volgt de grafiek de horizontale asymptoot. Bij de verticale asymptoot schiet ze naar boven of naar onder.",
    )),
    inv(
        r"Bereken de nulwaarde van \(g(x) = 2 + \dfrac{3}{x - 1}\). Schrijf als kommagetal.",
        ["-0,5", "−0,5", "-1/2"],
        r"\(2 + \frac{3}{x - 1} = 0 \Rightarrow \frac{3}{x - 1} = -2 \Rightarrow x - 1 = -1{,}5 \Rightarrow x = -0{,}5\).",
    ),
    klik(
        "Klik op het moment van de dag waarop het het koudst is.",
        f"{T_GRAF}.svg",
        [punt_zone(T_GRAF, 3, 6)],
        "Het minimum ligt om 3 uur 's nachts, met 6 °C.",
    ),
    met_prent(f"{T_GRAF}.svg", mk(
        "Wat is het praktisch bereik van T?",
        [r"\([6, 18]\)", r"\([0, 24]\)", r"\([0, 20]\)", r"\([3, 15]\)"],
        0,
        r"Het bereik gaat over de functiewaarden: de temperatuur blijft tussen \(6\) en \(18\) °C. \([0, 24]\) is het praktisch domein.",
    )),
    klik(
        "Klik op een tijdstip waarop de temperatuur het snelst stijgt.",
        f"{T_GRAF}.svg",
        [punt_zone(T_GRAF, 9, 12, 40)],
        "Halfweg tussen het minimum (3 uur) en het maximum (15 uur), om 9 uur, is de grafiek het steilst.",
    ),
    met_prent(f"{T_GRAF}.svg", tabel(
        "Juist of fout over de temperatuur?",
        [
            ("Tussen 3 en 15 uur stijgt de temperatuur.", J),
            ("Om 15 uur is het 15 °C.", F),
            ("Tussen 3 en 9 uur stijgt de temperatuur met toenemende stijging.", J),
            ("Om 21 uur is het even warm als om 9 uur.", J),
        ],
        "Om 15 uur is het maximum 18 °C. Om 9 uur en om 21 uur ligt de temperatuur telkens halfweg tussen minimum en maximum: 12 °C.",
    )),
    tabel(
        "Even, oneven of geen van beide?",
        [
            (r"\(f(x) = x^{4} - 3x^{2}\)", "Even"),
            (r"\(f(x) = x^{3} + x\)", "Oneven"),
            (r"\(f(x) = x^{2} + x\)", "Geen van beide"),
            (r"\(f(x) = 5\)", "Even"),
        ],
        r"Even: \(f(-x) = f(x)\), symmetrisch rond de \(y\)-as. Oneven: \(f(-x) = -f(x)\), puntsymmetrisch rond de oorsprong.",
        kolommen=["Even", "Oneven", "Geen van beide"],
    ),
    mk(
        r"Van een oneven functie \(h\) weet je: \(h(3) = 7\). Hoeveel is \(h(-3)\)?",
        [r"\(-7\)", r"\(7\)", r"\(-3\)", r"Dat kan je niet weten."],
        0,
        r"Bij een oneven functie geldt \(h(-x) = -h(x)\), dus \(h(-3) = -7\).",
    ),
    mk(
        r"Een functie met periode \(4\) heeft \(p(1) = 6\). Welke waarde ken je dan zeker?",
        [r"\(p(13) = 6\)", r"\(p(4) = 6\)", r"\(p(5) = 10\)", r"\(p(-1) = 6\)"],
        0,
        r"De waarden herhalen zich telkens na \(4\): \(p(1) = p(5) = p(9) = p(13)\).",
    ),
    mk(
        r"Wat is het domein van \(k(x) = \dfrac{x + 1}{x^{2} - 9}\)?",
        [r"\(\mathbb{R} \setminus \{-3, 3\}\)", r"\(\mathbb{R} \setminus \{-1\}\)", r"\(\mathbb{R} \setminus \{9\}\)", r"\(\mathbb{R} \setminus \{-1, 3\}\)"],
        0,
        r"De noemer mag niet nul zijn: \(x^{2} = 9\) geeft \(x = \pm 3\).",
    ),
    sorteer(
        "Gaat het over een x-waarde of over een y-waarde?",
        ["x-waarde", "y-waarde"],
        [
            ["Een nulwaarde", "x-waarde"],
            ["Het domein", "x-waarde"],
            ["Een maximum", "y-waarde"],
            ["Het bereik", "y-waarde"],
            ["Een verticale asymptoot", "x-waarde"],
            ["Een horizontale asymptoot", "y-waarde"],
        ],
        "Het domein en de nulwaarden gaan over x, het bereik en de extrema over de functiewaarden y.",
    ),
    koppel(
        "Koppel de situatie aan het kenmerk dat ze beschrijft.",
        [
            ["Een auto verliest elk jaar waarde, maar steeds minder", "Dalend met afnemende daling"],
            ["Een verkoper verdient pas winst vanaf 200 stuks", "Nulwaarde"],
            ["De afkoeling van thee komt steeds dichter bij 20 °C", "Horizontale asymptoot"],
            ["Eb en vloed komen telkens na 12,5 uur terug", "Periode"],
        ],
        ["Verticale asymptoot"],
        "Telkens beschrijft de situatie een kenmerk van de grafiek.",
    ),
    mk(
        r"De hoogte van een pijl is \(h(t) = 40t - 5t^{2}\) (meter, \(t\) in seconden) tot hij de grond raakt. Wat is het praktisch domein?",
        [r"\([0, 8]\)", r"\([0, 4]\)", r"\([0, 80]\)", r"\(\mathbb{R}\)"],
        0,
        r"\(h(t) = 0\) voor \(t = 0\) en \(t = 8\). De pijl vliegt van \(0\) tot \(8\) seconden.",
    ),
    mk(
        r"Bij dezelfde pijl, \(h(t) = 40t - 5t^{2}\): wat is het praktisch bereik?",
        [r"\([0, 80]\)", r"\([0, 8]\)", r"\([0, 40]\)", r"\([0, 160]\)"],
        0,
        r"Het maximum ligt halverwege, in \(t = 4\): \(h(4) = 160 - 80 = 80\) meter.",
    ),
    tabel(
        "Juist of fout over nulwaarden en asymptoten?",
        [
            ("Een functie kan meer dan één nulwaarde hebben.", J),
            ("Een functie kan meer dan één snijpunt met de y-as hebben.", F),
            ("Een grafiek kan haar horizontale asymptoot snijden.", J),
            ("Een grafiek kan haar verticale asymptoot snijden.", F),
        ],
        "Bij elke x hoort hoogstens één functiewaarde. Een verticale asymptoot ligt bij een x die niet in het domein zit.",
    ),
    met_prent(f"{F_GRAF}.svg", volgorde(
        "Lees af op de grafiek van f en zet de functiewaarden van klein naar groot.",
        [r"\(f(2)\)", r"\(f(3)\)", r"\(f(0)\)", r"\(f(-1)\)", r"\(f(-2)\)"],
        r"\(f(2) = -4\) (minimum), \(f(3) \approx -2{,}3\), \(f(0) = 0\), \(f(-1) \approx 2{,}8\), \(f(-2) = 4\) (maximum).",
    )),
    open_(
        r"Een ouder zegt: het domein van \(h(t) = 40t - 5t^{2}\) is \([0, 8]\). Leg uit wat er beter kan.",
        r"Het domein van het voorschrift is \(\mathbb{R}\): je kan elke \(t\) invullen. Enkel in de situatie (de vlucht van de pijl) zijn alleen \(t\) van \(0\) tot \(8\) zinvol. Dat is het praktisch domein.",
        "Domein en praktisch domein zijn niet hetzelfde.",
    ),
    casus(
        r"Het aantal bezoekers \(B(u)\) in een zwembad, \(u\) uur na de opening om 9 uur, stijgt tot 13 uur naar 400, blijft dan een uur constant en daalt daarna tot sluiting om 20 uur, wanneer er niemand meer is.",
        [
            mk(
                "Wat is het praktisch domein van B?",
                [r"\([0, 11]\)", r"\([9, 20]\)", r"\([0, 400]\)", r"\([4, 5]\)"],
                0,
                r"\(u\) telt de uren na de opening: van \(0\) (9 uur) tot \(11\) (20 uur).",
            ),
            mk(
                "Op welk interval is B constant?",
                [r"\([4, 5]\)", r"\([13, 14]\)", r"\([0, 4]\)", r"\([5, 11]\)"],
                0,
                r"Van 13 tot 14 uur, dat is \(u = 4\) tot \(u = 5\).",
            ),
            mk(
                "Wat is de nulwaarde van B die in de situatie past?",
                [r"\(u = 11\)", r"\(u = 0\)", r"\(u = 20\)", r"\(u = 400\)"],
                0,
                r"Bij sluiting, \(u = 11\), is er niemand meer: \(B(11) = 0\). Bij de opening waren er misschien al wachtenden, dat staat er niet.",
            ),
        ],
    ),
]
