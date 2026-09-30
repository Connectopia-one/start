# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij wiskunde 🚀 Boost dubbele finaliteit.

Negen bundels komen van doorstroom en worden hier overgenomen met de
verschillen erin gepatcht; vier zijn nieuw geschreven, bij de vier thema's die
op de DF-fiche een andere nadruk krijgen. Zie `maak_wiskunde_df.py` voor het
waarom van die opsplitsing.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel
import maak_oefeningen_wiskunde_boost as doorstroom
import maak_wiskunde_df as leerbundels

VAK = leerbundels.VAK
DF = leerbundels.DF
HOE = doorstroom.HOE
W, WW, WL = doorstroom.W, doorstroom.WW, doorstroom.WL

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"

OVERNEMEN = {
    "oefenbundel-een-opgave-aanpakken-van-context-naar-wiskunde": None,
    "oefenbundel-reele-getallen-wortels-en-machten": None,
    "oefenbundel-ordenen-afronden-intervallen-en-wetenschappelijke-notatie": (
        "oefenbundel-ordenen-afronden-en-intervallen",
        "Ordenen, afronden en intervallen",
    ),
    "oefenbundel-rechten-vlakken-en-gelijkvormigheid": None,
    "oefenbundel-pythagoras-en-de-rechthoekige-driehoek": None,
    "oefenbundel-formules-omvormen-en-eerstegraadsvergelijkingen": None,
    "oefenbundel-functies-en-de-rechte": None,
    "oefenbundel-telproblemen-met-boom-en-venndiagram": None,
    "oefenbundel-statistiek-voorstellingen-centrum-en-spreiding": None,
}

# (bundelsleutel zonder categorie, haak, wat)
#   schrap-reeks    : haak is de kop van de reeks
#   schrap-oefening : haak is een stuk tekst uit de oefening
#   vervang-oefening: haak is een stuk tekst uit de oefening, met de nieuwe erachter
PATCHES = [
    ("oefenbundel-ordenen-afronden-en-intervallen", "Wetenschappelijke notatie", "schrap-reeks", None),
    ("oefenbundel-ordenen-afronden-en-intervallen", "Correct of niet?", "schrap-reeks", None),
    ("oefenbundel-ordenen-afronden-en-intervallen",
     "Een negatieve exponent betekent dat het getal negatief is.", "schrap-oefening", None),
    ("oefenbundel-ordenen-afronden-en-intervallen",
     "Waarom gebruiken wetenschappers machten van tien", "schrap-oefening", None),
    ("oefenbundel-functies-en-de-rechte", "de parabool y = x²", "vervang-oefening",
     ("kies", "de horizontale rechte y = 4", ["wel een functie", "geen functie"], 0)),
]

TEKSTFIXES = [("Wiskunde gevorderd", VAK, 9)]

VERBODEN = leerbundels.VERBODEN


def tekst_van(oef) -> str:
    return " ".join(str(d) for d in oef)


def pas_toe(bundels: dict):
    for kort, haak, wat, vervanger in PATCHES:
        sleutel = kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        reeksen = bundels[sleutel]["reeksen"]
        if wat == "schrap-reeks":
            raak = [i for i, r in enumerate(reeksen) if r["kop"] == haak]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} reeksen heten {haak!r}, verwacht 1")
            reeksen.pop(raak[0])
            continue
        if wat == "schrap-oefening":
            raak = [
                (i, j)
                for i, r in enumerate(reeksen)
                for j, o in enumerate(r["oefeningen"])
                if haak in tekst_van(o)
            ]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} oefeningen bevatten {haak!r}, verwacht 1")
            i, j = raak[0]
            reeksen[i]["oefeningen"].pop(j)
            if not reeksen[i]["oefeningen"]:
                raise SystemExit(f"{sleutel}: reeks {reeksen[i]['kop']!r} blijft leeg achter")
            continue
        if wat == "vervang-oefening":
            raak = [
                (i, j)
                for i, r in enumerate(reeksen)
                for j, o in enumerate(r["oefeningen"])
                if haak in tekst_van(o)
            ]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} oefeningen bevatten {haak!r}, verwacht 1")
            i, j = raak[0]
            reeksen[i]["oefeningen"][j] = vervanger
            continue
        raise SystemExit(f"Onbekende ingreep: {wat}")


