# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Stoffen classificeren en benoemen.

Chemie, de kop "Organische en anorganische stoffen: classificeren en
toepassingen" van de vakfiche natuurwetenschappen 2de graad doorstroom.
Deel 1 gaat over de stofklassen (oxide, hydroxide, zuur, zout, binair en
ternair) en de zuurresten; deel 2 over de triviale namen, de tien laagste
n-alkanen en de toepassingen van de stoffen die bij naam genoemd worden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Tot welke stofklasse hoort een verbinding van een element met zuurstof?",
        opties=["een oxide", "een hydroxide", "een zuur", "een zout"],
        antwoord=0,
        uitleg="Een oxide is een binaire verbinding met zuurstof, zoals calciumoxide of koolstofdioxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke groep herken je in de formule van een hydroxide?",
        opties=[
            "de hydroxidegroep OH",
            "de carbonaatgroep CO3",
            "het waterstofion H vooraan",
            "de sulfaatgroep SO4",
        ],
        antwoord=0,
        uitleg="Een hydroxide bestaat uit een metaal met een of meer OH-groepen, zoals natriumhydroxide of calciumhydroxide.",
    ),
    dict(
        type="waarofniet",
        vraag="De formule van een anorganisch zuur begint met waterstof.",
        antwoord=True,
        uitleg="Dat waterstofion is precies wat het zuur in water afstaat. Daarom schrijf je het vooraan, zoals in HCl of H2SO4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn binaire zuren? Kruis alles aan wat juist is.",
        opties=[
            "waterstofchloride",
            "waterstofsulfide",
            "waterstoffluoride",
            "salpeterzuur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een binair zuur bestaat uit waterstof en één ander element. Salpeterzuur bevat ook zuurstof en is dus ternair.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de triviale naam van de stof met formule HCl in water?",
        antwoord="zoutzuur",
        uitleg="De systematische naam is waterstofchloride. Opgelost in water noemen we het zoutzuur, en het zit onder andere in ontkalker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je het ion met formule NO3 min?",
        opties=["nitraation", "nitrietion", "sulfaation", "fosfaation"],
        antwoord=0,
        uitleg="Het nitraation komt van salpeterzuur. Je vindt het in kunstmest en in nitraatzouten zoals natriumnitraat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ternair zout bevat naast het metaal ook zuurstof.",
        antwoord=True,
        uitleg="Calciumcarbonaat is ternair: calcium, koolstof en zuurstof. Keukenzout heeft maar twee elementen en is dus binair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de naam van het ion met formule SO4 twee min?",
        opties=["sulfaation", "sulfide-ion", "sulfietion", "chloraation"],
        antwoord=0,
        uitleg="Het sulfaation komt van zwavelzuur. Het sulfide-ion is het binaire broertje, zonder zuurstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de stocknotatie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zet het oxidatiegetal van het metaal tussen haakjes",
            "ze gebruikt een Romeins cijfer voor dat getal",
            "ze wordt gebruikt bij ionverbindingen",
            "ze gebruikt Griekse telwoorden zoals di en tri",
        ],
        antwoord=[0, 1, 2],
        uitleg="IJzer(III)chloride is stocknotatie. De Griekse telwoorden horen bij atoomverbindingen, zoals koolstofdioxide.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het zout met formule NaCl in het dagelijks leven?",
        antwoord="keukenzout",
        uitleg="De systematische naam is natriumchloride. Het is een binair zout met een ionrooster.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke stofklasse hoort natriumwaterstofcarbonaat?",
        opties=[
            "een ternair zout met een carbonaatgroep erin",
            "een hydroxide met een OH-groep erin",
            "een binair oxide met alleen zuurstof erin",
            "een binair zuur met alleen waterstof erin",
        ],
        antwoord=0,
        uitleg="Het bevat natrium, waterstof, koolstof en zuurstof. Je kent het als bakpoeder, en het wordt gebruikt om deeg te laten rijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof krijgt de naam ammoniumzout?",
        opties=[
            "een zout waarin het metaalion vervangen is door een ammoniumion",
            "een zout dat je alleen in een oplossing van ammoniak kan maken",
            "een zout dat bij het oplossen in water ammoniakgas vrijgeeft",
            "een zout waarin stikstof de plaats van het zuurstofatoom inneemt",
        ],
        antwoord=0,
        uitleg="Het ammoniumion NH4 plus gedraagt zich als een positief metaalion. Ammoniumnitraat is een bekend voorbeeld uit de kunstmest.",
    ),
    dict(
        type="waarofniet",
        vraag="Koolstofdioxide en koolstofmonoxide zijn dezelfde stof met twee namen.",
        antwoord=False,
        uitleg="Koolstofdioxide heeft twee zuurstofatomen, koolstofmonoxide maar één. Het eerste ademen we uit, het tweede is een gevaarlijk gas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noteer je de brutoformule van water?",
        opties=["H2O", "HO2", "H2O2", "OH"],
        antwoord=0,
        uitleg="Twee waterstofatomen en één zuurstofatoom. H2O2 is waterstofperoxide, een heel andere stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verschil zit er tussen een brutoformule en een structuurformule?",
        opties=[
            "de brutoformule telt alleen de atomen, de structuurformule toont de bindingen",
            "de brutoformule toont de bindingen, de structuurformule telt de atomen",
            "de brutoformule geldt voor zouten, de structuurformule alleen voor metalen",
            "de brutoformule geeft de massa, de structuurformule geeft het smeltpunt",
        ],
        antwoord=0,
        uitleg="C2H6 is een brutoformule. De structuurformule tekent er de twee koolstofatomen met hun waterstofatomen aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Het chloraation en het chloride-ion zijn twee verschillende ionen.",
        antwoord=True,
        uitleg="Het chloride-ion is enkel chloor, Cl min. Het chloraation bevat ook zuurstof, ClO3 min.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt de formule Ca(OH)2. Tot welke stofklasse hoort die stof?",
        opties=[
            "een hydroxide, met calcium en twee OH-groepen erin",
            "een ternair zout, met calcium en zuurstof erin",
            "een binair oxide, met alleen calcium en zuurstof",
            "een ternair zuur, met waterstof en zuurstof erin",
        ],
        antwoord=0,
        uitleg="Een metaal met OH-groepen is een hydroxide. Je kent deze stof als gebluste kalk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het ion met formule CO3 twee min?",
        antwoord="carbonaation",
        uitleg="Het carbonaation komt van koolzuur. Calciumcarbonaat met dit ion is de hoofdbestanddeel van kalksteen en van krijt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een oxide bestaat altijd uit drie verschillende elementen.",
        antwoord=False,
        uitleg="Een oxide is een binaire verbinding: één element samen met zuurstof, dus twee elementen. Komt er een derde bij, dan is het geen oxide meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke naam hoort bij de formule H2SO4?",
        opties=[
            "zwavelzuur, een ternair zuur met zwavel en zuurstof erin",
            "waterstofsulfide, een binair zuur met alleen zwavel erin",
            "zwaveldioxide, een binair oxide met twee zuurstofatomen",
            "natriumsulfaat, een ternair zout met natrium en zwavel",
        ],
        antwoord=0,
        uitleg="Waterstof vooraan maakt het een zuur, en de zuurstof erin maakt het ternair. Zwavelzuur zit onder andere in een autobatterij.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de triviale naam van methaan in het dagelijks gebruik?",
        opties=["aardgas", "propaan", "butaan", "lachgas"],
        antwoord=0,
        uitleg="Aardgas bestaat vooral uit methaan. We gebruiken het om te verwarmen en om op te koken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel koolstofatomen heeft butaan?",
        opties=["vier", "drie", "twee", "vijf"],
        antwoord=0,
        uitleg="De naam zegt het: but staat voor vier. Methaan heeft één, ethaan twee, propaan drie en butaan vier koolstofatomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Alkanen zijn organische stoffen die alleen uit koolstof en waterstof bestaan.",
        antwoord=True,
        uitleg="Elk koolstofatoom maakt vier bindingen, de rest wordt met waterstof opgevuld. Daarom heet de reeks ook de verzadigde koolwaterstoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn alkanen? Kruis alles aan wat juist is.",
        opties=["propaan", "hexaan", "octaan", "ammoniak"],
        antwoord=[0, 1, 2],
        uitleg="De naam van een alkaan eindigt op aan en begint met een telwoord. Ammoniak bevat stikstof en is geen koolwaterstof.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het alkaan met acht koolstofatomen?",
        antwoord="octaan",
        uitleg="Oct staat voor acht. Het octaangetal van benzine verwijst naar deze stof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor wordt calciumcarbonaat gebruikt?",
        opties=[
            "als bouwsteen van kalksteen, krijt en marmer",
            "als brandstof in een gasfles voor een barbecue",
            "als ontstopper om een verstopte afvoer te openen",
            "als drijfgas in een spuitbus met slagroom erin",
        ],
        antwoord=0,
        uitleg="Kalksteen bestaat zo goed als volledig uit calciumcarbonaat. Je vindt het ook in eierschalen en in de kalkaanslag van je kraan.",
    ),
    dict(
        type="waarofniet",
        vraag="Natriumhydroxide is de stof die we bijtende soda noemen.",
        antwoord=True,
        uitleg="Bijtende soda is een sterke base en zit in ontstopper. Soda zonder bijtend is een ander product, natriumcarbonaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stof kennen we als lachgas?",
        opties=[
            "distikstofoxide",
            "koolstofmonoxide",
            "waterstofsulfide",
            "zwaveldioxide",
        ],
        antwoord=0,
        uitleg="Distikstofoxide, met formule N2O, werd gebruikt als verdovingsmiddel. Het is ook een sterk broeikasgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is koolstofmonoxide zo gevaarlijk?",
        opties=[
            "het bindt in je bloed op de plaats waar zuurstof zou moeten zitten",
            "het verbrandt in je longen en veroorzaakt daar inwendige wonden",
            "het ruikt zo sterk dat je ervan in paniek schiet en hyperventileert",
            "het is zo zwaar dat het de lucht uit een hele kamer naar buiten duwt",
        ],
        antwoord=0,
        uitleg="Het gas is kleurloos en geurloos, en hecht veel sterker aan je bloed dan zuurstof. Het ontstaat bij onvolledige verbranding, bijvoorbeeld in een slecht onderhouden geiser.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we calciumoxide in het dagelijks leven?",
        antwoord="ongebluste kalk",
        uitleg="Giet je er water bij, dan wordt het calciumhydroxide, en dat is gebluste kalk. Die reactie geeft veel warmte af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruiken we ammoniak?",
        opties=[
            "als schoonmaakmiddel en als grondstof voor kunstmest",
            "als brandstof voor een motor op gewone benzine",
            "als bouwmateriaal voor muren en voor vloeren",
            "als voedingsstof die je rechtstreeks kan opeten",
        ],
        antwoord=0,
        uitleg="Ammoniak is een base met een scherpe geur. Het grootste deel van de wereldproductie gaat naar kunstmest.",
    ),
    dict(
        type="waarofniet",
        vraag="Koolzuurgas en koolzuur zijn twee namen voor precies dezelfde stof.",
        antwoord=False,
        uitleg="Koolzuurgas is koolstofdioxide. Koolzuur ontstaat pas als dat gas in water oplost, en dat is wat je in spuitwater hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zitten gewoonlijk in een gasfles voor de barbecue? Kruis alles aan wat juist is.",
        opties=["propaan", "butaan", "een mengsel van die twee", "waterstofchloride"],
        antwoord=[0, 1, 2],
        uitleg="Propaan en butaan zijn vloeibaar onder druk en verbranden schoon. Waterstofchloride is een zuur gas en heeft niets met brandstof te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruiken we fosforzuur onder andere?",
        opties=[
            "als zuur in frisdrank van het colatype",
            "als brandstof in een kacheltje op petroleum",
            "als bouwsteen van beton in de wegenbouw",
            "als drijfgas in een deodorant met verstuiver",
        ],
        antwoord=0,
        uitleg="Fosforzuur geeft cola zijn scherpe smaak. Het wordt ook gebruikt om roest van metaal te halen en in kunstmest.",
    ),
    dict(
        type="waarofniet",
        vraag="Water is de triviale naam van de stof die we systematisch diwaterstofoxide zouden noemen.",
        antwoord=True,
        uitleg="Bij heel bekende stoffen gebruiken we bijna altijd de triviale naam. Niemand vraagt aan tafel om diwaterstofoxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heet het alkaan met vijf koolstofatomen?",
        opties=["pentaan", "butaan", "hexaan", "heptaan"],
        antwoord=0,
        uitleg="Pent staat voor vijf. De reeks loopt methaan, ethaan, propaan, butaan, pentaan, hexaan, heptaan, octaan, nonaan en decaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest op een fles: ontstopper, bevat natriumhydroxide. Wat weet je over die stof?",
        opties=[
            "het is een hydroxide en dus een sterke base, bijtend voor je huid",
            "het is een zuur en dus gevaarlijk om samen met kalk te gebruiken",
            "het is een zout en lost gewoon op zonder iets met vuil te doen",
            "het is een oxide en reageert daarom helemaal niet met water",
        ],
        antwoord=0,
        uitleg="De OH-groep maakt het een base. Daarom staat er een waarschuwing op en werk je met handschoenen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het alkaan met tien koolstofatomen?",
        antwoord="decaan",
        uitleg="Dec staat voor tien, net als in decimeter. Het is het laatste van de tien eenvoudigste alkanen.",
    ),
    dict(
        type="waarofniet",
        vraag="Zoutzuur is net als zwavelzuur een ternair zuur.",
        antwoord=False,
        uitleg="Zoutzuur bevat alleen waterstof en chloor, dus twee elementen: het is binair. Zwavelzuur en salpeterzuur bevatten ook zuurstof en zijn ternair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt te horen dat een stof in schelpen en in kalkaanslag voorkomt en met zuur opschuimt. Welke stof is het?",
        opties=[
            "calciumcarbonaat, het zout van koolzuur met calcium erin",
            "calciumhydroxide, de base die we gebluste kalk noemen",
            "natriumchloride, het zout dat we keukenzout noemen",
            "waterstofsulfide, het gas dat naar rotte eieren ruikt",
        ],
        antwoord=0,
        uitleg="Carbonaten geven koolstofdioxide vrij als er zuur bij komt, en dat zie je opschuimen. Daarom verdwijnt kalkaanslag met azijn.",
    ),
]
