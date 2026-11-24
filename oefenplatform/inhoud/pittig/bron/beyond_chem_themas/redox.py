"""Oxidatiegetallen en redoxreacties — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Tabel van normpotentialen --------------------------------------------------
NP = Prent("normpotentialen", "Een stuk uit de tabel van normpotentialen", "tabel met links de geoxideerde vorm, in het midden de gereduceerde vorm en rechts de normpotentiaal in volt, van +1,36 bovenaan tot −2,37 onderaan")
RIJEN = [
    ("Cl₂", "Cl⁻", "+1,36"),
    ("Ag⁺", "Ag", "+0,80"),
    ("Cu²⁺", "Cu", "+0,34"),
    ("H₃O⁺", "H₂", "0,00"),
    ("Fe²⁺", "Fe", "−0,44"),
    ("Zn²⁺", "Zn", "−0,76"),
    ("Mg²⁺", "Mg", "−2,37"),
]
XK = [260, 500, 740]
NP.rect(140, 80, 720, 50, "#e8f0e0", DONKER, 8, 2)
for x, t in zip(XK, ("oxidator", "reductor", "E⁰ (V)")):
    NP.tekst(x, 113, t, 20, vet=True)
ZNP = {}
for i, (ox, red, e) in enumerate(RIJEN):
    y = 140 + i * 62
    NP.rect(140, y, 720, 56, "#ffffff" if i % 2 else "#fbf6ea", "#d9d4c4", 6, 1)
    NP.tekst(XK[0], y + 37, ox, 24, vet=True)
    NP.tekst(380, y + 37, "+ ne⁻ ⇌", 18)
    NP.tekst(XK[1], y + 37, red, 24, vet=True)
    NP.tekst(XK[2], y + 37, e, 22)
    ZNP[ox] = [Prent.zone(XK[0] - 70, y, 140, 56)]
    ZNP[red] = [Prent.zone(XK[1] - 70, y, 140, 56)]

# Drie proefbuizen -----------------------------------------------------------
PB = Prent("proefbuizen-metalen", "Drie proefbuizen: een metaalstrip in een oplossing", "drie proefbuizen met een etiket: zink in kopersulfaat, koper in zinksulfaat, zilver in zoutzuur; letters P, Q en R")
BUIZEN = {"P": ("Zn", "CuSO₄", "#bcd9ee"), "Q": ("Cu", "ZnSO₄", "#f4f9fd"), "R": ("Ag", "HCl", "#f4f9fd")}
for i, (k, (metaal, opl, kl)) in enumerate(BUIZEN.items()):
    x = 220 + i * 280
    PB.pad(f"M {x - 45} 120 L {x - 45} 430 Q {x - 45} 475 {x} 475 Q {x + 45} 475 {x + 45} 430 L {x + 45} 120", "#ffffff", DONKER, 3)
    PB.pad(f"M {x - 43} 260 L {x - 43} 430 Q {x - 43} 473 {x} 473 Q {x + 43} 473 {x + 43} 430 L {x + 43} 260 Z", kl, "none", 0)
    PB.rect(x - 10, 90, 20, 300, "#b9b6ad" if metaal != "Cu" else "#d08a4e", DONKER, 3, 2)
    PB.tekst(x, 515, f"{metaal} in {opl}", 20, vet=True)
    PB.letter(x, 570, k)
ZPB = {k: [Prent.zone(175 + i * 280, 90, 90, 390), Prent.rond(220 + i * 280, 570, 22)] for i, k in enumerate(BUIZEN)}

VRAGEN = [
    klik(
        "Klik in de tabel op de sterkste reductor.",
        NP.bestand, ZNP["Mg"],
        "Onderaan rechts: Mg staat het makkelijkst elektronen af.",
    ),
    klik(
        "Klik in de tabel op de sterkste oxidator.",
        NP.bestand, ZNP["Cl₂"],
        "Bovenaan links: Cl₂ neemt het makkelijkst elektronen op.",
    ),
    met_prent(NP.bestand, tabel(
        "Lost dit metaal op in zoutzuur?",
        [
            ("Mg", "Ja"),
            ("Zn", "Ja"),
            ("Cu", "Nee"),
            ("Ag", "Nee"),
        ],
        "Alleen metalen onder H₂ in de tabel worden door H₃O⁺ geoxideerd.",
        kolommen=["Ja", "Nee"],
    )),
    met_prent(NP.bestand, inv(
        "Hoeveel volt verschil zit er tussen het koppel van koper en dat van zink?",
        ["1,10", "1,1", "1.1", "1.10"],
        "0,34 − (−0,76) = 1,10 V.",
    )),
    klik(
        "Klik op de proefbuis waarin een redoxreactie spontaan doorgaat.",
        PB.bestand, ZPB["P"],
        "Zink is een sterkere reductor dan koper: Zn + Cu²⁺ → Zn²⁺ + Cu.",
    ),
    met_prent(PB.bestand, tabel(
        "Wat zie je na een tijdje in deze buis?",
        [
            ("P", "Koperkleurig neerslag op de strip"),
            ("Q", "Niets"),
            ("R", "Niets"),
        ],
        "In Q en R is de oxidator te zwak voor het metaal.",
        kolommen=["Koperkleurig neerslag op de strip", "Gasbelletjes", "Niets"],
    )),
    met_prent(PB.bestand, keuze(
        "In buis P wordt de blauwe kleur van de oplossing [[*lichter|donkerder|groen]].",
        "Cu²⁺-ionen worden gereduceerd tot koper en verdwijnen uit de oplossing.",
    )),
    tabel(
        "Welk oxidatiegetal heeft dit element in de verbinding?",
        [
            ("S in H₂SO₄", "+VI"),
            ("N in HNO₃", "+V"),
            ("Mn in KMnO₄", "+VII"),
            ("Cl in HClO", "+I"),
        ],
        "Reken met H +I, K +I en O −II; de som is nul.",
        kolommen=["+I", "+V", "+VI", "+VII"],
    ),
    tabel(
        "Welk oxidatiegetal heeft koolstof?",
        [
            ("CH₄", "−IV"),
            ("CH₃OH", "−II"),
            ("HCHO (methanal)", "0"),
            ("CO₂", "+IV"),
        ],
        "Hoe meer zuurstof aan het koolstofatoom, hoe hoger het oxidatiegetal.",
        kolommen=["−IV", "−II", "0", "+IV"],
    ),
    tabel(
        "Is dit een oxidatie of een reductie?",
        [
            ("Fe²⁺ → Fe³⁺", "Oxidatie"),
            ("Cl₂ → 2 Cl⁻", "Reductie"),
            ("Cu → Cu²⁺", "Oxidatie"),
            ("MnO₄⁻ → Mn²⁺", "Reductie"),
        ],
        "Stijgt het oxidatiegetal, dan is het een oxidatie.",
        kolommen=["Oxidatie", "Reductie"],
    ),
    casus(
        "In de reactie 2 Ag⁺ + Cu → 2 Ag + Cu²⁺ ...",
        [
            keuze(
                "... is koper de [[*reductor|oxidator]] en wordt het [[*geoxideerd|gereduceerd]].",
                "Koper staat twee elektronen af.",
            ),
            inv(
                "Hoeveel elektronen worden er in totaal uitgewisseld in deze vergelijking?",
                ["2", "twee"],
                "Eén koperatoom geeft 2 e⁻, die gaan naar 2 Ag⁺-ionen.",
            ),
            mk(
                "Waarom staat er een 2 voor Ag⁺?",
                [
                    "Zo zijn de elektronen in evenwicht",
                    "Zilver komt in de natuur altijd per twee atomen voor",
                    "Zo verloopt de reactie twee keer sneller",
                    "Zilver heeft in deze reactie oxidatiegetal +II",
                ],
                0,
                "Elk Ag⁺ neemt één elektron op, koper staat er twee af.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen bij het opstellen van een redoxvergelijking in zuur midden in volgorde.",
        [
            "Oxidatiegetallen bepalen",
            "De twee halfreacties opschrijven",
            "Zuurstof aanvullen met water en waterstof met H₃O⁺ of H⁺",
            "Elektronen gelijk maken met een factor",
            "De halfreacties optellen en vereenvoudigen",
        ],
        "Eerst zien wat er verandert, op het einde controleren op atomen en lading.",
    ),
    inv(
        "Hoeveel elektronen neemt mangaan op als MnO₄⁻ wordt omgezet tot Mn²⁺?",
        ["5", "vijf"],
        "Van +VII naar +II: vijf elektronen.",
    ),
    mk(
        "Waarom lost koper wel op in salpeterzuur maar niet in zoutzuur?",
        [
            "Nitraat is een sterkere oxidator",
            "Salpeterzuur bevat meer H₃O⁺ dan zoutzuur",
            "Chloride beschermt koper tegen elk zuur",
            "Koper staat onder waterstof in de tabel",
        ],
        0,
        "H₃O⁺ is te zwak voor koper, het nitraation niet.",
    ),
    tabel(
        "Gaat deze reactie spontaan door? Gebruik de waarden uit de tabel.",
        [
            ("Zn + Fe²⁺ → Zn²⁺ + Fe", "Ja"),
            ("Cu + Zn²⁺ → Cu²⁺ + Zn", "Nee"),
            ("Mg + 2 H₃O⁺ → Mg²⁺ + H₂ + 2 H₂O", "Ja"),
            ("2 Ag + Cu²⁺ → 2 Ag⁺ + Cu", "Nee"),
        ],
        "Spontaan als de oxidator hoger staat dan het koppel van de reductor.",
        kolommen=["Ja", "Nee"],
    ),
    sleep(
        "Een oxidator [[neemt]] elektronen op en wordt zelf [[gereduceerd]]. Zijn oxidatiegetal [[daalt]].",
        ["staat", "geoxideerd", "stijgt"],
        "Oxidator en reductor zitten altijd samen in een redoxreactie.",
    ),
    tabel(
        "Klopt dit over oxidatiegetallen?",
        [
            ("In O₂ heeft zuurstof oxidatiegetal 0.", J),
            ("In H₂O₂ heeft zuurstof −I.", J),
            ("In NaH heeft waterstof −I.", J),
            ("In een ion is de som altijd nul.", F),
        ],
        "In een ion is de som gelijk aan de lading.",
    ),
    koppel(
        "Koppel elk ion aan het oxidatiegetal van het centrale atoom.",
        [
            ("SO₄²⁻", "+VI"),
            ("NO₃⁻", "+V"),
            ("Cr₂O₇²⁻", "+VI per Cr"),
            ("ClO₄⁻", "+VII"),
        ],
        ["−II"],
        "Som van de oxidatiegetallen = lading van het ion.",
    ),
    mk(
        "Wat is een toeschouwerion in de reactie van zink met kopersulfaat?",
        ["SO₄²⁻", "Zn²⁺", "Cu²⁺", "CuSO₄"],
        0,
        "Het sulfaation staat links en rechts onveranderd.",
    ),
    tabel(
        "Welke deeltjes gebruik je om een halfreactie in te vullen?",
        [
            ("zuur midden: zuurstof aanvullen", "H₂O"),
            ("zuur midden: lading en waterstof", "H₃O⁺"),
            ("basisch midden: lading", "OH⁻"),
        ],
        "In basisch midden staat er geen H₃O⁺ in de oplossing.",
        kolommen=["H₂O", "H₃O⁺", "OH⁻"],
    ),
    inv(
        "Welk oxidatiegetal heeft ijzer in Fe₂O₃? Schrijf als +II, +III, ...",
        ["+III", "+3", "III"],
        "3 × (−II) = −6, verdeeld over twee ijzeratomen: +III.",
    ),
    mk(
        "Bij de verbranding van methaan, CH₄ + 2 O₂ → CO₂ + 2 H₂O, hoeveel eenheden stijgt het oxidatiegetal van koolstof?",
        ["8", "4", "2", "6"],
        0,
        "Van −IV naar +IV.",
    ),
    tabel(
        "Kan dit deeltje als oxidator, als reductor of als beide werken?",
        [
            ("Fe²⁺", "Beide"),
            ("Mg", "Reductor"),
            ("Cl₂", "Oxidator"),
        ],
        "Fe²⁺ kan naar Fe³⁺ (reductor) of naar Fe (oxidator).",
        kolommen=["Oxidator", "Reductor", "Beide"],
    ),
    keuze(
        "Een metaal dat [[*onder|boven]] waterstof staat in de tabel, lost op in zoutzuur met vorming van waterstofgas.",
        "Zo'n metaal is een sterkere reductor dan H₂.",
    ),
    inv(
        "Hoeveel elektronen staat één aluminiumatoom af om Al³⁺ te worden?",
        ["3", "drie"],
        "Van 0 naar +III.",
    ),
    tabel(
        "Klopt dit over het stuk tabel met normpotentialen?",
        [
            ("Ag⁺ kan Cu oxideren.", J),
            ("Zn kan Fe²⁺ reduceren.", J),
            ("Cu²⁺ kan Ag oxideren.", F),
        ],
        "Een oxidator reageert met elke reductor die lager in de tabel staat.",
    ),
    mk(
        "In de halfreactie MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O, waarom staan er 4 H₂O rechts?",
        [
            "Om de vier O-atomen op te vangen",
            "Om de lading links en rechts gelijk te maken",
            "Omdat de reactie in basisch midden doorgaat",
            "Om de vijf elektronen een plaats te geven",
        ],
        0,
        "In zuur midden vang je zuurstof op met water; de lading regel je met H⁺.",
    ),
    open_(
        "Leg uit waarom er in een redoxreactie altijd een oxidatie én een reductie tegelijk gebeuren.",
        "Elektronen bestaan niet los in een oplossing. Als een deeltje elektronen afstaat en geoxideerd wordt, moet een ander deeltje die elektronen opnemen en gereduceerd worden. Daarom moet het aantal afgestane elektronen gelijk zijn aan het aantal opgenomen elektronen.",
    ),
]
