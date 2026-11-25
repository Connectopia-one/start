# -*- coding: utf-8 -*-
"""Uitdaging Ontwikkeling en pedagogisch handelen 🚀 Boost dubbele finaliteit
(25 november 2026), in de vormen van het examen van de Examencommissie: 40
vragen die alle hoofdstukken door elkaar halen, van welzijn en de
determinanten van gezondheid tot Piaget, Kohlberg en Erikson, observeren,
communiceren, spel en activiteiten. Zes verzonnen observatienotities en zes
verzonnen uitspraken om op te klikken, tabellen, keuzelijsten, slepen,
koppelen, sorteren, volgorde, een casus en een open vraag. Geen nieuwe
leerstof: alles staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_oph.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Ontwikkeling en pedagogisch handelen"
BESTAND = "boost-df-oph-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/oph-boost-df-uitdaging"
NOT = "zes-notities.svg"
UIT = "zes-uitspraken.svg"
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Observatienotities
    klik("Bekijk de zes observatienotities. Klik op de notitie met een veralgemening over één kind.",
         NOT, [Z[2]],
         "'Altijd lui' is een besluit over al het gedrag van Mehdi. Een goede notitie beschrijft wat je op één moment ziet."),
    klik("Klik op de notitie met een vooroordeel over een hele groep.",
         NOT, [Z[4]],
         "Een vooroordeel is een mening over een groep zonder dat je de mensen kent. Een observatie moet objectief zijn."),
    klik("Klik op de notitie die toekijkend spel beschrijft.",
         NOT, [Z[5]],
         "Bij toekijkend spel kijkt het kind hoe anderen spelen, zonder zelf mee te doen."),
    klik("Klik op de notitie waarin de begeleider zijn eigen gevoel en een gok opschrijft in plaats van wat hij ziet.",
         NOT, [Z[6]],
         "'Ik denk' en 'vast moe' zijn geen waarneming. Een objectieve observatie beschrijft wat je ziet en hoort."),
    met_prent(NOT, tabel(
        "Voldoet deze notitie aan de criteria van een goede observatie?",
        [
            ("notitie 1", J),
            ("notitie 3", J),
            ("notitie 2", F),
        ],
        "Notities 1 en 3 beschrijven nauwkeurig en objectief wat er gebeurt. Notitie 2 is een veralgemening.")),

    # Uitspraken
    klik("Bekijk de zes uitspraken. Klik op de uitspraak met animisme.",
         UIT, [Z[1]],
         "Bij animisme geeft een kleuter levenloze dingen gevoelens of een wil: de zon is moe."),
    klik("Klik op de uitspraak die past bij het pre-conventionele stadium van Kohlberg.",
         UIT, [Z[2]],
         "In het pre-conventionele stadium tellen straf en beloning: ik doe het niet, want dan krijg ik straf."),
    klik("Klik op de uitspraak die hypothetisch denken toont.",
         UIT, [Z[4]],
         "Hypothetisch denken is redeneren over wat zou kunnen: 'wat als ...?'. Dat hoort bij het formeel-operationele stadium."),
    klik("Klik op de uitspraak die egocentrisme toont.",
         UIT, [Z[6]],
         "Een kleuter kent alleen zijn eigen kijk: wat hij niet ziet, ziet een ander volgens hem ook niet."),
    met_prent(UIT, keuze(
        "Uitspraak 3 toont dat het kind de [[*conservatie|objectpermanentie|animisme]] begrijpt. Uitspraak 5 past bij het [[*conventionele|post-conventionele]] stadium.",
        "Een hoeveelheid blijft gelijk als de vorm verandert: dat is conservatie. Je houden aan de regels omdat het zo hoort, is conventioneel.")),

    # Welzijn en determinanten
    sorteer(
        "Bij welke determinant van Lalonde hoort dit?",
        ["biologische factoren", "omgeving", "leefstijl", "voorzieningen"],
        [
            ["erfelijke aanleg voor diabetes", "biologische factoren"],
            ["een woning in een buurt met veel fijn stof", "omgeving"],
            ["elke dag roken", "leefstijl"],
            ["een huisarts in de buurt", "voorzieningen"],
        ],
        "Lalonde onderscheidt vier determinanten. Alleen de leefstijl kan je zelf het meest veranderen."),
    mk("Iemand kan koken en heeft alles in huis, maar heeft geen zin. Wat ontbreekt volgens het gedragswiel?",
       ["De drijfveren, zoals motivatie en gewoonten",
        "De competenties, want die persoon kan niet koken",
        "De context, want er is niets in huis om te koken",
        "De biologische factoren, zoals erfelijke aanleg"],
       0,
       "Wie het kan (competenties) en alles heeft (context), maar niet wil, mist drijfveren."),
    keuze(
        "De geluksdriehoek heeft [[*drie|vier|vijf]] bouwstenen. Wie zonder opleiding voor een ziek familielid zorgt, is een [[*mantelzorger|beroepskracht]].",
        "Goed omringd zijn, je goed voelen en jezelf kunnen zijn. Een mantelzorger zorgt onbetaald voor iemand uit zijn omgeving."),

    # Ontwikkeling
    volgorde(
        "Zet de levensloopfasen van een kind in de juiste volgorde.",
        ["baby", "peuter", "kleuter", "midden-kindertijd", "adolescentie"],
        "Na de kleuter komt de midden-kindertijd (lagere school), daarna de adolescentie."),
    koppel(
        "Koppel de levensfase aan het conflict van Erikson.",
        [
            ["baby", "vertrouwen tegenover wantrouwen"],
            ["peuter", "autonomie tegenover twijfel en schaamte"],
            ["adolescent", "identiteit tegenover identiteitsverwarring"],
        ],
        ["generativiteit tegenover stagnatie"],
        "Erikson koppelt elke fase aan een conflict. Generativiteit hoort bij de volwassenheid."),
    tabel(
        "Hoort deze beweging van een jong kind bij de grove of bij de fijne motoriek?",
        [
            ("leren lopen", "grof"),
            ("de pincetgreep", "fijn"),
            ("een bal wegtrappen", "grof"),
            ("met een schaar knippen", "fijn"),
        ],
        "Grove motoriek zijn grote bewegingen van armen, benen en romp. Fijne motoriek zijn precieze bewegingen van hand en vingers.",
        kolommen=["grof", "fijn"]),
    tabel(
        "Klopt dit over de ontwikkeling?",
        [
            ("De ontwikkeling gaat van grof naar fijn.", J),
            ("Babyreflexen blijven je hele leven bestaan.", F),
            ("Een groeispurt kan voor een tiener moeilijk zijn.", J),
        ],
        "De meeste babyreflexen verdwijnen na enkele maanden. Een groeispurt kan onhandig en onzeker maken."),
    keuze(
        "Een baby die weet dat een verstopt speeltje nog bestaat, heeft [[*objectpermanentie|conservatie]]. Een kind dat stokjes op lengte legt, doet aan [[*seriatie|classificatie]].",
        "Objectpermanentie ontstaat in het sensomotorische stadium. Ordenen op grootte heet seriatie."),
    mk("Een kind is veilig gehecht. Wat zie je meestal?",
       ["Het verkent de wereld en zoekt troost bij zijn zorgfiguur",
        "Het kind negeert zijn zorgfiguur als die vertrekt en terugkomt",
        "Het kind klampt zich vast en durft nooit van zijn zorgfiguur weg",
        "Het kind is bang voor iedereen, ook voor zijn eigen zorgfiguur"],
       0,
       "Een veilig gehecht kind gebruikt zijn zorgfiguur als veilige basis: het gaat op ontdekking en keert terug als het troost nodig heeft."),
    keuze(
        "Ouders die zorgen voor hun kinderen én voor hun eigen ouders, horen bij de [[*sandwichgeneratie|peergroep]]. Verouderen door roken en weinig beweging is [[*secundair|primair]] verouderen.",
        "De sandwichgeneratie zit tussen twee generaties in. Secundair verouderen hangt samen met leefstijl en omgeving."),

    # Observeren en rapporteren
    tabel(
        "Klopt dit over waarnemen en observeren in de kinderopvang?",
        [
            ("Bij een bedekte observatie weet de persoon niet dat hij bekeken wordt.", J),
            ("Een observatieschema gebruik je als je nog geen doel hebt.", F),
            ("Door gewenning merk je een prikkel na een tijd minder op.", J),
        ],
        "Een schema vraagt een doel vooraf: dan weet je waarop je let. Gewenning maakt dat je een blijvende prikkel minder opmerkt."),
    sleep(
        "Wat je op het werk te weten komt, valt onder het [[beroepsgeheim]]. Regels die uit waarden volgen, heten [[normen]].",
        ["vooroordeel", "behoeften"],
        "Over wat je op het werk hoort, zwijg je tegenover buitenstaanders. Normen zijn de regels die uit waarden komen."),

    # Gedrag en behoeften
    volgorde(
        "Zet de behoeften van Maslow in volgorde, van onderaan de piramide naar boven.",
        ["fysieke behoeften", "zekerheid", "sociaal contact", "erkenning", "zelfactualisatie"],
        "Onderaan staan eten, drinken en slapen. Pas als de lagere behoeften vervuld zijn, komen de hogere aan de beurt."),
    mk("Een kind komt zonder ontbijt naar school en kan zich niet concentreren. Hoe verklaar je dat met Maslow?",
       ["Een fysieke behoefte gaat voor op leren",
        "Het kind heeft vooral nood aan meer erkenning",
        "Het kind zit al op het niveau van zelfactualisatie",
        "Leren hoort bij de onderste laag van de piramide"],
       0,
       "De onderste laag eist eerst aandacht. Met honger lukt leren niet goed."),

    # Communiceren
    koppel(
        "Koppel de letter van de LSD-methode aan wat je doet.",
        [
            ["L", "actief luisteren met je houding en kleine aanmoedigingen"],
            ["S", "in je eigen woorden herhalen wat je begrepen hebt"],
            ["D", "open vragen en gevoelsvragen stellen"],
        ],
        ["een oplossing opleggen"],
        "Luisteren, Samenvatten, Doorvragen."),
    volgorde(
        "Zet de vier G's van het 4G-model in de juiste volgorde.",
        ["gedrag", "gevoel", "gevolg", "gewenst gedrag"],
        "Je benoemt eerst het gedrag, dan je gevoel en het gevolg, en tot slot het gewenste gedrag."),
    sorteer(
        "Welke stap van verbindend communiceren is dit?",
        ["waarneming", "gevoel", "behoefte", "verzoek"],
        [
            ["'Ik zie dat de blokken over de vloer liggen.'", "waarneming"],
            ["'Ik word daar zenuwachtig van.'", "gevoel"],
            ["'Ik wil dat niemand erover valt.'", "behoefte"],
            ["'Wil je ze in de bak leggen?'", "verzoek"],
        ],
        "Verbindend communiceren begint bij wat je waarneemt, en eindigt met een verzoek waarop de ander ook nee mag zeggen."),
    mk("Welke zin is een ik-boodschap?",
       ["'Ik schrik als je zo hard roept.'",
        "'Jij roept altijd veel te hard.'",
        "'Waarom moet jij weer zo roepen?'",
        "'Iedereen vindt je roepen vervelend.'"],
       0,
       "Een ik-boodschap vertelt wat het gedrag met jou doet, zonder de ander aan te vallen."),

    # Spel en activiteiten
    tabel(
        "Welke soort spel is dit?",
        [
            ("Twee peuters bouwen naast elkaar elk hun eigen toren.", "parallel"),
            ("Kinderen verdelen rollen en bouwen samen één kamp.", "coöperatief"),
            ("Een kleuter doet alsof de stoel een auto is.", "doen-alsof"),
        ],
        "Parallel spel is naast elkaar, coöperatief spel is samen naar één doel. Doen-alsof-spel komt uit het symbolisch denken.",
        kolommen=["parallel", "coöperatief", "doen-alsof"]),
    keuze(
        "Een lied zingen hoort bij [[*muzikale|manuele]] expressie. Een rol spelen hoort bij [[*dramatische|muzikale]] expressie.",
        "Bij muzikale expressie gebruik je klank en ritme. Bij dramatische expressie speel je een rol."),
    sorteer(
        "Is dit een ADL-activiteit of een vrijetijdsactiviteit voor een bewoner?",
        ["ADL", "vrije tijd"],
        [
            ["zich wassen", "ADL"],
            ["een kaartspel spelen", "vrije tijd"],
            ["zich aankleden", "ADL"],
            ["samen naar muziek luisteren", "vrije tijd"],
        ],
        "ADL zijn de activiteiten van het dagelijks leven, zoals wassen, aankleden en eten."),

    inv("Hoeveel stadia onderscheidt Piaget? Een getal.",
        ["4", "vier"],
        "Sensomotorisch, pre-operationeel, concreet-operationeel en formeel-operationeel."),
    mk("Waarin verschilt ouderdomsvergeetachtigheid van dementie?",
       ["Bij vergeetachtigheid leid je je leven gewoon verder",
        "Vergeetachtigheid komt alleen voor bij jonge volwassenen",
        "Dementie gaat na enkele weken vanzelf weer helemaal over",
        "Er is geen verschil, het zijn twee woorden voor hetzelfde"],
       0,
       "Wie vergeetachtig is, vergeet soms iets maar functioneert verder. Dementie is een ziekte die het dagelijks leven steeds meer verstoort."),
    tabel(
        "Klopt dit over respectvol omgaan en rapporteren?",
        [
            ("Interne rapportering blijft binnen de eigen werking.", J),
            ("Informatie over een kind deel je met iedereen die ernaar vraagt.", F),
            ("Gevoelige onderwerpen vermijd je het best helemaal.", F),
        ],
        "Informatie deel je alleen met wie ze nodig heeft voor de zorg. Een gevoelig onderwerp benader je met respect, je vermijdt het niet."),
    keuze(
        "Een peergroep bestaat uit [[*leeftijdsgenoten|familieleden]]. Als vrienden je aanzetten om meer te studeren, is dat [[*positieve|negatieve]] groepsdruk.",
        "Een peergroep is een groep leeftijdsgenoten. Groepsdruk kan ook goede gevolgen hebben."),
    sleep(
        "Snel en juist reageren op de signalen van een baby heet [[sensitieve responsiviteit]]. Angst voor vreemden begint meestal rond [[acht maanden]].",
        ["drie jaar", "gewenning"],
        "Sensitieve responsiviteit legt de basis voor een veilige gehechtheid. Rond acht maanden herkent een baby wie vreemd is."),
    mk("Waarom bied je in een kinderopvang verschillende soorten activiteiten aan?",
       ["Zo spreek je meer ervaringsgebieden en interesses aan",
        "Zo hoeven de kinderen nooit meer zelf te kiezen wat ze doen",
        "Zo is er helemaal geen tijd meer over voor vrij spel tussendoor",
        "Zo leren alle kinderen precies hetzelfde op hetzelfde moment"],
       0,
       "Elk kind is anders. Met een gevarieerd aanbod komen beweging, expressie, taal en samenspel allemaal aan bod."),

    casus(
        "In een woonzorgcentrum heeft mevrouw Peeters (82) last van haar handen. Ze knoopt haar bloes niet meer zelf dicht. Ze zit vaak alleen op haar kamer en zegt: 'Ik doe er toch niet meer toe.' Haar dochter komt elke dag na het werk langs en zorgt ook nog voor haar eigen kinderen.",
        [
            mk("Welke activiteit past het best om de handen van mevrouw Peeters soepel te houden?",
               ["Een functiebehoudende activiteit met haar handen",
                "Een activiteit die iets volledig nieuws aanleert",
                "Een activiteit waar ze enkel naar kijkt, zonder doen",
                "Geen activiteit, zodat haar handen rusten"],
               0,
               "Een functiebehoudende activiteit houdt in stand wat iemand nog kan."),
            tabel(
                "Klopt dit over de casus?",
                [
                    ("De dochter hoort bij de sandwichgeneratie.", J),
                    ("Mevrouw Peeters heeft nood aan sociaal contact en erkenning.", J),
                    ("Haar bloes zelf dichtknopen is een vrijetijdsactiviteit.", F),
                ],
                "De dochter zorgt voor haar moeder en haar kinderen. 'Ik doe er niet meer toe' wijst op een tekort aan contact en erkenning. Aankleden is een ADL-activiteit."),
        ]),

    open_("Beschrijf een activiteit die je met mevrouw Peeters en twee andere bewoners kan doen. Leg uit aan welke behoefte ze tegemoetkomt en hoe je zorgt dat het veilig en haalbaar blijft.",
          "Ik bak samen met mevrouw Peeters en twee andere bewoners koekjes. Ze werkt het deeg met haar handen, wat die soepel houdt, en ze praat met de anderen. Zo kom ik tegemoet aan haar behoefte aan sociaal contact en erkenning, want het resultaat delen we in de leefruimte. Ik kies een stevige tafel, zet het materiaal binnen handbereik en neem zelf de oven voor mijn rekening.",
          "Een goed antwoord beschrijft een concrete activiteit, koppelt die aan een behoefte (sociaal contact, erkenning, functiebehoud) en noemt een maatregel voor veiligheid of haalbaarheid."),
]
