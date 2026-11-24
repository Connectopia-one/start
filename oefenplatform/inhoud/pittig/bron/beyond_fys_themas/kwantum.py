"""Kwantumfysica: foto-elektrisch effect en dualiteit — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Kinetische energie tegen frequentie voor twee metalen ------------------------------
EK = Prent("ek-frequentie", "Hoeveel bewegingsenergie krijgt een losgeslagen elektron?", "grafiek van de maximale kinetische energie in 10⁻¹⁹ J tegen de frequentie in 10¹⁴ Hz; twee evenwijdige rechten: metaal A snijdt de f-as bij 5, metaal B bij 8; punten P (op A bij f = 9), Q (op B bij f = 9), R (snijpunt van A met de as), S (snijpunt van B met de as)")
X, Y = assen(EK, 0, 12, 0, 5, "f (10¹⁴ Hz)", "Ek,max (10⁻¹⁹ J)", 1, 1, links=130, rechts=900)
H = 0.663  # in 10^-19 J per 10^14 Hz
for naam, f0, kl in (("A", 5, BLAUW), ("B", 8, ORANJE)):
    EK.lijn(X(f0), Y(0), X(12), Y(H * (12 - f0)), kl, 4)
    EK.tekst(X(12) - 10, Y(H * (12 - f0)) - 14, f"metaal {naam}", 16, anker="end", kleur=kl, vet=True)
PU = {"P": (9, H * 4), "Q": (9, H * 1), "R": (5, 0), "S": (8, 0)}
LPU = {}
for k, (f, e) in PU.items():
    EK.cirkel(X(f), Y(e), 8, DONKER, DONKER, 1)
    LPU[k] = (X(f) - 32, Y(e) - 30)
    EK.letter(*LPU[k], k)
ZPU = {k: [Prent.rond(X(f), Y(e), 22), Prent.rond(*LPU[k], 22)] for k, (f, e) in PU.items()}

# Vier lampen op een metaalplaat -----------------------------------------------------
LA = Prent("vier-lampen", "Vier lampen schijnen op dezelfde metaalplaat", "een metaalplaat met drempelfrequentie 6,0 · 10¹⁴ Hz; vier lampen boven de plaat: A rood 4,3 · 10¹⁴ Hz fel, B groen 5,7 · 10¹⁴ Hz fel, C blauw 6,7 · 10¹⁴ Hz zwak, D uv 9,0 · 10¹⁴ Hz zwak")
LA.rect(80, 470, 840, 50, "#c9ccd1", DONKER, 6, 2)
LA.tekst(500, 552, "metaalplaat: f₀ = 6,0 · 10¹⁴ Hz", 20, vet=True)
LAMP = {"A": (180, ROOD, "4,3", "fel"), "B": (390, GROEN, "5,7", "fel"), "C": (610, BLAUW, "6,7", "zwak"), "D": (820, PAARS, "9,0", "zwak")}
for k, (x, kl, f, st) in LAMP.items():
    LA.rect(x - 60, 120, 120, 70, kl, DONKER, 14, 2)
    LA.tekst(x, 162, f"{f} · 10¹⁴ Hz", 15, kleur="#ffffff", vet=True)
    LA.tekst(x, 220, st, 18)
    n = 5 if st == "fel" else 2
    for j in range(n):
        dx = (j - (n - 1) / 2) * 22
        LA.lijn(x + dx, 240, x + dx * 2, 455, kl, 3, stippel=True)
    LA.letter(x, 90, k)
ZLA = {k: [Prent.zone(x - 70, 70, 140, 400)] for k, (x, *_r) in LAMP.items()}

VRAGEN = [
    klik(
        "Klik op de drempelfrequentie van metaal B.",
        EK.bestand, ZPU["S"],
        "Daar is de energie van het foton net genoeg om een elektron los te maken.",
    ),
    klik(
        "Bij dezelfde frequentie: klik op het elektron met de meeste bewegingsenergie.",
        EK.bestand, ZPU["P"],
        "Metaal A heeft een lagere uittree-energie, dus blijft er meer over.",
    ),
    met_prent(EK.bestand, keuze(
        "De twee rechten lopen evenwijdig omdat hun helling voor elk metaal [[*de constante van Planck|de drempelfrequentie]] is.",
        "Ek,max = h · f − h · f₀: de helling is h.",
    )),
    met_prent(EK.bestand, mk(
        "Licht van 6 · 10¹⁴ Hz valt op beide metalen. Wat gebeurt er?",
        ["Alleen uit A komen elektronen los", "Alleen uit B komen elektronen los", "Uit beide komen elektronen los", "Uit geen van beide"],
        0,
        "6 ligt boven de drempel van A (5) maar onder die van B (8).",
    )),
    met_prent(EK.bestand, inv(
        "Bereken de uittree-energie van metaal A, in 10⁻¹⁹ J. Neem h = 6,63 · 10⁻³⁴ J·s.",
        ["3,3", "3,32", "3,315", "3,3 · 10⁻¹⁹ J"],
        "h · f₀ = 6,63 · 10⁻³⁴ · 5 · 10¹⁴ ≈ 3,3 · 10⁻¹⁹ J.",
    )),
    klik(
        "Klik op een lamp die geen enkel elektron losmaakt, ook al schijnt ze fel.",
        LA.bestand, ZLA["A"] + ZLA["B"],
        "Rood en groen liggen onder de drempelfrequentie; feller maakt dat niet goed.",
    ),
    klik(
        "Klik op de lamp die de snelste elektronen losmaakt.",
        LA.bestand, ZLA["D"],
        "De hoogste frequentie geeft de meeste energie per foton.",
    ),
    met_prent(LA.bestand, tabel(
        "Klopt dit?",
        [
            ("Lamp C maakt elektronen los, al schijnt ze zwak.", J),
            ("Maak je lamp B nog feller, dan komen er toch elektronen los.", F),
            ("Maak je lamp D feller, dan komen er meer elektronen los.", J),
            ("Maak je lamp D feller, dan krijgt elk elektron meer energie.", F),
        ],
        "De frequentie beslist óf er elektronen loskomen en hoe snel; de intensiteit beslist hoeveel.",
    )),
    mk(
        "Hoe groot is de energie van een foton met f = 6,0 · 10¹⁴ Hz? Neem h = 6,63 · 10⁻³⁴ J·s.",
        ["4,0 · 10⁻¹⁹ J", "1,1 · 10⁻⁴⁸ J", "9,1 · 10⁻¹⁹ J", "6,6 · 10⁻²⁰ J"],
        0,
        "E = h · f = 6,63 · 10⁻³⁴ · 6,0 · 10¹⁴.",
    ),
    mk(
        "Een foton heeft 5,0 · 10⁻¹⁹ J. Het metaal vraagt 3,0 · 10⁻¹⁹ J om een elektron los te maken. Hoeveel bewegingsenergie krijgt het elektron hoogstens?",
        ["2,0 · 10⁻¹⁹ J", "8,0 · 10⁻¹⁹ J", "3,0 · 10⁻¹⁹ J", "5,0 · 10⁻¹⁹ J"],
        0,
        "Wat overblijft na het losmaken, wordt bewegingsenergie.",
    ),
    inv(
        "Een metaal vraagt 4,0 · 10⁻¹⁹ J per elektron. Hoe groot is de drempelfrequentie, in 10¹⁴ Hz? Neem h = 6,63 · 10⁻³⁴ J·s.",
        ["6,0", "6", "6,03", "6,0 · 10¹⁴ Hz"],
        "f₀ = E / h = 4,0 · 10⁻¹⁹ / 6,63 · 10⁻³⁴ ≈ 6,0 · 10¹⁴ Hz.",
    ),
    mk(
        "De golflengte van licht wordt drie keer zo klein. Hoe verandert de energie van één foton?",
        ["Ze wordt drie keer zo groot", "Ze wordt drie keer zo klein", "Ze wordt negen keer zo groot", "Ze blijft dezelfde waarde"],
        0,
        "E = h · c / λ: omgekeerd evenredig met λ.",
    ),
    tabel(
        "Pleit dit voor het golfmodel of het deeltjesmodel?",
        [
            ("interferentie bij de proef van Young", "Golfmodel"),
            ("het bestaan van een drempelfrequentie", "Deeltjesmodel"),
            ("een buigingspatroon van elektronen op nikkel", "Golfmodel"),
            ("een elektron dat de energie van één foton opneemt", "Deeltjesmodel"),
        ],
        "Licht en materie tonen allebei beide gezichten.",
        kolommen=["Golfmodel", "Deeltjesmodel"],
    ),
    casus(
        "In een tweespletenproef vuurt men elektronen één per één af op een scherm. Na tien elektronen zie je tien losse puntjes. Na tienduizend elektronen zie je strepen.",
        [
            mk(
                "Wat zijn de strepen?",
                ["Een interferentiepatroon", "De schaduw van de spleten", "Sporen van twee elektronen samen", "Een fout van het scherm"],
                0,
                "Elk elektron gaat als golf door beide spleten.",
            ),
            keuze(
                "Elk elektron komt aan als [[*één puntje|een uitgesmeerde streep]].",
                "Bij de meting gedraagt het zich als deeltje.",
            ),
            keuze(
                "De golffunctie geeft voor elk punt van het scherm [[*de kans|de zekerheid]] dat een elektron daar aankomt.",
                "Pas na veel elektronen zie je die kansverdeling.",
            ),
        ],
    ),
    mk(
        "Waarom heeft een vallende tennisbal geen merkbare golflengte?",
        ["Door zijn grote impuls is λ extreem klein", "Omdat hij elektrisch volledig neutraal is", "Omdat hij veel te traag door de lucht gaat", "Omdat hij steeds botst met luchtdeeltjes"],
        0,
        "λ = h / (m · v): een grote massa geeft een piepkleine golflengte.",
    ),
    keuze(
        "Hoe scherper je de plaats van een elektron kent, hoe [[*vager|scherper]] je zijn impuls kent.",
        "Het onzekerheidsbeginsel van Heisenberg.",
    ),
    mk(
        "Een fotocel in een deur werkt niet meer na een nieuwe lamp. Wat is de meest waarschijnlijke oorzaak?",
        ["Het licht heeft een te lage frequentie", "De nieuwe lamp schijnt veel te fel op de cel", "De lamp stuurt te veel fotonen per seconde", "De cel kreeg te veel licht en is opgebruikt"],
        0,
        "Onder de drempelfrequentie komt er geen enkel elektron los.",
    ),
    sorteer(
        "Is dit het foto-elektrisch effect of niet?",
        ["Foto-elektrisch effect", "Iets anders"],
        [
            ("een zonnepaneel dat stroom levert", "Foto-elektrisch effect"),
            ("een lichtsensor in een rookdetector", "Foto-elektrisch effect"),
            ("een spiegel die licht weerkaatst", "Iets anders"),
            ("een lens die een beeld maakt", "Iets anders"),
        ],
        "Licht dat ladingen losmaakt, is het foto-elektrisch effect.",
    ),
    koppel(
        "Koppel elk begrip aan zijn betekenis.",
        [
            ("drempelfrequentie", "de laagste frequentie die nog elektronen losmaakt"),
            ("orbitaal", "gebied waar een elektron met grote kans zit"),
            ("golffunctie", "beschrijft de kans om een deeltje ergens te vinden"),
            ("dualiteit", "zowel golf- als deeltjesgedrag"),
        ],
        ["vaste cirkelbaan rond de kern"],
        "In de kwantumfysica bestaat geen vaste baan.",
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Feller rood licht maakt uiteindelijk toch elektronen los.", F),
            ("Een elektron kan buigen rond kleine obstakels.", J),
            ("Na een meting valt de golffunctie samen tot één uitkomst.", J),
            ("Het onzekerheidsbeginsel verdwijnt met betere toestellen.", F),
        ],
        "Het is een eigenschap van de natuur zelf.",
    ),
    mk(
        "Wat toonde de proef van Davisson en Germer aan?",
        ["Elektronen kunnen buigen als golven", "Licht bestaat uit pakketjes energie", "Elektronen dragen een negatieve lading", "Atomen hebben een kleine, zware kern"],
        0,
        "Ze zagen een buigingspatroon op het kristal.",
    ),
    volgorde(
        "Zet deze fotonen van weinig naar veel energie.",
        ["infrarood", "rood licht", "blauw licht", "uv-straling"],
        "De energie stijgt met de frequentie.",
    ),
    inv(
        "Een foton heeft 3,3 · 10⁻¹⁹ J. Welke frequentie heeft het, in 10¹⁴ Hz? Neem h = 6,63 · 10⁻³⁴ J·s.",
        ["5,0", "5", "4,98", "5,0 · 10¹⁴ Hz"],
        "f = E / h ≈ 5,0 · 10¹⁴ Hz.",
    ),
    mk(
        "Je verdubbelt de frequentie van het licht op een metaal, ruim boven de drempel. Wat gebeurt er met de maximale bewegingsenergie van de elektronen?",
        ["Ze wordt meer dan dubbel zo groot", "Ze wordt precies dubbel zo groot", "Ze blijft even groot als ervoor", "Ze daalt want er zijn meer fotonen"],
        0,
        "Ek = h · f − h · f₀: het vaste stuk h · f₀ gaat er telkens af.",
    ),
    keuze(
        "Een elektron neemt bij het foto-elektrisch effect de energie op van [[*één foton|meerdere fotonen samen]].",
        "Daarom telt de energie per foton, niet de totale hoeveelheid licht.",
    ),
    mk(
        "Welk toestel gebruikt het golfkarakter van elektronen?",
        ["Een elektronenmicroscoop", "Een zonnepaneel op het dak", "Een gloeilamp", "Een fotocel in een deur"],
        0,
        "De kleine golflengte van elektronen geeft veel scherpere beelden dan licht.",
    ),
    sleep(
        "De energie van een foton is E = [[h]] · f. Licht onder de [[drempelfrequentie]] maakt geen elektronen los. Een grotere intensiteit geeft [[meer]] elektronen.",
        ["snellere", "λ"],
        "De frequentie bepaalt de energie per elektron.",
    ),
    open_(
        "Leg uit waarom het golfmodel van licht het foto-elektrisch effect niet kan verklaren.",
        "In het golfmodel stapelt energie zich op naarmate het licht feller is of langer schijnt, dus zou ook fel rood licht ooit elektronen losmaken. In werkelijkheid komt er onder de drempelfrequentie nooit een elektron los. Dat kan je enkel verklaren als licht in pakketjes (fotonen) met E = h · f komt en één elektron de energie van één foton opneemt.",
    ),
]
