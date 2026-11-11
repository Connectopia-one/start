"""België na 1945 — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="volksraadpleging-1950.svg", zelf=True,
         wat="Staafdiagram met het percentage ja-stemmen in België, Vlaanderen en Wallonië (afgerond zoals in de leerbundel).",
         vragen="tabel en klikvraag over de volksraadpleging"),
]

VRAGEN = [
    mk(
        "Wat legde het sociaal pact van 1944 vast, naast de grondslagen van een verplichte sociale zekerheid?",
        [
            "Het overleg tussen werkgevers en vakbonden",
            "Het algemeen stemrecht voor vrouwen bij alle verkiezingen",
            "De splitsing van de nationale partijen",
            "De financiering van het vrije onderwijs",
        ],
        0,
        "Werkgevers en vakbonden spraken samen de sociale zekerheid af, en ook dat ze blijvend met elkaar zouden overleggen. Dat model bestaat nog.",
    ),
    tabel(
        "Hoort het bij de takken van de sociale zekerheid?",
        [
            ("De terugbetaling van geneeskundige zorg", J),
            ("Een uitkering voor wie zijn werk verliest", J),
            ("Het wettelijk pensioen", J),
            ("Een gratis woning voor elk gezin", F),
        ],
        "Ziekteverzekering, werkloosheid, pensioen en kinderbijslag horen erbij. Een gratis woning niet.",
    ),
    mk(
        "Hoe wordt de sociale zekerheid vooral betaald?",
        [
            "Met bijdragen op het loon, aangevuld uit de belastingen",
            "Volledig met geld dat de Europese Unie elk jaar aan België overmaakt",
            "Met de winst van staatsbedrijven, zonder bijdragen van werkenden",
            "Met vrijwillige giften van burgers en verenigingen aan de ziekenfondsen",
        ],
        0,
        "Wie werkt en wie werk geeft, draagt bij. De algemene belastingen vullen aan.",
    ),
    sorteer(
        "Past het bij de klassieke verzorgingsstaat of bij het nieuwe idee van de actieve welvaartsstaat?",
        ["Verzorgingsstaat", "Actieve welvaartsstaat"],
        [
            ["Bestaanszekerheid bij ziekte, werkloosheid en ouderdom", "Verzorgingsstaat"],
            ["Een opleiding om opnieuw aan het werk te raken", "Actieve welvaartsstaat"],
            ["Begeleiding naar een nieuwe job", "Actieve welvaartsstaat"],
            ["Kinderopvang zodat ouders kunnen werken", "Actieve welvaartsstaat"],
        ],
        "De actieve welvaartsstaat verschuift de nadruk van uitkeren naar mensen opnieuw aan het werk helpen.",
    ),
    koppel(
        "Welke breuklijn hoort bij elke tegenstelling?",
        [
            ["Gelovig tegenover vrijzinnig", "Levensbeschouwelijke breuklijn"],
            ["Arbeid tegenover kapitaal", "Sociaaleconomische breuklijn"],
            ["Vlamingen tegenover Franstaligen", "Communautaire breuklijn"],
        ],
        ["Koude Oorlog"],
        "Drie breuklijnen lopen door de Belgische samenleving.",
    ),
    tabel(
        "Op welke breuklijn situeer je elk debat?",
        [
            ("Hoeveel moeten de hoogste inkomens bijdragen?", "Sociaaleconomisch"),
            ("Moet Vlaanderen meer bevoegdheden krijgen?", "Communautair"),
            ("Moeten de uitkeringen omhoog en de werkweek korter?", "Sociaaleconomisch"),
        ],
        "Inkomens en uitkeringen gaan over arbeid en kapitaal. Bevoegdheden gaan over de gemeenschappen.",
        kolommen=["Levensbeschouwelijk", "Sociaaleconomisch", "Communautair"],
    ),
    keuze(
        "Het schoolpact regelde de financiering van zowel het [[*vrije|private|buitenlandse]] als het officiële onderwijs, en garandeerde de vrije [[*schoolkeuze|lesinhoud|studiekeuze]].",
        "Twee netten met overheidsgeld, en ouders kiezen zelf de school.",
    ),
    mk(
        "Een krant uit 1946 schrijft over de kwestie die het land verdeelt. Waarover ging die koningskwestie?",
        [
            "Of Leopold III na de oorlog terug koning mocht worden",
            "Of België na de oorlog een republiek zou worden",
            "Wie na de dood van Leopold III de troon zou erven",
            "Of de koning na de oorlog nog alleen mocht beslissen over de kolonie Congo",
        ],
        0,
        "Leopold III was tijdens de oorlog in het bezette land gebleven. Na de oorlog was de vraag of hij mocht terugkeren.",
    ),
    met_prent("volksraadpleging-1950.svg", tabel(
        "Bekijk de uitslag van de volksraadpleging van 1950. Welke uitspraken kan je staven?",
        [
            ("In het hele land stemde een meerderheid ja.", J),
            ("In Wallonië stemde een meerderheid ja.", F),
            ("Het verschil tussen Vlaanderen en Wallonië was groot.", J),
            ("Elk landsdeel stemde ongeveer hetzelfde.", F),
        ],
        "Bijna 58 % ja in het hele land, maar ruim 70 % in Vlaanderen tegenover amper 4 op 10 in Wallonië.",
    )),
    klik(
        "Klik in de grafiek op het landsdeel waar de meerderheid neen stemde.",
        "volksraadpleging-1950.svg",
        [[71.2, 12, 17.5, 84]],
        "Wallonië, met amper 4 op 10 ja-stemmen: onder de stippellijn van 50 %.",
    ),
    mk(
        "Hoe eindigde de koningskwestie uiteindelijk?",
        [
            "Na stakingen en doden deed de koning troonsafstand voor zijn zoon",
            "De koning keerde terug en bleef daarna nog twintig jaar zonder enig protest regeren",
            "Het parlement schafte de monarchie af, en België werd voortaan een republiek met een president",
            "Een tweede volksraadpleging gaf Wallonië een eigen koning",
        ],
        0,
        "In Grâce-Berleur vielen drie doden. Leopold III deed troonsafstand en Boudewijn werd koning.",
    ),
    tabel(
        "Welke gevolgen had Leuven Vlaams in 1968?",
        [
            ("De regering van dat ogenblik viel over de kwestie.", J),
            ("De grote nationale partijen splitsten in een Vlaamse en een Franstalige.", J),
            ("De communautaire breuklijn werd de belangrijkste van de drie.", J),
            ("De universiteit bleef tweetalig op dezelfde plek.", F),
        ],
        "Een universiteitskwestie werd een politieke aardbeving. De Franstalige afdeling moest weg uit Vlaams gebied.",
    ),
    inv(
        "Hoe heet de nieuwe stad die de Franstalige universiteit na Leuven Vlaams bouwde?",
        "Louvain-la-Neuve",
        "Louvain-la-Neuve, in Waals-Brabant.",
    ),
    mk(
        "Een historicus beschrijft het naoorlogse België als een verzuild land. Wat bedoelt hij?",
        [
            "Groepen hebben elk hun eigen scholen, ziekenfondsen en verenigingen",
            "Het land wordt verdeeld in gewesten met elk een eigen parlement en een eigen regering",
            "De kerk en de staat worden volledig en voorgoed van elkaar gescheiden in de grondwet",
            "Elke partij moet een eigen krant hebben om te mogen opkomen",
        ],
        0,
        "Van de wieg tot het graf kon je binnen je eigen groep blijven.",
    ),
    sleep(
        "België kende drie zuilen: de katholieke, de [[socialistische]] en de [[liberale]] zuil, elk met een volledig netwerk van eigen organisaties.",
        ["communistische", "Vlaamse"],
        "Drie zuilen, elk met een volledig netwerk van organisaties.",
    ),
    tabel(
        "Was het een oorzaak van de ontzuiling vanaf de jaren zestig?",
        [
            ("De kerk verloor greep op het leven van de mensen.", J),
            ("Mensen gingen vrijer en individueler kiezen.", J),
            ("Onderwijs en televisie keken buiten de eigen groep.", J),
            ("Een wet verbood in 1960 alle zuilorganisaties.", F),
        ],
        "Secularisering, individualisering, en onderwijs en televisie. Er kwam geen verbod.",
    ),
    mk(
        "Een leerling zegt: \"Er was nooit ontzuiling, want ziekenfondsen en vakbonden tellen nog miljoenen leden.\" Wat is de beste reactie?",
        [
            "De organisaties bestaan nog, maar je blijft niet meer vanzelfsprekend in één zuil",
            "De leerling heeft gelijk: de verzuiling is sinds de jaren zestig alleen maar sterker geworden",
            "De ziekenfondsen en vakbonden zijn in de jaren zestig allemaal opgeheven",
            "Ontzuiling betekent dat de organisaties ophouden te bestaan, dus de leerling heeft gelijk",
        ],
        0,
        "De verzuiling werd zwakker. Wat verdween, is de vanzelfsprekendheid, niet de organisaties.",
    ),
    mk(
        "Een land heeft een parlement voor het hele land, maar ook deelstaten met hun eigen parlement en eigen bevoegdheden, waar het centrale gezag niet zomaar over beslist. Hoe noem je zo'n staat?",
        ["Een federale staat", "Een unitaire staat", "Een verzuilde staat", "Een verzorgingsstaat"],
        0,
        "In een federale staat zijn de bevoegdheden verdeeld over verschillende zelfstandige niveaus.",
    ),
    volgorde(
        "Zet deze gebeurtenissen uit de Belgische naoorlogse geschiedenis in de juiste volgorde.",
        ["De volksraadpleging over de koningskwestie", "Het schoolpact", "Leuven Vlaams", "De eerste staatshervorming", "De zesde staatshervorming"],
        "Eerst de koningskwestie, dan de schoolstrijd die met een pact eindigde, dan Leuven, en daarna de staatshervormingen.",
    ),
    tabel(
        "Welke veranderingen horen bij de zesde staatshervorming, van 2011 tot 2014?",
        [
            ("De overheveling van de kinderbijslag", J),
            ("De overheveling van delen van het arbeidsmarktbeleid", J),
            ("De splitsing van Brussel-Halle-Vilvoorde", J),
            ("De afschaffing van de provincies", F),
        ],
        "Kinderbijslag, delen van het arbeidsmarktbeleid en de splitsing van BHV. De provincies bleven bestaan.",
    ),
    sorteer(
        "Is het een bevoegdheid van een gemeenschap, van een gewest, of is ze federaal gebleven?",
        ["Gemeenschap", "Gewest", "Federaal"],
        [
            ["Onderwijs", "Gemeenschap"],
            ["Cultuur", "Gemeenschap"],
            ["Ruimtelijke ordening en vergunningen", "Gewest"],
            ["Leefmilieu, water en afval", "Gewest"],
            ["Het leger", "Federaal"],
            ["Justitie", "Federaal"],
        ],
        "Gemeenschappen gaan over personen, gewesten over het grondgebied. Leger en justitie bleven federaal.",
    ),
    keuze(
        "België telt [[*drie|twee|vier]] gewesten. In Vlaanderen werden het gewest en de gemeenschap [[*samengevoegd|gesplitst|afgeschaft]] tot één parlement en één regering. De Franstaligen deden dat [[*niet|ook|eerder]].",
        "Drie gewesten en drie gemeenschappen. Vlaanderen voegde samen, de Franstaligen niet.",
    ),
    inv(
        "Hoe heet een wet die het Vlaams Parlement goedkeurt? (één woord)",
        "decreet",
        "Een decreet.",
    ),
    mk(
        "Het Vlaams Parlement keurt een regeling goed over onderwijs. De federale regering is het er niet mee eens. Wat kan ze doen?",
        [
            "Niets zomaar: de regeling heeft dezelfde kracht als een federale wet",
            "Ze kan de regeling met een eenvoudige beslissing van de ministers vernietigen",
            "Ze vraagt de koning om de regeling te weigeren, en dan vervalt ze",
            "Ze kan de regeling vervangen door een federale wet, want een federale wet gaat altijd voor",
        ],
        0,
        "Deelstaten en federale overheid staan naast elkaar, niet boven elkaar.",
    ),
    volgorde(
        "Zet de bestuursniveaus die over het leven van een inwoner van Vlaanderen beslissen in volgorde, van het kleinste naar het grootste gebied.",
        ["De gemeente", "De provincie", "Het Vlaams Gewest en de Vlaamse Gemeenschap", "De federale overheid", "De Europese Unie"],
        "Van dichtbij naar ver weg: zes niveaus beslissen mee.",
    ),
    tabel(
        "Hoort het bij de principes van een democratische rechtsstaat?",
        [
            ("De scheiding van de wetgevende, de uitvoerende en de rechterlijke macht", J),
            ("Vrije en geheime verkiezingen waaraan iedereen mag deelnemen", J),
            ("Grondrechten die ook de overheid zelf moet naleven", J),
            ("Een regering die de rechters benoemt en ontslaat wanneer ze wil", F),
        ],
        "Machtenscheiding, vrije verkiezingen en grondrechten voor iedereen, ook tegenover de overheid.",
    ),
    casus(
        "Een partijprogramma bevat drie standpunten. Eén: Vlaanderen moet zijn arbeidsmarkt volledig zelf regelen. Twee: de hoogste inkomens moeten meer bijdragen. Drie: elke school moet lessen levensbeschouwing blijven aanbieden.",
        [
            tabel(
                "Op welke breuklijn ligt elk standpunt?",
                [
                    ("Standpunt een", "Communautair"),
                    ("Standpunt twee", "Sociaaleconomisch"),
                    ("Standpunt drie", "Levensbeschouwelijk"),
                ],
                "Bevoegdheden, inkomens en levensbeschouwing: drie breuklijnen in één programma.",
                kolommen=["Levensbeschouwelijk", "Sociaaleconomisch", "Communautair"],
            ),
            mk(
                "Welke les trek je hieruit voor het lezen van een partijprogramma?",
                [
                    "Je plaatst elk standpunt apart, niet de partij als geheel",
                    "Een partij hoort altijd bij precies één breuklijn",
                    "Een programma met standpunten op drie breuklijnen is tegenstrijdig en dus onbruikbaar",
                    "Enkel het eerste standpunt telt mee om de partij te plaatsen",
                ],
                0,
                "Een programma kan op meer dan één breuklijn tegelijk standpunten bevatten.",
            ),
            mk(
                "Een kiezer in Gent vindt een Franstalige partij met dit programma sympathiek. Kan hij op die partij stemmen?",
                [
                    "Nee, dat kan enkel in de kieskring Brussel",
                    "Ja, elke Belg kan overal op elke partij stemmen",
                    "Ja, maar alleen bij de Europese verkiezingen, en dan enkel als hij in Wallonië stemt",
                    "Nee, want Franstalige partijen nemen enkel aan gemeenteraadsverkiezingen deel",
                ],
                0,
                "Na de splitsing van de nationale partijen kies je in Vlaanderen tussen Vlaamse partijen. Brussel is de uitzondering.",
            ),
        ],
    ),
    open_(
        "Leg uit waarom België sinds 1970 telkens opnieuw een staatshervorming doorvoerde.",
        "De staatshervormingen zijn vooral antwoorden op de communautaire breuklijn tussen Vlamingen en Franstaligen. Telkens de spanning te hoog opliep, kwam er een nieuwe ronde, en zo groeide België van een unitaire naar een federale staat.",
    ),
]
