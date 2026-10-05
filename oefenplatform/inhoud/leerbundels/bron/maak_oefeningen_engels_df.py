# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Engels 🚀 Boost dubbele finaliteit.

Net als bij de leerbundels nemen we de doorstroomversie over en zetten we er de
verschillen in; zie `maak_engels_df.py` voor waarom. De ingrepen hangen aan een
stuk tekst van de oefening die ze raken, en elke ingreep moet precies één
oefening raken. Verandert er iets aan de doorstroombundel, dan stopt dit script
in plaats van er stil overheen te gaan.

De bundel over de modale hulpwerkwoorden valt helemaal weg, en er komen twee
nieuwe bij: een over klank, klemtoon en spelling, en een over spreken en
gesprekken.

De sleutels dragen het voorvoegsel "oefenbundel-" en eindigen op
"-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import maak_oefeningen_engels_boost as doorstroom
import maak_engels_df as leerbundels

VAK = "Engels"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"
W, WW, WL = "120px", "185px", "250px"

WEG = leerbundels.WEG
HERNOEM = leerbundels.HERNOEM

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Schrijf de hele zin over als dat gevraagd wordt; zo zie je de fout een tweede keer.",
    "Lees je antwoord daarna nog eens luidop. Wat raar klinkt, is het vaak ook.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# (sleutel zonder voorvoegsel en categorie, haak, wat, oefeningen)
PATCHES = [
    # ── Pronouns: de betrekkelijke voornaamwoorden gaan eruit
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "Betrekkelijke bijzinnen",
        "schrap-sectie",
        [],
    ),
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "The film what I saw was long.",
        "vervang",
        [
            ("kort", "What you want for your birthday?", "What do you want for your birthday?", WL),
        ],
    ),
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "('whose', 'vragend of betrekkelijk')",
        "vervang",
        [
            ("rij", [("whose", "vragend"), ("which", "vragend"),
                     ("nobody", "onbepaald"), ("each", "onbepaald")],
             "Schrijf bij elk woord welke soort voornaamwoord het is.", W),
        ],
    ),
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "The teachers helped the pupils, and they thanked them.",
        "na",
        [
            ("rij", [("… apples do you want?", "how many"),
                     ("… milk is left?", "how much"),
                     ("… is this jacket?", "how much"),
                     ("… times did you call?", "how many")],
             "Vul how much of how many in.", WW),
            ("kort", "Who do want tea?", "Who wants tea?", WL),
        ],
    ),
    # ── De tijden: de past perfect en going to gaan eruit
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "Past perfect",
        "schrap-sectie",
        [],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "Will of going to?",
        "schrap-sectie",
        [],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "She won't can come tomorrow.",
        "vervang",
        [
            ("kort", "She will comes tomorrow.", "She will come tomorrow.", WL),
        ],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "I was knowing the answer.",
        "na",
        [
            ("rij", [("That bag looks heavy. I … help you.", "will of 'll"),
                     ("I promise I … tell anyone.", "won't"),
                     ("I think it … rain tomorrow.", "will"),
                     ("The train … leave at six.", "will")],
             "Vul de toekomende tijd met will in.", WW),
            ("kort", "Schrijf de korte vorm van 'will not'.", "won't", W),
            ("open", "Noem vier gevallen waarin je 'will' gebruikt, met bij elk een eigen "
                     "voorbeeldzin in het Engels.",
             "Een beslissing op het moment zelf (I'll get it), een belofte (I promise I won't "
             "tell), een voorspelling (I think it will rain), en een feit over later (The train "
             "will leave at six).", 7),
        ],
    ),
    (
        "past-simple-past-continuous-en-de-toekomst-met-will",
        "Vertel aan iemand in het Engels wat je vorig weekend gedaan hebt",
        "vervang",
        [
            ("open", "Vertel aan iemand in het Engels wat je vorig weekend gedaan hebt en wat je "
                     "volgend weekend doet. Gebruik minstens één past simple, één past continuous "
                     "en één zin met will. Schrijf de drie zinnen hier eerst op.",
             "Eigen antwoord. Bijvoorbeeld: I went to my grandmother's on Saturday. While we were "
             "eating, my cousin called. Next weekend I will stay at home.", 8),
        ],
    ),
    # ── Zinsbouw: de betrekkelijke bijzinnen en de conditionals gaan eruit
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Conditionals zero en first",
        "schrap-sectie",
        [],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Wat betekent: The students who worked hard passed?",
        "vervang",
        [
            ("kort", "Hoeveel persoonsvormen heeft: It was late, so we went home?",
             "twee, dus het is een samengestelde zin", WL),
        ],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "En: The students, who worked hard, passed?",
        "vervang",
        [
            ("kort", "I will wait … you come back. Vul het voegwoord in.", "until of till", WW),
        ],
    ),
    (
        "zinsdelen-soorten-zinnen-en-samengestelde-zinnen",
        "Wat betekent unless?",
        "na",
        [
            ("open", "Wat is het verschil tussen nevenschikking en onderschikking? Geef van allebei "
                     "een voorbeeldzin in het Engels.",
             "Nevenschikking knoopt twee gelijkwaardige zinnen aan elkaar, die elk op zichzelf "
             "kunnen staan: I called her and she answered. Onderschikking hangt een bijzin onder "
             "een hoofdzin; die bijzin kan niet alleen staan: I stayed at home because it was "
             "raining.", 7),
        ],
    ),
]

