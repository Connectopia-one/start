"""De Volksrepubliek China: van Mao tot Xi — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="culturele-revolutie-affiche.webp", zelf=False,
         wat="Een Chinese affiche uit de Culturele Revolutie (1966-1976) met Rode Gardisten en het Rode Boekje of een portret van Mao.",
         waar="Wikimedia Commons, zoek op 'Cultural Revolution poster' of 'Red Guards poster'. Enkel met PD-China of publiek domein.",
         vragen="bronvraag over persoonsverheerlijking en doelpubliek"),
    dict(bestand="graanoogst-china.svg", zelf=True,
         wat="Grafiek van de graanoogst in China van 1957 tot 1962.",
         vragen="klikvraag op het dieptepunt en waarom de Grote Sprong tot achteruitgang leidt"),
    dict(bestand="tijdlijn-china.svg", zelf=True,
         wat="Tijdlijn van 1945 tot 2025 met een streepje per jaar.",
         vragen="klikvragen op 1949 en 1989"),
]

VRAGEN = [
    # ------------------------------------------------ de machtsovername door Mao
    tabel(
        "Juist of fout? De weg naar de communistische machtsovername.",
        [
            ("Communisten en nationalisten van de Guomindang vochten jarenlang een burgeroorlog uit.", J),
            ("Tijdens de Japanse inval vanaf 1937 sloten beide partijen tijdelijk een bondgenootschap.", J),
            ("De communisten haalden hun steun vooral uit de grote steden aan de kust.", F),
            ("De nationalisten van Chiang Kai-shek vluchtten na hun nederlaag naar Taiwan.", J),
        ],
        "De communisten bouwden hun steun op bij de arme boeren op het platteland. Na de nederlaag trok Chiang Kai-shek zich terug op Taiwan.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin Mao de Volksrepubliek China uitriep.",
        "tijdlijn-china.svg",
        [[7.7, 25, 3.3, 55]],
        "Op 1 oktober 1949, op het Tienanmenplein in Peking.",
    ),
    sorteer(
        "Was het een oorzaak of een gevolg van de communistische machtsovername in China?",
        ["Oorzaak", "Gevolg"],
        [
            ["Bittere armoede bij de boeren, die vaak zwaar verschuldigd waren aan grootgrondbezitters", "Oorzaak"],
            ["Corruptie en verdeeldheid binnen het nationalistische bewind", "Oorzaak"],
            ["De verzwakking van het land door de Japanse bezetting", "Oorzaak"],
            ["Een eenpartijstaat waarin de communistische partij alle macht heeft", "Gevolg"],
            ["De Verenigde Staten weigeren het nieuwe bewind te erkennen", "Gevolg"],
        ],
        "Armoede, een zwak en corrupt bewind en de oorlog maakten de communisten populair. Daarna volgden de eenpartijstaat en een breuk met de Verenigde Staten, die tot 1979 duurde.",
    ),
    mk(
        "Waarom kreeg Mao meer steun bij de boeren dan de nationalisten?",
        [
            "Hij beloofde hun grond en leefde met zijn troepen tussen hen",
            "Hij liet de boeren in elk dorp vrij kiezen tussen meerdere partijen en kandidaten",
            "Hij kreeg veel geld van de Verenigde Staten om voedsel uit te delen",
            "Hij beloofde de oude keizer terug op de troon te zetten",
        ],
        0,
        "Grond voor wie hem bewerkt was een krachtige belofte in een land waar de meeste mensen boer waren.",
    ),
    # ------------------------------------------------ het beleid onder Mao
    sorteer(
        "Tot welk domein hoort deze maatregel onder Mao?",
        ["Politiek", "Sociaal", "Cultureel", "Economisch"],
        [
            ["Andere partijen verbieden en tegenstanders laten opsluiten", "Politiek"],
            ["Een huwelijkswet die gedwongen huwelijken verbiedt en vrouwen het recht op echtscheiding geeft", "Sociaal"],
            ["Oude tempels, boeken en tradities laten vernielen", "Cultureel"],
            ["Vijfjarenplannen naar Sovjetvoorbeeld met de nadruk op zware industrie", "Economisch"],
        ],
        "Telkens één voorbeeld per domein. De huwelijkswet van 1950 veranderde de positie van vrouwen in het gezin.",
    ),
    mk(
        "Een Chinese staatsaffiche uit 1958 toont lachende boeren bij bergen graan, met de leuze: Vooruit met de Grote Sprong! Wat was de bedoeling van de makers?",
        [
            "De bevolking overhalen om vol mee te doen",
            "Buitenlandse kopers zoeken voor de Chinese rijst en thee",
            "De boeren waarschuwen voor een hongersnood die eraan kwam",
            "Kritiek geven op de leiding van de communistische partij",
        ],
        0,
        "Het is propaganda van de staat. Ze toont wat de partij wil bereiken. Leg de oogstcijfers ernaast en je ziet hoe het in werkelijkheid ging.",
    ),
    klik(
        "Klik in de grafiek op het jaar met de laagste graanoogst.",
        "graanoogst-china.svg",
        [[55.0, 10, 12.5, 86]],
        "In 1960 lag de oogst bijna een kwart lager dan in 1958.",
    ),
    tabel(
        "Juist of fout? De gevolgen van de Grote Sprong Voorwaarts (1958-1962).",
        [
            ("Een hongersnood met miljoenen doden.", J),
            ("Mao moest het dagelijkse bestuur een tijd aan anderen overlaten.", J),
            ("China werd de grootste staalproducent ter wereld.", F),
            ("Het vertrouwen in de cijfers van de partij nam toe.", F),
        ],
        "De Grote Sprong werd een ramp. Veel van het staal uit die jaren was onbruikbaar, en de opgeblazen cijfers ondermijnden het vertrouwen.",
    ),
    open_(
        "Leg in je eigen woorden uit waarom de Grote Sprong Voorwaarts tot sociaaleconomische achteruitgang leidde. Gebruik minstens twee oorzaken.",
        "Bijvoorbeeld: de boeren moesten in kleine ovens staal maken, waardoor er minder mensen op het land werkten en de oogst daalde. Bovendien gaven lokale leiders uit angst te hoge oogstcijfers door, zodat de staat te veel graan ophaalde en zelfs uitvoerde. Gevolg: een enorme hongersnood met miljoenen doden en een economie die jaren achteruitging.",
    ),
    keuze(
        "Met de Culturele Revolutie vanaf [[*1966|1949|1978]] wilde Mao zijn macht [[*terugwinnen|delen|afstaan]]. Jongeren in de [[*Rode Garde|Guomindang|volkscommunes]] vielen leraren en partijleden aan.",
        "Na de mislukking van de Grote Sprong had Mao aan invloed verloren. De Culturele Revolutie gaf hem die macht terug.",
    ),
    met_prent("culturele-revolutie-affiche.webp", tabel(
        "Juist of fout? Wat leer je uit deze affiche uit de Culturele Revolutie?",
        [
            ("De affiche verheerlijkt de leider als een bijna onfeilbare figuur.", J),
            ("Ze richt zich vooral tot jongeren.", J),
            ("Ze is gemaakt door tegenstanders van de partij.", F),
            ("Ze geeft een betrouwbaar beeld van het dagelijkse leven in die jaren.", F),
        ],
        "Een staatsaffiche toont het ideaal van de partij. Over het echte leven, met vervolgingen en gesloten scholen, zegt ze weinig.",
    ), volgt=True),

    # ------------------------------------------------ Deng Xiaoping
    klik(
        "Klik op de tijdlijn op het jaar waarin Deng Xiaoping zijn economische hervormingen begon.",
        "tijdlijn-china.svg",
        [[39.4, 25, 3.3, 55]],
        "Mao stierf in 1976. Vanaf 1978 zette Deng het land op een nieuwe economische koers.",
    ),
    tabel(
        "Juist of fout? De modernisering onder Deng Xiaoping.",
        [
            ("Boeren mochten een deel van hun oogst zelf op de markt verkopen.", J),
            ("In speciale economische zones aan de kust mochten buitenlandse bedrijven investeren.", J),
            ("De communistische partij gaf haar machtsmonopolie op.", F),
            ("Gezinnen mochten in principe nog maar één kind krijgen.", J),
        ],
        "Economisch ging China open, politiek bleef de partij alleen aan de macht. De eenkindpolitiek moest de bevolkingsgroei afremmen.",
    ),
    mk(
        "Deng zei: het maakt niet uit of een kat zwart of wit is, zolang ze muizen vangt. Wat bedoelde hij?",
        [
            "Wat de economie doet groeien, is goed",
            "De Chinezen moeten beter letten op de netheid van hun straten en steden",
            "Alle buitenlanders zijn welkom, behalve westerlingen",
            "De partij moet terug naar het strenge beleid van de vorige jaren",
        ],
        0,
        "Het resultaat telt, niet de leer. Zo verantwoordde Deng marktwerking in een communistische staat.",
    ),
    sleep(
        "Deng noemde zijn koers socialisme met Chinese [[kenmerken]]: een [[markteconomie]] onder leiding van één partij. Het eerste proefgebied was de zone van [[Shenzhen]], vlak bij Hongkong.",
        ["planeconomie", "Sjanghai", "democratie"],
        "Economische vrijheid zonder politieke vrijheid. Shenzhen groeide van vissersdorp tot miljoenenstad.",
    ),
    # ------------------------------------------------ Tienanmen
    klik(
        "Klik op de tijdlijn op het jaar waarin het leger het studentenprotest op het Tienanmenplein neersloeg.",
        "tijdlijn-china.svg",
        [[51.4, 25, 3.3, 55]],
        "In de nacht van 3 op 4 juni 1989, hetzelfde jaar waarin in Europa de Muur viel.",
    ),
    casus(
        "Lente 1989. Weken lang bezetten studenten en arbeiders het Tienanmenplein in Peking. Ze eisen persvrijheid, inspraak en een einde aan corruptie. Op 4 juni rijden tanks het plein op. Honderden, misschien duizenden mensen komen om. In China zelf wordt er tot vandaag niet over gesproken.",
        [
            mk(
                "Wat toont deze gebeurtenis over de houding van de Chinese overheid tegenover democratie?",
                [
                    "Economisch mocht er veel, maar de macht van de partij bleef onaantastbaar",
                    "De overheid organiseerde na het protest snel vrije verkiezingen in het hele land",
                    "De overheid liet de studenten begaan, omdat ze dezelfde eisen had",
                    "Het protest werd opgelost met een volksraadpleging over de eisen van de studenten",
                ],
                0,
                "De partij duldt geen politieke tegenmacht. Het neerslaan van het protest en de censuur erna tonen dat.",
            ),
            mk(
                "Waarom is een Chinees schoolboek geen bruikbare bron om te weten wat er op 4 juni gebeurde?",
                [
                    "De staat controleert wat erin staat en zwijgt de gebeurtenis dood",
                    "Schoolboeken bevatten nooit informatie over geschiedenis",
                    "Het is te lang na de feiten geschreven",
                    "Chinese schoolboeken zijn enkel in het Engels te krijgen",
                ],
                0,
                "Censuur maakt een bron onbruikbaar voor deze vraag. Je zoekt dan ooggetuigen, buitenlandse journalisten of diplomatieke berichten.",
            ),
        ],
    ),
    # ------------------------------------------------ Xi Jinping
    koppel(
        "Bij welk domein hoort dit kenmerk van het beleid onder Xi Jinping (aan de macht sinds 2012)?",
        [
            ["Politiek", "De grens van twee ambtstermijnen voor de president wordt in 2018 afgeschaft"],
            ["Sociaal", "Camera's met gezichtsherkenning en een puntensysteem dat het gedrag van burgers volgt"],
            ["Cultureel", "Strenge censuur op internet en nadruk op de Chinese droom en trots op het land"],
            ["Economisch", "De Nieuwe Zijderoute: wegen, havens en spoorlijnen in tientallen landen"],
        ],
        ["Vrije verkiezingen met meerdere partijen"],
        "Vrije verkiezingen met meerdere partijen bestaan in China niet, ook niet onder Xi.",
    ),
    tabel(
        "Juist of fout? China onder Xi Jinping.",
        [
            ("Xi voerde een grote campagne tegen corruptie, waarbij ook rivalen verdwenen.", J),
            ("In Xinjiang worden Oeigoeren, een moslimminderheid, in grote kampen opgesloten.", J),
            ("In Hongkong kwam er sinds 2020 meer ruimte voor protest en oppositie.", F),
            ("Na de eenkindpolitiek mogen gezinnen nu officieel drie kinderen krijgen.", J),
        ],
        "In Hongkong kwam er in 2020 net een strenge veiligheidswet die protest en oppositie aan banden legt.",
    ),
    mk(
        "Je vergelijkt de staatsvorm onder Mao met die van vandaag. Wat is de belangrijkste continuïteit?",
        [
            "Er is nog altijd één partij die alle macht heeft",
            "De economie is nog altijd volledig in handen van de staat",
            "Er zijn nog altijd volkscommunes op het platteland",
            "Buitenlandse bedrijven zijn nog altijd verboden",
        ],
        0,
        "De economie veranderde grondig, het politieke systeem nauwelijks. Dat is het verschil tussen economische en politieke modernisering.",
    ),
    tabel(
        "Is het een verschil tussen China onder Mao en China vandaag?",
        [
            ("Privébedrijven en miljardairs", "Verschil"),
            ("De meerderheid van de bevolking woont in de stad", "Verschil"),
            ("Grote rol in de wereldhandel", "Verschil"),
            ("Grote staatsbedrijven in sectoren zoals energie en banken", "Gelijk gebleven"),
        ],
        "China is verstedelijkt en rijk geworden met privébedrijven, maar de staat houdt de sleutelsectoren nog stevig in handen.",
        kolommen=["Verschil", "Gelijk gebleven"],
    ),
    # ------------------------------------------------ China in Afrika
    sorteer(
        "Wat haalt China uit Afrika en wat brengt het mee?",
        ["Haalt China er", "Brengt China mee"],
        [
            ["Olie, koper en kobalt", "Haalt China er"],
            ["Een afzetmarkt voor goedkope Chinese producten", "Haalt China er"],
            ["Steun van Afrikaanse landen in de VN", "Haalt China er"],
            ["Wegen, spoorlijnen, havens en stadions", "Brengt China mee"],
            ["Grote leningen", "Brengt China mee"],
        ],
        "Het is een ruil: grondstoffen, markten en politieke steun tegen infrastructuur en geld.",
    ),
    mk(
        "Waarom kiezen Afrikaanse regeringen soms liever voor Chinese leningen dan voor westerse?",
        [
            "China stelt geen voorwaarden over mensenrechten of bestuur",
            "Chinese leningen hoeven nooit terugbetaald te worden",
            "China eist dat er eerst vrije verkiezingen komen",
            "Westerse landen geven helemaal geen leningen aan Afrika",
        ],
        0,
        "China zegt zich niet te bemoeien met binnenlandse zaken. Westerse geldschieters koppelen hulp vaker aan voorwaarden.",
    ),
    casus(
        "Een Afrikaanse krant schrijft: Dankzij China hebben we eindelijk een spoorlijn naar de haven. Een andere krant: Het land kan de Chinese lening niet terugbetalen en moet nu de haven voor jaren uitbesteden aan een Chinees bedrijf.",
        [
            keuze(
                "De eerste krant ziet China als een [[*partner|bezetter|kolonisator]]. De tweede waarschuwt voor een [[*schuldenval|handelsoorlog|burgeroorlog]].",
                "Dezelfde investering, twee perspectieven. Critici vergelijken het soms met een nieuwe vorm van afhankelijkheid.",
            ),
            mk(
                "Welke vergelijking maken critici vaak bij China in Afrika?",
                [
                    "Met het Europese imperialisme van de 19de eeuw",
                    "Met de Marshallhulp, een gift zonder enige eigen belangen van de gever",
                    "Met de Europese Unie: landen geven samen macht af",
                    "Met de dekolonisatie: Afrika wordt onafhankelijk van Europa",
                ],
                0,
                "Er zijn gelijkenissen, zoals grondstoffen en afhankelijkheid, maar ook verschillen: China bezet geen gebieden en bestuurt ze niet zelf.",
            ),
        ],
    ),
    # ------------------------------------------------ contacten met het Westen
    volgorde(
        "Zet de stappen in de toenadering tussen China en het Westen in de juiste volgorde.",
        [
            "De Amerikaanse president Nixon bezoekt Peking",
            "Deng opent speciale economische zones voor buitenlandse bedrijven",
            "Groot-Brittannië geeft Hongkong terug aan China",
            "China wordt lid van de Wereldhandelsorganisatie",
        ],
        "Nixon in 1972, de zones vanaf 1980, Hongkong in 1997 en de Wereldhandelsorganisatie in 2001.",
    ),
    tabel(
        "Is het een gevolg van de contacten tussen China en het Westen?",
        [
            ("Westerse ketens en merken in Chinese steden", J),
            ("Veel producten in onze winkels zijn in China gemaakt", J),
            ("Duizenden Chinese studenten aan Europese en Amerikaanse universiteiten", J),
            ("China neemt het westerse parlementaire systeem over", F),
        ],
        "De contacten veranderden de economie en het dagelijks leven, niet het politieke systeem.",
    ),
    mk(
        "Bij de teruggave van Hongkong aan China gold het principe één land, twee systemen. Wat hield dat in?",
        [
            "Hongkong hield vijftig jaar een eigen economie en rechtspraak",
            "Hongkong zou om de beurt door China en Groot-Brittannië bestuurd worden",
            "Hongkong kreeg twee hoofdsteden, een Chinese en een Britse",
            "In Hongkong mochten voortaan precies twee politieke partijen bestaan",
        ],
        0,
        "Dat was de belofte bij de overdracht. Critici vinden dat de vrijheden de laatste jaren sterk zijn ingeperkt.",
    ),
    open_(
        "Vergelijk de manier waarop Mao en Deng China wilden versterken. Geef één gelijkenis en één verschil.",
        "Gelijkenis: allebei wilden ze van China een sterk land maken onder leiding van de communistische partij, zonder politieke oppositie. Verschil: Mao rekende op massamobilisatie en een planeconomie, zoals bij de Grote Sprong Voorwaarts; Deng opende de economie voor de markt en buitenlandse investeerders.",
    ),
]
