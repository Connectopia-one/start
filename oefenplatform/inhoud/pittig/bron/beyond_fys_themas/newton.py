"""De wetten van Newton — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Vier blokken met krachten -------------------------------------------------
BL = Prent("vier-blokken", "Vier blokken op een wrijvingsloze vloer, met de horizontale krachten erop", "vier blokken onder elkaar: P (4 kg) 30 N naar rechts en 10 N naar links; Q (2 kg) 15 N naar rechts en 15 N naar links; R (5 kg) 10 N naar rechts en 25 N naar links; S (5 kg) 20 N naar rechts en 5 N naar links")
BLOK = [("P", 4, 30, 10), ("Q", 2, 15, 15), ("R", 5, 10, 25), ("S", 5, 20, 5)]
for i, (k, m, re, li) in enumerate(BLOK):
    y = 110 + i * 130
    BL.lijn(250, y + 40, 750, y + 40, "#b9b9b9", 2)
    BL.rect(440, y - 20, 120, 60, "#e8d3a8", DONKER, 6, 2)
    BL.tekst(500, y + 17, f"{m} kg", 20, vet=True)
    BL.pijl(560, y + 10, 560 + re * 5, y + 10, ORANJE, 4)
    BL.tekst(560 + re * 5 + 12, y + 17, f"{re} N", 18, anker="start")
    BL.pijl(440, y + 10, 440 - li * 5, y + 10, BLAUW, 4)
    BL.tekst(440 - li * 5 - 12, y + 17, f"{li} N", 18, anker="end")
    BL.letter(110, y + 10, k)
ZB = {k: [Prent.zone(420, 110 + i * 130 - 30, 160, 80), Prent.rond(110, 110 + i * 130 + 10, 26)] for i, (k, *_r) in enumerate(BLOK)}

# Weegschaal in een lift ----------------------------------------------------
LW = Prent("lift-weegschaal", "Iemand staat op een weegschaal in een lift", "vier liften: A staat stil, B vertrekt en versnelt naar boven, C gaat met constante snelheid naar boven, D gaat naar boven maar remt af; bij elke lift een pijl voor de snelheid en een tekst")
TXT = {"A": ("staat stil", None), "B": ("versnelt", "omhoog"), "C": ("constante snelheid", "omhoog"), "D": ("remt af", "omhoog")}
for i, k in enumerate("ABCD"):
    x = 130 + i * 245
    LW.rect(x - 85, 120, 170, 330, "#f4f7fb", DONKER, 8, 3)
    LW.lijn(x, 60, x, 120, DONKER, 3)
    LW.cirkel(x, 230, 18, "#f3e3c8", DONKER, 2)
    LW.lijn(x, 248, x, 340, DONKER, 4)
    LW.lijn(x, 270, x - 30, 310, DONKER, 4)
    LW.lijn(x, 270, x + 30, 310, DONKER, 4)
    LW.lijn(x, 340, x - 22, 410, DONKER, 4)
    LW.lijn(x, 340, x + 22, 410, DONKER, 4)
    LW.rect(x - 45, 410, 90, 22, GRIJS, DONKER, 4, 2)
    tekst, zin = TXT[k]
    LW.tekst(x, 480, tekst, 18)
    if zin:
        LW.pijl(x + 70, 300, x + 70, 200, GROEN, 4)
        LW.tekst(x + 62, 330, "v", 18, vet=True)
    LW.letter(x, 540, k)
ZL = {k: [Prent.zone(130 + i * 245 - 85, 120, 170, 330), Prent.rond(130 + i * 245, 540, 26)] for i, k in enumerate("ABCD")}

VRAGEN = [
    klik(
        "Klik op het blok met de grootste versnelling.",
        BL.bestand, ZB["P"],
        "P: 20 N / 4 kg = 5,0 m/s². R en S: 15 N / 5 kg = 3,0 m/s². Q: 0.",
    ),
    klik(
        "Klik op het blok dat met een constante snelheid kan bewegen.",
        BL.bestand, ZB["Q"],
        "Alleen bij Q is de resulterende kracht nul.",
    ),
    met_prent(BL.bestand, tabel(
        "Hoe groot is de versnelling van dit blok?",
        [
            ("P", "5,0 m/s²"),
            ("Q", "0"),
            ("R", "3,0 m/s²"),
        ],
        "a = F_res / m.",
        kolommen=["0", "3,0 m/s²", "5,0 m/s²"],
    )),
    met_prent(BL.bestand, keuze(
        "Blok R versnelt naar [[*links|rechts]], blok S naar [[links|*rechts]].",
        "De versnelling wijst in de zin van de resulterende kracht.",
    )),
    met_prent(BL.bestand, mk(
        "Blok Q schuift al met 2 m/s naar rechts. Wat doet het verder?",
        [
            "Het gaat met 2 m/s verder",
            "Het remt langzaam af tot het stilstaat",
            "Het versnelt langzaam verder naar rechts",
            "Het keert om en gaat weer naar links",
        ],
        0,
        "Eerste wet: zonder resulterende kracht verandert de bewegingstoestand niet.",
    )),
    klik(
        "Klik op de lift waarin de weegschaal het meest aanwijst.",
        LW.bestand, ZL["B"],
        "De vloer moet je dragen én naar boven versnellen, dus F_N > m · g.",
    ),
    klik(
        "Klik op de lift waarin de weegschaal het minst aanwijst.",
        LW.bestand, ZL["D"],
        "Bij afremmen naar boven wijst de versnelling naar beneden, dus F_N < m · g.",
    ),
    met_prent(LW.bestand, tabel(
        "Wijst de weegschaal meer, minder of evenveel aan als op de grond?",
        [
            ("A", "Evenveel"),
            ("B", "Meer"),
            ("C", "Evenveel"),
            ("D", "Minder"),
        ],
        "Alleen de versnelling telt, niet de snelheid.",
        kolommen=["Meer", "Evenveel", "Minder"],
    )),
    met_prent(LW.bestand, mk(
        "De persoon in lift B heeft een massa van 60 kg en de lift versnelt met 2,0 m/s². Hoe groot is de normaalkracht? Neem g = 9,81 N/kg.",
        ["ongeveer 709 N", "ongeveer 589 N", "ongeveer 120 N", "ongeveer 469 N"],
        0,
        "F_N − m · g = m · a, dus F_N = 60 · (9,81 + 2,0) ≈ 709 N.",
    )),
    met_prent(LW.bestand, keuze(
        "In lift C is de normaalkracht [[*even groot als|groter dan|kleiner dan]] de zwaartekracht.",
        "Constante snelheid: geen resulterende kracht.",
    )),
    inv(
        "Je duwt een kist van 8,0 kg met 40 N. De wrijving is 8,0 N. Hoe groot is de versnelling, in m/s²?",
        ["4", "4,0", "4 m/s²", "4,0 m/s²"],
        "a = (40 − 8,0) / 8,0 = 4,0 m/s².",
    ),
    inv(
        "Welke resulterende kracht brengt een wagen van 1200 kg in 8,0 s van 0 naar 20 m/s, in N?",
        ["3000", "3000 N", "3,0 kN", "3 kN"],
        "a = 20 / 8,0 = 2,5 m/s², dus F = 1200 · 2,5 = 3000 N.",
    ),
    inv(
        "Een wagen van 1500 kg remt in 4,0 s van 20 m/s tot stilstand. Hoe groot is de remkracht, in N?",
        ["7500", "7500 N", "7,5 kN"],
        "a = 20 / 4,0 = 5,0 m/s², F = 1500 · 5,0 = 7500 N.",
    ),
    inv(
        "Op een lichaam werkt een resulterende kracht van 6,0 N en het versnelt met 1,5 m/s². Wat is zijn massa, in kg?",
        ["4", "4,0", "4 kg", "4,0 kg"],
        "m = F / a = 6,0 / 1,5 = 4,0 kg.",
    ),
    mk(
        "Een lift van 800 kg versnelt naar boven met 1,5 m/s². Hoe groot is de kracht in de kabel? Neem g = 9,81 N/kg.",
        ["ongeveer 9,0 kN", "ongeveer 7,8 kN", "ongeveer 1,2 kN", "ongeveer 6,6 kN"],
        0,
        "F_kabel = m · (g + a) = 800 · 11,31 ≈ 9,0 · 10³ N.",
    ),
    tabel(
        "Welke wet van Newton herken je het best?",
        [
            ("een gordel houdt je tegen bij een botsing", "Eerste"),
            ("een volle winkelkar komt trager op gang", "Tweede"),
            ("een geweer slaat terug bij het schieten", "Derde"),
            ("een raket vliegt in de lege ruimte", "Derde"),
        ],
        "Traagheid, F = m · a, en actie en reactie.",
        kolommen=["Eerste", "Tweede", "Derde"],
    ),
    koppel(
        "Koppel elke actie aan haar reactie.",
        [
            ("de aarde trekt aan de maan", "de maan trekt aan de aarde"),
            ("je voet duwt de grond naar achter", "de grond duwt je voet naar voren"),
            ("een raket duwt gas naar achter", "het gas duwt de raket naar voren"),
            ("een hamer slaat op een nagel", "de nagel duwt terug op de hamer"),
        ],
        ["de normaalkracht van de tafel op het boek"],
        "Actie en reactie werken altijd op twee verschillende lichamen.",
    ),
    mk(
        "Een boek ligt stil op een tafel. Welke twee krachten op het boek heffen elkaar op?",
        [
            "De zwaartekracht en de normaalkracht",
            "De zwaartekracht en de kracht van het boek op de aarde",
            "De normaalkracht en de kracht van het boek op de tafel",
            "Er werkt geen enkele kracht op het boek",
        ],
        0,
        "Ze werken op hetzelfde lichaam en zijn dus géén actie-reactiepaar.",
    ),
    casus(
        "Een vrachtwagen van 10 000 kg en een auto van 1000 kg botsen. Tijdens de botsing werkt er op de auto een kracht van 50 000 N.",
        [
            keuze(
                "De kracht op de vrachtwagen is [[*even groot|tien keer zo groot|tien keer zo klein]].",
                "Derde wet: actie en reactie zijn even groot.",
            ),
            inv(
                "Hoe groot is de versnelling van de auto, in m/s²?",
                ["50", "50 m/s²"],
                "a = 50 000 / 1000 = 50 m/s².",
            ),
            mk(
                "Hoe groot is de versnelling van de vrachtwagen?",
                ["5,0 m/s²", "50 m/s²", "500 m/s²", "0,50 m/s²"],
                0,
                "a = 50 000 / 10 000 = 5,0 m/s²: dezelfde kracht, tien keer meer massa.",
            ),
        ],
    ),
    mk(
        "Een bal wordt recht omhoog gegooid. Welke resulterende kracht werkt erop in het hoogste punt, zonder luchtweerstand?",
        [
            "De zwaartekracht, naar beneden",
            "Geen, want de bal staat even stil",
            "Een kracht naar boven, van de worp",
            "De zwaartekracht plus de worpkracht",
        ],
        0,
        "Na het loslaten werkt alleen nog de zwaartekracht, ook als v even nul is.",
    ),
    mk(
        "Een parachutist met uitrusting weegt 900 N en valt met constante snelheid. Hoe groot is de luchtweerstand?",
        ["900 N", "0 N", "meer dan 900 N", "minder dan 900 N"],
        0,
        "Constante snelheid: de krachten heffen elkaar op.",
    ),
    mk(
        "Je duwt met 30 N tegen een kast, maar ze beweegt niet. Hoe groot is de wrijvingskracht op de kast?",
        ["30 N", "0 N", "meer dan 30 N", "dat kan je niet weten"],
        0,
        "De kast blijft in rust, dus is de resulterende kracht nul.",
    ),
    keuze(
        "Bij dezelfde resulterende kracht geeft een twee keer zo grote massa een [[*twee keer zo kleine|twee keer zo grote|even grote]] versnelling.",
        "a = F / m.",
    ),
    tabel(
        "Klopt deze uitspraak over de wetten van Newton?",
        [
            ("Om met constante snelheid te blijven bewegen, is een resulterende kracht nodig.", F),
            ("Een astronaut in het ruimtestation voelt geen zwaartekracht meer.", F),
            ("De versnelling wijst in de zin van de resulterende kracht.", J),
            ("Bij dezelfde kracht versnelt een lichtere wagen harder.", J),
        ],
        "Kracht verandert beweging; ze is niet nodig om beweging te bewaren.",
    ),
    sorteer(
        "Is de resulterende kracht op het lichaam nul of niet?",
        ["Nul", "Niet nul"],
        [
            ("een auto rijdt met constant 90 km/h rechtdoor", "Nul"),
            ("een boek ligt stil op de kast", "Nul"),
            ("een appel valt van de boom", "Niet nul"),
            ("een lift remt af", "Niet nul"),
            ("een parachutist valt met constante snelheid", "Nul"),
        ],
        "Kijk alleen of de snelheid verandert.",
    ),
    volgorde(
        "Zet de stappen om de versnelling van een lichaam te vinden in volgorde.",
        [
            "Alle krachten op het lichaam tekenen",
            "De resulterende kracht bepalen",
            "a = F_res / m berekenen",
            "De zin van a gelijkstellen aan die van F_res",
        ],
        "Eerst de som van de krachten, dan pas de tweede wet.",
    ),
    sleep(
        "De eerste wet heet de [[traagheidswet]]. De tweede wet zegt F = m · [[a]]. Actie en reactie werken op [[twee verschillende]] lichamen.",
        ["hetzelfde", "v"],
        "Drie wetten, drie ideeën.",
    ),
    open_(
        "Leg met de tweede wet van Newton uit waarom een airbag je hoofd beschermt bij een botsing.",
        "Je hoofd moet bij de botsing van dezelfde snelheid tot stilstand komen. Met de airbag duurt dat afremmen langer, dus is de versnelling (de snelheidsverandering per seconde) kleiner. Volgens F = m · a is dan ook de kracht op je hoofd kleiner.",
    ),
]
