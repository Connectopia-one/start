# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij aardrijkskunde 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere plaatsen om mee te rekenen, andere gevallen om in te delen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een schema
tekenen, een oordeel verantwoorden). Wie hier iets bijschrijft, legt het eerst
naast `../../beyond/aardrijkskunde.json` en naast de leerbundel van hetzelfde
thema in `maak_aardrijkskunde_beyond.py`.

Alle kengetallen in de rekenoefeningen zijn nagerekend: een graad breedte is
111 km, een uurgordel vijftien graden, en de gradiënt van de temperatuur in de
troposfeer 0,65 °C per 100 m.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Aardrijkskunde"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NIVEAU = "-beyond"
VOOR = "oefenbundel-"

W = "120px"
WW = "185px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag: schrijf eerst de bewerking op en zet de eenheid erbij.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm, met een begrip uit de leerstof.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("situeren-kaarten-en-observatie",
    titel="Situeren, kaarten en observatie",
    reeksen=[
        dict(kop="Coördinaten omzetten",
             opdracht="Een graad heeft zestig minuten. Schrijf om, en rond af op één minuut.",
             oefeningen=[
                 ("rij", [("50,5° NB", "50° 30' NB"), ("4,25° OL", "4° 15' OL"),
                          ("12,75° ZB", "12° 45' ZB"), ("3,1° WL", "3° 06' WL")],
                  "Zet om naar graden en minuten.", W),
                 ("rij", [("51° 15' NB", "51,25° NB"), ("6° 45' OL", "6,75° OL"),
                          ("22° 30' ZB", "22,5° ZB")],
                  "Zet om naar een decimale graad.", W),
                 ("kort", "Hoeveel kilometer ligt er tussen 50° NB en 51° NB?",
                  "ongeveer 111 km", W),
                 ("kort", "En tussen 50° 00' NB en 50° 30' NB?", "ongeveer 55,5 km", W),
                 ("open", "Waarom kan je dezelfde rekening niét maken voor een graad "
                          "oosterlengte?",
                  "De meridianen lopen naar de polen toe naar elkaar, dus een graad lengte is "
                  "aan de evenaar 111 km en bij ons maar ongeveer 70 km. Breedtecirkels liggen "
                  "wel overal even ver van elkaar.", 3),
             ]),
        dict(kop="Absoluut of relatief?",
             opdracht="Duid aan hoe er gesitueerd wordt.",
             oefeningen=[
                 ("kies", "Het meetstation ligt op 46° 12' NB en 7° 48' OL.",
                  ["absoluut", "relatief"], 0),
                 ("kies", "Het dorp ligt op de zuidflank van de vallei, boven de "
                          "nevelgrens.", ["absoluut", "relatief"], 1),
                 ("kies", "Genk ligt ten oosten van Hasselt, langs het Albertkanaal.",
                  ["absoluut", "relatief"], 1),
                 ("kies", "De boring gebeurde op 60° ZB, 0° lengte.",
                  ["absoluut", "relatief"], 0),
                 ("open", "Geef van je eigen school één absolute en één relatieve situering.",
                  "Absoluut met coördinaten uit Geopunt of Google Maps (bijvoorbeeld "
                  "50° 56' NB, 5° 20' OL), relatief bijvoorbeeld: in het centrum van de "
                  "gemeente, naast het station.", 3),
             ]),
        dict(kop="De schaal",
             opdracht="Reken met de schaal. Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "Op een kaart 1 : 25 000 meet een weg 8 cm. Hoe lang is hij echt?",
                  "8 × 25 000 = 200 000 cm = 2 km", WW),
                 ("kort", "Op een kaart 1 : 10 000 is dezelfde weg hoeveel centimeter?",
                  "20 cm", W),
                 ("kort", "Twee dorpen liggen 15 km van elkaar. Hoeveel centimeter is dat op "
                          "1 : 300 000?", "5 cm", W),
                 ("kies", "Welke schaal is de grootste?",
                  ["1 : 10 000", "1 : 50 000", "1 : 250 000", "1 : 1 000 000"], 0),
                 ("waar", "Op een kaart met een grote schaal zie je een klein gebied met veel "
                          "detail.", True),
                 ("open", "Je moet een wandeling van 12 km uitstippelen door een bos. Welke "
                          "schaal kies je, en waarom?",
                  "Een grote schaal, bijvoorbeeld 1 : 10 000 of 1 : 25 000: je hebt de paden, "
                  "de hoogtelijnen en de knooppunten nodig, en die staan op een kleinschalige "
                  "kaart niet.", 3),
             ]),
        dict(kop="Welk gereedschap?",
             opdracht="Schrijf bij elke vraag het instrument of de bron die je nodig hebt.",
             oefeningen=[
                 ("rij", [("de hoogte van elk punt in een gemeente", "een hoogtekaart (DHM, uit lasermetingen)"),
                          ("de neerslag van vorige maand", "de meetreeks van een weerstation"),
                          ("het bodemgebruik in 1950 vergelijken met nu", "luchtfoto's van beide jaren")],
                  "Wat gebruik je?", WL),
                 ("rij", [("de ondergrond onder een bouwput", "een boring en een geologische kaart"),
                          ("de beweging van een gletsjer over tien jaar", "satellietbeelden"),
                          ("de drukte op een kruispunt", "een eigen veldwaarneming met een telling")],
                  "Wat gebruik je?", WL),
                 ("kort", "Hoe heet een computerprogramma dat kaartlagen over elkaar legt en "
                          "erop rekent?", "een GIS", WW),
             ]),
        dict(kop="Sterren, planeten en manen",
             opdracht="Zet bij elke uitspraak waar of niet waar.",
             oefeningen=[
                 ("waar", "Een ster maakt zelf licht, een planeet niet.", True),
                 ("waar", "Een maan draait rond een planeet.", True),
                 ("waar", "De zon is een van de grootste sterren van de Melkweg.", False),
                 ("waar", "Een telescoop in de ruimte ziet scherper dan een even grote "
                          "telescoop op de grond, omdat de atmosfeer het beeld niet verstoort.",
                  True),
                 ("kort", "Hoe heet het sterrenstelsel waarin de zon ligt?", "de Melkweg", W),
                 ("open", "Noem één voordeel van een satelliet boven een vliegtuig om de aarde "
                          "te observeren, en één nadeel.",
                  "Voordeel: een satelliet komt regelmatig over hetzelfde gebied en dekt de "
                  "hele aarde, ook onbereikbare streken. Nadeel: het beeld is minder "
                  "gedetailleerd dan een luchtfoto en wolken kunnen het zicht blokkeren.", 3),
             ]),
        dict(kop="De vier sferen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["verschijnsel", "sfeer", "waarom"],
                  [["een storm boven de Noordzee", "atmosfeer", "het gaat over de lucht"],
                   ["een modderstroom in de Alpen", None, None],
                   ["het smelten van de Groenlandse ijskap", None, None],
                   ["een bosbrand in Portugal", None, None]],
                  "modderstroom: geosfeer, het gaat over bodem en gesteente die bewegen · "
                  "ijskap: hydrosfeer, water in vaste vorm · bosbrand: biosfeer, het gaat "
                  "over het leven", WW),
                 ("open", "Leg met één voorbeeld uit dat de sferen op elkaar inwerken.",
                  "Bijvoorbeeld: een droogte in de atmosfeer laat de bodem (geosfeer) uitdrogen, "
                  "waardoor planten (biosfeer) afsterven en het water in de rivieren "
                  "(hydrosfeer) zakt. Eén verandering werkt dus door in de andere sferen.", 3),
             ]),
    ])

# ============================================================
zet("het-heelal-ontstaan-en-afstanden",
    titel="Het heelal: ontstaan en afstanden",
    reeksen=[
        dict(kop="De Big Bang op een rij",
             opdracht="Zet de gebeurtenissen in de juiste orde door er 1 tot 5 bij te schrijven.",
             oefeningen=[
                 ("rij", [("de eerste sterren gaan schijnen", "4"),
                          ("de oerknal zelf", "1"),
                          ("de eerste atomen vormen zich", "3"),
                          ("de zon en de aarde ontstaan", "5"),
                          ("de quarks vormen protonen en neutronen", "2")],
                  "Welk nummer?", "58px"),
                 ("kort", "Hoe oud is het heelal volgens de huidige metingen?",
                  "ongeveer 13,8 miljard jaar", WW),
                 ("kort", "Hoe oud is de aarde?", "ongeveer 4,6 miljard jaar", WW),
             ]),
        dict(kop="Drie vaststellingen",
             opdracht="Schrijf bij elke vaststelling wat ze bewijst.",
             oefeningen=[
                 ("rij", [("het licht van verre sterrenstelsels is roder dan verwacht",
                           "ze bewegen van ons weg: het heelal dijt uit"),
                          ("overal komt dezelfde zwakke straling uit de ruimte",
                           "de nagloed van de oerknal, de achtergrondstraling"),
                          ("er is ongeveer driekwart waterstof en een kwart helium",
                           "precies de verhouding die de eerste minuten na de oerknal opleveren")],
                  "Wat bewijst het?", WL),
                 ("waar", "Hoe verder een sterrenstelsel staat, hoe sneller het zich van ons "
                          "verwijdert.", True),
                 ("waar", "De aarde staat in het midden van de uitdijing.", False),
                 ("open", "Een klasgenoot zegt: als alles van ons weg beweegt, staan wij in het "
                          "centrum. Weerleg dat met het beeld van een rijzend rozijnenbrood.",
                  "In een rijzend brood gaat elke rozijn van elke andere weg, en elke rozijn ziet "
                  "hetzelfde beeld. Er is dus geen centrum: de ruimte zelf rekt uit, de stelsels "
                  "bewegen niet door de ruimte weg van één punt.", 4),
             ]),
        dict(kop="Drie scenario's",
             opdracht="Zet de juiste naam bij de beschrijving.",
             oefeningen=[
                 ("rij", [("de uitdijing gaat eeuwig door en alles koelt af", "big freeze"),
                          ("de zwaartekracht haalt het en alles stort weer samen", "big crunch"),
                          ("de uitdijing versnelt zo sterk dat alles uiteengerukt wordt", "big rip")],
                  "Welk scenario?", WW),
                 ("kies", "Welk scenario sluit het best aan bij de gemeten versnelde uitdijing?",
                  ["big freeze", "big crunch", "een stabiel heelal", "geen van de drie"], 0),
             ]),
        dict(kop="Afstanden rekenen",
             opdracht="1 AE = 149,6 miljoen km. Eén lichtjaar = 9,46 biljoen km. Rond af.",
             oefeningen=[
                 ("kort", "Hoe ver staat Mars van de zon in km, als dat 1,5 AE is?",
                  "1,5 × 149,6 = ongeveer 224 miljoen km", WW),
                 ("kort", "Jupiter staat op 5,2 AE. Hoeveel miljoen km is dat?",
                  "ongeveer 778 miljoen km", WW),
                 ("kort", "Hoe lang doet het licht van de zon over de weg naar de aarde?",
                  "ongeveer 8 minuten en 20 seconden", WW),
                 ("kort", "Proxima Centauri staat op 4,24 lichtjaar. Zie je die ster zoals ze nu "
                          "is?", "nee, zoals ze 4,24 jaar geleden was", WL),
                 ("open", "Waarom gebruiken sterrenkundigen de astronomische eenheid binnen het "
                          "zonnestelsel en het lichtjaar daarbuiten?",
                  "Binnen het zonnestelsel zijn de afstanden met de aarde-zonafstand als maat "
                  "handige getallen van 0,4 tot 30. Daarbuiten worden die getallen zo groot dat "
                  "ze onleesbaar zijn, en dan is het lichtjaar de maat die nog te schrijven is.",
                  4),
             ]),
        dict(kop="Het adres van de aarde",
             opdracht="Vul de reeks aan van klein naar groot.",
             oefeningen=[
                 ("tabel", ["trap", "naam"],
                  [["de planeet", "de aarde"],
                   ["het stelsel rond onze ster", None],
                   ["het sterrenstelsel", None],
                   ["de groep stelsels", None],
                   ["de supercluster", None]],
                  "het zonnestelsel · de Melkweg · de Lokale Groep · Laniakea", WW),
                 ("kort", "Hoeveel sterren heeft de Melkweg ongeveer?",
                  "ongeveer 100 tot 400 miljard", WW),
             ]),
    ])

