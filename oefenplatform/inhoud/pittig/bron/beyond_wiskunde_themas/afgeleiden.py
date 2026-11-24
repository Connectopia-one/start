"""Afgeleiden en het verloop van een functie — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("afgeleiden-hellinggrafiek-bey", -3, 4, -4, 6)


def _fa(x):
    return x * x - x - 2


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van de afgeleide f′ (niet van f!)", krommen=[(_fa, "paars", "f′", (-2.4, 3.4))], labelplek={"f′": (3.1, 5.6)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="hellinggrafiek f′(x) = x² − x − 2", vragen="klikvragen: van de afgeleide terug naar het verloop van f")]

VRAGEN = [
    klik(
        "Op de prent staat de grafiek van f′. Klik op de plaats die toont waar f een lokaal maximum heeft.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, -1, 0)],
        r"In \(x = -1\) gaat \(f'\) van positief naar negatief: f stijgt en gaat dan dalen.",
    ),
    klik(
        "Op de prent staat de grafiek van f′. Klik op de plaats die toont waar f een lokaal minimum heeft.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 2, 0)],
        r"In \(x = 2\) gaat \(f'\) van negatief naar positief.",
    ),
    klik(
        "Op de prent staat de grafiek van f′. Klik op het punt dat bij het buigpunt van f hoort.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0.5, -2.25)],
        r"Een buigpunt van f is een extremum van \(f'\): daar is \(f'' = 0\) en wisselt het teken. De top van \(f'\) ligt bij \(x = \tfrac{1}{2}\).",
    ),
    klik(
        "Op de prent staat de grafiek van f′. Klik in de strook waar f daalt.",
        f"{GRAF}.svg",
        [strook_zone(GRAF, -0.9, 1.9)],
        r"f daalt waar \(f' < 0\): tussen \(-1\) en \(2\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Op de prent staat f′. Juist of fout over f?",
        [("f is hol voor x > 1/2.", J), ("f stijgt op ]−∞, −1].", J), ("f heeft een maximum in x = 1/2.", F), ("f(2) is kleiner dan f(−1).", J), ("f′(0) = −2, dus f(0) = −2.", F)],
        r"\(f''\) is de helling van \(f'\): positief rechts van de top. \(f'(0)\) zegt iets over de helling van f, niet over haar waarde.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        "Wat is de afgeleide?",
        [(r"\(x^{3}e^{x}\)", r"\((3x^{2} + x^{3})e^{x}\)"), (r"\(\ln(x^{2} + 1)\)", r"\(\dfrac{2x}{x^{2} + 1}\)"), (r"\(\sin^{2}x\)", r"\(2\sin x\cos x\)"), (r"\(\dfrac{x}{x + 1}\)", r"\(\dfrac{1}{(x + 1)^{2}}\)")],
        "Productregel, kettingregel en quotiëntregel.",
        kolommen=[r"\((3x^{2} + x^{3})e^{x}\)", r"\(\dfrac{2x}{x^{2} + 1}\)", r"\(2\sin x\cos x\)", r"\(\dfrac{1}{(x + 1)^{2}}\)"],
    ),
    mk(
        r"Wat is de vergelijking van de raaklijn aan \(f(x) = \sqrt{x}\) in \(x = 4\)?",
        [r"\(y = \tfrac{1}{4}x + 1\)", r"\(y = \tfrac{1}{4}x + 2\)", r"\(y = \tfrac{1}{2}x\)", r"\(y = 4x - 14\)"],
        0,
        r"\(f'(x) = \tfrac{1}{2\sqrt{x}}\), \(f'(4) = \tfrac{1}{4}\), raakpunt \((4, 2)\): \(y - 2 = \tfrac{1}{4}(x - 4)\).",
    ),
    inv(
        r"Bereken \(f'(0)\) voor \(f(x) = e^{3x}\cos x\).",
        ["3"],
        r"\(f'(x) = 3e^{3x}\cos x - e^{3x}\sin x\). In 0: \(3 - 0 = 3\).",
    ),
    casus(
        r"Gegeven \(f(x) = x^{3} - 6x^{2} + 9x + 1\).",
        [
            mk(r"Wat is \(f'(x)\)?", [r"\(3x^{2} - 12x + 9\)", r"\(3x^{2} - 6x + 9\)", r"\(x^{2} - 12x + 9\)", r"\(3x^{2} - 12x + 10\)"], 0, "Macht per macht afleiden."),
            mk("Waar liggen de extrema?", [r"maximum bij \(x = 1\), minimum bij \(x = 3\)", r"minimum bij \(x = 1\), maximum bij \(x = 3\)", r"maximum bij \(x = 3\) en bij \(x = 1\)", r"geen extrema"], 0,
               r"\(3(x - 1)(x - 3)\): plus, min, plus."),
            inv("Wat is de x-coördinaat van het buigpunt?", ["2"], r"\(f''(x) = 6x - 12 = 0\)."),
            inv("Wat is de waarde van het lokaal maximum?", ["5"], r"\(f(1) = 1 - 6 + 9 + 1 = 5\)."),
        ],
    ),
    sorteer(
        "Wat weet je over de grafiek van f op dat interval?",
        ["Stijgend en hol", "Stijgend en bol", "Dalend en hol", "Dalend en bol"],
        [(r"\(f' > 0\), \(f'' > 0\)", "Stijgend en hol"), (r"\(f' > 0\), \(f'' < 0\)", "Stijgend en bol"), (r"\(f' < 0\), \(f'' > 0\)", "Dalend en hol"), (r"\(f' < 0\), \(f'' < 0\)", "Dalend en bol")],
        r"Het teken van \(f'\) geeft stijgen of dalen, het teken van \(f''\) hol (naar boven open) of bol.",
    ),
    mk(
        r"Een doos zonder deksel wordt gemaakt uit een vierkant karton van 30 cm door in de hoeken vierkantjes met zijde \(x\) weg te knippen. Voor welke \(x\) is het volume maximaal?",
        ["5 cm", "7,5 cm", "10 cm", "15 cm"],
        0,
        r"\(V = x(30 - 2x)^{2}\). \(V' = (30 - 2x)(30 - 6x) = 0\) geeft \(x = 5\) (\(x = 15\) geeft volume 0).",
    ),
    koppel(
        "Verbind de functie met haar afgeleide.",
        [(r"\(\tan x\)", r"\(\dfrac{1}{\cos^{2}x}\)"), (r"\(2^{x}\)", r"\(2^{x}\ln 2\)"), (r"\(\ln|x|\)", r"\(\dfrac{1}{x}\)"), (r"\(\sqrt{x}\)", r"\(\dfrac{1}{2\sqrt{x}}\)")],
        [r"\(x\,2^{x - 1}\)"],
        r"\(2^{x}\) is geen macht van x: \(x\,2^{x - 1}\) is een veelgemaakte fout.",
    ),
    tabel(
        "Over afgeleiden: juist of fout?",
        [(r"Als \(f'(a) = 0\), heeft f een extremum in a.", F), (r"\(f(x) = x^{3}\) heeft een buigpunt in 0.", J), (r"\(f(x) = |x|\) is afleidbaar in 0.", F), (r"Als f stijgt en \(f'' < 0\), stijgt f steeds trager.", J), (r"De afgeleide van \(e^{2x}\) is \(e^{2x}\).", F)],
        r"Bij \(x^{3}\) is \(f'(0) = 0\) maar er is geen extremum. \(|x|\) heeft een knik. \((e^{2x})' = 2e^{2x}\).",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        r"De gemiddelde verandering op \(\left[a, b\right]\) is de richtingscoëfficiënt van de [[*koorde|raaklijn]]. De afgeleide \(f'(a)\) is die van de [[*raaklijn|koorde]] in \(a\).",
        "Laat b naar a gaan: de koorde wordt de raaklijn.",
    ),
    inv(
        r"De positie van een deeltje is \(s(t) = t^{3} - 4t\) (m, t in s). Hoe groot is de versnelling na 2 s, in m/s²?",
        ["12"],
        r"\(v = s' = 3t^{2} - 4\), \(a = v' = 6t\). Bij \(t = 2\): \(12\).",
    ),
    mk(
        r"In welk punt van \(y = x^{2} - 4x\) is de raaklijn evenwijdig met \(y = 2x + 1\)?",
        [r"\((3, -3)\)", r"\((1, -3)\)", r"\((2, -4)\)", r"\((3, 2)\)"],
        0,
        r"\(2x - 4 = 2\) geeft \(x = 3\), \(y = 9 - 12 = -3\).",
    ),
    sleep(
        r"Volgens de middelwaardestelling van Lagrange bestaat er een \(c\) in \(\left]a, b\right[\) met \(f'(c) =\) [[\(\dfrac{f(b) - f(a)}{b - a}\)]], op voorwaarde dat f [[continu]] is op \(\left[a, b\right]\) en afleidbaar op \(\left]a, b\right[\).",
        [r"\(f(b) - f(a)\)", "periodiek"],
        "Ergens is de raaklijn evenwijdig met de koorde.",
    ),
    tabel(
        r"Over \(f(x) = xe^{-x}\). Juist of fout?",
        [(r"\(f'(x) = (1 - x)e^{-x}\)", J), (r"f heeft een maximum in \(x = 1\).", J), (r"Het maximum is \(\tfrac{1}{e}\).", J), (r"f is overal stijgend.", F)],
        r"\(f' > 0\) voor \(x < 1\) en \(< 0\) daarna.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"De totale kost is \(K(q) = 0{,}01q^{2} + 5q + 200\) euro. Wat is de marginale kost bij \(q = 100\)?",
        ["7 euro", "800 euro", "5 euro", "8 euro"],
        0,
        r"\(K'(q) = 0{,}02q + 5\), bij 100: \(2 + 5 = 7\) euro per extra stuk.",
    ),
    volgorde(
        "Zet de stappen van een functieonderzoek in een zinnige volgorde.",
        ["domein bepalen", "nulwaarden en snijpunt met de y-as", "f′ en het tekenschema: stijgen, dalen, extrema", "f″ en het tekenschema: hol, bol, buigpunten", "grafiek schetsen"],
        "Van wat de functie is, naar hoe ze verloopt, naar de schets.",
    ),
    inv(
        r"Hoeveel is de afgeleide van \(\ln(\cos x)\) in \(x = 0\)?",
        ["0", "nul"],
        r"\(\dfrac{-\sin x}{\cos x} = -\tan x\), in 0 gelijk aan 0.",
    ),
    mk(
        r"Van alle rechthoeken met omtrek 40 cm: welke heeft de grootste oppervlakte?",
        ["een vierkant van 10 bij 10", "een rechthoek van 15 bij 5", "een rechthoek van 20 bij 0", "er is geen grootste"],
        0,
        r"\(A = x(20 - x)\), \(A' = 20 - 2x = 0\) bij \(x = 10\).",
    ),
    tabel(
        "Bereken de tweede afgeleide van de functie.",
        [(r"\(x^{4}\)", r"\(12x^{2}\)"), (r"\(\sin x\)", r"\(-\sin x\)"), (r"\(e^{-x}\)", r"\(e^{-x}\)"), (r"\(\ln x\)", r"\(-\tfrac{1}{x^{2}}\)")],
        "Twee keer na elkaar afleiden.",
        kolommen=[r"\(12x^{2}\)", r"\(-\sin x\)", r"\(e^{-x}\)", r"\(-\tfrac{1}{x^{2}}\)"],
    ),
    mk(
        r"Voor welke \(a\) heeft \(f(x) = x^{3} + ax^{2} + 3x\) een buigpunt bij \(x = 1\)?",
        [r"\(a = -3\)", r"\(a = 3\)", r"\(a = -1\)", r"\(a = 0\)"],
        0,
        r"\(f''(x) = 6x + 2a\). \(6 + 2a = 0\) geeft \(a = -3\).",
    ),
    inv(
        r"Hoeveel is \(\lim\limits_{h \to 0}\dfrac{(2 + h)^{3} - 8}{h}\)?",
        ["12"],
        r"Dat is de afgeleide van \(x^{3}\) in \(x = 2\): \(3 \cdot 4 = 12\).",
    ),
    mk(
        r"Een ballon wordt opgeblazen: de straal groeit met 2 cm/s. Hoe snel groeit het volume \(V = \tfrac{4}{3}\pi r^{3}\) als \(r = 10\) cm?",
        [r"\(800\pi\) cm³/s", r"\(400\pi\) cm³/s", r"\(\tfrac{8000}{3}\pi\) cm³/s", r"\(80\pi\) cm³/s"],
        0,
        r"\(\tfrac{dV}{dt} = 4\pi r^{2} \cdot \tfrac{dr}{dt} = 4\pi \cdot 100 \cdot 2\).",
    ),
    tabel(
        r"De tabel geeft het teken van \(f'\): plus op \(\left]-\infty, -2\right[\), min op \(\left]-2, 3\right[\), min op \(\left]3, +\infty\right[\). Juist of fout?",
        [(r"f heeft een maximum in \(-2\).", J), (r"f heeft een minimum in \(3\).", F), (r"f daalt op \(\left[-2, +\infty\right[\).", J)],
        r"In 3 wisselt \(f'\) niet van teken: geen extremum, wel een horizontale raaklijn.",
        kolommen=["Juist", "Fout"],
    ),
]
