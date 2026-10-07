# -*- coding: utf-8 -*-
"""Pittige hoofdstukken geschiedenis 🌱 Start.

Geen nieuwe leerstof: alles staat op wat in het gewone hoofdstuk al aan bod
komt. De verdieping zit in de vraag: redeneren met jaartallen in plaats van ze
opzeggen, een bron wegen in plaats van ze benoemen, en oorzaak en gevolg
verbinden.
"""
NIVEAU = "start"
VAK = "Geschiedenis"
BESTAND = "start-geschiedenis-pittig.json"

TIJDLIJN = [
    {
        "type": "invultekst",
        "vraag": "In welke eeuw ligt het jaar 1600? Antwoord met een getal.",
        "antwoord": "16",
        "reken": "16",
        "uitleg": "De 16de eeuw loopt van 1501 tot en met 1600. Een eeuw eindigt op het jaar met de twee nullen, dus 1600 hoort er nog bij en 1601 is de eerste van de 17de.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het jaar 1900 hoorde nog bij de 19de eeuw.",
        "antwoord": True,
        "uitleg": "Klopt. De 19de eeuw loopt van 1801 tot en met 1900. De 20ste begon pas op 1 januari 1901.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel jaar later is 20 na Chr. dan 30 v.Chr.?",
        "opties": ["49", "50", "10", "51"],
        "antwoord": 0,
        "reken": "30 + 20 - 1",
        "uitleg": "Je zou 30 + 20 = 50 zeggen, maar er bestaat geen jaar 0: na 1 v.Chr. komt meteen 1 na Chr. Daardoor is het er één minder, dus 49.",
    },
    {
        "type": "invultekst",
        "vraag": "Een gebeurtenis staat op de tijdlijn tussen 1450 en 1500. In welke eeuw ligt ze? Antwoord met een getal.",
        "antwoord": "15",
        "reken": "15",
        "uitleg": "De 15de eeuw loopt van 1401 tot en met 1500. Bij een jaartal met vier cijfers neem je de eerste twee en tel je er één bij, behalve als het op twee nullen eindigt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je hebt een brief uit 1917 van een soldaat aan zijn moeder, en een schoolboek uit 2020 over de Eerste Wereldoorlog. Wat klopt?",
        "opties": [
            "de brief is een primaire bron, het boek een secundaire",
            "allebei zijn het primaire bronnen over die oorlog",
            "de brief is een secundaire bron, het boek een primaire",
            "allebei zijn het secundaire bronnen over die oorlog",
        ],
        "antwoord": 0,
        "uitleg": "Een primaire bron komt uit de tijd zelf, een secundaire is later gemaakt op basis van andere bronnen. De brief is van 1917, het boek van honderd jaar later.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een primaire bron is altijd betrouwbaarder dan een secundaire bron.",
        "antwoord": False,
        "uitleg": "Niet waar. Wie erbij was, kan zich vergissen, overdrijven of liegen. Een historicus die tien bronnen naast elkaar legde, kan dichter bij de waarheid zitten dan één ooggetuige.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel decennia zitten er in twee eeuwen?",
        "antwoord": "20",
        "reken": "200 / 10",
        "uitleg": "Een decennium is tien jaar en twee eeuwen zijn 200 jaar: 200 : 10 = 20.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een historicus vindt maar één bron over een veldslag, geschreven door de winnaar. Wat is het verstandigste besluit?",
        "opties": [
            "je weet nu hoe de slag verliep",
            "je weet hoe de winnaar erover vertelde",
            "de slag heeft dan waarschijnlijk niet plaatsgevonden",
            "één bron over een veldslag is altijd genoeg",
        ],
        "antwoord": 1,
        "uitleg": "De winnaar vertelt zijn versie, en die is bijna nooit de hele. Zolang er geen tweede bron is, weet je wat hij zegt, niet wat er gebeurde.",
    },
    {
        "type": "waarofniet",
        "vraag": "Spreken twee bronnen elkaar tegen, dan is de oudste altijd de juiste.",
        "antwoord": False,
        "uitleg": "Niet waar. Ouder is niet hetzelfde als juister. Je kijkt wie de bron maakte, waarom, en of er nog andere bronnen zijn die hetzelfde zeggen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In een film over de middeleeuwen draagt een ridder een polshorloge. Hoe noem je zo'n fout?",
        "opties": ["een anachronisme", "een kroniek", "een tijdvak", "een generatie"],
        "antwoord": 0,
        "uitleg": "Een anachronisme is iets dat in de verkeerde tijd staat. Het polshorloge bestond pas eeuwen later.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel jaar later is 1830 dan 1789?",
        "antwoord": "41",
        "reken": "1830 - 1789",
        "uitleg": "1830 − 1789 = 41 jaar. Allebei na Christus, dus hier hoef je niets af te trekken voor het ontbrekende jaar 0.",
    },
    {
        "type": "waarofniet",
        "vraag": "De prehistorie duurde veel langer dan alle geschiedenis erna samen.",
        "antwoord": True,
        "uitleg": "Klopt, en met ruime voorsprong. De prehistorie beslaat honderdduizenden jaren; de geschreven geschiedenis pas zowat vijfduizend.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is er geen jaar 0?",
        "opties": [
            "omdat de telling gewoon begint bij het jaar 1",
            "omdat het jaar 0 verloren gegaan is in de oudheid",
            "omdat men in die tijd het cijfer nul nog niet kende",
            "omdat het jaar 0 toen een schrikkeljaar was",
        ],
        "antwoord": 0,
        "uitleg": "Onze jaartelling begint te tellen bij 1, zoals je ook bij de eerste verdieping begint en niet bij de nulde. Daardoor komt na 1 v.Chr. meteen 1 na Chr.",
    },
    {
        "type": "invultekst",
        "vraag": "De Guldensporenslag was in 1302, de Eerste Wereldoorlog begon in 1914. Hoeveel jaar later is dat?",
        "antwoord": "612",
        "reken": "1914 - 1302",
        "uitleg": "1914 − 1302 = 612 jaar, dus ruim zes eeuwen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Op een tijdlijn komt 300 v.Chr. vóór 200 v.Chr.",
        "antwoord": True,
        "uitleg": "Klopt. Bij jaren voor Christus telt het grootste getal het verst terug. 300 v.Chr. is dus ouder en staat links van 200 v.Chr.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat maakt van de prehistorie geen geschiedenis in de strikte zin?",
        "opties": [
            "er zijn geen geschreven bronnen",
            "er woonden nog geen mensen",
            "er is niets van bewaard gebleven",
            "er gebeurde niets wat de moeite van het onthouden waard was",
        ],
        "antwoord": 0,
        "uitleg": "Prehistorie betekent letterlijk “voor de geschiedenis”: de tijd voor het schrift. Er waren wel degelijk mensen, en er is heel wat van bewaard, alleen geen teksten.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk jaar begon de 20ste eeuw?",
        "antwoord": "1901",
        "reken": "1901",
        "uitleg": "De 20ste eeuw loopt van 1901 tot en met 2000. Het jaar 1900 sloot de 19de eeuw af.",
    },
    {
        "type": "waarofniet",
        "vraag": "Verhalen die mondeling van generatie op generatie doorverteld worden, kunnen nooit als bron dienen.",
        "antwoord": False,
        "uitleg": "Niet waar, ze zijn een echte bron. Wel een waar je voorzichtig mee omspringt: bij elk doorvertellen kan er iets veranderen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je wil weten wat gewone mensen in 1850 aten. Welke bron helpt je het best?",
        "opties": [
            "een rekeningenboekje van een winkel uit die tijd",
            "een schilderij van een koninklijk banket",
            "een geschiedenisboek uit 2015",
            "een roman die in 1850 speelt maar in 1990 geschreven werd",
        ],
        "antwoord": 0,
        "uitleg": "Een rekeningenboekje toont wat er echt gekocht werd, en door wie. Het banket toont net de uitzondering, en de roman is verzonnen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Historici delen de tijd in periodes op omdat die periodes vroeger echt zo bestonden.",
        "antwoord": False,
        "uitleg": "Niet waar. Niemand werd wakker met de gedachte: vandaag begint de middeleeuwen. De indeling is een afspraak achteraf, om het overzichtelijk te houden.",
    },
]

