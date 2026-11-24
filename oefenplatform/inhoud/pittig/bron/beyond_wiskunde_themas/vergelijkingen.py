"""Vergelijkingen en ongelijkheden oplossen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, strook_zone

GRAF = venster("vergelijkingen-f-en-g-bey", -3, 6, -5, 8)


def _f(x):
    return x * x - 2 * x - 3


def _g(x):
    return x + 1


GRAFIEKEN = [
    dict(naam=GRAF, titel="De grafieken van f en g", krommen=[(_f, "groen", "f", (-2.2, 5.1)), (_g, "blauw", "g", (-3, 6))],
         labelplek={"f": (5.3, 7.2), "g": (5.6, 5.6)}),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="parabool f(x) = x² − 2x − 3 en rechte g(x) = x + 1", vragen="klikvragen over vergelijkingen en ongelijkheden grafisch oplossen")]

VRAGEN = [
    klik(
        r"Klik op het snijpunt dat de grootste oplossing van \(f(x) = g(x)\) toont.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 4, 5)],
        r"\(x^{2} - 2x - 3 = x + 1\) geeft \(x^{2} - 3x - 4 = 0\): \(x = -1\) of \(x = 4\). Het rechtse snijpunt is \((4, 5)\).",
    ),
    klik(
        r"Klik in de strook van de \(x\)-waarden waarvoor \(f(x) < g(x)\).",
        f"{GRAF}.svg",
        [strook_zone(GRAF, -0.8, 3.8)],
        r"Tussen de snijpunten \(x = -1\) en \(x = 4\) ligt de parabool onder de rechte.",
    ),
    klik(
        r"Klik op de nulwaarde van \(f\) die geen oplossing is van \(f(x) = g(x)\).",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3, 0)],
        r"\(f\) heeft nulwaarden \(-1\) en \(3\). In \(-1\) snijden f en g elkaar ook, in \(3\) niet: \(g(3) = 4\).",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        "Kijk naar de grafieken. Juist of fout?",
        [(r"\(f(x) \geq 0\) voor \(x \in \left]-\infty, -1\right] \cup \left[3, +\infty\right[\)", J),
         (r"\(f(x) = g(x)\) heeft drie oplossingen.", F),
         (r"\(g(x) > 0\) voor \(x > -1\)", J),
         (r"\(f(x) \geq g(x)\) voor \(x \in \left[-1, 4\right]\)", F),
         (r"\(f(x) = -4\) heeft precies één oplossing.", J)],
        r"De top van f is \((1, -4)\): de horizontale rechte \(y = -4\) raakt de parabool. Tussen \(-1\) en \(4\) ligt f onder g.",
        kolommen=["Juist", "Fout"],
    )),
    mk(
        r"Los op: \(\sqrt{2x + 7} = x + 2\).",
        [r"\(x = 1\)", r"\(x = 1\) of \(x = -3\)", r"\(x = -3\)", "geen oplossing"],
        0,
        r"Kwadrateren: \(2x + 7 = x^{2} + 4x + 4\), \(x^{2} + 2x - 3 = 0\), \(x = 1\) of \(x = -3\). Controle: bij \(-3\) staat rechts \(-1\), een wortel is nooit negatief.",
    ),
    inv(
        r"Los op: \(\sqrt{x + 5} = \sqrt{3x - 1}\). Typ \(x\).",
        ["3", "x = 3", "x=3"],
        r"\(x + 5 = 3x - 1\) geeft \(x = 3\). Bestaansvoorwaarden: \(x \geq -5\) en \(x \geq \tfrac{1}{3}\), dus in orde.",
    ),
    tabel(
        "Wat is de oplossingenverzameling van de vergelijking met absolute waarde?",
        [(r"\(|x - 3| = 5\)", r"\(\{-2, 8\}\)"), (r"\(|2x + 1| = -3\)", r"\(\varnothing\)"), (r"\(|x| = 0\)", r"\(\{0\}\)"), (r"\(|x + 2| = 6\)", r"\(\{-8, 4\}\)")],
        "Een absolute waarde is nooit negatief. Anders zijn er twee gevallen: de uitdrukking is gelijk aan het getal of aan het tegengestelde.",
        kolommen=[r"\(\{-2, 8\}\)", r"\(\varnothing\)", r"\(\{0\}\)", r"\(\{-8, 4\}\)"],
    ),
    mk(
        r"Los op: \(\dfrac{x + 3}{x - 1} \leq 0\).",
        [r"\(\left[-3, 1\right[\)", r"\(\left[-3, 1\right]\)", r"\(\left]-\infty, -3\right] \cup \left]1, +\infty\right[\)", r"\(\left]-3, 1\right[\)"],
        0,
        r"Teller nul bij \(-3\) (mag), noemer nul bij \(1\) (mag niet). Tekentabel: negatief tussen \(-3\) en \(1\).",
    ),
    sorteer(
        "Welke stap kan het aantal oplossingen veranderen?",
        ["Kan oplossingen toevoegen of verliezen", "Verandert niets"],
        [("beide leden kwadrateren", "Kan oplossingen toevoegen of verliezen"),
         (r"beide leden delen door \(x - 2\)", "Kan oplossingen toevoegen of verliezen"),
         (r"bij beide leden \(5\) optellen", "Verandert niets"),
         (r"beide leden met \(-3\) vermenigvuldigen in een vergelijking", "Verandert niets"),
         (r"beide leden vermenigvuldigen met \(x\)", "Kan oplossingen toevoegen of verliezen")],
        r"Kwadrateren en vermenigvuldigen met een uitdrukking in \(x\) kunnen valse oplossingen toevoegen. Delen door \(x - 2\) verliest \(x = 2\).",
    ),
    inv(
        r"Los op: \(\log_{2}(x + 1) + \log_{2}(x - 1) = 3\). Typ \(x\).",
        ["3", "x = 3", "x=3"],
        r"\(\log_{2}(x^{2} - 1) = 3\) geeft \(x^{2} = 9\). \(x = -3\) valt weg door de bestaansvoorwaarde \(x > 1\).",
    ),
    mk(
        r"Voor welke \(m\) heeft \(x^{2} + mx + 9 = 0\) geen reële oplossingen?",
        [r"\(-6 < m < 6\)", r"\(m < -6\) of \(m > 6\)", r"\(m = 6\)", r"\(m > 0\)"],
        0,
        r"\(D = m^{2} - 36 < 0\) geeft \(-6 < m < 6\).",
    ),
    casus(
        r"Je lost \(x^{2} - 4x - 5 \geq 0\) op.",
        [
            mk("Wat zijn de nulwaarden?", [r"\(-1\) en \(5\)", r"\(1\) en \(-5\)", r"\(-1\) en \(-5\)", r"\(4\) en \(5\)"], 0, r"\((x + 1)(x - 5) = 0\)."),
            mk("Waar is de uitdrukking positief?", ["buiten de nulwaarden", "tussen de nulwaarden", "nergens", "overal"], 0, r"\(a = 1 > 0\): de parabool opent naar boven."),
            mk("Wat is de oplossingenverzameling van deze ongelijkheid?", [r"\(\left]-\infty, -1\right] \cup \left[5, +\infty\right[\)", r"\(\left[-1, 5\right]\)", r"\(\left]-\infty, -1\right[ \cup \left]5, +\infty\right[\)", r"\(\left]-1, 5\right[\)"], 0,
               r"Met \(\geq\) horen de nulwaarden er ook bij: gesloten haakjes."),
        ],
    ),
    tabel(
        "Over vergelijkingen en ongelijkheden: juist of fout?",
        [(r"\(x^{2} > x\) geldt voor elke \(x > 0\).", F),
         (r"Uit \(x^{2} > 4\) volgt \(x > 2\).", F),
         (r"\(x^{2} - 6x + 9 > 0\) geldt voor elke \(x \neq 3\).", J),
         (r"\(\tfrac{1}{x} < 1\) geldt voor elke \(x > 1\).", J),
         (r"\(-x^{2} - 1 < 0\) geldt voor elke reële \(x\).", J)],
        r"Voor \(x = \tfrac{1}{2}\) is \(x^{2} < x\). Uit \(x^{2} > 4\) volgt \(x > 2\) of \(x < -2\). \((x - 3)^{2} > 0\) behalve in \(3\).",
        kolommen=["Juist", "Fout"],
    ),
    keuze(
        r"Bij \(f(x) > g(x)\) zoek je de \(x\)-waarden waar de grafiek van \(f\) [[*boven|onder]] die van \(g\) ligt. De snijpunten horen er [[*niet|wel]] bij.",
        "Een strikte ongelijkheid sluit de gelijkheid uit.",
    ),
    inv(
        r"Los op: \(3^{x + 1} - 3^{x} = 54\). Typ \(x\).",
        ["3", "x = 3", "x=3"],
        r"\(3^{x}(3 - 1) = 54\) geeft \(3^{x} = 27\), dus \(x = 3\).",
    ),
    mk(
        r"Los op: \(\dfrac{2}{x} = x - 1\).",
        [r"\(x = 2\) of \(x = -1\)", r"\(x = 2\)", r"\(x = -2\) of \(x = 1\)", r"\(x = 0\) of \(x = 2\)"],
        0,
        r"Met \(x \neq 0\): \(2 = x^{2} - x\), \(x^{2} - x - 2 = 0\). Beide oplossingen zijn toegelaten.",
    ),
    koppel(
        "Welke bestaansvoorwaarde hoort erbij?",
        [(r"\(\sqrt{5 - x}\)", r"\(x \leq 5\)"), (r"\(\ln(x + 2)\)", r"\(x > -2\)"), (r"\(\dfrac{1}{x^{2} - 4}\)", r"\(x \neq \pm 2\)"), (r"\(\dfrac{1}{\sqrt{x}}\)", r"\(x > 0\)")],
        [r"\(x \geq -2\)"],
        r"Onder een wortel \(\geq 0\), in een logaritme \(> 0\), een noemer \(\neq 0\). Bij \(\tfrac{1}{\sqrt{x}}\) komen beide samen.",
    ),
    mk(
        r"Hoeveel oplossingen heeft \(x^{4} - 13x^{2} + 36 = 0\)?",
        ["4", "2", "0", "1"],
        0,
        r"\(t = x^{2}\): \(t^{2} - 13t + 36 = 0\), \(t = 4\) of \(t = 9\). Dus \(x = \pm 2\) en \(x = \pm 3\).",
    ),
    volgorde(
        r"Zet de stappen om \(\dfrac{x - 1}{x + 3} > 2\) op te lossen in de goede volgorde.",
        [r"alles naar links: \(\dfrac{x - 1}{x + 3} - 2 > 0\)", r"op één noemer: \(\dfrac{-x - 7}{x + 3} > 0\)", r"nulwaarden van teller en noemer: \(-7\) en \(-3\)", r"tekentabel maken", r"besluit: \(-7 < x < -3\)"],
        "Vermenigvuldig niet met de noemer: je kent haar teken niet.",
    ),
    sleep(
        r"Na het [[kwadrateren]] van een irrationale vergelijking moet je elke oplossing [[controleren]] in de oorspronkelijke vergelijking, want er kunnen [[valse]] oplossingen bijkomen.",
        ["afronden", "ware", "ontbinden"],
        r"Uit \(a = b\) volgt \(a^{2} = b^{2}\), maar niet omgekeerd.",
    ),
    tabel(
        r"Hoeveel reële oplossingen?",
        [(r"\(e^{x} = -1\)", "0"), (r"\(\ln x = -1\)", "1"), (r"\(x^{3} = -8\)", "1"), (r"\(\sqrt{x} = -2\)", "0"), (r"\(x^{2} = 2x\)", "2")],
        r"\(e^{x} > 0\) en \(\sqrt{x} \geq 0\). \(\ln x = -1\) geeft \(x = \tfrac{1}{e}\). \(x^{2} = 2x\) geeft \(0\) en \(2\).",
        kolommen=["0", "1", "2"],
    ),
    inv(
        r"Los op: \(|2x - 4| < 6\). Typ de linkergrens van het interval.",
        ["-1", "−1"],
        r"\(-6 < 2x - 4 < 6\) geeft \(-2 < 2x < 10\), dus \(-1 < x < 5\).",
    ),
    mk(
        r"Een rechthoek heeft omtrek 20 cm. Voor welke breedtes \(x\) is de oppervlakte minstens 21 cm²?",
        [r"\(3 \leq x \leq 7\)", r"\(x \geq 3\)", r"\(x \leq 3\) of \(x \geq 7\)", r"\(0 < x < 10\)"],
        0,
        r"Lengte \(10 - x\): \(x(10 - x) \geq 21\) geeft \(x^{2} - 10x + 21 \leq 0\), dus tussen de nulwaarden \(3\) en \(7\).",
    ),
    tabel(
        r"Los grafisch op: de grafiek van \(h\) ligt boven de \(x\)-as op \(\left]-2, 1\right[\) en \(\left]4, +\infty\right[\) en heeft nulwaarden \(-2\), \(1\), \(4\). Klopt het?",
        [(r"\(h(x) < 0\) voor \(x \in \left]1, 4\right[\)", J), (r"\(h(0) > 0\)", J), (r"\(h(x) \leq 0\) voor \(x \leq -2\)", J), (r"\(h(5) < 0\)", F)],
        "Tussen de nulwaarden wisselt het teken. Links van -2 is h negatief, tussen 1 en 4 ook.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Los op: \(\left(\tfrac{1}{2}\right)^{x} > 8\).",
        [r"\(x < -3\)", r"\(x > -3\)", r"\(x > 3\)", r"\(x < 3\)"],
        0,
        r"\(\left(\tfrac{1}{2}\right)^{x} = 2^{-x} > 2^{3}\) geeft \(-x > 3\), dus \(x < -3\).",
    ),
    inv(
        r"Los op: \(\sqrt{x} + 2 = x\). Typ \(x\).",
        ["4", "x = 4", "x=4"],
        r"\(\sqrt{x} = x - 2\), kwadrateren: \(x = x^{2} - 4x + 4\), dus \(x = 1\) of \(x = 4\). Bij \(x = 1\) staat links \(3\) en rechts \(1\): vals.",
    ),
    mk(
        r"Voor welke \(x\) geldt \(x^{3} < x\)?",
        [r"\(x < -1\) of \(0 < x < 1\)", r"\(-1 < x < 1\)", r"\(0 < x < 1\)", r"\(x < 1\)"],
        0,
        r"\(x^{3} - x = x(x - 1)(x + 1) < 0\). Tekentabel met nulwaarden \(-1, 0, 1\).",
    ),
    tabel(
        r"Is \(x = 2\) een oplossing?",
        [(r"\(\sqrt{x + 7} = x + 1\)", J), (r"\(\log_{2}(x - 2) = 0\)", F), (r"\(x^{2} - 3x + 2 \leq 0\)", J), (r"\(\dfrac{x}{x - 2} = 1\)", F)],
        r"\(\sqrt{9} = 3\) klopt. \(\log_{2}0\) bestaat niet. \(4 - 6 + 2 = 0 \leq 0\). Bij \(x = 2\) is de noemer nul.",
        kolommen=["Juist", "Fout"],
    ),
]
