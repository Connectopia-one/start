"""Biomoleculen: sachariden, lipiden en proteïnen — pittig (🧬 Beyond doorstroom, biologie)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vier structuren van een eiwit -------------------------------------------
ES = Prent("eiwitstructuren", "Vier niveaus in de bouw van een eiwit", "vier vakken P, Q, R en S: een rij bolletjes, een spiraal, een geplooide kluwen en twee kluwens samen")
for i in range(4):
    ES.rect(30 + i * 240, 110, 220, 400, "#fbf6ea", DONKER, 14, 1.5)
KLB = ["#e8a0b0", "#9fd39a", "#8fc1e3", "#f2c14e", "#c8a8e0"]
# P: kralen in een rij
for j in range(9):
    y = 150 + j * 38
    ES.cirkel(140, y, 15, KLB[j % 5], DONKER, 1.5)
    if j:
        ES.lijn(140, y - 23, 140, y - 15, DONKER, 2)
# Q: helix
pts = [(380 + 45 * math.sin(t / 4), 150 + t * 4.5) for t in range(0, 75)]
ES.pad("M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts), "none", ROOD, 6)
# R: kluwen
ES.pad("M560 200 C 700 160 700 260 600 270 C 520 280 540 360 640 340 C 720 320 700 420 610 430 C 540 440 560 380 600 380 C 640 380 650 460 580 470", "none", ROOD, 6)
# S: twee kluwens
for dx, kl in ((0, ROOD), (90, BLAUW)):
    ES.pad(f"M{780 + dx} 220 C {860 + dx} 200 {860 + dx} 280 {800 + dx} 290 C {750 + dx} 300 {760 + dx} 360 {820 + dx} 350 C {870 + dx} 340 {860 + dx} 420 {800 + dx} 430", "none", kl, 6)
for i, k in enumerate("PQRS"):
    ES.letter(140 + i * 240, 545, k)
ZES = {k: [Prent.zone(30 + i * 240, 110, 220, 400), Prent.rond(140 + i * 240, 545, 22)] for i, k in enumerate("PQRS")}

# Triglyceride ---------------------------------------------------------------
TG = Prent("triglyceride", "Een triglyceride (schematisch)", "links een korte staander met drie armen, aan elke arm een lange keten; de onderste keten heeft een knik; letters A tot D")
TG.rect(120, 150, 60, 340, "#f5d9a8", DONKER, 10, 2)
for j, y in enumerate((190, 320, 450)):
    TG.cirkel(205, y, 14, ROOD, DONKER, 1.5)
    TG.lijn(180, y, 191, y, DONKER, 2)
    if j < 2:
        xs = [230 + k * 42 for k in range(15)]
        TG.pad("M" + " L".join(f"{x} {y + (10 if k % 2 else -10)}" for k, x in enumerate(xs)), "none", DONKER, 3)
    else:
        xs = [230 + k * 42 for k in range(8)]
        p1 = [(x, y + (10 if k % 2 else -10)) for k, x in enumerate(xs)]
        hx, hy = p1[-1]
        p2 = [(hx + k * 36 + (6 if k % 2 else -6), hy + k * 18 + (6 if k % 2 else -6)) for k in range(1, 8)]
        TG.pad("M" + " L".join(f"{x:.0f} {y2:.0f}" for x, y2 in p1 + p2), "none", DONKER, 3)
        TG.lijn(hx - 6, hy - 18, hx + 34, hy + 0, DONKER, 3)
LTG = {"A": (150, 560), "B": (550, 250), "C": (420, 560), "D": (240, 400)}
TG.lijn(150, 538, 150, 492, DONKER, 1)
TG.lijn(550, 272, 550, 300, DONKER, 1)
TG.lijn(435, 540, 515, 470, DONKER, 1)
TG.lijn(232, 418, 210, 440, DONKER, 1)
for k, (x, y) in LTG.items():
    TG.letter(x, y, k)
ZTG = {"A": [Prent.zone(120, 150, 60, 340), Prent.rond(*LTG["A"], 22)],
       "B": [Prent.zone(225, 170, 600, 40), Prent.zone(225, 300, 600, 40), Prent.rond(*LTG["B"], 22)],
       "C": [Prent.zone(490, 420, 90, 80), Prent.rond(*LTG["C"], 22)],
       "D": [Prent.rond(205, 450, 18), Prent.rond(205, 320, 18), Prent.rond(205, 190, 18), Prent.rond(*LTG["D"], 22)]}

VRAGEN = [
    klik(
        "Klik op de primaire structuur.",
        ES.bestand, ZES["P"],
        "De primaire structuur is de volgorde van de aminozuren.",
    ),
    klik(
        "Klik op een eiwit met een quaternaire structuur.",
        ES.bestand, ZES["S"],
        "Een quaternaire structuur bestaat uit meerdere ketens samen, zoals hemoglobine.",
    ),
    met_prent(ES.bestand, tabel(
        "Kijk naar de vier niveaus. Klopt dit?",
        [
            ("Q is een α-helix, een vorm van de secundaire structuur.", J),
            ("R wordt vastgehouden door bv. disulfidebindingen.", J),
            ("Bij denaturatie gaat de vorm van R verloren.", J),
            ("Bij denaturatie verandert de volgorde in P.", F),
        ],
        "Hitte breekt de zwakke bindingen, maar de peptidebindingen blijven.",
    )),
    klik(
        "Klik op de glycerol.",
        TG.bestand, ZTG["A"],
        "Een triglyceride is één glycerol met drie vetzuren.",
    ),
    klik(
        "Klik op de plaats van een dubbele binding.",
        TG.bestand, ZTG["C"],
        "Een dubbele binding geeft een knik in de keten: dat vetzuur is onverzadigd.",
    ),
    met_prent(TG.bestand, tabel(
        "Kijk naar de triglyceride. Klopt dit?",
        [
            ("De bovenste twee vetzuren zijn verzadigd.", J),
            ("Door de knik stapelen deze moleculen minder goed.", J),
            ("Bij D ontstond bij de vorming water.", J),
            ("Deze molecule is goed oplosbaar in water.", F),
        ],
        "De lange koolwaterstofketens zijn hydrofoob.",
    )),
    tabel(
        "Monosacharide, disacharide of polysacharide?",
        [
            ("glucose", "Mono"),
            ("lactose", "Di"),
            ("glycogeen", "Poly"),
            ("fructose", "Mono"),
            ("sacharose", "Di"),
        ],
        "Lactose is glucose met galactose, sacharose glucose met fructose.",
        kolommen=["Mono", "Di", "Poly"],
    ),
    koppel(
        "Koppel elke disacharide aan zijn twee bouwstenen.",
        [
            ("sacharose", "glucose en fructose"),
            ("lactose", "glucose en galactose"),
            ("maltose", "glucose en glucose"),
        ],
        ["glycerol en vetzuren", "aminozuren"],
        "Glycerol en vetzuren vormen een vet.",
    ),
    tabel(
        "Condensatie of hydrolyse?",
        [
            ("twee aminozuren vormen een dipeptide", "Condensatie"),
            ("zetmeel wordt in de darm tot glucose gesplitst", "Hydrolyse"),
            ("er komt water vrij", "Condensatie"),
            ("er wordt water verbruikt", "Hydrolyse"),
        ],
        "Opbouwen gaat met condensatie, afbreken met hydrolyse.",
        kolommen=["Condensatie", "Hydrolyse"],
    ),
    sorteer(
        "Wat is de rol van deze polysacharide?",
        ["Energie opslaan", "Stevigheid geven"],
        [
            ("zetmeel in een aardappel", "Energie opslaan"),
            ("glycogeen in de lever", "Energie opslaan"),
            ("cellulose in een celwand", "Stevigheid geven"),
            ("amylopectine", "Energie opslaan"),
        ],
        "Cellulose vormt rechte ketens die als kabels naast elkaar liggen.",
    ),
    mk(
        "Zetmeel en cellulose zijn allebei ketens van glucose. Waarom haalt een mens alleen uit zetmeel energie?",
        [
            "Hij mist het enzym voor de binding in cellulose",
            "Cellulose lost in de maag meteen helemaal op",
            "Een mens maakt geen enkel verteringsenzym",
            "Cellulose bestaat eigenlijk uit aminozuren",
        ],
        0,
        "De binding in cellulose is anders gericht dan die in zetmeel.",
    ),
    inv(
        "Hoeveel watermoleculen komen er vrij als een triglyceride gevormd wordt uit glycerol en drie vetzuren?",
        ["3", "drie"],
        "Voor elke binding één condensatie: drie keer water.",
    ),
    inv(
        "Hoeveel peptidebindingen telt een keten van 50 aminozuren?",
        ["49"],
        "Tussen n aminozuren liggen n - 1 bindingen.",
    ),
    tabel(
        "Verzadigd of onverzadigd vetzuur?",
        [
            ("heeft één of meer dubbele bindingen", "Onverzadigd"),
            ("rechte keten", "Verzadigd"),
            ("zit veel in olijfolie", "Onverzadigd"),
            ("zit veel in boter", "Verzadigd"),
        ],
        "Geknikte ketens stapelen minder goed: daarom is olie vloeibaar.",
        kolommen=["Verzadigd", "Onverzadigd"],
    ),
    tabel(
        "Klopt dit over fosfolipiden?",
        [
            ("De kop is hydrofiel.", J),
            ("De staarten zijn hydrofoob.", J),
            ("In water vormen ze een dubbele laag.", J),
            ("De staarten keren zich naar het water toe.", F),
        ],
        "De staarten verbergen zich in het midden van de laag.",
    ),
    mk(
        "Waarom levert een gram vet meer energie dan een gram suiker?",
        [
            "De ketens bevatten meer waterstof",
            "Vet wordt sneller in het bloed opgenomen",
            "Vet bevat meer zuurstofatomen dan suiker",
            "Suiker kan niet verbrand worden",
        ],
        0,
        "De ketens zijn sterker gereduceerd: bij verbranding komt meer energie vrij.",
    ),
    tabel(
        "Welke functie heeft deze proteïne?",
        [
            ("amylase", "Enzym"),
            ("actine en myosine", "Beweging"),
            ("antilichaam", "Afweer"),
            ("aquaporine", "Transport"),
            ("pepsine", "Enzym"),
        ],
        "Aquaporine is een kanaaleiwit voor water.",
        kolommen=["Enzym", "Beweging", "Afweer", "Transport"],
    ),
    casus(
        "Je kookt een ei. Het doorzichtige eiwit wordt wit en vast.",
        [
            keuze(
                "De eiwitten zijn [[*gedenatureerd|gehydrolyseerd|gecondenseerd]].",
                "De hitte breekt de zwakke bindingen die de vorm vasthouden.",
            ),
            tabel(
                "Wat is er veranderd in de eiwitten?",
                [
                    ("de tertiaire structuur", J),
                    ("de secundaire structuur", J),
                    ("de volgorde van de aminozuren", F),
                ],
                "De peptidebindingen blijven: de primaire structuur blijft gelijk.",
            ),
            mk(
                "Waarom is hoge koorts gevaarlijk voor de enzymen in je lichaam?",
                [
                    "Hun actief centrum verliest zijn vorm",
                    "Ze worden dan allemaal omgezet in vetten",
                    "Hun aminozuren veranderen van volgorde",
                    "Ze verlaten dan alle cellen tegelijk",
                ],
                0,
                "Zonder juiste vorm past het substraat niet meer.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over aminozuren?",
        [
            ("Elk aminozuur heeft een aminogroep en een carboxylgroep.", J),
            ("De restgroep verschilt van aminozuur tot aminozuur.", J),
            ("Een keten heeft een N-terminus en een C-terminus.", J),
            ("Alle aminozuren hebben dezelfde restgroep.", F),
        ],
        "Polaire en apolaire restgroepen sturen de plooiing.",
    ),
    sleep(
        "Zetmeel bestaat uit [[amylose]], een lange spiraal, en [[amylopectine]], dat sterk vertakt is. Dieren slaan suiker op als [[glycogeen]].",
        ["cellulose", "keratine", "cholesterol"],
        "Glycogeen zit vooral in de lever en de spieren.",
    ),
    tabel(
        "Klopt dit over lipiden?",
        [
            ("Cholesterol is een steroïde.", J),
            ("Vetweefsel houdt warmte vast.", J),
            ("Vitamine A, D, E en K lossen op in vet.", J),
            ("Cholesterol zit vooral in de celwand van planten.", F),
        ],
        "Cholesterol zit in het celmembraan van dierlijke cellen.",
    ),
    keuze(
        "Het eiwit dat haren en nagels hun hardheid geeft, heet [[*keratine|collageen|myosine]].",
        "Het zit vol disulfidebindingen.",
    ),
    mk(
        "Waarom geeft druivensuiker sneller energie dan een boterham?",
        [
            "Glucose hoeft niet meer gesplitst te worden",
            "Een boterham bevat helemaal geen suikers",
            "Zetmeel wordt in de maag al tot vet omgezet",
            "Glucose wordt pas in de dikke darm opgenomen",
        ],
        0,
        "Zetmeel moet eerst met hydrolyse in glucose gesplitst worden.",
    ),
    tabel(
        "Klopt dit over de glycosidische binding?",
        [
            ("Ze verbindt twee suikerringen.", J),
            ("Ze ontstaat bij een condensatiereactie.", J),
            ("Ze wordt bij de vertering met hydrolyse verbroken.", J),
            ("Ze verbindt twee aminozuren.", F),
        ],
        "Tussen aminozuren ligt een peptidebinding.",
    ),
    tabel(
        "Ring van vijf of ring van zes atomen in opgeloste vorm?",
        [
            ("glucose", "Zes"),
            ("fructose", "Vijf"),
            ("galactose", "Zes"),
        ],
        "Glucose en galactose sluiten tot een zesring, fructose tot een vijfring.",
        kolommen=["Vijf", "Zes"],
    ),
    keuze(
        "Een molecule die water afstoot, zoals een vetzuurstaart, noemt men [[*hydrofoob|hydrofiel|polair]].",
        "Hydrofoob betekent watervrezend.",
    ),
    tabel(
        "Klopt dit over de afbraak van proteïnen in de darm?",
        [
            ("Water splitst de peptidebindingen.", J),
            ("Enzymen versnellen die hydrolyse.", J),
            ("Er blijven losse aminozuren over.", J),
            ("Er komen glycerol en vetzuren vrij.", F),
        ],
        "Glycerol en vetzuren komen vrij bij de vertering van vetten.",
    ),
    open_(
        "Leg uit waarom de volgorde van de aminozuren de werking van een eiwit bepaalt.",
        "De volgorde van de aminozuren is de primaire structuur. Polaire en apolaire restgroepen trekken elkaar aan of stoten elkaar af, en sommige vormen bindingen, zoals disulfidebruggen. Zo plooit de keten tot een vaste vorm. Alleen met de juiste vorm past een eiwit op zijn partner, bv. een enzym op zijn substraat.",
    ),
]
