"""Bedrijfswetenschappen: hypothesetoetsen en correlatie — pittig (🌍 Beyond, wiskunde basis).

De nadruk ligt op de betekenis: p-waarden staan als uitkomst van een rekenapp
in de vraag of worden afgelezen.
"""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

P_GRAF = venster("toetsen-pwaarde", 0.3, 0.7, 0, 9, 0.05, 1)
S_GRAF = venster("toetsen-studie", 0, 10, 0, 100, 1, 10)


def _n(x):
    return math.exp(-((x - 0.5) / 0.05) ** 2 / 2) / (0.05 * math.sqrt(2 * math.pi))


LEERLINGEN = [(1, 40), (1.5, 47), (2, 49), (3, 51), (3.5, 58), (4, 61), (5, 63), (5.5, 70), (6, 73), (7, 52), (7.5, 79), (8, 84), (9, 88)]
AFWIJKER = (7, 52)

GRAFIEKEN = [
    dict(naam=P_GRAF, titel="Steekproevenverdeling van p̂ als H₀: p = 0,5 waar is (n = 100)",
         vlakken=[(_n, 0.58, 0.7, "#b5651d")], stippel=[("v", 0.58)],
         krommen=[(_n, "paars", "", (0.3, 0.7))], xlabel="p̂", ylabel="", ijk_x=0.05, ijk_y=2,
         xnamen={k * 0.05: f"{k * 0.05:.2f}".replace(".", ",") for k in range(6, 15)}),
    dict(naam=S_GRAF, titel="Studietijd (uur) en score op een toets (%) van 13 leerlingen",
         punten=[(x, y, "") for x, y in LEERLINGEN],
         krommen=[(lambda x: 6 * x + 35, "oranje", "", (0, 10))], xlabel="uur", ylabel="score", ijk_x=1, ijk_y=10),
]

PRENTEN = [dict(bestand=f"{g['naam']}.svg", zelf=True, wat=g["titel"], vragen="klikvragen over p-waarde en spreidingsdiagram") for g in GRAFIEKEN]