OUDHEID = [
    {
        "type": "meerkeuze",
        "vraag": "Waarom konden er pas steden ontstaan nadat de mensen aan landbouw begonnen?",
        "opties": [
            "er was voor het eerst meer voedsel dan men zelf opat",
            "omdat men toen pas stenen huizen kon bouwen",
            "omdat het klimaat toen veel warmer werd",
            "omdat men toen het wiel uitvond",
        ],
        "antwoord": 0,
        "uitleg": "Een boer die meer oogst dan hij nodig heeft, kan anderen voeden. Zo konden er mensen bestaan die geen voedsel zochten maar pot bakten, handel dreven of bestuurden. Dat is wat een stad mogelijk maakt.",
    },
    {
        "type": "waarofniet",
        "vraag": "De bronstijd kwam vóór de ijzertijd omdat brons bij een lagere temperatuur smelt dan ijzer.",
        "antwoord": True,
        "uitleg": "Klopt. Brons kon je al maken met de ovens van toen, maar voor ijzer had je veel hetere vuren nodig. Vandaar de volgorde: eerst steen, dan brons, dan ijzer.",
    },
    {
        "type": "invultekst",
        "vraag": "Welk volk noemde Julius Caesar de dappersten van alle Galliërs?",
        "antwoord": "de Belgen",
        "uitleg": "Caesar schreef dat over de Belgae, de stammen in onze streken. Het is meteen de oudste geschreven vermelding van onze naam.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een Romeinse heirbaan liep kaarsrecht door het landschap. Wat was daarvan het grootste voordeel?",
        "opties": [
            "het leger kon sneller ergens zijn",
            "de wegen waren mooier om te zien",
            "boeren konden er beter op ploegen",
            "het regenwater liep er sneller weg",
        ],
        "antwoord": 0,
        "uitleg": "Rechte wegen zijn korte wegen. Een leger dat snel van de ene grens naar de andere kon, hield een rijk van duizenden kilometers bij elkaar.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Romeinen legden hun wegen recht aan om het landschap mooier te maken.",
        "antwoord": False,
        "uitleg": "Niet waar. Het ging om snelheid: soldaten, boodschappers en handelswaar moesten zo kort mogelijk onderweg zijn.",
    },
    {
        "type": "invultekst",
        "vraag": "Waarop schreven de oude Egyptenaren, gemaakt van een rietplant?",
        "antwoord": "papyrus",
        "uitleg": "Papyrus werd uit de stengels van de papyrusplant geklopt en aan elkaar geplakt tot rollen. Ons woord papier komt ervan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In Athene mocht maar een klein deel van de bevolking meestemmen. Wie waren dat?",
        "opties": [
            "de vrije mannen uit Athene zelf",
            "alle inwoners boven de achttien",
            "alle mannen en alle vrouwen",
            "iedereen die belasting betaalde",
        ],
        "antwoord": 0,
        "uitleg": "Vrouwen, slaven en mensen van elders mochten niet meestemmen. Daardoor besliste maar een kleine minderheid mee.",
    },
    {
        "type": "waarofniet",
        "vraag": "De democratie van Athene lijkt op de onze, want iedereen mocht er meestemmen.",
        "antwoord": False,
        "uitleg": "Niet waar. Het was wel het begin van het idee, maar vrouwen, slaven en vreemdelingen stonden erbuiten. Dat was het grootste deel van de bevolking.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoe heet de periode waarin mensen nog geen metaal gebruikten en alles van steen, been en hout maakten?",
        "antwoord": "de steentijd",
        "uitleg": "De steentijd is veruit de langste periode van de menselijke geschiedenis. Pas daarna komen de bronstijd en de ijzertijd.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarvoor bouwden de Romeinen aquaducten?",
        "opties": [
            "om drinkwater naar de stad te brengen",
            "om het leger sneller te verplaatsen",
            "om de stad tegen aanvallers te beschermen",
            "om graan in op te slaan",
        ],
        "antwoord": 0,
        "uitleg": "Een aquaduct bracht vers water van een bron kilometers verderop naar de fonteinen, de thermen en de wc's van de stad, met een héél flauw verval.",
    },
    {
        "type": "waarofniet",
        "vraag": "De eerste mensen in onze streken woonden het liefst ver van water, want dat was gevaarlijk.",
        "antwoord": False,
        "uitleg": "Niet waar, ze woonden er juist graag dicht bij: drinken, vissen, en de dieren die er kwamen drinken. Water was het middelpunt, geen gevaar.",
    },
    {
        "type": "invultekst",
        "vraag": "Welke rivier zorgde in Egypte elk jaar voor vruchtbare grond door te overstromen?",
        "antwoord": "de Nijl",
        "uitleg": "De Nijl liet bij het zakken van het water een laag vruchtbaar slib achter. Zonder die jaarlijkse overstroming was Egypte woestijn gebleven.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het grootste verschil tussen een jager-verzamelaar en een boer uit de nieuwe steentijd?",
        "opties": [
            "de boer bleef op één plek wonen",
            "de boer at veel meer vlees",
            "de jager kende het vuur nog niet",
            "de boer gebruikte geen gereedschap",
        ],
        "antwoord": 0,
        "uitleg": "Een jager trok achter de dieren aan, een boer bleef bij zijn akker. Omdat boeren op één plek bleven wonen, ontstonden de eerste dorpen en later de steden.",
    },
    {
        "type": "waarofniet",
        "vraag": "In de Romeinse tijd was een slaaf wettelijk het bezit van zijn meester.",
        "antwoord": True,
        "uitleg": "Klopt. Een slaaf kon verkocht, verhuurd of erfelijk doorgegeven worden, net als een voorwerp. Vrijgelaten worden kon wel, maar dat besliste de meester.",
    },
    {
        "type": "invultekst",
        "vraag": "Welk metaal is een mengsel van koper en tin?",
        "antwoord": "brons",
        "uitleg": "Koper alleen is te zacht voor goed gereedschap. Er tin bij mengen geeft brons, dat harder is, en dat gaf de bronstijd haar naam.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe weten we iets over mensen uit de prehistorie, terwijl er geen geschreven bronnen zijn?",
        "opties": [
            "uit wat ze achterlieten: werktuigen, graven en beenderen",
            "uit verhalen die de Romeinen er veel later over opschreven",
            "uit hun kalenders en hun jaartellingen",
            "uit brieven die bewaard gebleven zijn",
        ],
        "antwoord": 0,
        "uitleg": "Archeologen graven op wat er nog ligt. Een versleten tand vertelt wat iemand at, een graf wat men over de dood dacht.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Grieken bedachten het theater, en de Romeinen namen dat later over.",
        "antwoord": True,
        "uitleg": "Klopt. De Grieken speelden al tragedies en komedies in openluchttheaters; de Romeinen bouwden er hun eigen versie van, naast het amfitheater voor de spelen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een archeoloog vindt Romeinse munten in een veld in Limburg. Wat mag hij daaruit besluiten?",
        "opties": [
            "dat er in dat gebied contact met de Romeinen was",
            "dat er op die plek zeker een Romeinse stad gestaan heeft",
            "dat de Romeinen daar een veldslag wonnen",
            "dat de bewoners daar Latijn spraken",
        ],
        "antwoord": 0,
        "uitleg": "Munten reizen: door handel, als soldij, of gewoon verloren onderweg. Ze bewijzen contact, niet dat er een stad of een slag was.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het schrift is ontstaan in Griekenland, en pas veel later in het Midden-Oosten.",
        "antwoord": False,
        "uitleg": "Niet waar, het is net andersom. In Mesopotamië en Egypte schreef men al duizenden jaren voor de Grieken hun alfabet ontwikkelden.",
    },
    {
        "type": "waarofniet",
        "vraag": "De mens temde de hond eerder dan het schaap of de koe.",
        "antwoord": True,
        "uitleg": "Klopt. De hond kwam al bij de jagers-verzamelaars, nog voor de landbouw. Schapen, geiten en koeien volgden pas toen men zich vestigde.",
    },
]

