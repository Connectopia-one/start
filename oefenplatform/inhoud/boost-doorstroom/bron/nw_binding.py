# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Chemische bindingen en roosters.

Chemie, de kop "Chemische bindingen" van de vakfiche natuurwetenschappen
2de graad doorstroom. Deel 1 gaat over de drie bindingstypes, de
elektronegativiteit en de Lewisstructuur; deel 2 over de vier roostertypes en
de eigenschappen die eruit volgen, met diamant en grafiet als voorbeeld.

De Lewisstructuur en het oxidatiegetal staan alleen in de uitgebreide fiche
(moderne talen en Latijn).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke binding ontstaat tussen een metaal en een niet-metaal?",
        opties=[
            "een ionbinding",
            "een atoombinding",
            "een metaalbinding",
            "een drievoudige binding",
        ],
        antwoord=0,
        uitleg="Het metaal staat elektronen af en het niet-metaal neemt ze op. De ionen die zo ontstaan trekken elkaar aan, en dat is de ionbinding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat een atoombinding, ook covalente binding genoemd?",
        opties=[
            "twee niet-metalen delen samen een of meer elektronenparen",
            "een metaal staat zijn buitenste elektronen af aan een niet-metaal",
            "de atomen laten hun elektronen vrij rondzwerven door het hele rooster",
            "de kernen van twee atomen smelten tot één grotere kern samen",
        ],
        antwoord=0,
        uitleg="Geen van de twee niet-metalen staat zijn elektronen graag af. Door een paar te delen bereiken ze samen de edelgasconfiguratie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een metaalbinding kunnen de buitenste elektronen zich vrij door het hele rooster bewegen.",
        antwoord=True,
        uitleg="Dat heet de elektronenzee. Ze verklaart waarom metalen elektriciteit geleiden en waarom je ze kan plooien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de elektronegativiteit zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze neemt in een periode toe naar rechts",
            "niet-metalen hebben een hoge elektronegativiteit",
            "metalen hebben een lage elektronegativiteit",
            "de edelgassen hebben de laagste elektronegativiteit van allemaal",
        ],
        antwoord=[0, 1, 2],
        uitleg="Naar rechts in een periode wordt een atoom gretiger naar elektronen. Metalen links zijn dat juist niet; de edelgassen vallen buiten die vergelijking omdat ze geen bindingen aangaan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het elektronenpaar van een atoom dat niet meedoet aan een binding?",
        antwoord="vrij elektronenpaar",
        uitleg="In een Lewisstructuur zet je dat paar als twee puntjes of een streepje bij het atoom zelf, niet tussen twee atomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een stof gemaakt uit twee niet-metalen. Welk bindingstype verwacht je?",
        opties=[
            "een atoombinding, want geen van beide staat elektronen graag af",
            "een ionbinding, want het ene atoom staat zijn elektronen toch af",
            "een metaalbinding, want er is een elektronenzee tussen de atomen",
            "geen enkele binding, want twee niet-metalen reageren nooit samen",
        ],
        antwoord=0,
        uitleg="Twee niet-metalen hebben beide een hoge elektronegativiteit. Delen is dan de enige weg naar een volle buitenste schil.",
    ),
    dict(
        type="waarofniet",
        vraag="In een Lewisstructuur stelt een streepje tussen twee atomen een bindend elektronenpaar voor.",
        antwoord=True,
        uitleg="Elk streepje tussen twee atomen is een gedeeld paar. De streepjes die bij één atoom staan, zijn de vrije elektronenparen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronenparen delen de twee stikstofatomen in een stikstofmolecule?",
        opties=["drie", "twee", "een", "vier"],
        antwoord=0,
        uitleg="Stikstof heeft vijf valentie-elektronen en heeft er dus drie nodig. De twee atomen delen drie paren, en dat heet een drievoudige binding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het oxidatiegetal van zuurstof in de meeste verbindingen?",
        opties=["min twee", "plus twee", "min een", "nul"],
        antwoord=0,
        uitleg="Zuurstof trekt elektronen sterk naar zich toe en krijgt daardoor meestal het oxidatiegetal min twee. In een enkelvoudige stof zoals zuurstofgas is het nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het oxidatiegetal zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "in een enkelvoudige stof is het altijd nul",
            "de som van de oxidatiegetallen in een neutrale stof is nul",
            "waterstof heeft meestal het oxidatiegetal plus een",
            "het oxidatiegetal is altijd gelijk aan de lading van het atoom",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het oxidatiegetal is een hulpmiddel om te boekhouden, geen echte lading. In een enkelvoudige stof is het nul en in een neutrale stof tellen ze samen tot nul op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof die uit twee verschillende elementen bestaat, noem je een ternaire stof.",
        antwoord=False,
        uitleg="Twee elementen is binair; ternair is er drie. Water en keukenzout zijn binair, zwavelzuur is ternair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat natrium zijn elektron af aan chloor en niet omgekeerd?",
        opties=[
            "chloor heeft een veel hogere elektronegativiteit dan natrium",
            "chloor heeft een veel kleinere kern dan natrium en trekt dus harder",
            "natrium heeft meer bezette schillen dan chloor en staat daarom af",
            "natrium heeft meer valentie-elektronen dan chloor en geeft er dus af",
        ],
        antwoord=0,
        uitleg="Chloor trekt elektronen veel sterker aan dan natrium. Natrium raakt zijn ene buitenste elektron graag kwijt, chloor heeft er juist één nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een formule-eenheid?",
        opties=[
            "de kleinste verhouding waarin de ionen in een ionrooster voorkomen",
            "de kleinste molecule die van die stof kan bestaan zonder te ontleden",
            "de massa van één mol van die stof uitgedrukt in gram per mol",
            "het aantal atomen dat in één korrel van de stof aanwezig is",
        ],
        antwoord=0,
        uitleg="Een ionrooster bestaat niet uit losse moleculen maar uit een netwerk van ionen. De formule-eenheid geeft daarvan enkel de verhouding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de binding waarbij de buitenste elektronen van alle atomen samen een zee vormen?",
        antwoord="metaalbinding",
        uitleg="De positieve metaalionen zitten in die zee van elektronen. Daardoor geleidt een metaal en breekt het niet maar plooit het.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dubbele binding tussen twee atomen betekent dat ze één elektronenpaar delen.",
        antwoord=False,
        uitleg="Bij een dubbele binding delen ze twee paren, dus vier elektronen. Eén paar is een enkelvoudige binding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel bindingen maakt een koolstofatoom gewoonlijk?",
        opties=["vier", "twee", "zes", "een"],
        antwoord=0,
        uitleg="Koolstof heeft vier valentie-elektronen en heeft er dus nog vier nodig. Daarom maakt het vier bindingen, zoals in methaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt de brutoformule van een stof met een metaal en een niet-metaal erin. Wat kan je al voorspellen?",
        opties=[
            "het is een ionverbinding, opgebouwd uit een ionrooster van ionen",
            "het is een molecule met gedeelde elektronenparen tussen de atomen",
            "het is een metaal met een elektronenzee die de ionen samenhoudt",
            "het is een edelgas dat geen enkele binding met iets anders aangaat",
        ],
        antwoord=0,
        uitleg="Een metaal met een niet-metaal geeft een ionbinding. De stof bouwt zich op als een rooster van positieve en negatieve ionen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een ionbinding worden elektronen echt overgedragen van het ene atoom naar het andere.",
        antwoord=True,
        uitleg="Daardoor ontstaan er twee ionen met tegengestelde lading. Bij een atoombinding worden de elektronen alleen gedeeld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de maat die zegt hoe sterk een atoom elektronen naar zich toe trekt?",
        antwoord="elektronegativiteit",
        uitleg="Hoe groter het verschil in elektronegativiteit tussen twee atomen, hoe meer de binding naar een ionbinding opschuift.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een Lewisstructuur?",
        opties=[
            "om te tonen welke elektronenparen gedeeld worden en welke vrij blijven",
            "om te tonen hoeveel neutronen en protonen elk atoom in de stof precies bevat",
            "om de massa van de molecule in gram per mol te kunnen berekenen",
            "om het smeltpunt van de stof in graden Celsius uit af te leiden",
        ],
        antwoord=0,
        uitleg="De Lewisstructuur tekent alleen de valentie-elektronen. Zo zie je in één oogopslag welke paren binden en welke vrij zijn.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welk roostertype hoort bij keukenzout?",
        opties=[
            "een ionrooster",
            "een molecuulrooster",
            "een atoomrooster",
            "een metaalrooster",
        ],
        antwoord=0,
        uitleg="Keukenzout is opgebouwd uit natriumionen en chloride-ionen. Die vormen samen een regelmatig ionrooster.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een stof met een ionrooster een hoog smeltpunt?",
        opties=[
            "de aantrekking tussen de ionen is in alle richtingen heel sterk",
            "de ionen zijn zo zwaar dat ze bijna niet in beweging te krijgen zijn",
            "er zitten geen elektronen in het rooster die warmte kunnen opnemen",
            "de losse moleculen in het rooster houden elkaar stevig op hun plaats",
        ],
        antwoord=0,
        uitleg="Om te smelten moet je die aantrekking in het hele rooster losbreken. Dat vraagt veel energie, dus een hoge temperatuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een molecuulrooster heeft meestal een laag smelt- en kookpunt.",
        antwoord=True,
        uitleg="Binnen de molecule zijn de bindingen sterk, maar tussen de moleculen is de aantrekking zwak. Die zwakke krachten verbreek je al bij een lage temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een metaalrooster zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het geleidt elektriciteit, ook in vaste toestand",
            "het is plooibaar in plaats van breekbaar",
            "het heeft glans",
            "het geleidt alleen elektriciteit als je het in water oplost",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vrije elektronen zorgen voor de geleiding en voor de glans, en de lagen ionen kunnen over elkaar schuiven zonder te breken. Metalen lossen niet op in water.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het roostertype van diamant, waarin elk atoom met atoombindingen aan zijn buren vastzit?",
        antwoord="atoomrooster",
        uitleg="Een atoomrooster is één groot netwerk van atoombindingen. Daarom is diamant zo hard en smelt het pas bij een enorme temperatuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geleidt keukenzout wel elektriciteit als het in water is opgelost, maar niet als vast blokje?",
        opties=[
            "in het water zijn de ionen losgekomen en kunnen ze bewegen",
            "in het water worden de ionen zelf omgezet in vrije elektronen",
            "in het water krijgen de ionen een veel grotere lading dan ervoor",
            "in het water vallen de moleculen van het zout in atomen uiteen",
        ],
        antwoord=0,
        uitleg="Stroom vraagt ladingen die zich kunnen verplaatsen. In het vaste rooster zitten de ionen vast, in water zijn ze vrij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een ionrooster is breekbaar.",
        antwoord=True,
        uitleg="Schuif je de lagen een stukje op, dan komen gelijke ladingen tegenover elkaar en stoten die elkaar af. Daardoor splijt het kristal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geleidt grafiet elektriciteit en diamant niet, terwijl ze allebei uit koolstof bestaan?",
        opties=[
            "in grafiet heeft elk atoom nog een elektron over dat vrij kan bewegen",
            "in grafiet zitten de atomen veel dichter op elkaar dan in diamant",
            "in grafiet zitten ionen in plaats van atomen in het hele rooster",
            "in grafiet zijn de atomen veel lichter dan die in een diamant",
        ],
        antwoord=0,
        uitleg="In grafiet maakt koolstof maar drie bindingen in een vlak. Het vierde elektron is vrij, en dat is precies wat geleiding nodig heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is grafiet zacht en diamant hard?",
        opties=[
            "in grafiet liggen de lagen los op elkaar en kunnen ze verschuiven",
            "in grafiet zijn de atoombindingen binnen een laag veel zwakker",
            "in grafiet zitten er veel meer vrije elektronenparen tussen de atomen",
            "in grafiet zijn de koolstofatomen zelf veel kleiner dan in diamant",
        ],
        antwoord=0,
        uitleg="De bindingen binnen een laag zijn juist heel sterk, maar tussen de lagen is de aantrekking zwak. Daardoor glijden de lagen over elkaar, en dat voelt zacht aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je stoffen die elektriciteit niet geleiden?",
        antwoord="isolatoren",
        uitleg="In een isolator kunnen de ladingen zich niet verplaatsen. Suiker en rubber zijn isolatoren, metalen en zoutoplossingen zijn geleiders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een vaste stof die glanst, stroom geleidt en plooit in plaats van breekt. Welk rooster heeft ze?",
        opties=[
            "een metaalrooster met vrije elektronen tussen de ionen",
            "een ionrooster met positieve en negatieve ionen om elkaar",
            "een molecuulrooster met losse moleculen naast elkaar",
            "een atoomrooster met een netwerk van atoombindingen",
        ],
        antwoord=0,
        uitleg="Glans, geleiding en plooibaarheid horen alle drie bij de elektronenzee. Dat is het metaalrooster.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof met een atoomrooster geleidt altijd elektriciteit, net zoals een metaal.",
        antwoord=False,
        uitleg="In een atoomrooster zitten alle elektronen vast in bindingen. Diamant geleidt daarom niet; grafiet is de uitzondering omdat daar een elektron per atoom vrij blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen zijn bij kamertemperatuur gas of vloeistof? Kruis alles aan wat juist is.",
        opties=[
            "zuurstof",
            "water",
            "koolstofdioxide",
            "keukenzout",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie hebben een molecuulrooster met zwakke krachten tussen de moleculen. Keukenzout heeft een ionrooster en is daarom vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de ionen van een zout als je het laat smelten?",
        opties=[
            "ze komen los van hun plaats en de gesmolten stof geleidt stroom",
            "ze worden omgezet in neutrale atomen zonder enige lading",
            "ze blijven precies op hun plaats, maar het rooster wordt groter",
            "ze geven hun lading door aan de moleculen van de lucht erboven",
        ],
        antwoord=0,
        uitleg="Smelten breekt het rooster, zonder de ionen zelf te veranderen. Een gesmolten zout geleidt daarom net als een zoutoplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bindingstype van een stof leid je af uit het metaal- of niet-metaalkarakter van de elementen erin.",
        antwoord=True,
        uitleg="Metaal met niet-metaal geeft een ionbinding, niet-metaal met niet-metaal een atoombinding, en metaal met metaal een metaalbinding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is suiker een isolator, ook al los je hem op in water?",
        opties=[
            "suiker valt in water niet in ionen uiteen, dus er bewegen geen ladingen",
            "suiker lost in water helemaal niet op en blijft als korrels liggen",
            "suiker neemt in water al zijn elektronen op in nieuwe bindingen",
            "suiker heeft in water een veel te hoge elektronegativiteit daarvoor",
        ],
        antwoord=0,
        uitleg="Suikermoleculen blijven in water hele moleculen. Zonder vrije ionen of vrije elektronen is er geen stroom mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap volgt rechtstreeks uit de vrije elektronen in een metaal?",
        opties=[
            "het metaal geleidt warmte en elektriciteit goed",
            "het metaal lost gemakkelijk op in een beetje water",
            "het metaal heeft een heel laag smeltpunt in vaste toestand",
            "het metaal breekt bij de minste stoot in kleine stukken",
        ],
        antwoord=0,
        uitleg="De vrije elektronen dragen zowel lading als warmte mee door het rooster. Daarom gebruiken we koper voor draden en pannen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een stof die elektriciteit goed geleidt?",
        antwoord="geleider",
        uitleg="Metalen zijn geleiders door hun vrije elektronen; zoutoplossingen en gesmolten zouten door hun vrije ionen.",
    ),
    dict(
        type="waarofniet",
        vraag="Diamant en grafiet bestaan uit verschillende elementen, en daarom verschillen hun eigenschappen zo sterk.",
        antwoord=False,
        uitleg="Ze bestaan allebei alleen uit koolstof. Het verschil zit volledig in de manier waarop die atomen in het rooster geschikt zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stof smelt bij 801 graden Celsius, is breekbaar en geleidt pas als ze gesmolten of opgelost is. Wat is ze?",
        opties=[
            "een zout met een ionrooster van positieve en negatieve ionen",
            "een metaal met een rooster van ionen in een zee van elektronen",
            "een gas met een molecuulrooster van losse kleine moleculen",
            "een diamant met een netwerk van sterke atoombindingen erin",
        ],
        antwoord=0,
        uitleg="Hoog smeltpunt, breekbaar en geleiding pas na smelten of oplossen: dat is precies het gedrag van een ionrooster.",
    ),
]
