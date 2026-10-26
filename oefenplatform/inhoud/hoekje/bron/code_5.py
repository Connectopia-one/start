# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Coderen en computers, deel 5: Gemini-reeks 4 van Kim, aangevuld.

Van de tien codeervragen uit Kims Gemini-reeks 4 (26 oktober 2026) stonden er
acht inhoudelijk al in deel 1 tot 4: P tegenover NP, 0,1 + 0,2, sorteren,
eindeloze recursie, Dijkstra, pakketjes, open source en de compiler. De
blockchain en de reguliere expressie zijn nieuw; de rest komt uit hoeken die
er nog niet waren: geheimschrift, kleurcodes, de millenniumbug, Enigma.
"""

VAK = "Coderen en computers"
BESTAND = "coderen-en-computers.json"
TITEL = "Geheimschrift, kleurcodes en slimme trucs"
VOLGORDE = 5

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Wat maakt een blockchain zo moeilijk om achteraf te vervalsen?",
        "opties": [
            "Elk blok draagt een vingerafdruk van het vorige, en duizenden computers bewaren een kopie",
            "Elk blok ligt opgeborgen in de kluis van één grote bank die er dag en nacht over waakt",
            "Elk blok wordt na een uur automatisch gewist, zodat er nooit iets te vervalsen overblijft",
            "Elk blok zit achter een wachtwoord dat alleen de uitvinder van de blockchain zelf kent",
        ],
        "antwoord": 0,
        "uitleg": "Elk blok bevat de hash, een soort vingerafdruk, van het blok ervoor. Verander je één cijfer in een oud blok, dan klopt zijn vingerafdruk niet meer, en die van alle blokken erna ook niet. Bovendien heeft niet één computer de lijst, maar duizenden tegelijk, en die vergelijken voortdurend. Wie wil vervalsen, moet ze dus bijna allemaal tegelijk om de tuin leiden. Bitcoin is de bekendste toepassing.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een programmeur zoekt in een lange tekst naar postcodes met het patroon [0-9]{4}. Wat is zo'n patroon?",
        "opties": [
            "Een reguliere expressie: zoek vier cijfers na elkaar, eender welke",
            "Een wachtwoord dat de zoekfunctie van het programma ontgrendelt",
            "Een rekensom die alle cijfers van nul tot negen bij elkaar optelt",
            "Een adres in het geheugen waar de postcodes opgeslagen staan",
        ],
        "antwoord": 0,
        "uitleg": "Een reguliere expressie, kortweg regex, is een mini-taal om patronen in tekst te beschrijven. [0-9] betekent: één cijfer. {4} betekent: vier keer. Zo kun je in één regel alle postcodes, e-mailadressen of telefoonnummers uit een tekst vissen, of nakijken of iemand een geldig adres invulde. Programmeurs vinden regex handig en tegelijk berucht, omdat een lang patroon er al snel uitziet als een kat die over het toetsenbord liep.",
    },
    {
        "type": "invultekst",
        "vraag": "Julius Caesar schoof in zijn geheime brieven elke letter drie plaatsen op in het alfabet: A werd D, B werd E. Hoe schrijf je KAT in zijn geheimschrift?",
        "antwoord": "NDW",
        "uitleg": "K schuift drie plaatsen op: L, M, N. A wordt D, en T wordt U, V, W. Zo krijg je NDW. Wie de boodschap ontvangt, schuift gewoon drie plaatsen terug. Dit is een van de oudste geheimschriften die we kennen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is het geheimschrift van Caesar vandaag kinderspel om te kraken?",
        "opties": [
            "Er zijn maar vijfentwintig mogelijke verschuivingen, die probeer je gewoon allemaal",
            "Caesar schreef zijn sleutel altijd netjes onderaan elke brief, voor de zekerheid",
            "Latijnse woorden zijn zo kort dat je ze meteen herkent, ook in geheimschrift",
            "Computers kunnen de oorspronkelijke inkt van de brief opsporen en uitlezen",
        ],
        "antwoord": 0,
        "uitleg": "Een verschuiving van zesentwintig brengt je terug bij het begin, dus er zijn er maar vijfentwintig. Probeer ze allemaal en bij één ervan staat er ineens leesbare tekst: dat heet een aanval met brute kracht. Nog sneller gaat het door te tellen welke letter het vaakst voorkomt. In het Nederlands is dat de E, dus die zit vast achter de letter die in het geheimschrift het meest opduikt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Op websites schrijft men een kleur vaak als #FF0000. Welke kleur is dat?",
        "opties": [
            "Felrood",
            "Felgroen",
            "Felblauw",
            "Pikzwart",
        ],
        "antwoord": 0,
        "uitleg": r"De code bestaat uit drie paartjes: rood, groen en blauw. Ze staan in het zestientallig stelsel, met de cijfers \(0\) tot \(9\) en daarna de letters A tot F. FF is het grootste getal dat met twee tekens kan, namelijk \(255\): rood staat dus voluit, groen en blauw staan op nul. #000000 is zwart, #FFFFFF is wit.",
    },
    {
        "type": "invultekst",
        "vraag": r"Een beeldpunt mengt rood, groen en blauw, en elk van die drie heeft \(256\) standen. Hoeveel verschillende kleuren kan dat beeldpunt tonen?",
        "antwoord": ["16777216", "16 777 216", "16.777.216"],
        "uitleg": r"Voor elke stand van rood heb je \(256\) standen van groen, en voor elke combinatie daarvan nog eens \(256\) van blauw: \(256 \cdot 256 \cdot 256 = 16\,777\,216\). Ruim zestien miljoen kleuren, meer dan een menselijk oog uit elkaar kan houden.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Waarom vreesde men dat computers op \(1\) januari \(2000\) in de war zouden raken?",
        "opties": [
            "Veel programma's bewaarden het jaartal met maar twee cijfers",
            "De klok in computers kon niet verder tellen dan het jaar 1999",
            "Er werd een groot virus verwacht dat op die dag zou ontwaken",
            "Alle satellieten moesten die nacht tegelijk van baan veranderen",
        ],
        "antwoord": 0,
        "uitleg": r"Om dure geheugenruimte te sparen, schreven programmeurs in de jaren zestig en zeventig 1975 gewoon als 75. Na 99 kwam dan 00, en een programma zou kunnen denken dat het \(1900\) was: rente verkeerd berekend, iemand plots honderd jaar oud. Wereldwijd werden jarenlang programma's nagekeken en hersteld. Daardoor gebeurde er op nieuwjaarsnacht bijna niets, en denken sommigen nu ten onrechte dat het gevaar overdreven was.",
    },
    {
        "type": "waarofniet",
        "vraag": r"Op \(19\) januari \(2038\) kunnen sommige oudere computers een probleem krijgen dat lijkt op dat van het jaar \(2000\).",
        "antwoord": True,
        "uitleg": r"Veel systemen tellen de tijd als het aantal seconden sinds \(1\) januari \(1970\), en bewaren dat in een vakje van \(32\) bits. Op \(19\) januari \(2038\) loopt dat vakje vol en springt het getal naar een negatieve waarde: de klok denkt dan dat het \(1901\) is. Nieuwe computers gebruiken \(64\) bits, en daarmee kom je honderden miljarden jaren toe.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je zoomt heel ver in op een vectortekening en op een gewone foto. Wat zie je?",
        "opties": [
            "De tekening blijft scherp, want ze bewaart vormen in plaats van puntjes",
            "De foto blijft scherp, want ze bewaart vormen in plaats van puntjes",
            "Allebei worden ze even wazig, want een scherm heeft maar zoveel puntjes",
            "De tekening verliest haar kleuren, terwijl de foto gewoon scherp blijft",
        ],
        "antwoord": 0,
        "uitleg": "Een foto is een raster van gekleurde vierkantjes. Zoom je in, dan worden die vierkantjes groter en zie je blokjes. Een vectortekening bewaart geen puntjes maar een beschrijving: een cirkel hier, met die straal, in die kleur. De computer tekent ze op elk formaat opnieuw, dus ze blijft haarscherp, op een postzegel én op een reclamebord. Logo's en lettertypes worden daarom bijna altijd als vector gemaakt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe raakte men in de Tweede Wereldoorlog toch aan de geheime berichten van de Duitse Enigma-machine?",
        "opties": [
            "Wiskundigen, eerst Poolse en later Britse, bouwden er speciale machines voor",
            "Een Duitse officier verkocht het volledige codeboek aan de Britse geheime dienst",
            "Een computer van IBM probeerde op een paar uur gewoon alle sleutels uit",
            "Men kraakte de code nooit, maar las de berichten na de oorlog in de archieven",
        ],
        "antwoord": 0,
        "uitleg": r"In \(1932\) kraakte de Poolse wiskundige Marian Rejewski de eerste versie al. In het Britse Bletchley Park bouwden Alan Turing en zijn ploeg daarna de Bombe, een machine die duizenden instellingen per minuut uitprobeerde. Een hulp daarbij: veel berichten begonnen met voorspelbare woorden, zoals een weerbericht. Er bestond toen nog geen computer zoals wij die kennen, het werk in Bletchley hielp die net mee uitvinden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom ziet dezelfde emoji er op een iPhone anders uit dan op een andere gsm?",
        "opties": [
            "Er wordt alleen een nummer verstuurd, en elk toestel tekent dat op zijn eigen manier",
            "De emoji wordt onderweg door de gsm-masten een klein beetje vervormd en verkleurd",
            "Elk merk verstuurt zijn eigen tekening, en de andere toestellen gokken wat het moet zijn",
            "Een gsm van een ander merk toont emoji altijd in een lagere kwaliteit, om data te sparen",
        ],
        "antwoord": 0,
        "uitleg": r"Een emoji is voor de computer gewoon een teken, net als de letter A. Het lachende gezichtje met tranen heeft bijvoorbeeld nummer \(128\,514\). Welke tekening er bij dat nummer hoort, kiest elke fabrikant zelf. Daarom kon een emoji die bij jou vriendelijk lacht, bij je vriend vroeger al eens grimmig uit de hoek komen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In een programma staat: als het regent OF het is koud, dan neem je een jas. Het regent niet, maar het is wel koud. Neem je een jas?",
        "opties": [
            "Ja, want bij OF volstaat het dat één van de twee waar is",
            "Nee, want bij OF moeten ze alle twee tegelijk waar zijn",
            "Nee, want de eerste voorwaarde is niet waar, dus stopt het",
            "Dat kan een computer niet beslissen zonder meer gegevens",
        ],
        "antwoord": 0,
        "uitleg": "In het programmeren betekent OF: minstens één van de twee, of allebei. Voor allebei-tegelijk gebruik je EN. In gewone taal bedoelen we met of soms 'het ene of het andere, maar niet allebei', zoals bij 'wil je soep of frietjes?'. Voor dat tweede heeft de computer een aparte bewerking: XOR, de exclusieve of.",
    },
    {
        "type": "invultekst",
        "vraag": r"Een programma begint met \(x = 3\). Daarna voert het drie keer na elkaar uit: \(x = x \cdot 2\). Welk getal zit er op het einde in \(x\)?",
        "antwoord": "24",
        "uitleg": r"Na de eerste keer is \(x\) gelijk aan \(6\), na de tweede \(12\), na de derde \(24\). Het gelijkheidsteken betekent in een programma niet 'is gelijk aan' zoals in de wiskunde, maar 'stop er dit in'. Vandaar dat \(x = x \cdot 2\) geen onzin is: neem wat er in \(x\) zit, verdubbel het, en stop het terug.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een film is een reeks stilstaande beelden. Hoeveel beelden per seconde toont een bioscoopfilm meestal?",
        "opties": [
            r"\(24\)",
            r"\(6\)",
            r"\(100\)",
            r"\(1000\)",
        ],
        "antwoord": 0,
        "uitleg": r"Al vanaf een twaalftal beelden per seconde zien onze hersenen beweging in plaats van losse foto's. Toen de film geluid kreeg, rond \(1927\), werd \(24\) de vaste afspraak. Computerspellen draaien vaak aan \(60\) beelden per seconde of meer, omdat snelle bewegingen dan vloeiender ogen en het spel sneller reageert.",
    },
    {
        "type": "waarofniet",
        "vraag": r"Een van de allereerste virussen voor de pc kwam in \(1986\) uit Pakistan en heette Brain.",
        "antwoord": True,
        "uitleg": "Twee broers uit Lahore, Basit en Amjad Alvi, schreven het. Het verspreidde zich via diskettes, en hun naam, adres en telefoonnummer stonden er gewoon in. Volgens hen wilden ze nagaan wie hun software illegaal kopieerde. Het virus deed weinig kwaad, maar reisde op een paar maanden de hele wereld rond.",
    },
    {
        "type": "waarofniet",
        "vraag": "Als je een bestand in een zip-map stopt, wordt het altijd kleiner.",
        "antwoord": False,
        "uitleg": "Inpakken werkt door herhalingen te zoeken en korter op te schrijven. Een tekst vol dezelfde woorden krimpt flink. Een foto, film of muziekbestand is meestal al ingepakt, en daar valt niets meer te halen. Zo'n bestand kan in een zip zelfs een tikje groter worden, door de extra gegevens die de zip er zelf bijschrijft. Er bestaat ook geen inpakmethode die élk bestand kleiner maakt: dan kon je blijven inpakken tot er niets overbleef.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het internet en het world wide web zijn twee namen voor hetzelfde.",
        "antwoord": False,
        "uitleg": r"Het internet is het wereldwijde netwerk van kabels, routers en computers, en bestaat sinds de jaren zeventig. Het web is één dienst die daarover loopt: pagina's met links. Het werd in \(1989\) bedacht in het onderzoekscentrum CERN bij Genève, door de Brit Tim Berners-Lee, met hulp van de Belg Robert Cailliau uit Tongeren. E-mail en videobellen gebruiken ook het internet, maar zijn geen web.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een computer versloeg de wereldkampioen schaken al in 1997, maar bij het bordspel go duurde dat tot 2016. Waarom?",
        "opties": [
            "Bij go zijn er zoveel mogelijke zetten dat gewoon vooruitrekenen niet volstaat",
            "Bij go zijn de regels nooit opgeschreven, dus kon een computer ze niet leren",
            "Go speel je met zwarte en witte stenen, en die kon een camera slecht zien",
            "Bij go mag je stenen achteraf verschuiven, en dat kan een computer niet volgen",
        ],
        "antwoord": 0,
        "uitleg": r"Een go-bord heeft \(19\) bij \(19\) punten, en er zijn meer mogelijke stellingen dan er atomen in het heelal zijn. Alle zetten doorrekenen is daar onbegonnen werk. AlphaGo leerde daarom eerst uit miljoenen partijen welke zetten er goed uitzien, en speelde daarna tegen zichzelf. Zo versloeg het in \(2016\) de Koreaanse topspeler Lee Sedol, met zetten waar kenners eerst om lachten.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe weet je gsm via gps waar je bent?",
        "opties": [
            "Hij meet hoelang de signalen van minstens vier satellieten onderweg waren",
            "Satellieten fotograferen de aarde en zoeken jouw toestel op hun beelden",
            "Hij stuurt een signaal omhoog en een satelliet roept terug waar je staat",
            "Elke straat heeft een eigen zendertje dat je gsm voorbij ziet komen",
        ],
        "antwoord": 0,
        "uitleg": "Gps-satellieten roepen voortdurend de exacte tijd en hun plaats rond. Je gsm luistert alleen maar. Uit hoe lang elk signaal onderweg was, rekent hij de afstand tot elke satelliet uit, en met vier zulke afstanden ligt jouw plek vast. Je gsm verstuurt daarvoor zelf niets: de satellieten weten dus niet dat jij er bent.",
    },
    {
        "type": "invultekst",
        "vraag": r"Een fietsslot heeft een code van vier cijfers, van \(0000\) tot \(9999\). Hoeveel verschillende codes zijn er?",
        "antwoord": ["10000", "10 000", "10.000"],
        "uitleg": r"Elk van de vier wieltjes heeft tien standen: \(10 \cdot 10 \cdot 10 \cdot 10 = 10\,000\). Een dief die er één per seconde probeert, is in het slechtste geval na bijna drie uur rond. Daarom gaat je gsm na een paar foute pogingen op slot: zo maakt hij uitproberen onmogelijk, ook al is de code kort.",
    },
]
