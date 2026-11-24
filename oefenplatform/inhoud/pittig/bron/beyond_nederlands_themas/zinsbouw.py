"""Zinsontleding en zinsbouw — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Ontleed de zin.\n\n\"Gisteren gaf de juf de kinderen in de klas een moeilijke toets.\"",
        [
            tabel(
                "Welk zinsdeel is elk stuk?",
                [
                    ("de juf", "Onderwerp"),
                    ("gaf", "Gezegde"),
                    ("een moeilijke toets", "Lijdend voorwerp"),
                    ("de kinderen", "Meewerkend voorwerp"),
                ],
                "Wie gaf? De juf. Wat gaf ze? Een toets. Aan wie? De kinderen.",
                kolommen=["Onderwerp", "Gezegde", "Lijdend voorwerp", "Meewerkend voorwerp"],
            ),
            keuze(
                "\"In de klas\" is een bijwoordelijke bepaling die antwoordt op de vraag [[*waar?|wanneer?|wie of wat?]].",
                "Een bijwoordelijke bepaling zegt iets over de omstandigheden.",
            ),
            keuze(
                "Omdat \"Gisteren\" vooraan staat, staat het onderwerp na de persoonsvorm. Dat is [[*inversie|een tangconstructie|onderschikking]].",
                "Het Nederlands is een tweedepositietaal.",
            ),
        ],
    ),
    casus(
        "Vergelijk de twee zinnen.\n\nA. \"De hond bijt de postbode.\"\nB. \"De postbode wordt door de hond gebeten.\"",
        [
            keuze(
                "Zin B is [[*passief|actief|bevelend]]: het onderwerp ondergaat de handeling.",
                "\"Wordt gebeten\" verraadt de lijdende vorm.",
            ),
            mk(
                "Welk zinsdeel is \"door de hond\" in zin B?",
                [
                    "Handelend voorwerp",
                    "Lijdend voorwerp",
                    "Meewerkend voorwerp",
                    "Voorzetselvoorwerp",
                ],
                0,
                "De uitvoerder in een passieve zin, met door.",
            ),
            keuze(
                "\"De postbode\" is in zin A het lijdend voorwerp en in zin B het [[*onderwerp|meewerkend voorwerp|handelend voorwerp]].",
                "Bij het omzetten naar passief wordt het lijdend voorwerp onderwerp.",
            ),
        ],
    ),
    tabel(
        "Enkelvoudig of samengesteld?",
        [
            ("Hij komt en zij blijft.", "Samengesteld"),
            ("De oude man met de hoed wandelt elke ochtend langs de rivier.", "Enkelvoudig"),
            ("Toen hij kwam, zweeg iedereen.", "Samengesteld"),
            ("Morgen vertrekken wij naar zee.", "Enkelvoudig"),
        ],
        "Het aantal persoonsvormen bepaalt het aantal zinnen, niet de lengte.",
        kolommen=["Enkelvoudig", "Samengesteld"],
    ),
    sorteer(
        "Nevenschikking of onderschikking?",
        ["Nevenschikking", "Onderschikking"],
        [
            ["Ik blijf thuis, want het regent.", "Nevenschikking"],
            ["Ik blijf thuis omdat het regent.", "Onderschikking"],
            ["Hij lacht, maar zij huilt.", "Nevenschikking"],
            ["Hoewel ze moe was, liep ze door.", "Onderschikking"],
        ],
        "Want en maar verbinden twee gelijkwaardige hoofdzinnen; omdat en hoewel leiden een bijzin in.",
    ),
    mk(
        "Waar staat de persoonsvorm in \"...omdat hij elke dag naar school fietst\"?",
        ["Achteraan", "Op de tweede plaats", "Vooraan", "Er is geen persoonsvorm"],
        0,
        "In een bijzin staat de persoonsvorm meestal achteraan.",
    ),
    casus(
        "Lees de zin.\n\n\"Hij heeft het boek dat zijn grootmoeder hem voor zijn verjaardag in een kleine boekhandel in Brugge had gekocht nog altijd niet gelezen.\"",
        [
            mk(
                "Wat maakt deze zin moeilijk te volgen?",
                [
                    "Een lange tangconstructie",
                    "Er staat geen onderwerp in",
                    "De zin is passief",
                    "Er staat geen persoonsvorm in",
                ],
                0,
                "\"Heeft\" en \"gelezen\" staan heel ver uit elkaar.",
            ),
            keuze(
                "Je maakt de zin leesbaarder door [[*de bijzin te verplaatsen of op te splitsen|meer bijzinnen toe te voegen|de persoonsvorm weg te laten]].",
                "Bijvoorbeeld: Zijn grootmoeder kocht hem een boek in Brugge. Hij heeft het nog altijd niet gelezen.",
            ),
        ],
    ),
    koppel(
        "Welke zinssoort is elke zin?",
        [
            ["Kom je ook?", "Vragende zin"],
            ["Sluit de deur!", "Bevelende zin"],
            ["Wat een mooie dag!", "Uitroepende zin"],
            ["De les begint om negen uur.", "Mededelende zin"],
        ],
        ["Beschrijvende zin", "Passieve zin"],
        "Zinssoorten naar hun bedoeling.",
    ),
    tabel(
        "Welk voorwerp is het deel tussen haakjes?",
        [
            ("Ze denkt (aan haar vakantie).", "Voorzetselvoorwerp"),
            ("Ze leest (een boek).", "Lijdend voorwerp"),
            ("Ze geeft (haar broer) een cadeau.", "Meewerkend voorwerp"),
        ],
        "Denken aan heeft een vast voorzetsel; aan wie geeft ze iets, is het meewerkend voorwerp.",
        kolommen=["Lijdend voorwerp", "Meewerkend voorwerp", "Voorzetselvoorwerp"],
    ),
    tabel(
        "Klopt dit over zinsontleding?",
        [
            ("Elke zin heeft een lijdend voorwerp.", F),
            ("Een zinsdeel kan uit één woord bestaan.", J),
            ("Het werkwoordelijk gezegde bestaat uit alle werkwoorden samen.", J),
            ("Wat je samen kan verplaatsen, vormt één zinsdeel.", J),
        ],
        "\"Hij slaapt\" heeft geen lijdend voorwerp.",
    ),
    mk(
        "In \"Mijn broer is sinds gisteren erg ziek\" is \"is ... ziek\":",
        [
            "Een naamwoordelijk gezegde",
            "Een werkwoordelijk gezegde",
            "Een lijdend voorwerp met een bepaling",
            "Een handelend voorwerp",
        ],
        0,
        "Een koppelwerkwoord met een naamwoordelijk deel.",
    ),
    inv(
        "Welk woord in \"De kinderen spelen buiten\" is de persoonsvorm?",
        ["spelen"],
        "De persoonsvorm verandert mee met het onderwerp en de tijd.",
    ),
    mk(
        "Waarom helpt zinsontleding bij de werkwoordspelling?",
        [
            "Je vindt het onderwerp bij de persoonsvorm",
            "Je ziet meteen welk lidwoord je nodig hebt in de zin",
            "Je hoeft dan de stam niet meer te zoeken",
            "Je weet dan of er een komma moet staan",
        ],
        0,
        "Wie het onderwerp niet vindt, weet niet of er een t bij moet.",
    ),
    sleep(
        "In een gewone mededelende hoofdzin staat de persoonsvorm op de [[tweede]] plaats. Staat er iets anders dan het onderwerp vooraan, dan treedt [[inversie]] op. In een bijzin staat de persoonsvorm meestal [[achteraan]].",
        ["eerste", "vooraan"],
        "Woordvolgorde in het Nederlands.",
    ),
    casus(
        "Ontleed de zin.\n\n\"Volgende week wordt de nieuwe sporthal door de burgemeester geopend.\"",
        [
            tabel(
                "Welk zinsdeel is elk stuk van de zin over de sporthal?",
                [
                    ("de nieuwe sporthal", "Onderwerp"),
                    ("wordt geopend", "Gezegde"),
                    ("door de burgemeester", "Handelend voorwerp"),
                    ("Volgende week", "Bijwoordelijke bepaling"),
                ],
                "In een passieve zin staat de uitvoerder met door.",
                kolommen=["Onderwerp", "Gezegde", "Handelend voorwerp", "Bijwoordelijke bepaling"],
            ),
            mk(
                "Hoe luidt de zin in de actieve vorm?",
                [
                    "Volgende week opent de burgemeester de nieuwe sporthal.",
                    "Volgende week wordt de burgemeester door de sporthal geopend.",
                    "De nieuwe sporthal opent volgende week de burgemeester.",
                    "Volgende week is de nieuwe sporthal door de burgemeester open.",
                ],
                0,
                "Het handelend voorwerp wordt onderwerp, het onderwerp wordt lijdend voorwerp.",
            ),
        ],
    ),
    tabel(
        "Welke zin is ontkennend?",
        [
            ("Hij komt niet.", J),
            ("Niemand heeft het gezien.", J),
            ("Hij komt morgen.", F),
        ],
        "Woorden als niet en niemand maken een zin ontkennend.",
    ),
    mk(
        "Hoe test je of \"de oude man met de hoed\" één zinsdeel is?",
        [
            "Je verplaatst het samen naar voren",
            "Je telt het aantal woorden in de groep",
            "Je zoekt het lidwoord",
            "Je zet de hele groep in het meervoud",
        ],
        0,
        "Wat je alleen samen kan verplaatsen, hoort samen.",
    ),
    tabel(
        "Leidt dit woord een bijzin in?",
        [
            ("omdat", J),
            ("hoewel", J),
            ("die", J),
            ("en", F),
        ],
        "En is nevenschikkend.",
    ),
    keuze(
        "In \"Hij zou gisteren gekomen zijn\" vormen [[*zou, gekomen en zijn|enkel zou|gisteren en zou]] samen het werkwoordelijk gezegde.",
        "Alle werkwoorden samen vormen het gezegde.",
    ),
    tabel(
        "Waarom wissel je in een tekst af tussen korte en lange zinnen?",
        [
            ("Enkel korte zinnen gaat hakkelen.", J),
            ("Enkel lange zinnen vermoeit de lezer.", J),
            ("Afwisseling houdt een tekst levendig.", J),
            ("Lange zinnen zijn altijd fout.", F),
        ],
        "Variatie in zinsbouw is een criterium bij schrijven.",
    ),
    inv(
        "In \"Hij geeft zijn zus een boek\": welk zinsdeel is \"zijn zus\"? Vul aan: het ... voorwerp.",
        ["meewerkend", "meewerkende"],
        "Aan wie geeft hij het boek? Aan zijn zus.",
    ),
    tabel(
        "Kan deze zin zonder het deel tussen haakjes?",
        [
            ("Hij slaapt (in de zetel).", J),
            ("(Hij) slaapt in de zetel.", F),
            ("Ze las (gisteren) een boek.", J),
        ],
        "Alleen onderwerp en gezegde zijn echt onmisbaar.",
    ),
    mk(
        "In \"Op mijn hulp kan je altijd rekenen\" is \"op mijn hulp\":",
        ["Een voorzetselvoorwerp", "Een meewerkend voorwerp", "Een handelend voorwerp", "Een onderwerp"],
        0,
        "Rekenen op heeft een vast voorzetsel.",
    ),
    keuze(
        "\"Morgen vertrekken wij\": het onderwerp \"wij\" staat [[*na|voor|zonder]] de persoonsvorm.",
        "Er staat iets anders vooraan, dus inversie.",
    ),
    open_(
        "Schrijf een tekst van drie zinnen over je weekend met afwisseling in zinsbouw: één enkelvoudige zin, één zin met nevenschikking en één met onderschikking.",
        "Zaterdag ging ik naar de markt. Ik kocht appels, maar de peren waren op. Omdat het zondag regende, bleef ik thuis met een boek.",
    ),
]
