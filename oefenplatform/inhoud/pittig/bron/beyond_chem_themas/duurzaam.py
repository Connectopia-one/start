"""Duurzame chemie en de circulaire economie — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Ladder van Lansink (zonder woorden) ---------------------------------------
LL = Prent("ladder-lansink", "De ladder van Lansink, zonder de namen van de treden", "een ladder met zes treden, van boven naar onder A tot F; bovenaan staat 'beste keuze', onderaan 'slechtste keuze'")
LL.lijn(380, 70, 380, 560, DONKER, 6)
LL.lijn(620, 70, 620, 560, DONKER, 6)
for i, k in enumerate("ABCDEF"):
    y = 110 + i * 85
    kl = ["#cde8c4", "#d9edcf", "#e6f1d8", "#f4eccd", "#f6dcc4", "#f3c6c0"][i]
    LL.rect(380, y - 18, 240, 36, kl, DONKER, 6, 2)
    LL.letter(500, y, k)
LL.tekst(660, 115, "beste keuze", 18, "start", vet=True, kleur=GROEN)
LL.tekst(660, 540, "slechtste keuze", 18, "start", vet=True, kleur=ROOD)
ZLL = {k: [Prent.zone(380, 92 + i * 85, 240, 36)] for i, k in enumerate("ABCDEF")}

# Drie economieën ------------------------------------------------------------
EC = Prent("drie-economieen", "Drie manieren om met grondstoffen om te gaan", "drie schema's: een rechte lijn van grondstof naar afval; een lijn met een kleine terugkoppeling en toch afval op het einde; een gesloten kring; letters P, Q en R")


def _vak(p, x, y, t, kl="#ffffff"):
    p.rect(x - 70, y - 22, 140, 44, kl, DONKER, 10, 2)
    p.tekst(x, y + 6, t, 16, vet=True)


# P: lineair
for i, t in enumerate(["grondstof", "product", "gebruik", "afval"]):
    _vak(EC, 130 + i * 200, 120, t, "#f3c6c0" if t == "afval" else "#ffffff")
    if i:
        EC.pijl(130 + (i - 1) * 200 + 72, 120, 130 + i * 200 - 72, 120, DONKER, 2)
EC.letter(60, 60, "P")
# Q: keten
for i, t in enumerate(["grondstof", "product", "gebruik", "restafval"]):
    _vak(EC, 130 + i * 200, 300, t, "#f3c6c0" if t == "restafval" else "#ffffff")
    if i:
        EC.pijl(130 + (i - 1) * 200 + 72, 300, 130 + i * 200 - 72, 300, DONKER, 2)
EC.pad("M 530 322 Q 430 390 330 322", "none", GROEN, 3)
EC.pijl(345, 333, 332, 323, GROEN, 3)
EC.tekst(430, 385, "deels hergebruik", 15, kleur=GROEN)
EC.letter(60, 240, "Q")
# R: circulair
for i, t in enumerate(["grondstof", "product", "gebruik"]):
    _vak(EC, 130 + i * 200, 480, t)
    if i:
        EC.pijl(130 + (i - 1) * 200 + 72, 480, 130 + i * 200 - 72, 480, DONKER, 2)
EC.pad("M 530 502 L 530 560 L 130 560 L 130 512", "none", GROEN, 3)
EC.pijl(130, 530, 130, 504, GROEN, 3)
EC.tekst(330, 585, "alles wordt opnieuw grondstof", 15, kleur=GROEN)
EC.letter(60, 420, "R")
ZEC = {"P": [Prent.zone(50, 90, 860, 60), Prent.rond(60, 60, 22)],
       "Q": [Prent.zone(50, 270, 860, 130), Prent.rond(60, 240, 22)],
       "R": [Prent.zone(50, 450, 560, 140), Prent.rond(60, 420, 22)]}

VRAGEN = [
    klik(
        "Klik op de trede van storten.",
        LL.bestand, ZLL["F"],
        "Storten staat onderaan, onder verbranden.",
    ),
    klik(
        "Klik op de trede van hergebruik.",
        LL.bestand, ZLL["B"],
        "Net onder preventie: het voorwerp zelf blijft heel.",
    ),
    met_prent(LL.bestand, tabel(
        "Welke trede is dit?",
        [
            ("A", "Preventie"),
            ("C", "Recyclage"),
            ("D", "Verbranden met energiewinning"),
            ("E", "Verbranden"),
        ],
        "Van boven naar onder: preventie, hergebruik, recyclage, verbranden met energiewinning, verbranden, storten.",
        kolommen=["Preventie", "Recyclage", "Verbranden met energiewinning", "Verbranden"],
    )),
    klik(
        "Klik op het schema van wieg tot wieg.",
        EC.bestand, ZEC["R"],
        "In een circulaire economie bestaat afval niet meer.",
    ),
    met_prent(EC.bestand, tabel(
        "Welke economie stelt dit schema voor?",
        [
            ("P", "Lineair"),
            ("Q", "Keten"),
            ("R", "Circulair"),
        ],
        "De keteneconomie hergebruikt veel, maar houdt toch nog afval over.",
        kolommen=["Lineair", "Keten", "Circulair"],
    )),
    met_prent(EC.bestand, keuze(
        "Schema P wordt ook van [[*wieg tot graf|wieg tot wieg]] genoemd.",
        "De grondstof eindigt als afval dat verdwijnt.",
    )),
    tabel(
        "Op welke trede van de ladder van Lansink hoort dit?",
        [
            ("een drinkbus in plaats van wegwerpflesjes", "Preventie"),
            ("een glazen fles uitspoelen en opnieuw vullen", "Hergebruik"),
            ("petflessen smelten tot nieuwe flessen", "Recyclage"),
            ("afval op een stortplaats", "Storten"),
        ],
        "Hoe hoger op de ladder, hoe minder grondstof en energie verloren gaan.",
        kolommen=["Preventie", "Hergebruik", "Recyclage", "Storten"],
    ),
    tabel(
        "Welke kleur waterstof is dit?",
        [
            ("elektrolyse met stroom uit zon of wind", "Groen"),
            ("uit aardgas, CO₂ gaat de lucht in", "Grijs"),
            ("uit aardgas, CO₂ wordt opgevangen", "Blauw"),
        ],
        "De kleur zegt hoe de waterstof gemaakt is, niet wat het is.",
        kolommen=["Groen", "Grijs", "Blauw"],
    ),
    tabel(
        "Is dit wit, grijs of zwart water?",
        [
            ("water uit de kraan om te drinken", "Wit"),
            ("water uit de douche en de wasmachine", "Grijs"),
            ("water uit het toilet", "Zwart"),
        ],
        "Grijs water kan je na een eenvoudige zuivering gebruiken om het toilet te spoelen.",
        kolommen=["Wit", "Grijs", "Zwart"],
    ),
    casus(
        "Een fabrikant maakt ethanol op twee manieren: (1) etheen + water → ethanol, (2) broomethaan + NaOH → ethanol + NaBr. M(ethanol) = 46, M(etheen) = 28, M(H₂O) = 18, M(broomethaan) = 109, M(NaOH) = 40 g/mol.",
        [
            inv(
                "Wat is de atoomeconomie van manier 1, in procent?",
                ["100", "100 %", "100%"],
                "28 + 18 = 46: alles komt in het product.",
            ),
            inv(
                "Wat is de atoomeconomie van manier 2, in procent? Rond af op een geheel getal.",
                ["31", "31 %", "31%"],
                "46 / (109 + 40) = 46 / 149 ≈ 0,31.",
            ),
            keuze(
                "Vanuit de groene chemie is manier [[*1|2]] de betere keuze.",
                "Een additie heeft geen bijproduct.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over biogebaseerd en biodegradeerbaar?",
        [
            ("Biogebaseerd zegt iets over de grondstof.", J),
            ("Biodegradeerbaar zegt iets over de afbraak.", J),
            ("Een biogebaseerde kunststof is altijd biodegradeerbaar.", F),
            ("Composteerbaar is strenger dan biodegradeerbaar.", J),
        ],
        "De twee woorden gaan over iets anders: begin of einde van het leven van een product.",
    ),
    mk(
        "Een petfles wordt vulling voor een jas, die daarna niet meer te recycleren is. Hoe heet dat?",
        ["Downcycling", "Preventie", "Hergebruik", "Composteren"],
        0,
        "De kwaliteit van het materiaal zakt.",
    ),
    tabel(
        "Is dit greenwashing?",
        [
            ("een groen blaadje op de verpakking zonder enige uitleg", "Ja"),
            ("het woord natuurlijk zonder bewijs", "Ja"),
            ("een officieel label met controle door een derde", "Nee"),
        ],
        "Greenwashing stelt iets groener voor dan het is.",
        kolommen=["Ja", "Nee"],
    ),
    koppel(
        "Koppel elke P aan wat ze betekent.",
        [
            ("people", "mensen"),
            ("planet", "de aarde"),
            ("prosperity", "welvaart"),
            ("peace", "vrede"),
            ("partnership", "samenwerking"),
        ],
        ["productie"],
        "De vijf P's van de duurzame ontwikkelingsdoelen.",
    ),
    mk(
        "Waarom staat preventie bovenaan de ladder?",
        [
            "Wat niet ontstaat, hoeft niet verwerkt",
            "Preventie levert de meeste energie op",
            "Preventie is de goedkoopste verbranding",
            "Na preventie kan je alles storten",
        ],
        0,
        "Elke andere trede kost nog energie of grondstof.",
    ),
    inv(
        "De duurzame ontwikkelingsdoelen werden afgesproken in 2015. Tegen welk jaar wil men ze halen?",
        ["2030"],
        "Zeventien doelen, met 2030 als einddatum.",
    ),
    sorteer(
        "Is dit een primaire of een secundaire microplastic?",
        ["Primair", "Secundair"],
        [
            ("korrels in een scrubcrème", "Primair"),
            ("pellets als grondstof voor de industrie", "Primair"),
            ("stukjes van een afgebroken plastic zak", "Secundair"),
            ("vezels uit fleece in het waswater", "Secundair"),
        ],
        "Primair is al klein gemaakt, secundair ontstaat door afbraak van iets groters.",
    ),
    tabel(
        "Klopt dit over de atoomeconomie?",
        [
            ("Een additie zonder bijproduct haalt 100 %.", J),
            ("Ze volgt uit de reactievergelijking alleen.", J),
            ("Ze is hetzelfde als het rendement.", F),
        ],
        "Het rendement meet hoeveel je in de praktijk echt uithaalt.",
    ),
    sleep(
        "Een microplastic is kleiner dan [[vijf millimeter]]. Groene waterstof maakt men met [[elektrolyse]]. Een katalysator past in de groene chemie omdat hij [[niet opgebruikt]] wordt.",
        ["vijf centimeter", "verbranding", "snel verbruikt"],
        "Groene chemie zoekt minder afval, minder energie en veiligere stoffen.",
    ),
    mk(
        "Wat maakt een product geschikt voor een circulaire economie?",
        [
            "De onderdelen kan je weer scheiden",
            "Het is uit zoveel mogelijk materialen gelijmd",
            "Het gaat zo kort mogelijk mee",
            "Het wordt na gebruik meteen gestort",
        ],
        0,
        "Uit elkaar halen maakt hergebruik en recyclage mogelijk.",
    ),
    mk(
        "Waarom staat verbranden met energiewinning hoger op de ladder dan storten?",
        [
            "De energie in het afval wordt nog gebruikt",
            "Er ontstaat bij verbranden helemaal geen CO₂",
            "Verbranden maakt nieuwe grondstoffen",
            "Gestort afval verdwijnt vanzelf",
        ],
        0,
        "Bij storten gaat alles verloren en blijft het afval liggen.",
    ),
    tabel(
        "Is dit een kenmerk van een lineaire of van een circulaire economie?",
        [
            ("nemen, maken, weggooien", "Lineair"),
            ("afval wordt grondstof", "Circulair"),
            ("producten ontworpen om te herstellen", "Circulair"),
            ("van wieg tot graf", "Lineair"),
        ],
        "Circulair: de kring is gesloten.",
        kolommen=["Lineair", "Circulair"],
    ),
    inv(
        "Bij een reactie A + B → C + D weegt het gewenste product C 60 g/mol en het bijproduct D 40 g/mol. Wat is de atoomeconomie in procent?",
        ["60", "60 %", "60%"],
        "60 / (60 + 40) = 0,60.",
    ),
    keuze(
        "Een kunststof die je in de tuincompost kan gooien, moet [[*composteerbaar|biogebaseerd|recycleerbaar]] zijn.",
        "Composteerbaar betekent afbraak binnen een vaste tijd en onder vaste omstandigheden.",
    ),
    tabel(
        "Hoort dit bij de groene chemie?",
        [
            ("een katalysator gebruiken", "Ja"),
            ("een reactie met een hoge atoomeconomie kiezen", "Ja"),
            ("zoveel mogelijk oplosmiddel gebruiken", "Nee"),
            ("hernieuwbare grondstoffen gebruiken", "Ja"),
        ],
        "Groene chemie zoekt minder afval, minder energie en veiligere stoffen.",
        kolommen=["Ja", "Nee"],
    ),
    mk(
        "Waarom is blauwe waterstof beter voor het klimaat dan grijze?",
        [
            "De CO₂ wordt opgevangen",
            "Ze komt uit zonne-energie",
            "Ze bevat geen waterstofatomen",
            "Ze is een andere molecule dan H₂",
        ],
        0,
        "Beide komen uit aardgas, maar bij blauwe komt de CO₂ niet in de lucht.",
    ),
    volgorde(
        "Zet de waterstofkleuren van meest naar minst CO₂-uitstoot bij de productie.",
        ["grijs", "blauw", "groen"],
        "Grijs stoot CO₂ uit, blauw vangt het op, groen gebruikt hernieuwbare stroom.",
    ),
    open_(
        "Leg uit waarom groene en grijze waterstof dezelfde stof zijn, maar toch niet even duurzaam.",
        "Het is in beide gevallen dezelfde molecule H₂ met dezelfde eigenschappen. Het verschil zit in hoe ze gemaakt wordt: groene waterstof komt uit elektrolyse van water met stroom uit zon of wind, grijze uit aardgas waarbij CO₂ in de lucht komt. De kleur zegt dus iets over de grondstof en de energie, en daarmee over de uitstoot.",
    ),
]
