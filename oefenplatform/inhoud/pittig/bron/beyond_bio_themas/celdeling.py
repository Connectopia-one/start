"""De celcyclus, mitose en meiose — pittig (🧬 Beyond doorstroom, biologie)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Celcyclus als taart ------------------------------------------------------
CC = Prent("celcyclus", "De celcyclus van een lichaamscel", "cirkel verdeeld in vier delen W, X, Y en Z; de pijl toont de richting")
_DELEN = [("W", 0, 150, "#cfe5f3"), ("X", 150, 270, "#f5d9a8"), ("Y", 270, 330, "#d6ecd2"), ("Z", 330, 360, "#f3c6d0")]
MX, MY, RR = 420, 340, 230
for k, a0, a1, kl in _DELEN:
    x0, y0 = MX + RR * math.sin(math.radians(a0)), MY - RR * math.cos(math.radians(a0))
    x1, y1 = MX + RR * math.sin(math.radians(a1)), MY - RR * math.cos(math.radians(a1))
    groot = 1 if a1 - a0 > 180 else 0
    CC.pad(f"M{MX} {MY} L{x0:.0f} {y0:.0f} A{RR} {RR} 0 {groot} 1 {x1:.0f} {y1:.0f} Z", kl, DONKER, 2)
LCC = {}
for k, a0, a1, kl in _DELEN:
    m = math.radians((a0 + a1) / 2)
    LCC[k] = (MX + 150 * math.sin(m), MY - 150 * math.cos(m))
    CC.letter(*LCC[k], k)
CC.pad(f"M{MX + 260 * math.sin(math.radians(20)):.0f} {MY - 260 * math.cos(math.radians(20)):.0f} A260 260 0 0 1 {MX + 260 * math.sin(math.radians(70)):.0f} {MY - 260 * math.cos(math.radians(70)):.0f}", "none", DONKER, 3)
_e = math.radians(70)
CC.svg(f'<polygon points="{MX + 260 * math.sin(_e) + 8:.0f},{MY - 260 * math.cos(_e) + 14:.0f} {MX + 248 * math.sin(_e) - 10:.0f},{MY - 248 * math.cos(_e) + 2:.0f} {MX + 272 * math.sin(_e) + 4:.0f},{MY - 272 * math.cos(_e) - 6:.0f}" fill="{DONKER}"/>')
CC.rect(720, 180, 250, 230, "#fbf6ea", DONKER, 14, 1.5)
CC.tekst(845, 215, "wat gebeurt er?", 15, vet=True)
for i, t in enumerate(("de cel groeit", "het DNA wordt gekopieerd", "de cel maakt zich klaar", "de cel deelt")):
    CC.tekst(845, 255 + i * 40, t, 15)
ZCC = {k: [Prent.rond(*LCC[k], 40), Prent.rond(*LCC[k], 22)] for k in LCC}

# Mitose in vier tekeningen, door elkaar ----------------------------------
MI = Prent("mitose-fasen", "Vier momenten uit een mitose (door elkaar)", "vier cellen A, B, C en D met elk vier chromosomen in een andere stand")


def _chrom(p, x, y, kl, dubbel=True, hoek=0):
    if dubbel:
        p.svg(f'<g transform="rotate({hoek} {x} {y})"><path d="M{x-10} {y-22} Q{x} {y} {x-10} {y+22}" stroke="{kl}" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M{x+10} {y-22} Q{x} {y} {x+10} {y+22}" stroke="{kl}" stroke-width="7" fill="none" stroke-linecap="round"/></g>')
    else:
        p.svg(f'<path d="M{x-12} {y-14} Q{x} {y+6} {x+12} {y-14}" stroke="{kl}" stroke-width="7" fill="none" stroke-linecap="round"/>')


_KL = [ROOD, BLAUW, ROOD, BLAUW]
# A = anafase
MI.ellips(140, 330, 100, 150, "#fdf0e0", DONKER, 2)
for i, dx in enumerate((-45, -15, 15, 45)):
    MI.lijn(140, 195, 140 + dx, 275, GRIJS, 1.5)
    MI.lijn(140, 465, 140 + dx, 368, GRIJS, 1.5)
    MI.svg(f'<path d="M{128+dx} 270 Q{140+dx} 295 {152+dx} 270" stroke="{_KL[i]}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    MI.svg(f'<path d="M{128+dx} {375} Q{140+dx} {355} {152+dx} {375}" stroke="{_KL[i]}" stroke-width="7" fill="none" stroke-linecap="round"/>')
# B = profase
MI.ellips(380, 330, 100, 150, "#fdf0e0", DONKER, 2)
MI.svg(f'<circle cx="380" cy="330" r="70" fill="none" stroke="{DONKER}" stroke-width="1.5" stroke-dasharray="6 6"/>')
for (dx, dy, h), kl in zip(((-30, -25, 30), (25, -30, -20), (-20, 30, -40), (30, 25, 10)), _KL):
    _chrom(MI, 380 + dx, 330 + dy, kl, hoek=h)
# C = telofase
MI.pad("M600 180 C 690 180 700 300 630 330 C 700 360 690 480 600 480 C 510 480 500 360 570 330 C 500 300 510 180 600 180 Z", "#fdf0e0", DONKER, 2)
MI.ellips(600, 250, 45, 35, "#fbf6ea", DONKER, 1.5)
MI.ellips(600, 410, 45, 35, "#fbf6ea", DONKER, 1.5)
for i, dx in enumerate((-20, -7, 7, 20)):
    MI.lijn(600 + dx, 235, 600 + dx, 265, _KL[i], 5)
    MI.lijn(600 + dx, 395, 600 + dx, 425, _KL[i], 5)
# D = metafase
MI.ellips(860, 330, 100, 150, "#fdf0e0", DONKER, 2)
MI.lijn(765, 330, 955, 330, GRIJS, 0.8, stippel=True)
for i, dx in enumerate((-72, -24, 24, 72)):
    MI.lijn(860, 185, 860 + dx, 312, GRIJS, 1)
    MI.lijn(860, 475, 860 + dx, 348, GRIJS, 1)
    _chrom(MI, 860 + dx, 330, _KL[i], hoek=90)
LMI = {"A": (140, 530), "B": (380, 530), "C": (600, 530), "D": (860, 530)}
for k, (x, y) in LMI.items():
    MI.letter(x, y, k)
ZMI = {"A": [Prent.zone(40, 180, 200, 300), Prent.rond(*LMI["A"], 22)],
       "B": [Prent.zone(280, 180, 200, 300), Prent.rond(*LMI["B"], 22)],
       "C": [Prent.zone(520, 180, 180, 300), Prent.rond(*LMI["C"], 22)],
       "D": [Prent.zone(760, 180, 200, 300), Prent.rond(*LMI["D"], 22)]}

VRAGEN = [
    klik(
        "Klik op het deel van de celcyclus waarin het DNA gekopieerd wordt.",
        CC.bestand, ZCC["X"],
        "Na G1 komt de S-fase, daarna G2 en dan de deling.",
    ),
    met_prent(CC.bestand, tabel(
        "Kijk naar de celcyclus. Klopt dit?",
        [
            ("W is de G1-fase, waarin de cel groeit.", J),
            ("W, X en Y samen vormen de interfase.", J),
            ("Z is het kortste deel van de cyclus.", J),
            ("Een zenuwcel draait de hele tijd rond in deze cirkel.", F),
        ],
        "Een zenuwcel zit in G0, buiten de cyclus. X is hier de S-fase en Y de G2-fase.",
    )),
    klik(
        "Klik op de cel in de metafase.",
        MI.bestand, ZMI["D"],
        "In de metafase staan de chromosomen in het evenaarsvlak.",
    ),
    klik(
        "Klik op de cel waarin de zusterchromatiden naar de polen getrokken worden.",
        MI.bestand, ZMI["A"],
        "Dat is de anafase.",
    ),
    met_prent(MI.bestand, volgorde(
        "Zet de vier tekeningen in de juiste volgorde.",
        ["B", "D", "A", "C"],
        "Profase (B), metafase (D), anafase (A), telofase (C).",
    )),
    met_prent(MI.bestand, tabel(
        "Kijk naar de vier cellen. Klopt dit?",
        [
            ("In B verdwijnt het kernmembraan.", J),
            ("In C knijpt het celmembraan in: dit is een dierlijke cel.", J),
            ("In D bestaat elk chromosoom uit twee chromatiden.", J),
            ("In A gaan homologe chromosomen uit elkaar.", F),
        ],
        "In een mitose gaan zusterchromatiden uit elkaar, geen homologe paren.",
    )),
    tabel(
        "Mitose, meiose of allebei?",
        [
            ("er ontstaan vier cellen", "Meiose"),
            ("er gebeurt crossing-over", "Meiose"),
            ("er gaat een S-fase aan vooraf", "Allebei"),
            ("de dochtercellen zijn erfelijk gelijk", "Mitose"),
            ("er wordt een spoelfiguur gebruikt", "Allebei"),
        ],
        "Beide gebruiken microtubuli als trekdraden.",
        kolommen=["Mitose", "Meiose", "Allebei"],
    ),
    inv(
        "Een cel van een hond heeft 78 chromosomen. Hoeveel chromosomen heeft een zaadcel van een hond?",
        ["39"],
        "Een gameet is haploïd: 78 / 2 = 39.",
    ),
    inv(
        "Een lichaamscel van een kat heeft 38 chromosomen. Hoeveel chromatiden telt ze in de metafase van de mitose?",
        ["76"],
        "In de metafase heeft elk chromosoom twee chromatiden: 38 x 2 = 76.",
    ),
    inv(
        "Een organisme heeft 3 chromosomenparen. Hoeveel verschillende gameten kan het door mixing alleen al vormen?",
        ["8", "acht"],
        "Elk paar heeft twee mogelijkheden: 2 x 2 x 2 = 8.",
    ),
    casus(
        "Een cel met 4 chromosomen (2 paren) gaat in meiose. Volg het aantal chromosomen en chromatiden.",
        [
            inv(
                "Hoeveel chromatiden heeft de cel na de S-fase?",
                ["8", "acht"],
                "Vier chromosomen met elk twee chromatiden.",
            ),
            inv(
                "Hoeveel chromosomen heeft elke cel na meiose I?",
                ["2", "twee"],
                "Na meiose I zijn de paren gescheiden: de cel is haploïd.",
            ),
            inv(
                "Hoeveel chromatiden heeft elke cel na meiose II?",
                ["2", "twee"],
                "In meiose II gaan de zusterchromatiden uit elkaar: elke cel heeft 2 enkelvoudige chromosomen.",
            ),
        ],
    ),
    tabel(
        "Meiose I of meiose II?",
        [
            ("de homologe paren gaan uit elkaar", "Meiose I"),
            ("de zusterchromatiden gaan uit elkaar", "Meiose II"),
            ("er vormen zich chiasmata", "Meiose I"),
            ("lijkt het meest op een mitose", "Meiose II"),
        ],
        "Crossing-over gebeurt in de profase van meiose I.",
        kolommen=["Meiose I", "Meiose II"],
    ),
    koppel(
        "Koppel elke fase van de celcyclus aan wat er gebeurt.",
        [
            ("G1", "de cel groeit en maakt eiwitten"),
            ("S", "het DNA wordt gekopieerd"),
            ("G2", "de kopieën worden nagekeken"),
            ("G0", "de cel deelt niet meer"),
        ],
        ["de homologe paren wisselen stukken uit"],
        "Dat laatste is crossing-over in de meiose.",
    ),
    mk(
        "Een geneesmiddel tegen kanker houdt de vorming van de spoelfiguur tegen. In welke fase blijven de cellen steken?",
        [
            "Rond de metafase van de mitose",
            "In de G1-fase, nog voor het DNA gekopieerd is",
            "In de S-fase, tijdens het kopiëren van het DNA",
            "In de G0-fase, buiten de celcyclus",
        ],
        0,
        "Zonder trekdraden kunnen de chromosomen niet in het evenaarsvlak gaan staan en niet uiteengaan.",
    ),
    mk(
        "Waarom komt er geen S-fase tussen meiose I en meiose II?",
        [
            "Anders halveert het aantal chromosomen niet",
            "De cel heeft na meiose I geen DNA meer over",
            "In meiose II worden geen chromatiden gescheiden",
            "De spoelfiguur werkt pas na een volgende S-fase",
        ],
        0,
        "Eén kopieerronde en twee delingen geven vier haploïde cellen.",
    ),
    tabel(
        "Plantencel of dierlijke cel?",
        [
            ("er vormt zich een celplaat", "Plantencel"),
            ("het celmembraan knijpt in", "Dierlijke cel"),
            ("een nieuwe celwand scheidt de dochtercellen", "Plantencel"),
            ("er ontstaat een insnoeringsgroef", "Dierlijke cel"),
        ],
        "Een plantencel kan niet insnoeren door haar stevige wand.",
        kolommen=["Plantencel", "Dierlijke cel"],
    ),
    sleep(
        "Bij [[crossing-over]] wisselen [[homologe]] chromosomen stukken uit op een [[chiasma]]. Zo komen allelen van vader en moeder op één chromosoom.",
        ["mitose", "zuster", "centromeer"],
        "Zusterchromatiden zijn kopieën: uitwisselen tussen hen geeft niets nieuws.",
    ),
    tabel(
        "Waar of niet waar over de variatie tussen gameten?",
        [
            ("Mixing verdeelt de paren toevallig over de polen.", J),
            ("Crossing-over maakt nieuwe combinaties van allelen.", J),
            ("Broers en zussen verschillen daardoor van elkaar.", J),
            ("Twee eicellen van dezelfde vrouw zijn erfelijk altijd gelijk.", F),
        ],
        "Door mixing en crossing-over is bijna elke gameet anders.",
    ),
    mk(
        "Bij een meiose gaat één chromosomenpaar niet uit elkaar. Wat is het gevolg?",
        [
            "Gameten met een chromosoom te veel of te weinig",
            "Gameten die allemaal diploïd geworden zijn",
            "Een extra S-fase in alle gameten tegelijk",
            "Een gewone mitose in plaats van een meiose in de klier",
        ],
        0,
        "Na een bevruchting kan dat bv. trisomie 21 geven.",
    ),
    tabel(
        "Klopt dit over de controlepunten?",
        [
            ("Ze kijken of het DNA onbeschadigd is.", J),
            ("Ze kijken of de cel groot genoeg is.", J),
            ("Een cel met beschadigd DNA wordt even tegengehouden.", J),
            ("Ze zorgen ervoor dat elke cel zo snel mogelijk deelt.", F),
        ],
        "Zo wordt een fout niet aan alle dochtercellen doorgegeven.",
    ),
    keuze(
        "Na de anafase vormt zich in de [[*telofase|profase|metafase]] rond elke groep chromosomen een nieuw kernmembraan.",
        "De chromosomen rollen dan weer los tot chromatine.",
    ),
    mk(
        "Bij katten heeft elke generatie 38 chromosomen per lichaamscel. Hoe blijft dat aantal gelijk?",
        [
            "De meiose halveert, de bevruchting verdubbelt",
            "Elke gameet krijgt alle 38 chromosomen mee",
            "Bij de bevruchting verdwijnt de helft van het DNA",
            "De mitose halveert het aantal na elke geboorte",
        ],
        0,
        "Twee haploïde gameten van 19 geven een diploïde zygote van 38.",
    ),
    tabel(
        "Klopt dit over de G0-fase?",
        [
            ("Een cel in G0 doet haar werk maar deelt niet.", J),
            ("Veel zenuwcellen blijven hun hele leven in G0.", J),
            ("G0 ligt buiten de gewone celcyclus.", J),
            ("In G0 wordt het DNA een tweede keer gekopieerd.", F),
        ],
        "Spiercellen en zenuwcellen delen na hun vorming bijna niet meer.",
    ),
    keuze(
        "De trekdraden van de spoelfiguur grijpen aan op het [[*kinetochoor|nucleosoom|chiasma]] bij het centromeer.",
        "Zo kunnen ze de chromatiden naar de polen trekken.",
    ),
    tabel(
        "Waarvoor dient deze celdeling in het lichaam?",
        [
            ("een wonde in de huid groeit dicht", "Mitose"),
            ("in de teelballen ontstaan zaadcellen", "Meiose"),
            ("een kind groeit", "Mitose"),
            ("in de eierstokken ontstaan eicellen", "Meiose"),
        ],
        "Meiose gebeurt bij de mens alleen in de geslachtsklieren.",
        kolommen=["Mitose", "Meiose"],
    ),
    mk(
        "Na meiose I heeft een menselijke cel 23 chromosomen. Waarom noemt men die cel al haploïd?",
        [
            "Van elk paar is er nog maar één over",
            "Elk chromosoom heeft nog maar één chromatide",
            "Het DNA is tijdens meiose I gehalveerd door een S-fase",
            "De cel heeft haar kernmembraan voorgoed verloren",
        ],
        0,
        "Elk chromosoom heeft wel nog twee chromatiden: die gaan pas in meiose II uiteen.",
    ),
    volgorde(
        "Zet de stappen van een meiose in de juiste volgorde.",
        ["S-fase", "Crossing-over tussen homologe chromosomen", "De paren gaan uit elkaar", "De zusterchromatiden gaan uit elkaar", "Vier haploïde cellen"],
        "Eerst meiose I met de paren, dan meiose II met de chromatiden.",
    ),
    open_(
        "Leg uit waarom twee kinderen van dezelfde ouders, die geen eeneiige tweeling zijn, erfelijk verschillen.",
        "Bij de meiose worden de chromosomenparen toevallig over de polen verdeeld (mixing). Tijdens de profase van meiose I wisselen homologe chromosomen ook stukken uit (crossing-over). Daardoor is bijna elke eicel en elke zaadcel erfelijk anders. Bij elke bevruchting komt dus een andere combinatie samen.",
    ),
]
