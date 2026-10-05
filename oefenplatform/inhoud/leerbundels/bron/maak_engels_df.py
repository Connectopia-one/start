# -*- coding: utf-8 -*-
"""De leerbundels voor Engels op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche Engels 2de graad dubbele finaliteit, geldig vanaf
1 januari 2027. Die fiche vraagt dezelfde woordvelden en dezelfde vaardigheden
als de twee doorstroomfiches, maar op een ander ERK-niveau: A2 in plaats van
B1. Daarom bouwen we de bundels hier niet opnieuw, maar nemen we die van
doorstroom over en zetten we de verschillen erin.

Wat de dubbele finaliteit **niet** vraagt en hier dus uit gaat:

  * de modale hulpwerkwoorden — de hele bundel daarover valt weg
  * de past perfect simple
  * de toekomst met 'going to', de future continuous en 'shall'
  * de betrekkelijke voornaamwoorden en de betrekkelijke bijzinnen
  * de conditionals zero en first als apart begrip
  * 'used to' en 'will be able to'

Twee bundels zijn hier nieuw, voor leerstof die de A2-fiche wél vraagt:

  * **Klank, klemtoon, intonatie en spelling.** De fiche zet daar een eigen
    rij voor: uitspraak van klanken, woordaccent, articulatie, intonatie, de
    relatie tussen klank- en schriftbeeld, en de spelling van frequente
    woorden.
  * **Spreken, gesprekken en hoe je beoordeeld wordt.** Spreken en de twee
    mondelinge interacties zijn samen 24 % van het examen, met drie eigen
    beoordelingsrijen: lichaamstaal, spreektempo en vlotheid, en uitspraak en
    intonatie.

Bij dubbele finaliteit bestaat er ook geen Engels 1 en Engels 2: het is één
examen met zeven onderdelen. Dat staat in TEKSTFIXES.

De sleutels eindigen op "-boost-dubbele-finaliteit", de volledige naam van de
categorie, net zoals bij doorstroom. De vragen komen uit
`../../boost-dubbele-finaliteit/engels.json`.
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import maak_engels_boost as doorstroom

tabel = bundel.tabel

VAK = "Engels"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"

# De bundel over de modale hulpwerkwoorden valt helemaal weg: can, must,
# should en hun soortgenoten staan niet op de A2-fiche.
WEG = ["modal-auxiliaries-imperative-en-infinitive"]

# Bundels die een andere naam krijgen, omdat hun inhoud hier anders is.
HERNOEM = {
    "pronouns-de-zeven-soorten": (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "Pronouns: de vijf soorten en de onbepaalde woorden",
    ),
    "de-verleden-en-de-toekomende-tijden": (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "Past simple, past continuous en de toekomst met will",
    ),
    "zinsdelen-soorten-zinnen-en-bijzinnen": (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Zinsdelen, soorten zinnen en samengestelde zinnen",
    ),
}

# ─────────────────────────────────────────────────────────────
# De ingrepen. Elke regel is (sleutel, haak, wat, blokken):
#   haak    een stuk tekst dat in precies één blok van die bundel staat,
#           of bij "schrap-sectie" de kop van de sectie
#   wat     "vervang" het blok, "na" het blok, of "schrap-sectie"
# De sleutel is de nieuwe, hernoemde sleutel.
# ─────────────────────────────────────────────────────────────
PATCHES = [
    # ── Pronouns
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "Betrekkelijke voornaamwoorden",
        "schrap-sectie",
        [],
    ),
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "<strong>Who's</strong> is de korte vorm",
        "na",
        [
            ("p", "Vraag je met <strong>who</strong> naar het <strong>onderwerp</strong>, dan heb "
                  "je <strong>geen do</strong> nodig: <em>Who <strong>wants</strong> tea?</em> "
                  "Vraag je naar iets anders, dan wel: <em>Who <strong>do</strong> you want?</em>, "
                  "<em>What <strong>does</strong> your father do?</em> Na do of does blijft het "
                  "werkwoord kaal."),
            ("p", "De volgorde in een vraag is <strong>vraagwoord, hulpwerkwoord, onderwerp, "
                  "werkwoord</strong>. Het onderwerp staat dus <strong>achter</strong> de "
                  "persoonsvorm, niet ervoor. <em>What you want?</em> is fout; het is <em>What "
                  "<strong>do</strong> you want?</em>"),
            ("kader", "<strong>How much</strong> of <strong>how many</strong>? Kan je het tellen, "
                      "dan is het <em>how many</em>: <em>how many apples</em>. Kan je het niet "
                      "tellen, dan is het <em>how much</em>: <em>how much milk</em>, <em>how much "
                      "is this jacket?</em>"),
        ],
    ),
    # ── Schrijven
    (
        "schrijven-schriftelijke-interactie-en-literatuurbeleving",
        "Schrijven en schriftelijke interactie wegen samen",
        "na",
        [
            ("p", "Dit zijn de zeven onderdelen van je examen en wat ze wegen: "
                  "<strong>lezen 30 %</strong>, <strong>luisteren 30 %</strong>, schrijven 8 %, "
                  "schriftelijke interactie 8 %, spreken 8 %, en twee keer mondelinge interactie, "
                  "elk 8 %. Lezen en luisteren samen zijn dus <strong>60 %</strong>: zwaarder dan "
                  "al de rest samen."),
        ],
    ),
    # ── Past simple, past continuous en de toekomst met will
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "De past perfect",
        "schrap-sectie",
        [],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "<strong>Used to</strong> zegt dat iets",
        "vervang",
        [],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "<th style=\"border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 9px;"
        "color:#234539;font-weight:600;text-align:left;\">Vorm</th>",
        "vervang",
        [
            ("p", tabel(
                ["Wanneer", "Voorbeeld"],
                [
                    ["een beslissing op het moment zelf",
                     "<em>That bag looks heavy. <strong>I'll</strong> help you.</em>"],
                    ["een belofte",
                     "<em>I promise I <strong>won't</strong> tell anyone.</em>"],
                    ["een voorspelling",
                     "<em>I think it <strong>will</strong> rain tomorrow.</em>"],
                    ["een feit over later",
                     "<em>The train <strong>will</strong> leave at six.</em>"],
                ],
            )),
            ("p", "De korte vormen zijn <strong>I'll, you'll, she'll, we'll, they'll</strong> en "
                  "voor de ontkenning <strong>won't</strong>. Die laatste verandert de klank "
                  "helemaal, anders dan don't of can't."),
        ],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "Twee modale werkwoorden na elkaar kan niet",
        "vervang",
        [
            ("weetje", "Woorden als <strong>tomorrow</strong>, <em>next week</em> en <em>in a few "
                       "days</em> verraden meteen dat je de toekomst nodig hebt, net zoals "
                       "yesterday de past simple verraadt."),
        ],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "<strong>Shall</strong> komt in het moderne Engels",
        "vervang",
        [],
    ),
    # ── Zinsdelen, soorten zinnen en samengestelde zinnen
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "kijk naar de trailer van een Engelstalige film en let op de tijden",
        "vervang",
        [
            ("kader", "<strong>Deze week:</strong> kijk naar de trailer van een Engelstalige film "
                      "en let op de tijden: hoor je <em>will</em> of een verleden tijd? Vertel "
                      "daarna in drie zinnen waar de film over gaat. Doe het één keer, en let "
                      "daarna op wat je miste of niet gezegd kreeg. Dat is precies je volgende "
                      "oefening."),
        ],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Betrekkelijke bijzinnen en de komma",
        "schrap-sectie",
        [],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Komt de bijzin <strong>vooraan</strong>",
        "na",
        [
            ("p", "Een paar onderschikkende voegwoorden die vaak terugkomen: "
                  "<strong>because</strong> geeft de reden, <strong>although</strong> en "
                  "<strong>though</strong> een tegenstelling, <strong>unless</strong> een "
                  "voorwaarde, <strong>while</strong> een gelijktijdigheid en "
                  "<strong>until</strong> of <strong>till</strong> een einde in de tijd: "
                  "<em>I will wait <strong>until</strong> you come back.</em>"),
            ("p", "<strong>So</strong> hoort bij de nevenschikkers en betekent dan 'dus': "
                  "<em>It was late, <strong>so</strong> we went home.</em> Pas op, want so is "
                  "ook een bijwoord: <em>It was <strong>so</strong> late.</em> Daar verbindt het "
                  "niets."),
            ("kader", "Tel de <strong>persoonsvormen</strong>. Eén persoonsvorm is een "
                      "<strong>enkelvoudige</strong> zin, twee of meer maken er een "
                      "<strong>samengestelde</strong> van, met of zonder voegwoord."),
        ],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "wat altijd waar is",
        "vervang",
        [],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Meer voorbeelden van de <strong>zero</strong>",
        "vervang",
        [],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "En van de <strong>first</strong>",
        "vervang",
        [
            ("p", "Een <strong>als-zin</strong> met <strong>if</strong> gebruik je vaak: "
                  "<em><strong>If it rains</strong>, we <strong>will</strong> stay at home.</em> "
                  "<em><strong>If I miss</strong> the train, I <strong>will</strong> take the "
                  "bus.</em>"),
        ],
    ),
]

# ─────────────────────────────────────────────────────────────
# Woorden die overal moeten veranderen, met hoe vaak ze voorkomen. Klopt het
# aantal niet, dan stopt het script: zo merk je het als de doorstroombundels
# veranderen.
# ─────────────────────────────────────────────────────────────
TEKSTFIXES = [
    (
        "Maar <strong>luisteren</strong> is de helft van het examen Engels 1, en "
        "<strong>mondelinge interactie</strong> (30 %) en <strong>spreken</strong> (8 %) zijn "
        "samen <strong>38 %</strong> van Engels 2.",
        "Maar <strong>luisteren</strong> is 30 % van je examen, en <strong>spreken</strong> met "
        "de twee <strong>mondelinge interacties</strong> samen nog eens <strong>24 %</strong>.",
        12,
    ),
    ("op B1-niveau", "op A2-niveau", 1),
    (
        "Schrijven en schriftelijke interactie wegen samen <strong>58 %</strong> van het examen "
        "Engels 2.",
        "Schrijven en schriftelijke interactie wegen samen <strong>16 %</strong> van je examen.",
        1,
    ),
    (
        "<strong>Literatuurbeleving</strong> weegt bij Engels 2 <strong>4 %</strong>. Dat is "
        "minder dan schrijven (29 %), maar het is wel",
        "Je <strong>beleving van een literaire tekst</strong> verwoorden komt bij het lezen en "
        "het schrijven aan bod. Het is",
        1,
    ),
]

# Bundels waarvan de ondertitel niet meer klopt na de ingrepen.
ONDERTITELS = {
    "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden":
        "De persoonlijke, bezittelijke, wederkerende, aanwijzende en vragende voornaamwoorden, "
        "plus de onbepaalde woorden en de hoeveelheden.",
    "past-simple-past-continuous-en-de-toekomst-met-will":
        "De past simple met haar onregelmatige werkwoorden, de past continuous, en de toekomst "
        "met will.",
    "zinsdelen-soorten-zinnen-en-samengestelde-zinnen":
        "De zinsdelen, de woordvolgorde, de vijf soorten zinnen, de congruentie, en zinnen aan "
        "elkaar knopen met nevenschikking en onderschikking.",
}

# De onthoudlijstjes van de drie aangepaste bundels, helemaal opnieuw.
ONTHOUD = {
    "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden": [
        "Onderwerpsvorm: I, you, he, she, it, we, they. Voorwerpsvorm: me, you, him, her, it, us, them.",
        "Na een voorzetsel komt de voorwerpsvorm: this is for her.",
        "It verwijst naar een ding of een dier.",
        "Its is van hem of van haar; it's is de korte vorm van it is.",
        "Bezittelijk bijvoeglijk: my, your, his, her, its, our, their. Zelfstandig: mine, yours, his, hers, ours, theirs.",
        "Wederkerend: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves.",
        "Wash en dress zijn in het Engels niet wederkerend: she washed and got dressed.",
        "Aanwijzend dichtbij: this en these. Veraf: that en those.",
        "Vragend: who, whom, whose, which en what. Which bij een beperkte keuze, what bij een open keuze.",
        "Vraag je met who naar het onderwerp, dan geen do: who wants tea?",
        "De volgorde in een vraag: vraagwoord, hulpwerkwoord, onderwerp, werkwoord.",
        "How many bij wat je kan tellen, how much bij wat je niet kan tellen en bij een prijs.",
        "Onbepaald: someone, anything, nobody, everybody. Ze horen bij een werkwoord in het enkelvoud.",
        "In vragen en ontkenningen anything, in bevestigende zinnen something.",
        "Twee ontkenningen in één zin mag niet: I didn't see anything.",
        "You is in het Engels enkelvoud én meervoud, jij én u.",
        "Is een verwijzing onduidelijk, herhaal dan gewoon het naamwoord.",
    ],
    "past-simple-past-continuous-en-de-toekomst-met-will": [
        "Regelmatig: worked, liked, studied, stopped, travelled.",
        "Onregelmatig: go went gone, see saw seen, take took taken, write wrote written, buy bought bought, drink drank drunk.",
        "In een vraag of ontkenning gebruik je did plus de basisvorm: didn't come, did you go.",
        "To be heeft geen did nodig: were you there? Was bij I, he, she en it; were bij you, we en they.",
        "Past continuous: was of were plus -ing. De lange handeling continuous, de korte simple.",
        "Na while de lange handeling, na when de korte. Twee keer continuous is tegelijk bezig.",
        "Yesterday, last week en ago vragen de past simple.",
        "Will gebruik je voor een beslissing op het moment zelf, een belofte, een voorspelling en een feit over later.",
        "Na will komt de kale basisvorm: geen to, geen -ing, en nooit een s.",
        "De korte vormen zijn I'll, she'll, we'll en voor de ontkenning won't.",
        "In een vraag wisselen will en het onderwerp: where will you be next week?",
        "Tomorrow, next week en in a few days vragen de toekomende tijd.",
        "Na if en when geen will: if it rains, we will stay at home.",
    ],
    "zinsdelen-soorten-zinnen-en-samengestelde-zinnen": [
        "De zinsdelen: onderwerp, persoonsvorm, lijdend voorwerp en meewerkend voorwerp.",
        "Staat het meewerkend voorwerp achter het lijdend voorwerp, dan komt er to of for voor.",
        "De gewone volgorde is onderwerp, persoonsvorm, rest. Zet nooit iets tussen het werkwoord en het lijdend voorwerp.",
        "De bepalingen achteraan staan in de volgorde hoe, waar, wanneer.",
        "De vijf soorten zinnen: mededelend, ontkennend, vragend, bevelend en uitroepend.",
        "Bij een uitroep draait de volgorde niet om: how fast she runs, what a mess.",
        "Een bevelende zin heeft geen onderwerp: close the door.",
        "Staat er al een hulpwerkwoord in de zin, dan heb je voor een vraag geen do nodig.",
        "Congruentie: het werkwoord past zich aan het onderwerp aan. The news is, the police are.",
        "Nevenschikking knoopt twee gelijkwaardige zinnen aan elkaar: and, but, or, so.",
        "Onderschikking hangt een bijzin onder een hoofdzin: because, although, unless, while, until.",
        "Although en but zet je niet samen in één zin.",
        "Komt de bijzin vooraan, dan staat de komma achter de bijzin.",
        "Tel de persoonsvormen: twee of meer maken er een samengestelde zin van.",
        "Wissel af tussen soorten zinnen, anders leest je tekst hakkelend of juist te zwaar.",
    ],
}

# Woorden die na de ingrepen nergens meer mogen staan.
VERBODEN = [
    "past perfect",
    "going to",
    "shall",
    "betrekkelijk",
    "conditional",
    "used to",
    "will be able",
    "modale hulpwerkwoord",
    "engels 1",
    "engels 2",
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


def hernoem_sectie(bundels: dict, sleutel: str, oud: str, nieuw: str):
    secties = bundels[sleutel + NIEUW]["secties"]
    raak = [s for s in secties if s["kop"] == oud]
    if len(raak) != 1:
        raise SystemExit(f"{sleutel}: {len(raak)} secties heten {oud!r}, verwacht 1")
    raak[0]["kop"] = nieuw


def bouw() -> dict:
    uit = {}
    for sleutel, b in doorstroom.BUNDELS.items():
        if not sleutel.endswith(OUD):
            raise SystemExit(f"Doorstroomsleutel zonder categorie: {sleutel}")
        kort = sleutel[: -len(OUD)]
        if kort in WEG:
            continue
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        if kort in HERNOEM:
            kort, titel = HERNOEM[kort]
            nieuw["titel"] = titel
        uit[kort + NIEUW] = nieuw
    if len(uit) != len(doorstroom.BUNDELS) - len(WEG):
        raise SystemExit("Er is een bundel kwijtgeraakt of dubbel gezet")

    pas_toe(uit)
    hernoem_sectie(uit, "past-simple-past-continuous-en-de-toekomst-met-will",
                   "De toekomst: will en going to", "De toekomst met will")
    hernoem_sectie(uit, "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
                   "De conditionals zero en first", "Als-zinnen en afwisseling")
    hernoem_sectie(uit, "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
                   "Onbepaalde voornaamwoorden", "Onbepaalde voornaamwoorden en hoeveelheden")

    for oud, nieuw, hoevaak in TEKSTFIXES:
        uit, aantal = fix_teksten(uit, oud, nieuw)
        if aantal != hoevaak:
            raise SystemExit(f"{oud!r} staat {aantal} keer in de bundels, verwacht {hoevaak}")
    for kort, onder in ONDERTITELS.items():
        uit[kort + NIEUW]["onder"] = onder
    for kort, lijst in ONTHOUD.items():
        uit[kort + NIEUW]["onthoud"] = list(lijst)

    uit.update(NIEUWE_BUNDELS)

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


# ─────────────────────────────────────────────────────────────
# De twee bundels die hier nieuw zijn.
# ─────────────────────────────────────────────────────────────
BUITEN = (
    "p",
    "Op dit platform oefen je lezen, woordenschat en grammatica. Maar "
    "<strong>luisteren</strong> en <strong>spreken</strong> zijn samen bijna de helft van je "
    "examen, en die oefen je alleen met geluid en met iemand tegenover je.",
)

NIEUWE_BUNDELS = {}

NIEUWE_BUNDELS["klank-klemtoon-intonatie-en-spelling" + NIEUW] = dict(
    vak=VAK,
    niveau=DF,
    titel="Klank, klemtoon, intonatie en spelling",
    onder="Hoe het Engels klinkt, waar de klemtoon valt, wat je wel schrijft maar niet hoort, "
          "en hoe je de frequente woorden spelt.",
    secties=[
        dict(
            kop="Klank en schriftbeeld",
            blokken=[
                ("p", "Het Engels schrijft niet wat het zegt. Dezelfde letter kan telkens anders "
                      "klinken: vergelijk de a van <em>cat</em>, <em>car</em>, <em>cake</em> en "
                      "<em>about</em>. Omgekeerd kan dezelfde klank op verschillende manieren "
                      "geschreven worden: <em>see</em>, <em>sea</em> en <em>scene</em>."),
                ("p", "Sommige letters schrijf je wel en hoor je niet. Een paar frequente:"),
                ("p", tabel(
                    ["Woord", "Je hoort niet"],
                    [["<em>knee</em>, <em>knife</em>, <em>know</em>", "de k"],
                     ["<em>hour</em>, <em>honest</em>", "de h"],
                     ["<em>island</em>", "de s"],
                     ["<em>listen</em>, <em>castle</em>", "de t"],
                     ["<em>half</em>, <em>talk</em>, <em>walk</em>", "de l"],
                     ["<em>write</em>, <em>wrong</em>", "de w"]],
                )),
                ("kader", "Omdat <em>hour</em> met een klinkerklank begint, schrijf je er "
                          "<strong>an</strong> voor: <em>an hour</em>. Het lidwoord volgt de "
                          "<strong>klank</strong>, niet de letter."),
                ("p", "Woorden die hetzelfde klinken maar anders geschreven worden, zijn een "
                      "bekende valkuil: <em>their</em> en <em>there</em>, <em>to</em>, "
                      "<em>too</em> en <em>two</em>, <em>write</em> en <em>right</em>, "
                      "<em>your</em> en <em>you're</em>. Je hoort het verschil niet; je ziet het."),
                ("weetje", "Ook de verleden tijd <em>read</em> klinkt als <em>red</em>, terwijl de "
                           "tegenwoordige tijd <em>read</em> als <em>reed</em> klinkt. Eén "
                           "schriftbeeld, twee klanken."),
                ("p", "Een paar klanken die het Nederlands niet heeft. De <strong>th</strong> "
                      "komt in twee soorten: stemloos in <em>think</em> en <em>thank</em>, "
                      "stemhebbend in <em>this</em>, <em>that</em> en <em>they</em>. En de lengte "
                      "van een klinker maakt een ander woord: <em>ship</em> is kort, "
                      "<em>sheep</em> is lang."),
            ],
        ),
        dict(
            kop="Woordaccent",
            blokken=[
                ("p", "In elk Engels woord van meer dan één lettergreep ligt de klemtoon op één "
                      "bepaalde lettergreep: <em>TA-ble</em>, <em>WA-ter</em>, <em>O-pen</em>, "
                      "maar <em>a-BOUT</em> en <em>com-PU-ter</em>. Leg je ze verkeerd, dan klinkt "
                      "het woord meteen vreemd, ook al zijn alle klanken juist."),
                ("p", "De onbeklemtoonde lettergrepen worden half ingeslikt. Daarom hoor je bij "
                      "het luisteren vooral de <strong>beklemtoonde</strong> lettergrepen, en "
                      "haal je de inhoud van een zin er het snelst uit als je daarop mikt."),
                ("kader", "Bij sommige woorden <strong>verschuift</strong> de klemtoon en "
                          "verandert daarmee de woordsoort. Het cadeau is een "
                          "<em><strong>PRE</strong>-sent</em>, een zelfstandig naamwoord; iets "
                          "voorstellen is <em>pre-<strong>SENT</strong></em>, een werkwoord. Zo "
                          "ook <em>RE-cord</em> en <em>re-CORD</em>."),
            ],
        ),
        dict(
            kop="Intonatie en articulatie",
            blokken=[
                ("p", "<strong>Intonatie</strong> is de melodie van je zin: hoe je stem stijgt en "
                      "daalt. Bij een vraag die je met yes of no beantwoordt, gaat je stem aan het "
                      "eind <strong>omhoog</strong>: <em>Are you coming?</em> Bij een vraag met "
                      "een vraagwoord daalt ze juist: <em>Where are you going?</em>"),
                ("p", "<strong>Articulatie</strong> is hoe duidelijk je de klanken vormt. Wie de "
                      "klanken afmaakt in plaats van ze in te slikken, wordt zonder moeite "
                      "verstaan. Je uitspraak hoeft niet te klinken als die van iemand uit "
                      "Londen; ze moet je boodschap niet in de weg staan."),
            ],
        ),
        dict(
            kop="De uitgangen -ed en -s",
            blokken=[
                ("p", "De <strong>-ed</strong> van de verleden tijd klinkt op drie manieren, "
                      "zonder dat de spelling verandert:"),
                ("p", tabel(
                    ["Na een", "Klinkt als", "Voorbeeld"],
                    [["t- of d-klank", "een extra lettergreep", "<em>wanted</em>, <em>needed</em>, <em>started</em>"],
                     ["stemloze klank", "een t", "<em>worked</em>, <em>liked</em>, <em>stopped</em>"],
                     ["stemhebbende klank", "een d", "<em>played</em>, <em>lived</em>, <em>opened</em>"]],
                )),
                ("p", "Met de <strong>meervouds-s</strong> gebeurt hetzelfde: een z na een "
                      "stemhebbende klank (<em>dogs</em>, <em>pens</em>), een s na een stemloze "
                      "(<em>cats</em>, <em>books</em>), en een hele lettergreep erbij na een "
                      "sisklank (<em>boxes</em>, <em>watches</em>, <em>buses</em>)."),
            ],
        ),
        dict(
            kop="De spelling van frequente woorden",
            blokken=[
                ("p", "Een paar regels halen de meeste fouten eruit:"),
                ("p", tabel(
                    ["Regel", "Voorbeeld"],
                    [["korte klinker plus één medeklinker: verdubbelen",
                      "stop → stopping, run → running, swim → swimming"],
                     ["stomme e valt weg voor -ing",
                      "make → making, write → writing, dance → dancing"],
                     ["y achter een medeklinker wordt ie of ies",
                      "study → studied, baby → babies, carry → carries"],
                     ["y achter een klinker blijft staan",
                      "boy → boys, play → plays"],
                     ["na een sisklank komt -es",
                      "box → boxes, watch → watches, bus → buses"],
                     ["sommige woorden op -f krijgen -ves",
                      "leaf → leaves, knife → knives, wife → wives"]],
                )),
                ("p", "En een paar woorden die bijna iedereen fout schrijft: "
                      "<strong>because</strong>, <strong>friend</strong>, "
                      "<strong>beautiful</strong>, <strong>necessary</strong>, "
                      "<strong>receive</strong>, <strong>definitely</strong> (er zit "
                      "<em>finite</em> in) en <strong>address</strong>, met dubbele d én dubbele s, terwijl het "
                      "Nederlandse <em>adres</em> er geen enkele heeft."),
                ("kader", "Het ezelsbruggetje <strong>i before e except after c</strong> dekt de "
                          "meeste gevallen: <em>believe</em> en <em>field</em>, maar "
                          "<em>receive</em> en <em>ceiling</em>."),
                ("p", "Hoofdletters liggen anders dan in het Nederlands. Dagen, maanden, talen, "
                      "landen en nationaliteiten krijgen er een: <em>Monday</em>, <em>July</em>, "
                      "<em>English</em>, <em>Belgium</em>. De <strong>seizoenen</strong> niet: "
                      "<em>winter</em>, <em>spring</em>, <em>summer</em>, <em>autumn</em>."),
                ("p", "De apostrof staat waar letters weggevallen zijn: <em>don't</em>, "
                      "<em>can't</em>, <em>I'm</em>, <em>won't</em>. Zonder apostrof is het een "
                      "ander woord, of geen woord."),
                ("weetje", "Je mag op het examen een spellingcontrole gebruiken om je tekst na te "
                           "kijken. Die vindt je typfouten, maar ze schrijft niets voor jou en ze "
                           "ziet niet dat je <em>their</em> schreef waar <em>there</em> moest "
                           "staan: allebei bestaan ze."),
                ("p", "<strong>Spelfouten</strong> kosten je niet meteen al je punten: ze tellen "
                      "pas mee als ze het <strong>begrip</strong> van je tekst in de weg staan. "
                      "Een lezer die moet raden wat je bedoelt, kost je er wel."),
            ],
        ),
        dict(kop="Oefen dit ook buiten het scherm", blokken=[
            BUITEN,
            ("kader", "<strong>Deze week:</strong> zoek de tekst van een Engels liedje dat je goed "
                      "kent en lees mee terwijl het speelt. Let op de woorden waar je iets anders "
                      "hoorde dan er staat."),
        ]),
    ],
    onthoud=[
        "Het Engels schrijft niet wat het zegt: dezelfde letter kan verschillende klanken hebben.",
        "Stomme letters: de k van knee, de h van hour, de s van island, de t van listen, de l van half.",
        "An hour, want het lidwoord volgt de klank en niet de letter.",
        "Gelijkklinkend maar anders geschreven: their en there, to, too en two, write en right, your en you're.",
        "De th is stemloos in think en stemhebbend in this. Ship is kort, sheep is lang.",
        "De klemtoon ligt op één lettergreep: TA-ble, maar a-BOUT en com-PU-ter.",
        "Verschuift de klemtoon, dan verandert de woordsoort: PRE-sent en pre-SENT.",
        "Intonatie stijgt bij een ja-neevraag en daalt bij een vraag met een vraagwoord.",
        "Articulatie is de klanken afmaken. Een accent is geen fout.",
        "De -ed is een extra lettergreep na t of d, een t na een stemloze klank, een d na een stemhebbende.",
        "De meervouds-s klinkt als z na een stemhebbende klank en wordt een lettergreep na een sisklank.",
        "Korte klinker plus één medeklinker: verdubbelen. Stomme e valt weg voor -ing.",
        "Y achter een medeklinker wordt ie of ies; achter een klinker blijft ze staan.",
        "Na een sisklank komt -es: boxes, watches, buses.",
        "i before e except after c: believe, maar receive.",
        "Dagen, maanden, talen en landen met een hoofdletter, de seizoenen niet.",
    ],
)

NIEUWE_BUNDELS["spreken-gesprekken-en-hoe-je-beoordeeld-wordt" + NIEUW] = dict(
    vak=VAK,
    niveau=DF,
    titel="Spreken, gesprekken en hoe je beoordeeld wordt",
    onder="Wat je zegt om een gesprek te beginnen, gaande te houden en te beëindigen, en waarop "
          "een mondelinge opdracht beoordeeld wordt.",
    secties=[
        dict(
            kop="Alledaagse sociale contacten",
            blokken=[
                ("p", "Een groot deel van wat je mondeling moet kunnen, zijn de kleine dingen die "
                      "een gesprek mogelijk maken: iemand begroeten en aanspreken, afscheid nemen, "
                      "iets voorstellen, bedanken, uitnodigen, je verontschuldigen en reageren als "
                      "iemand zich verontschuldigt."),
                ("p", tabel(
                    ["Wat je doet", "Wat je zegt"],
                    [["een onbekende aanspreken", "<em>Excuse me, is this seat free?</em>"],
                     ["kennismaken", "<em>Nice to meet you.</em>"],
                     ["iets voorstellen", "<em>Why don't we go to the pool?</em> / <em>How about a swim?</em>"],
                     ["uitnodigen", "<em>Would you like to come to my party?</em>"],
                     ["bedanken", "<em>Thank you very much for your help.</em>"],
                     ["je verontschuldigen", "<em>I'm sorry I'm late.</em> / <em>I'm afraid I'm late.</em>"],
                     ["daarop reageren", "<em>That's all right, don't worry.</em>"],
                     ["afscheid nemen", "<em>It was nice talking to you. See you tomorrow.</em>"]],
                )),
                ("kader", "<strong>Could you …?</strong> maakt van een bevel een vraag. "
                          "<em>Tell me when the bus leaves</em> klinkt hard; <em>Could you tell me "
                          "when the bus leaves?</em> is wat je tegen een onbekende zegt. Vergeet "
                          "<em>please</em> en <em>thank you</em> niet."),
            ],
        ),
        dict(
            kop="Een gesprek voeren",
            blokken=[
                ("p", "Bij een <strong>spreekopdracht</strong> ben je alleen aan het woord: je "
                      "bouwt zelf een verhaaltje op. Bij een <strong>gesprek</strong> hangt wat je "
                      "zegt af van wat de ander net zei. Daarom kan je een gesprek nooit helemaal "
                      "op voorhand uitschrijven; voorlezen is geen gesprek."),
                ("p", "Je moet een eenvoudig gesprek kunnen <strong>beginnen, gaande houden en "
                      "beëindigen</strong>. Gaande houden doe je met vragen die de ander een reden "
                      "geven om verder te vertellen: <em>What happened next?</em>, <em>Really? "
                      "Tell me more.</em>, <em>How did you feel about that?</em> Beëindigen doe je "
                      "met een bedankje en een reden: <em>Thanks for your time, I have to go "
                      "now.</em>"),
                ("p", "Je geeft en vraagt ook <strong>informatie</strong> (<em>Could you tell me "
                      "when the shop opens?</em>), je geeft je <strong>mening</strong> (<em>I "
                      "think the film was too long.</em>), je <strong>vertelt</strong> iets en "
                      "reageert op vragen, en je <strong>legt</strong> iemand iets uit."),
                ("kader", "Raak je de draad kwijt? <em>Could you repeat that, please?</em> of "
                          "<em>Could you speak more slowly, please?</em> Dat is geen zwakte maar "
                          "een strategie: je houdt het gesprek er net mee gaande."),
            ],
        ),
        dict(
            kop="Waarop je beoordeeld wordt",
            blokken=[
                ("p", "Vijf dingen gelden voor alles wat je zegt of schrijft:"),
                ("p", tabel(
                    ["Vereiste", "Wat ermee bedoeld wordt"],
                    [["taakvoltooiing", "je doel is bereikt, je boodschap komt over, de opdracht is volledig uitgevoerd"],
                     ["woordenschat", "je gebruikt frequente woorden en vaste uitdrukkingen correct"],
                     ["grammatica en zinsbouw", "eenvoudige correcte zinnen; fouten verstoren de communicatie niet"],
                     ["tekststructuur en samenhang", "inleiding, midden en slot, met signaalwoorden"],
                     ["register en beleefdheid", "neutraal of informeel, aangepast aan wie voor je zit"]],
                )),
                ("p", "En drie gelden <strong>alleen</strong> voor het mondelinge deel:"),
                ("p", tabel(
                    ["Vereiste", "Wat ermee bedoeld wordt"],
                    [["lichaamstaal", "je gebruikt ze zelf en je leest ze af bij je gesprekspartner"],
                     ["spreektempo en vlotheid", "onderbrekingen, valse starts en herformuleringen zijn aanvaardbaar"],
                     ["uitspraak en intonatie", "helder genoeg om je boodschap niet in de weg te staan; een accent is geen fout"]],
                )),
                ("weetje", "Scheldwoorden horen in geen enkel register thuis, ook niet verzacht "
                           "tot <em>sh*t</em>. Ze kosten je punten op register en "
                           "beleefdheidsconventies."),
            ],
        ),
        dict(
            kop="Strategieën die werken",
            blokken=[
                ("p", "Vóór je begint: gebruik het <strong>communicatiemodel</strong>. Waarom "
                      "spreek je? Voor wie is je boodschap? Met wie communiceer je? Wat wil je "
                      "precies vertellen? Maak dan een <strong>spreekplan met kernwoorden</strong>, "
                      "geen uitgeschreven tekst, want die klinkt meteen als een tekst."),
                ("p", "Tijdens het spreken: zit je vast, laat je dan niet ontmoedigen en bereik je "
                      "doel met de woorden die je <strong>wél</strong> kent. Ken je "
                      "<em>crutches</em> niet, dan zeg je <em>the sticks you walk with after you "
                      "break a leg</em>. Begrijpt je gesprekspartner je niet, zeg het dan op een "
                      "<strong>andere manier</strong> in plaats van luider."),
                ("p", "Speel in op wat de ander zegt: toon interesse, toon respect, stel een "
                      "vervolgvraag. Een gesprek waarin maar één iemand praat, is geen gesprek."),
            ],
        ),
        dict(
            kop="Hoe het examen verloopt",
            blokken=[
                ("p", "Je examen bestaat uit <strong>drie</strong> delen. De "
                      "<strong>spreekopdracht</strong> neem je thuis op en dien je in tot drie "
                      "dagen vóór je digitale examen; doe je dat niet op tijd, dan mag je niet "
                      "deelnemen. Het <strong>digitale examen</strong> maak je op de computer in het "
                      "<strong>examencentrum</strong> in Brussel en het duurt 150 minuten; de "
                      "onderdelen zijn lezen, luisteren en schrijven. Daarna volgt het "
                      "<strong>gesprek</strong>: 15 minuten voorbereiding voor 2 opdrachten, en "
                      "een gesprek van 10 minuten."),
                ("p", "De gewichten liggen zo: lezen 30 %, luisteren 30 %, schrijven 8 %, "
                      "schriftelijke interactie 8 %, spreken 8 %, en twee keer mondelinge "
                      "interactie, elk 8 %. Lezen en luisteren samen zijn dus 60 %, het mondelinge "
                      "deel 24 %."),
                ("kader", "Er is <strong>geen giscorrectie</strong>. Een vraag openlaten levert "
                          "nooit meer op dan ze proberen."),
            ],
        ),
        dict(kop="Oefen dit ook buiten het scherm", blokken=[
            BUITEN,
            ("kader", "<strong>Deze week:</strong> neem je gsm en vertel twee minuten in het Engels "
                      "wat je vandaag gedaan hebt. Luister het terug en let op één ding: waar viel "
                      "je stil, en welk woord zocht je?"),
        ]),
    ],
    onthoud=[
        "Alledaagse sociale contacten: begroeten, aanspreken, afscheid nemen, voorstellen, bedanken, uitnodigen, je verontschuldigen en daarop reageren.",
        "Could you …? maakt van een bevel een beleefde vraag. Vergeet please en thank you niet.",
        "Bij een spreekopdracht ben je alleen aan het woord; bij een gesprek reageer je op de ander.",
        "Een gesprek gaande houden: What happened next? Really? Tell me more. How did you feel about that?",
        "Een gesprek beëindigen: bedank en geef een reden.",
        "Vijf vereisten voor alles: taakvoltooiing, woordenschat, grammatica en zinsbouw, tekststructuur en samenhang, register en beleefdheid.",
        "Drie vereisten alleen mondeling: lichaamstaal, spreektempo en vlotheid, uitspraak en intonatie.",
        "Onderbrekingen, valse starts en herformuleringen zijn aanvaardbaar.",
        "Communicatiemodel: waarom, voor wie, met wie, wat en via welk kanaal.",
        "Maak een spreekplan met kernwoorden, geen uitgeschreven tekst.",
        "Ken je een woord niet, omschrijf het dan met woorden die je wel kent.",
        "Wordt je niet begrepen, herformuleer dan in plaats van luider te spreken.",
        "Could you repeat that, please? en Could you speak more slowly, please?",
        "De spreekopdracht neem je thuis op en dien je in tot drie dagen voor het digitale examen.",
        "Het digitale examen duurt 150 minuten; het gesprek duurt 10 minuten na 15 minuten voorbereiding.",
        "Lezen 30 %, luisteren 30 %, het mondelinge deel samen 24 %. Er is geen giscorrectie.",
    ],
)

BUNDELS = bouw()

if __name__ == "__main__":
    for sleutel, b in BUNDELS.items():
        bundel.schrijf(b, sleutel)
        print(" ", sleutel)
