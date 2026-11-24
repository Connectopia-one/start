"""Water en homeostase bij planten — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL

# Doorsnede van een blad, zonder namen ------------------------------------
BLAD = Prent("blad-doorsnede", "Doorsnede van een blad", "schematische doorsnede van een blad met cuticula, epidermis, vulweefsel, sponsweefsel, vaatbundel en huidmondje")
BLAD.rect(80, 80, 840, 12, "#f3e7a8", DONKER, 0, 1)                     # cuticula
for i in range(14):
    BLAD.rect(80 + i * 60, 92, 60, 38, "#f4f1e8")                       # bovenepidermis
for i in range(21):
    BLAD.rect(82 + i * 40, 132, 36, 120, LICHTGROEN, DONKER, 12)        # palissade
    for k in range(4):
        BLAD.cirkel(100 + i * 40, 150 + k * 28, 6, GROEN, GROEN, 1)
for (x, y) in [(130, 300), (230, 290), (320, 320), (700, 290), (800, 320), (880, 290), (150, 370), (260, 365), (760, 370), (860, 370)]:
    BLAD.ellips(x, y, 42, 26, "#cfe3b8")                                 # sponsweefsel
BLAD.ellips(500, 325, 110, 62, "#efe6cf")                                # vaatbundel
BLAD.ellips(500, 305, 70, 26, BLAUW)                                      # xyleem
BLAD.ellips(500, 352, 70, 20, ORANJE)                                     # floeem
for i in range(14):
    if i in (10, 11):
        continue
    BLAD.rect(80 + i * 60, 410, 60, 36, "#f4f1e8")                       # onderepidermis
BLAD.ellips(680, 428, 22, 16, LICHTGROEN)
BLAD.ellips(740, 428, 22, 16, LICHTGROEN)                                 # sluitcellen
BLAD.tekst(500, 520, "Bovenaan valt het licht op het blad. Onderaan grenst het blad aan de lucht.", 18)
Z_CUTICULA = Prent.zone(80, 74, 840, 22)
Z_PALISSADE = Prent.zone(80, 132, 840, 120)
Z_XYLEEM = Prent.zone(430, 279, 140, 52)
Z_FLOEEM = Prent.zone(430, 332, 140, 40)
Z_HUIDMOND = Prent.zone(650, 405, 120, 46)

# Een plant ---------------------------------------------------------------
PLANT = Prent("plant-organen", "Een plant", "plant met bloem, stengel, bladeren, wortel en wortelharen")
PLANT.lijn(0, 400, 1000, 400, "#8a6d3b", 3)
PLANT.rect(490, 140, 20, 260, GROEN, GROEN)                               # stengel
PLANT.pad("M500 260 C 600 200, 700 220, 760 250 C 700 290, 600 300, 500 270 Z", LICHTGROEN)
PLANT.pad("M500 320 C 400 260, 300 280, 240 310 C 300 350, 400 350, 500 330 Z", LICHTGROEN)
for a in range(6):
    import math
    PLANT.ellips(500 + 40 * math.cos(a), 110 + 40 * math.sin(a), 30, 18, GEEL)
PLANT.cirkel(500, 110, 22, ORANJE)
PLANT.pad("M500 400 L 500 520 M500 450 L 430 540 M500 460 L 580 560", "none", "#8a6d3b", 6)
for (x, y) in [(440, 520), (430, 545), (575, 540), (585, 565), (505, 515)]:
    PLANT.pad(f"M{x} {y} l -25 10 M{x} {y} l 22 14 M{x} {y} l 4 26", "none", "#8a6d3b", 1)
Z_WORTELHAAR = Prent.zone(390, 490, 230, 110)
Z_BLAD = [Prent.zone(505, 215, 260, 78), Prent.zone(235, 276, 255, 72)]
Z_BLOEM = Prent.zone(430, 60, 140, 100)

VRAGEN = [
    klik(
        "Klik in de doorsnede op het weefsel met de meeste bladgroenkorrels.",
        BLAD.bestand, [Z_PALISSADE],
        "Het vulweefsel net onder de bovenkant zit vol chloroplasten. Daar gebeurt het meeste werk van de fotosynthese.",
    ),
    klik(
        "Klik op de vaten die water en zouten aanvoeren vanuit de wortel.",
        BLAD.bestand, [Z_XYLEEM],
        "In de vaatbundel liggen de houtvaten of het xyleem bovenaan, de zeefvaten of het floëem eronder.",
    ),
    klik(
        "Klik op de vaten die de assimilaten uit dit blad wegvoeren.",
        BLAD.bestand, [Z_FLOEEM],
        "Het floëem vervoert de suikers uit de fotosynthese naar de rest van de plant.",
    ),
    klik(
        "Klik op de plek waar waterdamp het blad verlaat en koolstofdioxide binnenkomt.",
        BLAD.bestand, [Z_HUIDMOND],
        "Het huidmondje tussen de twee sluitcellen aan de onderkant laat gassen door.",
    ),
    klik(
        "Klik op het laagje dat het waterverlies tussen de huidmondjes door beperkt.",
        BLAD.bestand, [Z_CUTICULA],
        "De cuticula is een waslaagje bovenop de epidermis.",
    ),
    klik(
        "Klik op de plaats waar de plant het grootste deel van haar water opneemt.",
        PLANT.bestand, [Z_WORTELHAAR],
        "De wortelharen vergroten het contactoppervlak met de bodem enorm.",
    ),
    klik(
        "Klik op het orgaan waar het meeste water de plant verlaat.",
        PLANT.bestand, Z_BLAD,
        "Het meeste water verdampt via de huidmondjes van de bladeren. Dat is transpiratie.",
    ),
    casus(
        "Lies vergeet haar kamerplant een week water te geven. Het is warm en zonnig. De bladeren hangen slap en de stengel zakt in.",
        [
            mk(
                "Wat is er in de cellen van de plant gebeurd?",
                [
                    "De vacuoles zijn leeggelopen",
                    "De celwanden zijn opgelost in het water",
                    "De chloroplasten zijn uit de cel verdwenen",
                    "De wortelharen zijn veel langer geworden",
                ],
                0,
                "De cellen verliezen hun turgor: er duwt geen vocht meer tegen de celwand.",
            ),
            tabel(
                "Klopt dit over de plant van Lies?",
                [
                    ("Ze verloor door verdamping meer water dan ze opnam.", J),
                    ("Ze zet haar huidmondjes wijd open om af te koelen.", F),
                    ("Haar fotosynthese vertraagt.", J),
                    ("Het warme weer versnelde het waterverlies.", J),
                ],
                "Bij droogte sluit de plant haar huidmondjes. Daardoor komt er ook minder koolstofdioxide binnen.",
            ),
            mk(
                "Welk hormoon zorgt ervoor dat de huidmondjes dichtgaan?",
                ["Abscisinezuur", "Auxine uit de stengeltop", "Ethyleen uit rijpe vruchten", "Glucose"],
                0,
                "Abscisinezuur is het hormoon van de droogte. Glucose is geen hormoon.",
            ),
            keuze(
                "Lies geeft de plant weer water. De cellen krijgen hun [[*turgor|cuticula|chloroplasten]] terug en de plant gaat weer rechtop staan.",
                "De vacuoles vullen zich en duwen weer tegen de celwand.",
            ),
        ],
    ),
    volgorde(
        "Zet de weg van een watermolecule door de plant in de juiste volgorde.",
        [
            "Opname door een wortelhaar",
            "Transport omhoog door het xyleem",
            "Aankomst in het blad",
            "Ontsnappen als damp door een huidmondje",
        ],
        "Wateropname, watertransport en transpiratie: de drie stappen van de waterhuishouding.",
    ),
    koppel(
        "Koppel elke kracht aan wat ze doet bij het watertransport.",
        [
            ("worteldruk", "De wortel duwt water van onderuit de houtvaten in."),
            ("transpiratiezuiging", "Verdamping in het blad trekt aan de waterdraad."),
            ("capillariteit", "Water kruipt vanzelf omhoog in een heel nauwe buis."),
        ],
        ["De bloem pompt water naar beneden."],
        "Duwen van onderaf, trekken van bovenaf en omhoogkruipen in nauwe vaten.",
    ),
    tabel(
        "Stijgt of daalt de transpiratie?",
        [
            ("De lucht rond de plant wordt veel vochtiger.", "Daalt"),
            ("Het wordt warmer en zonniger.", "Stijgt"),
            ("De plant sluit haar huidmondjes.", "Daalt"),
            ("Er waait een droge wind over de bladeren.", "Stijgt"),
        ],
        "Water verdampt van vochtig naar droog. Hoe groter dat verschil en hoe warmer, hoe meer verdamping.",
        kolommen=["Stijgt", "Daalt"],
    ),
    sorteer(
        "Gaat deze stof door het xyleem of door het floëem?",
        ["Xyleem", "Floëem"],
        [
            ["water uit de bodem", "Xyleem"],
            ["opgeloste mineralen", "Xyleem"],
            ["glucose uit het blad", "Floëem"],
            ["suikers naar een vrucht", "Floëem"],
        ],
        "Xyleem vervoert water en mineralen omhoog, floëem vervoert assimilaten in beide richtingen.",
    ),
    mk(
        "Een blad sluit zijn huidmondjes op een droge dag. Welk nadeel heeft dat?",
        [
            "Er komt minder koolstofdioxide binnen",
            "Er gaat meer water verloren door verdamping",
            "De wortel neemt plots veel meer water op",
            "Het blad maakt veel meer glucose dan normaal",
        ],
        0,
        "Dezelfde huidmondjes laten water ontsnappen en koolstofdioxide binnen.",
    ),
    tabel(
        "Is dit een grondstof, een product of de energiebron van de fotosynthese?",
        [
            ("water", "Grondstof"),
            ("koolstofdioxide", "Grondstof"),
            ("glucose", "Product"),
            ("zuurstofgas", "Product"),
            ("licht", "Energiebron"),
        ],
        "Koolstofdioxide en water geven onder invloed van licht glucose en zuurstofgas.",
        kolommen=["Grondstof", "Product", "Energiebron"],
    ),
    sleep(
        "Verliest een blad te veel water, dan verslappen de [[sluitcellen]] en gaat het huidmondje dicht. Het verlies daalt weer. Dat terugkoppelen heet [[feedback]], en zo houdt de plant haar inwendig milieu stabiel: [[homeostase]].",
        ["chloroplasten", "fotosynthese", "capillariteit"],
        "Het gevolg van een proces stuurt dat proces zelf bij.",
    ),
    casus(
        "In een proef zet een klas twee gelijke plantjes in een afgesloten glazen bak. Bak A staat in de zon, bak B in een donkere kast. Na een dag meten ze het zuurstofgas in de bakken.",
        [
            mk(
                "In welke bak zit na een dag het meeste zuurstofgas?",
                ["Bak A, in de zon", "Bak B, in de kast", "In beide evenveel", "In geen van beide"],
                0,
                "Zonder licht is er geen energie voor de fotosynthese, dus geen zuurstofgas erbij.",
            ),
            tabel(
                "Klopt dit over de plant in bak B?",
                [
                    ("Ze maakt even veel glucose als de plant in de zon.", F),
                    ("Ze teert op haar voorraad.", J),
                    ("Ze heeft geen licht als energiebron.", J),
                ],
                "In het donker maakt een plant geen glucose bij.",
            ),
        ],
    ),
    mk(
        "Een plant op de vensterbank buigt naar het raam. Wat gebeurt er aan de donkere kant van de stengel?",
        [
            "Er zit meer auxine en de cellen strekken sneller",
            "Er zit minder auxine en de cellen stoppen met groeien",
            "Er komt ethyleen vrij en de stengel gaat er rijpen",
            "De huidmondjes gaan er dicht door abscisinezuur",
        ],
        0,
        "Auxine wordt weggedrukt van het licht. De donkere kant groeit harder, zodat de stengel naar het licht buigt.",
    ),
    koppel(
        "Koppel elk plantenhormoon aan zijn taak.",
        [
            ("auxine", "De stengel naar het licht laten groeien"),
            ("ethyleen", "Vruchten laten rijpen"),
            ("abscisinezuur", "Huidmondjes sluiten bij droogte"),
        ],
        ["Licht opvangen in de chloroplast"],
        "Licht opvangen doet het bladgroen, geen hormoon.",
    ),
    keuze(
        "Eén rijpe appel in een mand laat de andere sneller rijpen, omdat hij het gas [[*ethyleen|zuurstofgas|koolstofdioxide]] afgeeft.",
        "Ethyleen is een gasvormig plantenhormoon.",
    ),
    tabel(
        "Klopt dit over de bouw van een plant?",
        [
            ("Een plant heeft vier organen: wortel, stengel, blad en bloem.", J),
            ("Houtvaten en zeefvaten liggen samen in een vaatbundel.", J),
            ("Een nerf in een blad is een vaatbundel.", J),
            ("De epidermis is een transportweefsel.", F),
            ("De cuticula ligt onder het vulweefsel.", F),
        ],
        "De epidermis en de cuticula zijn huidweefsel en dekken de plant af.",
    ),
    mk(
        "Waarom liggen de meeste huidmondjes aan de onderkant van het blad?",
        [
            "Daar is het koeler en verliest de plant minder water",
            "Daar valt het meeste licht op het blad als de zon schijnt",
            "Daar zitten de meeste bladgroenkorrels van het hele blad",
            "Daar komt het water uit de wortel als allereerste aan",
        ],
        0,
        "Aan de onderkant is het koeler en vochtiger dan aan de zonkant.",
    ),
    mk(
        "Water stijgt in een nauw glazen buisje vanzelf een stukje omhoog. Welke kracht in de plant lijkt daarop?",
        ["Capillariteit", "De worteldruk", "De turgor", "Transpiratiezuiging"],
        0,
        "Water blijft aan de wand hangen en de moleculen kleven aan elkaar. De houtvaten zijn zulke nauwe buizen.",
    ),
    tabel(
        "Klopt dit over transpiratie?",
        [
            ("Ze koelt het blad af bij warm weer.", J),
            ("Ze is de belangrijkste motor van het watertransport naar boven.", J),
            ("Ze duwt het water van het blad naar de wortel.", F),
            ("Ze levert de suikers voor de plant.", F),
        ],
        "Transpiratie trekt water omhoog en koelt. De suikers komen van de fotosynthese.",
    ),
    klik(
        "Klik op het orgaan dat bij deze plant geen rol speelt in de waterhuishouding of de fotosynthese, maar in de voortplanting.",
        PLANT.bestand, [Z_BLOEM],
        "Wortel, stengel en blad nemen water op, vervoeren het en laten het verdampen. De bloem dient voor de voortplanting.",
    ),
    tabel(
        "Welke omgevingsfactor speelt mee in de waterhuishouding van een plant?",
        [
            ("de lichtsterkte op de bladeren", J),
            ("de vochtigheid van de bodem", J),
            ("de kleur van de bloemblaadjes", F),
            ("de temperatuur van de lucht", J),
            ("de vorm van de bloempot", F),
        ],
        "Licht, temperatuur en de vochtigheid van bodem en lucht spelen mee.",
    ),
    open_(
        "Leg uit waarom de waterhuishouding van een plant en haar fotosynthese nauw met elkaar samenhangen. Gebruik de woorden huidmondjes, koolstofdioxide en water.",
        "Water is een grondstof van de fotosynthese. Bovendien laten dezelfde huidmondjes waterdamp ontsnappen en koolstofdioxide binnen. Sluit de plant bij droogte haar huidmondjes om water te sparen, dan komt er ook amper koolstofdioxide binnen en valt de fotosynthese zo goed als stil.",
    ),
]
