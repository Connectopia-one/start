"""De gravitatiekracht en de cirkelbeweging — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Steen aan een touw ----------------------------------------------------------
CB = Prent("steen-aan-touw", "Een steen aan een touw draait tegen de wijzers van de klok in, van bovenaf gezien", "een cirkel met in het midden een hand; de steen zit rechts op de cirkel; vier pijlen vanuit de steen: A naar boven (raaklijn, in de draaizin), B naar het midden, C naar buiten, D naar beneden (raaklijn, tegen de draaizin)")
M = (420, 340)
R = 200
CB.svg(f'<circle cx="{M[0]}" cy="{M[1]}" r="{R}" fill="none" stroke="#9a9a9a" stroke-width="2" stroke-dasharray="8 6"/>')
CB.cirkel(*M, 16, "#f3e3c8", DONKER, 2)
ST = (M[0] + R, M[1])
CB.lijn(*M, *ST, DONKER, 2)
CB.pad(f"M {M[0] + 140 * math.cos(math.radians(-150)):.1f} {M[1] + 140 * math.sin(math.radians(-150)):.1f} A 140 140 0 0 0 {M[0] + 140 * math.cos(math.radians(150)):.1f} {M[1] + 140 * math.sin(math.radians(150)):.1f}", "none", GROEN, 3)
CB.pijl(M[0] + 140 * math.cos(math.radians(155)), M[1] + 140 * math.sin(math.radians(155)), M[0] + 140 * math.cos(math.radians(150)) + 2, M[1] + 140 * math.sin(math.radians(150)) + 6, GROEN, 3)
CB.cirkel(*ST, 18, GRIJS, DONKER, 2)
PL = {"A": (0, -1), "B": (-1, 0), "C": (1, 0), "D": (0, 1)}
LP = {}
for k, (dx, dy) in PL.items():
    CB.pijl(ST[0] + 22 * dx, ST[1] + 22 * dy, ST[0] + 150 * dx, ST[1] + 150 * dy, ORANJE, 5)
    LP[k] = (ST[0] + 180 * dx + (28 if dx == 0 else 0), ST[1] + 180 * dy + (0 if dx == 0 else -28))
    if k == "B":
        LP[k] = (ST[0] - 110, ST[1] + 36)
    CB.letter(*LP[k], k)
ZC = {k: [Prent.rond(ST[0] + 100 * dx, ST[1] + 100 * dy, 34), Prent.rond(*LP[k], 24)] for k, (dx, dy) in PL.items()}

# Drie satellietbanen ---------------------------------------------------------
SB = Prent("satellietbanen", "Drie satellieten met dezelfde massa in een cirkelbaan rond de aarde", "de aarde in het midden; drie cirkelbanen met straal r (P), 2r (Q) en 4r (R) gemeten vanaf het middelpunt van de aarde")
C0 = (500, 320)
for k, (r, h) in {"P": (65, 0), "Q": (130, 60), "R": (260, 130)}.items():
    SB.svg(f'<circle cx="{C0[0]}" cy="{C0[1]}" r="{r}" fill="none" stroke="#9a9a9a" stroke-width="2" stroke-dasharray="7 5"/>')
SB.cirkel(*C0, 40, "#7fb3d5", DONKER, 2)
SB.tekst(C0[0], C0[1] + 7, "aarde", 16, vet=True)
SATS = {"P": (65, -40), "Q": (130, 20), "R": (260, -25)}
LS = {}
for k, (r, g) in SATS.items():
    x, y = C0[0] + r * math.cos(math.radians(g)), C0[1] + r * math.sin(math.radians(g))
    SB.rect(x - 9, y - 9, 18, 18, ORANJE, DONKER, 2, 2)
    LS[k] = (x + 34, y - 26)
    SB.letter(*LS[k], k)
SB.tekst(C0[0], 620, "straal van de banen: P = r, Q = 2r, R = 4r", 18)
ZSB = {k: [Prent.rond(C0[0] + r * math.cos(math.radians(g)), C0[1] + r * math.sin(math.radians(g)), 24), Prent.rond(*LS[k], 22)] for k, (r, g) in SATS.items()}

VRAGEN = [
    klik(
        "Klik op de pijl die de zin van de versnelling van de steen toont.",
        CB.bestand, ZC["B"],
        "De middelpuntzoekende versnelling wijst naar het midden van de cirkel.",
    ),
    klik(
        "Het touw breekt op dit ogenblik. Klik op de pijl die toont waar de steen heen vliegt.",
        CB.bestand, ZC["A"],
        "Zonder kracht gaat de steen rechtdoor in de zin van zijn snelheid: raaklijnig, niet naar buiten.",
    ),
    met_prent(CB.bestand, tabel(
        "Welke pijl toont de zin van deze grootheid?",
        [
            ("de snelheid", "A"),
            ("de versnelling", "B"),
            ("de resulterende kracht", "B"),
        ],
        "Kracht en versnelling hebben dezelfde zin; de snelheid staat er loodrecht op.",
        kolommen=["A", "B", "C"],
    )),
    met_prent(CB.bestand, mk(
        "Welke kracht speelt hier de rol van middelpuntzoekende kracht?",
        ["De spankracht in het touw", "De zwaartekracht op de steen", "De luchtweerstand", "Een aparte middelpuntvliedende kracht"],
        0,
        "De middelpuntzoekende kracht is geen extra kracht, maar de rol die het touw speelt.",
    )),
    met_prent(CB.bestand, keuze(
        "Laat je de steen sneller ronddraaien op dezelfde cirkel, dan wordt de spankracht [[*groter|kleiner|niet anders]].",
        "F_c = m · v² / r.",
    )),
    klik(
        "Klik op de satelliet die het snelst beweegt.",
        SB.bestand, ZSB["P"],
        "v = √(G · M / r): hoe dichter bij de aarde, hoe sneller.",
    ),
    klik(
        "Klik op de satelliet met de langste omlooptijd.",
        SB.bestand, ZSB["R"],
        "Verder weg is de baan langer én de snelheid kleiner.",
    ),
    met_prent(SB.bestand, tabel(
        "Hoe groot is de baansnelheid, als P met snelheid v draait?",
        [
            ("P", "v"),
            ("Q", "v / √2"),
            ("R", "v / 2"),
        ],
        "v ~ 1 / √r: 2r geeft v / √2, 4r geeft v / √4.",
        kolommen=["v", "v / √2", "v / 2"],
    )),
    met_prent(SB.bestand, mk(
        "Op P werkt een gravitatiekracht F. Hoe groot is ze op R?",
        ["F / 16", "F / 4", "F / 2", "F"],
        0,
        "Vier keer zo ver: 4² = 16 keer zwakker.",
    )),
    met_prent(SB.bestand, keuze(
        "Een tweede satelliet met dubbele massa op baan Q gaat [[*even snel|half zo snel|twee keer zo snel]] als die op Q.",
        "De massa van de satelliet valt weg uit v = √(G · M / r).",
    )),
    inv(
        "Een wiel draait 90 keer per minuut rond. Wat is de frequentie, in Hz?",
        ["1,5", "1,5 Hz", "1.5"],
        "f = 90 / 60 = 1,5 Hz.",
    ),
    inv(
        "Een lichaam draait rond met een periode van 0,50 s. Hoe groot is de hoeksnelheid, in rad/s? Rond af op één decimaal.",
        ["12,6", "12,6 rad/s", "4π", "12.6"],
        "ω = 2π / T = 2π / 0,50 = 4π ≈ 12,6 rad/s.",
    ),
    inv(
        "Een auto rijdt met 20 m/s door een bocht met straal 50 m. Hoe groot is de middelpuntzoekende versnelling, in m/s²?",
        ["8", "8,0", "8 m/s²", "8,0 m/s²"],
        "a_c = v² / r = 400 / 50 = 8,0 m/s².",
    ),
    inv(
        "Hoe groot is de middelpuntzoekende kracht op een auto van 1000 kg die met 15 m/s door een bocht met straal 45 m rijdt, in N?",
        ["5000", "5000 N", "5,0 kN", "5 kN"],
        "F_c = m · v² / r = 1000 · 225 / 45 = 5000 N.",
    ),
    mk(
        "Een kind op een draaimolen zit op 3,0 m van het midden. Eén ronde duurt 6,0 s. Hoe snel beweegt het kind?",
        ["3,1 m/s", "0,50 m/s", "18 m/s", "1,0 m/s"],
        0,
        "v = 2π · r / T = 2π · 3,0 / 6,0 ≈ 3,1 m/s.",
    ),
    mk(
        "Een auto neemt dezelfde bocht twee keer zo snel. Hoeveel wrijvingskracht is er nodig om in de bocht te blijven?",
        ["4 keer zoveel", "2 keer zoveel", "evenveel", "de helft"],
        0,
        "F_c = m · v² / r: de snelheid staat in het kwadraat.",
    ),
    mk(
        "Je verdubbelt één van twee massa's en ook de afstand ertussen. Wat gebeurt er met de gravitatiekracht?",
        ["Ze wordt de helft", "Ze blijft gelijk", "Ze wordt 2 keer zo groot", "Ze wordt 4 keer zo klein"],
        0,
        "× 2 voor de massa en ÷ 4 voor de afstand: samen ÷ 2.",
    ),
    mk(
        "Hoe groot is de gravitatiekracht tussen twee massa's van 1000 kg op 1,0 m van elkaar? Neem G = 6,67 · 10⁻¹¹ N·m²/kg².",
        ["6,7 · 10⁻⁵ N", "6,7 · 10⁻⁸ N", "6,7 · 10⁻² N", "9,8 · 10³ N"],
        0,
        "F = G · m₁ · m₂ / r² = 6,67 · 10⁻¹¹ · 10⁶ / 1 ≈ 6,7 · 10⁻⁵ N: heel klein.",
    ),
    mk(
        "Een planeet heeft twee keer de massa en twee keer de straal van de aarde. Hoe groot is g aan haar oppervlak?",
        ["Half zo groot als op aarde", "Twee keer zo groot als op aarde", "Even groot als op aarde", "Vier keer zo groot als op aarde"],
        0,
        "g = G · M / R²: × 2 en ÷ 4 geeft ÷ 2.",
    ),
    mk(
        "Op welke hoogte boven het aardoppervlak is g vier keer kleiner dan aan het oppervlak?",
        ["Eén aardstraal hoog", "Twee aardstralen hoog", "Vier aardstralen hoog", "Een halve aardstraal hoog"],
        0,
        "g ~ 1 / r²: r moet 2 keer zo groot zijn, dus 2R vanaf het middelpunt, één R boven het oppervlak.",
    ),
    mk(
        "Hoe snel draait een satelliet op r = 1,0 · 10⁷ m van het middelpunt van de aarde? Neem G · M = 4,0 · 10¹⁴ m³/s².",
        ["6,3 km/s", "40 km/s", "2,0 km/s", "0,63 km/s"],
        0,
        "v = √(G · M / r) = √(4,0 · 10⁷) ≈ 6,3 · 10³ m/s.",
    ),
    casus(
        "Op een draaimolen die in 5,0 s één ronde draait, zit Mila op 1,5 m en Arno op 3,0 m van het midden.",
        [
            keuze(
                "Mila en Arno hebben [[*dezelfde|een verschillende]] hoeksnelheid.",
                "Ze doen er allebei 5,0 s over per ronde.",
            ),
            mk(
                "Hoe verhoudt de baansnelheid van Arno zich tot die van Mila?",
                ["Twee keer zo groot", "Even groot", "De helft", "Vier keer zo groot"],
                0,
                "v = ω · r, en Arno zit twee keer zo ver.",
            ),
            mk(
                "Hoe verhoudt de middelpuntzoekende versnelling van Arno zich tot die van Mila?",
                ["Twee keer zo groot", "Vier keer zo groot", "Even groot", "De helft"],
                0,
                "a_c = ω² · r: bij dezelfde ω evenredig met r.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("De middelpuntzoekende kracht is een extra kracht naast de andere krachten.", F),
            ("Bij een eenparig cirkelvormige beweging is de versnelling nul.", F),
            ("Op de maan is je massa kleiner dan op aarde.", F),
            ("Een zware en een lichte satelliet op dezelfde baan gaan even snel.", J),
        ],
        "De richting van v verandert, dus is er wel een versnelling.",
    ),
    sorteer(
        "Welke kracht speelt de rol van middelpuntzoekende kracht?",
        ["Wrijving", "Spankracht", "Gravitatie"],
        [
            ("een auto in een bocht", "Wrijving"),
            ("de maan rond de aarde", "Gravitatie"),
            ("een kogel aan een touw bij het kogelslingeren", "Spankracht"),
            ("een satelliet rond de aarde", "Gravitatie"),
            ("een fietser in een bocht op een vlakke weg", "Wrijving"),
        ],
        "Telkens een bestaande kracht die naar het midden wijst.",
    ),
    koppel(
        "Koppel elke grootheid aan haar formule.",
        [
            ("hoeksnelheid", "2π / T"),
            ("baansnelheid", "ω · r"),
            ("middelpuntzoekende versnelling", "v² / r"),
            ("gravitatiekracht", "G · m₁ · m₂ / r²"),
        ],
        ["m · v"],
        "Bij een satelliet zet je F_g gelijk aan m · v² / r.",
    ),
    keuze(
        "Een satelliet die verder van de aarde draait, beweegt [[*trager|sneller]] en doet [[korter|*langer]] over één omloop.",
        "v = √(G · M / r).",
    ),
    sleep(
        "Bij een satelliet speelt de [[gravitatiekracht]] de rol van [[middelpuntzoekende]] kracht. De versnelling wijst naar het [[middelpunt]] van de baan.",
        ["middelpuntvliedende", "raaklijn"],
        "Zo valt de satelliet voortdurend rond de aarde.",
    ),
    open_(
        "Leg uit waarom astronauten in het ruimtestation zweven, terwijl de zwaartekracht daar nog bijna even sterk is als op aarde.",
        "Het ruimtestation en de astronauten vallen samen voortdurend rond de aarde: de gravitatiekracht houdt ze in hun cirkelbaan. Omdat ze allemaal dezelfde versnelling hebben, duwt de vloer niet tegen de astronauten. Ze voelen zich gewichtloos, ook al werkt de gravitatie nog volop.",
    ),
]
