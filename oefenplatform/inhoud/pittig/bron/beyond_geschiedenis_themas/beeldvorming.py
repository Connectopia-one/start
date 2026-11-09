"""Beeldvorming, vergelijken en verleden-heden-toekomst — pittig (🌍 Beyond).

De bron in de casus is een oefenbron: een verzonnen voorbeeld, en dat staat er ook bij.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = []

VRAGEN = [
    mk(
        "Een leerling zegt: \"Mijn handboek toont gewoon het verleden zoals het was.\" Wat is de beste reactie?",
        [
            "Het toont een beeld dat iemand opbouwde uit bronnen en interpretatie",
            "Klopt, een handboek is altijd een exacte kopie van het verleden",
            "Klopt, zolang het handboek recenter is dan de gebeurtenissen zelf",
            "Een handboek toont nooit iets over het verleden, alleen meningen",
        ],
        0,
        "Het verleden zelf ligt achter ons. Wat wij hebben, is historische beeldvorming.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over historische beelden.",
        [
            ("Over dezelfde gebeurtenis kunnen meerdere beelden naast elkaar bestaan.", J),
            ("Twee historici met dezelfde bronnen komen altijd tot precies hetzelfde beeld.", F),
            ("Een beeld kan veranderen als er nieuwe bronnen opduiken.", J),
            ("Een beeld verandert enkel als het verleden zelf verandert.", F),
        ],
        "Het verleden verandert niet, het beeld wel: door nieuwe bronnen en door de vragen die de samenleving stelt.",
    ),
    mk(
        "Welke Belgische figuur is het duidelijkste voorbeeld van een historisch beeld dat sterk veranderde?",
        ["Leopold II", "Hendrik Conscience", "Adolphe Sax", "Peter Paul Rubens"],
        0,
        "Van koning-bouwer naar een veel kritischer blik, door nieuwe bronnen en nieuwe vragen.",
    ),
    mk(
        "Wat stuurt volgens de standplaatsgebondenheid mee welke vragen een historicus stelt?",
        [
            "Zijn tijd, zijn afkomst en zijn overtuiging",
            "Enkel het aantal bronnen dat hij vindt",
            "De lengte van het boek dat hij moet schrijven",
            "Niets, een goede historicus is volledig neutraal",
        ],
        0,
        "Iedere historicus kijkt vanuit een eigen positie.",
    ),
    tabel(
        "Een historicus kan niet volledig neutraal zijn. Wat kan hij wel doen?",
        [
            ("Eerlijk zijn over zijn vertrekpunt", J),
            ("Zijn bronnen tonen", J),
            ("Andere lezingen bespreken", J),
            ("Doen alsof hij zelf geen standpunt heeft", F),
        ],
        "Openheid over vertrekpunt, bronnen en andere lezingen maakt een beeld controleerbaar.",
    ),
    mk(
        "Een leerling schrijft in een toets: \"Napoleon was eigenlijk een heel verlegen man.\" Hij noemt geen enkele bron. Welke redeneerwijze ontbreekt?",
        ["Bewijs gebruiken", "Actualiseren", "Continuïteit benoemen", "Verbanden leggen"],
        0,
        "Elke uitspraak over het verleden moet op bronnen kunnen steunen. Zonder bron is het een mening.",
    ),
    koppel(
        "Welke redeneerwijze pas je toe in elke situatie?",
        [
            ["Het Marshallplan wilde Europa heropbouwen, maar zette het ook stevig in het westerse kamp", "Bedoelde en onbedoelde gevolgen"],
            ["Rosa Parks beslist om te blijven zitten", "Menselijke actoren benoemen"],
            ["Je legt een verband tussen propaganda uit de jaren dertig en desinformatie vandaag", "Actualiseren"],
            ["Je begrijpt de Franse Revolutie vanuit de honger en de schulden van toen", "Historisch contextualiseren"],
        ],
        ["Stereotypering analyseren"],
        "Twaalf redeneerwijzen staan op het programma; hier zie je er vier aan het werk.",
    ),
    mk(
        "Een leerling schrijft: \"De mensen in 1850 waren slecht, want vandaag is kinderarbeid verboden.\" Wat loopt er mis?",
        [
            "Hij beoordeelt het verleden met de maatstaf van vandaag",
            "Hij gebruikt te veel bronnen uit 1850",
            "Kinderarbeid bestond in 1850 nog niet",
            "Hij past de redeneerwijze actualiseren correct toe",
        ],
        0,
        "Dat is net de valkuil bij actualiseren. Begrijpen is iets anders dan goedpraten.",
    ),
    tabel(
        "Evolutie of revolutie?",
        [
            ("De geleidelijke groei van het aantal vrouwen in het hoger onderwijs", "Evolutie"),
            ("De Oktoberrevolutie in Rusland", "Revolutie"),
            ("De trage ontzuiling vanaf de jaren zestig", "Evolutie"),
            ("De val van het oude regime in Frankrijk in enkele jaren tijd", "Revolutie"),
        ],
        "Een evolutie verloopt geleidelijk, een revolutie is een plotse en diepe omslag.",
        kolommen=["Evolutie", "Revolutie"],
    ),
    mk(
        "Een reiziger ontmoet in Parijs drie onvriendelijke kelners en schrijft: \"Parijzenaars zijn onvriendelijk.\" Wat doet hij?",
        [
            "Hij veralgemeent: enkele gevallen worden een regel",
            "Hij actualiseert: hij legt een verband tussen verleden en heden",
            "Hij gebruikt bewijs: drie kelners zijn genoeg voor een besluit",
            "Hij contextualiseert: hij begrijpt Parijs vanuit zijn tijd",
        ],
        0,
        "Drie gevallen worden een regel voor miljoenen mensen.",
    ),
    casus(
        "Oefenbron (verzonnen voorbeeld). Een Belgische reisgids uit 1925 schrijft over Congo: \"De inboorlingen zijn als kinderen: vrolijk, maar zonder plan voor morgen.\"",
        [
            mk(
                "Welke redeneerwijze pas je op deze zin toe?",
                ["Stereotypering analyseren", "Continuïteit benoemen", "Evolutie en revolutie benoemen", "Bewijs gebruiken"],
                0,
                "Een vast en vereenvoudigd beeld wordt aan een hele groep mensen toegeschreven.",
            ),
            tabel(
                "Mag je dit besluiten op basis van de zin?",
                [
                    ("De zin zegt veel over hoe men in België in 1925 over Congo dacht.", "Mag"),
                    ("De zin beschrijft hoe de Congolezen echt waren.", "Mag niet"),
                    ("De zin is waardeloos voor een historicus.", "Mag niet"),
                ],
                "Een slechte bron over Congo, maar een uitstekende over het denken van de maker en zijn publiek.",
                kolommen=["Mag", "Mag niet"],
            ),
            mk(
                "Welke vraag stel je als historicus het best bij deze zin?",
                [
                    "Wat zegt deze zin over de maker en zijn tijd?",
                    "Hoeveel kinderen woonden er in 1925 in Congo?",
                    "Was de schrijver van de reisgids zelf ooit een kind?",
                    "Welke reisgids verkocht in 1925 het best?",
                ],
                0,
                "Je vraagt wat de zin over de maker zegt.",
            ),
        ],
    ),
    mk(
        "Een leerling vergelijkt het oude Rome met België vandaag en besluit: \"Wij zijn gewoon beter.\" Wat is er mis?",
        [
            "Vergelijken dient om te begrijpen, niet om te rangschikken",
            "Je mag enkel samenlevingen uit dezelfde periode vergelijken",
            "Rome en België hebben helemaal niets met elkaar gemeen, dus vergelijken heeft geen zin",
            "Er is niets mis: een vergelijking moet altijd met een winnaar eindigen",
        ],
        0,
        "Je vergelijkt om elke samenleving beter te begrijpen, binnen een periode en tussen periodes.",
    ),
    sorteer(
        "In welke groep kenmerken hoort elk vergelijkingspunt?",
        ["Politiek", "Sociaal", "Cultureel", "Economisch"],
        [
            ["De staatsvorm: democratie of dictatuur", "Politiek"],
            ["Slavernij en onvrije arbeid", "Sociaal"],
            ["Levensbeschouwing", "Cultureel"],
            ["Handel en handelsnetwerken", "Economisch"],
            ["Migratie en wij-zij-denken", "Sociaal"],
            ["Propaganda", "Cultureel"],
        ],
        "Vier groepen kenmerken om samenlevingen te vergelijken.",
    ),
    mk(
        "Wat is het grootste verschil tussen het imperialisme van de vroegmoderne tijd en dat van de negentiende eeuw?",
        [
            "In de negentiende eeuw werd ook het binnenland bezet en bestuurd, eerder vooral de kust",
            "In de vroegmoderne tijd ging het om grondstoffen, later alleen om prestige",
            "In de negentiende eeuw speelde Europa geen rol meer in Afrika",
            "Er is geen verschil: de middelen en de motieven waren precies dezelfde",
        ],
        0,
        "De motieven leken op elkaar, de middelen verschilden enorm.",
    ),
    mk(
        "Hoe vergelijk je de staatsvorm onder Mao met China vandaag het best?",
        [
            "Politieke continuïteit met één partij, naast een grondig veranderde economie",
            "Volledige verandering: China werd een democratie met vrije verkiezingen",
            "Volledige continuïteit: zowel de politiek als de economie bleven gelijk",
            "Economische continuïteit, naast een totaal nieuwe politieke structuur",
        ],
        0,
        "In beide gevallen is één partij aan de macht, maar de economie verschilt grondig.",
    ),
    tabel(
        "Juist of fout? Samenlevingen vergelijken.",
        [
            ("In de negentiende eeuw bestonden een industrieel Engeland, een keizerlijk China en koloniale samenlevingen naast elkaar.", J),
            ("Slavernij kwam in maar één periode voor.", F),
            ("Slavernij nam in verschillende periodes een andere vorm aan.", J),
            ("Je vergelijkt enkel binnen eenzelfde periode, nooit tussen periodes.", F),
        ],
        "Je vergelijkt binnen en tussen periodes, van de prehistorie tot vandaag.",
    ),
    mk(
        "Elk jaar op 11 november staan dorpen aan hun oorlogsmonument stil bij hun gesneuvelden. Welk begrip past daarbij?",
        ["Een collectieve herinnering", "Een stereotypering", "Een veralgemening", "Een primaire bron"],
        0,
        "Een vaste dag, een monument en een gedeelde betekenis: het gedeelde beeld dat een groep bewaart en doorgeeft.",
    ),
    mk(
        "Hoe veranderde de herinnering aan de Holocaust na 1945?",
        [
            "Eerst over de oorlog in het algemeen, later kwam de genocide centraal",
            "Ze is sinds 1945 elk jaar op precies dezelfde manier herdacht",
            "Eerst stond de genocide centraal, later sprak men enkel nog over de oorlog",
            "Men herdenkt de Holocaust pas sinds de laatste ooggetuigen overleden zijn, rond het jaar 2000",
        ],
        0,
        "Pas vanaf de jaren zestig en zeventig kwam de genocide op de Joden centraal te staan.",
    ),
    tabel(
        "Wat droeg ertoe bij dat de herinnering aan de Holocaust veranderde?",
        [
            ("Overlevenden begonnen te spreken.", J),
            ("Er kwam historisch onderzoek.", J),
            ("De samenleving stelde andere vragen.", J),
            ("De kampen werden pas in de jaren zeventig ontdekt.", F),
        ],
        "Getuigen, onderzoek en nieuwe vragen veranderden de herinnering.",
    ),
    keuze(
        "De internationale herdenkingsdag van de Holocaust valt op [[*27 januari|8 mei|21 juli]].",
        "27 januari.",
    ),
    mk(
        "In een stad staat een standbeeld van een koloniale generaal. Voor sommige inwoners is hij een held, voor anderen een onderdrukker. Welke redeneerwijze helpt je dat te begrijpen?",
        ["Meerdere perspectieven hanteren", "Evolutie en revolutie benoemen", "Continuïteit benoemen", "Bewijs gebruiken"],
        0,
        "De betekenis die men aan een figuur geeft, kan van groep tot groep verschillen.",
    ),
    mk(
        "Een verkozen meerderheid wil een wet die een minderheid haar stemrecht afneemt. Waarom kan dat in een rechtsstaat niet?",
        [
            "Ook een meerderheid moet zich aan de wet en de grondrechten houden",
            "Een meerderheid mag in een democratie nooit wetten maken",
            "Alleen de koning mag over het stemrecht beslissen",
            "Het kan wel, als de meerderheid groot genoeg is",
        ],
        0,
        "Daarom spreekt men van een rechtsstaat, en niet enkel van een democratie.",
    ),
    tabel(
        "Is het een beperking van de democratische rechtsstaat in de praktijk?",
        [
            ("Niet iedereen wordt in de politiek even goed vertegenwoordigd.", J),
            ("Wie geld of een netwerk heeft, krijgt soms meer gehoor.", J),
            ("Trage procedures laten problemen soms lang aanslepen.", J),
            ("Burgers mogen kritiek geven op de regering.", F),
        ],
        "Kritiek op de regering is geen beperking. Waar die niet mag, is er geen rechtsstaat meer.",
    ),
    mk(
        "Hoe kan een democratie van binnenuit onder druk komen, zonder staatsgreep of oorlog?",
        [
            "Door de pers aan banden te leggen of rechters onder druk te zetten",
            "Door elk jaar opnieuw verkiezingen te organiseren voor alle niveaus",
            "Door burgers een petitie te laten tekenen",
            "Door het aantal gemeenten in het land te verminderen via fusies",
        ],
        0,
        "Wie de pers en de rechters controleert, kan de rechtsstaat uithollen zonder één schot te lossen.",
    ),
    tabel(
        "Is het een manier om zelf verantwoordelijkheid op te nemen in een democratische rechtsstaat?",
        [
            ("Gaan stemmen", J),
            ("Je informeren en je mening onderbouwd verdedigen", J),
            ("Naar een inspraakavond van je gemeente gaan", J),
            ("Nooit het nieuws volgen, want dat is toch allemaal hetzelfde", F),
        ],
        "Stemmen, je informeren en meedoen: ook een vereniging of een petitie horen erbij.",
    ),
    mk(
        "Op welke niveaus stem je, worden er regels gemaakt en kan je naar een rechter stappen?",
        [
            "Gemeente, deelstaten, federaal niveau en Europese Unie",
            "Enkel op het federale niveau, want de rest voert alleen uit",
            "Enkel op het niveau van de gemeente en de provincie",
            "Enkel op het niveau van de Europese Unie, sinds het Verdrag van Lissabon",
        ],
        0,
        "De rechtsstaat werkt op elk bestuursniveau.",
    ),
    mk(
        "Een leerling zegt: \"Geschiedenis is nutteloos, want ze kan de toekomst niet voorspellen.\" Wat is de beste reactie?",
        [
            "Voorspellen kan niet, maar je herkent processen die vandaag opnieuw spelen",
            "Geschiedenis kan de toekomst wel voorspellen, als je genoeg bronnen hebt",
            "De leerling heeft gelijk: het verleden heeft niets met vandaag te maken",
            "Geschiedenis is enkel nuttig om jaartallen te leren",
        ],
        0,
        "Hoe propaganda werkt, hoe een crisis een samenleving splijt, hoe rechten verworven en verloren raken: dat herken je.",
    ),
    open_(
        "Leg met een voorbeeld uit hoe kennis over propaganda uit de jaren dertig je kan helpen om vandaag het nieuws kritisch te lezen.",
        "Totalitaire regimes gebruikten affiches, film en radio om één beeld op te dringen en tegenspraak uit te schakelen, bijvoorbeeld de personencultus rond Stalin. Wie weet hoe dat werkte, herkent vandaag sneller berichten die één kant tonen, emoties bespelen of de maker verbergen. Je vraagt dan: wie maakte dit, voor wie en met welke bedoeling?",
    ),
]
