# -*- coding: utf-8 -*-
"""Complexe getallen.

Het onderdeel "Complexe getallen" van fiche G2, achttien procent van dat
examen. Er zijn drie voorstellingswijzen die je door elkaar moet kunnen
gebruiken: het vlak van Gauss, de cartesische vorm en de goniometrische vorm.

Deel 1 is de cartesische vorm en het vlak van Gauss.
Deel 2 is de goniometrische vorm, de formule van de Moivre en het oplossen
van vergelijkingen in de complexe getallen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de imaginaire eenheid i?",
        opties=[
            "het getal waarvan het kwadraat min één is",
            "het getal waarvan het kwadraat één is",
            "de vierkantswortel uit het getal één",
            "een ander woord voor het getal oneindig",
        ],
        antwoord=0,
        uitleg="Met i erbij heeft elke tweedegraadsvergelijking oplossingen, ook als de discriminant negatief is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het reëel deel van drie min vijf i?",
        opties=["drie", "min vijf", "vijf", "min drie"],
        antwoord=0,
        uitleg="Het reëel deel is het getal zonder i. Het imaginair deel is min vijf, dus zonder de i erbij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is i tot de vierde macht? Schrijf het getal.",
        antwoord=["1", "een", "één"],
        uitleg="i in het kwadraat is min één, en min één in het kwadraat is één. De machten van i herhalen zich dus om de vier.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk reëel getal is ook een complex getal.",
        antwoord=True,
        uitleg="Het is dan een complex getal met imaginair deel nul. De reële getallen liggen op de horizontale as van het vlak van Gauss.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het toegevoegde complexe getal van twee plus drie i?",
        opties=[
            "twee min drie i",
            "min twee plus drie i",
            "min twee min drie i",
            "drie plus twee i",
        ],
        antwoord=0,
        uitleg="Alleen het imaginair deel wisselt van teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is de modulus van drie plus vier i?",
        opties=["vijf", "zeven", "twaalf", "één"],
        antwoord=0,
        uitleg="De modulus is de afstand tot de oorsprong, dus de wortel uit negen plus zestien.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan twee complexe getallen van klein naar groot ordenen.",
        antwoord=False,
        uitleg="De complexe getallen zijn niet geordend. Hun moduli kan je wel vergelijken, maar de getallen zelf niet.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het imaginair deel van zeven min twee i? Schrijf het getal.",
        antwoord=["-2", "min 2"],
        uitleg="Het imaginair deel is het getal bij i, dus min twee, en niet min twee i.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is twee plus drie i, plus één min i?",
        opties=[
            "drie plus twee i",
            "drie plus vier i",
            "één plus twee i",
            "twee plus twee i",
        ],
        antwoord=0,
        uitleg="Je telt de reële delen samen en de imaginaire delen samen, net als bij vectoren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een complex getal maal zijn toegevoegde is altijd een reëel getal.",
        antwoord=True,
        uitleg="Je krijgt het kwadraat van de modulus, dus een niet-negatief reëel getal. Daarom gebruik je de toegevoegde net om te delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe deel je door een complex getal in cartesische vorm?",
        opties=[
            "teller en noemer vermenigvuldigen met de toegevoegde van de noemer",
            "teller en noemer vermenigvuldigen met de noemer zelf, onveranderd",
            "het reëel deel en het imaginair deel apart delen",
            "de modulus delen en het argument gelijk laten",
        ],
        antwoord=0,
        uitleg="De noemer wordt dan reëel en je kan gewoon verder rekenen. Apart delen werkt niet, net zoals bij een breuk met een wortel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de modulus van vijf i? Schrijf het getal.",
        antwoord=["5", "vijf"],
        uitleg="Het punt ligt vijf eenheden boven de oorsprong op de imaginaire as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op de verticale as van het vlak van Gauss?",
        opties=[
            "het imaginair deel van het getal",
            "het reëel deel van het getal",
            "de modulus van het getal",
            "het argument van het getal",
        ],
        antwoord=0,
        uitleg="Horizontaal het reëel deel, verticaal het imaginair deel. Elk complex getal is dus een punt in het vlak.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zuiver imaginair getal heeft reëel deel nul.",
        antwoord=True,
        uitleg="Het ligt dan op de verticale as. Een zuiver reëel getal heeft net imaginair deel nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is één plus i, in het kwadraat?",
        opties=["twee i", "twee", "min twee", "één plus twee i"],
        antwoord=0,
        uitleg="Werk uit: één plus twee i plus i in het kwadraat. Dat laatste is min één, dus blijft twee i over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het argument van een complex getal?",
        opties=[
            "de hoek met de positieve reële as",
            "de afstand tot de oorsprong van het vlak",
            "het reëel deel gedeeld door het imaginair deel",
            "het aantal cijfers na de komma in de modulus",
        ],
        antwoord=0,
        uitleg="De afstand tot de oorsprong is net de modulus. Samen leggen modulus en argument het getal volledig vast.",
    ),
    dict(
        type="waarofniet",
        vraag="i tot de derde macht is gelijk aan i.",
        antwoord=False,
        uitleg="i tot de derde is i kwadraat maal i, dus min één maal i, en dat is min i. Pas i tot de vijfde is weer i.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is i tot de derde macht? Schrijf het antwoord.",
        antwoord=["-i", "min i"],
        uitleg="i kwadraat is min één, en dat maal i geeft min i.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelt de optelling van twee complexe getallen voor in het vlak van Gauss?",
        opties=[
            "dezelfde constructie als het optellen van twee vectoren",
            "een draaiing van het ene getal rond het andere getal",
            "een vermenigvuldiging van de twee afstanden",
            "een spiegeling om de horizontale reële as",
        ],
        antwoord=0,
        uitleg="Je legt de pijlen achter elkaar. Draaien hoort bij vermenigvuldigen, niet bij optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een punt in het vlak van Gauss als je het toegevoegde getal neemt?",
        opties=[
            "het spiegelt om de horizontale as",
            "het spiegelt om de verticale as",
            "het draait een halve slag rond de oorsprong",
            "het blijft precies op dezelfde plaats staan",
        ],
        antwoord=0,
        uitleg="Alleen het imaginair deel wisselt van teken, dus het punt klapt om over de reële as.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ziet de goniometrische vorm van een complex getal eruit?",
        opties=[
            "de modulus maal de cosinus van het argument plus i maal de sinus ervan",
            "het reëel deel maal de cosinus plus het imaginair deel maal de sinus",
            "de modulus maal het argument, plus i maal de modulus",
            "de cosinus van de modulus plus i maal de sinus van de modulus",
        ],
        antwoord=0,
        uitleg="Zo zie je de twee gegevens die een complex getal vastleggen meteen staan: hoe ver en onder welke hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vermenigvuldigt twee complexe getallen in goniometrische vorm. Wat doe je?",
        opties=[
            "de moduli vermenigvuldigen en de argumenten optellen",
            "de moduli optellen en de argumenten vermenigvuldigen",
            "de moduli en de argumenten allebei vermenigvuldigen",
            "de moduli en de argumenten allebei bij elkaar optellen",
        ],
        antwoord=0,
        uitleg="Vermenigvuldigen is dus uitrekken en draaien tegelijk. Bij delen deel je de moduli en trek je de argumenten af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel oplossingen heeft de vergelijking z tot de derde is acht in de complexe getallen? Schrijf het cijfer.",
        antwoord=["3", "drie"],
        uitleg="Een vergelijking van de vorm z tot de macht n is a heeft er altijd precies n. Twee is er één van; de twee andere zijn niet reëel.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het delen van twee complexe getallen in goniometrische vorm trek je de argumenten af.",
        antwoord=True,
        uitleg="En de moduli deel je. Delen is dus krimpen en terugdraaien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de formule van de Moivre?",
        opties=[
            "je verheft de modulus tot de macht n en vermenigvuldigt het argument met n",
            "je vermenigvuldigt de modulus met n en verheft het argument tot de macht n",
            "je verheft zowel de modulus als het argument tot de macht n",
            "je verheft de modulus tot de macht n en laat het argument gelijk",
        ],
        antwoord=0,
        uitleg="Ze volgt rechtstreeks uit de regel voor vermenigvuldigen, n keer na elkaar toegepast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar liggen de n oplossingen van z tot de macht n is a in het vlak van Gauss?",
        opties=[
            "op één cirkel, gelijkmatig over de omtrek verdeeld",
            "op één rechte door de oorsprong van het hele vlak",
            "allemaal op de horizontale reële as samen",
            "willekeurig verspreid, zonder vast patroon",
        ],
        antwoord=0,
        uitleg="Ze hebben allemaal dezelfde modulus, en hun argumenten verschillen telkens evenveel. Ze vormen dus de hoekpunten van een regelmatige veelhoek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tweedegraadsvergelijking met een negatieve discriminant heeft geen oplossingen in de complexe getallen.",
        antwoord=False,
        uitleg="Ze heeft er net twee. Daarvoor werden de complexe getallen ingevoerd. In de reële getallen zijn er inderdaad geen.",
    ),
    dict(
        type="invultekst",
        vraag="Los op in de complexe getallen: x kwadraat plus één is nul. Schrijf de oplossing met het plusteken.",
        antwoord=["i"],
        uitleg="x kwadraat is min één, dus x is i of min i.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de oplossingen van x kwadraat min twee x plus vijf is nul?",
        opties=[
            "één plus twee i en één min twee i",
            "twee plus i en twee min i",
            "min één plus twee i en min één min twee i",
            "één plus vier i en één min vier i",
        ],
        antwoord=0,
        uitleg="De discriminant is vier min twintig, dus min zestien. De wortel daaruit is vier i, en gedeeld door twee geeft dat twee i.",
    ),
    dict(
        type="waarofniet",
        vraag="De twee complexe oplossingen van een tweedegraadsvergelijking met reële coëfficiënten zijn elkaars toegevoegde.",
        antwoord=True,
        uitleg="Ze verschillen alleen in het teken voor de wortel uit de discriminant, en die wortel is zuiver imaginair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ga je van de cartesische naar de goniometrische vorm?",
        opties=[
            "je berekent de modulus en het argument uit het reëel en imaginair deel",
            "je berekent de cosinus en de sinus van het reëel deel",
            "je vermenigvuldigt het reëel deel met het imaginair deel",
            "je verwisselt het reëel deel en het imaginair deel gewoon van plaats",
        ],
        antwoord=0,
        uitleg="De modulus is de wortel uit de som van de kwadraten, en het argument vind je met de tangens, met het juiste kwadrant erbij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel graden is het argument van het getal i? Schrijf het getal.",
        antwoord=["90", "negentig"],
        uitleg="Het punt ligt recht boven de oorsprong, dus een kwart draai vanaf de positieve reële as.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de goniometrische vorm handig bij machtsverheffen?",
        opties=[
            "omdat je dan alleen de modulus moet machtsverheffen en het argument vermenigvuldigen",
            "omdat de cosinus en de sinus van een hoek altijd tussen min één en plus één liggen",
            "omdat je dan helemaal geen rekenregel meer nodig hebt bij machten",
            "omdat het resultaat dan altijd een reëel getal wordt",
        ],
        antwoord=0,
        uitleg="Probeer één plus i tot de tiende in cartesische vorm en je ziet het verschil meteen.",
    ),
    dict(
        type="waarofniet",
        vraag="De modulus van een product van twee complexe getallen is de som van hun moduli.",
        antwoord=False,
        uitleg="Het is net het product van de moduli. Het zijn de argumenten die worden opgeteld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel n-de machtswortels heeft een complex getal dat niet nul is?",
        opties=[
            "precies n",
            "precies twee",
            "precies één",
            "oneindig veel",
        ],
        antwoord=0,
        uitleg="In de reële getallen zijn dat er hoogstens twee. In de complexe getallen zijn het er altijd n.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werden de complexe getallen ingevoerd?",
        opties=[
            "omdat niet elke vergelijking een oplossing had in de reële getallen",
            "omdat de reële getallen niet geordend konden worden",
            "omdat men de oppervlakte van een cirkel wou berekenen",
            "omdat men wortels uit positieve getallen eenvoudiger wou schrijven",
        ],
        antwoord=0,
        uitleg="Een getal waarvan het kwadraat min één is, bestond niet. Door het toe te voegen, kreeg elke veeltermvergelijking oplossingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een veelterm van graad n heeft in de complexe getallen precies n nulwaarden, als je ze met hun multipliciteit telt.",
        antwoord=True,
        uitleg="Dat is de hoofdstelling van de algebra. In de reële getallen kunnen het er minder zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de modulus van min drie? Schrijf het getal.",
        antwoord=["3", "drie"],
        uitleg="De modulus is een afstand en dus nooit negatief. Voor een reëel getal is ze de absolute waarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een vermenigvuldiging met i met een punt in het vlak van Gauss?",
        opties=[
            "het draait een kwart slag rond de oorsprong",
            "het spiegelt om de horizontale reële as",
            "het schuift één eenheid naar boven op",
            "het verdubbelt de afstand tot de oorsprong",
        ],
        antwoord=0,
        uitleg="De modulus van i is één en haar argument negentig graden, dus de afstand blijft en de hoek groeit met een kwart draai.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk argument heeft een negatief reëel getal?",
        opties=[
            "honderdtachtig graden",
            "nul graden",
            "negentig graden",
            "tweehonderdzeventig graden",
        ],
        antwoord=0,
        uitleg="Het ligt links van de oorsprong op de reële as, dus een halve draai vanaf de positieve kant.",
    ),
]
