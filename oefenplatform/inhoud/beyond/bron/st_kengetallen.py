# -*- coding: utf-8 -*-
"""Centrummaten: het rekenkundig gemiddelde, de mediaan en de modus.

De fiche noemt deze drie bij naam en vraagt ze "met ICT" te berekenen. Het
rekenwerk is dus niet het leerdoel; de keuze is dat wel. Wanneer is het
gemiddelde het eerlijkste getal en wanneer de mediaan? Dat is de vraag waar
dit thema over gaat, want het is ook de vraag die in het nieuws elke week
fout wordt beantwoord.

Twee dingen die hier altijd fout gaan, en daarom staan ze in de vragen:
  1. De mediaan van een even aantal gegevens is het gemiddelde van de twee
     middelste, niet een van de twee.
  2. De gegevens moeten eerst gerangschikt worden vóór je de mediaan zoekt.
     Wie dat vergeet, leest gewoon de middelste van de onsorteerde lijst af.

Wat de twee van elkaar onderscheidt: het gemiddelde voelt elke uitschieter,
de mediaan niet. Bij scheve data, zoals lonen en huurprijzen, liggen de twee
daarom ver uit elkaar, en dan is de mediaan het eerlijkere getal.

Deel 1 is de drie maten en hoe je ze berekent.
Deel 2 is de keuze tussen de drie en de uitschieters.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het rekenkundig gemiddelde?",
        opties=[
            "je telt alle waarden op en deelt door het aantal waarden",
            "je neemt de middelste waarde van de gerangschikte lijst",
            "je neemt de waarde die het vaakst voorkomt",
            "je telt de grootste en de kleinste waarde op",
        ],
        antwoord=0,
        uitleg="De som gedeeld door het aantal. Dat is de maat die elke waarde laat meewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van een dataset?",
        opties=[
            "de middelste waarde als je de gegevens rangschikt",
            "het gemiddelde van de grootste en de kleinste waarde",
            "de waarde die het vaakst voorkomt in de dataset",
            "de som van alle waarden gedeeld door het aantal",
        ],
        antwoord=0,
        uitleg="Rangschikken is de eerste stap, en die wordt het vaakst vergeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de modus van een dataset?",
        opties=[
            "de waarde die het vaakst voorkomt",
            "de middelste waarde van de gerangschikte lijst",
            "de som gedeeld door het aantal waarden",
            "het verschil tussen de grootste en de kleinste waarde",
        ],
        antwoord=0,
        uitleg="Als twee waarden even vaak voorkomen, zijn er twee modi. Soms is er geen enkele.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een even aantal gegevens is de mediaan de kleinste van de twee middelste waarden.",
        antwoord=False,
        uitleg="Ze is het gemiddelde van de twee middelste. Bij 10, 12, 14 en 16 is de mediaan dus 13, een getal dat zelf niet in de lijst staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gemiddelde van 3, 5, 5, 8 en 9?",
        opties=["zes", "vijf", "acht", "dertig"],
        antwoord=0,
        uitleg="De som is dertig en er zijn vijf waarden, dus dertig gedeeld door vijf is zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van 3, 5, 5, 8 en 9?",
        opties=["vijf", "zes", "acht", "vier"],
        antwoord=0,
        uitleg="De lijst staat al gerangschikt en de derde van vijf waarden is vijf.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de modus van 3, 5, 5, 8 en 9? Geef het getal in cijfers.",
        antwoord=["5"],
        uitleg="Vijf komt twee keer voor, de andere waarden één keer.",
    ),
    dict(
        type="waarofniet",
        vraag="De modus kan ook bij een niet-numerieke variabele bepaald worden.",
        antwoord=True,
        uitleg="De meest voorkomende studierichting of haarkleur: daar zijn een gemiddelde en een mediaan onmogelijk, de modus niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van 10, 12, 14 en 16?",
        opties=["dertien", "twaalf", "veertien", "dertien komma vijf"],
        antwoord=0,
        uitleg="Het gemiddelde van de twee middelste, twaalf en veertien, is dertien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zoekt de mediaan van 8, 3, 9, 5 en 5 en antwoordt negen. Wat ging er mis?",
        opties=[
            "hij vergat te rangschikken, de mediaan is vijf",
            "hij nam het gemiddelde in plaats van de mediaan",
            "hij nam de modus in plaats van de mediaan",
            "hij vergat te delen door het aantal waarden",
        ],
        antwoord=0,
        uitleg="Gerangschikt staat er 3, 5, 5, 8, 9 en de derde waarde is vijf. Negen is gewoon de middelste van de onsorteerde lijst.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gemiddelde moet altijd een van de waarden uit de dataset zijn.",
        antwoord=False,
        uitleg="Zelden zelfs. Het gemiddelde aantal kinderen per gezin is 1,7 en zo'n gezin bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het gemiddelde uit een frequentietabel?",
        opties=[
            "je vermenigvuldigt elke waarde met haar frequentie en deelt door het totaal",
            "je telt alle verschillende waarden op en deelt door hun aantal",
            "je neemt de waarde met de grootste frequentie uit de tabel",
            "je telt alle frequenties op en deelt door het aantal rijen",
        ],
        antwoord=0,
        uitleg="Een waarde die tien keer voorkomt, moet ook tien keer meewegen. Dat is een gewogen gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="De waarden 1, 2 en 3 komen respectievelijk 2, 3 en 5 keer voor. Wat is het gemiddelde?",
        opties=["2,3", "twee", "drie", "1,8"],
        antwoord=0,
        uitleg="Twee plus zes plus vijftien is drieëntwintig, gedeeld door tien waarden is 2,3.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de mediaan van 4, 6, 8, 10, 12, 14 en 16? Geef het getal in cijfers.",
        antwoord=["10"],
        uitleg="Zeven waarden, dus de vierde. Dat is tien.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dataset kan twee modi hebben.",
        antwoord=True,
        uitleg="Als twee waarden even vaak en het vaakst voorkomen. Men spreekt dan van een bimodale verdeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke centrummaat kan je berekenen voor de variabele woonplaats?",
        opties=[
            "enkel de modus",
            "enkel de mediaan",
            "enkel het gemiddelde",
            "alle drie de centrummaten",
        ],
        antwoord=0,
        uitleg="Woonplaatsen zijn geen getallen, dus optellen en rangschikken gaan niet. Tellen welke het vaakst voorkomt, wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dataset van zes getallen heeft een gemiddelde van tien. Wat is de som?",
        opties=["zestig", "zestien", "tien", "zes"],
        antwoord=0,
        uitleg="Zes maal tien is zestig. Uit het gemiddelde en het aantal volgt altijd de som.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een symmetrische verdeling liggen het gemiddelde en de mediaan dicht bij elkaar.",
        antwoord=True,
        uitleg="Bij een perfect symmetrische verdeling vallen ze samen. Dat is een van de kenmerken van de normale verdeling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe bereken je volgens de fiche de centrummaten bij een grote dataset? Eén woord.",
        antwoord=["ICT", "rekenapps", "rekenapp"],
        uitleg="Met ICT, dus met de rekenapps. Bij duizenden waarden is dat de enige werkbare manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dataset bestaat uit 7, 7, 7 en 7. Wat zijn het gemiddelde, de mediaan en de modus?",
        opties=[
            "alle drie gelijk aan zeven",
            "het gemiddelde is zeven, de andere twee bestaan niet",
            "alle drie gelijk aan achtentwintig",
            "het gemiddelde is achtentwintig en de rest is zeven",
        ],
        antwoord=0,
        uitleg="Zonder spreiding vallen de drie maten samen. Dat gebeurt enkel als alle waarden gelijk zijn.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het gemiddelde als er één enorme uitschieter bijkomt?",
        opties=[
            "het schuift mee in de richting van de uitschieter",
            "het blijft precies waar het was",
            "het schuift in de tegengestelde richting",
            "het wordt gelijk aan de uitschieter",
        ],
        antwoord=0,
        uitleg="Elke waarde weegt mee in de som, dus één groot getal trekt het gemiddelde omhoog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de mediaan als er één enorme uitschieter bijkomt?",
        opties=[
            "ze verandert nauwelijks",
            "ze verdubbelt ongeveer in waarde",
            "ze wordt gelijk aan de uitschieter",
            "ze verdwijnt uit de dataset",
        ],
        antwoord=0,
        uitleg="De mediaan kijkt enkel naar de plaats in de rij. Hoe groot de grootste waarde is, doet haar niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gemiddelde van 2, 3, 3, 4 en 50?",
        opties=["12,4", "drie", "vier", "62"],
        antwoord=0,
        uitleg="De som is tweeënzestig, gedeeld door vijf is 12,4. En toch ligt vier van de vijf waarden onder vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="De mediaan van 2, 3, 3, 4 en 50 is vier.",
        antwoord=False,
        uitleg="De derde van vijf gerangschikte waarden is drie. Hier beschrijft de mediaan de dataset veel eerlijker dan het gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men voor lonen liever de mediaan dan het gemiddelde?",
        opties=[
            "omdat een paar heel hoge lonen het gemiddelde optrekken",
            "omdat de mediaan altijd hoger uitkomt dan het gemiddelde",
            "omdat lonen geen gemiddelde kunnen hebben",
            "omdat de mediaan makkelijker te berekenen is dan het gemiddelde",
        ],
        antwoord=0,
        uitleg="Het mediane loon is het loon van de middelste werknemer. Dat is wat de meeste mensen willen weten.",
    ),
    dict(
        type="invultekst",
        vraag="Welke centrummaat is het minst gevoelig voor uitschieters? Eén woord.",
        antwoord=["mediaan", "de mediaan"],
        uitleg="De mediaan. Men noemt haar daarom robuust.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een verdeling die scheef naar rechts hangt, ligt het gemiddelde boven de mediaan.",
        antwoord=True,
        uitleg="De lange staart rechts trekt het gemiddelde mee. Bij huurprijzen en inkomens is dat altijd zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente meldt een gemiddeld inkomen van 45.000 euro en een mediaan van 32.000 euro. Wat besluit je?",
        opties=[
            "de verdeling hangt scheef naar rechts door enkele hoge inkomens",
            "de verdeling hangt scheef naar links door enkele lage inkomens",
            "de verdeling is symmetrisch rond 38.500 euro",
            "een van de twee getallen is fout berekend",
        ],
        antwoord=0,
        uitleg="Gemiddelde ver boven de mediaan is het klassieke teken van een staart naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer is het gemiddelde een goede keuze?",
        opties=[
            "bij een redelijk symmetrische verdeling zonder grote uitschieters",
            "bij een verdeling met een lange staart naar rechts",
            "bij een niet-numerieke variabele zoals studierichting",
            "altijd, want het gemiddelde gebruikt alle gegevens",
        ],
        antwoord=0,
        uitleg="Dan gebruikt het alle informatie zonder vertekend te worden. Dat is zijn sterkte én zijn zwakte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gemiddelde zonder de spreiding erbij zegt eigenlijk weinig.",
        antwoord=True,
        uitleg="Twee klassen met hetzelfde gemiddelde kunnen er heel verschillend uitzien. Geef altijd ook een spreidingsmaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling heeft een gemiddelde van 12 op vier toetsen. Hij haalt een vijfde toets met 2. Wat is zijn nieuwe gemiddelde?",
        opties=["tien", "elf", "zeven", "twaalf"],
        antwoord=0,
        uitleg="Vier maal twaalf is achtenveertig, plus twee is vijftig, gedeeld door vijf is tien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee klassen hebben allebei een gemiddelde van 14. In klas A ligt alles tussen 13 en 15, in klas B tussen 4 en 20. Wat betekent dat?",
        opties=[
            "klas B is veel breder gespreid, al is het centrum hetzelfde",
            "klas B heeft een hoger gemiddelde dan klas A",
            "klas A heeft een hogere mediaan dan klas B",
            "de twee klassen zijn statistisch niet te vergelijken",
        ],
        antwoord=0,
        uitleg="Hetzelfde centrum, een heel andere spreiding. Daarom hoort er altijd een spreidingsmaat bij een gemiddelde.",
    ),
    dict(
        type="invultekst",
        vraag="Een dataset van tien getallen heeft een gemiddelde van acht. Wat is de som? Geef het getal in cijfers.",
        antwoord=["80"],
        uitleg="Tien maal acht is tachtig.",
    ),
    dict(
        type="waarofniet",
        vraag="De modus ligt altijd tussen het gemiddelde en de mediaan.",
        antwoord=False,
        uitleg="Niet noodzakelijk. Bij een scheve verdeling liggen de drie vaak in een vaste orde, maar een uitzondering is zo gemaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft: het gemiddelde huis kost 350.000 euro, dus de helft van de huizen kost minder. Wat is de fout?",
        opties=[
            "dat zou gelden voor de mediaan, niet voor het gemiddelde",
            "dat geldt enkel als de prijzen in euro uitgedrukt zijn",
            "er is geen fout, een gemiddelde splitst de data altijd in twee",
            "men moet eerst de modus van de prijzen berekenen",
        ],
        antwoord=0,
        uitleg="De mediaan splitst de data in twee gelijke helften. Bij huizenprijzen ligt het gemiddelde hoger, dus meer dan de helft kost minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dataset heeft geen enkele waarde die vaker voorkomt dan de andere. Wat zeg je over de modus?",
        opties=[
            "er is geen modus voor deze dataset",
            "de modus is dan het gemiddelde van alle waarden",
            "de modus is dan de grootste waarde van de dataset",
            "elke waarde is dan de modus van de dataset",
        ],
        antwoord=0,
        uitleg="Bij continue metingen komt bijna geen waarde twee keer voor. Groepeer dan eerst en zoek de modale klasse.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gemiddelde van twee gemiddelden is in het algemeen niet het gemiddelde van de hele groep.",
        antwoord=True,
        uitleg="Enkel als de twee groepen even groot zijn. Anders moet je wegen met het aantal in elke groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Klas A heeft tien leerlingen met gemiddelde 12, klas B heeft dertig met gemiddelde 16. Wat is het gemiddelde van de veertig samen?",
        opties=["vijftien", "veertien", "dertien", "zestien"],
        antwoord=0,
        uitleg="Honderdtwintig plus vierhonderdtachtig is zeshonderd, gedeeld door veertig is vijftien. Niet veertien, want klas B is groter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke centrummaat gebruik je om te zeggen wat de meest gekozen optie is?",
        opties=[
            "de modus",
            "de mediaan",
            "het rekenkundig gemiddelde",
            "de variatiebreedte",
        ],
        antwoord=0,
        uitleg="De modus is de meest voorkomende waarde, dus de populairste keuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker verwijdert alle uitschieters om een mooier gemiddelde te krijgen. Wat zeg je?",
        opties=[
            "uitschieters verwijder je enkel met een reden, en je meldt het altijd",
            "dat is de normale werkwijze bij elke statistische analyse",
            "dat mag nooit, uitschieters blijven altijd in de dataset",
            "dan moet hij ook de kleinste waarden verwijderen voor het evenwicht",
        ],
        antwoord=0,
        uitleg="Een tikfout mag eruit. Een echt bijzonder geval weglaten omdat het niet past, is de data vervalsen.",
    ),
]
