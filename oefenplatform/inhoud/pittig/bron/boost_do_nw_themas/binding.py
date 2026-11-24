"""Chemische bindingen en roosters — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Vier roosters, zonder namen --------------------------------------------
ROO = Prent("vier-roosters", "Vier roosters, schematisch", "ionrooster, metaalrooster, molecuulrooster en atoomrooster")
VAKJE = {}
def _kader(letter, x, y):
    ROO.rect(x, y, 420, 240, "#ffffff", DONKER, 12)
    ROO.letter(x + 24, y + 24, letter)
    VAKJE[letter] = Prent.zone(x, y, 420, 240)
# A: ionrooster
_kader("A", 60, 70)
for i in range(5):
    for j in range(3):
        x, y = 130 + i * 70, 130 + j * 60
        plus = (i + j) % 2 == 0
        ROO.cirkel(x, y, 22 if plus else 28, "#fbe7c6" if plus else "#d6e6f2")
        ROO.tekst(x, y + 7, "+" if plus else "−", 22, vet=True)
# B: metaalrooster
_kader("B", 520, 70)
for i in range(5):
    for j in range(3):
        x, y = 590 + i * 70, 130 + j * 60
        ROO.cirkel(x, y, 22, "#fbe7c6")
        ROO.tekst(x, y + 7, "+", 22, vet=True)
for (x, y) in [(625, 112), (695, 160), (765, 112), (835, 160), (625, 220), (695, 205), (765, 220), (835, 100), (660, 245), (800, 250), (730, 140)]:
    ROO.cirkel(x, y, 5, BLAUW, BLAUW, 1)
# C: molecuulrooster
_kader("C", 60, 350)
for (x, y) in [(140, 420), (260, 410), (380, 430), (170, 520), (300, 500), (420, 520)]:
    ROO.cirkel(x, y, 20, ROOD)
    ROO.cirkel(x + 24, y - 14, 12, "#ffffff")
    ROO.cirkel(x + 24, y + 14, 12, "#ffffff")
# D: atoomrooster
_kader("D", 520, 350)
pts = [(580 + i * 60 + (30 if j % 2 else 0), 410 + j * 55) for i in range(6) for j in range(3)]
pts = [(x, y) for x, y in pts if x < 920]
for a in pts:
    for b in pts:
        if a < b and ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 < 70:
            ROO.lijn(a[0], a[1], b[0], b[1], DONKER, 3)
for x, y in pts:
    ROO.cirkel(x, y, 13, GRIJS)

# Lewisstructuur van water -----------------------------------------------
LEW = Prent("lewis-water", "Lewisstructuur van een watermolecule", "O in het midden met twee bindende paren naar H en twee vrije elektronenparen")
LEW.tekst(500, 360, "O", 70, vet=True)
LEW.tekst(300, 360, "H", 70, vet=True)
LEW.tekst(700, 360, "H", 70, vet=True)
LEW.lijn(345, 336, 455, 336, DONKER, 6)
LEW.lijn(545, 336, 655, 336, DONKER, 6)
LEW.lijn(470, 250, 530, 250, DONKER, 6)
LEW.lijn(470, 400, 530, 400, DONKER, 6)
Z_VRIJ = [Prent.zone(455, 225, 90, 50), Prent.zone(455, 375, 90, 50)]
Z_BINDEND = [Prent.zone(345, 310, 110, 50), Prent.zone(545, 310, 110, 50)]

VRAGEN = [
    klik(
        "Klik op het rooster van keukenzout.",
        ROO.bestand, [VAKJE["A"]],
        "Een ionrooster bestaat uit positieve en negatieve ionen die elkaar in alle richtingen aantrekken.",
    ),
    klik(
        "Klik op het rooster dat ook in vaste toestand elektriciteit geleidt.",
        ROO.bestand, [VAKJE["B"]],
        "Een metaalrooster heeft vrije elektronen: de elektronenzee.",
    ),
    klik(
        "Klik op het rooster van een stof met een laag smelt- en kookpunt.",
        ROO.bestand, [VAKJE["C"]],
        "In een molecuulrooster is de aantrekking tussen de moleculen zwak.",
    ),
    klik(
        "Klik op het rooster dat bij diamant past.",
        ROO.bestand, [VAKJE["D"]],
        "Een atoomrooster is één groot netwerk van atoombindingen. Daarom is diamant zo hard.",
    ),
    met_prent(ROO.bestand, tabel(
        "Kijk naar de vier roosters. Klopt dit?",
        [
            ("Rooster A is breekbaar.", J),
            ("Rooster B kan je plooien.", J),
            ("In rooster C zijn de bindingen binnen een molecule zwak.", F),
            ("In rooster D zitten alle elektronen vast in bindingen.", J),
        ],
        "Binnen de molecule zijn de bindingen sterk, tussen de moleculen zwak.",
    )),
    klik(
        "Klik op een vrij elektronenpaar.",
        LEW.bestand, Z_VRIJ,
        "Een vrij paar staat als streepje bij één atoom, niet tussen twee atomen.",
    ),
    klik(
        "Klik op een bindend elektronenpaar.",
        LEW.bestand, Z_BINDEND,
        "Een streepje tussen twee atomen is een gedeeld paar.",
    ),
    met_prent(LEW.bestand, tabel(
        "Kijk naar de Lewisstructuur. Klopt dit?",
        [
            ("Zuurstof deelt twee elektronenparen.", J),
            ("Zuurstof heeft twee vrije elektronenparen.", J),
            ("Er is een dubbele binding tussen O en H.", F),
            ("Rond zuurstof staan in totaal acht elektronen.", J),
        ],
        "Twee bindende en twee vrije paren: acht elektronen, een volle schil.",
    )),
    tabel(
        "Welk bindingstype verwacht je?",
        [
            ("natrium en chloor", "Ionbinding"),
            ("waterstof en zuurstof", "Atoombinding"),
            ("koper en zink", "Metaalbinding"),
            ("magnesium en zuurstof", "Ionbinding"),
            ("koolstof en waterstof", "Atoombinding"),
        ],
        "Metaal met niet-metaal: ionbinding. Twee niet-metalen: atoombinding. Twee metalen: metaalbinding.",
        kolommen=["Ionbinding", "Atoombinding", "Metaalbinding"],
    ),
    casus(
        "Een onbekende stof smelt pas bij 801 °C. Laat je ze vallen, dan splijt het kristal. Als vast blokje geleidt ze geen stroom, opgelost in water wel.",
        [
            mk(
                "Welk rooster heeft deze stof?",
                ["Een ionrooster", "Een metaalrooster", "Een molecuulrooster", "Een atoomrooster"],
                0,
                "Hoog smeltpunt, breekbaar en geleiding pas na oplossen: een zout.",
            ),
            mk(
                "Waarom geleidt ze opgelost wel en vast niet?",
                [
                    "In water kunnen de ionen bewegen",
                    "In water ontstaan er vrije elektronen",
                    "Water zelf is een goede geleider",
                    "Het kristal is te koud om te geleiden",
                ],
                0,
                "Stroom vraagt ladingen die zich kunnen verplaatsen.",
            ),
            mk(
                "Waarom splijt het kristal als het valt?",
                [
                    "Gelijke ladingen komen tegenover elkaar",
                    "De vrije elektronen lopen uit het rooster weg",
                    "De losse moleculen laten elkaar zomaar los",
                    "De atoombindingen smelten door de klap",
                ],
                0,
                "Schuiven de lagen op, dan stoten gelijke ladingen elkaar af.",
            ),
        ],
    ),
    tabel(
        "Diamant of grafiet?",
        [
            ("geleidt elektriciteit", "Grafiet"),
            ("heel hard", "Diamant"),
            ("lagen die over elkaar glijden", "Grafiet"),
            ("elk atoom maakt vier bindingen", "Diamant"),
            ("elk atoom heeft nog een vrij elektron", "Grafiet"),
        ],
        "Beide bestaan uit koolstof. Het verschil zit in hoe de atomen in het rooster zitten.",
        kolommen=["Diamant", "Grafiet"],
    ),
    tabel(
        "Klopt dit over de elektronegativiteit?",
        [
            ("Ze neemt in een periode toe naar rechts.", J),
            ("Niet-metalen hebben een hoge elektronegativiteit.", J),
            ("Chloor trekt elektronen sterker aan dan natrium.", J),
            ("Een groot verschil wijst op een atoombinding.", F),
        ],
        "Hoe groter het verschil, hoe meer de binding naar een ionbinding opschuift.",
    ),
    koppel(
        "Koppel elke molecule aan het soort binding tussen de atomen.",
        [
            ("N₂", "drievoudige binding"),
            ("O₂", "dubbele binding"),
            ("H₂", "enkelvoudige binding"),
        ],
        ["ionbinding"],
        "Stikstof deelt drie paren, zuurstof twee, waterstof één.",
    ),
    inv(
        "In methaan CH₄ zit één koolstofatoom. Hoeveel elektronenparen deelt het in totaal?",
        ["4", "vier"],
        "Koolstof heeft vier valentie-elektronen en heeft er nog vier nodig: vier bindingen, één met elk waterstofatoom.",
    ),
    tabel(
        "Klopt dit over het oxidatiegetal?",
        [
            ("In een enkelvoudige stof is het altijd nul.", J),
            ("Zuurstof heeft in de meeste verbindingen min twee.", J),
            ("De som in een neutrale stof is nul.", J),
            ("In zuurstofgas is het oxidatiegetal van zuurstof min twee.", F),
        ],
        "Zuurstofgas is een enkelvoudige stof, dus nul.",
    ),
    sorteer(
        "Binair of ternair?",
        ["Binair", "Ternair"],
        [
            ["water H₂O", "Binair"],
            ["keukenzout NaCl", "Binair"],
            ["koolstofdioxide CO₂", "Binair"],
            ["zwavelzuur H₂SO₄", "Ternair"],
            ["natriumhydroxide NaOH", "Ternair"],
        ],
        "Binair: twee elementen. Ternair: drie elementen.",
    ),
    sorteer(
        "Geleider of isolator?",
        ["Geleider", "Isolator"],
        [
            ["koper", "Geleider"],
            ["zoutoplossing", "Geleider"],
            ["gesmolten keukenzout", "Geleider"],
            ["suikeroplossing", "Isolator"],
            ["rubber", "Isolator"],
            ["diamant", "Isolator"],
        ],
        "Geleiden vraagt vrije elektronen of vrije ionen.",
    ),
    mk(
        "Waarom geleidt een suikeroplossing geen stroom?",
        [
            "Suiker valt in water niet in ionen uiteen",
            "Suiker lost eigenlijk helemaal niet op in water",
            "Suiker heeft een metaalrooster zonder elektronen",
            "Suiker trekt alle vrije ionen uit het water aan",
        ],
        0,
        "Suikermoleculen blijven hele moleculen. Er bewegen geen ladingen.",
    ),
    sleep(
        "Bij een [[ionbinding]] worden elektronen overgedragen. Bij een [[atoombinding]] worden ze gedeeld. Bij een [[metaalbinding]] vormen ze een elektronenzee.",
        ["isolator", "formule-eenheid"],
        "Drie bindingstypes, drie manieren om met de buitenste elektronen om te gaan.",
    ),
    keuze(
        "NaCl is geen molecule maar een [[*formule-eenheid|isotoop|vrij elektronenpaar]]: de kleinste verhouding van de ionen in het rooster.",
        "Een ionrooster bestaat niet uit losse moleculen.",
    ),
    mk(
        "Bij de vorming van keukenzout gaat een elektron van natrium naar chloor. Waarom die richting?",
        [
            "Chloor trekt elektronen veel sterker aan",
            "Natrium heeft een hogere elektronegativiteit",
            "Chloor heeft geen valentie-elektronen",
            "Natrium is een niet-metaal zoals chloor",
        ],
        0,
        "Chloor heeft een veel hogere elektronegativiteit dan natrium.",
    ),
    tabel(
        "Klopt dit over een metaalrooster?",
        [
            ("Het geleidt ook in vaste toestand.", J),
            ("Het is plooibaar in plaats van breekbaar.", J),
            ("De vrije elektronen voeren ook warmte mee.", J),
            ("Het bestaat uit positieve en negatieve ionen.", F),
        ],
        "Een metaalrooster bestaat uit positieve ionen in een zee van elektronen.",
    ),
    keuze(
        "Een gesmolten zout geleidt stroom, omdat de [[*ionen|moleculen|neutronen]] loskomen van hun plaats.",
        "Smelten breekt het rooster zonder de ionen te veranderen.",
    ),
    tabel(
        "Welk roostertype past bij elke stof?",
        [
            ("een vaste stof die glanst, stroom geleidt en plooit", "Metaalrooster"),
            ("koolstofdioxide, een gas bij kamertemperatuur", "Molecuulrooster"),
            ("diamant", "Atoomrooster"),
            ("keukenzout", "Ionrooster"),
        ],
        "De eigenschappen volgen uit het roostertype.",
        kolommen=["Ionrooster", "Metaalrooster", "Molecuulrooster", "Atoomrooster"],
    ),
    tabel(
        "Klopt dit over de Lewisstructuur?",
        [
            ("Je tekent enkel de valentie-elektronen.", J),
            ("Een streepje tussen twee atomen is een bindend paar.", J),
            ("Een dubbele binding is één gedeeld paar.", F),
        ],
        "Een dubbele binding is twee gedeelde paren, dus vier elektronen.",
    ),
    mk(
        "Je mengt een metaal en een niet-metaal tot een nieuwe stof. Wat voorspel je?",
        [
            "Het is een ionverbinding",
            "Het is een molecule met een dubbele binding",
            "Het is een metaal met een elektronenzee",
            "Het is een edelgas dat niet reageert",
        ],
        0,
        "Een metaal met een niet-metaal geeft een ionbinding en een ionrooster.",
    ),
    keuze(
        "Twee niet-metalen gaan een [[*atoombinding|ionbinding|metaalbinding]] aan, want geen van beide staat graag elektronen af.",
        "Delen is dan de enige manier om een volle schil te bereiken.",
    ),
    open_(
        "Leg uit waarom water bij kamertemperatuur vloeibaar is, terwijl keukenzout pas bij 801 °C smelt. Gebruik de woorden molecuulrooster, ionrooster en aantrekking.",
        "Water heeft een molecuulrooster. Binnen de molecule zijn de bindingen sterk, maar de aantrekking tussen de moleculen is zwak en breekt al bij een lage temperatuur. Keukenzout heeft een ionrooster: de ionen trekken elkaar in alle richtingen sterk aan, en om dat hele rooster los te breken is veel energie nodig.",
    ),
]
