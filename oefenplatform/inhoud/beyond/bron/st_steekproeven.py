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
        opties=[r"\(\mu\)", r"\(\bar{x}\)", "s", r"\(\hat{p}\)"],
        antwoord=0,
        uitleg=r"\(\mu\) is het populatiegemiddelde, \(\bar{x}\) het steekproefgemiddelde.",
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
        opties=[r"\(\hat{p}\)", r"\(p\) zonder dakje", r"\(\mu\) met index X", r"s met index \(n\)"],
        antwoord=0,
        uitleg=r"De populatieproportie is \(p\), de steekproefproportie is \(\hat{p}\) erboven.",
    ),
    dict(
        type="invultekst",
        vraag="Welke Griekse letter gebruikt de bijlage voor de populatiestandaardafwijking? Eén woord.",
        antwoord=["sigma", "σ"],
        uitleg=r"\(\sigma\) voor de populatie, de letter s voor de steekproef.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere steekproef geeft meestal een betere schatting van het populatiegemiddelde.",
        antwoord=True,
        uitleg=r"De spreiding van het steekproefgemiddelde daalt met \(\sqrt{n}\), dus meer metingen helpen.",
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
        uitleg=r"s voor de steekproef, \(\sigma\) voor de populatie. Dat onderscheid wordt op het examen nagekeken.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het populatiegemiddelde \(\mu\) is meestal een getal dat je op voorhand kent.",
        antwoord=False,
        uitleg=r"Bijna nooit. Juist omdat je \(\mu\) niet kent, neem je een steekproef en schat je het.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een stad van honderdduizend inwoners worden vierhonderd mensen bevraagd. Wat is de steekproefgrootte?",
        opties=["vierhonderd", "honderdduizend", "honderdduizend vierhonderd", "dat valt niet te zeggen"],
        antwoord=0,
        uitleg=r"\(n\) is het aantal onderzochte elementen, niet de omvang van de populatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van de vierhonderd bevraagde mensen zeggen honderd ja. Wat is de steekproefproportie?",
        opties=["nul komma vijfentwintig", "nul komma vijfenzeventig", r"\(0{,}4\)", "vier komma nul nul"],
        antwoord=0,
        uitleg="Honderd gedeeld door vierhonderd is nul komma vijfentwintig, of vijfentwintig procent. Nul komma vijfenzeventig is het deel dat geen ja zei.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De steekproefproportie \(\hat{p}\) is een getal tussen nul en één.",
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
        vraag=r"Een leerling schrijft dat het steekproefgemiddelde \(\mu\) is. Waarom is dat fout?",
        opties=[
            r"\(\mu\) staat voor het populatiegemiddelde, het steekproefgemiddelde is \(\bar{x}\)",
            r"\(\mu\) bestaat alleen bij een normale verdeling en niet bij een steekproef",
            r"\(\mu\) is geen gemiddelde maar een standaardafwijking",
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
            r"N met gemiddelde \(\mu\) en standaardafwijking \(\sigma : \sqrt{n}\)",
            r"N met gemiddelde \(\mu\) en standaardafwijking \(\sigma\)",
            r"N met gemiddelde \(\mu : n\) en standaardafwijking \(\sigma\)",
            "N met gemiddelde nul en standaardafwijking één",
        ],
        antwoord=0,
        uitleg=r"Het gemiddelde blijft \(\mu\), maar de spreiding wordt kleiner: \(\sigma : \sqrt{n}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwaarde geeft het formularium voor het benaderen van de steekproevenverdeling van het steekproefgemiddelde?",
        opties=[
            r"\(n \geq 30\)",
            r"\(n \geq 100\)",
            r"\(n \cdot p \geq 10\)",
            "de populatie is normaal verdeeld",
        ],
        antwoord=0,
        uitleg="Bij een gemiddelde is dat de enige voorwaarde. Bij een proportie komen er twee bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de steekproevenverdeling van de steekproefproportie gelden er drie voorwaarden in plaats van één.",
        antwoord=True,
        uitleg=r"\(n\) minstens dertig, \(n \cdot p\) minstens tien, en \(n \cdot (1 - p)\) minstens tien.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(n = 100\) en \(p\) gelijk aan \(0{,}2\): zijn de voorwaarden voor de steekproefproportie voldaan?",
        opties=[
            r"ja, want honderd is minstens dertig, \(n \cdot p\) is twintig en \(n \cdot (1-p)\) is tachtig",
            r"nee, want \(n \cdot p\) is te klein",
            r"nee, want \(p\) is kleiner dan \(0{,}5\)",
            r"nee, want \(n\) moet minstens tweehonderd zijn",
        ],
        antwoord=0,
        uitleg="Alle drie de getallen halen hun drempel, dus je mag de normale benadering gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(n = 40\) en \(p\) gelijk aan \(0{,}05\): mag je de normale benadering gebruiken?",
        opties=[
            r"nee, want \(n \cdot p\) is twee en dat is kleiner dan tien",
            "ja, want veertig is groter dan dertig",
            r"ja, want \(p\) ligt tussen nul en één",
            r"nee, want \(n \cdot (1-p)\) is achtendertig en dat is te groot",
        ],
        antwoord=0,
        uitleg="De eerste voorwaarde is voldaan, maar de tweede niet. Dan mag het niet.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(n\) gelijk aan vijfentwintig mag je de normale benadering voor het steekproefgemiddelde gebruiken.",
        antwoord=False,
        uitleg=r"Het formularium vraagt \(n\) minstens dertig. Vijfentwintig haalt die drempel niet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met de spreiding van het steekproefgemiddelde als \(n\) vier keer groter wordt?",
        opties=[
            "ze wordt gehalveerd",
            "ze wordt vier keer kleiner",
            "ze blijft gelijk",
            "ze wordt twee keer groter",
        ],
        antwoord=0,
        uitleg=r"Je deelt door \(\sqrt{n}\), en de wortel uit vier is twee. Vier keer meer werk voor twee keer minder spreiding.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(\sigma = 10\) en \(n = 100\), hoeveel is de standaardafwijking van het steekproefgemiddelde?",
        opties=["één", "tien", r"\(0{,}1\)", "honderd"],
        antwoord=0,
        uitleg="Tien gedeeld door de wortel uit honderd is tien gedeeld door tien, dus één.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(\sigma = 15\) en \(n\) gelijk aan tweehonderdvijfentwintig, hoeveel is \(\sigma : \sqrt{n}\)? Geef het getal in cijfers.",
        antwoord=["1", "één", "een"],
        uitleg="De wortel uit tweehonderdvijfentwintig is vijftien, en vijftien gedeeld door vijftien is één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft volgens het formularium de standaardafwijking van de steekproefproportie?",
        opties=[
            r"\(\sqrt{\dfrac{p \cdot (1-p)}{n}}\)",
            r"\(p \cdot (1-p) : n\)",
            r"\(\sqrt{n} \cdot p \cdot (1-p)\)",
            r"\(p : \sqrt{n}\)",
        ],
        antwoord=0,
        uitleg="Let op de wortel rond de hele breuk. Zonder die wortel krijg je de variantie.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het gemiddelde van de steekproevenverdeling van het steekproefgemiddelde is gelijk aan \(\mu\).",
        antwoord=True,
        uitleg=r"Steekproeven schieten wel eens hoger en wel eens lager, maar gemiddeld landen ze op \(\mu\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(p\) gelijk aan \(0{,}5\) en \(n = 100\), hoeveel is de standaardafwijking van de steekproefproportie?",
        opties=[r"\(0{,}05\)", r"\(0{,}5\)", "nul komma vijfentwintig", "vijf"],
        antwoord=0,
        uitleg=r"De wortel uit nul komma vijfentwintig gedeeld door honderd is \(\sqrt{0{,}00}\) vijfentwintig, dus \(0{,}05\).",
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
        uitleg=r"\(n\) moet minstens dertig zijn. Bij een proportie komen daar nog twee voorwaarden bij.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(n = 200\) en \(p\) gelijk aan \(0{,}02\) zijn alle voorwaarden voor de proportie voldaan.",
        antwoord=False,
        uitleg=r"\(n \cdot p\) is vier, en dat is kleiner dan tien. Bij een kleine \(p\) heb je een veel grotere steekproef nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een onderzoeker heeft \(n = 500\) en \(p\) gelijk aan \(0{,}03\). Hoe controleert hij de derde voorwaarde?",
        opties=[
            "hij rekent vijfhonderd maal nul komma zevenennegentig uit en kijkt of dat minstens tien is",
            r"hij rekent vijfhonderd gedeeld door \(0{,}03\) uit",
            r"hij kijkt of \(0{,}03\) groter is dan tien gedeeld door vijfhonderd",
            "hij rekent de wortel uit vijfhonderd uit en vergelijkt met tien",
        ],
        antwoord=0,
        uitleg=r"Dat is \(n \cdot (1 - p)\), hier \(485\). De tweede voorwaarde, \(n \cdot p\), geeft vijftien. Allebei dus in orde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de steekproevenverdeling je over één concrete steekproef?",
        opties=[
            r"hoe ver haar gemiddelde waarschijnlijk van \(\mu\) af ligt",
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
        uitleg=r"Verrassend genoeg niet. De formules gebruiken \(n\) en niet de populatiegrootte: duizend Belgen en duizend Chinezen geven dezelfde foutenmarge.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een leerling gebruikt bij een proportie de voorwaarde \(n\) minstens dertig en stopt daar. Wat gaat er mis?",
        opties=[
            r"hij vergeet \(n \cdot p\) en \(n \cdot (1-p)\) te controleren, en die kunnen falen",
            "niets, bij een proportie is dertig de enige voorwaarde",
            "hij moet de voorwaarde voor het gemiddelde gebruiken, niet die voor de proportie",
            "hij moet dertig vervangen door honderd",
        ],
        antwoord=0,
        uitleg=r"Bij een kleine of een heel grote \(p\) sneuvelt een van die twee, ook al is \(n\) groot. Dat is het hele punt van de drie voorwaarden.",
    ),
]