# ============================================================
zet("de-zon-en-het-zonnestelsel",
    titel="De zon en het zonnestelsel",
    reeksen=[
        dict(kop="De lagen van de zon",
             opdracht="Zet de lagen van binnen naar buiten, met 1 tot 6.",
             oefeningen=[
                 ("rij", [("de fotosfeer", "4"), ("de kern", "1"), ("de corona", "6"),
                          ("de convectiezone", "3"), ("de chromosfeer", "5"),
                          ("de stralingszone", "2")],
                  "Welk nummer?", "58px"),
                 ("kort", "Hoe warm is het in de kern van de zon?",
                  "ongeveer 15 miljoen °C", WW),
                 ("kort", "En aan de fotosfeer, het oppervlak dat wij zien?",
                  "ongeveer 5500 °C", WW),
                 ("waar", "De corona is kouder dan de fotosfeer.", False),
                 ("kort", "Welke kernreactie levert de energie van de zon?",
                  "kernfusie: waterstof smelt samen tot helium", WL),
             ]),
        dict(kop="Wat de zon uitstuurt",
             opdracht="Schrijf het juiste begrip op.",
             oefeningen=[
                 ("rij", [("een koeler, donkerder vlek op de fotosfeer", "een zonnevlek"),
                          ("een lus van gloeiend gas boven het oppervlak", "een protuberans"),
                          ("de stroom deeltjes die de zon de ruimte in blaast", "de zonnewind"),
                          ("het licht boven de poolstreken als die deeltjes aankomen",
                           "het poollicht (aurora)")],
                  "Hoe heet het?", WL),
                 ("kort", "Na hoeveel jaar is het aantal zonnevlekken weer op zijn hoogste punt?",
                  "ongeveer elf jaar", W),
                 ("open", "Noem twee dingen op aarde die een sterke zonnestorm kan verstoren.",
                  "Bijvoorbeeld het stroomnet (inductiestromen in hoogspanningslijnen), "
                  "satellieten en gps, radioverbindingen en de luchtvaart over de polen.", 3),
             ]),
        dict(kop="Hoe het zonnestelsel ontstond",
             opdracht="Vul in of kies.",
             oefeningen=[
                 ("rij", [("de wolk gas en stof waaruit alles begon", "de zonnenevel"),
                          ("het samenklonteren van stofkorrels tot grotere lichamen", "accretie"),
                          ("de schijf waarin de planeten gevormd werden", "de protoplanetaire schijf")],
                  "Hoe heet het?", WL),
                 ("open", "Waarom liggen de vier kleine, rotsachtige planeten binnen en de vier "
                          "reuzen buiten?",
                  "Dicht bij de jonge zon was het te warm: daar bleven alleen gesteente en "
                  "metaal over. Verder weg, achter de vorstlijn, kon ijs blijven bestaan, dus "
                  "daar was veel meer materiaal om grote planeten met dikke gasmantels te "
                  "vormen.", 4),
             ]),
        dict(kop="De acht planeten",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["planeet", "soort", "iets waaraan je ze herkent"],
                  [["Mercurius", "aardse planeet", "de kleinste, snelste omloop (88 dagen)"],
                   ["Venus", None, None],
                   ["Mars", None, None],
                   ["Jupiter", None, None],
                   ["Saturnus", None, None],
                   ["Neptunus", None, None]],
                  "Venus: aardse planeet, de heetste door haar dikke CO₂-dampkring · "
                  "Mars: aardse planeet, rood door ijzeroxide, twee kleine manen · "
                  "Jupiter: gasreus, de grootste, met de Grote Rode Vlek · "
                  "Saturnus: gasreus, met de duidelijkste ringen · "
                  "Neptunus: ijsreus, de verste, met de hardste winden", WW),
                 ("kies", "Welke planeet is de heetste?",
                  ["Mercurius", "Venus", "de aarde", "Jupiter"], 1),
                 ("kort", "Waarom is dat niet de planeet die het dichtst bij de zon staat?",
                  "Venus heeft een dikke CO2-atmosfeer, dus een zeer sterk broeikaseffect", WL),
                 ("waar", "Uranus en Neptunus heten ijsreuzen, Jupiter en Saturnus gasreuzen.",
                  True),
             ]),
        dict(kop="Gordels, dwergplaneten en kometen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Tussen welke twee planeten ligt de asteroïdengordel?",
                  "tussen Mars en Jupiter", WW),
                 ("kort", "Hoe heet de gordel ijsachtige lichamen voorbij Neptunus?",
                  "de Kuipergordel", WW),
                 ("kort", "En de bolvormige wolk veel verder nog, waar de langperiodieke kometen "
                          "vandaan komen?", "de Oortwolk", WW),
                 ("rij", [("Pluto", "dwergplaneet"), ("Ceres", "dwergplaneet in de asteroïdengordel"),
                          ("Eris", "dwergplaneet in de Kuipergordel")],
                  "Wat is het?", WL),
                 ("open", "Waarom is Pluto geen planeet meer?",
                  "Een planeet moet rond de zon draaien, bolvormig zijn én zijn baan "
                  "leeggeveegd hebben. Pluto haalt dat laatste niet: hij deelt zijn baan met "
                  "andere lichamen van de Kuipergordel.", 3),
                 ("kort", "Waaruit bestaat de staart van een komeet?",
                  "gas en stof dat van de kern afdampt bij de zon", WL),
             ]),
    ])


# ============================================================
zet("de-bewegingen-van-de-aarde",
    titel="De bewegingen van de aarde",
    reeksen=[
        dict(kop="Rotatie of revolutie?",
             opdracht="Duid aan welke beweging het verschijnsel verklaart.",
             oefeningen=[
                 ("kies", "dag en nacht", ["rotatie", "revolutie"], 0),
                 ("kies", "de seizoenen", ["rotatie", "revolutie"], 1),
                 ("kies", "de uurgordels", ["rotatie", "revolutie"], 0),
                 ("kies", "de middernachtzon in Noorwegen in juni",
                  ["rotatie", "revolutie"], 1),
                 ("kies", "het corioliseffect", ["rotatie", "revolutie"], 0),
                 ("kort", "Hoe lang doet de aarde over één rotatie ten opzichte van de zon?",
                  "24 uur", W),
                 ("kort", "En over één revolutie?", "365,25 dagen", W),
                 ("open", "Waarom hebben we een schrikkeljaar?",
                  "Een omloop duurt bijna een kwart dag langer dan 365 dagen. Zonder "
                  "schrikkeldag zouden de kalender en de seizoenen na eeuwen niet meer "
                  "samenvallen, dus komt er elke vier jaar een dag bij.", 3),
             ]),
        dict(kop="Rekenen met uurgordels",
             opdracht="Vijftien graden lengte is één uur. Oost is vooruit, west is achteruit.",
             oefeningen=[
                 ("kort", "In Brussel (15° OL-gordel) is het 14 uur. Hoe laat is het op 45° OL?",
                  "16 uur", W),
                 ("kort", "Hoeveel uur verschil is er tussen 0° en 75° WL?",
                  "5 uur, en het is daar vroeger", WW),
                 ("kort", "Het is 9 uur in New York (75° WL). Hoe laat is het in Londen (0°)?",
                  "14 uur", W),
                 ("waar", "Wie de datumgrens naar het westen oversteekt, slaat een dag over.",
                  True),
                 ("open", "Waarom loopt de datumgrens niet kaarsrecht over 180°?",
                  "Ze is om eilandengroepen en landen heen gelegd, zodat één land of één "
                  "eilandengroep niet in twee verschillende dagen zou liggen.", 3),
             ]),
        dict(kop="Het corioliseffect",
             opdracht="Vul in.",
             oefeningen=[
                 ("kies", "Een bewegende luchtmassa wijkt op het noordelijk halfrond af naar",
                  ["links", "rechts", "niet"], 1),
                 ("kies", "Op het zuidelijk halfrond wijkt ze af naar",
                  ["links", "rechts", "niet"], 0),
                 ("kies", "Op de evenaar is de afwijking",
                  ["het sterkst", "even sterk als elders", "nul"], 2),
                 ("open", "Leg uit waarom een depressie op het noordelijk halfrond tegen de "
                          "klok in draait.",
                  "De lucht stroomt naar het lagedrukcentrum toe, maar wijkt onderweg naar "
                  "rechts af. Daardoor komt ze niet recht binnen maar draait ze er linksom "
                  "rond: tegen de klok in.", 4),
             ]),
        dict(kop="De schuine as en de seizoenen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel graden helt de aardas?", "23,5°", W),
                 ("rij", [("21 juni", "zon loodrecht op de Kreeftskeerkring, zomer bij ons"),
                          ("21 december", "zon loodrecht op de Steenbokskeerkring, winter bij ons"),
                          ("21 maart en 23 september", "zon loodrecht op de evenaar, overal twaalf uur dag")],
                  "Wat gebeurt er?", WL),
                 ("waar", "In juni staat de aarde het dichtst bij de zon, en daarom is het "
                          "zomer.", False),
                 ("open", "Waarom is het bij ons in juni warmer, als de afstand niet de reden "
                          "is?",
                  "Door de schuine as staat de zon in juni hoger boven de horizon en is de dag "
                  "langer. Dezelfde hoeveelheid zonlicht valt dan op een kleiner oppervlak en "
                  "warmt dat langer op.", 4),
                 ("kort", "Boven welke breedte komt de poolnacht voor?",
                  "boven 66,5° (de poolcirkels)", WW),
                 ("kort", "Hoe heet de zon die in juni in Noord-Noorwegen niet ondergaat?",
                  "de middernachtzon", WW),
             ]),
        dict(kop="Dezelfde parallel, dezelfde zon",
             opdracht="Reken en verklaar.",
             oefeningen=[
                 ("kort", "Hoeveel bedraagt de middaghoogte van de zon in Hasselt (51° NB) op "
                          "21 maart?", "90 − 51 = 39°", WW),
                 ("kort", "En op 21 juni?", "39 + 23,5 = 62,5°", WW),
                 ("kort", "En op 21 december?", "39 − 23,5 = 15,5°", WW),
                 ("open", "Twee steden liggen op dezelfde breedtecirkel, de ene aan de kust en "
                          "de andere diep in het binnenland. Krijgen ze dezelfde zonnestand, en "
                          "hetzelfde klimaat?",
                  "Dezelfde zonnestand wel, want die hangt alleen van de breedte en de datum af. "
                  "Niet hetzelfde klimaat: de zee dempt de temperatuurverschillen, dus de "
                  "kuststad heeft zachtere winters en koelere zomers.", 4),
             ]),
    ])

