"""Limieten, continuïteit en asymptoten — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone, vak_zone

GRAF = venster("limieten-rationaal-bey", -5, 8, -8, 12)


def _f(x):
    return (x * x - 1) / (x - 2) if abs(x - 2) > 1e-9 else None


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafiek van f(x) = (x² − 1)/(x − 2) met haar asymptoten",
         krommen=[(_f, "groen", "f", (-5, 8)), (lambda x: x + 2, "#9a9a9a", "", (-5, 8))],
         stippel=[("v", 2)], labelplek={"f": (6.6, 11)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="rationale functie met verticale asymptoot x = 2 en schuine asymptoot y = x + 2 (grijs)", vragen="klikvragen over asymptoten en nulwaarden")]

VRAGEN = [
    klik(
        "Klik op de verticale asymptoot, op de hoogte van de x-as.",
        f"{GRAF}.svg",
        [vak_zone(GRAF, 1.6, 2.4, -1, 1)],
        r"De noemer is nul bij \(x = 2\) en de teller niet (\(4 - 1 = 3\)): een pool, dus een verticale asymptoot.",
    ),
    klik(
        "Klik op het snijpunt van de grafiek met de y-as.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 0, 0.5)],
        r"\(f(0) = \tfrac{-1}{-2} = \tfrac{1}{2}\).",
    ),
    klik(
        "Klik op de grootste nulwaarde van f.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 1, 0)],
        r"\(x^{2} - 1 = 0\) geeft \(x = \pm 1\). Beide liggen links van de asymptoot.",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafiek. Juist of fout?",
        [(r"\(\lim\limits_{x \to 2^{+}} f(x) = +\infty\)", J), (r"\(\lim\limits_{x \to 2^{-}} f(x) = +\infty\)", F), ("De grijze rechte y = x + 2 is een schuine asymptoot.", J), ("f heeft een horizontale asymptoot.", F), ("f is continu in x = 2.", F)],
        r"Links van 2 is de noemer negatief en de teller positief: \(-\infty\). Een schuine asymptoot sluit een horizontale aan dezelfde kant uit.",
        kolommen=["Juist", "Fout"],
    )),
    met_prent(f"{GRAF}.svg", mk(
        "Kijk naar de grafiek. Hoe vind je de grijze asymptoot algebraïsch?",
        [r"door \(x^{2} - 1\) te delen door \(x - 2\): het quotiënt is \(x + 2\)", r"door \(f(0)\) te berekenen en die waarde als snijpunt te nemen", r"door de noemer nul te stellen en \(x = 2\) op te lossen", r"door \(\lim\limits_{x \to 2} f(x)\) te berekenen van beide kanten"],
        0,
        r"\(x^{2} - 1 = (x - 2)(x + 2) + 3\), dus \(f(x) = x + 2 + \tfrac{3}{x - 2}\). De breuk gaat naar 0 op oneindig.",
    )),
    tabel(
        "Bereken de limiet.",
        [(r"\(\lim\limits_{x \to 3}\dfrac{x^{2} - 9}{x - 3}\)", r"\(6\)"), (r"\(\lim\limits_{x \to +\infty}\dfrac{5x^{3} - x}{2x^{3} + 4}\)", r"\(\tfrac{5}{2}\)"), (r"\(\lim\limits_{x \to +\infty}\dfrac{x + 1}{x^{2}}\)", r"\(0\)"), (r"\(\lim\limits_{x \to 0}\dfrac{\sin x}{x}\)", r"\(1\)")],
        "Ontbinden bij 0/0, hoogste machten op oneindig, en de standaardlimiet van sin x / x.",
        kolommen=[r"\(6\)", r"\(\tfrac{5}{2}\)", r"\(0\)", r"\(1\)"],
    ),
    mk(
        r"Hoeveel is \(\lim\limits_{x \to +\infty}\left(\sqrt{x^{2} + 6x} - x\right)\)?",
        [r"\(3\)", r"\(0\)", r"\(+\infty\)", r"\(6\)"],
        0,
        r"Vermenigvuldig met de toegevoegde: \(\dfrac{6x}{\sqrt{x^{2} + 6x} + x} \to \dfrac{6}{2} = 3\).",
    ),
    sorteer(
        "Is dit een onbepaaldheid?",
        ["Onbepaald", "Niet onbepaald"],
        [(r"\(\tfrac{0}{0}\)", "Onbepaald"), (r"\(\tfrac{\infty}{\infty}\)", "Onbepaald"), (r"\(\infty - \infty\)", "Onbepaald"), (r"\(0 \cdot \infty\)", "Onbepaald"), (r"\(\tfrac{5}{\infty}\)", "Niet onbepaald"), (r"\(\infty + \infty\)", "Niet onbepaald")],
        r"\(\tfrac{5}{\infty} = 0\) en \(\infty + \infty = \infty\). Bij een onbepaaldheid moet je eerst herschrijven.",
    ),
    mk(
        r"Welke uitspraak over \(f(x) = \dfrac{x^{2} - 4}{x^{2} - 2x}\) klopt?",
        [r"perforatie bij \(x = 2\), verticale asymptoot \(x = 0\)", r"verticale asymptoten \(x = 0\) en \(x = 2\)", r"perforatie bij \(x = 0\), asymptoot \(x = 2\)", "geen asymptoten"],
        0,
        r"\(\dfrac{(x - 2)(x + 2)}{x(x - 2)} = \dfrac{x + 2}{x}\) voor \(x \neq 2\). Bij \(x = 2\) ontbreekt enkel een punt, bij \(x = 0\) is er een pool.",
    ),
    inv(
        r"Voor welke \(k\) is \(f(x) = \begin{cases} x^{2} + k & x < 1 \\ 3x - 1 & x \geq 1 \end{cases}\) continu?",
        ["1"],
        r"Linkerlimiet \(1 + k\), rechterlimiet \(f(1) = 2\). Gelijk als \(k = 1\).",
    ),
    koppel(
        "Verbind de functie met haar asymptoten.",
        [(r"\(\dfrac{2x + 1}{x - 4}\)", r"\(x = 4\) en \(y = 2\)"), (r"\(\dfrac{x^{2}}{x + 1}\)", r"\(x = -1\) en \(y = x - 1\)"), (r"\(\dfrac{3}{x^{2} + 1}\)", r"enkel \(y = 0\)"), (r"\(e^{x}\)", r"\(y = 0\) links")],
        [r"\(x = 0\) en \(y = 1\)"],
        r"\(x^{2} = (x + 1)(x - 1) + 1\). \(x^{2} + 1\) is nooit nul.",
    ),
    mk(
        r"Hoeveel is \(\lim\limits_{x \to 0}\dfrac{e^{x} - 1}{x}\) met de regel van de l'Hôpital?",
        [r"\(1\)", r"\(0\)", r"\(e\)", r"\(+\infty\)"],
        0,
        r"Vorm \(\tfrac{0}{0}\): afleiden geeft \(\dfrac{e^{x}}{1} \to 1\).",
    ),
    casus(
        r"Gegeven \(f(x) = \dfrac{2x^{2} - 8}{x^{2} - x - 2}\).",
        [
            mk("Ontbind teller en noemer.", [r"\(\dfrac{2(x - 2)(x + 2)}{(x - 2)(x + 1)}\)", r"\(\dfrac{2(x - 4)(x + 4)}{(x - 2)(x + 1)}\)", r"\(\dfrac{2(x - 2)^{2}}{(x + 2)(x - 1)}\)", r"\(\dfrac{(2x - 4)(x + 2)}{(x + 2)(x - 1)}\)"], 0, r"\(2(x^{2} - 4)\) en \(x^{2} - x - 2 = (x - 2)(x + 1)\)."),
            inv(r"Hoeveel is \(\lim\limits_{x \to 2} f(x)\)? Typ als breuk.", ["8/3"], r"\(\dfrac{2(x + 2)}{x + 1} \to \dfrac{8}{3}\)."),
            mk("Welke verticale asymptoot heeft f?", [r"\(x = -1\)", r"\(x = 2\)", r"\(x = -2\)", "geen"], 0, "Enkel bij x = −1 blijft de noemer nul na het schrappen."),
            mk("Welke horizontale asymptoot?", [r"\(y = 2\)", r"\(y = 0\)", r"\(y = 1\)", "geen"], 0, "Graad teller = graad noemer: verhouding van de hoogste coëfficiënten."),
        ],
    ),
    tabel(
        "Juist of fout?",
        [("Een functie kan haar horizontale asymptoot snijden.", J), ("Een functie kan haar verticale asymptoot snijden.", F), ("Elke rationale functie heeft een verticale asymptoot.", F), ("Een continue functie op [a, b] die van teken wisselt, heeft een nulwaarde in ]a, b[.", J), ("Elke afleidbare functie is continu.", J)],
        r"Bij een verticale asymptoot bestaat \(f\) niet. \(\tfrac{1}{x^{2} + 1}\) heeft geen pool. De laatste twee zijn stellingen uit de leerstof.",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        r"Is de graad van de teller [[*één hoger dan|gelijk aan|kleiner dan]] die van de noemer, dan heeft een rationale functie een schuine asymptoot. Is ze kleiner, dan is de horizontale asymptoot [[*\(y = 0\)|\(y = 1\)|de x-as niet]].",
        "Vergelijk de hoogste machten.",
    ),
    mk(
        r"Hoeveel is \(\lim\limits_{x \to -\infty}\dfrac{\sqrt{4x^{2} + 1}}{x}\)?",
        [r"\(-2\)", r"\(2\)", r"\(0\)", r"\(-\infty\)"],
        0,
        r"\(\sqrt{4x^{2} + 1} \approx 2|x| = -2x\) voor negatieve \(x\). Dus \(\tfrac{-2x}{x} = -2\).",
    ),
    inv(
        r"Bereken \(\lim\limits_{x \to 4}\dfrac{\sqrt{x} - 2}{x - 4}\). Typ als breuk.",
        ["1/4", "0,25", "0.25"],
        r"\(x - 4 = (\sqrt{x} - 2)(\sqrt{x} + 2)\), dus de limiet is \(\tfrac{1}{\sqrt{4} + 2} = \tfrac{1}{4}\).",
    ),
    sleep(
        r"Een functie is continu in \(a\) als \(f(a)\) [[bestaat]], de limiet in \(a\) bestaat en die twee [[gelijk]] zijn.",
        ["nul is", "verschillend"],
        "Drie voorwaarden: waarde, limiet en gelijkheid.",
    ),
    tabel(
        "Wat is de eenzijdige limiet?",
        [(r"\(\lim\limits_{x \to 1^{-}}\dfrac{1}{x - 1}\)", r"\(-\infty\)"), (r"\(\lim\limits_{x \to 1^{+}}\dfrac{1}{x - 1}\)", r"\(+\infty\)"), (r"\(\lim\limits_{x \to 1^{-}}\dfrac{1}{(x - 1)^{2}}\)", r"\(+\infty\)"), (r"\(\lim\limits_{x \to 0^{+}}\ln x\)", r"\(-\infty\)")],
        "Kijk naar het teken van de noemer net links of rechts. Een kwadraat is altijd positief.",
        kolommen=[r"\(-\infty\)", r"\(+\infty\)"],
    ),

    mk(
        r"De schuine asymptoot van \(f(x) = \dfrac{2x^{2} + 3x}{x - 1}\) is…",
        [r"\(y = 2x + 5\)", r"\(y = 2x + 3\)", r"\(y = 2x\)", r"\(y = x + 5\)"],
        0,
        r"Euclidische deling: \(2x^{2} + 3x = (x - 1)(2x + 5) + 5\).",
    ),
    volgorde(
        r"Zet de stappen om \(\lim\limits_{x \to +\infty}\dfrac{3x^{2} - x}{x^{2} + 2}\) te berekenen in volgorde.",
        [r"vaststellen: vorm \(\tfrac{\infty}{\infty}\)", r"\(x^{2}\) afzonderen in teller en noemer", r"vereenvoudigen tot \(\dfrac{3 - \tfrac{1}{x}}{1 + \tfrac{2}{x^{2}}}\)", r"de breuken met \(x\) in de noemer gaan naar 0", r"besluit: \(3\)"],
        "Eerst het type onbepaaldheid, dan de passende techniek.",
    ),
    inv(
        r"Hoeveel is \(\lim\limits_{x \to +\infty} x e^{-x}\)?",
        ["0", "nul"],
        r"Vorm \(\tfrac{x}{e^{x}}\) met \(\tfrac{\infty}{\infty}\): l'Hôpital geeft \(\tfrac{1}{e^{x}} \to 0\).",
    ),
    mk(
        r"Bij welke functie is \(x = 3\) een perforatie?",
        [r"\(\dfrac{x^{2} - 9}{x - 3}\)", r"\(\dfrac{x + 3}{x - 3}\)", r"\(\dfrac{1}{(x - 3)^{2}}\)", r"\(\sqrt{x - 3}\)"],
        0,
        r"Teller en noemer zijn beide nul bij \(x = 3\) en de factor valt weg: de limiet \(6\) bestaat, maar \(f(3)\) niet.",
    ),
    sorteer(
        r"Continu op heel \(\mathbb{R}\)?",
        ["Continu op ℝ", "Niet continu op ℝ"],
        [(r"\(x^{5} - 3x + 1\)", "Continu op ℝ"), (r"\(\tfrac{1}{x}\)", "Niet continu op ℝ"), (r"\(e^{-x^{2}}\)", "Continu op ℝ"), (r"\(\tan x\)", "Niet continu op ℝ"), (r"\(|x|\)", "Continu op ℝ")],
        r"\(|x|\) heeft een knik in 0 maar geen sprong: continu, niet afleidbaar.",
    ),
    inv(
        r"Hoeveel is \(\lim\limits_{x \to +\infty}\dfrac{\ln x}{x}\)?",
        ["0", "nul"],
        r"Vorm \(\tfrac{\infty}{\infty}\): l'Hôpital geeft \(\tfrac{1/x}{1} \to 0\). Een logaritme groeit trager dan x.",
    ),
    mk(
        r"Hoeveel is \(\lim\limits_{x \to 0}\dfrac{\sin 3x}{x}\)?",
        [r"\(3\)", r"\(1\)", r"\(\tfrac{1}{3}\)", r"\(0\)"],
        0,
        r"\(\dfrac{\sin 3x}{x} = 3 \cdot \dfrac{\sin 3x}{3x} \to 3\).",
    ),
    tabel(
        r"Over \(f(x) = \dfrac{x + 1}{x^{2} - 1}\). Juist of fout?",
        [(r"\(x = 1\) is een verticale asymptoot.", J), (r"\(x = -1\) is een verticale asymptoot.", F), (r"\(y = 0\) is een horizontale asymptoot.", J), (r"\(\lim\limits_{x \to -1} f(x) = -\tfrac{1}{2}\)", J)],
        r"\(f(x) = \tfrac{1}{x - 1}\) voor \(x \neq -1\): bij \(-1\) is er een perforatie.",
        kolommen=["Juist", "Fout"],
    ),
]
