# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — Het uitscheidingsstelsel.

Biologie, blok "Stofwisselingsfysiologie en secretie". Deel 1 gaat over de
bouw van het uitscheidingsstelsel en de nier, deel 2 over de werking van het
nefron, de osmoregulatie en de aandoeningen.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "In welke volgorde stroomt urine door het uitscheidingsstelsel?",
        [
            "nier, urineleider, urineblaas, urinebuis",
            "nier, urinebuis, urineblaas, urineleider",
            "urineblaas, nier, urineleider, urinebuis",
            "urineleider, nier, urinebuis, urineblaas",
        ],
        0,
        "De nier maakt de urine. Via de urineleider gaat ze naar de urineblaas, waar ze verzameld wordt, en via de urinebuis verlaat ze het lichaam.",
    ),
    M(
        "Wat is de functie van de urineleider of ureter?",
        [
            "urine van de nier naar de blaas brengen",
            "urine van de blaas naar buiten brengen",
            "bloed van de aorta naar de nier brengen",
            "gefilterd bloed van de nier terugvoeren",
        ],
        0,
        "Elke nier heeft een urineleider. Door peristaltiek in de wand gaat de urine naar de urineblaas.",
    ),
    I(
        "Hoe heet het buisje waarlangs de urine van de urineblaas naar buiten gaat?",
        ["urinebuis", "urethra"],
        "De urinebuis of urethra loopt van de blaas naar buiten. Een interne en een externe kringspier houden ze dicht tot je plast.",
    ),
    W(
        "De externe kringspier van de urineblaas kan je bewust aansturen.",
        True,
        "De interne kringspier werkt onbewust. De externe kringspier bestaat uit dwarsgestreept spierweefsel en kan je zelf openen en sluiten.",
    ),
    M(
        "Welke delen kan je op een lengtedoorsnede van de nier zien? Kruis alles aan wat juist is.",
        ["de nierschors of cortex", "het niermerg met de nierpiramides", "het nierbekken", "de galblaas"],
        [0, 1, 2],
        "Van buiten naar binnen zie je het nierkapsel, de schors, het merg met de piramides, de nierkelken en het nierbekken. De galblaas hoort bij de lever.",
    ),
    M(
        "Welk orgaantje ligt als een kapje bovenop elke nier en maakt onder meer adrenaline?",
        ["de bijnier", "de alvleesklier", "de milt", "de schildklier"],
        0,
        "De bijnier ligt op de nier, maar hoort bij het hormonaal stelsel. Ze maakt hormonen zoals adrenaline en aldosteron.",
    ),
    I(
        "Hoe noemt men de kleinste werkende eenheid van de nier, waarvan elke nier er ongeveer een miljoen heeft?",
        "nefron",
        "Een nefron bestaat uit een nierlichaampje en een nierbuisje. Daar wordt het bloed gefilterd en de urine gevormd.",
    ),
    M(
        "Waaruit bestaat het nierlichaampje of lichaampje van Malpighi?",
        [
            "de glomerulus met daarrond het kapsel van Bowman",
            "de lus van Henle met de verzamelbuis eromheen en de haarvaten",
            "de nierpiramide met daarin het nierbekken",
            "de bijnier met daaronder het nierkapsel",
        ],
        0,
        "In het nierlichaampje ligt een kluwen haarvaten, de glomerulus, omringd door het kapsel van Bowman dat het filtraat opvangt.",
    ),
    M(
        "In welke volgorde stroomt het filtraat door het nefron?",
        [
            "kapsel van Bowman, eerste kronkelbuisje, lus van Henle, tweede kronkelbuisje, verzamelbuis",
            "verzamelbuis, lus van Henle, eerste kronkelbuisje, kapsel van Bowman, tweede kronkelbuisje",
            "lus van Henle, kapsel van Bowman, verzamelbuis, eerste kronkelbuisje, tweede kronkelbuisje",
            "eerste kronkelbuisje, kapsel van Bowman, tweede kronkelbuisje, lus van Henle, verzamelbuis",
        ],
        0,
        "Het filtraat komt in het kapsel van Bowman, gaat door het eerste kronkelbuisje, de dalende en stijgende tak van de lus van Henle, het tweede kronkelbuisje en ten slotte de verzamelbuis.",
    ),
    M(
        "Welke lagen vormen samen de nierfilter tussen het bloed in de glomerulus en het kapsel van Bowman? Kruis alles aan wat juist is.",
        ["het endotheel van de haarvaten", "het basaalmembraan", "de podocyten", "het nierbekken"],
        [0, 1, 2],
        "Het bloed wordt gefilterd door drie lagen: het endotheel met poriën, het basaalmembraan en de podocyten met hun voetjes.",
    ),
    W(
        "Het bloed komt de glomerulus binnen via het afvoerend nierslagadertje en verlaat ze via het aanvoerend nierslagadertje.",
        False,
        "Het is omgekeerd: het aanvoerend slagadertje brengt het bloed naar de glomerulus en het afvoerend slagadertje voert het weg.",
    ),
    M(
        "Via welk bloedvat komt het bloed de nier binnen?",
        ["de nierslagader", "de nierader", "de leverpoortader", "de longslagader"],
        0,
        "De nierslagader komt van de aorta en brengt bloed naar de nier. De nierader voert het gezuiverde bloed af naar de onderste holle ader.",
    ),
    M(
        "Waarom laat een gezonde nierfilter geen rode bloedcellen en bijna geen grote eiwitten door?",
        [
            "ze zijn te groot om door de filter te passen",
            "ze worden in de glomerulus meteen afgebroken",
            "ze worden door de bijnier tegengehouden",
            "ze zitten vast in het nierbekken",
        ],
        0,
        "De nierfilter werkt op grootte. Water, zouten, glucose en ureum gaan erdoor, bloedcellen en grote eiwitten niet.",
    ),
    W(
        "Bloed of veel eiwit in de urine kan erop wijzen dat de nierfilter beschadigd is.",
        True,
        "Normaal blijven bloedcellen en grote eiwitten in het bloed. Vindt men ze in de urine, dan is de filter mogelijk aangetast.",
    ),
    M(
        "Welke stoffen vind je in een normale urine? Kruis alles aan wat juist is.",
        ["water", "ureum", "eiwitten zoals albumine", "glucose in grote hoeveelheid"],
        [0, 1],
        "Urine bestaat vooral uit water, met ureum, urinezuur en zouten. Grote eiwitten zoals albumine gaan normaal niet door de nierfilter. Glucose wordt normaal volledig teruggeresorbeerd. Glucose in de urine wijst bijvoorbeeld op diabetes.",
    ),
    I(
        "Hoe heet de stikstofhoudende afvalstof die de lever maakt uit de afbraak van aminozuren en die de nieren uitscheiden?",
        "ureum",
        "Bij de afbraak van aminozuren ontstaat giftig ammoniak. De lever zet dat om in het minder giftige ureum, dat met de urine het lichaam verlaat.",
    ),
    M(
        "Welk hormoon maakt de nier aan om de aanmaak van rode bloedcellen te stimuleren?",
        ["erytropoëtine (EPO)", "adrenaline", "aldosteron", "antidiuretisch hormoon"],
        0,
        "Bij zuurstoftekort maakt de nier EPO. Dat zet het beenmerg aan om meer rode bloedcellen te maken.",
    ),
    M(
        "Uit hoeveel lagen bestaat de wand van de urineleider?",
        ["drie", "één", "twee", "vijf"],
        0,
        "De wand van de urineleider heeft drie lagen: een slijmvlies aan de binnenkant, een spierlaag in het midden en een bindweefsellaag aan de buitenkant.",
    ),
    M(
        "Hoe heet de ruimte in de nier waarin de urine uit de nierkelken samenkomt, voor ze de urineleider ingaat?",
        ["het nierbekken", "de nierpapil", "de nierschors", "het kapsel van Bowman"],
        0,
        "De urine druppelt via de nierpapillen in de nierkelken en komt samen in het nierbekken. Van daar gaat ze naar de urineleider.",
    ),
    W(
        "Het niermerg ligt aan de buitenkant van de nier, rond de nierschors.",
        False,
        "De nierschors ligt aan de buitenkant, onder het nierkapsel. Het niermerg met de nierpiramides ligt meer naar binnen.",
    ),
]

