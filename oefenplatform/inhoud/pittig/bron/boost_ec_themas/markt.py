"""De markt met volkomen concurrentie en de overheid — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_markt, met een zelfgetekende vraag- en aanbodgrafiek om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, PAARS, ROOD, DONKER

# Qv = 150 − 3P, Qa = 30 + 3P: evenwicht P = 20, Q = 90
VA = Prent("vraag-aanbod-grenzen", "Markt voor huurfietsen per dag", "vraag- en aanbodcurve met een prijslijn van 14 en van 26 euro en punten A tot E")
OX, OY = 140, 570
def P(q, p): return OX + q * 4.6, OY - p * 13
VA.lijn(OX, OY, OX + 760, OY, DONKER, 3); VA.lijn(OX, OY, OX, 50, DONKER, 3)
for q in range(20, 170, 20):
    VA.lijn(P(q, 0)[0], OY, P(q, 0)[0], OY + 8, DONKER, 2); VA.tekst(P(q, 0)[0], OY + 28, str(q), 16)
for p in range(5, 40, 5):
    VA.lijn(OX - 8, P(0, p)[1], OX, P(0, p)[1], DONKER, 2); VA.tekst(OX - 14, P(0, p)[1] + 5, str(p), 15, "end")
VA.tekst(OX + 760, OY + 56, "hoeveelheid Q", 18, "end"); VA.tekst(OX - 10, 42, "prijs P (euro)", 18, "start")
VA.lijn(*P(150 - 3 * 36, 36), *P(150 - 3 * 2, 2), BLAUW, 4)
VA.lijn(*P(30 + 3 * 2, 2), *P(30 + 3 * 36, 36), ORANJE, 4)
VA.tekst(P(150 - 3 * 3, 3)[0] + 10, P(150 - 3 * 3, 3)[1] - 6, "vraag", 18, "start", BLAUW, True)
VA.tekst(P(30 + 3 * 35, 35)[0] + 10, P(30 + 3 * 35, 35)[1] + 6, "aanbod", 18, "start", ORANJE, True)
for p in (14, 26):
    VA.lijn(OX, P(0, p)[1], OX + 740, P(0, p)[1], PAARS, 2, True)
    VA.tekst(OX + 740, P(0, p)[1] - 8, f"{p} euro", 16, "end", PAARS, True)
PT = {"A": (90, 20), "B": (72, 14), "C": (108, 14), "D": (72, 26), "E": (108, 26)}
OFF = {"A": (32, 4), "B": (-30, 30), "C": (30, 30), "D": (-30, -26), "E": (30, -26)}
for t, (q, p) in PT.items():
    x, y = P(q, p); VA.cirkel(x, y, 7, DONKER, DONKER, 1); VA.letter(x + OFF[t][0], y + OFF[t][1], t)
U = "vraag-aanbod-grenzen.svg"
Z = {t: Prent.rond(P(q, p)[0] + OFF[t][0], P(q, p)[1] + OFF[t][1], 32) for t, (q, p) in PT.items()}

VRAGEN = [
    klik("Klik op het marktevenwicht.", U, [Z["A"]],
         "In A snijden vraag en aanbod elkaar: P = 20, Q = 90."),
    klik("De overheid legt een maximumprijs van 14 euro op. Klik op het punt dat toont hoeveel er dan gevraagd wordt.", U, [Z["C"]],
         "Bij 14 euro ligt de vraag op 150 − 42 = 108 (punt C). Het aanbod is maar 72 (punt B): een tekort van 36."),
    klik("De overheid legt een minimumprijs van 26 euro op. Klik op het punt dat toont hoeveel er dan aangeboden wordt.", U, [Z["E"]],
         "Bij 26 euro is het aanbod 30 + 78 = 108 (punt E) en de vraag 72 (punt D): een overschot van 36."),
    tabel("Klopt dit volgens de grafiek?",
          [("Bij een maximumprijs van 14 euro ontstaat er een tekort.", J), ("Bij een minimumprijs van 26 euro ontstaat er een tekort.", F), ("Een maximumprijs van 26 euro zou niets veranderen.", J), ("Een minimumprijs van 14 euro zou niets veranderen.", J)],
          "Een plafond boven het evenwicht en een bodem eronder zijn niet bindend."),
    casus("Lees de functies.\n\nOp de markt voor verse aardbeien geldt: Qv = 900 − 50P en Qa = 100 + 30P (P in euro per kilo, Q in kilo per dag).", [
        inv("Wat is de evenwichtsprijs? Schrijf enkel het getal.", ["10"],
            "900 − 50P = 100 + 30P → 800 = 80P → P = 10."),
        inv("Wat is de evenwichtshoeveelheid? Schrijf enkel het getal.", ["400"],
            "900 − 500 = 400 en 100 + 300 = 400."),
        inv("Hoe groot is het tekort bij een prijs van 8 euro? Schrijf enkel het getal.", ["160"],
            "Qv = 900 − 400 = 500; Qa = 100 + 240 = 340; tekort = 160."),
        keuze("Bij een prijs van 12 euro is er een [[*overschot|tekort|evenwicht]].",
              "Qv = 300, Qa = 460: er wordt meer aangeboden dan gevraagd."),
    ]),
    tabel("Wat verschuift er op de markt?",
          [("Het inkomen van de gezinnen stijgt (gewoon goed).", "vraag naar rechts"), ("De grondstoffen worden duurder.", "aanbod naar links"), ("Er komen veel nieuwe aanbieders bij.", "aanbod naar rechts"), ("Het product raakt uit de mode.", "vraag naar links")],
          "Vraagfactoren verschuiven de vraag, kostenfactoren het aanbod.",
          kolommen=["vraag naar rechts", "vraag naar links", "aanbod naar rechts", "aanbod naar links"]),
    tabel("Stijgt of daalt de evenwichtsprijs?",
          [("De vraag schuift naar rechts.", "stijgt"), ("Het aanbod schuift naar rechts.", "daalt"), ("Het aanbod schuift naar links.", "stijgt"), ("De vraag schuift naar links.", "daalt")],
          "Meer vraag of minder aanbod duwt de prijs omhoog.",
          kolommen=["stijgt", "daalt"]),
    keuze("De prijs van een product daalt. De consumenten [[*schuiven over dezelfde vraagcurve|verschuiven de hele vraagcurve]].",
          "Een prijsverandering is een beweging langs de curve."),
    keuze("Een tekort duwt de prijs [[*omhoog|omlaag]].",
          "Klanten zijn bereid meer te betalen."),
    tabel("Hoort dit bij volkomen concurrentie?",
          [("heel veel kopers en verkopers", J), ("een homogeen product", J), ("één aanbieder die de prijs bepaalt", F), ("volledige informatie over prijs en kwaliteit", J), ("hoge drempels om toe te treden", F)],
          "Bij volkomen concurrentie is elk bedrijf een prijsnemer en is toetreden vrij."),
    mk("Op welke van deze markten zijn de bedrijven het duidelijkst prijsnemers?",
       ["de wereldmarkt voor koffiebonen", "de markt voor smartphones van één merk", "de markt voor treinreizen in België", "de markt voor designerschoenen"], 0,
       "Een homogeen product met veel kopers en verkopers."),
    keuze("Een prijsnemer die meer vraagt dan de marktprijs, [[*verkoopt niets meer|verkoopt evenveel|verkoopt meer]].",
          "De klanten kopen dan bij een andere aanbieder."),
    inv("De vraag is Qv = 300 − 6P. Hoeveel wordt er gevraagd bij een prijs van 15? Schrijf enkel het getal.", ["210"],
        "300 − 90 = 210."),
    inv("Het aanbod is Qa = 40 + 4P. Hoeveel wordt er aangeboden bij een prijs van 20? Schrijf enkel het getal.", ["120"],
        "40 + 80 = 120."),
    sorteer("Ontstaat er een tekort of een overschot?", ["tekort", "overschot"],
            [("maximumprijs onder het evenwicht", "tekort"), ("minimumprijs boven het evenwicht", "overschot"), ("prijs boven het evenwicht zonder ingreep", "overschot"), ("prijs onder het evenwicht zonder ingreep", "tekort")],
            "Een te lage prijs geeft een tekort, een te hoge een overschot."),
    tabel("Welk gevolg kan een tekort door een maximumprijs hebben?",
          [("wachtlijsten", J), ("een zwarte markt", J), ("een groot overschot in de winkels", F), ("rantsoenering", J)],
          "Er is te weinig voor iedereen die wil kopen aan die prijs."),
    keuze("Een overheid legt soms een maximumprijs op om een basisgoed [[*betaalbaar te houden|duurder te maken|uit de markt te halen]].",
          "Denk aan huur of energie."),
    keuze("Bij een minimumprijs boven het evenwicht koopt de overheid soms het [[*overschot op|tekort op|aanbod af]].",
          "Anders blijft de voorraad liggen."),
    mk("Een hittegolf doet de vraag naar ijs stijgen. Wat gebeurt er?",
       ["De prijs en de hoeveelheid stijgen.", "De prijs stijgt en de hoeveelheid daalt.", "De prijs daalt en de hoeveelheid stijgt.", "De prijs en de hoeveelheid dalen."], 0,
       "De vraagcurve schuift naar rechts langs de stijgende aanbodcurve."),
    sleep("Het marktmechanisme is [[zelfregulerend]]: een tekort duwt de prijs [[omhoog]] en een overschot duwt de prijs [[omlaag]].",
          ["vast", "naar links"], "Zo stuurt de prijs vraag en aanbod bij."),
    keuze("Volkomen concurrentie is vooral een model, want merken, reclame en patenten [[*maken producten verschillend|zijn verboden|bestaan niet]].",
          "Bijna geen echte markt voldoet aan alle voorwaarden."),
    klik("Klik op het punt dat toont hoeveel er aangeboden wordt bij een maximumprijs van 14 euro.", U, [Z["B"]],
         "Bij 14 euro bieden de verhuurders 30 + 42 = 72 fietsen aan."),
    inv("Hoe groot is het overschot bij een minimumprijs van 26 euro in de grafiek van de huurfietsen? Schrijf enkel het getal.", ["36"],
        "Aanbod 108 − vraag 72 = 36."),
    keuze("Een minimumprijs onder de evenwichtsprijs [[*verandert niets|veroorzaakt een tekort|veroorzaakt een overschot]].",
          "De bodem is niet bindend: de marktprijs ligt er al boven."),
    tabel("Beweging langs de curve of verschuiving van de curve?",
          [("De prijs van appels daalt, mensen kopen meer appels.", "langs de curve"), ("Appels worden plots heel populair door een tv-programma.", "verschuiving"), ("De boeren krijgen een goedkopere oogstmachine.", "verschuiving"), ("De prijs van appels stijgt, er worden meer appels aangeboden.", "langs de curve")],
          "Een prijsverandering is een beweging; iets anders verschuift de curve.",
          kolommen=["langs de curve", "verschuiving"]),
    keuze("Een homogeen product is bij elke aanbieder [[*hetzelfde|anders|duurder]].",
          "Tarwe van de ene boer is niet te onderscheiden van die van de andere."),
    open_("Leg uit wat er gebeurt als de prijs van zonnebrillen boven het evenwicht ligt.",
          "Er wordt meer aangeboden dan gevraagd, dus ontstaat er een overschot. De winkels verlagen hun prijs tot vraag en aanbod weer gelijk zijn.",
          "Een overschot duwt de prijs naar het evenwicht."),
]
