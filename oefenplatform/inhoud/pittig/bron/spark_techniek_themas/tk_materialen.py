# -*- coding: utf-8 -*-
"""Pittige vragen bij "Materialen en grondstoffen" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en 2, maar met twee proeven die je samen moet
lezen, de onderdompelingsmethode als rekenstap, en eigenschappen die je eerst
moet herkennen en dan in hun groep moet zetten.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="Je test een grijs staafje. In een stroomkring laat het een lampje branden, maar een magneet trekt het niet aan. Wat weet je nu over het staafje?",
        opties=[
            "Het is een non-ferrometaal",
            "Het is een ferrometaal dat niet kan roesten",
            "Het is een niet-metaal dat toch stroom geleidt",
            "Het is een niet-metaal, want de magneet trekt niet",
        ],
        antwoord=0,
        uitleg="Het lampje brandt, dus de geleidingsproef zegt: metaal. De magneet trekt niet, dus de magneetproef zegt: geen ijzer erin, non-ferro. Dat de magneet niet trekt, betekent niet dat het geen metaal is: aluminium en koper worden ook niet aangetrokken.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een magneet een voorwerp niet aantrekt, weet je zeker dat het voorwerp van een niet-metaal gemaakt is.",
        antwoord=False,
        uitleg="De magneetproef zegt alleen of een metaal ijzer bevat. Een aluminium of koperen voorwerp wordt ook niet aangetrokken en is toch een metaal. Om metaal of niet-metaal te kennen, heb je de geleidingsproef nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lepel geleidt de stroom, maar een magneet trekt hem niet aan. Van welke materialen kan die lepel gemaakt zijn? (meerdere antwoorden mogelijk)",
        opties=["Aluminium", "Koper", "Glas", "Hout", "Staal"],
        antwoord=[0, 1],
        uitleg="De lepel geleidt, dus het is een metaal, en de magneet trekt niet, dus het is een non-ferrometaal: aluminium of koper. Staal is een ferrometaal en zou aangetrokken worden. Hout en glas zijn niet-metalen en geleiden de stroom niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rij loopt in de juiste volgorde van grondstof naar materiaal naar product?",
        opties=[
            "IJzererts, staal, spijker",
            "Staal, ijzererts, spijker",
            "IJzererts, spijker, staal",
            "Glas, zand, drinkglas op tafel",
        ],
        antwoord=0,
        uitleg="IJzererts komt uit de grond en is de grondstof. Daar maak je staal van, het materiaal, en van staal maak je een spijker, het product. Staal staat dus nooit vooraan, en bij glas en zand is zand de grondstof en niet glas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling maakt een lijstje met alleen grondstoffen. Welke woorden staan daar terecht op? (meerdere antwoorden mogelijk)",
        opties=["Wol", "Aardolie", "Zand", "Staal", "Baksteen"],
        antwoord=[0, 1, 2],
        uitleg="Wol, aardolie en zand haal je zo uit de natuur, dus het zijn grondstoffen. Staal is al een materiaal dat uit ijzererts gemaakt is, en baksteen is een materiaal dat uit klei gebakken is. Die twee horen dus niet op het lijstje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor een gootsteen kiest men inox en geen gewoon staal. Waarom?",
        opties=[
            "Gewoon staal is een ferrometaal en dat kan roesten",
            "Gewoon staal geleidt de elektrische stroom helemaal niet",
            "Inox is een grondstof en daarom een stuk goedkoper",
            "Inox is een enkelvoudig metaal en dus veel zuiverder",
        ],
        antwoord=0,
        uitleg="Staal bevat ijzer, en ferrometalen kunnen roesten. Inox is roestvrij staal, en dat wil je bij een gootsteen die altijd nat wordt. Inox is geen grondstof en geen enkelvoudig metaal: het is een legering.",
    ),
    dict(
        type="waarofniet",
        vraag="Zet je een stof in een stroomkring en blijft het lampje uit, dan is die stof geen metaal.",
        antwoord=True,
        uitleg="Metalen geleiden de stroom, dus met een metaal in de kring zou het lampje branden. Blijft het uit, dan heb je een niet-metaal, zoals hout, glas of kunststof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een glazen plaatje breekt bij een kleine tik. Een stalen plaatje van dezelfde grootte deukt, maar blijft heel. Welke eigenschap verschilt hier, en bij welke groep hoort ze?",
        opties=[
            "De broosheid, een mechanische eigenschap",
            "De broosheid, een fysische eigenschap",
            "De hardheid, een technologische eigenschap",
            "Het smeltpunt, een mechanische eigenschap",
        ],
        antwoord=0,
        uitleg="Glas breekt makkelijk, dus glas is broos, en het staal verdraagt veel voor het breekt. Broosheid gaat over hoe een materiaal zich houdt onder een kracht, en dat is mechanisch. Het smeltpunt is fysisch en heeft met deze tik niets te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie van deze eigenschappen horen in dezelfde groep. Welke hoort er niet bij?",
        opties=[
            "Warmtegeleiding",
            "Hardheid",
            "Treksterkte",
            "Taaiheid",
        ],
        antwoord=0,
        uitleg="Hardheid, treksterkte en taaiheid zijn mechanische eigenschappen: ze hebben met kracht te maken. Warmtegeleiding is een fysische eigenschap, samen met het smeltpunt en de massadichtheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil de massadichtheid van een steen kennen. Wat moet je daarvoor allemaal meten?",
        opties=[
            "De massa, en het volume met de onderdompelingsmethode",
            "Alleen de massa, want die vind je met een gewone weegschaal",
            "Het volume, en daarna of een magneet de steen kan aantrekken",
            "De hardheid, en daarna hoe ver je de steen kan uitrekken",
        ],
        antwoord=0,
        uitleg="Massadichtheid is de massa gedeeld door het volume, dus je hebt die twee nodig. Het volume vind je door de steen onder te dompelen en te kijken hoeveel water hij verplaatst. Alleen de massa is niet genoeg: een grote lichte steen en een kleine zware steen kunnen even veel wegen.",
    ),
    dict(
        type="invultekst",
        vraag="Een leerling onderzoekt van een materiaal de hardheid, de treksterkte, het smeltpunt en de watervastheid. Hoeveel van die vier eigenschappen zijn mechanische eigenschappen? Antwoord met een getal.",
        antwoord="2",
        reken="1 + 1",
        uitleg="Hardheid en treksterkte zijn mechanisch. Het smeltpunt is een fysische eigenschap en de watervastheid een technologische. Wie alles wat je met een proef onderzoekt mechanisch noemt, komt op vier uit, en dat klopt niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten of soldeertin al smelt bij de temperatuur van je soldeerbout. Naar welke eigenschap kijk je, en bij welke groep hoort ze?",
        opties=[
            "Het smeltpunt, een fysische eigenschap",
            "Het smeltpunt, een mechanische eigenschap",
            "De hardheid, een mechanische eigenschap",
            "De verwerkingstijd, een technologische eigenschap",
        ],
        antwoord=0,
        uitleg="Of iets smelt bij een bepaalde temperatuur, lees je af aan het smeltpunt. Het smeltpunt is een fysische eigenschap, net als de warmtegeleiding en de massadichtheid, en geen mechanische: het heeft niets met kracht te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vork van aluminium en een vork van hout kan je uit elkaar houden met de geleidingsproef, maar niet met de magneetproef.",
        antwoord=True,
        uitleg="Aluminium geleidt de stroom en hout niet, dus bij de geleidingsproef zie je een verschil. Een magneet trekt geen van beide aan: aluminium is non-ferro en hout is geen metaal. Bij de magneetproef zie je dus geen verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kiest een materiaal voor een tuinbank die het hele jaar buiten in de regen staat. Naar welke groep eigenschappen kijk je vooral?",
        opties=[
            "Naar de technologische eigenschappen",
            "Naar de fysische eigenschappen",
            "Naar de magnetische eigenschappen",
            "Naar de elektrische eigenschappen",
        ],
        antwoord=0,
        uitleg="Tegen regen kunnen heet watervastheid, en dat is een technologische eigenschap. Of een magneet de bank aantrekt of of ze stroom geleidt, maakt voor een tuinbank niets uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Elasticiteit onderzoek je door een materiaal uit te rekken, en daarom is elasticiteit een technologische eigenschap.",
        antwoord=False,
        uitleg="De proef klopt: je rekt het materiaal uit en kijkt of het terugveert. Maar elasticiteit is een mechanische eigenschap, net als hardheid en treksterkte. Technologisch zijn vervormbaarheid, watervastheid, bewerkbaarheid en de verwerkingstijd van een lijm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze materialen komen niet kant-en-klaar in de natuur voor, maar worden door de mens gemaakt? (meerdere antwoorden mogelijk)",
        opties=["Kunststof", "Composiet", "Brons", "Soldeertin", "Leder"],
        antwoord=[0, 1, 2, 3],
        uitleg="Kunststof en composiet zijn kunstmatige materialen. Brons en soldeertin zijn legeringen, en die worden gemaakt door metalen samen te smelten. Leder komt van de huid van een dier en is een natuurlijk materiaal.",
    ),
    dict(
        type="invultekst",
        vraag="Een staafje laat een lampje in een stroomkring branden en wordt door een magneet aangetrokken. Het staafje is dus van een ___ gemaakt. Antwoord met één woord.",
        antwoord="ferrometaal",
        uitleg="Het lampje brandt, dus het is een metaal. De magneet trekt het aan, dus er zit ijzer in. Een metaal met ijzer erin is een ferrometaal.",
    ),
    dict(
        type="invultekst",
        vraag="Een stof in het lokaal vat zelf niet zomaar vlam, maar kan een brand veroorzaken of een vuurtje in de buurt erger maken. Welk woord staat bij het gevaarpictogram op de fles? Antwoord met één woord.",
        antwoord="oxiderend",
        uitleg="Een oxiderende stof kan brand veroorzaken of erger maken. Ontvlambaar is iets anders: dan vat de stof zelf vlam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ontstopper voor de gootsteen kan je huid en je ogen aantasten. Welk gevaarpictogram verwacht je op de fles?",
        opties=[
            "Bijtend of corrosief",
            "Oxiderend, want de stof kan brand erger maken",
            "Gassen onder druk, want de fles kan openbarsten",
            "Ontvlambaar, want de stof kan vlam vatten",
        ],
        antwoord=0,
        uitleg="Een stof die brandwonden aan je huid of je ogen geeft, draagt het pictogram voor bijtend of corrosief. De andere pictogrammen waarschuwen voor vuur of voor een fles die kan openbarsten, en daar gaat het hier niet over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de geleidingsproef en de magneetproef kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Brandt het lampje, dan is de stof een metaal",
            "Trekt de magneet aan, dan bevat het metaal ijzer",
            "Brandt het lampje, dan is de stof een ferrometaal",
            "Trekt de magneet niet aan, dan is de stof geen metaal",
        ],
        antwoord=[0, 1],
        uitleg="De geleidingsproef beantwoordt de vraag metaal of niet-metaal, de magneetproef de vraag ferro of non-ferro. Een brandend lampje zegt dus niets over ijzer, en een magneet die niet trekt, zegt niets over metaal of niet-metaal: koper wordt ook niet aangetrokken.",
    ),
]