DEEL2 = [
    M(
        "Wat gebeurt er bij de filtratie in de nier?",
        [
            "water en kleine opgeloste stoffen worden uit de glomerulus in het kapsel geperst",
            "nuttige stoffen gaan vanuit het nierbuisje terug naar het bloed in de haarvaten",
            "extra afvalstoffen worden vanuit het bloed actief in het nierbuisje gebracht",
            "de afgewerkte urine verlaat het lichaam langs de urineleider en daarna de urinebuis",
        ],
        0,
        "Door de hoge bloeddruk in de glomerulus wordt een deel van het plasma door de filter geduwd. Dat filtraat heet voorurine.",
    ),
    I(
        "Hoe noemt men de vloeistof die na de filtratie in het kapsel van Bowman zit, nog voor de terugopname?",
        "voorurine",
        "Per dag ontstaat ongeveer 180 liter voorurine. Het grootste deel daarvan wordt teruggeresorbeerd, zodat er maar ongeveer 1,5 liter urine overblijft.",
    ),
    M(
        "Wat is resorptie of reabsorptie in de nier?",
        [
            "nuttige stoffen gaan uit het nierbuisje terug naar het bloed",
            "het bloed wordt in de glomerulus door de filter geperst",
            "afvalstoffen worden vanuit het bloed in het buisje gepompt",
            "de urine wordt in de urineblaas verzameld en daar een tijd bewaard tot je plast",
        ],
        0,
        "Bij resorptie haalt het lichaam water, glucose, aminozuren en zouten terug uit de voorurine, via diffusie, osmose en actief transport.",
    ),
    W(
        "Bij een gezond persoon wordt alle glucose uit de voorurine teruggeresorbeerd.",
        True,
        "Glucose wordt in het eerste kronkelbuisje volledig teruggenomen. Pas bij een te hoge bloedsuikerspiegel kan er glucose in de urine verschijnen.",
    ),
    M(
        "Wat bedoelt men met secretie in het nefron?",
        [
            "extra stoffen actief vanuit het bloed in het nierbuisje brengen",
            "het terugnemen van water uit het nierbuisje naar het bloed",
            "het doorlaten van plasma door de nierfilter in de glomerulus",
            "het verzamelen van de afgewerkte urine in het nierbekken en de nierkelken",
        ],
        0,
        "Bij secretie brengen de cellen van het nierbuisje stoffen zoals sommige geneesmiddelen en H⁺-ionen actief vanuit het bloed in de urine.",
    ),
    M(
        "Welke processen gebeuren in het nefron om urine te maken? Kruis alles aan wat juist is.",
        ["filtratie", "resorptie", "secretie", "emulgeren"],
        [0, 1, 2],
        "Filtratie, resorptie en secretie maken samen de urine, die daarna wordt uitgescheiden. Emulgeren doen galzouten bij de vertering.",
    ),
    M(
        "Wat is osmoregulatie?",
        [
            "het constant houden van de hoeveelheid water en zouten in het lichaam",
            "het constant houden van de lichaamstemperatuur rond 37 °C, ook bij koude",
            "het regelen van de hoeveelheid suiker in het bloed na een maaltijd",
            "het aanpassen van de ademhaling en de hartslag bij een inspanning",
        ],
        0,
        "Bij osmoregulatie houdt het lichaam de osmotische waarde van het bloed stabiel. De nieren spelen daarin de hoofdrol.",
    ),
    M(
        "Waar wordt het antidiuretisch hormoon (ADH) aan het bloed afgegeven?",
        ["door de hypofyse", "door de bijnier", "door de alvleesklier", "door de nier zelf"],
        0,
        "ADH wordt gemaakt in de hypothalamus en via de hypofyse aan het bloed afgegeven. Het werkt in op de nier.",
    ),
    M(
        "Je hebt veel gezweet en weinig gedronken. Wat gebeurt er met de ADH-afgifte en de urine?",
        [
            "er komt meer ADH, de verzamelbuis neemt meer water terug en je plast weinig en geconcentreerd",
            "er komt minder ADH, de verzamelbuis neemt minder water terug en je plast veel en verdund",
            "er komt meer ADH, de verzamelbuis neemt minder water terug en je plast veel en verdund",
            "er komt minder ADH, de verzamelbuis neemt meer water terug en je plast weinig en geconcentreerd",
        ],
        0,
        "Osmoreceptoren merken dat het bloed te geconcentreerd is. De hypofyse geeft meer ADH af, de verzamelbuis wordt beter doorlaatbaar voor water en er gaat meer water terug naar het bloed.",
    ),
    W(
        "ADH maakt de wand van de verzamelbuis minder doorlaatbaar voor water.",
        False,
        "ADH doet net het omgekeerde: het maakt de verzamelbuis beter doorlaatbaar, zodat er meer water terug naar het bloed gaat.",
    ),
    M(
        "Welke onderdelen horen bij het feedbacksysteem van de waterhuishouding? Kruis alles aan wat juist is.",
        [
            "osmoreceptoren als sensor",
            "de hypothalamus als controlecentrum",
            "de nieren als effector",
            "de alvleesklier als sensor",
        ],
        [0, 1, 2],
        "Osmoreceptoren meten de concentratie, de hypothalamus beslist en stuurt ADH aan, en de nieren voeren uit. Daarnaast zorgt de dorstprikkel ervoor dat je drinkt.",
    ),
    I(
        "Welk gevoel zet de hypothalamus in gang wanneer het bloed te geconcentreerd wordt, zodat je meer gaat drinken?",
        ["dorst", "dorstprikkel"],
        "De dorstprikkel is de neurale kant van de waterhuishouding. Samen met ADH zorgt ze ervoor dat er weer genoeg water in het lichaam komt.",
    ),
    W(
        "Alcohol remt de afgifte van ADH, waardoor je meer moet plassen.",
        True,
        "Met minder ADH neemt de verzamelbuis minder water terug. Je plast meer en kan uitdrogen.",
    ),
    M(
        "Wat is een veelvoorkomende oorzaak van een blaasontsteking?",
        [
            "bacteriën die via de urinebuis binnendringen",
            "een tekort aan ADH in het bloed van de patiënt",
            "te veel rode bloedcellen in de voorurine",
            "een verstopping van de nierslagader door een stolsel",
        ],
        0,
        "Een blaasontsteking is meestal een infectie met darmbacteriën. Omdat de urinebuis bij vrouwen kort is, komt ze bij hen vaker voor.",
    ),
    M(
        "Welke maatregelen helpen nierstenen voorkomen? Kruis alles aan wat juist is.",
        ["voldoende water drinken", "niet te veel zout eten", "gezond en gevarieerd eten", "zo weinig mogelijk plassen"],
        [0, 1, 2],
        "Veel drinken verdunt de urine, zodat zouten minder snel kristalliseren. Weinig zout en een gezond dieet helpen ook.",
    ),
    M(
        "Hoe kan een arts een niersteen zonder operatie verkleinen?",
        [
            "met een toestel dat de steen met schokgolven in stukjes slaat",
            "met een kunstnier die de steen uit het bloed filtert",
            "met een spoelvloeistof die de patiënt via de mond moet drinken",
            "met extra ADH, waardoor de steen oplost in de urine",
        ],
        0,
        "Een niersteenverbrijzelaar slaat de steen met schokgolven van buiten het lichaam in kleine stukjes. Die verlaten het lichaam met de urine.",
    ),
    M(
        "Wat gebeurt er bij hemodialyse?",
        [
            "het bloed stroomt door een kunstnier en geeft er afvalstoffen af aan een spoelvloeistof",
            "de zieke nier wordt in een operatie vervangen door de gezonde nier van een donor",
            "de patiënt krijgt elke week EPO om de werking van zijn eigen nieren te herstellen",
            "de urineleider wordt met een buisje verwijd zodat de urine makkelijker wegloopt",
        ],
        0,
        "Bij hemodialyse gaat het bloed via een shunt naar de kunstnier. Afvalstoffen diffunderen door een semipermeabel membraan naar de dialysevloeistof.",
    ),
    W(
        "Bij nierfalen kunnen afvalstoffen zoals ureum zich in het bloed opstapelen.",
        True,
        "Als de nieren onvoldoende filteren, blijven afvalstoffen in het bloed. Dan is dialyse of een niertransplantatie nodig.",
    ),
    I(
        "Hoe heet de verbinding tussen een slagader en een ader, die men in de arm aanlegt om vlot bloed te kunnen afnemen voor hemodialyse?",
        "shunt",
        "Door de shunt wordt de ader breder en steviger. Zo kan men er drie keer per week een naald in steken voor de dialyse.",
    ),
    W(
        "De lus van Henle ligt volledig in de nierschors.",
        False,
        "De lus van Henle duikt diep het niermerg in. Daar helpt ze een hoge zoutconcentratie op te bouwen, waardoor de nier geconcentreerde urine kan maken.",
    ),
]