def overgenomen() -> dict:
    uit = {}
    for kort, hernoem in OVERNEMEN.items():
        bron = kort + OUD
        if bron not in doorstroom.OEFENBUNDELS:
            raise SystemExit(f"Onbekende doorstroombundel: {bron}")
        nieuw = copy.deepcopy(doorstroom.OEFENBUNDELS[bron])
        nieuw["niveau"] = DF
        if hernoem:
            kort, nieuw["titel"] = hernoem
        uit[kort + NIEUW] = nieuw
    pas_toe(uit)
    for oud, nieuw, hoevaak in TEKSTFIXES:
        uit, aantal = leerbundels.fix_teksten(uit, oud, nieuw)
        if aantal != hoevaak:
            raise SystemExit(f"{oud!r} staat {aantal} keer in de oefenbundels, verwacht {hoevaak}")
    return uit


def controleer(bundels: dict):
    for sleutel, b in bundels.items():
        alles = " ".join(
            [b["titel"]]
            + [r["kop"] + " " + r["opdracht"] for r in b["reeksen"]]
            + [tekst_van(o) for r in b["reeksen"] for o in r["oefeningen"]]
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{sleutel} gebruikt nog {woord!r}, dat staat niet op de DF-fiche")
        if b["vak"] != VAK or b["niveau"] != DF:
            raise SystemExit(f"{sleutel} draagt {b['vak']!r} / {b['niveau']!r}")


OEFENBUNDELS = overgenomen()
NIEUWE = {}


# ============================================================
NIEUWE["oefenbundel-de-rechthoekige-driehoek-oplossen-en-toepassen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="De rechthoekige driehoek oplossen en toepassen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke zijde is welke?",
             opdracht="Je kijkt naar hoek A in een rechthoekige driehoek. Duid aan.",
             oefeningen=[
                 ("kies", "de zijde tegenover de rechte hoek",
                  ["de schuine zijde", "de overstaande zijde van A", "de aanliggende zijde van A"], 0),
                 ("kies", "de rechthoekszijde die tegenover A ligt",
                  ["de schuine zijde", "de overstaande zijde van A", "de aanliggende zijde van A"], 1),
                 ("kies", "de rechthoekszijde die tegen A aan ligt",
                  ["de schuine zijde", "de overstaande zijde van A", "de aanliggende zijde van A"], 2),
             ]),
        dict(kop="De verhoudingen uitrekenen",
             opdracht="In een driehoek met zijden 6, 8 en 10 kijk je naar de hoek tegenover de zijde 6. Vul aan.",
             oefeningen=[
                 ("rij", [("sinus", "0,6"), ("cosinus", "0,8"), ("tangens", "0,75")], "Uitkomst", W),
             ]),
        dict(kop="En nog een driehoek",
             opdracht="In een driehoek met zijden 5, 12 en 13 kijk je naar de hoek tegenover de zijde 5. Rond af op twee cijfers na de komma.",
             oefeningen=[
                 ("rij", [("sinus", "0,38"), ("cosinus", "0,92"), ("tangens", "0,42")], "Uitkomst", W),
             ]),
        dict(kop="Welke verhouding gebruik je?",
             opdracht="Schrijf sinus, cosinus of tangens.",
             oefeningen=[
                 ("rij", [
                     ("je kent de hoek en de schuine zijde, je zoekt de overstaande", "sinus"),
                     ("je kent de hoek en de aanliggende zijde, je zoekt de overstaande", "tangens"),
                     ("je kent de hoek en de aanliggende zijde, je zoekt de schuine", "cosinus"),
                     ("je kent de twee rechthoekszijden, je zoekt de hoek", "tangens"),
                 ], "Verhouding", WW),
             ]),
        dict(kop="Bereken de zijde",
             opdracht="Rond af op twee cijfers na de komma en zet de eenheid erbij.",
             oefeningen=[
                 ("open", "Een ladder van 8 meter staat onder 65 graden met de grond. Hoe hoog reikt hij?",
                  "8 · sin 65° = 7,25 meter", 3),
                 ("open", "De schuine zijde is 20 cm en een scherpe hoek is 30 graden. Hoe lang is de overstaande zijde?",
                  "20 · sin 30° = 10 cm", 3),
                 ("open", "De aanliggende zijde is 15 cm en de hoek is 40 graden. Hoe lang is de overstaande zijde?",
                  "15 · tan 40° = 12,59 cm", 3),
             ]),
        dict(kop="Bereken de hoek",
             opdracht="Schrijf eerst de verhouding op, dan de hoek.",
             oefeningen=[
                 ("open", "De overstaande zijde is 3 cm en de schuine zijde 6 cm.",
                  "sinus is 3/6 = 0,5, dus de hoek is 30 graden", 3),
                 ("open", "De twee rechthoekszijden zijn allebei 7 cm.",
                  "tangens is 7/7 = 1, dus de hoek is 45 graden", 3),
             ]),
        dict(kop="De grondformule",
             opdracht="Bereken het andere goniometrische getal van dezelfde scherpe hoek.",
             oefeningen=[
                 ("rij", [("de sinus is 0,6, dus de cosinus is", "0,8"),
                          ("de cosinus is 0,28, dus de sinus is", "0,96")], "Uitkomst", W),
             ]),
        dict(kop="Hoogte en kijkhoek",
             opdracht="Maak eerst een schets. Rond af op één cijfer na de komma.",
             oefeningen=[
                 ("open", "Je staat 30 meter van een boom en kijkt onder 28 graden naar de top. Je ogen zitten 1,5 meter hoog. Hoe hoog is de boom?",
                  "30 · tan 28° = 16,0 meter, plus 1,5 meter ooghoogte, dus 17,5 meter", 4),
                 ("open", "Een vlieger hangt aan 25 meter touw onder 40 graden met de grond. Hoe hoog hangt hij?",
                  "25 · sin 40° = 16,1 meter", 3),
                 ("open", "Een bergpad van 800 meter loopt onder 9 graden. Hoeveel hoogte win je?",
                  "800 · sin 9° = 125,1 meter", 3),
             ]),
        dict(kop="Hellingen",
             opdracht="Reken uit. Denk eraan dat een hellingspercentage de tangens is, niet de hoek.",
             oefeningen=[
                 ("open", "Een weg helt 12 procent. Hoeveel stijg je over 250 meter horizontaal?",
                  "0,12 · 250 = 30 meter", 3),
                 ("open", "Een oprit mag hoogstens 6 procent hellen en moet 24 centimeter overbruggen. Hoe lang moet hij minstens zijn?",
                  "0,24 gedeeld door 0,06 is 4 meter", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De sinus van een scherpe hoek kan groter zijn dan 1.", False),
                 ("waar", "De tangens van een scherpe hoek kan groter zijn dan 1.", True),
                 ("waar", "De twee scherpe hoeken van een rechthoekige driehoek zijn samen 90 graden.", True),
                 ("waar", "Een helling van 10 procent komt overeen met een hoek van 10 graden.", False),
                 ("waar", "Met één gegeven zijde kan je de hele driehoek oplossen.", False),
                 ("waar", "Bij 45 graden zijn de sinus en de cosinus aan elkaar gelijk.", True),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Waarom hangen sinus, cosinus en tangens enkel van de hoek af en niet van de grootte van de driehoek?",
                  "Driehoeken met dezelfde hoeken zijn gelijkvormig: alle zijden worden met dezelfde factor vermenigvuldigd, en die factor valt in de breuk weg.", 4),
                 ("open", "Je berekent een scherpe hoek en krijgt 96 graden. Wat besluit je?",
                  "Dat er een fout in de berekening zit: in een rechthoekige driehoek blijft elke scherpe hoek onder 90 graden.", 3),
             ]),
    ],
)


