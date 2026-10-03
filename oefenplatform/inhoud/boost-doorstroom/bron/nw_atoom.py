# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — De bouw van het atoom en het periodiek systeem.

Chemie, de kop "Atoom- en molecuulbouw" van de vakfiche natuurwetenschappen
2de graad doorstroom, met de onderdelen "Bouw en eigenschappen van atomen" en
"Opbouw periodiek systeem der elementen". Deel 1 gaat over de deeltjes in het
atoom, het atoomnummer en het massagetal; deel 2 over het PSE zelf, de
elektronenconfiguratie en de ionen.

De relatieve en de absolute massa en de atoommassa-eenheid u staan alleen in
de uitgebreide fiche (moderne talen en Latijn). Ze zitten daarom achteraan in
deel 1.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke deeltjes zitten in de atoomkern?",
        opties=[
            "protonen en neutronen",
            "protonen en elektronen",
            "neutronen en elektronen",
            "alleen elektronen",
        ],
        antwoord=0,
        uitleg="Protonen en neutronen vormen samen de kern en heten daarom nucleonen. De elektronen bewegen eromheen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de lading van de deeltjes zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "een proton is positief geladen",
            "een elektron is negatief geladen",
            "een neutron is niet geladen",
            "een neutron is positief geladen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het proton is positief, het elektron negatief en het neutron neutraal. In een atoom zijn er evenveel protonen als elektronen, dus is het geheel neutraal.",
    ),
    dict(
        type="waarofniet",
        vraag="Het atoomnummer van een element is gelijk aan het aantal protonen in de kern.",
        antwoord=True,
        uitleg="Het atoomnummer bepaalt om welk element het gaat. Verander je het aantal protonen, dan heb je een ander element.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat telt het massagetal?",
        opties=[
            "het aantal protonen plus het aantal neutronen",
            "het aantal protonen plus het aantal elektronen",
            "het aantal neutronen plus het aantal elektronen",
            "het aantal protonen in de kern alleen",
        ],
        antwoord=0,
        uitleg="De massa van een atoom zit bijna helemaal in de kern. Daarom telt het massagetal de nucleonen: protonen en neutronen samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de deeltjes in de kern, protonen en neutronen samen?",
        antwoord="nucleonen",
        uitleg="Nucleus is het Latijnse woord voor kern. De nucleonen bepalen samen het massagetal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een atoom heeft atoomnummer 11 en massagetal 23. Hoeveel neutronen zitten er in de kern?",
        opties=["12", "11", "23", "34"],
        antwoord=0,
        uitleg="Het aantal neutronen is het massagetal min het atoomnummer, dus 23 min 11 is 12.",
    ),
    dict(
        type="waarofniet",
        vraag="In een neutraal atoom zijn er evenveel protonen als elektronen.",
        antwoord=True,
        uitleg="De positieve en de negatieve ladingen heffen elkaar dan precies op. Verlies of win je elektronen, dan wordt het een ion.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar zit bijna de hele massa van een atoom?",
        opties=[
            "in de kern",
            "in de elektronenwolk",
            "gelijk verdeeld over het hele atoom",
            "in de buitenste schil",
        ],
        antwoord=0,
        uitleg="Een elektron weegt bijna tweeduizend keer minder dan een proton. De kern is heel klein maar bevat zo goed als alle massa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de relatieve atoommassa?",
        opties=[
            "de massa van een atoom vergeleken met de atoommassa-eenheid u",
            "de massa van een atoom uitgedrukt in kilogram",
            "het aantal protonen vermenigvuldigd met het aantal neutronen",
            "de massa van een mol van die stof uitgedrukt in gram",
        ],
        antwoord=0,
        uitleg="De relatieve atoommassa is een verhoudingsgetal, zonder eenheid. Je leest ze af in het periodiek systeem.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruiken we voor de atoommassa-eenheid?",
        antwoord="u",
        uitleg="Eén u is ongeveer de massa van één proton of één neutron. Daarmee wordt de relatieve atoommassa vergeleken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe reken je de absolute massa van een atoom uit?",
        opties=[
            "de relatieve atoommassa vermenigvuldigen met de waarde van één u in kilogram",
            "de relatieve atoommassa delen door de waarde van één u uitgedrukt in kilogram",
            "het massagetal optellen bij het atoomnummer van het element",
            "het aantal neutronen vermenigvuldigen met het aantal elektronen",
        ],
        antwoord=0,
        uitleg="De relatieve massa zegt hoeveel keer zwaarder dan u. Vermenigvuldig je dat met de waarde van u in kilogram, dan krijg je de echte massa.",
    ),
    dict(
        type="waarofniet",
        vraag="De relatieve atoommassa van een atoom druk je uit in kilogram.",
        antwoord=False,
        uitleg="De relatieve atoommassa is een verhoudingsgetal zonder eenheid. De absolute massa is de echte massa, en die druk je wel in kilogram uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in het PSE bij een element: atoomnummer 17. Wat weet je meteen? Kruis alles aan wat juist is.",
        opties=[
            "de kern bevat 17 protonen",
            "een neutraal atoom heeft 17 elektronen",
            "het element staat op de zeventiende plaats in het PSE",
            "de kern bevat 17 neutronen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het atoomnummer geeft de protonen, en in een neutraal atoom evenveel elektronen, en de plaats in het systeem. Het aantal neutronen lees je er niet uit af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als een atoom een elektron verliest?",
        opties=[
            "het wordt een positief ion",
            "het wordt een negatief ion",
            "het wordt een ander element",
            "het blijft neutraal",
        ],
        antwoord=0,
        uitleg="Er blijft dan een proton over waarvan de lading niet meer opgeheven wordt. Het deeltje is positief geladen, en dat heet een positief ion.",
    ),
    dict(
        type="waarofniet",
        vraag="Een atoom dat twee elektronen opneemt, krijgt daardoor een positieve lading.",
        antwoord=False,
        uitleg="Elektronen zijn negatief, dus wie er twee bij krijgt, wordt juist twee keer negatief geladen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke informatie haal je uit de symbolische voorstelling van een ion?",
        opties=[
            "om welk element het gaat en hoeveel elektronen het opgenomen of afgestaan heeft",
            "hoeveel neutronen de kern van het ion bevat en hoe zwaar het ion precies weegt",
            "in welke stoffen het ion kan voorkomen en met welke andere ionen",
            "bij welke temperatuur het ion smelt en bij welke het kookt",
        ],
        antwoord=0,
        uitleg="Het symbool zegt welk element het is; de lading rechtsboven zegt hoeveel elektronen er af of bij gekomen zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een deeltje heeft 12 protonen en 10 elektronen. Wat is het?",
        opties=[
            "een positief ion met lading 2 plus",
            "een negatief ion met lading 2 min",
            "een neutraal atoom van dat element",
            "een atoom met massagetal 22",
        ],
        antwoord=0,
        uitleg="Er zijn twee positieve ladingen meer dan negatieve, dus het deeltje is twee keer positief. Het is een magnesiumion.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een atoom dat elektronen heeft opgenomen of afgestaan en daardoor geladen is?",
        antwoord="ion",
        uitleg="Een ion ontstaat door elektronen te winnen of te verliezen. Het aantal protonen blijft hetzelfde, dus het blijft hetzelfde element.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee atomen van hetzelfde element kunnen een verschillend aantal neutronen hebben.",
        antwoord=True,
        uitleg="Dat zijn isotopen. Hun atoomnummer is gelijk, hun massagetal niet, en chemisch gedragen ze zich hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een atoom als geheel elektrisch neutraal?",
        opties=[
            "er zijn evenveel protonen als elektronen, en hun ladingen heffen elkaar op",
            "de neutronen in de kern maken de ladingen van alle andere deeltjes onschadelijk",
            "de elektronen bewegen zo snel dat hun lading wegvalt",
            "de kern is zo klein dat zijn lading niet meetelt",
        ],
        antwoord=0,
        uitleg="Elke positieve lading in de kern heeft een negatieve tegenhanger in de elektronenwolk. Samen geeft dat nul.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een periode in het periodiek systeem?",
        opties=[
            "een horizontale rij",
            "een verticale kolom",
            "een blok van acht elementen",
            "een groep metalen onderaan",
        ],
        antwoord=0,
        uitleg="De perioden lopen van links naar rechts. Het periodenummer zegt hoeveel bezette schillen een atoom van dat element heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben de elementen van eenzelfde hoofdgroep gemeen?",
        opties=[
            "ze hebben evenveel valentie-elektronen",
            "ze hebben evenveel bezette schillen",
            "ze hebben hetzelfde massagetal",
            "ze hebben hetzelfde atoomnummer",
        ],
        antwoord=0,
        uitleg="Het groepsnummer van een hoofdgroep geeft het aantal elektronen in de buitenste schil. Daardoor reageren die elementen op een vergelijkbare manier.",
    ),
    dict(
        type="waarofniet",
        vraag="Het periodenummer geeft het aantal bezette schillen van een atoom.",
        antwoord=True,
        uitleg="Een element uit periode 3 heeft drie bezette schillen. Daarom worden de atomen naar onder toe groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen passen er in de eerste en in de tweede schil volgens het model van Bohr?",
        opties=[
            "2 in de eerste en 8 in de tweede",
            "8 in de eerste en 8 in de tweede",
            "2 in de eerste en 2 in de tweede",
            "8 in de eerste en 18 in de tweede",
        ],
        antwoord=0,
        uitleg="De eerste schil is vol met twee elektronen, de tweede met acht. Daarom hebben helium en neon allebei een volle buitenste schil.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de elektronen in de buitenste schil van een atoom?",
        antwoord="valentie-elektronen",
        uitleg="De valentie-elektronen doen mee aan de bindingen. Hun aantal bepaalt hoe een element zich chemisch gedraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de elektronenconfiguratie van een natriumatoom met atoomnummer 11?",
        opties=["2, 8, 1", "2, 8, 8", "8, 2, 1", "2, 9"],
        antwoord=0,
        uitleg="Je vult de schillen van binnen naar buiten: eerst twee, dan acht, en de elfde komt alleen in de derde schil. Dat ene buitenste elektron geeft natrium zijn gedrag.",
    ),
    dict(
        type="waarofniet",
        vraag="Een atoom met een volle buitenste schil is weinig reactief.",
        antwoord=True,
        uitleg="Dat is de edelgasconfiguratie. Zo'n atoom hoeft geen elektronen af te staan of op te nemen, en gaat dus bijna geen bindingen aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat natrium graag één elektron af?",
        opties=[
            "daardoor houdt het een volle schil over, zoals een edelgas",
            "daardoor wordt het atoom zwaarder en dus veel stabieler dan het daarvoor was",
            "daardoor verliest het een proton uit zijn kern",
            "daardoor wordt het een atoom van een ander element",
        ],
        antwoord=0,
        uitleg="Na het afstaan blijft de configuratie 2, 8 over, net die van neon. Het natriumion is daardoor veel stabieler dan het atoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het metaalkarakter in het PSE zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "links in het systeem staan de metalen",
            "rechtsboven staan de niet-metalen",
            "helemaal rechts staat de groep van de edelgassen",
            "het metaalkarakter neemt naar rechts toe",
        ],
        antwoord=[0, 1, 2],
        uitleg="Metalen staan links en in het midden, niet-metalen rechtsboven, en de laatste kolom zijn de edelgassen. Naar rechts neemt het metaalkarakter juist af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de bijzonder stabiele elektronenverdeling met een volle buitenste schil?",
        antwoord="edelgasconfiguratie",
        uitleg="Elementen gaan bindingen aan tot ze die configuratie bereiken, door elektronen af te staan, op te nemen of te delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een element staat in groep 2 en in periode 4. Wat weet je over zijn atoom?",
        opties=[
            "het heeft twee valentie-elektronen en vier bezette schillen",
            "het heeft vier valentie-elektronen en twee bezette schillen",
            "het heeft twee protonen en vier neutronen in de kern",
            "het heeft twee bezette schillen en vier elektronen in totaal",
        ],
        antwoord=0,
        uitleg="Het groepsnummer van een hoofdgroep geeft de valentie-elektronen, het periodenummer geeft de bezette schillen.",
    ),
    dict(
        type="waarofniet",
        vraag="De elementen van groep 1 nemen gemakkelijk zeven elektronen op om aan een volle schil te komen.",
        antwoord=False,
        uitleg="Met één elektron in de buitenste schil is dat ene afstaan veel eenvoudiger dan er zeven opnemen. Daarom zijn die metalen zo reactief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom neemt een zuurstofatoom liever twee elektronen op dan er zes af te staan?",
        opties=[
            "twee opnemen vraagt veel minder dan zes afstaan om de volle schil te bereiken",
            "zuurstof kan helemaal geen elektronen afstaan aan andere atomen",
            "zuurstof wordt daardoor een positief ion, en dat is stabieler",
            "zuurstof heeft al een volle buitenste schil en moet dus helemaal niets veranderen",
        ],
        antwoord=0,
        uitleg="Zuurstof heeft zes valentie-elektronen en heeft er dus nog twee nodig voor een volle schil van acht. Twee opnemen is veel eenvoudiger dan er zes kwijtraken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lading krijgt een ion van een element uit groep 2?",
        opties=["2 plus", "2 min", "1 plus", "6 min"],
        antwoord=0,
        uitleg="Die elementen staan hun twee valentie-elektronen af. Daardoor houden ze twee positieve ladingen over.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal valentie-elektronen van een hoofdgroepelement lees je af aan het periodenummer.",
        antwoord=False,
        uitleg="Dat lees je af aan het groepsnummer. Het periodenummer geeft het aantal bezette schillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elementen horen bij de edelgassen? Kruis alles aan wat juist is.",
        opties=["helium", "neon", "argon", "waterstof"],
        antwoord=[0, 1, 2],
        uitleg="Helium, neon en argon staan in de laatste kolom en hebben een volle buitenste schil. Waterstof staat helemaal links en is geen edelgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijken de eigenschappen van elementen in eenzelfde groep zo sterk op elkaar?",
        opties=[
            "ze hebben evenveel elektronen in hun buitenste schil",
            "ze hebben evenveel neutronen in hun kern",
            "ze hebben precies dezelfde relatieve atoommassa",
            "ze staan alle vier in dezelfde periode van het PSE",
        ],
        antwoord=0,
        uitleg="Het chemische gedrag wordt bepaald door de buitenste schil. Zijn die gelijk, dan reageren de elementen op dezelfde manier.",
    ),
    dict(
        type="waarofniet",
        vraag="Een atoom en zijn ion hebben hetzelfde aantal protonen.",
        antwoord=True,
        uitleg="Alleen de elektronen veranderen. Zou het aantal protonen veranderen, dan had je een ander element.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een verticale kolom in het periodiek systeem?",
        antwoord="groep",
        uitleg="De elementen van één groep hebben evenveel valentie-elektronen en lijken daarom sterk op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een deeltje met 17 protonen en 18 elektronen. Hoe noteer je het?",
        opties=[
            "als een chloride-ion met lading 1 min",
            "als een chlooratoom zonder enige lading",
            "als een argonatoom zonder enige lading",
            "als een chloride-ion met lading 1 plus",
        ],
        antwoord=0,
        uitleg="Atoomnummer 17 is chloor. Eén elektron te veel geeft één negatieve lading, en zo bereikt het de configuratie van argon.",
    ),
]
