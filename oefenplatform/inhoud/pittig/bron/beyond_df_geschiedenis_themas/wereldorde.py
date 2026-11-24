"""Een nieuwe wereldorde: de Verenigde Naties en de Koude Oorlog — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="ijzeren-gordijn.webp", zelf=False,
         wat="Kaart van Europa tijdens de Koude Oorlog met het ijzeren gordijn (Beyond doorstroom).",
         vragen="kaartvraag over de twee blokken"),
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvragen op 1961 en 1989"),
]

VRAGEN = [
    # --- VN
    tabel(
        "Volkenbond of Verenigde Naties?",
        [
            ("Opgericht na de Eerste Wereldoorlog", "Volkenbond"),
            ("Opgericht in 1945", "Verenigde Naties"),
            ("Een Veiligheidsraad met vijf vaste leden", "Verenigde Naties"),
            ("De Verenigde Staten werden nooit lid.", "Volkenbond"),
            ("Bijna elke staat ter wereld is lid.", "Verenigde Naties"),
        ],
        "De Verenigde Naties volgden de Volkenbond op, met de VS en de Sovjet-Unie erbij.",
        kolommen=["Volkenbond", "Verenigde Naties"],
    ),
    mk(
        "Waarom lag de Veiligheidsraad tijdens de Koude Oorlog vaak verlamd?",
        [
            "Elk vast lid kon een besluit blokkeren",
            "De raad mocht pas na 1991 samenkomen",
            "De Sovjet-Unie was geen lid van de Verenigde Naties",
            "De raad had geen enkele bevoegdheid",
        ],
        0,
        "De VS en de Sovjet-Unie hadden allebei een vetorecht en blokkeerden elkaars voorstellen.",
    ),
    tabel(
        "Algemene Vergadering of Veiligheidsraad?",
        [
            ("Spreekt zich uit over wereldproblemen", "Algemene Vergadering"),
            ("Kan sancties opleggen", "Veiligheidsraad"),
            ("Kan een vredesmacht sturen", "Veiligheidsraad"),
        ],
        "Enkel de Veiligheidsraad neemt dwingende beslissingen.",
        kolommen=["Algemene Vergadering", "Veiligheidsraad"],
    ),
    # --- blokken
    sorteer(
        "Westblok of Oostblok?",
        ["Westblok", "Oostblok"],
        [
            ["markteconomie", "Westblok"],
            ["planeconomie", "Oostblok"],
            ["vrije verkiezingen", "Westblok"],
            ["één partij", "Oostblok"],
            ["NAVO", "Westblok"],
            ["Warschaupact", "Oostblok"],
            ["Marshallplan", "Westblok"],
        ],
        "Niet enkel legers stonden tegenover elkaar, maar twee manieren om een samenleving in te richten.",
    ),
    mk(
        "Waarom mochten de landen van het Oostblok niet ingaan op het Marshallplan?",
        [
            "Moskou wilde niet dat ze aan de VS gebonden raakten",
            "Het Marshallplan was enkel voor Afrika bedoeld",
            "De Oostbloklanden hadden geen schade door de oorlog",
            "De Verenigde Naties verboden het",
        ],
        0,
        "Steun voor de heropbouw bond de landen tegelijk aan de Verenigde Staten.",
    ),
    met_prent("ijzeren-gordijn.webp", tabel(
        "Bekijk de kaart van Europa tijdens de Koude Oorlog. Welke uitspraken kun je staven?",
        [
            ("Het ijzeren gordijn liep van de Oostzee tot de Adriatische Zee.", J),
            ("Duitsland was verdeeld over beide blokken.", J),
            ("België hoorde bij de NAVO.", J),
            ("Polen hoorde bij de NAVO.", F),
        ],
        "Polen hoorde bij het Warschaupact. België was lid van de NAVO.",
    )),
    tabel(
        "Een leerling zegt: \"De Koude Oorlog was een oorlog waarin de VS en de Sovjet-Unie tegen elkaar vochten.\" Wat is juist?",
        [
            ("Ze vochten nooit rechtstreeks tegen elkaar.", J),
            ("De strijd liep langs bondgenoten, wapens, spionage en propaganda.", J),
            ("Afschrikking met kernwapens maakte een aanval zinloos.", J),
            ("In 1962 vielen Amerikaanse troepen Moskou binnen.", F),
        ],
        "Koud, omdat de twee grootmachten niet rechtstreeks vochten.",
    ),
    mk(
        "Hoe werkte de afschrikking?",
        [
            "Wie aanvalt, wordt zelf ook vernietigd",
            "Elk blok mocht maar één kernwapen hebben",
            "De VN namen alle kernwapens in beslag",
            "Wie aanvalt, krijgt het Marshallplan",
        ],
        0,
        "Beide kampen hadden zoveel kernwapens dat een aanval zelfmoord werd.",
    ),
    casus(
        "Een Amerikaanse affiche uit 1950 toont een rode hand die over de wereldbol grijpt. Onderaan staat: \"Hou het communisme tegen!\"",
        [
            mk(
                "Hoe lees je deze affiche uit de Koude Oorlog het best?",
                [
                    "Als propaganda voor het eigen kamp",
                    "Als neutrale uitleg over het communisme",
                    "Als een affiche van de Sovjet-Unie",
                    "Als bewijs dat Moskou de wereld veroverde",
                ],
                0,
                "Propaganda stelt de vijand dreigend voor, zodat het eigen kamp samenhoudt.",
            ),
            tabel(
                "Mag je dit besluiten uit de affiche?",
                [
                    ("In de VS vreesde men het communisme.", "Mag"),
                    ("De Sovjet-Unie had in 1950 de hele wereld in handen.", "Mag niet"),
                    ("De makers wilden steun voor het eigen beleid.", "Mag"),
                ],
                "De affiche zegt veel over de angst in het westen, weinig over de echte macht van Moskou.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    # --- Duitsland en Berlijn
    tabel(
        "Welke uitspraken over Duitsland en Berlijn kloppen?",
        [
            ("In 1949 ontstonden de Bondsrepubliek en de DDR.", J),
            ("Berlijn lag volledig in de sovjetzone.", J),
            ("West-Berlijn lag als een eiland in het oosten.", J),
            ("Berlijn werd in twee sectoren verdeeld.", F),
        ],
        "De stad werd in vier sectoren verdeeld, net zoals Duitsland zelf.",
    ),
    mk(
        "Waarom was een luchtbrug nodig tijdens de blokkade van 1948-1949?",
        [
            "De wegen naar West-Berlijn waren afgesloten",
            "West-Berlijn had geen eigen wegen of spoorlijnen",
            "De VN verboden vrachtwagens in Duitsland",
            "Vliegtuigen waren goedkoper dan treinen",
        ],
        0,
        "West-Berlijn lag midden in de sovjetzone. Toen de wegen dichtgingen, bracht het westen maandenlang alles per vliegtuig.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Berlijnse Muur gebouwd werd.",
        "tijdlijn-1750-2030.svg",
        [[67.7, 25, 6.2, 55]],
        "1961, om de vlucht van inwoners naar het westen te stoppen.",
    ),
    # --- crisissen
    volgorde(
        "Zet de crisissen van de Koude Oorlog in chronologische volgorde.",
        ["De blokkade van Berlijn", "De oorlog in Korea", "Hongarije", "De Muur", "De Cubacrisis", "Praag"],
        "1948-1949, 1950-1953, 1956, 1961, 1962 en 1968.",
    ),
    mk(
        "Waarom noemt men de Koreaanse oorlog een proxyoorlog?",
        [
            "Elk blok steunde een kant zonder zelf te verklaren",
            "De VS en de Sovjet-Unie verklaarden elkaar de oorlog",
            "Korea vocht tegen de Verenigde Naties",
            "Het was een oorlog zonder wapens",
        ],
        0,
        "De grootmachten bleven buiten een rechtstreeks gevecht. Het land waar gevochten werd, betaalde de prijs.",
    ),
    casus(
        "Oktober 1962. Amerikaanse vliegtuigen fotograferen raketbases op Cuba, op 150 kilometer van de VS. Dertien dagen lang houdt de wereld de adem in.",
        [
            mk(
                "Waarom was deze crisis zo gevaarlijk?",
                [
                    "Ze bracht de wereld dicht bij een kernoorlog",
                    "Cuba viel de Sovjet-Unie aan met zijn leger",
                    "De Berlijnse Muur werd die maand gebouwd",
                    "De Verenigde Naties werden toen ontbonden",
                ],
                0,
                "Sovjetraketten zo dicht bij de VS dreigden de afschrikking te doen ontploffen.",
            ),
            tabel(
                "Wat klopt over de Cubacrisis?",
                [
                    ("De Sovjet-Unie plaatste raketten op Cuba.", J),
                    ("De crisis werd na dertien dagen opgelost.", J),
                    ("De VS en de Sovjet-Unie vochten op Cuba rechtstreeks tegen elkaar.", F),
                ],
                "Het bleef bij dreiging. Daarna zochten de blokken meer afspraken.",
            ),
        ],
    ),
    tabel(
        "Wat toont het optreden van de sovjettroepen in Hongarije (1956) en Tsjechoslowakije (1968)?",
        [
            ("Pogingen tot hervorming werden beëindigd.", J),
            ("De Oostbloklanden mochten niet vrij hun eigen koers kiezen.", J),
            ("De NAVO stuurde troepen om de hervormers te helpen.", F),
        ],
        "Moskou greep in. Het westen deed niets, uit vrees voor een grote oorlog.",
    ),
    koppel(
        "Welk begrip over de Koude Oorlog hoort bij elke omschrijving?",
        [
            ["De blokken zoeken afspraken over wapens en handel.", "Détente"],
            ["Landen die bij geen blok horen", "Niet-gebonden landen"],
            ["Meer openheid in het publieke leven", "Glasnost"],
            ["Hervorming van de economie", "Perestrojka"],
        ],
        ["Luchtbrug", "Marshallplan"],
        "Détente in de jaren zeventig, glasnost en perestrojka onder Gorbatsjov na 1985.",
    ),
    # --- einde
    klik(
        "Klik op de tijdlijn op het jaar waarin de Berlijnse Muur openging.",
        "tijdlijn-1750-2030.svg",
        [[76.4, 25, 6.2, 55]],
        "November 1989. In 1991 viel de Sovjet-Unie uiteen.",
    ),
    mk(
        "Waarom verliep 1989 in Midden-Europa grotendeels vreedzaam, anders dan in 1956 en 1968?",
        [
            "Moskou greep deze keer niet in",
            "De NAVO bezette Oost-Duitsland",
            "De Muur werd met tanks neergehaald",
            "De VN stuurden een vredesmacht",
        ],
        0,
        "Onder Gorbatsjov stuurde de Sovjet-Unie geen troepen. Dat maakte het verschil.",
    ),
    tabel(
        "Na 1991 zag Europa er anders uit. Welke veranderingen kloppen?",
        [
            ("Duitsland werd opnieuw één staat.", J),
            ("Landen uit het Oostblok sloten later aan bij de EU.", J),
            ("Het Warschaupact verdween.", J),
            ("De wereld bleef in twee militaire blokken verdeeld.", F),
        ],
        "De bipolaire wereld van na 1945 kwam ten einde.",
    ),
    sleep(
        "In [[1991]] viel de Sovjet-Unie uiteen in [[vijftien]] onafhankelijke staten. De laatste leider was [[Gorbatsjov]].",
        ["1989", "twee", "Stalin"],
        "Na de val van de Muur in 1989 volgde twee jaar later het einde van de Sovjet-Unie.",
    ),
    mk(
        "Hoe hangen de Tweede Wereldoorlog en de Koude Oorlog samen?",
        [
            "De twee overwinnaars werden rivalen om Europa",
            "Duitsland won de Tweede Wereldoorlog en verdeelde Europa",
            "De Koude Oorlog begon al voor 1939",
            "De Volkenbond verdeelde Europa in twee blokken",
        ],
        0,
        "Waar hun legers in 1945 stopten, kwam de scheidingslijn te liggen.",
    ),
    open_(
        "Leg uit waarom het ijzeren gordijn meer was dan een militaire grens.",
        "Het scheidde twee manieren om een samenleving in te richten: in het westen een markteconomie met vrije verkiezingen, in het oosten een planeconomie met één partij. Daarbij hoorden ook twee bondgenootschappen, de NAVO en het Warschaupact, en het Marshallplan dat het westen aan de VS bond.",
    ),
    open_(
        "Toon met twee voorbeelden dat de Koude Oorlog niet rechtstreeks tussen de VS en de Sovjet-Unie werd uitgevochten.",
        "In Korea vochten noord en zuid tussen 1950 en 1953, elk gesteund door een blok: een proxyoorlog. Tijdens de Cubacrisis van 1962 bleef het bij dreiging en werd een oorlog vermeden. De strijd liep verder langs spionage, propaganda en een wapenwedloop met kernwapens.",
    ),
    keuze(
        "De NAVO werd opgericht in [[*1949|1955|1945]], het Warschaupact pas in [[*1955|1949|1961]].",
        "Het westen organiseerde zich eerst militair. Het oosten volgde zes jaar later.",
    ),
    inv(
        "Hoe noemt men een wereld die door twee grootmachten bepaald wordt?",
        ["bipolair", "een bipolaire wereld", "bipolaire wereld", "bipolaire"],
        "Na 1945 bepaalden de VS en de Sovjet-Unie de wereldpolitiek.",
    ),
    tabel(
        "Wat bracht de détente van de jaren zeventig?",
        [
            ("Verdragen over kernwapens", J),
            ("De slotakte van Helsinki", J),
            ("Het einde van de Sovjet-Unie", F),
        ],
        "De blokken bleven bestaan, maar zochten afspraken.",
    ),
    tabel(
        "Welke rechten staan in de Universele Verklaring van de Rechten van de Mens van 1948?",
        [
            ("Rechten die voor alle mensen gelden", J),
            ("Rechten die overal gelden", J),
            ("Rechten die enkel voor burgers van de VS gelden", F),
        ],
        "Universeel betekent: voor iedereen, overal.",
    ),
]