# ============================================================
zet("de-maan-getijden-en-verduisteringen",
    titel="De maan, getijden en verduisteringen",
    reeksen=[
        dict(kop="De omloop van de maan",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel dagen doet de maan over één omloop rond de aarde ten "
                          "opzichte van de sterren?", "27,3 dagen", W),
                 ("kort", "En van nieuwe maan tot nieuwe maan?", "29,5 dagen", W),
                 ("open", "Waarom zijn die twee niet gelijk?",
                  "Terwijl de maan rond de aarde draait, schuift de aarde zelf verder rond de "
                  "zon. De maan moet dus iets meer dan een volle ronde maken voor ze weer "
                  "dezelfde stand ten opzichte van de zon heeft.", 4),
                 ("waar", "Wij zien altijd dezelfde zijde van de maan, omdat de maan niet om "
                          "haar as draait.", False),
                 ("kort", "Hoe heet het dat de maan in dezelfde tijd één keer rond haar as en "
                          "één keer rond de aarde draait?", "gebonden rotatie", WW),
             ]),
        dict(kop="De schijngestalten",
             opdracht="Zet ze in de juiste orde met 1 tot 4, te beginnen bij nieuwe maan.",
             oefeningen=[
                 ("rij", [("volle maan", "3"), ("nieuwe maan", "1"),
                          ("laatste kwartier", "4"), ("eerste kwartier", "2")],
                  "Welk nummer?", "58px"),
                 ("kort", "Waar staat de maan bij nieuwe maan?",
                  "tussen de aarde en de zon", WW),
                 ("waar", "Bij volle maan staat de maan achter de aarde ten opzichte van de "
                          "zon.", True),
                 ("open", "Waarom zie je bij nieuwe maan niets?",
                  "De zon beschijnt dan de achterzijde van de maan. De kant die naar ons gekeerd "
                  "is, ligt in de schaduw.", 3),
             ]),
        dict(kop="Eb en vloed",
             opdracht="Vul in.",
             oefeningen=[
                 ("kort", "Hoeveel keer hoogwater is er in 24 uur en 50 minuten?",
                  "twee keer", W),
                 ("rij", [("nieuwe maan en volle maan", "springtij: het grootste verschil"),
                          ("eerste en laatste kwartier", "doodtij: het kleinste verschil")],
                  "Welk getij, en waarom?", WL),
                 ("open", "Leg uit waarom er aan de andere kant van de aarde óók hoogwater is, "
                          "waar de maan juist niet staat.",
                  "De maan trekt het water aan de maanzijde naar zich toe, maar trekt ook de "
                  "aarde zelf iets naar zich toe, weg onder het water aan de overzijde. Daardoor "
                  "blijft daar een tweede waterberg achter.", 4),
                 ("kort", "Welk hemellichaam werkt ook mee aan de getijden, maar zwakker?",
                  "de zon", W),
             ]),
        dict(kop="Verduisteringen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kies", "Een zonsverduistering kan alleen bij",
                  ["nieuwe maan", "eerste kwartier", "volle maan", "elke stand"], 0),
                 ("kies", "Een maansverduistering kan alleen bij",
                  ["nieuwe maan", "eerste kwartier", "volle maan", "elke stand"], 2),
                 ("kort", "Wat staat er bij een maansverduistering in het midden?",
                  "de aarde", W),
                 ("open", "Als de drie lichamen elke maand dezelfde standen doorlopen, waarom is "
                          "er dan niet elke maand een verduistering?",
                  "De baan van de maan ligt onder een kleine hoek met de baan van de aarde. "
                  "Meestal gaat de maan net boven of onder de lijn aarde-zon door, en alleen "
                  "waar de banen elkaar kruisen valt er een schaduw.", 4),
                 ("waar", "Bij een totale zonsverduistering is de kernschaduw op aarde maar "
                          "enkele honderden kilometer breed.", True),
             ]),
    ])

# ============================================================
zet("de-opbouw-van-de-atmosfeer",
    titel="De opbouw van de atmosfeer",
    reeksen=[
        dict(kop="De lagen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["laag", "van … tot …", "waaraan je ze kent"],
                  [["troposfeer", "0 tot ongeveer 12 km", "hier gebeurt het weer"],
                   ["stratosfeer", None, None],
                   ["mesosfeer", None, None],
                   ["thermosfeer", None, None]],
                  "stratosfeer: 12 tot 50 km, hier zit de ozonlaag en stijgt de temperatuur "
                  "met de hoogte · mesosfeer: 50 tot 85 km, de koudste laag, hier verbranden "
                  "de meteoren · thermosfeer: 85 tot 600 km, zeer ijle lucht, hier ontstaat "
                  "het poollicht", WW),
                 ("kort", "In welke laag vliegt een verkeersvliegtuig meestal?",
                  "onderaan de stratosfeer, boven het weer", WL),
                 ("waar", "In de stratosfeer stijgt de temperatuur met de hoogte.", True),
             ]),
        dict(kop="Rekenen met de gradiënt",
             opdracht="In de troposfeer daalt de temperatuur 0,65 °C per 100 m. Reken na.",
             oefeningen=[
                 ("kort", "Aan de voet van een berg is het 18 °C. Hoe koud is het 2000 m hoger?",
                  "18 − 13 = 5 °C", WW),
                 ("kort", "Op 3000 m is het −4 °C. Hoe warm is het op zeeniveau?",
                  "−4 + 19,5 = 15,5 °C", WW),
                 ("kort", "Hoe hoog moet je klimmen om 10 °C te verliezen?",
                  "ongeveer 1540 m", WW),
                 ("open", "Een dorp op 1200 m hoogte ligt op dezelfde breedte als een stad aan "
                          "de kust. Welk temperatuurverschil verwacht je door de hoogte alleen?",
                  "Ongeveer 1200 ÷ 100 × 0,65 = 7,8 °C koeler in het dorp, als al de rest gelijk "
                  "zou zijn.", 3),
             ]),
        dict(kop="Waar de lucht uit bestaat",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("stikstof", "ongeveer 78 %"), ("zuurstof", "ongeveer 21 %"),
                          ("argon", "ongeveer 0,9 %"), ("koolstofdioxide", "ongeveer 0,04 %")],
                  "Welk aandeel?", WW),
                 ("open", "CO2 is maar 0,04 % van de lucht. Waarom is dat toch belangrijk?",
                  "CO2 houdt warmtestraling tegen. Een klein aandeel van een sterk "
                  "broeikasgas bepaalt mee hoeveel warmte de aarde kwijtraakt, dus een kleine "
                  "stijging werkt stevig door in de temperatuur.", 4),
                 ("rij", [("ozon hoog in de stratosfeer", "nuttig: het houdt uv-straling tegen"),
                          ("ozon beneden in de troposfeer", "schadelijk: het prikt in de longen")],
                  "Nuttig of schadelijk, en waarom?", WL),
             ]),
        dict(kop="Albedo",
             opdracht="Zet de oppervlakken in de orde van het hoogste naar het laagste albedo.",
             oefeningen=[
                 ("rij", [("verse sneeuw", "1"), ("een naaldbos", "4"),
                          ("woestijnzand", "2"), ("de oceaan", "5"), ("een betonnen plein", "3")],
                  "Welk nummer?", "58px"),
                 ("kort", "Wat betekent een albedo van 0,8?",
                  "80 % van het zonlicht wordt weerkaatst", WL),
                 ("open", "Leg uit waarom het smelten van zee-ijs de opwarming versnelt.",
                  "IJs weerkaatst het zonlicht sterk, open water slorpt het bijna helemaal op. "
                  "Minder ijs betekent dus meer warmte-opname, meer smelt en nog minder ijs: een "
                  "versterkende terugkoppeling.", 4),
             ]),
        dict(kop="Wat de temperatuur van een plaats bepaalt",
             opdracht="Schrijf bij elk paar wie het warmst is, en door welke factor.",
             oefeningen=[
                 ("rij", [("Oslo of Rome in juli", "Rome, door de breedte"),
                          ("Oostende of Luik in januari", "Oostende, door de nabijheid van de zee"),
                          ("Genk of de top van de Mont Ventoux in mei", "Genk, door de hoogte")],
                  "Wie, en waarom?", WL),
                 ("kort", "Hoe heet een lijn op een kaart die punten met dezelfde temperatuur "
                          "verbindt?", "een isotherm", WW),
                 ("kort", "Hoe heet het verschijnsel dat een stad warmer is dan haar "
                          "omgeving?", "het hitte-eiland", WW),
                 ("open", "Noem twee maatregelen die het hitte-eiland van een stad verkleinen.",
                  "Bijvoorbeeld meer bomen en parken (schaduw en verdamping), ontharden van "
                  "pleinen en parkings, lichte dakbedekking, water in de stad brengen, groene "
                  "daken.", 3),
             ]),
    ])


# ============================================================
zet("luchtdruk-en-winden",
    titel="Luchtdruk en winden",
    reeksen=[
        dict(kop="Hoge of lage druk?",
             opdracht="Schrijf bij elk kenmerk H (hoge druk) of L (lage druk).",
             oefeningen=[
                 ("rij", [("de lucht daalt", "H"), ("de lucht stijgt", "L"),
                          ("wolken en neerslag", "L"), ("een heldere hemel", "H"),
                          ("de lucht stroomt aan de grond naar het centrum toe", "L"),
                          ("de lucht waaiert aan de grond uiteen", "H")],
                  "H of L?", "58px"),
                 ("kort", "Hoeveel hPa is de gemiddelde luchtdruk op zeeniveau?",
                  "1013 hPa", W),
                 ("waar", "Bij 1035 hPa in de winter verwacht je mist of vrieskou, geen regen.",
                  True),
                 ("open", "Waarom regent het bij lage druk?",
                  "De lucht stijgt op. Hoger is het kouder, dus koelt ze af tot onder het "
                  "dauwpunt, de waterdamp condenseert op condensatiekernen en er vormen zich "
                  "wolken en neerslag.", 4),
             ]),
        dict(kop="Isobaren lezen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat verbindt een isobaar?",
                  "punten met dezelfde luchtdruk", WW),
                 ("kies", "Waar waait het het hardst?",
                  ["waar de isobaren dicht bij elkaar liggen",
                   "waar ze ver uit elkaar liggen",
                   "altijd in het centrum van een hoog",
                   "dat kan je er niet aan zien"], 0),
                 ("kort", "Welke kracht zet de lucht in beweging, van hoog naar laag?",
                  "de drukgradiëntkracht", WW),
                 ("open", "Waarom waait de wind niet recht van het hoog naar het laag?",
                  "Het corioliseffect buigt de bewegende lucht af, op het noordelijk halfrond "
                  "naar rechts. Daardoor draait ze rond de drukkernen in plaats van er recht "
                  "op af te gaan. Wrijving aan de grond laat haar de isobaren nog onder een "
                  "hoek kruisen.", 4),
             ]),
        dict(kop="De drukgordels",
             opdracht="Vul de tabel aan, van de evenaar naar de pool.",
             oefeningen=[
                 ("tabel", ["breedte", "druk", "wat je er ziet"],
                  [["0°", "laag", "ITCZ: stijgende lucht, zware buien, regenwoud"],
                   ["30°", None, None],
                   ["60°", None, None],
                   ["90°", None, None]],
                  "30°: hoog, dalende droge lucht, de woestijngordel · "
                  "60°: laag, het polaire front, depressies en wisselvallig weer · "
                  "90°: hoog, koude dalende lucht, poolwoestijn", WW),
                 ("open", "Leg uit waarom de grote woestijnen rond 30° breedte liggen.",
                  "De lucht die aan de evenaar is opgestegen en haar vocht heeft afgegeven, "
                  "daalt rond 30° weer neer. Dalende lucht wordt warmer en droger, dus vormen "
                  "zich geen wolken en valt er bijna geen neerslag.", 4),
                 ("kort", "Hoe heet de zone waar de passaten samenkomen?",
                  "de ITCZ (intertropische convergentiezone)", WL),
             ]),
        dict(kop="Winden met een naam",
             opdracht="Schrijf de naam en de richting.",
             oefeningen=[
                 ("rij", [("de vaste wind tussen 30° en de evenaar, noordelijk halfrond",
                           "de noordoostpassaat"),
                          ("de overheersende wind bij ons, tussen 30° en 60°",
                           "de westenwind"),
                          ("de snelle band wind op tien kilometer hoogte",
                           "de straalstroom, van west naar oost")],
                  "Hoe heet hij, en vanwaar waait hij?", WL),
                 ("rij", [("overdag aan zee, van de zee naar het land", "de zeewind"),
                          ("'s nachts aan zee, van het land naar de zee", "de landwind")],
                  "Hoe heet hij?", WW),
                 ("open", "Leg uit waarom de zeewind overdag waait en 's nachts omkeert.",
                  "Land warmt overdag sneller op dan water. Boven het land stijgt de lucht, de "
                  "druk daalt er, en koelere lucht van boven de zee stroomt toe. 's Nachts "
                  "koelt het land sneller af dan de zee en keert alles om.", 4),
                 ("kort", "Uit welke richting komt de zomermoesson in India, en wat brengt ze?",
                  "van de zee (zuidwest), met veel regen", WL),
                 ("waar", "De wintermoesson waait van het land naar de zee en is droog.", True),
             ]),
    ])

