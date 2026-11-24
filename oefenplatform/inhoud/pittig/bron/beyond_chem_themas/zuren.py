"""Zuren en basen volgens Brønsted-Lowry — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Protolysereactie -----------------------------------------------------------
PR = Prent("protolyse-ammoniak", "Een protolysereactie in water", "de vergelijking NH₃ + H₂O ⇌ NH₄⁺ + OH⁻ met onder elk deeltje een letter A tot D en een boogje dat een H⁺ toont")
XS = {"A": 170, "B": 380, "C": 640, "D": 850}
FORM = {"A": "NH₃", "B": "H₂O", "C": "NH₄⁺", "D": "OH⁻"}
for k, x in XS.items():
    PR.rect(x - 75, 270, 150, 80, "#ffffff", DONKER, 16, 2)
    PR.tekst(x, 323, FORM[k], 34, vet=True)
    PR.letter(x, 420, k)
PR.tekst(275, 323, "+", 34, vet=True)
PR.tekst(510, 323, "⇌", 40, vet=True)
PR.tekst(745, 323, "+", 34, vet=True)
PR.pad("M 380 262 Q 275 170 180 262", "none", ROOD, 3)
PR.pijl(205, 238, 182, 262, ROOD, 3)
PR.tekst(280, 195, "H⁺", 24, kleur=ROOD, vet=True)
ZPR = {k: [Prent.zone(x - 75, 270, 150, 80), Prent.rond(x, 420, 22)] for k, x in XS.items()}

# Drie zure oplossingen in deeltjesmodel -------------------------------------
DZ = Prent("sterk-zwak-zuur", "Drie oplossingen van drie verschillende zuren HA, als deeltjes", "drie bekerglazen P, Q en R met deeltjes HA, A⁻ en H₃O⁺ in verschillende verhoudingen (watermoleculen niet getekend)")
INHOUD = {
    "P": ["HA"] * 5 + ["A⁻", "H₃O⁺"],
    "Q": ["A⁻", "H₃O⁺"] * 4,
    "R": ["HA"] * 3 + ["A⁻", "H₃O⁺"] * 2,
}
KL = {"HA": "#cfe5f3", "A⁻": "#f7d9b5", "H₃O⁺": "#f3c6d0"}
SPOTS = [(-45, -100), (45, -85), (-50, -35), (40, -20), (-45, 30), (50, 45), (-40, 95), (45, 110)]
for i, (k, lijst) in enumerate(INHOUD.items()):
    cx = 180 + i * 320
    DZ.pad(f"M {cx - 120} 150 L {cx - 120} 440 Q {cx - 120} 465 {cx - 95} 465 L {cx + 95} 465 Q {cx + 120} 465 {cx + 120} 440 L {cx + 120} 150", "#f4f9fd", DONKER, 3)
    for j, d in enumerate(lijst):
        dx, dy = SPOTS[j]
        DZ.rect(cx + dx - 32, 320 + dy - 18, 64, 36, KL[d], DONKER, 14, 1)
        DZ.tekst(cx + dx, 320 + dy + 7, d, 17, vet=True)
    DZ.letter(cx, 530, k)
ZDZ = {k: [Prent.zone(60 + i * 320, 150, 240, 315), Prent.rond(180 + i * 320, 530, 22)] for i, k in enumerate(INHOUD)}

VRAGEN = [
    klik(
        "Klik op het deeltje dat in de heenreactie als zuur werkt.",
        PR.bestand, ZPR["B"],
        "Water staat een proton af aan ammoniak.",
    ),
    klik(
        "Klik op de geconjugeerde base van water in deze reactie.",
        PR.bestand, ZPR["D"],
        "H₂O min één proton is OH⁻.",
    ),
    met_prent(PR.bestand, tabel(
        "Welke rol speelt dit deeltje in de reactie?",
        [
            ("A", "Base"),
            ("B", "Zuur"),
            ("C", "Zuur"),
            ("D", "Base"),
        ],
        "In de terugreactie staat NH₄⁺ een proton af aan OH⁻. Zo ontstaan twee geconjugeerde paren.",
        kolommen=["Zuur", "Base"],
    )),
    klik(
        "Klik op de oplossing van een sterk zuur.",
        DZ.bestand, ZDZ["Q"],
        "Een sterk zuur staat zijn proton zo goed als volledig af: geen HA meer over.",
    ),
    klik(
        "Klik op de oplossing van het zwakste zuur.",
        DZ.bestand, ZDZ["P"],
        "Daar is het kleinste deel van de HA-moleculen geïoniseerd.",
    ),
    met_prent(DZ.bestand, tabel(
        "Wat is de ionisatiegraad in deze oplossing, afgelezen uit de tekening?",
        [
            ("P", "1 op 6"),
            ("Q", "4 op 4"),
            ("R", "2 op 5"),
        ],
        "Tel de A⁻-ionen ten opzichte van alle zuurdeeltjes, HA en A⁻ samen. Elke A⁻ was eerst een HA.",
        kolommen=["1 op 6", "2 op 5", "4 op 4"],
    )),
    tabel(
        "Wat is het geconjugeerde zuur of de geconjugeerde base?",
        [
            ("de base van H₂SO₄", "HSO₄⁻"),
            ("het zuur van NH₃", "NH₄⁺"),
            ("de base van HCO₃⁻", "CO₃²⁻"),
            ("het zuur van HCO₃⁻", "H₂CO₃"),
        ],
        "Een paar verschilt altijd precies één proton.",
        kolommen=["HSO₄⁻", "NH₄⁺", "CO₃²⁻", "H₂CO₃"],
    ),
    tabel(
        "Kan dit deeltje als amfolyt werken?",
        [
            ("H₂O", "Ja"),
            ("HCO₃⁻", "Ja"),
            ("H₂PO₄⁻", "Ja"),
            ("Cl⁻", "Nee"),
            ("H₃O⁺", "Nee"),
        ],
        "Een amfolyt kan een proton afstaan én opnemen.",
        kolommen=["Ja", "Nee"],
    ),
    mk(
        "Zuur X heeft pKz = 4,8 en zuur Y heeft pKz = 3,2. Wat weet je?",
        [
            "Y is sterker en zijn base is zwakker",
            "X is sterker en zijn base is zwakker",
            "Y is sterker en zijn base ook sterker",
            "Ze zijn even sterk, de concentratie beslist",
        ],
        0,
        "Kleinere pKz = sterker zuur. Hoe sterker het zuur, hoe zwakker de geconjugeerde base.",
    ),
    tabel(
        "Is de oplossing van dit zout zuur, basisch of neutraal?",
        [
            ("natriumchloride", "Neutraal"),
            ("natriumacetaat", "Basisch"),
            ("ammoniumchloride", "Zuur"),
            ("kaliumnitraat", "Neutraal"),
        ],
        "Kijk welk ion de geconjugeerde base of het geconjugeerde zuur is van iets zwaks.",
        kolommen=["Zuur", "Basisch", "Neutraal"],
    ),
    casus(
        "Je hebt twee flessen met 0,1 mol/L: zoutzuur en azijnzuur.",
        [
            keuze(
                "Zoutzuur heeft de [[*laagste|hoogste]] pH van de twee.",
                "HCl ioniseert volledig en geeft meer H₃O⁺.",
            ),
            tabel(
                "Klopt dit over de twee flessen?",
                [
                    ("Ze bevatten evenveel mol zuur per liter.", J),
                    ("In de fles azijnzuur zitten vooral niet-geïoniseerde moleculen.", J),
                    ("Azijnzuur is minder geconcentreerd dan zoutzuur.", F),
                ],
                "Sterk of zwak gaat over de ionisatie, niet over de concentratie.",
            ),
            mk(
                "Welk deeltje komt in de fles azijnzuur het meest voor, naast water?",
                ["CH₃COOH", "CH₃COO⁻", "H₃O⁺", "OH⁻"],
                0,
                "Slechts een klein deel van de azijnzuurmoleculen is geïoniseerd.",
            ),
        ],
    ),
    inv(
        "Hoeveel protonen kan het carbonaation CO₃²⁻ in totaal opnemen?",
        ["2", "twee"],
        "CO₃²⁻ → HCO₃⁻ → H₂CO₃: een tweewaardige base.",
    ),
    volgorde(
        "Zet de stappen bij het afstaan van alle protonen van fosforzuur in volgorde.",
        ["H₃PO₄", "H₂PO₄⁻", "HPO₄²⁻", "PO₄³⁻"],
        "Elke stap gaat er een proton af en wordt de lading één negatiever.",
    ),
    sleep(
        "Een zuur is een protondonor en een base is een proton[[acceptor]]. Bij een protolysereactie gaat een [[H⁺]] van het zuur naar de base. Een base hoeft daarvoor geen [[OH-groep]] te hebben.",
        ["donor", "OH⁻", "dubbele binding"],
        "Ammoniak is een base zonder OH-groep.",
    ),
    tabel(
        "Klopt dit over Kz en Kb van een geconjugeerd paar?",
        [
            ("Kz · Kb is gelijk aan de ionisatieconstante van water.", J),
            ("Een grote Kz hoort bij een kleine Kb.", J),
            ("pKz + pKb = 14 bij 25 °C.", J),
            ("Een sterk zuur heeft een sterke geconjugeerde base.", F),
        ],
        "Kz · Kb = 10⁻¹⁴ bij 25 °C.",
    ),
    inv(
        "Een zuur heeft pKz = 4,8. Wat is de pKb van zijn geconjugeerde base bij 25 °C?",
        ["9,2", "9.2"],
        "14 − 4,8 = 9,2.",
    ),
    mk(
        "Waarom werkt een zuurbase-indicator?",
        [
            "Het zuur en zijn base hebben een andere kleur",
            "De indicator reageert enkel met sterke zuren",
            "De indicator verandert van kleur door warmte",
            "Hij lost alleen in basisch midden goed op",
        ],
        0,
        "De indicator is zelf een zwak zuur; de pH bepaalt welke vorm overheerst.",
    ),
    koppel(
        "Koppel elk zuur aan zijn waardigheid.",
        [
            ("HCl", "eenwaardig"),
            ("H₂SO₄", "tweewaardig"),
            ("H₃PO₄", "driewaardig"),
        ],
        ["vierwaardig"],
        "Tel de protonen die het zuur kan afstaan.",
    ),
    tabel(
        "Is dit een sterk of een zwak zuur?",
        [
            ("zoutzuur", "Sterk"),
            ("salpeterzuur", "Sterk"),
            ("azijnzuur", "Zwak"),
            ("koolzuur", "Zwak"),
        ],
        "HCl, HNO₃ en H₂SO₄ zijn de bekende sterke zuren.",
        kolommen=["Sterk", "Zwak"],
    ),
    mk(
        "Je lost ammoniumchloride op in water en meet een pH onder 7. Welk deeltje zorgt daarvoor?",
        [
            "NH₄⁺, dat een proton afstaat",
            "Cl⁻, dat een proton opneemt",
            "OH⁻ uit het ammoniumchloride",
            "Cl⁻, dat een sterke base is",
        ],
        0,
        "NH₄⁺ is het geconjugeerde zuur van de zwakke base ammoniak.",
    ),
    inv(
        "Hoeveel geconjugeerde zuur-baseparen zitten er in één protolysereactie?",
        ["2", "twee"],
        "Het zuur met zijn base en de base met haar zuur.",
    ),
    tabel(
        "Welk deeltje is hier de geconjugeerde base van?",
        [
            ("OH⁻", "H₂O"),
            ("H₂O", "H₃O⁺"),
            ("NH₃", "NH₄⁺"),
        ],
        "Tel er één proton bij om het geconjugeerde zuur te vinden.",
        kolommen=["H₂O", "H₃O⁺", "NH₄⁺"],
    ),
    mk(
        "Waarom is het chloride-ion in water geen merkbare base?",
        [
            "Het is de geconjugeerde base van een sterk zuur",
            "Het heeft geen vrij elektronenpaar om te binden",
            "Het is positief geladen en stoot protonen af",
            "Het lost helemaal niet op in water",
        ],
        0,
        "HCl staat zijn proton zo graag af dat Cl⁻ het bijna nooit terugneemt.",
    ),
    keuze(
        "Water reageert met azijnzuur als een [[*base|zuur]], en met ammoniak als een [[zuur|*base]].",
        "Bij azijnzuur neemt water een proton op, bij ammoniak staat het er een af.",
    ),
    tabel(
        "Klopt dit over de ionisatiegraad?",
        [
            ("Bij een sterk zuur ligt ze bijna op 100 %.", J),
            ("Bij een zwak zuur is ze klein.", J),
            ("Ze is altijd gelijk aan de pH.", F),
        ],
        "De ionisatiegraad is het deel van de moleculen dat zijn proton heeft afgestaan.",
    ),
    mk(
        "In welke richting ligt het evenwicht HCO₃⁻ + OH⁻ ⇌ CO₃²⁻ + H₂O?",
        [
            "Naar rechts: OH⁻ is een sterkere base dan CO₃²⁻",
            "Naar links: H₂O is een sterker zuur dan HCO₃⁻",
            "Precies in het midden, want beide zijn amfolyten",
            "Er is geen evenwicht, want er reageert niets",
        ],
        0,
        "Een protolyse loopt naar de kant van het zwakste zuur en de zwakste base.",
    ),
    sorteer(
        "Is dit deeltje in water een zuur, een base of beide?",
        ["Zuur", "Base", "Beide"],
        [
            ("NH₄⁺", "Zuur"),
            ("H₃O⁺", "Zuur"),
            ("CH₃COO⁻", "Base"),
            ("OH⁻", "Base"),
            ("HSO₄⁻", "Beide"),
            ("H₂O", "Beide"),
        ],
        "Een amfolyt kan beide.",
    ),
    open_(
        "Leg uit wat het verschil is tussen een sterk zuur en een geconcentreerd zuur.",
        "Sterk zegt hoe goed een zuur zijn protonen afstaat: een sterk zuur ioniseert in water zo goed als volledig. Geconcentreerd zegt hoeveel zuur er per liter opgelost is. Een zwak zuur kan dus geconcentreerd zijn, en een sterk zuur kan sterk verdund zijn.",
    ),
]
