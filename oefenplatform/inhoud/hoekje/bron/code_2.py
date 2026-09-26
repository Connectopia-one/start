# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Coderen en computers, deel 2: algoritmes en netwerken."""

VAK = "Coderen en computers"
BESTAND = "coderen-en-computers.json"
TITEL = "Algoritmes, netwerken en geheimschrift"
VOLGORDE = 2

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Waarover gaat de beroemde vraag P versus NP?",
        "opties": [
            "Of alles wat snel te controleren is, ook snel op te lossen is",
            "Of een computer ooit even slim kan worden als een mens",
            "Of er een grens is aan hoe snel een processor kan worden",
            "Of elk programma uiteindelijk vanzelf tot een einde komt",
        ],
        "antwoord": 0,
        "uitleg": "Een ingevulde sudoku nakijken gaat in een paar tellen; een moeilijke sudoku zelf oplossen kan veel langer duren. Niemand heeft ooit bewezen dat dat verschil echt moet bestaan. Er staat een miljoen dollar op een sluitend antwoord.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Bij versleuteling met een publieke sleutel deel je die sleutel gerust met iedereen. Hoe kan dat veilig zijn?",
        "opties": [
            "Met die sleutel kun je enkel vergrendelen, niet meer openen",
            "De sleutel verandert elke paar seconden automatisch van vorm",
            "Alleen computers van hetzelfde merk mogen de sleutel gebruiken",
            "De sleutel werkt maar één keer en is daarna waardeloos geworden",
        ],
        "antwoord": 0,
        "uitleg": "Zo'n slot heeft twee sleutels die bij elkaar horen: de publieke om dicht te doen, de private om open te doen. Bij RSA steunt dat op iets eenvoudigs: twee grote priemgetallen vermenigvuldigen is makkelijk, het product weer ontbinden is monsterlijk zwaar.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het verschil tussen inpakken met en zonder verlies?",
        "opties": [
            "Zonder verlies krijg je het origineel exact terug, met verlies niet",
            "Met verlies krijg je het origineel exact terug, zonder verlies niet",
            "Zonder verlies werkt alleen bij tekst, met verlies alleen bij beeld",
            "Met verlies maakt het bestand groter, zonder verlies kleiner",
        ],
        "antwoord": 0,
        "uitleg": "Een zipbestand of een PNG geeft je elke bit terug; een JPEG of een MP3 gooit details weg die je toch nauwelijks ziet of hoort, en is daardoor veel kleiner. Voor een programma of een tekst mag je nooit iets weggooien, voor een vakantiefoto wel.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een IP-adres?",
        "opties": [
            "Het nummer waaraan een toestel op het netwerk te herkennen is",
            "De naam van een website zoals je die in de balk typt",
            "Het wachtwoord waarmee je op een draadloos netwerk raakt",
            "Het serienummer dat de fabrikant in je toestel gebrand heeft",
        ],
        "antwoord": 0,
        "uitleg": "Zonder zo'n nummer weet het netwerk niet waar het antwoord naartoe moet, zoals een brief zonder adres. Een DNS-server vertaalt de naam die jij typt naar dat nummer. Het serienummer van je netwerkkaart is iets anders: dat heet een MAC-adres.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een goed bewaard wachtwoord staat versleuteld in de databank, zodat de website het weer kan uitlezen.",
        "antwoord": False,
        "uitleg": "Een goede website bewaart geen wachtwoord, ook niet versleuteld, maar een hash: een berekening die je niet kunt terugdraaien. Bij het inloggen doet ze dezelfde berekening en vergelijkt de uitkomst. Daarom kan zo'n site je wachtwoord nooit toesturen, alleen laten resetten.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat doet het slotje bij https in je browser?",
        "opties": [
            "Het verkeer tussen jou en de site is versleuteld onderweg",
            "De site is door iemand gecontroleerd en betrouwbaar bevonden",
            "De site slaat geen enkel gegeven over jou op de server op",
            "Je bent volledig anoniem: niemand ziet welke site je bezoekt",
        ],
        "antwoord": 0,
        "uitleg": "Wie onderweg meeluistert, ziet alleen wartaal. Wat het slotje níét zegt: of de site eerlijk is. Ook een oplichterssite kan https hebben. Kijk dus altijd ook naar de naam in de adresbalk.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je moet een miljoen namen sorteren. Welke aanpak is veruit de snelste?",
        "opties": [
            "De lijst telkens in twee helften splitsen en die samenvoegen",
            "Telkens twee buren vergelijken en ze eventueel omwisselen",
            "Steeds de kleinste van de rest zoeken en vooraan zetten",
            "De namen één voor één op hun juiste plaats tussenschuiven",
        ],
        "antwoord": 0,
        "uitleg": "Splitsen en samenvoegen heet mergesort en kost ongeveer n keer log n werk: voor een miljoen namen zo'n twintig miljoen stappen. De drie andere kosten er n keer n, dus duizend miljard. Dat is het verschil tussen een seconde en dagen.",
    },
    {
        "type": "waarofniet",
        "vraag": "De cloud is eigenlijk gewoon de computer van iemand anders.",
        "antwoord": True,
        "uitleg": "Je bestanden staan in een datacenter vol servers, meestal in meerdere kopieën op verschillende plekken. Handig, want je geraakt er overal bij, maar het betekent ook dat iemand anders die schijven beheert. Daarom blijft een eigen back-up nuttig.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het grote verschil tussen een gewoon programma en machinaal leren?",
        "opties": [
            "Een gewoon programma volgt regels, machinaal leren leidt ze af uit voorbeelden",
            "Machinaal leren volgt regels, een gewoon programma leidt ze af uit voorbeelden",
            "Machinaal leren heeft geen processor nodig, een gewoon programma wel",
            "Een gewoon programma werkt met tekst, machinaal leren alleen met beeld",
        ],
        "antwoord": 0,
        "uitleg": "Wil je katten herkennen, dan is het bijna onmogelijk om alle regels op te schrijven. Toon in plaats daarvan honderdduizend foto's met het juiste label, en het model stelt zijn eigen instellingen bij tot het meestal juist zit. Vandaar dat zo'n model soms fouten maakt die een mens nooit zou maken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een QR-code blijft leesbaar, ook als er een stuk van weg is. Hoe komt dat?",
        "opties": [
            "Er zit foutcorrectie in: de gegevens staan er meermaals in verwerkt",
            "De scanner raadt de ontbrekende stukjes op basis van de vorm",
            "De zwarte vierkanten in de hoeken bevatten de hele boodschap",
            "Een QR-code bevat zo weinig tekst dat een stukje volstaat",
        ],
        "antwoord": 0,
        "uitleg": "Met de Reed-Solomon-methode zitten er extra controlegegevens in, tot dertig procent van de code. Daarom kun je zelfs een logo in het midden plakken. De drie grote vierkanten in de hoeken zijn er om de scanner te laten zien hoe de code gedraaid staat.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een cookie is een klein programma dat een website op je computer laat draaien.",
        "antwoord": False,
        "uitleg": "Een cookie is geen programma maar een kort tekstje, bijvoorbeeld een nummer. De site stuurt het mee terug bij elk bezoek, en herkent je zo. Handig om ingelogd te blijven, maar ook de manier waarop advertentiebedrijven je over verschillende sites volgen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent het dat een programma open source is?",
        "opties": [
            "Iedereen mag de broncode inkijken, gebruiken en aanpassen",
            "Het programma is altijd gratis en mag nooit geld kosten",
            "Het programma werkt op elk besturingssysteem dat bestaat",
            "De makers geven geen ondersteuning bij problemen",
        ],
        "antwoord": 0,
        "uitleg": "Gratis en open zijn twee verschillende dingen: er bestaat betaalde open software en gratis gesloten software. Het voordeel van open code is dat duizenden mensen fouten en lekken kunnen vinden. Linux, Firefox en VLC werken zo.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je stuurt een foto naar de andere kant van de wereld. Hoe reist die?",
        "opties": [
            "In kleine pakketjes die elk hun eigen weg zoeken en weer samenkomen",
            "In één stuk over één vaste lijn die zolang gereserveerd blijft",
            "Als radiogolven die via een satelliet rechtstreeks aankomen",
            "Als één lange stroom die elke router onderweg eerst volledig opslaat",
        ],
        "antwoord": 0,
        "uitleg": "Dat heet pakketschakeling, en het is de vondst waarop het hele internet rust. Valt er onderweg een verbinding weg, dan nemen de volgende pakketjes gewoon een andere route. Aan de aankomst worden ze weer in de juiste volgorde gelegd.",
    },
    {
        "type": "waarofniet",
        "vraag": "De wet van Moore is een natuurwet die zegt hoe snel chips moeten worden.",
        "antwoord": False,
        "uitleg": "Het is geen natuurwet maar een waarneming: Gordon Moore zag in 1965 dat het aantal transistors op een chip ongeveer elke twee jaar verdubbelde. Dat klopte decennialang, maar het is een trend, geen wet, en hij loopt intussen op zijn einde.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom kan een computer 'A' en '65' op dezelfde manier opslaan?",
        "opties": [
            "Alles is bits; wat het betekent hangt af van hoe je het leest",
            "Letters worden altijd eerst in getallen omgerekend en dan bewaard",
            "De computer bewaart bij elke letter stiekem ook haar tekening",
            "Letters en getallen staan in twee gescheiden soorten geheugen",
        ],
        "antwoord": 0,
        "uitleg": "In het geheugen staat alleen 01000001. Lees je dat als een getal, dan is het 65; lees je het als een teken, dan is het de hoofdletter A. Daarom moet een programma altijd weten wat voor soort gegeven het beetpakt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is de Turingtest?",
        "opties": [
            "Kan een mens in een gesprek nog uitmaken wie de machine is?",
            "Kan een machine een rekensom sneller oplossen dan een mens?",
            "Kan een programma uitrekenen of een ander programma stopt?",
            "Kan een machine zonder fouten een hele dag blijven draaien?",
        ],
        "antwoord": 0,
        "uitleg": "Turing stelde in 1950 voor om de vraag of een machine kan denken te vervangen door iets meetbaars: typt iemand met een mens of met een machine, en merkt hij het verschil? Of dat echt iets over denken zegt, wordt nog altijd druk besproken.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een bestand dat je uit de prullenbak verwijdert, staat vaak nog een tijd op de schijf.",
        "antwoord": True,
        "uitleg": "Meestal wordt alleen het verwijzinkje weggehaald, zoals een titel uit de inhoudstafel schrappen terwijl de bladzijden blijven. De gegevens blijven staan tot er iets anders overheen geschreven wordt, en zijn tot dan vaak terug te halen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het handigste aan een functie in een programma?",
        "opties": [
            "Je schrijft een stuk werk één keer en gebruikt het overal opnieuw",
            "Je programma wordt er automatisch sneller door bij het draaien",
            "De computer onthoudt de uitkomst en hoeft nooit te herrekenen",
            "Je code neemt er minder plaats mee in op de harde schijf",
        ],
        "antwoord": 0,
        "uitleg": "Moet er iets veranderen, dan pas je één plek aan in plaats van twintig. Dat scheelt niet alleen typwerk: het is de belangrijkste manier om fouten te vermijden in een groot programma.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel bits zitten er in één byte?",
        "antwoord": "8",
        "uitleg": "Acht. Daarmee kun je 256 verschillende waarden voorstellen, precies genoeg voor alle letters, cijfers en leestekens van de oude ASCII-tabel. Een kilobyte is er duizend, een megabyte een miljoen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is een back-up op dezelfde computer geen echte back-up?",
        "opties": [
            "Bij diefstal, brand of een kapotte schijf ben je alles tegelijk kwijt",
            "Een kopie op dezelfde schijf raakt vanzelf na verloop van tijd stuk",
            "De computer overschrijft zo'n kopie automatisch na een paar weken",
            "Een tweede kopie maakt je computer merkbaar trager bij het opstarten",
        ],
        "antwoord": 0,
        "uitleg": "De vuistregel heet drie-twee-één: drie kopieën, op twee soorten dragers, waarvan één ergens anders. En een back-up die je nooit hebt teruggezet, weet je eigenlijk niet of hij werkt.",
    },
]
