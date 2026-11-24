"""Het communicatiemodel en ruis — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Een middelbare school wil dat ouders hun kind inschrijven voor de schoolreis. De directie zet om tien uur 's avonds een bericht in de schoolapp: \"Inschrijven vóór morgen 9u, anders geen plaats.\" De helft van de ouders gebruikt de app niet. Een vader leest het wel, maar is net thuis na een nachtdienst en vergeet het.",
        [
            tabel(
                "Welk onderdeel van het communicatiemodel is wat?",
                [
                    ("de directie", "Zender"),
                    ("de ouders", "Ontvanger"),
                    ("de schoolapp", "Kanaal"),
                    ("het bericht over inschrijven", "Boodschap"),
                ],
                "Wie stuurt, wie krijgt, waarlangs en wat.",
                kolommen=["Zender", "Ontvanger", "Kanaal", "Boodschap"],
            ),
            mk(
                "Welk onderdeel koos de school het slechtst?",
                ["Het kanaal", "De boodschap", "Het doel", "De zender"],
                0,
                "De inhoud klopt en het doel is duidelijk, maar via dat kanaal bereikt het bericht de helft van de ouders niet.",
            ),
            keuze(
                "De vermoeidheid van de vader na zijn nachtdienst is [[*interne ruis|externe ruis|context]].",
                "Wat in de persoon zelf zit, is interne ruis.",
            ),
            mk(
                "Hoe benoem je dat veel kinderen niet ingeschreven raken?",
                [
                    "Het effect wijkt af van het doel",
                    "Het doel en het effect vallen samen",
                    "De zender was tegelijk ontvanger",
                    "Er was geen enkele ruis in het spel",
                ],
                0,
                "Het doel was inschrijven, het effect is dat velen het missen.",
            ),
        ],
    ),
    sorteer(
        "Interne of externe ruis?",
        ["Interne ruis", "Externe ruis"],
        [
            ["een drilboor voor het raam van het lokaal", "Externe ruis"],
            ["piekeren over een ruzie", "Interne ruis"],
            ["een haperende videoverbinding", "Externe ruis"],
            ["de taal niet goed beheersen", "Interne ruis"],
            ["een krakende microfoon", "Externe ruis"],
            ["boos zijn op de spreker", "Interne ruis"],
        ],
        "Extern komt van buitenaf of uit het kanaal, intern zit in het hoofd van zender of ontvanger.",
    ),
    tabel(
        "Klopt dit over het communicatiemodel?",
        [
            ("Een zender kan ook een organisatie zijn.", J),
            ("In een gesprek wisselen zender en ontvanger voortdurend.", J),
            ("Ruis zit altijd bij de ontvanger.", F),
            ("Het model werkt enkel bij geschreven teksten.", F),
        ],
        "Het model werkt bij elke boodschap, en ruis kan langs beide kanten zitten.",
    ),
    casus(
        "Een verpleegkundige legt in vaktaal uit wat de uitslag van een bloedonderzoek betekent. De patiënt is bang voor slecht nieuws. Op de gang rinkelt voortdurend een telefoon. De patiënt knikt, maar begrijpt er niets van.",
        [
            tabel(
                "Welke ruis is er?",
                [
                    ("de rinkelende telefoon", "Extern"),
                    ("de angst van de patiënt", "Intern"),
                    ("het onbekende vakjargon voor de patiënt", "Intern"),
                ],
                "Vakjargon dat je niet begrijpt, werkt als ruis bij de ontvanger.",
                kolommen=["Extern", "Intern"],
            ),
            mk(
                "Wat had de zender vooral anders moeten doen?",
                [
                    "Zijn taal aanpassen aan de ontvanger",
                    "Veel luider spreken dan de rinkelende telefoon",
                    "De uitslag in een brief sturen",
                    "De patiënt minder laten vragen",
                ],
                0,
                "Ruis bestrijd je zelden door luider te worden. Wie zijn taal niet aanpast, laat de boodschap stranden.",
            ),
        ],
    ),
    mk(
        "Een reclamespot wil dat je een frisdrank koopt. Jij onthoudt enkel het grappige liedje. Wat zie je?",
        [
            "Doel en effect lopen uiteen",
            "Het kanaal was slecht gekozen",
            "Er was externe ruis in de spot",
            "De zender bleef verborgen",
        ],
        0,
        "Het doel ligt vooraf vast bij de zender. Het effect meet je achteraf bij de ontvanger.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Wat de zender wil bereiken", "Doel"],
            ["Wat de boodschap werkelijk teweegbrengt", "Effect"],
            ["De omstandigheden waarin de boodschap landt", "Context"],
            ["Het middel waarlangs de boodschap gaat", "Kanaal"],
        ],
        ["Alinea", "Signaalwoord"],
        "Vier van de negen begrippen uit het model.",
    ),
    mk(
        "Je ziet een affiche zonder afzender: \"Stem op 12 mei NEE!\" Welk onderdeel van het model ontbreekt?",
        ["De zender", "De ontvanger", "Het kanaal", "Het doel"],
        0,
        "Kanaal, ontvanger en doel zijn duidelijk. Juist de zender ontbreekt, en dat is zelf een signaal.",
    ),
    casus(
        "Een filmpje over pesten op school staat op een platform tussen grappige dansfilmpjes. Veel kijkers scrollen er lachend voorbij.",
        [
            mk(
                "Welk onderdeel van het model speelt hier vooral mee?",
                ["De context", "De zender", "De boodschap", "De interne ruis"],
                0,
                "De omgeving kleurt hoe iets ontvangen wordt.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("Dezelfde boodschap op een andere plek kan anders binnenkomen.", J),
                    ("Dezelfde boodschap kan bij twee kijkers een ander effect hebben.", J),
                    ("Het effect hangt enkel van de woorden af.", F),
                ],
                "Context, voorkennis en stemming bepalen het effect mee.",
            ),
        ],
    ),
    tabel(
        "In welk geval valt het effect samen met het doel?",
        [
            ("Een uitnodiging die wordt aangenomen", J),
            ("Een grap die iemand kwetst", F),
            ("Een waarschuwing die mensen doet lachen", F),
            ("Een uitleg die de ontvanger niet begrijpt", F),
        ],
        "Alleen bij de aanvaarde uitnodiging komt eruit wat de zender wilde.",
    ),
    mk(
        "Hoe beperkt een zender externe ruis het best?",
        [
            "Door een rustiger moment of kanaal te kiezen",
            "Door luider en sneller te praten tegen de ontvanger",
            "Door meer vakjargon en moeilijke woorden te gebruiken",
            "Door de boodschap korter te maken",
        ],
        0,
        "Een ander moment, een andere plaats of een ander kanaal werkt beter dan harder roepen.",
    ),
    sleep(
        "Voor je een mail schrijft aan een onbekende instantie, bepaal je eerst je [[doel]] en je [[ontvanger]]. Daaruit volgen de toon en het [[register]].",
        ["kanaal", "ruis"],
        "Het model helpt ook bij schrijven, niet enkel bij lezen.",
    ),
    tabel(
        "Een bericht gaat enkel rond op sociale media, nergens anders. Wat mag je besluiten?",
        [
            ("Geen redactie heeft het nagekeken.", J),
            ("Het is daarom zeker onwaar.", F),
            ("Het is een reden om verder te kijken.", J),
        ],
        "Op sociale media publiceert iedereen zonder tussenstap. Dat is geen bewijs, wel een signaal.",
    ),
    keuze(
        "Emoji's in een bericht horen in het model bij [[*de boodschap|het kanaal|de context]].",
        "Ze dragen betekenis en toon, net als woorden.",
    ),
    mk(
        "Een bedrijf stuurt al zijn klanten een mail over een prijsstijging, net voor de feestdagen. Wat hoort bij de context?",
        [
            "De zakelijke relatie en het moment",
            "De precieze woorden in de onderwerpregel",
            "Het mailprogramma dat de klant gebruikt",
            "Het logo onderaan de mail",
        ],
        0,
        "Context is het kader: wie staat tot wie in welke verhouding, en wanneer.",
    ),
    casus(
        "Lies stuurt haar vriend een appje: \"Leuk dat je er gisteren wéér niet was 🙂\". Hij leest het op de bus, tussen roepende kinderen, en antwoordt: \"Ja, het was ook leuk thuis!\"",
        [
            mk(
                "Wat wilde Lies waarschijnlijk zeggen?",
                [
                    "Dat ze teleurgesteld is",
                    "Dat ze het leuk vond dat hij thuisbleef",
                    "Dat ze volgende keer ook niet komt",
                    "Dat ze de bus van haar vriend miste",
                ],
                0,
                "Het woordje \"wéér\" en de context verraden ironie.",
            ),
            tabel(
                "Wat speelde mee in het misverstand?",
                [
                    ("Een appje toont geen stem of gezicht.", J),
                    ("De roepende kinderen op de bus.", J),
                    ("De emoji kan op twee manieren gelezen worden.", J),
                    ("Lies was geen echte zender.", F),
                ],
                "Kanaal, externe ruis en een dubbelzinnige boodschap.",
            ),
            keuze(
                "Het antwoord van de vriend toont dat het [[*effect|doel|kanaal]] niet overeenkomt met wat Lies bedoelde.",
                "Effect is wat er werkelijk gebeurt bij de ontvanger.",
            ),
        ],
    ),
    tabel(
        "Een zender, een boodschap en een ontvanger. Wie is in elk geval de ontvanger?",
        [
            ("Een leerkracht zegt tegen de klas: \"Mooi werk.\"", "De klas"),
            ("Een krant schrijft een artikel voor haar abonnees.", "De abonnees"),
            ("Een merk lanceert een reclame voor tieners.", "De tieners"),
        ],
        "De ontvanger kan één persoon zijn of een hele groep.",
        kolommen=["De klas", "De abonnees", "De tieners"],
    ),
    mk(
        "Waarom vraag je je bij een lees- of luistertekst af wie de ontvanger is?",
        [
            "Dat verklaart de toon en de woordkeuze",
            "Dan weet je altijd wie de zender van de tekst is",
            "Dan kan je de ruis volledig wegnemen",
            "Dan hoef je de context niet te kennen",
        ],
        0,
        "Een tekst voor kinderen ziet er anders uit dan een tekst voor een minister.",
    ),
    tabel(
        "Je herkent nepnieuws aan een bericht zonder auteur dat enkel op sociale media rondgaat. Welke onderdelen van het model gebruik je?",
        [
            ("de zender", J),
            ("het kanaal", J),
            ("het doel", J),
            ("de interne ruis van de lezer", F),
        ],
        "Je kijkt wie het stuurt, waarlangs en waarom. Ruis speelt hier geen rol.",
    ),
    mk(
        "Een politicus geeft dezelfde boodschap op een persconferentie en in een anoniem appje. Wat verandert er?",
        [
            "Hoe betrouwbaar de boodschap overkomt",
            "De inhoud van de boodschap zelf, woord voor woord",
            "Het doel dat de politicus heeft",
            "Niets, want de woorden zijn dezelfde",
        ],
        0,
        "Het kanaal zegt iets over de bedoeling van de zender en kleurt de boodschap mee.",
    ),
    inv(
        "Lawaai, een slechte verbinding of een krakende microfoon: welk soort ruis is dat? Antwoord met één woord.",
        ["extern", "externe", "externe ruis"],
        "Externe ruis zit buiten de personen.",
    ),
    tabel(
        "Hoort dit begrip in het communicatiemodel?",
        [
            ("ruis", J),
            ("context", J),
            ("effect", J),
            ("alinea", F),
            ("tussentitel", F),
        ],
        "Het model telt negen begrippen. Alinea en tussentitel horen bij de tekstopbouw.",
    ),
    mk(
        "Een leerling zegt tijdens een groepswerk: \"Doe maar, ik vind alles goed.\" Ze bedoelt dat ze geen zin heeft. De anderen denken dat ze akkoord is. Waar zit het probleem?",
        [
            "Het effect verschilt van wat ze bedoelde",
            "Er was externe ruis in het lokaal aanwezig",
            "Het kanaal van een gesprek is ongeschikt",
            "De anderen waren geen echte ontvangers",
        ],
        0,
        "Wat ze werkelijk teweegbracht, verschilt van wat ze wilde zeggen.",
    ),
    open_(
        "Je moet je klas uitnodigen voor een benefietavond. Kies een zender, een kanaal en een moment, en leg uit hoe je ruis beperkt.",
        "Zender: de klasvertegenwoordiger, want die kennen de leerlingen. Kanaal: een kort bericht in de klasgroep plus een aankondiging in de klas, zodat niemand het mist. Moment: 's middags, niet laat op de avond. Ruis beperk ik door het bericht kort en duidelijk te houden en het niet tijdens een toetsweek te sturen.",
    ),
]
