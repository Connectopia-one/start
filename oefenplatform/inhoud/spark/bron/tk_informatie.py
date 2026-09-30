# -*- coding: utf-8 -*-
"""De vragen voor "Informatieverwerkende systemen" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technische systemen —
informatieverwerkend systeem": sensoren en actuatoren, het IPO-model, de
pictogrammen, en de logica in besturing met logische poorten.

Deel 1 gaat over sensoren en actuatoren, over invoer, verwerking en uitvoer met
het IPO-model, en over de pictogrammen die de fiche bij dit systeem zet.
Deel 2 gaat over de EN-, OF- en NIET-poort, de binaire code en de
waarheidstabel.

Een waarheidstabel is niet te tekenen in een vraag zonder afbeelding, dus wordt
er in woorden naar gevraagd: welke uitgang hoort bij welke ingangen. De tabellen
zelf staan in de leerbundel.

De pictogrammen van de fiche zijn hier alleen bruikbaar als je ze in woorden
kunt beschrijven. Daarom geen vragen over een pictogram dat je moet zien, en
geen vraag over het teken met de boogjes: dat lijkt op een gsm zowel op wifi
als op signaalsterkte, en dan raadt een kind naar wat wij bedoelen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat doet een sensor?",
        opties=[
            "Hij meet iets in de omgeving",
            "Hij voert zelf een beweging uit",
            "Hij slaat de gegevens van het systeem op",
            "Hij verdeelt de stroom over de onderdelen",
        ],
        antwoord=0,
        uitleg="Een sensor voelt iets: licht, beweging, druk, geluid. Hij geeft dat door aan de verwerking als een signaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een actuator?",
        opties=[
            "Hij voert iets uit, zoals bewegen of geluid maken",
            "Hij meet hoeveel licht er in de kamer valt",
            "Hij bewaart de gegevens van het hele systeem",
            "Hij verbindt het systeem met het internet",
        ],
        antwoord=0,
        uitleg="Een actuator doet iets in de echte wereld: een lamp die aangaat, een luidspreker die geluid maakt, een motor die draait.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn sensoren?",
        opties=[
            "Een lichtsensor",
            "Een bewegingssensor",
            "Een microfoon",
            "Een luidspreker",
            "Een lamp aan het plafond",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een microfoon voelt geluid, dus is het een sensor. Een luidspreker maakt geluid en een lamp maakt licht: dat zijn actuatoren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn actuatoren?",
        opties=[
            "Een luidspreker",
            "Een lamp",
            "Een zoemer",
            "Een druksensor",
            "Een microfoon",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een actuator voert uit. De druksensor en de microfoon meten juist iets, dus dat zijn sensoren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een microfoon is een actuator.",
        antwoord=False,
        uitleg="Een microfoon vangt geluid op, dus is het een sensor. De luidspreker die het geluid weer uitstuurt, is de actuator.",
    ),
    dict(
        type="invultekst",
        vraag="De drie letters van het IPO-model staan voor input, process en ___.",
        antwoord=["output", "uitvoer"],
        uitleg="Input is de invoer, process de verwerking en output de uitvoer. Elk informatieverwerkend systeem is in die drie stukken te verdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de P in het IPO-model?",
        opties=[
            "Process of verwerking",
            "Product of resultaat",
            "Programma of code",
            "Paneel of scherm",
        ],
        antwoord=0,
        uitleg="De P staat voor process, de verwerking. Dat is het stuk waar de processor of de logische poorten beslissen wat er moet gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk deel van het IPO-model hoort een druktoets?",
        opties=[
            "Bij de invoer",
            "Bij de verwerking",
            "Bij de uitvoer",
            "Bij de voeding",
        ],
        antwoord=0,
        uitleg="Een druktoets is een invoerorgaan: jij geeft er iets mee aan het systeem door. Een lichtsensor is dat ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welk deel van het IPO-model hoort een alarm dat afgaat?",
        opties=[
            "Bij de uitvoer",
            "Bij de invoer",
            "Bij de verwerking",
            "Bij de opslag",
        ],
        antwoord=0,
        uitleg="Het alarm is wat het systeem naar buiten brengt, dus een uitvoerorgaan. Een lamp die aangaat is dat ook.",
    ),
    dict(
        type="waarofniet",
        vraag="Een processor hoort bij de verwerking in het IPO-model.",
        antwoord=True,
        uitleg="De processor en de logische poorten doen het denkwerk. Zij horen bij de P van process.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een straatlamp gaat vanzelf aan zodra het donker wordt. Welke sensor zit erin?",
        opties=[
            "Een lichtsensor",
            "Een druksensor",
            "Een microfoon",
            "Een bewegingssensor",
        ],
        antwoord=0,
        uitleg="De lamp reageert op hoeveel licht er is, dus meet de sensor licht. Op beweging reageert hij niet: hij brandt ook als er niemand voorbijkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="De deur van een winkel gaat open zodra je ervoor komt staan. Welke sensor is dat?",
        opties=[
            "Een bewegingssensor",
            "Een lichtsensor",
            "Een temperatuursensor",
            "Een microfoon",
        ],
        antwoord=0,
        uitleg="De deur reageert op wie eraan komt, dus op beweging. Een temperatuursensor of een microfoon zou hier niets nuttigs meten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sensor zet een verandering in de omgeving om in een signaal voor het systeem.",
        antwoord=True,
        uitleg="Dat is precies zijn taak. Zonder sensor weet een systeem niet wat er buiten gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar plaats je de bewegingssensor van een automatische deur het best?",
        opties=[
            "Boven de deur, gericht naar wie eraan komt",
            "Op de vloer vlak onder de deur zelf",
            "Achteraan in de winkel bij de kassa",
            "Aan de buitenkant van het dak van het gebouw",
        ],
        antwoord=0,
        uitleg="De sensor moet je zien vóór je bij de deur bent, anders gaat die te laat open. Daarom hangt hij hoog en kijkt hij naar buiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram met de wolk betekent dat het toestel bijna leeg is.",
        antwoord=False,
        uitleg="De wolk staat voor opslag in de cloud: je bestanden staan niet op het toestel zelf maar op een server. Hoe vol de batterij is, zegt het batterijpictogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk pictogram op een gsm laat zien hoeveel stroom er nog in het toestel zit?",
        opties=[
            "De batterijstatus",
            "De signaalsterkte",
            "De instellingen",
            "De bluetooth",
        ],
        antwoord=0,
        uitleg="Het batterijpictogram toont de batterijstatus. De signaalsterkte zegt hoe goed je verbinding is, en dat is iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de afkorting www?",
        opties=[
            "World wide web",
            "Wireless web world",
            "Web wide window",
            "World web wire",
        ],
        antwoord=0,
        uitleg="World wide web, het wereldwijde web. Het staat vooraan in heel wat webadressen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke pictogrammen op een toestel gaan over verbinding maken?",
        opties=[
            "Wifi",
            "Bluetooth",
            "USB",
            "De batterijstatus",
            "De instellingen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wifi, bluetooth en USB zijn alle drie manieren om je toestel met iets anders te verbinden. De batterijstatus en de instellingen zeggen iets over het toestel zelf.",
    ),
    dict(
        type="waarofniet",
        vraag="De leeftijdspictogrammen van een spel of een film zeggen vanaf welke leeftijd de inhoud geschikt is.",
        antwoord=True,
        uitleg="Die pictogrammen lopen van alle leeftijden tot vanaf 18 jaar. Ze zeggen niets over hoe moeilijk of hoe lang een spel is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dienen de pictogrammen met geweld, angst of grof taalgebruik op een spel?",
        opties=[
            "Ze zeggen welke inhoud erin zit",
            "Ze zeggen hoe lang je mag spelen",
            "Ze zeggen hoeveel het spel kost",
            "Ze zeggen met hoeveel je kunt spelen",
        ],
        antwoord=0,
        uitleg="Naast de leeftijd staat er met een apart pictogram bij waaróm: geweld, angst, seks, discriminatie, drugs of alcohol, grof taalgebruik.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de binaire code kloppen?",
        opties=[
            "Een 1 betekent aan",
            "Een 0 betekent uit",
            "Er bestaan maar twee waarden",
            "Een 2 betekent half aan",
        ],
        antwoord=[0, 1, 2],
        uitleg="Binair wil zeggen: twee mogelijkheden. Aan of uit, 1 of 0, en niets daartussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer geeft een EN-poort een 1 aan de uitgang?",
        opties=[
            "Als beide ingangen 1 zijn",
            "Als minstens één van de ingangen 1 is",
            "Als de twee ingangen allebei 0 zijn",
            "Als de twee ingangen van elkaar verschillen",
        ],
        antwoord=0,
        uitleg="Bij een EN-poort moet het ene én het andere waar zijn. Is er maar één ingang 1, dan blijft de uitgang 0.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer geeft een OF-poort een 1 aan de uitgang?",
        opties=[
            "Als minstens één ingang 1 is",
            "Alleen als beide ingangen 1 zijn",
            "Alleen als beide ingangen 0 zijn",
            "Alleen als de twee ingangen gelijk zijn",
        ],
        antwoord=0,
        uitleg="Bij een OF-poort volstaat één ingang op 1. Staan ze allebei op 1, dan is de uitgang natuurlijk ook 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een NIET-poort?",
        opties=[
            "Hij keert het signaal om",
            "Hij telt de twee ingangen bij elkaar op",
            "Hij vergelijkt de twee ingangen met elkaar",
            "Hij houdt het signaal een tijdje tegen",
        ],
        antwoord=0,
        uitleg="Een NIET-poort maakt van een 1 een 0 en van een 0 een 1. Hij heeft maar één ingang nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een NIET-poort met een 1 aan de ingang geeft een 0 aan de uitgang.",
        antwoord=True,
        uitleg="Omkeren is zijn enige taak. Ingang 1 wordt uitgang 0, ingang 0 wordt uitgang 1.",
    ),
    dict(
        type="waarofniet",
        vraag="Een EN-poort met de ingangen 1 en 0 geeft een 1 aan de uitgang.",
        antwoord=False,
        uitleg="Bij een EN-poort moeten beide ingangen 1 zijn. Met 1 en 0 blijft de uitgang dus 0.",
    ),
    dict(
        type="waarofniet",
        vraag="Een OF-poort met de ingangen 1 en 0 geeft een 1 aan de uitgang.",
        antwoord=True,
        uitleg="Bij een OF-poort is één ingang op 1 al genoeg.",
    ),
    dict(
        type="invultekst",
        vraag="Het Engelse woord voor een EN-poort is een ___-poort.",
        antwoord=["AND", "and"],
        uitleg="EN is AND, OF is OR en NIET is NOT. Op schema's en in programma's kom je vaak de Engelse namen tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een alarm moet afgaan als het donker is én er beweging is. Welke poort gebruik je?",
        opties=[
            "Een EN-poort",
            "Een OF-poort",
            "Een NIET-poort",
            "Helemaal geen poort",
        ],
        antwoord=0,
        uitleg="Er moet aan twee voorwaarden tegelijk voldaan zijn, en dat is precies wat een EN-poort doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bel moet rinkelen als er op de voordeur óf op de achterdeur gedrukt wordt. Welke poort gebruik je?",
        opties=[
            "Een OF-poort",
            "Een EN-poort",
            "Een NIET-poort",
            "Twee NIET-poorten na elkaar",
        ],
        antwoord=0,
        uitleg="Eén van de twee knoppen is genoeg, dus een OF-poort. Met een EN-poort zou de bel pas rinkelen als er op allebei tegelijk gedrukt wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een waarheidstabel?",
        opties=[
            "Een tabel met alle mogelijke ingangen en de uitgang erbij",
            "Een tabel met de prijs van elk onderdeel van het systeem",
            "Een tabel met de maten die op een werktekening staan",
            "Een tabel met de namen van alle gebruikte componenten",
        ],
        antwoord=0,
        uitleg="In een waarheidstabel zet je elke mogelijke combinatie van ingangen op een rij, met daarnaast wat de uitgang dan doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel rijen heeft de waarheidstabel van een poort met twee ingangen?",
        opties=["Vier", "Twee", "Drie", "Acht"],
        antwoord=0,
        uitleg="De combinaties zijn 0 en 0, 0 en 1, 1 en 0, en 1 en 1. Dat zijn er vier.",
    ),
    dict(
        type="waarofniet",
        vraag="Een logische poort heeft altijd precies één uitgang.",
        antwoord=True,
        uitleg="Een EN-, OF- of NIET-poort heeft één of twee ingangen en altijd één uitgang. Die uitgang is 0 of 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke logische poorten noemt de fiche?",
        opties=[
            "De EN-poort",
            "De OF-poort",
            "De NIET-poort",
            "De PLUS-poort",
            "De MAAL-poort",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alleen die drie, en combinaties ervan. Een PLUS- of MAAL-poort bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lamp moet branden als het niet licht is. Welke poort zet je achter de lichtsensor?",
        opties=[
            "Een NIET-poort",
            "Een EN-poort",
            "Een OF-poort",
            "Twee EN-poorten na elkaar",
        ],
        antwoord=0,
        uitleg="De sensor geeft 1 als het licht is. Je wilt dat de lamp dan juist uit is, dus keer je het signaal om met een NIET-poort.",
    ),
    dict(
        type="waarofniet",
        vraag="Een EN-poort met beide ingangen op 0 geeft een 1 aan de uitgang.",
        antwoord=False,
        uitleg="Met twee nullen blijft de uitgang 0. Een EN-poort geeft alleen een 1 als beide ingangen 1 zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je met een waarheidstabel doen?",
        opties=[
            "De uitgang bepalen bij gegeven ingangen",
            "Zien welke poort er gebruikt is",
            "Alle mogelijke gevallen op een rij zetten",
            "De prijs van het hele systeem berekenen",
            "De kleur van de draden in de kring kiezen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een waarheidstabel gaat alleen over wat er in en uit gaat. Over prijzen en kleuren zegt ze niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de uitgang van een OF-poort als beide ingangen 0 zijn?",
        opties=[
            "Die wordt 0",
            "Die wordt 1",
            "Die blijft op de vorige waarde staan",
            "Die wisselt voortdurend tussen 0 en 1",
        ],
        antwoord=0,
        uitleg="Er is geen enkele ingang op 1, dus is er niets om door te geven. De uitgang blijft 0.",
    ),
    dict(
        type="waarofniet",
        vraag="Een OF-poort geeft alleen een 1 als beide ingangen 1 zijn.",
        antwoord=False,
        uitleg="Dat is de regel van de EN-poort. Bij een OF-poort is één ingang op 1 al voldoende.",
    ),
    dict(
        type="invultekst",
        vraag="Een 0 aan de ingang van een logische poort betekent ___.",
        antwoord="uit",
        uitleg="In de binaire code is 0 uit en 1 aan. Meer waarden bestaan er niet.",
    ),
]
