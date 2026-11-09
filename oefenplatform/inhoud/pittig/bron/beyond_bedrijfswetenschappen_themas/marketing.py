"""Marketingstrategie en de marketingmix — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import plc_zone

PRENTEN = [
    dict(bestand="productlevenscyclus.svg", zelf=True,
         wat="Omzetcurve van de productlevenscyclus in vijf genummerde fasen.",
         vragen="klikvragen en een tabel over de productlevenscyclus"),
]

VRAGEN = [
    klik(
        "Klik op de fase van de productlevenscyclus waarin de omzet het snelst stijgt en er steeds meer concurrenten bijkomen.",
        "productlevenscyclus.svg",
        [plc_zone(2)],
        "De groeifase (fase 3): het product slaat aan en concurrenten springen op de kar.",
    ),
    klik(
        "Klik op de fase waarin het product al bestaat, maar er nog geen omzet is.",
        "productlevenscyclus.svg",
        [plc_zone(0)],
        "De ontwikkelingsfase (fase 1): onderzoek en ontwerp kosten geld, maar er wordt nog niets verkocht.",
    ),
    met_prent("productlevenscyclus.svg", tabel(
        "In welke fase past elke beslissing het best?",
        [
            ("Veel reclame om het product bekend te maken", "Fase 2"),
            ("Het assortiment uitbreiden met nieuwe smaken om concurrenten voor te blijven", "Fase 3"),
            ("Kosten drukken en de klanten zo lang mogelijk vasthouden", "Fase 4"),
            ("Het product stilaan uit de rekken halen", "Fase 5"),
        ],
        "Eerst bekendheid opbouwen, dan uitbreiden, dan de positie verdedigen en tot slot afbouwen.",
        kolommen=["Fase 2", "Fase 3", "Fase 4", "Fase 5"],
    )),
    tabel(
        "Welke P van de marketingmix verandert bij elke beslissing?",
        [
            ("Een frisdrank komt voortaan ook in blik", "Product"),
            ("Tijdelijk 20 % korting bij aankoop van twee stuks", "Prijs"),
            ("De frisdrank wordt ook verkocht in tankstations", "Plaats"),
            ("Een reclamefilmpje op sociale media", "Promotie"),
        ],
        "Product, prijs, plaats en promotie zijn de vier instrumenten van de marketingmix.",
        kolommen=["Product", "Prijs", "Plaats", "Promotie"],
    ),
    koppel(
        "Welke C hoort bij welke P? De 4 C's bekijken de marketingmix vanuit de klant.",
        [
            ["Product", "Customer value: wat heeft de klant eraan?"],
            ["Prijs", "Cost: wat kost het de klant in totaal?"],
            ["Plaats", "Convenience: hoe makkelijk kan de klant het kopen?"],
            ["Promotie", "Communication: tweerichtingsverkeer met de klant"],
        ],
        ["Competition: wat doet de concurrent?"],
        "Elke P krijgt een tegenhanger vanuit het standpunt van de klant.",
    ),
    tabel(
        "Gaat het om B2B, B2C, C2C of C2B?",
        [
            ("Een particulier verkoopt zijn oude fiets via een tweedehandssite aan een andere particulier", "C2C"),
            ("Een bakkerij koopt bloem bij een groothandel", "B2B"),
            ("Een fotograaf verkoopt zijn foto's aan een reclamebureau", "C2B"),
            ("Een kledingketen verkoopt een trui aan een klant", "B2C"),
        ],
        "B staat voor business, C voor consumer. De eerste letter verkoopt, de tweede koopt.",
        kolommen=["B2B", "B2C", "C2C", "C2B"],
    ),
    tabel(
        "Is het een convenience, shopping, speciality of unsought goed voor de meeste mensen?",
        [
            ("Een brood bij de bakker om de hoek", "Convenience"),
            ("Een nieuwe winterjas, na vergelijken in drie winkels", "Shopping"),
            ("Een uurwerk van één bepaald luxemerk waar je speciaal voor naar de stad rijdt", "Speciality"),
            ("Een uitvaartverzekering", "Unsought"),
        ],
        "Convenience: snel en zonder nadenken. Shopping: vergelijken. Speciality: één merk, moeite doen. Unsought: je zoekt het niet uit jezelf.",
        kolommen=["Convenience", "Shopping", "Speciality", "Unsought"],
    ),
    mk(
        "Een fabrikant van verf verkoopt dezelfde verf aan particulieren en aan schildersbedrijven. Wanneer is de verf een industrieel goed?",
        [
            "Als een schildersbedrijf ze koopt om er zijn diensten mee te leveren",
            "Als ze in een grote pot van tien liter zit, die particulieren zelden kopen",
            "Als ze duurder is dan 100 euro per pot, want dan is het geen consumentengoed meer",
            "Nooit, want verf is altijd een consumentengoed, wie ze ook koopt",
        ],
        0,
        "Niet het product zelf, maar het gebruik bepaalt het: een bedrijf dat het gebruikt om te produceren, koopt een industrieel goed.",
    ),
    mk(
        "Een supermarkt verkoopt 12 soorten koffie en 400 andere productgroepen. Een koffiespeciaalzaak verkoopt 150 soorten koffie en niets anders. Wat klopt?",
        [
            "De supermarkt heeft een breed, de speciaalzaak een diep assortiment",
            "De supermarkt heeft een diep, de speciaalzaak een breed assortiment",
            "Beide hebben een smal en ondiep assortiment",
            "Breedte en diepte zijn hier gelijk",
        ],
        0,
        "Breedte: hoeveel productgroepen. Diepte: hoeveel varianten binnen één groep.",
    ),
    tabel(
        "Is het een A-merk of een winkelmerk, en welk soort winkelmerk?",
        [
            ("Een bekend merk dat in alle supermarkten ligt", "A-merk"),
            ("Het gewone huismerk van een supermarktketen, iets goedkoper dan het A-merk", "Standaard winkelmerk"),
            ("De goedkoopste lijn van de supermarkt, met een sobere verpakking", "Budgetmerk"),
            ("De lijn van de supermarkt met producten uit biologische teelt", "Biomerk"),
        ],
        "Winkelmerken horen bij de keten zelf. Ze bestaan in een standaard-, een budget- en een biolijn.",
        kolommen=["A-merk", "Standaard winkelmerk", "Budgetmerk", "Biomerk"],
    ),
    tabel(
        "Welke merkstrategie is het?",
        [
            ("Een chocolademerk brengt een nieuwe smaak uit onder dezelfde naam", "Lijnextensie"),
            ("Een chocolademerk brengt ijsjes uit onder zijn bekende naam", "Merkextensie"),
            ("Een fabrikant verkoopt drie verschillende merken wasmiddel in dezelfde winkel", "Multibrands"),
            ("Een fabrikant lanceert een volledig nieuwe naam voor een nieuw soort product", "Nieuw merk"),
        ],
        "Lijnextensie blijft in dezelfde productgroep, merkextensie stapt met de naam naar een andere.",
        kolommen=["Lijnextensie", "Merkextensie", "Multibrands", "Nieuw merk"],
    ),
    mk(
        "Een nieuwe smartwatch komt op de markt aan een hoge prijs. Na een jaar daalt de prijs stap voor stap. Welke prijsstrategie is dit, en waarom werkt ze hier?",
        [
            "Afroomprijs: fans betalen eerst veel voor een vernieuwend product",
            "Penetratieprijs: een lage prijs om snel veel klanten te winnen",
            "Penetratieprijs: de prijs daalt omdat het product mislukt",
            "Afroomprijs: de prijs blijft voor altijd hoog",
        ],
        0,
        "Bij afromen vraag je eerst de hoogste prijs aan wie het product meteen wil, en verlaag je later voor de grote groep.",
    ),
    mk(
        "Een nieuw merk frisdrank wil snel een groot marktaandeel in een markt met veel concurrenten. Welke prijs past het best?",
        ["Een penetratieprijs", "Een afroomprijs", "De hoogste prijs van de markt", "Een prijs die elke week verandert"],
        0,
        "Met een lage instapprijs trek je snel veel klanten weg bij de concurrentie.",
    ),
    tabel(
        "Welke distributie past bij elk product?",
        [
            ("Kauwgom", "Intensief"),
            ("Een merk van dure hifi-installaties, enkel bij erkende vakhandels", "Selectief"),
            ("Een sportwagen van een exclusief merk, één dealer per regio", "Exclusief"),
        ],
        "Hoe gewoner het product, hoe meer verkooppunten. Hoe exclusiever, hoe minder.",
        kolommen=["Intensief", "Selectief", "Exclusief"],
    ),
    sorteer(
        "Is het een push- of een pullstrategie?",
        ["Push", "Pull"],
        [
            ["De fabrikant geeft supermarkten extra korting als ze zijn product vooraan zetten", "Push"],
            ["De fabrikant maakt tv-reclame zodat klanten in de winkel naar het product vragen", "Pull"],
            ["Vertegenwoordigers bezoeken winkels met een speciale actie", "Push"],
            ["Een influencer toont het product aan haar volgers", "Pull"],
        ],
        "Push duwt het product via de tussenhandel naar de klant. Pull laat de klant zelf vragen, zodat de handel het moet inslaan.",
    ),
    keuze(
        "Met [[*SEO|SEA|een buyer persona]] zorg je dat je website hoger komt in de gewone zoekresultaten, zonder te betalen per klik. Met [[*SEA|SEO|e-commerce]] betaal je om als advertentie bovenaan te staan.",
        "SEO = zoekmachineoptimalisatie, SEA = zoekmachineadverteren.",
    ),
    volgorde(
        "Zet de fasen van de customer journey in de juiste volgorde.",
        ["Bewustwording", "Overweging", "Aankoop", "Service", "Loyaliteit"],
        "De klant ontdekt, vergelijkt, koopt, gebruikt met hulp van de service en komt terug als hij tevreden is.",
    ),
    tabel(
        "In welke fase van de customer journey hoort elk contactmoment?",
        [
            ("Een advertentie op sociale media die je voor het eerst het merk toont", "Bewustwording"),
            ("Reviews lezen en prijzen vergelijken", "Overweging"),
            ("De betaalpagina van de webwinkel", "Aankoop"),
            ("Een chat met de klantendienst over een defect", "Service"),
        ],
        "De klant komt op veel momenten met het merk in aanraking, van de eerste kennismaking tot na de aankoop.",
        kolommen=["Aankoop", "Service", "Bewustwording", "Overweging"],
    ),
    mk(
        "Wat is het verschil tussen een doelgroep en een buyer persona?",
        [
            "Een buyer persona is een fictief portret van één typische klant uit de doelgroep",
            "Een doelgroep is één bepaalde persoon, een buyer persona is een grote groep klanten",
            "Een buyer persona is een echte klant die de onderneming betaalt om reclame te maken",
            "Er is geen verschil: beide woorden betekenen de hele markt van een product",
        ],
        0,
        "De persona krijgt een naam, een leeftijd, gewoonten en noden, zodat je marketing gerichter wordt.",
    ),
    mk(
        "Een onderneming kiest als strategie: \"de goedkoopste aanbieder van fietsen voor studenten\". Welke marketingmix past daarbij?",
        [
            "Eenvoudige fietsen, lage prijs, verkoop online en dicht bij hogescholen, promotie via sociale media",
            "Luxefietsen, een hoge prijs, één exclusieve winkel in de stad en reclame in modebladen",
            "Fietsen op maat, een afroomprijs, enkel verkoop op beurzen en folders bij tandartsen",
            "Elektrische racefietsen, een penetratieprijs, verkoop via juweliers en reclame op de radio",
        ],
        0,
        "De vier P's moeten samen de strategie ondersteunen: lage kosten, voor studenten, waar studenten zijn.",
    ),
    sleep(
        "Na de ontwikkeling volgen in de productlevenscyclus de [[introductie]], de groei, de volwassenheid en tot slot de [[neergang]].",
        ["afroming", "penetratie"],
        "Elk product doorloopt die fasen, maar niet elke fase duurt even lang.",
    ),
    mk(
        "Een product zit in de volwassenheidsfase. De omzet stagneert. Welke maatregel helpt de cyclus te verlengen?",
        [
            "Een vernieuwde versie of een nieuwe toepassing lanceren",
            "Alle reclame stopzetten, want iedereen kent het product al",
            "De prijs sterk verhogen om de dalende verkoop te compenseren",
            "De distributie beperken tot één winkel om het product exclusief te maken",
        ],
        0,
        "Met een vernieuwing of een nieuwe doelgroep kan het product een nieuwe groeiperiode krijgen.",
    ),
    inv(
        "Hoe noemt men elk contactmoment tussen een klant en een merk tijdens de customer journey?",
        "touchpoint",
        "Een advertentie, een winkelbezoek, een mail van de klantendienst: allemaal touchpoints.",
    ),
    tabel(
        "Waar of niet waar over de marketingmix?",
        [
            ("Een luxemerk met een prijs onder die van de budgetmerken zou de klant verwarren.", J),
            ("De vier P's kies je los van elkaar, zonder te kijken naar de strategie.", F),
            ("Een andere doelgroep kan een andere marketingmix vragen voor hetzelfde product.", J),
        ],
        "De vier P's moeten samen één geloofwaardig verhaal vertellen voor de gekozen doelgroep.",
    ),
    mk(
        "Een producent van vlees verkoopt aan restaurants (B2B) en aan particulieren via een webwinkel (B2C). Waarin verschilt de aanpak meestal?",
        [
            "Bij B2B gaat het om grotere hoeveelheden, vaste afspraken en persoonlijke contacten",
            "Bij B2C zijn de bestellingen meestal groter en lopen de contracten langer dan bij B2B",
            "Bij B2B is reclame op televisie het belangrijkste middel om restaurants te bereiken",
            "Er is geen verschil, want vlees blijft vlees, wie het ook koopt",
        ],
        0,
        "Bedrijven kopen rationeler, in grotere volumes en vaak met langlopende contracten.",
    ),
    mk(
        "Een webwinkel stuurt klanten een week na hun aankoop een mail met tips en een kortingscode voor een volgende bestelling. Welke fase van de customer journey wil ze zo versterken?",
        ["Loyaliteit", "Bewustwording", "Overweging", "Aankoop"],
        0,
        "Ze wil dat tevreden klanten terugkomen: dat is loyaliteit.",
    ),
    open_(
        "Een nieuw merk sportdrank richt zich op jongeren die aan sport doen. Stel voor elke P van de marketingmix één concrete keuze voor.",
        "Product: een drank zonder toegevoegde suikers in een herbruikbare fles. Prijs: iets goedkoper dan de bekende merken. Plaats: sportclubs, fitnesszalen en supermarkten. Promotie: samenwerking met jonge sporters op sociale media.",
        "De keuzes moeten bij elkaar en bij de doelgroep passen.",
    ),
    casus(
        "Chocolatier Cacao verkoopt pralines in eigen winkels in drie steden. Ze wil een nieuwe lijn met chocoladerepen lanceren onder dezelfde naam, en die ook in supermarkten verkopen.",
        [
            mk(
                "Welke merkstrategie is dit?",
                ["Merkextensie", "Lijnextensie", "Multibrands", "Een winkelmerk"],
                0,
                "Ze gebruikt haar bekende naam voor een ander soort product: van pralines naar repen.",
            ),
            mk(
                "Hoe verandert haar distributie?",
                [
                    "Van exclusief naar veel intensiever",
                    "Van intensief naar exclusief",
                    "Ze blijft gelijk",
                    "Van selectief naar enkel online",
                ],
                0,
                "Van eigen winkels naar supermarkten: veel meer verkooppunten.",
            ),
            tabel(
                "Welke risico's en kansen horen bij deze stap?",
                [
                    ("Meer klanten leren het merk kennen.", J),
                    ("Het luxe-imago van de pralines kan lijden onder repen in de supermarkt.", J),
                    ("De repen worden automatisch speciality goods.", F),
                ],
                "Een merkextensie kan de naam versterken of verzwakken. Repen in de supermarkt zijn eerder convenience goods.",
            ),
        ],
    ),
]
