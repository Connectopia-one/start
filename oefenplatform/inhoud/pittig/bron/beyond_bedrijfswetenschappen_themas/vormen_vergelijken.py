"""Ondernemingsvormen vergelijken — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

PRENTEN = []

VRAGEN = [
    tabel(
        "Kies voor elk kenmerk de juiste ondernemingsvorm.",
        [
            ("Minstens drie oprichters bij de start", "cv"),
            ("Een minimumkapitaal van 61 500 euro", "nv"),
            ("Geen rechtspersoonlijkheid, wel minstens twee vennoten", "maatschap"),
            ("Eén oprichter volstaat, zonder minimumkapitaal", "bv"),
        ],
        "De cv vraagt drie oprichters, de nv als enige nog een minimumkapitaal. De maatschap is een overeenkomst tussen minstens twee mensen. De bv kan één persoon alleen oprichten.",
        kolommen=["bv", "nv", "cv", "maatschap"],
    ),
    mk(
        "Sara start een bv zonder minimumkapitaal. Wat moet ze bij de oprichting toch voorleggen aan de notaris?",
        [
            "Een financieel plan en een toereikend aanvangsvermogen",
            "Een bewijs dat ze al drie jaar als zelfstandige werkt",
            "Een lijst van minstens drie andere aandeelhouders voor later",
            "Een attest van de Nationale Bank met haar jaarrekening van vorig jaar",
        ],
        0,
        "Het minimumkapitaal verdween, maar de oprichters moeten aantonen dat het startvermogen volstaat voor de geplande activiteit.",
    ),
    tabel(
        "Kan een schuldeiser van de onderneming het privévermogen van de eigenaar aanspreken?",
        [
            ("Een leverancier van een eenmanszaak", J),
            ("Een bank die geld leende aan een nv", F),
            ("Een klant met een schadeclaim tegen een maatschap", J),
            ("Een verhuurder van een kantoor van een cv", F),
        ],
        "Bij de eenmanszaak en de maatschap sta je met je privévermogen in. De bv, de nv en de cv zijn rechtspersonen met beperkte aansprakelijkheid.",
    ),
    mk(
        "Tom heeft een eenmanszaak die failliet gaat met 40 000 euro schulden. Hij heeft 15 000 euro op zijn privérekening. Wat gebeurt er met dat spaargeld?",
        [
            "Zijn schuldeisers kunnen het gebruiken om de schulden te betalen",
            "Het blijft volledig van hem, want enkel de zaak zelf is failliet",
            "Het gaat naar de staat als boete voor het faillissement",
            "Het wordt verdeeld onder zijn personeel als ontslagvergoeding",
        ],
        0,
        "Een eenmanszaak heeft geen eigen vermogen los van de ondernemer: zijn privévermogen staat mee in voor de schulden van de zaak.",
    ),
    sorteer(
        "Is de vorm een rechtspersoon of niet?",
        ["Rechtspersoon", "Geen rechtspersoon"],
        [
            ["Besloten vennootschap", "Rechtspersoon"],
            ["Naamloze vennootschap", "Rechtspersoon"],
            ["Coöperatieve vennootschap", "Rechtspersoon"],
            ["Maatschap", "Geen rechtspersoon"],
            ["Eenmanszaak", "Geen rechtspersoon"],
        ],
        "Een rechtspersoon heeft zelf rechten en plichten. De maatschap en de eenmanszaak hebben dat niet.",
    ),
    keuze(
        "Een nv wordt opgericht met een [[*authentieke|onderhandse|mondelinge]] akte, en haar winst wordt belast in de [[*vennootschapsbelasting|personenbelasting|rechtspersonenbelasting]].",
        "De notaris maakt de akte op. Als rechtspersoon betaalt de nv zelf belasting op haar winst.",
    ),
    mk(
        "Drie vrienden willen samen een fietsenwinkel beginnen. Ze willen hun huis niet riskeren en hebben samen maar 5 000 euro. Welke vormen komen in aanmerking? Duid alle juiste antwoorden aan.",
        [
            "Een bv",
            "Een cv",
            "Een nv",
            "Een maatschap",
        ],
        [0, 1],
        "Bv en cv geven beperkte aansprakelijkheid zonder minimumkapitaal. Voor een nv is 61 500 euro nodig, en bij een maatschap riskeren ze hun privévermogen.",
    ),
    koppel(
        "Welke vorm past bij elke situatie?",
        [
            ["Een beursgenoteerd bedrijf met duizenden aandeelhouders die vlot willen verkopen", "nv"],
            ["Een bakker die alleen werkt en geen vennootschap wil", "eenmanszaak"],
            ["Twee kinesisten die samen een praktijk huren zonder rechtspersoon", "maatschap"],
            ["Een energieproject van buurtbewoners die samen beslissen", "cv"],
        ],
        ["vzw"],
        "Vrij overdraagbare aandelen passen bij de nv. Samenwerking tussen veel leden past bij de cv. Wie alleen en zonder vennootschap werkt, heeft een eenmanszaak.",
    ),
    tabel(
        "Waar of niet waar over de boekhouding?",
        [
            ("Een kleine eenmanszaak mag een enkelvoudige boekhouding voeren.", J),
            ("Een cv moet een dubbele boekhouding voeren.", J),
            ("Een bv mag kiezen voor een enkelvoudige boekhouding als ze klein is.", F),
            ("Een nv legt haar jaarrekening neer bij de Nationale Bank.", J),
        ],
        "Elke vennootschap met rechtspersoonlijkheid voert een dubbele boekhouding, hoe klein ook. Alleen kleine eenmanszaken mogen het eenvoudiger doen.",
    ),
    mk(
        "Lien heeft aandelen in een bv en wil ze verkopen aan haar buurman. De statuten zeggen er niets over. Wat geldt dan?",
        [
            "De andere aandeelhouders moeten eerst akkoord gaan",
            "Ze mag ze vrij verkopen, zoals bij elke vennootschap",
            "Aandelen van een bv kunnen nooit verkocht worden",
            "Enkel de notaris beslist of de verkoop doorgaat",
        ],
        0,
        "Bij de bv is de overdracht aan buitenstaanders standaard beperkt. De statuten kunnen dat wel anders regelen.",
    ),
    inv(
        "Hoeveel oprichters heeft een nv minstens nodig? Antwoord met een getal.",
        "1",
        "Eén oprichter volstaat voor een nv. Het minimumkapitaal van 61 500 euro blijft wel.",
    ),
    tabel(
        "Kies voor elk kenmerk de juiste vorm.",
        [
            ("Aandelen zijn in principe vrij overdraagbaar", "nv"),
            ("De winst valt bij elke vennoot in de personenbelasting", "maatschap"),
            ("Aandelen gaan zonder andere regeling enkel vlot naar andere aandeelhouders", "cv"),
        ],
        "Bij de nv circuleren aandelen vrij. Bij de cv blijft de groep van leden normaal gesloten. De maatschap is fiscaal doorzichtig: elke vennoot geeft zijn deel aan.",
        kolommen=["nv", "cv", "maatschap"],
    ),
    mk(
        "Waarom kiest een ondernemer met een hoge winst vaak voor een vennootschap in plaats van een eenmanszaak?",
        [
            "Het tarief van de vennootschapsbelasting ligt lager dan de hoogste schijf van de personenbelasting",
            "Een vennootschap hoeft nooit belasting te betalen op haar winst",
            "Een vennootschap hoeft geen boekhouding bij te houden",
            "In een vennootschap moet je geen voorafbetalingen doen",
        ],
        0,
        "In de personenbelasting stijgt het tarief tot 50 %. De vennootschapsbelasting heeft een vast tarief van 25 %, met een verlaagd tarief voor kleine vennootschappen.",
    ),
    sleep(
        "Een eenmanszaak heeft geen [[rechtspersoonlijkheid]]. De ondernemer is daardoor [[onbeperkt]] aansprakelijk, en zijn winst valt in de [[personenbelasting]].",
        ["beperkt", "vennootschapsbelasting"],
        "Zonder rechtspersoon vallen zaak en ondernemer samen, ook fiscaal.",
    ),
    mk(
        "Een maatschap heeft schulden die ze niet kan betalen. Wie moet ze uiteindelijk betalen?",
        [
            "De vennoten, ook met hun eigen vermogen",
            "Niemand, want een maatschap is geen persoon",
            "Enkel de vennoot die de schuld aanging, alleen met zijn inbreng",
            "De notaris die de akte opmaakte",
        ],
        0,
        "Een maatschap heeft geen eigen rechtspersoonlijkheid, dus de vennoten staan zelf in voor de schulden.",
    ),
    sorteer(
        "Welke akte is nodig om de vorm op te richten?",
        ["Authentieke akte", "Geen authentieke akte nodig"],
        [
            ["bv", "Authentieke akte"],
            ["nv", "Authentieke akte"],
            ["cv", "Authentieke akte"],
            ["Maatschap", "Geen authentieke akte nodig"],
            ["Eenmanszaak", "Geen authentieke akte nodig"],
        ],
        "Voor de drie vennootschappen met rechtspersoonlijkheid moet de notaris de akte opmaken.",
    ),
    mk(
        "Een leerling zegt: \"Een bv is altijd beter dan een eenmanszaak, want je bent beperkt aansprakelijk.\" Wat is de beste reactie?",
        [
            "Er zijn ook nadelen: een notarisakte, een dubbele boekhouding en meer kosten",
            "Klopt, een eenmanszaak heeft enkel nadelen en geen enkel voordeel",
            "Fout, want een bv is net onbeperkt aansprakelijk",
            "Klopt, want een bv betaalt nooit belasting op haar winst",
        ],
        0,
        "Een eenmanszaak is eenvoudig en goedkoop te starten. Een vennootschap beschermt je privévermogen, maar vraagt meer formaliteiten.",
    ),
    volgorde(
        "Rangschik van minst naar meest formaliteiten bij de start.",
        ["Eenmanszaak", "Maatschap", "bv", "nv"],
        "De eenmanszaak schrijft zich gewoon in. De maatschap is een overeenkomst. De bv vraagt een notaris en een financieel plan, de nv daarbovenop een minimumkapitaal.",
    ),
    tabel(
        "Is er een notaris nodig?",
        [
            ("Twee artsen richten een maatschap op", F),
            ("Een webshop wordt een bv", J),
            ("Een schrijnwerker start als zelfstandige in eigen naam", F),
            ("Een groep landbouwers richt een cv op", J),
        ],
        "Enkel voor de bv, de nv en de cv is een authentieke akte verplicht.",
    ),
    tabel(
        "In welke belasting valt de winst van de onderneming?",
        [
            ("De winst van een eenmanszaak", "Personenbelasting"),
            ("De winst van een bv", "Vennootschapsbelasting"),
            ("De winst van een maatschap", "Personenbelasting"),
            ("De winst van een cv", "Vennootschapsbelasting"),
        ],
        "Een rechtspersoon betaalt zelf vennootschapsbelasting. Zonder rechtspersoon valt de winst bij de ondernemer of de vennoten.",
        kolommen=["Personenbelasting", "Vennootschapsbelasting"],
    ),
    mk(
        "Met welke vormen kan één persoon helemaal alleen starten? Duid alle juiste antwoorden aan.",
        ["De eenmanszaak", "De bv", "De nv", "De cv", "De maatschap"],
        [0, 1, 2],
        "De cv vraagt drie oprichters en de maatschap minstens twee vennoten. Bv en nv kan je alleen oprichten.",
    ),
    mk(
        "Welke uitspraak over de cv klopt?",
        [
            "Ze heeft minstens drie oprichters en een coöperatief doel",
            "Ze heeft geen rechtspersoonlijkheid, zoals de maatschap",
            "Ze moet minstens 61 500 euro kapitaal hebben",
            "Ze mag een enkelvoudige boekhouding voeren",
        ],
        0,
        "De cv is een rechtspersoon zonder minimumkapitaal, met dubbele boekhouding en minstens drie oprichters.",
    ),
    keuze(
        "Bij een maatschap is er [[*geen|een beperkte|een volledige]] rechtspersoonlijkheid, dus de winst wordt belast bij [[*de vennoten|de maatschap|de notaris]].",
        "De maatschap is fiscaal doorzichtig: de winst wordt verdeeld en elke vennoot geeft zijn deel aan.",
    ),
    mk(
        "Een eenmanszaak maakt 120 000 euro winst. Wat is het grootste nadeel fiscaal tegenover een bv met dezelfde winst?",
        [
            "Het progressieve tarief: een groot deel valt in de schijf van 50 %",
            "Een eenmanszaak betaalt btw op haar winst",
            "Een eenmanszaak moet elk jaar een minimumkapitaal bijstorten",
            "De winst van een eenmanszaak wordt dubbel belast",
        ],
        0,
        "De personenbelasting is progressief. De vennootschapsbelasting heeft een vlak tarief.",
    ),
    sleep(
        "In een bv, een nv en een cv riskeren de aandeelhouders enkel hun [[inbreng]]. Hun [[privévermogen]] blijft buiten schot, omdat de vennootschap een [[rechtspersoon]] is.",
        ["loon", "maatschap"],
        "Beperkte aansprakelijkheid: wat je in de vennootschap stak, kan je verliezen, de rest niet.",
    ),
    open_(
        "Leg in twee zinnen uit waarom een nv beter past bij een groot bedrijf dat naar de beurs wil dan een bv.",
        "Bij een nv zijn de aandelen vrij overdraagbaar, zodat beleggers ze makkelijk kunnen kopen en verkopen op de beurs. Bij een bv is de overdracht aan buitenstaanders standaard beperkt.",
        "Vrije overdraagbaarheid is wat een beursnotering mogelijk maakt.",
    ),
    mk(
        "Wat hebben de bv, de nv en de cv allemaal gemeen?",
        [
            "Rechtspersoonlijkheid en beperkte aansprakelijkheid",
            "Minstens drie oprichters bij de oprichting van de vennootschap",
            "Een minimumkapitaal van 61 500 euro bij de start",
            "Vrij overdraagbare aandelen voor iedereen, ook buitenstaanders",
        ],
        0,
        "Alle drie zijn rechtspersonen met beperkte aansprakelijkheid, opgericht bij de notaris en belast in de vennootschapsbelasting.",
    ),
    casus(
        "Noor en Jasper willen samen een koffiebar openen. Ze hebben 20 000 euro spaargeld. Noor heeft een huis, Jasper niet. Ze willen later misschien een derde vennoot laten instappen, maar enkel als ze allebei akkoord gaan.",
        [
            mk(
                "Welke vorm raad je hen aan?",
                [
                    "Een bv",
                    "Een nv",
                    "Een maatschap",
                    "Twee aparte eenmanszaken",
                ],
                0,
                "De bv vraagt geen minimumkapitaal, beschermt het huis van Noor en beperkt standaard de toetreding van nieuwe aandeelhouders.",
            ),
            tabel(
                "Waarom past een nv of een maatschap minder?",
                [
                    ("Voor een nv hebben ze te weinig startkapitaal.", J),
                    ("Bij een maatschap riskeert Noor haar huis.", J),
                    ("Een maatschap mag geen koffiebar uitbaten.", F),
                ],
                "Een nv vraagt 61 500 euro, een maatschap geeft geen bescherming van het privévermogen. Een maatschap mag wel een koffiebar uitbaten.",
            ),
            keuze(
                "Voor hun vennootschap moeten ze naar de [[*notaris|gemeente|rechtbank]], en ze leggen een [[*financieel plan|ondernemingsnummer|loonbrief]] voor.",
                "De notaris maakt de oprichtingsakte op. Het financieel plan toont dat het aanvangsvermogen volstaat.",
            ),
        ],
    ),
]