# ============================================================
NIEUWE["oefenbundel-stelsels-van-twee-eerstegraadsvergelijkingen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Stelsels van twee eerstegraadsvergelijkingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Klopt dit koppel?",
             opdracht="Vul het koppel in allebei de vergelijkingen in en duid aan.",
             oefeningen=[
                 ("kies", "(3, 2) voor x + y = 5 en x − y = 1",
                  ["klopt", "klopt niet"], 0),
                 ("kies", "(4, 2) voor x + y = 6 en 2x + y = 12",
                  ["klopt", "klopt niet"], 1),
                 ("kies", "(1, 5) voor y = 5x en x + y = 6",
                  ["klopt", "klopt niet"], 0),
             ]),
        dict(kop="Los op met substitutie",
             opdracht="Vul de uitgeschreven onbekende in de andere vergelijking in. Schrijf je oplossing als koppel.",
             oefeningen=[
                 ("open", "y = 3x en x + y = 12", "x = 3 en y = 9, dus (3, 9)", 3),
                 ("open", "x = 2y en x + y = 9", "y = 3 en x = 6, dus (6, 3)", 3),
             ]),
        dict(kop="Los op met gelijkstelling",
             opdracht="Stel de twee uitdrukkingen aan elkaar gelijk.",
             oefeningen=[
                 ("open", "y = 2x + 1 en y = 4x − 3", "2x + 1 = 4x − 3 geeft x = 2 en y = 5, dus (2, 5)", 3),
             ]),
        dict(kop="Los op met combinatie",
             opdracht="Tel op of trek af zodat een onbekende wegvalt.",
             oefeningen=[
                 ("open", "x + y = 12 en x − y = 2", "optellen geeft 2x = 14, dus x = 7 en y = 5: (7, 5)", 3),
                 ("open", "3x + y = 14 en 3x − y = 4", "optellen geeft 6x = 18, dus x = 3 en y = 5: (3, 5)", 3),
             ]),
        dict(kop="Welke soort stelsel?",
             opdracht="Schrijf bepaald, strijdig of onbepaald.",
             oefeningen=[
                 ("rij", [("x + y = 4 en x + y = 9", "strijdig"),
                          ("x + y = 4 en 2x + 2y = 8", "onbepaald"),
                          ("x + y = 4 en x − y = 0", "bepaald")], "Soort", WW),
             ]),
        dict(kop="Wat zie je op de grafiek?",
             opdracht="Verbind het beeld met het stelsel.",
             oefeningen=[
                 ("rij", [("twee snijdende rechten", "bepaald, één oplossing"),
                          ("twee evenwijdige rechten", "strijdig, geen oplossing"),
                          ("twee samenvallende rechten", "onbepaald, oneindig veel")], "Het stelsel", WL),
             ]),
        dict(kop="Wat besluit je?",
             opdracht="Je werkt een stelsel uit en dit blijft over. Wat betekent dat?",
             oefeningen=[
                 ("rij", [("0 = 0", "onbepaald: oneindig veel oplossingen"),
                          ("0 = 6", "strijdig: geen enkele oplossing")], "Betekenis", WL),
             ]),
        dict(kop="Vraagstukken",
             opdracht="Schrijf eerst op wat x en wat y voorstelt, dan het stelsel, dan de oplossing.",
             oefeningen=[
                 ("open", "Drie pennen en twee schriften kosten 11 euro. Eén pen en twee schriften kosten 7 euro. Hoeveel kost een pen?",
                  "3p + 2s = 11 en p + 2s = 7; aftrekken geeft 2p = 4, dus een pen kost 2 euro en een schrift 2,50 euro.", 5),
                 ("open", "Een rechthoek heeft een omtrek van 26 cm en is 3 cm langer dan breed. Hoe lang en hoe breed is hij?",
                  "l + b = 13 en l − b = 3; optellen geeft 2l = 16, dus 8 cm lang en 5 cm breed.", 5),
                 ("open", "In een zaal staan stoelen en krukken, samen 40 zitplaatsen. Er zijn 12 stoelen meer dan krukken. Hoeveel krukken staan er?",
                  "s + k = 40 en s − k = 12; aftrekken geeft 2k = 28, dus 14 krukken en 26 stoelen.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "De koppels (2, 5) en (5, 2) zijn dezelfde oplossing.", False),
                 ("waar", "Een stelsel heeft altijd precies één oplossing.", False),
                 ("waar", "Je mag een vergelijking langs beide kanten met hetzelfde getal vermenigvuldigen.", True),
                 ("waar", "Bij een strijdig stelsel is de oplossingenverzameling de lege verzameling.", True),
                 ("waar", "Twee evenwijdige rechten hebben één gemeenschappelijk punt.", False),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Waarom kan je één vergelijking met twee onbekenden niet oplossen?",
                  "Omdat er oneindig veel koppels aan voldoen. Pas een tweede voorwaarde kiest er één uit.", 4),
                 ("open", "Wanneer kies je combinatie en wanneer substitutie?",
                  "Combinatie als een onbekende in beide vergelijkingen dezelfde coëfficiënt heeft; substitutie als er ergens al een onbekende alleen staat.", 4),
             ]),
    ],
)


