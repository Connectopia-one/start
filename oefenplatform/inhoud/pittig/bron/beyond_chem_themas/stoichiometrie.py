"""Stoichiometrie, overmaat en de algemene gaswet — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Deeltjesmodel: 2 H2 + O2 -> 2 H2O ----------------------------------------
DM = Prent("deeltjes-waterstof-zuurstof", "Een mengsel van waterstofgas en zuurstofgas, voor en na de reactie", "links een vak 'voor' met vier H₂- en drie O₂-moleculen, rechts drie vakken P, Q en R met mogelijke toestanden na de reactie")
HK = "#ffffff"
OK = "#e57373"


def _h2(p, x, y):
    p.cirkel(x - 9, y, 10, HK, DONKER, 2)
    p.cirkel(x + 9, y, 10, HK, DONKER, 2)


def _o2(p, x, y):
    p.cirkel(x - 12, y, 14, OK, DONKER, 2)
    p.cirkel(x + 12, y, 14, OK, DONKER, 2)


def _h2o(p, x, y):
    p.cirkel(x - 16, y + 12, 9, HK, DONKER, 2)
    p.cirkel(x + 16, y + 12, 9, HK, DONKER, 2)
    p.cirkel(x, y, 14, OK, DONKER, 2)


def _vak(p, x, y, titel):
    p.rect(x, y, 200, 260, "#fbfbf7", DONKER, 14, 2)
    p.tekst(x + 100, y - 12, titel, 18, vet=True)


_vak(DM, 30, 150, "voor")
for (x, y) in ((80, 200), (170, 230), (90, 300), (180, 330)):
    _h2(DM, x, y)
for (x, y) in ((130, 380), (75, 250), (175, 285)):
    _o2(DM, x, y)
DM.pijl(240, 280, 290, 280, DONKER, 3)
TOEST = {
    "P": {"h2o": 4, "o2": 1, "h2": 0},
    "Q": {"h2o": 2, "o2": 2, "h2": 2},
    "R": {"h2o": 4, "o2": 0, "h2": 0},
}
POS = [(60, 50), (140, 60), (60, 130), (140, 140), (60, 215), (140, 215)]
for i, (k, t) in enumerate(TOEST.items()):
    bx = 310 + i * 230
    _vak(DM, bx, 150, "na: " + k)
    j = 0
    for soort, n in t.items():
        for _ in range(n):
            x, y = POS[j]
            {"h2o": _h2o, "o2": _o2, "h2": _h2}[soort](DM, bx + x, 150 + y)
            j += 1
    DM.letter(bx + 100, 460, k)
DM.cirkel(560, 560, 10, HK, DONKER, 2)
DM.tekst(578, 566, "H", 16, "start")
DM.cirkel(640, 560, 13, OK, DONKER, 2)
DM.tekst(660, 566, "O", 16, "start")
ZDM = {k: [Prent.zone(310 + i * 230, 150, 200, 260), Prent.rond(410 + i * 230, 460, 22)] for i, k in enumerate(TOEST)}

# Gasvolume en temperatuur --------------------------------------------------
GV = Prent("gasvolume-temperatuur", "Volume van een hoeveelheid gas bij normale druk", "assenstelsel met de temperatuur in kelvin horizontaal en het volume in liter verticaal; een rechte door de oorsprong en vier punten A tot D")
X, Y = assen(GV, 0, 600, 0, 50, "T (K)", "V (L)", 100, 10, links=130, rechts=900)
GV.lijn(X(0), Y(0), X(600), Y(600 * 22.4 / 273), BLAUW, 3)
GV.tekst(X(380), Y(40), "1 mol gas", 17, kleur=BLAUW, vet=True)
PUNTEN = {"A": (273, 22.4), "B": (546, 44.8), "C": (273, 44.8), "D": (136.5, 11.2)}
for k, (t, v) in PUNTEN.items():
    GV.cirkel(X(t), Y(v), 7, ORANJE, DONKER, 2)
    GV.letter(X(t) + 32, Y(v) - 26, k)
ZGV = {k: [Prent.rond(X(t), Y(v), 22), Prent.rond(X(t) + 32, Y(v) - 26, 22)] for k, (t, v) in PUNTEN.items()}

VRAGEN = [
    klik(
        "Klik op de toestand na de reactie 2 H₂ + O₂ → 2 H₂O.",
        DM.bestand, ZDM["P"],
        "Vier H₂ hebben twee O₂ nodig: vier H₂O, en één O₂ blijft over.",
    ),
    met_prent(DM.bestand, tabel(
        "Wat is er met deze toestand aan de hand?",
        [
            ("P", "Klopt"),
            ("Q", "Reactie te vroeg gestopt"),
            ("R", "Er verdwijnen atomen"),
        ],
        "In Q zijn waterstofgas en zuurstofgas allebei nog niet op. In R ontbreken twee zuurstofatomen.",
        kolommen=["Klopt", "Reactie te vroeg gestopt", "Er verdwijnen atomen"],
    )),
    met_prent(DM.bestand, tabel(
        "Kijk naar het mengsel voor de reactie. Klopt dit?",
        [
            ("Waterstofgas is het limiterend reagens.", J),
            ("Zuurstofgas is in overmaat.", J),
            ("Er ontstaan evenveel watermoleculen als er H₂-moleculen waren.", J),
            ("Er reageren drie O₂-moleculen.", F),
        ],
        "4 / 2 = 2 voor H₂ en 3 / 1 = 3 voor O₂: H₂ is beperkend.",
    )),
    klik(
        "Klik op het punt dat 1 mol gas bij 546 K voorstelt.",
        GV.bestand, ZGV["B"],
        "Dubbele temperatuur in kelvin bij gelijke druk: dubbel volume, 44,8 L.",
    ),
    klik(
        "Klik op het punt dat geen 1 mol gas maar 2 mol gas voorstelt.",
        GV.bestand, ZGV["C"],
        "Bij 273 K neemt 1 mol 22,4 L in. 44,8 L bij dezelfde temperatuur is 2 mol.",
    ),
    met_prent(GV.bestand, tabel(
        "Welk punt hoort bij deze situatie, bij normale druk?",
        [
            ("1 mol gas bij 0 °C", "A"),
            ("1 mol gas bij −136,5 °C", "D"),
            ("1 mol gas bij 273 °C", "B"),
        ],
        "Reken eerst om naar kelvin: tel 273 op.",
        kolommen=["A", "B", "C", "D"],
    )),
    inv(
        "Welke coëfficiënt hoort voor O₂ in C₂H₆ + … O₂ → 2 CO₂ + 3 H₂O? Je mag een breuk of kommagetal geven.",
        ["3,5", "3.5", "7/2"],
        "Rechts 4 + 3 = 7 zuurstofatomen, dus 3,5 O₂. Met gehele getallen: 2 C₂H₆ + 7 O₂ → 4 CO₂ + 6 H₂O.",
    ),
    tabel(
        "Welke coëfficiënt hoort er voor deze stof in Fe₂O₃ + 3 CO → 2 Fe + 3 CO₂, als je alles met 2 vermenigvuldigt?",
        [
            ("Fe₂O₃", "2"),
            ("CO", "6"),
            ("Fe", "4"),
            ("CO₂", "6"),
        ],
        "Een vergelijking blijft kloppen als je alle coëfficiënten met hetzelfde getal vermenigvuldigt.",
        kolommen=["2", "4", "6"],
    ),
    mk(
        "Hoeveel gram water ontstaat er uit 4 g waterstofgas (2 g/mol) met genoeg zuurstofgas? M(H₂O) = 18 g/mol.",
        ["36 g", "18 g", "72 g", "22 g"],
        0,
        "4 g H₂ is 2 mol. 2 H₂ + O₂ → 2 H₂O geeft ook 2 mol water: 2 × 18 = 36 g.",
    ),
    casus(
        "Je laat 1 mol N₂ reageren met 6 mol H₂ volgens N₂ + 3 H₂ → 2 NH₃.",
        [
            keuze(
                "Het limiterend reagens is [[*stikstofgas|waterstofgas|ammoniak]].",
                "1 / 1 = 1 voor N₂ en 6 / 3 = 2 voor H₂: de kleinste uitkomst is beperkend.",
            ),
            inv(
                "Hoeveel mol ammoniak ontstaat er hoogstens?",
                ["2", "2 mol", "twee"],
                "1 mol N₂ geeft 2 mol NH₃.",
            ),
            inv(
                "Hoeveel mol waterstofgas blijft er over?",
                ["3", "3 mol", "drie"],
                "Er reageert 3 mol H₂, dus 6 − 3 = 3 mol blijft over.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van een berekening van massa naar massa in de goede volgorde.",
        [
            "De vergelijking uitbalanceren",
            "De gegeven massa omrekenen naar mol",
            "Met de coëfficiënten naar mol van de gevraagde stof",
            "Het aantal mol omrekenen naar gram",
        ],
        "Je rekent altijd via mol, want de coëfficiënten zijn molverhoudingen.",
    ),
    inv(
        "Hoeveel kelvin is −23 °C?",
        ["250", "250 K"],
        "−23 + 273 = 250 K.",
    ),
    mk(
        "Een gas in een afgesloten spuit heeft 2 L bij 300 K. Je verwarmt tot 450 K bij gelijke druk. Wat is het nieuwe volume?",
        ["3 L", "1,3 L", "2 L", "4,5 L"],
        0,
        "V is recht evenredig met T in kelvin: 2 × 450 / 300 = 3 L.",
    ),
    mk(
        "Je halveert het volume van een gas bij gelijke temperatuur. Wat gebeurt er met de druk?",
        ["Ze verdubbelt", "Ze halveert", "Ze blijft gelijk", "Ze wordt vier keer zo groot"],
        0,
        "p × V blijft gelijk als n en T gelijk blijven.",
    ),
    tabel(
        "Wat gebeurt er met het volume van een gas als je dit verandert en de rest gelijk blijft?",
        [
            ("de temperatuur in kelvin verdubbelen", "Groter"),
            ("de druk verdubbelen", "Kleiner"),
            ("het aantal mol verdubbelen", "Groter"),
        ],
        "V = n × R × T / p.",
        kolommen=["Groter", "Kleiner"],
    ),
    tabel(
        "Klopt dit over de reactie 4 Al + 3 O₂ → 2 Al₂O₃?",
        [
            ("4 mol aluminium reageert met 3 mol zuurstofgas.", J),
            ("2 mol aluminium geeft 1 mol aluminiumoxide.", J),
            ("4 g aluminium reageert met 3 g zuurstofgas.", F),
            ("Er staan links en rechts zes zuurstofatomen.", J),
        ],
        "De coëfficiënten zijn molverhoudingen, geen massaverhoudingen.",
    ),
    inv(
        "Hoeveel liter CO₂ (bij normomstandigheden) ontstaat er bij het verbranden van 0,5 mol methaan, CH₄ + 2 O₂ → CO₂ + 2 H₂O?",
        ["11,2", "11.2", "11,2 L"],
        "0,5 mol CH₄ geeft 0,5 mol CO₂: 0,5 × 22,4 = 11,2 L.",
    ),
    mk(
        "Je hebt 3 mol Mg en 1 mol O₂ voor 2 Mg + O₂ → 2 MgO. Wat is in overmaat?",
        ["Magnesium", "Zuurstofgas", "Geen van beide", "Magnesiumoxide"],
        0,
        "3 / 2 = 1,5 voor Mg en 1 / 1 = 1 voor O₂: zuurstofgas is beperkend, er blijft 1 mol Mg over.",
    ),
    koppel(
        "Koppel elke letter uit p × V = n × R × T aan de juiste eenheid.",
        [
            ("p", "pascal"),
            ("V", "kubieke meter"),
            ("n", "mol"),
            ("T", "kelvin"),
        ],
        ["graden Celsius"],
        "Temperatuur altijd in kelvin, nooit in graden Celsius.",
    ),
    sleep(
        "Bij normomstandigheden is de temperatuur [[0 °C]] en neemt één mol gas [[22,4 L]] in. Dat geldt voor [[elk]] gas.",
        ["25 °C", "24,5 L", "alleen zuurstof"],
        "Het molair volume hangt niet af van het soort gas, wel van druk en temperatuur.",
    ),
    tabel(
        "Hoeveel mol zuurstofgas heb je nodig voor de volledige verbranding?",
        [
            ("1 mol CH₄", "2"),
            ("1 mol C₃H₈", "5"),
            ("2 mol H₂", "1"),
        ],
        "Balanceer telkens eerst C en H, zuurstof het laatst.",
        kolommen=["1", "2", "5"],
    ),
    mk(
        "Waarom gebruikt men bij een verbranding in de industrie vaak een overmaat lucht?",
        [
            "Zo verbrandt de brandstof zo volledig mogelijk",
            "Zo ontstaat er meer koolstofdioxide dan mogelijk",
            "Lucht verlaagt de temperatuur tot onder 0 °C",
            "De coëfficiënten veranderen dan in ons voordeel",
        ],
        0,
        "De duurdere stof, de brandstof, moet volledig opgebruikt worden.",
    ),
    inv(
        "Hoeveel mol gas is 2,24 L bij normomstandigheden?",
        ["0,1", "0.1", "0,1 mol"],
        "2,24 / 22,4 = 0,1 mol.",
    ),
    inv(
        "Bij CaCO₃ → CaO + CO₂ ontleedt 50 g kalksteen (100 g/mol). Hoeveel gram CaO (56 g/mol) ontstaat er?",
        ["28", "28 g"],
        "50 g is 0,5 mol CaCO₃, dat geeft 0,5 mol CaO: 0,5 × 56 = 28 g.",
    ),
    tabel(
        "Mag je dit doen om een vergelijking uit te balanceren?",
        [
            ("een coëfficiënt voor een formule zetten", J),
            ("een index in een formule veranderen", F),
            ("alle coëfficiënten met hetzelfde getal vermenigvuldigen", J),
            ("een stof weglaten die niet past", F),
        ],
        "De formules staan vast. Je mag enkel de aantallen deeltjes aanpassen.",
    ),
    mk(
        "Hoeveel gram zuurstofgas (32 g/mol) is nodig om 1 mol propaan te verbranden, C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O?",
        ["160 g", "32 g", "96 g", "128 g"],
        0,
        "5 mol × 32 g/mol = 160 g.",
    ),
    keuze(
        "Bij een aflopende reactie stopt de reactie zodra het [[*limiterend reagens|reagens in overmaat|reactieproduct]] op is.",
        "Van de stof in overmaat blijft er na afloop iets over.",
    ),
    open_(
        "Leg uit waarom de stof waarvan je het minste mol hebt niet altijd het limiterend reagens is.",
        "Het hangt ook af van de coëfficiënten in de reactievergelijking. Je deelt het aantal mol van elke stof door haar coëfficiënt: de kleinste uitkomst is het limiterend reagens. Bij N₂ + 3 H₂ is 2 mol H₂ beperkend tegenover 1 mol N₂, omdat je per mol stikstof drie mol waterstof nodig hebt.",
    ),
]
