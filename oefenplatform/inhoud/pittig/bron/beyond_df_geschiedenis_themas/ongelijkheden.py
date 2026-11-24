"""Ongelijkheden: klassenmaatschappij en sociale strijd — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader (Beyond doorstroom).",
         vragen="klikvragen op 1893 en 1919 (stemrecht)"),
]

VRAGEN = [
    # --- standen en klassen
    tabel(
        "Standenmaatschappij of klassenmaatschappij?",
        [
            ("Je plaats ligt vast bij je geboorte.", "Standen"),
            ("Je plaats hangt af van je bezit en je positie in de productie.", "Klassen"),
            ("De adel heeft voorrechten bij de wet.", "Standen"),
            ("Voor de wet is iedereen gelijk, maar arm en rijk liggen ver uit elkaar.", "Klassen"),
        ],
        "In de standenmaatschappij beslist je geboorte, in de klassenmaatschappij je bezit.",
        kolommen=["Standen", "Klassen"],
    ),
    sorteer(
        "Tot welke klasse behoort elke persoon in de negentiende eeuw?",
        ["Grote burgerij", "Kleine burgerij", "Arbeidersklasse"],
        [
            ["een bankier in Brussel", "Grote burgerij"],
            ["de eigenaar van een spinnerij", "Grote burgerij"],
            ["een bakker met een eigen winkel", "Kleine burgerij"],
            ["een lagere bediende", "Kleine burgerij"],
            ["een mijnwerker in de Borinage", "Arbeidersklasse"],
            ["een dagloner", "Arbeidersklasse"],
        ],
        "De grote burgerij bezit kapitaal en productiemiddelen, de kleine burgerij wat bezit, de arbeiders enkel hun arbeidskracht.",
    ),
    mk(
        "Waarom had de grote burgerij in de negentiende eeuw niet alleen het geld, maar ook de politieke macht?",
        [
            "Het cijnskiesrecht gaf de stem aan wie belasting betaalde",
            "De grondwet gaf de adel alle zetels in het parlement van het land",
            "De koning koos zelf welke bankiers in het parlement zaten",
            "Arbeiders waren bij wet verplicht om op de burgerij te stemmen",
        ],
        0,
        "Wie rijk was, betaalde genoeg belasting om te mogen stemmen. Zo bleven geld en macht bij dezelfde groep.",
    ),
    inv(
        "Hoe noemde Marx de arbeidersklasse, die enkel haar arbeidskracht bezit?",
        ["het proletariaat", "proletariaat"],
        "Bij Marx heet de arbeidersklasse het proletariaat.",
    ),
    mk(
        "Een leerling zegt: \"In een klassenmaatschappij kan iedereen rijk worden, dus ongelijkheid is geen probleem.\" Wat is de beste reactie?",
        [
            "Opklimmen kan, maar voor wie arm is, blijft het moeilijk",
            "Dat klopt, want na 1830 was er in België geen armoede meer",
            "Dat klopt niet, want in een klassenmaatschappij beslist je geboorte",
            "Dat klopt, want elke arbeider kreeg na tien jaar een eigen fabriek",
        ],
        0,
        "Voor de wet is iedereen gelijk, maar slechts een enkeling klom op. De verschillen tussen arm en rijk bleven groot.",
    ),
    # --- sociale kwestie
    casus(
        "Lees de bron. Een onderzoeker schrijft in 1843: \"In deze spinnerij werken kinderen van negen jaar, twaalf uur per dag. De moeders werken mee aan de machines. Hun loon is laag, maar zonder dat geld kan het gezin de huur niet betalen.\"",
        [
            mk(
                "Wat kun je uit deze bron besluiten?",
                [
                    "Kinderarbeid was toen gewoon en toegelaten",
                    "Kinderarbeid was in 1843 al verboden, maar niemand hield zich eraan",
                    "Kinderen werkten enkel in de vakantie in de spinnerij",
                    "Kinderen kregen een hoger loon dan hun moeders",
                ],
                0,
                "Er bestond toen geen wet die kinderarbeid beperkte. De eerste wet kwam er pas in 1889.",
            ),
            mk(
                "Waarom lieten ouders hun kinderen zo werken?",
                [
                    "Het gezin had het loon nodig",
                    "De kinderen wilden liever werken dan naar school gaan",
                    "De wet verplichtte kinderen om vanaf negen jaar te werken",
                    "De fabrikant betaalde de kinderen meer dan de vaders",
                ],
                0,
                "Lonen waren laag. Zonder het loon van vrouwen en kinderen raakte het gezin niet rond.",
            ),
            tabel(
                "Welke gegevens uit de bron horen bij de sociale kwestie?",
                [
                    ("kinderen die twaalf uur werken", J),
                    ("een gezin dat de huur amper kan betalen", J),
                    ("een spinnerij die winst maakt voor de fabrikant", F),
                ],
                "De sociale kwestie is de vraag wat er met de armoede van de arbeiders moest gebeuren.",
            ),
        ],
    ),
    mk(
        "Waarom verzetten arbeiders zich tegen uitbetaling in natura?",
        [
            "Ze moesten alles in de duurdere fabriekswinkel kopen",
            "Ze kregen dan helemaal geen loon meer voor hun werk",
            "Ze moesten hun loon dan zelf ophalen in Brussel",
            "Ze kregen dan alleen nog groenten en geen brood",
        ],
        0,
        "Het loon kwam in bonnen voor de winkel van de fabriek, waar de prijzen hoger lagen. Een wet van 1887 verplichtte uitbetaling in geld.",
    ),
    tabel(
        "Een mijnwerker breekt in 1880 zijn been in de mijn. Wat gebeurt er waarschijnlijk?",
        [
            ("Hij krijgt geen loon zolang hij niet kan werken.", J),
            ("Een wettelijke verzekering betaalt zijn loon door.", F),
            ("Hij valt terug op familie, een ziekenkas of de armenzorg.", J),
            ("Het gezin kan op korte tijd tot de bedelstaf vervallen.", J),
        ],
        "Er was geen wettelijke bescherming. Een ongeval kon een gezin in één dag in armoede storten.",
    ),
    mk(
        "Waarom zegt men dat de fabriek de armoede zichtbaar maakte, maar niet nieuw?",
        [
            "Ook op het platteland was de armoede groot",
            "Voor 1800 bestond er in Europa helemaal geen armoede",
            "De fabrieken schaften de armoede op het platteland af",
            "De armoede bestond enkel in de grote steden van Engeland",
        ],
        0,
        "Denk aan de crisis in de Vlaamse vlasnijverheid rond 1845, met honger en tyfus op het platteland. In de stad zag je de armoede samengebald.",
    ),
    # --- arbeidersbeweging
    koppel(
        "Welk middel van de arbeidersbeweging hoort bij elke omschrijving?",
        [
            ["Samen het werk stilleggen om eisen af te dwingen", "Staking"],
            ["Samen geld opzijzetten voor slechte dagen", "Weerstandskas"],
            ["Een bakkerij die de arbeiders samen bezitten", "Coöperatie"],
            ["Een partij om de arbeiders in het parlement te vertegenwoordigen", "Belgische Werkliedenpartij"],
        ],
        ["Coalitieverbod", "Cijnskiesrecht"],
        "Staking, kas, coöperatie en partij waren middelen. Het coalitieverbod en het cijnskiesrecht waren net hindernissen.",
    ),
    mk(
        "Wat betekende het coalitieverbod concreet voor een arbeider in 1850?",
        [
            "Hij mocht zich niet met anderen verenigen om loon te eisen",
            "Hij mocht niet meer in een fabriek van een andere stad gaan werken",
            "Hij mocht geen lid worden van de katholieke kerk",
            "Hij mocht geen kinderen meer laten werken in de spinnerij",
        ],
        0,
        "Het verbod stond in de strafwet en werd pas in 1866 opgeheven.",
    ),
    keuze(
        "Het coalitieverbod stond in de strafwet. Je situeert het in het [[*politieke|culturele|economische]] domein, met gevolgen in het [[*sociale|religieuze|militaire]] domein.",
        "Een wet is politiek. Dat arbeiders zich niet mochten verenigen, raakte hun leven: dat is sociaal.",
    ),
    tabel(
        "Welke uitspraken over de arbeidersbeweging kloppen?",
        [
            ("Vooruit in Gent was een coöperatie.", J),
            ("Ook katholieken richtten arbeidersverenigingen op.", J),
            ("Uit de weerstandskassen groeiden de ziekenfondsen.", J),
            ("De beweging bestond enkel uit socialistische vakbonden.", F),
        ],
        "Naast vakbonden waren er kassen, coöperaties en een partij, en zowel socialisten als katholieken richtten verenigingen op.",
    ),
    mk(
        "Een thuiswever in 1800 kon moeilijk staken, een fabrieksarbeider in 1880 wel. Hoe verklaar je dat?",
        [
            "De fabriek bracht veel arbeiders met dezelfde belangen samen",
            "De stoommachine maakte het werk zo licht dat niemand nog moest werken",
            "De fabrikanten richtten zelf de eerste vakbonden op",
            "De industriële revolutie schafte het cijnskiesrecht af",
        ],
        0,
        "Wie thuis alleen weeft, staat alleen. Wie met duizend anderen in één zaal staat, kan samen handelen.",
    ),
    # --- wetten en stemrecht
    volgorde(
        "Zet in chronologische volgorde.",
        ["Het coalitieverbod wordt opgeheven", "De Belgische Werkliedenpartij wordt opgericht", "Stakingen en onlusten in Wallonië", "Loon moet in geld worden uitbetaald", "Een wet regelt de arbeid van vrouwen en kinderen"],
        "1866, 1885, 1886, 1887 en 1889.",
    ),
    mk(
        "Welk verband zie je tussen de onrust van 1886 en de wet van 1889?",
        [
            "Na stakingen en een onderzoek kwamen de eerste sociale wetten",
            "De wet van 1889 werd geschreven om de staking van 1886 te belonen",
            "De onrust van 1886 kwam er omdat de wet van 1889 te streng was",
            "Er is geen verband, want de wet regelde alleen de landbouw",
        ],
        0,
        "Het leger werd ingezet, er vielen doden, en daarna volgde een onderzoekscommissie. Zo kwamen de eerste sociale wetten er.",
    ),
    keuze(
        "De wet van 1889 bepaalde dat kinderen onder de [[*twaalf|achttien|zes]] jaar niet meer in de fabrieken mochten werken. Dat is meer dan [[*een halve eeuw|tien jaar|een eeuw]] na de onafhankelijkheid.",
        "Van 1830 tot 1889: bijna zestig jaar, en pas onder druk van stakingen en onrust.",
    ),
    mk(
        "Vakbonden en coöperaties hielpen, maar de arbeidersbeweging bleef vooral stemrecht eisen. Waarom?",
        [
            "Zonder stem konden de arbeiders geen sociale wetten laten stemmen",
            "Met stemrecht kregen de arbeiders meteen een hoger loon van de staat",
            "Het stemrecht verving het loon van de arbeiders",
            "Zonder stemrecht mochten de arbeiders geen staking houden",
        ],
        0,
        "Zolang alleen de burgerij stemde, kozen de verkozenen niet voor sociale wetten. Wie mee stemt, kan wetten afdwingen.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin een algemene staking het algemeen meervoudig stemrecht opleverde.",
        "tijdlijn-1750-2030.svg",
        [[46.5, 25, 6.2, 55]],
        "1893, net vóór het streepje van 1900.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Belgische mannen voor het eerst met één stem per man kozen.",
        "tijdlijn-1750-2030.svg",
        [[54.6, 25, 6.2, 55]],
        "1919, vlak na de Eerste Wereldoorlog.",
    ),
    casus(
        "Onder het algemeen meervoudig stemrecht stemmen drie mannen. Jef is mijnwerker en ongehuwd. Louis is getrouwd, heeft kinderen en een huis. Paul heeft een universitair diploma en bezit veel grond.",
        [
            tabel(
                "Wat klopt over hun stemmen?",
                [
                    ("Jef heeft één stem.", J),
                    ("Louis kan een extra stem krijgen.", J),
                    ("Paul heeft evenveel stemmen als Jef.", F),
                ],
                "Elke man stemt, maar bezit, diploma of gezin gaven één of twee stemmen extra.",
            ),
            mk(
                "Waarom was de arbeidersbeweging niet tevreden met dit stemrecht?",
                [
                    "Niet elke stem had hetzelfde gewicht",
                    "Arbeiders mochten nog altijd helemaal niet stemmen",
                    "Alleen vrouwen kregen extra stemmen",
                    "De mijnwerkers kregen meer stemmen dan de rijken",
                ],
                0,
                "De rijken hadden meer stemmen. De eis bleef: één man, één stem. Dat kwam er in 1919.",
            ),
        ],
    ),
    tabel(
        "Welke uitspraken over het stemrecht in België kloppen?",
        [
            ("In 1893 kwam er nog geen één stem per man.", J),
            ("Vrouwen mochten pas in 1948 voor het parlement stemmen.", J),
            ("Vrouwen mochten voor de gemeente eerder stemmen dan voor het parlement.", J),
            ("In 1919 mochten ook de vrouwen voor het parlement stemmen.", F),
        ],
        "1893 meervoudig, 1919 enkelvoudig voor mannen, 1948 voor vrouwen in het parlement.",
    ),
    sleep(
        "In 1900 bestond de sociale zekerheid zoals wij die kennen nog [[niet]]. Ze werd opgebouwd vanaf [[1944]]. Vakantie en een minimumloon zijn verworvenheden van de [[twintigste]] eeuw.",
        ["volledig", "1831", "achttiende"],
        "Rond 1900 waren er pas de eerste sociale wetten. De sociale zekerheid kwam na de Tweede Wereldoorlog.",
    ),
    mk(
        "Je leest een pamflet uit 1890: \"Eén man, één stem! Tien uur werken is genoeg!\" Van wie komt het waarschijnlijk?",
        [
            "Van de arbeidersbeweging",
            "Van de grote burgerij die het cijnskiesrecht verdedigt",
            "Van de fabrikanten die lange werkdagen nodig hebben",
            "Van de vorsten van de Heilige Alliantie",
        ],
        0,
        "Gelijk stemrecht en een kortere werkdag waren eisen van de arbeiders.",
    ),
    open_(
        "Leg uit hoe de arbeiders in België hun situatie verbeterden tussen 1866 en 1919. Gebruik minstens drie middelen of stappen.",
        "Na de opheffing van het coalitieverbod in 1866 konden ze zich verenigen in vakbonden, weerstandskassen en coöperaties. In 1885 kwam de Belgische Werkliedenpartij. Na de stakingen van 1886 kwamen de eerste sociale wetten, zoals de wet van 1889 op vrouwen- en kinderarbeid. De algemene staking van 1893 bracht het meervoudig stemrecht, en in 1919 kwam er één stem per man.",
    ),
    open_(
        "Waarom kwamen de eerste sociale wetten in België pas meer dan een halve eeuw na de onafhankelijkheid?",
        "Door het cijnskiesrecht had alleen de rijke burgerij politieke macht, en die volgde het economisch liberalisme: de staat moest zich niet met lonen en werk bemoeien. De arbeiders mochten zich tot 1866 niet eens verenigen. Pas onder druk van stakingen en onrust, zoals in 1886, kwamen er wetten.",
    ),
    mk(
        "Waarom werkten vrouwen en kinderen in de fabrieken en mijnen, en niet enkel de vaders?",
        [
            "Hun loon was lager en het gezin had dat geld nodig",
            "De wet verbood mannen om meer dan acht uur per dag te werken",
            "Vrouwen en kinderen waren sterker dan mannen voor het mijnwerk",
            "De vaders werkten allemaal als bankier of grote handelaar",
        ],
        0,
        "Voor de fabrikant waren vrouwen en kinderen goedkoop. Voor het gezin was elk loon nodig om rond te komen.",
    ),
]
