# -*- coding: utf-8 -*-
"""De leerbundels voor geschiedenis op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche geschiedenis 2de graad dubbele finaliteit, geldig
vanaf 1 januari 2027. Die fiche overlapt voor ongeveer 85 % met de
doorstroomfiche: dezelfde periodes, dezelfde samenlevingen, dezelfde
structuurbegrippen. Daarom bouwen we de bundels hier niet opnieuw, maar nemen
we die van doorstroom over en zetten we de verschillen er in.

Wat de dubbele finaliteit **niet** vraagt en hier dus uit gaat: de
geldeconomie, het handelskapitalisme, het mercantilisme, het
encomiendasysteem, het zelfvoorzienende domein en de nieuwe wetenschappelijke
methode. Wat ze **wel** vraagt en de doorstroombundel niet had: de lokale,
regionale en langeafstandshandel, de verwevenheid van stad en platteland,
Bagdad als kruispunt van internationale handel, de vernieuwingen in het
financiële verkeer, het drietal handelscompagnie – manufactuur –
huisnijverheid, het verband tussen landbouwproductiviteit en technische
vernieuwingen, het vergelijken van standpunten over slavenhandel in
verschillende bronnen, en de vormen van intercultureel contact tussen moslims
en christenen.

Die verschillen staan hieronder in PATCHES, één regel per ingreep, met de
tekst waarop ze aanhaakt. Elke ingreep moet precies één blok raken; raakt ze er
geen of meerdere, dan stopt het script. Zo kan een aanpassing aan de
doorstroombundel hier nooit stil voorbijgaan.

De sleutels eindigen op "-boost-dubbele-finaliteit", de volledige naam van de
categorie, net zoals bij doorstroom. De vragen komen uit
`../../boost-dubbele-finaliteit/geschiedenis.json`.
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import maak_geschiedenis_boost as doorstroom

VAK = "Geschiedenis"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"

# ─────────────────────────────────────────────────────────────
# De ingrepen. Elke regel is (sleutel, haak, wat, blokken):
#   haak    een stuk tekst dat in precies één blok van die bundel staat
#   wat     "vervang" het blok, "na" het blok, of "schrap-sectie" de hele sectie
# ─────────────────────────────────────────────────────────────
PATCHES = [
    # ── 3. Standen, domein en stad
    (
        "standen-domein-en-stad",
        "Het domein was <strong>zelfvoorzienend</strong>",
        "vervang",
        [],
    ),
    (
        "standen-domein-en-stad",
        "Op de <strong>lokale markt</strong> verhandelde men",
        "na",
        [
            ("p", "Handel bestaat op drie niveaus. <strong>Lokale handel</strong> is de wekelijkse markt: "
                  "brood van de bakker om de hoek, groenten van de boer uit het dorp. "
                  "<strong>Regionale handel</strong> gaat van stad tot stad binnen een streek. "
                  "<strong>Langeafstandshandel</strong> brengt goederen die de lange reis waard zijn: "
                  "specerijen uit Azië, zijde, zilver. Duur, licht en zeldzaam, want alleen dan weegt de "
                  "winst op tegen de reis."),
        ],
    ),
    (
        "standen-domein-en-stad",
        "Met de stad komt de <strong>geldeconomie</strong> op",
        "vervang",
        [
            ("p", "De <strong>ambachten en gilden</strong> horen in de eerste plaats in het "
                  "<strong>economische</strong> maatschappelijk domein thuis: ze gaan over werken, "
                  "produceren en verkopen. Ze regelden mee <strong>wie in de stad een beroep mocht "
                  "uitoefenen</strong>, hoeveel leerjongens je mocht hebben en welke kwaliteit je werk moest "
                  "halen. Dat een gilde daarnaast ook een altaar in de kerk onderhield en een eigen feestdag "
                  "vierde, maakt haar ook cultureel."),
        ],
    ),
    # ── 4. Geloof, kunst en macht in de middeleeuwen
    (
        "geloof-kunst-en-macht-in-de-middeleeuwen",
        "De <strong>zijderoutes</strong> zijn de handelswegen",
        "na",
        [
            ("p", "Op een kaart zie je meteen waarom <strong>Bagdad</strong> in de middeleeuwen een "
                  "<strong>kruispunt van internationale handel</strong> was: de zijderoutes uit het oosten, "
                  "de wegen naar de Middellandse Zee en de route langs de Perzische Golf naar Indië komen er "
                  "samen. Wie daar zit, ziet alles passeren en heft tol op alles wat passeert."),
        ],
    ),
    # ── 5. De 'Nieuwe' Wereld en de driehoekshandel
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Het <strong>encomiendasysteem</strong> is het Spaanse systeem",
        "vervang",
        [],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "het <strong>encomiendasysteem</strong> en",
        "vervang",
        [
            ("kader", "De <strong>demografische inzinking</strong> van de precolumbiaanse bevolking, de "
                      "<strong>Afro-Amerikaanse slavenhandel</strong> en de <strong>driehoekshandel</strong> "
                      "hangen samen: stierf de inheemse bevolking weg, dan viel de arbeidskracht in de "
                      "kolonies weg, terwijl de mijnen en de velden bleven. Die arbeid werd dan van elders "
                      "gehaald, uit Afrika, en zo draaide de driehoekshandel."),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "De driehoekshandel toont hoe het <strong>economische</strong>",
        "na",
        [
            ("p", "Op het examen kan je <strong>het standpunt over slavenhandel in verschillende bronnen "
                  "vergelijken</strong>. Twee bronnen die elkaar tegenspreken, betekent niet dat er één "
                  "liegt. Ga van elke bron na <strong>wie ze maakte en met welke bedoeling</strong>, en weeg "
                  "de twee standpunten dan tegen elkaar af. Een slavenhandelaar die over zijn winst schrijft "
                  "en een tot slaaf gemaakte die over de overtocht vertelt, schrijven allebei de waarheid van "
                  "hun kant. Wie ze naast elkaar legt, ziet net daarom meer."),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Kenmerken van het <strong>handelskapitalisme</strong>",
        "vervang",
        [
            ("p", "Er zijn drie <strong>organisatievormen van ondernemingen</strong>: de "
                  "<strong>handelscompagnie</strong>, de <strong>manufactuur</strong> en de "
                  "<strong>huisnijverheid</strong>. Een fabriek die volledig van de staat is, hoort er niet "
                  "bij; dat is een veel latere vorm."),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Het <strong>mercantilisme</strong> houdt in",
        "vervang",
        [],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "In de vroegmoderne tijd komen ook <strong>wisselbrieven</strong>",
        "vervang",
        [
            ("p", "Er komen ook <strong>nieuwe betaalmiddelen</strong>: dat zijn de "
                  "<strong>vernieuwingen in het financiële verkeer</strong>. De belangrijkste zijn de "
                  "<strong>wisselbrieven</strong>. Een <strong>wisselbrief</strong> is een papier waarmee je "
                  "in de ene stad betaalt en in de andere "
                  "het geld ophaalt, zodat een handelaar geen zak munten meer hoeft mee te zeulen over "
                  "onveilige wegen. Daarnaast komen <strong>banken</strong> en <strong>beurzen</strong> op; de "
                  "beurs van Antwerpen, en later Amsterdam, maakt handel mogelijk zonder dat de koopman zelf "
                  "mee moet reizen. Daaruit groeit het bankwezen."),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Het verband tussen de <strong>ontdekkingsreizen</strong> en het handelskapitalisme",
        "vervang",
        [],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Ook in de landbouw komen <strong>technische vernieuwingen</strong>",
        "na",
        [
            ("kader", "Het verband tussen de <strong>landbouwproductiviteit</strong> en de "
                      "<strong>technische vernieuwingen</strong>: betere werktuigen en betere methodes laten "
                      "<strong>dezelfde grond meer opbrengen</strong>. Een andere ploeg, een ander "
                      "vruchtwisselstelsel, een nieuw gewas: telkens haalt dezelfde akker meer voedsel op, en "
                      "telkens kunnen er meer monden mee gevoed worden."),
        ],
    ),
    # ── 6. Humanisme, Reformatie, renaissance en barok
    ("humanisme-reformatie-renaissance-en-barok", "Een nieuwe wetenschappelijke methode", "schrap-sectie", []),
    (
        "humanisme-reformatie-renaissance-en-barok",
        "Het <strong>anglicanisme</strong> ontstond niet uit een geloofsdiscussie",
        "na",
        [
            ("kader", "De Reformatie kent drie <strong>stromingen</strong>: het "
                      "<strong>lutheranisme</strong>, het <strong>anglicanisme</strong> en het "
                      "<strong>calvinisme</strong>. De <strong>Contrareformatie</strong> is er géén van: "
                      "dat is juist het antwoord van de katholieke Kerk op de Reformatie."),
        ],
    ),
    # ── 9. Het Ottomaanse Rijk en samenlevingen vergelijken
    (
        "het-ottomaanse-rijk-en-samenlevingen-vergelijken",
        "<strong>Economische systemen</strong> die je naast elkaar",
        "vervang",
        [
            ("p", "Het <strong>interculturele contact tussen moslims en christenen</strong> liep langs drie "
                  "wegen: de <strong>zijderoutes</strong>, de ontmoeting tussen de <strong>Arabische "
                  "cultuur</strong> en de <strong>cultuur van christelijk Europa</strong>, en de "
                  "<strong>kruistochten</strong>. Het waren dus niet alleen wapens: er ging ook wiskunde, "
                  "sterrenkunde en geneeskunde mee, en de Griekse geleerdheid kwam via Arabische vertalingen "
                  "terug in Europa. De ontdekkingsreizen naar Amerika horen hier niet bij, die zijn van later "
                  "en van een heel andere ontmoeting."),
        ],
    ),
]

# Losse woorden diep in een tabel of een opsomming. (oud, nieuw, hoe vaak).
TEKSTFIXES = [
    ("de geldeconomie, e-commerce", "de handel, e-commerce", 1),
]

# De ondertitel van bundel 3 noemt het zelfvoorzienende domein; dat begrip valt weg.
ONDERTITELS = {
    "standen-domein-en-stad": "De gelaagde samenleving, de agrarische samenleving en de heropbloei van de steden.",
}

VERBODEN = [
    "geldeconomie",
    "mercantilis",
    "handelskapitalis",
    "encomienda",
    "zelfvoorzienend",
    "wetenschappelijke methode",
]


def tekst_van(blok) -> str:
    return " ".join(str(d) for d in blok[1:])


def pas_toe(bundels: dict):
    for kort, haak, wat, nieuw in PATCHES:
        sleutel = kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        secties = bundels[sleutel]["secties"]
        if wat == "schrap-sectie":
            raak = [i for i, s in enumerate(secties) if s["kop"] == haak]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} secties heten {haak!r}, verwacht 1")
            secties.pop(raak[0])
            continue
        raak = [
            (i, j)
            for i, s in enumerate(secties)
            for j, b in enumerate(s["blokken"])
            if haak in tekst_van(b)
        ]
        if len(raak) != 1:
            raise SystemExit(f"{sleutel}: {len(raak)} blokken bevatten {haak!r}, verwacht 1")
        i, j = raak[0]
        if wat == "vervang":
            secties[i]["blokken"][j : j + 1] = nieuw
        elif wat == "na":
            secties[i]["blokken"][j + 1 : j + 1] = nieuw
        else:
            raise SystemExit(f"Onbekende ingreep: {wat}")


def fix_teksten(ding, oud: str, nieuw: str) -> tuple:
    """Vervangt oud door nieuw, hoe diep het ook zit, en telt hoe vaak."""
    if isinstance(ding, str):
        return ding.replace(oud, nieuw), ding.count(oud)
    if isinstance(ding, dict):
        aantal = 0
        for k, v in ding.items():
            ding[k], n = fix_teksten(v, oud, nieuw)
            aantal += n
        return ding, aantal
    if isinstance(ding, (list, tuple)):
        stuks, aantal = [], 0
        for v in ding:
            v, n = fix_teksten(v, oud, nieuw)
            stuks.append(v)
            aantal += n
        return type(ding)(stuks), aantal
    return ding, 0


def bouw() -> dict:
    uit = {}
    for sleutel, b in doorstroom.BUNDELS.items():
        if not sleutel.endswith(OUD):
            raise SystemExit(f"Doorstroomsleutel zonder categorie: {sleutel}")
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        uit[sleutel[: -len(OUD)] + NIEUW] = nieuw
    pas_toe(uit)
    for oud, nieuw, hoevaak in TEKSTFIXES:
        uit, aantal = fix_teksten(uit, oud, nieuw)
        if aantal != hoevaak:
            raise SystemExit(f"{oud!r} staat {aantal} keer in de bundels, verwacht {hoevaak}")
    for kort, onder in ONDERTITELS.items():
        uit[kort + NIEUW]["onder"] = onder
    for sleutel, b in uit.items():
        alles = " ".join(
            [b["onder"]]
            + [s["kop"] for s in b["secties"]]
            + [tekst_van(blok) for s in b["secties"] for blok in s["blokken"]]
            + list(b.get("onthoud", []))
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{sleutel} gebruikt nog {woord!r}, dat staat niet op de DF-fiche")
    return uit


BUNDELS = bouw()
