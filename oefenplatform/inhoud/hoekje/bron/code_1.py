# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Coderen en computers, deel 1: hoe een computer denkt."""

VAK = "Coderen en computers"
BESTAND = "coderen-en-computers.json"
TITEL = "Hoe een computer denkt"
VOLGORDE = 1

VRAGEN = [
    {
        "type": "invultekst",
        "vraag": "Het binaire getal 1011 is in gewone cijfers welk getal?",
        "antwoord": "11",
        "uitleg": "Van rechts naar links staan de plaatsen voor 1, 2, 4 en 8. Hier staat er een 1 bij 8, bij 2 en bij 1, samen 11. Precies zoals bij ons 253 staat voor 2 honderdtallen, 5 tientallen en 3 eenheden, maar dan met machten van twee.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel verschillende waarden kun je met 8 bits voorstellen?",
        "opties": ["256", "64", "128", "512"],
        "antwoord": 0,
        "uitleg": "Elke bit verdubbelt het aantal mogelijkheden: 2 tot de achtste is 256. Acht bits samen heten een byte, en daarmee tel je van 0 tot en met 255.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je rekent bit per bit 1010 EN 1100 uit. Wat komt eruit?",
        "opties": ["1000", "1110", "0110", "0100"],
        "antwoord": 0,
        "uitleg": "Bij EN is een bit alleen 1 als hij in beide getallen 1 is. Van links naar rechts: 1 en 1 geeft 1, 0 en 1 geeft 0, 1 en 0 geeft 0, 0 en 0 geeft 0. Dat wordt 1000. Bij OF zou je 1110 krijgen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat gebeurt er met wat in het RAM-geheugen staat als je de computer uitzet?",
        "opties": [
            "Het is weg, want dat geheugen heeft stroom nodig om te onthouden",
            "Het blijft staan, want dat geheugen bewaart alles zonder stroom",
            "Het wordt automatisch naar de harde schijf weggeschreven",
            "Het blijft nog een paar uur bewaard en verdwijnt dan langzaam",
        ],
        "antwoord": 0,
        "uitleg": "RAM is het werkblad van de computer: razendsnel, maar leeg zodra de stroom wegvalt. De harde schijf of SSD is de kast waar alles bewaard blijft. Daarom ben je een niet-opgeslagen tekst kwijt bij een stroompanne.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is de taak van de processor in een computer?",
        "opties": [
            "Instructies één voor één uitvoeren, miljarden keren per seconde",
            "Alle bestanden en foto's veilig op de lange termijn bewaren",
            "Het beeld naar het scherm sturen en de kleuren juist zetten",
            "De verbinding met het internet openhouden en gegevens ophalen",
        ],
        "antwoord": 0,
        "uitleg": "De processor kan eigenlijk maar heel eenvoudige dingen: optellen, vergelijken, een getal verplaatsen. Dat hij zo veel lijkt te kunnen, komt doordat hij die kleine stapjes onvoorstelbaar snel na elkaar doet.",
    },
    {
        "type": "waarofniet",
        "vraag": "In de meeste programmeertalen is het eerste element van een lijst nummer 0.",
        "antwoord": True,
        "uitleg": "Het nummer is eigenlijk een afstand: hoeveel plaatsen zit dit element van het begin? Dat is nul voor het eerste. Wie dat vergeet, maakt de klassieke off-by-one-fout en pakt er eentje te veel of te weinig.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom geeft een computer bij 0,1 + 0,2 vaak 0,30000000000000004?",
        "opties": [
            "0,1 en 0,2 zijn in het tweetallig stelsel geen exacte getallen",
            "De processor maakt bij optellen af en toe een kleine rekenfout",
            "Het scherm kan maar een beperkt aantal cijfers na de komma tonen",
            "De computer rondt elk antwoord altijd naar boven af, voor de zekerheid",
        ],
        "antwoord": 0,
        "uitleg": "In het tientallig stelsel kun je een derde ook niet exact schrijven: 0,333... loopt eeuwig door. In het tweetallig stelsel overkomt dat net 0,1 en 0,2. De computer bewaart dus een piepklein beetje te veel, en dat zie je bij het optellen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een stapel werkt volgens LIFO: wat er als laatste op ging, gaat er als eerste af. Wat is het tegenovergestelde?",
        "opties": [
            "Een wachtrij, waar wie eerst kwam ook eerst aan de beurt is",
            "Een lijst, waar je elk element meteen bij zijn nummer neemt",
            "Een boom, waar elk element onder een ander element hangt",
            "Een lus, waar je telkens weer bij het begin uitkomt",
        ],
        "antwoord": 0,
        "uitleg": "Een stapel is als een stapel borden: het bovenste bord pak je eerst. Een wachtrij is als de rij aan de kassa. Je computer gebruikt allebei voortdurend, bijvoorbeeld een stapel om bij te houden welke functie welke andere heeft opgeroepen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een functie die zichzelf oproept zonder stopvoorwaarde. Wat gebeurt er?",
        "opties": [
            "De stapel loopt vol en het programma valt stil met een foutmelding",
            "Het programma blijft rustig draaien maar geeft nooit een antwoord",
            "De computer merkt het en slaat de functie vanzelf over",
            "Het programma wordt trager maar komt er uiteindelijk toch uit",
        ],
        "antwoord": 0,
        "uitleg": "Bij elke oproep komt er een laagje op de stapel om te onthouden waar de computer moet terugkeren. Zonder stopvoorwaarde blijven die laagjes komen tot het geheugen op is: een stack overflow. Recursie is dus prima, maar zorg altijd voor een uitweg.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent de aanduiding O(n²) bij een algoritme?",
        "opties": [
            "Tien keer zoveel gegevens kost ongeveer honderd keer zoveel werk",
            "Het algoritme doet er altijd precies twee seconden over",
            "Het algoritme heeft twee keer zoveel geheugen nodig dan gewoonlijk",
            "Het programma bestaat uit twee lussen die na elkaar draaien",
        ],
        "antwoord": 0,
        "uitleg": "Zo'n aanduiding zegt niets over seconden, wel over hoe het werk groeit als de invoer groeit. Bij O(n) verdubbelt het werk als de invoer verdubbelt; bij O(n²) verviervoudigt het. Op een miljoen gegevens is dat het verschil tussen een seconde en dagen.",
    },
    {
        "type": "waarofniet",
        "vraag": "In een gesorteerde lijst van duizend namen vind je er eentje terug in ongeveer tien stappen.",
        "antwoord": True,
        "uitleg": "Met binair zoeken: kijk in het midden, gooi de verkeerde helft weg, en opnieuw. Duizend wordt vijfhonderd, tweehonderdvijftig, en na tien keer halveren blijft er één over. Bij een miljoen namen heb je er maar twintig nodig.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe slaat een computer de kleur van één beeldpunt meestal op?",
        "opties": [
            "Als drie getallen: hoeveel rood, hoeveel groen en hoeveel blauw",
            "Als één getal dat naar een vaste lijst van kleurnamen verwijst",
            "Als de golflengte van het licht dat die kleur zou uitstralen",
            "Als een mengsel van geel, blauw en rood, zoals bij verf",
        ],
        "antwoord": 0,
        "uitleg": "Elk van de drie krijgt meestal een byte, dus een waarde van 0 tot 255. Dat geeft ruim zestien miljoen kleuren. In een webpagina schrijf je dat hexadecimaal: #FF0000 is volle rood, #000000 zwart en #FFFFFF wit.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het woord bug komt van een echte insect dat ooit in een computer vastzat.",
        "antwoord": True,
        "uitleg": "In 1947 haalde het team van Grace Hopper een mot uit de Harvard Mark II. Ze plakten het beestje in het logboek met de notitie dat dit de eerste echte bug was. Het woord bestond in de techniek al langer, maar dit maakte het beroemd.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat doet een compiler?",
        "opties": [
            "Code die mensen schrijven omzetten naar taal die de machine snapt",
            "Fouten in een lopend programma opsporen terwijl het draait",
            "Een programma kleiner maken zodat het minder plaats inneemt",
            "De code netjes uitlijnen zodat ze leesbaarder wordt",
        ],
        "antwoord": 0,
        "uitleg": "De processor begrijpt alleen getallen. Een compiler vertaalt je hele programma vooraf naar die getallen; een interpreter vertaalt regel per regel terwijl het loopt. Vandaar dat een gecompileerd programma vaak sneller start.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het verschil tussen een lus en een voorwaarde in een programma?",
        "opties": [
            "Een lus herhaalt iets, een voorwaarde kiest of iets gebeurt",
            "Een voorwaarde herhaalt iets, een lus kiest of iets gebeurt",
            "Een lus werkt met getallen, een voorwaarde alleen met tekst",
            "Een voorwaarde werkt alleen bovenaan, een lus alleen onderaan",
        ],
        "antwoord": 0,
        "uitleg": "Die twee plus opeenvolging zijn genoeg om élk programma te schrijven, van een rekenmachine tot een spelletje. Alle andere dingen die een taal aanbiedt, zijn handigheidjes daarbovenop.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een computer kan uit zichzelf echt toevallige getallen bedenken.",
        "antwoord": False,
        "uitleg": "Een gewoon programma rekent een reeks uit die willekeurig lijkt maar vastligt zodra je het startgetal kent: pseudotoeval. Voor echt toeval heb je iets uit de buitenwereld nodig, zoals de ruis van een sensor of radioactief verval.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Ada Lovelace wordt vaak de eerste programmeur genoemd. Waarom?",
        "opties": [
            "Ze schreef rond 1843 al een reeks instructies voor een rekenmachine",
            "Ze bouwde in 1843 de eerste machine die zelf kon rekenen",
            "Ze bedacht de eerste programmeertaal met woorden in plaats van cijfers",
            "Ze ontdekte hoe je getallen in nullen en enen kunt schrijven",
        ],
        "antwoord": 0,
        "uitleg": "Ze werkte aan de analytische machine van Charles Babbage, die nooit gebouwd is. In haar aantekeningen staat een uitgewerkte werkwijze om Bernoulligetallen te berekenen. Ze zag bovendien als eerste dat zo'n machine méér kon dan rekenen alleen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een universele Turingmachine?",
        "opties": [
            "Een bedachte machine die elke andere machine kan nabootsen",
            "De eerste computer die tijdens de oorlog echt gebouwd is",
            "Een machine die kan beslissen of een programma ooit stopt",
            "Een test om te zien of een computer menselijk overkomt",
        ],
        "antwoord": 0,
        "uitleg": "Alan Turing beschreef in 1936 een heel eenvoudig apparaatje met een band en een leeskop. Zijn inzicht: één zo'n machine kan de beschrijving van elke andere inlezen en die uitvoeren. Dat is precies wat jouw computer doet als hij een programma opstart.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een computerprogramma kan van elk ander programma vooraf uitrekenen of het ooit zal stoppen.",
        "antwoord": False,
        "uitleg": "Turing bewees in 1936 dat dat onmogelijk is: het stopprobleem. Stel dat zo'n programma bestond, dan kun je er eentje mee bouwen dat precies het tegenovergestelde doet van wat er voorspeld wordt. Dat kan niet, dus het bestaat niet.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat doet een garbage collector?",
        "opties": [
            "Geheugen vrijmaken dat het programma niet meer gebruikt",
            "Oude bestanden van je schijf verwijderen om plaats te maken",
            "Fouten uit je code halen voor je het programma opstart",
            "Ongebruikte programma's van je computer verwijderen",
        ],
        "antwoord": 0,
        "uitleg": "In talen als Java, Python en JavaScript houdt de computer zelf bij welke stukjes geheugen nergens meer gebruikt worden, en geeft die terug. In C moet de programmeur dat met de hand doen, en vergeten leidt tot een geheugenlek.",
    },
]
