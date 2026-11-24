"""Gametogenese en de hormonale regeling — pittig (🧬 Beyond doorstroom, biologie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Cyclus -----------------------------------------------------------------
CY = Prent("hormonen-cyclus", "Hormonen in het bloed tijdens een cyclus van 28 dagen (vereenvoudigd)", "vier curves: hormoon 1 met smalle piek op dag 14, hormoon 2 met kleine piek op dag 14, hormoon 3 stijgt voor dag 14, hormoon 4 hoog rond dag 21")
X, Y = assen(CY, 0, 28, 0, 100, "dag van de cyclus", "hoeveelheid", 2, 25, links=130, rechts=900)
def g(t, m, s, h):
    return h * math.exp(-((t - m) / s) ** 2)
CURVES = {
    "1": (lambda t: 10 + g(t, 14, 0.9, 85), ROOD),
    "2": (lambda t: 14 + g(t, 3, 3, 8) + g(t, 14, 1.0, 30), ORANJE),
    "3": (lambda t: 12 + g(t, 12.5, 2.2, 55) + g(t, 21, 3, 25), BLAUW),
    "4": (lambda t: 5 + g(t, 21, 3.2, 70), PAARS),
}
for k, (f, kl) in CURVES.items():
    CY.pad("M" + " L ".join(f"{X(t / 10):.1f} {Y(f(t / 10)):.1f}" for t in range(0, 281)), "none", kl, 4)
POS = {"1": (15.6, 90), "2": (16.2, 40), "3": (10.2, 60), "4": (24, 65)}
for k, (t, a) in POS.items():
    CY.letter(X(t), Y(a), k)
ZCY = {k: [Prent.rond(X(t), Y(a), 24)] for k, (t, a) in POS.items()}
ZCY["1"].append(Prent.zone(X(13.3), Y(95), X(14.7) - X(13.3), Y(30) - Y(95)))
ZCY["4"].append(Prent.zone(X(18), Y(76), X(24) - X(18), 40))
CY.svg(f'<rect x="{X(0):.0f}" y="{Y(0) - 14:.0f}" width="{X(5) - X(0):.0f}" height="14" fill="#d9534f" opacity="0.6"/>')
CY.tekst(X(2.5), Y(0) - 20, "menstruatie", 13)

# Zaadcel ----------------------------------------------------------------
ZC = Prent("zaadcel-bouw", "Bouw van een zaadcel (sterk vergroot)", "kop met kapje vooraan, middenstuk, lange staart; letters A tot D")
ZC.ellips(230, 320, 90, 60, "#cfe3f0", DONKER, 2)
ZC.pad("M150 290 Q 120 320 150 350 Q 175 320 150 290 Z", "#f2c14e", DONKER, 2)
ZC.ellips(240, 320, 45, 32, "#8a6db0", "none", 0)
ZC.rect(318, 300, 130, 40, "#f2a66a", DONKER, 10, 2)
for x in range(330, 445, 18):
    ZC.pad(f"M{x} 305 q 6 15 0 30", "none", DONKER, 1.5)
ZC.pad("M448 320 C 540 260 600 380 690 320 C 780 260 840 380 940 320", "none", DONKER, 4)
LZC = {"A": (130, 230), "B": (240, 420), "C": (383, 400), "D": (800, 410)}
ZC.lijn(140, 250, 150, 290, DONKER, 1)
ZC.lijn(240, 400, 240, 352, DONKER, 1)
ZC.lijn(383, 380, 383, 340, DONKER, 1)
for k, (x, y) in LZC.items():
    ZC.letter(x, y, k)
ZZC = {"A": [Prent.zone(130, 285, 50, 70), Prent.rond(*LZC["A"], 24)],
       "B": [Prent.rond(240, 320, 40), Prent.rond(*LZC["B"], 24)],
       "C": [Prent.zone(318, 295, 130, 50), Prent.rond(*LZC["C"], 24)],
       "D": [Prent.zone(450, 260, 490, 120), Prent.rond(*LZC["D"], 24)]}

VRAGEN = [
    klik(
        "Klik op het hormoon dat met een plotse piek de ovulatie veroorzaakt.",
        CY.bestand, ZCY["1"],
        "De LH-piek laat de Graafse follikel barsten.",
    ),
    klik(
        "Klik op het hormoon dat vooral door het geel lichaam gemaakt wordt.",
        CY.bestand, ZCY["4"],
        "Progesteron is hoog in de luteale fase.",
    ),
    met_prent(CY.bestand, tabel(
        "Kijk naar de cyclus. Welk hormoon is welke curve?",
        [
            ("LH", "1"),
            ("FSH", "2"),
            ("oestrogeen", "3"),
            ("progesteron", "4"),
        ],
        "Oestrogeen stijgt mee met de rijpende follikels, progesteron komt na de ovulatie.",
        kolommen=["1", "2", "3", "4"],
    )),
    met_prent(CY.bestand, tabel(
        "Kijk naar de hormonen tijdens de cyclus. Klopt dit?",
        [
            ("De ovulatie valt rond dag 14.", J),
            ("Na dag 14 volgt de luteale fase.", J),
            ("Als curve 4 daalt, begint een nieuwe menstruatie.", J),
            ("Curve 3 is het hoogst tijdens de menstruatie.", F),
        ],
        "Zakt het progesteron, dan wordt het slijmvlies afgestoten.",
    )),
    klik(
        "Klik op het deel met de enzymen om bij de eicel te geraken.",
        ZC.bestand, ZZC["A"],
        "Het acrosoom vooraan op de kop.",
    ),
    klik(
        "Klik op het deel dat de energie levert voor het zwemmen.",
        ZC.bestand, ZZC["C"],
        "Het middenstuk zit vol mitochondria.",
    ),
    met_prent(ZC.bestand, tabel(
        "Kijk naar de zaadcel. Klopt dit?",
        [
            ("In B zitten 23 chromosomen.", J),
            ("D is opgebouwd uit microtubuli.", J),
            ("De zaadcel heeft veel cytoplasma als voorraad.", F),
        ],
        "Een zaadcel is bijna enkel kern en motor.",
    )),
    volgorde(
        "Zet de stappen van de spermatogenese in volgorde.",
        ["Spermatogonium", "Primaire spermatocyt", "Secundaire spermatocyt", "Spermatide", "Spermatozoïde"],
        "Twee meiotische delingen en dan rijping.",
    ),
    volgorde(
        "Zet de follikels in volgorde van rijping.",
        ["Primordiale follikel", "Primaire follikel", "Secundaire follikel", "Graafse follikel", "Geel lichaam"],
        "Na de ovulatie wordt de lege follikel het geel lichaam.",
    ),
    tabel(
        "Spermatogenese of oögenese?",
        [
            ("vier bruikbare cellen uit één voorlopercel", "Spermatogenese"),
            ("poollichaampjes", "Oögenese"),
            ("loopt onafgebroken vanaf de puberteit", "Spermatogenese"),
            ("start al voor de geboorte", "Oögenese"),
            ("de cel krijgt veel cytoplasma", "Oögenese"),
        ],
        "Eén grote eicel, veel kleine zaadcellen.",
        kolommen=["Spermatogenese", "Oögenese"],
    ),
    koppel(
        "Koppel elke cel aan haar taak.",
        [
            ("cel van Sertoli", "voedt de rijpende zaadcellen"),
            ("cel van Leydig", "maakt testosteron"),
            ("geel lichaam", "maakt progesteron"),
            ("Graafse follikel", "barst bij de ovulatie"),
        ],
        ["maakt hCG bij een zwangerschap"],
        "hCG komt van het jonge embryo.",
    ),
    tabel(
        "Welk hormoon werkt hier?",
        [
            ("de hypothalamus stuurt de hypofyse aan", "GnRH"),
            ("follikels laten rijpen", "FSH"),
            ("het slijmvlies laten opbouwen", "oestrogeen"),
            ("Sertolicellen remmen FSH", "inhibine"),
        ],
        "Een keten van hormonen met terugkoppeling.",
        kolommen=["GnRH", "FSH", "oestrogeen", "inhibine"],
    ),
    casus(
        "Een vrouw doet een zwangerschapstest. Hij is positief. Haar menstruatie blijft uit.",
        [
            keuze(
                "De test meet het hormoon [[*hCG|LH|FSH]].",
                "Dat maakt het jonge embryo.",
            ),
            keuze(
                "Dat hormoon houdt het [[*geel lichaam|Graafse follikel|poollichaampje]] in stand.",
                "Zo blijft er progesteron.",
            ),
            tabel(
                "Klopt dit over haar hormonen?",
                [
                    ("Het progesteron blijft hoog.", J),
                    ("Het baarmoederslijmvlies blijft dik.", J),
                    ("Er komt elke maand een nieuwe ovulatie.", F),
                ],
                "Hoog oestrogeen en progesteron remmen FSH en LH.",
            ),
        ],
    ),
    mk(
        "Waarom hangen de teelballen buiten de buikholte?",
        [
            "Zaadcellen ontwikkelen het best iets koeler",
            "Zo kunnen ze makkelijker testosteron afgeven",
            "Zo is er meer ruimte voor de blaas in de buik",
            "Daar komen ze beter in contact met de bijnieren",
        ],
        0,
        "Een paar graden onder 37 °C.",
    ),
    sleep(
        "Bij de oögenese krijgt de eicel bijna al het [[cytoplasma]]. De kleine cellen zonder voorraad heten [[poollichaampjes]]. Zo heeft de eicel [[voorraad]] voor het begin van de ontwikkeling.",
        ["DNA", "follikels", "testosteron"],
        "Ongelijke verdeling met een doel.",
    ),
    tabel(
        "Klopt dit over negatieve feedback?",
        [
            ("Het product remt zijn eigen aanmaak.", J),
            ("Veel testosteron remt GnRH en LH.", J),
            ("De pil steunt erop.", J),
            ("Het versterkt een hormoon tot het maximum.", F),
        ],
        "Zo blijft een hormoonspiegel binnen grenzen.",
    ),
    mk(
        "Op welk moment rondt de secundaire oöcyt haar meiose helemaal af?",
        [
            "Pas als ze bevrucht wordt",
            "Al vóór de geboorte van het meisje",
            "Op de dag van de menstruatie",
            "Net na de LH-piek, nog in de eierstok",
        ],
        0,
        "Ze blijft in de metafase staan tot er een zaadcel binnendringt.",
    ),
    tabel(
        "Welke klier levert dit aan het sperma?",
        [
            ("suikerrijk vocht als brandstof", "zaadblaasjes"),
            ("melkachtig vocht", "prostaat"),
            ("voorvocht dat de urinebuis spoelt", "klieren van Cowper"),
        ],
        "Samen met de zaadcellen vormt dat sperma.",
        kolommen=["zaadblaasjes", "prostaat", "klieren van Cowper"],
    ),
    tabel(
        "Klopt dit over de menstruatie?",
        [
            ("Ze begint als het progesteron zakt.", J),
            ("Het baarmoederslijmvlies wordt afgestoten.", J),
            ("Ze komt door een plotse stijging van progesteron.", F),
        ],
        "Zonder progesteron houdt het slijmvlies niet stand.",
    ),
    inv(
        "Uit één primaire spermatocyt ontstaan 4 zaadcellen. Hoeveel zaadcellen geven 250 primaire spermatocyten?",
        ["1000", "1 000"],
        "250 x 4 = 1 000.",
    ),
    tabel(
        "Klopt dit over testosteron?",
        [
            ("Het houdt de spermatogenese op gang.", J),
            ("Het vormt de secundaire geslachtskenmerken.", J),
            ("LH zet de cellen van Leydig aan om het te maken.", J),
            ("Het daalt bij mannen plots rond 50 jaar.", F),
        ],
        "Bij de man zakt het heel traag.",
    ),
    keuze(
        "De franjes van de eileider vangen de eicel op na de [[*ovulatie|menstruatie|bevruchting]].",
        "Ze strijken over de eierstok.",
    ),
    tabel(
        "Klopt dit over het voorvocht?",
        [
            ("Het komt uit de klieren van Cowper.", J),
            ("Er kunnen al zaadcellen in zitten.", J),
            ("Terugtrekken is daarom geen betrouwbare voorbehoedsmethode.", J),
            ("Het bevat nooit zaadcellen.", F),
        ],
        "Er kunnen zaadcellen uit de zaadleider meekomen.",
    ),
    mk(
        "Een arts vindt in een spermastaal veel zaadcellen, maar ze bewegen nauwelijks. Waar ligt het probleem waarschijnlijk?",
        [
            "In het middenstuk",
            "In het acrosoom op de kop",
            "In het aantal chromosomen",
            "In de klieren van Cowper",
        ],
        0,
        "Zonder ATP beweegt de staart niet.",
    ),
    keuze(
        "Bij de geboorte heeft een meisje al haar [[*primaire oöcyten|rijpe eicellen|Graafse follikels]] in de eierstok.",
        "Ze staan stil in de eerste meiotische deling.",
    ),
    tabel(
        "Welke lagen liggen rond een vrijgekomen eicel?",
        [
            ("zona pellucida", J),
            ("corona radiata", J),
            ("acrosoom", F),
        ],
        "Het acrosoom zit op de zaadcel.",
    ),
    tabel(
        "Hoeveel chromosomen heeft deze cel bij de mens?",
        [
            ("zaadcel", "23"),
            ("eicel", "23"),
            ("spermatogonium", "46"),
        ],
        "Gameten zijn haploïd.",
        kolommen=["23", "46"],
    ),
    open_(
        "Leg uit waarom de menstruatie uitblijft als een vrouw zwanger is.",
        "Het jonge embryo maakt hCG. Daardoor blijft het geel lichaam bestaan en progesteron maken. Zolang het progesteron hoog blijft, wordt het baarmoederslijmvlies niet afgestoten, dus komt er geen menstruatie.",
    ),
]
