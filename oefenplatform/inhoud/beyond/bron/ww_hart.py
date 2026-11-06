# -*- coding: utf-8 -*-
"""🌍 Beyond, welzijnswetenschappen — Het hart en de bloedsomloop.

Biologie, blok "Stofwisselingsfysiologie en secretie", koppen "Het hart" en
"De bloedsomloop". Deel 1 gaat over de bouw van het hart, de kleppen en de
bloedstroom, deel 2 over de prikkelgeleiding, de hartcyclus, het ECG en de
dubbele bloedsomloop met de bloedvaten.
"""

from ww_hulp import I, M, W

DEEL1 = [
    M(
        "Uit hoeveel holtes bestaat het menselijk hart?",
        ["vier: twee boezems en twee kamers", "twee: één boezem en één kamer", "drie: twee boezems en één kamer", "zes: drie boezems en drie kamers"],
        0,
        "Het hart heeft een linker- en een rechterboezem of atrium, en een linker- en een rechterkamer of ventrikel.",
    ),
    M(
        "Wat scheidt de linker- van de rechterhelft van het hart?",
        ["het tussenschot of septum", "het hartzakje of pericard", "de hartpunt of apex", "de aortaboog"],
        0,
        "Het septum houdt het zuurstofrijke bloed links gescheiden van het zuurstofarme bloed rechts.",
    ),
    M(
        "Welk bloedvat brengt zuurstofarm bloed uit het lichaam naar de rechterboezem?",
        ["de bovenste en de onderste holle ader", "de longaders uit beide longen", "de aorta met de aortaboog", "de longslagader naar de longen"],
        0,
        "Het bloed uit het lichaam komt via de bovenste en de onderste holle ader in de rechterboezem.",
    ),
    M(
        "Welk bloedvat vertrekt uit de rechterkamer?",
        ["de longslagader", "de aorta", "de longader", "de onderste holle ader"],
        0,
        "De rechterkamer pompt zuurstofarm bloed via de longslagader naar de longen.",
    ),
    W(
        "De longaders vervoeren zuurstofrijk bloed van de longen naar de linkerboezem.",
        True,
        "Aders brengen bloed naar het hart. De longaders zijn de enige aders met zuurstofrijk bloed, want dat bloed komt net uit de longen.",
    ),
    W(
        "Een slagader is een bloedvat dat altijd zuurstofrijk bloed vervoert.",
        False,
        "Een slagader vervoert bloed van het hart weg. De longslagader is een slagader met zuurstofarm bloed.",
    ),
    M(
        "Welke kamer heeft de dikste spierwand, en waarom?",
        [
            "de linkerkamer, want ze pompt het bloed door de hele grote bloedsomloop",
            "de rechterkamer, want ze pompt het bloed door de longen, die ver weg liggen",
            "de linkerboezem, want ze ontvangt het bloed met de hoogste druk",
            "alle kamers even dik, want ze pompen evenveel bloed per slag",
        ],
        0,
        "De linkerkamer moet een hoge druk opbouwen om het bloed door het hele lichaam te duwen. Daarom is haar spierwand veel dikker dan die van de rechterkamer.",
    ),
    M(
        "Welke klep ligt tussen de linkerboezem en de linkerkamer?",
        ["de mitralisklep", "de tricuspidalisklep", "de aortaklep", "de pulmonalisklep"],
        0,
        "De mitralisklep heeft twee slippen en ligt links. Rechts ligt de tricuspidalisklep, met drie slippen.",
    ),
    M(
        "Welke kleppen zijn atrioventriculaire kleppen? Kruis alles aan wat juist is.",
        ["de tricuspidalisklep", "de mitralisklep", "de aortaklep", "de pulmonalisklep"],
        [0, 1],
        "Atrioventriculaire kleppen liggen tussen een boezem en een kamer: de tricuspidalisklep rechts en de mitralisklep links. Aorta- en pulmonalisklep zijn halvemaanvormige kleppen bij de slagaders.",
    ),
    M(
        "Wat is de taak van de hartkleppen?",
        [
            "ze laten het bloed maar in één richting stromen",
            "ze bepalen hoe snel en hoe hard het hart klopt",
            "ze maken het bloed dat erdoor stroomt rijker aan zuurstof",
            "ze voeden de hartspier zelf met zuurstofrijk bloed",
        ],
        0,
        "De kleppen gaan open als het bloed in de goede richting duwt en sluiten als het zou terugstromen. Het bekende hartgeluid is het dichtklappen van de kleppen.",
    ),
    M(
        "In welke volgorde stroomt het bloed door de rechterhelft van het hart?",
        [
            "holle aders, rechterboezem, tricuspidalisklep, rechterkamer, pulmonalisklep, longslagader",
            "longaders, rechterboezem, mitralisklep, rechterkamer, aortaklep, aorta",
            "holle aders, rechterkamer, pulmonalisklep, rechterboezem, tricuspidalisklep, longslagader",
            "longslagader, rechterkamer, tricuspidalisklep, rechterboezem, holle aders, aorta",
        ],
        0,
        "Het zuurstofarme bloed komt via de holle aders in de rechterboezem, gaat door de tricuspidalisklep naar de rechterkamer en verlaat het hart via de pulmonalisklep en de longslagader.",
    ),
    I(
        "Hoe heet de grote slagader die het zuurstofrijke bloed uit de linkerkamer naar het lichaam brengt?",
        "aorta",
        "De aorta vertrekt uit de linkerkamer, maakt een boog en loopt dan langs de wervelkolom naar beneden. Alle slagaders van de grote bloedsomloop takken ervan af.",
    ),
    M(
        "Uit welke lagen bestaat de hartwand, van binnen naar buiten?",
        [
            "endocard, myocard, epicard",
            "epicard, myocard, endocard",
            "myocard, endocard, epicard",
            "pericard, endocard, myocard",
        ],
        0,
        "Het endocard bekleedt de binnenkant, het myocard is de dikke spierlaag en het epicard ligt aan de buitenkant. Errond zit nog het hartzakje of pericard.",
    ),
    I(
        "Hoe heet de dikke spierlaag van de hartwand?",
        ["myocard", "hartspier"],
        "Het myocard is de hartspier zelf. Een hartinfarct is het afsterven van een stuk myocard door een gebrek aan zuurstof.",
    ),
    M(
        "Hoe krijgt de hartspier zelf zuurstof en voedingsstoffen?",
        [
            "via de kransslagaders, die vlak boven de aortaklep van de aorta aftakken",
            "rechtstreeks uit het bloed dat door de kamers en boezems stroomt",
            "via de longaders, die eerst langs de hartspier lopen",
            "via het vocht in het hartzakje, dat voedingsstoffen doorgeeft aan de spier",
        ],
        0,
        "De kransslagaders of coronairen liggen als een krans rond het hart. Raakt er één verstopt, dan krijgt een deel van de hartspier geen zuurstof meer.",
    ),
    W(
        "Een hartinfarct ontstaat meestal doordat een kransslagader verstopt raakt.",
        True,
        "Achter de verstopping krijgt de hartspier geen zuurstof meer en sterft ze af. Snel ingrijpen beperkt de schade.",
    ),
    M(
        "Wat is het hartzakje of pericard?",
        [
            "een vlies rond het hart met wat vocht, zodat het vlot kan bewegen",
            "de holte binnen in de linkerkamer waar het bloed verzameld wordt",
            "het buitenste deel van de aorta, vlak boven het hart",
            "het klepje tussen de rechterboezem en de rechterkamer",
        ],
        0,
        "Het pericard omsluit het hart. In de pericardholte zit een beetje vocht dat de wrijving bij elke hartslag beperkt.",
    ),
    M(
        "Welke bloedvaten komen toe in het hart? Kruis alles aan wat juist is.",
        ["de bovenste holle ader", "de aorta", "de longaders", "de longslagader"],
        [0, 2],
        "Aders brengen bloed naar het hart: de holle aders naar de rechterboezem, de longaders naar de linkerboezem. De aorta en de longslagader vertrekken uit het hart.",
    ),
    W(
        "De onderkant of punt van het hart heet de hartbasis.",
        False,
        "De punt van het hart heet de apex en wijst naar links onderaan. De hartbasis is de brede bovenkant, waar de grote bloedvaten vertrekken en toekomen.",
    ),
    W(
        "Het hart ligt in de borstholte, tussen de twee longen in en een beetje naar links.",
        True,
        "Het hart ligt achter het borstbeen, tussen de longen, met de punt naar links onderaan.",
    ),
]

