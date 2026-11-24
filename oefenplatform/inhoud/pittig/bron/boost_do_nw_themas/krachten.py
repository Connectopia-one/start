"""Vrije val, verticale worp en krachten — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, assen

# Krachten op een auto ---------------------------------------------------
KR = Prent("krachten-auto", "Krachten op een auto die met constante snelheid rijdt", "auto met vier krachtpijlen A tot D")
KR.lijn(60, 470, 940, 470, DONKER, 3)
KR.rect(330, 300, 340, 120, "#d6e6f2", DONKER, 20)
KR.rect(400, 240, 200, 70, "#d6e6f2", DONKER, 16)
KR.cirkel(400, 440, 32, "#555555"); KR.cirkel(600, 440, 32, "#555555")
KR.cirkel(500, 360, 6, DONKER, DONKER)
KR.tekst(810, 230, "rijrichting →", 20)
PIJL = {"A": ((500, 360), (500, 560), ROOD), "B": ((500, 470), (500, 140), GROEN),
        "C": ((670, 400), (880, 400), BLAUW), "D": ((330, 400), (120, 400), ORANJE)}
for letter, ((x1, y1), (x2, y2), k) in PIJL.items():
    KR.pijl(x1, y1, x2, y2, k, 6)
POS = {"A": (540, 560), "B": (540, 150), "C": (880, 360), "D": (120, 360)}
ZP = {}
for letter, (x, y) in POS.items():
    KR.letter(x, y, letter)
    (x1, y1), (x2, y2), _ = PIJL[letter]
    ZP[letter] = [Prent.rond(x, y, 26)]
ZP["A"].append(Prent.zone(470, 475, 60, 95))
ZP["B"].append(Prent.zone(470, 130, 60, 220))
ZP["C"].append(Prent.zone(670, 380, 220, 40))
ZP["D"].append(Prent.zone(110, 380, 220, 40))

# Twee veren -------------------------------------------------------------
VE = Prent("twee-veren", "Kracht en uitrekking van twee veren", "F(Δl)-grafiek van veer A (stug) en veer B (slap)")
X, Y = assen(VE, 0, 10, 0, 50, "Δl (cm)", "F (N)", 1, 10)
VE.pad(f"M{X(0)} {Y(0)} L {X(8)} {Y(40)}", "none", BLAUW, 5)
VE.pad(f"M{X(0)} {Y(0)} L {X(10)} {Y(20)}", "none", ORANJE, 5)
VE.letter(X(8) + 30, Y(40), "A")
VE.letter(X(10) - 10, Y(20) - 40, "B")
Z_A = [Prent.zone(X(4), Y(28), X(8) - X(4) + 60, Y(14) - Y(28)), Prent.rond(X(8) + 30, Y(40), 28)]
Z_B = [Prent.zone(X(5), Y(14), X(10) - X(5), Y(6) - Y(14)), Prent.rond(X(10) - 10, Y(20) - 40, 28)]

VRAGEN = [
    klik(
        "Klik op de normaalkracht.",
        KR.bestand, ZP["B"],
        "De weg duwt loodrecht terug op de auto: naar boven.",
    ),
    klik(
        "Klik op de veldkracht, die zonder contact werkt.",
        KR.bestand, ZP["A"],
        "De zwaartekracht grijpt aan in het zwaartepunt en wijst naar beneden.",
    ),
    klik(
        "Klik op de wrijvingskracht.",
        KR.bestand, ZP["D"],
        "Wrijving werkt tegengesteld aan de beweging, hier naar achteren.",
    ),
    met_prent(KR.bestand, tabel(
        "De auto rijdt met constante snelheid. Klopt dit?",
        [
            ("Pijl C en pijl D zijn even lang.", J),
            ("Pijl A en pijl B zijn even groot.", J),
            ("De resulterende kracht is nul.", J),
            ("Pijl C moet langer zijn dan pijl D om te blijven rijden.", F),
        ],
        "Bij een constante snelheid in een rechte lijn heffen alle krachten elkaar op: krachtenbalans.",
    )),
    met_prent(KR.bestand, keuze(
        "De bestuurder remt. Dan wordt pijl [[*D|C|B]] groter dan pijl C, en de auto vertraagt.",
        "Bij vertragen werkt de resulterende kracht tegengesteld aan de beweging.",
    )),
    klik(
        "Klik op de stugste veer.",
        VE.bestand, Z_A,
        "Bij dezelfde uitrekking levert veer A meer kracht: grotere veerconstante.",
    ),
    met_prent(VE.bestand, inv(
        "Kijk naar de grafiek. Wat is de veerconstante van veer A, in N/cm?",
        ["5"],
        "40 N bij 8 cm: 40 : 8 = 5 N/cm.",
    )),
    met_prent(VE.bestand, inv(
        "Kijk naar de grafiek. Hoeveel cm rekt veer B uit bij een kracht van 10 N?",
        ["5"],
        "Veer B levert 20 N bij 10 cm, dus 2 N/cm. 10 N geeft 5 cm.",
    )),
    met_prent(VE.bestand, tabel(
        "Kijk naar de grafiek. Klopt dit?",
        [
            ("Kracht en uitrekking zijn recht evenredig.", J),
            ("Veer B rekt bij dezelfde kracht meer uit dan A.", J),
            ("Veer B heeft de grootste veerconstante.", F),
            ("Een dynamometer werkt met zo'n veer.", J),
        ],
        "Een slappe veer heeft een kleine veerconstante.",
    )),
    casus(
        "Lotte gooit een bal recht naar boven. Hij stijgt, staat even stil in het hoogste punt en valt terug. Je verwaarloost de luchtweerstand.",
        [
            tabel(
                "Klopt dit over de bal?",
                [
                    ("In het hoogste punt is de snelheid nul.", J),
                    ("In het hoogste punt is de versnelling nul.", F),
                    ("Tijdens het stijgen wijst de versnelling naar beneden.", J),
                    ("Tijdens het vallen is de versnelling groter dan tijdens het stijgen.", F),
                ],
                "De zwaartekracht stopt geen moment. De versnelling is altijd de valversnelling, naar beneden.",
            ),
            keuze(
                "Het stijgen heet een [[*verticale worp|vrije val|krachtenbalans]], het terugvallen een vrije val.",
                "De versnelling is in beide fasen dezelfde.",
            ),
        ],
    ),
    inv(
        "Een steen valt uit stilstand. Hoe snel valt hij na 3 s, met g = 10 m/s²? Antwoord in m/s.",
        ["30"],
        "v = g · t = 10 · 3 = 30 m/s.",
    ),
    tabel(
        "Werkt deze kracht met of zonder contact?",
        [
            ("zwaartekracht", "Zonder contact"),
            ("normaalkracht", "Met contact"),
            ("wrijvingskracht", "Met contact"),
            ("spankracht in een touw", "Met contact"),
        ],
        "De zwaartekracht is een veldkracht.",
        kolommen=["Met contact", "Zonder contact"],
    ),
    tabel(
        "Hoe groot is de resultante?",
        [
            ("30 N en 40 N in dezelfde zin", "70 N"),
            ("30 N en 40 N loodrecht op elkaar", "50 N"),
            ("40 N en 40 N in tegengestelde zin", "0 N"),
            ("40 N en 30 N in tegengestelde zin", "10 N"),
        ],
        "Dezelfde zin: optellen. Tegengesteld: aftrekken. Loodrecht: stelling van Pythagoras.",
        kolommen=["70 N", "50 N", "10 N", "0 N"],
    ),
    inv(
        "Twee krachten van 6 N en 8 N werken loodrecht op elkaar in hetzelfde punt. Hoe groot is de resultante, in N?",
        ["10"],
        "√(6² + 8²) = √100 = 10 N.",
    ),
    tabel(
        "Massa of gewicht?",
        [
            ("blijft gelijk op de maan", "Massa"),
            ("meet je in newton", "Gewicht"),
            ("hoeveelheid materie", "Massa"),
            ("is op de maan kleiner", "Gewicht"),
            ("meet je in kilogram", "Massa"),
        ],
        "Gewicht is een kracht. Massa verandert niet van plaats tot plaats.",
        kolommen=["Massa", "Gewicht"],
    ),
    inv(
        "Een rugzak van 8 kg. Hoe groot is de zwaartekracht erop, met 10 N/kg? Antwoord in newton.",
        ["80"],
        "F = m · g = 8 · 10 = 80 N.",
    ),
    inv(
        "Een veer heeft een veerconstante van 4 N/cm. Hoeveel cm rekt ze uit als er 2 kg aan hangt, met 10 N/kg?",
        ["5"],
        "De zwaartekracht is 20 N. In evenwicht is de veerkracht ook 20 N: 20 : 4 = 5 cm.",
    ),
    casus(
        "Een parachutist springt uit een vliegtuig. Eerst gaat hij steeds sneller, daarna valt hij met een constante snelheid.",
        [
            mk(
                "Waarom valt hij na een tijd met constante snelheid?",
                [
                    "De luchtweerstand is even groot als de zwaartekracht",
                    "De zwaartekracht valt hoog in de lucht helemaal weg",
                    "Zijn massa wordt tijdens de val een heel stuk kleiner",
                    "De luchtweerstand is veel groter dan de zwaartekracht",
                ],
                0,
                "Krachtenbalans: de resulterende kracht is nul, dus geen versnelling meer.",
            ),
            keuze(
                "In het begin is de zwaartekracht [[*groter dan|even groot als|kleiner dan]] de luchtweerstand.",
                "Daarom versnelt hij eerst.",
            ),
        ],
    ),
    tabel(
        "Kan een resulterende kracht dit veroorzaken?",
        [
            ("een voorwerp versnellen", J),
            ("een voorwerp van richting doen veranderen", J),
            ("een voorwerp van vorm doen veranderen", J),
            ("de massa van een voorwerp groter maken", F),
        ],
        "Een kracht verandert de beweging of de vorm, niet de hoeveelheid materie.",
    ),
    koppel(
        "Koppel elke grootheid aan haar eenheid.",
        [
            ("kracht", "newton"),
            ("massa", "kilogram"),
            ("zwaarteveldsterkte", "newton per kilogram"),
            ("valversnelling", "meter per seconde kwadraat"),
        ],
        ["meter per seconde"],
        "Meter per seconde is de eenheid van snelheid.",
    ),
    sleep(
        "Een astronaut zweeft in een ruimtestation. Zijn [[massa]] is dezelfde als op aarde. Op de maan is de [[zwaarteveldsterkte]] veel kleiner, dus ook zijn [[gewicht]].",
        ["veerconstante", "snelheid"],
        "Gewichtloos zijn is niet massaloos zijn.",
    ),
    inv(
        "Een maanrover heeft een massa van 200 kg. Hoe groot is zijn gewicht op de maan, met 1,62 N/kg? Antwoord in newton.",
        ["324"],
        "G = m · g = 200 · 1,62 = 324 N. Op aarde zou dat ongeveer 2000 N zijn.",
    ),
    inv(
        "Je schiet een pijl recht omhoog met 20 m/s. Na hoeveel seconden bereikt hij het hoogste punt, met g = 10 m/s²?",
        ["2"],
        "Elke seconde verliest hij 10 m/s. Na 2 s is de snelheid nul.",
    ),
    volgorde(
        "Zet in de juiste volgorde: je meet het gewicht van een etui met een dynamometer.",
        [
            "Controleer of de dynamometer op nul staat zonder last",
            "Hang de etui aan het haakje",
            "Wacht tot de veer stilhangt",
            "Lees de kracht af in newton",
        ],
        "Eerst nulstand, dan pas meten en aflezen als alles in evenwicht is.",
    ),
    sorteer(
        "Sorteer: werkt deze kracht naar boven of naar beneden?",
        ["Naar boven", "Naar beneden"],
        [
            ["de spankracht in het touw van een hangende lamp", "Naar boven"],
            ["het gewicht van een boek op een plank", "Naar beneden"],
            ["de normaalkracht van een vloer op een kast", "Naar boven"],
            ["de zwaartekracht op een vallende appel", "Naar beneden"],
            ["de luchtweerstand op een dalende parachutist", "Naar boven"],
        ],
        "Kijk telkens wie op wie duwt of trekt.",
    ),
    tabel(
        "Een kist staat stil op een helling. Klopt dit?",
        [
            ("De wrijvingskracht houdt de kist tegen.", J),
            ("De wrijvingskracht wijst de helling op.", J),
            ("Er werkt geen zwaartekracht omdat de kist stilstaat.", F),
            ("De resulterende kracht op de kist is nul.", J),
        ],
        "Zonder wrijving zou de kist naar beneden glijden. Stilstaan betekent krachtenbalans.",
    ),
    keuze(
        "Het punt waar je de zwaartekracht op een voorwerp tekent, heet het [[*zwaartepunt|steunpunt|draaipunt]].",
        "In dat punt kan je je de hele massa geconcentreerd denken.",
    ),
    open_(
        "Leg uit waarom een steen en een pluim in een vacuümbuis even snel vallen, maar in de lucht niet.",
        "In een vacuüm werkt enkel de zwaartekracht. De valversnelling is voor elke massa dezelfde, dus vallen ze even snel. In de lucht werkt ook de luchtweerstand. Die remt de lichte pluim veel meer af dan de steen.",
    ),
]