VRAGEN = [
    klik(
        "Een steekproef van 100 geeft p̂ = 0,58 (stippellijn). Je toetst rechtszijdig: H₁: p > 0,5. Klik op het gebied waarvan de oppervlakte de p-waarde is.",
        f"{P_GRAF}.svg",
        [vak_zone(P_GRAF, 0.582, 0.66, 0, 2.1)],
        "De p-waarde is de oppervlakte onder de kromme vanaf de waargenomen 0,58 in de richting van H₁: de gekleurde rechterstaart.",
    ),
    met_prent(f"{P_GRAF}.svg", mk(
        "Een rekenapp geeft voor deze rechterstaart een p-waarde van 0,055. Wat besluit je bij een significantieniveau van 10 %?",
        [
            "H₀ niet verwerpen, want 0,055 is kleiner dan 0,5",
            "H₀ verwerpen: het resultaat is significant",
            "H₀ is bewezen, want de p-waarde ligt dicht bij 0",
            "Je kan niets besluiten zonder de populatie",
        ],
        1,
        r"\(0{,}055 < 0{,}10\): zo'n extreem resultaat is te onwaarschijnlijk als H₀ waar is.",
    )),
    met_prent(f"{P_GRAF}.svg", mk(
        "Wat is hier de nulhypothese?",
        ["H₀: p̂ = 0,58", "H₀: p > 0,5", "H₀: p = 0,58", "H₀: p = 0,5"],
        3,
        "De nulhypothese gaat over de populatieproportie p en zegt 'geen verschil': p = 0,5.",
    )),
    klik(
        "Klik op de leerling die het verst afwijkt van de trendlijn.",
        f"{S_GRAF}.svg",
        [punt_zone(S_GRAF, *AFWIJKER, 30)],
        "Na 7 uur studeren verwacht de trendlijn ongeveer 77 %. Deze leerling haalde 52 %.",
    ),
    met_prent(f"{S_GRAF}.svg", mk(
        "Welke correlatiecoëfficiënt past het best bij dit spreidingsdiagram?",
        [r"\(r \approx -0{,}9\)", r"\(r \approx 0{,}1\)", r"\(r = 1\)", r"\(r \approx 0{,}9\)"],
        3,
        "De punten liggen dicht bij een stijgende rechte, maar niet precies erop.",
    )),
    met_prent(f"{S_GRAF}.svg", inv(
        "Hoeveel leerlingen studeerden meer dan 6 uur?",
        "4",
        "Rechts van 6 uur liggen de punten bij 7; 7,5; 8 en 9 uur.",
    )),
    mk(
        "Je kiest vooraf α = 0,05. Wat betekent dat?",
        [
            "De kans dat H₀ waar is, is 5 %",
            "Je verwerpt H₀ ten onrechte in hoogstens 5 % van de gevallen waarin ze waar is",
            "5 % van de mensen in de steekproef heeft een fout antwoord gegeven",
            "Het resultaat van de steekproef wijkt 5 % af van de echte waarde",
        ],
        1,
        "α is de grens die je vooraf kiest voor het risico om een juiste H₀ toch te verwerpen.",
    ),
    mk(
        "Een fabrikant beweert dat zijn batterijen gemiddeld 500 uur werken. Een consumentenorganisatie vermoedt dat het minder is. Welke alternatieve hypothese past?",
        ["H₁: μ > 500", "H₁: μ = 500", "H₁: μ ≠ 500", "H₁: μ < 500"],
        3,
        "H₁ is wat je wil aantonen: minder dan 500 uur. Dat is een linkszijdige toets.",
    ),
    mk(
        "Een machine moet zakjes van 250 g vullen. Te veel en te weinig zijn allebei een probleem. Welke alternatieve hypothese past?",
        ["H₁: μ < 250", "H₁: μ ≠ 250", "H₁: μ > 250", "H₁: x̄ ≠ 250"],
        1,
        "Een afwijking in beide richtingen telt: een tweezijdige toets over het populatiegemiddelde.",
    ),
    tabel(
        "Juist of fout over hypothesetoetsen?",
        [
            ("Een kleine p-waarde is een aanwijzing tegen H₀.", J),
            ("Bij een tweezijdige toets kijk je enkel naar de rechterstaart.", F),
            ("Met een grotere steekproef kan je makkelijker een klein verschil aantonen.", J),
            ("Een p-waarde van 0,30 betekent dat H₀ 30 % kans heeft om waar te zijn.", F),
        ],
        "Tweezijdig tel je beide staarten. Een p-waarde zegt hoe verrassend de gegevens zijn als H₀ waar is, niet hoe waarschijnlijk H₀ is.",
    ),
    keuze(
        "Een correlatiecoëfficiënt ligt altijd tussen [[*−1 en 1|0 en 1|−100 en 100]]. Bij een dalende trend is r [[*negatief|positief|nul]].",
        "Het teken volgt de richting van de trend.",
    ),
    sorteer(
        "Gaat het om een steekproefgrootheid of een populatieparameter?",
        ["Steekproef", "Populatie"],
        [
            ["p̂", "Steekproef"],
            ["p", "Populatie"],
            ["x̄", "Steekproef"],
            ["μ", "Populatie"],
            ["Het gemiddelde inkomen van alle Belgen", "Populatie"],
            ["Het aandeel ja-stemmers bij 500 bevraagden", "Steekproef"],
        ],
        "Hoedjes en strepen voor de steekproef, Griekse letters en p voor de populatie.",
    ),
    mk(
        "Tussen de prijs van een product en het aantal verkochte stuks is r = −0,85. Wat betekent dat?",
        [
            "Een hogere prijs gaat sterk samen met minder verkochte stuks",
            "85 % van de klanten koopt minder als de prijs stijgt",
            "Er is bijna geen verband, want r is kleiner dan 0",
            "Een hogere prijs veroorzaakt zeker minder verkoop",
        ],
        0,
        "Sterk (dicht bij −1) en negatief lineair verband. Over oorzaak zegt r niets.",
    ),
    mk(
        r"Welk spreidingsdiagram kan \(r \approx 0\) hebben?",
        [
            "Punten die mooi op een stijgende rechte liggen",
            "Punten zonder lineaire trend, zoals een wolk of een symmetrische parabool",
            "Punten die op een dalende rechte liggen",
            "Dat kan niet: r is nooit 0 als er punten in het diagram staan",
        ],
        1,
        "r meet enkel een lineair verband. Een parabool kan een sterk verband zijn, toch is r dan bijna 0.",
    ),
    volgorde(
        "Zet de stappen van een hypothesetoets in de goede volgorde.",
        [
            "Formuleer H₀ en H₁",
            "Kies het significantieniveau α",
            "Verzamel de steekproef en bepaal de p-waarde met ICT",
            "Vergelijk de p-waarde met α en formuleer het besluit in de context",
        ],
        "Hypothesen en α leg je vast voor je naar de gegevens kijkt.",
    ),
    koppel(
        "Koppel het begrip uit een hypothesetoets aan zijn betekenis.",
        [
            ["Nulhypothese", "De bewering die je op de proef stelt, meestal 'geen verschil'"],
            ["Alternatieve hypothese", "Wat je wil aantonen"],
            ["Significantieniveau", "De grens voor de p-waarde die je vooraf kiest"],
            ["Eenzijdige toets", "Je kijkt naar afwijkingen in één richting"],
        ],
        ["De grootte van de steekproef"],
        "H₀ is het uitgangspunt, H₁ het vermoeden, α de lat.",
    ),
    mk(
        "In de zomer is er een sterke correlatie tussen verkochte zonnecrème en verkochte ijsjes. Wat besluit je?",
        [
            "Zonnecrème doet mensen ijs kopen",
            "IJs eten doet mensen zonnecrème kopen",
            "Er is samenhang, waarschijnlijk door een derde variabele zoals het zonnige weer",
            "De correlatie is zeker toeval, want zonnecrème en ijs hebben niets met elkaar te maken",
        ],
        2,
        "Correlatie is geen causaliteit. Het weer beïnvloedt allebei.",
    ),
    mk(
        r"De trendlijn tussen studietijd x (uur) en score y (%) is \(y = 6x + 35\). Welke score voorspelt ze na 5 uur studeren?",
        [r"\(41\) %", r"\(65\) %", r"\(30\) %", r"\(70\) %"],
        1,
        r"\(6 \cdot 5 + 35\).",
    ),
    mk(
        "Mag je met diezelfde trendlijn y = 6x + 35 de score na 20 uur studeren voorspellen?",
        [
            "Ja, een trendlijn geldt overal",
            "Ja, de score is dan 155 %",
            "Nee, 20 uur ligt ver buiten de gemeten waarden en een score boven 100 % kan niet",
            "Nee, want een trendlijn mag je enkel gebruiken voor gehele aantallen uren",
        ],
        2,
        "Voorspellen buiten het gemeten gebied (extrapoleren) is riskant: het verband kan daar anders zijn.",
    ),
    sleep(
        "In een spreidingsdiagram zet je de [[onafhankelijke]] variabele op de horizontale as en de [[afhankelijke]] variabele op de verticale as. Een rechte die het verband zo goed mogelijk weergeeft, heet een [[trendlijn]].",
        ["toevallige", "asymptoot", "raaklijn"],
        "De afhankelijke variabele hangt (misschien) af van de andere.",
    ),
    mk(
        "Wat stelt de steekproevenverdeling van p̂ voor?",
        [
            "De verdeling van de antwoorden binnen één steekproef",
            "Hoe p̂ zou schommelen over heel veel steekproeven van dezelfde grootte",
            "De verdeling van de hele populatie waaruit je de steekproef trekt",
            "De kans dat de nulhypothese waar is, berekend uit één steekproef",
        ],
        1,
        "Elke steekproef geeft een andere p̂. Al die waarden samen vormen de steekproevenverdeling.",
    ),
    mk(
        "Wat gebeurt er met de spreiding van de steekproevenverdeling als de steekproefgrootte n toeneemt?",
        ["Ze wordt groter", "Ze blijft gelijk", "Ze wordt kleiner", "Ze wordt nul vanaf n = 30"],
        2,
        "Grotere steekproeven geven waarden die dichter bij de echte p liggen.",
    ),
    open_(
        "Leg uit waarom 'H₀ niet verwerpen' niet hetzelfde is als 'H₀ bewijzen'.",
        "Een grote p-waarde betekent enkel dat de gegevens niet verrassend zijn als H₀ waar is. Ze kunnen ook passen bij een kleine afwijking die je met deze steekproef niet ziet. Je hebt dus onvoldoende bewijs tegen H₀, maar geen bewijs voor H₀.",
        "Geen bewijs van schuld is nog geen bewijs van onschuld.",
    ),
    mk(
        "Een school test of een nieuwe methode het gemiddelde resultaat verhoogt. Nu is dat 62 %. Welk paar hypothesen past?",
        ["H₀: μ = 62, H₁: μ > 62", "H₀: μ > 62, H₁: μ = 62", "H₀: μ = 62, H₁: μ ≠ 62", "H₀: x̄ = 62, H₁: x̄ > 62"],
        0,
        "H₀ zegt 'geen verbetering', H₁ is het vermoeden. Hypothesen gaan over μ, niet over x̄.",
    ),
    mk(
        "Een toets geeft een p-waarde van 0,003. Wat besluit je bij α = 0,01?",
        [
            "H₀ verwerpen: het resultaat is significant",
            "H₀ niet verwerpen",
            "H₀ heeft 0,3 % kans om waar te zijn",
            "Je moet de toets herhalen met een grotere steekproef om zeker te zijn",
        ],
        0,
        r"\(0{,}003 < 0{,}01\).",
    ),
    tabel(
        "Juist of fout over correlatie?",
        [
            ("r = 1 betekent dat alle punten op een stijgende rechte liggen.", J),
            ("Een correlatie van 0,9 bewijst een oorzakelijk verband.", F),
            ("r verandert niet als je x en y van rol wisselt.", J),
            ("r = −0,8 wijst op een zwakker lineair verband dan r = 0,5.", F),
        ],
        "De sterkte zit in de afstand tot 0, los van het teken: |−0,8| > 0,5.",
    ),
    mk(
        "Een onderzoeker voert 20 toetsen uit met α = 0,05, terwijl H₀ telkens waar is. Hoeveel keer verwacht je toch een significant resultaat?",
        ["Nooit", "Ongeveer 1 keer", "Ongeveer 5 keer", "Ongeveer 10 keer"],
        1,
        r"Telkens 5 % kans op een onterechte verwerping: \(20 \cdot 0{,}05 = 1\).",
    ),
    casus(
        "Een webwinkel beweert dat 90 % van de pakjes op tijd komt. Een klantengroep volgt 200 pakjes: 170 komen op tijd. Ze vermoeden dat het minder is dan 90 %.",
        [
            mk(
                "Welk paar hypothesen past?",
                ["H₀: p = 0,9, H₁: p > 0,9", "H₀: p = 0,85, H₁: p < 0,85", "H₀: p = 0,9, H₁: p < 0,9", "H₀: p = 0,9, H₁: p ≠ 0,9"],
                2,
                "De bewering is p = 0,9. Het vermoeden is 'minder'.",
            ),
            mk(
                "Wat is de steekproefproportie p̂?",
                [r"\(0{,}9\)", r"\(0{,}85\)", r"\(0{,}17\)", r"\(0{,}15\)"],
                1,
                r"\(\frac{170}{200}\).",
            ),
            mk(
                "Een rekenapp geeft een p-waarde van 0,009. Wat besluit de klantengroep bij α = 0,05?",
                [
                    "De webwinkel heeft gelijk: 90 % komt op tijd",
                    "H₀ verwerpen: er is een significante aanwijzing dat minder dan 90 % op tijd komt",
                    "Er komt precies 85 % van alle pakjes op tijd, zoals in de steekproef",
                    "Er is te weinig informatie, want 200 pakjes is maar een klein deel van alle pakjes",
                ],
                1,
                r"\(0{,}009 < 0{,}05\). Het besluit gaat over de populatie, met een klein risico op vergissing.",
            ),
        ],
    ),
]
