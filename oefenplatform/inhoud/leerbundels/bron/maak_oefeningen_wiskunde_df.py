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
    ("oefenbundel-ordenen-afronden-en-intervallen", "Wetenschappelijke notatie: terugrekenen", "schrap-reeks", None),
    ("oefenbundel-ordenen-afronden-en-intervallen",
     "Een negatieve exponent betekent dat het getal negatief is.", "schrap-oefening", None),
    ("oefenbundel-ordenen-afronden-en-intervallen",
     "Waarom gebruiken wetenschappers machten van tien", "schrap-oefening", None),
    ("oefenbundel-functies-en-de-rechte", r"de parabool \(y = x^{2}\)", "vervang-oefening",
     ("kies", r"de dalende rechte \(y = -x + 5\)", ["wel een functie", "geen functie"], 0)),
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
             opdracht=r"Je kijkt naar hoek \(\alpha\) in een rechthoekige driehoek. Duid aan.",
             oefeningen=[
                 ("kies", "de zijde tegenover de rechte hoek",
                  ["de schuine zijde", r"de overstaande zijde van \(\alpha\)", r"de aanliggende zijde van \(\alpha\)"], 0),
                 ("kies", r"de rechthoekszijde die tegenover \(\alpha\) ligt",
                  ["de schuine zijde", r"de overstaande zijde van \(\alpha\)", r"de aanliggende zijde van \(\alpha\)"], 1),
                 ("kies", r"de rechthoekszijde die tegen \(\alpha\) aan ligt",
                  ["de schuine zijde", r"de overstaande zijde van \(\alpha\)", r"de aanliggende zijde van \(\alpha\)"], 2),
             ]),
        dict(kop="De verhoudingen uitrekenen",
             opdracht=r"In een driehoek met zijden \(6\), \(8\) en \(10\) kijk je naar de hoek tegenover de zijde \(6\). Vul aan.",
             oefeningen=[
                 ("rij", [(r"\(\sin \alpha\)", r"\(0{,}6\)"), (r"\(\cos \alpha\)", r"\(0{,}8\)"),
                          (r"\(\tan \alpha\)", r"\(0{,}75\)")], "Uitkomst", W),
             ]),
        dict(kop="En nog een driehoek",
             opdracht=r"In een driehoek met zijden \(5\), \(12\) en \(13\) kijk je naar de hoek tegenover de zijde \(5\). Rond af op twee cijfers na de komma.",
             oefeningen=[
                 ("rij", [(r"\(\sin \alpha\)", r"\(0{,}38\)"), (r"\(\cos \alpha\)", r"\(0{,}92\)"),
                          (r"\(\tan \alpha\)", r"\(0{,}42\)")], "Uitkomst", W),
             ]),
        dict(kop="Welke verhouding gebruik je?",
             opdracht=r"Schrijf \(\sin\), \(\cos\) of \(\tan\).",
             oefeningen=[
                 ("rij", [
                     ("je kent de hoek en de schuine zijde, je zoekt de overstaande", r"\(\sin\)"),
                     ("je kent de hoek en de aanliggende zijde, je zoekt de overstaande", r"\(\tan\)"),
                     ("je kent de hoek en de aanliggende zijde, je zoekt de schuine", r"\(\cos\)"),
                     ("je kent de twee rechthoekszijden, je zoekt de hoek", r"\(\tan\)"),
                 ], "Verhouding", WW),
             ]),
        dict(kop="Bereken de zijde",
             opdracht="Rond af op twee cijfers na de komma en zet de eenheid erbij.",
             oefeningen=[
                 ("open", r"Een ladder van \(8\) meter staat onder \(65^{\circ}\) met de grond. Hoe hoog reikt hij?",
                  r"\(8 \cdot \sin 65^{\circ} \approx 7{,}25\) meter", 3),
                 ("open", r"De schuine zijde is \(20\) cm en een scherpe hoek is \(30^{\circ}\). Hoe lang is de overstaande zijde?",
                  r"\(20 \cdot \sin 30^{\circ} = 10\) cm", 3),
                 ("open", r"De aanliggende zijde is \(15\) cm en de hoek is \(40^{\circ}\). Hoe lang is de overstaande zijde?",
                  r"\(15 \cdot \tan 40^{\circ} \approx 12{,}59\) cm", 3),
             ]),
        dict(kop="Bereken de hoek",
             opdracht="Schrijf eerst de verhouding op, dan de hoek.",
             oefeningen=[
                 ("open", r"De overstaande zijde is \(3\) cm en de schuine zijde \(6\) cm.",
                  r"\(\sin \alpha = \frac{3}{6} = 0{,}5\), dus \(\alpha = 30^{\circ}\)", 3),
                 ("open", r"De twee rechthoekszijden zijn allebei \(7\) cm.",
                  r"\(\tan \alpha = \frac{7}{7} = 1\), dus \(\alpha = 45^{\circ}\)", 3),
             ]),
        dict(kop="De grondformule",
             opdracht="Bereken het andere goniometrische getal van dezelfde scherpe hoek.",
             oefeningen=[
                 ("rij", [(r"\(\sin \alpha = 0{,}6\), dus \(\cos \alpha\) is", r"\(0{,}8\)"),
                          (r"\(\cos \alpha = 0{,}28\), dus \(\sin \alpha\) is", r"\(0{,}96\)")], "Uitkomst", W),
             ]),
        dict(kop="Hoogte en kijkhoek",
             opdracht="Maak eerst een schets. Rond af op één cijfer na de komma.",
             oefeningen=[
                 ("open", r"Je staat \(30\) meter van een boom en kijkt onder \(28^{\circ}\) naar de top. Je ogen zitten \(1{,}5\) meter hoog. Hoe hoog is de boom?",
                  r"\(30 \cdot \tan 28^{\circ} \approx 16{,}0\) meter, plus \(1{,}5\) meter ooghoogte, dus \(17{,}5\) meter", 4),
                 ("open", r"Een vlieger hangt aan \(25\) meter touw onder \(40^{\circ}\) met de grond. Hoe hoog hangt hij?",
                  r"\(25 \cdot \sin 40^{\circ} \approx 16{,}1\) meter", 3),
                 ("open", r"Een bergpad van \(800\) meter loopt onder \(9^{\circ}\). Hoeveel hoogte win je?",
                  r"\(800 \cdot \sin 9^{\circ} \approx 125{,}1\) meter", 3),
             ]),
        dict(kop="Hellingen",
             opdracht="Reken uit. Denk eraan dat een hellingspercentage de tangens is, niet de hoek.",
             oefeningen=[
                 ("open", r"Een weg helt \(12\,\%\). Hoeveel stijg je over \(250\) meter horizontaal?",
                  r"\(0{,}12 \cdot 250 = 30\) meter", 3),
                 ("open", r"Een oprit mag hoogstens \(6\,\%\) hellen en moet \(24\) centimeter overbruggen. Hoe lang moet hij minstens zijn?",
                  r"\(\frac{0{,}24}{0{,}06} = 4\) meter", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", r"\(\sin \alpha\) van een scherpe hoek kan groter zijn dan \(1\).", False),
                 ("waar", r"\(\tan \alpha\) van een scherpe hoek kan groter zijn dan \(1\).", True),
                 ("waar", r"De twee scherpe hoeken van een rechthoekige driehoek zijn samen \(90^{\circ}\).", True),
                 ("waar", r"Een helling van \(10\,\%\) komt overeen met een hoek van \(10^{\circ}\).", False),
                 ("waar", "Met één gegeven zijde kan je de hele driehoek oplossen.", False),
                 ("waar", r"Bij \(45^{\circ}\) zijn \(\sin \alpha\) en \(\cos \alpha\) aan elkaar gelijk.", True),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", r"Waarom hangen \(\sin\), \(\cos\) en \(\tan\) enkel van de hoek af en niet van de grootte van de driehoek?",
                  "Driehoeken met dezelfde hoeken zijn gelijkvormig: alle zijden worden met dezelfde factor vermenigvuldigd, en die factor valt in de breuk weg.", 4),
                 ("open", r"Je berekent een scherpe hoek en krijgt \(96^{\circ}\). Wat besluit je?",
                  r"Dat er een fout in de berekening zit: in een rechthoekige driehoek blijft elke scherpe hoek onder \(90^{\circ}\).", 3),
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
                 ("kies", r"\((3, 2)\) voor \(x + y = 5\) en \(x - y = 1\)",
                  ["klopt", "klopt niet"], 0),
                 ("kies", r"\((4, 2)\) voor \(x + y = 6\) en \(2x + y = 12\)",
                  ["klopt", "klopt niet"], 1),
                 ("kies", r"\((1, 5)\) voor \(y = 5x\) en \(x + y = 6\)",
                  ["klopt", "klopt niet"], 0),
             ]),
        dict(kop="Los op met substitutie",
             opdracht="Vul de uitgeschreven onbekende in de andere vergelijking in. Schrijf je oplossing als koppel.",
             oefeningen=[
                 ("open", r"\(y = 3x\) en \(x + y = 12\)", r"\(x = 3\) en \(y = 9\), dus \((3, 9)\)", 3),
                 ("open", r"\(x = 2y\) en \(x + y = 9\)", r"\(y = 3\) en \(x = 6\), dus \((6, 3)\)", 3),
             ]),
        dict(kop="Los op met gelijkstelling",
             opdracht="Stel de twee uitdrukkingen aan elkaar gelijk.",
             oefeningen=[
                 ("open", r"\(y = 2x + 1\) en \(y = 4x - 3\)",
                  r"\(2x + 1 = 4x - 3\) geeft \(x = 2\) en \(y = 5\), dus \((2, 5)\)", 3),
             ]),
        dict(kop="Los op met combinatie",
             opdracht="Tel op of trek af zodat een onbekende wegvalt.",
             oefeningen=[
                 ("open", r"\(x + y = 12\) en \(x - y = 2\)",
                  r"optellen geeft \(2x = 14\), dus \(x = 7\) en \(y = 5\): \((7, 5)\)", 3),
                 ("open", r"\(3x + y = 14\) en \(3x - y = 4\)",
                  r"optellen geeft \(6x = 18\), dus \(x = 3\) en \(y = 5\): \((3, 5)\)", 3),
             ]),
        dict(kop="Welke soort stelsel?",
             opdracht="Schrijf bepaald, strijdig of onbepaald.",
             oefeningen=[
                 ("rij", [(r"\(x + y = 4\) en \(x + y = 9\)", "strijdig"),
                          (r"\(x + y = 4\) en \(2x + 2y = 8\)", "onbepaald"),
                          (r"\(x + y = 4\) en \(x - y = 0\)", "bepaald")], "Soort", WW),
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
                 ("rij", [(r"\(0 = 0\)", "onbepaald: oneindig veel oplossingen"),
                          (r"\(0 = 6\)", "strijdig: geen enkele oplossing"),
                          (r"\(0 = -3\)", "strijdig: geen enkele oplossing"),
                          (r"\(x = 4\) en \(y = 1\)", "bepaald: precies één oplossing")], "Betekenis", WL),
             ]),
        dict(kop="Vraagstukken",
             opdracht=r"Schrijf eerst op wat \(x\) en wat \(y\) voorstelt, dan het stelsel, dan de oplossing.",
             oefeningen=[
                 ("open", r"Drie pennen en twee schriften kosten \(11\) euro. Eén pen en twee schriften kosten \(7\) euro. Hoeveel kost een pen?",
                  r"\(3p + 2s = 11\) en \(p + 2s = 7\); aftrekken geeft \(2p = 4\), dus een pen kost \(2\) euro en een schrift \(2{,}50\) euro.", 5),
                 ("open", r"Een rechthoek heeft een omtrek van \(26\) cm en is \(3\) cm langer dan breed. Hoe lang en hoe breed is hij?",
                  r"\(l + b = 13\) en \(l - b = 3\); optellen geeft \(2l = 16\), dus \(8\) cm lang en \(5\) cm breed.", 5),
             ]),
        dict(kop="Nog twee vraagstukken",
             opdracht="Dezelfde werkwijze: eerst de afspraak, dan het stelsel, dan de oplossing.",
             oefeningen=[
                 ("open", r"In een zaal staan stoelen en krukken, samen \(40\) zitplaatsen. Er zijn \(12\) stoelen meer dan krukken. Hoeveel krukken staan er?",
                  r"\(s + k = 40\) en \(s - k = 12\); aftrekken geeft \(2k = 28\), dus \(14\) krukken en \(26\) stoelen.", 5),
                 ("open", r"Twee volwassenen en drie kinderen betalen samen \(36\) euro voor het zwembad. Eén volwassene en drie kinderen betalen \(24\) euro. Wat kost een kaartje voor een volwassene?",
                  r"\(2v + 3k = 36\) en \(v + 3k = 24\); aftrekken geeft \(v = 12\), dus een volwassene betaalt \(12\) euro en een kind \(4\) euro.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", r"De koppels \((2, 5)\) en \((5, 2)\) zijn dezelfde oplossing.", False),
                 ("waar", "Een stelsel heeft altijd precies één oplossing.", False),
                 ("waar", "Je mag een vergelijking langs beide kanten met hetzelfde getal vermenigvuldigen.", True),
                 ("waar", r"Bij een strijdig stelsel is de oplossingenverzameling \(\emptyset\).", True),
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
             opdracht=r"Stel de functiewaarde gelijk aan \(0\) en los op naar \(x\).",
             oefeningen=[
                 ("rij", [(r"\(f(x) = 4x - 8\)", r"\(x = 2\)"), (r"\(f(x) = -2x + 10\)", r"\(x = 5\)"),
                          (r"\(f(x) = x + 7\)", r"\(x = -7\)"), (r"\(f(x) = 3x\)", r"\(x = 0\)")],
                  "Nulwaarde", W),
             ]),
        dict(kop="Nulwaarde of snijpunt met de y-as?",
             opdracht=r"Bereken allebei voor \(f(x) = 2x - 10\).",
             oefeningen=[
                 ("kort", "de nulwaarde", r"\(x = 5\)", W),
                 ("kort", r"het snijpunt met de \(y\)-as, dus \(f(0)\)", r"\(-10\)", W),
             ]),
        dict(kop="Het tekenverloop",
             opdracht="Vul de tabel aan. Schrijf waar de functie negatief is, waar ze nul is en waar ze positief is.",
             oefeningen=[
                 ("tabel", ["Functie", "Negatief", "Nul", "Positief"],
                  [[r"\(f(x) = 4x - 8\)", None, None, None], [r"\(f(x) = -2x + 10\)", None, None, None]],
                  r"\(4x - 8\): negatief links van \(2\), nul in \(2\), positief rechts van \(2\) · "
                  r"\(-2x + 10\): positief links van \(5\), nul in \(5\), negatief rechts van \(5\)", "150px"),
             ]),
        dict(kop="Het verloopschema",
             opdracht="Schrijf stijgend of dalend.",
             oefeningen=[
                 ("rij", [(r"\(f(x) = 3x - 1\)", "stijgend"), (r"\(f(x) = -x + 2\)", "dalend"),
                          (r"\(f(x) = 0{,}5x\)", "stijgend")], "Verloop", W),
             ]),
        dict(kop="Intervallen schrijven",
             opdracht="Schrijf de verzameling als interval. Let op de haakjes.",
             oefeningen=[
                 ("rij", [(r"alle \(x \geq -2\)", r"\(\left[-2, +\infty\right[\)"),
                          (r"alle \(x < 7\)", r"\(\left]-\infty, 7\right[\)"),
                          (r"alle \(x\) tussen \(0\) en \(5\), grenzen erbij", r"\(\left[0, 5\right]\)"),
                          (r"alle \(x\) tussen \(1\) en \(6\), grenzen niet mee", r"\(\left]1, 6\right[\)")],
                  "Interval", WW),
             ]),
        dict(kop="Op de getallenas",
             opdracht="Beschrijf wat je tekent: open of vol bolletje, en welke kant je arceert.",
             oefeningen=[
                 ("open", r"\(x > 4\)", r"open bolletje op \(4\), alles rechts ervan gearceerd", 2),
                 ("open", r"\(x \leq -1\)", r"vol bolletje op \(-1\), alles links ervan gearceerd", 2),
             ]),
        dict(kop="Twee functies",
             opdracht=r"Neem \(f(x) = 2x\) en \(g(x) = x + 3\). Reken uit.",
             oefeningen=[
                 ("open", "Waar snijden de twee grafieken elkaar?",
                  r"\(2x = x + 3\) geeft \(x = 3\), en de functiewaarde daar is \(6\).", 3),
                 ("open", r"Voor welke \(x\) is \(f(x) > g(x)\)?",
                  r"Voor \(x > 3\), dus \(\left]3, +\infty\right[\).", 3),
             ]),
        dict(kop="Break-even",
             opdracht=r"Een atelier heeft kosten \(K(x) = 200 + 15x\) en opbrengst \(O(x) = 35x\).",
             oefeningen=[
                 ("open", "Bij hoeveel stuks zijn kosten en opbrengst gelijk?",
                  r"\(200 + 15x = 35x\) geeft \(200 = 20x\), dus bij \(10\) stuks.", 3),
                 ("open", "Vanaf hoeveel stuks is er winst?",
                  r"Vanaf \(11\) stuks, want bij \(10\) is de winst nog nul.", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Duid aan of de uitspraak klopt.",
             oefeningen=[
                 ("waar", "Een stijgende grafiek heeft overal een positieve functiewaarde.", False),
                 ("waar", r"Een constante functie zoals \(f(x) = 5\) heeft geen nulwaarde.", True),
                 ("waar", r"Bij \(\infty\) staat het haakje van een interval altijd open.", True),
                 ("waar", "Twee verschillende rechten kunnen elkaar in twee punten snijden.", False),
                 ("waar", r"Bij \(f(x) \geq 0\) telt de nulwaarde zelf mee in de oplossing.", True),
                 ("waar", "Een tekenverloop toont waar de functie stijgt en waar ze daalt.", False),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een tekenverloop en een verloopschema?",
                  "Een tekenverloop toont waar de functiewaarde positief of negatief is; een verloopschema toont waar de functie stijgt of daalt.", 3),
                 ("open", "Waarom hangt het antwoord op een ongelijkheid ervan af of de rechte stijgt of daalt?",
                  "Een stijgende rechte is positief rechts van haar nulwaarde, een dalende links ervan.", 3),
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
                 ("open", r"Een staafdiagram van de omzet begint bij \(950\) in plaats van bij \(0\).",
                  r"De verticale as begint niet bij \(0\): kleine verschillen lijken veel groter dan ze zijn.", 3),
                 ("open", r"Op de tijdas staan \(2018\), \(2019\) en dan meteen \(2024\), met gelijke tussenafstanden.",
                  "De as is foutief geijkt en er worden jaren overgeslagen: de lijn loopt vlakker dan het verloop echt was.", 3),
                 ("open", "Een verdubbeling van de verkoop wordt getoond met een doos die twee keer zo breed én twee keer zo hoog is.",
                  "Uitvergroting: de oppervlakte wordt vier keer zo groot terwijl het cijfer maar verdubbelt.", 3),
             ]),
        dict(kop="Procent of procentpunt?",
             opdracht=r"Een cijfer gaat van \(20\,\%\) naar \(25\,\%\). Vul aan.",
             oefeningen=[
                 ("rij", [("de stijging in procentpunt", r"\(5\) procentpunt"),
                          ("de stijging in procent", r"\(25\,\%\)")], "Uitkomst", WW),
             ]),
        dict(kop="Reken na",
             opdracht="Schrijf je tussenstappen op.",
             oefeningen=[
                 ("open", r"Een jas van \(50\) euro krijgt eerst \(30\,\%\) en daarna \(20\,\%\) korting. Hoeveel procent korting is dat samen?",
                  r"\(50\) wordt \(35\) en daarna \(28\) euro. Dat is \(22\) euro korting op \(50\), dus \(44\,\%\) en niet \(50\,\%\).", 4),
                 ("open", r"Een prijs van \(200\) euro stijgt met \(25\,\%\) en daalt daarna met \(20\,\%\). Wat is de eindprijs?",
                  r"\(200\) wordt \(250\), en \(20\,\%\) van \(250\) is \(50\), dus opnieuw \(200\) euro.", 4),
             ]),
        dict(kop="Gemiddelde of mediaan?",
             opdracht=r"Neem de reeks \(12,\ 14,\ 15,\ 16\) en \(93\).",
             oefeningen=[
                 ("kort", "het rekenkundig gemiddelde", r"\(30\)", W),
                 ("kort", "de mediaan", r"\(15\)", W),
                 ("open", "Welk van de twee beschrijft deze reeks het best, en waarom?",
                  r"De mediaan, want de \(93\) is een uitschieter die het gemiddelde ver optrekt terwijl vier van de vijf getallen rond \(14\) liggen.", 3),
             ]),
        dict(kop="Wat weet je zeker?",
             opdracht="Duid aan.",
             oefeningen=[
                 ("kies", r"een winkel adverteert met 'tot \(50\,\%\) korting'",
                  [r"elk artikel heeft \(50\,\%\) korting", r"geen enkel artikel heeft meer dan \(50\,\%\) korting"], 1),
                 ("kies", r"een bedrijf meldt dat de winst met \(300\,\%\) groeide",
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
                 ("waar", "Een percentage zegt evenveel zonder als met het aantal erbij.", False),
             ]),
        dict(kop="Denken",
             opdracht="Schrijf je redenering uit.",
             oefeningen=[
                 ("open", "Waarom is een percentage zonder het aantal erachter lastig te beoordelen?",
                  r"\(100\,\%\) van twee mensen en \(100\,\%\) van tweeduizend mensen zien er in een grafiek hetzelfde uit.", 4),
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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-opgave-aanpakken-van-context-naar-wiskunde-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Mathematiseren is van de werkelijkheid naar de wiskunde gaan, demathematiseren is "
                    "terug. Vraag je af aan welke kant je op dat ogenblik staat.",
             waarom=[
                 "De tweede is het duidelijkst: \\(7{,}3\\) bussen bestaat niet, dus vertaal je het getal "
                 "terug naar de werkelijkheid en kom je op \\(8\\).",
             ]),
        dict(aanpak="Bij een vraagstuk weet je meteen welke leerstof je nodig hebt. Bij een probleem moet "
                    "je dat zelf uitzoeken, vaak uit meerdere hoofdstukken.",
             waarom=[None]),
        dict(aanpak="Een heuristiek is een aanpak die je op gang helpt. Zoek bij elk voorbeeld wat de "
                    "persoon eigenlijk dóét om vooruit te raken.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze: kijk naar de handeling, niet naar het onderwerp van de opgave.",
             waarom=[None]),
        dict(aanpak="De vier stappen van Polya zijn de ruggengraat van elk vraagstuk: begrijpen, plannen, "
                    "uitvoeren, reflecteren.",
             waarom=[None]),
        dict(aanpak="Vraag je bij elke handeling af of ze over lezen, kiezen, rekenen of controleren gaat. "
                    "Dat wijst meteen de stap aan.",
             waarom=[None]),
        dict(aanpak="Bij reflecteren zeg je eerst waarom de uitkomst niet kán kloppen, en pas daarna wat er "
                    "waarschijnlijk misliep. Die orde is belangrijk, want het eerste kan je altijd.",
             waarom=[
                 "Een omrekening tussen kubieke meter en liter is de klassieker: \\(1\\) m\\(^{3}\\) is "
                 "\\(1\\,000\\) liter.",
                 "Zet minuten altijd om in uren voor je deelt, anders klopt de eenheid van je antwoord "
                 "niet.",
                 None,
             ]),
        dict(aanpak="Schat eerst met ronde getallen, reken daarna precies. De schatting is je controle, "
                    "niet je antwoord.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze: zeg eerst waarom het niet kan.",
             waarom=[
                 None,
                 "Dit is de meest gemaakte procentfout: na een korting van \\(30\\,\\%\\) betaal je "
                 "\\(70\\,\\%\\), dus vermenigvuldig je met \\(0{,}7\\).",
             ]),
        dict(aanpak="Rond beide factoren naar een rond getal en reken dan uit je hoofd.",
             waarom=[None]),
        dict(aanpak="Schrijf zeker je plan en je controle op. De controle is wat van een antwoord een "
                    "zeker antwoord maakt.",
             waarom=[
                 "Terugrekenen van een korting doe je met een deling, niet door er \\(25\\,\\%\\) bij te "
                 "tellen. Dat laatste geeft \\(75\\) euro en is fout.",
                 "Kijk bij een rij altijd eerst naar de verschillen. Zijn die regelmatig, dan heb je het "
                 "patroon te pakken.",
             ]),
        dict(aanpak="Schrijf eerst op waar je letter voor staat. Zonder die zin is een formule niet te "
                    "lezen, ook niet door jezelf.",
             waarom=[None]),
        dict(aanpak="Werk met de vier stappen en schrijf je controle op.",
             waarom=[
                 "De controle is hier eenvoudig: de hoogte moet net iets kleiner zijn dan de ladder zelf.",
                 None,
             ]),
        dict(aanpak="Vier vaardigheden die in elk vraagstuk meespelen: lezen, rekenen, meten en tekenen, en "
                    "werken met je toestel.",
             waarom=[None]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen illustreren en bewijzen, en tussen "
                    "schatten en rekenen.",
             waarom=[
                 None,
                 "Een schatting zegt in welke orde van grootte het antwoord ligt. Ze vervangt de berekening "
                 "niet, ze controleert ze.",
                 "Eén tegenvoorbeeld volstaat om een altijd-uitspraak onderuit te halen; voorbeelden die "
                 "kloppen bewijzen nooit iets.",
                 None, None, None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en zeg wat reflecteren of verantwoorden je oplevert.",
             waarom=[None, None]),
        dict(aanpak="Hier gaat het om het verschil tussen een voorbeeld en een bewijs. Een redenering moet "
                    "voor élk getal opgaan.",
             waarom=[
                 None,
                 "Getallen tussen \\(0\\) en \\(1\\) worden kleiner als je ze kwadrateert. Dat is net het "
                 "soort geval dat je bij drie voorbeelden over het hoofd ziet.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-reele-getallen-wortels-en-machten-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="De verzamelingen zitten in elkaar: \\(\\mathbb{N}\\) in \\(\\mathbb{Z}\\) in "
                    "\\(\\mathbb{Q}\\) in \\(\\mathbb{R}\\). Gevraagd wordt de kleinste waarin het getal "
                    "past.",
             waarom=[
                 None,
                 "Let op \\(\\sqrt{49}\\): dat is gewoon \\(7\\), dus een natuurlijk getal. Niet elke "
                 "wortel is irrationaal.",
             ]),
        dict(aanpak="Een getal is rationaal als je het als breuk kan schrijven. Aan de decimale vorm zie je "
                    "het: stopt ze of herhaalt ze zich, dan is het rationaal.",
             waarom=[
                 "Een herhalend blokje maakt het getal rationaal: \\(0{,}2727\\ldots\\) is "
                 "\\(\\tfrac{27}{99}\\).",
                 None,
                 "\\(\\sqrt{64}\\) is \\(8\\). De wortel van een volkomen kwadraat is altijd rationaal.",
                 None,
             ]),
        dict(aanpak="Van breuk naar kommagetal deel je, van kommagetal naar procent vermenigvuldig je met "
                    "honderd. Vereenvoudig de breuk helemaal.",
             waarom=[None]),
        dict(aanpak="Splits het getal onder de wortel in een volkomen kwadraat maal de rest, en haal dat "
                    "kwadraat eruit.",
             waarom=[
                 "Bij \\(\\sqrt{48}\\) neem je \\(16 \\cdot 3\\), niet \\(4 \\cdot 12\\). Neem altijd het "
                 "grootste kwadraat, anders moet je nog eens verder.",
             ]),
        dict(aanpak="Zelfde werkwijze met grotere getallen. Ken je de kwadraten tot \\(144\\), dan gaat dit "
                    "vlot.",
             waarom=[None]),
        dict(aanpak="Zoek het getal dat drie keer met zichzelf vermenigvuldigd dit geeft. Een "
                    "derdemachtswortel mag ook van een negatief getal.",
             waarom=[None]),
        dict(aanpak="Vermenigvuldigen mag je onder één wortel zetten, optellen niet. Gelijke wortels tel je "
                    "op zoals gelijksoortige termen.",
             waarom=[
                 "Let op het laatste: \\(\\sqrt{16+9}\\) is \\(\\sqrt{25} = 5\\) en niet \\(4+3\\). Onder "
                 "de wortel reken je eerst de som uit.",
                 "\\(\\sqrt{a^{2}}\\) is de absolute waarde van \\(a\\), dus \\(4\\) en niet \\(-4\\). Een "
                 "vierkantswortel is nooit negatief.",
             ]),
        dict(aanpak="Vermenigvuldig teller en noemer met de wortel uit de noemer. Je vermenigvuldigt dus "
                    "met \\(1\\) en verandert enkel de schrijfwijze.",
             waarom=[None]),
        dict(aanpak="Vier rekenregels: bij vermenigvuldigen tel je de exponenten op, bij delen trek je ze "
                    "af, bij een macht van een macht vermenigvuldig je, en een exponent op een product "
                    "geldt voor elke factor.",
             waarom=[None]),
        dict(aanpak="Een exponent nul geeft altijd \\(1\\), een negatieve exponent keert het getal om. Ze "
                    "maakt het nooit negatief.",
             waarom=[None]),
        dict(aanpak="Dezelfde regels, nu met letters erbij. Werk stap voor stap en schrijf nooit een "
                    "negatieve exponent in je eindantwoord.",
             waarom=[None]),
        dict(aanpak="Drie eigenschappen om bij naam te kennen: verdelen over een som is distributiviteit, "
                    "anders haakjes zetten is associativiteit, van plaats wisselen is commutativiteit.",
             waarom=[None]),
        dict(aanpak="Zeg eerst wát er fout is en geef dan het juiste antwoord. Zo onthoud je de regel in "
                    "plaats van het geval.",
             waarom=[
                 "De wortel van een som is niet de som van de wortels. Dat is de meest gemaakte fout van "
                 "heel dit hoofdstuk.",
                 None,
             ]),
        dict(aanpak="Zelfde opdracht: benoem de regel die geschonden wordt.",
             waarom=[
                 "De exponent geldt voor élke factor binnen de haakjes, dus ook voor de \\(2\\).",
                 None,
             ]),
        dict(aanpak="Ga bij elke uitspraak na of ze over de verzamelingen gaat of over een rekenregel.",
             waarom=[
                 None,
                 "Dat kan net niet bij de irrationale getallen zoals \\(\\pi\\) en \\(\\sqrt{2}\\). Juist "
                 "daarvoor bestaat \\(\\mathbb{R}\\).",
                 None, None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en gebruik een voorbeeld om je uitleg te dragen.",
             waarom=[None, None]),
        dict(aanpak="Hier gaat het telkens om hetzelfde: een andere schrijfwijze is nog geen ander getal, "
                    "en een regel moet voor élk getal opgaan.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-ordenen-afronden-en-intervallen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Zet alles in dezelfde vorm voor je vergelijkt. Bij negatieve getallen is het getal met "
                    "de grootste cijfers juist het kleinste.",
             waarom=[
                 "Bij \\(-7\\) en \\(-2\\) is \\(-7\\) het kleinste: hoe verder naar links op de "
                 "getallenas, hoe kleiner.",
             ]),
        dict(aanpak="Zet eerst alles om naar kommagetallen, dan is de volgorde zo gezien. Schrijf die "
                    "omzetting erbij.",
             waarom=[None, None]),
        dict(aanpak="Kijk enkel naar het eerste cijfer dat wegvalt: vijf of meer naar boven, anders naar "
                    "beneden. Rond nooit in twee keer af.",
             waarom=[
                 "\\(5{,}6349\\) en \\(5{,}6351\\) liggen dicht bij elkaar en ronden toch anders af. Het "
                 "cijfer erna telt niet mee.",
             ]),
        dict(aanpak="Maak van elke factor een rond getal en reken dan uit je hoofd. De schatting hoeft niet "
                    "juist te zijn, wel in de goede orde van grootte.",
             waarom=[None]),
        dict(aanpak="Een vierkant haakje betekent dat de grens meedoet, een rond haakje dat ze erbuiten "
                    "valt. Zeg dat in gewone taal in je antwoord.",
             waarom=[None]),
        dict(aanpak="Schrijf eerst op of de grens meedoet, en kies dan het haakje. Bij oneindig wijst het "
                    "haakje altijd naar buiten.",
             waarom=[None]),
        dict(aanpak="Zelfde werkwijze, nu ook met het gelijkheidsteken erbij.",
             waarom=[
                 "Let op \\(-\\tfrac{2}{5}\\) en \\(-0{,}5\\): dat is \\(-0{,}4\\) tegenover \\(-0{,}5\\), "
                 "dus het eerste is groter.",
             ]),
        dict(aanpak="Zelfde regel als hiervoor, nu op één cijfer. Let bij een negatief getal op: verder van "
                    "nul is kleiner.",
             waarom=[None]),
        dict(aanpak="Zet alles in kommagetallen en rangschik dan. Schrijf de omzetting erbij, dan vind je "
                    "een fout terug.",
             waarom=[None]),
        dict(aanpak="Twee vierkante haakjes is gesloten, twee ronde is open, één van elk is halfopen. Een "
                    "interval naar oneindig is altijd minstens halfopen.",
             waarom=[None]),
        dict(aanpak="Zeg eerst waar de fout zit en geef dan de juiste schrijfwijze.",
             waarom=[
                 "Twee keer afronden is de klassieke fout. Kijk naar één cijfer, het eerste dat wegvalt.",
                 None,
             ]),
        dict(aanpak="Antwoord in volle zinnen. Het gaat hier over wat een afgerond getal eigenlijk zegt.",
             waarom=[
                 None,
                 "Dit is waarom een meting altijd een marge heeft. Een getal op het scherm is een bereik, "
                 "geen punt.",
             ]),
        dict(aanpak="Denk aan de getallenas: tussen twee verschillende getallen ligt er altijd nog een.",
             waarom=[
                 None,
                 "Let op het verschil tussen de twee haakjes: met vierkante haakjes hoort \\(4\\) erbij, "
                 "met ronde valt het er net buiten en blijft er niets over.",
             ]),
        dict(aanpak="Ga bij elke uitspraak terug naar de betekenis van het haakje of naar de regel over "
                    "afronden.",
             waarom=[None, None, None]),
        dict(aanpak="Een afronding op honderd gram betekent dat het echte gewicht hoogstens vijftig gram "
                    "van de getoonde waarde afligt.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-rechten-vlakken-en-gelijkvormigheid-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Tel telkens de gemeenschappelijke punten: geen, één, of allemaal. Bij twee rechten "
                    "komt er één vraag bij: liggen ze samen in één vlak.",
             waarom=[
                 "Kruisende rechten zijn het geval dat enkel in de ruimte bestaat: ze snijden niet én ze "
                 "zijn niet evenwijdig. Denk aan een straat en een viaduct erboven.",
             ]),
        dict(aanpak="Een balk en een kubus hebben dezelfde aantallen; enkel de lengtes van de ribben "
                    "verschillen.",
             waarom=[None]),
        dict(aanpak="Drie manieren om een ruimtefiguur op papier te zetten: de ontwikkeling, de drie "
                    "aanzichten en het perspectief.",
             waarom=[
                 None, None,
                 "Juist daarom tekent men in de wiskundeles cavalière: je kan er lengtes op uitzetten die "
                 "in verhouding blijven.",
             ]),
        dict(aanpak="Doorsnede is wat in beide zit, unie is alles samen, en het verschil is wat in de "
                    "eerste zit maar niet in de tweede.",
             waarom=[
                 "Let op het verschil tussen \\(A \\setminus B\\) en \\(B \\setminus A\\): die twee zijn "
                 "niet hetzelfde. De volgorde telt.",
             ]),
        dict(aanpak="Zelfde werkwijze met andere getallen.",
             waarom=[None]),
        dict(aanpak="Drie kenmerken: twee gelijke hoeken (HH), drie evenredige zijden (ZZZ), of twee "
                    "evenredige zijden met de ingesloten hoek gelijk (ZHZ).",
             waarom=[
                 "Voor HH volstaan twee hoeken, want de derde volgt vanzelf uit de som van "
                 "\\(180^\\circ\\).",
             ]),
        dict(aanpak="Onthoud de drie machten: lengte maal \\(k\\), oppervlakte maal \\(k^{2}\\), volume "
                    "maal \\(k^{3}\\). Daarmee los je bijna elke vraag van dit hoofdstuk op.",
             waarom=[None]),
        dict(aanpak="Vermenigvuldig de maat op de tekening met het getal achter de dubbele punt, en reken "
                    "daarna om naar de gevraagde eenheid.",
             waarom=[
                 "Reken altijd in centimeter en zet pas op het einde om. Bij \\(1 : 25\\,000\\) geeft "
                 "\\(12\\) cm \\(300\\,000\\) cm, dus \\(3\\) km.",
             ]),
        dict(aanpak="Zoek eerst de factor \\(k\\), en kies dan de juiste macht: één voor lengte, twee voor "
                    "oppervlakte, drie voor volume of gewicht.",
             waarom=[
                 None,
                 "Gewicht volgt het volume, dus de derde macht. Daarom is een schaalmodel altijd veel "
                 "lichter dan je zou denken.",
                 None,
             ]),
        dict(aanpak="Zelfde werkwijze als de eerste reeks: tel de gemeenschappelijke punten.",
             waarom=[None]),
        dict(aanpak="Past de figuur op een blad, dan is ze vlak. Heeft ze dikte, dan hoort ze in de ruimte.",
             waarom=[None]),
        dict(aanpak="De factor is de nieuwe lengte gedeeld door de oude. Kleiner dan één betekent "
                    "verkleinen.",
             waarom=[None]),
        dict(aanpak="Nu de andere kant op: deel de echte maat door het getal achter de dubbele punt.",
             waarom=[None]),
        dict(aanpak="Zeg eerst wat er fout is en geef dan de juiste redenering.",
             waarom=[
                 "Bij een schaal staat links altijd de tekening en rechts de werkelijkheid. Lees ze als "
                 "één centimeter hier is tweehonderd centimeter daar.",
                 None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en gebruik de machten van \\(k\\) in je uitleg.",
             waarom=[
                 None,
                 "Dit heet het vierkant-kubuswet-probleem, en het verklaart ook waarom een mier wel "
                 "honderd keer haar gewicht draagt en een olifant niet.",
             ]),
        dict(aanpak="Vraag je telkens af welke grootheid er gevraagd wordt: lengte, oppervlakte of volume. "
                    "Dat bepaalt de macht.",
             waarom=[
                 None,
                 "Let op het verschil tussen gelijkvormig en gelijk: dezelfde vorm tegenover dezelfde vorm "
                 "én dezelfde grootte.",
             ]),
        dict(aanpak="Ga bij elke uitspraak terug naar de definitie van gelijkvormigheid of naar de "
                    "betekenis van de schaal.",
             waarom=[None, None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-pythagoras-en-de-rechthoekige-driehoek-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="De schuine zijde ligt tegenover de rechte hoek en is de langste. Je telt de kwadraten "
                    "van de twee andere op en neemt de wortel.",
             waarom=[
                 "Komt er geen mooi getal uit, dan laat je de wortel gewoon staan: \\(\\sqrt{13}\\) is "
                 "exacter dan \\(3{,}61\\).",
             ]),
        dict(aanpak="Zoek je een rechthoekszijde, dan trek je af in plaats van op te tellen. Het kwadraat "
                    "van de schuine zijde staat altijd alleen.",
             waarom=[
                 "Dit is waar het vaakst misloopt: eerst nagaan welke zijde de schuine is, dan pas tellen "
                 "of aftrekken.",
             ]),
        dict(aanpak="Zet de langste zijde apart en kijk of haar kwadraat gelijk is aan de som van de twee "
                    "andere kwadraten. Dat is de omgekeerde stelling.",
             waarom=[None, None, None, None, None]),
        dict(aanpak="De afstand tussen twee punten is Pythagoras op het verschil van de x-en en het "
                    "verschil van de y-en.",
             waarom=[
                 "Een verschil mag negatief zijn, want je kwadrateert het toch. Daarom hoef je niet te "
                 "letten op de volgorde van de punten.",
             ]),
        dict(aanpak="SOSCASTOA: sinus is overstaand op schuin, cosinus aanliggend op schuin, tangens "
                    "overstaand op aanliggend. Kijk welke twee zijden in het spel zijn.",
             waarom=[
                 "Komt de schuine zijde er niet in voor, dan is het altijd de tangens. Dat is de snelste "
                 "manier om te kiezen.",
             ]),
        dict(aanpak="Deze vier formules moet je uit het hoofd kennen. Schrijf ze op het begin van je toets "
                    "in de kantlijn, dan heb je ze de hele tijd bij de hand.",
             waarom=[None, None, None, None]),
        dict(aanpak="De waarden van \\(30^\\circ\\), \\(45^\\circ\\) en \\(60^\\circ\\) komen uit de halve "
                    "gelijkzijdige driehoek en het halve vierkant. Ken je die twee tekeningen, dan hoef je "
                    "de tabel niet vanbuiten te leren.",
             waarom=[
                 "Bij \\(90^\\circ\\) bestaat de tangens niet, want je zou door \\(\\cos 90^\\circ = 0\\) "
                 "moeten delen.",
             ]),
        dict(aanpak="Uit \\(\\sin^{2}\\alpha + \\cos^{2}\\alpha = 1\\) haal je de ene als je de andere "
                    "kent. Bij een scherpe hoek is het antwoord altijd positief.",
             waarom=[None]),
        dict(aanpak="Let bij elke uitspraak op de voorwaarde: rechthoekig, scherp, of zomaar een driehoek.",
             waarom=[
                 "Pythagoras geldt enkel in een rechthoekige driehoek. In een andere driehoek heb je de "
                 "cosinusregel nodig.",
                 None,
                 "Sinus en cosinus liggen altijd tussen \\(-1\\) en \\(1\\), want het zijn verhoudingen "
                 "met de langste zijde in de noemer.",
                 None, None, None, None,
             ]),
        dict(aanpak="Een exact antwoord laat de wortel of de breuk staan. Een benadering heeft een komma "
                    "en is afgerond.",
             waarom=[
                 "Geef in de wiskundeles altijd het exacte antwoord, tenzij er uitdrukkelijk om een "
                 "afronding gevraagd wordt.",
                 None, None,
             ]),
        dict(aanpak="Maak eerst een schets en zet de gegevens erop. Zo zie je meteen welke zijde de schuine "
                    "is.",
             waarom=[
                 None,
                 "Een ruimtediagonaal doe je in twee stappen: eerst de diagonaal van het grondvlak, dan "
                 "Pythagoras met de hoogte erbij.",
             ]),
        dict(aanpak="Schrijf eerst op welke formule je kiest en waarom, dan pas de berekening. Dat is ook "
                    "wat op een toets punten oplevert.",
             waarom=[
                 "Let op de laatste zin: de hoogte die je uitrekent, is de hoogte boven je ogen. Een "
                 "antwoord dat de werkelijkheid teruggeeft, zegt dat erbij.",
                 "Hier gebruik je een letter voor de verhouding. Dat is de aanpak bij elke opgave waar "
                 "enkel een verhouding en een diagonaal gegeven zijn.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-de-rechthoekige-driehoek-oplossen-en-toepassen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="De schuine zijde ligt vast, maar overstaand en aanliggend hangen af van de hoek waar "
                    "je naar kijkt. Zet dus altijd eerst je hoek aan.",
             waarom=[None, None, None]),
        dict(aanpak="Zoek eerst welke zijde overstaand, aanliggend en schuin is, en vul dan de drie breuken "
                    "in volgens SOSCASTOA.",
             waarom=[
                 "De zijde \\(6\\) is de overstaande, \\(8\\) de aanliggende en \\(10\\) de schuine. "
                 "Daarmee liggen de drie breuken vast.",
             ]),
        dict(aanpak="Zelfde werkwijze met een andere driehoek, nu met afronden.",
             waarom=[None]),
        dict(aanpak="Kijk welke twee zijden in het spel zijn. Komt de schuine zijde er niet in voor, dan is "
                    "het de tangens.",
             waarom=[None]),
        dict(aanpak="Zoek je een zijde, dan vermenigvuldig je met de sinus, cosinus of tangens van de hoek. "
                    "Zet je rekenmachine op graden.",
             waarom=[
                 None,
                 "Dat \\(\\sin 30^{\\circ} = 0{,}5\\) is het handigste controlepunt dat er is: de "
                 "overstaande zijde is dan juist de helft van de schuine.",
                 None,
             ]),
        dict(aanpak="Zoek je een hoek, dan reken je eerst de verhouding uit en gebruik je daarna de "
                    "omgekeerde toets op je rekenmachine.",
             waarom=[
                 None,
                 "Zijn de twee rechthoekszijden gelijk, dan is de hoek altijd \\(45^{\\circ}\\). Dat kan je "
                 "zonder rekenmachine zien.",
             ]),
        dict(aanpak="Uit \\(\\sin^{2}\\alpha + \\cos^{2}\\alpha = 1\\) vind je het ene uit het andere.",
             waarom=[None]),
        dict(aanpak="Maak eerst een schets, zet de gegevens erop en kijk welke zijde je kent. Bij een "
                    "kijkhoek vanaf de grond hoort je ooghoogte er nog bij.",
             waarom=[
                 "Vergeet de ooghoogte niet: je meet de hoek vanaf je ogen, niet vanaf je voeten.",
                 None, None,
             ]),
        dict(aanpak="Een hellingspercentage is de tangens, dus de stijging gedeeld door de horizontale "
                    "afstand. Zet het percentage eerst om in een kommagetal.",
             waarom=[
                 None,
                 "Hier reken je omgekeerd: je deelt de hoogte door de helling. Let op de eenheden, "
                 "\\(24\\) cm is \\(0{,}24\\) m.",
             ]),
        dict(aanpak="Let bij elke uitspraak op de grenzen van sinus en cosinus, en op het verschil tussen "
                    "een percentage en een hoek.",
             waarom=[
                 "Sinus en cosinus liggen tussen \\(-1\\) en \\(1\\), want de schuine zijde staat in de "
                 "noemer en is de langste.",
                 "De tangens heeft geen bovengrens: bij een hoek vlak onder \\(90^{\\circ}\\) wordt ze "
                 "enorm.",
                 None,
                 "Tien procent is de tangens, dus ongeveer \\(5{,}7^{\\circ}\\). Een percentage en een "
                 "hoek zijn twee verschillende dingen.",
                 "Je hebt altijd twee gegevens nodig naast de rechte hoek: twee zijden, of een zijde en "
                 "een hoek.",
                 None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en gebruik gelijkvormigheid in je uitleg.",
             waarom=[
                 "Dit is de reden waarom de tabellen van sinus en cosinus überhaupt bestaan: één waarde "
                 "per hoek, voor alle driehoeken samen.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-formules-omvormen-en-eerstegraadsvergelijkingen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Werk haakje voor haakje uit en let op het teken voor het haakje. Neem daarna de "
                    "gelijksoortige termen samen.",
             waarom=[
                 "De drie merkwaardige producten komen hier samen: het kwadraat van een som, van een "
                 "verschil, en het verschil van twee kwadraten. Herken je ze, dan spaar je veel rekenwerk.",
                 "Een minteken voor een haakje keert élke term binnen het haakje om. Daar gaat het meestal "
                 "mis.",
             ]),
        dict(aanpak="Zoek eerst een gemeenschappelijke factor. Lukt dat niet, kijk dan of het een "
                    "merkwaardig product is.",
             waarom=[
                 "\\(x^{2} - 25\\) is het verschil van twee kwadraten, dus \\((x+5)(x-5)\\). Een som van "
                 "twee kwadraten kan je niet ontbinden.",
             ]),
        dict(aanpak="Breng alle \\(x\\)-en naar links en alle getallen naar rechts, en deel dan. Wat je aan "
                    "de ene kant doet, doe je aan de andere.",
             waarom=[None]),
        dict(aanpak="Er is vaak meer dan één goede weg, maar één ervan is korter. Kijk of je eerst kan "
                    "delen voor je haakjes uitwerkt.",
             waarom=[
                 "Delen door \\(3\\) mag hier ook en is korter. Beide wegen geven \\(x = 7\\).",
                 None,
                 "Dit is de regel die je nooit mag vergeten: deel je door een negatief getal, dan draait "
                 "het ongelijkheidsteken om.",
                 None,
             ]),
        dict(aanpak="Vermenigvuldig beide leden met het kleinste gemeen veelvoud van de noemers. Daarna is "
                    "het een gewone vergelijking.",
             waarom=[None]),
        dict(aanpak="Vallen alle \\(x\\)-en weg, kijk dan naar wat er overblijft: een ware uitspraak "
                    "betekent oneindig veel oplossingen, een valse geen enkele.",
             waarom=[None, None]),
        dict(aanpak="Los op zoals een gelijkheid, met één regel erbij: vermenigvuldig of deel je door een "
                    "negatief getal, dan draait het teken om. Schrijf het antwoord ook als interval.",
             waarom=[
                 "Let op de drie met een negatieve coëfficiënt. Daar draait het teken om, en juist daar "
                 "gaan de meeste punten verloren.",
             ]),
        dict(aanpak="Een formule omvormen is hetzelfde als een vergelijking oplossen, met letters in de "
                    "plaats van getallen. Zet de gevraagde letter alleen.",
             waarom=[None, None]),
        dict(aanpak="Vul de gegeven waarden in de omgevormde formule in en zet er de juiste eenheid bij.",
             waarom=[None]),
        dict(aanpak="Schrijf eerst op wat je onbekende voorstelt, dan de vergelijking, dan de oplossing, en "
                    "ten slotte de controle.",
             waarom=[
                 None,
                 "Bij een vergelijking tussen twee tarieven zoek je het punt waar ze gelijk zijn. Daarna "
                 "zeg je in woorden welke kant van dat punt je moet hebben.",
                 "Opeenvolgende even getallen verschillen telkens \\(2\\). Daarom werkt \\(x\\), \\(x+2\\), "
                 "\\(x+4\\).",
             ]),
        dict(aanpak="Een vergelijking is grafisch een snijpunt, een ongelijkheid een stuk van de grafiek "
                    "boven of onder de as.",
             waarom=[None, None]),
        dict(aanpak="Ga bij elke uitspraak terug naar de regels: wat mag je met beide leden doen, en "
                    "wanneer draait een teken om.",
             waarom=[
                 "Het teken draait enkel om bij een negatief getal. Bij een positief blijft alles staan.",
                 None,
                 "Die letter kan nul zijn, en delen door nul mag niet. Daarom splits je zo'n geval altijd "
                 "op.",
                 "De energie hangt af van het kwadraat van de snelheid. Twee keer zo snel is dus vier keer "
                 "zoveel energie.",
                 None,
                 "Het moet \\(-2x + 10\\) zijn: het minteken geldt voor élke term tussen de haakjes.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-stelsels-van-twee-eerstegraadsvergelijkingen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Een koppel is maar een oplossing als het in béide vergelijkingen klopt. Vul dus altijd "
                    "allebei in.",
             waarom=[
                 None,
                 "Hier klopt de eerste wel en de tweede niet. Eén vergelijking die niet uitkomt, volstaat "
                 "om het koppel af te wijzen.",
                 None,
             ]),
        dict(aanpak="Staat er ergens al een onbekende alleen, dan vul je die uitdrukking in de andere "
                    "vergelijking in. Zo blijft er één vergelijking met één onbekende over.",
             waarom=[
                 None,
                 "Vergeet de tweede waarde niet: een stelsel oplossen betekent het hele koppel geven, niet "
                 "enkel \\(x\\).",
             ]),
        dict(aanpak="Staan beide vergelijkingen al in de vorm \\(y = \\ldots\\), dan stel je de twee "
                    "rechterleden aan elkaar gelijk.",
             waarom=[None]),
        dict(aanpak="Tel de twee vergelijkingen op of trek ze van elkaar af, zo dat een onbekende wegvalt. "
                    "Staan de coëfficiënten tegengesteld, dan tel je op.",
             waarom=[
                 "Hier vallen de \\(y\\)-en weg bij optellen, want \\(+y\\) en \\(-y\\) heffen elkaar op.",
                 None,
             ]),
        dict(aanpak="Vergelijk de twee vergelijkingen: zeggen ze hetzelfde, dan is het stelsel onbepaald; "
                    "spreken ze elkaar tegen, dan strijdig; anders bepaald.",
             waarom=[
                 "De tweede is gewoon de eerste maal twee, dus zeggen ze precies hetzelfde. Daarom zijn er "
                 "oneindig veel oplossingen.",
             ]),
        dict(aanpak="Elke vergelijking is een rechte. Het aantal snijpunten is het aantal oplossingen.",
             waarom=[None]),
        dict(aanpak="Vallen alle onbekenden weg, kijk dan naar wat er overblijft: een ware uitspraak "
                    "betekent oneindig veel, een valse geen enkele.",
             waarom=[None]),
        dict(aanpak="Schrijf eerst op waar elke letter voor staat. Daarna vertaal je elke zin in één "
                    "vergelijking.",
             waarom=[
                 "Aftrekken is hier het snelst, want de \\(2s\\) staat in beide vergelijkingen. Zoek altijd "
                 "eerst wat je zonder omweg kan wegwerken.",
                 "Een omtrek van \\(26\\) cm geeft \\(l + b = 13\\), niet \\(26\\). Reken de omtrek dus "
                 "eerst om naar de halve omtrek.",
             ]),
        dict(aanpak="Zelfde werkwijze: eerst de afspraak over je letters, dan het stelsel, dan de controle.",
             waarom=[None, None]),
        dict(aanpak="Let bij elke uitspraak op de volgorde van het koppel en op het aantal mogelijke "
                    "oplossingen.",
             waarom=[
                 "In een koppel staat eerst \\(x\\), dan \\(y\\). \\((2,5)\\) en \\((5,2)\\) zijn dus twee "
                 "verschillende punten.",
                 "Een stelsel kan ook geen of oneindig veel oplossingen hebben. Dat zijn de strijdige en de "
                 "onbepaalde stelsels.",
                 None, None, None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en zeg wat elke vergelijking toevoegt.",
             waarom=[
                 "Eén vergelijking met twee onbekenden is een hele rechte vol oplossingen. Daarom heb je er "
                 "evenveel vergelijkingen nodig als onbekenden.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-functies-en-de-rechte-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Bij een functie hoort bij elke \\(x\\) precies één \\(y\\). De verticalelijntest zegt "
                    "het meteen: snijdt een verticale lijn de grafiek twee keer, dan is het geen functie.",
             waarom=[
                 None,
                 "Een verticale rechte heeft bij één \\(x\\) oneindig veel \\(y\\)-waarden, dus is ze geen "
                 "functie.",
                 None,
                 "Een cirkel heeft bij de meeste \\(x\\)-waarden twee punten, een boven en een onder. "
                 "Daarom valt hij af.",
                 "Een horizontale rechte is wél een functie: bij elke \\(x\\) hoort één \\(y\\), toevallig "
                 "altijd dezelfde.",
             ]),
        dict(aanpak="Vul het getal in voor \\(x\\) en reken uit. Wordt het antwoord gegeven en is \\(x\\) "
                    "gevraagd, dan los je een vergelijking op.",
             waarom=[
                 "Let op de laatste: daar werk je omgekeerd, met \\(5x - 3 = 17\\).",
             ]),
        dict(aanpak="Kijk naar de verschillen tussen de opeenvolgende waarden. Zijn die telkens gelijk, dan "
                    "is de groei lineair.",
             waarom=[None]),
        dict(aanpak="De richtingscoëfficiënt is het verschil van de \\(y\\)-en gedeeld door het verschil "
                    "van de \\(x\\)-en. Hoeveel \\(y\\) stijgt per stap naar rechts.",
             waarom=[
                 "Een rico van nul betekent een horizontale rechte: de \\(y\\) verandert niet.",
             ]),
        dict(aanpak="Het teken van de rico zegt het: positief is stijgen, negatief is dalen.",
             waarom=[None, None]),
        dict(aanpak="Ken je de rico en één punt, vul dan dat punt in \\(y = ax + b\\) in om \\(b\\) te "
                    "vinden. Ken je twee punten, reken dan eerst de rico.",
             waarom=[
                 "Het punt \\((0, b)\\) geeft \\(b\\) meteen weg: daar snijdt de rechte de \\(y\\)-as.",
             ]),
        dict(aanpak="De waarde bij \\(x = 0\\) is \\(b\\), en het vaste verschil per stap is \\(a\\). Zo "
                    "lees je het voorschrift zo uit een tabel.",
             waarom=[None]),
        dict(aanpak="Voor het snijpunt met de \\(x\\)-as zet je \\(y = 0\\), voor dat met de \\(y\\)-as "
                    "\\(x = 0\\).",
             waarom=[None]),
        dict(aanpak="Recht evenredig is het bijzondere geval zonder vast bedrag: de rechte gaat door de "
                    "oorsprong. Staat er een \\(b\\) bij, dan is het enkel lineair.",
             waarom=[None, None, None, None]),
        dict(aanpak="Zeg er altijd bij wat \\(a\\) en \\(b\\) in die situatie betekenen. Dat is wat een "
                    "model van een formule onderscheidt.",
             waarom=[
                 None, None,
                 "Lineair afschrijven betekent elk jaar hetzelfde bedrag: \\(30\\,000 : 12 = 2\\,500\\) "
                 "euro per jaar.",
             ]),
        dict(aanpak="Antwoord in volle zinnen en gebruik de begrippen oorsprong, ijk en rico.",
             waarom=[None, None]),
        dict(aanpak="Ga bij elke uitspraak terug naar de definitie van een functie of naar de betekenis van "
                    "\\(a\\) en \\(b\\).",
             waarom=[
                 None, None, None,
                 "Delen door nul mag niet, dus hoort \\(0\\) niet bij het domein. Dat is net wat een domein "
                 "doet: zeggen welke \\(x\\)-waarden mogen.",
                 "Bij \\(y = x^{2}\\) geven \\(2\\) en \\(-2\\) allebei \\(4\\). Dat mag: één \\(y\\) bij "
                 "twee \\(x\\)-en is geen probleem, omgekeerd wel.",
                 "De afhankelijke variabele staat op de \\(y\\)-as, want haar waarde volgt uit de \\(x\\).",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-tekenverloop-verloopschema-en-grafisch-oplossen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="De nulwaarde is de \\(x\\) waarvoor de functiewaarde nul is. Zet het voorschrift "
                    "gelijk aan nul en los op.",
             waarom=[None]),
        dict(aanpak="Let op het verschil: de nulwaarde is een \\(x\\), het snijpunt met de \\(y\\)-as is "
                    "een functiewaarde. Voor het tweede vul je \\(x = 0\\) in.",
             waarom=[None, None]),
        dict(aanpak="Zet de nulwaarde op de as en kijk aan welke kant de rechte boven en onder de as ligt. "
                    "Een stijgende rechte is rechts van haar nulwaarde positief.",
             waarom=[
                 "Bij een dalende rechte draait alles om: dan staat het plus links. Kijk dus altijd eerst "
                 "naar het teken van de rico.",
             ]),
        dict(aanpak="Het verloopschema volgt enkel uit het teken van de rico: positief is stijgend, "
                    "negatief is dalend.",
             waarom=[None]),
        dict(aanpak="Een vierkant haakje betekent dat de grens meedoet, een rond haakje niet. Bij oneindig "
                    "staat het haakje altijd open.",
             waarom=[None]),
        dict(aanpak="Een vol bolletje betekent dat de grens meetelt, een open bolletje niet. Dat komt "
                    "overeen met het soort haakje.",
             waarom=[None, None]),
        dict(aanpak="Twee grafieken vergelijken doe je door ze gelijk te stellen. De oplossing van de "
                    "ongelijkheid is dan de kant van dat snijpunt waar de ene boven de andere ligt.",
             waarom=[
                 None,
                 "Kijk na het snijpunt welke rechte het snelst stijgt. \\(f\\) heeft rico \\(2\\) en \\(g\\) "
                 "rico \\(1\\), dus ligt \\(f\\) erboven vanaf \\(x = 3\\).",
             ]),
        dict(aanpak="Het break-evenpunt is waar kosten en opbrengst elkaar snijden. Daarna reken je in hele "
                    "stuks verder.",
             waarom=[
                 None,
                 "Bij precies tien stuks is de winst nog nul. Daarom begint de winst pas bij het elfde "
                 "stuk, en zegt het antwoord elf en niet tien.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen het téken van de functiewaarde en het "
                    "verloop van de grafiek.",
             waarom=[
                 "Een stijgende rechte is links van haar nulwaarde negatief. Stijgen en positief zijn twee "
                 "verschillende dingen.",
                 "Een horizontale rechte op hoogte \\(5\\) raakt de \\(x\\)-as nooit, dus is er geen "
                 "nulwaarde.",
                 None,
                 "Twee verschillende rechten snijden elkaar hoogstens één keer, of ze zijn evenwijdig en "
                 "snijden nooit.",
                 None,
                 "Dat doet het verloopschema. Een tekenverloop zegt enkel waar de functie boven of onder de "
                 "as ligt.",
             ]),
        dict(aanpak="Antwoord in volle zinnen en gebruik de woorden teken, verloop en nulwaarde.",
             waarom=[None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-telproblemen-met-boom-en-venndiagram-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Bij keuzes die na elkaar komen, vermenigvuldig je het aantal mogelijkheden van elke "
                    "stap. Dat is de productregel.",
             waarom=[
                 None,
                 "Let op het aantal tekens per plaats: drie letters uit \\(26\\) en drie cijfers uit "
                 "\\(10\\), dus \\(26^{3} \\cdot 10^{3}\\).",
             ]),
        dict(aanpak="Zijn alle stappen gelijk, dan wordt de productregel een macht: het aantal "
                    "mogelijkheden tot de macht het aantal stappen.",
             waarom=[None]),
        dict(aanpak="Teken vanuit één beginpunt een tak per mogelijkheid, en laat elke tak opnieuw "
                    "splitsen. Het aantal uiteinden is het aantal mogelijkheden.",
             waarom=[None]),
        dict(aanpak="Mag hetzelfde opnieuw gekozen worden, dan blijft het aantal gelijk; mag het niet, dan "
                    "daalt het met één per stap.",
             waarom=[
                 "Vergelijk de eerste twee: \\(6 \\cdot 5 \\cdot 4\\) tegenover \\(6 \\cdot 6 \\cdot 6\\). "
                 "Of er teruggelegd wordt, verandert heel de berekening.",
             ]),
        dict(aanpak="Bij twee groepen die overlappen tel je op en trek je de doorsnede er één keer af, "
                    "anders tel je die dubbel.",
             waarom=[None]),
        dict(aanpak="Wie aan geen van beide voldoet, vind je door het totaal min wie aan minstens één "
                    "voldoet.",
             waarom=[None]),
        dict(aanpak="Enkel de ene groep is die groep min de doorsnede. Het getal in de cirkel bevat altijd "
                    "ook de overlap.",
             waarom=[None]),
        dict(aanpak="Vul een venndiagram altijd van binnen naar buiten: eerst het midden, dan de twee "
                    "stukken ernaast, dan wat buiten de cirkels valt.",
             waarom=[
                 "Begin met de \\(6\\) in het midden: \\(15 - 6 = 9\\) voor enkel voetbal en \\(13 - 6 = "
                 "7\\) voor enkel basket, en \\(28 - 22 = 6\\) blijft over.",
             ]),
        dict(aanpak="Vier tekens om te kennen: doorsnede, vereniging, aantal elementen, en de lege "
                    "verzameling.",
             waarom=[None]),
        dict(aanpak="Dezelfde somregel, nu in tekens. Je kan ze ook omgekeerd gebruiken om de doorsnede te "
                    "vinden.",
             waarom=[
                 "De derde werkt omgekeerd: \\(18 + 20 - 30 = 8\\). Zo vind je hoeveel er in beide groepen "
                 "zitten.",
             ]),
        dict(aanpak="Zoek eerst welke regel past: overlappen de groepen, dan de somregel; is het tegendeel "
                    "makkelijker te tellen, dan de complementregel.",
             waarom=[
                 "Vergeet de getallen die door allebei deelbaar zijn niet: \\(10\\), \\(20\\) en \\(30\\) "
                 "zitten in beide lijstjes.",
                 "Minstens één is bijna altijd makkelijker via het tegendeel: geen enkele. Dat is één geval "
                 "in plaats van zeven.",
             ]),
        dict(aanpak="Opeenvolgende keuzes vragen een boomdiagram, overlappende groepen een venndiagram.",
             waarom=[None, None, None]),
        dict(aanpak="Ga bij elke uitspraak na of de groepen overlappen en of de keuzes na elkaar komen.",
             waarom=[
                 "Dan tel je de mensen in de overlap twee keer. Daarom staat er een min in de somregel.",
                 None, None,
                 "Dat is net het boomdiagram. Een venndiagram dient voor groepen die elkaar overlappen.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-statistiek-voorstellingen-centrum-en-spreiding-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Kan je ermee rekenen, dan is het numeriek. Zijn het groepen, vraag je dan af of er een "
                    "natuurlijke volgorde in zit.",
             waarom=[
                 "Zwak, voldoende en goed hebben een volgorde, kleuren niet. Dat verschil bepaalt welke "
                 "maten en welke diagrammen mogen.",
             ]),
        dict(aanpak="Een relatieve frequentie is het aantal gedeeld door het totaal. Maal honderd geeft het "
                    "percentage.",
             waarom=[None]),
        dict(aanpak="Deel elk aantal door het totaal en vermenigvuldig met honderd. De som moet altijd "
                    "honderd procent geven; dat is je controle.",
             waarom=[None]),
        dict(aanpak="Het klassenmidden is het gemiddelde van de twee grenzen. Je gebruikt het als de ene "
                    "waarde die heel die klasse vertegenwoordigt.",
             waarom=[None]),
        dict(aanpak="Kies het diagram naar wat je wil tonen: een verloop in de tijd, een aandeel in een "
                    "geheel, een verdeling in klassen, of de spreiding.",
             waarom=[
                 "Een cirkeldiagram toont enkel aandelen van één geheel. Wil je een verloop tonen, dan is "
                 "het nooit de juiste keuze.",
             ]),
        dict(aanpak="Deze tekens komen in elke opgave terug. Let op het verschil tussen \\(\\sigma\\) en de "
                    "interkwartielafstand: allebei spreiding, maar op een andere manier gemeten.",
             waarom=[None]),
        dict(aanpak="Rangschik eerst van klein naar groot. Het gemiddelde reken je uit, de mediaan ligt in "
                    "het midden, de modus komt het vaakst voor.",
             waarom=[
                 "Bij een even aantal waarden is de mediaan het gemiddelde van de twee middelste. Hier dus "
                 "\\(8\\) en niet \\(7\\) of \\(9\\).",
             ]),
        dict(aanpak="Zelfde werkwijze met een oneven aantal waarden.",
             waarom=[
                 "Bij een oneven aantal is er één middelste waarde en hoef je niets te middelen.",
             ]),
        dict(aanpak="Tel eerst het aantal waarden. Oneven geeft één middelste, even geeft het gemiddelde "
                    "van de twee middelste.",
             waarom=[None]),
        dict(aanpak="\\(Q_{2}\\) is de mediaan; \\(Q_{1}\\) is de mediaan van de onderste helft en "
                    "\\(Q_{3}\\) die van de bovenste helft.",
             waarom=[
                 "Splits de reeks in twee helften van vier en zoek in elke helft de mediaan: \\(5\\) en "
                 "\\(13\\).",
             ]),
        dict(aanpak="Zitten er uitschieters in, dan geeft de mediaan het eerlijkste beeld. Liggen de "
                    "waarden dicht bij elkaar, dan mag het gemiddelde.",
             waarom=[
                 "Dit is het klassieke voorbeeld: één groot loon trekt het gemiddelde boven dat van bijna "
                 "iedereen. Daarom spreekt men over het mediaanloon.",
                 None,
             ]),
        dict(aanpak="De standaardafwijking zegt hoe ver de waarden gemiddeld van het gemiddelde liggen. "
                    "Klein is dicht bijeen, groot is ver uiteen.",
             waarom=[
                 "Twee reeksen met hetzelfde gemiddelde kunnen er heel anders uitzien. Daarom hoort er bij "
                 "een centrummaat altijd een spreidingsmaat.",
                 None,
             ]),
        dict(aanpak="Ga bij elke uitspraak na of het over het centrum of over de spreiding gaat, en of de "
                    "gegevens numeriek of categorisch zijn.",
             waarom=[
                 "In een histogram staan de klassen naast elkaar op een doorlopende as, dus raken de "
                 "staven elkaar. In een staafdiagram staat er ruimte tussen.",
                 None,
                 "Juist niet: \\(Q_{3} - Q_{1}\\) kijkt enkel naar de middelste helft, dus een uitschieter "
                 "valt erbuiten.",
                 None, None,
                 "De modus is de enige centrummaat die ook bij kleuren of merken werkt, want je hoeft er "
                 "niet mee te rekenen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-misleiding-met-cijfers-en-grafieken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Kijk bij elke grafiek eerst naar de assen: waar begint de verticale as, en staan de "
                    "stappen op de horizontale as even ver uit elkaar.",
             waarom=[
                 "Een as die niet bij nul begint is de meest voorkomende truc. Het is niet verboden, maar "
                 "het hoort er duidelijk bij te staan.",
                 None,
                 "Dit komt terug bij elke tekening die een getal uitbeeldt: de ogen zien oppervlakte, en "
                 "die groeit met het kwadraat.",
             ]),
        dict(aanpak="Procentpunt is het verschil tussen twee percentages, procent is de relatieve stijging "
                    "ervan. Zeg altijd welke van de twee je bedoelt.",
             waarom=[
                 "Van \\(20\\) naar \\(25\\) is \\(5\\) procentpunt, maar \\(5 : 20 = 25\\,\\%\\) relatief. "
                 "Hetzelfde cijfer, twee heel verschillende getallen.",
             ]),
        dict(aanpak="Reken twee percentages na elkaar altijd stap voor stap uit. Ze optellen mag niet, want "
                    "het tweede percentage gaat over een kleiner bedrag.",
             waarom=[
                 None,
                 "Hier zie je het omgekeerde: \\(25\\,\\%\\) erbij en daarna \\(20\\,\\%\\) eraf brengt je "
                 "precies terug. Een stijging en een daling van hetzelfde percentage heffen elkaar niet op.",
             ]),
        dict(aanpak="Reken allebei uit en kijk hoe ver ze uit elkaar liggen. Dat verschil is zelf al een "
                    "aanwijzing dat er een uitschieter in zit.",
             waarom=[
                 "Het gemiddelde ligt hier hoger dan vier van de vijf waarden. Dat is het teken dat het "
                 "gemiddelde hier niets beschrijft.",
                 None, None,
             ]),
        dict(aanpak="Lees een krantenkop letterlijk en vraag je af wat er precies beweerd wordt en wat niet.",
             waarom=[
                 "Tot vijftig procent zegt enkel iets over het maximum. Eén artikel met die korting "
                 "volstaat om de zin waar te maken.",
                 "Een groei van \\(300\\,\\%\\) betekent drie keer de winst erbij, dus vier keer zoveel. "
                 "Verdrievoudigen zou \\(200\\,\\%\\) groei zijn.",
                 "Een verdubbeling van een heel klein risico blijft een klein risico. Zonder het beginpunt "
                 "zegt een relatieve stijging niets.",
             ]),
        dict(aanpak="Vraag je af wie je door je manier van vragen al bij voorbaat uitsluit. Dat is wat een "
                    "steekproef scheeftrekt.",
             waarom=[None, None]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen een cijfer dat klopt en een beeld dat "
                    "klopt.",
             waarom=[
                 None, None,
                 "Dit is de kern van heel het hoofdstuk: misleiden kan met cijfers die allemaal juist zijn.",
                 None, None,
                 "Zonder het aantal weet je niet of een percentage over twee mensen of over tweeduizend "
                 "gaat.",
             ]),
        dict(aanpak="Antwoord in volle zinnen en noem telkens wat er ontbreekt om het cijfer te kunnen "
                    "beoordelen.",
             waarom=[None, None]),
    ],
)
