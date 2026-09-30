# -*- coding: utf-8 -*-
"""De vragen voor "Formules omvormen en eerstegraadsvergelijkingen".

Uit de bouwsteen Relaties en verandering: bij een formule één variabele
uitdrukken in functie van een andere, met de eigenschappen van gelijkheden en
de teken- en rekenregels, en daarnaast het algebraïsch en grafisch oplossen van
eerstegraadsvergelijkingen en -ongelijkheden in één onbekende, met de
oplossingenverzameling, de intervalnotatie en het verband met de nulwaarde en
het tekenverloop van een functie.

De formules uit de natuurwetenschappen die de fiche opsomt, komen hier als
context aan bod: massadichtheid, de eenparig rechtlijnige beweging, kracht,
druk, energie, de wet van Ohm, de veerkracht en de molaire concentratie.

Deel 1 is het omvormen van formules. Deel 2 zijn de vergelijkingen en de
ongelijkheden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke eigenschap van gelijkheden gebruik je om bij beide leden hetzelfde getal op te tellen?",
        opties=[
            "wat je links doet, moet je rechts ook doen, anders klopt de gelijkheid niet meer",
            "je mag links iets optellen en rechts iets aftrekken, zolang het evenveel is",
            "je mag bij een gelijkheid alleen vermenigvuldigen, nooit optellen",
            "je mag enkel getallen optellen, nooit een uitdrukking met een letter",
        ],
        antwoord=0,
        uitleg="Een gelijkheid is een balans. Wie aan één kant iets verandert, moet dat aan de andere kant ook doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat mag je nooit doen bij het omvormen van een gelijkheid?",
        opties=[
            "beide leden delen door nul",
            "beide leden vermenigvuldigen met min 1",
            "bij beide leden hetzelfde getal optellen",
            "de linker- en het rechterlid van plaats verwisselen",
        ],
        antwoord=0,
        uitleg="Delen door nul is niet gedefinieerd. Delen door een letter mag wel, maar alleen als je weet dat ze niet nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag="De massadichtheid is massa gedeeld door volume. Hoe druk je de massa uit?",
        opties=[
            "massa is massadichtheid maal volume",
            "massa is volume gedeeld door massadichtheid",
            "massa is massadichtheid gedeeld door volume",
            "massa is massadichtheid plus volume",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt beide leden met het volume, en dan valt het rechts weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="De wet van Ohm zegt: spanning is stroom maal weerstand. Hoe druk je de weerstand uit?",
        opties=[
            "weerstand is spanning gedeeld door stroom",
            "weerstand is stroom gedeeld door spanning",
            "weerstand is spanning maal stroom",
            "weerstand is spanning min stroom",
        ],
        antwoord=0,
        uitleg="Je deelt beide leden door de stroom.",
    ),
    dict(
        type="meerkeuze",
        vraag="De zwaartekracht is massa maal valversnelling. Hoe bereken je de massa uit een gegeven kracht?",
        opties=[
            "de kracht delen door de valversnelling",
            "de kracht vermenigvuldigen met de valversnelling",
            "de valversnelling delen door de kracht",
            "de kracht en de valversnelling optellen",
        ],
        antwoord=0,
        uitleg="Een kracht van 98 newton bij een valversnelling van ongeveer 9,8 geeft een massa van 10 kilogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Druk is kracht gedeeld door oppervlakte. Wat gebeurt er als de oppervlakte kleiner wordt bij dezelfde kracht?",
        opties=[
            "de druk wordt groter",
            "de druk wordt kleiner",
            "de druk blijft gelijk",
            "de kracht wordt automatisch kleiner",
        ],
        antwoord=0,
        uitleg="Daarom zakt een naald wel in het hout en een vingertop niet, bij dezelfde duwkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="De formule voor de eenparig rechtlijnige beweging is x is x nul plus v maal t. Hoe druk je t uit?",
        opties=[
            "t is x min x nul, gedeeld door v",
            "t is x plus x nul, gedeeld door v",
            "t is v gedeeld door x min x nul",
            "t is x maal v min x nul",
        ],
        antwoord=0,
        uitleg="Eerst breng je x nul naar het andere lid, daarna deel je door v.",
    ),
    dict(
        type="meerkeuze",
        vraag="De kinetische energie is een half maal massa maal snelheid in het kwadraat. Wat gebeurt er als de snelheid verdubbelt?",
        opties=[
            "de energie wordt vier keer zo groot",
            "de energie wordt twee keer zo groot",
            "de energie wordt half zo groot",
            "de energie blijft gelijk",
        ],
        antwoord=0,
        uitleg="De snelheid staat in het kwadraat. Daarom groeit de remweg zo snel met de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="De molaire concentratie is aantal mol gedeeld door volume. Hoe bereken je het volume?",
        opties=[
            "het aantal mol delen door de concentratie",
            "het aantal mol maal de concentratie",
            "de concentratie delen door het aantal mol",
            "de concentratie en het aantal mol optellen",
        ],
        antwoord=0,
        uitleg="Dezelfde omvorming als bij de massadichtheid: de noemer en de uitkomst wisselen van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een formule lineair is in x?",
        opties=[
            "x komt enkel in de eerste macht voor, zonder kwadraat of wortel",
            "x staat altijd links van het gelijkheidsteken",
            "de grafiek gaat altijd door de oorsprong",
            "er staat precies één x in de hele formule",
        ],
        antwoord=0,
        uitleg="De grafiek van een lineair verband is een rechte. Een zuiver kwadratisch verband geeft een parabool.",
    ),
    dict(
        type="meerkeuze",
        vraag="De oppervlakte van een vierkant is de zijde in het kwadraat. Hoe druk je de zijde uit?",
        opties=[
            "de zijde is de vierkantswortel van de oppervlakte",
            "de zijde is de oppervlakte gedeeld door twee",
            "de zijde is de oppervlakte gedeeld door vier",
            "de zijde is de oppervlakte in het kwadraat",
        ],
        antwoord=0,
        uitleg="Delen door vier zou de omtrek geven, niet de zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="De veerkracht is de veerconstante maal de uitrekking. Hoe bereken je de uitrekking?",
        opties=[
            "de kracht delen door de veerconstante",
            "de kracht maal de veerconstante",
            "de veerconstante delen door de kracht",
            "de kracht min de veerconstante",
        ],
        antwoord=0,
        uitleg="Bij een stijve veer, dus een grote constante, geeft dezelfde kracht een kleinere uitrekking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je na het omvormen best met een getallenvoorbeeld?",
        opties=[
            "omdat een tekenfout of een verkeerde bewerking zo meteen opvalt",
            "omdat een formule pas geldt als je er getallen in gezet hebt",
            "omdat de fiche dat verplicht bij elke omvorming",
            "omdat je anders geen rekenmachine mag gebruiken",
        ],
        antwoord=0,
        uitleg="Vul in de oorspronkelijke formule getallen in, en kijk of je omgevormde versie hetzelfde geeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het omvormen van een formule mag je beide leden door dezelfde letter delen, ook als die nul kan zijn.",
        antwoord=False,
        uitleg="Delen door nul mag niet, dus je moet eerst weten dat die letter niet nul is.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je beide leden van een gelijkheid met min 1 vermenigvuldigt, blijft de gelijkheid kloppen.",
        antwoord=True,
        uitleg="Alle tekens draaien om, maar links en rechts blijven gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="In de formule voor de kinetische energie is de energie recht evenredig met de snelheid.",
        antwoord=False,
        uitleg="Ze is recht evenredig met het kwadraat van de snelheid. Dat is iets heel anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lineair verband tussen twee grootheden geeft een rechte als grafiek.",
        antwoord=True,
        uitleg="Bij een recht evenredig verband gaat die rechte bovendien door de oorsprong.",
    ),
    dict(
        type="invultekst",
        vraag="Massadichtheid is massa gedeeld door volume. Wat is de massa van 3 liter water met dichtheid 1 kg per liter?",
        antwoord=["3", "3 kg", "3 kilogram"],
        uitleg="Massa is dichtheid maal volume.",
    ),
    dict(
        type="invultekst",
        vraag="Bij een spanning van 12 volt en een stroom van 3 ampère, hoeveel ohm is de weerstand?",
        antwoord=["4", "4 ohm"],
        uitleg="Weerstand is spanning gedeeld door stroom.",
    ),
    dict(
        type="invultekst",
        vraag="De oppervlakte van een vierkant is 49. Hoe lang is de zijde?",
        antwoord=["7"],
        uitleg="De wortel van 49.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van 3x plus 5 is 20?",
        opties=["x is 5", "x is 15", "x is 25 op 3", "x is 8"],
        antwoord=0,
        uitleg="Eerst 5 aftrekken aan beide kanten, dan door 3 delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van 2x min 7 is x plus 3?",
        opties=["x is 10", "x is 4", "x is min 10", "x is 3 op 2"],
        antwoord=0,
        uitleg="Breng x naar links en 7 naar rechts: x is 3 plus 7.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het ongelijkheidsteken als je beide leden door min 2 deelt?",
        opties=[
            "het draait om",
            "het blijft staan zoals het stond",
            "het wordt een gelijkheidsteken",
            "het verdwijnt en je krijgt een interval",
        ],
        antwoord=0,
        uitleg="Dat is de enige plaats waar een ongelijkheid zich anders gedraagt dan een gelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossingenverzameling van min 3x groter dan 9?",
        opties=[
            "alle x kleiner dan min 3",
            "alle x groter dan min 3",
            "alle x groter dan 3",
            "alle x kleiner dan 3",
        ],
        antwoord=0,
        uitleg="Delen door min 3 draait het teken om: x kleiner dan min 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noteer je 'alle x kleiner dan of gelijk aan 4' als interval?",
        opties=["]−∞, 4]", "]−∞, 4[", "[4, +∞[", "]4, +∞["],
        antwoord=0,
        uitleg="De 4 hoort erbij, dus rechts een vierkant haakje naar binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de oplossing van f(x) is nul en de grafiek van f?",
        opties=[
            "het is de x-waarde waar de grafiek de x-as snijdt",
            "het is de y-waarde waar de grafiek de y-as snijdt",
            "het is de helling van de grafiek in dat punt",
            "het is het hoogste punt van de grafiek",
        ],
        antwoord=0,
        uitleg="Die x-waarde heet de nulwaarde, en het punt op de grafiek heet het nulpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="De oplossing van f(x) groter dan nul lees je af uit ...",
        opties=[
            "het tekenverloop: waar staat de functie positief?",
            "het verloopschema: waar stijgt de functie?",
            "de nulwaarde alleen, zonder verder te kijken",
            "het snijpunt met de y-as",
        ],
        antwoord=0,
        uitleg="Het tekenverloop zegt waar de grafiek boven en waar ze onder de x-as ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vergelijking geeft 0 is 5. Wat besluit je?",
        opties=[
            "de vergelijking heeft geen oplossing",
            "de vergelijking heeft oneindig veel oplossingen",
            "x is gelijk aan 5",
            "je maakte zeker een rekenfout",
        ],
        antwoord=0,
        uitleg="Er blijft een onwaarheid over, dus geen enkele x voldoet. De oplossingenverzameling is leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vergelijking geeft 0 is 0. Wat besluit je?",
        opties=[
            "elke waarde van x is een oplossing",
            "er is geen enkele oplossing",
            "x is gelijk aan nul",
            "de vergelijking is fout opgeschreven",
        ],
        antwoord=0,
        uitleg="Er blijft een waarheid over, dus elke x voldoet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een taxi vraagt 4 euro opstap en 1,5 euro per kilometer. Welke vergelijking hoort bij een rit van 19 euro?",
        opties=[
            "4 plus 1,5x is 19",
            "4 maal 1,5x is 19",
            "4x plus 1,5 is 19",
            "1,5 min 4x is 19",
        ],
        antwoord=0,
        uitleg="De opstap betaal je één keer, de kilometerprijs per kilometer. De rit is 10 kilometer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee abonnementen: A kost 20 euro plus 0,10 euro per minuut, B kost 8 euro plus 0,20 euro per minuut. Vanaf wanneer is A goedkoper?",
        opties=[
            "vanaf meer dan 120 minuten",
            "vanaf meer dan 60 minuten",
            "vanaf meer dan 40 minuten",
            "A is altijd duurder dan B",
        ],
        antwoord=0,
        uitleg="Stel 20 plus 0,1x kleiner dan 8 plus 0,2x. Dan 12 kleiner dan 0,1x, dus x groter dan 120.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe los je een eerstegraadsvergelijking grafisch op?",
        opties=[
            "je tekent links en rechts als een functie en zoekt het snijpunt",
            "je tekent enkel de linkerkant en leest de top af",
            "je berekent de oppervlakte tussen de twee rechten",
            "je zoekt waar de twee grafieken evenwijdig lopen",
        ],
        antwoord=0,
        uitleg="De x-waarde van het snijpunt is de oplossing. Hebben de rechten geen snijpunt, dan is er geen oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oplossing van x op 3 plus 2 is 5?",
        opties=["x is 9", "x is 21", "x is 1", "x is 15"],
        antwoord=0,
        uitleg="Eerst 2 aftrekken, dan met 3 vermenigvuldigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het delen van een ongelijkheid door een positief getal draait het teken om.",
        antwoord=False,
        uitleg="Alleen bij een negatief getal. Bij een positief getal verandert er niets.",
    ),
    dict(
        type="waarofniet",
        vraag="De oplossingenverzameling van een ongelijkheid noteer je meestal als een interval.",
        antwoord=True,
        uitleg="Dat is korter dan een zin, en je ziet meteen of de grens erbij hoort.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eerstegraadsvergelijking in één onbekende heeft altijd precies één oplossing.",
        antwoord=False,
        uitleg="Ze kan er ook geen of oneindig veel hebben, afhankelijk van wat er na het vereenvoudigen overblijft.",
    ),
    dict(
        type="waarofniet",
        vraag="De nulwaarde van een functie is de x-waarde waarvoor de functiewaarde nul is.",
        antwoord=True,
        uitleg="Het bijhorende punt op de grafiek heet het nulpunt en ligt op de x-as.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: 5x min 3 is 12. Wat is x?",
        antwoord=["3"],
        uitleg="5x is 15, dus x is 3.",
    ),
    dict(
        type="invultekst",
        vraag="Los op: 2(x plus 4) is 18. Wat is x?",
        antwoord=["5"],
        uitleg="x plus 4 is 9.",
    ),
    dict(
        type="invultekst",
        vraag="Een taxi vraagt 4 euro opstap en 1,5 euro per kilometer. Hoeveel kilometer rij je voor 19 euro?",
        antwoord=["10", "10 km"],
        uitleg="19 min 4 is 15, gedeeld door 1,5 is 10.",
    ),
]
