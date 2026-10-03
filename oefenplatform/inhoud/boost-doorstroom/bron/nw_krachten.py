# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Vrije val, verticale worp en krachten.

Fysica, de koppen "Verticale worp en vrije val", "Krachten", "Krachten
samenstellen", "Zwaartekracht" en "Veerkracht" van de vakfiche
natuurwetenschappen 2de graad doorstroom. Deel 1 gaat over de vrije val, de
verticale worp en de soorten krachten; deel 2 over krachten samenstellen, de
krachtenbalans, de zwaartekracht en de veerkracht.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een vrije val?",
        opties=[
            "een val waarbij alleen de zwaartekracht op het voorwerp werkt",
            "een val waarbij ook de wrijving van de lucht een rol speelt",
            "een val waarbij het voorwerp eerst naar boven wordt gegooid",
            "een val waarbij het voorwerp met een vaste snelheid naar beneden gaat",
        ],
        antwoord=0,
        uitleg="Je verwaarloost de luchtweerstand. Daardoor valt elk voorwerp even snel, hoe zwaar het ook is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe groot is de valversnelling op aarde ongeveer?",
        opties=[
            "9,81 meter per seconde kwadraat",
            "1,62 meter per seconde kwadraat",
            "98,1 meter per seconde kwadraat",
            "0,98 meter per seconde kwadraat",
        ],
        antwoord=0,
        uitleg="Elke seconde komt er ongeveer 9,81 meter per seconde snelheid bij. Op de maan is dat maar 1,62.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vrije val zonder luchtweerstand vallen een steen en een pluim even snel.",
        antwoord=True,
        uitleg="De valversnelling is voor elke massa dezelfde. In lucht wint de steen alleen doordat de pluim veel meer weerstand ondervindt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gooit een bal recht naar boven. Wat gebeurt er in het hoogste punt?",
        opties=[
            "de snelheid is nul maar de versnelling blijft naar beneden gericht",
            "de snelheid en de versnelling zijn op dat ogenblik allebei nul",
            "de versnelling is nul maar de snelheid blijft naar boven gericht",
            "de snelheid en de versnelling zijn allebei naar boven gericht",
        ],
        antwoord=0,
        uitleg="De zwaartekracht stopt geen moment. Daarom gaat de bal in dat punt onmiddellijk weer naar beneden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de beweging van een bal die je recht naar boven gooit?",
        antwoord="verticale worp",
        uitleg="Zodra de bal weer naar beneden komt, is het een vrije val. De versnelling is in beide fasen dezelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een steen valt uit stilstand. Welke snelheid heeft hij na 2 seconden, met 10 meter per seconde kwadraat als valversnelling?",
        opties=[
            "20 meter per seconde",
            "10 meter per seconde",
            "5 meter per seconde",
            "40 meter per seconde",
        ],
        antwoord=0,
        uitleg="Je vermenigvuldigt de valversnelling met de tijd: 10 maal 2. Dat is dezelfde rekenwijze als bij elke eenparig versnelde beweging.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een verticale worp naar boven is de versnelling tijdens het opgaan naar boven gericht.",
        antwoord=False,
        uitleg="De zwaartekracht werkt altijd naar beneden, ook tijdens het opgaan. Daardoor wordt de bal juist vertraagd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten zijn echte soorten krachten? Kruis alles aan wat juist is.",
        opties=["de zwaartekracht", "de normaalkracht", "de wrijvingskracht", "de versnellingskracht"],
        antwoord=[0, 1, 2],
        uitleg="Zwaartekracht, normaalkracht, wrijvingskracht, veerkracht, spankracht en motorkracht zijn soorten krachten. Een versnellingskracht bestaat niet als aparte soort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de normaalkracht?",
        opties=[
            "de kracht waarmee een oppervlak loodrecht terugduwt op het voorwerp",
            "de kracht waarmee de aarde elk voorwerp naar haar middelpunt trekt",
            "de kracht die een voorwerp tegenwerkt als het over iets schuift",
            "de kracht waarmee een uitgerekte veer aan het voorwerp trekt",
        ],
        antwoord=0,
        uitleg="Normaal betekent hier loodrecht. Het is de kracht waarmee een tafel een boek tegenhoudt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het punt waarin je de hele zwaartekracht op een voorwerp laat aangrijpen?",
        antwoord="zwaartepunt",
        uitleg="Bij een regelmatig voorwerp ligt dat punt in het midden. Of een voorwerp omvalt, hangt af van waar dat punt zich bevindt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen kan een resulterende kracht teweegbrengen? Kruis alles aan wat juist is.",
        opties=[
            "versnellen",
            "vertragen",
            "van richting veranderen",
            "van massa veranderen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie zijn samen wat we een verandering van bewegingstoestand noemen. De massa van een voorwerp verandert niet door een kracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp dat met een constante snelheid in een rechte lijn beweegt, heeft een resulterende kracht van nul.",
        antwoord=True,
        uitleg="Alle krachten erop heffen elkaar dan op. Dat heet een krachtenbalans, en dan verandert er niets aan de beweging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boek ligt stil op een tafel. Welke krachten werken erop?",
        opties=[
            "de zwaartekracht naar beneden en de normaalkracht naar boven",
            "alleen de zwaartekracht naar beneden, want het boek beweegt niet",
            "alleen de normaalkracht naar boven, want de tafel houdt het tegen",
            "de zwaartekracht naar beneden en de wrijvingskracht naar boven",
        ],
        antwoord=0,
        uitleg="Die twee zijn even groot en tegengesteld, dus is de resulterende kracht nul. Daarom blijft het boek liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een parachutist valt na een tijdje met een constante snelheid. Wat weet je dan?",
        opties=[
            "de luchtweerstand is even groot geworden als de zwaartekracht",
            "de zwaartekracht heeft op die hoogte helemaal opgehouden",
            "de parachutist heeft zijn massa tijdens het vallen verloren",
            "de luchtweerstand is op dat ogenblik groter dan de zwaartekracht",
        ],
        antwoord=0,
        uitleg="De twee krachten heffen elkaar op, dus is er geen versnelling meer. Die snelheid heet de eindsnelheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kracht is een vectoriële grootheid.",
        antwoord=True,
        uitleg="Een kracht heeft een grootte, een richting, een zin en een aangrijpingspunt. Daarom tekenen we ze als een pijl.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eenheid van kracht?",
        opties=["de newton", "de joule", "de pascal", "de watt"],
        antwoord=0,
        uitleg="Eén newton is de kracht die een massa van één kilogram één meter per seconde kwadraat doet versnellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto remt. In welke zin werkt de resulterende kracht?",
        opties=[
            "tegengesteld aan de zin van de beweging",
            "in dezelfde zin als de beweging",
            "loodrecht op de zin van de beweging",
            "er werkt op dat ogenblik geen enkele kracht",
        ],
        antwoord=0,
        uitleg="Vertragen betekent dat de resulterende kracht de beweging tegenwerkt. De wrijving van de remmen zorgt daarvoor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kracht die een voorwerp tegenwerkt wanneer het over een oppervlak schuift?",
        antwoord="wrijvingskracht",
        uitleg="Ze werkt altijd tegengesteld aan de beweging. Zonder wrijving zou je niet kunnen stappen of remmen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voorwerp in een vrije val heeft tijdens het vallen een steeds grotere versnelling.",
        antwoord=False,
        uitleg="De versnelling blijft gelijk aan de valversnelling. Het is de snelheid die steeds groter wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat een bal vallen en gooit een tweede bal op hetzelfde ogenblik recht naar beneden. Wat verschilt er?",
        opties=[
            "de tweede bal heeft een beginsnelheid, maar dezelfde versnelling",
            "de tweede bal heeft een grotere versnelling dan de eerste bal",
            "de tweede bal heeft geen versnelling omdat hij al snelheid heeft",
            "de tweede bal valt precies even snel als de bal die je laat vallen",
        ],
        antwoord=0,
        uitleg="De zwaartekracht is voor beide ballen dezelfde, dus is de versnelling gelijk. Alleen de beginsnelheid verschilt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de grootte van de zwaartekracht op een voorwerp?",
        opties=[
            "de massa vermenigvuldigen met de zwaarteveldsterkte",
            "de massa delen door de zwaarteveldsterkte van de plaats",
            "de massa vermenigvuldigen met de snelheid van het voorwerp",
            "de massa optellen bij de zwaarteveldsterkte van de plaats",
        ],
        antwoord=0,
        uitleg="Massa maal zwaarteveldsterkte geeft de kracht in newton. Op aarde is die sterkte ongeveer 9,81 newton per kilogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over massa en gewicht zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "massa is de hoeveelheid materie in een voorwerp",
            "gewicht is een kracht en meet je in newton",
            "je massa blijft op de maan dezelfde",
            "je gewicht blijft op de maan hetzelfde",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je massa is overal gelijk, ook op de maan. Je gewicht is daar zes keer kleiner, omdat de zwaarteveldsterkte kleiner is.",
    ),
    dict(
        type="waarofniet",
        vraag="De massa van een voorwerp verandert niet als je het naar de maan brengt.",
        antwoord=True,
        uitleg="Massa is de hoeveelheid materie en die blijft dezelfde. Alleen de zwaartekracht erop verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een voorwerp van 5 kilogram hangt stil aan een veer. Hoe groot is de veerkracht, met 10 newton per kilogram?",
        opties=["50 newton", "5 newton", "10 newton", "0,5 newton"],
        antwoord=0,
        uitleg="Het voorwerp hangt stil, dus is er een krachtenbalans. De veerkracht is dan even groot als de zwaartekracht van 50 newton.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk toestel meet je rechtstreeks de grootte van een kracht?",
        antwoord="dynamometer",
        uitleg="Een dynamometer is in de kern een veer met een schaal erop. Hoe verder de veer uitrekt, hoe groter de kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de veerkracht van een veer?",
        opties=[
            "de veerconstante vermenigvuldigen met de lengteverandering",
            "de veerconstante delen door de lengteverandering van de veer",
            "de massa vermenigvuldigen met de lengte van de hele veer",
            "de lengteverandering delen door de massa van het voorwerp",
        ],
        antwoord=0,
        uitleg="De veerkracht is recht evenredig met hoeveel de veer uitrekt. De veerconstante zegt hoe stug die veer is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een veer met een grotere veerconstante rekt bij dezelfde kracht minder uit.",
        antwoord=True,
        uitleg="Een grote veerconstante betekent een stugge veer. Je hebt dan meer kracht nodig voor dezelfde uitrekking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee krachten van 30 en 40 newton werken op hetzelfde punt en maken een hoek van 90 graden. Hoe groot is de resultante?",
        opties=["50 newton", "70 newton", "10 newton", "35 newton"],
        antwoord=0,
        uitleg="Bij een rechte hoek gebruik je de stelling van Pythagoras: de wortel uit 900 plus 1600 is 50.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee krachten van 30 en 40 newton werken op hetzelfde punt in dezelfde richting en dezelfde zin. Hoe groot is de resultante?",
        opties=["70 newton", "50 newton", "10 newton", "1200 newton"],
        antwoord=0,
        uitleg="Werken twee krachten in dezelfde zin, dan tel je hun groottes gewoon op. Bij tegengestelde zin trek je ze van elkaar af.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de ene kracht die hetzelfde effect heeft als alle krachten samen?",
        antwoord="resultante",
        uitleg="Je kan ze ook de resulterende kracht noemen. Is ze nul, dan verandert de bewegingstoestand niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de zwaarteveldsterkte zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "op de maan is ze veel kleiner dan op aarde",
            "ze wordt uitgedrukt in newton per kilogram",
            "ze verschilt van hemellichaam tot hemellichaam",
            "ze is op elk hemellichaam precies dezelfde",
        ],
        antwoord=[0, 1, 2],
        uitleg="Op aarde is ze ongeveer 9,81 en op de maan 1,62 newton per kilogram. Daardoor weegt hetzelfde voorwerp op de maan veel minder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een astronaut zweeft in een ruimtestation. Wat is er met zijn massa gebeurd?",
        opties=[
            "niets, zijn massa is net dezelfde als op aarde",
            "zijn massa is tot nul herleid door het zweven",
            "zijn massa is zes keer kleiner geworden dan op aarde",
            "zijn massa is groter geworden door de hoge snelheid",
        ],
        antwoord=0,
        uitleg="Gewichtloos zijn betekent niet massaloos zijn. Het station en de astronaut vallen samen rond de aarde, en daarom voelt hij geen druk van een vloer.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee krachten van gelijke grootte en tegengestelde zin tellen samen op tot een dubbel zo grote resultante.",
        antwoord=False,
        uitleg="Ze heffen elkaar volledig op, dus is de resultante nul. Optellen doe je alleen bij krachten in dezelfde zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet de zwaartekracht op verschillende massa's en zet ze in een grafiek. Wat zie je?",
        opties=[
            "een rechte door de oorsprong, want de twee zijn recht evenredig",
            "een kromme die naar boven afbuigt bij grotere massa's",
            "een vlakke lijn, want de zwaartekracht blijft altijd gelijk",
            "een rechte die daalt, want een grotere massa valt trager",
        ],
        antwoord=0,
        uitleg="De steilheid van die rechte is de zwaarteveldsterkte. Zo kan je uit meetresultaten afleiden op welk hemellichaam gemeten is.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gewicht van een voorwerp meet je in kilogram.",
        antwoord=False,
        uitleg="Gewicht is een kracht en meet je dus in newton. De kilogram is de eenheid van massa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een veer rekt 4 centimeter uit bij een kracht van 20 newton. Wat is de veerconstante?",
        opties=[
            "5 newton per centimeter",
            "80 newton per centimeter",
            "0,2 newton per centimeter",
            "24 newton per centimeter",
        ],
        antwoord=0,
        uitleg="Je deelt de kracht door de uitrekking: 20 gedeeld door 4. Met die constante kan je elke andere uitrekking voorspellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten werken op een auto die met constante snelheid op een vlakke weg rijdt? Kruis alles aan wat juist is.",
        opties=[
            "de motorkracht naar voren",
            "de wrijvingskracht naar achteren",
            "de zwaartekracht naar beneden",
            "een extra kracht die hem vooruit blijft versnellen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Motorkracht en wrijving zijn even groot, dus blijft de snelheid gelijk. Een extra versnellende kracht is er niet, anders zou hij sneller gaan.",
    ),
    dict(
        type="waarofniet",
        vraag="De zwaartekracht is een veldkracht: ze werkt zonder dat er contact nodig is.",
        antwoord=True,
        uitleg="De aarde hoeft een voorwerp niet aan te raken om eraan te trekken. Een normaalkracht of wrijvingskracht vraagt wel contact.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel newton is de zwaartekracht op een massa van 2 kilogram, met 10 newton per kilogram?",
        antwoord="20",
        uitleg="Je vermenigvuldigt de massa met de zwaarteveldsterkte: 2 maal 10. Met de nauwkeuriger 9,81 kom je op 19,62 newton.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kist staat stil op een helling en schuift niet weg. Welke kracht houdt haar tegen?",
        opties=[
            "de wrijvingskracht tussen de kist en de helling",
            "de normaalkracht van de helling op de kist",
            "de zwaartekracht van de aarde op de kist",
            "de spankracht van het oppervlak van de helling",
        ],
        antwoord=0,
        uitleg="De zwaartekracht trekt de kist langs de helling naar beneden. Alleen de wrijving kan die component tegenhouden.",
    ),
]
