"""Vergelijkingen grafisch oplossen — pittig (🌍 Beyond, wiskunde basis)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

FG_GRAF = venster("vergelijkingen-fg", -3, 6, -5, 8, 1, 1)
EX_GRAF = venster("vergelijkingen-medicijn", 0, 12, 0, 90, 1, 10)
SIN_GRAF = venster("vergelijkingen-sinus", 0, 2 * math.pi, -2, 4, math.pi / 6, 1)


def _f(x):
    return x * x - 2 * x - 3


def _g(x):
    return x + 1


def _c(t):
    return 80 * 0.8 ** t


def _s(x):
    return 2 * math.sin(x) + 1


T_40 = math.log(0.5) / math.log(0.8)  # ongeveer 3,1

_PI = {1: "π/6", 2: "π/3", 3: "π/2", 4: "2π/3", 5: "5π/6", 6: "π", 7: "7π/6", 8: "4π/3", 9: "3π/2", 10: "5π/3", 11: "11π/6", 12: "2π"}

GRAFIEKEN = [
    dict(naam=FG_GRAF, titel="De grafieken van f en g",
         krommen=[(_f, "groen", "f", (-2.6, 5.2)), (_g, "blauw", "g", (-3, 6))],
         labelplek={"f": (-2.2, _f(-2.2)), "g": (5.4, _g(5.4))}),
    dict(naam=EX_GRAF, titel="Medicijn in het bloed: C (mg), t uur na inname",
         krommen=[(_c, "paars", "", (0, 12))], stippel=[("h", 20)], xlabel="t", ylabel="C", ijk_x=1, ijk_y=10),
    dict(naam=SIN_GRAF, titel="De grafiek van f(x) = 2 sin x + 1",
         krommen=[(_s, "oranje", "", (0, 2 * math.pi))], ijk_x=math.pi / 6, ijk_y=1,
         xnamen={k * (math.pi / 6): v for k, v in _PI.items()}),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over grafisch oplossen") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        r"Klik op een punt waarvan de \(x\)-coördinaat een oplossing is van \(f(x) = g(x)\).",
        f"{FG_GRAF}.svg",
        [punt_zone(FG_GRAF, -1, 0), punt_zone(FG_GRAF, 4, 5)],
        r"De oplossingen van \(f(x) = g(x)\) zijn de \(x\)-coördinaten van de snijpunten van beide grafieken: \((-1, 0)\) en \((4, 5)\).",
    ),
    klik(
        r"Klik op het nulpunt van f dat geen oplossing geeft van \(f(x) = g(x)\).",
        f"{FG_GRAF}.svg",
        [punt_zone(FG_GRAF, 3, 0)],
        r"f heeft nulwaarden \(-1\) en \(3\). In \(x = 3\) is \(g(3) = 4 \neq 0\): daar snijden de grafieken elkaar niet.",
    ),
    met_prent(f"{FG_GRAF}.svg", mk(
        r"Wat is de oplossingenverzameling van \(f(x) = g(x)\)?",
        [r"\(V = \{(-1, 0), (4, 5)\}\)", r"\(V = \{-1, 4\}\)", r"\(V = \{0, 5\}\)", r"\(V = \{-1, 3\}\)"],
        1,
        r"In de oplossingenverzameling staan enkel de \(x\)-waarden waarvoor beide functiewaarden gelijk zijn. De punten zelf zijn de snijpunten.",
    )),
    met_prent(f"{FG_GRAF}.svg", mk(
        r"Hoeveel oplossingen heeft \(f(x) = -4\)?",
        [r"Twee", r"Eén", r"Geen", r"Drie"],
        1,
        r"De rechte \(y = -4\) raakt de parabool enkel in de top \((1, -4)\).",
    )),
    met_prent(f"{FG_GRAF}.svg", tabel(
        "Hoeveel oplossingen heeft elke vergelijking?",
        [
            (r"\(f(x) = -5\)", "Geen"),
            (r"\(f(x) = 5\)", "Twee"),
            (r"\(g(x) = 7\)", "Eén"),
            (r"\(f(x) = 0\)", "Twee"),
        ],
        r"Teken in gedachten de horizontale rechte \(y = k\) en tel de snijpunten met de grafiek. Een niet-horizontale rechte zoals g wordt door elke horizontale rechte één keer gesneden.",
        kolommen=["Geen", "Eén", "Twee"],
    )),
    klik(
        r"Klik op het punt dat de oplossing van \(80 \cdot 0{,}8^t - 40 = 0\) aangeeft.",
        f"{EX_GRAF}.svg",
        [punt_zone(EX_GRAF, T_40, 40, 32)],
        r"\(80 \cdot 0{,}8^t - 40 = 0\) is hetzelfde als \(80 \cdot 0{,}8^t = 40\): het punt van de grafiek op hoogte \(C = 40\), bij \(t \approx 3{,}1\).",
    ),
    met_prent(f"{EX_GRAF}.svg", mk(
        r"Het rekentoestel geeft als oplossing \(t \approx 6{,}2\). Wat betekent dat in deze context?",
        [
            "Na ongeveer 6,2 uur is er van het medicijn nog maar 20 % over in het bloed.",
            "Ongeveer 6,2 uur na de inname zit er nog 20 mg van het medicijn in het bloed.",
            "Elk uur verdwijnt er ongeveer 6,2 mg van het medicijn uit het bloed van de patiënt.",
            "Ongeveer 20 uur na de inname zit er nog 6,2 mg van het medicijn in het bloed.",
        ],
        1,
        r"\(t\) is de tijd in uur en \(C\) de hoeveelheid in mg. Het snijpunt zegt: op \(t \approx 6{,}2\) is \(C = 20\). In het begin was er \(80\) mg, dus \(20\) mg is \(25\) %.",
    )),
    inv(
        r"Bereken met \(C(t) = 80 \cdot 0{,}8^t\) hoeveel mg er na 5 uur in het bloed zit. Rond af op een geheel getal.",
        "26",
        r"\(80 \cdot 0{,}8^5 = 80 \cdot 0{,}32768 \approx 26{,}2\), dus ongeveer \(26\) mg.",
    ),
    klik(
        r"Klik op een punt waarvan de \(x\)-coördinaat een oplossing is van \(2 \sin x + 1 = 0\).",
        f"{SIN_GRAF}.svg",
        [punt_zone(SIN_GRAF, 7 * math.pi / 6, 0), punt_zone(SIN_GRAF, 11 * math.pi / 6, 0)],
        r"De oplossingen zijn de nulwaarden van f: \(\frac{7\pi}{6}\) en \(\frac{11\pi}{6}\).",
    ),
    met_prent(f"{SIN_GRAF}.svg", mk(
        r"Wat is de oplossingenverzameling van \(2 \sin x + 1 = 2\) op \([0, 2\pi]\)?",
        [r"\(\left\{\frac{\pi}{6}, \frac{11\pi}{6}\right\}\)", r"\(\left\{\frac{\pi}{3}, \frac{2\pi}{3}\right\}\)", r"\(\left\{\frac{\pi}{6}, \frac{5\pi}{6}\right\}\)", r"\(\left\{\frac{\pi}{2}\right\}\)"],
        2,
        r"De rechte \(y = 2\) snijdt de grafiek tweemaal op dit interval, symmetrisch rond de top in \(\frac{\pi}{2}\).",
    )),
    met_prent(f"{SIN_GRAF}.svg", mk(
        r"Voor welke waarden van k heeft \(2 \sin x + 1 = k\) precies één oplossing op \([0, 2\pi]\)?",
        [r"\(k = 1\)", r"\(k = 0\)", r"\(k = 2\)", r"\(k = 3\) of \(k = -1\)"],
        3,
        r"Enkel de horizontale rechten door de top \(\left(\frac{\pi}{2}, 3\right)\) en door het dal \(\left(\frac{3\pi}{2}, -1\right)\) raken de grafiek in één punt. De rechte \(y = 1\) snijdt de grafiek in \(0\), \(\pi\) en \(2\pi\).",
    )),
    tabel(
        "Juist of fout over vergelijkingen en grafieken?",
        [
            (r"De oplossingen van \(f(x) = 0\) zijn de nulwaarden van f.", J),
            (r"Als de grafieken van f en g elkaar nergens snijden, kan \(f(x) = g(x)\) toch een oplossing hebben.", F),
            (r"\(f(x) = g(x)\) oplossen komt neer op de nulwaarden van \(f - g\) zoeken.", J),
            (r"Een veeltermvergelijking van de derde graad heeft altijd drie oplossingen.", F),
        ],
        r"Een oplossing van \(f(x) = g(x)\) is een \(x\) waar beide grafieken even hoog zijn, dus een snijpunt. \(x^3 + 1 = 0\) heeft maar één reële oplossing.",
    ),
    mk(
        r"Een vergelijking \(b \cdot a^x + c = 0\) heeft \(b > 0\). Wanneer heeft ze een oplossing?",
        [r"Als \(c > 0\)", r"Als \(c = 0\)", r"Als \(c < 0\)", r"Altijd"],
        2,
        r"\(b \cdot a^x = -c\). Links staat altijd een positief getal, dus \(-c\) moet positief zijn.",
    ),
    mk(
        r"Je wil \(x^3 - 2x = x + 1\) grafisch oplossen. Wat doe je met je rekentoestel?",
        [
            r"Je voert \(y_1 = x^3 - 2x\) in en zoekt de nulwaarden",
            r"Je voert \(y_1 = x^3 - 2x\) en \(y_2 = x + 1\) in en zoekt de snijpunten",
            r"Je voert \(y_1 = x^3 - 2x\) en \(y_2 = x + 1\) in en zoekt de toppen",
            r"Je voert \(y_1 = x^3 - 3x - 1\) in en zoekt het minimum",
        ],
        1,
        r"Linkerlid en rechterlid worden twee functies. Waar ze even groot zijn, snijden de grafieken. Ook \(y_1 = x^3 - 3x - 1\) zou kunnen, maar dan zoek je de nulwaarden, niet het minimum.",
    ),
    keuze(
        r"De vergelijking \(4 \sin x + 7 = 0\) heeft [[*geen|twee|oneindig veel]] oplossingen, want \(4 \sin x + 7\) ligt altijd tussen [[*3 en 11|−4 en 4|0 en 7]].",
        r"\(\sin x\) ligt tussen \(-1\) en \(1\). Maal 4 en plus 7 geeft waarden van 3 tot 11: nooit 0.",
    ),
    sorteer(
        "Heeft de vergelijking een reële oplossing of niet?",
        ["Heeft een oplossing", "Heeft geen oplossing"],
        [
            [r"\(3 \sin x - 2 = 0\)", "Heeft een oplossing"],
            [r"\(\sin 2x + 3 = 0\)", "Heeft geen oplossing"],
            [r"\(x^3 + 1 = 0\)", "Heeft een oplossing"],
            [r"\(x^2 + 4 = 0\)", "Heeft geen oplossing"],
            [r"\(-2 \sin(x - 1) = 1\)", "Heeft een oplossing"],
            [r"\(x^4 + x^2 + 1 = 0\)", "Heeft geen oplossing"],
        ],
        r"Een sinusvergelijking heeft een oplossing als de rechte binnen het bereik van de functie valt. Een even macht plus een positief getal is nooit 0, een derdemacht neemt elke waarde aan.",
    ),
    mk(
        r"Een bal wordt opgegooid: \(h(t) = -5t^2 + 20t + 1\) (m, t in s). Wanneer is de bal op 16 m hoogte?",
        [r"Na \(1\) s en na \(3\) s", r"Enkel na \(2\) s", r"Enkel na \(1\) s", r"Na \(3\) s en na \(16\) s"],
        0,
        r"Snij de grafiek met \(y = 16\): \(-5t^2 + 20t - 15 = 0\) geeft \(t = 1\) en \(t = 3\). Eén keer op weg naar boven, één keer op weg naar beneden.",
    ),
    inv(
        r"Een kolonie bacteriën groeit volgens \(N(t) = 500 \cdot 1{,}2^t\) (t in uur). Los grafisch op: na hoeveel uur zijn er 3000 bacteriën? Rond af op één decimaal.",
        "9,8",
        r"Snij \(y_1 = 500 \cdot 1{,}2^x\) met \(y_2 = 3000\): \(x \approx 9{,}83\), dus na ongeveer \(9{,}8\) uur.",
    ),
    mk(
        r"Hoe noteer je dat \(x^2 + 1 = 0\) geen reële oplossing heeft?",
        [r"\(V = \{0\}\)", r"\(V = \mathbb{R}\)", r"\(V = \{\varnothing\}\)", r"\(V = \varnothing\)"],
        3,
        r"Geen oplossing is de lege verzameling, \(\varnothing\) of \(\{\,\}\). \(\{\varnothing\}\) is een verzameling met één element in.",
    ),
    volgorde(
        "Zet de stappen om een vergelijking grafisch op te lossen in de goede volgorde.",
        [
            r"Schrijf de vergelijking als \(f(x) = g(x)\)",
            r"Voer f en g in als \(y_1\) en \(y_2\)",
            "Kies een venster waarin je alle snijpunten ziet",
            "Laat het toestel de snijpunten berekenen",
            "Noteer de oplossingenverzameling en formuleer het antwoord in de context",
        ],
        "Eerst de vergelijking klaarzetten, dan invoeren, venster kiezen, snijpunten zoeken en tot slot het antwoord in woorden.",
    ),
    koppel(
        "Koppel de vergelijking aan wat je op de grafiek zoekt.",
        [
            [r"\(f(x) = 0\)", "De nulwaarden van f"],
            [r"\(f(x) = g(x)\)", "De x-coördinaten van de snijpunten van de grafieken van f en g"],
            [r"\(f(x) = 3\)", r"De x-coördinaten van de snijpunten van de grafiek van f met \(y = 3\)"],
            [r"\(f(x) = f(2)\)", r"De x-waarden waar f even hoog is als in \(x = 2\)"],
        ],
        ["De y-coördinaat van de top van f"],
        "Een vergelijking oplossen geeft altijd x-waarden. Hoe hoog de grafiek ergens is, is een functiewaarde.",
    ),
    sleep(
        r"Omdat de sinus [[periodiek]] is, heeft \(3 \sin 2x = 1\) op \(\mathbb{R}\) [[oneindig veel]] oplossingen. Daarom vraagt men ze meestal op een begrensd [[interval]].",
        ["symmetrisch", "twee", "domein"],
        r"Na elke periode \(\pi\) herhaalt de grafiek zich, en daarmee ook de snijpunten.",
    ),
    mk(
        r"Wat is de oplossingenverzameling van \(x^3 - 4x = 0\)?",
        [r"\(\{0, 2\}\)", r"\(\{-2, 0, 2\}\)", r"\(\{-2, 2\}\)", r"\(\{0, 4\}\)"],
        1,
        r"\(x^3 - 4x = x(x - 2)(x + 2)\). De grafiek snijdt de \(x\)-as drie keer.",
    ),
    tabel(
        "Juist of fout over grafisch oplossen met ICT?",
        [
            ("Een slecht gekozen venster kan snijpunten verbergen.", J),
            ("Als het toestel één snijpunt toont, is er zeker maar één oplossing.", F),
            ("De oplossingen die het toestel geeft, zijn altijd exact.", F),
            ("In een context ga je na of een oplossing zinvol is, bijvoorbeeld geen negatieve tijd.", J),
        ],
        "Het toestel toont enkel wat in beeld is en rekent met benaderingen. Kijk daarom ook buiten het venster en controleer de context.",
    ),
    mk(
        r"De temperatuur op een dag is \(T(u) = 4 \sin\left(\frac{\pi}{12}(u - 9)\right) + 15\) (°C, u uur na middernacht). Wanneer is het precies 15 °C, tussen 0 en 24 uur?",
        [r"Om 15 uur", r"Om 9 uur en om 21 uur", r"Enkel om 9 uur", r"Om 3 uur en om 15 uur"],
        1,
        r"\(15\) is de evenwichtslijn. De sinus is \(0\) als \(\frac{\pi}{12}(u - 9)\) gelijk is aan \(0\) of \(\pi\): \(u = 9\) of \(u = 21\).",
    ),
    open_(
        r"Leg uit waarom je bij \(f(x) = g(x)\) enkel de x-coördinaten van de snijpunten noteert.",
        r"De onbekende in de vergelijking is \(x\). Een oplossing is een getal \(x\) waarvoor \(f(x)\) en \(g(x)\) gelijk zijn. In het snijpunt is dat zo; de \(y\)-coördinaat is die gemeenschappelijke functiewaarde, maar geen oplossing.",
        "Een vergelijking in x heeft x-waarden als oplossing.",
    ),
    mk(
        r"In hoeveel punten snijdt de grafiek van \(y = 2^x\) de rechte \(y = 2x\)?",
        [r"Eén", r"Geen", r"Drie", r"Twee"],
        3,
        r"In \(x = 1\) (\(2 = 2\)) en in \(x = 2\) (\(4 = 4\)). Daartussen ligt de rechte boven de exponentiële grafiek, daarbuiten eronder.",
    ),
    casus(
        r"Een kop thee koelt af volgens \(T(t) = 70 \cdot 0{,}9^t + 20\) (°C, t in minuten).",
        [
            mk(
                "Welke vergelijking los je op om te weten wanneer de thee 50 °C is?",
                [r"\(70 \cdot 0{,}9^t = 50\)", r"\(70 \cdot 0{,}9^t + 20 = 50\)", r"\(70 \cdot 0{,}9^{50} + 20 = t\)", r"\(0{,}9^t + 20 = 50\)"],
                1,
                r"De temperatuur \(T(t)\) moet \(50\) zijn. Herleid: \(70 \cdot 0{,}9^t - 30 = 0\).",
            ),
            mk(
                r"Het rekentoestel geeft \(t \approx 8{,}0\). Wat is het antwoord in de context?",
                [
                    "Na ongeveer 50 minuten is de thee 8 °C.",
                    "De thee koelt elke minuut ongeveer 8 °C af.",
                    "Na ongeveer 8 minuten is de thee 50 °C.",
                    "Na ongeveer 8 minuten is de thee 20 °C.",
                ],
                2,
                "t is de tijd in minuten, T de temperatuur. Op t ≈ 8 is T = 50.",
            ),
            mk(
                r"Waarom heeft \(70 \cdot 0{,}9^t + 20 = 15\) geen oplossing?",
                ["Omdat 0,9 kleiner is dan 1", "Omdat 15 kleiner is dan 70", "Omdat de grafiek de y-as niet snijdt", "Omdat de thee nooit onder 20 °C zakt"],
                3,
                r"\(70 \cdot 0{,}9^t\) is altijd positief, dus \(T(t) > 20\). De thee nadert de kamertemperatuur, maar zakt er nooit onder.",
            ),
        ],
    ),
]
