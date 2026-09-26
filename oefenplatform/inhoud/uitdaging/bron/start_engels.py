# -*- coding: utf-8 -*-
"""Uitdaging Engels 🌱 Start: woorden, to be en to have, de tegenwoordige tijd
en zinsbouw door elkaar, met echte Engelse zinnetjes om uit te lezen.
"""
NIVEAU = "start"
VAK = "Engels"
BESTAND = "start-engels-uitdaging.json"

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Lees: \"Tom has got two sisters. He doesn't have a brother. His sisters go to the same school as Tom.\" Hoeveel kinderen zijn er in het gezin van Tom?",
        "opties": ["Drie", "Twee", "Vier", "Eén"],
        "antwoord": 0,
        "uitleg": "Tom heeft twee zussen en geen broer. Tom zelf telt mee, dus samen zijn ze met drie.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke van deze vier zinnen klopt?",
        "opties": [
            "My sister doesn't have a bike.",
            "My sister doesn't has a bike.",
            "My sister don't have a bike.",
            "My sister doesn't has got a bike.",
        ],
        "antwoord": 0,
        "uitleg": "Bij she hoort doesn't, en na doesn't blijft het werkwoord in zijn gewone vorm staan: doesn't have, nooit doesn't has.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan met de juiste vorm: \"My brother ... television every evening.\" (to watch)",
        "antwoord": "watches",
        "uitleg": "Bij he, she of it komt er een -s bij. Eindigt het werkwoord op -ch, dan wordt dat -es: watches.",
    },
    {
        "type": "waarofniet",
        "vraag": "In de zin \"She has got a cat\" mag je \"has got\" vervangen door \"has\".",
        "antwoord": True,
        "uitleg": "Waar. She has got a cat en she has a cat betekenen allebei: ze heeft een kat. Has got hoor je vooral in Groot-Brittannië.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke vraag staat hier correct?",
        "opties": [
            "Does your sister speak French?",
            "Do your sister speaks French?",
            "Does your sister speaks French?",
            "Is your sister speak French?",
        ],
        "antwoord": 0,
        "uitleg": "Bij your sister hoort does, en dan blijft het werkwoord kaal: does ... speak. De -s zit al in does.",
    },
    {
        "type": "invultekst",
        "vraag": "Wat is het meervoud van \"woman\"?",
        "antwoord": "women",
        "uitleg": "Woman wordt women, net zoals man man men wordt. Die meervouden krijgen geen -s, je moet ze uit het hoofd kennen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Het is 7.45 uur. Hoe zeg je dat in het Engels?",
        "opties": [
            "Quarter to eight",
            "Quarter past eight",
            "Quarter to seven",
            "Half past seven",
        ],
        "antwoord": 0,
        "uitleg": "In het Engels kijk je vooruit naar het volgende uur: een kwartier vóór acht. Let op, dat is anders dan bij ons kwart voor acht wel, maar half acht niet.",
    },
    {
        "type": "waarofniet",
        "vraag": "\"Tomorrow\" en \"yesterday\" betekenen allebei gisteren.",
        "antwoord": False,
        "uitleg": "Niet waar. Yesterday is gisteren, tomorrow is morgen. Ze wijzen dus net de andere kant op in de tijd.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Lees: \"Go straight on, then turn left at the station. The shop is opposite the church.\" Waar is de winkel?",
        "opties": [
            "Tegenover de kerk",
            "Naast het station",
            "Rechts van de kerk",
            "Achter het station",
        ],
        "antwoord": 0,
        "uitleg": "Opposite betekent tegenover. Next to zou naast betekenen, en turn left is linksaf slaan.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan: \"Where ... your parents from?\"",
        "antwoord": "are",
        "uitleg": "Your parents is meervoud, dus hoort daar are bij: where are your parents from?",
    },
    {
        "type": "meerkeuze",
        "vraag": "In welke zin staan de woorden in de juiste volgorde?",
        "opties": [
            "I often play football on Saturday.",
            "I play often football on Saturday.",
            "Often I play on Saturday football.",
            "I play football often on Saturday.",
        ],
        "antwoord": 0,
        "uitleg": "Woorden als often, never en always staan vlak voor het werkwoord, en het lijdend voorwerp volgt meteen op dat werkwoord.",
    },
    {
        "type": "waarofniet",
        "vraag": "In het Engels schrijf je de maanden én de dagen van de week met een hoofdletter.",
        "antwoord": True,
        "uitleg": "Waar: Monday, July, December. In het Nederlands schrijf je die net met een kleine letter, dus dat is een makkelijke valkuil.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke zin is helemaal juist?",
        "opties": [
            "My father has got an old red car.",
            "My father has got a old red car.",
            "My father has got an red old car.",
            "My father have got an old red car.",
        ],
        "antwoord": 0,
        "uitleg": "Voor een klinkerklank staat an, dus an old. En in het Engels staan de bijvoeglijke naamwoorden vóór het zelfstandig naamwoord, in de volgorde old red car.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan: \"My brother is twelve years ...\" (hoe je in het Engels je leeftijd afmaakt)",
        "antwoord": "old",
        "uitleg": "In het Engels zeg je he is twelve years old, dus met het werkwoord to be. I have twelve years bestaat niet.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent \"I don't understand. Could you repeat that, please?\"",
        "opties": [
            "Ik begrijp het niet. Kan u dat herhalen, alstublieft?",
            "Ik weet het niet. Mag ik het antwoord krijgen, alstublieft?",
            "Ik hoor u niet. Kan u luider spreken, alstublieft?",
            "Ik ben het er niet mee eens. Mag ik iets zeggen, alstublieft?",
        ],
        "antwoord": 0,
        "uitleg": "To understand is begrijpen en to repeat is herhalen. Dit zijn twee zinnen die altijd van pas komen in de les.",
    },
    {
        "type": "waarofniet",
        "vraag": "Je vraagt iemands leeftijd in het Engels met \"How many years have you?\"",
        "antwoord": False,
        "uitleg": "Niet waar. Dat is te letterlijk vertaald uit het Nederlands. In het Engels vraag je: How old are you?",
    },
    {
        "type": "meerkeuze",
        "vraag": "Lees: \"Emma is eleven. She lives in Hasselt with her mother, her father and her grandmother. She has got a dog.\" Wie woont er bij Emma in huis?",
        "opties": [
            "Haar ouders en haar grootmoeder",
            "Haar ouders en haar tante",
            "Haar ouders en haar nicht",
            "Alleen haar moeder en haar hond",
        ],
        "antwoord": 0,
        "uitleg": "Mother en father zijn haar ouders, en grandmother is haar grootmoeder. Aunt zou tante zijn en cousin neef of nicht.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan: \"There ... three books on the table.\"",
        "antwoord": "are",
        "uitleg": "Er zijn er drie, dus meervoud: there are. Bij één boek zou je there is schrijven.",
    },
    {
        "type": "waarofniet",
        "vraag": "\"His\" en \"her\" zeggen allebei van wie iets is.",
        "antwoord": True,
        "uitleg": "Waar. His book is zijn boek, her book is haar boek. Welke van de twee je neemt, hangt af van de eigenaar, niet van het voorwerp.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In welke zin staat een fout?",
        "opties": [
            "He doesn't plays football.",
            "He doesn't play football.",
            "She watches television.",
            "They don't live in Belgium.",
        ],
        "antwoord": 0,
        "uitleg": "Na doesn't blijft het werkwoord kaal: he doesn't play. De -s zit al in doesn't verwerkt.",
    },
]
