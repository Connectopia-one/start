# -*- coding: utf-8 -*-
"""De vragen voor "Statistiek: voorstellingen, centrum en spreiding".

Uit de bouwsteen Data en onzekerheid: numerieke en categorische gegevens,
geordend en niet-geordend, gegroepeerd en niet-gegroepeerd, de frequentietabel
met absolute en relatieve frequentie, de klasse en het klassenmidden, en de
voorstellingen: staafdiagram, cirkeldiagram, lijndiagram, histogram, boxplot en
dotplot. Daarnaast de vorm van een verdeling (symmetrisch of scheef,
uitschieters, clusters), de centrummaten (rekenkundig gemiddelde, mediaan,
modus) en de spreidingsmaten (variatiebreedte, kwartielen, interkwartielafstand
en standaardafwijking).

Deel 1 is de soorten gegevens en de voorstellingen. Deel 2 is centrum en
spreiding.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke gegevens zijn numeriek?",
        opties=[
            "de lengte van de leerlingen in centimeter",
            "de kleur van de auto's op de parking",
            "het merk van de gsm van elke leerling",
            "de vakken waarin iemand het liefst les krijgt",
        ],
        antwoord=0,
        uitleg="Met numerieke gegevens kan je rekenen; de andere drie zijn categorisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke categorische gegevens zijn geordend?",
        opties=[
            "de rapportscore als zeer goed, goed of zwak",
            "de haarkleur van de leerlingen in de klas",
            "de gemeente waar iemand woont",
            "het merk van de fiets waarmee je komt",
        ],
        antwoord=0,
        uitleg="Daar zit een volgorde in. Bij haarkleur of gemeente is er geen natuurlijke volgorde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de absolute frequentie van een waarde?",
        opties=[
            "hoeveel keer die waarde voorkomt",
            "welk deel van het geheel die waarde uitmaakt",
            "het verschil met de grootste waarde",
            "de plaats van die waarde in de rij",
        ],
        antwoord=0,
        uitleg="De relatieve frequentie is het aandeel, vaak in procent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Van 25 leerlingen komen er 10 met de fiets. Wat is de relatieve frequentie?",
        opties=["40 procent", "10 procent", "25 procent", "15 procent"],
        antwoord=0,
        uitleg="10 gedeeld door 25 is 0,4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het klassenmidden van de klasse van 10 tot 20?",
        opties=["15", "10", "20", "5"],
        antwoord=0,
        uitleg="Het gemiddelde van de twee grenzen. Je gebruikt het om met gegroepeerde gegevens te rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een staafdiagram en een histogram?",
        opties=[
            "een histogram hoort bij klassen, dus de staven raken elkaar",
            "een histogram gebruikt liggende staven in plaats van rechtopstaande",
            "een staafdiagram hoort enkel bij numerieke gegevens",
            "er is geen verschil, het zijn twee woorden voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Bij een staafdiagram staan de categorieën los, dus staan de staven uit elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een lijndiagram?",
        opties=[
            "om een verloop in de tijd te tonen",
            "om het aandeel van elk deel in een geheel te tonen",
            "om twee variabelen tegen elkaar uit te zetten",
            "om te tonen hoe scheef een verdeling is",
        ],
        antwoord=0,
        uitleg="De temperatuur per maand bijvoorbeeld; de lijn maakt de stijging of daling zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een cirkeldiagram?",
        opties=[
            "om het aandeel van elk deel in een geheel te tonen",
            "om een verloop over de tijd heen te volgen",
            "om de spreiding rond het gemiddelde te tonen",
            "om het aantal uitschieters te tellen",
        ],
        antwoord=0,
        uitleg="Alle sectoren samen zijn honderd procent. Bij veel categorieën wordt het onleesbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af op een boxplot?",
        opties=[
            "de kleinste waarde, de drie kwartielen en de grootste waarde",
            "het gemiddelde en de standaardafwijking",
            "de absolute frequentie van elke waarde",
            "het verloop van de gegevens door de tijd",
        ],
        antwoord=0,
        uitleg="De doos loopt van het eerste tot het derde kwartiel, met de mediaan als streep erin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont een dotplot?",
        opties=[
            "elke meting als een punt boven haar waarde",
            "elke meting als een staaf naast de andere",
            "het gemiddelde van elke klasse als een punt",
            "het verband tussen twee verschillende variabelen",
        ],
        antwoord=0,
        uitleg="Zo zie je meteen waar de waarden zich opstapelen en welke ver weg liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ziet een rechtsscheve verdeling eruit?",
        opties=[
            "het grootste deel ligt links, met een lange staart naar rechts",
            "het grootste deel ligt rechts, met een lange staart naar links",
            "links en rechts van het midden ligt evenveel",
            "er liggen twee opstapelingen ver uit elkaar",
        ],
        antwoord=0,
        uitleg="Zo zien lonen eruit: veel mensen rond een gewoon loon, enkelen met heel veel meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een uitschieter?",
        opties=[
            "een waarde die ver van de rest van de gegevens ligt",
            "de waarde die het vaakst in de reeks voorkomt",
            "de waarde die precies in het midden ligt",
            "het verschil tussen de grootste en de kleinste waarde",
        ],
        antwoord=0,
        uitleg="Ga altijd na of het een meetfout is of een echte waarneming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als een dotplot twee clusters toont?",
        opties=[
            "de gegevens vallen uiteen in twee groepen met elk hun eigen niveau",
            "de helft van de gegevens is verkeerd gemeten",
            "de verdeling is perfect symmetrisch",
            "er is precies één uitschieter in de reeks",
        ],
        antwoord=0,
        uitleg="Vaak zit er dan een verborgen verschil achter, bijvoorbeeld twee klassen samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Gegroepeerde gegevens staan in klassen in plaats van per losse waarde.",
        antwoord=True,
        uitleg="Bij veel verschillende waarden is dat overzichtelijker.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cirkeldiagram is geschikt om een verloop in de tijd te tonen.",
        antwoord=False,
        uitleg="Daarvoor neem je een lijndiagram. Een cirkeldiagram toont delen van één geheel.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle relatieve frequenties samen geven honderd procent.",
        antwoord=True,
        uitleg="Ze verdelen het geheel onder elkaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een histogram laat je ruimte tussen de staven.",
        antwoord=False,
        uitleg="De klassen sluiten op elkaar aan, dus de staven raken elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het klassenmidden van de klasse van 20 tot 30?",
        antwoord=["25"],
        uitleg="Het gemiddelde van de grenzen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een waarde die ver van de rest van de gegevens ligt?",
        antwoord=["uitschieter", "een uitschieter"],
        uitleg="Ga na of het geen meetfout is.",
    ),
    dict(
        type="invultekst",
        vraag="Van 50 mensen kiezen er 20 voor soep. Hoeveel procent is dat?",
        antwoord=["40", "40 procent", "40%"],
        uitleg="20 gedeeld door 50.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het rekenkundig gemiddelde?",
        opties=[
            "de som van alle waarden gedeeld door het aantal waarden",
            "de middelste waarde van de gerangschikte reeks",
            "de waarde die het vaakst voorkomt in de reeks",
            "het verschil tussen de grootste en de kleinste waarde",
        ],
        antwoord=0,
        uitleg="De middelste waarde is de mediaan, de vaakst voorkomende is de modus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van 3, 7, 8, 12 en 20?",
        opties=["8", "10", "12", "7"],
        antwoord=0,
        uitleg="De reeks staat al gerangschikt; 8 is de derde van vijf waarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van 4, 6, 9 en 11?",
        opties=["7,5", "6", "9", "7"],
        antwoord=0,
        uitleg="Bij een even aantal neem je het gemiddelde van de twee middelste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de modus van 2, 3, 3, 5 en 9?",
        opties=["3", "5", "4,4", "2"],
        antwoord=0,
        uitleg="De waarde die het vaakst voorkomt. Het gemiddelde is hier 4,4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de mediaan bij lonen vaak eerlijker dan het gemiddelde?",
        opties=[
            "een paar heel hoge lonen trekken het gemiddelde omhoog",
            "de mediaan is altijd groter dan het gemiddelde",
            "het gemiddelde kan je bij lonen niet berekenen",
            "de mediaan houdt rekening met alle uitschieters",
        ],
        antwoord=0,
        uitleg="De mediaan kijkt enkel naar wie in het midden staat en blijft dus rustig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de variatiebreedte van een reeks?",
        opties=[
            "het verschil tussen de grootste en de kleinste waarde",
            "het verschil tussen het derde en het eerste kwartiel",
            "de gemiddelde afstand tot het rekenkundig gemiddelde",
            "de middelste waarde van de gerangschikte reeks",
        ],
        antwoord=0,
        uitleg="Eén uitschieter maakt die breedte meteen heel groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het eerste kwartiel?",
        opties=[
            "de waarde waaronder een kwart van de gegevens ligt",
            "de waarde waaronder de helft van de gegevens ligt",
            "de kleinste waarde uit de hele reeks",
            "het gemiddelde van het eerste kwart van de reeks",
        ],
        antwoord=0,
        uitleg="Het tweede kwartiel is de mediaan, het derde laat driekwart onder zich.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de interkwartielafstand?",
        opties=[
            "het derde kwartiel min het eerste kwartiel",
            "de grootste waarde min de kleinste waarde",
            "de mediaan min het rekenkundig gemiddelde",
            "het gemiddelde van de vier kwartielen samen",
        ],
        antwoord=0,
        uitleg="Dat is de breedte van de doos van de boxplot: de middelste helft van de gegevens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de interkwartielafstand minder gevoelig voor een uitschieter dan de variatiebreedte?",
        opties=[
            "hij kijkt enkel naar de middelste helft van de gegevens",
            "hij deelt de uitschieter over alle waarden uit",
            "hij laat het grootste kwart van de gegevens twee keer meetellen",
            "hij telt enkel de waarden boven het gemiddelde mee",
        ],
        antwoord=0,
        uitleg="De uiterste waarden vallen erbuiten en veranderen er dus niets aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de standaardafwijking?",
        opties=[
            "hoe ver de waarden gemiddeld van het gemiddelde af liggen",
            "hoe ver de grootste en de kleinste waarde uit elkaar liggen",
            "welke waarde precies in het midden van de reeks ligt",
            "hoeveel verschillende waarden er in de reeks zitten",
        ],
        antwoord=0,
        uitleg="Een kleine standaardafwijking betekent dat de waarden dicht bij elkaar liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee klassen hebben hetzelfde gemiddelde, maar klas A heeft een grotere standaardafwijking. Wat betekent dat?",
        opties=[
            "in klas A liggen de punten verder uit elkaar",
            "in klas A zijn de punten gemiddeld hoger",
            "in klas A zitten meer leerlingen dan in de andere klas",
            "in klas A is de mediaan gelijk aan het gemiddelde",
        ],
        antwoord=0,
        uitleg="Het gemiddelde zegt niets over de spreiding; daarvoor heb je een spreidingsmaat nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gemiddelde van 4, 8, 10 en 14?",
        opties=["9", "10", "8", "36"],
        antwoord=0,
        uitleg="De som is 36, gedeeld door 4.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke centrummaat kan je met categorische gegevens werken?",
        opties=[
            "de modus, want die telt enkel welke categorie het vaakst voorkomt",
            "het rekenkundig gemiddelde, want dat werkt met elke soort gegevens",
            "de mediaan, want die vraagt geen enkele volgorde",
            "de standaardafwijking, want die meet enkel spreiding",
        ],
        antwoord=0,
        uitleg="Met haarkleuren kan je niet rekenen, maar je kan wel tellen welke het vaakst voorkomt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het rekenkundig gemiddelde is gevoelig voor uitschieters.",
        antwoord=True,
        uitleg="Eén heel grote waarde trekt het hele gemiddelde omhoog.",
    ),
    dict(
        type="waarofniet",
        vraag="De mediaan is altijd gelijk aan het rekenkundig gemiddelde.",
        antwoord=False,
        uitleg="Enkel bij een symmetrische verdeling vallen ze ongeveer samen.",
    ),
    dict(
        type="waarofniet",
        vraag="De doos van een boxplot bevat de middelste helft van de gegevens.",
        antwoord=True,
        uitleg="Ze loopt van het eerste tot het derde kwartiel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reeks kan geen twee modi hebben.",
        antwoord=False,
        uitleg="Komen twee waarden even vaak en het vaakst voor, dan zijn er twee modi.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de mediaan van 2, 5, 6, 9 en 20?",
        antwoord=["6"],
        uitleg="De middelste van vijf gerangschikte waarden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen het derde en het eerste kwartiel?",
        antwoord=["interkwartielafstand", "de interkwartielafstand"],
        uitleg="Dat is de breedte van de doos van de boxplot.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het gemiddelde van 6, 10 en 14?",
        antwoord=["10"],
        uitleg="De som is 30, gedeeld door 3.",
    ),
]