# Opdrachten van een reeks die na de ingrepen niet meer kloppen.
# (sleutel zonder voorvoegsel en categorie, kop van de reeks, nieuwe opdracht)
OPDRACHTEN = [
    (
        "pronouns-de-vijf-soorten-en-de-onbepaalde-woorden",
        "Welke soort?",
        "Schrijf bij elk woord welke soort voornaamwoord het is: persoonlijk, bezittelijk, "
        "wederkerend, aanwijzend, vragend of onbepaald.",
    ),
]

VERBODEN = leerbundels.VERBODEN

# Twee gevallen waarin een verboden woord onschuldig is. In een oefening staat
# ook de breedte van het invulvakje ("185px"), en die plakt bij het nakijken
# tegen het woord ervoor aan: "In het Engels 185px" leest dan als "engels 1".
# En "going to the coast" is gewoon het werkwoord to go met een plaats erachter,
# niet de toekomende tijd die niet op de fiche staat.
ONSCHULDIG = [
    "going to the coast",
]


def tekst_van(oef) -> str:
    return " ".join(str(d) for d in oef if not str(d).endswith("px"))


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
        kort = sleutel[len("oefenbundel-") : -len(OUD)]
        if kort in WEG:
            continue
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        if kort in HERNOEM:
            kort, titel = HERNOEM[kort]
            nieuw["titel"] = titel
        uit["oefenbundel-" + kort + NIEUW] = nieuw
    if len(uit) != len(doorstroom.OEFENBUNDELS) - len(WEG):
        raise SystemExit("Er is een oefenbundel kwijtgeraakt of dubbel gezet")

    pas_toe(uit)
    for kort, kop, opdracht in OPDRACHTEN:
        reeksen = uit["oefenbundel-" + kort + NIEUW]["reeksen"]
        raak = [r for r in reeksen if r["kop"] == kop]
        if len(raak) != 1:
            raise SystemExit(f"{kort}: {len(raak)} reeksen heten {kop!r}, verwacht 1")
        raak[0]["opdracht"] = opdracht
    uit.update(NIEUWE_BUNDELS)

    for sleutel, b in uit.items():
        alles = " ".join(
            [b["onder"]]
            + list(b.get("hoe", []))
            + [r["kop"] + " " + r.get("opdracht", "") for r in b["reeksen"]]
            + [tekst_van(o) for r in b["reeksen"] for o in r["oefeningen"]]
        ).lower()
        for onschuldig in ONSCHULDIG:
            alles = alles.replace(onschuldig, "")
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{sleutel} gebruikt nog {woord!r}, dat staat niet op de DF-fiche")
    return uit


