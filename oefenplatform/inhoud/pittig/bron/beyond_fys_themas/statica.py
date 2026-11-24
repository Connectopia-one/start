"""Statica: krachten, moment en evenwicht — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Hefboom met gewichten -------------------------------------------------------
HB = Prent("hefboom-haakjes", "Een lichte hefboom: links hangt 30 N op 0,4 m van het draaipunt", "een balk op een driehoekig draaipunt met een schaal van 0,1 m; links hangt een gewicht van 30 N op 0,4 m; rechts vier haakjes P tot S op 0,1, 0,2, 0,3 en 0,4 m")
def _x(m):
    return 500 + m * 900
HB.rect(_x(-0.5), 250, _x(0.5) - _x(-0.5), 24, "#e8d3a8", DONKER, 4, 2)
HB.pad(f"M 500 274 L 470 340 L 530 340 Z", GRIJS, DONKER, 2)
HB.rect(455, 340, 90, 14, "#9a9a9a", DONKER, 2, 2)
for i in range(-5, 6):
    HB.lijn(_x(i / 10), 250, _x(i / 10), 262, DONKER, 2)
    HB.tekst(_x(i / 10), 236, f"{abs(i) / 10:.1f}".replace(".", ","), 16)
HB.tekst(500, 200, "afstand tot het draaipunt (m)", 16)
HB.lijn(_x(-0.4), 274, _x(-0.4), 380, DONKER, 2)
HB.rect(_x(-0.4) - 40, 380, 80, 70, "#cfd8e3", DONKER, 6, 2)
HB.tekst(_x(-0.4), 422, "30 N", 20, vet=True)
for k, m in zip("PQRS", (0.1, 0.2, 0.3, 0.4)):
    HB.pad(f"M {_x(m)} 274 L {_x(m)} 300 A 10 10 0 1 1 {_x(m) - 10} 310", "none", DONKER, 3)
    HB.letter(_x(m), 350, k)
ZH = {k: [Prent.zone(_x(m) - 26, 270, 52, 105)] for k, m in zip("PQRS", (0.1, 0.2, 0.3, 0.4))}

# Kist op een helling ---------------------------------------------------------
KH = Prent("kist-helling", "Een kist die stil op een helling staat, met vijf krachtpijlen", "een helling van 30 graden met een kist erop; pijlen A recht naar beneden, B loodrecht op de helling naar boven, C langs de helling naar boven, D horizontaal naar links, E langs de helling naar beneden")
a = math.radians(30)
x0, y0 = 120, 560
x1, y1 = 900, 560 - 780 * math.tan(a)
KH.pad(f"M {x0} {y0} L {x1} {y0} L {x1} {y1:.1f} Z", "#efe6d2", DONKER, 2)
# kist midden op de helling
ux, uy = math.cos(a), -math.sin(a)   # langs de helling omhoog
nx, ny = -math.sin(a), -math.cos(a)  # loodrecht op de helling, weg van het vlak
mx, my = x0 + 470 * ux, y0 + 470 * uy
hw, hh = 70, 55
hoeken = [(mx - hw * ux, my - hw * uy), (mx + hw * ux, my + hw * uy), (mx + hw * ux + 2 * hh * nx, my + hw * uy + 2 * hh * ny), (mx - hw * ux + 2 * hh * nx, my - hw * uy + 2 * hh * ny)]
KH.pad("M " + " L ".join(f"{p:.1f} {q:.1f}" for p, q in hoeken) + " Z", "#c9a46a", DONKER, 3)
cx, cy = mx + hh * nx, my + hh * ny
KH.cirkel(cx, cy, 6, DONKER, DONKER, 1)
L = 150
PIJLEN = {
    "A": (0, 1),
    "B": (nx, ny),
    "C": (ux, uy),
    "D": (-1, 0),
    "E": (-ux, -uy),
}
LPOS = {}
for k, (dx, dy) in PIJLEN.items():
    KH.pijl(cx, cy, cx + L * dx, cy + L * dy, ORANJE, 5)
    LPOS[k] = (cx + (L + 32) * dx, cy + (L + 32) * dy)
    KH.letter(*LPOS[k], k)
KH.tekst(x0 + 120, y0 - 16, "30°", 20)
ZK = {k: [Prent.rond(cx + 0.7 * L * dx, cy + 0.7 * L * dy, 30), Prent.rond(*LPOS[k], 24)] for k, (dx, dy) in PIJLEN.items()}

VRAGEN = [
    klik(
        "Aan welk haakje hang je een gewicht van 40 N zodat de hefboom in evenwicht is?",
        HB.bestand, ZH["R"],
        "Links: 30 N · 0,4 m = 12 N·m. Rechts: 40 N · d = 12 N·m, dus d = 0,3 m.",
    ),
    met_prent(HB.bestand, tabel(
        "Op welke afstand rechts moet dit gewicht hangen voor evenwicht?",
        [
            ("40 N", "0,3 m"),
            ("60 N", "0,2 m"),
            ("120 N", "0,1 m"),
        ],
        "Telkens moet het moment rechts 12 N·m zijn.",
        kolommen=["0,1 m", "0,2 m", "0,3 m"],
    )),
    met_prent(HB.bestand, mk(
        "De hefboom is in evenwicht met 40 N aan haakje R. Hoe groot is de kracht van het draaipunt op de balk? De balk zelf weegt bijna niets.",
        ["70 N", "10 N", "40 N", "12 N"],
        0,
        "Ook de krachten moeten samen nul zijn: 30 N + 40 N naar beneden, dus 70 N naar boven.",
    )),
    met_prent(HB.bestand, keuze(
        "Hang je de 40 N aan haakje S, dan kantelt de balk naar [[*rechts|links]].",
        "Rechts wordt het moment 40 · 0,4 = 16 N·m, groter dan de 12 N·m links.",
    )),
    met_prent(HB.bestand, inv(
        "Hoe groot is het moment van het gewicht links, in N·m?",
        ["12", "12 Nm", "12 N·m", "12 N m"],
        "M = F · d = 30 · 0,4 = 12 N·m.",
    )),
    klik(
        "Klik op de pijl van de normaalkracht.",
        KH.bestand, ZK["B"],
        "De normaalkracht staat loodrecht op het oppervlak waarop de kist rust.",
    ),
    klik(
        "De kist staat stil. Klik op de pijl van de wrijvingskracht.",
        KH.bestand, ZK["C"],
        "De kist wil naar beneden glijden; de wrijving werkt dat tegen, dus langs de helling naar boven.",
    ),
    met_prent(KH.bestand, tabel(
        "Welke kracht stelt deze pijl voor?",
        [
            ("A", "Zwaartekracht"),
            ("B", "Normaalkracht"),
            ("C", "Wrijvingskracht"),
        ],
        "De zwaartekracht wijst altijd recht naar beneden, naar het middelpunt van de aarde.",
        kolommen=["Zwaartekracht", "Normaalkracht", "Wrijvingskracht"],
    )),
    met_prent(KH.bestand, keuze(
        "Maak je de helling steiler, dan wordt de component van de zwaartekracht langs de helling [[*groter|kleiner]] en de normaalkracht [[groter|*kleiner]].",
        "Hoe steiler, hoe meer van de zwaartekracht langs het vlak wijst en hoe minder erop drukt.",
    )),
    mk(
        "Een kist van 50 kg ligt op een vlakke vloer met μ = 0,40. Welke kracht heb je minstens nodig om haar te doen schuiven? Neem g = 9,81 N/kg.",
        ["ongeveer 196 N", "ongeveer 491 N", "ongeveer 20 N", "ongeveer 125 N"],
        0,
        "F_w = μ · F_N = 0,40 · 50 · 9,81 ≈ 196 N.",
    ),
    inv(
        "Een veer met k = 200 N/m levert een kracht van 6,0 N. Hoeveel is ze uitgerekt, in cm?",
        ["3", "3,0", "3 cm", "3,0 cm"],
        "Δℓ = F / k = 6,0 / 200 = 0,030 m.",
    ),
    mk(
        "Twee krachten van 5,0 N en 12 N werken loodrecht op elkaar op hetzelfde punt. Hoe groot is de resulterende kracht?",
        ["13 N", "17 N", "7,0 N", "8,5 N"],
        0,
        "√(5,0² + 12²) = √169 = 13 N.",
    ),
    mk(
        "Twee krachten liggen op één lijn: 20 N naar rechts en 15 N naar links. Wat is de resulterende kracht?",
        ["5 N naar rechts", "35 N naar rechts", "5 N naar links", "25 N naar rechts"],
        0,
        "Tegengestelde zin: je trekt ze van elkaar af; de grootste bepaalt de zin.",
    ),
    mk(
        "Je trekt met 60 N aan een koord dat 60° maakt met de grond. Hoe groot is de horizontale component? (cos 60° = 0,50)",
        ["30 N", "52 N", "60 N", "120 N"],
        0,
        "F_x = F · cos α = 60 · 0,50 = 30 N.",
    ),
    inv(
        "Een kracht van 50 N werkt op 0,80 m van het draaipunt, onder een hoek van 30° met de stang. Hoe groot is het moment, in N·m? (sin 30° = 0,50)",
        ["20", "20 Nm", "20 N·m"],
        "M = F · d · sin α = 50 · 0,80 · 0,50 = 20 N·m.",
    ),
    tabel(
        "Hoe groot is het moment van een kracht F op afstand d van het draaipunt, in deze situatie?",
        [
            ("de werklijn gaat door het draaipunt", "0"),
            ("de kracht staat loodrecht op de stang", "F · d"),
            ("de kracht maakt 30° met de stang", "F · d / 2"),
        ],
        "M = F · d · sin α.",
        kolommen=["0", "F · d / 2", "F · d"],
    ),
    inv(
        "Om een zware deur te openen is een moment van 15 N·m nodig. Je duwt loodrecht op 0,25 m van de scharnieren. Hoeveel kracht heb je nodig, in N?",
        ["60", "60 N"],
        "F = M / d = 15 / 0,25 = 60 N. Aan de klink op 0,75 m zou 20 N volstaan.",
    ),
    mk(
        "Een torenkraan heft 2000 N op 15 m van de toren. Het tegengewicht hangt op 5,0 m aan de andere kant. Hoe zwaar moet het zijn voor evenwicht?",
        ["6000 N", "667 N", "2000 N", "10 000 N"],
        0,
        "2000 · 15 = F · 5,0, dus F = 6000 N.",
    ),
    casus(
        "Op een wip zit kind A, dat 250 N weegt, op 1,6 m van het draaipunt. Kind B weegt 400 N.",
        [
            inv(
                "Op hoeveel meter van het draaipunt moet B zitten voor evenwicht?",
                ["1", "1,0", "1 m", "1,0 m"],
                "250 · 1,6 = 400 · d, dus d = 1,0 m.",
            ),
            keuze(
                "Schuift B dichter naar het draaipunt, dan gaat de kant van [[*A|B]] naar beneden.",
                "Het moment van B wordt kleiner dan dat van A.",
            ),
            mk(
                "Hoe groot is de kracht van het draaipunt op de wip in evenwicht? De plank zelf weegt bijna niets.",
                ["650 N", "150 N", "400 N", "0 N"],
                0,
                "Krachtenbalans: 250 N + 400 N naar beneden, dus 650 N naar boven.",
            ),
        ],
    ),
    casus(
        "Een lichte plank van 4,0 m ligt op twee steunen aan de uiteinden. Op 1,0 m van de linkersteun staat een last van 600 N.",
        [
            inv(
                "Hoeveel draagt de rechtersteun, in N?",
                ["150", "150 N"],
                "Momenten rond de linkersteun: 600 · 1,0 = F_R · 4,0, dus F_R = 150 N.",
            ),
            inv(
                "Hoeveel draagt de linkersteun, in N?",
                ["450", "450 N"],
                "Samen 600 N: 600 − 150 = 450 N.",
            ),
            keuze(
                "Schuif je de last naar het midden, dan draagt elke steun [[*300 N|600 N|150 N]].",
                "Symmetrisch: de last verdeelt zich gelijk.",
            ),
        ],
    ),
    sorteer(
        "Is dit een contactkracht of een veldkracht?",
        ["Contactkracht", "Veldkracht"],
        [
            ("de zwaartekracht", "Veldkracht"),
            ("de normaalkracht", "Contactkracht"),
            ("de wrijvingskracht", "Contactkracht"),
            ("de spankracht in een koord", "Contactkracht"),
            ("de magnetische kracht", "Veldkracht"),
        ],
        "Een veldkracht werkt op afstand, zonder aanraking.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een auto met constante snelheid rechtdoor is in translatie-evenwicht.", J),
            ("Een breed, laag lichaam kantelt minder snel dan een smal, hoog lichaam.", J),
            ("Je gewicht druk je uit in kilogram.", F),
            ("Op een helling is de normaalkracht even groot als de zwaartekracht.", F),
        ],
        "Gewicht is een kracht, in newton. Op een helling draagt de normaalkracht maar een deel.",
    ),
    koppel(
        "Koppel elke kracht aan haar formule.",
        [
            ("zwaartekracht", "m · g"),
            ("wrijvingskracht", "μ · F_N"),
            ("veerkracht", "k · Δℓ"),
            ("moment van een kracht", "F · d · sin α"),
        ],
        ["q · E"],
        "Allemaal in newton, behalve het moment: newtonmeter.",
    ),
    volgorde(
        "Zet de stappen om een evenwichtsprobleem op te lossen in volgorde.",
        [
            "Alle krachten op het lichaam tekenen",
            "Een handig draaipunt kiezen",
            "Momenten linksom gelijkstellen aan momenten rechtsom",
            "Met de krachtenbalans de laatste onbekende vinden",
        ],
        "Kies het draaipunt waar een onbekende kracht aangrijpt: die valt dan uit de momentenbalans.",
    ),
    sleep(
        "Een lichaam is in statisch evenwicht als de som van de [[krachten]] én de som van de [[momenten]] nul is. De zwaartekracht grijpt aan in het [[zwaartepunt]].",
        ["snelheden", "draaipunt"],
        "Eén van de twee is niet genoeg.",
    ),
    open_(
        "Leg uit waarom een hoge, smalle kast makkelijker omvalt dan een lage, brede kast met dezelfde massa.",
        "Een lichaam valt om als de werklijn van de zwaartekracht buiten het steunvlak komt. Bij een hoge, smalle kast ligt het zwaartepunt hoog en het steunvlak is smal, dus is er maar een kleine kanteling nodig. Bij een lage, brede kast moet je veel verder kantelen.",
    ),
]
