"""Elektrische energie, potentiaal en spanning — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Homogeen veld tussen twee platen --------------------------------------------
PL = Prent("platen-potentiaal", "Twee evenwijdige platen op 10 cm van elkaar", "links een plaat op 200 V, rechts een plaat op 0 V, gestippelde lijnen om de 2 cm, een liniaal van 0 tot 10 cm onderaan, vier punten A tot D")
def _x(cm):
    return 200 + 60 * cm
PL.rect(180, 90, 20, 440, ROOD, DONKER, 3, 2)
PL.rect(800, 90, 20, 440, BLAUW, DONKER, 3, 2)
PL.tekst(190, 75, "200 V", 22, vet=True)
PL.tekst(810, 75, "0 V", 22, vet=True)
for cm in (2, 4, 6, 8):
    PL.lijn(_x(cm), 95, _x(cm), 525, GRIJS, 2, stippel=True)
PL.lijn(_x(0), 570, _x(10), 570, DONKER, 2)
for cm in range(11):
    PL.lijn(_x(cm), 562, _x(cm), 578, DONKER, 2)
    PL.tekst(_x(cm), 602, str(cm), 16)
PL.tekst(900, 602, "cm", 16)
PUNT = {"A": (2, 200), "B": (5, 180), "C": (5, 470), "D": (8, 330)}
for k, (cm, y) in PUNT.items():
    PL.cirkel(_x(cm), y, 7, DONKER, DONKER, 1)
    PL.letter(_x(cm) + 28, y - 24, k)
ZP = {k: [Prent.rond(_x(cm), y, 24), Prent.rond(_x(cm) + 28, y - 24, 22)] for k, (cm, y) in PUNT.items()}

# Equipotentiaallijnen rond een puntlading ------------------------------------------
EQ = Prent("equipotentiaal-puntlading", "Equipotentiaallijnen rond een positieve puntlading", "een positieve lading in het midden met drie gestippelde cirkels van 300 V, 200 V en 100 V; vier punten P tot S")
C0 = (480, 340)
for r, v in ((80, 300), (120, 200), (240, 100)):
    EQ.svg(f'<circle cx="{C0[0]}" cy="{C0[1]}" r="{r}" fill="none" stroke="#7a7a7a" stroke-width="2" stroke-dasharray="8 6"/>')
    EQ.tekst(C0[0], C0[1] - r - 8, f"{v} V", 18, vet=True)
EQ.cirkel(*C0, 20, ROOD, DONKER, 2)
EQ.tekst(C0[0], C0[1] + 10, "+", 28, kleur="#ffffff", vet=True)
def _op(r, graden):
    h = math.radians(graden)
    return C0[0] + r * math.cos(h), C0[1] - r * math.sin(h)
HOEK = {"P": (120, 20), "Q": (120, 200), "R": (240, -30), "S": (80, 250)}
QPUNT = {k: _op(r, g) for k, (r, g) in HOEK.items()}
LET = {k: (_op(r + 32, g) if k != "S" else _op(r - 36, g)) for k, (r, g) in HOEK.items()}
for k, (x, y) in QPUNT.items():
    EQ.cirkel(x, y, 7, DONKER, DONKER, 1)
    EQ.letter(*LET[k], k)
ZQ = {k: [Prent.rond(*QPUNT[k], 24), Prent.rond(*LET[k], 22)] for k in QPUNT}

VRAGEN = [
    klik(
        "Klik op het punt met de hoogste potentiaal.",
        PL.bestand, ZP["A"],
        "De potentiaal daalt gelijkmatig van de plaat op 200 V naar die op 0 V; A ligt het dichtst bij 200 V.",
    ),
    klik(
        "Klik op het punt waarnaar je een lading uit B kan verplaatsen zonder dat er arbeid nodig is.",
        PL.bestand, ZP["C"],
        "B en C liggen even ver van de platen, dus op dezelfde equipotentiaallijn.",
    ),
    met_prent(PL.bestand, tabel(
        "Welke potentiaal heeft dit punt?",
        [
            ("A", "160 V"),
            ("B", "100 V"),
            ("D", "40 V"),
        ],
        "Per cm daalt de potentiaal met 200 V / 10 = 20 V.",
        kolommen=["40 V", "100 V", "160 V"],
    )),
    met_prent(PL.bestand, inv(
        "Hoe groot is de spanning U tussen A en D, in volt?",
        ["120", "120 V"],
        "V_A − V_D = 160 V − 40 V = 120 V.",
    )),
    met_prent(PL.bestand, inv(
        "Hoe groot is de veldsterkte tussen de platen, in N/C?",
        ["2000", "2000 N/C", "2 · 10³", "2,0 · 10³"],
        "E = U / d = 200 V / 0,10 m = 2000 N/C (of V/m).",
    )),
    met_prent(PL.bestand, mk(
        "Een proton vertrekt uit rust in A. Met hoeveel kinetische energie komt het voorbij D?",
        ["120 eV", "160 eV", "40 eV", "200 eV"],
        0,
        "Het doorloopt 160 V − 40 V = 120 V, en één elementaire lading wint dan 120 eV.",
    )),
    met_prent(PL.bestand, keuze(
        "Een elektron dat in D vrijkomt, beweegt vanzelf naar [[*de plaat op 200 V|de plaat op 0 V]].",
        "Een negatieve lading beweegt vanzelf naar een hogere potentiaal.",
    )),
    klik(
        "Klik op het punt waar een kleine positieve lading de grootste potentiële energie heeft.",
        EQ.bestand, ZQ["S"],
        "E_p = q · V, en S ligt op de lijn van 300 V.",
    ),
    met_prent(EQ.bestand, inv(
        "Een lading van 2,0 µC gaat van P naar R. Hoeveel arbeid levert de elektrische kracht, in mJ?",
        ["0,2", "0,20", "0,2 mJ", "0,20 mJ", "0.2"],
        "W = q · (V_P − V_R) = 2,0 · 10⁻⁶ · 100 = 2,0 · 10⁻⁴ J = 0,20 mJ.",
    )),
    met_prent(EQ.bestand, tabel(
        "Een kleine positieve lading start in P. Wat geldt voor deze verplaatsing?",
        [
            ("van P naar Q", "Geen arbeid"),
            ("van P naar R", "Het veld levert arbeid"),
            ("van P naar S", "Jij moet arbeid leveren"),
        ],
        "Naar een lagere potentiaal gaat vanzelf; naar een hogere kost arbeid.",
        kolommen=["Geen arbeid", "Het veld levert arbeid", "Jij moet arbeid leveren"],
    )),
    met_prent(EQ.bestand, mk(
        "Waarom liggen de lijnen van 200 V en 100 V veel verder uit elkaar dan die van 300 V en 200 V?",
        [
            "Het veld is daar zwakker",
            "De lading is daar negatiever geworden",
            "Equipotentiaallijnen liggen altijd even ver uit elkaar",
            "Verder van de lading is het veld juist sterker",
        ],
        0,
        "Waar het veld zwak is, heb je een grotere afstand nodig voor hetzelfde potentiaalverschil.",
    )),
    inv(
        "Een stofkorrel met lading 2,0 · 10⁻⁶ C en massa 1,0 · 10⁻⁶ kg vertrekt uit rust en doorloopt 100 V. Hoe snel gaat hij dan, in m/s?",
        ["20", "20 m/s"],
        "q · U = ½ · m · v²: 2,0 · 10⁻⁴ = 0,5 · 10⁻⁶ · v², dus v² = 400 en v = 20 m/s.",
    ),
    mk(
        "Een proton en een elektron doorlopen elk 1000 V. Wat klopt?",
        [
            "Ze winnen evenveel energie",
            "Het proton wint meer energie, want het is zwaarder",
            "Het elektron wint meer energie, want het is lichter",
            "Ze krijgen precies dezelfde snelheid",
        ],
        0,
        "Beide winnen e · U = 1000 eV, maar het lichte elektron wordt veel sneller.",
    ),
    inv(
        "Een elektron wint 4,8 · 10⁻¹⁷ J. Hoeveel elektronvolt is dat? Neem 1 eV = 1,6 · 10⁻¹⁹ J.",
        ["300", "300 eV"],
        "4,8 · 10⁻¹⁷ / 1,6 · 10⁻¹⁹ = 300 eV.",
    ),
    inv(
        "Een deeltje met lading 2e doorloopt een spanning van 1500 V. Hoeveel eV energie wint het?",
        ["3000", "3000 eV", "3 keV"],
        "W = q · U = 2e · 1500 V = 3000 eV.",
    ),
    mk(
        "V_A = 30 V en V_B = 90 V. Hoe groot is U_AB?",
        ["−60 V", "60 V", "120 V", "−120 V"],
        0,
        "U_AB = V_A − V_B = 30 − 90 = −60 V.",
    ),
    inv(
        "In een homogeen veld van 4000 N/C liggen twee punten 3,0 cm uit elkaar, langs een veldlijn. Hoe groot is de spanning ertussen, in volt?",
        ["120", "120 V"],
        "U = E · d = 4000 · 0,030 = 120 V.",
    ),
    mk(
        "Een lading van 3,0 mC gaat vanzelf van een punt op 80 V naar een punt op 30 V. Hoeveel arbeid levert de elektrische kracht?",
        ["0,15 J", "0,33 J", "0,090 J", "150 J"],
        0,
        "W = q · U = 3,0 · 10⁻³ · 50 = 0,15 J.",
    ),
    inv(
        "Een lading van 4,0 µC zit in een punt met V = 250 V. Hoe groot is haar potentiële energie, in mJ?",
        ["1", "1,0", "1 mJ", "1,0 mJ"],
        "E_p = q · V = 4,0 · 10⁻⁶ · 250 = 1,0 · 10⁻³ J = 1,0 mJ.",
    ),
    tabel(
        "Klopt deze uitspraak over potentiaal en spanning?",
        [
            ("Een positieve lading beweegt vanzelf naar een lagere potentiaal.", J),
            ("Een elektron beweegt vanzelf naar een hogere potentiaal.", J),
            ("De arbeid van de elektrische kracht hangt af van de gevolgde weg.", F),
            ("Loodrecht op de veldlijnen verplaatsen kost arbeid.", F),
        ],
        "Alleen begin- en eindpunt tellen; langs een equipotentiaallijn is W = 0.",
    ),
    sorteer(
        "Hangt deze grootheid af van de lading die je in het punt zet?",
        ["Hangt af van q", "Eigenschap van het punt"],
        [
            ("de potentiële energie E_p", "Hangt af van q"),
            ("de potentiaal V", "Eigenschap van het punt"),
            ("de veldsterkte E", "Eigenschap van het punt"),
            ("de kracht F", "Hangt af van q"),
        ],
        "V = E_p / q en E = F / q: delen door q maakt er een eigenschap van de plaats van.",
    ),
    koppel(
        "Koppel elke grootheid aan de formule die erbij hoort.",
        [
            ("potentiaal V", "E_p / q"),
            ("spanning U_AB", "V_A − V_B"),
            ("arbeid W van het veld", "q · U"),
            ("veldsterkte E in een homogeen veld", "U / d"),
        ],
        ["F · q"],
        "Zo hangen veld, potentiaal en energie samen.",
    ),
    volgorde(
        "Zet de stappen in volgorde om de eindsnelheid van een lading te vinden die uit rust een spanning doorloopt.",
        [
            "Spanning U en lading q opzoeken",
            "Gewonnen energie berekenen met q · U",
            "Die energie gelijkstellen aan ½ · m · v²",
            "Oplossen naar v",
        ],
        "Alle verloren potentiële energie wordt kinetische energie.",
    ),
    casus(
        "In een elektronenkanon versnelt een spanning van 2000 V elektronen die uit rust vertrekken.",
        [
            inv(
                "Hoeveel elektronvolt kinetische energie heeft een elektron op het einde?",
                ["2000", "2000 eV", "2 keV"],
                "Eén elementaire lading door 2000 V: 2000 eV.",
            ),
            mk(
                "Hoeveel joule is dat? Neem 1 eV = 1,6 · 10⁻¹⁹ J.",
                ["3,2 · 10⁻¹⁶ J", "1,6 · 10⁻¹⁶ J", "3,2 · 10⁻²² J", "1,25 · 10²² J"],
                0,
                "2000 · 1,6 · 10⁻¹⁹ = 3,2 · 10⁻¹⁶ J.",
            ),
            keuze(
                "Bij 4000 V wordt de kinetische energie [[*twee keer|vier keer]] zo groot.",
                "E_k = e · U is recht evenredig met U.",
            ),
            mk(
                "Met welke factor wordt de snelheid dan groter?",
                ["√2", "2", "4", "½"],
                0,
                "E_k ~ v², dus twee keer zoveel energie geeft √2 ≈ 1,41 keer zo snel.",
            ),
        ],
    ),
    mk(
        "Tussen twee punten meet je U = 0. Wat weet je zeker?",
        [
            "Ze hebben dezelfde potentiaal",
            "Er is in die punten helemaal geen lading",
            "Er is daar geen elektrisch veld in de buurt",
            "Er loopt een grote stroom tussen die punten",
        ],
        0,
        "U is een verschil; beide punten kunnen samen op 500 V staan.",
    ),
    sleep(
        "Een positieve lading beweegt vanzelf van [[hoge]] naar [[lage]] potentiaal. Equipotentiaallijnen staan [[loodrecht]] op de veldlijnen.",
        ["evenwijdig", "nul"],
        "Langs een equipotentiaallijn verricht het veld geen arbeid.",
    ),
    open_(
        "Leg uit waarom je een lading langs een equipotentiaallijn kan verschuiven zonder arbeid te leveren.",
        "Op een equipotentiaallijn is de potentiaal overal dezelfde. De potentiële energie E_p = q · V verandert dus niet. Dat kan alleen als de elektrische kracht loodrecht staat op de verplaatsing, en dan verricht ze geen arbeid.",
    ),
]
