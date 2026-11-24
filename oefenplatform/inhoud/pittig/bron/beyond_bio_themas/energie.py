"""Fotosynthese, celademhaling en gisting — pittig (🧬 Beyond doorstroom, biologie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Chloroplast en mitochondrion ------------------------------------------
CM = Prent("chloroplast-mitochondrion", "Een chloroplast (links) en een mitochondrion (rechts)", "links een chloroplast met stapels thylakoïden en stroma, rechts een mitochondrion met cristae en matrix; letters A tot F")
CM.ellips(250, 330, 210, 140, "#b9dc9c", DONKER, 3)
CM.ellips(250, 330, 198, 128, "#d6ecc2", DONKER, 1)
for cx in (130, 220, 310, 380):
    for j in range(5):
        CM.rect(cx - 30, 280 + j * 16, 60, 13, "#4f8a32", DONKER, 6, 1)
CM.lijn(160, 300, 190, 300, "#4f8a32", 4)
CM.lijn(250, 340, 280, 340, "#4f8a32", 4)
CM.ellips(730, 330, 220, 130, "#f2a66a", DONKER, 3)
CM.ellips(730, 330, 205, 116, "#fce1c8", DONKER, 1)
pad = "M530 330"
for i in range(9):
    x = 560 + i * 40
    pad += f" L {x} 330 L {x} {250 if i % 2 == 0 else 410} L {x + 20} {250 if i % 2 == 0 else 410} L {x + 20} 330"
CM.pad(pad + " L 930 330", "none", DONKER, 3)
LCM = {"A": (130, 230), "B": (250, 420), "C": (60, 200), "D": (720, 230), "E": (650, 370), "F": (940, 200)}
CM.lijn(75, 215, 95, 245, DONKER, 1)
CM.lijn(925, 215, 905, 240, DONKER, 1)
for k, (x, y) in LCM.items():
    CM.letter(x, y, k)
ZCM = {"A": [Prent.zone(95, 275, 320, 85), Prent.rond(*LCM["A"], 26)],
       "B": [Prent.zone(100, 380, 300, 60), Prent.rond(*LCM["B"], 26)],
       "D": [Prent.zone(560, 245, 340, 30), Prent.zone(560, 385, 340, 30), Prent.rond(*LCM["D"], 26)],
       "E": [Prent.zone(560, 290, 340, 60), Prent.rond(*LCM["E"], 26)]}

# Lichtcurve -------------------------------------------------------------
LC = Prent("lichtcurve-fotosynthese", "Zuurstofproductie van een waterplant bij toenemende lichtsterkte", "curve die stijgt en afvlakt; punten P, Q en R")
X, Y = assen(LC, 0, 100, -10, 50, "lichtsterkte", "netto zuurstof", 10, 10, links=150, rechts=900)
pts = [f"{X(l):.1f} {Y(-8 + 55 * (1 - math.exp(-l / 25))):.1f}" for l in range(0, 101)]
LC.pad("M" + " L ".join(pts), "none", GROEN, 4)
LC.lijn(X(0), Y(0), X(100), Y(0), DONKER, 2)
def lp(l):
    return X(l), Y(-8 + 55 * (1 - math.exp(-l / 25)))
LLC = {"P": lp(0), "Q": lp(4.5), "R": lp(95)}
OFF = {"P": (50, 10), "Q": (60, -40), "R": (0, -40)}
for k, (x, y) in LLC.items():
    LC.cirkel(x, y, 6, ORANJE, DONKER, 1)
    LC.letter(x + OFF[k][0], y + OFF[k][1], k)
ZLC = {k: [Prent.rond(x, y, 16), Prent.rond(x + OFF[k][0], y + OFF[k][1], 22)] for k, (x, y) in LLC.items()}

VRAGEN = [
    klik(
        "Klik op de plaats waar de lichtreacties gebeuren.",
        CM.bestand, ZCM["A"],
        "In het thylakoïdmembraan zitten de fotosystemen.",
    ),
    klik(
        "Klik op de plaats waar de Calvincyclus loopt.",
        CM.bestand, ZCM["B"],
        "In het stroma rond de thylakoïden.",
    ),
    klik(
        "Klik op de plaats waar de eindoxidaties gebeuren.",
        CM.bestand, ZCM["D"],
        "Op de cristae van het binnenmembraan.",
    ),
    met_prent(CM.bestand, tabel(
        "Kijk naar de twee organellen. Klopt dit?",
        [
            ("In E loopt de Krebscyclus.", J),
            ("C en F wijzen allebei naar een dubbel membraan.", J),
            ("In B ontstaat zuurstofgas.", F),
            ("Beide organellen hebben een protonengradiënt voor ATP.", J),
        ],
        "Zuurstof ontstaat bij de splitsing van water in de thylakoïden.",
    )),
    klik(
        "Klik op het punt waar fotosynthese en celademhaling elkaar in evenwicht houden.",
        LC.bestand, ZLC["Q"],
        "Netto zuurstof is daar nul: het compensatiepunt.",
    ),
    met_prent(LC.bestand, tabel(
        "Kijk naar de lichtcurve. Klopt dit?",
        [
            ("Bij P verbruikt de plant netto zuurstof.", J),
            ("Bij R is licht niet meer de beperkende factor.", J),
            ("Bij P doet de plant geen celademhaling.", F),
            ("Meer CO2 kan de curve bij R nog hoger brengen.", J),
        ],
        "In het donker ademt de plant gewoon verder.",
    )),
    tabel(
        "Lichtreacties of donkerreacties?",
        [
            ("water wordt gesplitst", "Lichtreacties"),
            ("CO2 wordt vastgelegd", "Donkerreacties"),
            ("ATP en NADPH worden gemaakt", "Lichtreacties"),
            ("ATP en NADPH worden verbruikt", "Donkerreacties"),
            ("in het thylakoïdmembraan", "Lichtreacties"),
        ],
        "De donkerreacties hebben geen licht nodig, wel de producten van de lichtreacties.",
        kolommen=["Lichtreacties", "Donkerreacties"],
    ),
    volgorde(
        "Zet de stappen van de aerobe celademhaling in volgorde.",
        ["Glycolyse", "Decarboxylatie van pyruvaat", "Krebscyclus", "Eindoxidaties"],
        "Enkel de glycolyse gebeurt buiten het mitochondrion.",
    ),
    tabel(
        "Waar gebeurt het?",
        [
            ("glycolyse", "cytoplasma"),
            ("Krebscyclus", "matrix"),
            ("eindoxidaties", "cristae"),
        ],
        "Van buiten naar binnen in de cel.",
        kolommen=["cytoplasma", "matrix", "cristae"],
    ),
    tabel(
        "Melkzuurgisting, alcoholische gisting of aerobe celademhaling?",
        [
            ("spiercel bij een sprint", "Melkzuurgisting"),
            ("gist in brooddeeg", "Alcoholische gisting"),
            ("levert de meeste ATP per glucose", "Aerobe celademhaling"),
            ("maakt ethanol", "Alcoholische gisting"),
        ],
        "Gisting levert enkel de winst van de glycolyse.",
        kolommen=["Melkzuurgisting", "Alcoholische gisting", "Aerobe celademhaling"],
    ),
    casus(
        "Een bakker laat deeg rijzen met gist. In een afgesloten kom gaat het deeg na een uur flink omhoog.",
        [
            keuze(
                "De gist doet aan [[*alcoholische gisting|melkzuurgisting|fotosynthese]].",
                "Zonder veel zuurstof.",
            ),
            keuze(
                "Het deeg rijst door het gas [[*koolstofdioxide|zuurstof|stikstof]].",
                "Het gas zit gevangen in het deeg.",
            ),
            tabel(
                "Klopt dit over het deeg?",
                [
                    ("Er ontstaat ook een beetje ethanol.", J),
                    ("Die verdampt bij het bakken.", J),
                    ("De gist maakt hier veel meer ATP dan met zuurstof.", F),
                ],
                "Gisting levert maar weinig ATP.",
            ),
        ],
    ),
    mk(
        "Waarom komt de zuurstof die een plant afgeeft uit water en niet uit CO2?",
        [
            "Water wordt gesplitst om elektronen te leveren",
            "CO2 bevat geen zuurstofatomen in zijn molecule",
            "Het zuurstof uit CO2 komt pas vrij in het donker",
            "Water neemt het zuurstof uit CO2 over in het stroma",
        ],
        0,
        "Fotosysteem II splitst water.",
    ),
    koppel(
        "Koppel elke stof aan haar rol.",
        [
            ("NADH", "vervoert elektronen naar de keten"),
            ("zuurstof", "laatste elektronenacceptor"),
            ("ATP", "werkmunt van de energie in de cel"),
            ("chlorofyl a", "vangt licht in het reactiecentrum"),
        ],
        ["slaat energie op voor weken"],
        "ATP is geen voorraad: het wordt meteen weer gebruikt.",
    ),
    sleep(
        "Chlorofyl neemt vooral [[rood]] en [[blauw]] licht op. [[Groen]] licht wordt weerkaatst, daarom zien bladeren groen.",
        ["geel", "infrarood"],
        "Carotenoïden vangen een deel van het andere licht.",
    ),
    tabel(
        "Klopt dit over een plant?",
        [
            ("Ze ademt dag en nacht.", J),
            ("In het licht maakt ze meer zuurstof dan ze verbruikt.", J),
            ("In het donker staan de lichtreacties stil.", J),
            ("Ze doet enkel fotosynthese.", F),
        ],
        "Ook plantencellen hebben mitochondria.",
    ),
    mk(
        "Waarom heeft een spiercel bij melkzuurgisting nog iets aan het omzetten van pyruvaat?",
        [
            "Zo komt NAD⁺ weer vrij voor de glycolyse",
            "Zo ontstaat er extra ATP uit het melkzuur zelf",
            "Zo wordt de spier minder zuur en minder moe",
            "Zo kan het mitochondrion zonder zuurstof verder",
        ],
        0,
        "Zonder NAD⁺ stopt de glycolyse.",
    ),
    tabel(
        "Klopt dit over de herfstkleuren?",
        [
            ("Het chlorofyl wordt afgebroken.", J),
            ("De carotenoïden waren er al.", J),
            ("De boom maakt in de herfst plots gele pigmenten aan.", F),
        ],
        "Het groen verdwijnt en het geel wordt zichtbaar.",
    ),
    keuze(
        "Een organisme dat zijn eigen voedsel maakt uit anorganische stoffen, is [[*autotroof|heterotroof|anaeroob]].",
        "Planten zijn het bekendste voorbeeld.",
    ),
    tabel(
        "Klopt dit over het ATP-synthase?",
        [
            ("Het zit in het thylakoïdmembraan en in het binnenmembraan van het mitochondrion.", J),
            ("Protonen die erdoor terugstromen, drijven het aan.", J),
            ("Het splitst water.", F),
        ],
        "Een protonengradiënt werkt als een stuwdam.",
    ),
    inv(
        "Bij de aerobe celademhaling worden per molecule glucose 6 moleculen CO2 gevormd. Hoeveel moleculen CO2 geven 5 moleculen glucose?",
        ["30"],
        "5 x 6 = 30.",
    ),
    tabel(
        "Wat neemt de fotosynthese op en wat geeft ze af?",
        [
            ("koolstofdioxide", "Neemt op"),
            ("water", "Neemt op"),
            ("zuurstof", "Geeft af"),
            ("glucose", "Geeft af"),
        ],
        "Bij de celademhaling is het net omgekeerd.",
        kolommen=["Neemt op", "Geeft af"],
    ),
    mk(
        "In een cel zonder zuurstof wordt toch nog wat ATP gemaakt. Welke stap loopt nog?",
        [
            "De glycolyse",
            "De Krebscyclus in de matrix",
            "De eindoxidaties op de cristae",
            "De Calvincyclus in het stroma",
        ],
        0,
        "Die heeft geen zuurstof nodig.",
    ),
    keuze(
        "Het vastleggen van CO2 in een organische molecule heet [[*koolstoffixatie|decarboxylatie|glycolyse]].",
        "Dat gebeurt in de Calvincyclus.",
    ),
    tabel(
        "Klopt dit over de eindoxidaties?",
        [
            ("Ze leveren de meeste ATP.", J),
            ("Er ontstaat water.", J),
            ("Ze hebben zuurstof nodig.", J),
            ("Ze gebeuren in het cytoplasma.", F),
        ],
        "Op de cristae van het mitochondrion.",
    ),
    tabel(
        "Klopt dit over de donkerreacties?",
        [
            ("Ze lopen ook in het licht.", J),
            ("Ze stoppen kort nadat het donker wordt.", J),
            ("Ze maken glucose uit CO2.", J),
            ("Ze kunnen alleen in het donker verlopen.", F),
        ],
        "Zonder ATP en NADPH uit de lichtreacties stoppen ze.",
    ),
    tabel(
        "Wat zie je in de reactievergelijking van de aerobe celademhaling?",
        [
            ("glucose", "Beginstof"),
            ("zuurstof", "Beginstof"),
            ("koolstofdioxide", "Eindproduct"),
            ("water", "Eindproduct"),
        ],
        "C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O.",
        kolommen=["Beginstof", "Eindproduct"],
    ),
    tabel(
        "Klopt dit over de glycolyse?",
        [
            ("Ze splitst glucose in twee pyruvaat.", J),
            ("Ze gebeurt in het cytoplasma.", J),
            ("Ze heeft geen zuurstof nodig.", J),
            ("Ze levert het grootste deel van de ATP.", F),
        ],
        "Het meeste ATP komt uit de eindoxidaties.",
    ),
    open_(
        "Leg uit waarom fotosynthese en celademhaling elkaars omgekeerde genoemd worden, en waarom dat toch niet helemaal klopt.",
        "Wat de fotosynthese opneemt (CO2 en water) geeft de celademhaling af, en omgekeerd voor glucose en zuurstof. Maar het zijn andere stappen, met andere enzymen, op andere plaatsen: de fotosynthese in de chloroplast met licht, de celademhaling in het cytoplasma en het mitochondrion.",
    ),
]
