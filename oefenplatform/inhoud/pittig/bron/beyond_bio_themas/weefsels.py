"""Celdifferentiatie, weefsels en celtypes — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Doorsnede blad ---------------------------------------------------------
BL = Prent("blad-doorsnede", "Dwarsdoorsnede van een blad", "lagen van boven naar onder: waslaag, bovenhuid, palissadecellen, sponsweefsel met luchtruimten, onderhuid met huidmondje, en een vaatbundel")
BL.rect(60, 100, 880, 10, "#f2e7a0", DONKER, 0, 1)
for i in range(22):
    BL.rect(60 + i * 40, 110, 40, 40, "#eef6e2", DONKER, 0, 1)
for i in range(29):
    x = 60 + i * 30
    BL.rect(x + 2, 152, 26, 120, "#9cc97a", DONKER, 8, 1)
    for j in range(4):
        BL.cirkel(x + 15, 172 + j * 26, 5, "#3f7a2a", "none", 0)
import random
random.seed(4)
for i in range(30):
    x = 80 + (i % 15) * 58 + random.randint(-8, 8)
    y = 310 + (i // 15) * 70 + random.randint(-6, 6)
    BL.ellips(x, y, 24, 18, "#b9dc9c", DONKER, 1)
BL.ellips(560, 340, 70, 55, "#f3efe6", DONKER, 2)
for x, y in ((540, 320), (570, 320), (550, 345), (585, 350)):
    BL.cirkel(x, y, 9, "#5b8bc0", DONKER, 1)
for x, y in ((535, 370), (565, 375), (590, 378)):
    BL.cirkel(x, y, 7, "#c88a5a", DONKER, 1)
for i in range(22):
    x = 60 + i * 40
    if 380 <= x <= 420:
        continue
    BL.rect(x, 420, 40, 36, "#eef6e2", DONKER, 0, 1)
BL.ellips(390, 438, 14, 18, "#9cc97a", DONKER, 1)
BL.ellips(430, 438, 14, 18, "#9cc97a", DONKER, 1)
BL.rect(60, 456, 880, 8, "#f2e7a0", DONKER, 0, 1)
LBL = {"A": (980, 105), "B": (980, 210), "C": (980, 340), "D": (410, 520), "E": (680, 300)}
BL.lijn(940, 105, 958, 105, DONKER, 1)
BL.lijn(940, 210, 958, 210, DONKER, 1)
BL.lijn(940, 340, 958, 340, DONKER, 1)
BL.lijn(410, 498, 410, 452, DONKER, 1)
BL.lijn(658, 305, 625, 325, DONKER, 1)
for k, (x, y) in LBL.items():
    BL.letter(x if x < 970 else 975, y, k)
ZBL = {"A": [Prent.zone(60, 96, 880, 18), Prent.rond(975, 105, 22)],
       "B": [Prent.zone(60, 150, 880, 124), Prent.rond(975, 210, 22)],
       "C": [Prent.zone(60, 280, 460, 130), Prent.zone(640, 280, 300, 130), Prent.rond(975, 340, 22)],
       "D": [Prent.zone(370, 418, 80, 40), Prent.rond(*LBL["D"], 26)],
       "E": [Prent.zone(490, 285, 140, 110), Prent.rond(*LBL["E"], 26)]}

# Celtypes ---------------------------------------------------------------
CT = Prent("celtypes-mens", "Vijf celtypes van de mens (niet op schaal)", "vijf cellen P tot T: schijf zonder kern, cel met lange uitloper, langgerekte cel met strepen, cel met uitsteeksels aan één kant, cel met trilhaartjes")
# P rode bloedcel
CT.ellips(140, 300, 70, 70, "#d9534f", DONKER, 2)
CT.ellips(140, 300, 30, 30, "#e88a87", "none", 0)
# Q zenuwcel
CT.cirkel(300, 300, 35, "#c8a8e0", DONKER, 2)
CT.cirkel(300, 300, 12, PAARS, "none", 0)
for dx, dy in ((-30, -40), (-40, 20), (10, -45)):
    CT.lijn(300 + dx * 0.7, 300 + dy * 0.7, 300 + dx * 1.7, 300 + dy * 1.7, DONKER, 2)
CT.lijn(335, 300, 470, 300, DONKER, 3)
CT.pad("M470 300 l 20 -15 M470 300 l 20 15 M470 300 l 25 0", "none", DONKER, 2)
# R spiercel
CT.rect(540, 260, 160, 80, "#e8a0a0", DONKER, 30, 2)
for x in range(555, 690, 12):
    CT.lijn(x, 265, x, 335, "#b25555", 2)
for x in (580, 640):
    CT.ellips(x, 300, 10, 6, PAARS, "none", 0)
# S darmcel
CT.rect(750, 250, 90, 120, "#f5d9a8", DONKER, 4, 2)
for x in range(755, 840, 9):
    CT.rect(x, 232, 5, 18, "#f5d9a8", DONKER, 2, 1)
CT.cirkel(795, 330, 14, PAARS, "none", 0)
# T trilhaarcel
CT.rect(880, 250, 80, 120, "#cfe3f0", DONKER, 4, 2)
for x in range(885, 960, 9):
    CT.pad(f"M{x} 250 q 4 -12 0 -22 q -4 -10 2 -18", "none", DONKER, 1.5)
CT.cirkel(920, 330, 14, PAARS, "none", 0)
LCT = {"P": (140, 420), "Q": (380, 420), "R": (620, 420), "S": (795, 420), "T": (920, 420)}
for k, (x, y) in LCT.items():
    CT.letter(x, y, k)
ZCT = {"P": [Prent.rond(140, 300, 72)], "Q": [Prent.zone(260, 240, 240, 120)], "R": [Prent.zone(540, 260, 160, 80)],
       "S": [Prent.zone(750, 225, 90, 145)], "T": [Prent.zone(880, 205, 80, 165)]}
for k in ZCT:
    ZCT[k].append(Prent.rond(*LCT[k], 26))

VRAGEN = [
    klik(
        "Klik op de laag met de meeste chloroplasten.",
        BL.bestand, ZBL["B"],
        "Het palissadeparenchym ligt rechtop en dicht opeen onder de bovenhuid.",
    ),
    klik(
        "Klik op de opening waarlangs CO2 het blad binnenkomt.",
        BL.bestand, ZBL["D"],
        "Een huidmondje met twee sluitcellen.",
    ),
    klik(
        "Klik op de vaatbundel.",
        BL.bestand, ZBL["E"],
        "Xyleem en floëem liggen samen in de nerf.",
    ),
    met_prent(BL.bestand, tabel(
        "Kijk naar de doorsnede van het blad. Klopt dit?",
        [
            ("A beperkt het waterverlies.", J),
            ("In C kunnen gassen vlot bewegen tussen de cellen.", J),
            ("D ligt aan de onderkant, waar minder zon en wind is.", J),
            ("B bestaat uit dode cellen.", F),
        ],
        "Palissadecellen zijn levende cellen vol chloroplasten.",
    )),
    klik(
        "Klik op de cel zonder kern.",
        CT.bestand, ZCT["P"],
        "Een rode bloedcel heeft geen kern en dus meer plaats voor hemoglobine.",
    ),
    klik(
        "Klik op de cel die een prikkel over een lange afstand doorgeeft.",
        CT.bestand, ZCT["Q"],
        "Een zenuwcel met een lang axon.",
    ),
    met_prent(CT.bestand, tabel(
        "Kijk naar de vijf celtypes. Welke cel is dit?",
        [
            ("rode bloedcel", "P"),
            ("zenuwcel", "Q"),
            ("spiercel", "R"),
            ("darmcel", "S"),
            ("trilhaarcel", "T"),
        ],
        "De vorm verraadt de taak.",
        kolommen=["P", "Q", "R", "S", "T"],
    )),
    met_prent(CT.bestand, tabel(
        "Kijk naar de cellen. Klopt dit over hun bouw?",
        [
            ("De uitsteeksels van S vergroten het oppervlak voor opname.", J),
            ("T duwt slijm naar boven in de luchtwegen.", J),
            ("R heeft veel mitochondria nodig.", J),
            ("P kan zich nog delen.", F),
        ],
        "Zonder kern is er geen DNA om na te maken.",
    )),
    volgorde(
        "Zet de groei van een plantencel in volgorde.",
        ["Celdeling", "Celstrekking", "Celdifferentiatie"],
        "Bij een dier is er geen strekking: daar volgt na de deling een stamcelstadium.",
    ),
    tabel(
        "Kenmerk van een stamcel of van een gedifferentieerde cel?",
        [
            ("kan nog veel celtypes worden", "Stamcel"),
            ("heeft een vaste vorm en taak", "Gedifferentieerd"),
            ("blijft zich delen", "Stamcel"),
            ("staat vaak stil in de G0-fase", "Gedifferentieerd"),
        ],
        "Bij differentiatie gaan genen aan en uit.",
        kolommen=["Stamcel", "Gedifferentieerd"],
    ),
    tabel(
        "Welk plantenweefsel is dit?",
        [
            ("vervoert water van wortel naar blad", "xyleem"),
            ("vervoert suikers naar de rest van de plant", "floëem"),
            ("dode cellen met verhoute wand voor stevigheid", "sclerenchym"),
            ("levende cellen die stoffen opslaan", "parenchym"),
        ],
        "Xyleem en floëem samen heten transportweefsel.",
        kolommen=["xyleem", "floëem", "sclerenchym", "parenchym"],
    ),
    tabel(
        "Welk dierlijk weefsel is dit?",
        [
            ("bedekt de binnenkant van de darm", "epitheel"),
            ("kraakbeen en bot", "bindweefsel"),
            ("geeft prikkels door", "zenuwweefsel"),
            ("trekt samen", "spierweefsel"),
        ],
        "Vier grote groepen weefsels bij een dier.",
        kolommen=["epitheel", "bindweefsel", "zenuwweefsel", "spierweefsel"],
    ),
    casus(
        "Een tuinder snijdt een stukje stengel van een plant af en zet het in water. Na enkele weken heeft het wortels.",
        [
            keuze(
                "De nieuwe plant is een [[*kloon|hybride|mutant]] van de oude.",
                "Ze heeft precies hetzelfde DNA.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("Plantencellen kunnen weer alles worden.", J),
                    ("De nieuwe plant ontstond zonder bevruchting.", J),
                    ("De nieuwe plant heeft de helft van de chromosomen.", F),
                ],
                "Plantencellen blijven totipotent.",
            ),
        ],
    ),
    mk(
        "Wat gebeurt er met de huidmondjes bij droogte, en wat is het gevolg?",
        [
            "Ze sluiten, waardoor de fotosynthese vertraagt",
            "Ze gaan wijder open om extra water op te kunnen nemen",
            "Ze sluiten, waardoor de plant net sneller gaat groeien",
            "Ze verdwijnen helemaal en komen pas na regen terug",
        ],
        0,
        "Er komt minder CO2 binnen.",
    ),
    koppel(
        "Koppel elke bouw aan de functie die erbij past.",
        [
            ("wortelharen", "groot oppervlak voor wateropname"),
            ("microvilli", "groot oppervlak voor opname van voedingsstoffen"),
            ("cuticula", "beperkt het waterverlies"),
            ("trilharen", "duwen slijm naar boven"),
        ],
        ["maakt hemoglobine aan"],
        "Bouw en functie horen bij elkaar.",
    ),
    tabel(
        "Klopt dit over xyleemcellen?",
        [
            ("Ze zijn bij volle werking dood.", J),
            ("Ze vormen holle buizen.", J),
            ("Hun wand is verstevigd.", J),
            ("Ze vervoeren vooral suikers.", F),
        ],
        "Suikers gaan via het floëem.",
    ),
    sleep(
        "Elke lichaamscel heeft hetzelfde [[DNA]]. Wat een cel tot spiercel maakt, is welke [[genen]] aan staan. Dat proces heet [[differentiatie]].",
        ["eiwit", "organellen", "bevruchting"],
        "Andere genen aan, andere eiwitten, andere cel.",
    ),
    mk(
        "Waarom kan kraakbeen na een blessure zo traag herstellen?",
        [
            "Het heeft geen bloedvaten",
            "Het bestaat enkel uit dode cellen",
            "Het heeft geen stamcellen nodig",
            "Het wordt elke nacht volledig vernieuwd",
        ],
        0,
        "De cellen krijgen hun stoffen traag via diffusie.",
    ),
    tabel(
        "Haploïd of diploïd?",
        [
            ("eicel", "Haploïd"),
            ("huidcel", "Diploïd"),
            ("zaadcel", "Haploïd"),
            ("levercel", "Diploïd"),
        ],
        "Geslachtscellen hebben 23 chromosomen, lichaamscellen 46.",
        kolommen=["Haploïd", "Diploïd"],
    ),
    tabel(
        "Waarvoor kan stamceltherapie gebruikt worden?",
        [
            ("nieuwe bloedcellen laten aanmaken", J),
            ("beschadigd weefsel vervangen", J),
            ("een virusinfectie meteen genezen", F),
        ],
        "Bijvoorbeeld bij leukemie, met beenmergstamcellen.",
    ),
    keuze(
        "Cellen in de worteltop die zich blijven delen, heten [[*meristeemcellen|sclerenchymcellen|xyleemcellen]].",
        "Meristeem is het delingsweefsel van een plant.",
    ),
    tabel(
        "Klopt dit over een vaatbundel?",
        [
            ("Er liggen xyleem en floëem in.", J),
            ("Er ligt ook steunweefsel bij.", J),
            ("Zo gaan transport en stevigheid samen.", J),
            ("Een vaatbundel komt ook bij dieren voor.", F),
        ],
        "Bij dieren vervoeren bloed en lymfe de stoffen.",
    ),
    mk(
        "Een onderzoeker ziet lange buizen van cellen zonder inhoud, met een dikke wand. Waar komt dat staal waarschijnlijk vandaan?",
        [
            "Uit het hout van een stengel",
            "Uit het epitheel van de darm",
            "Uit een spier van een been",
            "Uit het palissadeweefsel van een blad",
        ],
        0,
        "Xyleem of houtvaten.",
    ),
    tabel(
        "Klopt dit over wortel en stengel?",
        [
            ("De cortex brengt water naar de vaatbundel.", J),
            ("De stengel brengt de bladeren naar het licht.", J),
            ("Wortelharen zijn uitlopers van één cel.", J),
            ("De wortel doet aan fotosynthese.", F),
        ],
        "Wortels zitten in het donker.",
    ),
    inv(
        "Een zenuwcel heeft een axon van 0,9 m. De cel zelf is 0,1 mm breed. Hoeveel keer langer is het axon dan de cel breed is?",
        ["9000", "9 000"],
        "0,9 m = 900 mm; 900 : 0,1 = 9 000.",
    ),
    tabel(
        "Klopt dit over een kloon?",
        [
            ("Ze heeft hetzelfde DNA als haar ouder.", J),
            ("Een uitloper van een aardbei is een kloon.", J),
            ("Een kloon ontstaat altijd na bevruchting.", F),
        ],
        "Klonen is ongeslachtelijke voortplanting.",
    ),
    keuze(
        "Een spons van cellen met grote luchtruimten tussen, in een blad, heet het [[*sponsparenchym|palissadeparenchym|collenchym]].",
        "Daar bewegen CO2, zuurstof en waterdamp.",
    ),
    tabel(
        "Klopt dit over een rode bloedcel van de mens?",
        [
            ("Ze heeft geen kern.", J),
            ("Ze zit vol hemoglobine.", J),
            ("Nieuwe rode bloedcellen komen uit stamcellen in het beenmerg.", J),
            ("Ze heeft veel mitochondria.", F),
        ],
        "Zonder organellen is er maximaal plaats voor hemoglobine.",
    ),
    open_(
        "Leg uit waarom een rode bloedcel en een zenuwcel er zo verschillend uitzien, terwijl ze hetzelfde DNA hebben.",
        "Bij de differentiatie staan in elke cel andere genen aan. Een rode bloedcel maakt veel hemoglobine en verliest haar kern, zodat er veel plaats is voor zuurstoftransport. Een zenuwcel krijgt een lang axon om prikkels over grote afstand door te geven. De vorm past bij de taak.",
    ),
]
