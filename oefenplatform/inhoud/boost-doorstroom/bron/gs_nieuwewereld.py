# -*- coding: utf-8 -*-
"""De vragen voor "De 'Nieuwe' Wereld en de driehoekshandel".

Uit de vakfiche, vroegmoderne tijd: de ontdekkingsreizen (motieven, technische
vernieuwingen, reizigers en routes), de twee kolonisatiegolven, de invloed van
kolonisatie op godsdienst, taal en cultuur, de driehoekshandel en de
slavenhandel, monocultuur en roofbouw, en daarnaast de commerciële revolutie
met het handelskapitalisme, het mercantilisme en de nieuwe ondernemingsvormen.

Deel 1 gaat over de reizen en de kolonisatie. Deel 2 over de driehoekshandel en
over wat er in Europa zelf economisch veranderde.

De aanhalingstekens rond 'Nieuwe' staan er met opzet: die wereld was enkel nieuw
voor wie er vandaan kwam. Voor wie er woonde, was ze dat niet.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat waren de motieven voor de ontdekkingsreizen?",
        opties=[
            "economisch: een eigen weg naar de specerijen van Azië",
            "godsdienstig: het christendom verspreiden",
            "politiek: aanzien en gebied voor de eigen vorst",
            "sportief: een wedstrijd tussen zeelui",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij bijna elke reis lopen die drie door elkaar. Goud, God en glorie, zegt men wel eens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zochten de Portugezen en Spanjaarden een zeeweg naar Azië?",
        opties=[
            "de landroute liep door gebieden waar tussenhandelaars de prijs bepaalden",
            "over land reizen was door de paus voor alle christenen verboden verklaard",
            "er lag aan de hele kust van Azië geen enkele haven om aan te leggen",
            "de landroute naar het oosten was toen pas voor het eerst ontdekt",
        ],
        antwoord=0,
        uitleg="Specerijen die via vele handen kwamen, waren in Lissabon peperduur. Wie zelf tot bij de bron voer, hield die winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk instrument gebruikte een zeevaarder om op open zee zijn breedtegraad te bepalen?",
        opties=[
            "het astrolabium",
            "het kompas",
            "de zandloper",
            "het roer",
        ],
        antwoord=0,
        uitleg="Je meet er de hoogte van de zon of van een ster mee. Het kompas geeft enkel de richting aan, de zandloper enkel de tijd.",
    ),
    dict(
        type="invultekst",
        vraag="Welke zeevaarder voer in 1492 in dienst van Spanje de Atlantische Oceaan over?",
        antwoord="Columbus",
        uitleg="Hij dacht tot aan Azië te zijn gevaren, en hield dat ook vol. Wat hij bereikte, waren eilanden in de Caraïben.",
    ),
    dict(
        type="waarofniet",
        vraag="Columbus wist bij zijn terugkeer dat hij een voor Europa onbekend werelddeel had bereikt.",
        antwoord=False,
        uitleg="Hij bleef geloven dat hij in Azië was. Dat het om een ander werelddeel ging, wordt pas later duidelijk, en Amerigo Vespucci gaf het zijn naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie voer als eerste rond Kaap de Goede Hoop tot in Indië?",
        opties=[
            "Vasco da Gama",
            "Ferdinand Magellaan",
            "Christoffel Columbus",
            "Hernán Cortés",
        ],
        antwoord=0,
        uitleg="In 1498 bereikt hij Calicut. Magellaans vloot vaart later als eerste rond de wereld, Cortés is geen ontdekkingsreiziger maar veroveraar.",
    ),
    dict(
        type="waarofniet",
        vraag="Portugal bouwde vooral een net van handelsposten langs de kusten, Spanje veroverde grote gebieden in het binnenland.",
        antwoord=True,
        uitleg="Portugal wilde de handel beheersen, Spanje het land zelf. Dat verschil verklaart waarom hun rijken er zo anders uitzien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijken vernietigden de Spanjaarden in de 16de eeuw?",
        opties=[
            "het Aztekenrijk in Mexico",
            "het Incarijk in de Andes",
            "de Mayasteden in Midden-Amerika",
            "het Chinese keizerrijk",
        ],
        antwoord=[0, 1, 2],
        uitleg="China bleef buiten hun bereik. De drie andere vielen wel, met weinig soldaten maar met bondgenoten, paarden, vuurwapens en vooral ziekten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de belangrijkste oorzaak van de demografische inzinking van de precolumbiaanse bevolking?",
        opties=[
            "ziekten waartegen zij geen weerstand hadden, zoals pokken en mazelen",
            "het slechte klimaat van die jaren, met koude winters en droge zomers",
            "een grote hongersnood die al woedde vóór de komst van de Spanjaarden",
            "de vlucht van een groot deel van de bevolking over zee naar Europa",
        ],
        antwoord=0,
        uitleg="Naar schatting stierf het grootste deel van de bevolking binnen een eeuw. Oorlog en dwangarbeid kwamen daar nog bovenop.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het Spaanse systeem waarbij een kolonist arbeid mocht opeisen van de inheemse bevolking?",
        antwoord="het encomiendasysteem",
        uitleg="In ruil moest hij hen beschermen en bekeren. In de praktijk was het dwangarbeid in de mijnen en op de velden.",
    ),
    dict(
        type="waarofniet",
        vraag="De demografische inzinking, het encomiendasysteem en de Afrikaanse slavenhandel hangen met elkaar samen.",
        antwoord=True,
        uitleg="Stierf de inheemse bevolking weg, dan viel de gedwongen arbeid van het encomiendasysteem weg. Die arbeid werd van elders gehaald, uit Afrika.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk land hoort bij de eerste kolonisatiegolf en niet bij de tweede?",
        opties=[
            "Portugal",
            "Engeland",
            "Frankrijk",
            "de Verenigde Provinciën",
        ],
        antwoord=0,
        uitleg="De eerste golf is die van Portugal en Spanje, vanaf ongeveer 1500. De drie andere komen pas vanaf de 17de eeuw op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je vandaag nog welk land welk gebied koloniseerde?",
        opties=[
            "aan de taal die er gesproken wordt en aan de plaatsnamen",
            "aan het klimaat van het gebied en aan de gewassen die er groeien",
            "aan de hoogte van de bergen en aan de loop van de rivieren",
            "aan de breedtegraad waarop het gebied op de wereldkaart ligt",
        ],
        antwoord=0,
        uitleg="Brazilië spreekt Portugees, de rest van Zuid-Amerika Spaans. Ook godsdienst en rechtssysteem dragen dat spoor.",
    ),
    dict(
        type="waarofniet",
        vraag="De kolonisatie liet de godsdienst van de gekoloniseerde volkeren ongemoeid.",
        antwoord=False,
        uitleg="Missionering hoorde bij het project zelf. Oude gebruiken verdwenen of mengden zich met het christendom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is monocultuur in een kolonie?",
        opties=[
            "een heel gebied wordt met één gewas beplant, voor de uitvoer",
            "in het hele gebied leeft nog maar één volk met één eigen cultuur",
            "in het hele gebied wordt nog maar één enkele taal gesproken",
            "in het hele gebied staat nog maar één fabriek, van de gouverneur",
        ],
        antwoord=0,
        uitleg="Suikerriet, katoen of tabak, zo ver je kijken kan. Dat maakt een kolonie rijk aan uitvoer en tegelijk afhankelijk voor haar eigen voedsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Roofbouw betekent dat men de grond of de mijn uitput zonder aan de toekomst te denken.",
        antwoord=True,
        uitleg="Zilver uit Potosí, hout uit de bossen, vruchtbaarheid uit de bodem. Wat op is, is op, en de winst vertrok naar Europa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gewassen en ertsen kwamen uit de koloniën naar Europa?",
        opties=[
            "zilver uit de Andes",
            "suiker en tabak uit de Caraïben",
            "aardappelen en maïs uit Amerika",
            "rijst uit Amerika",
        ],
        antwoord=[0, 1, 2],
        uitleg="Rijst komt uit Azië. De drie andere veranderen Europa grondig: het zilver de prijzen, de aardappel en de maïs het voedsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijft men 'Nieuwe' Wereld met aanhalingstekens?",
        opties=[
            "omdat die wereld enkel nieuw was voor de Europeanen die er aankwamen",
            "omdat de naam pas in de 20ste eeuw bedacht werd door aardrijkskundigen",
            "omdat het gebied in werkelijkheid nooit bestaan heeft zoals men dacht",
            "omdat het woord uit het Latijn komt en dus vertaald moet worden gelezen",
        ],
        antwoord=0,
        uitleg="Er woonden al miljoenen mensen met eigen rijken en steden. De naam vertelt dus iets over wie hem gebruikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Spaanse kroniek over de verovering van Mexico geeft het volledige beeld van wat er gebeurd is.",
        antwoord=False,
        uitleg="Ze is geschreven door de winnaar, vaak om zijn eigen optreden te verdedigen. Er bestaan ook Azteekse verslagen, en die vertellen het anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Kolonisatie draait in de eerste plaats om welk maatschappelijk domein?",
        opties=[
            "het politieke domein, want het gaat over gezag over gebied",
            "het culturele domein alleen, want het gaat over taal en geloof",
            "het maritieme domein, want alles gebeurde met schepen over zee",
            "het sportieve domein, want het was een wedloop tussen landen",
        ],
        antwoord=0,
        uitleg="Ze raakt wel alle domeinen tegelijk: economisch door de handel, cultureel door taal en geloof, sociaal door de slavernij.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie hoekpunten had de driehoekshandel?",
        opties=[
            "Europa, West-Afrika en Amerika",
            "Europa, Azië en Afrika",
            "Spanje, Portugal en Engeland",
            "de Middellandse Zee, de Noordzee en de Oostzee",
        ],
        antwoord=0,
        uitleg="Elk been van de driehoek had zijn eigen lading, en op elk been werd winst gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat werd er op elk been van de driehoekshandel vervoerd?",
        opties=[
            "van Europa naar Afrika: wapens, textiel en alcohol",
            "van Afrika naar Amerika: tot slaaf gemaakte mensen",
            "van Amerika naar Europa: suiker, katoen en tabak",
            "van Europa naar Amerika: specerijen uit Azië",
        ],
        antwoord=[0, 1, 2],
        uitleg="De specerijen kwamen langs een heel andere route. De drie andere ladingen sluiten de driehoek.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de oversteek van Afrika naar Amerika in de driehoekshandel?",
        antwoord="de middenpassage",
        uitleg="Weken in het ruim, vastgeketend. Een groot deel van de mensen overleefde die overtocht niet.",
    ),
    dict(
        type="waarofniet",
        vraag="De slavenhandel werd in Europa zelf lange tijd als een gewone handel beschouwd.",
        antwoord=True,
        uitleg="Er werd openlijk in geïnvesteerd, met aandelen en verzekeringen. Pas in de 18de eeuw groeit er een beweging die ze wil afschaffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de commerciële revolutie?",
        opties=[
            "een grondige verandering van het economische systeem door handel en geld",
            "een gewapende opstand van de handelaars tegen de koning en zijn belastingen",
            "de uitvinding van de stoommachine en het begin van de fabrieksnijverheid",
            "het einde van alle handel met Azië na de val van Constantinopel in 1453",
        ],
        antwoord=0,
        uitleg="Niet plots zoals een opstand, maar wel ingrijpend: wie handelt en investeert, wordt belangrijker dan wie grond bezit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn kenmerken van het handelskapitalisme?",
        opties=[
            "winst wordt opnieuw geïnvesteerd om meer winst te maken",
            "kapitaal wordt door meerdere mensen samengelegd",
            "het risico van een reis wordt gespreid over vele aandeelhouders",
            "de vorst bezit alle handelsschepen en alle handelswaar van het land",
        ],
        antwoord=[0, 1, 2],
        uitleg="De schepen waren meestal van particuliere compagnieën, niet van de vorst. De drie andere kenmerken maken het verschil met de oudere handel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houdt mercantilisme in?",
        opties=[
            "een land moet meer uitvoeren dan invoeren, om edelmetaal binnen te halen",
            "alle landen moeten volkomen vrij met elkaar kunnen handelen, zonder rechten",
            "alle handel over de grenzen heen moet door de vorst verboden worden",
            "iedereen in het land mag voortaan zijn eigen munten laten slaan",
        ],
        antwoord=0,
        uitleg="Daarom beschermde een vorst zijn eigen nijverheid met invoerrechten en behield hij de handel met zijn koloniën voor zichzelf.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens het mercantilisme is vrije handel met alle landen het beste voor een vorst.",
        antwoord=False,
        uitleg="Het gaat net uit van het omgekeerde: wat het ene land wint, verliest het andere. Vrije handel als idee komt pas met Adam Smith.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een onderneming waarvan het kapitaal in verhandelbare delen verdeeld is?",
        antwoord="een handelscompagnie",
        uitleg="De Verenigde Oost-Indische Compagnie is er het bekendste voorbeeld van. Wie een deel kocht, deelde in de winst en in het risico.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is huisnijverheid?",
        opties=[
            "een handelaar levert grondstof aan gezinnen, die thuis het werk uitvoeren",
            "een werkplaats waar alle arbeiders samen in één grote zaal aan het werk zijn",
            "een winkel aan huis waar een ambachtsman verkoopt wat hij zelf gemaakt heeft",
            "een boerderij die alles voor eigen verbruik teelt en niets verkoopt",
        ],
        antwoord=0,
        uitleg="Zo ontweek men de regels van de stedelijke ambachten, en het loon op het platteland lag lager. Men noemt het ook het verlagsysteem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen huisnijverheid en een manufactuur?",
        opties=[
            "in een manufactuur werken de arbeiders samen op één plaats, onder toezicht",
            "in een manufactuur werkt men met machines op stoom, in huisnijverheid met de hand",
            "huisnijverheid bestaat enkel in de stad, een manufactuur enkel op het platteland",
            "een manufactuur maakt enkel voedsel, huisnijverheid enkel kleding en textiel",
        ],
        antwoord=0,
        uitleg="Nog altijd met de hand, vandaar de naam. Het samenbrengen laat wel toe het werk op te splitsen en de kwaliteit te bewaken.",
    ),
    dict(
        type="waarofniet",
        vraag="In de vroegmoderne tijd komen wisselbrieven, banken en beurzen op.",
        antwoord=True,
        uitleg="De beurs van Antwerpen, en later Amsterdam, maakt handel mogelijk zonder dat er een zak munten mee moet reizen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het vruchtwisselstelsel?",
        opties=[
            "elk jaar een ander gewas op hetzelfde veld, zodat er geen braakland meer nodig is",
            "elk jaar een derde van alle grond laten rusten, zodat de bodem kan herstellen",
            "elk jaar precies hetzelfde gewas zaaien, zodat de boer er ervaring mee opbouwt",
            "elk jaar de velden een tijd onder water zetten om het onkruid te verdrijven",
        ],
        antwoord=0,
        uitleg="Klaver en rapen geven de bodem terug wat het graan eruit haalt, en voeden ondertussen het vee. Meer vee geeft meer mest, en meer mest geeft meer graan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen landbouwproductiviteit en bevolkingsgroei?",
        opties=[
            "meer voedsel per stuk grond betekent dat er meer mensen kunnen leven",
            "meer mensen op hetzelfde gebied maakt de grond vanzelf vruchtbaarder",
            "de twee hebben niets met elkaar te maken en verlopen los van elkaar",
            "meer voedsel leidt ertoe dat er net minder mensen geboren worden",
        ],
        antwoord=0,
        uitleg="Minder hongersnood betekent ook minder sterfte. De bevolking van Europa groeit in de 18de eeuw dan ook sterk.",
    ),
    dict(
        type="waarofniet",
        vraag="De standensamenleving verdween in de vroegmoderne tijd volledig.",
        antwoord=False,
        uitleg="De standen blijven in de wet bestaan tot de Franse Revolutie. Maar een rijke koopman zonder titel past er steeds slechter in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe veranderde de verhouding tussen de sociale groepen in de vroegmoderne tijd?",
        opties=[
            "de rijke burgerij wordt machtiger dan haar stand laat vermoeden",
            "sommige adellijke families verarmen",
            "geld begint titels te kopen, door huwelijk of aankoop van een ambt",
            "de boeren worden de grootste grondbezitters",
        ],
        antwoord=[0, 1, 2],
        uitleg="De grond bleef grotendeels in handen van adel en Kerk. De drie andere bewegingen ondergraven de oude ordening wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Het zilver uit Amerika maakte Spanje op lange termijn tot het rijkste en sterkste land van Europa.",
        antwoord=False,
        uitleg="Het zilver ging naar oorlogen en naar invoer, de prijzen stegen, en de eigen nijverheid kwijnde. De winst bleef uiteindelijk bij de landen die leverden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de ontdekkingsreizen en het handelskapitalisme?",
        opties=[
            "de reizen vroegen veel kapitaal vooraf en beloofden grote winst achteraf",
            "de reizen maakten kapitaal overbodig, want de buit betaalde alles vanzelf",
            "het handelskapitalisme bestond al lang voor er enige handel gedreven werd",
            "de reizen werden volledig door de Kerk betaald en niet door handelaars",
        ],
        antwoord=0,
        uitleg="Een schip uitrusten kostte een vermogen en kon alles verliezen. Precies daarom legde men geld samen en spreidde men het risico.",
    ),
    dict(
        type="waarofniet",
        vraag="De driehoekshandel is een voorbeeld van hoe het economische en het sociale domein in elkaar grijpen.",
        antwoord=True,
        uitleg="Wat op papier een handelsstroom is, gaat over mensen die tot koopwaar gemaakt werden. Het rekenblad van een reder verbergt dat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noem je de commerciële revolutie een breuk en geen continuïteit?",
        opties=[
            "het economische systeem zelf verandert, niet alleen de hoeveelheid handel",
            "er wordt in die eeuwen voor het allereerst handel gedreven in Europa",
            "er komt in die eeuwen voor het allereerst geld in omloop in Europa",
            "alle boeren verdwijnen en iedereen gaat voortaan in de handel werken",
        ],
        antwoord=0,
        uitleg="Handel en geld bestonden al eeuwen. Nieuw is dat winst systematisch opnieuw geïnvesteerd wordt, en dat een groep daar rijk en machtig mee wordt.",
    ),
]
