"""De eerste en de tweede industriële revolutie — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="kinderarbeid-mijn.webp", zelf=False,
         wat="Britse gravure (1854): kinderen in een steenkoolmijn.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="casus over kinderarbeid"),
]

VRAGEN = [
    # --- eerste industriële revolutie
    sorteer(
        "Hoort het kenmerk bij de eerste of bij de tweede industriële revolutie?",
        ["Eerste", "Tweede"],
        [
            ["de stoommachine van James Watt", "Eerste"],
            ["de mechanisering van de textiel", "Eerste"],
            ["elektriciteit en aardolie", "Tweede"],
            ["laboratoria in het bedrijf", "Tweede"],
            ["de spoorlijn Brussel-Mechelen", "Eerste"],
            ["kunstmest en verfstoffen", "Tweede"],
        ],
        "De eerste golf draaide op steenkool, stoom en textiel. Vanaf ongeveer 1870 kwamen elektriciteit, aardolie, chemie en het labo.",
    ),
    tabel(
        "Welke voorwaarden verklaren waarom de industriële revolutie in Engeland begon?",
        [
            ("Steenkool en ijzererts lagen dicht bij elkaar.", J),
            ("Er was kapitaal uit de handel en de kolonies.", J),
            ("De bevolking groeide en leverde werkvolk en kopers.", J),
            ("Engeland had de grootste oppervlakte van Europa.", F),
        ],
        "Grondstoffen, kapitaal en mensen. Over de oppervlakte van het land zegt de leerstof niets, en Engeland was ook niet het grootste land.",
    ),
    mk(
        "Waarom was de stoommachine zo belangrijk voor de plaats waar een fabriek kon staan?",
        [
            "Een fabriek hoefde niet meer aan een rivier te staan",
            "Een fabriek moest voortaan altijd naast een haven aan zee staan",
            "Een fabriek kon voortaan enkel nog in een grote hoofdstad staan",
            "Een fabriek mocht voortaan niet meer bij een steenkoolmijn staan",
        ],
        0,
        "Watt's stoommachine zette warmte om in beweging. Waterkracht was niet meer nodig.",
    ),
    mk(
        "Een leerling zegt: \"Door de industriële revolutie verdween de landbouw.\" Wat is de beste reactie?",
        [
            "Nee, de landbouw werd net een voorwaarde",
            "Ja, alle boeren werkten na 1800 in een fabriek in de stad",
            "Ja, want er was in Engeland geen vruchtbare grond meer over",
            "Nee, want de fabrieken stonden allemaal op het platteland",
        ],
        0,
        "Meer opbrengst per akker voedde de groeiende steden en maakte handen vrij voor de fabriek. De landbouw verdween niet.",
    ),
    casus(
        "Een fabrieksreglement uit Gent, rond 1840: \"Het werk begint om vijf uur 's morgens bij het luiden van de bel. Wie vijf minuten te laat komt, verliest een kwart van zijn dagloon. Praten tijdens het werk is verboden.\"",
        [
            mk(
                "Wat was voor een arbeider die van het platteland kwam het meest nieuw?",
                [
                    "De klok bepaalde het ritme",
                    "Hij moest voor het eerst met zijn handen werken",
                    "Hij werkte voor het eerst samen met dieren",
                    "Hij mocht voor het eerst zelf zijn werkuren kiezen",
                ],
                0,
                "Op het land bepaalden daglicht en seizoen het werk. In de fabriek bepaalde de bel wanneer je begon en stopte.",
            ),
            tabel(
                "Wat kun je uit dit reglement besluiten?",
                [
                    ("De fabrikant legde strenge regels op.", "Mag"),
                    ("Arbeiders konden boetes krijgen.", "Mag"),
                    ("Alle fabrieken in Europa hadden precies dit reglement.", "Mag niet"),
                    ("De arbeiders waren tevreden met deze regels.", "Mag niet"),
                ],
                "Eén reglement toont hoe het in die fabriek was. Over alle fabrieken of over wat de arbeiders dachten, zegt het niets.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    # --- België
    tabel(
        "Welke uitspraken over de industrialisering van België kloppen?",
        [
            ("België was het eerste land op het vasteland dat industrialiseerde.", J),
            ("Wallonië was de streek van steenkool en staal.", J),
            ("De Kempense mijnen openden al rond 1800.", F),
            ("Vlaanderen kende rond 1845 nog grote armoede in de linnennijverheid.", J),
        ],
        "Wallonië en Gent liepen voorop. De Kempense mijnen openden pas na 1900, en Vlaanderen industrialiseerde later.",
    ),
    koppel(
        "Welke persoon of plaats hoort bij elke omschrijving?",
        [
            ["Smokkelde een Engelse spinmachine in stukken naar Gent", "Lieven Bauwens"],
            ["Bouwde in Seraing machines en locomotieven", "John Cockerill"],
            ["Verbeterde de stoommachine", "James Watt"],
            ["Textielstad met spinnerijen en weverijen", "Gent"],
        ],
        ["Metternich", "Borinage"],
        "Bauwens en Cockerill brachten Engelse kennis naar België. Watt verbeterde de stoommachine. De Borinage was een steenkoolbekken, geen textielstad.",
    ),
    mk(
        "Waarom moest Lieven Bauwens de spinmachine in stukken binnensmokkelen?",
        [
            "Engeland verbood de uitvoer ervan",
            "De machine was te groot voor de Belgische wegen en bruggen van toen",
            "Willem I had elke machine uit het buitenland verboden in Gent",
            "De Gentse arbeiders wilden geen machines en vernielden ze",
        ],
        0,
        "Engeland wilde zijn voorsprong houden en verbood de uitvoer van machines. Toch haalde België Engelse machines en vaklui binnen.",
    ),
    mk(
        "Waarom legde de jonge Belgische staat zelf een spoornet aan?",
        [
            "Om niet afhankelijk te zijn van de Nederlandse waterwegen",
            "Omdat de grondwet van 1831 verbood dat bedrijven spoorlijnen aanlegden",
            "Omdat Willem I het spoornet in 1839 als geschenk aanbood",
            "Omdat er in België geen enkele rivier of kanaal bestond",
        ],
        0,
        "Na 1830 lag Nederland dwars. Een eigen spoornet hield de handel open, met de lijn Brussel-Mechelen van 1835 als begin.",
    ),
    keuze(
        "De eerste industriegebieden in België lagen bij de [[*steenkoolbekkens|wijngaarden|bergen]] van Luik, Henegouwen en de Borinage, en in [[*Gent|Brugge|Ieper]] met zijn spinnerijen.",
        "Kolen trokken de zware industrie aan, en Gent had een haven en een traditie in textiel.",
    ),
    open_(
        "Leg uit waarom de eerste Belgische fabrieken vaak bij een steenkoolbekken of een waterloop stonden.",
        "Brandstof vervoeren was duur. Bij een steenkoolbekken had je de kolen voor de stoommachine dichtbij, en een waterloop leverde kracht en vervoer. Pas met de spoorweg werd vervoer snel en goedkoop.",
    ),
    # --- tweede industriële revolutie
    tabel(
        "Wat was nieuw in de tweede industriële revolutie?",
        [
            ("Een voertuig dat zijn eigen brandstof meeneemt", J),
            ("Lampen, dynamo's en motoren", J),
            ("Steenkool als eerste energiebron van de fabriek", F),
            ("Bedrijven met een eigen laboratorium", J),
        ],
        "De verbrandingsmotor, de elektrotechniek en het labo zijn nieuw. Steenkool dreef al de eerste golf aan.",
    ),
    mk(
        "Waarom werden de bedrijven tijdens de tweede industriële revolutie zo groot?",
        [
            "Machines en labo's kostten heel veel kapitaal",
            "De overheid verplichtte elk bedrijf om minstens duizend arbeiders te hebben",
            "Kleine bedrijven werden door de grondwet van 1831 verboden",
            "Arbeiders wilden alleen nog in heel grote fabrieken werken",
        ],
        0,
        "Wie veel kapitaal nodig heeft, bundelt geld in een naamloze vennootschap, met banken ernaast.",
    ),
    casus(
        "Drie staalbedrijven spreken in 1900 af: \"Niemand van ons verkoopt zijn staal onder de prijs van 120 frank per ton. Bedrijf A levert enkel in het noorden, B in het zuiden en C in het buitenland.\"",
        [
            inv(
                "Hoe noem je zo'n afspraak tussen bedrijven?",
                ["een kartel", "kartel"],
                "Een kartel is een afspraak tussen bedrijven over prijzen of markten.",
            ),
            tabel(
                "Wat zijn de gevolgen van deze afspraak?",
                [
                    ("De bedrijven beconcurreren elkaar niet meer.", J),
                    ("De klant kan nergens goedkoper staal vinden.", J),
                    ("De prijs van staal daalt sterk.", F),
                ],
                "Een kartel schakelt de concurrentie uit. Voor de klant blijven de prijzen hoog.",
            ),
        ],
    ),
    sleep(
        "Een onderneming waarvan het kapitaal in [[aandelen]] verdeeld is, heet een [[naamloze vennootschap]]. Zo konden veel mensen samen het [[kapitaal]] voor grote fabrieken bijeenbrengen.",
        ["kartel", "loon", "vakbond"],
        "Door het kapitaal te verdelen in aandelen konden bedrijven veel geld verzamelen.",
    ),
    volgorde(
        "Zet deze gebeurtenissen over de industriële revolutie in chronologische volgorde.",
        ["De eerste industriële revolutie begint in Engeland", "Bauwens brengt een spinmachine naar Gent", "De spoorlijn Brussel-Mechelen opent", "De tweede industriële revolutie begint", "De eerste Belgische wet op kinderarbeid"],
        "Tweede helft 18de eeuw, rond 1800, 1835, rond 1870 en 1889.",
    ),
    # --- gevolgen
    casus(
        "Bekijk de Britse gravure uit 1854. Ze toont kinderen in een steenkoolmijn: het ene duwt een kolenwagen, het andere bedient een luchtdeur.",
        [
            met_prent("kinderarbeid-mijn.webp", mk(
                "Waarom zetten mijnbazen graag kinderen aan het werk?",
                ["Ze waren goedkoop en pasten in kleine ruimtes", "Ze waren sterker dan volwassen mijnwerkers", "De wet verplichtte mijnen om kinderen aan te nemen", "Ze kregen een hoger loon dan hun ouders"],
                0,
                "Kinderen kostten weinig en konden door smalle mijngangen.",
            )),
            tabel(
                "Welke uitspraken over kinderarbeid in België kloppen?",
                [
                    ("In 1850 beperkte geen enkele wet de kinderarbeid.", J),
                    ("De eerste wet op kinderarbeid kwam er in 1889.", J),
                    ("De grondwet van 1831 verbood kinderarbeid.", F),
                ],
                "Pas in 1889 kwam een eerste wet. Tot dan had de staat zich er niet mee bemoeid.",
            ),
        ],
    ),
    mk(
        "Wat betekent de demografische transitie?",
        [
            "De sterfte daalt eerst, de geboorten pas later",
            "De geboorten dalen eerst, de sterfte pas veel later in de eeuw",
            "Sterfte en geboorten stijgen tegelijk in de hele negentiende eeuw",
            "De mensen trekken massaal van de stad terug naar het platteland",
        ],
        0,
        "Tussen de twee dalingen in groeit de bevolking snel.",
    ),
    tabel(
        "Een arbeidersgezin woont in 1870 in een Gents beluik. Wat is waarschijnlijk?",
        [
            ("Het huisje ligt rond een gesloten koer met weinig licht.", J),
            ("Veel gezinnen delen één pomp en één toilet.", J),
            ("Ziektes als tyfus en cholera verspreiden zich snel.", J),
            ("Het gezin heeft recht op betaalde vakantie.", F),
        ],
        "Beluiken waren klein, donker en ongezond. Vakantie en minimumloon kwamen pas in de twintigste eeuw.",
    ),
    mk(
        "Je ziet een grafiek van het aantal inwoners van Luik tussen 1800 en 1900. Hoe verklaar je de sterke stijging?",
        [
            "De fabrieken trokken mensen van het platteland",
            "Er werden in Luik geen kinderen meer geboren na 1800",
            "De stad werd in 1815 bij Frankrijk gevoegd",
            "Alle boeren uit Engeland verhuisden naar Luik",
        ],
        0,
        "Verstedelijking: werk in de fabriek lokte mensen naar de stad.",
    ),
    sorteer(
        "In welk domein situeer je elk gevolg van de industrialisering?",
        ["Economisch", "Sociaal", "Politiek"],
        [
            ["de wereldhandel groeit door stoomschepen", "Economisch"],
            ["arbeiders wonen in beluiken", "Sociaal"],
            ["de eerste wet op kinderarbeid", "Politiek"],
            ["grote naamloze vennootschappen", "Economisch"],
            ["werkdagen van twaalf uur", "Sociaal"],
        ],
        "Fabriek en handel zijn economisch, wonen en werken sociaal, en via de sociale wetten komt ook het politieke domein in beeld.",
    ),
    tabel(
        "Welke voorzieningen bestonden rond 1880 voor een fabrieksarbeider?",
        [
            ("Een vergoeding na een arbeidsongeval", F),
            ("Een wettelijk minimumloon", F),
            ("Betaalde vakantie", F),
            ("Een werkdag van twaalf uur of langer", J),
        ],
        "De arbeider stond er alleen voor. Vakantie en minimumloon zijn verworvenheden van de twintigste eeuw.",
    ),
    open_(
        "Leg uit hoe de spoorweg de industrie veranderde. Geef twee gevolgen.",
        "Grondstoffen zoals steenkool en goederen konden snel en goedkoop vervoerd worden. Daardoor kon een fabriek werken voor een markt ver buiten haar eigen streek, en hoefde ze minder dicht bij de kolen te staan. Samen met de stoomschepen maakte de spoorweg ook de wereldhandel veel groter.",
    ),
    mk(
        "Wat verbindt de tweede industriële revolutie met de wetenschap?",
        [
            "Bedrijven deden eigen onderzoek in labo's",
            "Wetenschappers werden verboden in fabrieken te werken",
            "De wetenschap verdween volledig uit de universiteiten",
            "Alle uitvindingen kwamen nog van ambachtslui thuis",
        ],
        0,
        "De wetenschap kwam de fabriek binnen. Chemie en elektrotechniek steunden op onderzoek.",
    ),
    keuze(
        "De tweede industriële revolutie situeer je vanaf ongeveer [[*1870|1750|1945]] tot [[*de Eerste Wereldoorlog|de Franse Revolutie|de val van de Berlijnse Muur]].",
        "Vanaf ongeveer 1870 tot 1914 kwamen elektriciteit, aardolie, chemie en elektrotechniek op.",
    ),
    mk(
        "Hoe kon België zo snel industrialiseren, terwijl de uitvindingen uit Engeland kwamen?",
        [
            "Het haalde Engelse machines en vaklui binnen",
            "Het vond zelf alle machines uit, nog voor Engeland dat deed",
            "Het kreeg alle fabrieken cadeau van het Congres van Wenen",
            "Het verbood de invoer van alle Engelse kennis en machines",
        ],
        0,
        "Bauwens smokkelde een spinmachine, Cockerill bracht Engelse kennis naar Seraing. Daarbij had België zelf steenkool en ijzer.",
    ),
    tabel(
        "Een leerling vergelijkt de werkplaats van vroeger met de fabriek. Wat zegt hij terecht?",
        [
            ("Vroeger werkte men thuis of in kleine werkplaatsen.", J),
            ("In de fabriek bepaalde de arbeider zelf wanneer hij stopte.", F),
            ("In de fabriek stonden de machines op één plaats samen.", J),
            ("Ook de werkplaats van vroeger had een stoommachine van Watt.", F),
        ],
        "Thuiswerk en kleine werkplaatsen maakten plaats voor de fabriek, waar machine en klok het ritme bepaalden.",
    ),
]
