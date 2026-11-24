"""Buffers en zuurbasetitraties — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Titratiecurve zwak zuur met sterke base ------------------------------------
TC = Prent("titratiecurve-azijnzuur", "Titratiecurve: 20 mL azijnzuur getitreerd met natronloog van 0,1 mol/L", "assenstelsel met het volume toegevoegde base horizontaal en de pH verticaal; een kromme die eerst traag stijgt, dan steil, dan weer vlak; twee gekleurde stroken voor indicatoren; punten A tot D")
X, Y = assen(TC, 0, 40, 0, 14, "V natronloog (mL)", "pH", 5, 2, links=130, rechts=880)
TC.rect(X(0), Y(6.2), X(40) - X(0), Y(4.4) - Y(6.2), "#f7d9b5", "none", 0, 0)
TC.rect(X(0), Y(10), X(40) - X(0), Y(8.2) - Y(10), "#f3c6d0", "none", 0, 0)
TC.tekst(X(39.5), Y(5.3) + 6, "omslag methylrood", 15, "end")
TC.tekst(X(39.5), Y(9.1) + 6, "omslag fenolftaleïne", 15, "end")


def _ph(v):
    ca, va, cb, pk = 0.1, 20, 0.1, 4.75
    nz, nb = ca * va, cb * v
    vt = va + v
    if v < 0.05:
        ka = 10 ** -pk
        return -math.log10(math.sqrt(ka * ca))
    if nb < nz - 1e-6:
        return pk + math.log10(nb / (nz - nb))
    if abs(nb - nz) < 1e-6:
        cb2 = nz / vt
        kb = 1e-14 / 10 ** -pk
        return 14 + math.log10(math.sqrt(kb * cb2))
    oh = (nb - nz) / vt
    return 14 + math.log10(oh)


pts = []
for i in range(0, 401):
    v = i / 10
    if abs(v - 20) < 0.05:
        v = 20
    pts.append((X(v), Y(min(_ph(v), 13.2))))
TC.pad("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts), "none", BLAUW, 4)
PT = {"A": 0, "B": 10, "C": 20, "D": 35}
for k, v in PT.items():
    TC.cirkel(X(v), Y(_ph(v)), 7, GEEL, DONKER, 2)
    TC.letter(X(v) + (32 if k == "A" else -32), Y(_ph(v)) - 26, k)
ZTC = {k: [Prent.rond(X(v), Y(_ph(v)), 22), Prent.rond(X(v) + (32 if k == "A" else -32), Y(_ph(v)) - 26, 22)] for k, v in PT.items()}

# Opstelling titratie --------------------------------------------------------
OP = Prent("opstelling-titratie", "Opstelling voor een titratie", "een statief met een buret, onderaan een kraantje, en daaronder een erlenmeyer; letters A tot D")
OP.rect(180, 560, 260, 20, "#d9d4c4", DONKER, 4, 2)
OP.rect(200, 70, 14, 490, "#d9d4c4", DONKER, 4, 2)
OP.rect(214, 160, 236, 12, "#d9d4c4", DONKER, 3, 2)
OP.rect(450, 80, 36, 330, "#ffffff", DONKER, 6, 2)
OP.rect(452, 150, 32, 258, "#dcebf7", "none", 0, 0)
for j in range(0, 12):
    y = 100 + j * 25
    OP.lijn(450, y, 466, y, DONKER, 1)
OP.pad("M 452 150 Q 468 162 484 150", "none", DONKER, 2)
OP.pad("M 450 410 L 462 450 L 474 450 L 486 410 Z", "#ffffff", DONKER, 2)
OP.rect(440, 425, 56, 12, "#7aa35c", DONKER, 3, 2)
OP.lijn(468, 450, 468, 480, DONKER, 2)
OP.pad("M 440 480 L 440 500 L 380 560 L 556 560 L 496 500 L 496 480 Z", "#f3c6d0", DONKER, 3)
LOP = {"A": (560, 280), "B": (560, 155), "C": (560, 430), "D": (620, 535)}
for k, (x, y) in LOP.items():
    OP.letter(x, y, k)
OP.lijn(538, 280, 488, 280, GRIJS, 1)
OP.lijn(538, 155, 486, 155, GRIJS, 1)
OP.lijn(538, 430, 498, 430, GRIJS, 1)
OP.lijn(598, 535, 530, 535, GRIJS, 1)
ZOP = {"A": [Prent.zone(448, 80, 40, 330), Prent.rond(*LOP["A"], 22)],
       "B": [Prent.zone(448, 142, 40, 20), Prent.rond(*LOP["B"], 22)],
       "C": [Prent.zone(436, 420, 64, 24), Prent.rond(*LOP["C"], 22)],
       "D": [Prent.zone(380, 480, 176, 80), Prent.rond(*LOP["D"], 22)]}

VRAGEN = [
    klik(
        "Klik op het equivalentiepunt.",
        TC.bestand, ZTC["C"],
        "Midden in de steile sprong: 20 mL base voor 20 mL zuur van dezelfde concentratie.",
    ),
    klik(
        "Klik op het punt waar de pH gelijk is aan de pKz van azijnzuur.",
        TC.bestand, ZTC["B"],
        "Halverwege het equivalentiepunt zijn zuur en geconjugeerde base even groot: pH = pKz.",
    ),
    met_prent(TC.bestand, tabel(
        "Wat zit er in de erlenmeyer op dit punt, naast water en Na⁺?",
        [
            ("A", "Vooral azijnzuur"),
            ("B", "Een buffer"),
            ("C", "Vooral acetaat"),
            ("D", "Acetaat en OH⁻"),
        ],
        "Na het equivalentiepunt is er overmaat base.",
        kolommen=["Vooral azijnzuur", "Een buffer", "Vooral acetaat", "Acetaat en OH⁻"],
    )),
    met_prent(TC.bestand, mk(
        "Welke indicator past bij deze titratie?",
        [
            "Fenolftaleïne: haar omslag valt in de sprong",
            "Methylrood: haar omslag valt in de sprong",
            "Allebei even goed, het is een sterk zuur",
            "Geen van beide, een titratie kan niet zonder pH-meter",
        ],
        0,
        "Het equivalentiepunt ligt boven pH 7. Methylrood zou al omslaan in het bufferstuk.",
    )),
    met_prent(TC.bestand, inv(
        "Lees de pH af in punt B. Rond af op een geheel getal.",
        ["5", "pH 5"],
        "Ongeveer 4,75, de pKz van azijnzuur: afgerond 5.",
    )),
    klik(
        "Klik op het deel van de opstelling dat je vooraf spoelt met titrans.",
        OP.bestand, ZOP["A"],
        "De buret: water zou het titrans verdunnen.",
    ),
    klik(
        "Klik op de plaats waar je het volume afleest.",
        OP.bestand, ZOP["B"],
        "Bij de onderkant van de meniscus, op ooghoogte.",
    ),
    met_prent(OP.bestand, tabel(
        "Mag dit deel nat zijn van gedestilleerd water voor je begint?",
        [
            ("A", "Nee"),
            ("D", "Ja"),
        ] + [("de pipet voor het zuur", "Nee")],
        "Water in de erlenmeyer verandert het aantal mol zuur niet; water in buret of pipet verdunt de oplossing.",
        kolommen=["Ja", "Nee"],
    )),
    tabel(
        "Is dit mengsel een buffer?",
        [
            ("azijnzuur met natriumacetaat", "Ja"),
            ("ammoniak met ammoniumchloride", "Ja"),
            ("zoutzuur met natriumchloride", "Nee"),
            ("koolzuur met natriumwaterstofcarbonaat", "Ja"),
        ],
        "Een buffer is een zwak zuur met zijn geconjugeerde base, of een zwakke base met haar zuur.",
        kolommen=["Ja", "Nee"],
    ),
    tabel(
        "Welk deeltje van de azijnzuurbuffer vangt dit op?",
        [
            ("een beetje zoutzuur", "CH₃COO⁻"),
            ("een beetje natronloog", "CH₃COOH"),
        ] + [("extra H₃O⁺ uit een zure regenbui", "CH₃COO⁻")],
        "De base van het paar neemt H₃O⁺ weg, het zuur neemt OH⁻ weg.",
        kolommen=["CH₃COOH", "CH₃COO⁻"],
    ),
    inv(
        "Je wil een buffer rond pH 9,2. Welke pKz moet het zuur van je paar ongeveer hebben?",
        ["9,2", "9.2", "9"],
        "Een buffer werkt het best rond zijn pKz.",
    ),
    mk(
        "Een buffer heeft pKz 4,8. In welk gebied werkt hij goed?",
        ["Tussen pH 3,8 en 5,8", "Tussen pH 1 en 4,8", "Tussen pH 4,8 en 9,2", "Bij elke pH tussen 0 en 14"],
        0,
        "Ongeveer één eenheid rond de pKz.",
    ),
    casus(
        "Je titreert 25 mL zoutzuur met natronloog van 0,1 mol/L. Het equivalentiepunt ligt bij 20 mL.",
        [
            inv(
                "Hoeveel mol NaOH is er toegevoegd tot het equivalentiepunt?",
                ["0,002", "0.002", "2·10⁻³", "0,002 mol"],
                "0,1 × 0,020 = 0,002 mol.",
            ),
            inv(
                "Wat is de concentratie van het zoutzuur in mol/L?",
                ["0,08", "0.08", "0,08 mol/L"],
                "0,002 mol / 0,025 L = 0,08 mol/L.",
            ),
            keuze(
                "Het equivalentiepunt ligt bij pH [[*7|onder 7|boven 7]].",
                "Sterk zuur en sterke base: er blijft een neutraal zout over.",
            ),
        ],
    ),
    tabel(
        "Wordt het gemeten volume titrans hierdoor te groot of te klein?",
        [
            ("de buret is met water gespoeld, niet met titrans", "Te groot"),
            ("je titreert voorbij de kleuromslag", "Te groot"),
            ("er hangt een luchtbel onder het kraantje die verdwijnt", "Te groot"),
            ("de pipet met zuur was nog nat van water", "Te klein"),
        ],
        "Verdund titrans vraagt meer volume; verdund zuur in de pipet bevat minder mol.",
        kolommen=["Te groot", "Te klein"],
    ),
    volgorde(
        "Zet de stappen van een titratie in de goede volgorde.",
        [
            "De buret spoelen en vullen met titrans",
            "Met een pipet het zuur in de erlenmeyer brengen",
            "Een paar druppels indicator toevoegen",
            "Titreren tot de kleur blijvend omslaat",
            "Het volume aflezen en de concentratie berekenen",
        ],
        "Spoelen en vullen eerst, rekenen op het einde.",
    ),
    tabel(
        "Ligt het equivalentiepunt bij pH 7, erboven of eronder?",
        [
            ("sterk zuur met sterke base", "Bij 7"),
            ("zwak zuur met sterke base", "Boven 7"),
            ("zwakke base met sterk zuur", "Onder 7"),
        ],
        "Wat overblijft, is de geconjugeerde base of het geconjugeerde zuur van het zwakke deeltje.",
        kolommen=["Onder 7", "Bij 7", "Boven 7"],
    ),
    mk(
        "Je verdunt een buffer met evenveel water. Wat gebeurt er?",
        [
            "pH bijna gelijk, capaciteit lager",
            "De pH stijgt meteen met één volle eenheid",
            "De pH daalt meteen met één volle eenheid",
            "De buffer werkt daarna helemaal niet meer",
        ],
        0,
        "De verhouding zuur/base blijft gelijk; er zijn wel minder deeltjes om iets op te vangen.",
    ),
    sleep(
        "Bloed wordt gebufferd door [[koolzuur]] en het [[waterstofcarbonaation]]. Zo blijft de pH rond [[7,4]].",
        ["zoutzuur", "chloride-ion", "5,6"],
        "Door sneller te ademen verlies je CO₂ en verschuift het evenwicht.",
    ),
    inv(
        "Je titreert 10 mL zwavelzuur (tweewaardig) met 0,1 mol/L NaOH en verbruikt 20 mL. Wat is de concentratie van het zwavelzuur in mol/L?",
        ["0,1", "0.1", "0,1 mol/L"],
        "0,002 mol NaOH reageert met 0,001 mol H₂SO₄: 0,001 / 0,010 = 0,1 mol/L.",
    ),
    mk(
        "Je mengt 0,2 mol azijnzuur met 0,1 mol NaOH. Wat krijg je?",
        [
            "Een buffer met evenveel zuur als base",
            "Een neutrale oplossing van natriumacetaat",
            "Een oplossing met overmaat sterke base",
            "Zuiver azijnzuur zonder acetaat",
        ],
        0,
        "0,1 mol zuur reageert tot acetaat: 0,1 mol zuur en 0,1 mol acetaat blijven.",
    ),
    tabel(
        "Klopt dit over de buffercapaciteit?",
        [
            ("Ze is groter bij hogere concentraties van zuur en base.", J),
            ("Ze is het grootst als zuur en base even veel aanwezig zijn.", J),
            ("Ze is onbeperkt.", F),
        ],
        "Is een van de twee op, dan werkt de buffer niet meer.",
    ),
    inv(
        "Hoeveel mL natronloog heb je in de titratiecurve van azijnzuur toegevoegd in punt B?",
        ["10", "10 mL"],
        "De helft van de 20 mL tot het equivalentiepunt.",
    ),
    koppel(
        "Koppel elk stuk glaswerk aan zijn taak bij een titratie.",
        [
            ("buret", "het titrans druppelsgewijs toevoegen"),
            ("pipet", "het zuur nauwkeurig afmeten"),
            ("erlenmeyer", "de oplossing die je titreert"),
            ("maatkolf", "het titrans op een juiste concentratie maken"),
        ],
        ["de pH nauwkeurig meten"],
        "Een pH-meter is geen glaswerk.",
    ),
    mk(
        "Waarom doe je eerst een snelle proeftitratie?",
        [
            "Om te weten rond welk volume de sprong ligt",
            "Om de buret te spoelen met de oplossing",
            "Om de indicator op te warmen voor het echte werk",
            "Om het equivalentiepunt naar pH 7 te brengen",
        ],
        0,
        "Daarna kan je bij de echte titratie rond dat volume traag druppelen.",
    ),
    tabel(
        "Klopt dit over de titratie van een verdunder zuur?",
        [
            ("De pH-sprong wordt kleiner.", J),
            ("Het equivalentiepunt vraagt minder titrans.", J),
            ("De pH bij de start ligt lager.", F),
        ],
        "Verdunder zuur start bij een hogere pH en heeft minder mol om te neutraliseren.",
    ),
    keuze(
        "Zonder indicator kan je het equivalentiepunt ook vinden met een [[*pH-meter|thermometer|weegschaal]].",
        "Je zet de pH uit tegen het volume en zoekt de steile sprong.",
    ),
    mk(
        "Waarom buffert zoutzuur met natriumchloride niet?",
        [
            "Cl⁻ is een te zwakke base",
            "Natriumchloride lost niet op in zoutzuur",
            "Zoutzuur heeft geen geconjugeerde base",
            "Het mengsel heeft een pH van precies 7",
        ],
        0,
        "Een buffer heeft een zwak zuur en een base die echt protonen opneemt nodig.",
    ),
    open_(
        "Leg uit waarom de titratiecurve rond punt B bijna vlak loopt.",
        "In dat stuk zit er zowel azijnzuur als acetaat in de erlenmeyer: een buffer. Elke toegevoegde OH⁻ wordt door het azijnzuur weggenomen en omgezet in acetaat. De verhouding tussen zuur en base verandert maar langzaam, dus de pH stijgt maar weinig, tot het zuur bijna op is.",
    ),
]
