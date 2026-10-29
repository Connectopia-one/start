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
            r"beide leden vermenigvuldigen met \(-1\)",
            "bij beide leden hetzelfde getal optellen",
            "de linker- en het rechterlid van plaats verwisselen",
        ],
        antwoord=0,
        uitleg="Delen door nul is niet gedefinieerd. Delen door een letter mag wel, maar alleen als je weet dat ze niet nul is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De massadichtheid is \(\rho = \tfrac{m}{V}\). Hoe druk je de massa \(m\) uit?",
        opties=[
            r"\(m = \rho \cdot V\)",
            r"\(m = \tfrac{V}{\rho}\)",
            r"\(m = \tfrac{\rho}{V}\)",
            r"\(m = \rho + V\)",
        ],
        antwoord=0,
        uitleg=r"Je vermenigvuldigt beide leden met \(V\), en dan valt \(V\) rechts weg.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De wet van Ohm zegt \(U = R \cdot I\). Hoe druk je de weerstand \(R\) uit?",
        opties=[
            r"\(R = \tfrac{U}{I}\)",
            r"\(R = \tfrac{I}{U}\)",
            r"\(R = U \cdot I\)",
            r"\(R = U - I\)",
        ],
        antwoord=0,
        uitleg=r"Je deelt beide leden door \(I\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De zwaartekracht is \(F = m \cdot g\). Hoe bereken je de massa \(m\) uit een gegeven kracht?",
        opties=[
            r"\(m = \tfrac{F}{g}\)",
            r"\(m = F \cdot g\)",
            r"\(m = \tfrac{g}{F}\)",
            r"\(m = F + g\)",
        ],
        antwoord=0,
        uitleg=r"\(F = 98\) newton bij \(g \approx 9{,}8\) geeft \(m = 10\) kilogram.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Druk is \(p = \tfrac{F}{A}\). Wat gebeurt er als \(A\) kleiner wordt bij dezelfde \(F\)?",
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
        vraag=r"De formule voor de eenparig rechtlijnige beweging is \(x = x_{0} + v \cdot t\). Hoe druk je \(t\) uit?",
        opties=[
            r"\(t = \tfrac{x - x_{0}}{v}\)",
            r"\(t = \tfrac{x + x_{0}}{v}\)",
            r"\(t = \tfrac{v}{x - x_{0}}\)",
            r"\(t = x \cdot v - x_{0}\)",
        ],
        antwoord=0,
        uitleg=r"Eerst breng je \(x_{0}\) naar het andere lid, daarna deel je door \(v\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De kinetische energie is \(E_{k} = \tfrac{1}{2}mv^{2}\). Wat gebeurt er als \(v\) verdubbelt?",
        opties=[
            "de energie wordt vier keer zo groot",
            "de energie wordt twee keer zo groot",
            "de energie wordt half zo groot",
            "de energie blijft gelijk",
        ],
        antwoord=0,
        uitleg=r"\(v\) staat in het kwadraat, dus \((2v)^{2} = 4v^{2}\). Daarom groeit de remweg zo snel met de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De molaire concentratie is \(c = \tfrac{n}{V}\). Hoe bereken je het volume \(V\)?",
        opties=[
            r"\(V = \tfrac{n}{c}\)",
            r"\(V = n \cdot c\)",
            r"\(V = \tfrac{c}{n}\)",
            r"\(V = c + n\)",
        ],
        antwoord=0,
        uitleg="Dezelfde omvorming als bij de massadichtheid: de noemer en de uitkomst wisselen van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent het dat een formule lineair is in \(x\)?",
        opties=[
            r"\(x\) komt enkel in de eerste macht voor, zonder kwadraat of wortel",
            r"\(x\) staat altijd links van het gelijkheidsteken",
            "de grafiek gaat altijd door de oorsprong",
            r"er staat precies één \(x\) in de hele formule",
        ],
        antwoord=0,
        uitleg="De grafiek van een lineair verband is een rechte. Een zuiver kwadratisch verband geeft een parabool.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De oppervlakte van een vierkant is \(A = z^{2}\). Hoe druk je de zijde \(z\) uit?",
        opties=[
            r"\(z = \sqrt{A}\)",
            r"\(z = \tfrac{A}{2}\)",
            r"\(z = \tfrac{A}{4}\)",
            r"\(z = A^{2}\)",
        ],
        antwoord=0,
        uitleg=r"Delen door \(4\) zou de omtrek geven, niet de zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De veerkracht is \(F = k \cdot u\). Hoe bereken je de uitrekking \(u\)?",
        opties=[
            r"\(u = \tfrac{F}{k}\)",
            r"\(u = F \cdot k\)",
            r"\(u = \tfrac{k}{F}\)",
            r"\(u = F - k\)",
        ],
        antwoord=0,
        uitleg=r"Bij een stijve veer, dus een grote \(k\), geeft dezelfde kracht een kleinere uitrekking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je na het omvormen best met een getallenvoorbeeld?",
        opties=[
            "omdat een tekenfout of een verkeerde bewerking zo meteen opvalt",
            "omdat een formule pas geldt als je er getallen in gezet hebt",
            "omdat het examen dat verplicht bij elke omvorming",
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
        vraag=r"Als je beide leden van een gelijkheid met \(-1\) vermenigvuldigt, blijft de gelijkheid kloppen.",
        antwoord=True,
        uitleg="Alle tekens draaien om, maar links en rechts blijven gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="In de formule voor de kinetische energie is de energie recht evenredig met de snelheid.",
        antwoord=False,
        uitleg=r"Ze is recht evenredig met \(v^{2}\). Dat is iets heel anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lineair verband tussen twee grootheden geeft een rechte als grafiek.",
        antwoord=True,
        uitleg="Bij een recht evenredig verband gaat die rechte bovendien door de oorsprong.",
    ),
    dict(
        type="invultekst",
        vraag=r"Massadichtheid is \(\rho = \tfrac{m}{V}\). Wat is de massa van \(3\) liter water met \(\rho = 1\) kg per liter?",
        antwoord=["3", "3 kg", "3 kilogram"],
        uitleg=r"\(m = \rho \cdot V\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bij \(U = 12\) volt en \(I = 3\) ampère, hoeveel ohm is de weerstand?",
        antwoord=["4", "4 ohm"],
        uitleg=r"\(R = \tfrac{U}{I} = \tfrac{12}{3}\).",
    ),
    dict(
        type="invultekst",
        vraag=r"De oppervlakte van een vierkant is \(49\). Hoe lang is de zijde?",
        antwoord=["7"],
        uitleg=r"\(\sqrt{49} = 7\).",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(3x + 5 = 20\)?",
        opties=[r"\(x = 5\)", r"\(x = 15\)", r"\(x = \tfrac{25}{3}\)", r"\(x = 8\)"],
        antwoord=0,
        uitleg=r"Eerst \(5\) aftrekken aan beide kanten, dan door \(3\) delen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(2x - 7 = x + 3\)?",
        opties=[r"\(x = 10\)", r"\(x = 4\)", r"\(x = -10\)", r"\(x = \tfrac{3}{2}\)"],
        antwoord=0,
        uitleg=r"Breng \(x\) naar links en \(7\) naar rechts: \(x = 3 + 7\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat gebeurt er met het ongelijkheidsteken als je beide leden door \(-2\) deelt?",
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
        vraag=r"Wat is de oplossingenverzameling van \(-3x > 9\)?",
        opties=[
            r"alle \(x < -3\)",
            r"alle \(x > -3\)",
            r"alle \(x > 3\)",
            r"alle \(x < 3\)",
        ],
        antwoord=0,
        uitleg=r"Delen door \(-3\) draait het teken om: \(x < -3\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe noteer je \(x \leq 4\) als interval?",
        opties=[r"\(\left]-\infty, 4\right]\)", r"\(\left]-\infty, 4\right[\)",
                r"\(\left[4, +\infty\right[\)", r"\(\left]4, +\infty\right[\)"],
        antwoord=0,
        uitleg=r"De \(4\) hoort erbij, dus rechts een vierkant haakje naar binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het verband tussen de oplossing van \(f(x) = 0\) en de grafiek van \(f\)?",
        opties=[
            r"het is de \(x\)-waarde waar de grafiek de \(x\)-as snijdt",
            r"het is de \(y\)-waarde waar de grafiek de \(y\)-as snijdt",
            "het is de helling van de grafiek in dat punt",
            "het is het hoogste punt van de grafiek",
        ],
        antwoord=0,
        uitleg=r"Die \(x\)-waarde heet de nulwaarde, en het punt op de grafiek heet het nulpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De oplossing van \(f(x) > 0\) lees je af uit ...",
        opties=[
            "het tekenverloop: waar staat de functie positief?",
            "het verloopschema: waar stijgt de functie?",
            "de nulwaarde alleen, zonder verder te kijken",
            "het snijpunt met de y-as",
        ],
        antwoord=0,
        uitleg=r"Het tekenverloop zegt waar de grafiek boven en waar ze onder de \(x\)-as ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vergelijking geeft \(0 = 5\). Wat besluit je?",
        opties=[
            "de vergelijking heeft geen oplossing",
            "de vergelijking heeft oneindig veel oplossingen",
            r"\(x = 5\)",
            "je maakte zeker een rekenfout",
        ],
        antwoord=0,
        uitleg=r"Er blijft een onwaarheid over, dus geen enkele \(x\) voldoet. De oplossingenverzameling is \(\emptyset\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een vergelijking geeft \(0 = 0\). Wat besluit je?",
        opties=[
            r"elke waarde van \(x\) is een oplossing",
            "er is geen enkele oplossing",
            r"\(x = 0\)",
            "de vergelijking is fout opgeschreven",
        ],
        antwoord=0,
        uitleg=r"Er blijft een waarheid over, dus elke \(x\) voldoet.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een taxi vraagt \(4\) euro opstap en \(1{,}5\) euro per kilometer. Welke vergelijking hoort bij een rit van \(19\) euro?",
        opties=[
            r"\(4 + 1{,}5x = 19\)",
            r"\(4 \cdot 1{,}5x = 19\)",
            r"\(4x + 1{,}5 = 19\)",
            r"\(1{,}5 - 4x = 19\)",
        ],
        antwoord=0,
        uitleg=r"De opstap betaal je één keer, de kilometerprijs per kilometer. De rit is \(10\) kilometer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee abonnementen: A kost \(20\) euro plus \(0{,}10\) euro per minuut, B kost \(8\) euro plus \(0{,}20\) euro per minuut. Vanaf wanneer is A goedkoper?",
        opties=[
            r"vanaf meer dan \(120\) minuten",
            r"vanaf meer dan \(60\) minuten",
            r"vanaf meer dan \(40\) minuten",
            "A is altijd duurder dan B",
        ],
        antwoord=0,
        uitleg=r"Stel \(20 + 0{,}1x < 8 + 0{,}2x\). Dan \(12 < 0{,}1x\), dus \(x > 120\).",
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
        uitleg=r"De \(x\)-waarde van het snijpunt is de oplossing. Hebben de rechten geen snijpunt, dan is er geen oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de oplossing van \(\tfrac{x}{3} + 2 = 5\)?",
        opties=[r"\(x = 9\)", r"\(x = 21\)", r"\(x = 1\)", r"\(x = 15\)"],
        antwoord=0,
        uitleg=r"Eerst \(2\) aftrekken, dan met \(3\) vermenigvuldigen.",
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
        vraag=r"De nulwaarde van een functie is de \(x\)-waarde waarvoor de functiewaarde nul is.",
        antwoord=True,
        uitleg=r"Het bijhorende punt op de grafiek heet het nulpunt en ligt op de \(x\)-as.",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(5x - 3 = 12\). Wat is \(x\)?",
        antwoord=["3"],
        uitleg=r"\(5x = 15\), dus \(x = 3\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Los op: \(2(x + 4) = 18\). Wat is \(x\)?",
        antwoord=["5"],
        uitleg=r"\(x + 4 = 9\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een taxi vraagt \(4\) euro opstap en \(1{,}5\) euro per kilometer. Hoeveel kilometer rij je voor \(19\) euro?",
        antwoord=["10", "10 km"],
        uitleg=r"\(19 - 4 = 15\), en \(15 : 1{,}5 = 10\).",
    ),
]
