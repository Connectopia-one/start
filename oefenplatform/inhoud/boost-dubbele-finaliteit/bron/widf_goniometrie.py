# -*- coding: utf-8 -*-
"""De vragen voor "De rechthoekige driehoek oplossen en toepassen".

Nieuw geschreven voor dubbele finaliteit. Het overgenomen thema "Pythagoras en
de rechthoekige driehoek" voert in zijn tweede deel de sinus, de cosinus en de
tangens in. Dit thema bouwt daarop verder: hier reken je er echt mee. Je zoekt
zijden, je zoekt hoeken, je lost de volledige driehoek op, en je past dat toe
op de situaties die de DF-fiche noemt: de hoogte van een boom of een gebouw uit
de kijkhoek en de afstand, en het hoogteverschil uit de hellingshoek en de
lengte van een pad. De definities zelf worden hier niet opnieuw gegeven; die
staan in het vorige thema.

Deel 1 gaat over zijden berekenen, deel 2 over hoeken en over de toepassingen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je kijkt in een rechthoekige driehoek naar hoek A. Welke zijde is de overstaande zijde van A?",
        opties=[
            "de zijde die tegenover A ligt",
            "de zijde die tegenover de rechte hoek ligt",
            "de langste zijde van de driehoek",
            "de zijde waarop de driehoek rust",
        ],
        antwoord=0,
        uitleg="Overstaande en aanliggende hangen af van de hoek waar je naar kijkt. Verander je van hoek, dan wisselen ze van plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijde is de aanliggende zijde van hoek A?",
        opties=[
            "de rechthoekszijde die tegen A aan ligt",
            "de schuine zijde, want die ligt ook tegen A aan",
            "de zijde tegenover A",
            "altijd de kortste zijde van de driehoek",
        ],
        antwoord=0,
        uitleg="Twee zijden raken hoek A: de schuine zijde en een rechthoekszijde. Met aanliggende bedoelen we die rechthoekszijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een rechthoekige driehoek met zijden 3, 4 en 5: hoeveel is de sinus van de hoek tegenover de zijde 3?",
        opties=["0,6", "0,8", "0,75", "1,25"],
        antwoord=0,
        uitleg="De overstaande zijde is 3 en de schuine is 5, dus 3 gedeeld door 5 is 0,6.",
    ),
    dict(
        type="meerkeuze",
        vraag="In diezelfde driehoek met zijden 3, 4 en 5: hoeveel is de cosinus van de hoek tegenover de zijde 3?",
        opties=["0,8", "0,6", "0,75", "1,33"],
        antwoord=0,
        uitleg="De aanliggende zijde is 4 en de schuine is 5, dus 4 gedeeld door 5 is 0,8.",
    ),
    dict(
        type="meerkeuze",
        vraag="In diezelfde driehoek met zijden 3, 4 en 5: hoeveel is de tangens van de hoek tegenover de zijde 3?",
        opties=["0,75", "0,6", "0,8", "1,25"],
        antwoord=0,
        uitleg="Overstaande gedeeld door aanliggende is 3 gedeeld door 4, dus 0,75.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een scherpe hoek en de schuine zijde, en je zoekt de overstaande zijde. Wat reken je?",
        opties=[
            "de sinus van de hoek maal de schuine zijde",
            "de cosinus van de hoek maal de schuine zijde",
            "de schuine zijde gedeeld door de sinus",
            "de tangens van de hoek maal de schuine zijde",
        ],
        antwoord=0,
        uitleg="Sinus is overstaande op schuine, dus de overstaande is sinus maal schuine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een scherpe hoek en de aanliggende zijde, en je zoekt de overstaande zijde. Wat reken je?",
        opties=[
            "de tangens van de hoek maal de aanliggende zijde",
            "de sinus van de hoek maal de aanliggende zijde",
            "de aanliggende zijde gedeeld door de cosinus",
            "de cosinus van de hoek maal de aanliggende zijde",
        ],
        antwoord=0,
        uitleg="Tangens is overstaande op aanliggende, dus de overstaande is tangens maal aanliggende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent een scherpe hoek en de aanliggende zijde, en je zoekt de schuine zijde. Wat reken je?",
        opties=[
            "de aanliggende zijde gedeeld door de cosinus",
            "de aanliggende zijde maal de cosinus",
            "de aanliggende zijde gedeeld door de sinus",
            "de aanliggende zijde maal de tangens",
        ],
        antwoord=0,
        uitleg="Cosinus is aanliggende op schuine, dus de schuine is aanliggende gedeeld door de cosinus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ladder van 6 meter staat onder een hoek van 60 graden met de grond. Hoe hoog reikt hij ongeveer tegen de muur?",
        opties=["5,20 meter", "3,00 meter", "6,93 meter", "10,39 meter"],
        antwoord=0,
        uitleg="De hoogte is de overstaande zijde: 6 maal de sinus van 60 graden geeft ongeveer 5,20 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Diezelfde ladder van 6 meter onder 60 graden: hoe ver staat zijn voet van de muur?",
        opties=["3 meter", "5,20 meter", "6,93 meter", "12 meter"],
        antwoord=0,
        uitleg="De afstand tot de muur is de aanliggende zijde: 6 maal de cosinus van 60 graden is 6 maal 0,5, dus 3 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="De sinus van een hoek is 0,5 en de schuine zijde is 10. Hoe lang is de overstaande zijde?",
        opties=["5", "20", "0,05", "10,5"],
        antwoord=0,
        uitleg="Sinus maal schuine zijde geeft de overstaande: 0,5 maal 10 is 5.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangen deze verhoudingen enkel van de hoek af en niet van de grootte van de driehoek?",
        opties=[
            "omdat driehoeken met dezelfde hoeken gelijkvormig zijn",
            "omdat elke rechthoekige driehoek even groot is",
            "omdat je de schuine zijde altijd op 1 zet",
            "omdat je de zijden toch afrondt op gehele getallen",
        ],
        antwoord=0,
        uitleg="Bij gelijkvormige driehoeken worden alle zijden met dezelfde factor vermenigvuldigd, en die factor valt in de breuk weg.",
    ),
    dict(
        type="waarofniet",
        vraag="De tangens van een scherpe hoek kan groter zijn dan 1.",
        antwoord=True,
        uitleg="Zodra de overstaande zijde langer is dan de aanliggende, is de breuk groter dan 1.",
    ),
    dict(
        type="waarofniet",
        vraag="De sinus en de cosinus van een hoek van 45 graden zijn aan elkaar gelijk.",
        antwoord=True,
        uitleg="Bij 45 graden zijn de twee rechthoekszijden even lang, dus overstaande en aanliggende zijn gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een goniometrisch getal van een scherpe hoek kan negatief zijn.",
        antwoord=False,
        uitleg="Zijden hebben een positieve lengte, dus een verhouding van twee zijden blijft positief.",
    ),
    dict(
        type="waarofniet",
        vraag="In een rechthoekige driehoek zijn de twee scherpe hoeken samen 180 graden.",
        antwoord=False,
        uitleg="Ze zijn samen 90 graden. De rechte hoek neemt al 90 van de 180 graden in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een driehoek heeft een rechte hoek en een scherpe hoek van 30 graden. Hoe groot is de derde hoek?",
        opties=["60 graden", "30 graden", "90 graden", "120 graden"],
        antwoord=0,
        uitleg="Alle hoeken samen zijn 180 graden, en 180 min 90 min 30 is 60.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kijk je voor je begint na of je rekentoestel op graden staat?",
        opties=[
            "omdat je anders een fout antwoord krijgt bij een juiste berekening",
            "omdat het toestel anders een foutmelding geeft",
            "omdat graden nauwkeuriger rekenen dan andere instellingen",
            "omdat een rechthoekige driehoek enkel in graden bestaat",
        ],
        antwoord=0,
        uitleg="Staat je toestel anders ingesteld, dan klopt er niets van je uitkomst terwijl je redenering wel juist was.",
    ),
    dict(
        type="invultekst",
        vraag="Welke verhouding gebruik je als je de overstaande en de aanliggende zijde kent en de hoek zoekt?",
        antwoord=["de tangens", "tangens", "tan"],
        uitleg="Overstaande op aanliggende is de tangens. Met de inverse vind je de hoek terug.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de zijde die tegenover de rechte hoek ligt?",
        antwoord=["de schuine zijde", "schuine zijde", "de hypotenusa"],
        uitleg="De schuine zijde is altijd de langste zijde van een rechthoekige driehoek.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'de rechthoekige driehoek oplossen'?",
        opties=[
            "alle zijden en alle hoeken ervan berekenen",
            "enkel de oppervlakte ervan berekenen",
            "de driehoek in twee gelijke stukken verdelen",
            "de omtrek en de oppervlakte ervan berekenen",
        ],
        antwoord=0,
        uitleg="Met één zijde en één scherpe hoek, of met twee zijden, liggen alle andere zijden en hoeken vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent de overstaande zijde en de schuine zijde, en je zoekt de hoek. Wat doe je?",
        opties=[
            "je deelt ze door elkaar en neemt de inverse sinus",
            "je deelt ze door elkaar en neemt de inverse tangens",
            "je deelt ze door elkaar en neemt de inverse cosinus",
            "je telt ze op en deelt door 90",
        ],
        antwoord=0,
        uitleg="Overstaande op schuine is de sinus. De inverse sinus op je rekentoestel geeft de hoek terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je kent allebei de rechthoekszijden en je zoekt een scherpe hoek. Wat doe je?",
        opties=[
            "je deelt ze door elkaar en neemt de inverse tangens",
            "je deelt ze door elkaar en neemt de inverse sinus",
            "je telt ze op en neemt de inverse cosinus",
            "je gebruikt eerst Pythagoras en dan de inverse sinus",
        ],
        antwoord=0,
        uitleg="De twee rechthoekszijden zijn de overstaande en de aanliggende, en dat is precies de tangens.",
    ),
    dict(
        type="meerkeuze",
        vraag="De cosinus van een scherpe hoek is 0,96. Hoeveel is de sinus?",
        opties=["0,28", "0,04", "0,48", "1,04"],
        antwoord=0,
        uitleg="Met de grondformule: 1 min 0,9216 is 0,0784, en de wortel daarvan is 0,28.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een weg heeft een hellingspercentage van 8 procent. Wat betekent dat?",
        opties=[
            "je stijgt 8 meter over 100 meter horizontaal",
            "je stijgt 8 meter over 100 meter weglengte",
            "de hellingshoek is 8 graden",
            "je stijgt 8 centimeter per meter weglengte",
        ],
        antwoord=0,
        uitleg="Een hellingspercentage is de tangens van de hellingshoek, uitgedrukt in procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bergpad van 500 meter loopt onder een hellingshoek van 12 graden. Hoeveel hoogte win je ongeveer?",
        opties=["104 meter", "489 meter", "106 meter", "60 meter"],
        antwoord=0,
        uitleg="De padlengte is de schuine zijde, dus je rekent 500 maal de sinus van 12 graden, ongeveer 104 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vlieger hangt aan 40 meter touw dat onder 55 graden met de grond staat. Hoe hoog hangt hij ongeveer?",
        opties=["32,8 meter", "22,9 meter", "57,1 meter", "48,8 meter"],
        antwoord=0,
        uitleg="Het touw is de schuine zijde, dus de hoogte is 40 maal de sinus van 55 graden, ongeveer 32,8 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een mast werpt een schaduw van 12 meter terwijl de zon 40 graden boven de horizon staat. Hoe hoog is de mast ongeveer?",
        opties=["10,1 meter", "7,7 meter", "14,3 meter", "15,7 meter"],
        antwoord=0,
        uitleg="De schaduw is de aanliggende zijde, dus de hoogte is 12 maal de tangens van 40 graden, ongeveer 10,1 meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je staat 20 meter van een gebouw en kijkt naar de top onder 35 graden. Je ogen zitten 1,6 meter hoog. Hoe hoog is het gebouw ongeveer?",
        opties=["15,6 meter", "14,0 meter", "12,4 meter", "17,2 meter"],
        antwoord=0,
        uitleg="20 maal de tangens van 35 graden is ongeveer 14,0 meter, en daar komt je ooghoogte van 1,6 meter nog bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oprit mag hoogstens 5 procent hellen en moet 30 centimeter overbruggen. Hoe lang moet hij minstens zijn?",
        opties=["6 meter", "1,5 meter", "60 meter", "15 meter"],
        antwoord=0,
        uitleg="Vijf procent wil zeggen 5 centimeter stijging per meter. Voor 30 centimeter heb je dus 6 meter nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een helling van 25 procent komt ongeveer overeen met welke hellingshoek?",
        opties=["14 graden", "25 graden", "4 graden", "45 graden"],
        antwoord=0,
        uitleg="Het hellingspercentage is de tangens: de inverse tangens van 0,25 is ongeveer 14 graden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een helling van 100 procent komt overeen met een hoek van 45 graden.",
        antwoord=True,
        uitleg="Bij 100 procent stijg je even veel als je vooruit gaat, en de tangens van 45 graden is precies 1.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe steiler de helling, hoe groter de sinus van de hellingshoek.",
        antwoord=True,
        uitleg="Bij dezelfde padlengte win je meer hoogte naarmate de hoek groter wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Met één gegeven zijde alleen kan je een rechthoekige driehoek volledig oplossen.",
        antwoord=False,
        uitleg="Je hebt er een tweede gegeven bij nodig: nog een zijde, of een van de scherpe hoeken.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hellingspercentage van een weg is hetzelfde getal als de hellingshoek in graden.",
        antwoord=False,
        uitleg="Acht procent is niet acht graden, maar ongeveer 4,6 graden. Het percentage is de tangens van de hoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je berekent een scherpe hoek in een rechthoekige driehoek en krijgt 91 graden. Wat weet je?",
        opties=[
            "er zit een fout in je berekening",
            "de driehoek is stomphoekig",
            "je moet het antwoord afronden naar 90",
            "de schuine zijde was te kort gegeven",
        ],
        antwoord=0,
        uitleg="De rechte hoek neemt al 90 graden in, dus een scherpe hoek in diezelfde driehoek blijft altijd daaronder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je eerst een schets voor je begint te rekenen?",
        opties=[
            "omdat je dan ziet welke zijde overstaand en welke aanliggend is",
            "omdat een schets op het examen verplicht is",
            "omdat je anders geen rekentoestel mag gebruiken",
            "omdat de tekening het antwoord al geeft",
        ],
        antwoord=0,
        uitleg="De meeste fouten komen van de verkeerde verhouding kiezen. Op een schets met de gegevens erbij zie je meteen welke je nodig hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je berekent een hoogte en je rekentoestel toont 5,1962. Waarom rond je pas op het einde af?",
        opties=[
            "omdat afronden onderweg je eindantwoord verder doet afwijken",
            "omdat het rekentoestel anders een fout geeft",
            "omdat een hoogte altijd op vier cijfers moet staan",
            "omdat je anders de eenheid vergeet te noteren",
        ],
        antwoord=0,
        uitleg="Elke afronding onderweg stapelt zich op. Reken met de volledige tussenresultaten en rond het eindantwoord af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de hoek waaronder je vanaf de grond omhoog kijkt naar de top van een boom?",
        antwoord=["de kijkhoek", "kijkhoek"],
        uitleg="Samen met je afstand tot de boom geeft de kijkhoek je de hoogte, via de tangens.",
    ),
    dict(
        type="invultekst",
        vraag="Welk goniometrisch getal is het hellingspercentage van een weg?",
        antwoord=["de tangens", "tangens", "tan"],
        uitleg="Acht procent betekent dat de tangens van de hellingshoek 0,08 is.",
    ),
]
