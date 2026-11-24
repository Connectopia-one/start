"""Enzymen, transport door membranen en osmose — pittig (🧬 Beyond doorstroom, biologie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# pH-optimum -------------------------------------------------------------
PH = Prent("enzym-ph-optimum", "Activiteit van twee enzymen bij verschillende pH", "twee klokvormige curves: enzym 1 met top bij pH 2, enzym 2 met top bij pH 8")
X, Y = assen(PH, 0, 12, 0, 100, "pH", "activiteit (%)", 1, 25, links=130, rechts=900)
for top, kl in ((2, ORANJE), (8, BLAUW)):
    pts = []
    for i in range(0, 121):
        ph = i / 10
        a = 100 * math.exp(-((ph - top) / 1.3) ** 2)
        pts.append(f"{X(ph):.1f} {Y(a):.1f}")
    PH.pad("M" + " L ".join(pts), "none", kl, 4)
PH.tekst(X(2), Y(100) - 12, "enzym 1", 16, kleur=ORANJE, vet=True)
PH.tekst(X(8), Y(100) - 12, "enzym 2", 16, kleur=BLAUW, vet=True)
ZPH = {"top1": [Prent.rond(X(2), Y(100), 34)], "top2": [Prent.rond(X(8), Y(100), 34)]}

# Osmose ----------------------------------------------------------------
OS = Prent("osmose-bloedcellen", "Rode bloedcellen in drie oplossingen", "drie bekers K, L en M; in K een gekrompen cel, in L een normale cel, in M een opgezwollen cel")
for i, (x, k) in enumerate(((180, "K"), (500, "L"), (820, "M"))):
    OS.pad(f"M{x - 120} 160 L {x - 110} 520 L {x + 110} 520 L {x + 120} 160", "#e7f1fa", DONKER, 3)
    OS.letter(x, 570, k)
OS.pad("M150 330 q 15 -30 30 -10 q 20 -25 30 5 q 25 10 5 30 q 10 30 -25 20 q -20 25 -35 0 q -30 0 -15 -25 q -20 -15 10 -20 Z", "#d9534f", DONKER, 2)
OS.ellips(500, 340, 60, 40, "#d9534f", DONKER, 2)
OS.ellips(500, 340, 24, 14, "#e88a87", "none", 0)
OS.cirkel(820, 340, 70, "#e88a87", DONKER, 2)
for x in (180, 500, 820):
    for dx, dy in ((-60, -120), (40, -140), (-50, 120), (60, 110)):
        OS.cirkel(x + dx, 340 + dy, 4, "#5b8bc0", "none", 0)
ZOS = {k: [Prent.zone(x - 120, 160, 240, 360), Prent.rond(x, 570, 26)] for x, k in ((180, "K"), (500, "L"), (820, "M"))}

VRAGEN = [
    met_prent(PH.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("Enzym 1 kan pepsine uit de maag zijn.", J),
            ("Enzym 2 werkt goed in de dunne darm.", J),
            ("Bij pH 5 werken beide enzymen nauwelijks.", J),
            ("Enzym 1 werkt het best in een basisch milieu.", F),
        ],
        "Elk enzym heeft zijn eigen pH-optimum.",
    )),
    klik(
        "Klik op het pH-optimum van het enzym dat in een zuur milieu werkt.",
        PH.bestand, ZPH["top1"],
        "Enzym 1 heeft zijn top bij pH 2.",
    ),
    met_prent(PH.bestand, inv(
        "Kijk naar de grafiek. Bij welke pH werkt enzym 2 het snelst?",
        ["8"],
        "De top van de blauwe curve ligt bij pH 8.",
    )),
    klik(
        "Klik op de beker met een hypertone oplossing.",
        OS.bestand, ZOS["K"],
        "Water verlaat de cel: ze krimpt.",
    ),
    klik(
        "Klik op de beker waarin de cel kan barsten.",
        OS.bestand, ZOS["M"],
        "In een hypotone oplossing, zoals zuiver water, stroomt water de cel in.",
    ),
    met_prent(OS.bestand, tabel(
        "Kijk naar de drie bekers. Welke oplossing zit erin?",
        [
            ("isotoon", "L"),
            ("hypertoon", "K"),
            ("hypotoon", "M"),
        ],
        "Water gaat naar de kant met de hoogste concentratie opgeloste stoffen.",
        kolommen=["K", "L", "M"],
    )),
    tabel(
        "Passief of actief transport?",
        [
            ("diffusie van zuurstof", "Passief"),
            ("de natrium-kaliumpomp", "Actief"),
            ("water door een aquaporine", "Passief"),
            ("glucose via een carriereiwit met de gradiënt mee", "Passief"),
            ("een protonpomp", "Actief"),
        ],
        "Actief transport kost ATP en gaat tegen de gradiënt in.",
        kolommen=["Passief", "Actief"],
    ),
    tabel(
        "Endocytose of exocytose?",
        [
            ("een witte bloedcel eet een bacterie op", "Endocytose"),
            ("een cel scheidt insuline af", "Exocytose"),
            ("het membraan plooit naar binnen", "Endocytose"),
            ("een blaasje versmelt met het celmembraan", "Exocytose"),
        ],
        "Endo is naar binnen, exo naar buiten.",
        kolommen=["Endocytose", "Exocytose"],
    ),
    tabel(
        "Klopt dit over enzymen?",
        [
            ("Ze verlagen de activeringsenergie.", J),
            ("Ze komen onveranderd uit de reactie.", J),
            ("Ze bepalen in welke richting een reactie loopt.", F),
            ("Het zijn meestal eiwitten.", J),
        ],
        "Een enzym versnelt alleen.",
    ),
    casus(
        "In een proef leg je een stukje rauwe lever in waterstofperoxide. Het schuimt hevig. Een gekookt stukje lever schuimt niet.",
        [
            keuze(
                "Het enzym in de lever heet [[*catalase|lactase|amylase]].",
                "Het splitst waterstofperoxide in water en zuurstof.",
            ),
            keuze(
                "In het gekookte stukje is het enzym [[*gedenatureerd|verzadigd|vermenigvuldigd]].",
                "De ruimtelijke vorm is verloren.",
            ),
            tabel(
                "Klopt dit over de proef?",
                [
                    ("Het schuim is zuurstofgas.", J),
                    ("Het gekookte stukje is de controle voor de rol van het enzym.", J),
                    ("Koken versnelt elk enzym.", F),
                ],
                "Boven het optimum valt de activiteit sterk terug.",
            ),
        ],
    ),
    mk(
        "Waarom vlakt de reactiesnelheid af als je steeds meer substraat toevoegt, bij een vaste hoeveelheid enzym?",
        [
            "Elk actief centrum is al bezet",
            "Het substraat remt het enzym af als inhibitor",
            "Het enzym wordt bij elke reactie opgebruikt",
            "De temperatuur daalt door het extra substraat",
        ],
        0,
        "Dat heet verzadiging.",
    ),
    koppel(
        "Koppel elk begrip aan zijn uitleg.",
        [
            ("actief centrum", "de holte waarin het substraat past"),
            ("inhibitor", "stof die een enzym remt"),
            ("co-enzym", "kleine molecule die het enzym helpt"),
            ("denaturatie", "verlies van de ruimtelijke vorm"),
        ],
        ["stof die een enzym altijd sneller maakt bij elke temperatuur"],
        "Een co-enzym komt vaak uit een vitamine.",
    ),
    sleep(
        "Lactase splitst [[lactose]] in glucose en [[galactose]]. Het past op geen enkele andere stof: het is [[substraatspecifiek]].",
        ["zetmeel", "fructose", "onverzadigd"],
        "Sleutel en slot.",
    ),
    mk(
        "Je legt een blaadje sla en een druppel bloed in zuiver water. Waarom blijven de slacellen heel?",
        [
            "De celwand vangt de druk op",
            "Een plantencel laat geen water binnen",
            "Een plantencel heeft geen vacuole",
            "Zuiver water is voor planten isotoon",
        ],
        0,
        "De volle vacuole duwt tegen de wand: turgor.",
    ),
    tabel(
        "Klopt dit over de natrium-kaliumpomp?",
        [
            ("Ze verbruikt ATP.", J),
            ("Ze pompt drie natriumionen naar buiten.", J),
            ("Ze pompt twee kaliumionen naar binnen.", J),
            ("Ze volgt de concentratiegradiënt.", F),
        ],
        "Ze pompt net tegen de gradiënt in.",
    ),
    tabel(
        "Anabool of katabool?",
        [
            ("eiwitsynthese", "Anabool"),
            ("celademhaling", "Katabool"),
            ("fotosynthese", "Anabool"),
            ("spijsvertering", "Katabool"),
        ],
        "Opbouwen kost energie, afbreken levert energie.",
        kolommen=["Anabool", "Katabool"],
    ),
    keuze(
        "Een plantencel in een sterke zoutoplossing verliest water: het cytoplasma trekt los van de celwand. Dat heet [[*plasmolyse|turgor|fagocytose]].",
        "Het blad gaat slap hangen.",
    ),
    mk(
        "Hoe zie je op een energiediagram dat een enzym aanwezig is?",
        [
            "De top tussen begin en eind is lager",
            "Het eindniveau ligt veel lager dan zonder enzym",
            "Het beginniveau ligt hoger dan zonder enzym",
            "Er is helemaal geen top meer in de curve",
        ],
        0,
        "De activeringsenergie is kleiner, begin en eind blijven gelijk.",
    ),
    tabel(
        "Wat verhoogt de reactiesnelheid, als er genoeg substraat is?",
        [
            ("meer enzym toevoegen", J),
            ("de temperatuur naar het optimum brengen", J),
            ("een inhibitor toevoegen", F),
            ("de pH ver van het optimum zetten", F),
        ],
        "Remmers en een slechte pH vertragen.",
    ),
    tabel(
        "Klopt dit over osmose?",
        [
            ("Water gaat door een halfdoorlaatbaar membraan.", J),
            ("Water gaat naar de kant met meer opgeloste stoffen.", J),
            ("Ook de opgeloste stoffen gaan vrij door het membraan.", F),
        ],
        "Het membraan houdt de opgeloste stoffen tegen.",
    ),
    inv(
        "Eén molecule catalase splitst ongeveer 40 miljoen moleculen waterstofperoxide per seconde. Hoeveel miljoen is dat in een halve minuut?",
        ["1200", "1 200"],
        "40 miljoen x 30 = 1 200 miljoen.",
    ),
    tabel(
        "Klopt dit over een kanaaleiwit?",
        [
            ("Het vormt een doorgang door het membraan.", J),
            ("Het laat enkel bepaalde ionen door.", J),
            ("Het verbruikt ATP.", F),
        ],
        "Transport door een kanaal is passief.",
    ),
    mk(
        "Veel geneesmiddelen werken als inhibitor. Wat doen ze dan?",
        [
            "Ze remmen een bepaald enzym",
            "Ze maken extra enzym aan in de cel",
            "Ze verhogen de lichaamstemperatuur",
            "Ze breken het substraat zelf af",
        ],
        0,
        "Ze bezetten het actief centrum of veranderen de vorm van het enzym.",
    ),
    keuze(
        "Bij hoge temperatuur vouwt een enzym open: het [[*denatureert|verzadigt|kristalliseert]].",
        "Dat is meestal niet omkeerbaar.",
    ),
    tabel(
        "Klopt dit over diffusie?",
        [
            ("Deeltjes gaan van veel naar weinig.", J),
            ("Het kost de cel geen energie.", J),
            ("Het stopt als de concentratie overal gelijk is.", J),
            ("Het gaat altijd tegen de gradiënt in.", F),
        ],
        "Netto stopt het bij evenwicht; de deeltjes blijven wel bewegen.",
    ),
    tabel(
        "Waar werkt dit enzym het best?",
        [
            ("pepsine", "maag"),
            ("trypsine", "dunne darm"),
            ("speekselamylase", "mond"),
        ],
        "Elk enzym hoort bij zijn eigen milieu.",
        kolommen=["mond", "maag", "dunne darm"],
    ),
    tabel(
        "Klopt dit over ATP?",
        [
            ("Het levert de energie voor actief transport.", J),
            ("Bij de splitsing ontstaan ADP en fosfaat.", J),
            ("Het is een enzym.", F),
        ],
        "ATP is de energiedrager van de cel.",
    ),
    open_(
        "Leg uit waarom een enzym bij 70 °C nauwelijks nog werkt, terwijl het bij 37 °C snel werkt.",
        "Een enzym is een eiwit met een precieze ruimtelijke vorm. Bij 37 °C past het substraat in het actief centrum. Bij 70 °C vouwt het eiwit open, het denatureert. Het actief centrum verliest zijn vorm en het substraat past er niet meer in.",
    ),
]
