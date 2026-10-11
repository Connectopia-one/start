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
        "vraag": r"Na \(20\,\%\) korting betaal je \(48\) euro voor een jas. Wat was de prijs voor de korting?",
        "opties": [r"\(60\) euro", r"\(57{,}60\) euro", r"\(58\) euro", r"\(68\) euro"],
        "antwoord": 0,
        "reken": "48 / 0.8",
        "uitleg": r"Je betaalt \(80\,\%\) van de oude prijs. Dus \(48 : 0{,}8 = 60\) euro. Reken maar na: \(20\,\%\) van \(60\) is \(12\), en \(60 - 12 = 48\).",
    },
    {
        "type": "invultekst",
        "vraag": r"Een prijs stijgt met \(10\,\%\) en daalt daarna met \(10\,\%\). Hoeveel procent van de oorspronkelijke prijs betaal je dan? Antwoord met een getal.",
        "antwoord": "99",
        "reken": "1.1 * 0.9 * 100",
        "uitleg": r"Eerst \(110\,\%\), dan daarvan \(90\,\%\): \(1{,}1 \times 0{,}9 = 0{,}99\), dus \(99\,\%\). De daling rekent op het hogere bedrag, dus je komt iets lager uit dan je begon.",
    },
    {
        "type": "waarofniet",
        "vraag": r"Een stijging met \(10\,\%\) gevolgd door een daling met \(10\,\%\) brengt je precies terug bij de oorspronkelijke prijs.",
        "antwoord": False,
        "uitleg": r"Niet waar. Je eindigt op \(99\,\%\) van het begin. Procenten rekenen telkens op het bedrag van dát moment, en dat is na de stijging groter geworden.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Hoeveel is \((-3)^{2} - 3^{2}\)?",
        "opties": [r"\(0\)", r"\(18\)", r"\(-18\)", r"\(6\)"],
        "antwoord": 0,
        "reken": "(-3) ** 2 - 3 ** 2",
        "uitleg": r"\((-3)^{2} = -3x -3 = 9\) en \(3^{2} = 9\). Dus \(9 - 9 = 0\). Let op de haakjes: zonder haakjes zou \(-3^{2}\) gelijk zijn aan \(-9\).",
    },
    {
        "type": "invultekst",
        "vraag": r"Hoeveel is \(\sqrt{144} - \sqrt{81}\)?",
        "antwoord": "3",
        "reken": "144 ** 0.5 - 81 ** 0.5",
        "uitleg": r"\(\sqrt{144} = 12\) en \(\sqrt{81} = 9\), dus \(12 - 9 = 3\). Je mag de wortels niet eerst aftrekken: \(\sqrt{144 - 81}\) zou \(\sqrt{63}\) zijn, en dat is heel iets anders.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Neem de uitspraak: als een getal deelbaar is door \(6\), dan is het deelbaar door \(3\). Wat gebeurt er als je ze omdraait?",
        "opties": [
            r"Dan krijg je: deelbaar door \(3\), dus door \(6\). En dat klopt niet",
            "Dan krijg je dezelfde uitspraak, want omdraaien verandert niets",
            "Dan krijg je een uitspraak die ook altijd juist blijft gelden",
            "Dan krijg je een uitspraak die enkel voor oneven getallen geldt",
        ],
        "antwoord": 0,
        "uitleg": r"\(9\) is deelbaar door \(3\) maar niet door \(6\). Eén zo'n tegenvoorbeeld volstaat. Een uitspraak omdraaien mag alleen als er een dubbele pijl ⇔ staat.",
    },
    {
        "type": "waarofniet",
        "vraag": "Eén tegenvoorbeeld volstaat om een uitspraak die met 'alle' begint, te weerleggen.",
        "antwoord": True,
        "uitleg": r"Waar. 'Alle priemgetallen zijn oneven' sneuvelt op het getal \(2\). Om zo'n uitspraak te bewíjzen heb je daarentegen een redenering nodig, geen voorbeelden.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In een gelijkbenige driehoek is de tophoek \(40\) graden. Hoe groot is elk van de twee basishoeken?",
        "opties": [r"\(70\) graden", r"\(40\) graden", r"\(50\) graden", r"\(80\) graden"],
        "antwoord": 0,
        "reken": "(180 - 40) / 2",
        "uitleg": r"De drie hoeken zijn samen \(180\) graden, dus blijft er \(140\) over voor de twee basishoeken. Die zijn even groot: \(140 : 2 = 70\).",
    },
    {
        "type": "invultekst",
        "vraag": r"Een vierkant heeft een omtrek van \(36\) cm. Hoeveel \(\text{cm}^{2}\) is zijn oppervlakte?",
        "antwoord": "81",
        "reken": "(36 / 4) ** 2",
        "uitleg": r"Een vierkant heeft vier gelijke zijden: \(36 : 4 = 9\) cm. De oppervlakte is \(9 \times 9 = 81\,\text{cm}^{2}\).",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Hoeveel is \(3\,\text{m}^{2}\) in \(\text{cm}^{2}\)?",
        "opties": [r"\(30\,000\,\text{cm}^{2}\)", r"\(300\,\text{cm}^{2}\)", r"\(3\,000\,\text{cm}^{2}\)", r"\(300\,000\,\text{cm}^{2}\)"],
        "antwoord": 0,
        "uitleg": r"Bij oppervlaktematen zet je twee stappen per trede: \(1\,\text{m}^{2} = 100\,\text{dm}^{2} = 10\,000\,\text{cm}^{2}\). Dus \(3\,\text{m}^{2} = 30\,000\,\text{cm}^{2}\).",
    },
    {
        "type": "waarofniet",
        "vraag": "Als je elke ribbe van een kubus verdubbelt, wordt het volume acht keer zo groot.",
        "antwoord": True,
        "uitleg": r"Waar. Een kubus van \(2\) cm heeft \(8\,\text{cm}^{3}\), een van \(4\) cm heeft \(64\,\text{cm}^{3}\). Je verdubbelt in drie richtingen, dus \(2 \times 2 \times 2 = 8\) keer.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Een rij begint met \(3\), \(7\), \(11\), \(15\), … Welk getal staat op de twintigste plaats?",
        "opties": [r"\(79\)", r"\(83\)", r"\(80\)", r"\(75\)"],
        "antwoord": 0,
        "reken": "3 + 19 * 4",
        "uitleg": r"Elke stap is +\(4\). Van de eerste naar de twintigste plaats zet je negentien stappen: \(3 + 19 \times 4 = 79\). Let op: negentien stappen, niet twintig.",
    },
    {
        "type": "invultekst",
        "vraag": r"Los op: \(3x - 5 = 16\). Wat is x?",
        "antwoord": "7",
        "reken": "(16 + 5) / 3",
        "uitleg": r"Doe eerst +\(5\) aan beide kanten: \(3x = 21\). Deel dan door \(3\): \(x = 7\).",
    },
    {
        "type": "meerkeuze",
        "vraag": "Vier even snelle schilders doen zes dagen over een huis. Hoe lang doen zes van die schilders erover?",
        "opties": [r"\(4\) dagen", r"\(9\) dagen", r"\(3\) dagen", r"\(5\) dagen"],
        "antwoord": 0,
        "reken": "4 * 6 / 6",
        "uitleg": r"Het werk is \(4 \times 6 = 24\) mandagen. Met zes schilders: \(24 : 6 = 4\) dagen. Meer schilders betekent minder dagen, niet meer.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het aantal schilders en het aantal dagen dat ze nodig hebben, zijn recht evenredig.",
        "antwoord": False,
        "uitleg": "Niet waar, ze zijn omgekeerd evenredig: verdubbel je het aantal schilders, dan halveert het aantal dagen. Bij recht evenredig zouden ze samen stijgen.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"Een reeks bestaat uit \(2\), \(3\), \(3\), \(4\) en \(48\). Welk kengetal geeft het eerlijkste beeld van een gewone waarde uit die reeks?",
        "opties": [
            r"De mediaan, want die ligt niet onder invloed van die ene \(48\)",
            "Het gemiddelde, want daar tellen alle waarden even zwaar mee",
            "De modus, want die waarde komt nu eenmaal het vaakst voor",
            "Het grootste getal, want dat toont wat er mogelijk is hier",
        ],
        "antwoord": 0,
        "uitleg": r"Het gemiddelde is \(12\), terwijl vier van de vijf waarden onder de \(5\) liggen. Eén uitschieter trekt een gemiddelde scheef; de mediaan \((3)\) blijft staan.",
    },
    {
        "type": "invultekst",
        "vraag": r"Een groep is \(15\,\%\) van het geheel. Hoeveel graden krijgt die groep in een cirkeldiagram?",
        "antwoord": "54",
        "reken": "0.15 * 360",
        "uitleg": r"Een volledige cirkel is \(360\) graden, en \(15\,\%\) daarvan is \(0{,}15 \times 360 = 54\) graden.",
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
        "vraag": r"Je hebt \(4\) T-shirts, \(3\) broeken en \(2\) paar schoenen. Hoeveel verschillende combinaties kan je aantrekken?",
        "opties": [r"\(24\)", r"\(9\)", r"\(12\)", r"\(18\)"],
        "antwoord": 0,
        "reken": "4 * 3 * 2",
        "uitleg": r"Bij elk van de \(4\) shirts passen \(3\) broeken, dat zijn al \(12\) combinaties, en bij elk daarvan nog \(2\) paar schoenen: \(4 \times 3 \times 2 = 24\).",
    },
]
