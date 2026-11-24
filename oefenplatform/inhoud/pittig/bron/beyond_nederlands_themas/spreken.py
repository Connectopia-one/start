"""Spreken en gesprekken voeren — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

SPREEKBEURT = (
    "Lees hoe een leerling een spreekbeurt over zwerfvuil voorbereidt.\n\n"
    "Lotte schrijft haar hele tekst woord voor woord uit en leert hem van buiten. Ze oefent één keer, in haar hoofd. "
    "Op de opname kijkt ze vooral naar haar blad. Ze begint met: \"Euh, ja, mijn spreekbeurt gaat dus over iets.\" "
    "Halverwege vertelt ze over een nieuw punt dat ze in het slot nog had willen zeggen. Ze eindigt met: \"Dat was het.\""
)

GESPREK = (
    "Een gesprek op het examen over de stelling \"Huiswerk moet afgeschaft worden.\"\n\n"
    "Examinator: \"Wat vind jij daarvan?\"\n"
    "Sam: \"Ik ben voor, want na school wil ik ook tijd voor mijn sport.\"\n"
    "Examinator: \"Maar oefenen thuis helpt toch om leerstof te onthouden?\"\n"
    "Sam: \"...\""
)

VRAGEN = [
    casus(
        SPREEKBEURT,
        [
            tabel(
                "Wat loopt er mis bij Lotte?",
                [
                    ("Ze heeft geen oogcontact met haar publiek.", J),
                    ("Haar inleiding kondigt het onderwerp niet duidelijk aan.", J),
                    ("Ze brengt een nieuw punt waar het niet hoort.", J),
                    ("Ze kiest een onderwerp dat niet mag.", F),
                ],
                "Het onderwerp is prima. Lichaamstaal, inleiding en opbouw kunnen beter.",
            ),
            mk(
                "Wat had Lotte beter gedaan in plaats van alles uit te schrijven?",
                [
                    "Een spreekplan met kernwoorden maken",
                    "Haar tekst nog sneller voorlezen",
                    "Haar tekst nog twee keer langer maken",
                    "Helemaal niets op papier zetten vooraf",
                ],
                0,
                "Kernwoorden houden je lijn vast en laten je vrij spreken.",
            ),
            keuze(
                "Lotte oefent het best [[*hardop, zodat ze hoort waar ze struikelt|in stilte, om haar stem te sparen|niet, zodat het spontaan blijft]].",
                "Pas hardop merk je waar een zin niet vlot loopt en hoe lang je spreekt.",
            ),
            mk(
                "Welk slot past beter?",
                [
                    "Kortom: wie zijn afval meeneemt, houdt de buurt proper.",
                    "Ik weet eigenlijk niet goed meer wat ik nog moet zeggen, dus.",
                    "En dan nog iets nieuws: plastic in de zee, dat is ook erg.",
                    "Dat was het dan, ik ben blij dat het eindelijk gedaan is.",
                ],
                0,
                "Een slot vat samen of besluit. Geen nieuw punt.",
            ),
        ],
    ),
    casus(
        GESPREK,
        [
            mk(
                "Wat is een sterke reactie van Sam?",
                [
                    "\"Dat klopt, maar korte oefeningen in de klas kunnen dat ook.\"",
                    "\"Nee hoor, dat is gewoon helemaal niet waar, echt niet.\"",
                    "\"Ik weet het niet, misschien heeft u wel gelijk, ik zwijg.\"",
                    "\"Waarom vraagt u dat aan mij, ik ben toch geen leerkracht?\"",
                ],
                0,
                "Hij erkent het punt van de ander en verdedigt zijn standpunt met een argument.",
            ),
            tabel(
                "Is dit een goede gespreksstrategie voor Sam?",
                [
                    ("samenvatten wat de examinator zei voor hij antwoordt", J),
                    ("even nadenken voor hij reageert", J),
                    ("het onderwerp veranderen naar zijn sport", F),
                    ("vragen hoe de examinator het zelf ziet", J),
                ],
                "Samenvatten, een denkpauze en doorvragen houden het gesprek gaande.",
            ),
        ],
    ),
    tabel(
        "Geldt dit criterium enkel bij spreken?",
        [
            ("uitspraak en intonatie", J),
            ("register", F),
            ("lichaamstaal", J),
            ("taakvoltooiing", F),
            ("vlotheid", J),
        ],
        "Register en taakvoltooiing gelden bij elke opdracht.",
    ),
    koppel(
        "Koppel elke situatie aan het criterium waarop ze slecht scoort.",
        [
            ("Je stem blijft de hele tijd even vlak.", "uitspraak en intonatie"),
            ("Je stokt na elke zin en zoekt woorden.", "vlotheid"),
            ("Je staat met je rug half naar het publiek.", "lichaamstaal"),
            ("Je spreekt een jury van volwassenen aan met 'gasten'.", "register"),
        ],
        ["spelling"],
        "Spelling speelt bij spreken geen rol.",
    ),
    tabel(
        "Klopt dit over vlotheid?",
        [
            ("Een bewuste pauze kan je boodschap versterken.", J),
            ("Hoe sneller je spreekt, hoe vlotter je klinkt.", F),
            ("Telkens stokken en opnieuw beginnen is niet vlot.", J),
        ],
        "Vlotheid gaat over haperen, niet over tempo of stilte.",
    ),
    mk(
        "Hoe maak je je structuur hoorbaar voor je luisteraars?",
        [
            "Met signaalwoorden als ten eerste",
            "Door zo luid mogelijk te spreken",
            "Door je tekst sneller af te ronden",
            "Door telkens je blad omhoog te houden",
        ],
        0,
        "Een luisteraar kan niet terugbladeren. Signaalwoorden tonen de opbouw.",
    ),
    keuze(
        "Op het examen krijg je [[*vijftien|vijf|dertig]] minuten voorbereiding voor een gesprek van ongeveer tien minuten.",
        "Gebruik die tijd voor kernwoorden en argumenten.",
    ),
    tabel(
        "Kies je hier verzorgde standaardtaal?",
        [
            ("een presentatie voor een jury op het examen", J),
            ("een gesprek met een onbekende werkgever", J),
            ("een babbel met je beste vriend op de bus", F),
        ],
        "Hoe groter de afstand, hoe formeler je taal.",
    ),
    sorteer(
        "Gaat dit over wat je zegt of over hoe je het zegt?",
        ["Wat", "Hoe"],
        [
            ["je argumenten", "Wat"],
            ["de volledigheid van je antwoord", "Wat"],
            ["je oogcontact", "Hoe"],
            ["de melodie van je zinnen", "Hoe"],
            ["je houding", "Hoe"],
            ["de opbouw van je verhaal", "Wat"],
        ],
        "Beide worden beoordeeld.",
    ),
    casus(
        "Je spreekt over een boek van de lectuurlijst. De examinator vraagt: \"Wat vond je ervan?\"",
        [
            mk(
                "Welk antwoord toont het best je leeservaring?",
                [
                    "\"Het slot raakte me, omdat de vader eindelijk eerlijk is.\"",
                    "\"Het gaat over een jongen die met zijn vader op reis gaat.\"",
                    "\"Het boek heeft ongeveer driehonderd bladzijden en tien delen.\"",
                    "\"Ik vond het oké, gewoon wel goed, niet slecht en niet super.\"",
                ],
                0,
                "Je eigen reactie onderbouwen, geen samenvatting van de inhoud.",
            ),
            tabel(
                "Hoort dit bij het verwoorden van je leeservaring?",
                [
                    ("zeggen welk personage je irriteerde en waarom", J),
                    ("de hele inhoud hoofdstuk per hoofdstuk navertellen", F),
                    ("vertellen wat het boek bij je opriep", J),
                ],
                "Een leeservaring gaat over jouw reactie.",
            ),
        ],
    ),
    mk(
        "Je gesprekspartner zegt iets wat je maar half begrijpt. Wat doe je?",
        [
            "Je vat samen wat je begreep en vraagt door",
            "Je knikt en doet alsof je alles begrijpt",
            "Je begint snel over een heel ander onderwerp",
            "Je antwoordt gewoon iets over je eigen mening",
        ],
        0,
        "Samenvatten en doorvragen voorkomt misverstanden.",
    ),
    tabel(
        "Neem je zo een actieve rol in een gesprek?",
        [
            ("Je geeft het woord door aan wie nog niets zei.", J),
            ("Je wacht tot iemand je iets vraagt.", F),
            ("Je vat samen waar het gesprek staat.", J),
            ("Je stelt een vervolgvraag.", J),
        ],
        "Wie enkel afwacht, voert geen gesprek.",
    ),
    volgorde(
        "Zet de stappen van een gesprek beleefd afsluiten in een logische volgorde.",
        [
            "Kort samenvatten waar jullie geraakt zijn",
            "Bedanken voor het gesprek",
            "Een gepaste afscheidsformule gebruiken",
        ],
        "Eerst inhoudelijk afronden, dan bedanken, dan afscheid nemen.",
    ),
    sleep(
        "Bij een spreekbeurt [[luistert]] je publiek en kan het niet terugbladeren. Daarom maak je je [[structuur]] hoorbaar en betrek je de zaal met [[oogcontact]].",
        ["leest", "spelling", "lay-out"],
        "Spreken vraagt andere middelen dan schrijven.",
    ),
    keuze(
        "Je publiek kijkt verward. Je [[*herneemt het punt in andere woorden|gaat sneller door naar het slot|leest je blad nog eens voor]].",
        "Bijsturen tijdens het spreken is een spreekstrategie.",
    ),
    tabel(
        "Klopt dit over de opname thuis?",
        [
            ("Je kan oefenen, herbekijken en opnieuw opnemen.", J),
            ("De beoordeling is soepeler dan bij een live spreekbeurt.", F),
            ("Lichaamstaal telt ook op de opname mee.", J),
        ],
        "De opname geeft je kansen om bij te sturen. De criteria blijven dezelfde.",
    ),
    casus(
        "Je houdt een spreekbeurt van vijf minuten voor je klas over de vraag of scholen later mogen beginnen.",
        [
            mk(
                "Welke inleiding werkt het best?",
                [
                    "Wie van jullie was vanochtend nog moe? Ik vertel waarom later starten helpt.",
                    "Euh, ik ga dus iets vertellen over school en zo, en over het slapen en zo.",
                    "Mijn onderwerp is scholen. Dat is het. Ik begin meteen met het eerste punt.",
                    "Ik heb dit onderwerp gekozen omdat de leerkracht zei dat het moest van haar.",
                ],
                0,
                "Ze trekt de aandacht en kondigt het onderwerp aan.",
            ),
            tabel(
                "Past dit in het midden van je spreekbeurt?",
                [
                    ("wat onderzoek zegt over de slaap van jongeren", J),
                    ("wat het zou betekenen voor bus- en lesuren", J),
                    ("een samenvatting van wat je al zei", F),
                ],
                "Het midden bevat de uitwerking. De samenvatting hoort in het slot.",
            ),
            keuze(
                "Een woord als [[*bovendien|euh|dus ja]] kondigt een volgend argument aan.",
                "Signaalwoorden maken de opbouw hoorbaar.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over intonatie?",
        [
            ("Met je stem maak je het verschil tussen een vraag en een stellige uitspraak.", J),
            ("Intonatie gaat over welke woorden je kiest.", F),
            ("Een vlakke stem maakt je verhaal moeilijker om te volgen.", J),
        ],
        "Intonatie is de melodie en de klemtoon van je zinnen.",
    ),
    mk(
        "Je krijgt in een gesprek een onverwachte vraag. Wat is de beste reactie?",
        [
            "Je zegt dat je even nadenkt en antwoordt dan",
            "Je antwoordt meteen het eerste wat je te binnen schiet",
            "Je zegt dat die vraag niet in je voorbereiding stond",
            "Je herhaalt je vorige antwoord nog een keer volledig",
        ],
        0,
        "Een korte denkpauze klinkt beter dan een halsoverkop antwoord.",
    ),
    tabel(
        "Hoort dit in je voorbereiding van vijftien minuten?",
        [
            ("kernwoorden en argumenten noteren", J),
            ("een volledig script uitschrijven om voor te lezen", F),
            ("bedenken wat de ander kan tegenwerpen", J),
        ],
        "Een gesprek verloopt nooit zoals je het plant. Kernwoorden werken, een script niet.",
    ),
    keuze(
        "Je gebruikt in je spreekbeurt een beeldspraak als \"zwerfvuil is een sluipend gif\". Dat scoort goed op [[*woordenschat|vlotheid|lichaamstaal]].",
        "Bij woordenschat verwacht men ook figuurlijke taal.",
    ),
    tabel(
        "Gaat dit over beleefdheidsconventies in een gesprek?",
        [
            ("de examinator aanspreken met u", J),
            ("de ander laten uitspreken", J),
            ("de melodie van je stem", F),
            ("bedanken op het einde", J),
        ],
        "Beleefdheid geldt ook mondeling. De melodie van je stem is intonatie.",
    ),
    open_(
        "Je bereidt een gesprek voor over de stelling \"Elke jongere moet een jaar vrijwilligerswerk doen.\" Noteer je standpunt, twee argumenten en een vraag die je aan je gesprekspartner kan stellen.",
        "Standpunt: ik ben tegen een verplichting, wel voor aanmoediging. Argument 1: wie verplicht wordt, doet het met minder inzet. Argument 2: niet iedereen kan een jaar missen, bijvoorbeeld wie moet werken. Vraag: \"Hoe zou jij ervoor zorgen dat jongeren het graag doen?\"",
    ),
]
