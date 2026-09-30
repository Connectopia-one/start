# -*- coding: utf-8 -*-
"""De vragen voor "Reële getallen, wortels en machten".

Uit de bouwsteen Getallenleer van de vakfiche: de invoering van de reële
getallen als vervollediging van de getallenas, natuurlijke, gehele, rationale
en irrationale getallen, de drie decimale voorstellingswijzen, de verbanden
tussen decimale vorm, wortelvorm, breuk en procent, derdemachtsworteltrekking,
de eigenschappen associativiteit, commutativiteit en distributiviteit, en het
rekenen met vierkantswortels en met machten met gehele exponenten, ook in
lettervormen.

Deel 1 zijn de getalverzamelingen en de vormen. Deel 2 is het rekenwerk met
wortels en machten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom volstaan de rationale getallen niet om de getallenas te vullen?",
        opties=[
            "omdat er lengtes bestaan die je niet als breuk kan schrijven, zoals de wortel van 2",
            "omdat er tussen twee breuken altijd nog een andere breuk ligt en het dus nooit stopt",
            "omdat een breuk altijd een begrensde decimale vorm heeft en dus niet ver genoeg gaat",
            "omdat negatieve getallen geen plaats hebben in de verzameling van de breuken",
        ],
        antwoord=0,
        uitleg="De schuine zijde van een rechthoekige driehoek met rechthoekszijden 1 meet precies wortel 2, en dat is geen breuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze getallen is irrationaal?",
        opties=["de wortel van 2", "de breuk 7 op 3", "het getal 0,125", "het getal min 4"],
        antwoord=0,
        uitleg="7 op 3 is een breuk, 0,125 is 1 op 8 en min 4 is geheel. Alleen wortel 2 laat zich niet als breuk schrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tot welke verzameling behoort het getal min 7 wel, maar niet tot de kleinere ervoor?",
        opties=[
            "de gehele getallen, want min 7 is geen natuurlijk getal",
            "de natuurlijke getallen, want min 7 is een geheel aantal",
            "de irrationale getallen, want min 7 is niet positief",
            "de reële getallen, want min 7 is geen breuk te schrijven",
        ],
        antwoord=0,
        uitleg="De natuurlijke getallen beginnen bij nul en gaan omhoog. De gehele getallen nemen de negatieve erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de decimale vorm van een rationaal getal altijd?",
        opties=[
            "begrensd of onbegrensd repeterend",
            "altijd begrensd, met hoogstens drie cijfers na de komma",
            "altijd onbegrensd en nooit repeterend",
            "afhankelijk van of de teller groter is dan de noemer",
        ],
        antwoord=0,
        uitleg="1 op 4 is 0,25 en stopt. 1 op 3 is 0,333... en herhaalt. Een irrationaal getal doet geen van beide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke decimale vorm hoort bij een irrationaal getal?",
        opties=[
            "onbegrensd en niet-repeterend",
            "onbegrensd en repeterend, zoals 0,272727...",
            "begrensd, met heel veel cijfers na de komma",
            "begrensd, maar alleen in een andere talstelsel",
        ],
        antwoord=0,
        uitleg="De cijfers van pi stoppen niet en herhalen zich ook nooit in een vast patroon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke breuk hoort bij 0,75?",
        opties=["3 op 4", "7 op 5", "3 op 5", "5 op 7"],
        antwoord=0,
        uitleg="0,75 is 75 op 100, en dat vereenvoudigt tot 3 op 4. In procent is het 75 procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel procent is de breuk 2 op 5?",
        opties=["40 procent", "25 procent", "52 procent", "20 procent"],
        antwoord=0,
        uitleg="2 gedeeld door 5 is 0,4, en dat is 40 procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de derdemachtswortel van 27?",
        opties=["3", "9", "27 gedeeld door 3", "ongeveer 5,2"],
        antwoord=0,
        uitleg="3 maal 3 maal 3 is 27. Bij een vierkantswortel zou het antwoord ongeveer 5,2 zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de derdemachtswortel van 125?",
        opties=["5", "25", "15", "ongeveer 11,2"],
        antwoord=0,
        uitleg="5 tot de derde macht is 125.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap gebruik je als je 3 maal (20 plus 7) schrijft als 3 maal 20 plus 3 maal 7?",
        opties=[
            "de distributiviteit",
            "de associativiteit",
            "de commutativiteit",
            "de omgekeerde bewerking",
        ],
        antwoord=0,
        uitleg="Distributiviteit verdeelt de vermenigvuldiging over de optelling. Dat is precies hoe je handig hoofdrekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap gebruik je als je (2 plus 8) plus 5 verandert in 2 plus (8 plus 5)?",
        opties=[
            "de associativiteit",
            "de distributiviteit",
            "de commutativiteit",
            "de eigenschap van het neutraal element",
        ],
        antwoord=0,
        uitleg="Associativiteit verplaatst de haakjes. Commutativiteit zou de volgorde van de termen omdraaien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze berekeningen is enkel mogelijk in de verzameling van de reële getallen?",
        opties=[
            "de lengte van de schuine zijde van een rechthoekige driehoek met zijden 1 en 1",
            "de oppervlakte van een rechthoek met zijden 3 en 4 centimeter",
            "de helft van een oneven geheel getal uitrekenen",
            "het verschil van twee natuurlijke getallen uitrekenen",
        ],
        antwoord=0,
        uitleg="Die lengte is wortel 2 en dat is irrationaal. De andere drie blijven binnen de breuken of de gehele getallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over het getal pi klopt?",
        opties=[
            "het is irrationaal, dus geen enkele breuk geeft het exact weer",
            "het is gelijk aan de breuk 22 op 7, maar dan afgerond",
            "het is rationaal, want je kan het tot op elk cijfer berekenen",
            "het is een geheel getal zodra je het afrondt op nul cijfers",
        ],
        antwoord=0,
        uitleg="22 op 7 is een benadering, geen gelijkheid. Afronden verandert bovendien niets aan wat een getal is.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk natuurlijk getal is ook een geheel getal.",
        antwoord=True,
        uitleg="De verzamelingen zitten in elkaar: natuurlijk zit in geheel, geheel zit in rationaal, rationaal zit in reëel.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk reëel getal kan je als breuk van twee gehele getallen schrijven.",
        antwoord=False,
        uitleg="Dat geldt alleen voor de rationale getallen. Wortel 2 en pi lukken niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het getal 0,125 is rationaal.",
        antwoord=True,
        uitleg="Het is 1 op 8, en de decimale vorm stopt netjes.",
    ),
    dict(
        type="waarofniet",
        vraag="De wortel van 9 is een irrationaal getal.",
        antwoord=False,
        uitleg="De wortel van 9 is precies 3, dus zelfs een natuurlijk getal. Alleen wortels die niet opgaan zijn irrationaal.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de derdemachtswortel van 64?",
        antwoord=["4"],
        uitleg="4 maal 4 maal 4 is 64.",
    ),
    dict(
        type="invultekst",
        vraag="Schrijf 0,4 als een vereenvoudigde breuk (bijvoorbeeld 3/5).",
        antwoord=["2/5"],
        uitleg="0,4 is 4 op 10, en dat vereenvoudigt tot 2 op 5.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel procent is de breuk 3/8?",
        antwoord=["37,5", "37,5 %", "37,5 procent"],
        uitleg="3 gedeeld door 8 is 0,375.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe vereenvoudig je de wortel van 50?",
        opties=[
            "5 maal de wortel van 2",
            "2 maal de wortel van 5",
            "25 maal de wortel van 2",
            "de wortel van 25 plus de wortel van 25",
        ],
        antwoord=0,
        uitleg="50 is 25 maal 2, en de wortel van 25 is 5. Let op: wortels mag je niet zomaar optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vereenvoudig je de wortel van 72?",
        opties=[
            "6 maal de wortel van 2",
            "8 maal de wortel van 3",
            "2 maal de wortel van 6",
            "3 maal de wortel van 8",
        ],
        antwoord=0,
        uitleg="72 is 36 maal 2 en de wortel van 36 is 6. De laatste optie klopt wel qua waarde maar is niet vereenvoudigd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de wortel van 3 maal de wortel van 12?",
        opties=["6", "de wortel van 15", "36", "3 maal de wortel van 4"],
        antwoord=0,
        uitleg="Wortels mag je vermenigvuldigen onder één wortelteken: wortel van 36 is 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maak je de noemer van de breuk 1 op wortel 5 wortelvrij?",
        opties=[
            "teller en noemer vermenigvuldigen met wortel 5, wat wortel 5 op 5 geeft",
            "teller en noemer vermenigvuldigen met 5, wat 5 op wortel 25 geeft",
            "de wortel gewoon weglaten, want 1 op wortel 5 is ongeveer 1 op 2",
            "de breuk omkeren, want dan staat de wortel in de teller",
        ],
        antwoord=0,
        uitleg="Wortel 5 maal wortel 5 is 5, dus de noemer wordt een gewoon getal. De breuk zelf verandert niet van waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 2 tot de macht min 3?",
        opties=["1 op 8", "min 8", "min 6", "1 op 6"],
        antwoord=0,
        uitleg="Een negatieve exponent keert om: 2 tot de macht min 3 is 1 gedeeld door 2 tot de derde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 5 tot de macht nul?",
        opties=["1", "0", "5", "dat is niet bepaald"],
        antwoord=0,
        uitleg="Elke macht met exponent nul is 1, behalve voor het grondtal nul zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is a tot de vierde maal a tot de derde?",
        opties=["a tot de zevende", "a tot de twaalfde", "2a tot de zevende", "a tot de eerste"],
        antwoord=0,
        uitleg="Bij vermenigvuldigen tel je de exponenten op. Vermenigvuldigen doe je pas bij een macht van een macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is (a tot de derde) tot de tweede?",
        opties=["a tot de zesde", "a tot de vijfde", "2a tot de derde", "a tot de negende"],
        antwoord=0,
        uitleg="Bij een macht van een macht vermenigvuldig je de exponenten: 3 maal 2 is 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is a tot de zesde gedeeld door a kwadraat?",
        opties=["a tot de vierde", "a tot de derde", "a tot de achtste", "1 op a tot de vierde"],
        antwoord=0,
        uitleg="Bij delen trek je de exponenten af: 6 min 2 is 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de wortel van 3 plus de wortel van 3?",
        opties=[
            "2 maal de wortel van 3",
            "de wortel van 6",
            "de wortel van 9",
            "3 maal de wortel van 2",
        ],
        antwoord=0,
        uitleg="Wortels optellen gaat zoals appels optellen: twee keer hetzelfde wortelteken geeft er twee van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er mis met de bewering dat de wortel van 9 plus 16 gelijk is aan 3 plus 4?",
        opties=[
            "een wortel splitst niet over een som: wortel 25 is 5, geen 7",
            "niets, want 9 en 16 zijn allebei volkomen kwadraten",
            "de fout zit in 16, want de wortel daarvan is niet 4",
            "de volgorde klopt niet: je moet eerst worteltrekken en dan optellen",
        ],
        antwoord=0,
        uitleg="Splitsen mag bij een product en bij een quotiënt, niet bij een som of een verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is (2a) tot de derde?",
        opties=["8 a tot de derde", "2 a tot de derde", "6 a tot de derde", "8a"],
        antwoord=0,
        uitleg="De exponent geldt voor alles tussen de haakjes, dus ook voor de 2: 2 tot de derde is 8.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de wortel van a kwadraat als a negatief is?",
        opties=[
            "min a, want het resultaat is altijd positief",
            "a, want wortel en kwadraat heffen elkaar altijd op",
            "a kwadraat, want de wortel verandert niets",
            "dat kan niet berekend worden",
        ],
        antwoord=0,
        uitleg="Een vierkantswortel geeft nooit een negatief getal. Is a gelijk aan min 3, dan is de wortel van a kwadraat gelijk aan 3.",
    ),
    dict(
        type="waarofniet",
        vraag="De wortel van een product is het product van de wortels.",
        antwoord=True,
        uitleg="Dat mag: wortel van 4 maal 9 is wortel 4 maal wortel 9, dus 2 maal 3.",
    ),
    dict(
        type="waarofniet",
        vraag="De wortel van een som is de som van de wortels.",
        antwoord=False,
        uitleg="Wortel van 9 plus 16 is 5, terwijl 3 plus 4 gelijk is aan 7.",
    ),
    dict(
        type="waarofniet",
        vraag="Een negatieve exponent maakt van een macht een breuk met 1 in de teller.",
        antwoord=True,
        uitleg="3 tot de macht min 2 is 1 op 9.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het vermenigvuldigen van twee machten met hetzelfde grondtal vermenigvuldig je de exponenten.",
        antwoord=False,
        uitleg="Dan tel je ze op. Vermenigvuldigen doe je bij een macht van een macht.",
    ),
    dict(
        type="invultekst",
        vraag="Vereenvoudig de wortel van 18. Schrijf bijvoorbeeld 2 wortel 5 als 2√5.",
        antwoord=["3√2", "3 wortel 2"],
        uitleg="18 is 9 maal 2, en de wortel van 9 is 3.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is 3 tot de macht min 2? Geef het antwoord als breuk, bijvoorbeeld 1/4.",
        antwoord=["1/9"],
        uitleg="3 kwadraat is 9, en de negatieve exponent keert om.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de wortel van 5 maal de wortel van 20?",
        antwoord=["10"],
        uitleg="5 maal 20 is 100, en de wortel van 100 is 10.",
    ),
]
