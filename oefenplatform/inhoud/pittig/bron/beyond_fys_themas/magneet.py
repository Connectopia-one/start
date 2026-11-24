"""Magneten en het magnetisch veld — pittig (🔭 Beyond doorstroom, fysica)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Staafmagneet met veldlijnen (zonder pijlen) -----------------------------------
SM = Prent("staafmagneet-veld", "Veldlijnen rond een staafmagneet", "een liggende staafmagneet met de noordpool links en de zuidpool rechts, veldlijnen zonder pijlen, drie punten A (ver boven het midden), B (vlak links naast de noordpool) en C (rechts van de zuidpool)")
PN, PZ = (395, 340), (605, 340)


def _b(x, y):
    bx = by = 0.0
    for (px, py), s in ((PN, 1), (PZ, -1)):
        ddx, ddy = x - px, y - py
        r3 = (ddx * ddx + ddy * ddy) ** 1.5
        bx += s * ddx / r3
        by += s * ddy / r3
    return bx, by


def _in_magneet(x, y):
    return 355 < x < 645 and 305 < y < 375


def _lijn(x, y, zin):
    pts = [(x, y)]
    for _ in range(3000):
        bx, by = _b(x, y)
        n = math.hypot(bx, by)
        x, y = x + zin * 2.5 * bx / n, y + zin * 2.5 * by / n
        pts.append((x, y))
        if _in_magneet(x, y) or not (15 < x < 985 and 55 < y < 630):
            break
    return pts, _in_magneet(x, y)


for i in range(18):
    hoek = 2 * math.pi * (i + 0.5) / 18
    for pool, zin in ((PN, 1), (PZ, -1)):
        x, y = pool[0] + 52 * math.cos(hoek), pool[1] + 52 * math.sin(hoek)
        if _in_magneet(x, y):
            continue
        pts, binnen = _lijn(x, y, zin)
        if zin == -1 and binnen:
            continue
        SM.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", GRIJS, 2)
SM.rect(360, 310, 140, 60, ROOD, DONKER, 4, 2)
SM.rect(500, 310, 140, 60, BLAUW, DONKER, 4, 2)
SM.tekst(430, 350, "N", 28, kleur="#ffffff", vet=True)
SM.tekst(570, 350, "Z", 28, kleur="#ffffff", vet=True)
SPUNT = {"A": (500, 130), "B": (320, 340), "C": (760, 340)}
for k, (x, y) in SPUNT.items():
    SM.cirkel(x, y, 7, DONKER, DONKER, 1)
    SM.letter(x, y - 36, k)
ZS = {k: [Prent.rond(x, y, 26), Prent.rond(x, y - 36, 22)] for k, (x, y) in SPUNT.items()}

# Rechte draad en spoel -------------------------------------------------------------
DS = Prent("draad-en-spoel", "Een rechte draad met de stroom naar je toe, en een spoel", "links een draad loodrecht op het blad met de stroom uit het blad naar je toe, met vier punten P (boven), Q (rechts), R (onder) en S (links); rechts een spoel met de stroom aan de voorkant naar beneden en de uiteinden X (links) en Y (rechts)")
DS.svg('<circle cx="230" cy="330" r="110" fill="none" stroke="#9a9a9a" stroke-width="2" stroke-dasharray="7 6"/>')
DS.cirkel(230, 330, 26, "#ffffff", DONKER, 3)
DS.cirkel(230, 330, 7, DONKER, DONKER, 1)
DS.tekst(230, 500, "stroom naar je toe", 18)
DPUNT = {"P": (230, 220), "Q": (340, 330), "R": (230, 440), "S": (120, 330)}
LPUNT = {"P": (230, 178), "Q": (382, 330), "R": (230, 482 - 8), "S": (78, 330)}
LPUNT["R"] = (270, 455)
for k, (x, y) in DPUNT.items():
    DS.cirkel(x, y, 7, DONKER, DONKER, 1)
    DS.letter(*LPUNT[k], k)
ZDR = {k: [Prent.rond(*DPUNT[k], 26), Prent.rond(*LPUNT[k], 22)] for k in DPUNT}
# spoel
for x in range(580, 861, 40):
    DS.ellips(x, 330, 22, 90, "none", "#b5b5b5", 2)
    DS.pad(f"M {x} 240 A 22 90 0 0 1 {x} 420", "none", DONKER, 3)
for x in (620, 740, 860):
    DS.pijl(x + 22, 312, x + 22, 350, ROOD, 3)
DS.lijn(580, 420, 580, 520, DONKER, 3)
DS.lijn(860, 240, 860, 160, DONKER, 3)
DS.tekst(720, 560, "stroom aan de voorkant naar beneden", 18)
DS.letter(520, 330, "X")
DS.letter(930, 330, "Y")
ZX = [Prent.rond(520, 330, 30)]
ZY = [Prent.rond(930, 330, 30)]

VRAGEN = [
    klik(
        "Klik op het punt waar het magnetisch veld het sterkst is.",
        SM.bestand, ZS["B"],
        "Vlak bij een pool liggen de veldlijnen het dichtst bij elkaar.",
    ),
    klik(
        "Klik op het punt waar de noordpool van een kompasnaald naar rechts wijst.",
        SM.bestand, ZS["A"],
        "Buiten de magneet lopen de veldlijnen van N naar Z; boven het midden is dat naar rechts.",
    ),
    met_prent(SM.bestand, tabel(
        "Naar welke kant wijst de noordpool van een kompasnaald in dit punt?",
        [
            ("A", "Naar rechts"),
            ("B", "Naar links"),
            ("C", "Naar links"),
        ],
        "De naald volgt de veldlijn: weg van N, naar Z toe.",
        kolommen=["Naar links", "Naar rechts"],
    )),
    met_prent(SM.bestand, mk(
        "Je breekt de magneet precies in het midden. Wat zit er aan de breuk van het linkse stuk?",
        ["Een zuidpool", "Een noordpool", "Geen pool", "Een halve pool"],
        0,
        "Elk stuk wordt een volledige magneet; het linkse stuk heeft links N, dus rechts Z.",
    )),
    met_prent(SM.bestand, keuze(
        "Binnen in de magneet lopen de veldlijnen van [[*Z naar N|N naar Z]].",
        "Magnetische veldlijnen zijn gesloten kringen.",
    )),
    met_prent(SM.bestand, mk(
        "Je legt een tweede staafmagneet rechts naast deze, met zijn noordpool naar de Z toe. Wat gebeurt er?",
        [
            "Ze trekken elkaar aan",
            "Ze stoten elkaar af",
            "Er gebeurt niets, er is geen contact",
            "De tweede magneet draait zich om",
        ],
        0,
        "Ongelijksoortige polen trekken elkaar aan.",
    )),
    klik(
        "Klik op het punt waar de noordpool van een kompasnaald naar links wijst.",
        DS.bestand, ZDR["P"],
        "Duim naar je toe: de vingers krommen tegen de wijzers van de klok in. Bovenaan is dat naar links.",
    ),
    met_prent(DS.bestand, mk(
        "Je keert de stroom in de draad om. Wat doen de kompasnaalden rond de draad?",
        [
            "Ze draaien allemaal een halve toer",
            "Ze blijven precies zoals ze stonden",
            "Ze gaan allemaal naar de draad wijzen",
            "Ze gaan allemaal naar het noorden wijzen",
        ],
        0,
        "De cirkels blijven, maar de zin van de veldlijnen keert om.",
    )),
    klik(
        "Klik op het uiteinde van de spoel dat de noordpool is.",
        DS.bestand, ZY,
        "Vingers met de stroom mee rond de spoel: de duim wijst naar rechts, naar Y.",
    ),
    met_prent(DS.bestand, tabel(
        "Je brengt een staafmagneet bij de spoel. Trekken ze elkaar aan of stoten ze af?",
        [
            ("noordpool van de magneet bij X", "Aantrekken"),
            ("zuidpool van de magneet bij X", "Afstoten"),
            ("noordpool van de magneet bij Y", "Afstoten"),
        ],
        "X is de zuidpool van de spoel, Y de noordpool.",
        kolommen=["Aantrekken", "Afstoten"],
    )),
    met_prent(DS.bestand, keuze(
        "Schuif je een ijzeren kern in de spoel, dan wordt het veld [[*veel sterker|zwakker|niet anders]].",
        "De weissgebieden in het ijzer richten zich mee en versterken het veld.",
    )),
    inv(
        "Door een lange rechte draad loopt 10 A. Hoe groot is B op 2,0 cm van de draad, in mT? Neem μ₀ = 4π · 10⁻⁷ T·m/A.",
        ["0,1", "0,10", "0,1 mT", "0,10 mT", "0.1"],
        "B = μ₀ · I / (2π · r) = 2 · 10⁻⁷ · 10 / 0,020 = 1,0 · 10⁻⁴ T = 0,10 mT.",
    ),
    mk(
        "Rond een draad meet je B. Je halveert de stroom en gaat twee keer zo ver staan. Hoe groot wordt B?",
        ["B / 4", "B / 2", "B", "4 · B"],
        0,
        "B ~ I / r: de helft van de stroom en twee keer de afstand geeft een factor ½ · ½.",
    ),
    mk(
        "Op welke afstand van een draad met 20 A is B = 2,0 · 10⁻⁴ T? Neem μ₀ = 4π · 10⁻⁷ T·m/A.",
        ["2,0 cm", "20 cm", "0,20 cm", "4,0 cm"],
        0,
        "r = μ₀ · I / (2π · B) = 2 · 10⁻⁷ · 20 / 2,0 · 10⁻⁴ = 0,020 m.",
    ),
    inv(
        "Een spoel van 25 cm lang heeft 500 windingen en voert 2,0 A. Hoe groot is B binnenin, in mT? Neem μ₀ = 4π · 10⁻⁷ T·m/A en rond af op één decimaal.",
        ["5", "5,0", "5 mT", "5,0 mT", "5.0"],
        "B = μ₀ · N · I / ℓ = 4π · 10⁻⁷ · 500 · 2,0 / 0,25 ≈ 5,0 · 10⁻³ T.",
    ),
    inv(
        "Een spoel van 20 cm met 400 windingen moet binnenin B = 2,5 mT geven. Hoeveel stroom is er nodig, in ampère? Neem μ₀ = 4π · 10⁻⁷ T·m/A en rond af op één decimaal.",
        ["1", "1,0", "1 A", "1,0 A"],
        "I = B · ℓ / (μ₀ · N) = 2,5 · 10⁻³ · 0,20 / (4π · 10⁻⁷ · 400) ≈ 1,0 A.",
    ),
    tabel(
        "Met welke factor verandert B binnen in een lange spoel?",
        [
            ("twee keer zoveel windingen op dezelfde lengte", "× 2"),
            ("dezelfde windingen over twee keer de lengte", "÷ 2"),
            ("drie keer zoveel stroom", "× 3"),
        ],
        "B = μ₀ · N · I / ℓ.",
        kolommen=["× 2", "÷ 2", "× 3"],
    ),
    mk(
        "Een spoel zonder kern geeft B = 2 mT. Je verdubbelt de stroom en halveert het aantal windingen per meter. Hoe groot wordt B?",
        ["2 mT", "4 mT", "1 mT", "8 mT"],
        0,
        "× 2 voor de stroom en ÷ 2 voor de windingen per meter heffen elkaar op.",
    ),
    mk(
        "Waar rond een rechte draad is B even groot als in een punt op 3 cm?",
        [
            "In elk punt op 3 cm van de draad",
            "Alleen recht boven de draad op 3 cm",
            "Alleen in het punt op 3 cm aan de overkant",
            "Nergens anders, B is overal verschillend",
        ],
        0,
        "B hangt alleen af van I en r: alle punten op dezelfde cirkel.",
    ),
    sorteer(
        "Wordt deze stof sterk aangetrokken door een magneet?",
        ["Ferromagnetisch", "Niet ferromagnetisch"],
        [
            ("ijzer", "Ferromagnetisch"),
            ("nikkel", "Ferromagnetisch"),
            ("koper", "Niet ferromagnetisch"),
            ("aluminium", "Niet ferromagnetisch"),
            ("cobalt", "Ferromagnetisch"),
        ],
        "Alleen ijzer, nikkel, cobalt en hun legeringen.",
    ),
    casus(
        "Een ijzeren spijker hangt aan een sterke magneet. Onder de spijker hangt nog een tweede spijker.",
        [
            mk(
                "Wat gebeurt er in de bovenste spijker?",
                [
                    "De weissgebieden richten zich",
                    "De spijker wordt elektrisch geladen",
                    "Er ontstaat een losse noordpool",
                    "De atomen verhuizen naar één kant",
                ],
                0,
                "Magnetische influentie: de spijker wordt zelf een magneetje.",
            ),
            mk(
                "Waarom blijft de tweede spijker hangen?",
                [
                    "De eerste is zelf een magneetje",
                    "Ijzer kleeft altijd aan ijzer vast",
                    "De magneet trekt door lucht nooit",
                    "Er loopt een stroom door beide",
                ],
                0,
                "Elke spijker richt de weissgebieden van de volgende.",
            ),
            keuze(
                "Verhit je de spijkers sterk, dan [[*verliezen ze hun magnetisme|worden ze sterker magnetisch]].",
                "De warmte schudt de weissgebieden weer door elkaar.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak over magneten?",
        [
            ("Magnetische veldlijnen zijn gesloten kringen.", J),
            ("Je kan een losse noordpool maken door een magneet te breken.", F),
            ("Een magneet trekt ook door een houten plank heen.", J),
            ("Een magneet trekt elk metaal aan.", F),
        ],
        "Elk stukje van een magneet heeft twee polen.",
    ),
    koppel(
        "Koppel elke situatie aan de vorm van het veld.",
        [
            ("rond een rechte stroomdraad", "cirkels rond de draad"),
            ("binnen in een lange spoel", "evenwijdige lijnen langs de as"),
            ("rond een staafmagneet", "van N buitenom naar Z"),
            ("in het midden van een stroomlus", "loodrecht op het vlak van de lus"),
        ],
        ["stervormig vanuit één pool"],
        "Een spoel heeft buiten hetzelfde veld als een staafmagneet.",
    ),
    mk(
        "Welke handeling demagnetiseert een magneet niet?",
        [
            "Hem een nacht in de koelkast leggen",
            "Hem sterk opwarmen in een vlam",
            "Er herhaaldelijk hard op slaan met een hamer",
            "Hem langdurig in een vuur laten liggen",
        ],
        0,
        "Warmte en schokken schudden de weissgebieden door elkaar; koude doet dat niet.",
    ),
    keuze(
        "Duim in de zin van de stroom: je gekromde vingers geven de zin van [[*de veldlijnen|de kracht]] rond een rechte draad.",
        "Dat is de rechterhandregel.",
    ),
    volgorde(
        "Zet in volgorde wat er gebeurt als een stuk ijzer gemagnetiseerd wordt.",
        [
            "De weissgebieden wijzen alle kanten op",
            "Een magneet komt in de buurt",
            "De weissgebieden richten zich in dezelfde zin",
            "Het ijzer gedraagt zich zelf als magneet",
        ],
        "Zonder magneet heffen de gebiedjes elkaar op.",
    ),
    sleep(
        "Elke magneet heeft twee [[polen]]. Het magnetisme van een atoom komt van de [[kringstroom]] en de spin van zijn elektronen. IJzer, nikkel en cobalt zijn [[ferromagnetisch]].",
        ["ladingen", "isolator"],
        "Een bewegende lading maakt altijd een magnetisch veld.",
    ),
    open_(
        "Leg uit waarom je twee kleinere magneten krijgt als je een staafmagneet breekt, en geen losse noord- en zuidpool.",
        "Een magneet bestaat uit heel veel weissgebieden die elk al een klein magneetje met twee polen zijn. Breek je de staaf, dan blijven die gebiedjes gericht. Elk stuk heeft dus aan het ene uiteinde een noordpool en aan het andere een zuidpool.",
    ),
]
