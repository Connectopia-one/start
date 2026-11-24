"""Genregulatie, epigenetica en nature of nurture — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Lac-operon zonder lactose ------------------------------------------------
LO = Prent("lac-operon", "Het lac-operon van E. coli, zonder lactose in het milieu", "DNA als balk met vakken A tot E; boven de operator zit een eiwit vast")
LO.rect(40, 330, 920, 50, "#e8e8e8", DONKER, 4, 2)
VAKKEN = [("A", 60, 200, "#f2c14e"), ("B", 300, 120, "#cfe5f3"), ("C", 420, 90, "#f3c6d0"), ("D", 510, 430, "#9fd39a")]
for k, x, b, kl in VAKKEN:
    LO.rect(x, 330, b, 50, kl, DONKER, 4, 2)
for i, x in enumerate((510, 653, 796)):
    LO.lijn(x, 330, x, 380, DONKER, 2)
    LO.tekst(x + 72, 362, ("gen 1", "gen 2", "gen 3")[i], 15)
LO.tekst(160, 362, "regulatorgen", 15)
# repressor op operator
LO.pad("M420 330 C 410 270 430 230 465 230 C 500 230 520 270 510 330 Z", "#c8a8e0", DONKER, 2)
# repressor wordt gemaakt van A
LO.pijl(130, 320, 130, 240, GRIJS, 2)
LO.pad("M100 230 C 95 180 115 160 130 160 C 145 160 165 180 160 230 Z", "#c8a8e0", DONKER, 2)
LO.cirkel(360, 245, 34, "#dde6ee", DONKER, 2)
LO.tekst(360, 251, "RNA-pol", 13, vet=True)
LO.tekst(600, 470, "geen mRNA van gen 1, 2 en 3", 17, kleur=ROOD, vet=True)
LLO = {"A": (130, 440), "B": (360, 440), "C": (465, 440), "D": (580, 280), "E": (560, 200)}
LO.lijn(130, 418, 130, 382, DONKER, 1)
LO.lijn(360, 418, 360, 382, DONKER, 1)
LO.lijn(465, 418, 465, 382, DONKER, 1)
LO.lijn(580, 302, 580, 328, DONKER, 1)
LO.lijn(540, 210, 500, 240, DONKER, 1)
for k, (x, y) in LLO.items():
    LO.letter(x, y, k)
ZLO = {"A": [Prent.zone(60, 330, 200, 50), Prent.rond(*LLO["A"], 22)],
       "B": [Prent.zone(300, 330, 120, 50), Prent.rond(*LLO["B"], 22)],
       "C": [Prent.zone(420, 330, 90, 50), Prent.rond(*LLO["C"], 22)],
       "D": [Prent.zone(510, 330, 430, 50), Prent.rond(*LLO["D"], 22)],
       "E": [Prent.zone(415, 228, 100, 100), Prent.rond(100, 195, 35), Prent.rond(*LLO["E"], 22)]}

# Chromatine open en dicht -------------------------------------------------
CH = Prent("chromatine-open-dicht", "Twee stukken chromatine in dezelfde cel", "links strak opeengepakte nucleosomen met kleine bolletjes op het DNA, rechts losse nucleosomen met vlaggetjes op de histonen")
CH.tekst(250, 110, "stuk X", 20, vet=True)
CH.tekst(750, 110, "stuk Y", 20, vet=True)
for r in range(3):
    for c in range(3):
        x, y = 190 + c * 60, 220 + r * 75
        CH.cirkel(x, y, 30, "#c8a8e0", DONKER, 2)
CH.pad("M150 200 C 260 180 300 260 160 290 C 300 300 300 360 150 370", "none", BLAUW, 4)


def _bz(p0, p1, p2, p3, t):
    return tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t * t * c + t ** 3 * d for a, b, c, d in zip(p0, p1, p2, p3))


for kromme in (((150, 200), (260, 180), (300, 260), (160, 290)), ((160, 290), (300, 300), (300, 360), (150, 370))):
    for t in (0.2, 0.45, 0.7, 0.92):
        CH.cirkel(*_bz(*kromme, t), 7, ROOD, DONKER, 1)
CH.pad("M560 300 C 600 220 640 380 700 300 C 760 220 800 380 860 300 C 900 240 930 300 950 280", "none", BLAUW, 4)
for x in (630, 770, 900):
    CH.cirkel(x, 300, 30, "#c8a8e0", DONKER, 2)
    CH.lijn(x, 270, x, 230, DONKER, 2)
    CH.svg(f'<polygon points="{x},230 {x+26},238 {x},246" fill="{GROEN}" stroke="{DONKER}"/>')
CH.rect(120, 480, 760, 90, "#fbf6ea", DONKER, 12, 1.5)
CH.cirkel(160, 525, 7, ROOD, DONKER, 1)
CH.tekst(180, 531, "methylgroep op het DNA", 16, "start")
CH.svg(f'<polygon points="520,515 546,523 520,531" fill="{GROEN}" stroke="{DONKER}"/>')
CH.tekst(560, 531, "acetylgroep op een histon", 16, "start")
ZCH = {"X": [Prent.zone(140, 170, 220, 240)], "Y": [Prent.zone(550, 200, 410, 140)]}

VRAGEN = [
    klik(
        "Klik op de operator.",
        LO.bestand, ZLO["C"],
        "De operator ligt tussen de promotor en de genen. Daar bindt de repressor.",
    ),
    klik(
        "Klik op het gen dat doorlopend afgelezen wordt en voor de repressor codeert.",
        LO.bestand, ZLO["A"],
        "Het regulatorgen ligt buiten het operon.",
    ),
    met_prent(LO.bestand, tabel(
        "Kijk naar het lac-operon. Klopt dit?",
        [
            ("B is de aanlegplaats van RNA-polymerase.", J),
            ("E houdt de polymerase tegen.", J),
            ("De genen in D gaan samen aan of samen uit.", J),
            ("Komt er lactose bij, dan bindt die op B.", F),
        ],
        "Lactose bindt op de repressor E, die dan loslaat van de operator.",
    )),
    met_prent(LO.bestand, mk(
        "Er komt lactose in het milieu. Wat verandert er eerst op de tekening?",
        [
            "E laat de operator los",
            "A wordt uit het DNA geknipt",
            "D verhuist naar vóór de promotor",
            "De polymerase bindt op het regulatorgen",
        ],
        0,
        "Lactose werkt als inductor: ze verandert de vorm van de repressor.",
    )),
    klik(
        "Klik op het stuk chromatine waarvan de genen het best gelezen worden.",
        CH.bestand, ZCH["Y"],
        "Acetylgroepen maken het chromatine losser, zodat polymerase erbij kan.",
    ),
    met_prent(CH.bestand, tabel(
        "Kijk naar de twee stukken chromatine. Klopt dit?",
        [
            ("In X legt methylering de genen stil.", J),
            ("X lijkt op heterochromatine.", J),
            ("In X en Y is de volgorde van de basen anders.", F),
            ("Het patroon in X kan later weer veranderen.", J),
        ],
        "Epigenetica verandert de leesbaarheid, niet de letters van het DNA.",
    )),
    tabel(
        "Wat gebeurt er met het lac-operon?",
        [
            ("geen lactose", "Operon uit"),
            ("lactose aanwezig, geen glucose", "Operon aan"),
            ("de repressor zit op de operator", "Operon uit"),
            ("lactose zit vast op de repressor", "Operon aan"),
        ],
        "Zolang er glucose is, gebruikt de bacterie liever glucose.",
        kolommen=["Operon aan", "Operon uit"],
    ),
    koppel(
        "Koppel elk deel van het lac-operon aan zijn rol.",
        [
            ("promotor", "hier bindt RNA-polymerase"),
            ("operator", "hier bindt de repressor"),
            ("regulatorgen", "codeert voor de repressor"),
            ("lactose", "werkt als inductor"),
        ],
        ["knipt de introns weg"],
        "Bacteriën hebben vrijwel geen introns.",
    ),
    volgorde(
        "Zet de stappen in volgorde wanneer een bacterie plots lactose krijgt.",
        ["Lactose bindt op de repressor", "De repressor laat de operator los", "Polymerase leest de genen af", "De enzymen voor lactose worden gemaakt", "Lactose wordt afgebroken"],
        "Is alle lactose op, dan bindt de repressor opnieuw en gaat het operon uit.",
    ),
    mk(
        "Een bacterie heeft een fout in het regulatorgen: ze maakt geen werkende repressor. Wat gebeurt er?",
        [
            "Ze maakt de enzymen ook zonder lactose",
            "Ze kan daarna nooit nog lactose afbreken",
            "Ze maakt vanaf dan geen glucose meer aan",
            "Ze verliest het hele operon uit haar DNA",
        ],
        0,
        "Zonder repressor staat niets op de operator: het operon staat altijd aan.",
    ),
    tabel(
        "Epigenetisch of een verandering in het DNA zelf?",
        [
            ("een methylgroep op een cytosine", "Epigenetisch"),
            ("een base die door een andere vervangen wordt", "Verandering in het DNA"),
            ("acetylgroepen op de histonen", "Epigenetisch"),
            ("een stuk chromosoom dat wegvalt", "Verandering in het DNA"),
        ],
        "Epigenetica verandert niet de volgorde van de basen.",
        kolommen=["Epigenetisch", "Verandering in het DNA"],
    ),
    keuze(
        "Het afremmen van een gen door kleine stukjes RNA die op het mRNA binden, heet [[*RNA-interferentie|methylering|transcriptie]].",
        "Het gen zelf blijft staan, alleen het mRNA wordt stilgelegd of afgebroken.",
    ),
    mk(
        "Waarom kan een cel met RNA-interferentie sneller stoppen met een eiwit dan door het gen uit te zetten?",
        [
            "Het mRNA dat al klaar is, wordt stilgelegd",
            "Het gen wordt in één stap uit het DNA geknipt",
            "De ribosomen worden allemaal tegelijk afgebroken",
            "De cel gaat dan meteen en voorgoed in de G0-fase",
        ],
        0,
        "Wie alleen het gen uitzet, heeft nog al het mRNA dat al in het cytoplasma zit.",
    ),
    tabel(
        "Op welk niveau regelt de cel hier haar genexpressie?",
        [
            ("transcriptiefactoren binden op de promotor", "Transcriptie"),
            ("een micro-RNA bindt op het mRNA", "mRNA"),
            ("methylering legt een gen stil", "Transcriptie"),
            ("het mRNA wordt sneller afgebroken", "mRNA"),
        ],
        "Methylering houdt de transcriptiefactoren weg van het gen.",
        kolommen=["Transcriptie", "mRNA"],
    ),
    casus(
        "Eeneiige tweelingzussen Ella en Fien worden bij de geboorte gescheiden. Ella groeit op met veel sport en gezond eten, Fien met weinig beweging en veel stress. Op hun veertigste ziet de arts verschillen.",
        [
            keuze(
                "Hun DNA is [[*gelijk|totaal verschillend|half gelijk]].",
                "Eeneiige tweelingen komen uit één zygote.",
            ),
            tabel(
                "Kan dit verschil tussen Ella en Fien door de omgeving komen?",
                [
                    ("Fien heeft een hogere bloeddruk.", J),
                    ("Fien weegt meer.", J),
                    ("Ze hebben een andere bloedgroep.", F),
                    ("Hun DNA-methylering verschilt.", J),
                ],
                "De bloedgroep ligt volledig vast in het DNA.",
            ),
            mk(
                "Fien krijgt later een kind. Wat geldt voor haar epigenetische merktekens?",
                [
                    "Ze worden bij de gameten grotendeels gewist",
                    "Ze gaan altijd allemaal naar het kind",
                    "Ze veranderen de basen in het DNA van het kind",
                    "Ze gaan alleen naar zonen, niet naar dochters",
                ],
                0,
                "Een klein deel kan wel blijven, maar het meeste wordt gewist.",
            ),
        ],
    ),
    tabel(
        "Vooral nature, vooral nurture of allebei?",
        [
            ("de bloedgroep", "Vooral nature"),
            ("de taal die iemand spreekt", "Vooral nurture"),
            ("de lichaamslengte", "Allebei"),
            ("een hoge bloeddruk", "Allebei"),
        ],
        "Bij de meeste kenmerken werken aanleg en omgeving samen.",
        kolommen=["Vooral nature", "Vooral nurture", "Allebei"],
    ),
    sleep(
        "Bij [[methylering]] komt een kleine groep op het DNA en wordt een gen meestal [[stilgelegd]]. Bij [[acetylering]] van de histonen wordt het chromatine losser.",
        ["replicatie", "aangezet", "mutatie"],
        "Beide veranderingen kunnen weer ongedaan gemaakt worden.",
    ),
    tabel(
        "Klopt dit over celspecifieke genexpressie?",
        [
            ("Een spiercel en een levercel hebben hetzelfde DNA.", J),
            ("Ze lezen elk een ander deel van hun genen.", J),
            ("Genen voor de ribosomen staan in bijna alle cellen aan.", J),
            ("Een zenuwcel verliest de genen die ze niet gebruikt.", F),
        ],
        "De genen blijven, maar liggen opgerold of stilgelegd.",
    ),
    mk(
        "Waarom maakt E. coli de lactose-enzymen niet als er ook glucose is?",
        [
            "Glucose is zonder extra enzymen bruikbaar",
            "Glucose breekt de lactose zelf al af",
            "Lactose is giftig zolang er glucose is",
            "Glucose bindt op de promotor van het operon",
        ],
        0,
        "Enzymen maken kost energie: de bacterie spaart die zolang het kan.",
    ),
    tabel(
        "Kan dit het epigenetische patroon van iemand beïnvloeden?",
        [
            ("voeding", J),
            ("langdurige stress", J),
            ("roken", J),
            ("de kleur van de kleren die je draagt", F),
        ],
        "Zo kan de omgeving mee bepalen welke genen gelezen worden.",
    ),
    keuze(
        "Een stof die een operon aanzet, zoals lactose, heet een [[*inductor|repressor|promotor]].",
        "Ze haalt de repressor van de operator.",
    ),
    tabel(
        "Klopt dit over transcriptiefactoren?",
        [
            ("Ze binden in de buurt van de promotor.", J),
            ("Sommige zetten een gen aan, andere remmen het.", J),
            ("Welke er in een cel zijn, bepaalt mee het celtype.", J),
            ("Ze knippen het gen uit het DNA.", F),
        ],
        "Ze beslissen of een gen gelezen wordt, het gen zelf blijft staan.",
    ),
    inv(
        "Een operon heeft 3 genen voor 3 enzymen. Hoeveel signalen heeft de bacterie nodig om alle drie tegelijk aan te zetten?",
        ["1", "één", "een"],
        "Eén inductor zet het hele operon aan. Dat is net het voordeel.",
    ),
    tabel(
        "Klopt dit over een micro-RNA?",
        [
            ("Het is maar een twintigtal nucleotiden lang.", J),
            ("Het past op een stuk van een mRNA.", J),
            ("Het legt de translatie stil.", J),
            ("Het codeert zelf voor een eiwit.", F),
        ],
        "Het is een regelaar, geen boodschapper voor een eiwit.",
    ),
    keuze(
        "Het verschuiven en herschikken van de nucleosomen, waardoor genen beter of slechter leesbaar worden, heet [[*chromatine remodeling|DNA-replicatie|crossing-over]].",
        "Net als methylering en acetylering hoort het bij de epigenetica.",
    ),
    tabel(
        "Klopt dit over een plant die uit hetzelfde zaad in de schaduw opgroeit?",
        [
            ("Haar genotype is gelijk aan dat van een plant in de zon.", J),
            ("Haar fenotype kan anders zijn.", J),
            ("De schaduw verandert de basen in haar DNA.", F),
        ],
        "De omgeving werkt in op het fenotype.",
    ),
    mk(
        "Een cel heeft duizenden genen, maar leest er telkens maar een deel van. Wat is daarvan het voordeel?",
        [
            "Ze spaart energie en grondstoffen",
            "Zo blijft het DNA altijd binnen de kern",
            "Zo gaat de replicatie van het DNA sneller",
            "Zo heeft ze minder codons nodig",
        ],
        0,
        "Een cel maakt alleen de eiwitten die ze op dat moment nodig heeft.",
    ),
    open_(
        "Leg uit waarom men epigenetica een brug noemt tussen nature en nurture.",
        "Nature is de aanleg in het DNA, nurture de invloed van de omgeving. Bij epigenetica blijft het DNA gelijk, maar voeding, stress of roken veranderen mee welke genen gelezen worden, bv. door methylering of acetylering. Zo werkt de omgeving via de genen in op het fenotype.",
    ),
]
