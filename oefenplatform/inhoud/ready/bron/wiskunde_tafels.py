# -*- coding: utf-8 -*-
"""Ready (3de en 4de leerjaar), wiskunde, proefhoofdstuk "Tafels en delen".

Officieel doel einde 4de leerjaar (brochure Minimumdoelen en visieteksten
... 4de en 6de jaar lager onderwijs, Vlaamse overheid, stand 25/11/2026):
tafels van vermenigvuldiging tot 10 paraat, delen met en zonder rest,
delers en veelvouden, deelbaar door 2, 5, 10, 100 en 1000.

Gewone cijfers, geen formules: kinderen van 8 en 9 lezen dat makkelijker.
Bouwen en nakijken: python3 bouw.py wiskunde_tafels
"""

TITEL = "Tafels en delen"

UITLEG_1 = 'Vermenigvuldigen is groepjes maken: 4 × 3 is 4 groepjes van 3, samen 12. Wisselen mag: 3 × 4 is ook 12. Trucjes: × 1 blijft hetzelfde, × 0 is 0, × 10 zet een nul achter het getal.'

UITLEG_2 = 'Delen is eerlijk verdelen: 12 : 3 = 4, want 4 × 3 = 12. Gaat het niet precies, dan is er een rest: 14 : 4 = 3 rest 2. Deelbaar door 2: het getal eindigt op 0, 2, 4, 6 of 8.'

DEEL_1 = [
    dict(type="meerkeuze", vraag="Hoeveel is 7 × 8?", opties=["54", "56", "48", "64"], antwoord=1, reken=56,
         uitleg="7 × 8 = 56. Een ezelsbruggetje: 5, 6, 7, 8, want 56 = 7 × 8."),
    dict(type="invultekst", vraag="6 × 9 = ___", antwoord="54", reken=54,
         uitleg="6 × 10 = 60. Eén groepje van 6 minder: 60 − 6 = 54."),
    dict(type="meerkeuze", vraag="Welke som hoort bij 4 groepjes van 3 appels?", opties=["3 + 4", "4 × 3", "4 + 4 + 4 + 4", "3 × 3"], antwoord=1,
         uitleg="4 groepjes van 3 is 3 + 3 + 3 + 3, en dat schrijf je korter als 4 × 3 = 12."),
    dict(type="waarofniet", vraag="3 × 8 is evenveel als 8 × 3.", antwoord=True,
         uitleg="Bij vermenigvuldigen mag je de getallen wisselen. Allebei geven ze 24."),
    dict(type="invultekst", vraag="9 × 10 = ___", antwoord="90", reken=90,
         uitleg="Maal 10 zet een nul achter het getal: 9 wordt 90."),
    dict(type="meerkeuze", vraag="Welk getal staat niet in de tafel van 4?", opties=["16", "28", "30", "36"], antwoord=2,
         uitleg="De tafel van 4 is 4, 8, 12, 16, 20, 24, 28, 32, 36, 40. Het getal 30 zit daar niet tussen."),
    dict(type="waarofniet", vraag="Elke uitkomst van de tafel van 5 eindigt op een 5.", antwoord=False,
         uitleg="De helft eindigt op 0: 10, 20, 30, 40 en 50. De andere helft eindigt op 5."),
    dict(type="invultekst", vraag="Een spin heeft 8 poten. Hoeveel poten hebben 6 spinnen samen?", antwoord="48", reken=48,
         uitleg="6 spinnen met elk 8 poten: 6 × 8 = 48."),
    dict(type="meerkeuze", vraag="Hoeveel is 0 × 9?", opties=["9", "0", "1", "90"], antwoord=1, reken=0,
         uitleg="0 groepjes van 9 is niets. Een getal maal 0 is altijd 0."),
    dict(type="waarofniet", vraag="De uitkomsten van de tafel van 2 zijn altijd even getallen.", antwoord=True,
         uitleg="2, 4, 6, 8, 10, ... Iets dat je in twee gelijke delen kan verdelen, is even."),
    dict(type="meerkeuze", vraag="Welke vermenigvuldiging geeft 36?", opties=["4 × 8", "5 × 7", "6 × 6", "3 × 11"], antwoord=2,
         uitleg="6 × 6 = 36. Ook 4 × 9 geeft 36, maar die staat er niet bij."),
    dict(type="invultekst", vraag="7 × ___ = 63", antwoord="9", reken=9,
         uitleg="Zoek in de tafel van 7: 7, 14, 21, 28, 35, 42, 49, 56, 63. Dat is de 9de: 7 × 9 = 63."),
    dict(type="meerkeuze", vraag="In een doos eieren zitten 2 rijen van 6 eieren. Hoeveel eieren zitten in 3 dozen?",
         opties=["12", "36", "18", "30"], antwoord=1, reken=36,
         uitleg="Eén doos: 2 × 6 = 12 eieren. Drie dozen: 3 × 12 = 36 eieren."),
    dict(type="waarofniet", vraag="De tafel van 10 krijg je door een nul achter het getal te zetten.", antwoord=True,
         uitleg="4 × 10 = 40, 7 × 10 = 70. Er komt telkens een nul achter."),
    dict(type="invultekst", vraag="1 × 57 = ___", antwoord="57", reken=57,
         uitleg="Eén groepje van 57 is gewoon 57. Een getal maal 1 blijft hetzelfde."),
    dict(type="meerkeuze", vraag="Lena koopt 5 stripboeken van 7 euro. Hoeveel betaalt ze?",
         opties=["30 euro", "12 euro", "35 euro", "57 euro"], antwoord=2, reken=35,
         uitleg="5 boeken van 7 euro: 5 × 7 = 35 euro."),
    dict(type="waarofniet", vraag="6 × 8 = 46", antwoord=False,
         uitleg="6 × 8 = 48. Reken na: 5 × 8 = 40, en nog één keer 8 erbij is 48."),
    dict(type="meerkeuze", vraag="Welk rijtje is het begin van de tafel van 3?",
         opties=["3, 5, 7, 9", "3, 6, 10, 13", "3, 9, 27, 81", "3, 6, 9, 12"], antwoord=3,
         uitleg="In de tafel van 3 komt er telkens 3 bij: 3, 6, 9, 12, 15, ..."),
    dict(type="waarofniet", vraag="Als je een getal met 1 vermenigvuldigt, wordt het groter.", antwoord=False,
         uitleg="Een getal maal 1 blijft precies hetzelfde: 8 × 1 = 8."),
    dict(type="invultekst", vraag="4 × 6 = 24. Hoeveel is dan 8 × 6?", antwoord="48", reken=48,
         uitleg="8 is het dubbele van 4. Dan is de uitkomst ook het dubbele: 24 + 24 = 48."),
]

