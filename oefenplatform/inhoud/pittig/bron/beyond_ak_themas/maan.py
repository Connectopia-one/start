"""De maan, getijden en verduisteringen — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Maan in vier standen ---------------------------------------------------
MS = Prent("maan-vier-standen", "De maan rond de aarde, van boven de noordpool gezien", "aarde in het midden, zonlicht van links, maan in standen A tot D")
CX, CY, R = 560, 340, 200
for y in range(120, 580, 70):
    MS.pijl(60, y, 180, y, "#e8c547", 3)
MS.tekst(120, 100, "zonlicht", 18)
MS.cirkel(CX, CY, R, "none", GRIJS, 1)
MS.cirkel(CX, CY, 48, "#9bc1df", DONKER)
MS.pad(f"M{CX} {CY - 48} A 48 48 0 0 1 {CX} {CY + 48} Z", "#2c3e50", "none")
MS.tekst(CX, CY + 80, "aarde", 16)
ST = {"A": (CX - R, CY), "B": (CX, CY + R), "C": (CX + R, CY), "D": (CX, CY - R)}
for k, (x, y) in ST.items():
    MS.cirkel(x, y, 22, "#e6e1d3", DONKER)
    MS.pad(f"M{x} {y - 22} A 22 22 0 0 1 {x} {y + 22} Z", "#3a3a3a", "none")
LP = {"A": (CX - R - 10, CY - 55), "B": (CX + 55, CY + R + 10), "C": (CX + R + 55, CY), "D": (CX + 55, CY - R - 10)}
for k, (x, y) in LP.items():
    MS.letter(x, y, k)
a1, a2 = math.radians(150), math.radians(120)
MS.pad(f"M{CX + (R + 40) * math.cos(a1):.0f} {CY + (R + 40) * math.sin(a1):.0f} A {R + 40} {R + 40} 0 0 0 {CX + (R + 40) * math.cos(a2):.0f} {CY + (R + 40) * math.sin(a2):.0f}", "none", DONKER, 2)
ex, ey = CX + (R + 40) * math.cos(a2), CY + (R + 40) * math.sin(a2)
MS.pijl(ex - 14, ey - 8, ex + 2, ey + 1, DONKER, 2)
MS.tekst(CX - 220, CY + 220, "zin van de omloop", 15)
ZMS = {k: [Prent.rond(*ST[k], 32), Prent.rond(*LP[k], 26)] for k in ST}

# Zonsverduistering -------------------------------------------------------
ZV = Prent("zonsverduistering", "Een zonsverduistering (niet op schaal)", "zon, maan en aarde met kernschaduw en bijschaduw, punten P, Q en R op aarde")
SX, SY, SR = 170, 320, 130
MX, MY, MR = 520, 320, 24
EX, EY, ER = 860, 320, 110
ZV.pad(f"M{MX} {MY - MR} L {EX - 20} {EY - 90} L {EX - 20} {EY + 90} L {MX} {MY + MR} Z", "#d6d6d6", "none")
ZV.pad(f"M{MX} {MY - MR} L {EX - ER + 8} {EY} L {MX} {MY + MR} Z", "#555555", "none")
ZV.cirkel(SX, SY, SR, "#f4c542", DONKER)
ZV.cirkel(MX, MY, MR, "#bdbdbd", DONKER)
ZV.cirkel(EX, EY, ER, "#9bc1df", DONKER)
ZV.tekst(SX, SY + SR + 36, "zon", 18)
ZV.tekst(MX, MY + 60, "maan", 18)
ZV.tekst(EX, EY + ER + 36, "aarde", 18)
PQ = {"P": (EX - ER + 4, EY), "Q": (EX - ER + 25, EY - 65), "R": (EX + 20, EY - ER + 6)}
for k, (x, y) in PQ.items():
    ZV.cirkel(x, y, 7, ORANJE, DONKER)
LPQ = {"P": (EX - ER - 50, EY + 40), "Q": (EX - ER - 20, EY - 120), "R": (EX + 70, EY - ER - 30)}
for k, (x, y) in LPQ.items():
    ZV.letter(x, y, k)
ZZV = {k: [Prent.rond(*PQ[k], 18), Prent.rond(*LPQ[k], 26)] for k in PQ}

VRAGEN = [
    klik(
        "Klik op de stand bij nieuwe maan.",
        MS.bestand, ZMS["A"],
        "De maan staat tussen aarde en zon en keert ons haar donkere kant toe.",
    ),
    klik(
        "Klik op de stand bij volle maan.",
        MS.bestand, ZMS["C"],
        "De aarde staat tussen zon en maan: je kijkt recht op de verlichte kant.",
    ),
    klik(
        "Klik op de stand bij het eerste kwartier.",
        MS.bestand, ZMS["B"],
        "Na nieuwe maan komt in de zin van de omloop het eerste kwartier.",
    ),
    met_prent(MS.bestand, tabel(
        "Kijk naar de standen. Klopt dit?",
        [
            ("In A en C is er springtij.", J),
            ("In B en D is er doodtij.", J),
            ("Een zonsverduistering kan enkel in stand C.", F),
            ("Een maansverduistering kan enkel in stand C.", J),
        ],
        "Zonsverduistering bij nieuwe maan (A), maansverduistering bij volle maan (C).",
    )),
    met_prent(MS.bestand, keuze(
        "In stand D zie je het [[*laatste kwartier|eerste kwartier|volle maan]].",
        "Na volle maan krimpt de maan tot een halve: het laatste kwartier.",
    )),
    klik(
        "Klik op een plaats op aarde waar de zon volledig bedekt is.",
        ZV.bestand, ZZV["P"],
        "In de kernschaduw is de verduistering totaal.",
    ),
    klik(
        "Klik op een plaats waar je een gedeeltelijke zonsverduistering ziet.",
        ZV.bestand, ZZV["Q"],
        "In de bijschaduw zie je maar een deel van de zon bedekt.",
    ),
    met_prent(ZV.bestand, tabel(
        "Kijk naar de tekening. Klopt dit?",
        [
            ("Op plaats R zie je geen verduistering.", J),
            ("De kernschaduw raakt maar een kleine strook van de aarde.", J),
            ("Het is nu volle maan.", F),
            ("De maan staat tussen de zon en de aarde.", J),
        ],
        "Een zonsverduistering kan enkel bij nieuwe maan.",
    )),
    tabel(
        "Sterrenmaand of schijngestaltenmaand?",
        [
            ("ongeveer 27,3 dagen", "Sterrenmaand"),
            ("ongeveer 29,5 dagen", "Schijngestaltenmaand"),
            ("van nieuwe maan tot nieuwe maan", "Schijngestaltenmaand"),
            ("één omloop ten opzichte van de sterren", "Sterrenmaand"),
        ],
        "De aarde schuift intussen op rond de zon, dus de maan moet een stukje extra afleggen.",
        kolommen=["Sterrenmaand", "Schijngestaltenmaand"],
    ),
    tabel(
        "Klopt dit over de gebonden rotatie?",
        [
            ("De maan draait één keer om haar as per omloop.", J),
            ("Daardoor zien we altijd dezelfde kant.", J),
            ("De achterkant krijgt nooit zonlicht.", F),
            ("De maan draait niet om haar as.", F),
        ],
        "De achterkant krijgt evenveel zon, je ziet ze enkel niet van op aarde.",
    ),
    tabel(
        "Eb, vloed, hoogtij of laagtij?",
        [
            ("het water komt op", "Vloed"),
            ("het water zakt", "Eb"),
            ("het water staat het hoogst", "Hoogtij"),
            ("het water staat het laagst", "Laagtij"),
        ],
        "Eb en vloed zijn bewegingen, hoog- en laagtij momenten.",
        kolommen=["Eb", "Vloed", "Hoogtij", "Laagtij"],
    ),
    tabel(
        "Springtij of doodtij?",
        [
            ("bij volle maan", "Springtij"),
            ("bij het eerste kwartier", "Doodtij"),
            ("zon en maan in een rechte hoek gezien van de aarde", "Doodtij"),
            ("zon, aarde en maan op één lijn", "Springtij"),
        ],
        "Op één lijn versterken de aantrekkingen elkaar.",
        kolommen=["Springtij", "Doodtij"],
    ),
    inv(
        "Op een dag is het hoogtij om 6 uur 's morgens. Hoe laat is het ongeveer het volgende hoogtij? Rond af op een heel uur.",
        ["18", "18 uur", "18u"],
        "Er is ongeveer twee keer hoogtij per etmaal, dus ruim 12 uur later.",
    ),
    mk(
        "Waarom is er niet elke maand een zonsverduistering?",
        [
            "De maanbaan helt ongeveer 5° op de aardbaan",
            "De maan is meestal te ver weg om de zon te bedekken",
            "De zon draait om haar as en kijkt dan de andere kant op",
            "Bij nieuwe maan staat de maan altijd achter de aarde",
        ],
        0,
        "Meestal gaat de maan net boven of onder de zon door.",
    ),
    tabel(
        "Zonsverduistering of maansverduistering?",
        [
            ("de maan schuift voor de zon", "Zonsverduistering"),
            ("de maan valt in de aardschaduw", "Maansverduistering"),
            ("op het hele nachtelijke halfrond te zien", "Maansverduistering"),
            ("totaal enkel in een smalle strook", "Zonsverduistering"),
            ("de maan kleurt roodachtig", "Maansverduistering"),
        ],
        "Bij een maansverduistering staat de aarde tussen zon en maan.",
        kolommen=["Zonsverduistering", "Maansverduistering"],
    ),
    casus(
        "Een astronaut loopt op de maan. Ze springt met haar zware pak gemakkelijk een meter hoog en ziet haar voetstappen scherp in het stof.",
        [
            keuze(
                "Ze springt zo gemakkelijk omdat de zwaartekracht er ongeveer [[*een zesde|de helft|een tiende]] is van die op aarde.",
                "Alles weegt er ongeveer zes keer minder.",
            ),
            tabel(
                "Waarom blijven haar voetstappen er heel lang liggen?",
                [
                    ("er waait geen wind", J),
                    ("er valt geen neerslag", J),
                    ("de maan heeft geen zwaartekracht", F),
                    ("er is bijna geen erosie", J),
                ],
                "Zonder atmosfeer is er geen wind, regen of erosie.",
            ),
        ],
    ),
    inv(
        "De maan schuift per dag ongeveer 13° op. Hoeveel minuten later komt ze daardoor ongeveer op? Rond af op tientallen.",
        ["50"],
        "Bij 4 minuten per graad: 13 · 4 = 52, ongeveer 50 minuten.",
    ),
    tabel(
        "Klopt dit over de maan?",
        [
            ("Ze straalt zelf licht uit.", F),
            ("Er zit ijs in kraters bij de polen.", J),
            ("De donkere vlakten zijn gestolde lava.", J),
            ("Ze heeft een dikke atmosfeer met wolken.", F),
        ],
        "De maan weerkaatst enkel zonlicht en heeft bijna geen atmosfeer.",
    ),
    volgorde(
        "Zet de schijngestalten in de juiste volgorde, te beginnen na volle maan.",
        [
            "Volle maan",
            "Afnemende maan",
            "Laatste kwartier",
            "Nieuwe maan",
            "Eerste kwartier",
        ],
        "Na volle maan neemt het verlichte deel af tot nieuwe maan, daarna wast ze weer.",
    ),
    sleep(
        "De zon is ongeveer [[400]] keer groter dan de maan, maar staat ook ongeveer 400 keer [[verder]]. Daarom lijken ze aan de hemel ongeveer [[even groot]].",
        ["4", "dichter", "half zo groot"],
        "Daardoor kan de maan de zon net helemaal bedekken.",
    ),
    tabel(
        "Klopt dit over een getijdencentrale?",
        [
            ("Ze werkt op het binnen- en buitenstromen van het water.", J),
            ("Ze levert voorspelbare energie.", J),
            ("Ze werkt op de wind boven de zee.", F),
        ],
        "Eb en vloed zijn op voorhand te berekenen.",
    ),
    met_prent(MS.bestand, tabel(
        "Kijk naar de standen. Welke schijngestalte hoort bij welke stand?",
        [
            ("nieuwe maan", "A"),
            ("eerste kwartier", "B"),
            ("volle maan", "C"),
            ("laatste kwartier", "D"),
        ],
        "In de zin van de omloop: A, B, C, D.",
        kolommen=["A", "B", "C", "D"],
    )),
    met_prent(ZV.bestand, keuze(
        "Het donkere deel van de schaduw achter de maan heet de [[*kernschaduw|bijschaduw|aardschaduw]].",
        "In de bijschaduw is de zon maar gedeeltelijk bedekt.",
    )),
    inv(
        "Hoeveel kilometer staat de maan gemiddeld van de aarde? Rond af op duizenden.",
        ["384000", "384 000"],
        "Gemiddeld ongeveer 384 400 km.",
    ),
    tabel(
        "Klopt dit over de getijden?",
        [
            ("Er zijn twee getijdenbulten op aarde.", J),
            ("De maan trekt sterker aan het water dan de zon.", J),
            ("De zon speelt geen enkele rol.", F),
            ("Een kust draait per etmaal twee keer door een bult.", J),
        ],
        "De zon werkt ongeveer half zo sterk als de maan mee.",
    ),
    keuze(
        "Bij een totale maansverduistering ziet de maan er vaak [[*roodachtig|felwit|groen]] uit.",
        "Zonlicht buigt door onze atmosfeer, het blauwe licht wordt verstrooid en het rode bereikt de maan.",
    ),
    tabel(
        "Klopt dit over de maanbaan?",
        [
            ("Ze is een ellips.", J),
            ("Ze helt ongeveer 5° op het eclipticavlak.", J),
            ("De maan draait van oost naar west rond de aarde.", F),
        ],
        "De maan draait van west naar oost, in dezelfde zin als de aarde.",
    ),
    tabel(
        "Een totale zonsverduistering kan enkel als dit klopt:",
        [
            ("het is nieuwe maan", J),
            ("de maan staat dicht bij een knoop van haar baan", J),
            ("het is volle maan", F),
        ],
        "Enkel dan staan zon, maan en aarde echt op één lijn.",
    ),
    open_(
        "Leg uit waarom een totale maansverduistering op veel meer plaatsen te zien is dan een totale zonsverduistering.",
        "Bij een maansverduistering valt de maan in de schaduw van de aarde. Iedereen die de maan op dat moment ziet, dus het hele nachtelijke halfrond, ziet de verduistering. Bij een zonsverduistering is de kernschaduw van de kleine maan maar een smalle strook op aarde.",
    ),
]
