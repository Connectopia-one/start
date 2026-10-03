# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Grootheden, eenheden en wetenschappelijk onderzoek.

Het onderdeel "Wetenschappelijk onderzoek en STEM" van de vakfiche
natuurwetenschappen 2de graad doorstroom: de koppen "Grootheden, eenheden en
verbanden", "Onderzoeksmethode", "Ontwerp van een oplossing" en "Interactie
tussen STEM-disciplines onderling en met de maatschappij". Deel 1 gaat over
grootheden, eenheden, voorvoegsels en verbanden tussen grootheden; deel 2
over de stappen van een onderzoek, het ontwerpen van een oplossing en de
wisselwerking met de maatschappij.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een grootheid en een eenheid?",
        opties=[
            "de grootheid is wat je meet, de eenheid is waarin je het uitdrukt",
            "de eenheid is wat je meet, de grootheid is waarin je het uitdrukt",
            "een grootheid hoort bij fysica en een eenheid bij chemie",
            "een grootheid is altijd een vector en een eenheid nooit",
        ],
        antwoord=0,
        uitleg="Lengte is de grootheid, de meter is de eenheid. Een meetresultaat bestaat altijd uit een getal en een eenheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijn SI-eenheden? Kruis alles aan wat juist is.",
        opties=["de meter", "de kilogram", "de seconde", "de kilometer per uur"],
        antwoord=[0, 1, 2],
        uitleg="De kilometer per uur is een afgeleide eenheid die veel gebruikt wordt, maar in het SI-stelsel reken je snelheid in meter per seconde.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorvoegsel mega betekent een miljoen.",
        antwoord=True,
        uitleg="Kilo is duizend, mega een miljoen. Naar de andere kant gaat het over centi en milli naar micro en nano.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel seconden is 2 microseconden?",
        opties=[
            "2 maal tien tot de macht min zes seconden",
            "2 maal tien tot de macht min drie seconden",
            "2 maal tien tot de macht min negen seconden",
            "2 maal tien tot de macht zes seconden",
        ],
        antwoord=0,
        uitleg="Micro betekent een miljoenste. Nano is nog duizend keer kleiner, dus tien tot de macht min negen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk voorvoegsel betekent een miljardste?",
        antwoord="nano",
        uitleg="Nano is tien tot de macht min negen. Een nanometer is dus een miljardste van een meter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee grootheden zijn recht evenredig. Hoe ziet hun grafiek uit?",
        opties=[
            "een rechte die door de oorsprong gaat",
            "een rechte die de verticale as boven nul snijdt",
            "een kromme die naar de assen toe buigt",
            "een vlakke lijn boven de horizontale as",
        ],
        antwoord=0,
        uitleg="Recht evenredig betekent dat de verhouding gelijk blijft. Nul hoort dan bij nul, dus gaat de rechte door de oorsprong.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een omgekeerd evenredig verband blijft het product van de twee grootheden gelijk.",
        antwoord=True,
        uitleg="Wordt de ene twee keer groter, dan wordt de andere twee keer kleiner. De grafiek is een kromme die naar de assen toe buigt zonder ze te raken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verdubbelt de ene grootheid en de andere wordt vier keer zo groot. Welk verband is dat?",
        opties=[
            "een kwadratisch verband",
            "een recht evenredig verband",
            "een omgekeerd evenredig verband",
            "een lineair verband met een constante erbij",
        ],
        antwoord=0,
        uitleg="Twee in het kwadraat is vier. De kinetische energie en de snelheid hangen zo samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een lineair en een recht evenredig verband?",
        opties=[
            "een lineair verband is een rechte die niet door de oorsprong hoeft te gaan",
            "een lineair verband is een kromme en een recht evenredig verband een rechte",
            "een lineair verband geldt alleen voor positieve waarden van de grootheden",
            "een lineair verband heeft altijd een steilheid die precies gelijk is aan een",
        ],
        antwoord=0,
        uitleg="Recht evenredig is het bijzondere geval dat de rechte door nul gaat. De lengte van een veer in functie van de kracht is lineair maar niet recht evenredig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel gram is 0,25 kilogram?",
        antwoord="250",
        uitleg="Kilo betekent duizend, dus vermenigvuldig je met 1000. Omgekeerd deel je door 1000 om van gram naar kilogram te gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zet je meetresultaten in een tabel voor je een grafiek maakt?",
        opties=[
            "zo zie je de paren bij elkaar en kan je ze ordenen voor je ze uitzet",
            "zo hoef je de eenheden niet meer bij elk van de getallen te schrijven",
            "zo wordt de meting zelf nauwkeuriger dan ze eerst was",
            "zo kan je de getallen afronden tot ze mooi uitkomen",
        ],
        antwoord=0,
        uitleg="Een tabel laat je de metingen overzichtelijk naast elkaar zetten, met hun eenheid in de hoofding. Pas daarna zie je in de grafiek welk verband erin zit.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een formule omvormen zodat een andere grootheid alleen staat.",
        antwoord=True,
        uitleg="Uit de wet van Ohm haal je zo zowel de spanning als de stroomsterkte of de weerstand. Je doet aan beide kanten hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel meter is 45 centimeter?",
        opties=["0,45 meter", "4,5 meter", "450 meter", "0,045 meter"],
        antwoord=0,
        uitleg="Centi betekent een honderdste, dus deel je door 100. Milli zou door 1000 zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet een lengte met een meetlint en leest 1,2 meter af. Hoeveel beduidende cijfers heeft dat resultaat?",
        opties=["twee", "een", "drie", "vier"],
        antwoord=0,
        uitleg="De 1 en de 2 zijn beide gemeten. Schrijf je 1,200 meter, dan beweer je een nauwkeurigheid die het meetlint niet heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meetresultaat zonder eenheid is nog altijd bruikbaar als je het getal kent.",
        antwoord=False,
        uitleg="Vijf kan vijf meter of vijf kilometer zijn. Zonder eenheid zegt het getal niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootheden en eenheden horen bij elkaar? Kruis alles aan wat juist is.",
        opties=[
            "kracht in newton",
            "energie in joule",
            "vermogen in watt",
            "druk in newton",
        ],
        antwoord=[0, 1, 2],
        uitleg="Druk meet je in pascal, dus newton per vierkante meter. De newton alleen is de eenheid van kracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je eerst een schatting van je antwoord?",
        opties=[
            "zo merk je meteen of je uitkomst een onzinnige grootte heeft",
            "zo hoef je de echte berekening daarna niet meer te maken",
            "zo wordt je meting achteraf nauwkeuriger dan ze was",
            "zo kan je de eenheid van het antwoord gewoon weglaten",
        ],
        antwoord=0,
        uitleg="Weet je dat een mens ongeveer 70 kilogram weegt, dan zie je een uitkomst van 7000 kilogram direct als fout. Dat vangt een rekenfout vroeg op.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is de SI-eenheid van tijd?",
        antwoord="seconde",
        uitleg="Alle andere tijdseenheden leid je daarvan af. In formules reken je altijd in seconden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek geeft je precieze meetwaarden en een tabel toont je het verband ertussen.",
        antwoord=False,
        uitleg="Het is net omgekeerd: een tabel geeft de precieze waarden, een grafiek laat het verband zien. Uit beide kan je gegevens halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet een massa met een balans die tot op een gram nauwkeurig is. Hoe schrijf je 325 gram op?",
        opties=[
            "als 325 gram, met drie beduidende cijfers",
            "als 325,00 gram, want dat ziet nauwkeuriger uit",
            "als ongeveer 300 gram, want afronden is veiliger",
            "als 0,325 gram, want gram is de SI-eenheid",
        ],
        antwoord=0,
        uitleg="Je schrijft precies wat je gemeten hebt, niet meer en niet minder. De SI-eenheid van massa is trouwens de kilogram, dus 0,325 kilogram.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een onderzoeksvraag?",
        opties=[
            "de vraag die je met je onderzoek wil beantwoorden",
            "het antwoord dat je al voor het onderzoek verwacht",
            "de lijst materialen die je voor het onderzoek nodig hebt",
            "de conclusie die je achteraf uit je gegevens trekt",
        ],
        antwoord=0,
        uitleg="Ze moet nauwkeurig genoeg zijn om er echt op te kunnen antwoorden. Het verwachte antwoord erbij heet de hypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "een onderbouwde verwachting die je met je onderzoek nagaat",
            "een conclusie die uit de gemeten gegevens volgt",
            "een vraag die je aan het begin van je onderzoek stelt",
            "een lijst van de stappen die je gaat uitvoeren",
        ],
        antwoord=0,
        uitleg="Ze mag ook verkeerd blijken. Dat is geen mislukt onderzoek, want ook een weerlegde hypothese levert kennis op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die door het onderzoek weerlegd wordt, maakt het onderzoek niet waardeloos.",
        antwoord=True,
        uitleg="Je weet daarna meer dan ervoor. Wetenschap werkt juist door verwachtingen te testen en te verwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij de wetenschappelijke methode? Kruis alles aan wat juist is.",
        opties=[
            "een onderzoeksvraag opstellen",
            "data verzamelen en analyseren",
            "een conclusie formuleren",
            "de gegevens aanpassen tot ze bij je hypothese passen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gegevens aanpassen is geen onderzoek maar bedrog. Je past je conclusie aan de gegevens aan, nooit omgekeerd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het plan waarin je vastlegt hoe je je onderzoek gaat uitvoeren?",
        antwoord="onderzoeksplan",
        uitleg="Daarin staat welke metingen je doet, met welk materiaal en in welke orde. Zo kan iemand anders je onderzoek herhalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verander je in een proef maar één ding tegelijk?",
        opties=[
            "anders weet je achteraf niet welke verandering het gevolg veroorzaakte",
            "anders duurt de proef veel langer dan ze hoeft te duren",
            "anders heb je voor de proef veel meer materiaal nodig dan je hebt staan",
            "anders kan je de gegevens niet in een tabel zetten",
        ],
        antwoord=0,
        uitleg="Alle andere omstandigheden houd je gelijk. Zo weet je zeker waar het verschil vandaan komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een conclusie moet een antwoord geven op de onderzoeksvraag en steunen op je gegevens.",
        antwoord=True,
        uitleg="Wat je niet gemeten hebt, mag niet in je conclusie staan. En een conclusie die de vraag niet beantwoordt, is geen conclusie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting een paar keer?",
        opties=[
            "om de invloed van toevallige meetfouten kleiner te maken",
            "om het meetinstrument zelf nauwkeuriger te maken",
            "om meer getallen te hebben voor je tabel en je grafiek",
            "om de proef langer te laten duren dan één meting zou",
        ],
        antwoord=0,
        uitleg="Het gemiddelde van meer metingen ligt dichter bij de echte waarde. Een grote spreiding verraadt bovendien dat er iets niet klopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als eerste bij het ontwerpen van een oplossing voor een probleem?",
        opties=[
            "je definieert het probleem zo scherp als je kan",
            "je bouwt een eerste versie en kijkt of ze werkt",
            "je kiest het materiaal waarmee je gaat werken",
            "je schrijft je besluit over de oplossing al op",
        ],
        antwoord=0,
        uitleg="Pas als het probleem duidelijk is, kan je criteria opstellen waaraan je oplossing moet voldoen. Daarna splits je het eventueel in deelproblemen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de voorwaarden waaraan je oplossing moet voldoen?",
        antwoord="criteria",
        uitleg="Zonder criteria kan je achteraf niet beoordelen of je oplossing goed is. Ze maken het evalueren mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom splits je een moeilijk probleem op in deelproblemen?",
        opties=[
            "elk deel is afzonderlijk makkelijker op te lossen en samen vormen ze het geheel",
            "zo hoef je de moeilijkste delen van het probleem niet meer aan te pakken",
            "zo heb je meer kans dat minstens een deel van de oplossing toevallig werkt",
            "zo wordt het probleem zelf een stuk kleiner dan het in het begin was",
        ],
        antwoord=0,
        uitleg="Je lost de delen apart op en integreert ze daarna in één totaaloplossing. Het probleem blijft wel even groot.",
    ),
    dict(
        type="waarofniet",
        vraag="Zodra je oplossing gebouwd is, ben je klaar en hoef je ze niet meer te evalueren.",
        antwoord=False,
        uitleg="Bijna geen enkel ontwerp is in één keer goed. Je toetst het aan je criteria en stuurt het bij waar nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de letters van STEM?",
        opties=[
            "wetenschappen, technologie, engineering en wiskunde",
            "wetenschappen, techniek, economie en maatschappij",
            "studie, techniek, ervaring en meten",
            "systemen, technologie, energie en materialen",
        ],
        antwoord=0,
        uitleg="De M staat voor mathematics, dus wiskunde. Het idee is dat die vier samen aan een probleem werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rollen speelden de STEM-disciplines bij de ontwikkeling van een vaccin? Kruis alles aan wat juist is.",
        opties=[
            "wetenschappelijke kennis om het vaccin te ontwikkelen",
            "technologische kennis om het koel te bewaren en te vervoeren",
            "wiskundige kennis om de verspreiding in kaart te brengen",
            "taalkundige kennis om het vaccin werkzaam te maken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Dat is een voorbeeld van hoe de disciplines samenwerken aan één maatschappelijke uitdaging. Elke discipline droeg er haar eigen stuk aan bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Maatschappelijke uitdagingen zijn een reden waarom er nieuwe technieken en materialen ontwikkeld worden.",
        antwoord=True,
        uitleg="Denk aan de energieomslag of aan een pandemie. De vraag uit de maatschappij stuurt waar onderzoek naartoe gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in een grafiek dat de stroomsterkte recht evenredig stijgt met de spanning. Wat concludeer je?",
        opties=[
            "de weerstand is in die meetreeks constant gebleven",
            "de weerstand is tijdens de meting gelijkmatig gestegen",
            "de weerstand is tijdens de meting gelijkmatig gedaald",
            "de weerstand heeft geen enkel verband met deze meting",
        ],
        antwoord=0,
        uitleg="Een rechte door de oorsprong betekent een vaste verhouding tussen spanning en stroom. Die verhouding is precies de weerstand.",
    ),
    dict(
        type="waarofniet",
        vraag="Je conclusie mag ook steunen op wat je verwachtte, ook als je metingen iets anders zeggen.",
        antwoord=False,
        uitleg="De gegevens beslissen, niet de verwachting. Wijken ze af, dan ga je op zoek naar de oorzaak of verwerp je je hypothese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je op hoe je een onderzoek hebt uitgevoerd?",
        opties=[
            "zodat iemand anders het kan herhalen en je resultaat kan nakijken",
            "zodat je achteraf je gegevens kan aanpassen als ze niet kloppen",
            "zodat je het materiaal niet meer hoeft op te ruimen na de proef",
            "zodat je conclusie ook geldt voor onderzoeken die je niet deed",
        ],
        antwoord=0,
        uitleg="Herhaalbaarheid is een kern van wetenschap. Wie je werkwijze niet kent, kan je resultaat niet controleren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het stuk van een onderzoek waarin je terugkijkt op je methode en je resultaten?",
        antwoord="reflectie",
        uitleg="Je zegt daar wat goed liep, wat je anders zou doen en hoe betrouwbaar je resultaat is. Daarna communiceer je je besluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil nagaan of plantjes sneller groeien met meer licht. Wat is de beste opzet?",
        opties=[
            "dezelfde plantjes, dezelfde pot en grond, alleen een verschillende lichtduur",
            "verschillende soorten plantjes, elk met een eigen hoeveelheid licht erbij",
            "dezelfde plantjes, maar ook een verschillende hoeveelheid water erbij",
            "dezelfde plantjes samen in één pot, met elke dag een andere lichtduur",
        ],
        antwoord=0,
        uitleg="Alleen de grootheid die je onderzoekt mag verschillen. Verander je er twee, dan weet je achteraf niet welke het verschil maakte.",
    ),
]
