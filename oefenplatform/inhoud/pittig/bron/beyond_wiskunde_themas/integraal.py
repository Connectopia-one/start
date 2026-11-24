"""De bepaalde integraal en haar toepassingen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("integraal-parabool-bey", -0.5, 4.5, -2, 4)

GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f(x) = x² − 4x + 3",
         krommen=[(lambda x: x * x - 4 * x + 3, "groen", "f", (-0.4, 4.4))],
         labelplek={"f": (4.2, 3.4)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="parabool x² − 4x + 3 met nulwaarden 1 en 3", vragen="klikvragen over het teken van een integraal")]

VRAGEN = [
    klik(
        r"Klik in de strook waar \(\int f(x)\,dx\) over die strook negatief uitkomt.",
        f"{GRAF}.svg",
        [strook_zone(GRAF, 1.1, 2.9)],
        r"Tussen de nulwaarden 1 en 3 ligt de grafiek onder de x-as.",
    ),
    klik(
        r"Klik op het punt waar je de integraal \(\int_{0}^{4} f(x)\,dx\) moet splitsen als je de werkelijke oppervlakte zoekt, en dat links van de top ligt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 1, 0)],
        r"In de nulwaarden \(x = 1\) en \(x = 3\) wisselt het teken. Links van de top ligt \(x = 1\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        r"Kijk naar de grafiek van \(f\). Juist of fout?",
        [(r"\(\int_{3}^{4} f(x)\,dx > 0\)", J), (r"\(\int_{1}^{3} f(x)\,dx\) is groter dan \(\int_{0}^{1} f(x)\,dx\)", F), (r"\(\int_{0}^{4} f(x)\,dx\) is gelijk aan de werkelijke oppervlakte tussen grafiek en x-as", F), (r"\(\int_{2}^{2} f(x)\,dx = 0\)", J)],
        r"Onder de x-as telt de oppervlakte negatief mee, dus de integraal over [0, 4] is kleiner dan de werkelijke oppervlakte.",
        kolommen=["Juist", "Fout"],
    )),
    inv(
        r"Bereken \(\int_{1}^{3}(x^{2} - 4x + 3)\,dx\). Schrijf het antwoord als breuk.",
        ["-4/3", "−4/3"],
        r"\(\left[\tfrac{x^{3}}{3} - 2x^{2} + 3x\right]_{1}^{3} = 0 - \tfrac{4}{3}\).",
    ),
    mk(
        r"Hoe groot is de werkelijke oppervlakte tussen de grafiek van \(f(x) = x^{2} - 4x + 3\) en de x-as, van \(x = 0\) tot \(x = 3\)?",
        [r"\(\tfrac{8}{3}\)", r"\(0\)", r"\(\tfrac{4}{3}\)", r"\(4\)"],
        0,
        r"Splits in \(x = 1\): \(\int_{0}^{1}f\,dx = \tfrac{4}{3}\) en tel daar de absolute waarde van het stuk onder de as bij.",
    ),
    sorteer(
        "Is de integraal positief, negatief of nul?",
        ["Positief", "Negatief", "Nul"],
        [(r"\(\int_{0}^{\pi}\sin x\,dx\)", "Positief"), (r"\(\int_{-2}^{2}x^{3}\,dx\)", "Nul"), (r"\(\int_{0}^{1}(x - 2)\,dx\)", "Negatief"),
         (r"\(\int_{1}^{e}\ln x\,dx\)", "Positief"), (r"\(\int_{3}^{1}x^{2}\,dx\)", "Negatief"), (r"\(\int_{0}^{2\pi}\cos x\,dx\)", "Nul")],
        "Let op het teken van de functie en op grenzen die omgekeerd staan.",
    ),
    mk(
        r"Hoe groot is de oppervlakte tussen \(y = 4 - x^{2}\) en \(y = x + 2\)?",
        [r"\(\tfrac{9}{2}\)", r"\(\tfrac{7}{6}\)", r"\(\tfrac{27}{2}\)", r"\(3\)"],
        0,
        r"Snijpunten \(x = -2\) en \(x = 1\). \(\int_{-2}^{1}(2 - x - x^{2})\,dx = \tfrac{7}{6} + \tfrac{10}{3} = \tfrac{9}{2}\).",
    ),
    volgorde(
        "Zet de stappen om de oppervlakte tussen twee krommen te berekenen in volgorde.",
        ["maak een schets", "zoek de snijpunten", "bepaal welke kromme boven ligt", "integreer boven min onder", "tel de stukken op als ze van rol wisselen"],
        "De schets helpt je de rest goed te doen.",
    ),
    mk(
        r"Je laat \(y = \sqrt{x}\) op \([0,\ 4]\) wentelen om de x-as. Wat is de inhoud?",
        [r"\(8\pi\)", r"\(\tfrac{16}{3}\pi\)", r"\(4\pi\)", r"\(16\pi\)"],
        0,
        r"\(V = \pi\int_{0}^{4}x\,dx = \pi\cdot 8\).",
    ),
    inv(
        r"De rechte \(y = x\) op \([0,\ 3]\) wentelt om de x-as en vormt een kegel. De inhoud is \(k\pi\). Hoeveel is \(k\)?",
        ["9"],
        r"\(\pi\int_{0}^{3}x^{2}\,dx = 9\pi\), net als \(\tfrac{1}{3}\pi r^{2}h\) met \(r = h = 3\).",
    ),
    casus(
        r"Een fietser rijdt met snelheid \(v(t) = t - 2\) m/s, met \(t\) in seconden, van \(t = 0\) tot \(t = 4\). Een negatieve snelheid betekent achteruit.",
        [
            inv(r"Hoeveel is \(\int_{0}^{4}v(t)\,dt\)? Schrijf het getal.", ["0"], r"\(\left[\tfrac{t^{2}}{2} - 2t\right]_{0}^{4} = 8 - 8\)."),
            inv(r"Hoeveel meter legt de fietser in totaal af?", ["4"], r"2 m achteruit tot \(t = 2\), dan 2 m vooruit."),
            mk("Wat stelt het eerste antwoord voor?", ["de verplaatsing", "de afgelegde weg", "de gemiddelde snelheid", "de versnelling"], 0, "De integraal van de snelheid is de verplaatsing."),
        ],
    ),
    tabel(
        "Juist of fout?",
        [(r"\(\int_{a}^{b}f(x)\,dx + \int_{b}^{c}f(x)\,dx = \int_{a}^{c}f(x)\,dx\)", J), (r"\(\int_{a}^{b}k\,f(x)\,dx = k\int_{a}^{b}f(x)\,dx\)", J), (r"\(\int_{a}^{b}f(x)^{2}\,dx = \left(\int_{a}^{b}f(x)\,dx\right)^{2}\)", F), (r"\(\int_{-a}^{a}x^{5}\,dx = 0\)", J), (r"\(\int_{a}^{b}f(x)\,dx \geq 0\) zodra \(b > a\)", F)],
        r"Kwadrateren en integreren mag je niet van plaats wisselen. Of de integraal positief is, hangt ook van het teken van \(f\) af.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        r"Je benadert \(\int_{0}^{2}x\,dx\) met 4 rechthoekjes van breedte \(\tfrac{1}{2}\).",
        [
            inv("Hoeveel is de ondersom? Geef een decimaal getal.", ["1,5", "1.5"], r"\(\tfrac{1}{2}(0 + 0{,}5 + 1 + 1{,}5)\)."),
            inv("Hoeveel is de bovensom? Geef een decimaal getal.", ["2,5", "2.5"], r"\(\tfrac{1}{2}(0{,}5 + 1 + 1{,}5 + 2)\)."),
            mk("Wat gebeurt er met het verschil tussen bovensom en ondersom als je 8 rechthoekjes neemt?", ["het halveert", "het blijft gelijk", "het verdubbelt", "het wordt nul"], 0,
               r"Het verschil is hier \(f(2) - f(0)\) maal de breedte, en die breedte halveert."),
        ],
    ),
    mk(
        r"Wat is \(\dfrac{d}{dx}\int_{1}^{x}t^{2}\,dt\)?",
        [r"\(x^{2}\)", r"\(\tfrac{x^{3}}{3}\)", r"\(x^{2} - 1\)", r"\(2x\)"],
        0,
        r"\(\tfrac{x^{3}}{3} - \tfrac{1}{3}\) afleiden geeft \(x^{2}\): de hoofdstelling.",
    ),
    koppel(
        "Verbind de toepassing met de formule.",
        [("oppervlakte tussen twee krommen", r"\(\int_{a}^{b}(f - g)\,dx\)"), ("inhoud bij wenteling om de x-as", r"\(\pi\int_{a}^{b}f(x)^{2}\,dx\)"), ("booglengte", r"\(\int_{a}^{b}\sqrt{1 + f'(x)^{2}}\,dx\)"), ("gemiddelde waarde", r"\(\tfrac{1}{b - a}\int_{a}^{b}f(x)\,dx\)")],
        [r"\(\int_{a}^{b}f'(x)\,dx\)"],
        "Elke toepassing is een integraal van een andere uitdrukking.",
    ),
    inv(
        r"Wat is de gemiddelde waarde van \(f(x) = x^{2}\) op \([0,\ 3]\)?",
        ["3", "drie"],
        r"\(\tfrac{1}{3}\int_{0}^{3}x^{2}\,dx = \tfrac{1}{3}\cdot 9\).",
    ),
    mk(
        r"De middelwaardestelling geeft een \(c\) in \([0,\ 3]\) met \(c^{2}\) gelijk aan de gemiddelde waarde van \(x^{2}\). Welke \(c\)?",
        [r"\(\sqrt{3}\)", r"\(\tfrac{3}{2}\)", r"\(3\)", r"\(\tfrac{\sqrt{3}}{2}\)"],
        0,
        r"\(c^{2} = 3\) en \(c\) ligt in het interval.",
    ),
    inv(
        r"Bereken de booglengte van \(y = \tfrac{2}{3}x\sqrt{x}\) op \([0,\ 3]\). Schrijf het antwoord als breuk.",
        ["14/3"],
        r"\(f'(x) = \sqrt{x}\), dus \(\int_{0}^{3}\sqrt{1 + x}\,dx = \tfrac{2}{3}\left[(1 + x)\sqrt{1 + x}\right]_{0}^{3} = \tfrac{2}{3}(8 - 1)\).",
    ),
    keuze(
        r"Een integraal over een stuk onder de x-as is [[*negatief|positief|nul]]. De werkelijke oppervlakte van dat stuk is [[*positief|negatief|nul]].",
        "De integraal is een georiënteerde oppervlakte.",
    ),
    mk(
        r"De marginale kost is \(K'(q) = 10 + 0{,}2q\) euro per stuk. Met hoeveel stijgt de totale kost als de productie van 100 naar 200 stuks gaat?",
        ["4000 euro", "1000 euro", "6000 euro", "50 euro"],
        0,
        r"\(\left[10q + 0{,}1q^{2}\right]_{100}^{200} = 6000 - 2000\).",
    ),
    tabel(
        "Welke eenheid heeft de integraal?",
        [(r"debiet in l/min, over minuten", "l"), (r"versnelling in m/s², over seconden", "m/s"), (r"vermogen in W, over seconden", "J"), (r"snelheid in km/h, over uren", "km")],
        "De eenheid van de integraal is die van de functie maal die van de veranderlijke.",
        kolommen=["l", "m/s", "J", "km"],
    ),
    inv(
        r"Uit een kraan loopt water met debiet \(3t^{2}\) liter per minuut. Hoeveel liter loopt er in de eerste 2 minuten uit?",
        ["8"],
        r"\(\int_{0}^{2}3t^{2}\,dt = \left[t^{3}\right]_{0}^{2}\).",
    ),
    sleep(
        r"Een Riemannsom telt [[rechthoekjes]] op. Hoe [[smaller]] ze worden, hoe beter de benadering. De limiet is de [[bepaalde integraal]].",
        ["driehoekjes", "breder", "afgeleide"],
        "Onder- en bovensom kruipen naar hetzelfde getal.",
    ),
    mk(
        r"Welke uitdrukking geeft de oppervlakte tussen \(y = \sin x\) en de x-as op \([0,\ 2\pi]\)?",
        [r"\(2\int_{0}^{\pi}\sin x\,dx\)", r"\(\int_{0}^{2\pi}\sin x\,dx\)", r"\(\int_{0}^{\pi}\sin x\,dx\)", r"\(\pi\int_{0}^{2\pi}\sin^{2}x\,dx\)"],
        0,
        r"Over \([\pi,\ 2\pi]\) ligt de grafiek onder de as; door symmetrie is dat stuk even groot als het eerste.",
    ),
    tabel(
        r"De grafiek van \(f\) heeft een sprong in \(x = 2\). Juist of fout?",
        [(r"Je kan \(\int_{0}^{4}f(x)\,dx\) berekenen door te splitsen in \(x = 2\).", J), (r"\(F(4) - F(0)\) met één formule voor \(F\) geeft altijd het juiste resultaat.", F), (r"Een sprong verandert niets aan de oppervlakte van een rechthoekje van breedte nul.", J)],
        "De hoofdstelling vraagt een continue functie op het interval; splits daarom in de sprong.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Welke integraal geeft de inhoud als je \(y = x^{2}\) op \([0,\ 1]\) om de x-as laat wentelen?",
        [r"\(\pi\int_{0}^{1}x^{4}\,dx\)", r"\(\pi\int_{0}^{1}x^{2}\,dx\)", r"\(\int_{0}^{1}x^{4}\,dx\)", r"\(2\pi\int_{0}^{1}x^{2}\,dx\)"],
        0,
        r"Kwadrateer de functie: \((x^{2})^{2} = x^{4}\). De inhoud is \(\tfrac{\pi}{5}\).",
    ),
]
