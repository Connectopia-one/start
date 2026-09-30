# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij aardrijkskunde ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere schalen om mee te rekenen, andere situaties om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een schema
invullen, een besluit uitschrijven). Wie hier iets bijschrijft, legt het eerst
naast `../../spark/aardrijkskunde.json`.

Bij de rekenvragen over de schaal is elk antwoord nagerekend. De regel die
overal geldt: streep achter de 1 : … twee nullen weg en je hebt meters, streep
er vijf weg en je hebt kilometers.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Aardrijkskunde"
SPARK = "✨ Spark — 1ste en 2de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag: schrijf eerst de bewerking op en zet de eenheid erbij.",
    "Bij een situatie: zeg niet alleen wát je ziet, maar ook waaróm dat zo is.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-een-kaart-lezen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Een kaart lezen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat hoort erop?",
             opdracht="Vul in wat op een kaart welke naam draagt.",
             oefeningen=[
                 ("rij", [("zegt waarover de kaart gaat", "de titel"),
                          ("legt de tekens en de kleuren uit", "de legende"),
                          ("zegt hoeveel keer het gebied verkleind is", "de schaal"),
                          ("wijst aan waar het noorden ligt", "de noordpijl")],
                  "Hoe heet dit?", WW),
                 ("waar", "Een luchtfoto heeft altijd een legende.", False),
                 ("waar", "Een kaart, een luchtfoto en een satellietbeeld tonen alle drie een gebied van bovenaf.", True),
                 ("kort", "Hoe noem je een kaart van een klein gebied met veel details?", "een plan", W),
             ]),

        dict(kop="Windstreken",
             opdracht="Schrijf de windstreek voluit.",
             oefeningen=[
                 ("rij", [("tussen het noorden en het oosten", "het noordoosten"),
                          ("tussen het zuiden en het oosten", "het zuidoosten"),
                          ("tussen het noorden en het westen", "het noordwesten"),
                          ("recht tegenover het oosten", "het westen")],
                  "Welke windstreek?", WW),
                 ("open", "Je kijkt naar het westen. Wat ligt er links van je, wat rechts en wat achter je?",
                  "Links het zuiden, rechts het noorden, achter je het oosten.", 4),
                 ("kort", "Met welk toestel weet je welke kant het noorden op ligt?", "met een kompas", WW),
             ]),

        dict(kop="Rekenen met de schaal",
             opdracht="Schrijf de bewerking op en zet de eenheid erbij.",
             oefeningen=[
                 ("rij", [("1 cm op een kaart 1 : 20 000", "200 meter"),
                          ("1 cm op een kaart 1 : 75 000", "750 meter"),
                          ("1 cm op een kaart 1 : 200 000", "2 kilometer"),
                          ("1 cm op een kaart 1 : 5 000", "50 meter")],
                  "Hoeveel is dat in het echt?", WW),
                 ("kort", "Je meet 6 cm op een kaart 1 : 50 000. Hoeveel kilometer is dat?", "3 kilometer", WW),
                 ("kort", "Je meet 2,5 cm op een kaart 1 : 100 000. Hoeveel kilometer is dat?", "2,5 kilometer", WW),
                 ("kort", "Twee dorpen liggen 2 km uit elkaar. Hoeveel cm is dat op een kaart 1 : 25 000?",
                  "8 centimeter", WW),
                 ("kies", "Op welke van deze kaarten zie je van hetzelfde dorp het minste detail?",
                  ["1 : 5 000", "1 : 25 000", "1 : 250 000"], 2),
                 ("open", "Leg uit waarom je een bochtige weg niet met een rechte lat kan opmeten, en hoe je het wel doet.",
                  "Een rechte lat meet de afstand in vogelvlucht, en die is korter dan de weg zelf. Je legt een "
                  "touwtje over alle bochten en meet dat touwtje daarna in één rechte lijn.", 5),
             ]),

        dict(kop="Hoogtelijnen",
             opdracht="",
             oefeningen=[
                 ("waar", "Twee hoogtelijnen op dezelfde kaart kunnen elkaar kruisen.", False),
                 ("waar", "De hoogte op een kaart wordt geteld vanaf de zeespiegel.", True),
                 ("kort", "Je gaat van de hoogtelijn van 80 m naar die van 215 m. Hoeveel stijg je?",
                  "135 meter", WW),
                 ("kort", "Hoe heet het hoogst gelegen punt van een gebied?", "het hoogtepunt", WW),
                 ("open", "Op een kaart liggen de hoogtelijnen aan de noordkant van een heuvel dicht bijeen en "
                          "aan de zuidkant ver uit elkaar. Langs welke kant klim je het gemakkelijkst, en waarom?",
                  "Langs de zuidkant. Lijnen ver uit elkaar betekenen dat je over een langere afstand evenveel "
                  "stijgt, dus loopt het daar flauwer op.", 5),
             ]),

        dict(kop="Reliëfvormen",
             opdracht="Vul de juiste reliëfvorm in: vlakte, plateau, heuvel of berg.",
             oefeningen=[
                 ("rij", [("laag en vlak", "een vlakte"),
                          ("hooggelegen en bovenaan vlak", "een plateau"),
                          ("rond en niet zo hoog", "een heuvel"),
                          ("veel hoger en meestal steiler", "een berg")],
                  "Welke reliëfvorm?", WW),
                 ("kort", "Hoe heet de lijn in de verte waar lucht en aarde elkaar lijken te raken?",
                  "de horizonlijn", WW),
                 ("open", "Een vlakte en een plateau zijn allebei vlak bovenaan. Wat is dan het verschil?",
                  "De hoogte. Een vlakte ligt laag boven de zeespiegel, een plateau ligt hoog.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-waar-op-aarde-ben-je-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Waar op aarde ben je?",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De lijnen van het gradennet",
             opdracht="Vul in op welke breedte of lengte de lijn ligt.",
             oefeningen=[
                 ("rij", [("de evenaar", "0° breedte"),
                          ("de keerkringen", "23,5° noorder- en zuiderbreedte"),
                          ("de poolcirkels", "66,5° noorder- en zuiderbreedte"),
                          ("de nulmeridiaan", "0° lengte")],
                  "Waar ligt ze?", WL),
                 ("waar", "Alle meridianen zijn even lang.", True),
                 ("waar", "Alle breedtecirkels zijn even lang.", False),
                 ("kort", "Hoe heet de lijn ongeveer tegenover de nulmeridiaan, waar de datum verspringt?",
                  "de datumlijn", WW),
                 ("kies", "Welke breedte bestaat niet?", ["45° noorderbreedte", "90° zuiderbreedte", "120° noorderbreedte"], 2),
             ]),

        dict(kop="Coördinaten lezen",
             opdracht="Zeg van elke plaats waar ze ligt ten opzichte van de evenaar en van Greenwich.",
             oefeningen=[
                 ("rij", [("30° N, 20° O", "boven de evenaar, ten oosten van Greenwich"),
                          ("10° Z, 60° W", "onder de evenaar, ten westen van Greenwich"),
                          ("70° N, 15° W", "boven de evenaar, ten westen van Greenwich"),
                          ("40° Z, 145° O", "onder de evenaar, ten oosten van Greenwich")],
                  "Waar ligt deze plaats?", WL),
                 ("waar", "Bij coördinaten noem je eerst de lengte en daarna de breedte.", False),
                 ("kort", "Op ongeveer welke breedte ligt België?", "ongeveer 50° noorderbreedte", WL),
                 ("open", "Twee vrienden geven allebei hun woonplaats door met dezelfde coördinaten, tot op de "
                          "graad. Kan dat, en wat weet je dan?",
                  "Dat kan: op één graad nauwkeurig is een vak van tientallen kilometers breed. Precies "
                  "dezelfde plek hoeft het dus niet te zijn, maar ver uit elkaar wonen ze niet.", 5),
             ]),

        dict(kop="Absoluut of relatief?",
             opdracht="Duid aan of de zin de plaats absoluut of relatief situeert.",
             oefeningen=[
                 ("rij", [("\"Ons huis ligt achter de kerk.\"", "relatief"),
                          ("\"De vuurtoren staat op 51° N en 3° O.\"", "absoluut"),
                          ("\"Het dorp ligt tien kilometer ten zuiden van Hasselt.\"", "relatief"),
                          ("\"Het meetpunt ligt op 49° N en 6° O.\"", "absoluut")],
                  "Absoluut of relatief?", WW),
                 ("open", "Leg uit waarom \"de Kerkstraat, nummer 12\" geen goede manier is om een plaats "
                          "wereldwijd te situeren.",
                  "Omdat dezelfde straatnaam in heel veel gemeenten voorkomt. Zonder gemeente en land weet "
                  "niemand welke Kerkstraat je bedoelt; coördinaten betekenen overal ter wereld hetzelfde.", 5),
             ]),

        dict(kop="Werelddelen en oceanen",
             opdracht="",
             oefeningen=[
                 ("kort", "Welke oceaan ligt tussen Europa en Amerika?", "de Atlantische Oceaan", WL),
                 ("kort", "Door welk werelddeel loopt de evenaar?", "Afrika", W),
                 ("waar", "Antarctica is een werelddeel.", True),
                 ("open", "Noem de zeven werelddelen.",
                  "Europa, Azië, Afrika, Noord-Amerika, Zuid-Amerika, Oceanië en Antarctica.", 4),
                 ("kies", "Waar begin je in een atlas als je een stad wil opzoeken?",
                  ["bij de eerste kaart", "bij het register achteraan", "bij de inhoudstafel vooraan"], 1),
             ]),

        dict(kop="Referentiepunten",
             opdracht="Schrijf bij elk referentiepunt of het sterrenkundig, staatkundig of topografisch is.",
             oefeningen=[
                 ("rij", [("de poolcirkel", "sterrenkundig"),
                          ("de provincie", "staatkundig"),
                          ("de Maas", "topografisch"),
                          ("de keerkring", "sterrenkundig")],
                  "Welke soort?", WW),
                 ("rij", [("het Plateau van de Ardennen", "topografisch"),
                          ("de gemeente", "staatkundig"),
                          ("de Indische Oceaan", "topografisch"),
                          ("het werelddeel", "staatkundig")],
                  "Welke soort?", WW),
                 ("open", "Je staat midden in een bos zonder herkenningspunten en wil je positie tot op enkele "
                          "meters kennen. Welk hulpmiddel gebruik je, en waarom niet een kompas?",
                  "Een satellietnavigatiesysteem, want dat berekent je positie uit de signalen van satellieten. "
                  "Een kompas zegt alleen welke kant het noorden op ligt, niet waar je staat.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-lagen-van-een-landschap-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="De lagen van een landschap",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Natuurlijk of van de mens?",
             opdracht="Schrijf bij elke laag of ze natuurlijk is of door de mens gemaakt.",
             oefeningen=[
                 ("rij", [("het reliëf", "natuurlijk"),
                          ("de bebouwing", "van de mens"),
                          ("de ondergrond", "natuurlijk"),
                          ("de transportwegen", "van de mens")],
                  "Natuurlijk of van de mens?", WW),
                 ("rij", [("de vegetatie", "natuurlijk"),
                          ("de ontginning", "van de mens"),
                          ("het klimaat", "natuurlijk"),
                          ("het landgebruik", "van de mens")],
                  "Natuurlijk of van de mens?", WW),
                 ("waar", "De menselijke lagen van een landschap kunnen op enkele jaren tijd sterk veranderen.", True),
             ]),

        dict(kop="Bodem en ondergrond",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet de bovenste losse laag waarin planten hun wortels zetten?", "de bodem", W),
                 ("kort", "Welk woord gebruik je voor hoe grof of fijn de korrels van een bodem zijn?",
                  "de textuur", W),
                 ("kies", "Welke bodemsoort laat het water het moeilijkst door?", ["zand", "leem", "klei"], 2),
                 ("kort", "Noem een voorbeeld van vast gesteente in de ondergrond.",
                  "kalksteen (of zandsteen, of leisteen)", WL),
                 ("open", "In de Kempen ligt een zandbodem. Wat betekent dat voor het regenwater, en wat merk je "
                          "daaraan in de zomer?",
                  "Het regenwater zakt er snel weg, want zand heeft grove korrels. In een droge zomer staan de "
                  "planten er daardoor sneller te verdorren dan op een leem- of kleibodem.", 5),
             ]),

        dict(kop="Landbouw",
             opdracht="Schrijf bij elk bedrijf welke tak van de landbouw het is.",
             oefeningen=[
                 ("rij", [("tarwe telen op een groot veld", "akkerbouw"),
                          ("legkippen houden voor eieren", "veeteelt"),
                          ("aardbeien telen in een serre", "tuinbouw"),
                          ("een boomgaard met appelbomen", "tuinbouw")],
                  "Welke tak?", WW),
                 ("kort", "Hoe noem je een bedrijf dat én dieren houdt én gewassen teelt?",
                  "gemengde landbouw", WW),
                 ("waar", "Een serre maakt de teler minder afhankelijk van het weer buiten.", True),
             ]),

        dict(kop="Wat de mens neerzet",
             opdracht="",
             oefeningen=[
                 ("rij", [("huizen in één rij langs een gewestweg, kilometers ver", "lintbebouwing"),
                          ("een put waaruit steen of zand gehaald wordt", "een groeve"),
                          ("leidingen en kabels voor water, gas en stroom", "nutsvoorzieningen"),
                          ("grondstoffen uit de bodem of ondergrond halen", "ontginning")],
                  "Hoe heet dit?", WW),
                 ("kies", "Wat hoort NIET bij de lijninfrastructuur?",
                  ["een spoorlijn", "een hoogspanningsleiding", "een appartementsgebouw"], 2),
                 ("open", "Waarom bouwt een bedrijf zijn fabriek liever langs een kanaal dan midden in een "
                          "woonwijk? Geef twee redenen.",
                  "Eén: grondstoffen en producten raken er vlot aan en weg, want zware goederen gaan goedkoop "
                  "over water. Twee: in een woonwijk zou het lawaai en het vrachtverkeer de buren storen, en is "
                  "er geen plaats voor grote loodsen.", 5),
                 ("waar", "Toerisme verandert het landschap niet, want toeristen blijven maar even.", False),
             ]),

        dict(kop="Alles samen",
             opdracht="",
             oefeningen=[
                 ("open", "Je staat op een heuvel en ziet: akkers, een dorpje, een spoorlijn en een fabriek. "
                          "Noem bij elk van die vier welke laag van het landschap je ziet.",
                  "De akkers en de fabriek horen bij het landgebruik, het dorpje bij de bebouwing, de spoorlijn "
                  "bij de transportwegen. De fabriek hoort daarnaast ook bij het landgebruik: industrie.", 6),
                 ("open", "Leg uit waarom water als een aparte laag geteld wordt, terwijl het ook in de bodem zit.",
                  "Omdat water de andere lagen mee vormt en verandert: het slijt het reliëf uit, het voert "
                  "bodemdeeltjes aan en af, en het bepaalt wat er kan groeien.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-waarom-landschappen-verschillen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Waarom landschappen verschillen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De drie trappen",
             opdracht="Schrijf bij elke eenheid of het een laagvlakte, een laagplateau of een plateau is.",
             oefeningen=[
                 ("rij", [("de Vlaamse Laagvlakte", "laagvlakte"),
                          ("het Haspengouws Laagplateau", "laagplateau"),
                          ("het Plateau van de Ardennen", "plateau"),
                          ("de Laagvlakte van de Kust", "laagvlakte")],
                  "Welke trap?", WW),
                 ("rij", [("het Brabants Laagplateau", "laagplateau"),
                          ("het Plateau van de Hoge Venen", "plateau"),
                          ("de Kempense Laagvlakte", "laagvlakte"),
                          ("het Henegouws Laagplateau", "laagplateau")],
                  "Welke trap?", WW),
                 ("kort", "Hoe hoog ligt het Signaal van Botrange?", "694 meter", W),
                 ("waar", "De Heuvelruggen van de Condroz zijn een vlak plateau zonder hoogteverschillen.", False),
                 ("open", "Je rijdt van Oostende naar Malmedy. Beschrijf in één zin wat er onderweg met het "
                          "reliëf gebeurt, en waarom dat zo is.",
                  "Het gaat geleidelijk omhoog, van de laagvlakte aan de kust over de laagplateaus naar de "
                  "plateaus van het zuidoosten: België klimt van het noordwesten naar het zuidoosten.", 5),
             ]),

        dict(kop="Klimaat- en vegetatiezones",
             opdracht="",
             oefeningen=[
                 ("rij", [("mossen en heel lage planten, vlak bij de pool", "toendra"),
                          ("een brede gordel naaldbos in het noorden", "taiga"),
                          ("grasvlakten met verspreide bomen", "savanne"),
                          ("warm en nat het hele jaar, rond de evenaar", "tropisch regenwoud")],
                  "Welke vegetatiezone?", WW),
                 ("kort", "In welke vegetatiezone ligt België?", "het loofwoud", WW),
                 ("kort", "In welke klimaatzone ligt België?", "de gematigde zone", WW),
                 ("kies", "Waar op aarde ligt de warmste klimaatzone?",
                  ["rond de polen", "rond de evenaar", "op de keerkringen"], 1),
                 ("open", "Waarom groeien er in een woestijn zo weinig planten? En wat is het gevolg daarvan "
                          "voor het zand?",
                  "Er valt veel te weinig neerslag, dus planten krijgen te weinig water. Omdat er nauwelijks "
                  "planten staan die het zand vasthouden, heeft de wind er vrij spel en verplaatsen de duinen "
                  "zich over de jaren heen.", 6),
             ]),

        dict(kop="Waar de mensen wonen",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe noem je het aantal inwoners per vierkante kilometer?",
                  "de bevolkingsdichtheid", WL),
                 ("rij", [("de Sahara", "dunbevolkt"),
                          ("de Himalaya", "dunbevolkt"),
                          ("België", "dichtbevolkt"),
                          ("Antarctica", "dunbevolkt")],
                  "Dicht- of dunbevolkt?", WW),
                 ("open", "Noem de drie soorten gebieden die van nature dunbevolkt zijn, en zeg bij elk waarom.",
                  "Woestijnen, want er is te weinig water. Hooggebergten, want het is er te koud en te steil. "
                  "Poolgebieden, want het is er te koud.", 6),
             ]),

        dict(kop="Het samenspel van de lagen",
             opdracht="",
             oefeningen=[
                 ("waar", "De landschapsvormende lagen staan los van elkaar en beïnvloeden elkaar niet.", False),
                 ("kort", "Hoe heet de hoogte waarboven het in een gebergte te koud is voor bomen?",
                  "de boomgrens", WW),
                 ("rij", [("een leembodem", "vruchtbaar, goed voor akkerbouw"),
                          ("een natte bodem", "eerder weiland"),
                          ("een schrale zandbodem", "levert minder op per hectare")],
                  "Wat doet de landbouw ermee?", WL),
                 ("open", "Twee dorpen liggen even ver van de stad, maar het ene groeide veel sterker. Bedenk "
                          "twee verklaringen die met het landschap of de infrastructuur te maken hebben.",
                  "Bijvoorbeeld: het ene ligt aan een spoorlijn of een grote weg en het andere niet, zodat je er "
                  "vlotter raakt. Of: het ene ligt op een droge hoogte en het andere in een natte vallei waar "
                  "bouwen moeilijker is.", 6),
                 ("kort", "Hoe noem je een landschap dat de mens nauwelijks veranderd heeft?",
                  "een natuurlijk landschap", WL),
             ]),

        dict(kop="De vijf P's",
             opdracht="Schrijf bij elk voorbeeld onder welke P het vooral valt.",
             oefeningen=[
                 ("rij", [("een beekvallei beschermen", "Planet"),
                          ("een eerlijk loon betalen", "People"),
                          ("betaalbare energie voor elk gezin", "Prosperity"),
                          ("landen die samen een verdrag sluiten", "Partnership")],
                  "Welke P?", WW),
                 ("kort", "Welke P gaat over vrede?", "Peace", W),
                 ("waar", "Wat de ene P vooruithelpt, kan een andere P tegelijk schaden.", True),
                 ("open", "Waarom hoort vrede in een model over duurzaamheid?",
                  "Omdat er in een oorlog niets opgebouwd of beschermd wordt: wat er staat gaat kapot, en er is "
                  "geen rust om aan de toekomst te werken.", 4),
                 ("kort", "Wat betekent duurzaamheid in één zin?",
                  "voorzien in wat we nu nodig hebben zonder later tekort te doen", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-aarde-beweegt-en-slijt-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="De aarde beweegt en slijt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Aardbevingen",
             opdracht="",
             oefeningen=[
                 ("rij", [("het punt in de diepte waar de beweging begint", "de haard"),
                          ("het punt op het aardoppervlak recht daarboven", "het epicentrum"),
                          ("het toestel dat de trillingen optekent", "de seismograaf"),
                          ("een scheur in de aardkorst waarlangs stukken bewegen", "een breuklijn")],
                  "Hoe heet dit?", WW),
                 ("kort", "Hoe noem je een reusachtige vloedgolf na een zeebeving?", "een tsunami", W),
                 ("waar", "In België komen af en toe lichte aardbevingen voor.", True),
                 ("open", "Waarom bouwt men in een aardbevingsgebied gebouwen die kunnen meebewegen, in plaats "
                          "van extra stijve gebouwen?",
                  "Omdat een stijf gebouw de schok niet kwijt kan en daardoor scheurt of instort. Een gebouw dat "
                  "meegeeft, vangt de beweging op en blijft staan.", 5),
             ]),

        dict(kop="Vulkanen",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet het gesmolten gesteente onder de grond?", "magma", W),
                 ("kort", "En hoe heet hetzelfde gesteente als het naar buiten stroomt?", "lava", W),
                 ("kort", "Hoe heet de trechtervormige opening bovenaan een vulkaan?", "de krater", W),
                 ("waar", "Alle vulkanen op aarde barsten regelmatig uit.", False),
                 ("open", "Leg uit waarom mensen tóch in de buurt van een actieve vulkaan gaan wonen.",
                  "Omdat de bodem er op lange termijn bijzonder vruchtbaar wordt door de as en de verweerde "
                  "lava. Er valt dus veel te oogsten, en dat weegt voor veel gezinnen op tegen het risico.", 5),
                 ("kort", "Welke stad werd in het jaar 79 bedolven door de Vesuvius?", "Pompeii", W),
             ]),

        dict(kop="Verwering, erosie of sedimentatie?",
             opdracht="Schrijf bij elke zin welk van de drie het is.",
             oefeningen=[
                 ("rij", [("water bevriest in een barst en de rots springt uiteen", "verwering"),
                          ("een rivier voert zand mee naar zee", "erosie"),
                          ("aan de monding vormt zich een waaier van zand en slib", "sedimentatie"),
                          ("regenwater lost kalksteen langzaam op", "verwering")],
                  "Welk van de drie?", WW),
                 ("rij", [("de wind blaast zand tot een duin op", "sedimentatie"),
                          ("een gletsjer schuurt een dal uit", "erosie"),
                          ("de stenen van een oude muur brokkelen af", "verwering"),
                          ("op de bodem van een meer zakt slib neer", "sedimentatie")],
                  "Welk van de drie?", WW),
                 ("kort", "Hoe heet het proces waarbij water in een barst bevriest en de rots openduwt?",
                  "vorstverwering", WW),
             ]),

        dict(kop="Dalen en landvormen",
             opdracht="",
             oefeningen=[
                 ("kies", "Welke vorm krijgt een dal dat een rivier zich in een plateau insnijdt?",
                  ["een U-vorm", "een V-vorm", "een vlakke bodem met steile wanden"], 1),
                 ("kort", "Waaraan herken je een dal dat ooit door een gletsjer uitgeschuurd is?",
                  "aan de brede bodem en de steile wanden", WL),
                 ("waar", "Een rivier zet het meeste materiaal af waar ze het snelst stroomt.", False),
                 ("kort", "Hoe noem je een heuvel van zand die door de wind is opgewaaid?", "een duin", W),
                 ("kort", "Hoe noem je het afbreken van de kustlijn door de zee?", "kusterosie", WW),
                 ("open", "Waarom liggen er in kalkstreken zoals de Condroz zoveel grotten?",
                  "Omdat kalksteen door water wordt opgelost. Regenwater sijpelt in de barsten, lost de kalk "
                  "stukje bij beetje op, en laat na duizenden jaren holtes achter.", 5),
             ]),

        dict(kop="Erosie tegenhouden",
             opdracht="",
             oefeningen=[
                 ("waar", "Planten en bomen beschermen de bodem tegen erosie.", True),
                 ("open", "Een boer ploegt een helling van boven naar beneden. Wat gebeurt er bij een zware "
                          "regenbui, en wat zou hij beter doen?",
                  "Het water stroomt door de voren naar beneden en neemt vruchtbare grond mee. Ploegt hij langs "
                  "de helling in plaats van er recht op, dan werken de voren als kleine drempels die het water "
                  "tegenhouden.", 6),
                 ("open", "Waardoor is de leembodem van Haspengouw daar terechtgekomen, en hoelang geleden "
                          "ongeveer?",
                  "Door de wind, duizenden jaren geleden. Het is aangewaaid stof dat daar is blijven liggen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-weer-en-zijn-uitschieters-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Het weer en zijn uitschieters",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Meten wat het weer doet",
             opdracht="Vul het toestel en de eenheid in.",
             oefeningen=[
                 ("tabel", ["wat je meet", "waarmee", "in welke eenheid"],
                  [["de temperatuur", None, None],
                   ["de luchtdruk", None, None],
                   ["de neerslag", None, None],
                   ["de windsnelheid", None, None]],
                  "temperatuur: een thermometer, in graden Celsius. Luchtdruk: een barometer, in hectopascal. "
                  "Neerslag: een regenmeter, in millimeter. Windsnelheid: een anemometer, in kilometer per uur "
                  "of in Beaufort."),
                 ("kort", "Er viel 18 mm regen. Hoeveel liter kwam er op één vierkante meter?", "18 liter", WW),
                 ("waar", "Een noordenwind is een wind die naar het noorden waait.", False),
                 ("open", "Waarom staat de thermometer van een weerstation in een wit kastje met spleetjes?",
                  "Het wit en de wanden houden de zon weg, en de spleetjes laten de lucht door. Zo meet je de "
                  "temperatuur van de lucht en niet die van de zon op het glas.", 5),
             ]),

        dict(kop="Hoge en lage druk",
             opdracht="",
             oefeningen=[
                 ("rij", [("de lucht zakt, weinig wolken", "een hogedrukgebied"),
                          ("de lucht stijgt, wolken en regen", "een lagedrukgebied of depressie")],
                  "Welk gebied is dit?", WL),
                 ("kies", "De barometer daalt sterk. Wat mag je verwachten?",
                  ["rustig en droog weer", "wolken, wind en kans op regen", "vorst"], 1),
                 ("open", "Waarom is het op een bergtop meestal kouder dan in het dal eronder?",
                  "Omdat de lucht hoger dunner is en minder warmte vasthoudt.", 4),
             ]),

        dict(kop="Het klimatogram",
             opdracht="",
             oefeningen=[
                 ("kort", "Wat tonen de staafjes op een klimatogram?", "de neerslag per maand", WL),
                 ("kort", "En wat toont de lijn?", "de temperatuur per maand", WL),
                 ("open", "Op een klimatogram is juli de koudste maand en januari de warmste. Op welk halfrond "
                          "ligt die plaats, en hoe weet je dat?",
                  "Op het zuidelijk halfrond. Daar zijn de seizoenen omgekeerd: als het bij ons zomer is, is het "
                  "daar winter.", 5),
                 ("waar", "Sneeuw en hagel zijn ook vormen van neerslag.", True),
                 ("waar", "Het weer van morgen kan tot op het uur nauwkeurig voorspeld worden.", False),
             ]),

        dict(kop="Stormen",
             opdracht="",
             oefeningen=[
                 ("rij", [("een tropische wervelstorm boven warm zeewater", "een orkaan"),
                          ("een smalle draaiende luchtslurf onder een onweerswolk", "een tornado"),
                          ("water dat bij storm tegen de kust wordt opgestuwd", "een stormvloed"),
                          ("het rustige midden van een wervelstorm", "het oog")],
                  "Hoe heet dit?", WW),
                 ("kort", "Vanaf welke windkracht op de schaal van Beaufort spreekt men van storm?",
                  "vanaf 9", W),
                 ("waar", "Een tornado bestrijkt een veel breder gebied dan een orkaan.", False),
                 ("open", "Waarom ontstaan orkanen enkel boven warm zeewater?",
                  "Omdat warm water veel damp en energie levert. Die damp stijgt op, condenseert en geeft "
                  "daarbij de warmte af die de storm op gang houdt.", 5),
                 ("open", "Waarom is een stormvloed aan onze kust gevaarlijker als hij samenvalt met springtij?",
                  "Omdat het water bij springtij toch al hoger staat dan gewoonlijk. De opgestuwde golf komt er "
                  "dan bovenop, en dan raakt het water sneller over de dijk.", 5),
             ]),

        dict(kop="Wateroverlast",
             opdracht="",
             oefeningen=[
                 ("waar", "Verharde oppervlakken zoals wegen en parkings vergroten de kans op wateroverlast.", True),
                 ("open", "Noem drie sporen die een overstroming in een landschap achterlaat.",
                  "Een laag slib op de velden, weggespoelde wegen en bruggen, en uitgesleten geulen in de "
                  "akkers.", 5),
                 ("open", "Noem drie maatregelen die helpen tegen wateroverlast na hevige regen, en zeg wat ze "
                          "alle drie gemeen hebben.",
                  "Een overstromingsgebied naast de rivier aanleggen, regenwater laten insijpelen in plaats van "
                  "het af te voeren, en beken meer ruimte geven om te kronkelen. Ze geven het water alle drie "
                  "plaats en tijd in plaats van het weg te jagen.", 6),
                 ("kort", "Wat betekent code oranje in een weerbericht?",
                  "er wordt gevaarlijk weer verwacht", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-klimaat-verandert-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Het klimaat verandert",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Brandstoffen en gassen",
             opdracht="",
             oefeningen=[
                 ("kort", "Welke naam dragen steenkool, aardolie en aardgas samen?",
                  "fossiele brandstoffen", WL),
                 ("open", "Waarom raken fossiele brandstoffen op?",
                  "Omdat er veel sneller van verbruikt wordt dan er bij komt. Ze zijn ontstaan uit resten van "
                  "planten en dieren van miljoenen jaren geleden; nieuwe voorraad duurt dus even lang.", 5),
                 ("rij", [("koolstofdioxide", "broeikasgas"),
                          ("methaan", "broeikasgas"),
                          ("waterdamp", "broeikasgas"),
                          ("zuurstof", "geen broeikasgas")],
                  "Broeikasgas of niet?", WW),
                 ("kort", "Waar komt het methaan vandaan dat het broeikaseffect mee versterkt?",
                  "uit veeteelt, rijstvelden en stortplaatsen", WL),
                 ("kort", "Hoe heet de laag gassen rond de aarde waarin het weer zich afspeelt?",
                  "de atmosfeer of dampkring", WL),
             ]),

        dict(kop="Het broeikaseffect",
             opdracht="",
             oefeningen=[
                 ("waar", "Zonder broeikaseffect zou het op aarde gemiddeld ver onder nul zijn.", True),
                 ("waar", "Het broeikaseffect is pas ontstaan door de mens.", False),
                 ("open", "Leg in twee zinnen uit wat het versterkt broeikaseffect is.",
                  "Er zitten meer broeikasgassen in de lucht dan vroeger. Daardoor ontsnapt er minder warmte "
                  "naar de ruimte en wordt het op aarde warmer.", 5),
                 ("open", "Waarom noemt men bossen en oceanen koolstofputten, en waarom verlies je bij het "
                          "kappen van een bos twee keer?",
                  "Omdat ze koolstofdioxide uit de lucht opnemen. Kap je een bos, dan komt de koolstof die erin "
                  "zat vrij, én verdwijnt de put die hem opnam.", 6),
                 ("kort", "Waarom stoot een draaiende windmolen geen koolstofdioxide uit?",
                  "omdat er niets verbrand wordt om stroom te maken", WL),
             ]),

        dict(kop="De zeespiegel",
             opdracht="",
             oefeningen=[
                 ("open", "Noem twee redenen waarom de zeespiegel stijgt door de opwarming.",
                  "Water zet uit als het warmer wordt, en ijs dat op het land ligt smelt en loopt naar zee "
                  "(gletsjers en landijs).", 5),
                 ("waar", "Als al het drijvende zee-ijs rond de noordpool smelt, stijgt de zeespiegel daardoor "
                          "sterk.", False),
                 ("open", "Leg uit waarom drijvend zee-ijs niet meetelt voor de zeespiegel.",
                  "Drijvend ijs verplaatst al evenveel water als het zelf weegt. Smelt het, dan neemt het "
                  "precies die plaats in; er komt dus niets bij.", 5),
                 ("kort", "Hoe heet een muur of dam die het land tegen het water beschermt?", "een dijk", W),
                 ("kort", "Waarom is zeespiegelstijging voor België een probleem?",
                  "omdat de polders achter de kust heel laag liggen", WL),
             ]),

        dict(kop="Gevolgen",
             opdracht="",
             oefeningen=[
                 ("rij", [("vruchtbaar land dat stilaan woestijn wordt", "verwoestijning"),
                          ("mensen die hun streek verlaten door droogte of overstroming", "klimaatvluchtelingen"),
                          ("koraal dat verbleekt en afsterft door warm water", "koraalverbleking"),
                          ("je aanpassen aan een klimaat dat al veranderd is", "adaptatie")],
                  "Hoe heet dit?", WL),
                 ("open", "Noem drie gevolgen van klimaatverandering die men in België zelf merkt.",
                  "Drogere zomers met lage waterstanden, hevigere buien die wateroverlast geven, en meer "
                  "hittegolven dan vroeger.", 5),
                 ("waar", "Klimaatverandering treft alle landen even hard.", False),
                 ("open", "Waarom schuiven plant- en diersoorten op naar het noorden?",
                  "Omdat hun leefgebied meeschuift met de warmte: waar het vroeger te koud voor hen was, is het "
                  "nu warm genoeg.", 4),
             ]),

        dict(kop="Wat eraan te doen",
             opdracht="",
             oefeningen=[
                 ("rij", [("woningen beter isoleren", "minder uitstoten"),
                          ("een plein ontharden zodat water in de grond kan", "adaptatie"),
                          ("stroom opwekken met wind en zon", "minder uitstoten"),
                          ("een dijk verhogen", "adaptatie")],
                  "Uitstoot verminderen of adaptatie?", WL),
                 ("open", "Waarom is het in een stad op een zomerse dag warmer dan op het platteland eromheen?",
                  "Omdat steen en asfalt de warmte langer vasthouden, en omdat er weinig groen is dat water "
                  "verdampt en zo afkoelt.", 5),
                 ("open", "Iemand zegt: wat ik zelf doe telt niet mee, want de uitstoot van één gezin is te "
                          "klein. Wat antwoord je?",
                  "De uitstoot van de hele wereld is niets anders dan de optelsom van alle gezinnen, bedrijven "
                  "en landen samen. Zegt iedereen dat, dan verandert er niets; bovendien beslist wat veel mensen "
                  "doen ook wat bedrijven en overheden aanbieden.", 6),
                 ("kort", "Waarom lost geen enkel land klimaatverandering alleen op?",
                  "omdat de dampkring van de hele wereld gedeeld is", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-mens-verandert-het-landschap-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="De mens verandert het landschap",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Infrastructuur",
             opdracht="Schrijf bij elk voorbeeld of het transport- of energie-infrastructuur is.",
             oefeningen=[
                 ("rij", [("een kanaal graven", "transport"),
                          ("een windmolenpark bouwen", "energie"),
                          ("een spoorlijn verdubbelen", "transport"),
                          ("een hoogspanningslijn aanleggen", "energie")],
                  "Welke soort?", WW),
                 ("kort", "Hoe heet het geheel van masten en kabels dat stroom over lange afstanden vervoert?",
                  "het hoogspanningsnet", WL),
                 ("open", "Waarom staan windmolens vaak aan de kust of op open vlakten?",
                  "Omdat het daar harder en gelijkmatiger waait: er staan geen gebouwen of bossen die de wind "
                  "afremmen.", 4),
                 ("open", "Noem één nadeel van een autosnelweg door een natuurgebied.",
                  "Hij snijdt het leefgebied van dieren in stukken: wat vroeger één gebied was, zijn dan twee "
                  "gebieden met een barrière ertussen.", 4),
             ]),

        dict(kop="Bebouwing en ontginning",
             opdracht="",
             oefeningen=[
                 ("rij", [("een stuk grond dat in bouwpercelen verdeeld wordt", "een verkaveling"),
                          ("de afvalheuvel naast een oude steenkoolmijn", "een terril"),
                          ("delfstoffen uit de diepere ondergrond halen", "mijnbouw"),
                          ("een put waaruit steen of zand komt", "een groeve")],
                  "Hoe heet dit?", WW),
                 ("open", "De bevolking van België groeit maar traag, en toch neemt de oppervlakte bebouwing "
                          "toe. Hoe kan dat?",
                  "Omdat er steeds meer en kleinere gezinnen zijn. Meer gezinnen betekent meer woningen, ook als "
                  "er niet meer mensen wonen.", 5),
                 ("open", "Waarom liggen de oudste dorpskernen van Vlaanderen vaak op een lichte hoogte?",
                  "Omdat het daar droger was dan in de vallei. Wie kon kiezen, bouwde niet met zijn voeten in "
                  "het water.", 4),
                 ("waar", "Aan de Belgische kust staat bijna de hele zeedijk vol met hoogbouw.", True),
             ]),

        dict(kop="Landbouw en bos",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet het verdwijnen van bos om er landbouwgrond of bebouwing van te maken?",
                  "ontbossing", WW),
                 ("open", "Noem drie gevolgen van ontbossing op een helling.",
                  "De bodem spoelt sneller weg, er wordt minder koolstofdioxide opgenomen, en dieren verliezen "
                  "hun leefgebied.", 5),
                 ("open", "Waarom worden landbouwpercelen steeds groter gemaakt, en wat verdwijnt daarbij?",
                  "Omdat grote machines er efficiënter kunnen werken. Door percelen samen te voegen verdwijnen "
                  "de hagen en houtkanten ertussen, en net die waren schuilplaats voor vogels en insecten.", 6),
                 ("kort", "Hoe heet het kunstmatig van water voorzien van land?", "irrigatie", W),
                 ("open", "Noem twee nadelen die irrigatie kan hebben.",
                  "De rivier of het grondwater raakt uitgeput, de bodem kan verzilten, en verderop blijft er "
                  "minder water over. Twee van die drie volstaan.", 5),
             ]),

        dict(kop="Verharding en ontharding",
             opdracht="",
             oefeningen=[
                 ("rij", [("grond bedekken met beton, asfalt of tegels", "verharding"),
                          ("beton of tegels weghalen zodat de grond open ligt", "ontharding"),
                          ("een ondiepe kom waar regenwater in kan zakken", "een wadi"),
                          ("voedsel telen in of vlak bij de stad", "stadslandbouw")],
                  "Hoe heet dit?", WW),
                 ("open", "Een gemeente breekt een betonnen schoolplein op en legt er gras en bomen aan. Noem "
                          "drie gevolgen.",
                  "Regenwater kan weer in de grond zakken, het is er op warme dagen koeler, en er is meer plaats "
                  "voor planten en dieren.", 5),
                 ("open", "Een nieuwe fabriek geeft werk aan driehonderd mensen maar vervuilt de beek ernaast. "
                          "Beschrijf dat met twee P's van het 5P-model.",
                  "Ze doet Prosperity vooruitgaan, want er komt werk en welvaart bij, en Planet achteruit, want "
                  "de beek en wat erin leeft gaan erop achteruit.", 6),
             ]),

        dict(kop="Twee misverstanden",
             opdracht="",
             oefeningen=[
                 ("waar", "Elke menselijke ingreep in het landschap heeft enkel nadelen.", False),
                 ("waar", "Een landschap dat door de mens veranderd is, kan nooit meer hersteld worden.", False),
                 ("open", "Geef van elk van die twee stellingen een voorbeeld dat aantoont dat ze niet klopt.",
                  "Bij de eerste: een spoorlijn of een kanaal brengt ook werk, verplaatsing en goedkoop "
                  "transport. Bij de tweede: een oude groeve die een natuurgebied wordt, of een rechtgetrokken "
                  "beek die weer mag kronkelen. Het herstel duurt alleen langer dan het afbreken.", 6),
                 ("open", "Waarom heeft ontbossing in het Amazonegebied gevolgen voor de hele wereld?",
                  "Omdat dat bos veel koolstofdioxide opneemt. Verdwijnt het, dan blijft er overal meer CO2 in "
                  "de lucht hangen, want de dampkring is gedeeld.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-onderzoeken-met-kaartlagen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Onderzoeken met kaartlagen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het gereedschap van de viewer",
             opdracht="",
             oefeningen=[
                 ("rij", [("waarin je lagen aan- en uitzet", "het lagenpaneel"),
                          ("waarmee je een adres of coördinaten ingeeft", "de zoekbalk"),
                          ("waarmee je een afstand of oppervlakte meet", "het meetgereedschap"),
                          ("waarmee je weet wat de kleuren betekenen", "de legende")],
                  "Hoe heet dit?", WW),
                 ("kort", "Hoe noem je één soort gegevens die je over de kaart legt?", "een kaartlaag", WW),
                 ("kort", "Hoe noem je een programma waarin je kaartlagen kan bekijken, stapelen en meten?",
                  "een GIS-viewer", WW),
                 ("open", "Waarom zou je een kaartlaag doorzichtig maken?",
                  "Om te zien wat eronder ligt, zodat je twee lagen tegelijk kan vergelijken.", 4),
                 ("waar", "In een kaartviewer heb je geen meetlat nodig om een afstand te kennen.", True),
             ]),

        dict(kop="Welke laag heb je nodig?",
             opdracht="Schrijf bij elke vraag welke laag of lagen je aanzet.",
             oefeningen=[
                 ("rij", [("Ligt deze wijk lager dan de rest van de gemeente?", "de hoogtelaag"),
                          ("Is er gebouwd vlak bij het water?", "de waterlopen en de bebouwing"),
                          ("Liggen de boomgaarden op leemgrond?", "de bodemkaart en het landgebruik"),
                          ("Is er sinds 1990 meer verhard?", "twee luchtfoto's van verschillende jaren")],
                  "Welke laag of lagen?", WL),
                 ("open", "Waarom neem je bij een onderzoek naar verharding twee luchtfoto's van verschillende "
                          "jaren, en niet één recente?",
                  "Omdat je dan de verandering ziet en niet alleen de toestand van vandaag. Met één foto weet je "
                  "niet of er meer of minder verhard is dan vroeger.", 5),
                 ("waar", "Hoe meer kaartlagen je tegelijk aanzet, hoe beter je onderzoek wordt.", False),
             ]),

        dict(kop="De vier stappen",
             opdracht="Zet de vier stappen van een geografisch onderzoek in de juiste volgorde.",
             oefeningen=[
                 ("tabel", ["volgorde", "de stap"],
                  [["1", None], ["2", None], ["3", None], ["4", None]],
                  "1. de vraag stellen, 2. lagen kiezen, 3. analyseren, 4. besluiten.", "250px"),
                 ("kort", "Hoe heet een verwacht antwoord dat je vooraf opschrijft en daarna nakijkt?",
                  "een hypothese", WW),
                 ("kort", "Hoe heet het gebied dat je in je onderzoek bekijkt?", "het onderzoeksgebied", WL),
                 ("waar", "Een hypothese die weerlegd wordt, maakt het onderzoek waardeloos.", False),
                 ("open", "Wat doe je als de kaartlagen je hypothese niet bevestigen?",
                  "Je schrijft op wat je wél ziet en trekt daaruit je besluit. Je vermeldt er ook bij dat je "
                  "hypothese niet klopte; dat is op zich een resultaat.", 5),
             ]),

        dict(kop="Goede en slechte onderzoeksvragen",
             opdracht="Duid aan of de vraag bruikbaar is voor een kaartonderzoek.",
             oefeningen=[
                 ("rij", [("\"Ligt de wijk die onderloopt lager dan de rest van het dorp?\"", "bruikbaar"),
                          ("\"Is de natuur mooi?\"", "niet bruikbaar"),
                          ("\"Liggen de boomgaarden van deze gemeente op leembodem?\"", "bruikbaar"),
                          ("\"Waarom houden mensen van hun dorp?\"", "niet bruikbaar")],
                  "Bruikbaar of niet?", WW),
                 ("open", "Noem drie eigenschappen van een goede onderzoeksvraag.",
                  "Ze is zo nauwkeurig mogelijk geformuleerd, ze gaat over een afgebakend gebied, en ze is met "
                  "de gekozen bronnen te beantwoorden.", 5),
             ]),

        dict(kop="Besluiten trekken",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie dingen die in het besluit van een kaartonderzoek horen.",
                  "Een antwoord op de onderzoeksvraag, waarop je dat antwoord baseert, en of je hypothese "
                  "klopte of niet.", 5),
                 ("waar", "Twee patronen die op de kaart samenvallen, bewijzen dat het ene het andere "
                          "veroorzaakt.", False),
                 ("open", "Leg uit waarom samenvallen op een kaart geen bewijs is.",
                  "Ze kunnen allebei door iets derds veroorzaakt zijn, of toevallig samenvallen. Samenvallen is "
                  "een aanwijzing die je verder moet onderzoeken, geen bewijs.", 5),
                 ("kort", "Een perceel meet 0,8 hectare. Hoeveel vierkante meter is dat?",
                  "8000 vierkante meter", WL),
                 ("open", "Waarom volstaat een kaartonderzoek soms niet en moet je toch ter plaatse gaan kijken?",
                  "Omdat niet alles op een kaart terechtkomt: geur, geluid, hoe nat de grond aanvoelt, wat er "
                  "sinds de laatste opname veranderd is.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-landschap-op-het-terrein-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Het landschap op het terrein",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Lokaliseren en oriënteren",
             opdracht="Schrijf bij elke zin of het over lokaliseren of over oriënteren gaat.",
             oefeningen=[
                 ("rij", [("je coördinaten aflezen op je toestel", "lokaliseren"),
                          ("de kaart draaien tot de noordpijl klopt", "oriënteren"),
                          ("je eigen punt op de kaart aanduiden", "lokaliseren"),
                          ("aan de kerktoren zien welke kant je uit kijkt", "oriënteren")],
                  "Wat doe je?", WW),
                 ("waar", "Een kompas werkt betrouwbaar vlak naast een ijzeren hek.", False),
                 ("waar", "Een satellietnavigatiesysteem werkt overal even goed, ook binnen.", False),
                 ("kort", "In welke richting staat de zon bij ons rond de middag?", "in het zuiden", W),
                 ("open", "Noem drie dingen die je meeneemt voor een terreinonderzoek, en zeg bij elk waarvoor.",
                  "Een kompas om je te oriënteren, een kaart van het gebied om je te lokaliseren en te "
                  "vergelijken, en een schepje om een kuiltje te graven en de bodem te bekijken.", 6),
             ]),

        dict(kop="Het reliëf beschrijven",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie dingen die je noteert als je het reliëf van je onderzoeksgebied "
                          "beschrijft.",
                  "De helling van het terrein, de hoogteverschillen die je ziet, en waar de horizonlijn ligt.", 5),
                 ("kort", "Hoe heet het verschil tussen het laagste en het hoogste punt van je gebied?",
                  "het hoogteverschil", WW),
                 ("open", "Je staat onderaan een helling. Wat merk je aan de horizonlijn, en waarom?",
                  "Ze ligt dichtbij, want de helling neemt je zicht weg. Bovenop diezelfde helling kijk je veel "
                  "verder.", 5),
                 ("kort", "Hoe heet een tekening van het terrein zoals je het van opzij zou zien?",
                  "een transect of doorsnede", WL),
                 ("open", "Waarom maak je op het terrein een schets in plaats van alleen een foto?",
                  "Omdat je op een schets zelf kiest wat belangrijk is: je laat weg wat niet ter zake doet en "
                  "zet groot wat wel telt. Een foto neemt alles even hard mee.", 5),
             ]),

        dict(kop="Vegetatie, bebouwing en landgebruik",
             opdracht="",
             oefeningen=[
                 ("rij", [("er staan loofbomen, dicht op elkaar", "vegetatie"),
                          ("er staan vier loodsen met een parking", "bebouwing"),
                          ("de grond dient voor akkerbouw", "landgebruik"),
                          ("er staat gras met verspreide struiken", "vegetatie")],
                  "Wat beschrijf je?", WW),
                 ("open", "Je ziet midden in een weide een rij knotwilgen langs een gracht. Wat besluit je "
                          "daaruit, en waarom?",
                  "Dat het een landschapselement is dat de mens heeft aangeplant. Knotwilgen groeien niet "
                  "vanzelf in een rechte rij, en knotten doet de natuur ook niet.", 5),
                 ("open", "Waarom noteer je het tijdstip van je waarnemingen?",
                  "Omdat het landschap er per seizoen en per uur anders bij ligt: de bladeren, het licht, het "
                  "water in de gracht en de drukte op de weg verschillen.", 5),
             ]),

        dict(kop="De bodem determineren",
             opdracht="Schrijf bij elke waarneming welk los gesteente het is.",
             oefeningen=[
                 ("rij", [("het knerpt duidelijk tussen je vingers", "zand"),
                          ("het voelt zacht en melig aan, bijna als bloem", "leem"),
                          ("je rolt er een dun draadje van en het blijft heel", "klei"),
                          ("je ziet de korrels met het blote oog liggen", "grind")],
                  "Welk gesteente?", WW),
                 ("kort", "Hoe heet een tabel waarmee je stap voor stap bepaalt met welk gesteente je te maken "
                          "hebt?", "een determineertabel", WL),
                 ("open", "Noem de drie dingen die je bij een bodemonderzoek op het terrein bekijkt.",
                  "De textuur van de bodem, de kleur van de lagen en hoe vochtig de bodem is.", 5),
                 ("waar", "De bovenste bodemlaag is meestal donkerder dan de laag eronder.", True),
                 ("open", "Je vindt in een weide een natte, grijzige bodem met riet errond. Wat besluit je, en "
                          "op grond waarvan?",
                  "Dat het grondwater daar hoog staat. Riet groeit niet op droge grond, en een bodem wordt "
                  "grijzig van langdurige natheid.", 5),
             ]),

        dict(kop="Het verslag",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie dingen die in een verslag van een terreinonderzoek horen.",
                  "Waar en wanneer je gekeken hebt, wat je waargenomen hebt, en welk besluit je eruit trekt.", 5),
                 ("waar", "Wie een terreinonderzoek doet, mag zonder meer overal een put graven.", False),
                 ("open", "Waarom vergelijk je je waarnemingen achteraf met een kaart?",
                  "Om na te gaan of wat je zag overeenkomt met wat de kaart toont. Klopt het niet, dan is dat op "
                  "zich al een vondst: misschien is de kaart ouder dan het landschap.", 5),
                 ("open", "Waarom is je eigen leefomgeving een goed onderzoeksgebied om mee te beginnen?",
                  "Omdat je er vaak komt en de veranderingen zelf ziet. Je weet al hoe het er vroeger uitzag, en "
                  "dat is precies wat een kaart je niet geeft.", 5),
                 ("kort", "Hoe noem je samen de manieren om ter plaatse in het landschap te werken?",
                  "terreintechnieken", WW),
             ]),
    ],
)