# ============================================================
zet("neerslag-en-de-kringloop-van-het-water",
    titel="Neerslag en de kringloop van het water",
    reeksen=[
        dict(kop="De kringloop benoemen",
             opdracht="Schrijf bij elke stap het juiste woord.",
             oefeningen=[
                 ("rij", [("water wordt waterdamp aan het oppervlak", "verdamping"),
                          ("planten geven waterdamp af", "transpiratie"),
                          ("waterdamp wordt weer vloeibaar", "condensatie"),
                          ("water zakt in de bodem", "infiltratie"),
                          ("water loopt over het oppervlak weg", "afstroming")],
                  "Hoe heet de stap?", WW),
                 ("kort", "Hoe heet het water dat onder de grond blijft zitten?",
                  "het grondwater", WW),
                 ("open", "Wat gebeurt er met de kringloop als je een weide vervangt door een "
                          "parking?",
                  "De regen kan niet meer infiltreren, dus de afstroming neemt sterk toe. Het "
                  "water komt sneller en in grotere hoeveelheid in de riolering en de beken "
                  "terecht, en het grondwater wordt niet aangevuld.", 4),
             ]),
        dict(kop="Vochtigheid en dauwpunt",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat is het dauwpunt?",
                  "de temperatuur waarbij de lucht verzadigd is en de damp condenseert", WL),
                 ("waar", "Warme lucht kan meer waterdamp bevatten dan koude.", True),
                 ("kort", "Waarop condenseert de waterdamp in de lucht?",
                  "op condensatiekernen (stofjes, zout)", WL),
                 ("rij", [("een platte, grijze laag die de hele hemel bedekt", "stratus"),
                          ("een stapelwolk met een platte voet", "cumulus"),
                          ("een hoge, ijle veerwolk", "cirrus"),
                          ("een torenhoge buienwolk met een aambeeld", "cumulonimbus")],
                  "Welke wolk?", WW),
                 ("open", "Waarom slaat de ruit van de badkamer aan na een douche?",
                  "De lucht in de badkamer is warm en vol waterdamp. Aan het koude glas koelt ze "
                  "af tot onder het dauwpunt, dus condenseert de damp er tot druppels.", 3),
             ]),
        dict(kop="Neerslag meten",
             opdracht="Reken na. 1 mm neerslag is 1 liter per vierkante meter.",
             oefeningen=[
                 ("kort", "Er viel 18 mm regen. Hoeveel liter is dat op een dak van 60 m²?",
                  "18 × 60 = 1080 liter", WW),
                 ("kort", "Een regenton van 300 liter vangt het water van 25 m² dak. Bij hoeveel "
                          "mm regen is hij vol?", "300 ÷ 25 = 12 mm", WW),
                 ("kort", "Een station meet in een jaar 780 mm. Hoeveel is dat per maand "
                          "gemiddeld?", "65 mm", W),
                 ("waar", "Een regenmeter wordt vlak tegen een muur gezet, zodat de wind hem "
                          "niet omblaast.", False),
             ]),
        dict(kop="Drie soorten regen",
             opdracht="Schrijf bij elke situatie de soort.",
             oefeningen=[
                 ("rij", [("de lucht wordt tegen een gebergte omhoog geduwd",
                           "stuwingsregen (orografisch)"),
                          ("de grond warmt sterk op en de lucht stijgt in bellen op",
                           "stijgingsregen (convectief)"),
                          ("warme lucht schuift over koude lucht langs een front",
                           "frontale regen")],
                  "Welke soort?", WL),
                 ("kort", "Hoe heet de droge zijde achter een gebergte?",
                  "de regenschaduw", WW),
                 ("open", "Noem drie redenen waarom de ene plek veel natter is dan de andere.",
                  "Bijvoorbeeld: de ligging in een drukgordel (ITCZ nat, 30° droog), de "
                  "afstand tot de zee, een gebergte dat de lucht omhoog duwt of juist een "
                  "regenschaduw maakt, en een warme of koude zeestroom voor de kust.", 4),
                 ("kort", "Waarom is de Atacamawoestijn zo droog, ondanks de oceaan ernaast?",
                  "de koude Humboldtstroom: koude lucht stijgt niet op", WL),
             ]),
    ])

# ============================================================
zet("klimaatgebieden-biomen-en-zeestromen",
    titel="Klimaatgebieden, biomen en zeestromen",
    reeksen=[
        dict(kop="Weer of klimaat?",
             opdracht="Duid aan.",
             oefeningen=[
                 ("kies", "Morgen wordt het 7 °C met buien.", ["weer", "klimaat"], 0),
                 ("kies", "In juli is het in Sevilla gemiddeld 36 °C.", ["weer", "klimaat"], 1),
                 ("kies", "Het regent nu al drie dagen.", ["weer", "klimaat"], 0),
                 ("kort", "Over hoeveel jaar wordt een klimaatgemiddelde berekend?",
                  "dertig jaar", W),
             ]),
        dict(kop="Van klimaat naar bioom",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["klimaat", "bioom", "typisch voor de planten"],
                  [["tropisch, het hele jaar nat", "tropisch regenwoud", "meerdere lagen, altijd groen"],
                   ["tropisch met een droog seizoen", None, None],
                   ["droog, minder dan 250 mm", None, None],
                   ["mediterraan", None, None],
                   ["koud met naaldbos", None, None],
                   ["poolklimaat zonder bomen", None, None]],
                  "tropisch met een droog seizoen: savanne, grassen met enkele bomen die hun "
                  "blad verliezen · droog: woestijn, weinig planten, diepe wortels en "
                  "vetplanten · mediterraan: hardbladig struikgewas, kleine leerachtige "
                  "bladeren · koud met naaldbos: taiga, naalden en kegels · poolklimaat: "
                  "toendra, mossen, korstmossen en dwergstruiken", WW),
                 ("open", "Waarom staan er in de toendra geen bomen?",
                  "Het groeiseizoen is te kort en te koud, en de bodem is permanent bevroren "
                  "(permafrost), zodat wortels niet diep kunnen gaan en het smeltwater niet "
                  "wegkan.", 3),
                 ("kort", "Welk bioom hoort bij Hasselt?",
                  "gematigd loofbos", WW),
             ]),
        dict(kop="Zeestromen",
             opdracht="Schrijf warm of koud, en wat de stroom met de kust doet.",
             oefeningen=[
                 ("rij", [("de Noord-Atlantische Drift langs West-Europa",
                           "warm: zachte winters, veel regen"),
                          ("de Humboldtstroom langs Peru en Chili",
                           "koud: zeer droog, mist zonder regen"),
                          ("de Benguelastroom langs Namibië",
                           "koud: de Namibwoestijn tot aan zee")],
                  "Warm of koud, en het gevolg?", WL),
                 ("open", "Leg uit waarom het in januari in Bergen (Noorwegen, 60° NB) zachter "
                          "is dan in Montreal (Canada, 45° NB).",
                  "Bergen ligt aan de warme Noord-Atlantische Drift en krijgt zeelucht, "
                  "Montreal ligt in een continentaal binnenland met koude landlucht. De "
                  "zeestroom en de zee wegen hier zwaarder door dan de breedte.", 4),
             ]),
        dict(kop="De thermohaliene circulatie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Welke twee eigenschappen van het water drijven deze circulatie aan?",
                  "de temperatuur en het zoutgehalte", WL),
                 ("kort", "Waar zinkt het water in de Atlantische Oceaan?",
                  "bij Groenland en in de Labradorzee", WL),
                 ("open", "Waarom kan smeltwater van Groenland deze circulatie vertragen?",
                  "Smeltwater is zoet, dus het maakt het oppervlaktewater lichter. Lichter water "
                  "zinkt minder makkelijk, en net dat zinken trekt de hele lopende band op gang.",
                  4),
                 ("waar", "Als die circulatie zou stilvallen, zou het in West-Europa warmer "
                          "worden.", False),
             ]),
    ])


# ============================================================
zet("het-weer-in-europa",
    titel="Het weer in Europa",
    reeksen=[
        dict(kop="Warmtefront of koufront?",
             opdracht="Schrijf bij elk kenmerk WF of KF.",
             oefeningen=[
                 ("rij", [("lange, gelijkmatige regen uit een grijze laag", "WF"),
                          ("korte, hevige buien en soms onweer", "KF"),
                          ("cirrus eerst, dan steeds lagere wolken", "WF"),
                          ("een cumulonimbus met een aambeeld", "KF"),
                          ("daarna wordt het zachter", "WF"),
                          ("daarna klaart het op en wordt het frisser", "KF")],
                  "WF of KF?", "58px"),
                 ("kort", "Hoe heet het front dat ontstaat als het koufront het warmtefront "
                          "inhaalt?", "een occlusie", WW),
                 ("open", "Waarom is de regen van een koufront korter maar heviger dan die van "
                          "een warmtefront?",
                  "Een koufront heeft een steile voorzijde en duwt de warme lucht snel omhoog. "
                  "Dat geeft hoge buienwolken en een korte, hevige bui. Een warmtefront is "
                  "flauw hellend: de warme lucht glijdt traag omhoog en geeft een brede, grijze "
                  "wolkenlaag met urenlange regen.", 4),
             ]),
        dict(kop="Welke luchtsoort?",
             opdracht="Schrijf de luchtsoort op: maritiem of continentaal, polair of tropisch.",
             oefeningen=[
                 ("rij", [("vochtige, koele lucht van de Atlantische Oceaan", "maritiem polair"),
                          ("droge, ijzige lucht uit Rusland in januari", "continentaal polair"),
                          ("warme, vochtige lucht van de Azoren", "maritiem tropisch"),
                          ("hete, droge lucht uit de Sahara in juli", "continentaal tropisch")],
                  "Welke luchtsoort?", WL),
                 ("open", "Welke luchtsoort brengt bij ons een hittegolf, en waarom?",
                  "Continentaal tropische lucht uit Noord-Afrika of Zuid-Europa: ze is in een "
                  "warm binnenland opgewarmd, bevat weinig vocht en kan daardoor bij ons zonder "
                  "wolken hoog oplopen.", 3),
             ]),
        dict(kop="Een depressie trekt voorbij",
             opdracht="Zet de waarnemingen in de juiste orde met 1 tot 5.",
             oefeningen=[
                 ("rij", [("hoge sluierwolken komen op", "1"),
                          ("urenlange regen, de wind draait, het wordt zachter", "2"),
                          ("de warme sector: grijs, zacht, wat motregen", "3"),
                          ("een smalle band met hevige buien", "4"),
                          ("opklaringen, frisser, soms een stapelwolk", "5")],
                  "Welk nummer?", "58px"),
                 ("kort", "Hoe heet het deel tussen het warmtefront en het koufront?",
                  "de warme sector", WW),
             ]),
        dict(kop="Een weerkaart lezen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat betekent een L op een weerkaart?",
                  "een lagedrukgebied, een depressie", WW),
                 ("kort", "Hoe teken je een koufront?",
                  "een lijn met driehoekjes aan de kant waarheen het trekt", WL),
                 ("kort", "En een warmtefront?", "een lijn met halve bollen", WW),
                 ("kies", "Een kaart toont 1028 hPa boven Midden-Europa en wijd uit elkaar "
                          "liggende isobaren. Wat verwacht je?",
                  ["storm en regen", "rustig, droog weer", "zware onweders", "sneeuwval"], 1),
                 ("open", "Waarom kan een weerbericht van tien dagen nooit even betrouwbaar "
                          "zijn als een van morgen?",
                  "De atmosfeer is een chaotisch systeem: een klein verschil in de "
                  "beginmetingen groeit elke dag uit tot een groter verschil in de uitkomst. "
                  "Na ongeveer een week is die fout zo groot geworden dat de voorspelling niet "
                  "meer beter is dan het gemiddelde van het seizoen.", 4),
                 ("kort", "Welke snelle wind op tien kilometer hoogte stuurt onze depressies?",
                  "de straalstroom", WW),
             ]),
    ])

