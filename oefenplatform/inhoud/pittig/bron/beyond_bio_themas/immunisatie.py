"""Immunisatie, bloedgroepen en falende afweer — pittig (🧬 Beyond doorstroom, biologie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Bloedgroepkaart --------------------------------------------------------
BG = Prent("bloedgroep-test", "Bloedgroeptest van vier personen", "tabel met rijen W, X, Y, Z en kolommen anti-A, anti-B, anti-D; een gespikkelde druppel betekent samenklonteren")
KOL = ["anti-A", "anti-B", "anti-D"]
RIJ = {"W": (1, 0, 1), "X": (0, 0, 0), "Y": (1, 1, 1), "Z": (0, 1, 0)}
import random
random.seed(7)
for j, t in enumerate(KOL):
    BG.tekst(360 + j * 200, 110, t, 20, vet=True)
for i, (naam, uitslag) in enumerate(RIJ.items()):
    y = 180 + i * 115
    BG.letter(150, y, naam)
    for j, klont in enumerate(uitslag):
        x = 360 + j * 200
        BG.cirkel(x, y, 42, "#e2a0a0" if klont else "#d9534f", DONKER, 2)
        if klont:
            for _ in range(14):
                BG.cirkel(x + random.randint(-26, 26), y + random.randint(-26, 26), random.randint(4, 8), "#8b1e1e", "none", 0)
ZBG = {naam: [Prent.zone(110, 180 + i * 115 - 50, 760, 100)] for i, naam in enumerate(RIJ)}

# Hiv-verloop ------------------------------------------------------------
HV = Prent("hiv-verloop", "Verloop van een onbehandelde hiv-infectie (schematisch)", "twee curves over 10 jaar: T-helpercellen dalen traag, virus piekt in het begin en stijgt aan het einde; fasen 1, 2 en 3")
X, Y = assen(HV, 0, 10, 0, 100, "jaren na besmetting", "hoeveelheid (relatief)", 1, 25, links=140, rechts=900)
def tcel(t):
    if t < 0.5:
        return 100 - 50 * t
    if t < 1:
        return 75 + 20 * (t - 0.5)
    if t < 8:
        return 85 - 60 * (t - 1) / 7
    return max(5, 25 - 10 * (t - 8))
def virus(t):
    v = 85 * math.exp(-((t - 0.35) / 0.2) ** 2) + 12 * (1 - math.exp(-t / 0.3))
    if t > 7.5:
        v += 18 * (t - 7.5) ** 2
    return min(v, 95)
HV.pad("M" + " L ".join(f"{X(t / 40):.1f} {Y(tcel(t / 40)):.1f}" for t in range(0, 401)), "none", BLAUW, 4)
HV.pad("M" + " L ".join(f"{X(t / 40):.1f} {Y(virus(t / 40)):.1f}" for t in range(0, 401)), "none", ROOD, 4)
HV.tekst(X(5), Y(tcel(5)) - 34, "T-helpercellen", 16, kleur=BLAUW, vet=True)
HV.tekst(X(4), Y(virus(4)) - 14, "virus", 16, kleur=ROOD, vet=True)
for t in (1, 8):
    HV.lijn(X(t), Y(0), X(t), Y(100), GRIJS, 2, stippel=True)
for nr, t in (("1", 0.5), ("2", 4.5), ("3", 9)):
    HV.letter(X(t), Y(100) + 6, nr)
ZHV = {"1": [Prent.zone(X(0), Y(100), X(1) - X(0), Y(0) - Y(100))],
       "2": [Prent.zone(X(1), Y(100), X(8) - X(1), Y(0) - Y(100))],
       "3": [Prent.zone(X(8), Y(100), X(10) - X(8), Y(0) - Y(100))]}

VRAGEN = [
    klik(
        "Klik op de persoon met bloedgroep O negatief.",
        BG.bestand, ZBG["X"],
        "Geen klonters bij anti-A, anti-B en anti-D.",
    ),
    klik(
        "Klik op de persoon die de universele ontvanger is voor rode bloedcellen.",
        BG.bestand, ZBG["Y"],
        "AB positief: klonters bij anti-A en anti-B.",
    ),
    met_prent(BG.bestand, tabel(
        "Kijk naar de test. Welke bloedgroep heeft elke persoon?",
        [
            ("W", "A positief"),
            ("X", "O negatief"),
            ("Y", "AB positief"),
            ("Z", "B negatief"),
        ],
        "Klonteren bij anti-A betekent A-antigeen, enzovoort.",
        kolommen=["A positief", "O negatief", "AB positief", "B negatief"],
    )),
    met_prent(BG.bestand, tabel(
        "Kijk naar de test. Mag de eerste persoon rode bloedcellen geven aan de tweede?",
        [
            ("X geeft aan W", J),
            ("W geeft aan X", F),
            ("Z geeft aan Y", J),
            ("Y geeft aan Z", F),
        ],
        "De ontvanger mag geen antilichamen hebben tegen de antigenen van de gever.",
    )),
    klik(
        "Klik op de fase waarin er jarenlang weinig klachten zijn.",
        HV.bestand, ZHV["2"],
        "De chronische fase: het virus vermenigvuldigt zich traag verder.",
    ),
    met_prent(HV.bestand, tabel(
        "Kijk naar het verloop van de hiv-infectie. Klopt dit?",
        [
            ("In fase 1 stijgt het virus snel.", J),
            ("De T-helpercellen dalen jarenlang langzaam.", J),
            ("In fase 3 is er aids.", J),
            ("In fase 2 is het virus helemaal verdwenen.", F),
        ],
        "Het virus blijft aanwezig, ook als je niets merkt.",
    )),
    tabel(
        "Welke soort immunisatie is dit?",
        [
            ("je maakt waterpokken door", "natuurlijk actief"),
            ("je krijgt een vaccin tegen mazelen", "kunstmatig actief"),
            ("een baby krijgt antilichamen via de placenta", "natuurlijk passief"),
            ("je krijgt antilichamen na een beet", "kunstmatig passief"),
        ],
        "Actief: zelf aanmaken. Passief: krijgen.",
        kolommen=["natuurlijk actief", "kunstmatig actief", "natuurlijk passief", "kunstmatig passief"],
    ),
    tabel(
        "Actieve of passieve immunisatie?",
        [
            ("werkt meteen", "Passief"),
            ("geeft geheugencellen", "Actief"),
            ("beschermt jaren", "Actief"),
            ("verdwijnt na enkele weken", "Passief"),
        ],
        "Geleende antilichamen worden afgebroken.",
        kolommen=["Actief", "Passief"],
    ),
    casus(
        "Een resusnegatieve vrouw is zwanger van haar tweede kind. Het eerste kind was resuspositief en ze kreeg toen geen inspuiting.",
        [
            keuze(
                "Bij de eerste bevalling kon ze antilichamen tegen het [[*D-antigeen|A-antigeen|B-antigeen]] aanmaken.",
                "Bloed van het kind kwam in haar bloed.",
            ),
            tabel(
                "Klopt dit over het tweede kind?",
                [
                    ("Als het resuspositief is, loopt het gevaar.", J),
                    ("Antilichamen van de moeder kunnen de placenta over.", J),
                    ("Een resusnegatief kind loopt hetzelfde gevaar.", F),
                ],
                "Anti-D valt enkel resuspositieve rode bloedcellen aan.",
            ),
            keuze(
                "Dit wordt voorkomen met een [[*anti-D-inspuiting|vaccin tegen resus|bloedtransfusie met O]] rond de bevalling.",
                "Die ruimt de cellen van het kind op voor de moeder reageert.",
            ),
        ],
    ),
    koppel(
        "Koppel elke ziekte aan wat er misgaat.",
        [
            ("allergie", "overdreven afweer tegen iets onschuldigs"),
            ("auto-immuunziekte", "afweer valt eigen gezonde cellen aan"),
            ("aids", "te weinig T-helpercellen"),
        ],
        ["te veel rode bloedcellen", "bloedgroep die verandert"],
        "Drie manieren waarop de afweer faalt.",
    ),
    mk(
        "Waarom beschermt een hoge vaccinatiegraad ook wie niet gevaccineerd is?",
        [
            "De verwekker vindt amper nieuwe gastheren",
            "Gevaccineerden geven hun antilichamen door bij aanraking",
            "Het vaccin verspreidt zich door de lucht naar anderen",
            "Ongevaccineerden maken dan zelf meer antilichamen aan",
        ],
        0,
        "Dat heet groepsimmuniteit.",
    ),
    tabel(
        "Welke antilichamen zitten in het plasma?",
        [
            ("bloedgroep A", "anti-B"),
            ("bloedgroep B", "anti-A"),
            ("bloedgroep O", "anti-A en anti-B"),
            ("bloedgroep AB", "geen van beide"),
        ],
        "Je maakt antilichamen tegen wat je zelf niet hebt.",
        kolommen=["anti-A", "anti-B", "anti-A en anti-B", "geen van beide"],
    ),
    sleep(
        "Bij een allergie gaan [[IgE]]-antilichamen op de [[mestcellen]] zitten. Bij een nieuw contact zetten die [[histamine]] vrij.",
        ["IgG", "rode bloedcellen", "insuline"],
        "Dat geeft een loopneus, jeuk en zwelling.",
    ),
    tabel(
        "Klopt dit over een incompatibele transfusie?",
        [
            ("De rode bloedcellen klitten samen.", J),
            ("Ze gaan kapot: hemolyse.", J),
            ("Het kan levensgevaarlijk zijn.", J),
            ("Het merk je pas na enkele jaren.", F),
        ],
        "De reactie komt snel.",
    ),
    mk(
        "Waarom mag plasma van groep O niet zomaar aan iedereen gegeven worden?",
        [
            "Het bevat anti-A en anti-B",
            "Het bevat A- en B-antigenen",
            "Het bevat geen eiwitten",
            "Het bevat te veel rode bloedcellen",
        ],
        0,
        "Voor plasma is AB de universele donor.",
    ),
    tabel(
        "Is dit een auto-immuunziekte?",
        [
            ("multiple sclerose", J),
            ("de ziekte van Crohn", J),
            ("psoriasis", J),
            ("griep", F),
        ],
        "Griep is een virusinfectie.",
    ),
    keuze(
        "Hiv is een [[*retrovirus|bacterie|prion]]: het zet zijn RNA om in DNA.",
        "Met het enzym omgekeerd transcriptase.",
    ),
    tabel(
        "Klopt dit over een vaccin?",
        [
            ("Het kan een dode verwekker bevatten.", J),
            ("Het kan een stukje van de verwekker bevatten.", J),
            ("Het laat je zelf geheugencellen maken.", J),
            ("Het bevat altijd volledig besmettelijke verwekkers.", F),
        ],
        "Afgezwakt, dood of een stukje.",
    ),
    mk(
        "Waarom bestaat er nog geen goed vaccin tegen hiv?",
        [
            "Het virus verandert voortdurend zijn oppervlak",
            "Hiv heeft helemaal geen antigenen op zijn oppervlak",
            "Een vaccin mag niet in T-helpercellen komen",
            "Hiv overleeft niet buiten het lichaam",
        ],
        0,
        "Antilichamen passen na een tijd niet meer.",
    ),
    tabel(
        "Klopt dit over een anafylactische shock?",
        [
            ("Het hele lichaam reageert.", J),
            ("De bloeddruk kan sterk dalen.", J),
            ("Een adrenalinepen kan levens redden.", J),
            ("Het blijft beperkt tot de prikplaats.", F),
        ],
        "Snel handelen is nodig.",
    ),
    keuze(
        "Iemand met antilichamen tegen hiv in het bloed noemt men [[*seropositief|resuspositief|allergisch]].",
        "Die antilichamen verschijnen pas enkele weken na de besmetting.",
    ),
    tabel(
        "Klopt dit over borstvoeding?",
        [
            ("De baby krijgt antilichamen van de moeder.", J),
            ("Het is passieve immunisatie.", J),
            ("De baby krijgt er levenslange geheugencellen door.", F),
        ],
        "Geleende antilichamen verdwijnen na een tijd.",
    ),
    inv(
        "In een klas van 25 leerlingen zijn er 23 gevaccineerd. Hoeveel procent is dat?",
        ["92"],
        "23 : 25 = 0,92 = 92 %.",
    ),
    tabel(
        "Waarom sterft iemand met aids meestal aan een andere ziekte?",
        [
            ("De afweer wordt niet meer aangestuurd.", J),
            ("Gewone verwekkers krijgen vrij spel.", J),
            ("Hiv vernietigt zelf het hart.", F),
        ],
        "Opportunistische infecties.",
    ),
    tabel(
        "Klopt dit over de bloedgroep?",
        [
            ("Ze ligt vast in het DNA.", J),
            ("Ze blijft je hele leven dezelfde.", J),
            ("Een beenmergtransplantatie kan ze wel veranderen.", J),
            ("Ze verandert vanzelf in de puberteit.", F),
        ],
        "Het beenmerg maakt de rode bloedcellen.",
    ),
    tabel(
        "Klopt dit over een auto-immuunziekte?",
        [
            ("Ze is meestal chronisch.", J),
            ("Men onderdrukt de afweerreactie.", J),
            ("Ze is besmettelijk.", F),
        ],
        "Het is geen infectie.",
    ),
    tabel(
        "Welke antigenen staan op de rode bloedcellen?",
        [
            ("bloedgroep A", "A"),
            ("bloedgroep AB", "A en B"),
            ("bloedgroep O", "geen"),
        ],
        "O heeft geen A- en geen B-antigeen.",
        kolommen=["A", "A en B", "geen"],
    ),
    open_(
        "Leg uit waarom iemand met bloedgroep A geen bloed van groep B mag krijgen.",
        "Iemand met bloedgroep A heeft anti-B-antilichamen in zijn plasma. Rode bloedcellen van groep B dragen het B-antigeen. De anti-B van de ontvanger klit die cellen samen en ze gaan kapot. Dat is levensgevaarlijk.",
    ),
]
