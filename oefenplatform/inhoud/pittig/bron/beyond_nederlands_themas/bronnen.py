"""Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Op sociale media circuleert dit bericht, zonder auteur:\n\n"
        "\"SCHANDAAL!!! Winkelketen Bonmarché sluit ALLE winkels volgende week. Duizenden jobs weg. De media zwijgen erover! Deel voor het te laat is!!! Lees alles op www.waarheid-nu.biz\"",
        [
            tabel(
                "Welke signalen wijzen op nepnieuws?",
                [
                    ("Er wordt geen auteur vermeld.", J),
                    ("De titel is sterk lokkend opgesteld.", J),
                    ("Het bericht beweert dat de media zwijgen.", J),
                    ("Het bericht is kort.", F),
                ],
                "Geen auteur, geen bron, maximaal lokken: een klassiek patroon. De lengte zegt niets.",
            ),
            mk(
                "Wat is je eerste stap?",
                [
                    "Kijken of een nieuwsredactie het ook brengt",
                    "Het bericht delen met je vrienden en familie",
                    "De site waarheid-nu.biz grondig doorlezen",
                    "De winkelketen een boze mail sturen",
                ],
                0,
                "Is zoiets waar, dan staat het snel bij elke redactie. Staat het nergens anders, dan is dat al een antwoord.",
            ),
            mk(
                "De site staat vol advertenties. Wat is waarschijnlijk het doel van het bericht?",
                [
                    "Bezoekers naar die site lokken",
                    "Werknemers van de keten waarschuwen voor hun ontslag",
                    "Journalisten aanzetten tot onderzoek naar de keten",
                    "Klanten informeren over de nieuwe openingsuren",
                ],
                0,
                "Meer bezoekers is meer bekeken advertenties. Het bericht is lokaas.",
            ),
        ],
    ),
    tabel(
        "Over welke vraag gaat elk criterium?",
        [
            ("Kloppen de feiten die erin staan?", "Correct"),
            ("Wie is de zender en wat wil die?", "Betrouwbaar"),
            ("Helpt deze tekst mij bij mijn eigen vraag?", "Bruikbaar"),
        ],
        "Betrouwbaar gaat over de zender, correct over de inhoud, bruikbaar over jouw doel.",
        kolommen=["Betrouwbaar", "Correct", "Bruikbaar"],
    ),
    casus(
        "Twee kranten brengen hetzelfde cijfer over de werkloosheid.\n\n"
        "Krant A: \"Werkloosheid stijgt met 3 procent.\"\n"
        "Krant B: \"Werkloosheid stijgt voor de derde maand op rij.\"",
        [
            mk(
                "Wat zie je hier?",
                [
                    "Twee frames rond hetzelfde feit",
                    "Een van de twee kranten liegt over de cijfers",
                    "Twee verschillende cijfers over de werkloosheid",
                    "Twee keer exact dezelfde boodschap aan de lezer",
                ],
                0,
                "Het feit is hetzelfde, de kadering verschilt: omvang tegenover herhaling.",
            ),
            keuze(
                "Krant B legt de nadruk op [[*de herhaling|de omvang|de oorzaak]] van de stijging.",
                "\"Derde maand op rij\" doet een trend vermoeden.",
            ),
        ],
    ),
    tabel(
        "Is dit een voorbeeld van framing?",
        [
            ("spreken over een belastingverlaging of over een besparing op de staatskas", J),
            ("spreken over klimaatverandering of over klimaatontwrichting", J),
            ("spreken over een auto of over een wagen", F),
        ],
        "Auto en wagen zijn gewone synoniemen. De andere paren zetten dezelfde zaak in een ander licht.",
    ),
    mk(
        "Een minister schrijft op de site van zijn partij hoe goed zijn beleid werkt. Hoe beoordeel je die tekst?",
        [
            "Partijdig, dus je zoekt een tweede bron",
            "Onwaar, want een partij liegt per definitie altijd",
            "Neutraal, want een minister kent de cijfers het best",
            "Onbruikbaar, want sites van partijen zijn verboden bronnen",
        ],
        0,
        "Belang maakt een tekst niet onwaar, wel partijdig.",
    ),
    tabel(
        "Juist of fout?",
        [
            ("Een tekst vol feiten kan toch een vertekend beeld geven.", J),
            ("Een verzorgde website is voldoende bewijs van betrouwbaarheid.", F),
            ("Eén criterium beslist op zichzelf of een bron deugt.", F),
            ("De criteria gelden ook voor beeld en geluid.", J),
        ],
        "Je maakt een afweging. Hoe meer rode vlaggen, hoe voorzichtiger.",
    ),
    casus(
        "Een filmpje toont een staafgrafiek over de prijs van een brood: 2023 = 96 cent, 2024 = 99 cent. De verticale as begint bij 95.",
        [
            mk(
                "Wat gebeurt er met de indruk van de kijker?",
                [
                    "Een kleine stijging lijkt enorm",
                    "De cijfers worden onleesbaar",
                    "De stijging lijkt kleiner dan ze is",
                    "Er verandert niets aan de indruk",
                ],
                0,
                "De cijfers kloppen, maar het beeld misleidt. Een afgesneden as is de bekendste truc.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("De cijfers in de grafiek kunnen correct zijn.", J),
                    ("De grafiek verandert de boodschap, niet enkel de vorm.", J),
                    ("Een grafiek is altijd neutraler dan tekst.", F),
                ],
                "Multimediale elementen kunnen een boodschap versterken of veranderen.",
            ),
        ],
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Een bericht dat een politieke overtuiging wil opdringen", "Propaganda"],
            ["Een bericht dat je iets wil doen kopen", "Reclame"],
            ["Een algoritme dat je vooral toont wat bij je past", "Filterbubbel"],
            ["Een omgeving waar je je eigen mening terughoort", "Echokamer"],
        ],
        ["Framing", "Publireportage"],
        "Vier begrippen rond beïnvloeding.",
    ),
    mk(
        "Je vindt hetzelfde bericht op vijf sites, telkens met exact dezelfde zinnen. Wat besluit je?",
        [
            "Het is waarschijnlijk vijf keer dezelfde bron",
            "Het is zeker waar, want vijf sites bevestigen het",
            "Het is zeker vals, want sites kopiëren nooit nieuws",
            "Het is een publireportage van een bekend merk",
        ],
        0,
        "Kopieën zijn geen onafhankelijke bevestiging. Zoek wie het als eerste bracht.",
    ),
    casus(
        "Je maakt een spreekbeurt over slaap bij jongeren. Je vindt deze bronnen:\n\n"
        "A. Een artikel van een slaaponderzoeker dat studies bij tieners samenvat (2024).\n"
        "B. Een blog van een matrassenmerk over \"de perfecte nachtrust\" (2024).\n"
        "C. Een studie over slaap bij gepensioneerden (2023).\n"
        "D. Een krantenartikel over slaapregels voor studiebeurzen uit 2014.",
        [
            mk(
                "Welke bron is het bruikbaarst?",
                ["A", "B", "C", "D"],
                0,
                "Bruikbaar hangt van je doel af: onderzoek bij precies jouw groep.",
            ),
            tabel(
                "Wat is het probleem met elke andere bron?",
                [
                    ("B", "Belanghebbende zender"),
                    ("C", "Andere doelgroep"),
                    ("D", "Mogelijk verouderd"),
                ],
                "Zender, relevantie en actualiteit: drie verschillende criteria.",
                kolommen=["Belanghebbende zender", "Andere doelgroep", "Mogelijk verouderd"],
            ),
        ],
    ),
    mk(
        "Waarom pas je de criteria best ook toe op berichten die je graag gelooft?",
        [
            "Die controleren we vaak minder streng",
            "Die zijn meestal vals en misleidend",
            "Die komen vaker van een anonieme zender",
            "Die bevatten altijd meer meningen dan feiten",
        ],
        0,
        "Wat je mening bevestigt, glipt makkelijker door je filter.",
    ),
    mk(
        "Een opiniestuk bestaat bijna volledig uit meningen. Wat betekent dat voor jou als je feiten zoekt?",
        [
            "Je haalt er weinig feiten uit",
            "Het stuk is fout geschreven en mag niet gepubliceerd worden",
            "Het stuk is daardoor ook propaganda van een politieke partij",
            "Je moet het stuk als nepnieuws melden bij het platform",
        ],
        0,
        "Een opiniestuk hoort vol meningen te zitten. Het is gewoon niet de juiste bron voor feiten.",
    ),
    sleep(
        "Een lokkende titel dient vooral het aantal [[clicks]], niet de [[inhoud]]. Een [[publireportage]] moet herkenbaar zijn als betaalde inhoud.",
        ["auteur", "frame"],
        "Lokken en betaalde inhoud: allebei zetten ze je op je hoede.",
    ),
    tabel(
        "Een anonieme account met veel volgers deelt een haatbericht. Klopt dit?",
        [
            ("Anonimiteit kan een rem op harde taal wegnemen.", J),
            ("Veel volgers maakt een bericht betrouwbaar.", F),
            ("Een echokamer kan zo'n bericht versterken.", J),
        ],
        "Zonder naam en gezicht valt een rem weg. Populariteit is geen bewijs.",
    ),
    mk(
        "Een artikel staat op de site van een universiteit. Wat besluit je?",
        [
            "Goed teken, maar check auteur en bronnen",
            "Het is automatisch betrouwbaar en correct",
            "Het is automatisch een publireportage",
            "Het is automatisch verouderd",
        ],
        0,
        "Ook op een universiteitssite staan opiniestukken en persberichten.",
    ),
    casus(
        "Lees de twee titels over hetzelfde voorstel.\n\n"
        "Titel 1: \"Regering wil hardwerkende gezinnen nog dieper in de zakken zitten\"\n"
        "Titel 2: \"Regering stelt hogere bijdrage voor om zorg betaalbaar te houden\"",
        [
            tabel(
                "Welke titel doet wat?",
                [
                    ("kadert de maatregel als diefstal", "Titel 1"),
                    ("kadert de maatregel als solidariteit", "Titel 2"),
                    ("gebruikt de beladen uitdrukking \"in de zakken zitten\"", "Titel 1"),
                ],
                "Dezelfde maatregel, twee frames: lasten tegenover bijdrage.",
                kolommen=["Titel 1", "Titel 2"],
            ),
            mk(
                "Welke titel ligt het dichtst bij een neutrale titel die de lading dekt?",
                [
                    "Geen van beide, ze kaderen allebei",
                    "Titel 1, want die spreekt over gezinnen",
                    "Titel 2, want die spreekt over zorg",
                    "Allebei, want ze gaan over hetzelfde voorstel",
                ],
                0,
                "Ook \"om zorg betaalbaar te houden\" kiest een invalshoek. Een neutrale titel zou enkel het voorstel noemen.",
            ),
            inv(
                "Hoe heet het verschijnsel dat beide titels tonen? Antwoord met één woord.",
                ["framing", "frames", "kadering", "kaderen"],
                "Framing: een onderwerp zo voorstellen dat je het op een bepaalde manier ziet.",
            ),
        ],
    ),
    sorteer(
        "Propaganda of reclame?",
        ["Propaganda", "Reclame"],
        [
            ["een affiche van een staat die oproept de leider te volgen", "Propaganda"],
            ["een filmpje dat een nieuwe smartphone aanprijst", "Reclame"],
            ["een pamflet van een beweging dat een ideologie verspreidt", "Propaganda"],
            ["een folder met kortingen van een supermarkt", "Reclame"],
        ],
        "Allebei persuasief. Propaganda stuurt je denken, reclame je koopgedrag.",
    ),
    mk(
        "Je kan de betrouwbaarheid van een bron niet inschatten. Wat doe je het best?",
        [
            "Een tweede, onafhankelijke bron zoeken",
            "De bron toch gebruiken zonder vermelding",
            "Alleen de foto's uit de bron gebruiken",
            "De bron weglaten en niets meer zoeken",
        ],
        0,
        "Een tweede bron is de snelste test.",
    ),
    tabel(
        "Waarom kijk je welke bronnen een tekst zelf gebruikt?",
        [
            ("Je kan nagaan waarop de beweringen steunen.", J),
            ("Je hoeft de schrijver dan niet op zijn woord te geloven.", J),
            ("Een tekst met bronnen is altijd volledig correct.", F),
        ],
        "Met bronnen kan je zelf gaan kijken. Een garantie is het niet.",
    ),
    mk(
        "Een fabrikant van frisdrank geeft cijfers over suiker in zijn drankjes. Hoe ga je ermee om?",
        [
            "Ze kunnen kloppen; je let op selectie en nadruk",
            "Ze kloppen zeker niet, want hij heeft er belang bij",
            "Ze kloppen zeker, want hij kent zijn product best",
            "Ze zijn onbruikbaar, want het zijn cijfers",
        ],
        0,
        "Belang betekent niet dat alles fout is, wel dat je kritisch kijkt naar wat getoond en weggelaten wordt.",
    ),
    keuze(
        "Een bericht uit 2014 over de regels voor een studiebeurs is [[*mogelijk verouderd|zeker correct|zeker propaganda]]: regelgeving verandert.",
        "Bij zulke onderwerpen is de datum zelf een criterium.",
    ),
    keuze(
        "Wat een algoritme niet doorlaat, bestaat voor jou niet. Je zit dan in een [[*filterbubbel|publireportage|frame]].",
        "De filter zit tussen jou en het aanbod. Een echokamer is de groep die je mening terugkaatst.",
    ),
    open_(
        "Je twijfelt over de betrouwbaarheid van een bericht over een nieuwe regel voor studiebeurzen. Beschrijf in drie stappen hoe je het nagaat.",
        "1. Ik kijk wie de zender is en of die er belang bij heeft. 2. Ik kijk naar de datum, want regels veranderen. 3. Ik zoek een tweede, onafhankelijke bron, bijvoorbeeld de officiële site of een nieuwsredactie.",
    ),
]
