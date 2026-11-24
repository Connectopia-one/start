"""Nanomaterialen — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Logaritmische grootteschaal ------------------------------------------------
GS = Prent("grootteschaal-nano", "Een grootteschaal van 0,1 nm tot 1 mm", "een horizontale as met machten van tien, van 0,1 nanometer tot 1 millimeter; het gebied van 1 tot 100 nm is gekleurd; vijf pijltjes A tot E")
XL, XR = 80, 920
LMIN, LMAX = -1, 6  # log10 van nm


def xn(nm):
    return XL + (math.log10(nm) - LMIN) / (LMAX - LMIN) * (XR - XL)


GS.rect(xn(1), 260, xn(100) - xn(1), 80, "#d6ecd2", "none", 0, 0)
GS.tekst((xn(1) + xn(100)) / 2, 245, "nanogebied", 18, vet=True, kleur=GROEN)
GS.lijn(XL, 340, XR, 340, DONKER, 3)
for e, lab in zip(range(-1, 7), ["0,1 nm", "1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm"]):
    GS.lijn(xn(10 ** e), 330, xn(10 ** e), 350, DONKER, 2)
    GS.tekst(xn(10 ** e), 378, lab, 16, vet=True)
PUNT = {"A": 0.1, "B": 1, "C": 100, "D": 7000, "E": 80000}
for k, v in PUNT.items():
    GS.pijl(xn(v), 190, xn(v), 330, DONKER, 2)
    GS.letter(xn(v), 165, k)
ZGS = {k: [Prent.zone(xn(v) - 22, 140, 44, 195)] for k, v in PUNT.items()}

# Vier nanostructuren ---------------------------------------------------------
NS = Prent("nanostructuren", "Vier nanostructuren van koolstof of metaal", "vier tekeningen: een bol uit zeshoeken en vijfhoeken, een buis met een honingraatpatroon, een vlak honingraatnet en een bolletje uit metaalatomen; letters P tot S")


def _hexnet(p, x0, y0, cols, rows, r=14, rand=DONKER, klip=None):
    w = r * math.sqrt(3)
    for j in range(rows):
        for i in range(cols):
            cx = x0 + i * w + (w / 2 if j % 2 else 0)
            cy = y0 + j * 1.5 * r
            if klip and not klip(cx, cy):
                continue
            pts = [(cx + r * math.cos(math.radians(60 * a + 30)), cy + r * math.sin(math.radians(60 * a + 30))) for a in range(6)]
            p.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts) + " Z", "none", rand, 2)


# P: buckyball
NS.cirkel(140, 280, 85, "#f4f1e8", DONKER, 3)
_hexnet(NS, 65, 205, 7, 7, 13, klip=lambda x, y: (x - 140) ** 2 + (y - 280) ** 2 < 70 ** 2)
for a in range(5):
    cx = 140 + 40 * math.cos(math.radians(72 * a - 90))
    cy = 280 + 40 * math.sin(math.radians(72 * a - 90))
    pts = [(cx + 10 * math.cos(math.radians(72 * b - 90)), cy + 10 * math.sin(math.radians(72 * b - 90))) for b in range(5)]
    NS.pad("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z", "#f7d9b5", DONKER, 2)
# Q: nanobuis
NS.rect(300, 220, 200, 120, "#f4f1e8", DONKER, 0, 3)
_hexnet(NS, 308, 232, 8, 6, 13, klip=lambda x, y: 300 < x < 498 and 222 < y < 338)
NS.ellips(500, 280, 22, 60, "#ffffff", DONKER, 3)
NS.ellips(300, 280, 22, 60, "#f4f1e8", DONKER, 3)
# R: grafeen
NS.rect(570, 210, 220, 140, "#f4f1e8", DONKER, 0, 2)
_hexnet(NS, 590, 228, 8, 6, 13, klip=lambda x, y: 585 < x < 775 and 222 < y < 338)
# S: metaalnanodeeltje
for (dx, dy) in [(0, 0), (-28, 0), (28, 0), (-14, -24), (14, -24), (-14, 24), (14, 24), (0, -48), (0, 48), (-42, -24), (42, -24), (-42, 24), (42, 24)]:
    NS.cirkel(890 + dx, 280 + dy, 15, "#e7c55b", DONKER, 2)
for k, x in zip("PQRS", (140, 400, 680, 890)):
    NS.letter(x, 450, k)
ZNS = {"P": [Prent.rond(140, 280, 90), Prent.rond(140, 450, 22)],
       "Q": [Prent.zone(275, 215, 250, 130), Prent.rond(400, 450, 22)],
       "R": [Prent.zone(555, 195, 250, 170), Prent.rond(680, 450, 22)],
       "S": [Prent.rond(890, 280, 75), Prent.rond(890, 450, 22)]}

VRAGEN = [
    klik(
        "Klik op de dikte van een menselijke haar.",
        GS.bestand, ZGS["E"],
        "Ongeveer 80 000 nm, of 80 µm.",
    ),
    klik(
        "Klik op de grootte van een los atoom.",
        GS.bestand, ZGS["A"],
        "Een atoom is ongeveer 0,1 nm groot, onder het nanogebied.",
    ),
    met_prent(GS.bestand, tabel(
        "Ligt dit punt in het nanogebied?",
        [
            ("A", "Nee"),
            ("B", "Ja"),
            ("C", "Ja"),
            ("D", "Nee"),
        ],
        "Een nanomateriaal meet ongeveer 1 tot 100 nm.",
        kolommen=["Ja", "Nee"],
    )),
    met_prent(GS.bestand, inv(
        "Hoeveel keer groter is punt E dan punt C?",
        ["800", "achthonderd"],
        "80 000 nm / 100 nm = 800.",
    )),
    klik(
        "Klik op het 2D-nanomateriaal.",
        NS.bestand, ZNS["R"],
        "Grafeen: één laag koolstofatomen, alleen in de dikte nanoklein.",
    ),
    klik(
        "Klik op de structuur die als opgerold grafeen kan gezien worden.",
        NS.bestand, ZNS["Q"],
        "Een koolstofnanobuis: 1D, lang in één richting.",
    ),
    met_prent(NS.bestand, tabel(
        "Is deze structuur een 0D-, 1D- of 2D-nanomateriaal?",
        [
            ("P", "0D"),
            ("Q", "1D"),
            ("R", "2D"),
            ("S", "0D"),
        ],
        "0D is in alle richtingen nanoklein, 1D lang in één richting, 2D lang in twee richtingen.",
        kolommen=["0D", "1D", "2D"],
    )),
    met_prent(NS.bestand, tabel(
        "Waarvoor gebruikt men een structuur zoals deze?",
        [
            ("S als gouddeeltje", "Covidtest"),
            ("R", "Buigbaar scherm"),
            ("Q", "Licht en sterk materiaal"),
        ],
        "Goud op nanomaat kleurt de teststreep, grafeen is doorzichtig en geleidend, nanobuizen zijn heel sterk.",
        kolommen=["Covidtest", "Buigbaar scherm", "Licht en sterk materiaal"],
    )),
    inv(
        "Een kubus heeft een ribbe van 1 cm. Je verdeelt hem in kubusjes van 1 mm. Hoeveel keer groter wordt het totale oppervlak?",
        ["10", "tien"],
        "1000 kubusjes van 6 mm² = 6000 mm², tegenover 600 mm² eerst: 10 keer.",
    ),
    mk(
        "Waarom is een nanokatalysator zo zuinig?",
        [
            "Hij heeft veel oppervlak per gram",
            "Hij wordt tijdens de reactie opgebruikt",
            "Hij verandert de reactie-energie",
            "Hij werkt alleen in het donker",
        ],
        0,
        "Een katalysator werkt aan zijn oppervlak.",
    ),
    tabel(
        "Is dit een top-down- of een bottom-upmethode?",
        [
            ("een vaste stof fijnmalen", "Top-down"),
            ("een laag wegetsen", "Top-down"),
            ("deeltjes laten groeien uit losse atomen", "Bottom-up"),
            ("moleculen zichzelf laten ordenen", "Bottom-up"),
        ],
        "Top-down begint groot, bottom-up begint bij atomen of moleculen.",
        kolommen=["Top-down", "Bottom-up"],
    ),
    casus(
        "Een zonnecrème bevat titaandioxide in nanodeeltjes.",
        [
            mk(
                "Waarom kiest men voor nanodeeltjes en niet voor gewone korrels?",
                [
                    "Ze filteren uv en blijven doorzichtig",
                    "Ze zijn veel goedkoper dan gewone korrels",
                    "Ze lossen op in water en spoelen zo weg",
                    "Ze maken de huid bruin zonder de zon",
                ],
                0,
                "Gewone korrels geven een witte laag op de huid.",
            ),
            keuze(
                "Op het etiket moet er [[*nano|bio|light]] staan bij die stof.",
                "Zo weet de koper dat er deeltjes op nanomaat in zitten.",
            ),
            tabel(
                "Is dit een voordeel of een mogelijk nadeel?",
                [
                    ("doorzichtig op de huid", "Voordeel"),
                    ("deeltjes kunnen tot in cellen komen", "Nadeel"),
                    ("het effect op het milieu is nog niet goed gekend", "Nadeel"),
                ],
                "Nanomaterialen hebben nieuwe voordelen en nieuwe risico's.",
                kolommen=["Voordeel", "Nadeel"],
            ),
        ],
    ),
    mk(
        "Waarom smelt een goudnanodeeltje bij een lagere temperatuur dan een goudklomp?",
        [
            "Veel atomen zitten aan het oppervlak",
            "Het bevat naast goud ook andere atomen",
            "Het heeft een hogere dichtheid dan de klomp",
            "Het gedraagt zich zoals een thermoplast",
        ],
        0,
        "Atomen aan het oppervlak zijn minder sterk gebonden.",
    ),
    tabel(
        "Klopt dit over grafeen?",
        [
            ("Het is per gewicht sterker dan staal.", J),
            ("Het geleidt stroom.", J),
            ("Het bestaat uit één laag koolstofatomen.", J),
            ("Het is een 0D-materiaal.", F),
        ],
        "Grafeen is 2D.",
    ),
    koppel(
        "Koppel elk nanomateriaal aan zijn eigenschap of toepassing.",
        [
            ("zilvernanodeeltjes", "antibacterieel in verband of sokken"),
            ("quantumdots", "kleur in een scherm"),
            ("nanobuizen", "versterking van een licht materiaal"),
            ("titaandioxide nano", "uv-filter in zonnecrème"),
        ],
        ["magnetisch maken van glas"],
        "Telkens volgt de toepassing uit de kleine maat.",
    ),
    volgorde(
        "Zet van klein naar groot.",
        ["een atoom", "een buckyball", "een nanodeeltje van 50 nm", "een haar"],
        "0,1 nm, ongeveer 1 nm, 50 nm en ongeveer 80 000 nm.",
    ),
    mk(
        "Waarom kan je nanodeeltjes niet zien met een gewone lichtmicroscoop?",
        [
            "Ze zijn kleiner dan de golflengte van licht",
            "Ze zijn helemaal doorzichtig voor alle licht",
            "Ze bewegen te snel heen en weer om te zien",
            "Ze lossen op zodra er licht op valt",
        ],
        0,
        "Daarvoor is een elektronenmicroscoop nodig.",
    ),
    sleep(
        "Hoe [[kleiner]] een deeltje, hoe groter zijn oppervlak ten opzichte van zijn [[volume]]. Daardoor is een nanodeeltje vaak [[reactiever]].",
        ["groter", "massa", "trager"],
        "Dat is de kern van de nanochemie.",
    ),
    inv(
        "Hoeveel nanometer is 1 micrometer?",
        ["1000", "duizend"],
        "1 µm = 10⁻⁶ m = 1000 × 10⁻⁹ m.",
    ),
    tabel(
        "Welke eigenschap verandert hier op nanomaat?",
        [
            ("goud dat rood kleurt", "Optisch"),
            ("een lager smeltpunt", "Thermisch"),
            ("zilver dat bacteriën doodt", "Chemisch"),
        ],
        "Kleur is optisch, smelten is thermisch, reactiviteit is chemisch.",
        kolommen=["Optisch", "Thermisch", "Chemisch"],
    ),
    inv(
        "Een buckyball C₆₀ heeft de vorm van een voetbal. Hoeveel koolstofatomen zitten er in twee zulke balletjes samen?",
        ["120", "honderdtwintig"],
        "2 × 60 = 120.",
    ),
    tabel(
        "Is dit een 0D-, 1D-, 2D- of 3D-nanomateriaal?",
        [
            ("een quantumdot", "0D"),
            ("een nanodraad", "1D"),
            ("een laagje van één atoom dik", "2D"),
            ("een gewoon blok met nanoporen", "3D"),
        ],
        "Tel in hoeveel richtingen het materiaal groot is.",
        kolommen=["0D", "1D", "2D", "3D"],
    ),
    mk(
        "Waarom geleidt een koolstofnanobuis stroom?",
        [
            "Pi-elektronen bewegen langs de buis",
            "Er zitten metaalionen in de wand van de buis",
            "De buis is gevuld met een zoutoplossing",
            "Koolstof staat altijd vrij zijn elektronen af",
        ],
        0,
        "Net als in grafeen kunnen de elektronen van de pi-bindingen bewegen.",
    ),
    keuze(
        "Nanodeeltjes zijn een risico voor de gezondheid omdat ze tot [[*in de cellen|op de huid|in de kleren]] kunnen komen.",
        "Grote deeltjes blijven buiten, nanodeeltjes niet altijd.",
    ),
    tabel(
        "Klopt dit over nanoplastics?",
        [
            ("Ze zijn kleiner dan microplastics.", J),
            ("Ze kunnen door celwanden gaan.", J),
            ("Ze breken snel af in de natuur.", F),
        ],
        "De stevige ketens breken nauwelijks af.",
    ),
    inv(
        "Hoeveel meter is 1 nanometer? Schrijf als 10^-x.",
        ["10^-9", "10⁻⁹", "1e-9", "10^(-9)"],
        "Nano staat voor een miljardste.",
    ),
    mk(
        "Waarom kleurt een teststreep van een covidtest met gouden nanodeeltjes rood en niet goudgeel?",
        [
            "Op nanomaat reageert goud anders op licht",
            "Er wordt rode kleurstof aan het goud toegevoegd",
            "Goud wordt in de test geoxideerd tot roest",
            "Het bloed van de test kleurt de streep",
        ],
        0,
        "De kleur hangt af van de grootte van het deeltje.",
    ),
    open_(
        "Leg uit waarom zilver op nanomaat zoveel sterker antibacterieel werkt dan een zilveren lepel.",
        "Een nanodeeltje is heel klein, zodat een groot deel van zijn atomen aan het oppervlak zit. Met dezelfde massa zilver heb je dus veel meer oppervlak waar zilverionen vrijkomen en waar bacteriën mee in contact komen. Bij een lepel zit bijna al het zilver binnenin en doet niet mee.",
    ),
]
