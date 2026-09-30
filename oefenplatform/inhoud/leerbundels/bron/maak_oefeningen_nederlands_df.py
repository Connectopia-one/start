# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij Nederlands 🚀 Boost dubbele finaliteit.

Net als bij de leerbundels nemen we negen bundels over uit de doorstroomversie
en schrijven we er drie nieuw; zie `maak_nederlands_df.py` voor waarom. De
ingrepen hangen aan een stuk tekst van de oefening die ze raken, en elke
ingreep moet precies één oefening raken.

De sleutels dragen het voorvoegsel "oefenbundel-" en eindigen op
"-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel
import maak_oefeningen_nederlands_boost as doorstroom
import maak_nederlands_df as leerbundels

VAK = "Nederlands"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"

W, WW, WL = "120px", "185px", "250px"

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"
WEG = leerbundels.WEG
HOE = doorstroom.HOE
echte_leven = doorstroom.echte_leven

PATCHES = [
    # Parodie staat niet op de DF-fiche; dysfemisme wel, naast het eufemisme
    # dat al in dezelfde rij staat.
    (
        "betekenis-beeldspraak-en-gevoelswaarde",
        "Een liedje dat een bekende hit grappig nadoet.",
        "vervang",
        [
            ("rij", [("Hij is niet meer onder ons.", "eufemisme"),
                     ("Ze noemen dat oude huis een krot.", "dysfemisme")],
             "Welke stijlfiguur of humorvorm?", WL),
        ],
    ),
]


def tekst_van(oef) -> str:
    return " ".join(str(d) for d in oef)


def pas_toe(bundels: dict):
    for kort, haak, wat, nieuw in PATCHES:
        sleutel = "oefenbundel-" + kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        reeksen = bundels[sleutel]["reeksen"]
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


def overgenomen() -> dict:
    uit = {}
    weg = set()
    for sleutel, b in doorstroom.OEFENBUNDELS.items():
        if not sleutel.endswith(OUD):
            raise SystemExit(f"Doorstroomsleutel zonder categorie: {sleutel}")
        kort = sleutel[len("oefenbundel-") : -len(OUD)]
        if kort in WEG:
            weg.add(kort)
            continue
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        uit["oefenbundel-" + kort + NIEUW] = nieuw
    if weg != set(WEG):
        raise SystemExit(f"Deze bundels staan niet (meer) bij doorstroom: {set(WEG) - weg}")
    pas_toe(uit)
    return uit


OEFENBUNDELS = overgenomen()

