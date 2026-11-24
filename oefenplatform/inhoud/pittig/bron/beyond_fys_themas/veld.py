"""De wet van Coulomb en het elektrisch veld — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Dipoolveld met berekende veldlijnen --------------------------------------
DV = Prent("dipoolveld", "Veldlijnen tussen een positieve en een negatieve puntlading", "veldlijnen die vertrekken bij een positieve lading links en aankomen bij een negatieve lading rechts; drie punten A (midden tussen de ladingen), B (boven het midden) en C (linksonder, ver weg)")
QP, QN = (330, 330), (670, 330)


def _veld(x, y):
    ex = ey = 0.0
    for (qx, qy), s in ((QP, 1), (QN, -1)):
        dx, dy = x - qx, y - qy
        r3 = (dx * dx + dy * dy) ** 1.5
        ex += s * dx / r3
        ey += s * dy / r3
    return ex, ey


for i in range(16):
    hoek = 2 * math.pi * (i + 0.5) / 16
    x, y = QP[0] + 24 * math.cos(hoek), QP[1] + 24 * math.sin(hoek)
    pts = [(x, y)]
    for _ in range(2500):
        ex, ey = _veld(x, y)
        n = math.hypot(ex, ey)
        x, y = x + 2.5 * ex / n, y + 2.5 * ey / n
        pts.append((x, y))
        if math.hypot(x - QN[0], y - QN[1]) < 24 or not (15 < x < 985 and 55 < y < 630):
            break
    DV.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", GRIJS, 2)
    m = len(pts) // 2 if len(pts) < 400 else 90
    (a, b), (c, d) = pts[m], pts[m + 6]
    DV.pijl(a, b, c, d, DONKER, 2)
# lijnen die van buitenaf bij de negatieve lading aankomen (achterwaarts getekend)
for i in range(16):
    hoek = 2 * math.pi * (i + 0.5) / 16
    if math.cos(hoek) < 0.2:
        continue
    x, y = QN[0] + 24 * math.cos(hoek), QN[1] + 24 * math.sin(hoek)
    pts = [(x, y)]
    for _ in range(2500):
        ex, ey = _veld(x, y)
        n = math.hypot(ex, ey)
        x, y = x - 2.5 * ex / n, y - 2.5 * ey / n
        pts.append((x, y))
        if math.hypot(x - QP[0], y - QP[1]) < 24 or not (15 < x < 985 and 55 < y < 630):
            break
    if math.hypot(x - QP[0], y - QP[1]) < 24:
        continue
    DV.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", GRIJS, 2)
    (a, b), (c, d) = pts[96], pts[90]
    DV.pijl(a, b, c, d, DONKER, 2)
DV.cirkel(*QP, 22, ROOD, DONKER, 2)
DV.tekst(QP[0], QP[1] + 10, "+", 30, kleur="#ffffff", vet=True)
DV.cirkel(*QN, 22, BLAUW, DONKER, 2)
DV.tekst(QN[0], QN[1] + 10, "−", 30, kleur="#ffffff", vet=True)
PUNT = {"A": (500, 330), "B": (500, 170), "C": (130, 520)}
for k, (x, y) in PUNT.items():
    DV.cirkel(x, y, 7, DONKER, DONKER, 1)
    DV.letter(x + 26, y - 26, k)
ZD = {k: [Prent.rond(x, y, 26), Prent.rond(x + 26, y - 26, 22)] for k, (x, y) in PUNT.items()}

# Drie veldlijnenpatronen ---------------------------------------------------------
DR = Prent("drie-velden", "Drie veldlijnenpatronen", "drie vakken: P een lading met lijnen die naar buiten wijzen, Q twee evenwijdige platen met rechte lijnen van boven naar onder, R een lading met lijnen die naar binnen wijzen; de ladingen zijn grijs zonder teken")
for cx, zin in ((170, 1), (830, -1)):
    DR.rect(cx - 150, 90, 300, 430, "#ffffff", DONKER, 16, 2)
    for i in range(12):
        h = 2 * math.pi * i / 12
        x1, y1 = cx + 24 * math.cos(h), 305 + 24 * math.sin(h)
        x2, y2 = cx + 125 * math.cos(h), 305 + 125 * math.sin(h)
        DR.lijn(x1, y1, x2, y2, GRIJS, 2)
        mx, my = cx + 78 * math.cos(h), 305 + 78 * math.sin(h)
        DR.pijl(mx - zin * 6 * math.cos(h), my - zin * 6 * math.sin(h), mx + zin * 6 * math.cos(h), my + zin * 6 * math.sin(h), DONKER, 2)
    DR.cirkel(cx, 305, 20, "#b9b9b9", DONKER, 2)
DR.rect(350, 90, 300, 430, "#ffffff", DONKER, 16, 2)
DR.rect(385, 175, 230, 14, "#9a9a9a", DONKER, 3, 2)
DR.rect(385, 420, 230, 14, "#9a9a9a", DONKER, 3, 2)
for x in range(405, 600, 32):
    DR.lijn(x, 192, x, 418, GRIJS, 2)
    DR.pijl(x, 296, x, 312, DONKER, 2)
for k, cx in (("P", 170), ("Q", 500), ("R", 830)):
    DR.letter(cx, 570, k)
ZR = {k: [Prent.zone(cx - 150, 90, 300, 430), Prent.rond(cx, 570, 24)] for k, cx in (("P", 170), ("Q", 500), ("R", 830))}

VRAGEN = [
    klik(
        "Klik op het punt waar het elektrisch veld het sterkst is.",
        DV.bestand, ZD["A"],
        "Daar liggen de veldlijnen het dichtst bij elkaar, en beide ladingen trekken in dezelfde zin.",
    ),
    klik(
        "Klik op het punt waar het elektrisch veld het zwakst is.",
        DV.bestand, ZD["C"],
        "Daar liggen de lijnen het verst uit elkaar: ver van beide ladingen.",
    ),
    met_prent(DV.bestand, mk(
        "Je zet een elektron in punt A. In welke zin werkt de kracht erop?",
        [
            "Naar links, naar de positieve lading",
            "Naar rechts, in de zin van de veldlijnen",
            "Naar boven, loodrecht op de lijnen",
            "Er werkt in A geen enkele kracht",
        ],
        0,
        "Op een negatieve lading werkt de kracht tegen de zin van het veld in.",
    )),
    met_prent(DV.bestand, mk(
        "Je verdubbelt beide ladingen. Wat verandert er?",
        [
            "Zelfde patroon, E overal 2 keer zo groot",
            "Het patroon wordt een homogeen veld met rechte lijnen",
            "Zelfde patroon, E overal 4 keer kleiner",
            "De veldlijnen draaien om en lopen van rechts naar links",
        ],
        0,
        "Het veld van elke lading is evenredig met die lading; de vorm blijft dezelfde.",
    )),
    met_prent(DV.bestand, keuze(
        "Op deze tekening kunnen twee veldlijnen elkaar [[*nooit|soms wel]] snijden.",
        "In een snijpunt zou het veld twee zinnen tegelijk hebben.",
    )),
    klik(
        "Klik op het veld van een negatieve puntlading.",
        DR.bestand, ZR["R"],
        "Veldlijnen lopen naar een negatieve lading toe.",
    ),
    klik(
        "Klik op het veld waarin een proeflading overal even grote kracht voelt.",
        DR.bestand, ZR["Q"],
        "Tussen twee evenwijdige platen is het veld homogeen.",
    ),
    met_prent(DR.bestand, tabel(
        "Wat doet E als je in dit veld verder weg gaat van de lading of tussen de platen schuift?",
        [
            ("P", "Wordt kleiner"),
            ("Q", "Blijft gelijk"),
            ("R", "Wordt kleiner"),
        ],
        "Rond een puntlading geldt E ~ 1/r²; tussen platen is E constant.",
        kolommen=["Wordt kleiner", "Blijft gelijk", "Wordt groter"],
    )),
    met_prent(DR.bestand, keuze(
        "In vak Q is de bovenste plaat [[*positief|negatief]] geladen.",
        "De veldlijnen vertrekken bij de positieve plaat.",
    )),
    inv(
        "Bereken F tussen 2,0 µC en 5,0 µC op 0,30 m van elkaar. Neem k = 9,0 · 10⁹ N·m²/C². Antwoord in N.",
        ["1", "1,0", "1 N", "1,0 N"],
        "F = 9,0 · 10⁹ · 2,0 · 10⁻⁶ · 5,0 · 10⁻⁶ / 0,30² = 0,090 / 0,090 = 1,0 N.",
    ),
    mk(
        "Twee ladingen trekken elkaar aan met 12 N. Je verdrievoudigt één lading en halveert de afstand. Hoe groot is F nu?",
        ["144 N", "72 N", "18 N", "36 N"],
        0,
        "Drie keer de lading geeft ×3, halve afstand geeft ×4: 12 · 3 · 4 = 144 N.",
    ),
    mk(
        "Twee ladingen stoten elkaar af met 27 N. Je zet ze drie keer zo ver uit elkaar. Hoe groot is F nu?",
        ["3,0 N", "9,0 N", "81 N", "13,5 N"],
        0,
        "Drie keer zo ver geeft 3² = 9 keer minder: 27 / 9 = 3,0 N.",
    ),
    tabel(
        "Met welke factor verandert F tussen twee puntladingen?",
        [
            ("de afstand wordt 2 keer zo groot", "÷ 4"),
            ("beide ladingen worden 2 keer zo groot", "× 4"),
            ("één lading wordt de helft", "÷ 2"),
            ("de afstand wordt de helft", "× 4"),
        ],
        "F is evenredig met elke lading en omgekeerd evenredig met r².",
        kolommen=["× 4", "÷ 2", "÷ 4"],
    ),
    inv(
        "Hoe groot is E op 0,20 m van een puntlading van 4,0 nC? Neem k = 9,0 · 10⁹ N·m²/C². Antwoord in N/C.",
        ["900", "900 N/C", "9 · 10²", "9,0 · 10²"],
        "E = k · q / r² = 9,0 · 10⁹ · 4,0 · 10⁻⁹ / 0,040 = 36 / 0,040 = 900 N/C.",
    ),
    inv(
        "Op welke afstand van een puntlading van 2,0 nC is E = 450 N/C? Neem k = 9,0 · 10⁹ N·m²/C². Antwoord in m.",
        ["0,2", "0,20", "0,2 m", "0,20 m", "0.2"],
        "r² = k · q / E = 18 / 450 = 0,040 m², dus r = 0,20 m.",
    ),
    mk(
        "In punt P is E = 3,0 · 10⁴ N/C, gemeten met een proeflading van 2 µC. Je neemt een proeflading van 6 µC. Hoe groot is E nu?",
        ["3,0 · 10⁴ N/C", "9,0 · 10⁴ N/C", "1,0 · 10⁴ N/C", "1,8 · 10⁵ N/C"],
        0,
        "E hangt niet af van de proeflading: F wordt drie keer groter, F / q blijft gelijk.",
    ),
    mk(
        "Een lading van −2 µC zit in een punt waar E = 500 N/C naar rechts wijst. Welke kracht werkt erop?",
        [
            "1,0 · 10⁻³ N naar links",
            "1,0 · 10⁻³ N naar rechts",
            "2,5 · 10⁸ N naar links",
            "1,0 · 10³ N naar rechts",
        ],
        0,
        "F = E · q = 500 · 2 · 10⁻⁶ = 1,0 · 10⁻³ N, tegen het veld in want de lading is negatief.",
    ),
    mk(
        "Een elektron en een proton zitten in hetzelfde homogene veld. Wat klopt over de elektrische krachten?",
        [
            "Even groot, maar tegengesteld van zin",
            "Op het proton veel groter, want het is zwaarder",
            "Op het elektron veel groter, want het is lichter",
            "Even groot en allebei in de zin van het veld",
        ],
        0,
        "F = E · q en beide dragen een lading e, met een tegengesteld teken.",
    ),
    inv(
        "Op een lading in de hoek van een rechthoek werken twee coulombkrachten loodrecht op elkaar: 3,0 N en 4,0 N. Hoe groot is de resulterende kracht in N?",
        ["5", "5,0", "5 N", "5,0 N"],
        "Vectoren loodrecht optellen: √(3,0² + 4,0²) = 5,0 N.",
    ),
    casus(
        "Een lading van +4 µC staat op 0 cm, een lading van +1 µC op 30 cm. Je zet een kleine proeflading ergens op de lijn ertussen.",
        [
            inv(
                "Op hoeveel cm van de lading van +4 µC is de resulterende kracht op de proeflading nul?",
                ["20", "20 cm"],
                "4 / x² = 1 / (30 − x)² geeft 2 / x = 1 / (30 − x), dus x = 20 cm.",
            ),
            mk(
                "Is dat punt nog altijd het evenwichtspunt als de proeflading negatief is?",
                [
                    "Ja, beide krachten keren om",
                    "Nee, het schuift naar de grote lading",
                    "Nee, het schuift naar de kleine lading",
                    "Nee, voor een negatieve lading bestaat er geen",
                ],
                0,
                "Beide krachten draaien om, maar blijven even groot: ze heffen elkaar nog steeds op.",
            ),
            keuze(
                "Buiten het stuk tussen de twee ladingen ligt er [[*geen|nog een]] punt waar de kracht nul is.",
                "Buiten de ladingen werken beide krachten in dezelfde zin.",
            ),
        ],
    ),
    sorteer(
        "Welk veld hoort bij deze situatie?",
        ["Radiaal", "Homogeen", "Dipoolveld"],
        [
            ("rond één geladen bolletje", "Radiaal"),
            ("tussen twee evenwijdige platen met + en −", "Homogeen"),
            ("rond een + en een − puntlading naast elkaar", "Dipoolveld"),
            ("rond één negatieve puntlading", "Radiaal"),
        ],
        "Een radiaal veld heeft lijnen als de spaken van een wiel.",
    ),
    koppel(
        "Koppel elke grootheid aan haar eenheid.",
        [
            ("kracht F", "N"),
            ("veldsterkte E", "N/C"),
            ("lading q", "C"),
            ("constante k", "N·m²/C²"),
        ],
        ["J/s"],
        "E = F / q, dus newton per coulomb.",
    ),
    tabel(
        "Klopt deze uitspraak over het elektrisch veld?",
        [
            ("De coulombkracht tussen twee ladingen is in water kleiner dan in lucht.", J),
            ("E in een punt hangt af van de proeflading die je er zet.", F),
            ("Een grote lading trekt harder aan een kleine dan omgekeerd.", F),
            ("Binnen in een holle geladen geleider is E nul.", J),
        ],
        "Actie en reactie zijn even groot; E is een eigenschap van de plaats.",
    ),
    mk(
        "Wat hebben de wet van Coulomb en de gravitatiewet gemeen?",
        [
            "Beide zijn omgekeerd evenredig met r²",
            "Beide kunnen zowel aantrekken als afstoten",
            "Beide hangen af van de massa van de voorwerpen",
            "Beide worden sterker als de afstand toeneemt",
        ],
        0,
        "De gravitatie trekt altijd aan; de coulombkracht kan ook afstoten.",
    ),
    mk(
        "Waarom zit je bij onweer vrij veilig in een auto met een metalen koets?",
        [
            "Binnen de metalen koets is er geen veld",
            "De rubberen banden isoleren de auto van de grond",
            "Glas trekt de bliksem weg van de inzittenden",
            "De motor zet de elektrische energie meteen om",
        ],
        0,
        "De koets werkt als een kooi van Faraday: de lading blijft aan de buitenkant.",
    ),
    keuze(
        "Een negatieve lading in een veld dat naar boven wijst, voelt een kracht naar [[*beneden|boven]].",
        "Tegen de zin van het veld in.",
    ),
    sleep(
        "E = F / q is de kracht per [[eenheid van lading]]. Rond een puntlading is E evenredig met [[1/r²]]. Tussen twee evenwijdige platen is het veld [[homogeen]].",
        ["r²", "radiaal", "eenheid van massa"],
        "Zo beschrijf je een veld los van de proeflading.",
    ),
    open_(
        "Leg uit waarom een veldlijnentekening toont waar het veld sterk is, ook al staan er geen getallen op.",
        "Hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het veld daar is. Waar de lijnen uit elkaar wijken, wordt het veld zwakker. De zin van de lijnen toont de richting van de kracht op een positieve lading.",
    ),
]
