"""Morfologie: samenstellingen, afleidingen en werkwoordstijden — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    tabel(
        "Samenstelling of afleiding?",
        [
            ("tandarts", "Samenstelling"),
            ("vriendelijk", "Afleiding"),
            ("boekenkast", "Samenstelling"),
            ("onmogelijk", "Afleiding"),
            ("leesbaar", "Afleiding"),
        ],
        "Een samenstelling bestaat uit zelfstandige woorden; bij een afleiding is minstens één deel een voor- of achtervoegsel.",
        kolommen=["Samenstelling", "Afleiding"],
    ),
    casus(
        "Je leest het woord \"onbetaalbaarheid\" voor het eerst.",
        [
            volgorde(
                "Zet de delen van het woord in de juiste volgorde.",
                ["on", "betaal", "baar", "heid"],
                "Voorvoegsel, grondwoord en twee achtervoegsels.",
            ),
            tabel(
                "Wat doet elk deel?",
                [
                    ("on-", "Keert de betekenis om"),
                    ("-baar", "Maakt er een bijvoeglijk naamwoord van"),
                    ("-heid", "Maakt er een zelfstandig naamwoord van"),
                ],
                "Achtervoegsels veranderen vaak de woordsoort.",
                kolommen=["Keert de betekenis om", "Maakt er een bijvoeglijk naamwoord van", "Maakt er een zelfstandig naamwoord van"],
            ),
            mk(
                "Wat betekent het woord?",
                [
                    "Het niet te betalen zijn",
                    "Iemand die niet betaalt",
                    "Een betaling die te laat is",
                    "Het opnieuw betalen van iets",
                ],
                0,
                "Wie het woord ontleedt, raadt de betekenis zonder woordenboek.",
            ),
        ],
    ),
    tabel(
        "In welke tijd staat elke zin?",
        [
            ("Hij werkt.", "OTT"),
            ("Hij heeft gewerkt.", "VTT"),
            ("Hij werkte.", "OVT"),
            ("Hij had gewerkt.", "VVT"),
        ],
        "Onvoltooid of voltooid, tegenwoordig of verleden.",
        kolommen=["OTT", "VTT", "OVT", "VVT"],
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"(1) Sara stapt de klas binnen. (2) Iedereen kijkt op. (3) Gisteren had ze haar toets vergeten. "
        "(4) Vandaag zal ze alles uitleggen. (5) 'Ga zitten,' zegt de leraar.\"",
        [
            tabel(
                "In welke tijd of wijs staat het werkwoord?",
                [
                    ("(1) stapt", "OTT"),
                    ("(3) had vergeten", "VVT"),
                    ("(4) zal uitleggen", "OTKT"),
                    ("(5) Ga", "Imperatief"),
                ],
                "OTT is de onvoltooid tegenwoordige, OTKT de onvoltooid toekomende tijd (zullen plus infinitief). De kale stam als bevel is de imperatief.",
                kolommen=["OTT", "VVT", "OTKT", "Imperatief"],
            ),
            mk(
                "Waarom staat zin 3 in de voltooid verleden tijd?",
                [
                    "Het gebeurde vóór het vertelde moment",
                    "Het gebeurt op dit eigenste moment in de klas",
                    "Het zal pas later gebeuren",
                    "Het is een bevel aan Sara",
                ],
                0,
                "De vvt plaatst iets nog verder terug dan het verleden van het verhaal.",
            ),
            keuze(
                "Het verhaal staat grotendeels in de tegenwoordige tijd. Dat voelt [[*nabij|afstandelijk|formeel]].",
                "De tijd stuurt hoe de lezer de gebeurtenis plaatst.",
            ),
        ],
    ),
    tabel(
        "Sterk of zwak werkwoord?",
        [
            ("zingen: zong, gezongen", "Sterk"),
            ("werken: werkte, gewerkt", "Zwak"),
            ("lopen: liep, gelopen", "Sterk"),
            ("bouwen: bouwde, gebouwd", "Zwak"),
        ],
        "Een sterk werkwoord verandert van klinker; een zwak krijgt -te of -de.",
        kolommen=["Sterk", "Zwak"],
    ),
    koppel(
        "Welk meervoud of verkleinwoord is juist?",
        [
            ["kind", "kinderen"],
            ["stad", "steden"],
            ["koning (verkleinwoord)", "koninkje"],
            ["bloem (verkleinwoord)", "bloempje"],
        ],
        ["kinds", "koningje"],
        "Een kleine groep woorden krijgt -eren; na ng wordt het verkleinwoord -kje.",
    ),
    tabel(
        "Klopt dit over morfologie?",
        [
            ("Een verkleinwoord is altijd onzijdig.", J),
            ("Elk meervoud wordt gevormd met -en of -s.", F),
            ("Een samenstelling kan uit drie woorden bestaan.", J),
            ("Verbuiging slaat op werkwoorden.", F),
        ],
        "Werkwoorden vervoeg je, naamwoorden verbuig je.",
    ),
    sorteer(
        "Is het een tussenletter of niet?",
        ["Met tussenletter", "Zonder tussenletter"],
        [
            ["pannenkoek", "Met tussenletter"],
            ["zonnebloem", "Met tussenletter"],
            ["tafelpoot", "Zonder tussenletter"],
            ["deurklink", "Zonder tussenletter"],
        ],
        "De tussenklank verbindt twee delen; in het schrift heet ze de tussenletter.",
    ),
    mk(
        "\"Hij belt zijn moeder op.\" Wat gebeurt er met het werkwoord \"opbellen\"?",
        [
            "Het valt uiteen in twee delen",
            "Het krijgt een tussenletter",
            "Het wordt een sterk werkwoord",
            "Het verandert in een afleiding",
        ],
        0,
        "Een scheidbaar werkwoord: het voorvoegsel schuift naar achteren.",
    ),
    keuze(
        "Bij \"een groot huis\" maar \"het grote huis\" zie je een [[*verbuiging|vervoeging|afleiding]] van het bijvoeglijk naamwoord.",
        "De extra e is een verbuiging.",
    ),
    tabel(
        "Te of de in de verleden tijd?",
        [
            ("maken", "te"),
            ("horen", "de"),
            ("fietsen", "te"),
            ("leven", "de"),
        ],
        "Eindigt de stam op een scherpe medeklinker, dan komt er -te bij; anders -de. Bij leven telt de v.",
        kolommen=["te", "de"],
    ),
    mk(
        "Welk woord is géén afleiding?",
        ["huisdeur", "waarheid", "ongezond", "verwerking"],
        0,
        "Huisdeur bestaat uit twee zelfstandige woorden: een samenstelling.",
    ),
    sleep(
        "Het deel na de stam heet de [[uitgang]]. De gebiedende wijs heet ook [[imperatief]] en bestaat uit de kale [[stam]].",
        ["infinitief", "tussenklank"],
        "Stam, uitgang en imperatief.",
    ),
    mk(
        "Waarom is het werkwoord \"zijn\" lastig?",
        [
            "Het volgt de gewone regels niet",
            "Het heeft geen voltooid deelwoord",
            "Het bestaat niet in de verleden tijd",
            "Het is altijd een koppelwerkwoord",
        ],
        0,
        "Ben, is, was, waren, geweest: er valt weinig regel in te ontdekken.",
    ),
    casus(
        "Vergelijk: \"het huis\" en \"het huisje\", \"de tafel\" en \"het tafeltje\", \"de bloem\" en \"het bloempje\".",
        [
            mk(
                "Wat valt op aan het lidwoord?",
                [
                    "Een verkleinwoord krijgt altijd het",
                    "Het lidwoord blijft altijd gelijk",
                    "Een verkleinwoord krijgt altijd de",
                    "Verkleinwoorden hebben geen lidwoord",
                ],
                0,
                "Een verkleinwoord is altijd onzijdig.",
            ),
            keuze(
                "Het verkleinwoord van \"boom\" is [[*boompje|boomje|boomtje]].",
                "Na een lange klinker plus m komt -pje.",
            ),
        ],
    ),
    tabel(
        "Welk voltooid deelwoord is juist?",
        [
            ("verwachten", "verwacht"),
            ("gebeuren", "gebeurd"),
            ("zingen", "gezongen"),
        ],
        "Ver- krijgt geen ge-; gebeuren krijgt een d; zingen is sterk.",
        kolommen=["verwacht", "gebeurd", "gezongen"],
    ),
    mk(
        "In welke tijd staat \"Wij dachten aan jou\"?",
        [
            "Onvoltooid verleden tijd",
            "Voltooid verleden tijd",
            "Voltooid tegenwoordige tijd",
            "Onvoltooid toekomende tijd",
        ],
        0,
        "Dachten is één werkwoordsvorm in het verleden, zonder hulpwerkwoord.",
    ),
    tabel(
        "Welk achtervoegsel maakt welke woordsoort?",
        [
            ("-heid (vrijheid)", "Zelfstandig naamwoord"),
            ("-baar (leesbaar)", "Bijvoeglijk naamwoord"),
            ("-er (werker)", "Zelfstandig naamwoord"),
            ("-lijk (vriendelijk)", "Bijvoeglijk naamwoord"),
        ],
        "Achtervoegsels veranderen vaak de woordsoort van het grondwoord.",
        kolommen=["Zelfstandig naamwoord", "Bijvoeglijk naamwoord"],
    ),
    inv(
        "Schrijf de imperatief van \"luisteren\": ...!",
        ["luister", "Luister"],
        "De imperatief is de kale stam.",
    ),
    mk(
        "Een leerling schrijft \"hij antwoord\". Wat liep er mis?",
        [
            "Hij vergat de t na de stam",
            "Hij koos het verkeerde lidwoord bij het werkwoord",
            "Hij schreef het werkwoord in de verleden tijd",
            "Hij gebruikte een sterk werkwoord als zwak werkwoord",
        ],
        0,
        "Stam antwoord plus t bij hij: hij antwoordt.",
    ),
    tabel(
        "Kan je het woord nog verder ontleden in betekenisvolle delen?",
        [
            ("kinderfietsbel", J),
            ("onvriendelijkheid", J),
            ("tafel", F),
        ],
        "Tafel is een grondwoord; de andere bestaan uit meerdere delen.",
    ),
    keuze(
        "\"Zij liepen naar huis\" staat in de [[*onvoltooid verleden tijd|voltooid verleden tijd|onvoltooid tegenwoordige tijd]].",
        "Het gebeurde in het verleden en wordt niet als afgerond voorgesteld.",
    ),
    tabel(
        "Vervoeging of verbuiging?",
        [
            ("ik werk, hij werkt", "Vervoeging"),
            ("groot, grote", "Verbuiging"),
            ("ik liep, wij liepen", "Vervoeging"),
        ],
        "Werkwoorden vervoeg je, naamwoorden en bijvoeglijke naamwoorden verbuig je.",
        kolommen=["Vervoeging", "Verbuiging"],
    ),
    inv(
        "Een deel dat achteraan aan een woord geplakt wordt om een nieuw woord te maken, zoals -heid, heet een ... Antwoord met één woord.",
        ["achtervoegsel", "suffix"],
        "Een voorvoegsel staat vooraan, een achtervoegsel achteraan.",
    ),
    open_(
        "Zet de zin \"Ik schrijf een brief\" in de voltooid tegenwoordige, de onvoltooid verleden en de onvoltooid toekomende tijd.",
        "Voltooid tegenwoordig: ik heb een brief geschreven. Onvoltooid verleden: ik schreef een brief. Onvoltooid toekomend: ik zal een brief schrijven.",
    ),
]
