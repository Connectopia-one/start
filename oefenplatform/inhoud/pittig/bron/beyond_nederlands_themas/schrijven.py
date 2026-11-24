"""Schrijven en schriftelijke interactie — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

KLACHT = (
    "Lees de klachtbrief van een leerling.\n\n"
    "\"Onderwerp: fiets\n\n"
    "Hallo,\n"
    "ik heb bij jullie een fiets gekocht en die is al kapot. Echt schandalig!!! De ketting springt er af en de remmen werken half. "
    "Ik heb hem op 3 september gekocht in jullie winkel in Hasselt, voor 450 euro. Ik wil een nieuwe of mijn geld terug. "
    "Ook was de verkoper onvriendelijk. 😡\n"
    "Groetjes, Arne\""
)

VRAGEN = [
    casus(
        KLACHT,
        [
            tabel(
                "Op welk criterium schiet de brief tekort?",
                [
                    ("register en beleefdheidsconventies", J),
                    ("tekstopbouw: de feiten komen pas na de emotie", J),
                    ("taakvoltooiing: er staat geen vraag in", F),
                    ("een duidelijke onderwerpregel", J),
                ],
                "De vraag staat er wel: een nieuwe fiets of het geld terug. Toon, opbouw en onderwerpregel kunnen beter.",
            ),
            mk(
                "Wat hoort in de inleiding van deze klacht?",
                [
                    "Wanneer en waar hij de fiets kocht",
                    "Dat de verkoper in de winkel onvriendelijk was",
                    "Dat hij het geld terug wil",
                    "Een uitroep over hoe schandalig het is",
                ],
                0,
                "De inleiding maakt meteen duidelijk waarover de brief gaat en wat er gebeurde.",
            ),
            keuze(
                "Een betere onderwerpregel is: [[*Klacht over defecte fiets gekocht op 3 september|Fiets!!!|Hallo]].",
                "Kort, duidelijk en ter zake.",
            ),
            tabel(
                "Wat maakt de brief formeler?",
                [
                    ("\"Geachte heer of mevrouw\" als aanspreking", J),
                    ("de emoji weglaten", J),
                    ("\"Met vriendelijke groeten\" als slot", J),
                    ("meer uitroeptekens", F),
                ],
                "Een gepaste aanspreking en slotgroet, zonder emoji's.",
            ),
        ],
    ),
    tabel(
        "Welk tekstdoel heeft elke schrijfopdracht vooral?",
        [
            ("een recensie van een film", "Je mening geven"),
            ("een stappenplan voor een spel", "Iets uitleggen"),
            ("een antirookpamflet", "Overtuigen"),
            ("een brochure over een jeugdhuis", "Informatie geven"),
        ],
        "Het doel bepaalt de keuzes die je maakt bij het schrijven.",
        kolommen=["Je mening geven", "Iets uitleggen", "Overtuigen", "Informatie geven"],
    ),
    volgorde(
        "Zet de schrijfstrategieën in een logische volgorde.",
        [
            "Doel, ontvanger en kanaal bepalen",
            "Een schrijfplan met kernwoorden maken",
            "De tekst schrijven",
            "De tekst grondig nalezen",
        ],
        "Eerst denken, dan plannen, dan schrijven en tot slot nalezen.",
    ),
    tabel(
        "Klopt dit over de beoordelingscriteria?",
        [
            ("Spelling is een apart criterium.", J),
            ("Een tekst die zijn doel bereikt, scoort ook goed op spelling.", F),
            ("Men verwacht ook minder frequente woorden en figuurlijke taal.", J),
            ("Een foutloze tekst kan toch ongepast klinken.", J),
        ],
        "Taakvoltooiing, register en spelling zijn aparte criteria.",
    ),
    casus(
        "Op een forum schrijft iemand: \"Ik vind dat gsm's op school helemaal verboden moeten worden. Ze leiden alleen maar af.\" Je wil reageren.",
        [
            mk(
                "Wat is de belangrijkste eis bij schriftelijke interactie?",
                [
                    "Je speelt in op wat de ander schreef",
                    "Je schrijft een zo lang mogelijk bericht",
                    "Je herhaalt je eigen standpunt drie keer",
                    "Je gebruikt zoveel mogelijk vakjargon",
                ],
                0,
                "Bij interactie draait het om reageren op de ander.",
            ),
            tabel(
                "Is dit een goede reactie?",
                [
                    ("\"Ik begrijp dat meldingen afleiden, maar met een gsm zoek je ook snel iets op.\"", J),
                    ("\"Jij snapt er duidelijk niets van.\"", F),
                    ("\"Wat denk je van een gsm-vrije les met af en toe een opdracht?\"", J),
                ],
                "Inspelen, nuanceren en voorstellen doen. Een persoonlijke aanval niet.",
            ),
        ],
    ),
    mk(
        "Je zit vast en vindt de juiste formulering niet. Wat doe je het best?",
        [
            "Je omschrijft het of zoekt het op",
            "Je laat de hele zin gewoon helemaal weg",
            "Je schrijft dat stukje dan in het Engels",
            "Je stopt meteen met de hele schrijfopdracht",
        ],
        0,
        "Je doel bereiken langs een andere weg is zelf een strategie.",
    ),
    tabel(
        "Wat doe je met informatie uit vier bronnen?",
        [
            ("Je verwijst er correct naar.", J),
            ("Je weegt af hoe betrouwbaar ze zijn.", J),
            ("Je neemt alinea's letterlijk over zonder vermelding.", F),
            ("Je verwerkt ze in je eigen woorden.", J),
        ],
        "Zonder bronvermelding lijkt het alsof je andermans werk voor het jouwe laat doorgaan.",
    ),
    mk(
        "Waarom is nalezen nodig, ook met een spellingcontrole?",
        [
            "Ze mist fouten die een bestaand woord opleveren",
            "Ze verandert je hele tekst zonder iets te vragen",
            "Ze werkt helemaal niet op het digitale examen",
            "Ze controleert enkel de hoofdletters in je tekst",
        ],
        0,
        "Een spellingcontrole vindt geen fout als word in plaats van wordt.",
    ),
    keuze(
        "Een flyer voor een evenement vraagt vooral [[*creatief taalgebruik met lay-out en korte, pakkende zinnen|lange, academische zinnen|een volledige bronnenlijst]].",
        "Een flyer moet in één oogopslag werken.",
    ),
    tabel(
        "Welke keuze maakt je tekst samenhangend?",
        [
            ("signaalwoorden gebruiken", J),
            ("per alinea één deelonderwerp", J),
            ("alle zinnen even lang maken", F),
            ("een herkenbare opbouw", J),
        ],
        "Even lange zinnen maken een tekst eentonig, niet samenhangend.",
    ),
    sleep(
        "Bij [[taakvoltooiing]] kijkt men of je boodschap volledig en ter zake is. Bij [[register]] kijkt men naar de toon. Een verslag van een onderzoeksopdracht vraagt [[objectieve]] taal.",
        ["spreektaal", "emoji's"],
        "Drie criteria en een conventie.",
    ),
    casus(
        "Je schrijft een mail aan de directeur van een jeugdhuis. Je vraagt of jouw klas er een avond een debat mag organiseren.",
        [
            tabel(
                "Hoort dit in de mail?",
                [
                    ("een onderwerpregel als \"Vraag: debatavond 6de jaar op 12 maart\"", J),
                    ("de datum, het uur en het aantal deelnemers", J),
                    ("een uitgebreid verslag van je laatste vakantie", F),
                    ("een vraag om een antwoord tegen een bepaalde datum", J),
                ],
                "Alles wat de ontvanger nodig heeft om te beslissen, en niets meer.",
            ),
            keuze(
                "De beste aanspreking is [[*Geachte mevrouw Peeters|Hey Peeters|Yo]].",
                "Een formele mail aan iemand die je niet kent, vraagt een beleefde aanspreking.",
            ),
            mk(
                "Welke slotzin past het best?",
                [
                    "Alvast bedankt voor uw antwoord.",
                    "Laat maar iets weten, hè, ciao!",
                    "Antwoord snel want we hebben haast!!",
                    "Doei en tot de volgende keer.",
                ],
                0,
                "Beleefd en formeel, zonder druk te zetten.",
            ),
            tabel(
                "Is dit register gepast in deze mail?",
                [
                    ("\"Graag zouden we uw zaal gebruiken.\"", J),
                    ("\"Da's toch geen probleem zeker?\"", F),
                    ("\"Mogen wij u vragen of dat mogelijk is?\"", J),
                ],
                "Spreektaal en tussentaal passen niet in een formele mail.",
            ),
        ],
    ),
    koppel(
        "Koppel elk criterium aan de vraag die je erbij stelt.",
        [
            ("taakvoltooiing", "Staat alles erin wat de opdracht vraagt?"),
            ("tekstopbouw", "Zijn inleiding, midden en slot duidelijk?"),
            ("register", "Past de toon bij de lezer?"),
            ("woordenschat", "Gebruik ik gevarieerde en precieze woorden?"),
        ],
        ["Heb ik minstens drie bronnen geciteerd?"],
        "Elk criterium bekijkt de tekst vanuit een andere kant.",
    ),
    casus(
        "Een leerling schrijft in een betoog: \"Sport is gezond. Ik speel voetbal. Mijn broer speelt ook voetbal. Daarom moet iedereen sporten. Sport is ook leuk. Mijn vriend zit op tennis. Sport is gezond.\"",
        [
            tabel(
                "Wat loopt er mis?",
                [
                    ("Een zin wordt letterlijk herhaald.", J),
                    ("Er staan geen signaalwoorden die verbanden tonen.", F),
                    ("De argumenten zijn persoonlijke voorbeelden.", J),
                    ("De zinnen zijn kort en eentonig.", J),
                ],
                "Daarom is wel een signaalwoord. Herhaling, eentonige zinnen en losse voorbeelden verzwakken het betoog.",
            ),
            mk(
                "Welke herschrijving is het sterkst?",
                [
                    "Wie geregeld sport, heeft minder kans op hartziekten. Bovendien geeft samen sporten plezier.",
                    "Sport is heel erg gezond en ook leuk, echt waar, iedereen weet dat toch al lang.",
                    "Mijn broer speelt voetbal en mijn vriend tennis, dus sport is toch wel duidelijk goed.",
                    "Sport. Gezond. Leuk. Iedereen moet het doen, anders ben je eigenlijk gewoon lui.",
                ],
                0,
                "Een algemeen argument met een signaalwoord dat een tweede argument aankondigt.",
            ),
        ],
    ),
    sorteer(
        "Gebruik je deze strategie vóór, tijdens of na het schrijven?",
        ["Voor", "Tijdens", "Na"],
        [
            ["kernwoorden noteren in een schrijfplan", "Voor"],
            ["de lezer en het doel bepalen", "Voor"],
            ["een woord omschrijven dat je niet vindt", "Tijdens"],
            ["per deelonderwerp een alinea beginnen", "Tijdens"],
            ["spelling en leestekens nakijken", "Na"],
            ["controleren of alles beantwoord is", "Na"],
        ],
        "Plannen, uitvoeren en controleren.",
    ),
    mk(
        "Welke bronvermelding is volledig genoeg?",
        [
            "Vlaams Instituut Gezond Leven, 'Bewegen', geraadpleegd op 4 maart",
            "Ik vond deze info ergens op een website over bewegen en sport",
            "Google, zoekterm bewegen en gezondheid bij jongeren",
            "Een artikel dat de leerkracht vorige week in de klas toonde",
        ],
        0,
        "Wie, wat en wanneer: zo kan een lezer de bron terugvinden.",
    ),
    casus(
        "Opdracht: \"Schrijf voor de schoolkrant een tekst van ongeveer 250 woorden waarin je uitlegt hoe de nieuwe fietsenstalling werkt.\"",
        [
            mk(
                "Wat is hier het tekstdoel?",
                [
                    "Uitleggen",
                    "Overtuigen",
                    "Creatief zijn met taal",
                    "Je mening geven",
                ],
                0,
                "Het werkwoord uitleggen in de opdracht verraadt het doel.",
            ),
            tabel(
                "Voldoet deze tekst aan de taakvoltooiing?",
                [
                    ("een tekst van 600 woorden over de geschiedenis van de fiets", F),
                    ("een stappenplan met waar je je badge scant en waar je je fiets plaatst", J),
                    ("een betoog waarom fietsen beter is dan de bus", F),
                ],
                "Taakvoltooiing: de tekst doet wat de opdracht vraagt, binnen de gevraagde lengte.",
            ),
            keuze(
                "Een tussentitel of opsomming helpt hier vooral bij [[*de lay-out en de leesbaarheid|de spelling|het register]].",
                "Lay-out ondersteunt de structuur van een tekst.",
            ),
        ],
    ),
    keuze(
        "Op het digitale examen mag je vaak [[*een woordenboek en de spellingcontrole|een vertaalapp met AI|je eigen notities van thuis]] gebruiken.",
        "Wat toegelaten is, gebruik je best ook.",
    ),
    tabel(
        "Is dit een goede alinea-indeling?",
        [
            ("elke nieuwe gedachte een nieuwe alinea", J),
            ("een kernzin die het onderwerp van de alinea noemt", J),
            ("na elke zin een witregel", F),
        ],
        "Een alinea is een blok rond één gedachte.",
    ),
    open_(
        "Herschrijf de klachtbrief van Arne zodat hij aan de criteria voldoet.",
        "Onderwerp: Klacht over defecte fiets gekocht op 3 september\n\nGeachte heer of mevrouw,\nOp 3 september kocht ik in uw winkel in Hasselt een fiets voor 450 euro. Na enkele weken springt de ketting eraf en werken de remmen slecht. Ik vraag u daarom de fiets te herstellen of te vervangen, of mij het aankoopbedrag terug te betalen. Ik kijk uit naar uw antwoord.\nMet vriendelijke groeten\nArne",
    ),
]
