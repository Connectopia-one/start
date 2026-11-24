"""Bevruchting, embryo en foetus — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Route ------------------------------------------------------------------
RT = Prent("route-eileider", "Van ovulatie tot innesteling (schematisch)", "eierstok links, eileider als boog, baarmoeder rechts; punten A tot E langs de weg")
RT.ellips(130, 420, 70, 45, "#f3c6d0", DONKER, 2)
RT.tekst(130, 490, "eierstok", 15)
RT.pad("M190 360 C 260 200 450 160 620 230", "none", "#e8a0b0", 34)
RT.pad("M190 360 C 260 200 450 160 620 230", "none", DONKER, 1)
RT.pad("M600 180 C 700 140 900 160 920 300 C 930 420 860 560 760 580 C 660 560 600 420 610 300 Z", "#f3c6d0", DONKER, 3)
RT.pad("M640 230 C 720 200 870 210 880 310 C 885 400 830 520 760 530 C 690 520 650 410 650 320 Z", "#e8a0b0", DONKER, 1)
RT.tekst(770, 620, "baarmoeder", 15)
for x, y, r in ((175, 380, 10), (240, 265, 10), (360, 200, 13), (500, 190, 14)):
    RT.cirkel(x, y, r, "#fff3d6", DONKER, 1.5)
for dx, dy in ((-4, -4), (4, -4), (-4, 4), (4, 4)):
    RT.cirkel(500 + dx, 190 + dy, 4, "#f2c14e", DONKER, 0.5)
RT.cirkel(870, 330, 18, "#fff3d6", DONKER, 1.5)
RT.cirkel(864, 330, 7, PAARS, "none", 0)
LRT = {"A": (175, 320), "B": (240, 215), "C": (360, 140), "D": (500, 130), "E": (930, 360)}
for k, (x, y) in LRT.items():
    RT.letter(x, y, k)
ZRT = {"A": [Prent.rond(175, 380, 28), Prent.rond(*LRT["A"], 22)],
       "B": [Prent.rond(240, 265, 28), Prent.rond(*LRT["B"], 22)],
       "C": [Prent.rond(360, 200, 30), Prent.rond(*LRT["C"], 22)],
       "D": [Prent.rond(500, 190, 30), Prent.rond(*LRT["D"], 22)],
       "E": [Prent.rond(870, 330, 34), Prent.rond(*LRT["E"], 22)]}

# Blastocyst -------------------------------------------------------------
BC = Prent("blastocyst", "Doorsnede van een blastocyst", "holle bol met een buitenste laag cellen P, een klompje cellen binnenin Q en een holte R")
for i in range(28):
    import math
    h = i / 28 * 2 * math.pi
    BC.cirkel(500 + 200 * math.cos(h), 330 + 200 * math.sin(h), 24, "#f5d9a8", DONKER, 1.5)
for dx, dy in ((-40, -140), (0, -150), (40, -140), (-20, -110), (20, -110), (-55, -110), (55, -110), (0, -80)):
    BC.cirkel(500 + dx, 330 + dy, 22, "#c8a8e0", DONKER, 1.5)
LBC = {"P": (760, 330), "Q": (500, 70), "R": (520, 400)}
BC.lijn(735, 330, 712, 330, DONKER, 1)
BC.lijn(500, 92, 500, 160, DONKER, 1)
for k, (x, y) in LBC.items():
    BC.letter(x, y, k)
ZBC = {"P": [Prent.rond(700, 330, 30), Prent.rond(300, 330, 30), Prent.rond(500, 530, 30), Prent.rond(*LBC["P"], 22)],
       "Q": [Prent.zone(430, 160, 140, 110), Prent.rond(*LBC["Q"], 22)],
       "R": [Prent.zone(380, 300, 240, 160), Prent.rond(*LBC["R"], 22)]}

VRAGEN = [
    klik(
        "Klik op de plek waar de bevruchting gebeurt.",
        RT.bestand, ZRT["B"],
        "In het eerste derde van de eileider.",
    ),
    klik(
        "Klik op de innesteling.",
        RT.bestand, ZRT["E"],
        "Rond dag zes nestelt de blastocyst zich in het baarmoederslijmvlies.",
    ),
    met_prent(RT.bestand, tabel(
        "Kijk naar de weg van de eicel. Klopt dit?",
        [
            ("A is de eicel net na de ovulatie.", J),
            ("Bij D is het een bolletje van enkele cellen.", J),
            ("Tussen B en D groeit het geheel sterk in grootte.", F),
            ("De reis van B naar E duurt enkele dagen.", J),
        ],
        "Bij de klievingsdelingen wordt het geheel niet groter.",
    )),
    klik(
        "Klik op het deel van de blastocyst dat later het embryo wordt.",
        BC.bestand, ZBC["Q"],
        "De embryoblast of kiemknop.",
    ),
    met_prent(BC.bestand, tabel(
        "Kijk naar de blastocyst. Klopt dit?",
        [
            ("P dringt met enzymen in het baarmoederslijmvlies.", J),
            ("P levert later een deel van de placenta.", J),
            ("R is gevuld met vocht.", J),
            ("R wordt het hart van het embryo.", F),
        ],
        "P is de trofoblast.",
    )),
    volgorde(
        "Zet de stadia na de bevruchting in volgorde.",
        ["Zygote", "Klievingsdelingen", "Morula", "Blastocyst", "Innesteling"],
        "Morula betekent moerbei.",
    ),
    volgorde(
        "Zet de fasen van de geboorte in volgorde.",
        ["Indaling", "Ontsluiting", "Uitdrijving", "Nageboorte"],
        "Bij de nageboorte komt de placenta eruit.",
    ),
    tabel(
        "Uit welk kiemblad ontstaat dit?",
        [
            ("zenuwstelsel", "ectoderm"),
            ("huid", "ectoderm"),
            ("skelet", "mesoderm"),
            ("bloedvaten", "mesoderm"),
            ("bekleding van de darm", "endoderm"),
        ],
        "Ecto is buiten, meso is midden, endo is binnen.",
        kolommen=["ectoderm", "mesoderm", "endoderm"],
    ),
    koppel(
        "Koppel elke stap aan wat er gebeurt.",
        [
            ("acrosoomreactie", "enzymen van de zaadcel komen vrij"),
            ("corticale reactie", "de eicel sluit zich af voor andere zaadcellen"),
            ("amfimixie", "de twee kernen smelten samen"),
            ("gastrulatie", "er ontstaan drie kiembladen"),
        ],
        ["de placenta komt los"],
        "Dat laatste is de nageboorte.",
    ),
    tabel(
        "Klopt dit over de placenta?",
        [
            ("Ze geeft zuurstof en voedingsstoffen door.", J),
            ("Ze voert afvalstoffen van het kind af.", J),
            ("Ze maakt hormonen.", J),
            ("Het bloed van moeder en kind mengt er rechtstreeks.", F),
        ],
        "Ze stromen langs elkaar, gescheiden door een dunne wand.",
    ),
    casus(
        "Een vrouw van 30 jaar wil zwanger worden. Haar huisarts geeft haar advies.",
        [
            keuze(
                "Ze neemt best [[*foliumzuur|vitamine C|ijzer]] al voor de zwangerschap.",
                "Het verkleint de kans op een open rug.",
            ),
            tabel(
                "Is dit een goed advies?",
                [
                    ("geen alcohol drinken", J),
                    ("niet roken", J),
                    ("geen rauw vlees eten", J),
                    ("helemaal niet meer bewegen", F),
                ],
                "Matig bewegen is juist goed.",
            ),
            keuze(
                "Rauw vlees vermijden beschermt tegen [[*toxoplasmose|rode hond|mazelen]].",
                "Een parasiet die ook in kattenuitwerpselen zit.",
            ),
        ],
    ),
    mk(
        "Waarom zijn de eerste acht weken het gevoeligst?",
        [
            "Dan worden alle organen aangelegd",
            "Dan groeit het kind het snelst in gewicht",
            "Dan is de placenta het grootst",
            "Dan bewegen de armen en benen voor het eerst",
        ],
        0,
        "Een stoornis tijdens de organogenese laat blijvende sporen.",
    ),
    tabel(
        "Embryo of foetus?",
        [
            ("week 5", "Embryo"),
            ("week 7", "Embryo"),
            ("week 12", "Foetus"),
            ("week 30", "Foetus"),
        ],
        "Vanaf ongeveer de negende week heet het een foetus.",
        kolommen=["Embryo", "Foetus"],
    ),
    tabel(
        "Invasief of niet invasief?",
        [
            ("echografie", "Niet invasief"),
            ("vruchtwaterpunctie", "Invasief"),
            ("vlokkentest", "Invasief"),
            ("NIPT in het bloed van de moeder", "Niet invasief"),
        ],
        "Invasieve tests halen cellen weg en hebben een klein risico.",
        kolommen=["Invasief", "Niet invasief"],
    ),
    sleep(
        "In de navelstreng brengen twee [[slagaders]] zuurstofarm bloed naar de placenta. Eén [[ader]] brengt zuurstofrijk bloed terug naar het [[kind]].",
        ["haarvaten", "lymfevat", "moeder"],
        "Net omgekeerd dan je zou verwachten bij slagaders.",
    ),
    mk(
        "Waarom raakt een eicel maar door één zaadcel bevrucht?",
        [
            "De corticale reactie sluit haar af",
            "De andere zaadcellen sterven in de vagina",
            "Er komt altijd maar één zaadcel tot in de eileider",
            "De eicel heeft maar één gaatje in haar wand",
        ],
        0,
        "De zona pellucida verhardt.",
    ),
    tabel(
        "Welke barrière moet een zaadcel overwinnen?",
        [
            ("het zure milieu van de vagina", J),
            ("de slijmprop in de baarmoederhals", J),
            ("de lagen rond de eicel", J),
            ("de placenta", F),
        ],
        "De placenta ontstaat pas na de innesteling.",
    ),
    keuze(
        "Een stof die een afwijking bij een embryo kan veroorzaken, heet [[*teratogeen|mutageen|hormonaal]].",
        "Alcohol is een bekend voorbeeld.",
    ),
    tabel(
        "Klopt dit over roken tijdens de zwangerschap?",
        [
            ("Koolstofmonoxide bezet hemoglobine.", J),
            ("Nicotine vernauwt de bloedvaten.", J),
            ("Het kind krijgt minder zuurstof.", J),
            ("Het kind wordt er zwaarder door.", F),
        ],
        "Het geboortegewicht ligt gemiddeld lager.",
    ),
    inv(
        "Een eicel leeft na de ovulatie ongeveer 24 uur, een zaadcel ongeveer 3 dagen. Hoeveel uur is dat voor de zaadcel?",
        ["72"],
        "3 x 24 = 72 uur.",
    ),
    tabel(
        "Klopt dit over het vruchtwater?",
        [
            ("Het zit in de amnionholte.", J),
            ("Het vangt schokken op.", J),
            ("Het loopt weg als de vruchtvliezen breken.", J),
            ("Het is bloed van de moeder.", F),
        ],
        "Het wordt omsloten door het amnionvlies.",
    ),
    mk(
        "Een prenatale test is normaal. Waarom kan de arts toch niet beloven dat het kind volledig gezond is?",
        [
            "Een test vindt niet elke aandoening",
            "Het kan enkel na de geboorte gebeuren",
            "Het verandert het DNA van het kind",
            "Het werkt alleen bij tweelingen",
        ],
        0,
        "Een test zoekt naar bepaalde afwijkingen, niet naar alles.",
    ),
    keuze(
        "Tijdens de ontsluiting gaat de [[*baarmoederhals|eileider|placenta]] tot ongeveer tien centimeter open.",
        "Door de weeën.",
    ),
    tabel(
        "Klopt dit over de klievingsdelingen?",
        [
            ("De cellen delen zonder te groeien.", J),
            ("Het geheel wordt niet groter.", J),
            ("De cellen worden telkens kleiner.", J),
            ("Ze gebeuren pas na de innesteling.", F),
        ],
        "Ze gebeuren onderweg in de eileider.",
    ),
    tabel(
        "Klopt dit over het hart van het embryo?",
        [
            ("Het begint rond de vierde week te kloppen.", J),
            ("Dat is vaak nog voor de moeder weet dat ze zwanger is.", J),
            ("Het klopt pas vanaf de derde maand.", F),
        ],
        "Het is een van de eerste organen die werken.",
    ),
    keuze(
        "Meisjes worden gevaccineerd tegen [[*rubella|toxoplasmose|hiv]] om een latere zwangerschap te beschermen.",
        "Rode hond kan ernstige afwijkingen geven bij een embryo.",
    ),
    inv(
        "Na 5 klievingsdelingen, hoeveel cellen heeft het embryo dan, als alle cellen telkens delen?",
        ["32"],
        "2 tot de vijfde = 32.",
    ),
    open_(
        "Leg uit waarom de cellen bij de klievingsdelingen steeds kleiner worden.",
        "Bij de klievingsdelingen delen de cellen zich snel na elkaar zonder tussendoor te groeien. Het totale volume blijft dat van de zygote, dus wordt elke nieuwe cel kleiner. Pas na de innesteling krijgt het embryo voedsel om te groeien.",
    ),
]