# ============================================================
OEFENBUNDELS["oefenbundel-feit-en-mening-stelling-argument-en-conclusie" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Feit en mening, stelling, argument en conclusie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Feit of mening?",
             opdracht="Een feit kan je nagaan, een mening is wat iemand ervan vindt. Duid aan wat het is.",
             oefeningen=[
                 ("kies", "De gemeente telde vorig jaar 412 nieuwe inwoners.", ["een feit", "een mening"], 0),
                 ("kies", "De gemeente doet veel te weinig voor jongeren.", ["een feit", "een mening"], 1),
                 ("kies", "Een dagpas voor de bus kost 7,50 euro.", ["een feit", "een mening"], 0),
                 ("kies", "De bus is onbetaalbaar geworden voor scholieren.", ["een feit", "een mening"], 1),
                 ("kies", "In dit gebouw zijn 96 zonnepanelen geplaatst.", ["een feit", "een mening"], 0),
                 ("kies", "Zonnepanelen zijn de slimste investering voor een gezin.",
                  ["een feit", "een mening"], 1),
             ]),
        dict(kop="Stelling, standpunt, argument of conclusie?",
             opdracht="Schrijf bij elke zin welk van de vier het is.",
             oefeningen=[
                 ("rij", [("De schooldag moet later beginnen.", "de stelling"),
                          ("Ik ben daarvoor.", "het standpunt"),
                          ("Tieners slapen 's ochtends structureel te kort.", "een argument"),
                          ("Daarom moet de school om negen uur starten.", "de conclusie")],
                  "Wat is het?", WL),
                 ("rij", [("Het zwembad moet open blijven.", "de stelling"),
                          ("Het is het enige zwembad in de gemeente.", "een argument")],
                  "Wat is het?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="",
             oefeningen=[
                 ("waar", "De stelling en het standpunt zijn hetzelfde.", False),
                 ("waar", "De conclusie staat meestal in het slot van de tekst.", True),
                 ("waar", "Een goede conclusie voegt nog een nieuw argument toe.", False),
                 ("waar", "Een schrijver die een tegenargument noemt, is van mening veranderd.", False),
                 ("waar", "Eén argument dat echt over de stelling gaat, weegt zwaarder dan vijf die ernaast "
                          "liggen.", True),
             ]),
        dict(kop="Welk signaalwoord?",
             opdracht="Vul in met want, omdat, daarom of maar.",
             oefeningen=[
                 ("tabel", ["zin", "signaalwoord"],
                  [["Het park ligt vol afval, ___ de gemeente haalde er vorig jaar twaalf ton weg.", None],
                   ["___ de bus vaak te laat komt, vertrekken veel leerlingen te vroeg.", None],
                   ["De cijfers zijn duidelijk. ___ moet er iets veranderen.", None]],
                  "Rij 1: want (reden achteraf). Rij 2: Omdat (reden vooraan). Rij 3: Daarom (gevolg).",
                  "200px"),
             ]),
        dict(kop="Wat loopt er mis?",
             opdracht="",
             oefeningen=[
                 ("open", "'Ik vind dat het skatepark er moet komen, want ik vind dat het er moet komen.' "
                          "Leg in twee zinnen uit wat er mis is.",
                  "Na 'want' hoort een réden te staan, iets nieuws. Hier wordt het standpunt enkel "
                  "herhaald, dus de lezer weet nog altijd niet waarom.", 5),
                 ("open", "Iemand schrijft over afval in het park: 'Het is daar echt vreselijk vuil, dat "
                          "ziet toch iedereen.' Maak daar een bruikbaar argument van.",
                  "Zoek een cijfer dat je kan nagaan, bijvoorbeeld hoeveel zwerfvuil de gemeente er vorig "
                  "jaar weghaalde of hoeveel meldingen er binnenkwamen. Een oordeel herhalen overtuigt "
                  "niemand, een getal wel.", 6),
             ]),
        dict(kop="Zelf opbouwen",
             opdracht="",
             oefeningen=[
                 ("open", "Neem de stelling: 'De gemeente moet gratis bussen inleggen voor jongeren.' "
                          "Schrijf je standpunt, twee argumenten en een conclusie.",
                  "Bijvoorbeeld. Standpunt: ik ben daarvoor. Argument 1: een dagpas kost 7,50 euro, en wie "
                  "vijf dagen per week naar school gaat, betaalt daarmee een fors deel van zijn "
                  "vakantiejob. Argument 2: minder jongeren met de brommer betekent minder ongevallen op "
                  "de gewestweg. Conclusie: omdat de kost hoog ligt en de winst breder is dan het vervoer "
                  "alleen, moet de gemeente dit invoeren.", 9),
             ]),
        dict(kop="Bronnen die elkaar tegenspreken",
             opdracht="",
             oefeningen=[
                 ("open", "Twee bronnen geven een ander cijfer over hetzelfde onderwerp. Noem drie dingen "
                          "die je nagaat voor je er een kiest.",
                  "Wie is de zender en is die deskundig? Wanneer is het geschreven, is de informatie nog "
                  "actueel? Welke bronnen gebruikt de tekst zelf, en met welke bedoeling is hij "
                  "geschreven?", 6),
             ]),
        echte_leven(
            "Ga deze week één keer in gesprek met iemand die er anders over denkt dan jij. Schrijf vooraf "
            "je stelling, je standpunt en twee argumenten op. Noteer achteraf welk argument van de ander "
            "je niet zag aankomen.",
            "Er is geen juist antwoord. Let erop of je oplossingsgericht bleef: zoek je samen iets waar "
            "jullie allebei mee verder kunnen, of zoek je enkel gelijk? En kon je erkennen dat een "
            "argument van de ander klopte?", 8),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-fictie-personages-verhaallijn-tijd-en-ruimte" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Fictie, personages, verhaallijn, tijd en ruimte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Fictie of non-fictie?",
             opdracht="Duid aan wat het is.",
             oefeningen=[
                 ("kies", "Een biografie van een wielrenner.", ["fictie", "non-fictie"], 1),
                 ("kies", "Een fantasyroman over een school voor tovenaars.", ["fictie", "non-fictie"], 0),
                 ("kies", "Een reisverslag van een tocht die iemand echt maakte.", ["fictie", "non-fictie"], 1),
                 ("kies", "Een roman over een echte staking, met verzonnen personages.",
                  ["fictie", "non-fictie"], 0),
                 ("kies", "Een boek over de geschiedenis van je stad.", ["fictie", "non-fictie"], 1),
             ]),
        dict(kop="Welk begrip?",
             opdracht="Schrijf het juiste begrip erbij: personage, verhaallijn, tijd of ruimte.",
             oefeningen=[
                 ("rij", [("Het verhaal speelt in een dorp aan zee.", "de ruimte"),
                          ("Het verhaal beslaat één nacht.", "de tijd"),
                          ("De zus van het hoofdpersonage keert halverwege terug.", "een personage"),
                          ("Eerst de brand, dan het proces, dan de verhuizing.", "de verhaallijn")],
                  "Welk begrip?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="",
             oefeningen=[
                 ("waar", "Een verhaal kan meer dan één verhaallijn hebben.", True),
                 ("waar", "Een verhaal moet zijn gebeurtenissen in chronologische volgorde vertellen.", False),
                 ("waar", "Een strip kan een literaire tekst zijn.", True),
                 ("waar", "Een bijsluiter bij een geneesmiddel is een literaire tekst.", False),
                 ("waar", "Een boek dat op ware feiten gebaseerd is, is daarom non-fictie.", False),
                 ("waar", "Voor het examen lees of beluister je twee boeken van de boekenlijst.", True),
             ]),
        dict(kop="Wat doet de ruimte met het verhaal?",
             opdracht="",
             oefeningen=[
                 ("open", "Een verhaal speelt volledig in één huis tijdens één storm. Wat doet dat met de "
                          "sfeer, en waarom?",
                  "De ruimte is klein en de tijd is kort, dus niemand kan weg en alles moet zich daar en "
                  "dan oplossen. Dat maakt zo'n verhaal benauwd en gespannen.", 5),
                 ("open", "Een verhaal speelt in een dorp waar iedereen elkaar kent. Noem één ding dat "
                          "daardoor moeilijker wordt voor de personages.",
                  "Een geheim bewaren. In een dorp waar iedereen elkaar kent, valt afwezigheid op en "
                  "wordt er gepraat.", 4),
             ]),
        dict(kop="Feit of interpretatie?",
             opdracht="Duid aan of je de uitspraak kan nakijken in het boek, of dat ze uit de tekst afgeleid is.",
             oefeningen=[
                 ("kies", "Het boek telt achtentwintig hoofdstukken.", ["feit", "interpretatie"], 0),
                 ("kies", "De schrijver wil laten zien dat zwijgen ook schade doet.",
                  ["feit", "interpretatie"], 1),
                 ("kies", "Het hoofdpersonage groeit doorheen het boek.", ["feit", "interpretatie"], 1),
                 ("kies", "Het verhaal speelt in 1954.", ["feit", "interpretatie"], 0),
             ]),
        dict(kop="Je eigen beleving",
             opdracht="",
             oefeningen=[
                 ("open", "Welke van deze twee zinnen is bruikbaar in een gesprek over je boek, en waarom? "
                          "(a) 'Het was een heel goed boek, ik raad het aan.' (b) 'Het slot liet me "
                          "verward achter, omdat ik niet wist wie ik gelijk moest geven.'",
                  "Zin b. Die zegt wát je voelde en waardóór. Zin a is een oordeel zonder uitleg, en "
                  "daar kan je gesprekspartner niets mee.", 5),
                 ("open", "Schrijf drie zinnen over een boek dat je ooit las: wat raakte je, waardoor "
                          "precies, en wat zou jij anders gedaan hebben dan het hoofdpersonage?",
                  "Er is geen juist antwoord. Kijk na of je bij elk van de drie een stuk uit het boek kan "
                  "aanwijzen; zonder dat blijft het bij een gevoel.", 7),
             ]),
        echte_leven(
            "Vertel deze week aan iemand over een boek, een film of een serie, in drie minuten, zonder de "
            "verhaallijn na te vertellen. Praat enkel over de personages, de ruimte en wat het met jou "
            "deed. Noteer achteraf wat die persoon vroeg.",
            "Er is geen juist antwoord. Let erop of de ander na drie minuten wilde weten hoe het afliep. "
            "Als dat zo is, heb je precies gedaan wat een gesprek over een boek moet doen.", 8),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-lichaamstaal-beleefdheid-en-een-tekst-die-werkt" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Lichaamstaal, beleefdheid en een tekst die werkt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke vorm van non-verbale communicatie?",
             opdracht="Schrijf het juiste woord erbij: mimiek, intonatie, articulatie, tempo of volume.",
             oefeningen=[
                 ("rij", [("Hij trekt zijn wenkbrauwen op terwijl hij het zegt.", "mimiek"),
                          ("Haar stem gaat aan het eind van de zin omhoog.", "intonatie"),
                          ("Hij spreekt zo binnensmonds dat je hem niet verstaat.", "articulatie"),
                          ("Ze ratelt door haar tekst heen van de zenuwen.", "tempo")],
                  "Welke vorm?", WL),
             ]),
        dict(kop="Gepast of ongepast?",
             opdracht="Duid aan.",
             oefeningen=[
                 ("kies", "Drie smileys in een sollicitatiemail.", ["gepast", "ongepast"], 1),
                 ("kies", "Een smiley in een WhatsAppbericht aan een vriendin.", ["gepast", "ongepast"], 0),
                 ("kies", "Een formele mail afsluiten met 'groetjes'.", ["gepast", "ongepast"], 1),
                 ("kies", "Een onbekende volwassene aanspreken met 'u'.", ["gepast", "ongepast"], 0),
                 ("kies", "Een hele zin in hoofdletters typen op een forum.", ["gepast", "ongepast"], 1),
             ]),
        dict(kop="Welk criterium?",
             opdracht="Schrijf bij elke opmerking het criterium waar ze over gaat.",
             oefeningen=[
                 ("rij", [("Je tekst bereikt zijn doel niet, de lezer weet nog altijd niet wat je wil.",
                           "taakvoltooiing"),
                          ("Elke zin begint bij jou met 'ik'.", "grammatica en zinsbouw"),
                          ("Er zit geen inleiding of slot in je tekst.", "tekststructuur en samenhang"),
                          ("Je schrijft 'hey' aan een directeur.", "register en beleefdheid")],
                  "Welk criterium?", WL),
                 ("rij", [("Je gebruikt enkel de allergewoonste woorden.", "woordenschat"),
                          ("Je tekst staat in één blok zonder alinea's.", "tekstopbouw en lay-out")],
                  "Welk criterium?", WL),
             ]),
        dict(kop="Schrijven of spreken?",
             opdracht="Duid aan bij welke soort opdracht dit criterium enkel geldt.",
             oefeningen=[
                 ("kies", "spelling en leestekengebruik", ["schrijven", "spreken"], 0),
                 ("kies", "uitspraak en intonatie", ["schrijven", "spreken"], 1),
                 ("kies", "tekstopbouw en lay-out", ["schrijven", "spreken"], 0),
                 ("kies", "vlotheid", ["schrijven", "spreken"], 1),
                 ("kies", "lichaamstaal en oogcontact", ["schrijven", "spreken"], 1),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="",
             oefeningen=[
                 ("waar", "Emoji's horen bij non-verbale communicatie.", True),
                 ("waar", "Aan iemands lichaamstaal kan je zien of hij liegt.", False),
                 ("waar", "Notities mogen in telegramstijl, met afkortingen en symbolen.", True),
                 ("waar", "Elke tekst met een gepaste lay-out heeft tussentitels.", False),
                 ("waar", "Per alinea hoort er één deelonderwerp in.", True),
                 ("waar", "Op het examen Nederlands mag je een online woordenboek gebruiken.", True),
                 ("waar", "Kleding en uiterlijk horen niet bij communicatie.", False),
             ]),
        dict(kop="Strategie kiezen",
             opdracht="",
             oefeningen=[
                 ("open", "Je komt in een leestekst een woord tegen dat je niet kent. Noem drie dingen die "
                          "je probeert voor je het opzoekt.",
                  "De betekenis afleiden uit de context. Kijken hoe het woord gevormd is: is het een "
                  "afleiding of een samenstelling? Kijken of je kennis van een andere taal helpt. Pas "
                  "daarna zoek je op, en enkel als je het woord echt nodig hebt.", 6),
                 ("open", "Waarom maak je een spreekplan met kernwoorden en niet met uitgeschreven zinnen?",
                  "Met kernwoorden hou je je lijn vast en blijf je vrij in je formulering. Een "
                  "uitgeschreven tekst lees je af, en dan verlies je de connectie met je luisteraar.", 5),
             ]),
        dict(kop="Notities nemen",
             opdracht="",
             oefeningen=[
                 ("open", "Welke eis geldt er voor je notities, en welke eis níét?",
                  "Wel: ze sluiten aan bij de inhoud en zijn achteraf nog bruikbaar, bijvoorbeeld om een "
                  "samenvatting mee te maken. Niet: dat ze in volledige, nette zinnen staan. Afkortingen, "
                  "symbolen, telegramstijl, een schema, een tabel of een mindmap mogen allemaal.", 6),
             ]),
        echte_leven(
            "Neem deze week één keer een gesprek van jezelf op, bijvoorbeeld terwijl je iets uitlegt aan "
            "iemand. Luister het daarna terug en let op drie dingen: je tempo, je articulatie en hoe vaak "
            "je 'euh' zegt. Noteer wat je wil veranderen.",
            "Er is geen juist antwoord. De meeste mensen schrikken vooral van hun tempo. Wie zichzelf één "
            "keer heeft teruggehoord, spreekt daarna bijna altijd trager en duidelijker.", 8),
    ],
)
