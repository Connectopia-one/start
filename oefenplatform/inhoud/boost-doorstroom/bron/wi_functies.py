# -*- coding: utf-8 -*-
"""De vragen voor "Functies en de rechte".

Uit de bouwsteen Relaties en verandering: het functiebegrip met functiewaarde,
afhankelijke en onafhankelijke variabele, domein en bereik, de vier
voorstellingswijzen (verwoording, tabel, grafiek en voorschrift) en het verband
ertussen, en daarnaast de eerstegraadsfunctie: het voorschrift f(x) is ax plus
b, het lineaire en het recht evenredige verband, lineaire groei, de
richtingscoëfficiënt en het snijpunt met de y-as, en het opstellen van de
vergelijking van een rechte uit een richtingscoëfficiënt met een punt of uit
twee punten.

De modellen die de fiche noemt komen als context terug: de rechtlijnige
beweging met constante snelheid, vaste en variabele kosten, hydrostatische
druk, energiegebruik en afschrijving.

Deel 1 is het functiebegrip. Deel 2 is de rechte.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer is een verband een functie?",
        opties=[
            "als bij elke x hoogstens één y hoort",
            "als bij elke y hoogstens één x hoort",
            "als de grafiek een rechte is",
            "als x en y allebei positief zijn",
        ],
        antwoord=0,
        uitleg="Een verticale lijn mag de grafiek dus maar één keer snijden. Dat heet de verticalelijntest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke variabele is bij 'de kost hangt af van het aantal kilometer' de onafhankelijke?",
        opties=[
            "het aantal kilometer",
            "de kost",
            "allebei even sterk",
            "dat kan je niet bepalen",
        ],
        antwoord=0,
        uitleg="De onafhankelijke variabele kies je zelf, de afhankelijke volgt eruit. Ze staat op de horizontale as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van een functie?",
        opties=[
            "de verzameling van alle x-waarden waarvoor de functie een waarde geeft",
            "de verzameling van alle y-waarden die de functie aanneemt",
            "de verzameling van de nulwaarden van de functie",
            "de verzameling van alle punten op de grafiek",
        ],
        antwoord=0,
        uitleg="Het bereik is de tegenhanger: dat zijn de y-waarden die er uitkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bereik van een functie?",
        opties=[
            "de verzameling van alle y-waarden die de functie aanneemt",
            "de verzameling van alle x-waarden waarvoor ze bestaat",
            "de afstand tussen de kleinste en de grootste x-waarde",
            "het aantal snijpunten met de x-as",
        ],
        antwoord=0,
        uitleg="Op de grafiek lees je het bereik af door naar de verticale as te kijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier voorstellingswijzen van een functie noemt de fiche?",
        opties=[
            "verwoording, tabel, grafiek en voorschrift",
            "formule, tekening, verhaal en schema",
            "grafiek, diagram, tabel en histogram",
            "voorschrift, nulwaarde, top en domein",
        ],
        antwoord=0,
        uitleg="Je moet van elke vorm naar elke andere kunnen overstappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor f(x) is 3x min 2, hoeveel is f(4)?",
        opties=["10", "14", "5", "12"],
        antwoord=0,
        uitleg="3 maal 4 is 12, min 2 is 10.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor f(x) is 3x min 2, voor welke x is f(x) gelijk aan 13?",
        opties=["5", "11", "4", "39"],
        antwoord=0,
        uitleg="3x is 15, dus x is 5. Je lost een vergelijking op in plaats van in te vullen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het domein van de functie f(x) is 1 op x?",
        opties=[
            "alle reële getallen behalve nul",
            "alle positieve reële getallen",
            "alle reële getallen",
            "alle gehele getallen behalve nul",
        ],
        antwoord=0,
        uitleg="Delen door nul mag niet, dus x is nul valt weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een recht evenredig verband tussen twee grootheden?",
        opties=[
            "als de ene verdubbelt, verdubbelt de andere ook",
            "als de ene verdubbelt, wordt de andere half zo groot",
            "de som van de twee blijft altijd gelijk",
            "het verschil van de twee blijft altijd gelijk",
        ],
        antwoord=0,
        uitleg="De grafiek is een rechte door de oorsprong, met voorschrift y is ax.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een lineair en een recht evenredig verband?",
        opties=[
            "een recht evenredig verband gaat door de oorsprong, een lineair verband niet noodzakelijk",
            "een lineair verband gaat door de oorsprong, een recht evenredig verband niet",
            "er is geen verschil tussen de twee",
            "een lineair verband heeft altijd een negatieve helling",
        ],
        antwoord=0,
        uitleg="Bij y is 2x plus 5 is het verband lineair maar niet recht evenredig: bij nul kilometer betaal je al 5 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel geeft bij x is 1, 2, 3 de waarden 4, 7, 10. Wat voor groei is dat?",
        opties=[
            "lineaire groei, want er komt telkens 3 bij",
            "kwadratische groei, want de verschillen stijgen",
            "omgekeerd evenredig, want de waarden stijgen",
            "geen enkel herkenbaar verband",
        ],
        antwoord=0,
        uitleg="Bij lineaire groei is het verschil per stap constant. Het voorschrift is 3x plus 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel geeft bij x is 1, 2, 3 de waarden 1, 4, 9. Wat voor groei is dat?",
        opties=[
            "niet-lineaire groei, want de verschillen worden groter",
            "lineaire groei, want de waarden stijgen elke stap",
            "omgekeerd evenredige groei",
            "constante groei zonder toename",
        ],
        antwoord=0,
        uitleg="De verschillen zijn 3 en 5, dus geen rechte. Dit is het kwadratische verband y is x kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort bij een grafiek altijd een ijk op de assen?",
        opties=[
            "zonder ijk kan je geen enkele waarde aflezen",
            "omdat de grafiek anders niet op het blad past",
            "omdat de fiche dat verplicht voor elke tekening",
            "om te tonen welke variabele afhankelijk is",
        ],
        antwoord=0,
        uitleg="Een grafiek zonder ijk toont enkel een vorm en geen getallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een functie mag dezelfde y-waarde bij meerdere x-waarden horen.",
        antwoord=True,
        uitleg="Dat is geen probleem: bij y is x kwadraat hoort y is 4 bij zowel x is 2 als x is min 2.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een functie mogen bij dezelfde x-waarde twee verschillende y-waarden horen.",
        antwoord=False,
        uitleg="Dan is het geen functie meer. Een verticale lijn zou de grafiek twee keer snijden.",
    ),
    dict(
        type="waarofniet",
        vraag="De afhankelijke variabele staat op de verticale as.",
        antwoord=True,
        uitleg="De onafhankelijke, die je zelf kiest, staat op de horizontale as.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk lineair verband is ook recht evenredig.",
        antwoord=False,
        uitleg="Alleen als het door de oorsprong gaat, dus als b gelijk is aan nul.",
    ),
    dict(
        type="invultekst",
        vraag="Voor f(x) is 2x plus 7, hoeveel is f(5)?",
        antwoord=["17"],
        uitleg="10 plus 7.",
    ),
    dict(
        type="invultekst",
        vraag="Voor f(x) is 4x min 1, voor welke x is f(x) gelijk aan 11?",
        antwoord=["3"],
        uitleg="4x is 12.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de verzameling van alle y-waarden die een functie aanneemt?",
        antwoord=["bereik", "het bereik"],
        uitleg="De x-waarden vormen het domein.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent de a in het voorschrift f(x) is ax plus b?",
        opties=[
            "de richtingscoëfficiënt: hoeveel y stijgt per eenheid x",
            "de hoogte waarop de rechte de y-as snijdt",
            "de x-waarde waar de rechte de x-as snijdt",
            "de hoek die de rechte met de x-as maakt, in graden",
        ],
        antwoord=0,
        uitleg="Is a gelijk aan 3, dan gaat de rechte drie omhoog per stap naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de b in het voorschrift f(x) is ax plus b?",
        opties=[
            "de y-waarde waar de rechte de verticale as snijdt",
            "de helling van de rechte",
            "de nulwaarde van de functie",
            "het aantal snijpunten met de x-as",
        ],
        antwoord=0,
        uitleg="Vul x is nul in en je houdt b over. Bij een taxirit is b de opstapprijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de richtingscoëfficiënt van de rechte door (1, 2) en (4, 11)?",
        opties=["3", "9", "min 3", "1 op 3"],
        antwoord=0,
        uitleg="Het verschil in y gedeeld door het verschil in x: 9 gedeeld door 3.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de richtingscoëfficiënt van de rechte door (0, 5) en (2, 1)?",
        opties=["min 2", "2", "min 4", "4"],
        antwoord=0,
        uitleg="Het verschil in y is min 4 over een verschil in x van 2. De rechte daalt dus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het voorschrift van de rechte met richtingscoëfficiënt 2 door het punt (0, 3)?",
        opties=["y is 2x plus 3", "y is 3x plus 2", "y is 2x min 3", "y is 2x"],
        antwoord=0,
        uitleg="Het punt ligt op de y-as, dus je kan b meteen aflezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het voorschrift van de rechte met richtingscoëfficiënt 4 door het punt (1, 6)?",
        opties=["y is 4x plus 2", "y is 4x plus 6", "y is 4x min 2", "y is 6x plus 4"],
        antwoord=0,
        uitleg="Vul in: 6 is 4 maal 1 plus b, dus b is 2.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je van een rechte met richtingscoëfficiënt nul?",
        opties=[
            "ze loopt horizontaal",
            "ze loopt verticaal",
            "ze gaat door de oorsprong",
            "ze bestaat niet",
        ],
        antwoord=0,
        uitleg="De y-waarde verandert niet als x verandert. Het voorschrift is dan y is b.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee rechten zijn evenwijdig. Wat weet je over hun richtingscoëfficiënten?",
        opties=[
            "ze zijn gelijk",
            "ze zijn tegengesteld",
            "hun product is min één",
            "ze zijn allebei nul",
        ],
        antwoord=0,
        uitleg="Bij loodrechte rechten is het product van de richtingscoëfficiënten wel min één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fietser rijdt aan 18 kilometer per uur en is al 5 kilometer ver. Welk voorschrift hoort bij de afgelegde weg?",
        opties=["s is 18t plus 5", "s is 5t plus 18", "s is 18t min 5", "s is 23t"],
        antwoord=0,
        uitleg="Dit is de eenparig rechtlijnige beweging: de beginpositie is b en de snelheid is de richtingscoëfficiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een drukkerij rekent 60 euro opstartkosten plus 0,40 euro per affiche. Wat is het voorschrift van de totale kost?",
        opties=["k is 0,40n plus 60", "k is 60n plus 0,40", "k is 60,40n", "k is 0,40n min 60"],
        antwoord=0,
        uitleg="De opstartkosten zijn de vaste kosten en dus de b. De prijs per stuk is de richtingscoëfficiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een machine van 20 000 euro wordt in tien jaar lineair afgeschreven tot nul. Hoeveel is ze na vier jaar waard?",
        opties=["12 000 euro", "8 000 euro", "16 000 euro", "10 000 euro"],
        antwoord=0,
        uitleg="Per jaar 2000 euro minder. Na vier jaar is dat 8000 euro minder dan 20 000.",
    ),
    dict(
        type="meerkeuze",
        vraag="De hydrostatische druk stijgt met ongeveer 1 bar per 10 meter diepte, bovenop 1 bar aan de oppervlakte. Welke druk hoort bij 30 meter?",
        opties=["4 bar", "3 bar", "30 bar", "31 bar"],
        antwoord=0,
        uitleg="1 bar lucht plus 3 bar water. Het verband is lineair maar niet recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar snijdt de rechte y is 2x min 8 de x-as?",
        opties=["in (4, 0)", "in (0, 4)", "in (min 4, 0)", "in (0, min 8)"],
        antwoord=0,
        uitleg="Stel y gelijk aan nul: 2x is 8, dus x is 4. Het punt (0, min 8) is het snijpunt met de y-as.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rechte met een negatieve richtingscoëfficiënt daalt van links naar rechts.",
        antwoord=True,
        uitleg="Hoe groter x, hoe kleiner y.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verticale rechte is de grafiek van een functie.",
        antwoord=False,
        uitleg="Bij één x-waarde horen dan oneindig veel y-waarden, en dat mag niet bij een functie.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee punten volstaan om de vergelijking van een rechte te bepalen.",
        antwoord=True,
        uitleg="Uit de twee punten haal je de richtingscoëfficiënt, en daarna vul je één punt in om b te vinden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij vaste en variabele kosten samen is de totale kost recht evenredig met het aantal stuks.",
        antwoord=False,
        uitleg="Door de vaste kosten gaat de rechte niet door de oorsprong. Het verband is wel lineair.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de richtingscoëfficiënt van de rechte door (2, 3) en (5, 12)?",
        antwoord=["3"],
        uitleg="9 gedeeld door 3.",
    ),
    dict(
        type="invultekst",
        vraag="Waar snijdt de rechte y is 3x min 12 de x-as? Geef de x-waarde.",
        antwoord=["4"],
        uitleg="Stel y gelijk aan nul.",
    ),
    dict(
        type="invultekst",
        vraag="Een machine van 20 000 euro wordt in tien jaar lineair afgeschreven. Hoeveel euro per jaar?",
        antwoord=["2000", "2 000", "2000 euro"],
        uitleg="20 000 gedeeld door 10.",
    ),
]
