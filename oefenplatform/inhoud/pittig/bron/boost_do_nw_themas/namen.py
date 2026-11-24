"""Stoffen classificeren en benoemen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Formulekaarten ----------------------------------------------------------
KRT = Prent("formulekaarten", "Acht formules", "kaarten met CaO, NaOH, HCl, NaCl, H₂SO₄, CaCO₃, CO en NH₄NO₃")
KAART = {}
for i, f in enumerate(["CaO", "NaOH", "HCl", "NaCl", "H₂SO₄", "CaCO₃", "CO", "NH₄NO₃"]):
    x, y = 70 + (i % 4) * 225, 110 + (i // 4) * 220
    KRT.rect(x, y, 190, 160, "#ffffff", DONKER, 16)
    KRT.tekst(x + 95, y + 95, f, 40, vet=True)
    KAART[f] = Prent.zone(x, y, 190, 160)

# Vier structuurformules --------------------------------------------------
ALK = Prent("vier-alkanen", "Vier structuurformules", "structuurformules van alkanen met 1, 3, 2 en 4 koolstofatomen")
BLOK = {}
def _alkaan(letter, n, x0, y0):
    ALK.rect(x0, y0, 440, 240, "#ffffff", DONKER, 12)
    ALK.letter(x0 + 24, y0 + 24, letter)
    BLOK[letter] = Prent.zone(x0, y0, 440, 240)
    breedte = 70 * (n - 1)
    sx, cy = x0 + 220 - breedte / 2, y0 + 130
    for i in range(n):
        cx = sx + i * 70
        ALK.tekst(cx, cy + 10, "C", 28, vet=True)
        ALK.lijn(cx, cy - 16, cx, cy - 40, DONKER, 3); ALK.tekst(cx, cy - 46, "H", 22)
        ALK.lijn(cx, cy + 18, cx, cy + 42, DONKER, 3); ALK.tekst(cx, cy + 66, "H", 22)
        if i < n - 1:
            ALK.lijn(cx + 14, cy, cx + 56, cy, DONKER, 3)
    ALK.lijn(sx - 14, cy, sx - 38, cy, DONKER, 3); ALK.tekst(sx - 50, cy + 8, "H", 22)
    ex = sx + (n - 1) * 70
    ALK.lijn(ex + 14, cy, ex + 38, cy, DONKER, 3); ALK.tekst(ex + 50, cy + 8, "H", 22)
_alkaan("A", 1, 40, 70, )
_alkaan("B", 3, 520, 70)
_alkaan("C", 2, 40, 360)
_alkaan("D", 4, 520, 360)

VRAGEN = [
    klik(
        "Klik op de formule van een oxide.",
        KRT.bestand, [KAART["CaO"], KAART["CO"]],
        "Een oxide is een binaire verbinding met zuurstof: CaO en CO.",
    ),
    klik(
        "Klik op de formule van een hydroxide.",
        KRT.bestand, [KAART["NaOH"]],
        "Een metaal met een OH-groep is een hydroxide.",
    ),
    klik(
        "Klik op de formule van een ternair zuur.",
        KRT.bestand, [KAART["H₂SO₄"]],
        "Waterstof vooraan maakt het een zuur. Met zwavel en zuurstof erbij zijn er drie elementen.",
    ),
    klik(
        "Klik op de formule van een ammoniumzout.",
        KRT.bestand, [KAART["NH₄NO₃"]],
        "In een ammoniumzout vervangt het ammoniumion NH₄ plus het metaalion.",
    ),
    klik(
        "Klik op de stof die met zuur opschuimt en in kalkaanslag voorkomt.",
        KRT.bestand, [KAART["CaCO₃"]],
        "Calciumcarbonaat geeft koolstofdioxide vrij als er zuur bij komt.",
    ),
    met_prent(KRT.bestand, tabel(
        "Kijk naar de acht formules. Klopt dit?",
        [
            ("HCl is een binair zuur.", J),
            ("NaCl is een binair zout.", J),
            ("CaCO₃ is een binair zout.", F),
            ("CO is een gevaarlijk, geurloos gas.", J),
            ("NaOH heet in het dagelijks leven keukenzout.", F),
        ],
        "CaCO₃ bevat drie elementen. NaOH is bijtende soda, NaCl is keukenzout.",
    )),
    klik(
        "Klik op de structuurformule van propaan.",
        ALK.bestand, [BLOK["B"]],
        "Prop staat voor drie: drie koolstofatomen.",
    ),
    klik(
        "Klik op de structuurformule van het hoofdbestanddeel van aardgas.",
        ALK.bestand, [BLOK["A"]],
        "Aardgas bestaat vooral uit methaan, met één koolstofatoom.",
    ),
    klik(
        "Klik op de structuurformule die bij de brutoformule C₂H₆ past.",
        ALK.bestand, [BLOK["C"]],
        "Twee koolstofatomen en zes waterstofatomen: ethaan.",
    ),
    met_prent(ALK.bestand, tabel(
        "Kijk naar de vier structuurformules. Klopt dit?",
        [
            ("Elk koolstofatoom maakt vier bindingen.", J),
            ("D is butaan, met brutoformule C₄H₁₀.", J),
            ("Deze stoffen bevatten ook zuurstof.", F),
            ("Propaan en butaan zitten in een gasfles voor de barbecue.", J),
        ],
        "Alkanen bestaan enkel uit koolstof en waterstof.",
    )),
    koppel(
        "Koppel elk ion aan zijn formule.",
        [
            ("nitraation", "NO₃⁻"),
            ("sulfaation", "SO₄²⁻"),
            ("carbonaation", "CO₃²⁻"),
            ("chloride-ion", "Cl⁻"),
            ("ammoniumion", "NH₄⁺"),
        ],
        ["ClO₃⁻"],
        "ClO₃⁻ is het chloraation, met zuurstof erin.",
    ),
    koppel(
        "Koppel elke triviale naam aan de stof.",
        [
            ("keukenzout", "natriumchloride"),
            ("zoutzuur", "waterstofchloride in water"),
            ("bijtende soda", "natriumhydroxide"),
            ("ongebluste kalk", "calciumoxide"),
            ("gebluste kalk", "calciumhydroxide"),
            ("lachgas", "distikstofoxide"),
        ],
        ["koolstofmonoxide"],
        "Koolstofmonoxide heeft geen gebruikelijke triviale naam in deze lijst.",
    ),
    tabel(
        "Oxide, hydroxide, zuur of zout?",
        [
            ("Ca(OH)₂", "Hydroxide"),
            ("H₂S", "Zuur"),
            ("CO₂", "Oxide"),
            ("NaHCO₃", "Zout"),
            ("HNO₃", "Zuur"),
        ],
        "Waterstof vooraan wijst op een zuur, OH bij een metaal op een hydroxide.",
        kolommen=["Oxide", "Hydroxide", "Zuur", "Zout"],
    ),
    volgorde(
        "Zet deze alkanen van weinig naar veel koolstofatomen.",
        ["methaan", "propaan", "pentaan", "heptaan", "nonaan"],
        "Methaan 1, propaan 3, pentaan 5, heptaan 7, nonaan 9.",
    ),
    inv(
        "Een alkaan heeft zes koolstofatomen. Hoeveel waterstofatomen heeft het? Elk koolstofatoom maakt vier bindingen.",
        ["14", "veertien"],
        "Hexaan is C₆H₁₄: de vier middelste C dragen elk 2 H, de twee eind-C elk 3 H. Samen 8 plus 6 is 14.",
    ),
    casus(
        "Op een fles ontstopper staat: bevat natriumhydroxide. Op een fles ontkalker staat: bevat zoutzuur.",
        [
            tabel(
                "Klopt dit over de twee flessen?",
                [
                    ("De ontstopper bevat een sterke base.", J),
                    ("De ontkalker bevat een zuur.", J),
                    ("Zoutzuur is een ternair zuur.", F),
                    ("Natriumhydroxide heet ook bijtende soda.", J),
                ],
                "Zoutzuur bevat enkel waterstof en chloor: binair.",
            ),
            mk(
                "Waarom werkt de ontkalker tegen kalkaanslag?",
                [
                    "Zuur maakt calciumcarbonaat los",
                    "Zuur maakt de kalk harder en gladder",
                    "Zuur verandert kalk in keukenzout",
                    "Zuur koelt de kalk af tot ijs",
                ],
                0,
                "Calciumcarbonaat schuimt op met zuur en geeft koolstofdioxide vrij.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over de stocknotatie?",
        [
            ("Ze zet het oxidatiegetal van het metaal tussen haakjes.", J),
            ("Ze gebruikt een Romeins cijfer.", J),
            ("IJzer(III)chloride bevat ijzer met oxidatiegetal drie.", J),
            ("Ze telt het aantal zuurstofatomen.", F),
        ],
        "De stocknotatie toont het oxidatiegetal van het metaal.",
    ),
    tabel(
        "Waarvoor gebruiken we deze stof?",
        [
            ("ammoniak", "Kunstmest en schoonmaken"),
            ("fosforzuur", "Frisdrank van het colatype"),
            ("natriumwaterstofcarbonaat", "Bakpoeder"),
            ("methaan", "Verwarmen en koken"),
        ],
        "Ook bij naam genoemde stoffen hebben een toepassing die je moet kennen.",
        kolommen=["Kunstmest en schoonmaken", "Frisdrank van het colatype", "Bakpoeder", "Verwarmen en koken"],
    ),
    mk(
        "In een slecht verluchte badkamer brandt een geiser onvolledig. Waarom is dat levensgevaarlijk?",
        [
            "Er ontstaat CO, dat in je bloed bindt",
            "Er ontstaat een gas met een scherpe, prikkelende geur",
            "Er ontstaat een sterk zuur dat je huid aantast",
            "Er ontstaat een gas dat ontploft zodra het licht ziet",
        ],
        0,
        "Het gas is kleurloos en geurloos en ontstaat bij onvolledige verbranding.",
    ),
    sleep(
        "Koolstofdioxide heet ook [[koolzuurgas]]. Lost het op in water, dan ontstaat [[koolzuur]], zoals in spuitwater. Koolstofmonoxide heeft maar [[één]] zuurstofatoom.",
        ["kalk", "twee", "zoutzuur"],
        "Koolzuurgas en koolzuur zijn twee verschillende stoffen.",
    ),
    tabel(
        "Binair of ternair?",
        [
            ("zoutzuur", "Binair"),
            ("zwavelzuur", "Ternair"),
            ("calciumcarbonaat", "Ternair"),
            ("waterstofsulfide", "Binair"),
            ("salpeterzuur", "Ternair"),
        ],
        "Zwavelzuur en salpeterzuur bevatten ook zuurstof.",
        kolommen=["Binair", "Ternair"],
    ),
    keuze(
        "Giet je water bij ongebluste kalk, dan ontstaat [[*gebluste kalk|keukenzout|koolzuur]] en komt er veel warmte vrij.",
        "Calciumoxide wordt calciumhydroxide.",
    ),
    klik(
        "Klik op de structuurformule van het alkaan met tien waterstofatomen.",
        ALK.bestand, [BLOK["D"]],
        "Butaan C₄H₁₀: tel de H-atomen in D.",
    ),
    klik(
        "Klik op de formule van een binair zout.",
        KRT.bestand, [KAART["NaCl"]],
        "Natriumchloride bestaat uit twee elementen en is een zout.",
    ),
    mk(
        "Wat is het verschil tussen een brutoformule en een structuurformule?",
        [
            "De structuurformule toont ook de bindingen",
            "De brutoformule toont ook alle bindingen",
            "De structuurformule telt enkel de koolstofatomen",
            "De brutoformule geldt enkel voor zouten",
        ],
        0,
        "C₂H₆ is een brutoformule. De structuurformule tekent er de bindingen bij.",
    ),
    tabel(
        "Klopt dit over de alkanen?",
        [
            ("Ze bestaan enkel uit koolstof en waterstof.", J),
            ("Hun naam eindigt op aan.", J),
            ("Ammoniak is een alkaan.", F),
            ("Decaan heeft tien koolstofatomen.", J),
            ("Octaan heeft zes koolstofatomen.", F),
        ],
        "Oct staat voor acht. Ammoniak bevat stikstof.",
    ),
    keuze(
        "Water heet systematisch [[*diwaterstofoxide|waterstofperoxide|waterstofchloride]], maar niemand gebruikt die naam aan tafel.",
        "H₂O₂ is waterstofperoxide, een heel andere stof.",
    ),
    tabel(
        "Zit er zuurstof in dit ion?",
        [
            ("chloride-ion", F),
            ("chloraation", J),
            ("sulfide-ion", F),
            ("sulfaation", J),
        ],
        "Het chloraation en het sulfaation bevatten zuurstof, het chloride-ion en het sulfide-ion niet.",
    ),
    open_(
        "Je krijgt de formule CaCO₃. Leg uit tot welke stofklasse ze hoort, of ze binair of ternair is, en noem een plaats waar je deze stof vindt.",
        "CaCO₃ is een zout: calcium met het carbonaation CO₃²⁻. Er zitten drie elementen in (calcium, koolstof en zuurstof), dus het is ternair. Je vindt het in kalksteen, krijt, marmer, eierschalen of kalkaanslag.",
    ),
]
