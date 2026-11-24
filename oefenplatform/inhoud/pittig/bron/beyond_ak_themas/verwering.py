"""Verwering, karst en massatransport — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Karstlandschap ---------------------------------------------------------
KA = Prent("karst-doorsnede", "Doorsnede door een kalkplateau", "kalkplateau met trechter A, beek die verdwijnt bij B, grot met C (hangend) en D (staand), uitgang E in het dal")
KA.rect(40, 180, 920, 440, "#ddd6c0", DONKER, 0, 1)
for y in range(230, 620, 50):
    KA.lijn(40, y, 960, y, "#c4bca2", 1)
for x in (180, 330, 600, 760):
    KA.lijn(x, 180, x + 10, 330, "#9a917a", 2)
KA.pad("M40 180 L 140 180 L 180 220 L 210 240 L 240 220 L 280 180 L 960 180 L 960 60 L 40 60 Z", "#ffffff", "none", 0)
KA.pad("M140 180 L 180 220 L 210 240 L 240 220 L 280 180", "none", DONKER, 2)
KA.pad("M420 170 Q 500 160 560 182", "none", BLAUW, 5)
KA.pad("M560 182 L 575 260 L 600 330", "none", BLAUW, 4)
KA.pad("M560 330 Q 600 300 700 320 Q 800 330 860 380 L 880 460 Q 800 480 700 470 Q 600 470 560 420 Z", "#4a4438", DONKER, 2)
for x in (640, 700, 760):
    KA.pad(f"M{x - 8} 318 L {x} 365 L {x + 8} 320 Z", "#efe8d2", "none", 0)
for x in (620, 690, 770):
    KA.pad(f"M{x - 12} 470 L {x} 425 L {x + 12} 470 Z", "#efe8d2", "none", 0)
KA.pad("M860 420 L 960 470 L 960 620 L 880 620 Z", "#ffffff", "none", 0)
KA.pad("M860 420 L 960 470", "none", BLAUW, 6)
KA.tekst(500, 145, "beek", 16, kleur=BLAUW)
LKA = {"A": (210, 280), "B": (600, 200), "C": (700, 270), "D": (690, 520), "E": (905, 410)}
KA.lijn(700, 290, 700, 330, DONKER, 1)
KA.lijn(690, 500, 690, 440, DONKER, 1)
for k, (x, y) in LKA.items():
    KA.letter(x, y, k)
ZKA = {"A": [Prent.zone(140, 180, 140, 60), Prent.rond(*LKA["A"], 26)],
       "B": [Prent.zone(545, 170, 40, 90), Prent.rond(*LKA["B"], 26)],
       "C": [Prent.zone(625, 315, 150, 55), Prent.rond(*LKA["C"], 26)],
       "D": [Prent.zone(605, 420, 180, 52), Prent.rond(*LKA["D"], 26)],
       "E": [Prent.zone(860, 400, 100, 80), Prent.rond(*LKA["E"], 26)]}

# Helling ----------------------------------------------------------------
HE = Prent("helling-massatransport", "Een helling in de bergen", "rotswand met kegel P, helling met scheve palen Q, grond die wegschuift R over een kleilaag S")
HE.pad("M40 620 L 40 120 L 220 100 L 250 380 L 960 560 L 960 620 Z", "#c9b48a", DONKER, 2)
HE.pad("M40 120 L 220 100 L 250 380 L 40 380 Z", "#9a917a", DONKER, 2)
HE.pad("M250 380 L 300 330 L 360 395 Z", "#7d7466", DONKER, 1)
for x in (420, 470, 520):
    y = 380 + (x - 250) * 180 / 710
    HE.lijn(x, y, x + 30, y - 50, "#6b4f2a", 5)
HE.pad("M620 480 L 880 540 L 870 590 L 640 560 Z", "#8d6e4a", DONKER, 2)
HE.pad("M600 555 L 958 602", "none", "#7aa0c0", 7)
HE.tekst(600, 590, "kleilaag", 14, "end", kleur="#2b5d8a")
HE.pijl(700, 470, 800, 500, ROOD, 3)
LHE = {"P": (305, 300), "Q": (500, 380), "R": (740, 455), "S": (560, 545)}
for k, (x, y) in LHE.items():
    HE.letter(x, y, k)
ZHE = {"P": [Prent.zone(250, 330, 110, 65), Prent.rond(*LHE["P"], 26)],
       "Q": [Prent.zone(410, 380, 150, 70), Prent.rond(*LHE["Q"], 26)],
       "R": [Prent.zone(620, 480, 260, 80), Prent.rond(*LHE["R"], 26)],
       "S": [Prent.zone(600, 545, 360, 55), Prent.rond(*LHE["S"], 26)]}

VRAGEN = [
    klik(
        "Klik op de trechtervormige inzinking in het kalkplateau.",
        KA.bestand, ZKA["A"],
        "Dat is een doline: het dak van een holte zakte in.",
    ),
    klik(
        "Klik op de plek waar de ondergrondse rivier weer bovenkomt.",
        KA.bestand, ZKA["E"],
        "Dat is een resurgentie.",
    ),
    klik(
        "Klik op de druipstenen die van de bodem omhoog groeien.",
        KA.bestand, ZKA["D"],
        "Stalagmieten staan, stalactieten hangen.",
    ),
    met_prent(KA.bestand, tabel(
        "Kijk naar het kalkplateau. Welke letter hoort erbij?",
        [
            ("doline", "A"),
            ("verdwijngat", "B"),
            ("stalactieten", "C"),
            ("resurgentie", "E"),
        ],
        "Het water verdwijnt bij B en komt bij E terug boven.",
        kolommen=["A", "B", "C", "D", "E"],
    )),
    met_prent(KA.bestand, tabel(
        "Kijk naar de spleten en de grot. Klopt dit?",
        [
            ("De verticale spleten zijn diaklazen.", J),
            ("Het water lost de kalk op langs die spleten.", J),
            ("Bovenop het plateau stromen veel beken.", F),
            ("Dit landschap kan ook in zandsteen ontstaan.", F),
        ],
        "Karst vraagt een oplosbaar gesteente zoals kalksteen.",
    )),
    klik(
        "Klik op de puinkegel onder de rotswand.",
        HE.bestand, ZHE["P"],
        "Losgevroren brokken stapelen zich op aan de voet van de wand.",
    ),
    klik(
        "Klik op de plek waar je de traagste vorm van massatransport ziet.",
        HE.bestand, ZHE["Q"],
        "Scheefgezakte palen of bomen verraden bodemcreep.",
    ),
    met_prent(HE.bestand, tabel(
        "Kijk naar de helling. Klopt dit?",
        [
            ("Bij R schuift een stuk grond weg.", J),
            ("S werkt als glijvlak.", J),
            ("Het puin bij P is ontstaan door massatransport.", J),
            ("De palen bij Q staan scheef door de wind.", F),
        ],
        "Klei laat geen water door en wordt glad als ze nat is.",
    )),
    tabel(
        "Fysische, chemische of biologische verwering?",
        [
            ("water bevriest in een spleet", "Fysisch"),
            ("zuur regenwater lost kalk op", "Chemisch"),
            ("boomwortels wrikken een rots open", "Biologisch"),
            ("korstmossen scheiden zuren af", "Biologisch"),
            ("ijzer in gesteente roest", "Chemisch"),
        ],
        "Kapotbreken, oplossen of door levende wezens.",
        kolommen=["Fysisch", "Chemisch", "Biologisch"],
    ),
    tabel(
        "Welke vorm van verwering overheerst hier?",
        [
            ("toendra in Noord-Canada", "vorstverwering"),
            ("tropisch regenwoud", "chemische verwering"),
            ("hooggebergte boven de boomgrens", "vorstverwering"),
        ],
        "Kou geeft vorst, warmte en vocht geven chemische reacties.",
        kolommen=["vorstverwering", "chemische verwering"],
    ),
    volgorde(
        "Zet de stappen van vorstverwering in de juiste volgorde.",
        [
            "Regenwater loopt in een spleet",
            "Het water bevriest en zet uit",
            "De spleet wordt een beetje wijder",
            "Na vele keren vriezen en dooien breekt het gesteente",
        ],
        "IJs neemt ongeveer een tiende meer plaats in dan water.",
    ),
    mk(
        "Waarom is een grafsteen van kalksteen na honderd jaar slecht leesbaar, en een van graniet niet?",
        [
            "Regenwater is licht zuur en lost kalk op",
            "Kalksteen is altijd zachter omdat het jonger is dan graniet",
            "Graniet trekt geen water aan omdat het magmatisch is",
            "De letters in graniet zijn altijd veel dieper uitgekapt",
        ],
        0,
        "Kalksteen is gevoelig voor chemische verwering.",
    ),
    tabel(
        "Snel of traag massatransport?",
        [
            ("bodemcreep", "Traag"),
            ("steenlawine", "Snel"),
            ("afstorting", "Snel"),
            ("modderstroom", "Snel"),
        ],
        "Bodemcreep gaat enkele millimeter per jaar.",
        kolommen=["Snel", "Traag"],
    ),
    sorteer(
        "Maakt dit een helling stabieler of onstabieler?",
        ["Stabieler", "Onstabieler"],
        [
            ("herbebossen", "Stabieler"),
            ("bossen kappen", "Onstabieler"),
            ("draineren", "Stabieler"),
            ("zware regen", "Onstabieler"),
            ("terrassen aanleggen", "Stabieler"),
            ("bouwen bovenaan de helling", "Onstabieler"),
        ],
        "Water en gewicht maken een helling zwakker, wortels houden ze vast.",
    ),
    casus(
        "Na dagen van zware regen schuift in een bergdorp een helling naar beneden. Het puin blokkeert de rivier in het dal.",
        [
            keuze(
                "Het water maakte de bodem [[*zwaarder en gladder|lichter en stroever|droger en harder]].",
                "Water vult de poriën en verlaagt de wrijving.",
            ),
            keuze(
                "Achter de puindam kan een [[*meer|delta|doline]] ontstaan.",
                "Het rivierwater kan niet meer weg.",
            ),
            tabel(
                "Klopt dit over het gevaar?",
                [
                    ("De dam kan later plots doorbreken.", J),
                    ("Een vloedgolf kan dan het dal in stromen.", J),
                    ("Een puindam is altijd blijvend stevig.", F),
                ],
                "Daarom worden zulke meren snel bewaakt of gecontroleerd leeggemaakt.",
            ),
        ],
    ),
    sleep(
        "Regenwater neemt [[koolstofdioxide]] op en wordt licht zuur. Het lost [[kalksteen]] op. Waar een druppel in een grot verdampt, slaat de kalk weer neer als [[druipsteen]].",
        ["zuurstof", "graniet", "lava"],
        "Zo groeien stalactieten en stalagmieten heel traag.",
    ),
    tabel(
        "Klopt dit over karst in België?",
        [
            ("Je vindt het in de kalkstreken van Wallonië.", J),
            ("De grotten van Han liggen in zo'n streek.", J),
            ("De Kempen zijn een typisch karstgebied.", F),
        ],
        "De Kempen hebben zand, geen kalk.",
    ),
    koppel(
        "Koppel elke karstvorm aan zijn uitleg.",
        [
            ("karren", "groeven in een blootliggend kalkoppervlak"),
            ("diaklaas", "natuurlijke spleet in de kalk"),
            ("verdwijngat", "plek waar een beek in de grond verdwijnt"),
            ("doline", "trechter door een ingezakte holte"),
        ],
        ["kegel van puin onder een rotswand"],
        "Dat laatste is een puinkegel, geen karst.",
    ),
    mk(
        "Waarom gebeuren er in Vlaanderen bijna geen steenlawines?",
        [
            "Er zijn bijna geen steile hellingen of rotswanden",
            "Het regent in Vlaanderen te weinig om bodem te laten schuiven",
            "Vlaamse bodems bevatten nooit klei die als glijvlak dient",
            "Het vriest in Vlaanderen nooit lang genoeg om rots te breken",
        ],
        0,
        "Massatransport vraagt hoogteverschil.",
    ),
    tabel(
        "Verwering, erosie of sedimentatie?",
        [
            ("een rots valt ter plaatse uiteen", "Verwering"),
            ("een rivier voert zand mee", "Erosie"),
            ("zand bezinkt in een meer", "Sedimentatie"),
            ("vorst doet een steen barsten", "Verwering"),
        ],
        "Uiteenvallen, wegvoeren, neerleggen.",
        kolommen=["Verwering", "Erosie", "Sedimentatie"],
    ),
    keuze(
        "Bij massatransport is [[*de zwaartekracht|de wind|het getij]] het motortje.",
        "Water helpt, maar trekt niet zelf.",
    ),
    mk(
        "Waarom legt men vangnetten langs een bergweg onder een steile wand?",
        [
            "Vorst maakt brokken los die kunnen vallen",
            "De netten houden de sneeuw op de weg tegen",
            "Ze beschermen de wand tegen chemische verwering",
            "Ze vangen de modder van een lahar op",
        ],
        0,
        "Vooral bij dooi in de lente komen brokken los.",
    ),
    tabel(
        "Klopt dit over druipstenen?",
        [
            ("Een stalactiet hangt aan het plafond.", J),
            ("Ze groeien heel traag.", J),
            ("Ze bestaan uit neergeslagen kalk.", J),
            ("Ze ontstaan door vorstverwering.", F),
        ],
        "Soms groeien een stalactiet en een stalagmiet samen tot een zuil.",
    ),
    inv(
        "Een stalagmiet groeit ongeveer 0,1 mm per jaar. Hoeveel cm groeit hij in 1 000 jaar?",
        ["10"],
        "1 000 x 0,1 mm = 100 mm = 10 cm.",
    ),
    keuze(
        "Een kleilaag in een helling is gevaarlijk omdat ze [[*geen water doorlaat|veel water doorlaat|altijd bevroren is]] en glad wordt.",
        "Het water blijft erboven staan en de grond erboven glijdt weg.",
    ),
    tabel(
        "Welke vorm van massatransport is dit?",
        [
            ("brokken vallen vrij van een steile wand", "afstorting"),
            ("modder en stenen storten snel door een dal", "modderstroom"),
            ("de bodem kruipt millimeters per jaar", "bodemcreep"),
        ],
        "De snelheid en het water maken het verschil.",
        kolommen=["afstorting", "modderstroom", "bodemcreep"],
    ),
    mk(
        "Waarom vind je in een karstgebied weinig beken aan de oppervlakte?",
        [
            "Het water verdwijnt via spleten ondergronds",
            "Het regent op kalkplateaus veel minder dan elders",
            "De kalk zuigt al het water op en houdt het vast",
            "De beken bevriezen er bijna het hele jaar door",
        ],
        0,
        "Langs diaklazen en verdwijngaten gaat het water de diepte in.",
    ),
    open_(
        "Leg uit waarom chemische verwering in het tropisch regenwoud veel sneller gaat dan in de toendra.",
        "In het regenwoud is het warm en heel vochtig. Warmte versnelt chemische reacties en water is nodig om stoffen op te lossen. In de toendra is het koud en ligt het water vaak bevroren, dus gaan de reacties heel traag. Daar overheerst vorstverwering.",
    ),
]
