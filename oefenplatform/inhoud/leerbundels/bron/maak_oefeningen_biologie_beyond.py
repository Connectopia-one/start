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
