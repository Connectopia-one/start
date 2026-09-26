# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Coderen en computers, deel 3: vragen van Kim, aangevuld."""

VAK = "Coderen en computers"
BESTAND = "coderen-en-computers.json"
TITEL = "Poorten, netwerken en veiligheid"
VOLGORDE = 3

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Welke logische poort geeft alleen een 1 als de twee ingangen van elkaar verschillen?",
        "opties": ["De XOR-poort", "De AND-poort", "De OR-poort", "De NOT-poort"],
        "antwoord": 0,
        "uitleg": "XOR staat voor exclusive or: het een of het ander, maar niet allebei. 1 en 0 geeft 1, 1 en 1 geeft 0. Met een handvol van zulke poortjes bouw je een optelmachine, en daarmee uiteindelijk een hele processor.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Bij objectgericht programmeren kan een nieuwe klasse eigenschappen van een bestaande overnemen. Hoe heet dat?",
        "opties": [
            "Overerving",
            "Recursie",
            "Compilatie",
            "Iteratie",
        ],
        "antwoord": 0,
        "uitleg": "Schrijf één keer een klasse Dier met alles wat elk dier kan, en laat Hond en Kat daarvan erven. Ze krijgen dat gedrag er gratis bij en vullen alleen aan wat anders is. Zo hoef je hetzelfde nooit twee keer te schrijven.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat bedoelt men met het lawine-effect bij een hashfunctie?",
        "opties": [
            "Verander één tekentje in de invoer en de uitvoer is volledig anders",
            "Hoe meer mensen tegelijk hashen, hoe trager de berekening wordt",
            "Een hash wordt langer naarmate je er meer tekst in stopt",
            "Twee bijna gelijke invoeren geven ook een bijna gelijke uitvoer",
        ],
        "antwoord": 0,
        "uitleg": "Precies dat maakt een hash bruikbaar: aan de uitkomst valt niets af te leiden over wat erin ging, ook niet als je duizend kleine variaties probeert. Vandaar dat wachtwoorden zo bewaard worden. De laatste optie is net het tegenovergestelde en zou een hash waardeloos maken.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een deadlock in een computersysteem?",
        "opties": [
            "Twee processen wachten allebei eeuwig op iets dat de ander vasthoudt",
            "Een virus dat het hele systeem op slot zet en losgeld vraagt",
            "Een lek in de firewall waardoor er van buitenaf ingebroken wordt",
            "Een programma dat blijft draaien maar nooit een antwoord teruggeeft",
        ],
        "antwoord": 0,
        "uitleg": "Zoals twee mensen in een smalle gang die allebei beleefd wachten tot de ander passeert. Geen van beide doet iets fout, en toch gebeurt er niets meer. Besturingssystemen gaan dat te lijf door altijd dezelfde volgorde af te spreken, of door een van de twee wakker te schudden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat doet een DNS-server?",
        "opties": [
            "Hij vertaalt een naam zoals connectopia.one naar een nummer",
            "Hij bewaart de bestanden van een website op zijn harde schijf",
            "Hij controleert de binnenkomende e-mail op virussen en spam",
            "Hij verdeelt het internetverkeer eerlijk over alle gebruikers",
        ],
        "antwoord": 0,
        "uitleg": "Het is het telefoonboek van het internet. Jij typt een naam, je computer vraagt het bijbehorende IP-adres op, en pas dan kan de verbinding gelegd worden. Valt dat telefoonboek uit, dan lijkt het alsof het halve internet weg is, terwijl alle servers gewoon draaien.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een primaire sleutel in een databank?",
        "opties": [
            "Een kolom waarvan de waarde bij elke rij verschillend is",
            "Het hoofdwachtwoord waarmee de hele databank versleuteld is",
            "De tabel die als eerste aangemaakt werd in de databank",
            "De kolom die het vaakst gebruikt wordt bij het zoeken",
        ],
        "antwoord": 0,
        "uitleg": "Zo kun je elke rij eenduidig aanwijzen, ook als twee kinderen dezelfde naam hebben. Daarom staat er in bijna elke tabel een id-kolom vooraan. In het oefenplatform hangt de voortgang van een kind aan zo'n id, niet aan zijn naam.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het woord bit is een samentrekking van binary digit.",
        "antwoord": True,
        "uitleg": "Bedacht door John Tukey in de jaren veertig. Eén bit is het kleinste stukje informatie dat bestaat: ja of nee, aan of uit. Alles wat een computer doet, van een film tot dit vraagje, is uiteindelijk een lange rij van die keuzes.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een API?",
        "opties": [
            "Een afgesproken manier waarop programma's elkaar iets kunnen vragen",
            "Een taal waarin je websites schrijft, net zoals je HTML gebruikt",
            "Een beveiligd stuk geheugen waar wachtwoorden bewaard worden",
            "Een programma dat automatisch fouten uit je code haalt",
        ],
        "antwoord": 0,
        "uitleg": "Denk aan een loket: jij moet niet weten hoe het er achter werkt, je moet weten wat je mag vragen en wat je terugkrijgt. Een weer-app haalt zo de voorspelling op bij het weerinstituut, zonder ook maar iets van hun systemen te kennen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je hebt honderdduizend namen met een telefoonnummer erbij, en je wil razendsnel het nummer bij één naam vinden. Wat gebruik je?",
        "opties": [
            "Een hashtabel, waar de naam zelf de plaats in het geheugen bepaalt",
            "Een gewone lijst, die je van voren naar achteren doorloopt",
            "Een stapel, waarbij je telkens het bovenste element bekijkt",
            "Een wachtrij, waarbij wie eerst kwam ook eerst behandeld wordt",
        ],
        "antwoord": 0,
        "uitleg": "Een hashtabel rekent de naam om tot een getal en gebruikt dat als vakje. Je hoeft dus niets te doorzoeken: je rekent meteen uit waar het staat. Vandaar dat het bij honderd of bij honderdduizend namen ongeveer even snel gaat.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom heeft een computer een cache?",
        "opties": [
            "Om iets wat net gebruikt werd dichtbij te houden, want ophalen kost tijd",
            "Om bestanden veilig te bewaren als de stroom uitvalt",
            "Om te vermijden dat twee programma's tegelijk hetzelfde doen",
            "Om alle gegevens kleiner te maken zodat er meer op past",
        ],
        "antwoord": 0,
        "uitleg": "Het verschil is enorm: iets uit het cachegeheugen van de processor halen gaat honderden keren sneller dan uit het gewone geheugen, en dat weer duizenden keren sneller dan van schijf. Je browser doet hetzelfde met plaatjes van een website die je net bezocht.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een SSD is sneller dan een gewone harde schijf omdat hij sneller ronddraait.",
        "antwoord": False,
        "uitleg": "Een SSD draait helemaal niet: er zitten geen bewegende delen in, alleen geheugenchips. Een klassieke harde schijf moet een leeskop naar de juiste plek op een draaiende schijf bewegen, en dat mechanische wachten is net wat hem traag maakt.",
    },
    {
        "type": "waarofniet",
        "vraag": "De router bij jou thuis bewaart alle websites die iemand in huis bezoekt.",
        "antwoord": False,
        "uitleg": "Een router is een wegwijzer, geen archief: router komt van route. Hij stuurt pakketjes naar het juiste toestel en onthoudt alleen even welk antwoord bij welke vraag hoort. Op het internet staan er duizenden van die wegwijzers achter elkaar.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is phishing?",
        "opties": [
            "Een bericht dat zich voordoet als iemand die je vertrouwt",
            "Een programma dat je toetsaanslagen stiekem meeschrijft",
            "Een aanval waarbij een site met verkeer wordt platgelegd",
            "Een fout in een programma waardoor gegevens uitlekken",
        ],
        "antwoord": 0,
        "uitleg": "Het mikt niet op je computer maar op jou: haast, schrik of een buitenkansje moeten je op een link doen klikken. Vandaar de vuistregel dat een bank, een postbedrijf of een overheid nooit via een link om je wachtwoord of je kaartlezer vraagt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom is een code uit een app of per sms zo'n goede extra beveiliging?",
        "opties": [
            "Wie je wachtwoord steelt, heeft je telefoon daarmee nog niet",
            "Zo'n code is veel langer en dus veel moeilijker te raden",
            "De code wordt versleuteld verstuurd en je wachtwoord niet",
            "Je hoeft je wachtwoord daardoor niet meer te onthouden",
        ],
        "antwoord": 0,
        "uitleg": "Dat heet tweestapsverificatie: iets wat je wéét plus iets wat je hébt. Een dief aan de andere kant van de wereld kan het eerste stelen maar niet het tweede. Het is de enige maatregel die een gelekt wachtwoord nog kan opvangen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Met versiebeheer kun je terug naar élke bewaarde versie van een programma.",
        "antwoord": True,
        "uitleg": "Een systeem als Git houdt elke wijziging apart bij, met wie ze maakte en waarom, jaren aan een stuk. Je ziet dus precies wanneer een fout binnengeslopen is en kunt terug naar de dag ervoor. Ook dit oefenplatform wordt zo bijgehouden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een test in een programma eigenlijk?",
        "opties": [
            "Een stukje code dat controleert of een ander stukje nog klopt",
            "Een proefversie van het programma die je aan gebruikers geeft",
            "Een meting van hoe snel het programma kan draaien",
            "Een lijst van alle fouten die er ooit in gevonden zijn",
        ],
        "antwoord": 0,
        "uitleg": "Je legt vast: geef ik dit erin, dan moet dát eruit komen. Verander je later iets, dan lopen alle tests opnieuw en zie je meteen wat er stukgaat. Zonder tests merk je zoiets pas als een gebruiker het vindt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe kan een computer een emoji, Chinese tekens en het Griekse alfabet allemaal tegelijk aan?",
        "opties": [
            "Met Unicode, dat aan elk teken ter wereld een eigen nummer geeft",
            "Met een aparte lettertypefabriek voor elke taal op aarde",
            "Door de tekens als kleine afbeeldingen mee te sturen",
            "Door elk teken om te zetten naar het dichtstbijzijnde Latijnse",
        ],
        "antwoord": 0,
        "uitleg": "De oude ASCII-tabel had maar 128 plaatsen: genoeg voor Engels, niet voor de wereld. Unicode telt er intussen meer dan 150 000, van het Egyptische hiërogliefenschrift tot een avocado. Daarom kun je in één bericht Nederlands, Arabisch en een smiley mengen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe merkt een computer dat er onderweg een bitje omgeklapt is?",
        "opties": [
            "Er wordt een controlegetal meegestuurd dat dan niet meer klopt",
            "De ontvanger vraagt altijd alles twee keer op en vergelijkt",
            "Een omgeklapt bitje maakt het bestand meteen onleesbaar",
            "De verzender stuurt elk bericht een tweede keer, voor de zekerheid",
        ],
        "antwoord": 0,
        "uitleg": "Zo'n controlegetal wordt uit de gegevens zelf berekend. Klopt het aan de andere kant niet, dan is er onderweg iets misgegaan en wordt het stuk opnieuw gevraagd. Bij een QR-code of een cd gaat het nog verder: daar kan de fout zelfs hersteld worden zonder iets opnieuw te vragen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat kan een qubit in een kwantumcomputer dat een gewone bit niet kan?",
        "opties": [
            "In een mengeling van 0 en 1 tegelijk zitten tot je hem afleest",
            "Veel meer dan twee vaste waarden bewaren, bijvoorbeeld 0 tot 9",
            "Zijn waarde onthouden ook als de stroom volledig wegvalt",
            "Zichzelf herstellen zodra er een rekenfout in geslopen is",
        ],
        "antwoord": 0,
        "uitleg": "Daardoor kan zo'n machine heel veel mogelijkheden tegelijk doorrekenen. Dat maakt hem niet zomaar sneller in alles: alleen voor bepaalde problemen, zoals grote getallen ontbinden, is hij in theorie veel sterker. Precies daarom denkt men nu al na over nieuwe versleuteling.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je routeplanner zoekt de snelste weg tussen twee steden. Hoe doet hij dat?",
        "opties": [
            "Hij waaiert uit vanaf het vertrek en houdt per kruispunt de beste tijd bij",
            "Hij probeert alle mogelijke routes en kiest achteraf de kortste",
            "Hij trekt een rechte lijn en zoekt de wegen die daar het dichtst bij liggen",
            "Hij volgt altijd de weg met de hoogste toegelaten snelheid",
        ],
        "antwoord": 0,
        "uitleg": "Dat idee komt van Edsger Dijkstra, een Nederlander, die het in 1956 in twintig minuten bedacht op een terrasje. Alle routes uitproberen zou onbegonnen werk zijn: tussen twee steden liggen er astronomisch veel.",
    },
]
