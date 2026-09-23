# -*- coding: utf-8 -*-
"""De vragen voor "Energie, kracht en snelheid" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel chemie en fysica, "Energie" en "Kracht en snelheid":
energievormen en energieomzettingen herkennen en weten dat er telkens een deel
verloren gaat als warmte; krachten en hun vectoriële kenmerken
(aangrijpingspunt, grootte, richting en zin), de resulterende kracht, de
statische en de dynamische uitwerking, de dynamometer en de newton; en de
formule van de constante snelheid v = Δx/Δt met de omzettingen tussen m/s en
km/h en het lezen van grafieken.

Deel 1 gaat over de namen, de eenheden en de eenvoudige berekeningen. Deel 2
gaat over omgekeerd rekenen, over grafieken en over het soort verband tussen
snelheid, verplaatsing en tijdsduur.

De getallen zijn rond gekozen. `controleer_natuurwetenschappen.py` rekent ze na.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke energievorm heeft een fietser die snel rijdt?",
        opties=["Kinetische energie", "Chemische energie", "Kernenergie"],
        antwoord=0,
        uitleg="Kinetische energie of bewegingsenergie heeft alles wat beweegt. Hoe sneller en hoe zwaarder, hoe meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energievorm zit er in voedsel en in brandstof?",
        opties=["Chemische energie", "Elektrische energie", "Stralingsenergie"],
        antwoord=0,
        uitleg="Chemische energie zit opgeslagen in de bindingen tussen de atomen. Bij verbranding of celademhaling komt ze vrij.",
    ),
    dict(
        type="invultekst",
        vraag="Een steen die hoog op een muur ligt, heeft ___ energie door zijn hoogte.",
        antwoord="potentiële",
        uitleg="Potentiële energie is opgeslagen energie door de plaats of de vorm. Valt de steen, dan wordt ze kinetische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzetting gebeurt er in een lamp?",
        opties=[
            "Elektrische energie wordt lichtenergie en warmte",
            "Lichtenergie wordt elektrische energie",
            "Chemische energie wordt kernenergie",
        ],
        antwoord=0,
        uitleg="Een deel van de elektrische energie wordt licht, de rest warmte. Die warmte is hier de ongewenste vorm: ze gaat verloren.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij elke energieomzetting gaat er een deel verloren als warmte.",
        antwoord=True,
        uitleg="Er verdwijnt geen energie, maar een deel wordt omgezet in een minder bruikbare vorm, meestal warmte. Daarom wordt een gsm warm terwijl je hem gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn energievormen?",
        opties=["Thermische energie", "Kernenergie", "Stralingsenergie", "Massadichtheid"],
        antwoord=[0, 1, 2],
        uitleg="Thermische, elektrische, potentiële, kinetische, chemische, kern- en stralingsenergie zijn energievormen. Massadichtheid is een stofeigenschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van kracht?",
        opties=["De newton (N)", "De kilogram (kg)", "De joule (J)"],
        antwoord=0,
        uitleg="Kracht meet je in newton, met het symbool N. De grootheid zelf krijgt het symbool F.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarmee meet je een kracht?",
        opties=["Met een dynamometer", "Met een weegschaal", "Met een chronometer"],
        antwoord=0,
        uitleg="Een dynamometer is een veer met een schaalverdeling: hoe harder je trekt, hoe verder de veer uitrekt, en dat lees je af in newton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kracht trekt alles naar de aarde toe?",
        opties=["De zwaartekracht", "De wrijvingskracht", "De veerkracht"],
        antwoord=0,
        uitleg="De zwaartekracht werkt altijd naar het middelpunt van de aarde. Haar aangrijpingspunt ligt in het zwaartepunt van het voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn krachten?",
        opties=["Wrijvingskracht", "Spierkracht", "Veerkracht", "Kinetische energie"],
        antwoord=[0, 1, 2],
        uitleg="Zwaartekracht, wrijvingskracht, trekkracht, duwkracht, spierkracht, motorkracht en veerkracht zijn krachten. Energie is iets anders: die heeft geen richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier kenmerken heeft een kracht als vectoriële grootheid?",
        opties=[
            "Aangrijpingspunt, grootte, richting en zin",
            "Massa, volume, kleur en vorm",
            "Begin, einde, snelheid en tijd",
        ],
        antwoord=0,
        uitleg="Je tekent een kracht als een pijl: waar ze aangrijpt, hoe lang de pijl is (de grootte), langs welke lijn ze werkt (de richting) en welke kant ze op wijst (de zin).",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht kan een voorwerp vervormen.",
        antwoord=True,
        uitleg="Dat is de statische uitwerking: een spons die indeukt, een veer die uitrekt. De dynamische uitwerking is een verandering van de bewegingstoestand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitwerkingen van een kracht zijn dynamisch?",
        opties=["Versnellen", "Vertragen", "Van richting veranderen", "Uitrekken van een veer"],
        antwoord=[0, 1, 2],
        uitleg="Een dynamische uitwerking verandert de bewegingstoestand: sneller, trager of een andere kant op. Een veer die uitrekt, is een vervorming, dus statisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de formule voor een constante snelheid?",
        opties=["v = Δx / Δt", "v = Δx × Δt", "v = Δt / Δx"],
        antwoord=0,
        uitleg="Je deelt de verplaatsing door de tijdsduur. Δx is de verplaatsing in meter en Δt de tijdsduur in seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand legt 100 m af in 20 s. Wat is zijn snelheid?",
        opties=["5 m/s", "2 m/s", "20 m/s"],
        antwoord=0,
        uitleg="v = Δx / Δt = 100 m : 20 s = 5 m/s.",
    ),
    dict(
        type="invultekst",
        vraag="Een auto rijdt 90 km in 2 uur. Zijn gemiddelde snelheid is ___ km/h.",
        antwoord="45",
        uitleg="v = 90 km : 2 h = 45 km/h.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel km/h is 5 m/s?",
        opties=["18 km/h", "1,4 km/h", "50 km/h"],
        antwoord=0,
        uitleg="Van m/s naar km/h vermenigvuldig je met 3,6: 5 × 3,6 = 18 km/h.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel m/s is 72 km/h?",
        opties=["20 m/s", "259 m/s", "7,2 m/s"],
        antwoord=0,
        uitleg="Van km/h naar m/s deel je door 3,6: 72 : 3,6 = 20 m/s.",
    ),
    dict(
        type="invultekst",
        vraag="Twee uur is ___ seconden.",
        antwoord="7200",
        uitleg="1 h = 60 min = 3600 s, dus 2 h = 7200 s. Bij een berekening in m/s reken je tijd altijd eerst om naar seconden.",
    ),
    dict(
        type="waarofniet",
        vraag="De SI-eenheid van snelheid is m/s.",
        antwoord=True,
        uitleg="Meter per seconde is de SI-eenheid. Kilometer per uur mag ook, maar dat is een niet-SI-eenheid.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een fietser rijdt 30 s aan 4 m/s. Hoe ver raakt hij?",
        opties=["120 m", "7,5 m", "34 m"],
        antwoord=0,
        uitleg="Uit v = Δx / Δt volgt Δx = v × Δt = 4 × 30 = 120 m.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoelang doet een wandelaar over 300 m aan 5 m/s?",
        opties=["60 s", "1500 s", "6 s"],
        antwoord=0,
        uitleg="Uit v = Δx / Δt volgt Δt = Δx / v = 300 : 5 = 60 s, dus één minuut.",
    ),
    dict(
        type="invultekst",
        vraag="Een trein rijdt aan 36 km/h. In m/s is dat ___.",
        antwoord="10",
        uitleg="36 : 3,6 = 10 m/s. Handig om te onthouden: 36 km/h is precies 10 m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie gaat het snelst: A aan 15 m/s, B aan 50 km/h of C die 1 km in 2 minuten aflegt?",
        opties=["A", "B", "C"],
        antwoord=0,
        uitleg="Reken alles om naar km/h: A is 15 × 3,6 = 54 km/h, B is 50 km/h, en C doet 1 km in 2 min, dus 30 km/h. A is de snelste.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een grafiek staat de afgelegde weg (y) tegenover de tijd (x). Wat betekent een rechte door de oorsprong?",
        opties=[
            "Het voorwerp beweegt met een constante snelheid",
            "Het voorwerp staat stil",
            "Het voorwerp versnelt",
        ],
        antwoord=0,
        uitleg="Bij een constante snelheid komt er in elke seconde evenveel weg bij: recht evenredig, dus een rechte lijn. De steilheid van die rechte is de snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een horizontaal stuk in een grafiek van afstand tegenover tijd?",
        opties=[
            "Het voorwerp staat stil",
            "Het voorwerp rijdt heel snel",
            "Het voorwerp rijdt achteruit",
        ],
        antwoord=0,
        uitleg="De tijd loopt door, maar de afstand verandert niet. De snelheid is dan 0 m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag="In één grafiek lopen twee rechten: die van A is steiler dan die van B. Wat weet je?",
        opties=["A gaat sneller dan B", "B gaat sneller dan A", "Ze gaan even snel"],
        antwoord=0,
        uitleg="Steiler betekent meer afstand in dezelfde tijd, dus een grotere snelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt altijd dezelfde afstand af. Welk verband is er tussen snelheid en tijdsduur?",
        opties=[
            "Omgekeerd evenredig: twee keer zo snel is half zo lang onderweg",
            "Recht evenredig: twee keer zo snel is twee keer zo lang onderweg",
            "Er is geen verband",
        ],
        antwoord=0,
        uitleg="Bij een vaste afstand is hun product constant, dus als de ene verdubbelt, halveert de andere. Tussen verplaatsing en tijdsduur bij vaste snelheid is het verband wél recht evenredig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het verband tussen snelheid, verplaatsing en tijdsduur kloppen?",
        opties=[
            "Bij een vaste snelheid is de verplaatsing recht evenredig met de tijdsduur",
            "Bij een vaste afstand is de snelheid omgekeerd evenredig met de tijdsduur",
            "Bij een vaste tijdsduur is de verplaatsing recht evenredig met de snelheid",
            "Snelheid en tijdsduur zijn altijd recht evenredig",
        ],
        antwoord=[0, 1, 2],
        uitleg="Uit v = Δx / Δt volgen de drie eerste. De laatste klopt niet: langer onderweg zijn maakt je niet sneller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee mensen duwen een kast, allebei 200 N in dezelfde zin. Hoe groot is de resulterende kracht?",
        opties=["400 N in die zin", "0 N", "200 N"],
        antwoord=0,
        uitleg="Krachten in dezelfde richting en zin tel je op: 200 + 200 = 400 N. Duwen ze tegen elkaar in, dan trek je ze af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kinderen trekken aan een touw, allebei 150 N, maar in tegengestelde zin. Wat gebeurt er?",
        opties=[
            "De resultante is 0 N en het touw beweegt niet",
            "De resultante is 300 N",
            "Het touw beweegt naar links",
        ],
        antwoord=0,
        uitleg="Gelijke krachten in tegengestelde zin heffen elkaar op. Het voorwerp blijft in rust of houdt zijn constante snelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Wrijvingskracht werkt altijd tegen de beweging in.",
        antwoord=True,
        uitleg="Daarom vertraagt een bal die over het gras rolt. Zonder wrijving zou hij blijven rollen, maar zonder wrijving zou je ook niet kunnen stappen of remmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bal die je wegtrapt, verandert van richting én gaat sneller. Wat voor uitwerking is dat?",
        opties=[
            "Een dynamische uitwerking",
            "Een statische uitwerking",
            "Geen van beide",
        ],
        antwoord=0,
        uitleg="Alles wat de bewegingstoestand verandert, is dynamisch. Dat de bal tijdens de trap ook even indeukt, is dan weer statisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzettingen gebeuren er als je met een dynamo op je fiets rijdt?",
        opties=[
            "Chemische energie uit je voedsel wordt spierkracht en beweging",
            "Bewegingsenergie wordt elektrische energie in de dynamo",
            "Elektrische energie wordt licht in de lamp",
            "Licht wordt bewegingsenergie",
        ],
        antwoord=[0, 1, 2],
        uitleg="De ketting van omzettingen loopt van je voedsel tot het licht, en bij elke stap gaat er een deel verloren als warmte. De laatste optie loopt de verkeerde kant op.",
    ),
    dict(
        type="invultekst",
        vraag="Een voorwerp waarop de krachten elkaar opheffen en dat niet beweegt, is in ___.",
        antwoord="rust",
        uitleg="Bij een resultante van 0 N blijft een voorwerp in rust, of het blijft met een constante snelheid verder bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto rijdt het eerste uur 60 km en het tweede uur 80 km. Wat is zijn gemiddelde snelheid?",
        opties=["70 km/h", "140 km/h", "20 km/h"],
        antwoord=0,
        uitleg="Samen 140 km in 2 h, dus 140 : 2 = 70 km/h. De snelheid was niet constant, maar gemiddeld is ze 70 km/h.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet je een tijdsduur van 5 minuten eerst om naar seconden voor je in m/s rekent?",
        opties=[
            "Omdat m/s een verplaatsing in meter en een tijd in seconde vraagt",
            "Omdat minuten geen tijdseenheid zijn",
            "Omdat seconden altijd nauwkeuriger zijn",
        ],
        antwoord=0,
        uitleg="De eenheden moeten bij de formule passen: 5 min = 300 s. Vergeet je dat, dan zit je antwoord er een factor 60 naast.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht van 10 N naar links en een kracht van 10 N naar rechts hebben dezelfde richting maar een andere zin.",
        antwoord=True,
        uitleg="De richting is de lijn waarlangs de kracht werkt, hier de horizontale lijn. De zin is de kant waarheen de pijl wijst, en die is tegengesteld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hardloper doet 400 m in 50 s. Hoeveel km/h is dat?",
        opties=["28,8 km/h", "8 km/h", "20 km/h"],
        antwoord=0,
        uitleg="Eerst v = 400 : 50 = 8 m/s, en dan 8 × 3,6 = 28,8 km/h.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hangt een gewicht aan een dynamometer en leest 12 N af. Wat heb je gemeten?",
        opties=[
            "De zwaartekracht op dat gewicht",
            "De massa van dat gewicht",
            "De massadichtheid van dat gewicht",
        ],
        antwoord=0,
        uitleg="Een dynamometer meet kracht in newton, hier de zwaartekracht. Massa meet je met een weegschaal, in kilogram.",
    ),
]
