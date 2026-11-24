"""Redeneren met bronnen: bruikbaarheid en betrouwbaarheid — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

PRENTEN = [
    dict(bestand="betoging-van-bovenaf.svg", zelf=True,
         wat="Eigen tekening: een plein van bovenaf met verspreide betogers en één drukke hoek (Beyond doorstroom).",
         vragen="klikvraag over een bijgesneden beeld"),
]

VRAGEN = [
    # --- soorten
    tabel(
        "Je onderzoekt de staking in een Gentse spinnerij in 1905. Primaire of secundaire bron?",
        [
            ("Een brief van een staker uit 1905", "Primair"),
            ("Een handboek geschiedenis uit 2015", "Secundair"),
            ("Het loonregister van de spinnerij uit 1905", "Primair"),
            ("Een studie van een historicus uit 1980", "Secundair"),
            ("Een foto van de stakers voor de poort", "Primair"),
        ],
        "Primair komt uit de tijd zelf, secundair is later geschreven.",
        kolommen=["Primair", "Secundair"],
    ),
    sorteer(
        "Welk soort bron is elk voorbeeld?",
        ["Schriftelijk", "Materieel", "Beeld", "Mondeling"],
        [
            ["een krant", "Schriftelijk"],
            ["een register", "Schriftelijk"],
            ["een munt", "Materieel"],
            ["een werktuig", "Materieel"],
            ["een affiche", "Beeld"],
            ["een interview met een getuige", "Mondeling"],
        ],
        "Ook een gebouw of werktuig is een bron.",
    ),
    mk(
        "Een leerling zegt: \"Een primaire bron is altijd beter dan een secundaire.\" Wat is de beste reactie?",
        [
            "Nee, een ooggetuige kan zich vergissen",
            "Ja, want een secundaire bron is altijd gelogen",
            "Ja, want primaire bronnen zijn altijd volledig",
            "Nee, want primaire bronnen bestaan niet",
        ],
        0,
        "Een latere studie kan net alles naast elkaar leggen.",
    ),
    # --- bruikbaarheid
    tabel(
        "Je onderzoekt het leven van Limburgse mijnwerkers rond 1950. Welke bron is bruikbaar?",
        [
            ("Het dagboek van een mijnwerker uit Zolder, 1951", J),
            ("Het dagboek van een mijnwerker uit Wales, 1890", F),
            ("Een foto van een mijnwerkerscité in Genk, 1952", J),
            ("Een betrouwbare studie over boeren in de Kempen in 1700", F),
        ],
        "Thema, tijd en plaats moeten kloppen. Een betrouwbare bron over de verkeerde tijd blijft onbruikbaar.",
    ),
    casus(
        "Een krant verschijnt in 1942 onder censuur van de bezetter. Ze schrijft: \"De terroristen die de spoorlijn opbliezen, zijn opgepakt. De bevolking staat achter de orde.\"",
        [
            tabel(
                "Voor welke vraag is deze krant een goede bron?",
                [
                    ("Hoe sprak de bezetter over het verzet?", J),
                    ("Wat wilde de bezetter de bevolking laten lezen?", J),
                    ("Wat dacht de bevolking echt over het verzet?", F),
                ],
                "Onbetrouwbaar over de feiten, uitstekend over de bedoelingen van de bezetter.",
            ),
            mk(
                "Waarom noemt de krant de verzetslieden 'terroristen'?",
                [
                    "Het toont het standpunt van de bezetter",
                    "Het was de officiële naam van het verzet",
                    "De verzetslieden noemden zichzelf zo",
                    "Het woord betekende toen 'helden'",
                ],
                0,
                "Woordkeuze verraadt een standpunt. Een bron lees je in haar context.",
            ),
        ],
    ),
    koppel(
        "Welk begrip over bronnenonderzoek hoort bij elke omschrijving?",
        [
            ["Iets uit een andere tijd in een verkeerde tijd plaatsen", "Anachronisme"],
            ["De vraag of een bron voor een hele groep geldt", "Representativiteit"],
            ["Overnemen zonder te vermelden", "Plagiaat"],
            ["Kijken naar de wereld van waar je zelf staat", "Standplaatsgebondenheid"],
        ],
        ["Compositie", "Restauratie"],
        "Vier sleutelbegrippen bij het werken met bronnen.",
    ),
    mk(
        "Een film over 1830 toont een Belgische revolutionair met een polshorloge en een fiets. Wat is dat?",
        [
            "Een anachronisme",
            "Een primaire bron",
            "Een waardeoordeel",
            "Een vorm van representativiteit",
        ],
        0,
        "Polshorloges en fietsen horen niet bij 1830.",
    ),
    mk(
        "Eén mijnwerker schrijft in zijn dagboek dat hij gelukkig was in de mijn. Wat mag je besluiten?",
        [
            "Dat hij het zo beleefde",
            "Dat alle mijnwerkers gelukkig waren",
            "Dat het werk in de mijn niet gevaarlijk was",
            "Dat het dagboek vervalst is",
        ],
        0,
        "Eén dagboek vertelt over één mijnwerker. Representativiteit vraag je altijd na.",
    ),
    tabel(
        "Welke uitspraken over bronvermelding kloppen?",
        [
            ("Je vermeldt waar je een bron vond, zodat anderen kunnen controleren.", J),
            ("Ook hulp van een computerprogramma vermeld je.", J),
            ("Eén bron volstaat om een besluit te onderbouwen.", F),
            ("Overnemen zonder vermelden heet plagiaat.", J),
        ],
        "Een bronvermelding kost een regel en lost het probleem op.",
    ),
    # --- betrouwbaarheid
    volgorde(
        "Zet de vier vaste vragen bij een bron in de volgorde van het vragenrijtje.",
        ["Wie heeft ze gemaakt?", "Wanneer?", "Voor wie was ze bedoeld?", "Met welk doel?"],
        "Wie, wanneer, voor wie en waarom: daarmee begin je elke beoordeling.",
    ),
    casus(
        "Een generaal schrijft in 1935 zijn memoires over een veldslag uit 1917 die hij zelf leidde: \"Dankzij mijn plan werd de vijand verrast. De verliezen waren klein.\"",
        [
            tabel(
                "Waarop let je bij deze bron?",
                [
                    ("Hij heeft belang bij zijn eigen rol.", J),
                    ("Er liggen bijna twintig jaar tussen gebeurtenis en bron.", J),
                    ("Je toetst de verliezen aan andere bronnen.", J),
                    ("Omdat hij erbij was, klopt alles zeker.", F),
                ],
                "Een bron met een duidelijk belang lees je kritischer. Dat maakt haar niet waardeloos.",
            ),
            mk(
                "Welke bron leg je er het best naast?",
                [
                    "De verlieslijsten van het leger uit 1917",
                    "Een roman uit 2010 over een andere oorlog",
                    "Een tweede boek van dezelfde generaal",
                    "Een schoolboek over het Congres van Wenen",
                ],
                0,
                "Een bron uit de tijd zelf, zonder hetzelfde belang, toetst de bewering.",
            ),
        ],
    ),
    casus(
        "Bron A, een fabrikant in 1886: \"Een handvol onruststokers zette de arbeiders op.\" Bron B, een staker in 1886: \"We hadden honger. Niemand moest ons opzetten.\"",
        [
            mk(
                "Wat doe je als twee bronnen elkaar zo tegenspreken?",
                [
                    "Je zoekt bronnen bij",
                    "Je kiest de bron die je het meest aanspreekt",
                    "Je gooit beide bronnen weg",
                    "Je gelooft de bron met de langste tekst",
                ],
                0,
                "Je zoekt uit wie welk belang had en zoekt bronnen bij. Een tegenspraak is een aanwijzing dat er iets uit te leggen valt.",
            ),
            tabel(
                "Feit, mening of waardeoordeel?",
                [
                    ("In 1886 was er een staking.", "Feit"),
                    ("De stakers waren onruststokers.", "Waardeoordeel"),
                    ("Volgens de fabrikant zette een kleine groep de anderen op.", "Mening"),
                ],
                "Een feit is te controleren, een mening is een standpunt, een waardeoordeel noemt iets goed of slecht.",
                kolommen=["Feit", "Mening", "Waardeoordeel"],
            ),
        ],
    ),
    mk(
        "Een bron heeft geen auteur. Wat doe je ermee?",
        [
            "Toetsen aan andere bronnen",
            "Je gebruikt ze nooit meer in je werk",
            "Je verzint zelf een passende auteur",
            "Je gelooft ze zonder meer, net als andere",
        ],
        0,
        "Voorzichtig gebruiken, toetsen, en zeggen wat je niet weet.",
    ),
    tabel(
        "Een vrouw vertelt in 1995 over haar bevrijding in 1944. Waarvoor is haar getuigenis sterk, en waarvoor minder?",
        [
            ("Hoe ze de vreugde van de bevrijding beleefde", "Sterk"),
            ("Op welke dag en welk uur de eerste tank aankwam", "Minder"),
            ("Wat de bevrijding voor haar gezin betekende", "Sterk"),
        ],
        "Het geheugen verandert met de tijd en met wat men later hoorde. Over de beleving blijft een getuigenis waardevol.",
        kolommen=["Sterk", "Minder"],
    ),
    mk(
        "Waarom legt een historicus zijn werkwijze en bronnen open?",
        [
            "Hij is ook standplaatsgebonden",
            "Hij moet zijn boek langer maken",
            "Hij wil zijn mening verbergen",
            "Hij gebruikt nooit bronnen",
        ],
        0,
        "Afkomst, tijd, geloof en belang bepalen mee wat iemand ziet. Wie zijn werkwijze toont, laat anderen controleren.",
    ),
    keuze(
        "Een historicus vermeldt altijd de [[*datum|kleur|prijs]] van een bron, want de afstand tot de gebeurtenis telt mee. Hoe [[*dichter|verder|later]] bij de gebeurtenis, hoe meer de maker zelf kan weten.",
        "Afstand in tijd is een van de criteria voor betrouwbaarheid.",
    ),
    # --- internet en beeld
    klik(
        "Dit is een tekening van een plein tijdens een betoging, van bovenaf. Een fotograaf houdt enkel het drukste stuk over. Klik op dat stuk.",
        "betoging-van-bovenaf.svg",
        [[60.0, 18.0, 26.0, 42.0]],
        "Wie enkel dat stuk toont, laat de betoging veel groter lijken. Er is niets vervalst, en toch klopt het beeld niet meer.",
    ),
    tabel(
        "Waarom is een beeld vandaag geen bewijs op zichzelf?",
        [
            ("Beelden kunnen bewerkt worden.", J),
            ("Beelden kunnen volledig gemaakt worden.", J),
            ("Ook vroeger werden foto's in scène gezet.", J),
            ("Foto's kunnen nooit iets tonen wat echt gebeurde.", F),
        ],
        "De techniek maakt het nu eenvoudiger, maar ook vroeger werd geretoucheerd.",
    ),
    tabel(
        "Je vindt een website over de Belgische revolutie. Wat ga je na?",
        [
            ("Wie zit erachter?", J),
            ("Van wanneer is de pagina?", J),
            ("Staat ze bovenaan in de zoekresultaten?", F),
            ("Zeggen andere bronnen hetzelfde?", J),
        ],
        "Bovenaan staan gaat over techniek en geld, niet over juistheid.",
    ),
    mk(
        "Je ziet op sociale media een schokkend bericht met een foto. Wat doe je eerst?",
        [
            "Andere bronnen zoeken",
            "Het meteen doorsturen naar al je vrienden",
            "Geloven omdat er een foto bij staat",
            "Kijken hoeveel likes het heeft",
        ],
        0,
        "Ga na of onafhankelijke bronnen hetzelfde melden. Dezelfde vragen als bij een historische bron helpen bij het nieuws.",
    ),
    casus(
        "Over de staking van 1886 heb je drie bronnen: een affiche van de stakers, het dagboek van een mijnwerkersvrouw en een studie van een historicus uit 1990.",
        [
            koppel(
                "Wat vertelt elke bron vooral?",
                [
                    ["De affiche", "De bedoeling"],
                    ["Het dagboek", "De beleving"],
                    ["De studie", "Het overzicht"],
                ],
                ["De toekomst"],
                "Elke bron zegt iets anders. Daarom leg je ze naast elkaar.",
            ),
            mk(
                "Waarom gebruik je de drie samen?",
                [
                    "Ze vullen elkaar aan",
                    "Eén bron is altijd genoeg",
                    "De studie maakt de andere twee overbodig",
                    "Het dagboek is altijd het betrouwbaarst",
                ],
                0,
                "Eén enkele bron is niet genoeg om een besluit te onderbouwen.",
            ),
        ],
    ),
    sleep(
        "Een bron is [[bruikbaar]] als ze over thema, tijd en plaats van je vraag gaat. Een bron is [[betrouwbaar]] als je weet wie ze maakte, met welk belang, en als andere bronnen hetzelfde zeggen.",
        ["primair", "secundair"],
        "Bruikbaarheid hangt af van je vraag, betrouwbaarheid van de bron zelf.",
    ),
    open_(
        "Leg uit waarom een onbetrouwbare bron toch bruikbaar kan zijn. Geef een voorbeeld.",
        "Of een bron bruikbaar is, hangt af van je vraag. Een gecensureerde krant uit 1942 is onbetrouwbaar over de feiten, maar uitstekend als je wilt weten wat de bezetter de bevolking wilde laten lezen. Ook propaganda is een goede bron over de bedoelingen van wie ze maakte.",
    ),
    open_(
        "Je krijgt een foto van een volle betoging. Leg uit welke vragen je stelt voor je ze als bewijs gebruikt.",
        "Wie maakte de foto, wanneer, voor wie en met welk doel? Werd ze bijgesneden of bewerkt? Zeggen andere bronnen, zoals kranten of verslagen, hetzelfde over de grootte van de betoging? Een beeld is geen bewijs op zichzelf.",
    ),
    mk(
        "Wat betekent een bron 'in haar context lezen'?",
        [
            "Met de tijd erbij lezen",
            "Lezen met de woorden van vandaag",
            "Enkel de titel lezen",
            "Lezen zonder te weten wie ze schreef",
        ],
        0,
        "Woorden betekenden in 1850 niet hetzelfde als vandaag.",
    ),
    tabel(
        "Welke uitspraken over het beginnen van een onderzoek kloppen?",
        [
            ("Je begint met een historische vraag.", J),
            ("Zonder vraag weet je niet welke bron je nodig hebt.", J),
            ("Je verzamelt eerst alle bronnen ter wereld en kiest dan een vraag.", F),
        ],
        "De vraag bepaalt wat bruikbaar is.",
    ),
]
