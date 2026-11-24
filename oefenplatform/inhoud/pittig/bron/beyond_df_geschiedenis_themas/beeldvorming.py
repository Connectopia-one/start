"""Beeldvorming, standplaatsgebondenheid en betekenisgeving — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="septemberdagen-1830.webp", zelf=False,
         wat="Gustaf Wappers, 'Episode uit de Septemberdagen 1830' (Beyond doorstroom).",
         vragen="betekenisgeving door een jonge staat"),
]

VRAGEN = [
    # --- beeldvorming
    tabel(
        "Waar komt jouw beeld van de middeleeuwen vandaan?",
        [
            ("Uit films en reeksen", J),
            ("Uit handboeken", J),
            ("Uit verhalen in je gezin en omgeving", J),
            ("Enkel uit wetenschappelijk onderzoek", F),
        ],
        "Beeldvorming komt uit veel kanalen. Wie dat niet beseft, houdt zijn eigen beeld voor de geschiedenis zelf.",
    ),
    casus(
        "Twee ooggetuigen beschrijven dezelfde staking in 1886. De fabrikant: \"Een woeste bende vernielde mijn machines.\" Een arbeidster: \"Hongerige mensen eisten brood. Het leger schoot.\"",
        [
            mk(
                "Waarom beschrijven ze dezelfde gebeurtenis zo anders?",
                [
                    "Elk stond elders en had een ander belang",
                    "Een van beiden moet zeker liegen",
                    "Ze beschrijven twee verschillende stakingen",
                    "Ooggetuigen zijn nooit bruikbaar",
                ],
                0,
                "Twee eerlijke getuigen kunnen verschillen zonder dat een van beide liegt.",
            ),
            inv(
                "Hoe noem je het verschijnsel dat tijd, afkomst, geloof en belang mee bepalen wat iemand ziet?",
                ["standplaatsgebondenheid", "de standplaatsgebondenheid", "standplaatsgebonden"],
                "Iedereen kijkt van waar hij zelf staat, ook een historicus van vandaag.",
            ),
            tabel(
                "Een historicus wil deze staking met multiperspectiviteit onderzoeken. Welke bronnen zoekt hij nog?",
                [
                    ("Het verslag van de burgemeester", J),
                    ("Een brief van een soldaat die er was", J),
                    ("Een krant van een andere strekking", J),
                    ("Een tweede verslag van dezelfde fabrikant", F),
                ],
                "Multiperspectiviteit: dezelfde gebeurtenis bekijken vanuit verschillende standpunten.",
            ),
        ],
    ),
    mk(
        "Een handboek schrijft: \"In 1960 gaf België Congo de onafhankelijkheid.\" Welke kritiek past het best?",
        [
            "De zin is eurocentrisch",
            "De zin is een anachronisme",
            "De zin bevat een rekenfout",
            "De zin is negationisme",
        ],
        0,
        "België staat als handelende partij centraal. De Congolezen die zelfbestuur eisten, verdwijnen uit beeld.",
    ),
    tabel(
        "Stereotype, vooroordeel of geen van beide?",
        [
            ("\"Alle Italianen zijn luidruchtig.\"", "Stereotype"),
            ("\"Alle Italianen zijn luidruchtig en dus onbeleefd.\"", "Vooroordeel"),
            ("\"In 1946 kwamen Italiaanse mijnwerkers naar België.\"", "Geen van beide"),
        ],
        "Een stereotype vereenvoudigt een groep. Komt er een waardeoordeel bij, dan is het een vooroordeel.",
        kolommen=["Stereotype", "Vooroordeel", "Geen van beide"],
    ),
    mk(
        "Een reclame uit 1950 toont Afrikanen steeds als lachende dragers voor een witte reiziger. Wat doet zo'n beeld?",
        [
            "Het versterkt een stereotype",
            "Het geeft een neutraal beeld van Afrika",
            "Het is een primaire bron over Afrika in 1300",
            "Het toont alle perspectieven tegelijk",
        ],
        0,
        "Wie beelden maakt, kiest wat je te zien krijgt.",
    ),
    tabel(
        "Wat hoort bij historische empathie, en wat niet?",
        [
            ("Je probeert te begrijpen waarom mensen toen zo handelden.", J),
            ("Je plaatst hun keuzes in de kennis en normen van hun tijd.", J),
            ("Begrijpen betekent goedkeuren.", F),
            ("Je kan iets verklaren en tegelijk scherp afkeuren.", J),
        ],
        "Begrijpen is niet goedkeuren.",
    ),
    mk(
        "Over het koloniale verleden wordt vandaag anders geschreven dan vijftig jaar geleden. Waarom?",
        [
            "Nieuwe vragen en bronnen geven een ander beeld",
            "Het verleden zelf is veranderd",
            "Alle oude bronnen zijn verdwenen",
            "Historici mogen niet meer over Congo schrijven",
        ],
        0,
        "Het verleden verandert niet, het beeld ervan wel.",
    ),
    casus(
        "Een Belgisch handboek uit 1965 en een Congolees handboek uit 2010 beschrijven allebei 30 juni 1960.",
        [
            mk(
                "Wat verwacht je?",
                [
                    "Dezelfde feiten met een andere nadruk",
                    "Twee helemaal verschillende datums",
                    "Exact dezelfde tekst",
                    "Dat een van beide de onafhankelijkheid ontkent",
                ],
                0,
                "Andere hoofdrollen, andere nadruk, dezelfde feiten.",
            ),
            tabel(
                "Welke uitspraken over handboeken kloppen?",
                [
                    ("Een handboek maakt keuzes over wat erin staat.", J),
                    ("Het is geschreven in een bepaalde tijd met bepaalde vragen.", J),
                    ("Een handboek is altijd volledig en neutraal.", F),
                ],
                "Daarom is het nuttig te weten wie een geschiedenis geschreven heeft.",
            ),
        ],
    ),
    mk(
        "Je bekijkt een film over de Tweede Wereldoorlog uit 1960. Waarvoor is die film vooral een goede bron?",
        [
            "Hoe men in 1960 naar de oorlog keek",
            "Wat elke soldaat in 1944 precies zei",
            "De echte gevechten aan het front",
            "De toekomst van Europa na 2000",
        ],
        0,
        "Een film zegt veel over de tijd waarin hij gemaakt werd.",
    ),
    # --- betekenisgeving
    sorteer(
        "Is het geschiedenis of herinnering?",
        ["Geschiedenis", "Herinnering"],
        [
            ["een studie op basis van archieven", "Geschiedenis"],
            ["een herdenking op 11 november", "Herinnering"],
            ["een bloemenneerlegging bij een monument", "Herinnering"],
            ["het vergelijken van bronnen", "Geschiedenis"],
        ],
        "Geschiedenis onderzoekt, herinnering wordt beleefd. Herinnering is zelf wel een onderwerp voor onderzoek.",
    ),
    tabel(
        "Waarin toont een samenleving welke waarde ze aan haar verleden hecht?",
        [
            ("Feestdagen en herdenkingen", J),
            ("Standbeelden en straatnamen", J),
            ("Beschermd erfgoed", J),
            ("De weersvoorspelling", F),
        ],
        "Betekenisgeving is de waarde die een samenleving aan haar verleden toekent.",
    ),
    casus(
        "Bekijk het schilderij. De Belgische staat bestelde in 1834 dit werk van Gustaf Wappers over de septemberdagen van 1830. Het hing later in een museum en stond in schoolboeken.",
        [
            met_prent("septemberdagen-1830.webp", mk(
                "Wat deed de jonge staat met dit schilderij?",
                [
                    "Het gaf betekenis aan zijn ontstaan",
                    "Het onderzocht neutraal wat er gebeurde",
                    "Het ontkende de revolutie van 1830",
                    "Het bekritiseerde de opstandelingen",
                ],
                0,
                "De staat koos een heldhaftig beeld van 1830. Dat is betekenisgeving.",
            )),
            tabel(
                "Mag je dit besluiten?",
                [
                    ("Het schilderij vertelt veel over hoe België zichzelf wilde zien.", "Mag"),
                    ("Het schilderij toont precies hoe de gevechten verliepen.", "Mag niet"),
                    ("De staat wilde met dit werk de opstand eren.", "Mag"),
                    ("Wappers zag elk gevecht met eigen ogen.", "Mag niet"),
                ],
                "Een kunstwerk is vooral een bron over de ideeën van zijn eigen tijd.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    mk(
        "Welke gebeurtenis herdenkt België op 11 november?",
        [
            "De wapenstilstand van 1918",
            "De onafhankelijkheid van België",
            "De val van de Berlijnse Muur",
            "De eedaflegging van Leopold I",
        ],
        0,
        "Een herdenking kiest wie en wat herdacht wordt.",
    ),
    tabel(
        "Wat klopt over de keuzes die een land maakt bij het herdenken?",
        [
            ("Wat een land herdenkt, kan in de tijd veranderen.", J),
            ("De slachtoffers van de kolonisatie komen pas sinds kort in de Belgische herdenkingen voor.", J),
            ("Een herdenking is hetzelfde als historisch onderzoek.", F),
        ],
        "Herdenken is kiezen. Die keuzes zeggen iets over de tijd waarin men herdenkt.",
    ),
    tabel(
        "Is het erfgoed?",
        [
            ("Een oud gebouw", J),
            ("Een landschap", J),
            ("Een ambacht dat doorgegeven wordt", J),
            ("Een gebruik zoals een jaarlijkse stoet", J),
            ("Een nieuwe smartphone uit de winkel", F),
        ],
        "Erfgoed is wat uit het verleden bewaard en doorgegeven wordt, ook gebruiken en ambachten.",
    ),
    # --- omstreden
    casus(
        "In een Belgische stad staat sinds 1926 een standbeeld van Leopold II. In 2020 komt er protest. De stad plaatst een bord met uitleg over de Congo-Vrijstaat naast het beeld.",
        [
            mk(
                "Waarom ligt dit standbeeld vandaag onder vuur?",
                [
                    "De persoon wordt nu anders beoordeeld",
                    "Het beeld is te klein voor het plein",
                    "Het beeld werd in 2020 gemaakt",
                    "Niemand weet wie Leopold II was",
                ],
                0,
                "Toen het geplaatst werd, eerde men de koning. Vandaag weegt het geweld in de Vrijstaat zwaarder.",
            ),
            tabel(
                "Welke uitspraken kloppen?",
                [
                    ("Het bord plaatst het beeld in zijn context.", J),
                    ("Het beeld zegt ook iets over 1926.", J),
                    ("Het debat gaat ook over hoe wij vandaag kijken.", J),
                    ("Verplaatsen naar een museum is nooit een optie.", F),
                ],
                "Uitleg erbij of het beeld naar een museum: twee mogelijke oplossingen.",
            ),
        ],
    ),
    mk(
        "Waarom vraagt elk voorwerp uit een koloniaal museum onderzoek voor het teruggegeven wordt?",
        [
            "Men moet de herkomst kennen",
            "Men moet de kleur van het voorwerp bepalen",
            "Men moet weten hoeveel bezoekers het zagen",
            "Teruggave is in België verboden",
        ],
        0,
        "België maakte een wettelijk kader. Hoe kwam het stuk hier terecht? Dat moet uitgezocht worden.",
    ),
    tabel(
        "Welke uitspraken over negationisme kloppen?",
        [
            ("Het is het ontkennen van de Holocaust.", J),
            ("Het is in België bij wet strafbaar sinds 1995.", J),
            ("Het is gewoon een mening zoals een andere.", F),
            ("Het ontkent vastgestelde feiten.", J),
        ],
        "Geen mening, maar het ontkennen van wat vastgesteld is.",
    ),
    mk(
        "Een politicus zegt: \"In onze gouden eeuw was alles beter, dus moeten we terug naar toen.\" Wat is hier aan de hand?",
        [
            "Het verleden wordt gebruikt voor een eis",
            "Een neutrale beschrijving van het verleden",
            "Historische empathie met de gouden eeuw",
            "Een primaire bron uit de gouden eeuw",
        ],
        0,
        "Politiek misbruik: het verleden vervormen of uitzoeken om een eis te onderbouwen.",
    ),
    # --- verleden, heden, toekomst
    tabel(
        "Waarom studeren we geschiedenis?",
        [
            ("Om te begrijpen hoe het heden geworden is.", J),
            ("Grenzen en instellingen van nu hebben een voorgeschiedenis.", J),
            ("Om de toekomst precies te voorspellen.", F),
        ],
        "Geschiedenis verklaart het heden, ze voorspelt de toekomst niet.",
    ),
    sorteer(
        "Breuk of continuïteit?",
        ["Breuk", "Continuïteit"],
        [
            ["de val van de Muur in 1989", "Breuk"],
            ["de communautaire breuklijn die van 1830 tot vandaag meespeelt", "Continuïteit"],
            ["de onafhankelijkheid van Congo op 30 juni 1960", "Breuk"],
            ["de uitvoer van grondstoffen uit Congo, toen en nu", "Continuïteit"],
        ],
        "Naast breuken zie je lijnen die over een lange periode doorlopen.",
    ),
    koppel(
        "Welk begrip over beeldvorming en herinnering hoort bij elke omschrijving?",
        [
            ["Een gebeurtenis vanuit verschillende standpunten bekijken", "Multiperspectiviteit"],
            ["Europa als maatstaf voor het hele verhaal nemen", "Eurocentrisme"],
            ["De waarde die een samenleving aan haar verleden geeft", "Betekenisgeving"],
            ["Het ontkennen van de Holocaust", "Negationisme"],
        ],
        ["Anachronisme", "Restauratie"],
        "Vier begrippen uit dit thema.",
    ),
    sleep(
        "Een [[stereotype]] is een vast en vereenvoudigd beeld van een groep. Komt er een waardeoordeel bij, dan is het een [[vooroordeel]]. Wie beelden maakt, [[kiest]] wat je te zien krijgt.",
        ["feit", "erfgoed"],
        "Beelden kunnen stereotypen versterken.",
    ),
    open_(
        "Leg met een voorbeeld uit waarom het beeld van een periode kan veranderen, terwijl het verleden zelf niet verandert.",
        "Het verleden ligt vast, maar historici stellen nieuwe vragen en vinden nieuwe bronnen. Over het koloniale verleden schreef men vijftig jaar geleden vooral vanuit België, over scholen en mijnen. Vandaag stelt men vragen over geweld, rechten en de Congolese kant. Het beeld verandert, de feiten niet.",
    ),
    open_(
        "Een stad twijfelt: een omstreden standbeeld laten staan met een bord, of naar een museum verplaatsen? Geef een argument voor elke oplossing.",
        "Bord: het beeld blijft zichtbaar als bron over de tijd waarin het geplaatst werd, en de uitleg plaatst het in zijn context. Museum: het beeld eert de persoon dan niet meer op een openbaar plein, maar blijft bewaard en kan er met uitleg getoond worden. Het debat gaat vooral over hoe wij vandaag naar het verleden kijken.",
    ),
]