# ============================================================
zet("de-opbouw-van-de-geosfeer",
    titel="De opbouw van de geosfeer",
    reeksen=[
        dict(kop="Chemisch of fysisch ingedeeld?",
             opdracht="Schrijf bij elke laag C (naar samenstelling) of F (naar gedrag).",
             oefeningen=[
                 ("rij", [("de korst", "C"), ("de lithosfeer", "F"), ("de mantel", "C"),
                          ("de asthenosfeer", "F"), ("de buitenkern", "C")],
                  "C of F?", "58px"),
                 ("kort", "Tot hoe diep gaat de lithosfeer ongeveer?",
                  "ongeveer 100 km", W),
                 ("kort", "Hoe diep ligt de grens tussen mantel en kern?",
                  "ongeveer 2900 km", W),
                 ("kort", "Hoe diep is het middelpunt van de aarde?", "6371 km", W),
                 ("open", "Leg uit waarom de lithosfeer niet hetzelfde is als de korst.",
                  "De lithosfeer is de starre buitenschil: de korst plus het bovenste, stijve "
                  "deel van de mantel. De indeling korst-mantel gaat over de samenstelling, de "
                  "indeling lithosfeer-asthenosfeer over hoe het gesteente zich gedraagt.", 4),
             ]),
        dict(kop="Seismische golven",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("gaat door vaste stof én door vloeistof", "de P-golf"),
                          ("gaat alleen door vaste stof", "de S-golf"),
                          ("komt als eerste aan bij een seismograaf", "de P-golf")],
                  "Welke golf?", WW),
                 ("open", "Hoe weten we dat de buitenkern vloeibaar is, zonder er ooit geweest "
                          "te zijn?",
                  "Achter de aarde ligt een schaduwzone waar geen S-golven aankomen. S-golven "
                  "gaan niet door vloeistof, dus moet de laag die ze tegenhoudt vloeibaar zijn. "
                  "P-golven komen er wel, maar afgebogen.", 4),
                 ("waar", "Seismische golven versnellen als ze in dichter gesteente komen.",
                  True),
             ]),
        dict(kop="Twee soorten korst",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "oceanische korst", "continentale korst"],
                  [["dikte", "5 tot 10 km", None],
                   ["gesteente", "basalt", None],
                   ["dichtheid", "ongeveer 3,0 g/cm³", None],
                   ["ouderdom", "jong, hoogstens 200 miljoen jaar", None]],
                  "continentale korst: 30 tot 70 km dik · graniet · ongeveer 2,7 g/cm³ · "
                  "oud, tot bijna 4 miljard jaar", WW),
                 ("open", "Waarom duikt bij een botsing altijd de oceanische korst onder de "
                          "continentale, en niet omgekeerd?",
                  "Oceanische korst is zwaarder per volume. Bij een botsing zakt de dichtste "
                  "plaat weg onder de lichtere: dat is subductie.", 3),
                 ("kort", "Waarom vind je nergens oceanische korst van 500 miljoen jaar oud?",
                  "ze is ondertussen door subductie verdwenen", WL),
             ]),
        dict(kop="Isostasie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Waarop drijft de lithosfeer?", "op de asthenosfeer", WW),
                 ("waar", "Onder een hoog gebergte is de korst dikker dan onder een vlakte.",
                  True),
                 ("open", "Scandinavië komt nog altijd ongeveer een centimeter per jaar "
                          "omhoog. Verklaar dat.",
                  "Tijdens de laatste ijstijd drukte een kilometersdikke ijskap de korst naar "
                  "beneden. Nu dat gewicht weg is, veert de korst traag terug naar haar "
                  "evenwicht, omdat het mantelgesteente eronder maar langzaam toestroomt.", 4),
                 ("kort", "Hoeveel centimeter is dat na een eeuw?", "ongeveer 1 meter", W),
             ]),
    ])

# ============================================================
zet("platentektoniek-en-reliefvorming",
    titel="Platentektoniek en reliëfvorming",
    reeksen=[
        dict(kop="De bewijzen van Wegener",
             opdracht="Schrijf bij elke vaststelling wat ze aantoont.",
             oefeningen=[
                 ("rij", [("de kusten van Zuid-Amerika en Afrika passen in elkaar",
                           "ze hebben ooit aan elkaar gelegen"),
                          ("dezelfde fossielen op beide continenten",
                           "die dieren en planten leefden op één landmassa"),
                          ("dezelfde gesteenten en gebergten aan beide zijden",
                           "de gebergteketen liep ooit door"),
                          ("gletsjerkrassen in wat nu de tropen is",
                           "die gebieden lagen ooit bij de pool")],
                  "Wat toont het aan?", WL),
                 ("kort", "Hoe heette het supercontinent van ongeveer 250 miljoen jaar geleden?",
                  "Pangea", W),
                 ("open", "Waarom werd Wegener in zijn tijd niet geloofd?",
                  "Hij kon geen kracht aanwijzen die continenten door de oceaanbodem zou kunnen "
                  "duwen. Pas toen men de mid-oceanische ruggen en de spreiding van de "
                  "oceaanbodem ontdekte, was er een motor voor zijn idee.", 4),
             ]),
        dict(kop="Drie soorten plaatbeweging",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["beweging", "wat er ontstaat", "een voorbeeld"],
                  [["uit elkaar (divergent)", "een rug of een slenk, nieuwe korst", "de Midden-Atlantische Rug, IJsland"],
                   ["naar elkaar, oceaan onder continent", None, None],
                   ["naar elkaar, continent tegen continent", None, None],
                   ["langs elkaar (transform)", None, None]],
                  "oceaan onder continent: een diepzeetrog en een vulkanische bergketen, de "
                  "Andes · continent tegen continent: een plooiingsgebergte zonder vulkanen, "
                  "de Himalaya · transform: geen nieuwe en geen verdwijnende korst, wel veel "
                  "bevingen, de San Andreasbreuk", WW),
                 ("kort", "Hoe heet het wegduiken van een plaat onder een andere?",
                  "subductie", WW),
                 ("kort", "Welk gebergte ontstond uit de botsing van India met Azië?",
                  "de Himalaya", WW),
                 ("kort", "Hoe heet de slenk in Oost-Afrika waar een continent uit elkaar "
                          "scheurt?", "de Oost-Afrikaanse Rift", WL),
             ]),
        dict(kop="Wat de platen beweegt",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("warme mantel stijgt op, koude zakt", "convectiestromen"),
                          ("het hoge gedeelte van de rug duwt de plaat weg", "ridge push"),
                          ("de zware, koude plaat trekt de rest mee de diepte in", "slab pull")],
                  "Hoe heet de kracht?", WW),
                 ("kort", "Hoeveel centimeter per jaar bewegen platen ongeveer?",
                  "1 tot 10 cm per jaar", WW),
                 ("kort", "Hoe ver is dat in een miljoen jaar, bij 5 cm per jaar?",
                  "50 km", W),
             ]),
        dict(kop="Hotspots en het reliëf van de oceaanbodem",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet de opstijgende pijp heet mantelmateriaal die niet aan een "
                          "plaatrand ligt?", "een mantelpluim of hotspot", WL),
                 ("open", "Waarom liggen de eilanden van Hawaï op een rij, met de oudste het "
                          "verst weg?",
                  "De hotspot blijft op zijn plaats terwijl de plaat erover schuift. Elke "
                  "vulkaan die erboven gevormd werd, is met de plaat meegedreven, en daarom "
                  "worden de eilanden ouder naarmate ze verder van de hotspot liggen.", 4),
                 ("rij", [("het vlakke, ondiepe deel vlak voor de kust", "het continentaal plat"),
                          ("de vlakke bodem van de diepzee", "de abyssale vlakte"),
                          ("de diepste geul, bij een subductiezone", "een trog")],
                  "Hoe heet het?", WW),
                 ("kort", "Hoe diep is de diepste trog ongeveer?",
                  "ongeveer 11 km (de Marianentrog)", WW),
                 ("waar", "De plaatsen van vulkanen en aardbevingen tekenen op een wereldkaart "
                          "de randen van de platen uit.", True),
             ]),
    ])


# ============================================================
zet("aardbevingen-en-vulkanisme",
    titel="Aardbevingen en vulkanisme",
    reeksen=[
        dict(kop="Waar een beving begint",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet het punt in de diepte waar de breuk begint?",
                  "het hypocentrum (de haard)", WW),
                 ("kort", "En het punt recht daarboven aan het oppervlak?",
                  "het epicentrum", WW),
                 ("waar", "Bij een even sterke beving is de schade groter naarmate het "
                          "hypocentrum dieper ligt.", False),
                 ("kort", "Met welk toestel registreer je een beving?",
                  "een seismograaf", WW),
                 ("open", "Hoe bepalen drie stations samen waar het epicentrum lag?",
                  "Elk station meet het tijdsverschil tussen de P- en de S-golf en weet daaruit "
                  "hoe ver de beving was. Rond elk station teken je een cirkel met die afstand; "
                  "de drie cirkels snijden elkaar in het epicentrum.", 4),
             ]),
        dict(kop="Magnitude of intensiteit?",
             opdracht="Schrijf M (magnitude) of I (intensiteit).",
             oefeningen=[
                 ("rij", [("de energie die bij de breuk vrijkwam", "M"),
                          ("de schade die mensen ter plaatse vaststellen", "I"),
                          ("één getal voor de hele beving", "M"),
                          ("verschilt van dorp tot dorp", "I")],
                  "M of I?", "58px"),
                 ("kort", "Hoeveel keer meer energie komt er vrij bij een magnitude 7 dan bij "
                          "een 6?", "ongeveer 32 keer", WW),
                 ("kort", "En bij een 8 ten opzichte van een 6?", "ongeveer 1000 keer", WW),
                 ("open", "Twee bevingen hebben dezelfde magnitude, maar de ene eist duizenden "
                          "doden en de andere geen enkele. Noem drie redenen.",
                  "De diepte en de ligging (onder een stad of onder de oceaan), de bouwwijze en "
                  "de bouwvoorschriften, de bodem (losse grond versterkt de trillingen), het "
                  "tijdstip, en of er waarschuwing en hulpdiensten zijn.", 4),
                 ("kort", "Hoe heet de vloedgolf na een onderzeese beving?",
                  "een tsunami", WW),
             ]),
        dict(kop="De delen van een vulkaan",
             opdracht="Schrijf het juiste woord.",
             oefeningen=[
                 ("rij", [("gesmolten gesteente onder de grond", "magma"),
                          ("hetzelfde, maar aan het oppervlak", "lava"),
                          ("de ruimte waar het magma zich verzamelt", "de magmahaard"),
                          ("de pijp naar boven", "de schoorsteen"),
                          ("de opening bovenaan", "de krater")],
                  "Hoe heet het?", WW),
                 ("kort", "Hoe heet de zeer brede inzinking die overblijft als de top "
                          "instort?", "een caldera", WW),
             ]),
        dict(kop="Twee soorten vulkanen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "schildvulkaan", "stratovulkaan"],
                  [["de lava", "dun en vloeibaar, basaltisch", None],
                   ["de helling", "flauw en breed", None],
                   ["de uitbarsting", "rustig, lavastromen", None],
                   ["een voorbeeld", "Mauna Loa, IJsland", None]],
                  "stratovulkaan: taaie, kiezelrijke lava · een steile, hoge kegel · "
                  "explosief, met as en pyroclastische stromen · de Vesuvius, de Fuji, "
                  "Mount St. Helens", WW),
                 ("open", "Waarom is een taaie lava gevaarlijker dan een vloeibare?",
                  "Taaie lava laat de gassen niet ontsnappen. De druk loopt op tot de prop "
                  "openbarst, en dan komt alles ineens vrij: een explosieve uitbarsting met as "
                  "en pyroclastische stromen in plaats van een lavastroom waar je voor kan "
                  "weglopen.", 4),
                 ("rij", [("een gloeiende wolk as en gas die langs de helling raast",
                           "een pyroclastische stroom"),
                          ("een modderstroom van as en smeltwater", "een lahar"),
                          ("de fijne deeltjes die kilometers hoog gaan", "vulkanische as")],
                  "Hoe heet het?", WL),
             ]),
        dict(kop="Toch wonen op een vulkaan",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Noem drie redenen waarom mensen op de flank van een actieve vulkaan "
                          "blijven wonen.",
                  "De bodem is bijzonder vruchtbaar door de as, er is aardwarmte voor "
                  "elektriciteit en verwarming, er zijn delfstoffen, het toerisme brengt geld "
                  "op, en het is gewoon hun thuis en hun grond.", 4),
                 ("open", "Noem twee dingen waarmee een land zich op een uitbarsting kan "
                          "voorbereiden.",
                  "Meetnetten voor kleine bevingen, bodemvervorming en gassen om op tijd te "
                  "waarschuwen, oefeningen en evacuatieplannen, bouwverbod in de gevaarlijkste "
                  "zones, en dijken of geulen om lahars af te leiden.", 3),
             ]),
    ])

