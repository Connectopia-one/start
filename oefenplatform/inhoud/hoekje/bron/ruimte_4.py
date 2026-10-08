# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — De ruimte, deel 4: vragen van Kim, aangevuld.

Kim stuurde op 8 oktober 2026 tien vragen. Vijf ervan stonden inhoudelijk al
in deel 1 tot 3 (de pulsar, donkere materie, het noorderlicht, de neutronenster
en de Fermi-paradox) en zijn vervangen door nieuwe over hetzelfde vak.
"""

VAK = "De ruimte"
BESTAND = "de-ruimte.json"
TITEL = "Tijd, licht en reizen door de ruimte"
VOLGORDE = 4

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Stel dat je vlak bij de rand van een zwart gat kon blijven hangen en van daar naar een klok op aarde keek. Wat zou je zien?",
        "opties": [
            "Die klok tikt veel sneller dan de jouwe",
            "Die klok tikt veel trager dan de jouwe",
            "Beide klokken lopen precies even snel door",
            "De klok op aarde blijft helemaal stilstaan",
        ],
        "antwoord": 0,
        "uitleg": "Hoe sterker de zwaartekracht, hoe trager de tijd gaat. Vlak bij een zwart gat kruipt jouw tijd dus, en alles daarbuiten lijkt op snelheid te staan: terwijl jij een uur beleeft, gaan op aarde jaren voorbij. Dit is iets anders dan de tweelingparadox, want daar doet de snelheid het werk en hier de zwaartekracht.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom kijkt de ruimtetelescoop James Webb in infrarood en niet in gewoon zichtbaar licht?",
        "opties": [
            "Omdat het licht van de verste sterrenstelsels onderweg is uitgerekt",
            "Omdat infraroodtelescopen veel goedkoper te bouwen zijn dan gewone",
            "Omdat infrarood als enige dwars door de dampkring van de aarde geraakt",
            "Omdat sterren in het begin van het heelal geen zichtbaar licht gaven",
        ],
        "antwoord": 0,
        "uitleg": "Het heelal dijt uit, en lichtgolven die er miljarden jaren door onderweg zijn, worden mee uitgerekt tot infrarood. Wie de allereerste sterrenstelsels wil zien, moet dus in infrarood kijken. Daarom staat Webb ook ver van de aarde en achter een groot zonnescherm: zijn eigen warmte zou het beeld anders overstralen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Sterrenstelsels bewegen van ons weg. Welk verband vonden Lemaître en Hubble tussen hun afstand en hun snelheid?",
        "opties": [
            "Hoe verder weg een stelsel staat, hoe sneller het zich verwijdert",
            "Hoe verder weg een stelsel staat, hoe trager het zich verwijdert",
            "Alle stelsels verwijderen zich met exact dezelfde vaste snelheid",
            "De snelheid hangt niet af van de afstand maar van de massa",
        ],
        "antwoord": 0,
        "uitleg": "Dat is precies wat je verwacht als de ruimte zelf uitdijt: zet stippen op een ballon en blaas hem op, dan lopen verre stippen sneller van elkaar weg dan nabije. De Belgische priester en sterrenkundige Georges Lemaître schreef het in 1927 op, Edwin Hubble mat het twee jaar later na. Sinds 2018 heet de wet officieel naar hen allebei.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is de leefbare zone rond een ster, ook wel de Goldilocks-zone genoemd?",
        "opties": [
            "De afstand waar vloeibaar water op een planeet kan blijven bestaan",
            "De buitenste rand van een stelsel waar geen straling meer binnenkomt",
            "De ring waarin stof en steen samenklonteren tot nieuwe planeten",
            "Het gebied waar de zwaartekracht van de ster precies wordt opgeheven",
        ],
        "antwoord": 0,
        "uitleg": "Te dicht bij de ster verdampt water, te ver weg bevriest het: daartussen ligt een smalle strook waar het precies goed is, zoals de pap van Goudlokje. De aarde zit er netjes in, Venus net te dicht en Mars net te ver. Het is wel een vuistregel, geen garantie: een dikke atmosfeer of een ondergrondse oceaan verschuift het plaatje.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom branden zware reuzensterren hun waterstof veel sneller op dan kleine rode dwergen?",
        "opties": [
            "Door hun massa is de kern zo heet dat de fusie op hol slaat",
            "Omdat ze veel sneller om hun eigen as draaien dan kleine sterren",
            "Omdat ze hun brandstof veel zuiniger en efficiënter kunnen gebruiken",
            "Omdat ze dichter bij andere sterren staan en elkaar opwarmen",
        ],
        "antwoord": 0,
        "uitleg": "Meer massa betekent meer druk en meer hitte in de kern, en de fusiesnelheid stijgt daar razendsnel mee. Een ster van tien zonsmassa's heeft tien keer zoveel brandstof maar verbruikt die duizenden keren sneller: hij leeft een paar miljoen jaar, terwijl een rode dwerg het biljoenen jaren uithoudt. Groot zijn is in de ruimte geen voordeel om oud te worden.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe vinden sterrenkundigen de meeste planeten bij andere sterren, zonder ze ooit te zien?",
        "opties": [
            "Ze meten het sterlicht dat even iets zwakker wordt",
            "Ze maken van heel dichtbij een foto met een grote telescoop",
            "Ze vangen de radiosignalen op die zulke planeten uitzenden",
            "Ze meten hoeveel warmte de planeet zelf de ruimte in straalt",
        ],
        "antwoord": 0,
        "uitleg": "Schuift een planeet voor zijn ster, dan daalt het licht van die ster een fractie van een procent, en dat elke omloop opnieuw. Uit de diepte van die dipjes volgt hoe groot de planeet is, uit hun ritme hoe lang zijn jaar duurt. Zo zijn er intussen duizenden gevonden, bijna geen enkele ooit met het blote oog gezien.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom zweven astronauten in een ruimtestation rond de aarde?",
        "opties": [
            "Omdat ze samen met het station voortdurend vallen",
            "Omdat er op die hoogte vrijwel geen zwaartekracht meer is",
            "Omdat het station zo snel draait dat de zwaartekracht wegvalt",
            "Omdat de lucht in het station lichter is dan de lucht beneden",
        ],
        "antwoord": 0,
        "uitleg": "Op de hoogte van het ISS is de zwaartekracht nog bijna negentig procent van die aan de grond. Het station valt alleen voortdurend naar de aarde toe terwijl het er zo snel naast schiet dat het er altijd naast valt: dat is wat een baan is. Wie meevalt, voelt geen gewicht, net zoals in een lift waarvan de kabel breekt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een ruimtecapsule wordt bij de terugkeer in de dampkring duizenden graden heet. Waardoor komt dat vooral?",
        "opties": [
            "De lucht vóór de capsule wordt samengeperst en daardoor gloeiend heet",
            "De capsule schuurt met hoge snelheid langs de luchtdeeltjes en wrijft warm",
            "De zon schijnt bij de terugkeer recht op de onderkant van de capsule",
            "De remraketten van de capsule blazen hun vuur tegen het hitteschild aan",
        ],
        "antwoord": 0,
        "uitleg": "Niet de wrijving maar de samenpersing doet het werk: de capsule duwt de lucht zo snel opzij dat die geen tijd heeft om weg te stromen, en samengeperste lucht wordt heet, net zoals in een fietspomp. Daarom is een hitteschild bot en breed in plaats van spits: de schokgolf blijft zo een eindje vóór de capsule hangen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent spaghettificatie bij een zwart gat?",
        "opties": [
            "Je voeten worden harder aangetrokken dan je hoofd, dus je rekt uit",
            "Je draait zo snel rond het gat dat je lichaam helemaal opkrult",
            "Het licht om je heen wordt tot lange slierten uiteengetrokken",
            "De tijd rekt zo ver uit dat één seconde eeuwen lijkt te duren",
        ],
        "antwoord": 0,
        "uitleg": "Bij een klein zwart gat verschilt de zwaartekracht tussen je voeten en je hoofd zo sterk dat je als een sliert wordt uitgerekt. Dat is hetzelfde soort getijdenkracht waarmee de maan onze zeeën optilt, maar dan miljarden keren sterker. Bij een reusachtig zwart gat gaat het veel geleidelijker, en zou je de rand in principe heel kunnen passeren.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat gebeurt er met het lichaam van een astronaut die maanden in gewichtloosheid leeft?",
        "opties": [
            "Botten en spieren worden zwakker en het hart wordt wat luier",
            "De botten worden juist steviger omdat ze niets meer te dragen hebben",
            "Het lichaam verandert nauwelijks, zelfs niet na een heel jaar",
            "Alleen het gehoor gaat achteruit door het lawaai van het station",
        ],
        "antwoord": 0,
        "uitleg": "Je lichaam breekt af wat het niet gebruikt, en zonder gewicht gebruikt het zijn botten en beenspieren nauwelijks. Daarom sporten astronauten elke dag twee uur, vastgesnoerd aan een loopband. Ze worden ook een paar centimeter langer omdat hun ruggenwervels uit elkaar zakken, en dat verdwijnt weer na de landing.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom maken wetenschappers zich zorgen over het puin dat rond de aarde cirkelt?",
        "opties": [
            "Elke botsing maakt nieuw puin, dat weer kan botsen",
            "Het puin valt massaal naar beneden en bedreigt de steden",
            "Het puin houdt zoveel zonlicht tegen dat de aarde afkoelt",
            "Het puin trekt met zijn zwaartekracht satellieten uit hun baan",
        ],
        "antwoord": 0,
        "uitleg": "Een verfschilfer van een centimeter gaat daarboven sneller dan een kogel. Botst er iets, dan ontstaan duizenden nieuwe scherven die zelf weer kunnen botsen, een kettingreactie die het Kessler-syndroom heet. In het slechtste geval wordt een hele baan onbruikbaar, en daar hangen net onze weer- en navigatiesatellieten.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Bijna alle planeten draaien in dezelfde richting rond de zon, en bijna allemaal in hetzelfde vlak. Hoe komt dat?",
        "opties": [
            "Ze zijn ontstaan uit één draaiende schijf gas en stof",
            "De zon trekt ze met haar magneetveld in het gelid",
            "Planeten die de andere kant op draaiden, zijn op de zon gevallen",
            "Ze duwen elkaar met hun zwaartekracht langzaam in dezelfde richting",
        ],
        "antwoord": 0,
        "uitleg": "Een wolk die inkrimpt, gaat sneller draaien en plat uit tot een schijf, net zoals pizzadeeg dat je rondslingert. In die schijf klonterden de planeten samen, dus erfden ze allemaal dezelfde draairichting. Venus en Uranus zijn de uitzonderingen, waarschijnlijk door een flinke botsing in hun jonge jaren.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een zonnezeil heeft geen motor en geen brandstof. Waardoor beweegt het dan?",
        "opties": [
            "Lichtdeeltjes van de zon duwen tegen het zeil",
            "De warmte van de zon blaast lucht achter het zeil weg",
            "Het magneetveld van de zon trekt aan het metaal van het zeil",
            "Een elektrische lading in het zeil stoot de zon van zich af",
        ],
        "antwoord": 0,
        "uitleg": "Licht heeft geen massa maar wel een duwtje in zich, en dat duwtje is piepklein: op een zeil zo groot als een voetbalveld staat ongeveer het gewicht van een paperclip. Maar het stopt nooit, dus een zonnezeil blijft versnellen en kan uiteindelijk sneller gaan dan een raket. In 2019 vloog LightSail 2 er echt mee.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Er vliegen elke seconde miljarden neutrino's door je lichaam. Waarom merk je daar niets van?",
        "opties": [
            "Ze botsen bijna nooit ergens tegen",
            "Ze zijn zo traag dat ze geen kracht kunnen zetten",
            "Ze blijven netjes buiten de atomen van je lichaam hangen",
            "Je huid houdt ze tegen, net zoals ze uv-licht tegenhoudt",
        ],
        "antwoord": 0,
        "uitleg": "Een neutrino voelt de elektrische kracht niet en gaat dus dwars door de lege ruimte in atomen. Je zou een muur lood van een lichtjaar dik nodig hebben om de helft tegen te houden. Om er toch eentje te vangen, bouwen natuurkundigen enorme tanks diep onder de grond en wachten ze op het zeldzame flitsje.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een zwart gat zuigt alles naar zich toe, ook een planeet die er in een rustige baan omheen draait.",
        "antwoord": False,
        "uitleg": "Een zwart gat is geen stofzuiger. Op afstand werkt zijn zwaartekracht precies zoals die van een gewone ster met dezelfde massa. Zou je de zon vervangen door een zwart gat van één zonsmassa, dan bleef de aarde rustig haar rondje draaien, het zou alleen donker en koud worden.",
    },
    {
        "type": "waarofniet",
        "vraag": "Op Mars weegt een steen ongeveer een derde van wat hij op aarde weegt.",
        "antwoord": True,
        "uitleg": "De zwaartekracht op Mars is 0,38 keer die op aarde, dus ongeveer een derde. Een astronaut van zestig kilo zou er nog geen vijfentwintig wegen. Op de maan is het nog minder, een zesde, en op Jupiter zou je er meer dan het dubbele wegen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een ruimtepak is vooral gemaakt om de astronaut warm te houden, want in de ruimte is het altijd ijskoud.",
        "antwoord": False,
        "uitleg": "Het grootste probleem is net oververhitting. In het zonlicht loopt de buitenkant van een pak ver boven honderd graden op, en de warmte die de astronaut zelf maakt, kan nergens heen: er is geen lucht om ze aan af te geven. Daarom loopt er koelwater door een onderpak met honderd meter dunne buisjes.",
    },
    {
        "type": "waarofniet",
        "vraag": "De Apollo-vluchten brachten samen honderden kilo's maansteen mee terug naar de aarde.",
        "antwoord": True,
        "uitleg": "Zes landingen leverden samen 382 kilo steen en stof op. Een deel ligt nog altijd ongeopend te wachten op betere meetapparatuur dan die van toen: in 2022 werd een buis uit 1972 voor het eerst opengemaakt. Juist die stenen verraadden dat de maan uit de aarde zelf is ontstaan.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoe heet de ruimtesonde die in 1977 vertrok en als eerste van alle mensenwerk de ruimte tussen de sterren bereikte? (één woord)",
        "antwoord": "Voyager",
        "uitleg": "Voyager 1 passeerde in 2012 de rand van de invloedssfeer van onze zon en vliegt nu door de interstellaire ruimte, meer dan twintig miljard kilometer ver. Aan boord hangt een gouden plaat met muziek, geluiden en groeten in vijfenvijftig talen, voor het geval iemand hem ooit vindt.",
    },
    {
        "type": "invultekst",
        "vraag": "De maan staat op ongeveer 384 000 km van ons. Licht legt 300 000 km per seconde af. Hoeveel seconden doet het maanlicht erover om bij ons te komen? Rond af op één cijfer na de komma.",
        "antwoord": "1,3",
        "uitleg": "384 000 gedeeld door 300 000 is 1,28, afgerond 1,3 seconde. Daarom duurde het bij de maanlandingen telkens bijna drie seconden voor er antwoord kwam: heen en terug. Bij Mars loopt dat op tot soms twintig minuten per richting, en daarom kan niemand een marsrobot met een joystick besturen.",
    },
]
