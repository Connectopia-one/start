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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-situeren-kaarten-en-observatie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een graad heeft zestig minuten, dus reken je met zestig en niet met honderd. "
                   "Van decimaal naar minuten: neem het deel na de komma maal 60. Van minuten "
                   "naar decimaal: deel de minuten door 60. En onthoud één getal: één graad "
                   "breedte is ongeveer 111 km, overal op aarde.",
            waarom=[
                "Reken de laatste na: 0,1 × 60 = 6, dus 3° 06'. Schrijf de minuten altijd met "
                "twee cijfers, zodat 06' niet als 60' gelezen wordt.",
                "En hier de omgekeerde weg: 15 gedeeld door 60 is 0,25. Een halve graad is dus "
                "30' en niet 50', en dat is de fout die iedereen één keer maakt.",
                None,
                "111 gedeeld door 2 = 55,5 km. Een halve graad is een halve afstand, want de "
                "breedtecirkels liggen overal even ver van elkaar.",
                "Reken het na met de cosinus: 111 × cos 50° is ongeveer 71 km. Aan de evenaar is "
                "een graad lengte nog 111 km, op de pool nul. Daarom kan je met lengte geen vaste "
                "afstand rekenen.",
            ],
        ),
        dict(
            aanpak="Absoluut situeren doe je met coördinaten of een adres: het klopt zonder dat "
                   "je iets anders moet kennen. Relatief situeren doe je ten opzichte van iets "
                   "anders. Zoek dus of er in de zin een ander punt genoemd wordt; is dat zo, "
                   "dan is het relatief.",
            waarom=[
                None,
                "Boven de nevelgrens is ook een relatieve situering, en dat is minder duidelijk "
                "dan ten oosten van Hasselt. Je kan het enkel plaatsen als je weet waar die "
                "grens ligt, en die verschuift.",
                None,
                "0° lengte lijkt op niets, maar het is de nulmeridiaan van Greenwich, en dat is "
                "een echte coördinaat. Dus absoluut.",
                "Toets je eigen antwoord: kan iemand met enkel jouw eerste situering de school "
                "op een kaart zetten zonder iets anders te kennen? Dan is ze absoluut.",
            ],
        ),
        dict(
            aanpak="De schaal 1 : 25 000 betekent dat één centimeter op de kaart 25 000 "
                   "centimeter in het echt is. Reken altijd eerst in centimeter en zet pas "
                   "achteraan om naar meter of kilometer. En onthoud: hoe kleiner het tweede "
                   "getal, hoe groter de schaal en hoe meer detail.",
            waarom=[
                "8 × 25 000 = 200 000 cm. Deel door 100 voor meter (2 000 m) en nog eens door "
                "1 000 voor kilometer (2 km).",
                "Dezelfde 2 km, maar nu op een schaal die twee en een half keer groter is: "
                "200 000 gedeeld door 10 000 = 20 cm. De weg wordt dus langer op het blad, niet "
                "in het echt.",
                "15 km is 1 500 000 cm; gedeeld door 300 000 geeft 5 cm. Zet de kilometers dus "
                "altijd eerst om in centimeter, anders ben je er een factor honderdduizend naast.",
                "1 : 10 000 is de grootste van de vier, want 1/10 000 is het grootste breukdeel. "
                "Dat voelt tegennatuurlijk, en daarom staat deze vraag erbij.",
                None,
                "Noem in je antwoord wat je nodig hebt en niet enkel welke schaal. Paden, "
                "hoogtelijnen en knooppunten staan alleen op een grootschalige kaart, en net "
                "daarom kies je ze.",
            ],
        ),
        dict(
            aanpak="Kies je bron naar wat je wil weten: hoogte komt van een hoogtemodel, een "
                   "meetreeks van een station, verandering over de tijd van beelden van twee "
                   "momenten, en de ondergrond van een boring. Wat je enkel ter plaatse kan "
                   "zien, vraagt een eigen waarneming.",
            waarom=[
                "Het DHM is het digitale hoogtemodel van Vlaanderen, gemaakt met laserscanning "
                "vanuit een vliegtuig. Het is nauwkeurig tot op enkele centimeter, en je kan het "
                "gratis bekijken op Geopunt.",
                "Let op de drukte op een kruispunt: daar bestaat geen bron voor. Sommige "
                "gegevens moet je zelf gaan tellen, en dat is ook geografisch werk.",
                "GIS staat voor geografisch informatiesysteem. Het idee is de laag: bodem, "
                "wegen, bevolking en hoogte over elkaar, en dan vragen stellen zoals welke huizen "
                "liggen in overstromingsgebied.",
            ],
        ),
        dict(
            aanpak="Houd drie soorten hemellichamen uit elkaar: een ster maakt zelf licht, een "
                   "planeet draait rond een ster en weerkaatst licht, een maan draait rond een "
                   "planeet. Bij de vragen over observatie telt telkens één ding: de atmosfeer "
                   "zit in de weg.",
            waarom=[
                None,
                None,
                "Niet waar. De zon is een heel gewone ster, eerder aan de kleine kant: de meeste "
                "sterren in de Melkweg zijn kleiner, en de grootste zijn honderden keren groter. "
                "Dat ze ons zo groot lijkt, komt enkel doordat ze dichtbij staat.",
                "Dit is ook waarom de Hubble- en de Webbtelescoop in de ruimte hangen. De "
                "atmosfeer doet de beelden trillen en houdt bovendien infrarood en ultraviolet "
                "tegen.",
                None,
                "Noem bij deze vraag het regelmatige en het volledige van een satelliet. Een "
                "vliegtuig vliegt waar en wanneer je het stuurt maar nooit over de hele aarde; "
                "een satelliet komt elke paar dagen over hetzelfde punt, en net daarmee kan je "
                "verandering meten.",
            ],
        ),
        dict(
            aanpak="Vier sferen: de atmosfeer is lucht, de hydrosfeer is water in elke vorm, de "
                   "geosfeer is gesteente en bodem, de biosfeer is het leven. Vraag je bij elk "
                   "verschijnsel af wat er precies beweegt of verandert, want dat beslist de "
                   "sfeer.",
            waarom=[
                "Let op de ijskap: die hoort bij de hydrosfeer en niet bij de geosfeer, want ijs "
                "is water. Men spreekt soms apart van de cryosfeer voor al het ijs en de sneeuw "
                "op aarde.",
                "Toets je eigen voorbeeld: het moet minstens drie sferen raken en een richting "
                "hebben, van oorzaak naar gevolg. Twee verschijnselen naast elkaar zetten toont "
                "nog geen samenhang.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-heelal-ontstaan-en-afstanden-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De orde van de oerknal volgt de temperatuur: hoe koeler, hoe grotere dingen "
                   "er kunnen bestaan. Eerst losse deeltjes, dan protonen en neutronen, dan "
                   "atomen, dan sterren, en pas veel later ons zonnestelsel. Ken de twee "
                   "kerngetallen: 13,8 en 4,6 miljard jaar.",
            waarom=[
                "Merk op hoe laat de aarde in de rij komt: ze is pas bij ongeveer twee derde van "
                "de geschiedenis van het heelal ontstaan. De atomen waaruit jij bestaat, zijn "
                "dus in oudere sterren gemaakt.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Drie onafhankelijke vaststellingen die alle drie naar de oerknal wijzen: de "
                   "roodverschuiving, de achtergrondstraling en de verhouding waterstof-helium. "
                   "Dat het er drie zijn die van elkaar losstaan, is het sterkste argument; leer "
                   "ze dus als een drieluik.",
            waarom=[
                "De roodverschuiving is hetzelfde verschijnsel als het lager worden van een "
                "sirene die wegrijdt, maar dan met licht. Rood is de lange kant van het "
                "spectrum, dus roder betekent weg van ons.",
                "Dit is de wet van Hubble, en het is precies wat je bij een uitrekkende ruimte "
                "verwacht: hoe meer ruimte er tussen jou en iets zit, hoe meer ruimte er bij "
                "komt.",
                None,
                "Het beeld van het rozijnenbrood is het antwoord dat ze willen horen. De kern "
                "ervan is de laatste zin: de ruimte zelf rekt uit. De stelsels razen niet door de "
                "ruimte weg van een punt; de afstanden ertussen worden groter.",
            ],
        ),
        dict(
            aanpak="Drie scenario's, en elk hangt af van wie het haalt: de uitdijing of de "
                   "zwaartekracht. Haalt de zwaartekracht het, dan stort alles samen; haalt de "
                   "uitdijing het, dan koelt alles af; versnelt ze onbeperkt, dan scheurt alles.",
            waarom=[
                None,
                "De metingen wijzen op een uitdijing die versnelt, en bij de huidige waarden "
                "eindigt dat in een heelal dat eeuwig verder uitdijt en afkoelt. De big rip "
                "vraagt dat de versnelling zelf nog toeneemt, en daar is geen bewijs voor.",
            ],
        ),
        dict(
            aanpak="Twee maten en twee gebruiken. Binnen het zonnestelsel reken je in "
                   "astronomische eenheden: het aantal AE maal 149,6 geeft miljoen kilometer. "
                   "Daarbuiten reken je in lichtjaren, en dan is de afstand ook meteen de tijd "
                   "die het licht erover deed.",
            waarom=[
                "1,5 × 149,6 = 224,4 miljoen km.",
                "5,2 × 149,6 = 777,9 miljoen km, dus ongeveer 778 miljoen.",
                "Reken het zelf na: 149,6 miljoen km gedeeld door 300 000 km per seconde is "
                "ongeveer 499 seconden, en dat is 8 minuten en 19 seconden.",
                "Dit is het mooiste gevolg van een lichtjaar: je kijkt altijd naar het verleden. "
                "Ging die ster vorig jaar uit, dan zie je haar nog meer dan drie jaar schijnen.",
                "Noem in je antwoord dat het om leesbare getallen gaat. In AE loopt het "
                "zonnestelsel van 0,4 tot 30, mooi hanteerbaar; in kilometers zou Proxima "
                "Centauri 40 biljoen km zijn, een getal waar niemand mee rekent.",
            ],
        ),
        dict(
            aanpak="Het adres van de aarde gaat van klein naar groot, telkens een stap verder: "
                   "zonnestelsel, Melkweg, Lokale Groep, en daarboven de superclusterstructuur "
                   "Laniakea. Elke stap is ongeveer honderd keer groter dan de vorige.",
            waarom=[
                "De Lokale Groep is de verzameling van ongeveer vijftig stelsels rond de Melkweg "
                "en de Andromedanevel; Laniakea is de supercluster waarin die groep ligt. De naam "
                "betekent onmetelijke hemel in het Hawaïaans.",
                "Het brede bereik in dit antwoord is geen onzekerheid van jou maar van de "
                "wetenschap: je kan de sterren niet tellen, je schat ze uit de massa van het "
                "stelsel, en die schatting verschilt per methode.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-zon-en-het-zonnestelsel-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De lagen van de zon gaan van binnen naar buiten: kern, stralingszone, "
                   "convectiezone, fotosfeer, chromosfeer, corona. Onthoud de fotosfeer als de "
                   "grens: dat is wat je ziet, en alles daarbuiten is atmosfeer van de zon.",
            waarom=[
                "De namen zeggen zelf hoe de energie naar buiten gaat: in de stralingszone als "
                "straling, in de convectiezone met stromend gas, zoals kokend water in een pan.",
                None,
                None,
                "Niet waar, en dat is een van de grote open vragen van de zonnefysica. De corona "
                "is één tot drie miljoen graden, dus honderden keren heter dan het oppervlak "
                "eronder, en niemand weet precies hoe ze zo warm wordt.",
                "Let op het woord fusie. In een kerncentrale op aarde gebeurt het omgekeerde, "
                "splitsing van zware kernen; de zon smelt lichte kernen samen, en dat levert veel "
                "meer energie per kilo.",
            ],
        ),
        dict(
            aanpak="Vier verschijnselen, van binnen naar buiten en van de zon naar ons: een vlek "
                   "op het oppervlak, een lus erboven, de deeltjesstroom door de ruimte, en wat "
                   "die deeltjes bij ons doen. Zo hangen ze ook samen in één keten.",
            waarom=[
                "Een zonnevlek is donker omdat ze koeler is, ongeveer 4 000 in plaats van 5 500 "
                "graden. Apart zou zo'n vlek nog helder schijnen; ze lijkt zwart naast de rest.",
                "De elfjarige cyclus is nuttig om te weten: rond het maximum zijn er meer "
                "zonnestormen, en dus meer poollicht en meer risico voor satellieten.",
                "Noem er twee van de genoemde. Dat het stroomnet erbij hoort, verrast meestal: "
                "in 1989 viel de stroom in Québec negen uur uit door een zonnestorm.",
            ],
        ),
        dict(
            aanpak="Het ontstaan van het zonnestelsel is één verhaal in drie woorden: een wolk "
                   "die samentrekt (de zonnenevel), een schijf die zich vormt, en korrels die "
                   "samenklonteren (accretie). De vorstlijn verklaart daarna waar wat terechtkwam.",
            waarom=[
                None,
                "Het kernwoord in dit antwoord is de vorstlijn: de afstand waarbinnen het te warm "
                "was voor ijs. Binnen die lijn bleef enkel gesteente en metaal over, en daar is "
                "veel minder van dan van ijs. Vandaar vier kleine planeten binnen en vier reuzen "
                "buiten.",
            ],
        ),
        dict(
            aanpak="Vier aardse planeten binnen, vier reuzen buiten, en bij elk één kenmerk om te "
                   "onthouden. Let bij Venus op de valkuil: de heetste planeet is niet de "
                   "dichtste bij de zon, en dat heeft met haar atmosfeer te maken.",
            waarom=[
                None,
                None,
                "Venus komt tot ongeveer 465 graden, Mercurius tot 430 aan de dagzijde maar min "
                "180 in de nacht. Mercurius heeft namelijk bijna geen atmosfeer om de warmte vast "
                "te houden, en Venus een heel dikke.",
                "Het verschil zit in de samenstelling: Jupiter en Saturnus zijn vooral waterstof "
                "en helium, Uranus en Neptunus bevatten veel meer water, ammoniak en methaan, en "
                "dat noemt men ijs in de sterrenkunde.",
            ],
        ),
        dict(
            aanpak="Drie verzamelplaatsen in opklimmende afstand: de asteroïdengordel tussen Mars "
                   "en Jupiter, de Kuipergordel voorbij Neptunus, en de Oortwolk nog veel verder "
                   "als bolvormige schil. Bij de dwergplaneten hoort telkens de plaats waar ze "
                   "liggen.",
            waarom=[
                None,
                None,
                "De Oortwolk is nooit gezien: men besluit hem uit de banen van kometen die uit "
                "alle richtingen komen en duizenden jaren over één omloop doen.",
                None,
                "Let op de derde voorwaarde, want daarop valt Pluto. Hij is wel bolvormig en "
                "draait wel rond de zon, maar hij heeft zijn baan niet leeggeveegd. Sinds 2006 "
                "heet hij daarom een dwergplaneet.",
                "De staart ontstaat pas in de buurt van de zon, en hij wijst altijd van de zon "
                "weg, ook als de komeet al wegvliegt. Het is dus geen spoor dat hij achterlaat.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-bewegingen-van-de-aarde-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: gaat het over één dag of over één jaar? Rotatie is het "
                   "draaien om de eigen as en verklaart alles van dag en nacht tot het "
                   "corioliseffect. Revolutie is de omloop rond de zon en verklaart alles wat met "
                   "seizoenen te maken heeft.",
            waarom=[
                None,
                None,
                None,
                "De middernachtzon hoort bij de revolutie én bij de schuine as, niet bij de "
                "rotatie: hij bestaat enkel in juni, dus op een bepaald punt van de omloop.",
                None,
                None,
                None,
                "Reken het na: 0,25 dag per jaar maal vier jaar is één hele dag. Zonder "
                "schrikkeldag zou het na 700 jaar in juni winter zijn op de kalender, en net "
                "daarom bestaat de regel ook voor de eeuwjaren.",
            ],
        ),
        dict(
            aanpak="Vijftien graden lengte is één uur, want 360 graden in 24 uur. Reken dus het "
                   "verschil in graden, deel door vijftien, en kijk dan naar de richting: naar "
                   "het oosten is het later, naar het westen vroeger.",
            waarom=[
                "45 min 15 is 30 graden, gedeeld door 15 is 2 uur, en oostwaarts is later, dus "
                "16 uur.",
                "75 gedeeld door 15 = 5 uur. Let op de richting: westerlengte betekent vroeger, "
                "dus daar is het 5 uur eerder dan op de nulmeridiaan.",
                "Hier reken je van west naar oost, dus bijtellen: 9 + 5 = 14 uur. Zet bij zo'n "
                "oefening altijd eerst op papier welke richting je gaat.",
                "Waar, en dat is de kant die het vaakst verkeerd onthouden wordt. Van Azië naar "
                "Amerika, dus oostwaarts, krijg je een dag terug; westwaarts verlies je er een.",
                None,
            ],
        ),
        dict(
            aanpak="Het corioliseffect wijkt af naar rechts op het noordelijk halfrond en naar "
                   "links op het zuidelijk; op de evenaar is het nul. Onthoud enkel die drie "
                   "feiten, dan kan je elk windsysteem en elke depressie zelf uittekenen.",
            waarom=[
                None,
                None,
                None,
                "Teken het mee met vier pijlen naar het middelpunt en buig ze elk naar rechts: "
                "dan zie je dat ze samen tegen de klok in gaan draaien. Op het zuidelijk "
                "halfrond draait een depressie dus met de klok mee.",
            ],
        ),
        dict(
            aanpak="De schuine as van 23,5 graden verklaart de seizoenen, en de vier vaste data "
                   "verklaren waar de zon loodrecht staat. Let op de grote valkuil: de afstand "
                   "tot de zon is niet de reden van de seizoenen.",
            waarom=[
                None,
                "Merk op dat 23,5 graden terugkomt in de keerkringen en dat 90 min 23,5 de "
                "poolcirkels op 66,5 graden geeft. Die drie getallen hangen dus aan elkaar vast.",
                "Niet waar, en het is zelfs omgekeerd: in januari staat de aarde het dichtst bij "
                "de zon. Dat de afstand het niet is, bewijst ook het zuidelijk halfrond, waar het "
                "in juni winter is terwijl de afstand dezelfde is.",
                "Noem beide redenen: een hogere zonnestand én een langere dag. De hogere stand "
                "betekent dat dezelfde bundel licht op een kleiner oppervlak valt, en dus meer "
                "warmte per vierkante meter.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="De middaghoogte van de zon reken je met één formule: 90 min je breedte, en "
                   "dan de helling erbij of eraf. Bij 21 juni plus 23,5 graden, bij 21 december "
                   "min 23,5 graden, in maart en september niets.",
            waarom=[
                None,
                "Reken mee: 39 + 23,5 = 62,5 graden. Dat is de hoogste stand van het jaar bij "
                "ons, en nog altijd geen 90 graden; de zon staat in België nooit loodrecht.",
                "39 − 23,5 = 15,5 graden. Dat lage getal verklaart de lange schaduwen en de "
                "zwakke opwarming in december: het licht valt heel schuin binnen.",
                "Let op de twee delen van het antwoord. De zonnestand hangt enkel van de breedte "
                "en de datum af, dus die is gelijk; het klimaat hangt ook van de zee af, en de "
                "zee warmt traag op en koelt traag af.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-maan-getijden-en-verduisteringen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee omlooptijden om uit elkaar te houden: 27,3 dagen ten opzichte van de "
                   "sterren en 29,5 dagen van nieuwe maan tot nieuwe maan. Het verschil komt "
                   "doordat de aarde zelf verder schuift; dat is dezelfde gedachte als bij de "
                   "sterrendag en de zonnedag.",
            waarom=[
                None,
                "Dit is de maand die je op de kalender ziet: de schijngestalten herhalen zich elke "
                "29,5 dagen, en daar komt het woord maand van.",
                "Reken het ruw na: de aarde legt in die 27 dagen ongeveer 27 graden van haar "
                "baan af, en de maan moet die 27 graden nog bijhalen. Dat kost ongeveer twee "
                "dagen, en zo kom je van 27,3 aan 29,5.",
                "Niet waar, en dat is de valkuil van dit hoofdstuk. De maan draait wél om haar "
                "as, maar precies even snel als ze rond de aarde gaat. Daarom zien we altijd "
                "dezelfde kant.",
                "Gebonden rotatie is geen toeval: de getijdenkrachten van de aarde hebben de maan "
                "in die stand vastgezet, en dat gebeurt bij veel manen in het zonnestelsel.",
            ],
        ),
        dict(
            aanpak="De schijngestalten zijn niets anders dan de hoek waaronder wij de "
                   "verlichte helft zien. Leg bij elke stand de drie lichamen op een rij: staat "
                   "de maan tussen aarde en zon, dan is het nieuwe maan; staat de aarde in het "
                   "midden, dan is het volle maan.",
            waarom=[
                None,
                None,
                None,
                "Let erop dat de maan bij nieuwe maan niet in de schaduw van de aarde zit, al "
                "wordt dat vaak gedacht. De zon beschijnt gewoon de andere helft, en die keert ze "
                "van ons af.",
            ],
        ),
        dict(
            aanpak="Getijden komen van twee waterbergen: één aan de maanzijde en één aan de "
                   "overzijde. Daardoor is er twee keer hoogwater per etmaal van de maan. "
                   "Datzelfde beeld verklaart springtij en doodtij: staan zon en maan op één "
                   "lijn, dan tellen hun krachten op.",
            waarom=[
                "Die 24 uur en 50 minuten is het etmaal van de maan: ze komt elke dag ongeveer "
                "vijftig minuten later op. Daarom schuift het uur van het hoogwater elke dag mee.",
                "Springtij bij nieuwe en volle maan, doodtij bij de kwartieren. Onthoud het aan de "
                "lijn: op één lijn werken zon en maan samen, in een rechte hoek werken ze tegen "
                "elkaar.",
                "Dit is het moeilijkste van de bundel. De sleutel is de tweede zin: de maan trekt "
                "ook aan de aarde zelf. Aan de verre kant wordt de aarde dus onder het water "
                "weggetrokken, en daar blijft een tweede berg over.",
                "De zon is veel zwaarder maar ook veel verder, en bij getijden telt vooral het "
                "verschil in trekkracht over de breedte van de aarde. Daarom haalt de zon maar "
                "ongeveer de helft van het effect van de maan.",
            ],
        ),
        dict(
            aanpak="Houd de twee verduisteringen uit elkaar aan wat er in het midden staat. Bij "
                   "een zonsverduistering staat de maan in het midden, dus is het nieuwe maan; "
                   "bij een maansverduistering staat de aarde in het midden, dus is het volle "
                   "maan.",
            waarom=[
                None,
                None,
                None,
                "Dit is de vraag waar het hoofdstuk om draait. De maanbaan helt ongeveer vijf "
                "graden, dus de maan zit meestal net boven of net onder de schaduwlijn. Enkel in "
                "de twee knooppunten waar de banen kruisen, kan er een verduistering zijn.",
                "Waar, en daarom is een totale zonsverduistering zo'n zeldzaam schouwspel op één "
                "plaats: de kernschaduw is een smalle baan die over de aarde schuift, terwijl een "
                "maansverduistering tegelijk zichtbaar is voor het hele nachtelijke halfrond.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-opbouw-van-de-atmosfeer-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vier lagen van onder naar boven: troposfeer, stratosfeer, mesosfeer, "
                   "thermosfeer. Onthoud ze aan de temperatuur, want die wisselt per laag van "
                   "richting: dalen, stijgen, dalen, stijgen. De grenzen liggen rond 12, 50 en "
                   "85 km.",
            waarom=[
                "Dat de temperatuur in de stratosfeer stijgt, komt door de ozonlaag: die neemt "
                "uv-straling op en warmt daardoor op. Zo hangen de twee dingen die je van die "
                "laag moet kennen aan elkaar.",
                "Een verkeersvliegtuig vliegt op ongeveer 10 tot 12 km, dus net op de grens. De "
                "reden is praktisch: boven de troposfeer is er geen bewolking en minder "
                "turbulentie, en de ijle lucht geeft minder weerstand.",
                None,
            ],
        ),
        dict(
            aanpak="Met 0,65 graden per 100 meter reken je altijd in twee stappen: eerst het "
                   "hoogteverschil gedeeld door 100, dan maal 0,65. Klim je, dan trek je af; daal "
                   "je, dan tel je bij. Wil je de hoogte uit een verschil halen, dan deel je door "
                   "0,65 en maal 100.",
            waarom=[
                "2000 gedeeld door 100 is 20, maal 0,65 is 13 graden. Dus 18 − 13 = 5 °C.",
                "Hier moet je bijtellen, want je daalt: 30 × 0,65 = 19,5, en −4 + 19,5 = 15,5 °C. "
                "De richting is het enige waar je op moet letten.",
                "10 gedeeld door 0,65 = 15,4, maal 100 is ongeveer 1 540 m. Toets het omgekeerd: "
                "15,4 × 0,65 is inderdaad 10 graden.",
                "1 200 gedeeld door 100 maal 0,65 = 7,8 °C. Let op de laatste woorden van het "
                "antwoord: als al de rest gelijk zou zijn. In werkelijkheid speelt ook de zee "
                "mee, en die maakt de kuststad in de winter juist zachter.",
            ],
        ),
        dict(
            aanpak="Ken de vier aandelen uit het hoofd: 78, 21, 0,9 en 0,04 procent. En houd de "
                   "twee ozons uit elkaar aan hun plaats: hoog in de stratosfeer is ozon een "
                   "schild, laag bij de grond is het luchtvervuiling.",
            waarom=[
                "Merk op dat die vier samen al bijna honderd procent zijn. Waterdamp staat er "
                "niet bij omdat het aandeel ervan sterk wisselt, van bijna niets tot enkele "
                "procent.",
                "Het punt is dat een aandeel niets zegt over het effect. Stikstof en zuurstof "
                "nemen warmtestraling bijna niet op, CO2 wel, dus die 0,04 procent doet bijna al "
                "het werk, samen met waterdamp en methaan.",
                "Hetzelfde molecuul, twee tegengestelde rollen: dat is het hele punt van deze "
                "lijn. Men spreekt daarom van goede ozon boven en slechte ozon beneden.",
            ],
        ),
        dict(
            aanpak="Albedo is het deel van het zonlicht dat weerkaatst wordt. Licht en wit "
                   "weerkaatsen veel, donker weinig, en water het minst van al. De orde volgt dus "
                   "de kleur: sneeuw, zand, beton, bos, oceaan.",
            waarom=[
                "Verse sneeuw haalt tot 0,9, de oceaan ongeveer 0,06. Dat is bijna het hele "
                "bereik, en daarom weegt juist ijs zo zwaar in het klimaat.",
                None,
                "Dit heet een versterkende terugkoppeling, en het is het belangrijkste begrip van "
                "de reeks. Het gevolg versterkt zijn eigen oorzaak, en daardoor gaat de opwarming "
                "in de poolgebieden twee tot drie keer sneller dan gemiddeld.",
            ],
        ),
        dict(
            aanpak="Vier factoren bepalen de temperatuur van een plaats: de breedte, de hoogte, "
                   "de afstand tot de zee en de bebouwing. Zoek bij elk paar welke van die vier "
                   "verschilt, want de andere drie zijn dan ongeveer gelijk gehouden.",
            waarom=[
                "Let op het tweede paar: in januari is de kust warmer, in juli juist koeler. De "
                "zee dempt in beide richtingen, dus je moet altijd het seizoen meelezen.",
                None,
                None,
                "Twee van de genoemde volstaan. Wat ze gemeen hebben, is dat ze de stad minder "
                "warmte laten opslaan of meer laten verdampen. Een boom koelt dubbel: hij geeft "
                "schaduw en verdampt water.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-luchtdruk-en-winden-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Alles bij hoge en lage druk volgt uit één ding: de richting waarin de lucht "
                   "beweegt. Bij lage druk stijgt ze, en stijgende lucht koelt af en geeft "
                   "wolken en regen. Bij hoge druk daalt ze, en dalende lucht wordt warmer en "
                   "droger, dus helder weer.",
            waarom=[
                "Let op de laatste twee lijnen. Aan de grond stroomt de lucht naar een lage druk "
                "toe en waaiert ze bij een hoge druk uiteen; in de hoogte is het net omgekeerd. "
                "Zo is de kringloop rond.",
                "1013 hPa is ook het getal waarmee elke hoogtemeter ingesteld wordt. Boven 1020 "
                "spreken we van een hoog, onder 1000 van een diepe depressie.",
                "Waar, en dat is hoge druk in de winter: geen wolken, dus koelt de grond 's "
                "nachts sterk af, en de vochtige lucht blijft onder een inversie gevangen. Hoge "
                "druk geeft dus niet altijd zonnig weer.",
                "Noem de hele keten: stijgen, afkoelen, dauwpunt, condensatie op "
                "condensatiekernen, wolken. Wie enkel zegt dat de lucht stijgt, heeft de helft "
                "van het antwoord.",
            ],
        ),
        dict(
            aanpak="Een isobaar werkt als een hoogtelijn, maar voor luchtdruk. Dicht bij elkaar "
                   "betekent een steile drukhelling en dus veel wind, net zoals dichte "
                   "hoogtelijnen een steile berg betekenen.",
            waarom=[
                None,
                "Dit is het nuttigste dat je van een weerkaart kan lezen. De afstand tussen de "
                "isobaren geeft de windkracht, nog voor je naar de pijlen kijkt.",
                "De drukgradiëntkracht is de enige kracht die de lucht in beweging zet; coriolis "
                "en wrijving veranderen daarna alleen de richting, niet de aandrijving.",
                "Noem alle drie de krachten: druk, coriolis en wrijving. Zonder wrijving zou de "
                "wind precies langs de isobaren waaien; door de wrijving aan de grond kruist hij "
                "ze onder een hoek van ongeveer 20 tot 30 graden, en net daardoor kan hij een "
                "depressie binnenlopen.",
            ],
        ),
        dict(
            aanpak="De drukgordels wisselen af van de evenaar naar de pool: laag, hoog, laag, "
                   "hoog, dus op 0, 30, 60 en 90 graden. Onthoud ze aan het weer dat ze geven: "
                   "regenwoud, woestijn, wisselvallig, poolwoestijn.",
            waarom=[
                "Merk op dat 0 en 60 graden lage druk hebben en dus nat zijn, en 30 en 90 hoge "
                "druk en dus droog. De poolgebieden zijn daarom woestijnen, al liggen ze vol "
                "ijs: er valt bijna geen neerslag.",
                "Dit is de hele cel van Hadley in één antwoord: opstijgen aan de evenaar, vocht "
                "afgeven, en droog neerdalen rond 30 graden. Daar liggen de Sahara, de Arabische "
                "woestijn, de Kalahari en de Australische woestijnen.",
                "De ITCZ schuift met de zon mee, in juli naar het noorden en in januari naar het "
                "zuiden. Net die beweging maakt het regenseizoen in de tropen.",
            ],
        ),
        dict(
            aanpak="Houd twee soorten winden uit elkaar: de grote, vaste winden van de "
                   "drukgordels (passaat, westenwind, straalstroom) en de plaatselijke winden die "
                   "van het verschil tussen land en zee komen (zeewind, landwind, moesson). Die "
                   "laatste drie werken alle op hetzelfde principe.",
            waarom=[
                "Dat de passaat noordoost heet, komt van coriolis: de lucht gaat van 30 graden "
                "naar de evenaar en buigt naar rechts af. Een wind wordt altijd genoemd naar de "
                "richting waaruit hij komt.",
                None,
                "De zeewind, de landwind en de moesson zijn hetzelfde verschijnsel op drie "
                "schalen: per dag aan de kust, en per seizoen voor een heel continent. Leer er "
                "dus één goed en de andere volgen.",
                "De moesson is de zeewind in het groot: in de zomer warmt het Aziatische "
                "vasteland veel sterker op dan de oceaan, en dus stroomt vochtige zeelucht toe. "
                "In de winter is het continent kouder en keert de stroom om.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-neerslag-en-de-kringloop-van-het-water-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De kringloop is een kring van vaste woorden: verdamping en transpiratie "
                   "omhoog, condensatie en neerslag omlaag, en dan infiltratie of afstroming. "
                   "Houd die laatste twee goed uit elkaar, want daarop komt bijna elke vraag "
                   "over de stad terug.",
            waarom=[
                "Verdamping en transpiratie zijn hetzelfde verschijnsel met een andere bron: het "
                "oppervlak of de plant. Samen heet dat evapotranspiratie, en bij een bos is dat "
                "deel groot.",
                None,
                "Dit is de reden waarom een stad na een onweer onder water staat. Reken het ruw "
                "na: een weide laat het grootste deel infiltreren, asfalt bijna niets, dus komt "
                "hetzelfde buitje in een paar minuten in de beek in plaats van in een paar dagen.",
            ],
        ),
        dict(
            aanpak="Het dauwpunt is de temperatuur waarbij de lucht vol zit. Warme lucht kan meer "
                   "damp bevatten dan koude, dus afkoelen brengt de lucht altijd naar haar "
                   "dauwpunt. Daar komt elke vorm van condensatie uit: wolken, mist, dauw en de "
                   "ruit in de badkamer.",
            waarom=[
                None,
                None,
                "Zonder condensatiekernen zou de damp niet condenseren, ook niet onder het "
                "dauwpunt. Daarom werkt het bezaaien van wolken met zoutkristallen, en daarom "
                "komt er boven een stad soms meer neerslag.",
                "Leer de vier wolken aan twee kenmerken: hoog of laag, en in lagen of gestapeld. "
                "Cirrus is hoog en ijl, stratus laag en vlak, cumulus gestapeld, cumulonimbus de "
                "reus met het aambeeld bovenaan.",
                "Dit is hetzelfde verschijnsel als een wolk, in het klein. En het is ook de reden "
                "dat je in de winter je brillenglazen ziet aanslaan als je binnenkomt.",
            ],
        ),
        dict(
            aanpak="Eén millimeter neerslag is één liter per vierkante meter: dat maakt elke "
                   "rekening eenvoudig. Liters zijn millimeters maal de oppervlakte, en "
                   "millimeters zijn liters gedeeld door de oppervlakte.",
            waarom=[
                "18 × 60 = 1 080 liter. Dat is meer dan drie regentonnen, en het verklaart waarom "
                "een afvoerbuis van een dak zo snel vol staat.",
                "300 gedeeld door 25 = 12 mm. Een flinke zomerbui levert dus al een volle ton.",
                "780 gedeeld door 12 = 65 mm. Let op dat dit een gemiddelde is: bij ons valt er in "
                "december ongeveer het dubbele van wat er in april valt.",
                "Niet waar. Tegen een muur vangt de meter te veel of te weinig op, want de muur "
                "stuurt de wind en houdt regen af. Een regenmeter staat vrij, op ongeveer anderhalve "
                "meter en op minstens twee keer de hoogte van wat er in de buurt staat.",
            ],
        ),
        dict(
            aanpak="Drie soorten regen, en bij elk een eigen oorzaak van het opstijgen: een berg "
                   "duwt de lucht omhoog, de warme grond laat ze zelf opstijgen, of een front "
                   "schuift ze over koude lucht. Zoek dus in de situatie wat de lucht omhoog "
                   "brengt.",
            waarom=[
                "Onthoud ze aan de tijd die ze duren: convectieve regen is kort en fel, een "
                "onweersbui; frontale regen duurt uren en is gelijkmatig; stuwingsregen valt "
                "altijd aan dezelfde kant van het gebergte.",
                "De regenschaduw is de keerzijde van stuwingsregen: de lucht is haar vocht aan de "
                "windzijde kwijtgespeeld en daalt droog weer af. Zo ligt de woestijn van Nevada "
                "achter de Sierra Nevada en de Po-vlakte in de schaduw van de Alpen.",
                "Drie van de genoemde volstaan, en het mooiste is dat ze samen alle woestijnen "
                "verklaren: de ene door de drukgordel, de andere door een regenschaduw, de derde "
                "door een koude zeestroom.",
                "Boven koud water verdampt weinig, en koude lucht boven warmer land stijgt niet "
                "op. Daarom is de Atacama de droogste woestijn van de wereld: in sommige stations "
                "is er in jaren geen meetbare regen gevallen, al staat er wel vaak kustmist.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-klimaatgebieden-biomen-en-zeestromen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: gaat het over één moment of over een gemiddelde van jaren? "
                   "Weer is wat er nu gebeurt, klimaat is het gemiddelde over dertig jaar. Ook "
                   "drie dagen regen blijft weer, hoe lang het ook aanvoelt.",
            waarom=[
                None,
                None,
                "Dit is de klassieke valkuil: lang weer wordt geen klimaat. Omgekeerd zegt één "
                "koude winter niets over de opwarming, en net daarom is die periode van dertig "
                "jaar afgesproken.",
                None,
            ],
        ),
        dict(
            aanpak="Een bioom volgt uit twee gegevens: de temperatuur en de neerslag. Bij elk "
                   "bioom hoort een aanpassing van de planten, en daar vraagt de tabel naar: "
                   "bladverlies bij droogte, kleine leerachtige blaadjes in de Middellandse Zee, "
                   "naalden bij kou.",
            waarom=[
                "Merk op dat de aanpassing telkens hetzelfde doel heeft: water vasthouden of kou "
                "overleven. Een naald verliest minder water dan een blad, en een leerachtig "
                "blaadje verdampt bijna niet.",
                "Noem beide redenen. Het korte groeiseizoen is er één, de permafrost de andere: "
                "een boom heeft diepe wortels nodig en die kunnen in bevroren grond niet. Daarom "
                "ligt de boomgrens waar hij ligt.",
                None,
            ],
        ),
        dict(
            aanpak="Een warme zeestroom brengt zachte, vochtige lucht; een koude stroom brengt "
                   "droogte en mist. Zoek bij elke kust dus eerst of de stroom van de evenaar of "
                   "van de pool komt, want dat beslist het klimaat van die kust.",
            waarom=[
                "Let op het verschil tussen mist en regen bij een koude stroom. De lucht boven "
                "koud water wordt onderaan afgekoeld tot onder het dauwpunt, dus ontstaat er "
                "mist; maar ze stijgt niet op, en zonder opstijgen is er geen regen.",
                "Reken het verschil na: Bergen ligt vijftien breedtegraden noordelijker en is in "
                "januari toch zachter. Dat is het sterkste bewijs dat breedte alleen een klimaat "
                "niet verklaart.",
            ],
        ),
        dict(
            aanpak="De thermohaliene circulatie heeft haar naam van haar twee motoren: thermo "
                   "voor warmte en halien voor zout. Koud en zout water is zwaar en zinkt, en dat "
                   "zinken trekt de hele lopende band op gang. Elke vraag in deze reeks gaat "
                   "terug op dat ene punt.",
            waarom=[
                None,
                "Dat het water juist daar zinkt, komt doordat het er zowel koud als extra zout "
                "is: bij het bevriezen van zee-ijs blijft het zout in het water achter.",
                "Let op de laatste zin van het antwoord. Het is niet de koude die het water doet "
                "zinken maar de dichtheid, en zoet smeltwater verlaagt die dichtheid. Daarom is "
                "juist zoetwater een rem op een stroming die door kou wordt aangedreven.",
                "Niet waar, en dat is de reden waarom deze circulatie in het nieuws komt. Ze "
                "brengt warm water naar het noordoosten van de Atlantische Oceaan; valt ze weg, "
                "dan worden onze winters juist veel kouder, terwijl de aarde als geheel opwarmt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-weer-in-europa-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de twee fronten uit elkaar aan de helling. Een warmtefront is flauw: de "
                   "warme lucht glijdt traag omhoog, dus brede wolkenlagen en urenlange regen. "
                   "Een koufront is steil: de koude lucht duwt de warme snel omhoog, dus hoge "
                   "buienwolken en een korte, felle bui.",
            waarom=[
                "Let op de orde van de wolken bij een warmtefront: eerst cirrus, dan steeds lager "
                "en dikker. Dat is het nuttigste weerteken dat je zelf kan zien, want die "
                "sluierwolken komen uren voor de regen.",
                "Een occlusie is het einde van een depressie: het koufront haalt het warmtefront "
                "in, de warme sector wordt van de grond getild en de depressie vult zich op.",
                None,
            ],
        ),
        dict(
            aanpak="Een luchtsoort krijgt twee namen: waar ze gevormd is (maritiem of "
                   "continentaal) en hoe koud ze is (polair of tropisch). Zoek dus in de "
                   "omschrijving het vocht, dat geeft het eerste woord, en de temperatuur, dat "
                   "geeft het tweede.",
            waarom=[
                "Merk op dat maritiem altijd vochtig betekent en continentaal altijd droog, en "
                "dat die twee ook het dagelijkse verschil in België maken: westenwind geeft "
                "wolken, oostenwind geeft droge kou of droge hitte.",
                "Let op de laatste zin van het antwoord: weinig vocht betekent weinig wolken, en "
                "zonder wolken kan de zon de lucht nog verder opwarmen. Een hittegolf heeft dus "
                "zowel een warme herkomst als een droge lucht nodig.",
            ],
        ),
        dict(
            aanpak="Een depressie trekt in een vaste orde voorbij: eerst sluierwolken, dan het "
                   "warmtefront met lange regen, dan de warme sector, dan het koufront met buien, "
                   "en daarna opklaringen. Ken die vijf stappen en je kan een hele dag weer "
                   "voorspellen.",
            waarom=[
                "Merk op dat het twee keer regent met iets grijs maar droog ertussen. Wie na het "
                "warmtefront denkt dat het gedaan is, wordt door het koufront verrast.",
                None,
            ],
        ),
        dict(
            aanpak="Op een weerkaart lees je drie dingen: de letters H en L, de fronten met hun "
                   "symbolen, en de afstand tussen de isobaren. De driehoekjes van een koufront "
                   "en de halve bollen van een warmtefront wijzen altijd in de richting waarin "
                   "het front beweegt.",
            waarom=[
                None,
                None,
                None,
                "1028 hPa is hoge druk en wijd uit elkaar liggende isobaren betekenen weinig "
                "wind. Samen is dat een blokkerend hoog: rustig en droog, in de zomer zonnig en "
                "in de winter met mist of nachtvorst.",
                "Dit is het chaosbegrip, en het antwoord mag je in gewone woorden zetten: een "
                "kleine onzekerheid in de meting van vandaag groeit elke dag uit. Daarom werken "
                "weerdiensten met een hele reeks berekeningen naast elkaar en geven ze een kans "
                "in procent in plaats van één uitkomst.",
                "De straalstroom stuurt niet enkel waar de depressies gaan maar ook hoe snel. Ligt "
                "hij ver naar het zuiden, dan krijgen wij koude lucht; buigt hij om in een lus, "
                "dan blijft hetzelfde weer wekenlang hangen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-opbouw-van-de-geosfeer-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Er zijn twee indelingen van de aarde door elkaar, en dat is net wat deze "
                   "reeks test. Korst, mantel en kern gaan over waaruit het gesteente bestaat; "
                   "lithosfeer en asthenosfeer gaan over of het stijf of kneedbaar is. Zoek dus "
                   "in de naam: eindigt ze op -sfeer en gaat het over buigen, dan is het de "
                   "tweede indeling.",
            waarom=[
                None,
                None,
                None,
                None,
                "Dit is het hart van de reeks. De lithosfeer is korst plus het bovenste stijve "
                "stuk mantel, dus ze loopt dwars door de chemische indeling heen. Precies "
                "daarom kan men niet zeggen hoe diep de lithosfeer gaat door naar de korst te "
                "kijken.",
            ],
        ),
        dict(
            aanpak="Houd één regel vast: een P-golf is een duwgolf en kan door alles, een S-golf "
                   "is een schuifgolf en kan niet door een vloeistof. Daarmee kan je elke vraag "
                   "van deze reeks beantwoorden, ook die over de kern.",
            waarom=[
                "De P van primair helpt om te onthouden dat ze eerst aankomt. Een seismograaf "
                "ziet dus altijd twee aankomsten, en uit het verschil ertussen kan men de "
                "afstand tot het epicentrum berekenen.",
                "Dit is een mooi voorbeeld van onrechtstreeks meten: niet de kern zelf is "
                "gemeten maar de schaduw die ze maakt. Noem in je antwoord zeker de "
                "schaduwzone, want dat is het bewijs.",
                None,
            ],
        ),
        dict(
            aanpak="De twee soorten korst verschillen op vier punten: dikte, gesteente, "
                   "dichtheid en leeftijd. Onthoud één koppel en de rest volgt: oceanische korst "
                   "is dun maar zwaar, continentale korst is dik maar licht.",
            waarom=[
                None,
                "Let erop dat het om dichtheid gaat en niet om dikte. De oceanische korst is "
                "veel dunner en toch degene die wegduikt, juist omdat ze zwaarder is per "
                "kubieke centimeter.",
                "Dit sluit aan bij de vorige vraag: oceanische korst wordt aan een rug gemaakt "
                "en aan een trog weer opgeruimd. De oudste oceaanbodem is dan ook maar ongeveer "
                "200 miljoen jaar oud, terwijl continentale korst bijna vier miljard jaar kan "
                "halen.",
            ],
        ),
        dict(
            aanpak="Isostasie is evenwicht door drijven, net als een ijsblok in water: hoe "
                   "hoger het boven het water uitkomt, hoe dieper het eronder zit. Een gebergte "
                   "heeft dus een wortel, en wordt er gewicht weggehaald, dan komt de korst "
                   "omhoog.",
            waarom=[
                None,
                "Dat heet de gebergtewortel. Onder de Himalaya is de korst meer dan 70 km dik, "
                "terwijl ze onder Vlaanderen ongeveer 30 km haalt.",
                "Dit is het bekendste bewijs van isostasie dat vandaag nog bezig is. Noem in je "
                "antwoord zeker dat het gesteente eronder traag vloeit, want dat verklaart "
                "waarom het nog duurt terwijl het ijs al tienduizend jaar weg is.",
                "Reken na: 1 cm per jaar maal 100 jaar is 100 cm, dus 1 meter per eeuw. Dat is "
                "weinig per jaar en veel op de schaal van een mensenleven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-platentektoniek-en-reliefvorming-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Elk bewijs van Wegener volgt hetzelfde patroon: iets dat vandaag ver van "
                   "elkaar ligt, hoort bij elkaar. Zeg bij elke vaststelling dus niet enkel dat "
                   "de continenten bewogen zijn, maar wat precies ooit één geheel was: één kust, "
                   "één leefgebied, één gebergte, één ijskap.",
            waarom=[
                None,
                None,
                "Dit is het punt dat Wegener zelf het zwaarst woog: hij kon de beweging zien maar "
                "niet verklaren. Een goed idee zonder motor wordt niet geloofd, en dat is geen "
                "domheid van zijn tijdgenoten maar gewoon wetenschap.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke plaatrand twee dingen: bewegen de platen naar elkaar toe, "
                   "van elkaar weg of langs elkaar, en wat voor korst botst er. Naar elkaar toe "
                   "met oceanische korst erbij geeft een trog en vulkanen; twee continenten geeft "
                   "een plooiingsgebergte zonder vulkanen; langs elkaar geeft enkel bevingen.",
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
                "Deze oefening laat zien hoe een trage beweging over geologische tijd een "
                "oceaan kan openen.",
            ],
        ),
        dict(
            aanpak="Deze reeks gaat over reliëf dat niet aan een plaatrand hoort. Een hotspot "
                   "staat stil terwijl de plaat erover schuift, en dat laat een spoor na. Bij de "
                   "namen van de oceaanbodem helpt de diepte als ordening: plat, dan vlakte, dan "
                   "trog.",
            waarom=[
                None,
                "Dit is het sluitende bewijs dat de plaat beweegt en de warmtebron niet. Zeg in "
                "je antwoord beide helften: de hotspot blijft, de plaat schuift. Uit de afstand "
                "en de leeftijd van de eilanden kan men zelfs berekenen hoe snel de plaat gaat.",
                None,
                "11 km is diep genoeg om de Mount Everest erin te laten zakken met nog meer dan "
                "twee kilometer water erboven.",
                "Daarom kon men de platen in kaart brengen nog voor men de beweging kon meten: "
                "de bevingen en vulkanen tekenden de randen zelf uit.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-aardbevingen-en-vulkanisme-beyond"] = dict(
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
                None,
                "Dit is driehoeksmeting, net als bij gps. Eén station geeft enkel een afstand en "
                "dus een hele cirkel; drie cirkels snijden in één punt. Noem in je antwoord "
                "zeker waar die afstand vandaan komt: het tijdsverschil tussen de P- en de "
                "S-golf.",
            ],
        ),
        dict(
            aanpak="Magnitude is één getal voor de beving zelf, gemeten aan de energie; "
                   "intensiteit is wat mensen ter plaatse ondervinden en verschilt dus van "
                   "dorp tot dorp. Eén beving heeft één magnitude en tientallen intensiteiten.",
            waarom=[
                None,
                "De schaal is logaritmisch: één punt hoger is ongeveer 32 keer zoveel energie. "
                "Daarom is het verschil tussen een 5 en een 6 in het nieuws klein en in de "
                "werkelijkheid enorm.",
                "Reken na: 32 maal 32 is ongeveer 1000. Twee punten hoger is dus duizend keer "
                "zoveel energie.",
                "Noem er drie, en kies er het liefst drie van verschillende soort: één over de "
                "aarde (diepte, bodem), één over de gebouwen (bouwwijze, voorschriften) en één "
                "over de mensen (tijdstip, waarschuwing, hulpdiensten). Dat laat zien dat de "
                "schade niet enkel natuur is maar ook beleid.",
                None,
            ],
        ),
        dict(
            aanpak="Volg de weg van het gesteente van onder naar boven: magmahaard, "
                   "schoorsteen, krater. En onthoud het ene woordverschil dat vaak gevraagd "
                   "wordt: onder de grond heet het magma, boven de grond lava.",
            waarom=[
                "Dezelfde stof, twee namen, en het verschil zit enkel in waar ze is. Dat komt "
                "doordat de gassen bij het buitenkomen ontsnappen, waardoor lava zich anders "
                "gedraagt dan magma.",
                "Een caldera ontstaat als de magmahaard leegloopt en het dak erboven inzakt. De "
                "Santorini-baai en het Yellowstonebekken zijn calderas, en dat verklaart waarom "
                "een caldera veel breder is dan een krater.",
            ],
        ),
        dict(
            aanpak="Alles bij een vulkaan volgt uit één eigenschap: hoe taai de lava is. Taaie, "
                   "kiezelrijke lava geeft een steile kegel en een explosie; vloeibare lava geeft "
                   "een vlak schild en een stroom. Begin bij de lava en de rest van de tabel "
                   "volgt.",
            waarom=[
                "Merk op dat de vorm van de berg uit de lava volgt en niet omgekeerd. Taaie lava "
                "stroomt niet ver weg en stapelt zich op bij de krater, dus steil; vloeibare lava "
                "loopt kilometers ver uit, dus vlak zoals op Hawaï.",
                "Dit is de kern van de hele reeks, en de vergelijking met een fles helpt: schud "
                "je een fles met dikke siroop, dan komt er niets tot ze openspat. Noem in je "
                "antwoord de gassen, want zij maken de explosie, niet de lava zelf.",
                "Een pyroclastische stroom is de dodelijkste van de drie: hij gaat honderden "
                "kilometer per uur en is honderden graden warm. Een lahar kan ook jaren na de "
                "uitbarsting nog komen, want hij heeft enkel as en water nodig.",
            ],
        ),
        dict(
            aanpak="Twee open vragen die naar een afweging vragen. Zet bij de eerste naast de "
                   "voordelen van de grond ook het menselijke: het is hun thuis. Geef bij de "
                   "tweede maatregelen die echt uitvoerbaar zijn, van meten tot evacueren.",
            waarom=[
                "Noem er drie van verschillende soort: iets over de bodem, iets over geld, en "
                "het feit dat mensen niet zomaar verhuizen uit het dorp van hun familie. Net "
                "die laatste reden wordt in een examen vaak vergeten en is in de werkelijkheid "
                "de belangrijkste.",
                "Twee volstaan, maar laat zien dat er een keten is: eerst meten, dan "
                "waarschuwen, dan evacueren. Een meetnet zonder evacuatieplan redt niemand.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gesteenten-mineralen-en-datering-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elk gesteente hoe het gemaakt is. Uit magma dat stolt is "
                   "magmatisch, uit lagen die bezinken is sedimentair, uit een gesteente dat "
                   "onder druk en hitte veranderd is metamorf. De uitgang helpt niet, dus leer "
                   "de voorbeelden per groep.",
            waarom=[
                "Graniet en basalt zijn de twee voorbeelden die altijd terugkomen; kalksteen en "
                "zandsteen zijn de twee sedimentaire; marmer en leisteen de twee metamorfe. Met "
                "die zes namen geraak je door bijna elke vraag.",
                "Steenkool is de verrassing in de rij: het lijkt geen gesteente, maar het is "
                "ontstaan uit plantenresten die laag na laag bezonken en samengedrukt werden, en "
                "dus sedimentair.",
                "Lagen zijn het kenmerk dat je vanuit de verte ziet, in een steengroeve of in "
                "een berm. Fossielen komen er enkel in voor, want in magma dat stolt blijft "
                "niets over.",
            ],
        ),
        dict(
            aanpak="Eén regel beslist de korrelgrootte: hoe trager de afkoeling, hoe groter de "
                   "kristallen. Dieptegesteente koelt traag en is grof; uitvloeiingsgesteente "
                   "koelt snel en is fijn.",
            waarom=[
                "Dit is de belangrijkste oefening van de reeks, want ze toont dat dezelfde stof "
                "twee gesteenten kan geven. Noem in je antwoord de tijd, want dat is de enige "
                "echte reden.",
                None,
            ],
        ),
        dict(
            aanpak="Vier koppels om te kennen: kalksteen wordt marmer, klei wordt leisteen, "
                   "zandsteen wordt kwartsiet, graniet wordt gneis. Het gesteente wordt harder "
                   "en dichter, maar het smelt niet.",
            waarom=[
                None,
                "Noem beide: druk alleen of hitte alleen is niet genoeg. Daarom vind je metamorfe "
                "gesteenten in gebergten en bij een contact met magma.",
                "Niet waar, en dat is net het verschil met een magmatisch gesteente. Bij "
                "metamorfose blijft het gesteente vast en groeien de kristallen in vaste "
                "toestand om. Zou het smelten, dan kreeg je magma en nadien een magmatisch "
                "gesteente.",
            ],
        ),
        dict(
            aanpak="Relatieve datering is logica, geen meting: wat erbovenop ligt is jonger, en "
                   "wat ergens dwars door gaat is jonger dan wat het doorsnijdt. Met die twee "
                   "regels kan je een hele wand op orde zetten.",
            waarom=[
                None,
                "Dit is de doorsnijdingsregel, en je kan hem in twee richtingen gebruiken. De "
                "breuk zit ingeklemd tussen twee momenten: jonger dan wat ze stukmaakt, ouder "
                "dan wat er ongestoord over ligt.",
                "Let op beide helften van het antwoord. Kort geleefd maakt het fossiel precies "
                "in de tijd, wijd verspreid maakt het bruikbaar om lagen op verschillende "
                "plaatsen met elkaar te vergelijken.",
            ],
        ),
        dict(
            aanpak="Een halveringstijd is de tijd waarin de helft overblijft. Reken dus in "
                   "stappen van een halvering: na één de helft, na twee een kwart, na drie een "
                   "achtste. En kies de methode naar de ouderdom die je verwacht: koolstof-14 "
                   "voor duizenden jaren, uranium-lood voor miljoenen.",
            waarom=[
                None,
                "Reken na: 2 maal 5730 is 11 460 jaar, want een kwart is twee halveringen. Dat "
                "is ook ongeveer de grens van de methode, want na een tiental halveringen blijft "
                "er te weinig over om te meten.",
                "Twee redenen tegelijk: graniet heeft nooit geleefd en bevat dus geen "
                "koolstof-14, en 300 miljoen jaar is hoe dan ook duizenden halveringstijden. "
                "Koolstof-14 werkt enkel op wat ooit leefde en op hoogstens enkele tienduizenden "
                "jaren.",
                None,
                "Een eenvoudige ordening om te onthouden: eencellig, dan trilobieten en bossen, "
                "dan dinosauriërs, dan zoogdieren. De namen zelf helpen ook, want zoö betekent "
                "leven en kainos betekent nieuw.",
                "66 miljoen jaar is de grens tussen het Mesozoïcum en het Cenozoïcum, en dat is "
                "geen toeval: die uitstervingsgolf maakte plaats voor de zoogdieren.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verwering-karst-en-massatransport-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie woorden, drie plaatsen in de keten. Verwering gebeurt ter plaatse en "
                   "maakt het gesteente stuk, erosie voert het weg, sedimentatie legt het elders "
                   "neer. Vraag je dus telkens: blijft het liggen, gaat het mee, of wordt het "
                   "afgezet?",
            waarom=[
                "Let op het verschil tussen c en d bij de wind. Blaast de wind korrels tegen een "
                "rots, dan is dat erosie, want het zijn meegevoerde korrels die het werk doen. "
                "Wortels en vorst zijn verwering, want daar beweegt niets weg.",
                "Één zin volstaat, maar zet er het woord in dat het verschil maakt: ter plaatse "
                "tegenover afvoeren. Dat is ook het antwoord op bijna elke vraag van deze reeks.",
            ],
        ),
        dict(
            aanpak="Mechanisch is breken door een kracht, chemisch is veranderen van stof, "
                   "biologisch is het werk van een levend wezen. Kijk bij elke zin naar wat er "
                   "met het gesteente gebeurt: barst het, of lost het op?",
            waarom=[
                "Vorst en zoutkristallen staan er samen in, en ze werken allebei met uitzetten "
                "in een spleet: het ijs of het kristal groeit en duwt de rots verder open. Roest "
                "is chemisch, want het ijzer zelf verandert in een andere stof.",
                "Noem beide voorwaarden: warmte én water. Daarom ziet een graniet in de tropen "
                "er na duizend jaar helemaal anders uit dan dezelfde graniet in de Alpen, waar "
                "vooral de vorst werkt.",
            ],
        ),
        dict(
            aanpak="Karst is één verhaal: zuur regenwater lost kalksteen op. Alles wat je ziet "
                   "volgt daaruit, zowel wat wegvalt aan het oppervlak als wat neerslaat in een "
                   "grot. Houd stalactiet en stalagmiet uit elkaar met de letter: de t van "
                   "top hangt, de g van grond groeit omhoog.",
            waarom=[
                None,
                "Regenwater neemt koolstofdioxide op uit de lucht en uit de bodem, en wordt "
                "daardoor een zwak zuur. Daarom kan gewoon regenwater kalksteen aantasten zonder "
                "dat er iets vervuild is.",
                "Merk op dat een stalactiet en een stalagmiet precies het omgekeerde zijn van "
                "het oplossen: het water laat de kalk die het hogerop opnam hier weer achter.",
                "Dit verklaart ook de droge valleien in de Ardennen en in de Condroz. Zeg in je "
                "antwoord waar het water dan wel heen gaat, want het verdwijnt niet: het stroomt "
                "ondergronds verder tot een bron.",
            ],
        ),
        dict(
            aanpak="Zet de vier vormen op een lijn van traag naar snel: bodemkruip, "
                   "aardverschuiving, steenval, modderstroom. Het water beslist meestal de "
                   "snelheid, en de zwaartekracht doet altijd het werk.",
            waarom=[
                "Bodemkruip is de enige die je niet ziet gebeuren en wel ziet aan het gevolg: "
                "scheefgezakte muurtjes en gebogen boomstammen op een helling.",
                "Noem er vier van verschillende soort: de helling zelf, het water, het "
                "verdwijnen van de wortels, en een trilling of een ingreep van mensen. Het water "
                "is de belangrijkste, want het maakt de grond zwaarder en smeert tegelijk het "
                "glijvlak.",
                "Niet waar, en het is net omgekeerd. Wortels houden de bodem als een net vast en "
                "halen bovendien water uit de grond. Daarom is kaalkap een van de duidelijkste "
                "oorzaken van aardverschuivingen.",
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
                "Geef een duidelijk advies en hang er één argument uit de leerstof aan. Kies dan "
                "het water of de steilte, want dat zijn de twee factoren die bij 25 graden echt "
                "beslissen. Een advies zonder argument levert in een examen geen punten op.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-erosie-door-water-ijs-en-wind-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een stroombekken is alles wat naar dezelfde rivier afwatert, en de grens "
                   "ervan loopt over de hoogste lijn in het landschap. Debiet is een hoeveelheid "
                   "per tijd, dus reken je het om door met de tijd te vermenigvuldigen.",
            waarom=[
                None,
                "De waterscheiding volgt de toppen, dus op een kaart met hoogtelijnen kan je ze "
                "zelf tekenen: vanaf elke top naar de volgende top.",
                None,
                "Reken na: 45 maal 60 is 2700 m³ per minuut. Dat is meer dan een olympisch "
                "zwembad per minuut, en zo wordt een debietcijfer ineens voorstelbaar.",
            ],
        ),
        dict(
            aanpak="Een rivier doet in haar drie delen iets anders. Bovenaan erodeert ze, in het "
                   "midden vervoert en slingert ze, onderaan zet ze af. Het verval beslist alles: "
                   "veel verval geeft kracht naar beneden, weinig verval geeft slingeren en "
                   "afzetten.",
            waarom=[
                "Let op de vorm van de vallei, want dat is het snelste kenmerk: een V bovenaan, "
                "een brede vlakte in het midden en beneden. Grote keien horen bij veel kracht, "
                "fijn slib bij weinig.",
                "Dit is het hart van de hele bundel. Noem het woord verval, want daar hangt "
                "alles aan: zonder verval geen snelheid, zonder snelheid geen insnijding.",
            ],
        ),
        dict(
            aanpak="Hier draait het om één verrassing: de kleinste korrels zijn niet de "
                   "gemakkelijkste om op te nemen. Fijn zand gaat bij de laagste snelheid mee; "
                   "grind en keien zijn te zwaar en klei kleeft te vast.",
            waarom=[
                "Fijn zand is de gemakkelijkste korrel: licht genoeg om op te tillen en los "
                "genoeg om niet te plakken. Dat is ook de reden dat juist zand verstuift en wegwaait.",
                "Dit is het antwoord op de vorige vraag, in volle zinnen. Noem beide helften: "
                "klei vraagt veel kracht om op te nemen en blijft dan heel lang zweven. Daarom is "
                "een rivier troebel van klei en niet van grind.",
                "Niet waar, het is omgekeerd. Hoe trager het water, hoe fijner het materiaal dat "
                "bezinkt: de keien vallen al in de bovenloop uit, het slib pas in de monding.",
            ],
        ),
        dict(
            aanpak="In een bocht loopt het water aan de buitenkant sneller en aan de binnenkant "
                   "trager. Snel water erodeert, traag water zet af. Daarmee verklaar je de "
                   "steile oever, de zandbank en waarom een meander altijd breder wordt.",
            waarom=[
                "Dit is de motor achter een meander: de buitenbocht schuift op en de binnenbocht "
                "groeit aan, dus de bocht wordt elk jaar scherper tot ze zichzelf afsnijdt.",
                "Een hoefijzermeer is dus het einde van een meander, en het is het bewijs dat een "
                "rivier van loop verandert. In de vallei van de Maas liggen er verschillende.",
                None,
                "Dit is differentiële erosie in de praktijk. Noem beide delen: de trap die "
                "ontstaat én de uitholling onder de val, want daardoor schuift een waterval in de "
                "loop van de eeuwen stroomopwaarts op.",
            ],
        ),
        dict(
            aanpak="Elke kracht laat haar eigen spoor na. IJs geeft een U-vorm en ongesorteerd "
                   "puin, water sorteert, wind laat enkel het fijne liggen. Een U-vormige vallei "
                   "en een V-vormige vallei zijn het snelste onderscheid tussen ijs en water.",
            waarom=[
                "Let op het woord ongesorteerd bij de morene: een gletsjer duwt alles door "
                "elkaar vooruit, van stof tot keien, terwijl stromend water altijd sorteert op "
                "grootte. Löss is dan weer het fijnste, door de wind over honderden kilometers "
                "aangevoerd, en het is de reden dat Haspengouw zulke vruchtbare grond heeft.",
                "Een fjord toont twee dingen tegelijk: een gletsjer sneed de vallei uit tot onder "
                "het huidige zeeniveau, en nadien steeg de zee en liep ze onder.",
                "Noem de voorwaarde in plaats van enkel de plaats: losse, droge korrels zonder "
                "begroeiing. Daarom werkt wind ook op een akker die in de winter kaal ligt, en "
                "dat is precies waarom men er grasstroken aanlegt.",
            ],
        ),
        dict(
            aanpak="Twee lijstjes die elkaars spiegelbeeld zijn. Alles wat het water sneller "
                   "doet wegstromen vergroot de kans op een overstroming; alles wat het water "
                   "ruimte of tijd geeft verkleint ze. Houd dat ene criterium vast en je vindt "
                   "zelf nog voorbeelden.",
            waarom=[
                "Noem er drie van verschillende soort: iets over de bodem, iets over de rivier "
                "zelf en iets over waar men bouwt. Verharden is het sterkste voorbeeld, want "
                "regen die niet in de grond kan, komt binnen het uur in de beek.",
                "Merk op dat deze lijst gewoon het omgekeerde is van de vorige. Dat is geen "
                "toeval: het hele waterbeleid in Vlaanderen bestaat erin de ingrepen van de "
                "vorige eeuw terug te draaien.",
                "Het winterbed hoort bij de rivier, ook als het jaren droog blijft. Daarop "
                "bouwen betekent dat het water zijn ruimte ergens anders zoekt, meestal bij de "
                "buren stroomafwaarts.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-klimaat-doorheen-de-geologische-tijd-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een proxy is een onrechtstreekse thermometer: iets in de natuur dat het "
                   "klimaat van toen heeft opgeslagen. Vraag je bij elk archief wat er precies "
                   "bewaard is, want dat bepaalt wat je eruit kan lezen: lucht, groei, planten of "
                   "zeewater.",
            waarom=[
                "Merk op dat de ijskern het enige archief is waarin de lucht zelf bewaard bleef. "
                "De andere drie zijn onrechtstreeks: je leest er een gevolg in en leidt daaruit "
                "het klimaat af.",
                "800 000 jaar is ongeveer acht ijstijdcycli. Daardoor weten we niet alleen hoe "
                "koud het was maar ook dat CO2 en temperatuur samen op en neer gingen.",
                None,
            ],
        ),
        dict(
            aanpak="Houd twee getallen vast: 20 000 jaar geleden was het hoogtepunt van de "
                   "laatste ijstijd, en de zeespiegel stond toen ongeveer 120 meter lager. Bijna "
                   "elke vraag over die periode is daarmee te beantwoorden.",
            waarom=[
                None,
                "Dat water zat niet verdwenen maar vastgezet in het ijs op het land. Daarom is "
                "zeespiegel en ijskap altijd hetzelfde verhaal, in de ijstijd en vandaag.",
                "Noem de keten: ijs vangt water op, dus zakt de zee, dus valt de ondiepe Noordzee "
                "droog. Dat gebied heet Doggerland, en er worden nog botten en werktuigen uit "
                "opgevist.",
                None,
            ],
        ),
        dict(
            aanpak="Drie cycli in de baan van de aarde, elk met een eigen lengte: de vorm van de "
                   "baan, de helling van de as en de tolbeweging van de as. Zet in de tabel "
                   "telkens wat er beweegt en in hoeveel jaar, dan zie je het verschil meteen.",
            waarom=[
                "Een handige ordening is de duur: ongeveer 100 000 jaar, 41 000 jaar en 26 000 "
                "jaar. De helling bepaalt hoe sterk de seizoenen verschillen, de tolbeweging in "
                "welk seizoen de aarde het dichtst bij de zon staat.",
                "Dit is de kernvraag van de reeks. Noem de verdeling en de terugkoppeling: een "
                "koele zomer in het noorden laat sneeuw liggen, witte sneeuw weerkaatst meer "
                "zonlicht, en daardoor koelt het nog verder af. Zonder die versterking zouden de "
                "cycli veel te zwak zijn om een ijstijd te maken.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke factor of ze zonlicht tegenhoudt of warmte vasthoudt. "
                   "Aerosolen en wit ijs weren zonlicht en koelen af; broeikasgassen houden "
                   "warmte vast en warmen op.",
            waarom=[
                "Let op d: het is een terugkoppeling en geen oorzaak. De oceaan geeft CO2 af "
                "omdat het warmer wordt, en dat maakt het nog warmer. Zo versterkt een gevolg "
                "zijn eigen oorzaak.",
                "Zeg uitdrukkelijk dat de terugkoppeling versterkt, want dat is het woord dat "
                "gevraagd wordt. En let op: positief betekent hier niet goed maar "
                "zelfversterkend.",
                "Waar, en het verschil in duur is de les. Aerosolen van een vulkaan regenen na "
                "een jaar of twee uit de lucht; CO2 blijft eeuwen hangen. Daarom is een "
                "uitbarsting een onderbreking en een CO2-stijging een omslag.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-huidige-klimaatverandering-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de twee getallen naast elkaar: zonder broeikaseffect ongeveer 18 graden "
                   "onder nul, met broeikaseffect ongeveer 15 graden boven nul. Het natuurlijke "
                   "broeikaseffect maakt de aarde dus bewoonbaar; de vraag is enkel hoeveel we er "
                   "zelf bij doen.",
            waarom=[
                "Reken het verschil na: dat is ongeveer 33 graden die het broeikaseffect oplevert. "
                "Daarom is het broeikaseffect zelf niets slechts.",
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
                "deel ervan lost op in zeewater en vormt daar een zuur. Dat tast de schelpen en "
                "de koralen aan.",
                "Noem beide redenen, en vergeet de tweede niet: ook zonder één druppel smeltwater "
                "zou de zee stijgen, omdat warmer water uitzet. Die uitzetting levert ongeveer de "
                "helft van de stijging.",
            ],
        ),
        dict(
            aanpak="Elke waarneming in deze reeks is een vingerafdruk: ze past bij "
                   "broeikasgassen en niet bij een sterkere zon. Vraag je bij elk punt dus niet "
                   "of het warmer wordt, maar wat het uitsluit.",
            waarom=[
                "Het sterkste paar is b en c. Een sterkere zon zou de hele atmosfeer opwarmen en "
                "vooral de dagen; broeikasgassen warmen de onderste lucht op terwijl de hoge "
                "lucht afkoelt, en houden vooral de nachten warm. Dat is het verschil tussen een "
                "sterkere kachel en een dikkere deken.",
                "Geef twee argumenten van verschillende soort: één over de snelheid en één over "
                "de oorzaak. Geef ook toe wat juist is in de bewering, want het klimaat is "
                "inderdaad altijd veranderd; het is het tempo en de aanwijsbare oorzaak die het "
                "verschil maken.",
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
    ],
)

UITLEGBLADEN["oefenbundel-verstedelijking-en-ruimtegebruik-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De vier fasen volgen elkaar op in de tijd en je herkent ze aan de richting "
                   "van de verhuis. Naar de stad is urbanisatie, naar de rand suburbanisatie, "
                   "weg van de stad met bedrijven erbij desurbanisatie, en terug naar het "
                   "centrum reurbanisatie.",
            waarom=[
                "Let op het verschil tussen b en c: bij suburbanisatie verhuizen de mensen maar "
                "blijven ze in de stad werken, bij desurbanisatie vertrekken ook de werkplaatsen "
                "en de winkels. Dat tweede is wat een kern echt uitholt.",
                "Noem er twee van verschillende soort: iets dat het mogelijk maakte (de auto, "
                "goedkope grond) en iets dat men wilde (een huis met tuin, rust). Dat de overheid "
                "het bouwen buiten de stad jarenlang zelf aanmoedigde, wordt vaak vergeten en "
                "verklaart waarom Vlaanderen er anders uitziet dan Nederland.",
            ],
        ),
        dict(
            aanpak="Drie begrippen die op elkaar lijken en niet hetzelfde zijn. Ruimtebeslag is "
                   "alles wat ingenomen is, verharding is enkel het stuk onder beton of asfalt, "
                   "versnippering gaat over de stukken waarin de natuur uiteenvalt. Het eerste "
                   "is dus altijd groter dan het tweede.",
            waarom=[
                None,
                "De nevelstad is de naam voor het Vlaamse patroon als geheel: nergens echt stad "
                "en nergens echt platteland. Lintbebouwing is er één bouwsteen van.",
                "Een tuin hoort bij het ruimtebeslag en niet bij de verharding. Daarom is in "
                "Vlaanderen ongeveer een derde van de oppervlakte ingenomen terwijl de echte "
                "verharding rond de 16 procent zit.",
                "Dit is de kernvraag van de reeks. Noem wat er precies ontbreekt: niet de "
                "oppervlakte maar de verbinding. Daarom legt men ecoducten en onderdoorgangen "
                "aan, die geen vierkante meter natuur bijmaken en toch helpen.",
            ],
        ),
        dict(
            aanpak="Een stad warmt sterker op dan het platteland omdat ze warmte opslaat en "
                   "weinig verdampt. Zoek in je antwoord dus de drie soorten oorzaken: wat "
                   "warmte vasthoudt, wat ontbreekt om te koelen, en wat zelf warmte maakt.",
            waarom=[
                "Merk op dat het verschil vooral 's nachts groot is. Overdag schijnt de zon op "
                "beide, maar 's nachts geeft het platteland zijn warmte snel af terwijl het "
                "beton in de stad die nog uren uitstraalt.",
                "Noem er drie van verschillende soort, want dat laat zien dat je het mechanisme "
                "begrijpt: opslag in beton, gebrek aan groen en water, en de warmte van "
                "gebouwen en verkeer zelf.",
                "Deze vraag maakt van hitte een gezondheidsvraagstuk en geen comfortvraagstuk. "
                "Noem de mensen én de reden: bij een hittegolf stijgt het aantal overlijdens, en "
                "net de dichtstbebouwde wijken hebben het minste groen.",
            ],
        ),
        dict(
            aanpak="Drie niveaus en één plan: de gemeente geeft de vergunningen, Vlaanderen zet "
                   "de grote lijnen, en een ruimtelijk uitvoeringsplan zegt perceel per perceel "
                   "wat mag. Bij de slotvraag worden twee geldige belangen tegenover elkaar "
                   "gezet, dus geef er ook twee.",
            waarom=[
                None,
                "De bouwshift wordt ook betonstop genoemd, maar dat tweede woord is misleidend: "
                "het gaat niet over stoppen met bouwen maar over niet méér open ruimte "
                "aansnijden en dichter bouwen waar al bebouwing is.",
                "Geef beide argumenten echt hun gewicht; wie één kant afdoet als onredelijk "
                "mist het punt van de vraag. De eigenaar heeft een rechtmatige verwachting, de "
                "gemeente een rekening voor de gemeenschap. Precies daarom gaat de discussie over "
                "planschade en de vergoeding ervan.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-duurzaam-ruimtegebruik-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vier strategieën om geen nieuwe grond aan te snijden. Intensivering is meer "
                   "op dezelfde plek, hergebruik is een bestaand gebouw een nieuwe taak geven, "
                   "verweving is twee functies op één plek, tijdelijk gebruik is een plek "
                   "benutten tot er iets anders komt.",
            waarom=[
                "Let op c en e: bij verweving gaat het niet om hetzelfde gebouw maar om twee "
                "functies die samen door één ruimte bediend worden. Een speelplaats die in het "
                "weekend buurtplein is, dient twee groepen zonder één meter extra.",
                None,
                "Noem beide kanten van de rekening: wat je bespaart aan open ruimte en aan "
                "nieuwe wegen en riolering, tegenover de hogere bouwkost en de sanering. Die "
                "kosten voor de gemeenschap zijn het argument dat in een examen vaak ontbreekt.",
            ],
        ),
        dict(
            aanpak="Hier gaat het over de vraag waar de regen heen kan. Een wadi, doorlatende "
                   "klinkers en gras laten het water insijpelen; beton stuurt het naar de riool. "
                   "Bij de rekenoefening: zet millimeter regen om naar liter per vierkante meter, "
                   "want 1 mm op 1 m² is precies 1 liter.",
            waarom=[
                None,
                "Merk op dat het nergens alles of niets is behalve bij beton. Daarom helpt elke "
                "halve maatregel al: ook doorlatende klinkers nemen een flink deel weg.",
                "Reken na: de helft van 1200 m² is 600 m², en 20 mm op 600 m² is 600 maal 20 "
                "liter, dus 12 000 liter. De truc om te onthouden: 1 mm regen op 1 m² is 1 liter.",
            ],
        ),
        dict(
            aanpak="Beoordeel een plek niet op het huis maar op wat er rondom ligt. Kijk naar "
                   "vervoer, voorzieningen, veiligheid en groen. Dat is precies wat "
                   "knooppuntwaarde meet, en het is het argument waarmee je de laatste vraag "
                   "maakt.",
            waarom=[
                "Noem er vier van verschillende soort, en niet vier keer vervoer. Een gezin "
                "zonder auto heeft zowel verplaatsing als nabijheid nodig: een halte helpt niet "
                "als de school acht kilometer ver is.",
                "Geef een duidelijke keuze en drie argumenten, en zeg ook wat het alternatief "
                "kost. Dat tweede stuk is wat het antwoord sterk maakt: bouwen in het veld maakt "
                "iedereen van de auto afhankelijk en vraagt nieuwe nutsleidingen.",
                "Knooppuntwaarde is het woord waarmee de overheid deze hele afweging in één "
                "cijfer zet: hoe beter een plek ontsloten is en hoe meer voorzieningen er zijn, "
                "hoe logischer het is om daar dichter te bouwen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-landschap-lezen-beyond"] = dict(
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
                "zegt dat een landschap geen toestand is maar het resultaat van een "
                "geschiedenis.",
            ],
        ),
        dict(
            aanpak="Lees een landschap van onder naar boven en van oud naar jong: eerst het "
                   "reliëf, dan de bodem, dan het water, dan de begroeiing, dan de mens, en als "
                   "laatste de tijd. Die orde is geen afspraak maar een logica, want elke laag "
                   "verklaart de volgende.",
            waarom=[
                "Het reliëf en de bodem staan vooraan omdat ze het oudst zijn en de rest "
                "bepalen: waar het nat is, komt geen akker, en waar het steil is, komt geen "
                "dorp. De bewoning komt daarom helemaal achteraan.",
                "Noem bij zo'n vraag altijd wat het patroon oplost voor de mensen van toen. De "
                "lange smalle percelen geven elke boerderij een stuk van elk bodemtype, en het "
                "lint toont dat er niet gepland maar bijgebouwd is, huis na huis langs de "
                "bestaande baan.",
            ],
        ),
        dict(
            aanpak="Kies het beeld bij de vraag. Wil je hoogte, neem een hoogtemodel; wil je "
                   "vroeger, neem een oude luchtfoto; wil je een heel gewest in één keer, neem "
                   "een satellietbeeld; wil je laten zien hoe iets oogt, neem een schuine foto.",
            waarom=[
                "Een hoogtemodel uit lasermetingen is het sterkste van de vier, want het ziet "
                "ook wat onder de bomen ligt: oude wegen, grachten en zelfs akkergrenzen van "
                "eeuwen terug worden erop zichtbaar.",
                None,
                "Noem beide voordelen: lagen combineren en ermee rekenen. Dat tweede is wat een "
                "GIS echt onderscheidt van een kaart, want de vraag wie binnen vijfhonderd meter "
                "van een plein woont, kan je op papier niet stellen.",
            ],
        ),
        dict(
            aanpak="Systeemdenken betekent een ingreep door de sferen volgen: geosfeer, "
                   "hydrosfeer, atmosfeer, biosfeer. Zeg bij elke stap wat er verandert en noem "
                   "de sfeer, want de vraag telt de ketting en niet enkel het eindpunt.",
            waarom=[
                "Zet de drie stappen echt achter elkaar met een omdat ertussen, in plaats van "
                "drie losse gevolgen op te sommen. Dat is wat deze vraag test: het water loopt "
                "weg, dus de bodem droogt uit, dus verdampt er niets meer, dus wordt het heet.",
                None,
                "Noem de drie pijlers en geef bij elk een vraag die men ook echt kan stellen aan "
                "een verkaveling. Juist omdat die drie soms tegen elkaar in gaan, is duurzame "
                "ontwikkeling een afweging en geen vinkje.",
            ],
        ),
    ],
)