DEEL2 = [
    M(
        "Waar ontstaan de prikkels die het hart doen samentrekken?",
        [
            "in de sinusknoop, een groepje gangmakercellen in de boezem",
            "in de hersenen, die bij elke hartslag een signaal sturen",
            "in de linkerkamer, die het hardste werkt van alle holtes",
            "in de aorta, door de rek van haar wand bij elke nieuwe hartslag",
        ],
        0,
        "De sinusknoop of sinoatriale knoop is de natuurlijke gangmaker. Het hart klopt dus ook zonder signaal uit de hersenen.",
    ),
    M(
        "In welke volgorde loopt de prikkel door het impulsgeleidingssysteem van het hart?",
        [
            "sinusknoop, AV-knoop, bundel van His, bundeltakken, purkinjevezels",
            "AV-knoop, sinusknoop, purkinjevezels, bundel van His, bundeltakken",
            "bundel van His, sinusknoop, bundeltakken, AV-knoop, purkinjevezels",
            "purkinjevezels, bundeltakken, bundel van His, AV-knoop, sinusknoop",
        ],
        0,
        "De prikkel start in de sinusknoop, gaat via de boezems naar de AV-knoop, dan door de bundel van His en de bundeltakken naar de purkinjevezels in de kamerwand.",
    ),
    M(
        "Waarom houdt de AV-knoop de prikkel even tegen?",
        [
            "zodat de boezems eerst leeglopen voor de kamers samentrekken",
            "zodat de kamers eerst kunnen samentrekken voor de boezems dat doen",
            "zodat het hart tussen twee slagen helemaal stil kan blijven staan",
            "zodat de prikkel genoeg kracht opbouwt om de hersenen te bereiken",
        ],
        0,
        "Door die korte vertraging trekken eerst de boezems samen en duwen ze hun bloed in de kamers. Pas daarna trekken de kamers samen.",
    ),
    W(
        "Het autonoom zenuwstelsel kan de hartslag versnellen of vertragen, maar de sinusknoop bepaalt het basisritme.",
        True,
        "Hartzenuwen vanuit het cardiovasculair centrum passen het ritme aan, bijvoorbeeld bij inspanning. Het basisritme zelf komt uit de sinusknoop.",
    ),
    I(
        "Hoe noemt men de fase waarin de hartspier van een kamer samentrekt?",
        ["systole", "kamersystole"],
        "Systole is samentrekken, diastole is ontspannen. Tijdens de kamersystole wordt het bloed in de slagaders geperst.",
    ),
    M(
        "Wat gebeurt er tijdens de kamersystole? Kruis alles aan wat juist is.",
        [
            "de kamers trekken samen",
            "de atrioventriculaire kleppen sluiten",
            "de aortaklep en de pulmonalisklep gaan open",
            "de boezems trekken tegelijk samen",
        ],
        [0, 1, 2],
        "Als de kamers samentrekken, klappen de AV-kleppen dicht en gaan de halvemaanvormige kleppen open. De boezems zijn dan net ontspannen en vullen zich.",
    ),
    M(
        "Wat gebeurt er tijdens de rustfase van het hart?",
        [
            "boezems en kamers zijn ontspannen en het bloed loopt het hart in",
            "boezems en kamers trekken allebei tegelijk krachtig samen",
            "alleen de kamers trekken samen, terwijl de boezems gesloten blijven",
            "het hart staat helemaal stil en er stroomt even geen bloed meer",
        ],
        0,
        "In de rustfase zijn boezems en kamers in diastole. Het bloed uit de aders vult de boezems en loopt al voor een groot deel door naar de kamers.",
    ),
    M(
        "Wat registreert een elektrocardiogram of ECG?",
        [
            "de elektrische activiteit van het hart",
            "de druk in de grote slagaders",
            "de hoeveelheid zuurstof in het bloed",
            "het geluid van de hartkleppen",
        ],
        0,
        "Elektroden op de huid meten de elektrische prikkels die door het hart lopen. Zo ziet een arts of het ritme en de geleiding normaal zijn.",
    ),
    M(
        "Met welke gebeurtenis komt het QRS-complex op een ECG overeen?",
        [
            "de prikkeling van de kamers, net voor ze samentrekken",
            "de prikkeling van de boezems, net voor ze samentrekken",
            "het herstel van de kamers na hun samentrekking",
            "het dichtklappen van de aortaklep na de samentrekking",
        ],
        0,
        "De P-top hoort bij de boezems, het QRS-complex bij de prikkeling van de kamers en de T-top bij het herstel van de kamers.",
    ),
    W(
        "De T-top op een ECG hoort bij de prikkeling van de boezems.",
        False,
        "De prikkeling van de boezems is de P-top, de eerste golf. De T-top komt als laatste en hoort bij het herstel van de kamers.",
    ),
    M(
        "Wat is de kleine bloedsomloop?",
        [
            "de weg van de rechterkamer via de longen naar de linkerboezem",
            "de weg van de linkerkamer via het lichaam naar de rechterboezem",
            "de weg van de darmen via de lever naar het hart",
            "de weg van de nieren via de blaas naar buiten",
        ],
        0,
        "In de kleine bloedsomloop of longcirculatie gaat het bloed van het hart naar de longen en terug, waar het zuurstof opneemt en CO₂ afgeeft.",
    ),
    W(
        "Bij een dubbele bloedsomloop passeert het bloed twee keer door het hart bij één volledige rondgang door het lichaam.",
        True,
        "Eén keer voor de kleine bloedsomloop langs de longen, één keer voor de grote bloedsomloop langs de rest van het lichaam.",
    ),
    M(
        "Wat is een poortader?",
        [
            "een ader tussen twee haarvatennetwerken, zoals tussen darm en lever",
            "een ader die bloed rechtstreeks van een slagader naar het hart terugbrengt",
            "een slagader met een klep die het bloed bij de ingang van een orgaan tegenhoudt",
            "een lymfevat dat onder het sleutelbeen uitmondt in een grote ader",
        ],
        0,
        "Bij de leverpoortader gaat het bloed eerst door de haarvaten van de darmen, dan door de poortader en daarna opnieuw door haarvaten in de lever.",
    ),
    M(
        "Waarom loopt het bloed van de darmen eerst door de lever voor het terug naar het hart gaat?",
        [
            "de lever verwerkt eerst de opgenomen voedingsstoffen en ontgift het bloed",
            "de lever voegt eerst extra zuurstof toe aan het zuurstofarme bloed uit de darmen",
            "de lever filtert alle rode bloedcellen uit het bloed om ze te vernieuwen",
            "de lever pompt het bloed verder omdat de darmen te ver van het hart liggen",
        ],
        0,
        "Via de leverpoortader komt het bloed met voedingsstoffen eerst in de lever. Die slaat glucose op, verwerkt aminozuren en ontgift schadelijke stoffen.",
    ),
    M(
        "Wat is een verschil tussen een slagader en een ader?",
        [
            "een slagader heeft een dikke, gespierde wand, een ader een dunnere wand met kleppen",
            "een slagader heeft kleppen tegen terugstroming en een ader heeft er geen",
            "een ader heeft altijd een dikkere en meer gespierde wand dan de slagader ernaast",
            "een slagader vervoert bloed naar het hart, een ader bloed van het hart weg",
        ],
        0,
        "Slagaders moeten de hoge druk van het hart opvangen en hebben daarom een dikke wand. Aders hebben een lage druk, een dunnere wand en veneuze kleppen.",
    ),
    M(
        "Welke lagen vind je in de wand van een slagader? Kruis alles aan wat juist is.",
        ["een endotheellaag aan de binnenkant", "een laag glad spierweefsel", "bindweefsel aan de buitenkant", "een laag dwarsgestreept spierweefsel"],
        [0, 1, 2],
        "De wand bestaat uit endotheel, een middenlaag met glad spierweefsel en elastische vezels, en een buitenlaag van bindweefsel. Dwarsgestreept spierweefsel vind je in skeletspieren.",
    ),
    I(
        "Hoe heten de kleinste bloedvaten, met een wand van één cellaag dik, waar de uitwisseling met de weefsels gebeurt?",
        ["haarvaten", "capillairen"],
        "In de haarvaten gaan zuurstof en voedingsstoffen naar de weefsels en komen CO₂ en afvalstoffen in het bloed. Hun wand is maar één laag endotheel dik.",
    ),
    M(
        "Wat helpt het bloed in de aders van de benen terug naar het hart te stromen? Kruis alles aan wat juist is.",
        ["de veneuze kleppen", "het samentrekken van de beenspieren rond de aders", "de zuigwerking bij het inademen", "de hoge druk van de linkerkamer in de aders"],
        [0, 1, 2],
        "De druk in de aders is laag. De kleppen beletten terugstroming, de beenspieren knijpen de aders samen en de ademhaling zuigt het bloed mee naar boven.",
    ),
    W(
        "De druk in de aders is hoger dan in de slagaders.",
        False,
        "De druk is het hoogst vlak na het hart, in de aorta en de slagaders. In de haarvaten zakt ze, en in de aders is ze het laagst.",
    ),
    M(
        "In welke volgorde stroomt het bloed van het hart naar de weefsels en terug?",
        [
            "slagader, arteriolen, haarvaten, venulen, ader",
            "ader, venulen, haarvaten, arteriolen, slagader",
            "slagader, venulen, haarvaten, arteriolen, ader",
            "arteriolen, slagader, haarvaten, ader, venulen",
        ],
        0,
        "Slagaders vertakken in arteriolen en dan in haarvaten. Die komen samen in venulen, en die weer in aders die naar het hart lopen.",
    ),
]
