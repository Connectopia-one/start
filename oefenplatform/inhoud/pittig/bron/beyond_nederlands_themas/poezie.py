"""Poëzie: dichtvormen, strofen en rijm — pittig (🌍 Beyond doorstroom, Nederlands).

Alle gedichten zijn zelf geschreven, zonder naam van een bestaande dichter.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

GEDICHT1 = (
    "Lees het gedicht.\n\n"
    "De zee trekt zich terug, het strand ligt stil,\n"
    "een meeuw schreeuwt hees en zoekt haar weg.\n"
    "Ik weet niet meer wat ik nog wil,\n"
    "wat ik nog voel, wat ik nog zeg.\n\n"
    "Maar morgen komt het water weer,\n"
    "het neemt de sporen van mij mee,\n"
    "en wat ik vandaag zo bitter leer,\n"
    "vergeeft me straks de trouwe zee."
)

GEDICHT2 = (
    "Lees het gedicht.\n\n"
    "de trein\n"
    "vertrekt zonder\n"
    "te wachten op wie\n"
    "nog\n"
    "rent"
)

VRAGEN = [
    casus(
        GEDICHT1,
        [
            mk(
                "Welk rijmschema heeft de eerste strofe?",
                ["abab", "aabb", "abba", "aaaa"],
                0,
                "stil rijmt op wil, weg op zeg: eerste met derde, tweede met vierde.",
            ),
            keuze(
                "Dat rijmschema heet [[*gekruist rijm|gepaard rijm|omarmend rijm]].",
                "De rijmklanken kruisen elkaar.",
            ),
            keuze(
                "Een strofe van vier verzen is een [[*kwatrijn|terzet|distichon]].",
                "Het gedicht bestaat uit twee kwatrijnen.",
            ),
            mk(
                "Waar ligt de wending in de gedachtegang?",
                [
                    "Bij het woord \"Maar\" in vers 5",
                    "Bij de meeuw in vers 2",
                    "In het laatste woord van het gedicht",
                    "Er is geen wending in dit gedicht",
                ],
                0,
                "Van moedeloosheid naar hoop: \"Maar morgen\" slaat een andere richting in. Dat is de volta.",
            ),
            tabel(
                "Klopt dit over het gedicht?",
                [
                    ("Stil en wil vormen volrijm.", J),
                    ("De ik is zeker de dichter zelf.", F),
                    ("Zee, strand, meeuw en water horen tot hetzelfde semantische veld.", J),
                    ("Het gedicht is een sonnet.", F),
                ],
                "Een sonnet telt veertien verzen. Het lyrisch subject is een rol, niet noodzakelijk de dichter.",
            ),
            keuze(
                "\"Hees\" en \"zee\" klinken gelijk in de klinker. Dat heet [[*assonantie|alliteratie|enjambement]].",
                "Assonantie is klinkerrijm.",
            ),
        ],
    ),
    casus(
        GEDICHT2,
        [
            tabel(
                "Wat valt op aan de vorm?",
                [
                    ("De zin loopt over de versgrenzen heen.", J),
                    ("Er is geen rijm.", J),
                    ("Het woord \"nog\" staat alleen op een regel.", J),
                    ("Het is een kwatrijn.", F),
                ],
                "Vrije verzen, enjambement en witruimte dragen hier de vorm.",
            ),
            inv(
                "Hoe noem je het doorlopen van een zin over de versregel heen? Antwoord met één woord.",
                ["enjambement", "het enjambement"],
                "Het woord net na de breuk krijgt extra gewicht.",
            ),
            mk(
                "Wat bereikt de dichter door \"nog\" en \"rent\" elk alleen te zetten?",
                [
                    "Je voelt het rennen en de vertraging",
                    "Het gedicht wordt een limerick",
                    "Het rijmschema wordt omarmend in plaats van gekruist",
                    "Het gedicht krijgt een refrein",
                ],
                0,
                "Wat alleen staat, weegt zwaarder. Wit is een middel, geen leegte.",
            ),
        ],
    ),
    tabel(
        "Hoeveel verzen telt elke strofe?",
        [
            ("distichon", "2"),
            ("terzet", "3"),
            ("kwintet", "5"),
            ("sextet", "6"),
        ],
        "Een octaaf telt er acht, een kwatrijn vier.",
        kolommen=["2", "3", "5", "6"],
    ),
    koppel(
        "Welke dichtvorm hoort bij elke omschrijving?",
        [
            ["Een klaagzang om een verlies", "Elegie"],
            ["Een lofzang", "Ode"],
            ["Drie verzen van vijf, zeven en vijf lettergrepen", "Haiku"],
            ["Vijf grappige verzen op aabba met een pointe", "Limerick"],
        ],
        ["Rondeel", "Ballade"],
        "Vier vaste dichtvormen.",
    ),
    casus(
        "Lees het gedicht.\n\n"
        "Mijn hond is oud, zijn snuit is grijs,\n"
        "hij slaapt het liefst bij het vuur,\n"
        "hij droomt nog van een lange reis,\n"
        "van bos en wind en avontuur.",
        [
            mk(
                "Welk soort rijm hebben grijs en reis?",
                ["Staand rijm", "Slepend rijm", "Stafrijm", "Binnenrijm"],
                0,
                "De klemtoon ligt op de laatste lettergreep: mannelijk of staand rijm.",
            ),
            keuze(
                "Het rijmschema van deze strofe is [[*abab|aabb|abba]].",
                "grijs rijmt op reis, vuur op avontuur.",
            ),
            mk(
                "Bij welke dichtvorm past dit gedicht het best?",
                ["Een dierendicht", "Een minnelied", "Een acrostichon", "Een ode aan een god"],
                0,
                "Een dier staat centraal en krijgt een menselijk trekje: dromen van een reis.",
            ),
        ],
    ),
    tabel(
        "Welk rijmschema hoort bij welke naam?",
        [
            ("aabb", "Gepaard rijm"),
            ("abab", "Gekruist rijm"),
            ("abba", "Omarmend rijm"),
        ],
        "Bij abba omarmt het ene rijm het andere.",
        kolommen=["Gepaard rijm", "Gekruist rijm", "Omarmend rijm"],
    ),
    casus(
        "Lees het gedicht.\n\n"
        "Zon op de ramen\n"
        "Aan het ontbijt zitten we\n"
        "Rustig te zwijgen\n"
        "Altijd jij en ik samen",
        [
            mk(
                "Wat is dit voor een gedicht?",
                ["Een acrostichon", "Een limerick", "Een haiku met vier verzen", "Een rondeel"],
                0,
                "Lees de beginletters van boven naar beneden: ZARA.",
            ),
            inv(
                "Welke naam verbergt het gedicht?",
                ["Zara", "ZARA"],
                "De eerste letters van de verzen vormen samen een naam.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over poëzie?",
        [
            ("Een gedicht zonder rijm en vaste maat kan bestaan.", J),
            ("Een haiku telt vijf verzen.", F),
            ("Parlandopoëzie klinkt alsof iemand gewoon praat.", J),
            ("Een distichon telt drie verzen.", F),
        ],
        "Vrije verzen zijn er volop sinds de twintigste eeuw.",
    ),
    sorteer(
        "Gaat het begrip over klank of over bouw?",
        ["Klank", "Bouw"],
        [
            ["alliteratie", "Klank"],
            ["binnenrijm", "Klank"],
            ["enjambement", "Bouw"],
            ["kwatrijn", "Bouw"],
            ["assonantie", "Klank"],
            ["volta", "Bouw"],
        ],
        "Enjambement gaat over de zin tegenover het vers, niet over klank.",
    ),
    mk(
        "Een ballade eindigt met een korte slotstrofe die zich tot iemand richt. Hoe heet die?",
        ["Een envoi", "Een stok", "Een volta", "Een octaaf"],
        0,
        "Het envoi sluit een ballade of refrein af, vaak met een opdracht.",
    ),
    sleep(
        "In een refrein keert de [[stokregel]] telkens terug. In een rondeel keren bepaalde [[verzen]] letterlijk terug. Een sonnet telt [[veertien]] verzen.",
        ["drie", "strofen"],
        "Herhaling en vaste aantallen bepalen vaste dichtvormen.",
    ),
    mk(
        "Waarom lees je een gedicht best hardop?",
        [
            "Klank en ritme komen dan tot hun recht",
            "Dan hoef je het niet meer te begrijpen",
            "Dan ontdek je wie de dichter van het gedicht is",
            "Dan verdwijnt de witruimte",
        ],
        0,
        "Veel van wat een gedicht doet, zit in het geluid.",
    ),
    casus(
        "Lees het gedicht.\n\n"
        "Wie wacht er aan de poort?\n"
        "De wind, de wind, de wind.\n"
        "Hij roept een oud verloren woord\n"
        "en zoekt een kind.\n\n"
        "Wie wacht er aan de poort?\n"
        "De wind, de wind, de wind.",
        [
            tabel(
                "Wat zie je in dit gedicht?",
                [
                    ("Verzen keren letterlijk terug.", J),
                    ("\"Wind\" rijmt op \"kind\".", J),
                    ("Het gedicht telt veertien verzen.", F),
                ],
                "Door de herhaling draait het gedicht rond zijn as.",
            ),
            mk(
                "Bij welke dichtvorm sluit deze bouw het best aan?",
                ["Het rondeel", "De haiku", "De limerick", "Het acrostichon"],
                0,
                "In een rondeel keren bepaalde verzen letterlijk terug.",
            ),
            keuze(
                "De herhaalde regel \"De wind, de wind, de wind\" werkt in dit gedicht als [[*een refrein|een envoi|een volta]].",
                "Een regel die steeds terugkeert, geeft het gedicht een liedachtige draaiing.",
            ),
        ],
    ),
    tabel(
        "Staand of slepend rijm?",
        [
            ("hand en land", "Staand"),
            ("lopen en hopen", "Slepend"),
            ("water en later", "Slepend"),
            ("boom en stroom", "Staand"),
        ],
        "Bij slepend rijm volgt er nog een doffe lettergreep na de klemtoon.",
        kolommen=["Staand", "Slepend"],
    ),
    mk(
        "Een gedicht prijst met verheven woorden een oude eik in het dorp. Welke vorm?",
        ["Een ode", "Een elegie", "Een limerick", "Een envoi"],
        0,
        "Een ode bezingt iemand of iets. Een elegie treurt.",
    ),
    tabel(
        "Klopt dit over slampoetry?",
        [
            ("Het leeft van de stem en het publiek.", J),
            ("Het moet je vooral op papier zien staan.", F),
            ("Het wordt vaak op een podium gebracht.", J),
        ],
        "Een kalligram moet je net zien; slampoetry moet je horen.",
    ),
    inv(
        "Een sonnet opent klassiek met een strofe van acht verzen. Hoe heet die? Antwoord met één woord.",
        ["octaaf", "octet", "het octaaf"],
        "Na het octaaf volgt het sextet, en daartussen ligt vaak de volta.",
    ),
    open_(
        "Schrijf zelf een kwatrijn met gekruist rijm over je school of je straat, en duid het rijmschema aan.",
        "De bel gaat schel, de gangen vol (a)\nmet stemmen, tassen, natte jassen. (b)\nDe leraar zucht: het lokaal is dol, (a)\ntot iedereen weer zit in klassen. (b)\nRijmschema: abab, gekruist rijm.",
    ),
]
