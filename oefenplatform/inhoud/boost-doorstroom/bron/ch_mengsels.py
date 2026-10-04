# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Mengsels, zuivere stoffen en scheidingstechnieken.

Hoort bij "opbouw van materie" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_stoffen]. Samen 10 % van het examen.

Deel 1 gaat over het onderscheid tussen een mengsel en een zuivere stof, de
soorten mengsels die de fiche opsomt, de aggregatietoestanden en de
stofeigenschappen. Deel 2 gaat over het kiezen van een scheidingstechniek en
het benoemen van haar onderdelen, en over het kooktraject en het smelttraject
van een mengsel.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een zuivere stof en een mengsel?",
        opties=[
            "een zuivere stof bestaat uit één soort deeltje",
            "een zuivere stof is altijd vloeibaar bij kamertemperatuur",
            "een zuivere stof komt enkel in een laboratorium voor",
            "een zuivere stof heeft geen massadichtheid",
        ],
        antwoord=0,
        uitleg="Een zuivere stof bestaat uit één soort molecule of formule-eenheid. Een mengsel bevat meerdere bestanddelen die je er in principe weer uit kan halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke mengsels zijn homogeen? Kruis alles aan wat juist is.",
        opties=[
            "keukenzout opgelost in water",
            "brons, een legering van koper en tin",
            "zand in water",
            "een slaatje met olie en azijn",
        ],
        antwoord=[0, 1],
        uitleg="In een homogeen mengsel zie je de bestanddelen niet meer afzonderlijk, ook niet met een microscoop. Een oplossing en een legering zijn homogeen; zand in water en olie met azijn zijn heterogeen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Rook bestaat uit vaste deeltjes die in een gas zweven. Welk soort mengsel is dat?",
        opties=[
            "een aerosol",
            "een emulsie",
            "een suspensie",
            "een legering",
        ],
        antwoord=0,
        uitleg="Een aerosol is een mengsel van een vloeistof of een vaste stof in een gas. Rook is de vaste variant, nevel de vloeibare.",
    ),
    dict(
        type="meerkeuze",
        vraag="Mayonaise bestaat uit olie en water die fijn verdeeld door elkaar zitten. Hoe noem je zo'n mengsel?",
        opties=[
            "een emulsie",
            "een schuim",
            "een aerosol",
            "een oplossing",
        ],
        antwoord=0,
        uitleg="Een emulsie is een mengsel van twee vloeistoffen die normaal niet mengen. Bij mayonaise houdt de dooier de druppeltjes verdeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke mengsels zijn een schuim? Kruis alles aan wat juist is.",
        opties=[
            "slagroom",
            "badschuim",
            "messing",
            "mist boven een weide",
        ],
        antwoord=[0, 1],
        uitleg="In een schuim zit een gas verdeeld in een vloeistof of in een vaste stof. Messing is een legering en mist is een aerosol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een glas vruchtensap met pulp die langzaam naar de bodem zakt, is welk soort mengsel?",
        opties=[
            "een suspensie",
            "een oplossing",
            "een legering",
            "een nevel",
        ],
        antwoord=0,
        uitleg="Bij een suspensie zweven vaste deeltjes in een vloeistof zonder op te lossen. Ze zakken na een tijd naar de bodem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen zijn stofeigenschappen? Kruis alles aan wat juist is.",
        opties=[
            "het kookpunt",
            "de massadichtheid",
            "de massa van het staal",
            "het volume van het staal",
        ],
        antwoord=[0, 1],
        uitleg="Een stofeigenschap hangt niet af van hoeveel je ervan hebt. Massa en volume veranderen wel met de hoeveelheid, dus die zeggen niets over welke stof het is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie aggregatietoestanden onderscheidt de chemie?",
        opties=[
            "vast, vloeibaar en gas",
            "hard, zacht en vloeiend",
            "zuiver, gemengd en opgelost",
            "koud, lauw en warm",
        ],
        antwoord=0,
        uitleg="De aggregatietoestand zegt hoe de deeltjes ten opzichte van elkaar liggen en bewegen. Bij vast liggen ze vast, bij gas bewegen ze vrij door de ruimte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor is de massadichtheid van een stof de verhouding?",
        opties=[
            "de massa per volume",
            "het volume per massa",
            "de massa per mol",
            "het gewicht per oppervlakte",
        ],
        antwoord=0,
        uitleg="De massadichtheid is de massa gedeeld door het volume, bijvoorbeeld in kg/m³ of in g/L. Daarom zinkt een stof met een grotere massadichtheid in water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee stoffen zien er allebei uit als een wit poeder. Welke eigenschap gebruik je om ze te onderscheiden?",
        opties=[
            "het smeltpunt",
            "de kleur",
            "de massa van het staal",
            "de kleur van het potje",
        ],
        antwoord=0,
        uitleg="Het smeltpunt is voor elke zuivere stof een vast getal. De kleur is hier bij beide dezelfde en helpt dus niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de oplosbaarheid van een stof?",
        opties=[
            "hoeveel ervan in een bepaald volume oplosmiddel oplost",
            "hoe snel de stof uit elkaar valt in de lucht",
            "bij welke temperatuur de stof begint te koken",
            "hoeveel massa één mol van de stof heeft",
        ],
        antwoord=0,
        uitleg="De oplosbaarheid zegt hoeveel van een stof maximaal in een bepaalde hoeveelheid oplosmiddel gaat, bij een bepaalde temperatuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een molecule is een deeltje dat uit meerdere atomen bestaat.",
        antwoord=True,
        uitleg="Een molecule is een groepje atomen dat met atoombindingen aan elkaar hangt, zoals H₂O of O₂.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk mengsel bestaat uit minstens twee bestanddelen.",
        antwoord=True,
        uitleg="Precies daarom is het een mengsel. Met één bestanddeel heb je een zuivere stof.",
    ),
    dict(
        type="waarofniet",
        vraag="Een legering is een heterogeen mengsel van metalen.",
        antwoord=False,
        uitleg="Een legering is homogeen: je ziet de verschillende metalen niet meer afzonderlijk. Brons en messing zijn voorbeelden.",
    ),
    dict(
        type="waarofniet",
        vraag="Melk is een heldere oplossing.",
        antwoord=False,
        uitleg="Melk is wit en troebel omdat er vetbolletjes in het water zweven. Het is een emulsie, geen oplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="De geleidbaarheid van een stof hangt af van hoeveel je ervan hebt.",
        antwoord=False,
        uitleg="Geleidbaarheid is een stofeigenschap: ze hangt van de stof zelf af. Massa en volume veranderen wel met de hoeveelheid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een mengsel waarin je de bestanddelen nog afzonderlijk kan zien?",
        antwoord=["heterogeen", "een heterogeen mengsel", "heterogeen mengsel"],
        uitleg="Bij een heterogeen mengsel zie je de verschillende delen nog, zoals zand in water of olie op azijn.",
    ),
    dict(
        type="invultekst",
        vraag="Vul aan: nevel bestaat uit vloeibare druppeltjes die zweven in een ___.",
        antwoord=["gas", "een gas"],
        uitleg="Nevel is de vloeibare soort aerosol: fijne druppeltjes in een gas, zoals mist in de lucht.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stofeigenschap gebruikt actieve kool om kleurstoffen uit water te halen?",
        antwoord=["adsorptievermogen", "het adsorptievermogen", "aanhechtingsvermogen"],
        uitleg="Actieve kool heeft een enorm oppervlak waaraan deeltjes zich vasthechten. Dat vermogen heet adsorptie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de temperatuur waarbij een zuivere vaste stof vloeibaar wordt?",
        antwoord=["smeltpunt", "het smeltpunt"],
        uitleg="Bij het smeltpunt gaat een zuivere stof van vast naar vloeibaar, bij een vaste temperatuur.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke technieken kan je gebruiken om zand uit water te halen? Kruis alles aan wat juist is.",
        opties=[
            "filtreren",
            "decanteren",
            "destilleren",
            "chromatografie",
        ],
        antwoord=[0, 1],
        uitleg="Het zand is grover dan de poriën van een filter, dus houdt het filter het tegen. Het zakt ook naar de bodem, dus kan je het water eraf gieten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil zuiver water uit zeewater halen. Welke techniek kies je?",
        opties=[
            "destilleren",
            "filtreren",
            "zeven",
            "decanteren",
        ],
        antwoord=0,
        uitleg="Het zout zit opgelost, dus een filter houdt het niet tegen. Water en zout hebben wel een heel verschillend kookpunt, dus kook je het water weg en vang je het weer op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil het keukenzout overhouden uit pekel. Welke technieken kan je gebruiken? Kruis alles aan wat juist is.",
        opties=[
            "indampen",
            "kristalliseren",
            "filtreren",
            "zeven",
        ],
        antwoord=[0, 1],
        uitleg="Bij indampen en kristalliseren laat je het water weggaan en blijft het zout achter. Een filter of een zeef houdt opgeloste stoffen niet tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Olie en water zitten in één fles, gescheiden in twee lagen. Welke techniek kies je?",
        opties=[
            "decanteren",
            "destilleren",
            "indampen",
            "chromatografie",
        ],
        antwoord=0,
        uitleg="Bij decanteren laat je de lagen van elkaar lopen, met een scheitrechter. Dat kan omdat de vloeistoffen niet mengen en een verschillende massadichtheid hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke techniek gebruikt een draaiende beweging om zware deeltjes sneller te laten zakken?",
        opties=[
            "centrifugeren",
            "filtreren",
            "extraheren",
            "destilleren",
        ],
        antwoord=0,
        uitleg="Bij centrifugeren wordt het mengsel snel rondgedraaid. De deeltjes met de grootste massadichtheid gaan naar buiten en zakken dus veel sneller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil de kleurstoffen in een stift van elkaar scheiden. Welke techniek kies je?",
        opties=[
            "chromatografie",
            "zeven",
            "centrifugeren",
            "decanteren",
        ],
        antwoord=0,
        uitleg="Bij chromatografie loopt een oplosmiddel over papier mee. Elke kleurstof hecht anders aan het papier en komt dus op een andere hoogte terecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil cafeïne uit koffiebonen halen met een geschikt oplosmiddel. Welke techniek is dat?",
        opties=[
            "extraheren",
            "indampen",
            "zeven",
            "decanteren",
        ],
        antwoord=0,
        uitleg="Bij extraheren kiest men een oplosmiddel waarin alleen de gewenste stof goed oplost. De rest blijft achter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noem je bij het filtreren de vloeistof die door het filter gaat?",
        opties=[
            "het filtraat",
            "het residu",
            "het destillaat",
            "het extract",
        ],
        antwoord=0,
        uitleg="Het filtraat is wat erdoor gaat, het residu is wat op het filter achterblijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een zuivere stof zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze heeft een vast kookpunt",
            "ze heeft een vast smeltpunt",
            "ze heeft een kooktraject",
            "ze heeft altijd twee bestanddelen",
        ],
        antwoord=[0, 1],
        uitleg="Een zuivere stof kookt en smelt bij één temperatuur. Een traject, dus een gebied van temperaturen, hoort juist bij een mengsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is bij een mengsel sprake van een kooktraject en niet van een kookpunt?",
        opties=[
            "de samenstelling verandert terwijl het kookt",
            "een mengsel kookt altijd onder de 100 graden",
            "de thermometer wordt onnauwkeurig in een mengsel",
            "een mengsel kan niet koken",
        ],
        antwoord=0,
        uitleg="Het bestanddeel met het laagste kookpunt gaat er eerst uit. Daardoor verandert het mengsel en stijgt de temperatuur verder: je krijgt een gebied in plaats van één punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk toestel gebruik je om twee vloeistoflagen gecontroleerd van elkaar te laten lopen?",
        opties=[
            "een scheitrechter",
            "een maatkolf",
            "een erlenmeyer",
            "een horlogeglas",
        ],
        antwoord=0,
        uitleg="Een scheitrechter heeft onderaan een kraantje, dus kan je de onderste laag eruit laten lopen en op tijd stoppen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij destilleren koelt de damp in een liebigkoeler weer af tot vloeistof.",
        antwoord=True,
        uitleg="De damp gaat door een koeler met koud water errond en condenseert daar. Het druppelt dan in het opvangvat als destillaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Zeven en filtreren werken allebei op een verschil in kookpunt.",
        antwoord=False,
        uitleg="Ze werken op een verschil in deeltjesgrootte: een opening houdt de grote deeltjes tegen. Het kookpunt gebruikt men bij destilleren.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan een oplossing van zout in water filtreren om het zout eruit te halen.",
        antwoord=False,
        uitleg="Opgeloste ionen zijn veel kleiner dan de poriën van een filter en gaan er zonder meer door. Je moet het water laten verdampen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het filtreren noemt men het residu de vloeistof die door het filter loopt.",
        antwoord=False,
        uitleg="Het is net andersom: het residu blijft op het filter liggen en het filtraat loopt erdoor.",
    ),
    dict(
        type="waarofniet",
        vraag="Olie en water scheiden zich omdat ze een verschillende massadichtheid hebben en niet mengen.",
        antwoord=True,
        uitleg="Olie heeft een kleinere massadichtheid, dus gaat ze bovenaan liggen. Omdat ze niet mengen, blijven de twee lagen apart.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de vloeistof die je na een destillatie opvangt?",
        antwoord=["destillaat", "het destillaat"],
        uitleg="Het destillaat is wat verdampt is en weer vloeibaar geworden, dus de stof met het laagste kookpunt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke scheidingstechniek gebruikt een waterzuiveringsstation om kleur- en geurstoffen aan actieve kool te laten hechten?",
        antwoord=["adsorptie", "adsorberen"],
        uitleg="Bij adsorptie hechten de deeltjes zich aan het oppervlak van de kool. Ze lossen niet op en gaan niet door een filter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het temperatuurgebied waarin een mengsel kookt?",
        antwoord=["kooktraject", "het kooktraject"],
        uitleg="Een mengsel heeft geen vast kookpunt maar een kooktraject, omdat de samenstelling tijdens het koken verandert.",
    ),
    dict(
        type="invultekst",
        vraag="Welke scheidingstechniek kies je voor een mengsel van twee vloeistoffen die wel mengen maar een verschillend kookpunt hebben?",
        antwoord=["destilleren", "destillatie"],
        uitleg="Decanteren werkt niet bij vloeistoffen die mengen. Het verschil in kookpunt maakt destilleren hier de juiste keuze.",
    ),
]
