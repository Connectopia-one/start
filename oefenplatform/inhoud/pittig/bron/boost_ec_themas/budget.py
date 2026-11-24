"""De budgetlijn en de optimale goederencombinatie — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_budget, met een zelfgetekende budgetlijn en indifferentiecurven om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, GROEN, ROOD, DONKER

# Budget 80 euro, x kost 8 euro, y kost 10 euro: 8x + 10y = 80. Snijpunten x = 10, y = 8.
BL = Prent("budgetlijn-optimum", "Budgetlijn en indifferentiecurven", "budgetlijn 8x + 10y = 80 met drie indifferentiecurven en punten A tot E")
OX, OY, S = 140, 560, 44
def P(x, y): return OX + x * S, OY - y * S
BL.lijn(OX, OY, OX + 720, OY, DONKER, 3); BL.lijn(OX, OY, OX, 60, DONKER, 3)
for i in range(1, 15):
    BL.lijn(P(i, 0)[0], OY, P(i, 0)[0], OY + 8, DONKER, 2); BL.tekst(P(i, 0)[0], OY + 28, str(i), 15)
for i in range(1, 11):
    BL.lijn(OX - 8, P(0, i)[1], OX, P(0, i)[1], DONKER, 2); BL.tekst(OX - 14, P(0, i)[1] + 5, str(i), 15, "end")
BL.tekst(OX + 720, OY + 56, "goed x", 18, "end"); BL.tekst(OX - 10, 50, "goed y", 18, "start")
BL.lijn(*P(0, 8), *P(10, 0), ROOD, 4)
BL.tekst(P(10, 0)[0] + 8, P(10, 0)[1] - 12, "budgetlijn", 17, "start", ROOD, True)
# indifferentiecurven: (x)(y) = k, k = 10,752 (snijdt in C en E), 20 (raakt in (5,4)), 35
for k, kleur, naam in ((10.752, BLAUW, "I1"), (20, GROEN, "I2"), (35, ORANJE, "I3")):
    pts = []; x = k / 10.5
    while x <= 14.5:
        pts.append(P(x, k / x)); x += 0.2
    BL.pad("M " + " L ".join(f"{a:.1f},{b:.1f}" for a, b in pts), "none", kleur, 3)
    lx, ly = P(14.6, k / 14.6); BL.tekst(lx + 8, ly + 6, naam, 18, "start", kleur, True)
PUNTEN = {"A": (5, 4), "B": (2, 4), "C": (1.6, 6.72), "D": (7, 5), "E": (8.4, 1.28)}
for t, (x, y) in PUNTEN.items():
    px, py = P(x, y); BL.cirkel(px, py, 7, DONKER, DONKER, 1); BL.letter(px + 24, py - 22, t)
U = "budgetlijn-optimum.svg"
Z = {t: Prent.zone(P(x, y)[0] - 22, P(x, y)[1] - 50, 75, 72) for t, (x, y) in PUNTEN.items()}

VRAGEN = [
    klik("Het budget is 80 euro, x kost 8 euro en y kost 10 euro. Klik op de optimale goederencombinatie.", U, [Z["A"]],
         "In A raakt de budgetlijn de hoogst bereikbare indifferentiecurve I2: 8·5 + 10·4 = 80."),
    klik("Klik op een combinatie die de consument kan betalen, maar waarbij hij geld overhoudt.", U, [Z["B"]],
         "B ligt onder de budgetlijn: 8·2 + 10·4 = 56 euro."),
    klik("Klik op de combinatie die de consument niet kan betalen.", U, [Z["D"]],
         "D ligt boven de budgetlijn: 8·7 + 10·5 = 106 euro, meer dan 80."),
    klik("Klik op een punt waar de budgetlijn een indifferentiecurve snijdt, zodat de consument nog beter kan.", U, [Z["C"], Z["E"]],
         "C en E liggen op de budgetlijn én op I1. Langs de budgetlijn kan hij naar A schuiven en I2 halen."),
    tabel("Klopt dit volgens de prent?",
          [("I3 is voor deze consument onbereikbaar.", J), ("C en E kosten allebei 80 euro.", J), ("C en E geven evenveel nut als A.", F), ("In A zijn de helling van de budgetlijn en die van I2 gelijk.", J)],
          "C en E liggen op I1, lager dan I2."),
    casus("Lees de gegevens.\n\nMilan heeft 90 euro voor bioscoopbezoeken (x) en boeken (y). Een bioscoopbezoek kost 9 euro, een boek 15 euro.", [
        mk("Hoe luidt zijn budgetvergelijking?",
           ["9x + 15y = 90", "15x + 9y = 90", "9x + 15y = 135", "x + y = 90"], 0,
           "Prijs van x maal x, plus prijs van y maal y, is het budget."),
        inv("Hoeveel boeken kan hij kopen als hij niet naar de bioscoop gaat? Schrijf enkel het getal.", ["6"],
            "90 / 15 = 6."),
        inv("Hij gaat 5 keer naar de bioscoop. Hoeveel boeken kan hij dan nog kopen? Schrijf enkel het getal.", ["3"],
            "5 × 9 = 45; 90 − 45 = 45; 45 / 15 = 3."),
        keuze("De prijs van een bioscoopbezoek daalt naar 6 euro. De budgetlijn [[*draait rond het snijpunt met de as van y|schuift evenwijdig naar buiten|blijft liggen]].",
              "Wie alles aan boeken besteedt, merkt niets; de rest van de lijn draait naar buiten."),
        inv("Hoeveel keer kan hij dan maximaal naar de bioscoop? Schrijf enkel het getal.", ["15"],
            "90 / 6 = 15."),
    ]),
    tabel("Wat gebeurt er met de budgetlijn?",
          [("Het budget stijgt, de prijzen blijven gelijk.", "schuift evenwijdig"), ("Enkel de prijs van x daalt.", "draait"), ("Het budget en beide prijzen verdubbelen.", "blijft liggen"), ("Het budget daalt, de prijzen blijven gelijk.", "schuift evenwijdig")],
          "Een budgetwijziging verschuift, een prijswijziging van één goed draait, alles samen evenredig verandert niets.",
          kolommen=["schuift evenwijdig", "draait", "blijft liggen"]),
    keuze("De helling van de budgetlijn hangt af van de [[*verhouding van de prijzen|hoogte van het budget|voorkeuren van de consument]].",
          "Helling = px / py."),
    keuze("De helling van een indifferentiecurve hangt af van de [[*voorkeuren van de consument|prijzen van de goederen|hoogte van het budget]].",
          "Die helling is de ruilverhouding die de consument zelf wil."),
    inv("Een boek kost 20 euro, een film 5 euro. Hoeveel films kost één boek? Schrijf enkel het getal.", ["4"],
        "20 / 5 = 4: voor één boek geef je vier films op."),
    inv("Een consument heeft 150 euro. Goed x kost 15 euro, goed y 25 euro. Waar snijdt de budgetlijn de as van y? Schrijf enkel het getal.", ["6"],
        "150 / 25 = 6."),
    inv("Een gezin heeft 200 euro. Vlees kost 16 euro per kilo, groenten 4 euro per kilo. Het koopt 8 kilo vlees. Hoeveel kilo groenten kan het nog kopen? Schrijf enkel het getal.", ["18"],
        "8 × 16 = 128; 200 − 128 = 72; 72 / 4 = 18."),
    sorteer("Waar ligt deze combinatie? Budget 60 euro, x kost 6 euro, y kost 4 euro.", ["onder de budgetlijn", "op de budgetlijn", "boven de budgetlijn"],
            [("4 x en 9 y", "op de budgetlijn"), ("5 x en 5 y", "onder de budgetlijn"), ("8 x en 4 y", "boven de budgetlijn"), ("10 x en 0 y", "op de budgetlijn"), ("2 x en 10 y", "onder de budgetlijn"), ("6 x en 7 y", "boven de budgetlijn")],
            "Reken 6x + 4y uit en vergelijk met 60."),
    mk("Waarom ligt het optimum altijd op de budgetlijn?",
       ["Met het overschot wint hij nog nut.", "Onder de lijn zijn de prijzen hoger.", "Boven de lijn is het nut altijd nul.", "Op de lijn zijn alle combinaties gelijk."], 0,
       "Zolang er budget overblijft, kan hij een hogere curve halen."),
    tabel("Klopt dit over het optimum?",
          [("In het optimum raakt de budgetlijn de hoogst bereikbare indifferentiecurve.", J), ("Een snijpunt met een indifferentiecurve is het optimum.", F), ("Twee consumenten met hetzelfde budget en dezelfde prijzen kiezen altijd hetzelfde.", F), ("Stijgt het budget, dan haalt het optimum een hogere curve.", J)],
          "Een snijpunt laat nog een hogere curve toe; voorkeuren verschillen."),
    keuze("Een gezin krijgt 5 % opslag, maar alle prijzen stijgen met 5 %. De budgetlijn [[*blijft liggen|schuift naar buiten|draait]].",
          "Budget en prijzen stijgen evenredig: de koopkracht verandert niet."),
    tabel("Schuift de budgetlijn van een gezin hierdoor naar buiten?",
          [("een hogere kinderbijslag", J), ("een lagere belasting op het inkomen", J), ("een hogere btw op alle producten", F)],
          "Meer budget of lagere prijzen vergroten de haalbare combinaties."),
    inv("In het optimum besteedt een consument 300 euro. Goed x kost 30 euro en hij koopt 6 x. Goed y kost 20 euro. Hoeveel y koopt hij? Schrijf enkel het getal.", ["6"],
        "6 × 30 = 180; 300 − 180 = 120; 120 / 20 = 6."),
    sleep("Links in de budgetvergelijking staan de [[uitgaven]] aan beide goederen, rechts staat het [[budget]].",
          ["nut", "prijzen"], "px·x + py·y = budget."),
    keuze("Daalt de prijs van x, dan koopt de consument meestal [[*meer|minder]] van x.",
          "Zijn koopkracht stijgt en x wordt relatief goedkoper. Zo verklaart de theorie de vraagcurve."),
    keuze("Zolang de prijzen vastliggen, is de budgetlijn een [[*rechte|kromme|cirkel]].",
          "De helling is overal dezelfde prijsverhouding."),
    inv("Budget 120 euro, x kost 10 euro, y kost 20 euro. De prijs van x zakt naar 8 euro. Hoeveel x kan hij nu maximaal kopen? Schrijf enkel het getal.", ["15"],
        "120 / 8 = 15."),
    keuze("Een punt onder de budgetlijn is [[*betaalbaar maar niet optimaal|onbetaalbaar|altijd het optimum]].",
          "Er blijft geld over waarmee hij nog nut kan winnen."),
    koppel("Welk gegeven hoort bij welk deel van de tekening?",
           [("budget / prijs van x", "snijpunt met de as van x"), ("budget / prijs van y", "snijpunt met de as van y"), ("prijs van x / prijs van y", "helling van de budgetlijn")],
           ["helling van de indifferentiecurve"], "Zo teken je een budgetlijn uit drie gegevens."),
    inv("Een consument heeft 48 euro. Goed x kost 6 euro, goed y 8 euro. Hij koopt 4 x. Hoeveel y kan hij nog kopen? Schrijf enkel het getal.", ["3"],
        "4 × 6 = 24; 48 − 24 = 24; 24 / 8 = 3."),
    open_("Leg uit waarom twee vrienden met hetzelfde zakgeld en dezelfde prijzen toch iets anders kopen.",
          "Hun budgetlijn is dezelfde, maar hun voorkeuren en dus hun indifferentiecurven verschillen, zodat het raakpunt op een andere plaats ligt.",
          "Dezelfde budgetlijn, andere indifferentiemap."),
]
