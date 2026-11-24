"""De dekolonisatie van Congo — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvragen op 1960 en 1997"),
]

VRAGEN = [
    # --- dekolonisatie algemeen
    tabel(
        "Welke oorzaken van de dekolonisatie na 1945 kloppen?",
        [
            ("De Europese mogendheden waren door de oorlog verzwakt.", J),
            ("In de kolonies groeiden bewegingen die zelfbestuur eisten.", J),
            ("Soldaten uit de kolonies hadden in Europa meegevochten.", J),
            ("Het handvest van de VN sprak van het zelfbeschikkingsrecht van volken.", J),
            ("De kolonies brachten na 1945 niets meer op.", F),
        ],
        "Verzwakking, prestigeverlies, eigen bewegingen en het zelfbeschikkingsrecht speelden mee.",
    ),
    volgorde(
        "Zet in chronologische volgorde.",
        ["India wordt onafhankelijk", "Indonesië wordt onafhankelijk", "Het Afrikaanse jaar", "Mobutu neemt de macht", "Het land heet Zaïre", "Mobutu wordt afgezet"],
        "1947, 1949, 1960, 1965, 1971 en 1997.",
    ),
    tabel(
        "Een leerling zegt: \"De dekolonisatie verliep overal vreedzaam.\" Welke gegevens spreken dat tegen?",
        [
            ("In Algerije ging er een lange oorlog aan vooraf.", J),
            ("In Indochina ging er een lange oorlog aan vooraf.", J),
            ("In Kenia was er een gewapend conflict.", J),
            ("India werd in 1947 onafhankelijk.", F),
        ],
        "Dat India onafhankelijk werd, zegt op zich niets over geweld. Algerije, Indochina en Kenia tonen dat het niet overal vreedzaam ging.",
    ),
    # --- weg naar 1960
    casus(
        "In 1955 stelt een Belgische hoogleraar een plan voor: Congo zou over dertig jaar onafhankelijk kunnen worden. In januari 1959 breken in Leopoldstad zware rellen uit. Op 30 juni 1960 is Congo onafhankelijk.",
        [
            mk(
                "Wat valt op als je het plan van 1955 vergelijkt met wat er gebeurde?",
                [
                    "Het ging veel sneller dan gepland",
                    "Het ging precies volgens het plan van dertig jaar",
                    "Congo werd pas in 1985 onafhankelijk",
                    "Het plan werd door Lumumba geschreven",
                ],
                0,
                "Tussen de rellen en de onafhankelijkheid lag maar anderhalf jaar. Jarenlang voorbereid was het niet.",
            ),
            tabel(
                "Wat zegt het plan van 1955 over het denken in België?",
                [
                    ("Men dacht dat de onafhankelijkheid nog ver weg was.", J),
                    ("Zelfs dertig jaar lag toen al gevoelig.", J),
                    ("België wilde Congo zo snel mogelijk vrijlaten.", F),
                ],
                "Snel onafhankelijk maken was niet het plan.",
            ),
        ],
    ),
    koppel(
        "Welke persoon hoort bij elke omschrijving?",
        [
            ["Eerste premier, sprak op 30 juni over het koloniale onrecht", "Patrice Lumumba"],
            ["Staatshoofd, met zijn beweging in Leopoldstad", "Joseph Kasavubu"],
            ["Nam in 1965 met een staatsgreep de macht", "Mobutu Sese Seko"],
            ["Sprak in 2020 in een brief zijn diepste spijt uit", "Koning Filip"],
        ],
        ["Leopold II", "Stanley"],
        "Vier figuren van 1960 tot vandaag. Leopold II en Stanley horen bij de Vrijstaat.",
    ),
    mk(
        "Uit welke groep kwamen de eerste eisen voor zelfbestuur?",
        [
            "De évolués, Congolezen met een opleiding",
            "De Belgische ambtenaren in Leopoldstad",
            "De missionarissen van de grote kerken",
            "De directie van de Union Minière",
        ],
        0,
        "Het manifest van Conscience africaine uit 1956 is een voorbeeld.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Congo onafhankelijk werd.",
        "tijdlijn-1750-2030.svg",
        [[67.4, 25, 6.2, 55]],
        "30 juni 1960, in het Afrikaanse jaar.",
    ),
    tabel(
        "Waarom heet 1960 het Afrikaanse jaar?",
        [
            ("Zeventien Afrikaanse landen werden dat jaar onafhankelijk.", J),
            ("Congo was een van die landen.", J),
            ("In dat jaar werd heel Afrika in één keer onafhankelijk.", F),
        ],
        "Een hele reeks staten, niet heel het werelddeel.",
    ),
    mk(
        "Waarom stond Congo er in 1960 zwak voor om zichzelf te besturen?",
        [
            "Er waren amper Congolezen met een universitair diploma",
            "Er waren in Congo helemaal geen scholen",
            "Er waren geen grondstoffen meer in de mijnen",
            "Alle Congolezen spraken enkel Nederlands",
        ],
        0,
        "Lager onderwijs was er ruim, hoger onderwijs amper. De eerste universiteiten kwamen pas in de jaren vijftig.",
    ),
    casus(
        "Op 30 juni 1960 spreken koning Boudewijn en de Congolese leiders. Lumumba neemt onverwacht het woord en spreekt over de vernederingen, de slagen en het onrecht van de koloniale tijd.",
        [
            mk(
                "Waarom maakte deze toespraak zoveel indruk?",
                [
                    "Ze stond niet in het programma",
                    "Lumumba sprak de koning helemaal niet tegen",
                    "Het was de eerste toespraak ooit in Congo",
                    "Hij las een brief van Leopold II voor",
                ],
                0,
                "Op een feestelijke plechtigheid sprak een Congolese leider openlijk over het onrecht.",
            ),
            tabel(
                "Wat kun je uit deze gebeurtenis besluiten?",
                [
                    ("De Belgische en de Congolese kijk op de koloniale tijd verschilden.", "Mag"),
                    ("Alle Congolezen dachten precies hetzelfde als Lumumba.", "Mag niet"),
                    ("De verhouding tussen België en de nieuwe staat begon gespannen.", "Mag"),
                ],
                "Eén toespraak toont een standpunt, niet wat iedereen dacht.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    # --- Congocrisis
    tabel(
        "Wat gebeurde er kort na de onafhankelijkheid?",
        [
            ("In juli 1960 kwam het leger in opstand.", J),
            ("Katanga scheidde zich af.", J),
            ("De VN stuurden troepen.", J),
            ("Congo werd een rustig en stabiel land.", F),
        ],
        "De Congocrisis brak meteen uit.",
    ),
    mk(
        "Waarom woog de afscheiding van Katanga zo zwaar?",
        [
            "Daar lagen de mijnen, met het koper",
            "Daar lag de hoofdstad Leopoldstad",
            "Daar woonden de meeste Belgen van het land",
            "Daar lag de enige haven van Congo",
        ],
        0,
        "Wie Katanga had, had de rijkdom van het land. Belgische belangen speelden mee.",
    ),
    tabel(
        "Welke uitspraken over de dood van Lumumba kloppen?",
        [
            ("Hij werd begin 1961 afgezet, gevangengenomen en vermoord.", J),
            ("Een Belgische onderzoekscommissie stelde in 2001 Belgische betrokkenheid vast.", J),
            ("Die vaststelling kwam veertig jaar na de feiten.", J),
            ("Hij stierf in 1997 als oude man.", F),
        ],
        "Het duurde veertig jaar voor het Belgische parlement de betrokkenheid onderzocht.",
    ),
    # --- Mobutu
    tabel(
        "Welke kenmerken had het bestuur van Mobutu?",
        [
            ("Eén partij", J),
            ("Geen vrije pers", J),
            ("Grote rijkdom voor hemzelf en zijn omgeving", J),
            ("Vrije verkiezingen om de vijf jaar", F),
        ],
        "Men spreekt van een kleptocratie: een bestuur dat de rijkdom van het land voor zichzelf neemt.",
    ),
    inv(
        "Hoe noemt men een bestuur waarin de leiders de rijkdom van het land voor zichzelf nemen?",
        ["een kleptocratie", "kleptocratie"],
        "Mobutu en zijn omgeving werden schatrijk, terwijl het land arm bleef.",
    ),
    mk(
        "Waarom steunde het westen Mobutu zo lang?",
        [
            "Hij was een bondgenoot tegen het communisme",
            "Hij liet vrije verkiezingen houden in heel Zaïre",
            "Hij gaf Congo terug aan België",
            "Hij was lid van de Europese Unie",
        ],
        0,
        "In de Koude Oorlog telde de keuze van kamp zwaarder dan de manier van besturen.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Mobutu werd afgezet en het land weer Congo heette.",
        "tijdlijn-1750-2030.svg",
        [[78.9, 25, 6.2, 55]],
        "1997, net voor het streepje van 2000.",
    ),
    keuze(
        "In 1971 gaf Mobutu het land de naam [[*Zaïre|Katanga|Leopoldstad]]. Na 1997 heette het de [[*Democratische Republiek Congo|Congo-Vrijstaat|Belgische Kongo]].",
        "Zaïre van 1971 tot 1997, daarna de Democratische Republiek Congo.",
    ),
    # --- vandaag
    tabel(
        "Welke problemen kent het oosten van Congo na 1997?",
        [
            ("Gewapende groepen vechten om gebied en mijnen.", J),
            ("Miljoenen mensen zijn op de vlucht geweest.", J),
            ("Er zijn geen grondstoffen meer.", F),
        ],
        "De rijkdom aan grondstoffen voedt net de strijd.",
    ),
    mk(
        "Waarom spelen grondstoffen uit Congo vandaag nog een rol in de wereldeconomie?",
        [
            "Kobalt en coltan zitten in batterijen",
            "Congo levert nog altijd het meeste rubber",
            "Congo heeft de enige steenkool ter wereld",
            "Alle euromunten worden van Congolees koper gemaakt",
        ],
        0,
        "Kobalt en coltan zitten in batterijen en elektronica.",
    ),
    tabel(
        "Hoe gaat België vandaag om met het koloniale verleden?",
        [
            ("In 2020 richtte het parlement een onderzoekscommissie op.", J),
            ("De commissie leverde veel materiaal, maar geen gezamenlijk besluit.", J),
            ("Koning Filip sprak zijn diepste spijt uit.", J),
            ("Koning Filip bood een formele verontschuldiging aan.", F),
        ],
        "Spijt in een brief en bij het bezoek van 2022, maar geen formele verontschuldiging.",
    ),
    sorteer(
        "Waar zie je in Congo vandaag nog sporen van de koloniale tijd?",
        ["Grenzen", "Economie", "Bestuur"],
        [
            ["lijnen getrokken in Berlijn", "Grenzen"],
            ["uitvoer van enkele grondstoffen", "Economie"],
            ["mijnen in handen van buitenlandse bedrijven", "Economie"],
            ["een apparaat dat nooit voor zelfbestuur gemaakt was", "Bestuur"],
        ],
        "Grenzen, economie en bestuur dragen er nog de sporen van.",
    ),
    mk(
        "Vergelijk Belgisch Congo van 1950 met Congo van 1965. Wat valt op?",
        [
            "De macht lag eerst in Brussel, daarna bij één man",
            "In beide jaren waren er vrije verkiezingen",
            "In beide jaren was Lumumba premier",
            "In 1965 was Congo opnieuw een kolonie",
        ],
        0,
        "Van een kolonie bestuurd vanuit Brussel naar een dictatuur van Mobutu.",
    ),
    sleep(
        "Op de [[Ronde Tafelconferentie]] in Brussel werd beslist dat Congo op [[30 juni]] 1960 onafhankelijk zou worden. [[Lumumba]] werd de eerste premier.",
        ["Conferentie van Berlijn", "21 juli", "Mobutu"],
        "Berlijn verdeelde Afrika in 1884-1885. Mobutu kwam pas in 1965 aan de macht.",
    ),
    open_(
        "Leg uit waarom Congo na 30 juni 1960 in een crisis terechtkwam. Gebruik minstens drie elementen.",
        "De onafhankelijkheid kwam heel snel, na amper anderhalf jaar, zonder voorbereiding. Er waren amper Congolezen met een universitair diploma om het land te besturen. In juli 1960 kwam het leger in opstand en scheidde het rijke Katanga zich af, met Belgische belangen erachter. Begin 1961 werd premier Lumumba vermoord. De Koude Oorlog speelde mee: het westen steunde later Mobutu.",
    ),
    open_(
        "Leg uit waarom het koloniale verleden in België vandaag nog besproken wordt, en geef twee voorbeelden.",
        "De gevolgen van de koloniale tijd werken door in Congo, in grenzen, economie en bestuur, en er zijn nog veel vragen over wat er gebeurde, zoals de moord op Lumumba. Voorbeelden: in 2020 richtte het parlement een onderzoekscommissie op, en koning Filip sprak in 2020 en 2022 zijn diepste spijt uit.",
    ),
    mk(
        "Hoe kwam Mobutu in 1965 aan de macht?",
        [
            "Met een staatsgreep",
            "Na vrije verkiezingen met veel partijen",
            "Als opvolger aangeduid door koning Boudewijn",
            "Na een beslissing van de Verenigde Naties",
        ],
        0,
        "Hij greep de macht en bleef tot 1997.",
    ),
    tabel(
        "Waarom kreeg de dekolonisatie na 1945 een duw in de rug?",
        [
            ("Het prestige van Europa was door de oorlog aangetast.", J),
            ("Het handvest van de VN sprak van zelfbeschikking.", J),
            ("De Europese landen waren sterker dan ooit.", F),
        ],
        "Een verzwakt Europa kon zijn kolonies moeilijk vasthouden.",
    ),
]
