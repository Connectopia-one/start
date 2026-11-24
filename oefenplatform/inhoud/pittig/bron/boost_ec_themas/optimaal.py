"""De optimale productiegrootte en winstmaximalisatie — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_optimaal, met zelfgetekende kostencurven en twee prijslijnen om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, GROEN, ROOD, PAARS, ORANJE, DONKER

def _mk(q): return 10 - 1.2 * q + 0.06 * q * q
def _gvk(q): return 10 - 0.6 * q + 0.02 * q * q
def _gk(q): return _gvk(q) + 400 / q
OP = Prent("optimum-prijzen", "MK, GK en GVK met twee marktprijzen", "kostencurven met prijslijnen van 30 en 8 euro en vijf punten A tot E")
OX, OY = 130, 570
def P(q, e): return OX + q * 21, OY - e * 11.5
OP.lijn(OX, OY, OX + 780, OY, DONKER, 3); OP.lijn(OX, OY, OX, 50, DONKER, 3)
for q in range(5, 40, 5):
    OP.lijn(P(q, 0)[0], OY, P(q, 0)[0], OY + 8, DONKER, 2); OP.tekst(P(q, 0)[0], OY + 28, str(q), 16)
for e in range(5, 45, 5):
    OP.lijn(OX - 8, P(0, e)[1], OX, P(0, e)[1], DONKER, 2); OP.tekst(OX - 14, P(0, e)[1] + 5, str(e), 15, "end")
OP.tekst(OX + 780, OY + 56, "hoeveelheid q", 18, "end"); OP.tekst(OX - 10, 42, "euro per stuk", 18, "start")
def curve(f, a, b, kleur):
    pts = []; q = a
    while q <= b + 1e-9:
        pts.append(P(q, f(q))); q += 0.25
    OP.pad("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts), "none", kleur, 3)
curve(_mk, 0.5, 34.5, ROOD); curve(_gk, 12, 36, BLAUW); curve(_gvk, 0.5, 36, GROEN)
OP.tekst(*[v + d for v, d in zip(P(34.5, _mk(34.5)), (12, 6))], "MK", 18, "start", ROOD, True)
OP.tekst(*[v + d for v, d in zip(P(36, _gk(36)), (8, 6))], "GK", 18, "start", BLAUW, True)
OP.tekst(*[v + d for v, d in zip(P(36, _gvk(36)), (8, 6))], "GVK", 18, "start", GROEN, True)
for prijs, naam in ((30, "prijs 1 = 30 euro"), (8, "prijs 2 = 8 euro")):
    OP.lijn(OX, P(0, prijs)[1], OX + 760, P(0, prijs)[1], PAARS, 2, True)
    OP.tekst(OX + 760, P(0, prijs)[1] - 8, naam, 16, "end", PAARS, True)
PT = {"A": (1.83, 8), "B": (18.17, 8), "C": (30.8, 30), "D": (27.9, _gk(27.9)), "E": (15, 5.5)}
OFF = {"A": (22, -26), "B": (24, -28), "C": (-30, -26), "D": (-4, 36), "E": (-30, 30)}
for t, (q, e) in PT.items():
    x, y = P(q, e); OP.cirkel(x, y, 7, DONKER, DONKER, 1); OP.letter(x + OFF[t][0], y + OFF[t][1], t)
U = "optimum-prijzen.svg"
Z = {t: Prent.rond(P(q, e)[0] + OFF[t][0], P(q, e)[1] + OFF[t][1], 32) for t, (q, e) in PT.items()}

VRAGEN = [
    klik("De marktprijs is 30 euro (prijs 1). Klik op de optimale productiegrootte.", U, [Z["C"]],
         "Het optimum ligt waar MK de prijslijn snijdt in het stijgende deel: MK = MO = 30."),
    klik("De marktprijs is 8 euro (prijs 2). Klik op de optimale productiegrootte.", U, [Z["B"]],
         "B ligt op het stijgende deel van MK. In A daalt MK nog: daar loont uitbreiden nog."),
    klik("Klik op het punt waar de prijs gelijk is aan de laagste gemiddelde kost: geen winst en geen verlies.", U, [Z["D"]],
         "In D snijdt MK de GK-curve in haar laagste punt, ongeveer 23 euro."),
    klik("Klik op het sluitingspunt.", U, [Z["E"]],
         "Het sluitingspunt is het laagste punt van GVK: daar snijdt MK de GVK."),
    tabel("Klopt dit volgens de grafiek met twee prijzen?",
          [("Bij prijs 1 maakt het bedrijf winst, want 30 ligt boven GK.", J), ("Bij prijs 2 maakt het bedrijf verlies, want 8 ligt onder GK.", J), ("Bij prijs 2 moet het bedrijf op korte termijn meteen sluiten.", F), ("A is geen optimum, ook al is daar MK = MO.", J)],
          "Prijs 2 ligt onder GK maar boven het laagste punt van GVK: op korte termijn nog produceren."),
    casus("Lees de tabel van een bedrijf bij volkomen concurrentie. De prijs is 15 euro.\n\nq: 10 · 11 · 12 · 13 · 14\nMK van dat stuk (euro): 9 · 11 · 14 · 15 · 19", [
        inv("Bij welke hoeveelheid ligt het optimum? Schrijf enkel het getal.", ["13"],
            "Bij 13 is MK = 15 = MO. Het 14de stuk kost 19 en brengt maar 15 op."),
        keuze("Het 12de stuk brengt [[*1 euro winst|1 euro verlies|niets]] op.",
              "MO 15 − MK 14 = 1 euro."),
        keuze("Het 14de stuk zou de winst met [[*4 euro doen dalen|4 euro doen stijgen|19 euro doen dalen]].",
              "MK 19 − MO 15 = 4 euro minder winst."),
    ]),
    sorteer("Wat doet het bedrijf met zijn productie?", ["uitbreiden", "inkrimpen", "zo laten"],
            [("MO 12, MK 9", "uitbreiden"), ("MO 12, MK 15", "inkrimpen"), ("MO 12, MK 12 (stijgend deel)", "zo laten"), ("MO 20, MK 14", "uitbreiden")],
            "Zolang een stuk meer opbrengt dan het kost, komt er winst bij."),
    inv("Een bedrijf heeft 6 000 euro constante kosten, verkoopt aan 25 euro en heeft 13 euro variabele kost per stuk. Hoeveel stuks moet het verkopen om break-even te draaien? Schrijf enkel het getal.", ["500"],
        "Dekkingsbijdrage 25 − 13 = 12; 6 000 / 12 = 500 stuks."),
    inv("Zelfde bedrijf: hoeveel winst maakt het bij 700 stuks? Schrijf enkel het getal.", ["2400", "2 400", "2.400"],
        "200 stuks boven break-even × 12 euro = 2 400 euro."),
    inv("Een bedrijf maakt 1 500 stuks. De prijs is 18 euro en GK is 14 euro. Hoe groot is de totale winst? Schrijf enkel het getal.", ["6000", "6 000", "6.000"],
        "(18 − 14) × 1 500 = 6 000 euro."),
    tabel("Wat doet het bedrijf op korte termijn?",
          [("prijs 12, GK 10, GVK 7", "produceren met winst"), ("prijs 9, GK 11, GVK 7", "produceren met verlies"), ("prijs 6, GK 11, GVK 7", "sluiten")],
          "Onder GK is er verlies; onder GVK sluit je beter.",
          kolommen=["produceren met winst", "produceren met verlies", "sluiten"]),
    keuze("De stijgende tak van de MK-curve is de [[*aanbodcurve|vraagcurve|budgetlijn]] van het bedrijf.",
          "Bij elke prijs produceert het bedrijf waar MK die prijs raakt."),
    keuze("Het verschil tussen de prijs en de variabele kost per stuk heet de [[*dekkingsbijdrage|marginale opbrengst|gemiddelde kost]].",
          "Ze dekt eerst de constante kosten, daarna is ze winst."),
    mk("Waarom kijkt een producent naar marginale grootheden?",
       ["Het gaat over dat ene extra stuk.", "Gemiddelden zijn moeilijker te rekenen.", "De marginale kost is altijd het laagst.", "De overheid verplicht dat bij de belasting."], 0,
       "Elke beslissing gaat over meer of minder produceren."),
    tabel("Klopt deze uitspraak over de optimale productiegrootte?",
          [("In het optimum is de totale opbrengst het hoogst.", F), ("MK = MO betekent niet altijd dat er winst is.", J), ("Alle bedrijven in een sector hebben hetzelfde optimum.", F), ("Wie te veel produceert, maakt minder winst.", J)],
          "Het optimum maximaliseert het verschil TO − TK; kosten verschillen per bedrijf."),
    keuze("De marktprijs stijgt van 10 naar 14 euro. Een bedrijf met stijgende MK [[*breidt zijn productie uit|krimpt zijn productie in|verandert niets]].",
          "Het produceert tot MK weer de nieuwe prijs raakt."),
    keuze("Er valt winst te halen bij volkomen concurrentie. Dan treden er nieuwe bedrijven toe en [[*zakt de prijs|stijgt de prijs|blijft de prijs gelijk]].",
          "Meer aanbod drukt de prijs."),
    sleep("Op het [[break-evenpunt]] is de winst nul. Zakt de prijs onder de laagste [[GVK]], dan sluit het bedrijf op korte termijn. Op lange termijn stopt het als de prijs onder de [[GK]] blijft.",
          ["MO", "optimum"], "Drie belangrijke drempels."),
    keuze("Een ijssalon draait 's winters verlies, maar dekt nog meer dan haar variabele kosten. Ze blijft best [[*open|dicht]].",
          "Zo dekt ze nog een deel van de huur."),
    tabel("Is dit een juiste stap om het optimum te vinden met een tabel van TO en TK?",
          [("TW = TO − TK uitrekenen per hoeveelheid", J), ("de hoeveelheid met de grootste TW kiezen", J), ("de hoeveelheid met de grootste TO kiezen", F)],
          "Je zoekt het grootste verschil, niet de grootste opbrengst."),
    inv("Een bedrijf verkoopt op een markt met volkomen concurrentie aan 22 euro. Bij welke marginale kost ligt zijn optimum? Schrijf enkel het getal.", ["22"],
        "Bij volkomen concurrentie is MO gelijk aan de prijs."),
    inv("In het optimum maakt een bedrijf 800 stuks. De prijs is 9 euro en TK is 6 000 euro. Hoe groot is de winst? Schrijf enkel het getal.", ["1200", "1 200", "1.200"],
        "TO = 800 × 9 = 7 200; TW = 7 200 − 6 000 = 1 200 euro."),
    keuze("Waarom telt alleen het snijpunt in het stijgende deel van MK? In het dalende deel [[*loont uitbreiden nog|is de winst al maximaal|is de prijs te laag]].",
          "Voorbij A worden de extra stuks nog goedkoper dan de prijs."),
    keuze("Een bedrijf verkoopt aan 10 euro. Zijn GVK is 8 euro en zijn GK 12 euro. Op korte termijn [[*blijft het produceren|sluit het meteen]].",
          "De variabele kosten zijn gedekt en er gaat nog 2 euro per stuk naar de constante kosten."),
    koppel("Welke voorwaarde hoort bij welk punt?",
           [("optimum", "MK = MO in het stijgende deel"), ("break-evenpunt", "TO = TK"), ("sluitingspunt", "prijs = laagste GVK"), ("kritisch punt", "prijs = laagste GK")],
           ["TO is maximaal"], "Vier punten die je moet kunnen onderscheiden."),
    tabel("Wat gebeurt er met de winst als het bedrijf één stuk extra maakt?",
          [("MO 7, MK 5", "stijgt"), ("MO 7, MK 9", "daalt"), ("MO 7, MK 7", "blijft gelijk")],
          "Vergelijk wat het stuk opbrengt met wat het kost.",
          kolommen=["stijgt", "daalt", "blijft gelijk"]),
    keuze("Een bedrijf verdubbelt zijn omzet. Zijn winst [[*hoeft niet te verdubbelen|verdubbelt altijd]].",
          "De kosten stijgen mee, en vanaf een punt zelfs sneller."),
    open_("Leg uit waarom een bedrijf met verlies op korte termijn soms toch blijft produceren.",
          "De constante kosten betaal je ook als je stopt. Zolang de prijs boven de GVK ligt, dekt elk stuk nog een deel van die constante kosten, dus is het verlies kleiner dan bij stoppen.",
          "Stoppen bespaart enkel de variabele kosten."),
]
