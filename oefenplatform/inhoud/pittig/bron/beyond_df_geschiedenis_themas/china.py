"""China: van keizerrijk tot wereldmacht — pittig (🌍 Beyond dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-china.svg", zelf=True,
         wat="Tijdlijn van 1945 tot 2025 (Beyond doorstroom).",
         vragen="klikvragen op 1949, 1978 en 1989"),
    dict(bestand="graanoogst-china.svg", zelf=True,
         wat="Grafiek van de graanoogst in China, 1957-1962 (Beyond doorstroom).",
         vragen="klikvraag op het dieptepunt tijdens de Grote Sprong"),
    dict(bestand="culturele-revolutie-affiche.webp", zelf=False,
         wat="Chinese affiche uit de Culturele Revolutie (Beyond doorstroom).",
         vragen="bronvraag over propaganda"),
]

VRAGEN = [
    # --- eeuw van de vernedering
    tabel(
        "Welke uitspraken over de ongelijke verdragen kloppen?",
        [
            ("Westerse burgers vielen in China niet onder de Chinese rechtspraak.", J),
            ("China moest havens openen en lage invoerrechten aanvaarden.", J),
            ("Ze gaven China voorrechten in Europa.", F),
            ("Ze lieten een gevoel van vernedering na.", J),
        ],
        "De voorrechten gingen naar de westerse mogendheden. Men spreekt van de eeuw van de vernedering.",
    ),
    mk(
        "Waarom speelt 'de eeuw van de vernedering' nog mee in de Chinese politiek van vandaag?",
        [
            "De herinnering voedt de wens om sterk te staan",
            "China betaalt nog elk jaar schadevergoeding aan Groot-Brittannië",
            "De ongelijke verdragen zijn nog altijd van kracht",
            "Hongkong is vandaag nog altijd een Britse kolonie",
        ],
        0,
        "Wie zich vernederd voelde, wil nooit meer zwak staan. Dat verhaal gebruikt de Chinese politiek nog.",
    ),
    tabel(
        "Was China rond 1900 een kolonie?",
        [
            ("China bleef formeel zelfstandig.", J),
            ("Mogendheden beheersten invloedssferen met mijnen en spoorwegen.", J),
            ("Eén Europese mogendheid bestuurde heel China.", F),
            ("Men spreekt soms van informeel imperialisme.", J),
        ],
        "Geen bestuur van buiten, maar verdragen en invloedssferen: China werd in stukken verdeeld zonder kolonie te worden.",
    ),
    mk(
        "Een Franse spotprent uit 1898 toont vorsten die met messen een taart met de naam China verdelen. Een Chinese man kijkt machteloos toe. Wat zegt deze bron?",
        [
            "Tijdgenoten zagen China als te verdelen gebied",
            "China verdeelde zelf zijn grondgebied onder zijn provincies",
            "De mogendheden wilden China helpen sterker te worden",
            "China was in 1898 al een communistische staat",
        ],
        0,
        "De taart toont hoe de mogendheden China als buit zagen.",
    ),
    volgorde(
        "Zet in chronologische volgorde.",
        ["Hongkong wordt Brits", "De opstand van de boxers", "Het keizerrijk valt", "De Lange Mars", "De Volksrepubliek wordt uitgeroepen"],
        "1842, 1900, 1911-1912, 1934-1935 en 1949.",
    ),
    mk(
        "Waartegen kwamen de boxers in 1900 in opstand, en hoe liep het af?",
        [
            "Tegen het Westen; ze werden neergeslagen",
            "Tegen de communisten; Mao werd verbannen naar Taiwan",
            "Tegen Japan; Mantsjoerije werd bevrijd",
            "Tegen de keizer; de republiek werd meteen uitgeroepen",
        ],
        0,
        "Een internationaal leger van mogendheden sloeg de opstand neer. Dat toonde opnieuw hoe zwak China stond.",
    ),
    # --- republiek en burgeroorlog
    koppel(
        "Welke persoon hoort bij elke omschrijving?",
        [
            ["Stichter van de republiek en van de Guomindang", "Sun Yat-sen"],
            ["Riep in 1949 de Volksrepubliek uit", "Mao Zedong"],
            ["Zette na 1978 de economische hervormingen in", "Deng Xiaoping"],
        ],
        ["Lenin", "Stalin"],
        "Drie Chinese leiders, drie keerpunten.",
    ),
    tabel(
        "Waarin verschilden de Chinese communisten van Marx?",
        [
            ("Ze steunden vooral op de boeren op het platteland.", J),
            ("Marx rekende vooral op de arbeiders in de fabrieken.", J),
            ("De Chinese communisten wilden het privébezit van fabrieken behouden.", F),
        ],
        "Marx dacht aan het proletariaat van de industriesteden. China was vooral een land van boeren.",
    ),
    mk(
        "Waarom was de Lange Mars belangrijk voor de communisten?",
        [
            "Mao werd er de leider van de partij",
            "De communisten veroverden er Peking mee",
            "Japan gaf zich na de mars over",
            "De nationalisten sloten er vrede mee",
        ],
        0,
        "Op de vlucht uit hun belegerde gebied, duizenden kilometers te voet, groeide Mao uit tot leider.",
    ),
    tabel(
        "Een leerling zegt: \"Voor China begon de Tweede Wereldoorlog in 1939.\" Welke gegevens nuanceren dat?",
        [
            ("Japan bezette Mantsjoerije in 1931.", J),
            ("Japan viel China zelf binnen in 1937.", J),
            ("De oorlog met Japan kostte miljoenen Chinezen het leven.", J),
            ("De Duitse inval in Polen was in 1939.", F),
        ],
        "Voor China begon de oorlog al voor de Duitse inval in Polen. Wanneer een oorlog begint, hangt af van waar je kijkt.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Mao de Volksrepubliek China uitriep.",
        "tijdlijn-china.svg",
        [[7.7, 25, 3.3, 55]],
        "Op 1 oktober 1949. De nationalisten weken uit naar Taiwan.",
    ),
    # --- Mao
    mk(
        "Wat was het plan van de Grote Sprong Voorwaarts van 1958?",
        [
            "China in enkele jaren industrialiseren",
            "Alle fabrieken aan buitenlandse bedrijven verkopen",
            "De boeren hun eigen grond teruggeven",
            "Vrije verkiezingen organiseren op het platteland",
        ],
        0,
        "Het werd een ramp: een hongersnood kostte tientallen miljoenen mensen het leven.",
    ),
    klik(
        "Klik in de grafiek op het jaar met de laagste graanoogst, midden in de Grote Sprong Voorwaarts.",
        "graanoogst-china.svg",
        [[55.0, 10, 12.5, 86]],
        "In 1960 lag de oogst het laagst. De hongersnood kostte tientallen miljoenen levens.",
    ),
    tabel(
        "Welke uitspraken over de Culturele Revolutie kloppen?",
        [
            ("Ze begon in 1966.", J),
            ("Jongeren vielen leraren en ambtenaren aan als vijanden.", J),
            ("Scholen en universiteiten vielen stil.", J),
            ("Ze bracht China vrije verkiezingen.", F),
        ],
        "De jongeren heetten Rode Gardisten. De Culturele Revolutie bracht chaos, geen vrijheid.",
    ),
    met_prent("culturele-revolutie-affiche.webp", mk(
        "Bekijk de affiche uit de Culturele Revolutie. Hoe lees je ze het best?",
        [
            "Als propaganda van de partij",
            "Als kritiek van de Rode Gardisten op Mao",
            "Als een foto van het echte dagelijkse leven",
            "Als een affiche van de Guomindang",
        ],
        0,
        "Een staatsaffiche toont het ideaal van de partij, niet de vervolgingen en gesloten scholen.",
    )),
    tabel(
        "China onder Mao en de Sovjet-Unie onder Stalin: gelijkenis of verschil?",
        [
            ("Eén partij met alle macht", "Gelijkenis"),
            ("Een geplande economie met vijfjarenplannen", "Gelijkenis"),
            ("Terreur tegen tegenstanders", "Gelijkenis"),
            ("Mao mikte eerst op het platteland, Stalin op de zware industrie", "Verschil"),
        ],
        "Het systeem leek sterk op elkaar, de nadruk verschilde.",
        kolommen=["Gelijkenis", "Verschil"],
    ),
    # --- na 1978
    klik(
        "Klik op de tijdlijn op het jaar waarin Deng Xiaoping zijn economische hervormingen begon.",
        "tijdlijn-china.svg",
        [[39.4, 25, 3.3, 55]],
        "1978, twee jaar na de dood van Mao.",
    ),
    sleep(
        "Na 1978 werd China een [[markteconomie]] onder leiding van [[één partij]]. Buitenlandse bedrijven kregen gunstige regels in [[speciale economische zones]], zoals Shenzhen.",
        ["planeconomie", "vrije verkiezingen", "invloedssferen"],
        "Men noemt dat socialisme met Chinese kenmerken: markt ja, politieke vrijheid nee.",
    ),
    tabel(
        "Wat veranderde er na 1978, en wat bleef?",
        [
            ("Markt en buitenlandse bedrijven", "Veranderde"),
            ("De machtspositie van de partij", "Bleef"),
            ("Geen vrije verkiezingen", "Bleef"),
            ("Speciale economische zones", "Veranderde"),
        ],
        "Economisch ging China open, politiek bleef alles bij het oude.",
        kolommen=["Veranderde", "Bleef"],
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin een betoging voor meer vrijheid op het Tiananmenplein met geweld werd beëindigd.",
        "tijdlijn-china.svg",
        [[51.4, 25, 3.3, 55]],
        "Juni 1989. Economische hervorming betekende geen politieke vrijheid.",
    ),
    casus(
        "Lente 1989. Weken lang betogen studenten en arbeiders op het Tiananmenplein in Peking voor persvrijheid en inspraak. In juni wordt de betoging met geweld beëindigd.",
        [
            mk(
                "Wat toont deze gebeurtenis over het Chinese model na 1978?",
                [
                    "De partij duldde geen tegenmacht",
                    "De partij organiseerde snel vrije verkiezingen",
                    "De studenten kregen al hun eisen ingewilligd",
                    "China werd daarna opnieuw een keizerrijk",
                ],
                0,
                "Markteconomie, maar één partij. Politieke tegenmacht werd niet geduld.",
            ),
            mk(
                "Waarom is een Chinees schoolboek een zwakke bron om te weten wat er in juni 1989 gebeurde?",
                [
                    "De staat bepaalt wat erin staat",
                    "Schoolboeken gaan nooit over geschiedenis",
                    "Het boek werd te snel na de feiten geschreven",
                    "Chinese schoolboeken zijn in het Engels geschreven",
                ],
                0,
                "Censuur maakt een bron zwak voor deze vraag. Je zoekt dan ooggetuigen en buitenlandse verslagen.",
            ),
        ],
    ),
    keuze(
        "Hongkong werd in [[*1842|1949|1911]] Brits en in [[*1997|1978|1989]] opnieuw een deel van China, met een eigen statuut.",
        "Na meer dan 150 jaar kwam de stad terug: het einde van een symbool van de vernedering.",
    ),
    tabel(
        "Welke uitspraken over China vandaag kloppen?",
        [
            ("Het is een van de grootste economieën ter wereld.", J),
            ("Het is een van de grootste uitstoters van broeikasgassen.", J),
            ("De uitstoot per inwoner ligt lager dan in sommige rijke landen.", J),
            ("De eenkindpolitiek geldt vandaag nog.", F),
        ],
        "De eenkindpolitiek gold van 1979 tot 2015.",
    ),
    mk(
        "Wat wil China bereiken met de Nieuwe Zijderoute?",
        [
            "Handel en politieke invloed vergroten",
            "Zijn eigen havens sluiten voor buitenlandse schepen",
            "De ongelijke verdragen opnieuw invoeren",
            "Hongkong teruggeven aan Groot-Brittannië",
        ],
        0,
        "Havens, spoorlijnen en wegen naar Azië, Afrika en Europa: zo groeit ook de politieke invloed van China.",
    ),
    inv(
        "Hoe noemt men de Chinese regel die van 1979 tot 2015 gold en de bevolkingsgroei moest afremmen?",
        ["de eenkindpolitiek", "eenkindpolitiek", "eenkindbeleid", "het eenkindbeleid"],
        "Een gezin mocht maar één kind hebben.",
    ),
    open_(
        "Leg uit waarom men de geschiedenis van China in de negentiende eeuw een voorbeeld van informeel imperialisme noemt.",
        "China werd niet volledig de kolonie van één mogendheid en bleef formeel zelfstandig. Maar in de Opiumoorlogen werd China gedwongen zijn markt te openen, met de ongelijke verdragen kregen westerse mogendheden havens, lage invoerrechten en eigen rechtspraak, en rond 1900 verdeelden ze China in invloedssferen met mijnen en spoorwegen. Het imperialisme kwam dus via verdragen en invloed, niet via een bestuur van buiten.",
    ),
    open_(
        "Vergelijk China onder Mao met China na 1978. Geef een verschil en een gelijkenis.",
        "Verschil: onder Mao plande de staat de economie en nam hij de grond in bezit; na 1978 kwamen markt en buitenlandse bedrijven in speciale economische zones. Gelijkenis: in beide periodes had één partij alle macht en waren er geen vrije verkiezingen, wat ook bleek op het Tiananmenplein in 1989.",
    ),
    sorteer(
        "In welk domein situeer je elke gebeurtenis?",
        ["Politiek", "Economisch", "Sociaal"],
        [
            ["de Volksrepubliek wordt uitgeroepen", "Politiek"],
            ["de speciale economische zones", "Economisch"],
            ["de eenkindpolitiek", "Sociaal"],
            ["de Opiumoorlogen om de markt te openen", "Economisch"],
            ["de betoging op het Tiananmenplein", "Politiek"],
        ],
        "Macht en bestuur zijn politiek, handel en bedrijven economisch, gezin en bevolking sociaal.",
    ),
    mk(
        "Waarom weken de nationalisten in 1949 uit naar Taiwan?",
        [
            "Ze hadden de burgeroorlog verloren",
            "Japan had hun Taiwan als geschenk gegeven",
            "Mao had hen uitgenodigd om daar te regeren",
            "Taiwan was de hoofdstad van het keizerrijk",
        ],
        0,
        "Na de burgeroorlog tussen 1927 en 1949 wonnen de communisten. De Guomindang trok zich terug op het eiland.",
    ),
]
