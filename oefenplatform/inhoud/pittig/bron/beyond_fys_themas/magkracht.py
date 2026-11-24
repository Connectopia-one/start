"""De magnetische kracht op een stroom en op een lading — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Deeltjes in een veld het blad in --------------------------------------------
VB = Prent("banen-in-veld", "Deeltjes die met dezelfde snelheid een magnetisch veld binnenvliegen", "een vak met kruisjes: het veld wijst het blad in; links komen deeltjes naar rechts binnen; vier banen: P buigt in een grote bocht naar boven, S in een kleine bocht naar boven, Q gaat rechtdoor, R buigt in een grote bocht naar beneden")
VB.rect(300, 70, 640, 540, "#f4f7fb", DONKER, 10, 2)
for x in range(340, 940, 60):
    for y in range(100, 600, 60):
        VB.tekst(x, y + 7, "×", 22, kleur="#8a9bb0")
VB.tekst(620, 640 - 6, "B wijst het blad in", 18)
VB.pijl(80, 340, 300, 340, DONKER, 3)
VB.tekst(150, 320, "v", 22, vet=True)
Y0 = 340
BAAN = {"P": (260, -1), "S": (120, -1), "R": (260, 1)}
EIND = {}
for k, (r, zin) in BAAN.items():
    cx, cy = 300, Y0 + zin * r
    pts = []
    for i in range(0, 91, 3):
        h = math.radians(i)
        x = cx + r * math.sin(h)
        y = cy - zin * r * math.cos(h)
        if not (70 < y < 610 and x < 940):
            break
        pts.append((x, y))
    VB.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", {"P": ROOD, "S": PAARS, "R": BLAUW}[k], 4)
    EIND[k] = pts[-1]
VB.lijn(300, Y0, 930, Y0, GROEN, 4)
EIND["Q"] = (900, Y0)
LET = {"P": (EIND["P"][0] + 30, EIND["P"][1] + 10), "S": (EIND["S"][0] + 34, EIND["S"][1] + 6), "R": (EIND["R"][0] + 30, EIND["R"][1] - 10), "Q": (900, Y0 - 34)}
for k, (x, y) in LET.items():
    VB.letter(x, y, k)
ZV = {k: [Prent.rond(x, y, 28)] for k, (x, y) in LET.items()}

# Draad tussen de polen van een hoefijzermagneet -----------------------------
DP = Prent("draad-tussen-polen", "Een draad tussen de polen van een magneet, de stroom gaat het blad in", "boven een noordpool, onder een zuidpool; in het midden een draad loodrecht op het blad met de stroom het blad in; vier pijlen rond de draad: A naar links, B naar rechts, C naar boven, D naar beneden")
DP.rect(330, 70, 340, 90, ROOD, DONKER, 6, 2)
DP.tekst(500, 130, "N", 34, kleur="#ffffff", vet=True)
DP.rect(330, 520, 340, 90, BLAUW, DONKER, 6, 2)
DP.tekst(500, 580, "Z", 34, kleur="#ffffff", vet=True)
for x in (380, 440, 560, 620):
    DP.lijn(x, 165, x, 515, "#b9b9b9", 2)
    DP.pijl(x, 420, x, 440, "#9a9a9a", 2)
DP.cirkel(500, 340, 26, "#ffffff", DONKER, 3)
DP.lijn(484, 324, 516, 356, DONKER, 3)
DP.lijn(516, 324, 484, 356, DONKER, 3)
PIJL = {"A": (460, 340, 300, 340), "B": (540, 340, 700, 340), "C": (500, 300, 500, 200), "D": (500, 380, 500, 480)}
for k, (x1, y1, x2, y2) in PIJL.items():
    DP.pijl(x1, y1, x2, y2, ORANJE, 5)
LP = {"A": (270, 340), "B": (730, 340), "C": (550, 210), "D": (550, 470)}
for k, (x, y) in LP.items():
    DP.letter(x, y, k)
ZP = {k: [Prent.zone(min(PIJL[k][0], PIJL[k][2]) - 20, min(PIJL[k][1], PIJL[k][3]) - 20, abs(PIJL[k][2] - PIJL[k][0]) + 40, abs(PIJL[k][3] - PIJL[k][1]) + 40), Prent.rond(*LP[k], 26)] for k in PIJL}

VRAGEN = [
    klik(
        "P en R horen bij twee ionen met dezelfde massa, lading en snelheid, maar een tegengesteld teken. Klik op de baan van het negatieve ion.",
        VB.bestand, ZV["R"],
        "v naar rechts en B het blad in: op een positieve lading werkt de kracht naar boven, op een negatieve naar beneden.",
    ),
    klik(
        "P en S horen bij twee positieve ionen met dezelfde lading en snelheid. Klik op de baan van het lichtste ion.",
        VB.bestand, ZV["S"],
        "r = m · v / (q · B): een kleinere massa geeft een kleinere straal.",
    ),
    met_prent(VB.bestand, tabel(
        "Welke baan volgt dit deeltje?",
        [
            ("een neutron", "Q"),
            ("het positieve ion", "P"),
            ("het negatieve ion", "R"),
        ],
        "Zonder lading is er geen lorentzkracht; het teken van de lading bepaalt de kant.",
        kolommen=["P", "Q", "R"],
    )),
    met_prent(VB.bestand, mk(
        "Je maakt het veld twee keer zo sterk. Wat gebeurt er met baan P?",
        [
            "De bocht wordt half zo groot",
            "De bocht wordt twee keer zo groot",
            "Het deeltje gaat sneller vliegen",
            "Het deeltje buigt nu naar beneden af",
        ],
        0,
        "r = m · v / (q · B): B × 2 geeft r ÷ 2. De snelheid blijft gelijk.",
    )),
    klik(
        "Klik op de pijl die de zin van de kracht op de draad toont.",
        DP.bestand, ZP["A"],
        "Het veld wijst van N naar Z, dus naar beneden. Stroom het blad in en veld naar beneden geeft een kracht naar links.",
    ),
    met_prent(DP.bestand, tabel(
        "Welke kant op werkt de kracht op de draad na deze verandering?",
        [
            ("de stroom keert om", "Naar rechts"),
            ("de magneet wordt omgedraaid", "Naar rechts"),
            ("de stroom keert om én de magneet wordt omgedraaid", "Naar links"),
        ],
        "Elke omkering keert de kracht om; twee omkeringen heffen elkaar op.",
        kolommen=["Naar links", "Naar rechts"],
    )),
    met_prent(DP.bestand, mk(
        "Je verdubbelt de stroom én een twee keer zo lang stuk draad ligt in het veld. Hoe verandert F?",
        ["× 4", "× 2", "blijft gelijk", "÷ 2"],
        0,
        "F = B · I · ℓ · sin α: I × 2 en ℓ × 2 geeft × 4.",
    )),
    inv(
        "Een draad van 0,20 m voert 5,0 A in een veld van 0,40 T, onder een hoek van 30° met de veldlijnen. Hoe groot is F, in N? (sin 30° = 0,50)",
        ["0,2", "0,20", "0,2 N", "0,20 N", "0.2"],
        "F = B · I · ℓ · sin α = 0,40 · 5,0 · 0,20 · 0,50 = 0,20 N.",
    ),
    inv(
        "Op een draad van 0,30 m loodrecht in een veld van 0,25 T werkt 0,15 N. Hoeveel stroom loopt er, in ampère?",
        ["2", "2,0", "2 A", "2,0 A"],
        "I = F / (B · ℓ) = 0,15 / (0,25 · 0,30) = 2,0 A.",
    ),
    tabel(
        "Hoe groot is de kracht op een stroomdraad onder deze hoek met de veldlijnen?",
        [
            ("90°", "F_max"),
            ("30°", "F_max / 2"),
            ("0°", "0"),
        ],
        "F ~ sin α, met sin 90° = 1, sin 30° = 0,5 en sin 0° = 0.",
        kolommen=["0", "F_max / 2", "F_max"],
    ),
    mk(
        "Een proton vliegt met 2,0 · 10⁶ m/s loodrecht door een veld van 0,50 T. Hoe groot is de lorentzkracht? Neem e = 1,6 · 10⁻¹⁹ C.",
        ["1,6 · 10⁻¹³ N", "6,4 · 10⁻¹³ N", "1,6 · 10⁻¹⁹ N", "5,0 · 10⁻¹³ N"],
        0,
        "F = q · v · B = 1,6 · 10⁻¹⁹ · 2,0 · 10⁶ · 0,50 = 1,6 · 10⁻¹³ N.",
    ),
    inv(
        "Een lading van 3,0 µC beweegt met 400 m/s loodrecht door een veld van 0,50 T. Hoe groot is F, in mN?",
        ["0,6", "0,60", "0,6 mN", "0,60 mN", "0.6"],
        "F = q · v · B = 3,0 · 10⁻⁶ · 400 · 0,50 = 6,0 · 10⁻⁴ N = 0,60 mN.",
    ),
    inv(
        "Datzelfde proton (m = 1,67 · 10⁻²⁷ kg, v = 2,0 · 10⁶ m/s) beschrijft een cirkel in het veld van 0,50 T. Hoe groot is de straal, in cm? Rond af op één decimaal.",
        ["4,2", "4,2 cm", "4.2"],
        "r = m · v / (q · B) = 1,67 · 10⁻²⁷ · 2,0 · 10⁶ / (1,6 · 10⁻¹⁹ · 0,50) ≈ 0,042 m.",
    ),
    tabel(
        "Wat gebeurt er met de straal van de cirkelbaan?",
        [
            ("de snelheid wordt 2 keer zo groot", "× 2"),
            ("het veld wordt 2 keer zo sterk", "÷ 2"),
            ("de massa wordt 2 keer zo groot", "× 2"),
        ],
        "r = m · v / (q · B).",
        kolommen=["× 2", "÷ 2"],
    ),
    casus(
        "In een massaspectrometer komen neonionen met dezelfde lading en snelheid in een homogeen veld. Het ene soort heeft massa 20 u, het andere 22 u.",
        [
            keuze(
                "De ionen van [[20 u|*22 u]] beschrijven de grootste bocht.",
                "r is recht evenredig met de massa.",
            ),
            mk(
                "Hoeveel keer zo groot is die straal?",
                ["1,1 keer", "2 keer", "1,2 keer", "0,9 keer"],
                0,
                "22 / 20 = 1,1.",
            ),
            keuze(
                "Maak je het veld sterker, dan liggen de twee inslagplaatsen [[*dichter bij elkaar|verder uit elkaar]].",
                "Beide stralen worden kleiner, dus ook het verschil.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen in een massaspectrometer in volgorde.",
        [
            "Atomen worden geïoniseerd",
            "Een spanning versnelt de ionen",
            "Het magnetisch veld buigt de ionen af",
            "De ionen raken de detector op een plaats die van hun massa afhangt",
        ],
        "Zwaardere ionen maken een grotere bocht.",
    ),
    tabel(
        "Wat gebeurt er met de draairichting van een gelijkstroommotor?",
        [
            ("de stroom keert om", "Keert om"),
            ("de magneten worden omgewisseld", "Keert om"),
            ("stroom en magneten keren allebei om", "Blijft gelijk"),
        ],
        "De kracht op elke zijde van de spoel keert om bij elke omkering.",
        kolommen=["Keert om", "Blijft gelijk"],
    ),
    mk(
        "Twee evenwijdige draden trekken elkaar aan. Je halveert de afstand. Wat gebeurt er met de kracht per meter?",
        ["Ze wordt twee keer zo groot", "Ze wordt vier keer zo groot", "Ze wordt de helft", "Ze verandert niet"],
        0,
        "F / ℓ = μ₀ · I₁ · I₂ / (2π · d): omgekeerd evenredig met d.",
    ),
    mk(
        "Twee evenwijdige draden op 0,10 m voeren elk 10 A in dezelfde zin. Hoe groot is de kracht per meter? Neem μ₀ = 4π · 10⁻⁷ T·m/A.",
        ["2,0 · 10⁻⁴ N/m, ze trekken aan", "2,0 · 10⁻⁴ N/m, ze stoten af", "2,0 · 10⁻⁵ N/m, ze trekken aan", "2,0 · 10⁻³ N/m, ze stoten af"],
        0,
        "F / ℓ = 2 · 10⁻⁷ · 10 · 10 / 0,10 = 2,0 · 10⁻⁴ N/m; stromen in dezelfde zin trekken aan.",
    ),
    mk(
        "Twee evenwijdige draden stoten elkaar af. Wat weet je zeker?",
        [
            "De stromen lopen tegengesteld",
            "De stromen lopen in dezelfde zin",
            "Eén van de twee draden voert geen stroom",
            "De draden zijn allebei elektrisch geladen",
        ],
        0,
        "Gelijke zin trekt aan, tegengestelde zin stoot af.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een magnetisch veld kan een lading niet sneller maken.", J),
            ("Een stilstaand elektron voelt een lorentzkracht.", F),
            ("In een cyclotron versnelt het magnetisch veld de deeltjes.", F),
            ("Een deeltje dat schuin het veld binnenkomt, volgt een schroeflijn.", J),
        ],
        "De magnetische kracht staat loodrecht op v en verricht geen arbeid.",
    ),
    sorteer(
        "Gaat het hier om de kracht op een stroom in een draad, of op losse geladen deeltjes?",
        ["Stroom in een draad", "Losse deeltjes"],
        [
            ("een luidspreker", "Stroom in een draad"),
            ("een gelijkstroommotor", "Stroom in een draad"),
            ("een massaspectrometer", "Losse deeltjes"),
            ("een cyclotron", "Losse deeltjes"),
            ("het noorderlicht", "Losse deeltjes"),
        ],
        "Laplacekracht op een draad, lorentzkracht op losse ladingen.",
    ),
    koppel(
        "Koppel elk toestel aan wat het doet.",
        [
            ("luidspreker", "duwt een membraan heen en weer"),
            ("hallsensor", "meet de sterkte van een magnetisch veld"),
            ("cyclotron", "versnelt deeltjes in een cirkelbaan"),
            ("massaspectrometer", "scheidt ionen op hun massa"),
        ],
        ["wekt een wisselspanning op"],
        "Alle vier gebruiken de magnetische kracht op bewegende ladingen.",
    ),
    keuze(
        "De magnetische kracht op een draad staat loodrecht op [[*de stroom én het veld|alleen de stroom|alleen het veld]].",
        "Ze staat loodrecht op het vlak van stroom en veld.",
    ),
    keuze(
        "In een cyclotron zorgt [[*het elektrisch veld|het magnetisch veld]] voor de versnelling.",
        "Het magnetisch veld houdt de deeltjes alleen in hun bocht.",
    ),
    sleep(
        "De kracht op een stroomdraad heet de [[laplacekracht]], die op één bewegende lading de [[lorentzkracht]]. Een lading die loodrecht een homogeen veld binnenkomt, volgt een [[cirkelbaan]].",
        ["coulombkracht", "rechte lijn"],
        "Beide krachten staan loodrecht op de beweging.",
    ),
    open_(
        "Leg uit waarom een magnetisch veld de richting van een bewegend deeltje kan veranderen, maar niet de grootte van zijn snelheid.",
        "De lorentzkracht staat altijd loodrecht op de snelheid. Een kracht loodrecht op de beweging verricht geen arbeid, dus de kinetische energie en de grootte van de snelheid blijven gelijk. Alleen de richting draait, en zo ontstaat een cirkelbaan.",
    ),
    met_prent(VB.bestand, mk(
        "Een elektron vliegt met dezelfde snelheid binnen. Hoe ziet zijn baan eruit?",
        [
            "Een heel kleine bocht naar beneden",
            "Een heel grote bocht naar beneden, groter dan R",
            "Een heel kleine bocht naar boven",
            "Een rechte lijn, net zoals bij baan Q",
        ],
        0,
        "Negatief, dus naar beneden; en een elektron is veel lichter dan een ion, dus r is veel kleiner.",
    )),
]
