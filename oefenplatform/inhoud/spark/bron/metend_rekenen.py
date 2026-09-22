# -*- coding: utf-8 -*-
"""De vragen voor "Metend rekenen" (✨ Spark, wiskunde).

De vakfiche zet hieronder: grootheden en eenheden (tijd, lengte, oppervlakte,
volume, massa), omzetten en afronden, omtrek van veelhoeken en van de cirkel,
oppervlakte van driehoeken, vierhoeken en cirkels, en oppervlakte én volume
van kubus, balk en cilinder.

Bij de cirkel rekenen we met π ≈ 3,14, en dat staat telkens in de vraag zelf.
Zo hoeft een kind niet te gokken met hoeveel cijfers er verwacht wordt.

Deel 1 gaat over eenheden en de gewone formules. Deel 2 vraagt samengestelde
figuren, ruimtefiguren en omgekeerd rekenen (van oppervlakte naar zijde).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je wil de afstand tussen twee steden opschrijven. Welke eenheid past het best?",
        opties=["Kilometer", "Centimeter", "Milliliter"],
        antwoord=0,
        uitleg="Kilometer. Een geschikte eenheid kiezen scheelt veel nullen: 120 km leest makkelijker dan 12 000 000 cm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel centimeter is 1 meter?",
        antwoord="100",
        uitleg="1 m = 100 cm. Elke stap op de maatladder is maal of gedeeld door 10, en van meter naar centimeter zijn het twee stappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel meter is 3,5 km?",
        opties=["3500 m", "350 m", "35 m"],
        antwoord=0,
        uitleg="1 km = 1000 m, dus 3,5 × 1000 = 3500 m.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel minuten is 2,5 uur?",
        antwoord="150",
        uitleg="Een uur heeft 60 minuten: 2,5 × 60 = 150 minuten. Let op, tijd gaat niet per tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel seconden zijn er in een kwartier?",
        opties=["900", "150", "1500"],
        antwoord=0,
        uitleg="Een kwartier is 15 minuten, en elke minuut heeft 60 seconden: 15 × 60 = 900 s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel gram is 2,5 kg?",
        opties=["2500 g", "250 g", "25 000 g"],
        antwoord=0,
        uitleg="1 kg = 1000 g, dus 2,5 × 1000 = 2500 g.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel milliliter gaat er in een halve liter?",
        opties=["500 ml", "50 ml", "5000 ml"],
        antwoord=0,
        uitleg="1 l = 1000 ml, dus een halve liter is 500 ml.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de omtrek van een rechthoek van 7 cm bij 3 cm, in centimeter?",
        antwoord="20",
        uitleg="Omtrek = 2 × (lengte + breedte) = 2 × (7 + 3) = 20 cm. Je loopt één keer rond de figuur.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de oppervlakte van een rechthoek van 7 cm bij 3 cm, in cm²?",
        antwoord="21",
        uitleg="Oppervlakte = lengte × breedte = 7 × 3 = 21 cm². Let op de eenheid: oppervlakte staat in cm², omtrek in cm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vierkant heeft een zijde van 6 cm. Wat is zijn omtrek?",
        opties=["24 cm", "36 cm", "12 cm"],
        antwoord=0,
        uitleg="Vier gelijke zijden: 4 × 6 = 24 cm. Met 6 × 6 = 36 krijg je de oppervlakte, en die staat in cm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een driehoek heeft een basis van 8 cm en een hoogte van 5 cm. Wat is zijn oppervlakte?",
        opties=["20 cm²", "40 cm²", "13 cm²"],
        antwoord=0,
        uitleg="Oppervlakte driehoek = (basis × hoogte) : 2 = (8 × 5) : 2 = 20 cm². De helft van een rechthoek met dezelfde maten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een parallellogram heeft een basis van 9 cm en een hoogte van 4 cm. Wat is zijn oppervlakte?",
        opties=["36 cm²", "18 cm²", "26 cm²"],
        antwoord=0,
        uitleg="Bij een parallellogram is het basis × hoogte = 9 × 4 = 36 cm², zonder delen door 2. En de hoogte is de loodrechte afstand, niet de schuine zijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de formule voor de omtrek van een cirkel?",
        opties=["2 × π × straal", "π × straal × straal", "π × straal"],
        antwoord=0,
        uitleg="De omtrek is 2 × π × straal, of even goed π × diameter. Met π × straal² bereken je de oppervlakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cirkel heeft een straal van 5 cm. Hoe groot is de omtrek? Neem π = 3,14.",
        opties=["31,4 cm", "15,7 cm", "78,5 cm"],
        antwoord=0,
        uitleg="Omtrek = 2 × π × straal = 2 × 3,14 × 5 = 31,4 cm. Met 78,5 zou je de oppervlakte hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cirkel heeft een straal van 5 cm. Hoe groot is de oppervlakte? Neem π = 3,14.",
        opties=["78,5 cm²", "31,4 cm²", "15,7 cm²"],
        antwoord=0,
        uitleg="Oppervlakte = π × straal² = 3,14 × 25 = 78,5 cm². In de formule kwadrateer je de straal, je vermenigvuldigt niet met 2.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het volume van een kubus met een ribbe van 4 cm, in cm³?",
        antwoord="64",
        uitleg="Volume kubus = ribbe³ = 4 × 4 × 4 = 64 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een balk is 5 cm bij 3 cm bij 2 cm. Wat is zijn volume?",
        opties=["30 cm³", "60 cm³", "10 cm³"],
        antwoord=0,
        uitleg="Volume balk = lengte × breedte × hoogte = 5 × 3 × 2 = 30 cm³.",
    ),
    dict(
        type="waarofniet",
        vraag="1 liter is hetzelfde als 1 dm³.",
        antwoord=True,
        uitleg="Juist. Een kubus van 1 dm bij 1 dm bij 1 dm bevat precies 1 liter. En 1 ml is 1 cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 2,5 m² in dm²?",
        opties=["250 dm²", "25 dm²", "2500 dm²"],
        antwoord=0,
        uitleg="Bij oppervlakte gaat elke stap maal 100, niet maal 10: 2,5 × 100 = 250 dm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Rond 12,467 af tot op twee decimalen.",
        opties=["12,47", "12,46", "12,5"],
        antwoord=0,
        uitleg="Het derde decimaal is 7, dus het cijfer ervoor gaat één omhoog: 12,47.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een vierkant heeft een oppervlakte van 49 cm². Hoe lang is een zijde?",
        opties=["7 cm", "24,5 cm", "12,25 cm"],
        antwoord=0,
        uitleg="Zijde × zijde = 49, dus de zijde is √49 = 7 cm. Hier gebruik je worteltrekken als omgekeerde van kwadrateren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechthoek heeft een oppervlakte van 48 cm² en een lengte van 8 cm. Hoe breed is hij?",
        opties=["6 cm", "40 cm", "16 cm"],
        antwoord=0,
        uitleg="Oppervlakte : lengte = breedte, dus 48 : 8 = 6 cm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een trapezium heeft evenwijdige zijden van 6 cm en 10 cm en een hoogte van 4 cm. Wat is zijn oppervlakte?",
        opties=["32 cm²", "40 cm²", "64 cm²"],
        antwoord=0,
        uitleg="Oppervlakte trapezium = (som van de evenwijdige zijden) × hoogte : 2 = (6 + 10) × 4 : 2 = 32 cm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ruit heeft diagonalen van 8 cm en 6 cm. Wat is zijn oppervlakte?",
        opties=["24 cm²", "48 cm²", "14 cm²"],
        antwoord=0,
        uitleg="Oppervlakte ruit = (diagonaal × diagonaal) : 2 = (8 × 6) : 2 = 24 cm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cirkel heeft een diameter van 10 cm. Hoe groot is de omtrek? Neem π = 3,14.",
        opties=["31,4 cm", "62,8 cm", "78,5 cm"],
        antwoord=0,
        uitleg="Omtrek = π × diameter = 3,14 × 10 = 31,4 cm. Let op of er een straal of een diameter gegeven is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de oppervlakte van een kubus met een ribbe van 3 cm?",
        opties=["54 cm²", "27 cm²", "9 cm²"],
        antwoord=0,
        uitleg="Een kubus heeft zes gelijke vierkanten: 6 × (3 × 3) = 54 cm². Met 27 zou je het volume hebben, en dat staat in cm³.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een balk is 5 cm bij 4 cm bij 2 cm. Wat is zijn totale oppervlakte?",
        opties=["76 cm²", "40 cm²", "38 cm²"],
        antwoord=0,
        uitleg="Drie paar vlakken: 2 × (5 × 4) + 2 × (5 × 2) + 2 × (4 × 2) = 40 + 20 + 16 = 76 cm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cilinder heeft een straal van 3 cm en een hoogte van 10 cm. Wat is zijn volume? Neem π = 3,14.",
        opties=["282,6 cm³", "94,2 cm³", "188,4 cm³"],
        antwoord=0,
        uitleg="Volume cilinder = π × straal² × hoogte = 3,14 × 9 × 10 = 282,6 cm³.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel liter gaat er in een kubus van 2 dm bij 2 dm bij 2 dm?",
        antwoord="8",
        uitleg="2 × 2 × 2 = 8 dm³, en 1 dm³ is 1 liter, dus 8 liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zwembad van 10 m bij 5 m staat 1,5 m vol water. Hoeveel liter is dat?",
        opties=["75 000 l", "75 l", "7500 l"],
        antwoord=0,
        uitleg="Volume = 10 × 5 × 1,5 = 75 m³. Eén m³ is 1000 liter, dus 75 000 liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 3 m² in cm²?",
        opties=["30 000 cm²", "300 cm²", "3000 cm²"],
        antwoord=0,
        uitleg="Van m naar cm is maal 100, dus bij oppervlakte maal 100 × 100 = 10 000. Dat geeft 3 × 10 000 = 30 000 cm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 2 m³ in liter?",
        opties=["2000 l", "200 l", "20 l"],
        antwoord=0,
        uitleg="1 m³ = 1000 dm³ = 1000 liter, dus 2 m³ = 2000 liter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tuin van 20 m bij 15 m: hoeveel are is dat?",
        opties=["3 are", "30 are", "300 are"],
        antwoord=0,
        uitleg="20 × 15 = 300 m², en 1 are is 100 m², dus 3 are. Een hectare is 100 are, ofwel 10 000 m².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een figuur bestaat uit een vierkant van 6 cm met daarop een halve cirkel met diameter 6 cm. Wat is de oppervlakte? Neem π = 3,14.",
        opties=["50,13 cm²", "64,26 cm²", "42,13 cm²"],
        antwoord=0,
        uitleg="Vierkant: 6 × 6 = 36. Halve cirkel met straal 3: (3,14 × 9) : 2 = 14,13. Samen 50,13 cm². Bij samengestelde figuren splits je in stukken die je wél kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit een vierkant van 10 cm knip je in elke hoek een vierkantje van 2 cm. Wat blijft er over aan oppervlakte?",
        opties=["84 cm²", "96 cm²", "64 cm²"],
        antwoord=0,
        uitleg="Het grote vierkant is 100 cm². Vier vierkantjes van 2 × 2 = 4 cm² geven samen 16 cm². Blijft over: 100 − 16 = 84 cm².",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wandelpad van 1,2 km leg je af in 15 minuten. Hoeveel meter per minuut is dat?",
        opties=["80 m", "8 m", "800 m"],
        antwoord=0,
        uitleg="1,2 km is 1200 m, en 1200 : 15 = 80 meter per minuut. Zet altijd eerst alles in dezelfde eenheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee rechthoeken met dezelfde omtrek hebben ook dezelfde oppervlakte.",
        antwoord=False,
        uitleg="Nee. Een rechthoek van 1 bij 5 en een van 3 bij 3 hebben allebei omtrek 12, maar de oppervlaktes zijn 5 en 9.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt de zijde van een vierkant. Wat gebeurt er met de oppervlakte?",
        opties=["Ze wordt vier keer zo groot", "Ze wordt dubbel zo groot", "Ze blijft gelijk"],
        antwoord=0,
        uitleg="Een vierkant van 3 cm heeft oppervlakte 9 cm², een van 6 cm heeft 36 cm². Dat is vier keer zo veel, want allebei de afmetingen verdubbelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een recept vraagt 250 ml melk. Hoeveel pakjes van 1 liter heb je nodig voor 5 keer het recept?",
        opties=["2 pakjes", "1 pakje", "5 pakjes"],
        antwoord=0,
        uitleg="5 × 250 = 1250 ml, dus 1,25 liter. Eén pakje is te weinig, dus je hebt er 2 nodig. Hier rond je naar boven af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plan heeft schaal 1 : 200. Een muur is 4 cm op het plan. Hoe lang is hij in het echt?",
        opties=["8 m", "80 m", "800 m"],
        antwoord=0,
        uitleg="4 × 200 = 800 cm, en dat is 8 meter. Zet de uitkomst altijd om naar een eenheid die past bij wat je meet.",
    ),
]
