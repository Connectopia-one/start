"""Anorganische stoffen: stofklassen en naamgeving — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Stamboom van de stofklassen ---------------------------------------------
SK = Prent("stofklassen-schema", "Indeling van de anorganische stoffen", "boomschema: bovenaan zuivere stoffen, daaronder twee takken, onderaan vier vakjes A oxiden, B hydroxiden, C zuren, D zouten")


def _vak(p, x, y, t, b=180, kl="#fbf6ea"):
    p.rect(x - b / 2, y - 28, b, 56, kl, DONKER, 12, 2)
    p.tekst(x, y + 6, t, 16, vet=True)


_vak(SK, 500, 110, "zuivere stoffen", 220)
_vak(SK, 260, 240, "enkelvoudige stoffen", 220)
_vak(SK, 740, 240, "samengestelde stoffen", 220)
for x in (140, 380):
    SK.lijn(260, 268, x, 352, DONKER, 2)
_vak(SK, 140, 380, "metalen", 160)
_vak(SK, 380, 380, "niet-metalen", 160)
SK.lijn(500, 138, 260, 212, DONKER, 2)
SK.lijn(500, 138, 740, 212, DONKER, 2)
XS = [560, 690, 820, 950]
for x in XS:
    SK.lijn(740, 268, x - 20, 482, DONKER, 2)
for i, (k, x) in enumerate(zip("ABCD", XS)):
    SK.rect(x - 75, 482, 110, 56, "#ffffff", DONKER, 12, 2)
    SK.tekst(x - 20, 516, ("oxiden", "hydroxiden", "zuren", "zouten")[i], 15, vet=True)
    SK.letter(x - 20, 585, k)
ZSK = {k: [Prent.zone(x - 75, 482, 110, 56), Prent.rond(x - 20, 585, 22)] for k, x in zip("ABCD", XS)}

# Ionrooster ---------------------------------------------------------------
IR = Prent("ionrooster-nacl", "Een stukje van het rooster van keukenzout", "raster van grote groene Cl⁻-bollen en kleine paarse Na⁺-bollen die elkaar afwisselen")
for r in range(5):
    for c in range(8):
        x, y = 200 + c * 80, 150 + r * 80
        if (r + c) % 2:
            IR.cirkel(x, y, 30, "#9fd39a", DONKER, 1.5)
            IR.tekst(x, y + 6, "Cl⁻", 15, vet=True)
        else:
            IR.cirkel(x, y, 18, "#c8a8e0", DONKER, 1.5)
            IR.tekst(x, y + 5, "Na⁺", 12, vet=True)
ZIR = {"binnen": [Prent.zone(245, 195, 470, 230)]}

VRAGEN = [
    klik(
        "In welk vakje hoort ammoniumnitraat, NH₄NO₃?",
        SK.bestand, ZSK["D"],
        "Het ammoniumion neemt de plaats van een metaalion in: het is een zout, ook zonder metaal.",
    ),
    met_prent(SK.bestand, tabel(
        "In welk vakje van het schema hoort deze stof?",
        [
            ("NaOH", "B"),
            ("H₂SO₄", "C"),
            ("KNO₃", "D"),
            ("SO₂", "A"),
            ("Ca(OH)₂", "B"),
        ],
        "Een zout is een metaalion (of ammoniumion) met een zuurrest.",
        kolommen=["A", "B", "C", "D"],
    )),
    met_prent(SK.bestand, tabel(
        "Kijk naar het schema. Klopt dit?",
        [
            ("Ozon, O₃, hoort bij de enkelvoudige stoffen.", J),
            ("IJzer hoort bij de metalen.", J),
            ("Zuurstofgas, O₂, hoort bij de niet-metalen.", J),
            ("Water hoort bij de enkelvoudige stoffen.", F),
        ],
        "Water bestaat uit twee elementen: het is samengesteld.",
    )),
    klik(
        "Klik op een ion dat in dit vlak aan vier kanten door ionen van de andere soort omringd is.",
        IR.bestand, ZIR["binnen"],
        "Elk ion binnenin het rooster heeft boven, onder, links en rechts een ion met de tegengestelde lading.",
    ),
    met_prent(IR.bestand, tabel(
        "Kijk naar het rooster. Klopt dit?",
        [
            ("Elk Na⁺-ion is omringd door Cl⁻-ionen.", J),
            ("Er zijn evenveel Na⁺- als Cl⁻-ionen.", J),
            ("NaCl bestaat als losse moleculen van twee atomen.", F),
            ("Het rooster als geheel is elektrisch neutraal.", J),
        ],
        "Een ionverbinding is een rooster, geen verzameling moleculen.",
    )),
    tabel(
        "Binair of ternair?",
        [
            ("Fe₂O₃", "Binair"),
            ("CaCO₃", "Ternair"),
            ("NaCl", "Binair"),
            ("H₂SO₄", "Ternair"),
            ("Al₂O₃", "Binair"),
        ],
        "Tel de verschillende elementen, niet de atomen.",
        kolommen=["Binair", "Ternair"],
    ),
    koppel(
        "Koppel elke formule aan haar systematische naam.",
        [
            ("Na₂SO₄", "natriumsulfaat"),
            ("Na₂SO₃", "natriumsulfiet"),
            ("NaClO", "natriumhypochloriet"),
            ("NaClO₄", "natriumperchloraat"),
        ],
        ["natriumsulfide", "natriumchloraat"],
        "Sulfide is S²⁻, chloraat is ClO₃⁻.",
    ),
    tabel(
        "Hoeveel waardig is dit zuur?",
        [
            ("HCl", "1"),
            ("H₂SO₄", "2"),
            ("H₃PO₄", "3"),
            ("HNO₃", "1"),
            ("H₂CO₃", "2"),
        ],
        "Tel de waterstofatomen die als ion kunnen loskomen.",
        kolommen=["1", "2", "3"],
    ),
    inv(
        "Hoeveel atomen telt één formule-eenheid Ca(OH)₂ in totaal?",
        ["5", "vijf"],
        "1 Ca + 2 O + 2 H = 5.",
    ),
    inv(
        "IJzer(III)oxide: welk oxidatiegetal heeft ijzer? Geef het getal.",
        ["3", "+3", "III"],
        "Het Romeinse cijfer geeft het oxidatiegetal van het metaal.",
    ),
    keuze(
        "Fe₂O₃ heet volgens de stocknotatie [[*ijzer(III)oxide|ijzer(II)oxide|ijzertrioxide]].",
        "2 x Fe³⁺ = +6 en 3 x O²⁻ = −6.",
    ),
    keuze(
        "CO heet met Griekse telwoorden [[*koolstofmonoxide|koolstofdioxide|dikoolstofoxide]].",
        "Griekse telwoorden gebruik je bij atoomverbindingen.",
    ),
    tabel(
        "Stocknotatie of Griekse telwoorden?",
        [
            ("CuCl₂", "Stocknotatie"),
            ("N₂O₅", "Griekse telwoorden"),
            ("FeSO₄", "Stocknotatie"),
            ("PCl₃", "Griekse telwoorden"),
        ],
        "Stocknotatie bij een metaal met meer dan één mogelijk oxidatiegetal, telwoorden bij niet-metalen onder elkaar.",
        kolommen=["Stocknotatie", "Griekse telwoorden"],
    ),
    sorteer(
        "Rangschik de chloorzuren van weinig naar veel zuurstofatomen.",
        ["Weinig zuurstof", "Middel", "Veel zuurstof"],
        [
            ("hypochlorigzuur, HClO", "Weinig zuurstof"),
            ("chlorigzuur, HClO₂", "Weinig zuurstof"),
            ("chloorzuur, HClO₃", "Middel"),
            ("perchloorzuur, HClO₄", "Veel zuurstof"),
        ],
        "Hypo- betekent nog één minder dan -iet, per- één meer dan -aat.",
    ),
    casus(
        "In de garage van Rik staan vier potten met enkel een triviale naam: bijtende soda, soda, bakpoeder en gebluste kalk.",
        [
            tabel(
                "Welke formule hoort bij welke pot?",
                [
                    ("bijtende soda", "NaOH"),
                    ("soda", "Na₂CO₃"),
                    ("bakpoeder", "NaHCO₃"),
                    ("gebluste kalk", "Ca(OH)₂"),
                ],
                "Soda en bijtende soda zijn twee heel verschillende stoffen.",
                kolommen=["NaOH", "Na₂CO₃", "NaHCO₃", "Ca(OH)₂"],
            ),
            keuze(
                "Bakpoeder is een [[*waterstofzout|hydraat|peroxide]].",
                "Er blijft één waterstof van het koolzuur over in de zuurrest.",
            ),
            mk(
                "Rik giet water bij ongebluste kalk. Wat ontstaat er?",
                [
                    "Gebluste kalk, Ca(OH)₂",
                    "Kalksteen, CaCO₃",
                    "Bijtende soda, NaOH",
                    "Ongebluste kalk, CaO",
                ],
                0,
                "CaO + H₂O → Ca(OH)₂, met veel warmte.",
            ),
        ],
    ),
    mk(
        "Waarom is H₂O₂ een peroxide en H₂O niet?",
        [
            "Er zitten twee zuurstofatomen aan elkaar",
            "Er zitten twee waterstofatomen in",
            "Het is een vloeistof bij kamertemperatuur",
            "Het bevat een metaal met een lading 2+",
        ],
        0,
        "Een peroxide heeft een O–O-brug.",
    ),
    tabel(
        "Klopt deze formule bij de naam?",
        [
            ("aluminiumoxide, Al₂O₃", J),
            ("magnesiumchloride, MgCl", F),
            ("calciumnitraat, Ca(NO₃)₂", J),
            ("ammoniumsulfaat, NH₄SO₄", F),
        ],
        "MgCl₂: Mg²⁺ vraagt twee Cl⁻. (NH₄)₂SO₄: SO₄²⁻ vraagt twee NH₄⁺.",
    ),
    inv(
        "Geef de formule van kaliumcarbonaat. Schrijf de cijfers gewoon achter de letters.",
        ["K2CO3", "K₂CO₃"],
        "K⁺ en CO₃²⁻: twee K⁺ voor één carbonaat.",
    ),
    inv(
        "Geef de formule van aluminiumsulfaat. Schrijf de cijfers gewoon achter de letters, met haakjes.",
        ["Al2(SO4)3", "Al₂(SO₄)₃"],
        "Al³⁺ en SO₄²⁻: 2 x 3 = 6 en 3 x 2 = 6.",
    ),
    tabel(
        "Klopt deze triviale naam?",
        [
            ("N₂O heet lachgas.", J),
            ("HCN heet blauwzuur.", J),
            ("CO₂ heet koolzuurgas.", J),
            ("NaOH heet bakpoeder.", F),
        ],
        "NaOH is bijtende soda. Bakpoeder is NaHCO₃.",
    ),
    sleep(
        "CuSO₄·5H₂O is een [[hydraat]]. De vijf moleculen [[kristalwater]] zitten in het rooster. De naam is kopersulfaat[[pentahydraat]].",
        ["peroxide", "zoutzuur", "dihydraat"],
        "Penta is vijf.",
    ),
    mk(
        "Een zout ontstaat uit salpeterzuur en kaliumhydroxide. Welk zout is het?",
        [
            "Kaliumnitraat, KNO₃",
            "Kaliumnitriet, KNO₂",
            "Kaliumnitride, K₃N",
            "Kaliumhydroxide, KOH",
        ],
        0,
        "De zuurrest NO₃⁻ komt uit het zuur, K⁺ uit de base.",
    ),
    tabel(
        "Welke stof is het?",
        [
            ("zoutzuur", "HCl in water"),
            ("zuurstofwater", "H₂O₂"),
            ("salpeterzuur", "HNO₃"),
            ("ontstopper", "NaOH-oplossing"),
        ],
        "Zuurstofwater valt langzaam uiteen in water en zuurstof.",
        kolommen=["HCl in water", "H₂O₂", "HNO₃", "NaOH-oplossing"],
    ),
    tabel(
        "Klopt dit over symbolen?",
        [
            ("K is kalium.", J),
            ("Pb is lood.", J),
            ("Fe en Cu zijn metalen uit het d-blok.", J),
            ("Ca is koolstof.", F),
        ],
        "Ca is calcium, C is koolstof.",
    ),
    mk(
        "Waarom schrijf je bij FeCl₃ ijzer(III)chloride, maar bij NaCl gewoon natriumchloride?",
        [
            "Natrium kent maar één oxidatiegetal",
            "Natrium is geen metaal en ijzer is dat wel",
            "Bij NaCl zijn er helemaal geen ionen",
            "NaCl is een atoomverbinding zonder metaal",
        ],
        0,
        "IJzer kan Fe²⁺ of Fe³⁺ zijn: dat moet je aanduiden.",
    ),
    tabel(
        "Klopt dit over de brutoformule?",
        [
            ("Ze zegt hoeveel atomen van elk element er in een molecule zitten.", J),
            ("Ze zegt niets over hoe de atomen gebonden zijn.", J),
            ("Bij een ionverbinding spreek je eerder van een formule-eenheid.", J),
            ("H₂O₂ en H₂O hebben dezelfde brutoformule.", F),
        ],
        "H₂O₂ heeft twee zuurstofatomen, H₂O één.",
    ),
    keuze(
        "De OH-groep is de kenmerkende groep van de [[*hydroxiden|oxiden|zouten]].",
        "NaOH, Ca(OH)₂ en Al(OH)₃ zijn hydroxiden.",
    ),
    open_(
        "Leg uit waarom NaCl geen molecule is, en wat de formule NaCl dan wel betekent.",
        "Keukenzout is een ionverbinding: Na⁺- en Cl⁻-ionen vormen samen een groot rooster, zonder losse deeltjes van twee atomen. De formule NaCl geeft daarom de formule-eenheid: de kleinste verhouding van de ionen, hier één Na⁺ op één Cl⁻.",
    ),
]
