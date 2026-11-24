"""Marxisme, sociaaldemocratie, christendemocratie en migratie — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

PRENTEN = []

VRAGEN = [
    # --- drie antwoorden vergelijken
    tabel(
        "Marxisme, sociaaldemocratie of christendemocratie? Welke stroming past bij elke uitspraak?",
        [
            ("De fabrieken moeten gemeenschappelijk bezit worden, langs een revolutie.", "Marxisme"),
            ("We hervormen stap voor stap, met verkozenen in het parlement.", "Sociaaldemocratie"),
            ("Privé-bezit mag blijven, maar de werkgever heeft plichten tegenover de arbeider.", "Christendemocratie"),
            ("De geschiedenis is een opeenvolging van klassenstrijden.", "Marxisme"),
            ("Werkgevers en werknemers moeten samenwerken, niet strijden.", "Christendemocratie"),
        ],
        "Marxisten wilden een revolutie, sociaaldemocraten hervormingen. De christendemocratie aanvaardde privé-bezit, maar wees de klassenstrijd af.",
        kolommen=["Marxisme", "Sociaaldemocratie", "Christendemocratie"],
    ),
    tabel(
        "Waarover waren de stromingen het eens of oneens?",
        [
            ("Marxisme en sociaaldemocratie waren het eens over het doel.", J),
            ("Marxisme en sociaaldemocratie waren het eens over de weg.", F),
            ("Christendemocratie en marxisme wilden allebei het privé-bezit afschaffen.", F),
            ("Alle drie wilden iets doen aan de armoede van de arbeiders.", J),
        ],
        "Alle drie zijn antwoorden op de sociale kwestie. Marxisme en sociaaldemocratie verschilden over de weg, de christendemocratie hield het privé-bezit.",
    ),
    # --- marxisme
    casus(
        "Een arbeider maakt op een dag tien stoelen. De fabrikant verkoopt ze samen voor 50 frank. Het hout en de machines kosten 20 frank. Het dagloon van de arbeider is 5 frank.",
        [
            inv(
                "Hoe noemt Marx de 25 frank die overblijft en die de eigenaar in zijn zak houdt?",
                ["de meerwaarde", "meerwaarde"],
                "De meerwaarde is het verschil tussen wat de arbeid opbrengt en wat het loon kost.",
            ),
            mk(
                "Wat zag Marx in die meerwaarde?",
                [
                    "Uitbuiting van de arbeider",
                    "Een eerlijke beloning voor de arbeider, die er zelf voor koos",
                    "Een belasting die de staat moest innen voor de armen",
                    "Een bewijs dat de fabrikant te weinig winst maakte",
                ],
                0,
                "De arbeider maakt de waarde, maar de eigenaar houdt het verschil. Daarom wilde Marx de productiemiddelen in gemeenschappelijk bezit.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen in de geschiedenis zoals Marx ze voorzag in de juiste volgorde.",
        ["Klassenstrijd tussen burgerij en arbeiders", "Revolutie van de arbeiders", "Dictatuur van het proletariaat", "Samenleving zonder klassen"],
        "Na de revolutie kwam volgens Marx een tussenfase, de dictatuur van het proletariaat, en daarna de klasseloze samenleving.",
    ),
    mk(
        "Waarom werden er internationales opgericht?",
        [
            "Arbeiders van elk land hadden hetzelfde belang",
            "De vorsten wilden samen de arbeiders beter beschermen",
            "De paus wilde alle katholieke vakbonden samenbrengen",
            "Fabrikanten wilden samen de lonen in Europa verhogen",
        ],
        0,
        "Voor Marx liep de strijd niet tussen landen maar tussen klassen. Daarom moesten arbeiders zich over de grenzen verenigen.",
    ),
    keuze(
        "Marx verwachtte dat het [[*kapitalisme|socialisme|feodalisme]] aan zijn eigen tegenstellingen ten onder zou gaan. Het marxisme situeer je in het economische en het [[*politieke|religieuze|artistieke]] domein.",
        "Het gaat over wie de fabrieken bezit (economisch) en wie de macht in de staat heeft (politiek).",
    ),
    tabel(
        "Een leerling vat het Communistisch Manifest samen. Wat schrijft hij terecht?",
        [
            ("Het verscheen in 1848.", J),
            ("Marx schreef het samen met Engels.", J),
            ("Het verdedigt dat fabrieken privébezit van hun eigenaar blijven.", F),
            ("Het ziet een revolutie van de arbeiders als onvermijdelijk.", J),
        ],
        "Dat fabrieken privébezit blijven, is net de liberale stelling.",
    ),
    # --- sociaaldemocratie
    mk(
        "Rond 1900 splitsten de socialisten zich. Wat werd er later van wie bij de revolutie bleef?",
        [
            "Communist",
            "Christendemocraat",
            "Liberaal van de grote burgerij",
            "Sociaaldemocraat in het parlement",
        ],
        0,
        "Wie voor hervormingen koos, werd sociaaldemocraat. Wie bij de revolutie bleef, werd later communist.",
    ),
    koppel(
        "Welk begrip over de sociale stromingen hoort bij elke omschrijving?",
        [
            ["Stap voor stap hervormen in plaats van een revolutie", "Reformisme"],
            ["Pensioen, kinderbijslag en ziekteverzekering voor iedereen", "Welvaartsstaat"],
            ["Het verschil tussen opbrengst van de arbeid en het loon", "Meerwaarde"],
            ["Een netwerk van verenigingen van één strekking", "Zuil"],
        ],
        ["Kartel", "Coalitieverbod"],
        "Reformisme en welvaartsstaat horen bij de sociaaldemocratie, meerwaarde bij Marx, zuil bij de verzuiling.",
    ),
    mk(
        "Waarom had de sociaaldemocratie het algemeen stemrecht absoluut nodig, terwijl het marxisme dat minder nodig had?",
        [
            "Ze wilde via het parlement hervormen",
            "Ze wilde dat alleen de rijken mochten stemmen in het parlement",
            "Ze wilde het parlement zo snel mogelijk afschaffen",
            "Ze wilde dat de paus de verkiezingen zou leiden",
        ],
        0,
        "Wie via wetten wil veranderen, heeft verkozenen nodig, en dus stemmen van de arbeiders.",
    ),
    casus(
        "Lees de twee bronnen. Bron A, 1870: \"Arbeiders, grijp de fabrieken! De staat van de burgerij moet vallen.\" Bron B, 1900: \"Wij eisen het algemeen stemrecht, een wet op de werkdag en een ziekenkas voor elke arbeider.\"",
        [
            koppel(
                "Welke stroming hoort bij welke bron?",
                [["Bron A", "Marxisme"], ["Bron B", "Sociaaldemocratie"]],
                ["Christendemocratie", "Liberalisme"],
                "A wil een omwenteling, B hervormingen langs wetten.",
            ),
            tabel(
                "Wat hebben de twee bronnen gemeen?",
                [
                    ("Ze willen het lot van de arbeiders verbeteren.", J),
                    ("Ze kiezen dezelfde weg.", F),
                    ("Ze verdedigen het economisch liberalisme.", F),
                ],
                "Hetzelfde doel, een andere weg. Geen van beide wil een staat die de economie aan zichzelf overlaat.",
            ),
        ],
    ),
    # --- christendemocratie
    tabel(
        "Wat staat er in Rerum Novarum van 1891?",
        [
            ("De arbeider heeft recht op een rechtvaardig loon.", J),
            ("Arbeiders mogen zich in eigen verenigingen organiseren.", J),
            ("Het privé-bezit moet worden afgeschaft.", F),
            ("Werkgever en werknemer hebben plichten tegenover elkaar.", J),
            ("De klassenstrijd is de motor van de geschiedenis.", F),
        ],
        "Rerum Novarum zoekt een middenweg: bescherming van de arbeider, maar met privé-bezit en zonder klassenstrijd.",
    ),
    sorteer(
        "Wat wijst de christendemocratie af bij welke stroming?",
        ["Afgewezen bij het economisch liberalisme", "Afgewezen bij het marxisme"],
        [
            ["de markt bepaalt alleen de lonen", "Afgewezen bij het economisch liberalisme"],
            ["de staat bemoeit zich niet met de werktijden", "Afgewezen bij het economisch liberalisme"],
            ["de klassenstrijd", "Afgewezen bij het marxisme"],
            ["de afschaffing van het privé-bezit", "Afgewezen bij het marxisme"],
        ],
        "Een loon moest een gezin kunnen onderhouden. Maar klassen zijn geen vijanden, en privé-bezit blijft.",
    ),
    mk(
        "Een christelijke arbeider zegt in 1900: \"Mijn patroon en ik zijn geen vijanden.\" Welke stroming spreekt hier?",
        [
            "De christendemocratie",
            "Het marxisme van het Communistisch Manifest",
            "Het economisch liberalisme van de nachtwachtstaat",
            "Het communisme van wie bij de revolutie bleef",
        ],
        0,
        "Klassen zijn voor de christendemocratie groepen die moeten samenwerken.",
    ),
    mk(
        "Hoe ontstond in België de verzuiling?",
        [
            "Elke strekking bouwde eigen vakbonden en ziekenkassen",
            "De grondwet verplichtte elke burger om lid te worden van één partij",
            "De staat bouwde zelf alle scholen en vakbonden in het land",
            "De vakbonden werden in 1866 allemaal samengevoegd tot één bond",
        ],
        0,
        "Naast de socialistische zuil groeide een christelijke, met eigen vakbonden, ziekenkassen, scholen en verenigingen.",
    ),
    # --- migratie
    sorteer(
        "Duwfactor of trekfactor?",
        ["Duwfactor", "Trekfactor"],
        [
            ["honger na een mislukte oogst", "Duwfactor"],
            ["werk in de Amerikaanse fabrieken", "Trekfactor"],
            ["werkloosheid in de eigen streek", "Duwfactor"],
            ["goedkope grond om te boeren", "Trekfactor"],
            ["oorlog in het eigen land", "Duwfactor"],
            ["veiligheid elders", "Trekfactor"],
        ],
        "Duwfactoren duwen iemand weg, trekfactoren lokken hem naar elders.",
    ),
    volgorde(
        "Zet de stappen in de arbeidsmigratie naar België in de juiste volgorde.",
        ["Akkoord met Italië", "Mijnramp in Marcinelle", "Akkoorden met Marokko en Turkije", "Migratiestop"],
        "1946, 1956, 1964 en 1974.",
    ),
    casus(
        "Giovanni komt in 1947 uit een arm dorp in Zuid-Italië naar de mijnen van Henegouwen. In 1975 laat hij zijn vrouw en kinderen overkomen.",
        [
            tabel(
                "Welke factoren speelden bij Giovanni?",
                [
                    ("Armoede in zijn dorp: een duwfactor", J),
                    ("Werk in de Belgische mijnen: een trekfactor", J),
                    ("Een akkoord tussen België en Italië", J),
                    ("De migratiestop verbood hem zijn gezin te laten komen", F),
                ],
                "Gezinshereniging bleef na 1974 mogelijk. De migratiestop gold voor de aanwerving van nieuwe arbeiders.",
            ),
            mk(
                "Waarom haalde België na 1945 arbeiders zoals Giovanni?",
                [
                    "Voor de mijnen en de heropbouw waren te weinig arbeiders",
                    "België had na de oorlog te veel werklozen in de mijnen",
                    "Italië betaalde België om zijn arbeiders op te nemen",
                    "De mijnen in België waren allemaal gesloten",
                ],
                0,
                "Er bleef werk liggen in de mijnen, de bouw en de staalnijverheid.",
            ),
        ],
    ),
    tabel(
        "Welke uitspraken over migratie in de negentiende eeuw kloppen?",
        [
            ("Miljoenen Europeanen trokken naar Amerika.", J),
            ("Ook Belgen uit arme Vlaamse streken vertrokken als landverhuizer.", J),
            ("Mensen trokken van het platteland naar de industriesteden.", J),
            ("Alle migratie ging van Amerika naar Europa.", F),
        ],
        "Armoede dreef mensen weg, werk en grond lokten hen. Ook binnen het land trokken mensen naar de steden.",
    ),
    mk(
        "Een krant schrijft in 1975: \"Sinds vorig jaar is de migratie naar België voorbij.\" Wat is de beste reactie?",
        [
            "Niet juist: gezinshereniging en studie bleven mogelijk",
            "Juist: sinds 1974 kwam er geen enkele migrant meer binnen",
            "Juist: de akkoorden met Italië en Marokko werden verboden",
            "Niet juist: er kwamen net meer mijnwerkers dan ooit",
        ],
        0,
        "De migratiestop gold voor nieuwe arbeiders. De migratie stopte niet, ze veranderde van vorm.",
    ),
    sleep(
        "In [[1956]] kostte een brand in de steenkoolmijn van [[Marcinelle]] 262 mensen het leven, veel van hen [[Italiaanse]] mijnwerkers.",
        ["1974", "Seraing", "Turkse"],
        "De ramp van Marcinelle toont hoe gevaarlijk het werk was waarvoor gastarbeiders kwamen.",
    ),
    open_(
        "Vergelijk hoe het marxisme en de christendemocratie de sociale kwestie wilden oplossen. Geef een gelijkenis en twee verschillen.",
        "Gelijkenis: allebei wilden ze het lot van de arbeiders verbeteren en wezen ze het economisch liberalisme af. Verschillen: het marxisme wilde het privé-bezit van de productiemiddelen afschaffen, de christendemocratie hield het privé-bezit. Het marxisme zag de klassenstrijd en een revolutie als weg, de christendemocratie wilde dat werkgevers en werknemers samenwerkten.",
    ),
    open_(
        "Leg uit waarom de sociaaldemocratie na 1945 vooral de sociale zekerheid centraal zette.",
        "De sociaaldemocratie wilde de samenleving stap voor stap hervormen langs wetten. Met het algemeen stemrecht kon ze dat via het parlement doen. Een stelsel van sociale zekerheid voor iedereen, met pensioen, kinderbijslag, ziekteverzekering en werkloosheidsuitkering, beschermde de arbeiders tegen de armoede die vroeger bij ziekte of ongeval dreigde.",
    ),
    keuze(
        "De akkoorden over arbeidsmigratie met Marokko en Turkije dateren van [[*1964|1946|1974]]. De gastarbeiders werkten vooral in de mijnen, de bouw en de [[*staalnijverheid|landbouw|banksector]].",
        "Eerst kwamen Italianen, later Spanjaarden en Grieken, en in 1964 Marokkanen en Turken.",
    ),
    mk(
        "Welke migratie hoort het nauwst bij de industrialisering zelf?",
        [
            "De trek naar de industriesteden",
            "De komst van Turkse arbeiders in 1964 naar de Belgische mijnen",
            "De gezinshereniging na de migratiestop van 1974",
            "De reis van Marx en Engels naar Londen",
        ],
        0,
        "De fabrieken trokken mensen van het platteland naar de stad: verstedelijking.",
    ),
    tabel(
        "Welke uitspraken over Marx' ideeën over de staat kloppen?",
        [
            ("De staat was voor Marx in handen van de burgerij.", J),
            ("Na de revolutie voorzag hij een dictatuur van het proletariaat.", J),
            ("Hij wilde dat de staat de economie aan zichzelf overliet.", F),
        ],
        "Marx zag de staat als instrument van de bezittende klasse. Laissez-faire was net de liberale houding.",
    ),
    mk(
        "Een fabrikant zegt in 1880: \"Mijn fabriek is van mij, en de markt bepaalt het loon.\" Welke stroming verwerpt beide delen van die uitspraak?",
        [
            "Het marxisme",
            "Het economisch liberalisme van de burgerij",
            "De christendemocratie van Rerum Novarum",
            "Het nationalisme van de romantiek",
        ],
        0,
        "Het marxisme wil gemeenschappelijk bezit én geen loon dat de markt bepaalt. De christendemocratie aanvaardt het privé-bezit wel, en verwerpt enkel het tweede deel.",
    ),
]
