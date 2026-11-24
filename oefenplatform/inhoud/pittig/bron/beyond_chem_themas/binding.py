"""Atoombinding en lewisstructuren — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Overlapping van orbitalen ------------------------------------------------
OV = Prent("overlapping-orbitalen", "Drie manieren waarop orbitalen overlappen", "drie tekeningen met twee kernen en hun orbitalen; letters P, Q en R")
LB = "#cfe5f3"
OR = "#f7d9b5"
# P: twee s-orbitalen kop aan kop
OV.cirkel(130, 200, 60, LB, DONKER, 2)
OV.cirkel(220, 200, 60, OR, DONKER, 2)
OV.cirkel(130, 200, 5, DONKER, DONKER, 1)
OV.cirkel(220, 200, 5, DONKER, DONKER, 1)
OV.lijn(40, 200, 310, 200, GRIJS, 1, stippel=True)
OV.letter(175, 330, "P")
# Q: twee p-orbitalen naast elkaar (zijdelings)
for x, kl in ((440, LB), (530, OR)):
    OV.ellips(x, 150, 30, 55, kl, DONKER, 2)
    OV.ellips(x, 250, 30, 55, kl, DONKER, 2)
    OV.cirkel(x, 200, 5, DONKER, DONKER, 1)
OV.lijn(380, 200, 590, 200, GRIJS, 1, stippel=True)
OV.letter(485, 330, "Q")
# R: twee p-orbitalen kop aan kop
OV.ellips(690, 200, 30, 20, LB, DONKER, 2)
OV.ellips(770, 200, 50, 26, LB, DONKER, 2)
OV.ellips(830, 200, 50, 26, OR, DONKER, 2)
OV.ellips(910, 200, 30, 20, OR, DONKER, 2)
OV.cirkel(720, 200, 5, DONKER, DONKER, 1)
OV.cirkel(880, 200, 5, DONKER, DONKER, 1)
OV.lijn(630, 200, 970, 200, GRIJS, 1, stippel=True)
OV.letter(820, 330, "R")
OV.tekst(500, 470, "De stippellijn is de lijn tussen de twee kernen (de bindingsas).", 18)
ZOV = {"P": [Prent.zone(60, 130, 230, 140), Prent.rond(175, 330, 22)],
       "Q": [Prent.zone(400, 90, 170, 220), Prent.rond(485, 330, 22)],
       "R": [Prent.zone(640, 160, 350, 80), Prent.rond(820, 330, 22)]}

# Lewisstructuren -----------------------------------------------------------
LW = Prent("lewis-hcn-water", "Lewisstructuren van waterstofcyanide en water", "links H, C en N verbonden met een enkele en een drievoudige binding, rechts een watermolecule; letters A tot E")


def _paar(p, x, y, verticaal=False):
    if verticaal:
        p.cirkel(x, y - 8, 4, DONKER, DONKER, 1)
        p.cirkel(x, y + 8, 4, DONKER, DONKER, 1)
    else:
        p.cirkel(x - 8, y, 4, DONKER, DONKER, 1)
        p.cirkel(x + 8, y, 4, DONKER, DONKER, 1)


# HCN
LW.tekst(80, 268, "H", 34, vet=True)
LW.lijn(105, 256, 175, 256, DONKER, 3)
LW.tekst(200, 268, "C", 34, vet=True)
for dy in (-10, 0, 10):
    LW.lijn(225, 256 + dy, 305, 256 + dy, DONKER, 3)
LW.tekst(330, 268, "N", 34, vet=True)
_paar(LW, 362, 256, True)
# Water
LW.tekst(720, 268, "O", 34, vet=True)
LW.lijn(700, 268, 640, 330, DONKER, 3)
LW.tekst(625, 360, "H", 34, vet=True)
LW.lijn(740, 268, 800, 330, DONKER, 3)
LW.tekst(815, 360, "H", 34, vet=True)
_paar(LW, 720, 212)
_paar(LW, 690, 240, True)
LBL = {"A": (140, 170), "B": (265, 170), "C": (400, 170), "D": (720, 150), "E": (640, 430)}
for k, (x, y) in LBL.items():
    LW.letter(x, y, k)
LW.lijn(140, 192, 140, 250, GRIJS, 1)
LW.lijn(265, 192, 265, 240, GRIJS, 1)
LW.lijn(400, 192, 368, 245, GRIJS, 1)
LW.lijn(720, 172, 720, 204, GRIJS, 1)
LW.lijn(640, 408, 668, 302, GRIJS, 1)
ZLW = {"A": [Prent.zone(105, 236, 70, 40), Prent.rond(*LBL["A"], 22)],
       "B": [Prent.zone(225, 236, 80, 40), Prent.rond(*LBL["B"], 22)],
       "C": [Prent.zone(350, 236, 30, 40), Prent.rond(*LBL["C"], 22)],
       "D": [Prent.zone(695, 200, 50, 25), Prent.rond(*LBL["D"], 22)],
       "E": [Prent.zone(635, 265, 70, 70), Prent.rond(*LBL["E"], 22)]}

VRAGEN = [
    klik(
        "Klik op de overlapping waardoor de atomen niet meer vrij kunnen draaien.",
        OV.bestand, ZOV["Q"],
        "Zijdelingse overlapping geeft een pi-binding. Bij draaien zou die overlapping verdwijnen.",
    ),
    met_prent(OV.bestand, tabel(
        "Welke binding ontstaat bij deze overlapping?",
        [
            ("P", "sigma"),
            ("Q", "pi"),
            ("R", "sigma"),
        ],
        "P en R overlappen op de bindingsas: coaxiaal. Q overlapt naast de as.",
        kolommen=["sigma", "pi"],
    )),
    met_prent(OV.bestand, tabel(
        "Vergelijk de drie overlappingen. Klopt dit?",
        [
            ("P en R zijn radiaal symmetrisch rond de as.", J),
            ("Q overlapt minder sterk dan R.", J),
            ("Q kan alleen bestaan als er al een binding zoals R ligt.", J),
            ("In P overlappen twee p-orbitalen.", F),
        ],
        "In P overlappen twee bolvormige s-orbitalen. Een pi-binding komt altijd bovenop een sigma-binding.",
    )),
    klik(
        "Klik op het deel van de lewisstructuur met één sigma- en twee pi-bindingen.",
        LW.bestand, ZLW["B"],
        "Een drievoudige binding: één sigma en twee pi.",
    ),
    klik(
        "Klik op een vrij elektronenpaar van het atoom dat er twee heeft.",
        LW.bestand, ZLW["D"],
        "Zuurstof in water heeft twee vrije paren, stikstof in HCN maar één.",
    ),
    met_prent(LW.bestand, tabel(
        "Wat stelt dit deel van de lewisstructuren voor?",
        [
            ("A", "Bindend paar"),
            ("C", "Vrij paar"),
            ("D", "Vrij paar"),
            ("E", "Bindend paar"),
        ],
        "Streepjes tussen atomen zijn bindende paren, puntjes bij één atoom zijn vrije paren.",
        kolommen=["Bindend paar", "Vrij paar"],
    )),
    met_prent(LW.bestand, inv(
        "Hoeveel sigma-bindingen telt waterstofcyanide (de linkse molecule) in totaal?",
        ["2", "twee"],
        "Eén in H–C en één in C≡N.",
    )),
    tabel(
        "Hoeveel sigma- en pi-bindingen telt deze molecule?",
        [
            ("CH₄", "4 sigma, 0 pi"),
            ("C₂H₄", "5 sigma, 1 pi"),
            ("C₂H₂", "3 sigma, 2 pi"),
            ("N₂", "1 sigma, 2 pi"),
        ],
        "Tussen twee atomen ligt altijd precies één sigma-binding.",
        kolommen=["4 sigma, 0 pi", "5 sigma, 1 pi", "3 sigma, 2 pi", "1 sigma, 2 pi"],
    ),
    inv(
        "Hoeveel pi-bindingen telt koolstofdioxide, O=C=O?",
        ["2", "twee"],
        "Twee dubbele bindingen, elk met één pi-binding.",
    ),
    tabel(
        "Wat gebeurt er als je van C–C naar C=C naar C≡C gaat?",
        [
            ("de bindingslengte", "Neemt af"),
            ("de totale bindingssterkte", "Neemt toe"),
            ("de vrije draaibaarheid", "Neemt af"),
        ],
        "Elke pi-binding trekt de atomen dichter bij elkaar en maakt draaien onmogelijk.",
        kolommen=["Neemt toe", "Neemt af"],
    ),
    mk(
        "Waarom is een pi-binding zwakker dan een sigma-binding?",
        [
            "De orbitalen overlappen minder, naast de as",
            "Er zit maar één elektron in een pi-binding",
            "Een pi-binding ligt verder van de kern af dan een ion",
            "Een pi-binding wordt door vrije paren afgestoten",
        ],
        0,
        "Zijdelingse overlapping is kleiner dan coaxiale overlapping.",
    ),
    keuze(
        "Bij een additiereactie aan een alkeen breekt de [[*pi-binding|sigma-binding|waterstofbrug]] open.",
        "De sigma-binding tussen de twee koolstofatomen blijft bestaan.",
    ),
    tabel(
        "Hoeveel vrije elektronenparen heeft het centrale atoom?",
        [
            ("O in H₂O", "2"),
            ("N in NH₃", "1"),
            ("C in CH₄", "0"),
            ("N in NH₄⁺", "0"),
        ],
        "In NH₄⁺ is het vrije paar van stikstof een bindend paar geworden.",
        kolommen=["0", "1", "2"],
    ),
    casus(
        "Ammoniak, NH₃, neemt een H⁺-ion op. Zo ontstaat het ammoniumion NH₄⁺.",
        [
            mk(
                "Welke soort binding ontstaat met het H⁺-ion?",
                [
                    "Een donor-acceptorbinding",
                    "Een ionbinding tussen N en H",
                    "Een metaalbinding",
                    "Een pi-binding",
                ],
                0,
                "Stikstof levert het hele elektronenpaar, H⁺ brengt geen elektronen mee.",
            ),
            inv(
                "Bereken de formele lading van stikstof in NH₄⁺. Gebruik + of − voor het getal.",
                ["+1", "1+", "+"],
                "5 valentie-elektronen − 0 vrije elektronen − 4 bindingen = +1.",
            ),
            tabel(
                "Hoe zie je dat terug in NH₄⁺?",
                [
                    ("De vier N–H-bindingen zijn na afloop gelijk.", J),
                    ("Stikstof heeft geen vrij elektronenpaar meer.", J),
                    ("Het ion heeft in totaal tien valentie-elektronen.", F),
                ],
                "5 + 4 − 1 = 8 valentie-elektronen.",
            ),
        ],
    ),
    tabel(
        "Welke binding hoort bij deze stof?",
        [
            ("natriumchloride", "Ionbinding"),
            ("koper", "Metaalbinding"),
            ("methaan", "Atoombinding"),
            ("magnesiumoxide", "Ionbinding"),
        ],
        "Metaal + niet-metaal geeft een ionbinding, niet-metalen onderling een atoombinding.",
        kolommen=["Atoombinding", "Ionbinding", "Metaalbinding"],
    ),
    inv(
        "Bereken de formele lading van zuurstof in H₃O⁺. Gebruik + of − voor het getal.",
        ["+1", "1+", "+"],
        "6 valentie-elektronen − 2 vrije elektronen − 3 bindingen = +1.",
    ),
    inv(
        "Hoeveel valentie-elektronen moet je in totaal verdelen bij de lewisstructuur van het carbonaation CO₃²⁻?",
        ["24", "vierentwintig"],
        "4 + 3 × 6 = 22, plus 2 voor de lading 2− = 24.",
    ),
    mk(
        "Waarom geleidt koper stroom en zout in vaste vorm niet?",
        [
            "Koperelektronen bewegen vrij, de ionen in vast zout niet",
            "Koper bevat ionen en zout bevat helemaal geen geladen deeltjes",
            "Zout heeft een metaalbinding die te sterk is om te geleiden",
            "In koper zitten de elektronen vast tussen telkens twee atomen",
        ],
        0,
        "De elektronenzee van een metaal kan bewegen; ionen in een rooster niet.",
    ),
    sorteer(
        "Bij welke soort binding hoort deze uitspraak?",
        ["Sigma-binding", "Pi-binding"],
        [
            ("ontstaat door coaxiale overlapping", "Sigma-binding"),
            ("laat vrij draaien toe", "Sigma-binding"),
            ("zit in elke enkelvoudige binding", "Sigma-binding"),
            ("ontstaat door zijdelingse overlapping", "Pi-binding"),
            ("is de reactieve plek van een alkeen", "Pi-binding"),
            ("kan er twee keer zijn tussen dezelfde atomen", "Pi-binding"),
        ],
        "Er is altijd maar één sigma-binding tussen twee atomen, wel tot twee pi-bindingen.",
    ),
    tabel(
        "Volgt dit atoom de octetregel in de lewisstructuur?",
        [
            ("O in H₂O (2 bindingen, 2 vrije paren)", J),
            ("C in CO₂ (2 dubbele bindingen)", J),
            ("Cl in Cl₂ (1 binding, 3 vrije paren)", J),
            ("C met 3 enkelvoudige bindingen en geen vrij paar", F),
        ],
        "Tel bindende én vrije elektronen: 3 bindingen zonder vrij paar is maar 6.",
    ),
    mk(
        "Benzeen is stabieler dan je met drie losse dubbele bindingen zou verwachten. Waarom?",
        [
            "De pi-elektronen zijn over de hele ring verspreid",
            "Benzeen heeft helemaal geen pi-bindingen in de ring",
            "De ring bevat zes sigma-bindingen tussen C en H",
            "Elk koolstofatoom van de ring heeft een vrij paar",
        ],
        0,
        "Zes p-orbitalen overlappen rondom en verdelen de elektronen over de ring.",
    ),
    sleep(
        "Bij een [[normale atoombinding]] levert elk atoom één elektron. Bij een [[donor-acceptorbinding]] levert één atoom het hele paar. Bij een [[ionbinding]] gaan elektronen volledig over.",
        ["metaalbinding", "pi-binding"],
        "Bij een metaalbinding bewegen de elektronen vrij tussen positieve ionen.",
    ),
    tabel(
        "Klopt dit over de formele lading?",
        [
            ("De som van de formele ladingen is de lading van het deeltje.", J),
            ("Bij de formele lading verdeel je bindende elektronen eerlijk.", J),
            ("De formele lading is altijd gelijk aan het oxidatiegetal.", F),
        ],
        "Bij het oxidatiegetal krijgt het meest elektronegatieve atoom het hele paar.",
    ),
    volgorde(
        "Zet de stappen om een lewisstructuur te tekenen in de goede volgorde.",
        [
            "Tel alle valentie-elektronen, met de lading erbij",
            "Verbind de atomen met enkelvoudige bindingen",
            "Verdeel de overige elektronen als vrije paren",
            "Maak dubbele bindingen waar een octet ontbreekt",
            "Bereken de formele ladingen ter controle",
        ],
        "Eerst tellen, dan het skelet, dan aanvullen tot elk atoom een octet heeft.",
    ),
    koppel(
        "Koppel elk deeltje aan zijn lewisstructuur in woorden.",
        [
            ("N₂", "drievoudige binding, één vrij paar per atoom"),
            ("O₂", "dubbele binding, twee vrije paren per atoom"),
            ("F₂", "enkelvoudige binding, drie vrije paren per atoom"),
            ("HF", "enkelvoudige binding, drie vrije paren op één atoom"),
        ],
        ["drievoudige binding, geen vrije paren"],
        "Elk atoom komt zo aan acht elektronen, waterstof aan twee.",
    ),
    mk(
        "Waarom zijn de pi-elektronen van een alkeen een gemakkelijk doelwit voor een aanval?",
        [
            "Ze liggen boven en onder de as",
            "Ze liggen precies tussen de twee kernen in",
            "Ze zijn positief geladen en trekken alles aan",
            "Ze zitten in een s-orbitaal dicht bij de kern",
        ],
        0,
        "Wat minder sterk gebonden is en meer naar buiten ligt, reageert makkelijker.",
    ),
    inv(
        "Hoeveel vrije elektronenparen teken je in totaal in de lewisstructuur van koolstofdioxide, O=C=O?",
        ["4", "vier"],
        "Elk zuurstofatoom heeft twee vrije paren, koolstof geen.",
    ),
    open_(
        "Leg uit waarom een molecule wel kan draaien rond een C–C-binding maar niet rond een C=C-binding.",
        "Een enkelvoudige binding is een sigma-binding: die overlapt langs de bindingsas en is radiaal symmetrisch, dus de overlapping blijft gelijk als je draait. In een dubbele binding zit er ook een pi-binding: die overlapt zijdelings boven en onder de as. Draaien zou die overlapping verbreken, dus de groepen zitten vast.",
    ),
]
