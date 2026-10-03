# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Het zenuwstelsel.

Biologie, de kop "Het zenuwstelsel" van de vakfiche natuurwetenschappen 2de
graad doorstroom. Deel 1 gaat over de bouw: het neuron, de indeling van het
zenuwstelsel en de zenuwen. Deel 2 gaat over de impuls zelf, de synaps en de
weg die een reflex en een gewilde beweging afleggen.

De rustpotentiaal, de depolarisatie en de actiepotentiaal staan alleen in de
uitgebreide fiche (moderne talen en Latijn). Ze zitten daarom samen in deel 2.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke twee delen vormen samen het centrale zenuwstelsel?",
        opties=[
            "de hersenen en het ruggenmerg",
            "de hersenen en de hersenzenuwen",
            "het ruggenmerg en de grensstrengen",
            "de zenuwen en de zintuigen van het lichaam",
        ],
        antwoord=0,
        uitleg="Hersenen en ruggenmerg vormen het centrale zenuwstelsel. Alle zenuwen die daar vertrekken, horen bij het perifere zenuwstelsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen horen bij het perifere zenuwstelsel? Kruis alles aan wat juist is.",
        opties=["de hersenzenuwen", "de ruggenmergzenuwen", "de grensstrengen", "het ruggenmerg"],
        antwoord=[0, 1, 2],
        uitleg="Alles buiten de hersenen en het ruggenmerg hoort bij het perifere stelsel: de hersenzenuwen, de ruggenmergzenuwen en de grensstrengen. Het ruggenmerg zelf is centraal.",
    ),
    dict(
        type="waarofniet",
        vraag="Het animale zenuwstelsel stuurt bewegingen aan waarover je zelf beslist.",
        antwoord=True,
        uitleg="Het animale deel bedient de dwarsgestreepte spieren en staat onder je wil. Het autonome deel regelt wat vanzelf doorgaat, zoals de hartslag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het sympathische zenuwstelsel?",
        opties=[
            "het zet het lichaam klaar voor inspanning of gevaar",
            "het brengt het lichaam tot rust na een inspanning",
            "het geeft alleen signalen door van de zintuigen naar binnen",
            "het stuurt uitsluitend de spieren van armen en benen aan",
        ],
        antwoord=0,
        uitleg="Het sympathische deel versnelt de hartslag, verwijdt de pupillen en maakt energie vrij. Het parasympathische deel doet net het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de zenuwcel die een signaal van een zintuig naar het centrale zenuwstelsel brengt?",
        antwoord="sensorisch neuron",
        uitleg="Een sensorisch of gevoelsneuron voert naar binnen. Een motorisch neuron voert het bevel weer naar buiten, naar de spier of de klier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen horen bij een neuron? Kruis alles aan wat juist is.",
        opties=["de dendrieten", "het axon", "het cellichaam met de celkern", "de synaptische spleet"],
        antwoord=[0, 1, 2],
        uitleg="Dendrieten, axon en cellichaam zijn delen van het neuron zelf. De synaptische spleet is de ruimte tússen twee neuronen.",
    ),
    dict(
        type="waarofniet",
        vraag="De dendrieten van een neuron vangen signalen op en het axon geeft ze door.",
        antwoord=True,
        uitleg="Het signaal loopt altijd in dezelfde richting: van de dendrieten over het cellichaam naar het axon en zijn eindknopjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van de myelineschede rond een axon?",
        opties=[
            "ze isoleert het axon zodat de impuls er sneller over gaat",
            "ze maakt de neurotransmitter aan die het signaal overdraagt",
            "ze vangt de prikkel op die van het zintuig binnenkomt",
            "ze verbindt het neuron rechtstreeks met de bloedvaten",
        ],
        antwoord=0,
        uitleg="De myelineschede is een vetachtig omhulsel, gemaakt door de cellen van Schwann. De impuls springt van knoop tot knoop en gaat daardoor veel sneller.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de onderbreking in de myelineschede waar de impuls als het ware naartoe springt?",
        antwoord="knoop van Ranvier",
        uitleg="Tussen twee cellen van Schwann ligt telkens een onbeklede plek. De impuls springt van knoop naar knoop, en dat is sneller dan stap voor stap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gemengde zenuw bevat alleen motorische vezels.",
        antwoord=False,
        uitleg="Een gemengde zenuw bevat zowel sensorische als motorische vezels. De meeste ruggenmergzenuwen zijn gemengd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt een schakelneuron meestal?",
        opties=[
            "in het ruggenmerg of in de hersenen",
            "in de huid, vlak bij de receptor",
            "in de spier die de beweging uitvoert",
            "in de zenuwen van arm en been",
        ],
        antwoord=0,
        uitleg="Een schakelneuron verbindt binnen het centrale zenuwstelsel het sensorische met het motorische neuron. Bij een reflex gebeurt dat in het ruggenmerg.",
    ),
    dict(
        type="waarofniet",
        vraag="Het parasympathische zenuwstelsel vertraagt de hartslag en bevordert de spijsvertering.",
        antwoord=True,
        uitleg="Het parasympathische deel is het rustsysteem. Het zet het lichaam aan om te herstellen, te verteren en energie op te slaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een zenuw precies?",
        opties=[
            "een bundel uitlopers van veel zenuwcellen samen",
            "één lange zenuwcel met één enkele uitloper",
            "de ruimte tussen twee zenuwcellen in",
            "een spier die signalen kan doorgeven",
        ],
        antwoord=0,
        uitleg="Een zenuw is geen cel maar een bundel. Honderden of duizenden uitlopers liggen er samen in, netjes verpakt in bindweefsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beweringen over het ruggenmerg zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het ligt beschermd in het wervelkanaal",
            "het hoort bij het centrale zenuwstelsel",
            "het kan zelf een reflex afhandelen zonder de hersenen",
            "het maakt de hormonen aan die de spieren aansturen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het ruggenmerg ligt in de wervelkolom, hoort bij het centrale stelsel en sluit bij een reflex de kortste weg. Hormonen maakt het niet; dat doen klieren.",
    ),
    dict(
        type="waarofniet",
        vraag="De celkern van een neuron ligt in het axon.",
        antwoord=False,
        uitleg="De celkern ligt in het cellichaam. Het axon is de lange uitloper die het signaal wegbrengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cellen maken de myelineschede rond een axon buiten het centrale zenuwstelsel?",
        opties=[
            "de cellen van Schwann",
            "de schakelneuronen",
            "de spierspoeltjes",
            "de ganglioncellen",
        ],
        antwoord=0,
        uitleg="Een cel van Schwann wikkelt zich meermaals rond het axon. Tussen twee van die cellen blijft telkens een knoop van Ranvier vrij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het uiteinde van een axon waar de neurotransmitter vrijkomt?",
        antwoord="eindknopje",
        uitleg="In de eindknopjes liggen blaasjes met neurotransmitter klaar. Komt de impuls aan, dan storten die hun inhoud in de synaptische spleet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een motorisch neuron brengt een bevel naar een effector. Welke effectoren kunnen dat zijn? Kruis alles aan wat juist is.",
        opties=["een spier", "een klier", "het hartspierweefsel", "een receptor in de huid"],
        antwoord=[0, 1, 2],
        uitleg="Spieren en klieren zijn de effectoren, de hartspier ook. Een receptor staat juist aan het begin van de weg, niet aan het einde.",
    ),
    dict(
        type="waarofniet",
        vraag="De grensstrengen links en rechts van de wervelkolom horen bij het animale zenuwstelsel.",
        antwoord=False,
        uitleg="Ze horen bij het autonome zenuwstelsel. In de grensstrengen liggen de schakelplaatsen van het sympathische deel, van waaruit zenuwen naar de organen lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een gemyeliniseerde zenuwvezel sneller dan een vezel zonder myeline?",
        opties=[
            "de impuls springt van knoop tot knoop in plaats van over de hele lengte te lopen",
            "de impuls hoeft geen neurotransmitter meer te gebruiken onderweg",
            "de vezel is dunner en het signaal moet dus minder ver",
            "de vezel maakt onderweg extra signalen bij die elkaar inhalen",
        ],
        antwoord=0,
        uitleg="Dat springen heet saltatoire geleiding. Omdat alleen de knopen van Ranvier meedoen, legt de impuls dezelfde afstand veel sneller af.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de rustpotentiaal van een neuron?",
        opties=[
            "het spanningsverschil over het membraan als er geen impuls is",
            "de spanning die ontstaat op het ogenblik dat er een impuls komt",
            "de tijd die een neuron nodig heeft voor het weer kan vuren",
            "de kracht waarmee een neurotransmitter op de receptor past",
        ],
        antwoord=0,
        uitleg="In rust is de binnenkant van het neuron negatief ten opzichte van de buitenkant. Dat vaste spanningsverschil is de rustpotentiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de stappen van een actiepotentiaal in de juiste volgorde.",
        opties=[
            "rustpotentiaal, depolarisatie, repolarisatie, herstelfase",
            "depolarisatie, rustpotentiaal, herstelfase, repolarisatie",
            "repolarisatie, depolarisatie, rustpotentiaal, herstelfase",
            "herstelfase, repolarisatie, depolarisatie, rustpotentiaal",
        ],
        antwoord=0,
        uitleg="Vanuit de rust slaat de spanning om bij de depolarisatie, keert ze terug bij de repolarisatie, en daarna volgt de herstelfase waarin het neuron weer klaar komt te staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prikkel die onder de drempelwaarde blijft, levert geen impuls op.",
        antwoord=True,
        uitleg="Pas boven de drempelwaarde vuurt het neuron. Daaronder gebeurt er niets; het is alles of niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een prikkel wordt twee keer zo sterk. Wat verandert er aan de impulsen in één zenuwvezel?",
        opties=[
            "er volgen meer impulsen per seconde, elk even groot",
            "elke impuls wordt twee keer zo groot als daarvoor",
            "de impulsen worden trager maar ook veel sterker",
            "er komt één impuls die twee keer zo lang duurt",
        ],
        antwoord=0,
        uitleg="De amplitude van een actiepotentiaal ligt vast. Een sterkere prikkel laat het neuron sneller na elkaar vuren, en zo weten de hersenen hoe sterk de prikkel was.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de smalle ruimte tussen het eindknopje van het ene neuron en het volgende neuron?",
        antwoord="synaptische spleet",
        uitleg="De neuronen raken elkaar niet. De neurotransmitter zwemt door die spleet naar de membraanreceptoren aan de overkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een synaps? Kruis alles aan wat juist is.",
        opties=[
            "de impuls laat blaasjes met neurotransmitter leeglopen",
            "de neurotransmitter past op membraanreceptoren aan de overkant",
            "het signaal gaat er maar in één richting over",
            "het signaal springt er als een vonk rechtstreeks over",
        ],
        antwoord=[0, 1, 2],
        uitleg="In de synaps wordt het elektrische signaal even chemisch. Alleen het eindknopje heeft blaasjes en alleen de overkant heeft receptoren, dus de richting ligt vast.",
    ),
    dict(
        type="waarofniet",
        vraag="De impulsoverdracht is van begin tot eind een zuiver elektrisch proces.",
        antwoord=False,
        uitleg="Binnen het neuron is het signaal elektrisch, maar in de synaps wordt het even chemisch, met een neurotransmitter. Aan de overkant wordt het weer elektrisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke weg legt een terugtrekreflex af?",
        opties=[
            "receptor, sensorisch neuron, schakelneuron in het ruggenmerg, motorisch neuron, spier",
            "receptor, sensorisch neuron, grote hersenen, motorisch neuron, spier",
            "receptor, motorisch neuron, schakelneuron, sensorisch neuron, spier",
            "spier, motorisch neuron, ruggenmerg, sensorisch neuron, receptor",
        ],
        antwoord=0,
        uitleg="Bij een reflex gaat het signaal niet eerst naar de grote hersenen. Het wordt in het ruggenmerg overgeschakeld, en daarom ben je zo snel weg van de hete pan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een gewilde beweging komen de grote hersenen er niet aan te pas.",
        antwoord=False,
        uitleg="Net wel. Een gewilde beweging vertrekt in de hersenschors; alleen een reflex loopt via de kortere weg door het ruggenmerg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze reacties zijn reflexen? Kruis alles aan wat juist is.",
        opties=[
            "de pupilreflex bij fel licht",
            "de kniepeesreflex bij een tik onder de knieschijf",
            "het terugtrekken van je hand bij hitte",
            "het aanbinden van je veters",
        ],
        antwoord=[0, 1, 2],
        uitleg="Pupilreflex, kniepeesreflex en terugtrekreflex gaan vanzelf en razendsnel. Je veters knopen is een aangeleerde, gewilde beweging.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de stof die in de synaps vrijkomt om het signaal over te dragen?",
        antwoord="neurotransmitter",
        uitleg="Een neurotransmitter is de chemische boodschapper van de synaps. Hij past als een sleutel op de receptoren aan de overkant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een signaal in een synaps maar in één richting?",
        opties=[
            "alleen het eindknopje heeft blaasjes en alleen de overkant heeft receptoren",
            "de spleet is te smal om in de andere richting over te steken",
            "de neurotransmitter beweegt alleen van boven naar beneden",
            "het axon ligt altijd hoger dan de dendriet ernaast",
        ],
        antwoord=0,
        uitleg="De bouw bepaalt de richting. Zender en ontvanger zijn verschillend, en dus kan het signaal maar één kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="Na een impuls is een neuron even niet in staat om opnieuw te vuren.",
        antwoord=True,
        uitleg="Dat is de herstelfase. Het membraan moet eerst zijn rustpotentiaal terugkrijgen voor er een nieuwe actiepotentiaal kan ontstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de toeschietreflex?",
        opties=[
            "het vrijkomen van melk uit de melkklier wanneer de baby zuigt",
            "het samentrekken van de pupil wanneer er fel licht op valt",
            "het strekken van het onderbeen bij een tik op de kniepees",
            "het wegtrekken van de hand wanneer je iets heets aanraakt",
        ],
        antwoord=0,
        uitleg="Het zuigen van de baby is de prikkel; het hormoon oxytocine zorgt dat de melk toeschiet. Het is een reflex waarbij ook een klier meedoet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent depolarisatie?",
        opties=[
            "het spanningsverschil over het membraan slaat kortstondig om",
            "het spanningsverschil over het membraan keert terug naar de rust",
            "het neuron maakt extra neurotransmitter aan in zijn eindknopjes",
            "het neuron verliest zijn myelineschede over een stukje axon",
        ],
        antwoord=0,
        uitleg="Bij depolarisatie stromen er positieve deeltjes naar binnen en wordt de binnenkant even positief. Daarna volgt de repolarisatie, waarbij de rusttoestand terugkeert.",
    ),
    dict(
        type="waarofniet",
        vraag="De amplitude van een actiepotentiaal wordt groter naarmate de prikkel sterker is.",
        antwoord=False,
        uitleg="De amplitude ligt vast. Een sterkere prikkel verandert niet de grootte maar het aantal impulsen per seconde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een reflex nuttig?",
        opties=[
            "het lichaam reageert op gevaar nog voor je erover nadenkt",
            "het lichaam kan zo bewegingen aanleren die het nog niet kent",
            "het lichaam spaart er neurotransmitter mee uit",
            "het lichaam kan zo sterkere spiersamentrekkingen maken",
        ],
        antwoord=0,
        uitleg="Omdat de weg over het ruggenmerg veel korter is, win je kostbare tijd. Je bent al weg van de hete pan voor je de pijn voelt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de hele weg die een impuls bij een reflex aflegt, van receptor tot effector?",
        antwoord="reflexboog",
        uitleg="De reflexboog loopt van de receptor via het sensorische neuron en het schakelneuron naar het motorische neuron en de effector.",
    ),
    dict(
        type="waarofniet",
        vraag="Een neurotransmitter werkt volgens het sleutel-slotprincipe: hij past maar op bepaalde receptoren.",
        antwoord=True,
        uitleg="Alleen een receptor met de juiste vorm reageert op die stof. Daardoor komt het signaal precies terecht waar het moet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je voelt pas pijn nadat je je hand al hebt weggetrokken. Hoe komt dat?",
        opties=[
            "de reflex loopt via het ruggenmerg, het pijnsignaal moet nog naar de hersenen",
            "de pijnreceptoren reageren veel trager dan de warmtereceptoren",
            "het ruggenmerg houdt het pijnsignaal eerst even tegen",
            "de spier stuurt het pijnsignaal pas door nadat ze samengetrokken is",
        ],
        antwoord=0,
        uitleg="De reflexboog is kort en klaar voor het signaal de hersenen bereikt. Pijn ontstaat pas in de hersenen, en dat duurt een fractie langer.",
    ),
]
