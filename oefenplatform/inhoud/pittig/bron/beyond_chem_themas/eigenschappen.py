"""Ruimtelijke structuur, polariteit en intermoleculaire krachten — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vier molecuulvormen -------------------------------------------------------
VM = Prent("molecuulvormen", "Vier ruimtelijke structuren rond een centraal atoom", "vier tekeningen met een centraal bolletje en bindingen; letters A tot D")
CX = {"A": 130, "B": 370, "C": 620, "D": 870}


def _bol(p, x, y, r=16, kl="#cfe5f3"):
    p.cirkel(x, y, r, kl, DONKER, 2)


# A: lineair
_bol(VM, CX["A"], 280, 22, "#f7d9b5")
for dx in (-80, 80):
    VM.lijn(CX["A"], 280, CX["A"] + dx, 280, DONKER, 4)
    _bol(VM, CX["A"] + dx, 280)
_bol(VM, CX["A"], 280, 22, "#f7d9b5")
# B: vlakke driehoek
x = CX["B"]
for (dx, dy) in ((0, -90), (-78, 45), (78, 45)):
    VM.lijn(x, 280, x + dx, 280 + dy, DONKER, 4)
    _bol(VM, x + dx, 280 + dy)
_bol(VM, x, 280, 22, "#f7d9b5")
# C: tetraëder (wig en streepjes)
x = CX["C"]
VM.lijn(x, 280, x, 185, DONKER, 4)
_bol(VM, x, 185)
VM.lijn(x, 280, x - 80, 330, DONKER, 4)
_bol(VM, x - 80, 330)
VM.pad(f"M {x} 276 L {x + 85} 318 L {x + 78} 334 Z", DONKER, DONKER, 1)
_bol(VM, x + 85, 330)
VM.lijn(x, 280, x + 5, 370, DONKER, 2, stippel=True)
_bol(VM, x + 5, 375)
_bol(VM, x, 280, 22, "#f7d9b5")
# D: geknikt met twee vrije paren
x = CX["D"]
for dx in (-70, 70):
    VM.lijn(x, 280, x + dx, 340, DONKER, 4)
    _bol(VM, x + dx, 340)
_bol(VM, x, 280, 22, "#f7d9b5")
VM.ellips(x - 28, 235, 14, 22, "#efe6f5", DONKER, 1)
VM.ellips(x + 28, 235, 14, 22, "#efe6f5", DONKER, 1)
VM.tekst(x, 200, "2 vrije paren", 15)
for k, xx in CX.items():
    VM.letter(xx, 470, k)
ZVM = {k: [Prent.zone(xx - 105, 170, 210, 220), Prent.rond(xx, 470, 22)] for k, xx in CX.items()}

# Waterstofbrug tussen twee watermoleculen ---------------------------------
WB = Prent("waterstofbrug-water", "Twee watermoleculen naast elkaar", "twee watermoleculen met O en H; tussen een H van de ene en de O van de andere een stippellijn; letters A tot D")
# molecule 1 links
WB.tekst(250, 330, "O", 38, vet=True, kleur=ROOD)
WB.lijn(230, 335, 170, 410, DONKER, 4)
WB.tekst(155, 440, "H", 32, vet=True)
WB.lijn(275, 320, 410, 320, DONKER, 4)
WB.tekst(430, 332, "H", 32, vet=True)
WB.tekst(250, 280, "δ−", 20, kleur=ROOD)
WB.tekst(430, 290, "δ+", 20, kleur=BLAUW)
# brug
WB.lijn(455, 320, 595, 320, GROEN, 4, stippel=True)
# molecule 2 rechts
WB.tekst(625, 332, "O", 38, vet=True, kleur=ROOD)
WB.lijn(645, 335, 705, 410, DONKER, 4)
WB.tekst(720, 440, "H", 32, vet=True)
WB.lijn(645, 300, 705, 225, DONKER, 4)
WB.tekst(720, 220, "H", 32, vet=True)
WB.cirkel(600, 270, 4, DONKER, DONKER, 1)
WB.cirkel(612, 262, 4, DONKER, DONKER, 1)
LWB = {"A": (340, 230), "B": (525, 230), "C": (560, 420), "D": (110, 330)}
for k, (xx, yy) in LWB.items():
    WB.letter(xx, yy, k)
WB.lijn(340, 252, 340, 315, GRIJS, 1)
WB.lijn(525, 252, 525, 315, GRIJS, 1)
WB.lijn(575, 400, 670, 370, GRIJS, 1)
WB.lijn(130, 340, 195, 375, GRIJS, 1)
ZWB = {"A": [Prent.zone(280, 305, 125, 30), Prent.rond(*LWB["A"], 22)],
       "B": [Prent.zone(460, 300, 130, 40), Prent.rond(*LWB["B"], 22)],
       "C": [Prent.zone(645, 340, 60, 70), Prent.rond(*LWB["C"], 22)],
       "D": [Prent.zone(165, 340, 70, 70), Prent.rond(*LWB["D"], 22)]}

VRAGEN = [
    klik(
        "Klik op de structuur van een atoom met sp²-hybridisatie.",
        VM.bestand, ZVM["B"],
        "Sterisch getal drie: vlakke driehoek, sp², hoek 120°.",
    ),
    klik(
        "Klik op de structuur waarvan de werkelijke hoek het verst onder de theoretische ligt.",
        VM.bestand, ZVM["D"],
        "Twee vrije paren duwen de bindingen het sterkst samen.",
    ),
    met_prent(VM.bestand, tabel(
        "Welke theoretische hoek hoort bij deze structuur, als je de vrije paren meetelt?",
        [
            ("A", "180°"),
            ("B", "120°"),
            ("C", "109,5°"),
            ("D", "109,5°"),
        ],
        "D heeft sterisch getal vier: theoretisch 109,5°, in werkelijkheid kleiner.",
        kolommen=["180°", "120°", "109,5°"],
    )),
    met_prent(VM.bestand, tabel(
        "Welke letter past bij deze molecule?",
        [
            ("CO₂", "A"),
            ("CH₄", "C"),
            ("H₂O", "D"),
            ("BF₃", "B"),
        ],
        "Boor heeft drie bindingen en geen vrij paar: vlakke driehoek.",
        kolommen=["A", "B", "C", "D"],
    )),
    klik(
        "Klik op de kracht die het kookpunt van water zo hoog maakt.",
        WB.bestand, ZWB["B"],
        "De waterstofbrug tussen moleculen moet je breken om water te laten koken.",
    ),
    met_prent(WB.bestand, tabel(
        "Is dit deel een binding binnen een molecule of een kracht tussen moleculen?",
        [
            ("A", "Binnen"),
            ("B", "Tussen"),
            ("C", "Binnen"),
            ("D", "Binnen"),
        ],
        "Alleen de stippellijn verbindt twee verschillende moleculen.",
        kolommen=["Binnen", "Tussen"],
    )),
    tabel(
        "Welk sterisch getal heeft het centrale atoom?",
        [
            ("C in CH₄", "4"),
            ("N in NH₃", "4"),
            ("C in CO₂", "2"),
            ("C in methanal, H₂C=O", "3"),
        ],
        "Tel bindingspartners en vrije paren. Een dubbele binding telt als één partner.",
        kolommen=["2", "3", "4"],
    ),
    tabel(
        "Welk hybridisatietype heeft dit koolstofatoom?",
        [
            ("in ethaan", "sp³"),
            ("in etheen", "sp²"),
            ("in ethyn", "sp"),
            ("in CO₂", "sp"),
        ],
        "Sterisch getal 4, 3 of 2 geeft sp³, sp² of sp.",
        kolommen=["sp", "sp²", "sp³"],
    ),
    tabel(
        "Is deze molecule polair?",
        [
            ("H₂O", "Polair"),
            ("CO₂", "Apolair"),
            ("CCl₄", "Apolair"),
            ("NH₃", "Polair"),
        ],
        "Bij CO₂ en CCl₄ heffen de bindingsdipolen elkaar op door de symmetrische vorm.",
        kolommen=["Polair", "Apolair"],
    ),
    volgorde(
        "Zet deze krachten van zwak naar sterk.",
        ["londonkracht", "dipoolkracht", "waterstofbrug", "ion-dipoolkracht"],
        "De londonkracht werkt altijd, maar is per contactpunt het zwakst.",
    ),
    volgorde(
        "Zet deze alkanen van laag naar hoog kookpunt.",
        ["methaan", "propaan", "pentaan", "octaan"],
        "Een langere keten geeft meer contact en dus sterkere londonkrachten.",
    ),
    mk(
        "Waarom kookt 2,2-dimethylpropaan lager dan pentaan, met dezelfde formule C₅H₁₂?",
        [
            "Het is bolvormiger: minder contactoppervlak",
            "Het vormt een waterstofbrug minder dan pentaan",
            "Het heeft meer koolstofatomen dan pentaan",
            "Het is polair, terwijl pentaan apolair is",
        ],
        0,
        "Vertakking maakt een molecule compacter: zwakkere londonkrachten.",
    ),
    casus(
        "In een proef meng je telkens twee stoffen: water, ethanol, hexaan en keukenzout.",
        [
            tabel(
                "Mengen deze stoffen goed of lost het op?",
                [
                    ("water en ethanol", "Ja"),
                    ("water en hexaan", "Nee"),
                    ("keukenzout in water", "Ja"),
                    ("keukenzout in hexaan", "Nee"),
                ],
                "Gelijk lost op in gelijk: polair bij polair, apolair bij apolair.",
                kolommen=["Ja", "Nee"],
            ),
            mk(
                "Welke kracht laat ethanol met water mengen?",
                [
                    "Waterstofbruggen via de OH-groep",
                    "Londonkrachten van de keten",
                    "Ion-dipoolkrachten met de ionen",
                    "Metaalbindingen tussen de moleculen",
                ],
                0,
                "De OH-groep van ethanol vormt waterstofbruggen met water.",
            ),
            keuze(
                "Hexaan blijft als een aparte laag op het water drijven omdat het [[*apolair|polair|ionisch]] is.",
                "Water houdt zijn eigen moleculen vast met waterstofbruggen en laat hexaan niet tussen.",
            ),
        ],
    ),
    tabel(
        "Welk rooster heeft deze stof in vaste vorm?",
        [
            ("diamant", "Atoomrooster"),
            ("ijzer", "Metaalrooster"),
            ("suiker", "Molecuulrooster"),
            ("keukenzout", "Ionrooster"),
        ],
        "Atoomrooster: overal atoombindingen. Molecuulrooster: losse moleculen die elkaar aantrekken.",
        kolommen=["Atoomrooster", "Ionrooster", "Metaalrooster", "Molecuulrooster"],
    ),
    tabel(
        "Geleidt deze stof elektrische stroom?",
        [
            ("vast koper", "Ja"),
            ("vast keukenzout", "Nee"),
            ("gesmolten keukenzout", "Ja"),
            ("vaste suiker", "Nee"),
        ],
        "Er moeten vrij bewegende ladingen zijn: elektronen of losse ionen.",
        kolommen=["Ja", "Nee"],
    ),
    inv(
        "Hoeveel bindingspartners heeft een centraal atoom met sterisch getal 3 en één vrij elektronenpaar?",
        ["2", "twee"],
        "3 − 1 = 2. Zo'n molecule is vlak en geknikt, zoals zwaveldioxide.",
    ),
    mk(
        "Waarom is de hoek in water (104,5°) kleiner dan in ammoniak (107°)?",
        [
            "Water heeft twee vrije paren, ammoniak maar één",
            "Water heeft een kleiner sterisch getal dan ammoniak",
            "Zuurstof heeft minder valentie-elektronen dan stikstof",
            "In water liggen de bindingen in één lijn",
        ],
        0,
        "Elk vrij paar duwt de bindingen iets dichter bij elkaar.",
    ),
    tabel(
        "Kan deze stof waterstofbruggen vormen met zichzelf?",
        [
            ("water", "Ja"),
            ("ammoniak", "Ja"),
            ("methaan", "Nee"),
            ("waterstoffluoride", "Ja"),
        ],
        "Waterstof moet aan N, O of F gebonden zijn.",
        kolommen=["Ja", "Nee"],
    ),
    sleep(
        "Een binding is polair als de twee atomen een verschillende [[elektronegatieve waarde]] hebben. De molecule als geheel is polair als de dipolen elkaar [[niet opheffen]]. Dat hangt af van de [[ruimtelijke structuur]].",
        ["atoommassa", "wel opheffen", "kleur"],
        "Polaire bindingen geven pas een polaire molecule als de vorm niet symmetrisch is.",
    ),
    mk(
        "Hoe zorgt water ervoor dat een Na⁺-ion in oplossing blijft?",
        [
            "De δ−-kant van zuurstof richt zich naar het ion",
            "De δ+-kant van waterstof richt zich naar het ion",
            "Water vormt een atoombinding met natrium",
            "Water geeft een elektron aan het natriumion",
        ],
        0,
        "Een positief ion wordt omringd door de negatieve kant van de watermoleculen.",
    ),
    tabel(
        "Klopt dit over smeltpunten?",
        [
            ("Diamant smelt bij een hogere temperatuur dan ijs.", J),
            ("Bij smelten van ijs breken de O–H-bindingen in de moleculen.", F),
            ("Keukenzout smelt bij een hogere temperatuur dan suiker.", J),
        ],
        "Bij smelten van een molecuulrooster breek je alleen krachten tussen de moleculen.",
    ),
    koppel(
        "Koppel elk molecule aan zijn ruimtelijke structuur.",
        [
            ("CH₄", "tetraëder"),
            ("NH₃", "piramide"),
            ("H₂O", "geknikt"),
            ("CO₂", "lineair"),
        ],
        ["vlakke vierhoek"],
        "Tel per centraal atoom de bindingspartners en de vrije paren.",
    ),
    inv(
        "Welke theoretische bindingshoek hoort bij sp-hybridisatie? Geef het getal in graden.",
        ["180", "180°", "180 graden"],
        "Twee richtingen die zo ver mogelijk uit elkaar liggen: een rechte lijn.",
    ),
    sorteer(
        "Is dit een kracht binnen een deeltje of een kracht tussen deeltjes?",
        ["Intramoleculair", "Intermoleculair"],
        [
            ("de O–H-binding in water", "Intramoleculair"),
            ("de C=C-binding in etheen", "Intramoleculair"),
            ("de waterstofbrug tussen twee watermoleculen", "Intermoleculair"),
            ("de londonkracht tussen twee hexaanmoleculen", "Intermoleculair"),
            ("de ion-dipoolkracht rond Na⁺ in water", "Intermoleculair"),
        ],
        "Bindingen zitten in de molecule. Krachten tussen moleculen bepalen kook- en smeltpunt.",
    ),
    mk(
        "Tetrachloormethaan, CCl₄, heeft vier polaire bindingen. Waarom is de molecule toch apolair?",
        [
            "De vier dipolen heffen elkaar symmetrisch op",
            "Chloor en koolstof zijn precies even elektronegatief",
            "Het centrale atoom heeft twee vrije elektronenparen",
            "De molecule is lineair net zoals koolstofdioxide",
        ],
        0,
        "Bij een tetraëder met vier gelijke partners valt het dipoolmoment weg.",
    ),
    inv(
        "Welk sterisch getal heeft het zuurstofatoom in dimethylether, CH₃–O–CH₃?",
        ["4", "vier"],
        "Twee bindingspartners en twee vrije paren: geknikt, net als water.",
    ),
    tabel(
        "Klopt dit over de roosters?",
        [
            ("Een metaalrooster geleidt ook in vaste toestand.", J),
            ("Een ionrooster is hard maar bros.", J),
            ("Een molecuulrooster heeft meestal een laag smeltpunt.", J),
            ("In een atoomrooster zitten losse moleculen.", F),
        ],
        "In een atoomrooster is het hele kristal één netwerk van atoombindingen.",
    ),
    open_(
        "Leg uit waarom water bij 100 °C kookt, terwijl methaan, met een vergelijkbare massa, al bij −161 °C kookt.",
        "Water is polair en vormt waterstofbruggen, omdat waterstof aan het sterk elektronegatieve zuurstof hangt. Die waterstofbruggen zijn veel sterker dan de londonkrachten die tussen de apolaire methaanmoleculen werken. Om water te laten koken moet je die sterke krachten breken, en daar is veel meer energie, dus een hogere temperatuur, voor nodig.",
    ),
]
