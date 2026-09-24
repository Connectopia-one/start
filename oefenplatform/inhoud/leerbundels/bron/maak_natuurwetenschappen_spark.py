# -*- coding: utf-8 -*-
"""De leerbundels voor natuurwetenschappen op ✨ Spark-niveau.

Gebaseerd op de vakfiche natuurwetenschappen 1ste graad A-stroom (geldig 2027).
Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met moeilijkere vragen. Kim uploadt de
bundel dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/natuurwetenschappen.json`
doet daar het voorwerk voor.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Natuurwetenschappen"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────────────────────── 1. Cellen, weefsels en organen
BUNDELS["cellen-weefsels-en-organen"] = dict(
    vak=VAK, niveau=SPARK, titel="Cellen, weefsels en organen",
    onder="Hoe een levend wezen opgebouwd is, van celonderdeel tot organisme.",
    secties=[
        dict(kop="De cel is de basiseenheid", blokken=[
            ("p", "Alles wat leeft, is opgebouwd uit <strong>cellen</strong>. Een mens, een eik, een "
                  "regenworm, een bacterie: allemaal cellen. De cel is de kleinste eenheid die nog leeft, "
                  "en daarom noemen we haar de <strong>basiseenheid</strong> van het leven."),
            ("p", "Een <strong>eencellig organisme</strong> bestaat uit één enkele cel. Die ene cel doet "
                  "alles zelf: voeding opnemen, energie maken, afval kwijtraken, zich voortplanten. Een "
                  "bacterie is daar het bekendste voorbeeld van. Een <strong>meercellig organisme</strong> "
                  "zoals een mens of een plant bestaat uit miljarden cellen die elk een eigen taak hebben."),
            ("kader", "Doet elke cel van een meercellig organisme hetzelfde? Nee. De cellen zijn "
                      "<strong>gespecialiseerd</strong>: een zenuwcel geeft signalen door, een rode bloedcel "
                      "vervoert zuurstof, een spiercel kan samentrekken. Net door die taakverdeling kan een "
                      "meercellig organisme veel meer dan een eencellige."),
        ]),
        dict(kop="In de cel: de celonderdelen", blokken=[
            ("p", "In elke cel zitten <strong>celonderdelen</strong>, ook wel celorganellen genoemd. Ze "
                  "hebben elk hun eigen functie, en samen houden ze de cel aan het werk."),
            ("fig", svg.twee_cellen(),
             "Celmembraan, celkern, cytoplasma en mitochondriën heeft elke cel. Celwand, bladgroenkorrels en de grote vacuole enkel de plantaardige."),
            ("fig", tabel(["celonderdeel", "wat doet het?"], [
                ["<strong>celkern</strong>", "bewaart de erfelijke informatie en stuurt de cel aan"],
                ["<strong>celmembraan</strong>", "het vlies rond de cel; regelt wat er in en uit gaat"],
                ["<strong>cytoplasma</strong>", "de gelei-achtige vloeistof in de cel waarin de celonderdelen liggen"],
                ["<strong>mitochondrion</strong>", "maakt energie vrij uit glucose: de celademhaling"],
                ["<strong>celwand</strong>", "enkel bij planten; geeft stevigheid en bescherming"],
                ["<strong>bladgroenkorrel</strong>", "enkel bij planten; vangt zonlicht op voor de fotosynthese"],
                ["<strong>vacuole</strong>", "slaat water en voedingsstoffen op; houdt de cel stevig"],
            ]), "Het meervoud van mitochondrion is mitochondriën. Een bladgroenkorrel heet ook een chloroplast."),
            ("p", "Het <strong>celmembraan</strong> laat niet zomaar alles door. Het is <em>selectief</em>: "
                  "sommige stoffen mogen binnen, andere blijven buiten. Zo houdt de cel haar samenstelling "
                  "in de hand."),
            ("p", "De <strong>celkern</strong> bewaart het erfelijk materiaal. Zou een cel haar kern "
                  "verliezen, dan verliest ze die informatie en kan ze zich ook niet meer delen."),
            ("weetje", "Mitochondriën worden de energiecentrales van de cel genoemd. Een spiercel heeft er "
                       "veel meer dan een huidcel: een spier moet veel energie hebben om samen te trekken, "
                       "en die energie komt uit de verbranding van glucose."),
        ]),
        dict(kop="Plantaardig of dierlijk?", blokken=[
            ("p", "Een plantaardige en een dierlijke cel lijken sterk op elkaar. Celkern, celmembraan, "
                  "cytoplasma en mitochondriën vind je in allebei. Drie dingen zijn typisch plantaardig: "
                  "de <strong>celwand</strong>, de <strong>bladgroenkorrels</strong> en één grote "
                  "<strong>vacuole</strong>. Een dierlijke cel heeft geen celwand en is daardoor buigzamer "
                  "van vorm."),
            ("p", "De celwand is gemaakt van cellulose en ligt rond het celmembraan. Hij is stevig, maar "
                  "laat water en opgeloste stoffen door. Dáárom staat een boom rechtop zonder skelet: "
                  "miljoenen stevige cellen dragen samen de hele boom. Een dier lost dat anders op, met "
                  "beenderen."),
            ("kader", "Een plant die te weinig water krijgt, gaat <strong>slap hangen</strong>. De "
                      "verklaring zit in de vacuole: een volle vacuole duwt de cel van binnenuit tegen de "
                      "celwand en houdt de plant stevig. Loopt ze leeg, dan verdwijnt die druk."),
            ("p", "Bladgroenkorrels werken alleen met licht. Een cel uit de <strong>wortel</strong> heeft er "
                  "dus geen: in de donkere bodem zou fotosynthese geen zin hebben. Een cel uit een "
                  "<strong>blad</strong> zit er net vol mee. Zie je onder de microscoop een cel met een "
                  "celwand, een grote vacuole én groene korrels, dan kijk je naar een bladcel."),
            ("p", "En ja, een plantencel heeft zowel bladgroenkorrels als mitochondriën. Ze maakt suikers "
                  "met haar bladgroenkorrels en verbrandt een deel van die suikers weer met haar "
                  "mitochondriën. Een plant ademt dus ook."),
        ]),
        dict(kop="Van cel tot organisme: de organisatieniveaus", blokken=[
            ("p", "Cellen staan niet los van elkaar. Ze werken samen in steeds grotere gehelen. Die trapjes "
                  "heten de <strong>organisatieniveaus</strong>, en je moet ze kunnen rangschikken volgens "
                  "toenemende of afnemende complexiteit."),
            ("fig", svg.stappen(["cellen", "weefsels", "organen", "stelsels", "organisme"]),
             "Vóór de cel komen nog de celonderdelen: de volledige rij is celonderdelen, cellen, weefsels, organen, stelsels, organisme. Van groot naar klein lees je ze gewoon achterstevoren."),
            ("p", "Een <strong>weefsel</strong> is een groep cellen van dezelfde soort die samen één taak "
                  "doen. Een <strong>orgaan</strong> bestaat uit verschillende weefsels samen. En "
                  "verschillende organen die samen één grote taak doen, vormen een "
                  "<strong>stelsel</strong> of orgaanstelsel."),
            ("fig", tabel(["niveau", "bij mens en dier", "bij planten"], [
                ["weefsel", "spierweefsel, zenuwweefsel, huidweefsel", "dekweefsel, transportweefsel"],
                ["orgaan", "maag, hart, longen, huid, nieren", "wortel, stengel, blad, bloem"],
                ["stelsel", "spijsverterings-, ademhalings-, transport-, uitscheidings-, voortplantings-, beender-, spier- en zenuwstelsel",
                 "transportstelsel en voortplantingsstelsel"],
            ]), "Een plant heeft geen longen, geen zenuwen en geen skelet: zij heeft maar twee stelsels."),
            ("p", "Het <strong>hart</strong> is dus geen weefsel maar een orgaan: er zitten spierweefsel, "
                  "zenuwweefsel en bloedvaten in. Hetzelfde geldt voor de maag, met haar spierweefsel om te "
                  "kneden, haar slijmvlies aan de binnenkant en haar zenuwweefsel dat alles aanstuurt. Het "
                  "<strong>transportweefsel</strong> van een plant loopt dan weer als buisjes door wortel, "
                  "stengel en blad en vervoert water en suikers; het <strong>dekweefsel</strong> is de "
                  "beschermlaag aan de buitenkant."),
            ("kader", "De stelsels werken ook onderling samen. Om zuurstof en voedingsstoffen tot in je "
                      "tenen te krijgen, heb je er drie tegelijk nodig: het "
                      "<strong>ademhalingsstelsel</strong> haalt de zuurstof binnen, het "
                      "<strong>spijsverteringsstelsel</strong> de voedingsstoffen, en het "
                      "<strong>transportstelsel</strong> brengt allebei tot bij elke cel. Het "
                      "<strong>beenderstelsel</strong> of skelet draagt ondertussen je lichaam, beschermt je "
                      "hersenen, hart en longen, en geeft je spieren een aanhechtingspunt."),
        ]),
        dict(kop="Cellen bekijken", blokken=[
            ("p", "Cellen zie je niet met het blote oog. Je kiest je hulpmiddel naar de vergroting die je "
                  "nodig hebt: een <strong>loep</strong> vergroot een paar keer, een "
                  "<strong>binoculair</strong> toont een insect in drie dimensies, en een "
                  "<strong>lichtmicroscoop</strong> vergroot honderden keren. Pas met die laatste zie je "
                  "afzonderlijke cellen, bijvoorbeeld in een dun velletje ui."),
            ("weetje", "Een loep volstaat niet om cellen te zien: ze vergroot gewoon te weinig. Dat is "
                       "precies wat 'het gepaste meetinstrument kiezen' betekent — te weinig nauwkeurig is "
                       "even onbruikbaar als helemaal niets."),
        ]),
    ],
    onthoud=[
        "De cel is de basiseenheid van het leven; een bacterie is eencellig, een mens meercellig.",
        "Van klein naar groot: celonderdelen, cellen, weefsels, organen, stelsels, organisme.",
        "Celkern, celmembraan, cytoplasma en mitochondriën heeft elke cel.",
        "Celwand, bladgroenkorrels en een grote vacuole heeft alleen de plantaardige cel.",
        "Een weefsel is een groep gelijke cellen; een orgaan bestaat uit verschillende weefsels.",
        "Cellen bekijk je met een lichtmicroscoop, niet met een loep.",
    ],
)

# ───────────────────────────────────────── 2. Fotosynthese en de plant
BUNDELS["fotosynthese-en-de-plant"] = dict(
    vak=VAK, niveau=SPARK, titel="Fotosynthese en de plant",
    onder="Hoe een plant met zonlicht haar eigen voedsel maakt, en waarom al het leven daarvan afhangt.",
    secties=[
        dict(kop="Wat gebeurt er bij fotosynthese?", blokken=[
            ("p", "Een plant maakt met behulp van <strong>zonlicht</strong> haar eigen suiker: "
                  "<strong>glucose</strong>. Daarvoor heeft ze twee grondstoffen nodig, "
                  "<strong>water</strong> (H₂O) en <strong>koolstofdioxide</strong> (CO₂), en ze houdt er "
                  "twee producten aan over: glucose (C₆H₁₂O₆) en <strong>zuurstofgas</strong> (O₂)."),
            ("fig", svg.fotosynthese(),
             "Wat er in gaat en wat er uit komt. Let op de richting van de pijlen: CO₂ en water in, zuurstofgas en glucose uit."),
            ("p", "Er gebeuren drie dingen tegelijk. Een <strong>energieomzetting</strong>: de "
                  "stralingsenergie van de zon, ook lichtenergie genoemd, wordt vastgelegd als "
                  "<strong>chemische energie</strong> in de glucose. Een <strong>stofomzetting</strong>: "
                  "koolstofdioxide en water worden glucose en zuurstofgas. En een "
                  "<strong>stofuitwisseling</strong> met de omgeving: er gaat CO₂ en water in, en er komt "
                  "zuurstofgas uit. Bij de <strong>opname en afgifte</strong> van stoffen spelen de "
                  "wortels (water) en de huidmondjes (CO₂ in, O₂ en waterdamp uit) de hoofdrol."),
            ("kader", "Glucose is een <strong>energierijke stof</strong>. De energie van het zonlicht zit "
                      "opgeslagen in de bindingen van dat molecule. Verbrandt een cel die suiker later met "
                      "zuurstof, dan komt die energie bij die <strong>verbranding</strong> weer vrij."),
            ("p", "Zonder licht valt alles stil. <strong>Bladgroen</strong> vangt het licht op; zonder "
                  "bladgroen en zonder licht is er geen fotosynthese. Een witte plek op een bontgekleurd "
                  "blad maakt dus geen suiker."),
        ]),
        dict(kop="Welke plantendelen doen mee?", blokken=[
            ("fig", svg.plantdelen(), "De vier organen van een plant: wortel, stengel, blad en bloem."),
            ("p", "De fotosynthese gebeurt vooral in het <strong>blad</strong>: dat ligt breed uitgespreid "
                  "in het licht en zit vol <strong>bladgroenkorrels</strong>. Die korrels zijn "
                  "celonderdelen: ze liggen in het cytoplasma van de bladcellen, dus je hebt een microscoop "
                  "nodig om ze te zien."),
            ("p", "De <strong>huidmondjes</strong> zijn kleine openingen in het blad, vooral aan de "
                  "onderkant. Ze laten koolstofdioxide binnen en zuurstofgas en waterdamp naar buiten. Dat "
                  "ze aan de onderkant zitten, is geen toeval: daar is het koeler en schaduwrijker, dus "
                  "verliest de plant minder water dan in de volle zon aan de bovenkant. Bij droogte gaan de "
                  "twee sluitcellen rond zo'n spleetje gewoon dicht."),
            ("p", "De <strong>wortels</strong> nemen water en opgeloste mineralen op uit de bodem. De "
                  "<strong>stengel</strong> houdt de bladeren in het licht en bevat het transportweefsel."),
            ("fig", svg.stappen(["water: wortel → stengel|→ blad", "glucose: blad →|stengel → wortel"],
                                breedte=420),
             "Water gaat omhoog en wordt gebruikt of verdampt via de huidmondjes. De suikers gaan de andere kant op, naar alle delen die zelf geen fotosynthese doen: wortels, bloemen en vruchten."),
            ("weetje", "Plak je de onderkant van alle bladeren af, zodat de huidmondjes dicht zitten, dan "
                       "groeit de plant trager. De deur voor de gassen zit dicht, dus de aanvoer van "
                       "koolstofdioxide stokt en de fotosynthese valt grotendeels stil."),
        ]),
        dict(kop="Autotroof en heterotroof", blokken=[
            ("p", "Een <strong>autotroof</strong> organisme maakt zijn eigen energierijke stoffen. "
                  "Autotroof betekent letterlijk 'zichzelf voedend': planten, algen en sommige bacteriën "
                  "horen erbij. In een voedselketen zijn zij de <strong>producenten</strong> waar alles mee "
                  "begint."),
            ("p", "Een <strong>heterotroof</strong> organisme moet zijn energierijke stoffen uit ander "
                  "materiaal halen. Een koe, een mens en ook een paddenstoel of een schimmel zijn "
                  "heterotroof. Let op: ook een autotroof organisme heeft energie nodig; het haalt ze "
                  "alleen rechtstreeks uit het licht."),
            ("kader", "De energie in het vlees dat je eet, komt oorspronkelijk van de zon. Het dier at "
                      "planten (of dieren die planten aten), en die planten legden zonne-energie vast in "
                      "suikers. Zo goed als alle energie in ons voedsel begint bij de fotosynthese."),
        ]),
        dict(kop="Wat doet de plant met haar glucose?", blokken=[
            ("p", "Drie dingen. Een deel <strong>verbrandt</strong> ze zelf voor energie. Een deel bouwt ze "
                  "om tot cellulose, de <strong>bouwstof</strong> van haar celwanden. En de rest bewaart ze "
                  "als <strong>zetmeel</strong>, een reservestof."),
            ("p", "Zetmeel slaat de plant op in bladeren, knollen of zaden. Een <strong>aardappel</strong> "
                  "is zo'n knol: een ondergrondse voorraadkast. De bladeren maakten de glucose, de plant "
                  "sloeg ze als zetmeel op om later weer uit te lopen."),
            ("p", "Naast water en CO₂ heeft een plant ook <strong>mineralen</strong> uit de bodem nodig, "
                  "zoals stikstof. Die komen mee met het water dat de wortels opnemen. Zonder mineralen "
                  "blijft een plant klein en verkleuren haar bladeren."),
            ("p", "Fotosynthese is dus in de eerste plaats belangrijk voor de plant zélf: ze levert de "
                  "energierijke stoffen om te groeien en te leven."),
        ]),
        dict(kop="Fotosynthese en celademhaling", blokken=[
            ("p", "De twee zijn elkaars omgekeerde. Bij de <strong>fotosynthese</strong> wordt energie "
                  "vastgelegd, bij de <strong>celademhaling</strong> wordt ze weer vrijgemaakt."),
            ("fig", tabel(["", "fotosynthese", "celademhaling"], [
                ["gaat in", "koolstofdioxide + water", "glucose + zuurstofgas"],
                ["komt uit", "glucose + zuurstofgas", "koolstofdioxide + water"],
                ["energie", "wordt vastgelegd (licht nodig)", "komt vrij"],
                ["wie", "alleen planten en andere autotrofen", "planten, dieren en de mens"],
                ["wanneer", "alleen met licht", "dag en nacht"],
            ]), "Een plant doet ze allebei; een dier alleen de celademhaling."),
            ("p", "Overdag maakt een plant méér zuurstof dan ze verbruikt. <strong>'s Nachts</strong> ligt "
                  "de fotosynthese stil en blijft alleen de celademhaling over: dan verbruikt ze zuurstof "
                  "en geeft ze koolstofdioxide af. Een plant geeft bij de fotosynthese dus geen "
                  "koolstofdioxide af — daar verbruikt ze het net."),
            ("weetje", "Zet je een plant in een donkere kast, dan worden haar bladeren na een tijd geel. "
                       "Zonder licht stopt de fotosynthese, teert de plant in op haar reserves en breekt ze "
                       "het bladgroen af."),
        ]),
        dict(kop="Waarom het voor iedereen belangrijk is", blokken=[
            ("p", "Voor <strong>mens en dier</strong>: alle voedsel begint bij planten, en de zuurstof die "
                  "wij inademen komt van de fotosynthese. Zonder fotosynthese is er op aarde geen leven "
                  "zoals wij het kennen."),
            ("p", "Voor het <strong>klimaat</strong>: koolstofdioxide is een <strong>broeikasgas</strong>. "
                  "Planten halen het uit de lucht, en daarom helpen bossen tegen de "
                  "<strong>klimaatverandering</strong>. <strong>Ontbossing</strong> doet het omgekeerde: "
                  "minder bomen betekent minder fotosynthese, dus minder opname van CO₂."),
            ("kader", "Een tuinder die zijn serre vol extra koolstofdioxide zet, doet dat om de groei aan "
                      "te jagen: CO₂ is een grondstof voor de fotosynthese, dus meer grondstof geeft meer "
                      "glucose — zolang licht en water niet tekortschieten."),
        ]),
    ],
    onthoud=[
        "Fotosynthese: koolstofdioxide + water → glucose + zuurstofgas, met licht als energiebron.",
        "Lichtenergie wordt chemische energie in de glucose.",
        "Wortels nemen water op, huidmondjes laten CO₂ binnen, bladgroenkorrels vangen het licht.",
        "Autotroof maakt zijn eigen voedsel (planten), heterotroof niet (dieren, schimmels, de mens).",
        "De plant gebruikt glucose als brandstof en bouwstof, en slaat de rest op als zetmeel.",
        "'s Nachts doet een plant alleen celademhaling: dan verbruikt ze zuurstof.",
    ],
)

# ───────────────────────────────────────── 3. Het menselijk lichaam
BUNDELS["het-menselijk-lichaam"] = dict(
    vak=VAK, niveau=SPARK, titel="Het menselijk lichaam",
    onder="Vier stelsels die samenwerken om elke cel van energie en materie te voorzien.",
    secties=[
        dict(kop="Waarom je voedsel en zuurstof nodig hebt", blokken=[
            ("p", "Mensen en andere dierlijke organismen hebben <strong>energie en materie</strong> nodig "
                  "om te functioneren. Die halen ze uit hun voedsel en uit de lucht. "
                  "<strong>Voedingsstoffen</strong> hebben daarbij drie functies."),
            ("fig", tabel(["functie", "waarvoor", "waarin"], [
                ["<strong>brandstof</strong>", "energie leveren", "suikers en vetten"],
                ["<strong>bouwstof</strong>", "groeien en herstellen", "eiwitten"],
                ["<strong>beschermstof</strong>", "je lichaam goed laten werken", "vitaminen en mineralen"],
            ]), "Water is ook een voedingsstof. Het levert geen energie, maar is even onmisbaar: het vervoert stoffen, regelt je temperatuur en voert afval af."),
            ("p", "<strong>Voedingsvezels</strong> uit groenten, fruit en volkoren producten worden niet "
                  "verteerd. Ze geven je darmen werk en houden je stoelgang vlot. Een "
                  "<strong>voedingsmiddel</strong> (een appel, een boterham) is trouwens iets anders dan "
                  "een voedingsstof: het voedingsmiddel is wat je eet, de voedingsstoffen zijn wat erin zit."),
        ]),
        dict(kop="Het spijsverteringsstelsel", blokken=[
            ("fig", svg.stappen(["mond", "slokdarm", "maag", "dunne|darm", "dikke|darm"]),
             "Tussen mond en slokdarm ligt de keel of keelholte; na de maag komt eerst de twaalfvingerige darm, en na de dikke darm volgen de endeldarm en de aars."),
            ("p", "In de <strong>mond</strong> wordt het voedsel fijngekauwd en gemengd met "
                  "<strong>speeksel</strong> uit de <strong>speekselklieren</strong>. Dat maakt het glad "
                  "en begint zetmeel al af te breken, nog voor je geslikt hebt. De <strong>maag</strong> "
                  "maakt <strong>maagsap</strong>: dat bevat zuur, doodt bacteriën en begint met het "
                  "afbreken van eiwitten."),
            ("p", "De <strong>lever</strong> maakt <strong>gal</strong>, dat in de "
                  "<strong>galblaas</strong> bewaard wordt. In de twaalfvingerige darm verdeelt gal de "
                  "vetten in heel kleine druppeltjes, zodat de verteringssappen er beter bij kunnen. De "
                  "<strong>alvleesklier</strong> levert <strong>alvleessap</strong>, de darmwand zelf "
                  "<strong>darmsap</strong>."),
            ("fig", tabel(["voedingsstof", "wordt omgezet in", "waar vooral"], [
                ["eiwitten", "aminozuren", "maag en dunne darm"],
                ["suikers zoals zetmeel", "glucose, fructose en/of galactose", "mond en dunne darm"],
                ["vetten", "glycerol en 3 vetzuren", "dunne darm, met hulp van gal"],
            ]), "Dat zijn de stofomzettingen van de spijsvertering: grote moleculen worden klein genoeg om door de darmwand te raken."),
            ("p", "In de <strong>dunne darm</strong> is de vertering klaar en gaan de verteerde "
                  "voedingsstoffen het bloed in. Dat opnemen heet <strong>absorptie</strong>, en het "
                  "gebeurt door de darmvlokken, die het oppervlak van de darm enorm groot maken. De "
                  "<strong>dikke darm</strong> haalt daarna vooral water uit wat overblijft. Wat niet "
                  "verteerd of opgenomen is, verlaat je lichaam als <strong>voedselresten</strong> via de "
                  "<strong>endeldarm</strong> en de <strong>aars</strong>."),
        ]),
        dict(kop="Het ademhalingsstelsel", blokken=[
            ("p", "Lucht komt binnen langs de <strong>neus</strong> of de mond, gaat door de keelholte, "
                  "langs de <strong>strottenklep</strong>, door de <strong>luchtpijp</strong> en de "
                  "<strong>luchtpijptakken</strong> naar de <strong>longen</strong>, tot in de "
                  "<strong>longblaasjes</strong>."),
            ("p", "De longblaasjes zijn piepkleine blaasjes met een heel dunne wand, omringd door "
                  "haarvaten. Daar gebeurt de stofuitwisseling: <strong>zuurstof</strong> gaat naar het "
                  "bloed en <strong>koolstofdioxide</strong> komt eruit. Koolstofdioxide en waterdamp zijn "
                  "je <strong>ademhalingsproducten</strong>."),
            ("kader", "Het <strong>middenrif</strong> is de platte spier onder de longen. Trekt die samen, "
                      "dan wordt de borstkas groter en stroomt er lucht naar binnen. De "
                      "<strong>strottenklep</strong> klapt bij het slikken over de luchtpijp, zodat voedsel "
                      "in de slokdarm gaat. Lukt dat niet, dan schiet je in je verkeerde keelgat."),
        ]),
        dict(kop="Het transportstelsel", blokken=[
            ("p", "Het hart pompt het bloed rond. Het heeft <strong>vier holtes</strong>: een linker- en "
                  "een rechterboezem, en een linker- en een rechterkamer. De boezems vangen het bloed op, "
                  "de kamers pompen het weg."),
            ("fig", svg.bloedsomloop(),
             "De kleine bloedsomloop gaat van het hart naar de longen en terug; de grote gaat van het hart naar de rest van het lichaam en terug."),
            ("p", "<strong>Slagaders</strong> voeren bloed wég van het hart en hebben een dikke, gespierde "
                  "wand. <strong>Aders</strong> brengen het terug en hebben kleppen die terugstromen "
                  "tegengaan. De <strong>haarvaten</strong> ertussen zijn de allerdunste bloedvaten, met "
                  "een wand van één cellaag: juist daardoor kunnen zuurstof, voedingsstoffen en "
                  "afvalstoffen erdoor naar de cellen en terug."),
            ("p", "De grootste slagader is de <strong>aorta</strong>, die uit de linkerkamer vertrekt met "
                  "zuurstofrijk bloed. De <strong>holle aders</strong> brengen het zuurstofarme bloed terug "
                  "naar de rechterboezem. Van daar gaat het via de <strong>longslagader</strong> naar de "
                  "longen en komt het als zuurstofrijk bloed via de <strong>longader</strong> terug. De "
                  "<strong>kransslagaders</strong> voeden ondertussen de hartspier zelf."),
            ("weetje", "In de longslagader stroomt <em>zuurstofarm</em> bloed. Een slagader heet zo omdat "
                       "ze van het hart wegvoert, niet omdat er zuurstofrijk bloed in zit."),
            ("fig", tabel(["bestanddeel van het bloed", "functie"], [
                ["plasma", "de vloeistof; vervoert opgeloste stoffen"],
                ["rode bloedcellen", "vervoeren zuurstof"],
                ["witte bloedcellen", "bestrijden ziektekiemen"],
                ["bloedplaatjes", "laten een wonde stollen"],
            ]), "Zonder bloedplaatjes zou een kleine snee blijven bloeden."),
        ]),
        dict(kop="Het uitscheidingsstelsel", blokken=[
            ("p", "Afvalstoffen moeten weg. Het <strong>orgaan</strong> dat urine maakt, is de nier. De "
                  "<strong>nieren</strong> filteren afvalstoffen uit het bloed en maken "
                  "er <strong>urine</strong> van; dat is een <strong>uitscheidingsproduct</strong>. Elke "
                  "nier heeft een <strong>urineleider</strong> naar de <strong>blaas</strong>, die de urine "
                  "alleen bewaart, en van de blaas naar buiten loopt één <strong>urinebuis</strong>."),
            ("p", "Een nier bestaat van buiten naar binnen uit het <strong>kapsel</strong>, de "
                  "<strong>schors</strong>, het <strong>merg</strong> met zijn <strong>piramides</strong>, "
                  "en het <strong>nierbekken</strong>, waar de urine samenkomt."),
            ("p", "Ook de <strong>zweetklieren</strong> (zweet), de <strong>longen</strong> "
                  "(koolstofdioxide en waterdamp) en de <strong>lever</strong> horen bij de uitscheiding. "
                  "Voedselresten zijn iets anders: die zijn nooit in je bloed geweest."),
        ]),
        dict(kop="Celademhaling: waar het allemaal voor dient", blokken=[
            ("p", "In élke cel, in de <strong>mitochondriën</strong>, gebeurt de "
                  "<strong>celademhaling</strong> of de verbranding van glucose: "
                  "<strong>glucose + zuurstofgas → koolstofdioxide + water + energie</strong>. Die energie "
                  "gebruikt de cel om te werken; de rest gaat verloren als warmte."),
            ("kader", "Celademhaling gebeurt dus niet in de longen. De longen zorgen alleen voor de aanvoer "
                      "van zuurstof en de afvoer van koolstofdioxide."),
            ("p", "Om één spiercel aan het werk te houden, moeten drie stelsels samenwerken: het "
                  "ademhalingsstelsel levert de zuurstof, het spijsverteringsstelsel de glucose, en het "
                  "transportstelsel brengt allebei tot bij de cel — en voert het afval weer af. Loop je "
                  "hard, dan hebben je spiercellen meer van allebei nodig en moet het afval sneller weg: "
                  "daarom ga je sneller ademen én klopt je hart sneller."),
        ]),
        dict(kop="Gezond eten en bewegen", blokken=[
            ("p", "Met de <strong>actieve voedings- en bewegingsdriehoek</strong> beoordeel je een eet- en "
                  "bewegingspatroon. Onderaan, in het donkergroene deel, staan <strong>water, groenten, "
                  "fruit en volle granen</strong>: daar eet je het meest van. Hoe hoger je komt, hoe minder "
                  "je er best van eet. In de <strong>rode bol</strong> staat wat je best vermijdt, zoals "
                  "sterk bewerkte voeding en frisdrank — en bij bewegen: <strong>lang stilzitten</strong>."),
            ("p", "Een patroon gezonder maken doe je met concrete aanpassingen: meer groenten en fruit, "
                  "water drinken in plaats van frisdrank, en elke dag bewegen. Lang stilzitten is ongezond, "
                  "ook als je daarnaast sport, dus sta regelmatig even recht."),
        ]),
    ],
    onthoud=[
        "Voedingsstoffen zijn brandstof, bouwstof of beschermstof.",
        "Eiwitten → aminozuren, zetmeel → glucose, vetten → glycerol en 3 vetzuren.",
        "De dunne darm neemt de voedingsstoffen op in het bloed: dat is de absorptie.",
        "Het hart heeft twee boezems en twee kamers; slagaders gaan weg van het hart, aders ernaartoe.",
        "Bloed bestaat uit plasma, rode bloedcellen, witte bloedcellen en bloedplaatjes.",
        "Celademhaling: glucose + zuurstofgas → koolstofdioxide + water + energie, in elke cel.",
    ],
)

# ───────────────────────────────────────── 4. Voortplanting
BUNDELS["voortplanting"] = dict(
    vak=VAK, niveau=SPARK, titel="Voortplanting",
    onder="Hoe planten, dieren en mensen voor nakomelingen zorgen.",
    secties=[
        dict(kop="Aseksueel of seksueel", blokken=[
            ("p", "Bij <strong>aseksuele</strong> of ongeslachtelijke voortplanting is er maar "
                  "<strong>één ouder</strong>: die maakt in feite een kopie van zichzelf. Bij "
                  "<strong>seksuele</strong> of geslachtelijke voortplanting versmelten er twee "
                  "<strong>geslachtscellen</strong> — een <strong>eicel</strong> en een "
                  "<strong>zaadcel</strong> — en komt er dus erfelijk materiaal van twee kanten."),
            ("fig", tabel(["", "aseksueel", "seksueel"], [
                ["ouders", "één", "twee (of twee geslachtscellen)"],
                ["nakomelingen", "erfelijk identiek aan de ouder", "allemaal verschillend"],
                ["voordeel", "snel, veel, geen partner nodig", "variatie: de soort past zich makkelijker aan"],
                ["nadeel", "één ziekte kan ze allemaal treffen", "trager, en je hebt een partner nodig"],
            ]), "Daarom houden kwekers een ras zuiver met stekken, en overleeft een soort in de natuur net dankzij de variatie."),
            ("weetje", "Bij <strong>maagdelijke voortplanting</strong> groeit er uit een onbevruchte eicel "
                       "tóch een nieuw individu. Bladluizen en sommige hagedissen doen dat. Het is een "
                       "vorm van aseksuele voortplanting: er komt geen zaadcel aan te pas."),
        ]),
        dict(kop="Planten zonder zaad", blokken=[
            ("p", "Planten hebben een hele reeks manieren om zich ongeslachtelijk voort te planten: "
                  "<strong>stekken</strong>, <strong>enten</strong>, <strong>oculeren</strong>, "
                  "<strong>scheuren</strong>, <strong>uitlopers</strong>, <strong>bollen</strong> en "
                  "<strong>knollen</strong>."),
            ("p", "Bij <strong>stekken</strong> snijd je een stukje stengel of blad af en laat je het "
                  "wortelen: daaruit groeit een volledige nieuwe plant, erfelijk identiek aan de "
                  "moederplant. Bij <strong>enten</strong> laat je een twijg van een goede soort vergroeien "
                  "met de stam van een andere; fruittelers doen dat om elk jaar dezelfde appels te oogsten. "
                  "Een tulp komt elk jaar terug uit haar <strong>bol</strong>, een aardappel uit haar "
                  "<strong>knol</strong>: ondergrondse voorraadkasten."),
            ("p", "Ook dieren kunnen het. Bij <strong>knopvorming</strong>, zoals bij gist, ontstaat er een "
                  "uitstulping aan de cel die als nieuw individu loskomt."),
        ]),
        dict(kop="De bloem: seksuele voortplanting bij planten", blokken=[
            ("fig", svg.bloemdoorsnede(),
             "Stempel, stijl en vruchtbeginsel vormen samen de stamper (vrouwelijk). Helmdraad en helmknop vormen de meeldraad (mannelijk)."),
            ("p", "De <strong>meeldraad</strong> bestaat uit een <strong>helmdraad</strong> met bovenaan "
                  "een <strong>helmknop</strong>, waarin het stuifmeel zit. De <strong>stamper</strong> "
                  "heeft bovenaan een kleverige <strong>stempel</strong>, daaronder de "
                  "<strong>stijl</strong> en onderaan het <strong>vruchtbeginsel</strong> met de "
                  "<strong>zaadbeginsels</strong>."),
            ("p", "Komt er stuifmeel op de stempel terecht, dan heet dat <strong>bestuiving</strong>. Pas "
                  "daarna kan de <strong>bevruchting</strong> volgen: de zaadcel raakt tot bij de eicel in "
                  "het zaadbeginsel en de twee versmelten tot één bevruchte eicel. Daaruit groeit een "
                  "zaadje met een <strong>kiemplant</strong>je en een voorraad voedsel erin. Bij genoeg "
                  "water en warmte kiemt dat en groeit er een nieuwe plant."),
            ("kader", "Waarom heeft gras geen opvallende bloemen? Omdat het "
                      "<strong>windbestuivend</strong> is: het moet geen insecten lokken met kleur, geur en "
                      "nectar, en maakt in de plaats daarvan enorm veel licht stuifmeel — waar "
                      "hooikoortspatiënten last van hebben."),
        ]),
        dict(kop="Het voortplantingsstelsel van de mens", blokken=[
            ("fig", tabel(["mannelijk", "vrouwelijk"], [
                ["teelballen: maken de zaadcellen", "eierstokken: hierin rijpen de eicellen"],
                ["bijballen: de zaadcellen rijpen er verder", "eileiders met eitrechters: vangen de eicel op"],
                ["zaadleiders: brengen ze naar de urinebuis", "baarmoeder en baarmoederhals"],
                ["prostaat en zaadblaasjes: maken het vocht", "vagina"],
                ["penis met eikel, voorhuid en zwellichamen; balzak", "clitoris en schaamlippen"],
            ]), "Sperma is het mengsel van zaadcellen en het vocht van de prostaat en de zaadblaasjes; dat vocht voedt en beschermt de zaadcellen."),
            ("p", "De <strong>primaire geslachtskenmerken</strong> zijn de geslachtsorganen zelf, waarmee "
                  "je geboren wordt. De <strong>secundaire geslachtskenmerken</strong> komen er in de "
                  "puberteit bij, door de <strong>geslachtshormonen</strong>: schaamhaar, een zwaardere "
                  "stem, bredere heupen, borstontwikkeling. De hormonen zijn "
                  "<strong>oestrogeen</strong>, <strong>progesteron</strong> en "
                  "<strong>testosteron</strong>."),
        ]),
        dict(kop="De menstruatiecyclus", blokken=[
            ("fig", svg.menstruatiecyclus(), "Eén cyclus, met de vier gebeurtenissen die je moet kunnen benoemen."),
            ("p", "Een cyclus duurt gemiddeld 28 dagen. De vier gebeurtenissen die je moet kunnen "
                  "benoemen zijn de <strong>eicelrijping</strong>, de <strong>verdikking</strong> van het "
                  "baarmoederslijmvlies, de <strong>eisprong</strong> en de "
                  "<strong>menstruatie</strong>."),
            ("p", "Tijdens een cyclus <strong>rijpt</strong> er een eicel in een eierstok en "
                  "<strong>verdikt</strong> het <strong>baarmoederslijmvlies</strong>, zodat het een "
                  "bevruchte eicel kan opvangen. Rond dag 14 volgt de <strong>eisprong</strong>: de rijpe "
                  "eicel komt vrij en wordt door de eitrechter opgevangen. Komt er geen bevruchting, dan "
                  "wordt het slijmvlies afgestoten: dat is de <strong>menstruatie</strong>, meteen dag 1 "
                  "van een nieuwe cyclus."),
            ("p", "De <strong>vruchtbare periode</strong> ligt rond de eisprong. Zaadcellen kunnen enkele "
                  "dagen overleven en de eicel ongeveer één dag, dus ze loopt van een paar dagen vóór tot "
                  "een dag na de eisprong."),
        ]),
        dict(kop="Van eisprong tot geboorte", blokken=[
            ("fig", svg.stappen(["eisprong", "geslachts-|gemeenschap", "bevruchting", "innesteling", "zwanger-|schap", "geboorte"]),
             "De fasen van de voortplanting in chronologische volgorde. Bij de geslachtsgemeenschap hoort de zaadlozing."),
            ("p", "De <strong>bevruchting</strong> gebeurt meestal in de <strong>eileider</strong>: de "
                  "zaadcellen zwemmen door de baarmoeder tot daar en één ervan versmelt met de eicel. De "
                  "<strong>bevruchte eicel</strong> reist naar de baarmoeder en nestelt zich in het "
                  "baarmoederslijmvlies: de <strong>innesteling</strong>."),
            ("p", "Daar, in de <strong>baarmoeder</strong>, groeit ze tijdens de <strong>zwangerschap</strong> "
                  "verder uit tot een baby. Ze deelt zich eerst tot een <strong>embryo</strong>. Vanaf ongeveer acht weken "
                  "spreken we van een <strong>foetus</strong>, en na ongeveer negen maanden volgt de "
                  "geboorte van de <strong>baby</strong>."),
        ]),
        dict(kop="Voorbehoedsmiddelen en soa's", blokken=[
            ("p", "<strong>Hormonale</strong> voorbehoedsmiddelen zijn de "
                  "<strong>anticonceptiepil</strong>, de <strong>anticonceptiepleister</strong>, de "
                  "<strong>vaginale ring</strong>, de <strong>prikpil</strong>, het "
                  "<strong>hormonenstaafje</strong> en het <strong>hormonenspiraaltje</strong>. De "
                  "hormonen houden de eisprong tegen — zonder eicel is er niets te bevruchten — en maken "
                  "het slijm in de baarmoederhals dikker, zodat zaadcellen moeilijker passeren."),
            ("p", "Niet-hormonaal zijn het <strong>koperspiraaltje</strong>, het "
                  "<strong>condoom</strong> en het <strong>vrouwencondoom</strong>."),
            ("kader", "Alleen een condoom of een vrouwencondoom beschermt óók tegen "
                      "<strong>soa's</strong>, want alleen die houden lichaamsvochten tegen. Hormonale "
                      "middelen en spiraaltjes voorkomen enkel een zwangerschap. Soa's geef je door bij "
                      "seksueel contact, en veel soa's geven in het begin geen enkele klacht — je ziet dus "
                      "niet aan iemand of die er een heeft."),
            ("p", "Een condoom gebruik je <strong>één keer</strong> en gooi je daarna weg. Hergebruik maakt "
                  "het onbetrouwbaar, zowel tegen zwangerschap als tegen soa's."),
        ]),
    ],
    onthoud=[
        "Aseksueel: één ouder, identieke nakomelingen. Seksueel: twee geslachtscellen, variatie.",
        "Stekken, enten, uitlopers, bollen en knollen zijn aseksueel; zaad ontstaat seksueel.",
        "Meeldraad = helmdraad + helmknop (mannelijk). Stamper = stempel + stijl + vruchtbeginsel.",
        "Bestuiving is stuifmeel op de stempel; bevruchting is het versmelten van zaadcel en eicel.",
        "Volgorde: eisprong, bevruchting in de eileider, innesteling, zwangerschap, geboorte.",
        "Alleen een condoom beschermt ook tegen soa's.",
    ],
)

# ───────────────────────────────────────── 5. Ecologie en biodiversiteit
BUNDELS["ecologie-en-biodiversiteit"] = dict(
    vak=VAK, niveau=SPARK, titel="Ecologie en biodiversiteit",
    onder="Hoe organismen samenhangen met elkaar en met hun omgeving, en wat de mens daarin verandert.",
    secties=[
        dict(kop="Biotoop, abiotisch en biotisch", blokken=[
            ("p", "Een <strong>biotoop</strong> is een plaats met haar eigen omstandigheden waar bepaalde "
                  "organismen leven: een bos, een weiland, een wetland, een moeras, een rivier, een "
                  "estuarium, zelfs een woonwijk. Een biotoop samen met alle organismen die erin leven én "
                  "hun onderlinge relaties, noemen we een <strong>ecosysteem</strong>."),
            ("p", "Wat in een biotoop op de organismen inwerkt, verdelen we in twee soorten. "
                  "<strong>Abiotische factoren</strong> komen uit de niet-levende omgeving: vocht, "
                  "temperatuur, licht, voedingsstoffen, zoutgehalte, bodemhardheid, geluidssterkte, "
                  "luchtvochtigheid, bodemvochtigheid, windsnelheid. <strong>Biotische factoren</strong> "
                  "zijn de levende wezens zelf: bacteriën, schimmels, planten en dieren."),
            ("p", "Die abiotische factoren bepalen mee wie waar kan leven. Waterplanten hebben licht nodig "
                  "dat tot in het water raakt, want zonder licht kunnen ze geen fotosynthese doen; in "
                  "troebel water verdwijnen ze."),
        ]),
        dict(kop="Meten en determineren in een biotoop", blokken=[
            ("fig", tabel(["wat je meet", "waarmee", "eenheid"], [
                ["temperatuur", "thermometer", "°C"],
                ["verlichtingssterkte", "lichtmeter", "lux (lx)"],
                ["luchtvochtigheid", "hygrometer", "%"],
                ["geluidssterkte", "geluidsmeter", "decibel (dB)"],
                ["windsnelheid", "anemometer", "m/s"],
                ["bodemvochtigheid", "vochtigheidsmeter", "%"],
                ["bodemhardheid", "valpen met plastic buis", "diepte in cm"],
            ]), "Meet je onder de bomen 300 lux en op de open plek 20 000 lux, dan verklaart dat meteen waarom daar andere soorten groeien."),
            ("p", "Om uit te zoeken wélke soort je voor je hebt, ga je <strong>determineren</strong>. Je "
                  "volgt een <strong>determineertabel</strong> of <strong>determineerkaart</strong>: "
                  "telkens kies je tussen twee kenmerken tot je bij de juiste soort uitkomt. Om goed te "
                  "kijken gebruik je een <strong>loep</strong>, een <strong>binoculair</strong> of een "
                  "<strong>microscoop</strong>. Een determineertabel is geen meetinstrument maar een "
                  "hulpmiddel."),
        ]),
        dict(kop="Wie eet wie: de voedselrelaties", blokken=[
            ("p", "Organismen hebben allerlei <strong>onderlinge relaties</strong>: om te eten, om te "
                  "schuilen (bescherming) en om zich voort te planten, denk aan een bij die een bloem "
                  "bestuift. De bekendste zijn de voedselrelaties."),
            ("fig", tabel(["rol", "wat ze doen", "voorbeeld"], [
                ["producenten", "maken zelf energierijke stoffen met fotosynthese", "planten, algen"],
                ["consumenten", "eten andere organismen", "konijn, vos"],
                ["detrivoren", "eten dood organisch materiaal", "regenworm, pissebed"],
                ["reducenten", "breken dode resten helemaal af tot voedingsstoffen", "bacteriën, schimmels"],
            ]), "Een jager of predator vangt en eet een prooi. Zonder reducenten zou alles onder dood materiaal bedolven raken."),
            ("p", "Een <strong>voedselketen</strong> is één rij met pijlen: gras → konijn → vos. De pijl "
                  "betekent 'wordt gegeten door', dus hij wijst in de richting waarin de energie stroomt. "
                  "In het echt eet een dier meestal van verschillende soorten; al die ketens samen vormen "
                  "een <strong>voedselweb</strong>."),
            ("fig", svg.voedselpiramide(),
             "Deze voorstelling heet de voedselpiramide: elke laag wordt smaller naar boven toe. Bij elke stap gaat er energie verloren als warmte, dus kan elke laag maar een kleinere laag boven zich voeden."),
            ("p", "De <strong>voedselkringloop</strong> toont nog iets anders: stoffen draaien rond. "
                  "Planten nemen voedingsstoffen op, dieren eten, alles sterft, reducenten breken het af en "
                  "de voedingsstoffen komen weer in de bodem. <strong>Energie</strong> daarentegen stroomt "
                  "maar één kant op: ze komt van de zon en gaat uiteindelijk verloren als warmte. Daarom "
                  "moet er telkens nieuwe zonne-energie bij."),
        ]),
        dict(kop="Wat er gebeurt als je aan één draad trekt", blokken=[
            ("p", "Een <strong>verstoring</strong> werkt door de hele keten. Verdwijnen alle vossen, dan "
                  "komen er eerst meer konijnen, en daardoor blijft er minder gras over; daarna sterven er "
                  "konijnen van de honger. Sterven de bijen uit, dan is er minder bestuiving, dus minder "
                  "vruchten en zaden, dus minder voedsel voor alles wat daarvan eet, en uiteindelijk ook "
                  "minder soorten bloeiende planten."),
            ("kader", "Ook <em>te veel</em> van iets is een verstoring. Spoelt er mest van een akker in een "
                      "vijver, dan komen er enorm veel algen. Het water wordt troebel, de waterplanten "
                      "sterven, en als de algen afsterven, verbruiken de reducenten zo veel zuurstof dat de "
                      "vissen stikken."),
        ]),
        dict(kop="Biodiversiteit en de mens", blokken=[
            ("p", "<strong>Biodiversiteit</strong> is de verscheidenheid aan soorten in een gebied, en ook "
                  "de variatie binnen een soort. Ze is een soort verzekering: een weiland met tien soorten "
                  "bloemen houdt bij ziekte of droogte altijd nog soorten over die het wel volhouden. Een "
                  "<strong>monocultuur</strong> kan door één ziekte of één droog jaar in zijn geheel "
                  "verloren gaan."),
            ("fig", tabel(["slecht voor de biodiversiteit", "goed voor de biodiversiteit"], [
                ["ontbossing, overbevissing", "ecoducten over of onder een weg"],
                ["vervuiling, verharding", "begrazing met schapen of runderen"],
                ["monocultuur", "streekeigen aanplanting"],
                ["invasieve exoten", "dagen zonder vlees"],
            ]), "Een exoot is een soort die van elders komt en hier niet van nature voorkomt; een invasieve exoot, zoals de Japanse duizendknoop, verdringt inheemse soorten omdat ze hier geen natuurlijke vijanden heeft."),
            ("p", "<strong>Begrazing</strong> lijkt ruw, maar grazers houden gras en struiken kort, zodat "
                  "kleine bloeiende planten licht krijgen. Daarom wordt het als beheer gebruikt. Een "
                  "<strong>ecoduct</strong> verbindt twee stukken natuur die door een weg doorsneden zijn, "
                  "zodat dieren zich kunnen verplaatsen en populaties niet geïsoleerd raken."),
            ("p", "Je eigen invloed meet je met je <strong>ecologische voetafdruk</strong>: de oppervlakte "
                  "natuur die nodig is voor jouw manier van leven. Je "
                  "<strong>watervoetafdruk</strong> telt daarbij ook het verborgen water mee, het water dat "
                  "nodig was om je kleren of je eten te maken."),
        ]),
        dict(kop="Aangepast aan je omgeving", blokken=[
            ("p", "<strong>Aanpassingen</strong> zijn kenmerken die de overlevingskansen en de "
                  "voortplantingskansen vergroten in een bepaalde omgeving: kleur, kieuwen, stekels, de "
                  "stand van de ogen, de gestalte, de grootte en de stand van de bladeren, de lengte van de "
                  "stengel."),
            ("fig", tabel(["kenmerk", "omgeving", "waarom het helpt"], [
                ["dikke vetlaag, kleine oren (ijsbeer)", "koud", "minder warmteverlies"],
                ["kleine of naaldvormige bladeren, waslaag, diepe wortels", "droog", "minder waterverlies"],
                ["kieuwen", "water", "zuurstof uit het water halen"],
                ["witte wintervacht", "sneeuw", "schutkleur: minder opgemerkt worden"],
                ["ogen opzij (haas) of vooraan (vos)", "prooi of jager", "rondom kijken of afstand schatten"],
            ]), "Wie langer leeft, krijgt meer nakomelingen. Zo blijven zulke kenmerken in een soort bestaan."),
        ]),
    ],
    onthoud=[
        "Abiotisch is niet-levend (licht, temperatuur, vocht); biotisch zijn de organismen zelf.",
        "Producenten, consumenten, detrivoren en reducenten: elk hun rol in de voedselrelaties.",
        "Een keten is één rij, een web zijn alle ketens samen, een piramide toont de aantallen.",
        "Stoffen gaan rond in een kringloop; energie stroomt maar één kant op en gaat verloren als warmte.",
        "Biodiversiteit maakt een ecosysteem bestand tegen ziekte, droogte en verstoring.",
        "Een aanpassing vergroot de overlevings- en voortplantingskansen in een bepaalde omgeving.",
    ],
)

# ───────────────────────────────────────── 6. Materie, stoffen en mengsels
BUNDELS["materie-stoffen-en-mengsels"] = dict(
    vak=VAK, niveau=SPARK, titel="Materie, stoffen en mengsels",
    onder="Het deeltjesmodel, en wat je ermee kan verklaren.",
    secties=[
        dict(kop="Het deeltjesmodel", blokken=[
            ("p", "Alle stoffen bestaan uit <strong>deeltjes</strong> die te klein zijn om te zien. Met dat "
                  "model kan je een hoop dagelijkse verschijnselen verklaren. Wat verschilt van toestand "
                  "tot toestand, is de <strong>afstand</strong> tussen de deeltjes en de "
                  "<strong>snelheid</strong> waarmee ze bewegen."),
            ("fig", svg.deeltjes(), "Vast, vloeibaar en gasvormig: de drie aggregatietoestanden."),
            ("fig", tabel(["toestand", "de deeltjes", "vorm en volume"], [
                ["vast", "dicht bij elkaar, op een vaste plaats, ze trillen alleen", "vaste vorm, vast volume"],
                ["vloeibaar", "dicht bij elkaar, maar ze schuiven langs elkaar", "geen vaste vorm, wel vast volume"],
                ["gasvormig", "ver uit elkaar, ze vliegen snel rond", "geen vaste vorm, geen vast volume"],
            ]), "Daarom kan je een gas samenpersen en een vaste stof niet: in een gas zit veel lege ruimte tussen de deeltjes."),
            ("p", "Dat gasdeeltjes snel alle kanten op vliegen, merk je meteen: de geur van soep verspreidt "
                  "zich door de hele keuken, ook al staat de pot in de hoek. Hoe warmer, hoe sneller de "
                  "deeltjes bewegen en hoe sneller je de geur ruikt."),
        ]),
        dict(kop="Faseovergangen", blokken=[
            ("fig", svg.faseovergangen(), "Oranje: er gaat warmte bij, de deeltjes bewegen sneller. Blauw: er gaat warmte weg, de deeltjes komen dichter bij elkaar."),
            ("p", "<strong>Smelten</strong> is vast naar vloeibaar, <strong>stollen</strong> het "
                  "omgekeerde; voor eenzelfde zuivere stof gebeuren ze bij dezelfde temperatuur, voor water "
                  "bij 0 °C. <strong>Verdampen</strong> is vloeibaar naar gasvormig, "
                  "<strong>condenseren</strong> het omgekeerde. <strong>Sublimeren</strong> gaat van vast "
                  "rechtstreeks naar gas — droogijs is vast koolstofdioxide en heet daarom droog ijs — en "
                  "<strong>rijpen</strong> of <strong>desublimeren</strong> gaat van gas rechtstreeks naar "
                  "vast, zoals rijp op een tak."),
            ("p", "Bij het <strong>verdampen</strong> van water bewegen de snelste moleculen zo hard dat ze "
                  "zich losmaken van de vloeistof. Het blijven watermoleculen, alleen ver uit elkaar in de "
                  "lucht. Condenseren zie je op een koud raam: het koude glas koelt de lucht ernaast af, "
                  "en koude lucht kan minder waterdamp bevatten."),
            ("weetje", "Tijdens het smelten van ijs <em>stijgt</em> de temperatuur niet. Zolang er nog ijs "
                       "drijft, blijft het mengsel 0 °C: alle toegevoerde warmte gaat naar het losmaken van "
                       "de deeltjes, niet naar opwarmen."),
        ]),
        dict(kop="Uitzetten en krimpen", blokken=[
            ("p", "Warm je een stof op, dan gaan de deeltjes <strong>heviger trillen</strong> en nemen ze "
                  "meer plaats in: de stof <strong>zet uit</strong>. Koel je ze af, dan komen de deeltjes "
                  "dichter bij elkaar en <strong>krimpt</strong> ze. Er komen geen deeltjes bij en de "
                  "deeltjes worden zelf niet groter."),
            ("p", "Daarom laten ze bij spoorstaven en bruggen een kleine opening: zonder die ruimte duwt "
                  "het uitzettende metaal tegen zichzelf en trekt het krom. Water is de bekende "
                  "uitzondering op de regel: bij het bevriezen zet het net uit."),
            ("kader", "Verwarm je een <em>afgesloten</em> fles met lucht, dan kan het volume niet groter "
                      "worden. De extra bewegingsenergie vertaalt zich dan in hardere botsingen tegen de "
                      "wand, en dus in meer druk. Daarom mag je een spuitbus nooit in het vuur gooien."),
        ]),
        dict(kop="Chemisch of fysisch?", blokken=[
            ("p", "Bij een <strong>fysisch verschijnsel</strong> ontstaat er geen nieuwe stof: alleen de "
                  "vorm of de toestand verandert. De deeltjes blijven dezelfde. Smelten, breken, oplossen "
                  "en verdampen zijn fysisch. Bij een <strong>chemisch verschijnsel</strong> — ook "
                  "chemische omzetting of chemische reactie genoemd — veranderen de deeltjes zelf en "
                  "ontstaan er <strong>nieuwe stoffen</strong>."),
            ("fig", tabel(["fysisch", "chemisch"], [
                ["een glas dat breekt", "ijzer dat roest"],
                ["ijs dat smelt, water dat kookt", "hout dat verbrandt"],
                ["suiker die oplost in water", "een appel die bruin wordt"],
                ["boter die smelt", "brood dat roostert"],
            ]), "Een kaars doet allebei tegelijk: de was smelt en verdampt (fysisch), en die damp verbrandt daarna met zuurstof (chemisch)."),
            ("p", "Hoe herken je een chemische reactie? Aan <strong>kleurverandering</strong>, "
                  "<strong>geurverandering</strong>, <strong>smaakverandering</strong>, "
                  "<strong>neerslagvorming</strong> of <strong>gasontwikkeling</strong>. Een chemische "
                  "omzetting is bovendien meestal niet zomaar om te keren: geroosterd brood krijg je niet "
                  "meer wit."),
            ("weetje", "IJzerwol die een week in vochtige lucht ligt, wordt bruin én zwaarder. Kleur­"
                       "verandering plus meer massa betekent een nieuwe stof: het ijzer verbond zich met "
                       "zuurstof tot roest. Roest is dus geen ijzer meer."),
        ]),
        dict(kop="Atomen, verbindingen, mengsels en zuivere stoffen", blokken=[
            ("p", "Een deeltje kan een <strong>atoom</strong> zijn of een <strong>chemische "
                  "verbinding</strong>: een groepje atomen dat met bindingen samenhangt, ook "
                  "<strong>molecule</strong> genoemd. De atoomsoorten of elementen die je moet kennen, zijn "
                  "<strong>koolstof (C)</strong>, <strong>zuurstof (O)</strong>, "
                  "<strong>waterstof (H)</strong> en <strong>ijzer (Fe)</strong>. Die letter is het chemisch "
                  "<strong>symbool</strong> van het element; Fe komt van het Latijnse "
                  "<em>ferrum</em>."),
            ("p", "De formule geeft de bouw van één deeltje. Water is <strong>H₂O</strong>: twee "
                  "waterstofatomen en één zuurstofatoom. Zuurstofgas is <strong>O₂</strong>: twee atomen "
                  "van dezelfde soort. Koolstofdioxide (CO₂) en glucose (C₆H₁₂O₆) bevatten dan weer "
                  "verschillende atoomsoorten."),
            ("p", "Een <strong>zuivere stof</strong> bestaat uit maar één soort deeltje, zoals zuiver water "
                  "of koper. In een <strong>mengsel</strong> zitten verschillende soorten deeltjes door "
                  "elkaar: zeewater is water met opgeloste zouten, lucht is een mengsel van gassen, melk "
                  "met suiker erin is een mengsel."),
            ("kader", "Krijg je een tekening met deeltjes: allemaal identieke bolletjes van twee aan elkaar "
                      "is een <strong>zuivere stof</strong> die uit moleculen bestaat. Twee verschillende "
                      "soorten door elkaar, of losse atomen samen met moleculen, is een "
                      "<strong>mengsel</strong>. Eén soort deeltje betekent altijd zuiver, ook als dat "
                      "deeltje zelf uit meerdere atomen bestaat."),
            ("p", "Oplossen verandert daar niets aan: de suikerdeeltjes zitten verspreid tussen de deeltjes "
                  "van de melk, maar het is nog altijd suiker. Wel verandert een mengsel de "
                  "<strong>stofeigenschappen</strong>: zuiver water bevriest bij 0 °C, zeewater pas lager. "
                  "Daarom strooien ze zout op de weg."),
            ("p", "Een <strong>stofeigenschap</strong> is een kenmerk dat typisch is voor een stof en niet "
                  "afhangt van hoe groot je stuk is: de smelttemperatuur, de kooktemperatuur, de kleur, de "
                  "geleidbaarheid, de massadichtheid."),
        ]),
    ],
    onthoud=[
        "Vast: deeltjes op een vaste plaats. Vloeibaar: ze schuiven. Gas: ver uit elkaar en snel.",
        "Smelten, stollen, verdampen, condenseren, sublimeren en rijpen zijn de zes faseovergangen.",
        "Uitzetten bij opwarmen: de deeltjes trillen heviger en nemen meer plaats in.",
        "Fysisch: geen nieuwe stof. Chemisch: wel, te herkennen aan kleur, geur, neerslag of gas.",
        "Zuivere stof = één soort deeltje. Mengsel = verschillende soorten door elkaar.",
        "Atoomsoorten om te kennen: C, O, H en Fe.",
    ],
)

# ───────────────────────────────────────── 7. Massadichtheid
BUNDELS["massadichtheid"] = dict(
    vak=VAK, niveau=SPARK, titel="Massadichtheid",
    onder="ρ = m / V, en alles wat je daarmee kan uitrekenen en verklaren.",
    secties=[
        dict(kop="Wat massadichtheid is", blokken=[
            ("p", "Waarom weegt een blok ijzer zwaarder dan een even groot blok hout? Omdat ijzer een "
                  "grotere <strong>massadichtheid</strong> heeft: bij ijzer zitten de deeltjes zwaarder en "
                  "dichter op elkaar. Massadichtheid zegt hoeveel massa er in één bepaalde hoeveelheid "
                  "ruimte zit."),
            ("fig", tabel(["grootheid", "symbool", "SI-eenheid", "ook gebruikt"], [
                ["massa", "m", "kilogram (kg)", "gram (g)"],
                ["volume", "V", "kubieke meter (m³)", "liter (L), cm³"],
                ["massadichtheid", "ρ (rho)", "kilogram per kubieke meter (kg/m³)", "g/cm³"],
            ]), "ρ is de Griekse letter rho. Let op het verschil tussen de kleine v (snelheid) en de hoofdletter V (volume)."),
            ("kader", "<strong>ρ = m / V</strong> — je deelt de massa door het volume.<br>"
                      "Daaruit volgt <strong>m = ρ × V</strong> en <strong>V = m / ρ</strong>. "
                      "Met dezelfde formule kan je dus alle drie de grootheden berekenen."),
            ("p", "Massadichtheid is een <strong>stofeigenschap</strong> en zelfs een stofconstante: ze "
                  "hangt niet af van hoe groot je stuk is. Een spijker en een balk van hetzelfde ijzer "
                  "hebben dezelfde massadichtheid. Leg je twee even grote blokjes van dezelfde stof samen, "
                  "dan verdubbelen massa én volume, en blijft hun verhouding gelijk. Twee voorwerpen met "
                  "dezelfde massa hebben daarom nog niet dezelfde massadichtheid: een kilo veren neemt veel "
                  "meer plaats in dan een kilo lood."),
        ]),
        dict(kop="Massa en volume meten", blokken=[
            ("p", "Het juiste <strong>meetinstrument</strong> kiezen hoort erbij. "
                  "De <strong>massa</strong> bepaal je door te wegen, met een "
                  "<strong>weegschaal</strong>. Het <strong>volume</strong> van een vloeistof meet je met "
                  "een <strong>maatcilinder</strong>. De massadichtheid van een vloeistof kan je ook "
                  "rechtstreeks meten met een <strong>dichtheidsmeter</strong> of densiteitsmeter, die in "
                  "de vloeistof drijft."),
            ("p", "Van een <strong>regelmatig voorwerp</strong> reken je het volume uit."),
            ("fig", tabel(["figuur", "formule", "voorbeeld"], [
                ["kubus", "V = z³ &nbsp;(z = de ribbe of zijde)", "ribbe 2 cm → V = 2 × 2 × 2 = 8 cm³"],
                ["balk", "V = l · b · h &nbsp;(lengte, breedte, hoogte)", "5 × 4 × 2 = 40 cm³"],
                ["bol", "V = 4/3 · π · r³ &nbsp;(r = de straal)", "straal 3 cm → 4/3 × 3,14 × 27 = 113,04 cm³"],
                ["cilinder", "V = π · r² · h &nbsp;(straal en hoogte)", "straal 2 cm, hoogte 10 cm → 3,14 × 4 × 10 = 125,6 cm³"],
            ]), "Reken met π ≈ 3,14 als er niets anders bij staat. Elke lengte in dezelfde eenheid, anders klopt je volume niet."),
            ("p", "Van een <strong>onregelmatig voorwerp</strong>, zoals een steen of een moer, bepaal je "
                  "het volume door <strong>onderdompeling</strong>. Het voorwerp duwt evenveel water opzij "
                  "als zijn eigen volume."),
            ("fig", svg.onderdompeling(), "Het verschil tussen het waterpeil vóór en na is het volume."),
            ("fig", svg.maatladder(["m³", "dm³ = L", "cm³ = mL"], onder="× 1000 naar beneden, : 1000 naar boven"),
             "1 m³ = 1000 L, 1 L = 1000 cm³, en 1 mL is precies 1 cm³. Dus 2 L = 0,002 m³ en 0,5 m³ = 500 L."),
            ("kader", "Van <strong>g/cm³ naar kg/m³</strong> vermenigvuldig je met 1000, en omgekeerd deel "
                      "je door 1000. Water is 1 g/cm³ = 1000 kg/m³; aluminium is 2700 kg/m³ = 2,7 g/cm³. "
                      "Eén liter water weegt dus precies 1 kg."),
        ]),
        dict(kop="Rekenen met ρ = m / V", blokken=[
            ("fig", tabel(["wat je zoekt", "hoe", "voorbeeld"], [
                ["massadichtheid", "ρ = m / V", "300 g en 100 cm³ → 3 g/cm³"],
                ["massa", "m = ρ × V", "19 g/cm³ × 3 cm³ = 57 g goud"],
                ["volume", "V = m / ρ", "780 g ijzer : 7,8 g/cm³ = 100 cm³"],
            ]), "Werk altijd eerst het volume uit als je een kubus, balk, bol of cilinder krijgt: 72 g in een kubus van 2 cm is 72 : 8 = 9 g/cm³."),
            ("p", "Een voorbeeld met onderdompeling: het water stijgt van 40 mL naar 55 mL, dus het volume "
                  "is 15 cm³. Weegt het blokje 40,5 g, dan is ρ = 40,5 : 15 = 2,7 g/cm³ — waarschijnlijk "
                  "aluminium. En 2 L olie van 0,9 g/cm³ weegt 0,9 × 2000 = 1800 g, dus 1,8 kg."),
        ]),
        dict(kop="Het verband tussen massa en volume", blokken=[
            ("p", "Meet je van dezelfde stof verschillende stukken, dan zie je een vast patroon: 10 cm³ "
                  "weegt 27 g, 20 cm³ weegt 54 g, 30 cm³ weegt 81 g. Telkens als het volume verdubbelt, "
                  "verdubbelt de massa. Massa en volume zijn dus <strong>recht evenredig</strong>, en de "
                  "verhouding m/V is overal dezelfde: hier 2,7 g/cm³, en dat is de massadichtheid."),
            ("fig", svg.evenredig_grafieken(),
             "Zet je massa (y) tegenover volume (x) voor één stof, dan krijg je de linkse grafiek: een rechte door de oorsprong."),
            ("p", "Staan er twee rechten in één grafiek, dan heeft de <strong>steilste</strong> de grootste "
                  "massadichtheid: bij hetzelfde volume hoort daar de grootste massa. Zo herken je op een "
                  "grafiek of in een tabel welke meetresultaten bij welke stof horen."),
            ("p", "Bij een <strong>vaste massa</strong> ligt het net omgekeerd: wordt het volume groter, "
                  "dan wordt ρ = m / V kleiner. Massadichtheid en volume zijn dan "
                  "<strong>omgekeerd evenredig</strong>: het volume staat in de formule onder de deelstreep. Daarom drijft een schip van staal: door zijn grote volume "
                  "is zijn gemiddelde massadichtheid klein."),
        ]),
        dict(kop="Zinken, zweven, stijgen of drijven", blokken=[
            ("fig", tabel(["als …", "dan …"], [
                ["ρ van het voorwerp &lt; ρ van de vloeistof", "het <strong>drijft</strong>"],
                ["ρ van het voorwerp = ρ van de vloeistof", "het <strong>zweeft</strong>: het blijft hangen waar je het loslaat"],
                ["ρ van het voorwerp &gt; ρ van de vloeistof", "het <strong>zinkt</strong>"],
            ]), "Laat je een voorwerp dat drijft onder water los, dan stijgt het tot het weer aan de oppervlakte komt."),
            ("p", "Het gaat dus altijd om de <strong>vergelijking van twee massadichtheden</strong>, niet "
                  "om het gewicht op zich: een zware boomstam drijft en een klein muntstuk zinkt. Water is "
                  "1 g/cm³, dus ijzer (7,8) en aluminium (2,7) zinken, terwijl kurk (0,24) en olie (0,9) "
                  "blijven drijven. Een voorwerp van 1200 kg/m³ zinkt in water van 1000 kg/m³."),
            ("p", "Een blokje van 60 g met een volume van 75 cm³ heeft ρ = 60 : 75 = 0,8 g/cm³: dat drijft. "
                  "IJs drijft om dezelfde reden: bij het bevriezen zet water uit, dus ijs is ongeveer "
                  "0,92 g/cm³. En een vetlaag blijft bovenop de soep liggen omdat vet ongeveer 0,9 g/cm³ "
                  "is en niet mengt met water."),
            ("weetje", "Hetzelfde geldt voor gassen: een luchtballon stijgt omdat de warme lucht erin een "
                       "kleinere massadichtheid heeft dan de koudere buitenlucht."),
        ]),
    ],
    onthoud=[
        "ρ = m / V, en dus m = ρ × V en V = m / ρ.",
        "V kubus = z³, V balk = l·b·h, V bol = 4/3·π·r³, V cilinder = π·r²·h.",
        "Onregelmatig voorwerp: volume bepalen door onderdompeling; 1 mL = 1 cm³.",
        "1 m³ = 1000 L; van g/cm³ naar kg/m³ maal 1000. Water is 1 g/cm³ = 1000 kg/m³.",
        "Massa en volume van dezelfde stof zijn recht evenredig: een rechte door de oorsprong.",
        "Kleinere massadichtheid dan de vloeistof = drijven; gelijk = zweven; groter = zinken.",
    ],
)

# ───────────────────────────────────────── 8. Energie, kracht en snelheid
BUNDELS["energie-kracht-en-snelheid"] = dict(
    vak=VAK, niveau=SPARK, titel="Energie, kracht en snelheid",
    onder="Energievormen en hun omzettingen, krachten en hun uitwerking, en v = Δx / Δt.",
    secties=[
        dict(kop="Energievormen", blokken=[
            ("fig", tabel(["energievorm", "waar je ze tegenkomt"], [
                ["thermische energie of warmte", "een warme kachel, wrijving"],
                ["elektrische energie", "het stopcontact, een batterij"],
                ["potentiële energie", "een steen die hoog op een muur ligt"],
                ["kinetische energie of bewegingsenergie", "een fietser die snel rijdt"],
                ["stralingsenergie, zoals lichtenergie", "de zon, een lamp"],
                ["chemische energie", "voedsel, brandstof, een batterij"],
                ["kernenergie", "een kerncentrale"],
            ]), "Potentiële energie is opgeslagen energie door plaats of vorm: valt de steen, dan wordt ze kinetische energie."),
            ("p", "Bij een <strong>energieomzetting</strong> verandert de ene vorm in de andere. In een "
                  "lamp wordt elektrische energie omgezet in lichtenergie <em>en warmte</em>. Er verdwijnt "
                  "nooit energie, maar er gaat bij elke omzetting wél een deel naar een <strong>minder "
                  "bruikbare of ongewenste vorm, meestal warmte</strong>. Daarom wordt een gsm warm terwijl "
                  "je hem gebruikt."),
            ("kader", "Een ketting van omzettingen, bij een fiets met dynamo: de chemische energie uit je "
                      "voedsel wordt spierkracht en beweging, de dynamo maakt van die bewegingsenergie "
                      "elektrische energie, en de lamp maakt daar licht van. Bij elke stap gaat er een deel "
                      "verloren als warmte."),
        ]),
        dict(kop="Krachten", blokken=[
            ("p", "Een <strong>kracht</strong> meet je in <strong>newton (N)</strong>, met een "
                  "<strong>dynamometer</strong>: een veer met een schaalverdeling, die verder uitrekt "
                  "naarmate je harder trekt. De grootheid krijgt het symbool <strong>F</strong>."),
            ("p", "Krachten die je moet herkennen: <strong>zwaartekracht</strong> (trekt alles naar het "
                  "middelpunt van de aarde), <strong>wrijvingskracht</strong>, <strong>trekkracht</strong>, "
                  "<strong>duwkracht</strong>, <strong>spierkracht</strong>, <strong>motorkracht</strong> "
                  "en <strong>veerkracht</strong>. Hang je een gewicht aan een dynamometer en lees je 12 N "
                  "af, dan heb je de zwaartekracht op dat gewicht gemeten — geen massa, want die meet je "
                  "in kilogram met een weegschaal."),
            ("fig", svg.krachtpijl(), "Een kracht teken je als een pijl: ze is een vectoriële grootheid met vier kenmerken."),
            ("p", "<strong>Aangrijpingspunt</strong>: waar de kracht aangrijpt. <strong>Grootte</strong>: "
                  "de lengte van de pijl. <strong>Richting</strong>: de lijn waarop ze werkt. "
                  "<strong>Zin</strong>: welke kant ze op wijst. Een kracht van 10 N naar links en één van "
                  "10 N naar rechts hebben dus dezelfde richting, maar een andere zin."),
            ("p", "Werken er meerdere krachten, dan tel je ze samen tot de <strong>resulterende "
                  "kracht</strong> of resultante. Twee mensen die allebei 200 N in dezelfde zin duwen, "
                  "geven samen 400 N. Twee kinderen die allebei 150 N in tegengestelde zin trekken, geven "
                  "een resultante van 0 N: de twee krachten heffen elkaar op en het touw beweegt niet. Bij een resultante van 0 N blijft een "
                  "voorwerp in <strong>rust</strong>, of het behoudt zijn <strong>constante "
                  "snelheid</strong>."),
            ("fig", tabel(["uitwerking", "wat er verandert", "voorbeeld"], [
                ["<strong>statisch</strong>", "de vorm: vervorming", "een veer die uitrekt, een spons die indeukt"],
                ["<strong>dynamisch</strong>", "de bewegingstoestand", "versnellen, vertragen, van bewegingsrichting veranderen"],
            ]), "Een bal die je wegtrapt, gaat sneller én verandert van richting: dynamisch. Dat hij tijdens de trap even indeukt, is statisch."),
            ("weetje", "De <strong>wrijvingskracht</strong> werkt altijd tegen de beweging in: daarom "
                       "vertraagt een bal die over het gras rolt. Maar zonder wrijving zou je ook niet "
                       "kunnen stappen of remmen."),
        ]),
        dict(kop="Constante snelheid", blokken=[
            ("kader", "De formule voor een <strong>constante snelheid</strong>:<br>"
                      "<strong>v = Δx / Δt</strong> — de verplaatsing gedeeld door de tijdsduur.<br>"
                      "Daaruit volgt <strong>Δx = v × Δt</strong> en <strong>Δt = Δx / v</strong>.<br>"
                      "Δx is de verplaatsing in meter (m), Δt de tijdsduur in seconde (s), v de snelheid in "
                      "meter per seconde (m/s). Kilometer per uur (km/h) mag ook, maar is geen SI-eenheid."),
            ("p", "Iemand die 100 m aflegt in 20 s, haalt 100 : 20 = 5 m/s. Een auto die 90 km rijdt in "
                  "2 uur, haalt 90 : 2 = 45 km/h. Rijdt hij het eerste uur 60 km en het tweede uur 80 km, "
                  "dan is zijn gemiddelde snelheid 140 : 2 = 70 km/h."),
            ("p", "Omgekeerd: een fietser die 30 s aan 4 m/s rijdt, legt 4 × 30 = 120 m af. Een wandelaar "
                  "doet over 300 m aan 5 m/s precies 300 : 5 = 60 s, dus één minuut."),
            ("fig", svg.maatladder(["km/h", "m/s"], onder="km/h → m/s: delen door 3,6 · m/s → km/h: maal 3,6"),
             "5 m/s = 18 km/h, 72 km/h = 20 m/s, 36 km/h = 10 m/s. Handig om te onthouden: 36 km/h is precies 10 m/s."),
            ("p", "Let op je eenheden. 1 km = 1000 m, 1 h = 60 min = 3600 s, dus 2 uur is 7200 s en 5 min "
                  "is 300 s. Reken tijd altijd eerst om naar seconden als je in m/s werkt: vergeet je dat, "
                  "dan zit je antwoord er een factor 60 naast. Wil je snelheden vergelijken, zet ze dan "
                  "eerst in dezelfde eenheid: 15 m/s is 54 km/h, en dat is sneller dan 50 km/h of dan 1 km "
                  "in 2 minuten (30 km/h). Een hardloper die 400 m in 50 s doet, haalt 8 m/s of 28,8 km/h."),
        ]),
        dict(kop="Grafieken en verbanden", blokken=[
            ("p", "Zet je de afgelegde weg (y) uit tegenover de tijd (x), dan betekent een "
                  "<strong>rechte door de oorsprong</strong> dat het voorwerp met een constante snelheid "
                  "beweegt: in elke seconde komt er evenveel weg bij. De <strong>steilheid</strong> van die "
                  "rechte is de snelheid, dus van twee rechten gaat de steilste het snelst. Een "
                  "<strong>horizontaal stuk</strong> betekent dat het voorwerp stilstaat: de tijd loopt "
                  "door, de afstand verandert niet, de snelheid is 0 m/s. Lees je bij 4 s een afstand van "
                  "20 m af, dan is v = 20 : 4 = 5 m/s."),
            ("fig", tabel(["wat vastligt", "verband", "in woorden"], [
                ["de snelheid", "verplaatsing en tijdsduur zijn <strong>recht evenredig</strong>", "twee keer zo lang rijden is twee keer zo ver"],
                ["de tijdsduur", "verplaatsing en snelheid zijn <strong>recht evenredig</strong>", "twee keer zo snel is twee keer zo ver"],
                ["de afstand", "snelheid en tijdsduur zijn <strong>omgekeerd evenredig</strong>", "twee keer zo snel is half zo lang onderweg"],
            ]), "Snelheid en tijdsduur zijn dus niet altijd recht evenredig: langer onderweg zijn maakt je niet sneller."),
        ]),
    ],
    onthoud=[
        "Bij elke energieomzetting gaat een deel verloren als warmte.",
        "Kracht: symbool F, eenheid newton (N), gemeten met een dynamometer.",
        "Vier kenmerken van een kracht: aangrijpingspunt, grootte, richting en zin.",
        "Statische uitwerking = vervorming; dynamische uitwerking = verandering van beweging.",
        "v = Δx / Δt; m/s → km/h maal 3,6, km/h → m/s delen door 3,6.",
        "Een rechte door de oorsprong in een x-t-grafiek betekent een constante snelheid.",
    ],
)

# ───────────────────────────────────────── 9. Veilig werken, meten en eenheden
BUNDELS["veilig-werken-meten-en-eenheden"] = dict(
    vak=VAK, niveau=SPARK, titel="Veilig werken, meten en eenheden",
    onder="Hoe je veilig en duurzaam werkt, welk meetinstrument je kiest, en hoe je grootheden en eenheden schrijft.",
    secties=[
        dict(kop="Veilig en duurzaam werken", blokken=[
            ("p", "Tijdens een onderzoek of een experiment werk je altijd veilig en duurzaam, met stoffen, "
                  "met organismen en met technische systemen zoals handgereedschap, glaswerk, een "
                  "bunsenbrander, een lichtmicroscoop, een weegschaal of een thermometer."),
            ("fig", tabel(["goed", "waarom"], [
                ["gemorste producten onmiddellijk opkuisen", "niemand glijdt uit of komt ermee in contact"],
                ["meetinstrumenten uitschakelen als je niet meet", "spaart energie en de batterij, en het toestel gaat langer mee"],
                ["hygiënisch omgaan met biologisch materiaal", "geen besmetting; levend materiaal zet je terug waar je het haalde"],
                ["biologisch afval correct sorteren", "duurzaam en veilig"],
                ["zuinig omspringen met chemische stoffen", "minder afval, minder risico"],
                ["elektrische toestellen nooit met natte handen bedienen", "water geleidt: risico op een elektrische schok"],
                ["handleidingen en werktekeningen juist interpreteren", "je weet hoe je het toestel veilig en juist bedient"],
                ["glaswerk voorzichtig behandelen en na gebruik schoonmaken", "glasscherven ruim je op met borstel en blik, nooit met je blote handen"],
            ]), "Bij een bunsenbrander: lang haar samenbinden, de brander nooit onbewaakt laten branden, brandbare stoffen ver weg houden, en achteraf de gastoevoer dichtdraaien."),
        ]),
        dict(kop="Het juiste meetinstrument kiezen", blokken=[
            ("fig", tabel(["grootheid", "meetinstrument of meetmethode"], [
                ["kracht", "dynamometer"],
                ["massadichtheid", "dichtheidsmeter of densiteitsmeter"],
                ["massa", "weegschaal"],
                ["volume", "maatcilinder"],
                ["lengte, afstand, verplaatsing", "meetlat, rolmeter, vouwmeter, schuifmaat, micrometer"],
                ["snelheid", "snelheidsmeter, speedgun"],
                ["tijdsduur", "chronometer, klok"],
                ["temperatuur", "thermometer"],
                ["verlichtingssterkte", "lichtmeter"],
                ["luchtvochtigheid", "hygrometer"],
                ["geluidssterkte", "geluidsmeter"],
                ["windsnelheid", "anemometer"],
                ["bodemvochtigheid", "vochtigheidsmeter"],
                ["bodemhardheid", "valpen met plastic buis"],
            ]), "Ook in een <strong>biotoop</strong> gebruik je deze instrumenten: je bepaalt er de temperatuur, het licht, de luchtvochtigheid, de bodemvochtigheid en de bodemhardheid mee. Deze tabel staat in bijlage 1 van de vakfiche — en die bijlage mag je níet gebruiken op het examen."),
            ("p", "Kies uit gelijksoortige instrumenten dat met de <strong>gepaste "
                  "nauwkeurigheid</strong>. Moet je 25 mL afmeten, neem dan een maatcilinder van 50 mL met "
                  "streepjes van 1 mL, niet één van 1 L met streepjes van 50 mL en al helemaal geen emmer. "
                  "Een <strong>schuifmaat</strong> leest tienden van millimeters af, een meetlat alleen "
                  "hele millimeters. Te weinig nauwkeurig is even onbruikbaar als helemaal niets."),
            ("p", "Voor bekijken in plaats van meten gebruik je een <strong>loep</strong>, een "
                  "<strong>binoculair</strong> of een <strong>lichtmicroscoop</strong>; een cel zie je "
                  "alleen met die laatste. Een <strong>determineertabel</strong> is ook een hulpmiddel, "
                  "geen meetinstrument."),
            ("kader", "<strong>Correct aflezen.</strong> Zet een maatcilinder recht, houd je oog op "
                      "dezelfde hoogte als de vloeistof en lees af aan de <em>onderkant van de holle "
                      "bolling</em>. Kijk je van bovenaf of schuin, dan lees je ernaast. Weeg je iets in "
                      "een bekerglas, weeg dan eerst het lege glas: een leeg bekerglas van 120 g dat met "
                      "water 370 g weegt, bevat 250 g water. En meet liefst meerdere keren: krijg je "
                      "12,4 cm, 12,5 cm en 12,4 cm, neem dan het gemiddelde. Herhalen vangt kleine "
                      "afleesfouten op."),
        ]),
        dict(kop="Grootheden, eenheden en symbolen", blokken=[
            ("fig", tabel(["grootheid", "symbool", "SI-eenheid", "niet-SI"], [
                ["lengte / afstand / verplaatsing", "l · x · Δx", "meter (m)", ""],
                ["volume", "V", "kubieke meter (m³)", "liter (L)"],
                ["massa", "m", "kilogram (kg)", "ton (t)"],
                ["tijdstip / tijdsduur", "t · Δt", "seconde (s)", "min, h"],
                ["temperatuur", "θ", "kelvin (K)", "°C"],
                ["snelheid", "v", "meter per seconde (m/s)", "km/h"],
                ["kracht", "F", "newton (N)", ""],
                ["massadichtheid", "ρ (de Griekse letter rho)", "kilogram per kubieke meter (kg/m³)", "g/L, g/cm³"],
                ["verlichtingssterkte", "E", "lux (lx)", ""],
                ["geluidssterkte", "L", "decibel (dB)", ""],
                ["relatieve luchtvochtigheid", "φ", "procent (%)", ""],
            ]), "Let op hoofdletters en kleine letters: v is snelheid, V is volume. Ook die tabel staat in bijlage 1 en moet je dus kennen."),
            ("p", "Geef bij een meting <strong>altijd de eenheid</strong> mee. '5' kan 5 gram of 5 kilogram "
                  "zijn; schrijft iemand bij de lengte van zijn tafel alleen '1,2', dan ontbreekt de "
                  "eenheid en betekent het getal niets. Pas met de eenheid erbij kan iemand anders je "
                  "meting gebruiken en vergelijken."),
        ]),
        dict(kop="Voorvoegsels en omzetten", blokken=[
            ("fig", tabel(["voorvoegsel", "betekent", "voorbeeld"], [
                ["kilo (k)", "1000", "1 km = 1000 m · 1 kg = 1000 g"],
                ["hecto (h)", "100", "1 hL = 100 L"],
                ["deca (da)", "10", "1 dam = 10 m"],
                ["deci (d)", "0,1", "1 dm = 0,1 m"],
                ["centi (c)", "0,01", "75 cm = 0,75 m"],
                ["milli (m)", "0,001 of een duizendste", "3 mm = 0,003 m · 250 mL = 0,25 L"],
            ]), "Van milli tot kilo: die reeks moet je vlot in twee richtingen kunnen gebruiken."),
            ("p", "Zo is 2 km gelijk aan 2000 m, 500 g aan 0,5 kg en 1,5 kg aan 1500 g. Een "
                  "<strong>schatting</strong> maken hoort er ook bij: een appel weegt ongeveer 150 g. Kom "
                  "je op 15 g of 1,5 kg uit, dan weet je meteen dat je je ergens vergist hebt."),
        ]),
    ],
    onthoud=[
        "Veilig werken: meteen opkuisen, nooit natte handen aan elektriciteit, glaswerk voorzichtig.",
        "Ken de tabel: welke grootheid meet je met welk instrument, en in welke eenheid.",
        "Kies het instrument met de gepaste nauwkeurigheid, en lees het correct af.",
        "Een meetresultaat is een getal én een eenheid.",
        "Milli = 0,001 · centi = 0,01 · deci = 0,1 · kilo = 1000.",
        "Meet meerdere keren en neem het gemiddelde.",
    ],
)

# ───────────────────────────────────────── 10. Wetenschappelijk onderzoek
BUNDELS["wetenschappelijk-onderzoek"] = dict(
    vak=VAK, niveau=SPARK, titel="Wetenschappelijk onderzoek",
    onder="De stappen van een onderzoek, een goede onderzoeksvraag, en hoe je verbanden onderzoekt.",
    secties=[
        dict(kop="De stappen van een onderzoek", blokken=[
            ("fig", svg.stappen(["probleem|afbakenen", "vraag en|hypothese", "onderzoeks-|plan",
                                 "data|verzamelen", "analyse en|conclusie", "reflectie"]),
             "Op het examen krijg je zo'n onderzoek als opgave, rond een wetenschappelijk, een STEM- of een maatschappelijk probleem."),
            ("p", "Een onderzoek begint met een <strong>probleemstelling</strong> die je definieert en "
                  "afbakent, en daarna met een <strong>onderzoeksvraag</strong>. Je formuleert een "
                  "<strong>hypothese</strong>: een verwachting die je vooraf opschrijft, vaak in de vorm "
                  "'als …, dan …'. Je schrijft ze op vóór je meet, anders pas je je verwachting ongemerkt "
                  "aan je resultaat aan."),
            ("p", "In je <strong>onderzoeksplan</strong> staat wat je meet, waarmee, hoe vaak en wat je "
                  "constant houdt. Daarna verzamel je <strong>data</strong> — je metingen en gegevens — "
                  "en verwerk je die in een tabel of een grafiek. Je trekt je "
                  "<strong>conclusie</strong> uit die data: ze is het antwoord of de verklaring op je "
                  "onderzoeksvraag. Ten slotte <strong>reflecteer</strong> je: je kijkt terug op je "
                  "methode en je resultaten en zegt eerlijk wat beter kon. En je "
                  "<strong>communiceert</strong>, in een verslag of een presentatie. In dat verslag horen je "
                  "onderzoeksvraag en hypothese, je <strong>werkwijze</strong> en je resultaten, en je "
                  "conclusie en reflectie."),
            ("kader", "<strong>STEM</strong> staat voor Science, Technology, Engineering en Mathematics. "
                      "Bij een STEM-opdracht zet je wetenschap, techniek, ontwerpen en wiskunde samen in om "
                      "een probleem op te lossen — ook een maatschappelijk probleem."),
        ]),
        dict(kop="Een goede onderzoeksvraag", blokken=[
            ("fig", tabel(["criterium", "dit wil zeggen"], [
                ["open", "de onderzoeksvraag is een open vraag, niet met ja of nee te beantwoorden"],
                ["enkelvoudig", "ze gaat over één onderwerp, één probleem"],
                ["objectief", "ze laat geen overtuiging of mening blijken"],
                ["haalbaar", "het onderzoek is uitvoerbaar met de tijd en de middelen die er zijn"],
                ["onderzoekbaar", "het is geen opzoekvraag en niet meteen oplosbaar"],
                ["relevant", "het antwoord draagt bij aan wat we al weten over het onderwerp"],
            ]), "Die zes criteria staan in bijlage 1 van de vakfiche, en de linkerkolom krijg je ook op het examen."),
            ("p", "Een goede vraag: <em>Welke invloed heeft de hoeveelheid water op de groei van "
                  "tuinkers?</em> Fout gaat het bij <em>Is tuinkers lekker?</em> (een mening), "
                  "<em>Hoeveel poten heeft een spin?</em> (een opzoekvraag, dus niet onderzoekbaar), "
                  "<em>Is een elektrische auto niet beter dan een benzineauto?</em> (niet open én niet "
                  "objectief: het antwoord zit al in de vraag) en <em>Groeien planten sneller met meer "
                  "licht en meer mest?</em> (niet enkelvoudig, want twee variabelen tegelijk, én gesloten). "
                  "Ook <em>Hoe evolueert de zeespiegel de komende honderd jaar?</em> valt af: mooi, maar "
                  "niet haalbaar voor een schoolonderzoek."),
        ]),
        dict(kop="Eerlijk meten", blokken=[
            ("p", "Een <strong>variabele</strong> is iets dat kan veranderen en dat je meet of instelt. In "
                  "een goede proef verander je er <strong>maar één</strong>, meet je er één, en houd je "
                  "alle andere gelijk. Test je of planten sneller groeien met meer licht, dan houd je de "
                  "hoeveelheid water, de soort plant en de temperatuur gelijk; alleen het licht verschilt."),
            ("p", "Verander je twee dingen tegelijk — mest én een plek voor het raam — dan lopen de twee "
                  "door elkaar en weet je achteraf niet waardoor het verschil komt. Je conclusie is dan "
                  "waardeloos."),
            ("p", "<strong>Herhaal</strong> je metingen. Eén meting kan toevallig afwijken, en met één "
                  "plant kan een toevalligheid je hele besluit sturen. Meerdere herhalingen en het "
                  "gemiddelde maken je resultaat betrouwbaarder."),
            ("weetje", "Een <strong>waarneming</strong> is wat je ziet of meet ('het water is 30 °C'). Een "
                       "<strong>besluit</strong> is wat je daaruit afleidt ('water koelt trager af met een "
                       "deksel'). Een conclusie steunt op data, nooit op een gevoel — en een hypothese die "
                       "niet uitkomt, is géén mislukking: je hebt geleerd hoe het níet zit. Resultaten "
                       "weglaten omdat ze niet passen, mag nooit."),
        ]),
        dict(kop="Data, modellen en verbanden", blokken=[
            ("p", "Om je gegevens voor te stellen gebruik je een <strong>model</strong>: een schets, een "
                  "tabel, een grafiek, een formule of een vergelijking. Op de <strong>horizontale as</strong> "
                  "van een grafiek zet je wat je zelf instelt of laat veranderen, op de verticale as wat "
                  "daarvan afhangt."),
            ("p", "Uit een tabel haal je verbanden: duurt het bij 10 °C 40 min, bij 20 °C 20 min en bij "
                  "40 °C 10 min, dan geldt: hoe hoger de temperatuur, hoe korter de tijd. Uit een grafiek "
                  "lees je hetzelfde af: meet je afkoelend water (80 °C, 60 °C, 45 °C, 35 °C, 30 °C), dan "
                  "krijg je een dalende kromme die steeds vlakker wordt."),
            ("fig", svg.evenredig_grafieken(),
             "Recht evenredig geeft een rechte door de oorsprong, omgekeerd evenredig een kromme."),
            ("p", "<strong>Recht evenredig</strong>: wordt de ene twee keer zo groot, dan de andere ook. "
                  "Het aantal broden en de prijs, de tijd die je fietst en de afgelegde weg aan constante "
                  "snelheid, de massa en het volume van eenzelfde stof. <strong>Omgekeerd "
                  "evenredig</strong>: wordt de ene twee keer zo groot, dan halveert de andere, en blijft "
                  "hun product constant. Meer werkers aan dezelfde klus betekent minder tijd."),
            ("p", "Uit een grafiek haal je ook getallen. Lees je op een rechte door de oorsprong bij 4 s een "
                  "<strong>afstand</strong> van 20 m af, dan is de snelheid 20 : 4 = 5 m/s."),
            ("kader", "<strong>Formules omvormen</strong> hoort erbij: je drukt één variabele uit "
                      "<strong>in functie van</strong> de andere. Uit v = Δx / Δt volgt "
                      "Δx = v × Δt en Δt = Δx / v. Uit ρ = m / V volgt m = ρ × V en V = m / ρ. Je "
                      "vermenigvuldigt of deelt gewoon beide kanten met dezelfde grootheid."),
            ("p", "Kies je meetbare variabele met zorg. Wil je weten welk isolatiemateriaal een beker "
                  "koffie het langst warm houdt, dan meet je de <em>temperatuur na een bepaalde tijd</em> "
                  "— niet de kleur of de prijs van het materiaal."),
        ]),
    ],
    onthoud=[
        "Volgorde: probleem, onderzoeksvraag en hypothese, plan, data, analyse en conclusie, reflectie.",
        "Een onderzoeksvraag is open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant.",
        "Verander één variabele tegelijk en houd de rest constant.",
        "Herhaal je metingen; een conclusie steunt op data, niet op een gevoel.",
        "Recht evenredig: rechte door de oorsprong. Omgekeerd evenredig: het product blijft constant.",
        "STEM = Science, Technology, Engineering en Mathematics.",
    ],
)
