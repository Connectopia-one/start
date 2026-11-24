"""Argumentatie en drogredenen — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lees het betoog.\n\n"
        "(1) De stad moet de bibliotheek elke avond tot tien uur openhouden. "
        "(2) Veel studenten hebben thuis geen rustige plek om te studeren. "
        "(3) Uit een bevraging bij 1200 studenten blijkt bovendien dat 64 procent 's avonds studeert. "
        "(4) Sommigen zeggen dat dit te duur is. "
        "(5) Maar de extra kosten zijn kleiner dan wat de stad jaarlijks uitgeeft aan één zomerfestival. "
        "(6) Langer openblijven is dus een kleine investering met een groot effect.",
        [
            tabel(
                "Welke rol speelt elke zin?",
                [
                    ("zin 1", "Stelling"),
                    ("zin 2", "Argument"),
                    ("zin 4", "Tegenargument"),
                    ("zin 6", "Conclusie"),
                ],
                "Stelling, argumenten, een tegenargument dat weerlegd wordt, en een conclusie.",
                kolommen=["Stelling", "Argument", "Tegenargument", "Conclusie"],
            ),
            mk(
                "Wat doet zin 5?",
                [
                    "Hij weerlegt het tegenargument",
                    "Hij geeft een nieuwe stelling",
                    "Hij herhaalt het eerste argument",
                    "Hij is een persoonlijke aanval",
                ],
                0,
                "\"Maar\" pareert de tegenwerping over de kosten.",
            ),
            mk(
                "Welke soort argumentatie gebruikt zin 3?",
                [
                    "Op basis van cijfers",
                    "Op basis van een autoriteit",
                    "Op basis van vergelijking",
                    "Op basis van oorzaak en gevolg",
                ],
                0,
                "Een percentage uit een bevraging is argumentatie met cijfers en statistieken.",
            ),
            tabel(
                "Welke vraag stel je bij de bevraging in zin 3?",
                [
                    ("Wie voerde ze uit?", J),
                    ("Wie heeft ze betaald?", J),
                    ("Hoe lang is het verslag?", F),
                    ("Wanneer werd ze gehouden?", J),
                ],
                "Uitvoerder, financiering en datum zeggen iets over de waarde. De lengte niet.",
            ),
            keuze(
                "Waarom is het sterk dat de schrijver zin 4 zelf noemt? Hij toont dat hij [[*de andere kant kent|geen argumenten heeft|zijn stelling opgeeft]].",
                "Wie de tegenwerping zelf opwerpt en weerlegt, laat weinig ruimte over.",
            ),
        ],
    ),
    tabel(
        "Feit of mening?",
        [
            ("Antwerpen telt meer inwoners dan Gent.", "Feit"),
            ("Dit boek is veel te langdradig.", "Mening"),
            ("De schooldag zou later moeten beginnen.", "Mening"),
            ("De les begint om 8.25 uur.", "Feit"),
        ],
        "Een feit kan je nagaan. Woorden als moeten en zouden wijzen vaak op een mening.",
        kolommen=["Feit", "Mening"],
    ),
    koppel(
        "Welke drogreden zit in elke uitspraak?",
        [
            ["\"Dat zegt iemand die zelf nooit op tijd komt.\"", "Persoonlijke aanval"],
            ["\"Iedereen vindt dit, dus het klopt.\"", "Meerderheid"],
            ["\"Als we dit toelaten, staan we morgen voor de afgrond.\"", "Hellend vlak"],
            ["\"Je bent voor ons of tegen ons.\"", "Vals dilemma"],
        ],
        ["Vergelijking", "Conclusie"],
        "Vier drogredenen die op een argument lijken maar niets bewijzen.",
    ),
    casus(
        "In een gemeente stegen tussen 2000 en 2020 zowel het aantal ooievaars als het aantal geboorten. Een krant kopt: \"Meer ooievaars, meer baby's!\"",
        [
            mk(
                "Wat mag je hieruit besluiten?",
                [
                    "Er is samenhang, geen bewezen oorzaak",
                    "Ooievaars veroorzaken geboorten",
                    "Geboorten lokken ooievaars naar de gemeente",
                    "De cijfers zijn zeker vervalst",
                ],
                0,
                "Twee lijnen die samen stijgen, bewijzen geen oorzakelijk verband.",
            ),
            keuze(
                "Vaak zit er achter zo'n samenhang een [[*derde factor|drogreden|cirkelredenering]], zoals een gemeente die groeit.",
                "Argumentatie op basis van oorzaak en gevolg vraagt dat het verband ook echt bestaat.",
            ),
        ],
    ),
    sorteer(
        "Gewoon argument of drogreden?",
        ["Argument", "Drogreden"],
        [
            ["Het project kost 2 miljoen euro, de helft van het budget.", "Argument"],
            ["Dit is altijd zo geweest, dus het moet zo blijven.", "Drogreden"],
            ["Een studie bij 3000 leerlingen toont betere resultaten.", "Argument"],
            ["Dit is verboden omdat het niet mag.", "Drogreden"],
        ],
        "De laatste is een cirkelredenering: de stelling dient als argument voor zichzelf.",
    ),
    mk(
        "Een bekende acteur zegt in een spot dat een siroop tegen verkoudheid helpt. Wat is het probleem?",
        [
            "Bekendheid is geen deskundigheid",
            "Acteurs mogen niet in reclame spelen",
            "Een spot bevat nooit argumenten",
            "Siroop is geen geneesmiddel",
        ],
        0,
        "Dit is een beroep op een valse autoriteit.",
    ),
    tabel(
        "Welke eis stel je aan een sterk argument?",
        [
            ("Het is waar.", J),
            ("Het gaat echt over de stelling.", J),
            ("Het weegt zwaar genoeg.", J),
            ("Het wordt luid uitgeroepen.", F),
        ],
        "Waar, ter zake en belangrijk genoeg. Uitroeptekens maken een betoog luider, niet sterker.",
    ),
    mk(
        "\"In Finland werkt een vierdaagse schoolweek al jaren, dus bij ons zal het ook werken.\" Welke vraag stel je eerst?",
        [
            "Is de situatie in Finland vergelijkbaar?",
            "Hoeveel inwoners en scholen telt Finland vandaag?",
            "Wie heeft deze uitspraak gedaan?",
            "Is dit een feit of een conclusie?",
        ],
        0,
        "Bij argumentatie op basis van vergelijking is de kernvraag of de vergelijking opgaat.",
    ),
    casus(
        "Een journalist vraagt een minister: \"Waarom zijn de wachtlijsten in de jeugdzorg zo lang?\" De minister antwoordt: \"Wij hebben de voorbije jaren fors geïnvesteerd in sport en cultuur voor jongeren.\"",
        [
            mk(
                "Wat gebeurt er?",
                [
                    "De vraag wordt ontweken",
                    "De vraag wordt met cijfers beantwoord",
                    "De minister weerlegt een tegenargument",
                    "De minister gebruikt een vals dilemma",
                ],
                0,
                "Het gesprek wordt naar veiliger terrein verlegd.",
            ),
            tabel(
                "Klopt dit over het antwoord?",
                [
                    ("Het kan waar zijn en toch niet ter zake.", J),
                    ("Een waar argument is altijd relevant.", F),
                    ("Een goede journalist vraagt door.", J),
                ],
                "Waar en ter zake zijn twee aparte eisen.",
            ),
        ],
    ),
    mk(
        "Iemand zegt: \"Deze maatregel is onrechtvaardig.\" Hoe beoordeel je die uitspraak het best?",
        [
            "Je kijkt op welke argumenten ze steunt",
            "Je zoekt het op in de bevolkingscijfers",
            "Je verwerpt ze, want het is een mening",
            "Je aanvaardt ze, want ze is stellig",
        ],
        0,
        "Een mening kan je niet nagaan als feit, wel of er goede redenen bij staan.",
    ),
    sleep(
        "De [[stelling]] opent het betoog nog onbewezen. De [[conclusie]] sluit af na het bewijs en moet uit de [[argumenten]] volgen.",
        ["drogreden", "mening"],
        "Vaak zeggen stelling en conclusie hetzelfde, maar op een ander moment.",
    ),
    tabel(
        "Cijfers in een betoog. Klopt dit?",
        [
            ("Correcte cijfers kunnen toch misleiden.", J),
            ("De keuze van wat je vergelijkt, kan het beeld sturen.", J),
            ("Cijfers liegen nooit.", F),
        ],
        "Selectie, vergelijkingsbasis en voorstelling bepalen wat cijfers lijken te zeggen.",
    ),
    mk(
        "Je schrijft een betoog en wil drogredenen vermijden. Wat controleer je bij elk argument?",
        [
            "Of het echt over de stelling gaat",
            "Of het met een uitroepteken eindigt",
            "Of het in de eerste alinea staat",
            "Of het een mening is",
        ],
        0,
        "Veel drogredenen ontstaan doordat je iets aanvoert dat naast de kwestie ligt.",
    ),
    casus(
        "Lees de reactie op een forum.\n\n"
        "\"Een verbod op vuurwerk? Belachelijk. Wie dat voorstelt, heeft duidelijk nooit plezier gehad op oudejaar. "
        "Bovendien: of we verbieden alles, of we laten mensen vrij. Vandaag vuurwerk, morgen de barbecue en straks mogen we niets meer.\"",
        [
            tabel(
                "Welke drogredenen vind je terug?",
                [
                    ("persoonlijke aanval", J),
                    ("vals dilemma", J),
                    ("hellend vlak", J),
                    ("beroep op wetenschappelijk onderzoek", F),
                ],
                "De voorsteller wordt aangevallen, er zijn maar twee keuzes, en er volgt een reeks rampen zonder bewijs.",
            ),
            keuze(
                "\"Of we verbieden alles, of we laten mensen vrij\" moffelt alle [[*tussenposities|argumenten|feiten]] weg.",
                "Bij een vals dilemma doet men alsof er maar twee mogelijkheden zijn.",
            ),
            mk(
                "Wat ontbreekt er het meest in deze reactie?",
                [
                    "Een argument over vuurwerk zelf",
                    "Een duidelijk standpunt van de schrijver",
                    "Een mening van de schrijver over het verbod",
                    "Een signaalwoord dat iets toevoegt",
                ],
                0,
                "Het standpunt is duidelijk, maar geen enkele zin gaat over de gevolgen van vuurwerk zelf.",
            ),
        ],
    ),
    inv(
        "Een redenering die klopt lijkt maar bij nader inzien niets bewijst, heet een ... Antwoord met één woord.",
        ["drogreden", "drogredenering"],
        "Een drogreden lijkt een argument maar bewijst niets.",
    ),
    mk(
        "Een studie bij drieduizend leerlingen toont dat later beginnen de resultaten verbetert. Welke soort argumentatie is dat?",
        [
            "Op basis van wetenschappelijk onderzoek",
            "Op basis van een valse autoriteit",
            "Op basis van een persoonlijke ervaring",
            "Op basis van een vergelijking met vroeger",
        ],
        0,
        "Er wordt naar onderzoek verwezen. Dan vraag je: wie, bij wie en wie betaalde?",
    ),
    tabel(
        "Klopt dit over debatteren?",
        [
            ("Je speelt in op wat je gesprekspartner zegt.", J),
            ("Je werkt enkel je eigen lijstje argumenten af.", F),
            ("Je weerlegt door te tonen waarom een argument niet opgaat.", J),
        ],
        "Wie enkel zijn eigen lijstje afwerkt, voert geen gesprek.",
    ),
    keuze(
        "\"Moeten\", \"zouden\" en \"horen te\" wijzen in een zin vaak op een [[*mening|feit|tegenargument]].",
        "Zulke woorden drukken uit wat iemand wenselijk vindt.",
    ),
    mk(
        "Twee zinnen: \"Scholen moeten later beginnen.\" en \"Tieners vallen pas laat in slaap.\" Wat is wat?",
        [
            "Eerst de stelling, dan een argument",
            "Eerst een argument, dan de stelling",
            "Allebei zijn het feiten",
            "Allebei zijn het tegenargumenten",
        ],
        0,
        "De eerste zegt wat er moet gebeuren, de tweede geeft de reden.",
    ),
    tabel(
        "Klopt dit over feiten en meningen?",
        [
            ("Een opiniestuk mag vol meningen staan.", J),
            ("Een mening hoort nooit in een tekst.", F),
            ("Een betoog dat enkel op meningen steunt, heeft weinig grond.", J),
        ],
        "Het punt is dat je weet welke van de twee je voor je hebt.",
    ),
    keuze(
        "\"Hij liegt niet, want hij spreekt altijd de waarheid\" is een [[*cirkelredenering|vergelijking|hellend vlak]].",
        "De stelling dient als argument voor zichzelf.",
    ),
    open_(
        "Neem de stelling \"Gsm's horen niet in de klas\". Geef een argument, een tegenargument en een weerlegging van dat tegenargument.",
        "Argument: meldingen leiden af en verminderen de concentratie. Tegenargument: met een gsm kan je snel iets opzoeken. Weerlegging: daarvoor kan de school laptops of tablets voorzien die enkel voor de les gebruikt worden.",
    ),
]
