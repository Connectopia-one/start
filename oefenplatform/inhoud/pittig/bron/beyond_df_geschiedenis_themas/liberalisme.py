"""Liberalisme en nationalisme — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

PRENTEN = []

VRAGEN = [
    # --- politiek liberalisme
    tabel(
        "Een liberaal uit de burgerij schrijft rond 1830 zijn wensen op. Welke punten passen in zijn lijstje?",
        [
            ("Een parlement dat beslist over de belastingen", J),
            ("Vrijheid van pers en van vereniging", J),
            ("Stemrecht voor iedere volwassen man, ook zonder bezit", F),
            ("Een vorst die alleen beslist, zonder grondwet", F),
        ],
        "De liberalen wilden een grondwet, een parlement en grondrechten. Stemrecht voor iedereen hoorde er niet bij: dat werd de eis van de arbeidersbeweging.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Wetgeven, besturen en rechtspreken liggen in verschillende handen.", "Machtenscheiding"],
            ["Enkel wie genoeg belasting betaalt, mag kiezen.", "Cijnskiesrecht"],
            ["De wet boven alle wetten, die de rechten van de burger vastlegt.", "Grondwet"],
            ["Een staat die zich beperkt tot orde, recht en veiligheid.", "Nachtwachtstaat"],
        ],
        ["Legitimiteit", "Algemeen stemrecht"],
        "Vier sleutelbegrippen van het liberalisme. Legitimiteit hoort bij Wenen, algemeen stemrecht bij de arbeidersbeweging.",
    ),
    mk(
        "Waarom kwam het liberalisme vooral op bij de gegoede burgerij?",
        [
            "Ze had bezit en kennis, maar weinig politieke macht",
            "Ze had al alle politieke macht en wilde die gewoon houden",
            "Ze had geen bezit en wilde dat de staat alles verdeelde",
            "Ze wilde de oude vorstenhuizen van voor 1789 terug op de troon",
        ],
        0,
        "Wie bezit en kennis heeft, maar niets te zeggen, wil inspraak. De ideeën van de Verlichting gaven daar de woorden voor.",
    ),
    mk(
        "Een liberaal wil een grondwet en machtenscheiding. Wat wil hij daarmee vooral voorkomen?",
        [
            "Dat één persoon alle macht heeft",
            "Dat de burgerij te veel inspraak krijgt in het bestuur van het land",
            "Dat de fabrikanten vrij kunnen beslissen over lonen en werkuren",
            "Dat de kranten vrij kunnen schrijven wat ze over de regering denken",
        ],
        0,
        "Grondwet en machtenscheiding binden de vorst aan regels en verdelen de macht.",
    ),
    tabel(
        "Een leerling zegt: \"De liberalen van 1830 waren democraten zoals wij.\" Welke gegevens spreken dat tegen?",
        [
            ("Ze verdedigden het cijnskiesrecht.", J),
            ("Alleen wie genoeg belasting betaalde, telde politiek mee.", J),
            ("Ze eisten vrijheid van meningsuiting.", F),
            ("Ze wilden een parlement dat de regering controleert.", F),
        ],
        "Grondrechten en een parlement zijn modern. Maar met het cijnskiesrecht bleef de politiek iets voor een kleine, rijke groep.",
    ),
    keuze(
        "Persvrijheid situeer je in het [[*politieke|economische|sociale]] domein, met een [[*culturele|militaire|religieuze]] kant: het gaat over macht, maar ook over wat je mag schrijven en lezen.",
        "Persvrijheid gaat over controle op de macht en over het vrije woord.",
    ),
    # --- economisch liberalisme
    sorteer(
        "Politiek of economisch liberalisme?",
        ["Politiek liberalisme", "Economisch liberalisme"],
        [
            ["een grondwet die de vorst aan regels bindt", "Politiek liberalisme"],
            ["gelijkheid voor de wet", "Politiek liberalisme"],
            ["vraag en aanbod bepalen de lonen", "Economisch liberalisme"],
            ["invoerrechten op graan afschaffen", "Economisch liberalisme"],
            ["laissez-faire", "Economisch liberalisme"],
            ["machtenscheiding", "Politiek liberalisme"],
        ],
        "Het politieke liberalisme gaat over macht en rechten, het economische over een staat die zich niet met de economie bemoeit.",
    ),
    mk(
        "Een fabrikant in 1840 laat kinderen twaalf uur per dag werken. Welke houding van de staat maakt dat mogelijk?",
        [
            "Laissez-faire: de staat bemoeit zich niet met de economie",
            "Legitimiteit: de oude vorstenhuizen krijgen hun troon terug",
            "Compensatie: wie gebied verliest, krijgt elders iets terug",
            "Machtsevenwicht: geen staat mag te machtig worden",
        ],
        0,
        "Laissez-faire gaf de fabrikanten de vrije hand: geen regels over lonen, uren of kinderarbeid.",
    ),
    casus(
        "Lees de bron. Een krant schrijft in 1845: \"Laat de handel vrij! Weg met de invoerrechten op graan. De staat moet de orde bewaren, maar zich niet mengen in wat de fabrikant zijn arbeiders betaalt. Vraag en aanbod regelen de lonen het best.\"",
        [
            mk(
                "Welke ideologie herken je in deze bron?",
                ["Het economisch liberalisme", "Het nationalisme", "De restauratie", "De romantiek"],
                0,
                "Vrije handel, geen staatsbemoeienis met lonen, vraag en aanbod: dat is economisch liberalisme.",
            ),
            tabel(
                "Wat zou de schrijver van deze bron vinden?",
                [
                    ("De staat moet een minimumloon vastleggen.", F),
                    ("De staat moet zorgen voor orde en veiligheid.", J),
                    ("Graan van buiten moet vrij binnen kunnen.", J),
                    ("De staat moet de werkuren in de fabriek beperken.", F),
                ],
                "De bron wil een nachtwachtstaat: orde ja, ingrijpen in lonen en uren nee.",
            ),
            mk(
                "Wie had het meest te winnen bij de ideeën uit deze bron?",
                [
                    "De fabrikanten",
                    "De arbeiders die lange dagen werkten voor een laag loon",
                    "De vorsten van de Heilige Alliantie",
                    "De kinderen die in de fabrieken werkten",
                ],
                0,
                "De vrije hand was voordelig voor de fabrikanten. De arbeiders kregen lange werkdagen en lage lonen zonder bescherming.",
            ),
        ],
    ),
    open_(
        "Leg het verband uit tussen het economisch liberalisme en de levensomstandigheden van de arbeiders in de negentiende eeuw.",
        "Het economisch liberalisme vond dat de staat zich niet met de economie mocht bemoeien (laissez-faire). Er kwamen dus geen regels over lonen, werkuren of kinderarbeid. De fabrikanten kregen de vrije hand, en de arbeiders werkten lange dagen voor lage lonen, zonder bescherming.",
    ),
    # --- nationalisme
    sorteer(
        "Eenmaking of onafhankelijkheid?",
        ["Eenmaking", "Onafhankelijkheid"],
        [
            ["de Duitse staten samenvoegen tot één rijk", "Eenmaking"],
            ["Italië samenvoegen tot één staat", "Eenmaking"],
            ["Griekenland maakt zich los van een vreemde heerser", "Onafhankelijkheid"],
            ["Polen wil zich losmaken", "Onafhankelijkheid"],
            ["België scheurt zich af in 1830", "Onafhankelijkheid"],
        ],
        "Eenmaking brengt verdeelde gebieden samen. Onafhankelijkheid maakt een volk los van een vreemde heerser.",
    ),
    tabel(
        "Een nationalist rond 1840 wil zijn volk overtuigen dat het een eigen staat verdient. Welke argumenten zou hij gebruiken?",
        [
            ("We spreken allemaal dezelfde taal.", J),
            ("We delen een gemeenschappelijk verleden.", J),
            ("Onze vorst werd in Wenen terug op de troon gezet.", F),
            ("Onze volksverhalen tonen wie we zijn.", J),
        ],
        "De argumenten kwamen uit het culturele domein: taal, verhalen en geschiedenis. Een vorst die in Wenen zijn troon terugkreeg, is net de oude orde.",
    ),
    mk(
        "Waarom kun je zeggen dat het schrijven van een woordenboek in de negentiende eeuw politiek werk was?",
        [
            "Een eigen taal gold als argument voor een eigen staat",
            "Woordenboeken werden geschreven in opdracht van het Congres van Wenen",
            "Woordenboeken legden vast wie mocht stemmen bij de verkiezingen",
            "Woordenboeken bepaalden de lonen in de fabrieken van het land",
        ],
        0,
        "Wie de eigen taal vastlegt, versterkt de band van de natie. En een natie hoort volgens de nationalisten een eigen staat te krijgen.",
    ),
    inv(
        "Welke kunststroming voedde het nationalisme met haar liefde voor volksverhalen, eigen taal en het verleden?",
        ["de romantiek", "romantiek"],
        "De romantiek keek naar het eigen verleden en de eigen taal. Zo gaf ze de natie een verhaal.",
    ),
    tabel(
        "Hoe veranderde het nationalisme in de loop van de negentiende eeuw?",
        [
            ("In het begin ging het vooral om zelfbestuur en eigen taal.", J),
            ("De agressieve vorm kwam pas later, tegen 1900.", J),
            ("De agressieve vorm werd later verbonden met het imperialisme.", J),
            ("Het nationalisme was van in het begin vijandig tegenover alle andere volken.", F),
        ],
        "Eerst bevrijdend, later soms uitsluitend en agressief.",
    ),
    mk(
        "Waarom botste het nationalisme met het Congres van Wenen?",
        [
            "Wenen tekende grenzen zonder naar de volken te kijken",
            "Wenen had alle volken in Europa een eigen staat beloofd en gegeven",
            "Wenen had de romantiek verboden in heel Europa en in de koloniën",
            "Wenen had Duitsland en Italië elk tot één sterke staat gemaakt",
        ],
        0,
        "Volken bleven verdeeld over staten of kwamen onder een vreemde heerser. Dat was precies wat de nationalisten wilden veranderen.",
    ),
    # --- samen tegen de oude orde
    casus(
        "Het is 1830. Twee mannen staan samen op een barricade tegen een vorst. Jan zegt: \"Ik vecht voor een grondwet, een parlement en persvrijheid.\" Pieter zegt: \"Ik vecht omdat mijn volk een eigen staat verdient.\"",
        [
            koppel(
                "Welke ideologie hoort bij wie?",
                [["Jan", "Liberalisme"], ["Pieter", "Nationalisme"]],
                ["Restauratie", "Laissez-faire"],
                "Jan wil grondrechten en een parlement: liberaal. Pieter wil een eigen staat: nationalist.",
            ),
            mk(
                "Waarom staan Jan en Pieter samen op dezelfde barricade?",
                [
                    "Ze willen allebei af van een vorst die alleen beslist",
                    "Ze willen allebei de toestand van voor 1789 herstellen in heel Europa",
                    "Ze zijn allebei lid van de Heilige Alliantie van Rusland en Pruisen",
                    "Ze willen allebei dat de staat de lonen van de arbeiders vastlegt",
                ],
                0,
                "Elk om zijn eigen reden, maar met dezelfde tegenstander: de oude orde.",
            ),
        ],
    ),
    mk(
        "Waarom noemt men liberalisme en nationalisme ideologieën?",
        [
            "Het zijn samenhangende stelsels van ideeën over de samenleving",
            "Het zijn twee kunststromingen die schilderijen over helden maakten",
            "Het zijn twee verdragen die op het Congres van Wenen getekend werden",
            "Het zijn twee landen die in 1830 onafhankelijk werden van hun vorst",
        ],
        0,
        "Een ideologie is een samenhangend stelsel van ideeën. Uit zulke stelsels groeien partijen en breuklijnen.",
    ),
    tabel(
        "Hoe reageerden de vorsten van de Heilige Alliantie op liberalisme en nationalisme?",
        [
            ("Ze traden ertegen op.", J),
            ("Ze steunden de liberale eisen voor een grondwet.", F),
            ("Ze wilden de orde van Wenen bewaren.", J),
            ("Ze hielpen volken aan een eigen staat.", F),
        ],
        "De vorsten wilden de oude orde bewaren. Liberalisme en nationalisme bedreigden die orde.",
    ),
    open_(
        "Leg uit waarom de liberale eisen na 1815 nog een halve eeuw bleven terugkomen, ondanks de restauratie.",
        "De restauratie zette de oude vorsten terug, maar nam de oorzaken niet weg. De burgerij bleef bezit en kennis hebben zonder politieke macht, en de ideeën van de Verlichting en de Franse Revolutie leefden voort. De onvrede bleef dus bestaan.",
    ),
    sleep(
        "Een bron uit 1848 roept op om alle Duitse staten samen te voegen tot één rijk: dat is [[nationalisme]]. Een bron die vraagt om de invoerrechten op graan af te schaffen, is [[economisch liberalisme]]. Een bron die een grondwet en persvrijheid eist, is [[politiek liberalisme]].",
        ["restauratie", "legitimiteit"],
        "Eenmaking is nationalistisch, vrije handel economisch liberaal en grondrechten politiek liberaal.",
    ),
    mk(
        "Voor wie was het algemeen enkelvoudig stemrecht later een belangrijke eis?",
        [
            "Voor de arbeidersbeweging",
            "Voor de liberalen van de gegoede burgerij in 1830",
            "Voor de vorsten van de Heilige Alliantie na 1815",
            "Voor Metternich en de andere leiders van het congres",
        ],
        0,
        "De liberalen hielden het bij het cijnskiesrecht. De arbeidersbeweging eiste later stemrecht voor iedereen.",
    ),
    keuze(
        "Volgens het economisch liberalisme bepalen [[*vraag en aanbod|de vorst en de adel|de vakbonden]] de prijzen en de lonen. De staat wordt dan een [[*nachtwachtstaat|welvaartsstaat|bufferstaat]].",
        "Vraag en aanbod regelen de markt. De staat bewaakt enkel orde, recht en veiligheid.",
    ),
    tabel(
        "Waarin verschillen liberalisme en nationalisme?",
        [
            ("Het liberalisme draait om de rechten van het individu.", J),
            ("Het nationalisme draait om de natie en een eigen staat.", J),
            ("Het nationalisme wil vooral de staat uit de economie houden.", F),
            ("Het liberalisme draait vooral om een gedeelde taal.", F),
        ],
        "Het liberalisme kijkt naar het individu, het nationalisme naar de gemeenschap van de natie.",
    ),
    open_(
        "Geef een voorbeeld van een situatie waarin liberalisme en nationalisme samenwerkten, en leg uit waarom dat kon.",
        "Bijvoorbeeld de Belgische revolutie van 1830: liberalen wilden grondrechten en een parlement, nationalisten een eigen staat. Ze konden samenwerken omdat ze dezelfde tegenstander hadden: een vorst die alleen besliste en de orde van Wenen.",
    ),
    volgorde(
        "Zet in chronologische volgorde.",
        ["De Verlichting", "De Franse Revolutie", "Het Congres van Wenen", "De Belgische revolutie", "De agressieve vorm van het nationalisme groeit"],
        "Eerst de ideeën van de Verlichting, dan de Revolutie van 1789, Wenen in 1815, België in 1830 en rond 1900 het agressieve nationalisme.",
    ),
    mk(
        "Een historicus noemt het nationalisme van 1830 'bevrijdend' en dat van 1900 'uitsluitend'. Wat bedoelt hij?",
        [
            "Eerst ging het om zelfbestuur, later noemde men andere volken minderwaardig",
            "Eerst wilde men een vorst zonder grondwet, later een vorst met een parlement",
            "Eerst wilde men vrije handel, later moest de staat alle lonen vastleggen",
            "Eerst wilde men de oude vorsten terug, later wilde men ze allemaal verjagen",
        ],
        0,
        "Het vroege nationalisme wilde vrijheid en een eigen taal. Rond 1900 kwam een vorm die andere volken als minder zag.",
    ),
]
