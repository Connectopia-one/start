"""Organische stoffen: stofklassen en naamgeving — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vijf skeletnotaties ------------------------------------------------------
SN = Prent("skeletnotaties", "Vijf moleculen in skeletnotatie", "vijf zigzaglijnen met functionele groepen, letters P tot T")


def _zigzag(p, x, y, n, dx=50, dy=28):
    pts = [(x + i * dx, y + (0 if i % 2 == 0 else -dy)) for i in range(n)]
    p.pad("M" + " L".join(f"{a} {b}" for a, b in pts), "none", DONKER, 3)
    return pts


# P: ethanol (C-C-OH)
pts = _zigzag(SN, 70, 180, 2)
SN.lijn(pts[-1][0], pts[-1][1], pts[-1][0] + 45, pts[-1][1] + 26, DONKER, 3)
SN.tekst(pts[-1][0] + 70, pts[-1][1] + 36, "OH", 20, vet=True, kleur=ROOD)
# Q: propanon (C-C(=O)-C)
pts = _zigzag(SN, 330, 180, 3, dy=-28)
SN.lijn(pts[1][0] - 4, pts[1][1], pts[1][0] - 4, pts[1][1] - 50, DONKER, 3)
SN.lijn(pts[1][0] + 4, pts[1][1], pts[1][0] + 4, pts[1][1] - 50, DONKER, 3)
SN.tekst(pts[1][0], pts[1][1] - 60, "O", 20, vet=True, kleur=ROOD)
# R: propanal (C-C-CHO)
pts = _zigzag(SN, 640, 180, 3)
xe, ye = pts[-1]
SN.lijn(xe, ye, xe + 45, ye - 26, DONKER, 3)
SN.lijn(xe + 3, ye + 7, xe + 48, ye - 19, DONKER, 3)
SN.tekst(xe + 62, ye - 30, "O", 20, vet=True, kleur=ROOD)
# S: ethaanzuur
pts = _zigzag(SN, 180, 430, 2)
SN.lijn(pts[-1][0] - 4, pts[-1][1], pts[-1][0] - 4, pts[-1][1] - 50, DONKER, 3)
SN.lijn(pts[-1][0] + 4, pts[-1][1], pts[-1][0] + 4, pts[-1][1] - 50, DONKER, 3)
SN.tekst(pts[-1][0], pts[-1][1] - 60, "O", 20, vet=True, kleur=ROOD)
SN.lijn(pts[-1][0], pts[-1][1], pts[-1][0] + 45, pts[-1][1] + 26, DONKER, 3)
SN.tekst(pts[-1][0] + 70, pts[-1][1] + 36, "OH", 20, vet=True, kleur=ROOD)
# T: methoxymethaan (ether)
SN.lijn(560, 430, 605, 404, DONKER, 3)
SN.tekst(620, 412, "O", 20, vet=True, kleur=ROOD)
SN.lijn(635, 404, 680, 430, DONKER, 3)
LSN = {"P": (110, 270), "Q": (380, 270), "R": (700, 270), "S": (220, 540), "T": (620, 540)}
for k, (x, y) in LSN.items():
    SN.letter(x, y, k)
ZSN = {"P": [Prent.zone(50, 110, 200, 130), Prent.rond(*LSN["P"], 22)],
       "Q": [Prent.zone(310, 90, 150, 150), Prent.rond(*LSN["Q"], 22)],
       "R": [Prent.zone(600, 70, 260, 170), Prent.rond(*LSN["R"], 22)],
       "S": [Prent.zone(160, 350, 200, 150), Prent.rond(*LSN["S"], 22)],
       "T": [Prent.zone(540, 380, 160, 70), Prent.rond(*LSN["T"], 22)]}

# Structuurformule pentaan-2-ol -------------------------------------------
PO = Prent("structuur-pentanol", "Beknopte structuurformule van een alcohol", "vijf koolstofatomen op een rij, met een OH-groep aan het tweede; letters A tot E bij de koolstofatomen")
XS = [140, 320, 500, 680, 860]
LAB = ["CH₃", "CH", "CH₂", "CH₂", "CH₃"]
for i, x in enumerate(XS):
    PO.rect(x - 50, 290, 100, 60, "#fbf6ea", DONKER, 10, 2)
    PO.tekst(x, 330, LAB[i], 24, vet=True)
    if i < 4:
        PO.lijn(x + 50, 320, XS[i + 1] - 50, 320, DONKER, 3)
    PO.letter(x, 420, "ABCDE"[i])
PO.lijn(320, 290, 320, 220, DONKER, 3)
PO.tekst(320, 205, "OH", 24, vet=True, kleur=ROOD)
ZPO = {k: [Prent.zone(XS[i] - 50, 290, 100, 60), Prent.rond(XS[i], 420, 22)] for i, k in enumerate("ABCDE")}

VRAGEN = [
    klik(
        "Klik op het keton.",
        SN.bestand, ZSN["Q"],
        "Bij een keton zit de C=O tussen twee koolstofatomen.",
    ),
    klik(
        "Klik op het aldehyde.",
        SN.bestand, ZSN["R"],
        "Bij een aldehyde zit de C=O aan het uiteinde van de keten.",
    ),
    met_prent(SN.bestand, tabel(
        "Welke naam hoort bij de molecule?",
        [
            ("P", "ethanol"),
            ("Q", "propanon"),
            ("S", "ethaanzuur"),
            ("T", "methoxymethaan"),
        ],
        "Tel elke hoek en elk uiteinde als een koolstofatoom.",
        kolommen=["ethanol", "propanon", "ethaanzuur", "methoxymethaan"],
    )),
    met_prent(SN.bestand, tabel(
        "Kijk naar de skeletnotaties. Klopt dit?",
        [
            ("Q en R hebben dezelfde brutoformule.", J),
            ("S is azijnzuur.", J),
            ("T is een ether.", J),
            ("P heeft drie koolstofatomen.", F),
        ],
        "Propanon en propanal: allebei C₃H₆O, maar een andere functionele groep.",
    )),
    klik(
        "Je nummert de hoofdketen volgens de IUPAC-regels. Klik op koolstofatoom nummer 4.",
        PO.bestand, ZPO["D"],
        "Je begint links, zodat de OH-groep nummer 2 krijgt. Dan is D nummer 4.",
    ),
    met_prent(PO.bestand, tabel(
        "Kijk naar de alcohol. Klopt dit?",
        [
            ("De naam is pentaan-2-ol.", J),
            ("Het is een secundaire alcohol.", J),
            ("De hoofdketen heeft vijf koolstofatomen.", J),
            ("De naam is pentaan-4-ol.", F),
        ],
        "Je nummert vanaf de kant die de OH-groep het laagste nummer geeft.",
    )),
    tabel(
        "Tot welke stofklasse hoort deze stof?",
        [
            ("CH₃-CH₂-OH", "Alcohol"),
            ("CH₃-COOH", "Carbonzuur"),
            ("CH₃-COO-CH₃", "Ester"),
            ("CH₃-NH₂", "Amine"),
            ("CH₃-CH₂-Cl", "Halogeenalkaan"),
        ],
        "Kijk naar de functionele groep.",
        kolommen=["Alcohol", "Carbonzuur", "Ester", "Amine", "Halogeenalkaan"],
    ),
    inv(
        "Hoeveel waterstofatomen heeft een alkaan met 7 koolstofatomen?",
        ["16"],
        "CnH2n+2: 2 x 7 + 2 = 16.",
    ),
    inv(
        "Hoeveel waterstofatomen heeft een alkeen met 5 koolstofatomen en één dubbele binding?",
        ["10"],
        "Een alkeen met één dubbele binding heeft er twee minder dan het alkaan: 12 − 2 = 10.",
    ),
    koppel(
        "Koppel elke uitgang aan haar stofklasse.",
        [
            ("-ol", "alcohol"),
            ("-al", "aldehyde"),
            ("-on", "keton"),
            ("-zuur", "carbonzuur"),
            ("-oaat", "ester"),
        ],
        ["alkyn"],
        "Een alkyn eindigt op -yn.",
    ),
    keuze(
        "CH₃-CH₂-CH₂-CHO heet [[*butanal|butanon|butaanzuur]].",
        "Vier koolstofatomen met een CHO-groep aan het uiteinde.",
    ),
    keuze(
        "Een ester van methanol en propaanzuur heet [[*methylpropanoaat|propylmethanoaat|methylpropanol]].",
        "De alcoholkant staat vooraan, de zuurkant achteraan.",
    ),
    tabel(
        "Primair, secundair of tertiair alcohol?",
        [
            ("propaan-1-ol", "Primair"),
            ("propaan-2-ol", "Secundair"),
            ("2-methylpropaan-2-ol", "Tertiair"),
            ("ethanol", "Primair"),
        ],
        "Tel hoeveel koolstofatomen er aan het C-atoom met de OH-groep zitten.",
        kolommen=["Primair", "Secundair", "Tertiair"],
    ),
    mk(
        "Waarom heet het but-1-een en niet but-3-een?",
        [
            "Je nummert vanaf de kant met het laagste nummer",
            "De dubbele binding staat altijd aan het begin",
            "Het cijfer zegt hoeveel dubbele bindingen er zijn",
            "But-3-een is een andere stof met vijf atomen",
        ],
        0,
        "Van de andere kant geteld begint de dubbele binding bij het eerste koolstofatoom.",
    ),
    tabel(
        "Verzadigd of onverzadigd?",
        [
            ("propaan", "Verzadigd"),
            ("propeen", "Onverzadigd"),
            ("ethyn", "Onverzadigd"),
            ("cyclohexaan", "Verzadigd"),
        ],
        "Verzadigd: enkel enkelvoudige bindingen tussen de koolstofatomen.",
        kolommen=["Verzadigd", "Onverzadigd"],
    ),
    casus(
        "In de keukenkast staan azijn, spiritus, nagellakremover en een flesje glycerol uit de apotheek.",
        [
            tabel(
                "Welke stof zit er vooral in?",
                [
                    ("azijn", "ethaanzuur"),
                    ("nagellakremover", "propanon"),
                    ("glycerol", "propaantriol"),
                ],
                "Aceton is propanon.",
                kolommen=["ethaanzuur", "propanon", "propaantriol"],
            ),
            inv(
                "Hoeveel OH-groepen telt één molecule uit het flesje uit de apotheek?",
                ["3", "drie"],
                "Propaantriol: tri is drie.",
            ),
            keuze(
                "Azijnzuur heeft [[*twee|één|drie]] koolstofatomen.",
                "Ethaan: twee koolstofatomen. Mierenzuur heeft er één.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over voorstellingen van een molecule?",
        [
            ("In een skeletnotatie is elke hoek een koolstofatoom.", J),
            ("Een bolstaafmodel toont ook de hoeken tussen de bindingen.", J),
            ("Een beknopte structuurformule neemt de H-atomen per koolstof samen.", J),
            ("Een brutoformule toont hoe de atomen gebonden zijn.", F),
        ],
        "De brutoformule zegt alleen hoeveel atomen van elk element.",
    ),
    mk(
        "Waarom is cyclohexaan niet aromatisch, terwijl benzeen het wel is?",
        [
            "Geen elektronen verspreid over de ring",
            "Het heeft geen zes koolstofatomen in de ring",
            "Het is helemaal geen cyclische stof",
            "Het bevat een zuurstofatoom in de ring",
        ],
        0,
        "Cyclohexaan heeft enkel enkelvoudige bindingen.",
    ),
    tabel(
        "Welke IUPAC-naam hoort bij deze gebruiksnaam?",
        [
            ("drankalcohol", "ethanol"),
            ("chloroform", "trichloormethaan"),
            ("mierenzuur", "methaanzuur"),
            ("aceton", "propanon"),
        ],
        "In chloroform zijn drie H-atomen van methaan vervangen door chloor.",
        kolommen=["ethanol", "trichloormethaan", "methaanzuur", "propanon"],
    ),
    sleep(
        "Een amide ontstaat als je de [[OH]] van een carbonzuur vervangt door [[NH₂]]. Een amide heeft dus zowel de [[C=O]] als een stikstofatoom.",
        ["CH₃", "Cl", "C≡C"],
        "Een amine heeft wel een stikstof, maar geen C=O.",
    ),
    tabel(
        "Klopt deze naam bij de formule?",
        [
            ("CH₃-CH₂-COOH: propaanzuur", J),
            ("CH₃-CO-CH₃: propanal", F),
            ("CH₃-O-CH₃: methoxymethaan", J),
            ("HO-CH₂-CH₂-OH: ethaandiol", J),
        ],
        "CH₃-CO-CH₃ is propanon: de C=O zit in het midden.",
    ),
    mk(
        "Twee stoffen hebben dezelfde brutoformule C₂H₆O. Hoe kan dat?",
        [
            "Een alcohol en een ether met een andere bouw",
            "Ze zijn allebei ethanol in een ander vat",
            "Een brutoformule kan nooit bij twee stoffen horen",
            "Het ene is een alkaan, het andere een alkeen",
        ],
        0,
        "Ethanol en methoxymethaan: dezelfde atomen, anders gebonden.",
    ),
    tabel(
        "Klopt dit over 2-methylbutaan?",
        [
            ("Het is een alkaan.", J),
            ("De hoofdketen heeft vier koolstofatomen.", J),
            ("Het heeft vijf koolstofatomen in totaal.", J),
            ("Het is onvertakt.", F),
        ],
        "De methylgroep op het tweede koolstofatoom is een vertakking.",
    ),
    inv(
        "Hoeveel koolstofatomen heeft hexaan?",
        ["6", "zes"],
        "Meth 1, eth 2, prop 3, but 4, pent 5, hex 6.",
    ),
    tabel(
        "Klopt dit over amines?",
        [
            ("CH₃-NH₂ is een primair amine.", J),
            ("Bij een amine tel je de ketens aan de stikstof.", J),
            ("Een tertiair amine heeft drie koolstofketens aan de stikstof.", J),
            ("Een primair amine heeft drie koolstofketens aan de stikstof.", F),
        ],
        "Eén keten: primair. Twee: secundair. Drie: tertiair.",
    ),
    keuze(
        "Een stof met een zuurstofatoom tussen twee koolstofketens, zonder dubbele binding, is een [[*ether|ester|aldehyde]].",
        "Bij een ester zit er ook nog een C=O naast.",
    ),
    tabel(
        "Klopt dit over de naam ethaandiol?",
        [
            ("Er zitten twee OH-groepen in.", J),
            ("De hoofdketen heeft twee koolstofatomen.", J),
            ("Het is een tweewaardige alcohol.", J),
            ("Het is een carbonzuur.", F),
        ],
        "Di staat voor het aantal OH-groepen.",
    ),
    open_(
        "Leg uit waarom propanon en propanal twee verschillende stoffen zijn, al hebben ze dezelfde brutoformule.",
        "Beide hebben drie koolstofatomen, zes waterstofatomen en één zuurstofatoom: C₃H₆O. Bij propanal zit de C=O-groep aan het uiteinde van de keten (aldehyde), bij propanon in het midden (keton). Een andere bouw geeft een andere functionele groep en dus andere eigenschappen.",
    ),
]
