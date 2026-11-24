"""Gedrag, interactie en ecosystemen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Een voedselweb in een bosrand ------------------------------------------
WEB = Prent("voedselweb-bosrand", "Een voedselweb in een bosrand", "voedselweb met gras, eik, konijn, rups, vos, mees, havik en reducenten")
KNOOP = {"gras": (170, 540), "eik": (470, 540), "konijn": (170, 370), "rups": (470, 370),
         "vos": (170, 200), "mees": (470, 200), "havik": (320, 80), "bacteriën en schimmels": (800, 370)}
def _pijl(a, b, stippel=False):
    (x1, y1), (x2, y2) = KNOOP[a], KNOOP[b]
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    if stippel:
        WEB.lijn(x1 + ux * 60, y1 + uy * 30, x2 - ux * 120, y2 - uy * 34, "#999999", 2, True)
    else:
        WEB.pijl(x1 + ux * 40, y1 + uy * 30, x2 - ux * 40, y2 - uy * 30, DONKER, 3)
for a, b in [("gras", "konijn"), ("eik", "rups"), ("rups", "mees"), ("konijn", "vos"), ("konijn", "havik"), ("mees", "havik")]:
    _pijl(a, b)
for naam, (x, y) in KNOOP.items():
    b = 240 if naam.startswith("bact") else 130
    WEB.rect(x - b / 2, y - 26, b, 52, "#ffffff" if not naam.startswith("bact") else "#f1eadb", DONKER, 14)
    WEB.tekst(x, y + 7, naam, 19)
WEB.tekst(800, 420, "breken alle dode resten af", 16, kleur="#666666")
WEB.tekst(800, 490, "Een pijl wijst van wie gegeten wordt", 16, kleur="#666666")
WEB.tekst(800, 512, "naar wie eet.", 16, kleur="#666666")
def Z(naam):
    x, y = KNOOP[naam]
    b = 240 if naam.startswith("bact") else 130
    return Prent.zone(x - b / 2 - 6, y - 30, b + 12, 60)

# Prooi en roofdier -------------------------------------------------------
PR = Prent("prooi-roofdier", "Aantal sneeuwhazen en lynxen over de jaren", "twee golvende curven: prooi en roofdier met vertraging")
PR.lijn(100, 560, 930, 560, DONKER, 2)
PR.lijn(100, 560, 100, 80, DONKER, 2)
PR.tekst(925, 595, "tijd (jaren)", 16, "end")
PR.tekst(92, 70, "aantal dieren", 16, "start")
def haas(x):
    return 330 - 170 * math.sin((x - 100) / 830 * 2 * math.pi * 2)
def lynx(x):
    return 430 - 90 * math.sin((x - 100) / 830 * 2 * math.pi * 2 - 1.2)
PR.pad("M" + " L ".join(f"{x} {haas(x):.1f}" for x in range(100, 931, 10)), "none", BLAUW, 4)
PR.pad("M" + " L ".join(f"{x} {lynx(x):.1f}" for x in range(100, 931, 10)), "none", ORANJE, 4)
PR.lijn(640, 110, 680, 110, BLAUW, 5); PR.tekst(690, 116, "sneeuwhazen (prooi)", 16, "start")
PR.lijn(640, 140, 680, 140, ORANJE, 5); PR.tekst(690, 146, "lynxen (roofdier)", 16, "start")
# toppen: haas bij fase pi/2 -> x = 100 + 830/8 + k*830/2 ; lynx later
_haas_top = [100 + 830 / 8 + k * 415 for k in range(2)]
_lynx_top = [x + 1.2 / (2 * math.pi * 2) * 830 for x in _haas_top]
Z_LYNXTOP = [Prent.zone(x - 40, lynx(x) - 30, 80, 60) for x in _lynx_top]
Z_HAASTOP = [Prent.zone(x - 40, haas(x) - 30, 80, 60) for x in _haas_top]

VRAGEN = [
    klik(
        "Klik op een producent in dit voedselweb.",
        WEB.bestand, [Z("gras"), Z("eik")],
        "Producenten maken met fotosynthese energierijke stoffen uit energiearme.",
    ),
    klik(
        "Klik op het organisme dat rechtstreeks al zijn voedsel kwijt is als alle eiken sterven.",
        WEB.bestand, [Z("rups")],
        "De rups eet enkel van de eik. De mees verliest pas daarna haar voedsel.",
    ),
    klik(
        "Klik op de groep die de materiekringloop rondmaakt.",
        WEB.bestand, [Z("bacteriën en schimmels")],
        "Reducenten zetten dode resten weer om in minerale stoffen.",
    ),
    klik(
        "Klik op een consument van de eerste orde.",
        WEB.bestand, [Z("konijn"), Z("rups")],
        "Consumenten van de eerste orde zijn planteneters.",
    ),
    klik(
        "Klik op de prooi die door twee verschillende roofdieren gegeten wordt.",
        WEB.bestand, [Z("konijn")],
        "Het konijn wordt gegeten door de vos en door de havik. Zo'n vertakking toont een voedselweb.",
    ),
    met_prent(WEB.bestand, tabel(
        "Kijk naar het voedselweb. Klopt dit?",
        [
            ("De mees is een consument van de tweede orde.", J),
            ("De havik eet van twee verschillende soorten.", J),
            ("Het konijn is een producent.", F),
            ("Vos en havik zijn concurrenten voor het konijn.", J),
            ("De pijlen tonen hoe de energie van de havik naar het gras gaat.", F),
        ],
        "De pijlen wijzen in de richting van de energiestroom: van wie gegeten wordt naar wie eet.",
    )),
    klik(
        "Klik op een top van het aantal roofdieren.",
        PR.bestand, Z_LYNXTOP,
        "De lynxen bereiken hun top telkens na de sneeuwhazen.",
    ),
    klik(
        "Klik op een moment waarop er het meeste prooi is.",
        PR.bestand, Z_HAASTOP,
        "Veel prooi laat daarna de roofdieren toenemen.",
    ),
    met_prent(PR.bestand, mk(
        "Waarom piekt het aantal lynxen telkens na het aantal sneeuwhazen?",
        [
            "Veel prooi laat de roofdieren later toenemen",
            "Lynxen eten pas als er weinig hazen zijn",
            "Sneeuwhazen eten op hun beurt de jonge lynxen",
            "Beide aantallen hangen helemaal niet samen",
        ],
        0,
        "Veel roofdieren laten de prooi weer afnemen, en dan dalen ook de roofdieren: een terugkoppeling.",
    )),
    tabel(
        "Aangeboren of aangeleerd gedrag?",
        [
            ("een spin die haar eerste web bouwt", "Aangeboren"),
            ("een hond die kwijlt bij het geluid van de voerbak", "Aangeleerd"),
            ("vogels die na een tijd blijven zitten bij een vogelverschrikker", "Aangeleerd"),
            ("een jonge aap die een andere aap nabootst", "Aangeleerd"),
        ],
        "Conditioneren, gewenning en nabootsen zijn vormen van leren.",
        kolommen=["Aangeboren", "Aangeleerd"],
    ),
    koppel(
        "Koppel elk voorbeeld aan de vorm van leren.",
        [
            ("Een hond kwijlt bij het geluid van de voerbak.", "conditioneren"),
            ("Vogels negeren na een tijd de vogelverschrikker.", "gewenning"),
            ("Jonge ganzen volgen wat ze eerst zien bewegen.", "inprenting"),
            ("Een rat vindt na veel pogingen de uitgang.", "trial-and-error"),
        ],
        ["balts"],
        "Balts is gedrag bij de voortplanting, geen vorm van leren.",
    ),
    tabel(
        "Welke interactie is dit?",
        [
            ("Een bij haalt nectar en bestuift de bloem.", "Mutualisme"),
            ("Een lintworm leeft in de darm van een mens.", "Parasitisme"),
            ("Een vos vangt en eet een konijn.", "Predatie"),
            ("Twee vogelsoorten eten hetzelfde zaad.", "Concurrentie"),
            ("Een schimmel maakt een stof die bacteriën doodt.", "Antibiose"),
        ],
        "Bij parasitisme heeft één voordeel en de ander schade, bij predatie wordt de ander gedood.",
        kolommen=["Mutualisme", "Parasitisme", "Predatie", "Concurrentie", "Antibiose"],
    ),
    sorteer(
        "Is dit een vorm van visuele, chemische of auditieve communicatie?",
        ["Visueel", "Chemisch", "Auditief"],
        [
            ["de dans van een honingbij", "Visueel"],
            ["een pauw die zijn staart opzet", "Visueel"],
            ["een geurspoor van mieren", "Chemisch"],
            ["een kat die met geur haar gebied afbakent", "Chemisch"],
            ["een merel die zingt", "Auditief"],
        ],
        "Wat je moet zien om te begrijpen, is visueel. Een geurstof is een chemisch signaal.",
    ),
    tabel(
        "Biotische of abiotische factor?",
        [
            ("de zuurtegraad van de bodem", "Abiotisch"),
            ("begrazing door schapen", "Biotisch"),
            ("de hoeveelheid neerslag", "Abiotisch"),
            ("betreding door wandelaars", "Biotisch"),
            ("de temperatuur", "Abiotisch"),
        ],
        "Betreding, begrazing en bemesting gaan uit van levende wezens.",
        kolommen=["Biotisch", "Abiotisch"],
    ),
    casus(
        "In een vijver van een park voeren veel bezoekers brood aan de eenden. Er komt jaren na elkaar veel organisch afval en eendenmest in het water.",
        [
            volgorde(
                "Zet de gevolgen in de vijver in de juiste volgorde.",
                [
                    "Het water raakt overbemest",
                    "Algen vermeerderen zich sterk",
                    "Er dringt minder licht door in de diepte",
                    "Afgestorven algen worden afgebroken",
                    "Het zuurstofgehalte daalt en vissen sterven",
                ],
                "Eutrofiëring: de afbraak verbruikt zo veel zuurstof dat vissen stikken.",
            ),
            mk(
                "Welke groep organismen verbruikt de zuurstof bij die afbraak?",
                ["Reducenten zoals bacteriën", "De producenten aan het wateroppervlak", "De eenden op de vijver", "De vissen diep in het water"],
                0,
                "Bacteriën breken de afgestorven algen af en verbruiken daarbij zuurstof.",
            ),
        ],
    ),
    tabel(
        "Draait dit rond in een kringloop, of stroomt het in één richting?",
        [
            ("koolstof", "Kringloop"),
            ("stikstof", "Kringloop"),
            ("water", "Kringloop"),
            ("energie", "Eén richting"),
        ],
        "Materie draait rond, energie komt binnen als licht en verlaat het systeem als warmte.",
        kolommen=["Kringloop", "Eén richting"],
    ),
    sleep(
        "Bij de [[fotosynthese]] legt een plant koolstof vast in glucose. Bij de [[celademhaling]] wordt glucose weer afgebroken tot koolstofdioxide en water. [[Reducenten]] geven de koolstof uit dode resten terug.",
        ["eutrofiëring", "consumenten", "inprenting"],
        "Zo sluit de koolstofkringloop.",
    ),
    mk(
        "Waarom kunnen er in een ecosysteem maar weinig toproofdieren leven?",
        [
            "Bij elke stap gaat het meeste energie verloren",
            "Toproofdieren hebben helemaal geen reducenten nodig",
            "Planteneters eten de jonge toproofdieren op",
            "Toproofdieren maken zelf geen glucose aan, planten wel",
        ],
        0,
        "Van de energie in een schakel komt maar een klein deel in de volgende.",
    ),
    tabel(
        "Klopt dit over de stikstofkringloop?",
        [
            ("Planten kunnen stikstofgas uit de lucht niet zelf gebruiken.", J),
            ("Bacteriën in wortelknolletjes zetten stikstof om.", J),
            ("Planten nemen nitraten op met hun wortels.", J),
            ("Stikstof stroomt in één richting en gaat als warmte verloren.", F),
        ],
        "Stikstof is materie en draait rond.",
    ),
    mk(
        "Een akker heeft één soort graan, een bloemrijke weide heeft er tientallen. Een plaag treft één plantensoort. Welk ecosysteem vangt dat het best op?",
        [
            "De weide, want andere soorten nemen de rol over",
            "De akker, want daar is alles even sterk tegen ziekte",
            "Beide even goed, want soorten spelen geen rol",
            "Geen van beide, want een plaag treft alle soorten",
        ],
        0,
        "Hoe meer soorten, hoe beter een ecosysteem een verstoring opvangt.",
    ),
    tabel(
        "Klopt dit over gedrag in een groep?",
        [
            ("Taakverdeling maakt een mierenkolonie sterker.", J),
            ("Imponeergedrag eindigt meestal in een echt gevecht.", F),
            ("Territoriumgedrag verzekert een dier van voedsel en een nestplaats.", J),
            ("Balts toont een partner dat het dier bij de juiste soort hoort.", J),
            ("Een kat die haar haren opzet, communiceert chemisch.", F),
        ],
        "Imponeren lost een conflict op zonder verwondingen. Haren opzetten is visueel.",
    ),
    keuze(
        "Een vis die een haai schoonmaakt en daar voedsel bij vindt, terwijl de haai er niets van merkt, is een voorbeeld van [[*commensalisme|parasitisme|predatie]].",
        "Bij commensalisme heeft er maar één voordeel. De ander merkt er niets van.",
    ),
    klik(
        "Klik op het toproofdier van dit voedselweb.",
        WEB.bestand, [Z("havik")],
        "De havik wordt door geen enkel ander dier in dit web gegeten.",
    ),
    mk(
        "Gras en eik staan onderaan het voedselweb. Wat doen ze voor het hele ecosysteem?",
        [
            "Ze leggen lichtenergie vast in glucose",
            "Ze breken dode resten af tot mineralen",
            "Ze eten andere dieren en houden ze in toom",
            "Ze zetten stikstofgas om tot nitraten",
        ],
        0,
        "Alle andere schakels leven van wat de producenten maken.",
    ),
    tabel(
        "Klopt dit over de piramide van biomassa?",
        [
            ("Elke hogere schakel bevat minder materie.", J),
            ("Bij elke stap gaat energie verloren als warmte.", J),
            ("De top van de piramide is het breedst.", F),
        ],
        "Daarom kan de top maar klein zijn.",
    ),
    keuze(
        "Temperatuur en neerslag veranderen door klimaatverandering. Dat zijn [[*abiotische|biotische|reducerende]] factoren, en soorten verschuiven of verdwijnen.",
        "Abiotische factoren bepalen wat er in een gebied kan leven.",
    ),
    tabel(
        "Raakt de waterkringloop de koolstofkringloop?",
        [
            ("Water is een grondstof van de fotosynthese.", J),
            ("Bij de celademhaling komt water vrij.", J),
            ("De twee kringlopen staan volledig los van elkaar.", F),
        ],
        "De kringlopen grijpen voortdurend in elkaar.",
    ),
    mk(
        "Een ziekte doodt bijna alle bomen van een bos. Wat is het gevolg?",
        [
            "Voedselrelaties en kringlopen raken verstoord",
            "Enkel de bomen verdwijnen, de rest blijft gelijk",
            "Er komen meteen meer toproofdieren in het bos",
            "De reducenten verdwijnen als eerste uit het bos",
        ],
        0,
        "De bomen zijn de belangrijkste producenten en bepalen de structuur van het bos.",
    ),
    open_(
        "Leg uit waarom de energie in een ecosysteem in één richting stroomt, terwijl de materie rondgaat. Gebruik de woorden producenten, consumenten, reducenten en warmte.",
        "Producenten vangen lichtenergie op en leggen die vast in energierijke stoffen. Consumenten eten die op, maar bij elke stap gaat een groot deel van de energie als warmte verloren, en die komt niet terug. De materie gaat wel rond: reducenten breken dode resten af tot minerale stoffen, die de producenten opnieuw opnemen.",
    ),
]
