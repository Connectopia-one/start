# -*- coding: utf-8 -*-
"""Veeltermen: deelbaarheid, de reststelling en het rekenschema van Horner.

Het onderdeel "Deelbaarheid" van de analysefiche G1, aangevuld met het
ontbinden in factoren dat daar uitdrukkelijk bij staat. De fiche vraagt dit
alleen in opgaven zonder context, dus hier staan geen verhaaltjes bij.

Deel 1 is de deling zelf: euclidisch delen, de reststelling en Horner.
Deel 2 is ontbinden in factoren en nulwaarden zoeken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat weet je zeker over de rest bij een euclidische deling van veeltermen?",
        opties=[
            "haar graad is kleiner dan die van de deler",
            "haar graad is kleiner dan die van het quotiënt",
            "haar graad is gelijk aan die van de deler zelf",
            "haar graad is kleiner dan die van het deeltal",
        ],
        antwoord=0,
        uitleg="Zodra de rest nog even hoog in graad is als de deler, kan je verder delen. Je stopt pas als dat niet meer kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband geldt altijd tussen deeltal, deler, quotiënt en rest?",
        opties=[
            "deeltal is deler maal quotiënt plus rest",
            "deeltal is deler plus quotiënt maal de rest",
            "deeltal is deler maal quotiënt min de rest",
            "deeltal is quotiënt plus deler plus de rest",
        ],
        antwoord=0,
        uitleg="Dat is de controle op elke deling. Werkt ze niet, dan zit er een rekenfout in je schema.",
    ),
    dict(
        type="invultekst",
        vraag="Je deelt een veelterm door een tweedegraadsveelterm. Welke graad heeft de rest hoogstens? Schrijf het cijfer.",
        antwoord=["1", "een", "één"],
        uitleg="De graad van de rest ligt strikt onder die van de deler, dus hoogstens één.",
    ),
    dict(
        type="waarofniet",
        vraag="De rest bij de deling van een veelterm P door x min a is gelijk aan P van a.",
        antwoord=True,
        uitleg="Dat is de reststelling. Je hoeft dus niet te delen om de rest te kennen: invullen volstaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je deelt x tot de derde min twee x kwadraat plus drie x min vier door x min één. Wat is de rest?",
        opties=["min twee", "min vier", "nul", "twee"],
        antwoord=0,
        uitleg="Vul één in: één min twee plus drie min vier is min twee. De reststelling geeft meteen het antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je het rekenschema van Horner?",
        opties=[
            "om te delen door een tweeterm x min a",
            "om een tweedegraadsvergelijking op te lossen",
            "om een breuk met wortels te vereenvoudigen",
            "om de afgeleide van een veelterm te vinden",
        ],
        antwoord=0,
        uitleg="Horner is een snelle schrijfwijze voor precies die ene deling. Voor andere delers val je terug op de gewone staartdeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan het rekenschema van Horner ook gebruiken om te delen door x kwadraat plus één.",
        antwoord=False,
        uitleg="Horner werkt enkel bij een deler van de vorm x min a. Voor een deler van hogere graad gebruik je de euclidische deling.",
    ),
    dict(
        type="invultekst",
        vraag="Neem de veelterm x tot de derde min acht. Hoeveel is haar waarde voor x gelijk aan twee? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Twee tot de derde is acht, en acht min acht is nul. Dus x min twee is een deler.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat weet je als de waarde van een veelterm P in a gelijk is aan nul?",
        opties=[
            "x min a is een deler van P",
            "x plus a is een deler van P",
            "de veelterm P heeft graad nul",
            "de veelterm P is overal gelijk aan nul",
        ],
        antwoord=0,
        uitleg="Volgens de reststelling is de rest dan nul, en een deling met rest nul gaat op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een veelterm van graad n heeft hoogstens n reële nulwaarden.",
        antwoord=True,
        uitleg="Elke nulwaarde levert een factor van graad één op, en samen kunnen die de graad niet overschrijden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je deelt met Horner door x plus drie. Welk getal zet je links in het schema?",
        opties=["min drie", "plus drie", "min één", "nul"],
        antwoord=0,
        uitleg="x plus drie is x min min drie, dus a is min drie. Het tekenfoutje hier is de klassieker van dit hoofdstuk.",
    ),
    dict(
        type="invultekst",
        vraag="De waarde van P in a is zeven. Wat is de rest bij de deling van P door x min a? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg="De reststelling zegt dat de rest net die functiewaarde is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je deelt een vijfdegraadsveelterm door een tweedegraadsveelterm. Welke graad heeft het quotiënt?",
        opties=["drie", "twee", "vier", "vijf"],
        antwoord=0,
        uitleg="De graden trekken af: vijf min twee is drie.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een deling van veeltermen opgaat, is de rest gelijk aan de graad van de deler.",
        antwoord=False,
        uitleg="Als een deling opgaat is de rest nul. Een rest is een veelterm, geen graad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nulwaarde van een veeltermfunctie?",
        opties=[
            "een x waarvoor de functiewaarde nul is",
            "de waarde die de functie in nul aanneemt",
            "het punt waar de grafiek de y-as snijdt",
            "de kleinste waarde die de functie bereikt",
        ],
        antwoord=0,
        uitleg="Op de grafiek zijn dat de snijpunten met de x-as. De waarde in nul is iets anders: dat is het snijpunt met de y-as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze veeltermen is deelbaar door x min één?",
        opties=[
            "x kwadraat plus twee x min drie",
            "x kwadraat plus twee x plus drie",
            "x kwadraat min twee x min drie",
            "x kwadraat plus drie x plus twee",
        ],
        antwoord=0,
        uitleg="Vul telkens één in. Alleen bij de eerste krijg je één plus twee min drie, dus nul.",
    ),
    dict(
        type="waarofniet",
        vraag="De reststelling werkt ook bij een deler van de vorm x plus a.",
        antwoord=True,
        uitleg="Je schrijft x plus a als x min min a en vult dan min a in.",
    ),
    dict(
        type="invultekst",
        vraag="Neem twee x kwadraat min drie x plus één. Hoeveel is de waarde voor x gelijk aan één? Schrijf het getal.",
        antwoord=["0", "nul"],
        uitleg="Twee min drie plus één is nul, dus x min één is een deler.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel getallen zet je bovenaan in het schema van Horner voor een derdegraadsveelterm?",
        opties=["vier", "drie", "twee", "vijf"],
        antwoord=0,
        uitleg="Alle coëfficiënten van graad drie tot en met de constante term, dus vier. Een ontbrekende graad schrijf je als nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt het laatste getal onderaan het schema van Horner voor?",
        opties=[
            "de rest van de deling",
            "de hoogste term van het quotiënt",
            "de nulwaarde van de veelterm zelf",
            "de graad die het quotiënt zal hebben",
        ],
        antwoord=0,
        uitleg="De getallen links daarvan zijn de coëfficiënten van het quotiënt. Het laatste is de rest, en dus ook de functiewaarde in a.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ontbind je x kwadraat min negen in factoren?",
        opties=[
            "x min drie, maal x plus drie",
            "x min drie, maal x min drie",
            "x plus drie, maal x plus drie",
            "x min negen, maal x plus één",
        ],
        antwoord=0,
        uitleg="Dat is het verschil van twee kwadraten: a kwadraat min b kwadraat is a min b maal a plus b.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan is a plus b, in het kwadraat, gelijk?",
        opties=[
            "a kwadraat plus twee ab plus b kwadraat",
            "a kwadraat plus b kwadraat zonder meer",
            "a kwadraat min twee ab plus b kwadraat",
            "twee maal a plus twee maal b, in het kwadraat",
        ],
        antwoord=0,
        uitleg="De dubbele term twee ab vergeten is de meest gemaakte fout van het hoofdstuk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel reële nulwaarden heeft x kwadraat min vier? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="Twee en min twee, want de ontbinding is x min twee maal x plus twee.",
    ),
    dict(
        type="waarofniet",
        vraag="De veelterm x kwadraat plus vier valt in de reële getallen uiteen in twee factoren van graad één.",
        antwoord=False,
        uitleg="Haar discriminant is negatief, dus ze heeft geen reële nulwaarden en blijft onontbindbaar in R. In de complexe getallen lukt het wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zondert de gemeenschappelijke factor af in drie x tot de derde min zes x kwadraat. Wat krijg je?",
        opties=[
            "drie x kwadraat, maal x min twee",
            "drie x kwadraat, maal x min zes",
            "drie x, maal x kwadraat min twee x",
            "x kwadraat, maal drie x min zes x",
        ],
        antwoord=0,
        uitleg="Drie en x kwadraat zitten in beide termen. Wat overblijft is x min twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontbind je x tot de derde min acht?",
        opties=[
            "x min twee, maal x kwadraat plus twee x plus vier",
            "x min twee, maal x kwadraat min twee x plus vier",
            "x min twee, maal x kwadraat plus twee x min vier",
            "x plus twee, maal x kwadraat plus twee x plus vier",
        ],
        antwoord=0,
        uitleg="Twee is een nulwaarde, dus x min twee is een deler. Horner geeft als quotiënt x kwadraat plus twee x plus vier.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de nulwaarde van twee x min zes? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="Twee x min zes is nul als x gelijk is aan drie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een veelterm ontbinden in factoren is een manier om haar nulwaarden te vinden.",
        antwoord=True,
        uitleg="Een product is nul zodra één factor nul is, dus elke factor levert meteen een nulwaarde op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je neemt termen samen in ax plus ay plus bx plus by. Wat krijg je?",
        opties=[
            "a plus b, maal x plus y",
            "a plus x, maal b plus y",
            "a maal b, plus x maal y",
            "a plus b plus x plus y, in het kwadraat",
        ],
        antwoord=0,
        uitleg="Eerst a buiten de eerste twee en b buiten de laatste twee, dan de gemeenschappelijke factor x plus y afzonderen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de discriminant van x kwadraat min vijf x plus zes? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="Vijfentwintig min vierentwintig is één. Positief, dus er zijn twee reële nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontbind je x kwadraat min vijf x plus zes?",
        opties=[
            "x min twee, maal x min drie",
            "x plus twee, maal x plus drie",
            "x min één, maal x min zes",
            "x min twee, maal x plus drie",
        ],
        antwoord=0,
        uitleg="Je zoekt twee getallen met som vijf en product zes: dat zijn twee en drie, allebei met een minteken in de factor.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tweedegraadsveelterm met een negatieve discriminant heeft twee reële nulwaarden.",
        antwoord=False,
        uitleg="Bij een negatieve discriminant zijn er geen reële nulwaarden en raakt of snijdt de parabool de x-as niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt een nulwaarde van een derdegraadsveelterm met gehele coëfficiënten. Welke getallen probeer je eerst?",
        opties=[
            "de delers van de constante term",
            "de delers van de hoogste coëfficiënt",
            "de getallen tussen min tien en tien",
            "de kwadraten van de coëfficiënten",
        ],
        antwoord=0,
        uitleg="Een gehele nulwaarde moet de constante term delen. Dat zijn er meestal maar een handvol om te testen.",
    ),
    dict(
        type="waarofniet",
        vraag="a min b, in het kwadraat, is gelijk aan a kwadraat min twee ab plus b kwadraat.",
        antwoord=True,
        uitleg="Alleen de middelste term wisselt van teken. De laatste term blijft positief, want min b in het kwadraat is plus b kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe schrijf je vier x kwadraat min twaalf x plus negen als één kwadraat?",
        opties=[
            "twee x min drie, in het kwadraat",
            "twee x plus drie, in het kwadraat",
            "vier x min drie, in het kwadraat",
            "twee x min negen, in het kwadraat",
        ],
        antwoord=0,
        uitleg="De dubbele term is twee maal twee x maal drie, dus twaalf x, en die is hier negatief.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van de nulwaarden van x kwadraat min zeven x plus twaalf? Schrijf het getal.",
        antwoord=["7", "zeven"],
        uitleg="De nulwaarden zijn drie en vier. De som is min b op a, dus zeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel reële nulwaarden heeft x tot de derde min x?",
        opties=["drie", "twee", "één", "geen"],
        antwoord=0,
        uitleg="Zonder x afzonderen krijg je x maal x min één maal x plus één. De nulwaarden zijn nul, één en min één.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke veelterm van oneven graad heeft minstens één reële nulwaarde.",
        antwoord=True,
        uitleg="Bij een oneven graad gaat de functie van min oneindig naar plus oneindig, dus ze moet de x-as kruisen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontbind je x tot de vierde min zestien zo ver mogelijk in R?",
        opties=[
            "x min twee, maal x plus twee, maal x kwadraat plus vier",
            "x min twee, maal x plus twee, maal x kwadraat min vier",
            "x min vier, maal x plus vier, maal x kwadraat plus één",
            "x min twee, maal x plus twee, maal x min twee, maal x plus twee",
        ],
        antwoord=0,
        uitleg="Eerst het verschil van kwadraten, dan nog eens op x kwadraat min vier. De factor x kwadraat plus vier blijft staan, want die heeft geen reële nulwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontbind je een veelterm in factoren?",
        opties=[
            "om haar nulwaarden en delers te zien",
            "om haar graad met één te verlagen",
            "om haar afgeleide sneller te berekenen",
            "om haar grafiek naar boven te schuiven",
        ],
        antwoord=0,
        uitleg="Uit de factoren lees je de nulwaarden rechtstreeks af, en je ziet meteen door welke tweetermen de veelterm deelbaar is.",
    ),
]
