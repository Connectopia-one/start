"""Neerslag en de kringloop van het water — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Gebergte met stijgingsregen --------------------------------------------
GB = Prent("gebergte-regenschaduw", "Vochtige zeewind waait over een gebergte", "doorsnede: zee links, gebergte in het midden, punten A, B, C")
GB.rect(40, 470, 220, 90, "#9bc1df", "none", 0)
GB.tekst(150, 525, "zee", 18)
GB.pad("M260 560 L 260 470 L 380 450 L 560 170 L 700 430 L 960 460 L 960 560 Z", "#c9b48a", DONKER, 2)
GB.pijl(60, 400, 230, 400, BLAUW, 4)
GB.pijl(300, 380, 450, 230, BLAUW, 4)
GB.pijl(650, 230, 800, 380, ORANJE, 4)
for x, y in ((420, 170), (480, 130), (360, 220)):
    GB.ellips(x, y, 55, 28, "#d9dde2", DONKER, 1)
for x in range(350, 480, 22):
    GB.lijn(x, 230 - (x - 350) * 0.5, x - 8, 280 - (x - 350) * 0.5, BLAUW, 2)
GB.tekst(150, 380, "vochtige wind", 16)
PG = {"A": (430, 380), "B": (560, 130), "C": (790, 420)}
for k, (x, y) in PG.items():
    GB.letter(x, y, k)
ZGB = {"A": [Prent.zone(330, 300, 160, 160), Prent.rond(430, 380, 26)],
       "B": [Prent.rond(560, 150, 40)],
       "C": [Prent.zone(690, 380, 260, 90), Prent.rond(790, 420, 26)]}

# Waterkringloop ----------------------------------------------------------
WK = Prent("waterkringloop", "De kringloop van het water", "zee, wolk, land met bos en pijlen 1 tot 6")
WK.rect(40, 450, 380, 130, "#9bc1df", "none", 0)
WK.pad("M420 580 L 420 450 Q 600 420 760 330 L 960 300 L 960 580 Z", "#c9b48a", DONKER, 2)
WK.pad("M420 520 Q 650 500 960 480", "none", BLAUW, 3)
WK.rect(420, 540, 540, 40, "#8fb3cf", "none", 0)
WK.tekst(700, 568, "grondwater", 16)
for x in (800, 850, 900):
    WK.lijn(x, 320, x, 290, "#6b4f2a", 5)
    WK.cirkel(x, 275, 22, "#6aa84f", DONKER, 1)
WK.ellips(420, 120, 120, 45, "#d9dde2", DONKER, 1)
WK.ellips(640, 110, 110, 40, "#d9dde2", DONKER, 1)
PIJL = {"1": ((200, 430), (330, 170)), "2": ((470, 110), (580, 110)), "3": ((660, 160), (700, 330)),
        "4": ((720, 360), (720, 520)), "5": ((650, 362), (480, 428)), "6": ((860, 250), (720, 160))}
for k, ((x1, y1), (x2, y2)) in PIJL.items():
    WK.pijl(x1, y1, x2, y2, DONKER, 3)
LW = {"1": (235, 300), "2": (525, 70), "3": (725, 230), "4": (755, 450), "5": (560, 340), "6": (815, 195)}
for k, (x, y) in LW.items():
    WK.letter(x, y, k)
ZWK = {k: [Prent.rond(x, y, 28), Prent.zone(min(PIJL[k][0][0], PIJL[k][1][0]) - 12, min(PIJL[k][0][1], PIJL[k][1][1]) - 12, abs(PIJL[k][1][0] - PIJL[k][0][0]) + 24, abs(PIJL[k][1][1] - PIJL[k][0][1]) + 24)] for k, (x, y) in LW.items()}

VRAGEN = [
    klik(
        "Klik op de plaats waar stijgingsregen valt.",
        GB.bestand, ZGB["A"],
        "Aan de loefzijde moet de lucht omhoog, koelt ze af en regent ze uit.",
    ),
    klik(
        "Klik op de regenschaduw.",
        GB.bestand, ZGB["C"],
        "Aan de lijzijde daalt de lucht, warmt op en is ze droog.",
    ),
    met_prent(GB.bestand, tabel(
        "Kijk naar de doorsnede. Klopt dit?",
        [
            ("Bij B is het het koudst.", J),
            ("De lucht bij C warmt op terwijl ze daalt.", J),
            ("Bij C valt de meeste regen.", F),
            ("De lucht koelt af terwijl ze bij A opstijgt.", J),
        ],
        "Stijgende lucht koelt af, dalende lucht warmt op.",
    )),
    met_prent(GB.bestand, keuze(
        "De kant waar de wind tegen het gebergte waait, heet de [[*loefzijde|lijzijde|regenschaduw]].",
        "De andere kant is de lijzijde.",
    )),
    klik(
        "Klik op de pijl die verdamping boven zee toont.",
        WK.bestand, ZWK["1"],
        "Boven de oceanen gebeurt het grootste deel van de verdamping.",
    ),
    klik(
        "Klik op de pijl die infiltratie toont.",
        WK.bestand, ZWK["4"],
        "Water zakt de bodem in naar het grondwater.",
    ),
    met_prent(WK.bestand, tabel(
        "Kijk naar de kringloop. Welke pijl hoort bij welke stap?",
        [
            ("neerslag op het land", "3"),
            ("water dat terugstroomt naar zee", "5"),
            ("bomen die water afgeven via hun bladeren", "6"),
            ("wolken die met de wind naar het land drijven", "2"),
        ],
        "Verdampen, transport, neerslag, infiltratie, afstromen, en planten die ook damp afgeven.",
        kolommen=["2", "3", "5", "6"],
    )),
    tabel(
        "Absolute of relatieve luchtvochtigheid?",
        [
            ("12 gram damp per kubieke meter", "Absolute"),
            ("85 procent", "Relatieve"),
            ("hoeveel damp er echt in de lucht zit", "Absolute"),
            ("hoe dicht de lucht bij verzadiging zit", "Relatieve"),
        ],
        "Absoluut in gram per m³, relatief in procent.",
        kolommen=["Absolute", "Relatieve"],
    ),
    tabel(
        "Wat gebeurt er met de relatieve vochtigheid als de hoeveelheid damp gelijk blijft?",
        [
            ("de lucht koelt af", "Stijgt"),
            ("de lucht warmt op", "Daalt"),
            ("de lucht koelt af tot het dauwpunt", "Wordt 100 %"),
        ],
        "Koude lucht kan minder damp vasthouden.",
        kolommen=["Stijgt", "Daalt", "Wordt 100 %"],
    ),
    volgorde(
        "Zet het ontstaan van een wolk in de juiste volgorde.",
        [
            "Vochtige lucht stijgt op",
            "De lucht zet uit omdat de druk hoger lager is",
            "De lucht koelt af tot haar dauwpunt",
            "De damp condenseert op stof- en zoutdeeltjes",
            "Er vormen zich druppeltjes: een wolk",
        ],
        "Uitzetten koelt af, afkoelen doet condenseren.",
    ),
    tabel(
        "Convectieregen, stijgingsregen of frontale regen?",
        [
            ("dagelijkse onweersbuien bij de ITCZ", "Convectieregen"),
            ("regen aan de westkant van een gebergte", "Stijgingsregen"),
            ("warme lucht schuift over koude lucht", "Frontale regen"),
            ("een zware zomerbui na een hete dag", "Convectieregen"),
        ],
        "Opwarming, reliëf of een front doen de lucht opstijgen.",
        kolommen=["Convectieregen", "Stijgingsregen", "Frontale regen"],
    ),
    inv(
        "Er valt 25 mm regen op een plat dak van 8 m². Hoeveel liter water is dat?",
        ["200"],
        "1 mm is 1 liter per m²: 25 · 8 = 200 liter.",
    ),
    casus(
        "De Atacamawoestijn in Chili ligt aan de Stille Oceaan, maar het regent er bijna nooit.",
        [
            tabel(
                "Welke oorzaken spelen mee?",
                [
                    ("een koude zeestroom langs de kust", J),
                    ("een regenschaduw achter de Andes", J),
                    ("de ITCZ ligt er het hele jaar", F),
                ],
                "Koud water koelt de onderste lucht af, die dan niet opstijgt.",
            ),
            keuze(
                "De koude zeestroom langs die kust heet de [[*Humboldtstroom|Golfstroom|Noord-Atlantische Drift]].",
                "De Golfstroom en zijn verlengde zijn warm.",
            ),
        ],
    ),
    tabel(
        "Krijgt dit gebied meer of minder neerslag?",
        [
            ("een kust met een warme zeestroom", "Meer"),
            ("diep in een continent, ver van zee", "Minder"),
            ("een gebied met vaak een hogedrukgebied", "Minder"),
            ("de loefzijde van een gebergte", "Meer"),
        ],
        "Stijgende lucht en vocht van zee geven neerslag.",
        kolommen=["Meer", "Minder"],
    ),
    tabel(
        "Klopt dit over een kaart met isohyeten?",
        [
            ("Ze verbinden plaatsen met dezelfde neerslag.", J),
            ("Liggen ze ver uit elkaar, dan verandert de neerslag traag.", J),
            ("Je leest er de temperatuur op af.", F),
        ],
        "Voor temperatuur heb je isothermen.",
    ),
    tabel(
        "Klopt dit over verharding in een stad?",
        [
            ("Er infiltreert minder water in de bodem.", J),
            ("Er stroomt meer water meteen af naar de riool.", J),
            ("Het grondwater wordt er sneller aangevuld.", F),
            ("De kans op wateroverlast bij een zware bui stijgt.", J),
        ],
        "Op beton en asfalt kan het water de grond niet in.",
    ),
    mk(
        "Waarom zie je 's morgens vaak mist boven een weide na een heldere nacht?",
        [
            "De bodem straalde warmte uit en de lucht koelde tot het dauwpunt",
            "Het gras verdampt 's nachts veel meer water dan overdag in de volle zon",
            "Een heldere nacht brengt altijd vochtige lucht mee van de Noordzee",
            "De koude lucht stijgt 's nachts op en vormt zo hoog in de lucht een wolk",
        ],
        0,
        "Mist is een wolk aan de grond.",
    ),
    tabel(
        "Mist of nevel?",
        [
            ("je ziet minder dan een kilometer ver", "Mist"),
            ("je ziet meer dan een kilometer ver", "Nevel"),
            ("de dichtste van de twee", "Mist"),
        ],
        "Allebei zijn het wolken aan de grond.",
        kolommen=["Mist", "Nevel"],
    ),
    sleep(
        "Een wolk bestaat niet uit [[waterdamp]], want die is onzichtbaar. Ze bestaat uit kleine [[druppeltjes]] of ijskristallen. De damp condenseert op [[condensatiekernen]].",
        ["zout", "isohyeten"],
        "Zonder kernen blijft lucht veel vocht vasthouden.",
    ),
    tabel(
        "Klopt dit over neerslag in België?",
        [
            ("Ukkel krijgt ongeveer 800 à 900 mm per jaar.", J),
            ("De neerslag is over het hele jaar verdeeld.", J),
            ("In de Ardennen valt meer dan in Vlaanderen.", J),
            ("Het regent bijna enkel in de zomer.", F),
        ],
        "De westenwinden brengen het hele jaar vocht van de Atlantische Oceaan.",
    ),
    keuze(
        "Ongeveer 86 % van alle verdamping op aarde gebeurt boven de [[*oceanen|bossen|steden]].",
        "Daar is een eindeloos groot wateroppervlak.",
    ),
    met_prent(WK.bestand, keuze(
        "Pijl 4 eindigt in het [[*grondwater|zeewater|wolkendek]].",
        "Water dat de bodem in zakt, vult het grondwater aan.",
    )),
    met_prent(GB.bestand, tabel(
        "Kijk naar de doorsnede. Hoort dit bij de loefzijde of bij de regenschaduw?",
        [
            ("de natte helling bij A", "Loefzijde"),
            ("het droge gebied bij C", "Regenschaduw"),
            ("waar de wolken hun regen laten vallen", "Loefzijde"),
            ("waar warme, droge valwind waait", "Regenschaduw"),
        ],
        "De lucht verliest haar vocht aan de kant van de wind.",
        kolommen=["Loefzijde", "Regenschaduw"],
    )),
    tabel(
        "Is dit neerslag?",
        [
            ("hagel", J),
            ("ijzel", J),
            ("mist", F),
            ("natte sneeuw", J),
        ],
        "Mist is een wolk aan de grond, geen neerslag.",
    ),
    keuze(
        "Water dat niet verdampt en niet meteen afstroomt, zakt de bodem in. Dat heet [[*infiltratie|condensatie|transpiratie]].",
        "Zo wordt het grondwater aangevuld.",
    ),
    inv(
        "Hoeveel liter per vierkante meter valt er bij een bui van 12 mm?",
        ["12"],
        "1 mm is 1 liter per m².",
    ),
    tabel(
        "Klopt dit over bomen in de kringloop?",
        [
            ("Ze geven water af via hun bladeren.", J),
            ("Ze vangen regen op voor die de grond raakt.", J),
            ("Ze maken infiltratie onmogelijk.", F),
        ],
        "Wortels helpen het water juist de bodem in.",
    ),
    keuze(
        "Lucht die aan de lijzijde van een gebergte afdaalt, wordt [[*warmer en droger|kouder en natter|kouder en droger]].",
        "Dalende lucht wordt samengeperst en warmt op.",
    ),
    open_(
        "Leg uit waarom een berghelling die naar de zee kijkt veel natter is dan de helling aan de andere kant.",
        "De vochtige zeewind moet tegen de helling omhoog. De lucht zet uit, koelt af tot het dauwpunt en de damp condenseert: stijgingsregen aan de loefzijde. Aan de andere kant daalt de lucht, warmt op en heeft ze haar vocht al verloren. Daar ligt een regenschaduw.",
    ),
]
