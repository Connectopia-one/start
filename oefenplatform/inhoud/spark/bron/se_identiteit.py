# -*- coding: utf-8 -*-
"""De vragen voor "Ik ben wie ik ben" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik ben wie ik ben" (7,5 % van
het examen): het relationele, gelaagde en dynamische karakter van identiteit.

Deel 1 gaat over wat identiteit is, de twee soorten, de drie lagen van je
persoonlijke identiteit, de ID-cirkel en het verschil met je imago.
Deel 2 gaat over groepsidentiteit, subculturen, en hoe discriminatie,
solidariteit, verbondenheid en wij-zij-denken je identiteit beïnvloeden.

De fiche zegt uitdrukkelijk dat het examen neutraal blijft en geen persoonlijke
gegevens gebruikt. Deze vragen doen hetzelfde: ze beschrijven hoe het werkt,
ze beoordelen niemand.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met iemands identiteit?",
        opties=[
            "Het geheel van wat iemand tot die persoon maakt",
            "Het nummer dat op iemands identiteitskaart staat",
            "Het beroep dat iemand later wil doen",
            "De school waar iemand elke dag naartoe gaat",
        ],
        antwoord=0,
        uitleg="Je identiteit is alles samen wat jou tot jou maakt: je lichaam, je karakter, je afkomst, de groepen waar je bij hoort. Je identiteitskaart is maar een document.",
    ),
    dict(
        type="waarofniet",
        vraag="Je identiteit ligt bij je geboorte vast en verandert daarna niet meer.",
        antwoord=False,
        uitleg="Identiteit is dynamisch: ze verandert je hele leven lang. Wat jij belangrijk vindt op je twaalfde is niet hetzelfde als op je veertigste.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vakfiche onderscheidt twee soorten identiteit. Welke twee?",
        opties=[
            "Persoonlijke identiteit en groepsidentiteit",
            "Echte identiteit en valse identiteit",
            "Jonge identiteit en oude identiteit",
            "Openbare identiteit en geheime identiteit",
        ],
        antwoord=0,
        uitleg="Er is je persoonlijke identiteit, die over jou als individu gaat, en je groepsidentiteit, die over de groepen gaat waar je bij hoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze situaties gaan over iemands identiteit?",
        opties=[
            "Iemand vertelt uit welk land zijn grootouders komen",
            "Iemand legt uit waarom muziek zo belangrijk voor hem is",
            "Iemand zegt dat het buiten hard aan het regenen is",
            "Iemand vertelt bij welke jeugdbeweging hij zit",
        ],
        antwoord=[0, 1, 3],
        uitleg="Afkomst, wat je belangrijk vindt en de groepen waar je bij hoort, zeggen iets over wie iemand is. Het weer zegt daar niets over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat de laag 'biologische aspecten' van je persoonlijke identiteit?",
        opties=[
            "Uit je leeftijd, je lichaam en je geslacht",
            "Uit de punten die je op school haalt voor taal",
            "Uit de vrienden die je zelf gekozen hebt",
            "Uit de hobby's die je het liefste doet",
        ],
        antwoord=0,
        uitleg="De biologische laag gaat over je lichaam: leeftijd, geslacht, lengte, hoe je eruitziet, of je een beperking hebt. Dat kies je niet zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand omschrijft zichzelf als geduldig, nieuwsgierig en een beetje verlegen. Over welke laag gaat dat?",
        opties=[
            "Over zijn persoonlijke eigenschappen",
            "Over zijn biologische aspecten",
            "Over zijn familiale achtergrond",
            "Over zijn subcultuur",
        ],
        antwoord=0,
        uitleg="Geduldig, nieuwsgierig en verlegen zijn karaktertrekken. Die horen bij de laag van de persoonlijke eigenschappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke dingen horen bij de laag 'familiale achtergrond'?",
        opties=[
            "Of je broers of zussen hebt",
            "Het beroep dat je ouders doen",
            "De taal die er bij jou thuis gesproken wordt",
            "De kleur van je fiets en van je jas",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je familiale achtergrond is het gezin waarin je opgroeit: wie erbij hoort, wat ze doen, hoe er thuis gepraat wordt. Je fiets hoort daar niet bij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de tekening waarin je de elementen van je persoonlijke identiteit rond jezelf zet? Het is een ...",
        antwoord=["ID-cirkel", "identiteitscirkel"],
        uitleg="In een ID-cirkel zet je jezelf in het midden en er rond de elementen die samen jouw identiteit vormen.",
    ),
    dict(
        type="waarofniet",
        vraag="In een ID-cirkel staat één element in het midden: de persoon zelf.",
        antwoord=True,
        uitleg="Klopt. Jij staat in het midden, en rondom jou komen de elementen die samen jouw identiteit vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen je persoonlijke identiteit en je imago?",
        opties=[
            "Je identiteit is wie je écht bent, je imago is het beeld dat anderen van je hebben",
            "Je identiteit is het beeld dat anderen van je hebben, je imago is wie je écht bent",
            "Er is geen verschil, het zijn twee woorden voor hetzelfde",
            "Je identiteit heb je online, je imago heb je in het echte leven",
        ],
        antwoord=0,
        uitleg="Je imago is hoe anderen jou zien. Dat kan flink verschillen van wie je van binnen bent, zeker als je je anders voordoet dan je bent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand doet op sociale media alsof hij elk weekend op reis gaat, terwijl dat niet zo is. Wat is er aan de hand?",
        opties=[
            "Hij bouwt een imago op dat niet klopt met zijn identiteit",
            "Hij verandert de biologische laag van zijn identiteit",
            "Hij hoort voortaan bij een andere groepsidentiteit",
            "Hij heeft helemaal geen persoonlijke identiteit meer",
        ],
        antwoord=0,
        uitleg="Wat hij toont is zijn imago: het beeld dat anderen krijgen. Dat staat hier los van wie hij werkelijk is en wat hij werkelijk doet.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee mensen kunnen precies dezelfde persoonlijke identiteit hebben.",
        antwoord=False,
        uitleg="Nee. Zelfs een tweeling deelt niet alles: karakter, ervaringen en keuzes verschillen altijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemen we identiteit 'gelaagd'?",
        opties=[
            "Omdat ze uit verschillende lagen bestaat die samen bepalen wie je bent",
            "Omdat je ze laag per laag kan afleggen tot er niets van jou overblijft",
            "Omdat iedereen er precies drie lagen van heeft",
            "Omdat de onderste laag de belangrijkste is voor iedereen",
        ],
        antwoord=0,
        uitleg="Gelaagd wil zeggen dat je identiteit uit meerdere delen bestaat, zoals je lichaam, je karakter en je achtergrond. Ze werken samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand is een goede zwemmer, houdt van tekenen en woont bij zijn oma. Hoeveel lagen van zijn persoonlijke identiteit komen hier aan bod?",
        opties=["Drie", "Eén", "Twee", "Geen enkele"],
        antwoord=0,
        uitleg="Zwemmen en tekenen zeggen iets over zijn eigenschappen, en bij zijn oma wonen over zijn familiale achtergrond. Zijn lichaam speelt mee bij het zwemmen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan zelf kiezen tot welke laag van je identiteit je leeftijd hoort.",
        antwoord=False,
        uitleg="Je leeftijd hoort altijd bij de biologische laag, en je kiest hem ook niet zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over identiteit klopt?",
        opties=[
            "Je identiteit ontstaat mee in contact met anderen",
            "Je identiteit ontstaat volledig in je eentje",
            "Je identiteit wordt alleen door je ouders bepaald",
            "Je identiteit wordt alleen door je vrienden bepaald",
        ],
        antwoord=0,
        uitleg="Identiteit is relationeel: je ontdekt wie je bent in contact met anderen. Dat is meer dan alleen je ouders of alleen je vrienden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verhuist naar een ander land en begint zich na een paar jaar anders te voelen over wie hij is. Wat zie je hier?",
        opties=[
            "Dat identiteit dynamisch is en dus kan veranderen",
            "Dat identiteit alleen uit biologische aspecten bestaat",
            "Dat identiteit niets met je omgeving te maken heeft",
            "Dat hij zijn oude identiteit is kwijtgeraakt",
        ],
        antwoord=0,
        uitleg="Identiteit verandert mee met wat je meemaakt. Verhuizen naar een ander land is zo'n ervaring. Je oude identiteit verdwijnt daarmee niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we het beeld dat anderen van jou hebben? Je ...",
        antwoord="imago",
        uitleg="Je imago is het beeld dat anderen van je hebben. Dat kan kloppen met wie je bent, maar hoeft niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze uitspraken gaan NIET over identiteit?",
        opties=[
            "De bus komt vandaag tien minuten te laat",
            "De winkel op de hoek sluit om zes uur",
            "Ik voel me het meest mezelf als ik gitaar speel",
        ],
        antwoord=[0, 1],
        uitleg="De eerste twee zijn gewoon feiten over de wereld. Alleen de laatste zegt iets over wie iemand is.",
    ),
    dict(
        type="waarofniet",
        vraag="Je persoonlijke eigenschappen zijn een laag van je persoonlijke identiteit.",
        antwoord=True,
        uitleg="Klopt. De drie lagen zijn biologische aspecten, persoonlijke eigenschappen en familiale achtergrond.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar gaat groepsidentiteit over?",
        opties=[
            "Over de groepen waar je deel van uitmaakt",
            "Over je karakter en je gewoontes",
            "Over je lengte en je leeftijd",
            "Over het beeld dat anderen van je hebben",
        ],
        antwoord=0,
        uitleg="Groepsidentiteit gaat over het samen: je streek of land, de groepen waar je bij hoort, en de subculturen waarin je je thuis voelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen horen bij groepsidentiteit?",
        opties=[
            "De regio, het land of het gebied waar je vandaan komt",
            "De groepen waar je deel van uitmaakt",
            "De subculturen waar je bij hoort",
            "De kleur van je ogen en van je haar",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie staan zo in de vakfiche. De kleur van je ogen is biologisch en hoort bij je persoonlijke identiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: ik ben opgegroeid in Limburg en dat hoor je nog aan mijn accent. Over welke laag van groepsidentiteit gaat dat?",
        opties=[
            "Over de regio waar hij vandaan komt",
            "Over zijn subcultuur",
            "Over zijn sociale klasse",
            "Over zijn geloof of overtuiging",
        ],
        antwoord=0,
        uitleg="Waar je vandaan komt, is een laag van je groepsidentiteit. Een accent is daar een hoorbaar spoor van.",
    ),
    dict(
        type="waarofniet",
        vraag="Je gender, je sociale klasse en je geloof of overtuiging horen bij de groepen waar je deel van uitmaakt.",
        antwoord=True,
        uitleg="Klopt. Die drie noemt de vakfiche als voorbeelden van groepen waar je deel van uitmaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een subcultuur?",
        opties=[
            "Een kleinere groep binnen de samenleving met een eigen stijl",
            "Een cultuur die minder waard wordt gevonden dan een andere",
            "Een cultuur die ondergronds verboden is",
            "Een cultuur die maar één dag per jaar bestaat",
        ],
        antwoord=0,
        uitleg="Een subcultuur is een groep binnen de samenleving met een eigen stijl, eigen muziek of eigen gewoontes. Denk aan skaters of gamers.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan maar bij één groep tegelijk horen.",
        antwoord=False,
        uitleg="Iedereen hoort bij meerdere groepen tegelijk: je gezin, je klas, je sportclub, je streek. Die sluiten elkaar niet uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beïnvloeden persoonlijke identiteit en groepsidentiteit elkaar?",
        opties=[
            "In twee richtingen: de groep kleurt jou en jij de groep",
            "Alleen in één richting: de groep bepaalt jou volledig",
            "Alleen in één richting: jij bepaalt de groep volledig",
            "Ze hebben niets met elkaar te maken",
        ],
        antwoord=0,
        uitleg="Je neemt gewoontes van je groepen over, en tegelijk breng jij iets van jezelf in die groepen binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is discriminatie?",
        opties=[
            "Mensen anders en slechter behandelen om wie ze zijn",
            "Mensen met elkaar vergelijken op een eerlijke manier",
            "Iedereen precies dezelfde regels geven",
            "Mensen in groepen indelen om ze te tellen",
        ],
        antwoord=0,
        uitleg="Discriminatie is iemand slechter behandelen om een kenmerk zoals afkomst, geloof, gender of een beperking. Vergelijken op zich is dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is solidariteit?",
        opties=[
            "Elkaar steunen, ook als je er zelf niets bij wint",
            "Alleen helpen wie jou eerder al geholpen heeft",
            "Ervoor zorgen dat iedereen hetzelfde denkt",
            "Zorgen dat je zelf vooruitkomt",
        ],
        antwoord=0,
        uitleg="Solidariteit is opkomen voor elkaar zonder daar iets voor terug te vragen. Het is een van de dingen die je identiteit mee vormgeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is wij-zij-denken?",
        opties=[
            "De wereld opdelen in de eigen groep en de anderen",
            "Samen met anderen aan een groepswerk verder werken",
            "Om beurten het woord nemen in een gesprek",
            "Nadenken over wat je zelf voelt",
        ],
        antwoord=0,
        uitleg="Bij wij-zij-denken zet je de eigen groep tegenover de rest. Dat maakt het moeilijker om de anderen nog als individu te zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen kan wij-zij-denken hebben?",
        opties=[
            "Mensen buiten de eigen groep worden sneller uitgesloten",
            "Vooroordelen over de andere groep worden sterker",
            "De eigen groep voelt zich hechter",
            "Iedereen krijgt automatisch dezelfde kansen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wij-zij-denken maakt de eigen groep vaak hechter, maar duwt de anderen naar buiten en versterkt vooroordelen. Gelijke kansen komen er niet van.",
    ),
    dict(
        type="waarofniet",
        vraag="Verbondenheid betekent dat je het gevoel hebt ergens bij te horen.",
        antwoord=True,
        uitleg="Klopt. Verbondenheid is dat gevoel erbij te horen, bij een gezin, een groep vrienden, een club of een streek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klas zamelt geld in voor een medeleerling van wie het huis is afgebrand. Wat zie je hier?",
        opties=[
            "Solidariteit",
            "Discriminatie",
            "Wij-zij-denken",
            "Machtsmisbruik",
        ],
        antwoord=0,
        uitleg="Ze steunen iemand zonder er zelf iets bij te winnen. Dat is solidariteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wordt nooit gevraagd voor een groepswerk omdat hij een andere achtergrond heeft. Wat zie je hier?",
        opties=[
            "Discriminatie",
            "Solidariteit",
            "Verbondenheid",
            "Een gewoon meningsverschil",
        ],
        antwoord=0,
        uitleg="Hij wordt slechter behandeld om zijn achtergrond, niet om iets wat hij deed. Dat is discriminatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Discriminatie kan iemands beeld van zichzelf veranderen.",
        antwoord=True,
        uitleg="Klopt. Wie vaak buitengesloten wordt, gaat zichzelf anders bekijken. Zo werkt discriminatie in op iemands identiteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Subculturen bestaan alleen bij jongeren.",
        antwoord=False,
        uitleg="Ook volwassenen horen bij subculturen: motorrijders, verzamelaars, koorzangers. Leeftijd speelt daar geen rol in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand voelt zich thuis in twee culturen tegelijk. Hoe kan dat?",
        opties=[
            "Groepsidentiteit is gelaagd, dus je kan bij meerdere groepen horen",
            "Dat kan niet, je moet er altijd één kiezen",
            "Dat kan alleen als je in twee landen tegelijk woont",
            "Dat betekent dat hij helemaal geen persoonlijke identiteit heeft",
        ],
        antwoord=0,
        uitleg="Net zoals je bij meerdere groepen kan horen, kan je je in meerdere culturen thuis voelen. Kiezen hoeft niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we het opdelen van de wereld in de eigen groep en de anderen? Het is ...",
        antwoord=["wij-zij-denken", "wij zij denken"],
        uitleg="Wij-zij-denken zet de eigen groep tegenover de rest, en maakt het moeilijk om anderen nog als individu te zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zegt men dat identiteit relationeel is?",
        opties=[
            "Omdat ze vorm krijgt in je contacten met anderen",
            "Omdat ze alleen over je familieleden gaat",
            "Omdat ze pas telt als je een relatie hebt",
            "Omdat ze door de overheid wordt vastgelegd bij je geboorte",
        ],
        antwoord=0,
        uitleg="Relationeel wil zeggen: in verhouding tot anderen. Je ontdekt wie je bent door met anderen om te gaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Je groepsidentiteit heeft geen enkele invloed op je persoonlijke identiteit.",
        antwoord=False,
        uitleg="Ze beïnvloeden elkaar juist. De groepen waar je bij hoort, kleuren mee wie je bent en wat je belangrijk vindt.",
    ),
]