DEEL_2 = [
    dict(type="meerkeuze", vraag="Hoeveel is 42 : 6?", opties=["6", "7", "8", "36"], antwoord=1, reken=7,
         uitleg="42 : 6 = 7, want 7 × 6 = 42."),
    dict(type="invultekst", vraag="56 : 8 = ___", antwoord="7", reken=7,
         uitleg="Zoek in de tafel van 8 welk getal 56 geeft: 7 × 8 = 56."),
    dict(type="meerkeuze", vraag="Je verdeelt 18 snoepjes eerlijk over 3 kinderen. Hoeveel krijgt elk kind?",
         opties=["9", "15", "6", "21"], antwoord=2, reken=6,
         uitleg="18 : 3 = 6, want 6 × 3 = 18."),
    dict(type="waarofniet", vraag="35 : 5 = 7, want 7 × 5 = 35.", antwoord=True,
         uitleg="Bij elke deling hoort een vermenigvuldiging. Zo kan je een deling altijd nakijken."),
    dict(type="meerkeuze", vraag="Hoeveel is 23 : 5?", opties=["4 rest 3", "5 rest 2", "4 rest 2", "3 rest 8"], antwoord=0,
         uitleg="4 × 5 = 20 past erin. Van 20 tot 23 blijft er 3 over: 4 rest 3."),
    dict(type="invultekst", vraag="Hoeveel is de rest bij 30 : 7?", antwoord="2", reken=2,
         uitleg="4 × 7 = 28 past erin. 30 − 28 = 2, dus de rest is 2."),
    dict(type="waarofniet", vraag="Als je deelt door 4, kan de rest 5 zijn.", antwoord=False,
         uitleg="De rest is altijd kleiner dan het getal waardoor je deelt. Is de rest 4 of meer, dan past er nog een groepje van 4 bij."),
    dict(type="meerkeuze", vraag="26 kinderen gaan op uitstap. In een auto passen 4 kinderen. Hoeveel auto's zijn er nodig?",
         opties=["6", "7", "5", "8"], antwoord=1, reken=7,
         uitleg="26 : 4 = 6 rest 2. Ook die 2 kinderen moeten mee, dus je hebt een 7de auto nodig."),
    dict(type="meerkeuze", vraag="Welk getal is een deler van 24?", opties=["5", "7", "9", "8"], antwoord=3, reken=8,
         uitleg="8 past precies in 24: 3 × 8 = 24. De andere getallen laten een rest over."),
    dict(type="invultekst", vraag="Wat is het kleinste veelvoud van 7 dat groter is dan 30?", antwoord="35", reken=35,
         uitleg="De veelvouden van 7 zijn 7, 14, 21, 28, 35, ... Het eerste na 30 is 35."),
    dict(type="waarofniet", vraag="1 is een deler van elk getal.", antwoord=True,
         uitleg="Elk getal kan je delen door 1 zonder rest: 9 : 1 = 9."),
    dict(type="sorteren", vraag="Is het getal deelbaar door 2 of niet?",
         opties=["34", "51", "70", "19", "106", "87"],
         antwoord={"juist": [0, 1, 0, 1, 0, 1], "kolommen": ["deelbaar door 2", "niet deelbaar door 2"]},
         uitleg="Een getal is deelbaar door 2 als het eindigt op 0, 2, 4, 6 of 8. Dus 34, 70 en 106 wel, en 51, 19 en 87 niet."),
    dict(type="meerkeuze", vraag="Welk getal is deelbaar door 5?", opties=["52", "75", "98", "101"], antwoord=1, reken=75,
         uitleg="Een getal is deelbaar door 5 als het eindigt op 0 of 5. Alleen 75 doet dat."),
    dict(type="waarofniet", vraag="Een getal dat op 0 eindigt, is deelbaar door 10.", antwoord=True,
         uitleg="70 : 10 = 7, 430 : 10 = 43. Eindigt een getal op 0, dan gaat de deling door 10 precies op."),
    dict(type="meerkeuze", vraag="Welk getal is deelbaar door 100?", opties=["1 050", "2 010", "7 005", "3 400"], antwoord=3, reken=3400,
         uitleg="Een getal is deelbaar door 100 als het eindigt op 00. Alleen 3 400 doet dat."),
    dict(type="waarofniet", vraag="4 500 is deelbaar door 1 000.", antwoord=False,
         uitleg="Deelbaar door 1 000 betekent eindigen op 000. 4 500 eindigt op 500: 4 000 past erin, maar er blijft 500 over."),
    dict(type="invultekst", vraag="___ : 9 = 8", antwoord="72", reken=72,
         uitleg="Gebruik de vermenigvuldiging: 8 × 9 = 72. Dus 72 : 9 = 8."),
    dict(type="meerkeuze", vraag="Welk rijtje bevat alle delers van 12?",
         opties=["2, 4, 6, 8, 10, 12", "1, 2, 3, 4, 12", "1, 2, 3, 4, 6, 12", "12, 24, 36, 48"], antwoord=2,
         uitleg="12 kan je precies delen door 1, 2, 3, 4, 6 en 12. Het laatste rijtje zijn veelvouden van 12, geen delers."),
    dict(type="waarofniet", vraag="Elk veelvoud van 2 is ook een veelvoud van 4.", antwoord=False,
         uitleg="6 is een veelvoud van 2, maar niet van 4. Omgekeerd klopt het wel: elk veelvoud van 4 is ook een veelvoud van 2."),
    dict(type="meerkeuze", vraag="Mama knipt 40 cm lint in stukken van 6 cm. Hoeveel stukken krijgt ze, en hoeveel lint blijft over?",
         opties=["6 stukken, 4 cm over", "7 stukken, 2 cm over", "6 stukken, 2 cm over", "5 stukken, 10 cm over"], antwoord=0,
         uitleg="40 : 6 = 6 rest 4, want 6 × 6 = 36 en 40 − 36 = 4."),
]
