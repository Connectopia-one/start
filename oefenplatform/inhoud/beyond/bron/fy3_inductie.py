# -*- coding: utf-8 -*-
"""Elektromagnetische inductie — 🌍 Beyond, fysica.

Deel 1 gaat over het verschijnsel zelf: de magnetische flux en waarvan ze
afhangt, de inductiewet van Faraday, de wet van Lenz en hoe je daarmee de zin
van de inductiestroom vindt, en wat een grafiek van de flux over de inductie-
spanning zegt. Deel 2 gaat over de toepassingen: de dynamo en de
wisselspanningsgenerator, de transformator met zijn windingsverhouding, de
wervelstromen en wat daarop berust, van inductiekookplaat tot
elektromagnetische rem.

Eén zin draagt het hele thema: niet het veld wekt een spanning op, maar de
vérandering van de flux. Staat er niets te veranderen, dan is de
inductiespanning nul, hoe sterk de magneet ook is.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de magnetische flux door een winding?",
        opties=[
            "het veld maal de doorsneden oppervlakte, met de hoek erbij",
            "het veld gedeeld door de oppervlakte van de winding",
            "de stroom maal het aantal windingen van de spoel",
            "de spanning die de winding aan de kring levert",
        ],
        antwoord=0,
        uitleg="Je kan ze zien als het aantal veldlijnen dat door de winding gaat. In de "
        "formule staat de cosinus van de hoek met de normaal op het vlak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvan hangt de magnetische flux door een winding af? Kruis alles aan wat juist is.",
        opties=[
            "de sterkte van het magnetisch veld",
            "de oppervlakte van de winding",
            "de hoek tussen de winding en het veld",
            "het aantal vrije elektronen in de draad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ze is het grootst als de winding loodrecht in het veld staat. Het materiaal "
        "van de draad verandert aan de flux zelf niets.",
    ),
    dict(
        type="invultekst",
        vraag="In welke eenheid druk je de magnetische flux uit?",
        antwoord=["weber", "Wb", "de weber"],
        uitleg="Eén weber is één tesla maal één vierkante meter. Het symbool van de "
        "grootheid is de Griekse letter phi.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winding van 0,02 m² staat loodrecht in een veld van 0,5 T. Hoe groot is de flux?",
        opties=[
            "0,01 Wb",
            "25 Wb",
            "0,04 Wb",
            "10 Wb",
        ],
        antwoord=0,
        uitleg="De flux is B maal A: 0,5 maal 0,02 is 0,01 weber. De cosinus is hier één, "
        "want de winding staat loodrecht op het veld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de inductiewet van Faraday?",
        opties=[
            "de inductiespanning hangt af van hoe snel de flux verandert",
            "de inductiespanning hangt af van hoe groot de flux zelf is",
            "de inductiespanning hangt af van de weerstand van de spoel",
            "de inductiespanning hangt af van de stof rond de spoel heen",
        ],
        antwoord=0,
        uitleg="Ze is het aantal windingen maal de fluxverandering per seconde. Een grote "
        "maar onveranderlijke flux levert dus niets op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een magneet die stil in een spoel ligt, wekt een inductiespanning op.",
        antwoord=False,
        uitleg="Er verandert dan niets aan de flux, dus is de inductiespanning nul. Pas als "
        "je de magneet beweegt, ontstaat er spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je de flux door een spoel laten veranderen? Kruis alles aan wat juist is.",
        opties=[
            "door een magneet in of uit de spoel te bewegen",
            "door de spoel in het veld te laten draaien",
            "door de spoel op een hogere temperatuur te brengen",
            "door de draad van de spoel langer te maken",
        ],
        antwoord=[0, 1],
        uitleg="Ook het veld zelf sterker of zwakker maken werkt. Wat telt is dat het "
        "aantal veldlijnen door de winding verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de wet van Lenz?",
        opties=[
            "de inductiestroom werkt de verandering die hem veroorzaakt tegen",
            "de inductiestroom versterkt de verandering die hem veroorzaakt",
            "de inductiestroom loopt altijd in de zin van het veld",
            "de inductiestroom loopt altijd in dezelfde zin als de bron",
        ],
        antwoord=0,
        uitleg="Zou hij de verandering versterken, dan maakte je energie uit het niets. Het "
        "minteken in de wet van Faraday zegt precies dat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je duwt de noordpool van een magneet in een spoel. Wat doet de spoel?",
        opties=[
            "ze maakt aan die kant zelf een noordpool en duwt terug",
            "ze maakt aan die kant zelf een zuidpool en trekt aan",
            "ze maakt helemaal geen eigen magnetisch veld aan",
            "ze maakt een veld dwars op de as van de magneet",
        ],
        antwoord=0,
        uitleg="Volgens de wet van Lenz werkt ze het naderen tegen. Trek je de magneet er "
        "weer uit, dan maakt ze juist een zuidpool en houdt ze hem tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je moet arbeid leveren om een magneet in een gesloten spoel te duwen.",
        antwoord=True,
        uitleg="De inductiestroom duwt terug, dus moet je die tegenkracht overwinnen. Die "
        "arbeid komt er als elektrische energie weer uit; zo werkt een dynamo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een spoel met 200 windingen ziet de flux in 0,1 s met 0,004 Wb veranderen. Hoe groot is de inductiespanning?",
        opties=[
            "8 V",
            "0,8 V",
            "80 V",
            "0,08 V",
        ],
        antwoord=0,
        uitleg="N maal de fluxverandering gedeeld door de tijd: 200 maal 0,004 gedeeld door "
        "0,1 is 8 volt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de inductiespanning als je het aantal windingen verdubbelt?",
        opties=[
            "ze wordt twee keer zo groot",
            "ze wordt half zo groot",
            "ze blijft precies even groot",
            "ze wordt vier keer zo groot",
        ],
        antwoord=0,
        uitleg="Het aantal windingen staat als factor in de wet van Faraday. Elke winding "
        "levert immers haar eigen bijdrage.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de wet die zegt dat een inductiestroom zijn eigen oorzaak tegenwerkt?",
        antwoord=["wet van Lenz", "Lenz", "lenz"],
        uitleg="Ze volgt uit het behoud van energie. In de wet van Faraday staat ze als het "
        "minteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="De flux door een spoel blijft een tijdlang constant op een grafiek. Wat doet de inductiespanning in dat stuk?",
        opties=[
            "ze is nul",
            "ze is daar juist het grootst",
            "ze stijgt gelijkmatig door",
            "ze wisselt daar van teken",
        ],
        antwoord=0,
        uitleg="De inductiespanning volgt de steilheid van de fluxgrafiek. Een vlak stuk "
        "betekent geen verandering, dus geen spanning.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe steiler de fluxgrafiek loopt, hoe kleiner de inductiespanning op dat ogenblik is.",
        antwoord=False,
        uitleg="Juist omgekeerd: de spanning is de fluxverandering per seconde, dus een "
        "steile helling betekent een snelle verandering en dus een grote spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden bepalen de inductiespanning van een spoel? Kruis alles aan wat juist is.",
        opties=[
            "het aantal windingen",
            "de snelheid waarmee de flux verandert",
            "de weerstand van de draad",
            "de massa van de magneet",
        ],
        antwoord=[0, 1],
        uitleg="De weerstand bepaalt wel hoeveel stroom er bij die spanning loopt, maar niet "
        "de spanning zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom levert een magneet die je sneller in een spoel duwt, meer spanning op?",
        opties=[
            "de flux verandert dan in minder tijd evenveel",
            "het veld van de magneet wordt dan zelf sterker",
            "de spoel krijgt dan meer windingen te verwerken",
            "de weerstand van de draad daalt bij snelheid",
        ],
        antwoord=0,
        uitleg="In de wet van Faraday staat de verandering per seconde. Dezelfde verandering "
        "in de helft van de tijd geeft dus het dubbele.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rechthoekige winding draait rond in een homogeen veld. Hoe verloopt de inductiespanning?",
        opties=[
            "ze wisselt regelmatig van teken, als een sinus",
            "ze blijft constant zolang de winding draait",
            "ze stijgt onophoudelijk zolang je blijft draaien",
            "ze is nul, want het veld verandert zelf niet",
        ],
        antwoord=0,
        uitleg="De flux gaat van maximaal naar nul naar maximaal in de andere zin. Zo wekt "
        "een generator wisselspanning op.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder een gesloten kring is er wel een inductiespanning, maar geen inductiestroom.",
        antwoord=True,
        uitleg="De spanning ontstaat door de fluxverandering, maar stroom heeft een gesloten "
        "weg nodig. Daarom meet je bij een open spoel wel spanning en geen stroom.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de wet die de inductiespanning met de fluxverandering verbindt?",
        antwoord=["wet van Faraday", "Faraday", "inductiewet"],
        uitleg="Ze luidt dat de inductiespanning min N maal de fluxverandering per seconde "
        "is. Het minteken komt van de wet van Lenz.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe wekt een dynamo op een fiets spanning op?",
        opties=[
            "een magneet draait langs een spoel en laat de flux wisselen",
            "de wrijving van het wiel maakt de spoel warm genoeg",
            "de band perst lucht door een kleine turbine heen",
            "de spoel laadt zich op zoals een batterij dat doet",
        ],
        antwoord=0,
        uitleg="Hoe sneller je fietst, hoe sneller de flux verandert en hoe feller de lamp "
        "brandt. De spiertrekkracht die je daarvoor levert, is precies de wet van Lenz "
        "aan het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toestellen werken met elektromagnetische inductie? Kruis alles aan wat juist is.",
        opties=[
            "een dynamo op een fiets",
            "een transformator in een laadblokje",
            "een inductiekookplaat",
            "een gewone gloeilamp",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een gloeilamp werkt gewoon doordat een draad warm wordt. De eerste drie "
        "hebben allemaal een veranderend magnetisch veld nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Welke soort spanning levert een generator met een draaiende winding?",
        antwoord=["wisselspanning", "wisselspanning", "wissel"],
        uitleg="De flux gaat heen en weer, dus keert ook de spanning telkens om. Een "
        "batterij levert wel gelijkspanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een transformator?",
        opties=[
            "om een wisselspanning hoger of lager te maken",
            "om wisselspanning in gelijkspanning om te zetten",
            "om de stroom in een kring te onderbreken",
            "om energie op te slaan voor later gebruik",
        ],
        antwoord=0,
        uitleg="Hij bestaat uit twee spoelen op dezelfde ijzeren kern. De verhouding van de "
        "windingen bepaalt de verhouding van de spanningen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een transformator heeft 500 windingen primair en 50 secundair. Wat doet hij met een spanning van 230 V?",
        opties=[
            "hij verlaagt ze tot 23 V",
            "hij verhoogt ze tot 2300 V",
            "hij laat ze op 230 V staan",
            "hij verlaagt ze tot 115 V",
        ],
        antwoord=0,
        uitleg="De spanningen verhouden zich als de windingen: tien keer minder windingen "
        "geeft tien keer minder spanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een transformator heeft 100 windingen primair en 400 secundair. Hoe heet zo'n transformator?",
        opties=[
            "een optransformator, want hij verhoogt de spanning",
            "een neertransformator, want hij verlaagt de spanning",
            "een gelijkrichter, want hij maakt er gelijkstroom van",
            "een scheidingstransformator, want hij verandert niets",
        ],
        antwoord=0,
        uitleg="Meer windingen secundair betekent een hogere spanning. De stroom wordt dan "
        "wel evenredig kleiner, want de energie kan niet uit het niets komen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een transformator werkt ook op gelijkspanning.",
        antwoord=False,
        uitleg="Bij gelijkspanning verandert de flux niet meer zodra de stroom constant is, "
        "en dan is er geen inductie. Daarom werkt hij enkel op wisselspanning.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt stroom over grote afstanden op hoogspanning vervoerd?",
        opties=[
            "bij een kleinere stroom gaat er veel minder warmte verloren",
            "bij een hogere spanning gaan de elektronen veel sneller",
            "bij een hogere spanning is er minder koperdraad nodig",
            "bij een hogere spanning is de kans op blikseminslag kleiner",
        ],
        antwoord=0,
        uitleg="Hetzelfde vermogen bij een hogere spanning betekent een kleinere stroom. Het "
        "verlies in de kabels gaat met het kwadraat van de stroom, dus daalt het sterk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kringstromen die in een massief stuk metaal ontstaan bij een veranderende flux?",
        antwoord=["wervelstromen", "foucaultstromen", "wervelstroom"],
        uitleg="Ze werken de beweging tegen en maken het metaal warm. Een inductiekookplaat "
        "en een elektromagnetische rem gebruiken dat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt een inductiekookplaat?",
        opties=[
            "een wisselend veld wekt wervelstromen op in de bodem van de pan",
            "een spoel onder de plaat wordt heet en geeft die warmte door",
            "de plaat zendt infraroodstraling naar de bodem van de pan",
            "de plaat wrijft met trillingen langs de bodem van de pan",
        ],
        antwoord=0,
        uitleg="De warmte ontstaat in de pan zelf, niet in de plaat. Daarom werkt zo'n plaat "
        "enkel met een pan van ferromagnetisch materiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt een inductiekookplaat niet met een pan van aluminium?",
        opties=[
            "aluminium is niet ferromagnetisch genoeg voor de koppeling",
            "aluminium geleidt de warmte veel te snel naar boven weg",
            "aluminium smelt bij de temperatuur van zo'n kookplaat",
            "aluminium is te licht om op de plaat te blijven staan",
        ],
        antwoord=0,
        uitleg="Het veld koppelt veel te zwak met een niet-ferromagnetische bodem. Daarom "
        "hebben zulke pannen vaak een laagje staal in de bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toestellen berusten op elektromagnetische inductie? Kruis alles aan wat juist is.",
        opties=[
            "de dynamo op een fiets",
            "een draadloze oplader",
            "een gewone gloeilamp",
            "een mechanische veer in een klok",
        ],
        antwoord=[0, 1],
        uitleg="Ook de elektrische gitaar, de detectielus in het wegdek, de microfoon en de "
        "fietscomputer horen erbij. Overal verandert er een flux.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de pick-up van een elektrische gitaar?",
        opties=[
            "de trillende stalen snaar verandert de flux door een spoeltje",
            "de snaar raakt het spoeltje aan en sluit zo de kring",
            "de luidspreker neemt het geluid van de snaar rechtstreeks op",
            "de spoel stuurt een stroompje door de snaar heen",
        ],
        antwoord=0,
        uitleg="Onder elke snaar zit een magneetje met een spoel eromheen. Een nylon snaar "
        "zou niets opwekken, want die is niet ferromagnetisch.",
    ),
    dict(
        type="waarofniet",
        vraag="Een elektromagnetische rem raakt het wiel niet aan.",
        antwoord=True,
        uitleg="De wervelstromen in de draaiende schijf werken de beweging tegen, zonder "
        "contact. Daardoor slijt er niets, maar remmen tot stilstand lukt er niet mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over wervelstromen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze ontstaan in een massief stuk metaal in een veranderend veld",
            "ze werken de beweging die ze veroorzaakt tegen",
            "gleuven of dunne plaatjes maken ze veel kleiner",
            "ze ontstaan even goed in een stuk hout of plastic",
        ],
        antwoord=[0, 1, 2],
        uitleg="Er zijn vrije elektronen voor nodig, dus in een isolator ontstaan ze niet. "
        "Daarom valt de slinger van von Waltenhofen met gleuven veel vlotter.",
    ),
    dict(
        type="waarofniet",
        vraag="Een detectielus in het wegdek merkt een wagen op doordat de wagen de flux door de lus verandert.",
        antwoord=True,
        uitleg="Het metaal van de wagen verandert de zelfinductie van de lus. Een fiets met "
        "een kunststof frame wordt daardoor vaak niet opgemerkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de kern van een transformator uit dunne, van elkaar geïsoleerde plaatjes opgebouwd?",
        opties=[
            "om de wervelstromen in de kern klein te houden",
            "om de kern beter tegen roest te beschermen",
            "om de kern lichter en goedkoper te maken",
            "om het veld van de twee spoelen te scheiden",
        ],
        antwoord=0,
        uitleg="In een massieve kern zouden grote wervelstromen lopen en warmte maken. Dat "
        "is verloren energie, dus hakt men de weg voor die stromen in stukjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe laadt een draadloze oplader een telefoon op?",
        opties=[
            "een spoel in de lader wekt een stroom op in een spoel in de telefoon",
            "de lader stuurt de lading rechtstreeks door de lucht heen",
            "de lader warmt de batterij op zodat ze lading vasthoudt",
            "de lader maakt licht dat de batterij met een cel opvangt",
        ],
        antwoord=0,
        uitleg="Er loopt wisselstroom door de spoel van de lader, en de wisselende flux wekt "
        "spanning op in de telefoon. Daarom moeten de twee vlak tegen elkaar liggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een transformator kan het vermogen groter maken dan het vermogen dat erin gaat.",
        antwoord=False,
        uitleg="Energie komt niet uit het niets. Gaat de spanning omhoog, dan gaat de stroom "
        "evenredig omlaag, en in het beste geval blijft het vermogen gelijk.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee spoelen heeft een transformator?",
        antwoord=["primaire en secundaire", "primair en secundair", "primaire, secundaire"],
        uitleg="De primaire krijgt de spanning binnen, de secundaire geeft ze weer af. Hun "
        "aantal windingen bepaalt de verhouding.",
    ),
]
