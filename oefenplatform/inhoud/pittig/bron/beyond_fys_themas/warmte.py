"""Warmteleer: temperatuur, warmte en faseovergangen — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Opwarmcurve van ijs -----------------------------------------------------------
OC = Prent("opwarmcurve-ijs", "Je voegt gelijkmatig warmte toe aan ijs van −20 °C", "grafiek van de temperatuur tegen de toegevoegde warmte: A stijgt van −20 naar 0 °C, B horizontaal op 0 °C, C stijgt van 0 naar 100 °C, D lang horizontaal op 100 °C, E stijgt boven 100 °C")
X, Y = assen(OC, 0, 10, -40, 140, "toegevoegde warmte", "θ (°C)", 1, 20, links=130, rechts=900)
PTS = [(0, -20), (0.8, 0), (2.0, 0), (3.4, 100), (8.8, 100), (9.6, 130)]
OC.pad("M " + " L ".join(f"{X(a):.1f} {Y(b):.1f}" for a, b in PTS), "none", ROOD, 4)
LAB = {"A": (40, 18), "B": (0, -32), "C": (-30, -6), "D": (0, -32), "E": (-30, -6)}
ZO = {}
for k, ((a1, b1), (a2, b2)) in zip("ABCDE", zip(PTS, PTS[1:])):
    lx, ly = X((a1 + a2) / 2) + LAB[k][0], Y((b1 + b2) / 2) + LAB[k][1]
    OC.letter(lx, ly, k)
    ZO[k] = [Prent.zone(X(a1) - 4, min(Y(b1), Y(b2)) - 16, X(a2) - X(a1) + 8, abs(Y(b1) - Y(b2)) + 32), Prent.rond(lx, ly, 24)]

# Faseovergangen -------------------------------------------------------------------
FO = Prent("faseovergangen", "De zes faseovergangen tussen vast, vloeibaar en gas", "drie vakken in een driehoek: vast linksonder, vloeibaar rechtsonder, gas bovenaan; zes pijlen A tot F, telkens een heen- en een terugpijl tussen twee fasen, zonder namen")
VAK = {"vast": (200, 500), "vloeibaar": (800, 500), "gas": (500, 140)}
for naam, (x, y) in VAK.items():
    FO.rect(x - 90, y - 40, 180, 80, "#f4f7fb", DONKER, 14, 2)
    FO.tekst(x, y + 8, naam, 24, vet=True)


def _pijl(a, b, zijde):
    (x1, y1), (x2, y2) = VAK[a], VAK[b]
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    px_, py_ = -uy * zijde, ux * zijde
    s, e = 120, n - 120
    return (x1 + ux * s + px_, y1 + uy * s + py_, x1 + ux * e + px_, y1 + uy * e + py_)


OVG = {
    "A": ("vast", "vloeibaar", 18),
    "B": ("vloeibaar", "vast", 18),
    "C": ("vloeibaar", "gas", 18),
    "D": ("gas", "vloeibaar", 18),
    "E": ("vast", "gas", -18),
    "F": ("gas", "vast", -18),
}
ZFO = {}
for k, (a, b, z) in OVG.items():
    x1, y1, x2, y2 = _pijl(a, b, z)
    FO.pijl(x1, y1, x2, y2, ORANJE, 4)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    nx, ny = (y2 - y1), -(x2 - x1)
    n = math.hypot(nx, ny)
    lx, ly = mx + nx / n * 32 * (1 if z > 0 else -1) * (-1), my + ny / n * 32 * (1 if z > 0 else -1) * (-1)
    FO.letter(lx, ly, k)
    ZFO[k] = [Prent.rond(mx, my, 30), Prent.rond(lx, ly, 22)]

VRAGEN = [
    klik(
        "Klik op het stuk waarin het ijs smelt.",
        OC.bestand, ZO["B"],
        "Op 0 °C blijft de temperatuur gelijk: alle warmte gaat naar het smelten.",
    ),
    klik(
        "Klik op het stuk dat de meeste warmte kost.",
        OC.bestand, ZO["D"],
        "Het koken op 100 °C: de verdampingswarmte van water is veel groter dan alles daarvoor.",
    ),
    klik(
        "Klik op het stuk waarin er alleen vloeibaar water is.",
        OC.bestand, ZO["C"],
        "Tussen 0 °C en 100 °C stijgt de temperatuur van het water.",
    ),
    met_prent(OC.bestand, tabel(
        "Welke fase(n) zijn er in dit stuk?",
        [
            ("A", "Alleen vast"),
            ("B", "Vast en vloeibaar"),
            ("D", "Vloeibaar en gas"),
        ],
        "Op een horizontaal stuk liggen twee fasen naast elkaar.",
        kolommen=["Alleen vast", "Vast en vloeibaar", "Vloeibaar en gas"],
    )),
    met_prent(OC.bestand, keuze(
        "Stuk D is veel langer dan stuk B omdat de verdampingswarmte van water [[*veel groter|veel kleiner]] is dan de smeltwarmte.",
        "2256 kJ/kg tegenover 334 kJ/kg.",
    )),
    klik(
        "Klik op de pijl die rijpen voorstelt.",
        FO.bestand, ZFO["F"],
        "Rijpen is van gas rechtstreeks naar vast, zoals de witte laag op een autoruit.",
    ),
    klik(
        "Klik op de pijl die sublimeren voorstelt.",
        FO.bestand, ZFO["E"],
        "Sublimeren is van vast rechtstreeks naar gas, zoals bij droogijs.",
    ),
    met_prent(FO.bestand, tabel(
        "Neemt deze overgang warmte op of geeft ze warmte af?",
        [
            ("A", "Neemt op"),
            ("B", "Geeft af"),
            ("D", "Geeft af"),
            ("E", "Neemt op"),
        ],
        "Naar een lossere fase kost warmte; naar een vastere fase komt warmte vrij.",
        kolommen=["Neemt op", "Geeft af"],
    )),
    inv(
        "Hoeveel warmte is nodig om 0,50 kg aluminium van 20 °C tot 80 °C op te warmen, in kJ? Neem c = 900 J/(kg·K).",
        ["27", "27 kJ"],
        "Q = c · m · ΔT = 900 · 0,50 · 60 = 27 000 J.",
    ),
    inv(
        "Je giet 2,0 kg water van 60 °C bij 1,0 kg water van 30 °C. Welke eindtemperatuur krijg je, in °C, zonder verliezen?",
        ["50", "50 °C"],
        "Afgegeven = opgenomen: 2,0 · (60 − θ) = 1,0 · (θ − 30), dus θ = 50 °C.",
    ),
    mk(
        "Hoeveel warmte heb je nodig om 0,25 kg water van 20 °C tot 100 °C te brengen? Neem c = 4186 J/(kg·K).",
        ["ongeveer 84 kJ", "ongeveer 105 kJ", "ongeveer 21 kJ", "ongeveer 335 kJ"],
        0,
        "Q = 4186 · 0,25 · 80 ≈ 83 700 J.",
    ),
    inv(
        "Hoeveel warmte is er nodig om 2,0 kg ijs van 0 °C te laten smelten, in kJ? Neem l = 334 kJ/kg.",
        ["668", "668 kJ"],
        "Q = l · m = 334 · 2,0 = 668 kJ.",
    ),
    inv(
        "Hoeveel kg ijs van 0 °C kan je laten smelten met 100,2 kJ? Neem l = 334 kJ/kg.",
        ["0,3", "0,30", "0,3 kg", "0,30 kg", "0.3"],
        "m = Q / l = 100,2 / 334 = 0,30 kg.",
    ),
    mk(
        "Hoeveel warmte kost het om 0,10 kg water van 100 °C te laten verdampen? Neem l = 2256 kJ/kg.",
        ["226 kJ", "33 kJ", "22 560 kJ", "42 kJ"],
        0,
        "Q = l · m = 2256 · 0,10 ≈ 226 kJ.",
    ),
    inv(
        "In een joulevat staat 12 V over de weerstand en loopt 2,0 A, gedurende 300 s. Hoeveel warmte krijgt het water, in J?",
        ["7200", "7200 J", "7,2 kJ"],
        "Q = U · I · t = 12 · 2,0 · 300 = 7200 J.",
    ),
    inv(
        "Een waterkoker van 2000 W warmt 1,0 kg water op van 20 °C tot 100 °C. Hoeveel seconden duurt dat zonder verliezen? Neem c = 4186 J/(kg·K) en rond af op een geheel getal.",
        ["167", "167 s", "168"],
        "Q = 4186 · 1,0 · 80 = 334 880 J; t = Q / P ≈ 167 s.",
    ),
    mk(
        "Hoe groot is de warmtecapaciteit van 2,0 kg water? Neem c = 4186 J/(kg·K).",
        ["8372 J/K", "2093 J/K", "4186 J/K", "8372 J/kg"],
        0,
        "C = c · m: de warmte voor dit hele voorwerp per kelvin.",
    ),
    casus(
        "Een blokje metaal van 0,20 kg en 100 °C valt in een calorimeter met 0,50 kg water van 20 °C. De eindtemperatuur is 24 °C. Neem c_water = 4186 J/(kg·K) en verwaarloos de calorimeter zelf.",
        [
            inv(
                "Hoeveel warmte nam het water op, in J?",
                ["8372", "8372 J", "8,4 kJ"],
                "Q = 4186 · 0,50 · 4 = 8372 J.",
            ),
            keuze(
                "Het metaal gaf [[*evenveel|meer|minder]] warmte af.",
                "In een goede calorimeter gaat er geen warmte verloren.",
            ),
            mk(
                "Hoe groot is de specifieke warmtecapaciteit van het metaal?",
                ["ongeveer 550 J/(kg·K)", "ongeveer 4186 J/(kg·K)", "ongeveer 110 J/(kg·K)", "ongeveer 2200 J/(kg·K)"],
                0,
                "8372 = c · 0,20 · 76, dus c ≈ 551 J/(kg·K).",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Zolang zuiver water kookt, stijgt zijn temperatuur niet.", J),
            ("Een stijging van 15 K is een stijging van 15 °C.", J),
            ("Bij een lagere druk kookt water bij een hogere temperatuur.", F),
            ("Een metalen pan warmt sneller op dan het water erin, door haar lage c.", J),
        ],
        "Op een berg, bij lagere druk, kookt water al onder 100 °C.",
    ),
    sorteer(
        "Neemt deze faseovergang warmte op of geeft ze warmte af?",
        ["Neemt op", "Geeft af"],
        [
            ("smelten", "Neemt op"),
            ("verdampen", "Neemt op"),
            ("sublimeren", "Neemt op"),
            ("stollen", "Geeft af"),
            ("condenseren", "Geeft af"),
            ("rijpen", "Geeft af"),
        ],
        "Elke overgang heeft een omgekeerde met dezelfde warmte, met het andere teken.",
    ),
    koppel(
        "Koppel elke manier van warmtetransport aan wat ze kenmerkt.",
        [
            ("geleiding", "door contact tussen de deeltjes"),
            ("stroming", "met een bewegende vloeistof of een gas"),
            ("straling", "ook door het luchtledige"),
        ],
        ["alleen in metalen"],
        "Daarom heeft een thermosfles een vacuüm én een spiegelende laag.",
    ),
    volgorde(
        "Je voegt warmte toe aan ijs van −10 °C tot je stoom van 110 °C hebt. Zet de stappen in volgorde.",
        [
            "Het ijs warmt op tot 0 °C",
            "Het ijs smelt",
            "Het water warmt op tot 100 °C",
            "Het water kookt",
            "De stoom warmt verder op",
        ],
        "Tijdens smelten en koken blijft de temperatuur gelijk.",
    ),
    mk(
        "Waarom gebruik je water als koelvloeistof in een motor?",
        [
            "Het neemt veel warmte op per graad",
            "Het geleidt elektrische stroom heel goed",
            "Het kookt al bij een lage temperatuur",
            "Het heeft een heel lage specifieke warmtecapaciteit",
        ],
        0,
        "Water heeft een hoge specifieke warmtecapaciteit.",
    ),
    mk(
        "Waaraan herken je een mengsel op een stolcurve?",
        [
            "Een schuin stuk waar een vlak stuk hoort",
            "Een horizontaal stuk dat precies op 0 °C ligt",
            "Een curve die eerst stijgt en dan daalt",
            "Twee horizontale stukken op dezelfde temperatuur",
        ],
        0,
        "Een mengsel stolt over een temperatuurgebied, niet op één punt.",
    ),
    mk(
        "Welke manier van warmtetransport werkt ook door een vacuüm?",
        ["Straling", "Geleiding", "Stroming", "Geen enkele"],
        0,
        "Zo komt de warmte van de zon tot bij ons.",
    ),
    keuze(
        "In een snelkookpan is de druk hoger, dus kookt water er bij een [[*hogere|lagere]] temperatuur dan 100 °C.",
        "Het kookpunt hangt af van de druk boven de vloeistof.",
    ),
    sleep(
        "Om een stof op te warmen heb je Q = c · m · [[ΔT]] nodig. Voor een faseovergang is dat Q = [[l]] · m. Warmte stroomt vanzelf van [[warm naar koud]].",
        ["koud naar warm", "v"],
        "Tijdens een faseovergang staat er geen ΔT in de formule.",
    ),
    open_(
        "Leg uit waarom zweten je lichaam afkoelt.",
        "Het zweet op je huid verdampt. Verdampen kost veel warmte, en die warmte komt voor een groot deel van je huid. Zo voert het verdampende zweet energie af en daalt de temperatuur van je huid.",
    ),
]
