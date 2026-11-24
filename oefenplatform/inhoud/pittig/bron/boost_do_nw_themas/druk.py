"""Druk en de gaswetten — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, assen

# Waterton met vier punten ----------------------------------------------
WT = Prent("vier-punten-water", "Vier punten in een vat met water", "vat water met punten A tot D op verschillende diepte")
WT.rect(250, 120, 500, 420, "#ffffff", DONKER, 0)
WT.rect(252, 170, 496, 368, "#cfe5f5", "none", 0)
WT.lijn(252, 170, 748, 170, BLAUW, 3)
WT.tekst(500, 155, "wateroppervlak", 18)
PT = {"A": (340, 230), "B": (640, 330), "C": (380, 470), "D": (620, 470)}
for k, (x, y) in PT.items():
    WT.cirkel(x, y, 9, DONKER, DONKER)
    WT.letter(x + 40, y, k)
for d, y in (("1 m", 230), ("2 m", 330), ("3,5 m", 470)):
    WT.lijn(770, 170, 770, y, GRIJS, 2)
    WT.lijn(760, y, 780, y, GRIJS, 2)
    WT.tekst(830, y, d, 18)
ZW = {k: [Prent.rond(x, y, 24), Prent.rond(x + 40, y, 26)] for k, (x, y) in PT.items()}

# p-V-kromme -------------------------------------------------------------
PV = Prent("pv-kromme", "Druk en volume van een gas bij een vaste temperatuur", "dalende kromme p(V) met punten P, Q en R")
X, Y = assen(PV, 0, 5, 0, 5, "V (liter)", "p (bar)", 1, 1)
pts = []
v = 0.8
while v <= 5.0001:
    pts.append((X(v), Y(4 / v)))
    v += 0.05
PV.pad("M" + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", BLAUW, 5)
PP = {"P": (1, 4), "Q": (2, 2), "R": (4, 1)}
for k, (vv, pp) in PP.items():
    PV.cirkel(X(vv), Y(pp), 9, ORANJE, DONKER)
    PV.letter(X(vv) + 36, Y(pp) - 30, k)
ZPV = {k: [Prent.rond(X(vv), Y(pp), 26), Prent.rond(X(vv) + 36, Y(pp) - 30, 26)] for k, (vv, pp) in PP.items()}

VRAGEN = [
    klik(
        "Klik op het punt met de grootste hydrostatische druk dat het dichtst bij de wand links ligt.",
        WT.bestand, ZW["C"],
        "C en D liggen allebei op 3,5 m, de grootste diepte. C ligt links.",
    ),
    klik(
        "Klik op het punt met de kleinste hydrostatische druk.",
        WT.bestand, ZW["A"],
        "A ligt het minst diep onder het wateroppervlak.",
    ),
    met_prent(WT.bestand, tabel(
        "Kijk naar het vat. Klopt dit?",
        [
            ("In C en D is de hydrostatische druk even groot.", J),
            ("In B is de druk groter dan in A.", J),
            ("In D is de druk groter dan in C, want D ligt meer naar rechts.", F),
            ("Een breder vat zou in C een grotere druk geven.", F),
        ],
        "Enkel de diepte telt, niet de plaats links of rechts en niet de breedte van het vat.",
    )),
    met_prent(WT.bestand, inv(
        "Kijk naar het vat. Elke 10 m water geeft ongeveer 1 bar. Hoeveel bar hydrostatische druk is er ongeveer in B?",
        ["0,2", "0.2"],
        "B ligt op 2 m, dat is een vijfde van 10 m: ongeveer 0,2 bar.",
    )),
    klik(
        "Klik op het punt waar het gas het kleinste volume heeft.",
        PV.bestand, ZPV["P"],
        "P ligt het meest naar links op de volume-as: 1 liter.",
    ),
    met_prent(PV.bestand, tabel(
        "Kijk naar de kromme. Klopt dit?",
        [
            ("In P, Q en R is druk maal volume telkens 4.", J),
            ("Van Q naar R verdubbelt het volume en halveert de druk.", J),
            ("Druk en volume zijn hier recht evenredig.", F),
            ("Dit is een isotherm proces.", J),
        ],
        "Bij een vaste temperatuur blijft p · V gelijk: omgekeerd evenredig.",
    )),
    met_prent(PV.bestand, inv(
        "Kijk naar de kromme. Hoe groot is de druk als het volume 8 liter wordt, in bar?",
        ["0,5", "0.5"],
        "p · V = 4, dus 4 : 8 = 0,5 bar.",
    )),
    inv(
        "Een kist van 600 N staat op een vloer met een grondvlak van 0,2 m². Hoe groot is de druk op de vloer, in pascal?",
        ["3000"],
        "p = F : A = 600 : 0,2 = 3000 Pa.",
    ),
    tabel(
        "Wordt de druk op de ondergrond groter of kleiner?",
        [
            ("je gaat van platte schoenen naar naaldhakken", "Groter"),
            ("een vrachtwagen krijgt extra wielen", "Kleiner"),
            ("je slijpt een mes scherp", "Groter"),
            ("je gaat liggen in plaats van te staan op het ijs", "Kleiner"),
        ],
        "Minder contactoppervlak bij dezelfde kracht geeft meer druk.",
        kolommen=["Groter", "Kleiner"],
    ),
    tabel(
        "Reken om.",
        [
            ("2 bar", "200 000 Pa"),
            ("1013 hPa", "101 300 Pa"),
            ("0,5 bar", "50 000 Pa"),
        ],
        "1 bar = 100 000 Pa en 1 hPa = 100 Pa.",
        kolommen=["200 000 Pa", "101 300 Pa", "50 000 Pa"],
    ),
    casus(
        "Bij een hydraulische lift in een garage duw je met een kleine zuiger op olie. Aan de andere kant tilt een grote zuiger een auto op. De grote zuiger heeft een twintig keer groter oppervlak.",
        [
            keuze(
                "De druk in de olie is bij de grote zuiger [[*even groot als|twintig keer groter dan|twintig keer kleiner dan]] bij de kleine zuiger.",
                "Beginsel van Pascal: de druk plant zich onverminderd voort.",
            ),
            inv(
                "Je duwt met 500 N op de kleine zuiger. Hoeveel newton levert de grote zuiger?",
                ["10000", "10 000"],
                "Twintig keer meer oppervlak geeft twintig keer meer kracht: 20 · 500 = 10 000 N.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("De grote zuiger beweegt een kortere weg dan de kleine.", J),
                    ("Je wint kracht en je wint ook weg.", F),
                    ("De olie mag je vervangen door lucht zonder verschil.", F),
                ],
                "Wat je aan kracht wint, verlies je aan weg.",
            ),
        ],
    ),
    tabel(
        "Barometer of manometer?",
        [
            ("de luchtdruk in het weerbericht", "Barometer"),
            ("de druk in een fietsband", "Manometer"),
            ("de druk op een gasfles", "Manometer"),
            ("de luchtdruk op een bergtop", "Barometer"),
        ],
        "Een barometer is er voor de buitenlucht, een manometer voor een vat of leiding.",
        kolommen=["Barometer", "Manometer"],
    ),
    tabel(
        "Een duikster zwemt van 5 m naar 20 m diepte. Klopt dit?",
        [
            ("De hydrostatische druk op haar wordt groter.", J),
            ("De luchtdruk boven het water telt ook mee in de totale druk.", J),
            ("Ze moet haar oren klaren omdat de druk op haar trommelvlies stijgt.", J),
            ("Op 20 m is de hydrostatische druk kleiner, want het water is daar kouder.", F),
        ],
        "Hoe dieper, hoe meer water boven je en hoe groter de druk.",
    ),
    tabel(
        "Overdruk of onderdruk?",
        [
            ("een zuignap tegen een tegel", "Onderdruk"),
            ("een opgepompte voetbal", "Overdruk"),
            ("een fles bruiswater die nog dicht is", "Overdruk"),
            ("lucht uit een rietje zuigen", "Onderdruk"),
        ],
        "Overdruk is hoger dan de omgeving, onderdruk lager.",
        kolommen=["Overdruk", "Onderdruk"],
    ),
    tabel(
        "Reken om naar kelvin.",
        [
            ("0 °C", "273 K"),
            ("100 °C", "373 K"),
            ("-73 °C", "200 K"),
            ("-273 °C", "0 K"),
        ],
        "Tel 273 bij de graden Celsius.",
        kolommen=["0 K", "200 K", "273 K", "373 K"],
    ),
    koppel(
        "Koppel elk proces aan wat er gelijk blijft.",
        [
            ("isotherm", "de temperatuur"),
            ("isobaar", "de druk"),
            ("isochoor", "het volume"),
        ],
        ["de massadichtheid", "de diepte"],
        "Iso betekent gelijk: therm, baar en choor zeggen wat.",
    ),
    tabel(
        "Welk proces is dit?",
        [
            ("een spuitbus warmt op in de zon", "Isochoor"),
            ("je duwt traag een afgesloten spuit in", "Isotherm"),
            ("een ballon krimpt in de diepvries", "Isobaar"),
        ],
        "Spuitbus: vast volume. Spuit traag: temperatuur blijft. Ballon: druk blijft gelijk aan de buitenlucht.",
        kolommen=["Isotherm", "Isobaar", "Isochoor"],
    ),
    inv(
        "Een gas in een gesloten vat heeft 2 bar bij 300 K. Je verwarmt het tot 450 K. Hoe groot is de druk nu, in bar?",
        ["3"],
        "Bij gelijk volume zijn druk en absolute temperatuur recht evenredig: 450 : 300 = 1,5 en 1,5 · 2 = 3 bar.",
    ),
    inv(
        "Een gas van 6 liter bij 1 bar wordt bij gelijke temperatuur samengeperst tot 2 liter. Hoe groot is de druk nu, in bar?",
        ["3"],
        "p · V blijft 6. Bij 2 liter is de druk 6 : 2 = 3 bar.",
    ),
    inv(
        "Een ballon heeft 3 liter bij 300 K en de druk blijft gelijk. Hoeveel liter is hij bij 200 K?",
        ["2"],
        "Isobaar: volume en absolute temperatuur zijn recht evenredig. 200 : 300 = 2/3 en 2/3 · 3 = 2 liter.",
    ),
    mk(
        "Waarom mag je bij de gaswetten niet met graden Celsius rekenen?",
        [
            "De verhoudingen kloppen enkel vanaf het absolute nulpunt",
            "Graden Celsius bestaan niet in het lijstje van officiële eenheden",
            "Kelvin geeft altijd een kleiner en dus veel handiger getal om mee te rekenen",
            "Een thermometer meet in kelvin en niet in graden",
        ],
        0,
        "Van 10 °C naar 20 °C is geen verdubbeling van de beweging van de deeltjes. Van 283 K naar 293 K is dat duidelijk.",
    ),
    sleep(
        "Volgens het deeltjesmodel ontstaat gasdruk doordat de deeltjes tegen de [[wand]] botsen. Warm je het gas op, dan bewegen de deeltjes [[sneller]] en botsen ze harder. In een kleiner volume botsen ze [[vaker]].",
        ["trager", "minder vaak"],
        "Meer of hardere botsingen betekent meer druk.",
    ),
    tabel(
        "Klopt dit over een reëel gas?",
        [
            ("Bij lage druk gedraagt het zich bijna als een ideaal gas.", J),
            ("Bij hoge druk nemen de deeltjes zelf merkbaar plaats in.", J),
            ("Bij lage temperatuur trekken de deeltjes elkaar meer aan.", J),
            ("Het volgt de gaswet precies bij elke temperatuur.", F),
        ],
        "Een ideaal gas is een model. Echte gassen wijken af bij hoge druk en lage temperatuur.",
    ),
    volgorde(
        "Zet in de juiste volgorde: je fietspomp wordt warm.",
        [
            "Je duwt de zuiger naar beneden",
            "De lucht in de pomp wordt samengeperst",
            "De deeltjes krijgen meer energie",
            "De temperatuur van de lucht stijgt",
        ],
        "Samenpersen voert energie aan het gas toe.",
    ),
    inv(
        "Een olifant van 40 000 N staat op vier poten van elk 0,1 m². Hoe groot is de druk op de grond, in pascal?",
        ["100000", "100 000"],
        "Het totale oppervlak is 0,4 m². 40 000 : 0,4 = 100 000 Pa, dat is 1 bar.",
    ),
    tabel(
        "Een bergbeklimmer gaat van het dal naar een hoge top. Klopt dit?",
        [
            ("De luchtdruk daalt.", J),
            ("Er staat minder lucht boven haar.", J),
            ("Een zakje chips uit het dal bolt op de top op.", J),
            ("Ze heeft op de top meer zuurstof per ademteug.", F),
        ],
        "Met de hoogte daalt de luchtdruk. De lucht in het gesloten zakje duwt dan harder naar buiten dan de buitenlucht naar binnen.",
    ),
    keuze(
        "Bij het absolute nulpunt zou een gas [[*geen druk|de grootste druk|een druk van 1 bar]] uitoefenen, want de deeltjes botsen niet meer.",
        "Stilstaande deeltjes raken de wand niet.",
    ),
    open_(
        "Leg uit waarom een duiker op 30 m diepte een veel grotere druk voelt dan aan het oppervlak.",
        "Op 30 m staat er veel meer water boven hem. Het gewicht van dat water geeft een hydrostatische druk van ongeveer 3 bar. Daarbovenop komt nog de luchtdruk op het wateroppervlak, zodat de totale druk ongeveer 4 bar is.",
    ),
]
