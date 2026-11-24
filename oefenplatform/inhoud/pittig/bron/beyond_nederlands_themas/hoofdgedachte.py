"""Onderwerp, hoofdgedachte en samenvatten — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lees de tekst.\n\n"
    "(1) Wie vandaag door zijn tijdlijn scrolt, ziet vooral berichten die hem gelijk geven. "
    "(2) Dat is geen toeval: de algoritmes van sociale media tonen ons wat we al denken, omdat we daar langer naar kijken. "
    "(3) Zo ontstaan echokamers, waarin andere meningen nauwelijks nog binnendringen. "
    "(4) Bovendien hebben sensationele berichten een grotere kans om viraal te gaan dan genuanceerde. "
    "(5) Een filmpje van een schreeuwende politicus haalt een miljoen views, een rustig interview nauwelijks duizend. "
    "(6) Daardoor lijkt de tegenpartij extremer dan ze is. "
    "(7) Sociale media maken de kloof tussen groepen in de samenleving dus groter."
)

TEKST2 = (
    "Lees de tekst.\n\n"
    "Tieners slapen gemiddeld een uur te weinig. Dat komt niet door luiheid: in de puberteit schuift de biologische klok op, "
    "waardoor jongeren pas laat moe worden. Wie dan om zeven uur moet opstaan, begint de dag met een tekort. Dat tekort heeft gevolgen. "
    "Onderzoekers zien bij te korte nachten slechtere schoolresultaten, meer prikkelbaarheid en een groter risico op ongevallen met de fiets. "
    "Mijn neef viel vorig jaar zelfs in slaap tijdens een toets wiskunde. Ook schermen spelen mee: blauw licht 's avonds stelt het slaaphormoon nog verder uit. "
    "Kortom, het slaaptekort van tieners is grotendeels een biologisch probleem dat door ons dagritme en onze schermen verergert."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            inv(
                "Wat is het onderwerp van deze tekst? Antwoord in enkele woorden.",
                ["sociale media en polarisatie", "polarisatie door sociale media", "sociale media en de kloof in de samenleving", "polarisatie", "sociale media en de kloof", "de invloed van sociale media op polarisatie"],
                "Het onderwerp zeg je in één of enkele woorden: waarover gaat het?",
            ),
            mk(
                "Welke zin geeft de hoofdgedachte het best weer?",
                [
                    "Sociale media vergroten de kloof tussen groepen",
                    "Algoritmes tonen ons wat we graag zien op het scherm",
                    "Een schreeuwende politicus haalt een miljoen views",
                    "Sociale media bestaan uit tijdlijnen en echokamers",
                ],
                0,
                "Zin 7 vat samen waar alle hoofdpunten naartoe wijzen. Let op het signaalwoord \"dus\".",
            ),
            tabel(
                "Hoofdpunt of bijzaak?",
                [
                    ("Zin 3: echokamers houden andere meningen buiten.", "Hoofdpunt"),
                    ("Zin 4: sensationele berichten gaan vaker viraal.", "Hoofdpunt"),
                    ("Zin 5: het filmpje met een miljoen views.", "Bijzaak"),
                ],
                "Een voorbeeld illustreert een hoofdpunt, maar draagt het niet.",
                kolommen=["Hoofdpunt", "Bijzaak"],
            ),
            mk(
                "Wat verraadt het woord \"bovendien\" in zin 4?",
                [
                    "Er komt nog een reden bij",
                    "Er volgt een tegenstelling met zin 3",
                    "Er volgt een voorbeeld bij zin 3",
                    "De tekst gaat naar het slot",
                ],
                0,
                "Bovendien stapelt op: een tweede oorzaak naast de echokamers.",
            ),
            keuze(
                "Het woord \"daar\" in zin 2 verwijst naar [[*wat we al denken|de algoritmes|de tijdlijn]].",
                "Verwijswoorden knopen zinnen aan elkaar. Wie niet weet waarnaar ze verwijzen, verliest de draad.",
            ),
            mk(
                "Je moet de tekst samenvatten in twee zinnen. Wat laat je zeker weg?",
                [
                    "Het voorbeeld van de politicus",
                    "De echokamers",
                    "De sensationele berichten die viraal gaan",
                    "De groeiende kloof",
                ],
                0,
                "Voorbeelden en anekdotes sneuvelen eerst. Ze dragen de tekst niet.",
            ),
        ],
    ),
    tabel(
        "Onderwerp of hoofdgedachte?",
        [
            ("de kostprijs van wonen", "Onderwerp"),
            ("Wonen is voor jongeren onbetaalbaar geworden.", "Hoofdgedachte"),
            ("de rol van slaap", "Onderwerp"),
            ("Slaap is even belangrijk voor leren als studeren.", "Hoofdgedachte"),
        ],
        "Het onderwerp noemt waarover het gaat. De hoofdgedachte is een zin die er iets over beweert.",
        kolommen=["Onderwerp", "Hoofdgedachte"],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Waar staat de hoofdgedachte?",
                [
                    "In de laatste zin",
                    "In de eerste zin",
                    "In de zin over de neef",
                    "Nergens, je moet ze zelf bedenken",
                ],
                0,
                "\"Kortom\" kondigt een samenvatting aan. De hoofdgedachte staat niet altijd vooraan.",
            ),
            tabel(
                "Welke informatie neem je op in een samenvatting van vijftig woorden?",
                [
                    ("De biologische klok schuift op in de puberteit.", J),
                    ("Slaaptekort geeft slechtere resultaten en meer ongevallen.", J),
                    ("De neef die tijdens een toets in slaap viel.", F),
                    ("Blauw licht van schermen stelt de slaap verder uit.", J),
                ],
                "De anekdote over de neef illustreert, maar is geen hoofdpunt.",
            ),
            mk(
                "Welke samenvatting is het best?",
                [
                    "Tieners worden door hun biologische klok laat moe; vroeg opstaan en schermen vergroten dat tekort, met gevolgen voor school en veiligheid.",
                    "Tieners slapen gemiddeld een uur te weinig. Dat komt niet door luiheid. Mijn neef viel in slaap tijdens een toets.",
                    "Ik vind dat scholen later moeten beginnen, want tieners slapen te weinig en dat is slecht voor hun resultaten en hun humeur.",
                    "De tekst gaat over slaap, schermen, wiskunde, fietsen, de puberteit, hormonen, luiheid, toetsen, de neef van de schrijver en blauw licht bij tieners.",
                ],
                0,
                "Herformuleren, hoofdzaken behouden en geen eigen mening toevoegen. De tweede schrijft over, de derde geeft een mening, de vierde is een opsomming.",
            ),
            keuze(
                "In de zin \"Dat tekort heeft gevolgen\" verwijst \"dat tekort\" naar [[*het slaaptekort bij vroeg opstaan|het blauwe licht|de luiheid]].",
                "Het verwijswoord slaat terug op de vorige zin.",
            ),
        ],
    ),
    tabel(
        "Waaraan voldoet een goede samenvatting?",
        [
            ("Ze is korter dan de oorspronkelijke tekst.", J),
            ("Ze bevat de hoofdgedachte en de hoofdpunten.", J),
            ("Ze neemt zinnen letterlijk over.", F),
            ("Ze bevat je eigen mening over het onderwerp.", F),
            ("Ze mag de volgorde van de tekst veranderen.", J),
        ],
        "Je herformuleert in eigen woorden, met een duidelijke opbouw, zonder eigen mening.",
    ),
    mk(
        "Een leerling levert een samenvatting in van 900 woorden bij een tekst van 1000 woorden. Wat liep er vooral mis?",
        [
            "Hoofd- en bijzaken zijn niet gescheiden",
            "De leerling gebruikte te veel signaalwoorden",
            "De leerling veranderde de volgorde van de tekst",
            "De leerling liet de titel van de tekst weg",
        ],
        0,
        "Samenvatten begint bij kiezen wat weg mag.",
    ),
    tabel(
        "Klopt dit over notities?",
        [
            ("Telegramstijl en afkortingen mogen.", J),
            ("Een mindmap of tabel mag ook.", J),
            ("Iemand anders moet ze zonder uitleg kunnen lezen.", F),
            ("Je neemt alle voorbeelden over.", F),
        ],
        "Notities zijn voor jezelf. Ze moeten duidelijk genoeg zijn om er later mee te werken.",
    ),
    mk(
        "Wat is het voordeel van een mindmap boven een lijstje?",
        [
            "Je ziet de verbanden tussen de delen",
            "Een mindmap bevat altijd meer informatie",
            "Een mindmap kan je sneller overschrijven",
            "Een mindmap heeft geen hoofdgedachte nodig",
        ],
        0,
        "Een mindmap toont wat bij wat hoort. Een lijstje zet alles onder elkaar.",
    ),
    volgorde(
        "Je moet informatie uit drie artikels systematisch verwerken. Zet de stappen in de juiste volgorde.",
        [
            "Je leest met je vraag in het hoofd",
            "Je selecteert per tekst wat op je vraag slaat",
            "Je ordent je notities",
            "Je schrijft je tekst met een correcte bronvermelding",
        ],
        "Selecteren, ordenen, verwerken: telkens op dezelfde manier.",
    ),
    tabel(
        "Welke strategie helpt bij het luisteren naar een lange reportage?",
        [
            ("Korte notities nemen", J),
            ("Op signaalwoorden letten", J),
            ("Elk onbekend woord meteen opzoeken", F),
            ("Alles letterlijk meeschrijven", F),
        ],
        "Opzoeken en meeschrijven kosten je de draad.",
    ),
    mk(
        "Je komt in een examentekst een onbekend woord tegen dat je niet nodig hebt om de vraag te beantwoorden. Wat doe je?",
        [
            "Je leest gewoon door",
            "Je zoekt het meteen op",
            "Je slaat de hele alinea over",
            "Je stopt met de tekst",
        ],
        0,
        "Op een examen van twee uur zoek je enkel op wat echt nodig is.",
    ),
    tabel(
        "Welke hulpmiddelen tonen je de opbouw of de kern van een tekst?",
        [
            ("De titel en de tussentitels", J),
            ("Benadrukte woorden", J),
            ("Een kader met de kernboodschap", J),
            ("De breedte van de kantlijn", F),
        ],
        "Visuele hulpmiddelen wijzen je op de opbouw. De kantlijn zegt niets over de inhoud.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Waarover de tekst gaat, in enkele woorden", "Onderwerp"],
            ["De belangrijkste boodschap, in één zin", "Hoofdgedachte"],
            ["De elementen die de boodschap ondersteunen", "Hoofdpunten"],
            ["Signaalwoorden en verwijswoorden samen", "Structuuraanduiders"],
        ],
        ["Bronvermelding", "Anekdote"],
        "Vier begrippen die je nodig hebt om een tekst te doorgronden.",
    ),
    mk(
        "Je gebruikt je notities over vapen niet voor een samenvatting maar voor een opiniërende tekst. Wat is het verschil?",
        [
            "Je voegt je eigen standpunt toe",
            "Je hoeft de bronnen niet te vermelden",
            "Je neemt de zinnen letterlijk over",
            "Je laat de hoofdpunten weg",
        ],
        0,
        "Een opiniërende tekst gebruikt bronnen voor je mening. Bronvermelding blijft nodig.",
    ),
    sleep(
        "De hoofdgedachte kan in de [[inleiding]] staan, maar even goed in het [[slot]] of nergens letterlijk. Dan moet je ze zelf [[formuleren]].",
        ["titel", "overschrijven"],
        "De hoofdgedachte staat niet altijd in de eerste zin.",
    ),
    casus(
        "Je hoort een fragment uit een radioreportage.\n\n"
        "\"In Brussel staan sinds dit jaar zestig nieuwe deelfietsstations. Het stadsbestuur wil zo het autoverkeer in het centrum terugdringen. "
        "Toch blijven veel fietsen ongebruikt. Ten eerste liggen de stations vooral in de rijkere wijken. Ten tweede vinden veel inwoners de fietspaden te gevaarlijk. "
        "Een fietser vertelt dat ze twee keer bijna werd aangereden. Zolang de fietspaden niet veiliger worden, zal het plan dus maar half slagen.\"",
        [
            mk(
                "Wat is de hoofdgedachte van het fragment?",
                [
                    "Zonder veilige fietspaden slaagt het plan maar half",
                    "Er staan sinds dit jaar zestig nieuwe deelfietsstations",
                    "Een fietser werd twee keer bijna aangereden",
                    "Het stadsbestuur wil minder auto's in de straten",
                ],
                0,
                "Het slot met \"dus\" brengt de hoofdpunten samen.",
            ),
            tabel(
                "Wat noteer je tijdens het luisteren als hoofdpunt?",
                [
                    ("stations vooral in rijkere wijken", J),
                    ("fietspaden te gevaarlijk", J),
                    ("fietster twee keer bijna aangereden", F),
                ],
                "\"Ten eerste\" en \"ten tweede\" kondigen de hoofdpunten aan. Het getuigenis is een voorbeeld.",
            ),
            keuze(
                "De hoofdpunten worden aangekondigd door de signaalwoorden [[*ten eerste en ten tweede|toch en dus|sinds en zo]].",
                "Opsommende signaalwoorden laten de structuur van een luistertekst horen.",
            ),
        ],
    ),
    mk(
        "Een tekst heeft vier hoofdpunten. Hoeveel hoofdgedachten heeft hij?",
        ["Eén", "Vier", "Geen", "Even veel als alinea's"],
        0,
        "De hoofdgedachte is er één. De hoofdpunten die haar dragen, zijn er meestal meer.",
    ),
    mk(
        "Waarom vraag je je vóór het lezen af wat je al over het onderwerp weet?",
        [
            "Je herkent begrippen sneller",
            "Je hoeft de tekst dan niet volledig te lezen",
            "Je kan je eigen mening dan in de samenvatting zetten",
            "Je weet dan zeker wat de hoofdgedachte is",
        ],
        0,
        "Voorkennis helpt je de tekst vlotter te volgen en onbekende woorden te raden.",
    ),
    tabel(
        "Welke vraag helpt je om de hoofdgedachte te vinden?",
        [
            ("Wat wil de schrijver dat ik onthoud?", J),
            ("Waar wijzen alle hoofdpunten naartoe?", J),
            ("Welk woord komt het vaakst voor?", F),
            ("Hoeveel alinea's telt de tekst?", F),
        ],
        "Het meest voorkomende woord geeft hoogstens het onderwerp.",
    ),
    tabel(
        "Je vat een betoog over vapen samen. Mag dit erin?",
        [
            ("de stelling van de schrijver, in je eigen woorden", "Mag"),
            ("zijn belangrijkste argumenten", "Mag"),
            ("jouw mening over vapen", "Mag niet"),
            ("een letterlijk overgenomen alinea", "Mag niet"),
        ],
        "Een samenvatting geeft weer wat er stond, herschreven, zonder wat jij ervan vindt.",
        kolommen=["Mag", "Mag niet"],
    ),
    open_(
        "Lees opnieuw de tekst over sociale media. Vat hem samen in hoogstens drie zinnen, in je eigen woorden.",
        "Algoritmes tonen gebruikers vooral berichten die hun mening bevestigen, waardoor ze in echokamers terechtkomen. Daarnaast verspreiden opvallende, extreme berichten zich sneller dan genuanceerde, zodat andere groepen extremer lijken. Zo vergroten sociale media de kloof in de samenleving.",
    ),
]
