"""Galvanische cellen en elektrolyse — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL


def _beker(p, x, kl):
    p.pad(f"M {x - 110} 300 L {x - 110} 540 Q {x - 110} 560 {x - 90} 560 L {x + 90} 560 Q {x + 110} 560 {x + 110} 540 L {x + 110} 300", "#ffffff", DONKER, 3)
    p.rect(x - 108, 360, 216, 198, kl, "none", 10, 0)


# Galvanische cel zink-koper -------------------------------------------------
GC = Prent("galvanische-cel", "Een galvanische cel met zink en koper", "twee bekers: links een zinkstaaf in een zinksulfaatoplossing, rechts een koperstaaf in kopersulfaat; bovenaan een draad met een voltmeter, tussen de bekers een zoutbrug; letters A tot E")
_beker(GC, 250, "#eef1f3")
_beker(GC, 750, "#bcd9ee")
GC.rect(230, 230, 40, 280, "#b9b6ad", DONKER, 4, 2)
GC.rect(730, 230, 40, 280, "#d08a4e", DONKER, 4, 2)
GC.tekst(250, 590, "ZnSO₄", 18, vet=True)
GC.tekst(750, 590, "CuSO₄", 18, vet=True)
GC.pad("M 320 470 L 320 330 Q 320 300 350 300 L 650 300 Q 680 300 680 330 L 680 470", "none", "#efe6f5", 34)
GC.pad("M 320 470 L 320 330 Q 320 300 350 300 L 650 300 Q 680 300 680 330 L 680 470", "none", DONKER, 2)
GC.lijn(250, 230, 250, 110, DONKER, 3)
GC.lijn(750, 230, 750, 110, DONKER, 3)
GC.lijn(250, 110, 455, 110, DONKER, 3)
GC.lijn(545, 110, 750, 110, DONKER, 3)
GC.cirkel(500, 110, 45, "#ffffff", DONKER, 3)
GC.tekst(500, 122, "V", 32, vet=True)
LGC = {"A": (160, 260), "B": (850, 260), "C": (360, 75), "D": (500, 360), "E": (580, 60)}
for k, (x, y) in LGC.items():
    GC.letter(x, y, k)
GC.lijn(182, 265, 228, 290, GRIJS, 1)
GC.lijn(828, 265, 772, 290, GRIJS, 1)
GC.lijn(360, 97, 360, 108, GRIJS, 1)
GC.lijn(500, 338, 500, 318, GRIJS, 1)
GC.lijn(562, 74, 535, 85, GRIJS, 1)
ZGC = {"A": [Prent.zone(230, 230, 40, 280), Prent.rond(*LGC["A"], 22)],
       "B": [Prent.zone(730, 230, 40, 280), Prent.rond(*LGC["B"], 22)],
       "C": [Prent.zone(260, 95, 190, 30), Prent.zone(550, 95, 190, 30), Prent.rond(*LGC["C"], 22)],
       "D": [Prent.zone(300, 280, 400, 40), Prent.zone(300, 280, 40, 200), Prent.zone(660, 280, 40, 200), Prent.rond(*LGC["D"], 22)],
       "E": [Prent.rond(500, 110, 45), Prent.rond(*LGC["E"], 22)]}

# Elektrolyse van koperchloride ----------------------------------------------
EL = Prent("elektrolyse-koperchloride", "Elektrolyse van een oplossing van koper(II)chloride", "één beker met twee koolstofstaven, verbonden met een spanningsbron met een plus- en een minpool; elektroden P en Q")
_beker(EL, 500, "#bcd9ee")
EL.rect(425, 200, 30, 330, "#5a5a5a", DONKER, 4, 2)
EL.rect(545, 200, 30, 330, "#5a5a5a", DONKER, 4, 2)
EL.lijn(440, 200, 440, 110, DONKER, 3)
EL.lijn(560, 200, 560, 110, DONKER, 3)
EL.lijn(440, 110, 480, 110, DONKER, 3)
EL.lijn(520, 110, 560, 110, DONKER, 3)
EL.lijn(480, 75, 480, 145, DONKER, 4)
EL.lijn(520, 92, 520, 128, DONKER, 7)
EL.tekst(462, 70, "+", 30, vet=True)
EL.tekst(540, 80, "−", 30, vet=True)
EL.tekst(500, 590, "CuCl₂-oplossing", 18, vet=True)
EL.letter(320, 300, "P")
EL.letter(680, 300, "Q")
EL.lijn(342, 300, 423, 300, GRIJS, 1)
EL.lijn(658, 300, 577, 300, GRIJS, 1)
ZEL = {"P": [Prent.zone(425, 200, 30, 330), Prent.rond(320, 300, 22)],
       "Q": [Prent.zone(545, 200, 30, 330), Prent.rond(680, 300, 22)]}

VRAGEN = [
    klik(
        "Klik op de anode van de galvanische cel.",
        GC.bestand, ZGC["A"],
        "Zink is de sterkste reductor en wordt geoxideerd.",
    ),
    klik(
        "Klik op het deel waardoor ionen bewegen om de lading in evenwicht te houden.",
        GC.bestand, ZGC["D"],
        "De zoutbrug. Elektronen gaan door de draad, ionen door de brug.",
    ),
    met_prent(GC.bestand, tabel(
        "Wat gebeurt er met deze elektrode als de cel een tijd werkt?",
        [
            ("A", "Wordt lichter"),
            ("B", "Wordt zwaarder"),
        ] + [("de blauwe kleur rechts", "Wordt lichter")],
        "Zink lost op als Zn²⁺, koper slaat neer en Cu²⁺ verdwijnt uit de oplossing.",
        kolommen=["Wordt zwaarder", "Wordt lichter"],
    )),
    met_prent(GC.bestand, inv(
        "Wat wijst de voltmeter E aan bij normomstandigheden? Cu²⁺/Cu = +0,34 V, Zn²⁺/Zn = −0,76 V.",
        ["1,10", "1,1", "1.1", "1.10", "1,10 V"],
        "E(kathode) − E(anode) = 0,34 − (−0,76) = 1,10 V.",
    )),
    met_prent(GC.bestand, tabel(
        "Kijk naar de cel. Klopt dit?",
        [
            ("Elektronen lopen door C van A naar B.", J),
            ("B is de positieve pool.", J),
            ("Negatieve ionen uit D bewegen naar de beker met zink.", J),
            ("Elektronen lopen door de zoutbrug.", F),
        ],
        "In de zinkhalfcel komen Zn²⁺-ionen bij; negatieve ionen uit de brug compenseren dat.",
    )),
    klik(
        "Klik op de elektrode waar koper neerslaat.",
        EL.bestand, ZEL["Q"],
        "Q hangt aan de minpool: daar is de kathode en worden Cu²⁺-ionen gereduceerd.",
    ),
    met_prent(EL.bestand, tabel(
        "Wat geldt voor deze elektrode?",
        [
            ("P", "Anode, oxidatie"),
            ("Q", "Kathode, reductie"),
        ] + [("de elektrode waar chloorgas ontstaat", "Anode, oxidatie")],
        "Bij een elektrolyse is de anode de pluspool: Cl⁻ wordt daar geoxideerd tot Cl₂.",
        kolommen=["Anode, oxidatie", "Kathode, reductie"],
    )),
    met_prent(EL.bestand, mk(
        "Waarom is een spanningsbron nodig in deze opstelling?",
        [
            "Deze reactie gaat niet vanzelf door",
            "Zonder bron lost de koolstof op in de oplossing",
            "De bron levert de Cu²⁺-ionen voor de reactie",
            "De bron houdt de oplossing warm genoeg",
        ],
        0,
        "Cl₂ is een sterkere oxidator dan Cu²⁺: de omgekeerde reactie is spontaan, deze moet je afdwingen.",
    )),
    tabel(
        "Geldt dit voor een galvanische cel, een elektrolyse of beide?",
        [
            ("de oxidatie gebeurt aan de anode", "Beide"),
            ("de anode is de negatieve pool", "Galvanische cel"),
            ("er is een spanningsbron nodig", "Elektrolyse"),
            ("chemische energie wordt elektrische energie", "Galvanische cel"),
        ],
        "De afspraak over anode en kathode is altijd dezelfde, de polen wisselen.",
        kolommen=["Galvanische cel", "Elektrolyse", "Beide"],
    ),
    inv(
        "Bereken de bronspanning van een cel met Ag⁺/Ag (+0,80 V) en Cu²⁺/Cu (+0,34 V).",
        ["0,46", "0.46", "0,46 V"],
        "0,80 − 0,34 = 0,46 V. Koper is hier de anode.",
    ),
    tabel(
        "Welk metaal is de anode in deze cel?",
        [
            ("zink en koper", "Zn"),
            ("koper en zilver", "Cu"),
            ("magnesium en zink", "Mg"),
        ],
        "De anode is het metaal met de laagste normpotentiaal.",
        kolommen=["Zn", "Cu", "Mg"],
    ),
    casus(
        "Een cel wordt voorgesteld als Mg/Mg²⁺//Ag⁺/Ag. Gebruik Mg²⁺/Mg = −2,37 V en Ag⁺/Ag = +0,80 V.",
        [
            keuze(
                "De anode is [[*magnesium|zilver]].",
                "Links in de voorstelling staat de anode.",
            ),
            inv(
                "Wat is de bronspanning in volt?",
                ["3,17", "3.17", "3,17 V"],
                "0,80 − (−2,37) = 3,17 V.",
            ),
            mk(
                "Wat betekent de dubbele streep in het midden?",
                ["De zoutbrug", "De draad", "De voltmeter", "Een neerslag"],
                0,
                "Een enkele streep scheidt een elektrode van haar oplossing.",
            ),
        ],
    ),
    volgorde(
        "Volg de weg van de lading in een zink-kopercel, vanaf de oxidatie.",
        [
            "Zink staat elektronen af aan de anode",
            "De elektronen lopen door de draad",
            "Cu²⁺ neemt de elektronen op aan de kathode",
            "Ionen in de zoutbrug houden beide bekers neutraal",
        ],
        "De stroomkring is pas gesloten door draad én zoutbrug.",
    ),
    mk(
        "Waarom kan je gesmolten keukenzout elektrolyseren, maar vast keukenzout niet?",
        [
            "In de smelt kunnen de ionen bewegen",
            "In de smelt zijn er meer elektronen",
            "Vast zout bevat geen natriumionen",
            "Vast zout is een metaal en geleidt te goed",
        ],
        0,
        "Ionen moeten naar de elektroden kunnen gaan.",
    ),
    sleep(
        "Bij een elektrolyse is de kathode de [[negatieve]] pool. Daar worden positieve ionen [[gereduceerd]]. De reactie is [[gedwongen]].",
        ["positieve", "geoxideerd", "spontaan"],
        "Bij een galvanische cel is de kathode net de positieve pool.",
    ),
    tabel(
        "Klopt dit over een oplaadbare batterij?",
        [
            ("Bij het ontladen werkt ze als galvanische cel.", J),
            ("Bij het opladen gebeurt er een elektrolyse.", J),
            ("Bij het opladen gaat de reactie spontaan.", F),
        ],
        "Opladen duwt de reactie terug met elektrische energie.",
    ),
    koppel(
        "Koppel elk onderdeel van een galvanische cel aan zijn taak.",
        [
            ("anode", "plaats van de oxidatie"),
            ("kathode", "plaats van de reductie"),
            ("draad", "elektronenbrug"),
            ("zoutbrug", "ionen laten bewegen"),
        ],
        ["spanning afdwingen"],
        "Een galvanische cel heeft geen spanningsbron nodig.",
    ),
    tabel(
        "Wat ontstaat er bij de elektrolyse van water?",
        [
            ("aan de kathode", "H₂"),
            ("aan de anode", "O₂"),
            ("in totaal, per mol O₂", "2 mol H₂"),
        ],
        "2 H₂O → 2 H₂ + O₂.",
        kolommen=["H₂", "O₂", "2 mol H₂"],
    ),
    mk(
        "Bij het verzilveren van een lepel hangt de lepel aan de minpool. Welke elektrode gebruik je aan de pluspool?",
        ["Een staaf zilver", "Een staaf koolstof", "Een tweede lepel", "Een staaf zink"],
        0,
        "Het zilver van de anode lost op en vult de Ag⁺-ionen aan die op de lepel neerslaan.",
    ),
    keuze(
        "Aluminium maakt men met elektrolyse omdat Al³⁺ een [[*heel zwakke oxidator|heel sterke oxidator|sterke reductor]] is.",
        "Geen gewone reductor kan Al³⁺ spontaan reduceren.",
    ),
    tabel(
        "Is dit een galvanische cel of een elektrolyse?",
        [
            ("een zaklampbatterij die stroom levert", "Galvanisch"),
            ("een gsm die aan de lader hangt", "Elektrolyse"),
            ("koper zuiveren met stroom", "Elektrolyse"),
            ("een brandstofcel in een auto", "Galvanisch"),
        ],
        "Levert het stroom, dan is het galvanisch; vraagt het stroom, dan is het een elektrolyse.",
        kolommen=["Galvanisch", "Elektrolyse"],
    ),
    inv(
        "Een galvanische cel heeft een bronspanning van 1,56 V. De kathode is Ag⁺/Ag (+0,80 V). Wat is de normpotentiaal van de anode?",
        ["-0,76", "−0,76", "-0.76", "−0,76 V"],
        "0,80 − E(anode) = 1,56, dus E(anode) = −0,76 V: zink.",
    ),
    mk(
        "In welke richting gaan de positieve ionen bij een elektrolyse?",
        ["Naar de kathode, de minpool", "Naar de anode, de pluspool", "Ze blijven stil liggen", "Naar de spanningsbron"],
        0,
        "Tegengestelde ladingen trekken elkaar aan.",
    ),
    tabel(
        "Wat gebeurt er met de spanning van een galvanische cel?",
        [
            ("de normpotentialen liggen verder uit elkaar", "Groter"),
            ("de reactie is helemaal uitgewerkt", "Kleiner"),
            ("je vervangt koper door zilver tegenover zink", "Groter"),
        ],
        "Een uitgewerkte batterij heeft geen spanning meer.",
        kolommen=["Groter", "Kleiner"],
    ),
    keuze(
        "Elke halfcel heeft haar eigen beker, anders reageren zink en Cu²⁺ [[*rechtstreeks|helemaal niet|via de draad]].",
        "Dan komt de energie vrij als warmte en loopt er geen stroom door de draad.",
    ),
    tabel(
        "Klopt dit over de symbolische voorstelling Zn/Zn²⁺//Cu²⁺/Cu?",
        [
            ("Links staat de anode.", J),
            ("De enkele streep scheidt elektrode en oplossing.", J),
            ("Rechts gebeurt de oxidatie.", F),
        ],
        "Rechts staat de kathode, waar de reductie gebeurt.",
    ),
    sorteer(
        "Gebeurt dit aan de anode of aan de kathode van een elektrolyse van CuCl₂?",
        ["Anode", "Kathode"],
        [
            ("Cl⁻ staat elektronen af", "Anode"),
            ("er ontstaat chloorgas", "Anode"),
            ("Cu²⁺ neemt elektronen op", "Kathode"),
            ("er slaat koper neer", "Kathode"),
        ],
        "Oxidatie aan de anode, reductie aan de kathode.",
    ),
    open_(
        "Leg uit waarom een galvanische cel stopt met werken als je de zoutbrug weghaalt.",
        "Zonder zoutbrug kunnen er geen ionen tussen de twee bekers bewegen. In de beker van de anode komen er positieve ionen bij en in de beker van de kathode verdwijnen er. Er bouwt zich snel een lading op die de elektronen tegenhoudt, zodat er geen stroom meer loopt.",
    ),
]
