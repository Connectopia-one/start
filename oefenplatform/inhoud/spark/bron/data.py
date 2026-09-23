# -*- coding: utf-8 -*-
"""De vragen voor "Data en onzekerheid" (✨ Spark, wiskunde).

De vakfiche zet hieronder: soorten variabelen (numeriek of categorisch),
frequentietabellen, staaf-, cirkel- en lijndiagram, de drie centrummaten
(gemiddelde, mediaan, modus) en één spreidingsmaat (de variatiebreedte).

De fiche vraagt ook uitdrukkelijk dat je de uitkomsten *interpreteert*: niet
enkel uitrekenen, maar zeggen wat het betekent en welke maat past. Daarom gaat
een deel van deel 2 over de keuze tussen gemiddelde en mediaan.

Deel 1 blijft bij aflezen en uitrekenen. Deel 2 vraagt omgekeerd rekenen en
oordelen over welke maat het eerlijkste beeld geeft.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je telt hoeveel broers en zussen iedereen in de klas heeft. Wat voor soort gegeven is dat?",
        opties=["Numeriek, want het is een aantal", "Categorisch", "Geen van beide"],
        antwoord=0,
        uitleg="Een numerieke variabele is een getal waarmee je kan rekenen. Een categorische variabele is een soort of groep, zoals lievelingskleur of vervoermiddel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vraagt iedereen naar zijn lievelingskleur. Wat voor soort variabele is dat?",
        opties=["Categorisch", "Numeriek", "Allebei"],
        antwoord=0,
        uitleg="Kleuren zijn groepen, geen getallen. Je kan ze tellen, maar er geen gemiddelde van nemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je in een frequentietabel?",
        opties=[
            "Hoe vaak elke waarde voorkomt",
            "Het gemiddelde van alle waarden",
            "De grootste waarde",
        ],
        antwoord=0,
        uitleg="De frequentie is het aantal keer dat een waarde voorkomt. Zo'n tabel is meestal de eerste stap voor je een diagram tekent.",
    ),
    dict(
        type="invultekst",
        vraag="Bereken het gemiddelde van 4, 6 en 8.",
        antwoord="6",
        uitleg="Tel op en deel door het aantal: (4 + 6 + 8) : 3 = 18 : 3 = 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gemiddelde van 2, 5, 5 en 8?",
        opties=["5", "4", "6"],
        antwoord=0,
        uitleg="(2 + 5 + 5 + 8) : 4 = 20 : 4 = 5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de modus van 3, 7, 7, 9, 12?",
        opties=["7", "9", "7,6"],
        antwoord=0,
        uitleg="De modus is de waarde die het vaakst voorkomt. Hier is dat 7, want die staat er twee keer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van 3, 7, 9, 12, 20?",
        opties=["9", "10,2", "12"],
        antwoord=0,
        uitleg="De mediaan is het middelste getal als je ze op volgorde zet. Van vijf getallen is dat het derde: 9.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de variatiebreedte van 4, 9, 11 en 20?",
        opties=["16", "11", "20"],
        antwoord=0,
        uitleg="Variatiebreedte = grootste − kleinste = 20 − 4 = 16. Ze vertelt hoe ver de gegevens uit elkaar liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk diagram gebruik je het best om een verandering in de tijd te tonen?",
        opties=["Een lijndiagram", "Een cirkeldiagram", "Een staafdiagram"],
        antwoord=0,
        uitleg="Een lijndiagram laat zien hoe iets stijgt of daalt. Een staafdiagram vergelijkt groepen, een cirkeldiagram toont delen van één geheel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk diagram past het best om te tonen welk deel van de klas met de fiets komt?",
        opties=["Een cirkeldiagram", "Een lijndiagram", "Geen van beide"],
        antwoord=0,
        uitleg="Een cirkeldiagram toont hoe een geheel verdeeld is. De hele cirkel is samen 100 %, ofwel 360°.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden is de hele cirkel in een cirkeldiagram?",
        antwoord="360",
        uitleg="360°. Een kwart van de gegevens krijgt dus een sector van 90°.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klas van 25 komen er 10 met de fiets. Hoeveel procent is dat?",
        opties=["40 %", "25 %", "10 %"],
        antwoord=0,
        uitleg="10 : 25 = 0,40, dus 40 %.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep is 20 % van het geheel. Hoeveel graden krijgt die in een cirkeldiagram?",
        opties=["72°", "20°", "36°"],
        antwoord=0,
        uitleg="20 % van 360° = 0,20 × 360 = 72°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gemiddelde van 10, 10, 10 en 10?",
        opties=["10", "40", "4"],
        antwoord=0,
        uitleg="Zijn alle waarden gelijk, dan is het gemiddelde die waarde: 40 : 4 = 10.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gemiddelde moet altijd een van de gegeven waarden zijn.",
        antwoord=False,
        uitleg="Nee. Het gemiddelde van 4 en 7 is 5,5, en dat komt in de gegevens niet voor. De modus is wél altijd een van de waarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reeks heeft twee waarden die allebei het vaakst voorkomen. Wat betekent dat?",
        opties=["Er zijn twee modi", "Er is geen modus", "De modus is het gemiddelde"],
        antwoord=0,
        uitleg="Komen twee waarden even vaak voor, dan zijn er twee modi. Een reeks kan er ook helemaal geen hebben, als alles even vaak voorkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van 2, 4, 6 en 10?",
        opties=["5", "6", "5,5"],
        antwoord=0,
        uitleg="Bij een even aantal neem je het gemiddelde van de twee middelste: (4 + 6) : 2 = 5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een staafdiagram: waar lees je af hoe groot een groep is?",
        opties=["Aan de hoogte van de staaf", "Aan de breedte", "Aan de kleur"],
        antwoord=0,
        uitleg="De hoogte staat voor het aantal. De staven zijn even breed, zodat je ze eerlijk kan vergelijken.",
    ),
    dict(
        type="waarofniet",
        vraag="In een frequentietabel is de som van alle frequenties gelijk aan het aantal metingen.",
        antwoord=True,
        uitleg="Juist. Elke meting komt in precies één rij terecht, dus samen tellen ze op tot het totaal. Dat is meteen een handige controle.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt hoeveel uur je klasgenoten slapen. Wat is je onderzoeksvraag het best?",
        opties=[
            "Hoeveel uur slaapt een leerling uit onze klas gemiddeld per nacht?",
            "Slapen is gezond.",
            "Hoeveel leerlingen zitten er in de klas?",
        ],
        antwoord=0,
        uitleg="Een onderzoeksvraag is een vraag die je met je gegevens kan beantwoorden, en waarin staat wat je meet en bij wie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Vier vrienden verdienen € 10, € 12, € 14 en € 500 per week. Welke maat geeft het eerlijkste beeld van wat een gewone week opbrengt?",
        opties=["De mediaan", "Het gemiddelde", "De variatiebreedte"],
        antwoord=0,
        uitleg="Het gemiddelde is € 134, en dat lijkt op niemand. De mediaan is (12 + 14) : 2 = € 13 en past bij de meesten. Eén uitschieter trekt het gemiddelde ver weg, de mediaan bijna niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het gemiddelde van vier toetsen is 14. Wat is het totaal van de punten?",
        opties=["56", "14", "18"],
        antwoord=0,
        uitleg="Gemiddelde × aantal = totaal: 14 × 4 = 56. Zo reken je van een gemiddelde terug naar de som.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt 12, 15 en 16 op drie toetsen. Wat moet je op de vierde halen voor een gemiddelde van 15?",
        opties=["17", "15", "16"],
        antwoord=0,
        uitleg="Voor gemiddelde 15 over vier toetsen heb je 60 punten nodig. Je hebt er al 12 + 15 + 16 = 43, dus je hebt nog 17 nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een reeks van zes getallen is de mediaan 7, en het derde en vierde getal zijn 6 en 8. Klopt dat?",
        opties=["Ja, (6 + 8) : 2 = 7", "Nee, de mediaan moet 6 zijn", "Nee, de mediaan bestaat niet"],
        antwoord=0,
        uitleg="Bij zes getallen is de mediaan het gemiddelde van het derde en het vierde. Die hoeft zelf niet in de reeks voor te komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reeks heeft gemiddelde 20 en variatiebreedte 0. Wat weet je?",
        opties=["Alle waarden zijn 20", "Er zijn maar twee waarden", "De mediaan is 0"],
        antwoord=0,
        uitleg="Variatiebreedte 0 betekent dat grootste en kleinste gelijk zijn, dus alles is hetzelfde getal. En dat getal is dan ook het gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cirkeldiagram toont een sector van 90°. Welk deel van het geheel is dat?",
        opties=["Een vierde", "Een derde", "Een negende"],
        antwoord=0,
        uitleg="90 : 360 = 0,25, dus een vierde ofwel 25 %.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van 40 leerlingen komen er 15 te voet. Hoeveel graden krijgt die groep in een cirkeldiagram?",
        opties=["135°", "150°", "37,5°"],
        antwoord=0,
        uitleg="15 : 40 = 0,375, en 0,375 × 360 = 135°.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een staafdiagram begint zijn verticale as niet bij 0 maar bij 90. Wat is daar het gevaar van?",
        opties=[
            "Kleine verschillen lijken veel groter dan ze zijn",
            "De staven worden te breed",
            "Er is geen gevaar",
        ],
        antwoord=0,
        uitleg="Als de as niet bij nul begint, wordt een verschil van enkele eenheden visueel enorm. Kijk bij elk diagram eerst naar de as voor je conclusies trekt.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de mediaan van 5, 3, 9, 1 en 7?",
        antwoord="5",
        uitleg="Eerst op volgorde zetten: 1, 3, 5, 7, 9. Het middelste is 5. Vergeet dat sorteren nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het gemiddelde als je er een waarde bij doet die groter is dan het huidige gemiddelde?",
        opties=["Het stijgt", "Het daalt", "Het blijft gelijk"],
        antwoord=0,
        uitleg="Een waarde boven het gemiddelde trekt het omhoog. Een waarde die precies gelijk is aan het gemiddelde verandert er niets aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een frequentietabel staat: waarde 3 komt 5 keer voor, waarde 4 komt 3 keer voor. Hoeveel metingen zijn er?",
        opties=["8", "12", "27"],
        antwoord=0,
        uitleg="Tel de frequenties op: 5 + 3 = 8 metingen. De waarden zelf tel je niet op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarde 3 komt 5 keer voor en waarde 4 komt 3 keer voor. Wat is het gemiddelde?",
        opties=["3,375", "3,5", "8"],
        antwoord=0,
        uitleg="De som is 5 × 3 + 3 × 4 = 27, gedeeld door 8 metingen geeft 3,375. Vermenigvuldig elke waarde met haar frequentie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke centrummaat kan je gebruiken bij een categorische variabele zoals lievelingskleur?",
        opties=["Enkel de modus", "Het gemiddelde", "De mediaan"],
        antwoord=0,
        uitleg="Van kleuren kan je geen gemiddelde nemen en ze niet op volgorde zetten. Je kan wel zeggen welke het vaakst voorkomt: de modus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee klassen hebben allebei gemiddelde 14, maar klas A heeft variatiebreedte 4 en klas B heeft 16. Wat besluit je?",
        opties=[
            "In klas B liggen de resultaten veel verder uit elkaar",
            "Klas A is beter",
            "Klas B heeft meer leerlingen",
        ],
        antwoord=0,
        uitleg="Het gemiddelde zegt waar het midden ligt, de variatiebreedte hoe verspreid het is. Daarom heb je ze allebei nodig om twee groepen te vergelijken.",
    ),
    dict(
        type="waarofniet",
        vraag="De mediaan verandert nauwelijks als je één heel grote waarde toevoegt.",
        antwoord=True,
        uitleg="Juist. De mediaan kijkt enkel naar de plaats in de rij, niet naar hoe groot de getallen zijn. Daarom is ze betrouwbaarder bij uitschieters.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in een krant: „de gemiddelde Belg heeft 1,7 kinderen”. Hoe kan dat?",
        opties=[
            "Een gemiddelde hoeft geen bestaand aantal te zijn",
            "De krant heeft zich vergist",
            "Sommige kinderen tellen voor 0,7",
        ],
        antwoord=0,
        uitleg="Een gemiddelde is een rekenresultaat, geen echte persoon. Het is handig om groepen te vergelijken, maar het beschrijft niemand in het bijzonder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil twee klassen van verschillende grootte vergelijken. Wat gebruik je het best?",
        opties=[
            "Procenten, want dan telt de klasgrootte niet mee",
            "De absolute aantallen",
            "De variatiebreedte",
        ],
        antwoord=0,
        uitleg="10 van de 20 is meer dan 12 van de 40, ook al is 12 het grotere getal. Met procenten (50 % tegenover 30 %) vergelijk je eerlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van zeven metingen is de kleinste 3 en de grootste 3. Wat is de modus?",
        opties=["3", "Er is geen modus", "0"],
        antwoord=0,
        uitleg="Kleinste en grootste zijn allebei 3, dus alle zeven metingen zijn 3. Die waarde komt dus het vaakst voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de laatste stap van een statistisch onderzoek?",
        opties=[
            "Een antwoord formuleren op je onderzoeksvraag",
            "Het diagram inkleuren",
            "De variatiebreedte berekenen",
        ],
        antwoord=0,
        uitleg="Cijfers zijn geen antwoord. Je onderzoek is pas af als je in gewone taal zegt wat ze betekenen voor de vraag waarmee je begon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lijndiagram toont de temperatuur elk uur. Tussen 14 u en 15 u loopt de lijn steil omhoog. Wat betekent dat?",
        opties=[
            "Het werd in dat uur snel warmer",
            "Het was toen het warmst",
            "Er zijn meer metingen gedaan",
        ],
        antwoord=0,
        uitleg="Bij een lijndiagram zegt de steilheid hoe snel iets verandert, en de hoogte hoe groot het is. Dat zijn twee verschillende dingen.",
    ),
]
