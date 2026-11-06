# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — De bloeddruk en het lymfestelsel.

Biologie, blok "Stofwisselingsfysiologie en secretie", koppen "De bloeddruk"
en "Het lymfestelsel". Deel 1 gaat over de bloeddruk en de regeling ervan,
deel 2 over weefselvocht, lymfe en het lymfestelsel.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "Wat is de systolische bloeddruk of bovendruk?",
        [
            "de hoogste druk in de slagaders, als de kamers samentrekken",
            "de laagste druk in de slagaders, als het hart ontspant",
            "de druk in de aders vlak voor het bloed het hart binnenkomt",
            "de druk in de longen tijdens een diepe inademing",
        ],
        0,
        "Tijdens de kamersystole perst het hart bloed in de slagaders en is de druk het hoogst. Dat is de bovendruk.",
    ),
    I(
        "In welke eenheid drukt men de bloeddruk meestal uit?",
        ["mmHg", "millimeter kwik"],
        "De bloeddruk wordt uitgedrukt in millimeter kwik, mmHg. Een normale bloeddruk is ongeveer 120 over 80 mmHg.",
    ),
    M(
        "Welke bloeddruk geldt als een normale waarde bij een gezonde volwassene in rust?",
        ["ongeveer 120/80 mmHg", "ongeveer 200/150 mmHg", "ongeveer 60/20 mmHg", "ongeveer 80/120 mmHg"],
        0,
        "De bovendruk staat eerst en de onderdruk daarna. Rond 120 over 80 is normaal. 80/120 kan niet, want de onderdruk is altijd lager dan de bovendruk.",
    ),
    W(
        "Men spreekt van hypertensie als de bloeddruk in rust herhaaldelijk 140/90 mmHg of hoger is.",
        True,
        "Vanaf ongeveer 140 over 90 spreekt men van hoge bloeddruk of hypertensie. Bij een veel te lage druk spreekt men van hypotensie.",
    ),
    M(
        "Hoe evolueert de bloeddruk op de weg van het hart door de bloedsomloop?",
        [
            "hoog in de aorta, dalend in de kleine vaten en laag in de aders",
            "laag in de aorta, stijgend in de haarvaten en het hoogst in de aders",
            "overal even hoog, want het hart pompt met een constante kracht",
            "het hoogst in de haarvaten, omdat die het smalst zijn",
        ],
        0,
        "De druk is het hoogst vlak na het hart. Door de weerstand in de kleine vaten daalt ze, en in de holle aders is ze bijna nul.",
    ),
    I(
        "Hoe heten de zintuigcellen in de wand van de aorta en de halsslagaders die de bloeddruk meten?",
        ["baroreceptoren", "drukreceptoren"],
        "Baroreceptoren voelen hoe ver de vaatwand uitgerekt wordt. Ze sturen die informatie naar het cardiovasculair centrum in het verlengde merg.",
    ),
    M(
        "Waar ligt het cardiovasculair centrum dat de bloeddruk regelt?",
        ["in het verlengde merg", "in de linkerkamer", "in de nieren", "in de sinusknoop"],
        0,
        "Het cardiovasculair centrum in het verlengde merg verwerkt de signalen van de baroreceptoren en stuurt het hart en de bloedvaten bij.",
    ),
    M(
        "De bloeddruk is te hoog. Hoe reageert het negatief feedbacksysteem? Kruis alles aan wat juist is.",
        [
            "het hart gaat trager kloppen",
            "het slagvolume stijgt",
            "de bloedvaten verwijden (vasodilatatie)",
            "de bloedvaten vernauwen (vasoconstrictie)",
        ],
        [0, 2],
        "Bij een te hoge druk vertraagt het hart, pompt het minder bloed per slag en verwijden de bloedvaten. Zo zakt de druk weer.",
    ),
    M(
        "Welke rol speelt het orthosympatisch zenuwstelsel tijdens het sporten?",
        [
            "het versnelt de hartslag en doet de bloeddruk stijgen",
            "het vertraagt de hartslag en doet de bloeddruk dalen",
            "het zet de nieren aan om meer water uit te scheiden",
            "het remt de werking van de sinusknoop volledig af",
        ],
        0,
        "Het orthosympatisch zenuwstelsel zet het lichaam in actie: hart sneller, meer bloed naar de spieren. Na het sporten brengt het parasympatisch zenuwstelsel alles weer tot rust.",
    ),
    W(
        "Het parasympatisch zenuwstelsel zorgt na het sporten voor een snellere hartslag.",
        False,
        "Het parasympatisch zenuwstelsel is het rustsysteem: het vertraagt de hartslag en laat de bloeddruk weer dalen.",
    ),
    M(
        "Welke stof maken de nieren aan als de bloeddruk te laag is?",
        ["renine", "insuline", "ADH", "pepsine"],
        0,
        "Bij een te lage druk geven de nieren renine af. Dat start een keten die eindigt bij angiotensine II en aldosteron, die de druk weer doen stijgen.",
    ),
    M(
        "In welke volgorde verloopt het renine-angiotensinesysteem?",
        [
            "renine zet angiotensinogeen om in angiotensine I, en het ACE-enzym zet dat om in angiotensine II",
            "angiotensine II zet renine om in angiotensinogeen, en het ACE-enzym zet dat om in angiotensine I",
            "het ACE-enzym zet renine om in angiotensine I, dat de nieren omzetten in angiotensinogeen",
            "angiotensinogeen zet renine om in het ACE-enzym, dat de bloeddruk doet dalen",
        ],
        0,
        "Renine knipt angiotensinogeen tot angiotensine I. Het ACE-enzym maakt daar angiotensine II van, dat de bloedvaten vernauwt en aldosteron vrijmaakt.",
    ),
    M(
        "Hoe doet aldosteron de bloeddruk stijgen?",
        [
            "het laat de nieren meer zout en water terugnemen, dus meer bloedvolume",
            "het laat het hart sneller kloppen door rechtstreeks op de sinusknoop te werken",
            "het breekt het ACE-enzym af, zodat er meer angiotensine I overblijft",
            "het maakt de wand van de slagaders dunner zodat er meer bloed door kan",
        ],
        0,
        "Aldosteron uit de bijnier laat de nieren meer natrium terugnemen. Water volgt door osmose, het bloedvolume stijgt en dus ook de druk.",
    ),
    W(
        "Angiotensine II doet de bloedvaten vernauwen, waardoor de bloeddruk stijgt.",
        True,
        "Vasoconstrictie vergroot de weerstand in de bloedvaten. Daarom remmen veel bloeddrukverlagers het ACE-enzym, zodat er minder angiotensine II ontstaat.",
    ),
    M(
        "Welke gevolgen kan een langdurig te hoge bloeddruk hebben? Kruis alles aan wat juist is.",
        ["een beroerte", "een hartinfarct", "schade aan de nieren", "een hogere hematocriet door meer EPO"],
        [0, 1, 2],
        "Hoge bloeddruk beschadigt op lange termijn de bloedvaten van de hersenen, het hart en de nieren. Vaak merk je zelf lang niets.",
    ),
    M(
        "Wat is een typisch symptoom van een te lage bloeddruk?",
        [
            "duizeligheid bij snel rechtstaan",
            "een rood en opgezwollen gezicht",
            "een veel te trage spijsvertering",
            "een hogere lichaamstemperatuur",
        ],
        0,
        "Bij hypotensie krijgen de hersenen even te weinig bloed, vooral als je snel rechtstaat. Je wordt duizelig of ziet zwart.",
    ),
    M(
        "Wat kan je zelf doen om een te hoge bloeddruk te voorkomen? Kruis alles aan wat juist is.",
        ["minder zout eten", "regelmatig bewegen", "niet roken", "meer drop en zoute snacks eten"],
        [0, 1, 2],
        "Weinig zout, voldoende beweging, niet roken, een gezond gewicht en weinig alcohol houden de bloeddruk laag. Echte drop kan de bloeddruk net doen stijgen.",
    ),
    I(
        "Hoe noemt men het verwijden van de bloedvaten, waardoor de bloeddruk daalt?",
        "vasodilatatie",
        "Bij vasodilatatie ontspant het gladde spierweefsel in de vaatwand. Het omgekeerde, het vernauwen, heet vasoconstrictie.",
    ),
    W(
        "Bij een negatief feedbacksysteem versterkt de reactie de oorspronkelijke verandering nog.",
        False,
        "Een negatief feedbacksysteem werkt de verandering tegen. Stijgt de bloeddruk, dan zorgt het systeem dat ze weer daalt, en omgekeerd.",
    ),
    M(
        "Wat bepaalt mee hoe hoog de bloeddruk is? Kruis alles aan wat juist is.",
        ["het hartritme", "het slagvolume", "de wijdte van de bloedvaten", "het bloedvolume"],
        [0, 1, 2, 3],
        "Hoe vaker en hoe krachtiger het hart pompt, en hoe nauwer de bloedvaten, hoe hoger de druk. Ook het bloedvolume speelt mee.",
    ),
]

