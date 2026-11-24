"""Spieren, klieren en hormonen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Twee sarcomeren --------------------------------------------------------
SAR = Prent("sarcomeren", "Twee keer hetzelfde stukje spierfibril", "sarcomeer ontspannen (A) en samengetrokken (B) met Z-platen, actine en myosine")
def _sarcomeer(z1, z2, y0):
    for y in (y0 + 55, y0 + 105):
        SAR.lijn(z1, y, 490 if z1 > 200 else 420, y, ORANJE, 4)
        SAR.lijn(z2, y, 510 if z1 > 200 else 580, y, ORANJE, 4)
    for y in (y0 + 30, y0 + 80, y0 + 130):
        SAR.rect(330, y - 8, 340, 16, PAARS, DONKER, 6, 1)
    SAR.rect(z1 - 6, y0, 12, 160, DONKER, DONKER)
    SAR.rect(z2 - 6, y0, 12, 160, DONKER, DONKER)
_sarcomeer(150, 850, 110)
_sarcomeer(250, 750, 380)
SAR.letter(70, 190, "A")
SAR.letter(70, 460, "B")
Z_ZPLAAT = [Prent.zone(136, 100, 28, 180), Prent.zone(836, 100, 28, 180)]
Z_DONKER = Prent.zone(328, 125, 344, 130)
Z_LICHT = [Prent.zone(166, 125, 160, 130), Prent.zone(674, 125, 160, 130)]
Z_SAMEN = Prent.zone(40, 360, 760, 200)

# Glucose in het bloed over een dag --------------------------------------
def X(u):
    return 110 + (u - 6) * 52
def Y(g):
    return 560 - (g - 40) * 3.4
GLU = Prent("glucose-dag", "Glucosegehalte in het bloed van Mila op één dag", "grafiek van het glucosegehalte met drie maaltijden en een sporttraining")
GLU.rect(X(6), Y(110), X(22) - X(6), Y(70) - Y(110), "#eef4f8", "none", 0, 0)
GLU.tekst(X(6) + 10, Y(110) - 8, "normaal gebied", 16, "start", "#666666")
for g in (70, 110, 150):
    GLU.lijn(X(6) - 8, Y(g), X(6), Y(g), DONKER, 2)
    GLU.tekst(X(6) - 12, Y(g) + 6, str(g), 16, "end")
GLU.lijn(X(6), 560, X(22) + 10, 560, DONKER, 2)
GLU.lijn(X(6), 560, X(6), 80, DONKER, 2)
for u in range(6, 23, 2):
    GLU.lijn(X(u), 560, X(u), 568, DONKER, 2)
    GLU.tekst(X(u), 590, f"{u}u", 16)
GLU.tekst(X(6) - 8, 70, "glucose (mg/dl)", 16, "start")
pts = [(6, 85), (7.5, 88), (8.5, 150), (10, 95), (12, 88), (13, 140), (14.5, 92), (16, 85), (17, 58), (18, 72), (19, 90), (20, 145), (21.5, 98), (22, 92)]
GLU.pad("M" + " L ".join(f"{X(u):.1f} {Y(g):.1f}" for u, g in pts), "none", BLAUW, 4)
for u, t in [(8, "ontbijt"), (12.5, "middagmaal"), (19.5, "avondmaal")]:
    GLU.tekst(X(u), 110, t, 16, kleur="#666666")
GLU.tekst(X(16.5), 110, "sport", 16, kleur="#666666")
Z_PIEKEN = [Prent.zone(X(u) - 30, Y(g) - 25, 60, 60) for u, g in [(8.5, 150), (13, 140), (20, 145)]]
Z_DAL = Prent.zone(X(17) - 40, Y(70), 80, Y(50) - Y(70))

VRAGEN = [
    klik(
        "Klik op het sarcomeer dat samengetrokken is.",
        SAR.bestand, [Z_SAMEN],
        "Bij samentrekken schuiven de actinefilamenten tussen de myosinefilamenten en komen de Z-platen dichterbij.",
    ),
    klik(
        "Klik in sarcomeer A op een Z-plaat.",
        SAR.bestand, Z_ZPLAAT,
        "Een sarcomeer is het stukje spierfibril tussen twee Z-platen.",
    ),
    klik(
        "Klik in sarcomeer A op de donkere band.",
        SAR.bestand, [Z_DONKER],
        "De dikke myosinefilamenten laten minder licht door en vormen de donkere band.",
    ),
    klik(
        "Klik in sarcomeer A op een plek waar alleen actine ligt.",
        SAR.bestand, Z_LICHT,
        "Waar alleen de dunne actinefilamenten liggen, is de band licht.",
    ),
    met_prent(SAR.bestand, tabel(
        "Vergelijk A en B. Klopt dit?",
        [
            ("In B zijn de myosinefilamenten korter dan in A.", F),
            ("In B liggen de Z-platen dichter bij elkaar.", J),
            ("In B overlappen actine en myosine meer.", J),
            ("In B zijn de actinefilamenten langer geworden.", F),
        ],
        "De filamenten zelf blijven even lang. Ze schuiven langs elkaar.",
    )),
    klik(
        "Klik op een moment waarop de bètacellen van Mila veel insuline afgeven.",
        GLU.bestand, Z_PIEKEN,
        "Na een maaltijd stijgt het glucosegehalte. Dan geven de bètacellen insuline af.",
    ),
    klik(
        "Klik op het moment waarop de alfacellen van Mila glucagon nodig hebben.",
        GLU.bestand, [Z_DAL],
        "Na het sporten zakt het gehalte onder het normale gebied. Glucagon laat de lever glycogeen afbreken.",
    ),
    met_prent(GLU.bestand, tabel(
        "Kijk naar de grafiek van Mila. Klopt dit?",
        [
            ("Na elke maaltijd keert het gehalte terug naar het normale gebied.", J),
            ("Het sporten verbruikt glucose.", J),
            ("De grafiek toont een feedbacksysteem aan het werk.", J),
            ("Mila maakt geen insuline aan.", F),
        ],
        "Bij diabetes type 1 zou het gehalte na een maaltijd hoog blijven.",
    )),
    tabel(
        "Welk spierweefsel is dit?",
        [
            ("de spier die je arm buigt", "Dwarsgestreept"),
            ("de spieren in de wand van je darm", "Glad"),
            ("de wand van je hart", "Hartspier"),
            ("de spieren in een bloedvatwand", "Glad"),
            ("je kauwspier", "Dwarsgestreept"),
        ],
        "Dwarsgestreepte spieren bewegen het skelet, gladde spieren zitten in organen en bloedvaten.",
        kolommen=["Dwarsgestreept", "Glad", "Hartspier"],
    ),
    casus(
        "Zoë buigt haar arm om een zware boekentas op te tillen. Daarna strekt ze haar arm weer.",
        [
            mk(
                "Welke spier is de agonist als Zoë haar arm buigt?",
                ["De biceps", "De triceps", "De kuitspier", "De hartspier"],
                0,
                "De biceps trekt samen en buigt de arm. De triceps ontspant.",
            ),
            tabel(
                "Klopt dit over de armspieren van Zoë?",
                [
                    ("Bij het strekken trekt de triceps samen.", J),
                    ("De biceps duwt de arm terug open.", F),
                    ("Biceps en triceps zijn elkaars antagonist.", J),
                    ("Beide spieren werken onder haar wil.", J),
                ],
                "Een spier kan alleen trekken. Voor de omgekeerde beweging is de antagonist nodig.",
            ),
            keuze(
                "Voor deze inspanning breekt de spier [[*glycogeen|thyroxine|myosine]] af tot glucose.",
                "Een spier slaat glycogeen op als voorraad.",
            ),
        ],
    ),
    volgorde(
        "Zet de bouw van een spier van groot naar klein.",
        ["Spierbuik", "Spierbundel", "Spiervezel", "Spierfibril", "Sarcomeer"],
        "Elke bundel bestaat uit vezels, in elke vezel liggen fibrillen, en een fibril is een rij sarcomeren.",
    ),
    volgorde(
        "Zet de stappen van het bevel tot samentrekken in de juiste volgorde.",
        [
            "Een impuls loopt over het motorische neuron",
            "Aan de motorische eindplaat komt neurotransmitter vrij",
            "Het sarcolemma depolariseert",
            "De filamenten schuiven langs elkaar",
        ],
        "De motorische eindplaat is een synaps tussen zenuw en spier.",
    ),
    mk(
        "Waarom zijn de motorische eenheden in de oogspieren heel klein?",
        [
            "Oogbewegingen moeten heel fijn zijn",
            "Oogspieren hebben geen motorische eindplaat",
            "In het oog liggen geen motorische neuronen",
            "Oogspieren werken met hormonen in plaats van zenuwen",
        ],
        0,
        "Hoe fijner de beweging, hoe minder vezels één neuron bedient.",
    ),
    sorteer(
        "Endocrien, exocrien of gemengd?",
        ["Endocrien", "Exocrien", "Gemengd"],
        [
            ["de schildklier", "Endocrien"],
            ["de thymus", "Endocrien"],
            ["de zweetklier", "Exocrien"],
            ["de traanklier", "Exocrien"],
            ["de alvleesklier", "Gemengd"],
        ],
        "De alvleesklier maakt enzymen via een buisje en hormonen rechtstreeks voor het bloed.",
    ),
    koppel(
        "Koppel elk hormoon aan de klier die het maakt.",
        [
            ("thyroxine", "schildklier"),
            ("insuline", "alvleesklier"),
            ("adrenaline", "bijnier"),
            ("prolactine", "hypofyse"),
        ],
        ["traanklier"],
        "De traanklier is exocrien en maakt geen hormoon.",
    ),
    casus(
        "Lars heeft diabetes type 1. Voor zijn diagnose had hij voortdurend dorst en moest hij heel vaak plassen.",
        [
            mk(
                "Wat loopt er mis in het lichaam van Lars?",
                [
                    "Zijn bètacellen maken geen insuline meer",
                    "Zijn alfacellen maken te veel insuline aan",
                    "Zijn lever slaat te veel glycogeen op",
                    "Zijn schildklier maakt geen thyroxine meer",
                ],
                0,
                "Bij type 1 vallen de bètacellen uit.",
            ),
            tabel(
                "Klopt dit over Lars voor zijn behandeling?",
                [
                    ("Zijn glucosegehalte bleef te hoog.", J),
                    ("Er kwam glucose in zijn urine.", J),
                    ("De glucose trok water mee naar de urine.", J),
                    ("Zijn cellen namen extra veel glucose op.", F),
                ],
                "Zonder insuline kunnen de cellen de glucose niet opnemen.",
            ),
        ],
    ),
    sleep(
        "Stijgt het glucosegehalte, dan geven de [[bètacellen]] insuline af en slaat de lever glucose op als [[glycogeen]]. Daalt het, dan komt er [[glucagon]] uit de alfacellen.",
        ["thyroxine", "adrenaline"],
        "Twee hormonen houden het gehalte in evenwicht: een feedbacksysteem.",
    ),
    tabel(
        "Zenuw of hormoon: wat past bij de beschrijving?",
        [
            ("Het signaal reist met het bloed.", "Hormoon"),
            ("Het signaal is er in een fractie van een seconde.", "Zenuw"),
            ("Het effect kan uren duren.", "Hormoon"),
            ("Het signaal loopt over een axon.", "Zenuw"),
        ],
        "Hormonen zijn trager dan zenuwen, maar hun effect kan lang aanhouden.",
        kolommen=["Zenuw", "Hormoon"],
    ),
    mk(
        "Een hormoon komt overal in het lichaam. Waarom reageren maar enkele cellen?",
        [
            "Alleen doelwitcellen hebben de passende receptor",
            "Het hormoon raakt onderweg in het bloed helemaal op",
            "Alleen de cellen dicht bij de klier krijgen het hormoon",
            "Enkel spiercellen kunnen een hormoon echt opnemen",
        ],
        0,
        "Het sleutel-slotprincipe: alleen cellen met de passende receptor reageren.",
    ),
    tabel(
        "Gebeurt dit door adrenaline bij stress?",
        [
            ("de hartslag versnelt", J),
            ("er komt extra glucose vrij in het bloed", J),
            ("de spijsvertering krijgt voorrang", F),
            ("het lichaam wordt klaargezet voor inspanning", J),
            ("de bètacellen stoppen voorgoed", F),
        ],
        "Adrenaline uit de bijnier maakt het lichaam klaar om te vechten of te vluchten.",
    ),
    keuze(
        "Langdurige stress laat de bijnierschors [[*cortisol|insuline|thymosine]] afgeven.",
        "Cortisol laat onder meer het glucosegehalte stijgen.",
    ),
    tabel(
        "Klopt dit over spierweefsel?",
        [
            ("Een dwarsgestreepte spiervezel heeft veel kernen.", J),
            ("Het sarcolemma is het membraan rond een spiervezel.", J),
            ("Spierspoeltjes meten de rekking van een spier.", J),
            ("Glad spierweefsel trekt snel en kort samen.", F),
            ("Het hartspierweefsel kan je met je wil stilleggen.", F),
        ],
        "Glad spierweefsel trekt traag maar lang samen. Het hart werkt onwillekeurig.",
    ),
    mk(
        "Waarom heeft een spier een dicht net van bloedvaten nodig?",
        [
            "Ze verbruikt veel zuurstof en glucose",
            "Ze maakt zelf hormonen voor het bloed",
            "Ze moet haar Z-platen kunnen uitspoelen",
            "Ze stuurt haar impulsen via het bloed door",
        ],
        0,
        "Het bloed brengt zuurstof en voedingsstoffen en voert afval af.",
    ),
    keuze(
        "De kniepeesreflex begint bij de [[*spierspoeltjes|Z-platen|eilandjes van Langerhans]], die de rekking van de spier melden.",
        "Spierspoeltjes zijn receptoren in de spier zelf.",
    ),
    koppel(
        "Koppel elk hormoon van de hypofyse of de bijnier aan zijn werking.",
        [
            ("schildklierstimulerend hormoon", "zet de schildklier aan"),
            ("adrenaline", "maakt klaar om te vechten of te vluchten"),
            ("cortisol", "hormoon van de langdurige stress"),
        ],
        ["laat de pupil kleiner worden"],
        "De pupilreflex loopt via zenuwen, niet via deze hormonen.",
    ),
    tabel(
        "Klopt dit over de alvleesklier?",
        [
            ("Ze maakt spijsverteringsenzymen voor de darm.", J),
            ("Haar eilandjes van Langerhans maken hormonen.", J),
            ("Ze geeft al haar stoffen via een afvoerbuis af.", F),
        ],
        "Insuline en glucagon gaan rechtstreeks in het bloed.",
    ),
    open_(
        "Leg uit waarom een klier net als een spier een effector is, en wat het verschil is tussen hun antwoord.",
        "Een effector staat aan het einde van de weg van prikkel naar reactie en voert het antwoord uit nadat hij een signaal kreeg. Een spier antwoordt met een beweging, een klier met een stof, zoals een hormoon of zweet.",
    ),
]
