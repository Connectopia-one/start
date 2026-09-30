# -*- coding: utf-8 -*-
"""De vragen voor "Energie in een technisch systeem" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technische systemen —
energiesysteem", de twee stukken vóór de stroomkring: energieomzettingen met
nuttige en niet-nuttige energie, en fossiele brandstoffen tegenover
hernieuwbare energie.

Deel 1 gaat over de energievormen van de fiche (bewegings- of kinetische,
chemische, elektrische, potentiële, stralings- en warmte- of thermische
energie), over de omzetting in een technisch systeem en over wat daarvan de
nuttige en de niet-nuttige energie is.
Deel 2 gaat over fossiele brandstoffen en hernieuwbare energie, en over waarom
het verbranden van fossiele brandstoffen het klimaat verandert.

Twee dingen worden hier bewust juist gezet. Een technisch systeem maakt nooit
energie bij: het zet energie om. En het broeikaseffect zelf bestond er al
lang voor de mens: het probleem is dat wij het versterken.

De stroomkring, de grootheden en de eenheden staan niet hier maar in hun eigen
hoofdstukken, anders zouden dezelfde vragen twee keer voorkomen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke energievorm heeft een fietser die snel rijdt?",
        opties=[
            "Bewegingsenergie",
            "Chemische energie",
            "Stralingsenergie",
            "Potentiële energie",
        ],
        antwoord=0,
        uitleg="Alles wat beweegt heeft bewegingsenergie. Hoe sneller en hoe zwaarder, hoe meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ander woord voor bewegingsenergie is ...",
        opties=[
            "Kinetische energie",
            "Thermische energie",
            "Potentiële energie",
            "Elektrische energie",
        ],
        antwoord=0,
        uitleg="Kinetisch komt van het Griekse woord voor beweging. Thermische energie is warmte, dat is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Warmte is een energievorm.",
        antwoord=True,
        uitleg="Warmte of thermische energie staat in de fiche gewoon in het rijtje energievormen, naast beweging, licht, elektriciteit en chemische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzetting gebeurt er in een gloeilamp?",
        opties=[
            "Elektrische energie wordt licht en warmte",
            "Chemische energie wordt beweging",
            "Bewegingsenergie wordt elektrische energie",
            "Stralingsenergie wordt chemische energie",
        ],
        antwoord=0,
        uitleg="Er gaat elektriciteit in, en er komt licht en warmte uit. Het licht is wat je wilt, de warmte krijg je erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze energievormen noemt de vakfiche?",
        opties=[
            "Chemische energie",
            "Potentiële energie",
            "Stralingsenergie",
            "Digitale energie",
            "Statische energie",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt bewegings- of kinetische energie, chemische energie, elektrische energie, potentiële energie, stralingsenergie zoals licht, en warmte of thermische energie. Digitale en statische energie bestaan niet als energievorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een energieomzetting komt er meestal ook energie vrij die je niet kunt gebruiken.",
        antwoord=True,
        uitleg="Dat is de niet-nuttige energie. Meestal is dat warmte, en soms geluid of trilling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de niet-nuttige energie van een gloeilamp?",
        opties=[
            "De warmte",
            "Het licht",
            "De elektrische stroom",
            "De chemische energie",
        ],
        antwoord=0,
        uitleg="Je hangt een lamp op om licht te hebben, niet om te verwarmen. Alles wat als warmte weggaat, is dus niet-nuttige energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de nuttige energie van een elektrische boormachine?",
        opties=[
            "De bewegingsenergie van de boor",
            "De warmte die de motor afgeeft",
            "Het geluid dat de machine maakt",
            "De trilling die je in je handen voelt",
        ],
        antwoord=0,
        uitleg="Je koopt een boormachine om te boren, dus de draaiende beweging is de nuttige energie. Warmte, geluid en trilling krijg je erbij.",
    ),
    dict(
        type="invultekst",
        vraag="Energie die bij een omzetting vrijkomt maar die je niet kunt gebruiken, noemen we ___ energie.",
        antwoord=["niet-nuttige", "niet nuttige"],
        uitleg="De fiche zet nuttige en niet-nuttige energie tegenover elkaar. Bij bijna elk technisch systeem is de niet-nuttige energie warmte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een zonnepaneel kloppen?",
        opties=[
            "Het zet stralingsenergie om in elektrische energie",
            "Het werkt op het licht van de zon",
            "Het levert minder als het bewolkt is",
            "Het maakt zelf de energie die het levert",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een zonnepaneel maakt geen energie bij: het zet de energie van het zonlicht om in stroom. Minder licht betekent dus minder stroom.",
    ),
    dict(
        type="waarofniet",
        vraag="In een batterij zit chemische energie opgeslagen.",
        antwoord=True,
        uitleg="Een batterij bewaart chemische energie en zet die bij gebruik om in elektrische energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een steen die boven op een kast ligt, heeft ...",
        opties=[
            "Potentiële energie",
            "Bewegingsenergie",
            "Stralingsenergie",
            "Chemische energie",
        ],
        antwoord=0,
        uitleg="Potentiële energie is de energie van de plaats waar iets ligt. Valt de steen, dan wordt die potentiële energie bewegingsenergie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een elektrische waterkoker kloppen?",
        opties=[
            "Hij zet elektrische energie om in warmte",
            "Er komt ook wat geluid vrij",
            "De warmte is hier de nuttige energie",
            "Het licht van het controlelampje is de nuttige energie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij een waterkoker is warmte precies wat je wilt, dus is warmte hier de nuttige energie. Bij een lamp is dat net omgekeerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Het licht van een leeslamp is de niet-nuttige energie.",
        antwoord=False,
        uitleg="Bij een lamp is het licht net wél wat je wilt. De warmte is daar de niet-nuttige energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energieomzetting gebeurt er in een windmolen?",
        opties=[
            "Bewegingsenergie wordt elektrische energie",
            "Chemische energie wordt warmte en geluid",
            "Stralingsenergie wordt beweging en warmte",
            "Elektrische energie wordt licht en geluid",
        ],
        antwoord=0,
        uitleg="De wind laat de wieken draaien, en de generator maakt van die beweging stroom.",
    ),
    dict(
        type="waarofniet",
        vraag="Een elektrische motor zet bewegingsenergie om in elektrische energie.",
        antwoord=False,
        uitleg="Dat doet een generator. Een motor werkt net andersom: er gaat elektrische energie in en er komt beweging uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een gsm warm terwijl hij oplaadt?",
        opties=[
            "Een deel van de energie wordt warmte in plaats van lading",
            "De batterij zet warmte om in stroom",
            "Er is warmte nodig om een batterij te kunnen vullen",
            "De lader maakt met opzet warmte om de batterij te drogen",
        ],
        antwoord=0,
        uitleg="Bij elke omzetting gaat er een stuk als warmte weg. Die warmte is hier de niet-nuttige energie.",
    ),
    dict(
        type="invultekst",
        vraag="De energie die opgeslagen zit in steenkool, aardgas en in voedsel heet ___ energie.",
        antwoord="chemische",
        uitleg="Chemische energie zit vast in de stof zelf. Ze komt vrij als de stof verbrandt of verteert.",
    ),
    dict(
        type="meerkeuze",
        vraag="In de verbrandingsmotor van een auto wordt ...",
        opties=[
            "Chemische energie omgezet in beweging en warmte",
            "Elektrische energie omgezet in licht",
            "Stralingsenergie omgezet in chemische energie",
            "Potentiële energie omgezet in geluid en trilling",
        ],
        antwoord=0,
        uitleg="De brandstof bevat chemische energie. Bij het verbranden komt die vrij als beweging, en voor een groot stuk ook als warmte die de motor moet wegkoelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een technisch systeem kan energie uit het niets maken.",
        antwoord=False,
        uitleg="Een technisch systeem zet energie om van de ene vorm in de andere. Er komt nooit energie bij.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn fossiele brandstoffen?",
        opties=["Steenkool", "Aardgas", "Aardolie", "Wind", "Waterkracht"],
        antwoord=[0, 1, 2],
        uitleg="Fossiele brandstoffen zijn miljoenen jaren geleden in de grond ontstaan uit resten van planten en dieren. Wind en waterkracht zijn hernieuwbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent hernieuwbare energie?",
        opties=[
            "De bron raakt niet op",
            "De bron is altijd goedkoper dan een andere bron",
            "De energie kan alleen in de zomermaanden gebruikt worden",
            "De energie komt altijd uit een ander land dan het onze",
        ],
        antwoord=0,
        uitleg="De zon blijft schijnen, de wind blijft waaien en het water blijft stromen. Daarom heet die energie hernieuwbaar of duurzaam.",
    ),
    dict(
        type="waarofniet",
        vraag="Wind raakt op als je er te veel stroom mee maakt.",
        antwoord=False,
        uitleg="Wind is een hernieuwbare bron: die vult zichzelf aan. Bij steenkool of aardolie is dat wel zo, want daarvan zit er maar een bepaalde hoeveelheid in de grond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bron is géén hernieuwbare energiebron?",
        opties=["Steenkool", "De zon", "De wind", "Aardwarmte"],
        antwoord=0,
        uitleg="De fiche noemt de zon, de wind, het water en aardwarmte als hernieuwbare bronnen. Steenkool is een fossiele brandstof.",
    ),
    dict(
        type="waarofniet",
        vraag="Steenkool en aardgas ontstaan op een paar jaar tijd, dus ze raken nooit op.",
        antwoord=False,
        uitleg="Ze zijn over miljoenen jaren ontstaan. Wat wij nu opstoken, groeit dus niet opnieuw aan binnen een mensenleven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zorgt het verbranden van fossiele brandstoffen voor klimaatverandering?",
        opties=[
            "Er komt CO2 vrij, en dat is een broeikasgas",
            "Er komt zuurstof vrij die de lucht opwarmt",
            "Er komt water vrij dat de zeespiegel doet stijgen",
            "Er komt stof vrij dat het zonlicht tegenhoudt",
        ],
        antwoord=0,
        uitleg="Broeikasgassen houden warmte vast in de dampkring. Hoe meer CO2 wij erbij stoken, hoe sterker dat effect wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Het belangrijkste broeikasgas dat vrijkomt bij het verbranden van fossiele brandstoffen is ___.",
        antwoord=["CO2", "koolstofdioxide"],
        uitleg="CO2 of koolstofdioxide komt vrij bij elke verbranding van steenkool, aardgas, benzine of stookolie.",
    ),
    dict(
        type="waarofniet",
        vraag="CO2 is een broeikasgas.",
        antwoord=True,
        uitleg="CO2 houdt warmte vast in de dampkring. Dat is precies wat een broeikasgas doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bronnen noemt de fiche hernieuwbaar?",
        opties=["De zon", "De wind", "Het water", "Aardwarmte", "Steenkool"],
        antwoord=[0, 1, 2, 3],
        uitleg="Die vier staan letterlijk in de fiche. Steenkool hoort bij de fossiele brandstoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is aardwarmte?",
        opties=[
            "Warmte uit de diepe ondergrond",
            "Warmte van de zon op een dak",
            "Warmte van een houtkachel in huis",
            "Warmte die vrijkomt bij het verbranden van gas",
        ],
        antwoord=0,
        uitleg="Diep in de aarde is het warm. Die warmte haal je naar boven met buizen en pompen, en ze raakt niet op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zonnepaneel werkt op fossiele brandstof.",
        antwoord=False,
        uitleg="Een zonnepaneel werkt op het licht van de zon, en dat is een hernieuwbare bron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemen we hernieuwbare energie ook duurzame energie?",
        opties=[
            "Omdat de bron ook voor de volgende generaties blijft bestaan",
            "Omdat de installatie altijd honderd jaar lang blijft werken",
            "Omdat het altijd de goedkoopste manier van werken is",
            "Omdat er geen enkel toestel voor nodig is",
        ],
        antwoord=0,
        uitleg="Duurzaam betekent dat je iets kunt blijven doen zonder de aarde uit te putten. Het gaat over de bron, niet over de levensduur van het toestel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een waterkrachtcentrale zet ...",
        opties=[
            "De beweging van water om in elektrische energie",
            "Chemische energie om in stromend water en damp",
            "Warmte om in stromend water en waterdamp",
            "Licht om in bewegingsenergie en in geluid",
        ],
        antwoord=0,
        uitleg="Het stromende water laat een turbine draaien, en de generator maakt daar stroom van. Dezelfde omzetting als bij een windmolen, maar dan met water.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het opwekken van stroom met een windmolen komt er geen CO2 vrij.",
        antwoord=True,
        uitleg="Er wordt niets verbrand, dus er komt bij het draaien geen CO2 vrij. Dat is het grote voordeel van wind en zon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nadeel van energie uit wind en zon?",
        opties=[
            "Ze leveren niet altijd evenveel",
            "Ze zijn schadelijk voor de lucht",
            "Ze raken na een jaar of tien op",
            "Ze werken uitsluitend in de nacht",
        ],
        antwoord=0,
        uitleg="Zonder wind draait de molen niet, en 's nachts levert een zonnepaneel niets. Daarom is opslag in batterijen zo belangrijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Aardolie is een hernieuwbare energiebron.",
        antwoord=False,
        uitleg="Aardolie is een fossiele brandstof. Ze is miljoenen jaren oud en groeit niet aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke brandstof komt uit de grond en is miljoenen jaren oud?",
        opties=[
            "Steenkool",
            "Waterstof uit een fabriek",
            "Hout uit een beheerd bos",
            "Stroom uit een zonnepaneel op het dak",
        ],
        antwoord=0,
        uitleg="Steenkool is ontstaan uit plantenresten die miljoenen jaren onder de grond samengedrukt zijn. Daarom heet het een fossiele brandstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je zelf doen om minder fossiele brandstof te gebruiken?",
        opties=[
            "Met de fiets gaan in plaats van met de auto",
            "De verwarming een graad lager zetten",
            "Het licht uitdoen als je een kamer verlaat",
            "Elke dag een halfvolle wasmachine op negentig graden draaien",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat minder brandstof of minder stroom vraagt, helpt. Een halfvolle was op negentig graden doet net het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Het broeikaseffect bestond al voor de mens fossiele brandstoffen begon te gebruiken.",
        antwoord=True,
        uitleg="Het broeikaseffect is natuurlijk en zelfs nodig: zonder dat effect zou het op aarde veel te koud zijn. Het probleem is dat wij het versterken.",
    ),
    dict(
        type="invultekst",
        vraag="Energie uit bronnen die niet opraken, zoals de zon en de wind, noemen we ___ energie.",
        antwoord=["hernieuwbare", "duurzame"],
        uitleg="Hernieuwbaar en duurzaam worden in de fiche door elkaar gebruikt voor energie uit de zon, wind, water en aardwarmte.",
    ),
]
