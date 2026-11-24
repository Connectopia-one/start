r"""p-waarde, significantieniveau en fouten bij toetsen — pittig
(🌍 Beyond doorstroom, statistiek). Eigen vragen en een eigen prent,
zoals op het digitale examen."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Steekproevenverdeling onder H0 met drie gebieden ----------------------------------------
PW = Prent("pwaarde-gebieden", "Steekproevenverdeling van het gemiddelde onder H₀: μ = 50", "een klokcurve rond 50 met stippellijnen bij 46,6 en 53,4; links van 46,6 staat A, tussen de lijnen B, rechts van 53,4 C; de gevonden steekproef heeft gemiddelde 53,4")
L, R, B, H = 100, 900, 520, 360


def X(x):
    return L + (R - L) * (x - 42) / 16


def Yc(x):
    z = (x - 50) / 2
    return B - H * math.exp(-z * z / 2)


d = " ".join(f"{'M' if i == 0 else 'L'}{X(42 + i * 0.1):.1f},{Yc(42 + i * 0.1):.1f}" for i in range(161))
PW.pad(d + f" L{X(58):.1f},{B} L{X(42):.1f},{B} Z", "#dfe9d5", "none", 0)
PW.pad(d, "none", DONKER, 3)
PW.lijn(L - 10, B, R + 10, B, DONKER, 3)
for g in [46.6, 53.4]:
    PW.lijn(X(g), B, X(g), Yc(g) - 40, DONKER, 2, True)
for g in [44, 46, 48, 50, 52, 54, 56]:
    PW.lijn(X(g), B, X(g), B + 8, DONKER, 2)
    PW.tekst(X(g), B + 32, str(g), 18)
PW.tekst(X(53.4), Yc(53.4) - 52, "gevonden: 53,4", 18, "start")
PW.tekst((L + R) / 2, 600, "steekproefgemiddelde", 18)
PW.letter(X(44.6), B - 60, "A")
PW.letter(X(50), B - 60, "B")
PW.letter(X(55.4), B - 60, "C")
ZA = Prent.zone(L - 10, 150, X(46.6) - L + 10, B - 140)
ZB = Prent.zone(X(46.6), 150, X(53.4) - X(46.6), B - 140)
ZC = Prent.zone(X(53.4), 150, R + 10 - X(53.4), B - 140)

VRAGEN = [
    klik("De toets is rechtszijdig (H₁: μ > 50). Klik op het gebied waarvan de oppervlakte de p-waarde is.", PW.bestand, [ZC],
         "Minstens zo extreem in de richting van H₁: alles rechts van 53,4."),
    klik("Bij een tweezijdige toets (H₁: μ ≠ 50) hoort ook een tweede staart bij de p-waarde. Klik op die andere staart.", PW.bestand, [ZA],
         "Even ver van 50 aan de andere kant: links van 46,6."),
    klik("Klik op het gebied met resultaten die minder extreem zijn dan de gevonden steekproef.", PW.bestand, [ZB],
         "Dichter bij 50 dan 53,4."),
    met_prent(PW.bestand, keuze("De oppervlakte van C is 0,045. Bij een rechtszijdige toets met α = 0,05 [[*verwerp je H₀|verwerp je H₀ niet]].",
              "0,045 ≤ 0,05.")),
    met_prent(PW.bestand, inv("Bij een tweezijdige toets is de p-waarde dan A + C. Hoeveel is dat? Schrijf als decimaal getal.", ["0,09", "0.09"],
              "0,045 + 0,045 = 0,09.")),
    met_prent(PW.bestand, keuze("Met die tweezijdige p-waarde van 0,09 en α = 0,05 [[*verwerp je H₀ niet|verwerp je H₀]].",
              "0,09 > 0,05: te weinig bewijs.")),
    tabel("Verwerp je H₀? Telkens α = 0,05.", [
        ("p-waarde 0,008", J),
        ("p-waarde 0,21", F),
        ("p-waarde 0,05", J),
        ("p-waarde 0,051", F),
    ], "Verwerpen als de p-waarde kleiner is dan of gelijk aan α."),
    tabel("Verwerp je H₀ bij α = 0,01?", [
        ("p-waarde 0,004", J),
        ("p-waarde 0,03", F),
        ("p-waarde 0,011", F),
    ], "Een strenger significantieniveau vraagt een kleinere p-waarde."),
    casus(
        "Een bakkerij beweert dat haar broden gemiddeld 800 gram wegen. Een controleur vermoedt dat ze lichter zijn. "
        "Hij weegt 40 broden en vindt een gemiddelde van 792 gram. Een rekenapp geeft een p-waarde van 0,018. Hij gebruikt α = 0,05.",
        [
            keuze("H₁ is μ [[*<|>|≠]] 800.", "Lichter: kleiner dan."),
            keuze("Omdat 0,018 [[*kleiner|groter]] is dan 0,05, verwerpt hij H₀.", "p ≤ α."),
            mk("Welk besluit is correct geformuleerd?",
               ["op niveau 5 procent is er voldoende bewijs dat de broden lichter zijn",
                "het is bewezen dat elk brood minder dan 800 gram weegt",
                "er is 1,8 procent kans dat de bakkerij de waarheid spreekt",
                "de broden wegen gemiddeld precies 792 gram"], 0,
               "Noem het niveau en spreek over bewijs, niet over zekerheid."),
            mk("Stel dat de broden in werkelijkheid toch gemiddeld 800 gram wegen. Welke fout maakte de controleur dan?",
               ["een type I-fout", "een type II-fout", "geen fout", "een rekenfout"], 0,
               "Hij verwierp een H₀ die waar was."),
            keuze("Had hij α = 0,01 gekozen, dan zou hij H₀ [[*niet verwerpen|ook verwerpen]].",
                  "0,018 > 0,01."),
        ],
    ),
    koppel("Koppel elke situatie aan het soort fout.", [
        ["H₀ is waar en je verwerpt ze", "type I-fout"],
        ["H₀ is fout en je verwerpt ze niet", "type II-fout"],
        ["H₀ is fout en je verwerpt ze", "juist besluit"],
    ], ["kans 1 − α"], "Een fout ontstaat als je besluit niet past bij de werkelijkheid."),
    sorteer("Wat gebeurt er met de kansen als je α van 0,05 naar 0,01 verlaagt?", ["wordt kleiner", "wordt groter"], [
        ["kans op een type I-fout", "wordt kleiner"],
        ["kans op een type II-fout", "wordt groter"],
        ["de p-waarde die nodig is om H₀ te verwerpen", "wordt kleiner"],
        ["het aantal keer dat je H₀ niet verwerpt", "wordt groter"],
    ], "Strenger zijn: minder vals alarm, maar vaker een effect missen."),
    mk("Een alarm in een museum: H₀ is 'er is geen inbreker'. Het alarm gaat af als een kat door de zaal loopt. Welke fout is dat?",
       ["een type I-fout", "een type II-fout", "geen fout", "dat hangt af van α"], 0,
       "H₀ was waar, toch werd ze verworpen: vals alarm."),
    inv("Een team voert 40 toetsen uit op dingen die in werkelijkheid geen effect hebben, telkens met α = 0,05. Hoeveel significante resultaten verwacht je door toeval?", ["2", "twee"],
        "40 · 0,05 = 2."),
    keuze("Een p-waarde ligt altijd tussen [[*0 en 1|0 en 100|−1 en 1]].",
          "Ze is een kans."),
    tabel("Klopt deze uitspraak over de p-waarde?", [
        ("hoe kleiner, hoe sterker het bewijs tegen H₀", J),
        ("ze is de kans dat H₀ waar is", F),
        ("je berekent ze ervan uitgaand dat H₀ waar is", J),
        ("een grote p-waarde bewijst dat H₀ waar is", F),
    ], "De p-waarde is een kans op data, gegeven H₀; niet een kans op H₀."),
    volgorde("Zet de stappen na het opstellen van de hypothesen in de juiste volgorde.", [
        "α kiezen",
        "de steekproef nemen en meten",
        "de p-waarde berekenen met ICT",
        "p-waarde en α vergelijken en besluiten",
    ], "α kies je vooraf, voor je de data ziet."),
    sleep("Je kiest α [[vooraf]]. Is de p-waarde kleiner dan of gelijk aan α, dan is het resultaat [[significant]].",
          ["achteraf", "bewezen"], "Zo kan je α niet aanpassen aan wat je wil vinden."),
    mk("Twee onderzoeken vinden hetzelfde verschil met gemiddelden. Onderzoek A heeft n = 40, onderzoek B n = 4000. Welk heeft de kleinste p-waarde?",
       ["B", "A", "ze zijn gelijk", "dat kan je niet zeggen"], 0,
       "Een grotere steekproef geeft een kleinere spreiding, dus is hetzelfde verschil extremer."),
    keuze("De kans op een type I-fout is gelijk aan [[*α|de p-waarde|1 − α]].",
          "α is de kans om een ware H₀ te verwerpen."),
    inv("Iemand zegt: 'Bij α = 0,05 verwerp ik gemiddeld één op de hoeveel keer een ware H₀?' Geef het getal.", ["20", "twintig"],
        "0,05 = 1/20."),
    met_prent(PW.bestand, keuze("Hoe verder de gevonden waarde van 50 ligt, hoe [[*kleiner|groter]] gebied C en dus de p-waarde.",
              "Een extremer resultaat laat minder oppervlakte over in de staart.")),
    tabel("Welk soort fout kan je hier nog maken?", [
        ("je hebt H₀ verworpen", "type I-fout"),
        ("je hebt H₀ niet verworpen", "type II-fout"),
        ("je verwerpt een H₀ die eigenlijk fout is", "geen fout"),
    ], "Na verwerpen kan je enkel nog een type I-fout gemaakt hebben, en omgekeerd.",
       kolommen=["type I-fout", "type II-fout", "geen fout"]),
    mk("Hoe verklein je de kans op een type I-fout en een type II-fout tegelijk?",
       ["een grotere steekproef nemen",
        "α kleiner kiezen dan 0,01",
        "van een tweezijdige naar een eenzijdige toets overstappen",
        "de p-waarde afronden op één decimaal"], 0,
       "Meer gegevens maken de steekproevenverdeling smaller."),
    keuze("Een uitslag met p = 0,0001 bij een enorm grote steekproef kan een [[*heel klein|heel groot]] verschil zijn dat in de praktijk weinig betekent.",
          "Significant zegt niets over hoe groot het effect is."),
    inv("Bij α = 0,05: wat is de kans om een ware H₀ niet te verwerpen? Schrijf als decimaal getal.", ["0,95", "0.95"],
        "1 − 0,05 = 0,95."),
    open_("Een onderzoeker vindt p = 0,32 en schrijft: 'Er is dus geen verschil tussen beide groepen.' Verbeter zijn besluit en leg uit.",
          "Hij mag enkel zeggen dat er te weinig bewijs is voor een verschil. H₀ niet verwerpen bewijst H₀ niet: het verschil kan er zijn, maar de steekproef was misschien te klein om het aan te tonen."),
]
