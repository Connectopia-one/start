"""Chemisch evenwicht en de wet van Le Chatelier — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Snelheid van heen- en terugreactie ----------------------------------------
SV = Prent("snelheden-evenwicht", "Snelheid van de heen- en de terugreactie in de loop van de tijd", "assenstelsel met de tijd horizontaal en de snelheid verticaal; een dalende kromme voor de heenreactie en een stijgende voor de terugreactie die samenkomen; op een bepaald moment springt de heenreactie omhoog; vier gebieden A tot D")
X, Y = assen(SV, 0, 100, 0, 10, "tijd", "snelheid", 100, 10, links=130, rechts=900)
GEB = {"A": (0, 25), "B": (35, 60), "C": (60, 75), "D": (85, 100)}
for k, (a, b) in GEB.items():
    SV.svg(f'<rect x="{X(a):.1f}" y="{Y(10):.1f}" width="{X(b) - X(a):.1f}" height="{Y(0) - Y(10):.1f}" fill="{"#e8f0e0" if k in "BD" else "#fbf2e0"}" fill-opacity="0.8"/>')


def _heen(t):
    if t < 60:
        return 4 + 5 * math.exp(-t / 10)
    return 5 + 3 * math.exp(-(t - 60) / 8)


def _terug(t):
    if t < 60:
        return 4 - 4 * math.exp(-t / 10)
    return 5 - 1 * math.exp(-(t - 60) / 8)


heen = [(X(t), Y(_heen(t))) for t in [i * 0.5 for i in range(0, 120)]]
SV.pad("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in heen), "none", BLAUW, 4)
SV.lijn(X(59.5), Y(_heen(59.5)), X(60), Y(_heen(60)), BLAUW, 4)
SV.pad("M " + " L ".join(f"{X(t):.1f} {Y(_heen(t)):.1f}" for t in [60 + i * 0.5 for i in range(0, 81)]), "none", BLAUW, 4)
SV.pad("M " + " L ".join(f"{X(t):.1f} {Y(_terug(t)):.1f}" for t in [i * 0.5 for i in range(0, 201)]), "none", ORANJE, 4)
SV.tekst(X(10), Y(7.4), "heenreactie", 16, "start", kleur=BLAUW, vet=True)
SV.tekst(X(3), Y(0.6), "terugreactie", 16, "start", kleur=ORANJE, vet=True)
for k, (a, b) in GEB.items():
    SV.letter((X(a) + X(b)) / 2, Y(10) + 30, k)
ZSV = {k: [Prent.zone(X(a), Y(10), X(b) - X(a), Y(0) - Y(10))] for k, (a, b) in GEB.items()}

# Concentraties bij toevoegen van een reagens -------------------------------
CV = Prent("concentraties-verstoring", "Concentraties in een evenwicht A ⇌ B dat verstoord wordt", "assenstelsel met de tijd horizontaal en de concentratie verticaal; twee krommen die vlak worden, op een tijdstip springt de ene omhoog; letters P, Q en R")
X2, Y2 = assen(CV, 0, 100, 0, 1.0, "tijd", "c (mol/L)", 100, 0.2, links=130, rechts=900)


def _a(t):
    if t < 50:
        return 0.3 + 0.5 * math.exp(-t / 10)
    return 0.45 + 0.25 * math.exp(-(t - 50) / 8)


def _b(t):
    if t < 50:
        return 0.5 - 0.5 * math.exp(-t / 10)
    return 0.75 - 0.25 * math.exp(-(t - 50) / 8)


CV.pad("M " + " L ".join(f"{X2(t):.1f} {Y2(_a(t)):.1f}" for t in [i * 0.5 for i in range(0, 100)]), "none", BLAUW, 4)
CV.lijn(X2(49.5), Y2(_a(49.5)), X2(50), Y2(_a(50)), BLAUW, 4)
CV.pad("M " + " L ".join(f"{X2(t):.1f} {Y2(_a(t)):.1f}" for t in [50 + i * 0.5 for i in range(0, 101)]), "none", BLAUW, 4)
CV.pad("M " + " L ".join(f"{X2(t):.1f} {Y2(_b(t)):.1f}" for t in [i * 0.5 for i in range(0, 201)]), "none", ORANJE, 4)
CV.tekst(X2(97), Y2(0.38), "[A]", 18, "end", kleur=BLAUW, vet=True)
CV.tekst(X2(97), Y2(0.8), "[B]", 18, "end", kleur=ORANJE, vet=True)
LCV = {"P": (X2(20), Y2(0.9)), "Q": (X2(50), Y2(0.9)), "R": (X2(80), Y2(0.9))}
for k, (x, y) in LCV.items():
    CV.letter(x, y, k)
CV.lijn(X2(50), Y2(0.86), X2(50), Y2(0.02), GRIJS, 1, stippel=True)
ZCV = {"P": [Prent.zone(X2(0), Y2(1.0), X2(45) - X2(0), Y2(0) - Y2(1.0))],
       "Q": [Prent.zone(X2(46), Y2(1.0), X2(54) - X2(46), Y2(0) - Y2(1.0))],
       "R": [Prent.zone(X2(55), Y2(1.0), X2(100) - X2(55), Y2(0) - Y2(1.0))]}

VRAGEN = [
    klik(
        "Klik op een gebied waar het evenwicht nog niet bereikt is en er netto product bijkomt.",
        SV.bestand, ZSV["A"],
        "De heenreactie is daar sneller dan de terugreactie.",
    ),
    klik(
        "Klik op het gebied net na de verstoring, waar het evenwicht naar rechts schuift.",
        SV.bestand, ZSV["C"],
        "De heenreactie springt omhoog, bijvoorbeeld door extra reagens, en wordt even sneller dan de terugreactie.",
    ),
    met_prent(SV.bestand, tabel(
        "Kijk naar de snelheden. Klopt dit?",
        [
            ("In B en D zijn de twee snelheden gelijk.", J),
            ("In B staan de reacties stil.", F),
            ("In D liggen de snelheden hoger dan in B.", J),
            ("In A is de terugreactie sneller dan de heenreactie.", F),
        ],
        "In een dynamisch evenwicht lopen beide reacties door, even snel.",
    )),
    klik(
        "Klik op het moment waarop extra A wordt toegevoegd.",
        CV.bestand, ZCV["Q"],
        "Daar springt [A] plots omhoog.",
    ),
    met_prent(CV.bestand, tabel(
        "Wat gebeurt er in dit deel van de grafiek?",
        [
            ("P", "Evenwicht instellen"),
            ("Q", "Verstoring"),
            ("R", "Nieuw evenwicht instellen"),
        ],
        "Na de verstoring zakt [A] weer wat en stijgt [B]: het evenwicht verschuift naar rechts.",
        kolommen=["Evenwicht instellen", "Verstoring", "Nieuw evenwicht instellen"],
    )),
    met_prent(CV.bestand, mk(
        "Bereken K voor A ⇌ B met het eerste evenwicht (voor de verstoring).",
        ["Ongeveer 1,7", "Ongeveer 0,6", "Ongeveer 0,2", "Ongeveer 8"],
        0,
        "K = [B] / [A] = 0,5 / 0,3 ≈ 1,7.",
    )),
    met_prent(CV.bestand, mk(
        "Hoe groot is [B] / [A] in het nieuwe evenwicht, helemaal rechts?",
        [
            "Ongeveer 1,7, net als voor de verstoring",
            "Groter dan 1,7, want er is meer A",
            "Kleiner dan 1,7, want er is meer A",
            "Precies 1, want alles is opnieuw verdeeld",
        ],
        0,
        "0,75 / 0,45 ≈ 1,7. Bij gelijke temperatuur blijft K dezelfde, alleen de ligging verschuift.",
    )),
    inv(
        "Schrijf de uitdrukking van K voor N₂ + 3 H₂ ⇌ 2 NH₃. Welke exponent krijgt [H₂]?",
        ["3", "drie"],
        "K = [NH₃]² / ([N₂] · [H₂]³).",
    ),
    tabel(
        "Welke kant gaat het evenwicht N₂ + 3 H₂ ⇌ 2 NH₃ (exo-energetisch) op?",
        [
            ("je voegt N₂ toe", "Naar rechts"),
            ("je haalt NH₃ weg", "Naar rechts"),
            ("je verwarmt het mengsel", "Naar links"),
            ("je vergroot het volume van het vat", "Naar links"),
        ],
        "Rechts staan 2 mol gas, links 4 mol. Verwarmen bevoordeelt de endo-energetische terugreactie.",
        kolommen=["Naar links", "Naar rechts"],
    ),
    tabel(
        "Verandert de waarde van K door deze verstoring?",
        [
            ("de concentratie van een reagens verhogen", "Nee"),
            ("de temperatuur verhogen", "Ja"),
            ("een katalysator toevoegen", "Nee"),
            ("het volume verkleinen", "Nee"),
        ],
        "Alleen de temperatuur verandert K.",
        kolommen=["Ja", "Nee"],
    ),
    tabel(
        "Q is het reactiequotiënt. Welke kant gaat het mengsel op?",
        [
            ("Q < K", "Naar rechts"),
            ("Q > K", "Naar links"),
            ("Q = K", "Blijft"),
        ],
        "Het mengsel gaat altijd in de richting die Q gelijk maakt aan K.",
        kolommen=["Naar links", "Naar rechts", "Blijft"],
    ),
    casus(
        "Het evenwicht 2 NO₂ (bruin) ⇌ N₂O₄ (kleurloos) is exo-energetisch naar rechts.",
        [
            keuze(
                "Zet je de buis in ijswater, dan wordt het gas [[*lichter|donkerder|even bruin]].",
                "Afkoelen bevoordeelt de exo-energetische richting: meer kleurloos N₂O₄.",
            ),
            keuze(
                "Duw je de zuiger in, dan verschuift het evenwicht naar [[*N₂O₄|NO₂]], want daar zijn er minder mol gas.",
                "2 mol gas links tegenover 1 mol rechts.",
            ),
            mk(
                "Wat gebeurt er met K als je de buis opwarmt?",
                ["K wordt kleiner", "K wordt groter", "K blijft gelijk", "K wordt nul"],
                0,
                "Opwarmen verschuift een exo-energetisch evenwicht naar links: minder product, kleinere K.",
            ),
        ],
    ),
    tabel(
        "Verschuift dit evenwicht als je de druk verhoogt?",
        [
            ("H₂ + I₂ ⇌ 2 HI (alles gas)", "Nee"),
            ("N₂ + 3 H₂ ⇌ 2 NH₃", "Ja"),
            ("2 SO₂ + O₂ ⇌ 2 SO₃", "Ja"),
            ("CO + H₂O ⇌ CO₂ + H₂ (alles gas)", "Nee"),
        ],
        "Tel de mol gas links en rechts. Gelijk aantal: geen verschuiving.",
        kolommen=["Ja", "Nee"],
    ),
    mk(
        "Een katalysator verandert de ligging van een evenwicht niet. Waarom gebruikt men hem dan toch?",
        [
            "Het evenwicht wordt veel sneller bereikt",
            "De evenwichtsconstante wordt groter",
            "Er ontstaat meer product in het evenwicht",
            "De terugreactie wordt helemaal stopgezet",
        ],
        0,
        "Heen- en terugreactie gaan evenveel sneller: zelfde evenwicht, sneller bereikt.",
    ),
    inv(
        "Je verwacht 20 g product en haalt er 15 g uit. Wat is het rendement in procent?",
        ["75", "75 %", "75%"],
        "15 / 20 = 0,75 = 75 %.",
    ),
    inv(
        "Van 2 mol beginstof heeft 0,5 mol gereageerd. Wat is de omzettingsgraad in procent?",
        ["25", "25 %", "25%"],
        "0,5 / 2 = 0,25 = 25 %.",
    ),
    tabel(
        "Is dit een chemisch evenwicht, een aflopende reactie of geen reactie?",
        [
            ("er blijft van elke stof iets over, de concentraties blijven gelijk", "Evenwicht"),
            ("één beginstof is helemaal op", "Aflopend"),
            ("de stoffen reageren niet met elkaar", "Geen reactie"),
        ],
        "Een evenwicht houdt alle stoffen in het mengsel, ook al lijkt er niets te gebeuren.",
        kolommen=["Evenwicht", "Aflopend", "Geen reactie"],
    ),
    mk(
        "Bij welk evenwicht ligt het mengsel het sterkst aan de kant van de producten?",
        ["K = 10⁵", "K = 1", "K = 10⁻³", "K = 0,5"],
        0,
        "Hoe groter K, hoe meer producten in verhouding tot reagentia.",
    ),
    sleep(
        "Volgens Le Chatelier-Van 't Hoff [[werkt]] een evenwicht een verstoring [[tegen]]. Verwarm je, dan wint de [[endo-energetische]] richting.",
        ["versterkt", "mee", "exo-energetische"],
        "De verschuiving neemt een deel van de toegevoegde warmte weer op.",
    ),
    tabel(
        "Klopt dit over een dynamisch evenwicht?",
        [
            ("Je bereikt hetzelfde evenwicht vanuit de reagentia of vanuit de producten.", J),
            ("De concentraties van reagentia en producten zijn gelijk.", F),
            ("Er vormen voortdurend nieuwe productdeeltjes.", J),
        ],
        "Constant is niet hetzelfde als gelijk.",
    ),
    mk(
        "Waarom haalt men bij de productie van ammoniak het ammoniak voortdurend uit het mengsel?",
        [
            "Zo blijft het evenwicht naar rechts schuiven",
            "Zo wordt de evenwichtsconstante telkens groter",
            "Zo wordt de reactie endo-energetisch gemaakt",
            "Zo is er geen katalysator meer nodig daarna",
        ],
        0,
        "Een product weghalen is een verstoring die het evenwicht tegenwerkt door nieuw product te maken.",
    ),
    inv(
        "Bij een evenwicht is [A] = 0,2 mol/L en [B] = 0,8 mol/L voor A ⇌ B. Wat is K?",
        ["4", "vier"],
        "K = [B] / [A] = 0,8 / 0,2 = 4.",
    ),
    mk(
        "Bij A ⇌ B is K = 4. Een mengsel heeft [A] = 0,5 en [B] = 0,5 mol/L. Wat gebeurt er?",
        [
            "Er ontstaat meer B tot de verhouding 4 is",
            "Er ontstaat meer A tot de verhouding 4 is",
            "Er gebeurt niets, het is al een evenwicht",
            "De evenwichtsconstante wordt gelijk aan 1",
        ],
        0,
        "Q = 1 is kleiner dan K = 4: de reactie gaat naar rechts.",
    ),
    tabel(
        "Een gekleurd evenwicht wordt donkerder als je het opwarmt. Klopt dit?",
        [
            ("De richting naar de gekleurde stof is endo-energetisch.", J),
            ("Bij afkoelen wordt het mengsel lichter.", J),
            ("K verandert niet bij het opwarmen.", F),
        ],
        "Opwarmen bevoordeelt de endo-energetische richting, en dat verandert K.",
    ),
    volgorde(
        "Zet in de goede volgorde wat er gebeurt als je een product wegneemt uit een evenwicht.",
        [
            "De concentratie van het product daalt",
            "De terugreactie wordt trager",
            "De heenreactie is even sneller dan de terugreactie",
            "Er ontstaat nieuw product tot het evenwicht hersteld is",
        ],
        "Het evenwicht werkt de verstoring tegen door het weggenomen product aan te vullen.",
    ),
    keuze(
        "Het reactiequotiënt Q gebruikt dezelfde formule als K, maar met de concentraties [[*van elk ogenblik|in het evenwicht|bij de start]].",
        "Door Q en K te vergelijken weet je welke kant een mengsel op gaat.",
    ),
    koppel(
        "Koppel elke verstoring van een gasevenwicht aan de kant waar het naartoe schuift.",
        [
            ("volume verkleinen", "naar minder mol gas"),
            ("druk verlagen", "naar meer mol gas"),
            ("temperatuur verhogen", "naar de endo-energetische kant"),
            ("temperatuur verlagen", "naar de exo-energetische kant"),
        ],
        ["naar de kant van de katalysator"],
        "Telkens werkt het evenwicht de verandering tegen.",
    ),
    open_(
        "Leg uit waarom een evenwicht verschuift als je extra reagens toevoegt, maar de evenwichtsconstante toch gelijk blijft.",
        "Door extra reagens wordt de noemer in het reactiequotiënt groter, zodat Q kleiner is dan K. De heenreactie wordt even sneller dan de terugreactie, er ontstaat meer product en er verdwijnt wat reagens, tot Q weer gelijk is aan K. De ligging verandert dus, maar de verhouding die K bepaalt, blijft bij dezelfde temperatuur dezelfde.",
    ),
]
