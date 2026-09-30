# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij techniek ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere voorwerpen om te beoordelen, andere tandwielen om mee te
rekenen, en opdrachten die je enkel op papier kan maken (een waarheidstabel
invullen, een tabel aanvullen, een keuze verantwoorden). Wie hier iets
bijschrijft, legt het eerst naast `../../spark/techniek.json`.

De waarheidstabellen en de tandwielberekeningen zijn nagerekend.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Techniek"
SPARK = "✨ Spark — 1ste en 2de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag: schrijf eerst de bewerking op en zet de eenheid erbij.",
    "Bij een keuze: zeg niet alleen wát je kiest, maar ook waaróm.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-materialen-en-grondstoffen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Materialen en grondstoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Grondstof, materiaal of product?",
             opdracht="Schrijf bij elk woord welk van de drie het is.",
             oefeningen=[
                 ("rij", [("ijzererts", "grondstof"),
                          ("staal", "materiaal"),
                          ("een fietsframe", "product"),
                          ("wol", "grondstof")],
                  "Wat is dit?", WW),
                 ("rij", [("zand", "grondstof"),
                          ("glas", "materiaal"),
                          ("een drinkglas", "product"),
                          ("aardolie", "grondstof")],
                  "Wat is dit?", WW),
                 ("open", "Zet de rij van boom tot stoel op papier, met bij elk woord of het een grondstof, "
                          "een materiaal of een product is.",
                  "De boom is de grondstof, de plank of het hout is het materiaal, de stoel is het product.", 4),
             ]),

        dict(kop="Welke proef?",
             opdracht="",
             oefeningen=[
                 ("rij", [("is dit een metaal of een niet-metaal?", "de geleidingsproef"),
                          ("is dit een ferro- of een non-ferrometaal?", "de magneetproef")],
                  "Welke proef doe je?", WL),
                 ("open", "Leg uit waarom je met een magneet niet kan vaststellen of iets een metaal is.",
                  "Omdat alleen ferrometalen door een magneet aangetrokken worden. Aluminium en koper zijn wél "
                  "metalen maar reageren niet op een magneet.", 5),
                 ("rij", [("koper", "non-ferro"),
                          ("staal", "ferro"),
                          ("aluminium", "non-ferro"),
                          ("lood", "non-ferro")],
                  "Ferro of non-ferro?", WW),
                 ("waar", "Een magneet trekt aluminium aan.", False),
             ]),

        dict(kop="Legeringen en herkomst",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe noem je het materiaal dat ontstaat als je twee of meer metalen samensmelt?",
                  "een legering", WW),
                 ("rij", [("brons", "legering"),
                          ("koper", "enkelvoudig metaal"),
                          ("messing", "legering"),
                          ("inox", "legering")],
                  "Legering of enkelvoudig?", WW),
                 ("kort", "Welke korte naam draagt roestvrij staal in de techniek?", "inox", W),
                 ("rij", [("leder", "natuurlijk"),
                          ("kunststof", "kunstmatig"),
                          ("steen", "natuurlijk"),
                          ("composiet", "kunstmatig")],
                  "Natuurlijk of kunstmatig?", WW),
             ]),

        dict(kop="Eigenschappen sorteren",
             opdracht="Schrijf bij elke eigenschap of ze mechanisch, fysisch of technologisch is.",
             oefeningen=[
                 ("rij", [("hardheid", "mechanisch"),
                          ("smeltpunt", "fysisch"),
                          ("treksterkte", "mechanisch"),
                          ("warmtegeleiding", "fysisch")],
                  "Welke groep?", WW),
                 ("rij", [("vervormbaarheid", "technologisch"),
                          ("broosheid", "mechanisch"),
                          ("watervastheid", "technologisch"),
                          ("massadichtheid", "fysisch")],
                  "Welke groep?", WW),
                 ("kort", "Wat onderzoek je met de onderdompelingsmethode?", "de massadichtheid", WW),
                 ("kort", "Hoe noem je een materiaal dat veel kan verdragen voor het breekt?", "taai", W),
                 ("open", "Een onderdeel mag niet branden en moet tegen vocht kunnen. Kies tussen hout en "
                          "kunststof, en verantwoord je keuze.",
                  "Kunststof. Hout brandt en neemt vocht op; kunststof doet geen van beide.", 5),
             ]),

        dict(kop="De veiligheidspictogrammen",
             opdracht="",
             oefeningen=[
                 ("rij", [("de stof veroorzaakt brandwonden", "bijtend of corrosief"),
                          ("de stof kan vlam vatten", "ontvlambaar"),
                          ("de stof kan brand veroorzaken of erger maken", "oxiderend"),
                          ("schadelijk voor het water en de vissen", "gevaarlijk voor het aquatisch milieu")],
                  "Welk pictogram?", WL),
                 ("kort", "Waarvoor waarschuwt het pictogram met de gasfles?", "voor gassen onder druk", WL),
                 ("open", "Zoek thuis of op school één fles of doos met een gevaarpictogram. Schrijf op welk "
                          "product het is en welk gevaar het pictogram aangeeft.",
                  "Elk antwoord is goed zolang het product en het gevaar bij elkaar horen. Denk aan "
                  "ontstopper (bijtend), spiritus (ontvlambaar) of afwasmiddel voor de machine (bijtend).", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-energie-in-een-technisch-systeem-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Energie in een technisch systeem",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke energievorm?",
             opdracht="",
             oefeningen=[
                 ("rij", [("een rijdende trein", "bewegingsenergie"),
                          ("een boek op de bovenste plank", "potentiële energie"),
                          ("een volle batterij", "chemische energie"),
                          ("de zon op een zonnepaneel", "stralingsenergie")],
                  "Welke energievorm?", WW),
                 ("kort", "Wat is een ander woord voor bewegingsenergie?", "kinetische energie", WW),
                 ("waar", "Warmte is een energievorm.", True),
                 ("kort", "Welke energie zit er opgeslagen in steenkool, aardgas en voedsel?",
                  "chemische energie", WW),
             ]),

        dict(kop="Energieomzettingen",
             opdracht="Schrijf van elk systeem op van welke vorm naar welke vorm.",
             oefeningen=[
                 ("tabel", ["systeem", "van", "naar"],
                  [["een windmolen", None, None],
                   ["een zonnepaneel", None, None],
                   ["een gloeilamp", None, None],
                   ["een elektrische motor", None, None]],
                  "Windmolen: beweging → elektrisch. Zonnepaneel: straling → elektrisch. Gloeilamp: elektrisch "
                  "→ licht en warmte. Elektrische motor: elektrisch → beweging.", "120px"),
                 ("waar", "Een elektrische motor zet bewegingsenergie om in elektrische energie.", False),
                 ("open", "Leg uit wat een generator doet, en waarin hij verschilt van een elektrische motor.",
                  "Een generator zet beweging om in elektriciteit. Een elektrische motor doet precies het "
                  "omgekeerde: die zet elektriciteit om in beweging.", 5),
                 ("waar", "Een technisch systeem kan energie uit het niets maken.", False),
             ]),

        dict(kop="Nuttig en niet-nuttig",
             opdracht="",
             oefeningen=[
                 ("rij", [("een gloeilamp", "nuttig: licht — niet-nuttig: warmte"),
                          ("een waterkoker", "nuttig: warmte — niet-nuttig: geluid"),
                          ("een boormachine", "nuttig: de beweging van de boor"),
                          ("een luidspreker", "nuttig: geluid")],
                  "Wat is nuttig, wat niet?", WL),
                 ("open", "Waarom wordt een gsm warm terwijl hij oplaadt?",
                  "Omdat een deel van de energie warmte wordt in plaats van lading. Geen enkel toestel zet "
                  "alles nuttig om.", 5),
                 ("waar", "Het licht van een leeslamp is de niet-nuttige energie.", False),
             ]),

        dict(kop="Fossiel of hernieuwbaar",
             opdracht="",
             oefeningen=[
                 ("rij", [("steenkool", "fossiel"),
                          ("wind", "hernieuwbaar"),
                          ("aardolie", "fossiel"),
                          ("aardwarmte", "hernieuwbaar")],
                  "Fossiel of hernieuwbaar?", WW),
                 ("kort", "Wat is aardwarmte?", "warmte uit de diepe ondergrond", WL),
                 ("open", "Wat betekent hernieuwbare energie, en waarom noemen we ze ook duurzame energie?",
                  "Hernieuwbaar betekent dat de bron niet opraakt. Duurzaam omdat de bron ook voor de volgende "
                  "generaties blijft bestaan.", 5),
                 ("waar", "Wind raakt op als je er te veel stroom mee maakt.", False),
                 ("kort", "Welk broeikasgas komt vooral vrij bij het verbranden van fossiele brandstoffen?",
                  "CO2 of koolstofdioxide", WW),
             ]),

        dict(kop="Wat jij kan doen",
             opdracht="",
             oefeningen=[
                 ("open", "Noem drie dingen die jij zelf kan doen om minder fossiele brandstof te gebruiken.",
                  "Met de fiets gaan in plaats van met de auto, de verwarming een graad lager zetten, en het "
                  "licht uitdoen als je een kamer verlaat.", 5),
                 ("open", "Wat is het grootste nadeel van energie uit wind en zon?",
                  "Ze leveren niet altijd evenveel: op een windstille of donkere dag komt er weinig binnen.", 4),
                 ("waar", "Het broeikaseffect bestond al voor de mens fossiele brandstoffen begon te gebruiken.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-elektrische-stroomkring-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="De elektrische stroomkring",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De componenten",
             opdracht="",
             oefeningen=[
                 ("rij", [("opent of sluit de kring", "de schakelaar"),
                          ("laat de stroom moeilijker doorlopen", "de weerstand"),
                          ("zet stroom om in geluid", "de zoemer"),
                          ("verbindt de onderdelen met elkaar", "de geleider of draad")],
                  "Welk onderdeel?", WW),
                 ("kort", "Welke soort spanning levert een batterij?", "gelijkspanning", WW),
                 ("kort", "En een generator?", "wisselspanning", WW),
                 ("waar", "Een LED laat de stroom in twee richtingen door.", False),
                 ("open", "Noem de drie dingen die je nodig hebt om een lampje te laten branden.",
                  "Een spanningsbron, geleidende draden en het lampje zelf.", 4),
                 ("waar", "In een open stroomkring loopt er stroom.", False),
             ]),

        dict(kop="Serie of parallel?",
             opdracht="",
             oefeningen=[
                 ("rij", [("de lampjes van een kerstboom", "parallel"),
                          ("de twee schakelaars van een heggenschaar", "serie"),
                          ("de lampen in de kamers van een huis", "parallel"),
                          ("verbruikers achter elkaar in één kring", "serie")],
                  "Serie of parallel?", WW),
                 ("open", "Waarom staan de twee schakelaars van een heggenschaar in serie?",
                  "Omdat de kring dan pas gesloten is als je ze allebei indrukt. De schaar werkt zo alleen met "
                  "twee handen, en dan kunnen je handen niet bij het mes.", 5),
                 ("open", "Je draait één lampje los. Wat gebeurt er in serie, en wat in parallel?",
                  "In serie gaan ze allemaal uit, want de kring is onderbroken. In parallel blijven de andere "
                  "branden, want elk lampje heeft zijn eigen tak.", 5),
                 ("kort", "Hoe heet een schakeling die serie en parallel combineert?",
                  "een gemengde schakeling", WL),
             ]),

        dict(kop="Grootheden en eenheden",
             opdracht="Vul de eenheid in.",
             oefeningen=[
                 ("rij", [("spanning", "de volt"),
                          ("stroomsterkte", "de ampère"),
                          ("weerstand", "de ohm"),
                          ("vermogen", "de watt")],
                  "In welke eenheid?", WW),
                 ("waar", "De elektrische weerstand wordt uitgedrukt in ampère.", False),
                 ("kort", "Hoe noem je een multimeter die je gebruikt om de spanning te meten?",
                  "een voltmeter", WW),
                 ("open", "Hoe test je met een lampje of een materiaal stroom geleidt?",
                  "Je zet het materiaal in de kring, op de plaats van een draad, en kijkt of het lampje brandt. "
                  "Brandt het, dan geleidt het materiaal.", 5),
                 ("rij", [("koper", "geleider"),
                          ("rubber", "geen geleider"),
                          ("aluminium", "geleider"),
                          ("hout", "geen geleider")],
                  "Geleider of niet?", WW),
             ]),

        dict(kop="Gevaren",
             opdracht="",
             oefeningen=[
                 ("rij", [("er loopt meer stroom door een draad dan hij aankan", "overbelasting"),
                          ("de stroom vindt een te korte weg; er kan brand ontstaan", "kortsluiting"),
                          ("je krijgt een stroomstoot door je lichaam", "elektrocutie")],
                  "Welk gevaar?", WW),
                 ("kort", "Waarvoor waarschuwt het pictogram met de bliksemschicht?",
                  "voor gevaar voor elektrische spanning", WL),
                 ("rij", [("leidt stroom veilig naar de grond weg", "de aarding"),
                          ("onderbreekt de kring bij te veel stroom", "de automatische zekering"),
                          ("schakelt uit zodra er stroom weglekt", "de verliesstroomschakelaar")],
                  "Welke voorziening?", WL),
                 ("waar", "Dubbele isolatie is een soort gereedschap.", False),
             ]),

        dict(kop="Gereedschap",
             opdracht="",
             oefeningen=[
                 ("rij", [("het kunststof laagje van een draad halen", "een striptang"),
                          ("twee draden met tin verbinden", "een soldeerbout"),
                          ("twee draden met schroefjes klemmen", "een kroonsteentje"),
                          ("een draad doorknippen", "een zijsnijtang")],
                  "Welk gereedschap?", WW),
                 ("waar", "Een kroonsteentje dient om een draad door te knippen.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-informatieverwerkende-systemen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Informatieverwerkende systemen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Invoer, verwerking of uitvoer?",
             opdracht="",
             oefeningen=[
                 ("rij", [("een toetsenbord", "invoer"),
                          ("een beeldscherm", "uitvoer"),
                          ("de processor", "verwerking"),
                          ("een bewegingssensor", "invoer")],
                  "Welk deel van het systeem?", WW),
                 ("kort", "Hoe heet het schema met invoer, verwerking en uitvoer samen?",
                  "het IPO-schema", WW),
                 ("waar", "Een luidspreker is een invoerelement.", False),
                 ("open", "Wat doet een sensor, en wat doet een actuator?",
                  "Een sensor meet iets uit de omgeving en zet dat om in een signaal. Een actuator doet het "
                  "omgekeerde: die zet een signaal om in een beweging of een handeling.", 5),
             ]),

        dict(kop="Welke sensor?",
             opdracht="",
             oefeningen=[
                 ("rij", [("meet hoe warm het is", "een temperatuursensor"),
                          ("merkt of er iemand voorbijkomt", "een bewegingssensor"),
                          ("meet hoeveel licht er valt", "een lichtsensor"),
                          ("meet de afstand tot een voorwerp", "een afstandssensor")],
                  "Welke sensor?", WW),
                 ("open", "Een straatlamp gaat 's avonds van zichzelf aan. Leg uit met invoer, verwerking en "
                  "uitvoer hoe dat werkt.",
                  "Invoer: een lichtsensor meet dat het donker wordt. Verwerking: de regeling vergelijkt dat met "
                  "een grenswaarde. Uitvoer: de lamp gaat aan.", 6),
                 ("waar", "Een sensor beslist zelf wat er moet gebeuren.", False),
             ]),

        dict(kop="Analoog en digitaal",
             opdracht="",
             oefeningen=[
                 ("rij", [("een wijzer die vloeiend meedraait", "analoog"),
                          ("een reeks nullen en enen", "digitaal"),
                          ("een kwikthermometer", "analoog"),
                          ("een cijferklok", "digitaal")],
                  "Analoog of digitaal?", WW),
                 ("kort", "Hoe heet één cijfer, een 0 of een 1, in een digitaal signaal?", "een bit", W),
                 ("kort", "Uit hoeveel bits bestaat één byte?", "acht", W),
                 ("waar", "Een analoog signaal kan alle waarden tussen twee grenzen aannemen.", True),
             ]),

        dict(kop="De logische poorten",
             opdracht="Vul de uitkomst in.",
             oefeningen=[
                 ("tabel", ["poort", "0 en 0", "1 en 0", "1 en 1"],
                  [["EN", None, None, None],
                   ["OF", None, None, None]],
                  "EN: 0, 0, 1. OF: 0, 1, 1.", "56px"),
                 ("kort", "Welke poort maakt van een 1 een 0 en van een 0 een 1?", "de NIET-poort", WW),
                 ("open", "Een alarm moet afgaan als de deur open is óf als het raam open is. Welke poort heb je "
                  "nodig, en waarom?",
                  "Een OF-poort: één van de twee is al genoeg om het alarm te laten afgaan.", 5),
                 ("open", "Een machine mag pas starten als de kap dicht is én de noodstop niet ingedrukt is. "
                  "Welke poort is dat?",
                  "Een EN-poort: beide voorwaarden moeten waar zijn.", 4),
             ]),

        dict(kop="Communicatie en netwerk",
             opdracht="",
             oefeningen=[
                 ("rij", [("wie de boodschap verstuurt", "de zender"),
                          ("waarlangs de boodschap gaat", "het kanaal"),
                          ("wie de boodschap krijgt", "de ontvanger"),
                          ("wat de boodschap onderweg verstoort", "de ruis")],
                  "Welk deel van het communicatiemodel?", WL),
                 ("kort", "Hoe heet een netwerk van toestellen die via internet met elkaar praten?",
                  "het internet der dingen", WL),
                 ("waar", "Ruis is een onderdeel dat je bewust in een systeem inbouwt.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-krachten-en-stevigheid-in-een-constructie-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Krachten en stevigheid in een constructie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke kracht?",
             opdracht="",
             oefeningen=[
                 ("rij", [("je duwt van boven op een blokje", "druk"),
                          ("je trekt aan een touw", "trek"),
                          ("je draait een doek uit", "torsie"),
                          ("een plank zakt door in het midden", "buiging")],
                  "Welke krachtsoort?", WW),
                 ("kort", "In welke eenheid meet je een kracht?", "de newton", WW),
                 ("waar", "Een kracht heeft altijd een richting.", True),
                 ("kort", "Met welke drie dingen teken je een kracht als pijl?",
                  "aangrijpingspunt, richting en grootte", WL),
             ]),

        dict(kop="Sterke vormen",
             opdracht="",
             oefeningen=[
                 ("kort", "Welke vorm is de stevigste in een constructie?", "de driehoek", WW),
                 ("open", "Waarom zet men een schuine lat in een vierkant frame?",
                  "Omdat een vierkant kan vervormen tot een schuine vorm. De schuine lat maakt er twee driehoeken "
                  "van, en die vervormen niet.", 5),
                 ("kort", "Hoe noem je die schuine lat?", "een schoor of diagonaal", WW),
                 ("rij", [("een brug met driehoeken", "een vakwerkbrug"),
                          ("een dak met twee schuine vlakken", "een zadeldak"),
                          ("een vorm die de druk naar de zijkanten leidt", "een boog")],
                  "Hoe heet het?", WL),
                 ("waar", "Een buis is bij evenveel materiaal steviger dan een volle staaf van dezelfde dikte.",
                  False),
             ]),

        dict(kop="Rekenen met kracht",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "Een blok van 4 kg. Hoe groot is de zwaartekracht, met 10 N per kg?", "40 N", W),
                 ("kort", "Een kracht van 200 N op een vlak van 2 m². Hoe groot is de druk?", "100 N per m²", WW),
                 ("open", "Waarom zakken brede skilatten minder weg in de sneeuw dan smalle?",
                  "Omdat hetzelfde gewicht over een groter vlak verdeeld wordt. Daardoor is de druk per vierkante "
                  "centimeter kleiner.", 5),
                 ("kort", "Waar hangt de druk van af, buiten de grootte van de kracht?",
                  "van de grootte van het vlak", WL),
             ]),

        dict(kop="De hefboom",
             opdracht="",
             oefeningen=[
                 ("rij", [("het punt waarrond de hefboom draait", "het steunpunt"),
                          ("de kracht die je zelf zet", "de spierkracht"),
                          ("de kracht die je wil overwinnen", "de lastkracht")],
                  "Welk deel van de hefboom?", WL),
                 ("open", "Je zet het steunpunt verder van je hand en dichter bij de last. Moet je dan meer of "
                  "minder duwen? Leg uit.",
                  "Minder. Hoe langer de arm aan jouw kant en hoe korter aan de kant van de last, hoe minder "
                  "kracht je nodig hebt.", 5),
                 ("rij", [("een kruiwagen", "een hefboom"),
                          ("een notenkraker", "een hefboom"),
                          ("een schaar", "twee hefbomen samen")],
                  "Hefboom of niet?", WW),
                 ("waar", "Met een hefboom doe je hetzelfde werk met minder kracht, maar over een langere weg.",
                  True),
             ]),

        dict(kop="Stabiliteit",
             opdracht="",
             oefeningen=[
                 ("open", "Noem twee dingen die een voorwerp stabieler maken.",
                  "Een breed steunvlak en een laag zwaartepunt.", 4),
                 ("kort", "Hoe heet het punt waar je het gewicht van een voorwerp mag samendenken?",
                  "het zwaartepunt", WW),
                 ("open", "Waarom staat een racewagen stabieler in de bocht dan een bestelwagen?",
                  "Omdat hij veel lager bij de grond zit en breder is: een laag zwaartepunt boven een breed "
                  "steunvlak.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-verbinden-afwerken-en-veilig-werken-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Verbinden, afwerken en veilig werken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Los of vast?",
             opdracht="Zet bij elke verbinding of je ze weer kunt openen zonder iets stuk te maken.",
             oefeningen=[
                 ("rij", [("een lasverbinding", "vast"),
                          ("een boutverbinding", "los"),
                          ("een lijmverbinding", "vast"),
                          ("een ritssluiting", "los")],
                  "Los of vast?", WW),
                 ("kort", "Wat heb je nodig voor een boutverbinding?", "een bout en een moer", WW),
                 ("kort", "Hoe heet de verbinding waarbij je twee draden met gesmolten tin aan elkaar zet?",
                  "een soldeerverbinding", WW),
                 ("open", "Je bouwt een kast die je later weer moet kunnen afbreken. Kies je schroeven of "
                  "nagels? Leg uit.",
                  "Schroeven. Die kan je er weer uitdraaien; een nagel moet je eruit trekken en dan beschadig je "
                  "het hout.", 5),
                 ("waar", "Klittenband is geen verbinding.", False),
             ]),

        dict(kop="Houtverbindingen",
             opdracht="",
             oefeningen=[
                 ("rij", [("twee schuin afgezaagde stukken tegen elkaar", "een verstekverbinding"),
                          ("twee stukken hout met houten pinnetjes", "een deuvelverbinding"),
                          ("een deel dat kan draaien", "een scharnier")],
                  "Hoe heet het?", WL),
                 ("kort", "Wat doet een profiel in een constructie?",
                  "het verbindt delen en maakt het geheel stijver", WL),
                 ("open", "Noem drie dingen waar je op let als je een lijmsoort kiest.",
                  "Welke materialen je aan elkaar lijmt, of de verbinding nat kan worden, en hoeveel tijd je nog "
                  "hebt om de stukken te schikken.", 5),
                 ("kort", "Hoe heet de tijd waarin je de stukken nog kunt verschuiven nadat je gelijmd hebt?",
                  "de verwerkingstijd", WW),
             ]),

        dict(kop="Afwerken",
             opdracht="",
             oefeningen=[
                 ("rij", [("hout glad maken voor je het schildert", "schuren"),
                          ("een doorschijnende beschermlaag zetten", "vernissen"),
                          ("de kleur van het hout veranderen, met de nerf nog zichtbaar", "beitsen"),
                          ("het hout invetten zodat het water afstoot", "oliën")],
                  "Welke afwerkingstechniek?", WL),
                 ("open", "Waarom wordt hout gevernist of gelakt?",
                  "Om het te beschermen tegen vocht en slijtage.", 4),
                 ("waar", "Beitsen legt een dekkende laag over het hout, zodat je de nerf niet meer ziet.", False),
             ]),

        dict(kop="Veilig werken",
             opdracht="",
             oefeningen=[
                 ("kort", "Waar staan de drie letters PBM voor?",
                  "persoonlijke beschermingsmiddelen", WL),
                 ("rij", [("een oorbeschermer", "gehoorbescherming verplicht"),
                          ("een bril", "veiligheidsbril verplicht"),
                          ("een schoen", "veiligheidsschoenen verplicht")],
                  "Wat betekent het pictogram?", WL),
                 ("kort", "Welke bescherming draag je bij het boren in steen?", "een veiligheidsbril", WW),
                 ("open", "Wat staat er op een veiligheidsinstructiekaart?",
                  "De risico's van die machine en hoe je ze voorkomt.", 4),
                 ("open", "Noem drie veilige werkwijzen in een werkplaats.",
                  "Gemorste producten meteen opkuisen, de stekker uittrekken voor je aan de machine werkt, en "
                  "lang haar samenbinden voor je begint.", 5),
                 ("waar", "Je mag een elektrisch toestel bedienen met natte handen zolang je snel werkt.", False),
                 ("open", "Waarom bind je lang haar samen bij het werken met een machine?",
                  "Omdat het meegetrokken kan worden door draaiende delen.", 4),
                 ("kort", "Wat doe je eerst, voor je aan een machine gaat sleutelen?",
                  "de stekker uittrekken", WW),
             ]),

        dict(kop="Gereedschap",
             opdracht="",
             oefeningen=[
                 ("open", "Wat is het verschil tussen handgereedschap en een machine?",
                  "Een machine werkt met een motor of een andere aandrijving; handgereedschap beweegt door jouw "
                  "eigen kracht.", 5),
                 ("rij", [("een hamer", "handgereedschap"),
                          ("een boormachine", "machine"),
                          ("een verfborstel", "handgereedschap"),
                          ("een zaagmachine", "machine")],
                  "Handgereedschap of machine?", WW),
                 ("open", "Waarom moet je gereedschap onderhouden?",
                  "Omdat het dan veilig én nauwkeurig blijft werken.", 4),
                 ("waar", "Het meetbereik van een meetinstrument mag je overschrijden als het maar even duurt.",
                  False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-meten-eenheden-en-modelvoorstellingen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Meten, eenheden en modelvoorstellingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk meetinstrument?",
             opdracht="",
             oefeningen=[
                 ("rij", [("een hoeveelheid vloeistof", "een maatbeker"),
                          ("de dikte van een plaatje, heel nauwkeurig", "een schuifmaat"),
                          ("de massa van een voorwerp", "een weegschaal"),
                          ("de spanning over een lampje", "een multimeter")],
                  "Waarmee meet je het?", WW),
                 ("waar", "Een stappenplan is een meetinstrument.", False),
             ]),

        dict(kop="Grootheden en symbolen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["grootheid", "symbool", "SI-eenheid"],
                  [["massa", None, None],
                   ["lengte", None, None],
                   ["oppervlakte", None, None],
                   ["volume", None, None]],
                  "massa: m, kilogram. lengte: l, meter. oppervlakte: A, vierkante meter. "
                  "volume: V, kubieke meter.", "110px"),
                 ("kort", "Welk symbool hoort bij de grootheid omtrek?", "P", W),
                 ("kort", "Wat is de eenheid van kracht?", "de newton", W),
             ]),

        dict(kop="Omrekenen",
             opdracht="",
             oefeningen=[
                 ("rij", [("1 kilometer = ? meter", "1000 meter"),
                          ("1 centimeter = ? millimeter", "10 millimeter"),
                          ("1 kubieke decimeter = ? liter", "1 liter"),
                          ("1 meter = ? centimeter", "100 centimeter")],
                  "Vul in.", WW),
                 ("kies", "Wat betekent het voorvoegsel hecto?",
                  ["tien", "honderd", "duizend", "een tiende"], 1),
                 ("open", "Noem drie voorvoegsels die een eenheid kleiner maken.",
                  "deci, centi en milli.", 4),
                 ("waar", "Het voorvoegsel kilo betekent duizend.", True),
             ]),

        dict(kop="Rekenen met formules",
             opdracht="Schrijf eerst de formule op, dan de bewerking, dan het antwoord met zijn eenheid.",
             oefeningen=[
                 ("kort", "De oppervlakte van een rechthoek van 7 cm op 4 cm.", "28 vierkante centimeter", WW),
                 ("kort", "De omtrek van een vierkant met zijde 6 cm.", "24 centimeter", WW),
                 ("kort", "Het volume van een balk van 5 op 3 op 2 cm.", "30 kubieke centimeter", WW),
                 ("open", "Waarom staan er formules in bijlage 2 van de vakfiche?",
                  "Omdat je die op het examen mag gebruiken. Je moet ze dus niet vanbuiten kennen, wel kunnen "
                  "toepassen.", 5),
             ]),

        dict(kop="Tekeningen en schaal",
             opdracht="",
             oefeningen=[
                 ("rij", [("1:2", "de tekening is half zo groot als het voorwerp"),
                          ("2:1", "de tekening is twee keer zo groot als het voorwerp"),
                          ("1:1", "de tekening is even groot als het voorwerp")],
                  "Wat betekent de schaal?", WL),
                 ("kort", "Hoe heet de verhouding tussen de tekening en het echte voorwerp?", "de schaal", WW),
                 ("kort", "In welke eenheid staan de maten op een werktekening meestal?", "in millimeter", WW),
                 ("open", "Noem drie dingen die je op een werktekening terugvindt.",
                  "De maten van elk deel, de aanzichten van het voorwerp en de schaal waarop getekend is.", 5),
             ]),

        dict(kop="Aanzichten en modellen",
             opdracht="",
             oefeningen=[
                 ("rij", [("wat je ziet als je er recht van voren naar kijkt", "het vooraanzicht"),
                          ("wat je ziet als je er recht van boven op kijkt", "het bovenaanzicht"),
                          ("wat je ziet als je er van de zijkant naar kijkt", "het zijaanzicht"),
                          ("wat je ziet als je er van onderen naar kijkt", "het onderaanzicht")],
                  "Welk aanzicht?", WL),
                 ("rij", [("het platte patroon dat je dichtvouwt", "een ontvouwing"),
                          ("een tekening waarin je het voorwerp ruimtelijk ziet", "een isometrisch perspectief"),
                          ("een eerste ruwe tekening van een idee", "een conceptschets"),
                          ("een tekening van één onderdeel, groter getekend", "een detailontwerp")],
                  "Hoe heet het?", WL),
                 ("waar", "Een conceptschets is het definitieve ontwerp.", False),
                 ("open", "Wat staat er in een functiedriehoek?",
                  "De functie, het materiaal, de bewerking en de vorm.", 4),
                 ("waar", "Een functiedriehoek is een tekening van een voorwerp in drie aanzichten.", False),
                 ("open", "Waarom maakt een technicus eerst een schets voor hij begint te maken?",
                  "Om te zien of het idee klopt, voor er materiaal verloren gaat.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-transport-en-overbrengingen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Transport en overbrengingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Drijver en volger",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet het wiel dat de beweging geeft?", "de drijver", W),
                 ("kort", "En het wiel dat de beweging ontvangt?", "de volger", W),
                 ("rij", [("twee tandwielen die in elkaar grijpen", "rechtstreeks"),
                          ("de ketting van een fiets", "onrechtstreeks"),
                          ("twee wrijvingswielen die elkaar raken", "rechtstreeks"),
                          ("twee wielen met een riem ertussen", "onrechtstreeks")],
                  "Rechtstreeks of onrechtstreeks?", WW),
                 ("open", "Wat is het verschil tussen een rechtstreekse en een onrechtstreekse aandrijving?",
                  "Bij een rechtstreekse aandrijving raken de wielen elkaar. Bij een onrechtstreekse zit er een "
                  "riem of een ketting tussen.", 5),
                 ("waar", "De volger is het wiel dat de beweging geeft.", False),
             ]),

        dict(kop="Soorten overbrengingen",
             opdracht="",
             oefeningen=[
                 ("rij", [("een wiel met een groef waar een touw over loopt", "een katrol"),
                          ("een staaf die om een steunpunt draait", "een hefboom"),
                          ("wielen die de beweging doorgeven doordat ze elkaar raken", "wrijvingswielen"),
                          ("een reeks tanden die in elkaar grijpen", "tandwielen")],
                  "Hoe heet het?", WL),
                 ("open", "Waarom slippen wrijvingswielen soms?",
                  "Omdat ze elkaar alleen met wrijving vasthouden. Is die wrijving te klein, dan glijdt het ene "
                  "wiel langs het andere.", 5),
                 ("open", "Wat is een voordeel van een ketting boven een riem?",
                  "Een ketting kan niet slippen.", 4),
                 ("kort", "Welke overbrenging zit er tussen de trappers en het achterwiel van een fiets?",
                  "een ketting over twee tandwielen", WL),
                 ("kort", "Wat is een transportsysteem?", "een systeem dat iets of iemand verplaatst", WL),
             ]),

        dict(kop="Sneller of trager",
             opdracht="",
             oefeningen=[
                 ("rij", [("een klein tandwiel drijft een groot aan", "het grote draait trager"),
                          ("een groot tandwiel drijft een klein aan", "het kleine draait sneller"),
                          ("twee even grote wielen met een riem", "ze draaien even snel")],
                  "Wat gebeurt er?", WL),
                 ("waar", "Hoe meer tanden een tandwiel heeft, hoe sneller het draait bij dezelfde aandrijving.",
                  False),
                 ("kort", "Hoe noem je een overbrenging die de beweging trager maakt?", "een vertraging", WW),
                 ("open", "Meer snelheid bij een overbrenging gaat ten koste van iets. Van wat?",
                  "Van kracht. Je kan er niet meer uit halen dan erin gaat, dus wat je aan snelheid wint, verlies "
                  "je aan kracht.", 5),
             ]),

        dict(kop="Reken de omwentelingen",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "Een tandwiel met 10 tanden drijft er een met 30 aan. Hoe vaak draait het grote wiel "
                  "rond als het kleine drie keer rondgaat?", "één keer", WW),
                 ("kort", "Een tandwiel met 40 tanden drijft er een met 10 aan. Hoe vaak draait het kleine wiel "
                  "als het grote één keer rondgaat?", "vier keer", WW),
                 ("kort", "Een tandwiel met 12 tanden drijft er een met 36 aan. Hoe vaak trager draait het "
                  "grote wiel?", "drie keer trager", WL),
             ]),

        dict(kop="De draairichting",
             opdracht="",
             oefeningen=[
                 ("waar", "Twee tandwielen die in elkaar grijpen, draaien in dezelfde zin.", False),
                 ("waar", "Twee wielen met een gewone, niet gekruiste riem draaien in dezelfde zin.", True),
                 ("open", "Wat gebeurt er als je de riem van een riemoverbrenging laat kruisen, en waarom doet "
                  "men dat met opzet?",
                  "De volger draait dan in de andere zin. Men doet dat als de volger juist de andere kant op "
                  "moet draaien.", 5),
                 ("open", "Noem de drie dingen die een overbrenging met een beweging kan doen.",
                  "Ze kan de beweging versnellen, vertragen, of de richting ervan veranderen.", 5),
             ]),

        dict(kop="Hefbomen, katrollen en versnellingen",
             opdracht="",
             oefeningen=[
                 ("open", "Wat gebeurt er met de kracht die je nodig hebt als je bij een hefboom een langere "
                  "arm gebruikt?",
                  "Je hebt minder kracht nodig.", 4),
                 ("open", "Noem twee dingen die een stel katrollen voor je kan doen.",
                  "Het kan de richting van de kracht veranderen, en met meerdere katrollen hef je met minder "
                  "kracht.", 5),
                 ("waar", "Een stel katrollen verandert alleen de richting van het touw.", False),
                 ("open", "Waarom zet je op een fiets een licht verzet als je een helling opfietst?",
                  "Dan trap je lichter, maar je moet wel sneller trappen.", 5),
                 ("open", "Wat kies je met een versnellingsbak?",
                  "Je kiest tussen kracht en snelheid. In een lage versnelling trek je vlotter op, in een hoge "
                  "rij je sneller.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biotechnische-systemen-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Biotechnische systemen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Micro-organismen aan het werk",
             opdracht="",
             oefeningen=[
                 ("open", "Welke drie micro-organismen noemt de vakfiche?",
                  "Bacteriën, schimmels en gisten.", 4),
                 ("rij", [("brooddeeg laten rijzen", "gist"),
                          ("melk tot yoghurt maken", "bacteriën"),
                          ("kool tot zuurkool maken", "bacteriën")],
                  "Welk micro-organisme?", WW),
                 ("open", "Hoe wordt melk yoghurt?",
                  "Bacteriën zetten de melksuiker om. Daardoor wordt de melk zuur en dik.", 5),
                 ("waar", "Bij het maken van kaas komt er geen enkel micro-organisme aan te pas.", False),
                 ("kort", "Hoe heet de bewaartechniek waarbij micro-organismen het werk doen?",
                  "fermenteren", WW),
             ]),

        dict(kop="Bewaren",
             opdracht="",
             oefeningen=[
                 ("rij", [("bewaren in een zoute oplossing", "pekelen"),
                          ("in een gesloten pot verhitten", "wecken"),
                          ("de lucht uit de verpakking halen", "vacuüm verpakken"),
                          ("het water eruit halen", "drogen")],
                  "Welke bewaartechniek?", WL),
                 ("open", "Noem drie bewaartechnieken die met warmte werken.",
                  "Pasteuriseren, steriliseren en UHT.", 4),
                 ("kort", "Wat betekent UHT op een pak melk?",
                  "de melk is heel kort heel sterk verhit", WL),
                 ("open", "Wat doet invriezen met bacteriën, en waarom is koelen niet hetzelfde?",
                  "Invriezen legt hun groei zo goed als stil. Koelen vertraagt die groei alleen maar, dus "
                  "gekoeld voedsel blijft veel korter goed.", 6),
                 ("open", "Waarom blijft gedroogd fruit lang goed?",
                  "Zonder water kunnen bacteriën niet groeien.", 4),
                 ("open", "Waarom wordt vlees gerookt?",
                  "De rook remt bacteriën af, en ze geeft het vlees tegelijk smaak.", 4),
                 ("waar", "Vacuüm verpakken voegt juist lucht toe aan de verpakking.", False),
             ]),

        dict(kop="Het etiket",
             opdracht="",
             oefeningen=[
                 ("open", "Noem drie dingen die op het etiket van een voedingsmiddel moeten staan.",
                  "De ingrediëntenlijst, de allergenen en de houdbaarheidsdatum.", 5),
                 ("rij", [("ten minste houdbaar tot", "daarna kan de kwaliteit minder worden"),
                          ("te gebruiken tot", "daarna kan het product onveilig zijn")],
                  "Wat betekent het?", WL),
                 ("kort", "Wat is een allergeen?", "een stof waar sommige mensen op reageren", WL),
                 ("open", "Waarom staat de voedingswaarde op een etiket?",
                  "Zodat je weet hoeveel energie en welke stoffen erin zitten.", 4),
                 ("waar", "Ten minste houdbaar tot en te gebruiken tot betekenen precies hetzelfde.", False),
             ]),

        dict(kop="Wie controleert?",
             opdracht="",
             oefeningen=[
                 ("kort", "Waar staat de afkorting FAVV voor?",
                  "Federaal Agentschap voor de veiligheid van de voedselketen", WL),
                 ("open", "Wat is de taak van het FAVV, en wie controleert het?",
                  "Het waakt over de veiligheid van ons voedsel. Het controleert winkels, restaurants en "
                  "voedingsbedrijven.", 5),
             ]),

        dict(kop="De verpakking",
             opdracht="",
             oefeningen=[
                 ("open", "Noem drie dingen waarvoor een verpakking dient.",
                  "Het product beschermen bij het vervoer, het langer houdbaar maken, en informatie doorgeven "
                  "aan de klant.", 5),
                 ("open", "Waarom zit rode wijn in een donkere fles?",
                  "Om een reactie met licht tegen te gaan.", 4),
                 ("open", "Noem één voordeel en één nadeel van een plastic fles tegenover een glazen fles.",
                  "Voordeel: ze weegt minder, dus het vervoer kost minder. Nadeel: ze zorgt voor meer afval in "
                  "het milieu.", 5),
                 ("rij", [("drie pijlen die een driehoek vormen", "de verpakking is recycleerbaar"),
                          ("een cijfer van 1 tot 7 in het midden", "om welke soort kunststof het gaat"),
                          ("een glas en een vork", "het product is veilig voor voedsel"),
                          ("een doorstreepte vuilnisbak", "het mag niet bij het huisvuil")],
                  "Wat betekent het pictogram?", WL),
                 ("waar", "Het Groenpuntlogo betekent dat de verpakking van gerecycleerd materiaal gemaakt is.",
                  False),
                 ("kort", "Wat betekent composteerbaar?", "de verpakking kan vergaan tot compost", WL),
                 ("open", "Noem drie manieren om duurzaam met voedsel en verpakkingen om te gaan.",
                  "Kopen wat je echt nodig hebt, herbruikbare verpakkingen gebruiken, en je afval goed "
                  "sorteren.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-technisch-proces-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Het technisch proces",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vijf fasen",
             opdracht="Zet bij elke fase wat er gebeurt.",
             oefeningen=[
                 ("tabel", ["fase", "wat gebeurt er?"],
                  [["1", None], ["2", None], ["3", None], ["4", None], ["5", None]],
                  "1: je onderzoekt het probleem en de behoefte. 2: je ontwerpt en tekent het systeem. "
                  "3: je maakt het technisch systeem. 4: je neemt het in gebruik en test het. "
                  "5: je evalueert en stuurt bij waar nodig.", "320px"),
                 ("kort", "Hoeveel fasen heeft het technisch proces?", "vijf", W),
                 ("waar", "Het technisch proces begint bij een behoefte of een probleem.", True),
                 ("waar", "Het technisch proces kan alleen gebruikt worden voor een constructiesysteem.", False),
             ]),

        dict(kop="Fase 1: onderzoeken",
             opdracht="",
             oefeningen=[
                 ("kort", "Wat is een behoefteonderzoek?",
                  "nagaan wat de gebruiker echt nodig heeft", WL),
                 ("kort", "Hoe heet een eis waaraan je technisch systeem moet voldoen?", "een criterium", WW),
                 ("open", "Noem drie dingen die bij de eerste fase horen.",
                  "Het probleem onderzoeken, een behoefteonderzoek doen, en de criteria vastleggen.", 5),
                 ("waar", "Criteria stel je op nadat het systeem al gemaakt is.", False),
             ]),

        dict(kop="Fase 2: ontwerpen",
             opdracht="",
             oefeningen=[
                 ("open", "Noem drie dingen die bij de ontwerpfase horen.",
                  "Een schets of een model maken, het materiaal kiezen, en het gereedschap kiezen.", 5),
                 ("open", "Noem drie dingen die je in de ontwerpfase over het systeem beslist.",
                  "Welke verbindingstechnieken je gebruikt, welke sensoren of actuatoren nodig zijn, en welke "
                  "overbrengingen erin moeten komen.", 6),
                 ("open", "Waarom maak je een stappenplan voor je begint te maken?",
                  "Zo weet je in welke volgorde je moet werken.", 4),
                 ("waar", "Het stappenplan om het systeem te maken stel je pas op nadat het af is.", False),
             ]),

        dict(kop="Fase 3, 4 en 5",
             opdracht="",
             oefeningen=[
                 ("kort", "In welke fase licht je toe hoe je veilig met het gereedschap werkt?",
                  "in de maakfase, fase 3", WL),
                 ("kort", "Waaraan ga je in de laatste fase na of je systeem voldoet?",
                  "aan de opgestelde criteria", WL),
                 ("open", "Je systeem voldoet niet aan de criteria. Naar welke fase keer je volgens de fiche "
                  "terug, en waarom niet naar fase 1?",
                  "Naar fase 2 of fase 3. Het probleem en de behoefte zijn niet veranderd, alleen je ontwerp of "
                  "je uitvoering, dus die pak je opnieuw aan.", 6),
                 ("kort", "Wat betekent het als een ontwerp bijgestuurd wordt?",
                  "er wordt iets aan veranderd zodat het beter voldoet", WL),
             ]),

        dict(kop="STEM",
             opdracht="",
             oefeningen=[
                 ("tabel", ["letter", "waarvoor staat ze?"],
                  [["S", None], ["T", None], ["E", None], ["M", None]],
                  "S: science, wetenschappen. T: technology, technologie. E: engineering. "
                  "M: mathematics, wiskunde.", "290px"),
                 ("waar", "STEM gaat alleen over techniek.", False),
                 ("open", "Waarom gebruik je bij een ontwerp kennis uit wetenschappen én wiskunde?",
                  "Omdat een goed ontwerp meer dan één invalshoek vraagt. Een probleem laat zich zelden met één "
                  "vakgebied oplossen.", 6),
                 ("tabel", ["tijdens de coronacrisis", "welke kennis?"],
                  [["een vaccin ontwikkelen", None],
                   ["de verspreiding in kaart brengen", None],
                   ["het vaccin koel vervoeren", None]],
                  "Een vaccin ontwikkelen: wetenschappelijke kennis. De verspreiding in kaart brengen: "
                  "wiskundige kennis. Het vaccin koel vervoeren: technologische kennis.", "200px"),
             ]),

        dict(kop="Probleemoplossend ontwerpen",
             opdracht="",
             oefeningen=[
                 ("kort", "Wat is de eerste stap bij het ontwerpen van een oplossing?",
                  "het probleem duidelijk omschrijven", WL),
                 ("open", "Noem drie stappen van probleemoplossend ontwerpen.",
                  "Het probleem duidelijk bepalen, criteria opstellen voor de oplossing, en het probleem "
                  "opsplitsen in deelproblemen.", 5),
                 ("open", "Wat betekent het opsplitsen van een probleem in deelproblemen, en waarom voeg je de "
                  "oplossingen achteraf weer samen?",
                  "Je pakt elk stuk apart aan. Achteraan voeg je ze samen, omdat ze samen het hele probleem "
                  "moeten oplossen.", 6),
                 ("waar", "Soms volstaat het een bestaand systeem aan te passen in plaats van een nieuw te "
                  "ontwerpen.", True),
                 ("open", "Noem drie maatschappelijke uitdagingen die om nieuwe techniek vragen.",
                  "De klimaatverandering, een tekort aan grondstoffen, en de zorg voor een ouder wordende "
                  "bevolking.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-algoritmen-en-computationeel-denken-spark"] = dict(
    vak=VAK, niveau=SPARK, titel="Algoritmen en computationeel denken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat is een algoritme?",
             opdracht="",
             oefeningen=[
                 ("kort", "Wat is een algoritme?",
                  "een stappenplan met instructies in een vaste volgorde", WL),
                 ("rij", [("een recept om een cake te bakken", "een algoritme"),
                          ("een stappenplan om een boterham te smeren", "een algoritme"),
                          ("de code van een computerspel", "een algoritme")],
                  "Algoritme of niet?", WW),
                 ("waar", "Een algoritme moet altijd op een computer draaien.", False),
                 ("open", "Wat is het verschil tussen een digitaal en een niet-digitaal algoritme? Geef van elk "
                  "een voorbeeld.",
                  "Een niet-digitaal algoritme voer je zonder computer uit, bijvoorbeeld een stappenplan om een "
                  "boterham met choco te smeren. Een digitaal algoritme laat je door een computer uitvoeren, "
                  "bijvoorbeeld een lampje laten flikkeren met een programma.", 7),
                 ("waar", "In een algoritme mag je de stappen zomaar van volgorde wisselen.", False),
                 ("open", "Wat gebeurt er als één stap in een algoritme ontbreekt?",
                  "Het resultaat klopt meestal niet meer.", 4),
             ]),

        dict(kop="Een algoritme ontwerpen",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet een schema met pijlen dat de stappen van een algoritme toont?",
                  "een flowchart of stroomdiagram", WL),
                 ("open", "Waarvoor dient een flowchart?",
                  "Om de oplossing visueel voor te stellen, zodat je in één blik ziet hoe de stappen op elkaar "
                  "volgen.", 5),
                 ("kort", "Waarvoor staat IPO bij het analyseren van een probleem?",
                  "input, process en output", WL),
                 ("open", "Noem drie stappen die je volgt bij het ontwerpen van een algoritme.",
                  "Je formuleert de probleemstelling, je analyseert het probleem met IPO, en je test het "
                  "algoritme uit.", 5),
                 ("kort", "In welke programmeertaal vertaal je volgens de vakfiche je algoritme?",
                  "Scratch", W),
                 ("open", "Waarom test je een algoritme uit, en wat doe je als het niet het juiste resultaat "
                  "geeft?",
                  "Je test het om te zien of het echt doet wat je wilde. Geeft het niet het juiste resultaat, "
                  "dan stuur je het bij.", 6),
                 ("kort", "Wat is de laatste stap bij het ontwerpen van een algoritme?",
                  "testen en bijsturen waar nodig", WL),
             ]),

        dict(kop="Computationeel denken",
             opdracht="",
             oefeningen=[
                 ("rij", [("details weglaten die er niet toe doen", "abstractie"),
                          ("een probleem in kleinere delen opsplitsen", "decompositie"),
                          ("gelijkenissen tussen problemen zien", "patroonherkenning")],
                  "Welk principe?", WW),
                 ("open", "Welke vier principes van computationeel denken noemt de vakfiche?",
                  "Abstractie, decompositie, patroonherkenning en het algoritme.", 5),
                 ("waar", "Abstractie betekent zoveel mogelijk details toevoegen.", False),
                 ("open", "Je schrijft een algoritme om de weg naar school uit te leggen. Noem een detail dat je "
                  "weglaat, en zeg welk principe dat is.",
                  "De kleur van de huizen onderweg. Dat is abstractie: je laat weg wat er voor de weg niet toe "
                  "doet.", 6),
                 ("open", "Een spel heeft tien niveaus die sterk op elkaar lijken. Welk principe helpt hier, en "
                  "wat win je ermee?",
                  "Patroonherkenning. Je hergebruikt de oplossing die je voor het eerste niveau al gevonden "
                  "hebt, in plaats van tien keer opnieuw te beginnen.", 6),
                 ("open", "Noem drie momenten waarop decompositie helpt.",
                  "Als een probleem te groot is voor één keer, als verschillende delen los van elkaar werken, en "
                  "als je met meerdere mensen samenwerkt.", 5),
                 ("kort", "Wat is een voorbeeld van decompositie bij het maken van een spel?",
                  "apart werken aan de beweging, de punten en het geluid", WL),
             ]),

        dict(kop="Fouten en efficiëntie",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet een fout in een programma?", "een bug", W),
                 ("kort", "Hoe heet het opsporen en oplossen van zo'n fout?", "debuggen", W),
                 ("open", "Een programma moet een vierkant tekenen maar maakt maar drie zijden. Wat doe je?",
                  "Je debugt het algoritme: je zoekt de stap waar het fout gaat en past die aan.", 5),
                 ("waar", "Een fout in een algoritme vind je alleen door ernaar te kijken, nooit door het uit te "
                  "voeren.", False),
                 ("waar", "Efficiënt betekent dat een algoritme zoveel mogelijk stappen heeft.", False),
                 ("open", "Waarom is een korter algoritme met dezelfde uitkomst meestal beter?",
                  "Er kunnen minder fouten in sluipen.", 4),
                 ("open", "Noem drie dingen die je helpen om een efficiënt algoritme te schrijven.",
                  "Abstractie, decompositie en patroonherkenning.", 4),
             ]),
    ],
)
