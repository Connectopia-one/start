"""De zon en het zonnestelsel — pittig (🌍 Beyond doorstroom, aardrijkskunde)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Doorsnede van de zon --------------------------------------------------
ZO = Prent("zon-doorsnede", "Doorsnede van de zon (niet op schaal)", "zon met lagen A tot E en een boog gas F")
CX, CY = 420, 350
ZO.cirkel(CX, CY, 270, "#fde9c4", "none")              # corona
ZO.cirkel(CX, CY, 222, "#f7b267", DONKER, 1)            # chromosfeer
ZO.cirkel(CX, CY, 210, "#f4a259", DONKER, 2)            # fotosfeer
ZO.cirkel(CX, CY, 196, "#f08a4b", "none")               # convectiezone
ZO.cirkel(CX, CY, 130, "#e9724c", "none")               # stralingszone
ZO.cirkel(CX, CY, 60, "#c8553d", DONKER, 2)             # kern
ZO.cirkel(CX + 120, CY - 150, 10, "#9b4a2a", "none")    # zonnevlek
ZO.pad(f"M{CX + 190} {CY - 90} C {CX + 290} {CY - 170} {CX + 300} {CY - 40} {CX + 205} {CY - 40}", "none", ROOD, 6)
def _op(r, hoek):
    return CX + r * math.cos(math.radians(hoek)), CY - r * math.sin(math.radians(hoek))
ZO.letter(CX, CY, "A")
LAGEN = {"B": (_op(95, 190), (90, 300)), "C": (_op(180, 200), (90, 380)), "D": (_op(210, 215), (90, 460)), "E": (_op(250, 232), (90, 540))}
for k, ((x, y), (lx, ly)) in LAGEN.items():
    ZO.cirkel(x, y, 5, DONKER, DONKER)
    ZO.lijn(x, y, lx + 20, ly, DONKER, 1)
    ZO.letter(lx, ly, k)
ZZO = {"A": [Prent.rond(CX, CY, 55)]}
for k, ((x, y), (lx, ly)) in LAGEN.items():
    ZZO[k] = [Prent.rond(lx, ly, 24), Prent.rond(x, y, 14)]
ZO.letter(CX + 330, CY - 110, "F")
ZZO["F"] = [Prent.rond(CX + 330, CY - 110, 26), Prent.zone(CX + 200, CY - 170, 110, 140)]

# Zonnestelsel schema ----------------------------------------------------
ZS = Prent("zonnestelsel-schema", "Ons zonnestelsel, schematisch (niet op schaal)", "zon met banen, twee gordels en een komeet, punten A tot E")
SX, SY, H0 = 70, 360, 0.52
def _pt(r, th): return SX + r * math.cos(th), SY + r * math.sin(th)
def _boog(r, kleur="#c9c3b2"):
    x1, y1 = _pt(r, -H0); x2, y2 = _pt(r, H0)
    ZS.pad(f"M{x1:.0f} {y1:.0f} A {r} {r} 0 0 1 {x2:.0f} {y2:.0f}", "none", kleur, 1)
ZS.cirkel(SX, SY, 45, "#f4a259", DONKER)
banen = [90, 115, 140, 170, 290, 370, 440, 500]
groot = [5, 7, 7, 6, 22, 18, 12, 12]
for i, r in enumerate(banen):
    _boog(r)
    x, y = _pt(r, -0.3 + i * 0.07)
    ZS.cirkel(x, y, groot[i], "#7f8fa6" if i >= 4 else "#a0826d", DONKER, 1)
for j in range(70):
    th = -H0 + j * (2 * H0 / 70)
    x, y = _pt(215 + (j * 37 % 30), th)
    ZS.cirkel(x, y, 2.5, "#b3ab95", "none")
for j in range(60):
    th = -H0 + j * (2 * H0 / 60)
    x, y = _pt(545 + (j * 29 % 35), th)
    ZS.cirkel(x, y, 2.5, "#7f9fbf", "none")
# komeet onderaan, staart weg van de zon
KX, KY = _pt(330, 0.42)
hoek = math.atan2(KY - SY, KX - SX)
ZS.cirkel(KX, KY, 9, "#dfe6ee", DONKER, 1)
ZS.pad(f"M{KX:.0f} {KY - 8:.0f} L {KX + 150 * math.cos(hoek) - 10:.0f} {KY + 150 * math.sin(hoek) - 20:.0f} L {KX + 150 * math.cos(hoek) + 15:.0f} {KY + 150 * math.sin(hoek) + 10:.0f} Z", "#e8eef5", "#9bb4c8", 1)
P = {"A": (_pt(170, -0.2)[0], _pt(170, -0.2)[1] - 40),
     "B": (_pt(230, -0.42)[0] + 10, _pt(230, -0.42)[1] - 30),
     "C": (_pt(290, -0.02)[0] + 40, _pt(290, -0.02)[1] - 35),
     "D": (_pt(560, -0.2)[0] + 50, _pt(560, -0.2)[1]),
     "E": (KX - 50, KY + 10)}
for k, (x, y) in P.items():
    ZS.letter(x, y, k)
ZZS = {k: [Prent.rond(x, y, 26)] for k, (x, y) in P.items()}
ZZS["B"].append(Prent.rond(*_pt(228, -0.3), 30))
ZZS["C"].append(Prent.rond(*_pt(290, -0.02), 30))
ZZS["D"].append(Prent.rond(*_pt(560, 0), 34))
ZZS["E"].append(Prent.rond(KX + 50, KY + 40, 60))

VRAGEN = [
    klik(
        "Klik op de laag waar kernfusie de energie levert.",
        ZO.bestand, ZZO["A"],
        "In de kern smelten waterstofkernen samen tot helium.",
    ),
    klik(
        "Klik op het zichtbare oppervlak van de zon.",
        ZO.bestand, ZZO["D"],
        "De fotosfeer is de laag waaruit het zonlicht ontsnapt.",
    ),
    klik(
        "Klik op de buitenste laag, die je enkel bij een totale zonsverduistering ziet.",
        ZO.bestand, ZZO["E"],
        "De corona is zwak naast de felle fotosfeer.",
    ),
    klik(
        "Klik op de protuberans.",
        ZO.bestand, ZZO["F"],
        "Een boog gas die langs magnetische veldlijnen boven het oppervlak hangt.",
    ),
    met_prent(ZO.bestand, tabel(
        "Kijk naar de doorsnede. Welke letter hoort bij welke laag?",
        [
            ("stralingszone", "B"),
            ("convectiezone", "C"),
            ("kern", "A"),
            ("fotosfeer", "D"),
        ],
        "Van binnen naar buiten: kern, stralingszone, convectiezone, fotosfeer, chromosfeer, corona.",
        kolommen=["A", "B", "C", "D", "E"],
    )),
    klik(
        "Klik op de planetoïdengordel.",
        ZS.bestand, ZZS["B"],
        "Tussen de baan van Mars en die van Jupiter.",
    ),
    klik(
        "Klik op de baan van de grootste planeet.",
        ZS.bestand, ZZS["C"],
        "De vijfde baan, voorbij de planetoïdengordel: Jupiter.",
    ),
    klik(
        "Klik op de ring van ijzige brokstukken waarin ook Pluto ligt.",
        ZS.bestand, ZZS["D"],
        "De Kuipergordel ligt voorbij Neptunus.",
    ),
    met_prent(ZS.bestand, tabel(
        "Kijk naar de komeet bij E. Klopt dit?",
        [
            ("De staart wijst weg van de zon.", J),
            ("De komeet heeft een uitgerekte, elliptische baan.", J),
            ("Ver van de zon heeft ze een even lange staart.", F),
            ("De staart ontstaat doordat ijs verdampt dicht bij de zon.", J),
        ],
        "Zonnewind en stralingsdruk blazen de staart weg van de zon.",
    )),
    met_prent(ZS.bestand, keuze(
        "Punt A wijst naar de baan van [[*Mars|Jupiter|Venus]], de buitenste terrestrische planeet.",
        "Mercurius, Venus, aarde en Mars liggen binnen de planetoïdengordel.",
    )),
    tabel(
        "Terrestrische planeet of gasreus?",
        [
            ("Mercurius", "Terrestrisch"),
            ("Saturnus", "Gasreus"),
            ("Mars", "Terrestrisch"),
            ("Neptunus", "Gasreus"),
            ("Venus", "Terrestrisch"),
        ],
        "Klein en rotsachtig of groot zonder vast oppervlak.",
        kolommen=["Terrestrisch", "Gasreus"],
    ),
    tabel(
        "Meteoroïde, meteoor of meteoriet?",
        [
            ("een brokje dat nog in de ruimte rondvliegt", "Meteoroïde"),
            ("een lichtspoor aan de nachtelijke hemel", "Meteoor"),
            ("een steen uit de ruimte in een museum", "Meteoriet"),
        ],
        "Ruimte, atmosfeer, grond.",
        kolommen=["Meteoroïde", "Meteoor", "Meteoriet"],
    ),
    tabel(
        "Klopt dit over zonnevlekken?",
        [
            ("Ze zijn koeler dan de omgeving.", J),
            ("Een sterk magneetveld remt er de warmtestroom.", J),
            ("Bij een zonnemaximum zijn er weinig.", F),
            ("Hun aantal schommelt met een cyclus van ongeveer 11 jaar.", J),
        ],
        "Bij een maximum zijn er juist veel zonnevlekken.",
    ),
    volgorde(
        "Zet het ontstaan van het poollicht in de juiste volgorde.",
        [
            "De zon stoot geladen deeltjes uit",
            "De zonnewind bereikt de aarde",
            "Het magneetveld leidt de deeltjes naar de poolstreken",
            "De deeltjes botsen op zuurstof en stikstof hoog in de lucht",
            "Die gassen lichten op",
        ],
        "Zonnewind, magneetveld, botsing, licht.",
    ),
    tabel(
        "Kan een sterke zonnestorm dit veroorzaken?",
        [
            ("storingen in satellieten", J),
            ("poollicht tot in onze streken", J),
            ("spanningspieken in hoogspanningsnetten", J),
            ("een aardbeving", F),
        ],
        "Een zonnestorm werkt op het magneetveld en de elektronica, niet op de aardkorst.",
    ),
    volgorde(
        "Zet het ontstaan van het zonnestelsel in de juiste volgorde.",
        [
            "Een wolk gas en stof trekt samen onder haar zwaartekracht",
            "In het hart begint kernfusie: de zon ontstaat",
            "Rond de jonge zon blijft een platte schijf over",
            "Stof klontert samen tot steeds grotere brokken",
            "De planeten ontstaan",
        ],
        "Daarom draaien alle planeten in dezelfde zin en bijna in hetzelfde vlak.",
    ),
    mk(
        "Waarom draaien alle planeten in dezelfde zin en bijna in hetzelfde vlak?",
        [
            "Ze ontstonden uit dezelfde platte, draaiende schijf",
            "De zonnewind duwt ze allemaal netjes in dezelfde richting",
            "Jupiter trekt ze met zijn zwaartekracht in één vlak",
            "Ze werden na hun ontstaan één voor één door de zon ingevangen",
        ],
        0,
        "Het is een sterke aanwijzing voor het ontstaan uit een schijf.",
    ),
    tabel(
        "Kuipergordel of Oortwolk?",
        [
            ("een platte ring voorbij Neptunus", "Kuipergordel"),
            ("een bolvormige schil heel ver weg", "Oortwolk"),
            ("Pluto ligt erin", "Kuipergordel"),
            ("bron van kometen met heel lange omlooptijden", "Oortwolk"),
        ],
        "De Oortwolk ligt duizenden keren verder dan de Kuipergordel.",
        kolommen=["Kuipergordel", "Oortwolk"],
    ),
    tabel(
        "Klopt dit over de eerste atmosfeer van de aarde?",
        [
            ("Vulkanen bliezen waterdamp en koolstofdioxide uit.", J),
            ("Er zat al veel vrije zuurstof in.", F),
            ("Ook stikstof en zwavelgassen zaten erin.", J),
        ],
        "Vrije zuurstof kwam pas veel later, door levende wezens.",
    ),
    tabel(
        "Dwergplaneet of planetoïde?",
        [
            ("bolvormig door haar eigen zwaartekracht", "Dwergplaneet"),
            ("klein met een onregelmatige vorm", "Planetoïde"),
            ("Pluto", "Dwergplaneet"),
            ("een rotsbrok in de gordel tussen Mars en Jupiter", "Planetoïde"),
        ],
        "Pluto geldt sinds 2006 als dwergplaneet.",
        kolommen=["Dwergplaneet", "Planetoïde"],
    ),
    casus(
        "Elk jaar rond 12 augustus zie je veel vallende sterren: de Perseïden.",
        [
            keuze(
                "De aarde kruist dan het [[*stofspoor van een komeet|pad van de maan|magneetveld van Jupiter]].",
                "Een komeet laat stof achter langs haar baan.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("Elke vallende ster is een meteoor.", J),
                    ("De meeste brokjes verbranden helemaal in de atmosfeer.", J),
                    ("Elke vallende ster wordt een meteoriet.", F),
                ],
                "Enkel wat de grond haalt, heet een meteoriet.",
            ),
        ],
    ),
    sleep(
        "Energie ontstaat in de [[kern]] van de zon. Ze ontsnapt als licht uit de [[fotosfeer]]. De hete buitenste laag, de [[corona]], zie je enkel bij een totale zonsverduistering.",
        ["planetoïde", "Oortwolk"],
        "Van binnen naar buiten: kern, stralingszone, convectiezone, fotosfeer, chromosfeer, corona.",
    ),
    keuze(
        "Volgens de inslagtheorie ontstond de maan door een [[*botsing met de jonge aarde|samentrekkende gaswolk|vangst door Jupiter]].",
        "Een hemellichaam ter grootte van Mars ramde de jonge aarde.",
    ),
    met_prent(ZO.bestand, keuze(
        "Het donkere vlekje bovenaan op de zon is een [[*zonnevlek|protuberans|meteoriet]].",
        "Een zonnevlek is koeler en daardoor donkerder.",
    )),
    inv(
        "Hoeveel planeten telt ons zonnestelsel sinds 2006?",
        ["8", "acht"],
        "Pluto geldt sindsdien als dwergplaneet.",
    ),
    tabel(
        "Klopt dit over de gasreuzen?",
        [
            ("Ze hebben geen vast oppervlak.", J),
            ("Ze hebben elk meerdere manen.", J),
            ("Jupiter is de grootste planeet.", J),
            ("Mercurius en Venus hebben veel manen.", F),
        ],
        "Mercurius en Venus hebben geen enkele maan.",
    ),
    keuze(
        "Komt een komeet dicht bij de zon, dan vormt er zich rond de kern een wolk gas en stof: de [[*coma|corona|chromosfeer]].",
        "De corona hoort bij de zon.",
    ),
    tabel(
        "Klopt dit over de zonnewind?",
        [
            ("Hij bestaat vooral uit protonen en elektronen.", J),
            ("Hij ontsnapt uit de corona.", J),
            ("Hij blijft binnen de baan van Mercurius.", F),
        ],
        "De zonnewind doorkruist het hele zonnestelsel.",
    ),
    open_(
        "Leg uit waarom de staart van een komeet op de terugweg voor de komeet uit loopt.",
        "De staart wordt door de zonnewind en de stralingsdruk altijd weg van de zon geblazen. Beweegt de komeet weg van de zon, dan wijst die richting ook naar voren. Daarom loopt de staart dan voorop.",
    ),
]
