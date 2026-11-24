"""Elektriciteit en de wet van Ohm — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, assen

# U-I-grafiek ------------------------------------------------------------
UI = Prent("ui-twee-weerstanden", "Stroomsterkte en spanning bij twee weerstanden", "I(U)-grafiek van weerstand P en weerstand Q")
X, Y = assen(UI, 0, 12, 0, 3, "U (V)", "I (A)", 1, 0.5)
UI.pad(f"M{X(0)} {Y(0)} L {X(12)} {Y(3)}", "none", BLAUW, 5)
UI.pad(f"M{X(0)} {Y(0)} L {X(12)} {Y(1)}", "none", ORANJE, 5)
UI.letter(X(10) - 30, Y(2.5) - 30, "P")
UI.letter(X(11), Y(11 / 12) - 40, "Q")
ZUP = [Prent.zone(X(5), Y(3), X(12) - X(5), Y(1.1) - Y(3)), Prent.rond(X(10) - 30, Y(2.5) - 30, 26)]
ZUQ = [Prent.zone(X(5), Y(1.15), X(12) - X(5), Y(0.3) - Y(1.15)), Prent.rond(X(11), Y(11 / 12) - 40, 26)]

# Schakelschema ----------------------------------------------------------
SC = Prent("schakelschema", "Een schakelschema", "kring met bron, schakelaar, lamp, weerstand en twee meters A tot F")
L, R, T, B = 180, 820, 160, 480
# draden
SC.lijn(L, T, 330, T); SC.lijn(400, T, 560, T); SC.lijn(640, T, R, T)
SC.lijn(R, T, R, 280); SC.lijn(R, 360, R, B)
SC.lijn(R, B, 560, B); SC.lijn(460, B, L, B)
SC.lijn(L, B, L, 350); SC.lijn(L, 290, L, T)
# bron (links): lange en korte streep
SC.lijn(L - 40, 290, L + 40, 290, DONKER, 4)
SC.lijn(L - 20, 350, L + 20, 350, DONKER, 8)
SC.tekst(L + 60, 300, "+", 26)
# schakelaar (boven links)
SC.cirkel(330, T, 6, "#ffffff"); SC.cirkel(400, T, 6, "#ffffff")
SC.lijn(330, T, 395, T - 35, DONKER, 3)
# lamp (boven rechts)
SC.cirkel(600, T, 40, "#ffffff")
SC.lijn(572, T - 28, 628, T + 28); SC.lijn(572, T + 28, 628, T - 28)
# weerstand (rechts)
SC.rect(R - 22, 280, 44, 80, "#ffffff", DONKER, 0)
# ampèremeter (onder)
SC.cirkel(510, B, 40, "#ffffff")
SC.tekst(510, B + 10, "A", 30, vet=True)
# voltmeter parallel over weerstand
SC.lijn(R, 250, 920, 250); SC.lijn(920, 250, 920 , 280)
SC.lijn(920, 360, 920, 390); SC.lijn(920, 390, R, 390)
SC.cirkel(920, 320, 40, "#ffffff")
SC.tekst(920, 330, "V", 30, vet=True)
LET = {"1": (90, 320), "2": (365, 90), "3": (600, 80), "4": (750, 320), "5": (510, 570), "6": (920, 430)}
NAAM = {}
for k, (x, y) in LET.items():
    SC.letter(x, y, k)
ZSC = {
    "bron": [Prent.zone(L - 50, 270, 100, 100), Prent.rond(*LET["1"], 26)],
    "schakelaar": [Prent.zone(320, T - 50, 90, 60), Prent.rond(*LET["2"], 26)],
    "lamp": [Prent.rond(600, T, 44), Prent.rond(*LET["3"], 26)],
    "weerstand": [Prent.zone(R - 30, 275, 60, 90), Prent.rond(*LET["4"], 26)],
    "amperemeter": [Prent.rond(510, B, 44), Prent.rond(*LET["5"], 26)],
    "voltmeter": [Prent.rond(920, 320, 44), Prent.rond(*LET["6"], 26)],
}

VRAGEN = [
    klik(
        "Klik op het toestel dat de stroomsterkte meet.",
        SC.bestand, ZSC["amperemeter"],
        "De ampèremeter staat in serie in de kring: alle stroom gaat erdoor.",
    ),
    klik(
        "Klik op het toestel dat parallel over een onderdeel staat.",
        SC.bestand, ZSC["voltmeter"],
        "De voltmeter meet de spanning over de weerstand en staat er daarom parallel over.",
    ),
    klik(
        "Klik op het onderdeel dat de kring kan openen.",
        SC.bestand, ZSC["schakelaar"],
        "De schakelaar staat open: er loopt nu geen stroom.",
    ),
    klik(
        "Klik op de spanningsbron.",
        SC.bestand, ZSC["bron"],
        "De lange streep is de pluspool, de korte dikke streep de minpool.",
    ),
    met_prent(SC.bestand, tabel(
        "Kijk naar het schema. Klopt dit?",
        [
            ("Zolang de schakelaar open staat, brandt de lamp niet.", J),
            ("De voltmeter meet de spanning over de weerstand.", J),
            ("De ampèremeter meet enkel de stroom door de lamp, niet door de weerstand.", F),
            ("Onderdeel 3 is een lamp.", J),
        ],
        "In één enkele kring is de stroomsterkte overal dezelfde.",
    )),
    klik(
        "Klik op de grootste weerstand.",
        UI.bestand, ZUQ,
        "Bij dezelfde spanning loopt door Q de kleinste stroom: grootste weerstand.",
    ),
    met_prent(UI.bestand, inv(
        "Kijk naar de grafiek. Hoeveel ohm is weerstand P?",
        ["4"],
        "Bij 12 V loopt er 3 A: R = 12 : 3 = 4 Ω.",
    )),
    met_prent(UI.bestand, inv(
        "Kijk naar de grafiek. Hoeveel ampère loopt er door Q bij 6 V?",
        ["0,5", "0.5"],
        "Q is 12 Ω (12 V geeft 1 A). 6 : 12 = 0,5 A.",
    )),
    tabel(
        "Reken uit met de wet van Ohm.",
        [
            ("U = 9 V en R = 3 Ω, dan is I", "3 A"),
            ("I = 0,5 A en R = 20 Ω, dan is U", "10 V"),
            ("U = 230 V en I = 2 A, dan is R", "115 Ω"),
            ("U = 6 V en R = 2 Ω, dan is I", "3 A"),
        ],
        "U = R · I, dus I = U : R en R = U : I.",
        kolommen=["3 A", "10 V", "115 Ω"],
    ),
    koppel(
        "Koppel elke grootheid aan haar eenheid.",
        [
            ("stroomsterkte", "ampère"),
            ("spanning", "volt"),
            ("weerstand", "ohm"),
            ("lading", "coulomb"),
        ],
        ["watt"],
        "De watt is de eenheid van vermogen.",
    ),
    tabel(
        "Geleider of isolator?",
        [
            ("koperdraad", "Geleider"),
            ("rubberen handschoen", "Isolator"),
            ("zout water", "Geleider"),
            ("droog glas", "Isolator"),
            ("aluminiumfolie", "Geleider"),
        ],
        "Metalen hebben vrije elektronen, een zoutoplossing vrije ionen.",
        kolommen=["Geleider", "Isolator"],
    ),
    casus(
        "Jonas meet de stroomsterkte door een weerstand bij verschillende spanningen.\n\n| U (V) | I (A) |\n|---|---|\n| 2 | 0,1 |\n| 4 | 0,2 |\n| 6 | 0,3 |",
        [
            inv(
                "Hoeveel ohm is de weerstand?",
                ["20"],
                "2 : 0,1 = 20 Ω, en bij elke meting komt hetzelfde uit.",
            ),
            keuze(
                "Zet Jonas deze waarden in een grafiek, dan krijgt hij een [[*rechte door de oorsprong|dalende kromme|horizontale lijn]].",
                "Spanning en stroom zijn recht evenredig.",
            ),
            inv(
                "Welke stroomsterkte verwacht hij bij 10 V, in ampère?",
                ["0,5", "0.5"],
                "10 : 20 = 0,5 A.",
            ),
        ],
    ),
    tabel(
        "Wordt de weerstand van een draad groter of kleiner?",
        [
            ("je maakt de draad langer", "Groter"),
            ("je kiest een dikkere draad", "Kleiner"),
            ("je kiest een dunnere draad", "Groter"),
            ("je maakt de draad korter", "Kleiner"),
        ],
        "Een langere, nauwere weg geeft meer weerstand.",
        kolommen=["Groter", "Kleiner"],
    ),
    mk(
        "In een metaaldraad bewegen de elektronen van min naar plus. Waarom tekent men de stroom toch van plus naar min?",
        [
            "Die afspraak dateert van voor men wist dat elektronen negatief zijn",
            "De elektronen keren halverwege de draad altijd netjes van richting om",
            "In een metaal bewegen eigenlijk vooral de positieve kernen met de stroom mee",
            "De pluspool trekt de elektronen weg en zo ontstaat een tegenstroom",
        ],
        0,
        "Dat is de conventionele stroomzin.",
    ),
    tabel(
        "Gewenst of ongewenst Joule-effect?",
        [
            ("de gloeiplaat van een broodrooster", "Gewenst"),
            ("een warm verlengsnoer", "Ongewenst"),
            ("een elektrisch vuurtje", "Gewenst"),
            ("een opgewarmde laptoplader", "Ongewenst"),
        ],
        "Waar de warmte de bedoeling is, is het effect gewenst.",
        kolommen=["Gewenst", "Ongewenst"],
    ),
    koppel(
        "Koppel elke beveiliging aan wat ze doet.",
        [
            ("automatische zekering", "slaat af bij te grote stroom"),
            ("verliesstroomschakelaar", "slaat af als stroom langs een andere weg wegloopt"),
            ("aarddraad", "leidt stroom van een metalen omhulsel naar de grond"),
            ("dubbele isolatie", "houdt het omhulsel altijd spanningsloos"),
        ],
        ["meet de spanning over een toestel"],
        "Meten doet een voltmeter, en die beveiligt niets.",
    ),
    tabel(
        "Welk risico is dit vooral?",
        [
            ("twee blanke draden raken elkaar", "Kortsluiting"),
            ("de oven, de wasmachine en de droogkast op één kring", "Overbelasting"),
            ("met natte handen een kapotte stekker vastnemen", "Elektrocutie"),
        ],
        "Bij kortsluiting en overbelasting wordt de stroom te groot. Bij elektrocutie loopt hij door je lichaam.",
        kolommen=["Kortsluiting", "Overbelasting", "Elektrocutie"],
    ),
    inv(
        "Een strijkijzer van 2000 W staat anderhalf uur aan. Hoeveel kilowattuur verbruikt het?",
        ["3"],
        "2 kW · 1,5 h = 3 kWh.",
    ),
    sleep(
        "Bij een [[kortsluiting]] vindt de stroom een weg met bijna geen [[weerstand]]. De stroomsterkte wordt dan heel groot en de [[zekering]] slaat af.",
        ["voltmeter", "spanning"],
        "Zo voorkomt de zekering dat de draden te heet worden.",
    ),
    tabel(
        "Klopt dit over je lichaam en elektriciteit?",
        [
            ("Met natte handen is je weerstand kleiner.", J),
            ("Een grotere spanning geeft bij dezelfde weerstand een grotere stroom door je lichaam.", J),
            ("Het gevaar hangt vooral af van de stroom door je lichaam.", J),
            ("Droge huid geleidt beter dan natte huid.", F),
        ],
        "Wet van Ohm: I = U : R. Minder weerstand of meer spanning geeft meer stroom.",
    ),
    keuze(
        "Een batterij levert [[*gelijkspanning|wisselspanning|netspanning]], met een vaste plus- en minpool.",
        "Het stopcontact levert wisselspanning.",
    ),
    tabel(
        "Een ledlamp van 7 W geeft evenveel licht als een gloeilamp van 60 W. Klopt dit?",
        [
            ("De ledlamp zet per seconde minder energie om.", J),
            ("De gloeilamp maakt veel meer warmte.", J),
            ("De ledlamp heeft het grootste rendement.", J),
            ("Ze verbruiken in een uur evenveel energie.", F),
        ],
        "Minder vermogen voor dezelfde taak is zuiniger.",
    ),
    volgorde(
        "Zet in de juiste volgorde: een verliesstroomschakelaar redt iemand.",
        [
            "Een kapotte draad raakt het metalen omhulsel van een toestel",
            "Iemand raakt het omhulsel aan",
            "Er loopt stroom door die persoon naar de grond",
            "De schakelaar merkt dat er minder stroom terugkomt en slaat af",
        ],
        "Hij vergelijkt wat erin gaat met wat terugkomt.",
    ),
    met_prent(SC.bestand, tabel(
        "Kijk naar het schema. Welk nummer hoort bij welk onderdeel?",
        [
            ("de weerstand", "4"),
            ("de lamp", "3"),
            ("de voltmeter", "6"),
            ("de schakelaar", "2"),
        ],
        "Een weerstand is een rechthoekje, een lamp een rondje met een kruis.",
        kolommen=["2", "3", "4", "6"],
    )),
    met_prent(UI.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("Weerstand Q is drie keer zo groot als P.", J),
            ("Bij beide is de stroom recht evenredig met de spanning.", J),
            ("Hoe steiler de rechte, hoe groter de weerstand.", F),
            ("Bij 0 V loopt er door beide geen stroom.", J),
        ],
        "Een steilere rechte betekent meer stroom per volt: een kleinere weerstand.",
    )),
    inv(
        "Een lampje heeft 6 Ω en er loopt 0,5 A door. Hoeveel volt staat erover?",
        ["3"],
        "U = R · I = 6 · 0,5 = 3 V.",
    ),
    keuze(
        "Verdubbel je de weerstand bij dezelfde spanning, dan wordt de stroomsterkte [[*half zo groot|dubbel zo groot|even groot]].",
        "Stroom en weerstand zijn omgekeerd evenredig bij gelijke spanning.",
    ),
    open_(
        "Leg uit waarom een te dun verlengsnoer brandgevaarlijk kan zijn als je er een zware verwarming op aansluit.",
        "Een zware verwarming trekt een grote stroom. Een dunne draad heeft een grotere weerstand. Door het Joule-effect wordt de draad dan heet, en de isolatie kan smelten of vuur vatten.",
    ),
]
