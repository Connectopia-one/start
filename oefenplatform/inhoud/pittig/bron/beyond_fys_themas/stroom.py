"""Elektrodynamica: stroom, weerstand en schakelingen — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL


def weerstand_h(p, x, y, label):
    """Horizontale weerstand met midden (x, y)."""
    p.rect(x - 50, y - 16, 100, 32, "#ffffff", DONKER, 2, 3)
    p.tekst(x, y - 28, label, 20, vet=True)


def weerstand_v(p, x, y, label):
    """Verticale weerstand met midden (x, y)."""
    p.rect(x - 16, y - 50, 32, 100, "#ffffff", DONKER, 2, 3)
    p.tekst(x + 28, y + 7, label, 20, anker="start", vet=True)


def bron_v(p, x, y, label):
    """Verticale spanningsbron: lange streep (+) boven, korte (−) onder."""
    p.rect(x - 40, y - 14, 80, 28, "#ffffff", "#ffffff", 0, 0)
    p.lijn(x - 34, y - 10, x + 34, y - 10, DONKER, 4)
    p.lijn(x - 16, y + 10, x + 16, y + 10, DONKER, 7)
    p.tekst(x - 60, y + 7, label, 20, anker="end", vet=True)
    p.tekst(x + 44, y - 16, "+", 18)


# Gemengde schakeling -------------------------------------------------------
GS = Prent("gemengde-schakeling", "Een bron van 18 V met drie weerstanden", "een bron van 18 V; R1 = 6 ohm in de bovenste draad, daarna twee takken naast elkaar: R2 = 4 ohm en R3 = 12 ohm")
GS.lijn(180, 120, 800, 120, DONKER, 3)
GS.lijn(180, 520, 800, 520, DONKER, 3)
GS.lijn(180, 120, 180, 520, DONKER, 3)
GS.lijn(560, 120, 560, 520, DONKER, 3)
GS.lijn(800, 120, 800, 520, DONKER, 3)
bron_v(GS, 180, 320, "18 V")
weerstand_h(GS, 370, 120, "R₁ = 6 Ω")
weerstand_v(GS, 560, 320, "R₂ = 4 Ω")
weerstand_v(GS, 800, 320, "R₃ = 12 Ω")
for x, y in ((560, 120), (560, 520)):
    GS.cirkel(x, y, 6, DONKER, DONKER, 1)
ZG = {
    "R1": [Prent.zone(310, 60, 120, 80)],
    "R2": [Prent.zone(540, 265, 150, 110)],
    "R3": [Prent.zone(780, 265, 160, 110)],
}

# Waar zet je de meter? --------------------------------------------------------
MP = Prent("meters-plaatsen", "Een lamp en een weerstand in serie, met drie mogelijke plaatsen voor een meter", "een bron, een lamp en een weerstand in serie; plaats P in de draad zelf, plaats Q in een zijtak over de lamp, plaats R in een zijtak over de weerstand")
MP.lijn(150, 200, 850, 200, DONKER, 3)
MP.lijn(150, 200, 150, 480, DONKER, 3)
MP.lijn(850, 200, 850, 480, DONKER, 3)
MP.lijn(150, 480, 850, 480, DONKER, 3)
bron_v(MP, 150, 340, "bron")
# P in de onderste draad
MP.rect(460, 464, 80, 32, "#ffffff", "#ffffff", 0, 0)
MP.svg('<circle cx="500" cy="480" r="30" fill="#ffffff" stroke="#2f4a22" stroke-width="2" stroke-dasharray="6 5"/>')
MP.lijn(430, 480, 470, 480, DONKER, 3)
MP.lijn(530, 480, 570, 480, DONKER, 3)
MP.tekst(500, 490, "P", 26, vet=True)
# lamp
MP.rect(320, 184, 60, 32, "#ffffff", "#ffffff", 0, 0)
MP.cirkel(350, 200, 28, "#fff6d6", DONKER, 3)
MP.lijn(330, 180, 370, 220, DONKER, 2)
MP.lijn(370, 180, 330, 220, DONKER, 2)
MP.tekst(350, 250, "lamp", 18)
# weerstand
weerstand_h(MP, 670, 200, "")
MP.tekst(670, 250, "weerstand", 18)
# zijtakken Q en R
for (x1, x2, k) in ((270, 430, "Q"), (590, 750, "R")):
    MP.lijn(x1, 200, x1, 100, DONKER, 3)
    MP.lijn(x2, 200, x2, 100, DONKER, 3)
    xm = (x1 + x2) / 2
    MP.lijn(x1, 100, xm - 30, 100, DONKER, 3)
    MP.lijn(xm + 30, 100, x2, 100, DONKER, 3)
    MP.svg(f'<circle cx="{xm}" cy="100" r="30" fill="#ffffff" stroke="#2f4a22" stroke-width="2" stroke-dasharray="6 5"/>')
    MP.tekst(xm, 110, k, 26, vet=True)
    MP.cirkel(x1, 200, 6, DONKER, DONKER, 1)
    MP.cirkel(x2, 200, 6, DONKER, DONKER, 1)
ZM = {"P": [Prent.rond(500, 480, 36)], "Q": [Prent.rond(350, 100, 36)], "R": [Prent.rond(670, 100, 36)]}

VRAGEN = [
    klik(
        "Klik op de weerstand waarover de grootste spanning staat.",
        GS.bestand, ZG["R1"],
        "R₂ en R₃ samen zijn 3 Ω, R_v = 9 Ω en I = 2 A: over R₁ staat 12 V, over het parallelle stuk 6 V.",
    ),
    klik(
        "Klik op de weerstand waardoor de kleinste stroom loopt.",
        GS.bestand, ZG["R3"],
        "Over R₂ en R₃ staat dezelfde 6 V; door de grootste weerstand loopt de kleinste stroom.",
    ),
    met_prent(GS.bestand, mk(
        "Hoe groot is de vervangingsweerstand van de hele schakeling?",
        ["9 Ω", "22 Ω", "3 Ω", "2 Ω"],
        0,
        "R₂ // R₃: 1/4 + 1/12 = 4/12, dus 3 Ω. Plus R₁: 6 + 3 = 9 Ω.",
    )),
    met_prent(GS.bestand, inv(
        "Hoeveel stroom levert de bron, in ampère?",
        ["2", "2,0", "2 A", "2,0 A"],
        "I = U / R_v = 18 / 9 = 2,0 A.",
    )),
    met_prent(GS.bestand, inv(
        "Welke spanning staat er over R₂, in volt?",
        ["6", "6,0", "6 V", "6,0 V"],
        "Over R₁ staat 6 · 2,0 = 12 V, dus blijft er 18 − 12 = 6,0 V over voor het parallelle stuk.",
    )),
    met_prent(GS.bestand, tabel(
        "Hoeveel stroom loopt er door deze weerstand?",
        [
            ("R₁", "2,0 A"),
            ("R₂", "1,5 A"),
            ("R₃", "0,5 A"),
        ],
        "I₂ = 6 / 4 = 1,5 A en I₃ = 6 / 12 = 0,5 A; samen weer 2,0 A.",
        kolommen=["0,5 A", "1,5 A", "2,0 A"],
    )),
    met_prent(GS.bestand, keuze(
        "Haal je R₃ weg, dan wordt de stroom uit de bron [[*kleiner|groter|niet anders]].",
        "Er valt een weg weg, dus wordt R_v groter.",
    )),
    met_prent(GS.bestand, mk(
        "Hoeveel stroom levert de bron als R₃ weg is?",
        ["1,8 A", "2,0 A", "3,0 A", "1,5 A"],
        0,
        "R_v = 6 + 4 = 10 Ω, dus I = 18 / 10 = 1,8 A.",
    )),
    klik(
        "Klik op de plaats waar je een ampèremeter zet om de stroom door de lamp te meten.",
        MP.bestand, ZM["P"],
        "Een ampèremeter staat in serie: de stroom moet erdoor. In een serieschakeling is I overal gelijk.",
    ),
    klik(
        "Klik op de plaats waar je een voltmeter zet om de spanning over de weerstand te meten.",
        MP.bestand, ZM["R"],
        "Een voltmeter staat parallel over het onderdeel zelf.",
    ),
    met_prent(MP.bestand, mk(
        "Je zet per vergissing een voltmeter op plaats P. Wat gebeurt er?",
        [
            "Er loopt bijna geen stroom meer",
            "De lamp brandt veel feller dan voordien",
            "De meter toont de stroom in ampère",
            "Er verandert niets aan de schakeling",
        ],
        0,
        "Een voltmeter heeft een heel grote weerstand; in serie houdt hij de stroom bijna tegen.",
    )),
    met_prent(MP.bestand, mk(
        "Je zet per vergissing een ampèremeter op plaats Q. Wat gebeurt er met de lamp?",
        [
            "Ze dooft bijna helemaal uit",
            "Ze brandt feller, want de stroom wordt groter",
            "Er verandert niets, de meter meet gewoon",
            "Ze brandt even hard, maar de meter toont nul",
        ],
        0,
        "De meter heeft bijna geen weerstand: bijna alle stroom gaat via de zijtak en niet door de lamp.",
    )),
    met_prent(MP.bestand, keuze(
        "Een goede ampèremeter heeft een [[*heel kleine|heel grote]] eigen weerstand, een goede voltmeter een [[heel kleine|*heel grote]].",
        "Zo verstoren ze de kring zo weinig mogelijk.",
    )),
    inv(
        "Door een draad gaat in één minuut 90 C lading. Hoe groot is de stroomsterkte, in ampère?",
        ["1,5", "1,5 A", "1.5"],
        "I = Δq / Δt = 90 C / 60 s = 1,5 A.",
    ),
    mk(
        "Door een lamp loopt 0,32 A. Hoeveel elektronen gaan er per seconde door een doorsnede? Neem e = 1,6 · 10⁻¹⁹ C.",
        ["2,0 · 10¹⁸", "5,1 · 10⁻²⁰", "2,0 · 10⁻¹⁸", "3,2 · 10¹⁹"],
        0,
        "0,32 C per seconde, gedeeld door 1,6 · 10⁻¹⁹ C per elektron.",
    ),
    mk(
        "Een koperdraad wordt twee keer zo lang én twee keer zo dik in doorsnede. Wat gebeurt er met R?",
        ["Ze blijft gelijk", "Ze wordt 4 keer zo groot", "Ze wordt 2 keer zo groot", "Ze wordt de helft"],
        0,
        "R = ρ · ℓ / A: ℓ × 2 en A × 2 heffen elkaar op.",
    ),
    tabel(
        "Met welke factor verandert de weerstand van een draad uit hetzelfde metaal?",
        [
            ("de lengte wordt 2 keer zo groot", "× 2"),
            ("de doorsnede wordt 2 keer zo groot", "÷ 2"),
            ("de lengte wordt 4 keer zo groot", "× 4"),
        ],
        "R = ρ · ℓ / A: evenredig met de lengte, omgekeerd evenredig met de doorsnede.",
        kolommen=["× 2", "÷ 2", "× 4"],
    ),
    mk(
        "Drie gelijke weerstanden van 12 Ω staan parallel. Hoe groot is R_v?",
        ["4,0 Ω", "36 Ω", "12 Ω", "6,0 Ω"],
        0,
        "Bij n gelijke weerstanden parallel: R / n = 12 / 3 = 4,0 Ω.",
    ),
    inv(
        "Weerstanden van 3,0 Ω en 6,0 Ω staan parallel. Hoe groot is R_v, in ohm?",
        ["2", "2,0", "2 Ω", "2,0 Ω"],
        "1/R_v = 1/3 + 1/6 = 1/2, dus R_v = 2,0 Ω.",
    ),
    inv(
        "Bij 6,0 V loopt er 0,30 A door een weerstand die de wet van Ohm volgt. Hoeveel ampère loopt er bij 9,0 V?",
        ["0,45", "0,45 A", "0.45"],
        "R = 6,0 / 0,30 = 20 Ω, dus I = 9,0 / 20 = 0,45 A.",
    ),
    casus(
        "Een oude lichtslinger heeft 20 gelijke lampjes in serie op 230 V. Er loopt 0,10 A.",
        [
            inv(
                "Welke spanning staat er over één lampje, in volt?",
                ["11,5", "11,5 V", "11.5"],
                "De deelspanningen tellen op tot 230 V: 230 / 20 = 11,5 V.",
            ),
            inv(
                "Hoe groot is de weerstand van één lampje, in ohm?",
                ["115", "115 Ω"],
                "R = U / I = 11,5 / 0,10 = 115 Ω.",
            ),
            keuze(
                "Gaat er één lampje stuk, dan [[*doven alle lampjes|branden de andere gewoon verder]].",
                "In serie is er maar één weg: de kring is onderbroken.",
            ),
        ],
    ),
    sorteer(
        "Geldt dit voor een serieschakeling of een parallelschakeling?",
        ["Serie", "Parallel"],
        [
            ("de stroom is overal even groot", "Serie"),
            ("over elke tak staat dezelfde spanning", "Parallel"),
            ("R_v = R₁ + R₂", "Serie"),
            ("R_v is kleiner dan de kleinste weerstand", "Parallel"),
        ],
        "Serie: één weg. Parallel: elke tak een eigen weg.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("De elektronen in een draad bewegen van min naar plus.", J),
            ("Bij wisselstroom keert de zin van de stroom steeds om.", J),
            ("Een extra tak parallel maakt R_v groter.", F),
            ("In serie is de som van de deelspanningen gelijk aan de bronspanning.", J),
        ],
        "Elke extra tak is een extra weg voor de stroom, dus R_v daalt.",
    ),
    koppel(
        "Koppel elke grootheid aan haar eenheid.",
        [
            ("stroomsterkte I", "A"),
            ("spanning U", "V"),
            ("weerstand R", "Ω"),
            ("lading q", "C"),
        ],
        ["N"],
        "1 A = 1 C/s en 1 Ω = 1 V/A.",
    ),
    volgorde(
        "Zet de stappen om een gemengde schakeling door te rekenen in volgorde.",
        [
            "Het parallelle stuk vervangen door één weerstand",
            "Die optellen bij de weerstand in serie",
            "De bronstroom berekenen met I = U / R_v",
            "De spanning over het parallelle stuk berekenen",
            "De stroom per tak berekenen",
        ],
        "Van de delen naar het geheel, en dan terug naar de delen.",
    ),
    sleep(
        "Een ampèremeter zet je in [[serie]], een voltmeter [[parallel]]. Een draad wordt warm doordat de elektronen [[botsen]] tegen de atomen.",
        ["versnellen", "kortsluiting"],
        "Bij elke botsing gaat er energie naar het rooster.",
    ),
    open_(
        "Leg uit waarom de vervangingsweerstand van een parallelschakeling altijd kleiner is dan de kleinste weerstand erin.",
        "Elke tak is een extra weg voor de stroom. Bij dezelfde spanning loopt er door de schakeling dus meer stroom dan door de kleinste weerstand alleen. Meer stroom bij dezelfde spanning betekent een kleinere weerstand: R_v = U / I wordt kleiner.",
    ),
    met_prent(MP.bestand, tabel(
        "Welke meter hoort op deze plaats?",
        [
            ("P", "Ampèremeter"),
            ("Q", "Voltmeter"),
            ("R", "Voltmeter"),
        ],
        "In de draad zelf meet je stroom, in een zijtak over een onderdeel meet je spanning.",
        kolommen=["Ampèremeter", "Voltmeter"],
    )),
]