# ─────────────────────────────────────────────────────────────
# De twee oefenbundels die hier nieuw zijn.
# ─────────────────────────────────────────────────────────────
NIEUWE_BUNDELS = {}

NIEUWE_BUNDELS["oefenbundel-klank-klemtoon-intonatie-en-spelling" + NIEUW] = dict(
    vak=VAK,
    niveau=DF,
    titel="Klank, klemtoon, intonatie en spelling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(
            kop="Welke letter hoor je niet?",
            opdracht="Schrijf bij elk woord de letter die je wel schrijft maar niet uitspreekt.",
            oefeningen=[
                ("rij", [("knife", "k"), ("hour", "h"), ("island", "s"), ("castle", "t")],
                 "Schrijf de stomme letter.", W),
                ("rij", [("walk", "l"), ("wrong", "w"), ("know", "k"), ("listen", "t")],
                 "Schrijf de stomme letter.", W),
                ("kort", "Waarom schrijf je 'an hour' en niet 'a hour'?",
                 "omdat het lidwoord de klank volgt en hour met een klinkerklank begint", WL),
            ],
        ),
        dict(
            kop="Waar ligt de klemtoon?",
            opdracht="Schrijf het woord over en onderstreep de beklemtoonde lettergreep.",
            oefeningen=[
                ("rij", [("table", "TA-ble"), ("about", "a-BOUT"),
                         ("computer", "com-PU-ter"), ("open", "O-pen")],
                 "Schrijf de klemtoon in hoofdletters.", WW),
                ("open", "Het woord 'present' kan twee dingen zijn. Schrijf allebei de "
                         "uitspraken en zeg welke woordsoort erbij hoort.",
                 "PRE-sent is een zelfstandig naamwoord, het cadeau. Pre-SENT is een werkwoord, "
                 "iets voorstellen of aanbieden.", 4),
            ],
        ),
        dict(
            kop="Hoe klinkt de uitgang?",
            opdracht="Schrijf bij elk werkwoord of de -ed een extra lettergreep is, of klinkt "
                     "als een t of als een d.",
            oefeningen=[
                ("rij", [("wanted", "extra lettergreep"), ("worked", "t"),
                         ("played", "d"), ("started", "extra lettergreep")],
                 "Schrijf hoe de -ed klinkt.", WW),
                ("kort", "Hoeveel lettergrepen hoor je in 'boxes'?", "twee", W),
                ("kort", "Hoe klinkt de meervouds-s in 'dogs'?", "als een z", W),
            ],
        ),
        dict(
            kop="Klinkt het hetzelfde?",
            opdracht="Schrijf ja of nee, en bij nee waarin het verschil zit.",
            oefeningen=[
                ("rij", [("their en there", "ja"), ("to en two", "ja"),
                         ("ship en sheep", "nee, de klinker is kort of lang"),
                         ("write en right", "ja")],
                 "Schrijf ja of nee.", WL),
                ("kort", "Welk woord klinkt als 'two' en betekent 'ook'?", "too", W),
                ("kort", "In 'think' en in 'this' staat th. Waarin verschillen ze?",
                 "in think is de th stemloos, in this stemhebbend", WL),
            ],
        ),
        dict(
            kop="Intonatie",
            opdracht="Schrijf of je stem aan het eind van de zin stijgt of daalt.",
            oefeningen=[
                ("rij", [("Are you coming?", "stijgt"), ("Where are you going?", "daalt"),
                         ("I live in Hasselt.", "daalt"), ("Did you see that?", "stijgt")],
                 "Schrijf stijgt of daalt.", W),
            ],
        ),
        dict(
            kop="Spelling",
            opdracht="Schrijf de gevraagde vorm.",
            oefeningen=[
                ("rij", [("stop + ing", "stopping"), ("make + ing", "making"),
                         ("study + verleden tijd", "studied"), ("carry + hij", "carries")],
                 "Schrijf de juiste spelling.", WW),
                ("rij", [("baby", "babies"), ("box", "boxes"),
                         ("knife", "knives"), ("boy", "boys")],
                 "Schrijf het meervoud.", W),
                ("kort", "Schrijf vier woorden die veel mensen fout spellen, juist.",
                 "bijvoorbeeld because, friend, beautiful, necessary, receive, definitely, address",
                 WL),
                ("kort", "Welke woorden krijgen in het Engels een hoofdletter die ze in het "
                         "Nederlands niet krijgen?",
                 "dagen, maanden, talen, landen en nationaliteiten; de seizoenen niet", WL),
            ],
        ),
        dict(
            kop="Verbeter de zin",
            opdracht="Elke zin bevat één fout. Schrijf de hele zin correct over.",
            oefeningen=[
                ("kort", "I have a adress in Hasselt.", "I have an address in Hasselt.", WL),
                ("kort", "She studyed all evening.", "She studied all evening.", WL),
                ("kort", "There are three boxs on the table.", "There are three boxes on the table.", WL),
                ("kort", "We go swimming every monday.", "We go swimming every Monday.", WL),
                ("kort", "I dont know the answer.", "I don't know the answer.", WL),
            ],
        ),
        dict(
            kop="Voor het echte leven",
            opdracht="Deze oefening maak je op papier, maar ze is pas af als je ze hardop gedaan "
                     "hebt.",
            oefeningen=[
                ("open", "Zoek de tekst van een Engels liedje dat je goed kent. Schrijf drie "
                         "woorden op waar je iets anders hoorde dan er staat, en schrijf erbij "
                         "welke letter je niet hoorde of welke klank anders was.",
                 "Eigen antwoord. Het gaat erom dat je merkt hoe ver het schriftbeeld van de klank "
                 "kan liggen.", 8),
            ],
        ),
    ],
)

