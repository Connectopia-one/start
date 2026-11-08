"""De Tweede Wereldoorlog en de Holocaust — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, met_prent

PRENTEN = [
    dict(bestand="kazerne-dossin.webp", zelf=False,
         wat="Een foto van de Dossinkazerne in Mechelen (vandaag Kazerne Dossin, herinneringsplaats en museum). Een gewone buitenfoto van het gebouw volstaat; geen schokkende beelden.",
         waar="Wikimedia Commons, zoek 'Kazerne Dossin Mechelen'.",
         vragen="casus over herinneringsplaatsen en de Holocaust in België"),
]

VRAGEN = [
    tabel(
        "Welke oorzaken van de Tweede Wereldoorlog haalt men aan?",
        [
            ("De wrok over het Verdrag van Versailles", J),
            ("De economische crisis van de jaren dertig", J),
            ("De expansiedrang van de totalitaire regimes", J),
            ("De moord op de Oostenrijkse troonopvolger in Sarajevo", F),
        ],
        "Versailles, de crisis en de expansiedrang van de totalitaire regimes. Sarajevo was de aanleiding van de Eerste Wereldoorlog.",
    ),
    keuze(
        "De Duitse aanvalstactiek met snelle tankcolonnes en vliegtuigen heet [[*Blitzkrieg|loopgravenoorlog|appeasement]]. Tussen 1939 en 1942 boekten de [[*asmogendheden|geallieerden|Centralen]] vooral overwinningen.",
        "Met de Blitzkrieg veroverde Duitsland snel grote gebieden. Pas in 1942 keerde het tij.",
    ),
    koppel(
        "Welk keerpunt van 1942 hoort bij welk front?",
        [
            ["Oostfront", "Stalingrad"],
            ["Noord-Afrika", "El Alamein"],
            ["Stille Oceaan", "Midway"],
        ],
        ["Pearl Harbor", "Normandië"],
        "Drie keerpunten in 1942. Pearl Harbor was de Japanse aanval van 1941, Normandië de landing van 1944.",
    ),
    volgorde(
        "Zet de gebeurtenissen van de Tweede Wereldoorlog in de juiste volgorde.",
        ["De Duitse inval in Polen", "De Duitse inval in België", "De Duitse inval in de Sovjet-Unie", "De Japanse aanval op Pearl Harbor", "De landing in Normandië", "De atoombommen op Hiroshima en Nagasaki"],
        "September 1939, 10 mei 1940, 22 juni 1941, december 1941, 6 juni 1944 en augustus 1945.",
    ),
    mk(
        "Hoe kwamen de Verenigde Staten in de oorlog terecht?",
        [
            "Door de Japanse aanval op Pearl Harbor in december 1941",
            "Door de Duitse inval in Polen in september 1939",
            "Door de landing in Normandië in juni 1944",
            "Door de blokkade van Berlijn in het jaar 1948",
        ],
        0,
        "De aanval op Pearl Harbor bracht de Verenigde Staten in de oorlog, zowel tegen Japan als tegen Duitsland.",
    ),
    sorteer(
        "Is het een gelijkenis of een verschil tussen de twee wereldoorlogen?",
        ["Gelijkenis", "Verschil"],
        [
            ["Het zijn allebei totale oorlogen", "Gelijkenis"],
            ["In de tweede werd op veel meer plaatsen in de wereld gevochten", "Verschil"],
            ["In de tweede hoorden bezetting en uitroeiingspolitiek tot de oorlogvoering", "Verschil"],
            ["In de tweede bewogen de legers snel in plaats van zich in te graven", "Verschil"],
        ],
        "Beide oorlogen betrokken de hele samenleving. Maar de tweede was mondialer, sneller en had een uitroeiingspolitiek.",
    ),
    tabel(
        "Hoort het kenmerk bij de Eerste of bij de Tweede Wereldoorlog?",
        [
            ("Gifgas aan het front", "Eerste"),
            ("Meer burgerslachtoffers dan militaire slachtoffers", "Tweede"),
            ("Een lange loopgravenoorlog", "Eerste"),
            ("Gevechten in Azië, Afrika en op de oceanen", "Tweede"),
        ],
        "Gifgas aan het front en de loopgraven horen bij de eerste. In de tweede vielen meer burgers en werd over de hele wereld gevochten.",
        kolommen=["Eerste", "Tweede"],
    ),
    tabel(
        "Een historicus beschrijft de wereld van 1949. Welke veranderingen ten opzichte van 1939 noemt hij terecht?",
        [
            ("De Verenigde Staten en de Sovjet-Unie werden supermachten.", J),
            ("De Verenigde Naties werden opgericht.", J),
            ("De dekolonisatie kwam op gang.", J),
            ("Duitsland bleef één land met één regering.", F),
        ],
        "Duitsland werd in bezettingszones verdeeld en in 1949 in twee staten gesplitst.",
    ),
    keuze(
        "De nazileiders werden na de oorlog berecht in [[*Neurenberg|Versailles|Wenen]]. In 1948 nam de jonge VN de Universele Verklaring van de [[*Rechten van de Mens|Volkenbond|Neurenbergse wetten]] aan.",
        "Neurenberg werd de plaats van het grote proces. De Universele Verklaring van 1948 moest zulke misdaden in de toekomst voorkomen.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over bezet België.",
        [
            ("Duitsland viel België binnen op 10 mei 1940.", J),
            ("De Belgische veldtocht duurde 18 dagen.", J),
            ("Koning Leopold III week samen met de regering uit naar Londen.", F),
            ("Er ontstond een breuk tussen de koning en de regering.", J),
        ],
        "De koning bleef in bezet land, de regering week uit naar Londen. Dat leidde tot een breuk die na de oorlog de koningskwestie werd.",
    ),
    sorteer(
        "Welke vorm van collaboratie herken je?",
        ["Politiek", "Militair", "Economisch"],
        [
            ["Leden van het VNV werken mee met het bestuur van de bezetter", "Politiek"],
            ["Vrijwilligers vechten aan het oostfront mee met het Duitse leger", "Militair"],
            ["Een fabriek maakt onderdelen voor de Duitse oorlogsindustrie", "Economisch"],
            ["Rex steunt openlijk de bezetter", "Politiek"],
        ],
        "Politieke collaboratie door bewegingen als het VNV en Rex, militaire door vrijwilligers aan het oostfront, en economische door bedrijven die voor de bezetter werkten.",
    ),
    tabel(
        "Hoorde de daad bij het verzet?",
        [
            ("Sluikbladen drukken en verspreiden", J),
            ("Ontsnappingslijnen voor piloten opzetten", J),
            ("Onderduikadressen zoeken voor Joodse kinderen", J),
            ("Als vrijwilliger aan het oostfront gaan vechten", F),
        ],
        "Het verzet werkte in het geheim tegen de bezetter. Vechten aan het oostfront was militaire collaboratie.",
    ),
    mk(
        "Wat gebeurde er in 1943 bij Boortmeerbeek?",
        [
            "Drie verzetslieden brachten een deportatietrein tot stilstand",
            "De geallieerden landden er met parachutisten",
            "Het Ardennenoffensief begon er met een Duitse aanval",
            "De Belgische regering keerde er terug uit Londen",
        ],
        0,
        "Een zeldzame daad van gewapend verzet tegen de deportaties: drie verzetslieden hielden een trein naar Auschwitz tegen.",
    ),
    mk(
        "Waarom was de bevrijding van Antwerpen in september 1944 zo belangrijk voor de geallieerden?",
        [
            "De haven bleef vrijwel onbeschadigd en redde de bevoorrading",
            "Antwerpen was de hoofdstad van het bezette Duitsland",
            "De Duitse capitulatie werd er meteen ondertekend",
            "De koning bevond zich in Antwerpen en nam er de leiding",
        ],
        0,
        "Een werkende haven betekende brandstof, voedsel en munitie voor de legers. Daarom probeerde Duitsland met het Ardennenoffensief nog naar Antwerpen door te stoten.",
    ),
    mk(
        "Een leerling zegt: \"In de oorlog was je ofwel collaborateur, ofwel verzetsstrijder.\" Wat is de beste reactie?",
        [
            "De meeste mensen probeerden vooral te overleven, en sommigen deden in vier jaar allebei iets",
            "Klopt: elke Belg moest in 1940 kiezen en die keuze bleef vier jaar lang dezelfde",
            "Klopt: wie niet in het verzet zat, werd na de oorlog altijd als collaborateur veroordeeld",
            "Collaboratie en verzet bestonden in België niet, alleen in Frankrijk en Nederland",
        ],
        0,
        "Er waren geen twee scherp gescheiden kampen. Wie zo'n zwart-witbeeld maakt, veralgemeent.",
    ),
    inv(
        "Hoe noemt men de vervolging van wie met de bezetter had samengewerkt, na de bevrijding? (één woord)",
        "repressie",
        "De repressie vervolgde collaborateurs na 1944. Het is een begrip dat in België nog lang gevoelig bleef.",
    ),
    volgorde(
        "Zet de stappen in de vervolging van de Joden in nazi-Duitsland in de juiste volgorde.",
        ["Uitsluiting uit het openbare leven", "Gedwongen samenleven in getto's", "Systematische vernietiging in kampen"],
        "Eerst uitsluiting met wetten zoals die van Neurenberg, daarna de getto's, en ten slotte de vernietiging.",
    ),
    mk(
        "Wat werd besproken op de Wannseeconferentie van januari 1942?",
        [
            "De praktische organisatie van de vernietiging van de Joden",
            "De verdeling van Polen tussen Duitsland en de Sovjet-Unie",
            "De overgave van Italië aan de geallieerden",
            "De oprichting van de Verenigde Naties",
        ],
        0,
        "Daar werd de uitvoering van de genocide geregeld, met ambtenaren van verschillende ministeries.",
    ),
    casus(
        "Bekijk de foto van de Dossinkazerne in Mechelen. Vandaag is het gebouw een herinneringsplaats en museum. Lees ook: uit België vertrokken de treinen vanuit deze kazerne naar Auschwitz.",
        [
            met_prent("kazerne-dossin.webp", mk(
                "Welke rol speelde de Dossinkazerne in de Holocaust?",
                ["Van daaruit vertrokken de treinen naar Auschwitz", "Daar werd de Wannseeconferentie gehouden", "Daar vond het proces tegen de nazileiders plaats", "Daar drukte het verzet zijn sluikbladen"],
                0,
                "Joden en Roma uit België werden er verzameld en per trein naar Auschwitz gedeporteerd.",
            ), volgt=True),
            tabel(
                "Is dit een kenmerk van een collectieve herinnering?",
                [
                    ("Er wordt jaarlijks op een vaste dag bij stilgestaan.", "Ja"),
                    ("Er staat een monument of gedenkplaat in de openbare ruimte.", "Ja"),
                    ("Er bestaan heel veel geschreven bronnen over.", "Nee"),
                    ("Een hele groep deelt er een gevoel en een betekenis over.", "Ja"),
                ],
                "Het aantal bronnen zegt niets over een collectieve herinnering. Herdenkingen, monumenten en een gedeelde betekenis wel.",
                kolommen=["Ja", "Nee"],
            ),
            mk(
                "Waarom blijft herdenken op een plek als deze belangrijk nu de laatste ooggetuigen wegvallen?",
                [
                    "Onderwijs en bronnen moeten de herinnering dan overnemen",
                    "Omdat er vroeger nooit over de Holocaust gesproken werd",
                    "Omdat de plek bewijst dat er geen andere kampen waren",
                    "Omdat herdenken verplicht is voor elke Belgische burger",
                ],
                0,
                "Getuigenissen van overlevenden toonden wat cijfers niet kunnen. Zonder hen moeten musea, onderwijs en bronnen dat doen.",
            ),
        ],
    ),
    tabel(
        "Welke groepen vervolgde en vermoordde het naziregime, naast de Joden?",
        [
            ("Roma en Sinti", J),
            ("Mensen met een beperking", J),
            ("Politieke tegenstanders", J),
            ("Leden van de NSDAP", F),
        ],
        "Ook Roma en Sinti, mensen met een beperking en politieke tegenstanders werden slachtoffer.",
    ),
    mk(
        "Genocide is het opzettelijk geheel of gedeeltelijk vernietigen van een nationale, etnische, raciale of religieuze groep. Waarom past dat begrip op de Holocaust?",
        [
            "Een hele bevolkingsgroep moest doelbewust verdwijnen",
            "Er vielen in die oorlog veel doden aan beide kanten",
            "Er werd in de oorlog ook gifgas aan het front gebruikt",
            "De slachtoffers waren vooral soldaten van het verzet",
        ],
        0,
        "Het gaat om het opzet: het uitroeien van de Joden als groep. Veel doden in een oorlog maken op zich nog geen genocide.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over het begrip genocide.",
        [
            ("Het begrip bestond al lang voor de Tweede Wereldoorlog.", F),
            ("Het werd in 1944 gemunt.", J),
            ("Het kwam in 1948 in het internationale recht.", J),
        ],
        "Het woord werd tijdens de oorlog bedacht, juist om deze misdaad te kunnen benoemen, en in 1948 in het recht opgenomen.",
    ),
    keuze(
        "Zeg je dat de Holocaust niet alleen het werk was van enkele leiders, maar ook van gewone ambtenaren en spoorwegpersoneel, dan gebruik je de redeneerwijze [[*menselijke actoren benoemen|continuïteit benoemen|stereotypering analyseren]].",
        "Je toont dat mensen keuzes maakten en meewerkten. Dat is agency of menselijke actoren benoemen.",
    ),
    mk(
        "Bij benadering hoeveel Joden kwamen om in de Holocaust?",
        ["6 miljoen", "600 000", "60 miljoen", "60 000"],
        0,
        "Ongeveer 6 miljoen Joden werden vermoord.",
    ),
    mk(
        "De bewaarde loopgraven aan het IJzerfront zijn een herinneringsplaats. Aan welke oorlog herinneren ze?",
        ["Aan de Eerste Wereldoorlog", "Aan de Tweede Wereldoorlog", "Aan de Koude Oorlog", "Aan de Belgische revolutie"],
        0,
        "Het IJzerfront hoort bij 1914-1918. Een veelgemaakte fout is ze aan de Tweede Wereldoorlog te koppelen.",
    ),
    open_(
        "Vergelijk de Eerste en de Tweede Wereldoorlog. Geef één gelijkenis en twee verschillen.",
        "Gelijkenis: het zijn allebei totale oorlogen, waarin de hele samenleving betrokken werd. Verschillen: in de tweede werd op veel meer plaatsen in de wereld gevochten, en bezetting en uitroeiingspolitiek hoorden bij de oorlogvoering. Ook bewogen de legers in de tweede snel met tanks en vliegtuigen, terwijl ze zich in de eerste ingroeven in loopgraven.",
    ),
    sleep(
        "Het Ardennenoffensief was een laatste Duits [[tegenoffensief]] in de winter van [[1944]]. De oorlog eindigde in Europa met de Duitse [[capitulatie]] in mei 1945.",
        ["bezetting", "1943", "wapenstilstand"],
        "Na het mislukte Ardennenoffensief volgde in mei 1945 de Duitse overgave. In Azië eindigde de oorlog na de atoombommen.",
    ),
    mk(
        "Hoe kwam de Tweede Wereldoorlog in Azië ten einde?",
        [
            "Na de atoombommen op Hiroshima en Nagasaki",
            "Na de landing van de geallieerden in Normandië",
            "Na de Duitse nederlaag bij Stalingrad",
            "Na de val van de Berlijnse Muur",
        ],
        0,
        "In Europa capituleerde Duitsland in mei 1945. Japan gaf zich over in augustus 1945, na de atoombommen.",
    ),
]
