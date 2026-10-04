# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Druk bij vaste stoffen en in vloeistoffen.

Hoort bij "druk - gaswetten" van de vakfiche fysica 2de graad
doorstroomfinaliteit, een onderdeel van 15 % waarvan dit het eerste van twee
thema's is.

Deel 1 gaat over de druk op een oppervlak: p = F/A, de eenheden Pa, kPa, hPa,
mbar en bar, en het uitleggen van toepassingen uit het dagelijkse leven, zoals
een sneeuwschoen tegenover een naaldhak. Deel 2 gaat over de druk in een
vloeistof: de hydrostatische druk p = ρ.g.h, de totale druk met de luchtdruk
erbij, het beginsel van Pascal en de hydraulische pers.

De gemiddelde luchtdruk, 1013 hPa, en de massadichtheid van water,
1000 kg/m³, staan bij de constanten die een kind op het examen krijgt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de druk op een oppervlak?",
        opties=["p = F / A", "p = A / F", "p = F . A", "p = F + A"],
        antwoord=0,
        uitleg="De kracht gedeeld door de oppervlakte waarop ze werkt. Dezelfde kracht op een kleiner oppervlak geeft dus een grotere druk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen horen bij de SI-eenheid van druk? Kruis alles aan wat juist is.",
        opties=["de pascal", "de newton per vierkante meter", "de bar", "de newtonmeter"],
        antwoord=[0, 1],
        uitleg="Eén pascal is per afspraak één newton per vierkante meter, dus zijn dat twee namen voor dezelfde eenheid. De bar mag je gebruiken maar is geen SI-eenheid, en de newtonmeter hoort bij het moment van een kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel pascal is 1 bar?",
        opties=["100 000 Pa", "1000 Pa", "100 Pa", "10 000 000 Pa"],
        antwoord=0,
        uitleg="1 bar = 100 000 Pa = 1000 hPa. Een fietsband staat vaak op 4 bar, dus 400 000 Pa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kracht van 600 N werkt op een oppervlak van 0,30 m². Hoe groot is de druk?",
        opties=["2000 Pa", "180 Pa", "200 Pa", "20 000 Pa"],
        antwoord=0,
        uitleg="p = 600 / 0,30 = 2000 Pa, of 2,0 kPa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zak je met sneeuwschoenen minder diep in de sneeuw?",
        opties=[
            "het zooloppervlak is groter, dus de druk is kleiner",
            "je gewicht wordt op sneeuwschoenen zelf kleiner",
            "de sneeuw wordt eronder harder samengepakt",
            "de kracht op de sneeuw wordt een stuk kleiner",
        ],
        antwoord=0,
        uitleg="Je gewicht verandert niet, maar het verdeelt zich over een veel groter oppervlak. Dezelfde kracht gedeeld door een grotere A geeft een kleinere p.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee mensen met dezelfde schoenmaat staan in de modder. De zwaarste zakt dieper. Waarom?",
        opties=[
            "bij dezelfde oppervlakte geeft een grotere kracht een grotere druk",
            "bij dezelfde kracht geeft een grotere oppervlakte een grotere druk",
            "de modder duwt harder terug bij een kleine massa",
            "de zwaartekracht werkt sterker op grote mensen",
        ],
        antwoord=0,
        uitleg="De oppervlakte is gelijk, dus beslist de kracht. Een grotere massa geeft een grotere zwaartekracht en daardoor meer druk op de modder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorwerpen zijn gemaakt om de druk juist zo groot mogelijk te maken? Kruis alles aan wat juist is.",
        opties=[
            "een scherp mes",
            "een punaise",
            "een brede ski",
            "een plank onder een kraanpoot",
        ],
        antwoord=[0, 1],
        uitleg="Een mes en een punaise hebben een klein contactoppervlak, dus veel druk bij weinig kracht. Een ski en een plank spreiden de kracht juist uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een blok van 240 N staat op een vierkant grondvlak van 0,20 m bij 0,20 m. Hoe groot is de druk?",
        opties=["6000 Pa", "1200 Pa", "600 Pa", "48 Pa"],
        antwoord=0,
        uitleg="De oppervlakte is 0,20 . 0,20 = 0,040 m². Dan is p = 240 / 0,040 = 6000 Pa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt hetzelfde blok op zijn kleinste zijde in plaats van op zijn grootste. Wat gebeurt er met de druk op de tafel?",
        opties=[
            "ze wordt groter",
            "ze wordt kleiner",
            "ze blijft dezelfde",
            "ze wordt nul",
        ],
        antwoord=0,
        uitleg="De kracht blijft dezelfde, want de massa verandert niet. De oppervlakte wordt kleiner, dus de druk groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een vrachtwagen met dubbele wielen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het contactoppervlak met de weg wordt groter",
            "de druk op het wegdek wordt kleiner",
            "de zwaartekracht op de vrachtwagen wordt kleiner",
            "de massa van de lading wordt kleiner",
        ],
        antwoord=[0, 1],
        uitleg="Meer wielen betekent meer contactoppervlak, en dezelfde kracht over een grotere A geeft minder druk. Zo beschadigt de vrachtwagen het wegdek minder, maar hij wordt er niet lichter van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil met een gegeven kracht een zo grote druk mogelijk maken. Wat doe je?",
        opties=[
            "het contactoppervlak zo klein mogelijk maken",
            "het contactoppervlak zo groot mogelijk maken",
            "de kracht in twee richtingen ontbinden",
            "de kracht schuin laten aangrijpen",
        ],
        antwoord=0,
        uitleg="In p = F / A staat A in de noemer, dus een kleinere oppervlakte geeft een grotere druk. Daarom slijpt men een mes scherp.",
    ),
    dict(
        type="waarofniet",
        vraag="Dezelfde kracht geeft op een kleiner oppervlak een grotere druk.",
        antwoord=True,
        uitleg="In p = F / A staat A in de noemer. Daarom prikt een naald wel door je vel en een vingertop niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een druk van 1 hPa is hetzelfde als een druk van 100 Pa.",
        antwoord=True,
        uitleg="Hecto betekent honderd, dus 1 hPa = 100 Pa. De luchtdruk van 1013 hPa is dus 101 300 Pa.",
    ),
    dict(
        type="waarofniet",
        vraag="Druk is een vectoriële grootheid, want ze heeft een richting en een zin.",
        antwoord=False,
        uitleg="Druk is een getal met een eenheid, zonder richting. De kracht in de formule is wel een vector.",
    ),
    dict(
        type="waarofniet",
        vraag="Een millibar en een hectopascal zijn even grote eenheden.",
        antwoord=True,
        uitleg="1 mbar = 1 hPa = 100 Pa. Daarom staat op een weerkaart soms mbar en soms hPa voor hetzelfde getal.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grotere kracht op hetzelfde oppervlak geeft een kleinere druk.",
        antwoord=False,
        uitleg="Omgekeerd: F staat in de teller, dus een grotere kracht geeft een grotere druk.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor druk?",
        antwoord=["p"],
        uitleg="Een kleine p, niet te verwarren met P van vermogen.",
    ),
    dict(
        type="invultekst",
        vraag="Een kracht van 50 N werkt op 0,010 m². Hoe groot is de druk in pascal? Schrijf het getal.",
        antwoord=["5000", "5000 Pa"],
        uitleg="p = 50 / 0,010 = 5000 Pa, of 5,0 kPa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel hectopascal is 1 bar? Schrijf het getal.",
        antwoord=["1000", "1000 hPa"],
        uitleg="1 bar = 100 000 Pa en 1 hPa = 100 Pa, dus 1000 hPa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de oppervlakte waarop een kracht werkt in de formule van de druk? Schrijf het symbool.",
        antwoord=["A"],
        uitleg="A, van area. De eenheid is de vierkante meter.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de hydrostatische druk in een vloeistof?",
        opties=["p = ρ . g . h", "p = ρ . g . V", "p = F / A", "p = ρ / h"],
        antwoord=0,
        uitleg="De massadichtheid van de vloeistof maal de zwaarteveldsterkte maal de diepte. Die formule staat in de bijlage van het examen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de hydrostatische druk af? Kruis alles aan wat juist is.",
        opties=[
            "de diepte in de vloeistof",
            "de massadichtheid van de vloeistof",
            "de vorm van het vat",
            "de totale hoeveelheid vloeistof in het vat",
        ],
        antwoord=[0, 1],
        uitleg="Enkel ρ, g en h staan in de formule. Op dezelfde diepte is de druk in een smal buisje even groot als in een breed bad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de hydrostatische druk op 5,0 m diepte in water?",
        opties=["49 kPa", "4,9 kPa", "490 kPa", "9,8 kPa"],
        antwoord=0,
        uitleg="p = 1000 . 9,81 . 5,0 = 49 050 Pa, dus ongeveer 49 kPa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstaat er hydrostatische druk in een vloeistof?",
        opties=[
            "het gewicht van de vloeistof erboven duwt op wat eronder zit",
            "de deeltjes van de vloeistof botsen voortdurend op elkaar",
            "de vloeistof wordt door haar eigen gewicht samengedrukt",
            "de luchtdruk duwt de hele vloeistof naar beneden",
        ],
        antwoord=0,
        uitleg="Elke laag vloeistof draagt het gewicht van alles erboven. Daarom groeit de druk gelijkmatig met de diepte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de totale druk op 10 m diepte in een meer?",
        opties=[
            "de hydrostatische druk plus de luchtdruk",
            "enkel de hydrostatische druk",
            "enkel de luchtdruk",
            "de hydrostatische druk min de luchtdruk",
        ],
        antwoord=0,
        uitleg="Boven het water duwt de atmosfeer al met 1013 hPa. Die druk komt bij de hydrostatische druk van het water erboven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het beginsel van Pascal?",
        opties=[
            "een drukverandering plant zich in heel de vloeistof voort",
            "de druk neemt toe met de diepte",
            "de archimedeskracht is gelijk aan het gewicht van de weggeduwde vloeistof",
            "de druk hangt af van de vorm van het vat",
        ],
        antwoord=0,
        uitleg="Duw je ergens op een ingesloten vloeistof, dan stijgt de druk overal met hetzelfde bedrag. Daar werkt een hydraulische pers op.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een hydraulische pers duw je op een kleine zuiger en komt er een grote kracht uit de grote zuiger. Hoe kan dat?",
        opties=[
            "de druk is overal gelijk, dus geeft een grotere A meer kracht",
            "de druk wordt bij de grote zuiger zelf veel groter",
            "de vloeistof maakt onderweg energie bij",
            "de kleine zuiger beweegt veel sneller dan de grote",
        ],
        antwoord=0,
        uitleg="Uit p = F / A volgt F = p . A. Bij dezelfde druk levert de tien keer grotere zuiger tien keer meer kracht, maar hij komt ook tien keer minder ver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je je oren klaren als je duikt?",
        opties=[
            "de druk op het trommelvlies groeit met de diepte",
            "de druk in je oor groeit mee met de diepte",
            "de luchtdruk verdwijnt zodra je onder water zit",
            "het water is dieper een stuk kouder dan boven",
        ],
        antwoord=0,
        uitleg="Buiten het trommelvlies stijgt de druk met de diepte, binnen blijft ze gelijk. Klaren laat lucht door de buis van Eustachius zodat de druk aan beide kanten even groot wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duikt in zeewater in plaats van in zoet water, op dezelfde diepte. Welke uitspraken zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de hydrostatische druk is groter",
            "de massadichtheid van het water is groter",
            "de diepte telt niet meer mee",
            "de luchtdruk boven het water is groter",
        ],
        antwoord=[0, 1],
        uitleg="Zeewater heeft een grotere ρ, en ρ staat in de formule. De diepte telt nog altijd mee, en de luchtdruk boven de zee is dezelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk meetinstrument meet de luchtdruk?",
        opties=["een barometer", "een manometer", "een dynamometer", "een calorimeter"],
        antwoord=0,
        uitleg="Een barometer meet de luchtdruk. Een manometer meet de druk in een vat of een leiding, meestal als over- of onderdruk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke diepte in water is de hydrostatische druk ongeveer even groot als de luchtdruk van 1013 hPa?",
        opties=["ongeveer 10 m", "ongeveer 1 m", "ongeveer 100 m", "ongeveer 0,1 m"],
        antwoord=0,
        uitleg="Uit h = p / (ρ.g) = 101 300 / (1000 . 9,81) volgt ongeveer 10,3 m. Op 10 m diepte is de totale druk dus al bijna het dubbele van aan het oppervlak.",
    ),
    dict(
        type="waarofniet",
        vraag="De hydrostatische druk op dezelfde diepte is in een smalle buis even groot als in een breed vat.",
        antwoord=True,
        uitleg="In p = ρ.g.h staat de vorm van het vat niet. Enkel de diepte en de vloeistof tellen mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Een manometer die 2 bar overdruk aangeeft, meet een totale druk van ongeveer 3 bar.",
        antwoord=True,
        uitleg="Overdruk is wat er boven de luchtdruk zit. De luchtdruk is ongeveer 1 bar, dus de totale druk is ongeveer 3 bar.",
    ),
    dict(
        type="waarofniet",
        vraag="De luchtdruk wordt hoger als je een berg opklimt.",
        antwoord=False,
        uitleg="Hoger in de atmosfeer zit er minder lucht boven je, dus is de luchtdruk kleiner. Op een hoge berg is ze maar twee derde van die aan de zee.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een hydraulische pers krijg je meer energie uit de grote zuiger dan je in de kleine stopt.",
        antwoord=False,
        uitleg="De kracht wordt groter, maar de weg wordt even veel kleiner. De arbeid blijft dus dezelfde, op de wrijving na.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vloeistof oefent ook druk uit op de zijwanden van haar vat.",
        antwoord=True,
        uitleg="De druk in een vloeistof werkt in alle richtingen. Daarom spuit er water uit een gaatje in de zijkant van een emmer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de gemiddelde luchtdruk? Schrijf het getal in hPa.",
        antwoord=["1013", "1013 hPa"],
        uitleg="1013 hPa, dus 101 300 Pa of ongeveer 1 bar. Die waarde staat bij de constanten van het examen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk meetinstrument gebruikt men om de druk in een gasvat te meten?",
        antwoord=["manometer", "een manometer", "drukmeter"],
        uitleg="Een manometer. Voor de luchtdruk buiten gebruikt men een barometer.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de hydrostatische druk op 2,0 m diepte in water? Schrijf het getal in kPa, afgerond op een eenheid.",
        antwoord=["20", "20 kPa", "19,6"],
        uitleg="p = 1000 . 9,81 . 2,0 = 19 620 Pa, dus ongeveer 20 kPa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een druk die kleiner is dan de luchtdruk? Schrijf het woord.",
        antwoord=["onderdruk", "de onderdruk", "vacuüm"],
        uitleg="Onderdruk. Zit de druk boven de luchtdruk, dan heet het overdruk.",
    ),
]
