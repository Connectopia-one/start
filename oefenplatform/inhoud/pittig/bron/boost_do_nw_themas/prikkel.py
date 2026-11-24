"""Van prikkel tot reactie, en het oog — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD

# Doorsnede van het oog, zonder namen ------------------------------------
OOG = Prent("oog-doorsnede", "Doorsnede van het oog, zijaanzicht", "zijdelingse doorsnede van het oog: hoornvlies, iris, pupil, lens, straallichaam, netvlies, gele vlek, blinde vlek en oogzenuw")
CX, CY = 560, 330
OOG.pad("M740 392 L 950 430 L 950 480 L 734 410 Z", "#f1d9a8")                 # oogzenuw
OOG.cirkel(CX, CY, 210, "#ffffff", DONKER, 4)                                  # hard oogvlies
OOG.cirkel(CX, CY, 199, "#ffffff", "#8a5a3b", 6)                               # vaatvlies
def _boog(r, a1, a2):
    x1, y1 = CX + r * math.cos(math.radians(a1)), CY + r * math.sin(math.radians(a1))
    x2, y2 = CX + r * math.cos(math.radians(a2)), CY + r * math.sin(math.radians(a2))
    return f"M{x1:.1f} {y1:.1f} A {r} {r} 0 0 1 {x2:.1f} {y2:.1f}"
OOG.cirkel(CX, CY, 182, "#eef4f8", "none", 0)                                  # glasachtig lichaam
OOG.pad(_boog(190, -125, 125), "none", ROOD, 6)                                # netvlies
OOG.pad("M378 222 Q 290 330 378 438", "#e6f0f6", BLAUW, 4)                    # hoornvlies
OOG.rect(388, 238, 12, 62, "#7a5230", DONKER, 3)                               # iris boven
OOG.rect(388, 360, 12, 62, "#7a5230", DONKER, 3)                               # iris onder
OOG.ellips(436, 330, 30, 78, "#f7f0c8")                                        # lens
OOG.rect(420, 212, 30, 28, "#c9a27a", DONKER, 6)                               # straallichaam
OOG.rect(420, 420, 30, 28, "#c9a27a", DONKER, 6)
OOG.cirkel(750, 330, 13, GEEL, DONKER, 2)                                      # gele vlek
OOG.cirkel(738, 398, 13, "#222222", DONKER, 2)                                 # blinde vlek
OOG.tekst(150, 330, "licht", 22)
OOG.pijl(110, 345, 280, 345)
Z_LENS = Prent.zone(404, 250, 64, 160)
Z_PUPIL = Prent.zone(380, 300, 26, 60)
Z_IRIS = [Prent.zone(382, 232, 24, 72), Prent.zone(382, 356, 24, 72)]
Z_HOORN = Prent.zone(300, 220, 78, 220)
Z_GELE = Prent.rond(750, 330, 22)
Z_BLINDE = Prent.rond(738, 398, 22)
Z_ZENUW = Prent.zone(770, 400, 185, 85)
Z_STRAAL = [Prent.zone(414, 206, 42, 40), Prent.zone(414, 414, 42, 40)]

# Drie ogen met lichtstralen ---------------------------------------------
DRIE = Prent("drie-ogen-brandpunt", "Waar komen de lichtstralen van ver samen?", "drie ogen waarbij de stralen vóór, op en achter het netvlies samenkomen")
PUNT = {}
for i, (x, verschil) in enumerate([(200, -45), (500, 0), (800, 45)]):
    DRIE.cirkel(x, 300, 110, "#ffffff", DONKER, 3)
    DRIE.pad(f"M{x-100} 250 Q {x-130} 300 {x-100} 350", "#e6f0f6", BLAUW, 3)
    DRIE.ellips(x - 75, 300, 14, 40, "#f7f0c8")
    fx = x + 110 + verschil
    for y in (262, 300, 338):
        DRIE.lijn(x - 180, y, x - 75, y, GEEL if y != 300 else ORANJE, 2)
        DRIE.lijn(x - 75, y, fx, 300, ORANJE, 2)
    DRIE.pad(f"M{x+77} 222 A 110 110 0 0 1 {x+77} 378", "none", ROOD, 5)
    DRIE.letter(x, 460, "ABC"[i])
    PUNT["ABC"[i]] = Prent.zone(x - 140, 180, 280, 310)

VRAGEN = [
    klik(
        "Klik op het deel dat van vorm verandert als je scherpstelt.",
        OOG.bestand, [Z_LENS],
        "Bij accommodatie wordt de ooglens boller of platter.",
    ),
    klik(
        "Klik op het deel met de spieren die de pupil groter of kleiner maken.",
        OOG.bestand, Z_IRIS,
        "De straal- en kringspieren van de iris regelen hoeveel licht er binnenkomt.",
    ),
    klik(
        "Klik op de plek waar je het scherpst ziet.",
        OOG.bestand, [Z_GELE],
        "In de gele vlek liggen de kegeltjes het dichtst op elkaar.",
    ),
    klik(
        "Klik op de plek waar je niets ziet.",
        OOG.bestand, [Z_BLINDE],
        "Op de blinde vlek verlaat de oogzenuw het oog en liggen er geen staafjes of kegeltjes.",
    ),
    klik(
        "Klik op het doorzichtige deel van het harde oogvlies dat het licht als eerste breekt.",
        OOG.bestand, [Z_HOORN],
        "Het hoornvlies breekt het licht al voor een groot deel, nog voor de lens eraan te pas komt.",
    ),
    klik(
        "Klik op het deel met de accommodatiespier, die de lensbanden spant of ontspant.",
        OOG.bestand, Z_STRAAL,
        "De accommodatiespier zit in het straallichaam, dat bij het vaatvlies hoort.",
    ),
    klik(
        "Klik op het oog van iemand die bijziend is.",
        DRIE.bestand, [PUNT["A"]],
        "Bij bijziendheid komen de stralen van ver al vóór het netvlies samen.",
    ),
    klik(
        "Klik op het oog dat je helpt met een bolle of positieve lens.",
        DRIE.bestand, [PUNT["C"]],
        "Bij verziendheid valt het beeld achter het netvlies. Een bolle lens breekt het licht extra.",
    ),
    casus(
        "Noor raakt per ongeluk een hete pan aan en trekt haar hand weg nog voor ze echt beseft wat er gebeurt.",
        [
            koppel(
                "Koppel elk deel van de reactie van Noor aan zijn rol.",
                [
                    ("de hitte van de pan", "prikkel"),
                    ("de zintuigcellen in de huid", "receptor"),
                    ("de zenuwen", "conductor"),
                    ("de spier in de arm", "effector"),
                ],
                ["hormoon"],
                "Prikkel, receptor, conductor en effector: de weg van prikkel naar reactie.",
            ),
            tabel(
                "Klopt dit over de reactie van Noor?",
                [
                    ("De hitte is een uitwendige prikkel.", J),
                    ("Een klier voert hier de reactie uit.", F),
                    ("Het signaal gaat van de receptor naar de effector.", J),
                    ("Haar ogen zijn hier de receptor.", F),
                ],
                "De receptor zit in de huid, de effector is de armspier.",
            ),
        ],
    ),
    sorteer(
        "Is dit een uitwendige of een inwendige prikkel?",
        ["Uitwendig", "Inwendig"],
        [
            ["het geluid van een sirene", "Uitwendig"],
            ["een ijskoude wind", "Uitwendig"],
            ["de geur van verbrande toast", "Uitwendig"],
            ["dorst", "Inwendig"],
            ["honger", "Inwendig"],
            ["stress", "Inwendig"],
        ],
        "Inwendige prikkels ontstaan in het lichaam zelf.",
    ),
    tabel(
        "Is dit een tropie of een nastie?",
        [
            ("een stengel die naar het raam buigt", "Tropie"),
            ("een wortel die naar beneden groeit", "Tropie"),
            ("een bloem die dichtklapt bij kou", "Nastie"),
        ],
        "Bij een tropie bepaalt de richting van de prikkel de richting van de groei, bij een nastie niet.",
        kolommen=["Tropie", "Nastie"],
    ),
    mk(
        "Een plant en een kat krijgen allebei dezelfde lichtprikkel. Wat klopt er?",
        [
            "De plant stuurt met hormonen en reageert trager",
            "De plant reageert sneller, want ze heeft meer zenuwen",
            "Beide sturen elektrische impulsen langs zenuwbanen",
            "De kat reageert enkel met groeibewegingen van delen",
        ],
        0,
        "Een plant heeft geen zenuwstelsel. Haar antwoord is meestal een groeibeweging van uren of dagen.",
    ),
    koppel(
        "Koppel de receptor aan het zintuig.",
        [
            ("staafjes en kegeltjes", "zicht"),
            ("haarcellen", "gehoor"),
            ("zintuigcellen op de tong", "smaak"),
            ("receptoren hoog in de neus", "reuk"),
        ],
        ["sluitcellen"],
        "Sluitcellen zitten rond een huidmondje van een plant en zijn geen receptor.",
    ),
    volgorde(
        "Zet de lagen van de wand van de oogbol van buiten naar binnen.",
        ["Hard oogvlies", "Vaatvlies", "Netvlies"],
        "Het hoornvlies hoort bij de buitenste laag, iris en straallichaam bij het vaatvlies.",
    ),
    volgorde(
        "Zet de weg van een lichtsignaal in het netvlies in de juiste volgorde.",
        ["Staafjes en kegeltjes", "Bipolaire cellen", "Ganglioncellen", "Oogzenuw", "Hersenen"],
        "Het netvlies is in lagen gebouwd. De uitlopers van de ganglioncellen vormen samen de oogzenuw.",
    ),
    casus(
        "Sam komt uit het felle zonlicht een donkere kelder binnen. Eerst ziet hij bijna niets, na een tijdje ziet hij de dozen staan, maar alles lijkt grijs.",
        [
            tabel(
                "Klopt dit over wat er in het oog van Sam gebeurt?",
                [
                    ("Zijn pupillen worden groter.", J),
                    ("De staafjes nemen het werk over.", J),
                    ("De kegeltjes zien de kleuren nu scherper.", F),
                    ("Zijn ooglens wordt doorzichtiger.", F),
                ],
                "Bij weinig licht gaat de pupil open en werken vooral de staafjes. Die zien geen kleur.",
            ),
            mk(
                "Waarom lijkt alles in de kelder grijs?",
                [
                    "Staafjes zien geen kleur",
                    "Het glasachtig lichaam kleurt grijs",
                    "De oogzenuw is even uitgeschakeld",
                    "De lens draait het beeld op zijn kop",
                ],
                0,
                "Kegeltjes zien kleur bij veel licht, staafjes grijswaarden bij weinig licht.",
            ),
        ],
    ),
    tabel(
        "Wordt de ooglens boller of platter?",
        [
            ("Je kijkt van een verre berg naar je gsm.", "Boller"),
            ("Je kijkt van je boek naar een bord achteraan in de klas.", "Platter"),
            ("Je leest een klein etiket vlak voor je neus.", "Boller"),
        ],
        "Hoe dichterbij, hoe sterker het licht gebroken moet worden.",
        kolommen=["Boller", "Platter"],
    ),
    tabel(
        "Klopt dit over het oog?",
        [
            ("Het beeld op het netvlies staat op zijn kop.", J),
            ("Beide oogkamers liggen vóór de lens.", J),
            ("De pigmentlaag laat het licht terugkaatsen.", F),
            ("Het glasachtig lichaam houdt het oog bol.", J),
            ("De pupil is een spier in de iris.", F),
        ],
        "De pupil is een opening. De pigmentlaag slikt het licht, zodat het beeld niet wazig wordt.",
    ),
    sleep(
        "Bij bijziendheid is de oogbol te [[lang]] en valt het beeld [[vóór]] het netvlies. Een [[holle]] lens lost dat op.",
        ["kort", "achter", "bolle"],
        "Een holle of negatieve lens verzwakt de breking.",
    ),
    mk(
        "Een verkouden leerling zegt dat zijn soep nergens naar smaakt. Hoe komt dat?",
        [
            "De geur valt weg en die maakt veel van de smaak uit",
            "De zintuigcellen op zijn tong zijn helemaal verdwenen",
            "De soep is door de verkoudheid echt minder gekruid",
            "Zijn hersenen sturen geen bevel meer naar de tong",
        ],
        0,
        "Smaak en geur werken samen. Zit de neus dicht, dan smaakt eten vlak.",
    ),
    keuze(
        "Een wortel groeit de zwaartekracht achterna. Dat is [[*geotropie|fototropie|een nastie]].",
        "De wortel groeit naar de zwaartekracht toe, de stengel ervan weg.",
    ),
    mk(
        "Waarom stuurt elke soort receptor zijn signaal naar een eigen gebied in de hersenen?",
        [
            "Zo weet je welke soort prikkel binnenkomt",
            "Zo kan één receptor alle prikkels opvangen",
            "Zo hoeft er geen conductor meer tussen te zitten",
            "Zo gaat het signaal rechtstreeks naar de spier",
        ],
        0,
        "Daardoor weet je of je licht ziet, geluid hoort of pijn voelt.",
    ),
    klik(
        "Klik op de zenuw die de signalen van het netvlies naar de hersenen brengt.",
        OOG.bestand, [Z_ZENUW],
        "De oogzenuw verlaat het oog op de blinde vlek.",
    ),
    klik(
        "Klik op het oog dat zonder bril scherp ziet in de verte.",
        DRIE.bestand, [PUNT["B"]],
        "Bij een normaal oog komen de stralen van ver precies op het netvlies samen.",
    ),
    klik(
        "Klik op de opening waardoor het licht naar binnen gaat.",
        OOG.bestand, [Z_PUPIL],
        "De pupil is geen onderdeel maar een opening in het midden van de iris.",
    ),
    tabel(
        "Werkt dit bij een plant via hormonen?",
        [
            ("de strekking van cellen in de stengel", J),
            ("de vorming van bijwortels en zijscheuten", J),
            ("elektrische impulsen langs zenuwbanen", F),
            ("de rijping van vruchten", J),
            ("een bevel van de hersenen naar een spier", F),
        ],
        "Een plant heeft geen zenuwen of hersenen. Ze stuurt met hormonen.",
    ),
    keuze(
        "Een plant vangt licht op met [[*fotoreceptoren|mechanoreceptoren|haarcellen]].",
        "Mechanoreceptoren reageren op aanraking, druk of beweging.",
    ),
    open_(
        "Leg uit waarom je de wereld rechtop ziet, ook al valt het beeld omgekeerd op je netvlies. Gebruik de woorden lens, netvlies, oogzenuw en hersenen.",
        "De lens keert het beeld om, zodat het op het netvlies op zijn kop staat. Het netvlies zet het licht om in signalen die via de oogzenuw naar de hersenen gaan. Pas in de hersenen worden die signalen samengelegd en rechtgezet, zodat je de wereld rechtop ziet.",
    ),
]
