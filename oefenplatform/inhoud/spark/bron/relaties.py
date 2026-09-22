# -*- coding: utf-8 -*-
"""De vragen voor "Relaties en verandering" (✨ Spark, wiskunde).

De vakfiche zet hieronder vier dingen: coördinaten in een assenstelsel, het
rekenen met letters (eentermen, veeltermen, getalwaarde, de merkwaardige
producten), recht en omgekeerd evenredige verbanden in een formule, tabel of
grafiek, en vergelijkingen van de eerste graad met één onbekende.

Patronen horen er ook bij: regelmaat ontdekken en die in een formule zetten.

Deel 1 blijft bij één stap tegelijk. Deel 2 vraagt haakjes wegwerken, de
merkwaardige producten, omgekeerd evenredige verbanden en vraagstukken waar je
eerst zelf de vergelijking moet opstellen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="In een assenstelsel geeft een punt (3, 5) aan. Wat betekent de 3?",
        opties=[
            "Drie stappen langs de horizontale as",
            "Drie stappen omhoog",
            "Dat het punt drie keer voorkomt",
        ],
        antwoord=0,
        uitleg="Het eerste getal is de x-coördinaat en hoort bij de horizontale as. Het tweede is de y-coördinaat. Altijd in die volgorde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke coördinaten heeft de oorsprong?",
        opties=["(0, 0)", "(1, 1)", "(0, 1)"],
        antwoord=0,
        uitleg="De oorsprong is het punt waar de x-as en de y-as elkaar snijden, dus (0, 0).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een punt ligt op de x-as. Wat weet je over zijn y-coördinaat?",
        opties=["Die is 0", "Die is 1", "Die is even groot als de x-coördinaat"],
        antwoord=0,
        uitleg="Op de x-as ga je niet omhoog of omlaag, dus y = 0. Een punt op de y-as heeft net zo x = 0.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken de getalwaarde van 3x als x = 4.",
        antwoord="12",
        uitleg="3x betekent 3 × x, dus 3 × 4 = 12.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bereken de getalwaarde van 2a + 5 als a = 6.",
        opties=["17", "13", "22"],
        antwoord=0,
        uitleg="2 × 6 = 12, en 12 + 5 = 17. Eerst vermenigvuldigen, dan optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de eenterm 5x³, welk getal is de coëfficiënt?",
        opties=["5", "3", "x"],
        antwoord=0,
        uitleg="De coëfficiënt is het getal vooraan: 5. Het lettergedeelte is x³, en de graad van deze eenterm is 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee eentermen zijn gelijksoortig?",
        opties=["3x en 7x", "3x en 3x²", "3x en 3y"],
        antwoord=0,
        uitleg="Gelijksoortig betekent hetzelfde lettergedeelte. Alleen dan mag je optellen: 3x + 7x = 10x. Bij 3x en 3x² kan dat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Herleid: 4a + 3a − a",
        opties=["6a", "7a", "8a"],
        antwoord=0,
        uitleg="Alle drie zijn gelijksoortig, dus tel de coëfficiënten op: 4 + 3 − 1 = 6, dus 6a.",
    ),
    dict(
        type="meerkeuze",
        vraag="Werk de haakjes weg: 3(x + 2)",
        opties=["3x + 6", "3x + 2", "x + 6"],
        antwoord=0,
        uitleg="Distributief: de 3 gaat over allebei de termen. 3 × x = 3x en 3 × 2 = 6.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: x + 7 = 12. Wat is x?",
        antwoord="5",
        uitleg="Trek aan beide kanten 7 af: x = 12 − 7 = 5.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: 3x = 21. Wat is x?",
        antwoord="7",
        uitleg="Deel aan beide kanten door 3: x = 21 : 3 = 7.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: 2x + 5 = 17",
        opties=["x = 6", "x = 11", "x = 8"],
        antwoord=0,
        uitleg="Eerst de 5 eraf: 2x = 12. Dan delen door 2: x = 6. Controleer: 2 × 6 + 5 = 17.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: x − 4 = −9",
        opties=["x = −5", "x = −13", "x = 5"],
        antwoord=0,
        uitleg="Tel aan beide kanten 4 op: x = −9 + 4 = −5. Controleer: −5 − 4 = −9.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je het deel links van het gelijkheidsteken?",
        opties=["Het linkerlid", "De onbekende", "De oplossing"],
        antwoord=0,
        uitleg="Linkerlid en rechterlid, met het gelijkheidsteken ertussen. De onbekende is de letter, de oplossing is de waarde die klopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie broden kosten € 7,50. Wat kosten er vijf?",
        opties=["€ 12,50", "€ 15", "€ 10"],
        antwoord=0,
        uitleg="Recht evenredig: ga naar één brood, 7,50 : 3 = € 2,50. Dan 5 × 2,50 = € 12,50.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee grootheden zijn recht evenredig. Wat gebeurt er als je de ene verdubbelt?",
        opties=["De andere verdubbelt ook", "De andere halveert", "De andere blijft gelijk"],
        antwoord=0,
        uitleg="Bij een recht evenredig verband groeien ze samen mee. Het quotiënt van de twee blijft altijd hetzelfde; dat getal heet de evenredigheidsfactor.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de tabel hoort bij 2 het getal 6, bij 4 het getal 12 en bij 5 het getal 15. Welke formule past?",
        opties=["y = 3x", "y = x + 4", "y = 2x"],
        antwoord=0,
        uitleg="Elk tweede getal is drie keer het eerste: 6 : 2 = 3, 12 : 4 = 3, 15 : 5 = 3. De evenredigheidsfactor is dus 3.",
    ),
    dict(
        type="waarofniet",
        vraag="De grafiek van een recht evenredig verband is een rechte lijn door de oorsprong.",
        antwoord=True,
        uitleg="Juist. Bij nul van het ene hoort nul van het andere, dus de lijn vertrekt in (0, 0).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rij begint met 3, 7, 11, 15, … Welk getal komt er daarna?",
        opties=["19", "18", "20"],
        antwoord=0,
        uitleg="Er komt telkens 4 bij: 15 + 4 = 19.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft het aantal poten bij k koeien?",
        opties=["4k", "k + 4", "k : 4"],
        antwoord=0,
        uitleg="Elke koe heeft vier poten, dus 4 × k. Een formule opstellen begint met de vraag: wat gebeurt er per stuk?",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Werk uit: (a + b)²",
        opties=["a² + 2ab + b²", "a² + b²", "a² + ab + b²"],
        antwoord=0,
        uitleg="Het merkwaardig product: (a + b)² = a² + 2ab + b². De middelste term wordt het vaakst vergeten. Controleer met a = 2 en b = 3: (2 + 3)² = 25, en 4 + 12 + 9 = 25.",
    ),
    dict(
        type="meerkeuze",
        vraag="Werk uit: (a + b)(a − b)",
        opties=["a² − b²", "a² + b²", "a² − 2ab + b²"],
        antwoord=0,
        uitleg="De middelste termen vallen weg: −ab + ab = 0. Blijft over a² − b². Met a = 5 en b = 2: 7 × 3 = 21, en 25 − 4 = 21.",
    ),
    dict(
        type="meerkeuze",
        vraag="Werk uit: (x + 4)²",
        opties=["x² + 8x + 16", "x² + 16", "x² + 4x + 16"],
        antwoord=0,
        uitleg="Volgens (a + b)²: x² + 2 × x × 4 + 4² = x² + 8x + 16.",
    ),
    dict(
        type="meerkeuze",
        vraag="Werk uit: 2(3x − 5) + 4x",
        opties=["10x − 10", "6x − 10", "10x − 5"],
        antwoord=0,
        uitleg="Eerst de haakjes: 6x − 10. Dan 4x erbij: 6x + 4x = 10x, dus 10x − 10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de graad van de veelterm 3x² + 5x − 7?",
        opties=["2", "3", "1"],
        antwoord=0,
        uitleg="De graad van een veelterm is de hoogste exponent die erin voorkomt, hier 2.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bereken de getalwaarde van x² − 3x als x = 5.",
        opties=["10", "−10", "40"],
        antwoord=0,
        uitleg="25 − 15 = 10. Eerst machtsverheffen, dan vermenigvuldigen, dan aftrekken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bereken de getalwaarde van 2a − b als a = 3 en b = −4.",
        opties=["10", "2", "−10"],
        antwoord=0,
        uitleg="2 × 3 = 6, en dan min −4, wat hetzelfde is als plus 4: 6 + 4 = 10. Let op de twee mintekens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: 5x − 3 = 2x + 9",
        opties=["x = 4", "x = 2", "x = 12"],
        antwoord=0,
        uitleg="Haal de x'en naar één kant: 5x − 2x = 9 + 3, dus 3x = 12 en x = 4. Controleer: 5 × 4 − 3 = 17 en 2 × 4 + 9 = 17.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: 3(x − 2) = 15",
        opties=["x = 7", "x = 5", "x = 3"],
        antwoord=0,
        uitleg="Deel eerst door 3: x − 2 = 5, dus x = 7. Of werk de haakjes weg: 3x − 6 = 15.",
    ),
    dict(
        type="meerkeuze",
        vraag="Los op: x : 4 = 3",
        opties=["x = 12", "x = 0,75", "x = 7"],
        antwoord=0,
        uitleg="Vermenigvuldig aan beide kanten met 4: x = 12. Delen en vermenigvuldigen zijn elkaars omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Ik denk aan een getal. Het dubbele ervan plus 3 is 21. Welke vergelijking hoort daarbij?",
        opties=["2x + 3 = 21", "2(x + 3) = 21", "x + 3 = 21"],
        antwoord=0,
        uitleg="Het dubbele is 2x, en daar komt 3 bij. De oplossing is dan x = 9.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een taxi vraagt € 3 opstapgeld en € 2 per kilometer. Je betaalt € 19. Hoeveel kilometer reed je?",
        opties=["8 km", "9,5 km", "11 km"],
        antwoord=0,
        uitleg="De vergelijking is 3 + 2x = 19, dus 2x = 16 en x = 8 kilometer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zes werklui doen een klus in 4 dagen. Hoe lang doen twaalf werklui erover?",
        opties=["2 dagen", "8 dagen", "6 dagen"],
        antwoord=0,
        uitleg="Omgekeerd evenredig: dubbel zoveel mensen, half zo lang. Het product blijft gelijk: 6 × 4 = 24 en 12 × 2 = 24.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een omgekeerd evenredig verband in een tabel?",
        opties=[
            "Het product van de twee getallen is telkens hetzelfde",
            "Het quotiënt is telkens hetzelfde",
            "Het verschil is telkens hetzelfde",
        ],
        antwoord=0,
        uitleg="Bij omgekeerd evenredig blijft het product gelijk; bij recht evenredig blijft het quotiënt gelijk. Dat is meteen de manier om ze uit elkaar te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule hoort bij een omgekeerd evenredig verband met factor 24?",
        opties=["y = 24 : x", "y = 24x", "y = x + 24"],
        antwoord=0,
        uitleg="Omgekeerd evenredig betekent x × y = 24, dus y = 24 : x. Recht evenredig zou y = 24x zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met lucifers leg je vierkantjes op een rij: 1 vierkant kost 4 lucifers, 2 kosten er 7, 3 kosten er 10. Hoeveel voor n vierkantjes?",
        opties=["3n + 1", "4n", "3n"],
        antwoord=0,
        uitleg="Het eerste vierkant kost 4, elk volgend maar 3 extra omdat ze een zijde delen. Dus 3n + 1. Controleer bij n = 3: 3 × 3 + 1 = 10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rij begint met 2, 4, 8, 16, … Welk getal komt er daarna?",
        opties=["32", "24", "20"],
        antwoord=0,
        uitleg="Elk getal is het dubbele van het vorige: 16 × 2 = 32. Hier komt er niet telkens evenveel bij, dus is het geen recht evenredig verband.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee vergelijkingen die dezelfde oplossing hebben, heten gelijkwaardig.",
        antwoord=True,
        uitleg="Juist. Bij elke stap die je zet, maak je een gelijkwaardige vergelijking: eentje die er anders uitziet maar dezelfde oplossing heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij het oplossen van 4x = 20 deelt iemand enkel links door 4 en schrijft x = 20. Wat is er mis?",
        opties=[
            "Wat je links doet, moet je ook rechts doen",
            "Je mag niet delen bij een vergelijking",
            "Niets, het klopt",
        ],
        antwoord=0,
        uitleg="Een vergelijking is een evenwicht. Deel je maar één kant, dan klopt de gelijkheid niet meer. Juist is x = 20 : 4 = 5.",
    ),
    dict(
        type="meerkeuze",
        vraag="De omtrek van een rechthoek is 26 cm en de lengte is 8 cm. Welke vergelijking gebruik je voor de breedte b?",
        opties=["2(8 + b) = 26", "8 × b = 26", "8 + b = 26"],
        antwoord=0,
        uitleg="De omtrek is 2 × (lengte + breedte). Oplossen geeft 8 + b = 13, dus b = 5 cm.",
    ),
]
