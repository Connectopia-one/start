"""Beeldvorming en het verleden vandaag — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, MAP, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

TL = "tijdlijn-1000-1500.svg"

PRENTEN = [
    dict(bestand="standbeeld.svg", zelf=True,
         wat="Een bedacht standbeeld: figuur A groot op een sokkel met opgestoken arm, figuren B en C klein en geknield aan de voet.",
         vragen="klikvraag en tabelvraag over beeldvorming in een standbeeld"),
    dict(bestand=TL, zelf=True,
         wat="Tijdlijn van 1000 tot 1500 (dezelfde als bij Standen, domein en stad).",
         vragen="klikvraag: inname van Jeruzalem"),
    dict(bestand="karel-de-grote-durer.webp", zelf=False,
         wat="Het portret van Karel de Grote door Albrecht Dürer (rond 1512), met kroon, zwaard en rijksappel.",
         waar="Wikimedia Commons, zoek op 'Albrecht Dürer Emperor Charlemagne' (publiek domein).",
         vragen="meerkeuzevraag: wat leer je uit een portret dat 700 jaar later gemaakt is"),
    dict(bestand="guldensporenslag-de-keyser.webp", zelf=False,
         wat="Het grote schilderij van de Guldensporenslag door Nicaise De Keyser (1836).",
         waar="Wikimedia Commons, zoek op 'Nicaise de Keyser Battle of the Golden Spurs' (publiek domein).",
         vragen="meerkeuzevraag: wat toont een 19de-eeuws schilderij van 1302"),
]

VRAGEN = [
    # --- wat beeldvorming is
    mk(
        "Wat bedoelen we met historische beeldvorming?",
        [
            "Een beeld van het verleden, opgebouwd uit bronnen",
            "Een volledige en vaststaande weergave van alles wat ooit gebeurd is",
            "De verzameling van alle schilderijen en standbeelden over vroeger",
            "Een verhaal over vroeger dat een schrijver zonder bronnen verzint",
        ],
        0,
        "Wij hebben het verleden zelf niet meer, wel bronnen. Wat iemand daaruit opbouwt, is een beeld.",
    ),
    sleep(
        "Een beeld van het verleden is altijd een [[constructie]]. Wie het maakt, [[selecteert]] bronnen, leidt er informatie uit af, [[interpreteert]] en zoekt [[samenhang]].",
        ["kopie", "vergeet", "toeval"],
        "Kiezen, afleiden, interpreteren en samenhang zoeken: elke stap is een keuze van de maker.",
    ),
    tabel(
        "Klopt elke uitspraak over hoe een beeld van het verleden tot stand komt?",
        [
            ("Wat er destijds gebeurde, ligt vast.", J),
            ("Wat er destijds gebeurde, is volledig kenbaar.", F),
            ("Een pas ontdekte bron kan het beeld veranderen.", J),
            ("Nieuwe vragen aan oude bronnen kunnen het beeld veranderen.", J),
            ("Een beeld dat later verandert, was vroeger dus een leugen.", F),
        ],
        "De gebeurtenis zelf ligt vast, maar we kennen ze nooit helemaal. Nieuwe bronnen en nieuwe vragen schuiven het beeld op, zonder dat het oude beeld bewust gelogen was.",
    ),
    mk(
        "Twee historici schrijven over dezelfde opstand en komen tot een ander beeld. Wat is de meest waarschijnlijke verklaring?",
        [
            "Ze gebruikten andere bronnen of stelden andere vragen",
            "Een van beiden heeft zeker slordig gewerkt en moet zijn boek intrekken",
            "Het verleden zelf verandert telkens als er een nieuw boek over verschijnt",
            "Historici kiezen hun besluit vooraf en zoeken er pas daarna bronnen bij",
        ],
        0,
        "Een verschil is normaal. Pas als een beeld de bronnen tegenspreekt, is er een echt probleem.",
    ),
    # --- standplaatsgebondenheid
    sorteer(
        "Gaat het hier om de persoonlijke of de maatschappelijke context van wie een beeld maakt?",
        ["Persoonlijk", "Maatschappelijk"],
        [
            ["de afkomst van de maker", "Persoonlijk"],
            ["het geloof van de maker", "Persoonlijk"],
            ["het beroep van de maker", "Persoonlijk"],
            ["het land is in oorlog", "Maatschappelijk"],
            ["wie het geld voor het onderzoek geeft", "Maatschappelijk"],
            ["het jaar waarin een schoolboek gedrukt wordt", "Maatschappelijk"],
        ],
        "Afkomst, geloof en beroep horen bij de maker zelf. Oorlog, geldschieters en de tijd waarin een boek verschijnt, horen bij de samenleving rond die maker.",
    ),
    casus(
        "In 1099 nemen de kruisvaarders Jeruzalem in. Daarover bestaan Arabische kronieken en westerse (Latijnse) kronieken. Ze vertellen allebei over het bloedbad dat volgde.",
        [
            mk(
                "Welk beeld van de Franken geven de Arabische bronnen?",
                [
                    "Ruwe, gewelddadige indringers van ver weg",
                    "Beschaafde bevrijders die door God gestuurd waren",
                    "Vredige handelaars die kwamen om specerijen te kopen",
                    "Ongewapende pelgrims die de weg kwijt waren",
                ],
                0,
                "Voor wie in de stad woonde, waren de Franken vreemde, wrede veroveraars.",
            ),
            mk(
                "Hoe vertellen westerse kronieken hetzelfde bloedbad?",
                [
                    "Als een door God gewild succes",
                    "Als een schandaal waarvoor de paus zich later verontschuldigde",
                    "Als een ongeluk waar niemand echt schuld aan had",
                    "Ze zwijgen er helemaal over, alsof het nooit gebeurd is",
                ],
                0,
                "Hetzelfde geweld wordt aan de westerse kant een overwinning van het geloof.",
            ),
            mk(
                "Waarom verschillen die twee soorten bronnen vooral?",
                [
                    "Hun makers stonden aan een andere kant",
                    "De Arabische schrijvers waren er niet bij en verzonnen alles",
                    "Latijnse teksten zijn moeilijk en werden later slecht vertaald",
                    "De ene groep schreef op perkament, de andere op papier",
                ],
                0,
                "Standplaatsgebondenheid: wie aan een andere kant staat, ziet dezelfde gebeurtenis anders.",
            ),
        ],
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de kruisvaarders Jeruzalem innemen.",
        TL, [[20.7, 25, 3.5, 55]],
        "Jeruzalem werd ingenomen in 1099, tijdens de eerste kruistocht.",
    ),
    koppel(
        "Karel de Grote kreeg in de loop van de tijd verschillende beelden. Welk beeld hoort bij welke blik?",
        [
            ["wie kijkt naar wat landen vandaag samenbrengt", "vader van Europa"],
            ["wie kijkt naar zijn oorlogen tegen Saksen en Longobarden", "Frankische veroveraar"],
            ["wie kijkt vanuit de oostelijke helft van zijn rijk, later een eigen land", "Duits keizer"],
        ],
        ["Romeins senator"],
        "De vraag die je stelt, bepaalt het antwoord. Frankrijk en Duitsland claimden hem allebei, en na 1945 werd hij het symbool van Europese eenheid.",
    ),
    met_prent(
        "karel-de-grote-durer.webp",
        mk(
            "Dit portret van Karel de Grote werd rond 1512 geschilderd voor de stad Neurenberg, zo'n 700 jaar na zijn dood. Wat leer je er vooral uit?",
            [
                "Hoe men hem rond 1500 wilde zien",
                "Hoe Karel er echt uitzag, want de schilder kende oude portretten van hem",
                "Welke kleren en wapens de Franken rond het jaar 800 echt droegen",
                "Dat Karel de Grote zelf in Neurenberg geboren en begraven werd",
            ],
            0,
            "De schilder heeft Karel nooit gezien. Het portret toont vooral hoe een Duitse stad rond 1500 een machtige keizer wilde voorstellen.",
        ),
    ),
    tabel(
        "Je krijgt een beeld van het verleden voorgeschoteld, bijvoorbeeld in een documentaire. Is dit een nuttige vraag om te stellen?",
        [
            ("Wie maakte dit, en wanneer?", J),
            ("Op welke bronnen steunt het?", J),
            ("Wat wordt er niet verteld?", J),
            ("Wie gaf de opdracht?", J),
            ("Hoeveel kijkers heeft het gehad?", F),
        ],
        "Wie, wanneer, welke bronnen, wat ontbreekt en wie betaalde: zo zie je de keuzes achter het beeld. Hoe populair iets is, zegt niets over hoe juist het is.",
    ),
    mk(
        "Waarom is het nuttig te weten wie de opdracht gaf voor een beeld van het verleden?",
        [
            "De opdrachtgever bepaalt vaak mee wat verteld en verzwegen wordt",
            "Je kan de opdrachtgever dan zelf vragen of alles in het werk echt klopt",
            "Een werk zonder bekende opdrachtgever mag je nooit als bron gebruiken",
            "De opdrachtgever was meestal ook zelf de schilder of de schrijver van het werk",
        ],
        0,
        "Wie betaalt, wil vaak een bepaald beeld. Daarom weeg je een werk af tegen de belangen van wie het bestelde.",
    ),
    mk(
        "Iemand zegt: 'De middeleeuwer geloofde dat de aarde plat was.' Wat is daar vooral mis mee?",
        [
            "Het is een veralgemening die niet klopt",
            "Niets, dat staat zo in elke middeleeuwse kroniek en elk kloosterboek",
            "Het woord aarde bestond in de middeleeuwen nog niet, dus het is een anachronisme",
            "Het klopt voor de boeren, maar niet voor de geleerden in de kloosters",
        ],
        0,
        "Geleerden wisten in de middeleeuwen dat de aarde rond is. De uitspraak steunt niet op bronnen en wordt toch voortdurend herhaald.",
    ),
    mk(
        "Je komt in een oude bron een stereotype tegen over een volk. Wat doe je ermee?",
        [
            "Je benoemt het en analyseert het",
            "Je neemt het over, want de maker leefde toen en wist het dus beter",
            "Je schrapt de hele bron uit je onderzoek, want ze is onbruikbaar",
            "Je past de tekst van de bron aan zodat het stereotype verdwijnt",
        ],
        0,
        "Ook een stereotype vertelt iets: over hoe de maker naar die groep keek. Je neemt het alleen niet over als feit.",
    ),
    klik(
        "Ook een standbeeld doet aan beeldvorming. Klik op de figuur die de maker het belangrijkst wilde laten lijken.",
        "standbeeld.svg", [[38.0, 5.0, 30.0, 55.0]],
        "Figuur A staat hoog, is groot en heeft een krachtig gebaar. Hoe groot iemand is en waar hij staat, is een keuze van de maker.",
    ),
    dict(**tabel(
        "Bekijk het standbeeld opnieuw. Klopt elke uitspraak?",
        [
            ("De kleine, knielende figuren lijken ondergeschikt.", J),
            ("Het beeld toont neutraal hoe het er echt aan toe ging.", F),
            ("Het helpt te weten wie het beeld bestelde en wanneer.", J),
            ("Houding en grootte zijn keuzes van de maker.", J),
        ],
        "Een standbeeld is geen foto. Grootte, houding en plaats vertellen wie de maker belangrijk vond.",
    ), afbeelding_url=f"{MAP}/standbeeld.svg"),
    # --- verleden, heden, toekomst
    met_prent(
        "guldensporenslag-de-keyser.webp",
        mk(
            "Dit grote schilderij van de Guldensporenslag (1302) werd gemaakt in 1836. Wat toont het vooral?",
            [
                "Hoe men 1302 vijf eeuwen later wilde zien",
                "Een betrouwbaar ooggetuigenverslag van wie er in 1302 meevocht",
                "Hoe de Franse ridders hun eigen nederlaag later herdachten",
                "Welke wapens en kleren de Vlamingen op het slagveld droegen",
            ],
            0,
            "De schilder leefde vijf eeuwen later, in een jong België dat een eigen verleden zocht. Het schilderij is een bron over 1836, meer dan over 1302.",
        ),
    ),
    sleep(
        "Vlaamsgezinden geven de Guldensporenslag de betekenis van een Vlaamse overwinning op een [[vreemde overheerser]]. Die betekenis kreeg de slag pas in de [[19de]] eeuw. Voor de tijdgenoten was het vooral een [[sociale en politieke]] strijd.",
        ["godsdienstige", "14de", "naburige bondgenoot"],
        "De taalkundige en nationale betekenis komt er vijfhonderd jaar later bij. In 1302 ging het om ambachten, graaf en koning.",
    ),
    inv(
        "Op welke dag valt de feestdag van de Vlaamse Gemeenschap? Schrijf de dag en de maand.",
        ["11 juli", "elf juli"],
        "Op 11 juli, naar de Guldensporenslag van 11 juli 1302. Die keuze werd pas in de 20ste eeuw gemaakt.",
    ),
    mk(
        "Wat bedoelen we als we zeggen dat een herdenking iets vertelt over het heden?",
        [
            "Wat men herdenkt en hoe, hangt af van wat men nu belangrijk vindt",
            "Een herdenking vertelt precies hoe de gebeurtenis zelf verlopen is",
            "Herdenkingen gaan alleen over gebeurtenissen van de laatste tien jaar",
            "Een herdenking verandert nooit, want de datum van de gebeurtenis ligt vast",
        ],
        0,
        "Dat de Vlaamse feestdag pas in de 20ste eeuw gekozen werd, zegt iets over die 20ste eeuw.",
    ),
    tabel(
        "Klopt elke uitspraak over de lagen van identiteit?",
        [
            ("Je kan je tegelijk Vlaams en Belgisch voelen.", J),
            ("Je levensbeschouwing is ook een laag van je identiteit.", J),
            ("Je sociaaleconomische positie speelt mee in wie je bent.", J),
            ("Wie zich westers voelt, kan geen andere laag hebben.", F),
            ("Een mens moet uiteindelijk kiezen voor één laag.", F),
        ],
        "Vlaams, Belgisch, westers of niet-westers, sociaaleconomisch, levensbeschouwelijk: die lagen sluiten elkaar niet uit.",
    ),
    mk(
        "Waarom beoordeel je het verleden niet met de maatstaf van vandaag?",
        [
            "Dan begrijp je niet waarom iets toen vanzelfsprekend leek",
            "Omdat alles wat mensen vroeger deden, in hun tijd ook goed was",
            "Omdat begrijpen en goedkeuren eigenlijk hetzelfde zijn",
            "Omdat mensen van vroeger geen eigen waarden of regels hadden",
        ],
        0,
        "Je probeert eerst te begrijpen vanuit de tijd zelf. Begrijpen is niet hetzelfde als goedkeuren.",
    ),
    # --- kunst- en cultuuruitingen analyseren
    volgorde(
        "Zet de stappen om een kunst- of cultuuruiting te analyseren in de juiste volgorde.",
        [
            "Informatie verzamelen over tijd, ruimte, maker en soort",
            "Beschrijven wat je letterlijk ziet of hoort",
            "Onderwerp, doelpubliek en bedoeling bepalen",
            "Je analyse verwoorden",
        ],
        "Eerst de context, dan kijken, dan pas duiden, en ten slotte opschrijven.",
    ),
    sorteer(
        "Zoek je dit op in stap 1 van de kunstanalyse, of hoort het daar niet?",
        ["Stap 1", "Niet in stap 1"],
        [
            ["wanneer en waar het gemaakt is", "Stap 1"],
            ["wie de maker is", "Stap 1"],
            ["de titel en de soort uiting", "Stap 1"],
            ["welke kleuren en welk licht er gebruikt zijn", "Niet in stap 1"],
            ["wat het vandaag op een veiling zou opbrengen", "Niet in stap 1"],
        ],
        "Kleuren en licht beschrijf je in stap 2. De verkoopprijs hoort in geen enkele stap.",
    ),
    koppel(
        "Welke bedoeling past het best bij elke kunst- of cultuuruiting?",
        [
            ["een spotprent die een minister belachelijk maakt", "bekritiseren"],
            ["behangpapier met een herhaald bloemenmotief", "decoreren"],
            ["een volkslied dat op feestdagen gezongen wordt", "identiteit vormgeven"],
            ["een bord in een museum over een opgegraven pot", "informeren"],
            ["een stoel van een bekende ontwerper", "praktisch gebruiken"],
        ],
        ["verkopen"],
        "Vaak zijn er meerdere bedoelingen tegelijk, maar hier springt er telkens één uit. Verkopen staat niet in de lijst van bedoelingen.",
    ),
    casus(
        "In 1650 wordt in een Antwerpse kerk een groot Mariabeeld geplaatst. Het is vol beweging: wapperende kleren, gouden stralen en een breed gebaar naar de gelovigen.",
        [
            mk(
                "Welke bedoelingen passen het best bij dit beeld? (meerdere antwoorden)",
                ["Bevestigen", "Schoonheid creëren", "Entertainen", "Verkopen"],
                [0, 1],
                "Het beeld bevestigt het katholieke geloof en wil ontroeren door zijn schoonheid. Amusement is niet het doel, en verkopen staat niet in de lijst van bedoelingen.",
            ),
            mk(
                "Welke gebeurtenis uit de maatschappelijke context verklaart mee waarom juist hier zo'n beeld komt?",
                [
                    "De Beeldenstorm, bijna een eeuw eerder",
                    "De Guldensporenslag van 1302 in Kortrijk",
                    "De Franse Revolutie en het einde van de adel",
                    "De eerste stoommachines in de Antwerpse haven",
                ],
                0,
                "In 1566 werden kerken leeggehaald. Een prachtig nieuw Mariabeeld is daar een antwoord op.",
            ),
            open_(
                "Leg uit hoe de vorm van het beeld zijn bedoeling ondersteunt. Gebruik twee of drie zinnen.",
                "De beweging, het goud en het grote gebaar moeten de gelovige meeslepen. Zo laat het beeld het geloof voelen in plaats van het uit te leggen, wat de Contrareformatie wilde.",
                "Een goed antwoord verbindt wat je ziet (beweging, licht, gebaar) met de bedoeling (overtuigen, het geloof versterken).",
            ),
        ],
    ),
    mk(
        "Je ziet op sociale media een filmpje over een oude gebeurtenis. Wat neem je uit dit thema mee?",
        [
            "Je vraagt wie het maakte, met welke bronnen, voor wie en waarom",
            "Je gelooft het als het veel gedeeld wordt, want dan hebben velen het nagekeken",
            "Je gelooft niets, want filmpjes over het verleden zijn altijd verzonnen",
            "Je kijkt alleen of de beelden mooi en scherp genoeg gemaakt zijn",
        ],
        0,
        "Dezelfde vragen als bij een oude bron. Voorzichtig zijn is iets anders dan niets geloven.",
    ),
]
