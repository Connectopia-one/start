"""Erosie door water, ijs en wind — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Meander bovenaanzicht --------------------------------------------------
ME = Prent("meander-bovenaanzicht", "Een meanderende rivier van bovenaf", "rivier met een grote bocht, punten K en L aan de buitenkant, M en N aan de binnenkant, stroomrichting met pijl")
ME.rect(40, 60, 920, 560, "#dfe8c9", "none", 0, 0)
RIV = "M40 520 C 200 520 220 160 400 160 C 580 160 600 480 760 480 C 860 480 900 300 960 300"
ME.pad(RIV, "none", "#9bc1df", 48)
ME.pad(RIV, "none", BLAUW, 2)
ME.pad("M330 230 C 380 205 430 210 460 240 L 420 270 C 400 250 370 248 350 260 Z", "#f0dfa8", "none", 0)
ME.pad("M690 410 C 730 430 770 430 800 410 L 790 380 C 770 395 740 395 710 380 Z", "#f0dfa8", "none", 0)
ME.pijl(120, 470, 200, 400, DONKER, 3)
ME.tekst(105, 450, "stroming", 15, "end")
LME = {"K": (400, 105), "L": (760, 540), "M": (400, 230), "N": (750, 405)}
for k, (x, y) in LME.items():
    ME.letter(x, y, k)
ZME = {k: [Prent.rond(x, y, 32)] for k, (x, y) in LME.items()}
ZME["K"].append(Prent.zone(330, 110, 140, 30))
ZME["L"].append(Prent.zone(690, 495, 140, 30))

# Hjülströmdiagram (schematisch) ----------------------------------------
HJ = Prent("hjulstrom-schema", "Hjülströmdiagram (vereenvoudigd)", "korrelgrootte horizontaal, stroomsnelheid verticaal, drie zones")
L, R_, B, O = 140, 920, 80, 540
HJ.rect(L, B, R_ - L, O - B, "#eef3e4", "none", 0, 0)
ERO_ = f"M{L} {B + 40} C 330 300 420 400 480 395 C 560 390 700 260 {R_} {B + 30}"
SED_ = f"M{L} {O - 5} C 420 {O - 10} 560 470 {R_} {B + 200}"
HJ.pad(ERO_ + f" L {R_} {B} L {L} {B} Z", "#f4c9a8", "none", 0)
HJ.pad(SED_ + f" L {R_} {O} L {L} {O} Z", "#d8e3f0", "none", 0)
HJ.pad(ERO_, "none", ROOD, 3)
HJ.pad(SED_, "none", BLAUW, 3)
HJ.lijn(L, O, R_, O, DONKER, 2)
HJ.lijn(L, O, L, B, DONKER, 2)
for x, t in ((200, "klei"), (340, "silt"), (480, "zand"), (650, "grind"), (840, "keien")):
    HJ.tekst(x, O + 24, t, 15)
HJ.tekst(530, O + 52, "korrelgrootte", 16)
HJ.svg(f'<text x="80" y="{(B + O) // 2}" font-size="16" text-anchor="middle" transform="rotate(-90 80 {(B + O) // 2})" fill="#2f4a22">stroomsnelheid</text>')
LHJ = {"X": (520, 170), "Y": (360, 420), "Z": (760, 470)}
for k, (x, y) in LHJ.items():
    HJ.letter(x, y, k)
ZHJ = {"X": [Prent.zone(440, 100, 200, 160)], "Y": [Prent.zone(250, 390, 180, 70)], "Z": [Prent.zone(700, 430, 200, 90)]}

VRAGEN = [
    klik(
        "Klik op een oever waar de rivier het meest wegschuurt.",
        ME.bestand, ZME["K"] + ZME["L"],
        "De holle of buitenoever wordt uitgeschuurd.",
    ),
    klik(
        "Klik op een plek waar de rivier zand afzet.",
        ME.bestand, ZME["M"] + ZME["N"],
        "Aan de bolle of binnenoever stroomt het water trager.",
    ),
    met_prent(ME.bestand, tabel(
        "Kijk naar de meander. Klopt dit?",
        [
            ("Bij K stroomt het water het snelst.", J),
            ("Bij M ontstaat een zandbank.", J),
            ("De bochten worden in de loop van de tijd kleiner.", F),
            ("Zo'n rivier ligt meestal in een vlak gebied.", J),
        ],
        "De bochten groeien en schuiven op, tot de rivier ze soms afsnijdt.",
    )),
    klik(
        "Klik in de zone waar korrels worden opgenomen door het water.",
        HJ.bestand, ZHJ["X"],
        "Boven de rode lijn is de stroming snel genoeg om te eroderen.",
    ),
    klik(
        "Klik in de zone waar korrels bezinken.",
        HJ.bestand, ZHJ["Z"],
        "Onder de blauwe lijn is het water te traag om ze te dragen.",
    ),
    met_prent(HJ.bestand, tabel(
        "Kijk naar het Hjülströmdiagram. Klopt dit?",
        [
            ("Zand wordt het makkelijkst opgenomen.", J),
            ("Klei blijft bij trage stroming lang zweven.", J),
            ("Keien hebben de hoogste snelheid nodig.", J),
            ("Klei wordt bij de laagste snelheid opgenomen.", F),
        ],
        "Klei plakt aan elkaar, daarom vraagt ze toch een hoge snelheid.",
    )),
    tabel(
        "Bovenloop of benedenloop?",
        [
            ("groot verval", "Bovenloop"),
            ("V-dal", "Bovenloop"),
            ("alluviale vlakte", "Benedenloop"),
            ("vooral sedimentatie", "Benedenloop"),
            ("vooral verticale erosie", "Bovenloop"),
        ],
        "Hoe kleiner het verval, hoe trager het water.",
        kolommen=["Bovenloop", "Benedenloop"],
    ),
    tabel(
        "Rivier, gletsjer of wind?",
        [
            ("U-dal", "Gletsjer"),
            ("paddenstoelrots", "Wind"),
            ("meander", "Rivier"),
            ("zwerfkei", "Gletsjer"),
            ("löss", "Wind"),
            ("kloofdal", "Rivier"),
        ],
        "Elke kracht laat haar eigen sporen na.",
        kolommen=["Rivier", "Gletsjer", "Wind"],
    ),
    koppel(
        "Koppel elke transportwijze aan haar uitleg.",
        [
            ("suspensie", "zwevend meegevoerd"),
            ("saltatie", "huppelend over de bodem"),
            ("rollen", "over de bodem voortgeduwd"),
        ],
        ["opgelost in het water", "door de zon verdampt"],
        "Hoe fijner de korrel, hoe hoger hij meegaat.",
    ),
    keuze(
        "Een waterval werkt zich stroomopwaarts terug door [[*terugschrijdende|zijdelingse|differentiële]] erosie.",
        "Het water ondergraaft de voet van de waterval.",
    ),
    mk(
        "In een rivierdal blijven harde zandsteenbanken als richels staan, terwijl de zachte lagen ertussen wegslijten. Hoe heet dat?",
        [
            "Differentiële erosie",
            "Terugschrijdende erosie",
            "Chemische verwering",
            "Sedimentatie",
        ],
        0,
        "Niet alle lagen weerstaan even goed.",
    ),
    casus(
        "In Noorwegen loopt de zee diep het land in, tussen steile rotswanden die honderden meter hoog zijn.",
        [
            keuze(
                "Zo'n zeearm heet een [[*fjord|delta|estuarium]].",
                "Een ondergelopen gletsjerdal.",
            ),
            keuze(
                "Het dal heeft een [[*U-vorm|V-vorm|vlakke bodem zonder wanden]].",
                "Het ijs schuurde ook de wanden uit.",
            ),
            tabel(
                "Klopt dit over het ontstaan?",
                [
                    ("Het ijs sneed tot onder het huidige zeeniveau.", J),
                    ("Na de ijstijd steeg de zeespiegel.", J),
                    ("Een rivier groef dit dal uit.", F),
                ],
                "Gletsjers kunnen dieper snijden dan rivieren.",
            ),
        ],
    ),
    volgorde(
        "Zet de delen van een gletsjer van hoog naar laag.",
        ["Cirque", "Gletsjertong", "Gletsjerfront", "Frontmorene"],
        "In de cirque hoopt de sneeuw zich op, aan het front smelt het ijs.",
    ),
    tabel(
        "Klopt dit over de laatste ijstijden en België?",
        [
            ("Het ijs kwam niet tot in België.", J),
            ("De wind blies toen zand en löss over het land.", J),
            ("In Nederland duwde het ijs stuwwallen op.", J),
            ("België lag volledig onder een ijskap.", F),
        ],
        "België lag in een koude, kale toendra voor het ijs.",
    ),
    mk(
        "Waarom vind je in de Kempen zand en in Haspengouw löss?",
        [
            "Grove korrels vielen eerder neer dan fijne",
            "In Haspengouw regende het veel meer dan in de Kempen",
            "De Kempen lagen onder het ijs en Haspengouw niet",
            "Löss is pas na de ijstijd door rivieren aangevoerd",
        ],
        0,
        "De wind kwam uit het noorden en liet het zwaarste eerst vallen.",
    ),
    sorteer(
        "Glaciaal of interglaciaal?",
        ["Glaciaal", "Interglaciaal"],
        [
            ("koude fase", "Glaciaal"),
            ("ijskappen groeien", "Glaciaal"),
            ("warme periode tussen twee ijstijden", "Interglaciaal"),
            ("de tijd waarin wij nu leven", "Interglaciaal"),
        ],
        "Het pleistoceen wisselde koude en warme fasen af.",
    ),
    tabel(
        "Welke morene is dit?",
        [
            ("langs de zijkant van de gletsjer", "zijmorene"),
            ("vooraan aan het front", "frontmorene"),
            ("onder het ijs", "grondmorene"),
        ],
        "De grondmorene werkt als schuurpapier.",
        kolommen=["zijmorene", "frontmorene", "grondmorene"],
    ),
    sleep(
        "Een paddenstoelrots ontstaat doordat de wind [[zand]] meevoert tot ongeveer [[een meter]] hoog. Daar wordt de rots het meest [[weggeschuurd]].",
        ["klei", "tien meter", "opgebouwd"],
        "Daarom wordt de voet smaller dan de top.",
    ),
    tabel(
        "Klopt dit over winderosie?",
        [
            ("Ze werkt het sterkst in droge gebieden.", J),
            ("Plantengroei remt ze af.", J),
            ("Hagen rond akkers breken de wind.", J),
            ("Natte korrels waaien het makkelijkst weg.", F),
        ],
        "Vochtige korrels plakken aan elkaar.",
    ),
    mk(
        "Waarom overstroomt een rivier sneller als er in haar stroombekken veel verharding bijkomt?",
        [
            "Het regenwater loopt meteen af",
            "Verharding maakt de rivier smaller en ondieper",
            "Asfalt trekt meer regen aan dan een akker",
            "De waterscheidingskam verschuift naar de rivier toe",
        ],
        0,
        "Het water kan niet meer in de bodem zakken.",
    ),
    tabel(
        "Welke dalvorm hoort erbij?",
        [
            ("een rivier zaagt zich snel in hard gesteente", "kloofdal"),
            ("een rivier zaagt in de bovenloop, de wanden verweren", "V-dal"),
            ("een rivier breidt zich zijdelings uit", "vlakbodemdal"),
            ("een gletsjer vult het hele dal", "U-dal"),
        ],
        "De vorm verraadt de kracht die het dal maakte.",
        kolommen=["kloofdal", "V-dal", "vlakbodemdal", "U-dal"],
    ),
    keuze(
        "De lijn die twee stroombekkens van elkaar scheidt, heet de [[*waterscheidingskam|monding|alluviale vlakte]].",
        "Regen aan de ene kant gaat naar een andere rivier dan aan de andere kant.",
    ),
    tabel(
        "Klopt dit over gletsjerkrassen?",
        [
            ("Stenen in het ijs krassen over de rotsbodem.", J),
            ("De krassen tonen de richting waarin het ijs stroomde.", J),
            ("Ze ontstaan door de wind.", F),
        ],
        "Zo kan je zien waar het ijs vandaan kwam.",
    ),
    inv(
        "Een zwerfkei in Noord-Duitsland komt uit Zweden, ongeveer 600 km verder. Een gletsjer stroomde 50 m per jaar. Hoeveel jaar deed de kei over de reis?",
        ["12000", "12 000"],
        "600 km = 600 000 m; 600 000 : 50 = 12 000 jaar.",
    ),
    mk(
        "Een rivier heeft haar evenwichtsprofiel bereikt. Wat betekent dat?",
        [
            "Erosie en afzetting zijn er in balans",
            "De plek waar de rivier even breed als diep is",
            "De lijn tussen twee stroombekkens in het landschap",
            "Het punt waar zoet en zout water elkaar raken",
        ],
        0,
        "Een rivier streeft naar een holle, vlotte lijn van bron tot monding.",
    ),
    tabel(
        "Erosie of sedimentatie in de rivier?",
        [
            ("de stroming versnelt", "Erosie"),
            ("de rivier mondt uit in een meer", "Sedimentatie"),
            ("hoog water na zware regen", "Erosie"),
            ("de binnenkant van een bocht", "Sedimentatie"),
        ],
        "Snel water neemt mee, traag water legt neer.",
        kolommen=["Erosie", "Sedimentatie"],
    ),
    tabel(
        "Klopt dit over een stuwwal?",
        [
            ("Een ijskap duwde de lagen voor zich op.", J),
            ("Je vindt stuwwallen in Nederland.", J),
            ("Een rivier zette hem af.", F),
        ],
        "Het ijs werkte als een bulldozer.",
    ),
    open_(
        "Leg uit hoe een meander zich in de loop van de tijd verplaatst.",
        "In een bocht stroomt het water aan de buitenkant het snelst. Daar schuurt het de holle oever weg. Aan de binnenkant gaat het trager en wordt zand afgezet op de bolle oever. Zo groeit de bocht naar buiten en schuift ze stroomafwaarts op.",
    ),
]
