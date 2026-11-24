"""De horizontale worp — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Stroboscoopfoto van een horizontale worp ------------------------------------
SF = Prent("worp-stroboscoop", "Een bal rolt met 3,0 m/s van een tafel van 1,8 m: een foto om de 0,1 s", "raster in meter; de bal vertrekt aan de rand van de tafel op 1,8 m hoogte; zeven posities om de 0,1 s; P na 0,2 s, Q na 0,4 s, R na 0,6 s op de grond")
S = 250  # pixels per meter
OX, OY = 160, 560


def px(x, y):
    return OX + x * S, OY - y * S


for i in range(0, 11):
    xx = i * 0.25
    SF.lijn(OX + xx * S, OY - 1.9 * S, OX + xx * S, OY, "#ececec", 1)
for j in range(0, 10):
    yy = j * 0.2
    SF.lijn(OX - 100, OY - yy * S, OX + 2.5 * S, OY - yy * S, "#ececec", 1)
    SF.tekst(OX - 110, OY - yy * S + 6, f"{yy:.1f}".replace(".", ","), 14, anker="end")
for i in range(0, 5):
    SF.tekst(OX + i * 0.5 * S, OY + 24, f"{i * 0.5:.1f}".replace(".", ","), 14)
SF.tekst(OX + 2.5 * S + 10, OY + 24, "x (m)", 14, anker="start")
SF.tekst(OX - 110, OY - 1.9 * S - 10, "h (m)", 14, anker="end")
SF.rect(OX - 100, OY - 1.8 * S, 100, 14, "#c9a46a", DONKER, 2, 2)
SF.lijn(OX - 90, OY - 1.8 * S + 14, OX - 90, OY, DONKER, 3)
SF.lijn(OX - 10, OY - 1.8 * S + 14, OX - 10, OY, DONKER, 3)
SF.lijn(OX - 120, OY, OX + 2.6 * S, OY, DONKER, 3)
POS = {}
for n in range(7):
    t = n / 10
    x, y = 3.0 * t, 1.8 - 5 * t * t
    X, Y = px(x, y)
    SF.cirkel(X, Y - 10, 10, ORANJE, DONKER, 2)
    POS[n] = (X, Y - 10)
LAB = {"P": 2, "Q": 4, "R": 6}
for k, n in LAB.items():
    SF.letter(POS[n][0] + 32, POS[n][1] - 26, k)
ZS = {k: [Prent.rond(*POS[n], 24), Prent.rond(POS[n][0] + 32, POS[n][1] - 26, 22)] for k, n in LAB.items()}

# Drie worpen ---------------------------------------------------------------------
DW = Prent("drie-worpen", "Drie ballen worden tegelijk horizontaal weggegooid", "drie torens: A is 20 m hoog met een beginsnelheid van 10 m/s, B is 5 m hoog met 15 m/s, C is 20 m hoog met 5 m/s; de banen zijn niet getekend")
WORP = {"A": (20, 10), "B": (5, 15), "C": (20, 5)}
for i, (k, (h, v)) in enumerate(WORP.items()):
    x = 120 + i * 300
    top = 560 - h * 22
    DW.rect(x - 40, top, 80, 560 - top, "#d8d0c0", DONKER, 2, 2)
    DW.cirkel(x + 52, top - 12, 12, ORANJE, DONKER, 2)
    DW.pijl(x + 66, top - 12, x + 66 + v * 6, top - 12, DONKER, 3)
    DW.tekst(x + 70 + v * 3, top - 30, f"{v} m/s", 18, vet=True)
    DW.tekst(x, 590, f"{h} m hoog", 18)
    DW.letter(x - 70, top + 20, k)
DW.lijn(40, 560, 980, 560, DONKER, 3)
ZW = {k: [Prent.zone(120 + i * 300 - 50, 560 - h * 22 - 40, 180, h * 22 + 40), Prent.rond(120 + i * 300 - 70, 560 - h * 22 + 20, 24)] for i, (k, (h, v)) in enumerate(WORP.items())}

VRAGEN = [
    klik(
        "Klik op de positie waar de verticale snelheid 4,0 m/s is. Neem g = 10 m/s².",
        SF.bestand, ZS["Q"],
        "v_y = g · t = 4,0 m/s na 0,4 s.",
    ),
    klik(
        "Klik op de positie waar de bal 0,20 m gezakt is.",
        SF.bestand, ZS["P"],
        "Na 0,2 s: ½ · 10 · 0,04 = 0,20 m. De bal staat daar op 1,6 m hoogte.",
    ),
    met_prent(SF.bestand, tabel(
        "Hoe groot is de verticale snelheid in deze positie? Neem g = 10 m/s².",
        [
            ("P", "2,0 m/s"),
            ("Q", "4,0 m/s"),
            ("R", "6,0 m/s"),
        ],
        "v_y = g · t, met t = 0,2 s, 0,4 s en 0,6 s.",
        kolommen=["2,0 m/s", "4,0 m/s", "6,0 m/s"],
    )),
    met_prent(SF.bestand, keuze(
        "De horizontale afstand tussen twee opeenvolgende posities is [[*overal gelijk|steeds groter|steeds kleiner]].",
        "Horizontaal is het een ERB: x = v₀ · t.",
    )),
    met_prent(SF.bestand, mk(
        "Hoe snel gaat de bal in positie R?",
        ["6,7 m/s", "9,0 m/s", "6,0 m/s", "3,0 m/s"],
        0,
        "v = √(3,0² + 6,0²) = √45 ≈ 6,7 m/s.",
    )),
    klik(
        "Klik op de bal die het verst van zijn toren neerkomt. Neem g = 10 m/s².",
        DW.bestand, ZW["A"],
        "A: t = 2,0 s, x = 20 m. B: t = 1,0 s, x = 15 m. C: t = 2,0 s, x = 10 m.",
    ),
    klik(
        "Klik op de bal die het eerst de grond raakt.",
        DW.bestand, ZW["B"],
        "De valtijd hangt alleen van de hoogte af, en B is het laagst.",
    ),
    met_prent(DW.bestand, tabel(
        "Hoe ver van de toren komt deze bal neer? Neem g = 10 m/s².",
        [
            ("A", "20 m"),
            ("B", "15 m"),
            ("C", "10 m"),
        ],
        "t = √(2h / g), x = v₀ · t.",
        kolommen=["10 m", "15 m", "20 m"],
    )),
    met_prent(DW.bestand, mk(
        "Welke ballen raken tegelijk de grond?",
        ["A en C", "A en B", "B en C", "alle drie"],
        0,
        "Ze vertrekken van dezelfde hoogte; de beginsnelheid speelt geen rol voor de valtijd.",
    )),
    inv(
        "Een steen wordt horizontaal weggeworpen van 45 m hoog. Hoe lang duurt de val, in s? Neem g = 10 m/s².",
        ["3", "3,0", "3 s", "3,0 s"],
        "t = √(2 · 45 / 10) = √9 = 3,0 s.",
    ),
    inv(
        "Diezelfde steen vertrok met 8,0 m/s. Hoe ver komt hij, in m?",
        ["24", "24 m"],
        "x = v₀ · t = 8,0 · 3,0 = 24 m.",
    ),
    mk(
        "Hoe snel gaat die steen (8,0 m/s, 3,0 s vallen, g = 10 m/s²) als hij de grond raakt?",
        ["31 m/s", "38 m/s", "30 m/s", "22 m/s"],
        0,
        "v_y = 30 m/s en v_x = 8,0 m/s: v = √(64 + 900) ≈ 31 m/s.",
    ),
    mk(
        "Je werpt met dezelfde v₀ van een plaats die negen keer zo hoog is. Wat gebeurt er met de dracht?",
        ["Ze wordt 3 keer zo groot", "Ze wordt 9 keer zo groot", "Ze blijft gelijk", "Ze wordt 81 keer zo groot"],
        0,
        "x = v₀ · √(2h / g): de dracht gaat met √h.",
    ),
    mk(
        "Van een muur van 5,0 m wil je een bal horizontaal 12 m ver gooien. Met welke snelheid? Neem g = 10 m/s².",
        ["12 m/s", "6,0 m/s", "24 m/s", "2,4 m/s"],
        0,
        "t = √(2 · 5,0 / 10) = 1,0 s, dus v₀ = 12 / 1,0 = 12 m/s.",
    ),
    inv(
        "Een bal vertrekt horizontaal met 15 m/s. Hoeveel meter is hij gezakt na 30 m horizontaal? Neem g = 10 m/s².",
        ["20", "20 m"],
        "t = 30 / 15 = 2,0 s, dan h = ½ · 10 · 4,0 = 20 m.",
    ),
    inv(
        "Een knikker rolt van een tafel van 1,25 m en komt 1,5 m verder neer. Hoe snel rolde hij van de tafel, in m/s? Neem g = 10 m/s².",
        ["3", "3,0", "3 m/s", "3,0 m/s"],
        "t = √(2 · 1,25 / 10) = 0,50 s, dus v₀ = 1,5 / 0,50 = 3,0 m/s.",
    ),
    mk(
        "Een bal vertrekt horizontaal met 10 m/s. Na hoeveel tijd maakt zijn snelheid 45° met de horizontale? Neem g = 10 m/s².",
        ["1,0 s", "0,5 s", "2,0 s", "1,4 s"],
        0,
        "Bij 45° is v_y = v_x: g · t = 10 m/s, dus t = 1,0 s.",
    ),
    mk(
        "Twee knikkers rollen van dezelfde tafel: de ene met v₀, de andere met 3 · v₀. Hoe verhouden hun drachten zich?",
        ["1 : 3", "1 : 9", "1 : 1", "3 : 1"],
        0,
        "Dezelfde valtijd, dus de dracht is evenredig met v₀.",
    ),
    casus(
        "Een vliegtuig vliegt horizontaal met 50 m/s op 500 m hoogte en laat een hulppakket vallen. Neem g = 10 m/s² en verwaarloos de luchtweerstand.",
        [
            inv(
                "Hoe lang valt het pakket, in s?",
                ["10", "10 s"],
                "t = √(2 · 500 / 10) = √100 = 10 s.",
            ),
            inv(
                "Hoeveel meter vóór het doel moet het pakket losgelaten worden?",
                ["500", "500 m"],
                "x = 50 · 10 = 500 m.",
            ),
            keuze(
                "Als het vliegtuig rechtdoor blijft vliegen, landt het pakket [[*recht onder het vliegtuig|achter het vliegtuig|vóór het vliegtuig]].",
                "Het pakket houdt dezelfde v_x als het vliegtuig.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak, zonder luchtweerstand?",
        [
            ("Een zware en een lichte bal met dezelfde worp komen even ver.", J),
            ("Bij een horizontale worp raakt het voorwerp loodrecht de grond.", F),
            ("De horizontale snelheid blijft de hele vlucht gelijk.", J),
            ("Twee keer zo hoog werpen geeft twee keer zo ver.", F),
        ],
        "De dracht gaat met √h; v_x blijft, dus komt het schuin aan.",
    ),
    sorteer(
        "Blijft deze grootheid constant tijdens de vlucht, of verandert ze?",
        ["Constant", "Verandert"],
        [
            ("de horizontale snelheid v_x", "Constant"),
            ("de versnelling", "Constant"),
            ("de verticale snelheid v_y", "Verandert"),
            ("de grootte van de snelheid v", "Verandert"),
            ("de hoogte", "Verandert"),
        ],
        "Alleen de zwaartekracht werkt, verticaal en constant.",
    ),
    koppel(
        "Koppel elke grootheid aan haar formule bij een horizontale worp.",
        [
            ("valtijd", "√(2h / g)"),
            ("dracht", "v₀ · t"),
            ("verticale snelheid", "g · t"),
            ("snelheid", "√(v_x² + v_y²)"),
        ],
        ["m · g"],
        "Eerst de valtijd, dan de rest.",
    ),
    volgorde(
        "Zet de stappen om een horizontale worp op te lossen in volgorde.",
        [
            "De valtijd uit de hoogte halen",
            "De dracht berekenen met v₀ · t",
            "De verticale snelheid berekenen met g · t",
            "De snelheid bij het neerkomen samenstellen",
        ],
        "De tijd verbindt de twee bewegingen.",
    ),
    keuze(
        "Tijdens de vlucht staat de snelheidsvector altijd [[*raaklijnig aan de baan|loodrecht op de baan|recht naar beneden]].",
        "Hij wijst waar het voorwerp op dat ogenblik heen gaat.",
    ),
    mk(
        "Welke horizontale kracht werkt er op een horizontaal weggeworpen bal, zonder luchtweerstand?",
        [
            "Geen enkele",
            "De kracht van de worp, die afneemt",
            "De kracht van de worp, die gelijk blijft",
            "De zwaartekracht, schuin naar voren",
        ],
        0,
        "De hand werkt niet meer na het loslaten; v_x blijft door traagheid.",
    ),
    sleep(
        "Bij een horizontale worp is de beweging horizontaal een [[ERB]] en verticaal een [[vrije val]]. De baan is een [[parabool]].",
        ["cirkel", "EVRB omhoog"],
        "Dat is het onafhankelijkheidsbeginsel.",
    ),
    open_(
        "Leg uit waarom een kogel die je horizontaal wegschiet tegelijk de grond raakt met een kogel die je op hetzelfde moment van dezelfde hoogte laat vallen.",
        "Volgens het onafhankelijkheidsbeginsel verlopen de horizontale en de verticale beweging los van elkaar. Verticaal vertrekken beide kogels met v_y = 0 en versnellen ze allebei met g. Ze vallen dus even snel en even lang; de horizontale snelheid verandert daar niets aan.",
    ),
    inv(
        "Hoe groot is de verticale snelheid van een horizontaal weggeworpen bal na 1,5 s vlucht, in m/s? Neem g = 10 m/s².",
        ["15", "15 m/s"],
        "v_y = g · t = 10 · 1,5 = 15 m/s, los van de beginsnelheid.",
    ),
]
