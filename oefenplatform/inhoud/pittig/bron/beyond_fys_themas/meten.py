"""Meten en meetresultaten verwerken — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Analoge voltmeter ------------------------------------------------------------------
VM = Prent("analoge-voltmeter", "Een analoge voltmeter en drie ogen die de naald aflezen", "een halve cirkelschaal van 0 tot 10 V met een streepje per 0,2 V en een getal bij elke volt; de naald wijst 6,4 V aan; boven de meter drie ogen: A links schuin, B recht boven de naald, C rechts schuin")
CX, CY, R = 500, 520, 300
VM.rect(170, 180, 660, 380, "#f7f4ea", DONKER, 20, 3)
for i in range(51):
    a = math.radians(150 - 120 * i / 50)
    lang = 26 if i % 5 == 0 else 14
    x1, y1 = CX + R * math.cos(a), CY - R * math.sin(a)
    x2, y2 = CX + (R - lang) * math.cos(a), CY - (R - lang) * math.sin(a)
    VM.lijn(x1, y1, x2, y2, DONKER, 3 if i % 5 == 0 else 2)
    if i % 5 == 0:
        VM.tekst(CX + (R - 52) * math.cos(a), CY - (R - 52) * math.sin(a) + 7, str(i // 5), 20, vet=True)
VM.tekst(CX, CY - 90, "V", 28, vet=True)
an = math.radians(150 - 120 * 6.4 / 10)
VM.lijn(CX, CY, CX + (R + 10) * math.cos(an), CY - (R + 10) * math.sin(an), ROOD, 4)
VM.cirkel(CX, CY, 12, DONKER, DONKER, 1)
NX = CX + (R + 10) * math.cos(an)
OOG = {"A": (NX - 230, 90), "B": (NX, 90), "C": (NX + 230, 90)}
for k, (x, y) in OOG.items():
    VM.ellips(x, y, 30, 16, "#ffffff", DONKER, 2)
    VM.cirkel(x, y, 8, DONKER, DONKER, 1)
    VM.letter(x + 52, y - 10, k)
ZOOG = {k: [Prent.rond(x, y, 36), Prent.rond(x + 52, y - 10, 22)] for k, (x, y) in OOG.items()}

# Vier verbanden ---------------------------------------------------------------------
VB = Prent("vier-verbanden", "Vier grafieken met een ander verband tussen x en y", "vier kleine grafieken: A een rechte door de oorsprong, B een dalende kromme die beide assen nadert, C een stijgende parabool vanuit de oorsprong, D een stijgende rechte die de y-as boven de oorsprong snijdt")
VAK = {"A": (70, 80), "B": (530, 80), "C": (70, 360), "D": (530, 360)}
W, H = 400, 230
for k, (x0, y0) in VAK.items():
    ox, oy = x0 + 40, y0 + H - 20
    VB.pijl(ox, oy, x0 + W - 10, oy, DONKER, 2)
    VB.pijl(ox, oy, ox, y0 + 10, DONKER, 2)
    VB.tekst(x0 + W - 14, oy + 22, "x", 16, anker="end")
    VB.tekst(ox - 14, y0 + 24, "y", 16)
    f = {
        "A": lambda t: 0.9 * t,
        "B": lambda t: min(1.0, 0.1 / max(t, 0.01)),
        "C": lambda t: 0.95 * t * t,
        "D": lambda t: 0.3 + 0.6 * t,
    }[k]
    t0 = 0.1 if k == "B" else 0
    pts = [(t0 + (1 - t0) * i / 100) for i in range(101)]
    VB.pad("M " + " L ".join(f"{ox + t * (W - 70):.1f} {oy - f(t) * (H - 50):.1f}" for t in pts), "none", BLAUW, 4)
    VB.letter(x0 + W - 30, y0 + 30, k)
ZVB = {k: [Prent.zone(x0, y0, W, H)] for k, (x0, y0) in VAK.items()}

VRAGEN = [
    met_prent(VM.bestand, inv(
        "Lees de spanning af, in V.",
        ["6,4", "6,4 V", "6.4"],
        "Elk klein streepje is 0,2 V; de naald staat twee streepjes voorbij 6.",
    )),
    met_prent(VM.bestand, mk(
        "Hoe groot is de nauwkeurigheid van deze schaal?",
        ["0,2 V", "1 V", "0,1 V", "10 V"],
        0,
        "Tussen twee getallen liggen vijf streepjes.",
    )),
    klik(
        "Klik op het oog dat de naald correct afleest.",
        VM.bestand, ZOOG["B"],
        "Je kijkt recht van boven, anders lijkt de naald verschoven.",
    ),
    met_prent(VM.bestand, keuze(
        "Oog A en oog C lezen elk [[*een andere|dezelfde]] verkeerde waarde af.",
        "Wie schuin kijkt, ziet de naald verschoven tegen de schaal, telkens naar de andere kant.",
    )),
    met_prent(VM.bestand, mk(
        "Je verwacht een spanning van ongeveer 15 V. Wat doe je met deze meter?",
        ["Een meter met een groter bereik nemen", "Gewoon meten, de naald stopt wel op 10", "Twee keer meten en de waarden optellen", "Heel goed recht van boven kijken"],
        0,
        "Buiten het meetbereik meet je onbetrouwbaar en kan het toestel stuk.",
    )),
    klik(
        "Klik op het recht evenredig verband.",
        VB.bestand, ZVB["A"],
        "Een rechte door de oorsprong: y = k · x.",
    ),
    klik(
        "Klik op de grafiek van p · V = constant bij een gas.",
        VB.bestand, ZVB["B"],
        "Omgekeerd evenredig: het product blijft gelijk.",
    ),
    klik(
        "Klik op de grafiek van de afgelegde weg tegen de tijd bij een vrije val vanuit stilstand.",
        VB.bestand, ZVB["C"],
        "s = g · t² / 2: kwadratisch.",
    ),
    met_prent(VB.bestand, tabel(
        "Welk verband toont deze grafiek?",
        [
            ("A", "Recht evenredig"),
            ("B", "Omgekeerd evenredig"),
            ("D", "Lineair, niet evenredig"),
        ],
        "Een rechte die niet door de oorsprong gaat, is lineair maar niet evenredig.",
        kolommen=["Recht evenredig", "Omgekeerd evenredig", "Lineair, niet evenredig"],
    )),
    inv(
        "Een auto rijdt 72 km/h. Hoeveel is dat in m/s?",
        ["20", "20 m/s"],
        "72 / 3,6 = 20.",
    ),
    mk(
        "Hoeveel is 350 nm in meter?",
        ["3,5 · 10⁻⁷ m", "3,5 · 10⁻⁶ m", "3,5 · 10⁻¹¹ m", "3,5 · 10⁻⁴ m"],
        0,
        "Nano is 10⁻⁹: 350 · 10⁻⁹ = 3,5 · 10⁻⁷.",
    ),
    inv(
        "Hoeveel is 2,2 MΩ in ohm?",
        ["2200000", "2 200 000", "2,2 · 10⁶"],
        "Mega is 10⁶.",
    ),
    mk(
        "Hoeveel beduidende cijfers heeft 4,050 · 10³ m?",
        ["Vier", "Drie", "Twee", "Vijf"],
        0,
        "Alle cijfers in de mantisse tellen, ook de nullen.",
    ),
    mk(
        "Je meet 3,6 m en 2,15 s. Hoe schrijf je de snelheid?",
        ["1,7 m/s", "1,674 m/s", "1,67442 m/s", "2 m/s"],
        0,
        "Bij delen telt het kleinste aantal beduidende cijfers: twee.",
    ),
    inv(
        "Schrijf 0,000 082 in wetenschappelijke notatie.",
        ["8,2 · 10⁻⁵", "8,2e-5", "8,2 · 10^-5", "8,2 x 10⁻⁵"],
        "Eén cijfer verschillend van nul voor de komma.",
    ),
    mk(
        "Je weet dat Ek = m · v² / 2. Hoe druk je v uit?",
        ["v = √(2 · Ek / m)", "v = 2 · Ek / m", "v = √(Ek / (2 · m))", "v = Ek · m / 2"],
        0,
        "Eerst v² = 2 · Ek / m, dan de wortel.",
    ),
    casus(
        "Een leerling meet de valtijd van een kogel van 1,0 m hoogte met een handchronometer. Ze vindt 0,62 s, 0,38 s, 0,47 s en 0,45 s.",
        [
            mk(
                "Welke meting vertrouw je het minst?",
                ["0,62 s", "0,38 s", "0,47 s", "0,45 s"],
                0,
                "Ze ligt het verst van de andere.",
            ),
            keuze(
                "Een sensor met een lichtpoortje geeft hier een [[*betrouwbaardere|minder betrouwbare]] meting.",
                "Je reactietijd valt weg.",
            ),
            mk(
                "Welke uitkomst is realistisch als je schat met g ≈ 10 m/s²?",
                ["ongeveer 0,45 s", "ongeveer 4,5 s", "ongeveer 0,045 s", "ongeveer 45 s"],
                0,
                "t = √(2 · 1,0 / 10) ≈ 0,45 s.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak over veilig werken en meten?",
        [
            ("Batterijen van meetmateriaal gooi je bij het restafval.", F),
            ("Een spanningsbron zet je op de laagste stand voor je hem aansluit.", J),
            ("Een onwaarschijnlijke uitkomst controleer je eerst.", J),
            ("Met natte handen bedien je een toestel veilig als het uit staat.", F),
        ],
        "Water verlaagt de weerstand van je huid; batterijen zijn klein gevaarlijk afval.",
    ),
    koppel(
        "Koppel elke meting aan het juiste toestel.",
        [
            ("de kracht in een veer", "dynamometer"),
            ("het geluid op een fuif", "decibelmeter"),
            ("de stroom door een lamp", "multimeter"),
            ("de snelheid van een karretje", "bewegingssensor"),
        ],
        ["thermometer"],
        "Kies het toestel dat bij de grootheid en het bereik past.",
    ),
    volgorde(
        "Zet deze voorvoegsels van groot naar klein.",
        ["mega", "kilo", "milli", "micro", "nano"],
        "10⁶, 10³, 10⁻³, 10⁻⁶, 10⁻⁹.",
    ),
    sorteer(
        "Is dit een SI-basiseenheid of een afgeleide eenheid?",
        ["Basiseenheid", "Afgeleide eenheid"],
        [
            ("meter", "Basiseenheid"),
            ("kilogram", "Basiseenheid"),
            ("ampère", "Basiseenheid"),
            ("newton", "Afgeleide eenheid"),
            ("joule", "Afgeleide eenheid"),
        ],
        "De newton is kg · m/s², de joule N · m.",
    ),
    keuze(
        "Bij het optellen van 12,4 m en 3,256 m schrijf je de som met [[*één cijfer|drie cijfers]] na de komma.",
        "De minst precieze meting bepaalt het aantal decimalen: 15,7 m.",
    ),
    inv(
        "Hoeveel is 0,45 μA in ampère? Schrijf in wetenschappelijke notatie.",
        ["4,5 · 10⁻⁷", "4,5 · 10⁻⁷ A", "4,5e-7"],
        "Micro is 10⁻⁶: 0,45 · 10⁻⁶ = 4,5 · 10⁻⁷ A.",
    ),
    mk(
        "Je combineert v = s / t met s = 120 m en v = 15 m/s. Hoe groot is t?",
        ["8,0 s", "1800 s", "0,13 s", "105 s"],
        0,
        "t = s / v = 120 / 15.",
    ),
    mk(
        "Een leerling rekent uit dat een fietser 250 m/s rijdt. Wat doe je best?",
        ["De berekening nakijken, want dat kan niet", "Het zo noteren, de rekenmachine liegt niet", "Afronden tot 300 m/s", "Omzetten naar km/h en zo laten"],
        0,
        "Een schatting vooraf toont meteen dat dit onzin is.",
    ),
    keuze(
        "Als y en x omgekeerd evenredig zijn, blijft [[*het product x · y|het quotiënt y / x]] constant.",
        "x · y = k.",
    ),
    sleep(
        "De kleinste en grootste waarde die een toestel kan meten, heten samen het [[meetbereik]]. Het kleinste verschil dat het nog aanwijst, is de [[nauwkeurigheid]]. Een kracht meet je met een [[dynamometer]].",
        ["chronometer", "eenheid"],
        "Kies je toestel op basis van bereik en nauwkeurigheid.",
    ),
    open_(
        "Leg uit waarom je de uitkomst van een berekening niet met alle cijfers van je rekenmachine opschrijft.",
        "Een meting heeft een beperkte nauwkeurigheid. Schrijf je alle cijfers van de rekenmachine op, dan lijkt je antwoord veel nauwkeuriger dan je meting ooit was. Daarom rond je af op het aantal beduidende cijfers van de minst nauwkeurige meting.",
    ),
]
