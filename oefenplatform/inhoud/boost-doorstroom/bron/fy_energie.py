# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Arbeid, energie, vermogen en rendement.

Hoort bij "energie" van de vakfiche fysica 2de graad doorstroomfinaliteit, een
onderdeel van 10 % en daarmee één thema.

Deel 1 gaat over arbeid en de energievormen: W = F.Δx.cos α, positieve,
negatieve of geen arbeid, de kinetische energie, de potentiële gravitationele
energie en de potentiële elastische energie, en het onderscheid tussen een
open, een gesloten en een geïsoleerd systeem. Deel 2 gaat over de energiebalans
en de wet van behoud van energie, over de energiedissipatie naar warmte, en
over het rekenen met vermogen P = |ΔE|/Δt en rendement η = Enuttig/Etotaal.

Het arbeid-energietheorema staat op de fiche: de arbeid van de resulterende
kracht is gelijk aan de verandering van de kinetische energie. De tweede wet van
Newton staat er niet, dus de kracht zelf komt altijd uit de opgave.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de arbeid van een kracht?",
        opties=[
            "W = F . Δx . cos α",
            "W = F . Δx . sin α",
            "W = F / Δx",
            "W = F . Δx²",
        ],
        antwoord=0,
        uitleg="De kracht maal de verplaatsing maal de cosinus van de hoek tussen beide. Werkt de kracht in de zin van de verplaatsing, dan is cos α gelijk aan 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de SI-eenheid van arbeid en van energie?",
        opties=["de joule", "de newton", "de watt", "de newtonmeter"],
        antwoord=0,
        uitleg="De joule (J). Eén joule is één newton maal één meter, maar die naam blijft voorbehouden aan het moment van een kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duwt een kar 8,0 m vooruit met een kracht van 50 N in de zin van de beweging. Hoeveel arbeid verricht je?",
        opties=["400 J", "6,3 J", "58 J", "40 J"],
        antwoord=0,
        uitleg="W = 50 . 8,0 . cos 0° = 400 J, want cos 0° is 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een wrijvingskracht werkt tegen de beweging in. Welke arbeid verricht ze?",
        opties=["negatieve arbeid", "positieve arbeid", "geen arbeid", "dat hangt van de massa af"],
        antwoord=0,
        uitleg="De hoek tussen de kracht en de verplaatsing is 180°, en cos 180° is −1. De wrijving haalt dus energie uit de beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je draagt een doos horizontaal door een kamer. Welke arbeid verricht de kracht waarmee je de doos omhoog houdt?",
        opties=["geen arbeid", "positieve arbeid", "negatieve arbeid", "evenveel als de zwaartekracht"],
        antwoord=0,
        uitleg="De kracht is verticaal en de verplaatsing horizontaal, dus de hoek is 90° en cos 90° is nul. De arbeid is dan nul, al voelt het zwaar aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de kinetische energie?",
        opties=["Ek = m . v² / 2", "Ek = m . v / 2", "Ek = m . g . h", "Ek = k . Δl² / 2"],
        antwoord=0,
        uitleg="De halve massa maal het kwadraat van de snelheid. Twee keer zo snel geeft dus vier keer zoveel kinetische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto van 1200 kg rijdt met 20 m/s. Hoeveel kinetische energie heeft hij?",
        opties=["240 kJ", "24 kJ", "12 kJ", "480 kJ"],
        antwoord=0,
        uitleg="Ek = 1200 . 20² / 2 = 1200 . 400 / 2 = 240 000 J, dus 240 kJ.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een massa van 5,0 kg wordt 3,0 m omhoog getild. Hoeveel potentiële gravitationele energie komt erbij?",
        opties=["147 J", "15 J", "1,5 J", "1470 J"],
        antwoord=0,
        uitleg="Ep,gr = m . g . h = 5,0 . 9,81 . 3,0 = 147,15 J, dus ongeveer 147 J.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft de potentiële elastische energie van een ingedrukte veer?",
        opties=["Ep,el = k . Δl² / 2", "Ep,el = k . Δl / 2", "Ep,el = k . Δl", "Ep,el = m . g . Δl"],
        antwoord=0,
        uitleg="De veerconstante maal het kwadraat van de lengteverandering, gedeeld door twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze vier zijn echte energievormen? Kruis alles aan wat juist is.",
        opties=[
            "stralingsenergie",
            "chemische energie",
            "wrijvingsenergie",
            "drukenergie",
        ],
        antwoord=[0, 1],
        uitleg="Stralingsenergie en chemische energie horen bij de energievormen, naast de kinetische, de twee potentiële, de thermische, de elektrische en de kernenergie. Wrijving is een kracht en druk een grootheid, geen van beide een energievorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een geïsoleerd systeem zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er gaat geen energie in of uit",
            "er gaat geen materie in of uit",
            "de energie erin kan niet van vorm veranderen",
            "het is hetzelfde als een open systeem",
        ],
        antwoord=[0, 1],
        uitleg="Een geïsoleerd systeem wisselt noch materie noch energie uit. Binnenin mag de energie wel van vorm veranderen, zolang de som gelijk blijft. Een gesloten systeem houdt enkel de materie binnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht die loodrecht op de verplaatsing staat, verricht toch arbeid.",
        antwoord=False,
        uitleg="cos 90° is nul, dus W is nul. De normaalkracht op een voorwerp dat over een vlakke vloer schuift, verricht dus geen arbeid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp dat stilstaat, kan toch potentiële energie hebben.",
        antwoord=True,
        uitleg="Een steen bovenop een muur heeft Ep,gr door zijn hoogte, ook al beweegt hij niet. Enkel de kinetische energie is dan nul.",
    ),
    dict(
        type="waarofniet",
        vraag="Een auto die twee keer zo snel rijdt, heeft twee keer zoveel kinetische energie.",
        antwoord=False,
        uitleg="De snelheid staat in het kwadraat, dus wordt het vier keer zoveel. Daarom is een remweg bij dubbele snelheid vier keer zo lang.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kilowattuur is een eenheid van vermogen.",
        antwoord=False,
        uitleg="Een kilowattuur is een eenheid van energie: een vermogen maal een tijd. Eén kWh is 3,6 miljoen joule.",
    ),
    dict(
        type="waarofniet",
        vraag="De arbeid van de zwaartekracht op een voorwerp dat je optilt, is negatief.",
        antwoord=True,
        uitleg="De zwaartekracht wijst naar beneden en de verplaatsing naar boven, dus is de hoek 180°. Jij verricht dan positieve arbeid tegen de zwaartekracht in.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor arbeid?",
        antwoord=["W"],
        uitleg="W, van het Engelse work. De eenheid is de joule.",
    ),
    dict(
        type="invultekst",
        vraag="Een kracht van 25 N werkt over 4,0 m in de zin van de beweging. Hoeveel joule arbeid is dat? Schrijf het getal.",
        antwoord=["100", "100 J"],
        uitleg="W = 25 . 4,0 . 1 = 100 J.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de energie die een voorwerp heeft door zijn snelheid? Schrijf het woord bij energie.",
        antwoord=["kinetische", "kinetisch", "kinetische energie"],
        uitleg="De kinetische energie, met de formule m.v²/2.",
    ),
    dict(
        type="invultekst",
        vraag="Een massa van 2,0 kg hangt 10 m hoog. Hoeveel potentiële gravitationele energie heeft ze in joule? Schrijf het getal, afgerond op een eenheid.",
        antwoord=["196", "196 J", "200"],
        uitleg="Ep,gr = 2,0 . 9,81 . 10 = 196,2 J.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van behoud van energie?",
        opties=[
            "energie verdwijnt niet, ze verandert van vorm",
            "energie kan uit het niets ontstaan",
            "energie gaat bij elke omzetting verloren",
            "energie blijft altijd in dezelfde vorm",
        ],
        antwoord=0,
        uitleg="In een geïsoleerd systeem blijft de som van alle energie gelijk. Wat je kwijt lijkt te zijn, zit meestal als warmte in de omgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is energiedissipatie?",
        opties=[
            "bruikbare energie wordt een minder bruikbare vorm",
            "energie verdwijnt bij een omzetting helemaal",
            "warmte wordt opnieuw bruikbare energie",
            "energie wordt opgeslagen in een batterij",
        ],
        antwoord=0,
        uitleg="Bij elke omzetting gaat een deel naar warmte die je niet meer kan gebruiken. De energie is er nog, maar niet meer nuttig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft het vermogen?",
        opties=["P = |ΔE| / Δt", "P = ΔE . Δt", "P = Δt / |ΔE|", "P = F . Δx"],
        antwoord=0,
        uitleg="De omgezette energie gedeeld door de tijd die het duurde. De eenheid is de watt, dus joule per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lift verzet 48 kJ in 20 s. Welk vermogen levert hij?",
        opties=["2,4 kW", "960 kW", "0,42 kW", "24 kW"],
        antwoord=0,
        uitleg="P = 48 000 / 20 = 2400 W, dus 2,4 kW.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke formule geeft het rendement?",
        opties=[
            "η = Enuttig / Etotaal",
            "η = Etotaal / Enuttig",
            "η = Enuttig . Etotaal",
            "η = Etotaal − Enuttig",
        ],
        antwoord=0,
        uitleg="De nuttige energie gedeeld door de totale energie die je erin stopte. Het resultaat is een getal tussen 0 en 1, vaak als percentage geschreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lamp krijgt 60 J elektrische energie en geeft 9,0 J licht. Wat is het rendement?",
        opties=["15 %", "85 %", "6,7 %", "54 %"],
        antwoord=0,
        uitleg="η = 9,0 / 60 = 0,15, dus 15 %. De overige 51 J wordt warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een motor krijgt 2000 J en verliest 1400 J als warmte. Wat is zijn rendement?",
        opties=["30 %", "70 %", "140 %", "43 %"],
        antwoord=0,
        uitleg="De nuttige energie is 2000 − 1400 = 600 J, dus η = 600 / 2000 = 0,30.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal valt van een muur. Welke omzetting gebeurt er tijdens de val?",
        opties=[
            "potentiële gravitationele energie naar kinetische energie",
            "kinetische energie naar potentiële gravitationele energie",
            "chemische energie naar warmte",
            "elastische energie naar stralingsenergie",
        ],
        antwoord=0,
        uitleg="De hoogte neemt af en de snelheid toe. De potentiële gravitationele energie wordt dus kinetische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke omzettingen gebeuren er in een elektrische waterkoker? Kruis alles aan wat juist is.",
        opties=[
            "elektrische energie wordt thermische energie",
            "een deel van de warmte gaat naar de omgeving",
            "thermische energie wordt elektrische energie",
            "chemische energie wordt kinetische energie",
        ],
        antwoord=[0, 1],
        uitleg="De weerstand zet elektrische energie om in warmte voor het water, en een deel ontsnapt via de wand en de damp. Het omgekeerde gebeurt niet in een waterkoker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een stroomdiagram van een energieomzetting zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "de breedte van een pijl hoort bij de hoeveelheid energie",
            "alle uitgaande energie samen is zoveel als de ingaande",
            "de ongewenste energie laat je er gewoon buiten",
            "het diagram toont enkel de nuttige energie erin",
        ],
        antwoord=[0, 1],
        uitleg="Een stroomdiagram laat zien waar de energie naartoe gaat, nuttig én ongewenst. Door de wet van behoud van energie moet alles wat ingaat er ook weer uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het arbeid-energietheorema?",
        opties=[
            "de arbeid van de resultante is de verandering van de Ek",
            "de arbeid van een kracht is gelijk aan de potentiële energie",
            "de arbeid van de wrijvingskracht is altijd gelijk aan nul",
            "arbeid en vermogen zijn eigenlijk dezelfde grootheid",
        ],
        antwoord=0,
        uitleg="Verricht de resulterende kracht positieve arbeid, dan gaat het voorwerp sneller. Verricht ze negatieve arbeid, dan vertraagt het.",
    ),
    dict(
        type="waarofniet",
        vraag="Een rendement van meer dan 100 % kan niet bestaan.",
        antwoord=True,
        uitleg="Je kan er niet meer uithalen dan je erin stopt, want energie ontstaat niet uit het niets. Er gaat altijd een deel naar warmte, dus het blijft onder 100 %.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vrije val, zonder luchtweerstand, blijft de som van de kinetische en de potentiële gravitationele energie gelijk.",
        antwoord=True,
        uitleg="De ene vorm wordt de andere, zonder verlies. Daarom kan je de snelheid onderaan uit de hoogte berekenen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een toestel met een groter vermogen gebruikt bij hetzelfde werk altijd meer energie.",
        antwoord=False,
        uitleg="Een groter vermogen betekent dat het sneller gaat, niet dat het meer energie kost. Een krachtiger pomp verzet hetzelfde water in minder tijd met ongeveer dezelfde energie.",
    ),
    dict(
        type="waarofniet",
        vraag="De energie die als warmte naar de omgeving verdwijnt, is verloren en bestaat niet meer.",
        antwoord=False,
        uitleg="Ze bestaat nog, maar is zo verspreid dat je ze niet meer nuttig kan gebruiken. Dat heet energiedissipatie, niet verdwijnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het joule-effect is in elke toepassing ongewenst.",
        antwoord=False,
        uitleg="In een gloeilamp of een waterkoker heb je die opwarming net nodig. In een laadkabel of een stekkerdoos is dezelfde opwarming wel ongewenst.",
    ),
    dict(
        type="invultekst",
        vraag="Welk symbool gebruikt men voor rendement?",
        antwoord=["η", "eta", "n"],
        uitleg="De Griekse letter η (eta). Ze heeft geen eenheid, want het is een verhouding.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de SI-eenheid van vermogen? Schrijf de naam van de eenheid.",
        antwoord=["watt", "de watt", "W"],
        uitleg="De watt, en één watt is één joule per seconde.",
    ),
    dict(
        type="invultekst",
        vraag="Een toestel van 500 W staat 60 s aan. Hoeveel joule energie gebruikt het? Schrijf het getal.",
        antwoord=["30000", "30 000", "30000 J"],
        uitleg="ΔE = P . Δt = 500 . 60 = 30 000 J, dus 30 kJ.",
    ),
    dict(
        type="invultekst",
        vraag="Een motor krijgt 800 J en levert 200 J nuttig. Hoeveel procent is het rendement? Schrijf het getal.",
        antwoord=["25", "25 %", "25%"],
        uitleg="η = 200 / 800 = 0,25, dus 25 %.",
    ),
]
