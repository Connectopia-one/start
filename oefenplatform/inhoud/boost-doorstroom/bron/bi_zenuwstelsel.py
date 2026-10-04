# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Van prikkel tot reactie en het zenuwstelsel.

Hoort bij de kop "waarnemen en verwerken van prikkels" van de vakfiche
biologie 2de graad doorstroomfinaliteit. Dat onderdeel weegt 30 % van het
examen en is daarom over vier thema's gespreid: dit thema, het oog, het oor
en de spieren en klieren.

Deel 1 volgt de weg van prikkel naar reactie: receptor, zenuwbaan,
verwerking, effector, en het verschil tussen een bewuste reactie en een
reflex. Deel 2 gaat over de bouw: het centrale en perifere zenuwstelsel, de
delen van de hersenen, en het neuron tot in de details die de fiche opsomt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een prikkel?",
        opties=[
            "een verandering in of rond het lichaam die een reactie kan uitlokken",
            "de beweging van een spier nadat de hersenen een bevel gaven",
            "een boodschapperstof die door een klier in het bloed komt",
            "de kracht waarmee een zenuw tegen een spiervezel aan duwt",
        ],
        antwoord=0,
        uitleg="Een prikkel is de verandering zelf, bijvoorbeeld licht, geluid of warmte. De reactie komt daarna.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de weg van prikkel tot reactie in de juiste orde.",
        opties=[
            "receptor, sensorische zenuw, verwerking, motorische zenuw, effector",
            "effector, motorische zenuw, verwerking, sensorische zenuw, receptor",
            "receptor, motorische zenuw, effector, sensorische zenuw, verwerking",
            "verwerking, receptor, effector, sensorische zenuw, motorische zenuw",
        ],
        antwoord=0,
        uitleg="Een receptor vangt op, een sensorische baan brengt naar binnen, er wordt verwerkt, een motorische baan brengt naar buiten en de effector voert uit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het orgaan of de cel die de reactie uitvoert aan het einde van die weg?",
        antwoord=["effector", "de effector", "effectoren"],
        uitleg="Een effector is wat de opdracht uitvoert. Bij ons zijn dat vooral de spieren en de klieren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze structuren zijn effectoren? Kruis alles aan wat juist is.",
        opties=[
            "een skeletspier in de arm",
            "een zweetklier in de huid",
            "de hartspier",
            "een tastreceptor in de vingertop",
        ],
        antwoord=[0, 1, 2],
        uitleg="Spieren en klieren voeren uit, dus zijn effectoren. Een tastreceptor vangt juist op en staat aan het begin van de weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sensorische zenuw voert prikkels naar het centrale zenuwstelsel toe.",
        antwoord=True,
        uitleg="Sensorisch betekent gevoelig: die banen brengen de boodschap van de receptor naar binnen. Motorische banen gaan de andere richting uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor een reflex?",
        opties=[
            "hij verloopt snel en zonder dat je het eerst beslist",
            "hij verloopt traag omdat de grote hersenen alles overwegen",
            "hij komt alleen voor bij pasgeboren baby's",
            "hij gebeurt enkel in de klieren en nooit in de spieren",
        ],
        antwoord=0,
        uitleg="Bij een reflex schakelt de boodschap al in het ruggemerg of de hersenstam over. Daardoor reageer je nog voor je het beseft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de korte weg die een prikkel bij een reflex aflegt?",
        antwoord=["reflexboog", "de reflexboog", "reflexbogen"],
        uitleg="De reflexboog gaat van receptor naar ruggemerg en meteen weer naar de spier, zonder omweg langs de grote hersenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je raakt een hete pan aan en trekt je hand weg nog voor je de pijn voelt. Hoe verklaar je dat?",
        opties=[
            "het ruggemerg stuurt de spier al aan terwijl de boodschap nog naar de hersenen onderweg is",
            "de hand beweegt op eigen kracht, zonder dat er een zenuw bij te pas komt",
            "de huid trekt zich samen en duwt de hand zo van de pan weg",
            "de pijnreceptoren sturen rechtstreeks een bevel naar de spier zonder zenuwcel",
        ],
        antwoord=0,
        uitleg="De terugtrekreflex gaat via het ruggemerg, en dat is korter. De pijn komt pas aan als je hand al weg is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reflex test een arts met een tikje net onder de knieschijf?",
        opties=[
            "de kniepeesreflex",
            "de pupilreflex",
            "de toeschietreflex",
            "de terugtrekreflex",
        ],
        antwoord=0,
        uitleg="Het tikje rekt de pees uit, en de spier trekt zich meteen samen zodat het onderbeen opveert. Dat is de kniepeesreflex.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de pupilreflex worden je pupillen kleiner als er plots veel licht op valt.",
        antwoord=True,
        uitleg="De pupil vernauwt om het netvlies te beschermen. Dat gebeurt automatisch en aan beide ogen, ook als het licht maar op één oog valt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de toeschietreflex?",
        opties=[
            "de melk begint te vloeien zodra een baby aan de borst zuigt",
            "het ooglid knippert zodra er iets naar het oog toe komt",
            "de maag trekt samen zodra er voedsel in komt",
            "de huid krijgt kippenvel zodra het koud wordt",
        ],
        antwoord=0,
        uitleg="Het zuigen is de prikkel, de melkklier is de effector. De fiche noemt dit als voorbeeld van een reflex waarbij ook een hormoon meespeelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reflex kan je met wat oefening altijd onderdrukken.",
        antwoord=False,
        uitleg="Sommige reflexen, zoals de pupilreflex, blijven buiten je wil. Je kan ze niet afleren, ook niet met oefening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een bewuste reactie en een reflex? Kruis alles aan wat juist is.",
        opties=[
            "een reflex verloopt sneller dan een bewuste reactie",
            "bij een bewuste reactie komen de grote hersenen tussen",
            "een reflex schakelt over in het ruggemerg of de hersenstam",
            "een reflex gebruikt geen zenuwcellen en een bewuste reactie wel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Beide gebruiken zenuwcellen, dat is net het punt. Het verschil zit in waar de boodschap overschakelt en of je erbij nadenkt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een cel of structuur die een prikkel opvangt?",
        antwoord=["receptor", "de receptor", "receptoren"],
        uitleg="Receptoren zijn de ingangen van het zenuwstelsel. Ze staan in de huid, in de ogen, in de oren en in de organen zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een receptor een drempelwaarde?",
        opties=[
            "een te zwakke prikkel levert geen signaal op, zodat het lichaam niet op elk detail reageert",
            "een receptor kan maar één keer per dag een prikkel doorgeven",
            "een receptor moet eerst door een hormoon aangezet worden",
            "een receptor geeft enkel bij warmte een signaal door",
        ],
        antwoord=0,
        uitleg="Pas boven de drempelwaarde ontstaat er een zenuwimpuls. Zo blijft het zenuwstelsel niet aan het werk voor prikkels die niets betekenen.",
    ),
    dict(
        type="waarofniet",
        vraag="Dezelfde prikkel kan bij twee mensen tot een verschillende reactie leiden.",
        antwoord=True,
        uitleg="De verwerking hangt af van ervaring, aandacht en gemoedstoestand. Daarom schrikt de een van een spin en de ander niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke receptoren staan in de huid? Kruis alles aan wat juist is.",
        opties=[
            "tastreceptoren",
            "temperatuurreceptoren",
            "pijnreceptoren",
            "lichtreceptoren",
        ],
        antwoord=[0, 1, 2],
        uitleg="De huid voelt aanraking, warmte en koude, en pijn. Lichtreceptoren zitten in het netvlies van het oog.",
    ),
    dict(
        type="waarofniet",
        vraag="Een receptor in een inwendig orgaan meet enkel prikkels van buiten het lichaam.",
        antwoord=False,
        uitleg="Er zijn ook inwendige receptoren, bijvoorbeeld voor de bloeddruk, het zuurstofgehalte of de rek van de maagwand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hond die bij het rinkelen van zijn voerbak begint te kwijlen, toont wat?",
        opties=[
            "een geleerde reactie op een prikkel die eerst niets betekende",
            "een reflex die de hond al bij de geboorte had",
            "een reactie die volledig door hormonen geregeld wordt",
            "een gedraging die zonder receptor tot stand komt",
        ],
        antwoord=0,
        uitleg="Het geluid is door de ervaring aan voedsel gekoppeld geraakt. De reactie zelf verloopt automatisch, maar de koppeling is geleerd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het signaal dat langs een zenuwcel loopt?",
        antwoord=["zenuwimpuls", "impuls", "de zenuwimpuls"],
        uitleg="De zenuwimpuls is een elektrisch signaal dat langs de celmembraan loopt. Hij heeft altijd dezelfde sterkte; de frequentie zegt hoe sterk de prikkel was.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke delen vormen samen het centrale zenuwstelsel?",
        opties=[
            "de hersenen en het ruggemerg",
            "de hersenen en de zenuwen in de ledematen",
            "het ruggemerg en de zenuwknopen bij de organen",
            "de hersenen, het ruggemerg en alle klieren",
        ],
        antwoord=0,
        uitleg="Alles wat in de schedel en de wervelkolom beschut ligt, vormt het centrale zenuwstelsel. De zenuwen daarbuiten zijn het perifere zenuwstelsel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het deel van het zenuwstelsel dat buiten de hersenen en het ruggemerg ligt?",
        antwoord=["perifeer zenuwstelsel", "het perifere zenuwstelsel", "perifere zenuwstelsel"],
        uitleg="Perifeer betekent aan de buitenkant. Het zijn alle zenuwen en zenuwknopen die het centrale zenuwstelsel met de rest van het lichaam verbinden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen onderscheidt men bij de hersenen? Kruis alles aan wat juist is.",
        opties=[
            "de grote hersenen",
            "de kleine hersenen",
            "de hersenstam",
            "het ruggemerg",
        ],
        antwoord=[0, 1, 2],
        uitleg="Grote hersenen, kleine hersenen en hersenstam liggen in de schedel. Het ruggemerg ligt in de wervelkolom en hoort er dus niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is vooral de taak van de kleine hersenen?",
        opties=[
            "het afstemmen van bewegingen en het bewaren van het evenwicht",
            "het bewaren van herinneringen uit je vroege kindertijd",
            "het regelen van de ademhaling en de hartslag",
            "het opvangen van geluidsprikkels uit het binnenoor",
        ],
        antwoord=0,
        uitleg="De kleine hersenen maken een beweging vloeiend en houden je recht. De ademhaling en hartslag worden in de hersenstam geregeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke levensnoodzakelijke functies regelt de hersenstam?",
        opties=[
            "de ademhaling, de hartslag en de bloeddruk",
            "het lezen, het rekenen en het spreken",
            "het scherpstellen van het oog en het zien van kleur",
            "het aanmaken van rode bloedcellen en bloedplaatjes",
        ],
        antwoord=0,
        uitleg="De hersenstam houdt de basisfuncties aan de praat, ook als je slaapt. Daarom is schade daar zo ernstig.",
    ),
    dict(
        type="waarofniet",
        vraag="In de grote hersenen gebeurt het bewuste denken, het plannen en het leren.",
        antwoord=True,
        uitleg="De schors van de grote hersenen verwerkt wat je waarneemt en koppelt het aan wat je al weet. Daar zit ook de wil om iets te doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke delen onderscheidt de fiche bij een neuron? Kruis alles aan wat juist is.",
        opties=[
            "het cellichaam met de kern",
            "de dendrieten",
            "het axon met zijn eindknopjes",
            "de vacuole",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een neuron heeft een cellichaam, korte dendrieten die opvangen en één lang axon dat doorgeeft. Een vacuole is iets van plantencellen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de korte uitlopers van een neuron die signalen opvangen?",
        antwoord=["dendrieten", "dendriet", "de dendrieten"],
        uitleg="Dendrieten zijn de vertakte uitlopers rond het cellichaam. Zij nemen de signalen van andere cellen aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de myelineschede rond een axon?",
        opties=[
            "ze isoleert het axon zodat de impuls er sneller langs gaat",
            "ze maakt de neurotransmitters aan die het neuron afgeeft",
            "ze vangt de prikkels op die van de huid komen",
            "ze verbindt het neuron met een bloedvat voor de voeding",
        ],
        antwoord=0,
        uitleg="De myelineschede werkt als een isolatielaag. Daardoor springt de impuls van knoop naar knoop en gaat hij veel sneller.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de onderbrekingen in de myelineschede, waar de impuls van de ene naar de volgende springt?",
        antwoord=["knopen van ranvier", "knoop van ranvier", "insnoeringen van ranvier"],
        uitleg="Tussen twee cellen van Schwann ligt telkens een kaal stukje axon. Die knopen van Ranvier laten de impuls sprongsgewijs doorgaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cel maakt de myelineschede rond een axon in het perifere zenuwstelsel?",
        opties=[
            "de cel van Schwann",
            "de witte bloedcel",
            "de sluitcel",
            "de bètacel",
        ],
        antwoord=0,
        uitleg="Cellen van Schwann wikkelen zich als een rolletje rond het axon. Elk zo'n rolletje vormt één stuk van de schede.",
    ),
    dict(
        type="waarofniet",
        vraag="Een neuron heeft meerdere axonen maar slechts één dendriet.",
        antwoord=False,
        uitleg="Het is net omgekeerd: veel dendrieten en één axon. Dat axon kan wel aan het einde in vele eindknopjes uitlopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in een synaps tussen twee neuronen?",
        opties=[
            "het eindknopje geeft een stof af die aan een receptor op de volgende cel bindt",
            "de twee cellen groeien aan elkaar vast zodat er stroom door kan",
            "de impuls springt als een vonk door de lucht tussen de cellen",
            "de twee celkernen wisselen hun erfelijk materiaal uit",
        ],
        antwoord=0,
        uitleg="Er zit een spleet tussen de twee cellen. Het eindknopje lost die op met een boodschapperstof die op de membraanreceptor van de volgende cel past.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de structuur op de celmembraan waar zo'n boodschapperstof precies op past?",
        antwoord=["membraanreceptor", "receptor", "een membraanreceptor"],
        uitleg="De membraanreceptor is als een slot waarop maar één sleutel past. Daardoor werkt een stof enkel op de cellen die er de receptor voor hebben.",
    ),
    dict(
        type="waarofniet",
        vraag="In een synaps gaat het signaal altijd in één richting, van het eindknopje naar de volgende cel.",
        antwoord=True,
        uitleg="Enkel het eindknopje heeft de boodschapperstof en enkel de andere cel heeft de receptoren ervoor. Daarom kan het signaal niet terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke taken heeft het ruggemerg? Kruis alles aan wat juist is.",
        opties=[
            "het geleidt signalen tussen de hersenen en het lichaam",
            "het schakelt reflexen over zonder omweg langs de hersenen",
            "het ligt beschut in de wervelkolom",
            "het maakt de hormonen aan die de groei regelen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het ruggemerg is snelweg en schakelstation in één, beschut door de wervels. Hormonen komen van klieren, niet van het ruggemerg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dwarse breuk in het ruggemerg laat de gevoelens en bewegingen onder die plaats ongemoeid.",
        antwoord=False,
        uitleg="Alle banen naar en van dat gebied lopen door het ruggemerg. Breekt het, dan valt het gevoel en de beweging onder die hoogte weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gaat een impuls langs een gemyeliniseerd axon sneller dan langs een kaal axon?",
        opties=[
            "de impuls springt van knoop tot knoop in plaats van elk stukje membraan te doorlopen",
            "het gemyeliniseerde axon is altijd veel korter dan een kaal axon",
            "de myelineschede duwt de impuls met samentrekkingen vooruit",
            "het gemyeliniseerde axon gebruikt licht in plaats van elektriciteit",
        ],
        antwoord=0,
        uitleg="Enkel bij de knopen van Ranvier wordt de impuls opnieuw opgewekt. Door die sprongen gaat het tientallen keren sneller.",
    ),
    dict(
        type="waarofniet",
        vraag="Het zenuwstelsel werkt sneller dan het hormonale stelsel, maar het effect van een hormoon houdt langer aan.",
        antwoord=True,
        uitleg="Een zenuwimpuls doet er milliseconden over en is meteen voorbij. Een hormoon reist met het bloed en werkt minuten tot dagen door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ziekte tast de myelineschede van zenuwen aan. Welk gevolg verwacht je?",
        opties=[
            "de signalen gaan trager door, waardoor bewegen en voelen moeilijker wordt",
            "de neuronen maken meer dendrieten aan en de reactie wordt sneller",
            "de hersenen nemen de rol van de ontbrekende schede zelf over",
            "er verandert niets, want de impuls loopt even goed langs een kaal axon",
        ],
        antwoord=0,
        uitleg="Zonder isolatie verliest de impuls zijn sprongen en gaat hij veel trager. Dat geeft klachten bij het bewegen, het zien en het voelen.",
    ),
]
