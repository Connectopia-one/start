"""Nut, preferentie en de indifferentiecurve — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen ec_nut, met een zelfgetekende indifferentiemap om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, ORANJE, GROEN, DONKER

IM = Prent("indifferentiemap", "Indifferentiemap", "drie bolle indifferentiecurven I1, I2, I3 met vijf punten A tot E")
OX, OY, S = 140, 560, 40   # oorsprong, schaal: 1 eenheid = 40 px
def P(x, y): return OX + x * S, OY - y * S
IM.lijn(OX, OY, OX + 760, OY, DONKER, 3); IM.lijn(OX, OY, OX, 40, DONKER, 3)
IM.tekst(OX + 760, OY + 34, "goed X (boeken)", 20, "end")
IM.tekst(OX - 10, 30, "goed Y (spellen)", 20, "start")
for k, kleur, naam in ((12, BLAUW, "I1"), (30, ORANJE, "I2"), (56, GROEN, "I3")):
    pts = []
    x = k / 12.0
    while x <= 17.5:
        pts.append(P(x, k / x)); x += 0.25
    d = "M " + " L ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    IM.pad(d, "none", kleur, 3)
    lx, ly = P(17.6, k / 17.6)
    IM.tekst(lx + 10, ly + 6, naam, 20, "start", kleur, True)
PUNTEN = {"A": (2, 6), "B": (6, 2), "C": (5, 6), "D": (7, 8), "E": (3, 10)}
for t, (x, y) in PUNTEN.items():
    px, py = P(x, y)
    IM.cirkel(px, py, 7, DONKER, DONKER, 1)
    IM.letter(px + 24, py - 22, t)
U = "indifferentiemap.svg"
Z = {t: Prent.zone(P(x, y)[0] - 22, P(x, y)[1] - 50, 75, 72) for t, (x, y) in PUNTEN.items()}

VRAGEN = [
    klik("Klik op het punt dat deze consument het meeste nut geeft.", U, [Z["D"]],
         "D ligt op I3, de curve het verst van de oorsprong."),
    klik("Klik op het punt dat de consument evenveel nut geeft als punt A.", U, [Z["B"]],
         "A en B liggen allebei op I1: de consument is indifferent tussen de twee."),
    klik("Klik op een punt dat de consument evenveel nut geeft als punt C.", U, [Z["E"]],
         "C (5 boeken, 6 spellen) en E (3 boeken, 10 spellen) liggen allebei op I2."),
    tabel("Klopt dit volgens de indifferentiemap?",
          [("De consument verkiest C boven A.", J), ("De consument is indifferent tussen A en B.", J), ("B geeft meer nut dan E.", F), ("Uit de map alleen weet je welke combinatie hij koopt.", F)],
          "Hoger in de map is meer nut; wat hij kan kopen hangt af van zijn budget."),
    casus("Lees de tabel.\n\nLotte eet op een kermis smoutebollen.\n1ste portie: grensnut 12\n2de portie: grensnut 8\n3de portie: grensnut 3\n4de portie: grensnut 0\n5de portie: grensnut −4", [
        inv("Hoe groot is het totale nut na drie porties? Schrijf enkel het getal.", ["23"],
            "12 + 8 + 3 = 23."),
        inv("Na hoeveel porties is het totale nut maximaal? Schrijf het kleinste aantal.", ["3", "drie"],
            "Na 3 porties is het totale nut 23; de vierde voegt 0 toe, dus het blijft 23. Het maximum is bereikt bij 3 (of 4) porties."),
        keuze("Na de vijfde portie [[*daalt|stijgt|blijft gelijk]] het totale nut.",
              "Een negatief grensnut verlaagt het totale nut."),
        keuze("Dat het grensnut daalt, heet de wet van het [[*afnemende grensnut|stijgende totaal nut|dalende totaal nut]].",
              "Elke extra eenheid levert minder extra nut."),
    ]),
    koppel("Welk begrip hoort bij welke omschrijving?",
           [("grensnut", "het nut van de laatste eenheid"), ("totaal nut", "het nut van alle eenheden samen"), ("preferentie", "de ene combinatie liever hebben"), ("indifferentie", "evenveel nut van twee combinaties")],
           ["alternatieve kost"], "De kernbegrippen van het thema."),
    tabel("Klopt dit over het grensnut?",
          [("Het grensnut kan negatief worden.", J), ("Een dalend grensnut betekent altijd een dalend totaal nut.", F), ("Is het grensnut nul, dan is het totale nut maximaal.", J), ("Het grensnut is voor iedereen hetzelfde.", F)],
          "Zolang het grensnut positief is, stijgt het totale nut, alleen trager."),
    mk("Waarom betaal je in de woestijn veel voor het eerste glas water?",
       ["Het grensnut van dat eerste glas is hoog.", "Het water is daar van betere kwaliteit.", "Het tiende glas heeft een hoger grensnut.", "Het totale nut is daar altijd nul."], 0,
       "Wat je wil betalen, hangt samen met het grensnut."),
    keuze("Een indifferentiecurve is [[*dalend en bol naar de oorsprong|stijgend en recht|horizontaal]].",
          "Minder van het ene moet je goedmaken met meer van het andere."),
    keuze("Twee indifferentiecurven van dezelfde consument kunnen elkaar [[*nooit snijden|soms snijden|altijd snijden]].",
          "Anders zou één punt twee nutsniveaus hebben."),
    keuze("Het geheel van alle indifferentiecurven van één consument heet een [[*indifferentiemap|budgetlijn|bedrijfskolom]].",
          "Elke curve is één nutsniveau."),
    mk("Wat stelt de helling van een indifferentiecurve voor?",
       ["hoeveel Y je opgeeft voor één X", "de prijs van goed X in euro", "het budget van de consument", "het totale nut van de consument"], 0,
       "Dat is de marginale substitutievoet."),
    keuze("Een consument heeft veel boeken en weinig spellen. Hij wil [[*veel boeken opgeven|bijna geen boeken opgeven]] voor één extra spel.",
          "Van wat je veel hebt, is het grensnut laag."),
    tabel("Is deze uitspraak over nut juist?",
          [("Nut is persoonlijk: hetzelfde goed kan voor twee mensen een ander nut hebben.", J), ("Nut kan je precies in euro meten.", F), ("De wet van het afnemende grensnut geldt ook voor geld.", J)],
          "Daarom rangschikt de theorie liever combinaties."),
    tabel("Preferentie of indifferentie?",
          [("Ik vind 2 pizza's en 1 film even goed als 1 pizza en 3 films.", "indifferentie"), ("Ik heb liever 3 frietjes dan 2 frietjes.", "preferentie"), ("Het maakt me niet uit: thee of koffie.", "indifferentie"), ("Ik kies de combinatie met meer van allebei.", "preferentie")],
          "Even goed = indifferent; liever = preferentie.",
          kolommen=["preferentie", "indifferentie"]),
    sleep("Op één indifferentiecurve blijft het [[nut]] gelijk. Een curve die verder van de [[oorsprong]] ligt, geeft [[meer]] nut.",
          ["prijs", "minder"], "Zo lees je een indifferentiemap."),
    inv("Een consument krijgt van allebei de goederen één eenheid meer. Komt hij op een hogere of een lagere indifferentiecurve? Schrijf één woord.", ["hogere", "hoger"],
        "Meer van allebei is meer nut."),
    keuze("Een indifferentiecurve wordt naar rechts toe [[*vlakker|steiler]].",
          "Hoe meer X je al hebt, hoe minder Y je ervoor wil opgeven."),
    keuze("Wie twee goederen altijd één op één wil ruilen, heeft indifferentiecurven die [[*bijna recht|heel bol|verticaal]] lopen.",
          "Een vaste ruilverhouding geeft een rechte."),
    mk("Welke veronderstelling maakt de theorie over de consument?",
       ["Hij wil zijn nut maximaliseren.", "Hij koopt altijd het duurste goed.", "Hij heeft een onbeperkt budget.", "Hij kent het nut niet van goederen."], 0,
       "Het is een model dat keuzes redelijk goed verklaart."),
    keuze("De theorie werkt met twee goederen, omdat die in een [[*vlak|lijn|tabel]] te tekenen zijn.",
          "Twee assen: goed X en goed Y."),
    klik("Klik op het punt dat het minste nut geeft van alle punten op de prent.", U, [Z["A"], Z["B"]],
         "A en B liggen op I1, de laagste curve. Allebei zijn juist."),
    tabel("Rangschik: welk punt geeft meer nut?",
          [("A of C", "C"), ("B of D", "D"), ("E of A", "E")],
          "Hoe verder van de oorsprong, hoe meer nut.",
          kolommen=["C", "D", "E"]),
    inv("Hoe noem je de verhouding waarin een consument twee goederen wil ruilen zonder dat zijn nut verandert? Schrijf drie woorden.", ["marginale substitutievoet", "de marginale substitutievoet"],
        "De helling van de indifferentiecurve."),
    keuze("Een vegetariër krijgt een steak. Voor hem is het nut ervan [[*laag|even hoog als voor een vleesliefhebber]].",
          "Nut is subjectief."),
    sorteer("Stijgt of daalt het totale nut bij deze extra eenheid?", ["stijgt", "daalt", "blijft gelijk"],
            [("grensnut +6", "stijgt"), ("grensnut −2", "daalt"), ("grensnut 0", "blijft gelijk"), ("grensnut +1", "stijgt")],
            "Het teken van het grensnut beslist."),
    open_("Leg met een eigen voorbeeld uit wat de wet van het afnemende grensnut betekent.",
          "Het eerste stuk chocolade smaakt heerlijk, het vijfde veel minder: elk extra stuk geeft minder extra nut.",
          "Elke extra eenheid van hetzelfde goed levert minder extra nut op."),
]
