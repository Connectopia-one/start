"""Mengsels en zuivere stoffen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
import random
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Zes vakjes met deeltjes ------------------------------------------------
DEEL = Prent("deeltjes-zes-vakjes", "Zes stoffen, bekeken op deeltjesniveau", "zes vakjes met losse atomen, moleculen van één element, moleculen van twee elementen en mengsels")
VAK = {}
rnd = random.Random(7)
def _vak(letter, x, y, soort):
    DEEL.rect(x, y, 240, 190, "#ffffff", DONKER, 12)
    DEEL.letter(x + 24, y + 24, letter)
    VAK[letter] = Prent.zone(x, y, 240, 190)
    plekken = [(x + 50 + (i % 4) * 50, y + 60 + (i // 4) * 45) for i in range(12)]
    for i, (px, py) in enumerate(plekken):
        px += rnd.randint(-6, 6); py += rnd.randint(-6, 6)
        s = soort(i)
        if s == "a":
            DEEL.cirkel(px, py, 11, GRIJS)
        elif s == "b":
            DEEL.cirkel(px, py, 11, BLAUW)
        elif s == "aa":
            DEEL.cirkel(px - 8, py, 10, ROOD); DEEL.cirkel(px + 8, py, 10, ROOD)
        elif s == "ab":
            DEEL.cirkel(px - 9, py, 12, ROOD); DEEL.cirkel(px + 9, py, 8, "#ffffff")
_vak("A", 60, 80, lambda i: "a")
_vak("B", 380, 80, lambda i: "aa")
_vak("C", 700, 80, lambda i: "ab")
_vak("D", 60, 340, lambda i: "a" if i % 2 else "b")
_vak("E", 380, 340, lambda i: "aa" if i % 3 == 0 else "ab")
_vak("F", 700, 340, lambda i: "b")

# Twee opwarmcurven -------------------------------------------------------
OPW = Prent("opwarmcurven", "Twee vloeistoffen worden verwarmd tot ze koken", "opwarmcurve met een kookpunt (A) en met een kooktraject (B)")
OPW.lijn(110, 560, 930, 560, DONKER, 2)
OPW.lijn(110, 560, 110, 80, DONKER, 2)
OPW.tekst(102, 70, "temperatuur", 16, "start")
OPW.tekst(925, 595, "tijd", 16, "end")
OPW.pad("M110 500 L 420 230 L 900 230", "none", BLAUW, 4)
OPW.pad("M110 520 L 400 300 C 600 250, 780 200, 900 160", "none", ORANJE, 4)
OPW.letter(870, 270, "A"); OPW.letter(870, 120, "B")
Z_PLATEAU = [Prent.zone(430, 213, 130, 34), Prent.zone(760, 213, 140, 34)]
Z_TRAJECT = [Prent.zone(400, 255, 160, 50), Prent.zone(720, 150, 180, 58)]

VRAGEN = [
    klik(
        "Klik op een vakje met een mengsel.",
        DEEL.bestand, [VAK["D"], VAK["E"]],
        "In een mengsel zitten verschillende soorten deeltjes door elkaar.",
    ),
    klik(
        "Klik op het vakje met een zuivere stof die uit moleculen van één enkel element bestaat, zoals zuurstofgas.",
        DEEL.bestand, [VAK["B"]],
        "Zuurstofgas bestaat uit moleculen van twee zuurstofatomen. Een molecule kan uit atomen van één element bestaan.",
    ),
    klik(
        "Klik op het vakje met een zuivere stof waarvan elke molecule uit twee verschillende soorten atomen bestaat.",
        DEEL.bestand, [VAK["C"]],
        "Alle deeltjes zijn hetzelfde, dus het is een zuivere stof, ook al bestaan ze uit verschillende atomen.",
    ),
    met_prent(DEEL.bestand, tabel(
        "Kijk naar de zes vakjes. Klopt dit?",
        [
            ("A, B, C en F zijn zuivere stoffen.", J),
            ("In vakje D zie je moleculen.", F),
            ("Vakje E bevat twee soorten moleculen.", J),
            ("Vakje C is een mengsel, want er zitten twee soorten atomen in.", F),
        ],
        "Zuiver betekent één soort deeltjes. Een molecule mag uit verschillende atomen bestaan.",
    )),
    klik(
        "Klik op het stuk van de grafiek dat toont dat A een zuivere stof is.",
        OPW.bestand, Z_PLATEAU,
        "Tijdens het koken blijft de temperatuur van een zuivere stof gelijk: het kookpunt.",
    ),
    klik(
        "Klik op het kooktraject van het mengsel.",
        OPW.bestand, Z_TRAJECT,
        "Bij een mengsel blijft de temperatuur tijdens het koken stijgen.",
    ),
    tabel(
        "Homogeen of heterogeen?",
        [
            ("suiker opgelost in water", "Homogeen"),
            ("lucht", "Homogeen"),
            ("messing", "Homogeen"),
            ("slagroom", "Heterogeen"),
            ("vinaigrette", "Heterogeen"),
            ("modder", "Heterogeen"),
        ],
        "In een homogeen mengsel zie je de bestanddelen niet meer apart, ook niet met een microscoop.",
        kolommen=["Homogeen", "Heterogeen"],
    ),
    koppel(
        "Koppel elk mengsel aan zijn soort.",
        [
            ("melk", "emulsie"),
            ("opgeschudde modder", "suspensie"),
            ("rook", "aerosol"),
            ("badschuim", "schuim"),
            ("brons", "legering"),
        ],
        ["zuivere stof"],
        "Geen van deze is een zuivere stof: er zitten telkens meerdere stoffen in.",
    ),
    casus(
        "In het labo verwarmt Amir twee heldere, kleurloze vloeistoffen. Bij vloeistof 1 blijft de thermometer tijdens het koken op 100 °C staan. Bij vloeistof 2 stijgt de temperatuur tijdens het koken van 101 °C tot 104 °C.",
        [
            tabel(
                "Wat besluit Amir?",
                [
                    ("Vloeistof 1 is waarschijnlijk zuiver water.", J),
                    ("Vloeistof 2 is een mengsel.", J),
                    ("Vloeistof 2 heeft een kookpunt van 101 °C.", F),
                    ("Beide zijn zuivere stoffen, want ze zijn helder.", F),
                ],
                "Helder zegt niets: een oplossing is ook helder. Een mengsel heeft een kooktraject.",
            ),
            mk(
                "Hoe kan Amir uit vloeistof 2 zuiver water halen?",
                ["Door te destilleren", "Door te filtreren door papier", "Door voorzichtig te decanteren", "Door te zeven"],
                0,
                "Bij destilleren vang je de waterdamp op. De opgeloste stof blijft achter.",
            ),
        ],
    ),
    mk(
        "Waarom strooit men zout op een besneeuwde weg?",
        [
            "Een mengsel smelt bij een lagere temperatuur",
            "Zout warmt de weg op door een chemische reactie",
            "Zout maakt het ijs harder en daardoor minder glad",
            "Zout neemt al het water op uit de sneeuw",
        ],
        0,
        "Een mengsel heeft een smelttraject in plaats van een vast smeltpunt.",
    ),
    tabel(
        "Is dit een stofeigenschap?",
        [
            ("het kookpunt", J),
            ("de massa van een stuk", F),
            ("de massadichtheid", J),
            ("het volume van een fles", F),
            ("de geleidbaarheid", J),
        ],
        "Een stofeigenschap hangt niet af van hoeveel je van de stof hebt.",
    ),
    koppel(
        "Koppel elke scheiding aan de techniek die je gebruikt.",
        [
            ("zand uit water", "filtreren"),
            ("zuiver water uit zeewater", "destilleren"),
            ("keukenzout uit zout water", "indampen"),
            ("kleurstoffen uit stiftinkt", "chromatografie"),
            ("ijzervijlsel uit zand", "magneet"),
        ],
        ["smelten"],
        "Elke techniek steunt op een verschil in stofeigenschap.",
    ),
    tabel(
        "Op welk verschil steunt deze scheidingstechniek?",
        [
            ("filtreren", "Deeltjesgrootte"),
            ("zeven", "Deeltjesgrootte"),
            ("destilleren", "Kookpunt"),
            ("centrifugeren", "Massadichtheid"),
            ("extraheren", "Oplosbaarheid"),
        ],
        "Zonder verschil in stofeigenschap valt er niets te scheiden.",
        kolommen=["Deeltjesgrootte", "Kookpunt", "Massadichtheid", "Oplosbaarheid"],
    ),
    volgorde(
        "Zet de stappen van destilleren in de juiste volgorde.",
        [
            "Het mengsel verwarmen",
            "Het bestanddeel met het laagste kookpunt verdampt",
            "De damp koelt af in de koeler",
            "Het destillaat druppelt in de opvangkolf",
        ],
        "De stof met het hoogste kookpunt blijft achter.",
    ),
    casus(
        "Lena maakt een vinaigrette van olie en azijn. Na een tijdje drijft de olie bovenop. Ze wil de olie en de azijn weer apart.",
        [
            mk(
                "Waarom lukt filtreren hier niet?",
                [
                    "Beide vloeistoffen lopen door de filter",
                    "De olie verstopt meteen alle filters",
                    "Azijn lost op in het filterpapier zelf",
                    "Filtreren werkt enkel bij mengsels van gassen",
                ],
                0,
                "Filtreren werkt op deeltjesgrootte. Vloeibare druppeltjes gaan erdoor.",
            ),
            keuze(
                "Lena laat het mengsel uitzakken en giet de olie er voorzichtig af. Dat heet [[*decanteren|centrifugeren|extraheren]].",
                "Decanteren is voorzichtig afgieten boven een bezinksel of een tweede laag.",
            ),
            tabel(
                "Klopt dit over de vinaigrette?",
                [
                    ("Het is een emulsie.", J),
                    ("Het is een heterogeen mengsel.", J),
                    ("Olie en azijn verliezen hun eigen eigenschappen.", F),
                ],
                "Een bestanddeel van een mengsel behoudt zijn eigen stofeigenschappen.",
            ),
        ],
    ),
    sleep(
        "Na het filtreren blijft het [[residu]] op de filter liggen. Het [[filtraat]] loopt erdoor. Welk van de twee je nodig hebt, hangt af van je [[doel]].",
        ["destillaat", "loopmiddel"],
        "Allebei kunnen ze het bestanddeel zijn dat je zoekt.",
    ),
    mk(
        "Hoe haalt actieve kool geurstoffen uit water?",
        [
            "De stoffen hechten aan haar oppervlak",
            "Ze lost de geurstoffen chemisch op",
            "Ze verdampt het water weg",
            "Ze laat de stoffen bezinken door te draaien",
        ],
        0,
        "Dat is adsorptie. Actieve kool heeft een enorm inwendig oppervlak.",
    ),
    tabel(
        "Klopt dit over zuivere stoffen en mengsels?",
        [
            ("Kraantjeswater is een zuivere stof.", F),
            ("Een zuivere stof kan uit meer dan één element bestaan.", J),
            ("Scheiden verandert de stoffen niet chemisch.", J),
            ("Een legering is een heterogeen mengsel.", F),
            ("Lucht is een homogeen mengsel.", J),
        ],
        "Kraantjeswater bevat opgeloste zouten en gassen. Een legering is homogeen.",
    ),
    keuze(
        "Een labo scheidt bloedcellen van bloedplasma door snel rond te draaien met een [[*centrifuge|filter|koeler]].",
        "De zwaarste deeltjes worden naar buiten geduwd.",
    ),
    keuze(
        "Je zet theeblaadjes in heet water om de smaakstoffen eruit te halen. Dat is [[*extraheren|destilleren|zeven]].",
        "Je gebruikt een oplosmiddel waarin alleen de gezochte stof oplost.",
    ),
    klik(
        "Klik op het vakje met losse atomen van één soort.",
        DEEL.bestand, [VAK["A"], VAK["F"]],
        "In A en F zitten losse atomen, telkens van één soort. Zo'n stof is zuiver.",
    ),
    mk(
        "Zuurstofgas bestaat uit moleculen, ijzer uit losse atomen. Wat is het verschil?",
        [
            "Een molecule bestaat uit gebonden atomen",
            "Een molecule is altijd een mengsel van stoffen",
            "Een atoom bestaat uit verschillende moleculen",
            "Een molecule bevat nooit atomen van één element",
        ],
        0,
        "Zuurstofgas bestaat uit moleculen van twee zuurstofatomen.",
    ),
    sorteer(
        "Zuivere stof of mengsel?",
        ["Zuivere stof", "Mengsel"],
        [
            ["keukenzout", "Zuivere stof"],
            ["gedestilleerd water", "Zuivere stof"],
            ["zuurstofgas", "Zuivere stof"],
            ["bronwater", "Mengsel"],
            ["lucht", "Mengsel"],
            ["staal", "Mengsel"],
        ],
        "Zuiver betekent één soort deeltjes, niet schoon of natuurlijk.",
    ),
    keuze(
        "Melk en vinaigrette scheiden zich na een tijd weer, omdat het [[*emulsies|oplossingen|legeringen]] zijn.",
        "In een emulsie lossen de twee vloeistoffen niet in elkaar op.",
    ),
    tabel(
        "Klopt dit over de aggregatietoestand?",
        [
            ("Er zijn drie aggregatietoestanden: vast, vloeibaar en gas.", J),
            ("De toestand hangt af van de temperatuur en de druk.", J),
            ("Een stof heeft altijd maar één mogelijke toestand.", F),
        ],
        "Water kan ijs, vloeibaar water of waterdamp zijn.",
    ),
    tabel(
        "Kan je deze mengsels scheiden met een filter?",
        [
            ("zand in water", J),
            ("suiker opgelost in water", F),
            ("olie en water", F),
            ("krijtpoeder in water", J),
        ],
        "Een filter houdt enkel vaste deeltjes tegen die groter zijn dan de poriën. Opgeloste stoffen en vloeistoffen gaan erdoor.",
    ),
    open_(
        "Je krijgt een mengsel van zand, keukenzout en water. Beschrijf in twee stappen hoe je het zand en het zout elk apart terugwint, en zeg op welk verschil in stofeigenschap elke stap steunt.",
        "Stap 1: filtreren. Het zand blijft als residu op de filter, het zoute water loopt als filtraat door. Dat steunt op een verschil in deeltjesgrootte. Stap 2: het filtraat indampen. Het water verdampt en het zout kristalliseert uit. Dat steunt op een verschil in kookpunt.",
    ),
]
