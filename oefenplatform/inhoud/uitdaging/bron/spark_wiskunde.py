# -*- coding: utf-8 -*-
"""Uitdaging wiskunde ✨ Spark: de negen thema's door elkaar.

Twee stappen, een omgekeerde vraag of een redenering, in plaats van één
bewerking. Geen nieuwe leerstof: alles staat op wat in de thema's al geoefend
wordt.
"""
NIVEAU = "spark"
VAK = "Wiskunde"
BESTAND = "spark-wiskunde-uitdaging.json"

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Na 20 % korting betaal je 48 euro voor een jas. Wat was de prijs voor de korting?",
        "opties": ["60 euro", "57,60 euro", "58 euro", "68 euro"],
        "antwoord": 0,
        "reken": "48 / 0.8",
        "uitleg": "Je betaalt 80 % van de oude prijs. Dus 48 : 0,8 = 60 euro. Reken maar na: 20 % van 60 is 12, en 60 - 12 = 48.",
    },
    {
        "type": "invultekst",
        "vraag": "Een prijs stijgt met 10 % en daalt daarna met 10 %. Hoeveel procent van de oorspronkelijke prijs betaal je dan? Antwoord met een getal.",
        "antwoord": "99",
        "reken": "1.1 * 0.9 * 100",
        "uitleg": "Eerst 110 %, dan daarvan 90 %: 1,1 x 0,9 = 0,99, dus 99 %. De daling rekent op het hogere bedrag, dus je komt iets lager uit dan je begon.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een stijging met 10 % gevolgd door een daling met 10 % brengt je precies terug bij de oorspronkelijke prijs.",
        "antwoord": False,
        "uitleg": "Niet waar. Je eindigt op 99 % van het begin. Procenten rekenen telkens op het bedrag van dát moment, en dat is na de stijging groter geworden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel is (−3)² − 3²?",
        "opties": ["0", "18", "−18", "6"],
        "antwoord": 0,
        "reken": "(-3) ** 2 - 3 ** 2",
        "uitleg": "(−3)² = −3 x −3 = 9 en 3² = 9. Dus 9 − 9 = 0. Let op de haakjes: zonder haakjes zou −3² gelijk zijn aan −9.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel is √144 − √81?",
        "antwoord": "3",
        "reken": "144 ** 0.5 - 81 ** 0.5",
        "uitleg": "√144 = 12 en √81 = 9, dus 12 − 9 = 3. Je mag de wortels niet eerst aftrekken: √(144−81) zou √63 zijn, en dat is heel iets anders.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Neem de uitspraak: als een getal deelbaar is door 6, dan is het deelbaar door 3. Wat gebeurt er als je ze omdraait?",
        "opties": [
            "Dan krijg je: deelbaar door 3, dus door 6. En dat klopt niet",
            "Dan krijg je dezelfde uitspraak, want omdraaien verandert niets",
            "Dan krijg je een uitspraak die ook altijd juist blijft gelden",
            "Dan krijg je een uitspraak die enkel voor oneven getallen geldt",
        ],
        "antwoord": 0,
        "uitleg": "9 is deelbaar door 3 maar niet door 6. Eén zo'n tegenvoorbeeld volstaat. Een uitspraak omdraaien mag alleen als er een dubbele pijl ⇔ staat.",
    },
    {
        "type": "waarofniet",
        "vraag": "Eén tegenvoorbeeld volstaat om een uitspraak die met 'alle' begint, te weerleggen.",
        "antwoord": True,
        "uitleg": "Waar. 'Alle priemgetallen zijn oneven' sneuvelt op het getal 2. Om zo'n uitspraak te bewíjzen heb je daarentegen een redenering nodig, geen voorbeelden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In een gelijkbenige driehoek is de tophoek 40 graden. Hoe groot is elk van de twee basishoeken?",
        "opties": ["70 graden", "40 graden", "50 graden", "80 graden"],
        "antwoord": 0,
        "reken": "(180 - 40) / 2",
        "uitleg": "De drie hoeken zijn samen 180 graden, dus blijft er 140 over voor de twee basishoeken. Die zijn even groot: 140 : 2 = 70.",
    },
    {
        "type": "invultekst",
        "vraag": "Een vierkant heeft een omtrek van 36 cm. Hoeveel cm² is zijn oppervlakte?",
        "antwoord": "81",
        "reken": "(36 / 4) ** 2",
        "uitleg": "Een vierkant heeft vier gelijke zijden: 36 : 4 = 9 cm. De oppervlakte is 9 x 9 = 81 cm².",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel is 3 m² in cm²?",
        "opties": ["30 000 cm²", "300 cm²", "3 000 cm²", "300 000 cm²"],
        "antwoord": 0,
        "uitleg": "Bij oppervlaktematen zet je twee stappen per trede: 1 m² = 100 dm² = 10 000 cm². Dus 3 m² = 30 000 cm².",
    },
    {
        "type": "waarofniet",
        "vraag": "Als je elke ribbe van een kubus verdubbelt, wordt het volume acht keer zo groot.",
        "antwoord": True,
        "uitleg": "Waar. Een kubus van 2 cm heeft 8 cm³, een van 4 cm heeft 64 cm³. Je verdubbelt in drie richtingen, dus 2 x 2 x 2 = 8 keer.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een rij begint met 3, 7, 11, 15, … Welk getal staat op de twintigste plaats?",
        "opties": ["79", "83", "80", "75"],
        "antwoord": 0,
        "reken": "3 + 19 * 4",
        "uitleg": "Elke stap is +4. Van de eerste naar de twintigste plaats zet je negentien stappen: 3 + 19 x 4 = 79. Let op: negentien stappen, niet twintig.",
    },
    {
        "type": "invultekst",
        "vraag": "Los op: 3x − 5 = 16. Wat is x?",
        "antwoord": "7",
        "reken": "(16 + 5) / 3",
        "uitleg": "Doe eerst +5 aan beide kanten: 3x = 21. Deel dan door 3: x = 7.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Vier even snelle schilders doen zes dagen over een huis. Hoe lang doen zes van die schilders erover?",
        "opties": ["4 dagen", "9 dagen", "3 dagen", "5 dagen"],
        "antwoord": 0,
        "reken": "4 * 6 / 6",
        "uitleg": "Het werk is 4 x 6 = 24 mandagen. Met zes schilders: 24 : 6 = 4 dagen. Meer schilders betekent minder dagen, niet meer.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het aantal schilders en het aantal dagen dat ze nodig hebben, zijn recht evenredig.",
        "antwoord": False,
        "uitleg": "Niet waar, ze zijn omgekeerd evenredig: verdubbel je het aantal schilders, dan halveert het aantal dagen. Bij recht evenredig zouden ze samen stijgen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een reeks bestaat uit 2, 3, 3, 4 en 48. Welk kengetal geeft het eerlijkste beeld van een gewone waarde uit die reeks?",
        "opties": [
            "De mediaan, want die ligt niet onder invloed van die ene 48",
            "Het gemiddelde, want daar tellen alle waarden even zwaar mee",
            "De modus, want die waarde komt nu eenmaal het vaakst voor",
            "Het grootste getal, want dat toont wat er mogelijk is hier",
        ],
        "antwoord": 0,
        "uitleg": "Het gemiddelde is 12, terwijl vier van de vijf waarden onder de 5 liggen. Eén uitschieter trekt een gemiddelde scheef; de mediaan (3) blijft staan.",
    },
    {
        "type": "invultekst",
        "vraag": "Een groep is 15 % van het geheel. Hoeveel graden krijgt die groep in een cirkeldiagram?",
        "antwoord": "54",
        "reken": "0.15 * 360",
        "uitleg": "Een volledige cirkel is 360 graden, en 15 % daarvan is 0,15 x 360 = 54 graden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Neem A = {1, 2, 3, 4, 5, 6}, B de veelvouden van 2 in A en C de veelvouden van 3 in A. Wat is de doorsnede van B en C?",
        "opties": ["{6}", "{2, 3, 6}", "{ }", "{2, 3, 4, 6}"],
        "antwoord": 0,
        "uitleg": "B = {2, 4, 6} en C = {3, 6}. De doorsnede is wat in allebei zit, dus enkel 6. Dat is meteen het kleinste gemene veelvoud van 2 en 3.",
    },
    {
        "type": "waarofniet",
        "vraag": "De lege verzameling is een deelverzameling van elke verzameling.",
        "antwoord": True,
        "uitleg": "Waar. Er zit geen enkel element in dat buiten de andere verzameling valt, dus aan de voorwaarde is voldaan. Dat geldt ook voor de lege verzameling zelf.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je hebt 4 T-shirts, 3 broeken en 2 paar schoenen. Hoeveel verschillende combinaties kan je aantrekken?",
        "opties": ["24", "9", "12", "18"],
        "antwoord": 0,
        "reken": "4 * 3 * 2",
        "uitleg": "Bij elk van de 4 shirts passen 3 broeken, dat zijn al 12 combinaties, en bij elk daarvan nog 2 paar schoenen: 4 x 3 x 2 = 24.",
    },
]