MODERN = [
    {
        "type": "meerkeuze",
        "vraag": "Wat maakte de boekdrukkunst van Gutenberg zo ingrijpend?",
        "opties": [
            "boeken werden veel goedkoper en dus veel talrijker",
            "boeken werden voor het eerst met de hand gekopieerd",
            "er kwamen voor het eerst afbeeldingen in de boeken",
            "papier werd pas door hem uitgevonden",
        ],
        "antwoord": 0,
        "uitleg": "Met losse letters kon je honderden exemplaren zetten in de tijd die een monnik over één kopie deed. Daardoor kwamen boeken, en dus ideeën, binnen het bereik van veel meer mensen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Door de boekdrukkunst verspreidden nieuwe ideeën zich veel sneller dan daarvoor.",
        "antwoord": True,
        "uitleg": "Klopt. Wie iets te zeggen had, kon het in duizenden exemplaren de wereld in sturen. Dat is een van de redenen dat de Reformatie en de Verlichting zo snel om zich heen grepen.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel jaar duurde de Eerste Wereldoorlog?",
        "antwoord": "4",
        "reken": "1918 - 1914",
        "uitleg": "Van 1914 tot 1918, dus vier jaar. De Tweede duurde er zes, van 1939 tot 1945.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De industriële revolutie begon in Engeland. Welke uitvinding was daarvoor het belangrijkst?",
        "opties": ["de stoommachine", "de auto", "de gloeilamp", "de telefoon"],
        "antwoord": 0,
        "uitleg": "De stoommachine gaf kracht die niet van mensen, dieren, wind of water kwam. Daardoor konden fabrieken overal staan en draaien wanneer men wilde.",
    },
    {
        "type": "waarofniet",
        "vraag": "De industriële revolutie maakte het leven van de arbeiders meteen beter.",
        "antwoord": False,
        "uitleg": "Niet waar. De eerste tientallen jaren betekende ze lange dagen, kinderarbeid, ongezonde fabrieken en overvolle stadswijken. Betere lonen en rechten kwamen er pas na veel strijd.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoe heet de tijd waarin geleerden de rede en het eigen onderzoek boven oude gezagsargumenten stelden?",
        "antwoord": "de Verlichting",
        "uitleg": "In de 18de eeuw vonden denkers dat je alles zelf mocht onderzoeken in plaats van iets aan te nemen omdat het altijd zo geweest was. Uit dat idee komen ook mensenrechten en scheiding van machten voort.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat hield het leenstelsel in de middeleeuwen in?",
        "opties": [
            "een heer gaf grond in ruil voor trouw en krijgsdienst",
            "een boer leende geld van de kerk",
            "een koning leende zijn kroon uit",
            "een ambachtsman leende gereedschap van zijn gilde",
        ],
        "antwoord": 0,
        "uitleg": "De koning gaf land aan zijn leenmannen, die hem daarvoor trouw zwoeren en soldaten leverden. Zo hield men een rijk bij elkaar zonder geld of ambtenaren.",
    },
    {
        "type": "waarofniet",
        "vraag": "De pest die Europa in de 14de eeuw trof, doodde ongeveer één op de honderd mensen.",
        "antwoord": False,
        "uitleg": "Niet waar, het was veel erger: naar schatting een derde van de bevolking van Europa. Hele dorpen liepen leeg.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk jaar viel de Berlijnse Muur?",
        "antwoord": "1989",
        "reken": "1989",
        "uitleg": "De Muur deelde Berlijn van 1961 tot 1989. Met haar val begon het einde van de deling van Europa in oost en west.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom werd er na de Tweede Wereldoorlog aan een Europese samenwerking begonnen?",
        "opties": [
            "om samenwerking een nieuwe oorlog te laten voorkomen",
            "om samen militair sterker te staan tegen andere landen",
            "om één taal in te voeren in heel Europa",
            "om de grenzen strenger te bewaken",
        ],
        "antwoord": 0,
        "uitleg": "Het idee was eenvoudig: landen die hun kolen en staal samen beheren, kunnen moeilijk nog oorlog tegen elkaar voeren. Daar is de Europese Unie uit gegroeid.",
    },
    {
        "type": "waarofniet",
        "vraag": "In België kregen vrouwen pas in 1948 stemrecht voor de nationale verkiezingen.",
        "antwoord": True,
        "uitleg": "Klopt. Mannen hadden dat algemeen stemrecht al sinds 1919. Vrouwen moesten er bijna dertig jaar langer op wachten.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoe heet de plicht die ervoor zorgde dat kinderen naar school moesten in plaats van te werken?",
        "antwoord": "de leerplicht",
        "uitleg": "België voerde de leerplicht in 1914 in. Ze maakte in één keer een einde aan een groot deel van de kinderarbeid.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat maakte de grote ontdekkingsreizen van de 15de en 16de eeuw mogelijk?",
        "opties": [
            "betere schepen en betere navigatie",
            "de uitvinding van de stoommachine",
            "de uitvinding van de boekdrukkunst",
            "de komst van het internet",
        ],
        "antwoord": 0,
        "uitleg": "Schepen die tegen de wind in konden varen, plus het kompas en betere kaarten, maakten de oversteek van een oceaan haalbaar. De stoommachine kwam eeuwen later.",
    },
    {
        "type": "waarofniet",
        "vraag": "De steenkoolmijnen in Limburg sloten omdat de steenkool volledig op was.",
        "antwoord": False,
        "uitleg": "Niet waar. Er zat nog kool in de grond, maar ze werd te duur om boven te halen tegenover olie, gas en goedkopere kool uit het buitenland.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel jaar zat er tussen het begin van de Eerste en het begin van de Tweede Wereldoorlog?",
        "antwoord": "25",
        "reken": "1939 - 1914",
        "uitleg": "1914 en 1939, dus 25 jaar. Veel mensen maakten allebei de oorlogen mee.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent het dat België een constitutionele monarchie is?",
        "opties": [
            "er is een koning, maar de grondwet en het parlement bepalen",
            "de koning beslist alles alleen, zoals vroeger de vorsten",
            "het volk kiest om de vier jaar een nieuwe koning",
            "er is geen koning meer",
        ],
        "antwoord": 0,
        "uitleg": "Constitutioneel verwijst naar de grondwet. De koning is staatshoofd en tekent de wetten, maar het verkozen parlement en de regering beslissen.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Holocaust was de systematische moord op zes miljoen Joden door nazi-Duitsland.",
        "antwoord": True,
        "uitleg": "Klopt. Naast de Joden werden ook Roma, mensen met een beperking, politieke tegenstanders en anderen vervolgd en vermoord.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat veranderde er in de 19de eeuw aan waar de mensen woonden?",
        "opties": [
            "veel mensen trokken van het platteland naar de steden",
            "de steden liepen net leeg",
            "er kwamen vooral kastelen bij",
            "mensen bleven precies wonen waar ze altijd woonden",
        ],
        "antwoord": 0,
        "uitleg": "De fabrieken stonden in de steden, dus daar was werk. Steden als Gent en Luik groeiden razendsnel, met woningnood en ziekte tot gevolg.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Guldensporenslag van 1302 werd gewonnen door de Franse ridders.",
        "antwoord": False,
        "uitleg": "Niet waar. Het Vlaamse voetvolk won, en dat was juist het opzienbarende: voetvolk dat een leger ridders versloeg.",
    },
    {
        "type": "invultekst",
        "vraag": "In welke eeuw vond de Franse Revolutie plaats? Antwoord met een getal.",
        "antwoord": "18",
        "reken": "18",
        "uitleg": "De Franse Revolutie begon in 1789, en dat ligt in de 18de eeuw, die loopt van 1701 tot en met 1800.",
    },
]

HOOFDSTUKKEN = [
    ("Tijd en tijdlijn", TIJDLIJN),
    ("Van de prehistorie tot de Romeinen", OUDHEID),
    ("Van de middeleeuwen tot nu", MODERN),
]
