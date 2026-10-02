# -*- coding: utf-8 -*-
"""Kunst en cultuur: een kunstwerk analyseren.

Uit de leerinhoud over beeldvorming en over het culturele domein: hoe je een
kunstwerk uit de moderne en de hedendaagse tijd leest, welke stijlen er zijn, en
hoe kunst en macht met elkaar te maken hebben.

Deel 1 gaat over de werkwijze: wat je vaststelt voor je iets besluit. Deel 2 gaat
over de stijlen van de negentiende en de twintigste eeuw en over kunst in dienst
van een regime.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Met welke stap begin je als je een kunstwerk onderzoekt?",
        opties=[
            "beschrijven wat je werkelijk ziet",
            "zeggen of je het werk mooi vindt",
            "opzoeken wat het werk heeft gekost",
            "raden wat de maker gedacht heeft",
        ],
        antwoord=0,
        uitleg="Eerst vaststellen, dan verklaren. Wie met zijn mening begint, ziet de helft niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de vormkenmerken van een kunstwerk?",
        opties=[
            "de kleuren, de lijnen en de compositie",
            "het materiaal en de techniek van de maker",
            "de prijs waarvoor het verkocht werd",
            "de mening van de bezoekers van nu",
        ],
        antwoord=[0, 1],
        uitleg="Vorm is wat je kan aanwijzen. Inhoud en betekenis komen daarna, en ze steunen daarop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de functie van een kunstwerk?",
        opties=[
            "waarvoor het gemaakt werd en waar het hing of stond",
            "hoeveel het werk vandaag op een veiling opbrengt",
            "welke kleuren de maker het meest gebruikte",
            "hoe groot het werk in centimeters is",
        ],
        antwoord=0,
        uitleg="Een altaarstuk, een portret voor een salon en een affiche voor de straat vragen elk een ander oog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort de opdrachtgever bij de analyse van een kunstwerk?",
        opties=[
            "wie betaalt, bepaalt vaak wat er te zien is",
            "de opdrachtgever maakte het werk zelf",
            "de opdrachtgever bepaalt de prijs van nu",
            "de opdrachtgever koos de kleuren van het doek",
        ],
        antwoord=0,
        uitleg="Een vorst, een stad, een kerk of een fabrikant wil in een werk iets van zichzelf terugzien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de context van een kunstwerk?",
        opties=[
            "de tijd waarin het gemaakt is",
            "de lijst waarin het schilderij gevat is",
            "de zaal van het museum waar het nu hangt",
            "de naam die de maker aan het werk gaf",
        ],
        antwoord=0,
        uitleg="De tijd en de samenleving waarin het gemaakt is. Zonder die context blijft een werk een plaatje.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de manier waarop de delen van een werk over het vlak verdeeld zijn?",
        antwoord=["de compositie", "compositie", "opbouw"],
        uitleg="Wat in het midden staat, wat groot is en waar het licht valt: dat stuurt je blik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kunstwerk is voor een historicus vooral bruikbaar als bron over wat?",
        opties=[
            "over de ideeën en de smaak van zijn eigen tijd",
            "over de exacte toedracht van de gebeurtenis die het toont",
            "over de prijzen van materialen in die eeuw",
            "over de bevolkingsaantallen van die periode",
        ],
        antwoord=0,
        uitleg="Een schilderij van een veldslag toont zelden hoe die veldslag verliep, maar wel hoe men hem wilde zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een historisch schilderij geen betrouwbaar verslag van de gebeurtenis?",
        opties=[
            "het is vaak later gemaakt en met een bedoeling",
            "het is altijd door een ooggetuige gemaakt",
            "het bevat nooit enige historische informatie",
            "het is altijd kleiner dan de werkelijkheid",
        ],
        antwoord=0,
        uitleg="De maker kiest wat hij toont, wie groot in beeld komt en wie er helemaal niet bij staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nieuwe kunstvormen kwamen in de negentiende en twintigste eeuw op?",
        opties=[
            "de fotografie",
            "de film",
            "de fresco in een kerk",
            "het glasraam in een kathedraal",
        ],
        antwoord=[0, 1],
        uitleg="Fresco's en glasramen bestonden al eeuwen. Techniek bracht daar twee volledig nieuwe media bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg had de fotografie voor de schilderkunst?",
        opties=[
            "schilders gingen op zoek naar wat een foto niet kon",
            "schilders stopten allemaal met schilderen",
            "schilders gingen alleen nog portretten maken",
            "schilders kopieerden elke foto zo nauwkeurig mogelijk",
        ],
        antwoord=0,
        uitleg="Wie de werkelijkheid niet meer hoefde na te bootsen, kon met licht, kleur en vorm aan de slag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe gebruik je een gebouw als historische bron?",
        opties=[
            "je leest er materiaal en stijl uit",
            "je leest er uitsluitend het bouwjaar van af",
            "je leest er het aantal inwoners van de stad uit",
            "je leest er de wetten van die tijd uit",
        ],
        antwoord=0,
        uitleg="Materiaal, stijl en de bedoeling van de bouwer samen. Een fabriek, een stadhuis en een werkmanshuis van dezelfde eeuw zeggen elk iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de analyse van een kunstwerk komt beschrijven voor besluiten.",
        antwoord=True,
        uitleg="Pas als je hebt vastgesteld wat er te zien is, kan je zeggen wat het betekent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kunstwerk zegt meer over de gebeurtenis die het toont dan over de tijd waarin het gemaakt is.",
        antwoord=False,
        uitleg="Het is meestal het omgekeerde: het verraadt vooral de blik van zijn eigen tijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De opdrachtgever van een werk kan de inhoud ervan bepalen.",
        antwoord=True,
        uitleg="Wie betaalt, stelt voorwaarden. Dat geldt voor een vorstenportret en voor een affiche evenzeer.",
    ),
    dict(
        type="waarofniet",
        vraag="Het materiaal waarin een werk gemaakt is, doet voor de analyse niet mee.",
        antwoord=False,
        uitleg="Marmer, beton, staal of fotopapier: elk materiaal vraagt geld, techniek en een keuze.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook een gebouw of een affiche kan je als kunstwerk analyseren.",
        antwoord=True,
        uitleg="Dezelfde vragen gelden: vorm, inhoud, functie, opdrachtgever en tijd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel van de tijd en de samenleving waarin een werk gemaakt is?",
        antwoord=["de context", "context", "de historische context"],
        uitleg="Zonder context kan je een werk beschrijven, maar niet verklaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een portret van een negentiende-eeuwse fabrikant in zijn salon. Wat besluit je uit de keuze van die omgeving?",
        opties=[
            "hij wilde zijn rijkdom en zijn stand laten zien",
            "hij werkte dagelijks in dat salon aan zijn machines",
            "hij kon zich geen ander decor veroorloven",
            "de schilder koos het decor volledig zelf",
        ],
        antwoord=0,
        uitleg="Boeken, meubels en kledij in zo'n portret zijn geen toeval, maar een boodschap aan wie kijkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je bij een propaganda-affiche uit 1940?",
        opties=[
            "wie heeft ze laten maken en voor wie was ze bedoeld",
            "welk beeld van de vijand wordt er opgeroepen",
            "hoeveel exemplaren zijn er vandaag nog bewaard",
            "welke prijs brengt ze op een veiling op",
        ],
        antwoord=[0, 1],
        uitleg="Opdrachtgever en doelpubliek maken van een affiche een bron over de bedoelingen van haar maker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet een historicus een kunstwerk naast andere bronnen?",
        opties=[
            "om te toetsen wat het werk wel en niet kan aantonen",
            "om de prijs van het werk juist te kunnen schatten",
            "om de kleuren van het werk beter te kunnen zien",
            "om de maker van het werk te kunnen ontmaskeren",
        ],
        antwoord=0,
        uitleg="Eén bron is nooit genoeg. Een werk krijgt pas gewicht naast teksten, cijfers en andere beelden.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt de romantiek in de kunst van de negentiende eeuw?",
        opties=[
            "gevoel, verbeelding en het eigen verleden",
            "koele berekening en strenge wetenschappelijke weergave",
            "het weergeven van machines en fabrieken zonder gevoel",
            "het volledig weglaten van elk herkenbaar onderwerp",
        ],
        antwoord=0,
        uitleg="Die belangstelling voor eigen taal en verleden heeft het nationalisme van die eeuw mee gevoed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het realisme in de kunst van de negentiende eeuw?",
        opties=[
            "het gewone leven en de arbeid worden zonder opsmuk getoond",
            "de helden en de vorsten worden zo groot mogelijk getoond",
            "het onderwerp verdwijnt volledig uit het werk",
            "enkel bijbelse en mythologische verhalen worden getoond",
        ],
        antwoord=0,
        uitleg="Boeren, arbeiders en armen kwamen zo in de kunst terecht. Dat was voor veel kijkers een schok.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het impressionisme?",
        opties=[
            "licht en kleur op het moment van het kijken",
            "scherpe lijnen en een glad afgewerkt oppervlak",
            "enkel zwart-wit en geen kleur",
            "enkel werken over oorlog en geweld",
        ],
        antwoord=0,
        uitleg="Buiten werken en snel schilderen hoorden erbij. De toets zelf blijft in het werk zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het expressionisme van het begin van de twintigste eeuw?",
        opties=[
            "het gevoel wordt sterker dan de juiste weergave",
            "de werkelijkheid wordt zo nauwkeurig mogelijk nagebootst",
            "er wordt uitsluitend met rechte lijnen gewerkt",
            "er worden enkel portretten van vorsten gemaakt",
        ],
        antwoord=0,
        uitleg="Vormen worden vervormd en kleuren overdreven om een gevoel over te brengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt abstracte kunst?",
        opties=[
            "er wordt niets herkenbaars uit de werkelijkheid weergegeven",
            "er wordt zo nauwkeurig mogelijk nagebootst wat men ziet",
            "er worden enkel landschappen geschilderd",
            "er wordt enkel met fotografie gewerkt",
        ],
        antwoord=0,
        uitleg="Kleur, vorm en verhouding zijn dan zelf het onderwerp geworden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke Belgische kunstenaar is wereldberoemd om zijn surrealistische schilderijen?",
        opties=[
            "René Magritte",
            "Victor Horta",
            "Peter Paul Rubens",
            "Jan van Eyck",
        ],
        antwoord=0,
        uitleg="Horta is een architect, Rubens en Van Eyck zijn van eeuwen eerder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de naam Victor Horta?",
        opties=[
            "voor de art nouveau in de Brusselse architectuur",
            "voor het surrealisme in de Belgische schilderkunst",
            "voor het impressionisme in de Franse kunst",
            "voor de abstracte kunst van na 1945",
        ],
        antwoord=0,
        uitleg="Zijn huizen in Brussel staan op de werelderfgoedlijst, met hun ijzer, glas en gebogen lijnen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de bouwstijl rond 1900 met gebogen lijnen, ijzer en glas, waarvan Horta een meester was?",
        antwoord=["art nouveau", "de art nouveau", "jugendstil"],
        uitleg="In Duitsland heet ze jugendstil. Nieuwe materialen uit de industrie maakten die vormen mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nieuwe materialen veranderden de architectuur van de negentiende en twintigste eeuw?",
        opties=[
            "staal en gewapend beton",
            "glas in grote vlakken",
            "marmer en natuursteen",
            "hout en leem",
        ],
        antwoord=[0, 1],
        uitleg="Daarmee konden stations, hallen en later wolkenkrabbers gebouwd worden. Marmer en hout waren niet nieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe gebruikte een totalitair regime de kunst?",
        opties=[
            "als propaganda, met een voorgeschreven stijl en inhoud",
            "als een volledig vrije zaak van de kunstenaar zelf",
            "als een handelsproduct voor de buitenlandse markt",
            "als iets dat volledig verboden werd in het land",
        ],
        antwoord=0,
        uitleg="Wie zich niet schikte, kon niet meer tentoonstellen of lesgeven, en soms niet meer werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed het naziregime met kunst die het afwees?",
        opties=[
            "het bestempelde ze als ontaard",
            "het kocht ze aan en hing ze in de staatsmusea",
            "het liet ze vrij tentoonstellen in het hele land",
            "het liet er een prijs voor uitreiken elk jaar",
        ],
        antwoord=0,
        uitleg="Zulke werken gingen uit de musea. Moderne en abstracte kunst werden in 1937 zelfs op een spottentoonstelling gezet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het socialistisch realisme in de Sovjet-Unie?",
        opties=[
            "een voorgeschreven stijl die arbeid verheerlijkt",
            "een vrije stijl waarin kunstenaars alles mochten tonen",
            "een stijl die uitsluitend abstracte vormen gebruikte",
            "een stijl die het leven van de adel in beeld bracht",
        ],
        antwoord=0,
        uitleg="Heldhaftige arbeiders bij machines of op het veld: de kunst moest het plan ondersteunen.",
    ),
    dict(
        type="waarofniet",
        vraag="De romantiek gaf in de negentiende eeuw veel aandacht aan het eigen verleden en de eigen taal.",
        antwoord=True,
        uitleg="Daardoor heeft ze het nationalisme van die tijd ook inhoudelijk gevoed.",
    ),
    dict(
        type="waarofniet",
        vraag="Het realisme in de kunst bracht het leven van arbeiders en boeren in beeld.",
        antwoord=True,
        uitleg="Dat was nieuw: zulke mensen waren tot dan zelden het hoofdonderwerp van een groot schilderij.",
    ),
    dict(
        type="waarofniet",
        vraag="Abstracte kunst beeldt de werkelijkheid zo nauwkeurig mogelijk af.",
        antwoord=False,
        uitleg="Zij laat het herkenbare juist weg. Kleur en vorm zijn er zelf het onderwerp.",
    ),
    dict(
        type="waarofniet",
        vraag="In een totalitaire staat was de kunstenaar volledig vrij in zijn keuzes.",
        antwoord=False,
        uitleg="Stijl en inhoud werden er voorgeschreven, en wie afweek, werd aan de kant gezet.",
    ),
    dict(
        type="waarofniet",
        vraag="Nieuwe bouwmaterialen uit de industrie maakten nieuwe bouwstijlen mogelijk.",
        antwoord=True,
        uitleg="Zonder staal en gewapend beton geen stationshallen, geen Eiffeltoren en geen wolkenkrabbers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een schilderij van arbeiders die heldhaftig bij een hoogoven staan, uit de Sovjet-Unie van 1935. Hoe lees je dat?",
        opties=[
            "als kunst in dienst van het regime en zijn plannen",
            "als een vrije keuze van een onafhankelijke kunstenaar",
            "als een aanklacht tegen de werkomstandigheden",
            "als een nauwkeurig verslag van een werkdag",
        ],
        antwoord=0,
        uitleg="Stijl, onderwerp en toon horen bij de voorgeschreven koers van die jaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt een realistisch werk uit 1870 met een abstract werk uit 1930. Welk verschil valt op?",
        opties=[
            "het eerste toont mensen, het tweede vorm en kleur",
            "het eerste is abstract, het tweede is herkenbaar",
            "beide werken tonen uitsluitend vorsten en helden",
            "beide werken zijn zonder enige kleur gemaakt",
        ],
        antwoord=0,
        uitleg="Tussen die twee ligt de breuk waarin de kunst het nabootsen heeft opgegeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen de kunst en de samenleving van de twintigste eeuw?",
        opties=[
            "de kunst volgde de breuken van haar tijd",
            "de kunst stond volledig los van haar eigen tijd",
            "de kunst is in die eeuw helemaal niet veranderd",
            "de kunst werd in die eeuw door de kerk bepaald",
        ],
        antwoord=0,
        uitleg="Oorlog, techniek, stad en massamedia zijn in die kunst allemaal terug te vinden.",
    ),
]