# ============================================================
zet("gesteenten-mineralen-en-datering",
    titel="Gesteenten, mineralen en datering",
    reeksen=[
        dict(kop="In welke groep?",
             opdracht="Schrijf M (magmatisch), S (sedimentair) of Me (metamorf).",
             oefeningen=[
                 ("rij", [("graniet", "M"), ("kalksteen", "S"), ("marmer", "Me"),
                          ("basalt", "M"), ("zandsteen", "S"), ("leisteen", "Me")],
                  "Welke groep?", "58px"),
                 ("rij", [("steenkool", "S"), ("gneis", "Me"), ("kwartsiet", "Me"),
                          ("klei", "S")],
                  "Welke groep?", "58px"),
                 ("kort", "Waaraan herken je een sedimentair gesteente in een wand?",
                  "aan de lagen, en soms aan fossielen", WL),
             ]),
        dict(kop="Grof of fijn?",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Graniet heeft grote kristallen, basalt bijna geen. Allebei komen ze "
                          "uit magma. Verklaar het verschil.",
                  "Graniet is diep in de aarde heel traag afgekoeld: de kristallen hadden tijd "
                  "om te groeien. Basalt is aan het oppervlak snel gestold, dus de kristallen "
                  "bleven microscopisch klein.", 4),
                 ("rij", [("gestold in de diepte", "dieptegesteente, bijvoorbeeld graniet"),
                          ("gestold aan het oppervlak", "uitvloeiingsgesteente, bijvoorbeeld basalt")],
                  "Hoe heet het, met een voorbeeld?", WL),
             ]),
        dict(kop="Wat wordt wat?",
             opdracht="Schrijf het metamorfe gesteente dat ontstaat.",
             oefeningen=[
                 ("rij", [("kalksteen", "marmer"), ("klei of schalie", "leisteen"),
                          ("zandsteen", "kwartsiet"), ("graniet", "gneis")],
                  "Wat wordt het?", WW),
                 ("kort", "Door welke twee dingen verandert een gesteente in een metamorf "
                          "gesteente?", "hoge druk en hoge temperatuur", WL),
                 ("waar", "Bij metamorfose smelt het gesteente volledig.", False),
             ]),
        dict(kop="De lagen lezen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Welke laag is de oudste in een ongestoorde opeenvolging?",
                  "de onderste", W),
                 ("open", "Een breuk doorsnijdt alle lagen behalve de bovenste twee. Wat weet "
                          "je dan over de ouderdom van die breuk?",
                  "De breuk is jonger dan alle lagen die ze doorsnijdt en ouder dan de twee "
                  "lagen die er ongestoord overheen liggen. Ze is dus ontstaan tussen die twee "
                  "momenten.", 4),
                 ("kort", "Wat is een gidsfossiel?",
                  "een soort die kort geleefd heeft en wijd verspreid was", WL),
             ]),
        dict(kop="Absolute datering",
             opdracht="Reken en antwoord.",
             oefeningen=[
                 ("kort", "Wat is de halveringstijd van koolstof-14?",
                  "ongeveer 5730 jaar", WW),
                 ("kort", "Na hoeveel jaar is er nog een kwart van over?",
                  "ongeveer 11 460 jaar", WW),
                 ("kies", "Waarvoor gebruik je koolstof-14 níét?",
                  ["een stuk houtskool uit een grot",
                   "een bot van 20 000 jaar oud",
                   "een graniet van 300 miljoen jaar",
                   "een zaadje uit een Romeinse put"], 2),
                 ("kort", "Wat gebruik je dan wel voor gesteenten van miljoenen jaren?",
                  "uranium-lood of kalium-argon", WL),
                 ("rij", [("het leven blijft eencellig, de oudste tijd", "het Precambrium"),
                          ("de tijd van de trilobieten en de eerste bossen", "het Paleozoïcum"),
                          ("de tijd van de dinosauriërs", "het Mesozoïcum"),
                          ("de tijd van de zoogdieren en de mens", "het Cenozoïcum")],
                  "Welk tijdperk?", WW),
                 ("kort", "Hoeveel miljoen jaar geleden stierven de niet-vliegende "
                          "dinosauriërs uit?", "66 miljoen jaar", WW),
             ]),
    ])

# ============================================================
zet("verwering-karst-en-massatransport",
    titel="Verwering, karst en massatransport",
    reeksen=[
        dict(kop="Verwering, erosie of sedimentatie?",
             opdracht="Schrijf V, E of S.",
             oefeningen=[
                 ("rij", [("een rots barst ter plaatse door vorst", "V"),
                          ("een rivier voert het puin mee", "E"),
                          ("het zand wordt in de monding afgezet", "S"),
                          ("de wind blaast korrels tegen een rots", "E"),
                          ("wortels wrikken een steen uiteen", "V")],
                  "V, E of S?", "58px"),
                 ("kort", "Wat is het verschil tussen verwering en erosie in één zin?",
                  "verwering breekt af ter plaatse, erosie voert af", WL),
             ]),
        dict(kop="Drie soorten verwering",
             opdracht="Schrijf mechanisch, chemisch of biologisch.",
             oefeningen=[
                 ("rij", [("water bevriest in een spleet en zet uit", "mechanisch"),
                          ("kalksteen lost op in zuur regenwater", "chemisch"),
                          ("korstmossen scheiden zuren af", "biologisch"),
                          ("ijzer in het gesteente roest", "chemisch"),
                          ("zoutkristallen groeien in de poriën", "mechanisch")],
                  "Welke soort?", WW),
                 ("open", "Waarom gaat chemische verwering sneller in de tropen dan in de "
                          "Alpen?",
                  "Chemische reacties lopen sneller bij hoge temperatuur en met veel water. In "
                  "de tropen is het warm en nat, in de hooggebergten koud en droog, en daar "
                  "overheerst de mechanische vorstverwering.", 4),
             ]),
        dict(kop="Karst",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "In welk gesteente ontstaat karst?", "in kalksteen", W),
                 ("kort", "Welk gas in het regenwater maakt het zuur genoeg om kalk op te "
                          "lossen?", "koolstofdioxide", WW),
                 ("rij", [("een trechtervormige inzinking aan het oppervlak", "een doline"),
                          ("de plaats waar een beek onder de grond verdwijnt", "een verdwijngat"),
                          ("de kegel die van het plafond groeit", "een stalactiet"),
                          ("de kegel die van de bodem omhoog groeit", "een stalagmiet")],
                  "Hoe heet het?", WW),
                 ("open", "Waarom liggen er in een karstgebied weinig rivieren aan het "
                          "oppervlak?",
                  "Het water zakt door de spleten en de holtes weg in de ondergrond en stroomt "
                  "daar verder. Het komt pas veel verder, bij een bron, weer naar boven.", 3),
             ]),
        dict(kop="Massatransport",
             opdracht="Schrijf de naam, en of het snel of traag gaat.",
             oefeningen=[
                 ("rij", [("de bodemlaag kruipt millimeters per jaar hellingafwaarts",
                           "bodemkruip, zeer traag"),
                          ("een pakket grond glijdt in één keer weg over een glijvlak",
                           "een aardverschuiving, snel"),
                          ("een brij van water, modder en puin raast door een geul",
                           "een modderstroom, zeer snel"),
                          ("losse stenen vallen van een steile wand",
                           "steenval, snel")],
                  "Hoe heet het?", WL),
                 ("open", "Noem vier dingen die de kans op een aardverschuiving vergroten.",
                  "Een steile helling, veel water in de bodem na lange regen, het verdwijnen "
                  "van bomen en hun wortels, trillingen door een beving of door werken, en "
                  "gewicht of afgraving boven- of onderaan de helling.", 4),
                 ("waar", "Een helling met bos schuift makkelijker dan een kale helling.",
                  False),
             ]),
        dict(kop="Wat mensen eraan doen",
             opdracht="Schrijf + (verkleint het risico) of − (vergroot het).",
             oefeningen=[
                 ("rij", [("terrassen aanleggen", "+"), ("de helling kaalkappen", "−"),
                          ("de voet van de helling afgraven voor een weg", "−"),
                          ("steenslagnetten en keermuren plaatsen", "+"),
                          ("het water uit de helling draineren", "+"),
                          ("bovenaan zwaar bouwen", "−")],
                  "+ of −?", "58px"),
                 ("open", "Een gemeente wil bouwen op een helling van 25°. Welk advies geef je, "
                          "en met welk argument uit de leerstof?",
                  "Afraden of alleen met strenge voorwaarden: bij zo'n steilte volstaat een "
                  "natte periode of een afgraving aan de voet om de helling in beweging te "
                  "brengen. Wie er toch bouwt, moet draineren, de begroeiing houden en de voet "
                  "van de helling ongemoeid laten.", 4),
             ]),
    ])


