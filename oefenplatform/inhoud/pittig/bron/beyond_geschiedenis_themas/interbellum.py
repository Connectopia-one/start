"""Interbellum: totalitarisme en crisis — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, met_prent

PRENTEN = [
    dict(bestand="stalin-affiche.webp", zelf=False,
         wat="Gustav Klutsis, Kaders beslissen alles (1935): Stalin met arbeiders, piloten en kinderen.",
         waar="Wikimedia Commons, zoek 'Stalin poster five-year plan' of 'Soviet propaganda poster 1930s Stalin'.",
         vragen="casus over propaganda en personencultus"),
]

VRAGEN = [
    tabel(
        "Welke oorzaken van de beurscrash van 1929 kloppen?",
        [
            ("Aandelen werden gekocht met geleend geld.", J),
            ("Er was overproductie in industrie en landbouw.", J),
            ("De welvaart was zeer ongelijk verdeeld.", J),
            ("De Verenigde Staten hadden net een oorlog verloren.", F),
        ],
        "Lenen om aandelen te kopen, overproductie en ongelijkheid maakten de economie kwetsbaar. Een verloren oorlog speelde geen rol.",
    ),
    mk(
        "Hoe hangt de crisis van de jaren dertig samen met de opkomst van extreme partijen in Europa?",
        [
            "Werkloosheid en armoede maakten mensen vatbaar voor wie orde beloofde",
            "De crisis bleef beperkt tot de VS, dus er was in Europa geen verband",
            "Extreme partijen veroorzaakten de beurscrash van Wall Street zelf",
            "Door de crisis kregen democratische partijen net veel meer kiezers",
        ],
        0,
        "Wie zijn werk verliest en geen uitweg ziet, luistert sneller naar wie orde en werk belooft.",
    ),
    keuze(
        "Leg je uit hoe de crisis leidde tot steun voor extreme partijen, dan gebruik je de redeneerwijze [[*oorzaak en gevolg benoemen|stereotypering analyseren|actualiseren]].",
        "Je toont een verband tussen een toestand (crisis) en wat eruit volgde (radicalisering).",
    ),
    tabel(
        "Hoorde de maatregel bij de New Deal in de Verenigde Staten?",
        [
            ("Grote openbare werken om mensen aan het werk te zetten", J),
            ("Toezicht op de banken en de beurs", J),
            ("De eerste federale sociale zekerheid", J),
            ("Alle fabrieken onder het bezit van de staat brengen", F),
        ],
        "De New Deal brak met het idee dat de overheid zich niet met de economie moest bemoeien, maar de fabrieken bleven privé.",
    ),
    mk(
        "Waarom trof de crisis van de jaren dertig de Sovjet-Unie veel minder hard dan het Westen?",
        [
            "Haar economie werd buiten de wereldmarkt om gepland",
            "Ze had in die jaren de grootste beurs ter wereld",
            "Ze leende in die jaren veel geld aan Amerikaanse banken",
            "Ze voerde net zoals de VS een New Deal in, maar sneller",
        ],
        0,
        "Een planeconomie hing niet aan de wereldmarkt. Dat gaf het stelsel toen een aantrekkingskracht die achteraf moeilijk voor te stellen is.",
    ),
    sorteer(
        "Bij welk beleid van Stalin hoort elke maatregel?",
        ["Economisch", "Politiek", "Cultureel"],
        [
            ["Plannen van vijf jaar voor de zware industrie", "Economisch"],
            ["De landbouw onder controle van de staat brengen", "Economisch"],
            ["Strafkampen en zuiveringen tegen tegenstanders", "Politiek"],
            ["De leider op affiches als onfeilbaar voorstellen", "Cultureel"],
            ["Kunst die de arbeider en de opbouw verheerlijkt", "Cultureel"],
        ],
        "Industrie en landbouw zijn economisch, terreur politiek, en beeldvorming en kunst horen bij het culturele beleid.",
    ),
    tabel(
        "Welke gevolgen had de collectivisatie in de Sovjet-Unie?",
        [
            ("Verzet van boeren dat met geweld gebroken werd", J),
            ("Deportatie van rijkere boeren", J),
            ("Een zware hongersnood, onder meer in Oekraïne", J),
            ("Meer vrije markten waar boeren hun graan konden verkopen", F),
        ],
        "De dwang en de hongersnood kostten miljoenen mensen het leven.",
    ),
    casus(
        "Bekijk de Sovjet-affiche uit 1935. De titel betekent: Kaders beslissen alles. Stalin staat groot in beeld, omringd door lachende arbeiders, piloten en kinderen.",
        [
            met_prent("stalin-affiche.webp", keuze(
                "De affiche toont Stalin als bijna bovenmenselijke leider. Dat noemt men een [[*personencultus|collectivisatie|appeasement]]. De bedoeling is het bewind te [[*verheerlijken|bekritiseren|neutraal beschrijven]].",
                "De leider wordt voorgesteld als onfeilbaar. Propaganda moet steun en bewondering opwekken.",
            ), volgt=True),
            mk(
                "In welke maatschappelijke domeinen kan je deze affiche situeren? (meerdere antwoorden)",
                ["Politiek", "Cultureel", "Economisch", "In geen enkel domein"],
                [0, 1],
                "Ze verheerlijkt de leider en zijn bewind (politiek) en werkt met beeldtaal en een wereldbeeld (cultureel). Fabrieken of productiecijfers zie je op deze affiche niet.",
            ),
            tabel(
                "Mag je dit besluiten op basis van de affiche alleen?",
                [
                    ("Het regime wilde Stalin tonen als geliefde leider van het hele volk.", "Mag"),
                    ("Alle arbeiders in de Sovjet-Unie waren gelukkig.", "Mag niet"),
                    ("Stalin gebruikte propaganda om zijn beleid te steunen.", "Mag"),
                ],
                "Propaganda is een slechte bron over hoe het echt was, maar een uitstekende bron over wat het regime wilde laten geloven.",
                kolommen=["Mag", "Mag niet"],
            ),
        ],
    ),
    tabel(
        "Waaraan herken je een totalitaire staat?",
        [
            ("Eén partij en één leider", J),
            ("Controle over pers, onderwijs en kunst", J),
            ("Een geheime politie die tegenstanders uitschakelt", J),
            ("Vrije verkiezingen tussen meerdere partijen", F),
        ],
        "Een totalitaire staat wil alles beheersen. Vrije verkiezingen passen daar niet in.",
    ),
    mk(
        "Een leerling zegt: \"Een regime gebruikt ofwel propaganda, ofwel terreur.\" Wat is de beste verbetering?",
        [
            "Totalitaire regimes gebruiken ze naast elkaar: de ene hand lokt, de andere dreigt",
            "Klopt: propaganda hoort enkel bij democratieën en terreur enkel bij dictaturen, nooit samen",
            "Klopt: Stalin gebruikte alleen terreur en Hitler gebruikte alleen propaganda",
            "Propaganda en terreur bestonden in de jaren dertig nog niet als begrip",
        ],
        0,
        "Stalin, Mussolini en Hitler gebruikten allebei: propaganda om te overtuigen, terreur om tegenstand te breken.",
    ),
    volgorde(
        "Zet deze gebeurtenissen uit het interbellum in de juiste volgorde.",
        ["De Mars op Rome", "De dood van Lenin", "De start van de eerste vijfjarenplannen", "De beurscrash van Wall Street", "Hitler wordt rijkskanselier"],
        "1922, 1924, 1928, oktober 1929 en januari 1933.",
    ),
    tabel(
        "Wat deed Mussolini om van Italië een totalitaire staat te maken?",
        [
            ("Hij verbood de andere partijen.", J),
            ("Hij bracht de pers onder controle.", J),
            ("Hij richtte een politieke politie op.", J),
            ("Hij liet de koning alle macht uitoefenen.", F),
        ],
        "Partijen verbieden, de pers controleren en een politieke politie: zo nam de Duce alle macht.",
    ),
    koppel(
        "Welke leider hoort bij elke omschrijving?",
        [
            ["Noemde zich de Duce en kwam na de Mars op Rome aan de macht", "Mussolini"],
            ["Leidde de bolsjewieken en stierf in het begin van het interbellum", "Lenin"],
            ["Werd in januari 1933 rijkskanselier", "Hitler"],
            ["Lanceerde vanaf 1933 de New Deal", "Roosevelt"],
        ],
        ["Stalin"],
        "Vier leiders van het interbellum. Stalin volgde Lenin op.",
    ),
    volgorde(
        "Zet de stappen waarmee Hitler in 1933 en 1934 alle macht greep in de juiste volgorde.",
        ["Hitler wordt rijkskanselier", "De Rijksdag brandt af en de grondrechten worden opgeschort", "De Machtigingswet laat hem zonder parlement regeren", "Na de dood van Hindenburg voegt hij het presidentschap bij zijn ambt"],
        "Januari 1933, februari 1933, de Machtigingswet in 1933, en in 1934 na de dood van Hindenburg.",
    ),
    mk(
        "Hoe daalde de werkloosheid in nazi-Duitsland?",
        [
            "Met openbare werken en vooral met herbewapening",
            "Door alle fabrieken aan de arbeiders te geven",
            "Door de beurs van Berlijn volledig te sluiten",
            "Door alle vrouwen verplicht te laten werken",
        ],
        0,
        "Herbewapening gaf veel mensen werk, maar was ook een voorbereiding op oorlog.",
    ),
    sorteer(
        "Met welk middel hield het naziregime de bevolking in de pas?",
        ["Propaganda", "Jeugdbeweging", "Terreur"],
        [
            ["Films, radio en kranten die het regime verheerlijken", "Propaganda"],
            ["Kinderen moeten verplicht bij de Hitlerjugend", "Jeugdbeweging"],
            ["Een geheime politie en concentratiekampen", "Terreur"],
        ],
        "Overtuigen via pers, film en radio, opvoeden via de jeugdbeweging en dreigen met geheime politie en kampen.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over de vervolging van de Joden in de jaren dertig.",
        [
            ("Door de Neurenbergse wetten van 1935 verloren Joden hun burgerrechten.", J),
            ("Joden mochten na 1935 niet meer huwen met niet-Joden.", J),
            ("In de nacht van 9 op 10 november 1938 werden synagogen in brand gestoken.", J),
            ("Joden kregen in 1935 extra rechten om hen in Duitsland te houden.", F),
        ],
        "Stap voor stap werden Joden uitgesloten: eerst met wetten, dan met geweld zoals in november 1938.",
    ),
    mk(
        "Waarin verschilde het nationaalsocialisme vooral van het Italiaanse fascisme?",
        [
            "De rassenleer en het antisemitisme stonden centraal",
            "Het nationaalsocialisme had geen leider en geen partij",
            "Het Italiaanse fascisme liet vrije verkiezingen toe",
            "Het nationaalsocialisme gebruikte geen propaganda",
        ],
        0,
        "Het verschil zat in de rassenleer, die bij de nazi's centraal stond.",
    ),
    sorteer(
        "Gelijkenis of verschil tussen het stalinisme, het fascisme en het nationaalsocialisme?",
        ["Gelijkenis", "Verschil"],
        [
            ["Eén partij en één leider", "Gelijkenis"],
            ["Geen ruimte voor tegenspraak", "Gelijkenis"],
            ["Een planeconomie met collectieve landbouw", "Verschil"],
            ["Een leider die geen tegenspraak duldt en de pers controleert", "Gelijkenis"],
        ],
        "Alle drie zijn totalitair. De planeconomie hoort enkel bij de Sovjet-Unie.",
    ),
    volgorde(
        "Zet de stappen waarmee Hitler de afspraken van Versailles aantastte in de juiste volgorde.",
        ["Opnieuw dienstplicht en herbewapening", "Troepen trekken het Rijnland binnen", "Oostenrijk wordt ingelijfd", "De Conferentie van München", "Het niet-aanvalspact met de Sovjet-Unie"],
        "Van 1935 tot augustus 1939: eerst het leger, dan het Rijnland, Oostenrijk, het Sudetenland en tot slot het pact met Stalin.",
    ),
    mk(
        "Wat werd op de Conferentie van München in september 1938 beslist?",
        [
            "Duitsland mocht het Sudetenland van Tsjecho-Slowakije inlijven",
            "Duitsland moest het Rijnland opnieuw aan Frankrijk afstaan",
            "Duitsland en de Sovjet-Unie verdeelden samen Polen",
            "Italië en Duitsland verklaarden de oorlog aan Groot-Brittannië",
        ],
        0,
        "Frankrijk en Groot-Brittannië gaven toe om oorlog te vermijden.",
    ),
    keuze(
        "De politiek waarbij Frankrijk en Groot-Brittannië toegaven om een oorlog te vermijden, heet [[*appeasement|collectivisatie|unionisme]]. Ze bereikte haar doel [[*niet|wel|half]], want een jaar later brak de oorlog uit.",
        "Na München vroeg Hitler steeds meer. In september 1939 viel hij Polen binnen.",
    ),
    mk(
        "Waarom was het niet-aanvalspact van augustus 1939 tussen Duitsland en de Sovjet-Unie zo verrassend?",
        [
            "Twee aartsvijanden spraken een geheime verdeling van Polen af",
            "Het waren twee democratieën die normaal nooit verdragen met elkaar sloten",
            "Het pact maakte een einde aan de Tweede Wereldoorlog nog voor die begon",
            "Het pact gaf Polen de garantie dat het nooit aangevallen zou worden",
        ],
        0,
        "Communisme en nationaalsocialisme stonden tegenover elkaar, maar het pact gaf Hitler vrij spel. Amper een week later viel hij Polen binnen.",
    ),
    tabel(
        "Juist of fout? Lees elke uitspraak over het interbellum.",
        [
            ("Ook de democratieën in West-Europa bleven niet onaangeroerd door crisis en extreme partijen.", J),
            ("Mussolini werd na de Mars op Rome door de koning tot regeringsleider benoemd.", J),
            ("Hitler kwam in 1933 aan de macht door een gewapende staatsgreep.", F),
            ("De Grote Zuivering trof ook partijgenoten en legerofficieren.", J),
        ],
        "Hitler werd benoemd tot rijkskanselier en nam daarna stap voor stap alle macht. Stalins zuiveringen troffen ook zijn eigen partij.",
    ),
    open_(
        "Leg uit hoe Stalin propaganda gebruikte om zijn beleid te steunen. Gebruik twee voorbeelden.",
        "Stalin liet zich voorstellen als een onfeilbare, bijna bovenmenselijke leider: een personencultus. Affiches en kunst in de stijl van het socialistisch realisme verheerlijkten de arbeiders en de opbouw van het land, zoals de vijfjarenplannen. Zo moest de bevolking geloven dat het beleid slaagde, terwijl terreur en goelags de tegenstanders uitschakelden.",
    ),
    open_(
        "Leg het verband uit tussen de sociaaleconomische toestand tijdens het interbellum en de opkomst van de NSDAP.",
        "Na de crisis van 1929 kwamen in Duitsland miljoenen mensen zonder werk. Daarbij kwam de wrok over het Verdrag van Versailles. Werkloosheid en armoede maakten mensen vatbaar voor een partij die orde, werk en nationale trots beloofde. Zo groeide de NSDAP en werd Hitler in 1933 rijkskanselier.",
    ),
    inv(
        "Hoe heten de strafkampen in de Sovjet-Unie waar gevangenen dwangarbeid verrichtten? (meervoud)",
        "goelags",
        "In de goelags belandden miljoenen mensen, ook gewone burgers die als vijand van het volk werden aangeduid.",
    ),
    sleep(
        "Collectivisatie is het samenvoegen van kleine [[boerderijen]] tot grote bedrijven van staat of gemeenschap. Wie als [[koelak]] werd aangeduid, werd gedeporteerd. De kunst heette [[socialistisch]] realisme.",
        ["fabrieken", "bolsjewiek", "fascistisch"],
        "Collectivisatie gaat over landbouw. Koelak was het etiket voor rijkere boeren. Het socialistisch realisme verheerlijkte de arbeider.",
    ),
]
