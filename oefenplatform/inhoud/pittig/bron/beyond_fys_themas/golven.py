"""Golven en hun eigenschappen — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Momentopname van een lopende golf ----------------------------------------------
LG = Prent("lopende-golf", "Een momentopname van een golf die naar rechts loopt over een touw", "grafiek van de uitwijking in cm tegen de plaats x in m, amplitude 3 cm, golflengte 0,8 m; een pijl naar rechts; punten P (top), Q (evenwichtslijn net rechts van de top), R (dal), S (evenwichtslijn net rechts van het dal)")
X, Y = assen(LG, 0, 2.0, -4, 4, "x (m)", "y (cm)", 0.2, 1, links=130, rechts=900)
pts = [(i / 200 * 2.0, 3 * math.sin(2 * math.pi * (i / 200 * 2.0) / 0.8)) for i in range(201)]
LG.pad("M " + " L ".join(f"{X(a):.1f} {Y(b):.1f}" for a, b in pts), "none", BLAUW, 4)
LG.pijl(X(1.4), Y(3.7), X(1.8), Y(3.7), DONKER, 4)
LG.tekst(X(1.6), Y(3.7) - 12, "loopt naar rechts", 16)
PUNT = {"P": 0.2, "Q": 0.4, "R": 0.6, "S": 0.8}
LP = {}
for k, x in PUNT.items():
    y = 3 * math.sin(2 * math.pi * x / 0.8)
    LG.cirkel(X(x), Y(y), 8, ORANJE, DONKER, 2)
    LP[k] = (X(x) + 30, Y(y) + (-30 if y > 0.1 else 30))
    LG.letter(*LP[k], k)
ZL = {k: [Prent.rond(X(x), Y(3 * math.sin(2 * math.pi * x / 0.8)), 24), Prent.rond(*LP[k], 22)] for k, x in PUNT.items()}

# Breking aan een grensvlak ---------------------------------------------------------
BR = Prent("breking-glas", "Een lichtstraal valt uit de lucht op een glasplaat", "bovenaan lucht, onderaan glas, een gestippelde normaal; een invallende straal van linksboven; onderaan drie mogelijke gebroken stralen A (naar de normaal toe), B (rechtdoor) en C (van de normaal weg); bovenaan een straal D naar rechtsboven")
GY = 330
BR.rect(40, GY, 920, 260, "#dfeef4", DONKER, 0, 2)
BR.tekst(80, 120, "lucht", 22, anker="start", vet=True)
BR.tekst(80, GY + 230, "glas", 22, anker="start", vet=True)
BR.lijn(500, 80, 500, 590, GRIJS, 2, stippel=True)
BR.tekst(512, 100, "normaal", 16, anker="start")
i = math.radians(45)
L = 250
BR.lijn(500 - L * math.sin(i), GY - L * math.cos(i), 500, GY, ROOD, 4)
BR.pijl(500 - 0.55 * L * math.sin(i), GY - 0.55 * L * math.cos(i), 500 - 0.45 * L * math.sin(i), GY - 0.45 * L * math.cos(i), ROOD, 4)
STR = {"A": math.radians(28), "B": math.radians(45), "C": math.radians(65)}
LBR = {}
for k, r in STR.items():
    x2, y2 = 500 + 240 * math.sin(r), GY + 240 * math.cos(r)
    BR.pijl(500, GY, x2, y2, ORANJE, 4)
    LBR[k] = (500 + 275 * math.sin(r), GY + 275 * math.cos(r))
    BR.letter(*LBR[k], k)
xd, yd = 500 + 240 * math.sin(i), GY - 240 * math.cos(i)
BR.pijl(500, GY, xd, yd, ORANJE, 4)
LBR["D"] = (500 + 275 * math.sin(i), GY - 275 * math.cos(i))
BR.letter(*LBR["D"], "D")
ZB = {k: [Prent.rond(500 + 150 * math.sin(r), GY + 150 * math.cos(r), 34), Prent.rond(*LBR[k], 24)] for k, r in STR.items()}
ZB["D"] = [Prent.rond(500 + 150 * math.sin(i), GY - 150 * math.cos(i), 34), Prent.rond(*LBR["D"], 24)]

VRAGEN = [
    klik(
        "Klik op het deeltje dat op dit ogenblik het snelst naar boven beweegt.",
        LG.bestand, ZL["Q"],
        "De top schuift naar rechts op Q af; in de evenwichtsstand is de snelheid het grootst.",
    ),
    klik(
        "Klik op het deeltje dat op dit ogenblik het snelst naar beneden beweegt.",
        LG.bestand, ZL["S"],
        "Het dal schuift naar rechts op S af.",
    ),
    met_prent(LG.bestand, tabel(
        "Hoe beweegt dit deeltje op dit ogenblik?",
        [
            ("P", "Staat even stil"),
            ("Q", "Naar boven"),
            ("S", "Naar beneden"),
        ],
        "In een top of dal keert een deeltje om; daartussen beweegt het mee met wat er aankomt.",
        kolommen=["Naar boven", "Naar beneden", "Staat even stil"],
    )),
    met_prent(LG.bestand, inv(
        "Lees de golflengte af, in m.",
        ["0,8", "0,80", "0,8 m", "0.8"],
        "Van top tot top: 0,2 m tot 1,0 m.",
    )),
    met_prent(LG.bestand, inv(
        "De bron trilt met 5,0 Hz. Hoe snel loopt de golf, in m/s?",
        ["4", "4,0", "4 m/s", "4,0 m/s"],
        "v = λ · f = 0,8 · 5,0 = 4,0 m/s.",
    )),
    met_prent(LG.bestand, keuze(
        "De deeltjes P en R trillen [[*in tegenfase|in fase]].",
        "Ze liggen een halve golflengte uit elkaar.",
    )),
    klik(
        "Klik op de straal die het licht in het glas volgt.",
        BR.bestand, ZB["A"],
        "Glas heeft een grotere brekingsindex: de straal buigt naar de normaal toe.",
    ),
    klik(
        "Klik op de weerkaatste straal.",
        BR.bestand, ZB["D"],
        "De hoek van weerkaatsing is gelijk aan de hoek van inval.",
    ),
    met_prent(BR.bestand, keuze(
        "Gaat het licht omgekeerd van glas naar lucht, dan buigt de straal [[*van de normaal weg|naar de normaal toe]].",
        "In lucht gaat het licht sneller.",
    )),
    met_prent(BR.bestand, mk(
        "Wat blijft gelijk als het licht het glas binnengaat?",
        ["De frequentie", "De snelheid", "De golflengte", "De richting"],
        0,
        "De frequentie komt van de bron; snelheid en golflengte nemen af.",
    )),
    inv(
        "Geluid gaat 340 m/s. Welke golflengte heeft een toon van 680 Hz, in m?",
        ["0,5", "0,50", "0,5 m", "0,50 m", "0.5"],
        "λ = v / f = 340 / 680 = 0,50 m.",
    ),
    mk(
        "Hoe groot is het golfgetal van een golf met λ = 0,50 m?",
        ["12,6 rad/m", "2,0 rad/m", "3,1 rad/m", "0,50 rad/m"],
        0,
        "k = 2π / λ = 4π ≈ 12,6 rad/m.",
    ),
    casus(
        "Een golf volgt y = 0,02 · sin(20π · t − 4π · x), met y en x in meter en t in seconde.",
        [
            inv(
                "Hoe groot is de frequentie van deze golf, in Hz?",
                ["10", "10 Hz"],
                "ω = 20π = 2π · f, dus f = 10 Hz.",
            ),
            inv(
                "Hoe groot is de golflengte, in m?",
                ["0,5", "0,50", "0,5 m", "0.5"],
                "k = 4π = 2π / λ, dus λ = 0,50 m.",
            ),
            inv(
                "Hoe snel loopt de golf, in m/s?",
                ["5", "5,0", "5 m/s"],
                "v = λ · f = 0,50 · 10 = 5,0 m/s.",
            ),
            keuze(
                "Het minteken vóór 4π · x betekent dat de golf naar [[*rechts|links]] loopt.",
                "y = A · sin(ω · t − k · x) is een rechtslopende golf.",
            ),
        ],
    ),
    mk(
        "Licht valt onder 30° uit de lucht (n = 1,0) op glas (n = 1,5). Hoe groot is de brekingshoek ongeveer? (sin 30° = 0,50)",
        ["19°", "30°", "45°", "49°"],
        0,
        "sin r = sin 30° · 1,0 / 1,5 = 0,33, dus r ≈ 19°.",
    ),
    mk(
        "Hoe snel gaat licht in glas met n = 1,5? Neem c = 3,0 · 10⁸ m/s.",
        ["2,0 · 10⁸ m/s", "4,5 · 10⁸ m/s", "3,0 · 10⁸ m/s", "1,5 · 10⁸ m/s"],
        0,
        "v = c / n = 3,0 · 10⁸ / 1,5.",
    ),
    mk(
        "Op een snaar van 1,2 m vormt zich een staande golf met drie buiken. Hoe groot is de golflengte?",
        ["0,80 m", "1,2 m", "0,40 m", "3,6 m"],
        0,
        "Drie buiken zijn drie halve golflengten: 3 · λ/2 = 1,2 m.",
    ),
    inv(
        "Twee opeenvolgende knopen van een staande golf liggen 0,25 m uit elkaar. De golf loopt 100 m/s. Hoe groot is de frequentie, in Hz?",
        ["200", "200 Hz"],
        "λ = 2 · 0,25 = 0,50 m, dus f = 100 / 0,50 = 200 Hz.",
    ),
    mk(
        "Twee coherente bronnen in fase zenden golven met λ = 0,40 m uit. In punt P is het verschil in afstand tot de bronnen 0,60 m. Wat gebeurt er in P?",
        ["Destructieve interferentie", "Constructieve interferentie", "Er komt geen golf aan", "Een staande golf"],
        0,
        "0,60 m is anderhalve golflengte: de golven komen in tegenfase aan.",
    ),
    inv(
        "Een bron trilt al 4,0 s. Een deeltje ligt 6,0 m verder en de golf loopt 2,0 m/s. Hoelang trilt dat deeltje al, in s?",
        ["1", "1,0", "1 s", "1,0 s"],
        "De golf deed 6,0 / 2,0 = 3,0 s over de weg; 4,0 − 3,0 = 1,0 s.",
    ),
    mk(
        "Je laat de bron op hetzelfde touw twee keer zo snel trillen. Wat gebeurt er?",
        ["De golflengte halveert", "De golfsnelheid verdubbelt", "De golflengte verdubbelt", "De amplitude halveert"],
        0,
        "De snelheid hangt van het touw af; bij dubbele f wordt λ de helft.",
    ),
    mk(
        "Welke golf kan zich ook in het luchtledige voortplanten?",
        ["Licht", "Geluid", "Een golf op een touw", "Een watergolf"],
        0,
        "Licht is elektromagnetisch en heeft geen stof nodig.",
    ),
    tabel(
        "Klopt deze uitspraak over golven?",
        [
            ("Een golf neemt materie mee in haar richting.", F),
            ("Twee opeenvolgende knopen liggen een halve golflengte uit elkaar.", J),
            ("Een golf die een stof met grotere n binnengaat, gaat trager.", J),
            ("Coherente bronnen hebben elk een andere frequentie.", F),
        ],
        "Een golf vervoert energie, geen materie.",
    ),
    sorteer(
        "Is deze golf transversaal of longitudinaal?",
        ["Transversaal", "Longitudinaal"],
        [
            ("een golf op een gespannen touw", "Transversaal"),
            ("geluid in de lucht", "Longitudinaal"),
            ("licht", "Transversaal"),
            ("een slinky die je in en uit duwt", "Longitudinaal"),
        ],
        "Transversaal: dwars op de richting. Longitudinaal: langs de richting.",
    ),
    koppel(
        "Koppel elke golfeigenschap aan een voorbeeld.",
        [
            ("weerkaatsing", "een echo in de bergen"),
            ("breking", "een rietje dat geknikt lijkt in een glas water"),
            ("buiging", "muziek horen om de hoek van een gebouw"),
            ("interferentie", "stille plekken tussen twee luidsprekers"),
        ],
        ["een kurk die op en neer danst"],
        "Alle vier verklaar je met het principe van Huygens.",
    ),
    keuze(
        "Constructieve interferentie ontstaat als twee golven [[*in fase|in tegenfase]] aankomen.",
        "De uitwijkingen tellen dan op.",
    ),
    sleep(
        "De golfsnelheid is v = λ · [[f]]. Bij breking blijft de [[frequentie]] gelijk. Een punt van een staande golf dat niet trilt, heet een [[knoop]].",
        ["buik", "amplitude"],
        "Tussen twee knopen ligt een buik.",
    ),
    open_(
        "Leg uit waarom je de lage tonen van een feest om de hoek van een gebouw beter hoort dan de hoge tonen.",
        "Lage tonen hebben een grote golflengte. Hoe groter de golflengte in vergelijking met de opening of de hoek, hoe sterker een golf buigt. De lage tonen buigen dus beter rond het gebouw dan de hoge tonen met hun kleine golflengte.",
    ),
]
