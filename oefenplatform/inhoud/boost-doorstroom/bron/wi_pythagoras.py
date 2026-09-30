# -*- coding: utf-8 -*-
"""De vragen voor "Pythagoras en de rechthoekige driehoek".

Uit de bouwsteen Meetkunde en metend rekenen: de stelling van Pythagoras in het
vlak en in de ruimte, de analytische uitdrukking voor de afstand tussen twee
punten, de goniometrische getallen sinus, cosinus en tangens als verhoudingen
van zijden in een rechthoekige driehoek, de grondformule, de goniometrische
cirkel en de verwante hoeken.

Deel 1 is Pythagoras en de afstand tussen twee punten. Deel 2 is de
goniometrie in de rechthoekige driehoek, met de grondformule en de cirkel.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de stelling van Pythagoras?",
        opties=[
            "in een rechthoekige driehoek is de som van de kwadraten van de rechthoekszijden gelijk aan het kwadraat van de schuine zijde",
            "in elke driehoek is de som van de kwadraten van twee zijden gelijk aan het kwadraat van de derde zijde",
            "in een rechthoekige driehoek is de som van de rechthoekszijden gelijk aan de schuine zijde",
            "in elke driehoek is de langste zijde gelijk aan de som van de twee andere zijden",
        ],
        antwoord=0,
        uitleg="De stelling geldt uitsluitend voor rechthoekige driehoeken, en de schuine zijde staat altijd tegenover de rechte hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechthoekige driehoek heeft rechthoekszijden 6 en 8. Hoe lang is de schuine zijde?",
        opties=["10", "14", "48", "ongeveer 7"],
        antwoord=0,
        uitleg="36 plus 64 is 100, en de wortel van 100 is 10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechthoekige driehoek heeft een schuine zijde van 13 en een rechthoekszijde van 5. Hoe lang is de andere rechthoekszijde?",
        opties=["12", "8", "18", "ongeveer 14"],
        antwoord=0,
        uitleg="169 min 25 is 144, en de wortel van 144 is 12. Let op: hier trek je af in plaats van op te tellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een driehoek heeft zijden 9, 12 en 15. Is hij rechthoekig?",
        opties=[
            "ja, want 81 plus 144 is precies 225",
            "nee, want 9 plus 12 is niet gelijk aan 15",
            "ja, want alle drie de zijden zijn veelvouden van 3",
            "dat kan je zonder de hoeken niet bepalen",
        ],
        antwoord=0,
        uitleg="Je gebruikt de omgekeerde stelling: klopt de gelijkheid, dan is de driehoek rechthoekig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een driehoek heeft zijden 4, 5 en 7. Is hij rechthoekig?",
        opties=[
            "nee, want 16 plus 25 is 41 en dat is geen 49",
            "ja, want 4 plus 5 is groter dan 7",
            "ja, want 16 plus 25 komt dicht genoeg bij 49",
            "dat hangt af van welke hoek je meet",
        ],
        antwoord=0,
        uitleg="Bijna klopt niet. 41 tegenover 49 betekent dat de grootste hoek stomp is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ladder van 5 meter staat met de voet 3 meter van de muur. Hoe hoog reikt hij?",
        opties=["4 meter", "2 meter", "ongeveer 5,8 meter", "8 meter"],
        antwoord=0,
        uitleg="25 min 9 is 16, en de wortel daarvan is 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de afstand tussen de punten A(1, 2) en B(4, 6)?",
        opties=["5", "7", "ongeveer 3,6", "25"],
        antwoord=0,
        uitleg="Het verschil in x is 3 en in y is 4. Dan 9 plus 16 is 25, en de wortel is 5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de afstand tussen A(min 2, 1) en B(1, 5)?",
        opties=["5", "4", "ongeveer 3,2", "7"],
        antwoord=0,
        uitleg="Het verschil in x is 3 en in y is 4, dus weer de driehoek 3-4-5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de afstand tussen twee punten in het vlak?",
        opties=[
            "de wortel uit het kwadraat van het verschil in x plus het kwadraat van het verschil in y",
            "het verschil in x plus het verschil in y, samen gedeeld door twee",
            "de wortel uit het verschil in x plus het verschil in y",
            "het kwadraat van het verschil in x plus het kwadraat van het verschil in y",
        ],
        antwoord=0,
        uitleg="Het is Pythagoras op de rechthoekige driehoek die de twee punten met hun horizontale en verticale verschil maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een balk is 3 bij 4 bij 12. Hoe lang is de ruimtediagonaal?",
        opties=["13", "19", "12", "ongeveer 14,4"],
        antwoord=0,
        uitleg="Eerst de diagonaal van de bodem: wortel uit 9 plus 16 is 5. Dan wortel uit 25 plus 144 is 13.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom pas je bij een ruimtediagonaal Pythagoras twee keer toe?",
        opties=[
            "eerst voor de diagonaal van het grondvlak, dan voor de diagonaal met de hoogte erbij",
            "omdat een balk twee verschillende diagonalen heeft die je moet optellen",
            "omdat de stelling in de ruimte maar de helft van het resultaat geeft",
            "omdat je anders de eenheden niet kan omzetten naar meter",
        ],
        antwoord=0,
        uitleg="De eerste diagonaal is de rechthoekszijde van de tweede driehoek, samen met de hoogte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een televisie van 40 inch: wat wordt daarmee gemeten?",
        opties=[
            "de diagonaal van het scherm",
            "de breedte van het scherm",
            "de hoogte van het scherm",
            "de omtrek van het scherm",
        ],
        antwoord=0,
        uitleg="Daarom kan je met Pythagoras en de beeldverhouding de echte breedte en hoogte uitrekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke driehoek ligt de schuine zijde?",
        opties=[
            "tegenover de rechte hoek",
            "tegenover de kleinste hoek",
            "tussen de twee scherpe hoeken in",
            "altijd horizontaal onderaan de tekening",
        ],
        antwoord=0,
        uitleg="De schuine zijde is ook altijd de langste zijde van een rechthoekige driehoek.",
    ),
    dict(
        type="waarofniet",
        vraag="De stelling van Pythagoras geldt in elke driehoek.",
        antwoord=False,
        uitleg="Alleen in rechthoekige. Voor andere driehoeken heb je de cosinusregel nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een driehoek met zijden 5, 12 en 13 is rechthoekig.",
        antwoord=True,
        uitleg="25 plus 144 is 169, en dat is 13 in het kwadraat.",
    ),
    dict(
        type="waarofniet",
        vraag="De afstand tussen twee punten kan negatief zijn als het ene punt links van het andere ligt.",
        antwoord=False,
        uitleg="Door de kwadraten valt het teken weg, en een wortel geeft nooit een negatief getal.",
    ),
    dict(
        type="waarofniet",
        vraag="In een rechthoekige driehoek is de schuine zijde altijd de langste zijde.",
        antwoord=True,
        uitleg="Ze ligt tegenover de grootste hoek, en die is recht.",
    ),
    dict(
        type="invultekst",
        vraag="Een rechthoekige driehoek heeft rechthoekszijden 9 en 12. Hoe lang is de schuine zijde?",
        antwoord=["15"],
        uitleg="81 plus 144 is 225.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de afstand tussen A(0, 0) en B(6, 8)?",
        antwoord=["10"],
        uitleg="36 plus 64 is 100.",
    ),
    dict(
        type="invultekst",
        vraag="Een vierkant heeft een zijde van 1. Hoe lang is de diagonaal? Typ bijvoorbeeld 2√3.",
        antwoord=["√2", "wortel 2"],
        uitleg="1 plus 1 is 2, dus de diagonaal is de wortel van 2. Dat is meteen het klassieke irrationale getal.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de sinus van een scherpe hoek in een rechthoekige driehoek?",
        opties=[
            "de overstaande rechthoekszijde gedeeld door de schuine zijde",
            "de aanliggende rechthoekszijde gedeeld door de schuine zijde",
            "de overstaande gedeeld door de aanliggende rechthoekszijde",
            "de schuine zijde gedeeld door de overstaande rechthoekszijde",
        ],
        antwoord=0,
        uitleg="Ezelsbruggetje SOS CAS TOA: Sinus is Overstaande op Schuine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de cosinus van een scherpe hoek in een rechthoekige driehoek?",
        opties=[
            "de aanliggende rechthoekszijde gedeeld door de schuine zijde",
            "de overstaande rechthoekszijde gedeeld door de schuine zijde",
            "de aanliggende gedeeld door de overstaande rechthoekszijde",
            "de schuine zijde gedeeld door de aanliggende rechthoekszijde",
        ],
        antwoord=0,
        uitleg="Cosinus is Aanliggende op Schuine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de tangens van een scherpe hoek?",
        opties=[
            "de overstaande gedeeld door de aanliggende rechthoekszijde",
            "de aanliggende gedeeld door de overstaande rechthoekszijde",
            "de overstaande rechthoekszijde gedeeld door de schuine zijde",
            "de schuine zijde gedeeld door de aanliggende rechthoekszijde",
        ],
        antwoord=0,
        uitleg="Tangens is Overstaande op Aanliggende. Daarom werkt de tangens zo goed bij hellingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent de kijkhoek naar de top van een boom en je afstand tot de boom. Welk goniometrisch getal gebruik je?",
        opties=["de tangens", "de sinus", "de cosinus", "de grondformule"],
        antwoord=0,
        uitleg="Je kent de aanliggende zijde en zoekt de overstaande, en dat is precies de tangens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent de lengte van een helling en de hellingshoek, en je zoekt het hoogteverschil. Wat gebruik je?",
        opties=["de sinus", "de cosinus", "de tangens", "de stelling van Pythagoras"],
        antwoord=0,
        uitleg="De helling zelf is de schuine zijde en het hoogteverschil de overstaande zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de grondformule van de goniometrie?",
        opties=[
            "sinus kwadraat plus cosinus kwadraat is gelijk aan één",
            "sinus plus cosinus is gelijk aan één",
            "sinus gedeeld door cosinus is gelijk aan één",
            "sinus kwadraat min cosinus kwadraat is gelijk aan één",
        ],
        antwoord=0,
        uitleg="Ze volgt rechtstreeks uit Pythagoras op de goniometrische cirkel met straal 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="De sinus van een hoek is 0,6. Wat is de cosinus als de hoek scherp is?",
        opties=["0,8", "0,4", "1,6", "0,36"],
        antwoord=0,
        uitleg="0,36 plus cosinus kwadraat is 1, dus cosinus kwadraat is 0,64 en de cosinus is 0,8.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe druk je de tangens uit met de sinus en de cosinus?",
        opties=[
            "tangens is sinus gedeeld door cosinus",
            "tangens is cosinus gedeeld door sinus",
            "tangens is sinus maal cosinus",
            "tangens is sinus plus cosinus",
        ],
        antwoord=0,
        uitleg="Beide verhoudingen hebben de schuine zijde als noemer, en die valt bij het delen weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de sinus van 30 graden?",
        opties=["0,5", "ongeveer 0,87", "1", "ongeveer 0,58"],
        antwoord=0,
        uitleg="Bij 30 graden is de overstaande zijde precies de helft van de schuine zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de cosinus van 0 graden?",
        opties=["1", "0", "0,5", "dat bestaat niet"],
        antwoord=0,
        uitleg="Op de goniometrische cirkel ligt het punt bij 0 graden helemaal rechts, met x-waarde 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de straal van de goniometrische cirkel?",
        opties=["1", "2", "pi", "afhankelijk van de hoek"],
        antwoord=0,
        uitleg="Door straal 1 te kiezen zijn de cosinus en de sinus gewoon de x- en de y-coördinaat van het punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heten twee hoeken die samen 180 graden geven?",
        opties=["supplementair", "complementair", "anticomplementair", "tegengesteld"],
        antwoord=0,
        uitleg="Samen 90 graden heet complementair. Supplementaire hoeken hebben dezelfde sinus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heten twee hoeken die samen 90 graden geven?",
        opties=["complementair", "supplementair", "antisupplementair", "gelijk"],
        antwoord=0,
        uitleg="Bij complementaire hoeken wisselen sinus en cosinus van plaats: de sinus van 30 is de cosinus van 60.",
    ),
    dict(
        type="waarofniet",
        vraag="De sinus van een scherpe hoek is altijd kleiner dan één.",
        antwoord=True,
        uitleg="De overstaande zijde is altijd korter dan de schuine zijde.",
    ),
    dict(
        type="waarofniet",
        vraag="De tangens van 45 graden is gelijk aan één.",
        antwoord=True,
        uitleg="Bij 45 graden zijn de twee rechthoekszijden even lang, dus hun verhouding is 1.",
    ),
    dict(
        type="waarofniet",
        vraag="De cosinus van een hoek kan groter zijn dan één.",
        antwoord=False,
        uitleg="Ze is een verhouding met de schuine zijde als noemer, en die is altijd de grootste.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee complementaire hoeken hebben dezelfde sinus.",
        antwoord=False,
        uitleg="Bij complementaire hoeken is de sinus van de ene de cosinus van de andere. Dezelfde sinus hebben supplementaire hoeken.",
    ),
    dict(
        type="invultekst",
        vraag="De sinus van een scherpe hoek is 0,8. Hoeveel is de cosinus?",
        antwoord=["0,6"],
        uitleg="0,64 plus 0,36 is 1.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de tangens van 45 graden?",
        antwoord=["1"],
        uitleg="De twee rechthoekszijden zijn dan even lang.",
    ),
    dict(
        type="invultekst",
        vraag="Welke afkorting gebruik je voor overstaande op schuine zijde?",
        antwoord=["sinus", "sin"],
        uitleg="SOS CAS TOA helpt om de drie uit elkaar te houden.",
    ),
]
