"""De kosten- en de opbrengstencurven — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_kosten, met zelfgetekende kostencurven om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, GROEN, ROOD, PAARS, DONKER

# TCK = 400; GVK = 10 − 0,6q + 0,02q²; MK = 10 − 1,2q + 0,06q²; GK = GVK + 400/q
def _mk(q): return 10 - 1.2 * q + 0.06 * q * q
def _gvk(q): return 10 - 0.6 * q + 0.02 * q * q
def _gck(q): return 400 / q
def _gk(q): return _gvk(q) + _gck(q)
KC = Prent("kostencurven", "Kostencurven per stuk", "MK, GK, GVK en GCK van een bedrijf, met vier curven met een letter en een punt M")
OX, OY = 130, 570
def P(q, e): return OX + q * 21, OY - e * 11.5
KC.lijn(OX, OY, OX + 780, OY, DONKER, 3); KC.lijn(OX, OY, OX, 50, DONKER, 3)
for q in range(5, 40, 5):
    KC.lijn(P(q, 0)[0], OY, P(q, 0)[0], OY + 8, DONKER, 2); KC.tekst(P(q, 0)[0], OY + 28, str(q), 16)
for e in range(5, 45, 5):
    KC.lijn(OX - 8, P(0, e)[1], OX, P(0, e)[1], DONKER, 2); KC.tekst(OX - 14, P(0, e)[1] + 5, str(e), 15, "end")
KC.tekst(OX + 780, OY + 56, "hoeveelheid q", 18, "end"); KC.tekst(OX - 10, 42, "euro per stuk", 18, "start")
def curve(f, a, b, kleur):
    pts = []; q = a
    while q <= b + 1e-9:
        pts.append(P(q, f(q))); q += 0.25
    KC.pad("M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts), "none", kleur, 3)
curve(_mk, 3, 34.5, ROOD); curve(_gk, 12, 36, BLAUW); curve(_gvk, 1, 36, GROEN); curve(_gck, 10, 36, ORANJE)
LAB = {"A": P(34.5, _mk(34.5)), "B": P(36, _gk(36)), "C": P(5, _gvk(5)), "D": P(11, _gck(11))}
for t, (x, y) in LAB.items():
    dx = 28 if t != "D" else -30
    KC.letter(x + dx, y - (6 if t != "C" else 40), t)
qm = 27.9
MX, MY = P(qm, _gk(qm)); KC.cirkel(MX, MY, 8, DONKER, DONKER, 1); KC.tekst(MX - 4, MY + 34, "M", 20, vet=True)
U = "kostencurven.svg"
Z = {t: Prent.rond(x + (28 if t != "D" else -30), y - (6 if t != "C" else 40), 34) for t, (x, y) in LAB.items()}
ZM = Prent.rond(MX, MY + 10, 36)

VRAGEN = [
    klik("Klik op de letter bij de curve van de gemiddelde constante kost GCK.", U, [Z["D"]],
         "GCK daalt voortdurend: dezelfde 400 euro wordt over steeds meer stuks verdeeld."),
    klik("Klik op de letter bij de marginale kost MK.", U, [Z["A"]],
         "MK daalt eerst, stijgt dan steil en snijdt GVK en GK in hun laagste punt."),
    klik("Klik op de letter bij de gemiddelde kost GK.", U, [Z["B"]],
         "GK is de u-vormige curve die het hoogst ligt: GVK plus GCK."),
    tabel("Klopt dit volgens de kostencurven?",
          [("In punt M is de gemiddelde kost het laagst.", J), ("Links van M ligt MK onder GK, en daar daalt GK.", J), ("Rechts van M ligt MK boven GK, en daar daalt GK.", F), ("Het verschil tussen GK en GVK is GCK.", J)],
          "Ligt MK onder het gemiddelde, dan trekt het het gemiddelde omlaag; erboven trekt het omhoog."),
    casus("Lees de gegevens van een bakkerij.\n\nDe huur is 1 800 euro per maand, de verzekering 200 euro. Per brood kosten de grondstoffen en de energie samen 0,90 euro. De bakkerij verkoopt haar brood aan 2,50 euro. Deze maand bakt ze 2 000 broden.", [
        inv("Hoe groot zijn de totale constante kosten TCK, in euro? Schrijf enkel het getal.", ["2000", "2 000", "2.000"],
            "1 800 + 200 = 2 000 euro."),
        inv("Hoe groot zijn de totale kosten TK bij 2 000 broden, in euro? Schrijf enkel het getal.", ["3800", "3 800", "3.800"],
            "2 000 + 2 000 × 0,90 = 2 000 + 1 800 = 3 800 euro."),
        inv("Hoe groot is de gemiddelde kost GK per brood, in euro? Schrijf het getal met een komma.", ["1,90", "1,9", "1.90", "1.9"],
            "3 800 / 2 000 = 1,90 euro."),
        inv("Hoe groot is de totale winst, in euro? Schrijf enkel het getal.", ["1200", "1 200", "1.200"],
            "TO = 2 000 × 2,50 = 5 000; TW = 5 000 − 3 800 = 1 200 euro."),
        keuze("Bakt de bakkerij volgende maand 4 000 broden, dan [[*daalt|stijgt|blijft]] de gemiddelde constante kost.",
              "2 000 euro over 4 000 broden is 0,50 per brood in plaats van 1 euro."),
    ]),
    sorteer("Constante of variabele kost voor een fietsenfabriek?", ["constant", "variabel"],
            [("de huur van de hal", "constant"), ("het staal per fiets", "variabel"), ("de verzekering van het gebouw", "constant"), ("de banden per fiets", "variabel"), ("de afschrijving van de machines", "constant"), ("de verpakking per fiets", "variabel")],
            "Constante kosten veranderen niet met de hoeveelheid."),
    koppel("Welke formule hoort bij welke afkorting?",
           [("TK", "TCK + TVK"), ("GK", "TK / q"), ("TO", "p × q"), ("TW", "TO − TK"), ("GVK", "TVK / q")],
           ["TK × q"], "De afkortingen van het thema."),
    inv("TK bij 200 stuks is 3 000 euro, bij 201 stuks 3 012 euro. Hoe groot is MK van het 201ste stuk? Schrijf enkel het getal.", ["12"],
        "3 012 − 3 000 = 12 euro."),
    inv("Een bedrijf verkoopt 300 stuks aan 12 euro. Hoe groot is TO? Schrijf enkel het getal.", ["3600", "3 600", "3.600"],
        "300 × 12 = 3 600 euro."),
    inv("Een bedrijf verkoopt 400 stuks aan 15 euro. TCK is 2 500 euro en de variabele kost is 9 euro per stuk. Hoe groot is de winst? Schrijf enkel het getal.", ["-100", "−100", "- 100"],
        "TO = 6 000; TK = 2 500 + 3 600 = 6 100; TW = −100: een verlies van 100 euro."),
    tabel("Wat geldt bij volkomen concurrentie?",
          [("GO is gelijk aan de prijs.", J), ("MO is gelijk aan de prijs.", J), ("Wie meer wil verkopen, moet zijn prijs verlagen.", F), ("TO is een stijgende rechte door de oorsprong.", J)],
          "Het bedrijf is prijsnemer: elk stuk brengt evenveel op."),
    mk("Hoe ziet de MO-curve eruit bij volkomen concurrentie?",
       ["horizontaal op de prijs", "dalend van links naar rechts", "stijgend door de oorsprong", "als een u-vormige curve"], 0,
       "De prijs ligt vast, dus elk extra stuk brengt hetzelfde op."),
    keuze("Zolang MK onder GK ligt, [[*daalt|stijgt]] GK.",
          "Een goedkoper extra stuk trekt het gemiddelde omlaag."),
    keuze("De curve van de gemiddelde kost heeft meestal een [[*u-vorm|rechte vorm|dalende vorm]].",
          "Eerst wordt de vaste kost verdeeld, daarna wegen de afnemende meeropbrengsten door."),
    keuze("MK stijgt vanaf een bepaald punt, omdat de [[*meeropbrengsten afnemen|constante kosten stijgen|prijs daalt]].",
          "De kostencurve is het spiegelbeeld van de productiefunctie."),
    keuze("Een bedrijf maakt verlies als de prijs [[*onder de gemiddelde kost ligt|boven de gemiddelde kost ligt|gelijk is aan de marginale opbrengst]].",
          "Dan verlies je op elk stuk."),
    tabel("Winst, verlies of break-even?",
          [("prijs 10 euro, GK 8 euro", "winst"), ("prijs 6 euro, GK 7 euro", "verlies"), ("prijs 9 euro, GK 9 euro", "break-even")],
          "Vergelijk de prijs met de gemiddelde kost.",
          kolommen=["winst", "verlies", "break-even"]),
    tabel("Hangt de marginale kost hiervan af?",
          [("de grondstoffen per stuk", J), ("de huur van het gebouw", F), ("de energie per stuk", J)],
          "MK hangt alleen af van de variabele kosten."),
    sleep("De gemiddelde kost is de [[totale kosten]] gedeeld door de [[hoeveelheid]]. De marginale kost is de stijging van de totale kosten bij [[één stuk]] meer.",
          ["prijs", "winst"], "Twee kosten per stuk die je niet mag verwarren."),
    keuze("Een landbouwer verkoopt graan op de wereldmarkt aan 0,25 euro per kilo. Zijn MO voor de laatste kilo is [[*0,25 euro|lager dan 0,25 euro|hoger dan 0,25 euro]].",
          "Hij is prijsnemer."),
    klik("Klik op het punt waar de kostprijs per stuk het laagst is.", U, [ZM],
         "In M bereikt GK haar laagste punt; daar snijdt MK de GK-curve."),
    klik("Klik op de letter bij de gemiddelde variabele kost GVK.", U, [Z["C"]],
         "GVK ligt onder GK; het verschil is GCK. MK snijdt GVK in haar laagste punt."),
    inv("Een bedrijf heeft 6 000 euro totale kosten bij 1 500 stuks. Hoe groot is de gemiddelde kost per stuk? Schrijf enkel het getal.", ["4"],
        "6 000 / 1 500 = 4 euro."),
    keuze("Een fabriek ligt een maand stil. Ze betaalt dan nog wel haar [[*constante kosten|variabele kosten|marginale kosten]].",
          "Huur en verzekering lopen door."),
    tabel("Gemiddelde constante kost: TCK is 3 000 euro. Hoe groot is GCK?",
          [("bij 100 stuks", "30"), ("bij 300 stuks", "10"), ("bij 600 stuks", "5")],
          "Dezelfde 3 000 euro over meer stuks.",
          kolommen=["5", "10", "30"]),
    open_("Leg uit waarom het belangrijk is om constante en variabele kosten uit elkaar te houden.",
          "Alleen de variabele kosten veranderen als je meer of minder produceert; de constante kosten betaal je toch. Dat speelt mee bij de beslissing om meer te maken.",
          "Bij beslissingen over de hoeveelheid tellen vooral de variabele kosten."),
]
