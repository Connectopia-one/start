"""Congo: van Congo-Vrijstaat tot Belgisch Congo — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="rubber-coils.webp", zelf=False,
         wat="Spotprent 'In the Rubber Coils', Punch 1906.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="casus over de kritiek op de Vrijstaat"),
    dict(bestand="afrika-1914.webp", zelf=False,
         wat="Kaart van Afrika in 1914.",
         waar="Staat al op het platform (Beyond doorstroom).",
         vragen="klikvraag op Katanga"),
]

VRAGEN = [
    # --- Vrijstaat
    tabel(
        "Een leerling zegt: \"Vanaf 1885 was Congo een Belgische kolonie.\" Welke gegevens spreken dat tegen?",
        [
            ("Leopold II was in persoon de eigenaar.", J),
            ("Het Belgische parlement had er geen zeg in.", J),
            ("Pas in 1908 nam de Belgische staat het gebied over.", J),
            ("Stanley verkende het gebied in opdracht van de koning.", F),
        ],
        "Tot 1908 was de Congo-Vrijstaat persoonlijk bezit van Leopold II. Dat Stanley in zijn opdracht werkte, spreekt dat niet tegen.",
    ),
    mk(
        "Stanley liet plaatselijke leiders verdragen ondertekenen. Wat is daar het probleem mee?",
        [
            "Ze konden die verdragen vaak niet lezen",
            "Ze kregen er altijd een eerlijke prijs voor hun land voor",
            "De verdragen werden door het Belgische parlement goedgekeurd",
            "Stanley ondertekende de verdragen in naam van Frankrijk",
        ],
        0,
        "Van echte instemming was geen sprake als je niet weet wat je tekent.",
    ),
    tabel(
        "Leopold II vertelde Europa waarom hij in Congo was. Welke redenen gaf hij, en welke waren de echte winstbronnen?",
        [
            ("de strijd tegen de slavenhandel", "Officiële reden"),
            ("de beschaving brengen", "Officiële reden"),
            ("rubber uit de wilde lianen", "Winstbron"),
            ("ivoor van olifanten", "Winstbron"),
        ],
        "Tegenover Europa sprak hij over beschaving en slavenhandel. De winst kwam van rubber en ivoor.",
        kolommen=["Officiële reden", "Winstbron"],
    ),
    mk(
        "Waarom steeg de vraag naar rubber rond 1900 zo sterk?",
        [
            "Fietsen en auto's hadden rubber nodig",
            "Rubber werd gebruikt om de spoorwegen te bouwen in heel Europa",
            "Missionarissen gebruikten het om kerken te bouwen",
            "Het werd gegeten in tijden van honger",
        ],
        0,
        "De tweede industriële revolutie bracht fietsen en auto's, met banden van rubber.",
    ),
    mk(
        "Waarom moesten soldaten van de Force Publique een hand inleveren voor elke kogel?",
        [
            "Om te bewijzen dat geen kogel verspild was",
            "Omdat de koning zelf de handen wilde zien in Brussel",
            "Omdat de wet van 1889 dat verplichtte",
            "Om de dorpen te belonen voor hun rubber",
        ],
        0,
        "Kogels waren duur. Zo werden handen een bewijsstuk, en ook een straf voor wie het quotum niet haalde.",
    ),
    koppel(
        "Welk begrip hoort bij elke omschrijving?",
        [
            ["Leger en politie van de Vrijstaat", "Force Publique"],
            ["Zweep van gedroogde huid", "Chicotte"],
            ["De hoeveelheid rubber die een dorp moest leveren", "Quotum"],
            ["Ander woord voor rubber", "Caoutchouc"],
        ],
        ["Évolué", "Protectoraat"],
        "Vier begrippen uit de Vrijstaat. Évolués horen bij Belgisch Congo, een protectoraat is een andere vorm van overheersing.",
    ),
    casus(
        "Bekijk de spotprent uit het Britse blad Punch van 1906. Een slang met het hoofd van Leopold II heeft zich rond een Congolese man gewonden. Het onderschrift luidt: In the Rubber Coils.",
        [
            met_prent("rubber-coils.webp", mk(
                "Waarop doelt de tekenaar met de slang?",
                ["Op het rubberregime dat de bevolking verstikte", "Op de missiescholen die overal in Congo kwamen", "Op de spoorlijnen die Stanley aanlegde", "Op de handel in koper uit Katanga"],
                0,
                "De slang met het hoofd van de koning staat voor het systeem dat de bevolking in de greep hield.",
            )),
            mk(
                "Waarom moet je deze Britse bron kritisch lezen?",
                [
                    "Groot-Brittannië had zelf kolonies en concurrenten",
                    "Britten konden niet tekenen",
                    "Punch was een Belgisch blad van de koning",
                    "Er bestaan geen andere bronnen over de Vrijstaat",
                ],
                0,
                "Ook een Brits blad had een belang. Daarom toets je de bron aan missieverslagen en foto's.",
            ),
            tabel(
                "Welke uitspraken over de kritiek op de Vrijstaat kloppen?",
                [
                    ("Ze kwam vooral uit het buitenland.", J),
                    ("De journalist Morel bracht de feiten naar buiten.", J),
                    ("Consul Casement schreef er een verslag over.", J),
                    ("Missionarissen speelden geen enkele rol.", F),
                ],
                "Morel, Casement en missionarissen met foto's zetten druk. In 1908 nam België de kolonie over.",
            ),
        ],
    ),
    mk(
        "Je ziet een foto uit 1904 van een Congolese man met een verminkte hand. Wat bewijst die foto, en wat niet?",
        [
            "Verminking kwam voor, maar het dodental zegt ze niet",
            "Ze bewijst dat alle Congolezen een verminkte hand hadden",
            "Ze bewijst dat de koning de verminkingen zelf uitvoerde",
            "Ze bewijst niets, want foto's zijn nooit een bron",
        ],
        0,
        "Eén foto toont dat het gebeurde. Hoe vaak, en hoeveel doden er vielen, moet je uit andere bronnen halen.",
    ),
    tabel(
        "Welke uitspraken over de gevolgen voor de bevolking van de Vrijstaat kloppen?",
        [
            ("Geweld, honger en ziekte troffen de bevolking zwaar.", J),
            ("Schattingen van het dodental lopen uiteen.", J),
            ("Sommige schattingen gaan tot in de miljoenen.", J),
            ("Historici zijn het over het precieze dodental volledig eens.", F),
        ],
        "Er zijn geen volkstellingen uit die tijd, daarom lopen de schattingen uiteen.",
    ),
    # --- overgang
    volgorde(
        "Zet in de juiste volgorde.",
        ["De Conferentie van Berlijn", "Het rapport van Casement", "De Belgische staat neemt Congo over", "Uranium uit Shinkolobwe voor de atoombom", "De eerste universiteiten in Congo"],
        "1884-1885, 1904, 1908, de Tweede Wereldoorlog en de jaren vijftig.",
    ),
    mk(
        "Veranderde er voor de Congolezen veel door de overname van 1908?",
        [
            "Weinig: verplichte arbeid en teelten bleven",
            "Alles: vanaf 1908 kregen ze stemrecht in Brussel",
            "Alles: alle dwangarbeid verdween meteen voorgoed",
            "Niets: Leopold II bleef de eigenaar tot 1960",
        ],
        0,
        "De ergste wandaden van de Vrijstaat stopten, maar verplichte arbeid en verplichte teelten bleven bestaan.",
    ),
    # --- Belgisch Congo
    sorteer(
        "Welke macht van het koloniale drieluik hoort bij elk voorbeeld?",
        ["De staat", "De kerk", "De bedrijven"],
        [
            ["de gouverneur-generaal", "De staat"],
            ["de minister van Koloniën", "De staat"],
            ["de missiescholen", "De kerk"],
            ["de missiehospitalen", "De kerk"],
            ["de Union Minière", "De bedrijven"],
        ],
        "De staat bestuurde, de kerk verzorgde onderwijs en zorg, de bedrijven haalden de grondstoffen.",
    ),
    klik(
        "Bekijk de kaart van Afrika in 1914. Klik op de kolonie waartoe Katanga met zijn kopermijnen behoorde.",
        "afrika-1914.webp",
        [[50.5, 44.5, 17.5, 22]],
        "Katanga ligt in het zuidoosten van Congo, het gele vlak. De Union Minière du Haut-Katanga werd er een van de grootste mijnbedrijven ter wereld.",
    ),
    keuze(
        "Katanga was waardevol door zijn [[*koper|rubber|katoen]]. In de Tweede Wereldoorlog werd [[*uranium|ivoor|steenkool]] uit Shinkolobwe gebruikt voor de eerste atoombommen.",
        "Koper bracht Katanga zijn rijkdom, uranium gaf het een rol in de wereldpolitiek.",
    ),
    casus(
        "Een Congolese klerk in Léopoldville schrijft in 1955: \"Ik heb op de missieschool leren lezen en schrijven. Ik werk bij het bestuur. Maar 's avonds mag ik niet in de Europese stad komen, en over de wetten die ons regeren, mag ik niet meebeslissen.\"",
        [
            inv(
                "Hoe noemde men Congolezen zoals deze klerk, met een opleiding en een baan in het bestuur?",
                ["évolués", "evolués", "evolues", "de évolués", "een évolué", "évolué"],
                "De évolués waren een kleine middengroep. Juist uit hun rangen kwam de eis voor onafhankelijkheid.",
            ),
            tabel(
                "Welke kenmerken van Belgisch Congo herken je in de bron?",
                [
                    ("Het onderwijs lag bij de missies.", J),
                    ("Er was een avondklok voor Congolezen in de Europese stad.", J),
                    ("Congolezen hadden geen politieke rechten.", J),
                    ("Congolezen konden stemmen voor het parlement in Brussel.", F),
                ],
                "Zorg en onderwijs wel, zeggenschap niet: dat is paternalisme.",
            ),
            mk(
                "Waarom is het niet toevallig dat de eis voor onafhankelijkheid uit deze groep kwam?",
                [
                    "Ze hadden een opleiding, maar geen rechten",
                    "Ze waren de rijkste groep in heel Congo",
                    "Ze waren allemaal in België geboren",
                    "Ze werkten voor de Union Minière in Brussel",
                ],
                0,
                "Wie opgeleid is en toch niet mag meebeslissen, ziet het onrecht scherp.",
            ),
        ],
    ),
    mk(
        "Wat betekent het dat het Belgische bestuur in Congo paternalistisch was?",
        [
            "Het zorgde voor de bevolking, maar liet haar niet meebeslissen",
            "Het liet de Congolezen zelf hun regering kiezen en volgde hun wensen",
            "Het gaf de bevolking geen scholen en geen hospitalen",
            "Het liet alle beslissingen over aan de Congolese vorsten",
        ],
        0,
        "Men behandelde de bevolking als kinderen die geleid moeten worden.",
    ),
    tabel(
        "In Europa heette Congo een modelkolonie. Welke gegevens gebruikte men voor dat beeld, en welke liet men weg?",
        [
            ("Er waren scholen en hospitalen.", "Gebruikt"),
            ("De mijnen maakten winst.", "Gebruikt"),
            ("Congolezen hadden geen stemrecht.", "Weggelaten"),
            ("Belgen en Congolezen woonden gescheiden.", "Weggelaten"),
        ],
        "Het beeld van de modelkolonie hield geen rekening met het ontbreken van rechten.",
        kolommen=["Gebruikt", "Weggelaten"],
    ),
    mk(
        "Waarom had Congo in 1960 amper eigen artsen en ingenieurs?",
        [
            "De eerste universiteiten kwamen er pas in de jaren vijftig",
            "Het lager onderwijs bereikte bijna geen kinderen",
            "Congolese studenten mochten niet lezen leren",
            "Alle artsen waren na 1908 naar België verhuisd",
        ],
        0,
        "Het lager onderwijs van de missies bereikte veel kinderen, maar hoger onderwijs kwam te laat.",
    ),
    casus(
        "Een Belgisch schoolboek uit 1950 schrijft: \"België heeft Congo de beschaving geschonken. Waar vroeger wildernis was, staan nu scholen, kerken en fabrieken.\"",
        [
            mk(
                "Hoe lees je deze bron het best?",
                [
                    "Als beeldvorming van de kolonisator over zichzelf",
                    "Als betrouwbaar verslag van wat de Congolezen dachten",
                    "Als bewijs dat Congo vóór 1885 leeg was",
                    "Als een Congolese bron uit de tijd van de Vrijstaat",
                ],
                0,
                "Het boek is een goede bron over België in 1950, en een slechte over Congo.",
            ),
            tabel(
                "Wat laat het schoolboek weg?",
                [
                    ("De wandaden onder de Vrijstaat", J),
                    ("Het ontbreken van politieke rechten", J),
                    ("De gescheiden wijken in de steden", J),
                    ("De scholen van de missies", F),
                ],
                "De scholen staan er net in. Wat het eigen beeld schaadt, blijft weg.",
            ),
        ],
    ),
    sorteer(
        "In welk domein situeer je elk kenmerk van Congo?",
        ["Economisch", "Politiek", "Sociaal"],
        [
            ["rubber en ivoor als winst", "Economisch"],
            ["de koper van de Union Minière", "Economisch"],
            ["geen stemrecht voor Congolezen", "Politiek"],
            ["een gouverneur-generaal uit Brussel", "Politiek"],
            ["gescheiden wijken in de steden", "Sociaal"],
        ],
        "Winst is economisch, bestuur en rechten zijn politiek, het samenleven in de stad is sociaal.",
    ),
    open_(
        "Toon met twee argumenten dat Belgisch Congo een voorbeeld is van het modern imperialisme.",
        "Het gebied werd door een vreemde staat bezet en bestuurd, met een gouverneur-generaal uit Brussel en zonder rechten voor de Congolezen. De economie draaide op de uitvoer van grondstoffen zoals koper en uranium naar het buitenland, in plaats van op eigen industrie. Ook de beschavingsmissie diende als rechtvaardiging.",
    ),
    open_(
        "Vergelijk de Congo-Vrijstaat met Belgisch Congo. Geef een verschil en een gelijkenis.",
        "Verschil: de Vrijstaat was persoonlijk bezit van Leopold II, met extreem geweld voor rubber; Belgisch Congo werd bestuurd door de Belgische staat, samen met kerk en bedrijven, met scholen en hospitalen. Gelijkenis: in beide hadden de Congolezen geen zeggenschap, bleef er verplichte arbeid, en was de economie gericht op uitvoer van grondstoffen.",
    ),
    sleep(
        "De Britse journalist [[Morel]] en de Britse consul [[Casement]] brachten de wandaden naar buiten. Onder die druk nam de Belgische staat Congo in [[1908]] over.",
        ["Stanley", "Bismarck", "1885"],
        "Stanley verkende Congo voor de koning, Bismarck zat de Conferentie van Berlijn voor.",
    ),
    mk(
        "Leopold II bezocht Congo nooit. Wat zegt dat over zijn onderneming?",
        [
            "Hij bestuurde het als een bezit op afstand",
            "Hij was er niet in geïnteresseerd en verdiende er niets aan",
            "Hij liet de Congolezen zelf alle beslissingen nemen",
            "Hij had Congo al in 1885 aan de Belgische staat gegeven",
        ],
        0,
        "Leopold II bestuurde de Vrijstaat vanuit Brussel, met Stanley, de Force Publique en agenten ter plaatse.",
    ),
    tabel(
        "Welke uitspraken over de steden in Belgisch Congo kloppen?",
        [
            ("Belgen en Congolezen woonden in aparte wijken.", J),
            ("Elke wijk had eigen voorzieningen.", J),
            ("Congolezen mochten 's avonds vrij door de Europese stad.", F),
        ],
        "Er gold een avondklok voor Congolezen in de Europese stad.",
    ),
]
