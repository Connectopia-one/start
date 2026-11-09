"""Financieringsvormen — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import raster_zone

PRENTEN = [
    dict(bestand="financieringsvormen.svg", zelf=True,
         wat="Schema eigen of vreemd vermogen, korte of lange termijn, met drie vakken met een vraagteken.",
         vragen="klikvragen en een sorteervraag over financieringsvormen"),
]

VRAGEN = [
    klik(
        "Een onderneming gebruikt een kaskrediet om een drukke maand te overbruggen. Klik op het vak waar deze financiering hoort.",
        "financieringsvormen.svg",
        [raster_zone(1, 0, 2, 2)],
        "Een kaskrediet komt van de bank (vreemd vermogen) en is bedoeld voor korte tijd.",
    ),
    klik(
        "Een nv geeft nieuwe aandelen uit en de aandeelhouders storten geld. Klik op het vak waar deze financiering hoort.",
        "financieringsvormen.svg",
        [raster_zone(0, 1, 2, 2)],
        "Een kapitaalverhoging is eigen vermogen. Dat blijft in de onderneming en hoeft niet terugbetaald te worden.",
    ),
    met_prent("financieringsvormen.svg", tabel(
        "In welk vak van het schema hoort elke financieringsvorm?",
        [
            ("Zelffinanciering: winst in de reserves laten", "Eigen, lange termijn"),
            ("Een obligatielening op acht jaar", "Vreemd, lange termijn"),
            ("Leverancierskrediet", "Vreemd, korte termijn"),
            ("Een hypothecaire lening voor een magazijn", "Vreemd, lange termijn"),
            ("Een straight loan van drie maanden", "Vreemd, korte termijn"),
        ],
        "Eigen vermogen komt van de eigenaars. Leningen en uitstel van betaling zijn vreemd vermogen, kort of lang.",
        kolommen=["Eigen, lange termijn", "Vreemd, korte termijn", "Vreemd, lange termijn"],
    )),
    tabel(
        "Is het een voordeel van eigen vermogen of van vreemd vermogen?",
        [
            ("Er moet geen interest betaald worden, ook niet in een slecht jaar.", "Eigen vermogen"),
            ("De eigenaars hoeven hun zeggenschap niet te delen.", "Vreemd vermogen"),
            ("Interest is fiscaal aftrekbaar als kost.", "Vreemd vermogen"),
            ("Het hoeft nooit terugbetaald te worden.", "Eigen vermogen"),
        ],
        "Eigen vermogen is veilig maar deelt de zeggenschap en de winst. Vreemd vermogen kost interest, maar die is een aftrekbare kost.",
        kolommen=["Eigen vermogen", "Vreemd vermogen"],
    ),
    mk(
        "Een nv haalt 500 000 euro op met 500 obligaties van 1 000 euro aan 4 % per jaar, terug te betalen na zes jaar. Hoeveel interest betaalt ze per jaar?",
        ["20 000 euro", "40 000 euro", "2 000 euro", "120 000 euro"],
        0,
        "500 000 · 0,04 = 20 000 euro per jaar. Het kapitaal wordt pas op het einde in één keer terugbetaald.",
    ),
    mk(
        "Een onderneming neemt een straight loan van 60 000 euro voor drie maanden aan 6 % per jaar. Hoeveel interest betaalt ze?",
        ["900 euro", "3 600 euro", "1 800 euro", "300 euro"],
        0,
        "60 000 · 0,06 · 3/12 = 900 euro.",
    ),
    mk(
        "Een onderneming verkoopt 100 000 euro aan klantenfacturen aan een factor. De factor betaalt meteen 80 % en rekent 2 % commissie op het factuurbedrag. Hoeveel krijgt de onderneming meteen, en hoeveel kost de factor?",
        [
            "80 000 euro meteen, de factor kost 2 000 euro",
            "98 000 euro meteen, de factor kost 2 000 euro",
            "78 000 euro meteen, de factor kost 20 000 euro",
            "100 000 euro meteen, de factor kost niets",
        ],
        0,
        "Het voorschot is 80 % van 100 000 euro. De commissie is 2 % van 100 000 euro. De rest krijgt ze als de klanten betaald hebben.",
    ),
    tabel(
        "Gaat het om financiële of operationele leasing?",
        [
            ("Een huurcontract met de mogelijkheid om op het einde te kopen", "Financiële leasing"),
            ("De leasinggever zorgt voor onderhoud en vervangt de wagen na drie jaar", "Operationele leasing"),
            ("De leasingnemer draagt de risico's van het goed", "Financiële leasing"),
            ("Het lijkt sterk op gewoon huren", "Operationele leasing"),
        ],
        "Bij financiële leasing financier je in feite een aankoop. Operationele leasing is een vorm van huur met dienstverlening.",
        kolommen=["Financiële leasing", "Operationele leasing"],
    ),
    mk(
        "Wat is het belangrijkste verschil tussen crowdfunding en crowdlending?",
        [
            "Bij crowdlending moet de onderneming het geld met interest terugbetalen",
            "Crowdfunding gebeurt altijd via een bank, crowdlending enkel via een internetplatform",
            "Bij crowdfunding krijgen de gevers altijd aandelen en dus stemrecht in de onderneming",
            "Crowdlending is wettelijk enkel toegelaten voor vzw's en niet voor vennootschappen",
        ],
        0,
        "Bij crowdfunding geven mensen vaak in ruil voor een product of tegenprestatie. Crowdlending is een lening van veel particulieren.",
    ),
    sorteer(
        "Past de financieringsvorm bij een kortlopende of bij een langlopende behoefte?",
        ["Kortlopende behoefte", "Langlopende behoefte"],
        [
            ["Een seizoenspiek in de voorraad", "Kortlopende behoefte"],
            ["Een nieuwe productiehal", "Langlopende behoefte"],
            ["Klanten die traag betalen", "Kortlopende behoefte"],
            ["Een machine die tien jaar meegaat", "Langlopende behoefte"],
        ],
        "De looptijd van de financiering hoort te passen bij hoe lang het geld vastzit.",
    ),
    koppel(
        "Welke financieringsvorm past het best bij elke situatie?",
        [
            ["Een nieuw kantoorgebouw, met het gebouw als waarborg", "Hypothecaire lening"],
            ["Een machine van tien jaar, afgelost over haar levensduur", "Investeringskrediet"],
            ["Klanten betalen pas na 60 dagen, je wil sneller geld", "Factoring"],
            ["De rekening gaat in december tijdelijk onder nul", "Kaskrediet"],
        ],
        ["Obligatielening"],
        "Elke vorm heeft haar eigen doel en looptijd.",
    ),
    keuze(
        "Bij zelffinanciering [[*houdt de onderneming winst in|leent de onderneming bij de bank|verkoopt de onderneming vorderingen]]. Dat verhoogt het [[*eigen vermogen|vreemd vermogen|klantenkrediet]].",
        "Gereserveerde winst blijft in de onderneming en kost geen interest.",
    ),
    mk(
        "De familie die 100 % van een bv bezit, wil uitbreiden maar geen zeggenschap afstaan. Ze heeft zelf geen extra geld. Welke financiering past het best?",
        [
            "Een investeringskrediet bij de bank",
            "Een kapitaalverhoging met nieuwe aandeelhouders",
            "Crowdfunding met aandelen voor de gevers",
            "Een nieuwe vennoot laten instappen",
        ],
        0,
        "Een lening geeft geen stemrecht aan de bank. Nieuwe aandeelhouders wel.",
    ),
    tabel(
        "Waar of niet waar over obligaties, leverancierskrediet en straight loans?",
        [
            ("Bij een obligatielening leent de onderneming bij het publiek.", J),
            ("Obligatiehouders worden mede-eigenaar van de onderneming.", F),
            ("Leverancierskrediet kan geld kosten, als je daardoor een betalingskorting mist.", J),
            ("Een straight loan wordt in maandelijkse schijven afgelost.", F),
        ],
        "Obligatiehouders zijn schuldeisers. Een straight loan betaal je in één keer terug op de vervaldag.",
    ),
    mk(
        "Een onderneming financiert een machine van twaalf jaar met een kaskrediet. Wat is het grootste risico?",
        [
            "Het kaskrediet moet terug lang voor de machine het geld heeft opgebracht",
            "Een kaskrediet mag niet gebruikt worden voor een onderneming",
            "De machine wordt eigendom van de bank",
            "De interest van een kaskrediet is fiscaal niet aftrekbaar",
        ],
        0,
        "Kortlopend geld voor een langlopende investering zet de liquiditeit onder druk. Een investeringskrediet past beter.",
    ),
    inv(
        "Een onderneming heeft een investeringskrediet van 120 000 euro, af te lossen in zes gelijke jaarlijkse schijven. Hoeveel euro kapitaal lost ze elk jaar af? Schrijf enkel het getal.",
        "20000",
        "120 000 / 6 = 20 000 euro per jaar, plus de interest op wat nog openstaat.",
    ),
    sleep(
        "Bij een [[hypothecaire lening]] dient een gebouw als waarborg. Bij [[factoring]] verkoopt de onderneming haar vorderingen. Bij een [[kapitaalverhoging]] komen er aandelen bij.",
        ["kaskrediet", "leasing"],
        "Drie heel verschillende manieren om aan geld te komen.",
    ),
    mk(
        "Waarom kan een starter met weinig eigen vermogen moeilijk een banklening krijgen?",
        [
            "De bank ziet weinig buffer om verliezen op te vangen en wil een waarborg",
            "Banken lenen nooit aan nieuwe ondernemingen",
            "Een starter mag wettelijk geen schulden hebben",
            "Een starter betaalt geen interest",
        ],
        0,
        "Hoe minder eigen vermogen, hoe groter het risico voor de bank. Daarom vraagt ze een waarborg of een eigen inbreng.",
    ),
    tabel(
        "Wat gebeurt er met de solvabiliteit bij elke financieringsvorm?",
        [
            ("Een kapitaalverhoging", "Stijgt"),
            ("Zelffinanciering", "Stijgt"),
            ("Een obligatielening", "Daalt"),
            ("Crowdlending", "Daalt"),
        ],
        "Eigen vermogen versterkt de solvabiliteit, elke lening verzwakt ze.",
        kolommen=["Stijgt", "Daalt"],
    ),
    mk(
        "Een leasingcontract voor een bestelwagen: drie jaar huur, onderhoud en banden inbegrepen, en daarna gaat de wagen terug. Welke leasing is dit?",
        ["Operationele leasing", "Financiële leasing", "Factoring", "Een straight loan"],
        0,
        "Geen aankoopoptie, de leasinggever blijft eigenaar en zorgt voor het onderhoud.",
    ),
    volgorde(
        "Rangschik deze leningen van kortste naar langste gebruikelijke looptijd.",
        ["Kaskrediet", "Straight loan", "Investeringskrediet voor een machine", "Hypothecaire lening voor een gebouw"],
        "Een kaskrediet is doorlopend en kort, een straight loan enkele maanden, een investeringskrediet enkele jaren en een hypothecaire lening vaak vijftien tot twintig jaar.",
    ),
    mk(
        "Een webwinkel haalt via een platform 40 000 euro op bij 400 mensen. Elk krijgt over vier jaar zijn geld terug met 5 % interest per jaar. Welke vorm is dit?",
        ["Crowdlending", "Crowdfunding met een tegenprestatie", "Een kapitaalverhoging", "Factoring"],
        0,
        "Veel particulieren lenen geld en krijgen interest: crowdlending.",
    ),
    mk(
        "Bij een kapitaalverhoging komen er nieuwe aandeelhouders bij. Wat is een nadeel voor de bestaande aandeelhouders?",
        [
            "Ze moeten de zeggenschap en de toekomstige winst delen",
            "Ze moeten interest betalen aan de nieuwe aandeelhouders",
            "Het kapitaal moet na vijf jaar terugbetaald worden",
            "De solvabiliteit daalt",
        ],
        0,
        "Meer aandelen betekent dat elk bestaand aandeel een kleiner deel van de stemmen en van het dividend vertegenwoordigt.",
    ),
    mk(
        "Een belegger twijfelt tussen aandelen en obligaties van dezelfde nv. Wat krijgt hij als obligatiehouder?",
        [
            "Een vaste interest en zijn geld terug op de vervaldag, maar geen stemrecht",
            "Stemrecht op de algemene vergadering en een deel van de winst",
            "Een dividend dat elk jaar afhangt van de winst",
            "Een deel van de gebouwen als de nv stopt, vóór de banken",
        ],
        0,
        "Een obligatie is een lening aan de nv. De belegger is schuldeiser, geen eigenaar.",
    ),
    tabel(
        "Waar of niet waar over factoring?",
        [
            ("De factor neemt de inning van de vorderingen over.", J),
            ("Na factoring staan er minder handelsvorderingen op de balans.", J),
            ("Factoring kost de onderneming niets.", F),
        ],
        "De onderneming krijgt sneller geld, maar betaalt de factor een vergoeding.",
    ),
    open_(
        "Een onderneming wil een machine van 200 000 euro kopen die tien jaar meegaat. Bespreek twee geschikte financieringsvormen met telkens een voordeel.",
        "Een investeringskrediet: de aflossing loopt mee met de levensduur van de machine, en de bank wordt geen eigenaar. Financiële leasing: je hoeft niet alles meteen te betalen en kan de machine op het einde kopen. Ook zelffinanciering kan, zonder interest, als er genoeg reserves zijn.",
        "Een langlopende investering vraagt een langlopende financiering.",
    ),
    mk(
        "Een onderneming heeft een kaskrediet van 50 000 euro maar staat al maanden op − 48 000 euro. Wat besluit je?",
        [
            "Ze gebruikt kortlopend krediet voor een blijvende behoefte",
            "Haar liquiditeit is uitstekend, want ze heeft nog 2 000 euro ruimte op haar krediet",
            "Ze heeft te veel eigen vermogen en zou beter meer lenen bij de bank",
            "Ze moet haar klanten sneller leveren, dan daalt het kaskrediet vanzelf",
        ],
        0,
        "Een kaskrediet is bedoeld voor tijdelijke tekorten. Een blijvend tekort vraagt een langlopende oplossing.",
    ),
    casus(
        "Brouwerij Hop bv wil een nieuwe bottellijn van 300 000 euro, die vijftien jaar meegaat. Ze heeft 60 000 euro reserves. De zaakvoerders willen niemand anders laten meebeslissen. In de zomer heeft ze telkens een piek in de voorraad.",
        [
            mk(
                "Welke combinatie past het best voor de bottellijn?",
                [
                    "De reserves gebruiken en de rest met een investeringskrediet",
                    "Alles met een kaskrediet",
                    "Nieuwe aandeelhouders laten instappen voor het hele bedrag",
                    "Een straight loan van drie maanden",
                ],
                0,
                "Zelffinanciering plus een lening op lange termijn: geen nieuwe medebeslissers en een looptijd die past bij de machine.",
            ),
            mk(
                "Welke financiering past bij de voorraadpiek in de zomer?",
                ["Een kaskrediet of een straight loan", "Een obligatielening", "Een kapitaalverhoging", "Een hypothecaire lening"],
                0,
                "Een tijdelijke behoefte los je op met kortlopend krediet.",
            ),
            tabel(
                "Welke uitspraken over het plan kloppen?",
                [
                    ("Het investeringskrediet verlaagt de solvabiliteit.", J),
                    ("Door de reserves te gebruiken daalt het eigen vermogen.", F),
                    ("De interest op het investeringskrediet is een kost.", J),
                ],
                "Reserves gebruiken om te investeren verandert het eigen vermogen niet: het geld wordt een machine. De lening is wel extra vreemd vermogen.",
            ),
        ],
    ),
]
