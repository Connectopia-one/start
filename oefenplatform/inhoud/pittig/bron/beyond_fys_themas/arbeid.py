"""Arbeid, energie en vermogen — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# F(x)-grafiek ---------------------------------------------------------------------
FX = Prent("kracht-weg-grafiek", "De kracht op een wagentje in functie van de verplaatsing", "F(x)-grafiek: stuk A stijgt van 0 naar 30 N tussen 0 en 2 m, stuk B blijft 30 N tot 5 m, stuk C daalt naar 0 tussen 5 en 6 m; de oppervlakten zijn licht gekleurd")
X, Y = assen(FX, 0, 7, 0, 40, "x (m)", "F (N)", 1, 10, links=130, rechts=900)
FX.svg(f'<path d="M {X(0)} {Y(0)} L {X(2)} {Y(30)} L {X(2)} {Y(0)} Z" fill="#f6c89f" fill-opacity="0.6"/>')
FX.svg(f'<path d="M {X(2)} {Y(0)} L {X(2)} {Y(30)} L {X(5)} {Y(30)} L {X(5)} {Y(0)} Z" fill="#bcd6ec" fill-opacity="0.6"/>')
FX.svg(f'<path d="M {X(5)} {Y(0)} L {X(5)} {Y(30)} L {X(6)} {Y(0)} Z" fill="#c7e3bf" fill-opacity="0.6"/>')
FX.pad(f"M {X(0)} {Y(0)} L {X(2)} {Y(30)} L {X(5)} {Y(30)} L {X(6)} {Y(0)}", "none", DONKER, 4)
FX.letter(X(1.4), Y(10), "A")
FX.letter(X(3.5), Y(15), "B")
FX.letter(X(5.3), Y(8), "C")
ZF = {
    "A": [Prent.zone(X(0.6), Y(18), X(2) - X(0.6), Y(0) - Y(18))],
    "B": [Prent.zone(X(2), Y(30), X(5) - X(2), Y(0) - Y(30))],
    "C": [Prent.zone(X(5), Y(20), X(5.7) - X(5), Y(0) - Y(20))],
}

# Achtbaan -------------------------------------------------------------------
AB = Prent("achtbaan", "Een karretje vertrekt uit rust in P en rijdt zonder wrijving over de baan", "een achtbaan met punten P (20 m hoog, start), Q (0 m, het laagste punt), R (10 m) en S (15 m); een hoogteschaal links")
HX = lambda h: 570 - h * 19  # noqa: E731
AB.lijn(100, HX(0), 100, HX(25), DONKER, 2)
for h in range(0, 26, 5):
    AB.lijn(94, HX(h), 106, HX(h), DONKER, 2)
    AB.tekst(86, HX(h) + 6, f"{h} m", 15, anker="end")
pad = f"M 140 {HX(20)} C 260 {HX(20)} 300 {HX(0)} 400 {HX(0)} C 500 {HX(0)} 520 {HX(10)} 600 {HX(10)} C 680 {HX(10)} 690 {HX(3)} 760 {HX(3)} C 830 {HX(3)} 840 {HX(15)} 900 {HX(15)} L 960 {HX(15)}"
AB.pad(pad, "none", DONKER, 5)
AB.lijn(100, HX(0) + 20, 980, HX(0) + 20, "#b9b9b9", 2)
PUNT = {"P": (140, 20), "Q": (400, 0), "R": (600, 10), "S": (900, 15)}
for k, (x, h) in PUNT.items():
    AB.cirkel(x, HX(h), 9, ORANJE, DONKER, 2)
    AB.letter(x, HX(h) - 38, k)
ZA = {k: [Prent.rond(x, HX(h), 26), Prent.rond(x, HX(h) - 38, 22)] for k, (x, h) in PUNT.items()}

VRAGEN = [
    klik(
        "Klik op het stuk van de grafiek waarin de kracht de meeste arbeid verricht.",
        FX.bestand, ZF["B"],
        "Arbeid is de oppervlakte: A = 30 J, B = 90 J, C = 15 J.",
    ),
    met_prent(FX.bestand, inv(
        "Hoeveel arbeid verricht de kracht over de hele 6 m, in J?",
        ["135", "135 J"],
        "½ · 2 · 30 + 3 · 30 + ½ · 1 · 30 = 30 + 90 + 15 = 135 J.",
    )),
    met_prent(FX.bestand, tabel(
        "Hoeveel arbeid verricht de kracht in dit stuk?",
        [
            ("A", "30 J"),
            ("B", "90 J"),
            ("C", "15 J"),
        ],
        "Een driehoek is ½ · basis · hoogte, een rechthoek basis · hoogte.",
        kolommen=["15 J", "30 J", "90 J"],
    )),
    met_prent(FX.bestand, keuze(
        "Stuk A past bij [[*een veer die je steeds verder uitrekt|een kracht die gelijk blijft]].",
        "Bij een veer groeit de kracht recht evenredig met de uitrekking: F = k · x.",
    )),
    klik(
        "Klik op het punt waar het karretje het snelst rijdt.",
        AB.bestand, ZA["Q"],
        "Daar is de hoogte het kleinst, dus is de meeste potentiële energie kinetisch geworden.",
    ),
    klik(
        "Klik op het punt waar de kinetische energie even groot is als de potentiële energie.",
        AB.bestand, ZA["R"],
        "Op 10 m is de helft van de 20 m hoogte-energie omgezet: E_k = m · g · 10 = E_p.",
    ),
    met_prent(AB.bestand, tabel(
        "Hoe snel rijdt het karretje in dit punt? Neem g = 10 m/s².",
        [
            ("Q", "20 m/s"),
            ("R", "14 m/s"),
            ("S", "10 m/s"),
        ],
        "v = √(2 · g · Δh), met Δh de hoogte onder P: 20 m, 10 m en 5 m.",
        kolommen=["10 m/s", "14 m/s", "20 m/s"],
    )),
    met_prent(AB.bestand, mk(
        "Zou het karretje over een top van 25 m geraken?",
        [
            "Nee, het komt nooit hoger dan 20 m",
            "Ja, als het snel genoeg rijdt in Q",
            "Ja, want het karretje is zwaar genoeg",
            "Nee, maar met meer massa wel",
        ],
        0,
        "Zonder aandrijving kan de totale energie niet groter worden dan m · g · 20 m.",
    )),
    met_prent(AB.bestand, keuze(
        "Met wrijving komt het karretje in Q [[*trager|sneller|even snel]] aan.",
        "Een deel van de energie wordt warmte.",
    )),
    inv(
        "Een kracht van 50 N trekt een slee 8,0 m ver, onder 60° met de verplaatsing. Hoeveel arbeid levert ze, in J? (cos 60° = 0,50)",
        ["200", "200 J"],
        "W = F · s · cos α = 50 · 8,0 · 0,50 = 200 J.",
    ),
    mk(
        "Een kraan tilt 500 kg in 20 s 12 m omhoog. Hoe groot is het vermogen? Neem g = 10 N/kg.",
        ["3,0 kW", "60 kW", "0,30 kW", "6,0 kW"],
        0,
        "W = m · g · h = 60 000 J, P = W / t = 3000 W.",
    ),
    inv(
        "Een pomp van 1,5 kW tilt water 10 m hoog. Hoeveel kg water pompt ze per minuut? Neem g = 10 N/kg en verwaarloos verliezen.",
        ["900", "900 kg"],
        "In 60 s levert ze 90 000 J = m · 10 · 10, dus m = 900 kg.",
    ),
    inv(
        "Hoeveel kinetische energie heeft een auto van 1500 kg die 72 km/h rijdt, in kJ?",
        ["300", "300 kJ"],
        "72 km/h = 20 m/s. E_k = ½ · 1500 · 400 = 300 000 J.",
    ),
    mk(
        "Je rijdt drie keer zo snel. Wat gebeurt er met je kinetische energie?",
        ["Ze wordt 9 keer zo groot", "Ze wordt 3 keer zo groot", "Ze wordt 6 keer zo groot", "Ze blijft gelijk"],
        0,
        "E_k = ½ · m · v²: de snelheid staat in het kwadraat.",
    ),
    inv(
        "Een veer met k = 400 N/m wordt 10 cm ingedrukt. Hoeveel elastische energie zit erin, in J?",
        ["2", "2,0", "2 J", "2,0 J"],
        "E_p = ½ · k · x² = 0,5 · 400 · 0,010 = 2,0 J.",
    ),
    inv(
        "Een auto van 1000 kg remt van 20 m/s tot stilstand over 40 m. Hoe groot is de gemiddelde remkracht, in N?",
        ["5000", "5000 N", "5 kN", "5,0 kN"],
        "Arbeid-energietheorema: F · 40 = ½ · 1000 · 400 = 200 000 J, dus F = 5000 N.",
    ),
    mk(
        "Een toestel van 2000 W staat 3 uur aan. Hoeveel energie verbruikt het?",
        ["6 kWh", "6000 kWh", "0,67 kWh", "6 kW"],
        0,
        "E = P · t = 2 kW · 3 h = 6 kWh, of 2,16 · 10⁷ J.",
    ),
    inv(
        "Een bal valt van 2,0 m hoog en stuitert terug tot 1,5 m. Hoeveel procent van zijn energie is verloren gegaan?",
        ["25", "25 %", "25%"],
        "E_p is evenredig met h: 0,5 m van 2,0 m is 25 %.",
    ),
    mk(
        "Je gooit een bal omhoog en vangt hem op dezelfde hoogte weer op. Hoeveel arbeid verrichtte de zwaartekracht in totaal?",
        ["0 J", "m · g · 2h", "− m · g · h", "m · g · h"],
        0,
        "De zwaartekracht is conservatief: terug op het beginpunt is haar totale arbeid nul.",
    ),
    mk(
        "Twee motoren tillen dezelfde last even hoog. De ene doet er 10 s over, de andere 40 s. Wat klopt?",
        [
            "Evenveel arbeid, de eerste 4 keer meer vermogen",
            "De eerste levert 4 keer meer arbeid en meer vermogen",
            "Evenveel arbeid en ook evenveel vermogen",
            "De tweede levert meer arbeid omdat ze langer werkt",
        ],
        0,
        "W hangt niet af van de tijd; P = W / t wel.",
    ),
    casus(
        "Een slee van 40 kg vertrekt uit rust op een heuvel van 5,0 m hoog en komt beneden aan met 8,0 m/s. Neem g = 10 N/kg.",
        [
            inv(
                "Hoeveel potentiële energie had de slee bovenaan, in J?",
                ["2000", "2000 J", "2,0 kJ"],
                "E_p = m · g · h = 40 · 10 · 5,0 = 2000 J.",
            ),
            inv(
                "Hoeveel kinetische energie heeft ze beneden, in J?",
                ["1280", "1280 J"],
                "E_k = ½ · 40 · 64 = 1280 J.",
            ),
            inv(
                "Hoeveel energie werd onderweg warmte door de wrijving, in J?",
                ["720", "720 J"],
                "2000 − 1280 = 720 J: dat is de negatieve arbeid van de wrijving.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak over arbeid en energie?",
        [
            ("Wie een doos sneller optilt, levert een groter vermogen.", J),
            ("De kilowattuur is een eenheid van vermogen.", F),
            ("Kinetische energie kan negatief zijn.", F),
            ("De normaalkracht op een kist die over een vlakke vloer schuift, verricht geen arbeid.", J),
        ],
        "De kWh is energie: 1 kWh = 3,6 · 10⁶ J.",
    ),
    sorteer(
        "Is deze kracht conservatief of niet?",
        ["Conservatief", "Niet conservatief"],
        [
            ("de zwaartekracht", "Conservatief"),
            ("de veerkracht", "Conservatief"),
            ("de wrijvingskracht", "Niet conservatief"),
            ("de luchtweerstand", "Niet conservatief"),
            ("de elektrische kracht", "Conservatief"),
        ],
        "Bij een conservatieve kracht hangt de arbeid alleen af van begin- en eindpunt.",
    ),
    koppel(
        "Koppel elke energie aan haar formule.",
        [
            ("kinetische energie", "½ · m · v²"),
            ("gravitationele potentiële energie", "m · g · h"),
            ("elastische potentiële energie", "½ · k · x²"),
            ("arbeid van een constante kracht", "F · s · cos α"),
        ],
        ["m · a"],
        "Alles in joule.",
    ),
    volgorde(
        "Een pijl wordt recht omhoog geschoten met een boog. Zet de energievormen in de volgorde waarin ze het meest aanwezig zijn.",
        [
            "Elastische energie in de gespannen boog",
            "Kinetische energie van de vertrekkende pijl",
            "Potentiële energie in het hoogste punt",
            "Kinetische energie van de vallende pijl",
        ],
        "Zonder wrijving blijft de som de hele tijd gelijk.",
    ),
    sleep(
        "Het arbeid-energietheorema zegt dat de totale arbeid gelijk is aan de verandering van de [[kinetische]] energie. Vermogen is arbeid per [[seconde]], in [[watt]].",
        ["potentiële", "joule"],
        "1 W = 1 J/s.",
    ),
    open_(
        "Leg uit waarom een zware en een lichte slee zonder wrijving even snel beneden aankomen van dezelfde heuvel.",
        "Zonder wrijving wordt alle potentiële energie kinetische energie: m · g · h = ½ · m · v². De massa staat aan beide kanten en valt weg, zodat v = √(2 · g · h). De snelheid hangt dus alleen van de hoogte af.",
    ),
    keuze(
        "Bij een conservatieve kracht hangt de arbeid [[*alleen van begin- en eindpunt|ook van de gevolgde weg]] af.",
        "Daarom kan je er een potentiële energie aan koppelen.",
    ),
]
