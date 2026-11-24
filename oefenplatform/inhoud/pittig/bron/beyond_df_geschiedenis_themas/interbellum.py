"""Het interbellum: de opkomst van het totalitarisme — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="stalin-affiche.webp", zelf=False,
         wat="Gustav Klutsis, affiche uit 1935: Stalin met arbeiders, piloten en kinderen.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="casus over propaganda in de Sovjet-Unie"),
]

VRAGEN = [
    # --- drie machtsovernames
    tabel(
        "Hoe kwam elke leider aan de macht?",
        [
            ("Lenin, 1917", "Revolutie"),
            ("Mussolini, 1922", "Benoemd"),
            ("Hitler, 1933", "Benoemd"),
        ],
        "De bolsjewieken grepen de macht. Mussolini werd na de mars op Rome door de koning benoemd, Hitler werd rijkskanselier langs de grondwet om.",
        kolommen=["Revolutie", "Benoemd"],
    ),
    mk(
        "Wat is opvallend aan de manier waarop Hitler de democratie afbrak?",
        [
            "Hij deed het van binnenuit, na een wettige benoeming",
            "Hij greep de macht met een staatsgreep en een burgeroorlog",
            "Hij werd door de Volkenbond aangesteld als leider van Duitsland",
            "Hij liet zich door een volksraadpleging tot koning kronen",
        ],
        0,
        "Hij werd in januari 1933 benoemd, liet zich volmachten geven en verbood daarna de andere partijen en de vrije vakbonden.",
    ),
    volgorde(
        "Zet de stappen van Hitler na zijn benoeming in de juiste volgorde.",
        ["Hitler wordt rijkskanselier", "Hij krijgt volmachten om zonder parlement te regeren", "De Neurenberger wetten", "De Kristalnacht", "De inval in Polen"],
        "Januari 1933, daarna de volmachten, 1935, november 1938 en september 1939.",
    ),
    # --- Sovjet-Unie
    tabel(
        "Groei en terreur liepen in de Sovjet-Unie samen. Welke uitspraken tonen dat?",
        [
            ("De zware industrie groeide snel.", J),
            ("De collectivisering kostte miljoenen mensen het leven.", J),
            ("Boeren mochten zelf kiezen of ze hun grond inbrachten.", F),
            ("Ook partijleiders en officieren werden opgepakt.", J),
        ],
        "Groei en terreur liepen samen. Wie zich tegen de collectivisering verzette, werd verbannen of gedood.",
    ),
    mk(
        "Waarom volgde in Oekraïne een hongersnood met miljoenen doden?",
        [
            "De collectivisering ontwrichtte de landbouw",
            "De Duitse bezetter nam al het graan mee naar Duitsland",
            "De vijfjarenplannen verboden elke vorm van landbouw",
            "Een overstroming vernielde alle akkers van het land",
        ],
        0,
        "Boeren moesten hun grond en vee inbrengen in grote staatsbedrijven. Wie zich verzette, werd verbannen of gedood.",
    ),
    casus(
        "Bekijk de affiche uit de Sovjet-Unie van 1935. Stalin staat in het midden, groter dan de anderen. Rond hem staan lachende arbeiders, piloten en kinderen.",
        [
            met_prent("stalin-affiche.webp", mk(
                "Hoe lees je deze affiche het best?",
                [
                    "Als propaganda voor de leider en zijn bewind",
                    "Als een foto van het echte leven in de fabriek",
                    "Als kritiek van de arbeiders op Stalin",
                    "Als een affiche van de Volkenbond",
                ],
                0,
                "De affiche verheerlijkt de leider. Over het echte leven, met honger en terreur, zegt ze niets.",
            )),
            tabel(
                "Mag je dit besluiten op basis van de affiche?",
                [
                    ("Het regime wilde Stalin als geliefde leider tonen.", "Mag"),
                    ("Alle arbeiders in de Sovjet-Unie waren gelukkig.", "Mag niet"),
                    ("Propaganda was een middel van het regime.", "Mag"),
                ],
                "Propaganda zegt veel over wat het regime wilde tonen, weinig over hoe het echt was.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["De staat plant de economie, met zware industrie eerst.", "Vijfjarenplan"],
            ["Boeren brengen grond en vee in grote staatsbedrijven in.", "Collectivisering"],
            ["Ook partijleiders en officieren worden opgepakt.", "Grote Terreur"],
            ["Gevangenen doen er dwangarbeid.", "Werkkamp"],
        ],
        ["Appeasement", "Volmacht"],
        "Vier middelen en gevolgen van Stalins bewind.",
    ),
    # --- fascisme
    tabel(
        "Welke kenmerken horen bij het fascisme van Mussolini?",
        [
            ("Eén partij en één leider", J),
            ("Geen enkele oppositie", J),
            ("De staat staat boven het individu", J),
            ("Vrije verkiezingen met veel partijen", F),
        ],
        "Il Duce, de leider, duldde geen oppositie.",
    ),
    # --- crisis
    casus(
        "Een Duitse arbeider vertelt in 1932: \"Ik ben al twee jaar werkloos. De fabriek is dicht, de bank is failliet. De partijen in het parlement maken ruzie en doen niets. Een man die werk en orde belooft, krijgt mijn stem.\"",
        [
            mk(
                "Welk verband tussen de wereldcrisis en het nazisme toont deze bron?",
                [
                    "Werkloosheid maakte de partij aantrekkelijk",
                    "De crisis maakte de democratie in Duitsland sterker",
                    "De nazipartij veroorzaakte de beurskrach in New York",
                    "Werklozen mochten in Duitsland niet stemmen",
                ],
                0,
                "Wie geen werk en geen hoop had, luisterde naar wie orde en werk beloofde.",
            ),
            tabel(
                "Welke problemen van de Weimarrepubliek herken je of kun je eraan toevoegen?",
                [
                    ("crisis en werkloosheid", J),
                    ("herstelbetalingen", J),
                    ("inflatie", J),
                    ("een te sterk leger", F),
                ],
                "Herstelbetalingen, inflatie en crisis, met daarbovenop de wrok om Versailles. Het leger was net klein.",
            ),
        ],
    ),
    mk(
        "Waarom bleef de beurskrach van New York niet beperkt tot de Verenigde Staten?",
        [
            "Internationale handel en leningen brachten ze naar Europa",
            "Alle Europese banken stonden in New York",
            "De Volkenbond verplichtte Europa om mee te doen",
            "Europa had geen eigen fabrieken of banken",
        ],
        0,
        "Amerikaanse leningen werden teruggevraagd en de handel viel stil. Zo sloeg de crisis over.",
    ),
    tabel(
        "Een leerling zegt: \"Door de crisis van de jaren dertig werd de democratie in Europa sterker.\" Welke gegevens spreken dat tegen?",
        [
            ("Partijen die de democratie afwezen, groeiden.", J),
            ("In België haalden Rex en het VNV zetels.", J),
            ("Hitler werd in 1933 rijkskanselier.", J),
            ("In de crisis vielen banken om.", F),
        ],
        "Dat banken omvielen, klopt, maar het zegt niets over de democratie. De andere drie tonen dat de democratie onder druk kwam.",
    ),
    sleep(
        "De wrok om het Verdrag van [[Versailles]] gaf de nazipartij een verhaal. De [[werkloosheid]] na de beurskrach van [[1929]] gaf haar kiezers.",
        ["Wenen", "inflatie van 1917", "1939"],
        "Samen leverden ze het verhaal en de nood.",
    ),
    # --- totalitarisme
    tabel(
        "Autoritaire of totalitaire staat?",
        [
            ("De staat eist gehoorzaamheid, maar laat je gedachten met rust.", "Autoritair"),
            ("De staat wil ook je overtuiging en je denken beheersen.", "Totalitair"),
            ("Jeugdbewegingen binden kinderen vroeg aan de leider.", "Totalitair"),
            ("Een ministerie van propaganda stuurt radio en film.", "Totalitair"),
        ],
        "De ene eist gehoorzaamheid, de andere ook overtuiging.",
        kolommen=["Autoritair", "Totalitair"],
    ),
    mk(
        "Je ziet een foto van een massabijeenkomst met vlaggen, strakke rijen en één spreker. Waarom organiseerde een totalitair regime zulke bijeenkomsten?",
        [
            "Om het volk achter de leider te krijgen",
            "Om de oppositie vrij te laten spreken",
            "Om de leider te laten verkiezen door het volk",
            "Om een neutraal verslag van de politiek te geven",
        ],
        0,
        "Massabijeenkomsten, radio en film waren propaganda: het volk moest één worden met de leider.",
    ),
    sorteer(
        "Wat gebeurde er met de Joden in nazi-Duitsland?",
        ["1935", "1938"],
        [
            ["Ze verliezen hun rechten als burger.", "1935"],
            ["De uitsluiting wordt wet.", "1935"],
            ["Synagogen worden in brand gestoken.", "1938"],
            ["Joodse winkels worden geplunderd.", "1938"],
        ],
        "De Neurenberger wetten van 1935 en de Kristalnacht van november 1938.",
    ),
    mk(
        "Wat toont de Kristalnacht over de rol van de staat?",
        [
            "Het geweld werd door de staat aangemoedigd",
            "De staat beschermde de Joodse winkels met de politie",
            "De staat wist niet wat er gebeurde",
            "De Volkenbond liet de synagogen herbouwen",
        ],
        0,
        "Het was geen spontane uitbarsting: de staat moedigde het geweld aan.",
    ),
    tabel(
        "Welke kenmerken hadden de drie regimes gemeen?",
        [
            ("Eén partij en één leider", J),
            ("Geen vrije pers", J),
            ("Propaganda", J),
            ("Een geplande economie zonder privébezit", F),
        ],
        "De planeconomie hoorde bij de Sovjet-Unie, niet bij het fascisme en het nazisme.",
    ),
    # --- weg naar 1939
    volgorde(
        "Zet de stappen naar de Tweede Wereldoorlog in de juiste volgorde.",
        ["Het Rijnland wordt opnieuw bezet", "Oostenrijk wordt ingelijfd", "De conferentie van München", "Duitsland neemt de rest van Tsjechoslowakije", "Het pact met de Sovjet-Unie", "De inval in Polen"],
        "Elke stap bleef zonder gevolg, tot de inval in Polen in september 1939.",
    ),
    mk(
        "Waarom gaven Frankrijk en Groot-Brittannië in München toe aan Hitler?",
        [
            "Ze hoopten zo een oorlog te vermijden",
            "Ze waren bondgenoten van Duitsland",
            "Ze wilden zelf Tsjechoslowakije verdelen",
            "Hitler had de oorlog al gewonnen",
        ],
        0,
        "Dat heet appeasement, de verzoeningspolitiek. Het hield de oorlog niet tegen.",
    ),
    casus(
        "Een Britse krant schrijft in oktober 1938, na München: \"Vrede in onze tijd! Tsjechoslowakije staat een stuk grond af, en Europa is gered.\"",
        [
            tabel(
                "Welke besluiten kun je trekken met je kennis van wat volgde?",
                [
                    ("De krant was te optimistisch.", J),
                    ("Enkele maanden later nam Duitsland de rest van Tsjechoslowakije.", J),
                    ("München heeft de oorlog voorgoed afgewend.", F),
                ],
                "Een jaar later viel Duitsland Polen binnen.",
            ),
            mk(
                "Waarom kreeg Hitler door elke toegeving meer vertrouwen?",
                [
                    "Elke stap bleef zonder gevolg",
                    "De Volkenbond gaf hem telkens een prijs",
                    "Frankrijk sloot een verbond met hem",
                    "De VS stuurden hem soldaten",
                ],
                0,
                "Rijnland, Oostenrijk, een deel van Tsjechoslowakije: niemand hield hem tegen.",
            ),
        ],
    ),
    mk(
        "Wat was het geheime deel van het pact tussen Duitsland en de Sovjet-Unie van augustus 1939?",
        [
            "Ze verdeelden Polen",
            "Ze beloofden samen Frankrijk aan te vallen",
            "Ze richtten samen een nieuwe Volkenbond op",
            "Ze ruilden het Rijnland voor Oekraïne",
        ],
        0,
        "Openlijk beloofden ze elkaar niet aan te vallen. In het geheim verdeelden ze Polen. Een week later viel Duitsland binnen.",
    ),
    keuze(
        "Het interbellum is de periode van [[*1918|1914|1929]] tot [[*1939|1945|1933]].",
        "Tussen het einde van de ene en het begin van de andere wereldoorlog.",
    ),
    open_(
        "Leg uit hoe het Verdrag van Versailles en de wereldcrisis samen de opkomst van Hitler mogelijk maakten.",
        "Versailles liet in Duitsland wrok na: Duitsland kreeg de schuld, moest herstelbetalingen doen en verloor gebied. De Weimarrepubliek werd daarmee belast. Na de beurskrach van 1929 kwamen massale werkloosheid en armoede. Veel kiezers keerden zich af van de democratie en kozen voor de nazipartij, die een verhaal en orde beloofde. Zo werd Hitler in 1933 benoemd.",
    ),
    open_(
        "Vergelijk de Sovjet-Unie van Stalin met nazi-Duitsland. Geef twee gelijkenissen en een verschil.",
        "Gelijkenissen: één partij en één leider, een geheime politie, terreur en censuur, propaganda en jeugdbewegingen. Verschil: de Sovjet-Unie had een door de staat geplande economie en kwam er na een revolutie; Hitler werd langs een benoeming aan de macht gebracht en schafte het privébezit niet af.",
    ),
    tabel(
        "Welke stappen zette Hitler om zijn alleenheerschappij uit te bouwen?",
        [
            ("Hij liet zich volmachten geven.", J),
            ("Hij verbood de andere partijen.", J),
            ("Hij verbood de vrije vakbonden.", J),
            ("Hij liet vrije verkiezingen houden in 1934.", F),
        ],
        "Zo regeerde hij zonder parlement en zonder tegenspraak.",
    ),
    inv(
        "Welke titel droeg Mussolini als leider van Italië?",
        ["Il Duce", "Duce", "de Duce"],
        "Il Duce betekent: de leider.",
    ),
    mk(
        "Waarom verbood Hitler naast de andere partijen ook de vrije vakbonden?",
        [
            "Ze konden de arbeiders tegen hem verenigen",
            "Ze waren in 1919 al door Versailles verboden",
            "De vakbonden wilden zelf de partij van Hitler leiden",
            "De Volkenbond had erom gevraagd in Genève",
        ],
        0,
        "Een totalitaire staat duldt geen organisatie die los van de leider mensen samenbrengt.",
    ),
]
