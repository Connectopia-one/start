"""Klanken, spelling, diakritische tekens en interpunctie — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lees de mail. Er staan fouten in.\n\n"
        "\"Beste mevrouw,\n"
        "Vorige week (1) antwoorde ik op uw vraag over de uitstap. Wat er (2) gebeurt is, vind ik spijtig. "
        "Mijn zoon (3) word die dag twaalf en hij had zich er erg op verheugd. Ik hoop dat de school dit in (4) Januari opnieuw organiseert.\n"
        "Met vriendelijke groeten\"",
        [
            tabel(
                "Wat is de juiste vorm?",
                [
                    ("(1)", "antwoordde"),
                    ("(2)", "gebeurd"),
                    ("(3)", "wordt"),
                ],
                "Verleden tijd: stam antwoord + de. Voltooid deelwoord van gebeuren: gebeurd. Stam word + t bij hij.",
                kolommen=["antwoordde", "gebeurd", "wordt"],
            ),
            keuze(
                "Bij (4) schrijf je [[*januari|Januari|JANUARI]].",
                "Namen van maanden krijgen in het Nederlands een kleine letter.",
            ),
            mk(
                "Waarom gaan zulke fouten vaak mis?",
                [
                    "Je hoort het verschil niet",
                    "De regels zijn elk jaar anders",
                    "Woorden hebben geen stam",
                    "Mails volgen andere spellingregels",
                ],
                0,
                "Wie schrijft wat hij hoort, maakt fouten. De regel moet het gehoor overrulen.",
            ),
        ],
    ),
    tabel(
        "Kies de juiste vorm.",
        [
            ("Hij (verbrand / verbrandt) de oude brieven.", "verbrandt"),
            ("Ze heeft de brieven (verbrand / verbrandt).", "verbrand"),
            ("Ik (verwacht / verwachtt) je om acht uur.", "verwacht"),
        ],
        "Tegenwoordige tijd bij hij: stam + t. Voltooid deelwoord van verbranden: verbrand. Bij ik: de kale stam.",
        kolommen=["verbrandt", "verbrand", "verwacht"],
    ),
    tabel(
        "Kies de juiste verleden tijd.",
        [
            ("werken", "werkte"),
            ("reizen", "reisde"),
            ("praten", "praatte"),
            ("bouwen", "bouwde"),
        ],
        "Eindigt de stam op een scherpe medeklinker, dan komt er te bij. Bij reizen telt de z van de infinitief: reisde.",
        kolommen=["werkte", "reisde", "praatte", "bouwde"],
    ),
    mk(
        "Wat is de stam van \"verhuizen\"?",
        ["verhuis", "verhuiz", "verhuisz", "verhuize"],
        0,
        "Verhuizen min en geeft verhuiz, maar aan het eind van een woord wordt de z een s.",
    ),
    tabel(
        "Hoofdletter of niet?",
        [
            ("de Franse kaas", "Hoofdletter"),
            ("op maandag", "Kleine letter"),
            ("in de stad Gent", "Hoofdletter"),
            ("in december", "Kleine letter"),
        ],
        "Taal-, land- en stadsnamen krijgen een hoofdletter, ook als bijvoeglijk naamwoord. Weekdagen en maanden niet.",
        kolommen=["Hoofdletter", "Kleine letter"],
    ),
    koppel(
        "Welk teken hoort bij elk voorbeeld?",
        [
            ["ruïne", "Trema"],
            ["zo'n", "Apostrof"],
            ["Noord-Frankrijk", "Koppelteken"],
            ["café", "Accent"],
        ],
        ["Dubbele punt", "Spatie"],
        "Diakritische tekens veranderen de lezing van een woord.",
    ),
    tabel(
        "Juist of fout geschreven?",
        [
            ("auto's", J),
            ("foto's", J),
            ("tafel's", F),
            ("'s avonds", J),
        ],
        "Na een lange enkele klinker komt een apostrof voor de meervouds-s; tafels krijgt gewoon een s.",
    ),
    casus(
        "Lees de twee zinnen.\n\n"
        "A. \"We eten, opa.\"\n"
        "B. \"We eten opa.\"",
        [
            mk(
                "Wat toont dit voorbeeld?",
                [
                    "Leestekens bepalen mee de betekenis",
                    "Komma's zijn louter versiering in een zin",
                    "Zin B is grammaticaal onmogelijk",
                    "Een komma verandert enkel de klank",
                ],
                0,
                "Eén komma scheelt een mensenleven.",
            ),
            keuze(
                "In zin A spreekt de spreker opa [[*aan|niet aan|met een uitroep aan]].",
                "De komma scheidt de aanspreking van de rest van de zin.",
            ),
        ],
    ),
    mk(
        "In welke zin staat de komma correct?",
        [
            "Toen de bel ging, liep iedereen naar buiten.",
            "Toen de bel ging liep, iedereen naar buiten.",
            "Toen, de bel ging liep iedereen naar buiten.",
            "Toen de bel, ging liep iedereen naar buiten.",
        ],
        0,
        "Na een bijzin die vooraan staat, komt een komma.",
    ),
    tabel(
        "Waarvoor dient elk leesteken?",
        [
            ("Er volgen drie punten: prijs, kwaliteit en service.", "Dubbele punt"),
            ("Ze zei: \"Ik kom morgen.\"", "Aanhalingsteken"),
            ("Kom je ook?", "Vraagteken"),
        ],
        "De dubbele punt kondigt een opsomming aan, aanhalingstekens tonen een citaat.",
        kolommen=["Dubbele punt", "Aanhalingsteken", "Vraagteken"],
    ),
    sorteer(
        "Lange of korte klinker?",
        ["Lang", "Kort"],
        [
            ["maan", "Lang"],
            ["pit", "Kort"],
            ["zeep", "Lang"],
            ["bok", "Kort"],
            ["deur", "Lang"],
        ],
        "Maan, zeep en deur hebben een lang klinkend geluid.",
    ),
    keuze(
        "In \"dat is één keer te veel\" dient het accent om [[*nadruk te leggen|de klinker te splitsen|een letter weg te laten]].",
        "Zo lees je het getal en niet het lidwoord.",
    ),
    tabel(
        "Klopt dit over spelling en leestekens?",
        [
            ("Spelling volgt altijd precies de uitspraak.", F),
            ("Een trema en een accent zijn hetzelfde teken.", F),
            ("De spatie telt als interpunctieteken.", J),
            ("Hond wordt met een d geschreven, al klinkt hij met een t.", J),
        ],
        "Klankbeeld en schriftbeeld lopen vaak uiteen.",
    ),
    mk(
        "Hoe schrijf je het voltooid deelwoord van \"beantwoorden\"?",
        ["beantwoord", "beantwoordt", "beantwoordd", "gebeantwoord"],
        0,
        "De stam beantwoord eindigt al op een d, dus er komt geen tweede bij. Be- krijgt geen ge-.",
    ),
    sleep(
        "In \"geïnteresseerd\" staat een [[trema]] op de i. De onbeklemtoonde e in \"gemeente\" heet de [[doffe]] klank. \"Zo'n\" bevat een [[apostrof]].",
        ["accent", "koppelteken"],
        "Drie tekens en klanken.",
    ),
    casus(
        "Lees de zin uit een verslag.\n\n"
        "\"Na de vergadering (1) besprak / bespraakt de directeur de cijfers. Ze (2) zijn / zijnd erg (3) tegengevallen / tegengevald. "
        "Daarom (4) heeft / heefd het team een nieuw plan (5) bedacht / bedachd.\"",
        [
            tabel(
                "Welke vorm is juist?",
                [
                    ("(1)", "besprak"),
                    ("(3)", "tegengevallen"),
                    ("(5)", "bedacht"),
                ],
                "Sterke werkwoorden veranderen van klinker; bedenken heeft het voltooid deelwoord bedacht.",
                kolommen=["besprak", "tegengevallen", "bedacht"],
            ),
            keuze(
                "Bij (4) schrijf je [[*heeft|heefd|heeftt]].",
                "Hebben is onregelmatig: hij heeft.",
            ),
        ],
    ),
    tabel(
        "Gebruik je hier een koppelteken?",
        [
            ("Zuid-Afrika", J),
            ("zee-eend", J),
            ("twee-eiig", J),
            ("de-auto", F),
        ],
        "Bij eigennamen, botsende klinkers en woordgroepen als twee-eiig. Tussen lidwoord en naamwoord nooit.",
    ),
    mk(
        "Welk woord heeft een vast woordbeeld?",
        ["tafel", "lopen", "werken", "schrijven"],
        0,
        "Werkwoorden veranderen bij de vervoeging; een naamwoord als tafel blijft gelijk.",
    ),
    tabel(
        "Een formele brief. Klopt dit over interpunctie?",
        [
            ("Je past de leestekens zorgvuldig toe.", J),
            ("Uitroeptekens gebruik je spaarzaam.", J),
            ("Komma's zet je waar je ademhaalt.", F),
        ],
        "Spelling en leestekens zijn een apart beoordelingscriterium.",
    ),
    inv(
        "Schrijf de tegenwoordige tijd van \"vinden\" bij \"zij\" (enkelvoud): zij ...",
        ["vindt"],
        "Stam vind + t.",
    ),
    inv(
        "Schrijf de verleden tijd enkelvoud van \"leven\": hij ...",
        ["leefde"],
        "Bij leven telt de v van de infinitief: leefde, niet leefte.",
    ),
    keuze(
        "De letters a, e, i, o en u zijn [[*klinkers|medeklinkers|diakritische tekens]].",
        "Alle andere letters zijn medeklinkers; de y zit ertussenin.",
    ),
    mk(
        "Waarom krijgt \"oma\" in het meervoud een apostrof?",
        [
            "Anders lees je de a kort",
            "Alle familienamen krijgen er een",
            "Het woord komt uit het Frans",
            "Het is een samenstelling",
        ],
        0,
        "Omas zou je als oh-mas met korte a lezen; oma's bewaart de lange klank.",
    ),
    tabel(
        "Welk teken staat erin?",
        [
            ("geïnteresseerd", "Trema"),
            ("'s morgens", "Apostrof"),
            ("scène", "Accent"),
        ],
        "Elk teken stuurt de lezing anders.",
        kolommen=["Trema", "Apostrof", "Accent"],
    ),
    tabel(
        "Welk leesteken sluit de zin af?",
        [
            ("Wat een prachtige dag", "Uitroepteken"),
            ("Hoe laat begint de film", "Vraagteken"),
            ("De film begint om acht uur", "Punt"),
        ],
        "Een punt sluit een mededelende zin af, een vraagteken een vraag, een uitroepteken een uitroep.",
        kolommen=["Punt", "Vraagteken", "Uitroepteken"],
    ),
    open_(
        "Schrijf een zin waarin je \"word\" en \"wordt\" allebei correct gebruikt, en leg de regel uit.",
        "\"Ik word morgen achttien en mijn broer wordt volgende week twintig.\" Bij ik schrijf je de kale stam (word); bij hij of een zelfstandig naamwoord komt er een t bij de stam (wordt).",
    ),
]
