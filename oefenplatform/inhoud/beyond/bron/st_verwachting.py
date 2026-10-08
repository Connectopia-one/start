# -*- coding: utf-8 -*-
"""Verwachtingswaarde, variantie en standaardafwijking.

De vakfiche vraagt twee dingen apart: je berekent ze bij een binomiale
verdeling met ICT, én je interpreteert ze. Dat tweede is het echte leerdoel.
Een kind dat n maal p kan uitrekenen maar niet kan zeggen wat dat getal
betekent, haalt dit onderdeel niet.

Het formularium geeft voor X ~ B(n, p):
    E(X) = n · p
    Var(X) = n · p · (1 − p)
De standaardafwijking is de vierkantswortel van de variantie. De bijlage
noteert E(X) als mu met index X en Var(X) als sigma kwadraat met index X.

Twee misvattingen om op te vangen, en daarom staan ze hier als vraag:
de verwachtingswaarde hoeft geen mogelijke uitkomst te zijn (2,5 kinderen),
en de variantie heeft de eenheid in het kwadraat terwijl de
standaardafwijking dezelfde eenheid heeft als de kansvariabele zelf.

Deel 1 is de verwachtingswaarde.
Deel 2 is de variantie en de standaardafwijking.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de verwachtingswaarde van een kansvariabele?",
        opties=[
            "het gemiddelde dat je op lange termijn verwacht",
            "de uitkomst met de grootste kans van allemaal",
            "de grootste waarde die de kansvariabele kan aannemen",
            "de kans dat de meest waarschijnlijke uitkomst valt",
        ],
        antwoord=0,
        uitleg="Herhaal je het experiment heel vaak, dan schuift het gemiddelde van je uitkomsten naar E(X).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft E(X) bij X ~ B(n, p)?",
        opties=["n maal p", "n gedeeld door p", "n maal p maal (1−p)", "p tot de macht n"],
        antwoord=0,
        uitleg="Zo staat ze in het formularium: E(X) = n · p. Dat krijg je op het examen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(20; 0,5), hoeveel is E(X)?",
        opties=["tien", "twintig", "vijf", "nul komma vijf"],
        antwoord=0,
        uitleg="Twintig maal nul komma vijf is tien. Bij twintig muntworpen verwacht je tien keer kop.",
    ),
    dict(
        type="waarofniet",
        vraag="De verwachtingswaarde moet altijd een waarde zijn die de kansvariabele echt kan aannemen.",
        antwoord=False,
        uitleg="Nee. Het gemiddelde aantal kinderen per gezin kan 1,7 zijn, en geen enkel gezin heeft 1,7 kinderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je E(X) bij een discrete kansvariabele uit een tabel?",
        opties=[
            "je vermenigvuldigt elke waarde met haar kans en telt alles op",
            "je telt alle waarden op en deelt door het aantal waarden",
            "je neemt de waarde met de grootste kans",
            "je telt alle kansen op en deelt door het aantal waarden",
        ],
        antwoord=0,
        uitleg="E(X) is een gewogen gemiddelde: elke waarde weegt even zwaar als haar kans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kansvariabele heeft de waarden nul, één en twee met kansen 0,1 / 0,3 / 0,6. Hoeveel is E(X)?",
        opties=["1,5", "1", "1,2", "0,9"],
        antwoord=0,
        uitleg="Nul maal 0,1 plus één maal 0,3 plus twee maal 0,6 is 0 + 0,3 + 1,2 = 1,5.",
    ),
    dict(
        type="invultekst",
        vraag="Bij X ~ B(50; 0,2), hoeveel is E(X)? Geef het getal in cijfers.",
        antwoord=["10"],
        uitleg="Vijftig maal nul komma twee is tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(100; 0,3), hoeveel is E(X)?",
        opties=["dertig", "zeventig", "drie", "driehonderd"],
        antwoord=0,
        uitleg="Honderd maal nul komma drie is dertig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een eerlijke dobbelsteen die zestig keer gegooid wordt, is het verwachte aantal zessen tien.",
        antwoord=True,
        uitleg="Zestig maal een zesde is tien. Dat belet niet dat je er in werkelijkheid zeven of dertien kan gooien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een loterijlot kost twee euro en de verwachtingswaarde van je winst is 1,20 euro. Wat betekent dat?",
        opties=[
            "wie heel veel loten koopt, verliest gemiddeld tachtig cent per lot",
            "je wint zeker 1,20 euro bij elk lot dat je koopt",
            "je hebt zestig procent kans om je inleg terug te krijgen",
            "het lot is tachtig cent te duur en zou 1,20 euro moeten kosten",
        ],
        antwoord=0,
        uitleg="Verwachte opbrengst min inleg: 1,20 min 2 euro is min tachtig cent per lot op lange termijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een penaltyschutter raakt in tachtig procent van de gevallen. Hij neemt vijftien penalty's. Hoeveel doelpunten verwacht je?",
        opties=["twaalf", "tien", "dertien", "acht"],
        antwoord=0,
        uitleg="Vijftien maal nul komma acht is twaalf.",
    ),
    dict(
        type="waarofniet",
        vraag="Verdubbel je bij een binomiale verdeling het aantal experimenten, dan verdubbelt ook de verwachtingswaarde.",
        antwoord=True,
        uitleg="E(X) = n · p is recht evenredig met n. Bij de standaardafwijking gaat dat niet zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(10; 0,4) is E(X) gelijk aan vier. Wat betekent dat concreet?",
        opties=[
            "doe je de reeks van tien vaak opnieuw, dan haal je gemiddeld vier successen",
            "bij elke reeks van tien krijg je precies vier successen",
            "de kans op vier successen is veertig procent",
            "vier is de uitkomst met de kleinste kans van allemaal",
        ],
        antwoord=0,
        uitleg="De verwachtingswaarde zegt iets over het gemiddelde van veel reeksen, niet over één reeks.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt de bijlage voor de verwachtingswaarde van X? Eén Griekse letter.",
        antwoord=["mu", "mu x", "μ"],
        uitleg="E(X) wordt ook geschreven als mu met index X.",
    ),
    dict(
        type="waarofniet",
        vraag="E(X) kan negatief zijn.",
        antwoord=True,
        uitleg="Bij een kansvariabele die winst én verlies kan geven, zoals bij een gokspel, zeker wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een test heeft twintig vragen met vijf opties. Je gokt alles. Hoeveel juiste antwoorden verwacht je?",
        opties=["vier", "vijf", "tien", "twee"],
        antwoord=0,
        uitleg="Twintig maal een vijfde is vier. Daarom helpt gokken je zelden aan een voldoende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is E(X) een gewogen gemiddelde en geen gewoon gemiddelde?",
        opties=[
            "omdat elke waarde met haar eigen kans meetelt in plaats van even zwaar",
            "omdat je altijd door het aantal experimenten moet delen",
            "omdat de waarden in een kansverdeling altijd ongelijk verdeeld liggen",
            "omdat de som van de kansen gelijk moet zijn aan één",
        ],
        antwoord=0,
        uitleg="Een waarde met kans nul komma zes weegt zes keer zo zwaar als een waarde met kans nul komma één.",
    ),
    dict(
        type="invultekst",
        vraag="Bij X ~ B(400; 0,25), hoeveel is E(X)? Geef het getal in cijfers.",
        antwoord=["100"],
        uitleg="Vierhonderd maal nul komma vijfentwintig is honderd.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij X ~ B(n; 0,8) ligt E(X) precies in het midden van het bereik van X.",
        antwoord=False,
        uitleg="n maal nul komma acht ligt ver naar rechts. Enkel bij p gelijk aan een half valt E(X) in het midden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel verkoopt per dag gemiddeld 2,4 fietsen. Een leerling zegt dat dat niet kan. Wat antwoord je?",
        opties=[
            "een gemiddelde hoeft geen geheel getal te zijn, enkel de dagelijkse aantallen",
            "de leerling heeft gelijk, het moet afgerond worden naar twee fietsen",
            "dat kan enkel als de winkel halve fietsen verkoopt",
            "dan is de kansvariabele continu in plaats van discreet",
        ],
        antwoord=0,
        uitleg="Twaalf fietsen in vijf dagen geeft een gemiddelde van 2,4. Elke dag zelf is wel een geheel aantal.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat meet de standaardafwijking van een kansvariabele?",
        opties=[
            "hoeveel de uitkomsten gemiddeld van de verwachtingswaarde afwijken",
            "het verschil tussen de grootste en de kleinste uitkomst",
            "de kans dat de uitkomst gelijk is aan de verwachtingswaarde",
            "hoeveel experimenten je moet doen voor een betrouwbaar resultaat",
        ],
        antwoord=0,
        uitleg="Ze is een spreidingsmaat: klein betekent dat de uitkomsten dicht bij E(X) kleven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft Var(X) bij X ~ B(n, p)?",
        opties=[
            "n maal p maal (1−p)",
            "n maal p",
            "de wortel uit n maal p",
            "n kwadraat maal p",
        ],
        antwoord=0,
        uitleg="Zo staat ze in het formularium: Var(X) = n · p · (1 − p).",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kom je van de variantie naar de standaardafwijking?",
        opties=[
            "je neemt de vierkantswortel",
            "je neemt het kwadraat",
            "je deelt door het aantal experimenten",
            "je deelt door de verwachtingswaarde",
        ],
        antwoord=0,
        uitleg="De standaardafwijking is de wortel uit de variantie. Daarom is ze in dezelfde eenheid uitgedrukt als X.",
    ),
    dict(
        type="waarofniet",
        vraag="De variantie is uitgedrukt in de eenheid van X in het kwadraat.",
        antwoord=True,
        uitleg="Meet je in centimeter, dan is de variantie in vierkante centimeter en de standaardafwijking weer in centimeter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(20; 0,5), hoeveel is Var(X)?",
        opties=["vijf", "tien", "twintig", "twee komma vijf"],
        antwoord=0,
        uitleg="Twintig maal nul komma vijf maal nul komma vijf is vijf. De standaardafwijking is dan de wortel uit vijf.",
    ),
    dict(
        type="invultekst",
        vraag="Bij X ~ B(50; 0,2), hoeveel is Var(X)? Geef het getal in cijfers.",
        antwoord=["8"],
        uitleg="Vijftig maal nul komma twee maal nul komma acht is acht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(100; 0,3), hoeveel is de standaardafwijking ongeveer?",
        opties=["4,58", "21", "30", "9,17"],
        antwoord=0,
        uitleg="Var(X) = 100 · 0,3 · 0,7 = 21, en de wortel uit 21 is ongeveer 4,58.",
    ),
    dict(
        type="waarofniet",
        vraag="De variantie van een kansvariabele kan negatief zijn.",
        antwoord=False,
        uitleg="Nooit. Ze is opgebouwd uit kwadraten, dus ze is altijd nul of positief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke p is Var(X) bij een vast aantal n het grootst?",
        opties=[
            "bij p gelijk aan nul komma vijf",
            "bij p gelijk aan nul komma negen",
            "bij p gelijk aan nul komma één",
            "bij p gelijk aan nul komma nul één",
        ],
        antwoord=0,
        uitleg="p maal (1−p) is maximaal bij een half. Hoe dichter p bij nul of één ligt, hoe kleiner de spreiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(12; 0,5) is Var(X) gelijk aan drie. Hoeveel is de standaardafwijking?",
        opties=[
            "ongeveer 1,73",
            "negen",
            "zes",
            "ongeveer 0,58",
        ],
        antwoord=0,
        uitleg="De wortel uit drie is ongeveer 1,73.",
    ),
    dict(
        type="waarofniet",
        vraag="Een standaardafwijking van nul betekent dat de uitkomst altijd dezelfde is.",
        antwoord=True,
        uitleg="Geen spreiding betekent geen verschil tussen de uitkomsten. Bij p gelijk aan nul of één is dat zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee binomiale verdelingen hebben allebei E(X) gelijk aan tien, maar de ene heeft standaardafwijking 1 en de andere 3. Wat betekent dat?",
        opties=[
            "bij de tweede liggen de uitkomsten verder uit elkaar",
            "bij de tweede is de verwachtingswaarde minder betrouwbaar berekend",
            "bij de tweede zijn er drie keer zoveel experimenten gedaan",
            "bij de tweede is de kans op succes drie keer zo groot",
        ],
        antwoord=0,
        uitleg="Dezelfde verwachtingswaarde zegt niets over de spreiding. Daarom heb je allebei de getallen nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt de bijlage voor de standaardafwijking van X? Eén Griekse letter.",
        antwoord=["sigma", "sigma x", "σ"],
        uitleg="De standaardafwijking is sigma met index X, de variantie is sigma kwadraat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een machine vult flessen. Bij X ~ B(200; 0,05) telt X het aantal te lichte flessen. Hoeveel is E(X) en Var(X)?",
        opties=[
            "tien en 9,5",
            "tien en tien",
            "vijf en 9,5",
            "tien en 0,95",
        ],
        antwoord=0,
        uitleg="E(X) = 200 · 0,05 = 10 en Var(X) = 200 · 0,05 · 0,95 = 9,5.",
    ),
    dict(
        type="waarofniet",
        vraag="Verviervoudig je n bij een binomiale verdeling, dan verdubbelt de standaardafwijking.",
        antwoord=True,
        uitleg="De variantie wordt vier keer groter, en de wortel uit vier is twee. Spreiding groeit dus veel langzamer dan n.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men liever de standaardafwijking dan de variantie om een verdeling te beschrijven?",
        opties=[
            "omdat ze in dezelfde eenheid staat als de kansvariabele zelf",
            "omdat ze altijd een kleiner getal oplevert dan de variantie",
            "omdat je ze zonder rekenapp kan uitrekenen",
            "omdat ze nooit afhangt van het aantal experimenten",
        ],
        antwoord=0,
        uitleg="Een spreiding van 4,58 fietsen zegt iets; 21 vierkante fietsen zegt niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(80; 0,25), hoeveel zijn E(X) en Var(X)?",
        opties=["twintig en vijftien", "twintig en twintig", "twintig en zestig", "vijftien en twintig"],
        antwoord=0,
        uitleg="E(X) = 80 · 0,25 = 20 en Var(X) = 80 · 0,25 · 0,75 = 15.",
    ),
    dict(
        type="waarofniet",
        vraag="Om de standaardafwijking bij een binomiale verdeling te kennen, moet je eerst de hele kansverdeling opstellen.",
        antwoord=False,
        uitleg="Niet nodig. Het formularium geeft Var(X) = n · p · (1 − p) rechtstreeks uit n en p.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij X ~ B(60; 1/6) is E(X) gelijk aan tien. Hoeveel is Var(X) ongeveer?",
        opties=["8,33", "tien", "1,67", "vijftig"],
        antwoord=0,
        uitleg="Zestig maal een zesde maal vijf zesde is vijftig gedeeld door zes, ongeveer 8,33.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling vindt bij X ~ B(40; 0,5) een standaardafwijking van tien. Wat ging er mis?",
        opties=[
            "de wortel is vergeten, want Var(X) is tien en de standaardafwijking ongeveer 3,16",
            "er is met n gerekend in plaats van met p, het antwoord is twintig",
            "de variantie is twee keer geteld, het antwoord is vijf",
            "er ging niets mis, tien is het juiste antwoord",
        ],
        antwoord=0,
        uitleg="Var(X) = 40 · 0,5 · 0,5 = 10. De standaardafwijking is de wortel daarvan, ongeveer 3,16.",
    ),
]
