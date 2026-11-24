"""Overerving en de wetten van Mendel — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Stamboom kleurenblindheid -----------------------------------------------
ST = Prent("stamboom-kleurenblind", "Stamboom van een familie met kleurenblindheid", "drie generaties; vierkant = man, cirkel = vrouw, gevuld = kleurenblind; letters A tot E")


def _man(x, y, ziek=False):
    ST.rect(x - 28, y - 28, 56, 56, ROOD if ziek else "#ffffff", DONKER, 0, 2.5)


def _vrouw(x, y, ziek=False):
    ST.cirkel(x, y, 30, ROOD if ziek else "#ffffff", DONKER, 2.5)


# generatie I
ST.lijn(288, 140, 370, 140, DONKER, 2.5)
_man(260, 140)
_vrouw(400, 140)
ST.lijn(330, 140, 330, 200, DONKER, 2.5)
ST.lijn(200, 200, 460, 200, DONKER, 2.5)
for x in (200, 330, 460):
    ST.lijn(x, 200, x, 232, DONKER, 2.5)
# generatie II
_man(200, 260, True)
_man(330, 260)
_vrouw(460, 260)
ST.lijn(490, 260, 612, 260, DONKER, 2.5)
_man(640, 260)
ST.lijn(550, 260, 550, 340, DONKER, 2.5)
ST.lijn(420, 340, 680, 340, DONKER, 2.5)
for x in (420, 550, 680):
    ST.lijn(x, 340, x, 372, DONKER, 2.5)
# generatie III
_man(420, 400, True)
_vrouw(550, 400)
_man(680, 400)
for t, y in (("I", 140), ("II", 260), ("III", 400)):
    ST.tekst(90, y + 8, t, 22, vet=True)
LST = {"A": (400, 80), "B": (200, 330), "C": (525, 205), "D": (420, 470), "E": (550, 470)}
for k, (x, y) in LST.items():
    ST.letter(x, y, k)
ST.rect(110, 520, 780, 70, "#fbf6ea", DONKER, 12, 1.5)
ST.rect(140, 540, 30, 30, ROOD, DONKER, 0, 2)
ST.tekst(185, 562, "kleurenblind", 16, "start")
ST.rect(360, 540, 30, 30, "#ffffff", DONKER, 0, 2)
ST.tekst(405, 562, "man, ziet kleuren goed", 16, "start")
ST.cirkel(655, 555, 15, "#ffffff", DONKER, 2)
ST.tekst(680, 562, "vrouw, ziet kleuren goed", 16, "start")
_MID = {"A": (400, 140), "B": (200, 260), "C": (460, 260), "D": (420, 400), "E": (550, 400)}
ZST = {k: [Prent.rond(*_MID[k], 36), Prent.rond(*LST[k], 22)] for k in LST}

# Punnettvierkant bloedgroepen --------------------------------------------
PV = Prent("punnett-bloedgroep", "Kruising van een vader met bloedgroep A en een moeder met bloedgroep B", "vierkant van 2 op 2 met de gameten van vader bovenaan en van moeder links; vakjes P, Q, R en S")


def _gen(x, y, a, b, grootte=26):
    PV.svg(f'<text x="{x}" y="{y}" font-size="{grootte}" text-anchor="middle" fill="{DONKER}" font-weight="bold">{a}<tspan baseline-shift="super" font-size="{int(grootte*0.65)}">{b}</tspan></text>')


PV.tekst(560, 110, "gameten vader", 17)
PV.tekst(250, 330, "gameten moeder", 17, "end")
_gen(480, 175, "I", "A")
PV.tekst(640, 175, "i", 26, vet=True)
_gen(330, 280, "I", "B")
PV.tekst(330, 440, "i", 26, vet=True)
for i, (x, y, k) in enumerate(((400, 200, "P"), (560, 200, "Q"), (400, 360, "R"), (560, 360, "S"))):
    PV.rect(x, y, 160, 160, ("#f3c6d0", "#fff3d6", "#cfe5f3", "#ffffff")[i], DONKER, 0, 2.5)
LPV = {"P": (480, 320), "Q": (640, 320), "R": (480, 480), "S": (640, 480)}
_gen(462, 270, "I", "A")
_gen(500, 270, "I", "B")
_gen(630, 270, "I", "A")
PV.tekst(655, 270, "i", 26, vet=True)
_gen(470, 430, "I", "B")
PV.tekst(495, 430, "i", 26, vet=True)
PV.tekst(640, 430, "ii", 26, vet=True)
for k, (x, y) in LPV.items():
    PV.letter(x, y, k)
ZPV = {"P": [Prent.zone(400, 200, 160, 160)], "Q": [Prent.zone(560, 200, 160, 160)],
       "R": [Prent.zone(400, 360, 160, 160)], "S": [Prent.zone(560, 360, 160, 160)]}

VRAGEN = [
    klik(
        "Klik op een vrouw die zeker draagster is van kleurenblindheid.",
        ST.bestand, ZST["A"] + ZST["C"],
        "A heeft een kleurenblinde zoon, C ook. Een zoon krijgt zijn X altijd van zijn moeder.",
    ),
    met_prent(ST.bestand, tabel(
        "Kijk naar de stamboom. Klopt dit?",
        [
            ("B kreeg het allel voor kleurenblindheid van zijn moeder.", J),
            ("D kreeg het allel van zijn grootmoeder A, via zijn moeder C.", J),
            ("E heeft kans om draagster te zijn.", J),
            ("De vader van D is ook kleurenblind.", F),
        ],
        "De vader van D ziet kleuren goed. Een vader geeft aan een zoon zijn Y, niet zijn X.",
    )),
    met_prent(ST.bestand, mk(
        "Hoe groot is de kans dat E draagster is?",
        [
            "één op twee",
            "nul, want ze ziet goed",
            "één op vier",
            "zeker, want haar moeder is draagster",
        ],
        0,
        "E krijgt van haar vader een gezond X en van haar moeder C (XAXa) een gezond of een ziek X: 1 op 2.",
    )),
    klik(
        "Klik op het vakje van een kind met bloedgroep O.",
        PV.bestand, ZPV["S"],
        "Twee keer het recessieve allel i: bloedgroep O.",
    ),
    met_prent(PV.bestand, tabel(
        "Welke bloedgroep hoort bij het vakje?",
        [
            ("P", "AB"),
            ("Q", "A"),
            ("R", "B"),
            ("S", "O"),
        ],
        "IA en IB zijn codominant, en allebei dominant over i.",
        kolommen=["A", "B", "AB", "O"],
    )),
    met_prent(PV.bestand, inv(
        "Hoeveel procent kans heeft een kind van deze ouders op bloedgroep AB?",
        ["25", "25 %", "25%"],
        "Eén vakje van de vier.",
    )),
    tabel(
        "Welke verhouding van fenotypes verwacht je bij deze kruising?",
        [
            ("Aa x Aa, A dominant", "3 : 1"),
            ("Aa x aa", "1 : 1"),
            ("Rr x Rr, intermediair", "1 : 2 : 1"),
            ("AA x aa", "alles gelijk"),
        ],
        "Bij een intermediair kenmerk heeft elk genotype zijn eigen uitzicht.",
        kolommen=["3 : 1", "1 : 1", "1 : 2 : 1", "alles gelijk"],
    ),
    inv(
        "In de F2 van een monohybride kruising tel je 600 planten. Hoeveel verwacht je er met het recessieve kenmerk?",
        ["150"],
        "Een kwart van 600 = 150.",
    ),
    inv(
        "Bij een dihybride kruising AaBb x AaBb: hoeveel van de 16 vakjes tonen beide recessieve kenmerken?",
        ["1", "één"],
        "Alleen aabb: de 1 van 9 : 3 : 3 : 1.",
    ),
    inv(
        "Een plant met genotype AaBbCc: hoeveel soorten gameten kan ze maken als de genen op verschillende chromosomen liggen?",
        ["8", "acht"],
        "2 x 2 x 2 = 8.",
    ),
    casus(
        "Een kweker heeft een erwtenplant met paarse bloemen. Paars (P) is dominant over wit (p). Hij wil weten of de plant raszuiver is.",
        [
            keuze(
                "Hij kruist de plant best met een plant met [[*witte|paarse|roze]] bloemen.",
                "Een testkruising gebeurt met een homozygoot recessieve plant.",
            ),
            tabel(
                "Wat besluit hij uit het resultaat?",
                [
                    ("alle nakomelingen paars", "PP"),
                    ("ongeveer de helft wit", "Pp"),
                    ("een paar witte nakomelingen bij veel paarse", "Pp"),
                ],
                "Eén witte nakomeling bewijst al dat de plant een p-allel heeft.",
                kolommen=["PP", "Pp"],
            ),
            mk(
                "Waarom kweekt hij best veel nakomelingen?",
                [
                    "Bij weinig nakomelingen speelt het toeval te sterk",
                    "Bij weinig nakomelingen worden alle bloemen roze",
                    "Bij veel nakomelingen verandert het genotype van de plant",
                    "Bij weinig nakomelingen geldt de wet van Mendel niet meer",
                ],
                0,
                "Een verhouding komt pas te voorschijn bij grote aantallen.",
            ),
        ],
    ),
    tabel(
        "Dominant, intermediair of codominant?",
        [
            ("rood x wit geeft roze", "Intermediair"),
            ("bloedgroep AB", "Codominant"),
            ("paars x wit geeft paars bij erwten", "Dominant"),
            ("een koe met rode en witte haren door elkaar", "Codominant"),
        ],
        "Bij codominantie zie je beide kenmerken naast elkaar, niet gemengd.",
        kolommen=["Dominant", "Intermediair", "Codominant"],
    ),
    koppel(
        "Koppel elk begrip uit de erfelijkheidsleer aan zijn betekenis.",
        [
            ("homozygoot", "twee dezelfde allelen"),
            ("heterozygoot", "twee verschillende allelen"),
            ("genotype", "de allelen die iemand heeft"),
            ("fenotype", "het kenmerk dat je ziet"),
            ("locus", "de plaats van een gen op een chromosoom"),
        ],
        ["de insnoering van een chromosoom"],
        "De insnoering is het centromeer.",
    ),
    mk(
        "Een man met bloedgroep AB en een vrouw met bloedgroep O krijgen kinderen. Welke bloedgroep kan een kind NIET hebben?",
        [
            "AB",
            "A",
            "B",
            "Geen enkele, alles kan",
        ],
        0,
        "Het kind krijgt IA of IB van de vader en altijd i van de moeder: A of B.",
    ),
    tabel(
        "Kan een zoon dit kenmerk van zijn vader erven?",
        [
            ("een X-gebonden kenmerk", F),
            ("een kenmerk op chromosoom 7", J),
            ("een kenmerk op het Y-chromosoom", J),
            ("bloedgroep", J),
        ],
        "Een zoon krijgt van zijn vader de Y, nooit de X.",
    ),
    mk(
        "Een vrouw is draagster van hemofilie, haar man is gezond. Hoe groot is de kans dat een dochter hemofilie heeft?",
        [
            "nul, al kan ze draagster zijn",
            "één op twee, net als bij een zoon",
            "één op vier, want ze heeft twee X",
            "zeker, want de moeder is draagster",
        ],
        0,
        "Een dochter krijgt altijd het gezonde X van haar vader.",
    ),
    keuze(
        "Twee genen op hetzelfde chromosoom erven meestal samen over. Men noemt ze [[*gekoppeld|polygeen|letaal]].",
        "Alleen een crossing-over tussen de twee loci kan ze scheiden.",
    ),
    tabel(
        "Klopt dit over gekoppelde genen?",
        [
            ("Ze volgen de onafhankelijkheidswet niet.", J),
            ("Hoe verder ze uit elkaar liggen, hoe vaker crossing-over ze scheidt.", J),
            ("Ze liggen op verschillende chromosomen.", F),
            ("Een chiasma tussen beide loci kan nieuwe combinaties geven.", J),
        ],
        "Mendel werkte toevallig vooral met genen die niet gekoppeld waren.",
    ),
    mk(
        "Bij muizen geeft Yy x Yy een verhouding 2 gele op 1 grijze muis, en geen 3 op 1. Waarom?",
        [
            "YY is letaal: die muizen sterven voor de geboorte",
            "Y is codominant met y, zodat beide kleuren zichtbaar zijn",
            "De genen voor geel en grijs zijn gekoppeld op één chromosoom",
            "Geel is een polygeen kenmerk dat van veel genen afhangt",
        ],
        0,
        "Van AA, Aa, Aa, aa blijven alleen Aa, Aa en aa over: 2 op 1.",
    ),
    tabel(
        "Welk erfelijkheidspatroon past het best bij deze stamboom?",
        [
            ("komt in elke generatie voor, bij mannen en vrouwen evenveel", "Autosomaal dominant"),
            ("twee gezonde ouders krijgen een ziek kind, jongen of meisje", "Autosomaal recessief"),
            ("bijna alleen mannen, via gezonde moeders", "X-gebonden recessief"),
            ("slaat een generatie over, ook bij meisjes", "Autosomaal recessief"),
        ],
        "Een X-gebonden recessief kenmerk zie je vooral bij zonen van draagsters.",
        kolommen=["Autosomaal dominant", "Autosomaal recessief", "X-gebonden recessief"],
    ),
    sleep(
        "Lichaamslengte en huidkleur zijn [[polygeen]]: veel [[genen]] werken samen. Daarom zie je geen paar duidelijke klassen, maar een [[vloeiende]] reeks.",
        ["letaal", "allelen van één gen", "vaste"],
        "Bovendien speelt het milieu mee, zoals voeding.",
    ),
    tabel(
        "Klopt dit over Mendel?",
        [
            ("Hij werkte met erwtenplanten.", J),
            ("Hij sprak over erffactoren.", J),
            ("Hij gebruikte grote aantallen planten.", J),
            ("Hij kon de chromosomen al zien.", F),
        ],
        "Pas na zijn dood werden chromosomen in verband gebracht met erfelijkheid.",
    ),
    tabel(
        "Wat zegt de wet? Uniformiteitswet, splitsingswet of onafhankelijkheidswet?",
        [
            ("de hele F1 lijkt op elkaar", "Uniformiteit"),
            ("de twee allelen gaan naar verschillende gameten", "Splitsing"),
            ("twee kenmerken erven los van elkaar over", "Onafhankelijkheid"),
            ("in de F2 duikt het recessieve kenmerk weer op", "Splitsing"),
        ],
        "De onafhankelijkheidswet geldt voor genen op verschillende chromosomen.",
        kolommen=["Uniformiteit", "Splitsing", "Onafhankelijkheid"],
    ),
    inv(
        "Kruis Aa met aa. Hoeveel procent van de nakomelingen is heterozygoot?",
        ["50", "50 %", "50%"],
        "Aa, Aa, aa, aa: de helft.",
    ),
    keuze(
        "Een plant die van twee verschillende raszuivere lijnen komt, heet een [[*hybride|homozygoot|fenotype]].",
        "Een hybride is heterozygoot voor het kenmerk dat je volgt.",
    ),
    mk(
        "Wie bepaalt bij de mens of een kind een jongen of een meisje wordt?",
        [
            "De zaadcel, die een X of een Y meebrengt",
            "De eicel, die een X of een Y meebrengt",
            "De baarmoeder, door de hormonen van de moeder",
            "Het toeval bij de mitose van de zygote",
        ],
        0,
        "Een eicel draagt altijd een X.",
    ),
    inv(
        "Bij de mens zijn er voor het ABO-systeem drie allelen. Hoeveel verschillende genotypes zijn er dan mogelijk?",
        ["6", "zes"],
        "IAIA, IAi, IBIB, IBi, IAIB en ii.",
    ),
    open_(
        "Leg uit waarom kleurenblindheid veel vaker voorkomt bij mannen dan bij vrouwen.",
        "Het allel voor kleurenblindheid is recessief en ligt op het X-chromosoom. Een man heeft maar één X: heeft dat het allel, dan is hij kleurenblind. Een vrouw heeft twee X-chromosomen en is pas kleurenblind als beide het allel dragen. Met één gezond X is ze draagster en ziet ze goed.",
    ),
]
