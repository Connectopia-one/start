"""pH, pOH en rekenen met zuren en basen — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# pH-schaal met vijf oplossingen --------------------------------------------
PS = Prent("ph-schaal", "De pH-schaal met vijf oplossingen", "een gekleurde balk van pH 0 tot 14 met vijf pijltjes A tot E")
KLEUREN = ["#d9534f", "#e4683f", "#ec8a3c", "#f2ab3f", "#f4c84a", "#e8d950", "#c8dc5a", "#8fcf6a", "#5fbf8a", "#47aeb0", "#4597c9", "#4b7fcd", "#5867c4", "#6553b5", "#6a439f"]
X0, BREED = 100, 800
for i in range(15):
    PS.rect(X0 + i * BREED / 15, 300, BREED / 15, 70, KLEUREN[i], "none", 0, 0)
PS.rect(X0, 300, BREED, 70, "none", DONKER, 0, 2)


def xph(ph):
    return X0 + (ph + 0.5) * BREED / 15


for i in range(15):
    PS.tekst(xph(i), 400, str(i), 17, vet=True)
PS.tekst(X0, 440, "zuur", 18, "start", vet=True)
PS.tekst(X0 + BREED, 440, "basisch", 18, "end", vet=True)
PH = {"A": 1, "B": 4, "C": 7, "D": 9, "E": 13}
for k, v in PH.items():
    PS.pijl(xph(v), 220, xph(v), 295, DONKER, 3)
    PS.letter(xph(v), 195, k)
ZPS = {k: [Prent.zone(xph(v) - 25, 170, 50, 200)] for k, v in PH.items()}

# Verdunnen van een sterk zuur en een sterke base ----------------------------
VD = Prent("verdunnen-ph", "pH van een sterk zuur en een sterke base bij telkens tien keer verdunnen", "assenstelsel met het aantal keer tien keer verdunnen horizontaal en de pH verticaal; een stijgende en een dalende kromme die allebei naar 7 gaan; punten P, Q en R")
X, Y = assen(VD, 0, 8, 0, 14, "aantal keer ×10 verdund", "pH", 1, 2, links=130, rechts=900)


def _zuur(n):
    c = 10 ** (-1 - n)
    h = c / 2 + math.sqrt(c * c / 4 + 1e-14)
    return -math.log10(h)


VD.lijn(X(0), Y(7), X(8), Y(7), GRIJS, 1, stippel=True)
VD.pad("M " + " L ".join(f"{X(n / 10):.1f} {Y(_zuur(n / 10)):.1f}" for n in range(0, 81)), "none", ROOD, 4)
VD.pad("M " + " L ".join(f"{X(n / 10):.1f} {Y(14 - _zuur(n / 10)):.1f}" for n in range(0, 81)), "none", BLAUW, 4)
VD.tekst(X(0.3), Y(0.5), "sterk zuur", 16, "start", kleur=ROOD, vet=True)
VD.tekst(X(0.3), Y(13.3), "sterke base", 16, "start", kleur=BLAUW, vet=True)
PV = {"P": (2, _zuur(2)), "Q": (2, 14 - _zuur(2)), "R": (7, _zuur(7))}
for k, (n, v) in PV.items():
    VD.cirkel(X(n), Y(v), 7, GEEL, DONKER, 2)
    VD.letter(X(n) + 30, Y(v) + (30 if k == "Q" else -30), k)
ZVD = {k: [Prent.rond(X(n), Y(v), 22), Prent.rond(X(n) + 30, Y(v) + (30 if k == "Q" else -30), 22)] for k, (n, v) in PV.items()}

VRAGEN = [
    klik(
        "Klik op de oplossing met pOH 5.",
        PS.bestand, ZPS["D"],
        "pH = 14 − 5 = 9.",
    ),
    klik(
        "Klik op de oplossing met [H₃O⁺] = 10⁻⁴ mol/L.",
        PS.bestand, ZPS["B"],
        "pH = 4.",
    ),
    met_prent(PS.bestand, tabel(
        "Hoeveel keer meer H₃O⁺ zit er in de eerste oplossing dan in de tweede?",
        [
            ("A tegenover B", "1000"),
            ("B tegenover C", "1000"),
            ("C tegenover D", "100"),
            ("A tegenover C", "1 000 000"),
        ],
        "Elke pH-eenheid is een factor tien.",
        kolommen=["100", "1000", "1 000 000"],
    )),
    met_prent(PS.bestand, tabel(
        "Welke letter past bij deze oplossing?",
        [
            ("0,1 mol/L zoutzuur", "A"),
            ("0,1 mol/L natriumhydroxide", "E"),
            ("zuiver water bij 25 °C", "C"),
        ],
        "0,1 = 10⁻¹: pH 1 voor het zuur, pOH 1 en dus pH 13 voor de base.",
        kolommen=["A", "B", "C", "D", "E"],
    )),
    klik(
        "Klik op het punt waar het sterke zuur 100 keer verdund is.",
        VD.bestand, ZVD["P"],
        "Twee stappen van tien keer is honderd keer: de pH gaat van 1 naar 3.",
    ),
    met_prent(VD.bestand, tabel(
        "Kijk naar de verdunningsgrafiek. Klopt dit?",
        [
            ("In P is de pH 3.", J),
            ("In Q is de pH 11.", J),
            ("In R is de oplossing basisch geworden.", F),
            ("Bij heel sterk verdunnen gaan beide krommen naar 7.", J),
        ],
        "Een zuur blijft zuur, hoe sterk je het ook verdunt: de pH kruipt naar 7 maar komt er niet boven.",
    )),
    met_prent(VD.bestand, mk(
        "Waarom loopt de rode kromme helemaal rechts plat bij pH 7?",
        [
            "Het water zelf levert dan het meeste H₃O⁺",
            "Het zuur wordt bij heel sterk verdunnen een base",
            "De pOH wordt dan stilaan groter dan 14",
            "Het zuur verdampt bij sterk verdunnen weg",
        ],
        0,
        "Bij zo weinig zuur bepaalt de ionisatie van water de pH.",
    )),
    tabel(
        "Wat is de pH van deze oplossing?",
        [
            ("0,01 mol/L HCl", "2"),
            ("0,001 mol/L NaOH", "11"),
            ("0,05 mol/L H₂SO₄ (beide protonen af)", "1"),
            ("[OH⁻] = 10⁻⁵ mol/L", "9"),
        ],
        "Bij een base reken je eerst de pOH en trek je die af van 14.",
        kolommen=["1", "2", "9", "11"],
    ),
    inv(
        "Een oplossing heeft pH 3. Wat is [OH⁻] in mol/L? Schrijf als 10^-x.",
        ["10^-11", "10⁻¹¹", "1e-11", "10^(-11)"],
        "pOH = 14 − 3 = 11, dus [OH⁻] = 10⁻¹¹ mol/L.",
    ),
    mk(
        "Je verdunt 10 mL zoutzuur met pH 2 tot 1 L. Wat is de nieuwe pH?",
        ["4", "3", "2", "0"],
        0,
        "Honderd keer verdunnen: twee pH-eenheden hoger.",
    ),
    mk(
        "Je dampt 1 L natronloog met pH 12 in tot 100 mL. Wat is de nieuwe pH?",
        ["13", "11", "12", "14"],
        0,
        "[OH⁻] wordt tien keer groter: pOH van 2 naar 1, dus pH 13.",
    ),
    casus(
        "Je hebt 100 mL zoutzuur van 0,1 mol/L.",
        [
            inv(
                "Wat is de pH?",
                ["1", "pH 1", "een"],
                "0,1 = 10⁻¹.",
            ),
            inv(
                "Je vult aan met water tot 1 L. Wat is de pH nu?",
                ["2", "pH 2", "twee"],
                "Tien keer verdund: [H₃O⁺] = 0,01 mol/L.",
            ),
            keuze(
                "Het aantal mol H₃O⁺ in de oplossing is daarbij [[*gelijk gebleven|tien keer kleiner geworden|tien keer groter geworden]].",
                "Verdunnen verandert de concentratie, niet de hoeveelheid zuur.",
            ),
        ],
    ),
    tabel(
        "Is deze oplossing zuur, neutraal of basisch bij 25 °C?",
        [
            ("pOH = 12", "Zuur"),
            ("[H₃O⁺] = 10⁻⁹ mol/L", "Basisch"),
            ("[H₃O⁺] = [OH⁻]", "Neutraal"),
            ("pH = 6,5", "Zuur"),
        ],
        "pOH 12 betekent pH 2.",
        kolommen=["Zuur", "Neutraal", "Basisch"],
    ),
    volgorde(
        "Zet deze oplossingen van laag naar hoog pH.",
        ["0,1 mol/L HCl", "0,001 mol/L HCl", "zuiver water", "0,001 mol/L NaOH", "0,1 mol/L NaOH"],
        "pH 1, 3, 7, 11 en 13.",
    ),
    mk(
        "Twee oplossingen hebben dezelfde concentratie: 0,1 mol/L azijnzuur en 0,1 mol/L zoutzuur. Wat klopt?",
        [
            "Azijnzuur heeft een hogere pH dan 1",
            "Azijnzuur heeft ook precies pH 1",
            "Azijnzuur heeft een pH boven 7, het is basisch",
            "Zoutzuur heeft van de twee de hoogste pH",
        ],
        0,
        "Een zwak zuur ioniseert maar gedeeltelijk: minder H₃O⁺, hogere pH.",
    ),
    inv(
        "Hoeveel keer minder H₃O⁺ zit er in een oplossing van pH 6 dan in een van pH 2?",
        ["10000", "10 000", "10.000", "tienduizend"],
        "Vier eenheden verschil: 10⁴.",
    ),
    sleep(
        "In water geldt [H₃O⁺] · [OH⁻] = [[10⁻¹⁴]] bij 25 °C. Daarom is pH + pOH = [[14]]. Is de pH groter dan 7, dan is de oplossing [[basisch]].",
        ["10⁻⁷", "7", "zuur"],
        "Kw verandert met de temperatuur, dus ook de neutrale pH.",
    ),
    tabel(
        "Wat gebeurt er met de pH van een sterk zuur?",
        [
            ("tien keer verdunnen", "Stijgt"),
            ("indampen tot de helft", "Daalt"),
            ("een gelijke hoeveelheid zuiver water bijgieten", "Stijgt"),
        ],
        "Lagere concentratie H₃O⁺ geeft een hogere pH.",
        kolommen=["Stijgt", "Daalt"],
    ),
    mk(
        "Je mengt 50 mL HCl van 0,1 mol/L met 50 mL NaOH van 0,1 mol/L. Welke pH verwacht je?",
        ["7", "1", "13", "0"],
        0,
        "Evenveel mol H₃O⁺ en OH⁻: ze neutraliseren elkaar volledig.",
    ),
    koppel(
        "Koppel elke concentratie H₃O⁺ aan de pH.",
        [
            ("1 mol/L", "0"),
            ("10⁻³ mol/L", "3"),
            ("10⁻⁷ mol/L", "7"),
            ("10⁻¹² mol/L", "12"),
        ],
        ["−3"],
        "pH = −log [H₃O⁺].",
    ),
    tabel(
        "Klopt dit over verdunnen van een zwak zuur?",
        [
            ("De ionisatiegraad wordt groter.", J),
            ("De pH stijgt.", J),
            ("De zuurconstante verandert.", F),
        ],
        "Kz hangt alleen van de temperatuur af.",
    ),
    inv(
        "Wat is de pOH van een oplossing met [H₃O⁺] = 10⁻⁸ mol/L?",
        ["6", "pOH 6", "zes"],
        "pH = 8, dus pOH = 14 − 8 = 6.",
    ),
    mk(
        "Hoeveel keer moet je zoutzuur met pH 1 verdunnen om pH 4 te krijgen?",
        ["1000 keer", "3 keer", "30 keer", "100 keer"],
        0,
        "Drie pH-eenheden is een factor 10³.",
    ),
    tabel(
        "Hoeveel is [OH⁻] in deze oplossing?",
        [
            ("pH 13", "10⁻¹ mol/L"),
            ("pH 7", "10⁻⁷ mol/L"),
            ("pH 2", "10⁻¹² mol/L"),
        ],
        "Eerst de pOH: 14 − pH.",
        kolommen=["10⁻¹ mol/L", "10⁻⁷ mol/L", "10⁻¹² mol/L"],
    ),
    keuze(
        "Regenwater met pH 5,6 is [[*licht zuur|neutraal|licht basisch]], door opgelost koolstofdioxide.",
        "Alles onder 7 is zuur bij 25 °C.",
    ),
    tabel(
        "Klopt dit over de pH-schaal?",
        [
            ("Een verschil van 2 eenheden is een factor 100.", J),
            ("Een hogere pH betekent minder H₃O⁺.", J),
            ("Bij pH 7 zit er geen H₃O⁺ meer in water.", F),
        ],
        "Bij pH 7 is [H₃O⁺] = 10⁻⁷ mol/L, even veel als [OH⁻].",
    ),
    inv(
        "Wat is de pH van 0,0001 mol/L kaliumhydroxide, een sterke base?",
        ["10", "pH 10", "tien"],
        "[OH⁻] = 10⁻⁴, pOH 4, pH 14 − 4 = 10.",
    ),
    open_(
        "Leg uit waarom je een zuur nooit tot boven pH 7 kunt verdunnen.",
        "Bij het verdunnen daalt de concentratie van H₃O⁺ uit het zuur, maar water zelf levert ook altijd H₃O⁺ en OH⁻ in gelijke hoeveelheid. Als er bijna geen zuur meer is, wordt de pH bepaald door het water, dus komt hij dicht bij 7. Het zuur voegt nog altijd een beetje H₃O⁺ toe, dus de oplossing blijft net onder 7.",
    ),
]
