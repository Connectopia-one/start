"""Organische reacties: additie, eliminatie en condensatie — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Propeen voor Markownikov ---------------------------------------------------
PP = Prent("propeen-markownikov", "Structuurformule van propeen", "drie koolstofgroepen op een rij: CH₂, CH en CH₃, met een dubbele binding tussen de eerste twee; letters A, B en C")
XS = [230, 500, 770]
LAB = ["CH₂", "CH", "CH₃"]
for i, x in enumerate(XS):
    PP.rect(x - 60, 280, 120, 70, "#fbf6ea", DONKER, 12, 2)
    PP.tekst(x, 326, LAB[i], 28, vet=True)
    PP.letter(x, 430, "ABC"[i])
PP.lijn(290, 305, 440, 305, DONKER, 3)
PP.lijn(290, 325, 440, 325, DONKER, 3)
PP.lijn(560, 315, 710, 315, DONKER, 3)
PP.tekst(500, 200, "+ H–Br", 28, vet=True, kleur=ROOD)
ZPP = {k: [Prent.zone(XS[i] - 60, 280, 120, 70), Prent.rond(XS[i], 430, 22)] for i, k in enumerate("ABC")}

# Drie alcoholen -------------------------------------------------------------
AL = Prent("drie-alcoholen", "Drie alcoholen met vier koolstofatomen", "drie structuurformules: butaan-1-ol, butaan-2-ol en 2-methylpropaan-2-ol; letters P, Q en R")


def _groep(p, x, y, t, kl="#fbf6ea"):
    p.rect(x - 42, y - 26, 84, 52, kl, DONKER, 10, 2)
    p.tekst(x, y + 9, t, 20, vet=True)


# P: CH3-CH2-CH2-CH2-OH (verticaal)
for j, t in enumerate(["CH₃", "CH₂", "CH₂", "CH₂"]):
    _groep(AL, 170, 120 + j * 90, t)
    if j:
        AL.lijn(170, 94 + j * 90 - 38, 170, 94 + j * 90, DONKER, 3)
AL.lijn(212, 390, 250, 390, DONKER, 3)
_groep(AL, 292, 390, "OH", "#f3c6d0")
# Q: CH3-CH(OH)-CH2-CH3
for j, t in enumerate(["CH₃", "CH", "CH₂", "CH₃"]):
    _groep(AL, 500, 120 + j * 90, t)
    if j:
        AL.lijn(500, 94 + j * 90 - 38, 500, 94 + j * 90, DONKER, 3)
AL.lijn(542, 210, 580, 210, DONKER, 3)
_groep(AL, 622, 210, "OH", "#f3c6d0")
# R: (CH3)3C-OH
_groep(AL, 830, 250, "C")
for (x, y) in ((830, 130), (720, 250), (830, 370)):
    _groep(AL, x, y, "CH₃")
AL.lijn(830, 156, 830, 224, DONKER, 3)
AL.lijn(762, 250, 788, 250, DONKER, 3)
AL.lijn(830, 276, 830, 344, DONKER, 3)
AL.lijn(872, 250, 898, 250, DONKER, 3)
_groep(AL, 940, 250, "OH", "#f3c6d0")
for k, x in zip("PQR", (210, 540, 840)):
    AL.letter(x, 540, k)
ZAL = {"P": [Prent.zone(120, 90, 220, 330), Prent.rond(210, 540, 22)],
       "Q": [Prent.zone(450, 90, 220, 330), Prent.rond(540, 540, 22)],
       "R": [Prent.zone(670, 100, 320, 300), Prent.rond(840, 540, 22)]}

VRAGEN = [
    klik(
        "Klik op het koolstofatoom waar het H-atoom van HBr volgens Markownikov naartoe gaat.",
        PP.bestand, ZPP["A"],
        "Naar het koolstofatoom van de dubbele binding met de meeste waterstofatomen: CH₂.",
    ),
    met_prent(PP.bestand, keuze(
        "Het broomatoom komt op koolstofatoom [[*B|A|C]] en het hoofdproduct is [[*2-broompropaan|1-broompropaan]].",
        "Volgens Markownikov gaat Br naar het koolstofatoom met het minste waterstof.",
    )),
    met_prent(PP.bestand, tabel(
        "Wat ontstaat er als je deze stof laat adderen aan propeen?",
        [
            ("H₂", "Propaan"),
            ("Br₂", "1,2-dibroompropaan"),
            ("H₂O met een zuur", "Propaan-2-ol"),
        ],
        "Bij H₂O gaat de OH-groep volgens Markownikov naar het middelste koolstofatoom.",
        kolommen=["Propaan", "1,2-dibroompropaan", "Propaan-2-ol"],
    )),
    klik(
        "Klik op de alcohol die geen dehydrogenatie kan ondergaan.",
        AL.bestand, ZAL["R"],
        "Het koolstofatoom met de OH-groep draagt geen waterstofatoom meer: een tertiaire alcohol.",
    ),
    klik(
        "Klik op de alcohol die bij dehydrogenatie een aldehyde geeft.",
        AL.bestand, ZAL["P"],
        "Een primaire alcohol: de OH-groep zit aan het uiteinde.",
    ),
    met_prent(AL.bestand, tabel(
        "Is deze alcohol primair, secundair of tertiair?",
        [
            ("P", "Primair"),
            ("Q", "Secundair"),
            ("R", "Tertiair"),
        ],
        "Tel de koolstofatomen die aan het C-atoom met de OH-groep hangen: 1, 2 of 3.",
        kolommen=["Primair", "Secundair", "Tertiair"],
    )),
    met_prent(AL.bestand, mk(
        "Wat ontstaat er bij de dehydrogenatie van alcohol Q?",
        ["Butanon", "Butanal", "But-2-een", "Butaanzuur"],
        0,
        "Een secundaire alcohol wordt een keton.",
    )),
    met_prent(AL.bestand, inv(
        "Hoeveel verschillende alkenen kan alcohol Q geven bij dehydratatie, als je cis en trans niet apart telt?",
        ["2", "twee"],
        "Het water kan aan twee kanten weggaan: but-1-een of but-2-een.",
    )),
    tabel(
        "Welk reactietype is dit?",
        [
            ("ethanol → etheen + water", "Eliminatie"),
            ("etheen + water → ethanol", "Additie"),
            ("ethanol → ethanal + H₂", "Eliminatie"),
            ("propanon + H₂ → propaan-2-ol", "Additie"),
        ],
        "Dehydratatie en dehydrogenatie zijn eliminaties.",
        kolommen=["Additie", "Eliminatie"],
    ),
    tabel(
        "Hoeveel mol H₂ kan er maximaal adderen aan 1 mol van deze stof?",
        [
            ("etheen", "1"),
            ("ethyn", "2"),
            ("buta-1,3-dieen", "2"),
            ("ethaan", "0"),
        ],
        "Per pi-binding één H₂.",
        kolommen=["0", "1", "2"],
    ),
    casus(
        "Je voegt broomwater toe aan drie stoffen: hexaan, hex-1-een en cyclohexeen.",
        [
            tabel(
                "Ontkleurt het broomwater meteen?",
                [
                    ("hexaan", "Nee"),
                    ("hex-1-een", "Ja"),
                    ("cyclohexeen", "Ja"),
                ],
                "Alleen een dubbele binding laat broom meteen adderen.",
                kolommen=["Ja", "Nee"],
            ),
            mk(
                "Wat ontstaat er bij cyclohexeen?",
                ["1,2-dibroomcyclohexaan", "Broombenzeen en waterstofbromide", "Cyclohexanol en HBr", "Hexaan en broom"],
                0,
                "De ring blijft, de dubbele binding gaat open en twee Br-atomen komen erbij.",
            ),
            keuze(
                "Dit is een [[*elektrofiele additie|nucleofiele additie|radicalaire substitutie]].",
                "De pi-elektronen trekken het broom aan.",
            ),
        ],
    ),
    mk(
        "Waarom verloopt de additie aan een aldehyde nucleofiel?",
        [
            "Het C-atoom van C=O is licht positief",
            "Het O-atoom van C=O is licht positief",
            "Een aldehyde heeft geen pi-binding",
            "Een aldehyde is een radicaal",
        ],
        0,
        "Zuurstof trekt de elektronen naar zich toe; het koolstofatoom trekt een nucleofiel aan.",
    ),
    tabel(
        "Wat ontstaat er bij de additie van H₂ aan deze stof?",
        [
            ("propanal", "Primaire alcohol"),
            ("propanon", "Secundaire alcohol"),
            ("propeen", "Alkaan"),
        ],
        "Een aldehyde geeft een primaire, een keton een secundaire alcohol.",
        kolommen=["Primaire alcohol", "Secundaire alcohol", "Alkaan"],
    ),
    volgorde(
        "Zet de oxidatieproducten van propaan-1-ol in volgorde.",
        ["propaan-1-ol", "propanal", "propaanzuur"],
        "Een primaire alcohol wordt eerst een aldehyde, dan een carbonzuur.",
    ),
    mk(
        "Wat ontstaat er bij de eliminatie van HBr uit 2-broompropaan met een base?",
        ["Propeen", "Propaan", "Propaan-2-ol", "Propyn"],
        0,
        "Br en een H van het buuratoom gaan weg: een dubbele binding.",
    ),
    sleep(
        "Bij de [[dehydratatie]] gaat er water uit een alcohol en ontstaat er een [[alkeen]]. Men gebruikt daarvoor geconcentreerd [[zwavelzuur]] en warmte.",
        ["hydrogenering", "aldehyde", "zoutzuur"],
        "Het zwavelzuur trekt het water weg.",
    ),
    tabel(
        "Klopt dit over de verzadigingsgraad?",
        [
            ("Een ring telt mee als één onverzadiging.", J),
            ("Een drievoudige binding telt voor twee.", J),
            ("Een alkaan heeft verzadigingsgraad 1.", F),
        ],
        "Een alkaan is verzadigd: verzadigingsgraad 0.",
    ),
    koppel(
        "Koppel elke reactie aan haar naam.",
        [
            ("H₂ adderen aan een alkeen", "hydrogenering"),
            ("water afsplitsen uit een alcohol", "dehydratatie"),
            ("H₂ afsplitsen uit een alcohol", "dehydrogenatie"),
            ("water adderen aan een alkeen", "hydratatie"),
        ],
        ["verestering"],
        "Hydro- gaat over waterstof, hydra- over water.",
    ),
    mk(
        "Je oxideert 2-methylpropaan-2-ol voorzichtig. Wat neem je waar?",
        [
            "Er gebeurt niets",
            "Er ontstaat een aldehyde en water",
            "Er ontstaat een keton en water",
            "Er ontstaat eerst een carbonzuur",
        ],
        0,
        "Het koolstofatoom met OH draagt geen H: er kan geen C=O ontstaan.",
    ),
    inv(
        "Hoeveel mol Br₂ kan er maximaal adderen aan 1 mol propyn?",
        ["2", "twee"],
        "Een drievoudige binding heeft twee pi-bindingen.",
    ),
    keuze(
        "De additie van water aan een alkeen vraagt een [[*zuur|base|radicaal]] als katalysator.",
        "Water alleen is te zwak als elektrofiel.",
    ),
    inv(
        "Hoeveel mol H₂ heb je nodig om 1 mol buta-1,3-dieen volledig te verzadigen?",
        ["2", "twee"],
        "Twee dubbele bindingen, elk één H₂.",
    ),
    tabel(
        "Klopt dit over additie aan een alkyn?",
        [
            ("Na één H₂ ontstaat een alkeen.", J),
            ("Na twee H₂ ontstaat een alkaan.", J),
            ("De sigma-binding tussen de C-atomen gaat open.", F),
        ],
        "Alleen de pi-bindingen gaan open.",
    ),
    mk(
        "Welk product overheerst als HCl addeert aan 2-methylpropeen, (CH₃)₂C=CH₂?",
        ["2-chloor-2-methylpropaan", "1-chloor-2-methylpropaan", "2-methylpropaan", "1,2-dichloor-2-methylpropaan"],
        0,
        "H gaat naar CH₂, Cl naar het koolstofatoom met de twee methylgroepen.",
    ),
    sorteer(
        "Ontstaat er bij dehydrogenatie van deze alcohol een aldehyde, een keton of niets?",
        ["Aldehyde", "Keton", "Niets"],
        [
            ("ethanol", "Aldehyde"),
            ("propaan-1-ol", "Aldehyde"),
            ("propaan-2-ol", "Keton"),
            ("butaan-2-ol", "Keton"),
            ("2-methylpropaan-2-ol", "Niets"),
        ],
        "Primair: aldehyde. Secundair: keton. Tertiair: geen dehydrogenatie.",
    ),
    keuze(
        "Bij de eliminatie van HBr uit broomethaan heb je een [[*base|zuur|katalysator zoals FeBr₃]] nodig.",
        "De base haalt het waterstofatoom van het buuratoom weg.",
    ),
    tabel(
        "Is dit een additie aan een C=C of aan een C=O?",
        [
            ("etheen + H₂", "C=C"),
            ("ethanal + H₂", "C=O"),
            ("propanon + H₂", "C=O"),
            ("propeen + HBr", "C=C"),
        ],
        "Aan C=C verloopt de additie elektrofiel, aan C=O nucleofiel.",
        kolommen=["C=C", "C=O"],
    ),
    open_(
        "Leg uit waarom een additie het omgekeerde is van een eliminatie.",
        "Bij een additie gaat een pi-binding open en komen er twee atomen of groepen bij op twee buuratomen. Bij een eliminatie gaan er net twee atomen of groepen weg van twee buuratomen en ontstaat er een nieuwe pi-binding. Een alkeen plus water geeft een alcohol, en een alcohol min water geeft weer het alkeen.",
    ),
]
