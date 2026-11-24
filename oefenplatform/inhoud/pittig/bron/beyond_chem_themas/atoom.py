"""Atoombouw, orbitalen en het periodiek systeem — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Hokjesvoorstellingen van stikstof ----------------------------------------
HK = Prent("hokjes-stikstof", "Drie hokjesvoorstellingen voor een stikstofatoom (7 elektronen)", "drie rijen hokjes 1s, 2s en drie hokjes 2p met pijltjes op en neer; letters P, Q en R")


def _pijl(p, x, y, op):
    if op:
        p.pijl(x, y + 22, x, y - 18, DONKER, 3)
    else:
        p.pijl(x, y - 22, x, y + 18, DONKER, 3)


VULLINGEN = {
    "P": [[1, 0], [1, 0], [1], [1], [1]],
    "Q": [[1, 0], [1, 0], [1, 0], [1], []],
    "R": [[1, 1], [1, 0], [1], [1], [1]],
}
for r, (k, vul) in enumerate(VULLINGEN.items()):
    y = 150 + r * 150
    HK.letter(70, y, k)
    for j, (lab, x) in enumerate((("1s", 170), ("2s", 300), ("2p", 450), ("", 510), ("", 570))):
        HK.rect(x - 30, y - 30, 60, 60, "#ffffff", DONKER, 0, 2)
        if lab:
            HK.tekst(x + (60 if lab == "2p" else 0), y + 60, lab, 17, vet=True)
        els = vul[j]
        if len(els) == 2:
            _pijl(HK, x - 12, y, els[0] == 1)
            _pijl(HK, x + 12, y, els[1] == 1)
        elif len(els) == 1:
            _pijl(HK, x, y, True)
ZHK = {k: [Prent.zone(40, 110 + r * 150, 580, 80)] for r, k in enumerate(VULLINGEN)}

# Periodiek systeem in blokken ---------------------------------------------
PS = Prent("periodiek-blokken", "Het periodiek systeem, ingedeeld in blokken", "schema met het s-blok links, het d-blok in het midden, het p-blok rechts en het f-blok eronder; vijf letters A tot E")
CEL = 46
for rij in range(7):
    for kol in range(18):
        if rij == 0 and kol not in (0, 17):
            continue
        if rij in (1, 2) and 2 <= kol <= 11:
            continue
        kl = "#f3c6d0" if kol < 2 else ("#cfe5f3" if kol < 12 else "#d6ecd2")
        if kol == 17:
            kl = "#f5d9a8"
        PS.rect(80 + kol * CEL, 80 + rij * CEL, CEL - 3, CEL - 3, kl, DONKER, 3, 1)
for rij in range(2):
    for kol in range(14):
        PS.rect(80 + 3 * CEL + kol * CEL, 430 + rij * CEL, CEL - 3, CEL - 3, "#efe6f5", DONKER, 3, 1)
LPS = {"A": (80 + 0.5 * CEL, 80 + 7.6 * CEL), "B": (80 + 16.5 * CEL, 55), "C": (80 + 7 * CEL, 55), "D": (80 + 17.5 * CEL, 80 + 7.6 * CEL), "E": (80 + 10 * CEL, 560)}
for k, (x, y) in LPS.items():
    PS.letter(x, y, k)
ZPS = {"A": [Prent.zone(80, 80 + CEL, CEL, 6 * CEL), Prent.rond(*LPS["A"], 22)],
       "B": [Prent.zone(80 + 16 * CEL, 80 + CEL, CEL, 6 * CEL), Prent.rond(*LPS["B"], 22)],
       "C": [Prent.zone(80 + 2 * CEL, 80 + 3 * CEL, 10 * CEL, 4 * CEL), Prent.rond(*LPS["C"], 22)],
       "D": [Prent.zone(80 + 17 * CEL, 80, CEL, 7 * CEL), Prent.rond(*LPS["D"], 22)],
       "E": [Prent.zone(80 + 3 * CEL, 430, 14 * CEL, 2 * CEL), Prent.rond(*LPS["E"], 22)]}
PS.lijn(80 + 0.5 * CEL, 80 + 7.6 * CEL - 22, 80 + 0.5 * CEL, 80 + 7 * CEL, DONKER, 1)
PS.lijn(80 + 17.5 * CEL, 80 + 7.6 * CEL - 22, 80 + 17.5 * CEL, 80 + 7 * CEL, DONKER, 1)
PS.lijn(80 + 16.5 * CEL, 77, 80 + 16.5 * CEL, 80 + CEL, DONKER, 1)
PS.lijn(80 + 7 * CEL, 77, 80 + 7 * CEL, 80 + 3 * CEL, DONKER, 1)

VRAGEN = [
    klik(
        "Klik op de juiste hokjesvoorstelling van stikstof.",
        HK.bestand, ZHK["P"],
        "De drie 2p-elektronen zitten elk in een eigen hokje met dezelfde spin: regel van Hund.",
    ),
    met_prent(HK.bestand, tabel(
        "Welke regel wordt overtreden?",
        [
            ("P", "Geen"),
            ("Q", "Hund"),
            ("R", "Pauli"),
        ],
        "In R hebben twee elektronen in 1s dezelfde spin. In Q zitten er twee in één 2p-hokje terwijl er een leeg is.",
        kolommen=["Geen", "Hund", "Pauli"],
    )),
    met_prent(HK.bestand, tabel(
        "Kijk naar de juiste voorstelling P. Klopt dit?",
        [
            ("Stikstof heeft 1s² 2s² 2p³.", J),
            ("Stikstof heeft vijf valentie-elektronen.", J),
            ("Stikstof heeft drie ongepaarde elektronen.", J),
            ("Het 2s-subniveau is half gevuld.", F),
        ],
        "2s is helemaal vol, 2p is half gevuld.",
    )),
    klik(
        "Klik op de groep van de halogenen.",
        PS.bestand, ZPS["B"],
        "Groep 17: zeven valentie-elektronen.",
    ),
    klik(
        "Klik op de zeldzame aarden.",
        PS.bestand, ZPS["E"],
        "Het f-blok: de twee rijen die onder het systeem apart staan.",
    ),
    met_prent(PS.bestand, tabel(
        "Welke letter hoort bij deze groep of dit blok?",
        [
            ("alkalimetalen", "A"),
            ("edelgassen", "D"),
            ("overgangselementen", "C"),
            ("halogenen", "B"),
        ],
        "De overgangselementen vormen het d-blok in het midden.",
        kolommen=["A", "B", "C", "D"],
    )),
    tabel(
        "Hoeveel elektronen passen er in dit subniveau?",
        [
            ("s", "2"),
            ("p", "6"),
            ("d", "10"),
            ("f", "14"),
        ],
        "1, 3, 5 en 7 orbitalen van telkens twee elektronen.",
        kolommen=["2", "6", "10", "14"],
    ),
    inv(
        "Geef de elektronenconfiguratie van natrium (11 elektronen) in exponentnotatie, zonder spaties. Schrijf de exponenten als gewone cijfers.",
        ["1s22s22p63s1", "1s² 2s² 2p⁶ 3s¹", "1s²2s²2p⁶3s¹"],
        "2 + 2 + 6 + 1 = 11.",
    ),
    inv(
        "Een atoom heeft de verkorte configuratie [Ne] 3s² 3p⁴. In welke groep staat het? Geef enkel het groepsnummer.",
        ["16"],
        "2 + 4 = 6 valentie-elektronen in het p-blok: groep 16, de zuurstofgroep.",
    ),
    inv(
        "Hoeveel elektronen heeft het ion Mg²⁺? Magnesium heeft atoomnummer 12.",
        ["10", "tien"],
        "Twee elektronen afgestaan: 12 − 2 = 10, de configuratie van neon.",
    ),
    koppel(
        "Koppel elk kwantumgetal aan wat het aangeeft.",
        [
            ("hoofdkwantumgetal n", "de schil of het hoofdniveau"),
            ("nevenkwantumgetal", "het subniveau s, p, d of f"),
            ("magnetisch kwantumgetal", "welk orbitaal van het subniveau"),
            ("spinkwantumgetal", "+½ of −½"),
        ],
        ["het aantal neutronen in de kern"],
        "Vier kwantumgetallen beschrijven één elektron volledig.",
    ),
    volgorde(
        "Zet deze subniveaus in de volgorde waarin ze gevuld worden.",
        ["3s", "3p", "4s", "3d", "4p"],
        "Volgens de diagonaalregel komt 4s vóór 3d.",
    ),
    tabel(
        "Wordt de atoomradius groter of kleiner?",
        [
            ("naar beneden in een groep", "Groter"),
            ("naar rechts in een periode", "Kleiner"),
            ("van Na naar Na⁺", "Kleiner"),
            ("van Cl naar Cl⁻", "Groter"),
        ],
        "Een negatief ion krijgt extra elektronen die elkaar afstoten.",
        kolommen=["Groter", "Kleiner"],
    ),
    mk(
        "Waarom wordt de atoomradius kleiner als je in een periode naar rechts gaat?",
        [
            "De kernlading stijgt bij hetzelfde hoofdniveau",
            "Er komt bij elk element een nieuwe schil bij",
            "De elektronen vallen een voor een naar de kern",
            "Er zitten naar rechts telkens minder protonen",
        ],
        0,
        "De kern trekt sterker aan de elektronen van dezelfde schil.",
    ),
    casus(
        "Een element heeft de configuratie [Ar] 4s² 3d¹⁰ 4p⁵.",
        [
            inv(
                "Hoeveel valentie-elektronen heeft het?",
                ["7", "zeven"],
                "4s² en 4p⁵: 2 + 5 = 7.",
            ),
            keuze(
                "Het staat in groep 17, bij de [[*halogenen|edelgassen|alkalimetalen]].",
                "Zeven valentie-elektronen.",
            ),
            mk(
                "Welk ion vormt dit element het liefst?",
                [
                    "Een ion met lading 1−",
                    "Een ion met lading 1+",
                    "Een ion met lading 7+",
                    "Het vormt nooit een ion",
                ],
                0,
                "Eén elektron opnemen geeft de configuratie van het volgende edelgas.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over elektronegatieve waarde en metaalkarakter?",
        [
            ("Fluor heeft de hoogste elektronegatieve waarde.", J),
            ("Het metaalkarakter is het sterkst linksonder.", J),
            ("Een metaal staat zijn elektronen makkelijk af.", J),
            ("Edelgassen hebben het sterkste metaalkarakter.", F),
        ],
        "Edelgassen zijn niet-metalen met een volle buitenste schil.",
    ),
    mk(
        "Waarom eindigt de configuratie van chroom op 3d⁵ 4s¹?",
        [
            "Een halfgevuld d-subniveau is stabieler",
            "Chroom heeft maar één elektron in 4s nodig",
            "Het 4s-subniveau kan maar één elektron bevatten",
            "Chroom volgt de diagonaalregel helemaal niet",
        ],
        0,
        "Vijf elektronen, elk alleen in een d-orbitaal, geven een stabiele toestand.",
    ),
    keuze(
        "Het uitsluitingsprincipe van [[*Pauli|Hund|Bohr]] zegt dat twee elektronen nooit alle vier hun kwantumgetallen gelijk hebben.",
        "Daarom hebben twee elektronen in één orbitaal een tegengestelde spin.",
    ),
    tabel(
        "In welk blok staat dit element?",
        [
            ("[Ne] 3s¹", "s"),
            ("[Ar] 4s² 3d⁶", "d"),
            ("[Ne] 3s² 3p⁵", "p"),
            ("[He] 2s²", "s"),
        ],
        "Het blok is het subniveau van het laatst toegevoegde elektron.",
        kolommen=["s", "p", "d"],
    ),
    sleep(
        "Een orbitaal is het gebied waar een elektron zich met grote [[kans]] bevindt. In één orbitaal passen [[twee]] elektronen, met een [[tegengestelde]] spin.",
        ["zekerheid", "acht", "gelijke"],
        "Het model van Schrödinger werkt met kansen, niet met vaste banen.",
    ),
    tabel(
        "Klopt dit over Na⁺?",
        [
            ("Het heeft tien elektronen.", J),
            ("Het heeft de configuratie van neon.", J),
            ("Het is kleiner dan het natriumatoom.", J),
            ("Het heeft elf elektronen.", F),
        ],
        "Natrium staat één elektron af.",
    ),
    tabel(
        "Welk oxidatiegetal verwacht je?",
        [
            ("een element uit groep 1", "+I"),
            ("een element uit groep 2", "+II"),
            ("een element uit groep 16, in een ion", "−II"),
            ("een element uit groep 17, in een ion", "−I"),
        ],
        "Zo bereikt het atoom de configuratie van een edelgas.",
        kolommen=["+I", "+II", "−I", "−II"],
    ),
    mk(
        "Waarom vult 4s zich vóór 3d?",
        [
            "4s heeft een iets lagere energie",
            "4s ligt altijd dichter bij de kern dan 3d",
            "Het 3d-subniveau bestaat pas vanaf periode 5",
            "Er passen meer elektronen in 4s dan in 3d",
        ],
        0,
        "De diagonaalregel volgt de energie van de subniveaus.",
    ),
    inv(
        "Hoeveel elektronen passen er in het tweede hoofdniveau (n = 2)?",
        ["8", "acht"],
        "2s heeft er 2 en 2p heeft er 6.",
    ),
    tabel(
        "Klopt dit over de groepen?",
        [
            ("Elementen in één groep hebben evenveel valentie-elektronen.", J),
            ("Helium heeft twee valentie-elektronen en een volle schil.", J),
            ("Zuurstof en zwavel staan in dezelfde groep.", J),
            ("Een periode is een kolom in het systeem.", F),
        ],
        "Een periode is een rij, een groep is een kolom.",
    ),
    mk(
        "Welk deeltje heeft dezelfde elektronenconfiguratie als argon?",
        ["K⁺", "Na⁺", "Ne", "Cl"],
        0,
        "Kalium staat één elektron af en houdt er 18 over, net als argon.",
    ),
    tabel(
        "Hoeveel orbitalen heeft dit subniveau?",
        [
            ("2s", "1"),
            ("3p", "3"),
            ("3d", "5"),
            ("4f", "7"),
        ],
        "Het aantal orbitalen hangt van het soort subniveau af, niet van de schil.",
        kolommen=["1", "3", "5", "7"],
    ),
    open_(
        "Leg uit waarom een negatief ion groter is dan het atoom waaruit het ontstaat.",
        "Bij een negatief ion komen er een of meer elektronen bij, terwijl het aantal protonen in de kern gelijk blijft. De elektronen stoten elkaar meer af en elk elektron wordt minder sterk door de kern aangetrokken. Daardoor neemt de elektronenwolk meer plaats in.",
    ),
]
