"""Industrialisatie en de sociale kwestie — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvragen op 1893 en 1919 (stemrecht)"),
    dict(bestand="kinderarbeid-mijn.webp", zelf=False,
         wat="Een foto of gravure uit de 19de eeuw van kinderen die in een steenkoolmijn of textielfabriek werken. Liefst Belgisch of Brits, publiek domein.",
         waar="Wikimedia Commons, zoek 'child labour coal mine 19th century' of 'hiercheuse' (Belgische mijnmeisjes).",
         vragen="casus over leef- en werkomstandigheden"),
]

VRAGEN = [
    sorteer(
        "Hoort het kenmerk bij de eerste of bij de tweede industriële revolutie?",
        ["Eerste", "Tweede"],
        [
            ["Steenkool als energiebron", "Eerste"],
            ["De stoommachine van Watt in de fabriek", "Eerste"],
            ["Elektriciteit als nieuwe krachtbron", "Tweede"],
            ["Aardolie en de verbrandingsmotor", "Tweede"],
            ["De lopende band", "Tweede"],
            ["Vooral getrokken door Duitsland en de Verenigde Staten", "Tweede"],
        ],
        "De eerste revolutie draaide op kolen en stoom en begon in Engeland. De tweede bracht elektriciteit, olie, staal en scheikunde, en een nieuwe bedrijfsorganisatie met de lopende band.",
    ),
    mk(
        "Waarom stond een fabriek tijdens de eerste industriële revolutie meestal dicht bij een steenkoolmijn?",
        [
            "Omdat kolen zwaar en duur waren om te vervoeren",
            "Omdat arbeiders enkel in mijnstreken wilden wonen",
            "Omdat elektriciteit alleen bij de mijn opgewekt kon worden",
            "Omdat de overheid fabrieken elders verbood te bouwen",
        ],
        0,
        "De stoommachine had veel kolen nodig, en vervoer was traag en duur. Met elektriciteit en olie kon een fabriek later veel vrijer gelegen zijn.",
    ),
    mk(
        "Waarom vergelijkt men het energiegebruik van de twee industriële revoluties?",
        [
            "De overstap van kolen naar elektriciteit en olie veranderde waar fabrieken konden staan en wie de grootmachten werden",
            "Omdat beide revoluties precies dezelfde energiebron gebruikten, alleen in andere landen en in een andere eeuw",
            "Omdat men wil bewijzen dat de tweede revolutie minder energie nodig had dan de eerste, en dus zuiniger was",
            "Omdat energie het enige verschil is tussen beide revoluties; transport en organisatie bleven gelijk",
        ],
        0,
        "Energie bepaalde de ligging van fabrieken, het transport en het machtsevenwicht: Duitsland en de Verenigde Staten trokken de tweede revolutie.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over de economische sectoren tijdens de industrialisatie.",
        [
            ("De steenkoolmijnbouw hoort bij de primaire sector.", J),
            ("Het aandeel van de landbouw in de tewerkstelling groeide sterk.", F),
            ("Een mijn haalt een grondstof uit de bodem.", J),
            ("De fabrieken namen werk over van ambachtslui.", J),
        ],
        "Mijnbouw haalt grondstoffen uit de bodem: primaire sector. Tijdens de industrialisatie daalde het aandeel van de landbouw in de tewerkstelling.",
    ),
    koppel(
        "Welke uitvinding of persoon hoort bij elke omschrijving?",
        [
            ["Verbeterde de stoommachine zodat ze bruikbaar werd in fabrieken", "Watt"],
            ["Gaf in 1776 de vrije markt haar grondslag", "Smith"],
            ["Bouwde in Seraing een groot metaalbedrijf", "Cockerill"],
            ["Liet berichten over grote afstand in een oogwenk reizen", "De telegraaf"],
        ],
        ["Bismarck"],
        "Watt en de stoommachine, Smith en het economisch liberalisme, Cockerill en de Belgische zware industrie, en de telegraaf als sprong in de communicatie.",
    ),
    keuze(
        "Het economisch liberalisme wil dat de overheid de economie zo veel mogelijk [[*vrij laat|zelf plant|in handen neemt]]. Het kapitalisme vergroot de ongelijkheid, doordat de winst naar wie de fabriek [[*bezit|bouwt|bewaakt]] gaat.",
        "Smith verdedigde de vrije markt. In het kapitalisme gaat de winst naar de eigenaar, en die spanning tussen bezit en arbeid noemt men de sociale kwestie.",
    ),
    tabel(
        "Aanbodfactor of vraagfactor voor de Belgische industrialisatie?",
        [
            ("Steenkool in de bodem van Henegouwen en Luik", "Aanbod"),
            ("Banken die durfden investeren", "Aanbod"),
            ("Een groeiende bevolking die meer goederen koopt", "Vraag"),
            ("Vaklui met ervaring in textiel en metaal", "Aanbod"),
        ],
        "Aanbodfactoren maken productie mogelijk: grondstoffen, kapitaal en vakkennis. Een vraagfactor zorgt dat er kopers zijn.",
        kolommen=["Aanbod", "Vraag"],
    ),
    sorteer(
        "Welke industrie hoort bij welke streek in het 19de-eeuwse België?",
        ["Henegouwen en Luik", "Gent", "Verviers"],
        [
            ["Steenkoolmijnen", "Henegouwen en Luik"],
            ["Katoen- en textielfabrieken", "Gent"],
            ["Wolnijverheid", "Verviers"],
            ["Zware metaalindustrie zoals die van Cockerill", "Henegouwen en Luik"],
        ],
        "De steenkoolbekkens lagen in Henegouwen en Luik, met de zware industrie erbij. Gent was de textielstad, Verviers de wolstad.",
    ),
    mk(
        "Een leerling besluit: \"Vlaanderen was in de 19de eeuw de industriële motor van België.\" Wat klopt er niet?",
        [
            "De industrie lag vooral in Wallonië; Vlaanderen bleef langer landelijk, met Gent als uitzondering",
            "Er was in de 19de eeuw in heel België nog geen enkele fabriek of mijn te vinden",
            "Vlaanderen had wel de meeste steenkoolmijnen, maar geen enkele textielfabriek",
            "Er klopt niets niet: Vlaanderen was toen al veel sterker geïndustrialiseerd",
        ],
        0,
        "De steenkool lag in Henegouwen en Luik. Vlaanderen bleef landelijker, al was Gent een belangrijke textielstad.",
    ),
    inv(
        "Tussen welke twee steden reed in 1835 de eerste spoorlijn van het Europese vasteland? Schrijf: stad en stad.",
        "Brussel en Mechelen",
        "Brussel-Mechelen, in 1835: België was een van de eerste landen op het vasteland dat industrialiseerde.",
    ),
    mk(
        "Wat onderscheidt een klassenmaatschappij van de standenmaatschappij die eraan voorafging?",
        [
            "Je plaats hangt af van je bezit en je plaats in de productie, niet van je geboorte",
            "Je plaats hangt af van je geboorte, en niemand kan ooit van groep veranderen",
            "Iedereen heeft er precies evenveel bezit en hetzelfde inkomen",
            "Alleen de adel en de geestelijkheid hebben er nog rechten",
        ],
        0,
        "In een klassenmaatschappij bepaalt bezit waar je staat. Wie geen werktuigen meer bezit en voor loon werkt, is proletariër geworden.",
    ),
    inv(
        "Hoe heet het proces waarbij boeren en ambachtslui hun eigen werktuigen verliezen en loonarbeider worden? (één woord)",
        "proletarisering",
        "Proletarisering: wie vroeger met eigen gereedschap werkte, wordt afhankelijk van een loon in de fabriek.",
    ),
    casus(
        "Bekijk de prent. Ze toont kinderen die in de 19de eeuw in een mijn werken. Lees ook dit gegeven: de Belgische grondwet van 1831 verbood kinderarbeid niet.",
        [
            met_prent("kinderarbeid-mijn.webp", mk(
                "Waarom zetten fabrikanten en mijnbazen graag kinderen aan het werk?",
                ["Kinderen waren goedkoop en klaagden niet", "Kinderen waren sterker dan volwassenen", "De wet verplichtte hen om kinderen aan te nemen", "Kinderen kregen een hoger loon dan hun ouders"],
                0,
                "Kinderen kostten weinig en kwamen niet in opstand. Pas veel later kwam er een verbod op kinderarbeid.",
            ), volgt=True),
            tabel(
                "Welke leef- en werkomstandigheden van arbeiders in de 19de eeuw passen bij deze prent?",
                [
                    ("Werkdagen van twaalf uur en meer", J),
                    ("Een vergoeding bij ziekte of ongeval", F),
                    ("Wonen in overvolle beluiken zonder stromend water", J),
                    ("Een wettelijk verbod op kinderarbeid sinds 1831", F),
                ],
                "Lange dagen en slechte woningen waren gewoon. Een vergoeding bij ziekte of een verbod op kinderarbeid bestonden toen nog niet.",
            ),
            keuze(
                "Deze prent is een [[*audiovisuele|mondelinge|materiële]] bron. Ze toont de [[*sociale kwestie|restauratie|Reformatie]]: de spanning tussen wie de mijn bezit en wie er werkt.",
                "Foto's en prenten zijn audiovisuele bronnen. De slechte omstandigheden van arbeiders zijn de kern van de sociale kwestie.",
            ),
        ],
    ),
    sorteer(
        "Coöperatie, mutualiteit of vakbond?",
        ["Coöperatie", "Mutualiteit", "Vakbond"],
        [
            ["De leden kopen samen brood in en delen de winst", "Coöperatie"],
            ["Arbeiders sparen samen om bij ziekte een uitkering te krijgen", "Mutualiteit"],
            ["Arbeiders onderhandelen met de baas en leggen het werk neer", "Vakbond"],
            ["De leden produceren samen en verkopen in een eigen winkel", "Coöperatie"],
        ],
        "Een coöperatie produceert of koopt samen. Een mutualiteit of ziekenfonds keert uit bij ziekte. Een vakbond onderhandelt en staakt.",
    ),
    tabel(
        "Marxisme, sociaaldemocratie of christendemocratie? Welke stroming past bij elke uitspraak?",
        [
            ("Alleen een revolutie kan de arbeiders bevrijden.", "Marxisme"),
            ("We verbeteren het lot van de arbeiders langs verkiezingen en wetten.", "Sociaaldemocratie"),
            ("Privébezit mag, maar de arbeider heeft recht op een rechtvaardig loon.", "Christendemocratie"),
            ("De geschiedenis is een strijd tussen klassen.", "Marxisme"),
        ],
        "Marxisten wilden een revolutie, sociaaldemocraten hervorming via het parlement. De christendemocratie volgde Rerum Novarum: privébezit aanvaarden, maar met bescherming voor de arbeider.",
        kolommen=["Marxisme", "Sociaaldemocratie", "Christendemocratie"],
    ),
    mk(
        "De pauselijke brief Rerum Novarum verscheen in 1891. Wat was het belang ervan?",
        [
            "Hij gaf de christendemocratie haar sociale programma",
            "Hij riep de arbeiders op tot een gewapende revolutie",
            "Hij verbood elke vorm van privébezit voor katholieken",
            "Hij schafte het cijnskiesrecht in België af",
        ],
        0,
        "Rerum Novarum aanvaardde het privébezit, maar vroeg een rechtvaardig loon en bescherming voor de arbeider.",
    ),
    volgorde(
        "Zet de stappen in de evolutie van het Belgische stemrecht in de juiste volgorde.",
        ["Cijnskiesrecht voor wie genoeg belasting betaalt", "Algemeen meervoudig stemrecht na een algemene staking", "Algemeen enkelvoudig stemrecht voor mannen"],
        "Van 1831 tot 1893 cijnskiesrecht, in 1893 het algemeen meervoudig stemrecht, en in 1919 het algemeen enkelvoudig stemrecht voor mannen.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin het algemeen meervoudig stemrecht er kwam.",
        "tijdlijn-1750-2030.svg",
        [[46.5, 25, 6.2, 55]],
        "1893, na een algemene staking. Net vóór het streepje van 1900.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de mannen in België het algemeen enkelvoudig stemrecht kregen.",
        "tijdlijn-1750-2030.svg",
        [[54.6, 25, 6.2, 55]],
        "1919, vlak na de Eerste Wereldoorlog: één man, één stem.",
    ),
    mk(
        "Onder het algemeen meervoudig stemrecht van 1893 had elke man minstens één stem. Hoeveel stemmen kon één man ten hoogste uitbrengen?",
        ["3", "2", "5", "10"],
        0,
        "Wie bijvoorbeeld meer bezat of een diploma had, kreeg extra stemmen, tot ten hoogste drie.",
    ),
    mk(
        "Waarom bleef de plattelandsvlucht in België deels uit?",
        [
            "Goedkope werkmanskaarten lieten arbeiders op het platteland wonen en dagelijks naar de fabriek sporen",
            "De Belgische overheid verbood boeren om naar de stad te verhuizen, op straffe van gevangenis",
            "Er was in de 19de eeuw in de Belgische steden geen enkele fabriek waar je kon werken",
            "Alle Belgische fabrieken lagen midden op het platteland, ver van elke stad of spoorlijn",
        ],
        0,
        "Met de werkmanstrein werd pendelen goedkoop. Zo bleven veel arbeiders landelijk wonen.",
    ),
    sorteer(
        "Welke vorm van migratie herken je?",
        ["Plattelandsvlucht", "Pendelarbeid", "Seizoensarbeid", "Emigratie naar Amerika"],
        [
            ["Een boerenzoon verhuist voorgoed naar de fabrieksstad", "Plattelandsvlucht"],
            ["Een arbeider neemt elke ochtend de werkmanstrein naar Brussel", "Pendelarbeid"],
            ["Vlaamse arbeiders werken elke zomer enkele weken op akkers in een buurland en keren daarna terug", "Seizoensarbeid"],
            ["Een gezin vertrekt per schip om in Amerika goedkope grond te zoeken", "Emigratie naar Amerika"],
        ],
        "Verhuizen naar de stad, dagelijks heen en weer, tijdelijk voor een seizoen, of voorgoed naar een ander werelddeel.",
    ),
    tabel(
        "Welke redenen hadden veel Europeanen in de 19de eeuw om naar Amerika te trekken?",
        [
            ("Armoede en honger in eigen streek", J),
            ("De belofte van goedkope grond en werk", J),
            ("Vervolging om geloof of politieke overtuiging", J),
            ("Een verbod op landbouw in Europa", F),
        ],
        "Armoede, kansen in Amerika en vervolging dreven miljoenen mensen over de oceaan. Een verbod op landbouw bestond niet.",
    ),
    mk(
        "Een arbeider wil zijn loon verhogen. Wat doet een vakbond om dat te bereiken, wat een coöperatie niet doet?",
        [
            "Onderhandelen met de werkgever en eventueel staken",
            "Samen goederen produceren en de winst verdelen",
            "Samen sparen voor een uitkering bij ziekte",
            "Goedkoop brood verkopen in een eigen winkel",
        ],
        0,
        "Een vakbond onderhandelt en staakt, een coöperatie produceert of koopt samen in, een mutualiteit keert uit bij ziekte.",
    ),
    sleep(
        "De spoorweg met [[stoomlocomotieven]], het stoomschip en de [[telegraaf]] deden transport en communicatie vooruitspringen. In de tweede revolutie verdeelde de [[lopende band]] het werk in kleine stappen.",
        ["windmolen", "postkoets", "zeilschip"],
        "Stoom op land en zee, en de telegraaf voor berichten. De lopende band hoort bij de nieuwe bedrijfsorganisatie van de tweede revolutie.",
    ),
    mk(
        "Hoe vergroot het kapitalisme volgens zijn critici de sociale ongelijkheid?",
        [
            "De winst gaat naar de eigenaar van de fabriek en niet naar wie er werkt",
            "Iedereen krijgt in het kapitalisme exact hetzelfde loon, ook wie hard werkt",
            "De overheid neemt alle winst af en verdeelt ze onder de eigenaars",
            "Alleen arbeiders mogen een fabriek bezitten, en de burgerij wordt arm",
        ],
        0,
        "Wie de productiemiddelen bezit, krijgt de winst. Wie enkel zijn arbeid heeft, blijft afhankelijk van een loon.",
    ),
    open_(
        "Leg het verband uit tussen de industrialisatie en het ontstaan van de vakbonden. Gebruik de begrippen proletarisering en sociale kwestie.",
        "Door de industrialisatie verloren veel boeren en ambachtslui hun eigen werktuigen en werden ze loonarbeider: proletarisering. In de fabrieken werkten ze lange dagen voor een laag loon, zonder bescherming. Die spanning tussen eigenaars en arbeiders is de sociale kwestie. Om daar iets tegen te doen, organiseerden arbeiders zich in vakbonden die onderhandelden en staakten.",
    ),
    mk(
        "Wat was het verband tussen de algemene staking en het stemrecht in België?",
        [
            "Na een algemene staking kwam er in 1893 het algemeen meervoudig stemrecht",
            "Na een algemene staking werd het stemrecht in 1893 volledig afgeschaft",
            "Na een algemene staking kregen ook de vrouwen in 1893 stemrecht",
            "Er was geen verband: stakingen waren in België toen nog verboden",
        ],
        0,
        "De druk van de arbeiders dwong een eerste uitbreiding af. Het algemeen enkelvoudig stemrecht voor mannen volgde pas in 1919.",
    ),
]