DEEL2 = [
    M(
        "Hoe ontstaat weefselvocht?",
        [
            "de bloeddruk perst plasma uit het begin van de haarvaten",
            "de cellen maken zelf vocht aan dat ze tussen elkaar uitscheiden",
            "het lymfevocht stroomt uit de lymfeklieren tussen de cellen in",
            "de nieren pompen het water rechtstreeks in de weefsels rondom",
        ],
        0,
        "Aan het slagaderlijke begin van een haarvat is de hydrostatische druk hoger dan de osmotische druk. Er sijpelt plasma zonder grote eiwitten tussen de cellen.",
    ),
    M(
        "Waarom stroomt het meeste weefselvocht aan het einde van een haarvat terug in het bloed?",
        [
            "de bloeddruk is daar gezakt en de plasma-eiwitten trekken water terug",
            "de lymfevaten pompen het vocht met kracht terug in het haarvat",
            "het hart zuigt het vocht terug tijdens elke diastole van de kamers",
            "de cellen stoten het overtollige vocht actief af met hun pompen",
        ],
        0,
        "Aan het aderlijke einde is de hydrostatische druk lager dan de osmotische druk. Daardoor gaat het meeste vocht terug. Een klein overschot blijft achter.",
    ),
    I(
        "Hoe noemt men het weefselvocht zodra het in de lymfevaten is opgenomen?",
        "lymfe",
        "Het overtollige weefselvocht gaat in de lymfecapillairen en heet dan lymfe. Het bevat vooral water, zouten, wat eiwitten en lymfocyten.",
    ),
    M(
        "Wat is de belangrijkste functie van het lymfevatenstelsel bij de drainage van de weefsels?",
        [
            "het overtollige weefselvocht terug in het bloed brengen",
            "de zuurstof van de longen naar de weefsels brengen",
            "het bloed in de grote slagaders onder hoge druk houden",
            "de urine van de nieren naar de urineblaas brengen",
        ],
        0,
        "Lymfevaten verzamelen het vocht dat niet in de haarvaten terugkomt en brengen het via de borstbuis terug naar het bloed. Zo zwellen de weefsels niet op.",
    ),
    W(
        "Lymfevaten hebben kleppen, net als aders, zodat de lymfe maar in één richting stroomt.",
        True,
        "Het lymfestelsel heeft geen pomp zoals het hart. Spierbewegingen duwen de lymfe vooruit, en kleppen beletten dat ze terugstroomt.",
    ),
    M(
        "Waar mondt de borstbuis uit?",
        [
            "in een grote ader onder het sleutelbeen",
            "in de linkerkamer van het hart, naast de aorta",
            "in de twaalfvingerige darm, net als de galgang",
            "in de urineblaas, samen met de urineleider",
        ],
        0,
        "De borstbuis verzamelt de lymfe uit het grootste deel van het lichaam en mondt uit in een grote ader aan de linkerkant, onder het sleutelbeen.",
    ),
    M(
        "Welke organen horen bij het lymfestelsel? Kruis alles aan wat juist is.",
        ["de milt", "de schildklier", "de zwezerik of thymus", "de alvleesklier"],
        [0, 2],
        "Milt, amandelen, thymus, beenmerg en lymfeklieren zijn lymfeorganen. De schildklier is een hormoonklier en de alvleesklier een verterings- en hormoonklier.",
    ),
    M(
        "Wat gebeurt er in een lymfeklier?",
        [
            "de lymfe wordt gefilterd en lymfocyten ruimen ziektekiemen op",
            "de lymfe wordt omgezet in bloedplasma met rode bloedcellen",
            "er worden verteringsenzymen aan de lymfe toegevoegd voor de vetten",
            "de lymfe wordt opgeslagen tot de nieren ze uitscheiden",
        ],
        0,
        "Lymfeklieren zijn filters langs de lymfevaten. Bij een infectie zwellen ze op, omdat er veel lymfocyten aan het werk zijn.",
    ),
    W(
        "In de thymus rijpen de T-lymfocyten.",
        True,
        "De T in T-lymfocyt verwijst naar de thymus of zwezerik. Daar rijpen de jonge thymocyten tot T-lymfocyten, onder invloed van het hormoon thymosine.",
    ),
    I(
        "Hoe heet het hormoon van de thymus dat de rijping van T-lymfocyten stimuleert?",
        "thymosine",
        "Thymosine helpt de thymocyten om T-lymfocyten te worden. De thymus is vooral bij kinderen actief en krimpt na de puberteit.",
    ),
    M(
        "Wat is lymfoedeem?",
        [
            "een zwelling doordat lymfe niet goed afgevoerd wordt",
            "een infectie van de lymfeklieren door bacteriën of virussen",
            "een tekort aan lymfocyten in het bloed na een ziekte",
            "een te hoge bloeddruk in de lymfevaten van de longen",
        ],
        0,
        "Bij lymfoedeem blijft vocht in de weefsels hangen. Een arm of been zwelt op en voelt zwaar aan.",
    ),
    M(
        "Hoe kan lymfoedeem ontstaan? Kruis alles aan wat juist is.",
        [
            "na het wegnemen van lymfeklieren bij een kankeroperatie",
            "door bestraling die de lymfevaten beschadigt",
            "door een aangeboren afwijking aan de lymfevaten",
            "door te veel water te drinken op een warme dag",
        ],
        [0, 1, 2],
        "Lymfoedeem ontstaat als de afvoer verstoord is, bijvoorbeeld na een operatie of bestraling, of door een aangeboren fout. Gewoon veel drinken veroorzaakt het niet.",
    ),
    M(
        "Hoe behandelt men lymfoedeem?",
        [
            "met lymfedrainage, steunkousen of een drukverband",
            "met antibiotica die de verstopte lymfevaten openzetten",
            "met een bloedtransfusie om meer lymfocyten aan te voeren",
            "door minder te bewegen zodat de lymfe tot rust komt",
        ],
        0,
        "Manuele lymfedrainage, steunkousen of drukverband en beweging helpen het vocht af te voeren. Genezen kan meestal niet, maar de klachten worden kleiner.",
    ),
    M(
        "Waarom krijgen kinderen met ernstige ondervoeding soms een opgezwollen buik, hongeroedeem?",
        [
            "door te weinig eiwitten in het bloed gaat minder vocht terug in de haarvaten",
            "hun lymfevaten zijn verstopt door bacteriën uit vervuild water",
            "hun nieren maken te veel urine en houden zo te weinig water over",
            "hun maag zet uit door te veel lucht te slikken bij het eten",
        ],
        0,
        "Bij een eiwittekort daalt de osmotische druk van het bloed. Er gaat minder vocht terug naar de haarvaten, en het stapelt zich op in de weefsels en de buik.",
    ),
    W(
        "Weefselvocht bevat evenveel grote eiwitten als bloedplasma.",
        False,
        "Grote plasma-eiwitten zoals albumine passen nauwelijks door de haarvatwand. Daarom bevat weefselvocht veel minder eiwitten dan plasma.",
    ),
    M(
        "Waaruit bestaat de lymfe vooral?",
        [
            "water, zouten, wat eiwitten en lymfocyten",
            "rode bloedcellen en bloedplaatjes",
            "verteringsenzymen en gal",
            "ureum en urinezuur in hoge concentratie",
        ],
        0,
        "Lymfe lijkt op weefselvocht. Er zitten geen rode bloedcellen in, wel lymfocyten. Na een vette maaltijd bevat de lymfe uit de darmen ook veel vetdeeltjes.",
    ),
    M(
        "Welke rol speelt de milt? Kruis alles aan wat juist is.",
        [
            "ze ruimt versleten rode bloedcellen op",
            "ze bevat veel lymfocyten die het bloed op ziekteverwekkers controleren",
            "ze slaat een voorraad bloed op",
            "ze maakt gal aan voor de vertering",
        ],
        [0, 1, 2],
        "De milt filtert het bloed, ruimt oude rode bloedcellen op, helpt bij de afweer en houdt een voorraad bloed. Gal komt uit de lever.",
    ),
    W(
        "Het lymfestelsel heeft een eigen pomp, net zoals het bloed het hart heeft.",
        False,
        "Er is geen lymfepomp. De lymfe beweegt door het samentrekken van de spieren rond de lymfevaten, de ademhaling en de kleppen in de vaten.",
    ),
    M(
        "Waarom raadt men bij lymfoedeem net aan om te blijven bewegen?",
        [
            "werkende spieren knijpen de lymfevaten samen en duwen de lymfe vooruit",
            "door beweging maakt het lichaam meer lymfocyten, die het vocht opdrinken",
            "door beweging stijgt de bloeddruk, waardoor de lymfe in de aders gaat",
            "door beweging verdampt het overtollige vocht via de huid",
        ],
        0,
        "De spierpomp is de belangrijkste motor van het lymfestelsel. Daarom helpt rustig bewegen het vocht afvoeren.",
    ),
    I(
        "Hoe heten de kleinste lymfevaatjes, die tussen de cellen beginnen en het weefselvocht opnemen?",
        ["lymfecapillairen", "lymfehaarvaten"],
        "Lymfecapillairen beginnen blind tussen de cellen. Ze nemen weefselvocht op en komen samen in steeds grotere lymfevaten.",
    ),
]
