# -*- coding: utf-8 -*-
"""Arbeid, energie en vermogen — 🌍 Beyond, fysica.

Deel 1 gaat over arbeid: wanneer een kracht arbeid verricht en wanneer niet,
het verschil tussen een constante en een niet-constante kracht, de arbeid als
oppervlakte onder een F(x)-grafiek, en het onderscheid tussen conservatieve en
niet-conservatieve krachten. Deel 2 gaat over energie: kinetische energie,
gravitationele en elastische potentiële energie, het arbeid-energietheorema,
het behoud van energie met en zonder wrijving, en het vermogen.

Het onderscheid conservatief of niet is het scharnier van dit thema. Bij een
conservatieve kracht kan je met potentiële energie werken en telt alleen begin
en einde; bij wrijving moet je de hele weg kennen, want de energie gaat als
warmte verloren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer verricht een kracht arbeid?",
        opties=[
            "als het aangrijpingspunt verplaatst wordt in de zin van de kracht",
            "als de kracht groot genoeg is, ook zonder verplaatsing",
            "als de kracht lang genoeg blijft duwen tegen het lichaam",
            "als de kracht loodrecht op de verplaatsing staat",
        ],
        antwoord=0,
        uitleg="Duw je tegen een muur die niet wijkt, dan is de arbeid nul, hoe moe je ook "
        "wordt. Fysische arbeid is iets anders dan inspanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kracht van 40 N verplaatst een kist 3 m in dezelfde zin. Hoeveel arbeid is er verricht?",
        opties=[
            "120 J",
            "13 J",
            "43 J",
            "1200 J",
        ],
        antwoord=0,
        uitleg="Arbeid is kracht maal verplaatsing: 40 maal 3 is 120 joule.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je arbeid uit?",
        antwoord=["joule", "J", "de joule"],
        uitleg="Eén joule is één newton maal één meter. Het is ook de eenheid van energie, "
        "want arbeid is een omzetting van energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kelner die een blad met glazen horizontaal draagt, verricht arbeid op dat blad.",
        antwoord=False,
        uitleg="Hij duwt het blad omhoog en beweegt het vooruit, dus staat de kracht "
        "loodrecht op de verplaatsing. De arbeid van die kracht is daarom nul.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer verricht een kracht geen arbeid? Kruis alles aan wat juist is.",
        opties=[
            "als er geen verplaatsing is",
            "als de kracht loodrecht op de verplaatsing staat",
            "als de kracht zelf nul is",
            "als de verplaatsing tegen de kracht in gaat",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gaat de verplaatsing tegen de kracht in, dan is de arbeid negatief en dus "
        "niet nul. Daarom verricht de zwaartekracht geen arbeid als je horizontaal schuift.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af uit de oppervlakte onder een F(x)-grafiek?",
        opties=[
            "de verrichte arbeid",
            "de snelheid van het lichaam",
            "het vermogen van de kracht",
            "de massa van het lichaam",
        ],
        antwoord=0,
        uitleg="Kracht maal afstand is arbeid, en dat is precies een oppervlakte. Zo kan je "
        "ook met een kracht rekenen die onderweg verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten zijn niet constant? Kruis alles aan wat juist is.",
        opties=[
            "de veerkracht",
            "de gravitatiekracht op grote afstandsverschillen",
            "de zwaartekracht vlak bij het aardoppervlak",
            "een duwkracht die je constant houdt",
        ],
        antwoord=[0, 1],
        uitleg="De veerkracht groeit met de uitrekking en de gravitatiekracht daalt met r². "
        "Voor hun arbeid neem je de oppervlakte onder de grafiek of een integraal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een conservatieve kracht?",
        opties=[
            "een kracht waarvan de arbeid niet van de gevolgde weg afhangt",
            "een kracht die altijd dezelfde grootte houdt",
            "een kracht die altijd arbeid aan een lichaam onttrekt",
            "een kracht die enkel bij hoge snelheid werkt",
        ],
        antwoord=0,
        uitleg="Alleen begin- en eindpunt tellen. Daarom kan je er een potentiële energie "
        "bij definiëren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten zijn conservatief? Kruis alles aan wat juist is.",
        opties=[
            "de zwaartekracht",
            "de veerkracht",
            "de wrijvingskracht",
            "de remkracht van een rem",
        ],
        antwoord=[0, 1],
        uitleg="Ook de gravitatiekracht en de coulombkracht zijn conservatief. Wrijving, "
        "spierkracht en motorkracht zijn dat niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een kracht waarvan de arbeid wél van de gevolgde weg afhangt?",
        antwoord=["niet-conservatief", "niet conservatief", "dissipatief"],
        uitleg="Wrijving is het schoolvoorbeeld: hoe langer de weg, hoe meer energie er als "
        "warmte verdwijnt. Daarom kan je er geen potentiële energie bij definiëren.",
    ),
    dict(
        type="waarofniet",
        vraag="De arbeid van de wrijvingskracht is altijd negatief.",
        antwoord=True,
        uitleg="Ze wijst tegen de beweging in, dus onttrekt ze energie aan het lichaam. Die "
        "energie komt als warmte in het oppervlak en het lichaam terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je tilt een doos van 10 kg 1,5 m hoog. Hoeveel arbeid lever je? Neem g gelijk aan 10 N/kg.",
        opties=[
            "150 J",
            "15 J",
            "100 J",
            "1500 J",
        ],
        antwoord=0,
        uitleg="De zwaartekracht is 100 newton en de hoogte 1,5 meter: samen 150 joule. Die "
        "energie zit daarna als potentiële energie in de doos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist schuift 4 m over een vloer met een wrijvingskracht van 25 N. Hoeveel arbeid verricht de wrijving?",
        opties=[
            "−100 J",
            "100 J",
            "−6,25 J",
            "−29 J",
        ],
        antwoord=0,
        uitleg="De wrijving wijst tegen de beweging in, dus is haar arbeid negatief: 25 maal "
        "4 is 100 joule die als warmte verdwijnt.",
    ),
    dict(
        type="waarofniet",
        vraag="Arbeid kan negatief zijn.",
        antwoord=True,
        uitleg="Dat gebeurt als de kracht tegen de verplaatsing in wijst, zoals bij "
        "wrijving of bij remmen. De energie van het lichaam neemt dan af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel arbeid verricht de middelpuntzoekende kracht op een satelliet in een cirkelbaan?",
        opties=[
            "nul, want ze staat loodrecht op de beweging",
            "evenveel als de kinetische energie van de satelliet",
            "een negatieve arbeid, want ze trekt naar binnen",
            "dat hangt af van de massa van de satelliet",
        ],
        antwoord=0,
        uitleg="Daarom blijft de snelheid van zo'n satelliet constant. Een kracht loodrecht "
        "op de beweging verandert enkel de richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kracht van 20 N duwt onder een hoek van 60 graden met de verplaatsing. Hoeveel arbeid levert ze over 5 m?",
        opties=[
            "50 J",
            "100 J",
            "87 J",
            "25 J",
        ],
        antwoord=0,
        uitleg="Alleen de component langs de verplaatsing telt: de cosinus van 60 graden is "
        "een half, dus 20 maal 0,5 maal 5 is 50 joule.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over arbeid zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "arbeid wordt uitgedrukt in joule",
            "arbeid is negatief als de kracht tegen de verplaatsing in werkt",
            "bij een niet-constante kracht reken je met een integraal",
            "arbeid is een vector en heeft dus een richting",
        ],
        antwoord=[0, 1, 2],
        uitleg="Arbeid is een getal met een teken en geen vector. Dat teken zegt of de "
        "kracht energie toevoegt of wegneemt.",
    ),
    dict(
        type="waarofniet",
        vraag="De normaalkracht op een lichaam dat over een vlakke vloer schuift, verricht arbeid.",
        antwoord=False,
        uitleg="Ze staat loodrecht op de verplaatsing, dus is haar arbeid nul. Toch is ze "
        "een niet-conservatieve kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke arbeid verricht je als je met een boodschappentas een trap van 3 m oploopt, met een tas van 5 kg? Neem g gelijk aan 10 N/kg.",
        opties=[
            "150 J",
            "15 J",
            "50 J",
            "1,5 J",
        ],
        antwoord=0,
        uitleg="Enkel het hoogteverschil telt: 5 maal 10 maal 3 is 150 joule. Hoe lang de "
        "trap of hoe traag je gaat, verandert daar niets aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de oppervlakte onder een F(x)-grafiek?",
        antwoord=["arbeid", "de arbeid", "verrichte arbeid"],
        uitleg="Kracht maal afstand is arbeid, en dat is wat die oppervlakte voorstelt. Zo "
        "reken je ook met een kracht die onderweg verandert.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de kinetische energie van een lichaam?",
        opties=[
            "een half maal de massa maal het kwadraat van de snelheid",
            "de massa maal de snelheid",
            "de massa maal het kwadraat van de snelheid",
            "een half maal de massa maal de snelheid",
        ],
        antwoord=0,
        uitleg="Door dat kwadraat heeft twee keer zo snel rijden vier keer zo veel energie. "
        "Dat is waarom een botsing bij hoge snelheid zo veel zwaarder is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel kinetische energie heeft een auto van 1000 kg die 20 m/s rijdt?",
        opties=[
            "200 000 J",
            "20 000 J",
            "400 000 J",
            "10 000 J",
        ],
        antwoord=0,
        uitleg="Een half maal 1000 maal 400 is 200 000 joule, dus 200 kilojoule.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over kinetische en potentiële energie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "kinetische energie is de helft van de massa maal het kwadraat van de snelheid",
            "potentiële energie is de massa maal g maal de hoogte",
            "twee keer zo snel betekent vier keer zoveel kinetische energie",
            "potentiële energie hangt ook van de snelheid af",
        ],
        antwoord=[0, 1, 2],
        uitleg="Potentiële energie hangt alleen van de hoogte en de massa af. De snelheid "
        "zit volledig in de kinetische energie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe bereken je de gravitationele potentiële energie vlak bij het aardoppervlak?",
        antwoord=["m·g·h", "mgh", "m g h"],
        uitleg="Ze is massa maal g maal hoogte. Welke hoogte je als nulpunt kiest, mag je "
        "zelf bepalen, want alleen het verschil telt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel potentiële energie heeft een steen van 2 kg op 15 m hoogte? Neem g gelijk aan 10 N/kg.",
        opties=[
            "300 J",
            "30 J",
            "150 J",
            "3000 J",
        ],
        antwoord=0,
        uitleg="Massa maal g maal hoogte: 2 maal 10 maal 15 is 300 joule.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe snel raakt die steen de grond, als je de luchtweerstand verwaarloost?",
        opties=[
            "ongeveer 17 m/s",
            "ongeveer 30 m/s",
            "ongeveer 15 m/s",
            "ongeveer 300 m/s",
        ],
        antwoord=0,
        uitleg="Alle 300 joule wordt kinetische energie: 300 is een half maal 2 maal v "
        "kwadraat, dus v kwadraat is 300 en v is ongeveer 17 meter per seconde.",
    ),
    dict(
        type="waarofniet",
        vraag="De potentiële energie van een veer is recht evenredig met haar uitrekking zelf.",
        antwoord=False,
        uitleg="Ze gaat met het kwádraat van die uitrekking: ze is een half maal k maal de "
        "uitrekking in het kwadraat. Twee keer zo ver uitrekken slaat dus vier keer zo veel "
        "energie op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het arbeid-energietheorema?",
        opties=[
            "de totale arbeid op een lichaam is gelijk aan zijn verandering van kinetische energie",
            "de totale arbeid op een lichaam is gelijk aan zijn potentiële energie",
            "de arbeid van een kracht is altijd gelijk aan nul",
            "de arbeid is de kinetische energie gedeeld door de tijd",
        ],
        antwoord=0,
        uitleg="Remt een lichaam af, dan is de totale arbeid negatief. Daarom kan je er de "
        "eindsnelheid mee berekenen zonder de tijd te kennen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een slee van 20 kg glijdt zonder wrijving van een heuvel van 5 m hoog. Hoe snel is hij beneden? Neem g gelijk aan 10 N/kg.",
        opties=[
            "10 m/s",
            "5 m/s",
            "20 m/s",
            "50 m/s",
        ],
        antwoord=0,
        uitleg="Stel m maal g maal h gelijk aan een half m maal v kwadraat; de massa valt "
        "weg. Dan is v de wortel uit 2 maal 10 maal 5, dus 10 meter per seconde.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij die berekening speelt de massa van de slee geen rol.",
        antwoord=True,
        uitleg="Ze staat links en rechts in de vergelijking en valt dus weg. Een zware en "
        "een lichte slee komen zonder wrijving even snel beneden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over vermogen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het is de arbeid gedeeld door de tijd",
            "het staat in watt",
            "één watt is één joule per seconde",
            "het staat in joule",
        ],
        antwoord=[0, 1, 2],
        uitleg="Joule is de eenheid van arbeid en energie, niet van vermogen. Twee motoren "
        "kunnen dezelfde arbeid leveren en toch een ander vermogen hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energievormen wisselen elkaar af bij een slingerende schommel? Kruis alles aan wat juist is.",
        opties=[
            "kinetische energie",
            "gravitationele potentiële energie",
            "elastische potentiële energie",
            "kernenergie",
        ],
        antwoord=[0, 1],
        uitleg="Op het hoogste punt is alles potentieel, op het laagste punt alles "
        "kinetisch. Door wrijving gaat er elke slinger een beetje als warmte weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is vermogen?",
        opties=[
            "de arbeid die per seconde verricht wordt",
            "de arbeid maal de verlopen tijd",
            "de kracht maal de massa van het lichaam",
            "de energie die een lichaam in totaal bevat",
        ],
        antwoord=0,
        uitleg="De eenheid is de watt, en één watt is één joule per seconde. Twee motoren "
        "kunnen dezelfde arbeid leveren en toch een ander vermogen hebben.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je vermogen uit?",
        antwoord=["watt", "W", "de watt"],
        uitleg="Eén watt is één joule per seconde. Een kilowattuur is dus geen vermogen maar "
        "een hoeveelheid energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lift levert 60 000 J arbeid in 20 s. Hoe groot is zijn vermogen?",
        opties=[
            "3000 W",
            "1 200 000 W",
            "300 W",
            "0,0003 W",
        ],
        antwoord=0,
        uitleg="Deel de arbeid door de tijd: 60 000 gedeeld door 20 is 3000 watt, dus 3 "
        "kilowatt.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een doos sneller even hoog tilt, levert daardoor meer arbeid.",
        antwoord=False,
        uitleg="De arbeid hangt enkel af van de kracht en de hoogte, niet van de tijd. Wie "
        "het sneller doet, heeft wel een groter vermogen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel joule is één kilowattuur?",
        opties=[
            "3 600 000 J",
            "1000 J",
            "3600 J",
            "60 000 J",
        ],
        antwoord=0,
        uitleg="Duizend watt gedurende 3600 seconden: 1000 maal 3600 is 3,6 miljoen joule. "
        "Zo rekent de elektriciteitsmeter thuis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal valt van 2 m hoog en stuitert tot 1,4 m. Wat is er met de rest van de energie gebeurd?",
        opties=[
            "ze is bij de botsing als warmte en geluid vrijgekomen",
            "ze is in de lucht boven de bal blijven hangen",
            "ze is in potentiële energie van de grond omgezet",
            "ze is gewoon verdwenen, want energie gaat verloren",
        ],
        antwoord=0,
        uitleg="De bal en de vloer vervormen even en worden daarbij warm. Energie gaat nooit "
        "verloren, ze verandert van vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="In een gesloten systeem zonder wrijving blijft de som van de kinetische en de potentiële energie gelijk.",
        antwoord=True,
        uitleg="Dat is de wet van behoud van mechanische energie. Met wrijving klopt die som "
        "niet meer, want er verdwijnt energie als warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist glijdt met wrijving een helling af. Hoe pas je het behoud van energie toe?",
        opties=[
            "de potentiële energie wordt kinetische energie plus warmte",
            "de potentiële energie wordt volledig kinetische energie",
            "de kinetische energie wordt potentiële energie plus warmte",
            "de energie blijft gelijk, want wrijving telt niet mee",
        ],
        antwoord=0,
        uitleg="De arbeid van de wrijving is precies de energie die als warmte verdwijnt. "
        "Daarom komt de kist trager beneden dan zonder wrijving.",
    ),
]