NIEUWE_BUNDELS["oefenbundel-spreken-gesprekken-en-hoe-je-beoordeeld-wordt" + NIEUW] = dict(
    vak=VAK,
    niveau=DF,
    titel="Spreken, gesprekken en hoe je beoordeeld wordt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(
            kop="Wat zeg je?",
            opdracht="Schrijf één Engelse zin die past bij wat er gevraagd wordt.",
            oefeningen=[
                ("kort", "Je spreekt een onbekende aan op de trein.",
                 "bijvoorbeeld: Excuse me, is this seat free?", WL),
                ("kort", "Je nodigt een vriend uit voor je verjaardag.",
                 "bijvoorbeeld: Would you like to come to my party?", WL),
                ("kort", "Je bedankt iemand die je geholpen heeft.",
                 "bijvoorbeeld: Thank you very much for your help.", WL),
                ("kort", "Je verontschuldigt je omdat je te laat bent.",
                 "bijvoorbeeld: I'm sorry I'm late.", WL),
                ("kort", "Iemand anders verontschuldigt zich. Wat antwoord je?",
                 "bijvoorbeeld: That's all right, don't worry.", WL),
                ("kort", "Je neemt afscheid na een gesprek.",
                 "bijvoorbeeld: It was nice talking to you. See you tomorrow.", WL),
            ],
        ),
        dict(
            kop="Beleefd of niet?",
            opdracht="Schrijf bij elke zin of ze gepast is tegenover iemand die je niet kent. "
                     "Is ze dat niet, schrijf dan een betere zin.",
            oefeningen=[
                ("kort", "Tell me when the bus leaves.",
                 "niet gepast: Could you tell me when the bus leaves?", WL),
                ("kort", "Could you speak more slowly, please?", "gepast", WW),
                ("kort", "I want to know how I can register.",
                 "beter: I would like to know how I can register.", WL),
                ("kort", "That's not my problem.",
                 "niet gepast: I'm sorry to hear that, how can I help?", WL),
            ],
        ),
        dict(
            kop="Een gesprek gaande houden",
            opdracht="Schrijf telkens één Engelse vraag waarmee je de ander verder laat vertellen.",
            oefeningen=[
                ("open", "Je gesprekspartner vertelt dat hij vorig jaar in Ierland was. Schrijf "
                         "drie vragen die het gesprek verder helpen.",
                 "bijvoorbeeld: What did you do there? How long did you stay? Would you go back?", 6),
                ("kort", "Je hebt iets niet begrepen. Wat vraag je?",
                 "Could you repeat that, please?", WL),
                ("kort", "De ander spreekt te snel. Wat vraag je?",
                 "Could you speak more slowly, please?", WL),
            ],
        ),
        dict(
            kop="Waarop word je beoordeeld?",
            opdracht="Vul aan.",
            oefeningen=[
                ("tabel", ["Vereiste", "Geldt voor"],
                 [["taakvoltooiing", None], ["lichaamstaal", None],
                  ["spelling en leestekens", None], ["uitspraak en intonatie", None]],
                 "taakvoltooiing: allebei; lichaamstaal: alleen mondeling; spelling en leestekens: "
                 "alleen schriftelijk; uitspraak en intonatie: alleen mondeling", WW),
                ("kort", "Wat betekent taakvoltooiing?",
                 "je doel is bereikt en je opdracht is volledig uitgevoerd", WL),
                ("kort", "Wat is een gepast register op een examen?",
                 "neutraal of informeel, aangepast aan wie voor je zit, zonder scheldwoorden", WL),
                ("waar", "Een valse start of een herformulering maakt je spreekopdracht meteen "
                         "onvoldoende.", False),
                ("waar", "Je uitspraak moet helder genoeg zijn om je boodschap niet in de weg te "
                         "staan; een accent is geen fout.", True),
            ],
        ),
        dict(
            kop="Strategieën",
            opdracht="Beantwoord kort.",
            oefeningen=[
                ("open", "Je kent het Engelse woord voor 'kruk' niet, maar je moet het zeggen. "
                         "Schrijf op wat je dan zegt.",
                 "Je omschrijft het met woorden die je wel kent, bijvoorbeeld: the sticks you walk "
                 "with after you break a leg.", 4),
                ("kort", "Je gesprekspartner begrijpt je niet. Wat doe je?",
                 "je zegt het op een andere manier, niet luider", WL),
                ("kort", "Wat is een spreekplan met kernwoorden?",
                 "een lijstje van wat je in welke volgorde wil zeggen", WL),
                ("open", "Schrijf de vier vragen van het communicatiemodel op die je jezelf stelt "
                         "voor je begint te spreken.",
                 "Waarom spreek ik? Voor wie is mijn boodschap? Met wie communiceer ik? Wat wil ik "
                 "precies vertellen? En: via welk kanaal?", 6),
            ],
        ),
        dict(
            kop="Het examen",
            opdracht="Vul aan.",
            oefeningen=[
                ("rij", [("duur van het digitale examen", "150 minuten"),
                         ("duur van het gesprek", "10 minuten"),
                         ("voorbereidingstijd voor het gesprek", "15 minuten"),
                         ("aantal opdrachten bij het gesprek", "2")],
                 "Vul in.", WW),
                ("kort", "Wanneer dien je je spreekopdracht ten laatste in?",
                 "tot drie dagen voor je digitale examen", WL),
                ("kort", "Hoeveel wegen lezen en luisteren samen?", "60 procent", W),
                ("waar", "Er is giscorrectie: voor een fout antwoord gaan er punten af.", False),
            ],
        ),
        dict(
            kop="Voor het echte leven",
            opdracht="Deze oefening maak je op papier, maar ze is pas af als je ze hardop gedaan "
                     "hebt.",
            oefeningen=[
                ("open", "Schrijf een spreekplan met kernwoorden voor twee minuten over wat je "
                         "vandaag gedaan hebt. Neem jezelf daarna op met je gsm, luister terug, en "
                         "schrijf op waar je stilviel en welk woord je zocht.",
                 "Eigen antwoord. Het kernwoordenplan is het doel: wie zijn tekst uitschrijft, "
                 "leest voor, en dat hoor je.", 9),
            ],
        ),
    ],
)

OEFENBUNDELS = bouw()

if __name__ == "__main__":
    import oefenbundel

    for sleutel, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, sleutel)
        print(" ", sleutel)
