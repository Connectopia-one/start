# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij biologie 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere reeksen om te benoemen, andere gevallen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een
kruisingsschema uitschrijven, een stap uitleggen). Wie hier iets bijschrijft,
legt het eerst naast `../../beyond/biologie.json` en naast de leerbundel van
hetzelfde thema in `maak_biologie_beyond.py`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Biologie"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Bij een schema of een tabel: vul alle vakjes in, ook die waar je twijfelt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-de-cel-de-organellen-en-de-biologische-membranen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De cel, de organellen en de biologische membranen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk organel doet dit?",
             opdracht="Schrijf bij elke taak de naam van het organel.",
             oefeningen=[
                 ("rij", [("zet aminozuren aan elkaar tot een keten", "ribosoom"),
                          ("werkt eiwitten af en verpakt ze in blaasjes", "golgi-apparaat"),
                          ("verteert versleten celonderdelen", "lysosoom")], "Welk organel?", WW),
                 ("rij", [("maakt de ribosomen aan", "kernlichaampje"),
                          ("maakt het grootste deel van de ATP", "mitochondrion"),
                          ("legt bij de deling de trekdraden aan", "centrosoom")], "Welk organel?", WW),
             ]),
        dict(kop="Prokaryoot of eukaryoot?",
             opdracht="Schrijf prokaryoot, eukaryoot of beide.",
             oefeningen=[
                 ("rij", [("heeft een echte kern met een kernmembraan", "eukaryoot"),
                          ("heeft ribosomen", "beide"),
                          ("heeft mitochondriën", "eukaryoot")], None, W),
                 ("rij", [("heeft DNA", "beide"),
                          ("is meestal kleiner dan 5 micrometer", "prokaryoot"),
                          ("kan plasmiden bezitten", "prokaryoot")], None, W),
             ]),
        dict(kop="Plant, dier of beide?",
             opdracht="Schrijf plant, dier of beide.",
             oefeningen=[
                 ("rij", [("chloroplast", "plant"), ("celwand van cellulose", "plant"),
                          ("grote centrale vacuole", "plant")], None, W),
                 ("rij", [("celmembraan", "beide"), ("centrosoom", "dier"),
                          ("ruw endoplasmatisch reticulum", "beide")], None, W),
             ]),
        dict(kop="Het celmembraan",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Bestanddeel", "Wat het in het membraan doet"],
                  [["fosfolipiden", None], ["cholesterol", None], ["glycoproteïnen", None]],
                  "Fosfolipiden vormen de dubbellaag, de grondlaag van elk membraan. Cholesterol "
                  "houdt het membraan soepel maar stevig. Glycoproteïnen dragen de suikerketens "
                  "waarmee de cel herkend wordt.", WL),
                 ("open", "Waarom staan de staarten van de fosfolipiden naar binnen gekeerd en de "
                          "koppen naar buiten?",
                  "De koppen zijn hydrofiel en gaan dus naar het water aan beide kanten van het "
                  "membraan. De staarten zijn hydrofoob en kruipen daarom bij elkaar weg in het "
                  "midden.", 4),
                 ("waar", "Een biologisch membraan is een stijve plaat waarin niets kan bewegen.",
                  False),
             ]),
        dict(kop="Endosymbiose",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Noem drie waarnemingen aan een mitochondrion die de endosymbiosetheorie "
                          "steunen.",
                  "Het heeft zijn eigen cirkelvormige DNA, het heeft zijn eigen ribosomen, en het "
                  "heeft een dubbel membraan. Bovendien deelt het zich zelfstandig.", 4),
                 ("kort", "Welk ander organel heeft volgens die theorie dezelfde oorsprong?",
                  "de chloroplast", WW),
             ]),
        dict(kop="Buiten het membraan",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Waaruit bestaat de celwand van een plant?", "cellulose", W),
                 ("kort", "Waaruit bestaat de celwand van een schimmel?", "chitine", W),
                 ("kies", "Welke uitstulping van het celmembraan vergroot bij een darmcel het "
                          "opnameoppervlak?",
                  ["een flagel", "microvilli", "een pseudopode", "een plasmodesma"], 1),
                 ("open", "Waarom blijven cellen klein, ook bij een groot organisme?",
                  "Bij een grotere cel groeit het volume sneller dan de oppervlakte. Er is dan per "
                  "eenheid volume te weinig membraan om stoffen uit te wisselen. Een groot "
                  "organisme maakt daarom méér cellen in plaats van grotere.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-celdifferentiatie-weefsels-en-celtypes-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Celdifferentiatie, weefsels en celtypes",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van deling tot differentiatie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men het proces waarbij een cel zich specialiseert?",
                  "celdifferentiatie", WW),
                 ("open", "Alle cellen van je lichaam hebben hetzelfde DNA. Hoe kan een spiercel dan "
                          "zo verschillen van een zenuwcel?",
                  "Elke cel gebruikt maar een deel van haar genen. Welke genen aan staan, bepaalt "
                  "welke eiwitten de cel maakt, en dus wat ze kan.", 4),
                 ("kort", "Hoe noemt men een cel die zich nog tot verschillende celtypes kan "
                          "ontwikkelen?",
                  "een stamcel", WW),
             ]),
        dict(kop="De weefsels van een plant",
             opdracht="Schrijf de naam van het weefsel.",
             oefeningen=[
                 ("rij", [("voert water en mineralen naar boven", "xyleem"),
                          ("verdeelt opgeloste suikers over de plant", "floëem"),
                          ("deelt en zorgt voor de groei", "meristeem")], None, WW),
                 ("rij", [("bedekt en beschermt de buitenkant", "epidermis"),
                          ("staat rechtop onder de bovenkant van het blad", "palissadeparenchym"),
                          ("geeft stevigheid aan een stengel", "steunweefsel")], None, WW),
                 ("open", "Een wortelhaar is een lange, dunne uitloper van een huidcel. Welk voordeel "
                          "geeft die vorm?",
                  "Ze vergroot het oppervlak waarmee de wortel water en mineralen opneemt.", 3),
             ]),
        dict(kop="De weefsels van een dier",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Weefsel", "Waar je het vindt", "Wat het doet"],
                  [["epitheelweefsel", None, None], ["spierweefsel", None, None],
                   ["zenuwweefsel", None, None], ["bindweefsel", None, None]],
                  "Epitheelweefsel ligt op de huid en op de binnenwand van darm en longen, en "
                  "bedekt en beschermt. Spierweefsel zit in de spieren, het hart en de darmwand, en "
                  "zorgt voor beweging. Zenuwweefsel zit in de hersenen en de zenuwen, en geleidt "
                  "impulsen. Bindweefsel zit tussen de organen en in pezen en bot, en verbindt en "
                  "steunt.", WW),
             ]),
        dict(kop="Bijzondere cellen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Een rijpe rode bloedcel van de mens heeft geen kern meer. Wat levert dat "
                          "haar op, en wat kost het haar?",
                  "Zonder kern is er meer plaats voor hemoglobine, dus kan ze meer zuurstof "
                  "vervoeren. Maar ze kan zich niet meer delen en niets meer herstellen, en gaat "
                  "daardoor na ongeveer honderdtwintig dagen kapot.", 4),
                 ("kort", "Hoeveel chromosomen heeft een menselijke gameet?", "23", "90px"),
                 ("open", "Een zenuwcel heeft een heel lange uitloper. Waarom past die vorm bij haar "
                          "taak?",
                  "Ze moet een impuls over een grote afstand doorgeven, soms van je rug tot je "
                  "voet, en kan dat met één cel in plaats van met een rij overdrachten.", 3),
                 ("waar", "Een gedifferentieerde cel kan zich altijd nog tot elk ander celtype "
                          "ontwikkelen.", False),
             ]),
        dict(kop="Organisatieniveaus",
             opdracht="Zet in de juiste volgorde, van klein naar groot. Nummer van 1 tot 5.",
             oefeningen=[
                 ("rij", [("orgaan", "3"), ("cel", "1"), ("weefsel", "2")], "Nummer", "70px"),
                 ("rij", [("organisme", "5"), ("orgaanstelsel", "4")], "Nummer", "70px"),
                 ("open", "Leg met de darm als voorbeeld uit wat het verschil is tussen een "
                          "weefsel en een orgaan.",
                  "Een weefsel is een groep gelijkaardige cellen met één taak, zoals het "
                  "spierweefsel in de darmwand. Een orgaan bestaat uit verschillende weefsels die "
                  "samen een functie vervullen: de darm heeft epitheel, spier-, bind- en "
                  "zenuwweefsel samen.", 5),
             ]),
        dict(kop="Stamcellen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een embryonale en een adulte stamcel?",
                  "Een embryonale stamcel kan nog elk celtype worden. Een adulte stamcel, zoals in "
                  "het beenmerg, kan nog maar een beperkte groep celtypes worden.", 4),
                 ("open", "Waarom zijn stamcellen interessant voor de geneeskunde?",
                  "Je kan er beschadigd weefsel mee laten herstellen, bijvoorbeeld bloedcellen bij "
                  "een beenmergtransplantatie.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-enzymen-transport-door-membranen-en-osmose-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Enzymen, transport door membranen en osmose",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat een enzym doet",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Welke grootheid verlaagt een enzym, zodat de reactie sneller gaat?",
                  "de activeringsenergie", WL),
                 ("kort", "Hoe noemt men de stof waarop een enzym inwerkt?", "het substraat", WW),
                 ("kort", "Hoe noemt men de plaats op het enzym waar het substraat past?",
                  "de actieve plaats", WW),
                 ("open", "Waarom werkt amylase alleen op zetmeel en niet op een eiwit?",
                  "De actieve plaats van een enzym heeft een vorm die maar op één soort substraat "
                  "past. Een eiwit past daar niet in. Dat heet substraatspecificiteit.", 4),
             ]),
        dict(kop="Sneller of trager?",
             opdracht="Schrijf sneller, trager of geen verschil.",
             oefeningen=[
                 ("rij", [("de temperatuur stijgt van 20 naar 37 °C", "sneller"),
                          ("de temperatuur stijgt van 37 naar 70 °C", "trager"),
                          ("er komt meer substraat bij, met evenveel enzym", "sneller")],
                  None, W),
                 ("rij", [("de pH gaat van 7 naar 2 bij een darmenzym", "trager"),
                          ("er komt meer enzym bij, met veel substraat", "sneller"),
                          ("er komt een competitieve remmer bij", "trager")], None, W),
                 ("open", "Een enzym dat tot 70 °C verhit is, werkt ook na afkoelen niet meer. "
                          "Waarom niet?",
                  "Door de hitte is het eiwit gedenatureerd: zijn ruimtelijke vouw is uiteengevallen "
                  "en zijn actieve plaats bestaat niet meer. Die vouw komt bij afkoelen niet terug.",
                  4),
             ]),
        dict(kop="Welk transport?",
             opdracht="Schrijf diffusie, osmose, gefaciliteerde diffusie of actief transport.",
             oefeningen=[
                 ("rij", [("zuurstof dat zomaar door het membraan glijdt", "diffusie"),
                          ("glucose dat via een eiwitkanaal mee met de gradiënt gaat",
                           "gefaciliteerde diffusie"),
                          ("natrium dat met ATP tegen de gradiënt in gepompt wordt",
                           "actief transport")], None, WL),
                 ("rij", [("water dat naar de kant met meer opgeloste stof trekt", "osmose"),
                          ("koolstofdioxide dat uit een cel wegglijdt", "diffusie"),
                          ("jodium dat door een schildkliercel opgeslorpt wordt tot een hoge "
                           "concentratie", "actief transport")], None, WL),
                 ("waar", "Passief transport kost de cel ATP.", False),
             ]),
        dict(kop="Osmose doorrekenen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet een oplossing met méér opgeloste stof dan de cel?",
                  "hypertoon", W),
                 ("open", "Je legt een rode bloedcel in zuiver water. Wat gebeurt er, en hoe heet "
                          "dat?",
                  "Water stroomt naar binnen, want binnen is de concentratie opgeloste stof hoger. "
                  "De cel zwelt op en barst. Dat heet lyse of hemolyse.", 4),
                 ("open", "Je legt een plantencel in een sterke zoutoplossing. Wat gebeurt er, en "
                          "hoe heet dat?",
                  "Water stroomt naar buiten. De cel verslapt en het celmembraan komt van de "
                  "celwand los. Dat heet plasmolyse.", 4),
                 ("open", "Waarom barst een plantencel in zuiver water niet open, en een dierlijke "
                          "cel wel?",
                  "De plantencel heeft een stevige celwand die de druk tegenhoudt. Ze wordt stevig "
                  "of turgescent in plaats van te barsten. Een dierlijke cel heeft alleen een "
                  "membraan.", 4),
             ]),
        dict(kop="Grote stukken naar binnen en buiten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een cel neemt een groot deeltje op in een blaasje", "endocytose"),
                          ("een cel stoot de inhoud van een blaasje uit", "exocytose"),
                          ("een witte bloedcel slorpt een bacterie op", "fagocytose")], None, WW),
                 ("kort", "Hoe noemt men het opnemen van vocht met opgeloste stoffen in een blaasje?",
                  "pinocytose", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-fotosynthese-celademhaling-en-gisting-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Fotosynthese, celademhaling en gisting",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee vergelijkingen",
             opdracht="Schrijf de vergelijking uit.",
             oefeningen=[
                 ("kort", "De reactievergelijking van de fotosynthese.",
                  "6 CO2 + 6 H2O geeft C6H12O6 + 6 O2", WL),
                 ("kort", "De reactievergelijking van de aerobe celademhaling.",
                  "C6H12O6 + 6 O2 geeft 6 CO2 + 6 H2O en energie", WL),
                 ("open", "Waarom zegt men dat die twee processen in elkaar passen?",
                  "De producten van de ene zijn de grondstoffen van de andere. Glucose en zuurstof "
                  "uit de fotosynthese zijn wat de celademhaling verbruikt, en haar koolstofdioxide "
                  "en water zijn wat de fotosynthese nodig heeft.", 4),
             ]),
        dict(kop="Waar gebeurt het?",
             opdracht="Schrijf de plaats in de cel.",
             oefeningen=[
                 ("rij", [("de lichtreacties", "thylakoïdmembraan"),
                          ("de Calvincyclus", "stroma van de chloroplast"),
                          ("de glycolyse", "cytoplasma")], "Waar?", WL),
                 ("rij", [("de citroenzuurcyclus", "matrix van het mitochondrion"),
                          ("de eindoxidaties", "cristae van het mitochondrion"),
                          ("de melkzuurgisting", "cytoplasma")], "Waar?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De Calvincyclus kan alleen in volledige duisternis plaatsvinden.", False),
                 ("waar", "De zuurstof die een plant afgeeft, komt uit het gesplitste water.", True),
                 ("waar", "Een plant doet alleen aan fotosynthese en nooit aan celademhaling.",
                  False),
                 ("waar", "De glycolyse levert meer ATP op dan alles wat er in het mitochondrion "
                          "gebeurt.", False),
             ]),
        dict(kop="Gisting",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Gisting", "Producten", "Een toepassing"],
                  [["melkzuurgisting", None, None], ["alcoholische gisting", None, None]],
                  "Melkzuurgisting geeft melkzuur en een kleine hoeveelheid energie; "
                  "melkzuurbacteriën maken er yoghurt van melk mee. Alcoholische gisting geeft "
                  "ethanol, koolstofdioxide en een kleine hoeveelheid energie; gist doet daarmee "
                  "brooddeeg rijzen.", WW),
                 ("open", "Waarom levert gisting veel minder energie dan de aerobe celademhaling?",
                  "De glucose wordt maar gedeeltelijk afgebroken. In melkzuur en in ethanol zit nog "
                  "een hoop energie die de cel laat liggen.", 3),
                 ("open", "Een sprinter voelt na honderd meter zijn benen verzuren. Leg uit wat er "
                          "in zijn spiercellen gebeurd is.",
                  "Er was te weinig zuurstof voor de aerobe ademhaling, dus werd het "
                  "pyrodruivenzuur tot melkzuur omgezet. Dat melkzuur hoopt zich op, en dat voelt "
                  "hij als verzuring.", 4),
             ]),
        dict(kop="Een proef uitleggen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom zet je een plant een nacht in het donker voor je een proef over "
                          "fotosynthese start?",
                  "Om het aanwezige zetmeel uit de bladeren te laten verdwijnen. Anders weet je "
                  "niet of het zetmeel dat je achteraf vindt, van de proef komt.", 3),
                 ("kort", "Met welke stof toon je zetmeel in een blad aan?", "joodoplossing", WW),
                 ("open", "Een waterplant staat onder een omgekeerde trechter met een proefbuisje. "
                          "Je zet de lamp dichter en dichter bij. Wat verwacht je, en waar stopt het "
                          "effect?",
                  "Er komen meer gasbelletjes per minuut, want er is meer licht voor de "
                  "lichtreacties. Vanaf een bepaalde afstand stijgt het niet meer: dan is een "
                  "andere factor, zoals de koolstofdioxide of de temperatuur, de beperkende factor.",
                  5),
             ]),
        dict(kop="ATP",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Wat wordt ATP als het één fosfaatgroep afgeeft?", "ADP", "90px"),
                 ("kies", "Hoe noemt men een reactie waarbij energie vrijkomt?",
                  ["endo-energetisch", "exo-energetisch", "neutraal"], 1),
                 ("open", "Noem drie processen waarvoor een cel ATP gebruikt.",
                  "De samentrekking van een spier, het pompen van ionen tegen hun gradiënt in, en "
                  "het opbouwen van grote moleculen zoals eiwitten.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-niet-specifieke-en-specifieke-afweer-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Niet-specifieke en specifieke afweer",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke verdedigingslijn?",
             opdracht="Schrijf eerste, tweede of derde lijn.",
             oefeningen=[
                 ("rij", [("de onbeschadigde huid", "eerste"),
                          ("een macrofaag die een bacterie opslorpt", "tweede"),
                          ("een plasmacel die antilichamen maakt", "derde")], None, W),
                 ("rij", [("het zure maagsap", "eerste"),
                          ("koorts", "tweede"),
                          ("een cytotoxische T-cel die een besmette cel doodt", "derde")],
                  None, W),
             ]),
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men een lichaamsvreemde stof die een afweerreactie uitlokt?",
                  "een antigen", WW),
                 ("kort", "Hoe noemt men het eiwit dat een B-cel tegen één antigen maakt?",
                  "een antilichaam", WW),
                 ("kort", "Hoe noemt men een ziekteverwekker in het algemeen?", "een pathogeen",
                  WW),
                 ("kies", "Wat is géén ziekteverwekker die zich enkel in een levende cel kan "
                          "vermenigvuldigen?",
                  ["een bacterie", "een virus", "een prion"], 0),
             ]),
        dict(kop="Welke cel doet wat?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Cel", "Wat ze doet"],
                  [["macrofaag", None], ["T-helpercel", None], ["cytotoxische T-cel", None],
                   ["plasmacel", None], ["geheugencel", None]],
                  "Een macrofaag slorpt indringers op en toont hun antigenen. Een T-helpercel "
                  "dirigeert de hele reactie door de andere cellen te activeren. Een cytotoxische "
                  "T-cel doodt besmette lichaamscellen. Een plasmacel maakt grote hoeveelheden "
                  "antilichamen. Een geheugencel blijft jaren bestaan en maakt de tweede reactie "
                  "veel sneller.", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Koorts is altijd schadelijk en moet onmiddellijk weggewerkt worden.",
                  False),
                 ("waar", "De niet-specifieke afweer werkt meteen, maar onthoudt niets.", True),
                 ("waar", "Een ontsteking is een teken dat de afweer niet werkt.", False),
                 ("waar", "Antibiotica werken ook tegen virussen.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom helpt een lichte verhoging van de lichaamstemperatuur bij een "
                          "infectie?",
                  "Veel bacteriën en virussen vermenigvuldigen zich minder goed bij een hogere "
                  "temperatuur, terwijl de afweercellen sneller werken.", 3),
                 ("open", "Waarom word je de tweede keer dat je met hetzelfde virus in contact komt "
                          "meestal niet meer ziek?",
                  "Er zijn geheugencellen van de eerste keer overgebleven. Die herkennen het "
                  "antigen meteen en laten snel grote hoeveelheden antilichamen maken, nog voor je "
                  "iets voelt.", 4),
                 ("open", "Waarom is een brandwond gevaarlijker dan een gelijkaardige blauwe plek?",
                  "Bij een brandwond is de huid, de eerste verdedigingslijn, kapot. Ziekteverwekkers "
                  "kunnen daar zo binnen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-immunisatie-bloedgroepen-en-falende-afweer-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Immunisatie, bloedgroepen en falende afweer",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke immunisatie?",
             opdracht="Schrijf actief natuurlijk, actief kunstmatig, passief natuurlijk of passief "
                      "kunstmatig.",
             oefeningen=[
                 ("rij", [("je maakt zelf antilichamen na een griep",
                           "actief natuurlijk"),
                          ("je krijgt een vaccin", "actief kunstmatig"),
                          ("een baby krijgt antilichamen via de moedermelk",
                           "passief natuurlijk")], None, WL),
                 ("rij", [("je krijgt na een beet antilichamen tegen tetanus ingespoten",
                           "passief kunstmatig"),
                          ("antilichamen gaan door de placenta naar de foetus",
                           "passief natuurlijk"),
                          ("je maakt antilichamen na een waterpokkenbesmetting",
                           "actief natuurlijk")], None, WL),
                 ("open", "Waarom werkt ingespoten antilichaam meteen, en een vaccin niet?",
                  "Bij ingespoten antilichamen zijn de antilichamen er al. Bij een vaccin moet het "
                  "lichaam ze nog zelf aanmaken, en dat duurt dagen tot weken. Daarom beschermt het "
                  "vaccin wel lang en de inspuiting maar kort.", 5),
             ]),
        dict(kop="Bloedgroepen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Bloedgroep", "Antigen op de bloedcel", "Antilichaam in het plasma"],
                  [["A", None, None], ["B", None, None], ["AB", None, None], ["O", None, None]],
                  "Groep A heeft antigen A en antilichaam anti-B. Groep B heeft antigen B en "
                  "anti-A. Groep AB heeft A en B en geen van beide antilichamen. Groep O heeft geen "
                  "antigen en zowel anti-A als anti-B.", WW),
                 ("kort", "Welke groep is de universele donor?", "O", "90px"),
                 ("kort", "Welke groep is de universele ontvanger?", "AB", "90px"),
                 ("open", "Waarom mag iemand met groep A geen bloed van groep B krijgen?",
                  "In zijn plasma zit anti-B. Dat antilichaam klontert de toegediende bloedcellen "
                  "samen, en dat kan de bloedvaten verstoppen.", 4),
                 ("open", "Wat is de resusfactor, en waarom let men erop bij een zwangerschap?",
                  "Dat is een extra antigen, de D-factor, op de rode bloedcellen. Is de moeder "
                  "resusnegatief en het kind positief, dan kan de moeder antilichamen maken die een "
                  "volgend kind kunnen aanvallen.", 5),
             ]),
        dict(kop="Als de afweer misloopt",
             opdracht="Schrijf allergie, auto-immuunziekte of immuundeficiëntie.",
             oefeningen=[
                 ("rij", [("hooikoorts", "allergie"),
                          ("type 1 diabetes", "auto-immuunziekte"),
                          ("aids", "immuundeficiëntie")], None, WW),
                 ("rij", [("multiple sclerose", "auto-immuunziekte"),
                          ("een pindanotenallergie", "allergie"),
                          ("reumatoïde artritis", "auto-immuunziekte")], None, WW),
                 ("open", "Wat is het verschil tussen een allergie en een auto-immuunziekte?",
                  "Bij een allergie reageert de afweer veel te heftig op iets onschuldigs van "
                  "buiten. Bij een auto-immuunziekte valt de afweer lichaamseigen cellen aan.", 4),
                 ("open", "Waarom is hiv zo gevaarlijk, terwijl het zelf meestal niet dodelijk is?",
                  "Het virus valt de T-helpercel aan, de dirigent van de afweer. Zonder die cel kan "
                  "het lichaam zich tegen bijna niets meer verdedigen, en gewone infecties worden "
                  "dan dodelijk.", 5),
                 ("waar", "Een orgaantransplantatie wordt afgestoten omdat de afweer de vreemde "
                          "antigenen van de donor herkent.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-gametogenese-en-de-hormonale-regeling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Gametogenese en de hormonale regeling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Oögenese en spermatogenese naast elkaar",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Oögenese", "Spermatogenese"],
                  [["waar", None, None], ["aantal cellen per meiose", None, None],
                   ["wanneer begint het", None, None], ["hoelang gaat het door", None, None]],
                  "De oögenese gebeurt in de eierstok, de spermatogenese in de teelbal. Eén meiose "
                  "geeft bij de vrouw één eicel en poollichaampjes, bij de man vier zaadcellen. De "
                  "oögenese begint al voor de geboorte, de spermatogenese vanaf de puberteit. De "
                  "oögenese stopt bij de menopauze, de spermatogenese gaat levenslang door.", WW),
                 ("open", "Waarom geeft één meiose bij de vrouw maar één bruikbare cel?",
                  "Bij elke deling gaat bijna al het cytoplasma naar één cel. Die krijgt dus een "
                  "grote voorraad mee voor de eerste dagen na de bevruchting. De poollichaampjes "
                  "gaan verloren.", 4),
             ]),
        dict(kop="Welk hormoon?",
             opdracht="Schrijf de naam van het hormoon.",
             oefeningen=[
                 ("rij", [("laat een follikel rijpen", "FSH"),
                          ("lokt met een plotse piek de ovulatie uit", "LH"),
                          ("laat het baarmoederslijmvlies dikker worden", "oestrogeen")],
                  None, WW),
                 ("rij", [("wordt door het geel lichaam gemaakt", "progesteron"),
                          ("houdt het geel lichaam na een bevruchting in stand", "hCG"),
                          ("zet in de teelbal de zaadcelvorming aan", "testosteron")], None, WW),
             ]),
        dict(kop="De cyclus",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Op welke dag van een cyclus van 28 dagen valt de ovulatie meestal?",
                  "dag 14", W),
                 ("open", "Wat gebeurt er met het geel lichaam als er geen bevruchting is, en wat "
                          "is het gevolg?",
                  "Het valt na ongeveer twee weken uiteen. Daardoor zakt het progesteron, het "
                  "baarmoederslijmvlies wordt niet meer in stand gehouden en de menstruatie begint.",
                  4),
                 ("open", "Leg uit wat negatieve feedback in deze regeling betekent, met een "
                          "voorbeeld.",
                  "Een hoog hormoonpeil remt zijn eigen aansturing af. Veel oestrogeen remt de "
                  "afgifte van FSH, zodat er niet nog meer follikels gaan rijpen.", 4),
                 ("waar", "Na de menopauze kan een nieuwe eicel nog rijpen.", False),
             ]),
        dict(kop="De zaadcel",
             opdracht="Schrijf bij elk deel wat het doet.",
             oefeningen=[
                 ("tabel", ["Deel van de zaadcel", "Waarvoor het dient"],
                  [["acrosoom", None], ["kop", None], ["middenstuk", None], ["staart of flagel", None]],
                  "Het acrosoom bevat enzymen om door de omhulling van de eicel te dringen. In de "
                  "kop zit het haploïde DNA. Het middenstuk zit vol mitochondriën en levert de "
                  "energie. De staart zorgt voor de voortbeweging.", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een vrouw maakt na de puberteit elke maand nieuwe eicellen aan.", False),
                 ("waar", "De spermatogenese gaat bij een man levenslang door.", True),
                 ("waar", "Het geel lichaam ontstaat uit de follikel die net gesprongen is.", True),
                 ("waar", "Een eicel is diploïd, een zaadcel haploïd.", False),
             ]),
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het springen van de follikel", "de ovulatie"),
                          ("de kleine cellen die bij de oögenese verloren gaan",
                           "de poollichaampjes"),
                          ("de plaats waar de zaadcellen rijpen", "de bijbal")], None, WW),
                 ("kort", "Hoeveel dagen duurt de rijping van een zaadcel ongeveer?",
                  "ongeveer 70 dagen", WW),
                 ("open", "Waarom hangen de teelballen buiten de buikholte?",
                  "De zaadcelvorming vraagt een temperatuur die een paar graden onder de "
                  "lichaamstemperatuur ligt.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-bevruchting-embryo-en-foetus-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bevruchting, embryo en foetus",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De eerste dagen op een rij",
             opdracht="Nummer van 1 tot 6 in de juiste volgorde.",
             oefeningen=[
                 ("rij", [("de bevruchting in de eileider", "1"),
                          ("de eerste klievingsdeling", "2"),
                          ("de morula", "3")], "Nummer", "70px"),
                 ("rij", [("de blastula met een holte", "4"),
                          ("de innesteling in het baarmoederslijmvlies", "5"),
                          ("de vorming van de placenta", "6")], "Nummer", "70px"),
                 ("kort", "Waar vindt de bevruchting normaal plaats?", "in de eileider", WW),
                 ("kort", "Hoeveel dagen na de bevruchting nestelt de kiem zich ongeveer in?",
                  "ongeveer zes tot zeven dagen", WL),
             ]),
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men de bevruchte eicel?", "de zygote", WW),
                 ("open", "Waarom wordt de kiem tijdens de klievingsdelingen niet groter, terwijl "
                          "het aantal cellen wel stijgt?",
                  "De cellen delen zich zonder eerst te groeien. De bestaande massa wordt dus in "
                  "steeds kleinere cellen verdeeld.", 3),
                 ("waar", "Na de bevruchting kan een tweede zaadcel nog binnendringen.", False),
                 ("open", "Wat is het verschil tussen een eeneiige en een twee-eiige tweeling?",
                  "Een eeneiige tweeling komt uit één bevruchte eicel die in twee gesplitst is, en "
                  "de twee zijn dus genetisch gelijk. Een twee-eiige tweeling komt uit twee eicellen "
                  "en twee zaadcellen, en die twee lijken niet meer op elkaar dan gewone broers of "
                  "zussen.", 5),
             ]),
        dict(kop="De drie kiembladen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Kiemblad", "Waaruit het ontstaat"],
                  [["ectoderm", None], ["mesoderm", None], ["endoderm", None]],
                  "Uit het ectoderm komen de huid en het zenuwstelsel. Uit het mesoderm komen de "
                  "spieren, het skelet, het bloed en de nieren. Uit het endoderm komen de "
                  "binnenwand van de darm, de lever en de longen.", WL),
             ]),
        dict(kop="De placenta en de geboorte",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Het bloed van de moeder en dat van het kind raken elkaar in de placenta "
                          "niet. Hoe gaan zuurstof en voedsel dan over?",
                  "Door diffusie over een heel dun membraan tussen de twee bloedsomlopen. De "
                  "bloedgroepen kunnen zo verschillen zonder gevaar.", 4),
                 ("kort", "Hoe heet het bloedvat dat kind en placenta verbindt?", "de navelstreng",
                  WW),
                 ("kort", "Welk hormoon lokt de weeën uit?", "oxytocine", WW),
                 ("open", "Vanaf wanneer spreekt men van een foetus in plaats van een embryo, en "
                          "waarom valt de grens daar?",
                  "Vanaf ongeveer de negende week. Dan zijn alle organen aangelegd en gaat het "
                  "vooral nog om groeien en verfijnen.", 4),
             ]),
        dict(kop="Wat de ontwikkeling kan storen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men een stof die de ontwikkeling van een kiem kan schaden?",
                  "een teratogeen", WW),
                 ("open", "Waarom zijn de eerste acht weken van een zwangerschap de gevoeligste?",
                  "In die weken worden alle organen aangelegd. Een storing op dat moment heeft "
                  "veel grotere gevolgen dan later, wanneer de organen alleen nog groeien.", 4),
                 ("open", "Noem drie dingen die een zwangere beter vermijdt, met telkens de reden.",
                  "Alcohol, want dat gaat door de placenta en schaadt de hersenontwikkeling. Roken, "
                  "want dat vermindert de zuurstoftoevoer. En rauw vlees of ongewassen groenten, "
                  "want daarin kunnen ziekteverwekkers zoals toxoplasma zitten.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vruchtbaarheid-regelen-en-behandelen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vruchtbaarheid regelen en behandelen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort methode?",
             opdracht="Schrijf natuurlijk, barrière, hormonaal of chirurgisch.",
             oefeningen=[
                 ("rij", [("het condoom", "barrière"),
                          ("de pil", "hormonaal"),
                          ("de temperatuurmethode", "natuurlijk")], None, WW),
                 ("rij", [("de sterilisatie", "chirurgisch"),
                          ("het pessarium", "barrière"),
                          ("de prikpil", "hormonaal")], None, WW),
                 ("kort", "Welk middel beschermt ook tegen soa's?", "het condoom", WW),
             ]),
        dict(kop="Hoe werkt het?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Middel", "Hoe het werkt"],
                  [["de pil", None], ["het condoom", None], ["het koperspiraaltje", None],
                   ["de morning-afterpil", None]],
                  "De pil houdt met hormonen de LH-piek tegen, en dus de ovulatie. Het condoom "
                  "houdt de zaadcellen mechanisch tegen. Het koperspiraaltje maakt de baarmoeder "
                  "ongunstig voor zaadcellen en voor innesteling. De morning-afterpil stelt de "
                  "ovulatie uit of verhindert ze, en werkt dus vóór de bevruchting.", WL),
                 ("open", "Wat is het verschil tussen de morning-afterpil en de abortuspil?",
                  "De morning-afterpil voorkomt dat er een zwangerschap ontstaat. De abortuspil "
                  "beëindigt een zwangerschap die al bestaat.", 4),
             ]),
        dict(kop="Betrouwbaarheid",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Hoe noemt men het cijfer dat de betrouwbaarheid van een "
                          "voorbehoedsmiddel uitdrukt?",
                  "de pearlindex", WW),
                 ("open", "Waarom is de temperatuurmethode minder betrouwbaar dan de pil?",
                  "Ze berust op het vaststellen van de ovulatie achteraf, en de lichaamstemperatuur "
                  "wordt ook door ziekte, slaap en stress beïnvloed. De cyclus is bovendien niet "
                  "bij iedereen even regelmatig.", 5),
                 ("waar", "Een lage pearlindex betekent dat een middel betrouwbaar is.", True),
             ]),
        dict(kop="Bij een kinderwens",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de eicel wordt in een schaaltje bij zaadcellen gebracht", "IVF"),
                          ("één zaadcel wordt met een naald in de eicel gespoten", "ICSI"),
                          ("zaadcellen worden in de baarmoeder gebracht", "inseminatie")],
                  None, W),
                 ("open", "Bij welk probleem is ICSI nuttiger dan gewone IVF?",
                  "Als de zaadcellen te weinig beweeglijk zijn of te klein in aantal, zodat ze op "
                  "eigen kracht de eicel niet binnendringen.", 4),
                 ("open", "Noem vier dingen die de vruchtbaarheid van beide partners verlagen.",
                  "Roken, veel alcohol, overgewicht of sterk ondergewicht, en langdurige stress. "
                  "Ook de leeftijd speelt bij beiden mee.", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De pil beschermt ook tegen soa's.", False),
                 ("waar", "Een sterilisatie is bedoeld als een definitieve ingreep.", True),
                 ("waar", "De morning-afterpil werkt hoe vroeger ze genomen wordt, hoe beter.",
                  True),
                 ("waar", "Bij IVF gebeurt de bevruchting in de eileider.", False),
             ]),
        dict(kop="Een gesprek",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Iemand zegt dat hij geen condoom nodig heeft omdat zijn partner de pil "
                          "neemt. Wat antwoord je?",
                  "De pil voorkomt een zwangerschap, maar beschermt niet tegen soa's. Daarvoor is "
                  "een condoom nodig.", 4),
                 ("open", "Waarom wordt een koppel met een kinderwens aangeraden om bij beide "
                          "partners onderzoek te laten doen?",
                  "De oorzaak kan bij elk van beiden liggen, en vaak bij beiden tegelijk. Alleen "
                  "de ene onderzoeken laat de helft van de mogelijke oorzaken liggen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-dna-rna-en-de-replicatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="DNA, RNA en de replicatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De complementaire streng",
             opdracht="Schrijf de complementaire DNA-streng op.",
             oefeningen=[
                 ("rij", [("A T G C C A", "T A C G G T"),
                          ("G G A T T C", "C C T A A G"),
                          ("C A T G A T", "G T A C T A")], "Complement", WL),
                 ("rij", [("T A C G G A T", "A T G C C T A"),
                          ("A A T C G C", "T T A G C G")], "Complement", WL),
                 ("kort", "Schrijf het mRNA dat bij de DNA-streng A T G C C A hoort.",
                  "U A C G G U", WW),
             ]),
        dict(kop="DNA of RNA?",
             opdracht="Schrijf DNA, RNA of beide.",
             oefeningen=[
                 ("rij", [("bevat de base uracil", "RNA"),
                          ("bevat de base thymine", "DNA"),
                          ("bevat de base guanine", "beide")], None, W),
                 ("rij", [("heeft deoxyribose als suiker", "DNA"),
                          ("is meestal enkelstrengig", "RNA"),
                          ("bevat fosfaatgroepen", "beide")], None, W),
             ]),
        dict(kop="Rekenen met Chargaff",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "In een DNA-staal is 30 % van de basen adenine. Hoeveel procent is "
                          "thymine?",
                  "30 %", "90px"),
                 ("kort", "Hoeveel procent is dan guanine?", "20 %", "90px"),
                 ("open", "Leg uit waarom je dat kan berekenen.",
                  "A hoort altijd bij T en C altijd bij G, dus A is gelijk aan T en C aan G. Samen "
                  "is alles 100 %. Is A 30 %, dan is T ook 30 %, blijft er 40 % voor C en G samen, "
                  "en dus 20 % elk.", 5),
             ]),
        dict(kop="Van DNA tot chromosoom",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men de eiwitten waarrond het DNA opgewonden zit?",
                  "histonen", WW),
                 ("kort", "Hoe heet DNA met histonen samen?", "chromatine", WW),
                 ("kort", "Hoe noemt men de plaats waar de twee chromatiden samenhangen?",
                  "het centromeer", WW),
                 ("open", "Waarom is het nodig dat het DNA zo sterk opgewonden wordt?",
                  "In één menselijke cel zit samen ongeveer twee meter DNA. Dat moet in een kern van "
                  "een paar micrometer passen, en bij een deling netjes verdeeld kunnen worden.", 4),
             ]),
        dict(kop="De replicatie",
             opdracht="Schrijf bij elke taak het enzym.",
             oefeningen=[
                 ("rij", [("windt de dubbele helix open", "helicase"),
                          ("legt een kort beginstukje RNA aan", "primase"),
                          ("bouwt de nieuwe streng op van 5' naar 3'", "DNA-polymerase")],
                  None, WW),
                 ("rij", [("plakt de losse stukken aan elkaar", "ligase"),
                          ("haalt de spanning uit de opgewonden helix", "topo-isomerase")],
                  None, WW),
                 ("open", "Wat betekent het dat de replicatie semiconservatief is?",
                  "Elke nieuwe dubbele helix bestaat uit één oude streng, die als mal gediend "
                  "heeft, en één nieuw gebouwde streng.", 4),
                 ("open", "Waarom wordt de ene nieuwe streng in één stuk gebouwd en de andere in "
                          "stukjes?",
                  "Polymerase kan alleen van 5' naar 3' bouwen, en de twee strengen lopen "
                  "antiparallel. Aan de ene kant kan het dus meelopen met de opengaande vork, aan "
                  "de andere kant moet het telkens een stukje terug: dat geeft de losse stukken, de "
                  "okazakifragmenten.", 5),
                 ("waar", "Na de replicatie heeft de cel twee volledig nieuwe dubbele helices, "
                          "zonder één oude streng.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-celcyclus-mitose-en-meiose-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De celcyclus, mitose en meiose",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De celcyclus",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de cel groeit en maakt eiwitten aan", "G1-fase"),
                          ("het DNA wordt verdubbeld", "S-fase"),
                          ("de cel controleert en bereidt de deling voor", "G2-fase")],
                  None, WW),
                 ("kort", "Hoe noemen G1, S en G2 samen?", "de interfase", WW),
                 ("kort", "Hoe noemt men de fase waarin de cel zich echt deelt?", "de M-fase", WW),
                 ("open", "Waarom staan er controlepunten in de celcyclus?",
                  "Om na te gaan of alles in orde is voor de cel verder gaat: of het DNA zonder "
                  "fouten gekopieerd is en of de chromosomen goed vastzitten. Zo wordt een fout "
                  "niet doorgegeven.", 4),
             ]),
        dict(kop="Welke fase van de mitose?",
             opdracht="Schrijf profase, metafase, anafase of telofase.",
             oefeningen=[
                 ("rij", [("de chromosomen worden kort en dik en het kernmembraan verdwijnt",
                           "profase"),
                          ("de chromosomen staan op één lijn in het midden", "metafase"),
                          ("de chromatiden worden naar de polen getrokken", "anafase")], None, W),
                 ("rij", [("er vormen zich weer twee kernmembranen", "telofase"),
                          ("de trekdraden hechten aan de centromeren", "metafase")], None, W),
             ]),
        dict(kop="Mitose of meiose?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Mitose", "Meiose"],
                  [["aantal delingen", None, None], ["aantal dochtercellen", None, None],
                   ["chromosoomaantal erna", None, None],
                   ["zijn de dochtercellen gelijk", None, None],
                   ["waarvoor dient het", None, None]],
                  "De mitose is één deling, de meiose zijn er twee. De mitose geeft twee "
                  "dochtercellen, de meiose vier. Na de mitose is het aantal chromosomen gelijk "
                  "gebleven, na de meiose gehalveerd. De dochtercellen van de mitose zijn "
                  "genetisch identiek, die van de meiose alle verschillend. De mitose dient voor "
                  "groei en herstel, de meiose voor het maken van gameten.", WW),
             ]),
        dict(kop="Rekenen met chromosomen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", "Een cel met 46 chromosomen doet een mitose. Hoeveel chromosomen heeft "
                          "elke dochtercel?", "46", "90px"),
                 ("kort", "Dezelfde cel doet een meiose. Hoeveel chromosomen heeft elke gameet?",
                  "23", "90px"),
                 ("kort", "Hoeveel chromatiden heeft een cel met 46 chromosomen aan het einde van "
                          "de S-fase?", "92", "90px"),
                 ("open", "Een plant heeft 2n = 18. Hoeveel chromosomen zitten er in een stuifmeel"
                          "korrel, en waarom?",
                  "Negen. Een stuifmeelkorrel is een gameet en dus haploïd: de meiose heeft het "
                  "aantal gehalveerd.", 4),
             ]),
        dict(kop="Waarom is elke gameet anders?",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Hoe noemt men het uitwisselen van stukken tussen homologe chromosomen?",
                  "crossing-over", WW),
                 ("open", "Leg uit wat mixing of onafhankelijke verdeling betekent.",
                  "Bij de eerste meiotische deling gaat van elk chromosomenpaar toevallig de ene of "
                  "de andere kant op. Elke gameet krijgt dus een eigen mengeling van vaderlijke en "
                  "moederlijke chromosomen.", 4),
                 ("open", "Waarom is het voor een soort nuttig dat elke gameet verschilt?",
                  "Zo is er variatie in de nakomelingen. Verandert de omgeving, dan is er meer kans "
                  "dat er individuen zijn die er toch mee om kunnen.", 4),
                 ("waar", "Crossing-over gebeurt ook bij de mitose, net zoals bij de meiose.",
                  False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-overerving-en-de-wetten-van-mendel-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Overerving en de wetten van Mendel",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de allelen die een individu heeft", "het genotype"),
                          ("wat je aan het individu kan zien", "het fenotype"),
                          ("twee gelijke allelen", "homozygoot")], None, WW),
                 ("rij", [("twee verschillende allelen", "heterozygoot"),
                          ("het allel dat zich altijd toont", "dominant"),
                          ("het allel dat zich alleen zonder het andere toont", "recessief")],
                  None, WW),
             ]),
        dict(kop="Een monohybride kruising",
             opdracht="Schrijf het kruisingsschema uit en vul de verhoudingen in. Zwart (B) is "
                      "dominant over wit (b).",
             oefeningen=[
                 ("kort", "Welke gameten geeft een BB-dier?", "alleen B", W),
                 ("kort", "Welke gameten geeft een Bb-dier?", "B en b", W),
                 ("open", "Kruis Bb met Bb. Schrijf het schema uit en geef de verhouding van de "
                          "genotypes en van de fenotypes.",
                  "De gameten zijn B en b bij beide ouders. Het schema geeft BB, Bb, Bb en bb. De "
                  "genotypes staan dus 1 BB op 2 Bb op 1 bb, en de fenotypes 3 zwart op 1 wit.", 6),
                 ("open", "Kruis Bb met bb. Welke verhouding van de fenotypes verwacht je?",
                  "De helft Bb en de helft bb, dus 1 zwart op 1 wit.", 4),
                 ("open", "Een zwart dier wordt met een wit dier gekruist en er komen witte jongen "
                          "bij. Wat weet je nu over het genotype van het zwarte dier?",
                  "Het is heterozygoot, Bb. Was het BB, dan zouden alle jongen zwart zijn.", 4),
             ]),
        dict(kop="Een dihybride kruising",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", "Hoeveel verschillende gameten kan een AaBb-individu maken?", "vier",
                  "90px"),
                 ("kort", "Schrijf die vier gameten op.", "AB, Ab, aB en ab", WW),
                 ("kort", "Welke fenotypeverhouding verwacht je bij AaBb × AaBb?", "9 : 3 : 3 : 1",
                  WW),
                 ("open", "Hoeveel van de 16 vakjes in dat schema zijn dubbel recessief, en met "
                          "welk genotype?",
                  "Eén van de zestien, met genotype aabb.", 3),
             ]),
        dict(kop="Wat niet in het schema van Mendel past",
             opdracht="Schrijf intermediair, codominant, multipele allelie of X-gebonden.",
             oefeningen=[
                 ("rij", [("rood × wit geeft roze bloemen", "intermediair"),
                          ("bij groep AB zijn beide antigenen aanwezig", "codominant"),
                          ("de bloedgroep heeft drie allelen: A, B en O", "multipele allelie")],
                  None, WL),
                 ("rij", [("kleurenblindheid komt veel meer bij mannen voor", "X-gebonden"),
                          ("hemofilie gaat van grootvader via de moeder naar de kleinzoon",
                           "X-gebonden")], None, WL),
                 ("open", "Waarom komt een X-gebonden recessieve aandoening vaker bij mannen voor?",
                  "Een man heeft maar één X-chromosoom. Zit het allel daarop, dan heeft hij geen "
                  "tweede X met een gezond allel dat het kan opvangen. Een vrouw moet het op beide "
                  "X-chromosomen hebben.", 5),
                 ("waar", "Een vader kan zijn X-gebonden allel aan zijn zoon doorgeven.", False),
             ]),
        dict(kop="Een stamboom lezen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Een aandoening slaat in een stamboom een generatie over: de grootouders "
                          "hebben ze niet, de kleinkinderen wel. Wat besluit je over het allel?",
                  "Het is recessief. De tussengeneratie was heterozygoot drager en toonde de "
                  "aandoening dus niet, maar gaf het allel wel door.", 5),
                 ("open", "Twee gezonde ouders krijgen een kind met een recessieve aandoening. Wat "
                          "weet je over hun genotypes, en hoe groot was de kans?",
                  "Ze zijn beide heterozygoot drager. De kans per kind was één op vier.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-genexpressie-transcriptie-en-translatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Genexpressie: transcriptie en translatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van DNA naar eiwit",
             opdracht="Vul de rij aan. Gebruik de codontabel van je cursus waar nodig.",
             oefeningen=[
                 ("kort", "Schrijf het mRNA bij de DNA-streng T A C A A A G G T.",
                  "A U G U U U C C A", WL),
                 ("kort", "Hoeveel aminozuren codeert dat mRNA?", "drie", "90px"),
                 ("kort", "Welk codon start altijd de translatie?", "AUG", W),
                 ("kort", "Noem de drie stopcodons.", "UAA, UAG en UGA", WW),
             ]),
        dict(kop="De genetische code",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Uit hoeveel nucleotiden bestaat één codon?", "drie", "90px"),
                 ("open", "Er zijn 64 codons en maar 20 aminozuren. Wat betekent dat voor de code?",
                  "Meerdere codons kunnen hetzelfde aminozuur aanduiden. De code is dus "
                  "gedegenereerd of redundant. Daardoor verandert een mutatie het eiwit niet "
                  "altijd.", 4),
                 ("open", "Waarom kan een menselijk gen in een bacterie een werkend eiwit geven?",
                  "De genetische code is bij bijna alle organismen dezelfde. Een bacterieel "
                  "ribosoom leest dezelfde codons als een menselijk.", 4),
             ]),
        dict(kop="Transcriptie en translatie naast elkaar",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Transcriptie", "Translatie"],
                  [["waar in de cel", None, None], ["welk enzym of organel", None, None],
                   ["wat erin gaat", None, None], ["wat eruit komt", None, None]],
                  "De transcriptie gebeurt in de kern, door RNA-polymerase; er gaat DNA in en er "
                  "komt mRNA uit. De translatie gebeurt in het cytoplasma op het ribosoom; er gaat "
                  "mRNA in en er komt een polypeptideketen uit.", WW),
             ]),
        dict(kop="De rijping van het mRNA",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de stukken die uit het pre-mRNA geknipt worden", "introns"),
                          ("de stukken die aan elkaar geplakt blijven", "exons"),
                          ("het knippen en plakken zelf", "splicing")], None, WW),
                 ("open", "Noem twee dingen die er bij de rijping aan het mRNA toegevoegd worden, "
                          "en waarvoor ze dienen.",
                  "Een cap vooraan en een poly-A-staart achteraan. Ze beschermen het mRNA tegen "
                  "afbraak en helpen het de kern uit en op het ribosoom.", 4),
                 ("open", "Hoe kan één gen meerdere verschillende eiwitten geven?",
                  "Door alternatieve splicing: de cel kan andere exons samenvoegen en laat dan "
                  "telkens een ander stuk weg.", 4),
             ]),
        dict(kop="Op het ribosoom",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Wat brengt het juiste aminozuur bij het ribosoom?", "het tRNA", WW),
                 ("kort", "Hoe heet het drietal op het tRNA dat op het codon past?",
                  "het anticodon", WW),
                 ("kort", "Welk anticodon past op het codon G C A?", "C G U", W),
                 ("open", "Beschrijf in drie stappen wat er op het ribosoom gebeurt.",
                  "Het ribosoom bindt aan het mRNA bij het startcodon. Daarna komt bij elk codon "
                  "het passende tRNA met zijn aminozuur, en wordt dat aminozuur met een "
                  "peptidebinding aan de keten gehangen. Bij een stopcodon laat het ribosoom los "
                  "en komt de keten vrij.", 5),
                 ("waar", "Eén mRNA kan maar door één ribosoom tegelijk gelezen worden.", False),
             ]),
        dict(kop="Van keten naar werkend eiwit",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom werkt een polypeptideketen die net van het ribosoom komt, nog "
                          "niet altijd?",
                  "Ze moet zich eerst in haar juiste ruimtelijke vorm vouwen, en vaak worden er nog "
                  "stukken afgeknipt of groepen opgezet in het ER en het golgi-apparaat.", 4),
                 ("open", "Leg uit waarom de volgorde van de aminozuren de werking van een eiwit "
                          "bepaalt.",
                  "De volgorde bepaalt hoe de keten zich vouwt, en de vouw bepaalt op welk molecule "
                  "het eiwit past. Verandert de volgorde, dan verandert mogelijk de vouw en dus de "
                  "werking.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-genregulatie-epigenetica-en-nature-of-nurture-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Genregulatie, epigenetica en nature of nurture",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Waarom regelen?",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom zet een cel niet al haar genen tegelijk aan?",
                  "Een eiwit maken kost energie en grondstoffen. Een cel maakt dus alleen wat ze "
                  "op dat moment nodig heeft, en dat verschilt per celtype en per situatie.", 4),
                 ("open", "Een lever- en een spiercel hebben hetzelfde DNA. Waar zit het verschil "
                          "dan?",
                  "In welke genen bij elk van beide aan staan. Dat bepaalt welke eiwitten ze maken "
                  "en dus wat ze kunnen.", 4),
             ]),
        dict(kop="Het lac-operon",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het stuk DNA waaraan de repressor bindt", "de operator"),
                          ("het stuk waaraan RNA-polymerase bindt", "de promotor"),
                          ("het eiwit dat de operator kan blokkeren", "de repressor")], None, WW),
                 ("open", "Beschrijf wat er met het lac-operon gebeurt als er géén lactose in de "
                          "omgeving is.",
                  "De repressor zit op de operator. RNA-polymerase kan daar niet voorbij, dus "
                  "worden de genen voor de lactose-enzymen niet afgelezen.", 4),
                 ("open", "En wat gebeurt er zodra er lactose bijkomt?",
                  "De lactose bindt aan de repressor en verandert zijn vorm. De repressor laat de "
                  "operator los, RNA-polymerase kan door, en de enzymen worden gemaakt.", 4),
                 ("open", "Waarom is zo'n operon handig voor een bacterie?",
                  "Alle genen die voor één taak nodig zijn, staan er samen in en gaan dus samen aan "
                  "of uit, met één schakelaar.", 4),
             ]),
        dict(kop="Epigenetica",
             opdracht="Schrijf methylering of acetylering en zeg wat het doet.",
             oefeningen=[
                 ("rij", [("er komen methylgroepen op het DNA", "legt het gen stil"),
                          ("er komen acetylgroepen op de histonen", "maakt het gen leesbaar")],
                  "Gevolg", WL),
                 ("open", "Waarin verschilt een epigenetische verandering van een mutatie?",
                  "Een mutatie verandert de letters van het DNA zelf. Een epigenetische verandering "
                  "laat de letters staan en verandert alleen of ze gelezen kunnen worden.", 4),
                 ("open", "Een eeneiige tweeling heeft hetzelfde DNA, maar de ene krijgt op latere "
                          "leeftijd een ziekte en de andere niet. Hoe kan dat?",
                  "Ze hebben verschillend geleefd. Voeding, stress en omgeving zetten "
                  "epigenetische merktekens, zodat bij de ene andere genen aan of uit staan dan bij "
                  "de andere.", 5),
                 ("waar", "Epigenetische merktekens kunnen in sommige gevallen aan de volgende "
                          "generatie doorgegeven worden.", True),
             ]),
        dict(kop="Nature of nurture",
             opdracht="Schrijf vooral nature, vooral nurture of beide.",
             oefeningen=[
                 ("rij", [("je bloedgroep", "vooral nature"),
                          ("de taal die je spreekt", "vooral nurture"),
                          ("je lichaamsgewicht", "beide")], None, WW),
                 ("rij", [("je oogkleur", "vooral nature"),
                          ("je lichaamslengte", "beide"),
                          ("of je kan pianospelen", "vooral nurture")], None, WW),
                 ("open", "Waarom is tweelingonderzoek bij deze vraag nuttig?",
                  "Een eeneiige tweeling heeft hetzelfde DNA. Verschillen tussen de twee moeten dus "
                  "van de omgeving komen. En een tweeling die apart opgroeide, laat zien wat er "
                  "ondanks een andere omgeving toch gelijk blijft.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mutaties-mutagenen-en-kanker-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Mutaties, mutagenen en kanker",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke genmutatie?",
             opdracht="Schrijf substitutie, deletie, insertie of inversie.",
             oefeningen=[
                 ("rij", [("A A T G C C wordt A A T G A C", "substitutie"),
                          ("A A T G C C wordt A A T C C", "deletie"),
                          ("A A T G C C wordt A A T G T C C", "insertie")], None, WW),
                 ("rij", [("A A T G C C wordt A A C G T C", "inversie"),
                          ("A A T G C C wordt A A T G C C A", "insertie")], None, WW),
                 ("open", "Waarom is een deletie van één base meestal veel ernstiger dan een "
                          "substitutie?",
                  "Door een deletie schuift het hele leesraam op. Alle codons na die plaats worden "
                  "anders gelezen, dus klopt het hele verdere eiwit niet meer. Een substitutie "
                  "verandert hoogstens één aminozuur.", 5),
             ]),
        dict(kop="Wat is het gevolg?",
             opdracht="Schrijf stille mutatie, missense of nonsense.",
             oefeningen=[
                 ("rij", [("het codon wijzigt maar codeert hetzelfde aminozuur", "stille mutatie"),
                          ("er komt een ander aminozuur in de keten", "missense"),
                          ("er ontstaat vroegtijdig een stopcodon", "nonsense")], None, WW),
                 ("open", "Waarom kan een stille mutatie bestaan?",
                  "De genetische code is gedegenereerd: meerdere codons duiden hetzelfde aminozuur "
                  "aan. Verandert de derde letter vaak, dan blijft het aminozuur hetzelfde.", 4),
                 ("open", "Bij sikkelcelanemie is één aminozuur van de hemoglobineketen vervangen. "
                          "Waarom heeft dat zulke grote gevolgen?",
                  "Dat ene andere aminozuur verandert de vouw van het eiwit. De hemoglobine plakt "
                  "samen, de bloedcellen worden sikkelvormig en vervoeren minder zuurstof, en ze "
                  "blijven in de kleine bloedvaten steken.", 5),
             ]),
        dict(kop="Drie niveaus van mutatie",
             opdracht="Schrijf genmutatie, chromosoommutatie of genoommutatie.",
             oefeningen=[
                 ("rij", [("één base is vervangen", "genmutatie"),
                          ("een stuk van een chromosoom is omgekeerd", "chromosoommutatie"),
                          ("er is een chromosoom te veel", "genoommutatie")], None, WW),
                 ("rij", [("trisomie 21", "genoommutatie"),
                          ("een stuk van chromosoom 9 is aan chromosoom 22 geplakt",
                           "chromosoommutatie")], None, WW),
                 ("kort", "Hoe noemt men het verkeerd uiteengaan van de chromosomen bij de meiose?",
                  "non-disjunctie", WW),
             ]),
        dict(kop="Erfelijk of niet?",
             opdracht="Schrijf erfelijk of niet erfelijk, en zeg waarom.",
             oefeningen=[
                 ("rij", [("een mutatie in een huidcel door de zon", "niet erfelijk"),
                          ("een mutatie in een eicel", "erfelijk"),
                          ("een mutatie in een longcel door roken", "niet erfelijk")], None, WW),
                 ("open", "Leg uit waarom alleen een mutatie in een geslachtscel erfelijk is.",
                  "Alleen de geslachtscellen geven hun DNA aan de volgende generatie door. Een "
                  "lichaamscel geeft haar DNA enkel aan haar eigen dochtercellen, en die verdwijnen "
                  "met het individu.", 5),
             ]),
        dict(kop="Mutagenen en kanker",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men een factor die de kans op een mutatie verhoogt?",
                  "een mutageen", WW),
                 ("open", "Noem drie soorten mutagenen, met van elk een voorbeeld.",
                  "Straling, zoals uv-licht of röntgenstraling. Chemische stoffen, zoals de teer in "
                  "sigarettenrook. En sommige virussen, zoals HPV.", 4),
                 ("rij", [("een gen dat de celdeling aanzet en te actief geworden is", "oncogen"),
                          ("een gen dat de celdeling afremt en uitgevallen is",
                           "tumorsuppressorgen")], None, WL),
                 ("open", "Waarom is één mutatie meestal niet genoeg om kanker te krijgen?",
                  "Er zijn verschillende controles op de celdeling. Pas als er meerdere genen "
                  "misgaan, een oncogen te actief én een rem uitgevallen, gaat een cel ongeremd "
                  "delen.", 5),
                 ("kort", "Hoe noemt men het uitzaaien van kankercellen naar een ander orgaan?",
                  "metastase", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-dna-technologie-en-gentechnologie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="DNA-technologie en gentechnologie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het gereedschap",
             opdracht="Schrijf bij elke taak het gereedschap of de techniek.",
             oefeningen=[
                 ("rij", [("knipt DNA op een vaste plaats in de sequentie", "restrictie-enzym"),
                          ("plakt twee geknipte stukken definitief aan elkaar", "ligase"),
                          ("brengt DNA in een cel binnen", "een vector")], None, WW),
                 ("rij", [("vermenigvuldigt een stukje DNA miljoenen keren", "PCR"),
                          ("scheidt DNA-stukken naar grootte", "gelelektroforese"),
                          ("leest de volledige basenvolgorde uit", "sequencing")], None, WW),
                 ("kort", "Welke techniek past een gen op een gekozen plaats aan?", "CRISPR-Cas",
                  WW),
             ]),
        dict(kop="Natuurlijke genoverdracht bij bacteriën",
             opdracht="Schrijf transformatie, conjugatie of transductie.",
             oefeningen=[
                 ("rij", [("een bacterie neemt vrij DNA uit haar omgeving op", "transformatie"),
                          ("twee bacteriën wisselen DNA uit via een brug", "conjugatie"),
                          ("een virus brengt bacterieel DNA naar een andere bacterie",
                           "transductie")], None, WW),
                 ("open", "Waarom verspreidt antibioticumresistentie zich zo snel onder bacteriën?",
                  "Het gen zit vaak op een plasmide, en zo'n plasmide kan van de ene bacterie naar "
                  "de andere, soms zelfs naar een andere soort. Bacteriën delen zich daarbij heel "
                  "snel.", 5),
             ]),
        dict(kop="De drie stappen van een PCR",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Stap", "Wat er gebeurt"],
                  [["verhitten", None], ["afkoelen", None], ["verlengen", None]],
                  "Bij het verhitten komen de twee strengen van elkaar los. Bij het afkoelen "
                  "binden de primers op hun plaats. Bij het verlengen bouwt polymerase van elke "
                  "primer af een nieuwe streng.", WL),
                 ("open", "Na hoeveel cyclussen heb je uit één stuk DNA ongeveer duizend stukken? "
                          "Reken het uit.",
                  "Elke cyclus verdubbelt het aantal. Na tien cyclussen is dat 2 tot de tiende, "
                  "dus 1024 stukken.", 4),
             ]),
        dict(kop="Gelelektroforese",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Naar welke pool wandelt DNA in een gel, en waarom?",
                  "Naar de pluspool. De fosfaatgroepen maken DNA negatief geladen.", 3),
                 ("open", "Welke stukken komen het verst, en waarom?",
                  "De kleine stukken. Die schuiven gemakkelijker door de poriën van de gel dan de "
                  "grote.", 3),
                 ("open", "Waarom heeft iedereen een eigen DNA-fingerprint?",
                  "Op bepaalde plaatsen in het DNA staan korte stukjes die zich herhalen, en het "
                  "aantal herhalingen verschilt van persoon tot persoon. Dat geeft voor ieder een "
                  "eigen bandenpatroon.", 5),
             ]),
        dict(kop="Toepassingen en klonen",
             opdracht="Schrijf reproductief, moleculair of therapeutisch klonen.",
             oefeningen=[
                 ("rij", [("er wordt een volledig nieuw, genetisch gelijk individu gemaakt",
                           "reproductief"),
                          ("er wordt een stuk DNA in een gastheercel vermenigvuldigd",
                           "moleculair"),
                          ("er wordt weefsel gekweekt om een patiënt te behandelen",
                           "therapeutisch")], None, WW),
                 ("open", "Beschrijf in drie stappen hoe insuline met bacteriën gemaakt wordt.",
                  "Het menselijke insulinegen wordt met een restrictie-enzym uitgeknipt. Het wordt "
                  "met ligase in een plasmide gezet. Dat plasmide wordt in een bacterie gebracht, "
                  "en de bacterie maakt de insuline aan.", 5),
                 ("open", "Wat is het verschil tussen een cisgeen en een transgeen organisme?",
                  "Bij een cisgeen organisme komt het ingebrachte gen van een verwante soort die "
                  "ook natuurlijk kan kruisen. Bij een transgeen organisme komt het van een soort "
                  "over die grens heen.", 4),
                 ("open", "Noem één voordeel en één bezorgdheid bij een insectresistent gewas.",
                  "Een voordeel is dat er minder insecticide gesproeid moet worden. Een bezorgdheid "
                  "is dat de gevolgen op lange termijn voor andere insecten en voor de biodiversiteit "
                  "niet volledig gekend zijn.", 5),
                 ("waar", "Een kloon van een dier gedraagt zich precies hetzelfde als het origineel.",
                  False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-argumenten-voor-evolutie-en-de-evolutietheorieen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Argumenten voor evolutie en de evolutietheorieën",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk argument?",
             opdracht="Schrijf anatomie, embryologie, paleontologie, moleculaire biologie of "
                      "biogeografie.",
             oefeningen=[
                 ("rij", [("de voorpoot van een hond en de arm van een mens zijn gelijk gebouwd",
                           "anatomie"),
                          ("een vissen-, een kippen- en een mensenembryo hebben alle kieuwbogen",
                           "embryologie"),
                          ("in de oudste lagen liggen de eenvoudigste organismen",
                           "paleontologie")], None, WL),
                 ("rij", [("het hemoglobine van mens en chimpansee verschilt in weinig aminozuren",
                           "moleculaire biologie"),
                          ("Australië heeft buideldieren die elders niet voorkomen",
                           "biogeografie"),
                          ("alle organismen gebruiken dezelfde genetische code",
                           "moleculaire biologie")], None, WL),
             ]),
        dict(kop="Homoloog of analoog?",
             opdracht="Schrijf homoloog of analoog.",
             oefeningen=[
                 ("rij", [("de vleugel van een vleermuis en de arm van een mens", "homoloog"),
                          ("de vleugel van een insect en die van een vogel", "analoog"),
                          ("de vin van een haai en die van een dolfijn", "analoog")], None, W),
                 ("open", "Waarom wijst analogie niet op verwantschap?",
                  "Analoge organen hebben dezelfde functie maar een andere bouw en een andere "
                  "oorsprong. Ze zijn apart ontstaan omdat de omgeving bij beide groepen dezelfde "
                  "eisen stelde.", 5),
                 ("kort", "Hoe noemt men een orgaan dat bij een soort geen functie meer heeft?",
                  "een rudimentair orgaan", WL),
             ]),
        dict(kop="Fossielen lezen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom liggen de oudste fossielen het diepst?",
                  "Gesteentelagen stapelen zich van onder naar boven op. Wat later begraven werd, "
                  "ligt dus bovenop.", 3),
                 ("open", "Waarom is Archaeopteryx zo belangrijk?",
                  "Hij heeft kenmerken van twee groepen: veren zoals een vogel, en tanden en een "
                  "benige staart zoals een reptiel. Hij is dus een overgangsfossiel tussen "
                  "reptielen en vogels.", 5),
                 ("kort", "Hoe noemt men een reeks vondsten die een soort stap voor stap ziet "
                          "veranderen?",
                  "een continue reeks", WL),
             ]),
        dict(kop="Lamarck of Darwin?",
             opdracht="Schrijf Lamarck of Darwin.",
             oefeningen=[
                 ("rij", [("een giraf rekt haar nek en geeft die langere nek door", "Lamarck"),
                          ("giraffen met van nature een langere nek lieten meer nakomelingen na",
                           "Darwin"),
                          ("verworven eigenschappen zijn erfelijk", "Lamarck")], None, W),
                 ("open", "Waarom klopt de erfelijkheid van verworven eigenschappen niet?",
                  "Wat je tijdens je leven aan je lichaam verandert, zit niet in je geslachtscellen. "
                  "Alleen wat in het DNA van die cellen staat, gaat naar de volgende generatie.", 5),
                 ("open", "Noem de drie gedachten waarop de theorie van Darwin steunt.",
                  "Er is variatie tussen de individuen, er is selectie doordat niet allen even veel "
                  "nakomelingen krijgen, en die verschillen zijn erfelijk.", 4),
                 ("open", "Wat bedoelde Darwin met survival of the fittest?",
                  "Niet de sterkste, maar wie het best bij zijn omgeving past, krijgt meer "
                  "nakomelingen. Fit betekent hier passend.", 4),
             ]),
        dict(kop="De moderne evolutietheorie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men het aandeel van een allel in een populatie?",
                  "de allelfrequentie", WL),
                 ("open", "Noem de twee bronnen van genetische variatie in een populatie.",
                  "Mutaties, die nieuwe allelen maken, en de meiose met haar crossing-over en "
                  "mixing, die bestaande allelen telkens anders combineert.", 4),
                 ("open", "Een bacteriestam wordt resistent tegen een antibioticum. Leg uit hoe "
                          "dat gaat, en waar het antibioticum wel en niet voor zorgt.",
                  "Door toevallige mutaties waren enkele bacteriën al resistent. Het antibioticum "
                  "doodt de andere, zodat alleen die enkele zich voortplanten. Het antibioticum "
                  "selecteert dus, het maakt de bacteriën niet resistent.", 6),
                 ("waar", "Een individu kan tijdens zijn leven evolueren.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-selectie-soortvorming-en-de-menswording-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Selectie, soortvorming en de menswording",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk mechanisme?",
             opdracht="Schrijf natuurlijke selectie, seksuele selectie, genetische drift, gene flow "
                      "of kunstmatige selectie.",
             oefeningen=[
                 ("rij", [("na een storm blijven er nog vijf hagedissen op een eiland over",
                           "genetische drift"),
                          ("een boer kiest zelf de koeien die mogen kalven",
                           "kunstmatige selectie"),
                          ("pauwinnen kiezen de haan met de grootste staart",
                           "seksuele selectie")], None, WL),
                 ("rij", [("er trekken elk jaar vogels van de ene populatie naar de andere",
                           "gene flow"),
                          ("op roetzwarte bomen worden lichte vlinders meer opgegeten",
                           "natuurlijke selectie")], None, WL),
                 ("kort", "Hoe noemt men het geval waarin een klein groepje elders een nieuwe "
                          "populatie sticht?",
                  "het stichterseffect", WL),
             ]),
        dict(kop="Begrippen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Wat betekent fitness in de evolutieleer, en wat betekent het niet?",
                  "Het betekent hoeveel nakomelingen een individu nalaat die zelf weer "
                  "nakomelingen krijgen. Het betekent niet hoe sterk of gespierd het is.", 4),
                 ("open", "Waarom speelt genetische drift sterker in een kleine populatie?",
                  "In een kleine groep weegt één toevallige gebeurtenis veel zwaarder door in de "
                  "verhoudingen. In een grote groep vallen die toevalligheden tegen elkaar weg.",
                  4),
                 ("open", "Waarom verdwijnt een nadelig recessief allel zelden volledig uit een "
                          "grote populatie?",
                  "Heterozygote dragers tonen het niet, dus wordt er ook niet op hen geselecteerd. "
                  "Ze geven het allel ongemerkt door.", 4),
                 ("waar", "Genetische drift bevoordeelt de best aangepaste individuen.", False),
             ]),
        dict(kop="Welke isolatie?",
             opdracht="Schrijf geografisch, ecologisch, temporeel, ethologisch, gametisch of "
                      "postzygotisch.",
             oefeningen=[
                 ("rij", [("twee populaties zijn door een gebergte gescheiden", "geografisch"),
                          ("twee kikkersoorten in hetzelfde moeras kwaken verschillend",
                           "ethologisch"),
                          ("twee plantensoorten bloeien in een ander deel van het jaar",
                           "temporeel")], None, WW),
                 ("rij", [("twee soorten wonen in hetzelfde bos, de ene in de kruin en de andere "
                           "op de grond", "ecologisch"),
                          ("de zaadcel kan de eicel van de andere soort niet bevruchten",
                           "gametisch"),
                          ("een muildier is onvruchtbaar", "postzygotisch")], None, WW),
                 ("open", "Wat is het verschil tussen prezygotische en postzygotische isolatie?",
                  "Prezygotische isolatie verhindert dat er een bevruchting komt. Postzygotische "
                  "isolatie laat de bevruchting toe, maar de nakomeling leeft niet of is "
                  "onvruchtbaar.", 5),
                 ("open", "Wat is het verschil tussen allopatrische en sympatrische soortvorming?",
                  "Bij allopatrische soortvorming raken de twee groepen ruimtelijk gescheiden. Bij "
                  "sympatrische soortvorming blijven ze in hetzelfde gebied en scheiden ze zich "
                  "door een verschil in gedrag, leefplek of bloeitijd.", 5),
             ]),
        dict(kop="Wanneer is het één soort?",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Wanneer horen twee dieren tot dezelfde soort?",
                  "Als ze zich onderling kunnen voortplanten en daarbij vruchtbare nakomelingen "
                  "krijgen.", 3),
                 ("open", "Een paard en een ezel krijgen samen een muildier. Waarom zijn ze toch "
                          "twee soorten?",
                  "Het muildier is zelf onvruchtbaar. Er is dus geen voortplanting tussen de twee "
                  "groepen op lange termijn.", 4),
                 ("open", "Noem de drie dingen die nodig zijn voor soortvorming.",
                  "Variatie binnen de groep, isolatie tussen de twee groepen, en genoeg tijd.", 3),
             ]),
        dict(kop="De menswording",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men de hele groep mensachtigen, de uitgestorven soorten erbij?",
                  "de hominiden", WW),
                 ("open", "Welke verandering wordt als de eerste grote stap in de menswording "
                          "gezien, en welke drie lichamelijke aanpassingen horen erbij?",
                  "Het rechtop gaan lopen. Daarbij horen een S-vormige wervelkolom, een breder en "
                  "schuiner bekken, en een voetboog.", 5),
                 ("open", "Een groter hersenvolume gaf voordelen, maar kostte ook iets. Noem twee "
                          "kosten.",
                  "De hersenen verbruiken veel energie, en een groter hoofd maakt de bevalling "
                  "moeilijker en gevaarlijker.", 4),
                 ("waar", "De mens stamt rechtstreeks af van de chimpansee.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biomoleculen-sachariden-lipiden-en-proteinen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Biomoleculen: sachariden, lipiden en proteïnen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke groep?",
             opdracht="Schrijf sacharide, lipide of proteïne.",
             oefeningen=[
                 ("rij", [("glycogeen", "sacharide"), ("cholesterol", "lipide"),
                          ("keratine", "proteïne")], None, W),
                 ("rij", [("cellulose", "sacharide"), ("een triglyceride", "lipide"),
                          ("aquaporine", "proteïne")], None, W),
                 ("rij", [("amylose", "sacharide"), ("een fosfolipide", "lipide"),
                          ("collageen", "proteïne")], None, W),
             ]),
        dict(kop="Bouwsteen en bouwwerk",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Groep", "Bouwstenen", "Een voorbeeld van het grote molecule"],
                  [["sachariden", None, None], ["lipiden", None, None], ["proteïnen", None, None]],
                  "Sachariden zijn opgebouwd uit monosachariden zoals glucose; zetmeel is zo'n "
                  "groot molecule. Een triglyceride bestaat uit glycerol en drie vetzuren. "
                  "Proteïnen zijn opgebouwd uit aminozuren; hemoglobine is zo'n groot molecule.",
                  WL),
                 ("kort", "Hoe heet de reactie die twee bouwstenen verbindt en water afgeeft?",
                  "een condensatiereactie", WL),
                 ("kort", "Hoe heet de reactie die een molecule met water weer splitst?",
                  "hydrolyse", WW),
             ]),
        dict(kop="Sachariden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("glucose en galactose samen", "lactose"),
                          ("glucose en fructose samen", "sacharose"),
                          ("de binding tussen twee suikerringen", "glycosidebinding")], None, WW),
                 ("open", "Waarom is cellulose geschikt als bouwstof van een celwand, en zetmeel "
                          "niet?",
                  "De rechte ketens van cellulose liggen naast elkaar en vormen zo sterke vezels. "
                  "Zetmeel is opgerold en los, geschikt om op te slaan maar niet om te bouwen.", 5),
                 ("open", "Waarom kan een mens cellulose niet verteren, en een koe wel?",
                  "De mens heeft het enzym voor die binding niet. In de maag van een koe leven "
                  "micro-organismen die het wel hebben.", 4),
                 ("waar", "Zetmeel bestaat uit amylose en amylopectine.", True),
             ]),
        dict(kop="Lipiden",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom is olie bij kamertemperatuur vloeibaar en boter vast?",
                  "Olie heeft veel onverzadigde vetzuren met een dubbele binding en dus een knik in "
                  "de staart. Geknikte staarten kunnen minder dicht tegen elkaar liggen, dus blijft "
                  "het geheel vloeibaar.", 5),
                 ("open", "Waarom is een fosfolipide geschikt om een membraan te vormen?",
                  "Het heeft een waterminnende kop en twee waterafstotende staarten. In water gaan "
                  "de koppen naar buiten en de staarten naar binnen, en zo vormt zich vanzelf een "
                  "dubbellaag.", 5),
                 ("open", "Noem drie functies van lipiden in het lichaam.",
                  "Energievoorraad, warmte-isolatie, en bouwstof van de celmembranen. Ze zijn ook "
                  "grondstof voor hormonen.", 3),
                 ("open", "Waarom levert vet per gram meer energie dan suiker?",
                  "Vet is sterker gereduceerd: er zit per koolstofatoom meer waterstof in, en juist "
                  "die waterstof levert bij de oxidatie de energie.", 4),
             ]),
        dict(kop="Proteïnen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de volgorde van de aminozuren", "primaire structuur"),
                          ("de alfahelix en de bètaplaat", "secundaire structuur"),
                          ("de ruimtelijke vouw van één keten", "tertiaire structuur")], None, WL),
                 ("kort", "Hoe noemt men de structuur van een eiwit uit meerdere ketens?",
                  "de quaternaire structuur", WL),
                 ("kort", "Hoe heet de binding tussen twee aminozuren?", "de peptidebinding", WW),
                 ("open", "Welke twee groepen heeft elk aminozuur gemeenschappelijk, en wat "
                          "verschilt?",
                  "Elk aminozuur heeft een aminogroep en een carboxylgroep. Wat verschilt is de "
                  "restgroep of zijketen.", 4),
                 ("open", "Waarom werkt een gedenatureerd enzym niet meer?",
                  "Zijn ruimtelijke vouw is uiteengevallen, dus zijn actieve plaats past niet meer "
                  "op het substraat.", 4),
                 ("open", "Leg uit waarom één veranderd aminozuur een heel eiwit kan bederven.",
                  "De volgorde bepaalt hoe de keten zich vouwt. Eén ander aminozuur kan die vouw "
                  "veranderen, en met de vouw verandert wat het eiwit kan.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-en-duurzaam-werken-in-het-labo-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig en duurzaam werken in het labo",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat betekent dit pictogram?",
             opdracht="Schrijf waarvoor het pictogram waarschuwt.",
             oefeningen=[
                 ("rij", [("een vlam", "brandbaar"), ("een doodshoofd", "giftig"),
                          ("een hand en een oppervlak waarop een vloeistof inwerkt", "bijtend")],
                  None, WW),
                 ("rij", [("een uitroepteken", "schadelijk of irriterend"),
                          ("een dode boom en een dode vis", "gevaarlijk voor het milieu"),
                          ("een vlam boven een cirkel", "oxiderend")], None, WL),
                 ("waar", "Een product zonder gevarenpictogram is altijd volkomen veilig.", False),
             ]),
        dict(kop="Meten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men de kleinste en de grootste waarde die een instrument kan "
                          "meten?",
                  "het meetbereik", WW),
                 ("kort", "Hoe noemt men de kleinste waarde die je met een instrument nog kan "
                          "onderscheiden?",
                  "de resolutie", WW),
                 ("open", "Je moet 2 ml water afmeten en je hebt een maatbeker van 500 ml en een "
                          "maatcilinder van 10 ml. Welke kies je, en waarom?",
                  "De maatcilinder van 10 ml. Die heeft een fijnere verdeling, dus kan je er veel "
                  "nauwkeuriger 2 ml mee afmeten.", 4),
                 ("open", "Noem drie dingen die je bij elke meting doet.",
                  "Recht van voren aflezen, de eenheid erbij noteren, en de meting meerdere keren "
                  "herhalen.", 3),
             ]),
        dict(kop="Goed of fout?",
             opdracht="Schrijf goed of fout, en zeg kort waarom.",
             oefeningen=[
                 ("rij", [("een warme kolf meteen op een koude stenen tafel zetten", "fout"),
                          ("een balans op nul zetten voor je weegt", "goed"),
                          ("met de mond pipetteren om sneller te werken", "fout")], None, W),
                 ("rij", [("een microscoop aan arm en voet dragen", "goed"),
                          ("bij de grootste vergroting met de grove stelschroef scherpstellen",
                           "fout"),
                          ("een elektrisch toestel met natte handen aanzetten", "fout")], None, W),
                 ("open", "Waarom start je het bekijken van een preparaat met het kleinste "
                          "objectief?",
                  "Je ziet dan een groter stuk van het preparaat en vindt je beeld dus veel "
                  "gemakkelijker terug. Daarna schakel je over op een grotere vergroting.", 4),
                 ("open", "Waarom stel je bij de grootste vergroting alleen met de fijne "
                          "stelschroef scherp?",
                  "Het objectief staat dan heel dicht bij het glaasje. Met de grove schroef duw je "
                  "het in het preparaat en breek je het dekglaasje of de lens.", 5),
             ]),
        dict(kop="Wat doe je?",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Er breekt glaswerk op je tafel. Wat doe je, in drie stappen?",
                  "Je verwittigt de leraar, je raakt de scherven niet met je handen aan, en je "
                  "ruimt ze op met borstel en blik in de bak voor scherf.", 4),
                 ("open", "Er spat een bijtend product in je oog. Wat doe je als eerste?",
                  "Je spoelt onmiddellijk lang met veel water aan de oogdouche, en je verwittigt de "
                  "leraar.", 3),
                 ("open", "Je hebt te veel van een product afgemeten. Wat doe je met de rest, en "
                          "waarom niet terug in de fles?",
                  "De rest gaat naar het juiste afval. Terug in de voorraadfles zou de hele fles "
                  "kunnen besmetten.", 4),
                 ("open", "Waarom eet of drink je niet in een labo?",
                  "Je kan onbedoeld een product of een micro-organisme binnenkrijgen, bijvoorbeeld "
                  "via je handen of een spat op je boterham.", 4),
             ]),
        dict(kop="Afval en duurzaamheid",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men het volledig kiemvrij maken van materiaal met stoom onder "
                          "druk?",
                  "steriliseren", WW),
                 ("kort", "In welk toestel gebeurt dat?", "in een autoclaaf", WW),
                 ("open", "Waarom giet je chemisch afval niet in de gootsteen?",
                  "Het komt dan in het oppervlaktewater terecht en belast daar het milieu. "
                  "Sommige stoffen tasten ook de buizen aan.", 4),
                 ("open", "Noem drie manieren om in een labo duurzamer te werken.",
                  "Niet meer afmeten dan je nodig hebt, toestellen uitzetten als je ze niet "
                  "gebruikt, en afval gescheiden houden. Materiaal hergebruiken waar het kan, "
                  "hoort er ook bij.", 3),
                 ("open", "Leg uit waarom duurzaam werken ook veiliger werken is.",
                  "Minder product en minder afval betekent minder stoffen die kunnen morsen, "
                  "ontsnappen of verkeerd terechtkomen. Dat is tegelijk veiliger voor jezelf en "
                  "voor de omgeving.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De stappen op een rij",
             opdracht="Nummer van 1 tot 6 in de juiste volgorde.",
             oefeningen=[
                 ("rij", [("de onderzoeksvraag stellen", "1"),
                          ("een hypothese opschrijven", "2"),
                          ("een onderzoeksplan maken", "3")], "Nummer", "70px"),
                 ("rij", [("de proef uitvoeren en meten", "4"),
                          ("de resultaten verwerken in een tabel of grafiek", "5"),
                          ("een besluit formuleren", "6")], "Nummer", "70px"),
             ]),
        dict(kop="Welke variabele?",
             opdracht="Je onderzoekt of zaden sneller ontkiemen bij een hogere temperatuur. Schrijf "
                      "onafhankelijk, afhankelijk of constant.",
             oefeningen=[
                 ("rij", [("de temperatuur van de kast", "onafhankelijk"),
                          ("het aantal dagen tot het ontkiemen", "afhankelijk"),
                          ("de hoeveelheid water per bakje", "constant")], None, WW),
                 ("rij", [("de soort zaden", "constant"),
                          ("het aantal zaden per bakje", "constant"),
                          ("het percentage ontkiemde zaden", "afhankelijk")], None, WW),
                 ("kort", "Hoe noemt men de reeks zonder de onderzochte factor?",
                  "de controlegroep", WW),
             ]),
        dict(kop="Wat is er fout aan deze opstelling?",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Een leerling test een meststof op tien planten in de zon en op tien "
                          "planten zonder meststof in de schaduw.",
                  "Er verschillen twee factoren tegelijk: de meststof en het licht. Zie je een "
                  "verschil, dan weet je niet waaraan het ligt. Beide reeksen moeten op dezelfde "
                  "plaats staan.", 5),
                 ("open", "Een leerling meet één zaadje, ziet dat het na drie dagen ontkiemt en "
                          "besluit dat alle zaden drie dagen nodig hebben.",
                  "Eén meting is veel te weinig. Met een groter aantal zaden weegt een "
                  "uitzondering minder zwaar door en kan je een gemiddelde berekenen.", 5),
                 ("open", "Een leerling laat een meting die niet in zijn verwachting past, weg uit "
                          "zijn verslag.",
                  "Dat mag niet. Een afwijkende meting noteer je en je schrijft erbij wat je "
                  "ervan denkt. Weglaten wat niet past, maakt het resultaat onbetrouwbaar.", 5),
             ]),
        dict(kop="Grafieken",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Wat zet je op de horizontale as?", "wat je zelf veranderd hebt", WL),
                 ("open", "Noem de drie dingen die bij elke as horen.",
                  "De naam van de grootheid, de eenheid, en een regelmatige verdeling met "
                  "getallen.", 3),
                 ("kies", "Welk soort grafiek past bij een groei die je in de tijd volgt?",
                  ["een cirkeldiagram", "een lijngrafiek", "een staafdiagram zonder as"], 1),
                 ("open", "Waarom mag je een as niet bij een willekeurige waarde laten beginnen?",
                  "Dan lijken kleine verschillen veel groter dan ze zijn, en vertekent de grafiek "
                  "het beeld.", 4),
             ]),
        dict(kop="Besluiten en verbanden",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Twee reeksen hebben hetzelfde gemiddelde, maar in de ene liggen de "
                          "metingen veel verder uit elkaar. Wat besluit je?",
                  "Die reeks heeft meer spreiding en is dus minder betrouwbaar. Het gemiddelde "
                  "alleen zegt te weinig.", 4),
                 ("open", "Een grafiek toont dat er meer ijsjes verkocht worden in de weken waarin "
                          "meer mensen verdrinken. Wat besluit je?",
                  "Niet dat het ene het andere veroorzaakt. Er is een derde factor die beide "
                  "verklaart, namelijk warm weer.", 4),
                 ("open", "Noem de drie dingen die in een besluit horen.",
                  "Een antwoord op de onderzoeksvraag, of de hypothese bevestigd of weerlegd is, "
                  "en waarop je dat baseert.", 3),
                 ("waar", "Een weerlegde hypothese betekent dat je proef mislukt is.", False),
             ]),
        dict(kop="Ontwerpen en STEM",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Waarmee begint het ontwerpen van een oplossing?",
                  "met de eisen of criteria", WL),
                 ("kort", "Hoe noemt men een eerste werkend model dat je bouwt en test?",
                  "een prototype", WW),
                 ("kort", "Waarvoor staan de letters STEM?",
                  "wetenschappen, techniek, engineering en wiskunde", WL),
                 ("open", "Waarin verschilt ontwerpen van onderzoeken?",
                  "Onderzoeken wil een vraag beantwoorden en kennis opleveren. Ontwerpen wil een "
                  "probleem oplossen en levert iets dat werkt.", 4),
                 ("open", "Een school wil het waterverbruik van haar serre verlagen. Wat is een "
                          "goede eerste stap, en waarom?",
                  "Eerst meten hoeveel water er nu verbruikt wordt en waaraan. Zonder die cijfers "
                  "weet je niet waar de winst te halen is, en kan je achteraf niet nagaan of je "
                  "oplossing werkt.", 5),
                 ("open", "Je prototype voldoet niet aan één van je eisen. Wat doe je?",
                  "Je past het ontwerp aan en je test opnieuw, en daarna leg je het weer naast al "
                  "je eisen.", 4),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-de-cel-de-organellen-en-de-biologische-membranen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Elk organel heeft één kerntaak, en die taak zit meestal in de omschrijving "
                   "verstopt. Zie je het woord eiwit, denk aan ribosoom of golgi; zie je afbreken, "
                   "denk aan lysosoom; zie je energie, denk aan mitochondrion.",
            waarom=[
                "Zet de drie op een rij als een fabriek: het ribosoom maakt het eiwit, het golgi "
                "werkt het af en verpakt het, het lysosoom ruimt op. Zo zijn ze makkelijker uit "
                "elkaar te houden dan los uit het hoofd.",
                "Let op het kernlichaampje: het zit in de kern en maakt de ribosomen, dus het "
                "maakt zelf geen eiwit. Dat verschil wordt graag gevraagd.",
            ],
        ),
        dict(
            aanpak="Eén onderscheid beslist alles: een prokaryoot heeft geen echte kern en geen "
                   "membraanorganellen, een eukaryoot wel. Wat beide nodig hebben om te leven "
                   "(DNA, ribosomen, een celmembraan) is dus altijd beide.",
            waarom=[
                "Ribosomen zijn het antwoord beide, en dat is geen uitzondering: elke cel moet "
                "eiwitten maken, en een ribosoom heeft geen membraan nodig.",
                "Plasmiden zijn kleine losse ringen DNA naast het hoofd-DNA. Bacteriën wisselen ze "
                "onderling uit, en net daardoor kan resistentie tegen antibiotica zich zo snel "
                "verspreiden.",
            ],
        ),
        dict(
            aanpak="Een plantencel heeft drie dingen extra: de chloroplast, de celwand van "
                   "cellulose en de grote vacuole. Een dierlijke cel heeft het centrosoom. Al de "
                   "rest hebben ze samen.",
            waarom=[
                "Die drie horen bij elkaar in één verhaal: de chloroplast maakt het voedsel, de "
                "vacuole houdt het water vast en de celwand vangt de druk op die dat water geeft. "
                "Zo blijft een plant rechtstaan zonder skelet.",
                None,
            ],
        ),
        dict(
            aanpak="Een membraan is een dubbellaag fosfolipiden met eiwitten erin. Onthoud de "
                   "rolverdeling: de fosfolipiden maken de laag, cholesterol regelt de soepelheid, "
                   "en de glycoproteïnen zorgen voor de herkenning.",
            waarom=[
                "Dat de glycoproteïnen voor herkenning dienen, is geen detail: op die suikerketens "
                "staan onder meer de bloedgroepen, en daarop ziet je afweersysteem wat lichaamseigen "
                "is.",
                "Noem de twee woorden die het verklaren: hydrofiel en hydrofoob. Daarom vormt zo'n "
                "laag zich ook spontaan in water, zonder dat er iets aan vastgehouden moet worden.",
                "Niet waar, en dit is het vloeibaar-mozaïekmodel. De fosfolipiden en de eiwitten "
                "schuiven voortdurend langs elkaar, en net daardoor kan een membraan dichtgroeien "
                "na een scheurtje en kunnen cellen van vorm veranderen.",
            ],
        ),
        dict(
            aanpak="De endosymbiosetheorie zegt dat een mitochondrion ooit een vrijlevende "
                   "bacterie was die werd opgenomen. Elk argument is dus iets wat het organel nog "
                   "met een bacterie gemeen heeft: eigen DNA, eigen ribosomen, een eigen deling.",
            waarom=[
                "Noem er drie en let erop dat ze alle drie in dezelfde richting wijzen: dit "
                "organel gedraagt zich als een zelfstandig organisme. Het dubbele membraan is het "
                "spoor van het opslokken zelf, want de buitenste laag is van de opnemende cel.",
                "De chloroplast heeft dezelfde kenmerken, en in dat geval was de opgenomen "
                "bacterie een cyanobacterie. Alle zuurstof in onze lucht komt daar uiteindelijk "
                "van.",
            ],
        ),
        dict(
            aanpak="Wat buiten het membraan ligt, verschilt per groep: plant cellulose, schimmel "
                   "chitine, bacterie een eigen celwand. En de slotvraag gaat over oppervlak "
                   "tegenover volume, het terugkerende idee van dit hoofdstuk.",
            waarom=[
                None,
                "Chitine is dezelfde stof als in het schild van een insect. Dat een schimmel die "
                "stof gebruikt en geen cellulose, is een van de redenen dat schimmels bij de "
                "dieren horen en niet bij de planten.",
                "Microvilli zijn het antwoord, en het is dezelfde truc als bij een wortelhaar of "
                "een longblaasje: meer oppervlak op dezelfde plaats. Een flagel en een pseudopode "
                "dienen om te bewegen, een plasmodesma om twee plantencellen te verbinden.",
                "Dit is de kernvraag van de hele bundel. Noem het verband: het volume groeit met "
                "de derde macht en het oppervlak maar met de tweede, dus zakt de verhouding en "
                "raakt de uitwisseling te traag. Daarom bestaat een olifant uit meer cellen en "
                "niet uit grotere.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-celdifferentiatie-weefsels-en-celtypes-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Differentiatie betekent specialiseren. De sleutel is dat elke cel hetzelfde "
                   "DNA heeft maar niet dezelfde genen gebruikt. Hoe meer een cel gespecialiseerd "
                   "is, hoe minder ze nog iets anders kan worden.",
            waarom=[
                None,
                "Dit is het hart van het hoofdstuk. Noem de keten: welke genen aan staan bepaalt "
                "welke eiwitten er gemaakt worden, en de eiwitten bepalen wat een cel kan. "
                "Hetzelfde kookboek, een andere bladzijde.",
                "Een stamcel is dus het omgekeerde van een gedifferentieerde cel: ze heeft nog "
                "keuzes open. Daarom staat dit woord ook in de laatste reeks terug.",
            ],
        ),
        dict(
            aanpak="Hang elk plantenweefsel aan zijn taak. Xyleem en floëem zijn de twee "
                   "transportbanen, het meristeem is de groeiplaats, de epidermis de buitenkant "
                   "en het palissadeparenchym de fotosyntheselaag van het blad.",
            waarom=[
                "Houd de twee transportweefsels uit elkaar aan de richting: xyleem brengt water "
                "van de wortel naar boven, floëem brengt suiker van het blad naar waar ze nodig "
                "is, dus in beide richtingen.",
                "Dat het palissadeparenchym rechtop onder de bovenkant staat, is geen toeval: zo "
                "vangen die cellen het meeste licht en zitten ze vol chloroplasten.",
                "Dit is hetzelfde idee als bij de microvilli van een darmcel: een lange dunne vorm "
                "geeft veel oppervlak voor weinig volume. Vorm volgt functie, en dat komt in deze "
                "bundel nog twee keer terug.",
            ],
        ),
        dict(
            aanpak="Vier dierlijke weefsels, elk met een eigen werkwoord: epitheel bedekt, spier "
                   "beweegt, zenuw geleidt, bindweefsel verbindt en steunt. Zet in de tabel "
                   "telkens een plaats én dat werkwoord.",
            waarom=[
                "Merk op dat bindweefsel het breedste van de vier is: ook bot, pezen en vet horen "
                "erbij. Daarom is het ook het weefsel dat in bijna elk orgaan meezit.",
            ],
        ),
        dict(
            aanpak="Bij elke bijzondere cel hoort dezelfde vraag: welke vorm heeft ze, en wat "
                   "levert die vorm op? Zeg bij een voordeel ook altijd wat het kost, want net "
                   "die afweging wordt gevraagd.",
            waarom=[
                "Noem beide kanten, want de vraag vraagt er twee. Zonder kern geen deling en geen "
                "herstel, en dat is precies waarom je elke seconde miljoenen nieuwe rode "
                "bloedcellen moet aanmaken.",
                "23 is de helft van 46, en dat moet ook: bij de bevruchting komen twee gameten "
                "samen tot een cel met 46 chromosomen.",
                "Vorm volgt functie, nu voor een zenuwcel: één lange uitloper geeft minder "
                "vertraging dan een rij cellen die elkaar moeten doorgeven. De langste cel in je "
                "lichaam loopt van je onderrug tot je grote teen.",
                "Niet waar, en dat is net het verschil met een stamcel. Een gedifferentieerde cel "
                "heeft haar keuze gemaakt; enkel in het labo kan men haar met veel kunstgrepen "
                "terugzetten.",
            ],
        ),
        dict(
            aanpak="De organisatieniveaus gaan van klein naar groot: cel, weefsel, orgaan, "
                   "orgaanstelsel, organisme. Elk niveau is een groep van het vorige, en dat is "
                   "ook het antwoord op de laatste vraag.",
            waarom=[
                None,
                None,
                "Noem het verschil met het woord verschillende erin: een weefsel is één soort "
                "cellen, een orgaan bundelt meerdere weefsels. De darm is daarvoor het beste "
                "voorbeeld, want je kan er vier weefsels in aanwijzen.",
            ],
        ),
        dict(
            aanpak="Twee soorten stamcellen, en het verschil zit in hoeveel ze nog kunnen worden. "
                   "Embryonaal is alles, adult een beperkte groep. Daaruit volgt meteen waarom "
                   "ze medisch interessant zijn.",
            waarom=[
                "Zet het verschil in één woord: hoeveel keuzes blijven er open. Een adulte "
                "stamcel in het beenmerg maakt bloedcellen en geen zenuwcellen.",
                "Noem een echt voorbeeld, want dat maakt het antwoord sterk: een "
                "beenmergtransplantatie bij leukemie is stamceltherapie die al tientallen jaren "
                "bestaat.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-enzymen-transport-door-membranen-en-osmose-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een enzym is een eiwit dat een reactie versnelt zonder zelf op te geraken. "
                   "Drie woorden horen bij elkaar: het substraat is de stof, de actieve plaats is "
                   "de holte waar ze in past, en de activeringsenergie is de drempel die het enzym "
                   "verlaagt.",
            waarom=[
                "Let erop dat een enzym de reactie niet mogelijk maakt maar enkel versnelt: de "
                "drempel wordt lager, het eindresultaat blijft hetzelfde.",
                None,
                None,
                "Noem het woord substraatspecificiteit, want daar vraagt de oefening naar. Het "
                "beeld van een slot en een sleutel helpt: enkel de juiste vorm past, en daarom "
                "heeft je lichaam duizenden verschillende enzymen nodig.",
            ],
        ),
        dict(
            aanpak="Vier knoppen bepalen de snelheid: de temperatuur, de pH, de hoeveelheid "
                   "substraat en de hoeveelheid enzym. Bij temperatuur en pH is er een optimum, "
                   "dus te veel is even slecht als te weinig. Bij de hoeveelheden geldt: bijzetten "
                   "helpt zolang het andere niet beperkend is.",
            waarom=[
                "Let op het verschil tussen a en b. Van 20 naar 37 graden gaat het sneller, want "
                "je gaat naar het optimum toe; van 37 naar 70 gaat het trager, want het enzym valt "
                "uiteen. Dezelfde ingreep, twee uitkomsten.",
                "Een competitieve remmer gaat zelf op de actieve plaats zitten en houdt het "
                "substraat buiten. Veel geneesmiddelen en gifstoffen werken precies zo.",
                "Noem het woord denatureren en zeg erbij dat het onomkeerbaar is. Vergelijk het "
                "met een gebakken ei: afkoelen maakt het niet opnieuw vloeibaar.",
            ],
        ),
        dict(
            aanpak="Vier soorten transport, en twee vragen beslissen alles. Gaat het mee met de "
                   "gradiënt of tegen? Is er een eiwit nodig? Mee zonder eiwit is diffusie, mee "
                   "met een eiwit gefaciliteerde diffusie, tegen de gradiënt in met ATP actief "
                   "transport, en gaat het over water, dan heet het osmose.",
            waarom=[
                "Merk op dat enkel kleine en vetachtige stoffen zomaar door het membraan kunnen. "
                "Glucose is te groot en te waterminnend, dus heeft ze een kanaal nodig, ook al "
                "gaat ze de gemakkelijke kant op.",
                "Jodium in de schildklier is het mooiste voorbeeld van actief transport: de "
                "concentratie binnen is tientallen keren hoger dan buiten, en dat kan enkel met "
                "een pomp die energie verbruikt.",
                "Niet waar, en dat is net de betekenis van passief: het gaat van hoog naar laag en "
                "kost de cel niets. Enkel transport tegen de gradiënt in vraagt ATP.",
            ],
        ),
        dict(
            aanpak="Bij osmose gaat het water altijd naar de kant met het meeste opgeloste stof. "
                   "Bepaal dus eerst waar dat is, en kijk dan of er een celwand is: zonder "
                   "celwand barst de cel, met celwand wordt ze stevig.",
            waarom=[
                "Houd de drie woorden bij elkaar: hypertoon is meer opgeloste stof buiten, "
                "hypotoon minder, isotoon gelijk. Daarom wordt een patiënt met een isotone "
                "oplossing ingespoten en nooit met zuiver water.",
                "Noem de naam, want die wordt gevraagd: lyse, en bij een rode bloedcel "
                "hemolyse. Het water gaat naar binnen omdat binnen de concentratie hoger is.",
                "Plasmolyse is het spiegelbeeld: het water gaat naar buiten en het membraan trekt "
                "zich van de wand los. Dat is ook wat er gebeurt als je een plant bemest met te "
                "veel kunstmest, of als strooizout in de bodem komt.",
                "Dit is de kernvraag van de reeks. Noem de celwand en het woord turgescent: de "
                "wand vangt de druk op, en juist die druk houdt een plant rechtop. Daarom gaat een "
                "plant zonder water slap hangen.",
            ],
        ),
        dict(
            aanpak="Wat te groot is voor een kanaal, gaat in een blaasje. Naar binnen is "
                   "endocytose, naar buiten exocytose. Fagocytose en pinocytose zijn twee soorten "
                   "endocytose: vast tegenover vloeibaar.",
            waarom=[
                "Onthoud de woorddelen: fago betekent eten en pino drinken. Zo zijn de twee "
                "soorten endocytose niet meer te verwarren.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-fotosynthese-celademhaling-en-gisting-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De twee vergelijkingen zijn elkaars omkering. Leer er één goed en draai ze "
                   "om voor de andere: zes keer koolstofdioxide en water aan de ene kant, glucose "
                   "en zes keer zuurstof aan de andere.",
            waarom=[
                "Controleer je vergelijking altijd op het aantal atomen: zes koolstof links, zes "
                "in de glucose rechts. Dat is de snelste manier om te zien of je de coëfficiënten "
                "juist hebt.",
                None,
                "Noem het woord kringloop: de producten van de ene zijn de grondstoffen van de "
                "andere. Dat is ook de reden dat beide processen samen de koolstofkringloop van de "
                "hele aarde dragen.",
            ],
        ),
        dict(
            aanpak="Elke stap heeft een vaste plaats, en de ordening volgt het membraan. Wat met "
                   "licht of met een elektronentransport te maken heeft, gebeurt op een membraan; "
                   "de cycli gebeuren in de vloeistof erbinnen; de glycolyse gebeurt buiten de "
                   "organellen, in het cytoplasma.",
            waarom=[
                "Dat de lichtreacties op het thylakoïdmembraan gebeuren en de Calvincyclus in het "
                "stroma, is niet willekeurig: de lichtreacties hebben een membraan nodig om een "
                "protonengradiënt over op te bouwen.",
                "Merk op dat de glycolyse in het cytoplasma gebeurt, bij de melkzuurgisting. Dat "
                "verklaart waarom ook een cel zonder mitochondriën, en een cel zonder zuurstof, "
                "nog altijd die eerste stap kan zetten.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken waarin telkens iets net te absoluut staat. Zoek dus naar het "
                   "woord dat de bewering te sterk maakt: alleen, nooit, meer dan alles.",
            waarom=[
                "Niet waar. De Calvincyclus heeft zelf geen licht nodig, maar wel de ATP en de "
                "NADPH uit de lichtreacties. Daarom heet ze de lichtonafhankelijke reactie en niet "
                "de donkerreactie.",
                "Waar, en dat is met gemerkt water bewezen: de zuurstof komt uit het H2O en niet "
                "uit de CO2.",
                "Niet waar, en dit is de meest voorkomende misvatting. Een plant ademt dag en nacht, "
                "en overdag levert de fotosynthese enkel meer op dan de ademhaling verbruikt.",
                "Niet waar, en het verschil is groot: de glycolyse levert maar een paar ATP, "
                "terwijl de citroenzuurcyclus en de eindoxidaties samen het grootste deel leveren. "
                "Daarom hebben spier- en zenuwcellen zoveel mitochondriën.",
            ],
        ),
        dict(
            aanpak="Gisting is afbreken zonder zuurstof, en er zijn twee soorten met elk hun "
                   "eindproduct: melkzuur of ethanol met koolstofdioxide. Zet in de tabel het "
                   "product, het organisme en de toepassing.",
            waarom=[
                "Merk op dat het bij alcoholische gisting de koolstofdioxide is die het deeg doet "
                "rijzen, niet de alcohol: die verdampt in de oven.",
                "Noem waar de energie blijft: in het melkzuur of de ethanol zit nog veel energie "
                "opgeslagen. Dat alcohol brandt, bewijst het.",
                "Noem de hele keten: te weinig zuurstof, dus pyrodruivenzuur naar melkzuur, dus "
                "opstapeling. Het melkzuur zelf wordt nadien weer afgebroken, en daarom is de "
                "verzuring na een tijdje rust weg.",
            ],
        ),
        dict(
            aanpak="Bij een proef over fotosynthese gaat het telkens om één vraag: hoe weet je "
                   "dat het resultaat van je proef komt? Daarom eerst het zetmeel wegwerken, dan "
                   "één factor veranderen, en dan kijken waar het effect stopt.",
            waarom=[
                "Dit is het idee van een nulmeting: zonder die nacht in het donker weet je niet of "
                "het zetmeel oud of nieuw is. Elke goede proef begint met een gekende "
                "beginsituatie.",
                None,
                "Noem beide delen van het antwoord: meer belletjes, en een punt waar het stopt. "
                "Dat tweede is het begrip beperkende factor, en het geldt overal in de biologie: "
                "een proces gaat maar zo snel als zijn krapste schakel.",
            ],
        ),
        dict(
            aanpak="ATP is de kleine munt van de cel: ze geeft één fosfaatgroep af en wordt ADP. "
                   "Reacties die energie vrijgeven heten exo-energetisch, reacties die energie "
                   "vragen endo-energetisch.",
            waarom=[
                None,
                "Het voorvoegsel zegt het: exo is naar buiten, endo naar binnen. De celademhaling "
                "is exo-energetisch, de fotosynthese endo-energetisch.",
                "Noem er drie van verschillende soort: iets met beweging, iets met transport en "
                "iets met opbouw. Zo laat je zien dat ATP niet enkel voor spieren dient.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-niet-specifieke-en-specifieke-afweer-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie lijnen, en je herkent ze aan wat er gebeurt. De eerste lijn houdt buiten "
                   "en maakt geen onderscheid (huid, maagsap, slijm). De tweede lijn valt aan "
                   "zonder te weten wat het is (macrofaag, koorts, ontsteking). De derde lijn "
                   "richt zich op één bepaald antigen (B-cellen, T-cellen).",
            waarom=[
                "Houd het verschil tussen de tweede en de derde lijn vast: een macrofaag eet alles "
                "wat vreemd is, een plasmacel maakt antilichamen tegen één enkel antigen. "
                "Niet-specifiek tegenover specifiek, dat is het hele onderscheid.",
                "Koorts hoort bij de tweede lijn, ook al voelt het als een algemeen ziek zijn. Het "
                "is namelijk een reactie van het hele lichaam die geen onderscheid maakt tussen "
                "ziekteverwekkers.",
            ],
        ),
        dict(
            aanpak="Vier woorden die vaak door elkaar lopen. Een antigen is wat de reactie "
                   "uitlokt, een antilichaam is wat het lichaam ertegen maakt, een pathogeen is de "
                   "ziekteverwekker zelf. De tegenstelling antigen-antilichaam is de belangrijkste.",
            waarom=[
                None,
                "Let op de i tegenover de o: een antigen komt van buiten, een antilichaam maak je "
                "zelf. Wie die twee verwisselt, krijgt in bijna elke vraag van dit hoofdstuk een "
                "fout antwoord.",
                None,
                "Een bacterie is het antwoord, want ze is een eigen cel en kan zich buiten een "
                "gastheer vermeerderen. Een virus en een prion hebben de machinerie van een "
                "levende cel nodig, en dat is precies de reden dat antibiotica niet tegen een "
                "virus werken.",
            ],
        ),
        dict(
            aanpak="Vijf cellen, en elk heeft één rol in hetzelfde verhaal: de macrofaag meldt, "
                   "de T-helpercel dirigeert, de cytotoxische T-cel doodt, de plasmacel schiet met "
                   "antilichamen en de geheugencel blijft achter. Zet in de tabel telkens dat ene "
                   "werkwoord.",
            waarom=[
                "De T-helpercel is de belangrijkste van de vijf, want zonder haar doet geen van de "
                "andere iets. Precies daarom is hiv zo gevaarlijk, en dat komt in de volgende "
                "bundel terug.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken over afweer die alle vier de verkeerde kant op lijken te "
                   "wijzen. Vraag je bij elke: is dit een fout van het lichaam of een werkende "
                   "verdediging? Koorts en ontsteking zijn verdediging, geen schade.",
            waarom=[
                "Niet waar. Lichte koorts helpt, en ze onderdrukken kan de afweer zelfs trager "
                "maken. Enkel hoge koorts, lang aanhoudende koorts of koorts bij een baby vraagt "
                "een arts.",
                None,
                "Niet waar, het is net omgekeerd: roodheid, warmte, zwelling en pijn zijn de "
                "tekenen dat er bloed en afweercellen naar de plaats toestromen. Een ontsteking is "
                "de afweer aan het werk.",
                "Niet waar, en dit is het belangrijkste punt van de hele bundel. Antibiotica "
                "grijpen aan op iets wat enkel een bacterie heeft, bijvoorbeeld haar celwand. Een "
                "virus heeft dat niet, dus helpen ze niet bij griep of een verkoudheid.",
            ],
        ),
        dict(
            aanpak="Drie vragen die naar een verklaring vragen, niet naar een woord. Noem telkens "
                   "welke lijn of welke cel er in het spel is, en wat die precies doet. Dat is wat "
                   "een open vraag in dit hoofdstuk beoordeelt.",
            waarom=[
                "Noem beide kanten: slechter voor de indringer en beter voor de afweercellen. Eén "
                "van de twee is maar de helft van het antwoord.",
                "Noem het woord geheugencellen en zeg wat ze winnen: tijd. De eerste reactie duurt "
                "dagen, de tweede uren, en daarom merk je er niets meer van. Dit is ook precies "
                "waarop een vaccin steunt.",
                "Dit sluit aan bij de eerste reeks: een brandwond haalt de eerste verdedigingslijn "
                "weg. Daarom is infectie, en niet de wond zelf, bij grote brandwonden het "
                "grootste gevaar.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-immunisatie-bloedgroepen-en-falende-afweer-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee vragen beslissen de vier soorten. Maakt het lichaam de antilichamen zelf "
                   "(actief) of krijgt het ze kant-en-klaar (passief)? En gebeurt dat door de "
                   "natuur of door een arts (natuurlijk of kunstmatig)? Alles met een prik of een "
                   "vaccin is kunstmatig.",
            waarom=[
                "Moedermelk en placenta zijn de twee natuurlijke manieren om antilichamen te "
                "krijgen, en ze zijn dus passief: de baby maakt ze niet zelf en is daardoor maar "
                "enkele maanden beschermd.",
                None,
                "Noem beide kanten van de afweging: een inspuiting werkt meteen maar kort, een "
                "vaccin werkt traag maar lang. Daarom krijg je na een risicowond een inspuiting "
                "én soms een vaccin, elk met een eigen doel.",
            ],
        ),
        dict(
            aanpak="Bij bloedgroepen draait alles om één regel: je hebt nooit antilichamen tegen "
                   "je eigen antigen. Zet dus eerst het antigen in de tabel, en zet er dan het "
                   "andere antilichaam bij. Groep O heeft geen antigen en dus beide antilichamen.",
            waarom=[
                "Vul de tabel in die orde in en je kan nooit fout zitten: eerst het antigen van de "
                "naam, dan de antilichamen tegen wat je zelf niet hebt.",
                "O is universele donor omdat er op die bloedcellen geen antigen staat waarop de "
                "ontvanger kan reageren. Bij grote hoeveelheden speelt het plasma wel mee, en "
                "daarom werkt men in de praktijk met gewassen bloedcellen.",
                "AB is universele ontvanger omdat die persoon geen anti-A en geen anti-B heeft. "
                "Let op dat donor en ontvanger dus net omgekeerd liggen.",
                "Noem het antilichaam bij naam en zeg wat het doet: anti-B klontert de cellen "
                "samen. Die klontering heet agglutinatie en kan dodelijk zijn.",
                "Noem de D-factor en het gevaar voor een volgend kind. Daarom krijgt een "
                "resusnegatieve moeder vandaag een inspuiting met anti-D, zodat haar lichaam de "
                "antilichamen niet zelf aanmaakt.",
            ],
        ),
        dict(
            aanpak="Drie manieren waarop de afweer kan mislopen, en elk heeft een eigen fout. Een "
                   "allergie reageert te sterk op iets onschuldigs, een auto-immuunziekte valt het "
                   "eigen lichaam aan, een immuundeficiëntie doet te weinig. Vraag je dus: te veel, "
                   "verkeerd gericht, of te weinig?",
            waarom=[
                "Type 1 diabetes staat er bewust bij, want veel mensen weten niet dat het een "
                "auto-immuunziekte is: de afweer vernietigt de cellen in de pancreas die insuline "
                "maken.",
                None,
                "Zet het verschil in één woord: bij een allergie komt de dader van buiten, bij een "
                "auto-immuunziekte van binnen. In beide gevallen is het de reactie die het "
                "probleem is, niet de stof.",
                "Noem de T-helpercel, want dat is het hele antwoord. Hiv doodt de dirigent van de "
                "afweer, en daarna zijn het de gewone infecties die een patiënt doen sterven.",
                "Waar, en het laat zien dat afstoting geen fout van de afweer is maar haar normale "
                "werk. Daarom moet men na een transplantatie de afweer levenslang onderdrukken, "
                "met een hoger risico op infecties als prijs.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-gametogenese-en-de-hormonale-regeling-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de twee processen naast elkaar op vier punten: waar, hoeveel bruikbare "
                   "cellen, wanneer het begint en wanneer het stopt. Op elk van die vier punten "
                   "verschillen ze, en net daarop wordt gevraagd.",
            waarom=[
                "Het grootste verschil is het aantal: vier zaadcellen tegenover één eicel uit "
                "dezelfde meiose. Dat de oögenese al voor de geboorte begint, verklaart ook waarom "
                "de leeftijd van de moeder meespeelt: die cellen liggen er al tientallen jaren.",
                "Noem het cytoplasma, want daar gaat het om. Een zaadcel moet enkel zwemmen, een "
                "eicel moet de eerste dagen van een embryo voeden, en daarom krijgt zij alles mee "
                "en de poollichaampjes niets.",
            ],
        ),
        dict(
            aanpak="Zes hormonen, en de ordening zit in de keten: de hypofyse stuurt FSH en LH, "
                   "de eierstok antwoordt met oestrogeen en progesteron, de teelbal met "
                   "testosteron, en hCG komt enkel bij een zwangerschap. Zoek dus eerst wie het "
                   "hormoon maakt.",
            waarom=[
                "FSH en LH staan in de juiste orde van de cyclus: FSH laat rijpen, LH laat "
                "springen. De letters helpen: F van follikel, L van loslaten.",
                "hCG is het hormoon waarop een zwangerschapstest reageert. Dat het het geel "
                "lichaam in stand houdt, is precies waarom de menstruatie dan uitblijft.",
            ],
        ),
        dict(
            aanpak="De cyclus van 28 dagen heeft twee helften met de ovulatie in het midden. Voor "
                   "dag 14 rijpt de follikel, na dag 14 houdt het geel lichaam het slijmvlies in "
                   "stand. Valt dat weg, dan komt de menstruatie.",
            waarom=[
                "Dag 14 is een gemiddelde, niet een wet: de tweede helft is vrij vast rond "
                "veertien dagen, de eerste helft wisselt sterk van vrouw tot vrouw en van maand "
                "tot maand.",
                "Noem de keten: geel lichaam valt uiteen, progesteron zakt, slijmvlies laat los. "
                "De menstruatie is dus geen aparte gebeurtenis maar het gevolg van een hormoon "
                "dat wegvalt.",
                "Geef een echt voorbeeld, want de vraag vraagt erom. Negatieve feedback is overal "
                "in het lichaam hetzelfde idee als een thermostaat: het resultaat remt zijn eigen "
                "oorzaak af.",
                "Niet waar. De voorraad eicellen is bij de geboorte al vastgelegd en raakt op; "
                "daarom is de menopauze onomkeerbaar, terwijl de spermatogenese levenslang "
                "doorgaat.",
            ],
        ),
        dict(
            aanpak="Elk deel van een zaadcel hoort bij één taak: binnendringen, erfelijk "
                   "materiaal, energie, voortbeweging. Zet in de tabel dus niet wat het is maar "
                   "waarvoor het dient.",
            waarom=[
                "Dat het middenstuk vol mitochondriën zit, past bij de vorige bundel: zwemmen "
                "kost ATP. En het acrosoom laat zien waarom er veel zaadcellen nodig zijn, want "
                "hun enzymen helpen samen de omhulling open te maken.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken die je kan nakijken met de tabel van de eerste reeks. Twee "
                   "gaan over het verschil man-vrouw en twee over begrippen die vaak verwisseld "
                   "worden: follikel en geel lichaam, haploïd en diploïd.",
            waarom=[
                "Niet waar, en dit is de klassieke misvatting. Er komt geen nieuwe eicel bij; er "
                "rijpt elke maand één van de voorraad die er al voor de geboorte was.",
                None,
                None,
                "Niet waar, en het is net omgekeerd gesteld dan het hoort: beide gameten zijn "
                "haploïd, met 23 chromosomen. Pas na de bevruchting is de cel diploïd.",
            ],
        ),
        dict(
            aanpak="Drie begrippen en twee feiten over de man. Onthoud de bijbal als de plaats "
                   "waar de zaadcellen rijpen en bewaard worden, en de twee cijfers: ongeveer "
                   "zeventig dagen rijping, en een paar graden onder de lichaamstemperatuur.",
            waarom=[
                None,
                "Zeventig dagen is ook de reden dat een man die zijn levensstijl verandert, pas "
                "na twee tot drie maanden een ander resultaat ziet.",
                "Noem de temperatuur, want dat is het hele antwoord. Het verklaart ook waarom een "
                "warm bad, een laptop op de schoot of een te nauwe broek de vruchtbaarheid "
                "tijdelijk kan verlagen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bevruchting-embryo-en-foetus-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De eerste week verloopt in een vaste orde, en de plaats verandert mee: de "
                   "bevruchting gebeurt in de eileider, en terwijl de kiem naar de baarmoeder "
                   "zakt, deelt ze zich tot morula en blastula. Pas daar nestelt ze zich in.",
            waarom=[
                "Zet de namen op grootte van de celgroep: één cel, dan een klompje (morula), dan "
                "een bolletje met een holte (blastula). De namen zeggen zelf wat je ziet, want "
                "morula betekent moerbei.",
                "De innesteling en de placenta komen helemaal achteraan, en dat moet ook: eerst "
                "moet de kiem de baarmoeder bereiken.",
                None,
                "Zes tot zeven dagen is ongeveer de tijd die de kiem nodig heeft om door de "
                "eileider te reizen. Gebeurt de innesteling toch in de eileider, dan heet dat een "
                "buitenbaarmoederlijke zwangerschap.",
            ],
        ),
        dict(
            aanpak="Vier vragen over de eerste dagen. Houd twee dingen vast: de zygote is de "
                   "bevruchte eicel, en bij de klievingsdelingen worden de cellen kleiner in "
                   "plaats van het geheel groter.",
            waarom=[
                None,
                "Dit is het punt dat vaak misgaat. Een gewone celdeling wordt voorafgegaan door "
                "groei; bij de klieving wordt enkel verdeeld. Daarom is een morula van zestien "
                "cellen niet groter dan de eicel waaruit ze komt.",
                "Niet waar. Zodra de eerste zaadcel binnen is, verandert de omhulling zodat er "
                "geen tweede meer door kan. Zonder dat slot zou de cel te veel chromosomen "
                "krijgen.",
                "Noem beide kanten: één eicel die splitst tegenover twee eicellen. Daaruit volgt "
                "ook het genetische gevolg, en dat is waarop de vraag mikt.",
            ],
        ),
        dict(
            aanpak="Drie kiembladen, drie groepen organen. Onthoud de buitenste als buitenkant en "
                   "zenuwstelsel, de binnenste als binnenkant van darm en longen, en het midden "
                   "als alles ertussen: spieren, skelet, bloed, nieren.",
            waarom=[
                "Dat huid en zenuwstelsel uit hetzelfde kiemblad komen, is het verrassendste van "
                "de drie en wordt daarom graag gevraagd. Het klopt ook met de ontwikkeling: de "
                "neurale buis ontstaat door een instulping van de buitenste laag.",
            ],
        ),
        dict(
            aanpak="De placenta is een uitwisselingsorgaan zonder vermenging: het bloed van moeder "
                   "en kind komt niet samen. Houd daarnaast de twee feiten over de geboorte vast: "
                   "de navelstreng verbindt, oxytocine zet de weeën in gang.",
            waarom=[
                "Noem het woord diffusie en het dunne membraan. Precies omdat het bloed niet "
                "vermengt, kan een moeder een andere bloedgroep hebben dan haar kind, en toch is "
                "er bij de resusfactor een risico omdat er bij de geboorte wel wat bloed overgaat.",
                None,
                "Oxytocine werkt met positieve feedback: de weeën maken meer oxytocine en dat "
                "maakt sterkere weeën. Dat is een van de weinige plaatsen in het lichaam waar de "
                "feedback niet remt maar versterkt.",
                "Noem de week én de reden. De grens valt daar omdat het soort ontwikkeling "
                "verandert: eerst aanleggen, dan groeien. Dat verklaart ook waarom de eerste "
                "weken de gevoeligste zijn, zoals in de laatste reeks.",
            ],
        ),
        dict(
            aanpak="Een teratogeen is een stof die de ontwikkeling schaadt, en het gevaar hangt "
                   "vooral af van het tijdstip. Zet bij elk advies dus de reden, want zonder reden "
                   "is het geen antwoord op deze vragen.",
            waarom=[
                None,
                "Dit sluit aan bij de vorige reeks: in de eerste acht weken worden de organen "
                "aangelegd, en wat dan fout gaat, kan niet meer hersteld worden. Juist in die "
                "weken weet een vrouw soms nog niet dat ze zwanger is.",
                "Noem er drie met telkens een reden, en kies er drie van verschillende soort: iets "
                "dat de hersenen schaadt, iets dat de zuurstof vermindert, en iets met een "
                "ziekteverwekker. Zonder de reden erbij levert zo'n opsomming geen punten op.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vruchtbaarheid-regelen-en-behandelen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vier soorten, en de naam zegt waar ze ingrijpen. Een barrière houdt de "
                   "zaadcellen fysiek tegen, een hormonale methode grijpt in op de cyclus, een "
                   "natuurlijke methode berekent of meet, een chirurgische ingreep sluit de "
                   "banen af.",
            waarom=[
                None,
                None,
                "Dit is het belangrijkste punt van de hele bundel, en het komt in de laatste reeks "
                "terug: enkel een barrière houdt ook ziekteverwekkers tegen. Een hormonale methode "
                "doet dat niet, hoe betrouwbaar ze ook is tegen zwangerschap.",
            ],
        ),
        dict(
            aanpak="Zet bij elk middel op welk moment het ingrijpt: voor de ovulatie, voor de "
                   "bevruchting of voor de innesteling. Daarmee kan je ook het verschil tussen de "
                   "morning-afterpil en de abortuspil uitleggen.",
            waarom=[
                "Merk op dat de meeste middelen vóór de bevruchting werken: de pil houdt de "
                "ovulatie tegen, het condoom de zaadcellen. Het spiraaltje is het enige dat op "
                "twee plaatsen in de keten werkt.",
                "Zet het verschil in de tijd: voorkomen tegenover beëindigen. Dat onderscheid is "
                "ook wettelijk en medisch van belang, want het zijn twee verschillende "
                "geneesmiddelen met een verschillend tijdsvenster.",
            ],
        ),
        dict(
            aanpak="De pearlindex zegt hoeveel zwangerschappen er optreden bij honderd vrouwen die "
                   "een jaar lang hetzelfde middel gebruiken. Hoe lager dat getal, hoe "
                   "betrouwbaarder. En een methode die op meten berust, is altijd gevoeliger voor "
                   "toeval dan een methode die iets tegenhoudt.",
            waarom=[
                None,
                "Noem beide zwakke plekken: de meting zelf en de wisselende cyclus. Daarbij komt "
                "nog dat zaadcellen enkele dagen in het lichaam kunnen overleven, zodat de "
                "vruchtbare periode breder is dan één dag.",
                "Waar, en let op de richting: laag is goed. Dat is tegen de intuïtie, want bij de "
                "meeste cijfers is hoger beter.",
            ],
        ),
        dict(
            aanpak="Drie behandelingen op een lijn van weinig naar veel ingrijpen: inseminatie "
                   "brengt zaadcellen binnen, IVF laat de bevruchting buiten het lichaam gebeuren, "
                   "ICSI spuit één zaadcel in de eicel. Hoe groter het probleem met de zaadcellen, "
                   "hoe verder je op die lijn gaat.",
            waarom=[
                None,
                "Noem het probleem bij naam: te weinig of te weinig beweeglijke zaadcellen. Bij "
                "ICSI hoeft de zaadcel zelf niets meer te doen, en daarom is het de methode voor "
                "juist dat geval.",
                "Noem er vier en zeg erbij dat het voor beide partners geldt, want dat is de hele "
                "pointe van deze reeks. Dat ook de leeftijd van de man meespeelt, is minder "
                "bekend en wel waar.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken die je met de vorige reeksen kan nakijken. Twee ervan gaan "
                   "over een verwarring die vaak voorkomt: de pil en soa's, en waar de bevruchting "
                   "bij IVF gebeurt.",
            waarom=[
                "Niet waar, en het is de belangrijkste misvatting uit deze bundel. Dit is ook de "
                "vraag die in de laatste reeks als gesprek terugkomt.",
                "Waar, en dat is net de reden dat er een gesprek met een arts aan voorafgaat: een "
                "sterilisatie is soms nog om te keren, maar dat lukt lang niet altijd.",
                None,
                "Niet waar: in vitro betekent letterlijk in glas. De bevruchting gebeurt in het "
                "labo, en daarna wordt de kiem in de baarmoeder geplaatst.",
            ],
        ),
        dict(
            aanpak="Twee vragen waarin je de leerstof moet gebruiken in een gesprek. Antwoord dus "
                   "niet met een term maar met het argument, en zeg wat er ontbreekt in wat de "
                   "ander zegt.",
            waarom=[
                "Dit is dezelfde inhoud als vraag 12, nu in een gesprek. Een goed antwoord geeft "
                "de ander gelijk op het punt waar hij gelijk heeft en vult aan waar het mis gaat: "
                "de pil voorkomt een zwangerschap, niet een besmetting.",
                "Noem het cijfer achter het advies: de oorzaak ligt ongeveer even vaak bij de man "
                "als bij de vrouw, en vaak bij beiden samen. Daarom is eenzijdig onderzoek "
                "verloren tijd.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-dna-rna-en-de-replicatie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee paren om vast te houden: A hoort bij T en C hoort bij G. Schrijf de "
                   "streng onder elkaar en vervang base per base, van links naar rechts. Bij RNA "
                   "vervang je de T door een U.",
            waarom=[
                "Controleer je antwoord door de twee strengen onder elkaar te leggen: elke A moet "
                "een T onder zich hebben en elke C een G. Eén verschoven letter zie je zo meteen.",
                None,
                "Let op het verschil met de vorige oefeningen: bij mRNA komt er U waar je T zou "
                "schrijven. Al de rest blijft hetzelfde paren.",
            ],
        ),
        dict(
            aanpak="Drie verschillen tussen DNA en RNA: de suiker (deoxyribose tegenover ribose), "
                   "de base (thymine tegenover uracil) en het aantal strengen. Alles wat beide "
                   "nodig hebben om nucleïnezuur te zijn (fosfaat, de andere basen) is dus beide.",
            waarom=[
                "Thymine en uracil zijn het snelste kenmerk: zie je een U, dan is het RNA, zie je "
                "een T, dan is het DNA. Guanine en cytosine zitten in beide.",
                "De naam zegt het verschil in de suiker: deoxy betekent zonder zuurstof, en dat "
                "ene zuurstofatoom minder maakt DNA stabieler. Daarom bewaart de cel haar "
                "erfelijke informatie in DNA en niet in RNA.",
            ],
        ),
        dict(
            aanpak="De regel van Chargaff: A is gelijk aan T en C is gelijk aan G, en samen is "
                   "alles 100 procent. Zet dus eerst de twee die je kent, trek de som van 100 af, "
                   "en deel de rest in twee gelijke helften.",
            waarom=[
                None,
                "Reken na: A en T zijn samen 60 procent, dus blijft er 40 procent voor C en G "
                "samen, en dat is 20 procent elk.",
                "Schrijf je stappen op zoals in het antwoord, want de vraag vraagt de reden en "
                "niet het getal. De hele berekening steunt op het paren van de basen, en dat is "
                "ook het bewijs dat ze paren.",
            ],
        ),
        dict(
            aanpak="Van dun naar dik: DNA rond histonen geeft chromatine, en dat opgewonden geeft "
                   "een chromosoom met twee chromatiden die aan het centromeer samenhangen. Leer "
                   "die vier woorden in die orde.",
            waarom=[
                None,
                None,
                None,
                "Noem het getal, want dat maakt het concreet: ongeveer twee meter DNA in een kern "
                "van enkele micrometer. Dat is ongeveer alsof je dertig kilometer draad in een "
                "tennisbal moet krijgen, en toch nog netjes in twee kan verdelen.",
            ],
        ),
        dict(
            aanpak="Vijf enzymen, elk met één taak, en de orde is die van de werf: eerst "
                   "openwinden, dan spanning wegnemen, dan een beginstukje leggen, dan bouwen, dan "
                   "de stukken aan elkaar plakken. De uitgang -ase verraadt telkens dat het om een "
                   "enzym gaat.",
            waarom=[
                "De namen helpen: helicase van helix, polymerase van polymeer, ligase van "
                "verbinden. Wie de naam uitpakt, hoeft de taak niet los uit het hoofd te leren.",
                None,
                "Semiconservatief betekent half bewaard: elke dochterhelix houdt één oude streng "
                "bij. Dat is ook experimenteel bewezen, met zwaar stikstof in het klassieke "
                "experiment van Meselson en Stahl.",
                "Dit is de moeilijkste vraag van de bundel. Noem de twee feiten die het "
                "verklaren: polymerase bouwt maar in één richting, en de strengen lopen "
                "tegengesteld. Daaruit volgt de leidende streng in één stuk en de volgende streng "
                "in okazakifragmenten.",
                "Niet waar, en dit is dezelfde inhoud als vraag 15. Elke nieuwe dubbele helix "
                "bevat één oude streng; wie hier waar antwoordt, heeft het woord semiconservatief "
                "nog niet door.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-celcyclus-mitose-en-meiose-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De celcyclus bestaat uit vier stukken: G1 groeien, S kopiëren, G2 nakijken, M "
                   "delen. De letters helpen: S van synthese, M van mitose, en de twee G's zijn de "
                   "tussenpauzes.",
            waarom=[
                "Houd de S-fase goed vast, want daar verdubbelt het DNA. Alles wat je nadien over "
                "chromatiden berekent, hangt af van de vraag of de S-fase al gebeurd is.",
                None,
                None,
                "Noem wat er gecontroleerd wordt, want daar vraagt de oefening naar. Juist het "
                "wegvallen van die controle is wat een cel tot een tumorcel maakt: ze blijft delen "
                "ondanks de fouten.",
            ],
        ),
        dict(
            aanpak="Vier fasen in een vaste orde, en elke fase heeft één beeld. Profase: "
                   "chromosomen worden zichtbaar. Metafase: alles op één lijn. Anafase: "
                   "uiteentrekken. Telofase: twee nieuwe kernen. De voorvoegsels zeggen het: pro "
                   "is voor, meta is midden, ana is omhoog of uiteen, telo is einde.",
            waarom=[
                "Metafase is de fase die je op een foto het makkelijkst herkent: alle chromosomen "
                "netjes op een rij in het midden. Daarom gebruikt men net dat beeld om "
                "chromosomen te tellen.",
                None,
            ],
        ),
        dict(
            aanpak="Zet mitose en meiose naast elkaar op vijf punten: aantal delingen, aantal "
                   "dochtercellen, aantal chromosomen, of ze gelijk zijn, en waarvoor ze dienen. "
                   "Op alle vijf verschillen ze, en dat maakt de tabel makkelijk te onthouden.",
            waarom=[
                "Het kortste houvast: mitose is kopiëren, meiose is halveren en mengen. Daaruit "
                "volgen alle vijf de rijen van de tabel.",
            ],
        ),
        dict(
            aanpak="Houd twee regels vast. Mitose houdt het aantal gelijk, meiose halveert het. En "
                   "na de S-fase heeft elk chromosoom twee chromatiden, dus verdubbel je dan het "
                   "aantal chromatiden en niet het aantal chromosomen.",
            waarom=[
                None,
                None,
                "Dit is de strikvraag van de reeks: nog altijd 46 chromosomen, maar elk met twee "
                "chromatiden, dus 92 chromatiden. Het aantal chromosomen verandert pas bij de "
                "deling zelf.",
                "Noem het woord haploïd en de reden. 2n is 18, dus n is 9, en een stuifmeelkorrel "
                "is bij een plant het mannelijke gametenstadium.",
            ],
        ),
        dict(
            aanpak="Twee mechanismen maken elke gameet anders: crossing-over wisselt stukken uit "
                   "binnen een paar, en de onafhankelijke verdeling gooit de paren toevallig door "
                   "elkaar. Beide gebeuren enkel bij de meiose.",
            waarom=[
                None,
                "Reken even mee met de orde van grootte: met 23 paren die elk twee kanten op "
                "kunnen, zijn er al meer dan acht miljoen combinaties, en dan komt crossing-over "
                "daar nog bij.",
                "Noem het woord variatie en wat het oplevert bij verandering. Dit is het verband "
                "tussen dit hoofdstuk en de evolutieleer: zonder variatie valt er niets te "
                "selecteren.",
                "Niet waar. Bij de mitose liggen de homologe chromosomen niet tegen elkaar en "
                "wisselen ze dus niets uit; dat is precies waarom de dochtercellen van een mitose "
                "identiek zijn.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-overerving-en-de-wetten-van-mendel-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes woorden die elkaar paarsgewijs verklaren: genotype tegenover fenotype, "
                   "homozygoot tegenover heterozygoot, dominant tegenover recessief. Leer ze per "
                   "paar en niet los.",
            waarom=[
                "Houd genotype en fenotype uit elkaar met de g van genen en de f van wat je kan "
                "fotograferen. Twee dieren met hetzelfde fenotype kunnen een verschillend genotype "
                "hebben, en dat is de kern van vraag 7.",
                "Let op de formulering bij recessief: het toont zich enkel als het dominante allel "
                "er niet is, dus enkel bij homozygoot recessief.",
            ],
        ),
        dict(
            aanpak="Werk elke kruising in drie stappen: eerst de gameten van elke ouder, dan het "
                   "schema met vier vakjes, dan de verhoudingen. Schrijf de genotypes en de "
                   "fenotypes apart, want dat zijn twee verschillende verhoudingen.",
            waarom=[
                None,
                None,
                "Dit is de klassieke 1 op 2 op 1 en 3 op 1. Let op dat de genotypeverhouding drie "
                "groepen heeft en de fenotypeverhouding maar twee, omdat BB en Bb hetzelfde "
                "ogen.",
                "Een kruising met een homozygoot recessieve partner geeft altijd 1 op 1. Daarom "
                "gebruikt men net zo'n kruising om een genotype te testen, en dat is wat de "
                "volgende vraag doet.",
                "Noem de reden erbij, want die maakt het antwoord: één wit jong bewijst dat het "
                "zwarte dier een b-allel heeft. Eén nakomeling volstaat als bewijs, en dat is het "
                "mooie van een testkruising.",
            ],
        ),
        dict(
            aanpak="Bij twee genen vermenigvuldigt alles: twee soorten gameten per gen geeft vier "
                   "combinaties, en een schema van vier bij vier geeft zestien vakjes. De "
                   "verhouding 9 op 3 op 3 op 1 volgt daar rechtstreeks uit.",
            waarom=[
                "Reken het na met de formule 2 tot de macht van het aantal heterozygote genen: "
                "twee heterozygote genen geven 2 maal 2, dus vier soorten gameten.",
                "Schrijf ze systematisch op en niet door elkaar: eerst AB en Ab, dan aB en ab. Zo "
                "vergeet je er geen.",
                None,
                "Reken na: de kans op aa is een vierde en de kans op bb ook, dus samen een "
                "zestiende. Dat is ook het enige vakje van de zestien dat volledig recessief is.",
            ],
        ),
        dict(
            aanpak="Vier uitzonderingen op het eenvoudige schema. Intermediair geeft een "
                   "tussenvorm, codominant toont beide, multipele allelie betekent meer dan twee "
                   "allelen, X-gebonden betekent dat het gen op het X-chromosoom ligt. Dat "
                   "laatste herken je aan een verschil tussen mannen en vrouwen.",
            waarom=[
                "Houd intermediair en codominant uit elkaar: bij intermediair krijg je iets nieuws "
                "ertussen (roze), bij codominant zie je beide volledig naast elkaar (groep AB).",
                "Het kenmerk van X-gebonden in een stamboom is dat de aandoening van grootvader "
                "via een dochter naar een kleinzoon springt. Die dochter is draagster en toont "
                "niets.",
                "Noem het verschil in aantal X-chromosomen, want dat is het hele antwoord. Een man "
                "heeft geen tweede X om het op te vangen, en daarom volstaat één allel bij hem.",
                "Niet waar, en dit is de logische vervolgvraag. Een vader geeft zijn zoon een Y en "
                "zijn dochter een X, dus kan een X-gebonden allel nooit rechtstreeks van vader naar "
                "zoon gaan.",
            ],
        ),
        dict(
            aanpak="In een stamboom lees je het allel uit het patroon. Slaat de aandoening "
                   "generaties over, dan is ze recessief. Komt ze in elke generatie voor, dan is "
                   "ze dominant. Zit ze bijna enkel bij mannen, dan is ze X-gebonden.",
            waarom=[
                "Noem het woord drager, want daar draait het om: iemand kan het allel doorgeven "
                "zonder het te tonen. Dat kan enkel bij een recessief allel.",
                "Reken de kans na: beide ouders zijn Bb, dus is de kans op bb een vierde. Let op "
                "dat die kans voor elk kind opnieuw geldt en niet opgebruikt raakt: na één ziek "
                "kind is de kans bij het volgende weer één op vier.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-genexpressie-transcriptie-en-translatie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Werk in vaste stappen: eerst het mRNA uit de DNA-streng (A bij U, T bij A, C "
                   "bij G, G bij C), dan de codons per drie afsplitsen, dan tellen. Negen "
                   "nucleotiden zijn dus altijd drie codons.",
            waarom=[
                "Controleer je antwoord op de start: T A C in het DNA geeft A U G in het mRNA, en "
                "dat is net het startcodon. Dat is geen toeval maar een geheugensteun.",
                "Reken na: 9 gedeeld door 3 is 3 codons, dus drie aminozuren. Eén codon is altijd "
                "drie nucleotiden, en dat getal drie is de sleutel van heel dit hoofdstuk.",
                None,
                "De drie stopcodons zijn de enige codons die geen aminozuur aanduiden. Daarom "
                "zijn er 64 codons voor 20 aminozuren en niet 61 die allemaal iets coderen.",
            ],
        ),
        dict(
            aanpak="Reken met de getallen: vier basen op drie plaatsen geeft 4 maal 4 maal 4, dus "
                   "64 codons, voor maar 20 aminozuren. Daaruit volgt dat de code gedegenereerd "
                   "is, en dat ze bij bijna alle organismen dezelfde is.",
            waarom=[
                "Reken na waarom het drie moet zijn: met twee basen zou je 16 combinaties hebben, "
                "en dat is te weinig voor 20 aminozuren.",
                "Noem het woord gedegenereerd en het gevolg: een mutatie in de derde base "
                "verandert vaak niets. Dat is een ingebouwde veiligheid in de code zelf.",
                "Dit is de basis van de hele biotechnologie: omdat de code universeel is, kan een "
                "bacterie menselijke insuline maken. Noem het woord universeel in je antwoord.",
            ],
        ),
        dict(
            aanpak="Zet de twee processen naast elkaar op vier punten: waar, door welk enzym of "
                   "organel, wat erin gaat en wat eruit komt. Transcriptie is DNA naar RNA in de "
                   "kern, translatie is RNA naar eiwit in het cytoplasma.",
            waarom=[
                "De namen zeggen het verschil: transcriptie is overschrijven in dezelfde taal "
                "(nucleïnezuur naar nucleïnezuur), translatie is vertalen naar een andere taal "
                "(nucleotiden naar aminozuren).",
            ],
        ),
        dict(
            aanpak="Het pre-mRNA moet eerst rijpen: de introns eruit, de exons aan elkaar, en een "
                   "cap en een staart erbij. Onthoud de letters: in-trons gaan erin blijven zitten "
                   "als afval, ex-ons gaan eruit naar het ribosoom.",
            waarom=[
                None,
                "Noem beide en zeg waarvoor ze dienen, want de vraag vraagt de functie. Zonder "
                "cap en staart wordt het mRNA in de cel snel afgebroken.",
                "Alternatieve splicing is het antwoord op een raadsel: de mens heeft ongeveer "
                "20 000 genen en veel meer verschillende eiwitten. Eén gen kan dus meerdere "
                "eiwitten leveren.",
            ],
        ),
        dict(
            aanpak="Op het ribosoom komen drie moleculen samen: het mRNA met de boodschap, het "
                   "tRNA met het aminozuur, en het ribosoom zelf als werkbank. Het anticodon van "
                   "het tRNA is het complement van het codon, dus pas je dezelfde paringsregels "
                   "toe als bij het DNA, met U in plaats van T.",
            waarom=[
                None,
                None,
                "Reken na met de paringsregels: G hoort bij C, C bij G, A bij U. GCA geeft dus "
                "CGU. Let erop dat je bij RNA nooit een T schrijft.",
                "Beschrijf het in de drie stappen van het antwoord: starten, verlengen, stoppen. "
                "Dat is ook de indeling waarmee het in bijna elk handboek staat: initiatie, "
                "elongatie, terminatie.",
                "Niet waar. Meerdere ribosomen kunnen achter elkaar op hetzelfde mRNA zitten, en "
                "dat heet een polysoom. Zo maakt een cel in één keer veel kopieën van hetzelfde "
                "eiwit.",
            ],
        ),
        dict(
            aanpak="Een keten aminozuren is nog geen werkend eiwit. Er moet eerst gevouwen worden, "
                   "en vaak nog bijgewerkt in het ER en het golgi. En de vouw volgt uit de "
                   "volgorde, dus hangt de werking uiteindelijk aan die volgorde.",
            waarom=[
                "Dit sluit aan bij de eerste bundel: het golgi-apparaat werkt eiwitten af. Wat op "
                "het ribosoom gemaakt wordt, is dus een halffabricaat.",
                "Noem de keten van drie: volgorde bepaalt vouw, vouw bepaalt vorm, vorm bepaalt "
                "werking. Daarom kan één verkeerd aminozuur, zoals bij sikkelcelanemie, een heel "
                "eiwit onbruikbaar maken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-genregulatie-epigenetica-en-nature-of-nurture-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Beide vragen hebben hetzelfde antwoord in andere woorden: niet het DNA "
                   "verschilt tussen cellen, maar welke genen aan staan. Noem in je antwoord dus "
                   "altijd de kost van een eiwit maken en de keuze die de cel maakt.",
            waarom=[
                "Noem de kost, want dat is het argument: een eiwit maken vraagt aminozuren en "
                "ATP. Een bacterie die enzymen voor lactose maakt terwijl er geen lactose is, "
                "verspilt energie, en dat is precies wat het lac-operon vermijdt.",
                "Dit is dezelfde vraag als in de bundel over celdifferentiatie. Hetzelfde "
                "kookboek, een andere bladzijde open.",
            ],
        ),
        dict(
            aanpak="Het lac-operon heeft drie onderdelen: de promotor waar het polymerase aanhecht, "
                   "de operator als slagboom, en de repressor als slot op die slagboom. Lactose is "
                   "de sleutel die het slot wegneemt. Vertel het dus als een verhaal in die orde.",
            waarom=[
                "Houd promotor en operator uit elkaar: de promotor is de startplaats, de operator "
                "de slagboom er net achter. Beide zijn stukken DNA; de repressor is een eiwit.",
                "Noem de hele keten: repressor op de operator, polymerase geblokkeerd, geen "
                "enzymen. Zeg het in die richting, want de volgende vraag is net het omgekeerde.",
                "Let op hoe de regeling werkt: de lactose schakelt niets aan maar haalt een rem "
                "weg. Dat heet inductie, en het is zuiniger dan voortdurend aansturen.",
                "Noem het voordeel: één schakelaar voor alle genen van dezelfde taak. Daarom "
                "werken bacteriën met operons en wij met afzonderlijke regeling per gen.",
            ],
        ),
        dict(
            aanpak="Twee merktekens met een tegengesteld gevolg: methylgroepen op het DNA leggen "
                   "een gen stil, acetylgroepen op de histonen maken het leesbaar. Onthoud dat "
                   "acetylering het chromatine losser maakt, zodat het polymerase erbij kan.",
            waarom=[
                "De logica zit in de verpakking: losser opgewonden DNA is leesbaar, strak "
                "opgewonden DNA niet. Methylering trekt aan, acetylering laat los.",
                "Zet het verschil in de letters: een mutatie verandert de tekst, een epigenetische "
                "verandering zet er een markering bij of haalt die weg. De tekst zelf blijft.",
                "Dit is het bekendste bewijs dat epigenetica meespeelt. Noem de omgevingsfactoren "
                "bij naam: voeding, stress, roken, slaap. De tweeling begint met hetzelfde "
                "DNA en niet met dezelfde markeringen.",
                "Waar, en dat is het verrassendste van het hoofdstuk: sommige merktekens overleven "
                "de gametenvorming. Bij de mens is dat nog een onderzoeksgebied, bij planten en "
                "dieren zijn er duidelijke voorbeelden.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk kenmerk: ligt het vast in het DNA, komt het van de omgeving, "
                   "of werken ze samen? Zuivere nature-kenmerken zijn er weinig (bloedgroep, "
                   "oogkleur); bij bijna alles wat met gedrag of gezondheid te maken heeft, is het "
                   "antwoord beide.",
            waarom=[
                "Gewicht is het schoolvoorbeeld van beide: er is een erfelijke neiging én een "
                "omgeving van voeding en beweging. Wie hier één kant kiest, mist het punt.",
                "Lengte lijkt zuiver erfelijk en is het niet: de gemiddelde lengte in Vlaanderen "
                "steeg in honderd jaar met meer dan tien centimeter, en het DNA van de bevolking "
                "veranderde in die tijd niet.",
                "Noem beide soorten tweelingonderzoek, want samen maken ze het argument: "
                "verschillen tussen eeneiige tweelingen wijzen naar de omgeving, gelijkenissen bij "
                "apart opgegroeide tweelingen naar het DNA.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-mutaties-mutagenen-en-kanker-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vergelijk de twee rijen letter per letter en kijk wat er met het aantal "
                   "gebeurt. Evenveel letters met één andere is een substitutie, een letter minder "
                   "een deletie, een letter meer een insertie, en evenveel letters in een andere "
                   "orde een inversie.",
            waarom=[
                "Tel altijd eerst het aantal basen, want dat scheidt de vier soorten meteen in "
                "twee groepen. Pas daarna kijk je welke letter precies veranderd is.",
                "Bij a blijven alle letters dezelfde en staan ze enkel omgekeerd: T G C wordt C G "
                "T. Dat is het kenmerk van een inversie.",
                "Noem het woord leesraam, want dat is het hele antwoord. Het is hetzelfde als een "
                "letter weglaten in een zin die je per drie leest: alles erna verschuift en wordt "
                "onleesbaar.",
            ],
        ),
        dict(
            aanpak="Hier gaat het niet over de verandering in het DNA maar over het gevolg voor "
                   "het eiwit. Stil betekent geen verschil, missense betekent een ander aminozuur, "
                   "nonsense betekent een te vroeg stopcodon en dus een afgebroken eiwit.",
            waarom=[
                "Nonsense is de ernstigste van de drie, want het eiwit stopt halverwege en is "
                "bijna altijd onbruikbaar.",
                "Dit sluit aan bij de gedegenereerde code uit de vorige bundel. Vooral de derde "
                "letter van een codon is vaak vrij, en daarom blijft een mutatie daar zonder "
                "gevolg.",
                "Noem de keten: ander aminozuur, andere vouw, ander gedrag van het eiwit. Dit is "
                "het beste voorbeeld dat één letter in drie miljard al genoeg kan zijn.",
            ],
        ),
        dict(
            aanpak="Drie niveaus van klein naar groot: een genmutatie zit in één gen, een "
                   "chromosoommutatie verandert de bouw van een chromosoom, een genoommutatie "
                   "verandert het aantal chromosomen. Vraag je dus: letters, stukken of hele "
                   "chromosomen?",
            waarom=[
                None,
                "Trisomie 21 is het bekendste voorbeeld van een genoommutatie: er is één "
                "chromosoom 21 te veel, en dat is het downsyndroom. Het voorbeeld van chromosoom "
                "9 en 22 is de philadelphiatranslocatie, die bij een vorm van leukemie voorkomt.",
                "Non-disjunctie is de oorzaak achter een trisomie: bij de meiose gaan twee "
                "chromosomen van hetzelfde paar samen naar één cel.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: zit de mutatie in een geslachtscel of in een lichaamscel? "
                   "Alleen een geslachtscel geeft haar DNA aan een volgende generatie door. Zet "
                   "dus bij elk antwoord die reden.",
            waarom=[
                "Merk op dat a en c de meest voorkomende mutaties van allemaal zijn en toch niet "
                "erfelijk. Dat ze niet erfelijk zijn, betekent dus niet dat ze onschuldig zijn: "
                "het zijn juist die mutaties die kanker veroorzaken.",
                "Noem het verschil tussen een lichaamscel en een geslachtscel. Daarom spreekt men "
                "ook van somatische tegenover germinale mutaties.",
            ],
        ),
        dict(
            aanpak="Kanker ontstaat niet uit één fout. Onthoud het tweetal oncogen en "
                   "tumorsuppressorgen: het ene is een gaspedaal dat blijft hangen, het andere een "
                   "rem die uitvalt. Pas met beide samen gaat een cel ongeremd delen.",
            waarom=[
                None,
                "Noem er drie van verschillende soort, want de vraag vraagt soorten en niet drie "
                "keer hetzelfde: straling, een chemische stof en een virus. Dat ook een virus een "
                "mutageen kan zijn, is minder bekend en de reden dat er een vaccin tegen HPV "
                "bestaat.",
                "Het beeld van de auto helpt: een oncogen is een gaspedaal dat vast zit, een "
                "tumorsuppressorgen een rem die niet meer werkt. Een auto rijdt pas echt op hol "
                "als beide mislopen.",
                "Dit is het meertrapsmodel van kanker, en het verklaart twee dingen: waarom kanker "
                "vooral op latere leeftijd voorkomt, en waarom iemand die een mutatie erft, er "
                "vroeger en vaker ziek van wordt.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-dna-technologie-en-gentechnologie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet het gereedschap in de orde van het werk: knippen met een restrictie-enzym, "
                   "plakken met ligase, binnenbrengen met een vector, vermenigvuldigen met PCR, "
                   "scheiden met een gel, uitlezen met sequencing. Elk woord hoort bij precies één "
                   "handeling.",
            waarom=[
                "Dat een restrictie-enzym op een vaste plaats in de sequentie knipt, is wat de "
                "hele techniek mogelijk maakt: twee stukken DNA die met hetzelfde enzym geknipt "
                "zijn, passen op elkaar.",
                "Houd PCR en sequencing uit elkaar: PCR maakt meer van hetzelfde, sequencing leest "
                "wat er staat. Ze worden vaak na elkaar gebruikt en doen iets heel verschillends.",
                "CRISPR-Cas werkt als een zoek-en-vervangfunctie: een stukje RNA wijst de plaats "
                "aan en het enzym knipt daar. Dat precieze aanwijzen is wat het verschilt van de "
                "oudere technieken.",
            ],
        ),
        dict(
            aanpak="Drie manieren waarop bacteriën van nature DNA uitwisselen. De namen zeggen "
                   "het: transformatie is opnemen van buiten, conjugatie is een brug tussen twee "
                   "bacteriën, transductie is overbrengen door een virus.",
            waarom=[
                None,
                "Noem het plasmide, want dat is de kern van het antwoord. Het verklaart ook waarom "
                "resistentie zelfs tussen verschillende soorten bacteriën overgaat, en waarom "
                "antibiotica alleen gebruiken als het nodig is zo belangrijk is.",
            ],
        ),
        dict(
            aanpak="Een PCR-cyclus heeft drie stappen die aan de temperatuur hangen: heet maakt "
                   "los, koeler laat de primers binden, lauwwarm laat het polymerase bouwen. En "
                   "elke cyclus verdubbelt, dus reken met machten van twee.",
            waarom=[
                "De drie stappen heten denaturatie, annealing en extensie, en ze gebeuren in een "
                "toestel dat enkel de temperatuur regelt. Daarom kan één machine miljoenen kopieën "
                "maken zonder dat er iemand bij moet.",
                "Reken na: 2 tot de tiende is 1024, dus tien cyclussen. Omdat het verdubbelt, "
                "volstaan twintig cyclussen al voor meer dan een miljoen kopieën.",
            ],
        ),
        dict(
            aanpak="Twee eigenschappen verklaren een gel: DNA is negatief geladen, dus wandelt het "
                   "naar de pluspool, en kleine stukken schuiven sneller door de gel dan grote. "
                   "Daarmee kan je elke vraag over een bandenpatroon beantwoorden.",
            waarom=[
                "Noem de fosfaatgroepen, want dat is de reden van de lading. Zonder die lading zou "
                "elektroforese niet werken.",
                "Het beeld van een zeef helpt: kleine korrels raken er sneller door dan grote. "
                "Daarom staan de kleine fragmenten onderaan de gel, het verst van de start.",
                "Noem de herhalingen, want daar zit het verschil tussen mensen. Dit is de basis "
                "van forensisch onderzoek en van een vaderschapstest.",
            ],
        ),
        dict(
            aanpak="Drie soorten klonen, elk met een ander doel: een heel individu, een stuk DNA, "
                   "of weefsel voor een patiënt. En bij de toepassingen hoort altijd een afweging, "
                   "dus noem bij een voordeel ook een bezorgdheid.",
            waarom=[
                "Moleculair klonen is het meest gebruikte van de drie en haalt nooit het nieuws; "
                "reproductief klonen haalt altijd het nieuws en gebeurt bijna nooit.",
                "Beschrijf het in de drie stappen van het antwoord, met het gereedschap van de "
                "eerste reeks erin: knippen, plakken, binnenbrengen. Zo laat je zien dat je de "
                "techniek en niet enkel het verhaal kent.",
                "Zet het verschil in de grens: cisgeen blijft binnen wat ook door kruisen kon, "
                "transgeen gaat die grens over. Dat onderscheid speelt een rol in de discussie over "
                "de regels voor ggo's.",
                "Geef er echt één van elk, want de vraag vraagt een afweging. Een antwoord dat "
                "enkel voordelen of enkel bezwaren noemt, is geen afweging.",
                "Niet waar. Een kloon heeft hetzelfde DNA maar niet dezelfde omgeving, en zelfs "
                "niet dezelfde epigenetische merktekens. Dat is dezelfde les als bij de eeneiige "
                "tweeling uit de vorige bundel.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-argumenten-voor-evolutie-en-de-evolutietheorieen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf vakgebieden, vijf soorten bewijs. Zoek in de zin naar het soort "
                   "waarneming: een bouwplan is anatomie, een embryo embryologie, een fossiel "
                   "paleontologie, een molecule of een code moleculaire biologie, een verspreiding "
                   "over de aarde biogeografie.",
            waarom=[
                "Merk op dat de vijf argumenten elkaar onafhankelijk bevestigen. Dat is wat een "
                "theorie sterk maakt: vijf heel verschillende vakken komen bij dezelfde conclusie "
                "uit.",
                "Dat alle organismen dezelfde genetische code gebruiken, is het sterkste "
                "moleculaire argument: het wijst op één gemeenschappelijke voorouder van al het "
                "leven.",
            ],
        ),
        dict(
            aanpak="Houd twee woorden uit elkaar aan hun oorsprong. Homoloog betekent dezelfde "
                   "bouw en dezelfde afkomst, ook als de functie verschilt. Analoog betekent "
                   "dezelfde functie maar een andere bouw en afkomst. Kijk dus niet naar waar het "
                   "voor dient maar naar hoe het gebouwd is.",
            waarom=[
                "De vin van een haai en die van een dolfijn is het mooiste paar: allebei om te "
                "zwemmen, maar de ene is een visvin en de andere een omgebouwde poot. Dat heet "
                "convergente evolutie.",
                "Noem de twee woorden bouw en oorsprong, want daar hangt het verschil aan. "
                "Dezelfde functie in dezelfde omgeving geeft gelijkenis zonder verwantschap.",
                "Rudimentaire organen zijn een argument op zich: ze hebben enkel zin als restant "
                "van iets wat bij een voorouder wel werkte. De staartwervels en de "
                "oorspiertjes van de mens zijn voorbeelden.",
            ],
        ),
        dict(
            aanpak="Fossielen lezen steunt op twee regels: wat dieper ligt is ouder, en een "
                   "overgangsfossiel heeft kenmerken van twee groepen. Zoek bij zo'n fossiel dus "
                   "altijd beide groepen kenmerken.",
            waarom=[
                None,
                "Noem de kenmerken van beide groepen bij naam, want dat is waarom hij zo "
                "belangrijk is. Eén fossiel met veren én tanden laat zien dat die groepen niet "
                "altijd gescheiden waren.",
                None,
            ],
        ),
        dict(
            aanpak="Houd de twee theorieën uit elkaar aan de richting van de verandering. Bij "
                   "Lamarck verandert het individu eerst en wordt dat doorgegeven; bij Darwin is "
                   "de variatie er al en kiest de omgeving eruit. Zie je de woorden rekken, "
                   "oefenen of verworven, dan is het Lamarck.",
            waarom=[
                None,
                "Noem de geslachtscellen, want daar zit het antwoord. Dit is dezelfde logica als "
                "in de bundel over mutaties: wat in een lichaamscel verandert, gaat nergens heen.",
                "Noem alle drie, want Darwins theorie staat of valt met de drie samen: variatie, "
                "selectie en erfelijkheid. Valt er één weg, dan werkt het mechanisme niet.",
                "Zeg uitdrukkelijk wat fit niet betekent, want dat is de valkuil. Fit is passend "
                "bij de omgeving, en in een andere omgeving is dus iets anders fit.",
            ],
        ),
        dict(
            aanpak="De moderne theorie denkt in populaties en niet in individuen. Een populatie "
                   "evolueert doordat de allelfrequenties verschuiven; een individu doet dat niet. "
                   "Houd dat onderscheid vast, want de laatste vraag test precies dat.",
            waarom=[
                None,
                "Noem beide bronnen en het verschil: mutaties maken iets nieuw, de meiose "
                "herschikt wat er al is. Zonder mutaties zou de variatie uiteindelijk uitgeput "
                "raken.",
                "Dit is de kernvraag van de reeks. Zeg uitdrukkelijk dat het antibioticum "
                "selecteert en niet veroorzaakt, want juist die verwarring zit achter het "
                "misverstand dat bacteriën zich aanpassen aan een kuur.",
                "Niet waar, en dit is het verschil tussen een individu en een populatie. Een "
                "individu kan zich aanpassen (sterker worden, bruiner worden), maar evolueren doen "
                "enkel populaties over generaties heen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-selectie-soortvorming-en-de-menswording-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf mechanismen, en de vraag die ze scheidt is: wie of wat kiest? De "
                   "omgeving is natuurlijke selectie, een partner seksuele selectie, een mens "
                   "kunstmatige selectie, en niemand genetische drift. Gene flow is geen keuze "
                   "maar verhuizing.",
            waarom=[
                "Let op a: er kiest niemand, het is enkel toeval. Dat is het kenmerk van "
                "genetische drift, en in dit geval heet het een bottleneck of flessenhals.",
                None,
                "Het stichterseffect is een vorm van drift: de kleine groep die vertrekt, heeft "
                "toevallig niet dezelfde allelverhoudingen als de grote groep. Daarom hebben "
                "eilandpopulaties vaak bijzondere eigenschappen.",
            ],
        ),
        dict(
            aanpak="Vier vragen over begrippen die vaak verkeerd begrepen worden. Fitness gaat "
                   "over nakomelingen en niet over kracht, drift gaat over toeval en niet over "
                   "aanpassing. Zeg bij elke open vraag ook wat het niet is.",
            waarom=[
                "Zeg uitdrukkelijk wat het niet is, want dat is het punt van de vraag. Een "
                "onopvallend diertje met veel nakomelingen is fitter dan een sterk dier zonder.",
                "Het beeld van munten gooien helpt: tien keer kop op tien worpen gebeurt wel eens, "
                "duizend keer kop op duizend worpen nooit. Toeval weegt dus zwaarder in een kleine "
                "groep.",
                "Noem het woord drager, want dat is de reden. Dit is hetzelfde idee als bij een "
                "recessieve aandoening in een stamboom: wat niet te zien is, kan niet weggeselecteerd "
                "worden.",
                "Niet waar, en dat is net het verschil met selectie. Drift werkt zonder richting: "
                "ook een nuttig allel kan erdoor verdwijnen.",
            ],
        ),
        dict(
            aanpak="Zes vormen van isolatie, en ze vallen in twee groepen. Alles wat de "
                   "bevruchting verhindert, is prezygotisch (plaats, tijd, gedrag, gameten); wat "
                   "erna misloopt, is postzygotisch. Zoek dus eerst of er een bevruchting is "
                   "geweest.",
            waarom=[
                "Houd geografisch en ecologisch uit elkaar: bij geografisch is er een hindernis "
                "zoals een gebergte of een zee, bij ecologisch wonen ze op dezelfde plaats maar in "
                "een andere laag of op een andere ondergrond.",
                "Het muildier is het vaste voorbeeld van postzygotisch: de bevruchting lukt, het "
                "dier leeft, maar er komt geen volgende generatie.",
                "Zet de grens bij de bevruchting, want dat is de scheidslijn tussen de twee "
                "woorden. Zygote zit in de naam en wijst precies dat moment aan.",
                "Houd de twee woorden uit elkaar met hun voorvoegsel: allo betekent elders, sym "
                "betekent samen. Allopatrisch is dus met een hindernis ertussen, sympatrisch "
                "zonder.",
            ],
        ),
        dict(
            aanpak="Het soortbegrip hangt aan vruchtbare nakomelingen, niet aan uiterlijk. Reken "
                   "het antwoord dus altijd uit via die ene toets: komt er een volgende generatie "
                   "uit?",
            waarom=[
                "Het woord vruchtbaar is het sleutelwoord. Zonder dat woord is de definitie fout, "
                "want paard en ezel krijgen wel samen nakomelingen.",
                "Dit is de toepassing van de vorige vraag. Noem het woord onvruchtbaar, want daar "
                "hangt alles aan: de genen van de twee groepen komen niet duurzaam samen.",
                "Noem alle drie, en vergeet de tijd niet: isolatie zonder genoeg generaties geeft "
                "nog geen nieuwe soort.",
            ],
        ),
        dict(
            aanpak="Bij de menswording hangt bijna alles aan één verandering: rechtop lopen. Zoek "
                   "bij elke lichamelijke aanpassing dus het verband met die ene stap, en weeg bij "
                   "de hersenen de winst tegen de kost af.",
            waarom=[
                None,
                "Noem de drie aanpassingen en het verband met rechtop lopen, want dat is wat de "
                "vraag beoordeelt. Door rechtop te lopen kwamen de handen ook vrij, en dat maakte "
                "gereedschap mogelijk.",
                "Noem er twee van verschillende soort: iets over energie en iets over de geboorte. "
                "De bevalling bij de mens is door die combinatie van een breed hoofd en een smal "
                "bekken veel moeilijker dan bij andere zoogdieren.",
                "Niet waar, en dit is de bekendste misvatting van het hoofdstuk. Mens en chimpansee "
                "zijn neven met een gemeenschappelijke voorouder, en die voorouder was geen van "
                "beide.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-biomoleculen-sachariden-lipiden-en-proteinen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie groepen, en je herkent ze aan de uitgang of aan de bekendste leden. "
                   "Namen op -ose en -een van opslagstoffen zijn sachariden; vetten, oliën, "
                   "cholesterol en fosfolipiden zijn lipiden; namen op -ine die een taak uitvoeren "
                   "of een structuur vormen zijn proteïnen.",
            waarom=[
                "Glycogeen is de verrassing in de rij: het klinkt niet als een suiker en het is de "
                "opslagvorm van glucose in lever en spieren. Cholesterol klinkt niet als een vet "
                "en is er wel een.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Elke groep heeft haar bouwsteen: monosachariden voor de sachariden, glycerol "
                   "met vetzuren voor een triglyceride, aminozuren voor de proteïnen. En er zijn "
                   "maar twee reacties: aan elkaar zetten met waterverlies, of splitsen met "
                   "water.",
            waarom=[
                None,
                "De naam zegt het: condensatie laat water ontstaan. Daarom heet de omgekeerde "
                "reactie hydrolyse, letterlijk splitsen met water, en dat is precies wat er in je "
                "spijsvertering gebeurt.",
                None,
            ],
        ),
        dict(
            aanpak="Hier gaat het om twee suikerringen aan elkaar. Leer de drie disachariden met "
                   "hun bouwstenen: lactose is glucose met galactose, sacharose glucose met "
                   "fructose, maltose glucose met glucose. En let bij de lange ketens op de vorm, "
                   "want die bepaalt de functie.",
            waarom=[
                None,
                "Noem de vorm, want daar hangt alles aan: recht en naast elkaar geeft vezels, "
                "opgerold geeft een voorraad. Dezelfde bouwsteen, een andere binding, een heel "
                "andere stof.",
                "Noem het enzym, want dat is de reden. Een koe verteert cellulose niet zelf maar "
                "laat bacteriën in haar voormagen het werk doen, en daarom herkauwt ze.",
                None,
            ],
        ),
        dict(
            aanpak="Bij lipiden verklaart de vorm van de staart bijna alles. Een rechte, "
                   "verzadigde staart stapelt dicht en geeft een vaste stof; een geknikte, "
                   "onverzadigde staart stapelt los en geeft een olie. En een fosfolipide heeft "
                   "twee gezichten: een waterminnende kop en waterafstotende staarten.",
            waarom=[
                "Noem de dubbele binding en de knik, want dat is de oorzaak. Dit verklaart ook "
                "waarom men olie hardt om margarine te maken: men haalt de dubbele bindingen eruit.",
                "Dit is dezelfde uitleg als bij het celmembraan in de eerste bundel. Het "
                "belangrijkste woord is vanzelf: zo'n dubbellaag vormt zich spontaan in water, "
                "zonder dat er iets aan vastgehouden wordt.",
                "Noem er drie van verschillende soort, want vier keer energie is één antwoord. "
                "Dat lipiden ook grondstof zijn voor hormonen, wordt vaak vergeten.",
                "Noem de waterstof, want daar zit de energie. Vet levert ongeveer 9 kcal per gram "
                "tegenover 4 voor suiker, en daarom slaat het lichaam zijn reserve als vet op en "
                "niet als glycogeen.",
            ],
        ),
        dict(
            aanpak="Een eiwit heeft vier niveaus van structuur, en ze bouwen op elkaar: de "
                   "volgorde, de plaatselijke vorm (helix of plaat), de vouw van de hele keten, en "
                   "het samengaan van meerdere ketens. Alles wat die vouw stuk maakt, maakt het "
                   "eiwit onbruikbaar.",
            waarom=[
                "Onthoud de vier in die orde, want ze volgen uit elkaar: de primaire structuur "
                "bepaalt de secundaire, die de tertiaire, en die eventueel de quaternaire.",
                "Hemoglobine is het vaste voorbeeld van een quaternaire structuur: vier ketens "
                "samen. Daarom heeft één fout aminozuur er zulke grote gevolgen.",
                None,
                "Noem beide groepen bij naam en zeg wat verschilt: de restgroep. Juist die "
                "restgroep maakt het verschil tussen de twintig aminozuren, en dus tussen alle "
                "eiwitten.",
                "Dit sluit aan bij de bundel over enzymen: denatureren is de vouw verliezen, en de "
                "actieve plaats bestaat dan niet meer. De volgorde van de aminozuren is nog wel "
                "intact, en dat laat zien dat de volgorde alleen niet volstaat.",
                "Noem de keten van drie: volgorde, vouw, werking. Sikkelcelanemie is er het "
                "bekendste voorbeeld van.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-en-duurzaam-werken-in-het-labo-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De pictogrammen zijn beelden die zeggen wat er kan gebeuren. Vlam is brand, "
                   "doodshoofd is giftig, de inwerkende vloeistof is bijtend, het uitroepteken is "
                   "de lichtste waarschuwing, boom en vis gaan over het milieu, en een vlam boven "
                   "een cirkel betekent dat de stof brand aanwakkert.",
            waarom=[
                None,
                "Houd de vlam en de vlam boven een cirkel uit elkaar: het eerste brandt zelf, het "
                "tweede brandt niet maar laat iets anders veel heviger branden. Zuurstof en "
                "waterstofperoxide zijn oxiderend.",
                "Niet waar. Een pictogram staat er pas vanaf een bepaalde drempel, en ook stoffen "
                "zonder teken lees je eerst op het etiket. Er staat ook niets op over wat er "
                "gebeurt als je twee producten mengt.",
            ],
        ),
        dict(
            aanpak="Twee begrippen die bij een instrument horen: het meetbereik is van waar tot "
                   "waar het meet, de resolutie is het kleinste verschil dat het nog ziet. Kies "
                   "altijd het instrument waarvan het bereik net groot genoeg is, want dan is de "
                   "verdeling het fijnst.",
            waarom=[
                None,
                None,
                "Dit is de kernvraag van de reeks. Noem de fijnere verdeling als reden: 2 ml "
                "afmeten in een beker van 500 ml is onmogelijk nauwkeurig, want één streepje is "
                "daar al tientallen milliliter.",
                "Noem er drie van verschillende soort: iets over hoe je kijkt, iets over wat je "
                "opschrijft, en iets over herhalen. Recht van voren aflezen voorkomt een "
                "parallaxfout, en herhalen maakt een toevallige afwijking zichtbaar.",
            ],
        ),
        dict(
            aanpak="Bij elke handeling hoort dezelfde vraag: wat kan hier misgaan, en wie of wat "
                   "loopt er schade op? Zeg bij goed of fout dus altijd kort waarom, want dat is "
                   "wat de oefening vraagt.",
            waarom=[
                "Met de mond pipetteren is de ernstigste fout van de drie, want je kan het product "
                "zo binnenkrijgen. Daar bestaat een pipetballon voor, en die gebruik je altijd.",
                "De grove stelschroef bij de grootste vergroting is de klassieke fout waarmee elk "
                "jaar preparaten en lenzen sneuvelen, en de volgende vraag legt uit waarom.",
                "Noem het voordeel van het overzicht: met het kleinste objectief zoek je eerst wat "
                "je wil zien, en dan zoom je in. Omgekeerd beginnen kost veel meer tijd.",
                "Noem de afstand tussen de lens en het glaasje, want dat is de reden. Bij de "
                "grootste vergroting is die afstand kleiner dan een millimeter.",
            ],
        ),
        dict(
            aanpak="Vier situaties die om een handeling vragen. Houd overal dezelfde orde aan: "
                   "eerst het gevaar wegnemen of jezelf veilig stellen, dan verwittigen, dan "
                   "opruimen. Alleen bij een spat in het oog komt het spoelen altijd eerst.",
            waarom=[
                "Noem de drie stappen in die orde. Scherven met de handen oppakken is de fout die "
                "het vaakst gemaakt wordt, en glas met een chemisch product erop hoort in de "
                "scherfbak en niet bij het gewone afval.",
                "Bij het oog gaat spoelen vóór verwittigen, want elke seconde telt. Spoel lang, "
                "minstens een kwartier, en hou het oog daarbij open.",
                "Noem de besmetting van de voorraadfles, want dat is de reden. Een fles waar iets "
                "in teruggegoten is, is voor iedereen na jou onbruikbaar.",
                "Noem de weg waarlangs het binnenkomt: via je handen of een spat op je eten. "
                "Daarom is handen wassen bij het verlaten van een labo even belangrijk als bij het "
                "binnenkomen.",
            ],
        ),
        dict(
            aanpak="Duurzaam en veilig werken komen in deze reeks samen: minder product betekent "
                   "minder afval en minder risico. Houd daarnaast de twee woorden rond kiemvrij "
                   "maken vast: steriliseren is wat je doet, de autoclaaf is het toestel.",
            waarom=[
                None,
                "Een autoclaaf werkt met stoom onder druk, zodat de temperatuur boven 120 graden "
                "komt. Daarom doodt hij ook sporen, en dat lukt met koken alleen niet.",
                "Noem beide gevolgen: het milieu en de buizen. Chemisch afval hoort in de daarvoor "
                "bestemde recipiënten, met het etiket erop.",
                "Noem er drie van verschillende soort: iets over afmeten, iets over energie en iets "
                "over afval. Niet meer afmeten dan nodig is de goedkoopste en de effectiefste.",
                "Dit is het besluit van de hele bundel. Noem het verband: minder stof in huis is "
                "minder stof dat kan morsen of ontsnappen. Veilig en duurzaam zijn hier geen twee "
                "doelen maar één.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De zes stappen staan altijd in dezelfde orde: vraag, hypothese, plan, "
                   "uitvoeren, verwerken, besluiten. Onthoud dat de hypothese vóór de proef komt, "
                   "want een verwachting die je achteraf opschrijft, is geen hypothese.",
            waarom=[
                "De hypothese komt op plaats twee en niet later. Dat is geen formaliteit: wie "
                "pas na de meting een verwachting formuleert, kan zijn eigen resultaat niet meer "
                "toetsen.",
                "Let op het verschil tussen stap 5 en 6: verwerken is wat de cijfers zeggen, "
                "besluiten is wat dat betekent voor je vraag. Een grafiek is nog geen besluit.",
            ],
        ),
        dict(
            aanpak="Bij elke proef zijn er drie soorten variabelen. De onafhankelijke verander je "
                   "zelf, de afhankelijke meet je, en de constante houd je opzettelijk gelijk. "
                   "Vraag je dus: verander ik dit, meet ik dit, of hou ik dit gelijk?",
            waarom=[
                "Onthoud de twee met hun rol: de onafhankelijke is je oorzaak, de afhankelijke je "
                "gevolg. In een grafiek staat de onafhankelijke altijd op de horizontale as.",
                "Merk op dat er maar één onafhankelijke variabele mag zijn. Alles wat je niet "
                "onderzoekt, moet constant blijven, en dat is precies wat er in de volgende reeks "
                "misgaat.",
                "De controlegroep is nodig om te weten wat er zou gebeuren zonder je ingreep. "
                "Zonder vergelijkingspunt zegt een resultaat niets.",
            ],
        ),
        dict(
            aanpak="Zoek bij elke opstelling de fout in de methode, niet in het resultaat. De drie "
                   "klassieke fouten zijn: twee factoren tegelijk veranderen, te weinig metingen "
                   "doen, en een meting weglaten die niet past.",
            waarom=[
                "Noem allebei de factoren die verschillen, want daar zit de fout. De oplossing "
                "staat in het antwoord: beide reeksen op dezelfde plaats, en enkel de meststof "
                "verschilt.",
                "Noem het woord herhalen en het gemiddelde. Eén meting kan een uitzondering zijn, "
                "en je hebt geen manier om dat te weten.",
                "Dit is geen methodefout maar een eerlijkheidsfout, en die is de ernstigste. Een "
                "afwijkende meting noteer je en bespreek je; weglaten wat niet past, is het "
                "resultaat maken in plaats van meten.",
            ],
        ),
        dict(
            aanpak="Een grafiek heeft vaste regels: wat je zelf veranderde op de horizontale as, "
                   "elke as met grootheid, eenheid en een regelmatige verdeling, en een assenstelsel "
                   "dat het beeld niet vertekent. Kies de soort grafiek bij het soort gegeven.",
            waarom=[
                "Dit sluit aan bij de vorige reeks: op de horizontale as staat de onafhankelijke "
                "variabele, op de verticale de afhankelijke.",
                "Noem alle drie, want twee ervan vergeet men bijna altijd: de eenheid en de "
                "regelmatige verdeling. Een as met ongelijke stappen maakt elke lijn onbruikbaar.",
                "Een lijngrafiek past bij iets dat vloeiend in de tijd verandert; een staafdiagram "
                "bij losse categorieën en een cirkeldiagram bij delen van een geheel.",
                "Noem het woord vertekenen. Dit is ook de reden dat je een grafiek in het nieuws "
                "altijd eerst op zijn assen bekijkt.",
            ],
        ),
        dict(
            aanpak="Een besluit moet drie dingen bevatten: een antwoord op de vraag, iets over de "
                   "hypothese, en waarop je dat baseert. En let op twee valkuilen: een gemiddelde "
                   "zonder spreiding, en verband dat je voor oorzaak houdt.",
            waarom=[
                "Noem het woord spreiding. Twee reeksen met hetzelfde gemiddelde kunnen heel "
                "verschillend zijn, en daarom hoort er bij een gemiddelde altijd een idee van hoe "
                "ver de metingen uiteen liggen.",
                "Dit is het verschil tussen correlatie en oorzakelijkheid, en de derde factor is "
                "hier het warme weer. Noem die factor bij naam, want enkel zeggen dat het geen "
                "oorzaak is, verklaart niets.",
                "Noem alle drie, en vergeet het derde niet: waarop je je besluit baseert. Een "
                "besluit zonder verwijzing naar je eigen metingen is een mening.",
                "Niet waar, en dit is het belangrijkste punt van de hele bundel. Een weerlegde "
                "hypothese is een geslaagd onderzoek: je weet nu iets dat je eerst niet wist.",
            ],
        ),
        dict(
            aanpak="Ontwerpen werkt in een lus: eisen opstellen, prototype bouwen, testen, "
                   "aanpassen, opnieuw testen. Het verschil met onderzoeken zit in het doel: "
                   "onderzoek levert kennis op, een ontwerp levert iets dat werkt.",
            waarom=[
                "Beginnen met de eisen is wat ontwerpen van knutselen onderscheidt. Zonder eisen "
                "kan je achteraf niet zeggen of je oplossing goed is.",
                None,
                None,
                "Zet het verschil in het resultaat: kennis tegenover iets dat werkt. In een "
                "STEM-project zitten meestal beide, want je moet eerst iets uitzoeken voor je iets "
                "kan bouwen.",
                "Noem beide redenen: zonder beginmeting weet je niet waar de winst zit, en kan je "
                "achteraf niet bewijzen dat je iets verbeterd hebt. Dat heet een nulmeting.",
                "Noem de hele lus: aanpassen, opnieuw testen, en opnieuw naast alle eisen leggen. "
                "Een prototype dat niet voldoet, is geen mislukking maar de normale tussenstap.",
            ],
        ),
    ],
)
