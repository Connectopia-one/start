"""Stijlfiguren en beeldspraak — pittig (🌍 Beyond doorstroom, Nederlands).

Alle voorbeeldzinnen zijn zelf geschreven en worden aan niemand toegeschreven.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TOESPRAAK = (
    "Lees het fragment uit een toespraak van een leerling op de proclamatie.\n\n"
    "\"(1) Zes jaar lang waren deze gangen ons tweede huis. (2) Wij kwamen hier als kinderen, wij vertrekken als volwassenen. "
    "(3) Wij hebben gelachen, wij hebben gehuild, wij hebben gestudeerd tot diep in de nacht. "
    "(4) Duizend keer hebben we gedacht dat we het nooit zouden halen. (5) En was het de moeite waard? "
    "(6) Onze leerkrachten waren niet de slechtste. (7) De tijd vloog voorbij als een zwaluw in de zomer.\""
)

VRAGEN = [
    casus(
        TOESPRAAK,
        [
            tabel(
                "Welke stijlfiguur zit in elke zin?",
                [
                    ("zin 3", "Anafoor"),
                    ("zin 4", "Hyperbool"),
                    ("zin 5", "Retorische vraag"),
                    ("zin 6", "Litotes"),
                ],
                "Herhaling vooraan, overdrijving, een vraag zonder antwoord en een ontkend tegendeel.",
                kolommen=["Anafoor", "Hyperbool", "Retorische vraag", "Litotes"],
            ),
            mk(
                "Welke stijlfiguur zit in zin 2?",
                ["Antithese", "Ellips", "Eufemisme", "Synesthesie"],
                0,
                "Kinderen tegenover volwassenen, komen tegenover vertrekken.",
            ),
            keuze(
                "\"Deze gangen waren ons tweede huis\" in zin 1 is een [[*metafoor|vergelijking|personificatie]].",
                "Het beeld staat in de plaats van de zaak, zonder als of zoals.",
            ),
            keuze(
                "Zin 7 is een [[*vergelijking|metafoor|chiasme]].",
                "Het woordje als verbindt de zaak met het beeld.",
            ),
            mk(
                "Wat bedoelt de spreker met zin 6?",
                [
                    "Dat de leerkrachten erg goed waren",
                    "Dat de leerkrachten matig waren",
                    "Dat er slechtere scholen bestaan",
                    "Dat sommige leerkrachten slecht waren",
                ],
                0,
                "Bij een litotes zeg je iets door het tegendeel te ontkennen.",
            ),
            mk(
                "Waarom zet de spreker zin 5 in?",
                [
                    "De zaal vult zelf het antwoord in",
                    "Hij weet het antwoord niet",
                    "Hij wil een vraag van de zaal",
                    "Hij herhaalt een vraag van de directie",
                ],
                0,
                "Wie zelf tot het antwoord komt, gelooft het sterker.",
            ),
        ],
    ),
    tabel(
        "Welke stijlfiguur is elk voorbeeld?",
        [
            ("\"De wind fluisterde door de bomen.\"", "Personificatie"),
            ("\"het schreeuwende geel van de muren\"", "Synesthesie"),
            ("\"Haast je langzaam.\"", "Paradox"),
            ("\"Ik naar links, hij naar rechts.\"", "Ellips"),
        ],
        "Een menselijke daad voor iets levenloos, twee zintuigen door elkaar, een schijnbare tegenspraak en een weggelaten werkwoord.",
        kolommen=["Personificatie", "Synesthesie", "Paradox", "Ellips"],
    ),
    sorteer(
        "Vergroot of verzacht de stijlfiguur?",
        ["Vergroot", "Verzacht"],
        [
            ["hyperbool", "Vergroot"],
            ["litotes", "Verzacht"],
            ["eufemisme", "Verzacht"],
            ["understatement", "Verzacht"],
        ],
        "Een hyperbool overdrijft. Litotes, eufemisme en understatement zwakken af.",
    ),
    mk(
        "\"Eten om te leven, niet leven om te eten.\" Welke stijlfiguur?",
        ["Chiasme", "Anafoor", "Parallellisme", "Cliché"],
        0,
        "De tweede helft spiegelt de volgorde van de eerste.",
    ),
    tabel(
        "Vergelijking of metafoor?",
        [
            ("\"Zij is zo stil als een steen.\"", "Vergelijking"),
            ("\"Zijn woorden waren messen.\"", "Metafoor"),
            ("\"de voet van de berg\"", "Metafoor"),
            ("\"Hij vecht zoals een leeuw.\"", "Vergelijking"),
        ],
        "In een vergelijking staat een woordje als of zoals.",
        kolommen=["Vergelijking", "Metafoor"],
    ),
    casus(
        "Een reclame voor een nieuwe wagen: \"Een roofdier op vier wielen. Stil als de nacht, snel als de bliksem. Waarom zou je nog wachten?\"",
        [
            tabel(
                "Welke stijlfiguren vind je terug?",
                [
                    ("metafoor", J),
                    ("vergelijking", J),
                    ("retorische vraag", J),
                    ("litotes", F),
                ],
                "Stijlfiguren komen niet enkel in literatuur voor; reclame staat er vol mee.",
            ),
            keuze(
                "\"Stil als de nacht, snel als de bliksem\" volgt twee keer hetzelfde bouwpatroon. Dat heet een [[*parallellisme|chiasme|ellips]].",
                "Dezelfde vorm, twee keer na elkaar.",
            ),
        ],
    ),
    mk(
        "Een buurman noemt het afbranden van zijn schuur \"een klein ongemakje\". Welke stijlfiguur?",
        ["Understatement", "Hyperbool", "Klanknabootsing", "Antithese"],
        0,
        "Een understatement zwakt bewust af wat groot is.",
    ),
    tabel(
        "Klopt dit over beeldspraak?",
        [
            ("Ze komt ook in gewone spreektaal voor.", J),
            ("Ze maakt iets abstracts voelbaar.", J),
            ("Ze komt enkel in poëzie voor.", F),
            ("Een cliché is versleten beeldspraak.", J),
        ],
        "De poot van een tafel en de mond van een rivier: onze taal zit er vol mee.",
    ),
    mk(
        "Een schrijver noemt een overleden vrouw \"heengegaan\". Welke stijlfiguur?",
        ["Eufemisme", "Hyperbool", "Synesthesie", "Paradox"],
        0,
        "Een eufemisme verzacht een harde werkelijkheid.",
    ),
    koppel(
        "Welke stijlfiguur hoort bij elke omschrijving?",
        [
            ["Een woord dat de klank nabootst", "Klanknabootsing"],
            ["Dieren gedragen zich als mensen", "Antropomorfisme"],
            ["Een overeenkomst om iets uit te leggen", "Analogie"],
            ["Een heel verhaal dat voor iets anders staat", "Allegorie"],
        ],
        ["Inversie", "Litotes"],
        "Vier vormen van beeldspraak en klank.",
    ),
    mk(
        "Een krantenkop luidt: \"Storm van kritiek op nieuwe regel\". Wat is \"storm van kritiek\"?",
        [
            "Een cliché",
            "Een paradox",
            "Een chiasme",
            "Een ellips",
        ],
        0,
        "Ooit treffend, nu versleten door veelvuldig gebruik.",
    ),
    tabel(
        "Wat is het effect van een cliché?",
        [
            ("De zin leest vlot.", J),
            ("De zin blijft nauwelijks hangen.", J),
            ("De zin verrast de lezer.", F),
        ],
        "Juist omdat je het al honderd keer hoorde, raakt het niemand meer.",
    ),
    sleep(
        "\"Zacht ging de deur open\" zet het bijwoord vooraan: dat is [[inversie]]. \"Het hart werkt als een pomp\" is een [[analogie]]. \"Sis\" en \"klets\" zijn voorbeelden van [[onomatopee]].",
        ["anafoor", "hyperbool"],
        "Drie stijlfiguren rond zinsbouw, uitleg en klank.",
    ),
    casus(
        "Lees het gedicht.\n\n"
        "Nooit meer de geur van brood,\n"
        "nooit meer de klok die sloeg,\n"
        "nooit meer de stem die riep\n"
        "dat het al laat genoeg.\n\n"
        "Het huis is groot en leeg,\n"
        "de stilte rood en luid.",
        [
            tabel(
                "Welke stijlfiguren vind je in het gedicht terug?",
                [
                    ("anafoor", J),
                    ("synesthesie", J),
                    ("antithese", F),
                    ("paradox", J),
                ],
                "\"Nooit meer\" herhaalt vooraan; \"rood en luid\" mengt zien en horen; een luide stilte spreekt zichzelf schijnbaar tegen.",
            ),
            mk(
                "Wat drukt de anafoor in dit gedicht vooral uit?",
                [
                    "Het gemis dat steeds terugkomt",
                    "Dat het huis te klein geworden is",
                    "Dat de klok nog altijd slaat",
                    "Dat de ik graag verhuist",
                ],
                0,
                "De herhaling vooraan hamert het verlies erin.",
            ),
            keuze(
                "\"Dat het al laat genoeg\": het werkwoord \"was\" ontbreekt. Dat is een [[*ellips|inversie|hyperbool]].",
                "De lezer vult het weggelaten woord zelf aan.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over woordspelingen?",
        [
            ("Ze spelen met dubbele betekenis of klank.", J),
            ("Ze zijn meestal makkelijk te vertalen.", F),
            ("Je hoort twee betekenissen tegelijk.", J),
        ],
        "Daarom valt een woordspeling zelden te vertalen.",
    ),
    mk(
        "\"Wie zwijgt, verliest. Wie spreekt, wint.\" Welke twee stijlfiguren zitten hierin?",
        [
            "Parallellisme en antithese",
            "Chiasme en litotes",
            "Hyperbool en ellips",
            "Synesthesie en een eufemisme",
        ],
        0,
        "Dezelfde bouw twee keer, met tegengestelde inhoud: zwijgen tegenover spreken, verliezen tegenover winnen.",
    ),
    tabel(
        "Is het beeldspraak of een stijlfiguur van herhaling of zinsbouw?",
        [
            ("metafoor", "Beeldspraak"),
            ("personificatie", "Beeldspraak"),
            ("anafoor", "Herhaling of zinsbouw"),
            ("chiasme", "Herhaling of zinsbouw"),
        ],
        "Beeldspraak zet een beeld in de plaats van de zaak; andere stijlfiguren spelen met de bouw.",
        kolommen=["Beeldspraak", "Herhaling of zinsbouw"],
    ),
    mk(
        "In een dierenverhaal draagt een vos een hoed en leest hij de krant. Welk begrip past?",
        ["Antropomorfisme", "Synesthesie", "Understatement", "Retorische vraag"],
        0,
        "Dieren krijgen menselijke gedaante of menselijk gedrag.",
    ),
    keuze(
        "\"Hij is niet van gisteren\" om te zeggen dat iemand slim is, is een [[*litotes|hyperbool|metafoor van een dier]].",
        "Het tegendeel wordt ontkend, en zo klinkt het krachtiger.",
    ),
    tabel(
        "Welke stijlfiguur gebruikt een spreker die het publiek wil overtuigen vooral om ritme te geven?",
        [
            ("anafoor", J),
            ("parallellisme", J),
            ("ellips", F),
        ],
        "Herhaling en dezelfde bouw geven een toespraak ritme en kracht.",
    ),
    mk(
        "Een sportjournalist schrijft: \"De bal smeekte om een doelpunt.\" Welke stijlfiguur?",
        ["Personificatie", "Litotes", "Chiasme", "Parallellisme"],
        0,
        "Een bal kan niet smeken: iets levenloos krijgt een menselijke daad.",
    ),
    open_(
        "Schrijf drie zinnen over een regenachtige maandag: één met een personificatie, één met een hyperbool en één met een litotes. Benoem ze.",
        "Personificatie: de regen tikte ongeduldig op het raam. Hyperbool: ik heb een eeuwigheid op de bus gewacht. Litotes: het was niet bepaald de leukste dag van de week.",
    ),
]
