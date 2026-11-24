"""Arbeid, energie, vermogen en rendement — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Slinger met drie standen ----------------------------------------------
SL = Prent("slinger-drie-standen", "Een slinger in drie standen", "slinger met standen A (links hoog), B (laagste punt) en C (rechts hoog)")
OX, OY, L = 500, 110, 380
SL.rect(380, 90, 240, 20, "#c9b48a", DONKER, 4)
ST = {"A": -40, "B": 0, "C": 40}
for k, hoek in ST.items():
    x = OX + L * math.sin(math.radians(hoek))
    y = OY + L * math.cos(math.radians(hoek))
    SL.lijn(OX, OY, x, y, DONKER if k == "B" else GRIJS, 3, stippel=(k != "B"))
    SL.cirkel(x, y, 30, ORANJE if k == "B" else "#f3d3b4", DONKER)
    ST[k] = (x, y)
SL.pad(f"M{ST['A'][0]:.0f} {ST['A'][1]:.0f} Q {OX} {OY + L + 70} {ST['C'][0]:.0f} {ST['C'][1]:.0f}", "none", BLAUW, 2)
SL.lijn(150, OY + L, 850, OY + L, GRIJS, 1, stippel=True)
POSL = {"A": (ST["A"][0] - 70, ST["A"][1]), "B": (OX, OY + L + 70), "C": (ST["C"][0] + 70, ST["C"][1])}
ZS = {}
for k, (x, y) in POSL.items():
    SL.letter(x, y, k)
    ZS[k] = [Prent.rond(ST[k][0], ST[k][1], 36), Prent.rond(x, y, 26)]

# Stroomdiagram lamp -----------------------------------------------------
SD = Prent("stroomdiagram-lamp", "Energiestroom van een lamp per seconde", "stroomdiagram: 60 J elektrische energie in, pijl P 6 J licht, pijl Q 54 J warmte")
SD.rect(80, 220, 260, 180, "#f6e7a6", DONKER, 0)
SD.tekst(210, 300, "elektrische", 22, vet=True)
SD.tekst(210, 330, "energie 60 J", 22, vet=True)
SD.pad("M340 220 L 760 220 L 760 200 L 805 229 L 760 258 L 760 238 L 340 238 Z", "#fff4b0", DONKER, 2)
SD.pad("M340 238 L 340 400 L 520 400 Q 600 400 600 480 L 600 520 L 580 520 L 640 590 L 700 520 L 680 520 L 680 480 Q 680 238 340 238", "#f2b8a0", DONKER, 2)
SD.tekst(870, 237, "licht 6 J", 22)
SD.tekst(800, 560, "warmte 54 J", 22)
SD.letter(700, 190, "P")
SD.letter(470, 340, "Q")
ZSD = {"P": [Prent.zone(340, 195, 470, 60), Prent.rond(700, 190, 26)],
       "Q": [Prent.zone(400, 300, 300, 290), Prent.rond(470, 340, 26)]}

VRAGEN = [
    klik(
        "Klik op de stand waar de kinetische energie het grootst is.",
        SL.bestand, ZS["B"],
        "In het laagste punt is alle hoogte-energie omgezet in bewegingsenergie.",
    ),
    met_prent(SL.bestand, tabel(
        "Kijk naar de slinger. Je verwaarloost de wrijving. Klopt dit?",
        [
            ("In A is de snelheid nul.", J),
            ("In A en C is de hoogte-energie even groot.", J),
            ("In B is de totale energie het grootst.", F),
            ("Van B naar C wordt kinetische energie hoogte-energie.", J),
        ],
        "De som van de twee vormen blijft gelijk. Ze wisselen enkel van plaats.",
    )),
    met_prent(SL.bestand, keuze(
        "In het echt komt de slinger na een tijd tot stilstand. De energie is dan [[*omgezet in warmte|verdwenen|omgezet in massa]].",
        "Wrijving met de lucht en in het ophangpunt dissipeert de energie.",
    )),
    klik(
        "Klik op de ongewenste energie.",
        SD.bestand, ZSD["Q"],
        "Een lamp is bedoeld om licht te geven. De warmte is ongewenst.",
    ),
    met_prent(SD.bestand, inv(
        "Kijk naar het stroomdiagram. Hoeveel procent is het rendement van deze lamp?",
        ["10"],
        "6 : 60 = 0,1, dus 10 %.",
    )),
    met_prent(SD.bestand, inv(
        "Kijk naar het stroomdiagram. Wat is het vermogen van deze lamp, in watt?",
        ["60"],
        "Ze zet elke seconde 60 J om: 60 J/s = 60 W.",
    )),
    tabel(
        "Verricht deze kracht arbeid?",
        [
            ("je draagt een kist horizontaal door de gang", F),
            ("je tilt een kist van de grond op de tafel", J),
            ("je houdt een zware boodschappentas stil vast", F),
            ("een kraan hijst een balk omhoog", J),
        ],
        "Arbeid vraagt een verplaatsing in de richting van de kracht. Horizontaal dragen: de kracht staat loodrecht op de verplaatsing.",
    ),
    tabel(
        "Is de arbeid van deze kracht positief, negatief of nul?",
        [
            ("de wrijving op een schuivende slee", "Negatief"),
            ("de motorkracht van een versnellende auto", "Positief"),
            ("de normaalkracht op een rijdende trein", "Nul"),
            ("de zwaartekracht op een vallende appel", "Positief"),
        ],
        "Mee met de beweging: positief. Tegen de beweging: negatief. Loodrecht: nul.",
        kolommen=["Positief", "Negatief", "Nul"],
    ),
    inv(
        "Je trekt een slee 20 m ver met een kracht van 50 N in de bewegingsrichting. Hoeveel joule arbeid verricht je?",
        ["1000"],
        "W = F · s = 50 · 20 = 1000 J.",
    ),
    koppel(
        "Koppel elk voorbeeld aan de energievorm die erin opgeslagen zit.",
        [
            ("een opgespannen boog", "elastische potentiële energie"),
            ("water hoog in een stuwmeer", "gravitationele potentiële energie"),
            ("een rijdende fiets", "kinetische energie"),
            ("een boterham", "chemische energie"),
        ],
        ["stralingsenergie"],
        "Stralingsenergie zit in licht.",
    ),
    tabel(
        "Welke energieomzetting gebeurt hier vooral?",
        [
            ("een zonnepaneel", "stralingsenergie → elektrische energie"),
            ("een elektrische motor", "elektrische energie → kinetische energie"),
            ("een kampvuur", "chemische energie → warmte en licht"),
            ("een dynamo op een fiets", "kinetische energie → elektrische energie"),
        ],
        "Kijk wat erin gaat en wat er nuttig uitkomt.",
        kolommen=["stralingsenergie → elektrische energie", "elektrische energie → kinetische energie", "chemische energie → warmte en licht", "kinetische energie → elektrische energie"],
    ),
    tabel(
        "Open, gesloten of geïsoleerd systeem?",
        [
            ("een kookpot zonder deksel op het vuur", "Open"),
            ("een dichte blikken frisdrank in de koelkast", "Gesloten"),
            ("een ideale thermosfles die dicht is", "Geïsoleerd"),
        ],
        "Open: energie en materie. Gesloten: enkel energie. Geïsoleerd: geen van beide.",
        kolommen=["Open", "Gesloten", "Geïsoleerd"],
    ),
    inv(
        "Een rugzak van 5 kg ligt op een kast van 2 m hoog. Hoeveel joule hoogte-energie heeft hij, met 10 N/kg?",
        ["100"],
        "E = m · g · h = 5 · 10 · 2 = 100 J.",
    ),
    inv(
        "Een skateboarder van 50 kg rijdt met 4 m/s. Hoeveel joule kinetische energie heeft hij?",
        ["400"],
        "E = m · v² : 2 = 50 · 16 : 2 = 400 J.",
    ),
    casus(
        "Een knikker van 0,2 kg rolt zonder wrijving van een helling van 0,8 m hoog. Je rekent met 10 N/kg.",
        [
            inv(
                "Hoeveel joule hoogte-energie heeft de knikker bovenaan?",
                ["1,6", "1.6"],
                "0,2 · 10 · 0,8 = 1,6 J.",
            ),
            inv(
                "Hoe snel rolt hij onderaan, in m/s?",
                ["4"],
                "Alle 1,6 J wordt kinetische energie: 0,2 · v² : 2 = 1,6, dus v² = 16 en v = 4 m/s.",
            ),
            keuze(
                "Een knikker van 0,4 kg zou onderaan [[*even snel|twee keer zo snel|half zo snel]] rollen.",
                "De massa staat links en rechts in de energiebalans en valt dus weg.",
            ),
        ],
    ),
    tabel(
        "Een auto rijdt eerst 30 km/h en dan 60 km/h. Klopt dit?",
        [
            ("Zijn kinetische energie wordt vier keer zo groot.", J),
            ("Zijn kinetische energie wordt twee keer zo groot.", F),
            ("De remmen moeten dan meer energie in warmte omzetten.", J),
            ("Zijn massa wordt groter door de hogere snelheid.", F),
        ],
        "De snelheid staat in het kwadraat: 2² = 4.",
    ),
    inv(
        "Een veer met k = 200 N/m wordt 0,1 m ingedrukt. Hoeveel joule elastische energie zit erin?",
        ["1"],
        "E = k · u² : 2 = 200 · 0,01 : 2 = 1 J.",
    ),
    tabel(
        "Reken uit.",
        [
            ("1200 J in 4 s", "300 W"),
            ("3000 J in 10 s", "300 W"),
            ("600 J in 3 s", "200 W"),
            ("1000 J in 2 s", "500 W"),
        ],
        "Vermogen = energie : tijd.",
        kolommen=["200 W", "300 W", "500 W"],
    ),
    inv(
        "Een stofzuiger van 1500 W staat 2 uur aan. Hoeveel kilowattuur verbruikt hij?",
        ["3"],
        "1,5 kW · 2 h = 3 kWh.",
    ),
    tabel(
        "Eenheid van energie of van vermogen?",
        [
            ("joule", "Energie"),
            ("watt", "Vermogen"),
            ("kilowattuur", "Energie"),
            ("kilocalorie", "Energie"),
            ("kilowatt", "Vermogen"),
        ],
        "Kilowattuur is vermogen maal tijd, dus energie.",
        kolommen=["Energie", "Vermogen"],
    ),
    inv(
        "Een elektrische motor krijgt 800 J en levert 600 J beweging. Hoeveel procent is zijn rendement?",
        ["75"],
        "600 : 800 = 0,75, dus 75 %.",
    ),
    mk(
        "Een uitvinder zegt dat zijn machine een rendement van 110 % haalt. Wat is er mis?",
        [
            "Er kan niet meer nuttige energie uit dan er in gaat",
            "Een rendement druk je nooit in procent uit, maar altijd in joule",
            "Een machine heeft altijd een rendement van precies 100 %",
            "Een hoog rendement kan alleen bij een toestel met weinig vermogen",
        ],
        0,
        "Dat zou de wet van behoud van energie tegenspreken.",
    ),
    sleep(
        "Bij een waterkoker is de [[nuttige]] energie de warmte in het water. De warmte die naar de kamer gaat, is [[ongewenste]] energie. Het [[rendement]] is de verhouding van de nuttige tot de totale energie.",
        ["kinetische", "vermogen"],
        "Wat nuttig is, hangt af van waarvoor het toestel bedoeld is.",
    ),
    volgorde(
        "Zet de energieomzettingen in een waterkrachtcentrale in de juiste volgorde.",
        [
            "Water staat hoog in het stuwmeer",
            "Het water stroomt snel naar beneden",
            "Het water doet de turbine draaien",
            "De generator maakt elektrische energie",
        ],
        "Hoogte-energie wordt kinetische energie en dan elektrische energie.",
    ),
    met_prent(SD.bestand, inv(
        "Kijk naar het stroomdiagram. Hoeveel joule warmte geeft de lamp in één minuut?",
        ["3240"],
        "Elke seconde 54 J, en een minuut heeft 60 s: 54 · 60 = 3240 J.",
    )),
    inv(
        "Een bloempot van 2 kg valt van een balkon op 10 m hoogte. Hoeveel joule kinetische energie heeft hij net voor de grond? Je verwaarloost de luchtweerstand en rekent met 10 N/kg.",
        ["200"],
        "Alle hoogte-energie wordt kinetische energie: 2 · 10 · 10 = 200 J.",
    ),
    tabel(
        "Een waterkoker van 1000 W en een van 2000 W koken elk een liter water. Ze hebben hetzelfde rendement. Klopt dit?",
        [
            ("De waterkoker van 2000 W is ongeveer twee keer zo snel klaar.", J),
            ("Ze zetten allebei ongeveer evenveel energie om.", J),
            ("De waterkoker van 2000 W verbruikt dubbel zoveel energie.", F),
            ("Vermogen zegt hoe snel energie omgezet wordt.", J),
        ],
        "Zelfde energie in de helft van de tijd vraagt dubbel vermogen.",
    ),
    open_(
        "Leg uit waarom je fietsremmen warm worden als je een lange helling afrijdt en blijft remmen.",
        "Bij het dalen wordt hoogte-energie kinetische energie. Door te remmen verricht de wrijvingskracht negatieve arbeid. Zo wordt die energie omgezet in warmte in de remmen. De energie verdwijnt niet, ze verandert van vorm.",
    ),
]
