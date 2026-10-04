# -*- coding: utf-8 -*-
"""Celdifferentiatie, weefsels en celtypes — 🌍 Beyond, biologie.

Deel 1 gaat over celdifferentiatie bij plant en dier, over stamcellen en
stamceltherapie, over klonen, en over de weefsels van een plant met de
huidmondjes erbij. Deel 2 gaat over de onderdelen van blad, stengel en wortel
en over de weefsels en celtypes van een dier.

De fiche vraagt telkens het verband tussen het celtype en zijn functie, dus
vragen de vragen naar het waarom van een bouw en niet enkel naar de naam.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke reeks beschrijft de groei van een plantencel?",
        opties=[
            "celdeling, celstrekking, celdifferentiatie",
            "celdifferentiatie, celdeling, celstrekking",
            "celstrekking, celdifferentiatie, celdeling",
            "celdifferentiatie, celstrekking, celdeling",
        ],
        antwoord=0,
        uitleg="Eerst deelt de cel, dan rekt ze uit doordat haar vacuole water opneemt, "
        "en pas daarna krijgt ze haar definitieve vorm en taak.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heten de cellen in een plant die zich blijven delen, bijvoorbeeld in de worteltop?",
        antwoord=["meristeemcellen", "meristeem"],
        uitleg="Meristeemcellen zijn de nog niet gedifferentieerde cellen van een plant. "
        "Ze liggen in de toppen van stengel en wortel en in het cambium.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is celdifferentiatie?",
        opties=[
            "een cel krijgt een vorm en een taak",
            "een cel deelt zich in twee dochtercellen",
            "een cel neemt water op en rekt uit",
            "een cel wordt door een lysosoom afgebroken",
        ],
        antwoord=0,
        uitleg="Bij differentiatie gaan in een cel andere genen aan en andere uit. Zo "
        "wordt uit dezelfde erfelijke informatie een spiercel of een zenuwcel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een stamcel? Kruis alles aan wat juist is.",
        opties=[
            "ze kan zich blijven delen",
            "ze kan nog verschillende celtypes worden",
            "ze heeft geen kern",
            "ze is altijd een spiercel",
        ],
        antwoord=[0, 1],
        uitleg="Een stamcel is nog niet gedifferentieerd en blijft deelbaar. Daarom kan "
        "ze een voorraad vormen waaruit nieuwe gespecialiseerde cellen ontstaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een plant zit er tussen de celdeling en de celdifferentiatie een stamcelstadium.",
        antwoord=False,
        uitleg="Dat is de weg bij een dier. Bij een plant komt daar celstrekking in de "
        "plaats: de cel neemt water op en rekt uit voor ze haar taak krijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor kan stamceltherapie gebruikt worden? Kruis alles aan wat juist is.",
        opties=[
            "beschadigd weefsel vervangen",
            "nieuwe bloedcellen laten aanmaken",
            "de bloedgroep van iemand veranderen",
            "een virus sneller doen groeien",
        ],
        antwoord=[0, 1],
        uitleg="Bij een beenmergtransplantatie krijgt iemand bloedstamcellen die weer "
        "nieuwe bloedcellen aanmaken. Hetzelfde idee loopt bij onderzoek naar huid, "
        "hoornvlies en hartspier.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een organisme dat erfelijk helemaal gelijk is aan het organisme waaruit het komt?",
        antwoord=["kloon", "een kloon"],
        uitleg="Een kloon heeft hetzelfde DNA als zijn ouderorganisme. Bij planten komt "
        "dat van nature voor, bij dieren moet het kunstmatig gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kloneert een tuinder een plant?",
        opties=[
            "door een stek of een scheut te laten wortelen",
            "door twee planten met elkaar te kruisen",
            "door zaad van twee ouders te zaaien",
            "door stuifmeel op een stamper te brengen",
        ],
        antwoord=0,
        uitleg="Een stek, een uitloper of een knol geeft een plant met hetzelfde DNA. "
        "Zaad uit een kruising geeft juist nieuwe combinaties, dus geen kloon.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kloon van een plant kan uit één enkele gedifferentieerde cel groeien.",
        antwoord=True,
        uitleg="Plantencellen blijven totipotent: ze kunnen weer alles worden. In een "
        "weefselkweek groeit uit een paar cellen een volledige nieuwe plant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk weefsel van een plant beschermt haar tegen uitdroging?",
        opties=[
            "het huidweefsel",
            "het transportweefsel",
            "het grondweefsel",
            "het meristeem",
        ],
        antwoord=0,
        uitleg="Het huidweefsel ligt aan de buitenkant. Op het blad maken de "
        "epidermiscellen een waslaag of cuticula die water binnenhoudt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de waslaag op de epidermis van een blad?",
        antwoord=["cuticula", "waslaag"],
        uitleg="De cuticula is een dun vetachtig laagje op de epidermis. Ze laat geen "
        "water door, waardoor het blad niet uitdroogt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cellen van een plant transporteren water en mineralen van de wortel naar het blad?",
        opties=[
            "de xyleemcellen",
            "de floëemcellen",
            "de epidermiscellen",
            "de collenchymcellen",
        ],
        antwoord=0,
        uitleg="Xyleem of houtvaten vervoeren water en mineralen omhoog. Het floëem of "
        "de zeefvaten vervoeren de gemaakte suikers in beide richtingen.",
    ),
    dict(
        type="waarofniet",
        vraag="De xyleemcellen zijn bij volle werking dode cellen zonder inhoud.",
        antwoord=True,
        uitleg="Een rijpe houtvat heeft geen cytoplasma meer: er blijft een holle buis "
        "met verstevigde wand over. Daardoor stroomt het water er bijna zonder weerstand "
        "door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan de cellen van een vaatbundel in een bundel bij elkaar?",
        opties=[
            "transport en stevigheid gaan dan samen",
            "zo kan de plant beter fotosynthese doen",
            "zo blijven de huidmondjes gesloten",
            "zo kan de wortel sneller delen",
        ],
        antwoord=0,
        uitleg="In een vaatbundel liggen xyleem, floëem en steunweefsel samen. De dikke "
        "wanden van het xyleem geven de stengel mee zijn stevigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cellen horen bij het grondweefsel van een plant? Kruis alles aan wat juist is.",
        opties=[
            "parenchymcellen",
            "sclerenchymcellen",
            "zeefvaten",
            "wortelharen",
        ],
        antwoord=[0, 1],
        uitleg="Het grondweefsel bestaat uit parenchym, collenchym en sclerenchym. "
        "Zeefvaten horen bij het transportweefsel en wortelharen bij het huidweefsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functie van sclerenchymcellen?",
        opties=[
            "de plant stevigheid geven",
            "suikers vervoeren",
            "licht opvangen",
            "water opnemen uit de bodem",
        ],
        antwoord=0,
        uitleg="Sclerenchymcellen hebben een sterk verdikte, verhoute wand en zijn "
        "meestal dood. Ze dienen alleen nog als steun, bijvoorbeeld in vlasvezels.",
    ),
    dict(
        type="waarofniet",
        vraag="Wortelharen vergroten het oppervlak waarmee een plant water opneemt.",
        antwoord=True,
        uitleg="Een wortelhaar is een lange uitloper van een rhizodermiscel. Duizenden "
        "ervan maken het contactoppervlak met de bodem veel groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar liggen de huidmondjes van een blad meestal?",
        opties=[
            "aan de onderkant",
            "aan de bovenkant",
            "in de nerven",
            "in de wortel",
        ],
        antwoord=0,
        uitleg="Aan de onderkant is er minder zon en minder wind, dus verliest het blad "
        "daar minder water bij hetzelfde gasuitwisseling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een huidmondje?",
        opties=[
            "gassen in en uit het blad laten",
            "suikers naar de wortel vervoeren",
            "het blad stevigheid geven",
            "licht opvangen voor de fotosynthese",
        ],
        antwoord=0,
        uitleg="Door een huidmondje gaat koolstofdioxide naar binnen en zuurstof en "
        "waterdamp naar buiten. De twee sluitcellen kunnen de opening dichtzetten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij droogte zet een plant haar huidmondjes wijder open.",
        antwoord=False,
        uitleg="Bij droogte sluit de plant ze juist, om water te sparen. Dat remt dan "
        "wel de fotosynthese, want er komt minder koolstofdioxide binnen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welk deel van een blad bevat de meeste chloroplasten?",
        opties=[
            "het palissadeparenchym",
            "de cuticula",
            "de epidermis aan de onderkant",
            "het xyleem",
        ],
        antwoord=0,
        uitleg="De palissadecellen liggen net onder de bovenste epidermis, rechtop en "
        "dicht tegen elkaar. Daar valt het meeste licht, dus daar zit het meeste chlorofyl.",
    ),
    dict(
        type="invultekst",
        vraag="Welk weefsel van een blad heeft veel luchtruimten tussen de cellen, zodat gassen er door kunnen?",
        antwoord=["sponsparenchym", "sponsweefsel"],
        uitleg="Het sponsparenchym ligt onder het palissadeparenchym. Zijn luchtholten "
        "staan in verbinding met de huidmondjes, zodat gassen tot bij elke cel komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de cortex in een wortel?",
        opties=[
            "water en stoffen naar de vaatbundel brengen",
            "licht opvangen voor de fotosynthese",
            "de bloem laten openen",
            "zaad maken",
        ],
        antwoord=0,
        uitleg="De cortex is het grondweefsel tussen de wortelhuid en de vaatbundel. "
        "Water dat de wortelharen opnamen, gaat erdoor naar het xyleem.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stengel heeft onder andere als taak het blad naar het licht te brengen.",
        antwoord=True,
        uitleg="De stengel draagt de bladeren en zet ze in het licht, en vervoert "
        "tegelijk water omhoog en suikers naar beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke weefsels komen bij een dier voor? Kruis alles aan wat juist is.",
        opties=[
            "epitheelweefsel",
            "zenuwweefsel",
            "grondweefsel",
            "huidmondjesweefsel",
        ],
        antwoord=[0, 1],
        uitleg="Een dier heeft epitheel-, bind-, spier-, zenuw- en transportweefsel. "
        "Grondweefsel en huidmondjes horen bij een plant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functie van epitheelweefsel?",
        opties=[
            "oppervlakken bedekken en afschermen",
            "prikkels doorgeven",
            "het lichaam doen bewegen",
            "zuurstof vervoeren",
        ],
        antwoord=0,
        uitleg="Epitheel bedekt de huid en de binnenkant van darm, longen en bloedvaten. "
        "De cellen liggen dicht tegen elkaar, zodat er niets tussendoor lekt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk weefsel verbindt en ondersteunt andere weefsels, en bevat onder meer kraakbeen en bot?",
        antwoord=["bindweefsel", "steunweefsel"],
        uitleg="Bindweefsel heeft weinig cellen en veel tussenstof. Kraakbeen, bot, vet "
        "en bloed worden er allemaal bij gerekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een rode bloedcel bij de mens geen kern?",
        opties=[
            "er is dan meer plaats voor hemoglobine",
            "ze heeft dan geen zuurstof meer nodig",
            "ze kan dan sneller delen",
            "ze kan dan prikkels doorgeven",
        ],
        antwoord=0,
        uitleg="Zonder kern en zonder organellen is de cel één zak hemoglobine, en kan ze "
        "zich ook makkelijker vervormen om door een haarvat te glippen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rode bloedcel van de mens kan zich niet meer delen.",
        antwoord=True,
        uitleg="Zonder kern is er geen DNA om na te maken. Nieuwe rode bloedcellen "
        "ontstaan daarom uit stamcellen in het beenmerg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een zenuwcel zo lang uitgerekt?",
        opties=[
            "om een prikkel over een grote afstand door te geven",
            "om zuurstof op te slaan",
            "om zich sneller te kunnen delen",
            "om water uit het bloed te halen",
        ],
        antwoord=0,
        uitleg="Het axon van één zenuwcel kan bijna een meter lang zijn. Zo gaat een "
        "prikkel van het ruggemerg tot in de voet zonder van cel naar cel te moeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft een spiercel in grote hoeveelheid, en waarom?",
        opties=[
            "mitochondria, want samentrekken kost energie",
            "chloroplasten, want ze maakt haar eigen suiker",
            "lysosomen, want ze breekt voedsel af",
            "vacuolen, want ze moet stevig blijven",
        ],
        antwoord=0,
        uitleg="Een spiercel heeft onafgebroken ATP nodig om actine en myosine langs "
        "elkaar te laten schuiven. Vandaar de vele mitochondria.",
    ),
    dict(
        type="waarofniet",
        vraag="Door kraakbeen lopen bloedvaten die de kraakbeencellen van zuurstof voorzien.",
        antwoord=False,
        uitleg="Kraakbeen heeft geen bloedvaten. De cellen worden gevoed door stoffen "
        "die door de tussenstof heen diffunderen, en daarom herstelt kraakbeen traag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk celtype van de mens is haploïd?",
        opties=[
            "de geslachtscel",
            "de epitheelcel",
            "de spiercel",
            "de zenuwcel",
        ],
        antwoord=0,
        uitleg="Een ei- of zaadcel heeft 23 chromosomen, de helft van een lichaamscel. "
        "Bij de bevruchting komen de twee helften weer samen op 46.",
    ),
    dict(
        type="invultekst",
        vraag="Welke cellen van de luchtwegen hebben trilharen die slijm naar boven duwen?",
        antwoord=["trilhaarcellen", "trilhaarepitheel", "epitheelcellen"],
        uitleg="Het trilhaarepitheel van de luchtwegen slaat ritmisch naar boven. Zo "
        "wordt slijm met stof en bacteriën richting de keel geduwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een darmcel heeft aan haar binnenkant duizenden kleine uitsteeksels. Waarom?",
        opties=[
            "om meer voedingsstoffen op te nemen",
            "om prikkels door te geven",
            "om zich sneller te delen",
            "om zuurstof te vervoeren",
        ],
        antwoord=0,
        uitleg="Die microvilli vergroten het oppervlak enorm. Meer oppervlak betekent "
        "meer transporteiwitten en dus meer opname per cel.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle cellen van een mens hebben dezelfde genen, maar niet dezelfde genen staan aan.",
        antwoord=True,
        uitleg="Elke lichaamscel heeft hetzelfde DNA. Wat een cel tot spiercel of "
        "zenuwcel maakt, is welke genen in die cel tot expressie komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een weefsel zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het bestaat uit cellen met een gelijkaardige taak",
            "verschillende weefsels samen vormen een orgaan",
            "een weefsel bestaat altijd uit één enkele cel",
            "een weefsel komt alleen bij dieren voor",
        ],
        antwoord=[0, 1],
        uitleg="Een weefsel is een groep cellen met dezelfde opdracht. Een orgaan zoals "
        "de maag bestaat uit epitheel-, spier-, bind- en zenuwweefsel samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een gedifferentieerde zenuwcel zich niet meer delen?",
        opties=[
            "ze is uit de celcyclus gestapt",
            "ze heeft geen DNA meer",
            "ze heeft geen celmembraan",
            "ze bevat geen water",
        ],
        antwoord=0,
        uitleg="Een volledig gedifferentieerde cel blijft in de G0-fase staan. Ze doet "
        "haar werk, maar begint niet meer aan een nieuwe celcyclus.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een dier doen het xyleem en het floëem het transport van stoffen.",
        antwoord=False,
        uitleg="Xyleem en floëem zijn weefsels van een plant. Bij een dier vervoeren "
        "bloed en lymfe de stoffen; dat is zijn transportweefsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker ziet onder de microscoop cellen met een dikke wand, zonder inhoud, in lange buizen aan elkaar. Welk weefsel is dat?",
        opties=[
            "transportweefsel van een plant",
            "zenuwweefsel van een dier",
            "epitheelweefsel van een dier",
            "meristeem van een plant",
        ],
        antwoord=0,
        uitleg="Dode cellen met verdikte wand, op elkaar gestapeld tot een buis: dat is "
        "het beeld van houtvaten in het xyleem.",
    ),
]
