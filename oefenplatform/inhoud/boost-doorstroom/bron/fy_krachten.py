# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Krachten, krachtenbalans en zwaartekracht.

Hoort bij "beweging - krachten" van de vakfiche fysica 2de graad
doorstroomfinaliteit, het vierde van vijf thema's voor dat onderdeel van 35 %.

Deel 1 gaat over de kracht als vector: de vier kenmerken, alle krachten op een
voorwerp tekenen, krachten met dezelfde richting samenstellen, een krachtvector
in twee componenten ontbinden, en het verband tussen de resulterende kracht en
het veranderen of behouden van de snelheid. Deel 2 gaat over de drie krachten
met een formule op de fiche: de zwaartekracht Fz = m.g, de veerkracht
Fv = k.Δl en de statische wrijvingskracht Fw = μ.Fn, plus het verschil tussen
massa en gewicht.

De tweede wet van Newton staat niet op de fiche en F = m.a dus ook niet. Het
verband tussen de resulterende kracht en de beweging blijft hier kwalitatief:
een resulterende kracht van nul betekent dat de snelheid niet verandert.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van kracht, en wat meet je ermee?",
        opties=[
            "de newton, met een dynamometer",
            "de newton, met een balans",
            "de kilogram, met een dynamometer",
            "de joule, met een dynamometer",
        ],
        antwoord=0,
        uitleg="Een kracht meet je in newton met een dynamometer. Een balans meet massa in kilogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boek ligt stil op een tafel. Welke krachten werken erop?",
        opties=[
            "de zwaartekracht en de normaalkracht",
            "enkel de zwaartekracht",
            "enkel de normaalkracht",
            "de zwaartekracht en de wrijvingskracht",
        ],
        antwoord=0,
        uitleg="De zwaartekracht trekt het boek naar beneden en de tafel duwt met de normaalkracht terug. Die twee zijn even groot, dus het boek blijft liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee mensen duwen een kast in dezelfde zin, met 120 N en 80 N. Hoe groot is de resulterende kracht?",
        opties=["200 N", "40 N", "100 N", "9600 N"],
        antwoord=0,
        uitleg="Krachten met dezelfde richting en dezelfde zin tel je op: 120 + 80 = 200 N.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee mensen trekken aan een kar in tegengestelde zin, met 150 N en 90 N. Hoe groot is de resulterende kracht, en in welke zin?",
        opties=[
            "60 N, in de zin van de grootste kracht",
            "240 N, in de zin van de grootste kracht",
            "60 N, in de zin van de kleinste kracht",
            "0 N, de kar blijft stil",
        ],
        antwoord=0,
        uitleg="Bij een tegengestelde zin trek je de groottes van elkaar af: 150 − 90 = 60 N. De resultante wijst in de zin van de grootste kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft een krachtvector? Kruis alles aan wat juist is.",
        opties=[
            "een grootte in newton",
            "een aangrijpingspunt op het voorwerp",
            "een massa in kilogram",
            "een eenheid in joule",
        ],
        antwoord=[0, 1],
        uitleg="Een kracht heeft een grootte, een richting, een zin en een aangrijpingspunt. De massa en de joule horen bij andere grootheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als de resulterende kracht op een voorwerp nul is?",
        opties=[
            "de snelheid van het voorwerp verandert niet",
            "het voorwerp staat zeker stil",
            "er werkt geen enkele kracht op het voorwerp",
            "het voorwerp versnelt gelijkmatig",
        ],
        antwoord=0,
        uitleg="De krachten heffen elkaar op, dus de snelheid blijft gelijk in grootte, richting en zin. Dat kan rust zijn, maar ook een eenparige beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een slee wordt met een koord onder een hoek naar voren getrokken. In welke twee componenten ontbind je die kracht het best?",
        opties=[
            "een horizontale en een verticale component",
            "twee horizontale componenten",
            "twee verticale componenten",
            "een component langs het koord en een even grote tegengestelde",
        ],
        antwoord=0,
        uitleg="De horizontale component trekt de slee vooruit, de verticale component tilt hem een beetje op en vermindert zo de normaalkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de normaalkracht?",
        opties=[
            "de kracht van het oppervlak op het voorwerp, loodrecht erop",
            "de kracht van het voorwerp op het oppervlak, er juist langs",
            "de kracht die de wrijving veroorzaakt, langs het oppervlak",
            "de zwaartekracht op het voorwerp, met een andere naam",
        ],
        antwoord=0,
        uitleg="Normaal betekent hier loodrecht. Het oppervlak duwt loodrecht terug op het voorwerp dat erop ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de normaalkracht en de wrijvingskracht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze staan loodrecht op elkaar",
            "de wrijvingskracht ligt langs het oppervlak",
            "ze hebben dezelfde richting",
            "ze zijn altijd even groot",
        ],
        antwoord=[0, 1],
        uitleg="De normaalkracht staat loodrecht op het oppervlak en de wrijvingskracht ligt erlangs, dus de twee staan loodrecht op elkaar. Hun grootte heeft niets met elkaar te maken behalve via de wrijvingscoëfficiënt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp hangt stil aan een veer. Wat geldt voor de veerkracht?",
        opties=[
            "ze is even groot als de zwaartekracht en omhoog gericht",
            "ze is even groot als de zwaartekracht en omlaag gericht",
            "ze is groter dan de zwaartekracht",
            "ze is nul",
        ],
        antwoord=0,
        uitleg="Het voorwerp hangt stil, dus de resulterende kracht is nul. De veer trekt dan even hard omhoog als de zwaartekracht omlaag trekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe stel je de resultante van twee krachten met een verschillende richting grafisch samen?",
        opties=[
            "met de parallellogramregel",
            "door hun groottes op te tellen",
            "door hun groottes af te trekken",
            "door hun groottes te vermenigvuldigen",
        ],
        antwoord=0,
        uitleg="Je tekent een parallellogram met de twee vectoren als zijden. De diagonaal vanuit het aangrijpingspunt is de resultante.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht heeft altijd een voorwerp dat ze uitoefent en een voorwerp waarop ze werkt.",
        antwoord=True,
        uitleg="Een kracht is altijd een wisselwerking tussen twee voorwerpen. Daarom hoort bij de naam van een kracht altijd van wie op wat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp dat met een constante snelheid rechtdoor beweegt, heeft een resulterende kracht van nul.",
        antwoord=True,
        uitleg="De snelheid verandert niet, dus de krachten heffen elkaar op. Rijdt een auto met constante snelheid, dan is de motorkracht even groot als de wrijving.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee krachten van elk 50 N op hetzelfde voorwerp geven altijd een resultante van 100 N.",
        antwoord=False,
        uitleg="Enkel als ze dezelfde richting en zin hebben. Zijn ze tegengesteld, dan is de resultante nul, en bij een hoek ertussen iets daartussen.",
    ),
    dict(
        type="waarofniet",
        vraag="De lengte van een krachtvector op een tekening zegt niets over de grootte van de kracht.",
        antwoord=False,
        uitleg="Je tekent een krachtvector op schaal, bijvoorbeeld 1 cm voor 10 N. De lengte geeft dus net de grootte weer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een duwkracht en een trekkracht kunnen even goed met een vectorpijl getekend worden.",
        antwoord=True,
        uitleg="Allebei zijn het krachten met een grootte, een richting, een zin en een aangrijpingspunt. Het verschil zit enkel in de zin van de pijl.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de kracht die je krijgt als je alle krachten op een voorwerp samenstelt?",
        antwoord=["resulterende kracht", "de resulterende kracht", "resultante"],
        uitleg="De resulterende kracht of de resultante. Is die nul, dan verandert de snelheid niet.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor een kracht?",
        antwoord=["F"],
        uitleg="F, van het Latijnse woord voor kracht. De zwaartekracht krijgt Fz, de veerkracht Fv.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de kracht waarmee een oppervlak loodrecht terugduwt op een voorwerp dat erop ligt?",
        antwoord=["normaalkracht", "de normaalkracht", "normaal"],
        uitleg="De normaalkracht, met symbool Fn. Normaal betekent hier loodrecht.",
    ),
    dict(
        type="invultekst",
        vraag="Twee krachten van 30 N en 45 N werken in tegengestelde zin op hetzelfde voorwerp. Hoe groot is de resultante in newton? Schrijf het getal.",
        antwoord=["15", "15 N"],
        uitleg="45 − 30 = 15 N, in de zin van de kracht van 45 N.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de zwaartekracht op een voorwerp?",
        opties=["Fz = m . g", "Fz = m / g", "Fz = g / m", "Fz = m . g²"],
        antwoord=0,
        uitleg="De massa maal de zwaarteveldsterkte. In België is g = 9,81 N/kg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de zwaartekracht op een massa van 5,0 kg in België?",
        opties=["49 N", "5,0 N", "0,51 N", "490 N"],
        antwoord=0,
        uitleg="Fz = 5,0 . 9,81 = 49,05 N, dus 49 N met twee beduidende cijfers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de massa en het gewicht van een lichaam?",
        opties=[
            "de massa is een hoeveelheid materie, het gewicht is een kracht",
            "de massa is een kracht, het gewicht is een hoeveelheid materie",
            "er is geen verschil, enkel een andere eenheid",
            "de massa hangt af van de plaats, het gewicht niet",
        ],
        antwoord=0,
        uitleg="De massa in kilogram verandert niet als je verhuist naar de maan. Het gewicht is de kracht waarmee het lichaam op zijn steun duwt en wordt op de maan wel kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een astronaut in een ruimtestation zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "zijn massa blijft dezelfde als op aarde",
            "hij lijkt gewichtloos",
            "zijn massa is nul",
            "de aarde trekt niet meer aan hem",
        ],
        antwoord=[0, 1],
        uitleg="De massa verandert nooit van plaats tot plaats. De astronaut voelt zich gewichtloos omdat hij samen met het station in een vrije val rond de aarde beweegt, niet omdat de zwaartekracht verdwenen is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een veer rekt 4,0 cm uit onder een kracht van 12 N. Wat is de veerconstante?",
        opties=["300 N/m", "3,0 N/m", "48 N/m", "0,33 N/m"],
        antwoord=0,
        uitleg="Reken eerst om naar meter: 4,0 cm = 0,040 m. Dan is k = Fv / Δl = 12 / 0,040 = 300 N/m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een veer heeft een veerconstante van 250 N/m. Hoeveel rekt ze uit onder een kracht van 20 N?",
        opties=["8,0 cm", "80 cm", "0,80 cm", "12,5 cm"],
        antwoord=0,
        uitleg="Δl = Fv / k = 20 / 250 = 0,080 m, dus 8,0 cm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hangt dezelfde massa aan twee verschillende veren. Veer A rekt verder uit dan veer B. Wat geldt?",
        opties=[
            "veer A heeft de kleinere veerconstante",
            "veer A heeft de grotere veerconstante",
            "beide veren hebben dezelfde veerconstante",
            "veer A ondervindt een grotere kracht",
        ],
        antwoord=0,
        uitleg="Bij dezelfde kracht rekt de slappere veer verder uit. Een kleine k betekent dus een slappe veer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de statische wrijvingskracht?",
        opties=["Fw = μ . Fn", "Fw = μ / Fn", "Fw = μ . m", "Fw = Fn / μ"],
        antwoord=0,
        uitleg="De wrijvingscoëfficiënt maal de normaalkracht. Die formule staat in de bijlage die je op het examen mag gebruiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist van 20 kg staat op een horizontale vloer met μ = 0,30. Hoe groot is de wrijvingskracht die je net moet overwinnen om hem te doen schuiven?",
        opties=["59 N", "6,0 N", "196 N", "654 N"],
        antwoord=0,
        uitleg="Op een horizontale vloer is Fn = Fz = 20 . 9,81 = 196 N. Dan is Fw = 0,30 . 196 = 58,9 N, dus 59 N.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de wrijvingscoëfficiënt μ zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze heeft geen eenheid",
            "ze hangt af van de twee materialen die over elkaar schuiven",
            "ze wordt in newton uitgedrukt",
            "ze hangt af van de massa van het voorwerp",
        ],
        antwoord=[0, 1],
        uitleg="μ is een verhouding van twee krachten, dus een getal zonder eenheid. Ze hangt af van het soort oppervlakken, niet van de massa: die zit al in de normaalkracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet de zwaartekracht op dezelfde massa op de aarde en op de maan. Wat verschilt er? Kruis alles aan wat juist is.",
        opties=[
            "de zwaarteveldsterkte",
            "de massa van het voorwerp",
            "de grootte van de zwaartekracht",
            "de eenheid waarin je de kracht meet",
        ],
        antwoord=[0, 2],
        uitleg="De zwaarteveldsterkte op de maan is ongeveer 1,62 N/kg in plaats van 9,81 N/kg, dus is de zwaartekracht er ongeveer zes keer kleiner. De massa blijft dezelfde en de newton blijft de newton.",
    ),
    dict(
        type="waarofniet",
        vraag="De veerkracht is recht evenredig met de lengteverandering van de veer.",
        antwoord=True,
        uitleg="In Fv = k . Δl is k een constante, dus twee keer zo ver uitrekken vraagt twee keer zoveel kracht. In een grafiek geeft dat een rechte door de oorsprong.",
    ),
    dict(
        type="waarofniet",
        vraag="Een balans die kilogram aangeeft, meet eigenlijk een kracht en rekent die om.",
        antwoord=True,
        uitleg="Een weegschaal voelt hoe hard je erop duwt, dus een kracht, en deelt die door 9,81 om de massa te tonen. Op de maan zou dezelfde weegschaal daarom te weinig aangeven.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwaarder voorwerp op dezelfde vloer ondervindt een grotere wrijvingskracht.",
        antwoord=True,
        uitleg="De normaalkracht is groter, en Fw = μ . Fn. De wrijvingscoëfficiënt blijft wel dezelfde, want de materialen veranderen niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het zwaartepunt van een voorwerp ligt altijd binnen het voorwerp zelf.",
        antwoord=False,
        uitleg="Bij een ring of een hoefijzer ligt het zwaartepunt in de lege ruimte ertussen. Het is het punt waar je de zwaartekracht mag laten aangrijpen, geen stukje materie.",
    ),
    dict(
        type="waarofniet",
        vraag="De zwaarteveldsterkte en de valversnelling zijn twee verschillende getallen.",
        antwoord=False,
        uitleg="Het is hetzelfde getal met twee eenheden: in België 9,81 N/kg als zwaarteveldsterkte en 9,81 m/s² als valversnelling. Je bekijkt dezelfde g eens vanuit de kracht en eens vanuit de beweging.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor de veerconstante?",
        antwoord=["k"],
        uitleg="k, met als eenheid newton per meter. Hoe groter k, hoe stijver de veer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de zwaarteveldsterkte in België? Schrijf het getal in N/kg.",
        antwoord=["9,81", "9.81", "9,81 N/kg"],
        uitleg="9,81 N/kg. Die waarde staat bij de constanten die je op het examen krijgt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het punt waar je de zwaartekracht op een voorwerp mag laten aangrijpen?",
        antwoord=["zwaartepunt", "het zwaartepunt", "massamiddelpunt"],
        uitleg="Het zwaartepunt. Bij een regelmatig voorwerp van één materiaal ligt dat in het midden.",
    ),
    dict(
        type="invultekst",
        vraag="Een massa van 2,0 kg hangt aan een veer met k = 100 N/m. Hoeveel centimeter rekt de veer uit? Schrijf het getal in centimeter.",
        antwoord=["19,6", "20", "19.6"],
        uitleg="De veerkracht moet de zwaartekracht dragen: Fz = 2,0 . 9,81 = 19,62 N. Dan is Δl = 19,62 / 100 = 0,196 m, dus 19,6 cm.",
    ),
]