# ============================================================
NIEUWE["oefenbundel-tekenverloop-verloopschema-en-grafisch-oplossen" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Tekenverloop, verloopschema en grafisch oplossen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zoek de nulwaarde",
             opdracht="Stel de functiewaarde gelijk aan nul en los op naar x.",
             oefeningen=[
                 ("rij", [("f(x) = 4x − 8", "x = 2"), ("f(x) = −2x + 10", "x = 5"),
                          ("f(x) = x + 7", "x = −7"), ("f(x) = 3x", "x = 0")], "Nulwaarde", W),
             ]),
        dict(kop="Nulwaarde of snijpunt met de y-as?",
             opdracht="Bereken allebei voor f(x) = 2x − 10.",
             oefeningen=[
                 ("kort", "de nulwaarde", "x = 5", W),
                 ("kort", "het snijpunt met de y-as, dus f(0)", "−10", W),
             ]),
        dict(kop="Het tekenverloop",
             opdracht="Vul de tabel aan. Schrijf waar de functie negatief is, waar ze nul is en waar ze positief is.",
             oefeningen=[
                 ("tabel", ["Functie", "Negatief", "Nul", "Positief"],
                  [["f(x) = 4x − 8", None, None, None], ["f(x) = −2x + 10", None, None, None]],
                  "4x − 8: negatief links van 2, nul in 2, positief rechts van 2 · "
                  "−2x + 10: positief links van 5, nul in 5, negatief rechts van 5", "150px"),
             ]),
        dict(kop="Het verloopschema",
             opdracht="Schrijf stijgend of dalend.",
             oefeningen=[
                 ("rij", [("f(x) = 3x − 1", "stijgend"), ("f(x) = −x + 2", "dalend"),
                          ("f(x) = 0,5x", "stijgend")], "Verloop", W),
             ]),
        dict(kop="Intervallen schrijven",
             opdracht="Schrijf de verzameling als interval. Let op de haakjes.",
             oefeningen=[
                 ("rij", [("alle x groter dan of gelijk aan −2", "[−2, +∞["),
                          ("alle x kleiner dan 7", "]−∞, 7["),
                          ("alle x tussen 0 en 5, grenzen erbij", "[0, 5]"),
                          ("alle x tussen 1 en 6, grenzen niet mee", "]1, 6[")], "Interval", WW),
             ]),
        dict(kop="Op de getallenas",
             opdracht="Beschrijf wat je tekent: open of vol bolletje, en welke kant je arceert.",
             oefeningen=[
                 ("open", "x groter dan 4", "open bolletje op 4, alles rechts ervan gearceerd", 2),
                 ("open", "x kleiner dan of gelijk aan −1", "vol bolletje op −1, alles links ervan gearceerd", 2),
             ]),
        dict(kop="Twee functies",
             opdracht="Neem f(x) = 2x en g(x) = x + 3. Reken uit.",
             oefeningen=[
                 ("open", "Waar snijden de twee grafieken elkaar?", "2x = x + 3 geeft x = 3, en de functiewaarde daar is 6.", 3),
                 ("open", "Voor welke x is f(x) groter dan g(x)?", "Voor x groter dan 3, dus ]3, +∞[.", 3),
             ]),
        dict(kop="Break-even",
             opdracht="Een atelier heeft kosten K(x) = 200 + 15x en opbrengst O(x) = 35x.",
             oefeningen=[
                 ("open", "Bij hoeveel stuks zijn kosten en opbrengst gelijk?",
                  "200 + 15x = 35x geeft 200 = 20x, dus bij 10 stuks.", 3),
                 ("open", "Vanaf hoeveel stuks is er winst?",
                  "Vanaf 11 stuks, want bij 10 is de winst nog nul.", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een stijgende grafiek heeft overal een positieve functiewaarde.", False),
                 ("waar", "Een constante functie zoals f(x) = 5 heeft geen nulwaarde.", True),
                 ("waar", "Bij oneindig staat het haakje van een interval altijd open.", True),
                 ("waar", "Twee verschillende rechten kunnen elkaar in twee punten snijden.", False),
                 ("waar", "Bij f(x) ≥ 0 telt de nulwaarde zelf mee in de oplossing.", True),
                 ("waar", "Een tekenverloop toont waar de functie stijgt en waar ze daalt.", False),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een tekenverloop en een verloopschema?",
                  "Een tekenverloop toont waar de functiewaarde positief of negatief is; een verloopschema toont waar de functie stijgt of daalt.", 4),
                 ("open", "Waarom hangt het antwoord op een ongelijkheid ervan af of de rechte stijgt of daalt?",
                  "Een stijgende rechte is positief rechts van haar nulwaarde, een dalende links ervan.", 4),
             ]),
    ],
)


