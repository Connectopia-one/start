# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Water en homeostase bij planten.

Biologie, eerste kop van de vakfiche natuurwetenschappen 2de graad doorstroom:
"Homeostase en waterhuishouding bij planten". Deel 1 gaat over homeostase, het
feedbacksysteem en de drie stappen van de waterhuishouding; deel 2 over de
organen en weefsels van de plant, het transport van water en assimilaten, en
de band met de fotosynthese.

Het transport van assimilaten door het floëem staat alleen in de uitgebreide
fiche (moderne talen en Latijn). Het zit daarom in deel 2, zodat wie de
kortere fiche volgt deel 1 kan maken en deel 2 kan overslaan.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met homeostase bij een plant?",
        opties=[
            "haar inwendig milieu stabiel houden terwijl de omgeving verandert",
            "haar bladeren laten vallen zodra de temperatuur buiten daalt",
            "haar wortels zo diep mogelijk in de bodem laten doorgroeien",
            "haar groei volledig stilleggen van zodra er droogte optreedt",
        ],
        antwoord=0,
        uitleg="Homeostase is het in stand houden van een inwendig evenwicht. De omgeving van een plant verandert voortdurend; met regelsystemen houdt de plant haar eigen milieu toch binnen nauwe grenzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke omgevingsfactoren beïnvloeden de waterhuishouding van een plant? Kruis alles aan wat juist is.",
        opties=[
            "de lichtsterkte die op de bladeren valt",
            "de temperatuur van de lucht rond de plant",
            "de vochtigheidsgraad van de bodem en de lucht",
            "de kleur van de bloemblaadjes van de plant",
        ],
        antwoord=[0, 1, 2],
        uitleg="Licht, temperatuur en de vochtigheidsgraad van bodem en lucht zijn de omgevingsfactoren die meespelen. De kleur van de bloemblaadjes speelt geen rol in de waterhuishouding.",
    ),
    dict(
        type="waarofniet",
        vraag="In een feedbacksysteem gebruikt de plant het gevolg van een proces om dat proces zelf bij te sturen.",
        antwoord=True,
        uitleg="Dat is net wat feedback betekent: het resultaat wordt teruggekoppeld. Verliest het blad te veel water, dan sluiten de huidmondjes en daalt het verlies weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke drie stappen bestaat de waterhuishouding van een plant?",
        opties=[
            "wateropname, watertransport en transpiratie",
            "wateropname, verbranding en uitscheiding",
            "verdamping, bevriezing en opnieuw ontdooien",
            "watertransport, bloei en de vorming van zaden",
        ],
        antwoord=0,
        uitleg="De plant neemt water op in de wortel, vervoert het naar boven en laat het als damp ontsnappen door de huidmondjes. Die drie samen vormen de waterhuishouding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de druk van het vocht in de vacuole waardoor een plantencel stevig blijft staan?",
        antwoord="turgor",
        uitleg="De vacuole duwt met haar vocht tegen de celwand. Die turgor houdt een niet-houtige plant rechtop; valt hij weg, dan verwelkt de plant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welk deel neemt een plant het grootste deel van haar water op?",
        opties=[
            "met de wortelharen, net achter de worteltop",
            "met de huidmondjes aan de onderkant van het blad",
            "met de waslaag die bovenop de bladeren ligt",
            "met de bloemen tijdens de bloeiperiode in de lente",
        ],
        antwoord=0,
        uitleg="De wortelharen zijn lange uitstulpingen van de epidermis van de wortel. Ze vergroten het contactoppervlak met de bodem enorm, en daar gaat het water naar binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="De huidmondjes van de meeste bladeren liggen vooral aan de onderkant van het blad.",
        antwoord=True,
        uitleg="Aan de onderkant is het koeler en vochtiger, zodat de plant daar minder water verliest dan aan de bovenkant waar de zon op staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="De sluitcellen rond een huidmondje verliezen hun turgor. Wat gebeurt er? Kruis alles aan wat juist is.",
        opties=[
            "het huidmondje gaat dicht",
            "de verdamping door dat blad daalt",
            "de opname van koolstofdioxide wordt moeilijker",
            "de plant neemt meteen meer water op via het blad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Slappe sluitcellen laten het huidmondje dichtvallen. Dat spaart water, maar er komt ook minder koolstofdioxide binnen, waardoor de fotosynthese vertraagt. Een blad neemt geen water op via een gesloten huidmondje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is worteldruk?",
        opties=[
            "de druk waarmee de wortel water in de houtvaten duwt",
            "de druk van de bodem op de wortels van een grote boom",
            "de druk die het blad op de bladsteel uitoefent bij wind",
            "de druk waarmee de wortel zich een weg zoekt in de grond",
        ],
        antwoord=0,
        uitleg="Door actief zouten op te nemen trekt de wortel water aan. Dat duwt het water een eind omhoog in de houtvaten, los van wat er bovenaan gebeurt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de zuigkracht die bovenaan in de plant ontstaat doordat er water verdampt uit de bladeren?",
        antwoord="transpiratiezuiging",
        uitleg="Verdampt er water uit het blad, dan trekt dat aan de waterdraad in de houtvaten. Die transpiratiezuiging is de belangrijkste motor van het transport naar boven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent capillariteit bij het watertransport in een plant?",
        opties=[
            "water kruipt vanzelf omhoog in een heel nauwe buis",
            "water zakt vanzelf naar beneden in een brede buis",
            "water bevriest sneller in een dunne buis dan in een dikke",
            "water verdampt sneller uit een nauwe dan uit een wijde buis",
        ],
        antwoord=0,
        uitleg="In een heel nauwe buis trekt water zichzelf omhoog, omdat het aan de wand blijft hangen en de watermoleculen aan elkaar kleven. De houtvaten zijn zulke nauwe buizen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij felle zon en grote droogte zet een plant haar huidmondjes zo ver mogelijk open.",
        antwoord=False,
        uitleg="Net omgekeerd. Bij droogte sluit de plant haar huidmondjes om water te sparen, ook al legt ze daarmee haar fotosynthese een stuk stil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verwelkt een kamerplant die je een week niet begiet?",
        opties=[
            "de cellen verliezen hun turgor doordat de vacuoles leeglopen",
            "de celwanden lossen op doordat er geen water meer is",
            "de bladgroenkorrels verhuizen naar de wortels van de plant",
            "de plant bouwt haar huidmondjes af om water te besparen",
        ],
        antwoord=0,
        uitleg="Zonder aanvoer verliest de plant meer water door verdamping dan ze opneemt. De vacuoles lopen leeg, de cellen duwen niet meer tegen hun wand, en de stengels zakken in elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant verliest het grootste deel van haar water via de bloemen.",
        antwoord=False,
        uitleg="Het meeste water verdwijnt als damp door de huidmondjes van de bladeren. Dat heet transpiratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over transpiratie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zorgt voor een zuigkracht die water omhoog trekt",
            "ze koelt het blad af bij warm weer",
            "ze gebeurt vooral via de huidmondjes",
            "ze levert de plant de suikers die ze nodig heeft",
        ],
        antwoord=[0, 1, 2],
        uitleg="Transpiratie trekt water omhoog, koelt het blad en verloopt via de huidmondjes. Suikers komen niet van de transpiratie maar van de fotosynthese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant staat in heel vochtige lucht. Wat gebeurt er met haar transpiratie?",
        opties=[
            "ze daalt, want het verschil in vochtigheid wordt kleiner",
            "ze stijgt, want vochtige lucht neemt meer damp op",
            "ze blijft precies gelijk, want de plant regelt dat zelf",
            "ze stopt volledig, want de huidmondjes gaan allemaal dicht",
        ],
        antwoord=0,
        uitleg="Water verdampt van vochtig naar droog. Is de lucht al vochtig, dan is het verschil klein en verdampt er weinig, ook al staan de huidmondjes open.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heten de twee boonvormige cellen die samen een huidmondje openen en sluiten?",
        antwoord="sluitcellen",
        uitleg="De sluitcellen zwellen of verslappen naargelang hun vochtgehalte, en daarmee gaat de opening tussen hen in open of dicht.",
    ),
    dict(
        type="waarofniet",
        vraag="De waterhuishouding van een plant staat los van haar fotosynthese.",
        antwoord=False,
        uitleg="Ze hangen juist nauw samen. Water is een grondstof voor de fotosynthese, en dezelfde huidmondjes die water doorlaten, laten ook de koolstofdioxide binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant krijgt het signaal dat ze te veel water verliest. Welke reactie past bij haar feedbacksysteem?",
        opties=[
            "de sluitcellen verslappen en de huidmondjes gaan dicht",
            "de wortels laten meer water los aan de bodem rond hen",
            "de bladeren maken extra huidmondjes aan op dezelfde dag",
            "de bloemen gaan open zodat er meer damp kan ontsnappen",
        ],
        antwoord=0,
        uitleg="Het hormoon abscisinezuur laat de sluitcellen verslappen; de huidmondjes gaan dicht en het verlies daalt. Zo keert de plant terug naar haar evenwicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Water verplaatst zich in de plant van de wortel naar het blad.",
        antwoord=True,
        uitleg="Het water komt binnen in de wortel en gaat door de houtvaten omhoog naar de bladeren, waar het grootste deel verdampt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier organen onderscheid je bij een plant?",
        opties=[
            "wortel, stengel, blad en bloem",
            "wortel, bast, vrucht en zaad",
            "stengel, knop, schors en wortelhaar",
            "blad, bloem, meeldraad en stamper",
        ],
        antwoord=0,
        uitleg="Wortel, stengel, blad en bloem zijn de vier plantenorganen. Elk orgaan is opgebouwd uit verschillende weefsels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke weefsels horen bij het huidweefsel van een plant? Kruis alles aan wat juist is.",
        opties=["de epidermis", "de cuticula of waslaag", "de bast", "de houtvaten"],
        antwoord=[0, 1, 2],
        uitleg="Epidermis, cuticula en bast dekken de plant af en beschermen haar. De houtvaten horen bij het transportweefsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waardoor gaat het water met de opgeloste zouten van de wortel naar het blad?",
        opties=[
            "door de xyleemvaten, ook wel houtvaten genoemd",
            "door de floëemvaten, ook wel zeefvaten genoemd",
            "door de cuticula bovenop de bladeren van de plant",
            "door het vulweefsel tussen de nerven van het blad",
        ],
        antwoord=0,
        uitleg="Xyleem of houtvaten vervoeren water en mineralen in één richting: van beneden naar boven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het transportweefsel dat de suikers uit het blad naar de rest van de plant brengt?",
        antwoord="floëem",
        uitleg="Het floëem of de zeefvaten vervoert de assimilaten, dus de suikers uit de fotosynthese. Dat kan naar boven én naar beneden.",
    ),
    dict(
        type="waarofniet",
        vraag="Houtvaten en zeefvaten liggen samen in vaatbundels.",
        antwoord=True,
        uitleg="In een vaatbundel liggen xyleem en floëem naast elkaar. In een blad zie je zo'n bundel als een nerf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een assimilaat?",
        opties=[
            "een suiker die de plant zelf maakt bij de fotosynthese",
            "een zout dat de plant uit de bodem opneemt met haar wortels",
            "een afvalstof die de plant via de huidmondjes uitademt",
            "een hormoon dat de groei van de zijscheuten tegenhoudt",
        ],
        antwoord=0,
        uitleg="Assimilaten zijn de producten van de fotosynthese, vooral glucose. Ze gaan via het floëem naar de delen die ze nodig hebben of opslaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen heeft een plant nodig om aan fotosynthese te doen? Kruis alles aan wat juist is.",
        opties=["water", "koolstofdioxide", "licht als energiebron", "zuurstofgas"],
        antwoord=[0, 1, 2],
        uitleg="Water en koolstofdioxide zijn de grondstoffen, licht levert de energie. Zuurstofgas is geen grondstof maar juist een product van de fotosynthese.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de fotosynthese ontstaan glucose en zuurstofgas.",
        antwoord=True,
        uitleg="De algemene reactievergelijking is: koolstofdioxide en water geven onder invloed van licht glucose en zuurstofgas.",
    ),
    dict(
        type="invultekst",
        vraag="In welk organel van de plantencel gebeurt de fotosynthese?",
        antwoord="chloroplast",
        uitleg="De chloroplasten of bladgroenkorrels bevatten bladgroen, dat het licht opvangt. Daar vindt de fotosynthese plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom legt een plant bij aanhoudende droogte haar fotosynthese grotendeels stil?",
        opties=[
            "haar huidmondjes staan dicht, dus er komt amper koolstofdioxide binnen",
            "haar bladgroenkorrels worden afgebroken zodra het warm wordt",
            "haar wortels nemen bij droogte geen enkel mineraal meer op",
            "haar zeefvaten raken verstopt met suikers uit het blad",
        ],
        antwoord=0,
        uitleg="Om water te sparen sluit de plant haar huidmondjes. Daardoor stopt ook de aanvoer van koolstofdioxide, en zonder die grondstof valt de fotosynthese zo goed als stil.",
    ),
    dict(
        type="waarofniet",
        vraag="Het vulweefsel van een blad bevat nauwelijks bladgroenkorrels.",
        antwoord=False,
        uitleg="Net in het vulweefsel tussen de opperhuid en de vaatbundels zitten de cellen met de meeste chloroplasten. Daar gebeurt het meeste werk van de fotosynthese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke prikkel vangt een fotoreceptor van een plant op?",
        opties=["licht", "aanraking", "temperatuur", "zwaartekracht"],
        antwoord=0,
        uitleg="Een fotoreceptor reageert op licht. Aanraking valt onder de mechanoreceptoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant op de vensterbank groeit duidelijk naar het raam toe. Hoe komt dat?",
        opties=[
            "het hormoon auxine hoopt zich op aan de donkere kant en laat die kant sneller strekken",
            "het hormoon auxine hoopt zich op aan de lichte kant en laat die kant sneller strekken",
            "de bladgroenkorrels verhuizen allemaal naar de kant waar het licht vandaan komt",
            "de wortels duwen de stengel stilaan in de richting van het meeste licht",
        ],
        antwoord=0,
        uitleg="Auxine wordt weggedrukt van het licht. Aan de donkere kant zit er dus meer, die cellen strekken sneller, en de stengel buigt naar het licht toe.",
    ),
    dict(
        type="waarofniet",
        vraag="Ethyleen is het plantenhormoon dat de rijping van vruchten op gang brengt.",
        antwoord=True,
        uitleg="Ethyleen is een gas. Eén rijpe appel in een mand kan daardoor de hele mand doen rijpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke taken horen bij het hormoon abscisinezuur? Kruis alles aan wat juist is.",
        opties=[
            "het laat de huidmondjes sluiten bij droogte",
            "het helpt de plant water sparen in een droge periode",
            "het speelt mee bij het verliezen van bladeren",
            "het laat de stengel sneller naar het licht groeien",
        ],
        antwoord=[0, 1, 2],
        uitleg="Abscisinezuur is het hormoon van de droogte en de rust: huidmondjes dicht, water sparen, blad laten vallen. Het strekken naar het licht is het werk van auxine.",
    ),
    dict(
        type="waarofniet",
        vraag="Water en assimilaten gaan allebei door dezelfde vaten, maar in een andere richting.",
        antwoord=False,
        uitleg="Ze gaan door verschillende vaten: water door het xyleem, assimilaten door het floëem. Alleen liggen die vaten samen in één vaatbundel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de rol van de cuticula op een blad?",
        opties=[
            "ze beperkt het waterverlies van het blad",
            "ze vangt het licht op voor de fotosynthese",
            "ze voert de suikers af naar de stengel",
            "ze neemt water op uit de lucht rond het blad",
        ],
        antwoord=0,
        uitleg="De cuticula is een waslaagje op de epidermis. Water gaat er niet zomaar door, zodat het blad niet uitdroogt tussen de huidmondjes door.",
    ),
    dict(
        type="invultekst",
        vraag="Welk gas ontsnapt er door de huidmondjes als een plant volop aan fotosynthese doet?",
        antwoord="zuurstofgas",
        uitleg="Zuurstofgas is een product van de fotosynthese. Het verlaat het blad via dezelfde huidmondjes die koolstofdioxide binnenlaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant die in het donker staat, blijft even veel glucose maken als een plant in het licht.",
        antwoord=False,
        uitleg="Zonder licht is er geen energiebron voor de fotosynthese. De plant teert dan op haar voorraad in plaats van bij te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemen we de waterhuishouding een voorbeeld van homeostase?",
        opties=[
            "de plant stuurt opname en verlies bij zodat haar watergehalte binnen grenzen blijft",
            "de plant neemt altijd evenveel water op, wat er buiten ook gebeurt",
            "de plant geeft haar water door aan de planten die naast haar staan",
            "de plant slaat al haar water op in de bloemen tot er droogte komt",
        ],
        antwoord=0,
        uitleg="Opname, transport en verdamping worden voortdurend tegen elkaar afgewogen. Zo blijft het inwendige milieu stabiel terwijl het buiten verandert, en dat is homeostase.",
    ),
]
