r"""De normale verdeling — pittig (🌍 Beyond doorstroom, statistiek).
Eigen vragen en een eigen klokcurve, zoals op het digitale examen."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER

# Klokcurve N(60; 8) met gebieden A tot H -----------------------------------------------
NC = Prent("klokcurve-60-8", "Testscores: X ~ N(60; 8)", "een klokcurve met gemiddelde 60 en standaardafwijking 8; stippellijnen bij 36, 44, 52, 60, 68, 76 en 84; acht gebieden met de letters A tot H van links naar rechts")
L, R, B, H = 100, 900, 540, 380
XMIN, XMAX = 28, 92


def X(x):
    return L + (R - L) * (x - XMIN) / (XMAX - XMIN)


def Yc(x):
    z = (x - 60) / 8
    return B - H * math.exp(-z * z / 2)


pts = " ".join(f"L{X(XMIN + i * 0.25):.1f},{Yc(XMIN + i * 0.25):.1f}" for i in range(int((XMAX - XMIN) / 0.25) + 1))
NC.pad(f"M{X(XMIN):.1f},{B} " + pts + f" L{X(XMAX):.1f},{B} Z", "#dfe9d5", DONKER, 3)
NC.lijn(L - 20, B, R + 20, B, DONKER, 3)
GRENS = [36, 44, 52, 60, 68, 76, 84]
for g in GRENS:
    NC.lijn(X(g), B, X(g), Yc(g) if g != 60 else B - H - 10, DONKER, 2, True)
    NC.tekst(X(g), B + 30, str(g), 20)
NC.tekst((L + R) / 2, 610, "score", 18)
RAND = [XMIN] + GRENS + [XMAX]
LETTERS = "ABCDEFGH"
for i, c in enumerate(LETTERS):
    a, b = RAND[i], RAND[i + 1]
    m = (a + b) / 2
    if i in (0, 7):
        NC.letter(X(m), B - 70, c)
    else:
        NC.letter(X(m), B - 40, c)


def gebied(c):
    i = LETTERS.index(c)
    a, b = X(RAND[i]), X(RAND[i + 1])
    return [Prent.zone(a, 120, b - a, B - 110)]


VRAGEN = [
    klik("Klik op het gebied van de scores met een z-waarde tussen −2 en −1.", NC.bestand, gebied("C"),
         "Tussen 60 − 16 = 44 en 60 − 8 = 52."),
    klik("Klik op het gebied van de scores tussen één en twee standaardafwijkingen boven het gemiddelde.", NC.bestand, gebied("F"),
         "Tussen 68 en 76."),
    klik("Een leerling haalt 79. Klik op het gebied waarin die score ligt.", NC.bestand, gebied("G"),
         "79 ligt tussen 76 en 84, dus z tussen 2 en 3."),
    klik("Klik op het gebied waar volgens de vuistregel ongeveer 13,5 procent van de scores ligt, links van het gemiddelde.", NC.bestand, gebied("C"),
         "95 − 68 = 27 procent, verdeeld over twee kanten: 13,5 procent tussen −2σ en −σ."),
    met_prent(NC.bestand, keuze("Samen bevatten de gebieden D en E ongeveer [[*68|95|50]] procent van de scores.",
              "Dat is van μ − σ tot μ + σ.")),
    met_prent(NC.bestand, inv("Hoeveel procent van de scores ligt ongeveer rechts van 60?", ["50", "50%", "50 procent"],
              "De curve is symmetrisch rond het gemiddelde.")),
    met_prent(NC.bestand, inv("Welke z-waarde hoort bij een score van 48? Schrijf als decimaal getal.", ["-1,5", "-1.5"],
              r"\((48 - 60) / 8 = -1{,}5\).")),
    met_prent(NC.bestand, keuze("Ongeveer [[*2,5|5|16]] procent van de scores ligt boven 76.",
              "Buiten ±2σ ligt 5 procent, de helft daarvan rechts.")),
    casus(
        "De wachttijd aan een loket is bij benadering normaal verdeeld met gemiddelde 12 minuten en standaardafwijking 3 minuten.",
        [
            keuze("Dat noteer je als X ~ N([[*12|3]]; [[*3|12]]).", "Eerst μ, dan σ."),
            inv("Welke z-waarde hoort bij een wachttijd van 18 minuten?", ["2"],
                "(18 − 12) / 3 = 2."),
            mk("Tussen welke wachttijden ligt ongeveer 95 procent van de klanten?",
               ["6 en 18 minuten", "9 en 15 minuten", "3 en 21 minuten", "10 en 14 minuten"], 0,
               "μ ± 2σ = 12 ± 6."),
            inv("Hoeveel procent van de klanten wacht ongeveer langer dan 15 minuten?", ["16", "16%", "16 procent"],
                "Boven μ + σ ligt (100 − 68) / 2 = 16 procent."),
            tabel("Klopt dit voor deze wachttijden?", [
                ("P(X < 12) = 0,5", J),
                ("P(X = 12) is de grootste kans van allemaal", F),
                ("P(X > 15) = P(X < 9)", J),
            ], "Eén exacte waarde heeft kans 0; de curve is symmetrisch rond 12."),
        ],
    ),
    tabel("Welke curve is breder? Telkens hetzelfde gemiddelde.", [
        ("N(50; 4) of N(50; 9)", "N(50; 9)"),
        ("N(20; 2) of N(20; 1)", "N(20; 2)"),
        ("N(0; 1) of N(0; 0,5)", "N(0; 1)"),
    ], "Een grotere σ geeft een bredere, plattere curve.", kolommen=["N(50; 9)", "N(20; 2)", "N(0; 1)"]),
    inv(r"Bij \(X \sim N(170; 10)\): welke lengte hoort bij z = −1,5?", ["155"],
        r"\(170 - 1{,}5 \cdot 10 = 155\)."),
    mk("Jonas haalt 72 op wiskunde (μ = 60, σ = 6) en 80 op Frans (μ = 70, σ = 10). Waar doet hij het relatief beter?",
       ["wiskunde", "Frans", "even goed", "dat kan je niet vergelijken"], 0,
       "Wiskunde: z = 2. Frans: z = 1."),
    koppel("Koppel elk interval rond het gemiddelde aan het percentage volgens de vuistregel.", [
        ["μ ± σ", "ongeveer 68 procent"],
        ["μ ± 2σ", "ongeveer 95 procent"],
        ["μ ± 3σ", "ongeveer 99,7 procent"],
    ], ["ongeveer 50 procent"], "Dit heet ook de 68-95-99,7-regel."),
    keuze(r"Bij \(Z \sim N(0; 1)\) is \(P(-1 < Z < 1)\) ongeveer [[*0,68|0,95|0,5]].",
          "Eén standaardafwijking aan elke kant."),
    sorteer("Verandert dit de plaats of de breedte van de klokcurve?", ["plaats", "breedte"], [
        ["μ wordt groter", "plaats"],
        ["σ wordt kleiner", "breedte"],
        ["μ wordt kleiner", "plaats"],
        ["σ wordt groter", "breedte"],
    ], "μ bepaalt waar de top ligt, σ hoe breed de klok is."),
    sleep("Bij een normale verdeling vallen gemiddelde, [[mediaan]] en modus samen. Een kans is een [[oppervlakte]] onder de curve.",
          ["variantie", "hoogte"], "Door de symmetrie ligt alles onder de top."),
    inv(r"Bij \(X \sim N(80; 5)\): hoeveel procent ligt ongeveer tussen 70 en 85? Gebruik de vuistregel. Schrijf als decimaal getal.", ["81,5", "81.5"],
        "Van −2σ tot 0 is 47,5 procent, van 0 tot +σ is 34 procent. Samen 81,5."),
    volgorde("Zet de stappen om een z-waarde te berekenen in de juiste volgorde.", [
        "μ en σ aflezen",
        "μ aftrekken van de waarde",
        "het verschil delen door σ",
        "het teken van z interpreteren",
    ], r"\(z = (x - \mu) / \sigma\)."),
    met_prent(NC.bestand, tabel("Welke gebieden horen bij dit interval?", [
        ("scores tussen 52 en 68", "D en E"),
        ("scores tussen 44 en 52", "C"),
        ("scores boven 84", "H"),
    ], "Lees de grenzen af op de as.", kolommen=["D en E", "C", "H"])),
    keuze("De gebieden A en H zijn samen ongeveer [[*0,3|5|32]] procent van de scores.",
          "Buiten μ ± 3σ ligt 100 − 99,7 = 0,3 procent."),
    inv(r"Bij \(X \sim N(500; 20)\): welk gewicht hoort bij z = 2,5?", ["550"],
        r"\(500 + 2{,}5 \cdot 20 = 550\)."),
    mk("Welke situatie past het best bij een normale verdeling?",
       ["het gewicht van pakken koffie uit één machine",
        "het aantal kinderen per gezin in een gemeente",
        "het inkomen van alle inwoners van een land",
        "de uitslag van één worp met een eerlijke dobbelsteen"], 0,
       "Een continue meetwaarde die rond een doelgewicht schommelt."),
    inv(r"Bij \(X \sim N(40; 5)\) heeft een waarde z = −0,8. Welke waarde is dat?", ["36"],
        r"\(40 - 0{,}8 \cdot 5 = 36\)."),
    keuze("Bij de standaardnormale verdeling ligt ongeveer 95 procent tussen [[*−2 en 2|−1 en 1|0 en 2]].",
          "Voor Z is μ = 0 en σ = 1."),
    tabel("Klopt dit voor elke normale verdeling?", [
        ("de curve is symmetrisch rond μ", J),
        ("de top ligt boven het gemiddelde", J),
        ("de oppervlakte onder de curve hangt af van σ", F),
    ], "De totale oppervlakte is altijd 1."),
    open_("Een histogram van inkomens in een stad heeft een lange staart naar rechts. Mag je de vuistregel van de normale verdeling gebruiken? Leg uit.",
          "Nee. De vuistregel geldt enkel voor een symmetrische klokvorm. Met een lange staart naar rechts zijn de data scheef, dus past het model van de normale verdeling niet."),
]
