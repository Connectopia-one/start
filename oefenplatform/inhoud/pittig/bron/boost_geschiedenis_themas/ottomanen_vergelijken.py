"""Het Ottomaanse Rijk en samenlevingen vergelijken — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="ottomaanse-rijk.svg", zelf=True,
         wat="Schema van het Ottomaanse Rijk rond een zee, op drie werelddelen, met drie steden A, B en C zonder naam.",
         vragen="klikvragen op de hoofdstad (A) en op de belegerde stad (B)"),
    dict(bestand="tijdlijn-1400-1800.svg", zelf=True,
         wat="Tijdlijn van 1400 tot 1800 (dezelfde als bij De 'Nieuwe' Wereld).",
         vragen="klikvragen op 1453 en op de regering van Süleyman"),
    dict(bestand="suleymaniye.jpg", zelf=False,
         wat="Foto van de Süleymaniye-moskee in Istanbul, met koepels en minaretten, of van het blauw-witte tegelwerk binnenin.",
         waar="Wikimedia Commons, zoek op 'Süleymaniye Mosque' (kies een foto in het publiek domein of met vrije licentie en vermeld de fotograaf).",
         vragen="sorteervraag over Ottomaanse bouwkunst"),
]

TL = "tijdlijn-1400-1800.svg"
RIJK = "ottomaanse-rijk.svg"

VRAGEN = [
    tabel(
        "Klopt elke uitspraak over de ligging van het Ottomaanse Rijk?",
        [
            ("Het zwaartepunt lag rond de oostelijke Middellandse Zee.", J),
            ("Het rijk lag op drie werelddelen tegelijk.", J),
            ("Het reikte over de Balkan, Anatolië en Noord-Afrika.", J),
            ("Het lag vooral in West-Europa.", F),
        ],
        "Balkan, Anatolië, het Nabije Oosten en Noord-Afrika: Europa, Azië en Afrika.",
    ),
    klik(
        "Bekijk het schema van het Ottomaanse Rijk. Klik op de stad die de Ottomanen tot hun hoofdstad maakten.",
        RIJK, [[53.0, 29.0, 12.0, 13.0]],
        "A is Constantinopel, aan de zee-engte tussen Europa en Azië.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Ottomanen Constantinopel veroveren.",
        TL, [[15.5, 25, 2.2, 55]],
        "In 1453.",
    ),
    mk(
        "Waarom nemen veel historici de Ottomaanse verovering van Constantinopel als een grens tussen middeleeuwen en vroegmoderne tijd?",
        [
            "Daarmee eindigt het Byzantijnse Rijk",
            "Daarmee begint de Franse Revolutie, die alles verandert",
            "Toen werd de boekdrukkunst in Constantinopel zelf uitgevonden",
            "Toen werd het christendom in heel Europa voor het eerst verboden",
        ],
        0,
        "Met de val van de stad verdwijnt het Oost-Romeinse of Byzantijnse Rijk.",
    ),
    mk(
        "Waarin verschilde de sultan van Lodewijk XIV?",
        [
            "De sultan was ook kalief: wereldlijk en godsdienstig hoofd tegelijk",
            "De sultan werd door het volk verkozen, Lodewijk niet",
            "De sultan had geen enkele macht, zijn ministers beslisten alles",
            "De sultan moest elk besluit laten goedkeuren door de paus",
        ],
        0,
        "Lodewijk stelde de godsdienst in dienst van zijn macht, maar het hoofd van de Kerk was de paus.",
    ),
    tabel(
        "Wat hebben het gezag van de sultan en dat van Lodewijk XIV gemeen? Klopt elke uitspraak?",
        [
            ("Alle macht ligt bij één persoon.", J),
            ("Die persoon is aan niemand verantwoording schuldig.", J),
            ("Een grondwet begrenst hun macht.", F),
            ("Een parlement beslist mee.", F),
        ],
        "Verkiezing, grondwet en parlement ontbreken bij allebei.",
    ),
    inv(
        "Hoe heet het Ottomaanse stelsel waarbij godsdienstige minderheden hun eigen gemeenschap bestuurden, met eigen recht en eigen scholen?",
        ["millet", "millet-stelsel", "milletstelsel", "het millet-stelsel", "het milletstelsel"],
        "Het millet-stelsel. Christenen en joden betaalden een aparte belasting, maar mochten hun geloof behouden.",
    ),
    mk(
        "Na 1492 vonden joden die uit Spanje verdreven werden een nieuwe thuis in Saloniki en Constantinopel. Wat toont dat?",
        [
            "Andere godsdiensten mochten er blijven bestaan, ook al was het geen gelijkheid",
            "Joden hadden in het Ottomaanse Rijk precies dezelfde rechten als moslims",
            "Het Ottomaanse Rijk wilde alle joden tot de islam bekeren",
            "Spanje en het Ottomaanse Rijk hadden dat samen zo afgesproken",
        ],
        0,
        "In christelijk Europa werd afwijking vervolgd. In het Ottomaanse Rijk was er wel een plaats, al was het geen gelijkheid.",
    ),
    tabel(
        "Klopt elke uitspraak over de economie van het Ottomaanse Rijk?",
        [
            ("De landroutes tussen Europa en Azië liepen door zijn gebied.", J),
            ("Handel en ambacht bloeiden in grote steden.", J),
            ("De staat hield toezicht op prijzen en voorraden.", J),
            ("Met christelijke landen werd niet gehandeld.", F),
        ],
        "Met christelijke landen werd juist volop gehandeld.",
    ),
    mk(
        "Wat heeft het Ottomaanse Rijk te maken met de Europese ontdekkingsreizen?",
        [
            "Het beheerste de landroutes naar Azië, dus zocht Europa een zeeweg",
            "Ottomaanse zeevaarders toonden de Portugezen de weg naar Indië",
            "Het Ottomaanse Rijk betaalde de reis van Columbus",
            "De Ottomanen verboden elke handel met Azië",
        ],
        0,
        "Wie de landroutes beheerst, bepaalt mee de prijs. Een eigen zeeweg ontweek dat.",
    ),
    klik(
        "Süleyman I regeerde bijna een halve eeuw. Klik op de tijdlijn op de periode van zijn regering.",
        TL, [[31.2, 25, 10.0, 55]],
        "Süleyman regeerde van 1520 tot 1566, in dezelfde jaren als Karel V.",
    ),
    klik(
        "Bekijk opnieuw het schema. Klik op de stad die in 1529 door de Ottomanen belegerd werd en standhield.",
        RIJK, [[28.0, 7.0, 11.0, 13.0]],
        "B is Wenen. De stad lag buiten het rijk en hield stand.",
    ),
    koppel(
        "Süleyman I had twee bijnamen. Welke hoort waar?",
        [["in het Westen", "de Prachtlievende"], ["in eigen land", "de Wetgever"]],
        ["de Zonnekoning"],
        "In het Westen de Prachtlievende, in eigen land de Wetgever. De Zonnekoning is Lodewijk XIV.",
    ),
    mk(
        "Waarom sloot de Franse koning Frans I een verstandhouding met de sultan?",
        [
            "Hij zocht een bondgenoot tegen de Habsburgers",
            "Hij wilde zelf moslim worden en kalief van Frankrijk",
            "De paus had hem dat uitdrukkelijk gevraagd",
            "De sultan had Parijs veroverd en eiste trouw",
        ],
        0,
        "Politiek belang woog daar zwaarder dan geloof.",
    ),
    mk(
        "Wat zijn de capitulaties?",
        [
            "Handelsvoorrechten die de sultan aan Europese kooplui gaf",
            "De overgave van een Europese stad aan de Ottomanen",
            "De belasting die christenen en joden apart betaalden",
            "De vredesverdragen na het beleg van Wenen",
        ],
        0,
        "Franse en later andere kooplui kregen eigen rechten in Ottomaanse havens. De naam heeft niets met overgave te maken.",
    ),
    sorteer(
        "Langs welke weg verliep dit contact tussen het Ottomaanse Rijk en Europa?",
        ["Oorlog", "Handel", "Diplomatie"],
        [
            ["gevechten aan de grenzen in de Balkan", "Oorlog"],
            ["zeeslagen", "Oorlog"],
            ["kooplui in het Middellandse Zeegebied", "Handel"],
            ["vaste gezanten aan het hof", "Diplomatie"],
        ],
        "Oorlog, handel en diplomatie. Daarom mag je het rijk niet enkel als vijand van Europa beschrijven.",
    ),
    tabel(
        "Klopt elke uitspraak over de bloei en het verval van het rijk?",
        [
            ("De 16de eeuw is het hoogtepunt van het rijk.", J),
            ("De handel verlegde zich later naar de oceanen, weg van de landroutes.", J),
            ("Europa liep later voor op het gebied van techniek en leger.", J),
            ("Het verval begon al in de 16de eeuw.", F),
        ],
        "Het verval komt later en heeft meerdere oorzaken, ook de grootte van het rijk.",
    ),
    met_prent(
        "suleymaniye.jpg",
        sorteer(
            "Bekijk de Süleymaniye in Istanbul. Is dit een kenmerk van Ottomaanse bouwkunst of niet?",
            ["Ottomaans", "Niet Ottomaans"],
            [
                ["grote koepels", "Ottomaans"],
                ["slanke minaretten", "Ottomaans"],
                ["geometrische patronen en sierschrift", "Ottomaans"],
                ["tegelwerk in blauw en wit", "Ottomaans"],
                ["glasramen vol heiligenfiguren", "Niet Ottomaans"],
            ],
            "Koepels, minaretten, sierschrift, patronen en tegelwerk. Mensenfiguren vermijdt men.",
        ),
        volgt=True,
    ),
    # --- samenlevingen vergelijken
    sorteer(
        "Op welk soort kenmerk vergelijk je samenlevingen hier?",
        ["Politiek", "Sociaal", "Cultureel", "Economisch"],
        [
            ["bestuurlijke organisatie", "Politiek"],
            ["migratie", "Sociaal"],
            ["ongelijkheid", "Sociaal"],
            ["kunstuitingen", "Cultureel"],
            ["wetenschappen", "Cultureel"],
            ["handel", "Economisch"],
        ],
        "Politieke, sociale, culturele en economische kenmerken zijn de vaste vergelijkingspunten.",
    ),
    mk(
        "Wat hoort niet bij de kenmerken waarop je samenlevingen vergelijkt?",
        ["De afstand tot de evenaar", "De bestuurlijke organisatie", "De levensbeschouwing", "Het economische systeem"],
        0,
        "De afstand tot de evenaar is geen kenmerk van de samenleving zelf.",
    ),
    koppel(
        "Imperialisme of kolonialisme: welk begrip past bij elke beschrijving?",
        [
            ["het streven van een staat om zijn macht over andere gebieden uit te breiden", "Imperialisme"],
            ["één vorm daarvan, met vestiging en bestuur ter plaatse", "Kolonialisme"],
        ],
        ["Periodisering"],
        "Kolonialisme is een vorm van imperialisme. De twee betekenen dus niet hetzelfde.",
    ),
    tabel(
        "Wat hebben de Egyptische en de middeleeuwse gelaagde samenleving gemeen? Klopt elke uitspraak?",
        [
            ("Een kleine groep bovenaan leeft van het werk van een grote groep onderaan.", J),
            ("Godsdienst rechtvaardigt de ordening.", J),
            ("Je geboorte bepaalt je leven grotendeels.", J),
            ("Opklimmen ging in allebei makkelijk.", F),
        ],
        "Opklimmen kon in geen van beide.",
    ),
    mk(
        "Welke twee samenlevingen zijn voorbeelden van een multiculturele samenleving?",
        [
            "Het Ottomaanse Rijk en Al-Andalus",
            "Het Frankische rijk en het domein van een heer",
            "De Republiek van Plato en Sparta",
            "Het rijk van de Inca's en dat van de Azteken",
        ],
        0,
        "In beide leefden mensen met verschillende culturen en godsdiensten naast elkaar.",
    ),
    volgorde(
        "Zet deze economische systemen in de juiste volgorde, van vroeg naar laat.",
        ["het zelfvoorzienende domein", "het handelskapitalisme", "de industriële productie"],
        "Middeleeuwen, vroegmoderne tijd, 19de eeuw.",
    ),
    mk(
        "Wat betekent vergelijken?",
        [
            "Zowel gelijkenissen als verschillen benoemen",
            "Enkel de gelijkenissen zoeken",
            "Enkel de verschillen opsommen",
            "Beslissen welke samenleving de beste was",
        ],
        0,
        "Enkel gelijkenissen maakt alles hetzelfde, enkel verschillen maakt alles uniek.",
    ),
    mk(
        "Waarom vergelijk je met vaste kenmerken en niet zomaar met wat opvalt?",
        [
            "Wat opvalt, is vaak enkel wat vreemd is aan ons",
            "Vaste kenmerken zijn sneller te vinden in een boek",
            "Wat opvalt, staat nooit in de bronnen",
            "Leerkrachten willen nu eenmaal altijd dezelfde lijst",
        ],
        0,
        "Met vaste punten vergelijk je hetzelfde met hetzelfde, en zie je ook wat je anders over het hoofd zou zien.",
    ),
    volgorde(
        "Zet deze historische periodes in de juiste volgorde.",
        ["de prehistorie", "het oude nabije oosten", "de klassieke oudheid", "de middeleeuwen", "de vroegmoderne tijd"],
        "Van de prehistorie tot de vroegmoderne tijd.",
    ),
    inv(
        "Hoe heet het verdelen van de tijd in stukken met een naam en een grens? Antwoord met één woord.",
        ["periodisering", "de periodisering"],
        "Periodisering. Een periodegrens is altijd een keuze, want de verandering gebeurt niet overal tegelijk.",
    ),
    casus(
        "Een leerling schrijft: 'In 1302 versloegen de Belgen de Fransen. Mensen in de middeleeuwen waren dom, want ze geloofden dat de aarde in het midden van alles stond.'",
        [
            mk(
                "Welke fout maakt de leerling in de eerste zin?",
                ["Een anachronisme", "Een periodisering", "Een capitulatie", "Een vergelijking"],
                0,
                "België bestond in 1302 nog niet. Iets in de verkeerde tijd plaatsen is een anachronisme.",
            ),
            mk(
                "Wat ontbreekt er in de tweede zin?",
                ["Historische empathie", "Een jaartal", "Een bron uit de oudheid", "Een vergelijking met Egypte"],
                0,
                "Historische empathie is begrijpen waarom iets toen vanzelfsprekend leek. Dat is niet hetzelfde als goedkeuren.",
            ),
        ],
    ),
]
