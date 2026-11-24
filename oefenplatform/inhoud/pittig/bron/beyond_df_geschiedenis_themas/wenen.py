"""Restauratie en revolutie: het Congres van Wenen — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="europa-1815.webp", zelf=False,
         wat="Kaart van Europa na het Congres van Wenen (1815), met letters A, B en C.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="kaartvragen over de bufferstaat en Pruisen"),
]

VRAGEN = [
    # --- beginselen
    koppel(
        "Welk beginsel van Wenen zit achter elke beslissing?",
        [
            ["De Bourbons komen in Frankrijk terug op de troon.", "Legitimiteit"],
            ["Geen enkele grootmacht mag Europa nog kunnen overheersen.", "Machtsevenwicht"],
            ["Een staat die land afgeeft, krijgt elders gebied in de plaats.", "Compensatie"],
        ],
        ["Democratie", "Nationalisme"],
        "Legitimiteit brengt de oude vorstenhuizen terug, het machtsevenwicht houdt de grootmachten in toom en compensatie zorgt voor een ruil van gebieden. Democratie en nationalisme speelden in Wenen geen rol.",
    ),
    mk(
        "Oostenrijk kreeg in Wenen Lombardije en Venetië. Welk beginsel past daar het best bij, als je weet dat Oostenrijk elders gebied verloor?",
        [
            "Compensatie",
            "Legitimiteit",
            "Volkssoevereiniteit",
            "Neutraliteit",
        ],
        0,
        "Wie elders gebied afstond, kreeg er iets voor terug. Dat is compensatie.",
    ),
    tabel(
        "Welke uitspraken over de beginselen van Wenen kloppen?",
        [
            ("Restauratie is het herstel van de toestand van voor 1789.", J),
            ("Legitimiteit betekent dat elk volk zijn eigen vorst kiest.", F),
            ("Het machtsevenwicht moest een nieuwe Napoleon onmogelijk maken.", J),
            ("Compensatie betekent dat verslagen landen een boete betalen.", F),
        ],
        "Legitimiteit gaat over de oude vorstenhuizen, niet over een keuze van het volk. Compensatie is een ruil van gebied, geen boete.",
    ),
    keuze(
        "In Wenen wilden de grootmachten de oude vorstenhuizen [[*herstellen|afschaffen|verkiezen]]. Daarom spreekt men van de [[*restauratie|revolutie|emancipatie]].",
        "Restaureren is herstellen: terug naar de orde van voor de Franse Revolutie en Napoleon.",
    ),
    # --- wie en waar
    mk(
        "Waarom kreeg het verslagen Frankrijk met Talleyrand toch een plaats aan de onderhandelingstafel?",
        [
            "Een vernederd Frankrijk kon een bron van nieuwe onrust worden",
            "Frankrijk had de oorlog tegen Napoleon zelf mee gewonnen",
            "Talleyrand was van bij het begin de voorzitter van het congres",
            "Frankrijk betaalde als enige land alle kosten van het congres",
        ],
        0,
        "De grootmachten wilden rust. Een land dat zich vernederd voelt, zoekt later wraak.",
    ),
    tabel(
        "Wie speelde welke rol in Wenen?",
        [
            ("Metternich leidde het congres.", J),
            ("Rusland en Groot-Brittannië hoorden bij de landen die de toon aangaven.", J),
            ("Napoleon Bonaparte onderhandelde mee voor Frankrijk.", F),
            ("Willem I werd koning van een nieuwe bufferstaat.", J),
        ],
        "Napoleon was verslagen. Frankrijk werd vertegenwoordigd door Talleyrand.",
    ),
    open_(
        "Leg uit waarom het verstandig was om het verslagen Frankrijk mee te laten onderhandelen in Wenen.",
        "Een land dat buitengesloten en vernederd wordt, voelt zich onrechtvaardig behandeld en kan later wraak nemen. Door Frankrijk mee aan tafel te laten, verkleinde men de kans op nieuwe onrust en hielp men het machtsevenwicht te bewaren.",
    ),
    # --- de kaart
    klik(
        "Bekijk de kaart van Europa in 1815. Klik op de nieuwe staat die Frankrijk in het noorden moest insluiten.",
        "europa-1815.webp",
        [[29.5, 33, 8, 20]],
        "Gebied A is het Verenigd Koninkrijk der Nederlanden onder Willem I: de noordelijke en zuidelijke Nederlanden samen, als buffer tegen Frankrijk.",
    ),
    sorteer(
        "Welke beslissing van Wenen hoort bij welk gebied?",
        ["Bufferstaat", "Gebied voor een grootmacht", "Nieuw verband"],
        [
            ["het Verenigd Koninkrijk der Nederlanden", "Bufferstaat"],
            ["gebieden langs de Rijn voor Pruisen", "Gebied voor een grootmacht"],
            ["Lombardije en Venetië voor Oostenrijk", "Gebied voor een grootmacht"],
            ["de Duitse Bond", "Nieuw verband"],
        ],
        "De Nederlanden werden een buffer. Pruisen en Oostenrijk kregen gebied. De Duitse Bond verving het oude Heilige Roomse Rijk.",
    ),
    mk(
        "Waarom was het Rijnland voor Pruisen op lange termijn zo waardevol?",
        [
            "Er zaten steenkool en ijzer voor de industrie",
            "Het was het enige Pruisische gebied met een grote haven aan zee",
            "Er woonden vooral Franstaligen die Pruisen trouw waren",
            "Het lag ver weg van Frankrijk en dus buiten elk gevaar",
        ],
        0,
        "Steenkool en ijzer werden de motor van de industrie. Zo werd Pruisen later economisch sterk.",
    ),
    tabel(
        "Een leerling beschrijft de Duitse Bond. Wat zegt ze terecht?",
        [
            ("De aangesloten staten bleven zelfstandig.", J),
            ("Oostenrijk had er een leidende rol in.", J),
            ("De Bond was één sterk keizerrijk met één vorst.", F),
            ("De Bond kwam in de plaats van het Heilige Roomse Rijk.", J),
        ],
        "De Duitse Bond was een los verband van zelfstandige staten, met Oostenrijk in een leidende rol. Eén Duitse staat kwam er pas veel later.",
    ),
    keuze(
        "Zwitserland werd in Wenen erkend als [[*neutrale|bufferstaat met een|koloniale]] staat. In Frankrijk kwamen [[*de Bourbons|de Bonapartes|de Oranjes]] terug op de troon.",
        "Een neutraal Zwitserland en de terugkeer van de Bourbons: allebei pasten ze in het streven naar rust en herstel.",
    ),
    mk(
        "Wat toont het Verenigd Koninkrijk der Nederlanden over de manier waarop Wenen grenzen tekende?",
        [
            "Veiligheid woog zwaarder dan de wensen van de bevolking",
            "Men vroeg aan elke inwoner bij welk land hij wilde horen en telde de stemmen",
            "Men volgde overal nauwkeurig de taalgrens tussen Noord en Zuid",
            "Men gaf elk volk in de Nederlanden een eigen republiek",
        ],
        0,
        "Noord en Zuid werden samengevoegd om Frankrijk in te sluiten. Wat de bevolking wilde, telde niet mee.",
    ),
    # --- orde bewaken
    volgorde(
        "Zet deze stappen over het Congres van Wenen in de juiste volgorde.",
        ["De nederlaag van Napoleon", "Het Congres van Wenen begint", "De Heilige Alliantie wordt gesloten", "Een bron noemt de Alliantie een verbond tegen de volkeren", "De Belgische revolutie"],
        "Napoleon verslagen, het congres in 1814, de Heilige Alliantie in 1815, de bron uit 1820 en de Belgische revolutie in 1830.",
    ),
    tabel(
        "Hoe moesten de vorsten na 1815 de orde bewaken?",
        [
            ("Rusland, Oostenrijk en Pruisen sloten de Heilige Alliantie.", J),
            ("De grootmachten kwamen regelmatig samen op congressen.", J),
            ("Ze lieten opstandelingen hun eigen grondwet schrijven.", F),
            ("Ze traden samen op tegen opstanden en revoluties.", J),
        ],
        "De Heilige Alliantie en het congressysteem moesten revoluties in de kiem smoren, niet toegeven aan de opstandelingen.",
    ),
    casus(
        "Lees de twee uitspraken over de Heilige Alliantie. Bron A, een tegenstander in 1820: \"Dit is een verbond van vorsten tegen hun eigen volkeren.\" Bron B, een verdediger: \"Dankzij dit verbond blijft Europa in vrede.\"",
        [
            mk(
                "Waarover gaan de twee bronnen?",
                [
                    "Over dezelfde feiten, met een ander belang erachter",
                    "Over twee verschillende verbonden tussen andere vorsten",
                    "Over twee verschillende eeuwen die niets met elkaar te maken hebben",
                    "Over een oorlog tussen Rusland en Pruisen",
                ],
                0,
                "Beide spreken over het optreden van de Alliantie. De ene ziet onderdrukking, de andere vrede.",
            ),
            mk(
                "Welk feit gebruikt bron A wellicht als argument?",
                [
                    "Het verbond trad op tegen opstanden voor meer vrijheid",
                    "Het verbond schafte in heel Europa alle legers af",
                    "Het verbond voerde het stemrecht in voor alle burgers",
                    "Het verbond gaf alle koloniën overzee hun vrijheid terug",
                ],
                0,
                "Wie vrijheid wilde, werd door de Alliantie tegengehouden. Daarom noemt bron A het een verbond tegen de volkeren.",
            ),
            tabel(
                "Welke besluiten kun je uit de twee bronnen samen trekken?",
                [
                    ("Je standpunt kleurt hoe je dezelfde gebeurtenis beoordeelt.", "Mag"),
                    ("Een van beide bronnen moet volledig gelogen zijn.", "Mag niet"),
                    ("Iedereen in Europa was tevreden met de Alliantie.", "Mag niet"),
                ],
                "Twee bronnen kunnen allebei een deel van de waarheid tonen. Ze verschillen omdat de schrijvers een ander belang hebben.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    # --- wat hield, wat niet
    mk(
        "In welke mate bereikte Wenen zijn doelstellingen? Kies de best onderbouwde beoordeling.",
        [
            "Deels: het evenwicht hield een tijd, de oude orde niet",
            "Volledig: na 1815 kwamen er nergens in Europa nog opstanden of revoluties",
            "Niet: meteen na het congres brak een grote oorlog uit tussen alle grootmachten",
            "Volledig: de grenzen van 1815 zijn tot vandaag ongewijzigd gebleven",
        ],
        0,
        "Het machtsevenwicht hield een tijd, het herstel van de oude orde niet. Een oordeel klinkt zelden als een volmondig ja of neen.",
    ),
    tabel(
        "Wat kun je zien als je een kaart van Europa in 1815 naast een kaart in 1914 legt?",
        [
            ("Duitsland is één staat geworden.", J),
            ("Italië is één staat geworden.", J),
            ("De Duitse Bond bestaat nog in dezelfde vorm.", F),
            ("Er is net gebeurd wat Wenen had willen verhinderen.", J),
        ],
        "De eenmaking van Duitsland en Italië zette het evenwicht van Wenen op zijn kop.",
    ),
    sorteer(
        "Wat hield stand na Wenen, en wat niet?",
        ["Hield een tijd stand", "Hield niet stand"],
        [
            ["vrede tussen de grootmachten", "Hield een tijd stand"],
            ["het machtsevenwicht", "Hield een tijd stand"],
            ["het Verenigd Koninkrijk der Nederlanden", "Hield niet stand"],
            ["de verdeling van Duitsland en Italië", "Hield niet stand"],
            ["het einde van de ideeën van de Franse Revolutie", "Hield niet stand"],
        ],
        "Er kwam tientallen jaren geen grote oorlog. Maar België scheurde zich af in 1830, Duitsland en Italië werden één en de ideeën van de Revolutie leefden voort.",
    ),
    sleep(
        "Twee stromingen werkten tegen Wenen. Het [[nationalisme]] leefde bij volken die over verschillende staten verdeeld waren. Het [[liberalisme]] leefde bij burgers die [[grondrechten]] eisten.",
        ["absolutisme", "legitimiteit"],
        "Nationalisme en liberalisme kwamen uit de ideeën van de Franse Revolutie, die na 1815 bij de burgerij en de intellectuelen voortleefden.",
    ),
    mk(
        "Bij wie leefden de ideeën van de Franse Revolutie na 1815 vooral voort?",
        [
            "Bij de burgerij en de intellectuelen",
            "Bij de vorsten van de Heilige Alliantie",
            "Bij Metternich en zijn ministers",
            "Bij de adel die zijn voorrechten terugkreeg",
        ],
        0,
        "De vorsten en de adel wilden net de oude orde terug. De burgerij en de intellectuelen droegen de nieuwe ideeën verder.",
    ),
    open_(
        "Leg uit hoe een beslissing van Wenen zelf later tot onrust leidde. Gebruik een voorbeeld.",
        "Wenen tekende grenzen zonder rekening te houden met taal, cultuur en de wensen van de bevolking. Zo werden Noord en Zuid samengevoegd in het Verenigd Koninkrijk der Nederlanden, en in 1830 scheurde België zich af. Ook volken die verdeeld waren, zoals de Duitsers en Italianen, wilden één staat: het nationalisme werkte tegen Wenen.",
    ),
    klik(
        "Bekijk opnieuw de kaart van 1815. Klik op de grootmacht die in Wenen gebieden langs de Rijn kreeg.",
        "europa-1815.webp",
        [[46, 28, 23, 24], [37.5, 41, 6, 15]],
        "Gebied B is Pruisen. Het losse stuk in het westen is het Rijnland: zo kwam Pruisen aan de grens met Frankrijk te liggen, met steenkool en ijzer voor zijn latere industrie.",
    ),
    inv(
        "Wenen bracht in Europa geen democratie. Welk politiek gevolg had het congres wel voor de vorsten?",
        ["ze kregen hun absolute macht terug", "absolute macht", "hun absolute macht", "absolute macht terug", "de absolute macht"],
        "De vorsten kregen hun absolute macht grotendeels terug. Daarom eisten liberalen later grondrechten en een grondwet.",
    ),
    # --- situeren
    tabel(
        "Hoe situeer je het Congres van Wenen?",
        [
            ("Aan het begin van de moderne tijd", J),
            ("Vooral in het politieke domein", J),
            ("Als scharnierpunt dat een tijdperk afsluit en een nieuw opent", J),
            ("Als begin van de moderne tijd voor de hele wereld", F),
        ],
        "1815 als begin van de moderne tijd is een politieke en westerse keuze. Elders betekent dat jaartal weinig.",
    ),
    mk(
        "Een Chinese historicus zegt: \"1815 is voor ons geen begin van een nieuwe tijd.\" Wat toont dat?",
        [
            "Een indeling in periodes hangt af van je standpunt",
            "Dat China het Congres van Wenen eigenlijk mee leidde",
            "Dat 1815 een verkeerd jaartal is voor het congres",
            "Dat er in 1815 nergens ter wereld iets belangrijks gebeurde",
        ],
        0,
        "Periodes indelen is een keuze. 1815 als scharnierpunt is een westerse, politieke keuze.",
    ),
    mk(
        "Het congres was vooral politiek. Welk gevolg hoort eerder bij het sociale en culturele domein?",
        [
            "Burgers bleven ideeën van vrijheid doorgeven",
            "Pruisen kreeg het Rijnland met steenkool en ijzer",
            "Zwitserland werd in Europa als neutrale staat erkend",
            "De Bourbons kwamen in Frankrijk terug op de troon",
        ],
        0,
        "Grenzen en vorsten zijn politiek. Ideeën die bij groepen in de samenleving voortleven, horen bij het sociale en culturele domein.",
    ),
    open_(
        "Was het Congres van Wenen een succes? Geef een genuanceerd oordeel met een argument voor en een argument tegen.",
        "Voor: Europa bleef tientallen jaren zonder grote oorlog tussen de grootmachten, dankzij het machtsevenwicht. Tegen: het herstel van de oude orde hield niet, want liberalisme en nationalisme groeiden, België werd in 1830 onafhankelijk en Duitsland en Italië werden later één staat. Het was dus deels een succes.",
    ),
]
