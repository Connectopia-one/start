"""Klimaatgebieden, biomen en zeestromen — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Drie klimatogrammen -----------------------------------------------------
KG = Prent("drie-klimatogrammen", "Drie klimatogrammen", "drie kleine klimatogrammen A, B en C met temperatuur (lijn) en neerslag (staven)")
DATA = {
    "A": ([26, 26, 27, 27, 27, 26, 26, 26, 27, 27, 27, 26], [250, 240, 260, 280, 220, 180, 170, 180, 200, 230, 240, 260]),
    "B": ([10, 11, 13, 16, 20, 24, 27, 27, 23, 19, 14, 11], [80, 70, 60, 40, 25, 8, 2, 5, 30, 70, 90, 90]),
    "C": ([-20, -18, -10, 0, 8, 14, 17, 14, 7, -2, -12, -18], [20, 18, 20, 25, 40, 60, 70, 65, 45, 35, 25, 22]),
}
for i, (k, (temp, ns)) in enumerate(DATA.items()):
    x0, y0, b, h = 60 + i * 320, 90, 260, 400
    KG.rect(x0, y0, b, h, "#ffffff", GRIJS, 4)
    nul = y0 + h * 0.6
    KG.lijn(x0, nul, x0 + b, nul, GRIJS, 1)
    for m in range(12):
        bx = x0 + 10 + m * 20
        hh = ns[m] * 0.55
        KG.rect(bx, nul - hh, 14, hh, "#9bc1df", "none", 0)
    pts = [(x0 + 17 + m * 20, nul - temp[m] * 6) for m in range(12)]
    KG.pad("M" + " L ".join(f"{a:.0f} {c:.0f}" for a, c in pts), "none", ROOD, 3)
    KG.tekst(x0 + 17, y0 + h + 22, "J", 14); KG.tekst(x0 + 17 + 11 * 20, y0 + h + 22, "D", 14)
    KG.letter(x0 + b / 2, y0 + h + 60, k)
KG.tekst(500, 625, "rode lijn = temperatuur, blauwe staven = neerslag; middenlijn = 0 °C", 15)
ZKG = {k: [Prent.zone(60 + i * 320, 90, 260, 400), Prent.rond(60 + i * 320 + 130, 550, 26)] for i, k in enumerate(DATA)}

# Zeestromen Noord-Atlantische Oceaan -----------------------------------
ZS = Prent("zeestromen-atlantisch", "Zeestromen in het noorden van de Atlantische Oceaan (schematisch)", "oceaan met continenten links en rechts en vier zeestromen P, Q, R, S")
ZS.rect(40, 70, 920, 520, "#e3f0f7", "none", 0)
ZS.pad("M40 70 L 260 70 L 300 200 L 230 330 L 260 450 L 200 590 L 40 590 Z", "#d8cfae", DONKER, 2)
ZS.pad("M960 70 L 760 70 L 700 170 L 760 260 L 720 330 L 790 420 L 760 590 L 960 590 Z", "#d8cfae", DONKER, 2)
ZS.tekst(130, 330, "Amerika", 20, vet=True)
ZS.tekst(860, 180, "Europa", 20, vet=True)
ZS.tekst(870, 480, "Afrika", 20, vet=True)
ZS.pad("M320 500 C 300 400 320 330 380 260", "none", ROOD, 7); ZS.pijl(370, 272, 382, 258, ROOD, 7)
ZS.pad("M400 240 C 500 180 600 150 690 150", "none", ROOD, 7); ZS.pijl(675, 152, 695, 150, ROOD, 7)
ZS.pad("M740 340 C 700 420 690 480 640 540", "none", BLAUW, 7); ZS.pijl(650, 528, 636, 546, BLAUW, 7)
ZS.pad("M380 90 C 340 120 320 160 310 200", "none", BLAUW, 7); ZS.pijl(313, 186, 309, 206, BLAUW, 7)
LZ = {"P": (370, 420), "Q": (540, 120), "R": (640, 440), "S": (400, 150)}
for k, (x, y) in LZ.items():
    ZS.letter(x, y, k)
ZZS = {"P": [Prent.zone(290, 250, 110, 260), Prent.rond(*LZ["P"], 26)],
       "Q": [Prent.zone(390, 130, 310, 110), Prent.rond(*LZ["Q"], 26)],
       "R": [Prent.zone(620, 330, 140, 220), Prent.rond(*LZ["R"], 26)],
       "S": [Prent.zone(290, 75, 110, 135), Prent.rond(*LZ["S"], 26)]}
ZS.tekst(500, 615, "rood = warme stroom, blauw = koude stroom", 15)

VRAGEN = [
    klik(
        "Klik op het klimatogram met droge zomers en zachte, natte winters.",
        KG.bestand, ZKG["B"],
        "Dat is een mediterraan klimaat.",
    ),
    klik(
        "Klik op het klimatogram dat bij de taiga past.",
        KG.bestand, ZKG["C"],
        "Lange, strenge winters onder 0 °C, een korte koele zomer en weinig neerslag.",
    ),
    met_prent(KG.bestand, tabel(
        "Kijk naar de klimatogrammen. Klopt dit?",
        [
            ("A hoort bij het tropisch regenwoud.", J),
            ("Bij A is het temperatuurverschil over het jaar heel klein.", J),
            ("Bij C is het verschil tussen warmste en koudste maand het grootst.", J),
            ("Alle drie horen bij het zuidelijk halfrond.", F),
        ],
        "Bij B en C vallen de warmste maanden in juni tot augustus: noordelijk halfrond.",
    )),
    met_prent(KG.bestand, keuze(
        "Klimatogram C toont een [[*continentaal|tropisch|mediterraan]] klimaat met een groot verschil tussen zomer en winter.",
        "Ver van de zee werkt geen water als buffer.",
    )),
    klik(
        "Klik op de Golfstroom.",
        ZS.bestand, ZZS["P"],
        "De warme stroom die langs Noord-Amerika naar het noorden trekt.",
    ),
    klik(
        "Klik op de stroom die onze winters zacht houdt.",
        ZS.bestand, ZZS["Q"],
        "De Noord-Atlantische Drift brengt warm water tot bij West-Europa.",
    ),
    klik(
        "Klik op de Labradorstroom.",
        ZS.bestand, ZZS["S"],
        "Een koude stroom uit het noorden langs Canada.",
    ),
    met_prent(ZS.bestand, tabel(
        "Kijk naar de zeestromen. Klopt dit?",
        [
            ("Stroom R is de koude Canarische stroom.", J),
            ("De stromen vormen samen een kring met de klok mee.", J),
            ("Stroom S maakt de kust van Canada zachter.", F),
            ("De vaste winden drijven deze stromen aan het oppervlak aan.", J),
        ],
        "Op het noordelijk halfrond draaien de grote oceaankringen met de klok mee.",
    )),
    tabel(
        "Weer of klimaat?",
        [
            ("morgen regent het in Gent", "Weer"),
            ("in Gent valt gemiddeld 800 mm per jaar", "Klimaat"),
            ("vandaag waait het hard aan zee", "Weer"),
            ("de zomers in Sevilla zijn droog en heet", "Klimaat"),
        ],
        "Klimaat is een gemiddelde over ongeveer dertig jaar.",
        kolommen=["Weer", "Klimaat"],
    ),
    koppel(
        "Koppel elk bioom aan zijn kenmerk.",
        [
            ("savanne", "grasland met verspreide bomen, droge en natte tijd"),
            ("toendra", "te koud voor bomen, mossen en dwergstruiken"),
            ("steppe", "droog grasland van de gematigde streken"),
            ("taiga", "naaldbos van de koude, noordelijke streken"),
        ],
        ["altijd warm en nat met dichte boomlagen"],
        "Dat laatste is het tropisch regenwoud.",
    ),
    volgorde(
        "Zet de biomen in volgorde van de evenaar naar de pool, in het noorden van Afrika en Europa.",
        [
            "Tropisch regenwoud",
            "Savanne",
            "Woestijn",
        ],
        "Hoe verder van de evenaar, hoe korter de natte tijd, tot het subtropisch maximum.",
    ),
    volgorde(
        "Zet de biomen in volgorde van Midden-Europa naar de noordpool.",
        [
            "Gemengd loofbos",
            "Taiga",
            "Toendra",
            "Poolwoestijn",
        ],
        "Steeds kouder en kortere groeiseizoenen.",
    ),
    tabel(
        "Warme of koude zeestroom?",
        [
            ("Golfstroom", "Warm"),
            ("Humboldtstroom", "Koud"),
            ("Benguelastroom", "Koud"),
            ("Noord-Atlantische Drift", "Warm"),
            ("Canarische stroom", "Koud"),
        ],
        "Koude stromen lopen vaak langs de westkust van continenten.",
        kolommen=["Warm", "Koud"],
    ),
    casus(
        "Lima in Peru en Rio de Janeiro in Brazilië liggen allebei ongeveer even ver ten zuiden van de evenaar. Lima krijgt bijna geen regen, Rio veel.",
        [
            tabel(
                "Klopt dit?",
                [
                    ("Langs Lima loopt een koude zeestroom.", J),
                    ("Koud water koelt de onderste lucht af, die dan niet opstijgt.", J),
                    ("Lima ligt dichter bij de evenaar en is daarom droger.", F),
                ],
                "Dezelfde breedte geeft niet altijd hetzelfde klimaat.",
            ),
            keuze(
                "Langs de kust van Peru komt koud, voedselrijk diepwater naar boven. Dat heet [[*opwelling|condensatie|infiltratie]].",
                "Daardoor is die zee heel visrijk.",
            ),
        ],
    ),
    volgorde(
        "Zet de motor van de thermohaliene circulatie in de juiste volgorde.",
        [
            "Warm oppervlaktewater stroomt naar het noorden",
            "Bij Groenland koelt het af en wordt het zouter",
            "Het koude, zoute water wordt zwaarder en zinkt",
            "Het stroomt diep langs de bodem naar het zuiden",
            "Nieuw warm water wordt aan het oppervlak aangetrokken",
        ],
        "Koud en zout water is zwaar en zinkt.",
    ),
    tabel(
        "Klopt dit over smeltwater van Groenland?",
        [
            ("Het is zoet water.", J),
            ("Het maakt het oppervlaktewater lichter.", J),
            ("Het kan de thermohaliene circulatie afremmen.", J),
            ("Het maakt het zeewater zouter.", F),
        ],
        "Lichter water zinkt minder makkelijk.",
    ),
    mk(
        "Wat zou er waarschijnlijk gebeuren als de thermohaliene circulatie stilvalt?",
        [
            "West-Europa zou merkelijk kouder worden",
            "De zeespiegel zou overal meteen tientallen meters dalen",
            "De passaatwinden zouden van richting omkeren",
            "Het tropisch regenwoud zou zich tot in België uitbreiden",
        ],
        0,
        "De aanvoer van warm oppervlaktewater zou verzwakken.",
    ),
    tabel(
        "Zeeklimaat of continentaal klimaat?",
        [
            ("zachte winters en koele zomers", "Zeeklimaat"),
            ("strenge winters en hete zomers", "Continentaal"),
            ("groot temperatuurverschil over het jaar", "Continentaal"),
            ("België", "Zeeklimaat"),
        ],
        "Water warmt traag op en koelt traag af.",
        kolommen=["Zeeklimaat", "Continentaal"],
    ),
    tabel(
        "Klopt dit over permafrost?",
        [
            ("Het is bodem die jaar na jaar bevroren blijft.", J),
            ("Je vindt ze onder de toendra.", J),
            ("Ze ontdooit elke zomer helemaal.", F),
        ],
        "Enkel de bovenste laag ontdooit in de zomer.",
    ),
    sleep(
        "In een [[poolwoestijn]] valt bijna geen neerslag, want koude lucht kan amper [[waterdamp]] vasthouden. Toch ligt er veel ijs, omdat het bijna nooit [[smelt]].",
        ["savanne", "zout", "regent"],
        "Antarctica is de grootste woestijn van de wereld.",
    ),
    inv(
        "Over hoeveel jaar middel je meestal het weer uit om een klimaat te beschrijven?",
        ["30", "dertig"],
        "Zo vallen losse uitschieters weg.",
    ),
    keuze(
        "Een havenstad in Noorwegen op 60° NB blijft in de winter ijsvrij dankzij de [[*Noord-Atlantische Drift|Labradorstroom|Humboldtstroom]].",
        "Een warme stroom maakt de kust zachter.",
    ),
    klik(
        "Klik op het klimatogram waarbij het hele jaar door veel regen valt en het altijd warm is.",
        KG.bestand, ZKG["A"],
        "Warm en nat het hele jaar: tropisch regenwoud.",
    ),
    met_prent(ZS.bestand, keuze(
        "Stroom R loopt langs de westkust van Afrika en maakt die kust [[*droger|natter|warmer]].",
        "Een koude stroom houdt de lucht beneden: weinig regen.",
    )),
    tabel(
        "Welk bioom past bij deze plaats?",
        [
            ("altijd warm, jaarlijks meer dan 2000 mm regen", "Tropisch regenwoud"),
            ("warm, een natte en een droge tijd", "Savanne"),
            ("heet overdag, jaarlijks minder dan 250 mm", "Woestijn"),
            ("koude winters, droog grasland ver van zee", "Steppe"),
        ],
        "Temperatuur en neerslag samen bepalen het bioom.",
        kolommen=["Tropisch regenwoud", "Savanne", "Woestijn", "Steppe"],
    ),
    tabel(
        "Klopt dit over een klimatogram?",
        [
            ("De temperatuur staat als lijn.", J),
            ("De neerslag staat in staven per maand.", J),
            ("Zijn de warmste maanden december en januari, dan ligt de plaats op het zuidelijk halfrond.", J),
            ("Je leest er de luchtdruk per dag op af.", F),
        ],
        "Twaalf maanden temperatuur en neerslag naast elkaar.",
    ),
    keuze(
        "Op het noordelijk halfrond draaien de grote oceaankringen [[*met de klok mee|tegen de klok in|afwisselend in beide richtingen]].",
        "Door het corioliseffect buigt het water naar rechts af.",
    ),
    tabel(
        "Klopt dit over het mediterraan klimaat?",
        [
            ("In de zomer ligt het subtropisch maximum erboven.", J),
            ("De winters zijn zacht en nat.", J),
            ("De zomers zijn er nat door de westenwinden.", F),
        ],
        "In de zomer blijft het er droog en zonnig.",
    ),
    open_(
        "Leg uit waarom het in België in de winter zachter is dan in Newfoundland in Canada, dat op dezelfde breedte ligt.",
        "Bij ons brengt de Noord-Atlantische Drift warm water tot aan de kust, en de westenwind voert die zachte zeelucht over het land. Newfoundland ligt aan de koude Labradorstroom en krijgt vaker koude lucht van het continent. Dezelfde breedte geeft dus niet hetzelfde klimaat.",
    ),
]