# ============================================================
NIEUWE["oefenbundel-misleiding-met-cijfers-en-grafieken" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Misleiding met cijfers en grafieken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat is er mis?",
             opdracht="Noem de ingreep en leg uit wat ze met het beeld doet.",
             oefeningen=[
                 ("open", "Een staafdiagram van de omzet begint bij 950 in plaats van bij 0.",
                  "De verticale as begint niet bij nul: kleine verschillen lijken veel groter dan ze zijn.", 3),
                 ("open", "Op de tijdas staan 2018, 2019 en dan meteen 2024, met gelijke tussenafstanden.",
                  "De as is foutief geijkt en er worden jaren overgeslagen: de lijn loopt vlakker dan het verloop echt was.", 3),
                 ("open", "Een verdubbeling van de verkoop wordt getoond met een doos die twee keer zo breed én twee keer zo hoog is.",
                  "Uitvergroting: de oppervlakte wordt vier keer zo groot terwijl het cijfer maar verdubbelt.", 3),
             ]),
        dict(kop="Procent of procentpunt?",
             opdracht="Een cijfer gaat van 20 procent naar 25 procent. Vul aan.",
             oefeningen=[
                 ("rij", [("de stijging in procentpunt", "5 procentpunt"),
                          ("de stijging in procent", "25 procent")], "Uitkomst", WW),
             ]),
        dict(kop="Reken na",
             opdracht="Schrijf je tussenstappen op.",
             oefeningen=[
                 ("open", "Een jas van 50 euro krijgt eerst 30 procent en daarna 20 procent korting. Hoeveel procent korting is dat samen?",
                  "50 wordt 35 en daarna 28 euro. Dat is 22 euro korting op 50, dus 44 procent en niet 50.", 4),
                 ("open", "Een prijs van 200 euro stijgt met 25 procent en daalt daarna met 20 procent. Wat is de eindprijs?",
                  "200 wordt 250, en 20 procent van 250 is 50, dus opnieuw 200 euro.", 4),
             ]),
        dict(kop="Gemiddelde of mediaan?",
             opdracht="Neem de reeks 12, 14, 15, 16 en 93.",
             oefeningen=[
                 ("kort", "het rekenkundig gemiddelde", "30", W),
                 ("kort", "de mediaan", "15", W),
                 ("open", "Welk van de twee beschrijft deze reeks het best, en waarom?",
                  "De mediaan, want de 93 is een uitschieter die het gemiddelde ver optrekt terwijl vier van de vijf getallen rond 14 liggen.", 3),
             ]),
        dict(kop="Wat weet je zeker?",
             opdracht="Duid aan.",
             oefeningen=[
                 ("kies", "een winkel adverteert met 'tot 50 procent korting'",
                  ["elk artikel heeft 50 procent korting", "geen enkel artikel heeft meer dan 50 procent korting"], 1),
                 ("kies", "een bedrijf meldt dat de winst met 300 procent groeide",
                  ["de winst is verdrievoudigd", "de winst is vier keer zo groot geworden"], 1),
                 ("kies", "een krant schrijft dat het risico verdubbelt",
                  ["het risico is nu groot", "je weet niets zonder het risico van tevoren"], 1),
             ]),
        dict(kop="Is deze groep representatief?",
             opdracht="Duid aan en schrijf in één zin waarom.",
             oefeningen=[
                 ("open", "Een vraag over leesgewoontes, gesteld aan de uitgang van een bibliotheek.",
                  "Niet representatief: wie in een bibliotheek komt, leest per definitie meer dan gemiddeld.", 3),
                 ("open", "Een vraag over mobiliteit, gesteld aan mensen op een treinperron.",
                  "Niet representatief: wie op een perron staat, neemt de trein en dat zegt niets over wie met de auto rijdt.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Procent en procentpunt betekenen hetzelfde.", False),
                 ("waar", "Twee kortingen na elkaar mag je gewoon optellen.", False),
                 ("waar", "Een cijfer dat klopt, kan toch een verkeerde indruk geven.", True),
                 ("waar", "Een grafiek hoort te vermelden waar de cijfers vandaan komen.", True),
                 ("waar", "In een drie dimensies getekend cirkeldiagram lijken de sectoren vooraan groter.", True),
                 ("waar", "Een percentage zonder het aantal erbij zegt evenveel als een percentage met het aantal.", False),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Waarom is een percentage zonder het aantal erachter lastig te beoordelen?",
                  "Honderd procent van twee mensen en honderd procent van tweeduizend mensen zien er in een grafiek hetzelfde uit.", 4),
                 ("open", "Waarom vraag je bij een cijfer altijd wie het naar buiten brengt?",
                  "Wie belang heeft bij een uitkomst kan de voorstelling kleuren, ook met cijfers die perfect kloppen.", 4),
             ]),
    ],
)

OEFENBUNDELS.update(NIEUWE)
controleer(OEFENBUNDELS)

verwacht = {"oefenbundel-" + k + NIEUW for k in leerbundels.VOLGORDE}
if set(OEFENBUNDELS) != verwacht:
    raise SystemExit(
        "De oefenbundels komen niet overeen met de dertien thema's:\n"
        f"  te veel: {sorted(set(OEFENBUNDELS) - verwacht)}\n"
        f"  te weinig: {sorted(verwacht - set(OEFENBUNDELS))}"
    )
OEFENBUNDELS = {
    "oefenbundel-" + k + NIEUW: OEFENBUNDELS["oefenbundel-" + k + NIEUW]
    for k in leerbundels.VOLGORDE
}
