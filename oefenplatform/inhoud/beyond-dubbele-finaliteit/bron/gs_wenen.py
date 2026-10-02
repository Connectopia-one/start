# -*- coding: utf-8 -*-
"""Restauratie en revolutie: het Congres van Wenen.

Uit de leerinhoud "restauratie en revolutie" van de vakfiche geschiedenis,
3 dubbele finaliteit: de doelstellingen, de beslissingen en de gevolgen van het
Congres van Wenen, en de vraag in welke mate die doelstellingen bereikt zijn.

Het congres is in dezelfde fiche ook het scharnierpunt tussen de vroegmoderne
en de moderne tijd, dus de vragen hier sluiten aan bij het thema over het
historisch referentiekader.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag="In welke stad kwamen de Europese grootmachten in 1814 en 1815 samen om de kaart van Europa te hertekenen?",
        antwoord=["Wenen", "wenen"],
        uitleg="Het congres begon in september 1814 en eindigde in juni 1815, kort voor de slag bij Waterloo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Na de nederlaag van welke heerser kwam het Congres van Wenen samen?",
        opties=[
            "Napoleon Bonaparte",
            "Lodewijk XIV van Frankrijk",
            "keizer Karel V",
            "Willem I der Nederlanden",
        ],
        antwoord=0,
        uitleg="Napoleon had bijna heel Europa veroverd. Na zijn val moesten de grenzen opnieuw vastgelegd worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke staatsman uit Oostenrijk leidde het Congres van Wenen?",
        opties=[
            "Metternich",
            "Talleyrand",
            "Bismarck",
            "Cavour",
        ],
        antwoord=0,
        uitleg="Talleyrand onderhandelde voor Frankrijk. Bismarck en Cavour kwamen pas een halve eeuw later.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het beginsel van legitimiteit op het Congres van Wenen?",
        opties=[
            "de vorstenhuizen van voor Napoleon krijgen hun troon terug",
            "elk volk mag zelf kiezen door wie het bestuurd wordt",
            "elke staat krijgt precies evenveel grondgebied toegewezen",
            "de grenzen worden langs de taalgrenzen getrokken",
        ],
        antwoord=0,
        uitleg="De oude dynastieën werden als de rechtmatige vorsten beschouwd. In Frankrijk kwamen de Bourbons dus terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het beginsel van machtsevenwicht?",
        opties=[
            "geen enkele staat mag zo sterk worden dat hij Europa overheerst",
            "elke staat moet precies even veel inwoners gaan tellen",
            "alle staten moeten op termijn even welvarend worden",
            "alle staten moeten dezelfde staatsvorm en grondwet krijgen",
        ],
        antwoord=0,
        uitleg="De ervaring met Napoleon lag nog vers: één te machtige staat bracht heel Europa in oorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke doelstellingen streefden de grootmachten in Wenen na?",
        opties=[
            "het herstel van de oude vorstenhuizen",
            "een evenwicht tussen de grootmachten",
            "de invoering van het algemeen stemrecht",
            "de oprichting van één Europese staat",
        ],
        antwoord=[0, 1],
        uitleg="Stemrecht en eenmaking waren juist de eisen van de liberalen en de nationalisten, die het congres wilde tegenhouden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nieuwe staat ontstond in Wenen als buffer tegen Frankrijk?",
        opties=[
            "het Verenigd Koninkrijk der Nederlanden",
            "het Duitse Keizerrijk onder Pruisen",
            "het koninkrijk Italië onder Piëmont",
            "de Zwitserse bondsstaat met kantons",
        ],
        antwoord=0,
        uitleg="De noordelijke en de zuidelijke Nederlanden werden samengevoegd onder Willem I, precies om Frankrijk in te sluiten.",
    ),
    dict(
        type="invultekst",
        vraag="Wie werd koning van het Verenigd Koninkrijk der Nederlanden?",
        antwoord=["Willem I", "willem I", "Willem de Eerste"],
        uitleg="Hij regeerde over het noorden en het zuiden samen, van 1815 tot de Belgische onafhankelijkheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kreeg Pruisen op het Congres van Wenen?",
        opties=[
            "gebieden langs de Rijn, met steenkool en ijzer",
            "het eiland Sicilië en het zuiden van Italië",
            "de Zuidelijke Nederlanden met Antwerpen",
            "het hele Poolse gebied tot aan Warschau",
        ],
        antwoord=0,
        uitleg="Die Rijnlandse gebieden maakten Pruisen later tot de industriële motor van Duitsland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kwam er in de plaats van het oude Heilige Roomse Rijk?",
        opties=[
            "een losse Duitse Bond van zelfstandige staten",
            "één Duits keizerrijk met Berlijn als hoofdstad",
            "een Duitse republiek met een parlement",
            "een deel van Frankrijk",
        ],
        antwoord=0,
        uitleg="De Duitse Bond was een samenwerkingsverband, geen staat. De Duitse eenmaking kwam pas in 1871.",
    ),
    dict(
        type="waarofniet",
        vraag="Op het Congres van Wenen beslisten de grootmachten over de grenzen zonder de bevolking te vragen wat zij wilde.",
        antwoord=True,
        uitleg="Volken werden samengevoegd of opgesplitst zoals het in het machtsevenwicht paste. Dat werd later een bron van conflict.",
    ),
    dict(
        type="waarofniet",
        vraag="Frankrijk mocht als verslagen land niet aan de onderhandelingen deelnemen.",
        antwoord=False,
        uitleg="Talleyrand onderhandelde wel degelijk mee en slaagde erin Frankrijk binnen zijn oude grenzen te houden.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Congres van Wenen voerde in heel Europa de democratie in.",
        antwoord=False,
        uitleg="Het tegendeel: de vorsten herstelden hun macht. Liberale en nationale eisen werden onderdrukt.",
    ),
    dict(
        type="waarofniet",
        vraag="Na het Congres van Wenen bleef Europa tientallen jaren zonder een grote oorlog tussen de grootmachten.",
        antwoord=True,
        uitleg="Het machtsevenwicht werkte in dat opzicht. Pas met de Krimoorlog in de jaren 1850 botsten de grootmachten weer.",
    ),
    dict(
        type="waarofniet",
        vraag="De beslissingen van Wenen hielden tot het einde van de negentiende eeuw ongewijzigd stand.",
        antwoord=False,
        uitleg="België scheurde zich in 1830 los, Italië en Duitsland werden later één. De kaart van Wenen hield niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het herstel van de toestand van voor de Franse Revolutie en Napoleon?",
        antwoord=["de restauratie", "restauratie"],
        uitleg="Letterlijk het herstel. Volledig lukte het niet: de ideeën van de revolutie bleven leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk bondgenootschap sloten de vorsten van Rusland, Oostenrijk en Pruisen in 1815 om de orde te bewaken?",
        opties=[
            "de Heilige Alliantie",
            "de Volkenbond",
            "de Noord-Atlantische Verdragsorganisatie",
            "het Warschaupact",
        ],
        antwoord=0,
        uitleg="De Volkenbond kwam na de Eerste Wereldoorlog, de NAVO en het Warschaupact pas in de Koude Oorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hielden de grootmachten na 1815 regelmatig congressen?",
        opties=[
            "om samen op te treden tegen opstanden en revoluties",
            "om de wereldhandel onder de grootmachten te verdelen",
            "om een Europees parlement te laten verkiezen",
            "om de kolonies in Afrika onderling te verdelen",
        ],
        antwoord=0,
        uitleg="Dat overleg wordt het congressysteem genoemd. Afrika werd pas veel later verdeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk gevolg van het Congres van Wenen hoort bij het politieke domein?",
        opties=[
            "de vorsten kregen hun absolute macht grotendeels terug",
            "de stoommachine werd in alle fabrieken ingevoerd",
            "de bevolking van Europa verdubbelde in enkele jaren",
            "de romantiek werd de heersende kunststroming",
        ],
        antwoord=0,
        uitleg="De stoommachine en de romantiek horen bij het economische en het culturele domein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet beoordelen in welke mate de doelstellingen van Wenen bereikt zijn. Welk besluit is het meest verdedigbaar?",
        opties=[
            "het machtsevenwicht hield een tijd, het herstel van de oude orde niet",
            "alle doelstellingen van het congres werden volledig bereikt",
            "geen van de doelstellingen van het congres werd gehaald",
            "de doelstellingen zijn nergens opgeschreven, dus niet te beoordelen",
        ],
        antwoord=0,
        uitleg="Een grote oorlog bleef decennia uit, maar liberalisme en nationalisme lieten zich niet wegdrukken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In welke periode situeer je het Congres van Wenen?",
        opties=[
            "aan het begin van de moderne tijd",
            "aan het einde van de middeleeuwen",
            "midden in de hedendaagse tijd",
            "in de klassieke oudheid",
        ],
        antwoord=0,
        uitleg="Het congres wordt vaak als scharnierpunt tussen de vroegmoderne en de moderne tijd genomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke grootmachten gaven in Wenen de toon aan?",
        opties=[
            "Oostenrijk, Pruisen, Rusland en Groot-Brittannië",
            "Spanje, Portugal, Zweden, Denemarken en Noorwegen",
            "de Verenigde Staten, Japan, China en Brazilië",
            "Italië, Duitsland, België en Nederland samen",
        ],
        antwoord=0,
        uitleg="Italië, Duitsland en België bestonden als staat nog niet. De Verenigde Staten speelden in Europa geen rol.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het beginsel van compensatie op het congres?",
        opties=[
            "een staat die gebied afstaat, krijgt er elders iets voor terug",
            "de verliezers betalen een hoge boete aan de overwinnaars",
            "elke verdreven vorst krijgt een vergoeding voor zijn ballingschap",
            "de bevolking krijgt van de staat een vergoeding voor de oorlogsschade",
        ],
        antwoord=0,
        uitleg="Zo bleef het evenwicht tussen de grootmachten bewaard terwijl de kaart hertekend werd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebieden kwamen in Wenen onder Oostenrijks bestuur?",
        opties=[
            "Lombardije en Venetië in Noord-Italië",
            "de Rijnlandse gebieden in het westen van Duitsland",
            "Finland en de Baltische kust",
            "de Zuidelijke Nederlanden",
        ],
        antwoord=0,
        uitleg="Het Rijnland ging naar Pruisen, de Zuidelijke Nederlanden naar Willem I.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de Duitse Bond kloppen?",
        opties=[
            "de aangesloten staten bleven zelfstandig",
            "Oostenrijk had er een leidende rol in",
            "er kwam één Duitse keizer aan het hoofd",
            "de Bond voerde één munt en één leger in",
        ],
        antwoord=[0, 1],
        uitleg="Eén keizer, één munt en één leger kwamen er pas met het Duitse Keizerrijk in 1871.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het Verenigd Koninkrijk der Nederlanden kloppen?",
        opties=[
            "het verenigde de noordelijke en de zuidelijke Nederlanden",
            "het moest Frankrijk in het noorden insluiten",
            "het werd een republiek zonder vorst",
            "het bleef bestaan tot de Eerste Wereldoorlog",
        ],
        antwoord=[0, 1],
        uitleg="Willem I was koning, dus geen republiek, en het koninkrijk viel in 1830 al uiteen.",
    ),
    dict(
        type="waarofniet",
        vraag="Zwitserland werd op het Congres van Wenen als neutrale staat erkend.",
        antwoord=True,
        uitleg="Die neutraliteit paste in het machtsevenwicht: geen grootmacht mocht de Alpenpassen beheersen.",
    ),
    dict(
        type="waarofniet",
        vraag="In Frankrijk werd na Napoleon een republiek zonder koning opgericht.",
        antwoord=False,
        uitleg="Er kwam opnieuw een koning uit het huis Bourbon. Dat is het beginsel van legitimiteit in de praktijk: de dynastie van voor de revolutie kwam terug.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Congres van Wenen hield rekening met de taal en de cultuur van de bevolking bij het tekenen van de grenzen.",
        antwoord=False,
        uitleg="Het machtsevenwicht ging voor. Juist daardoor groeide het nationalisme als protest tegen die grenzen.",
    ),
    dict(
        type="waarofniet",
        vraag="De ideeën van de Franse Revolutie verdwenen na het Congres van Wenen volledig uit Europa.",
        antwoord=False,
        uitleg="Ze leefden ondergronds voort bij liberalen en nationalisten en kwamen in 1830 en 1848 weer boven.",
    ),
    dict(
        type="waarofniet",
        vraag="Het congressysteem na 1815 was bedoeld om revoluties in de kiem te smoren.",
        antwoord=True,
        uitleg="De vorsten spraken af om elkaar te steunen zodra er ergens een opstand uitbrak.",
    ),
    dict(
        type="waarofniet",
        vraag="De Belgische revolutie van 1830 bewijst dat de beslissingen van Wenen niet overal gedragen werden.",
        antwoord=True,
        uitleg="De samenvoeging met het noorden was een beslissing van buitenaf, en het zuiden maakte er na vijftien jaar een einde aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het streven dat geen enkele staat in Europa te machtig mag worden?",
        antwoord=["het machtsevenwicht", "machtsevenwicht", "evenwicht"],
        uitleg="Samen met legitimiteit, compensatie en solidariteit tussen de vorsten is dat een doelstelling van Wenen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het samenwerkingsverband van Duitse staten dat in 1815 ontstond?",
        antwoord=["de Duitse Bond", "Duitse Bond"],
        uitleg="Het kwam in de plaats van het Heilige Roomse Rijk en liet de staten hun zelfstandigheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bron uit 1820 noemt de Heilige Alliantie een verbond tegen de volkeren. Wat is daar een argument voor?",
        opties=[
            "het verbond trad op tegen opstanden voor meer vrijheid",
            "het verbond verdeelde de kolonies onder de leden ervan",
            "het verbond voerde overal het algemeen stemrecht in",
            "het verbond richtte een parlement voor heel Europa op",
        ],
        antwoord=0,
        uitleg="De vorsten beloofden elkaar steun bij binnenlandse onrust, en dat betekende in de praktijk tegen liberale eisen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men het Congres van Wenen een scharnierpunt?",
        opties=[
            "het sluit een tijdperk af en opent een nieuw",
            "het duurde langer dan elk ander congres",
            "er waren meer deelnemers dan ooit",
            "het vond plaats in een hoofdstad",
        ],
        antwoord=0,
        uitleg="Een scharnierpunt is een gebeurtenis die de overgang tussen twee historische periodes markeert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beperking heeft het als je 1815 als begin van de moderne tijd neemt?",
        opties=[
            "het is een politieke en westerse keuze, die elders weinig betekent",
            "er bestaan over dat jaar geen enkele betrouwbare bron of getuigenis",
            "er gebeurde in dat jaar helemaal niets van belang in Europa",
            "het jaartal werd pas na de Tweede Wereldoorlog bedacht",
        ],
        antwoord=0,
        uitleg="Economisch lag het keerpunt bij de industriële revolutie, en voor China of Afrika zegt 1815 niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen van het Congres van Wenen werkten op langere termijn tegen het congres zelf?",
        opties=[
            "het nationalisme bij volken die over staten verdeeld waren",
            "het liberalisme bij burgers die grondrechten eisten",
            "de uitbreiding van de kolonies in Afrika en Azië",
            "de oprichting van de Verenigde Naties in New York",
        ],
        antwoord=[0, 1],
        uitleg="De wedloop om Afrika kwam pas later, en de Verenigde Naties pas na de Tweede Wereldoorlog.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een kaart van Europa in 1815 en een kaart in 1914. Welk verschil valt het meest op?",
        opties=[
            "Duitsland en Italië zijn één staat geworden",
            "Frankrijk is van de kaart van Europa verdwenen",
            "Rusland is veel kleiner geworden dan in 1815",
            "er zijn tussen de staten geen grenzen meer te zien",
        ],
        antwoord=0,
        uitleg="Precies wat Wenen wilde vermijden, gebeurde: in het midden van Europa ontstond een sterke Duitse staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zou je het Congres van Wenen in de maatschappelijke domeinen situeren?",
        opties=[
            "vooral politiek, met gevolgen in het sociale en culturele domein",
            "uitsluitend economisch, want het ging over handel en grondstoffen",
            "uitsluitend cultureel, want het ging over kunst en wereldbeelden",
            "in geen enkel domein, want het was maar een vergadering",
        ],
        antwoord=0,
        uitleg="Grenzen en vorstenhuizen zijn politiek, maar de onvrede erover voedde sociale bewegingen en nationale kunst.",
    ),
]
