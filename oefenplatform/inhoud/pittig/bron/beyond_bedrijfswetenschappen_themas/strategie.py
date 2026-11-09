"""SWOT, stakeholders en het ondernemingsplan — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import raster_zone

PRENTEN = [
    dict(bestand="swot.svg", zelf=True,
         wat="Leeg SWOT-schema: intern of extern, helpend of hinderend.",
         vragen="klikvragen en een tabel over de SWOT-analyse"),
]

VRAGEN = [
    klik(
        "Een fietsenwinkel ziet dat de gemeente nieuwe fietssnelwegen aanlegt in de buurt. Klik op het vak van de SWOT waar dit hoort.",
        "swot.svg",
        [raster_zone(1, 0, 2, 2)],
        "De fietssnelwegen liggen buiten de onderneming en kunnen haar helpen: een kans.",
    ),
    klik(
        "De winkel heeft maar één personeelslid dat fietsen kan herstellen. Klik op het vak van de SWOT waar dit hoort.",
        "swot.svg",
        [raster_zone(0, 1, 2, 2)],
        "Het ligt in de onderneming zelf en hindert haar: een zwakte.",
    ),
    met_prent("swot.svg", tabel(
        "Waar hoort elk punt in de SWOT van een plaatselijke boekenwinkel?",
        [
            ("Het personeel geeft persoonlijk leesadvies", "Sterkte"),
            ("Een grote webwinkel levert boeken de volgende dag gratis", "Bedreiging"),
            ("De huur van het pand is hoog", "Zwakte"),
            ("Steeds meer scholen organiseren leesprojecten", "Kans"),
        ],
        "Sterktes en zwaktes liggen in de onderneming, kansen en bedreigingen in de omgeving.",
        kolommen=["Sterkte", "Zwakte", "Kans", "Bedreiging"],
    )),
    mk(
        "Een leerling zet \"Ons team spreekt vijf talen\" bij de kansen in de SWOT. Wat is er fout?",
        [
            "Het is een eigenschap van de onderneming zelf, dus een sterkte",
            "Het is een bedreiging, want talen zijn duur",
            "Er is niets fout: alles wat helpt, is een kans",
            "Het hoort niet in een SWOT, want het gaat over personeel",
        ],
        0,
        "Kansen komen van buiten. Wat de onderneming zelf in handen heeft, is een sterkte of een zwakte.",
    ),
    mk(
        "Waarom maak je eerst een SWOT-analyse voor je een strategie kiest?",
        [
            "Om sterktes te gebruiken voor kansen en zwaktes te beschermen tegen bedreigingen",
            "Omdat de wet dat oplegt bij de oprichting van een vennootschap",
            "Om de belastingen van het volgende jaar te berekenen",
            "Om de lonen van het personeel vast te leggen",
        ],
        0,
        "De SWOT verbindt wat de onderneming kan met wat er in de omgeving gebeurt.",
    ),
    sorteer(
        "Is de stakeholder intern of extern?",
        ["Intern", "Extern"],
        [
            ["Het personeel", "Intern"],
            ["De zaakvoerder", "Intern"],
            ["De buurtbewoners", "Extern"],
            ["De bank", "Extern"],
            ["De klanten", "Extern"],
            ["De overheid", "Extern"],
        ],
        "Interne stakeholders werken in of leiden de onderneming. Externe staan erbuiten, maar hebben er wel belang bij.",
    ),
    koppel(
        "Wat verwacht elke stakeholder vooral van de onderneming?",
        [
            ["Personeel", "Een goed loon en werkzekerheid"],
            ["Aandeelhouders", "Rendement op hun inbreng"],
            ["Klanten", "Goede producten aan een eerlijke prijs"],
            ["Overheid", "Belastingen en naleving van de regels"],
        ],
        ["Een hoge voorraad"],
        "Elke groep heeft andere belangen, die soms botsen.",
    ),
    mk(
        "Een fabriek wil 's nachts produceren om meer te verkopen. Welke stakeholders hebben dan tegengestelde belangen?",
        [
            "De aandeelhouders, die meer winst willen, en de buurtbewoners, die rust willen",
            "De klanten en de leveranciers, die allebei meer omzet willen",
            "De bank en de aandeelhouders, die allebei rendement willen",
            "De overheid en de klanten, die allebei lagere prijzen willen",
        ],
        0,
        "Meer productie helpt de winst, maar nachtwerk zorgt voor overlast in de buurt.",
    ),
    tabel(
        "Gaat de zin over de missie, de visie of de strategie?",
        [
            ("Wij brengen gezonde maaltijden tot bij mensen die zelf niet kunnen koken.", "Missie"),
            ("Over vijf jaar zijn wij de bekendste maaltijdservice van de provincie.", "Visie"),
            ("We openen twee nieuwe keukens en werken samen met thuiszorgdiensten.", "Strategie"),
        ],
        "De missie zegt waarom je bestaat, de visie waar je naartoe wil, de strategie hoe je daar raakt.",
        kolommen=["Missie", "Visie", "Strategie"],
    ),
    volgorde(
        "Zet de stappen van strategische planning in een logische volgorde.",
        [
            "De missie bepalen: waarom bestaan we?",
            "De visie bepalen: waar willen we staan?",
            "Een SWOT-analyse maken",
            "Een strategie kiezen en uitvoeren",
        ],
        "Eerst het bestaansrecht en het doel, dan de analyse van de situatie, dan de weg ernaartoe.",
    ),
    keuze(
        "Bij een marktonderzoek gebruik je bij [[*deskresearch|fieldresearch|een SWOT]] bestaande gegevens, en bij [[*fieldresearch|deskresearch|een financieel plan]] verzamel je zelf nieuwe gegevens.",
        "Bestaande statistieken opzoeken is deskresearch. Een enquête bij klanten is fieldresearch.",
    ),
    tabel(
        "Is het deskresearch of fieldresearch?",
        [
            ("Cijfers van Statbel over het aantal gezinnen in de gemeente opzoeken", "Deskresearch"),
            ("Voorbijgangers bevragen in de winkelstraat", "Fieldresearch"),
            ("Jaarverslagen van concurrenten lezen", "Deskresearch"),
            ("Een proefverkoop houden op een markt", "Fieldresearch"),
        ],
        "Desk: wat al bestaat. Field: zelf op het terrein nieuwe gegevens verzamelen.",
        kolommen=["Deskresearch", "Fieldresearch"],
    ),
    sorteer(
        "Hoort het in het financieel plan of in een ander deel van het ondernemingsplan?",
        ["Financieel plan", "Ander deel"],
        [
            ["De verwachte omzet van de eerste drie jaar", "Financieel plan"],
            ["De startinvesteringen en hoe ze gefinancierd worden", "Financieel plan"],
            ["Een beschrijving van de doelgroep", "Ander deel"],
            ["De geplande resultatenrekening", "Financieel plan"],
            ["De voorstelling van de oprichters", "Ander deel"],
        ],
        "Het financieel plan vertaalt het idee in cijfers: omzet, kosten, investeringen en financiering.",
    ),
    mk(
        "Een starter vraagt een lening voor zijn foodtruck. Waarom vraagt de bank zijn ondernemingsplan?",
        [
            "Om te zien of het project haalbaar is en of hij de lening kan terugbetalen",
            "Omdat de bank zelf mee de foodtruck wil uitbaten",
            "Om de belastingen van de starter te berekenen",
            "Omdat een ondernemingsplan de lening overbodig maakt",
        ],
        0,
        "Het plan toont het idee, de markt en de cijfers. Daaruit leidt de bank af hoe groot haar risico is.",
    ),
    mk(
        "De energieprijzen verdubbelen. Welke beslissing van een bakkerij is een logisch gevolg van deze actuele ontwikkeling?",
        [
            "Investeren in zuinigere ovens",
            "Meer personeel aanwerven voor de winkel",
            "De openingsuren op zondag verlengen",
            "Een tweede vestiging openen in een duurdere straat",
        ],
        0,
        "Een externe ontwikkeling verandert de kosten. Een zuinigere oven beperkt die bedreiging.",
    ),
    tabel(
        "Is de actuele ontwikkeling voor een webwinkel in kleding eerder een kans of een bedreiging?",
        [
            ("Steeds meer mensen kopen online", "Kans"),
            ("Strengere regels over het terugsturen van pakjes en afval", "Bedreiging"),
            ("Jongeren kopen graag tweedehands kleding", "Kans"),
            ("Transportkosten stijgen sterk", "Bedreiging"),
        ],
        "Hetzelfde nieuws kan voor de ene onderneming een kans en voor de andere een bedreiging zijn. Hier gaat het om een webwinkel in kleding die ook tweedehands wil verkopen.",
        kolommen=["Kans", "Bedreiging"],
    ),
    sleep(
        "Uit een SWOT volgt een strategie: je gebruikt je [[sterktes]] om [[kansen]] te benutten, en je werkt aan je [[zwaktes]] zodat [[bedreigingen]] minder pijn doen.",
        ["stakeholders", "visie"],
        "De vier vakken van de SWOT worden zo met elkaar verbonden.",
    ),
    mk(
        "Welke aspecten bepalen samen de bedrijfsstrategie? Duid alle juiste antwoorden aan.",
        [
            "Welke producten of diensten de onderneming aanbiedt",
            "Op welke klanten ze zich richt",
            "Hoe ze zich onderscheidt van de concurrentie",
            "De lievelingskleur van de zaakvoerder",
        ],
        [0, 1, 2],
        "Een strategie kiest wat je aanbiedt, voor wie en waarom men bij jou koopt.",
    ),
    mk(
        "Een koffiebar wil groeien. Uit haar SWOT blijkt: sterkte = eigen branderij, kans = veel kantoren in de buurt. Welke strategie past het best?",
        [
            "Verse koffie leveren aan de kantoren",
            "De eigen branderij verkopen om de vaste kosten van de zaak te verlagen",
            "Overschakelen op enkel thee, omdat kantoormensen minder koffie drinken",
            "De zaak op weekdagen sluiten en enkel in het weekend open zijn",
        ],
        0,
        "De strategie zet de sterkte (eigen koffie) in voor de kans (kantoren).",
    ),
    tabel(
        "Waar of niet waar over het ondernemingsplan?",
        [
            ("Het beschrijft het idee, de markt, de organisatie en de cijfers.", J),
            ("Het is enkel nuttig voor de bank, niet voor de ondernemer zelf.", F),
            ("Het financieel plan is bij een bv verplicht bij de oprichting.", J),
            ("Een ondernemingsplan verandert nooit meer na de start.", F),
        ],
        "Het plan helpt de ondernemer zelf om zijn idee door te denken. Het wordt bijgestuurd als de omstandigheden veranderen.",
    ),
    mk(
        "Een visie luidt: \"In 2030 is de helft van onze omzet afkomstig van herstellingen in plaats van verkoop.\" Wat zegt dit over de strategie?",
        [
            "Investeren in een hersteldienst en in opleiding",
            "De onderneming moet zo snel mogelijk stoppen met herstellingen",
            "De missie moet elk jaar veranderen",
            "De onderneming moet zo snel mogelijk meer nieuwe toestellen verkopen",
        ],
        0,
        "De strategie zijn de stappen om de visie te bereiken.",
    ),
    mk(
        "Een marktonderzoek toont dat de doelgroep vooral 's avonds online bestelt. Wat doet de onderneming met die informatie?",
        [
            "Ze stemt haar openingsuren, levering en reclame daarop af",
            "Ze negeert het, want marktonderzoek is enkel nuttig voor heel grote bedrijven",
            "Ze verandert haar missie volledig en kiest een helemaal nieuw product",
            "Ze verhoogt haar eigen vermogen met een kapitaalverhoging bij de aandeelhouders",
        ],
        0,
        "Marktonderzoek levert informatie om beslissingen beter te maken.",
    ),
    mk(
        "Een onderneming beslist haar leveranciers voortaan pas na 90 dagen te betalen in plaats van na 30. Welke stakeholder ondervindt daar het meeste nadeel van?",
        ["De leveranciers", "De klanten", "De aandeelhouders", "De buurtbewoners"],
        0,
        "Wat voor de onderneming een gunstiger leverancierskrediet is, is voor de leverancier een langer wachten op zijn geld.",
    ),
    inv(
        "Hoe noemt men een persoon of groep die belang heeft bij wat een onderneming doet, binnen of buiten de onderneming?",
        "stakeholder",
        "Personeel, klanten, buren, overheid, bank: allemaal stakeholders.",
    ),
    open_(
        "Kies een onderneming uit je buurt en geef een sterkte en een bedreiging. Leg uit waarom elk in dat vak hoort.",
        "Een bakkerij: sterkte is dat ze met eigen bloem van een lokale molen werkt, want dat ligt in de onderneming zelf en helpt haar. Bedreiging is dat een supermarkt in de buurt opent, want dat gebeurt buiten de onderneming en kan klanten wegnemen.",
        "Intern of extern, en helpt of hindert: die twee vragen bepalen het vak.",
    ),
    mk(
        "Wat is het verschil tussen een zwakte en een bedreiging?",
        [
            "Een zwakte ligt in de onderneming, een bedreiging komt van buiten",
            "Een zwakte is groter dan een bedreiging",
            "Een bedreiging kan de onderneming zelf veranderen, een zwakte niet",
            "Er is geen verschil: het zijn twee woorden voor hetzelfde",
        ],
        0,
        "Beide hinderen de onderneming, maar de oorsprong verschilt.",
    ),
    tabel(
        "Een bank, een buurtcomité en de aandeelhouders bekijken het plan voor een nieuwe fabriekshal. Waar letten ze vooral op?",
        [
            ("De bank", "Terugbetaling van de lening"),
            ("Het buurtcomité", "Geluid en verkeer"),
            ("De aandeelhouders", "Rendement"),
        ],
        "Elke stakeholder bekijkt hetzelfde plan vanuit zijn eigen belang.",
        kolommen=["Terugbetaling van de lening", "Geluid en verkeer", "Rendement"],
    ),
    casus(
        "Lars wil in zijn gemeente een fietskoerierdienst starten voor apotheken en winkels. Er is nog geen andere koerier. Lars kent de stad goed, maar heeft geen ervaring met boekhouden. De gemeente plant een autoluwe binnenstad.",
        [
            tabel(
                "Maak de SWOT van Lars.",
                [
                    ("Lars kent de stad goed", "Sterkte"),
                    ("Geen ervaring met boekhouden", "Zwakte"),
                    ("Een autoluwe binnenstad", "Kans"),
                    ("Een grote koeriersfirma kan na hem ook komen", "Bedreiging"),
                ],
                "Twee punten over Lars zelf, twee over de omgeving.",
                kolommen=["Sterkte", "Zwakte", "Kans", "Bedreiging"],
            ),
            mk(
                "Welk marktonderzoek past het best om de vraag in te schatten?",
                [
                    "Apothekers en winkeliers bevragen over hoe vaak ze iets laten leveren",
                    "Het aantal fietsen in België opzoeken",
                    "Zijn vrienden vragen of ze graag fietsen",
                    "Niets onderzoeken, want er is geen concurrent",
                ],
                0,
                "Fieldresearch bij de doelgroep zelf geeft de beste inschatting.",
            ),
            mk(
                "Hoe kan Lars zijn zwakte opvangen?",
                [
                    "Een boekhouder inschakelen of een cursus volgen",
                    "De zwakte gewoon weglaten uit zijn ondernemingsplan voor de bank",
                    "Meer fietsen kopen, zodat hij sneller meer leveringen kan doen",
                    "Wachten tot de autoluwe binnenstad er is",
                ],
                0,
                "Een zwakte ligt in de onderneming zelf: die kan hij zelf aanpakken.",
            ),
        ],
    ),
]
