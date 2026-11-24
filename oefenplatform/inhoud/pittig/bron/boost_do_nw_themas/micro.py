"""Biodiversiteit en micro-organismen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Groeicurve van een bacteriekweek ---------------------------------------
GROEI = Prent("groeicurve-bacterien", "Aantal bacteriën in een kweek", "groeicurve met aanloopfase, snelle groei, stilstand en afname")
GROEI.lijn(110, 560, 930, 560, DONKER, 2)
GROEI.lijn(110, 560, 110, 80, DONKER, 2)
GROEI.tekst(102, 70, "aantal levende bacteriën", 16, "start")
GROEI.tekst(925, 595, "tijd", 16, "end")
GROEI.pad("M110 500 L 260 492 C 300 480, 330 440, 350 410 L 520 160 C 540 135, 560 130, 600 128 L 740 130 C 780 140, 820 200, 900 300", "none", BLAUW, 4)
for x in (260, 530, 740):
    GROEI.lijn(x, 90, x, 560, "#bbbbbb", 1, True)
Z_AANLOOP = Prent.zone(110, 440, 150, 110)
Z_SNEL = Prent.zone(300, 140, 220, 330)
Z_STIL = Prent.zone(540, 95, 200, 90)
Z_AFNAME = Prent.zone(745, 120, 180, 220)

# Drie micro-organismen ---------------------------------------------------
DRIE = Prent("drie-micro-organismen", "Drie micro-organismen, niet op schaal", "bacterie met celwand zonder kern, virus met eiwitmantel, gistcel met kern en knop")
# A: bacterie
DRIE.rect(90, 230, 220, 120, "#d9ecc8", DONKER, 60, 5)
DRIE.rect(102, 242, 196, 96, "#eef6e6", DONKER, 48, 1)
DRIE.pad("M140 290 C 170 260, 200 320, 230 285 S 270 300, 260 280", "none", PAARS, 3)
DRIE.lijn(310, 290, 360, 270, DONKER, 2)
# B: virus
import math
pts = " ".join(f"{500 + 70 * math.cos(math.radians(a)):.1f},{290 + 70 * math.sin(math.radians(a)):.1f}" for a in range(0, 360, 60))
DRIE.svg(f'<polygon points="{pts}" fill="#f7e2b0" stroke="{DONKER}" stroke-width="4"/>')
DRIE.pad("M470 290 C 485 260, 505 320, 520 285 S 535 300, 530 280", "none", PAARS, 3)
for a in range(0, 360, 60):
    x, y = 500 + 70 * math.cos(math.radians(a)), 290 + 70 * math.sin(math.radians(a))
    DRIE.lijn(x, y, x + 20 * math.cos(math.radians(a)), y + 20 * math.sin(math.radians(a)), DONKER, 3)
# C: gistcel met knop
DRIE.ellips(780, 300, 90, 70, "#fbe7c6", DONKER, 3)
DRIE.ellips(880, 240, 36, 30, "#fbe7c6", DONKER, 3)
DRIE.cirkel(770, 305, 26, "#e7c3d6", PAARS, 3)
DRIE.ellips(820, 330, 18, 12, "#cfe3f0", BLAUW, 2)
for i, x in enumerate((200, 500, 800)):
    DRIE.letter(x, 460, "ABC"[i])
Z_A = Prent.zone(70, 200, 300, 290)
Z_B = Prent.zone(400, 190, 200, 300)
Z_C = Prent.zone(680, 190, 250, 300)
Z_KNOP = Prent.rond(880, 240, 42)

VRAGEN = [
    klik(
        "Klik op het micro-organisme dat geen cel is.",
        DRIE.bestand, [Z_B],
        "Een virus is erfelijk materiaal in een eiwitmantel, zonder celmembraan of organellen.",
    ),
    klik(
        "Klik op het micro-organisme zonder kernmembraan, met een stevige celwand.",
        DRIE.bestand, [Z_A],
        "Een bacterie is prokaryoot: het erfelijk materiaal ligt vrij in de cel.",
    ),
    klik(
        "Klik op het eukaryote micro-organisme.",
        DRIE.bestand, [Z_C],
        "Een gistcel heeft een echte kern met kernmembraan, net als alle schimmels.",
    ),
    klik(
        "Klik op het deel dat toont hoe deze gist zich vermeerdert.",
        DRIE.bestand, [Z_KNOP],
        "Bij knopvorming groeit een kleine dochtercel uit de moedercel en snoert zich af.",
    ),
    klik(
        "Klik op het deel van de curve waar de bacteriën het snelst vermeerderen.",
        GROEI.bestand, [Z_SNEL],
        "Na de aanloopfase volgt een fase van snelle groei door celsplitsing.",
    ),
    klik(
        "Klik op de fase waarin de bacteriën zich nog aanpassen en het aantal amper stijgt.",
        GROEI.bestand, [Z_AANLOOP],
        "Een kweek groeit niet meteen snel: eerst is er een aanloopfase.",
    ),
    klik(
        "Klik op de fase waarin er evenveel bacteriën bijkomen als er sterven.",
        GROEI.bestand, [Z_STIL],
        "In de stilstand blijft het aantal gelijk.",
    ),
    met_prent(GROEI.bestand, tabel(
        "Kijk naar de curve. Klopt dit?",
        [
            ("Een kweek groeit niet van begin tot eind even snel.", J),
            ("Op het einde daalt het aantal levende bacteriën.", J),
            ("Het aantal blijft stijgen zolang de kweek bestaat.", F),
            ("Er zijn vier fasen te zien.", J),
        ],
        "Een kweek doorloopt een aanloopfase, snelle groei, stilstand en afname.",
    )),
    tabel(
        "Prokaryoot, eukaryoot of geen van beide?",
        [
            ("een bacterie", "Prokaryoot"),
            ("een archaea", "Prokaryoot"),
            ("een schimmel", "Eukaryoot"),
            ("een gistcel", "Eukaryoot"),
            ("een virus", "Geen van beide"),
        ],
        "Een virus is geen cel en staat niet in de tree of life.",
        kolommen=["Prokaryoot", "Eukaryoot", "Geen van beide"],
    ),
    tabel(
        "Klopt dit over de indeling van het leven?",
        [
            ("Het driedomeinensysteem kent archaea, bacteriën en eukaryoten.", J),
            ("Het vijfrijkensysteem heeft een eigen rijk voor virussen.", F),
            ("Schimmels vormen een eigen rijk.", J),
            ("Een indeling toont hoe soorten verwant zijn.", J),
            ("Protisten zijn prokaryoot.", F),
        ],
        "De vijf rijken zijn planten, dieren, schimmels, prokaryoten en protisten.",
    ),
    koppel(
        "Koppel elk organisme aan zijn manier van vermeerderen.",
        [
            ("bacterie", "celsplitsing in twee gelijke cellen"),
            ("gist", "knopvorming"),
            ("virus", "een gastheercel laten bouwen"),
        ],
        ["bevruchting van een eicel"],
        "Micro-organismen vermeerderen zich ongeslachtelijk. Een virus heeft altijd een gastheercel nodig.",
    ),
    casus(
        "Senne heeft griep en koorts. Hij vraagt de dokter om antibiotica, want 'die hielpen vorig jaar ook bij zijn keelontsteking door bacteriën'.",
        [
            mk(
                "Waarom schrijft de dokter geen antibioticum voor?",
                [
                    "Griep komt door een virus",
                    "Senne is te jong voor een antibioticum",
                    "Een antibioticum werkt enkel tegen schimmels",
                    "Koorts maakt het antibioticum onwerkzaam",
                ],
                0,
                "Antibiotica grijpen aan op bacteriën, bijvoorbeeld op hun celwand. Een virus heeft die niet.",
            ),
            tabel(
                "Klopt dit over antibiotica en vaccins?",
                [
                    ("Slordig gebruik van antibiotica bevordert resistentie.", J),
                    ("Resistente bacteriën die overleven, vermenigvuldigen zich verder.", J),
                    ("Een vaccin tegen griep laat het afweersysteem oefenen.", J),
                    ("Tegen een schimmelinfectie neem je een antibioticum.", F),
                ],
                "Tegen schimmels gebruik je een antimycoticum.",
            ),
        ],
    ),
    tabel(
        "Welk micro-organisme speelt hier een rol?",
        [
            ("brood dat rijst", "Gist"),
            ("yoghurt", "Bacterie"),
            ("schimmelkaas", "Schimmel"),
            ("zuurkool", "Bacterie"),
            ("bier brouwen", "Gist"),
        ],
        "Melkzuurbacteriën maken yoghurt en zuurkool, gist laat brood rijzen en brouwt bier.",
        kolommen=["Gist", "Bacterie", "Schimmel"],
    ),
    koppel(
        "Koppel elke bewaringstechniek aan de groeivoorwaarde die ze wegneemt of de manier waarop ze werkt.",
        [
            ("drogen", "geen vocht meer"),
            ("pasteuriseren", "kort verhitten, de meeste sterven"),
            ("inmaken in zuur", "te lage zuurtegraad om te groeien"),
            ("inmaken in zout", "te hoog zoutgehalte om te groeien"),
        ],
        ["meer voedsel toevoegen"],
        "Bacteriën groeien met voedsel, vocht en een geschikte temperatuur. Bewaren haalt een voorwaarde weg.",
    ),
    mk(
        "Wat is het verschil tussen pasteuriseren en steriliseren?",
        [
            "Steriliseren doodt ook de sporen",
            "Pasteuriseren doodt ook alle sporen",
            "Steriliseren gebeurt zonder verhitting",
            "Pasteuriseren maakt een product droog",
        ],
        0,
        "Pasteuriseren doodt niet alles, het verlengt de houdbaarheid.",
    ),
    casus(
        "Naast een akker loopt een beek. Na een zware regenbui spoelt er veel mest in het water. Een paar weken later is het water groen van de algen, en daarna drijven er dode vissen.",
        [
            volgorde(
                "Zet de gebeurtenissen in de beek in de juiste volgorde.",
                [
                    "Er komen veel voedingsstoffen in het water",
                    "Algen bloeien op",
                    "Algen sterven massaal af",
                    "Afbrekende bacteriën verbruiken veel zuurstof",
                    "Vissen stikken",
                ],
                "Dat proces heet eutrofiëring.",
            ),
            keuze(
                "Zolang de vuilvracht klein blijft, maakt de beek zichzelf schoon dankzij [[*bacteriën die het afval afbreken|de stroming van het water|de algen die zuurstof opslaan]].",
                "Dat is de zelfzuiverende capaciteit van een waterloop.",
            ),
        ],
    ),
    sorteer(
        "Is dit een goede of een slechte kant van micro-organismen voor ons?",
        ["Goed", "Slecht"],
        [
            ["afval afbreken bij het composteren", "Goed"],
            ["water zuiveren in een installatie", "Goed"],
            ["vitamines maken in de darm", "Goed"],
            ["voedsel laten bederven", "Slecht"],
            ["een infectie veroorzaken", "Slecht"],
        ],
        "Micro-organismen zijn onmisbaar, ook al veroorzaken sommige ziekte of bederf.",
    ),
    tabel(
        "Klopt dit over het microbioom?",
        [
            ("Het darmmicrobioom helpt bij de vertering.", J),
            ("Het huidmicrobioom houdt ziekteverwekkers mee op afstand.", J),
            ("Probiotica zijn levende micro-organismen.", J),
            ("Prebiotica zijn bacteriën die je inneemt.", F),
            ("Het microbioom moet je zo veel mogelijk wegwassen.", F),
        ],
        "Prebiotica zijn voedingsstoffen die de goede bacteriën helpen groeien.",
    ),
    sleep(
        "Een organisme dat zelf zijn energierijke stoffen maakt, is [[autotroof]]. Een organisme dat zonder zuurstofgas kan leven, is [[anaëroob]]. Gist die suikers zonder zuurstofgas omzet in alcohol, doet aan [[gisting]].",
        ["heterotroof", "aëroob", "fotosynthese"],
        "Een heterotroof leeft van andere organismen.",
    ),
    mk(
        "Waarom vormt een bacterie soms een spore?",
        [
            "Om slechte omstandigheden te overleven",
            "Om zich daarna sneller te kunnen vermeerderen",
            "Om zo een gastheercel binnen te dringen",
            "Om zuurstofgas te maken voor anderen",
        ],
        0,
        "Een spore is een rustvorm met een harde wand.",
    ),
    mk(
        "Hoe maakt een virus nieuwe virusdeeltjes?",
        [
            "De gastheercel zet ze in elkaar",
            "Het virus deelt zich door celsplitsing",
            "Het virus vormt een knop die loskomt",
            "Het virus maakt ze in zijn eigen kern",
        ],
        0,
        "Een virus sluist zijn erfelijk materiaal binnen en laat de cel het werk doen.",
    ),
    keuze(
        "Bij sommige hardnekkige darminfecties helpt een [[*microbioomtransplantatie|antibioticakuur|vaccin]] waar antibiotica tekortschieten.",
        "Darmbacteriën van een gezonde donor herstellen het evenwicht.",
    ),
    klik(
        "Klik op de fase die volgt als het aantal levende bacteriën begint te dalen.",
        GROEI.bestand, [Z_AFNAME],
        "De laatste fase van een kweek is de afname.",
    ),
    tabel(
        "Heeft dit organisme of deeltje een celwand?",
        [
            ("een bacterie", J),
            ("een virus", F),
            ("een plantencel", J),
            ("een dierlijke cel", F),
        ],
        "Veel antibiotica grijpen aan op de celwand van bacteriën. Een virus heeft geen celwand.",
    ),
    mk(
        "Een gist laat brood rijzen. Welk gas maakt ze daarbij?",
        ["Koolstofdioxide", "Zuurstofgas", "Stikstofgas", "Waterstofgas"],
        0,
        "De gasbelletjes koolstofdioxide doen het deeg rijzen.",
    ),
    keuze(
        "Azijnzuurbacteriën maken van [[*alcohol|melksuiker|zetmeel]] azijn.",
        "Gist maakt alcohol, azijnzuurbacteriën zetten die verder om.",
    ),
    tabel(
        "Breekt deze maatregel de weg van een ziekteverwekker?",
        [
            ("handen wassen na het toiletbezoek", J),
            ("in je elleboog niezen", J),
            ("een vaccin laten zetten", J),
            ("een antibioticum nemen tegen een verkoudheid", F),
        ],
        "Een verkoudheid komt door een virus. Hygiëne onderbreekt de weg van de besmetting.",
    ),
    open_(
        "Leg uit hoe antibioticaresistentie ontstaat en waarom je een antibioticakuur altijd uitdoet zoals voorgeschreven.",
        "Bacteriën die het antibioticum toevallig overleven, vermenigvuldigen zich verder en geven die eigenschap door. Stop je te vroeg of gebruik je het slordig, dan overleven er meer bacteriën en krijgen resistente stammen de bovenhand. Een volledige kuur doodt zo veel mogelijk bacteriën.",
    ),
]
