# -*- coding: utf-8 -*-
"""Ongelijkheden: klassenmaatschappij en sociale strijd.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: de overgang van
een standenmaatschappij naar een klassenmaatschappij, de levensomstandigheden
van de arbeiders, en de strijd die daarop volgde, met de vakbonden, de stakingen
en de eerste sociale wetten.

Hierna volgen de ideologieën die uit die strijd ontstaan zijn.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een standenmaatschappij en een klassenmaatschappij?",
        opties=[
            "in een standenmaatschappij ligt je plaats bij je geboorte vast",
            "in een standenmaatschappij hangt je plaats af van je bezit",
            "in een klassenmaatschappij bestaan er helemaal geen verschillen",
            "in een klassenmaatschappij beslist de vorst wat je beroep is",
        ],
        antwoord=0,
        uitleg="In een klassenmaatschappij bepaalt je plaats in de productie waar je staat: bezit je een fabriek of je arbeid?",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klassen onderscheidt men in de negentiende-eeuwse samenleving?",
        opties=[
            "de grote burgerij van fabrikanten, bankiers en handelaars",
            "de arbeidersklasse van wie van zijn loon moet leven",
            "de stand van de adel met voorrechten bij de wet",
            "de stand van de geestelijkheid met eigen rechtbanken",
        ],
        antwoord=[0, 1],
        uitleg="Standen met eigen voorrechten en rechtbanken waren afgeschaft. Wat bleef, was het verschil in bezit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de klasse van wie geen bezit heeft en van zijn loon moet leven?",
        antwoord=["de arbeidersklasse", "arbeidersklasse", "het proletariaat"],
        uitleg="Marx gebruikte het woord proletariaat. Zijn bezit was zijn arbeidskracht, en niets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie behoorde tot de kleine burgerij?",
        opties=[
            "winkeliers, ambachtslui en lagere bedienden",
            "bankiers, fabrikanten en grote handelaars",
            "mijnwerkers, spinners en dagloners",
            "graven, baronnen en hun grondbezitters",
        ],
        antwoord=0,
        uitleg="Zij hadden wat bezit en soms wat personeel, maar zaten ver van de rijkdom van de grote burgerij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de sociale kwestie van de negentiende eeuw?",
        opties=[
            "de vraag wat er met de armoede van de arbeiders moest gebeuren",
            "de vraag welke taal het bestuur van het land moest gebruiken",
            "de vraag of de kerk of de staat de scholen mocht inrichten",
            "de vraag welke mogendheid de kolonies mocht besturen",
        ],
        antwoord=0,
        uitleg="Dat de rijkdom groeide terwijl de armoede bleef, werd een vraag die de politiek niet kon ontwijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe was een arbeidersgezin rond 1880 beschermd tegen ziekte of een ongeval?",
        opties=[
            "er was geen enkele wettelijke bescherming voorzien",
            "de staat betaalde een uitkering voor elke zieke arbeider",
            "de fabriek moest het loon tijdens de ziekte doorbetalen",
            "een verplichte verzekering dekte elk ongeval in de fabriek",
        ],
        antwoord=0,
        uitleg="Wie niet kon werken, kreeg niets. Een ongeval kon een gezin in één dag tot de bedelstaf brengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkten kinderen en vrouwen in de fabrieken en de mijnen?",
        opties=[
            "hun loon was lager en het gezin had dat geld nodig",
            "zij hadden daarvoor een opleiding gekregen in de school",
            "de wet verplichtte elk gezinslid om te gaan werken",
            "zij werden door de vakbonden naar de fabriek gestuurd",
        ],
        antwoord=0,
        uitleg="Het loon van een man alleen volstond niet. Een kind kostte de fabrikant maar een fractie daarvan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is uitbetaling in natura, waar arbeiders zich tegen verzetten?",
        opties=[
            "het loon werd in bonnen voor de winkel van de fabriek betaald",
            "het loon werd elke week in gouden en zilveren munten betaald",
            "het loon werd op de rekening van de arbeider overgeschreven",
            "het loon werd pas aan het einde van het jaar uitbetaald",
        ],
        antwoord=0,
        uitleg="In die winkel lagen de prijzen hoger. Een wet van 1887 verplichtte uitbetaling in geld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de arbeidersbuurten van de negentiende eeuw kloppen?",
        opties=[
            "veel gezinnen deelden één waterpomp en één toilet",
            "besmettelijke ziekten als tyfus en cholera grepen er om zich heen",
            "elke woning had een eigen tuin en een eigen waterleiding",
            "de steden bouwden er van het begin af aan riolen bij",
        ],
        antwoord=[0, 1],
        uitleg="De steden groeiden veel sneller dan hun riolen en hun waterleiding. Daar werd pas later aan gewerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het coalitieverbod?",
        opties=[
            "arbeiders mochten zich niet verenigen om loon te eisen",
            "partijen mochten geen regering met elkaar vormen",
            "fabrikanten mochten geen prijsafspraken met elkaar maken",
            "staten mochten geen militaire verdragen met elkaar sluiten",
        ],
        antwoord=0,
        uitleg="Wie het toch deed, kon vervolgd worden. In België werd dat verbod in 1866 opgeheven.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar werd het coalitieverbod in België opgeheven?",
        antwoord=["1866"],
        uitleg="Daarna konden arbeiders zich wettig verenigen. Staken bleef nog lang strafbaar in de praktijk.",
    ),
    dict(
        type="waarofniet",
        vraag="In een klassenmaatschappij bepaalt je geboorte voorgoed je plaats in de samenleving.",
        antwoord=False,
        uitleg="Dat was de standenmaatschappij. In een klassenmaatschappij telt in beginsel je bezit en je positie.",
    ),
    dict(
        type="waarofniet",
        vraag="De grote burgerij had in de negentiende eeuw zowel het geld als de politieke macht.",
        antwoord=True,
        uitleg="Door het cijnskiesrecht mochten juist zij kiezen. Zo bepaalden zij ook de wetten over hun fabrieken.",
    ),
    dict(
        type="waarofniet",
        vraag="Arbeiders mochten in België van 1830 tot 1866 wettig een vakbond oprichten.",
        antwoord=False,
        uitleg="Het coalitieverbod stond dat in de weg. Vereniging om loon te eisen was strafbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook in de landbouw en in de huisnijverheid was de armoede in de negentiende eeuw groot.",
        antwoord=True,
        uitleg="De crisis in de Vlaamse vlasnijverheid rond 1845 bracht honger en tyfus op het platteland.",
    ),
    dict(
        type="waarofniet",
        vraag="De eerste sociale wetten in België kwamen er al kort na de onafhankelijkheid.",
        antwoord=False,
        uitleg="Ze kwamen er pas na 1886, meer dan een halve eeuw later, en na veel onrust.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was een weerstandskas of een mutualiteit?",
        opties=[
            "een kas waar arbeiders samen geld in legden voor slechte dagen",
            "een kas waar de staat elke werkloze een uitkering uit betaalde",
            "een kas waar de fabrikanten hun winsten in bewaarden",
            "een kas waar de kerk de giften voor de armen in bewaarde",
        ],
        antwoord=0,
        uitleg="Uit die kassen groeiden later de ziekenfondsen en de stakingskassen van de vakbonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in een verslag van 1843 over kinderen van negen jaar die twaalf uur in een spinnerij werken. Wat besluit je?",
        opties=[
            "kinderarbeid was toen gewoon en wettelijk toegelaten",
            "kinderarbeid was toen verboden en werd dus bestraft",
            "het verslag moet een vergissing of een verzinsel zijn",
            "kinderarbeid bestond enkel in Engeland, niet bij ons",
        ],
        antwoord=0,
        uitleg="Zulke verslagen waren juist het bewijsmateriaal waarmee men later een verbod verdedigde.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk maatschappelijk domein situeer je het coalitieverbod?",
        opties=[
            "in het politieke domein, met gevolgen in het sociale",
            "uitsluitend in het economische domein van de handel",
            "uitsluitend in het culturele domein van de opvoeding",
            "in geen enkel maatschappelijk domein van die tijd",
        ],
        antwoord=0,
        uitleg="Het stond in de strafwet, dus politiek, en het raakte de verhouding tussen baas en arbeider.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de klassenmaatschappij kloppen?",
        opties=[
            "je plaats hangt af van je bezit en je positie in de productie",
            "de verschillen tussen arm en rijk bleven erg groot",
            "voorrechten bij de wet gelden nog volgens je geboorte",
            "elke arbeider kon in één generatie fabrikant worden",
        ],
        antwoord=[0, 1],
        uitleg="Voor de wet waren alle burgers gelijk. In de praktijk bleef opklimmen voor zeer weinigen haalbaar.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke middelen gebruikten de arbeiders in hun sociale strijd?",
        opties=[
            "de staking, om het werk stil te leggen",
            "de vakbond, om samen sterker te staan",
            "het cijnskiesrecht, om wetten te laten stemmen",
            "het kartel, om de prijzen te laten stijgen",
        ],
        antwoord=[0, 1],
        uitleg="Het cijnskiesrecht sloot hen juist uit, en kartels waren een middel van de fabrikanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een coöperatie in de arbeidersbeweging?",
        opties=[
            "een winkel of bakkerij die de arbeiders samen bezitten",
            "een kas waaruit de staat de werklozen betaalt",
            "een afspraak tussen fabrieken over hun prijzen",
            "een school die de fabriek voor de kinderen opricht",
        ],
        antwoord=0,
        uitleg="De Gentse coöperatie Vooruit bakte brood voor haar leden. De winst ging naar de beweging zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1886 in de Waalse industriegebieden?",
        opties=[
            "er brak een golf van stakingen en onlusten uit",
            "er werd het algemeen enkelvoudig stemrecht ingevoerd",
            "er werden alle steenkoolmijnen voorgoed gesloten",
            "er kwam een wet die de vakbonden verbood",
        ],
        antwoord=0,
        uitleg="Het leger werd ingezet en er vielen doden. Daarna kwam de sociale kwestie op de politieke agenda.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg had de onrust van 1886 op de wetgeving?",
        opties=[
            "er kwamen de eerste sociale wetten van het land",
            "er kwam een verbod op alle vormen van staking",
            "er kwam het algemeen stemrecht voor alle mannen",
            "er kwam een verbod op de oprichting van partijen",
        ],
        antwoord=0,
        uitleg="Een onderzoekscommissie bracht de toestanden in kaart. Daaruit volgden wetten over loon en kinderarbeid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat regelde de Belgische wet van 1889?",
        opties=[
            "de arbeid van vrouwen en kinderen in de fabrieken",
            "het recht van iedere man van het land om te stemmen",
            "de vergoeding bij elk arbeidsongeval in de fabriek",
            "de duur van de jaarlijkse vakantie met behoud van loon",
        ],
        antwoord=0,
        uitleg="Kinderen onder de twaalf mochten niet meer in een fabriek werken, en de nacht werd voor hen verboden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het samen stilleggen van het werk om eisen af te dwingen?",
        antwoord=["een staking", "staking", "de staking"],
        uitleg="Zonder stakingskas hield een staking niet lang. Daarom legden arbeiders eerst samen geld in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke partij werd in 1885 opgericht om de arbeiders politiek te vertegenwoordigen?",
        opties=[
            "de Belgische Werkliedenpartij",
            "de Liberale Partij van België",
            "de Katholieke Partij van België",
            "de Volksunie van Vlaanderen",
        ],
        antwoord=0,
        uitleg="Zij bundelde vakbonden, ziekenkassen en coöperaties in één beweging met één politiek programma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom was het algemeen stemrecht de kerneis van de arbeidersbeweging?",
        opties=[
            "zonder stemrecht kon zij geen sociale wetten laten stemmen",
            "zonder stemrecht mocht zij geen vakbond meer oprichten",
            "zonder stemrecht mochten arbeiders niet naar school",
            "zonder stemrecht mochten arbeiders geen winkel openen",
        ],
        antwoord=0,
        uitleg="Wie de wetten maakt, bepaalt de werkdag. Daarom was stemrecht geen doel apart, maar een middel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat leverde de algemene staking van 1893 in België op?",
        opties=[
            "het algemeen meervoudig stemrecht voor mannen",
            "het algemeen enkelvoudig stemrecht voor mannen",
            "het stemrecht voor vrouwen bij elke verkiezing",
            "een volledig verbod op elke vorm van staking",
        ],
        antwoord=0,
        uitleg="Elke man kreeg een stem, maar wie bezit, een diploma of een gezin had, kreeg er een of twee bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het algemeen meervoudig stemrecht?",
        opties=[
            "elke man stemt, en sommigen krijgen extra stemmen",
            "elke man en elke vrouw krijgt precies één stem",
            "enkel wie genoeg belasting betaalt, mag stemmen",
            "elke gemeente krijgt één stem bij de verkiezing",
        ],
        antwoord=0,
        uitleg="Zo bleef het gewicht van de burgerij overeind. De beweging bleef dus voor één man één stem ijveren.",
    ),
    dict(
        type="invultekst",
        vraag="In welk jaar mochten de Belgische mannen voor het eerst met één stem per man kiezen?",
        antwoord=["1919"],
        uitleg="Dat was na de Eerste Wereldoorlog. De vrouwen kregen dat recht voor het parlement pas in 1948.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer mochten de Belgische vrouwen voor het eerst voor het parlement stemmen?",
        opties=[
            "in 1948, na de Tweede Wereldoorlog",
            "in 1919, na de Eerste Wereldoorlog",
            "in 1893, na de eerste algemene staking",
            "in 1830, bij het ontstaan van het land",
        ],
        antwoord=0,
        uitleg="Voor de gemeente mochten zij eerder gaan stemmen, al vanaf 1920. Voor het parlement duurde het langer.",
    ),
    dict(
        type="waarofniet",
        vraag="De eerste sociale wetten in België kwamen er onder druk van stakingen en onrust.",
        antwoord=True,
        uitleg="Zonder 1886 was er geen onderzoekscommissie geweest, en zonder die commissie geen wetten.",
    ),
    dict(
        type="waarofniet",
        vraag="De arbeidersbeweging bestond enkel uit vakbonden.",
        antwoord=False,
        uitleg="Ze bestond ook uit ziekenkassen, coöperaties, partijen, en zelfs uit koren en toneelgezelschappen.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook katholieken richtten in de negentiende eeuw arbeidersverenigingen op.",
        antwoord=True,
        uitleg="Zij deden dat naast de socialistische beweging, met eigen vakbonden en eigen ziekenkassen.",
    ),
    dict(
        type="waarofniet",
        vraag="Na de invoering van het algemeen meervoudig stemrecht had elke stem hetzelfde gewicht.",
        antwoord=False,
        uitleg="Sommige mannen hadden twee of drie stemmen. Daarom bleef de eis van één man één stem overeind.",
    ),
    dict(
        type="waarofniet",
        vraag="De sociale zekerheid zoals wij die kennen, bestond in 1900 al volledig.",
        antwoord=False,
        uitleg="Er waren losse wetten en vrije kassen. Het stelsel van nu werd pas in 1944 en daarna opgebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de sociale strijd in België kloppen?",
        opties=[
            "het coalitieverbod werd in 1866 opgeheven",
            "de eerste sociale wetten volgden op de onrust van 1886",
            "het algemeen enkelvoudig stemrecht kwam er al in 1893",
            "de staat voerde al voor 1850 een werkloosheidsuitkering in",
        ],
        antwoord=[0, 1],
        uitleg="In 1893 kwam het meervoudige stemrecht; het enkelvoudige volgde pas in 1919.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een pamflet uit 1890 dat één man één stem en een werkdag van tien uur eist. Van wie komt het?",
        opties=[
            "van de arbeidersbeweging",
            "van de vereniging van fabrikanten",
            "van de regering van het land",
            "van de bisschoppen van België",
        ],
        antwoord=0,
        uitleg="Die twee eisen samen horen bij de beweging die het stemrecht als middel voor sociale wetten zag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de sociale strijd een gevolg van de industriële revolutie?",
        opties=[
            "de fabriek bracht veel arbeiders met dezelfde belangen samen",
            "de fabriek maakte van elke arbeider een kleine ondernemer",
            "de fabriek liet de arbeiders thuis en apart verder werken",
            "de fabriek gaf elke arbeider een stem in het bestuur",
        ],
        antwoord=0,
        uitleg="Wie thuis alleen weeft, staat alleen. Wie met duizend anderen in één zaal staat, kan samen handelen.",
    ),
]
