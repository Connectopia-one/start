# -*- coding: utf-8 -*-
"""Populatie, steekproef en de steekproevenverdeling.

Dit thema is het scharnier van de hele fiche. Zonder het onderscheid tussen
een populatiegetal en een steekproefgetal is een hypothesetoets niet te
begrijpen, en een betrouwbaarheidsinterval al evenmin.

De bijlage Begrippen en notaties is hier streng, en de fiche zegt dat alle
andere notaties als foutief gelden:
    steekproefgemiddelde x  tegenover populatiegemiddelde mu
    steekproefstandaardafwijking s  tegenover populatiestandaardafwijking sigma
    steekproefproportie p met dakje  tegenover populatieproportie p
En ze geeft variabiliteit een eigen definitie: het fenomeen dat verschillende
steekproeven uit eenzelfde populatie verschillende resultaten kunnen
opleveren.

Het formularium geeft de voorwaarden om de steekproevenverdeling met een
normale verdeling te benaderen, en die zijn verschillend voor een gemiddelde
en voor een proportie:
    gemiddelde:  n groter dan of gelijk aan 30
    proportie:   n groter dan of gelijk aan 30, én n maal p minstens 10,
                 én n maal (1 − p) minstens 10
Dat verschil is de kern van deel 2.

Deel 1 is populatie en steekproef.
Deel 2 is de steekproevenverdeling en haar voorwaarden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een populatie in de statistiek?",
        opties=[
            "de volledige groep waarover je een uitspraak wil doen",
            "het deel van de groep dat je werkelijk onderzocht hebt",
            "het aantal mensen dat in een land woont",
            "de groep met de grootste spreiding in de data",
        ],
        antwoord=0,
        uitleg="Wil je iets weten over alle Vlaamse zestienjarigen, dan is dat je populatie, ook al bevraag je er maar driehonderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een steekproef?",
        opties=[
            "een deel van de populatie dat je werkelijk onderzoekt",
            "de volledige groep waarover je je conclusies wil trekken",
            "het gemiddelde van alle waarden in de populatie",
            "de meting die het verst van het gemiddelde ligt",
        ],
        antwoord=0,
        uitleg="Je meet de steekproef en je besluit over de populatie. Dat is de hele kunst van de statistiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool gebruikt de bijlage voor het populatiegemiddelde?",
        opties=["mu", "x met een streepje", "s", "p met een dakje"],
        antwoord=0,
        uitleg="mu is het populatiegemiddelde, x met een streepje het steekproefgemiddelde.",
    ),
    dict(
        type="waarofniet",
        vraag="Het steekproefgemiddelde en het populatiegemiddelde zijn in de regel niet precies gelijk.",
        antwoord=True,
        uitleg="Dat verschil heet steekproefvariabiliteit, en de hele statistiek is erop gebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent variabiliteit volgens de bijlage van de vakfiche?",
        opties=[
            "verschillende steekproeven uit dezelfde populatie geven verschillende resultaten",
            "de waarden in een steekproef liggen ver van elkaar",
            "het populatiegemiddelde verandert in de loop van de tijd",
            "de meetinstrumenten geven elke keer een andere waarde",
        ],
        antwoord=0,
        uitleg="Zo staat ze letterlijk in de bijlage. Bevraag je driehonderd andere mensen, dan krijg je een ander gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk symbool gebruikt de bijlage voor de steekproefproportie?",
        opties=["p met een dakje", "p zonder dakje", "mu met index X", "s met index n"],
        antwoord=0,
        uitleg="De populatieproportie is p, de steekproefproportie is p met een dakje erboven.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Griekse letter gebruikt de bijlage voor de populatiestandaardafwijking? Eén woord.",
        antwoord=["sigma", "σ"],
        uitleg="sigma voor de populatie, de letter s voor de steekproef.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere steekproef geeft meestal een betere schatting van het populatiegemiddelde.",
        antwoord=True,
        uitleg="De spreiding van het steekproefgemiddelde daalt met de wortel uit n, dus meer metingen helpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een aselecte steekproef?",
        opties=[
            "een steekproef waarbij elk lid van de populatie dezelfde kans heeft om gekozen te worden",
            "een steekproef waarbij je de deelnemers zelf uitkiest op basis van hun antwoord",
            "een steekproef van minstens dertig personen",
            "een steekproef waarvan het gemiddelde gelijk is aan dat van de populatie",
        ],
        antwoord=0,
        uitleg="Zonder aselect kiezen kan je de resultaten niet naar de populatie doortrekken, hoe groot de steekproef ook is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker vraagt alleen bezoekers van een sportclub hoeveel ze bewegen. Wat is het probleem?",
        opties=[
            "de steekproef is niet representatief voor de hele bevolking",
            "de steekproef is te klein om een gemiddelde te berekenen",
            "er is geen populatiegemiddelde om mee te vergelijken",
            "bewegen is geen variabele die je kan meten",
        ],
        antwoord=0,
        uitleg="Wie in een sportclub staat, beweegt waarschijnlijk meer dan gemiddeld. Dat heet een vertekende steekproef.",
    ),
    dict(
        type="waarofniet",
        vraag="Een steekproef van duizend mensen die je zelf uitkiest, is betrouwbaarder dan een aselecte steekproef van driehonderd.",
        antwoord=False,
        uitleg="Omvang repareert geen vertekening. Een slecht gekozen grote steekproef blijft fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een variabele in een statistisch onderzoek?",
        opties=[
            "het kenmerk dat je bij elk element van de steekproef meet",
            "het aantal elementen in je steekproef",
            "het verschil tussen de steekproef en de populatie",
            "de letter die je aan het gemiddelde geeft",
        ],
        antwoord=0,
        uitleg="Lengte, leeftijd, inkomen of studierichting: elk van die kenmerken is een variabele.",
    ),
    dict(
        type="invultekst",
        vraag="Welke letter gebruikt de bijlage voor de steekproefstandaardafwijking? Eén letter.",
        antwoord=["s"],
        uitleg="s voor de steekproef, sigma voor de populatie. Dat onderscheid wordt op het examen nagekeken.",
    ),
    dict(
        type="waarofniet",
        vraag="Het populatiegemiddelde mu is meestal een getal dat je op voorhand kent.",
        antwoord=False,
        uitleg="Bijna nooit. Juist omdat je mu niet kent, neem je een steekproef en schat je het.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een stad van honderdduizend inwoners worden vierhonderd mensen bevraagd. Wat is de steekproefgrootte?",
        opties=["vierhonderd", "honderdduizend", "honderdduizend vierhonderd", "dat valt niet te zeggen"],
        antwoord=0,
        uitleg="n is het aantal onderzochte elementen, niet de omvang van de populatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van de vierhonderd bevraagde mensen zeggen honderd ja. Wat is de steekproefproportie?",
        opties=["nul komma vijfentwintig", "nul komma vijfenzeventig", "nul komma vier", "vier komma nul nul"],
        antwoord=0,
        uitleg="Honderd gedeeld door vierhonderd is nul komma vijfentwintig, of vijfentwintig procent. Nul komma vijfenzeventig is het deel dat geen ja zei.",
    ),
    dict(
        type="waarofniet",
        vraag="De steekproefproportie p met een dakje is een getal tussen nul en één.",
        antwoord=True,
        uitleg="Het is een deel van het geheel, dus altijd tussen nul en één. Soms wordt het als percentage geschreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom neemt men een steekproef in plaats van de hele populatie te onderzoeken?",
        opties=[
            "omdat de hele populatie onderzoeken te duur of onmogelijk is",
            "omdat een steekproef altijd nauwkeuriger is dan de hele populatie",
            "omdat de wet verbiedt dat je iedereen bevraagt",
            "omdat een populatiegemiddelde nooit berekend kan worden",
        ],
        antwoord=0,
        uitleg="Alle Vlamingen bevragen kost jaren. Een goed gekozen steekproef van duizend geeft al een bruikbaar beeld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een steekproef die een goede afspiegeling van de populatie is? Eén woord.",
        antwoord=["representatief", "representatieve"],
        uitleg="Een representatieve steekproef lijkt in haar samenstelling op de populatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling schrijft dat het steekproefgemiddelde mu is. Waarom is dat fout?",
        opties=[
            "mu staat voor het populatiegemiddelde, het steekproefgemiddelde is x met een streepje",
            "mu bestaat alleen bij een normale verdeling en niet bij een steekproef",
            "mu is geen gemiddelde maar een standaardafwijking",
            "dat is niet fout, de twee symbolen mogen door elkaar gebruikt worden",
        ],
        antwoord=0,
        uitleg="De fiche zegt uitdrukkelijk dat andere notaties als foutief gelden. Dit onderscheid kost dus punten.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de steekproevenverdeling van het steekproefgemiddelde?",
        opties=[
            "de verdeling van alle gemiddelden die je uit alle mogelijke steekproeven kan krijgen",
            "de verdeling van alle waarden in één steekproef",
            "de verdeling van de populatie zelf",
            "de verdeling van de verschillen tussen de grootste en de kleinste waarde",
        ],
        antwoord=0,
        uitleg="Neem je honderd steekproeven, dan krijg je honderd gemiddelden. Die vormen samen een verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke normale verdeling benadert volgens het formularium de steekproevenverdeling van het steekproefgemiddelde?",
        opties=[
            "N met gemiddelde mu en standaardafwijking sigma gedeeld door de wortel uit n",
            "N met gemiddelde mu en standaardafwijking sigma",
            "N met gemiddelde mu gedeeld door n en standaardafwijking sigma",
            "N met gemiddelde nul en standaardafwijking één",
        ],
        antwoord=0,
        uitleg="Het gemiddelde blijft mu, maar de spreiding wordt kleiner: sigma gedeeld door de wortel uit n.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarde geeft het formularium voor het benaderen van de steekproevenverdeling van het steekproefgemiddelde?",
        opties=[
            "n is minstens dertig",
            "n is minstens honderd",
            "n maal p is minstens tien",
            "de populatie is normaal verdeeld",
        ],
        antwoord=0,
        uitleg="Bij een gemiddelde is dat de enige voorwaarde. Bij een proportie komen er twee bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de steekproevenverdeling van de steekproefproportie gelden er drie voorwaarden in plaats van één.",
        antwoord=True,
        uitleg="n minstens dertig, n maal p minstens tien, en n maal (1 − p) minstens tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij n gelijk aan honderd en p gelijk aan nul komma twee: zijn de voorwaarden voor de steekproefproportie voldaan?",
        opties=[
            "ja, want honderd is minstens dertig, n maal p is twintig en n maal (1−p) is tachtig",
            "nee, want n maal p is te klein",
            "nee, want p is kleiner dan nul komma vijf",
            "nee, want n moet minstens tweehonderd zijn",
        ],
        antwoord=0,
        uitleg="Alle drie de getallen halen hun drempel, dus je mag de normale benadering gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij n gelijk aan veertig en p gelijk aan nul komma nul vijf: mag je de normale benadering gebruiken?",
        opties=[
            "nee, want n maal p is twee en dat is kleiner dan tien",
            "ja, want veertig is groter dan dertig",
            "ja, want p ligt tussen nul en één",
            "nee, want n maal (1−p) is achtendertig en dat is te groot",
        ],
        antwoord=0,
        uitleg="De eerste voorwaarde is voldaan, maar de tweede niet. Dan mag het niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij n gelijk aan vijfentwintig mag je de normale benadering voor het steekproefgemiddelde gebruiken.",
        antwoord=False,
        uitleg="Het formularium vraagt n minstens dertig. Vijfentwintig haalt die drempel niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de spreiding van het steekproefgemiddelde als n vier keer groter wordt?",
        opties=[
            "ze wordt gehalveerd",
            "ze wordt vier keer kleiner",
            "ze blijft gelijk",
            "ze wordt twee keer groter",
        ],
        antwoord=0,
        uitleg="Je deelt door de wortel uit n, en de wortel uit vier is twee. Vier keer meer werk voor twee keer minder spreiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij sigma gelijk aan tien en n gelijk aan honderd, hoeveel is de standaardafwijking van het steekproefgemiddelde?",
        opties=["één", "tien", "nul komma één", "honderd"],
        antwoord=0,
        uitleg="Tien gedeeld door de wortel uit honderd is tien gedeeld door tien, dus één.",
    ),
    dict(
        type="invultekst",
        vraag="Bij sigma gelijk aan vijftien en n gelijk aan tweehonderdvijfentwintig, hoeveel is sigma gedeeld door de wortel uit n? Geef het getal in cijfers.",
        antwoord=["1", "één", "een"],
        uitleg="De wortel uit tweehonderdvijfentwintig is vijftien, en vijftien gedeeld door vijftien is één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft volgens het formularium de standaardafwijking van de steekproefproportie?",
        opties=[
            "de wortel uit p maal (1−p) gedeeld door n",
            "p maal (1−p) gedeeld door n",
            "de wortel uit n maal p maal (1−p)",
            "p gedeeld door de wortel uit n",
        ],
        antwoord=0,
        uitleg="Let op de wortel rond de hele breuk. Zonder die wortel krijg je de variantie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gemiddelde van de steekproevenverdeling van het steekproefgemiddelde is gelijk aan mu.",
        antwoord=True,
        uitleg="Steekproeven schieten wel eens hoger en wel eens lager, maar gemiddeld landen ze op mu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij p gelijk aan nul komma vijf en n gelijk aan honderd, hoeveel is de standaardafwijking van de steekproefproportie?",
        opties=["nul komma nul vijf", "nul komma vijf", "nul komma vijfentwintig", "vijf"],
        antwoord=0,
        uitleg="De wortel uit nul komma vijfentwintig gedeeld door honderd is de wortel uit nul komma nul nul vijfentwintig, dus nul komma nul vijf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je de voorwaarden vóór je de normale benadering gebruikt?",
        opties=[
            "omdat de benadering anders niet geldig is en je besluit dan niets waard is",
            "omdat de rekenapp anders geen antwoord geeft",
            "omdat de voorwaarden bepalen hoe groot je significantieniveau mag zijn",
            "omdat je anders met de binomiale verdeling moet rekenen in plaats van met de normale",
        ],
        antwoord=0,
        uitleg="De fiche vraagt het ook letterlijk als leerdoel: je controleert of de voorwaarden voldaan zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de minimale steekproefgrootte in het formularium voor het benaderen van de steekproevenverdeling? Geef het getal in cijfers.",
        antwoord=["30"],
        uitleg="n moet minstens dertig zijn. Bij een proportie komen daar nog twee voorwaarden bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij n gelijk aan tweehonderd en p gelijk aan nul komma nul twee zijn alle voorwaarden voor de proportie voldaan.",
        antwoord=False,
        uitleg="n maal p is vier, en dat is kleiner dan tien. Bij een kleine p heb je een veel grotere steekproef nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker heeft n gelijk aan vijfhonderd en p gelijk aan nul komma nul drie. Hoe controleert hij de derde voorwaarde?",
        opties=[
            "hij rekent vijfhonderd maal nul komma zevenennegentig uit en kijkt of dat minstens tien is",
            "hij rekent vijfhonderd gedeeld door nul komma nul drie uit",
            "hij kijkt of nul komma nul drie groter is dan tien gedeeld door vijfhonderd",
            "hij rekent de wortel uit vijfhonderd uit en vergelijkt met tien",
        ],
        antwoord=0,
        uitleg="Dat is n maal (1 − p), hier 485. De tweede voorwaarde, n maal p, geeft vijftien. Allebei dus in orde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de steekproevenverdeling je over één concrete steekproef?",
        opties=[
            "hoe ver haar gemiddelde waarschijnlijk van mu af ligt",
            "wat het exacte populatiegemiddelde is",
            "hoeveel waarden in die steekproef uitschieters zijn",
            "hoe groot de volgende steekproef moet zijn",
        ],
        antwoord=0,
        uitleg="Daarom kan je er een foutenmarge uit afleiden en een hypothese mee toetsen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe groter de populatie, hoe groter de steekproef moet zijn om dezelfde nauwkeurigheid te halen.",
        antwoord=False,
        uitleg="Verrassend genoeg niet. De formules gebruiken n en niet de populatiegrootte: duizend Belgen en duizend Chinezen geven dezelfde foutenmarge.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling gebruikt bij een proportie de voorwaarde n minstens dertig en stopt daar. Wat gaat er mis?",
        opties=[
            "hij vergeet n maal p en n maal (1−p) te controleren, en die kunnen falen",
            "niets, bij een proportie is dertig de enige voorwaarde",
            "hij moet de voorwaarde voor het gemiddelde gebruiken, niet die voor de proportie",
            "hij moet dertig vervangen door honderd",
        ],
        antwoord=0,
        uitleg="Bij een kleine of een heel grote p sneuvelt een van die twee, ook al is n groot. Dat is het hele punt van de drie voorwaarden.",
    ),
]
