# -*- coding: utf-8 -*-
"""China: van keizerrijk tot wereldmacht.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd, met China als
casus buiten Europa: het keizerrijk onder westerse druk, de republiek, de
Volksrepubliek van Mao, en de weg naar de economische wereldmacht van vandaag.

Deel 1 loopt van de Opiumoorlogen tot 1949. Deel 2 gaat over de Volksrepubliek
en over het China van na 1978.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarover gingen de Opiumoorlogen in de negentiende eeuw?",
        opties=[
            "Groot-Brittannië dwong China zijn markt voor handel te openen",
            "China viel Groot-Brittannië aan om zijn kolonies af te nemen",
            "China en Japan vochten over het bezit van Korea",
            "Groot-Brittannië en Frankrijk vochten over Hongkong",
        ],
        antwoord=0,
        uitleg="Het ging om vrije handel, opium incluis. China verloor en moest havens en voorrechten afstaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de ongelijke verdragen die China in de negentiende eeuw moest ondertekenen?",
        opties=[
            "verdragen die westerse mogendheden voorrechten in China gaven",
            "verdragen waarin China aan Europa grondstoffen moest leveren",
            "verdragen waarin China en Europa gelijk behandeld werden",
            "verdragen die China het recht gaven havens in Europa te openen",
        ],
        antwoord=0,
        uitleg="Westerse burgers vielen in China niet onder de Chinese rechtspraak. Dat werd als vernedering ervaren.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stad moest China in 1842 aan Groot-Brittannië afstaan?",
        antwoord=["Hongkong", "Hong Kong"],
        uitleg="Ze bleef Brits tot 1997. Toen werd ze weer een deel van China, met een eigen statuut.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat waren de invloedssferen in China rond 1900?",
        opties=[
            "gebieden waarin één mogendheid de handel beheerste",
            "gebieden die door China aan Japan werden verkocht",
            "gebieden die door de Volkenbond bestuurd werden",
            "gebieden waarin de keizer geen belasting hoefde te heffen",
        ],
        antwoord=0,
        uitleg="Handel, mijnen en spoorwegen lagen er in één hand. China bleef op papier één rijk, maar werd zo in stukken verdeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waartegen kwamen de boxers in 1900 in opstand?",
        opties=[
            "tegen de westerse invloed in China",
            "tegen de keizerin en haar hof in Peking",
            "tegen de communistische partij van China",
            "tegen de Japanse bezetting van Mantsjoerije",
        ],
        antwoord=0,
        uitleg="Een internationaal leger sloeg de opstand neer. China moest daarna nog zwaardere voorwaarden slikken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1911 en 1912 in China?",
        opties=[
            "het keizerrijk viel en er kwam een republiek",
            "de communisten namen de macht in het land over",
            "Japan veroverde het hele Chinese grondgebied",
            "de keizer voerde een grondwet met stemrecht in",
        ],
        antwoord=0,
        uitleg="Na meer dan tweeduizend jaar keizers werd China een republiek. Het bleef er jarenlang onrustig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie wordt beschouwd als de stichter van de Chinese republiek?",
        opties=[
            "Sun Yat-sen",
            "Mao Zedong",
            "Chiang Kai-shek",
            "Deng Xiaoping",
        ],
        antwoord=0,
        uitleg="Hij stichtte ook de nationalistische partij, de Guomindang. Hij stierf lang voor 1949.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee partijen stonden in China tussen 1927 en 1949 tegenover elkaar?",
        opties=[
            "de nationalisten van de Guomindang",
            "de communisten onder leiding van Mao",
            "de aanhangers van de laatste keizer",
            "de bezettingstroepen van de Volkenbond",
        ],
        antwoord=[0, 1],
        uitleg="Zij vochten een burgeroorlog uit, met een gedwongen pauze toen Japan het land binnenviel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de Lange Mars van 1934 en 1935?",
        opties=[
            "de communisten trokken duizenden kilometers te voet",
            "de nationalisten trokken met hun leger naar het noorden van China",
            "de Japanners trokken met hun leger door het hele land",
            "de boeren trokken massaal van het platteland naar de steden",
        ],
        antwoord=0,
        uitleg="Zij vluchtten weg uit hun belegerde gebied. De meesten haalden het einde niet; Mao werd er de leider van de partij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed Japan in 1931 en in 1937 in China?",
        opties=[
            "het bezette Mantsjoerije en daarna China zelf",
            "het sloot met China een verdrag over vrije handel",
            "het steunde de communisten in hun burgeroorlog",
            "het gaf zijn invloedssfeer in China vrijwillig op",
        ],
        antwoord=0,
        uitleg="De oorlog tussen China en Japan begon dus voor de oorlog in Europa, en kostte miljoenen Chinezen het leven.",
    ),
    dict(
        type="invultekst",
        vraag="Wie riep op 1 oktober 1949 de Volksrepubliek China uit?",
        antwoord=["Mao Zedong", "Mao"],
        uitleg="De nationalisten weken naar Taiwan uit. Daar bleef hun republiek apart bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar weken de Chinese nationalisten in 1949 naartoe uit?",
        opties=[
            "naar het eiland Taiwan",
            "naar het eiland Hongkong",
            "naar Japan",
            "naar de Sovjet-Unie",
        ],
        antwoord=0,
        uitleg="Tot vandaag bepaalt de vraag of Taiwan een deel van China is de verhoudingen in die hele regio.",
    ),
    dict(
        type="waarofniet",
        vraag="China werd in de negentiende eeuw volledig een kolonie van één Europese mogendheid.",
        antwoord=False,
        uitleg="Het bleef formeel zelfstandig, maar werd door verdragen en invloedssferen in stukken verdeeld.",
    ),
    dict(
        type="waarofniet",
        vraag="De ongelijke verdragen hebben in China een gevoel van vernedering nagelaten.",
        antwoord=True,
        uitleg="Men spreekt er van de eeuw van de vernedering. Dat gevoel speelt in de Chinese politiek nog mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Chinese keizerrijk bestond nog tot na de Tweede Wereldoorlog.",
        antwoord=False,
        uitleg="Het viel al in 1912. Daarna volgden een republiek, warlords, een burgeroorlog en een bezetting.",
    ),
    dict(
        type="waarofniet",
        vraag="De communisten in China steunden vooral op de boeren op het platteland.",
        antwoord=True,
        uitleg="Daarin verschilden zij van Marx, die zijn hoop op de arbeiders in de fabrieken had gevestigd.",
    ),
    dict(
        type="waarofniet",
        vraag="De oorlog tussen China en Japan begon pas na de Duitse inval in Polen.",
        antwoord=False,
        uitleg="Die oorlog was al in 1937 begonnen, en Mantsjoerije was zelfs in 1931 al bezet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over China in de negentiende eeuw kloppen?",
        opties=[
            "het moest havens en voorrechten aan westerse mogendheden afstaan",
            "het verloor oorlogen tegen technisch sterkere legers",
            "het bleef volledig buiten de wereldhandel staan",
            "het bezette zelf gebieden in Europa en in Afrika",
        ],
        antwoord=[0, 1],
        uitleg="Die ervaring verklaart waarom China vandaag zo nadrukkelijk op zijn soevereiniteit staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen het imperialisme en de geschiedenis van China?",
        opties=[
            "China kreeg het imperialisme in de vorm van verdragen",
            "China werd volledig door Europa gekoloniseerd zoals Congo",
            "China bleef van het imperialisme helemaal gespaard",
            "China voerde zelf een imperialisme in Europa door",
        ],
        antwoord=0,
        uitleg="Dat heet soms informeel imperialisme: niet besturen, maar beheersen langs handel en verdragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet een spotprent uit 1900 waarin mogendheden een cake met de naam China verdelen. Wat zegt die bron?",
        opties=[
            "dat tijdgenoten China als te verdelen gebied beschouwden",
            "dat China toen een bondgenoot van Europa was geworden",
            "dat China in 1900 de sterkste mogendheid ter wereld was",
            "dat de mogendheden China met rust wilden laten",
        ],
        antwoord=0,
        uitleg="Een spotprent is een bron over hoe men dacht. Dat beeld van een verdeelbare cake zegt genoeg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoe werd de economie van China onder Mao ingericht?",
        opties=[
            "de staat plande de productie en nam de grond in bezit",
            "de markt bepaalde de prijzen en de productie volledig",
            "de boeren bleven eigenaar van hun grond en hun vee",
            "buitenlandse bedrijven mochten vrij in China beleggen",
        ],
        antwoord=0,
        uitleg="Net als in de Sovjet-Unie: collectivisering van de landbouw en vijfjarenplannen voor de industrie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was de Grote Sprong Voorwaarts van 1958?",
        opties=[
            "een plan om China in enkele jaren te industrialiseren",
            "een plan om de scholen en universiteiten uit te breiden",
            "een plan om China voor buitenlandse handel te openen",
            "een plan om het leger van China te moderniseren",
        ],
        antwoord=0,
        uitleg="Het liep uit op een van de zwaarste hongersnoden van de eeuw, met tientallen miljoenen doden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het gevolg van de Grote Sprong Voorwaarts?",
        opties=[
            "een hongersnood die tientallen miljoenen mensen het leven kostte",
            "een snelle stijging van de welvaart op het Chinese platteland",
            "een vrije markt met veel buitenlandse bedrijven in China",
            "het einde van de communistische partij in China",
        ],
        antwoord=0,
        uitleg="Onhaalbare streefcijfers en opgeklopte oogstverslagen deden de voorraden verdwijnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er tijdens de Culturele Revolutie vanaf 1966?",
        opties=[
            "jongeren vielen leraren en ambtenaren aan",
            "China voerde het algemeen stemrecht voor alle burgers in",
            "China opende zijn economie voor buitenlandse bedrijven",
            "de communistische partij verloor de macht in het land",
        ],
        antwoord=0,
        uitleg="Scholen en universiteiten vielen stil en miljoenen mensen werden vernederd of verbannen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemde men de jongeren die tijdens de Culturele Revolutie de oude orde aanvielen?",
        antwoord=["Rode Gardisten", "de Rode Gardisten", "rode gardisten"],
        uitleg="Zij droegen het rode boekje van Mao en traden hard op tegen wie zij burgerlijk vonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie zette na de dood van Mao de economische hervormingen in?",
        opties=[
            "Deng Xiaoping",
            "Sun Yat-sen",
            "Chiang Kai-shek",
            "Jozef Stalin",
        ],
        antwoord=0,
        uitleg="Hij liet markt en privé-initiatief toe, maar hield het politieke monopolie van de partij overeind.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kenmerkt het Chinese model na 1978?",
        opties=[
            "een markteconomie onder leiding van één partij",
            "een vrije markt met vrije verkiezingen erbij",
            "een geplande economie zoals onder Mao",
            "een economie zonder enige buitenlandse handel",
        ],
        antwoord=0,
        uitleg="Men noemt dat socialisme met Chinese kenmerken. Economische vrijheid ging er niet samen met politieke.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de speciale economische zones in China?",
        opties=[
            "streken met gunstige regels voor buitenlandse bedrijven",
            "streken waar enkel staatsbedrijven mochten blijven werken",
            "streken waar geen enkele fabriek mocht worden gebouwd",
            "streken waar de boeren hun eigen grond terugkregen",
        ],
        antwoord=0,
        uitleg="Shenzhen groeide zo van een vissersstreek tot een stad met miljoenen inwoners.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in juni 1989 op het Tiananmenplein in Peking?",
        opties=[
            "een betoging voor meer vrijheid werd met geweld beëindigd",
            "de communistische partij werd er afgezet door het leger",
            "de economische hervormingen werden er afgekondigd",
            "Hongkong werd er weer bij China gevoegd",
        ],
        antwoord=0,
        uitleg="Het leger trad op tegen studenten en burgers. Over die dagen mag in China niet vrij gesproken worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurde er in 1997 met Hongkong?",
        opties=[
            "het werd opnieuw een deel van China",
            "het werd een onafhankelijke staat",
            "het werd aan Groot-Brittannië verkocht",
            "het werd door Japan ingenomen",
        ],
        antwoord=0,
        uitleg="Het kreeg een eigen statuut. In de jaren daarna is de greep van Peking er sterk toegenomen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemde men de Chinese regel dat een gezin maar één kind mocht hebben?",
        antwoord=["de eenkindpolitiek", "eenkindpolitiek", "eenkindpolitiek van China"],
        uitleg="Ze gold van 1979 tot 2015. Nu kampt China juist met een bevolking die snel verouderd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke plaats heeft China vandaag in de wereldeconomie?",
        opties=[
            "het is een van de grootste economieën ter wereld",
            "het staat buiten de wereldhandel en voert niets uit",
            "het is uitsluitend een landbouwland zonder industrie",
            "het is volledig afhankelijk van hulp uit het westen",
        ],
        antwoord=0,
        uitleg="Van werkplaats van de wereld is het opgeschoven naar eigen techniek, eigen merken en eigen investeringen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de Nieuwe Zijderoute van China?",
        opties=[
            "een plan met havens, spoorlijnen en wegen",
            "een handelsverdrag tussen China en de Verenigde Staten",
            "een spoorlijn tussen Peking en Hongkong",
            "een plan om de Chinese landbouw te hervormen",
        ],
        antwoord=0,
        uitleg="Naar Azië, Afrika en Europa. China legt mee aan en leent het geld, en zo groeit ook zijn politieke invloed.",
    ),
    dict(
        type="waarofniet",
        vraag="Onder Mao was de Chinese economie door de staat gepland.",
        antwoord=True,
        uitleg="De staat bezat de grond en de bedrijven en bepaalde wat er geproduceerd werd.",
    ),
    dict(
        type="waarofniet",
        vraag="De Grote Sprong Voorwaarts heeft China snel welvarend gemaakt.",
        antwoord=False,
        uitleg="Ze leidde tot een hongersnood. De welvaart kwam pas met de hervormingen na 1978.",
    ),
    dict(
        type="waarofniet",
        vraag="Na 1978 liet China buitenlandse bedrijven toe in bepaalde zones.",
        antwoord=True,
        uitleg="Daar begon de groei die China tot een van de grootste economieën ter wereld heeft gemaakt.",
    ),
    dict(
        type="waarofniet",
        vraag="De economische hervormingen van China gingen samen met vrije verkiezingen.",
        antwoord=False,
        uitleg="De partij hield de politieke macht volledig in handen. 1989 maakte dat onmiskenbaar duidelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="China is vandaag een van de grootste uitstoters van broeikasgassen ter wereld.",
        antwoord=True,
        uitleg="Door zijn omvang en zijn industrie. Per inwoner ligt de uitstoot wel lager dan in sommige rijke landen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over China na 1949 kloppen?",
        opties=[
            "onder Mao was de economie door de staat gepland",
            "na 1978 kwamen er markt en buitenlandse bedrijven bij",
            "de communistische partij verloor na 1978 haar machtspositie",
            "China bleef tot vandaag buiten de wereldhandel",
        ],
        antwoord=[0, 1],
        uitleg="Economische koerswijziging zonder politieke koerswijziging: dat is het kenmerk van dit land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt China onder Mao met de Sovjet-Unie onder Stalin. Welke gelijkenis valt op?",
        opties=[
            "één partij, een geplande economie en terreur tegen tegenstanders",
            "vrije verkiezingen met verschillende partijen in beide landen",
            "een economie die volledig aan de vrije markt werd overgelaten",
            "een bestuur dat de macht met een parlement moest delen",
        ],
        antwoord=0,
        uitleg="Zulke vergelijkingen horen bij dit vak: je zet kenmerken van twee samenlevingen naast elkaar.",
    ),
]
