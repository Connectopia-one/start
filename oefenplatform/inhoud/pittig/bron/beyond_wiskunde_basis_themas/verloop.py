"""Bedrijfswetenschappen: verloop van een functie en optimaliseren — pittig (🌍 Beyond, wiskunde basis)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

F_GRAF = venster("verloop-f", -0.5, 4.5, -2, 7, 0.5, 1)
V_GRAF = venster("verloop-doos", 0, 10, 0, 700, 1, 50)


def _f(x):
    return x ** 3 - 6 * x ** 2 + 9 * x + 1


def _v(x):
    return x * (20 - 2 * x) ** 2


X_MAX = 10 / 3

GRAFIEKEN = [
    dict(naam=F_GRAF, titel="De grafiek van f(x) = x³ − 6x² + 9x + 1",
         krommen=[(_f, "groen", "", (-0.5, 4.4))], ijk_x=1, ijk_y=1),
    dict(naam=V_GRAF, titel="Volume V (cm³) van een open doos, x = zijde van de weggeknipte vierkantjes (cm)",
         krommen=[(_v, "blauw", "", (0, 10))], xlabel="x", ylabel="V", ijk_x=1, ijk_y=100),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over verloop en optimaliseren") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        "Klik op het buigpunt van f.",
        f"{F_GRAF}.svg",
        [punt_zone(F_GRAF, 2, 3, 30)],
        r"\(f''(x) = 6x - 12\) wisselt van teken in \(x = 2\). Het buigpunt is \((2, 3)\).",
    ),
    klik(
        "Klik boven een x-waarde waar f tegelijk dalend en hol is.",
        f"{F_GRAF}.svg",
        [strook_zone(F_GRAF, 2.05, 2.95)],
        r"\(f' = 3(x - 1)(x - 3) < 0\) op \(]1, 3[\) en \(f'' = 6x - 12 > 0\) voor \(x > 2\). Beide samen: tussen 2 en 3.",
    ),
    met_prent(f"{F_GRAF}.svg", tabel(
        r"Vul de samenvattende tabel aan: welk teken heeft \(f'\) of \(f''\)?",
        [
            (r"\(f'\) op \(]-\infty, 1[\)", "+"),
            (r"\(f''(2)\)", "0"),
            (r"\(f'\) op \(]3, +\infty[\)", "+"),
        ],
        r"\(f'(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)\) is positief buiten 1 en 3. \(f''(2) = 12 - 12 = 0\).",
        kolommen=["+", "−", "0"],
    )),
    met_prent(f"{F_GRAF}.svg", mk(
        "Wat is het lokaal minimum van f?",
        [r"\(5\), bereikt in \(x = 1\)", r"\(1\), bereikt in \(x = 3\)", r"\(3\), bereikt in \(x = 2\)", r"\(0\), bereikt in \(x = 0\)"],
        1,
        r"\(f'\) wisselt in \(x = 3\) van min naar plus. \(f(3) = 27 - 54 + 27 + 1 = 1\).",
    )),
    klik(
        "Uit een vierkant karton van 20 cm knip je in elke hoek een vierkantje van x cm weg en plooi je een open doos. Klik op het punt van de grafiek met het grootste volume.",
        f"{V_GRAF}.svg",
        [punt_zone(V_GRAF, X_MAX, _v(X_MAX), 32)],
        r"\(V'(x) = (20 - 2x)(20 - 6x) = 0\) geeft \(x = \frac{10}{3}\) (\(x = 10\) valt buiten het praktisch domein). \(V \approx 593\) cm³.",
    ),
    met_prent(f"{V_GRAF}.svg", mk(
        r"Wat is het praktisch domein van \(V(x) = x(20 - 2x)^2\)?",
        [r"\(\mathbb{R}\)", r"\(]0, 20[\)", r"\(]0, 10[\)", r"\([0, +\infty[\)"],
        2,
        r"x moet positief zijn en de bodem \(20 - 2x\) ook: \(0 < x < 10\).",
    )),
    mk(
        r"\(f'(x) = (x - 2)^2 (x + 1)\). Waar heeft f een lokaal extremum?",
        [r"In \(x = 2\) en in \(x = -1\)", r"Enkel in \(x = 2\)", r"Enkel in \(x = -1\)", "Nergens"],
        2,
        r"In \(x = -1\) wisselt \(f'\) van teken. In \(x = 2\) is \(f' = 0\), maar \((x - 2)^2\) blijft positief: geen tekenwissel.",
    ),
    mk(
        r"Je vindt \(f''(a) = 0\). Wat weet je dan zeker?",
        [
            "Dat a een buigpunt is",
            "Dat f in a een extremum heeft",
            "Niets zeker: je moet nagaan of f″ in a van teken wisselt",
            "Dat f constant is rond a",
        ],
        2,
        r"Bij \(f(x) = x^4\) is \(f''(0) = 0\), maar \(f''\) blijft positief: geen buigpunt.",
    ),
    tabel(
        "Juist of fout over het verloop van een functie?",
        [
            ("Een derdegraadsfunctie heeft altijd precies één buigpunt.", J),
            (r"Waar \(f'' > 0\), is de grafiek hol.", J),
            (r"In een buigpunt is \(f'\) altijd \(0\).", F),
            ("Een lokaal maximum is altijd de grootste functiewaarde op het hele domein.", F),
        ],
        r"\(f''\) van een derdegraadsfunctie is een eerstegraadsfunctie met één tekenwissel. In een buigpunt verandert de kromming, de helling hoeft niet 0 te zijn.",
    ),
    keuze(
        "Tweede-afgeleidetest: als f′(a) = 0 en f″(a) > 0, dan heeft f in a een lokaal [[*minimum|maximum|buigpunt]]. Waar f″ van teken wisselt, ligt een [[*buigpunt|extremum|nulpunt]].",
        "Hol rond een horizontale raaklijn: een dal.",
    ),
    mk(
        r"Waar heeft \(f(x) = x^4 - 4x^3\) een buigpunt?",
        [r"In \(x = 3\)", r"In \(x = 0\) en \(x = 2\)", r"Enkel in \(x = 0\)", r"In \(x = 0\) en \(x = 3\)"],
        1,
        r"\(f''(x) = 12x^2 - 24x = 12x(x - 2)\) wisselt van teken in \(0\) en in \(2\).",
    ),
    mk(
        r"Wat zijn de lokale extrema van \(f(x) = x^3 - 3x\)?",
        [
            r"Maximum \(2\) in \(x = -1\), minimum \(-2\) in \(x = 1\)",
            r"Maximum \(-2\) in \(x = 1\), minimum \(2\) in \(x = -1\)",
            r"Enkel een minimum \(0\) in \(x = 0\)",
            r"Maximum \(3\) in \(x = \sqrt{3}\)",
        ],
        0,
        r"\(f'(x) = 3x^2 - 3 = 0\) geeft \(x = \pm 1\). \(f(-1) = 2\), \(f(1) = -2\).",
    ),
    sorteer(
        "Is de grafiek hol of bol (op het hele domein)?",
        ["Hol", "Bol"],
        [
            [r"\(f(x) = x^2\)", "Hol"],
            [r"\(f(x) = -x^2\)", "Bol"],
            [r"\(f(x) = e^x\)", "Hol"],
            [r"\(f(x) = \ln x\)", "Bol"],
            [r"\(f(x) = \sqrt{x}\)", "Bol"],
            [r"\(f(x) = 2^x + x\)", "Hol"],
        ],
        r"Kijk naar het teken van \(f''\): \(e^x\) en \(2^x \ln^2 2\) zijn positief, \(-\frac{1}{x^2}\) en \(-\frac{1}{4x\sqrt{x}}\) negatief.",
    ),
    volgorde(
        "Zet de stappen om een extremumprobleem op te lossen in de goede volgorde.",
        [
            "Kies de veranderlijke en bepaal het praktisch domein",
            "Stel het voorschrift op van de grootheid die extreem moet zijn",
            "Bereken de afgeleide en haar nulwaarden",
            "Ga met een tekenverloop of de tweede afgeleide na of het een maximum of minimum is",
            "Formuleer het antwoord in de context",
        ],
        "Eerst modelleren, dan rekenen, dan controleren en antwoorden.",
    ),
    koppel(
        "Koppel de tekens aan het verloop van de grafiek.",
        [
            [r"\(f' > 0\) en \(f'' > 0\)", "Stijgend en hol"],
            [r"\(f' > 0\) en \(f'' < 0\)", "Stijgend en bol"],
            [r"\(f' < 0\) en \(f'' > 0\)", "Dalend en hol"],
            [r"\(f' < 0\) en \(f'' < 0\)", "Dalend en bol"],
        ],
        ["Constant"],
        "f′ zegt stijgen of dalen, f″ zegt hoe de grafiek buigt.",
    ),
    mk(
        "Twee positieve getallen hebben samen 20. Wat is hun grootst mogelijke product?",
        [r"\(400\)", r"\(100\)", r"\(99\)", r"\(200\)"],
        1,
        r"\(P(x) = x(20 - x)\), \(P'(x) = 20 - 2x = 0\) geeft \(x = 10\). \(10 \cdot 10 = 100\).",
    ),
    mk(
        "Een boer zet met 100 m draad een rechthoekig weiland af langs een rivier. Aan de rivierkant komt geen draad. Wat is de grootst mogelijke oppervlakte?",
        [r"\(625\) m²", r"\(2500\) m²", r"\(1000\) m²", r"\(1250\) m²"],
        3,
        r"Zijden x, x en \(100 - 2x\): \(A(x) = x(100 - 2x)\), \(A'(x) = 100 - 4x = 0\) bij \(x = 25\). \(25 \cdot 50 = 1250\).",
    ),
    inv(
        r"De kost per stuk is \(G(q) = q + \dfrac{400}{q}\) euro (\(q > 0\)). Bij hoeveel stuks is de kost per stuk het laagst?",
        "20",
        r"\(G'(q) = 1 - \frac{400}{q^2} = 0\) geeft \(q^2 = 400\), dus \(q = 20\).",
    ),
    mk(
        r"De winst bij verkoopprijs p (euro) is \(W(p) = -20p^2 + 1200p - 10\,000\). Bij welke prijs is de winst maximaal?",
        [r"\(60\) euro", r"\(30\) euro", r"\(15\) euro", r"\(1200\) euro"],
        1,
        r"\(W'(p) = -40p + 1200 = 0\) geeft \(p = 30\).",
    ),
    sleep(
        "Het [[praktisch domein]] bevat enkel waarden die in de context zinvol zijn. Een extremum op de [[rand]] van dat domein moet je apart nagaan.",
        ["bereik", "midden"],
        "Een afgeleide gelijk aan 0 vindt enkel extrema binnenin.",
    ),
    mk(
        r"\(f'\) wisselt in \(x = 4\) van teken, van min naar plus. Wat heeft f in \(x = 4\)?",
        ["Een lokaal maximum", "Een buigpunt", "Een lokaal minimum", "Een nulwaarde"],
        2,
        "Eerst dalen, dan stijgen: een dal.",
    ),
    mk(
        r"Een functie heeft \(f''(x) < 0\) voor elke x. Hoeveel lokale minima kan ze hebben?",
        [r"Eén", r"Twee", r"Oneindig veel", r"Geen enkel"],
        3,
        "De grafiek is overal bol. Een lokaal minimum vraagt een holle plek.",
    ),
    open_(
        "Leg uit waarom je bij een extremumprobleem niet mag stoppen bij 'f′(x) = 0'.",
        r"Een nulwaarde van \(f'\) kan een maximum, een minimum of geen van beide zijn (zoals bij \(x^3\) in 0). Met een tekenverloop van \(f'\) of de tweede afgeleide stel je vast welk soort extremum het is. Daarnaast kan het grootste of kleinste resultaat ook op de rand van het praktisch domein liggen.",
        "Een horizontale raaklijn is nog geen top of dal.",
    ),
    mk(
        "Een fabrikant ontwerpt een cilindervormig blikje van 330 cm³. Wat probeert hij meestal minimaal te maken?",
        ["De inhoud", "De hoogte", "De buitenoppervlakte, dus het materiaal", "De straal"],
        2,
        "De inhoud ligt vast. Minder oppervlakte betekent minder blik en lagere kosten.",
    ),
    tabel(
        r"Juist of fout over \(f(x) = x^3 - 3x^2\)?",
        [
            (r"f heeft een lokaal maximum in \(x = 0\).", J),
            (r"f heeft een buigpunt in \(x = 1\).", J),
            (r"f is hol op \(]-\infty, 1[\).", F),
            (r"f heeft een lokaal minimum in \(x = 1\).", F),
        ],
        r"\(f'(x) = 3x(x - 2)\): plus, min, plus. \(f''(x) = 6x - 6\): negatief voor \(x < 1\) (bol), positief erna.",
    ),
    mk(
        r"\(f(x) = x e^{-x}\) heeft afgeleide \(f'(x) = (1 - x)e^{-x}\). Waar bereikt f haar maximum?",
        [r"In \(x = 0\)", r"In \(x = -1\)", "f heeft geen maximum", r"In \(x = 1\)"],
        3,
        r"\(e^{-x}\) is altijd positief, dus het teken komt van \(1 - x\): plus en dan min.",
    ),
    mk(
        r"Een bal volgt \(h(t) = -4{,}9t^2 + 19{,}6t + 2\) (m, t in s). Hoe hoog komt hij maximaal?",
        [r"\(19{,}6\) m", r"\(41{,}2\) m", r"\(2\) m", r"\(21{,}6\) m"],
        3,
        r"\(h'(t) = -9{,}8t + 19{,}6 = 0\) bij \(t = 2\). \(h(2) = -19{,}6 + 39{,}2 + 2\).",
    ),
    casus(
        "Een rechthoekige tuin van 200 m² ligt tegen een muur. Langs de drie andere zijden komt een omheining. Noem x de lengte (m) van de zijden loodrecht op de muur.",
        [
            mk(
                "Welke functie geeft de lengte van de omheining?",
                [r"\(L(x) = 2x + 200x\)", r"\(L(x) = 2x + \dfrac{200}{x}\)", r"\(L(x) = x + \dfrac{200}{x}\)", r"\(L(x) = 2x + \dfrac{400}{x}\)"],
                1,
                r"De zijde langs de muur is \(\frac{200}{x}\). Twee zijden x en één zijde \(\frac{200}{x}\).",
            ),
            mk(
                "Voor welke x is de omheining het kortst?",
                [r"\(x = 20\)", r"\(x = 14{,}1\)", r"\(x = 5\)", r"\(x = 10\)"],
                3,
                r"\(L'(x) = 2 - \frac{200}{x^2} = 0\) geeft \(x^2 = 100\).",
            ),
            mk(
                "Hoe lang is die kortste omheining?",
                [r"\(40\) m", r"\(30\) m", r"\(60\) m", r"\(56{,}6\) m"],
                0,
                r"\(2 \cdot 10 + \frac{200}{10} = 20 + 20\).",
            ),
        ],
    ),
]
