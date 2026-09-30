# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij geschiedenis 🚀 Boost dubbele finaliteit.

Net als bij de leerbundels nemen we de doorstroomversie over en zetten we er de
verschillen in; zie `maak_geschiedenis_df.py` voor waarom. De ingrepen hangen
aan een stuk tekst van de oefening die ze raken, en elke ingreep moet precies
één oefening raken. Verandert er iets aan de doorstroombundel, dan stopt dit
script in plaats van er stil overheen te gaan.

De sleutels dragen het voorvoegsel "oefenbundel-" en eindigen op
"-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import maak_oefeningen_geschiedenis_boost as doorstroom
import maak_geschiedenis_df as leerbundels

VAK = "Geschiedenis"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"
W, WW, WL = "120px", "185px", "250px"

# (sleutel zonder voorvoegsel en categorie, haak, wat, oefeningen)
PATCHES = [
    # ── 3. Standen, domein en stad
    (
        "standen-domein-en-stad",
        "In welk maatschappelijk domein hoort het ontstaan van de geldeconomie",
        "vervang",
        [
            ("open", "In welk maatschappelijk domein horen de ambachten en gilden in de eerste plaats "
                     "thuis, en welk ander domein raken ze ook? Leg uit.",
             "In de eerste plaats economisch: ze gaan over werken, produceren en verkopen, en ze regelen "
                     "wie een beroep mag uitoefenen. Ze raken ook het culturele domein, want een gilde "
                     "onderhield een altaar in de kerk en vierde een eigen feestdag.", 6),
        ],
    ),
    (
        "standen-domein-en-stad",
        "Stad en platteland stonden in de middeleeuwen volledig los van elkaar.",
        "na",
        [
            ("kies", "Welk product hoort bij de langeafstandshandel en niet bij de lokale handel?",
             ["specerijen uit Azië", "brood van de bakker om de hoek",
              "groenten van de boer uit het dorp"], 0),
        ],
    ),
    # ── 5. De 'Nieuwe' Wereld en de driehoekshandel
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Hoe heet het systeem waarbij een kolonist arbeid mocht opeisen",
        "vervang",
        [
            ("kort", "Onder welke twee vlaggen voer de eerste kolonisatiegolf?",
             "onder Spaanse en Portugese vlag", "260px"),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Leg uit hoe de demografische inzinking, het encomiendasysteem",
        "vervang",
        [
            ("open", "Leg uit hoe de demografische inzinking van de precolumbiaanse bevolking, de "
                     "Afro-Amerikaanse slavenhandel en de driehoekshandel samenhangen. Schrijf het als "
                     "een ketting.",
             "De inheemse bevolking sterft grotendeels weg. Daardoor valt de arbeidskracht in de kolonies "
                     "weg, terwijl de mijnen en de velden blijven. Die arbeid wordt dan van elders "
                     "gehaald, uit Afrika, en dat is het been van de driehoekshandel tussen Afrika en "
                     "Amerika.", 6),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Hoe heet de oversteek van Afrika naar Amerika?",
        "na",
        [
            ("open", "Twee bronnen geven een heel ander standpunt over de slavenhandel: een handelaar "
                     "schrijft over zijn winst, een tot slaaf gemaakte vertelt over de overtocht. Wat doe "
                     "je met dat verschil?",
             "Je gooit er geen van beide weg. Je gaat van elke bron na wie ze maakte en met welke "
                     "bedoeling, en je weegt de twee standpunten tegen elkaar af. Ze schrijven allebei de "
                     "waarheid van hun kant; wie ze naast elkaar legt, ziet net daarom meer.", 6),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "meer uitvoeren dan invoeren, om edelmetaal binnen te halen",
        "vervang",
        [
            ("rij", [("een papier waarmee je hier betaalt en daar het geld ophaalt", "een wisselbrief"),
                     ("een handelaar levert grondstof aan gezinnen die thuis werken", "huisnijverheid"),
                     ("arbeiders werken samen op één plaats, onder toezicht", "een manufactuur"),
                     ("het kapitaal is in verhandelbare delen verdeeld", "een handelscompagnie")],
             "Welk begrip?", WL),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Noem drie kenmerken van het handelskapitalisme.",
        "vervang",
        [
            ("open", "Welke drie organisatievormen van ondernemingen horen bij de commerciële "
                     "revolutie? Zet er bij elk in één zin bij wat ze is.",
             "De handelscompagnie: het kapitaal is in verhandelbare delen verdeeld. De manufactuur: de "
                     "arbeiders werken samen op één plaats, onder toezicht, nog altijd met de hand. De "
                     "huisnijverheid: een handelaar levert grondstof aan gezinnen die thuis werken.", 6),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Het mercantilisme wil vrije handel met alle landen.",
        "vervang",
        [
            ("waar", "Bij huisnijverheid werken de arbeiders samen in één grote fabriek van de "
                     "ondernemer.", False),
            ("open", "Wat is het verband tussen de landbouwproductiviteit en de technische "
                     "vernieuwingen?",
             "Betere werktuigen en betere methodes laten dezelfde grond meer opbrengen. Een andere ploeg, "
                     "een ander vruchtwisselstelsel of een nieuw gewas: telkens haalt dezelfde akker meer "
                     "voedsel op, en telkens kunnen er meer monden mee gevoed worden.", 5),
        ],
    ),
    # ── 6. Humanisme, Reformatie, renaissance en barok
    ("humanisme-reformatie-renaissance-en-barok", "Een nieuwe wetenschappelijke methode", "schrap-sectie", []),
    # ── 9. Het Ottomaanse Rijk en samenlevingen vergelijken
    (
        "het-ottomaanse-rijk-en-samenlevingen-vergelijken",
        "Waarom werk je met vaste kenmerken en niet zomaar met wat opvalt?",
        "na",
        [
            ("open", "Langs welke drie wegen liep het contact tussen moslims en christenen?",
             "De zijderoutes, de ontmoeting tussen de Arabische cultuur en de cultuur van christelijk "
                     "Europa, en de kruistochten.", 4),
        ],
    ),
]

VERBODEN = leerbundels.VERBODEN


def tekst_van(oef) -> str:
    return " ".join(str(d) for d in oef)


def pas_toe(bundels: dict):
    for kort, haak, wat, nieuw in PATCHES:
        sleutel = "oefenbundel-" + kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        reeksen = bundels[sleutel]["reeksen"]
        if wat == "schrap-sectie":
            raak = [i for i, r in enumerate(reeksen) if r["kop"] == haak]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} reeksen heten {haak!r}, verwacht 1")
            reeksen.pop(raak[0])
            continue
        raak = [
            (i, j)
            for i, r in enumerate(reeksen)
            for j, o in enumerate(r["oefeningen"])
            if haak in tekst_van(o)
        ]
        if len(raak) != 1:
            raise SystemExit(f"{sleutel}: {len(raak)} oefeningen bevatten {haak!r}, verwacht 1")
        i, j = raak[0]
        if wat == "vervang":
            reeksen[i]["oefeningen"][j : j + 1] = nieuw
        elif wat == "na":
            reeksen[i]["oefeningen"][j + 1 : j + 1] = nieuw
        else:
            raise SystemExit(f"Onbekende ingreep: {wat}")


def bouw() -> dict:
    uit = {}
    for sleutel, b in doorstroom.OEFENBUNDELS.items():
        if not sleutel.endswith(OUD):
            raise SystemExit(f"Doorstroomsleutel zonder categorie: {sleutel}")
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        uit[sleutel[: -len(OUD)] + NIEUW] = nieuw
    pas_toe(uit)
    for sleutel, b in uit.items():
        alles = " ".join(
            [b["onder"]]
            + list(b.get("hoe", []))
            + [r["kop"] + " " + r.get("opdracht", "") for r in b["reeksen"]]
            + [tekst_van(o) for r in b["reeksen"] for o in r["oefeningen"]]
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{sleutel} gebruikt nog {woord!r}, dat staat niet op de DF-fiche")
    return uit


OEFENBUNDELS = bouw()
