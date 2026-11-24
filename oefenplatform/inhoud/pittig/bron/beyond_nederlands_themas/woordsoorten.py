"""Woordsoorten — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lees de zin.\n\n\"Gisteren kocht mijn zus drie oude boeken in de winkel die naast het station ligt.\"",
        [
            tabel(
                "Welke woordsoort is elk woord in deze zin?",
                [
                    ("Gisteren", "Bijwoord"),
                    ("mijn", "Voornaamwoord"),
                    ("drie", "Telwoord"),
                    ("oude", "Bijvoeglijk naamwoord"),
                ],
                "Gisteren zegt wanneer, mijn geeft bezit aan, drie telt en oude zegt iets over boeken.",
                kolommen=["Bijwoord", "Voornaamwoord", "Telwoord", "Bijvoeglijk naamwoord"],
            ),
            keuze(
                "\"Die\" is in deze zin een [[*betrekkelijk|aanwijzend|vragend]] voornaamwoord.",
                "Die wijst terug naar winkel en leidt de bijzin in.",
            ),
            keuze(
                "Het antecedent van \"die\" is [[*winkel|station|boeken]].",
                "Het antecedent is het woord waarnaar het betrekkelijk voornaamwoord terugwijst.",
            ),
            tabel(
                "Welke woordsoort is elk woord?",
                [
                    ("in", "Voorzetsel"),
                    ("naast", "Voorzetsel"),
                    ("winkel", "Zelfstandig naamwoord"),
                    ("kocht", "Werkwoord"),
                ],
                "Voorzetsels leggen een verband van plaats, tijd of richting.",
                kolommen=["Voorzetsel", "Zelfstandig naamwoord", "Werkwoord"],
            ),
        ],
    ),
    casus(
        "Vergelijk de twee zinnen.\n\nA. \"Het meisje loopt snel.\"\nB. \"Het snelle meisje wint.\"",
        [
            tabel(
                "Welke woordsoort heeft elk woord in de twee zinnen?",
                [
                    ("snel in zin A", "Bijwoord"),
                    ("snelle in zin B", "Bijvoeglijk naamwoord"),
                    ("meisje in beide zinnen", "Zelfstandig naamwoord"),
                ],
                "In A hoort snel bij het werkwoord, in B bij het zelfstandig naamwoord.",
                kolommen=["Bijwoord", "Bijvoeglijk naamwoord", "Zelfstandig naamwoord"],
            ),
            mk(
                "Wat leer je uit deze twee zinnen?",
                [
                    "De rol in de zin bepaalt de woordsoort",
                    "Een woord heeft altijd één vaste woordsoort",
                    "Bijwoorden staan altijd achteraan in de zin",
                    "Bijvoeglijke naamwoorden krijgen nooit een e",
                ],
                0,
                "Hetzelfde woord kan in twee zinnen een andere woordsoort zijn.",
            ),
            keuze(
                "\"Het\" is in beide zinnen een [[*lidwoord|persoonlijk voornaamwoord|bijwoord]].",
                "Het staat voor een zelfstandig naamwoord: het meisje.",
            ),
        ],
    ),
    tabel(
        "Lidwoord of persoonlijk voornaamwoord?",
        [
            ("Het regent al de hele dag.", "Persoonlijk voornaamwoord"),
            ("Het huis staat leeg.", "Lidwoord"),
            ("Ik vind het niet leuk.", "Persoonlijk voornaamwoord"),
        ],
        "Staat het voor een zelfstandig naamwoord, dan is het een lidwoord.",
        kolommen=["Lidwoord", "Persoonlijk voornaamwoord"],
    ),
    tabel(
        "Welk soort werkwoord is wordt, heeft, heeft en blijft in deze zinnen?",
        [
            ("Zij wordt dokter.", "Koppelwerkwoord"),
            ("Zij heeft hard gewerkt.", "Hulpwerkwoord"),
            ("Zij heeft een nieuwe fiets.", "Zelfstandig werkwoord"),
            ("Het weer blijft mooi.", "Koppelwerkwoord"),
        ],
        "In de eerste en de laatste zin staat het werkwoord vooraan: wordt en blijft. Hebben is hulpwerkwoord bij gewerkt, maar zelfstandig in de derde zin.",
        kolommen=["Koppelwerkwoord", "Hulpwerkwoord", "Zelfstandig werkwoord"],
    ),
    koppel(
        "Welk soort voornaamwoord is het vetgedrukte woord?",
        [
            ["Hij wast zich.", "Wederkerend"],
            ["Ze helpen elkaar.", "Wederkerig"],
            ["Deze fiets is van mij.", "Aanwijzend"],
            ["Wie heeft dat gedaan?", "Vragend"],
        ],
        ["Bezittelijk", "Betrekkelijk"],
        "Bij wederkerend keert de handeling terug op het onderwerp; bij wederkerig gaat ze over en weer.",
    ),
    sorteer(
        "Voegwoord, voorzetsel of bijwoord?",
        ["Voegwoord", "Voorzetsel", "Bijwoord"],
        [
            ["omdat", "Voegwoord"],
            ["hoewel", "Voegwoord"],
            ["tijdens", "Voorzetsel"],
            ["achter", "Voorzetsel"],
            ["zeer", "Bijwoord"],
            ["echter", "Bijwoord"],
        ],
        "Voegwoorden verbinden zinnen, voorzetsels staan voor een naamwoord, bijwoorden zeggen iets over een ander woord of de zin.",
    ),
    mk(
        "\"Oei, ik ben mijn sleutels vergeten!\" Welke woordsoort is \"oei\"?",
        ["Tussenwerpsel", "Bijwoord", "Voegwoord", "Telwoord van rang"],
        0,
        "Het staat los van de zinsbouw en drukt een gevoel uit.",
    ),
    tabel(
        "Hoofdtelwoord of rangtelwoord?",
        [
            ("vijf", "Hoofdtelwoord"),
            ("vijfde", "Rangtelwoord"),
            ("honderd", "Hoofdtelwoord"),
            ("eerste", "Rangtelwoord"),
        ],
        "Een hoofdtelwoord telt, een rangtelwoord ordent.",
        kolommen=["Hoofdtelwoord", "Rangtelwoord"],
    ),
    keuze(
        "In \"Dat is de buurvrouw wier hond altijd blaft\" is \"wier\" een [[*betrekkelijk|aanwijzend|wederkerend]] voornaamwoord dat ook bezit uitdrukt.",
        "Het verwijst terug naar buurvrouw en leidt de bijzin in.",
    ),
    tabel(
        "Klopt dit over de woordsoorten?",
        [
            ("Een lidwoord hoort bij een zelfstandig naamwoord.", J),
            ("Een hulpwerkwoord kan alleen staan zonder ander werkwoord.", F),
            ("Een voltooid deelwoord begint vaak met ge-.", J),
            ("Deze, die en dat zijn bezittelijke voornaamwoorden.", F),
        ],
        "Deze, die en dat zijn aanwijzend.",
    ),
    casus(
        "Lees de zin.\n\n\"Hoewel het erg koud was, bleven we heel lang buiten spelen.\"",
        [
            tabel(
                "Welke woordsoort hebben hoewel, erg, koud en we?",
                [
                    ("Hoewel", "Voegwoord"),
                    ("erg", "Bijwoord"),
                    ("koud", "Bijvoeglijk naamwoord"),
                    ("we", "Voornaamwoord"),
                ],
                "Erg zegt iets over koud en is dus een bijwoord; koud zegt iets over het onderwerp het.",
                kolommen=["Voegwoord", "Bijwoord", "Bijvoeglijk naamwoord", "Voornaamwoord"],
            ),
            keuze(
                "\"Hoewel\" leidt hier een bijzin in die een [[*toegeving|oorzaak|tijd]] uitdrukt.",
                "Hoewel geeft aan dat iets gebeurt ondanks iets anders.",
            ),
        ],
    ),
    inv(
        "Hoe noem je de onvervoegde vorm \"zwemmen\", zoals die in het woordenboek staat? Antwoord met één woord.",
        ["infinitief", "de infinitief", "onbepaalde wijs"],
        "De infinitief is de grondvorm van het werkwoord.",
    ),
    mk(
        "Waarom is het belangrijk te weten of \"is\" een koppelwerkwoord is?",
        [
            "Dan is er een naamwoordelijk gezegde",
            "Dan krijgt het woord een hoofdletter",
            "Dan is er geen onderwerp in de zin",
            "Dan moet je het werkwoord met dt schrijven",
        ],
        0,
        "Bij een koppelwerkwoord hoort een naamwoordelijk deel van het gezegde.",
    ),
    sleep(
        "In \"de fiets die ik kocht\" is \"fiets\" het [[antecedent]] en \"die\" een [[betrekkelijk]] voornaamwoord. \"Mijn\" in \"mijn fiets\" is [[bezittelijk]].",
        ["aanwijzend", "lidwoord"],
        "Voornaamwoorden en hun verwijzing.",
    ),
    mk(
        "Welke woordsoort is \"want\" in \"Ik blijf thuis, want ik ben ziek\"?",
        ["Voegwoord", "Voorzetsel", "Bijwoord van reden", "Tussenwerpsel"],
        0,
        "Want verbindt twee zinnen: een nevenschikkend voegwoord.",
    ),
    tabel(
        "Klopt dit over voornaamwoorden?",
        [
            ("In \"deze is van mij\" is deze zelfstandig gebruikt.", J),
            ("In \"deze fiets\" is deze bijvoeglijk gebruikt.", J),
            ("\"Elkaar\" is een wederkerend voornaamwoord.", F),
        ],
        "Elkaar is wederkerig: de handeling gaat over en weer.",
    ),
    mk(
        "In \"Hij heeft een fiets\" is \"heeft\":",
        ["Een zelfstandig werkwoord", "Een hulpwerkwoord van de voltooide tijd", "Een koppelwerkwoord", "Een tussenwerpsel"],
        0,
        "Zonder ander werkwoord draagt hebben zelf de betekenis.",
    ),
    sorteer(
        "Welk woord is een zelfstandig naamwoord?",
        ["Zelfstandig naamwoord", "Geen zelfstandig naamwoord"],
        [
            ["vrijheid", "Zelfstandig naamwoord"],
            ["het zwemmen (in \"het zwemmen is gezond\")", "Zelfstandig naamwoord"],
            ["zwemmen (in \"wij zwemmen\")", "Geen zelfstandig naamwoord"],
            ["vrij", "Geen zelfstandig naamwoord"],
        ],
        "Staat er een lidwoord voor, dan is een woord zelfstandig gebruikt.",
    ),
    keuze(
        "\"Welk\" in \"Welk boek lees je?\" is een [[*vragend|betrekkelijk|bezittelijk]] voornaamwoord.",
        "Het leidt een vraag in.",
    ),
    tabel(
        "Krijgt het voltooid deelwoord ge-?",
        [
            ("lopen: gelopen", J),
            ("verwachten: verwacht", F),
            ("werken: gewerkt", J),
            ("beloven: beloofd", F),
        ],
        "Werkwoorden met een onbeklemtoond voorvoegsel zoals ver- en be- krijgen geen ge-.",
    ),
    tabel(
        "Welke woordsoort is \"van\", \"en\" en \"au\"?",
        [
            ("van in \"de deur van het huis\"", "Voorzetsel"),
            ("en in \"brood en kaas\"", "Voegwoord"),
            ("au in \"Au, dat doet pijn\"", "Tussenwerpsel"),
        ],
        "Drie kleine woorden, drie woordsoorten.",
        kolommen=["Voorzetsel", "Voegwoord", "Tussenwerpsel"],
    ),
    mk(
        "Waarom helpt het om woordsoorten te kennen bij de werkwoordspelling?",
        [
            "Je herkent het werkwoord en zijn vorm",
            "Je hoeft dan geen stam meer te zoeken",
            "Alle werkwoorden krijgen dan een d",
            "Je kan dan elk woord met dt schrijven",
        ],
        0,
        "Wie ziet welk woord het werkwoord is en welke rol het speelt, spelt het correcter.",
    ),
    inv(
        "Het woord waarnaar een betrekkelijk voornaamwoord terugwijst, heet het ... Antwoord met één woord.",
        ["antecedent", "het antecedent"],
        "In \"de fiets die ik kocht\" is fiets het antecedent.",
    ),
    open_(
        "Leg uit waarom \"morgen\" in \"We vertrekken morgen\" een bijwoord is, maar in \"De morgen was koud\" niet.",
        "In de eerste zin zegt morgen wanneer het vertrekken gebeurt; het hoort bij het werkwoord, dus het is een bijwoord. In de tweede zin staat er een lidwoord voor en is het onderwerp van de zin: daar is het een zelfstandig naamwoord.",
    ),
]
