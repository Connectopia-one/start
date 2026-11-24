"""De opbouw van de geosfeer — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Doorsnede van de aarde -------------------------------------------------
DA = Prent("doorsnede-aarde", "Doorsnede van de aarde (dikte van de korst overdreven)", "kwart van de aarde met lagen A tot D en diepten")
CX, CY, R = 120, 600, 520
def kwart(r, kleur):
    DA.pad(f"M{CX} {CY} L {CX + r} {CY} A {r} {r} 0 0 0 {CX} {CY - r} Z", kleur, DONKER, 1)
kwart(R, "#a0826d")                       # korst
kwart(R - 22, "#e0a15a")                  # mantel
kwart(R * 3470 / 6370, "#f2c14e")         # buitenkern
kwart(R * 1220 / 6370, "#f6e27a")         # binnenkern
DIEPTE = {"2 900 km": R * 3470 / 6370, "5 100 km": R * 1220 / 6370}
for t, r in DIEPTE.items():
    DA.tekst(CX + r + 6, CY + 24, t, 14, "start")
DA.tekst(CX + R + 6, CY + 24, "0 km", 14, "start")
LET = {"A": (R - 11, 45), "B": ((R - 22 + R * 3470 / 6370) / 2, 45), "C": ((R * 3470 / 6370 + R * 1220 / 6370) / 2, 45), "D": (R * 0.5 * 1220 / 6370, 45)}
ZDA = {}
for k, (r, hoek) in LET.items():
    x, y = CX + r * math.cos(math.radians(hoek)), CY - r * math.sin(math.radians(hoek))
    if k == "A":
        DA.lijn(x, y, x + 120, y - 90, DONKER, 1)
        x, y = x + 140, y - 100
    DA.letter(x, y, k)
    ZDA[k] = [Prent.rond(x, y, 28)]
ZDA["B"].append(Prent.zone(CX + 330, CY - 380, 100, 100))
ZDA["C"].append(Prent.zone(CX + 120, CY - 200, 90, 60))
ZDA["D"].append(Prent.rond(CX + 40, CY - 40, 40))

# Korst op de mantel -----------------------------------------------------
KM = Prent("korst-doorsnede", "Continentale en oceanische korst op de mantel (schematisch)", "doorsnede met oceaan links, continent met gebergte rechts en punten P, Q, R, S")
KM.rect(40, 294, 920, 316, "#e0a15a", "none", 0)             # mantel
KM.tekst(500, 590, "mantel", 18, vet=True)
KM.rect(40, 170, 380, 70, "#9bc1df", "none", 0)              # zeewater
KM.rect(40, 240, 380, 14, "#d9cfa8", "none", 0)              # sediment
KM.rect(40, 254, 380, 40, "#5d5d5d", "none", 0)              # basaltkorst
KM.pad("M420 170 L 600 160 L 700 80 L 780 160 L 960 170 L 960 330 L 860 330 L 780 450 L 700 470 L 620 440 L 560 330 L 420 330 L 420 294 Z", "#c9b48a", DONKER, 2)
KM.pad("M40 294 L 420 294 L 420 330 L 560 330 L 620 440 L 700 470 L 780 450 L 860 330 L 960 330", "none", ROOD, 3)
KM.tekst(920, 360, "Moho", 16, "end", kleur=ROOD)
PQ = {"P": (230, 274), "Q": (230, 205), "R": (700, 380), "S": (500, 250)}
for k, (x, y) in PQ.items():
    KM.letter(x, y, k)
ZKM = {"P": [Prent.zone(40, 254, 380, 40), Prent.rond(*PQ["P"], 24)],
       "Q": [Prent.zone(40, 170, 380, 70), Prent.rond(*PQ["Q"], 24)],
       "R": [Prent.zone(600, 330, 200, 140), Prent.rond(*PQ["R"], 24)],
       "S": [Prent.zone(430, 175, 140, 150), Prent.rond(*PQ["S"], 24)]}

VRAGEN = [
    klik(
        "Klik op de vloeibare laag van de aarde.",
        DA.bestand, ZDA["C"],
        "De buitenkern is vloeibaar, tussen 2 900 en 5 100 km diepte.",
    ),
    klik(
        "Klik op de laag die het grootste deel van het volume van de aarde vult.",
        DA.bestand, ZDA["B"],
        "De mantel is bijna 2 900 km dik.",
    ),
    met_prent(DA.bestand, tabel(
        "Kijk naar de doorsnede. Welke letter hoort bij welke laag?",
        [
            ("korst", "A"),
            ("mantel", "B"),
            ("buitenkern", "C"),
            ("binnenkern", "D"),
        ],
        "Van buiten naar binnen: korst, mantel, buitenkern, binnenkern.",
        kolommen=["A", "B", "C", "D"],
    )),
    met_prent(DA.bestand, tabel(
        "Kijk naar de lagen op de doorsnede. Klopt dit?",
        [
            ("De grens tussen B en C heet de Gütenbergdiscontinuïteit.", J),
            ("De grens tussen A en B heet de Moho.", J),
            ("D is vloeibaar omdat het er het heetst is.", F),
            ("C en D bestaan vooral uit ijzer en nikkel.", J),
        ],
        "De binnenkern blijft vast door de enorme druk.",
    )),
    klik(
        "Klik op de basaltkorst onder de oceaan.",
        KM.bestand, ZKM["P"],
        "De oceanische korst is dun en bestaat vooral uit basalt.",
    ),
    klik(
        "Klik op de wortel van het gebergte.",
        KM.bestand, ZKM["R"],
        "Door isostasie steekt de korst onder een gebergte diep in de mantel.",
    ),
    met_prent(KM.bestand, tabel(
        "Kijk naar korst en mantel op de tekening. Klopt dit?",
        [
            ("De continentale korst is dikker dan de oceanische.", J),
            ("De rode lijn is de grens tussen korst en mantel.", J),
            ("Onder het gebergte is de korst het dunst.", F),
            ("Bovenop de basaltkorst ligt een laag sediment.", J),
        ],
        "Een gebergte heeft een diepe wortel.",
    )),
    tabel(
        "Chemische of fysische indeling?",
        [
            ("korst, mantel en kern", "Chemisch"),
            ("lithosfeer en asthenosfeer", "Fysisch"),
            ("binnenkern en buitenkern", "Fysisch"),
            ("mesosfeer als ondermantel", "Fysisch"),
        ],
        "Chemisch naar samenstelling, fysisch naar stevigheid.",
        kolommen=["Chemisch", "Fysisch"],
    ),
    tabel(
        "Continentale of oceanische korst?",
        [
            ("vooral basalt", "Oceanisch"),
            ("30 tot 70 km dik", "Continentaal"),
            ("nergens ouder dan ongeveer 200 miljoen jaar", "Oceanisch"),
            ("gesteenten van bijna vier miljard jaar", "Continentaal"),
            ("de grootste dichtheid", "Oceanisch"),
        ],
        "Oceanische korst is dun, zwaar en jong.",
        kolommen=["Continentaal", "Oceanisch"],
    ),
    tabel(
        "Klopt dit over de asthenosfeer?",
        [
            ("Ze is kneedbaar en stroomt heel traag.", J),
            ("De lithosfeerplaten schuiven erover.", J),
            ("Ze is volledig vloeibaar magma.", F),
            ("Ze ligt onder de lithosfeer.", J),
        ],
        "Ze is grotendeels vast, maar vervormbaar als heel stijve stroop.",
    ),
    tabel(
        "Klopt dit over seismische golven?",
        [
            ("Dwarsgolven gaan niet door vloeistof.", J),
            ("Ze gaan sneller in dichter gesteente.", J),
            ("Ze veranderen van richting bij een grens tussen lagen.", J),
            ("Dwarsgolven gaan vlot door de buitenkern.", F),
        ],
        "Dat dwarsgolven de buitenkern niet halen, bewijst dat die vloeibaar is.",
    ),
    koppel(
        "Koppel elk begrip aan zijn uitleg.",
        [
            ("seismograaf", "toestel dat bodembewegingen optekent"),
            ("isostasie", "evenwicht van de korst op de mantel"),
            ("lithosfeer", "de korst en de bovenste mantel samen"),
            ("Moho", "grens tussen korst en mantel"),
        ],
        ["grens tussen buiten- en binnenkern"],
        "Die laatste grens ligt op ongeveer 5 100 km.",
    ),
    inv(
        "De straal van de aarde is ongeveer 6 370 km. De kern begint op 2 900 km diepte. Hoeveel km is de straal van de kern ongeveer?",
        ["3470", "3 470"],
        "6 370 - 2 900 = 3 470 km.",
    ),
    inv(
        "De diepste boring haalde ruim 12 km. De continentale korst is daar ongeveer 36 km dik. Hoeveel procent van de korstdikte is dat? Rond af op een geheel getal.",
        ["33"],
        "12 : 36 = een derde, ongeveer 33 %.",
    ),
    casus(
        "Scandinavië stijgt nog altijd enkele millimeters per jaar, ook al is daar geen gebergtevorming meer.",
        [
            keuze(
                "Tijdens de laatste ijstijd drukte een dikke [[*ijskap|zeestroom|lavalaag]] de korst naar beneden.",
                "Die last is weggesmolten.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("De korst veert langzaam terug omhoog.", J),
                    ("Dat is een gevolg van isostasie.", J),
                    ("De korst zakt verder omdat het ijs weg is.", F),
                ],
                "Zoals een ijsberg die hoger komt als je er gewicht af haalt.",
            ),
        ],
    ),
    mk(
        "Een kompasnaald wijst naar het noorden. Welke laag van de aarde zorgt daarvoor?",
        [
            "De buitenkern, waar stromend ijzer werkt als een dynamo",
            "De korst, omdat die overal heel veel magnetisch ijzererts bevat",
            "De atmosfeer, omdat de zonnewind ze elke dag opnieuw oplaadt",
            "De binnenkern, omdat die stilstaat terwijl de rest van de aarde draait",
        ],
        0,
        "Dat veld beschermt ons tegen de zonnewind.",
    ),
    volgorde(
        "Zet de lagen van buiten naar binnen.",
        [
            "Lithosfeer",
            "Asthenosfeer",
            "Ondermantel of mesosfeer",
            "Buitenkern",
            "Binnenkern",
        ],
        "De fysische indeling van de aarde.",
    ),
    sleep(
        "Mohorovicic zag op zijn seismogrammen dat golven op een bepaalde diepte plots [[sneller]] gingen. Zo ontdekte hij de grens tussen [[korst]] en [[mantel]].",
        ["trager", "kern", "atmosfeer"],
        "In dichter gesteente gaan golven sneller.",
    ),
    tabel(
        "Klopt dit over de temperatuur in de aarde?",
        [
            ("Ze neemt toe met de diepte.", J),
            ("De warmte komt deels van het verval van radioactieve stoffen.", J),
            ("De warmte komt deels nog van het ontstaan van de aarde.", J),
            ("Onder de korst wordt het weer koeler.", F),
        ],
        "In een diepe mijn voel je het al.",
    ),
    keuze(
        "Let op: in de geosfeer is de mesosfeer de [[*ondermantel|bovenste luchtlaag|buitenkern]], in de atmosfeer een luchtlaag.",
        "Hetzelfde woord voor twee verschillende dingen.",
    ),
    tabel(
        "Klopt dit over de sedimentlaag op de oceaanbodem?",
        [
            ("Ze ligt bovenop de basaltkorst.", J),
            ("Ze bestaat uit slib, zand en resten van zeeleven.", J),
            ("Ze is het dikst vlak bij de oceanische rug.", F),
        ],
        "Bij de rug is de korst het jongst, dus ligt er nog weinig sediment.",
    ),
    mk(
        "Een seismograaf aan de andere kant van de aarde vangt na een zware beving wel drukgolven op, maar geen dwarsgolven. Wat besluit je daaruit?",
        [
            "Ergens onderweg zit een vloeibare laag",
            "De beving was te zwak om dwarsgolven te maken die zo ver geraken",
            "Dwarsgolven gaan enkel door de oceanen en niet door gesteente",
            "Het toestel stond op een plaats met heel dikke continentale korst",
        ],
        0,
        "Dwarsgolven worden tegengehouden door de vloeibare buitenkern.",
    ),
    mk(
        "Waarom zinkt oceanische korst onder continentale korst als ze botsen?",
        [
            "Ze is zwaarder per kubieke meter",
            "Ze is veel dikker en duwt daardoor naar beneden",
            "Ze is ouder en dus al grotendeels versleten en zacht",
            "Ze ligt onder water en wordt daardoor naar beneden gedrukt",
        ],
        0,
        "Basalt heeft een grotere dichtheid dan granietachtig gesteente.",
    ),
    tabel(
        "Welke diepte hoort erbij?",
        [
            ("grens korst en mantel onder een continent", "ongeveer 35 km"),
            ("grens mantel en kern", "ongeveer 2 900 km"),
            ("grens buitenkern en binnenkern", "ongeveer 5 100 km"),
            ("middelpunt van de aarde", "ongeveer 6 370 km"),
        ],
        "De Moho ligt onder de oceaan al op 5 tot 10 km.",
        kolommen=["ongeveer 35 km", "ongeveer 2 900 km", "ongeveer 5 100 km", "ongeveer 6 370 km"],
    ),
    sorteer(
        "Is dit een kenmerk van de lithosfeer of van de asthenosfeer?",
        ["Lithosfeer", "Asthenosfeer"],
        [
            ("star en breekbaar", "Lithosfeer"),
            ("bevat de korst", "Lithosfeer"),
            ("vervormbaar", "Asthenosfeer"),
            ("trage stroming", "Asthenosfeer"),
            ("in platen verdeeld", "Lithosfeer"),
        ],
        "De platen drijven op de vervormbare laag eronder.",
    ),
    inv(
        "De Marianentrog is ongeveer 11 km diep, de Kola-boring haalde ongeveer 12 km. Hoeveel km is dat samen, als je beide afstanden optelt?",
        ["23"],
        "11 + 12 = 23 km, nog altijd een klein stukje van 6 370 km.",
    ),
    keuze(
        "Een gebergte steekt hoog boven de omgeving uit. Onder dat gebergte is de korst [[*dikker|dunner|even dik]] dan onder een vlakte.",
        "Zoals een ijsberg: wat hoog uitsteekt, steekt ook diep onder water.",
    ),
    tabel(
        "Klopt dit over de binnenkern?",
        [
            ("Ze is vast.", J),
            ("De druk is er het grootst.", J),
            ("Ze is kouder dan de korst.", F),
            ("Ze bestaat vooral uit ijzer en nikkel.", J),
        ],
        "Het is er zo heet als aan het oppervlak van de zon.",
    ),
    open_(
        "Leg uit hoe we weten dat de buitenkern van de aarde vloeibaar is, hoewel niemand er ooit geweest is.",
        "Bij een aardbeving gaan seismische golven door de aarde. Dwarsgolven gaan enkel door vaste stof. Aan de andere kant van de aarde komen ze niet aan, er is een schaduwzone. Dus moeten ze ergens door vloeistof geraakt zijn: de buitenkern.",
    ),
]
