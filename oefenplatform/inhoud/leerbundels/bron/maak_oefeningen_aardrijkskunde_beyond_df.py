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
                   ["Caïro (Egypte)", None, None],
                   ["Rome (Italië)", None, None],
                   ["Tromsø (Noorwegen)", None, None]],
                  "Caïro: woestijnklimaat, woestijn · Rome: mediterraan klimaat, hardbladig "
                  "struikgewas · Tromsø: subpolair klimaat met zachte zeewinters, taiga die "
                  "naar toendra overgaat", WW),
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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-situeren-op-aarde-en-de-aardse-sferen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een graad heeft zestig minuten, net als een uur. Van een decimale graad naar "
                   "minuten vermenigvuldig je het stuk achter de komma met 60; de andere kant op "
                   "deel je de minuten door 60. Schrijf de letter (NB, ZB, OL, WL) er altijd bij, "
                   "want zonder die letter is een coördinaat waardeloos.",
            waarom=[
                "Reken er één na om de techniek te zien: 0,5 maal 60 is 30, dus 50,5° wordt "
                "50° 30'. Bij d is het 0,1 maal 60 is 6, en dan schrijf je 06' met een nul "
                "ervoor, zoals bij de tijd.",
                "Nu de andere kant op: 15 gedeeld door 60 is 0,25, dus 51° 15' wordt 51,25°. "
                "Handig om te onthouden: 15' is een kwart, 30' is een half en 45' is "
                "driekwart.",
                "111 km per breedtegraad is een getal dat je echt moet kennen, want het komt "
                "overal terug. Het volgt uit de omtrek van de aarde: 40 000 km gedeeld door 360 "
                "graden is ongeveer 111 km.",
                "Reken na: 30' is een halve graad, dus de helft van 111 km is 55,5 km. Let op dat "
                "dit enkel voor breedtegraden opgaat; bij lengtegraden wordt de afstand kleiner "
                "naar de polen toe.",
            ],
        ),
        dict(
            aanpak="Absoluut situeren gebeurt met getallen die overal ter wereld dezelfde "
                   "betekenis hebben: coördinaten. Relatief situeren gebeurt ten opzichte van "
                   "iets anders: naast, boven, ten oosten van. Zie je cijfers met graden, dan is "
                   "het absoluut.",
            waarom=[
                None,
                None,
                None,
                "Ook deze is absoluut, ook al zijn de getallen rond. 60° ZB en 0° lengte is een "
                "punt op de aardbol dat iedereen kan terugvinden, en dat is precies wat absoluut "
                "betekent.",
                "Geef er echt twee van jezelf, want daar test de vraag op. De absolute haal je "
                "uit Geopunt of een kaartendienst; de relatieve bedenk je zelf, en dan merk je "
                "dat die laatste enkel werkt voor wie de buurt kent.",
            ],
        ),
        dict(
            aanpak="Een schaal is een deling. 1 : 25 000 betekent dat 1 cm op de kaart 25 000 cm "
                   "in het echt is. Van kaart naar werkelijkheid vermenigvuldig je, van "
                   "werkelijkheid naar kaart deel je. Zet alles eerst in centimeter en reken pas "
                   "op het einde om naar meter of kilometer.",
            waarom=[
                "Schrijf de bewerking op zoals in het antwoord, want de omzetting op het einde is "
                "waar het meestal fout gaat: 200 000 cm is 2000 m en dus 2 km.",
                "Dezelfde weg, een schaal die tweemaal zo groot is, dus tweemaal zoveel "
                "centimeter op papier. Je hoeft hier niet opnieuw te beginnen van de 2 km.",
                "Reken na: 15 km is 1 500 000 cm, gedeeld door 300 000 is 5 cm. Dit is de "
                "omgekeerde richting, dus deel je.",
                "Hier gaat bijna iedereen de mist in, want 10 000 is het kleinste getal. Maar de "
                "schaal is een breuk: een tiendduizendste is groter dan een miljoenste. Hoe "
                "kleiner het getal achter de dubbele punt, hoe groter de schaal.",
                "Waar, en het hoort bij de vorige vraag. Een grote schaal geeft een klein gebied "
                "met veel detail, zoals een stadsplan; een kleine schaal geeft een groot gebied "
                "met weinig detail, zoals een wereldkaart.",
            ],
        ),
        dict(
            aanpak="Zoek eerst het halfrond, dan de graden. Staat een plaats boven de evenaar, "
                   "dan is het NB; links van Greenwich WL, rechts OL. Een halve graad "
                   "nauwkeurigheid is ruim genoeg, dus lees af en rond af.",
            waarom=[
                "Merk op dat de vier plaatsen elk in een ander kwadrant liggen: Reykjavik in het "
                "noordwesten, Nairobi in het noordoosten net onder de evenaar, Sydney in het "
                "zuidoosten en Quito op de evenaar zelf.",
                "Quito ligt bijna precies op nul graden, vandaar ook de naam van het land: "
                "Ecuador is Spaans voor evenaar.",
                None,
            ],
        ),
        dict(
            aanpak="Vier sferen: geosfeer voor gesteente en bodem, hydrosfeer voor water in elke "
                   "vorm, atmosfeer voor lucht, biosfeer voor alles wat leeft. Vraag je bij elk "
                   "verschijnsel welke stof er eigenlijk beweegt.",
            waarom=[
                "Een ijskap hoort bij de hydrosfeer en niet bij de geosfeer: het is water, enkel "
                "in vaste vorm. Dat is de verwarring die deze tabel test.",
                "Geef een voorbeeld waarin je minstens drie sferen na elkaar noemt, met een omdat "
                "ertussen. Dat de sferen op elkaar inwerken, is de reden dat aardrijkskunde ze "
                "samen bekijkt in plaats van één per één.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-heelal-en-de-plaats-van-de-aarde-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de geschiedenis van het heelal op orde van klein naar groot: eerst de "
                   "deeltjes, dan de atomen, dan de sterren, en pas heel laat de planeten. De "
                   "aarde komt helemaal achteraan, want ze is maar een derde zo oud als het "
                   "heelal.",
            waarom=[
                "Merk de orde: deeltjes, dan atomen, dan sterren. Je kan geen ster maken zonder "
                "atomen, en geen planeet zonder sterren die eerst zwaardere stoffen gemaakt "
                "hebben.",
                None,
                "Zet de twee getallen naast elkaar: 13,8 miljard tegenover 4,6 miljard. De aarde "
                "bestaat dus pas een derde van de tijd van het heelal.",
            ],
        ),
        dict(
            aanpak="Drie onafhankelijke waarnemingen die naar dezelfde oerknal wijzen: de "
                   "roodverschuiving, de achtergrondstraling en de verhouding waterstof-helium. "
                   "Zeg bij elke vaststelling niet enkel wat je ziet maar wat ze aantoont.",
            waarom=[
                "Roder licht betekent uitgerekte golven, en dat gebeurt als de bron zich "
                "verwijdert, net zoals een sirene lager klinkt als ze voorbij is. Dat is het "
                "sterkste bewijs van de uitdijing.",
                None,
                "Niet waar, en dit is de belangrijkste vraag van de reeks. Alles verwijdert zich "
                "van alles, zoals de rozijnen in een rijzend brood: elke rozijn ziet de andere "
                "weggaan en geen enkele staat in het midden. Er is dus geen middelpunt.",
            ],
        ),
        dict(
            aanpak="Twee maten en twee bewerkingen. Een astronomische eenheid gebruik je binnen "
                   "het zonnestelsel: vermenigvuldigen met 149,6 miljoen km. Een lichtjaar "
                   "gebruik je voor sterren, en het zegt tegelijk hoe lang het licht onderweg "
                   "was.",
            waarom=[
                "Reken na: 1,5 maal 149,6 is 224,4 miljoen km. Rond gerust af op 224, want de "
                "baan is geen perfecte cirkel en de afstand schommelt sowieso.",
                "Reken na: 5,2 maal 149,6 is ongeveer 778 miljoen km. Zo zie je ineens hoe leeg "
                "het buitenste deel van het zonnestelsel is: Jupiter staat meer dan vijf keer "
                "verder dan wij.",
                None,
                "Dit is het mooiste gevolg van een lichtjaar: je kijkt altijd naar het verleden. "
                "Zou die ster vandaag ontploffen, dan zien wij dat pas over ruim vier jaar.",
            ],
        ),
        dict(
            aanpak="Het adres van de aarde gaat van klein naar groot: zonnestelsel, Melkweg, "
                   "Lokale Groep, Laniakea. Elke stap is een verzameling van de vorige, net als "
                   "straat, gemeente, provincie, land.",
            waarom=[
                "De Lokale Groep is onze buurt van sterrenstelsels, met de Andromedanevel als "
                "grootste buur; Laniakea is de supercluster waarin die hele groep meebeweegt.",
                "Honderd tot vierhonderd miljard sterren, en onze zon is er één van. Dat getal "
                "maakt pas duidelijk waarom men niet elke ster apart onderzoekt.",
            ],
        ),
        dict(
            aanpak="Een ordening op grootte, en de sprongen zijn enorm. Houd je aan de orde maan, "
                   "aarde, Jupiter, zon, Melkweg, en reken niet op je gevoel, want het verschil "
                   "tussen de stappen is telkens tientallen keren.",
            waarom=[
                "De sprongen zijn groter dan ze lijken: Jupiter is elf keer breder dan de aarde "
                "en de zon nog tien keer breder dan Jupiter.",
                "109 keer in doorsnede, en dat wil zeggen dat er qua volume meer dan een miljoen "
                "aardes in de zon passen. Een getal in doorsnede en een getal in volume zijn dus "
                "twee heel verschillende dingen.",
                "Niet waar: een lichtjaar is een afstand, namelijk de weg die het licht in een "
                "jaar aflegt. Het woord jaar in de naam maakt dit de meest gestelde valstrik van "
                "het hoofdstuk.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-zonnestelsel-en-zijn-kleine-lichamen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de lagen van de zon van binnen naar buiten: kern, stralingszone, "
                   "convectiezone, fotosfeer, chromosfeer, corona. De temperatuur daalt eerst van "
                   "binnen naar buiten en stijgt daarna weer, en net dat laatste wordt graag "
                   "gevraagd.",
            waarom=[
                "Onthoud de orde aan wat de energie doet: ze ontstaat in de kern, reist als "
                "straling, dan als stroming, en verlaat de zon aan de fotosfeer. Chromosfeer en "
                "corona zie je enkel bij een zonsverduistering.",
                None,
                "5500 graden is het oppervlak dat wij als de rand van de zon zien. Dat de kern "
                "bijna drieduizend keer heter is, is het hele punt: enkel bij zulke temperaturen "
                "werkt kernfusie.",
                "Niet waar, en het is een van de open vragen in de sterrenkunde. De corona is "
                "ongeveer een miljoen graden en dus veel heter dan de fotosfeer eronder, terwijl "
                "ze verder van de warmtebron ligt.",
                "Noem beide delen: fusie, en wat er fuseert. Waterstof wordt helium, en het "
                "kleine verschil in massa komt vrij als energie. Dat is ook de reden dat de zon "
                "nog miljarden jaren meegaat.",
            ],
        ),
        dict(
            aanpak="Vier begrippen die bij elkaar horen in één verhaal: een zonnevlek is een "
                   "koelere plek, een protuberans een lus gas, de zonnewind de stroom deeltjes, "
                   "en het poollicht wat we hier van die deeltjes zien.",
            waarom=[
                "Merk op dat een zonnevlek donker lijkt maar nog altijd duizenden graden heet "
                "is: donker is hier enkel donker ten opzichte van wat eromheen ligt.",
                "De cyclus van elf jaar is de reden dat poollicht in sommige jaren tot in België "
                "te zien is en in andere jaren bijna nooit.",
                "Noem er twee van verschillende soort, bijvoorbeeld iets op de grond (het "
                "stroomnet) en iets in de ruimte (satellieten en gps). In 1989 lag het stroomnet "
                "van Quebec er door een zonnestorm negen uur uit, en dat maakt het heel concreet.",
            ],
        ),
        dict(
            aanpak="Zet de planeten in twee groepen: de vier aardse planeten zijn klein en van "
                   "steen, de vier reuzen zijn groot en van gas of ijs. Vul de tabel dan per "
                   "planeet met haar ene opvallende kenmerk, want dat is waarop gevraagd wordt.",
            waarom=[
                "Let op het verschil tussen gasreus en ijsreus in de tabel: Jupiter en Saturnus "
                "bestaan vooral uit waterstof en helium, Uranus en Neptunus hebben meer water, "
                "methaan en ammoniak, en dat is de reden voor hun blauwe kleur.",
                None,
                "Dit is de belangrijkste vraag van het hoofdstuk: niet de afstand tot de zon "
                "beslist de temperatuur, maar de dampkring. Venus heeft bijna 470 graden door "
                "haar dikke CO2-atmosfeer, Mercurius zonder atmosfeer koelt 's nachts tot ver "
                "onder nul af.",
                None,
            ],
        ),
        dict(
            aanpak="Drie verzamelplaatsen, van dichtbij naar ver: de asteroïdengordel tussen "
                   "Mars en Jupiter, de Kuipergordel voorbij Neptunus, en de Oortwolk nog veel "
                   "verder als een bol rond het hele zonnestelsel.",
            waarom=[
                None,
                None,
                "Let op het verschil in vorm: de twee gordels zijn platte ringen in hetzelfde "
                "vlak als de planeten, de Oortwolk is een bol rondom. Daarom komen kometen uit "
                "de Oortwolk uit elke richting.",
                None,
                "Noem de drie voorwaarden, want de vraag test die definitie en niet je mening "
                "over Pluto. De derde voorwaarde is waar hij op valt: hij deelt zijn baan met "
                "veel andere lichamen van de Kuipergordel.",
                "De staart ontstaat dus pas in de buurt van de zon en wijst altijd van de zon "
                "weg, ook als de komeet al op de terugweg is. Hij wordt namelijk door de "
                "zonnewind weggeblazen en volgt niet de baan.",
            ],
        ),
        dict(
            aanpak="De orde van de acht planeten moet je uit het hoofd kennen. Een spreekwoordje "
                   "met de beginletters helpt: Mercurius, Venus, aarde, Mars, Jupiter, Saturnus, "
                   "Uranus, Neptunus. Pluto hoort er sinds 2006 niet meer bij.",
            waarom=[
                None,
                None,
                "Pluto staat tussen de keuzes en is geen planeet meer, dus is Neptunus de verste "
                "planeet. Dat Pluto soms verder en soms minder ver staat dan Neptunus, komt "
                "doordat zijn baan erg uitgerekt is.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-bewegingen-van-de-aarde-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee bewegingen, twee soorten gevolgen. Rotatie is het tollen om de eigen as "
                   "in één dag en verklaart alles wat met het verloop van een dag te maken heeft. "
                   "Revolutie is de omloop om de zon in een jaar en verklaart alles wat met het "
                   "jaar en de seizoenen te maken heeft.",
            waarom=[
                None,
                None,
                None,
                "De middernachtzon hoort bij de revolutie, want ze bestaat enkel in juni en niet "
                "in december. Alles wat van de periode van het jaar afhangt, komt van de omloop "
                "en de schuine as, niet van de rotatie.",
                "Het corioliseffect komt van de rotatie: omdat de aarde onder de bewegende lucht "
                "doordraait, lijkt die lucht af te buigen. Zonder rotatie zou wind recht van hoge "
                "naar lage druk waaien.",
                None,
                None,
                "Noem het kwart: een omloop duurt ongeveer 365 dagen en 6 uur, en vier keer zes "
                "uur is precies een dag. Daarom komt er elke vier jaar een dag bij, en daarom "
                "zijn de eeuwjaren nog eens een uitzondering, want een kwart is niet exact.",
            ],
        ),
        dict(
            aanpak="Vijftien graden lengte is één uur, want 360 graden in 24 uur. Reken dus het "
                   "verschil in graden uit, deel door 15, en tel dat op als je naar het oosten "
                   "gaat en af als je naar het westen gaat.",
            waarom=[
                "Reken na: van 15° naar 45° is 30 graden, gedeeld door 15 is 2 uur, en naar het "
                "oosten dus later: 16 uur.",
                "Reken na: 75 gedeeld door 15 is 5 uur, en west betekent dat de klok er achter "
                "staat. Zet het woord vroeger of later er altijd bij, want een getal alleen is "
                "het antwoord niet.",
                "Reken na: 5 uur verschil, en van west naar oost tel je op, dus 9 plus 5 is 14 "
                "uur. Dit is dezelfde oefening als de vorige, maar nu met de uren erbij.",
                "Waar. Naar het westen over de datumgrens zet je de kalender een dag vooruit, dus "
                "sla je een dag over; naar het oosten leef je dezelfde dag twee keer.",
                "Zonder die bochten zou bijvoorbeeld Kiribati in twee verschillende dagen liggen. "
                "Dat is niet enkel lastig voor de bewoners maar ook voor alles wat met datums "
                "werkt: scholen, vluchten, contracten.",
            ],
        ),
        dict(
            aanpak="Eén regel volstaat: op het noordelijk halfrond naar rechts, op het zuidelijk "
                   "halfrond naar links, en op de evenaar niets. De afwijking wordt sterker naar "
                   "de polen toe.",
            waarom=[
                "Daarom draait de lucht rond een lagedrukgebied bij ons tegen de klok in. Het "
                "corioliseffect buigt de instromende lucht naar rechts, zodat ze er in een spiraal "
                "rond komt te draaien.",
                "Op het zuidelijk halfrond draait een depressie dus net de andere kant op. Dat is "
                "geen uitzondering maar hetzelfde effect, gezien van de andere kant van de "
                "aardbol.",
                "Op de evenaar is de afwijking nul, en daarom ontstaat er nooit een orkaan "
                "vlak op de evenaar: zonder coriolis krijgt een storm geen draaiing.",
            ],
        ),
        dict(
            aanpak="Alles in deze reeks komt uit één feit: de aardas staat 23,5 graden schuin. "
                   "Daardoor valt het zonlicht in juni steiler op ons halfrond en in december "
                   "flauwer. De afstand tot de zon speelt bijna geen rol.",
            waarom=[
                "23,5 graden is ook de breedte van de keerkringen, en 90 min 23,5 is 66,5: de "
                "breedte van de poolcirkels. Met dat ene getal liggen alle grenzen op de kaart "
                "vast.",
                None,
                "Niet waar, en het is net omgekeerd: in juli staat de aarde het verst van de zon. "
                "Dat de seizoenen op het zuidelijk halfrond tegengesteld zijn, bewijst het ook, "
                "want de afstand is voor beide halfronden gelijk.",
                "Noem beide redenen: de hoogte van de zon en de lengte van de dag. De hoogte is "
                "de belangrijkste, want steil licht valt op een kleiner oppervlak en is dus "
                "krachtiger per vierkante meter.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Hoe verder van de evenaar, hoe groter het verschil tussen zomer en winter. "
                   "Op de evenaar zijn dag en nacht het hele jaar ongeveer gelijk; bij een "
                   "equinox is dat overal zo.",
            waarom=[
                "Let op c en d: bij een equinox is de dag overal ongeveer twaalf uur, en op de "
                "evenaar is dat elke dag van het jaar zo. Oslo is het tegendeel: daar zijn de "
                "uitersten het grootst.",
                "Precies daarom bestaat er op de evenaar geen zomer en winter in onze zin, maar "
                "wel een regen- en een droog seizoen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-atmosfeer-en-de-temperatuur-op-aarde-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier lagen van onder naar boven, en de temperatuur gaat er afwisselend omlaag "
                   "en omhoog: troposfeer koeler, stratosfeer warmer, mesosfeer koeler, "
                   "thermosfeer warmer. Hang aan elke laag één kenmerk: het weer, de ozonlaag, de "
                   "vallende sterren, het poollicht.",
            waarom=[
                "Merk op waarom de temperatuur in de stratosfeer stijgt: de ozonlaag zit daar en "
                "die neemt uv-straling op, dus wordt de lucht er van boven af opgewarmd.",
                "Een vliegtuig vliegt net boven de troposfeer, en dat is geen toeval: daar zit "
                "het weer niet meer en is de lucht rustig, dus minder turbulentie en minder "
                "brandstof.",
                None,
            ],
        ),
        dict(
            aanpak="Eén regel voor de hele reeks: per 100 meter hoogte 0,65 graden kouder. Deel "
                   "de hoogte door 100, vermenigvuldig met 0,65, en trek dat af als je omhoog "
                   "gaat of tel het op als je omlaag rekent.",
            waarom=[
                "Reken na: 2000 gedeeld door 100 is 20, en 20 maal 0,65 is 13. Dus 18 min 13 is "
                "5 graden.",
                "Let op de richting: je rekent naar beneden, dus tel je op. 3000 gedeeld door 100 "
                "maal 0,65 is 19,5, en min 4 plus 19,5 is 15,5 graden.",
                "Nu de omgekeerde bewerking: 10 gedeeld door 0,65 is ongeveer 15,4, en dat maal "
                "100 meter is ongeveer 1540 m.",
                "Schrijf de bewerking op zoals in het antwoord, en zet er de voorwaarde bij: als "
                "al de rest gelijk zou zijn. In de werkelijkheid spelen ook de zee, de wind en "
                "de ligging van de vallei mee.",
            ],
        ),
        dict(
            aanpak="Leer de vier cijfers van de samenstelling en onthoud dat ozon twee gezichten "
                   "heeft. Hoog in de stratosfeer beschermt het ons; vlak bij de grond is het "
                   "een vervuilende stof.",
            waarom=[
                "Zet de getallen naast elkaar: stikstof en zuurstof samen zijn al 99 procent. "
                "Alles waar het klimaat om draait, zit in de laatste procent, en CO2 is daarvan "
                "nog maar 0,04 procent.",
                "Dit is het klassieke paar: dezelfde stof, twee plaatsen, twee beoordelingen. "
                "Zomersmog met te veel ozon aan de grond heeft dus niets te maken met het gat in "
                "de ozonlaag.",
            ],
        ),
        dict(
            aanpak="Albedo is het deel van het zonlicht dat weerkaatst wordt. Licht en wit "
                   "weerkaatst veel, donker weinig. Zet de oppervlakken dus op kleur: sneeuw "
                   "bovenaan, water onderaan.",
            waarom=[
                "Dat de oceaan de laagste albedo heeft, is het punt dat telt voor het klimaat: "
                "smelt zee-ijs weg, dan komt er donker water in de plaats dat juist veel warmte "
                "opneemt.",
                "Een albedo van 0,8 betekent dat er 80 procent terugkaatst en dus 20 procent "
                "opgenomen wordt. Verse sneeuw zit rond die waarde, asfalt rond 0,1.",
            ],
        ),
        dict(
            aanpak="Vier factoren bepalen de temperatuur van een plaats: de breedte, de hoogte, "
                   "de afstand tot de zee en de wind. Zoek bij elk paar welke van die vier "
                   "verschilt, want de andere drie zijn in zo'n vergelijking opzettelijk gelijk "
                   "gehouden.",
            waarom=[
                "Let op b: in januari is de zee warmer dan het land, dus is de kust zachter. In "
                "juli is het omgekeerd, en dan is Luik warmer dan Oostende. De zee dempt dus "
                "beide uitersten.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Een klimatogram lees je in drie stappen: eerst de schommeling van de "
                   "temperatuur, dan welke maand de warmste is, en dan de neerslag. De warmste "
                   "maand verraadt het halfrond, de rest verraadt het klimaattype.",
            waarom=[
                None,
                "Dit is de snelste test op een klimatogram: ligt de warmte in juli, dan noordelijk "
                "halfrond; ligt ze in januari, dan zuidelijk.",
                "Alle aanwijzingen passen samen: een milde winter boven nul, een zachte zomer, "
                "een kleine schommeling van 16 graden en regen in elke maand. Dat is een "
                "gematigd zeeklimaat, zoals bij ons.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-luchtdruk-wind-en-de-grote-circulatie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Alles volgt uit één vraag: stijgt de lucht of daalt ze? Stijgende lucht koelt "
                   "af en geeft wolken, dus lage druk en slecht weer. Dalende lucht wordt warmer "
                   "en droger, dus hoge druk en helder weer.",
            waarom=[
                "Let op e en f: aan de grond stroomt de lucht naar een lagedrukgebied toe en uit "
                "een hogedrukgebied weg. Dat moet ook, want wat bij een laag opstijgt, moet van "
                "onderaf aangevuld worden.",
                "1013 hPa is het gemiddelde waartegen al de rest wordt afgemeten. Boven de 1020 "
                "spreekt men van hoge druk, onder de 1000 van een stevige depressie.",
                "Waar, en dat verrast soms. Hoge druk in de winter betekent een heldere nacht, "
                "dus sterke afkoeling: dat geeft mist of vrieskou in plaats van regen.",
                "Noem de hele keten: stijgen, afkoelen, condenseren, wolken. De middelste stap is "
                "de belangrijkste, want koude lucht kan minder waterdamp dragen dan warme.",
            ],
        ),
        dict(
            aanpak="Isobaren zijn de hoogtelijnen van de luchtdruk. Hoe dichter ze bij elkaar "
                   "liggen, hoe steiler het verschil en hoe harder de wind. Een weerkaart lees "
                   "je dus eerst op de afstand tussen de lijnen.",
            waarom=[
                None,
                "Vergelijk het met een helling: dicht bij elkaar liggende lijnen betekenen een "
                "steile helling en dus veel snelheid. Daarom kan je aan een weerkaart de "
                "windkracht zien nog voor je een cijfer leest.",
                "De drukgradiëntkracht zet de lucht in beweging, maar het corioliseffect buigt ze "
                "af. Daarom waait de wind niet recht naar het centrum van een depressie maar in "
                "een spiraal eromheen.",
            ],
        ),
        dict(
            aanpak="De drukgordels wisselen af van de evenaar naar de pool: laag aan de evenaar, "
                   "hoog rond 30 graden, laag rond 60 graden, hoog aan de pool. Onthoud dat "
                   "patroon van laag-hoog-laag-hoog en je kan het weer van elke breedte "
                   "voorspellen.",
            waarom=[
                "Merk op dat de twee lage gordels de natte zones zijn en de twee hoge de droge: "
                "regenwoud aan de evenaar, woestijn op 30 graden, wisselvallig weer op 60 graden, "
                "poolwoestijn aan de pool.",
                "Dit is de vraag die het verband legt. Noem de hele cel: opstijgen aan de "
                "evenaar, het vocht valt daar als regen, de droge lucht daalt op 30 graden en "
                "warmt op. Daarom liggen de Sahara, de Arabische en de Australische woestijn alle "
                "drie op dezelfde breedte.",
                "De ITCZ schuift met de zon mee naar het noorden en het zuiden, en dat is precies "
                "wat de regenseizoenen in de tropen maakt.",
            ],
        ),
        dict(
            aanpak="Twee soorten winden door elkaar: de vaste winden van de grote circulatie "
                   "(passaat, westenwind, straalstroom) en de plaatselijke winden die per dag "
                   "omkeren (zeewind, landwind). Een wind heet altijd naar de richting waaruit "
                   "hij komt.",
            waarom=[
                "Merk op dat de passaat uit het noordoosten komt terwijl hij naar de evenaar "
                "waait: het corioliseffect buigt hem af. Zonder die afbuiging zou hij recht uit "
                "het noorden komen.",
                None,
                "Noem beide helften van de dag, want het verschil in opwarmingssnelheid is de "
                "hele verklaring: land warmt sneller op en koelt sneller af dan water. Dezelfde "
                "oorzaak, twee richtingen.",
                "De moesson is in feite een zeewind op de schaal van een werelddeel: in de zomer "
                "warmt het Aziatische vasteland sterk op en zuigt het vochtige lucht van de "
                "oceaan aan.",
                "Waar, en het is het spiegelbeeld van de zomermoesson. Daarom is er in India een "
                "droog winterhalfjaar en valt bijna alle regen van het jaar in enkele maanden.",
            ],
        ),
        dict(
            aanpak="Een weerbericht ontleed je op drie dingen: de druk, de wind en de tijd van de "
                   "dag. Hier staan ze er alle drie in, en elk antwoord komt uit de leerstof van "
                   "de vorige reeksen.",
            waarom=[
                None,
                "Dit sluit aan bij de hoge druk: zonder wolkendek straalt de grond 's nachts zijn "
                "warmte weg, de lucht erboven koelt tot onder het dauwpunt en de damp slaat neer "
                "als mist.",
                "Noem beide: de richting en wat ze over de lucht zegt. Oostenwind brengt bij ons "
                "continentale lucht, dus droog, in de winter koud en in de zomer heet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-water-in-de-lucht-en-de-neerslag-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De kringloop van het water heeft vaste woorden, en elk woord hoort bij één "
                   "richting. Water gaat omhoog door verdamping en transpiratie, wordt wolk door "
                   "condensatie, en gaat op de grond ofwel de bodem in (infiltratie) ofwel "
                   "eroverheen weg (afstroming).",
            waarom=[
                "Let op het verschil tussen a en b: verdamping gebeurt van een oppervlak, "
                "transpiratie gaat door planten heen. Een bos verdampt daardoor veel meer water "
                "dan een meer van dezelfde oppervlakte.",
                None,
                "Noem alle drie de gevolgen: meer afstroming, snellere piek in de beek, en geen "
                "aanvulling van het grondwater. Juist dat laatste maakt verharding tegelijk een "
                "oorzaak van wateroverlast en van droogte.",
            ],
        ),
        dict(
            aanpak="Eén zin verklaart de hele reeks: warme lucht kan meer waterdamp dragen dan "
                   "koude. Koelt lucht af tot haar dauwpunt, dan moet de damp eruit, en dat geeft "
                   "wolken, mist, dauw of een beslagen ruit.",
            waarom=[
                "Het dauwpunt is dus geen eigenschap van het weer maar van die lucht zelf: hoe "
                "vochtiger de lucht, hoe hoger haar dauwpunt en hoe sneller ze bij afkoeling "
                "condenseert.",
                None,
                "Zonder condensatiekernen zou de damp niet samenklonteren, ook niet onder het "
                "dauwpunt. Daarom zie je boven een vervuilde stad soms meer wolken, en daarom "
                "werkt het bezaaien van wolken met zoutdeeltjes soms.",
                "Vier wolken, drie hoogten: cirrus hoog, cumulus en stratus laag, cumulonimbus "
                "van beneden tot boven. Nimbus in de naam betekent altijd dat er neerslag uit "
                "valt.",
                "Dit is dezelfde natuurwet als bij mist, maar in je eigen badkamer. Noem de drie "
                "stappen: warme vochtige lucht, een koud oppervlak, afkoeling tot onder het "
                "dauwpunt.",
            ],
        ),
        dict(
            aanpak="Houd de ene regel vast: 1 mm neerslag is 1 liter per vierkante meter. Van "
                   "millimeter naar liter vermenigvuldig je met de oppervlakte, van liter naar "
                   "millimeter deel je erdoor.",
            waarom=[
                "Reken na: 18 maal 60 is 1080 liter. Dat is meer dan vijf regentonnen uit één "
                "bui, en zo zie je waarom een dak zo'n verschil maakt bij wateroverlast.",
                "Nu de omgekeerde bewerking: 300 gedeeld door 25 is 12 mm. Een bui van 12 mm is "
                "niets bijzonders, dus zo'n ton loopt meermaals per jaar over.",
                "Reken na: 780 gedeeld door 12 is 65 mm per maand. Dat is wel een gemiddelde: in "
                "ons klimaat valt er in de winter meer dan in de lente.",
                "Niet waar. Een regenmeter moet vrij staan, op ongeveer een meter hoogte en ver "
                "van muren en bomen, want die vangen regen weg of leiden hem net naar de meter "
                "toe. Een meting tegen een muur is onbruikbaar.",
            ],
        ),
        dict(
            aanpak="Drie soorten regen, en het verschil zit in wat de lucht omhoog duwt: een "
                   "gebergte, de warmte van de grond, of een front. Zoek in de situatie dus "
                   "steeds de oorzaak van het opstijgen.",
            waarom=[
                "Stuwingsregen en regenschaduw horen bij elkaar: aan de windzijde regent het "
                "veel, en de lucht die over de top gaat, is haar vocht kwijt en daalt warm en "
                "droog aan de andere kant.",
                None,
                "Dit is dezelfde regel als bij een koude zeestroom in het algemeen: koude lucht "
                "boven koud water stijgt niet op, dus is er mist en geen regen. In sommige delen "
                "van de Atacama is in jaren geen neerslag gemeten.",
            ],
        ),
        dict(
            aanpak="Dezelfde rekenregel als bij de regenmeter, nu voor een echt huis: millimeter "
                   "maal vierkante meter geeft liter. Houd het dakoppervlak van 90 m² bij elke "
                   "vraag vast, en reken op het einde hoe vaak de put daarmee vol zou gaan.",
            waarom=[
                "Reken na: 12 maal 90 is 1080 liter uit één gewone bui.",
                "Reken na: 800 maal 90 is 72 000 liter per jaar. Dat is ongeveer evenveel als "
                "wat een gezin van vier in een jaar aan drinkwater gebruikt.",
                "Reken na: 72 000 gedeeld door 5000 is 14,4, dus ongeveer veertien keer. Dat lijkt "
                "veel, maar het water komt niet gelijkmatig: in een natte week loopt de put over "
                "en in een droge zomer staat hij leeg.",
                "Dit is de les van de hele reeks, en het antwoord op de vorige vraag hoort erin: "
                "wat je kan opvangen hangt af van het dak, en wat je kan gebruiken van je "
                "verbruik. Een put groter dan die twee heeft geen zin.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-klimaten-biomen-en-zeestromen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Één vraag beslist: gaat het over één moment of over een gemiddelde van jaren? "
                   "Weer is wat er nu of morgen gebeurt, klimaat is het gemiddelde over dertig "
                   "jaar. Het woord gemiddeld in een zin is bijna altijd het teken van klimaat.",
            waarom=[
                None,
                None,
                "Ook drie dagen regen blijft weer. Dat is de klassieke valkuil: lang weer wordt "
                "geen klimaat, en één koude winter zegt niets over de opwarming.",
                "Die periode van dertig jaar is internationaal afgesproken, net om te vermijden "
                "dat een paar bijzondere jaren het beeld bepalen.",
            ],
        ),
        dict(
            aanpak="Een bioom volgt uit twee gegevens: de temperatuur en de neerslag. Bij elk "
                   "bioom hoort een aanpassing van de planten, en daar vraagt de tabel naar: "
                   "bladverlies bij droogte, kleine leerachtige blaadjes aan de Middellandse Zee, "
                   "naalden bij kou, mossen in de kou en de wind.",
            waarom=[
                "Merk op dat de aanpassing telkens hetzelfde doel heeft: water vasthouden of kou "
                "overleven. Een naald verliest minder water dan een blad, en een vetplant slaat "
                "water op in haar stam.",
                "Noem beide redenen: het korte, koude groeiseizoen én de permafrost. Een boom "
                "heeft diepe wortels nodig en die kunnen in bevroren grond niet, en net daar ligt "
                "de boomgrens.",
                "Dat ons bioom gematigd loofbos is, zie je nog in de namen van de bossen: beuk, "
                "eik en haagbeuk. Dat er nu akkers en steden staan, verandert het klimaat niet "
                "en dus het bioom niet.",
            ],
        ),
        dict(
            aanpak="Een warme zeestroom brengt zachte, vochtige lucht; een koude stroom brengt "
                   "droogte en mist. Zoek bij elke kust dus eerst of de stroom van de evenaar of "
                   "van de pool komt, want dat beslist het klimaat van die kust.",
            waarom=[
                "Let op het verschil tussen mist en regen bij b en c. Boven koud water wordt de "
                "lucht onderaan afgekoeld, dus ontstaat er mist, maar ze stijgt niet op, en "
                "zonder opstijgen is er geen regen. Daarom reikt de Namibwoestijn tot aan het "
                "strand.",
                "Reken het verschil na: Bergen ligt vijftien breedtegraden noordelijker dan "
                "Montreal en is in januari toch zachter. Dat is het sterkste bewijs dat breedte "
                "alleen een klimaat niet verklaart.",
            ],
        ),
        dict(
            aanpak="De naam zegt de twee motoren: thermo voor warmte en halien voor zout. Koud "
                   "en zout water is zwaar en zinkt, en dat zinken trekt de hele lopende band op "
                   "gang. Elke vraag van deze reeks gaat terug op dat ene punt.",
            waarom=[
                None,
                "Dat het water juist daar zinkt, komt doordat het er zowel koud als extra zout "
                "is: bij het bevriezen van zee-ijs blijft het zout in het water achter.",
                "Niet waar, en dat is net de reden dat deze circulatie in het nieuws komt. Ze "
                "brengt warm water naar het noordoosten van de Atlantische Oceaan; valt ze weg, "
                "dan worden onze winters juist veel kouder, terwijl de aarde als geheel opwarmt.",
            ],
        ),
        dict(
            aanpak="Zoek elke plaats in de atlas en lees eerst de breedte af, dan de ligging ten "
                   "opzichte van de zee. Met die twee gegevens en de klimaatgordels uit de "
                   "leerstof kan je het klimaat en het bioom er zelf bij zetten.",
            waarom=[
                "Zet de drie naast elkaar en je ziet de gordels op een rij: Caïro in de droge "
                "gordel rond 30 graden, Rome in de mediterrane zone met een droge zomer, Tromsø "
                "ver in het noorden maar door de zeestroom nog zacht voor zijn breedte.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-bouw-van-de-aarde-en-de-platentektoniek-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Er lopen twee indelingen van de aarde door elkaar, en dat is net wat deze "
                   "reeks test. Korst, mantel en kern gaan over waaruit het gesteente bestaat; "
                   "lithosfeer en asthenosfeer gaan over of het stijf is of kneedbaar. Vraag je "
                   "dus: gaat het over de stof of over het gedrag?",
            waarom=[
                "De lithosfeer is korst plus het bovenste stijve stuk mantel, dus ze loopt dwars "
                "door de chemische indeling heen. Precies daarom kan je niet uit de dikte van de "
                "korst afleiden hoe diep de lithosfeer gaat.",
                None,
                None,
                "6371 km is de straal van de aarde, en dus ook de afstand van het oppervlak tot "
                "het middelpunt. De diepste boring ooit haalde nog geen 13 km, dus is bijna alles "
                "wat we weten onrechtstreeks gemeten.",
            ],
        ),
        dict(
            aanpak="De twee soorten korst verschillen op vier punten: dikte, gesteente, "
                   "dichtheid en leeftijd. Onthoud één koppel en de rest volgt: oceanische korst "
                   "is dun maar zwaar, continentale korst is dik maar licht.",
            waarom=[
                "Let erop dat het bij subductie om dichtheid gaat en niet om dikte. De oceanische "
                "korst is veel dunner en duikt toch weg, juist omdat ze zwaarder is per kubieke "
                "centimeter.",
                "Oceaanbodem wordt aan een rug gemaakt en aan een trog weer opgeruimd, dus is de "
                "oudste maar ongeveer 200 miljoen jaar oud. Continentale korst wordt nooit "
                "opgeruimd en haalt bijna vier miljard jaar.",
            ],
        ),
        dict(
            aanpak="Elk bewijs van Wegener volgt hetzelfde patroon: iets dat vandaag ver van "
                   "elkaar ligt, hoort bij elkaar. Zeg dus niet enkel dat de continenten bewogen "
                   "zijn, maar wat precies ooit één geheel was: één kust, één leefgebied, één "
                   "gebergte, één ijskap.",
            waarom=[
                "Het sterkste bewijs is d, want gletsjerkrassen in de huidige tropen kunnen "
                "onmogelijk ter plaatse ontstaan zijn. Dat sluit elke andere verklaring uit.",
                "Wegener werd lang niet geloofd omdat hij geen kracht kon aanwijzen die "
                "continenten voortduwt. Pas met de ontdekking van de mid-oceanische ruggen was "
                "er een motor voor zijn idee.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke plaatrand twee dingen: bewegen de platen naar elkaar toe, "
                   "van elkaar weg of langs elkaar, en wat voor korst botst er. Naar elkaar toe "
                   "met oceanische korst geeft een trog en vulkanen; twee continenten geven een "
                   "plooiingsgebergte zonder vulkanen; langs elkaar geeft enkel bevingen.",
            waarom=[
                "Let op het verschil tussen de Andes en de Himalaya in de tabel. Bij de Andes "
                "duikt oceanische korst weg en smelt ze, dus zijn er vulkanen; bij de Himalaya "
                "botsen twee continenten die beide te licht zijn om te zakken, dus wordt het "
                "gesteente enkel opgeplooid.",
                None,
                None,
                "Een rift is het begin van een nieuwe oceaan: de Rode Zee was vijftien miljoen "
                "jaar geleden ook nog zo'n slenk.",
            ],
        ),
        dict(
            aanpak="Drie krachten, en ze werken samen op dezelfde plaat. Convectie is de motor "
                   "diep in de mantel, ridge push duwt vanaf de rug, slab pull trekt aan de kant "
                   "waar de plaat wegzakt. Slab pull is de sterkste van de drie.",
            waarom=[
                None,
                "Dat lijkt weinig, maar het is ongeveer even snel als je nagels groeien. Juist "
                "omdat het zo traag gaat, kan je het niet voelen en wel meten met gps.",
                "Reken na: 5 cm per jaar maal een miljoen jaar is 5 miljoen cm, en dat is 50 km. "
                "Zo opent een trage beweging over geologische tijd een hele oceaan.",
            ],
        ),
        dict(
            aanpak="Zoek elke plaats in de atlas en kijk wat er in de buurt getekend staat: een "
                   "rug betekent divergent, een trog of een bergketen convergent, een lange "
                   "breuk zonder beide transform.",
            waarom=[
                "IJsland is het bijzondere geval: daar komt een mid-oceanische rug boven water, "
                "en daarom kan je er de spreiding van de oceaanbodem op het droge zien, met "
                "scheuren en vulkanen erbij.",
                "Daarom kon men de platen in kaart brengen nog voor men hun beweging kon meten: "
                "de bevingen en de vulkanen tekenden de randen zelf uit.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vulkanen-en-aardbevingen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de twee punten uit elkaar: het hypocentrum zit in de diepte, waar de "
                   "breuk echt begint, en het epicentrum ligt er recht boven, aan het oppervlak. "
                   "Het epicentrum is dus een plaats op de kaart, het hypocentrum een plaats in "
                   "de aarde.",
            waarom=[
                None,
                None,
                "Niet waar, en let op de richting. Hoe dieper de haard, hoe meer gesteente de "
                "golven moeten doorkruisen en hoe meer energie onderweg verloren gaat. Een "
                "ondiepe beving van magnitude 6 doet meer schade dan een diepe van 7.",
                "Een seismograaf meet twee aankomsten: eerst de snelle P-golf, dan de S-golf. Uit "
                "het tijdsverschil ertussen leidt men af hoe ver de beving was.",
            ],
        ),
        dict(
            aanpak="Magnitude is één getal voor de beving zelf, gemeten aan de vrijgekomen "
                   "energie; intensiteit is wat mensen ter plaatse ondervinden en verschilt dus "
                   "van dorp tot dorp. Eén beving heeft één magnitude en tientallen "
                   "intensiteiten.",
            waarom=[
                None,
                "De schaal is logaritmisch: één punt hoger is ongeveer 32 keer zoveel energie. "
                "Daarom lijkt het verschil tussen een 5 en een 6 in het nieuws klein en is het in "
                "werkelijkheid enorm.",
                "Reken na: 32 maal 32 is ongeveer 1000. Twee punten hoger is dus duizend keer "
                "zoveel energie.",
                "Een tsunami is geen hoge golf op zee maar een heel lange golf die pas bij de "
                "kust oprijst. Daarom merken schepen op volle zee er nauwelijks iets van.",
            ],
        ),
        dict(
            aanpak="Volg de weg van het gesteente van onder naar boven: magmahaard, schoorsteen, "
                   "krater. En onthoud het ene woordverschil dat vaak gevraagd wordt: onder de "
                   "grond heet het magma, boven de grond lava.",
            waarom=[
                "Dezelfde stof, twee namen, en het verschil zit enkel in waar ze is. Bij het "
                "buitenkomen ontsnappen de gassen, en net daardoor gedraagt lava zich anders dan "
                "magma.",
                "Een caldera ontstaat als de magmahaard leegloopt en het dak erboven inzakt. "
                "Daarom is een caldera veel breder dan een krater: de baai van Santorini is er "
                "een van.",
            ],
        ),
        dict(
            aanpak="Alles bij een vulkaan volgt uit één eigenschap: hoe taai de lava is. Taaie, "
                   "kiezelrijke lava geeft een steile kegel en een explosie; vloeibare lava geeft "
                   "een vlak schild en een stroom. Begin bij de lava en de rest van de tabel "
                   "volgt.",
            waarom=[
                "Merk op dat de vorm van de berg uit de lava volgt en niet omgekeerd. Taaie lava "
                "stapelt zich op bij de krater, dus steil; vloeibare lava loopt kilometers ver "
                "uit, dus vlak zoals op Hawaï. En de taaie lava houdt de gassen vast tot de prop "
                "openbarst, en dat maakt de explosie.",
                "Een pyroclastische stroom is de dodelijkste van de drie: hij gaat honderden "
                "kilometer per uur en is honderden graden warm. Een lahar kan jaren na de "
                "uitbarsting nog komen, want hij heeft enkel as en water nodig.",
            ],
        ),
        dict(
            aanpak="Twee open vragen die naar een afweging vragen. Zet bij de eerste naast de "
                   "voordelen van de grond ook het menselijke: het is hun thuis. Geef bij de "
                   "tweede maatregelen die echt uitvoerbaar zijn, van meten tot evacueren.",
            waarom=[
                "Noem er drie van verschillende soort: iets over de bodem, iets over geld, en het "
                "feit dat mensen niet zomaar verhuizen uit het dorp van hun familie. Net die "
                "laatste reden wordt vaak vergeten en is in werkelijkheid de belangrijkste.",
                "Twee volstaan, maar laat zien dat er een keten is: eerst meten, dan waarschuwen, "
                "dan evacueren. Een meetnet zonder evacuatieplan redt niemand.",
            ],
        ),
        dict(
            aanpak="Bij elk advies hoort één reden, en die reden is altijd hetzelfde soort "
                   "vraag: wat valt er op je, waar kan je vast raken, en wat komt er na de "
                   "beving. Schrijf dus niet enkel goed of fout maar ook waarom.",
            waarom=[
                "Let op c: in een deuropening gaan staan is een oud advies uit de tijd van "
                "lemen huizen, en het klopt niet meer voor moderne gebouwen. Het hedendaagse "
                "advies is bukken, dekking zoeken en vasthouden, en d hoort daar achteraan bij, "
                "want een tsunami komt pas na de beving.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gesteenten-en-de-geologische-tijd-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk gesteente hoe het gemaakt is. Uit magma dat stolt is "
                   "magmatisch, uit lagen die bezinken sedimentair, uit een gesteente dat onder "
                   "druk en hitte veranderd is metamorf. De uitgang van de naam helpt niet, dus "
                   "leer de voorbeelden per groep.",
            waarom=[
                "Graniet en basalt zijn de twee magmatische voorbeelden die altijd terugkomen, "
                "kalksteen en zandsteen de twee sedimentaire, marmer en leisteen de twee "
                "metamorfe. Met die zes namen geraak je door bijna elke vraag.",
                "Steenkool is de verrassing in de rij: het lijkt geen gesteente, maar het is "
                "ontstaan uit plantenresten die laag na laag bezonken en samengedrukt werden, en "
                "dus sedimentair.",
                "Lagen zie je van op een afstand, in een steengroeve of in een berm. Fossielen "
                "komen enkel in sedimentair gesteente voor, want in magma dat stolt blijft niets "
                "bewaard.",
            ],
        ),
        dict(
            aanpak="Eén regel beslist de korrelgrootte: hoe trager de afkoeling, hoe groter de "
                   "kristallen. Dieptegesteente koelt traag af en is grof; uitvloeiingsgesteente "
                   "koelt snel af en is fijn.",
            waarom=[
                "Graniet en basalt komen uit dezelfde soort magma en zien er toch heel anders "
                "uit. Dat is de hele les: niet de stof maar de tijd bepaalt de korrel.",
            ],
        ),
        dict(
            aanpak="Vier koppels om te kennen: kalksteen wordt marmer, klei wordt leisteen, "
                   "zandsteen wordt kwartsiet, graniet wordt gneis. Het gesteente wordt harder en "
                   "dichter, maar het smelt niet.",
            waarom=[
                None,
                "Noem beide: druk alleen of hitte alleen is niet genoeg. Daarom vind je metamorfe "
                "gesteenten vooral in gebergten en bij een contact met magma.",
                "Niet waar, en dat is net het verschil met een magmatisch gesteente. Bij "
                "metamorfose blijft het gesteente vast en groeien de kristallen in vaste toestand "
                "om. Zou het smelten, dan kreeg je magma en nadien een magmatisch gesteente.",
            ],
        ),
        dict(
            aanpak="Relatieve datering is logica, geen meting: wat erbovenop ligt is jonger, en "
                   "wat ergens dwars door gaat is jonger dan wat het doorsnijdt. Een gidsfossiel "
                   "laat je dan lagen op verschillende plaatsen met elkaar vergelijken.",
            waarom=[
                None,
                "Let op beide helften van het antwoord. Kort geleefd maakt het fossiel precies in "
                "de tijd, wijd verspreid maakt het bruikbaar om ver van elkaar liggende lagen aan "
                "elkaar te koppelen.",
            ],
        ),
        dict(
            aanpak="Een halveringstijd is de tijd waarin de helft overblijft. Reken dus in "
                   "stappen van een halvering: na één de helft, na twee een kwart, na drie een "
                   "achtste. En kies de methode naar de ouderdom die je verwacht: koolstof-14 "
                   "voor duizenden jaren, uranium-lood voor miljoenen.",
            waarom=[
                None,
                "Reken na: 2 maal 5730 is 11 460 jaar, want een kwart is twee halveringen. Dat is "
                "ook ongeveer waar de methode haar nauwkeurigheid begint te verliezen.",
                "Twee redenen tegelijk: graniet heeft nooit geleefd en bevat dus geen koolstof-14, "
                "en 300 miljoen jaar is hoe dan ook duizenden halveringstijden. Koolstof-14 werkt "
                "enkel op wat ooit leefde en op hoogstens enkele tienduizenden jaren.",
                None,
                "66 miljoen jaar is de grens tussen het Mesozoïcum en het Cenozoïcum, en dat is "
                "geen toeval: die uitstervingsgolf maakte plaats voor de zoogdieren.",
            ],
        ),
        dict(
            aanpak="Elk gebruik volgt uit een eigenschap van het gesteente: hard voor een vloer "
                   "of een gevel, splijtbaar voor dakleien, kneedbaar voor baksteen, kalkrijk voor "
                   "cement. Denk dus niet aan de naam maar aan wat je met die steen kan doen.",
            waarom=[
                "Merk op dat leisteen juist gekozen wordt omdat het in dunne platen splijt, en "
                "klei omdat het te vormen en te bakken is. De eigenschap die een gesteente in de "
                "natuur kreeg, beslist waarvoor de mens het gebruikt.",
                "De steenkoolmijnen van Beringen, Zolder, Houthalen, Zwartberg, Winterslag, "
                "Waterschei en Eisden hebben de Kempen in de twintigste eeuw gemaakt tot wat ze "
                "zijn; de laatste mijn sloot in 1992.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verwering-en-massatransport-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie woorden, drie plaatsen in de keten. Verwering gebeurt ter plaatse en "
                   "maakt het gesteente stuk, erosie voert het weg, sedimentatie legt het elders "
                   "neer. Vraag je dus: blijft het liggen, gaat het mee, of wordt het afgezet?",
            waarom=[
                "Let op het verschil tussen c en d bij de wind. Blaast de wind korrels tegen een "
                "rots, dan is dat erosie, want het zijn meegevoerde korrels die het werk doen. "
                "Wortels en vorst zijn verwering, want daar beweegt niets weg.",
                "Één zin volstaat, maar zet er het woord in dat het verschil maakt: ter plaatse "
                "tegenover afvoeren.",
            ],
        ),
        dict(
            aanpak="Mechanisch is breken door een kracht, chemisch is veranderen van stof, "
                   "biologisch is het werk van een levend wezen. Kijk bij elke zin naar wat er "
                   "met het gesteente gebeurt: barst het, of lost het op?",
            waarom=[
                "Vorst en zoutkristallen werken allebei met uitzetten in een spleet: het ijs of "
                "het kristal groeit en duwt de rots verder open. Roest is chemisch, want het "
                "ijzer zelf verandert in een andere stof.",
            ],
        ),
        dict(
            aanpak="Karst is één verhaal: zuur regenwater lost kalksteen op. Alles wat je ziet "
                   "volgt daaruit, zowel wat wegvalt aan het oppervlak als wat neerslaat in een "
                   "grot. Houd stalactiet en stalagmiet uit elkaar met de letter: de t van top "
                   "hangt, de g van grond groeit omhoog.",
            waarom=[
                None,
                "Regenwater neemt koolstofdioxide op uit de lucht en uit de bodem en wordt "
                "daardoor een zwak zuur. Gewoon regenwater tast kalksteen dus aan, zonder dat er "
                "iets vervuild is.",
                "Merk op dat een stalactiet en een stalagmiet precies het omgekeerde zijn van het "
                "oplossen: het water laat de kalk die het hogerop opnam hier weer achter.",
            ],
        ),
        dict(
            aanpak="Zet de vier vormen op een lijn van traag naar snel: bodemkruip, "
                   "aardverschuiving, steenval, modderstroom. Het water beslist meestal de "
                   "snelheid, en de zwaartekracht doet altijd het werk.",
            waarom=[
                "Bodemkruip is de enige die je niet ziet gebeuren en wel ziet aan het gevolg: "
                "scheefgezakte muurtjes en gebogen boomstammen op een helling.",
                "Noem er vier van verschillende soort: de helling zelf, het water, het verdwijnen "
                "van de wortels, en een trilling of een ingreep van mensen. Het water is de "
                "belangrijkste, want het maakt de grond zwaarder en smeert tegelijk het glijvlak.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke ingreep of ze de helling vasthoudt of belast. Draineren, "
                   "terrassen en netten houden vast; afgraven aan de voet, kaalkappen en zwaar "
                   "bouwen bovenaan belasten. Water en gewicht zijn de twee sleutelwoorden.",
            waarom=[
                "Merk op dat c en f elkaars spiegelbeeld zijn: onderaan steun weghalen of "
                "bovenaan gewicht bijzetten geeft hetzelfde gevolg, want beide maken de helling "
                "steiler en zwaarder dan ze kan dragen.",
            ],
        ),
        dict(
            aanpak="Deze reeks brengt de leerstof naar je eigen straat. Zoek bij elk voorbeeld "
                   "weer dezelfde drie soorten: breekt er iets door een kracht, verandert er een "
                   "stof, of is er een levend wezen aan het werk?",
            waarom=[
                "De grafsteen is het mooiste voorbeeld, want je kan er de snelheid aan zien: "
                "letters in kalksteen uit de negentiende eeuw zijn vaak al onleesbaar, terwijl "
                "dezelfde letters in graniet nog scherp staan.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-erosie-door-water-ijs-en-wind-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een stroombekken is alles wat naar dezelfde rivier afwatert, en de grens "
                   "ervan loopt over de hoogste lijn in het landschap. Debiet is een hoeveelheid "
                   "per tijd, dus reken je het om door met de tijd te vermenigvuldigen.",
            waarom=[
                None,
                "De waterscheiding volgt de toppen, dus op een kaart met hoogtelijnen kan je ze "
                "zelf tekenen: van top naar top.",
                None,
                "Reken na: 45 maal 60 is 2700 m³ per minuut. Dat is meer dan een olympisch "
                "zwembad per minuut, en zo wordt een debietcijfer ineens voorstelbaar.",
            ],
        ),
        dict(
            aanpak="Een rivier doet in haar drie delen iets anders: bovenaan erodeert ze, in het "
                   "midden vervoert en slingert ze, onderaan zet ze af. Het verval beslist alles, "
                   "en de vorm van de vallei verraadt waar je bent.",
            waarom=[
                "Let op de vorm van de vallei, want dat is het snelste kenmerk: een V bovenaan, "
                "een brede vlakte in het midden en beneden. Grote keien horen bij veel kracht, "
                "fijn slib bij weinig.",
            ],
        ),
        dict(
            aanpak="In een bocht loopt het water aan de buitenkant sneller en aan de binnenkant "
                   "trager. Snel water erodeert, traag water zet af. Daarmee verklaar je de "
                   "steile oever, de zandbank en waarom een meander altijd breder wordt.",
            waarom=[
                "Dit is de motor achter een meander: de buitenbocht schuift op en de binnenbocht "
                "groeit aan, dus wordt de bocht elk jaar scherper tot ze zichzelf afsnijdt.",
                "Een hoefijzermeer is dus het einde van een meander, en het bewijs dat een rivier "
                "van loop verandert. In de vallei van de Maas liggen er verschillende.",
                "Differentiële erosie verklaart ook een waterval: de harde laag blijft staan, het "
                "zachtere gesteente erachter slijt weg, en zo ontstaat een trap.",
            ],
        ),
        dict(
            aanpak="Elke kracht laat haar eigen spoor na. IJs geeft een U-vorm en ongesorteerd "
                   "puin, water sorteert op grootte, wind laat enkel het fijnste liggen. Een "
                   "U-vormige en een V-vormige vallei zijn het snelste onderscheid tussen ijs en "
                   "water.",
            waarom=[
                "Let op het woord ongesorteerd bij de morene: een gletsjer duwt alles door elkaar "
                "vooruit, van stof tot keien, terwijl stromend water altijd sorteert. Löss is het "
                "fijnste van al, door de wind over honderden kilometers aangevoerd, en het is de "
                "reden dat Haspengouw zulke vruchtbare grond heeft.",
                "Een fjord toont twee dingen tegelijk: een gletsjer sneed de vallei uit tot onder "
                "het huidige zeeniveau, en nadien steeg de zee en liep ze onder.",
            ],
        ),
        dict(
            aanpak="Twee lijstjes die elkaars spiegelbeeld zijn. Alles wat het water sneller doet "
                   "wegstromen vergroot de kans op een overstroming; alles wat het water ruimte "
                   "of tijd geeft verkleint ze. Houd dat ene criterium vast en je vindt zelf nog "
                   "voorbeelden.",
            waarom=[
                "Noem er drie van verschillende soort: iets over de bodem, iets over de rivier "
                "zelf en iets over waar men bouwt. Verharden is het sterkste voorbeeld, want "
                "regen die niet in de grond kan, komt binnen het uur in de beek.",
                "Merk op dat deze lijst gewoon het omgekeerde is van de vorige. Dat is geen "
                "toeval: veel van het huidige waterbeleid bestaat erin de ingrepen van de vorige "
                "eeuw terug te draaien.",
                "Het winterbed hoort bij de rivier, ook als het jaren droog blijft. Daarop bouwen "
                "betekent dat het water zijn ruimte ergens anders zoekt, meestal bij de buren "
                "stroomafwaarts.",
            ],
        ),
        dict(
            aanpak="Zoek de twee rivieren in de atlas en volg ze van bron naar monding. Let bij "
                   "de monding op het verschil tussen een delta en een estuarium: een delta "
                   "splitst zich in armen, een estuarium is één brede trechter waar de zee "
                   "binnendringt.",
            waarom=[
                "De Maas ontspringt in Frankrijk, stroomt door België en Nederland en mondt daar "
                "samen met de Rijn uit. Een rivier die drie landen doorkruist, betekent ook dat "
                "ze over de grenzen heen beheerd moet worden.",
                None,
                None,
                "Noem beide redenen: het kleine verval en de brede, diepe monding. Juist omdat de "
                "vloed tot in Antwerpen komt, kunnen zeeschepen er aanmeren, en juist daarom zijn "
                "er ook stormvloedkeringen en overstromingsgebieden nodig.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-huidige-klimaatverandering-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de twee getallen naast elkaar: zonder broeikaseffect ongeveer 18 graden "
                   "onder nul, met broeikaseffect ongeveer 15 graden boven nul. Het natuurlijke "
                   "broeikaseffect maakt de aarde dus bewoonbaar; de vraag is enkel hoeveel we er "
                   "zelf bij doen.",
            waarom=[
                "Reken het verschil na: dat is ongeveer 33 graden die het broeikaseffect "
                "oplevert. Daarom is het broeikaseffect zelf niets slechts.",
                None,
                "Stikstof is de valkuil: het maakt bijna vier vijfde van de lucht uit en is toch "
                "geen broeikasgas. Een gas houdt enkel warmte tegen als het molecule uit "
                "verschillende atomen bestaat en kan buigen of trillen.",
                "Drie zinnen volstaan, maar laat alle drie de stappen erin staan: zonlicht komt "
                "binnen, de aarde straalt infrarood terug, de gassen houden dat tegen. Zonder de "
                "middelste stap klopt de uitleg niet, want de gassen houden het zonlicht zelf "
                "niet tegen.",
            ],
        ),
        dict(
            aanpak="Een reeks met vaste cijfers. Leer er drie: ongeveer 1,1 tot 1,2 graden "
                   "opwarming sinds 1850-1900, ongeveer 20 cm zeespiegelstijging sinds 1900, en "
                   "een oceaan die verzuurt. Rond gerust af, maar ken de orde van grootte.",
            waarom=[
                "Let op het vergelijkingspunt: sinds 1850-1900, de tijd voor de industrie op "
                "volle kracht kwam. Een opwarmingscijfer zonder vertrekpunt zegt niets.",
                None,
                "Verzuren is het minst bekende gevolg en hoort nochtans bij hetzelfde CO2: een "
                "deel ervan lost op in zeewater en vormt daar een zuur, dat de schelpen en de "
                "koralen aantast.",
                "Noem beide redenen, en vergeet de tweede niet: ook zonder één druppel smeltwater "
                "zou de zee stijgen, omdat warmer water uitzet. Die uitzetting levert ongeveer de "
                "helft van de stijging.",
            ],
        ),
        dict(
            aanpak="Elke waarneming in deze reeks is een vingerafdruk: ze past bij broeikasgassen "
                   "en niet bij een sterkere zon. Vraag je bij elk punt dus niet of het warmer "
                   "wordt, maar wat het uitsluit.",
            waarom=[
                "Het sterkste paar is b en c. Een sterkere zon zou de hele atmosfeer opwarmen en "
                "vooral de dagen; broeikasgassen warmen de onderste lucht op terwijl de hoge "
                "lucht afkoelt, en houden vooral de nachten warm. Dat is het verschil tussen een "
                "sterkere kachel en een dikkere deken.",
            ],
        ),
        dict(
            aanpak="Mitigatie bestrijdt de oorzaak, adaptatie vangt de gevolgen op. Vraag je bij "
                   "elke maatregel of ze de uitstoot verlaagt of ons wapent tegen wat al "
                   "onderweg is. Beide zijn nodig; het is geen keuze tussen de twee.",
            waarom=[
                "Merk op dat je de twee niet aan het soort maatregel ziet maar aan het doel. Een "
                "boom planten kan allebei zijn: voor de koolstof is het mitigatie, voor de "
                "schaduw in de stad adaptatie.",
                None,
                "Noem beide kanten: wie het minst heeft uitgestoten wordt het hardst getroffen, "
                "en de generaties die nog moeten komen hebben niets beslist. Daarom staat er in "
                "het Akkoord van Parijs ook geld voor de armere landen, en niet enkel een "
                "temperatuurdoel.",
            ],
        ),
        dict(
            aanpak="Zet de keuzes op grootte en niet op gevoel. Vliegen weegt het zwaarst, dan "
                   "de auto, dan het dagelijkse rundvlees; de bus is al veel lichter en de fiets "
                   "bijna niets. Een verre vlucht alleen kost meer dan een heel jaar naar school "
                   "rijden.",
            waarom=[
                "De sprongen zijn groter dan ze lijken: één verre vlucht heen en terug zit in de "
                "orde van een ton CO2 per persoon, en dat haal je met de bus of de fiets in geen "
                "jaren.",
                "Hier is er geen juist antwoord, en dat is bewust: de vraag test of je het effect "
                "afweegt tegen wat haalbaar is. Zet in je antwoord dus zowel de grootte van de "
                "winst als de reden waarom jij het volhoudt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verstedelijking-en-het-ruimtelijk-beleid-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De vier fasen volgen elkaar op in de tijd en je herkent ze aan de richting "
                   "van de verhuis. Naar de stad is urbanisatie, naar de rand suburbanisatie, "
                   "weg van de stad met de bedrijven erbij desurbanisatie, en terug naar het "
                   "centrum reurbanisatie.",
            waarom=[
                "Let op het verschil tussen b en c: bij suburbanisatie verhuizen de mensen maar "
                "blijven ze in de stad werken, bij desurbanisatie vertrekken ook de werkplaatsen "
                "en de winkels. Dat tweede holt een kern echt uit.",
                "Noem er twee van verschillende soort: iets dat het mogelijk maakte (de auto, "
                "goedkope grond) en iets dat men wilde (een huis met tuin, rust). Dat de overheid "
                "het bouwen buiten de stad jarenlang zelf aanmoedigde, wordt vaak vergeten en "
                "verklaart waarom Vlaanderen er anders uitziet dan Nederland.",
            ],
        ),
        dict(
            aanpak="Drie begrippen die op elkaar lijken en niet hetzelfde zijn. Ruimtebeslag is "
                   "alles wat ingenomen is, verharding enkel het stuk onder beton of asfalt, "
                   "versnippering gaat over de stukken waarin de natuur uiteenvalt. Het eerste is "
                   "dus altijd groter dan het tweede.",
            waarom=[
                None,
                "De nevelstad is de naam voor het Vlaamse patroon als geheel: nergens echt stad "
                "en nergens echt platteland. Lintbebouwing is er één bouwsteen van.",
                "Een tuin hoort bij het ruimtebeslag en niet bij de verharding. Daarom is in "
                "Vlaanderen ongeveer een derde van de oppervlakte ingenomen terwijl de echte "
                "verharding rond de 16 procent zit.",
            ],
        ),
        dict(
            aanpak="Een stad warmt sterker op dan het platteland omdat ze warmte opslaat en "
                   "weinig verdampt. Zoek in je antwoord dus drie soorten oorzaken: wat warmte "
                   "vasthoudt, wat ontbreekt om te koelen, en wat zelf warmte maakt.",
            waarom=[
                "Merk op dat het verschil vooral 's nachts groot is. Overdag schijnt de zon op "
                "beide, maar 's nachts geeft het platteland zijn warmte snel af terwijl het beton "
                "in de stad die nog uren uitstraalt.",
                "Noem er drie van verschillende soort, want dat laat zien dat je het mechanisme "
                "begrijpt: opslag in beton, gebrek aan groen en water, en de warmte van gebouwen "
                "en verkeer zelf. Bij een hittegolf is dat geen comfortvraag maar een "
                "gezondheidsvraag, want juist in de dichtstbebouwde wijken is er het minste "
                "groen.",
            ],
        ),
        dict(
            aanpak="Drie niveaus en één plan: de gemeente geeft de vergunningen, Vlaanderen zet "
                   "de grote lijnen, en een ruimtelijk uitvoeringsplan zegt perceel per perceel "
                   "wat mag. Bij de slotvraag staan twee geldige belangen tegenover elkaar, dus "
                   "geef er ook twee.",
            waarom=[
                None,
                "De bouwshift wordt ook betonstop genoemd, maar dat tweede woord is misleidend: "
                "het gaat niet over stoppen met bouwen maar over niet méér open ruimte aansnijden "
                "en dichter bouwen waar al bebouwing is.",
                "Geef beide argumenten echt hun gewicht; wie één kant afdoet als onredelijk mist "
                "het punt van de vraag. De eigenaar heeft een rechtmatige verwachting, de gemeente "
                "een rekening voor de gemeenschap. Precies daarom gaat de discussie over "
                "planschade en de vergoeding ervan.",
            ],
        ),
        dict(
            aanpak="Deze reeks is onderzoekswerk met Geopunt of de site van je gemeente. Zoek de "
                   "twee gegevens op, reken de dichtheid zelf uit, en kijk pas daarna naar de "
                   "luchtfoto met de begrippen van de vorige reeksen in het hoofd.",
            waarom=[
                None,
                None,
                "Deel het aantal inwoners door de oppervlakte in km². Een paar getallen om je "
                "uitkomst mee te vergelijken: Vlaanderen zit rond de 490 inwoners per km², "
                "Antwerpen boven de 2500 en een landelijke gemeente in de Westhoek onder de 150.",
                "Beschrijf wat je ziet en gebruik daarbij de woorden van de leerstof: kern, lint, "
                "verkaveling, open ruimte. In de meeste Vlaamse gemeenten is het antwoord allebei, "
                "en dat is precies de nevelstad uit het begin van de bundel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-landschap-lezen-en-duurzaam-ruimtegebruik-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk element of de natuur het maakte of de mens. Een rechte lijn "
                   "is bijna altijd menselijk; een vorm die het reliëf of het water volgt, is "
                   "bijna altijd natuurlijk. Een houtkant is geplant en dus menselijk, ook al "
                   "bestaat hij uit bomen.",
            waarom=[
                "Het paar dat vaak misloopt is b tegenover e. Een duinengordel is door wind en "
                "zee gevormd, een houtkant door een boer geplant om een perceel af te zetten. "
                "Levend materiaal maakt iets dus niet natuurlijk.",
                "Landschapsgenese betekent letterlijk het ontstaan van het landschap. Het woord "
                "zegt dat een landschap geen toestand is maar het resultaat van een geschiedenis.",
            ],
        ),
        dict(
            aanpak="Lees een landschap van onder naar boven en van oud naar jong: eerst het "
                   "reliëf, dan de bodem, dan het water, dan de begroeiing, dan de mens, en als "
                   "laatste de tijd. Die orde is geen afspraak maar een logica, want elke laag "
                   "verklaart de volgende.",
            waarom=[
                "Het reliëf en de bodem staan vooraan omdat ze het oudst zijn en de rest bepalen: "
                "waar het nat is, komt geen akker, en waar het steil is, komt geen dorp. De "
                "bewoning komt daarom helemaal achteraan.",
            ],
        ),
        dict(
            aanpak="Kies het beeld bij de vraag. Wil je hoogte, neem een hoogtemodel; wil je "
                   "vroeger, neem een oude luchtfoto; wil je een heel gewest in één keer, neem een "
                   "satellietbeeld; wil je laten zien hoe iets oogt, neem een schuine foto.",
            waarom=[
                "Een hoogtemodel uit lasermetingen is het sterkste van de vier, want het ziet ook "
                "wat onder de bomen ligt: oude wegen, grachten en zelfs akkergrenzen van eeuwen "
                "terug worden erop zichtbaar.",
                None,
                "Noem beide voordelen: lagen combineren en ermee rekenen. Dat tweede is wat een "
                "GIS echt onderscheidt van een kaart, want de vraag wie binnen vijfhonderd meter "
                "van een plein woont, kan je op papier niet stellen.",
            ],
        ),
        dict(
            aanpak="Vier strategieën om geen nieuwe grond aan te snijden. Intensivering is meer "
                   "op dezelfde plek, hergebruik is een bestaand gebouw een nieuwe taak geven, "
                   "verweving is twee functies op één plek, tijdelijk gebruik is een plek benutten "
                   "tot er iets anders komt.",
            waarom=[
                "Let op c en e: bij verweving gaat het niet om hetzelfde gebouw maar om twee "
                "functies die samen door één ruimte bediend worden. Een speelplaats die in het "
                "weekend buurtplein is, dient twee groepen zonder één meter extra.",
                "Een brownfield opnieuw gebruiken slaat twee vogels in één slag: je neemt geen "
                "nieuwe open ruimte in en een vervuilde plek wordt gesaneerd.",
            ],
        ),
        dict(
            aanpak="Hier gaat het over de vraag waar de regen heen kan. Een wadi, doorlatende "
                   "klinkers en gras laten het water insijpelen; beton stuurt het naar de riool. "
                   "Bij de rekenoefening: 1 mm regen op 1 m² is precies 1 liter.",
            waarom=[
                None,
                "Merk op dat het nergens alles of niets is behalve bij beton. Daarom helpt elke "
                "halve maatregel al: ook doorlatende klinkers nemen een flink deel weg.",
                "Reken na: de helft van 1200 m² is 600 m², en 20 mm op 600 m² is 600 maal 20 "
                "liter, dus 12 000 liter. Dat is twee tankwagens water die niet meer naar de "
                "riool gaan maar in de grond zakken.",
            ],
        ),
        dict(
            aanpak="Zet bij zo'n afweging de argumenten in dezelfde soorten tegenover elkaar: "
                   "bereikbaarheid, grondgebruik, en wat het met de kern doet. Een alternatief is "
                   "pas een alternatief als het dezelfde winkel mogelijk maakt op minder ruimte.",
            waarom=[
                "Geef twee voor en twee tegen, en zorg dat ze over verschillende dingen gaan. Het "
                "sterkste tegenargument is wat er met de dorpskern gebeurt, want een winkel buiten "
                "het dorp trekt de klanten weg bij de winkels die er al zijn.",
                "Een goed alternatief combineert functies op dezelfde grond: winkel beneden, "
                "wonen boven, parking onder of gedeeld. Dat is de verweving en de intensivering "
                "uit de vierde reeks, nu toegepast.",
            ],
        ),
    ],
)
