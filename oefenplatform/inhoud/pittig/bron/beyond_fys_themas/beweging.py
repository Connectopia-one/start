"""Rechtlijnige beweging: ERB en EVRB — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen


def _grafiek(p, X, Y, pts, labels):
    p.pad("M " + " L ".join(f"{X(t):.1f} {Y(v):.1f}" for t, v in pts), "none", BLAUW, 4)
    zones = {}
    for k, ((t1, v1), (t2, v2)), (dx, dy) in zip("ABCD", zip(pts, pts[1:]), labels):
        tm, vm = (t1 + t2) / 2, (v1 + v2) / 2
        lx, ly = X(tm) + dx, Y(vm) + dy
        p.letter(lx, ly, k)
        zones[k] = [Prent.zone(X(t1) - 4, min(Y(v1), Y(v2)) - 16, X(t2) - X(t1) + 8, abs(Y(v1) - Y(v2)) + 32), Prent.rond(lx, ly, 24)]
    return zones


XT = Prent("x-t-grafiek", "De plaats van een wagentje in de tijd", "x(t)-grafiek: A stijgt van 0 naar 40 m tussen 0 en 4 s, B blijft 40 m tot 6 s, C stijgt naar 80 m tot 8 s, D daalt naar 40 m tot 12 s")
X1, Y1 = assen(XT, 0, 12, 0, 100, "t (s)", "x (m)", 1, 20, links=130, rechts=900)
ZX = _grafiek(XT, X1, Y1, [(0, 0), (4, 40), (6, 40), (8, 80), (12, 40)], [(-34, -6), (0, -34), (-34, -6), (30, -20)])

VT = Prent("v-t-grafiek", "De snelheid van een fietser in de tijd", "v(t)-grafiek: A stijgt van 0 naar 12 m/s tussen 0 en 4 s, B blijft 12 m/s tot 10 s, C daalt naar 0 tussen 10 en 13 s")
X2, Y2 = assen(VT, 0, 14, 0, 15, "t (s)", "v (m/s)", 1, 3, links=130, rechts=900)
ZV = _grafiek(VT, X2, Y2, [(0, 0), (4, 12), (10, 12), (13, 0)], [(-34, -6), (0, -34), (34, -6)])

VRAGEN = [
    klik(
        "Klik op het stuk waarin het wagentje stilstaat.",
        XT.bestand, ZX["B"],
        "De plaats verandert niet: de helling, en dus v, is nul.",
    ),
    klik(
        "Klik op het stuk waarin het wagentje terugrijdt.",
        XT.bestand, ZX["D"],
        "Daar daalt x: de helling en dus v zijn negatief.",
    ),
    klik(
        "Klik op het stuk waarin het wagentje het snelst rijdt.",
        XT.bestand, ZX["C"],
        "C: 40 m in 2 s = 20 m/s. A en D: 10 m/s.",
    ),
    met_prent(XT.bestand, mk(
        "Hoe groot zijn de afgelegde weg s en de verplaatsing Δx over de hele rit van 12 s?",
        ["s = 120 m en Δx = 40 m", "s = 40 m en Δx = 120 m", "s = 80 m en Δx = 80 m", "s = 120 m en Δx = 120 m"],
        0,
        "s = 40 + 0 + 40 + 40 = 120 m. Δx = 40 m − 0 m = 40 m.",
    )),
    met_prent(XT.bestand, inv(
        "Hoe groot is de gemiddelde snelheid over de afgelegde weg in de hele rit van 12 s, in m/s?",
        ["10", "10 m/s"],
        "v_gem = s / Δt = 120 m / 12 s = 10 m/s.",
    )),
    met_prent(XT.bestand, tabel(
        "Hoe groot is de snelheid in dit stuk?",
        [
            ("A", "10 m/s"),
            ("B", "0"),
            ("D", "−10 m/s"),
        ],
        "v is de helling Δx / Δt; terugrijden geeft een negatieve v.",
        kolommen=["−10 m/s", "0", "10 m/s"],
    )),
    klik(
        "Klik op het stuk waarin de fietser vertraagt.",
        VT.bestand, ZV["C"],
        "De snelheid daalt: a is tegengesteld aan v.",
    ),
    klik(
        "Klik op het stuk met een eenparig rechtlijnige beweging.",
        VT.bestand, ZV["B"],
        "Constante snelheid: horizontaal op een v(t)-grafiek.",
    ),
    met_prent(VT.bestand, tabel(
        "Hoe groot is de versnelling in dit stuk?",
        [
            ("A", "3,0 m/s²"),
            ("B", "0"),
            ("C", "−4,0 m/s²"),
        ],
        "a is de helling van de v(t)-grafiek: 12 / 4 en −12 / 3.",
        kolommen=["−4,0 m/s²", "0", "3,0 m/s²"],
    )),
    met_prent(VT.bestand, inv(
        "Hoeveel meter legt de fietser in totaal af in de 13 s?",
        ["114", "114 m"],
        "Oppervlakte: ½ · 4 · 12 + 6 · 12 + ½ · 3 · 12 = 24 + 72 + 18 = 114 m.",
    )),
    met_prent(VT.bestand, keuze(
        "In stuk C rijdt de fietser [[*nog vooruit|al achteruit]].",
        "v is er nog positief, alleen kleiner wordend.",
    )),
    inv(
        "Hoeveel km/h is 25 m/s?",
        ["90", "90 km/h"],
        "Vermenigvuldig met 3,6: 25 · 3,6 = 90 km/h.",
    ),
    mk(
        "Je rijdt 30 km aan 60 km/h en daarna 30 km aan 30 km/h. Hoe groot is je gemiddelde snelheid?",
        ["40 km/h", "45 km/h", "50 km/h", "35 km/h"],
        0,
        "Tijd: 0,5 h + 1,0 h = 1,5 h voor 60 km, dus 40 km/h. Het tweede stuk duurt langer en weegt zwaarder.",
    ),
    inv(
        "Twee wagens rijden naar elkaar toe op 300 m afstand, met 20 m/s en 10 m/s. Na hoeveel seconden kruisen ze elkaar?",
        ["10", "10 s"],
        "Samen naderen ze met 30 m/s: 300 / 30 = 10 s.",
    ),
    mk(
        "Hoe ver valt een steen in 4,0 s vrije val? Neem g = 9,81 m/s².",
        ["ongeveer 78 m", "ongeveer 39 m", "ongeveer 157 m", "ongeveer 20 m"],
        0,
        "h = ½ · g · t² = 0,5 · 9,81 · 16 ≈ 78 m.",
    ),
    mk(
        "Je laat een steen in een put vallen en ziet hem na 3,0 s onderaan. Hoe diep is de put? Neem g = 9,81 m/s².",
        ["ongeveer 44 m", "ongeveer 29 m", "ongeveer 88 m", "ongeveer 15 m"],
        0,
        "h = ½ · 9,81 · 9,0 ≈ 44 m.",
    ),
    inv(
        "Je gooit een bal met 14 m/s recht omhoog. Hoe hoog komt hij, in m? Neem g = 9,81 m/s² en rond af op een geheel getal.",
        ["10", "10 m", "10,0"],
        "v² = v₀² − 2 · g · h met v = 0: h = 14² / (2 · 9,81) ≈ 10 m.",
    ),
    inv(
        "Diezelfde bal (14 m/s omhoog): na hoeveel seconden is hij terug op werphoogte? Rond af op één decimaal.",
        ["2,9", "2,9 s", "2.9"],
        "Omhoog duurt 14 / 9,81 ≈ 1,43 s en naar beneden even lang: ≈ 2,9 s.",
    ),
    inv(
        "Een auto rijdt 72 km/h en remt met 5,0 m/s². Hoe lang is de remweg, in m?",
        ["40", "40 m"],
        "72 km/h = 20 m/s. Δx = v₀² / (2a) = 400 / 10 = 40 m.",
    ),
    mk(
        "Hoeveel keer zo lang wordt de remweg als je drie keer zo snel rijdt, met dezelfde remvertraging?",
        ["9 keer", "3 keer", "6 keer", "27 keer"],
        0,
        "Δx = v₀² / (2a): de snelheid staat in het kwadraat.",
    ),
    casus(
        "Een auto rijdt met 20 m/s voorbij een stilstaande motor. Op dat ogenblik vertrekt de motor met 2,5 m/s².",
        [
            inv(
                "Na hoeveel seconden haalt de motor de auto in?",
                ["16", "16 s"],
                "20 · t = ½ · 2,5 · t², dus t = 40 / 2,5 = 16 s.",
            ),
            inv(
                "Hoeveel meter hebben ze dan allebei afgelegd?",
                ["320", "320 m"],
                "20 · 16 = 320 m.",
            ),
            mk(
                "Hoe snel rijdt de motor op het moment dat hij de auto inhaalt?",
                ["40 m/s", "20 m/s", "16 m/s", "80 m/s"],
                0,
                "v = a · t = 2,5 · 16 = 40 m/s: dubbel zo snel als de auto.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een negatieve versnelling betekent altijd dat het lichaam vertraagt.", F),
            ("Zonder luchtweerstand vallen een zware en een lichte steen even snel.", J),
            ("In het hoogste punt van een verticale worp is de versnelling nul.", F),
            ("De afgelegde weg is nooit kleiner dan de grootte van de verplaatsing.", J),
        ],
        "In het hoogste punt is v = 0, maar a blijft g naar beneden.",
    ),
    sorteer(
        "Is dit een ERB of een EVRB (zonder luchtweerstand)?",
        ["ERB", "EVRB"],
        [
            ("een trein rijdt met constante snelheid rechtdoor", "ERB"),
            ("een steen valt vanuit stilstand", "EVRB"),
            ("een auto remt gelijkmatig af", "EVRB"),
            ("een bal wordt recht omhoog gegooid", "EVRB"),
            ("een roltrap brengt je met constante snelheid naar boven", "ERB"),
        ],
        "ERB: a = 0. EVRB: a constant en niet nul.",
    ),
    koppel(
        "Koppel elke eigenschap van een grafiek aan wat ze voorstelt.",
        [
            ("de helling van een x(t)-grafiek", "de snelheid"),
            ("de helling van een v(t)-grafiek", "de versnelling"),
            ("de oppervlakte onder een v(t)-grafiek", "de verplaatsing"),
            ("de oppervlakte onder een a(t)-grafiek", "de snelheidsverandering"),
        ],
        ["de massa"],
        "Helling: delen door Δt. Oppervlakte: vermenigvuldigen met Δt.",
    ),
    volgorde(
        "Zet de fasen van een bal die je recht omhoog gooit in volgorde.",
        [
            "De bal verlaat je hand met v₀ omhoog",
            "De snelheid omhoog neemt af",
            "In het hoogste punt is v nul",
            "De snelheid naar beneden neemt toe",
            "De bal komt met v₀ naar beneden terug op werphoogte",
        ],
        "De hele tijd is a = g naar beneden.",
    ),
    keuze(
        "Bij een EVRB vanuit rust is de x(t)-grafiek een [[*parabool|rechte]] en de v(t)-grafiek een [[parabool|*schuine rechte]].",
        "x = ½ · a · t² en v = a · t.",
    ),
    sleep(
        "Bij een [[ERB]] blijft de snelheid constant. Bij een [[EVRB]] blijft de versnelling constant. Bij een vrije val is die versnelling [[g]].",
        ["v", "nul"],
        "Op aarde is g ≈ 9,81 m/s².",
    ),
    open_(
        "Leg uit waarom een bal die je recht omhoog gooit in zijn hoogste punt toch een versnelling heeft, al staat hij even stil.",
        "Ook in het hoogste punt werkt de zwaartekracht. De versnelling is dus nog altijd g naar beneden. De snelheid is daar maar één ogenblik nul en verandert meteen verder: van omhoog naar omlaag. Snelheid nul betekent niet dat de snelheid niet verandert.",
    ),
]
