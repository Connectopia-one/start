"""Harmonische trillingen — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# y(t) van één trilling ----------------------------------------------------------
YT = Prent("trilling-y-t", "De uitwijking van een trillend massa-veersysteem", "sinusgrafiek van de uitwijking in cm tegen de tijd in s, amplitude 4 cm, periode 0,8 s; punten P (t = 0,2 s, top), Q (t = 0,4 s, door de evenwichtslijn naar beneden), R (t = 0,6 s, dal) en S (t = 0,8 s, door de evenwichtslijn naar boven)")
X, Y = assen(YT, 0, 2.0, -5, 5, "t (s)", "y (cm)", 0.2, 1, links=130, rechts=900)
pts = [(i / 200 * 2.0, 4 * math.sin(2 * math.pi * (i / 200 * 2.0) / 0.8)) for i in range(201)]
YT.pad("M " + " L ".join(f"{X(a):.1f} {Y(b):.1f}" for a, b in pts), "none", BLAUW, 4)
PUNT = {"P": 0.2, "Q": 0.4, "R": 0.6, "S": 0.8}
LP = {}
for k, t in PUNT.items():
    y = 4 * math.sin(2 * math.pi * t / 0.8)
    YT.cirkel(X(t), Y(y), 8, ORANJE, DONKER, 2)
    LP[k] = (X(t) + 30, Y(y) + (-30 if y >= 0 else 30))
    YT.letter(*LP[k], k)
ZY = {k: [Prent.rond(X(t), Y(4 * math.sin(2 * math.pi * t / 0.8)), 24), Prent.rond(*LP[k], 22)] for k, t in PUNT.items()}

# Twee trillingen --------------------------------------------------------------
TT = Prent("twee-trillingen", "Telkens twee trillingen met dezelfde frequentie", "drie vakken A, B en C met elk een blauwe en een oranje sinus: in A vallen ze samen, in B is de ene het spiegelbeeld van de andere, in C loopt de oranje een kwart periode achter")
for i, (k, fase) in enumerate((("A", 0), ("B", math.pi), ("C", -math.pi / 2))):
    x0 = 50 + i * 315
    TT.rect(x0, 90, 290, 400, "#ffffff", DONKER, 14, 2)
    TT.lijn(x0 + 15, 290, x0 + 275, 290, GRIJS, 2)
    for kleur, ph, dik in ((BLAUW, 0, 5), (ORANJE, fase, 3)):
        p2 = [(x0 + 15 + j * 2.6, 290 - 120 * math.sin(2 * math.pi * j / 50 + ph)) for j in range(101)]
        TT.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in p2), "none", kleur, dik)
    TT.letter(x0 + 145, 550, k)
ZT = {k: [Prent.zone(50 + i * 315, 90, 290, 400), Prent.rond(50 + i * 315 + 145, 550, 26)] for i, k in enumerate("ABC")}

VRAGEN = [
    klik(
        "Klik op het punt waar het lichaam het snelst naar beneden beweegt.",
        YT.bestand, ZY["Q"],
        "In de evenwichtsstand is de snelheid het grootst; bij Q daalt de grafiek.",
    ),
    klik(
        "Klik op het punt waar de versnelling het grootst is en naar boven wijst.",
        YT.bestand, ZY["R"],
        "In de onderste stand trekt de terugroepkracht het hardst naar boven: a = −ω² · y.",
    ),
    met_prent(YT.bestand, tabel(
        "Wat weet je over de snelheid in dit punt?",
        [
            ("P", "Nul"),
            ("Q", "Maximaal"),
            ("R", "Nul"),
            ("S", "Maximaal"),
        ],
        "In de uiterste standen keert het lichaam om; door de evenwichtsstand gaat het het snelst.",
        kolommen=["Nul", "Maximaal"],
    )),
    met_prent(YT.bestand, inv(
        "Lees de amplitude af op de grafiek, in cm.",
        ["4", "4 cm", "4,0"],
        "De grootste uitwijking vanaf de evenwichtslijn.",
    )),
    met_prent(YT.bestand, inv(
        "Welke frequentie heeft deze trilling, in Hz?",
        ["1,25", "1,25 Hz", "1.25"],
        "T = 0,8 s, dus f = 1 / 0,8 = 1,25 Hz.",
    )),
    met_prent(YT.bestand, mk(
        "Hoe groot is de pulsatie ω?",
        ["7,9 rad/s", "1,25 rad/s", "0,80 rad/s", "5,0 rad/s"],
        0,
        "ω = 2π / T = 2π / 0,8 ≈ 7,9 rad/s.",
    )),
    met_prent(YT.bestand, inv(
        "Hoe groot is de uitwijking na 0,1 s, in cm? Rond af op één decimaal.",
        ["2,8", "2,8 cm", "2.8"],
        "y = 4 · sin(2π · 0,1 / 0,8) = 4 · sin(π/4) ≈ 2,8 cm.",
    )),
    klik(
        "Klik op het paar trillingen dat in tegenfase is.",
        TT.bestand, ZT["B"],
        "Als de ene in de top staat, staat de andere in het dal: Δφ = π rad.",
    ),
    klik(
        "Klik op het paar trillingen dat in fase is.",
        TT.bestand, ZT["A"],
        "Ze bereiken samen hun top en samen hun dal.",
    ),
    met_prent(TT.bestand, tabel(
        "Hoe groot is het faseverschil bij dit paar?",
        [
            ("A", "0"),
            ("B", "π rad"),
            ("C", "π/2 rad"),
        ],
        "Een kwart periode is een kwart van 2π.",
        kolommen=["0", "π/2 rad", "π rad"],
    )),
    mk(
        "Een massa van 0,50 kg hangt aan een veer met k = 200 N/m. Hoe groot is de eigenfrequentie?",
        ["3,2 Hz", "20 Hz", "0,32 Hz", "64 Hz"],
        0,
        "f₀ = 1/(2π) · √(k / m) = 1/(2π) · √400 = 20 / 2π ≈ 3,2 Hz.",
    ),
    mk(
        "Je maakt een slinger vier keer zo lang. Wat gebeurt er met de eigenfrequentie?",
        ["Ze wordt de helft", "Ze wordt een kwart", "Ze blijft gelijk", "Ze verdubbelt"],
        0,
        "f₀ ~ 1/√ℓ: √4 = 2.",
    ),
    inv(
        "Hoe groot is de periode van een slinger van 2,45 m, in s? Neem g = 9,81 m/s² en rond af op één decimaal.",
        ["3,1", "3,1 s", "3.1", "3,14"],
        "T = 2π · √(ℓ / g) = 2π · √0,25 ≈ 3,1 s.",
    ),
    mk(
        "Je hangt vier keer zoveel massa aan dezelfde veer. Wat gebeurt er met de eigenfrequentie?",
        ["Ze wordt de helft", "Ze wordt een kwart", "Ze verdubbelt", "Ze blijft gelijk"],
        0,
        "f₀ ~ √(k / m): √4 = 2 in de noemer.",
    ),
    mk(
        "Een veer rekt 10 cm uit als er 5,0 N aan trekt. Hoe groot is de krachtconstante?",
        ["50 N/m", "0,50 N/m", "2,0 N/m", "500 N/m"],
        0,
        "k = F / y = 5,0 / 0,10 = 50 N/m.",
    ),
    inv(
        "Een massa aan een veer met k = 50 N/m staat 4,0 cm onder de evenwichtsstand. Hoe groot is de terugroepkracht, in N?",
        ["2", "2,0", "2 N", "2,0 N"],
        "|F| = k · y = 50 · 0,040 = 2,0 N, naar boven gericht.",
    ),
    mk(
        "Twee trillingen hebben een periode van 0,8 s. De ene loopt 0,2 s voor op de andere. Hoe groot is het faseverschil?",
        ["π/2 rad", "π rad", "0,2 rad", "2π rad"],
        0,
        "0,2 s is een kwart periode, dus een kwart van 2π.",
    ),
    casus(
        "Een trilling volgt de vergelijking y = 0,03 · sin(10π · t), met y in meter en t in seconde.",
        [
            inv(
                "Hoe groot is de amplitude, in cm?",
                ["3", "3 cm", "3,0"],
                "A = 0,03 m = 3 cm.",
            ),
            inv(
                "Hoe groot is de frequentie, in Hz?",
                ["5", "5 Hz", "5,0"],
                "ω = 10π = 2π · f, dus f = 5 Hz.",
            ),
            mk(
                "Waar staat het lichaam op t = 0?",
                ["In de evenwichtsstand", "In de bovenste stand", "In de onderste stand", "Halfweg naar boven"],
                0,
                "De beginfase is nul en sin 0 = 0.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak over trillingen?",
        [
            ("Bij een slinger met kleine uitslag hangt de periode niet af van de massa.", J),
            ("Een trilling met een grotere frequentie heeft een grotere periode.", F),
            ("In de uiterste stand is de versnelling nul.", F),
            ("Bij demping verdwijnt energie als warmte naar de omgeving.", J),
        ],
        "In de uiterste stand is de terugroepkracht juist het grootst.",
    ),
    sorteer(
        "Gaat het om resonantie of om demping?",
        ["Resonantie", "Demping"],
        [
            ("een schommel die je op het juiste ritme steeds hoger duwt", "Resonantie"),
            ("een glas dat breekt door een zuivere, luide toon", "Resonantie"),
            ("een slinger die stilaan uitdooft", "Demping"),
            ("een schokbreker die een auto snel tot rust brengt", "Demping"),
        ],
        "Resonantie: de aandrijving past bij de eigenfrequentie. Demping haalt energie weg.",
    ),
    koppel(
        "Koppel elke grootheid van een trilling aan haar eenheid.",
        [
            ("amplitude A", "m"),
            ("periode T", "s"),
            ("frequentie f", "Hz"),
            ("pulsatie ω", "rad/s"),
        ],
        ["N/m"],
        "De beginfase staat in radiaal.",
    ),
    volgorde(
        "Een trilling vertrekt in de evenwichtsstand naar boven. Zet de standen van één periode in volgorde.",
        [
            "Evenwichtsstand, naar boven",
            "Bovenste stand",
            "Evenwichtsstand, naar beneden",
            "Onderste stand",
            "Evenwichtsstand, weer naar boven",
        ],
        "Na één periode begint alles opnieuw.",
    ),
    keuze(
        "Bij een gedempte trilling neemt vooral de [[*amplitude|frequentie]] af.",
        "Wrijving haalt energie weg; het ritme blijft ongeveer gelijk.",
    ),
    mk(
        "Met welke frequentie trilt een lichaam dat door een uitwendige kracht wordt aangedreven?",
        [
            "Met de frequentie van die kracht",
            "Altijd met zijn eigenfrequentie",
            "Met het gemiddelde van beide frequenties",
            "Met de dubbele eigenfrequentie",
        ],
        0,
        "Bij een gedwongen trilling neemt het lichaam de frequentie van de aandrijving over.",
    ),
    mk(
        "Waarom laat men soldaten niet in de pas over een lichte brug marcheren?",
        [
            "Hun ritme kan resonantie veroorzaken",
            "Ze zijn samen te zwaar voor elke brug",
            "De brug dempt hun stappen te sterk",
            "Ze verliezen zo het evenwicht op de brug",
        ],
        0,
        "Valt het ritme samen met de eigenfrequentie, dan groeit de amplitude gevaarlijk aan.",
    ),
    sleep(
        "Een harmonische trilling volgt y = A · sin(ω · t + [[φ]]). De kracht van de veer is een [[terugroepkracht]]. Bij [[resonantie]] wordt de amplitude heel groot.",
        ["demping", "T"],
        "F = −k · y wijst altijd naar de evenwichtsstand.",
    ),
    open_(
        "Leg uit waarom de snelheid van een trillend lichaam het grootst is in de evenwichtsstand.",
        "In de uiterste standen staat het lichaam even stil en zit alle energie in de veer. Op weg naar de evenwichtsstand duwt de terugroepkracht het lichaam steeds sneller. Voorbij de evenwichtsstand keert de kracht om en remt ze het lichaam af. De snelheid is dus maximaal precies in de evenwichtsstand.",
    ),
    keuze(
        "Verdubbel je de uitslag van een slinger, zolang die klein blijft, dan blijft de periode [[*ongeveer gelijk|twee keer zo lang|half zo lang]].",
        "f₀ = 1/(2π) · √(g / ℓ): de amplitude komt er niet in voor.",
    ),
]