# ============================================================
zet("erosie-door-water-ijs-en-wind",
    titel="Erosie door water, ijs en wind",
    reeksen=[
        dict(kop="Het stroombekken",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Wat is een stroombekken?",
                  "al het gebied waarvan het water naar dezelfde rivier loopt", WL),
                 ("kort", "Hoe heet de lijn die twee stroombekkens scheidt?",
                  "de waterscheiding", WW),
                 ("kort", "Wat meet je in m³ per seconde?",
                  "het debiet", W),
                 ("kort", "Een rivier voert 45 m³/s af. Hoeveel is dat per minuut?",
                  "2700 m³", W),
             ]),
        dict(kop="Boven-, midden- of benedenloop?",
             opdracht="Schrijf B (boven), M (midden) of BE (beneden).",
             oefeningen=[
                 ("rij", [("een steile V-vormige vallei", "B"), ("meanders in een brede vlakte", "M"),
                          ("een delta met zandbanken", "BE"), ("grote keien in de bedding", "B"),
                          ("fijn slib dat bezinkt", "BE")],
                  "B, M of BE?", "58px"),
                 ("open", "Waarom slijt een rivier bovenaan vooral in de diepte en onderaan niet "
                          "meer?",
                  "Bovenaan is het verval groot, dus het water stroomt snel en snijdt zich "
                  "verticaal in. Verder stroomafwaarts wordt het verval klein: de rivier heeft "
                  "geen kracht meer om dieper te gaan en gaat zijdelings slingeren en afzetten.",
                  4),
             ]),
        dict(kop="Transport en afzetting",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kies", "Welke korrel wordt bij de laagste stroomsnelheid opgenomen?",
                  ["klei", "fijn zand", "grind", "een kei"], 1),
                 ("open", "Klei bestaat uit de kleinste deeltjes, en toch is er veel snelheid "
                          "nodig om ze op te nemen. Verklaar dat.",
                  "Kleideeltjes kleven aan elkaar vast. Je moet eerst die samenhang breken, en "
                  "dat vraagt meer kracht dan het losmaken van een zandkorrel die los op de "
                  "bodem ligt. Eenmaal in het water blijft klei dan wel heel lang zweven.", 4),
                 ("waar", "Hoe trager het water, hoe grover het materiaal dat bezinkt.", False),
             ]),
        dict(kop="Meanders",
             opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("de buitenbocht", "snel water: erosie, een steile oever"),
                          ("de binnenbocht", "traag water: afzetting, een zandbank")],
                  "Wat gebeurt er?", WL),
                 ("kort", "Hoe heet het meertje dat overblijft als een meander wordt "
                          "afgesneden?", "een hoefijzermeer", WW),
                 ("kort", "Hoe heet het verschijnsel dat hard gesteente blijft staan en zacht "
                          "wegslijt?", "differentiële erosie", WW),
                 ("open", "Waarom zit er in de bovenloop van een rivier vaak een waterval op de "
                          "plaats waar een harde laag ligt?",
                  "Het zachtere gesteente stroomafwaarts slijt sneller weg, zodat er een trap "
                  "ontstaat. Het water valt over de harde laag naar beneden en holt de zachte "
                  "laag eronder nog verder uit.", 4),
             ]),
        dict(kop="IJs en wind",
             opdracht="Schrijf bij elk spoor welke kracht het maakte.",
             oefeningen=[
                 ("rij", [("een U-vormige vallei", "een gletsjer"),
                          ("een rug van ongesorteerd puin aan het einde van een vallei",
                           "een gletsjer: een eindmorene"),
                          ("een zwerfkei van graniet in de Kempen", "een gletsjer of smeltwater"),
                          ("een duinenrij achter het strand", "de wind"),
                          ("een dik pakket fijn, geel stof in Haspengouw", "de wind: löss")],
                  "Welke kracht?", WL),
                 ("kort", "Hoe heet een door de zee ondergelopen gletsjervallei?",
                  "een fjord", WW),
                 ("open", "Waarom werkt wind alleen in woestijnen en aan de kust echt sterk?",
                  "Wind krijgt alleen vat op losse, droge korrels. Waar begroeiing of vocht de "
                  "korrels vasthoudt, kan hij ze niet opnemen. In een woestijn en op een droog "
                  "strand ontbreekt die bescherming.", 4),
             ]),
        dict(kop="Overstromen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Noem drie menselijke ingrepen die de kans op een overstroming "
                          "vergroten.",
                  "Verharden van de bodem, rechttrekken van beken, bouwen in het winterbed van "
                  "een rivier, draineren van natte gronden en ontbossing bovenstrooms.", 3),
                 ("open", "En drie die ze verkleinen.",
                  "Overstromingsgebieden aanleggen, beken opnieuw laten meanderen, ontharden en "
                  "infiltratie bevorderen, regenwater opvangen, en niet meer bouwen in "
                  "overstromingsgevoelig gebied.", 3),
                 ("kort", "Hoe heet het deel van de vallei dat alleen bij hoog water onder "
                          "loopt?", "het winterbed", WW),
             ]),
    ])

# ============================================================
zet("klimaat-doorheen-de-geologische-tijd",
    titel="Klimaat doorheen de geologische tijd",
    reeksen=[
        dict(kop="Hoe we het weten",
             opdracht="Schrijf bij elk archief wat het je vertelt.",
             oefeningen=[
                 ("rij", [("luchtbellen in een ijskern",
                           "de samenstelling van de lucht van toen, dus ook het CO2-gehalte"),
                          ("de breedte van boomringen", "hoe gunstig elk groeiseizoen was"),
                          ("stuifmeelkorrels in veen", "welke planten er groeiden, dus het klimaat"),
                          ("schelpjes in zeesediment", "de temperatuur van het zeewater")],
                  "Wat vertelt het?", WL),
                 ("kort", "Hoe ver gaan de diepste ijskernen van Antarctica terug?",
                  "ongeveer 800 000 jaar", WW),
                 ("waar", "Een archief dat het klimaat van vroeger bewaart, noemen we een "
                          "proxy.", True),
             ]),
        dict(kop="IJstijden",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel jaar geleden was de laatste ijstijd op haar hoogtepunt?",
                  "ongeveer 20 000 jaar", WW),
                 ("kort", "Hoeveel meter lager stond de zeespiegel toen?",
                  "ongeveer 120 m lager", WW),
                 ("open", "Waarom kon je toen te voet van het vasteland naar Engeland?",
                  "Al dat water zat vast in de ijskappen, dus stond de zeespiegel veel lager. "
                  "De ondiepe Noordzee lag droog en vormde een vlakte met rivieren waar mensen "
                  "en dieren over trokken.", 3),
                 ("kort", "Hoe heet een warmere periode tussen twee ijstijden?",
                  "een interglaciaal", WW),
             ]),
        dict(kop="De cycli van Milanković",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["cyclus", "wat verandert", "periode"],
                  [["excentriciteit", "de vorm van de baan rond de zon", "ongeveer 100 000 jaar"],
                   ["obliquiteit", None, None],
                   ["precessie", None, None]],
                  "obliquiteit: de helling van de aardas, tussen 22,1° en 24,5°, ongeveer "
                  "41 000 jaar · precessie: de tolbeweging van de aardas, ongeveer "
                  "26 000 jaar", WW),
                 ("open", "Die cycli veranderen de totale energie van de zon nauwelijks. "
                          "Waarom beslissen ze dan toch over een ijstijd?",
                  "Ze verdelen de energie anders over de breedten en de seizoenen. Een koele "
                  "zomer in het noorden volstaat: dan smelt de sneeuw van de winter niet "
                  "helemaal, het albedo stijgt en terugkoppelingen versterken de afkoeling.", 4),
             ]),
        dict(kop="De andere oorzaken",
             opdracht="Schrijf K (koelt af) of W (warmt op).",
             oefeningen=[
                 ("rij", [("een zware vulkaanuitbarsting met veel aerosolen", "K"),
                          ("meer CO2 in de atmosfeer", "W"),
                          ("een grotere ijskap, dus een hoger albedo", "K"),
                          ("de oceaan geeft CO2 af bij opwarming", "W")],
                  "K of W?", "58px"),
                 ("open", "Leg de terugkoppeling van het ijs-albedo in eigen woorden uit, en zeg "
                          "of ze versterkt of afremt.",
                  "Minder ijs betekent een donkerder oppervlak, dus meer opname van zonlicht, "
                  "dus meer opwarming, dus nog minder ijs. Het effect versterkt zichzelf: een "
                  "positieve of versterkende terugkoppeling.", 4),
                 ("waar", "Een vulkaanuitbarsting koelt de aarde jarenlang af, een "
                          "CO2-stijging warmt haar eeuwenlang op.", True),
             ]),
    ])

# ============================================================
zet("de-huidige-klimaatverandering",
    titel="De huidige klimaatverandering",
    reeksen=[
        dict(kop="Het broeikaseffect",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe warm zou het gemiddeld op aarde zijn zonder broeikaseffect?",
                  "ongeveer −18 °C", WW),
                 ("kort", "En hoe warm is het nu gemiddeld?", "ongeveer 15 °C", W),
                 ("rij", [("CO2", "broeikasgas"), ("methaan", "broeikasgas"),
                          ("waterdamp", "broeikasgas"), ("stikstof", "geen broeikasgas")],
                  "Wel of geen broeikasgas?", WW),
                 ("open", "Leg in drie zinnen uit hoe het broeikaseffect werkt.",
                  "Zonlicht gaat door de atmosfeer en warmt het aardoppervlak op. De aarde "
                  "straalt die warmte terug als infrarood. Broeikasgassen houden een deel van "
                  "die straling tegen en stralen ze deels terug naar beneden, zodat het aan de "
                  "grond warmer blijft.", 4),
             ]),
        dict(kop="Wat we nu al meten",
             opdracht="Vul de getallen aan.",
             oefeningen=[
                 ("kort", "Hoeveel graden is de aarde opgewarmd sinds 1850-1900?",
                  "ongeveer 1,1 tot 1,2 °C", WW),
                 ("kort", "Hoeveel centimeter steeg de zeespiegel sinds 1900 ongeveer?",
                  "ongeveer 20 cm", W),
                 ("rij", [("de gletsjers in de Alpen", "krimpen"),
                          ("het zee-ijs in de Noordelijke IJszee in september", "neemt af"),
                          ("de zuurtegraad van de oceaan", "de oceaan verzuurt")],
                  "Wat gebeurt ermee?", WL),
                 ("open", "Noem twee redenen waarom de zeespiegel stijgt.",
                  "Het smeltwater van gletsjers en ijskappen komt in de oceaan terecht, én "
                  "warmer water zet uit, zodat hetzelfde water meer plaats inneemt.", 3),
             ]),
        dict(kop="Hoe we weten dat het de mens is",
             opdracht="Schrijf bij elke waarneming waarom ze naar de mens wijst.",
             oefeningen=[
                 ("rij", [("de koolstof in de extra CO2 heeft de vingerafdruk van fossiele brandstof",
                           "fossiele koolstof is oud en mist C-14"),
                          ("de hoge atmosfeer koelt af terwijl de lage opwarmt",
                           "dat past bij broeikasgassen, niet bij een sterkere zon"),
                          ("de nachten warmen sterker op dan de dagen",
                           "ook dat past bij broeikasgassen en niet bij meer zonlicht"),
                          ("de zonneactiviteit vertoont sinds 1980 geen stijging",
                           "de zon kan de opwarming dus niet verklaren")],
                  "Waarom wijst het naar de mens?", WL),
                 ("open", "Iemand zegt: het klimaat is altijd veranderd, dus dit is natuurlijk. "
                          "Geef twee argumenten waarom dat niet volstaat.",
                  "De snelheid: wat vroeger duizenden jaren duurde, gebeurt nu in honderd jaar. "
                  "En de oorzaak is aanwijsbaar: de natuurlijke factoren (zon, vulkanen, "
                  "baanparameters) wijzen nu de andere kant op of veranderen niet, terwijl de "
                  "CO2 uit fossiele brandstof meetbaar stijgt.", 4),
             ]),
        dict(kop="Mitigatie of adaptatie?",
             opdracht="Schrijf M of A.",
             oefeningen=[
                 ("rij", [("windmolens bouwen", "M"), ("dijken verhogen", "A"),
                          ("minder vlees eten", "M"), ("meer schaduwbomen in de stad", "A"),
                          ("huizen isoleren", "M"), ("gewassen kiezen die tegen droogte kunnen", "A")],
                  "M of A?", "58px"),
                 ("kort", "Op hoeveel graden wil het Akkoord van Parijs de opwarming houden?",
                  "ruim onder 2 °C, liefst 1,5 °C", WL),
                 ("open", "Waarom noemt men de klimaatverandering ook een kwestie van "
                          "rechtvaardigheid?",
                  "De landen en de generaties die het minst hebben uitgestoten, worden er het "
                  "hardst door getroffen en hebben het minste geld om zich aan te passen. Wie "
                  "het probleem veroorzaakt heeft, draagt dus niet de grootste gevolgen.", 4),
             ]),
    ])


