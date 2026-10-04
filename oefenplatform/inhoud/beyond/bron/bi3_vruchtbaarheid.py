# -*- coding: utf-8 -*-
"""Vruchtbaarheid regelen en behandelen — 🌍 Beyond, biologie.

Deel 1 gaat over de methoden om de vruchtbaarheid te regelen: natuurlijk,
barrière, hormonaal, spiraaltjes, sterilisatie en noodanticonceptie, met hun
werking, hun betrouwbaarheid en de vraag of ze tegen soa's beschermen. Deel 2
gaat over de behandeling van vruchtbaarheidsproblemen en over wat de
vruchtbaarheid van een man of een vrouw kan verminderen.

De fiche vraagt bij elke methode de werking, de voor- en nadelen én de
betrouwbaarheid, en ze vraagt uitdrukkelijk welke methoden tegen soa's
beschermen. Dat laatste komt daarom in beide delen terug: het is het punt
waarop leerlingen het vaakst de mis in gaan.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarop berusten de natuurlijke methoden om de vruchtbaarheid te regelen?",
        opties=[
            "op het mijden van de vruchtbare dagen",
            "op het stilleggen van de eisprong met hormonen",
            "op het tegenhouden van de zaadcellen met een vlies",
            "op het doorknippen van de zaadleiders",
        ],
        antwoord=0,
        uitleg="Bij een natuurlijke methode wordt de vruchtbare periode opgespoord en "
        "gemeden. Er komt geen hormoon en geen barrière aan te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke methoden sporen de vruchtbare dagen op? Kruis alles aan wat juist is.",
        opties=[
            "de temperatuurmethode",
            "de ovulatiemethode",
            "de combinatiepil",
            "het koperspiraal",
        ],
        antwoord=[0, 1],
        uitleg="De temperatuurmethode volgt de lichte stijging van de "
        "lichaamstemperatuur na de ovulatie, de ovulatiemethode volgt het slijm van de "
        "baarmoederhals. De kalendermethode rekent met de lengte van de vorige cycli.",
    ),
    dict(
        type="waarofniet",
        vraag="De natuurlijke methoden zijn minder betrouwbaar omdat een cyclus kan verschuiven.",
        antwoord=True,
        uitleg="Ziekte, stress of een onregelmatige cyclus verschuiven de ovulatie. "
        "Daardoor valt de vruchtbare periode anders dan de berekening zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een condoom?",
        opties=[
            "het houdt de zaadcellen tegen",
            "het belet de eisprong",
            "het maakt het slijmvlies ongeschikt",
            "het doodt de eicel",
        ],
        antwoord=0,
        uitleg="Een condoom is een barrièremiddel: het sperma komt niet in de vagina. "
        "Daarmee houdt het ook ziekteverwekkers tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke middelen beschermen ook tegen soa's? Kruis alles aan wat juist is.",
        opties=[
            "het mannencondoom",
            "het vrouwencondoom",
            "de combinatiepil",
            "de temperatuurmethode",
        ],
        antwoord=[0, 1],
        uitleg="Alleen de condooms vormen een echte barrière tussen de slijmvliezen. "
        "Hormonale middelen en spiraaltjes regelen wel de vruchtbaarheid, maar laten "
        "ziekteverwekkers gewoon door.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het kapje dat voor de baarmoederhals geplaatst wordt?",
        antwoord=["pessarium", "diafragma", "een pessarium"],
        uitleg="Het pessarium of diafragma sluit de baarmoederhals af en wordt met een "
        "zaaddodend middel gebruikt. Het beschermt niet tegen soa's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de combinatiepil in het lichaam?",
        opties=[
            "de eisprong tegenhouden met oestrogeen en progestageen",
            "de zaadcellen in de vagina doden",
            "de bevruchte eicel uit de baarmoeder verwijderen",
            "het slijm van de baarmoederhals dunner maken",
        ],
        antwoord=0,
        uitleg="De pil houdt het hormoonpeil kunstmatig hoog. De hypofyse geeft daardoor "
        "geen LH-piek meer, en zonder LH-piek geen ovulatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke middelen werken met hormonen? Kruis alles aan wat juist is.",
        opties=[
            "de hormoonpleister",
            "de prikpil",
            "het koperspiraal",
            "het pessarium",
        ],
        antwoord=[0, 1],
        uitleg="Pleister, vaginale ring, prikpil, implantaat, minipil en hormoonspiraal "
        "geven alle een hormoon af. Het koperspiraal en het pessarium doen dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een koperspiraal en een hormoonspiraal?",
        opties=[
            "het koperspiraal werkt zonder hormoon",
            "het koperspiraal zit buiten het lichaam",
            "het hormoonspiraal beschermt tegen soa's",
            "het hormoonspiraal blijft maar één cyclus zitten",
        ],
        antwoord=0,
        uitleg="Koper maakt de baarmoeder ongeschikt voor zaadcellen en innesteling. Een "
        "hormoonspiraal geeft daarbovenop een progestageen af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de ingreep waarbij bij een man de zaadleiders doorgeknipt worden?",
        antwoord=["sterilisatie", "vasectomie", "de sterilisatie"],
        uitleg="Bij een man worden de zaadleiders onderbroken, bij een vrouw de "
        "eileiders. Een sterilisatie is bedoeld als blijvend en dus niet zomaar om te "
        "keren.",
    ),
    dict(
        type="waarofniet",
        vraag="Na een sterilisatie bij een man maakt hij geen testosteron meer aan.",
        antwoord=False,
        uitleg="De cellen van Leydig blijven testosteron maken. Alleen de weg van de "
        "zaadcellen naar buiten is onderbroken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is noodanticonceptie?",
        opties=[
            "een middel na onbeschermd vrijen",
            "een middel dat elke dag genomen wordt",
            "een middel dat tegen soa's beschermt",
            "een middel dat de vruchtbaarheid verhoogt",
        ],
        antwoord=0,
        uitleg="De morning-afterpil en het noodspiraaltje worden achteraf gebruikt, zo "
        "snel mogelijk. Ze zijn bedoeld voor een uitzondering, niet als vaste methode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de morning-afterpil vooral?",
        opties=[
            "door de ovulatie uit te stellen",
            "door een ingenestelde vrucht af te breken",
            "door de zaadcellen in de vagina te doden",
            "door het baarmoederslijmvlies dikker te maken",
        ],
        antwoord=0,
        uitleg="Ze stelt de eisprong uit of houdt hem tegen, en werkt dus beter naarmate "
        "ze sneller genomen wordt. De abortuspil werkt anders: die beëindigt een "
        "bestaande zwangerschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zaaddodend middel is alleen betrouwbaar als het samen met een barrièremiddel gebruikt wordt.",
        antwoord=True,
        uitleg="Alleen gebruikt is een zaaddodend middel weinig betrouwbaar. Samen met "
        "een pessarium of een condoom vult het de bescherming aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zegt men bij een methode altijd hoe betrouwbaar ze is?",
        opties=[
            "omdat verkeerd gebruik de betrouwbaarheid verlaagt",
            "omdat elke methode even betrouwbaar is",
            "omdat de betrouwbaarheid niet te meten is",
            "omdat de betrouwbaarheid van het weer afhangt",
        ],
        antwoord=0,
        uitleg="Er is een verschil tussen het ideale gebruik en het werkelijke gebruik. "
        "Een pil die een dag vergeten wordt, is minder betrouwbaar dan de cijfers op de "
        "bijsluiter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het hormoon dat de eisprong uitlokt en dat de pil onderdrukt?",
        antwoord=["LH", "luteïniserend hormoon", "lh"],
        uitleg="De LH-piek laat de Graafse follikel springen. Zonder die piek komt er "
        "geen eicel vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vrouwencondoom regelt de vruchtbaarheid, maar beschermt niet tegen soa's.",
        antwoord=False,
        uitleg="Het vrouwencondoom bekleedt de vaginawand en bedekt ook een stukje "
        "eromheen. Daardoor beschermt het, net als het mannencondoom, wel tegen soa's.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon zit er in de minipil, naast geen oestrogeen?",
        antwoord=["progestageen", "progesteron", "een progestageen"],
        uitleg="De minipil bevat alleen een progestageen. Daardoor kan ze gebruikt worden "
        "als oestrogeen niet mag, maar ze moet wel heel regelmatig genomen worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voordeel heeft een hormoonimplantaat tegenover de pil?",
        opties=[
            "het werkt jaren zonder dagelijkse inname",
            "het beschermt ook tegen soa's",
            "het kan elke dag weggelaten worden",
            "het werkt zonder enig hormoon",
        ],
        antwoord=0,
        uitleg="Een staafje onder de huid van de bovenarm geeft jarenlang een "
        "progestageen af. Er is dus niets dagelijks te onthouden, en dat verhoogt de "
        "betrouwbaarheid in de praktijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nadeel van een spiraaltje?",
        opties=[
            "het moet door een arts geplaatst worden",
            "het moet elke dag ingenomen worden",
            "het werkt maar één dag",
            "het belet de eisprong nooit",
        ],
        antwoord=0,
        uitleg="Het plaatsen en verwijderen gebeurt bij een arts en kan pijnlijk zijn. "
        "Daarna werkt het wel jaren zonder dat er iets te onthouden valt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij kunstmatige inseminatie?",
        opties=[
            "sperma wordt in de baarmoeder gebracht",
            "een eicel wordt buiten het lichaam bevrucht",
            "een eicel wordt bij een donor weggenomen",
            "een embryo wordt in de eileider gelegd",
        ],
        antwoord=0,
        uitleg="Bij inseminatie wordt het sperma rechtstreeks ingebracht, rond de "
        "ovulatie. De bevruchting gebeurt dus nog in het lichaam zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent KID tegenover KI?",
        opties=[
            "het sperma komt van een donor",
            "de eicel komt van een donor",
            "de bevruchting gebeurt in een schaaltje",
            "er wordt één zaadcel ingespoten",
        ],
        antwoord=0,
        uitleg="KI gebruikt sperma van de partner, KID dat van een donor. Daar wordt voor "
        "gekozen als de partner geen bruikbare zaadcellen heeft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de techniek waarbij eicel en zaadcellen buiten het lichaam samengebracht worden?",
        antwoord=["ivf", "in-vitrofertilisatie", "IVF"],
        uitleg="Bij in-vitrofertilisatie gebeurt de bevruchting in een schaaltje in het "
        "labo. Daarna wordt een embryo in de baarmoeder geplaatst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen IVF en ICSI?",
        opties=[
            "bij ICSI wordt één zaadcel in de eicel gespoten",
            "bij ICSI gebeurt alles in het lichaam zelf",
            "bij ICSI wordt er geen eicel gebruikt",
            "bij ICSI is er geen hormonale stimulatie nodig",
        ],
        antwoord=0,
        uitleg="Bij IVF moeten de zaadcellen zelf binnendringen, bij ICSI wordt er één "
        "met een naald ingebracht. ICSI helpt dus als de zaadcellen te traag of te weinig "
        "beweeglijk zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor een IVF-behandeling worden de eierstokken hormonaal gestimuleerd.",
        antwoord=True,
        uitleg="Met hormonen rijpen er meerdere follikels in plaats van één. Zo zijn er "
        "meerdere eicellen te oogsten in één cyclus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is in-vitromaturatie?",
        opties=[
            "onrijpe eicellen buiten het lichaam laten rijpen",
            "sperma buiten het lichaam laten rijpen",
            "een embryo langer in het labo houden",
            "de baarmoeder op de innesteling voorbereiden",
        ],
        antwoord=0,
        uitleg="Bij IVM worden onrijpe eicellen geoogst en pas in het labo verder "
        "gerijpt. Dat vraagt minder of geen hormonale stimulatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer komt eiceldonatie in beeld?",
        opties=[
            "als de vrouw zelf geen bruikbare eicellen heeft",
            "als de man geen bruikbare zaadcellen heeft",
            "als de baarmoeder te klein is",
            "als het koppel een tweeling wil",
        ],
        antwoord=0,
        uitleg="Een donoreicel wordt met het sperma van de partner bevrucht via IVF. Het "
        "embryo wordt daarna bij de wensmoeder geplaatst.",
    ),
    dict(
        type="invultekst",
        vraag="Welk onderzoek bij een man kijkt naar het aantal, de vorm en de beweeglijkheid van de zaadcellen?",
        antwoord=["spermaonderzoek", "een spermaonderzoek", "spermogram"],
        uitleg="Een spermastaal laat zien of er genoeg goed gebouwde en beweeglijke "
        "zaadcellen zijn. Daarmee wordt beslist of IVF volstaat of ICSI nodig is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gedrag verlaagt de vruchtbaarheid van een man? Kruis alles aan wat juist is.",
        opties=[
            "roken",
            "veel alcohol drinken",
            "regelmatig matig bewegen",
            "voldoende slapen",
        ],
        antwoord=[0, 1],
        uitleg="Roken, alcohol en drugs verminderen het aantal en de kwaliteit van de "
        "zaadcellen. Bewegen en slapen werken juist de goede kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="Alleen de leeftijd van de vrouw speelt een rol bij de vruchtbaarheid van een koppel.",
        antwoord=False,
        uitleg="Bij een vrouw daalt het aantal en de kwaliteit van de eicellen sneller, "
        "maar ook bij een man neemt de kwaliteit van het sperma met de jaren af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan overgewicht de vruchtbaarheid verlagen?",
        opties=[
            "het verstoort het hormonale evenwicht",
            "het verkleint de baarmoeder",
            "het sluit de eileiders af",
            "het verandert de bloedgroep",
        ],
        antwoord=0,
        uitleg="Vetweefsel maakt zelf hormonen aan en verstoort zo de cyclus en de "
        "spermaproductie. Dat geldt bij mannen en bij vrouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een kankerbehandeling de vruchtbaarheid aantasten?",
        opties=[
            "ze raakt ook de snel delende geslachtscellen",
            "ze verhoogt het testosteronpeil te sterk",
            "ze verdikt het baarmoederslijmvlies",
            "ze maakt het sperma te vloeibaar",
        ],
        antwoord=0,
        uitleg="Chemotherapie en bestraling treffen snel delende cellen, en dat zijn ook "
        "de cellen van de gametogenese. Daarom wordt er soms vooraf sperma of "
        "eierstokweefsel bewaard.",
    ),
    dict(
        type="waarofniet",
        vraag="Langdurige stress kan de cyclus van een vrouw verstoren.",
        antwoord=True,
        uitleg="Stresshormonen grijpen in op de hypothalamus en de hypofyse. Daardoor kan "
        "de ovulatie verschuiven of helemaal uitblijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloeden van buitenaf kunnen de vruchtbaarheid verlagen? Kruis alles aan wat juist is.",
        opties=[
            "zware metalen",
            "bepaalde medicijnen",
            "water uit de kraan",
            "zuurstof in de lucht",
        ],
        antwoord=[0, 1],
        uitleg="Zware metalen, sommige medicijnen, pesticiden en hormoonverstoorders "
        "grijpen in op de hormonen of op de gameten zelf. Water en zuurstof doen dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangen de teelballen buiten het lichaam?",
        opties=[
            "zaadcellen rijpen bij een lagere temperatuur",
            "zaadcellen hebben meer zuurstof nodig",
            "zaadcellen moeten sneller naar buiten kunnen",
            "zaadcellen worden daar door hormonen bereikt",
        ],
        antwoord=0,
        uitleg="De spermatogenese verloopt het best enkele graden onder de "
        "lichaamstemperatuur. Daarom verlaagt langdurige warmte, zoals een hete bad of een "
        "laptop op de schoot, de kwaliteit van het sperma.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel chromosomen zitten er in een gezonde menselijke zaadcel?",
        antwoord=["23", "drieëntwintig"],
        uitleg="Een gameet is haploïd: 23 chromosomen. Bij de bevruchting komt het aantal "
        "weer op 46.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vruchtbaarheidsbehandeling lukt altijd vanaf de eerste poging.",
        antwoord=False,
        uitleg="De kans per poging ligt duidelijk onder de helft en daalt met de leeftijd. "
        "Daarom zijn er meestal meerdere pogingen nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden bij een IVF-behandeling meestal niet alle embryo's tegelijk geplaatst?",
        opties=[
            "om een meerlingzwangerschap te vermijden",
            "omdat embryo's niet bewaard kunnen worden",
            "omdat de baarmoeder er maar één aankan per jaar",
            "omdat er anders geen hormonen genoeg zijn",
        ],
        antwoord=0,
        uitleg="Meerdere embryo's tegelijk verhogen de kans op een tweeling of drieling, "
        "en dat geeft meer risico. De overige embryo's worden ingevroren voor een volgende "
        "poging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de morning-afterpil en de abortuspil?",
        opties=[
            "de eerste voorkomt, de tweede beëindigt een zwangerschap",
            "de eerste beëindigt, de tweede voorkomt een zwangerschap",
            "ze doen precies hetzelfde",
            "de eerste werkt met koper, de tweede met een hormoon",
        ],
        antwoord=0,
        uitleg="De morning-afterpil stelt de ovulatie uit en werkt dus voor er een "
        "zwangerschap is. De abortuspil breekt een bestaande zwangerschap af en gebeurt "
        "onder medisch toezicht.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stoffen in ons milieu lijken op hormonen en kunnen daardoor de vruchtbaarheid storen?",
        antwoord=["hormoonverstoorders", "hormoonverstorende stoffen"],
        uitleg="Hormoonverstoorders binden op dezelfde receptoren als echte hormonen. "
        "Daardoor sturen ze de cyclus of de spermaproductie de verkeerde kant op.",
    ),
]
