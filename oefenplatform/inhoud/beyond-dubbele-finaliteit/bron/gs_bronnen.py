# -*- coding: utf-8 -*-
"""Redeneren met bronnen: bruikbaarheid en betrouwbaarheid.

Uit de leerinhoud over bronnen, het zwaarste onderdeel van de vakfiche: soorten
bronnen, een historische vraag stellen, nagaan of een bron bruikbaar is voor die
vraag, en nagaan of ze betrouwbaar is.

Deel 1 gaat over de soorten bronnen en over bruikbaarheid. Deel 2 gaat over
betrouwbaarheid, over het verschil tussen feit en mening, en over bronnen op het
internet.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een primaire bron?",
        opties=[
            "een bron uit de tijd van de gebeurtenis zelf",
            "een bron die later over de gebeurtenis schrijft",
            "een bron die in een handboek staat afgedrukt",
            "een bron die door een historicus geschreven is",
        ],
        antwoord=0,
        uitleg="Een brief, een foto, een register of een voorwerp van die tijd. Wie later schrijft, is secundair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een secundaire bron?",
        opties=[
            "een werk dat later over de gebeurtenis geschreven is",
            "een voorwerp uit de tijd van de gebeurtenis",
            "een getuigenis van iemand die erbij was",
            "een brief die tijdens de gebeurtenis verstuurd werd",
        ],
        antwoord=0,
        uitleg="Een handboek of een studie van een historicus bijvoorbeeld. Zij verwerken primaire bronnen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een bron die uit de tijd van de gebeurtenis zelf komt?",
        antwoord=["een primaire bron", "primaire bron", "primair"],
        uitleg="Zij is niet automatisch betrouwbaarder, maar ze staat wel het dichtst bij wat gebeurde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten bronnen gebruikt een historicus?",
        opties=[
            "schriftelijke bronnen, zoals brieven, kranten en registers",
            "materiële bronnen, zoals gebouwen, werktuigen en munten",
            "uitsluitend de handboeken en studies van historici",
            "uitsluitend bronnen die in een museum bewaard worden",
        ],
        antwoord=[0, 1],
        uitleg="Daar komen beeldbronnen, mondelinge getuigenissen en digitale bronnen bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom begin je een onderzoek met een historische vraag?",
        opties=[
            "zonder vraag kan je niet beoordelen wat je nodig hebt",
            "zonder een vraag mag je geen enkele bron gaan lezen",
            "zonder een vraag kan je geen bron samenvatten of citeren",
            "zonder een vraag bestaat er over dat thema geen bron",
        ],
        antwoord=0,
        uitleg="Bruikbaarheid bestaat niet in het algemeen: een bron is bruikbaar voor een bepaalde vraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is een bron bruikbaar voor je onderzoek?",
        opties=[
            "als ze over thema, tijd en plaats van je vraag gaat",
            "als ze zo oud mogelijk is en van een ooggetuige komt",
            "als ze door een bekende historicus geschreven is",
            "als ze zo kort mogelijk is om te kunnen lezen",
        ],
        antwoord=0,
        uitleg="Een betrouwbare bron over de verkeerde plaats of tijd blijft voor jouw vraag onbruikbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt het dagelijks leven van mijnwerkers in Limburg rond 1950. Welke bron is bruikbaar?",
        opties=[
            "een dagboek van een mijnwerker uit Zolder",
            "een wet over de mijnen in Engeland uit 1850",
            "een krantenartikel over de Koude Oorlog",
            "een studie over de Romeinse mijnbouw",
        ],
        antwoord=0,
        uitleg="Thema, tijd en plaats kloppen alle drie. Dat is de toets voor bruikbaarheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een anachronisme?",
        opties=[
            "iets uit een andere tijd in een verkeerde tijd plaatsen",
            "een bron die in een vreemde taal is opgetekend",
            "een bron waarvan de naam van de auteur onbekend is",
            "een bron die door twee verschillende mensen gemaakt is",
        ],
        antwoord=0,
        uitleg="Zoals spreken over de Belgen in de tijd van de Romeinen zoals wij het woord vandaag bedoelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat je een bron in zijn context moet lezen?",
        opties=[
            "je leest ze met de tijd en de omstandigheden erbij",
            "je leest ze met de ogen en de kennis van vandaag",
            "je leest ze zonder iets over de auteur te weten",
            "je leest ze alleen in een moderne vertaling",
        ],
        antwoord=0,
        uitleg="Woorden en ideeën betekenden in 1850 niet hetzelfde als vandaag. Zonder context lees je ze fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is representativiteit van een bron?",
        opties=[
            "de vraag of ze voor een hele groep geldt",
            "de vraag of ze in een museum bewaard wordt",
            "de vraag of ze in het Nederlands geschreven is",
            "de vraag of ze door een overheid gemaakt is",
        ],
        antwoord=0,
        uitleg="Eén dagboek van één mijnwerker vertelt over hem. Voor alle mijnwerkers heb je meer nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vermeld je altijd waar je een bron gevonden hebt?",
        opties=[
            "zodat anderen je werk kunnen nagaan en controleren",
            "zodat je tekst wat langer en voller wordt",
            "zodat je de bron zelf niet meer hoeft te lezen",
            "zodat je zelf als de auteur mag doorgaan",
        ],
        antwoord=0,
        uitleg="Zonder bronvermelding is een besluit niet te controleren, en overnemen zonder vermelding is plagiaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het overnemen van het werk van iemand anders zonder dat te vermelden?",
        antwoord=["plagiaat", "plagiaat plegen", "plagiëren"],
        uitleg="Ook een tekst die een computerprogramma voor je schrijft, moet je als zo'n hulp vermelden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een primaire bron is altijd betrouwbaarder dan een secundaire bron.",
        antwoord=False,
        uitleg="Een ooggetuige kan zich vergissen of belang hebben. Een latere studie kan juist alles naast elkaar leggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Of een bron bruikbaar is, hangt af van de vraag die je stelt.",
        antwoord=True,
        uitleg="Daarom begin je met je vraag en niet met je bronnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gebouw of een werktuig kan ook een historische bron zijn.",
        antwoord=True,
        uitleg="Dat zijn materiële bronnen. Zij vertellen over techniek, geld en dagelijks leven.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén enkele bron is genoeg om een historisch besluit te onderbouwen.",
        antwoord=False,
        uitleg="Je legt bronnen naast elkaar. Wat verschillende bronnen bevestigen, staat sterker.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bron uit de tijd zelf lees je best met de kennis van haar eigen tijd erbij.",
        antwoord=True,
        uitleg="Anders lees je er betekenissen in die er voor de tijdgenoten niet in zaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je altijd bij een bron?",
        opties=[
            "wie heeft ze gemaakt, en wanneer",
            "voor wie was ze bedoeld, en met welk doel",
            "hoeveel ze vandaag waard is",
            "in welk museum ze nu ligt",
        ],
        antwoord=[0, 1],
        uitleg="Auteur, tijd, publiek en doel: die vier vragen brengen je al heel ver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt hoe de bezetter in 1942 over het verzet sprak. Welke bron past daarbij het best?",
        opties=[
            "een krant die onder censuur van de bezetter verscheen",
            "een studie van een historicus die in 1990 verscheen",
            "een dagboek van iemand die bij het verzet zat",
            "een handboek voor het middelbaar van vandaag",
        ],
        antwoord=0,
        uitleg="Voor de vraag hoe de bezetter sprak, is zijn eigen pers juist de beste bron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een gecensureerde krant uit 1942 toch een waardevolle bron?",
        opties=[
            "ze toont wat de bezetter wilde laten lezen",
            "ze geeft de feiten van die dagen juist weer",
            "ze is volledig onafhankelijk geschreven",
            "ze bevat geen enkele vorm van propaganda",
        ],
        antwoord=0,
        uitleg="Een onbetrouwbare bron over de feiten kan een uitstekende bron over de bedoelingen zijn.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarnaar kijk je om de betrouwbaarheid van een bron te beoordelen?",
        opties=[
            "wie de auteur is en welk belang hij kan hebben",
            "hoe dicht de bron bij de gebeurtenis staat",
            "hoe mooi en verzorgd de bron is opgemaakt",
            "hoe lang en hoe uitvoerig de bron is",
        ],
        antwoord=[0, 1],
        uitleg="Daar komt bij of andere bronnen hetzelfde zeggen, en of de bron volledig bewaard is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent standplaatsgebondenheid?",
        opties=[
            "iemand kijkt naar de wereld van waar hij zelf staat",
            "een bron hoort altijd in één bepaald museum",
            "een gebeurtenis gebeurt altijd op één plaats",
            "een historicus mag enkel zijn eigen streek onderzoeken",
        ],
        antwoord=0,
        uitleg="Afkomst, tijd, geloof en belang bepalen mee wat iemand ziet. Dat geldt ook voor de historicus zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een feit en een mening?",
        opties=[
            "een feit is te controleren, een mening is een standpunt",
            "een feit staat in een krant, een mening in een boek",
            "een feit is altijd ouder dan een mening",
            "een feit komt van een historicus, een mening van een getuige",
        ],
        antwoord=0,
        uitleg="In één zin kunnen ze samen zitten. Leren scheiden is een deel van het vak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een waardeoordeel?",
        opties=[
            "een uitspraak die iets goed of slecht noemt",
            "een uitspraak die een datum of een jaar vastlegt",
            "een uitspraak die een aantal noemt",
            "een uitspraak die een plaats aanwijst",
        ],
        antwoord=0,
        uitleg="Een historicus mag er een hebben, maar hij moet het onderscheiden van wat hij vaststelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als twee bronnen elkaar tegenspreken?",
        opties=[
            "je zoekt uit wie welk belang had",
            "je neemt de langste bron van de twee",
            "je neemt de bron die je zelf het best bevalt",
            "je laat de vraag onbeantwoord en stopt ermee",
        ],
        antwoord=0,
        uitleg="En je zoekt bronnen bij. Een tegenspraak is geen probleem maar een aanwijzing: er valt iets uit te leggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een getuigenis van vijftig jaar later minder betrouwbaar over details?",
        opties=[
            "het geheugen verandert met de tijd",
            "de getuige was er niet bij toen het gebeurde",
            "een getuigenis is nooit een bron voor een historicus",
            "oude mensen vertellen nooit de waarheid",
        ],
        antwoord=0,
        uitleg="Wat je later hoorde, kruipt in je herinnering. Over de beleving blijft zo'n getuigenis wel heel waardevol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met een bron waarvan de auteur onbekend is?",
        opties=[
            "je gebruikt ze voorzichtig en toetst ze",
            "je verwerpt ze meteen en vermeldt ze niet",
            "je gebruikt ze zonder enig voorbehoud",
            "je verzint zelf een waarschijnlijke auteur",
        ],
        antwoord=0,
        uitleg="Soms is de inhoud of de herkomst toch te plaatsen. Je zegt dan wat je niet weet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vermeldt een historicus de datum van een bron altijd?",
        opties=[
            "de afstand tot de gebeurtenis telt mee",
            "de datum maakt de bron automatisch betrouwbaar",
            "de datum zegt wie de auteur geweest is",
            "de datum bepaalt in welk museum ze ligt",
        ],
        antwoord=0,
        uitleg="Een verslag van dezelfde week en een terugblik van dertig jaar later wegen anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je na of een website betrouwbaar is?",
        opties=[
            "je kijkt wie erachter zit en van wanneer ze is",
            "je kijkt of ze mooi vormgegeven is",
            "je kijkt hoe hoog ze in de zoekresultaten staat",
            "je kijkt hoeveel reacties er onder staan",
        ],
        antwoord=0,
        uitleg="Wie iets publiceert en met welke bedoeling: dat is op het internet dezelfde vraag als op papier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met een opvallend bericht dat je op sociale media tegenkomt?",
        opties=[
            "je zoekt of onafhankelijke bronnen hetzelfde melden",
            "je deelt het meteen door voor je het vergeet",
            "je gelooft het omdat het al vaak gedeeld is",
            "je gelooft het omdat er een foto bij het bericht staat",
        ],
        antwoord=0,
        uitleg="Een foto bewijst niets: beelden worden bewerkt, en een computer kan er volledig nieuwe maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een beeld vandaag geen bewijs meer op zichzelf?",
        opties=[
            "beelden kunnen bewerkt of volledig gemaakt worden",
            "beelden worden nooit in kranten gebruikt",
            "beelden zijn altijd ouder dan hun gebeurtenis",
            "beelden kunnen niet opgeslagen worden",
        ],
        antwoord=0,
        uitleg="Ook vroeger werden foto's geretoucheerd en in scène gezet. De techniek maakt het nu wel veel eenvoudiger.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel dat iemand de wereld bekijkt van de plaats waar hij zelf staat?",
        antwoord=["standplaatsgebondenheid", "de standplaatsgebondenheid"],
        uitleg="Het betekent niet dat iemand liegt. Het betekent dat elke blik ergens vandaan komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bron met een duidelijk belang bij haar verhaal lees je kritischer.",
        antwoord=True,
        uitleg="Dat belang maakt haar niet waardeloos, maar je weet waar je op moet letten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een feit en een mening staan nooit in dezelfde zin.",
        antwoord=False,
        uitleg="Ze zitten juist vaak door elkaar. Daarom moet je ze bewust leren scheiden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een historicus heeft zelf ook een standplaats die zijn werk beïnvloedt.",
        antwoord=True,
        uitleg="Daarom legt hij zijn werkwijze en zijn bronnen open, zodat anderen het kunnen nagaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een website is betrouwbaar als ze bovenaan de zoekresultaten staat.",
        antwoord=False,
        uitleg="Die plaats zegt iets over techniek en geld, niet over juistheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een getuigenis van lang na de feiten is waardevol om de beleving te leren kennen.",
        antwoord=True,
        uitleg="Voor data, aantallen en de precieze toedracht neem je documenten van die tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een memoires van een generaal over zijn eigen veldslag. Waar let je op?",
        opties=[
            "hij heeft belang bij zijn eigen rol",
            "hij was er niet bij en kan er dus niets over zeggen",
            "memoires zijn nooit bruikbaar voor een historicus",
            "memoires zijn altijd betrouwbaarder dan documenten",
        ],
        antwoord=0,
        uitleg="Zulke teksten worden geschreven met het oog op het nageslacht. Dat maakt ze boeiend én gekleurd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een affiche, een dagboek en een studie over dezelfde staking. Hoe gebruik je ze?",
        opties=[
            "je legt ze naast elkaar en vergelijkt ze",
            "je kiest er één uit en laat de andere weg",
            "je gebruikt alleen de studie van de historicus",
            "je gebruikt alleen de bronnen van die tijd zelf",
        ],
        antwoord=0,
        uitleg="Elk van de drie zegt iets anders: de bedoeling, de beleving en het overzicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het beoordelen van bronnen niet alleen voor de les geschiedenis nuttig?",
        opties=[
            "dezelfde vragen helpen je bij nieuws en bij sociale media",
            "het helpt je enkel bij een examen over de negentiende eeuw",
            "het is enkel nuttig voor wie historicus wil worden",
            "het heeft met het nieuws van vandaag niets te maken",
        ],
        antwoord=0,
        uitleg="Wie is de bron, wat is het doel en wie bevestigt het: die vragen gelden elke dag.",
    ),
]
