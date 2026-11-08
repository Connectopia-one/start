"""De Eerste Wereldoorlog en de Russische revoluties — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="remember-belgium.webp", zelf=False,
         wat="De Britse wervingsaffiche 'Remember Belgium - Enlist To-Day' uit 1915 (een soldaat voor een brandend Belgisch dorp). Publiek domein.",
         waar="Wikimedia Commons, zoek 'Remember Belgium enlist today poster'.",
         vragen="casus over propaganda in een totale oorlog"),
    dict(bestand="tijdlijn-1750-2030.svg", zelf=True,
         wat="Dezelfde tijdlijn als bij het referentiekader.",
         vragen="klikvraag op 1917"),
]

VRAGEN = [
    tabel(
        "Aanleiding of oorzaak van de Eerste Wereldoorlog?",
        [
            ("De moord op Frans Ferdinand in Sarajevo", "Aanleiding"),
            ("Wedijver en nationalisme tussen de grote mogendheden", "Oorzaak"),
            ("Een wedloop in bewapening", "Oorzaak"),
            ("Een web van bondgenootschappen", "Oorzaak"),
        ],
        "De aanleiding is de vonk: de moord in juni 1914. De oorzaken zijn de opgestapelde spanningen: nationalisme, militarisme en bondgenootschappen.",
        kolommen=["Aanleiding", "Oorzaak"],
    ),
    mk(
        "Waarom kon een moord in Sarajevo uitgroeien tot een oorlog tussen bijna alle grote mogendheden?",
        [
            "Het web van bondgenootschappen sleepte het ene land na het andere mee",
            "Alle landen van Europa hadden samen Frans Ferdinand als koning gekozen",
            "De Volkenbond verplichtte zijn leden om elkaar in de oorlog te steunen",
            "Sarajevo was in 1914 de hoofdstad van zowel Frankrijk als Rusland",
        ],
        0,
        "Bondgenoten moesten elkaar helpen. Zo werd een conflict op de Balkan een oorlog tussen de Triple Entente en de Centralen.",
    ),
    sorteer(
        "Hoorde het land bij de Triple Entente of bij de Centralen?",
        ["Triple Entente", "Centralen"],
        [
            ["Frankrijk", "Triple Entente"],
            ["Rusland", "Triple Entente"],
            ["Groot-Brittannië", "Triple Entente"],
            ["Duitsland", "Centralen"],
            ["Oostenrijk-Hongarije", "Centralen"],
        ],
        "De Triple Entente bestond uit Frankrijk, Rusland en Groot-Brittannië. Duitsland en Oostenrijk-Hongarije stonden aan de kant van de Centralen.",
    ),
    mk(
        "Een leerling schrijft: \"België koos in 1914 de kant van Frankrijk.\" Wat is de juiste verbetering?",
        [
            "België werd binnengevallen volgens het plan Von Schlieffen en verdedigde zijn neutraliteit",
            "België koos de kant van Duitsland, omdat het bang was voor het Franse leger",
            "België bleef de hele oorlog volledig buiten de gevechten, zoals Zwitserland",
            "België viel zelf Duitsland binnen om het Rijnland terug te winnen",
        ],
        0,
        "Het Duitse plan wilde Frankrijk snel uitschakelen via het neutrale België. België koos niet, het werd binnengevallen.",
    ),
    volgorde(
        "Zet de gebeurtenissen van de Eerste Wereldoorlog in de juiste volgorde.",
        ["De moord in Sarajevo", "De Duitse inval in België", "De opmars loopt vast en de legers graven zich in", "De Verenigde Staten treden toe", "De wapenstilstand"],
        "Juni 1914, augustus 1914, eind 1914, 1917 en 11 november 1918.",
    ),
    mk(
        "Waarom ging de bewegingsoorlog van 1914 over in een loopgravenoorlog?",
        [
            "De opmars liep vast en beide legers groeven zich in",
            "Beide legers hadden geen kogels meer en moesten wachten",
            "De legers kregen het bevel om eerst de winter af te wachten",
            "De tank was al uitgevonden en maakte elke opmars onmogelijk",
        ],
        0,
        "Toen geen van beide legers nog vooruit raakte, groeven ze zich in. Mitrailleurs maakten aanvallen over open terrein bijna onmogelijk.",
    ),
    keuze(
        "Men noemt de Eerste Wereldoorlog een [[*totale|koude|beperkte]] oorlog, omdat de hele samenleving werd ingezet. [[*Propaganda|Neutraliteit|Appeasement]] moest de steun van de bevolking vasthouden.",
        "Fabrieken, voedsel, vrouwen, kolonies en nieuws werden allemaal ingezet. Propaganda hield het moreel hoog.",
    ),
    casus(
        "Bekijk de Britse affiche uit 1915. Een soldaat staat voor een brandend dorp. Bovenaan staat: Remember Belgium. Onderaan: Enlist to-day, dat betekent: neem vandaag dienst.",
        [
            met_prent("remember-belgium.webp", keuze(
                "Het doelpubliek van deze affiche zijn [[*jonge Britse mannen|Belgische vluchtelingen|Duitse soldaten]]. De bedoeling is [[*mensen overtuigen om dienst te nemen|een neutraal verslag geven|de Duitse inval goedpraten]].",
                "Een wervingsaffiche richt zich op wie nog niet in het leger zit, en wil hen tot handelen aanzetten.",
            ), volgt=True),
            mk(
                "Waarom gebruikte een Britse affiche het lot van België?",
                [
                    "De inval in het neutrale België was voor Groot-Brittannië een sterk argument om de oorlog te steunen",
                    "België was in 1915 een Britse kolonie, net zoals Indië dat in die jaren was",
                    "Groot-Brittannië wilde België na de oorlog als bufferstaat voor zichzelf houden",
                    "Belgische soldaten vochten in 1915 enkel in Groot-Brittannië en niet aan het front",
                ],
                0,
                "Het verhaal van het binnengevallen, neutrale land maakte de oorlog rechtvaardig in de ogen van het Britse publiek.",
            ),
            tabel(
                "Mag je deze besluiten trekken uit de affiche?",
                [
                    ("De Britse regering wilde haar bevolking achter de oorlog krijgen.", "Mag"),
                    ("Elk Belgisch dorp is in 1914 afgebrand.", "Mag niet"),
                    ("Propaganda was een middel in een totale oorlog.", "Mag"),
                ],
                "Propaganda is een slechte bron over wat er precies gebeurde, maar een uitstekende bron over wat men wilde laten geloven.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over België in de Eerste Wereldoorlog.",
        [
            ("Het Belgische leger hield stand aan de IJzer.", J),
            ("Het leger hield een klein stuk van het land vrij.", J),
            ("De loopgraven die je vandaag bezoekt, zijn nog in hun oorspronkelijke staat.", F),
            ("Van de oorlog zie je vandaag kerkhoven, monumenten en musea.", J),
        ],
        "Het IJzerfront hield het laatste stukje vrij België. Wat je vandaag aan loopgraven bezoekt, is heraangelegd.",
    ),
    tabel(
        "Waarom en wanneer? Lees elke uitspraak over 1917.",
        [
            ("De Verenigde Staten traden toe door de onbeperkte Duitse duikbotenoorlog.", J),
            ("Rusland vocht tot het einde van de oorlog mee aan de kant van de Entente.", F),
            ("Na de revolutie sloot Rusland een aparte vrede.", J),
        ],
        "In 1917 kwam Amerika erbij en viel Rusland weg. Rusland vocht dus niet mee tot het einde.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar van de Februari- en de Oktoberrevolutie in Rusland.",
        "tijdlijn-1750-2030.svg",
        [[53.9, 25, 6.2, 55]],
        "1917, nog tijdens de Eerste Wereldoorlog, net vóór het streepje van 1920.",
    ),
    sorteer(
        "In welk domein situeer je elk gevolg van de oorlog?",
        ["Politiek", "Economisch", "Sociaal"],
        [
            ["Nieuwe staten en nieuwe regimes", "Politiek"],
            ["Schulden en verwoeste streken", "Economisch"],
            ["Miljoenen doden en gewonden", "Sociaal"],
            ["Vrouwen nemen in de fabrieken het werk van de mannen over", "Sociaal"],
        ],
        "De gevolgen spelen in verschillende domeinen tegelijk. De nieuwe plaats van vrouwen in het werk is een sociale verandering.",
    ),
    tabel(
        "Welke punten stonden in het Veertienpuntenplan van Woodrow Wilson?",
        [
            ("Open diplomatie in plaats van geheime verdragen", J),
            ("Het zelfbeschikkingsrecht van de volkeren", J),
            ("De oprichting van een volkerenbond", J),
            ("Een Duits keizerrijk dat groter wordt dan voor de oorlog", F),
        ],
        "Wilson wilde een nieuwe, open wereldorde met zelfbeschikking en een volkerenbond.",
    ),
    sorteer(
        "Was het een bepaling van het Verdrag van Versailles, of een onbedoeld gevolg ervan?",
        ["Bepaling", "Onbedoeld gevolg"],
        [
            ["Duitsland moet de schuld voor de oorlog erkennen", "Bepaling"],
            ["Duitsland moet herstelbetalingen doen", "Bepaling"],
            ["Elzas-Lotharingen gaat terug naar Frankrijk", "Bepaling"],
            ["Extreme partijen in Duitsland vinden een voedingsbodem", "Onbedoeld gevolg"],
            ["De wrok over het verdrag helpt Hitler aan steun", "Onbedoeld gevolg"],
        ],
        "De bepalingen waren bedoeld om Duitsland te verzwakken. Dat het verdrag als een dictaat werd ervaren en extreme partijen hielp, was niet de bedoeling.",
    ),
    mk(
        "Welk verband leg je met de redeneerwijze bedoelde en onbedoelde gevolgen tussen Versailles en de Tweede Wereldoorlog?",
        [
            "Het verdrag wilde Duitsland verzwakken, maar de wrok erover hielp onbedoeld Hitler aan steun",
            "Het verdrag wilde bewust een nieuwe oorlog uitlokken, en dat is ook precies gebeurd zoals bedoeld",
            "Het verdrag had geen enkel gevolg, want Duitsland heeft het nooit ondertekend",
            "Het verdrag maakte Duitsland groter, en daardoor wilde het nog meer gebied",
        ],
        0,
        "Het bedoelde gevolg was een zwak Duitsland. Het onbedoelde gevolg was een voedingsbodem voor extreme partijen.",
    ),
    tabel(
        "Sterkte of zwakte van de Volkenbond?",
        [
            ("Ze werd opgericht om conflicten vreedzaam te beslechten.", "Sterkte"),
            ("De Verenigde Staten traden nooit toe.", "Zwakte"),
            ("Ze had geen eigen leger.", "Zwakte"),
            ("Beslissingen vroegen de instemming van iedereen.", "Zwakte"),
        ],
        "Het doel was sterk, maar zonder de Verenigde Staten, zonder leger en met eenparigheid kon de bond landen niet tot de orde roepen.",
        kolommen=["Sterkte", "Zwakte"],
    ),
    mk(
        "Vergelijk de Volkenbond met de Verenigde Naties. Welke uitspraak klopt?",
        [
            "Geen van beide heeft een eigen staand leger; de VN laat lidstaten blauwhelmen per missie leveren",
            "Beide werden opgericht na de Tweede Wereldoorlog, in hetzelfde jaar en in dezelfde stad",
            "De Volkenbond had een vetorecht voor vijf landen, de VN heeft dat niet meer",
            "De Verenigde Staten waren lid van de Volkenbond, maar niet van de VN",
        ],
        0,
        "De Volkenbond had geen leger, en ook de VN heeft geen staand leger. De Verenigde Staten traden nooit toe tot de bond, wel tot de VN. Het vetorecht hoort bij de VN.",
    ),
    tabel(
        "Kenmerken van Rusland onder Nicolaas II. Juist of fout?",
        [
            ("Rusland was een autocratie.", J),
            ("De meeste Russen waren arme boeren.", J),
            ("De tsaar deelde zijn macht met een sterk verkozen parlement.", F),
            ("Nederlagen en honger in de oorlog ondermijnden zijn gezag.", J),
        ],
        "De tsaar regeerde alleen over een grote, arme boerenbevolking. De oorlog maakte de toestand onhoudbaar.",
    ),
    mk(
        "Na de Februarirevolutie kwam er een voorlopige regering. Waarom verloor ze zo snel haar steun?",
        [
            "Ze zette de oorlog voort, stelde de verdeling van de grond uit en de voedseltekorten bleven",
            "Ze sloot meteen vrede met Duitsland en gaf alle grond aan de adel terug",
            "Ze bracht de tsaar terug op de troon en schafte de verkiezingen af",
            "Ze voerde de vijfjarenplannen in en dwong de boeren in collectieve bedrijven",
        ],
        0,
        "Oorlog, grond en brood bleven onopgelost. Daar speelde Lenin met zijn belofte vrede, brood en land handig op in.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["De tsaar doet troonsafstand en er komt een voorlopige regering", "Februarirevolutie"],
            ["De bolsjewieken onder Lenin grijpen de macht", "Oktoberrevolutie"],
            ["De arbeidersklasse grijpt in de overgangsfase alle macht", "Dictatuur van het proletariaat"],
            ["Graan wordt bij de boeren opgeëist en voedsel op rantsoen gezet", "Oorlogscommunisme"],
        ],
        ["Collectivisatie"],
        "Vier stappen van 1917 tot de burgeroorlog. Collectivisatie hoort pas bij Stalin, vanaf 1928.",
    ),
    sleep(
        "Lenin vatte zijn belofte samen in drie woorden: vrede, [[brood]] en [[land]]. Na de Oktoberrevolutie volgde geen rust maar een [[burgeroorlog]] van jaren.",
        ["vrijheid", "olie", "wapenstilstand"],
        "Vrede, brood en land sprak de soldaten, arbeiders en boeren aan. De macht moest daarna nog in een burgeroorlog bevochten worden.",
    ),
    mk(
        "Hoe leidde het beleid van Nicolaas II tot de Februarirevolutie?",
        [
            "Hij regeerde alleen en hield vast aan de oorlog, terwijl nederlagen en honger zijn gezag ondermijnden",
            "Hij gaf de boeren alle grond en sloot meteen vrede, waarna de adel tegen hem in opstand kwam",
            "Hij voerde de vijfjarenplannen in en liet koelakken deporteren naar strafkampen",
            "Hij liet de bolsjewieken regeren en trok zich terug uit de politiek",
        ],
        0,
        "Een autocraat die een rampzalige oorlog voortzet in een arm land: daar brak het gezag van de tsaar op.",
    ),
    tabel(
        "Kenmerk van het oorlogscommunisme of niet?",
        [
            ("De industrie komt in handen van de staat.", J),
            ("Graan wordt bij de boeren opgeëist.", J),
            ("Voedsel wordt op rantsoen gezet.", J),
            ("Boeren mogen hun graan vrij op de markt verkopen.", F),
        ],
        "In de burgeroorlog nam de staat alles in handen. Vrije handel in graan was er net niet.",
        kolommen=["Kenmerk", "Geen kenmerk"],
    ),
    open_(
        "Leg uit waarom men de Eerste Wereldoorlog een totale oorlog noemt. Geef drie voorbeelden.",
        "De hele samenleving werd voor de oorlog ingezet, niet alleen het leger. Fabrieken maakten wapens en munitie, voedsel werd voor het front gebruikt, vrouwen namen het werk van de mannen in de fabrieken over, kolonies leverden soldaten en grondstoffen, en propaganda moest de steun van de bevolking vasthouden.",
    ),
    tabel(
        "Welke nieuwe wapens maakten van de Eerste Wereldoorlog een slachting zonder weerga?",
        [
            ("De mitrailleur", J),
            ("Gifgas", J),
            ("De tank", J),
            ("De atoombom", F),
        ],
        "Mitrailleur, gifgas en tank horen bij de Eerste Wereldoorlog. De atoombom kwam pas in 1945.",
    ),
    mk(
        "Bij het uitbreken van de oorlog dachten veel mensen dat hij voor de kerstdagen voorbij zou zijn. Waarom liep dat anders?",
        [
            "De bewegingsoorlog liep vast in een loopgravenoorlog die jaren duurde",
            "Alle legers spraken af om pas na de kerstdagen te beginnen vechten",
            "De Verenigde Staten traden meteen toe en verlengden zo de oorlog",
            "Rusland won de oorlog al in 1914, maar de andere landen gaven niet op",
        ],
        0,
        "Toen de opmars vastliep, groeven de legers zich in. De oorlog duurde tot de wapenstilstand van 11 november 1918.",
    ),
    keuze(
        "In 1919 tekende Duitsland het Verdrag van Versailles in de [[*Spiegelzaal|Rijksdag|Volkenbond]], dezelfde zaal waar in [[*1871|1815|1914]] het Duitse Keizerrijk werd uitgeroepen.",
        "Dezelfde zaal, de rollen omgedraaid: de vernedering van Frankrijk in 1871 werd in 1919 de vernedering van Duitsland.",
    ),
]
