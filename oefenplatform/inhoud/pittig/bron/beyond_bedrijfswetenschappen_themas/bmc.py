"""Het Business Model Canvas en de BCG-matrix — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import bmc_zone, raster_zone

PRENTEN = [
    dict(bestand="bmc.svg", zelf=True,
         wat="Leeg Business Model Canvas met de negen bouwstenen.",
         vragen="klikvragen en tabellen over het BMC"),
    dict(bestand="bcg.svg", zelf=True,
         wat="Lege BCG-matrix: marktgroei en marktaandeel.",
         vragen="klikvragen over de BCG-matrix"),
]

VRAGEN = [
    klik(
        "Een fietsenmaker verkoopt via zijn winkel, een webwinkel en een kraam op de jaarmarkt. Klik op de bouwsteen van het BMC waar dit hoort.",
        "bmc.svg",
        [bmc_zone("kanalen")],
        "Kanalen: hoe de onderneming haar klanten bereikt en levert.",
    ),
    klik(
        "De fietsenmaker werkt samen met een groothandel in onderdelen en met de gemeente voor deelfietsen. Klik op de bouwsteen waar dit hoort.",
        "bmc.svg",
        [bmc_zone("partners")],
        "Partners: andere organisaties die de onderneming nodig heeft om haar model te laten werken.",
    ),
    klik(
        "Klik op de bouwsteen die de vraag beantwoordt: welk probleem lossen we op voor de klant?",
        "bmc.svg",
        [bmc_zone("waarde")],
        "De waardepropositie staat in het midden: waarom kiest de klant voor jou?",
    ),
    met_prent("bmc.svg", tabel(
        "Een streamingdienst voor muziek vult haar BMC in. In welke bouwsteen hoort elk element?",
        [
            ("Een maandelijks abonnement en reclame bij de gratis versie", "Inkomstenstromen"),
            ("De licenties bij platenfirma's en de servers", "Kostenstructuur"),
            ("Een app en een website", "Kanalen"),
            ("Afspeellijsten op maat die je nieuwe muziek laten ontdekken", "Waardepropositie"),
        ],
        "Inkomsten en kosten staan onderaan het canvas, kanalen en waarde in het bovenste deel.",
        kolommen=["Waardepropositie", "Kanalen", "Kostenstructuur", "Inkomstenstromen"],
    )),
    met_prent("bmc.svg", tabel(
        "Hoort het element bij kernactiviteiten of bij kernmiddelen van een bakkerij?",
        [
            ("Elke nacht brood bakken", "Kernactiviteiten"),
            ("De ovens en het pand", "Kernmiddelen"),
            ("Het recept van de huisgemaakte taart", "Kernmiddelen"),
            ("Bestellingen leveren aan restaurants", "Kernactiviteiten"),
        ],
        "Activiteiten zijn wat je doet, middelen zijn wat je daarvoor nodig hebt: mensen, machines, kennis.",
        kolommen=["Kernactiviteiten", "Kernmiddelen"],
    )),
    mk(
        "Een leerling zet \"Jongeren tussen 15 en 25 die graag gamen\" bij de waardepropositie van een gamewinkel. Waar hoort het eigenlijk?",
        ["Bij de klantsegmenten", "Bij de kanalen", "Bij de partners", "Bij de kernmiddelen"],
        0,
        "Een groep klanten is een klantsegment. De waardepropositie beschrijft wat je hen biedt.",
    ),
    mk(
        "Waarom staat de waardepropositie in het midden van het canvas?",
        [
            "Alles links maakt ze mogelijk, alles rechts brengt ze bij de klant",
            "Omdat ze de grootste kost van de onderneming is en dus het meeste aandacht vraagt",
            "Omdat ze enkel voor de aandeelhouders belangrijk is",
            "Omdat ze elke maand verandert",
        ],
        0,
        "Links staat de kant van de onderneming (partners, activiteiten, middelen), rechts de kant van de klant.",
    ),
    tabel(
        "Waar of niet waar over het Business Model Canvas?",
        [
            ("Het geeft op één blad een overzicht van hoe een onderneming waarde creëert.", J),
            ("Klantrelaties gaan over hoe je contact houdt met je klanten.", J),
            ("De kostenstructuur toont hoe de onderneming geld verdient.", F),
            ("Een verandering in één bouwsteen kan andere bouwstenen beïnvloeden.", J),
        ],
        "Hoe je geld verdient, staat bij de inkomstenstromen. De bouwstenen hangen samen.",
    ),
    mk(
        "Een webwinkel beslist om ook een fysieke winkel te openen. Welke bouwstenen veranderen zeker mee? Duid alle juiste antwoorden aan.",
        ["Kanalen", "Kostenstructuur", "Kernmiddelen", "Klantsegmenten"],
        [0, 1, 2],
        "Een nieuw verkoopkanaal vraagt een pand (middel) en brengt huur en personeel (kosten) mee. De doelgroep kan dezelfde blijven.",
    ),
    mk(
        "Een gratis app verdient enkel aan reclame. Ze voert een betaalde versie zonder reclame in. Welke bouwsteen krijgt er vooral iets bij?",
        ["Inkomstenstromen", "Partners", "Kernmiddelen", "Kostenstructuur"],
        0,
        "Er komt een nieuwe manier bij om geld te verdienen: abonnementen naast reclame.",
    ),
    koppel(
        "Welke vraag beantwoordt elke bouwsteen?",
        [
            ["Voor wie creëren we waarde?", "Klantsegmenten"],
            ["Hoe bereiken we de klant?", "Kanalen"],
            ["Waarvoor willen klanten betalen?", "Inkomstenstromen"],
            ["Wat moeten we zelf goed doen?", "Kernactiviteiten"],
        ],
        ["Visie"],
        "Elke bouwsteen is een vraag die de ondernemer moet beantwoorden.",
    ),
    klik(
        "Een product heeft een groot marktaandeel in een markt die nog sterk groeit. Klik op het vak van de BCG-matrix waar het hoort.",
        "bcg.svg",
        [raster_zone(0, 0, 2, 2)],
        "Groot aandeel in een groeiende markt: een star.",
    ),
    klik(
        "Klik op het vak van de BCG-matrix met de producten die het meeste geld opleveren en weinig investeringen vragen.",
        "bcg.svg",
        [raster_zone(1, 0, 2, 2)],
        "De cash cow: groot marktaandeel in een markt die nauwelijks nog groeit.",
    ),
    met_prent("bcg.svg", tabel(
        "Waar hoort elk product van een frisdrankproducent in de BCG-matrix?",
        [
            ("Een klassieke cola, marktleider in een stabiele markt", "Cash cow"),
            ("Een nieuwe energiedrank met weinig verkoop in een snelgroeiende markt", "Question mark"),
            ("Een oude limonade die bijna niemand koopt, in een krimpende markt", "Dog"),
            ("Een suikervrije ijsthee, marktleider in een snelgroeiende markt", "Star"),
        ],
        "Twee vragen per product: groeit de markt, en is ons aandeel groot?",
        kolommen=["Star", "Cash cow", "Question mark", "Dog"],
    )),
    tabel(
        "Welk strategisch doel past meestal bij elk vak van de BCG-matrix?",
        [
            ("Star", "Investeren om de positie te behouden"),
            ("Cash cow", "Melken: geld gebruiken voor andere producten"),
            ("Question mark", "Kiezen: fors investeren of stoppen"),
            ("Dog", "Afstoten"),
        ],
        "Het geld van de cash cows financiert de stars en de veelbelovende question marks.",
        kolommen=["Investeren om de positie te behouden", "Melken: geld gebruiken voor andere producten", "Kiezen: fors investeren of stoppen", "Afstoten"],
    ),
    mk(
        "Een star verliest na enkele jaren aan groei, omdat de markt verzadigd raakt. Het marktaandeel blijft groot. Wat wordt het product?",
        ["Een cash cow", "Een dog", "Een question mark", "Het blijft een star"],
        0,
        "Groot aandeel, lage groei: de star schuift door naar cash cow.",
    ),
    mk(
        "Een onderneming heeft enkel cash cows en dogs. Wat is het grootste gevaar op lange termijn?",
        [
            "Er komen geen nieuwe groeiproducten om de cash cows later te vervangen",
            "Ze verdient vandaag te weinig geld met haar producten om nog te overleven",
            "Ze investeert te veel in nieuwe producten",
            "De markt groeit te snel voor haar",
        ],
        0,
        "Cash cows leveren nu geld op, maar zonder stars of question marks is er geen opvolging.",
    ),
    sleep(
        "De BCG-matrix zet de [[marktgroei]] uit tegen het [[marktaandeel]]. Een [[question mark]] heeft een klein aandeel in een groeiende markt.",
        ["winst", "dog", "omzet"],
        "Twee assen, vier vakken.",
    ),
    keuze(
        "Een cash cow vraagt [[*weinig|veel|geen enkele]] investeringen en levert [[*veel|weinig|geen]] geld op.",
        "Het product heeft zijn plaats veroverd in een markt die niet meer groeit.",
    ),
    mk(
        "Een question mark heeft een marktaandeel van 3 % in een markt die 20 % per jaar groeit. De onderneming heeft weinig geld. Wat is een logische keuze?",
        [
            "Kiezen: ofwel geld van een cash cow inzetten om er een star van te maken, ofwel stoppen",
            "Niets doen, want een question mark wordt vanzelf een star",
            "Het product melken zoals een cash cow",
            "De prijs verhogen zodat het marktaandeel daalt",
        ],
        0,
        "Een question mark vraagt veel geld. Zonder investering blijft het aandeel klein en wordt het later een dog.",
    ),
    volgorde(
        "Zet het typische levenspad van een succesvol product in de BCG-matrix in de juiste volgorde.",
        ["Question mark", "Star", "Cash cow", "Dog"],
        "Een nieuw product start klein in een groeiende markt, wordt marktleider, blijft leider als de groei stopt en raakt op het einde in verval.",
    ),
    sorteer(
        "Hoort het bij de linkerkant (de onderneming) of de rechterkant (de klant) van het canvas?",
        ["Kant van de onderneming", "Kant van de klant"],
        [
            ["Partners", "Kant van de onderneming"],
            ["Kernmiddelen", "Kant van de onderneming"],
            ["Klantrelaties", "Kant van de klant"],
            ["Kanalen", "Kant van de klant"],
            ["Kernactiviteiten", "Kant van de onderneming"],
            ["Klantsegmenten", "Kant van de klant"],
        ],
        "De waardepropositie verbindt beide kanten in het midden.",
    ),
    inv(
        "Hoe noemt men in de BCG-matrix een product met een klein marktaandeel in een markt die nauwelijks groeit?",
        "dog",
        "Een dog brengt weinig op en heeft weinig toekomst. Vaak is afstoten de beste keuze.",
    ),
    mk(
        "Een fitnessclub wil haar klantrelaties verbeteren. Welke maatregel hoort daarbij?",
        [
            "Een persoonlijke coach en een app met schema's op maat",
            "Een nieuwe leverancier zoeken voor de fitnesstoestellen in de zaal",
            "Een goedkoper energiecontract afsluiten voor de verwarming",
            "Een banklening aangaan voor een tweede vestiging in de stad",
        ],
        0,
        "Klantrelaties gaan over het soort contact met de klant: persoonlijk, automatisch, in een gemeenschap.",
    ),
    tabel(
        "Waar of niet waar over de BCG-matrix?",
        [
            ("Een dog kan soms toch behouden worden, bijvoorbeeld omdat klanten hem samen met andere producten kopen.", J),
            ("Een star levert altijd meer geld op dan hij kost.", F),
            ("Met de BCG-matrix beoordeel je de hele productportefeuille.", J),
        ],
        "Een star brengt veel op, maar vraagt ook veel investeringen om bij te blijven in een groeiende markt.",
    ),
    open_(
        "Vul voor een schoolcafetaria drie bouwstenen van het BMC in: klantsegmenten, waardepropositie en inkomstenstromen.",
        "Klantsegmenten: leerlingen en leerkrachten van de school. Waardepropositie: snel een gezonde en betaalbare lunch zonder de school te verlaten. Inkomstenstromen: verkoop van broodjes, soep en drank, eventueel een abonnement per trimester.",
        "De drie bouwstenen moeten bij elkaar passen: wat je biedt, voor wie, en hoe je ervoor betaald wordt.",
    ),
    mk(
        "Een onderneming haalt veel geld uit haar cash cow. Waar zet ze dat geld volgens de BCG-logica best in?",
        [
            "In stars en veelbelovende question marks",
            "In de dogs, om hun marktaandeel op te krikken",
            "Volledig in de cash cow zelf",
            "Nergens: het blijft op de bank staan",
        ],
        0,
        "De cash cow financiert de groeiers van morgen.",
    ),
    casus(
        "Zuivelbedrijf Melkweg heeft vier producten: halfvolle melk (marktleider, markt stabiel), plantaardige yoghurt (klein aandeel, markt groeit snel), chocolademelk in glazen fles (klein aandeel, markt krimpt) en eiwitpudding (marktleider, markt groeit snel).",
        [
            tabel(
                "Plaats elk product in de BCG-matrix.",
                [
                    ("Halfvolle melk", "Cash cow"),
                    ("Plantaardige yoghurt", "Question mark"),
                    ("Chocolademelk in glazen fles", "Dog"),
                    ("Eiwitpudding", "Star"),
                ],
                "Telkens: groeit de markt, en is het aandeel groot?",
                kolommen=["Star", "Cash cow", "Question mark", "Dog"],
            ),
            mk(
                "Welk product levert waarschijnlijk het geld om de plantaardige yoghurt te laten groeien?",
                ["De halfvolle melk", "De chocolademelk", "De eiwitpudding", "De plantaardige yoghurt zelf"],
                0,
                "De cash cow brengt veel op en vraagt weinig investeringen.",
            ),
            mk(
                "Welke beslissing past bij de chocolademelk in glazen fles?",
                [
                    "Afbouwen of verkopen, tenzij ze om een andere reden nodig is",
                    "Fors investeren in een grote reclamecampagne op televisie en op sociale media",
                    "Een nieuwe fabriek bouwen enkel voor de glazen flessen",
                    "De productie verdubbelen",
                ],
                0,
                "Een dog in een krimpende markt heeft weinig toekomst.",
            ),
        ],
    ),
]
