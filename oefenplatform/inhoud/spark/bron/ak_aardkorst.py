# -*- coding: utf-8 -*-
"""De vragen voor "De aarde beweegt en slijt" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "veranderingen in het landschap"
(40 % van het examen, samen met [[ak_weer]], [[ak_klimaat]] en [[ak_mens]]).

Deel 1 gaat over aardbevingen en vulkaanuitbarstingen, en over wat die op korte
en op lange termijn met een landschap doen.
Deel 2 gaat over de drie processen die het reliëf langzaam bijschaven:
verwering of afbraak, erosie of wegvoeren, en sedimentatie of afzetten, telkens
door wind, door water en door ijs.

Het onderscheid tussen die drie processen is waar kinderen op vastlopen, en het
examen vraagt er uitdrukkelijk naar. Verwering is afbreken ter plaatse, erosie
is het losse materiaal meenemen, sedimentatie is het ergens anders laten vallen.
Elke vraag hierover blijft bij die volgorde.

Voorbeelden van plaatsen worden alleen gebruikt waar ze algemeen gekend zijn
(de Vesuvius boven Pompeii, IJsland op de grens van twee platen). Wie er een
voorbeeld bij schrijft, kiest er een dat in elke schoolatlas staat.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="In een streek staat op een ochtend een laag grijze as over de velden en de daken. Wat is daar gebeurd?",
        opties=[
            "Een vulkaan in de buurt is uitgebarsten",
            "Er is een zware storm overgetrokken",
            "De bodem is er aan het uitdrogen",
            "Een rivier is er buiten haar oevers getreden",
        ],
        antwoord=0,
        uitleg="Bij een uitbarsting schiet er as de lucht in, die daarna kilometers ver neerdaalt. Een storm of een overstroming laat heel andere sporen na.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waardoor ontstaat een aardbeving?",
        opties=[
            "Door plotse beweging van stukken aardkorst",
            "Door de druk van het water in de oceanen",
            "Door de warmte van de zon op het oppervlak",
            "Door de zwaarte van gebergten op de bodem",
        ],
        antwoord=0,
        uitleg="De aardkorst bestaat uit platen die traag tegen elkaar schuiven. Blijft de spanning ergens haken en schiet ze dan los, dan schokt de grond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men het punt op het aardoppervlak recht boven de plaats waar een aardbeving ontstaat?",
        opties=[
            "Het epicentrum",
            "De krater",
            "De breuklijn",
            "De magnitude",
        ],
        antwoord=0,
        uitleg="De beving zelf ontstaat dieper in de aarde, in de haard. Het punt daar recht boven aan de oppervlakte is het epicentrum, en daar zijn de schokken het hevigst.",
    ),
    dict(
        type="invultekst",
        vraag="Het toestel dat de trillingen van een aardbeving opmeet en optekent, heet een ___.",
        antwoord="seismograaf",
        uitleg="Een seismograaf tekent de trillingen als een golvende lijn. Uit die metingen leiden wetenschappers af hoe zwaar de beving was en waar ze ontstond.",
    ),
    dict(
        type="waarofniet",
        vraag="In België komen af en toe lichte aardbevingen voor.",
        antwoord=True,
        uitleg="Zware bevingen kent ons land niet, maar lichte schokken worden er wel degelijk gemeten, vooral in het oosten. Meestal merk je er nauwelijks iets van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan een zware aardbeving op zee veroorzaken?",
        opties=[
            "Een vloedgolf die de kust overspoelt",
            "Een lange periode van droogte aan land",
            "Een plotse daling van de zeespiegel wereldwijd",
            "Een blijvende verandering van de zeestromingen",
        ],
        antwoord=0,
        uitleg="Een beving op de zeebodem duwt een enorme hoeveelheid water omhoog. Die golf, een tsunami, kan uren later een kust ver weg treffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen magma en lava?",
        opties=[
            "Magma zit onder de grond, lava stroomt erbovenop",
            "Magma is vloeibaar en lava is altijd vast",
            "Magma is koud gesteente en lava is warm gesteente",
            "Magma komt uit de zee en lava uit het land",
        ],
        antwoord=0,
        uitleg="Het is hetzelfde gesmolten gesteente, maar het krijgt een andere naam zodra het naar buiten komt. Onder de grond magma, aan het oppervlak lava.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan er bij een vulkaanuitbarsting naar buiten komen? Er zijn er meerdere juist.",
        opties=[
            "Lava",
            "As",
            "Gassen",
            "Grondwater uit de diepte",
            "Zeewater uit de oceaan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een uitbarsting spuwt gesmolten gesteente, as en gassen uit. Grond- en zeewater komen er niet uit; wel kan water dat in aanraking komt met magma explosief verdampen.",
    ),
    dict(
        type="invultekst",
        vraag="De trechtervormige opening bovenaan een vulkaan heet de ___.",
        antwoord="krater",
        uitleg="Door de krater komen lava, as en gassen naar buiten. Stort de top na een zware uitbarsting in, dan ontstaat er een veel bredere caldera.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen brengt een vulkaanuitbarsting op korte termijn? Er zijn er meerdere juist.",
        opties=[
            "Huizen en akkers verdwijnen onder lava en as",
            "Mensen moeten hun dorp in allerijl verlaten",
            "De lucht raakt gevuld met as en met gassen",
            "De bodem wordt er stilaan een stuk vruchtbaarder",
            "Er groeit na verloop van tijd een nieuw bos op",
        ],
        antwoord=[0, 1, 2],
        uitleg="Op korte termijn is een uitbarsting vernietigend: bedelven, vluchten, een lucht vol as. Een vruchtbare bodem en nieuw bos komen pas jaren later.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verandering brengt een vulkaan op lange termijn?",
        opties=[
            "De bodem wordt er bijzonder vruchtbaar",
            "De streek wordt er onbewoonbaar voor altijd",
            "Er kan daarna nooit meer een uitbarsting komen",
            "Het klimaat van het werelddeel wordt er warmer",
        ],
        antwoord=0,
        uitleg="Vulkanische as zit vol mineralen. Daarom liggen er op de hellingen van actieve vulkanen vaak akkers en dorpen, ondanks het gevaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Mensen gaan nooit wonen in de buurt van een actieve vulkaan.",
        antwoord=False,
        uitleg="Toch wel, en met miljoenen. De grond is er vruchtbaar en het land is er goedkoop, en veel mensen hebben er ook gewoon geen alternatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stad werd in het jaar 79 bedolven door de Vesuvius?",
        opties=[
            "Pompeii",
            "Rome",
            "Napels",
            "Athene",
        ],
        antwoord=0,
        uitleg="Pompeii verdween onder een dikke laag as. Juist daardoor bleef de stad zo goed bewaard dat archeologen ze eeuwen later konden opgraven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen er op IJsland zoveel vulkanen?",
        opties=[
            "Omdat het eiland op de grens van twee platen ligt",
            "Omdat het eiland zo dicht bij de noordpool ligt",
            "Omdat er zoveel gletsjers op het eiland liggen",
            "Omdat het eiland volledig uit zand bestaat",
        ],
        antwoord=0,
        uitleg="Op een plaats waar twee platen uit elkaar bewegen, kan magma gemakkelijk naar boven. IJsland ligt precies op zo'n grens, midden in de Atlantische Oceaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over aardbevingen kloppen? Er zijn er meerdere juist.",
        opties=[
            "Ze duren meestal maar enkele seconden",
            "Ze komen vaker voor langs de randen van platen",
            "Ze kunnen gebouwen doen instorten",
            "Ze worden aangekondigd enkele dagen vooraf",
            "Ze komen alleen op het land voor, nooit op zee",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een beving duurt kort, treft vooral plaatsgrenzen en kan zware schade aanrichten. Voorspellen op dagen vooraf lukt niet, en op zee gebeuren ze evengoed.",
    ),
    dict(
        type="waarofniet",
        vraag="Een landschap kan door een uitbarsting in enkele dagen sterker veranderen dan door erosie in duizend jaar.",
        antwoord=True,
        uitleg="Dat is het verschil tussen snelle en trage verandering. Een uitbarsting of een beving werkt in uren, verwering en erosie doen er eeuwen over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een breuklijn?",
        opties=[
            "Een scheur in de aardkorst waarlangs stukken bewegen",
            "De grens tussen twee landen zoals ze op de wereldkaart staat",
            "De lijn waar een rivier in de zee uitmondt",
            "De rand van een krater na een uitbarsting",
        ],
        antwoord=0,
        uitleg="Langs een breuklijn schuiven blokken aardkorst langs elkaar. Juist daar komen aardbevingen het vaakst voor.",
    ),
    dict(
        type="invultekst",
        vraag="Een reusachtige vloedgolf na een zeebeving noemt men een ___.",
        antwoord="tsunami",
        uitleg="Op open zee is zo'n golf laag en nauwelijks merkbaar. Pas bij de kust, waar het water ondieper wordt, stapelt ze zich op tot een muur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kunnen mensen zich het best wapenen tegen aardbevingen?",
        opties=[
            "Gebouwen zo bouwen dat ze mee kunnen bewegen",
            "De breuklijnen onder de stad dichtgooien met beton",
            "Enkel nog houten huizen van één verdieping bouwen",
            "De bevolking elk jaar naar een ander gebied brengen",
        ],
        antwoord=0,
        uitleg="Tegenhouden kan niemand een beving. Wat wel helpt, is bouwen volgens regels die de schokken opvangen, en oefenen wat je moet doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle vulkanen op aarde barsten regelmatig uit.",
        antwoord=False,
        uitleg="Sommige zijn actief, andere sluimeren al eeuwen, en nog andere zijn definitief uitgedoofd. Een sluimerende vulkaan kan wel opnieuw wakker worden.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Aan een oude kerk brokkelen de stenen aan de buitenkant af. Wat gebeurt daar?",
        opties=[
            "De steen wordt ter plaatse afgebroken",
            "De steen wordt door de wind weggeblazen",
            "De steen wordt door regen naar beneden gespoeld",
            "De steen wordt door de zon uitgerekt",
        ],
        antwoord=0,
        uitleg="Dat is verwering: gesteente valt uiteen op de plaats waar het ligt, door vorst, door regenwater en door temperatuurverschillen. Pas daarna kan het weggevoerd worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen verwering en erosie?",
        opties=[
            "Verwering breekt af, erosie voert weg",
            "Verwering voert weg, erosie breekt af",
            "Verwering gebeurt door water, erosie door wind",
            "Verwering duurt kort, erosie duurt eeuwen",
        ],
        antwoord=0,
        uitleg="Eerst valt het gesteente ter plaatse uiteen: dat is verwering. Daarna nemen water, wind of ijs de brokstukken mee: dat is erosie.",
    ),
    dict(
        type="invultekst",
        vraag="Het afzetten van meegevoerd materiaal op een andere plaats heet ___.",
        antwoord="sedimentatie",
        uitleg="Zodra het water of de wind vertraagt, kan het materiaal niet meer gedragen worden en valt het neer. Zo ontstaan zandbanken, delta's en duinen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Water dringt in een barst in de rots, bevriest en zet uit. De rots springt uiteen. Hoe heet dat?",
        opties=[
            "Vorstverwering",
            "Erosie door ijs",
            "Sedimentatie",
            "Chemische afbraak",
        ],
        antwoord=0,
        uitleg="Bevriezend water zet ongeveer een tiende uit en wrikt zo de barst open. Na veel vries- en dooibeurten breekt de rots. Daarom brokkelen bergwanden vooral in het voorjaar af.",
    ),
    dict(
        type="waarofniet",
        vraag="Regenwater kan kalksteen langzaam oplossen.",
        antwoord=True,
        uitleg="Regenwater is licht zuur en kalksteen is daar gevoelig voor. Zo ontstaan in kalkstreken grotten, spleten en verdwijngaten waar beken in de grond verdwijnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten kunnen materiaal wegvoeren? Er zijn er meerdere juist.",
        opties=[
            "Stromend water",
            "Wind",
            "Bewegend ijs",
            "De zwaartekracht van de maan",
            "De warmte van de zon",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt wind, water en ijs als de drie krachten die het reliëf veranderen. Zon en maan spelen een rol in het weer en de getijden, maar voeren zelf niets weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rivier snijdt zich in een plateau in. Welke vorm krijgt het dal?",
        opties=[
            "Een V-vorm",
            "Een U-vorm",
            "Een volledig vlakke bodem",
            "Een ronde kom",
        ],
        antwoord=0,
        uitleg="Een rivier schuurt vooral naar beneden, dus het dal wordt smal en diep met schuine wanden: een V. Een gletsjer schuurt ook zijwaarts en laat een brede U achter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een dal dat ooit door een gletsjer uitgeschuurd werd?",
        opties=[
            "Aan de brede bodem en de steile wanden",
            "Aan de scherpe V-vorm van het dal",
            "Aan de rivier die er middenin stroomt",
            "Aan het bos dat er tot bovenaan groeit",
        ],
        antwoord=0,
        uitleg="Een gletsjer is breed en zwaar en schaaft de flanken mee af. Wat overblijft is een dal met een vlakke bodem en rechte wanden, de klassieke U-vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rivier zet het meeste materiaal af waar ze het snelst stroomt.",
        antwoord=False,
        uitleg="Net omgekeerd. Snel stromend water houdt korrels in beweging; pas waar de stroom vertraagt, in de binnenbocht of aan de monding, valt het materiaal neer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een delta?",
        opties=[
            "Een waaier van afzettingen waar een rivier uitmondt",
            "Een diep dal dat door een gletsjer is uitgeschuurd",
            "Een rij duinen die de wind heeft opgeworpen",
            "Een meer dat na een aardbeving is ontstaan",
        ],
        antwoord=0,
        uitleg="Bij de monding verliest een rivier haar snelheid en laat ze haar zand en slib vallen. Zo groeit er een vlak, vertakt gebied aan: de delta.",
    ),
    dict(
        type="invultekst",
        vraag="Een heuvel van zand die door de wind is opgewaaid, noem je een ___.",
        antwoord="duin",
        uitleg="Duinen ontstaan waar de wind zand opneemt en het achter een obstakel weer laat vallen. Aan onze kust houden ze het achterland droog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het zand van een woestijn kloppen? Er zijn er meerdere juist.",
        opties=[
            "Er groeien nauwelijks planten die het zand vasthouden",
            "De wind heeft er daardoor vrij spel",
            "Duinen verplaatsen zich er over de jaren heen",
            "Het zand is er lichter dan zand aan onze kust",
            "Er valt er nooit een druppel regen op de bodem",
        ],
        antwoord=[0, 1, 2],
        uitleg="Plantenwortels houden losse korrels vast. Waar niets groeit, kan de wind het zand oppakken en verplaatsen de duinen zich. Het zand zelf weegt evenveel als elders, en ook in een woestijn regent het soms.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boer ploegt een helling van boven naar beneden. Wat gebeurt er bij een zware regenbui?",
        opties=[
            "Het water spoelt door de voren en neemt grond mee",
            "Het water blijft in de voren staan en zakt weg",
            "Het water verdampt sneller door de open grond",
            "Het water zoekt zijn weg naar de zijkant van de akker",
        ],
        antwoord=0,
        uitleg="Voren die met de helling mee lopen, werken als goten. Ploegt de boer dwars op de helling, dan houden de voren het water juist tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Planten en bomen beschermen de bodem tegen erosie.",
        antwoord=True,
        uitleg="Bladeren breken de kracht van de regendruppels en wortels houden de grond samen. Wordt een helling kaalgekapt, dan spoelt de vruchtbare laag bij de eerste bui weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke landvormen zijn door sedimentatie ontstaan? Er zijn er meerdere juist.",
        opties=[
            "Een delta",
            "Een zandbank",
            "Een duinengordel",
            "Een kloof in een plateau",
            "Een krater van een vulkaan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Delta's, zandbanken en duinen bestaan uit materiaal dat ergens anders is weggehaald en hier is neergelegd. Een kloof is juist uitgeschuurd, en een krater komt van een uitbarsting.",
    ),
    dict(
        type="meerkeuze",
        vraag="De leembodem van Haspengouw is duizenden jaren geleden aangevoerd. Waardoor?",
        opties=[
            "Door de wind",
            "Door een gletsjer",
            "Door de zee",
            "Door een vulkaan",
        ],
        antwoord=0,
        uitleg="Tijdens de ijstijden blies de wind fijn stof over het kale landschap en zette het in dikke lagen af. Die leem maakt Haspengouw tot vandaag vruchtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Aan de kust breekt de zee stukken van de kustlijn af. Hoe noemt men dat?",
        opties=[
            "Kusterosie",
            "Kustsedimentatie",
            "Kustverwering",
            "Kustophoging",
        ],
        antwoord=0,
        uitleg="De golven slaan tegen de kust en nemen zand en stukken klif mee. Op andere plaatsen langs diezelfde kust wordt dat materiaal weer afgezet.",
    ),
    dict(
        type="waarofniet",
        vraag="Verwering, erosie en sedimentatie gebeuren zo traag dat je ze nooit in één mensenleven kan zien.",
        antwoord=False,
        uitleg="Meestal gaat het traag, maar niet altijd. Na een hevige onweersbui kan een akker in één namiddag diepe geulen krijgen, en een storm verplaatst duinen in enkele uren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom liggen er in kalkstreken zoals de Condroz zoveel grotten?",
        opties=[
            "Omdat kalksteen door water wordt opgelost",
            "Omdat kalksteen door de vorst uiteenvalt",
            "Omdat de wind er de steen heeft uitgehold",
            "Omdat er vroeger gletsjers overheen schoven",
        ],
        antwoord=0,
        uitleg="Water dat door spleten in de kalksteen sijpelt, lost de steen langzaam op. Na duizenden jaren blijven er gangen en zalen over.",
    ),
    dict(
        type="invultekst",
        vraag="Het uiteenvallen van gesteente op de plaats zelf, zonder dat het weggevoerd wordt, heet ___.",
        antwoord="verwering",
        uitleg="Verwering is de eerste stap. Zonder verwering zou erosie weinig te vervoeren hebben, want massief gesteente neemt geen enkele rivier mee.",
    ),
]
