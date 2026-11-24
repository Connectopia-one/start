"""Aardbevingen en vulkanisme — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Doorsnede stratovulkaan ------------------------------------------------
VD = Prent("vulkaan-doorsnede", "Doorsnede van een stratovulkaan", "vulkaan met magmakamer, schoorsteen, krater en zijschoorsteen, letters A tot D")
VD.rect(40, 520, 920, 100, "#a0826d", "none", 0, 0)
for i, kleur in enumerate(["#8a7a68", "#b8a58a", "#8a7a68", "#b8a58a", "#8a7a68"]):
    d = i * 45
    VD.pad(f"M{120 + d} 520 L {455 + d * 0.15} {130 + d} L {545 - d * 0.15} {130 + d} L {880 - d} 520 Z", kleur, "none", 0)
VD.pad("M120 520 L 455 130 L 545 130 L 880 520", "none", DONKER, 2)
VD.pad("M455 130 L 480 165 L 520 165 L 545 130", "#f3efe6", DONKER, 2)
VD.ellips(500, 570, 150, 40, ROOD, DONKER, 2)
VD.rect(488, 165, 24, 370, ROOD, "none", 0, 0)
VD.pad("M505 380 L 650 300 L 662 318 L 512 400 Z", ROOD, "none", 0)
LVD = {"A": (500, 590), "B": (420, 330), "C": (500, 100), "D": (690, 270)}
VD.lijn(495, 320, 435, 330, DONKER, 1)
VD.lijn(650, 300, 675, 280, DONKER, 1)
for k, (x, y) in LVD.items():
    VD.letter(x, y, k)
ZVD = {"A": [Prent.zone(350, 530, 300, 80), Prent.rond(*LVD["A"], 26)],
       "B": [Prent.zone(480, 170, 40, 360), Prent.rond(*LVD["B"], 26)],
       "C": [Prent.zone(450, 120, 100, 50), Prent.rond(*LVD["C"], 26)],
       "D": [Prent.zone(560, 285, 110, 50), Prent.rond(*LVD["D"], 26)]}

# Seismogram -------------------------------------------------------------
SG = Prent("seismogram-p-s", "Seismogram van één meetstation", "tijdlijn met golven, eerste uitslag bij 2 min, grotere bij 5 min")
SG.lijn(60, 520, 960, 520, DONKER, 2)
for m in range(0, 11):
    x = 80 + m * 85
    SG.lijn(x, 515, x, 525, DONKER, 2)
    SG.tekst(x, 550, str(m), 16)
SG.tekst(510, 590, "tijd na de beving (minuten)", 18)
pts = []
for i in range(0, 851):
    t = i / 85
    a = 2
    if t >= 2:
        a += 25 * math.exp(-(t - 2) * 0.6) + 8
    if t >= 5:
        a += 110 * math.exp(-(t - 5) * 0.7)
    y = 300 + a * math.sin(i * 1.3) * (1 if i % 2 else 0.8)
    pts.append(f"{80 + i:.0f} {y:.1f}")
SG.pad("M" + " L ".join(pts), "none", BLAUW, 1.5)
LSG = {"P": (250, 200), "S": (505, 140)}
SG.lijn(250, 220, 250, 290, DONKER, 1, stippel=True)
SG.lijn(505, 160, 505, 200, DONKER, 1, stippel=True)
for k, (x, y) in LSG.items():
    SG.letter(x, y, k)
ZSG = {"P": [Prent.zone(235, 200, 60, 200), Prent.rond(*LSG["P"], 26)],
       "S": [Prent.zone(490, 120, 70, 360), Prent.rond(*LSG["S"], 26)]}

VRAGEN = [
    klik(
        "Klik op de plaats waar het magma zich verzamelt voor een uitbarsting.",
        VD.bestand, ZVD["A"],
        "Dat is de magmakamer, diep onder de vulkaan.",
    ),
    klik(
        "Klik op de zijschoorsteen.",
        VD.bestand, ZVD["D"],
        "Lava kan ook langs een zijkanaal naar buiten komen.",
    ),
    met_prent(VD.bestand, tabel(
        "Kijk naar de doorsnede van de vulkaan. Klopt dit?",
        [
            ("De vulkaan is opgebouwd uit lagen lava en as.", J),
            ("B is de schoorsteen of pijp.", J),
            ("C ligt aan de voet van de vulkaan.", F),
            ("Dit type vulkaan heeft flauwe hellingen.", F),
        ],
        "Een stratovulkaan is steil; C is de krater bovenaan.",
    )),
    klik(
        "Klik op de aankomst van de snelste golven.",
        SG.bestand, ZSG["P"],
        "De primaire golven komen het eerst aan.",
    ),
    met_prent(SG.bestand, tabel(
        "Kijk naar het seismogram. Klopt dit?",
        [
            ("De P-golven kwamen ongeveer 2 minuten na de beving aan.", J),
            ("Tussen P en S zit ongeveer 3 minuten.", J),
            ("Hoe verder het station van de haard, hoe kleiner dat verschil.", F),
            ("De S-golven geven hier de grootste uitslag.", J),
        ],
        "Hoe verder weg, hoe groter de tijd tussen P en S.",
    )),
    mk(
        "Station 1 meet 1 minuut tussen P en S, station 2 meet 4 minuten. Wat besluit je?",
        [
            "Station 1 ligt dichter bij het epicentrum",
            "Station 2 ligt dichter bij het epicentrum",
            "De beving was bij station 2 vier keer zwaarder",
            "Er waren twee verschillende aardbevingen na elkaar",
        ],
        0,
        "P-golven lopen sneller, dus de voorsprong groeit met de afstand.",
    ),
    tabel(
        "Hypocentrum of epicentrum?",
        [
            ("de haard in de diepte", "Hypocentrum"),
            ("het punt aan het oppervlak erboven", "Epicentrum"),
            ("daar is de schade meestal het grootst", "Epicentrum"),
            ("daar komt de spanning vrij", "Hypocentrum"),
        ],
        "Hypo betekent onder, epi betekent boven.",
        kolommen=["Hypocentrum", "Epicentrum"],
    ),
    tabel(
        "Schildvulkaan of stratovulkaan?",
        [
            ("dunne basaltische lava", "Schildvulkaan"),
            ("steile kegel", "Stratovulkaan"),
            ("explosieve uitbarstingen", "Stratovulkaan"),
            ("Hawaï", "Schildvulkaan"),
            ("boven een subductiezone", "Stratovulkaan"),
        ],
        "Taai magma houdt gas vast en ontploft; dun magma vloeit weg.",
        kolommen=["Schildvulkaan", "Stratovulkaan"],
    ),
    volgorde(
        "Zet het uitgeworpen materiaal van groot naar klein.",
        ["Vulkanische bom", "Lapilli", "Vulkanische as"],
        "As is zo fijn dat ze over een heel werelddeel kan waaien.",
    ),
    inv(
        "Eén stap hoger op de magnitudeschaal geeft ongeveer 32 keer zoveel energie. Hoeveel keer zoveel energie geeft magnitude 7 tegenover magnitude 5? Rond af op een honderdtal.",
        ["1000", "1 000", "1024"],
        "32 x 32 = 1 024, ongeveer 1 000 keer.",
    ),
    mk(
        "Een beving van magnitude 6 treft twee steden even hard. Waarom vallen er in de ene veel meer doden?",
        [
            "De gebouwen zijn er niet bevingsveilig gebouwd",
            "De schaal van Richter meet er een veel hogere waarde",
            "De P-golven zijn daar trager en blijven langer hangen",
            "Het epicentrum verschuift naar de armste stad",
        ],
        0,
        "Ook hulpdiensten, voorbereiding en losse ondergrond spelen mee.",
    ),
    casus(
        "Op 26 december 2004 schoof bij Sumatra de zeebodem plots meters omhoog.",
        [
            keuze(
                "Daardoor ontstond een [[*tsunami|lahar|gloedwolk]].",
                "De hele waterkolom werd opgetild.",
            ),
            tabel(
                "Klopt dit over die golf?",
                [
                    ("Op volle zee was ze laag en heel snel.", J),
                    ("Aan de kust werd ze hoog.", J),
                    ("Ze bleef beperkt tot de kust van Sumatra.", F),
                ],
                "Ze trof kusten tot in Afrika.",
            ),
            keuze(
                "Vlak voor zo'n golf trekt de zee zich vaak [[*eerst terug|eerst hoger op|helemaal niet terug]].",
                "Wie dat ziet, moet meteen hoger gelegen grond zoeken.",
            ),
        ],
    ),
    koppel(
        "Koppel elk vulkanisch gevaar aan de juiste uitleg.",
        [
            ("lahar", "modderstroom van as en water"),
            ("gloedwolk", "razendsnelle wolk van gloeiend gas en as"),
            ("asregen", "fijne as die daken laat bezwijken"),
            ("lavastroom", "gesmolten gesteente dat traag de helling afloopt"),
        ],
        ["tsunami door een onderzeese beving"],
        "Een gloedwolk is het dodelijkst: je kan er niet voor wegvluchten.",
    ),
    tabel(
        "Klopt dit over aardbevingen in België?",
        [
            ("Er zijn af en toe lichte bevingen.", J),
            ("Ze komen voor rond oude breuken, zoals de Roerdalslenk.", J),
            ("België ligt op een plaatgrens.", F),
        ],
        "De breuken bewegen nog een heel klein beetje.",
    ),
    sleep(
        "Een vulkaan in een subductiezone heeft [[taai]] magma met veel [[kiezelzuur]]. Het gas kan niet ontsnappen, dus barst hij [[explosief]] uit.",
        ["dun", "ijzer", "rustig"],
        "Bij een hotspot is het magma basaltisch en dun.",
    ),
    tabel(
        "Klopt dit over het voorspellen van aardbevingen?",
        [
            ("We weten goed in welke gebieden ze voorkomen.", J),
            ("Een waarschuwing kan enkele seconden winnen.", J),
            ("Het precieze uur is vooraf gekend.", F),
        ],
        "Sensoren vangen de P-golven op en waarschuwen voor de S-golven.",
    ),
    mk(
        "Waarom beeft de grond harder in een vallei vol los zand dan op een rotsheuvel ernaast?",
        [
            "Losse grond versterkt de golven",
            "In de vallei ligt het hypocentrum altijd dichter",
            "Op de heuvel komen enkel de P-golven aan",
            "De golven kunnen niet door vast gesteente",
        ],
        0,
        "Daarom bouwt men liefst op vaste rots.",
    ),
    sorteer(
        "Is dit een voordeel of een nadeel van wonen bij een vulkaan?",
        ["Voordeel", "Nadeel"],
        [
            ("vruchtbare grond", "Voordeel"),
            ("aardwarmte", "Voordeel"),
            ("lahars", "Nadeel"),
            ("toerisme", "Voordeel"),
            ("gloedwolken", "Nadeel"),
        ],
        "Daarom wonen er toch miljoenen mensen op de flanken.",
    ),
    tabel(
        "Klopt dit over grote uitbarstingen en het klimaat?",
        [
            ("Zwaveldeeltjes komen tot in de stratosfeer.", J),
            ("Ze weerkaatsen zonlicht.", J),
            ("Het wordt daardoor een tijd koeler.", J),
            ("De aarde warmt daardoor jaren op.", F),
        ],
        "Na Tambora in 1815 volgde een jaar zonder zomer.",
    ),
    keuze(
        "Om het epicentrum te vinden, teken je rond [[*drie|twee|vier]] meetstations een cirkel en zoek je het snijpunt.",
        "Met twee cirkels heb je nog twee mogelijke punten.",
    ),
    mk(
        "In 2010 lag het vliegverkeer boven Europa dagenlang stil. Waarom?",
        [
            "Fijne as uit IJsland kan vliegtuigmotoren doen uitvallen",
            "Een tsunami had de grote luchthavens langs de kust overspoeld",
            "Een zware beving had de landingsbanen in Europa gebroken",
            "Lava uit IJsland stroomde tot aan de Europese kusten",
        ],
        0,
        "De as smelt in een motor en verstopt hem.",
    ),
    tabel(
        "Welke schaal of welk toestel hoort erbij?",
        [
            ("magnitude in de haard", "schaal van Richter"),
            ("zware bevingen het best gemeten", "MMS"),
            ("tekent bodembewegingen op", "seismograaf"),
        ],
        "De seismograaf levert de gegevens voor de schalen.",
        kolommen=["schaal van Richter", "MMS", "seismograaf"],
    ),
    tabel(
        "Magma of lava?",
        [
            ("zit in de magmakamer", "Magma"),
            ("stroomt de helling af", "Lava"),
            ("stijgt op door de schoorsteen", "Magma"),
            ("stolt aan de lucht tot gesteente", "Lava"),
        ],
        "Dezelfde stof: onder de grond magma, erbuiten lava.",
        kolommen=["Magma", "Lava"],
    ),
    keuze(
        "Een schildvulkaan barst meestal [[*rustig|explosief|nooit]] uit, omdat het gas makkelijk uit de dunne lava ontsnapt.",
        "Denk aan de lavastromen op Hawaï.",
    ),
    mk(
        "Waarom ligt het epicentrum vlak boven het hypocentrum en niet ernaast?",
        [
            "Het is per definitie het punt recht erboven",
            "De golven gaan enkel recht omhoog naar het oppervlak",
            "De breuk loopt altijd verticaal naar de oppervlakte",
            "Het hypocentrum ligt altijd vlak onder de korst",
        ],
        0,
        "Het epicentrum is de projectie van de haard op het aardoppervlak.",
    ),
    open_(
        "Leg uit waarom er langs de Ring of Fire zoveel vulkanen en aardbevingen zijn.",
        "Rond de Stille Oceaan duiken oceanische platen onder andere platen. Bij dat schuren haken ze vast en komt spanning vrij: aardbevingen. De duikende plaat smelt in de diepte, het magma stijgt op en vormt vulkanen.",
    ),
    tabel(
        "Klopt dit over naschokken?",
        [
            ("Ze volgen na de hoofdbeving.", J),
            ("Ze zijn meestal lichter.", J),
            ("Ze kunnen al beschadigde gebouwen laten instorten.", J),
            ("Ze komen altijd vóór de hoofdbeving.", F),
        ],
        "Het gesteente zoekt een nieuw evenwicht.",
    ),
    inv(
        "P-golven lopen ongeveer 6 km per seconde. Hoeveel km leggen ze af in 2 minuten?",
        ["720"],
        "120 s x 6 km = 720 km.",
    ),
]
