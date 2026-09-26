# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Geschiedenis van België, deel 2: van 1940 tot vandaag."""

VAK = "Geschiedenis van België"
BESTAND = "geschiedenis-van-belgie.json"
TITEL = "Van de Koningskwestie tot vandaag"
VOLGORDE = 2

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Hoe lang hield het Belgische leger stand bij de Duitse inval van mei 1940?",
        "opties": [
            "Achttien dagen",
            "Vier maanden",
            "Drie dagen",
            "Bijna een jaar",
        ],
        "antwoord": 0,
        "uitleg": "De achttiendaagse veldtocht liep van 10 tot 28 mei 1940. Het Fort van Eben-Emael, dat als onneembaar gold, viel al de eerste dag doordat Duitse soldaten er met zweefvliegtuigen bovenop landden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarover ging de Koningskwestie na de Tweede Wereldoorlog?",
        "opties": [
            "Of Leopold III na zijn houding in de oorlog nog koning mocht blijven",
            "Welke zoon van Leopold III de troon zou mogen bestijgen",
            "Of België na de oorlog nog wel een koning nodig had",
            "Of de koning nog het recht had om ministers te benoemen",
        ],
        "antwoord": 0,
        "uitleg": "De koning bleef in 1940 in het land terwijl zijn regering naar Londen uitweek, en dat werd hem zwaar aangerekend. Bij de volksraadpleging van 1950 stemde bijna 58 procent voor zijn terugkeer, maar Vlaanderen en Wallonië stemden zeer verschillend.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Koningskwestie eindigde ermee dat Leopold III afstand deed van de troon.",
        "antwoord": True,
        "uitleg": "Na stakingen en zware onrust, met doden bij Grâce-Berleur, droeg hij in 1950 zijn macht over aan zijn zoon Boudewijn. Die legde in juli 1951 de eed af, negentien jaar oud, en bleef 42 jaar koning.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarover ging de Schoolstrijd van 1950 tot 1958?",
        "opties": [
            "Hoeveel geld de staat aan het vrije onderwijs mocht geven",
            "Vanaf welke leeftijd kinderen naar school moesten gaan",
            "In welke taal er in de Brusselse scholen lesgegeven werd",
            "Of meisjes en jongens samen in één klas mochten zitten",
        ],
        "antwoord": 0,
        "uitleg": "Katholieken en niet-katholieken stonden lijnrecht tegenover elkaar over de subsidies voor het katholieke onderwijs. Het Schoolpact van 1958 maakte er een einde aan: vrije keuze voor de ouders, en geld voor beide netten. Die afspraak staat er vandaag nog.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat stelt het Atomium eigenlijk voor?",
        "opties": [
            "Een kristal van ijzer, miljarden keren vergroot",
            "Een molecule water met haar waterstofatomen",
            "Het zonnestelsel met de zon in het midden",
            "Een atoom uranium zoals in een kerncentrale",
        ],
        "antwoord": 0,
        "uitleg": "Negen bollen in de vorm waarin ijzeratomen zich rangschikken, zo'n 165 miljard keer vergroot. Ingenieur André Waterkeyn ontwierp het voor de wereldtentoonstelling Expo 58 in Brussel, in volle vooruitgangsoptimisme.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk jaar werd Congo onafhankelijk van België? Geef het jaartal.",
        "antwoord": "1960",
        "uitleg": "Op 30 juni 1960, nog geen jaar nadat de eerste grote onlusten uitbraken. Patrice Lumumba werd de eerste premier; hij werd al in januari 1961 vermoord. Een Belgische onderzoekscommissie stelde in 2001 een morele verantwoordelijkheid van ons land vast.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat gebeurde er in 1962 en 1963 met de taalgrens?",
        "opties": [
            "Ze werd bij wet vastgelegd en veranderde niet meer mee met de tellingen",
            "Ze werd voor het eerst getekend, want daarvoor bestond ze niet",
            "Ze werd afgeschaft, zodat elke gemeente haar taal zelf koos",
            "Ze werd verlegd zodat Brussel volledig Nederlandstalig werd",
        ],
        "antwoord": 0,
        "uitleg": "Vóór die wetten kon de taalrol van een gemeente om de tien jaar wijzigen door de talentelling. Vlaanderen zag dat als een langzaam opschuiven van de grens. Sindsdien ligt ze vast, met een stelsel van faciliteiten in enkele gemeenten.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom werd in 1968 aan de universiteit van Leuven zo hard geprotesteerd?",
        "opties": [
            "Studenten eisten dat de Franstalige afdeling zou vertrekken",
            "Studenten eisten dat de universiteit gratis zou worden",
            "Studenten eisten dat ook meisjes mochten studeren",
            "Studenten eisten dat de universiteit naar Brussel zou verhuizen",
        ],
        "antwoord": 0,
        "uitleg": "Onder de leuze Leuven Vlaams viel zelfs de regering. De universiteit splitste in twee, en de Franstalige afdeling bouwde een volledig nieuwe stad: Louvain-la-Neuve. Zelfs de boekenverzameling werd verdeeld.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel staatshervormingen heeft België sinds 1970 doorgevoerd?",
        "opties": ["Zes", "Twee", "Vier", "Tien"],
        "antwoord": 0,
        "uitleg": "In 1970, 1980, 1988, 1993, 2001 en 2011 tot 2014. Elke keer schoven er bevoegdheden van de federale staat naar de gemeenschappen en gewesten. Zo werd een land dat als één geheel begon, stap voor stap federaal.",
    },
    {
        "type": "waarofniet",
        "vraag": "België heeft drie gewesten én drie gemeenschappen, en die vallen niet samen.",
        "antwoord": True,
        "uitleg": "De gewesten gaan over de grond: economie, wegen, milieu. De gemeenschappen gaan over de mensen: onderwijs, cultuur, welzijn. In Brussel wonen mensen van twee gemeenschappen door elkaar, dus daar zijn beide bevoegd. Vandaar dat wij zoveel regeringen hebben.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat staat er sinds 1993 in het eerste artikel van de grondwet?",
        "opties": [
            "Dat België een federale staat is van gemeenschappen en gewesten",
            "Dat België een koninkrijk is met een erfelijke koning",
            "Dat België drie officiële talen heeft op zijn grondgebied",
            "Dat België voor altijd een neutraal land wil blijven",
        ],
        "antwoord": 0,
        "uitleg": "Dat artikel staat helemaal vooraan omdat het de hele opbouw van het land samenvat. Het kwam er bij de vierde staatshervorming, dezelfde die de rechtstreekse verkiezing van de gewestparlementen invoerde.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom kwamen er vanaf 1946 veel Italiaanse arbeiders naar België?",
        "opties": [
            "België had mijnwerkers nodig en ruilde hen tegen steenkool",
            "Italië had te weinig plaats en stuurde gezinnen naar het noorden",
            "De Belgische staat wilde het Italiaans als vierde taal invoeren",
            "Ze kwamen de wegen en bruggen na de oorlog heropbouwen",
        ],
        "antwoord": 0,
        "uitleg": "Het akkoord was letterlijk mannen voor kolen: voor elke arbeider leverde België een hoeveelheid steenkool aan Italië. De opvang was hard, en op 8 augustus 1956 stierven bij de mijnramp van Marcinelle 262 mijnwerkers, van wie 136 Italianen.",
    },
    {
        "type": "waarofniet",
        "vraag": "In België wordt vandaag nog steeds steenkool gedolven.",
        "antwoord": False,
        "uitleg": "De laatste Waalse mijn sloot in 1984, de laatste Vlaamse, in Zolder, in 1992. De mijngebouwen kregen daarna een nieuw leven: op de terreinen van de mijn van Winterslag in Genk staat nu de T2-campus, waar wij ook workshops geven.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel dagen zat België in 2010 en 2011 zonder nieuwe federale regering?",
        "opties": ["541", "212", "98", "1024"],
        "antwoord": 0,
        "uitleg": "Een record dat de wereldpers haalde. De oude regering bleef al die tijd in lopende zaken doorwerken, dus het land draaide gewoon verder. Studenten organiseerden er zelfs frietrevoluties en fuiven rond.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom heet Brussel vaak de hoofdstad van Europa?",
        "opties": [
            "De Commissie en de Raad van de Europese Unie zetelen er",
            "Het Europees Parlement vergadert er als enige plaats",
            "De euro wordt er gedrukt voor alle deelnemende landen",
            "Het is de grootste stad van de Europese Unie",
        ],
        "antwoord": 0,
        "uitleg": "Officieel is geen enkele stad dé hoofdstad van de EU, maar het dagelijkse werk gebeurt grotendeels in Brussel. Het Parlement verhuist voor zijn plenaire zittingen naar Straatsburg. Ook het hoofdkwartier van de NAVO staat sinds 1967 in Brussel.",
    },
    {
        "type": "invultekst",
        "vraag": "In welk jaar kwamen de eurobiljetten en euromunten in onze portemonnee? Geef het jaartal.",
        "antwoord": "2002",
        "uitleg": "Op 1 januari 2002 verdween de Belgische frank uit het dagelijks leven. Als rekenmunt bestond de euro al sinds 1999. Eén euro was 40,3399 frank, en veel mensen rekenden nog jaren in hun hoofd terug.",
    },
    {
        "type": "waarofniet",
        "vraag": "Koning Filip volgde zijn vader Albert II op nadat die in 2013 afstand deed van de troon.",
        "antwoord": True,
        "uitleg": "Albert II was pas de tweede Belgische koning die aftrad in plaats van te sterven op de troon. Hij volgde in 1993 zijn broer Boudewijn op, die onverwacht overleed. Filip legde de eed af op 21 juli 2013.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke feestdag wordt op 11 juli gevierd, en waaraan herinnert die?",
        "opties": [
            "De Vlaamse feestdag, naar de Guldensporenslag van 1302",
            "De Waalse feestdag, naar de opstand tegen Nederland",
            "De nationale feestdag, naar de eed van Leopold I",
            "De feestdag van de Duitstalige Gemeenschap",
        ],
        "antwoord": 0,
        "uitleg": "Bij Kortrijk versloeg een leger van voetvolk uit de Vlaamse steden de Franse ridders te paard. De nationale feestdag valt op 21 juli, de Waalse in september en die van de Duitstalige Gemeenschap in november.",
    },
    {
        "type": "meerkeuze",
        "vraag": "België was in 1951 en 1957 mede-oprichter van wat later de Europese Unie werd. Waarom wilden die landen samenwerken?",
        "opties": [
            "Landen die samen handelen en produceren, voeren minder snel oorlog",
            "Europa wilde met één munt beginnen om sneller te kunnen betalen",
            "De Verenigde Staten verplichtten hen ertoe na de wereldoorlog",
            "De landen wilden samen een leger vormen tegen de Sovjet-Unie",
        ],
        "antwoord": 0,
        "uitleg": "Het begon met kolen en staal, precies de grondstoffen waarmee je wapens maakt: leg die samen onder gezamenlijk beheer en oorlog wordt praktisch veel moeilijker. Zes landen deden mee, waaronder de drie Beneluxlanden.",
    },
    {
        "type": "waarofniet",
        "vraag": "Na de bevrijding van september 1944 bleef België verder van de oorlog gespaard.",
        "antwoord": False,
        "uitleg": "In december 1944 brak in de Ardennen nog een zwaar Duits tegenoffensief uit, met Bastogne als beroemdste belegerde stad. En Antwerpen werd maandenlang met V-bommen bestookt, net omdat de geallieerden die onbeschadigde haven nodig hadden voor hun bevoorrading.",
    },
]
