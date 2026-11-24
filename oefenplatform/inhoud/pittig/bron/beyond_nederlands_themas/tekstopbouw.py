"""Tekstopbouw, alineaverbanden en structuuraanduiders — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST = (
    "Lees de tekst.\n\n"
    "[A] Steeds meer steden voeren een zone in waar oude, vervuilende wagens niet meer binnen mogen. Is dat een goed idee?\n\n"
    "[B] De lucht in die steden wordt er aantoonbaar schoner door. Bewoners krijgen minder vaak last van hun luchtwegen, "
    "vooral kinderen en ouderen. Bovendien wordt het centrum stiller.\n\n"
    "[C] Daar staat tegenover dat mensen met een klein inkomen vaak net een oude wagen rijden. Zij kunnen zich geen nieuwe veroorloven "
    "en raken zo moeilijker in de stad.\n\n"
    "[D] Om dat op te vangen, geven sommige steden een premie aan wie zijn oude wagen inruilt voor een fiets of een abonnement op de bus.\n\n"
    "[E] Een zone voor schone lucht werkt dus, op voorwaarde dat de stad ook aan wie het minder breed heeft denkt."
)

VRAGEN = [
    casus(
        TEKST,
        [
            tabel(
                "Welk deel van de IMS-structuur is elke alinea?",
                [
                    ("[A]", "Inleiding"),
                    ("[C]", "Midden"),
                    ("[E]", "Slot"),
                ],
                "De inleiding zet het onderwerp neer met een vraag, het midden werkt uit, het slot besluit.",
                kolommen=["Inleiding", "Midden", "Slot"],
            ),
            mk(
                "Welk verband legt [C] met [B]?",
                ["Tegenstellend", "Chronologisch", "Voorwaardelijk", "Concluderend"],
                0,
                "\"Daar staat tegenover\" zet een tegengewicht naast de voordelen.",
            ),
            mk(
                "Welk verband legt [D] met [C]?",
                ["Doel-middel", "Oorzakelijk", "Vergelijkend", "Chronologisch"],
                0,
                "\"Om dat op te vangen\" noemt het doel, de premie is het middel.",
            ),
            keuze(
                "Het woord \"Zij\" in [C] verwijst naar [[*mensen met een klein inkomen|de steden|de oude wagens]].",
                "Verwijswoorden slaan terug op iets wat eerder genoemd werd.",
            ),
            tabel(
                "Welk soort structuuraanduider is elk woord?",
                [
                    ("Bovendien [B]", "Signaalwoord"),
                    ("dus [E]", "Signaalwoord"),
                    ("Zij [C]", "Verwijswoord"),
                    ("dat [D]", "Verwijswoord"),
                ],
                "Signaalwoorden geven de gedachtegang aan, verwijswoorden knopen zinnen aan elkaar.",
                kolommen=["Signaalwoord", "Verwijswoord"],
            ),
            mk(
                "Welke vaste tekststructuur volgt de tekst als geheel het best?",
                [
                    "De evaluatiestructuur",
                    "De handelingsstructuur",
                    "De ontwikkelingsstructuur",
                    "De onderzoeksstructuur",
                ],
                0,
                "Voordelen en nadelen worden afgewogen tot een oordeel: werkt, op voorwaarde dat...",
            ),
            keuze(
                "In [E] wijst \"op voorwaarde dat\" op een [[*voorwaardelijk|chronologisch|vergelijkend]] verband.",
                "Het besluit geldt alleen als er iets aan voldaan is.",
            ),
        ],
    ),
    tabel(
        "Welk verband geeft elk signaalwoord aan?",
        [
            ("want", "Redengevend"),
            ("daarentegen", "Tegenstellend"),
            ("ten eerste", "Opsommend"),
            ("daarom", "Concluderend"),
        ],
        "Signaalwoorden geven een signaal over wat er komt.",
        kolommen=["Redengevend", "Tegenstellend", "Opsommend", "Concluderend"],
    ),
    koppel(
        "Welke vaste tekststructuur past bij elke tekst?",
        [
            ["een recept voor pannenkoeken", "Handelingsstructuur"],
            ["elektrische en benzinewagens naast elkaar op prijs en verbruik", "Vergelijkingsstructuur"],
            ["hoe het openbaar vervoer in vijftig jaar veranderde", "Ontwikkelingsstructuur"],
            ["een verslag met vraag, methode, resultaten en besluit", "Onderzoeksstructuur"],
        ],
        ["Alfabetstructuur", "Rijmstructuur"],
        "Negen vaste structuren; elk volgt een herkenbaar patroon.",
    ),
    casus(
        "Een tekst over plastic in zee heeft deze tussentitels:\n\n1. Een soep van plastic\n2. Hoe komt het daar?\n3. Wat kunnen overheden doen?",
        [
            mk(
                "Welke vaste structuur herken je?",
                [
                    "De probleemstructuur",
                    "De onderzoeksstructuur",
                    "De vergelijkingsstructuur",
                    "De handelingsstructuur",
                ],
                0,
                "Probleem, oorzaken, oplossingen.",
            ),
            keuze(
                "Als deel 3 eindigt bij wat de overheid moet doen en wie dat betaalt, schuift de tekst op naar de [[*maatregelstructuur|evaluatiestructuur|ontwikkelingsstructuur]].",
                "Eén tekst kan meer dan één structuur bevatten.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over tekstopbouw?",
        [
            ("Eén alinea behandelt één deelonderwerp.", J),
            ("Een tekst kan maar één vaste structuur bevatten.", F),
            ("Een goede lay-out garandeert een goede inhoud.", F),
            ("Hetzelfde signaalwoord kan twee verbanden aangeven.", J),
        ],
        "\"Dan\" kan chronologisch zijn of voorwaardelijk.",
    ),
    sorteer(
        "Chronologisch of voorwaardelijk gebruik van \"dan\"?",
        ["Chronologisch", "Voorwaardelijk"],
        [
            ["Eerst at hij, dan vertrok hij.", "Chronologisch"],
            ["Als het regent, dan blijven we thuis.", "Voorwaardelijk"],
            ["Ze opende de deur en dan zag ze het.", "Chronologisch"],
            ["Wie niet betaalt, die mag dan niet mee.", "Voorwaardelijk"],
        ],
        "Hetzelfde woord, twee verbanden.",
    ),
    mk(
        "Je wil snel weten of een lange tekst nuttig is voor je onderzoek. Wat lees je zeker niet eerst?",
        [
            "Het midden, zin voor zin",
            "De titel en de tussentitels",
            "De eerste alinea van de tekst",
            "Het slot met het besluit",
        ],
        0,
        "Titel, tussentitels, inleiding en slot geven in enkele minuten de kern.",
    ),
    tabel(
        "Welke conventie hoort bij een formele e-mail?",
        [
            ("een duidelijke onderwerpregel", J),
            ("een gepaste aanspreking", J),
            ("een knipogende smiley", F),
            ("correcte spelling en interpunctie", J),
        ],
        "Elke tekstsoort heeft conventies. Een smiley hoort bij informele communicatie.",
    ),
    volgorde(
        "Zet de delen van een argumentatieve tekst in de gebruikelijke volgorde.",
        [
            "Het standpunt wordt ingeleid",
            "De argumenten worden gegeven",
            "Tegenargumenten worden weerlegd",
            "De conclusie volgt",
        ],
        "Stelling, argumenten, tegenargumenten en conclusie.",
    ),
    mk(
        "Een alinea begint met \"Daardoor stegen de prijzen.\" Welk verband legt die zin met de vorige alinea?",
        ["Oorzakelijk", "Tegenstellend", "Opsommend", "Vergelijkend"],
        0,
        "\"Daardoor\" noemt een gevolg van wat ervoor stond.",
    ),
    tabel(
        "Een tekst over jeugdwerkloosheid bevat een foto van één jongere die op straat slaapt. Klopt dit?",
        [
            ("De foto kan de boodschap versterken.", J),
            ("De foto kan de conclusie van de lezer sturen.", J),
            ("Een foto verandert nooit hoe je een tekst leest.", F),
        ],
        "Een foto van het ergste geval stuurt je conclusie, zonder dat er een woord verandert.",
    ),
    sleep(
        "Tussentitels maken een tekst [[toegankelijker]]. Een witregel tussen alinea's toont waar een nieuwe [[gedachte]] begint. Wie de opbouw herkent, volgt de tekst [[sneller]].",
        ["langer", "moeilijker"],
        "Opbouw helpt de lezer.",
    ),
    keuze(
        "Een inleiding die met een vraag begint, zoals \"Is dat een goed idee?\", wil vooral [[*interesse wekken|het besluit geven|een bron vermelden]].",
        "De inleiding zet het onderwerp neer en maakt je nieuwsgierig naar het midden.",
    ),
    casus(
        "Lees de tekst.\n\n"
        "In 1817 bouwde Karl von Drais een loopfiets zonder trappers. Rond 1860 kwamen er trappers op het voorwiel. "
        "Later, in de jaren 1880, verscheen de fiets met een ketting naar het achterwiel, zoals we die nu kennen. "
        "Sindsdien veranderde vooral het materiaal: vandaag rijden we op aluminium, carbon en zelfs met een motortje.",
        [
            mk(
                "Welke vaste structuur volgt de tekst?",
                [
                    "De ontwikkelingsstructuur",
                    "De argumentatiestructuur",
                    "De probleemstructuur van een tekst",
                    "De evaluatiestructuur",
                ],
                0,
                "De tekst volgt hoe iets in de loop van de tijd evolueert.",
            ),
            tabel(
                "Welke woorden tonen het chronologische verband?",
                [
                    ("In 1817", J),
                    ("Later", J),
                    ("Sindsdien", J),
                    ("zelfs", F),
                ],
                "Tijdsaanduidingen zetten de alinea's op de tijdlijn. \"Zelfs\" versterkt alleen.",
            ),
            keuze(
                "\"Sindsdien\" verwijst terug naar [[*de jaren 1880|1817|vandaag]].",
                "Ook een woord als sindsdien knoopt aan bij wat ervoor stond.",
            ),
        ],
    ),
    mk(
        "Een recensie van een restaurant weegt het eten, de bediening en de prijs af en eindigt met drie sterren. Welke structuur is dat?",
        [
            "De evaluatiestructuur",
            "De verklaringsstructuur",
            "De maatregelstructuur",
            "De handelingsstructuur",
        ],
        0,
        "Een evaluatie beoordeelt aan de hand van criteria en komt tot een oordeel.",
    ),
    tabel(
        "Is dit een verband tussen alinea's?",
        [
            ("oorzakelijk", J),
            ("voordelen-nadelen", J),
            ("alfabetisch", F),
            ("doel-middel", J),
        ],
        "Alfabetisch is een ordening van een lijst, geen verband tussen gedachten.",
    ),
    mk(
        "Een handleiding nummert haar stappen met \"ten eerste, ten tweede, tot slot\". Waarom?",
        [
            "De volgorde van de stappen is de inhoud",
            "Het maakt de tekst langer en dus duidelijker",
            "Het is een verplichte conventie bij elke tekst",
            "Het wijst op een tegenstelling tussen stappen",
        ],
        0,
        "Bij een instructie moet de volgorde ondubbelzinnig zijn.",
    ),
    tabel(
        "Een tekst legt uit waarom de zee zout is, zonder er een oordeel over te geven. Klopt dit?",
        [
            ("Hij volgt de verklaringsstructuur.", J),
            ("Hij volgt de argumentatiestructuur.", F),
            ("Hij kan signaalwoorden als doordat en daardoor bevatten.", J),
        ],
        "De verklaringsstructuur legt uit hoe of waarom iets zo is.",
    ),
    mk(
        "Een tekst zonder enige witregel of alinea. Wat is het grootste nadeel voor de lezer?",
        [
            "Hij ziet niet waar een gedachte begint",
            "De tekst bevat dan minder informatie",
            "De tekst kan dan geen slot hebben",
            "De schrijver mag dan geen signaalwoorden gebruiken",
        ],
        0,
        "Zonder alinea's moet de lezer zelf uitzoeken waar een gedachte begint en eindigt.",
    ),
    inv(
        "Verwijswoorden en signaalwoorden heten samen ... Antwoord met één woord.",
        ["structuuraanduiders", "structuuraanduider"],
        "Ze maken de opbouw en de gedachtegang van een tekst zichtbaar.",
    ),
    open_(
        "Schrijf een korte alinea van drie zinnen over smartphones op school. Gebruik een tegenstellend en een concluderend signaalwoord en onderstreep ze in gedachten.",
        "Smartphones helpen leerlingen om snel iets op te zoeken. Toch leiden meldingen tijdens de les vaak af. Daarom kiezen veel scholen voor een gsm-vrije les met af en toe een opdracht op de telefoon.",
    ),
]
