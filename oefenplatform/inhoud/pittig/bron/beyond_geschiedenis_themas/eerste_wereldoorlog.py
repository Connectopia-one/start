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
            ("Militarisme bij de grote mogendheden", "Oorzaak"),
        ],
        "De aanleiding is de vonk: de moord in juni 1914. De oorzaken zijn de opgestapelde spanningen: onder meer nationalisme en militarisme.",
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
            "België werd binnengevallen en verdedigde zijn neutraliteit",
            "België koos de kant van Duitsland, omdat het bang was voor het grote Franse leger",
            "België bleef de hele oorlog volledig buiten de gevechten, net zoals Zwitserland",
            "België viel in 1914 zelf Duitsland binnen om het Rijnland terug te winnen",
        ],
        0,
        "Het Duitse plan wilde Frankrijk snel uitschakelen via het neutrale België. België koos niet, het werd binnengevallen.",
    ),
    volgorde(
        "Zet de gebeurtenissen van de Eerste Wereldoorlog in de juiste volgorde.",
        ["De moord in Sarajevo", "De Duitse inval in België", "De Verenigde Staten treden toe", "De wapenstilstand", "Duitsland tekent het Verdrag van Versailles"],
        "Juni 1914, augustus 1914, 1917, november 1918 en 1919.",
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
        "Toen geen van beide legers nog vooruit raakte, groeven ze zich in.",
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
                    "De inval in het neutrale België was een sterk argument om de oorlog te steunen",
                    "België was in 1915 een Britse kolonie, net zoals Indië dat in die jaren ook was",
                    "Groot-Brittannië wilde België na de oorlog als eigen bufferstaat voor zichzelf houden",
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
                    ("De affiche toont hoe de Britse overheid de oorlog wilde laten zien.", "Mag"),
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
        "Lees elke uitspraak over het keerjaar waarin Amerika in de oorlog stapte.",
        [
            ("De Verenigde Staten traden toe door de onbeperkte Duitse duikbotenoorlog.", J),
            ("Rusland vocht tot het einde van de oorlog mee aan de kant van de Entente.", F),
            ("Na de revolutie sloot Rusland een aparte vrede.", J),
        ],
        "In hetzelfde jaar kwam Amerika erbij en viel Rusland weg. Rusland vocht dus niet mee tot het einde.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar van de Februari- en de Oktoberrevolutie in Rusland.",
        "tijdlijn-1750-2030.svg",
        [[54.0, 25, 6.2, 55]],
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
        "Welke militaire bepaling legde het Verdrag van Versailles aan Duitsland op?",
        [
            "Het mocht nog maar een klein leger houden",
            "Het moest zijn hele vloot aan Rusland geven",
            "Het moest soldaten leveren aan de Volkenbond",
            "Het moest zijn leger onder Frans bevel plaatsen",
        ],
        0,
        "Een klein leger, de schuld erkennen en herstelbetalingen: zo wilde men Duitsland verzwakken.",
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
        "In welk jaar werd de Volkenbond opgericht?",
        ["1920", "1914", "1918", "1945"],
        0,
        "De Volkenbond kwam er in 1920, na de vrede van Versailles.",
    ),
    tabel(
        "Kenmerken van Rusland onder Nicolaas II. Juist of fout?",
        [
            ("Rusland was een autocratie.", J),
            ("De meeste Russen waren arme boeren.", J),
            ("De tsaar deelde zijn macht met een sterk verkozen parlement.", F),
            ("Rusland was een sterk geïndustrialiseerd land met weinig boeren.", F),
        ],
        "De tsaar regeerde alleen over een grote, arme boerenbevolking. De oorlog maakte de toestand onhoudbaar.",
    ),
    mk(
        "Na de Februarirevolutie kwam er een voorlopige regering. Waarom verloor ze zo snel haar steun?",
        [
            "Ze zette de oorlog voort, stelde de grondverdeling uit, en de tekorten bleven",
            "Ze sloot meteen vrede met Duitsland en gaf alle grond terug aan de oude adel",
            "Ze bracht de tsaar terug op de troon en schafte alle geplande verkiezingen af",
            "Ze voerde de vijfjarenplannen in en dwong de boeren in collectieve bedrijven",
        ],
        0,
        "Oorlog, grond en voedsel bleven onopgelost, en daar speelden de bolsjewieken op in.",
    ),
    koppel(
        "Welke naam hoort bij elke omschrijving uit de jaren 1914 tot 1917?",
        [
            ["De tsaar doet troonsafstand en er komt een voorlopige regering", "Februarirevolutie"],
            ["De bolsjewieken onder Lenin grijpen de macht", "Oktoberrevolutie"],
            ["Het Duitse aanvalsplan om Frankrijk via België snel uit te schakelen", "Plan Von Schlieffen"],
        ],
        ["Collectivisatie", "Veertienpuntenplan"],
        "Twee revoluties in 1917 en het Duitse aanvalsplan van 1914. Collectivisatie hoort pas bij Stalin, het Veertienpuntenplan bij Wilson.",
    ),
    sleep(
        "Lenin vatte zijn belofte samen in drie woorden: vrede, [[brood]] en [[land]]. Na de Oktoberrevolutie volgde geen rust maar een [[burgeroorlog]] van jaren.",
        ["vrijheid", "olie", "wapenstilstand"],
        "Vrede, brood en land sprak de soldaten, arbeiders en boeren aan. De macht moest daarna nog in een burgeroorlog bevochten worden.",
    ),
    mk(
        "Hoe leidde het beleid van Nicolaas II tot de Februarirevolutie?",
        [
            "Hij regeerde alleen en hield vast aan de oorlog, terwijl nederlagen en honger zijn gezag sloopten",
            "Hij gaf de boeren alle grond en sloot meteen vrede, waarna de adel tegen hem in opstand kwam",
            "Hij voerde de vijfjarenplannen in en liet rijke boeren als koelakken deporteren naar verre strafkampen",
            "Hij liet de bolsjewieken van Lenin regeren en trok zich vrijwillig terug uit de hele politiek",
        ],
        0,
        "Een autocraat die een rampzalige oorlog voortzet in een arm land: daar brak het gezag van de tsaar op.",
    ),
    tabel(
        "Kenmerk van het oorlogscommunisme of niet?",
        [
            ("De industrie komt in handen van de staat.", "Kenmerk"),
            ("Graan wordt bij de boeren opgeëist.", "Kenmerk"),
            ("Voedsel wordt op rantsoen gezet.", "Kenmerk"),
            ("Boeren mogen hun graan vrij op de markt verkopen.", "Geen kenmerk"),
        ],
        "In de burgeroorlog nam de staat alles in handen. Vrije handel in graan was er net niet.",
        kolommen=["Kenmerk", "Geen kenmerk"],
    ),
    open_(
        "Geef drie voorbeelden van hoe niet alleen het leger, maar de hele samenleving voor de Eerste Wereldoorlog werd ingezet.",
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
        "Wat dachten veel mensen bij het uitbreken van de oorlog in 1914 over de duur ervan?",
        [
            "Dat hij voor de kerstdagen voorbij zou zijn",
            "Dat hij minstens tien jaar zou duren",
            "Dat hij pas zou eindigen als Amerika meedeed",
            "Dat er nooit echt gevochten zou worden",
        ],
        0,
        "Velen verwachtten een korte oorlog. Het werden ruim vier jaren.",
    ),
    keuze(
        "In 1919 tekende Duitsland het Verdrag van Versailles in de [[*Spiegelzaal|Rijksdag|Volkenbond]], dezelfde zaal waar in [[*1871|1815|1914]] het Duitse Keizerrijk werd uitgeroepen.",
        "Dezelfde zaal, de rollen omgedraaid: de vernedering van Frankrijk in 1871 werd in 1919 de vernedering van Duitsland.",
    ),
    mk(
        "Wat betekent de dictatuur van het proletariaat, zoals Lenin die invoerde?",
        [
            "De arbeidersklasse grijpt in een overgangsfase alle macht",
            "De tsaar regeert met de steun van de arbeiders en boeren",
            "Een verkozen parlement verdeelt de macht over alle partijen",
            "De adel en de kerk nemen samen het bestuur van het land over",
        ],
        0,
        "In naam van de arbeiders nam de partij van Lenin alle macht. Tegenstanders en andere partijen kregen geen ruimte.",
    ),
]
