# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Coderen en computers, deel 4: vragen van Kim, aangevuld.

Van Kims tien vragen van 8 oktober 2026 stonden er zeven inhoudelijk al in
deel 1 tot 3 (RAM tegenover schijf, API, qubits, de oneindige lus, garbage
collection, open source en Big O). Die zijn vervangen door nieuwe.
"""

VAK = "Coderen en computers"
BESTAND = "coderen-en-computers.json"
TITEL = "Beelden, netwerken en slimme machines"
VOLGORDE = 4

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Een recursieve functie roept zichzelf op. Wat heeft zo'n functie absoluut nodig om bruikbaar te zijn?",
        "opties": [
            "Een geval waarin ze zichzelf niet meer oproept",
            "Een lus die rond de hele functie heen staat opgesteld",
            "Minstens twee getallen die ze met elkaar vergelijkt",
            "Een tweede functie die haar van buitenaf stopzet",
        ],
        "antwoord": 0,
        "uitleg": "Dat heet het basisgeval. Bij faculteit is dat: 1 maal 1 is 1, klaar. Elke oproep moet een stapje dichter bij dat basisgeval komen, anders stapelt de computer oproepen op tot zijn geheugen vol zit. Veel problemen worden met recursie opeens kort: zoeken in een map met mappen erin, bijvoorbeeld.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het gevaar van een sql-injectie bij een website?",
        "opties": [
            "Iemand typt in een invulveld een stuk databasetaal mee",
            "Iemand stuurt zoveel bezoekers tegelijk dat de server plat gaat",
            "Iemand onderschept het verkeer tussen de bezoeker en de website",
            "Iemand raadt het wachtwoord van de beheerder door te blijven proberen",
        ],
        "antwoord": 0,
        "uitleg": "Plakt de website jouw tekst zomaar in haar databankopdracht, dan voert ze jouw stukje mee uit en kan je gegevens opvragen of wissen. De oplossing is oud en simpel: geef wat de bezoeker typt apart mee, als gegeven, nooit als deel van de opdracht. Toch staat het al jaren in de top drie van de grootste lekken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een webpagina is gemaakt met html, css en javascript. Wat doet elk van die drie?",
        "opties": [
            "Html is de inhoud, css het uitzicht, javascript het gedrag",
            "Html is het uitzicht, css het gedrag, javascript de inhoud",
            "Html is het gedrag, css de inhoud, javascript het uitzicht",
            "Alle drie doen hetzelfde, het hangt af van welke browser je kiest",
        ],
        "antwoord": 0,
        "uitleg": "Html zet de titels, tekst en knoppen op hun plaats, css bepaalt kleur, lettertype en ligging, en javascript laat er iets gebeuren als je klikt. Zet je de css uit, dan blijft een kale maar leesbare pagina over. Dat is meteen de reden waarom een goed gebouwde site ook werkt voor wie hem laat voorlezen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat kan een grafische kaart beter dan de gewone processor van een computer?",
        "opties": [
            "Duizenden eenvoudige bewerkingen tegelijk uitvoeren",
            "Eén lange ingewikkelde berekening veel sneller afwerken",
            "Veel meer gegevens langdurig bewaren zonder stroom",
            "Programma's begrijpen die voor een andere computer geschreven zijn",
        ],
        "antwoord": 0,
        "uitleg": "Een processor is een paar heel slimme werkkrachten, een grafische kaart een leger van duizenden eenvoudige. Voor een beeld moet elk van de miljoenen beeldpunten apart berekend worden, en dat gaat prima tegelijk. Daarom draait vandaag ook kunstmatige intelligentie op grafische kaarten: dat rekenwerk heeft precies dezelfde vorm.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je opent een jpg-foto, past niets aan en bewaart ze toch telkens opnieuw. Wat gebeurt er?",
        "opties": [
            "De foto wordt elke keer een beetje slechter",
            "Er verandert niets, het bestand blijft identiek",
            "Het bestand wordt elke keer merkbaar groter",
            "De kleuren draaien langzaam naar het blauw toe",
        ],
        "antwoord": 0,
        "uitleg": "Jpg gooit bij elke bewaarbeurt details weg die het oog toch nauwelijks ziet, en dat is onomkeerbaar. Doe je dat honderd keer, dan zie je blokjes en vegen verschijnen. Png en raw werken verliesvrij: daar blijft elk beeldpunt zoals het was, en dat kost plaats.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe leert een computerprogramma een kat van een hond te onderscheiden?",
        "opties": [
            "Het krijgt duizenden foto's met het juiste antwoord erbij",
            "Een programmeur schrijft alle regels op waaraan je een kat herkent",
            "Het zoekt tijdens het kijken zelf op internet wat er op de foto staat",
            "Het vergelijkt de foto met één perfecte voorbeeldfoto van een kat",
        ],
        "antwoord": 0,
        "uitleg": "Het programma gokt, hoort hoe ver het ernaast zat en draait aan miljoenen interne knopjes om het de volgende keer beter te doen. Niemand schrijft op wat een kat is, want dat lukt niet: snorharen heeft een zeehond ook. De keerzijde is dat zo'n model ook de fouten en de scheefheid van zijn voorbeelden overneemt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom kan een taalmodel een antwoord geven dat volledig verzonnen is en toch heel zeker klinkt?",
        "opties": [
            "Het voorspelt wat goed klinkt, niet wat het heeft nagekeken",
            "Het liegt met opzet als het de vraag niet graag beantwoordt",
            "Het haalt zijn antwoorden altijd ergens van een website en kiest de verkeerde",
            "Het is stuk, want een goed getraind model vergist zich nooit",
        ],
        "antwoord": 0,
        "uitleg": "Zo'n model is getraind om telkens het volgende woord te kiezen dat past, niet om de waarheid op te zoeken. Een vlotte zin met een verzonnen boektitel erin past perfect, dus komt hij eruit alsof het klopt. Daarom blijft dezelfde regel gelden als bij een vreemde op straat: leuk antwoord, maar controleer het zelf.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat doet een vpn als je op openbare wifi zit?",
        "opties": [
            "Het stuurt je verkeer versleuteld via een andere server",
            "Het maakt je internetverbinding merkbaar sneller dan ze was",
            "Het verwijdert alle virussen van het netwerk waarop je zit",
            "Het verbergt je volledig, zodat niemand ter wereld je nog kan volgen",
        ],
        "antwoord": 0,
        "uitleg": "Wie meeluistert op het netwerk, ziet enkel nog een versleutelde tunnel naar die ene server. Maar de uitbater van die server ziet wél alles, dus je verplaatst het vertrouwen, je laat het niet verdwijnen. En de websites zelf herkennen je nog altijd aan je account en je cookies.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een verbinding met veel bandbreedte maar veel vertraging: waarvoor is dat vervelend?",
        "opties": [
            "Een spel of een videogesprek, want elk antwoord komt te laat",
            "Een grote film downloaden, want die komt nooit helemaal binnen",
            "Een back-up van je computer maken, want die kan dan niet doorgaan",
            "Een foto bekijken, want die wordt dan met minder kleuren getoond",
        ],
        "antwoord": 0,
        "uitleg": "Bandbreedte is hoe breed de weg is, vertraging hoe lang de rit duurt. Een vrachtwagen vol harde schijven naar Parijs rijden heeft gigantische bandbreedte en een vertraging van vier uur. Voor een film maakt dat niet uit, voor een gesprek wel: daar telt elke tiende seconde.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Twee delen van een programma tellen tegelijk hetzelfde getal met één op. Wat kan er misgaan?",
        "opties": [
            "Allebei lezen ze dezelfde oude waarde, dus er komt er maar één bij",
            "Het getal wordt dubbel zo groot als het had moeten worden",
            "Het programma valt altijd meteen stil met een duidelijke foutmelding",
            "Er kan niets misgaan, de computer doet alles netjes na elkaar",
        ],
        "antwoord": 0,
        "uitleg": "Optellen is in werkelijkheid drie stappen: lezen, er één bij doen, terugschrijven. Komt de tweede ertussen na het lezen, dan schrijft ze hetzelfde resultaat. Zo'n fout heet een race, en hij is berucht omdat hij meestal nét niet optreedt terwijl je kijkt. Een slot rond die drie stappen lost het op.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe kan een zoekmachine in een halve seconde door miljarden pagina's gaan?",
        "opties": [
            "Ze heeft vooraf een register gemaakt van welk woord waar staat",
            "Ze bezoekt op het moment van je vraag razendsnel alle websites",
            "Ze vraagt het aan de websites zelf, die meteen antwoorden",
            "Ze bewaart elke vraag die ooit gesteld is met het juiste antwoord erbij",
        ],
        "antwoord": 0,
        "uitleg": "Robots lezen dag en nacht pagina's en bouwen een register, zoals de index achteraan een boek: bij het woord vulkaan staat een lijst van pagina's. Jouw vraag wordt in dat register opgezocht, niet op het web. Daarom duurt het soms dagen voor een nieuwe pagina te vinden is.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het verschil tussen een computervirus en een worm?",
        "opties": [
            "Een worm verspreidt zich zelf, een virus heeft een gastbestand nodig",
            "Een virus verspreidt zich zelf, een worm heeft een gastbestand nodig",
            "Een worm richt schade aan, een virus kijkt alleen maar mee",
            "Er is geen verschil, het zijn twee woorden voor hetzelfde",
        ],
        "antwoord": 0,
        "uitleg": "Een virus nestelt zich in een bestand of programma en reist mee wanneer iemand dat doorgeeft. Een worm heeft niemand nodig: hij zoekt zelf gaten in het netwerk en springt verder. Daarom gaat een worm zo snel. In 2017 legde WannaCry op één dag ziekenhuizen en fabrieken in honderdvijftig landen stil.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een computer doet alles stap voor stap volgens vaste regels. Hoe maakt hij dan een willekeurig getal?",
        "opties": [
            "Hij rekent uit een startwaarde een rij uit die willekeurig lijkt",
            "Hij kiest zomaar een getal uit zijn geheugen, zonder enige regel",
            "Hij vraagt het telkens aan een server van de fabrikant",
            "Dat kan niet, dus elk spel gebruikt altijd dezelfde getallen",
        ],
        "antwoord": 0,
        "uitleg": "Zo'n rij heet pseudotoevallig: begin je twee keer met dezelfde startwaarde, dan krijg je twee keer exact dezelfde getallen. Handig om een spel te kunnen naspelen, gevaarlijk voor beveiliging. Daarom tappen computers voor echte sleutels iets rommeligs af: ruis van de temperatuur, de tijd tussen toetsaanslagen, muisbewegingen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom laat een website je soms plaatjes met fietsen of verkeerslichten aanduiden?",
        "opties": [
            "Om te zien of je een mens bent, en meteen om beelden te laten benoemen",
            "Om te meten hoe snel jouw internetverbinding de beelden binnenhaalt",
            "Om jouw smaak te leren kennen en er reclame op af te stemmen",
            "Omdat de wet voorschrijft dat elke website een test moet voorleggen",
        ],
        "antwoord": 0,
        "uitleg": "Het is een test die voor een mens makkelijk en voor een programma lastig is. Maar je werkt er ook gratis mee: jouw aanduidingen werden gebruikt om boeken te digitaliseren en om zelfrijdende auto's beelden te leren herkennen. Intussen worden programma's er beter in dan mensen, dus kijken sites nu vooral naar hoe je muis beweegt.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een unittest is een stukje code dat controleert of een ander stukje code doet wat het moet doen.",
        "antwoord": True,
        "uitleg": "Je schrijft op: met deze invoer moet er dit uitkomen. Bij elke wijziging draaien al die tests opnieuw, vaak honderden tegelijk, en ze klagen meteen als er iets stuk is dat vorige week nog werkte. Zonder tests durft niemand nog iets te veranderen aan een groot programma, en dan verroest het.",
    },
    {
        "type": "waarofniet",
        "vraag": "In een programma betekent null hetzelfde als het getal nul.",
        "antwoord": False,
        "uitleg": "Nul is een waarde, null betekent dat er helemaal geen waarde is. Nul euro op je rekening is iets anders dan geen rekening hebben. Tony Hoare, die null in 1965 bedacht, noemde het later zijn vergissing van een miljard dollar, omdat zoveel programma's crashen op iets wat er niet blijkt te zijn.",
    },
    {
        "type": "waarofniet",
        "vraag": "Met https erbij kan niemand nog zien wélke website je bezoekt.",
        "antwoord": False,
        "uitleg": "De inhoud van de pagina's is versleuteld, maar de naam van de website lekt onderweg nog altijd: je computer moet ze opvragen om er te geraken. Je internetleverancier ziet dus wel dát je op een bepaalde site was, niet welke pagina's je daar las of wat je typte.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een computer kan twee getallen van duizend cijfers met elkaar vermenigvuldigen, ook al past zo'n getal in geen enkele geheugenplaats.",
        "antwoord": True,
        "uitleg": "Het programma zet zo'n getal in stukken en rekent ermee zoals jij op papier doet: cijfer voor cijfer, met onthouden. Dat is precies wat beveiliging nodig heeft, want de sleutels achter het slotje in je browser zijn getallen van honderden cijfers.",
    },
    {
        "type": "invultekst",
        "vraag": "Binair zoeken vindt een naam in een gesorteerde lijst van 1000 namen in ongeveer 10 stappen. Hoeveel stappen heeft het ongeveer nodig bij 2000 namen?",
        "antwoord": "11",
        "uitleg": "Elke stap halveert de lijst, dus een lijst twee keer zo lang kost maar één stap extra. Bij een miljoen namen ben je er in twintig stappen, bij een miljard in dertig. Daarom is dit algoritme zo geliefd: het wordt nauwelijks trager als je gegevens exploderen.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel bits heb je minstens nodig om 1000 verschillende waarden te kunnen voorstellen?",
        "antwoord": "10",
        "uitleg": "Met n bits maak je 2 tot de n verschillende combinaties. Negen bits geven er 512, te weinig, tien bits geven er 1024, net genoeg. Dat is ook waarom een kilobyte eigenlijk 1024 bytes is en niet 1000: de tweemachten liggen nu eenmaal niet op ronde tientallen.",
    },
]
