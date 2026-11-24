"""Luchtdruk en winden — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Isobarenkaart -----------------------------------------------------------
IK = Prent("isobaren-kaart", "Isobaren boven een stuk van Europa (noordelijk halfrond)", "lagedrukgebied links met dichte isobaren, hogedrukgebied rechts met wijde isobaren, punten A tot D")
LX, LY = 300, 330
HX, HY = 790, 330
for i, d in enumerate([985, 990, 995, 1000, 1005]):
    r = 45 + i * 38
    IK.ellips(LX, LY, r * 1.1, r, "none", BLAUW, 2)
    IK.tekst(LX, LY - r - 4, str(d), 13, kleur=BLAUW)
for i, d in enumerate([1030, 1025, 1020]):
    r = 60 + i * 60
    IK.ellips(HX, HY, r * 1.05, r * 0.9, "none", ROOD, 2)
    IK.tekst(HX, HY - r * 0.9 - 4, str(d), 13, kleur=ROOD)
IK.tekst(LX, LY + 10, "L", 34, kleur=BLAUW, vet=True)
IK.tekst(HX, HY + 12, "H", 34, kleur=ROOD, vet=True)
PNT = {"A": (LX + 180, LY + 60), "B": (LX - 25, LY + 25), "C": (HX + 40, HY + 40), "D": (HX - 150, HY - 200)}
for k, (x, y) in PNT.items():
    IK.cirkel(x, y, 7, ORANJE, DONKER)
    IK.letter(x + 28, y - 22, k)
ZIK = {k: [Prent.rond(x, y, 22), Prent.rond(x + 28, y - 22, 24)] for k, (x, y) in PNT.items()}

# Drukgordels -------------------------------------------------------------
DG = Prent("drukgordels", "Drukgordels en winden aan de grond op het noordelijk halfrond", "breedtes van 0° tot 90° met drukgordels, windpijlen en zones P, Q, R")
L0, R0, T0, B0 = 230, 760, 70, 590
def GY(lat): return B0 - lat / 90 * (B0 - T0)
DG.rect(L0, T0, R0 - L0, B0 - T0, "#eef5fa", DONKER, 0)
GORD = [(0, "equatoriaal minimum", BLAUW), (30, "subtropisch maximum", ROOD), (60, "subpolair minimum", BLAUW), (90, "polair maximum", ROOD)]
for lat, naam, kl in GORD:
    DG.lijn(L0, GY(lat), R0, GY(lat), kl, 3)
    DG.tekst(L0 - 12, GY(lat) + 5, f"{lat}°", 16, "end")
    DG.tekst(R0 + 12, GY(lat) + 5, naam, 16, "start", kleur=kl)
def pijlen(lat1, lat2, dx, dy):
    for x in (330, 490, 650):
        ym = (GY(lat1) + GY(lat2)) / 2
        DG.pijl(x - dx / 2, ym - dy / 2, x + dx / 2, ym + dy / 2, DONKER, 3)
pijlen(0, 30, -70, 50)    # noordoostpassaat: naar het zuidwesten
pijlen(30, 60, 70, -50)   # westenwinden uit het zuidwesten
pijlen(60, 90, -70, 50)   # poolwinden uit het noordoosten
ZONES = {"P": (0, 30), "Q": (30, 60), "R": (60, 90)}
ZDG = {}
for k, (a, b2) in ZONES.items():
    DG.letter(L0 + 30, (GY(a) + GY(b2)) / 2 - 40, k)
    ZDG[k] = [Prent.zone(L0, GY(b2) + 6, R0 - L0, GY(a) - GY(b2) - 12)]
DG.tekst(R0, B0 + 32, "pijlen = windrichting aan de grond, noord is boven", 15, "end")

VRAGEN = [
    klik(
        "Klik op de plaats waar het het hardst waait.",
        IK.bestand, ZIK["A"],
        "Daar liggen de isobaren het dichtst bij elkaar: groot drukverschil over korte afstand.",
    ),
    klik(
        "Klik op de plaats waar de lucht daalt en het meestal droog en helder is.",
        IK.bestand, ZIK["C"],
        "In het centrum van een hogedrukgebied daalt de lucht.",
    ),
    met_prent(IK.bestand, tabel(
        "Kijk naar de kaart met isobaren. Klopt dit?",
        [
            ("Rond L draait de wind tegen de klok in.", J),
            ("Rond H draait de wind met de klok mee.", J),
            ("Bij D waait het harder dan bij A.", F),
            ("De kerndruk van L ligt onder 985 hPa.", J),
        ],
        "Op het noordelijk halfrond: laag tegen de klok in, hoog met de klok mee.",
    )),
    met_prent(IK.bestand, keuze(
        "Op plaats B stijgt de lucht op en is de kans op [[*regen|nachtvorst onder een heldere hemel|een windstille, droge dag]] groot.",
        "Stijgende lucht koelt af en vormt wolken.",
    )),
    klik(
        "Klik op de zone van de passaatwinden.",
        DG.bestand, ZDG["P"],
        "Tussen het subtropisch maximum en de evenaar.",
    ),
    klik(
        "Klik op de zone van de westenwinden, waarin ook België ligt.",
        DG.bestand, ZDG["Q"],
        "Tussen 30° en 60°: van het subtropisch maximum naar het subpolair minimum.",
    ),
    met_prent(DG.bestand, tabel(
        "Kijk naar de gordels. Thermisch of dynamisch?",
        [
            ("equatoriaal minimum", "Thermisch"),
            ("subtropisch maximum", "Dynamisch"),
            ("polair maximum", "Thermisch"),
            ("subpolair minimum", "Dynamisch"),
        ],
        "Thermisch door opwarming of afkoeling, dynamisch door de circulatie.",
        kolommen=["Thermisch", "Dynamisch"],
    )),
    met_prent(DG.bestand, tabel(
        "Kijk naar de gordels. Klopt dit?",
        [
            ("Op 30° daalt droge lucht, daar liggen veel woestijnen.", J),
            ("De passaatwinden komen op dit halfrond uit het noordoosten.", J),
            ("Bij 0° daalt de lucht en is het droog.", F),
        ],
        "Aan de evenaar stijgt warme lucht: veel regen.",
    )),
    tabel(
        "Hogedrukgebied of lagedrukgebied?",
        [
            ("anticycloon", "Hogedruk"),
            ("depressie", "Lagedruk"),
            ("maximum", "Hogedruk"),
            ("cycloon", "Lagedruk"),
            ("een kerndruk van 960 hPa", "Lagedruk"),
        ],
        "Depressie, minimum en cycloon zijn lagedrukgebieden.",
        kolommen=["Hogedruk", "Lagedruk"],
    ),
    tabel(
        "Een noordoostenwind bij ons: klopt dit?",
        [
            ("Hij komt uit het noordoosten.", J),
            ("Hij blaast naar het zuidwesten.", J),
            ("Hij is genoemd naar de richting waarheen hij waait.", F),
        ],
        "Een wind heet naar de richting waaruit hij komt.",
    ),
    tabel(
        "Draait de wind met of tegen de klok in?",
        [
            ("rond een depressie, noordelijk halfrond", "Tegen de klok in"),
            ("rond een anticycloon, noordelijk halfrond", "Met de klok mee"),
            ("rond een depressie, zuidelijk halfrond", "Met de klok mee"),
            ("rond een anticycloon, zuidelijk halfrond", "Tegen de klok in"),
        ],
        "Op het zuidelijk halfrond buigt alles naar links af.",
        kolommen=["Met de klok mee", "Tegen de klok in"],
    ),
    inv(
        "De gemiddelde luchtdruk aan zee is 1013 hPa. Een depressie heeft 978 hPa in de kern. Hoeveel hPa ligt dat onder het gemiddelde?",
        ["35"],
        "1013 - 978 = 35 hPa.",
    ),
    tabel(
        "Zeewind of landwind?",
        [
            ("op een warme zomernamiddag aan de kust", "Zeewind"),
            ("'s nachts aan de kust", "Landwind"),
            ("het land is warmer dan de zee", "Zeewind"),
            ("de zee is warmer dan het land", "Landwind"),
        ],
        "De wind waait naar het warmste deel, waar de lucht stijgt.",
        kolommen=["Zeewind", "Landwind"],
    ),
    volgorde(
        "Zet het ontstaan van een zeewind in de juiste volgorde.",
        [
            "Het land warmt sneller op dan de zee",
            "Boven het land stijgt warme lucht op",
            "De luchtdruk aan de grond boven het land daalt",
            "Koelere lucht stroomt van de zee naar het land",
        ],
        "Lucht stroomt van hoge naar lage druk.",
    ),
    mk(
        "Een orkaan trekt over de oceaan op 15° NB. Waarom kan zo'n storm niet ontstaan op 0°?",
        [
            "Het corioliseffect is daar te klein",
            "Het zeewater is daar veel te koud voor sterke stormen",
            "Er staat aan de evenaar eigenlijk nooit wind",
            "De zon staat er te laag om de lucht genoeg op te warmen",
        ],
        0,
        "Een orkaan heeft afbuiging nodig om rond een kern te gaan draaien.",
    ),
    tabel(
        "Klopt dit over de ITCZ?",
        [
            ("De passaatwinden van beide halfronden komen er samen.", J),
            ("Ze schuift mee met de zenitale zon.", J),
            ("Er valt veel convectieve regen.", J),
            ("Ze ligt het hele jaar precies op de evenaar.", F),
        ],
        "In onze zomer schuift ze naar het noorden.",
    ),
    tabel(
        "Klopt dit over de straalstroom?",
        [
            ("Hij waait op ongeveer 10 km hoogte.", J),
            ("Hij ligt op de grens van koude poollucht en warme lucht.", J),
            ("Hij stuurt de banen van depressies over Europa.", J),
            ("Het is een wind aan de grond, net boven de zee.", F),
        ],
        "Een smalle band zeer snelle hoogtewind.",
    ),
    koppel(
        "Koppel elk begrip over wind aan zijn uitleg.",
        [
            ("isobaar", "lijn van gelijke luchtdruk"),
            ("schaal van Beaufort", "windkracht van 0 tot 12"),
            ("circulatiecel", "kringloop van stijgende en dalende lucht"),
            ("moesson", "wind die twee keer per jaar van richting keert"),
        ],
        ["wind die elke dag twee keer keert"],
        "Dat laatste is de land- en zeewind.",
    ),
    casus(
        "Het is januari. Boven België ligt al een week een krachtig hogedrukgebied.",
        [
            tabel(
                "Wat verwacht je?",
                [
                    ("weinig wolken", J),
                    ("koude nachten met kans op vorst", J),
                    ("dagenlang zware regen", F),
                    ("weinig wind", J),
                ],
                "Dalende lucht doet wolken oplossen. In de winter koelt het dan 's nachts sterk af.",
            ),
            keuze(
                "In het centrum van dit gebied [[*daalt|stijgt|stopt]] de lucht.",
                "Een maximum heeft dalende lucht.",
            ),
        ],
    ),
    sleep(
        "Wind ontstaat door een verschil in [[luchtdruk]]. De lucht stroomt van [[hoge]] naar lage druk, maar buigt door het [[corioliseffect]] af.",
        ["temperatuur", "lage", "albedo"],
        "Op het noordelijk halfrond naar rechts.",
    ),
    inv(
        "Uit hoeveel richtingen per jaar waait een moesson?",
        ["2", "twee"],
        "In de zomer vochtig van de zee, in de winter droog van het land.",
    ),
    met_prent(DG.bestand, keuze(
        "In zone R waaien de [[*poolwinden|westenwinden|passaatwinden]], van het polair maximum naar het subpolair minimum.",
        "Ze komen uit het noordoosten.",
    )),
    met_prent(IK.bestand, inv(
        "Kijk naar de kaart. Hoeveel hPa verschillen twee naast elkaar liggende isobaren rond L?",
        ["5"],
        "985, 990, 995, 1000, 1005: telkens 5 hPa.",
    )),
    keuze(
        "Een wind van 12 op de schaal van Beaufort heet [[*orkaankracht|windstil|een zwakke bries]].",
        "Beaufort gaat van 0, windstil, tot 12, orkaankracht.",
    ),
    tabel(
        "Klopt dit over de luchtdruk?",
        [
            ("Het is het gewicht van de luchtkolom boven een plaats.", J),
            ("Op een bergtop is ze lager dan in het dal.", J),
            ("Je meet ze op een weerkaart in hectopascal.", J),
            ("Ze is overal op aarde op elk moment even groot.", F),
        ],
        "Verschillen in luchtdruk maken net de wind.",
    ),
    keuze(
        "Trekt de ene depressie na de andere over België, dan ligt de straalstroom [[*boven of net zuidelijk van ons|ver noordelijk van ons|boven de evenaar]].",
        "Depressies trekken mee onder de straalstroom.",
    ),
    inv(
        "Op welke breedte, in graden, liggen de subtropische maxima ongeveer?",
        ["30"],
        "De lucht die aan de evenaar opsteeg, daalt daar weer.",
    ),
    keuze(
        "De meest voorkomende wind in België komt uit het [[*zuidwesten|noordoosten|zuidoosten]].",
        "België ligt in de gordel van de westenwinden.",
    ),
    open_(
        "Leg uit waarom de grote woestijnen van de aarde rond 30° breedte liggen.",
        "De lucht die aan de evenaar opstijgt, daalt rond 30° weer neer. Dalende lucht warmt op en kan meer waterdamp vasthouden, dus vormen er zich geen wolken. Zo ontstaat een droge hogedrukgordel, het subtropisch maximum.",
    ),
]
