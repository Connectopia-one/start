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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-een-engelse-tekst-analyseren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de tekst eerst één keer helemaal door zonder te stoppen bij woorden die je niet kent. Het onderwerp is waarover de tekst gaat, in een paar woorden. De hoofdgedachte is wat hij daarover zegt, in één hele zin.",
            waarom=[
                "Het onderwerp is geen zin. Zet er geen werkwoord bij, want dan maak je er de hoofdgedachte van.",
                "Een goede hoofdgedachte bevat hier twee delen: de bus rijdt, maar hij dreigt te verdwijnen. Alleen het eerste deel is te weinig, want dan mist de kern van de tekst.",
                "Elk uur tussen middernacht en vier uur: dat zijn de bussen van 0, 1, 2, 3 en 4 uur, dus vijf. Let op zulke vragen, want tussen twee uren tellen doe je snel één bus te weinig.",
                "Dit is een letterlijke vraag: beide helften staan er zo in (meant for people who work late shifts, most passengers have been students). Schrijf dan over wat er staat, verzin er niets bij.",
                "Dit is de afleidvraag. Twee zinnen samen geven het antwoord: de bus van vier uur is bijna altijd leeg, en de gemeente schrapt de dienst als er niet meer volk komt. Er staat nergens letterlijk dat hij verdwijnt, maar het volgt wel uit de tekst.",
                "Unless betekent if not: tenzij. Unless more people start using it is dus hetzelfde als if more people do not start using it.",
            ],
        ),
        dict(
            aanpak="Bij een beoordeling zoek je eerst de toon in het geheel, en daarna de uitzondering. Woorden als the only thing, but en however wijzen het ene punt van kritiek aan.",
            waarom=[
                "The only thing I would change verraadt dat er maar één minpunt is, en Absolutely op het einde maakt het oordeel duidelijk. Dus gemengd, maar overwegend positief.",
                "Het staat er bijna letterlijk: the only thing I would change is the starting time. Alles ervoor en erna is lof.",
                "To fly by is een vaste uitdrukking: voorbijvliegen. Zo'n uitdrukking vertaal je nooit woord voor woord, want vliegen heeft er niets mee te maken.",
                "Een beoordeling geeft een mening en wil je overtuigen om iets wel of niet te doen. Dat is opiniërend. Informatief zou alleen de feiten geven: de uren, de prijs, de duur.",
            ],
        ),
        dict(
            aanpak="Tussen de regels lezen is: wat volgt hieruit, ook al staat het er niet? Zoek het woordje dat het verschil maakt: unlike, who, on, under. Dat kleine woord draagt de hele betekenis.",
            waarom=[
                "Unlike his brother betekent in tegenstelling tot zijn broer. Als Tom het niet kan en hij is de uitzondering, dan kan de broer het wel.",
                "Beide gelden, dus een feestdag op een zondag valt onder allebei de regels. Een stapelvraag: twee voorwaarden tegelijk.",
                "In under ten minutes is minder dan tien minuten. Dat men het zo opschrijft, zegt dat het opvallend snel was.",
                "Will watch from the side is een nette manier om te zeggen dat je er niet in mag. Engels zegt zo'n regel vaak in de toekomende tijd en zonder het woord niet.",
            ],
        ),
        dict(
            aanpak="Zoek in elke uitspraak het woord dat ze te streng maakt (alleen, altijd, eerst, moet), of de twee begrippen die omgedraaid zijn.",
            waarom=[
                "Het staat omgekeerd. Het onderwerp is enkele woorden, de hoofdgedachte is één hele zin.",
                "Dat is precies het verschil tussen afleiden en overschrijven. Je antwoord moet uit de tekst volgen, maar het hoeft er niet in te staan.",
                "Vertalen kost tijd die je op een examen niet hebt, en het is ook niet nodig: je begrijpt een tekst meestal al met zeventig of tachtig procent van de woorden.",
                "Dit heet scannen: je laat je ogen over de tekst gaan tot je de vorm ziet die je zoekt, een uur, een getal, een naam.",
                "De titel en de eerste en laatste zin dragen de hoofdgedachte bijna altijd mee. Dat is sneller dan heel de tekst nog eens lezen.",
            ],
        ),
        dict(
            aanpak="Een nieuwsfilmpje is kort en heeft een duidelijke structuur, dus het is de beste oefening voor onderwerp en hoofdgedachte.",
            waarom=[
                "Er is geen juist antwoord. Wie na één keer kijken het onderwerp al heeft, zit goed; voor de hoofdgedachte heb je meestal een tweede keer nodig, en dat is normaal.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-tekstsoorten-tekstverbanden-en-verwijswoorden-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk fragment af wat het met jou wil doen. Je iets laten doen is prescriptief, je iets laten weten informatief, je iets laten kopen persuasief, je iets laten vinden opiniërend, je iets laten meemaken narratief, en je iets laten voelen met beeldspraak literair.",
            waarom=[
                "De vorm verraadt het. Een gebiedende wijs zonder onderwerp (shake, do not take) is prescriptief. Data en plaatsen zonder mening zijn informatief. Een oproep plus een reden om nu te handelen (give blood today) is persuasief.",
                "If you ask me is het signaal van een mening. Een rij gebeurtenissen in het verleden is een verhaal. En de wind die brieven leest kan niet letterlijk: dat is beeldspraak, dus literair.",
            ],
        ),
        dict(
            aanpak="Leer signaalwoorden in paren, want ze komen per twee of drie voor hetzelfde verband. Oorzaak: because, since, as. Gevolg: so, therefore, as a result. Tegenstelling: but, however, although, despite, yet.",
            waarom=[
                "Let op het verschil tussen because en therefore: because staat vóór de oorzaak, therefore vóór het gevolg. Dezelfde inhoud, omgekeerde volgorde.",
                "Unlike legt een vergelijking door een verschil aan te wijzen. Als het om een gelijkenis gaat, gebruik je like of similarly.",
                "Deze vier zijn er om apart te leren. Since betekent hier omdat, niet sinds. En yet betekent hier toch, niet nog. Welk van de twee het is, lees je aan de rest van de zin af.",
            ],
        ),
        dict(
            aanpak="Hier moet je niet alleen het verband kennen maar ook waar het woord mag staan. Although krijgt een hele zin achter zich, despite een naamwoord, en so verbindt twee zinnen.",
            waarom=[
                "So verbindt het gevolg aan de oorzaak die ervoor staat. Therefore kan ook, maar dan met een punt of een puntkomma ervoor.",
                "Although staat vooraan en krijgt een hele zin achter zich (onderwerp plus persoonsvorm). But kan dat niet: dat staat altijd tussen de twee zinnen in.",
                "For instance en for example zijn uitwisselbaar. Let op de komma erna, die hoort erbij.",
                "Dit is de reden waarom despite en although niet uitwisselbaar zijn. Despite krijgt een naamwoord achter zich (despite the rain), although een hele zin (although it rained). Despite of the rain is fout; dan moet het in spite of zijn.",
            ],
        ),
        dict(
            aanpak="Een verwijswoord zoek je altijd in wat ervoor staat. Let op het verschil: she of he wijst naar een persoon, this of that naar een heel idee of een hele gebeurtenis, en it kan naar allebei wijzen.",
            waarom=[
                "She is enkelvoud en vrouwelijk, en er is maar één vrouw genoemd.",
                "Dit is het verschil met she. This wijst hier niet naar de toets maar naar het schrappen ervan, dus naar wat er in de vorige zin gebeurde. Dat kan het Engels met één woord.",
                "It verwijst hier naar de hele toestand van de vorige zin: het ijs en de late bussen samen. Zoek bij it dus niet altijd één woord.",
                "Her verwijst in de gewone lezing naar het onderwerp van de zin, dus naar Ann. Strikt genomen is de zin dubbelzinnig, en dat is precies waarom je in je eigen tekst beter de naam herhaalt als er twijfel kan zijn.",
            ],
        ),
        dict(
            aanpak="Let in deze uitspraken op twee dingen: woorden die te absoluut zijn (alleen, altijd), en twee begrippen die als gelijk voorgesteld worden terwijl ze dat niet zijn.",
            waarom=[
                "Een reisverslag kan narratief en informatief tegelijk zijn, een reclametekst persuasief en informatief. Je zoekt dus de hoofdfunctie, niet de enige.",
                "Ze dragen de redenering. Haal je ze weg, dan staan er losse zinnen zonder verband, en de lezer moet zelf raden hoe ze samenhangen.",
                "Een bijsluiter zegt wat je moet doen, in de gebiedende wijs en zonder onderwerp. Dat is de definitie van prescriptief.",
                "Therefore is een gevolg (dus), however een tegenstelling (echter). Precies het omgekeerde van elkaar, en toch worden ze vaak verwisseld.",
                "Although opent een zin en krijgt een hele zin achter zich. But staat tussen de twee zinnen in. Zie ook oefening 7.",
            ],
        ),
        dict(
            aanpak="Een podcast of een gesprek bevat veel meer signaalwoorden dan een verhaal, want daar wordt geredeneerd. Daarom werkt deze oefening het best met een discussie.",
            waarom=[
                "Er is geen juist antwoord. Vier of vijf signaalwoorden in tien minuten is normaal. Hoor je er geen, dan luister je waarschijnlijk naar een verhaal in plaats van naar een gesprek.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-de-engelstalige-wereld-gewoontes-en-conventies-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Brits en Amerikaans Engels verschillen in een paar honderd woorden. De handigste manier om ze te leren is in paren, want dan onthoud je meteen welke van de twee welke is.",
            waarom=[
                "Vier paren, telkens Brits tegenover Amerikaans: lift en elevator, holiday en vacation, lorry en truck, petrol en gas. Let op gas, dat in het Amerikaans benzine betekent en niet gas.",
                "Football is de lastigste: in Brits Engels is dat voetbal, in Amerikaans Engels is football iets heel anders en heet voetbal soccer. En crisps zijn chipszakjes, terwijl Amerikaanse chips net de frieten zijn (Brits: chips).",
            ],
        ),
        dict(
            aanpak="De spellingverschillen volgen een paar vaste patronen: Brits our waar Amerikaans or schrijft, Brits re waar Amerikaans er schrijft, en Brits een dubbele l waar Amerikaans er één schrijft.",
            waarom=[
                "Vier patronen in één rij: colour en favourite (our), centre (re), travelled (dubbele l). Dezelfde regels gelden voor neighbour, theatre en cancelled.",
            ],
        ),
        dict(
            aanpak="Deze vragen gaan over misverstanden die in het echt geld of tijd kosten: verdiepingen, data, temperaturen en afstanden. Leer ze één keer goed, dan heb je er je leven lang iets aan.",
            waarom=[
                "In het Brits is the ground floor het gelijkvloers en the first floor de eerste verdieping, dus een trap hoger. In het Amerikaans is the first floor net wel het gelijkvloers. Bij twijfel vraag je het na.",
                "Brits schrijft dag/maand/jaar, zoals wij. Amerikaans schrijft maand/dag/jaar, dus 9/12 is daar 12 september. Dat is de meest verwarrende van allemaal; schrijf in een mail daarom de maand voluit: 9 December 2027.",
                "Fahrenheit naar Celsius: trek er 30 af en deel door twee, dan zit je er dicht bij. 95 min 30 is 65, gedeeld door twee is ongeveer 32, en het juiste antwoord is 35. Goed genoeg om te weten dat het warm is.",
                "To queue is in de rij staan, en in het Verenigd Koninkrijk is dat bijna een instituut. Voorsteken valt er zwaarder dan bijna elke andere onbeleefdheid.",
                "Eén mile is ongeveer 1,6 km. Tien miles is dus ongeveer 16 km. Voor het omgekeerde deel je door 1,6.",
            ],
        ),
        dict(
            aanpak="Aanhef en afsluiter horen in het Engels bij elkaar als een paar. Ken je de naam niet, dan is het Dear Sir or Madam met Yours faithfully. Ken je de naam wel, dan Dear Mr of Ms met Yours sincerely.",
            waarom=[
                "De vuistregel die je nergens moet opzoeken: faithfully bij een naamloze aanhef, sincerely bij een naam. In het informele geval mag alles losser: Hi Sam met Best wishes, See you soon of Take care.",
                "Ms spreek je uit als miz. Het is het Engelse antwoord op het feit dat Mr niets zegt over getrouwd zijn en Mrs of Miss wel. In een zakelijke brief gebruik je altijd Ms, tenzij iemand zelf anders tekent.",
            ],
        ),
        dict(
            aanpak="Beleefdheid zit in het Engels in de vorm van je vraag, niet in een extra woord. Maak van een bevel een vraag met could you, of van een eis een wens met I would like.",
            waarom=[
                "Could you is de veiligste opener die er is: hij werkt bij elke vraag en tegen iedereen. Can you kan ook, maar klinkt directer.",
                "I want klinkt in het Engels als eisen. I would like (of I'd like) is de normale vorm in een winkel, een hotel of een restaurant.",
                "Twee dingen tegelijk: could you ervoor en please erachter. Please alleen volstaat niet om een bevel beleefd te maken.",
                "Het Engels verwacht hier een geruststelling, niet alleen een knikje. That's all right, no problem of don't worry about it horen erbij, en een stilte leest als verwijt.",
            ],
        ),
        dict(
            aanpak="Vier feesten die in bijna elke Engelstalige tekst en reeks terugkomen. Twee ervan hebben een vaste datum, twee niet.",
            waarom=[
                "Thanksgiving is de enige zonder vaste datum: de vierde donderdag van november, in de Verenigde Staten. Canada viert het al in oktober. St Patrick's Day is Iers, Independence Day Amerikaans, en Halloween wordt zowat overal gevierd.",
            ],
        ),
        dict(
            aanpak="Let op twee dingen: een uitspraak die twee namen gelijkstelt die niet hetzelfde betekenen, en een uitspraak die iets over gewoontes beweert.",
            waarom=[
                "England is één land. Great Britain is Engeland, Schotland en Wales samen, en the United Kingdom is dat plus Noord-Ierland. Een Schot England zeggen is geen kleine vergissing.",
                "Kies er één en hou je eraan, in heel je tekst. Colour en center door elkaar leest als slordigheid, en het staat ook zo in de beoordelingscriteria.",
                "In de Verenigde Staten hoort een fooi van ongeveer vijftien tot twintig procent bij de rekening, want het loon van het personeel rekent erop. In het Verenigd Koninkrijk is dat veel minder vanzelfsprekend.",
                "Engels is officiële taal in meer dan vijftig landen, waaronder India, Zuid-Afrika, Nigeria, Singapore en Ierland. Daarom hoor je zoveel verschillende accenten op een luisterexamen.",
                "Het Engels gebruikt please, thank you en sorry véél vaker dan wij. Waar wij dank je zeggen, zegt een Brit vaak drie keer thanks in hetzelfde gesprek. Te weinig danken leest daar als onbeleefd.",
            ],
        ),
        dict(
            aanpak="Een uur kijken is genoeg om het verschil zelf te horen. Let niet alleen op woorden maar ook op uitspraak en op het weglaten van de r.",
            waarom=[
                "Er is geen juist antwoord. Denk aan lift en elevator, flat en apartment, rubbish en trash, queue en line, mate en buddy.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-schrijven-schriftelijke-interactie-en-literatuurbeleving-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk eerst wat de opdracht van je wil, want daar hangt je hele tekst van af: je toon, je opbouw en je lengte. Vertellen gaat in de verleden tijd, uitleggen in stappen, overtuigen met argumenten.",
            waarom=[
                "Let op het verschil tussen uitleggen en overtuigen. Uitleggen wil dat je lezer het snapt; overtuigen wil dat hij iets doet. Dat vraagt een heel andere tekst.",
                "En let op het verschil tussen informatie vragen en informatie geven. Het eerste is een mail vol vragen, het tweede een bericht vol feiten. Beide zijn kort, maar ze lijken verder niet op elkaar.",
            ],
        ),
        dict(
            aanpak="Dit zijn zes vaste functies die in bijna elke schrijfopdracht terugkomen. Leer er één goede zin per functie van vanbuiten, dan heb je altijd een opener.",
            waarom=[
                "Would you like to … is de standaarduitnodiging. Do you want to komt directer over, wat tussen vrienden kan maar verder niet.",
                "Belangstelling tonen is in het Engels bijna verplicht: zonder zo'n zin leest je bericht koel. How are you feeling now en I hope you're better doen hetzelfde.",
                "Thank you so much klinkt warmer dan thanks. En zet er altijd bij waarvoor je bedankt, want dat maakt het echt.",
                "Een verontschuldiging in het Engels bestaat uit twee delen: sorry plus een reden. Alleen sorry voelt afgeraffeld.",
                "Dit is het beleefde nee. I'd love to, but … erkent eerst de uitnodiging. I'm afraid is daarbij geen angst maar een verzachter: het hoort erbij.",
                "I would like to know how … is de veilige opener voor elke vraag om informatie. Direct beginnen met How can I register klinkt kort.",
            ],
        ),
        dict(
            aanpak="De beoordelingscriteria zijn de lijst waarop je je eigen tekst kan nakijken voor je ze afgeeft. Vier punten, en ze meten vier verschillende dingen.",
            waarom=[
                "Zet ze in volgorde van gewicht: taakvoltooiing eerst, want een foutloze tekst die de opdracht niet uitvoert, haalt daar niets. Daarna de structuur, dan het register, dan de lay-out.",
                "Taakvoltooiing is het woord dat je moet kennen, want het komt op elk verbeterblad terug.",
                "Op taakvoltooiing, niet op grammatica. Het aantal woorden hoort bij de opdracht, en de helft schrijven betekent dat je ze niet volledig uitgevoerd hebt. Tel je woorden dus echt.",
            ],
        ),
        dict(
            aanpak="Een woord omschrijven in plaats van opzoeken is een vaardigheid waarvoor je punten krijgt. Begin met wat het is (a thing, a person, a place) en zeg daarna waarvoor het dient.",
            waarom=[
                "Het patroon dat altijd werkt: the thing you use when … of someone who … Je hoeft het juiste woord niet te kennen om verstaanbaar te zijn.",
                "A fortnight is een woord dat je in het Brits Engels echt tegenkomt, ook in een treinregeling of een huurcontract. Het komt van fourteen nights.",
                "Someone who … is de opener voor elk beroep. Zo kan je elk beroep omschrijven dat je niet kent.",
                "Let op de spelling van receipt: de p schrijf je wel en hoor je niet. En het is niet hetzelfde als a recipe, een recept om te koken.",
            ],
        ),
        dict(
            aanpak="Een samenvatting zegt wat er in het boek staat en kan iedereen nakijken. Een leeservaring zegt wat het boek met jóu deed, en begint dus bij ik.",
            waarom=[
                "Zie het patroon: een zin die begint met The story of The book is een samenvatting; een zin die begint met I of made me is een leeservaring. Op een examen literatuurbeleving wordt het tweede gevraagd, en antwoorden van de eerste soort halen daar weinig.",
            ],
        ),
        dict(
            aanpak="Tel bij een schrijfopdracht eerst hoeveel vragen of punten erin zitten, en vink ze af in je antwoord. Dat is precies wat taakvoltooiing meet.",
            waarom=[
                "Drie vragen in de opdracht, dus drie vragen in je mail. En de aanhef hoort bij de afsluiter: Dear Sir or Madam gaat met Yours faithfully, want je kent de naam niet.",
                "Bij schriftelijke interactie mag je geen enkele vraag laten liggen, ook niet de kleine. Hier zijn het er twee: meekomen én de camera. Zelf een vraag terugstellen maakt het een echt gesprek.",
            ],
        ),
        dict(
            aanpak="Iemand je eigen tekst laten voorlezen is de snelste manier om te horen welke zinnen niet lopen. Jij leest over je eigen fouten heen, een ander niet.",
            waarom=[
                "Er is geen juist antwoord. Haperen gebeurt bijna altijd op dezelfde twee plaatsen: te lange zinnen, en een woordvolgorde die letterlijk uit het Nederlands komt.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-woordvelden-mensen-gezondheid-en-het-dagelijkse-leven-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het Engels maakt bij familie andere scheidingen dan wij. Let vooral op cousin, dat zowel neef als nicht kan zijn, en op nephew en niece, die alleen over het kind van je broer of zus gaan.",
            waarom=[
                "Bij ons is neef zowel het kind van je tante als de zoon van je zus. Het Engels houdt die uit elkaar: cousin voor het kind van je tante of oom, nephew en niece voor het kind van je broer of zus.",
                "Twee patronen: in-law voor aangetrouwd (mother-in-law, brother-in-law) en step voor een stiefband (stepmother, stepbrother). Beide schrijf je met streepjes of aan elkaar, nooit los.",
            ],
        ),
        dict(
            aanpak="Formuliertaal is een klein lijstje dat op elk formulier terugkomt: in een hotel, bij een inschrijving, in een sollicitatie. Leer het één keer en je herkent het overal.",
            waarom=[
                "Surname is je achternaam (ook family name of last name), en first name of forename je voornaam. Marital status vraagt of je single, married of divorced bent, en occupation je beroep, niet je hobby.",
            ],
        ),
        dict(
            aanpak="Bij gevoelens en gezondheid let je op twee dingen: de spelling van een paar lastige woorden, en de vaste uitdrukkingen die je niet woord voor woord kan vertalen.",
            waarom=[
                "Disappointed: één s, dubbele p. Het is een van de vaakst verkeerd gespelde woorden van het Engels.",
                "Cheerful is opgewekt, gloomy is somber. Denk aan gloom, duisternis.",
                "A sore throat is de vaste uitdrukking. Sore betekent pijnlijk en past bij meer lichaamsdelen: a sore back, sore feet.",
                "Under the weather betekent zich niet lekker voelen, en heeft niets met het weer te maken. Zulke uitdrukkingen moet je in hun geheel leren.",
                "The chemist's is in het Verenigd Koninkrijk de apotheek, in de Verenigde Staten is dat the drugstore of the pharmacy. Let op de 's: die staat er omdat het eigenlijk het huis van de chemist is, net als bij the butcher's en the baker's.",
            ],
        ),
        dict(
            aanpak="Lichaamsdelen leer je het best per lichaamsdeel waar ze aan vastzitten: dan onthoud je ze in groepjes in plaats van als losse lijst.",
            waarom=[
                "Elbow en wrist horen bij de arm, ankle bij het been. Pas op dat je wrist (pols) en ankle (enkel) niet verwisselt: ze doen hetzelfde werk aan een ander lid.",
                "Hip is de heup en hoort bij het been, shoulder de schouder en hoort bij de arm. Throat is de keel, van binnen; neck is de hals, van buiten.",
            ],
        ),
        dict(
            aanpak="Do en make zijn allebei doen of maken, en je kan ze niet vertalen. Vuistregel: do bij werk en taken, make bij iets dat uit het niets ontstaat.",
            waarom=[
                "Do the washing-up, do your homework, do the shopping: allemaal taken. Make the bed, make a mistake, make a cake, make a decision: allemaal iets dat er daarvoor niet was. De vuistregel dekt het meeste; de rest leer je per uitdrukking.",
            ],
        ),
        dict(
            aanpak="Vier zinnen, vier verschillende valkuilen: een ontelbaar woord, een woord dat altijd meervoud is, een maat bij een ontelbaar woord, en een adjectief dat nooit een s krijgt.",
            waarom=[
                "Hair is ontelbaar als je het over je kapsel hebt, dus enkelvoud: my hair is long. A hair met een s bestaat ook, maar dan gaat het over losse haren in je soep.",
                "Trousers is altijd meervoud, net als jeans, glasses en scissors. Wil je er één bedoelen, dan zeg je a pair of trousers.",
                "Bread is ontelbaar, dus je telt de verpakking: two loaves of bread, a slice of bread. Hetzelfde met advice, information, furniture en news.",
                "Een Engels adjectief krijgt nooit een meervoud. Two red jackets, niet two reds jackets. Dat is meteen het grootste verschil met het Nederlands en het Frans.",
            ],
        ),
        dict(
            aanpak="Let op de valse vrienden: woorden die eruitzien als een Nederlands woord maar iets anders betekenen. En let op de verdiepingen, want die scheelt er één.",
            waarom=[
                "Het Britse ground floor is ons gelijkvloers; de first floor is een trap hoger. In de Verenigde Staten is the first floor net wél het gelijkvloers.",
                "A starter is het voorgerecht, the main course het hoofdgerecht en pudding of dessert het nagerecht. In de Verenigde Staten heet het voorgerecht an appetizer, en an entrée is daar verwarrend genoeg het hoofdgerecht.",
                "Dit is de valse vriend. Ons arm betekent in het Engels poor; het Engelse arm is het lichaamsdeel.",
                "English, Belgian, French, Dutch: in het Engels krijgen nationaliteiten, talen, maanden en weekdagen allemaal een hoofdletter. Het Nederlands doet dat bij maanden en dagen niet, dus daar gaat het mis.",
                "Washing-up liquid is afwasmiddel, voor de handafwas. Waspoeder voor de machine is washing powder of laundry detergent. Eén streepje verschil, een heel ander product.",
            ],
        ),
        dict(
            aanpak="Woorden die je elke dag vastneemt, blijven beter hangen dan woorden uit een lijst, want je ziet het voorwerp erbij.",
            waarom=[
                "Er is geen juist antwoord. Wie tien woorden opschrijft en er de dag erna zes onthoudt, doet het goed.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-woordvelden-school-werk-reizen-en-de-samenleving-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Instructietaal is de woordenschat van de opgaven zelf. Ken je ze niet, dan kan je een tekst perfect begrijpen en toch het verkeerde doen.",
            waarom=[
                "The odd one out is het woord dat niet in het rijtje past. Dat is een opdracht die op een examen vaak terugkomt.",
                "Let op summarise: dat is de enige van de zes waar je zelf moet schrijven. De andere vijf vragen alleen een vinkje, een streep of een verbinding.",
            ],
        ),
        dict(
            aanpak="Schoolwoorden verschillen tussen het Brits en het Amerikaans, en een paar zien er anders uit dan je verwacht. Leer de Britse, want daar is het Engels van de Examencommissie op gericht.",
            waarom=[
                "A subject is een vak, geen onderwerp van een tekst (dat is a topic). En a term is een trimester; het schooljaar heeft er in het Verenigd Koninkrijk drie.",
                "To sit an exam is de Britse uitdrukking, letterlijk een examen zitten. To take an exam kan ook, en is Amerikaans.",
                "Resit, met het voorvoegsel re voor opnieuw. Zo ook rewrite, rebuild, rethink: dat voorvoegsel maakt in het Engels moeiteloos nieuwe woorden.",
            ],
        ),
        dict(
            aanpak="Beroepen zijn woordenschat die je op een examen bij elk thema kan tegenkomen. Een paar lijken op niets dat je kent, en net die moet je leren.",
            waarom=[
                "Een midwife is letterlijk een vrouw die met je mee is (mid betekende oorspronkelijk samen met). An estate agent is een makelaar; in de Verenigde Staten heet dat a real estate agent of a realtor.",
                "A solicitor is een advocaat die advies geeft en dossiers voorbereidt; a barrister is er een die voor de rechtbank pleit. In de Verenigde Staten heet het allebei a lawyer, of an attorney.",
            ],
        ),
        dict(
            aanpak="De woorden rond werk komen in elke sollicitatietekst terug. Let op de voorzetsels, want die moet je samen met het werkwoord leren.",
            waarom=[
                "To apply for a job, en to apply to a company. Het voorzetsel hoort bij het werkwoord en is niet te vertalen.",
                "To resign is zelf ontslag nemen. Verwar het niet met to be fired, dat ontslagen worden betekent omdat je iets fout deed.",
                "To be made redundant betekent ontslagen worden omdat de functie verdwijnt, niet omdat je slecht werkte. Dat verschil telt in het Engels, ook sociaal.",
                "Work is ontelbaar, zoals bread en advice: je kan het niet tellen en er komt geen s aan. Eén baan is a job, twee banen are two jobs.",
            ],
        ),
        dict(
            aanpak="Dit zijn woorden die je in het echt nodig hebt aan een loket, in een winkel of op een station. Een paar ervan betekenen in het Brits iets heel anders dan je zou denken.",
            waarom=[
                "A return ticket is heen en terug, a single ticket alleen heen. In de Verenigde Staten heet dat a round-trip ticket en a one-way ticket.",
                "Dit is de val. In het Verenigd Koninkrijk is a subway een voetgangerstunnel; de metro heet daar the Underground of the Tube. In de Verenigde Staten is the subway wél de metro.",
                "Delayed betekent vertraagd, cancelled afgeschaft. Op een bord staat vaak alleen het getal erbij, dus delayed by 20 minutes.",
                "A refund is je geld terug. Wil je een ander exemplaar, dan vraag je a replacement of an exchange.",
                "Zonder receipt (kasticket) krijg je in de meeste winkels geen geld terug. Let weer op die stomme p in de spelling.",
                "At the newsagent's, weer met die 's. Dezelfde bouw als the chemist's, the butcher's en the baker's.",
            ],
        ),
        dict(
            aanpak="Het uur zeggen gaat in het Engels met past tot het halfuur en met to erna. En let op een paar weerwoorden die je nergens anders tegenkomt.",
            waarom=[
                "Drizzle is motregen, een woord dat je in elke Britse weerberichtgeving hoort. En freezing is in spreektaal gewoon ijskoud, ook als het niet vriest.",
                "Past betekent over, to betekent voor: half past seven is half acht bij ons, quarter to nine is kwart voor negen. Let op half past seven, want dat is 7.30 en niet 6.30. Een fortnight is twee weken.",
            ],
        ),
        dict(
            aanpak="Bij sporten kiest het Engels tussen drie werkwoorden, en dat is geen gevoel maar een regel: play bij een sport met een bal of een tegenstander, go bij een sport op ing, do bij de rest.",
            waarom=[
                "Play football, play tennis (bal en tegenstander), go swimming, go running, go cycling (de ing-vorm), do yoga, do judo, do athletics (de rest). Die drie groepen dekken bijna alle sporten.",
            ],
        ),
        dict(
            aanpak="Eén echte vraag stellen in het Engels doet meer voor je zelfvertrouwen dan tien oefeningen, want er zit een echt antwoord aan vast.",
            waarom=[
                "Er is geen juist antwoord. Mailen mag, bellen leert meer: dan moet je ook luisteren, en dat is net het stuk dat je niet kan oefenen op papier.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-nouns-articles-quantifiers-en-numerals-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het Engelse meervoud is meestal een s, maar er zijn vier groepen uitzonderingen: woorden op y, woorden op f, woorden met een eigen vorm, en woorden die niet veranderen. Leer ze per groep.",
            waarom=[
                "Een y na een medeklinker wordt ies (country, countries), maar een y na een klinker niet (key, keys). En na een sisklank komt es: box, boxes.",
                "Een f of fe wordt ves: leaf, leaves; wolf, wolves. Potato en tomato krijgen es, maar photo en piano niet. Crisis wordt crises, zoals analysis en thesis: een Grieks patroon.",
                "Vier onregelmatige: man, men; tooth, teeth; goose, geese; person, people. Person heeft ook persons, maar dat gebruik je bijna alleen in juridische taal.",
                "Sheep, fish, series en species blijven gelijk. Toothbrush krijgt es vanwege de sisklank, en dat is dus een gewoon meervoud ondanks tooth.",
            ],
        ),
        dict(
            aanpak="Een ontelbaar woord staat nooit in het meervoud en krijgt een enkelvoudig werkwoord. De Engelse lijst is langer dan je denkt, en net die woorden gebruik je vaak.",
            waarom=[
                "Advice en furniture zijn ontelbaar, en wij zeggen wel adviezen en meubels. Daar gaat het dus mis. Wil je er één bedoelen, dan zeg je a piece of advice of a piece of furniture.",
                "News is ontelbaar en toch eindigt het op een s, dus het krijgt een enkelvoudig werkwoord: the news is good. Work is ontelbaar, a job telbaar.",
            ],
        ),
        dict(
            aanpak="De bezitsvorm met 's gebruik je bij mensen en dieren; bij voorwerpen zeg je of. Let op waar de apostrof staat bij een meervoud.",
            waarom=[
                "Bij een meervoud dat al op s eindigt, komt de apostrof erna: the girls' room. Bij een onregelmatig meervoud zonder s komt 's erbij: the children's toys. En bij een voorwerp gebruik je of: the roof of the house, niet the house's roof.",
            ],
        ),
        dict(
            aanpak="A of an hangt af van de klánk die volgt, niet van de letter. En bij een algemeen begrip (schoolvakken, talen, muziek) staat er in het Engels helemaal geen lidwoord.",
            waarom=[
                "An hour met an, want de h is stom en je hoort een klinker. En history en English krijgen niets, want het gaat over het vak en de taal in het algemeen.",
                "Dit zijn de twee valstrikken. A university met a, want je hoort joe, een medeklinkerklank. An honest man met an, want de h is stom. En the book you lent me krijgt wél the, want het is dat ene boek.",
            ],
        ),
        dict(
            aanpak="Much hoort bij ontelbaar, many bij telbaar. Hetzelfde paar: a little bij ontelbaar, a few bij telbaar.",
            waarom=[
                "Zoek eerst of het woord telbaar is. Water en salt kan je niet tellen, dus much en a little. Books en friends wel, dus many en a few. Let op: a few betekent enkele, few zonder a betekent weinig, en dat is bijna het omgekeerde.",
            ],
        ),
        dict(
            aanpak="Vijf klassieke fouten: het ontbrekende lidwoord bij een beroep, het werkwoord na a lot of people, het ontelbare news, some tegenover any, en een ontelbaar woord dat geteld wordt.",
            waarom=[
                "Bij een beroep staat in het Engels altijd a of an: he is a teacher. Dat is net het omgekeerde van het Frans en het Nederlands.",
                "People is een meervoud, dus there are. Let op: there is a lot of water klopt wel, want water is ontelbaar. Het werkwoord volgt het woord na of.",
                "News eindigt op een s maar is enkelvoud: the news is good. Zo ook mathematics, physics en politics.",
                "In een vraag en na een ontkenning wordt some meestal any. Some in een vraag kan wel als je iets aanbiedt: would you like some tea?",
                "Information is ontelbaar, dus je telt stukken: two pieces of information. Hetzelfde met advice, news en furniture.",
            ],
        ),
        dict(
            aanpak="Rangtelwoorden krijgen th, met drie uitzonderingen die je moet kennen: first, second, third. En let op de punt en de komma, want die staan in het Engels omgekeerd aan bij ons.",
            waarom=[
                "Drie spellingen om apart te leren: fifth (van five, zonder e), ninth (van nine, zonder e) en twelfth (van twelve, met f).",
                "Let op and voor het laatste stuk: that is Brits Engels. In het Amerikaans laat men het weg: one thousand two hundred fifty.",
                "Het Engels gebruikt een punt waar wij een komma zetten, en een komma waar wij een punt of een spatie zetten. 3,5 wordt dus 3.5 en 1.250 wordt 1,250. Op een examen met cijfers is dat de val.",
                "Hundred, thousand en million blijven in het enkelvoud als er een getal voor staat: two thousand people. Alleen zonder getal krijgen ze een s: thousands of people.",
            ],
        ),
        dict(
            aanpak="Getallen zijn het stuk van een luisterexamen dat het vaakst misgaat, want ze gaan snel voorbij en je kan ze niet uit de context afleiden.",
            waarom=[
                "Er is geen juist antwoord. Grote getallen en decimalen zijn wat je in een verslag het vaakst mist, precies omdat de punt en de komma anders staan dan bij ons.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-pronouns-de-vijf-soorten-en-de-onbepaalde-woorden-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes soorten voornaamwoorden, elk met hun eigen rijtje. Persoonlijk (I, me), bezittelijk (my, mine), wederkerend (myself), aanwijzend (this, those), vragend (who, which) en onbepaald (somebody, each).",
            waarom=[
                "Let op hers zonder apostrof: het bezittelijke voornaamwoord heeft er nooit een. En themselves eindigt op selves, het meervoud van self.",
                "Whose is vragend (van wie) en wordt verward met who's (who is). En each en every zijn onbepaald maar altijd enkelvoud: each pupil has a book.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk gat af welke functie het woord heeft. Doet het iets, dan neem je de onderwerpsvorm (I, she, they). Ondergaat het iets of staat er een voorzetsel voor, dan de voorwerpsvorm (me, her, them).",
            waarom=[
                "She and I staat vooraan, dus onderwerpsvorm; for her staat achter een voorzetsel, dus voorwerpsvorm. Its zonder apostrof is bezittelijk, en yours is het bezittelijke zonder naamwoord erachter.",
                "Himself en ourselves zijn wederkerend: het onderwerp doet iets aan zichzelf, of doet het zelf. Those is het meervoud van that, voor iets verder weg; these is het meervoud van this.",
            ],
        ),
        dict(
            aanpak="Its is bezittelijk en heeft nooit een apostrof. It's is altijd de samentrekking van it is of it has. De test: kan je it is of it has invullen, dan schrijf je it's.",
            waarom=[
                "Doe de test bij elk van de vier. The dog wagged it is tail klopt niet, dus its. It is raining klopt wel, dus it's. Dit is de meest gemaakte fout in het hele Engels, ook door moedertaalsprekers.",
            ],
        ),
        dict(
            aanpak="Zes zinnen, zes verschillende valkuilen. Kijk telkens eerst naar de functie van het woord in de zin, dan naar de vorm.",
            waarom=[
                "Beide staan vooraan als onderwerp, dus she and I. De test: laat de ander weg. Me went to the cinema klinkt meteen fout, I went wel.",
                "Theirselves bestaat niet. Het rijtje is myself, yourself, himself, herself, itself, ourselves, yourselves, themselves.",
                "Het Engels zet geen twee ontkenningen in één zin. Na didn't wordt nothing dus anything. I saw nothing kan wel, want dan staat er maar één ontkenning.",
                "Everybody, somebody, nobody en each zijn enkelvoud, hoeveel mensen het ook zijn. Dus was, niet were.",
                "Een vraag met een vraagwoord heeft in het Engels do, does of did nodig, behalve als het vraagwoord zelf het onderwerp is (zie oefening 15).",
                "Yours staat alleen, zonder naamwoord erachter. Staat er wel een naamwoord, dan is het your: your book.",
            ],
        ),
        dict(
            aanpak="Een zin is pas duidelijk als elk voornaamwoord maar naar één ding kan verwijzen. Twijfel je zelf, dan twijfelt je lezer ook: herhaal dan gewoon de naam.",
            waarom=[
                "He kan hier even goed Tom als Ben zijn. Engelse schrijvers lossen dat op door de naam te herhalen, ook al klinkt dat wat omslachtig: duidelijkheid gaat voor.",
                "Hier staan twee meervouden naast elkaar, dus they en them kunnen allebei twee kanten op. Eén van de twee vervangen door de naam volstaat.",
                "How much bij ontelbaar en bij een prijs (how much is this jacket), how many bij telbaar. Let op how many times: keren zijn telbaar.",
                "Who is hier zelf het onderwerp, dus er komt géén do bij: who wants tea. Vergelijk met who do you want to invite, waar who het voorwerp is en do er wél bij hoort.",
            ],
        ),
        dict(
            aanpak="Pijlen tekenen van een voornaamwoord naar zijn woord is de snelste manier om te zien of een tekst duidelijk is, en het helpt ook bij je eigen schrijven.",
            waarom=[
                "Er is geen juist antwoord. Twijfel ontstaat bijna altijd als twee mogelijke antwoorden hetzelfde geslacht of hetzelfde getal hebben.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-adjectives-adverbs-comparatives-en-voorzetsels-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een bijwoord maak je in het Engels met ly, maar er zijn drie spellingregels en een handvol woorden die niet meedoen.",
            waarom=[
                "Drie spellingen: een y wordt ily (easy, easily), een le wordt ly (terrible, terribly), en de rest krijgt gewoon ly erbij. Good is onregelmatig: het bijwoord is well.",
                "Fast en hard zijn al bijwoord zonder ly. Fastly bestaat niet, en hardly bestaat wel maar betekent iets anders (zie de volgende reeks).",
            ],
        ),
        dict(
            aanpak="Een bijvoeglijk naamwoord hoort bij een naamwoord, een bijwoord bij een werkwoord. Maar na de zintuigwerkwoorden (look, taste, smell, sound, feel) staat juist een bijvoeglijk naamwoord.",
            waarom=[
                "Sings is een gewoon werkwoord, dus well. Tastes en looks zijn zintuigwerkwoorden, dus delicious en happy, want ze zeggen iets over de soep en over hem, niet over het proeven of het kijken. Drive is een bevel met een gewoon werkwoord, dus carefully.",
            ],
        ),
        dict(
            aanpak="Hard en hardly zien eruit als een paar maar betekenen bijna het tegenovergestelde. Hard is hard of zwaar; hardly betekent nauwelijks.",
            waarom=[
                "De rest van de zin verraadt het: she is exhausted, dus ze heeft hard gewerkt.",
                "Hier ook: no excuse, dus hij heeft juist bijna niets gedaan. Hardly is een halve ontkenning, en daarom komt er geen tweede ontkenning bij.",
                "Lately betekent de laatste tijd. Late betekent laat, en lately is dus net geen bijwoord van late. Nog zo'n paar als hard en hardly.",
            ],
        ),
        dict(
            aanpak="Korte woorden krijgen er en est, lange woorden krijgen more en most. De grens ligt ongeveer bij twee lettergrepen, en een paar woorden zijn onregelmatig.",
            waarom=[
                "Let op de spelling: big wordt bigger met een dubbele g, easy wordt easier met een i. Expensive is lang, dus more expensive. Good en bad zijn onregelmatig: better en best, worse en worst.",
                "Not as hard as betekent minder moeilijk dan. As … as vergelijkt twee gelijke dingen; met not ervoor zeg je dat het ene minder is dan het andere.",
                "Dit is een vaste bouw: the more …, the easier … Twee keer the, en twee vergrotende trappen. Zoals hoe meer je oefent, hoe makkelijker het wordt.",
            ],
        ),
        dict(
            aanpak="Drie voorzetsels van tijd, drie vaste gebruiken. At bij een uur, on bij een dag of een datum, in bij een maand, een jaar of een deel van de dag. De uitzonderingen zijn at night en at the weekend.",
            waarom=[
                "At seven o'clock (uur), on Monday (dag), in July (maand), at night (uitzondering). In the night bestaat wel, maar betekent iets anders.",
                "In the morning met in, maar on Friday morning met on, want er staat een dag bij. Zodra er een dag in de uitdrukking zit, wint on.",
            ],
        ),
        dict(
            aanpak="Vaste voorzetsels horen bij het woord ervoor en zijn niet te vertalen. Leer ze als één geheel: wait for, listen to, good at, afraid of.",
            waarom=[
                "Wij zeggen wachten op en luisteren naar, en dat zijn precies de twee die je in het Engels fout kan vertalen. Good at (niet in) en afraid of horen er ook bij.",
                "Discuss krijgt geen voorzetsel: discuss the problem, niet discuss about. En arrive in bij een stad of een land, arrive at bij een gebouw of een station.",
            ],
        ),
        dict(
            aanpak="Vijf zinnen, vijf verschillende regels: het adjectief zonder meervoud, het bijwoord zonder ly, de versterking bij een vergrotende trap, de bouw van as … as, en een vast voorzetsel.",
            waarom=[
                "Een Engels adjectief krijgt nooit een meervoud: two red cars. Dit is de meest gemaakte fout van Nederlandstaligen.",
                "Fastly bestaat niet; fast is zelf al het bijwoord.",
                "Bij een vergrotende trap zeg je much better, far better of a lot better. Very hoort bij de gewone vorm: very good.",
                "As tall as, twee keer as. Than hoort bij de vergrotende trap (taller than), as bij de gelijkheid.",
                "Arrive at the station, want een station is een gebouw. Arrive in London, want dat is een stad. En arrive to bestaat niet.",
            ],
        ),
        dict(
            aanpak="Een kamer beschrijven is de oefening waarmee je in één minuut merkt welke alledaagse woorden je nog mist, en dat zijn er bij iedereen een paar.",
            waarom=[
                "Er is geen juist antwoord. De woorden die je niet vindt, zijn precies de woorden die je moet opzoeken; schrijf ze meteen op.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-de-tegenwoordige-tijden-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De present simple is overal dezelfde vorm, behalve bij he, she en it: daar komt een s bij. Alleen de spelling van die s heeft drie regeltjes.",
            waarom=[
                "Na een sisklank komt es: watches. Een y na een medeklinker wordt ies: flies. Een y na een klinker blijft: plays. En go wordt goes.",
                "Dezelfde drie regels: does en misses met es, carries met ies (want een medeklinker voor de y), fixes met es na de x.",
            ],
        ),
        dict(
            aanpak="De present simple is voor wat altijd of gewoonlijk zo is; de present continuous voor wat nu bezig is of voor een afspraak die vastligt. Zoek het signaalwoord.",
            waarom=[
                "Look en right now wijzen naar nu, dus continuous. A lot en every Saturday wijzen naar een gewoonte, dus simple.",
                "Twee bijzonderheden. Know is een werkwoord van denken en voelen, en die staan nooit in de continuous. En we are meeting at six voor een vastgelegde afspraak: de continuous kan ook naar de toekomst wijzen.",
            ],
        ),
        dict(
            aanpak="De ing-vorm heeft drie spellingregels: een stomme e valt weg, een korte beklemtoonde lettergreep verdubbelt zijn medeklinker, en ie wordt y.",
            waarom=[
                "Sit wordt sitting (verdubbeld), write wordt writing (de e valt weg), lie wordt lying (ie wordt y), begin wordt beginning (verdubbeld, want de klemtoon ligt achteraan). Bij visit gebeurt dat niet: de klemtoon ligt vooraan, dus visiting.",
            ],
        ),
        dict(
            aanpak="De present perfect gebruik je als het verleden tot nu doorloopt of nu nog telt. Dat is precies het stuk waar het Nederlands een tegenwoordige of een verleden tijd zet, en dus waar het misgaat.",
            waarom=[
                "Wij zeggen ik woon sinds 2020, het Engels zegt I have lived since 2020. Begonnen in het verleden en nog altijd zo: dat vraagt een present perfect.",
                "Het gevolg telt nu: de sleutels zijn nu weg. Daarom geen past simple maar een present perfect.",
                "For bij een duur (three years), since bij een beginpunt (Monday). Yet staat achteraan en in een vraag of ontkenning; already staat in het midden en in een bevestigende zin.",
            ],
        ),
        dict(
            aanpak="De regel is kort: staat er een afgesloten tijd bij (yesterday, in 2019, two hours ago, last year), dan past simple. Loopt het door tot nu of telt het nu nog, dan present perfect.",
            waarom=[
                "Yesterday, in 2019 en two hours ago zijn alle drie afgesloten, dus past simple. For years loopt door tot nu, dus present perfect.",
                "Last year is voorbij en afgesloten. Dan kan er geen present perfect staan, hoe recent het ook voelt. I have been to London zonder tijdsbepaling kan wel.",
                "When vraagt naar een precies moment in het verleden, en dat is per definitie afgesloten. Daarom altijd when did you arrive.",
            ],
        ),
        dict(
            aanpak="Zes zinnen, zes verschillende regels. Kijk telkens eerst welk woord de tijd draagt: does, is, have. Dat woord neemt de vervoeging voor zijn rekening, en de rest blijft kaal.",
            waarom=[
                "Does draagt al de derde persoon, dus het werkwoord erna blijft kaal: does she live. Dezelfde regel als bij he doesn't live here.",
                "Three books is meervoud, dus there are. There is hoort bij één ding of bij een ontelbaar woord.",
                "Know is een werkwoord van denken en voelen, en die staan nooit in de continuous. Zo ook like, want, believe, understand, need en see.",
                "Na have hoort het voltooid deelwoord, niet de verleden tijd: eaten, niet ate. Dat is de derde kolom van het rijtje.",
                "Zelfde reden als in oefening 14: know kan niet in een continuous, ook niet in de present perfect. Dus I have known her for years.",
                "Een vraag naar iets dat begon in het verleden en nog bezig is, gaat in de present perfect continuous: how long have you been learning English. Are you learning zou alleen over dit moment gaan.",
            ],
        ),
        dict(
            aanpak="Jezelf hardop horen vertellen is de snelste test: wie over vandaag praat, heeft vanzelf een present perfect en een continuous nodig.",
            waarom=[
                "Er is geen juist antwoord. Bijvoorbeeld: I have finished my homework (klaar, telt nu) en I am waiting for dinner (nu bezig).",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-past-simple-past-continuous-en-de-toekomst-met-will-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De drie vormen zijn de basis van alles wat verleden is: infinitief, past simple en past participle. De onregelmatige rijtjes moet je gewoon vanbuiten kennen; er is geen regel voor.",
            waarom=[
                "Let op welke er twee dezelfde vormen hebben (bought, bought en brought, brought) en welke er drie verschillende hebben (go, went, gone en drink, drank, drunk). De derde kolom gebruik je na have en na be, en nergens anders.",
            ],
        ),
        dict(
            aanpak="De regelmatige verleden tijd is ed, met drie spellingregels: y wordt ied, een korte beklemtoonde lettergreep verdubbelt, en een woord dat al op e eindigt krijgt alleen een d.",
            waarom=[
                "Study wordt studied (y na een medeklinker), stop wordt stopped (verdubbeld), like wordt liked (alleen een d), travel wordt travelled in het Brits Engels (dubbele l) en traveled in het Amerikaans.",
            ],
        ),
        dict(
            aanpak="De past continuous zegt dat iets bezig was; de past simple dat iets gebeurde. In één zin samen: het langere stuk in de continuous, de onderbreking in de simple.",
            waarom=[
                "Zie het patroon: while hoort bij de continuous, when bij de simple. I was reading when the phone rang: het lezen was bezig, het bellen gebeurde. En he arrived at eight staat alleen, dus gewoon past simple.",
            ],
        ),
        dict(
            aanpak="Tien zinnen over de verleden en de toekomende tijd. De rode draad: één woord draagt de tijd (did, will), en het werkwoord erna blijft kaal.",
            waarom=[
                "Didn't draagt al het verleden, dus het werkwoord blijft kaal: didn't come.",
                "Was is zelf al het werkwoord, dus er komt geen did bij: were you there. Did gebruik je alleen bij gewone werkwoorden.",
                "Know kan niet in een continuous, ook niet in het verleden. Dus I knew the answer.",
                "In spreektaal en in een informele tekst kort je will af tot 'll: I'll help you. De ontkenning is won't, en die kort je altijd af.",
                "Won't, met een apostrof tussen de o en de t. Het is de enige korte vorm van het Engels die er heel anders uitziet dan het woord zelf.",
                "Vier gebruiken op een rij: een beslissing op het moment zelf (I'll help you), een belofte (I won't tell), een voorspelling (I think it will rain) en een feit over later (the train will leave).",
                "Na will komt de kale infinitief, zonder to. Dat geldt voor alle hulpwerkwoorden: can, must, should, may.",
                "En zonder s, om dezelfde reden: will draagt alles, het werkwoord blijft kaal.",
                "Na when, before, after, as soon as en until gebruikt het Engels een tegenwoordige tijd, ook als het over later gaat. Dat is een echt verschil met het Nederlands.",
                "Dezelfde regel na if: if it rains, we will stay. De toekomst zit in de hoofdzin, nooit in de als-zin.",
            ],
        ),
        dict(
            aanpak="Over je weekend praten dwingt je vanzelf in alle drie de tijden, en dat maakt het de beste oefening voor dit hoofdstuk.",
            waarom=[
                "Er is geen juist antwoord. Bijvoorbeeld: I went to my grandmother's on Saturday. While we were eating, my cousin called. Next weekend I will stay at home.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-zinsdelen-soorten-zinnen-en-samengestelde-zinnen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek altijd eerst de persoonsvorm, dan het onderwerp (wie of wat doet het) en dan het lijdend voorwerp (wie of wat ondergaat het). In het Engels staat die volgorde bijna altijd vast.",
            waarom=[
                "Het onderwerp is de hele groep woorden, niet alleen het naamwoord: my little sister, the children. En let op were in de tweede zin: dat is een koppelwerkwoord, dus daar volgt geen lijdend voorwerp maar een naamwoordelijk deel.",
                "Het meewerkend voorwerp staat in het Engels vóór het lijdend voorwerp als er geen to bij staat. His friend krijgt het cadeau, dus dat is het meewerkend voorwerp.",
                "Met to keert de volgorde om: eerst het lijdend voorwerp, dan to plus het meewerkend voorwerp. Beide zinnen zijn juist, maar je kan ze niet mengen.",
            ],
        ),
        dict(
            aanpak="De Engelse woordvolgorde is vaster dan de Nederlandse: onderwerp, persoonsvorm, lijdend voorwerp, en dan de bepalingen in de orde hoe, waar, wanneer.",
            waarom=[
                "Very much hoort achteraan, nooit tussen like en this film. Het Engels laat niets tussen het werkwoord en zijn lijdend voorwerp komen.",
                "Onthoud de orde van de bepalingen: hoe (beautifully), waar (at the concert), wanneer (last night). Dat is precies omgekeerd aan het Nederlands, waar wanneer meestal eerst komt.",
                "Een tijdsbepaling mag ook vooraan staan, en dan komt er géén omkering: yesterday I went home, niet yesterday went I home. Dat laatste is de klassieke Nederlandse fout.",
            ],
        ),
        dict(
            aanpak="Vijf soorten zinnen, elk met hun eigen vorm. Je herkent ze aan het werkwoord vooraan (bevelend), aan do of een hulpwerkwoord vooraan (vragend), aan not (ontkennend) en aan what of how (uitroepend).",
            waarom=[
                "Let op doesn't want: de ontkenning zit in het hulpwerkwoord, niet in het werkwoord zelf. En een vraag met een gewoon werkwoord heeft altijd do, does of did nodig.",
                "Een bevel heeft geen onderwerp. En er zijn twee soorten uitroep: what a plus een naamwoord (what a beautiful garden) en how plus een bijvoeglijk naamwoord of bijwoord (how fast she runs).",
            ],
        ),
        dict(
            aanpak="Een vraag maken gaat in het Engels op twee manieren. Staat er al een hulpwerkwoord of een vorm van be, dan zet je dat vooraan. Staat er geen, dan haal je do, does of did erbij.",
            waarom=[
                "Vergelijk de vier. Plays heeft geen hulpwerkwoord, dus komt does erbij en wordt plays weer play. Can, have en are staan er al, dus die schuiven gewoon naar voren.",
                "Een aanhangvraag spiegelt de zin: is de zin bevestigend, dan is het staartje ontkennend, en omgekeerd. You're coming wordt dus aren't you. Hetzelfde met she didn't call, did she.",
            ],
        ),
        dict(
            aanpak="Vier klassieke valstrikken bij de overeenkomst. Zoek telkens het echte onderwerp, en weet dat een paar woorden in het Engels anders geteld worden dan bij ons.",
            waarom=[
                "News eindigt op een s maar is enkelvoud. Everybody is ook enkelvoud, hoeveel mensen het ook zijn. The police is net omgekeerd: dat is altijd meervoud. En in one of my friends is het echte onderwerp one, dus enkelvoud.",
            ],
        ),
        dict(
            aanpak="Voegwoorden zeggen welk verband er tussen twee zinnen ligt. Let op waar ze staan: because en although openen een bijzin, so en but staan tussen de twee zinnen in.",
            waarom=[
                "Vergelijk de eerste twee: because staat vóór de oorzaak, so vóór het gevolg. Dezelfde inhoud, omgekeerde volgorde. En but en although doen hetzelfde werk, maar but staat tussenin en although vooraan.",
                "Unless betekent tenzij. Let op dat er geen tweede ontkenning bij komt: unless you hurry, niet unless you don't hurry.",
                "If not, dus tenzij. Daarom zit de ontkenning al in het woord zelf.",
                "De praktische test: een nevenschikkende zin kan je in twee losse zinnen knippen (I called her. She answered.). Een bijzin kan dat niet: because it was raining staat alleen niet overeind.",
            ],
        ),
        dict(
            aanpak="Een zin is samengesteld zodra er twee persoonsvormen in staan. En de komma volgt één eenvoudige regel: hij staat achter de bijzin als die vooraan staat.",
            waarom=[
                "Was en went zijn allebei persoonsvorm, dus twee. Een infinitief of een ing-vorm telt niet mee.",
                "Until en till betekenen allebei tot. Let erop dat er na until een tegenwoordige tijd volgt, ook al gaat het over later: until you come back.",
                "Staat de bijzin vooraan, dan komt er een komma achter: When I arrived, she was asleep. Staat ze achteraan, dan niet: She was asleep when I arrived.",
            ],
        ),
        dict(
            aanpak="In een echte tekst zie je meteen welke voegwoorden er echt toe doen, en dat zijn er maar een handvol.",
            waarom=[
                "Er is geen juist antwoord. And, but en because zijn in bijna elke tekst de drie meest gebruikte.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-klank-klemtoon-intonatie-en-spelling-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het Engels schrijft veel letters die het niet uitspreekt. Ze zitten bijna altijd in dezelfde combinaties: kn, wr, lk, st en een h vooraan. Leer de combinatie, niet het losse woord.",
            waarom=[
                "Vier verschillende: de k van knife (zoals in knee en knock), de h van hour (zoals in honest), de s van island, de t van castle (zoals in listen en whistle).",
                "Walk, talk en half verliezen hun l. Wrong, write en wrap verliezen hun w. Know en knee hun k, listen en castle hun t.",
                "Het lidwoord volgt de klánk, niet de letter. Hour begint met een klinkerklank (aur), dus an. Daarom ook an honest man, maar a university, want dat begint met joe.",
            ],
        ),
        dict(
            aanpak="Het Engels heeft woordklemtoon, en die ligt niet altijd vooraan. Bij een verkeerde klemtoon word je soms niet verstaan, ook als elke klank klopt.",
            waarom=[
                "Bij woorden van twee lettergrepen ligt de klemtoon meestal vooraan bij een naamwoord (TA-ble, O-pen) en achteraan bij een werkwoord (a-BOUT is een voorzetsel, maar vergelijk de-CIDE, be-GIN).",
                "Dit patroon komt vaker voor: PRE-sent en pre-SENT, RE-cord en re-CORD, OB-ject en ob-JECT. Vooraan het naamwoord, achteraan het werkwoord. Een handige regel om te onthouden.",
            ],
        ),
        dict(
            aanpak="De uitgangen ed en s klinken op drie manieren, en dat hangt af van de klank ervóór. Je hoeft die regels niet uit het hoofd te kennen om ze te horen, maar ze helpen bij het luisteren.",
            waarom=[
                "Na een t of een d wordt ed een extra lettergreep (wanted, started). Na een stemloze klank klinkt het als een t (worked, watched). Na een stemhebbende klank als een d (played, called).",
                "Na een sisklank komt es erbij als extra lettergreep: box wordt bo-xes. Hetzelfde bij watches, wishes en churches.",
                "Na een stemhebbende klank klinkt de meervouds-s als een z: dogs, cars, pens. Na een stemloze als een s: cats, books, maps.",
            ],
        ),
        dict(
            aanpak="Homofonen zijn woorden die hetzelfde klinken maar anders geschreven worden. Ze zijn de grootste bron van spelfouten, ook bij moedertaalsprekers.",
            waarom=[
                "Their, there en they're klinken alle drie gelijk, net als to, too en two, en write en right. Ship en sheep klinken níét gelijk: het verschil zit in de korte i tegenover de lange ie, en dat is net een van de moeilijkste klanken voor ons.",
                "Too met dubbele o betekent ook of te veel. To is het voorzetsel, two het getal.",
                "Think, thing en three hebben een stemloze th (je blaast); this, that en the een stemhebbende (je laat je stem trillen). Nederlandstaligen maken er vaak een d of een s van, en dan wordt this plots dis.",
            ],
        ),
        dict(
            aanpak="De intonatie van een Engelse vraag hangt af van het soort vraag. Een ja-neevraag stijgt op het einde, een vraag met een vraagwoord daalt, net als een gewone mededeling.",
            waarom=[
                "Zie het patroon: are you coming en did you see that zijn ja-neevragen, dus stijgend. Where are you going heeft een vraagwoord en daalt, net als een mededeling. Wie elke vraag laat stijgen, klinkt onzeker.",
            ],
        ),
        dict(
            aanpak="De Engelse spellingregels zijn er maar een handvol: de stomme e valt weg voor ing, een korte beklemtoonde lettergreep verdubbelt, en een y na een medeklinker wordt i.",
            waarom=[
                "Stop wordt stopping (verdubbeld), make wordt making (de e valt weg), study wordt studied en carry wordt carries (y wordt i). Dezelfde drie regels dus als bij de werkwoorden.",
                "Baby wordt babies (y na een medeklinker), boy wordt boys (y na een klinker), box wordt boxes (sisklank), knife wordt knives (f wordt ves).",
                "De woorden die het vaakst fout gaan: because, friend, beautiful, necessary, receive, definitely en address. Schrijf de jouwe op een lijstje en kijk dat na voor je je tekst afgeeft.",
                "Dagen, maanden, talen, landen en nationaliteiten krijgen in het Engels een hoofdletter: Monday, July, English, Belgium, Belgian. De seizoenen niet: summer, winter. Dat is een echt verschil met het Nederlands, waar dagen en maanden klein blijven.",
            ],
        ),
        dict(
            aanpak="Vijf zinnen met vijf gewone spelfouten. Lees je eigen tekst op het einde nog eens apart na op spelling: dat is sneller dan het tijdens het schrijven proberen.",
            waarom=[
                "Twee fouten in één: address met dubbele d en dubbele s, en an voor een klinkerklank.",
                "Een y na een medeklinker wordt ied: studied. Vergelijk played, waar de y na een klinker staat.",
                "Na een sisklank komt es: boxes. Zie ook oefening 14.",
                "Monday met een hoofdletter, zoals alle weekdagen en maanden in het Engels.",
                "Don't met een apostrof, want het is de samentrekking van do not. Een apostrof vervangt altijd de weggelaten letters.",
            ],
        ),
        dict(
            aanpak="Een liedje is de snelste manier om te merken hoe ver de Engelse spelling van de uitspraak afligt, want je kent de melodie al.",
            waarom=[
                "Er is geen juist antwoord. Het gaat erom dat je merkt hoe ver het schriftbeeld van de klank kan liggen, en dat je daarna gerichter luistert.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-spreken-gesprekken-en-hoe-je-beoordeeld-wordt-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes vaste situaties die in elk spreekexamen terugkomen. Leer er één goede zin per situatie van vanbuiten, dan hoef je ter plekke niets te bedenken.",
            waarom=[
                "Excuse me is de vaste opener om een onbekende aan te spreken. Sorry gebruik je als je al iets gedaan hebt.",
                "Would you like to … is de uitnodiging. Do you want to … klinkt directer en past alleen tussen vrienden.",
                "Zet er altijd bij waarvoor je bedankt. Thank you for your help is warmer dan een kaal thanks.",
                "Twee delen: sorry plus de reden. Een verontschuldiging zonder reden klinkt in het Engels afgeraffeld.",
                "Het Engels verwacht hier een geruststelling. Een stilte of een knikje leest als verwijt. That's all right, no problem of don't worry about it horen erbij.",
                "Een gesprek afsluiten hoort ook bij de beoordeling. It was nice talking to you plus iets over de volgende keer is de standaardafsluiter.",
            ],
        ),
        dict(
            aanpak="Beleefdheid zit in het Engels in de vórm van je zin, niet in een extra woord. Maak van een bevel een vraag met could you, en van een eis een wens met I would like.",
            waarom=[
                "Een kaal bevel tegenover een onbekende is in het Engels onbeleefd, ook met please erachter. Could you ervoor lost het op.",
                "Deze is al goed: could you plus please. Niet elke zin in zo'n reeks is fout, en dat is net de test.",
                "I want klinkt als eisen. I would like (of I'd like) is de normale vorm in elke formele situatie.",
                "Dit is geen taalfout maar een houding. In een gesprek over een probleem verwacht het Engels eerst meeleven, dan een aanbod om te helpen.",
            ],
        ),
        dict(
            aanpak="Op een spreekexamen word je ook beoordeeld op interactie: laat je de ander aan het woord en help je het gesprek vooruit? Open vragen doen dat, ja-neevragen niet.",
            waarom=[
                "Let op dat het open vragen zijn: what, how long, why. Een vraag waarop de ander alleen yes of no kan antwoorden, legt het gesprek net stil.",
                "Could you repeat that, please is beter dan what, dat kortaf klinkt. Sorry, I didn't catch that kan ook.",
                "More slowly, met de vergrotende trap van het bijwoord. Speak slower hoor je ook, maar more slowly is correcter.",
            ],
        ),
        dict(
            aanpak="De beoordelingscriteria verschillen tussen een spreek- en een schrijfopdracht. Vraag je telkens af of de luisteraar het hoort of de lezer het ziet.",
            waarom=[
                "Taakvoltooiing geldt bij allebei. Lichaamstaal, uitspraak en intonatie kan je alleen horen of zien, dus die gelden alleen mondeling. Spelling en leestekens kan je alleen zien, dus alleen schriftelijk.",
                "Taakvoltooiing is het zwaarste criterium: een vlot gesprek dat de opdracht niet uitvoert, haalt daar niets.",
                "Register is je toon tegenover wie voor je zit. Op een gesprek met een examinator is neutraal of licht informeel goed; te familiair of te stijf valt allebei op.",
                "Een valse start of een herformulering is normaal, ook bij moedertaalsprekers. Wat telt is of je boodschap overkomt, niet of je zonder haperen praat.",
                "Een accent is geen fout, en het wordt ook niet gemeten. Wat gemeten wordt, is of je verstaanbaar bent.",
            ],
        ),
        dict(
            aanpak="Strategieën zijn wat je doet als het misloopt. Precies daarvoor krijg je punten: niet omdat alles vlot gaat, maar omdat je het gesprek aan de gang houdt.",
            waarom=[
                "Omschrijven is een vaardigheid waarvoor je punten krijgt. The thing you use when … of someone who … werkt bij bijna elk woord.",
                "Luider spreken helpt niet, want de ander hoorde je wel, hij begreep je niet. Zeg het in andere woorden, of korter.",
                "Kernwoorden, geen volledige zinnen. Wie zijn tekst uitschrijft, leest voor, en dat hoort een examinator meteen.",
                "Waarom, voor wie, met wie, wat precies, en langs welk kanaal. Die vijf vragen zijn het communicatiemodel, en ze bepalen samen je toon en je opbouw.",
            ],
        ),
        dict(
            aanpak="Weten hoe het examen in elkaar zit, scheelt stress. Kijk de cijfers na op de website van de Examencommissie voor je inschrijft, want die kunnen veranderen.",
            waarom=[
                "Reken met het geheel: het digitale examen duurt 150 minuten, en het gesprek is een aparte afspraak van ongeveer tien minuten, met een kwartier voorbereidingstijd en twee opdrachten.",
                "Drie dagen voor je digitale examen is de uiterste datum. Wacht daar niet mee tot het laatste moment, want je hebt opnames en bestanden nodig.",
                "Lezen en luisteren samen wegen zestig procent, dus meer dan de helft van je punten. Oefen die twee dus zeker even hard als schrijven en spreken.",
                "Er is geen giscorrectie: een fout antwoord kost je niets meer dan een leeg antwoord. Laat dus nooit een vraag open staan.",
            ],
        ),
        dict(
            aanpak="Jezelf opnemen is ongemakkelijk en daarom werkt het: je hoort in één keer wat je publiek hoort.",
            waarom=[
                "Er is geen juist antwoord. Het kernwoordenplan is het doel: wie zijn tekst uitschrijft, leest voor, en dat hoor je meteen.",
            ],
        ),
    ]
)
