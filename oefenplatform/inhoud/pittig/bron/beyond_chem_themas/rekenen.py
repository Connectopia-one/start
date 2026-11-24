"""Chemisch rekenen: mol, molaire massa en concentratie — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Rekenschema rond de mol ---------------------------------------------------
RS = Prent("rekenschema-mol", "Rekenschema rond de stofhoeveelheid", "in het midden een vak 'mol (n)', errond vakken voor massa, aantal deeltjes, gasvolume en concentratie, verbonden met pijlen met de letters A tot F")
MID = (500, 330)
RS.rect(420, 290, 160, 80, "#f7d9b5", DONKER, 16, 3)
RS.tekst(500, 340, "mol (n)", 26, vet=True)
VAKKEN = {
    "massa (m, in g)": (170, 160),
    "aantal deeltjes (N)": (830, 160),
    "gasvolume (V, n.o.)": (170, 500),
    "oplossing: volume (V, in L)": (830, 500),
}
for t, (x, y) in VAKKEN.items():
    RS.rect(x - 130, y - 38, 260, 76, "#cfe5f3", DONKER, 16, 2)
    RS.tekst(x, y + 7, t, 19, vet=True)
# pijlen: telkens heen (naar mol) en terug
PIJLEN = {
    "A": ((305, 170), (440, 285)),   # massa -> mol
    "B": ((420, 315), (285, 200)),   # mol -> massa
    "C": ((580, 300), (710, 190)),   # mol -> deeltjes
    "D": ((290, 470), (420, 360)),   # gasvolume -> mol
    "E": ((580, 360), (710, 470)),   # mol -> volume oplossing (V = n/c)
}
for k, ((x1, y1), (x2, y2)) in PIJLEN.items():
    RS.pijl(x1, y1, x2, y2, DONKER, 3)
LP = {"A": (405, 195), "B": (320, 290), "C": (630, 220), "D": (330, 440), "E": (670, 440)}
for k, (x, y) in LP.items():
    RS.letter(x, y, k)
ZRS = {k: [Prent.rond(*LP[k], 24), Prent.zone(min(a[0], b[0]), min(a[1], b[1]), abs(a[0] - b[0]), abs(a[1] - b[1]))] for k, (a, b) in PIJLEN.items()}

# Vier oplossingen -----------------------------------------------------------
OP = Prent("vier-oplossingen", "Vier oplossingen van dezelfde stof", "vier bekerglazen met een etiket: hoeveel mol opgeloste stof in welk volume; letters P tot S")
GLAZEN = {"P": ("0,2 mol", "500 mL"), "Q": ("0,1 mol", "100 mL"), "R": ("0,5 mol", "2 L"), "S": ("0,3 mol", "1 L")}
for i, (k, (mol, vol)) in enumerate(GLAZEN.items()):
    x = 140 + i * 240
    OP.pad(f"M {x - 70} 200 L {x - 70} 430 Q {x - 70} 450 {x - 50} 450 L {x + 50} 450 Q {x + 70} 450 {x + 70} 430 L {x + 70} 200", "none", DONKER, 3)
    OP.rect(x - 68, 300, 136, 148, "#dcebf7", "none", 8, 0)
    OP.rect(x - 60, 330, 120, 74, "#ffffff", DONKER, 8, 2)
    OP.tekst(x, 362, mol, 20, vet=True)
    OP.tekst(x, 390, "in " + vol, 18)
    OP.letter(x, 530, k)
ZOP = {k: [Prent.zone(70 + i * 240, 200, 140, 250), Prent.rond(140 + i * 240, 530, 22)] for i, k in enumerate(GLAZEN)}

VRAGEN = [
    klik(
        "Klik op de pijl waar je deelt door de molaire massa.",
        RS.bestand, ZRS["A"],
        "Van massa naar mol: n = m / M.",
    ),
    klik(
        "Klik op de pijl waar je deelt door 22,4 L/mol.",
        RS.bestand, ZRS["D"],
        "Van gasvolume bij normomstandigheden naar mol.",
    ),
    met_prent(RS.bestand, tabel(
        "Wat doe je bij deze pijl?",
        [
            ("B", "× M"),
            ("C", "× 6,022·10²³"),
            ("E", ": c"),
        ],
        "Van mol naar massa vermenigvuldig je met M. Van mol naar volume oplossing deel je door de concentratie.",
        kolommen=["× M", "× 6,022·10²³", ": c"],
    )),
    klik(
        "Klik op de oplossing met de hoogste molaire concentratie.",
        OP.bestand, ZOP["Q"],
        "0,1 mol in 0,1 L is 1 mol/L. De andere zijn 0,4, 0,25 en 0,3 mol/L.",
    ),
    met_prent(OP.bestand, tabel(
        "Welke molaire concentratie heeft deze oplossing?",
        [
            ("P", "0,4 mol/L"),
            ("R", "0,25 mol/L"),
            ("S", "0,3 mol/L"),
        ],
        "c = n / V, met V in liter.",
        kolommen=["0,25 mol/L", "0,3 mol/L", "0,4 mol/L"],
    )),
    met_prent(OP.bestand, inv(
        "Je giet oplossing Q aan met water tot 250 mL. Wat is de nieuwe concentratie in mol/L?",
        ["0,4", "0.4", "0,4 mol/L"],
        "Er blijft 0,1 mol in 0,25 L: 0,4 mol/L.",
    )),
    inv(
        "Wat is de molaire massa van glucose, C₆H₁₂O₆? Gebruik C 12, H 1 en O 16 g/mol.",
        ["180", "180 g/mol"],
        "6 × 12 + 12 × 1 + 6 × 16 = 72 + 12 + 96 = 180.",
    ),
    inv(
        "Hoeveel mol is 90 gram glucose (M = 180 g/mol)?",
        ["0,5", "0.5", "0,5 mol"],
        "n = m / M = 90 / 180 = 0,5 mol.",
    ),
    inv(
        "Hoeveel liter neemt 0,5 mol zuurstofgas in bij normomstandigheden?",
        ["11,2", "11.2", "11,2 L"],
        "0,5 × 22,4 = 11,2 liter.",
    ),
    tabel(
        "Bevatten deze twee hoeveelheden evenveel moleculen?",
        [
            ("1 mol water en 1 mol koolstofdioxide", J),
            ("18 g water en 44 g koolstofdioxide", J),
            ("18 g water en 18 g koolstofdioxide", F),
            ("22,4 L stikstofgas en 22,4 L zuurstofgas, bij n.o.", J),
        ],
        "Evenveel mol betekent evenveel moleculen. Dezelfde massa betekent dat niet.",
    ),
    casus(
        "Je maakt 250 mL van een NaOH-oplossing van 0,2 mol/L. NaOH heeft een molaire massa van 40 g/mol.",
        [
            inv(
                "Hoeveel mol NaOH heb je nodig?",
                ["0,05", "0.05", "0,05 mol"],
                "n = c × V = 0,2 × 0,25 = 0,05 mol.",
            ),
            inv(
                "Hoeveel gram NaOH weeg je af?",
                ["2", "2 g", "2 gram"],
                "m = n × M = 0,05 × 40 = 2 g.",
            ),
            volgorde(
                "Zet de stappen bij het maken van de oplossing in de goede volgorde.",
                [
                    "De vaste stof afwegen",
                    "Oplossen in een beetje water in de maatkolf",
                    "Aanvullen met water tot de maatstreep",
                    "De kolf afsluiten en goed omschudden",
                ],
                "Pas aanvullen als de stof opgelost is, en daarna mengen.",
            ),
        ],
    ),
    mk(
        "Je verdunt 50 mL van een oplossing van 1 mol/L tot 200 mL. Wat is de nieuwe concentratie?",
        ["0,25 mol/L", "4 mol/L", "0,5 mol/L", "0,125 mol/L"],
        0,
        "c₂ = c₁ × V₁ / V₂ = 1 × 50 / 200 = 0,25 mol/L.",
    ),
    inv(
        "Hoeveel mL van een oplossing van 2 mol/L heb je nodig om 100 mL van 0,5 mol/L te maken?",
        ["25", "25 mL"],
        "V₁ = c₂ × V₂ / c₁ = 0,5 × 100 / 2 = 25 mL.",
    ),
    tabel(
        "Welke concentratie-uitdrukking is dit?",
        [
            ("mol opgeloste stof per liter oplossing", "molaire concentratie"),
            ("gram opgeloste stof per liter oplossing", "massaconcentratie"),
            ("gram opgeloste stof per 100 g oplossing", "massaprocent"),
            ("mL opgeloste stof per 100 mL oplossing", "volumeprocent"),
        ],
        "Kijk telkens naar wat er in de teller en de noemer staat.",
        kolommen=["molaire concentratie", "massaconcentratie", "massaprocent", "volumeprocent"],
    ),
    volgorde(
        "Zet deze verhoudingen van groot naar klein.",
        ["procent", "promille", "ppm", "ppb"],
        "Per honderd, per duizend, per miljoen, per miljard.",
    ),
    inv(
        "Hoeveel mL zuivere alcohol zit er in 500 mL wijn van 12 volumeprocent?",
        ["60", "60 mL"],
        "12 mL per 100 mL, dus 5 × 12 = 60 mL.",
    ),
    inv(
        "Een oplossing bevat 0,1 mol NaCl (58,5 g/mol) in 1 liter. Wat is de massaconcentratie in g/L?",
        ["5,85", "5.85", "5,85 g/L"],
        "0,1 × 58,5 = 5,85 g per liter.",
    ),
    mk(
        "Water bevat 2 mg lood per liter. Hoeveel ppm is dat ongeveer?",
        ["2 ppm", "2 ppb", "0,2 ppm", "2 promille"],
        0,
        "In water komt 1 mg per liter ongeveer overeen met 1 ppm.",
    ),
    tabel(
        "Klopt dit over één mol koolstofdioxide (44 g/mol)?",
        [
            ("Het weegt 44 gram.", J),
            ("Het bevat 6,022·10²³ moleculen.", J),
            ("Het bevat twee mol zuurstofatomen.", J),
            ("Het neemt bij elke temperatuur 22,4 L in.", F),
        ],
        "22,4 L geldt alleen bij normomstandigheden.",
    ),
    mk(
        "Een stof bestaat voor 40 % uit koolstof, 6,7 % uit waterstof en 53,3 % uit zuurstof. Waarom deel je eerst elk percentage door de atoommassa?",
        [
            "Zo krijg je de verhouding in mol",
            "Zo wordt de som precies honderd procent",
            "Zo weet je de massa van één molecule in gram",
            "Zo vind je de dichtheid van die stof",
        ],
        0,
        "Een formule geeft de verhouding in aantallen atomen, dus in mol.",
    ),
    inv(
        "Een metalen blokje weegt 54 g en heeft een volume van 20 cm³. Wat is de massadichtheid in g/cm³?",
        ["2,7", "2.7", "2,7 g/cm³"],
        "ρ = m / V = 54 / 20 = 2,7 g/cm³.",
    ),
    sleep(
        "Bij het verdunnen blijft het aantal [[mol]] opgeloste stof gelijk. Het [[volume]] wordt groter, dus de [[concentratie]] daalt.",
        ["massadichtheid", "molaire massa"],
        "Daarom geldt c₁ × V₁ = c₂ × V₂.",
    ),
    tabel(
        "Hoeveel mol atomen van dit element zit er in 1 mol Ca(OH)₂?",
        [
            ("Ca", "1"),
            ("O", "2"),
            ("H", "2"),
        ],
        "De index 2 na het haakje geldt voor O en H samen.",
        kolommen=["1", "2", "3"],
    ),
    inv(
        "Hoeveel massaprocent zuurstof zit er in water? Gebruik H 1 en O 16 g/mol. Rond af op een geheel getal.",
        ["89", "89 %", "89%"],
        "16 / 18 = 0,888... dus ongeveer 89 %.",
    ),
    koppel(
        "Koppel elke grootheid aan haar eenheid.",
        [
            ("stofhoeveelheid", "mol"),
            ("molaire massa", "g/mol"),
            ("molaire concentratie", "mol/L"),
            ("massadichtheid", "g/cm³"),
        ],
        ["mol/g"],
        "De eenheid vertelt je meteen welke formule je nodig hebt.",
    ),
    mk(
        "Hoeveel waterstofatomen zitten er in 0,5 mol methaan, CH₄?",
        ["1,2·10²⁴", "3,0·10²³", "6,0·10²³", "2,4·10²⁴"],
        0,
        "0,5 mol × 4 = 2 mol H-atomen, en 2 × 6,022·10²³ ≈ 1,2·10²⁴.",
    ),
    tabel(
        "Klopt dit over een oplossing van 10 massaprocent suiker?",
        [
            ("In 200 g oplossing zit 20 g suiker.", J),
            ("In 100 g oplossing zit 90 g water.", J),
            ("Je lost 10 g suiker op in 100 g water.", F),
        ],
        "Het procent gaat over de massa van de hele oplossing, niet over het water alleen.",
    ),
    open_(
        "Leg uit waarom 10 g waterstofgas (2 g/mol) veel meer moleculen bevat dan 10 g zuurstofgas (32 g/mol).",
        "Het aantal moleculen hangt af van het aantal mol, niet van de massa. Met n = m / M is 10 g waterstofgas 5 mol en 10 g zuurstofgas maar 0,3125 mol. Omdat een waterstofmolecule veel lichter is, heb je er voor dezelfde massa veel meer nodig, ongeveer zestien keer zoveel.",
    ),
]
