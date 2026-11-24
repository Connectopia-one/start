"""Atoomkernen en radioactief verval — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Nuclidenkaart ----------------------------------------------------------------------
NK = Prent("nuclidenkaart", "Een vereenvoudigde nuclidenkaart", "aantal neutronen N horizontaal (0 tot 150), aantal protonen Z verticaal (0 tot 100); een stippellijn N = Z; een groene strook stabiele kernen die eerst langs N = Z loopt en dan afbuigt naar meer neutronen; vier kernen: A rechts onder de strook, B links boven de strook, C op de strook, D helemaal bovenaan het einde van de strook")
X, Y = assen(NK, 0, 150, 0, 100, "N", "Z", 25, 20, links=130, rechts=880)
NK.lijn(X(0), Y(0), X(100), Y(100), GRIJS, 2, stippel=True)
NK.tekst(X(92), Y(100) + 8, "N = Z", 16, anker="end")
def zband(n):
    return n if n < 20 else 20 + (n - 20) * 0.62
bov = [(n, zband(n) + 6) for n in range(0, 127, 2)]
ond = [(n, zband(n) - 6) for n in range(126, -1, -2)]
NK.pad("M " + " L ".join(f"{X(a):.1f} {Y(max(b, 0)):.1f}" for a, b in bov + ond) + " Z", "#bfe0b0", GROEN, 2)
KE = {"A": (80, zband(80) - 18), "B": (40, zband(40) + 20), "C": (55, zband(55)), "D": (126, zband(126))}
LKE = {}
for k, (n, z) in KE.items():
    NK.cirkel(X(n), Y(z), 9, ORANJE, DONKER, 2)
    LKE[k] = (X(n) + 30, Y(z) + 28) if k != "B" else (X(n) - 30, Y(z) - 28)
    NK.letter(*LKE[k], k)
ZKE = {k: [Prent.rond(X(n), Y(z), 24), Prent.rond(*LKE[k], 22)] for k, (n, z) in KE.items()}

# Vervalkromme -----------------------------------------------------------------------
VK = Prent("vervalkromme", "Het aantal kernen van een radioactieve stof in de loop van de tijd", "grafiek van het aantal nog niet vervallen kernen (in 1000) tegen de tijd in uur, van 0 tot 24 uur; start bij 800, halveringstijd 6 uur; punten A bij 6 h, B bij 12 h, C bij 18 h")
X2, Y2 = assen(VK, 0, 24, 0, 900, "t (h)", "N (×1000)", 3, 100, links=130, rechts=900)
VK.pad("M " + " L ".join(f"{X2(t / 10):.1f} {Y2(800 * 0.5 ** (t / 60)):.1f}" for t in range(241)), "none", BLAUW, 4)
PV = {"A": 6, "B": 12, "C": 18}
LPV = {}
for k, t in PV.items():
    n = 800 * 0.5 ** (t / 6)
    VK.cirkel(X2(t), Y2(n), 8, ORANJE, DONKER, 2)
    LPV[k] = (X2(t) + 28, Y2(n) - 30)
    VK.letter(*LPV[k], k)
ZPV = {k: [Prent.rond(X2(t), Y2(800 * 0.5 ** (t / 6)), 22), Prent.rond(*LPV[k], 22)] for k, t in PV.items()}

VRAGEN = [
    klik(
        "Klik op de kern die waarschijnlijk via bèta-min-verval vervalt.",
        NK.bestand, ZKE["A"],
        "Hij heeft te veel neutronen voor zijn aantal protonen; een neutron wordt een proton.",
    ),
    klik(
        "Klik op de kern met te weinig neutronen.",
        NK.bestand, ZKE["B"],
        "Hij ligt aan de kant van te veel protonen: bèta-plus-verval brengt hem naar de strook.",
    ),
    klik(
        "Klik op de kern die het meest kans maakt op alfaverval.",
        NK.bestand, ZKE["D"],
        "Heel zware kernen worden lichter door een heliumkern uit te zenden.",
    ),
    met_prent(NK.bestand, keuze(
        "Bij zware kernen ligt de strook [[*aan de kant van meer neutronen|op de lijn N = Z]].",
        "Extra neutronen geven kernkracht zonder extra afstoting.",
    )),
    met_prent(NK.bestand, mk(
        "Kern A vervalt via bèta-min. In welke richting schuift hij op de kaart?",
        ["Eén naar links en één naar boven", "Eén naar rechts en één naar beneden", "Vier naar links en twee naar beneden", "Hij blijft op dezelfde plaats"],
        0,
        "N daalt met één, Z stijgt met één.",
    )),
    klik(
        "Klik op het ogenblik dat er nog een kwart van de kernen over is.",
        VK.bestand, ZPV["B"],
        "Twee halveringstijden: van 800 naar 200.",
    ),
    met_prent(VK.bestand, inv(
        "Lees de halveringstijd af, in uur.",
        ["6", "6 h", "6 uur"],
        "Na 6 h is 800 gedaald tot 400.",
    )),
    met_prent(VK.bestand, inv(
        "Hoeveel kernen (in 1000) zijn er na 24 uur nog over?",
        ["50", "50 000", "50000"],
        "Vier halveringstijden: 800 / 16 = 50.",
    )),
    met_prent(VK.bestand, mk(
        "Hoe groot is de desintegratieconstante van deze stof?",
        ["0,12 per uur", "6,0 per uur", "0,50 per uur", "4,2 per uur"],
        0,
        "λ = 0,693 / 6 h ≈ 0,12 per uur.",
    )),
    met_prent(VK.bestand, keuze(
        "De activiteit in punt A is [[*de helft van|even groot als]] de activiteit bij de start.",
        "A = λ · N, dus de activiteit daalt mee met N.",
    )),
    inv(
        "Hoeveel neutronen heeft lood-208, met Z = 82?",
        ["126"],
        "N = A − Z = 208 − 82.",
    ),
    mk(
        "Thorium-232 (Z = 90) doet alfaverval. Welke kern ontstaat?",
        ["A = 228 en Z = 88", "A = 232 en Z = 91", "A = 230 en Z = 89", "A = 228 en Z = 90"],
        0,
        "A daalt met 4, Z met 2: dat is radium.",
    ),
    mk(
        "Koolstof-14 (Z = 6) doet bèta-min-verval. Welke kern ontstaat?",
        ["Stikstof-14 met Z = 7", "Boor-14 met Z = 5", "Koolstof-13 met Z = 6", "Stikstof-15 met Z = 7"],
        0,
        "A blijft 14, Z stijgt met één.",
    ),
    mk(
        "Fluor-18 (Z = 9) doet bèta-plus-verval. Welke kern ontstaat?",
        ["Zuurstof-18 met Z = 8", "Neon-18 met Z = 10", "Fluor-17 met Z = 9", "Zuurstof-14 met Z = 7"],
        0,
        "Een proton wordt een neutron: Z daalt met één.",
    ),
    inv(
        "Een stof heeft een halveringstijd van 3 dagen. Welk deel is er na 15 dagen nog over? Schrijf als breuk.",
        ["1/32", "1 / 32"],
        "Vijf halveringstijden: (1/2)⁵.",
    ),
    mk(
        "Een bron heeft nu 1200 Bq. Na 20 jaar is dat 150 Bq. Hoe groot is de halveringstijd?",
        ["6,7 jaar", "10 jaar", "2,5 jaar", "20 jaar"],
        0,
        "1200 → 600 → 300 → 150: drie halveringstijden in 20 jaar.",
    ),
    casus(
        "In een houten voorwerp uit een opgraving is nog een kwart van de oorspronkelijke hoeveelheid koolstof-14 over. Koolstof-14 heeft een halveringstijd van 5730 jaar.",
        [
            inv(
                "Hoeveel halveringstijden zijn er voorbij?",
                ["2", "twee"],
                "Een kwart is (1/2)².",
            ),
            inv(
                "Hoe oud is het voorwerp, in jaar?",
                ["11460", "11 460", "ongeveer 11 460"],
                "2 · 5730 = 11 460 jaar.",
            ),
            keuze(
                "De klok begint te lopen wanneer de boom [[*sterft|geplant wordt]].",
                "Zolang hij leeft, neemt hij nieuwe koolstof-14 op.",
            ),
        ],
    ),
    tabel(
        "Wat verandert bij dit verval?",
        [
            ("alfaverval", "A en Z"),
            ("bèta-min-verval", "Alleen Z"),
            ("gammaverval", "Geen van beide"),
        ],
        "Bij bèta blijft het aantal nucleonen gelijk; gamma neemt alleen energie mee.",
        kolommen=["A en Z", "Alleen Z", "Geen van beide"],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Een radioactieve stof in de vriezer vervalt trager.", F),
            ("Na drie halveringstijden is nog een achtste over.", J),
            ("Een korte halveringstijd geeft een grote desintegratieconstante.", J),
            ("De sterke kernkracht werkt over grote afstanden.", F),
        ],
        "Verval trekt zich niets aan van temperatuur of druk.",
    ),
    koppel(
        "Koppel elk deeltje aan het verval waarbij het wegvliegt.",
        [
            ("heliumkern", "alfaverval"),
            ("elektron", "bèta-min-verval"),
            ("positron", "bèta-plus-verval"),
            ("energierijk foton", "gammaverval"),
        ],
        ["kernsplijting"],
        "Dit zijn de vier soorten van spontaan verval.",
    ),
    sorteer(
        "Zijn dit isotopen van hetzelfde element of niet?",
        ["Isotopen", "Geen isotopen"],
        [
            ("koolstof-12 en koolstof-14", "Isotopen"),
            ("uranium-235 en uranium-238", "Isotopen"),
            ("koolstof-14 en stikstof-14", "Geen isotopen"),
            ("kalium-40 en argon-40", "Geen isotopen"),
        ],
        "Isotopen hebben hetzelfde aantal protonen.",
    ),
    volgorde(
        "Uranium-238 vervalt in stappen. Zet deze kernen in de volgorde van de reeks.",
        ["uranium-238", "thorium-234", "protactinium-234", "uranium-234"],
        "Alfa (−4, −2), dan bèta-min (Z + 1), dan nog eens bèta-min.",
    ),
    mk(
        "Een radioactief preparaat bevat 4,0 · 10²⁰ kernen. De desintegratieconstante is 2,0 · 10⁻⁹ per seconde. Hoe groot is de activiteit?",
        ["8,0 · 10¹¹ Bq", "2,0 · 10²⁹ Bq", "4,0 · 10¹¹ Bq", "5,0 · 10⁻³⁰ Bq"],
        0,
        "A = λ · N = 2,0 · 10⁻⁹ · 4,0 · 10²⁰.",
    ),
    keuze(
        "Een nuclide met Z = 8 en N = 8 ligt [[*in de stabiliteitsband|ver buiten de stabiliteitsband]].",
        "Bij lichte kernen geldt N ≈ Z: dit is zuurstof-16.",
    ),
    mk(
        "Welke straling raakt een kern kwijt zonder dat het element verandert?",
        ["Gammastraling", "Alfastraling", "Bèta-min-straling", "Bèta-plus-straling"],
        0,
        "Bij gamma blijven A en Z gelijk; de kern verliest alleen energie.",
    ),
    inv(
        "Hoeveel protonen heeft een kern met A = 40 en N = 21?",
        ["19"],
        "Z = A − N = 40 − 21: dat is kalium-40.",
    ),
    sleep(
        "Het massagetal is het aantal [[nucleonen]]. Kernen met hetzelfde aantal protonen maar een ander aantal neutronen heten [[isotopen]]. De activiteit meet je in [[becquerel]].",
        ["elektronen", "sievert"],
        "Eén becquerel is één verval per seconde.",
    ),
    open_(
        "Leg uit waarom zware kernen meer neutronen dan protonen nodig hebben om stabiel te zijn.",
        "Protonen stoten elkaar elektrisch af, en die afstoting werkt over de hele kern. De sterke kernkracht trekt alle nucleonen aan, maar alleen over korte afstand. Extra neutronen leveren extra kernkracht zonder extra afstoting. Hoe groter de kern, hoe meer neutronen nodig zijn om de afstoting te compenseren.",
    ),
]
