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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-zender-ruis-en-de-zeven-tekstsoorten-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elke tekst af wat de schrijver vooral wil: iets laten weten, iets laten "
                    "doen, overtuigen, vertellen, of iets moois maken. Dat hoofddoel bepaalt de tekstsoort.",
             waarom=[
                 "Een reisverslag vertelt wat er gebeurd is, dus narratief. Zou het vooral uitleggen hoe "
                 "Peru in elkaar zit, dan was het informatief.",
                 None,
             ]),
        dict(aanpak="Allebei willen ze je overtuigen, maar op een andere manier: persuasief werkt op gevoel "
                    "en beeld, argumentatief op redenering en bewijs.",
             waarom=[
                 None,
                 "Cijfers van een officiële bron maken het argumentatief. Het is de bewijsvoering die het "
                 "onderscheid maakt, niet het onderwerp.",
                 None, None,
             ]),
        dict(aanpak="Loop de vijf plaatsen van het schema af: wie, aan wie, wat, waarlangs, en waarom.",
             waarom=[None]),
        dict(aanpak="Ruis is alles wat de boodschap stoort. Zit ze in de formulering, dan bij de zender; "
                    "in de verbinding, dan bij het kanaal; in de aandacht of de voorkennis, dan bij de "
                    "ontvanger.",
             waarom=[
                 None,
                 "Dit is de nuttigste van heel het hoofdstuk: wie zendt, is verantwoordelijk voor de "
                 "duidelijkheid. De fout bij de ander leggen lost niets op.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het verschil tussen de bedoeling van de schrijver en de vorm "
                    "van de tekst.",
             waarom=[
                 "De meeste teksten hebben meerdere bedoelingen tegelijk. Voor de tekstsoort kijk je naar "
                 "de hóófdbedoeling.",
                 None, None,
                 "Een handleiding zegt wat jij moet doen, dus is ze prescriptief. Narratief zou betekenen "
                 "dat ze een verhaal vertelt.",
             ]),
        dict(aanpak="Bij zelf schrijven is er geen modelantwoord. Kijk na of je bedoeling door heel de "
                    "tekst klopt: feiten zonder oordeel, of juist een duidelijk standpunt.",
             waarom=[None, None]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt. Het papierwerk vooraf is maar "
                    "de helft.",
             waarom=[
                 "Waar de ander doorvraagt, zat de ruis. Dat is de beste oefening in duidelijk formuleren "
                 "die er is.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-hoofdgedachte-alinea-en-structuuraanduiders-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Een signaalwoord kondigt het verband aan dat volgt. Vervang het in gedachten door "
                    "want, maar, en, of dus, en je weet welk verband het is.",
             waarom=[None, None]),
        dict(aanpak="Zoek eerst welk verband er tussen de twee delen zit, en kies dan een woord dat precies "
                    "dat verband legt. Meerdere woorden kunnen juist zijn.",
             waarom=[
                 None, None,
                 "Tenzij is het woord voor een uitzonderingsvoorwaarde: het gaat door, behalve als het "
                 "regent.",
                 None,
             ]),
        dict(aanpak="De hoofdgedachte is de zin waar de rest van de alinea bij hoort. Cijfers, namen en "
                    "voorbeelden zijn de uitwerking, niet de kern.",
             waarom=[
                 "Het aantal deelnemers is een detail dat het onderzoek staaft. De kern is wat eruit komt.",
                 None, None,
             ]),
        dict(aanpak="Drie delen met elk hun taak. Elke alinea in het midden draagt één hoofdgedachte.",
             waarom=[
                 None,
                 "Hou dat onderscheid vast: signaalwoorden werken tussen zinnen, structuuraanduiders over "
                 "de hele tekst.",
             ]),
        dict(aanpak="Let bij elke uitspraak op het woord altijd of nooit. Dat is bij alinea's bijna nooit "
                    "waar.",
             waarom=[
                 None,
                 "Een korte alinea kan net een sterk effect hebben, bijvoorbeeld om iets te benadrukken.",
                 "Ze staat vaak vooraan, maar even goed achteraan als besluit, of verspreid over de alinea.",
                 None,
             ]),
        dict(aanpak="Een samenvatting geeft de hoofdlijn in je eigen woorden. Alles wat enkel illustreert, "
                    "laat je weg.",
             waarom=[
                 "Je eigen mening hoort er niet in. Dat is het verschil tussen samenvatten en bespreken.",
                 None,
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Dat de ander moet vragen, is de beste controle op je structuur die er bestaat: daar "
                 "ontbrak een verband of een hoofdgedachte.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-bronnen-wegen-objectief-gekleurd-of-nep-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Zoek de woorden die een oordeel meedragen. Staan er enkel cijfers, namen en data, dan "
                    "is de zin objectief.",
             waarom=[
                 None,
                 "Duwde er vlotjes door en omstreden zijn de gekleurde woorden. Het feit blijft hetzelfde, "
                 "enkel de toon verandert.",
                 "Een golf en overspoelde maken van een aantal een ramp. Een getal zou hier veel meer "
                 "zeggen.",
                 None,
             ]),
        dict(aanpak="Streep eerst de gekleurde woorden door en schrijf dan op wat er feitelijk gebeurd is. "
                    "Een getal in de plaats van een gevoelswoord is bijna altijd een verbetering.",
             waarom=[None, None]),
        dict(aanpak="Betrouwbaarheid lees je af aan controleerbaarheid: wie schreef het, wanneer, en waarop "
                    "steunt het.",
             waarom=[
                 None,
                 "Geen auteur is een reden om verder te kijken, geen bewijs van onbetrouwbaarheid. Dat "
                 "onderscheid is de kern van bronnen wegen.",
             ]),
        dict(aanpak="Wie een onderzoek betaalt, heeft er belang bij. Dat maakt het niet waardeloos, wel iets "
                    "om bij te vermelden en strenger te lezen.",
             waarom=[
                 None,
                 "Die drie vragen, bron, datum en tweede bron, kosten je een halve minuut en halen het "
                 "meeste eruit.",
             ]),
        dict(aanpak="Een feit kan je nakijken, een mening niet, en een aanname is iets wat de schrijver "
                    "zomaar veronderstelt.",
             waarom=[
                 "Let op de aanname: iedereen wil toch is een zin die je zonder bewijs meekrijgt. Juist "
                 "zulke zinnen sturen een tekst.",
                 "Bronnen vermelden kan ook voor de schijn. Kijk na of de bron bestaat en of ze zegt wat er "
                 "beweerd wordt.",
                 None,
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Spreek over de bron, niet over de persoon die het doorstuurde. Anders wordt het een ruzie "
                 "in plaats van een gesprek.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-standaardtaal-tussentaal-en-register-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Vier variëteiten op een rij, van verzorgd naar los: standaardtaal, tussentaal, "
                    "dialect en jongerentaal. Kijk naar de woorden én naar de klanken die opgeschreven zijn.",
             waarom=[
                 "Tussentaal herken je aan kleine dingen: da in plaats van dat, en een he erachter. Het is "
                 "geen dialect, maar ook geen standaardtaal.",
             ]),
        dict(aanpak="Het register volgt uit de situatie, niet uit het onderwerp: wie is de ander, en hoe "
                    "goed ken je hem.",
             waarom=[None, None, None, None]),
        dict(aanpak="Vervang de gewestelijke vormen door standaardvormen en maak de zin af. Let op gij en "
                    "kunde, want die vallen het eerst op.",
             waarom=[None, None, None]),
        dict(aanpak="Een register is een keuze, geen kwestie van goed of fout. De vraag is telkens of het "
                    "past bij de situatie.",
             waarom=[
                 "Dit is het belangrijkste inzicht van het hoofdstuk: tussentaal is niet fout, ze is soms "
                 "ongepast. Dat is iets anders.",
                 None, None,
                 "In een gesprek met vrienden klinkt strakke standaardtaal afstandelijk. Passen bij de "
                 "situatie is het doel, niet zo verzorgd mogelijk.",
             ]),
        dict(aanpak="Een verzorgde mail heeft een aanspreking, een duidelijke vraag, volledige zinnen en "
                    "een afsluiting. Zeg in de eerste zin waarover het gaat.",
             waarom=[None]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Let op wat er naast de woorden verandert: tempo, toon en hoeveel je uitlegt. Dat hoort "
                 "allemaal bij het register.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-de-woordsoorten-op-een-rij-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elk woord af wat het doet in de zin: iets benoemen, iets beschrijven, "
                    "iets vervangen, of twee delen verbinden.",
             waarom=[
                 "Vergelijk luid en luide: hetzelfde woord, een andere soort, naargelang het iets zegt over "
                 "het werkwoord of over het naamwoord.",
                 None,
             ]),
        dict(aanpak="Eén vraag beslist: zegt het woord iets over een zelfstandig naamwoord, dan is het een "
                    "bijvoeglijk naamwoord; zegt het iets over het werkwoord, dan een bijwoord.",
             waarom=[None, None, None, None]),
        dict(aanpak="Zeven soorten voornaamwoorden. Let vooral op die, want dat woord kan aanwijzend én "
                    "betrekkelijk zijn.",
             waarom=[
                 "In die fiets daar wijst die aan, in de fiets die stuk is verwijst die terug naar fiets. "
                 "Staat er een hele bijzin achter, dan is het betrekkelijk.",
                 None,
             ]),
        dict(aanpak="Lidwoorden zijn er maar drie: de, het en een. Een telwoord zegt hoeveel of de "
                    "hoeveelste.",
             waarom=[
                 None,
                 "Veel, weinig en enkele voelen als bijvoeglijke naamwoorden, maar ze tellen, dus zijn het "
                 "onbepaalde telwoorden.",
             ]),
        dict(aanpak="Ga woord voor woord door de zin en benoem elk woord apart. Sla geen lidwoorden of "
                    "voorzetsels over.",
             waarom=[
                 "Let op haar: hier hoort het bij bed, dus is het bezittelijk. In ik zag haar is hetzelfde "
                 "woord persoonlijk.",
                 "De soort hangt af van wat het woord in díé zin doet. Daarom kan hetzelfde woord van soort "
                 "wisselen.",
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Uitleggen aan iemand anders is de scherpste toets: pas dan merk je of je de regel echt "
                 "kent of enkel de voorbeelden.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-werkwoorden-tijden-en-woordvorming-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Twee vragen per zin: is de handeling af (voltooid) of niet, en ligt ze in het heden, "
                    "het verleden of de toekomst. De naam volgt uit die twee.",
             waarom=[
                 "Een hulpwerkwoord hebben of zijn maakt de tijd voltooid. Zonder dat is ze onvoltooid.",
                 None,
             ]),
        dict(aanpak="Zoek eerst de stam en kijk dan naar het onderwerp. Is het een deelwoord, gebruik dan "
                    "het ezelsbruggetje met een ander werkwoord dat je wel hoort.",
             waarom=[
                 "Hij of zij krijgt stam plus t: wordt. Dat de stam al op d eindigt, verandert daar niets "
                 "aan.",
                 "Staat jij ná de persoonsvorm, dan valt de t weg: vind jij. Die uitzondering wordt het "
                 "vaakst vergeten.",
                 None,
                 "Bij een deelwoord vervang je het werkwoord door één waar je het verschil hóórt, zoals "
                 "gewerkt of geleerd. De stam van gebeuren eindigt op r, en die staat niet in 't kofschip, "
                 "dus wordt het gebeurd.",
                 None,
                 "De stam van verven eindigt op v, en de v staat niet in 't kofschip, dus geverfd met een "
                 "d. Die ene regel lost zowat elk deelwoord op.",
             ]),
        dict(aanpak="Een zwak werkwoord houdt zijn klinker en krijgt te of de; een sterk werkwoord "
                    "verandert zijn klinker.",
             waarom=[None]),
        dict(aanpak="Een samenstelling plakt twee bestaande woorden aan elkaar; een afleiding gebruikt een "
                    "voor- of achtervoegsel dat niet apart bestaat.",
             waarom=[None, None]),
        dict(aanpak="In de bedrijvende vorm doet het onderwerp de handeling, in de lijdende ondergaat het "
                    "ze. Omzetten betekent dat de lijdend voorwerp onderwerp wordt.",
             waarom=[
                 None, None,
                 "Dat is net waarom de lijdende vorm soms gebruikt wordt: er is een fout gemaakt zegt niet "
                 "wie ze maakte.",
                 "Het hangt af van de laatste letter van de stam: 't kofschip of fokschaap beslist tussen t "
                 "en d.",
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Het springen naar de tegenwoordige tijd heet de historische tegenwoordige tijd. In een "
                 "gesprek mag dat; in een verslag hou je één tijd aan.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-zinsdelen-en-samengestelde-zinnen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Zoek altijd eerst de persoonsvorm, dan het onderwerp met wie of wat, en dan pas de "
                    "rest. In die volgorde valt elk zinsdeel op zijn plaats.",
             waarom=[
                 "Het meewerkend voorwerp kan je herkennen aan de vraag aan wie: zij geeft het boek áán haar "
                 "broer.",
                 "Let op het verschil tussen een bijwoordelijke bepaling en een voorzetselvoorwerp: bij het "
                 "tweede ligt het voorzetsel vast bij het werkwoord, je wacht altijd óp iets.",
             ]),
        dict(aanpak="Zet de persoonsvorm vooraan in gedachten en vraag wie of wat. Wat daarop antwoordt, is "
                    "het onderwerp, ook al staat het achteraan.",
             waarom=[
                 "Er staat iemand is een valkuil: er is geen onderwerp, iemand wel. Het woord er vult enkel "
                 "de eerste plaats op.",
             ]),
        dict(aanpak="Een hoofdzin kan op zichzelf staan, een bijzin niet. Kijk ook naar de persoonsvorm: in "
                    "een bijzin schuift ze naar achter.",
             waarom=[None, None, None, None]),
        dict(aanpak="Nevenschikking zet twee gelijkwaardige zinnen naast elkaar (en, maar, of, want). "
                    "Onderschikking hangt er een bijzin onder (omdat, toen, dat, die).",
             waarom=[
                 None,
                 "Dit is de snelste toets die er is: staat de persoonsvorm achteraan, dan is het een "
                 "bijzin. Je hoeft het voegwoord niet eens te kennen.",
             ]),
        dict(aanpak="Zet de twee zinnen om tot één: één wordt hoofdzin, de andere bijzin. Vergeet de komma "
                    "voor de bijzin niet als die ertussen staat.",
             waarom=[
                 None, None,
                 "Elke persoonsvorm hoort bij één zin. Tel je er twee, dan is de zin samengesteld.",
                 "Een bijzin heeft altijd een hoofdzin nodig. Daarom is omdat het regent op zich geen zin.",
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Hardop ontleden is de beste manier: zodra je het moet zeggen, hoor je zelf waar je "
                 "twijfelt.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-spelling-leestekens-en-klanken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="In het Nederlands krijgen talen, volkeren en aardrijkskundige namen een hoofdletter; "
                    "dagen, maanden en seizoenen niet.",
             waarom=[
                 "Let op het verschil met het Engels: daar krijgen dagen en maanden wél een hoofdletter. "
                 "Daarom gaat dit zo vaak mis.",
                 None, None,
             ]),
        dict(aanpak="Twee woorden die samen één begrip vormen, schrijf je aan elkaar. Een streepje komt er "
                    "enkel waar klinkers tegen elkaar botsen of waar het anders onleesbaar wordt.",
             waarom=[
                 "Ten minste los betekent op zijn minst, tenminste aaneen betekent althans. De betekenis "
                 "bepaalt de schrijfwijze.",
                 None,
             ]),
        dict(aanpak="Lees de zin hardop en luister naar de pauzes. Een komma bij een opsomming en voor "
                    "maar, een dubbelpunt voor wat je aankondigt, aanhalingstekens rond wat iemand zegt.",
             waarom=[
                 "Let op waar de aanhalingstekens sluiten en weer openen: de tussenzin vroeg hij staat "
                 "erbuiten.",
                 None, None,
             ]),
        dict(aanpak="Puntkomma en dubbelpunt worden door elkaar gehaald. De puntkomma scheidt, de "
                    "dubbelpunt kondigt aan.",
             waarom=[None, None]),
        dict(aanpak="Een lettergreep heeft altijd één klinkerklank. Of een medeklinker verdubbelt, hangt af "
                    "van de lengte van de klinker ervoor.",
             waarom=[
                 None,
                 "Dit is de regel achter zowat alle verdubbelingen: een korte klinker houdt zijn klank "
                 "doordat er twee medeklinkers achter komen.",
                 None,
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Een dictee hardop laat je horen wat je ziet: een komma is een korte pauze, een punt een "
                 "lange.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-betekenis-beeldspraak-en-gevoelswaarde-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Zoek het woordje als of zoals. Staat het er, dan is het een vergelijking; staat het er "
                    "niet en wordt het ene gewoon het andere genoemd, dan is het een metafoor.",
             waarom=[
                 "Let op de twee laatste: dezelfde gedachte, één keer met als en één keer zonder. Dat ene "
                 "woordje bepaalt de naam.",
             ]),
        dict(aanpak="Vraag je af wat de schrijver doet: iets levends maken van iets doods, overdrijven, het "
                    "omgekeerde zeggen van wat hij bedoelt, verzachten of juist verharden.",
             waarom=[
                 "Ironie herken je aan het verschil tussen de woorden en de situatie. Zonder die situatie is "
                 "het gewoon een compliment.",
                 "Een eufemisme verzacht, een dysfemisme maakt harder. Allebei beschrijven ze hetzelfde "
                 "feit met een ander gevoel.",
             ]),
        dict(aanpak="Veel uitdrukkingen kunnen allebei: letterlijk kloppen én figuurlijk iets anders "
                    "betekenen. Kijk naar de situatie om te weten welke bedoeld is.",
             waarom=[None, None, None]),
        dict(aanpak="Zoek het oordeel dat in het woord zelf zit. Dezelfde eigenschap kan positief of "
                    "negatief klinken naargelang het woord dat je kiest.",
             waarom=[
                 None,
                 "Dit komt terug bij elke tekst die wil overtuigen: de woordkeuze draagt het oordeel, ook "
                 "als alle feiten kloppen.",
             ]),
        dict(aanpak="Een onbekend woord raad je uit de zin eromheen en uit de bouw van het woord zelf.",
             waarom=[
                 None, None,
                 "Synoniemen betekenen ongeveer hetzelfde, maar niet precies. Gevoelswaarde en register "
                 "verschillen bijna altijd.",
             ]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[None]),
    ],
)

UITLEGBLADEN["oefenbundel-feit-en-mening-stelling-argument-en-conclusie-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(aanpak="Vraag je af of je het kan nagaan. Staat er een getal, een datum of een naam, dan is "
                    "het meestal een feit; staat er een oordeelswoord in, dan een mening.",
             waarom=[
                 None, None, None,
                 "Onbetaalbaar is het oordeelswoord: wat voor de ene veel is, is dat voor de andere niet. "
                 "Het bedrag zelf is wel een feit.",
                 None, None,
             ]),
        dict(aanpak="De stelling is de uitspraak waarover het gaat, het standpunt is of je voor of tegen "
                    "bent, een argument is de reden, en de conclusie herhaalt waar het toe leidt.",
             waarom=[
                 "Let op het verschil tussen de stelling en het standpunt: de stelling ligt op tafel, het "
                 "standpunt is wat jij ervan vindt.",
                 None,
             ]),
        dict(aanpak="Let bij elke uitspraak op wat een goede opbouw hoort te doen: niets nieuws in het slot, "
                    "en argumenten die echt over de stelling gaan.",
             waarom=[
                 None, None,
                 "Een conclusie bindt samen wat er al stond. Een nieuw argument hoort in het midden, want "
                 "de lezer kan er in het slot niets meer mee.",
                 "Een tegenargument noemen en het daarna weerleggen, maakt een betoog juist sterker. Het "
                 "toont dat je de andere kant kent.",
                 None,
             ]),
        dict(aanpak="Want en omdat geven een reden, daarom een gevolg, maar een tegenstelling. Let op de "
                    "plaats in de zin: want staat tussen twee hoofdzinnen, omdat begint een bijzin.",
             waarom=[None]),
        dict(aanpak="Zoek bij een zwak argument wat er ontbreekt: een reden die nieuw is, of een feit dat je "
                    "kan nagaan.",
             waarom=[
                 "Dit heet een cirkelredenering: de reden is het standpunt zelf. Het klinkt als een "
                 "argument maar zegt niets.",
                 None,
             ]),
        dict(aanpak="Bouw op in vier stappen: stelling, standpunt, argumenten, conclusie. Zet bij elk "
                    "argument iets wat je kan nagaan.",
             waarom=[None]),
        dict(aanpak="Spreken twee bronnen elkaar tegen, kijk dan naar zender, datum en bedoeling voor je "
                    "kiest.",
             waarom=[None]),
        dict(aanpak="Deze oefening tel je pas af als je ze echt gedaan hebt.",
             waarom=[
                 "Een gesprek winnen en een gesprek voeren zijn twee verschillende dingen. Kunnen zeggen "
                 "dat de ander daar een punt heeft, is een vaardigheid op zich.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-fictie-personages-verhaallijn-tijd-en-ruimte-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Stel één vraag: is dit verzonnen of niet? Non-fictie gaat over wat echt gebeurd is en wat je kan nakijken. Fictie is verzonnen, ook als de schrijver echte plaatsen, echte jaartallen of een echte gebeurtenis gebruikt om haar verhaal in te zetten.",
            waarom=[
                "Een biografie vertelt het leven van een mens die echt bestond, en de schrijver moet zich aan de feiten houden.",
                None,
                "Een reisverslag gaat over een tocht die echt gemaakt is, dus je kan nakijken wat er staat.",
                "De staking is echt, maar de mensen in het boek zijn verzonnen. Zodra de personages verzonnen zijn, is het verhaal fictie.",
                None,
            ],
        ),
        dict(
            aanpak="Vier vragen helpen je kiezen. Wie? Dat is een personage. Waar? Dat is de ruimte. Wanneer en hoe lang? Dat is de tijd. Wat gebeurt er, en in welke orde? Dat is de verhaallijn.",
            waarom=[
                "Let op het verschil tussen tijd en verhaallijn. De tijd is wanneer het speelt en hoe lang het duurt (één nacht). De verhaallijn is de rij gebeurtenissen zelf: eerst de brand, dan het proces, dan de verhuizing.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak twee keer en zoek het woordje dat ze te streng maakt: moet, altijd, daarom. Eén tegenvoorbeeld is genoeg om zo'n uitspraak te kelderen.",
            waarom=[
                "Veel boeken lopen met twee of drie lijnen naast elkaar, bijvoorbeeld het verhaal van de moeder en dat van de dochter.",
                "Een verhaal mag beginnen bij het einde, terugspringen in de tijd of met flashbacks werken. Dat is een keuze van de schrijver, geen regel.",
                "Een literaire tekst gaat over hoe iets verteld wordt, niet over de vorm. Ook een strip, een gedicht, een hoorspel of een film kan literair zijn.",
                "Een bijsluiter is een zakelijke, informatieve tekst. Hij wil je iets laten doen of weten, niet iets laten voelen of ervaren.",
                "Dit is de klassieke valkuil. Gebaseerd op ware feiten betekent dat de schrijver vertrokken is van iets echts, maar de personages en gesprekken erbij verzonnen heeft. Dan is het nog altijd fictie.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je af wat de ruimte en de tijd met de personages dóen. Een kleine ruimte of een korte tijd zet mensen onder druk: ze kunnen niet weg en ze kunnen niet wachten. Een grote ruimte of een lange tijd geeft lucht.",
            waarom=[
                "Eén huis en één storm betekent: geen uitweg en geen uitstel. Daarom voelt zo'n verhaal benauwd, ook als er niets gewelddadigs gebeurt.",
                "In een klein dorp is afwezigheid zichtbaar en wordt er gepraat. Wat in een stad niemand opvalt, weet in een dorp de volgende dag iedereen.",
            ],
        ),
        dict(
            aanpak="Een feit kan je nakijken door het boek open te slaan: het staat er, of het staat er niet. Een interpretatie is wat jij uit het boek haalt. Die kan goed onderbouwd zijn en toch anders zijn dan die van iemand anders.",
            waarom=[
                None,
                "Wat een schrijver wil laten zien, staat nergens in het boek geschreven. Jij leidt het af, en dat is een interpretatie, ook als bijna elke lezer ze deelt.",
                "Groeien is iets wat jij vaststelt door het begin met het einde te vergelijken. Twee lezers kunnen daarover van mening verschillen.",
                "Een jaartal staat zwart op wit in de tekst, dus dat is een feit.",
            ],
        ),
        dict(
            aanpak="Een bruikbare zin over een boek zegt twee dingen: wat het met jou deed, en waardoor precies. Zonder dat tweede stuk is het een oordeel waar niemand iets mee kan.",
            waarom=[
                "Zin a zegt alleen dát je het goed vond. Zin b zegt wat er met je gebeurde (verward) en waardoor (je wist niet wie gelijk had). Daar kan je gesprekspartner op ingaan.",
                "Er is geen juist antwoord, maar er is wel een test: kan je bij elk van de drie zinnen een stuk uit het boek aanwijzen? Lukt dat niet, dan blijf je bij een gevoel hangen.",
            ],
        ),
        dict(
            aanpak="Deze oefening lukt pas als je ze echt doet. Drie minuten is langer dan je denkt, en zonder de verhaallijn moet je het over de personages en de ruimte hebben. Precies dat is wat een gesprek over een boek vraagt.",
            waarom=[
                "Er is geen juist antwoord. Let op één teken: wilde de ander na drie minuten weten hoe het afliep? Dan heb je hem nieuwsgierig gemaakt zonder het verhaal weg te geven.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-lichaamstaal-beleefdheid-en-een-tekst-die-werkt-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de vijf woorden even op een rij met wat ze betekenen. Mimiek is je gezicht. Intonatie is hoe je stem op en neer gaat. Articulatie is hoe duidelijk je de klanken vormt. Tempo is hoe snel je spreekt. Volume is hoe hard.",
            waarom=[
                "Verwar articulatie niet met volume. Binnensmonds spreken kan luid gebeuren en nog altijd onverstaanbaar zijn: het zijn de klanken die niet afgewerkt worden.",
            ],
        ),
        dict(
            aanpak="Vraag je telkens af aan wie je schrijft en wat jullie verhouding is. Hetzelfde teken of woord kan in het ene gesprek perfect zijn en in het andere misplaatst. Het gaat niet over goed of slecht Nederlands, maar over het register.",
            waarom=[
                "Een sollicitatiemail is een formele tekst aan iemand die je niet kent en die over jou beslist. Smileys maken de toon te vertrouwelijk.",
                None,
                "Groetjes hoort bij een informeel bericht. In een formele mail schrijf je met vriendelijke groeten of met de meeste hoogachting.",
                None,
                "Hoofdletters lezen als roepen. Wil je iets uitlichten, gebruik dan één woord vet of een korte zin apart.",
            ],
        ),
        dict(
            aanpak="De criteria van het examen zijn een lijstje waarop je je eigen tekst kan nakijken. Zoek bij elke opmerking waar ze precies over gaat: over wat je wilde bereiken, over je zinnen, over de bouw van je tekst, of over je toon.",
            waarom=[
                "Taakvoltooiing gaat over de opdracht: heb je gedaan wat er gevraagd werd, en bereikt je tekst zijn doel? Een tekst kan vlekkeloos geschreven zijn en hier toch op afgaan.",
                "Alinea's zijn geen opmaak maar inhoud: elke alinea is één deelonderwerp. Zonder alinea's ziet je lezer niet waar het ene stuk eindigt en het andere begint.",
            ],
        ),
        dict(
            aanpak="Vraag je af of de lezer het ziet of de luisteraar het hoort. Wat met letters en bladindeling te maken heeft, geldt enkel bij schrijven. Wat met je stem en je lichaam te maken heeft, geldt enkel bij spreken.",
            waarom=[
                "Een luisteraar hoort geen punten en komma's, dus dit criterium kan enkel bij een schrijfopdracht gelden.",
                None,
                "Lay-out is wat je op het blad ziet: alinea's, tussentitels, witruimte. Bij spreken bestaat dat niet.",
                "Vlotheid gaat over doorspreken zonder te blijven haperen of te veel euh te zeggen.",
                None,
            ],
        ),
        dict(
            aanpak="Zoek weer het te strenge woordje: elke, altijd, nooit, niet. En wees voorzichtig met uitspraken die te mooi klinken om waar te zijn, zoals het idee dat je liegen kan zien.",
            waarom=[
                "Een emoji vervangt net wat je gezicht en je stem zouden doen. Daarom hoort hij bij non-verbale communicatie.",
                "Dit is een hardnekkig misverstand. Onderzoek laat zien dat mensen leugens amper beter herkennen dan door te gokken. Wegkijken of friemelen kan ook zenuwen of verlegenheid zijn.",
                "Notities zijn voor jou, niet voor een lezer. Afkortingen, symbolen, een schema, een tabel of een mindmap mogen allemaal.",
                "Een korte tekst van drie alinea's heeft geen tussentitels nodig. Een gepaste lay-out past bij de lengte en het soort tekst.",
                None,
                "Een woordenboek mag, ook online. Het gaat om een hulpmiddel, niet om iemand die het werk voor je doet.",
                "Hoe je erbij staat en hoe je gekleed bent, zegt iets voor je eerste woord gevallen is. Dat is ook communicatie.",
            ],
        ),
        dict(
            aanpak="Een strategie is een plan dat je kiest voordat je begint. Bij een onbekend woord ga je van wat je zelf kan naar wat je moet opzoeken. Bij spreken kies je een hulpmiddel dat je houvast geeft zonder je vast te zetten.",
            waarom=[
                "Opzoeken is de laatste stap, niet de eerste. Op het examen heb je ook geen tijd om elk woord na te kijken, en vaak heb je het woord niet nodig om de vraag te kunnen beantwoorden.",
                "Een uitgeschreven tekst lees je af: je kijkt naar je blad in plaats van naar je publiek, en één gemiste zin brengt je van je lijn. Kernwoorden houden je op koers en laten je vrij.",
            ],
        ),
        dict(
            aanpak="Let op wat er wél geëist wordt en wat niet. Bij notities wordt de vorm niet beoordeeld, maar het nut wel.",
            waarom=[
                "De eis is dat je notities bij de inhoud aansluiten en achteraf nog bruikbaar zijn, bijvoorbeeld om er een samenvatting mee te maken. Nette volledige zinnen zijn geen eis.",
            ],
        ),
        dict(
            aanpak="Je eigen stem terughoren is ongemakkelijk, en daarom werkt het. Je hoort in één keer wat je publiek de hele tijd hoort.",
            waarom=[
                "Er is geen juist antwoord. De meeste mensen schrikken vooral van hun tempo. Wie zichzelf één keer teruggehoord heeft, spreekt daarna bijna altijd trager en duidelijker.",
            ],
        ),
    ]
)
