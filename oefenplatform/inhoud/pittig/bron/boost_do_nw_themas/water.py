"""Stoffen in water, reacties en berekeningen — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# pH-schaal met vijf oplossingen ------------------------------------------
PH = Prent("ph-schaal", "Vijf oplossingen op de pH-schaal", "pH-schaal van 0 tot 14 met vijf oplossingen A tot E")
def X(p):
    return 80 + p * 60
for p in range(14):
    t = p / 13
    r, g, b = int(220 - 120 * t), int(80 + 100 * (1 - abs(t - 0.5) * 2)), int(60 + 160 * t)
    PH.rect(X(p), 300, 60, 60, f"rgb({r},{g},{b})", "none", 0, 0)
PH.rect(X(0), 300, 840, 60, "none", DONKER, 0, 2)
for p in range(15):
    PH.lijn(X(p), 360, X(p), 372, DONKER, 2)
    PH.tekst(X(p), 395, p, 18)
PH.tekst(X(7), 430, "pH", 20, vet=True)
OPL = {"A": 2, "B": 5, "C": 7, "D": 9, "E": 13}
Z = {}
for letter, p in OPL.items():
    PH.lijn(X(p), 210, X(p), 298, DONKER, 3)
    PH.letter(X(p), 190, letter)
    Z[letter] = Prent.zone(X(p) - 30, 160, 60, 140)

VRAGEN = [
    klik(
        "Klik op de oplossing die neutraal is.",
        PH.bestand, [Z["C"]],
        "Een neutrale oplossing heeft pH 7.",
    ),
    klik(
        "Klik op de oplossing die duizend keer zuurder is dan B.",
        PH.bestand, [Z["A"]],
        "Elke stap op de schaal is een factor tien. Van pH 5 naar pH 2 is drie stappen: tien maal tien maal tien.",
    ),
    klik(
        "Klik op de oplossing die het best past bij natriumhydroxide in water.",
        PH.bestand, [Z["E"]],
        "Natriumhydroxide geeft hydroxide-ionen vrij en maakt de oplossing sterk basisch.",
    ),
    klik(
        "Klik op de oplossing met de meeste waterstofionen.",
        PH.bestand, [Z["A"]],
        "Hoe lager de pH, hoe meer waterstofionen.",
    ),
    met_prent(PH.bestand, tabel(
        "Kijk naar de pH-schaal. Klopt dit?",
        [
            ("A en B zijn zuur.", J),
            ("D en E zijn basisch.", J),
            ("B is twee keer zuurder dan C.", F),
            ("Meng je A met een gepaste hoeveelheid E, dan schuift de pH naar 7.", J),
        ],
        "Van pH 7 naar pH 5 is twee stappen: honderd keer zuurder. Zuur en base neutraliseren elkaar.",
    )),
    tabel(
        "Dissociëren of ioniseren?",
        [
            ("NaCl lost op in water", "Dissociëren"),
            ("HCl-gas lost op in water", "Ioniseren"),
            ("NaOH lost op in water", "Dissociëren"),
        ],
        "Bij dissociatie komen bestaande ionen los, bij ionisatie valt een molecule uiteen in nieuwe ionen.",
        kolommen=["Dissociëren", "Ioniseren"],
    ),
    sorteer(
        "Elektrolyt of niet-elektrolyt?",
        ["Elektrolyt", "Niet-elektrolyt"],
        [
            ["keukenzout", "Elektrolyt"],
            ["zoutzuur", "Elektrolyt"],
            ["natriumhydroxide", "Elektrolyt"],
            ["suiker", "Niet-elektrolyt"],
            ["alcohol", "Niet-elektrolyt"],
        ],
        "Zouten, zuren en hydroxiden vormen ionen. Suiker en alcohol lossen op als hele moleculen.",
    ),
    tabel(
        "Polair of apolair?",
        [
            ("water", "Polair"),
            ("hexaan", "Apolair"),
            ("zuurstofgas", "Apolair"),
            ("tetrachloormethaan", "Apolair"),
        ],
        "Enkelvoudige stoffen en alkanen zijn typisch apolair.",
        kolommen=["Polair", "Apolair"],
    ),
    casus(
        "Je hebt vier bekers: een vast blokje keukenzout, een zoutoplossing, een suikeroplossing en gesmolten keukenzout. Je test met een lampje of ze stroom geleiden.",
        [
            tabel(
                "Brandt het lampje?",
                [
                    ("vast blokje keukenzout", F),
                    ("zoutoplossing", J),
                    ("suikeroplossing", F),
                    ("gesmolten keukenzout", J),
                ],
                "Stroom vraagt ladingen die kunnen bewegen: vrije ionen in een oplossing of een smelt.",
            ),
            keuze(
                "In de zoutoplossing zijn de ionen omringd door watermoleculen. Dat heet [[*hydratatie|ionisatie|neutralisatie]].",
                "De polaire watermoleculen houden de ionen gescheiden.",
            ),
        ],
    ),
    keuze(
        "De dissociatievergelijking van keukenzout is NaCl → [[*Na⁺ + Cl⁻|Na + Cl|Na⁻ + Cl⁺]].",
        "De ionen komen los met de lading die ze in het rooster al hadden.",
    ),
    mk(
        "Je schudt olie en water samen. Na een minuut liggen ze weer in twee lagen. Hoe komt dat?",
        [
            "Olie is apolair en water polair",
            "Olie is een elektrolyt die ioniseert",
            "Water is apolair en olie juist polair",
            "Olie dissocieert in water tot ionen",
        ],
        0,
        "Gelijk lost op in gelijk.",
    ),
    koppel(
        "Koppel elke reactie aan haar soort.",
        [
            ("zilverionen + chloride-ionen → witte vaste stof", "neerslagreactie"),
            ("H⁺ + OH⁻ → H₂O", "neutralisatie"),
            ("een atoom staat elektronen af aan een ander", "redoxreactie"),
        ],
        ["dissociatie"],
        "Dissociatie is het loskomen van ionen bij het oplossen, geen reactie tussen stoffen.",
    ),
    tabel(
        "Klopt dit over een redoxreactie?",
        [
            ("Oxidatie is elektronen afstaan.", J),
            ("De oxidator neemt elektronen op.", J),
            ("De reductor wordt zelf gereduceerd.", F),
            ("Het oxidatiegetal van minstens twee elementen verandert.", J),
            ("In ijzer als enkelvoudige stof is het oxidatiegetal min twee.", F),
        ],
        "De reductor staat elektronen af en wordt zelf geoxideerd. In een enkelvoudige stof is het oxidatiegetal nul.",
    ),
    tabel(
        "Klopt dit over een neerslag- en een neutralisatiereactie?",
        [
            ("Bij een neutralisatie ontstaan een zout en water.", J),
            ("Spectatorionen doen niet mee aan de reactie.", J),
            ("Twee oplossingen samengieten geeft altijd een neerslag.", F),
            ("Een oplosbaarheidstabel zegt of er een neerslag ontstaat.", J),
        ],
        "Heel vaak gebeurt er niets, omdat alle combinaties goed oplossen.",
    ),
    inv(
        "Hoeveel gram is 3 mol water? De molaire massa is 18 g/mol.",
        ["54"],
        "Massa is stofhoeveelheid maal molaire massa: 3 · 18 = 54 g.",
    ),
    inv(
        "Hoeveel mol is 90 g water? De molaire massa is 18 g/mol.",
        ["5"],
        "Deel de massa door de molaire massa: 90 : 18 = 5 mol.",
    ),
    inv(
        "In 0,25 liter oplossing zit 0,5 mol opgeloste stof. Wat is de molaire concentratie in mol per liter?",
        ["2"],
        "0,5 mol gedeeld door 0,25 liter is 2 mol per liter.",
    ),
    inv(
        "Je wil 2 liter oplossing van 0,1 mol per liter. Hoeveel mol stof los je op?",
        ["0,2", "0.2"],
        "Stofhoeveelheid is concentratie maal volume: 0,1 · 2 = 0,2 mol.",
    ),
    casus(
        "Bij de reactie 2 H₂ + O₂ → 2 H₂O laat je 4 mol waterstofgas volledig reageren.",
        [
            inv(
                "Hoeveel mol zuurstofgas heb je daarvoor nodig?",
                ["2"],
                "De coëfficiënten geven de verhouding in mol: 2 tegen 1. Voor 4 mol H₂ heb je 2 mol O₂ nodig.",
            ),
            inv(
                "Hoeveel mol water ontstaat er?",
                ["4"],
                "H₂ en H₂O staan in de verhouding 2 tegen 2. Uit 4 mol H₂ ontstaat 4 mol H₂O.",
            ),
            inv(
                "Hoeveel gram water is dat? De molaire massa is 18 g/mol.",
                ["72"],
                "4 · 18 = 72 g.",
            ),
        ],
    ),
    keuze(
        "Eén mol van een stof bevat altijd ongeveer [[*6 · 10²³|6 · 10³|18]] deeltjes.",
        "Dat getal heet het getal van Avogadro.",
    ),
    mk(
        "Hoe meet je de pH het nauwkeurigst?",
        [
            "Met een pH-meter",
            "Met een indicator",
            "Door te proeven",
            "Door de geur te ruiken",
        ],
        0,
        "Een pH-meter geeft een getal. Een indicator toont enkel een kleur bij een bepaald gebied.",
    ),
    klik(
        "Klik op de oplossing die honderd keer minder zuur is dan B.",
        PH.bestand, [Z["C"]],
        "Elke stap is een factor tien. Van pH 5 naar pH 7 is twee stappen: honderd keer minder zuur.",
    ),
    tabel(
        "Een indicator wordt rood in deze oplossing. Wat weet je?",
        [
            ("De oplossing is zuur.", J),
            ("Er zijn veel waterstofionen.", J),
            ("De pH ligt boven 7.", F),
        ],
        "Welke kleur bij welke pH hoort, lees je af in een tabel van de indicator.",
    ),
    sleep(
        "Bij een neutralisatie vormen een [[waterstofion]] en een [[hydroxide-ion]] samen water. De andere ionen blijven als [[spectatorionen]] in de oplossing.",
        ["neerslag", "reductor"],
        "Dat is de essentiële reactievergelijking van een neutralisatie.",
    ),
    keuze(
        "De molaire massa van een stof druk je uit in [[*gram per mol|mol per liter|kilogram]].",
        "Je leest ze af uit het periodiek systeem.",
    ),
    tabel(
        "Klopt dit over een aflopende reactie?",
        [
            ("Ze gaat door tot een van de stoffen op is.", J),
            ("De coëfficiënten geven de verhouding in mol.", J),
            ("De coëfficiënten geven de verhouding in gram.", F),
        ],
        "Wil je grammen, dan reken je met de molaire massa om.",
    ),
    open_(
        "Leg uit waarom keukenzout dissocieert en waterstofchloride ioniseert als ze in water oplossen.",
        "Keukenzout heeft een ionrooster: de ionen Na⁺ en Cl⁻ bestaan al en komen in water gewoon los van elkaar. Dat is dissociëren. Waterstofchloride bestaat als gas uit moleculen zonder ionen. In water valt de molecule uiteen in H⁺ en Cl⁻, ionen die er eerst niet waren. Dat is ioniseren.",
    ),
]
