"""Primitieven en de onbepaalde integraal — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone

GRAF = venster("primitieven-familie-bey", -3, 3, -3, 7)

GRAFIEKEN = [
    dict(naam=GRAF, titel="Drie primitieven A, B en C van f(x) = 2x",
         krommen=[(lambda x: x * x + 2, "groen", "A", (-2.2, 2.2)), (lambda x: x * x, "blauw", "B", (-2.6, 2.6)), (lambda x: x * x - 2, "oranje", "C", (-2.9, 2.9))],
         labelplek={"A": (-2.0, 6.6), "B": (-2.45, 6.4), "C": (2.75, 5.6)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="drie parabolen x² + 2, x² en x² − 2", vragen="klikvragen over de integratieconstante")]

VRAGEN = [
    klik(
        r"Klik op het punt van de primitieve van \(2x\) die door \((1, 3)\) gaat.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 1, 3)],
        r"\(F(x) = x^{2} + C\) met \(1 + C = 3\), dus \(C = 2\): de bovenste parabool A.",
    ),
    klik(
        r"Klik op het punt waar de primitieve met \(F(0) = -2\) de y-as snijdt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0, -2)],
        r"\(C = -2\): parabool C door \((0, -2)\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de drie primitieven. Juist of fout?",
        [("De drie grafieken zijn verticaal verschoven ten opzichte van elkaar.", J), ("In x = 1 hebben de drie grafieken dezelfde helling.", J), ("Er is maar één van de drie een echte primitieve van 2x.", F), ("Het verschil tussen A en C is overal 4.", J)],
        r"Alle drie hebben afgeleide \(2x\): ze verschillen enkel in de constante.",
        kolommen=["Juist", "Fout"],
    )),
    tabel(
        "Wat is de primitieve?",
        [(r"\(\int x^{-3}\,dx\)", r"\(-\dfrac{1}{2x^{2}} + C\)"), (r"\(\int \sqrt{x}\,dx\)", r"\(\tfrac{2}{3}x\sqrt{x} + C\)"), (r"\(\int \dfrac{3}{x}\,dx\)", r"\(3\ln|x| + C\)"), (r"\(\int e^{2x}\,dx\)", r"\(\tfrac{1}{2}e^{2x} + C\)")],
        r"Macht plus één en delen door de nieuwe exponent, behalve bij \(x^{-1}\).",
        kolommen=[r"\(-\dfrac{1}{2x^{2}} + C\)", r"\(\tfrac{2}{3}x\sqrt{x} + C\)", r"\(3\ln|x| + C\)", r"\(\tfrac{1}{2}e^{2x} + C\)"],
    ),
    mk(
        r"Bereken \(\int (3x^{2} - 4x + 5)\,dx\).",
        [r"\(x^{3} - 2x^{2} + 5x + C\)", r"\(6x - 4 + C\)", r"\(x^{3} - 4x^{2} + 5x + C\)", r"\(3x^{3} - 2x^{2} + 5 + C\)"],
        0,
        r"Splitsen: \(\int 3x^{2}\,dx = x^{3}\), \(\int 4x\,dx = 2x^{2}\), \(\int 5\,dx = 5x\).",
    ),
    mk(
        r"Bereken \(\int 2x(x^{2} + 1)^{4}\,dx\).",
        [r"\(\tfrac{1}{5}(x^{2} + 1)^{5} + C\)", r"\((x^{2} + 1)^{5} + C\)", r"\(\tfrac{2}{5}x(x^{2} + 1)^{5} + C\)", r"\(\tfrac{1}{5}x^{2}(x^{2} + 1)^{5} + C\)"],
        0,
        r"Substitutie \(u = x^{2} + 1\), \(du = 2x\,dx\): \(\int u^{4}\,du = \tfrac{u^{5}}{5}\).",
    ),
    mk(
        r"Bereken \(\int x e^{x}\,dx\).",
        [r"\((x - 1)e^{x} + C\)", r"\(\tfrac{x^{2}}{2}e^{x} + C\)", r"\(xe^{x} + C\)", r"\((x + 1)e^{x} + C\)"],
        0,
        r"Partieel met \(u = x\), \(v' = e^{x}\): \(xe^{x} - \int e^{x}\,dx\).",
    ),
    sorteer(
        "Welke methode pak je eerst?",
        ["Substitutie", "Partiële integratie", "Splitsen"],
        [(r"\(\int \cos x\,e^{\sin x}\,dx\)", "Substitutie"), (r"\(\int x\ln x\,dx\)", "Partiële integratie"), (r"\(\int \left(x^{2} + \tfrac{1}{x}\right)dx\)", "Splitsen"),
         (r"\(\int \dfrac{2x}{x^{2} + 4}\,dx\)", "Substitutie"), (r"\(\int x\sin x\,dx\)", "Partiële integratie"), (r"\(\int (e^{x} - 3x)\,dx\)", "Splitsen")],
        "Staat de afgeleide van een binnenste functie erbij: substitutie. Een product van twee verschillende soorten functies: partieel.",
    ),
    inv(
        r"\(F\) is een primitieve van \(f(x) = 6x^{2}\) met \(F(1) = 5\). Hoeveel is \(F(2)\)?",
        ["19"],
        r"\(F(x) = 2x^{3} + C\), \(2 + C = 5\), \(C = 3\). \(F(2) = 16 + 3 = 19\).",
    ),
    koppel(
        "Verbind de integraal met haar uitkomst.",
        [(r"\(\int \sin x\,dx\)", r"\(-\cos x + C\)"), (r"\(\int \dfrac{1}{\cos^{2}x}\,dx\)", r"\(\tan x + C\)"), (r"\(\int \cos 3x\,dx\)", r"\(\tfrac{1}{3}\sin 3x + C\)"), (r"\(\int \dfrac{1}{1 + x^{2}}\,dx\)", r"\(\arctan x + C\)")],
        [r"\(\cos x + C\)"],
        r"De afgeleide van \(\cos x\) is \(-\sin x\), dus \(\int \sin x\,dx = -\cos x + C\).",
    ),
    tabel(
        "Juist of fout?",
        [(r"\(\int f(x)g(x)\,dx = \int f(x)\,dx \cdot \int g(x)\,dx\)", F), (r"\(\int (f + g)\,dx = \int f\,dx + \int g\,dx\)", J), (r"\(\int \dfrac{1}{x^{2}}\,dx = \ln x^{2} + C\)", F), (r"Twee primitieven van dezelfde functie verschillen een constante.", J), (r"\(\int 0\,dx = C\)", J)],
        r"Er is geen productregel voor integralen. \(\int x^{-2}\,dx = -\tfrac{1}{x} + C\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Bereken \(\int \dfrac{x^{2} + 1}{x}\,dx\) voor \(x > 0\).",
        [r"\(\tfrac{x^{2}}{2} + \ln x + C\)", r"\(\tfrac{x^{3}/3 + x}{x^{2}/2} + C\)", r"\(x + \ln x + C\)", r"\(\tfrac{x^{2}}{2} - \tfrac{1}{x^{2}} + C\)"],
        0,
        r"Eerst splitsen: \(x + \tfrac{1}{x}\).",
    ),
    casus(
        r"Je berekent \(\int x\ln x\,dx\) met partiële integratie.",
        [
            mk("Welke keuze werkt?", [r"\(u = \ln x\), \(v' = x\)", r"\(u = x\), \(v' = \ln x\)", r"\(u = x\ln x\), \(v' = 1\)", r"geen van beide"], 0, r"\(\ln x\) afleiden maakt het eenvoudiger; \(\ln x\) primitiveren niet."),
            mk("Wat is dan v?", [r"\(\tfrac{x^{2}}{2}\)", r"\(1\)", r"\(x^{2}\)", r"\(\tfrac{1}{x}\)"], 0, r"Primitieve van \(x\)."),
            mk("Wat is de uitkomst?", [r"\(\tfrac{x^{2}}{2}\ln x - \tfrac{x^{2}}{4} + C\)", r"\(\tfrac{x^{2}}{2}\ln x + C\)", r"\(x\ln x - x + C\)", r"\(\tfrac{x^{2}}{2}\ln x - \tfrac{x^{2}}{2} + C\)"], 0,
               r"\(\tfrac{x^{2}}{2}\ln x - \int \tfrac{x^{2}}{2}\cdot\tfrac{1}{x}\,dx = \tfrac{x^{2}}{2}\ln x - \tfrac{x^{2}}{4}\)."),
        ],
    ),
    keuze(
        r"Integratie door substitutie is de [[*kettingregel|productregel|quotiëntregel]] omgekeerd. Partiële integratie is de [[*productregel|kettingregel|somregel]] omgekeerd.",
        "Elke integratiemethode hoort bij een afleidingsregel.",
    ),
    inv(
        r"Bereken \(\int_{0}^{1}(4x^{3} + 1)\,dx\).",
        ["2"],
        r"\(\left[x^{4} + x\right]_{0}^{1} = 2\).",
    ),
    mk(
        r"Bereken \(\int \tan x\,dx\).",
        [r"\(-\ln|\cos x| + C\)", r"\(\ln|\cos x| + C\)", r"\(\dfrac{1}{\cos^{2}x} + C\)", r"\(\ln|\sin x| + C\)"],
        0,
        r"\(\tan x = \dfrac{\sin x}{\cos x} = -\dfrac{(\cos x)'}{\cos x}\).",
    ),
    tabel(
        r"Is \(F\) een primitieve van \(f\)?",
        [(r"\(F(x) = \ln(x^{2} + 1)\), \(f(x) = \dfrac{2x}{x^{2} + 1}\)", J), (r"\(F(x) = \sin^{2}x\), \(f(x) = \sin 2x\)", J), (r"\(F(x) = e^{x^{2}}\), \(f(x) = e^{x^{2}}\)", F), (r"\(F(x) = -\cos^{2}x\), \(f(x) = \sin 2x\)", J)],
        r"Controleer door \(F\) af te leiden. \(\sin^{2}x\) en \(-\cos^{2}x\) verschillen \(1\): allebei primitieven van \(\sin 2x\).",
        kolommen=["Juist", "Fout"],
    ),
    sleep(
        r"Bij \(\int x^{n}\,dx\) verhoog je de exponent met [[1]] en deel je door [[de nieuwe exponent]]. Dat werkt niet voor \(n =\) [[−1]].",
        ["2", "de oude exponent", "0"],
        r"Voor \(n = -1\) krijg je \(\ln|x|\).",
    ),
    mk(
        r"Een snelheid is \(v(t) = 3t^{2} - 2t\) m/s. Bij \(t = 0\) is de positie 4 m. Wat is de positie bij \(t = 2\)?",
        ["8 m", "4 m", "12 m", "10 m"],
        0,
        r"\(s(t) = t^{3} - t^{2} + 4\), \(s(2) = 8 - 4 + 4 = 8\).",
    ),
    volgorde(
        r"Zet de stappen van de substitutie bij \(\int x\cos(x^{2})\,dx\) in volgorde.",
        [r"kies \(u = x^{2}\)", r"\(du = 2x\,dx\), dus \(x\,dx = \tfrac{1}{2}du\)", r"schrijf \(\tfrac{1}{2}\int \cos u\,du\)", r"integreer: \(\tfrac{1}{2}\sin u + C\)", r"terug naar x: \(\tfrac{1}{2}\sin(x^{2}) + C\)"],
        "Vergeet niet terug te keren naar de oorspronkelijke veranderlijke.",
    ),
    inv(
        r"Bereken \(\int_{1}^{e}\dfrac{1}{x}\,dx\).",
        ["1"],
        r"\(\ln e - \ln 1 = 1\).",
    ),
    mk(
        r"Bereken \(\int \sin^{2}x\,dx\) met \(\sin^{2}x = \tfrac{1 - \cos 2x}{2}\).",
        [r"\(\tfrac{x}{2} - \tfrac{\sin 2x}{4} + C\)", r"\(\tfrac{\sin^{3}x}{3} + C\)", r"\(\tfrac{x}{2} + \tfrac{\sin 2x}{4} + C\)", r"\(-\cos^{2}x + C\)"],
        0,
        r"\(\tfrac{1}{2}\int 1\,dx - \tfrac{1}{2}\int\cos 2x\,dx\).",
    ),
    tabel(
        "Controleer door af te leiden: klopt de primitieve?",
        [(r"\(\int \ln x\,dx = x\ln x - x + C\)", J), (r"\(\int \dfrac{1}{2x + 1}\,dx = \ln|2x + 1| + C\)", F), (r"\(\int 2^{x}\,dx = \dfrac{2^{x}}{\ln 2} + C\)", J)],
        r"\((\ln|2x + 1|)' = \tfrac{2}{2x + 1}\): er ontbreekt een factor \(\tfrac{1}{2}\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Welke functie heeft als primitieve \(F(x) = x^{2}e^{x}\)?",
        [r"\((x^{2} + 2x)e^{x}\)", r"\(2xe^{x}\)", r"\(x^{2}e^{x}\)", r"\(\tfrac{x^{3}}{3}e^{x}\)"],
        0,
        r"Leid \(F\) af met de productregel.",
    ),
    inv(
        r"Voor welke \(a\) is \(\int_{0}^{a} 2x\,dx = 9\), met \(a > 0\)?",
        ["3"],
        r"\(a^{2} = 9\).",
    ),
    mk(
        r"Bereken \(\int \dfrac{e^{x}}{e^{x} + 1}\,dx\).",
        [r"\(\ln(e^{x} + 1) + C\)", r"\(x - \ln(e^{x} + 1) + C\)", r"\(\dfrac{e^{x}}{x} + C\)", r"\(e^{x}\ln(e^{x} + 1) + C\)"],
        0,
        r"De teller is de afgeleide van de noemer: \(\int \tfrac{f'}{f}\,dx = \ln|f| + C\).",
    ),
    tabel(
        r"Na de substitutie \(u = 2x + 1\) in \(\int_{0}^{1}(2x + 1)^{3}\,dx\): juist of fout?",
        [(r"De nieuwe grenzen zijn 1 en 3.", J), (r"\(dx = 2\,du\)", F), (r"De integraal wordt \(\tfrac{1}{2}\int_{1}^{3}u^{3}\,du\).", J), (r"De uitkomst is 10.", J)],
        r"\(dx = \tfrac{1}{2}du\); \(\tfrac{1}{2}\cdot\tfrac{81 - 1}{4} = 10\).",
        kolommen=["Juist", "Fout"],
    ),
    inv(
        r"Euclidische deling geeft \(\dfrac{x^{2} + 3x + 3}{x + 1} = x + 2 + \dfrac{1}{x + 1}\). Hoeveel is \(\int_{0}^{1}(x + 2)\,dx\)? Geef een decimaal getal.",
        ["2,5", "2.5"],
        r"\(\left[\tfrac{x^{2}}{2} + 2x\right]_{0}^{1} = 2{,}5\). De volledige integraal is dan \(2{,}5 + \ln 2\).",
    ),
]
