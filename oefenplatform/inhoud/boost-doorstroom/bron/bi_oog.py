# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Het oog.

Hoort bij "waarnemen en verwerken van prikkels" van de vakfiche biologie
2de graad doorstroomfinaliteit.

Deel 1 gaat over de bouw van het oog en over de weg die het licht aflegt tot
op het netvlies: hoornvlies, pupil, iris, lens, kamervocht, glasachtig
lichaam, vaatvlies, harde oogvlies. Deel 2 gaat over het netvlies zelf
(staafjes, kegeltjes, gele vlek, blinde vlek), over accommodatie en de
pupilreflex, en over de afwijkingen die de fiche opsomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Door welk doorzichtig deel komt het licht het oog binnen?",
        opties=[
            "het hoornvlies",
            "het vaatvlies",
            "het harde oogvlies",
            "het netvlies",
        ],
        antwoord=0,
        uitleg="Het hoornvlies is het doorzichtige voorste stukje van de buitenste laag. Het buigt het licht ook al een eerste keer af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de weg van het licht door het oog in de juiste orde.",
        opties=[
            "hoornvlies, pupil, lens, glasachtig lichaam, netvlies",
            "netvlies, lens, pupil, hoornvlies, glasachtig lichaam",
            "pupil, hoornvlies, netvlies, lens, glasachtig lichaam",
            "lens, hoornvlies, glasachtig lichaam, pupil, netvlies",
        ],
        antwoord=0,
        uitleg="Eerst het hoornvlies, dan de opening in de iris, dan de lens, dan de geleiachtige ruimte, en helemaal achteraan het netvlies.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de opening in het midden van de iris waar het licht door gaat?",
        antwoord=["pupil", "de pupil"],
        uitleg="De pupil is geen structuur maar een opening. Hij ziet zwart omdat het licht dat erin valt, niet meer terugkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van de iris of het regenboogvlies?",
        opties=[
            "de hoeveelheid licht regelen die het oog binnenkomt",
            "het licht scherp op het netvlies laten vallen",
            "de prikkels van het netvlies naar de hersenen brengen",
            "het oog van voedingsstoffen en zuurstof voorzien",
        ],
        antwoord=0,
        uitleg="De iris is een ringvormig spiertje. Trekt het samen, dan wordt de pupil kleiner en komt er minder licht binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="De kleur van iemands ogen is de kleur van de iris.",
        antwoord=True,
        uitleg="Blauwe, groene of bruine ogen hebben te maken met de hoeveelheid pigment in de iris. De pupil erin blijft bij iedereen zwart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen vormen samen de wand van de oogbol? Kruis alles aan wat juist is.",
        opties=[
            "het harde oogvlies",
            "het vaatvlies",
            "het netvlies",
            "het glasachtig lichaam",
        ],
        antwoord=[0, 1, 2],
        uitleg="Van buiten naar binnen: harde oogvlies, vaatvlies, netvlies. Het glasachtig lichaam is geen laag van de wand maar de vulling binnenin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het harde oogvlies of de sclera?",
        opties=[
            "het geeft de oogbol zijn vorm en beschermt hem",
            "het vangt het licht op en zet het om in zenuwimpulsen",
            "het voorziet het netvlies van bloed en zuurstof",
            "het stelt het oog scherp op een voorwerp dichtbij",
        ],
        antwoord=0,
        uitleg="De sclera is de stevige witte buitenlaag, het wit van het oog. Zij houdt de bol in vorm en beschermt wat erin ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van het vaatvlies?",
        opties=[
            "het netvlies van bloed voorzien en strooilicht wegnemen",
            "de lens van vorm doen veranderen bij het scherpstellen",
            "het oog vochtig houden met tranen",
            "de oogbol in zijn kas doen draaien",
        ],
        antwoord=0,
        uitleg="Het vaatvlies ligt vol bloedvaten en is donker gepigmenteerd. Zo voedt het het netvlies en slikt het het licht op dat erdoor komt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de doorzichtige gelei die de ruimte achter de lens opvult?",
        antwoord=["glasachtig lichaam", "het glasachtig lichaam", "glasvocht"],
        uitleg="Het glasachtig lichaam houdt de oogbol van binnenuit op spanning en laat tegelijk het licht door naar het netvlies.",
    ),
    dict(
        type="waarofniet",
        vraag="Het kamervocht vult de hele ruimte achter de lens tot aan het netvlies.",
        antwoord=False,
        uitleg="Die ruimte is met het glasachtig lichaam gevuld. Het kamervocht zit net vóór de lens, in de voorste oogkamer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft het hoornvlies geen bloedvaten?",
        opties=[
            "bloedvaten zouden het licht tegenhouden en het zicht wazig maken",
            "het hoornvlies heeft geen voeding en geen zuurstof nodig",
            "bloedvaten passen niet in zo'n dunne laag",
            "het hoornvlies krijgt zijn voeding uit de tranen alleen",
        ],
        antwoord=0,
        uitleg="Het hoornvlies moet volkomen doorzichtig blijven, dus mogen er geen vaten door. Het haalt zijn voeding uit het kamervocht en de tranen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen buigen het licht af zodat het op het netvlies samenkomt? Kruis alles aan wat juist is.",
        opties=[
            "het hoornvlies",
            "de lens",
            "het kamervocht",
            "de iris",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hoornvlies, kamervocht en lens zijn doorzichtig en buigen het licht. De iris laat licht alleen door of houdt het tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="De lens van het oog is bolvormig en kan haar vorm niet veranderen.",
        antwoord=False,
        uitleg="De lens is elastisch en wordt boller of platter. Net daardoor kan je scherpstellen op dichtbij en op verre dingen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het veranderen van de vorm van de lens om scherp te stellen?",
        antwoord=["accommodatie", "accomodatie", "de accommodatie"],
        uitleg="Bij accommodatie trekt het kringspiertje rond de lens samen, waardoor de lens boller wordt. Zo zie je iets dichtbij scherp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kijkt van je blad op naar de bomen in de verte. Wat gebeurt er met je lens?",
        opties=[
            "ze wordt platter, want voor ver kijken moet het licht minder gebogen worden",
            "ze wordt boller, want voor ver kijken moet het licht sterker gebogen worden",
            "ze schuift naar voren tot tegen de iris aan",
            "ze blijft net dezelfde vorm houden en het netvlies schuift mee",
        ],
        antwoord=0,
        uitleg="Licht van ver valt bijna recht binnen en hoeft dus weinig gebogen te worden. De lens ontspant en wordt platter.",
    ),
    dict(
        type="waarofniet",
        vraag="Het beeld dat op het netvlies valt, staat op zijn kop.",
        antwoord=True,
        uitleg="De lens keert het beeld om, zowel boven-onder als links-rechts. De hersenen zetten het weer recht bij de verwerking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke spieren laten de oogbol in zijn kas draaien?",
        opties=[
            "de uitwendige oogspieren",
            "het kringspiertje rond de lens",
            "de spiertjes van de iris",
            "de spieren van het ooglid",
        ],
        antwoord=0,
        uitleg="Rond elke oogbol liggen zes uitwendige oogspieren. Zij draaien het oog zodat beide ogen op hetzelfde punt gericht blijven.",
    ),
    dict(
        type="waarofniet",
        vraag="Het oog werkt als een camera: een opening regelt het licht en een lens stelt scherp op een gevoelig oppervlak.",
        antwoord=True,
        uitleg="De pupil is het diafragma, de lens het objectief en het netvlies de sensor. Een camera stelt wel scherp door de lens te verschuiven, en het oog door haar van vorm te veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom knippert een oog een paar keer per minuut?",
        opties=[
            "om het tranenvocht gelijk over het hoornvlies te verdelen",
            "om de lens opnieuw op haar plaats te duwen",
            "om het netvlies even rust te geven van het licht",
            "om het kamervocht door de voorste kamer te laten stromen",
        ],
        antwoord=0,
        uitleg="Knipperen strijkt een vers laagje tranenvocht over het oog. Dat houdt het hoornvlies vochtig en spoelt stof weg.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stevige witte buitenlaag van de oogbol?",
        antwoord=["harde oogvlies", "het harde oogvlies", "sclera"],
        uitleg="Het harde oogvlies of de sclera is het wit dat je naast de iris ziet. Vooraan gaat het over in het doorzichtige hoornvlies.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten lichtgevoelige cellen liggen in het netvlies?",
        opties=[
            "staafjes en kegeltjes",
            "sluitcellen en wortelharen",
            "alfacellen en bètacellen",
            "neuronen en cellen van Schwann",
        ],
        antwoord=0,
        uitleg="Staafjes en kegeltjes zijn de fotoreceptoren van het oog. Elk soort heeft zijn eigen taak in het zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de staafjes? Kruis alles aan wat juist is.",
        opties=[
            "ze werken ook bij weinig licht",
            "ze geven geen kleur door",
            "ze liggen vooral buiten het midden van het netvlies",
            "ze geven het scherpste beeld van het hele netvlies",
        ],
        antwoord=[0, 1, 2],
        uitleg="Staafjes zijn gevoelig maar zien grijs, en liggen vooral aan de zijkant. Het scherpste beeld komt van de kegeltjes in de gele vlek.",
    ),
    dict(
        type="invultekst",
        vraag="Welke lichtgevoelige cellen in het netvlies laten je kleuren zien?",
        antwoord=["kegeltjes", "de kegeltjes", "kegeltje"],
        uitleg="Er zijn drie soorten kegeltjes, elk gevoelig voor een ander deel van het licht. Samen laten ze je alle kleuren onderscheiden.",
    ),
    dict(
        type="waarofniet",
        vraag="In het halfduister zie je nauwelijks kleuren omdat dan vooral de staafjes werken.",
        antwoord=True,
        uitleg="Kegeltjes hebben veel licht nodig. Valt het licht weg, dan nemen de staafjes over en wordt alles grijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de gele vlek?",
        opties=[
            "de plaats op het netvlies met de meeste kegeltjes, waar je het scherpst ziet",
            "de plaats waar de oogzenuw het netvlies verlaat en naar de hersenen loopt",
            "het pigment dat het vaatvlies zijn donkere kleur geeft en strooilicht wegneemt",
            "het vlekje tranenvocht dat na het knipperen op het hoornvlies achterblijft",
        ],
        antwoord=0,
        uitleg="De gele vlek ligt recht tegenover de pupil en zit volgepakt met kegeltjes. Daar kijk je naar wanneer je iets aandachtig bekijkt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de plaats waar de oogzenuw het netvlies verlaat en er geen lichtgevoelige cellen zijn?",
        antwoord=["blinde vlek", "de blinde vlek"],
        uitleg="Daar lopen alle zenuwvezels samen naar buiten, dus is er geen plaats voor staafjes of kegeltjes. Op die plek zie je niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom merk je in het dagelijks leven niets van je blinde vlek?",
        opties=[
            "het andere oog ziet dat stukje wel, en de hersenen vullen de rest aan",
            "de blinde vlek ligt zo klein dat er nooit licht op valt",
            "de oogzenuw geeft dat stukje van het beeld toch door",
            "de blinde vlek bestaat enkel bij mensen met een oogafwijking",
        ],
        antwoord=0,
        uitleg="De twee ogen hebben hun blinde vlek niet op dezelfde plaats in het beeld. Daarbij vullen de hersenen het gat aan met wat eromheen ligt.",
    ),
    dict(
        type="waarofniet",
        vraag="De oogzenuw brengt de impulsen van het netvlies naar de hersenen.",
        antwoord=True,
        uitleg="De staafjes en kegeltjes zetten licht om in zenuwimpulsen, en de oogzenuw voert die naar het achterste deel van de grote hersenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij de pupilreflex als je van een donkere kamer naar buiten in de zon stapt?",
        opties=[
            "de iris trekt samen en de pupil wordt kleiner",
            "de iris ontspant en de pupil wordt groter",
            "de lens wordt boller zodat er minder licht doorkomt",
            "het netvlies schuift naar achteren om het licht te ontwijken",
        ],
        antwoord=0,
        uitleg="Veel licht laat de kringspier van de iris samentrekken. De pupil vernauwt en zo wordt het netvlies beschermd.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan de grootte van je pupil met je wil regelen.",
        antwoord=False,
        uitleg="De pupilreflex loopt buiten je wil om. Je kan er niet voor kiezen je pupil wijder te zetten, ook niet met oefening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand ziet dichtbij scherp maar ver weg wazig. Wat is er aan de hand?",
        opties=[
            "de oogbol is te lang of de lens buigt te sterk, dus valt het beeld voor het netvlies",
            "de oogbol is te kort of de lens buigt te zwak, dus valt het beeld achter het netvlies",
            "de gele vlek heeft te weinig kegeltjes om een scherp beeld te vormen",
            "het hoornvlies is in de ene richting anders gekromd dan in de andere",
        ],
        antwoord=0,
        uitleg="Dat is bijziendheid. Het licht komt al samen voor het netvlies bereikt is, dus is het beeld daar weer uiteengelopen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de afwijking waarbij je ver weg scherp ziet maar dichtbij wazig?",
        antwoord=["verziendheid", "verziend", "hypermetropie"],
        uitleg="Bij verziendheid is de oogbol te kort of de lens te zwak, zodat het beeld pas achter het netvlies samenkomt. Een bolle lens in een bril helpt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lens corrigeert bijziendheid?",
        opties=[
            "een holle lens, die het licht wat uiteen laat gaan",
            "een bolle lens, die het licht extra samenbrengt",
            "een gekleurde lens, die een deel van het licht wegneemt",
            "een cilindrische lens, die in één richting anders buigt",
        ],
        antwoord=0,
        uitleg="Bij bijziendheid komt het licht te vroeg samen, dus moet je het eerst wat spreiden. Dat doet een holle of negatieve lens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is ouderdomsverziendheid?",
        opties=[
            "de lens wordt met de jaren stijver, waardoor accommoderen moeilijker wordt",
            "het netvlies verliest met de jaren al zijn staafjes aan de zijkanten",
            "de pupil kan met de jaren niet meer vernauwen bij fel zonlicht",
            "de oogzenuw wordt met de jaren steeds korter en trekt aan het netvlies",
        ],
        antwoord=0,
        uitleg="Een stijve lens wordt niet meer goed bol, dus lukt dichtbij scherpstellen minder. Daarom houden mensen hun boek verder weg of nemen ze een leesbril.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij kleurenblindheid werken een of meer soorten kegeltjes niet goed.",
        antwoord=True,
        uitleg="Vaak gaat het om de kegeltjes voor rood of groen. Die kleuren zijn dan moeilijk van elkaar te onderscheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is astigmatisme?",
        opties=[
            "het hoornvlies of de lens is onregelmatig gekromd, waardoor lijnen vervormen",
            "de pupil blijft altijd even groot, ook in het donker en in de volle zon",
            "het netvlies laat op één plek los van het vaatvlies dat eronder ligt",
            "de twee ogen kijken niet in dezelfde richting en zien elk iets anders",
        ],
        antwoord=0,
        uitleg="Bij astigmatisme buigt het hoornvlies in de ene richting anders dan in de andere. Een cilindrische lens in de bril maakt dat weer gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bril met de verkeerde sterkte beschadigt het netvlies blijvend.",
        antwoord=False,
        uitleg="Je ziet er wazig door en kan er hoofdpijn van krijgen, maar het netvlies raakt er niet beschadigd van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zie je met twee ogen diepte en met één oog veel minder?",
        opties=[
            "elk oog ziet het voorwerp vanuit een iets andere hoek en de hersenen leggen die beelden samen",
            "elk oog ziet een andere kleur en uit die twee kleuren samen halen de hersenen de afstand",
            "het ene oog ziet scherp en het andere ziet wazig, en dat verschil verraadt de afstand",
            "met twee ogen valt er twee keer zoveel licht op elk netvlies, dus zie je meer detail",
        ],
        antwoord=0,
        uitleg="Je ogen staan een stukje van elkaar, dus zien ze niet precies hetzelfde. Uit dat kleine verschil halen de hersenen de afstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij het omzetten van licht in een waarneming? Kruis alles aan wat juist is.",
        opties=[
            "het licht valt op een staafje of kegeltje in het netvlies",
            "die cel wekt een zenuwimpuls op",
            "de oogzenuw brengt de impuls naar de hersenen",
            "de iris zet de impuls om in een beeld",
        ],
        antwoord=[0, 1, 2],
        uitleg="Opvangen, omzetten, doorgeven en in de hersenen verwerken. De iris doet daar niet aan mee; die regelt enkel het licht.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat je uiteindelijk ziet, ligt al helemaal vast op het netvlies.",
        antwoord=False,
        uitleg="De hersenen zetten het beeld recht, vullen de blinde vlek aan en koppelen wat je ziet aan wat je al kent. Zien is dus ook verwerken.",
    ),
]