# ============================================================
zet("verstedelijking-en-ruimtegebruik",
    titel="Verstedelijking en ruimtegebruik",
    reeksen=[
        dict(kop="Welke fase?",
             opdracht="Schrijf urbanisatie, suburbanisatie, desurbanisatie of reurbanisatie.",
             oefeningen=[
                 ("rij", [("boeren trekken naar de fabrieken in de stad", "urbanisatie"),
                          ("gezinnen bouwen een villa in de rand en pendelen", "suburbanisatie"),
                          ("ook de bedrijven verlaten de stad, de kern verarmt", "desurbanisatie"),
                          ("jonge mensen kiezen weer voor een appartement in het centrum",
                           "reurbanisatie")],
                  "Welke fase?", WL),
                 ("open", "Noem twee redenen waarom gezinnen in de jaren zestig en zeventig naar "
                          "de rand trokken.",
                  "De auto maakte pendelen mogelijk, bouwgrond was er goedkoop, men wilde een "
                  "eigen huis met tuin en rust, en de overheid steunde het bouwen buiten de "
                  "stad.", 3),
             ]),
        dict(kop="De Vlaamse ruimte",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe noem je de bebouwing die zich lint na lint langs de steenwegen "
                          "uitstrekt?", "lintbebouwing", WW),
                 ("kort", "Hoe heet het patroon van overal verspreide bebouwing zonder "
                          "duidelijke stadsgrens?", "de nevelstad", WW),
                 ("rij", [("het aandeel van de oppervlakte dat door bebouwing en infrastructuur "
                           "ingenomen is", "het ruimtebeslag"),
                          ("het deel daarvan dat onder beton of asfalt zit", "de verharding"),
                          ("het opdelen van natuur in kleine stukken door wegen", "de versnippering")],
                  "Hoe heet het?", WL),
                 ("open", "Waarom is versnippering erg voor dieren, ook als de totale "
                          "oppervlakte natuur gelijk blijft?",
                  "Kleine stukken liggen van elkaar gescheiden door wegen en bebouwing. Dieren "
                  "kunnen niet meer van het ene naar het andere, dus worden de populaties te "
                  "klein, verzwakt de soort en kan een gebied na een ramp niet opnieuw bevolkt "
                  "worden.", 4),
             ]),
        dict(kop="Het hitte-eiland",
             opdracht="Reken en verklaar.",
             oefeningen=[
                 ("kort", "Hoeveel graden warmer kan een stadscentrum op een zomernacht zijn "
                          "dan het platteland eromheen?", "enkele graden, tot ongeveer 7 °C", WL),
                 ("open", "Noem drie oorzaken van het stedelijk hitte-eiland.",
                  "Beton en asfalt slaan overdag warmte op en geven ze 's nachts af, er is "
                  "weinig groen en water om te verdampen en schaduw te geven, de regen loopt "
                  "weg in plaats van te verdampen, en gebouwen, auto's en airco's geven zelf "
                  "warmte af.", 4),
                 ("open", "Wie heeft er het meest last van, en waarom is dat een reden om er "
                          "iets aan te doen?",
                  "Ouderen, zieken, jonge kinderen en mensen in een klein appartement zonder "
                  "tuin of airco, vaak in de dichtstbebouwde en armste wijken. Hitte is daar "
                  "een gezondheidsrisico, dus het gaat niet alleen over comfort.", 4),
             ]),
        dict(kop="Wie beslist over de ruimte",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("beslist over de meeste vergunningen", "de gemeente"),
                          ("legt de grote lijnen voor heel Vlaanderen vast", "de Vlaamse overheid"),
                          ("het plan dat vastlegt wat op een perceel mag", "een ruimtelijk uitvoeringsplan")],
                  "Wie of wat?", WL),
                 ("kort", "Hoe heet het plan om tegen 2040 geen extra open ruimte meer aan te "
                          "snijden?", "de bouwshift (de betonstop)", WL),
                 ("open", "Een eigenaar heeft een bouwgrond in een gebied dat men open wil "
                          "houden. Geef het argument van de eigenaar én dat van de gemeente.",
                  "De eigenaar: hij heeft betaald voor bouwgrond en rekent op die waarde, dus "
                  "hij vindt dat hij mag bouwen of vergoed moet worden. De gemeente: verdere "
                  "verspreide bebouwing kost veel aan wegen, riolering en vervoer, en zet "
                  "water, natuur en landbouwgrond verder onder druk.", 4),
             ]),
    ])

# ============================================================
zet("duurzaam-ruimtegebruik",
    titel="Duurzaam ruimtegebruik",
    reeksen=[
        dict(kop="Welke strategie?",
             opdracht="Schrijf intensivering, hergebruik, verweving of tijdelijk gebruik.",
             oefeningen=[
                 ("rij", [("op dezelfde grond twee bouwlagen meer zetten", "intensivering"),
                          ("een oude fabriek ombouwen tot lofts", "hergebruik"),
                          ("winkels beneden en woningen boven", "verweving"),
                          ("een braakliggend terrein tien jaar als moestuin gebruiken",
                           "tijdelijk gebruik"),
                          ("een schoolspeelplaats in het weekend openstellen als buurtplein",
                           "verweving")],
                  "Welke strategie?", WL),
                 ("kort", "Hoe heet een verlaten, vaak vervuild bedrijventerrein dat je opnieuw "
                          "kan gebruiken?", "een brownfield", WW),
                 ("open", "Waarom is bouwen op een brownfield beter dan op een weide, ook al is "
                          "het duurder?",
                  "Je neemt geen nieuwe open ruimte in, de wegen, de riolering en het openbaar "
                  "vervoer liggen er al, en een vervuilde plek wordt gesaneerd. De hogere "
                  "kostprijs weegt op tegen de kosten die een nieuwe verkaveling aan de "
                  "gemeenschap bezorgt.", 4),
             ]),
        dict(kop="Water en ontharden",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoe heet een ondiepe groene kom waarin regenwater kan insijpelen?",
                  "een wadi", W),
                 ("rij", [("een gewone betonverharding", "alles stroomt af"),
                          ("waterdoorlatende klinkers", "een deel sijpelt door"),
                          ("een grasveld", "bijna alles sijpelt in")],
                  "Wat doet het water?", WL),
                 ("open", "Een school onthardt haar speelplaats van 1200 m² voor de helft. Bij "
                          "20 mm regen: hoeveel liter gaat er nu niet meer naar de riool?",
                  "600 m² × 20 mm = 600 × 20 = 12 000 liter dat kan infiltreren in plaats van "
                  "af te stromen.", 3),
             ]),
        dict(kop="Wat een plek goed maakt",
             opdracht="Beoordeel en verantwoord.",
             oefeningen=[
                 ("open", "Noem vier dingen die een woonplek voor een gezin zonder auto goed "
                          "maken.",
                  "Een station of een bushalte dichtbij, een school en een winkel op "
                  "wandelafstand, veilige fietspaden, groen en een speelplek in de buurt, en "
                  "een dokter of apotheek in de omgeving.", 4),
                 ("open", "Twee bouwgronden: de ene naast een station in een dorpskern, de "
                          "andere vier kilometer verder in het veld. Welke zou je volgens het "
                          "omgevingsdenken bebouwen, en met welke drie argumenten?",
                  "De grond bij het station: de bewoners kunnen zich zonder auto verplaatsen, "
                  "de voorzieningen bestaan al, en je laat open ruimte open in plaats van ze "
                  "aan te snijden. Bouwen in het veld vraagt nieuwe wegen en riolering en maakt "
                  "iedereen van de auto afhankelijk.", 4),
                 ("kort", "Hoe noem je de waarde van een plek gemeten aan het openbaar vervoer "
                          "en de voorzieningen eromheen?", "de knooppuntwaarde", WL),
             ]),
    ])

# ============================================================
zet("het-landschap-lezen",
    titel="Het landschap lezen",
    reeksen=[
        dict(kop="Natuurlijk of menselijk?",
             opdracht="Schrijf N of M.",
             oefeningen=[
                 ("rij", [("een rivierterras", "N"), ("een houtkant tussen twee akkers", "M"),
                          ("een doline in de kalkbodem", "N"), ("een rechtgetrokken beek", "M"),
                          ("een duinengordel", "N"), ("een spoorwegberm", "M")],
                  "N of M?", "58px"),
                 ("kort", "Hoe heet het geheel van processen waardoor een landschap geworden is "
                          "wat het is?", "de landschapsgenese", WW),
             ]),
        dict(kop="Een landschap stap voor stap",
             opdracht="Zet de stappen in een logische orde met 1 tot 6.",
             oefeningen=[
                 ("rij", [("het reliëf en de hellingen bekijken", "1"),
                          ("de bodem en het gesteente erbij nemen", "2"),
                          ("het water: beken, grachten, vijvers", "3"),
                          ("de begroeiing en het landgebruik", "4"),
                          ("de bewoning, de percelen en de wegen", "5"),
                          ("de tijdslaag: wat is oud, wat is recent", "6")],
                  "Welk nummer?", "58px"),
                 ("open", "Je ziet op een luchtfoto lange smalle percelen loodrecht op een "
                          "beek, met daartussen een lint van huizen langs een weg. Wat leid je "
                          "daaruit af?",
                  "De percelen zijn zo verdeeld dat elke boerderij zowel natte grond bij de "
                  "beek als drogere grond hogerop had. Het lint langs de weg wijst op bebouwing "
                  "die stuk voor stuk langs de bestaande baan is bijgekomen, niet op een "
                  "geplande wijk.", 4),
             ]),
        dict(kop="Kijken van boven",
             opdracht="Schrijf welk beeld je kiest.",
             oefeningen=[
                 ("rij", [("de hoogte van elk punt in een gemeente tot op enkele centimeter",
                           "een digitaal hoogtemodel uit lasermetingen"),
                          ("zien hoe hetzelfde dorp er in 1971 uitzag", "een oude luchtfoto"),
                          ("de bodembedekking van heel Vlaanderen in één kaart",
                           "een satellietbeeld of een bodemgebruikskaart"),
                          ("laten zien hoe steil een helling oogt voor een bezoeker",
                           "een schuine foto")],
                  "Welk beeld?", WL),
                 ("kort", "Hoe heet het Vlaamse portaal met kaartlagen, luchtfoto's en "
                          "percelen?", "Geopunt", W),
                 ("open", "Wat is het voordeel van een GIS boven een papieren kaart?",
                  "Je kan er lagen in combineren (hoogte, water, bebouwing, bevolking), erop "
                  "rekenen (afstanden, oppervlakten, wie binnen 500 m woont) en de kaart "
                  "bijwerken zonder hem opnieuw te tekenen.", 4),
             ]),
        dict(kop="Systeemdenken",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een gemeente verhardt een groot plein in het centrum. Volg het "
                          "gevolg door drie sferen.",
                  "Het regenwater kan niet meer infiltreren (hydrosfeer): het stroomt versneld "
                  "naar de beek en vergroot de kans op wateroverlast. De bodem eronder droogt "
                  "uit en het grondwater wordt niet aangevuld (geosfeer). De bomen die er "
                  "stonden verdwijnen, dus minder schaduw en verdamping, en het plein wordt een "
                  "hete plek (atmosfeer en biosfeer).", 5),
                 ("kort", "Hoe heet het geheel van zeventien doelen van de Verenigde Naties voor "
                          "2030?", "de duurzame ontwikkelingsdoelen (SDG's)", WL),
                 ("open", "Duurzame ontwikkeling steunt op drie pijlers. Noem ze, en geef bij "
                          "een nieuwe verkaveling van elk één vraag.",
                  "Ecologisch: hoeveel open ruimte en natuur gaat eraan? Sociaal: kunnen ook "
                  "mensen met een kleiner inkomen er wonen, en geraken ze er zonder auto? "
                  "Economisch: wat kosten de wegen, de riolering en het vervoer aan de "
                  "gemeenschap, en wat brengt het op?", 5),
             ]),
    ])
