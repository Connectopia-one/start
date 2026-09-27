# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van aardrijkskunde 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere plaatsen, andere schaalberekeningen en opdrachten waarbij een
kind zelf iets tekent. Wie hier iets bijschrijft, legt het eerst naast
`../../start/aardrijkskunde.json`.

Er staan bewust geen landkaarten in om na te tekenen: een kaart uit het hoofd
getekend klopt niet, en een kind mag geen foute vorm inprenten. De
tekenopdrachten gaan daarom over een kompasroos en een legende.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

W = "120px"
WW = "180px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Heb je een atlas in huis? Die mag je erbij nemen.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-kaartlezen-en-orientatie"] = dict(
    vak="Aardrijkskunde", titel="Kaartlezen en oriëntatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De windstreken",
             opdracht="Vier hoofdwindstreken, en daartussen nog vier.",
             oefeningen=[
                 ("teken", "Teken een kompasroos en zet er de acht windstreken bij, met hun "
                           "afkorting.",
                  "N bovenaan, O rechts, Z onderaan, W links. Daartussen NO, ZO, ZW en NW.", 55),
                 ("rij", [("tegenover het oosten", "het westen"),
                          ("tussen zuid en west", "het zuidwesten"),
                          ("tegenover het zuiden", "het noorden"),
                          ("tussen noord en west", "het noordwesten")],
                  "Welke windstreek is dat?", WW),
                 ("open", "De zon komt op in het oosten. Je staat 's morgens met je gezicht "
                          "naar de zon. Welke windstreek ligt dan achter je, en welke links?",
                  "Achter je het westen, links van je het noorden, rechts het zuiden.", 3),
                 ("waar", "Op een kaart staat het noorden meestal bovenaan.", True),
             ]),

        dict(kop="De schaal",
             opdracht="De schaal zegt hoeveel keer de werkelijkheid verkleind is.",
             oefeningen=[
                 ("rij", [("schaal 1 : 1 000, 1 cm op de kaart", "10 m"),
                          ("schaal 1 : 25 000, 1 cm op de kaart", "250 m"),
                          ("schaal 1 : 200 000, 1 cm op de kaart", "2 km")],
                  "Hoeveel is dat in het echt?", WW),
                 ("open", "Op een kaart met schaal 1 : 50 000 meet je 6 cm tussen twee dorpen. "
                          "Hoeveel kilometer is dat in het echt? Schrijf je berekening erbij.",
                  "6 × 50 000 cm = 300 000 cm = 3 000 m = 3 km.", 3),
                 ("kies", "Welke kaart toont het meeste detail?",
                  ["schaal 1 : 10 000", "schaal 1 : 100 000",
                   "schaal 1 : 1 000 000", "schaal 1 : 25 000"], 0),
             ]),

        dict(kop="Kleuren en tekens",
             opdracht="Zonder legende is een kaart alleen maar een prentje.",
             oefeningen=[
                 ("rij", [("blauw", "water"), ("groen", "laagvlakte"),
                          ("bruin", "bergen of hoogland"), ("geel", "duinen of droge vlakte")],
                  "Wat betekent die kleur meestal op een landkaart?", WW),
                 ("teken", "Teken een legende voor een kaart van je buurt, met vier tekens: "
                           "een school, een winkel, een park en een fietspad.",
                  "Elk teken mag je zelf verzinnen, zolang er telkens bij staat wat het "
                  "betekent. Dat is precies wat een legende doet.", 50),
                 ("open", "Wat is het verschil tussen een satellietbeeld en een kaart?",
                  "Een satellietbeeld is een echte foto van bovenaf, met alles erop. Een kaart "
                  "is getekend en vereenvoudigd: alleen wat je nodig hebt, met tekens en "
                  "kleuren en met namen erbij.", 3),
                 ("waar", "Een plattegrond toont een gebied zoals je het van bovenaf ziet.", True),
             ]),

        dict(kop="Lijnen op de aardbol",
             opdracht="Denkbeeldige lijnen helpen om een plaats aan te duiden.",
             oefeningen=[
                 ("rij", [("verdeelt de aarde in noord en zuid", "de evenaar"),
                          ("lopen van pool tot pool", "de meridianen"),
                          ("loopt door Greenwich", "de nulmeridiaan"),
                          ("lopen evenwijdig met de evenaar", "de breedtecirkels")],
                  "Welke lijn is dat?", WW),
                 ("open", "Waarom is het bij ons middag terwijl het in New York nog ochtend is?",
                  "De aarde draait om haar as, dus de zon staat niet overal tegelijk het "
                  "hoogst. Daarom is de aarde in tijdzones verdeeld.", 3),
                 ("kies", "Welk toestel gebruikt satellieten om te tonen waar je bent?",
                  ["een kompas", "een gps", "een windmeter", "een barometer"], 1),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-belgie"] = dict(
    vak="Aardrijkskunde", titel="België",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Provincies en hoofdplaatsen",
             opdracht="Vlaanderen telt vijf provincies, Wallonië vijf.",
             oefeningen=[
                 ("open", "Schrijf de vijf Vlaamse provincies op.",
                  "West-Vlaanderen, Oost-Vlaanderen, Antwerpen, Vlaams-Brabant en Limburg.", 3),
                 ("rij", [("Limburg", "Hasselt"), ("Oost-Vlaanderen", "Gent"),
                          ("West-Vlaanderen", "Brugge"), ("Antwerpen", "Antwerpen")],
                  "Wat is de hoofdplaats van die provincie?", WW),
                 ("rij", [("aan de kust", "West-Vlaanderen"),
                          ("het verst in het oosten van Vlaanderen", "Limburg"),
                          ("tussen Oost-Vlaanderen en Limburg", "Vlaams-Brabant")],
                  "Welke provincie is dat?", WW),
                 ("waar", "België telt drie gewesten.", True),
             ]),

        dict(kop="Water en landschap",
             opdracht="Denk aan wat er stroomt en hoe het land ligt.",
             oefeningen=[
                 ("rij", [("Antwerpen", "de Schelde"), ("Luik", "de Maas"),
                          ("Gent", "de Leie en de Schelde")],
                  "Welke rivier stroomt door die stad?", WW),
                 ("open", "Beschrijf in twee zinnen hoe het landschap van België verandert als "
                          "je van de kust naar de Ardennen reist.",
                  "Aan de kust zijn er duinen en strand, daarachter vlak polderland. Verder "
                  "landinwaarts wordt het licht golvend, en in het zuiden, in de Ardennen, "
                  "wordt het echt heuvelachtig met bossen en diepe valleien.", 3),
                 ("open", "Waarom liggen de grote havens van België aan het water en niet "
                          "midden in het land?",
                  "Schepen moeten er kunnen komen. Antwerpen ligt aan de Schelde en Zeebrugge "
                  "aan de zee, zodat goederen rechtstreeks aan- en afgevoerd kunnen worden.", 3),
                 ("kies", "Hoe heet het hoogste punt van België?",
                  ["de Kemmelberg", "het Signaal van Botrange",
                   "de Mont Ventoux", "de Vaalserberg"], 1),
             ]),

        dict(kop="Buurlanden en talen",
             opdracht="Vier buurlanden, drie landstalen.",
             oefeningen=[
                 ("open", "Schrijf de vier buurlanden van België op, en zet erbij in welke "
                          "richting elk ongeveer ligt.",
                  "Nederland in het noorden, Duitsland in het oosten, Luxemburg in het "
                  "zuidoosten en Frankrijk in het zuiden en zuidwesten.", 3),
                 ("rij", [("Vlaanderen", "Nederlands"), ("Wallonië", "Frans"),
                          ("de Oostkantons", "Duits")],
                  "Welke taal spreekt men daar vooral?", WW),
                 ("waar", "Brussel is officieel tweetalig: Nederlands en Frans.", True),
                 ("open", "Waarom heeft een klein land als België drie landstalen? "
                          "Schrijf wat je erover weet.",
                  "Het land is ontstaan uit gebieden waar al verschillende talen gesproken "
                  "werden. In het noorden Nederlands, in het zuiden Frans, en in het oosten "
                  "een klein Duitstalig gebied dat er na de Eerste Wereldoorlog bijkwam.", 3),
             ]),

        dict(kop="Wonen en werken in België",
             opdracht="Waar mensen wonen, hangt samen met het landschap en het werk.",
             oefeningen=[
                 ("rij", [("haven en diamant", "Antwerpen"),
                          ("de Europese instellingen", "Brussel"),
                          ("vroeger de steenkoolmijnen", "Limburg"),
                          ("toerisme aan het strand", "de kust")],
                  "Aan welke plaats denk je?", WW),
                 ("open", "Noem twee redenen waarom er in Vlaanderen zoveel mensen op een "
                          "kleine oppervlakte wonen.",
                  "Bijvoorbeeld: het is vlak en vruchtbaar, er liggen veel steden dicht bij "
                  "elkaar, er is veel werk, en het ligt centraal in Europa met goede havens "
                  "en wegen.", 3),
                 ("waar", "De Ardennen liggen in het zuiden van België en zijn veel dunner "
                          "bevolkt dan Vlaanderen.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-europa-en-de-wereld"] = dict(
    vak="Aardrijkskunde", titel="Europa en de wereld",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Werelddelen en oceanen",
             opdracht="Zes bewoonde werelddelen, en Antarctica erbij.",
             oefeningen=[
                 ("open", "Schrijf de werelddelen op die je kent.",
                  "Azië, Afrika, Noord-Amerika, Zuid-Amerika, Antarctica, Europa en Oceanië "
                  "(met Australië).", 3),
                 ("rij", [("tussen Europa en Amerika", "de Atlantische Oceaan"),
                          ("tussen Europa en Afrika", "de Middellandse Zee"),
                          ("de grootste oceaan", "de Stille Oceaan of Grote Oceaan")],
                  "Welk water is dat?", WW),
                 ("waar", "Europa is het kleinste werelddeel.", False),
                 ("open", "In welk werelddeel ligt de Sahara, en wat voor gebied is het?",
                  "In Afrika. Het is de grootste warme woestijn ter wereld: heel droog, "
                  "overdag heet en 's nachts koud.", 3),
             ]),

        dict(kop="Landen en hoofdsteden",
             opdracht="Schrijf de hoofdstad, of het land.",
             oefeningen=[
                 ("rij", [("Frankrijk", "Parijs"), ("Duitsland", "Berlijn"),
                          ("Italië", "Rome"), ("Spanje", "Madrid"),
                          ("Nederland", "Amsterdam"), ("Verenigd Koninkrijk", "Londen")],
                  "Wat is de hoofdstad?", WW),
                 ("rij", [("Lissabon", "Portugal"), ("Wenen", "Oostenrijk"),
                          ("Athene", "Griekenland"), ("Stockholm", "Zweden")],
                  "In welk land ligt die stad?", WW),
                 ("open", "Noem drie landen waar je met de euro kan betalen.",
                  "Bijvoorbeeld: België, Nederland, Duitsland, Frankrijk, Spanje, Italië, "
                  "Portugal, Oostenrijk, Griekenland, Ierland, Finland.", 2),
             ]),

        dict(kop="Bergen, rivieren en klimaat",
             opdracht="De hoogte en de ligging bepalen mee hoe het er is om te leven.",
             oefeningen=[
                 ("rij", [("scheidt Frankrijk en Spanje", "de Pyreneeën"),
                          ("de hoogste berg ter wereld", "de Mount Everest"),
                          ("de bergketen door Zwitserland en Oostenrijk", "de Alpen")],
                  "Welke berg of bergketen is dat?", WW),
                 ("open", "Waarom ligt er op hoge bergen sneeuw, ook in de zomer?",
                  "Hoe hoger je komt, hoe kouder het wordt. Boven een bepaalde hoogte blijft "
                  "het het hele jaar door vriezen, dus smelt de sneeuw er nooit helemaal.", 3),
                 ("open", "Als het bij ons zomer is, is het in Australië winter. Hoe komt dat?",
                  "Australië ligt op het zuidelijk halfrond. De as van de aarde staat schuin, "
                  "dus als het noorden naar de zon gekeerd is, is het zuiden dat net niet.", 3),
                 ("kies", "Hoeveel tijdzones zijn er ongeveer op aarde?",
                  ["12", "24", "36", "100"], 1),
             ]),

        dict(kop="Groot en klein",
             opdracht="Denk aan oppervlakte, niet aan het aantal mensen.",
             oefeningen=[
                 ("rij", [("het grootste land ter wereld", "Rusland"),
                          ("het grootste werelddeel", "Azië"),
                          ("land én werelddeel tegelijk", "Australië")],
                  "Vul aan.", WW),
                 ("open", "De evenaar loopt niet door Europa. Door welke werelddelen dan wel?",
                  "Door Afrika, Zuid-Amerika en Azië (Indonesië).", 2),
                 ("open", "Je reist van België naar Spanje. Reis je dan naar het noorden of "
                          "naar het zuiden? En wat merk je aan het weer?",
                  "Naar het zuiden. Het wordt er warmer en droger, want hoe dichter bij de "
                  "evenaar, hoe steiler de zon binnenvalt.", 3),
             ]),
    ],
)
