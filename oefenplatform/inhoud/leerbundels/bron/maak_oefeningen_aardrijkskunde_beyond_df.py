# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij aardrijkskunde 🌍 Beyond dubbele finaliteit.

De fiche van dubbele finaliteit volgt dezelfde leerstof als die van doorstroom,
maar lichter en concreter: het examen bestaat uit gesloten vraagvormen, zonder
giscorrectie, met de atlas en Geopunt bij de hand. Deze bundels hergebruiken
daarom de reeksen van `maak_oefeningen_aardrijkskunde_beyond.py` die feiten en
toepassingen oefenen, laten de zwaarste redeneeropdrachten daar, en zetten er
oefeningen bij die bij deze fiche horen: werken met de atlas, een kaart of een
grafiek lezen, en een oordeel geven over een geval uit de eigen omgeving.

Eén bundel per thema, niet per deel. De sleutels dragen het voorvoegsel
"oefenbundel-" en het achtervoegsel "-beyond-dubbele-finaliteit".
"""
import copy
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel
import maak_oefeningen_aardrijkskunde_beyond as door

VAK = "Aardrijkskunde"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
NIVEAU = "-beyond-dubbele-finaliteit"
VOOR = "oefenbundel-"

W = "120px"
WW = "185px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag: schrijf eerst de bewerking op en zet de eenheid erbij.",
    "Je mag de atlas en Geopunt gebruiken, net als op het examen.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def reeks(slug, kop, weg=()):
    """Eén reeks uit de bundel van doorstroom, eventueel zonder een paar
    oefeningen die hier te zwaar zijn (nummer vanaf 1)."""
    for r in door.OEFENBUNDELS["oefenbundel-" + slug + "-beyond"]["reeksen"]:
        if r["kop"] == kop:
            r = copy.deepcopy(r)
            if weg:
                r["oefeningen"] = [o for i, o in enumerate(r["oefeningen"], 1) if i not in weg]
            return r
    raise KeyError(f"{slug}: {kop}")


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("situeren-op-aarde-en-de-aardse-sferen",
    titel="Situeren op aarde en de aardse sferen",
    reeksen=[
        reeks("situeren-kaarten-en-observatie", "Coördinaten omzetten", weg=(5,)),
        reeks("situeren-kaarten-en-observatie", "Absoluut of relatief?"),
        reeks("situeren-kaarten-en-observatie", "De schaal", weg=(6,)),
        dict(kop="Met de atlas erbij",
             opdracht="Zoek de plaatsen op in je atlas en schrijf de coördinaten op, afgerond "
                      "op een halve graad.",
             oefeningen=[
                 ("rij", [("Reykjavik", "ongeveer 64° NB, 22° WL"),
                          ("Nairobi", "ongeveer 1° ZB, 37° OL"),
                          ("Sydney", "ongeveer 34° ZB, 151° OL"),
                          ("Quito", "ongeveer 0°, 78° WL")],
                  "Welke coördinaten?", WL),
                 ("kort", "Welke van die vier ligt het dichtst bij de evenaar?",
                  "Quito (en Nairobi ligt er ook vlakbij)", WL),
                 ("kort", "Welke ligt op het zuidelijk halfrond én op het oostelijk halfrond?",
                  "Sydney", W),
             ]),
        reeks("situeren-kaarten-en-observatie", "De vier sferen"),
    ])

# ============================================================
zet("het-heelal-en-de-plaats-van-de-aarde",
    titel="Het heelal en de plaats van de aarde",
    reeksen=[
        reeks("het-heelal-ontstaan-en-afstanden", "De Big Bang op een rij"),
        reeks("het-heelal-ontstaan-en-afstanden", "Drie vaststellingen", weg=(4,)),
        reeks("het-heelal-ontstaan-en-afstanden", "Afstanden rekenen", weg=(5,)),
        reeks("het-heelal-ontstaan-en-afstanden", "Het adres van de aarde"),
        dict(kop="Groot, groter, grootst",
             opdracht="Zet in de orde van klein naar groot, met 1 tot 5.",
             oefeningen=[
                 ("rij", [("de maan", "1"), ("de aarde", "2"), ("Jupiter", "3"),
                          ("de zon", "4"), ("de Melkweg", "5")],
                  "Welk nummer?", "58px"),
                 ("kort", "Hoeveel keer past de aarde ongeveer in de zon, qua doorsnede?",
                  "ongeveer 109 keer", WW),
                 ("waar", "Een lichtjaar is een maat voor tijd.", False),
             ]),
    ])

# ============================================================
zet("het-zonnestelsel-en-zijn-kleine-lichamen",
    titel="Het zonnestelsel en zijn kleine lichamen",
    reeksen=[
        reeks("de-zon-en-het-zonnestelsel", "De lagen van de zon"),
        reeks("de-zon-en-het-zonnestelsel", "Wat de zon uitstuurt"),
        reeks("de-zon-en-het-zonnestelsel", "De acht planeten"),
        reeks("de-zon-en-het-zonnestelsel", "Gordels, dwergplaneten en kometen"),
        dict(kop="De volgorde van de planeten",
             opdracht="Vul aan vanaf de zon.",
             oefeningen=[
                 ("rij", [("1", "Mercurius"), ("2", "Venus"), ("3", "de aarde"),
                          ("4", "Mars"), ("5", "Jupiter"), ("6", "Saturnus"),
                          ("7", "Uranus"), ("8", "Neptunus")],
                  "Welke planeet?", WW),
                 ("kies", "Welke is de grootste planeet?",
                  ["de aarde", "Saturnus", "Jupiter", "Neptunus"], 2),
                 ("kies", "Welke staat het verst van de zon?",
                  ["Uranus", "Neptunus", "Pluto", "Saturnus"], 1),
             ]),
    ])

# ============================================================
zet("de-bewegingen-van-de-aarde",
    titel="De bewegingen van de aarde",
    reeksen=[
        reeks("de-bewegingen-van-de-aarde", "Rotatie of revolutie?"),
        reeks("de-bewegingen-van-de-aarde", "Rekenen met uurgordels"),
        reeks("de-bewegingen-van-de-aarde", "Het corioliseffect", weg=(4,)),
        reeks("de-bewegingen-van-de-aarde", "De schuine as en de seizoenen"),
        dict(kop="De dag duurt niet overal even lang",
             opdracht="Vul in met korter, langer of even lang.",
             oefeningen=[
                 ("rij", [("21 juni in Oslo, vergeleken met Rome", "langer"),
                          ("21 december in Oslo, vergeleken met Rome", "korter"),
                          ("21 maart in Quito, vergeleken met Hasselt", "even lang"),
                          ("21 juni op de evenaar, vergeleken met 21 december daar",
                           "even lang")],
                  "Korter, langer of even lang?", WW),
                 ("kort", "Hoeveel uur duurt de dag op de evenaar het hele jaar door?",
                  "ongeveer twaalf uur", WW),
             ]),
    ])

# ============================================================
zet("de-atmosfeer-en-de-temperatuur-op-aarde",
    titel="De atmosfeer en de temperatuur op aarde",
    reeksen=[
        reeks("de-opbouw-van-de-atmosfeer", "De lagen"),
        reeks("de-opbouw-van-de-atmosfeer", "Rekenen met de gradiënt"),
        reeks("de-opbouw-van-de-atmosfeer", "Waar de lucht uit bestaat", weg=(2,)),
        reeks("de-opbouw-van-de-atmosfeer", "Albedo", weg=(3,)),
        reeks("de-opbouw-van-de-atmosfeer", "Wat de temperatuur van een plaats bepaalt",
              weg=(4,)),
        dict(kop="Een klimatogram lezen",
             opdracht="Een station meet in januari 2 °C en 70 mm, in juli 18 °C en 55 mm.",
             oefeningen=[
                 ("kort", "Hoe groot is de jaarschommeling van de temperatuur?",
                  "18 − 2 = 16 °C", W),
                 ("kort", "In welk halfrond ligt dit station, en waaraan zie je dat?",
                  "het noordelijke: juli is de warmste maand", WL),
                 ("kies", "Welk klimaat past hierbij?",
                  ["een woestijnklimaat", "een gematigd zeeklimaat",
                   "een tropisch regenwoudklimaat", "een poolklimaat"], 1),
             ]),
    ])

# ============================================================
zet("luchtdruk-wind-en-de-grote-circulatie",
    titel="Luchtdruk, wind en de grote circulatie",
    reeksen=[
        reeks("luchtdruk-en-winden", "Hoge of lage druk?"),
        reeks("luchtdruk-en-winden", "Isobaren lezen", weg=(4,)),
        reeks("luchtdruk-en-winden", "De drukgordels"),
        reeks("luchtdruk-en-winden", "Winden met een naam"),
        dict(kop="Het weerbericht van vandaag",
             opdracht="Lees het bericht en antwoord. „Een hogedrukgebied van 1030 hPa boven "
                      "Midden-Europa houdt de depressies op de Atlantische Oceaan tegen. Bij ons "
                      "blijft het droog, met in de ochtend mist en in de namiddag een zwakke "
                      "oostenwind.”",
             oefeningen=[
                 ("kort", "Waarom blijft het droog?",
                  "in een hogedrukgebied daalt de lucht, dus vormen zich geen regenwolken", WL),
                 ("kort", "Waarom is er 's ochtends mist?",
                  "de heldere nacht laat de grond sterk afkoelen tot onder het dauwpunt", WL),
                 ("kort", "Waar komt de wind vandaan, en wat zegt dat over de lucht?",
                  "uit het oosten: continentale lucht, dus droog", WL),
             ]),
    ])

# ============================================================
zet("water-in-de-lucht-en-de-neerslag",
    titel="Water in de lucht en de neerslag",
    reeksen=[
        reeks("neerslag-en-de-kringloop-van-het-water", "De kringloop benoemen"),
        reeks("neerslag-en-de-kringloop-van-het-water", "Vochtigheid en dauwpunt"),
        reeks("neerslag-en-de-kringloop-van-het-water", "Neerslag meten"),
        reeks("neerslag-en-de-kringloop-van-het-water", "Drie soorten regen", weg=(3,)),
        dict(kop="Regenwater thuis",
             opdracht="Reken na voor een huis met een dak van 90 m² en een put van 5000 liter.",
             oefeningen=[
                 ("kort", "Hoeveel liter levert een bui van 12 mm?",
                  "12 × 90 = 1080 liter", WW),
                 ("kort", "Bij 800 mm regen per jaar: hoeveel liter is dat in een jaar?",
                  "800 × 90 = 72 000 liter", WW),
                 ("kort", "Hoeveel keer zou de put daarmee gevuld kunnen worden?",
                  "ongeveer veertien keer", W),
                 ("open", "Waarom is een grotere put niet altijd beter?",
                  "Een put die zelden volloopt, kost geld en plaats zonder meer water op te "
                  "leveren. Wat je kan gebruiken hangt af van het dakoppervlak en van je "
                  "verbruik, niet van de grootte alleen.", 3),
             ]),
    ])

# ============================================================
zet("klimaten-biomen-en-zeestromen",
    titel="Klimaten, biomen en zeestromen",
    reeksen=[
        reeks("klimaatgebieden-biomen-en-zeestromen", "Weer of klimaat?"),
        reeks("klimaatgebieden-biomen-en-zeestromen", "Van klimaat naar bioom"),
        reeks("klimaatgebieden-biomen-en-zeestromen", "Zeestromen"),
        reeks("klimaatgebieden-biomen-en-zeestromen", "De thermohaliene circulatie", weg=(3,)),
        dict(kop="Vier plaatsen vergelijken",
             opdracht="Zoek de plaatsen in de atlas en vul aan.",
             oefeningen=[
                 ("tabel", ["plaats", "klimaat", "bioom"],
                  [["Manaus (Brazilië)", "tropisch regenwoudklimaat", "tropisch regenwoud"],
                   ["Caïro (Egypte)", "", ""],
                   ["Rome (Italië)", "", ""],
                   ["Tromsø (Noorwegen)", "", ""]],
                  "Vul de twee lege kolommen aan.", WW),
             ]),
    ])


# ============================================================
zet("de-bouw-van-de-aarde-en-de-platentektoniek",
    titel="De bouw van de aarde en de platentektoniek",
    reeksen=[
        reeks("de-opbouw-van-de-geosfeer", "Chemisch of fysisch ingedeeld?", weg=(5,)),
        reeks("de-opbouw-van-de-geosfeer", "Twee soorten korst", weg=(2,)),
        reeks("platentektoniek-en-reliefvorming", "De bewijzen van Wegener", weg=(3,)),
        reeks("platentektoniek-en-reliefvorming", "Drie soorten plaatbeweging"),
        reeks("platentektoniek-en-reliefvorming", "Wat de platen beweegt"),
        dict(kop="Op de kaart",
             opdracht="Zoek de plaatsen in de atlas en schrijf op welke plaatbeweging er "
                      "speelt.",
             oefeningen=[
                 ("rij", [("IJsland", "divergent: de Midden-Atlantische Rug"),
                          ("de westkust van Zuid-Amerika", "convergent: subductie, de Andes"),
                          ("de Himalaya", "convergent: twee continenten botsen"),
                          ("Californië, de San Andreasbreuk", "transform: langs elkaar")],
                  "Welke beweging?", WL),
                 ("kort", "Waarom liggen bijna alle vulkanen en bevingen in dezelfde smalle "
                          "banden?", "dat zijn de randen van de platen", WL),
             ]),
    ])

# ============================================================
zet("vulkanen-en-aardbevingen",
    titel="Vulkanen en aardbevingen",
    reeksen=[
        reeks("aardbevingen-en-vulkanisme", "Waar een beving begint", weg=(5,)),
        reeks("aardbevingen-en-vulkanisme", "Magnitude of intensiteit?", weg=(4,)),
        reeks("aardbevingen-en-vulkanisme", "De delen van een vulkaan"),
        reeks("aardbevingen-en-vulkanisme", "Twee soorten vulkanen", weg=(2,)),
        reeks("aardbevingen-en-vulkanisme", "Toch wonen op een vulkaan"),
        dict(kop="Wat doe je bij een beving?",
             opdracht="Schrijf goed of fout, en in één woord waarom.",
             oefeningen=[
                 ("rij", [("onder een stevige tafel kruipen", "goed: bescherming tegen vallend puin"),
                          ("de lift nemen naar beneden", "fout: de lift kan blokkeren"),
                          ("in een deuropening van een oud huis gaan staan",
                           "fout: dat is een oud advies, de deurlijst beschermt niet"),
                          ("na de beving weg van de kust gaan", "goed: er kan een tsunami komen")],
                  "Goed of fout, en waarom?", WL),
             ]),
    ])

# ============================================================
zet("gesteenten-en-de-geologische-tijd",
    titel="Gesteenten en de geologische tijd",
    reeksen=[
        reeks("gesteenten-mineralen-en-datering", "In welke groep?"),
        reeks("gesteenten-mineralen-en-datering", "Grof of fijn?", weg=(1,)),
        reeks("gesteenten-mineralen-en-datering", "Wat wordt wat?"),
        reeks("gesteenten-mineralen-en-datering", "De lagen lezen", weg=(2,)),
        reeks("gesteenten-mineralen-en-datering", "Absolute datering", weg=(5,)),
        dict(kop="Waarvoor gebruiken we het?",
             opdracht="Schrijf bij elk gesteente waarvoor de mens het gebruikt.",
             oefeningen=[
                 ("rij", [("kalksteen", "cement, kalk, bouwsteen"),
                          ("graniet", "keien, gevels, werkbladen"),
                          ("leisteen", "dakleien"),
                          ("klei", "bakstenen en dakpannen"),
                          ("zand en grind", "beton en wegen")],
                  "Waarvoor?", WL),
                 ("kort", "Welk gesteente ligt onder de Kempen en werd er tot 1992 "
                          "ontgonnen?", "steenkool", WW),
             ]),
    ])

# ============================================================
zet("verwering-en-massatransport",
    titel="Verwering en massatransport",
    reeksen=[
        reeks("verwering-karst-en-massatransport", "Verwering, erosie of sedimentatie?"),
        reeks("verwering-karst-en-massatransport", "Drie soorten verwering", weg=(2,)),
        reeks("verwering-karst-en-massatransport", "Karst", weg=(4,)),
        reeks("verwering-karst-en-massatransport", "Massatransport", weg=(3,)),
        reeks("verwering-karst-en-massatransport", "Wat mensen eraan doen", weg=(2,)),
        dict(kop="Verwering in je eigen straat",
             opdracht="Schrijf welke soort verwering je hier ziet.",
             oefeningen=[
                 ("rij", [("een gevel met afgebrokkelde voegen na een strenge winter",
                           "mechanisch: vorstverwering"),
                          ("een grafsteen in kalksteen waarvan de letters vervagen",
                           "chemisch: oplossing door zuur regenwater"),
                          ("een stoeptegel die omhoog geduwd wordt door een boomwortel",
                           "biologisch"),
                          ("roestbruine vlekken op een oude ijzeren poort", "chemisch: oxidatie")],
                  "Welke soort?", WL),
             ]),
    ])

# ============================================================
zet("erosie-door-water-ijs-en-wind",
    titel="Erosie door water, ijs en wind",
    reeksen=[
        reeks("erosie-door-water-ijs-en-wind", "Het stroombekken"),
        reeks("erosie-door-water-ijs-en-wind", "Boven-, midden- of benedenloop?", weg=(2,)),
        reeks("erosie-door-water-ijs-en-wind", "Meanders", weg=(4,)),
        reeks("erosie-door-water-ijs-en-wind", "IJs en wind", weg=(3,)),
        reeks("erosie-door-water-ijs-en-wind", "Overstromen"),
        dict(kop="De Maas en de Schelde",
             opdracht="Zoek het op in de atlas en antwoord.",
             oefeningen=[
                 ("kort", "In welk land ontspringt de Maas?", "in Frankrijk", W),
                 ("kort", "Waar mondt de Schelde uit?",
                  "in de Noordzee, via de Westerschelde", WL),
                 ("kort", "Hoe heet de monding waar eb en vloed ver landinwaarts komen?",
                  "een estuarium", WW),
                 ("open", "Waarom is de Schelde in Antwerpen nog een getijdenrivier, zo ver van "
                          "zee?",
                  "Het verval is er heel klein en de monding is breed en diep, zodat de "
                  "vloedgolf van de Noordzee tot ver landinwaarts kan doordringen.", 3),
             ]),
    ])

# ============================================================
zet("de-huidige-klimaatverandering",
    titel="De huidige klimaatverandering",
    reeksen=[
        reeks("de-huidige-klimaatverandering", "Het broeikaseffect"),
        reeks("de-huidige-klimaatverandering", "Wat we nu al meten"),
        reeks("de-huidige-klimaatverandering", "Hoe we weten dat het de mens is", weg=(2,)),
        reeks("de-huidige-klimaatverandering", "Mitigatie of adaptatie?"),
        dict(kop="Je eigen voetafdruk",
             opdracht="Zet in de orde van de grootste uitstoot naar de kleinste, met 1 tot 5.",
             oefeningen=[
                 ("rij", [("een vlucht naar New York en terug", "1"),
                          ("een jaar met de auto naar school en terug, 10 km per dag", "2"),
                          ("een jaar elke dag rundvlees eten", "3"),
                          ("een jaar met de bus naar school", "4"),
                          ("een jaar met de fiets naar school", "5")],
                  "Welk nummer?", "58px"),
                 ("open", "Welke van die keuzes zou jij het eerst veranderen, en waarom net "
                          "die?",
                  "Een eigen antwoord, zolang het de grootte van het effect afweegt tegen wat "
                  "haalbaar is: een jaarlijkse verre vlucht weegt zwaarder dan de bus, maar wie "
                  "niet vliegt, wint meer met de fiets of met minder vlees.", 4),
             ]),
    ])

# ============================================================
zet("verstedelijking-en-het-ruimtelijk-beleid",
    titel="Verstedelijking en het ruimtelijk beleid",
    reeksen=[
        reeks("verstedelijking-en-ruimtegebruik", "Welke fase?"),
        reeks("verstedelijking-en-ruimtegebruik", "De Vlaamse ruimte", weg=(4,)),
        reeks("verstedelijking-en-ruimtegebruik", "Het hitte-eiland", weg=(3,)),
        reeks("verstedelijking-en-ruimtegebruik", "Wie beslist over de ruimte"),
        dict(kop="Je eigen gemeente",
             opdracht="Zoek het op in Geopunt en vul in voor je eigen gemeente.",
             oefeningen=[
                 ("kort", "Hoeveel inwoners telt je gemeente?",
                  "een eigen antwoord, uit Geopunt of de gemeentelijke website", WL),
                 ("kort", "Hoeveel vierkante kilometer is ze groot?",
                  "een eigen antwoord", W),
                 ("kort", "Bereken de bevolkingsdichtheid in inwoners per km².",
                  "inwoners gedeeld door de oppervlakte", WL),
                 ("open", "Zie je op de luchtfoto lintbebouwing, een compacte kern of allebei? "
                          "Beschrijf in twee zinnen wat je ziet.",
                  "Een eigen antwoord dat benoemt waar de bebouwing dicht is (meestal rond de "
                  "kerk, het station of de markt) en waar ze zich in linten langs de steenwegen "
                  "uitstrekt.", 3),
             ]),
    ])

# ============================================================
zet("het-landschap-lezen-en-duurzaam-ruimtegebruik",
    titel="Het landschap lezen en duurzaam ruimtegebruik",
    reeksen=[
        reeks("het-landschap-lezen", "Natuurlijk of menselijk?"),
        reeks("het-landschap-lezen", "Een landschap stap voor stap", weg=(2,)),
        reeks("het-landschap-lezen", "Kijken van boven"),
        reeks("duurzaam-ruimtegebruik", "Welke strategie?", weg=(3,)),
        reeks("duurzaam-ruimtegebruik", "Water en ontharden"),
        dict(kop="Een plek beoordelen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een supermarkt wil bouwen op een weide net buiten het dorp, met een "
                          "parking van honderd plaatsen. Geef twee argumenten voor en twee "
                          "tegen.",
                  "Voor: makkelijk bereikbaar met de auto, goedkope grond, werk in de gemeente. "
                  "Tegen: er verdwijnt open ruimte en de parking verhardt die, wie geen auto "
                  "heeft geraakt er niet, en de winkels in de kern verliezen klanten, waardoor "
                  "het centrum leegloopt.", 5),
                 ("open", "Geef één alternatief dat met dezelfde winkel minder ruimte "
                          "inneemt.",
                  "De winkel in de kern zetten of op een leegstaand terrein, met woningen "
                  "erboven en een ondergrondse of gedeelde parking, zodat dezelfde grond twee "
                  "of drie functies draagt.", 3),
             ]),
    ])
