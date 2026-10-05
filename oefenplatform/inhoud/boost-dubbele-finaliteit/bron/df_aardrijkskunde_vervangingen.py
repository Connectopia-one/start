# -*- coding: utf-8 -*-
"""De vragen die voor 🚀 Boost dubbele finaliteit anders moeten dan bij
doorstroom, voor aardrijkskunde.

De sleutel is de vraagtekst van de doorstroomvraag, de waarde is de vraag die
in de plaats komt. `bouw_aardrijkskunde.py` hiernaast wisselt ze om en stopt
als een sleutel niet meer bestaat.

Beide fiches van 2027 hebben dezelfde acht rubrieken met dezelfde gewichten:
situeren 10 %, bevolking 20 %, stad en platteland 10 %, economische processen
20 %, mondialisering 10 %, duurzaamheid 10 %, het versterkte broeikaseffect
10 % en geografisch onderzoek 10 %. De tien thema's blijven dus dezelfde. Wat
verschilt, is hoe diep elke rubriek gaat. Deze fiche laat weg:

  * **Bevolking.** De Human Development Index staat er niet in: wel de
    ontwikkelingsgraad als begrip, niet de index die ze meet. Het
    vruchtbaarheidscijfer en het migratiesaldo staan niet bij de kengetallen,
    en het demografisch transitiemodel met zijn fasen staat er helemaal niet
    in. De bevolkingsstructuur van een land vergelijken valt weg; de
    bevolkingsevolutie uit een leeftijdshistogram lezen blijft.
  * **Stad en platteland.** De hiërarchie van steden met haar criteria staat
    er niet in, en ook inbreiding en stadslandbouw niet.
  * **Economie en mondialisering.** Protectionisme, outsourcing en de
    reconversie van een oud industrieterrein staan er niet in.
  * **Duurzaamheid en landbouw.** Bodemerosie en bodemdegradatie staan niet
    in het lijstje gevolgen; ontbossing en schaalvergroting wel.
  * **Het broeikaseffect.** De stralingsbalans en het albedo staan er niet in,
    de koolstofcyclus en de vier sferen wel. Bij de gevolgen valt de
    verspreiding van tropische ziektes weg.

In de plaats komt wat deze fiche wél zet: de scholingsgraad als
sociaaleconomische factor, de bevolkingsdichtheid uit bronnen lezen, de
beïnvloedende factoren (klimaat en klimaatverandering, reliëf, bodemkwaliteit,
de politieke en de oorlogssituatie, welvaart en welzijn, armoede), de
koolstofcyclus tussen de vier sferen, en de SDG's naast de vijf P's.

Elke vervanging houdt hetzelfde type: een waar-of-niet-waar-vraag blijft waar
of blijft niet waar, en een meerkeuzevraag met meerdere juiste antwoorden
houdt er meerdere. Zo blijft het evenwicht per hoofdstuk kloppen.
"""

VERVANGINGEN = {}

# ───────────────────────── Waar wonen de mensen? Geen index voor ontwikkeling,
# wel de bevolkingsdichtheid uit bronnen en de factoren die ze beïnvloeden.
VERVANGINGEN.update(
    {
        "Je krijgt een tabel met per land het aantal inwoners en de oppervlakte. Wat kan je daaruit zelf berekenen?": dict(
            type="meerkeuze",
            vraag="Je krijgt een tabel met per land het aantal inwoners en de oppervlakte. Wat kan je daaruit zelf berekenen?",
            opties=[
                "De bevolkingsdichtheid van elk land",
                "Het geboortecijfer van elk van die landen",
                "De gemiddelde welvaart van elk van die landen",
                "Het aantal mensen dat er jaarlijks wegtrekt",
            ],
            antwoord=0,
            uitleg="Inwoners gedeeld door oppervlakte geeft de dichtheid. Voor een geboortecijfer, de welvaart of het vertrek van mensen heb je heel andere gegevens nodig.",
        ),
        "Waarvoor staat de afkorting HDI?": dict(
            type="meerkeuze",
            vraag="Wat lees je af van een thematische kaart van de bevolkingsdichtheid?",
            opties=[
                "Hoeveel mensen er per vierkante kilometer wonen",
                "Hoeveel mensen er in totaal in het land wonen",
                "Hoe snel de bevolking van het land groeit",
                "Waar de grenzen van de klimaatzones liggen",
            ],
            antwoord=0,
            uitleg="De legende koppelt elke kleur aan een aantal inwoners per vierkante kilometer. Het totale aantal inwoners van een land staat er niet op; daarvoor heb je een tabel nodig.",
        ),
        "Welke zaken zitten samen in de HDI verwerkt? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="In welke bronnen vind je de bevolkingsdichtheid van een streek terug? Kruis alles aan wat juist is.",
            opties=[
                "een thematische kaart met een legende",
                "een tabel met inwoners en oppervlakte",
                "een satellietbeeld van de aarde bij nacht",
                "een klimatogram van het weerstation",
                "een determineertabel van gesteenten",
            ],
            antwoord=[0, 1, 2],
            uitleg="Een kaart geeft ze rechtstreeks, een tabel laat ze berekenen, en lichtvlekken op een nachtbeeld verraden waar veel mensen wonen. Een klimatogram en een determineertabel gaan over heel andere dingen.",
        ),
        "De HDI van een land is een getal tussen 0 en 1.": dict(
            type="waarofniet",
            vraag="Twee kaarten van dezelfde bevolkingsdichtheid kunnen er heel anders uitzien als hun legende andere klassen gebruikt.",
            antwoord=True,
            uitleg="Wie de grenzen tussen de klassen verschuift, verschuift ook de kleurvlekken. Daarom lees je altijd eerst de legende voor je besluit wat een kaart zegt.",
        ),
        "Waarom is de HDI een betere maat voor ontwikkeling dan alleen het inkomen per inwoner?": dict(
            type="meerkeuze",
            vraag="Waarom zet men de dichtheid in klassen op een kaart, in plaats van bij elk gebied het exacte getal te schrijven?",
            opties=[
                "Zo zie je het patroon in één oogopslag",
                "Zo worden de cijfers zelf nauwkeuriger",
                "Zo hoeft de kaart geen legende te hebben",
                "Zo passen er meer landen op de kaart",
            ],
            antwoord=0,
            uitleg="Klassen en kleuren maken van een lijst getallen een beeld, en dan springt de verspreiding in het oog. Nauwkeuriger worden de cijfers er juist niet van.",
        ),
        "Land A heeft een HDI van 0,92, land B een HDI van 0,48. Wat mag je daaruit besluiten?": dict(
            type="meerkeuze",
            vraag="Op een satellietbeeld van de aarde bij nacht liggen de lichtvlekken niet gelijk verspreid. Wat leid je daaruit af?",
            opties=[
                "Daar wonen veel mensen met elektriciteit",
                "Daar is de bodem het meest vruchtbaar",
                "Daar valt de meeste neerslag per jaar",
                "Daar liggen de hoogste bergen van de aarde",
            ],
            antwoord=0,
            uitleg="Licht komt van steden, wegen en havens. Het beeld verraadt dus waar mensen samenwonen, al zie je er niets van hoe vruchtbaar of hoe nat een streek is.",
        ),
        "Twee landen met dezelfde HDI hebben daarom ook precies dezelfde levensverwachting.": dict(
            type="waarofniet",
            vraag="Op een kaart van de bevolkingsdichtheid kan je ook aflezen hoeveel inwoners er jaarlijks bijkomen.",
            antwoord=False,
            uitleg="Zo'n kaart geeft één moment weer. Voor de groei heb je twee tijdstippen nodig, of de kengetallen van de bevolking.",
        ),
        "Welke omstandigheden kunnen de HDI van een land doen dalen? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke omstandigheden doen mensen uit een streek wegtrekken? Kruis alles aan wat juist is.",
            opties=[
                "een oorlog die jaren aansleept",
                "droogte waardoor de oogst mislukt",
                "armoede zonder uitzicht op werk",
                "de ligging dicht bij de nulmeridiaan",
                "de tijdzone waarin de streek valt",
            ],
            antwoord=[0, 1, 2],
            uitleg="Oorlog, droogte en armoede zijn pushfactoren: ze duwen mensen weg. Waar een streek op het gradennet ligt, verandert niets aan hoe het er leeft.",
        ),
        "Welke organisatie berekent en publiceert elk jaar de Human Development Index?": dict(
            type="invultekst",
            vraag="Hoe noem je de kwaliteit van de grond, die bepaalt hoeveel voedsel er in een streek kan groeien?",
            antwoord=["bodemkwaliteit", "de bodemkwaliteit"],
            uitleg="De bodemkwaliteit is een van de drie natuurlijke factoren achter de bevolkingsdichtheid, naast het klimaat en het reliëf.",
        ),
        "Binnen één land kan de ontwikkelingsgraad sterk verschillen tussen streken.": dict(
            type="waarofniet",
            vraag="Een oorlog kan de bevolkingsdichtheid van een streek in enkele jaren sterk doen zakken.",
            antwoord=True,
            uitleg="Mensen vluchten weg en komen niet altijd terug. In Syrië liepen hele steden leeg in minder dan tien jaar.",
        ),
        "Op een wereldkaart van de HDI valt een duidelijk patroon op. Welk?": dict(
            type="meerkeuze",
            vraag="In welke streek verwacht je door de klimaatverandering dat er mensen zullen wegtrekken?",
            opties=[
                "Een streek waar het drinkwater opraakt",
                "Een streek waar de winters korter worden",
                "Een streek die hoog in de bergen ligt",
                "Een streek met veel bos rond de dorpen",
            ],
            antwoord=0,
            uitleg="Zonder water is landbouw en zelfs wonen onmogelijk. Kortere winters of veel bos zijn op zich geen reden om te vertrekken.",
        ),
        "Een tabel geeft per land de levensverwachting, de scholingsduur en het inkomen. Wat kan je daarmee?": dict(
            type="meerkeuze",
            vraag="Je vergelijkt twee kaarten van de bevolkingsdichtheid van hetzelfde land. Waarop let je eerst?",
            opties=[
                "Op het jaartal en op de klassen van de legende",
                "Op de kleur die de kaartmaker gekozen heeft",
                "Op het formaat waarop de kaart afgedrukt is",
                "Op de taal waarin de titel geschreven staat",
            ],
            antwoord=0,
            uitleg="Zonder hetzelfde jaartal en dezelfde klassen vergelijk je appels met peren. De kleur en het formaat veranderen de cijfers niet.",
        ),
        "De HDI meet ook hoe gelijk de welvaart binnen een land verdeeld is.": dict(
            type="waarofniet",
            vraag="Armoede zorgt er altijd voor dat mensen uit hun streek wegtrekken.",
            antwoord=False,
            uitleg="Verhuizen kost geld, papieren en contacten. Wie het armst is, blijft daarom vaak net achter, terwijl mensen met iets meer middelen vertrekken.",
        ),
        "Waarom zet men de HDI op een kaart in plaats van alleen in een tabel?": dict(
            type="meerkeuze",
            vraag="Waarom blijft een streek met vruchtbare grond vaak dichtbevolkt, ook zonder industrie?",
            opties=[
                "Er groeit genoeg voedsel voor veel mensen",
                "Er is altijd werk te vinden in de fabrieken",
                "De grond is er veel goedkoper dan elders",
                "Het klimaat is er milder dan in de buurstreken",
            ],
            antwoord=0,
            uitleg="Waar de landbouw veel mensen kan voeden, blijven er veel mensen wonen. De Nijlvallei en de delta van de Ganges zijn daar voorbeelden van.",
        ),
        "Welke uitspraak over rijkdom en ontwikkeling klopt?": dict(
            type="meerkeuze",
            vraag="Welke uitspraak over welvaart en bevolkingsdichtheid klopt?",
            opties=[
                "Er is geen vast verband tussen die twee",
                "Een hogere dichtheid geeft altijd meer welvaart",
                "Een hogere dichtheid geeft altijd minder welvaart",
                "De welvaart wordt in de dichtheid meegerekend",
            ],
            antwoord=0,
            uitleg="Nederland is dichtbevolkt en welvarend, Bangladesh is dichtbevolkt en arm, Canada is dunbevolkt en welvarend. De twee meten verschillende dingen.",
        ),
        "Hoe noem je met één woord het niveau van welvaart, gezondheid en onderwijs in een land, dat de HDI probeert te meten?": dict(
            type="invultekst",
            vraag="Hoe noem je met één woord het niveau van welvaart, gezondheid en onderwijs in een land?",
            antwoord=["ontwikkelingsgraad", "de ontwikkelingsgraad"],
            uitleg="De ontwikkelingsgraad vat samen hoe goed het met de mensen in een land gaat. Ze verbeteren is een belangrijke stap naar een duurzame wereld.",
        ),
        "De HDI van een land kan door de jaren heen stijgen en dalen.": dict(
            type="waarofniet",
            vraag="Een politieke beslissing kan de bevolkingsdichtheid van een streek veranderen.",
            antwoord=True,
            uitleg="Wie een haven, een luchthaven of een hoofdstad op een bepaalde plaats zet, trekt daar mensen naartoe. Brasilia werd zo in het binnenland uit het niets gebouwd.",
        ),
        "Wat is het verband tussen ontwikkelingsgraad en bevolkingsdichtheid?": dict(
            type="meerkeuze",
            vraag="Een streek is dunbevolkt en heeft toch veel grondstoffen in de grond. Wat verwacht je er?",
            opties=[
                "Mijnen of putten met weinig mensen errond",
                "Een dichte rij steden langs de hele streek",
                "Veel landbouw op kleine, vruchtbare percelen",
                "Een hoge bevolkingsdichtheid in het hele gebied",
            ],
            antwoord=0,
            uitleg="Moderne ontginning vraagt machines, niet veel handen. In Noord-Australië en Siberië liggen grote mijnen in een vrijwel leeg landschap.",
        ),
        "Je moet bij een bron over de HDI kritisch nakijken. Waarop let je? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke gegevens heb je nodig om te weten of een streek in tien jaar dichter bevolkt werd? Kruis alles aan wat juist is.",
            opties=[
                "het aantal inwoners tien jaar geleden",
                "het aantal inwoners van vandaag",
                "de oppervlakte van die streek",
                "de klimaatzone van die streek",
                "de hoogte boven de zeespiegel",
            ],
            antwoord=[0, 1, 2],
            uitleg="Met twee keer het aantal inwoners en de oppervlakte bereken je de dichtheid van toen en van nu. Klimaatzone en hoogte verklaren wel iets, maar meten niets.",
        ),
        "Een land met een lage HDI is een land waar niemand rijk is.": dict(
            type="waarofniet",
            vraag="Een dunbevolkte streek is altijd een arme streek.",
            antwoord=False,
            uitleg="IJsland, Canada en Australië zijn dunbevolkt en welvarend. Hoeveel mensen er wonen zegt op zich niets over hoe het hun gaat.",
        ),
    }
)

# ───────────────────────── Hoe een bevolking verandert. Geen vruchtbaarheids-
# cijfer, geen migratiesaldo en geen transitiemodel met fasen; wel de vijf
# kengetallen die de fiche opsomt en het verloop uit grafieken en tabellen.
VERVANGINGEN.update(
    {
        "Waarop slaat het geboortecijfer van een land?": dict(
            type="meerkeuze",
            vraag="Waarop slaat het geboortecijfer van een land?",
            opties=[
                "Het aantal geboorten per duizend inwoners per jaar",
                "Het aantal kinderen dat een vrouw gemiddeld krijgt",
                "Het aantal geboorten in dat land in één jaar tijd",
                "Het aandeel kinderen in de bevolking van dat land",
            ],
            antwoord=0,
            uitleg="Het geboortecijfer is een verhoudingsgetal per duizend inwoners, zodat je grote en kleine landen met elkaar kan vergelijken. Het gewone aantal geboorten zegt zonder het aantal inwoners niets.",
        ),
        "Wat is het migratiesaldo van een land?": dict(
            type="meerkeuze",
            vraag="In een land is de immigratie groter dan de emigratie. Wat betekent dat?",
            opties=[
                "Er komen meer mensen bij dan er vertrekken",
                "Er vertrekken meer mensen dan er bijkomen",
                "Er worden meer kinderen geboren dan er mensen sterven",
                "Er wonen meer mensen in de stad dan op het platteland",
            ],
            antwoord=0,
            uitleg="Immigratie is aankomen, emigratie is vertrekken. Komen er meer mensen aan dan er vertrekken, dan groeit de bevolking door migratie, ook als er weinig kinderen geboren worden.",
        ),
        "Welke kengetallen heb je nodig om de totale bevolkingsgroei van een land te kennen? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke kengetallen heb je nodig om de totale bevolkingsgroei van een land te kennen? Kruis alles aan wat juist is.",
            opties=[
                "het geboortecijfer van dat land",
                "het sterftecijfer van dat land",
                "de immigratie en de emigratie",
                "de oppervlakte van dat land",
                "de klimaatzone van dat land",
            ],
            antwoord=[0, 1, 2],
            uitleg="Geboorten min sterften geeft de natuurlijke aangroei; daarbij komt wie aankomt en wie vertrekt. Oppervlakte en klimaatzone zeggen over de groei zelf niets.",
        ),
        "Een land waar de natuurlijke aangroei negatief is, kan toch in bevolking groeien.": dict(
            type="waarofniet",
            vraag="Een land waar de natuurlijke aangroei negatief is, kan toch in bevolking groeien.",
            antwoord=True,
            uitleg="Dat kan als er genoeg mensen bijkomen van buiten het land. In verschillende West-Europese landen komt de groei vandaag bijna helemaal van immigratie.",
        ),
        "Wat betekent een vruchtbaarheidscijfer van 1,4?": dict(
            type="meerkeuze",
            vraag="Waarom daalt het geboortecijfer meestal als de welvaart in een land stijgt?",
            opties=[
                "Kinderen gaan langer naar school en vrouwen werken buitenshuis",
                "Er worden door de welvaart minder mensen geboren per jaar",
                "De gezondheidszorg maakt het krijgen van kinderen moeilijker",
                "De overheid verbiedt in welvarende landen grote gezinnen",
            ],
            antwoord=0,
            uitleg="Met onderwijs, werk en een pensioen verandert de plaats van kinderen in een gezin. Welvaart en welzijn horen daarom bij de factoren die een bevolkingsevolutie verklaren.",
        ),
        "Hoe noem je het geboortecijfer min het sterftecijfer van een land?": dict(
            type="invultekst",
            vraag="Hoe noem je het geboortecijfer min het sterftecijfer van een land?",
            antwoord=["natuurlijke aangroei", "de natuurlijke aangroei"],
            uitleg="De natuurlijke aangroei telt alleen geboorten en sterften mee. Wil je de totale groei, dan reken je de immigratie en de emigratie erbij.",
        ),
        "Het migratiesaldo van de hele wereld samen is nul.": dict(
            type="waarofniet",
            vraag="Wie uit een land emigreert, immigreert in een ander land.",
            antwoord=True,
            uitleg="Wie ergens vertrekt, komt elders aan. Voor de wereld samen heffen aankomst en vertrek elkaar dus op; alleen per land blijft er een verschil over.",
        ),
        "Wat beschrijft het model van de demografische transitie?": dict(
            type="meerkeuze",
            vraag="Met welke bronnen leg je het verloop van het geboorte- en het sterftecijfer van een land uit?",
            opties=[
                "Met grafieken en tabellen van die cijfers",
                "Met een klimatogram van dat land",
                "Met een determineertabel van gesteenten",
                "Met een satellietbeeld van dat land",
            ],
            antwoord=0,
            uitleg="Een lijngrafiek laat de twee cijfers naast elkaar lopen en toont waar het gat tussen beide wijder of smaller wordt. Een klimatogram of een satellietbeeld toont die cijfers niet.",
        ),
        "In welke fase van de demografische transitie zijn zowel het geboortecijfer als het sterftecijfer hoog en groeit de bevolking nauwelijks?": dict(
            type="meerkeuze",
            vraag="In een land zijn het geboortecijfer en het sterftecijfer beide hoog. Wat gebeurt er met de bevolking?",
            opties=[
                "Ze blijft ongeveer gelijk",
                "Ze groeit elk jaar snel aan",
                "Ze krimpt elk jaar fors",
                "Ze verdubbelt in tien jaar tijd",
            ],
            antwoord=0,
            uitleg="Er worden veel kinderen geboren, maar er sterven ook veel mensen. De twee cijfers liggen dicht bij elkaar, dus blijft het aantal inwoners ongeveer op zijn plaats.",
        ),
        "Waarom groeit de bevolking het snelst in de tweede fase van de transitie?": dict(
            type="meerkeuze",
            vraag="In een land daalt het sterftecijfer snel terwijl het geboortecijfer hoog blijft. Wat gebeurt er met de bevolking?",
            opties=[
                "Ze groeit snel aan",
                "Ze blijft ongeveer gelijk",
                "Ze begint te krimpen",
                "Ze veroudert zonder te groeien",
            ],
            antwoord=0,
            uitleg="Betere voeding, drinkwater en gezondheidszorg doen de sterfte zakken. Gewoonten rond kinderen krijgen veranderen veel trager, dus loopt het gat tussen beide cijfers wijd open.",
        ),
        "In de vierde fase van de demografische transitie liggen geboorte- en sterftecijfer allebei laag.": dict(
            type="waarofniet",
            vraag="In een land met een laag geboortecijfer en een lange levensverwachting stijgt het aandeel ouderen.",
            antwoord=True,
            uitleg="Onderaan komen er minder kinderen bij en bovenaan blijven de mensen langer leven. Samen tilt dat het aandeel ouderen omhoog, en dat is vergrijzing.",
        ),
        "Een land heeft een geboortecijfer van 34 ‰ en een sterftecijfer van 9 ‰. In welke fase zit het waarschijnlijk?": dict(
            type="meerkeuze",
            vraag="Een land heeft een geboortecijfer van 34 ‰ en een sterftecijfer van 9 ‰. Wat verwacht je er?",
            opties=[
                "Een snel groeiende, jonge bevolking",
                "Een krimpende, sterk verouderde bevolking",
                "Een bevolking die al jaren gelijk blijft",
                "Een bevolking die vooral door migratie groeit",
            ],
            antwoord=0,
            uitleg="De natuurlijke aangroei is 25 per duizend, dus bijna drie procent per jaar. Zo'n land heeft een brede basis in zijn leeftijdshistogram.",
        ),
        "Waarom volgt niet elk land de demografische transitie op dezelfde manier?": dict(
            type="meerkeuze",
            vraag="Waarom verschilt de bevolkingsevolutie zo sterk van land tot land?",
            opties=[
                "Beleid, oorlog, welvaart en cultuur verlopen overal anders",
                "Alleen landen op het noordelijk halfrond zien hun cijfers dalen",
                "De cijfers hangen bijna volledig van de oppervlakte af",
                "De cijfers werden pas sinds enkele jaren bijgehouden",
            ],
            antwoord=0,
            uitleg="Een geboortebeleid, een oorlog, de welvaart en wat in een streek gebruikelijk is, grijpen in elkaar. Eén enkele oorzaak aanwijzen klopt zelden.",
        ),
        "Een land in de vierde fase van de transitie heeft dezelfde leeftijdsstructuur als een land in de eerste fase.": dict(
            type="waarofniet",
            vraag="Twee landen waarvan de bevolking even traag groeit, hebben daarom ook dezelfde leeftijdsopbouw.",
            antwoord=False,
            uitleg="Een bevolking kan traag groeien met veel kinderen en veel sterfgevallen, of met weinig kinderen en veel ouderen. In het histogram zien die twee er helemaal anders uit.",
        ),
        "Een land heeft een negatief migratiesaldo en veel vertrek van jonge, opgeleide mensen. Welke gevolgen verwacht je?": dict(
            type="meerkeuze",
            vraag="Uit een land vertrekken veel jonge, opgeleide mensen en er komen er weinig bij. Welke gevolgen verwacht je?",
            opties=[
                "De bevolking veroudert en er verdwijnt kennis uit het land",
                "De bevolking verjongt en de arbeidsmarkt wordt krapper",
                "Het geboortecijfer stijgt en de vergrijzing neemt af",
                "De bevolkingsdichtheid stijgt in het hele land",
            ],
            antwoord=0,
            uitleg="Wie vertrekt is meestal jong en opgeleid. De achterblijvende bevolking wordt dus gemiddeld ouder, en het land verliest mensen die het net nodig heeft.",
        ),
    }
)

# ───────────────────────── Stad en platteland. Geen hiërarchie van steden, geen
# inbreiding en geen stadslandbouw; wel wat de fiche zet over segregatie,
# multiculturaliteit, functiewijziging en het veranderende landschap.
VERVANGINGEN.update(
    {
        "Welke beïnvloedende factoren noemt de vakfiche bij de keuze tussen stad en platteland? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke factoren spelen mee in de keuze tussen de stad en het platteland? Kruis alles aan wat juist is.",
            opties=[
                "het klimaat en de klimaatverandering",
                "de politieke en de oorlogssituatie",
                "de welvaart, het welzijn en armoede",
                "het aantal meridianen over het land",
                "de kleurkeuze van de kaartmaker",
            ],
            antwoord=[0, 1, 2],
            uitleg="Klimaat en klimaatverandering, reliëf, bodemkwaliteit, de politieke situatie, de oorlogssituatie, welvaart en welzijn, en armoede: dat is de hele rij. Meridianen en kleuren horen bij het lezen van een kaart.",
        ),
        "Een gezin verhuist van de stad naar een dorp twintig kilometer verderop, voor een tuin en een rustiger straat. Hoe noem je dat?": dict(
            type="meerkeuze",
            vraag="Een gezin verhuist van de stad naar een dorp twintig kilometer verderop, voor een tuin en een rustiger straat. Hoe noem je dat?",
            opties=["Stadsvlucht", "Verstedelijking", "Ontvolking", "Segregatie"],
            antwoord=0,
            uitleg="Stadsvlucht is het vertrek van stadsbewoners naar de rand en het platteland. Het is een van de motoren achter de verstedelijking van dorpen.",
        ),
        "Op welke gronden bepaalt men de hiërarchie tussen steden?": dict(
            type="meerkeuze",
            vraag="Wat bedoelt men met een functiewijziging in een stad?",
            opties=[
                "Een gebouw of een wijk krijgt een ander gebruik",
                "Een wijk krijgt er in korte tijd veel inwoners bij",
                "Een stad krijgt een nieuw bestuur na de verkiezingen",
                "Een straat wordt voor het autoverkeer afgesloten",
            ],
            antwoord=0,
            uitleg="Een fabriek wordt een woonblok, een kerk een bibliotheek, een warenhuis een school. Het gebouw blijft staan, wat erin gebeurt verandert.",
        ),
        "Hoe noem je met één woord de rangorde tussen steden op basis van hun belang?": dict(
            type="invultekst",
            vraag="Hoe noem je het leeglopen van afgelegen dorpen, waar werk en voorzieningen verdwijnen?",
            antwoord=["ontvolking", "de ontvolking"],
            uitleg="Ontvolking is het omgekeerde van verstedelijking. Eerst verdwijnen de winkel, de school en de bus, en daarna de mensen.",
        ),
        "Waarom staat Brussel hoog in de Europese stedenhiërarchie, ook al is het niet de grootste stad van Europa?": dict(
            type="meerkeuze",
            vraag="Waarom trekt Brussel zoveel internationale bedrijven en organisaties aan?",
            opties=[
                "Er zetelen belangrijke Europese instellingen",
                "Het ligt precies in het midden van het continent",
                "Het heeft de grootste haven van het continent",
                "Het heeft het oudste stadscentrum van Europa",
            ],
            antwoord=0,
            uitleg="Door de Europese instellingen en de NAVO komen er diplomaten, lobbyisten en hoofdkantoren naartoe. Die banen trekken op hun beurt opnieuw mensen aan.",
        ),
        "Een dorp krijgt er in twintig jaar drie verkavelingen bij, maar geen enkele nieuwe winkel. Wat gebeurt er?": dict(
            type="meerkeuze",
            vraag="Een dorp krijgt er in twintig jaar drie verkavelingen bij, maar geen enkele nieuwe winkel. Wat gebeurt er?",
            opties=[
                "Het wordt een woondorp waar men voor alles wegrijdt",
                "Het wordt daardoor een stad met een eigen centrum",
                "De bevolkingsdichtheid van het dorp daalt erdoor",
                "De open ruimte rond het dorp neemt erdoor toe",
            ],
            antwoord=0,
            uitleg="Wonen komt erbij, voorzieningen niet. De inwoners werken, winkelen en gaan naar school elders, en de autoafhankelijkheid van het dorp neemt toe.",
        ),
        "Wat is inbreiding?": dict(
            type="meerkeuze",
            vraag="Wat bedoelt men met de versnippering van de open ruimte?",
            opties=[
                "Wegen en bebouwing hakken ze in kleine stukken",
                "Ze wordt in één keer volledig volgebouwd",
                "Ze wordt opgekocht door één grote eigenaar",
                "Ze verandert van landbouwgrond in natuurgebied",
            ],
            antwoord=0,
            uitleg="Elke weg en elke verkaveling snijdt een stuk af. Wat overblijft zijn kleine lapjes waar grotere dieren niet meer tussen kunnen bewegen.",
        ),
        "Waarom kiezen veel steden vandaag voor inbreiding in plaats van uitbreiding?": dict(
            type="meerkeuze",
            vraag="Waarom proberen steden vandaag te bouwen op plekken die al gebruikt werden?",
            opties=[
                "Zo blijft de open ruimte buiten de stad gespaard",
                "Zo wordt bouwen binnen de stad altijd goedkoper",
                "Zo daalt het aantal inwoners van de stad sneller",
                "Zo verdwijnt de sociale segregatie uit de wijken",
            ],
            antwoord=0,
            uitleg="Open ruimte is in Vlaanderen schaars geworden. Bouwen op een oud bedrijfsterrein houdt bovendien de voorzieningen dicht bij de mensen, waardoor er minder autokilometers nodig zijn.",
        ),
        "Wat is stadslandbouw?": dict(
            type="meerkeuze",
            vraag="Wat is een gevolg van veranderende mobiliteit voor het landschap?",
            opties=[
                "Rond afritten en stations komt er bebouwing bij",
                "De bevolking van een stad verdubbelt in tien jaar",
                "Het klimaat van een streek wordt er milder van",
                "De bodemkwaliteit van de akkers verbetert erdoor",
            ],
            antwoord=0,
            uitleg="Waar een snelweg of een spoorlijn komt, volgen bedrijven en woningen. Zo trekt een nieuwe verbinding het landschap mee in een andere vorm.",
        ),
        "Welke voordelen worden aan stadslandbouw toegeschreven? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke veranderingen horen bij de groei van een stad? Kruis alles aan wat juist is.",
            opties=[
                "nieuwe wijken aan de rand van de stad",
                "meer verharding en minder open ruimte",
                "meer verkeer op de wegen naar het centrum",
                "een dalende bevolkingsdichtheid in de stad",
                "een kleiner wordend bebouwd oppervlak",
            ],
            antwoord=[0, 1, 2],
            uitleg="Een groeiende stad zet zich uit, verhardt meer grond en genereert meer verplaatsingen. De dichtheid en het bebouwde oppervlak dalen daarbij juist niet.",
        ),
        "Een gemeente breekt een betonnen plein open en plant er bomen. Welk probleem pakt ze daarmee aan?": dict(
            type="meerkeuze",
            vraag="Een gemeente breekt een betonnen plein open en plant er bomen. Welk probleem pakt ze daarmee aan?",
            opties=[
                "De hitte en het wegstromen van regenwater",
                "De sociale segregatie tussen de wijken",
                "De ontvolking van het platteland eromheen",
                "De multiculturaliteit van de buurt errond",
            ],
            antwoord=0,
            uitleg="Minder verharding betekent meer schaduw, meer verdamping en water dat in de bodem trekt. Aan segregatie of ontvolking verandert een plein niets.",
        ),
    }
)

# ───────────────────────── Grondstoffen, energie en industrie. Geen reconversie
# en geen outsourcing; wel de scholingsgraad als sociaaleconomische factor.
VERVANGINGEN.update(
    {
        "Waarom kiest een bedrijf voor dagbouw als dat kan?": dict(
            type="meerkeuze",
            vraag="Waarom kiest een bedrijf voor dagbouw als dat kan?",
            opties=[
                "Het is goedkoper en veiliger dan ondergronds werken",
                "Het levert altijd zuiverder erts op dan een mijn",
                "Het is beter voor het landschap dan een mijn",
                "Het kan alleen in gebieden zonder bergen",
            ],
            antwoord=0,
            uitleg="Geen schachten, geen instortingsgevaar, grote machines die veel tegelijk verzetten: dat drukt de kosten. Voor het landschap is dagbouw juist ingrijpender, want er verdwijnt een hele laag grond.",
        ),
        "Welke fysische factoren beïnvloeden waar energie geproduceerd wordt? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke fysische factoren beïnvloeden waar energie geproduceerd wordt? Kruis alles aan wat juist is.",
            opties=[
                "het klimaat en de klimaatverandering",
                "het reliëf van het gebied",
                "de grondstoffen in de bodem",
                "de staatsvorm van het land",
                "het loon van de werknemers",
            ],
            antwoord=[0, 1, 2],
            uitleg="Klimaat, reliëf en grondstoffen zijn fysische factoren. De staatsvorm is geopolitiek en de verloning sociaaleconomisch; die drie groepen staan bewust naast elkaar.",
        ),
        "Hoe noem je het omvormen van een oud industrieterrein tot iets nieuws, zoals de mijnsite van Genk die een bedrijven- en onderzoekspark werd?": dict(
            type="invultekst",
            vraag="Hoe noem je de brandstoffen die uit de resten van planten en dieren in de bodem ontstonden?",
            antwoord=["fossiele brandstoffen", "fossiele brandstof", "fossiel"],
            uitleg="Steenkool, aardolie en aardgas zijn fossiele brandstoffen. Ze raken op en komen daarom bij de niet-hernieuwbare energiebronnen te staan.",
        ),
        "Welke sociaaleconomische factoren noemt de vakfiche bij het industriële proces? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke sociaaleconomische factoren beïnvloeden het industriële proces? Kruis alles aan wat juist is.",
            opties=[
                "de opleiding van de werknemers",
                "de verloning van de werknemers",
                "vraag en aanbod en de afzetmarkt",
                "de klimaatzone van het gebied",
                "de reliëfeenheid van het gebied",
            ],
            antwoord=[0, 1, 2],
            uitleg="Hoe geschoold de mensen zijn, wat ze verdienen, en of er vraag is naar het product: dat zijn sociaaleconomische factoren. Klimaatzone en reliëfeenheid horen bij de fysische.",
        ),
        "Hoe noem je het verplaatsen van werk of productie naar een bedrijf in een ander land?": dict(
            type="invultekst",
            vraag="Hoe noem je het opleidingsniveau van de mensen in een streek, een factor bij het kiezen van een vestigingsplaats?",
            antwoord=["scholingsgraad", "de scholingsgraad"],
            uitleg="Een bedrijf dat ingenieurs of technici nodig heeft, zoekt een streek waar die te vinden zijn. Daarom staat de scholingsgraad bij de sociaaleconomische factoren.",
        ),
        "Een streek verliest haar mijnen, maar krijgt later een wetenschapspark en een campus. Wat is hier gebeurd?": dict(
            type="meerkeuze",
            vraag="Een streek verliest haar mijnen en de fabrieken sluiten één na één. Wat is hier gebeurd?",
            opties=[
                "De-industrialisatie",
                "Industrialisatie",
                "Verstedelijking",
                "Multiculturaliteit",
            ],
            antwoord=0,
            uitleg="De oude industrie verdwijnt en neemt het werk mee. Wat er daarna met de terreinen en met de mensen gebeurt, bepaalt of een streek weer op gang komt.",
        ),
    }
)

# ───────────────────────── Landbouw, handel en toerisme. Geen bodemerosie en
# geen bodemdegradatie; wel ontbossing, schaalvergroting en de scholingsgraad.
VERVANGINGEN.update(
    {
        "Welke fysische factoren beïnvloeden volgens de vakfiche het landbouwproces? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke fysische factoren beïnvloeden het landbouwproces? Kruis alles aan wat juist is.",
            opties=[
                "het klimaat en de klimaatverandering",
                "het reliëf van het gebied",
                "de bodemkwaliteit en de ondergrond",
                "de staatsvorm van het land",
                "de afzetmarkt van het product",
            ],
            antwoord=[0, 1, 2],
            uitleg="Bij de landbouw komen bodemkwaliteit en ondergrond er uitdrukkelijk bij, naast klimaat en reliëf. De staatsvorm is geopolitiek, de afzetmarkt sociaaleconomisch.",
        ),
        "Bodemerosie treedt sneller op wanneer een helling na de oogst kaal blijft liggen.": dict(
            type="waarofniet",
            vraag="Of een gewas ergens geteeld kan worden, hangt mee af van de ondergrond onder de bouwvoor.",
            antwoord=True,
            uitleg="Op een ondoorlaatbare laag blijft het water staan, op zand zakt het meteen weg. De diepte waarop wortels kunnen groeien, hangt er ook van af.",
        ),
        "Wat is bodemdegradatie?": dict(
            type="meerkeuze",
            vraag="Een boer verkoopt zijn melk aan een zuivelbedrijf in Duitsland. Wat is dat bedrijf voor hem?",
            opties=[
                "Zijn afzetmarkt",
                "Zijn landbouwsysteem",
                "Zijn productiewijze",
                "Zijn bodemkwaliteit",
            ],
            antwoord=0,
            uitleg="De afzetmarkt is waar het product verkocht wordt. Voor sommige boeren ligt die in het dorp, voor andere in een ander land of een ander werelddeel.",
        ),
        "Welke fysische factoren maken een streek aantrekkelijk voor toerisme? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke fysische factoren maken een streek aantrekkelijk voor toerisme? Kruis alles aan wat juist is.",
            opties=[
                "een klimaat met veel zonuren",
                "een kust met stranden",
                "een reliëf met bergen voor wintersport",
                "een hoge bevolkingsdichtheid",
                "het lidmaatschap van een handelsblok",
            ],
            antwoord=[0, 1, 2],
            uitleg="Klimaat, kust en reliëf zijn fysische troeven. Dichtheid is sociaaleconomisch en een handelsblok geopolitiek; die spelen ook mee, maar via een andere weg.",
        ),
        "De Human Development Index van een land speelt mee in hoeveel toerisme het aantrekt.": dict(
            type="waarofniet",
            vraag="De scholingsgraad van de bevolking speelt mee in hoeveel toerisme een streek aantrekt.",
            antwoord=True,
            uitleg="Gidsen, hotelpersoneel en reisleiders met talenkennis maken een bestemming bruikbaar voor bezoekers. Daarom staat de scholingsgraad bij de factoren achter het toerisme.",
        ),
        "Een bron toont dat een land vooral grondstoffen uitvoert en afgewerkte producten invoert. Wat besluit je?": dict(
            type="meerkeuze",
            vraag="Een bron toont dat een land vooral grondstoffen uitvoert en afgewerkte producten invoert. Wat besluit je?",
            opties=[
                "De bewerking en de winst gebeuren grotendeels elders",
                "Het land heeft een grote eigen verwerkende industrie",
                "Het land heeft een groot overschot op zijn handel",
                "Het land ligt noodzakelijk in de gematigde zone",
            ],
            antwoord=0,
            uitleg="Wie ruwe grondstoffen verkoopt en afgewerkte producten terugkoopt, laat de meerwaarde over aan de landen die verwerken. Dat patroon speelt in veel discussies over ontwikkeling een rol.",
        ),
    }
)

# ───────────────────────── Mondialisering. Geen protectionisme, geen vrijhandel
# en geen outsourcing; wel de samenwerkingsverbanden, de spanningen, de
# migratiebewegingen, de ontvolking, braindrain, braingain en landgrabbing.
VERVANGINGEN.update(
    {
        "Jongeren over de hele wereld volgen dezelfde muziek, series en mode. Waarvan is dat een voorbeeld?": dict(
            type="meerkeuze",
            vraag="Jongeren over de hele wereld volgen dezelfde muziek, series en mode. Waarvan is dat een voorbeeld?",
            opties=[
                "Culturele mondialisering",
                "Economische mondialisering",
                "Politieke mondialisering",
                "Een vorm van landgrabbing",
            ],
            antwoord=0,
            uitleg="Gewoonten, smaak en taal reizen mee met de media. Het gevolg is dat het aanbod overal op elkaar begint te lijken, wat plaatselijke tradities onder druk zet.",
        ),
        "Wat wordt bedoeld met outsourcing?": dict(
            type="meerkeuze",
            vraag="Wat gebeurt er met de prijs van een product als het in grote hoeveelheden op één plaats gemaakt wordt?",
            opties=[
                "De prijs per stuk zakt",
                "De prijs per stuk stijgt door het transport",
                "De prijs blijft overal precies gelijk",
                "De prijs hangt enkel van de grondstof af",
            ],
            antwoord=0,
            uitleg="De kosten van een fabriek en van machines worden over veel meer stuks verdeeld. Dat is een van de redenen waarom productie zich op enkele plaatsen in de wereld samenpakt.",
        ),
        "Hoe noem je het beschermen van de eigen markt met invoerrechten en quota?": dict(
            type="invultekst",
            vraag="Hoe noem je het opkopen of langdurig huren van grote stukken landbouwgrond in een ander land?",
            antwoord=["landgrabbing", "land grabbing"],
            uitleg="Bedrijven en staten verzekeren zich zo van voedsel of biobrandstof. De opbrengst gaat meestal naar de uitvoer en niet naar de streek zelf.",
        ),
        "Wat is het belangrijkste doel van de Verenigde Naties?": dict(
            type="meerkeuze",
            vraag="Wat is het belangrijkste doel van de Verenigde Naties?",
            opties=[
                "Vrede en samenwerking tussen bijna alle landen ter wereld",
                "Een gemeenschappelijke munt voor alle lidstaten",
                "Een gezamenlijk leger voor Europa en Noord-Amerika",
                "Een gezamenlijke markt voor Zuid-Amerika",
            ],
            antwoord=0,
            uitleg="De VN werd na de Tweede Wereldoorlog opgericht om oorlog te voorkomen. Daarnaast werkt ze rond ontwikkeling, gezondheid, vluchtelingen en klimaat.",
        ),
        "Een Afrikaans land leidt verpleegkundigen op, en velen vertrekken naar Europa. Wat gebeurt er?": dict(
            type="meerkeuze",
            vraag="Een Afrikaans land leidt verpleegkundigen op, en velen vertrekken naar Europa. Wat gebeurt er?",
            opties=[
                "Braindrain in Afrika en braingain in Europa",
                "Braingain in Afrika en braindrain in Europa",
                "Landgrabbing in Afrika en ontvolking in Europa",
                "Vergrijzing in Afrika en verjonging in Europa",
            ],
            antwoord=0,
            uitleg="Het land dat de opleiding betaalde, verliest de kennis; het land dat hen ontvangt, wint ze gratis. Daar staat tegenover dat die verpleegkundigen vaak geld naar huis sturen.",
        ),
        "Welke gevolgen van mondialisering somt de vakfiche op? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke gevolgen van mondialisering ken je? Kruis alles aan wat juist is.",
            opties=[
                "migratiebewegingen en ontvolking",
                "landgrabbing in arme landen",
                "braindrain en braingain",
                "verzilting van de landbouwgrond",
                "verschuiving van de klimaatzones",
            ],
            antwoord=[0, 1, 2],
            uitleg="Samenwerkingsverbanden, spanningen tussen landen, migratie en ontvolking, braindrain en braingain, en landgrabbing: dat is de rij. Verzilting en klimaatzones horen bij andere rubrieken.",
        ),
        "Een land kiest één keer tussen vrijhandel en protectionisme en blijft daar dan bij.": dict(
            type="waarofniet",
            vraag="Een handelsblok zoals de Europese Unie beslist ook over het leger van zijn lidstaten.",
            antwoord=False,
            uitleg="De EU gaat over handel, regels, geld en beleid. Militaire samenwerking loopt via de NAVO, en die heeft een deels andere lijst leden.",
        ),
        "Hoe noem je met één woord de handel zonder invoerrechten en drempels tussen landen?": dict(
            type="invultekst",
            vraag="Hoe noem je met één woord de wereldwijde verbondenheid van handel, cultuur en politiek?",
            antwoord=["mondialisering", "de mondialisering", "globalisering"],
            uitleg="Mondialisering is de rode draad onder de hele rubriek: de wereld hangt economisch, cultureel, sociaal en politiek steeds dichter aan elkaar.",
        ),
        "Waarom staat landgrabbing zo vaak ter discussie?": dict(
            type="meerkeuze",
            vraag="Waarom staat landgrabbing zo vaak ter discussie?",
            opties=[
                "De lokale bevolking verliest grond die ze zelf bewerkte",
                "De grond wordt er daarna nooit meer bewerkt",
                "Het gebeurt uitsluitend in Europese landen",
                "Het is bij internationaal verdrag volledig verboden",
            ],
            antwoord=0,
            uitleg="Op papier is de verkoop vaak wettelijk, maar wie het land al generaties bewerkte zonder eigendomsbewijs, staat plots buiten. De opbrengst gaat bovendien meestal naar de uitvoer.",
        ),
    }
)

# ───────────────────────── Duurzaam omgaan met de ruimte. Geen reconversie en
# geen bodemdegradatie; wel de vijf P's, de SDG's, ontbossing en
# schaalvergroting.
VERVANGINGEN.update(
    {
        "Een land met een hoge Human Development Index heeft daarom automatisch een kleine ecologische voetafdruk.": dict(
            type="waarofniet",
            vraag="Een welvarend land heeft daarom automatisch een kleine ecologische voetafdruk.",
            antwoord=False,
            uitleg="Vaak is het omgekeerde waar: hoge welvaart gaat samen met veel verbruik, veel vlees, veel vliegen en veel afval. Ontwikkeling en duurzaamheid lopen niet vanzelf gelijk.",
        ),
        "Duurzaam ruimtegebruik betekent dat je met dezelfde oppervlakte meer doet, in plaats van telkens nieuwe ruimte aan te snijden.": dict(
            type="waarofniet",
            vraag="Duurzaam ruimtegebruik betekent dat je met dezelfde oppervlakte meer doet, in plaats van telkens nieuwe ruimte aan te snijden.",
            antwoord=True,
            uitleg="Hergebruik van een leegstaand gebouw, bouwen op een oud bedrijfsterrein, een terrein met meerdere functies: dat spaart open ruimte. Nieuwe grond aansnijden is altijd de duurste keuze voor de planeet.",
        ),
        "Welke gevolgen van verstedelijking op het leefmilieu somt de vakfiche op? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke gevolgen heeft verstedelijking voor het leefmilieu? Kruis alles aan wat juist is.",
            opties=[
                "Versnippering van de open ruimte en verharding",
                "Het hitte-eilandeffect in de stad",
                "Luchtvervuiling en verkeersdrukte",
                "Schaalvergroting in de landbouw",
                "Het afsmelten van de gletsjers",
            ],
            antwoord=[0, 1, 2],
            uitleg="Versnippering, verharding, het hitte-eilandeffect, luchtvervuiling en verkeersdrukte horen bij de stad. Schaalvergroting hoort bij de landbouw, de gletsjers bij het broeikaseffect.",
        ),
        "Wat gebeurt er bij industrialisatie van een streek?": dict(
            type="meerkeuze",
            vraag="Wat gebeurt er bij industrialisatie van een streek?",
            opties=[
                "Er komt fabrieksactiviteit bij, met werk en met ruimtebeslag",
                "De fabrieken verdwijnen uit de streek, met werk en al",
                "De open ruimte in de streek neemt elk jaar toe",
                "De landbouwbedrijven in de streek worden kleiner",
            ],
            antwoord=0,
            uitleg="Industrialisatie brengt werk, inwoners en infrastructuur, maar ook uitstoot en ruimtebeslag. Het omgekeerde is de-industrialisatie, en dan verdwijnt het werk uit de streek.",
        ),
        "Wat is het duurzame voordeel van reconversie tegenover een nieuw terrein aansnijden?": dict(
            type="meerkeuze",
            vraag="Wat is het duurzame voordeel van bouwen op een oud bedrijfsterrein tegenover een nieuw terrein aansnijden?",
            opties=[
                "De grond werd al gebruikt, dus er gaat geen open ruimte verloren",
                "De grond is altijd goedkoper dan een stuk onbebouwde grond",
                "Er zijn voor zo'n terrein nooit vergunningen voor nodig",
                "De bouwwerken duren er altijd korter dan bij nieuwbouw",
            ],
            antwoord=0,
            uitleg="Ruimte die al aangesneden was, blijft aangesneden. Dat is de grootste winst, ook als de sanering en de verbouwing zelf een stuk duurder uitvallen.",
        ),
        "Waarom is bodemdegradatie een probleem voor de lange termijn?": dict(
            type="meerkeuze",
            vraag="Waarom levert akkerbouw op een pas ontbost tropisch perceel na enkele jaren veel minder op?",
            opties=[
                "De vruchtbare laag is er dun en raakt snel uitgeput",
                "Het klimaat van de streek verandert erdoor in enkele jaren",
                "De grond komt er in een andere reliëfeenheid te liggen",
                "De regen valt er na het kappen van het bos nooit meer",
            ],
            antwoord=0,
            uitleg="In een tropisch bos zit het meeste voedsel in de bomen zelf, niet in de grond. Is het bos weg, dan is de voorraad na een paar oogsten op en trekt men verder.",
        ),
        "Een stad legt een fietssnelweg aan en verlaagt de parkeerplaatsen in het centrum. Welke problemen pakt ze daarmee aan? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Een stad legt een fietssnelweg aan en schrapt parkeerplaatsen in het centrum. Welke problemen pakt ze daarmee aan? Kruis alles aan wat juist is.",
            opties=[
                "Luchtvervuiling in het centrum",
                "Verkeersdrukte in de straten",
                "Verharding door parkeerplaatsen",
                "Schaalvergroting op de akkers errond",
                "Versnippering door de ringweg",
            ],
            antwoord=[0, 1, 2],
            uitleg="Minder auto's betekent minder uitstoot, minder drukte en minder asfalt. Aan de landbouw errond of aan een bestaande ringweg verandert een fietspad niets.",
        ),
        "Hoe noem je het opnieuw inrichten van een oude industriesite voor een nieuw gebruik, zoals wonen of onderzoek?": dict(
            type="invultekst",
            vraag="Met welke afkorting van drie letters duidt men de duurzame ontwikkelingsdoelen van de Verenigde Naties aan?",
            antwoord=["sdg", "sdg's", "de sdg's"],
            uitleg="SDG staat voor sustainable development goals. Je krijgt het overzicht ervan op het examen, dus je hoeft ze niet van buiten te kennen.",
        ),
    }
)

# ───────────────────────── Het versterkte broeikaseffect. Geen stralingsbalans
# en geen albedo; wel de koolstofcyclus tussen de vier sferen.
VERVANGINGEN.update(
    {
        "Welke van deze zijn broeikasgassen volgens de vakfiche? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke van deze gassen werken als broeikasgas? Kruis alles aan wat juist is.",
            opties=["Koolstofdioxide", "Methaan", "Lachgas", "Zuurstof", "Stikstofgas"],
            antwoord=[0, 1, 2],
            uitleg="Waterdamp, koolstofdioxide, methaan en lachgas houden warmte vast. Zuurstof en stikstofgas vormen samen het grootste deel van de lucht maar werken niet als broeikasgas.",
        ),
        "Wat is de stralingsbalans van de aarde?": dict(
            type="meerkeuze",
            vraag="Wat bedoelt men met de biosfeer?",
            opties=[
                "Alle levende wezens op aarde",
                "Alle lucht rond de aarde",
                "Al het water op en in de aarde",
                "Alle gesteente en bodem van de aarde",
            ],
            antwoord=0,
            uitleg="De vier sferen zijn de geosfeer, de biosfeer, de atmosfeer en de hydrosfeer. Koolstof schuift tussen die vier heen en weer.",
        ),
        "Wat betekent albedo?": dict(
            type="meerkeuze",
            vraag="Langs welke weg gaat koolstof van de atmosfeer naar de hydrosfeer?",
            opties=[
                "Koolstofdioxide lost op in het zeewater",
                "Regen spoelt koolstof uit het gesteente",
                "Vulkanen blazen koolstof in de oceaan",
                "Dieren brengen koolstof naar de zeebodem",
            ],
            antwoord=0,
            uitleg="De oceanen slorpen een flink deel van de uitgestoten koolstofdioxide op. Daardoor stijgt de temperatuur voorlopig trager, maar wordt het zeewater wel zuurder.",
        ),
        "Welk oppervlak heeft het hoogste albedo?": dict(
            type="meerkeuze",
            vraag="Waarom noemt men de koolstofcyclus een kringloop?",
            opties=[
                "De koolstof gaat van sfeer naar sfeer en komt weer terug",
                "De koolstof blijft altijd in dezelfde sfeer rondgaan",
                "De hoeveelheid koolstof op aarde neemt elk jaar toe",
                "De koolstof verdwijnt na een tijd helemaal uit de aarde",
            ],
            antwoord=0,
            uitleg="Een plant haalt koolstof uit de lucht, een dier eet de plant, bij afbraak komt ze weer vrij, en een deel belandt voor miljoenen jaren in het gesteente. Er gaat niets verloren, het verhuist.",
        ),
        "Als zee-ijs smelt, komt er donkerder water bloot dat meer warmte opneemt.": dict(
            type="waarofniet",
            vraag="Een bos dat gekapt en verbrand wordt, geeft zijn koolstof aan de atmosfeer.",
            antwoord=True,
            uitleg="Alles wat in de stammen, de takken en de bodem lag opgeslagen, komt bij het verbranden als koolstofdioxide vrij. Daarom telt ontbossing mee in de uitstoot van een land.",
        ),
        "Hoe noem je het weerkaatsingsvermogen van een oppervlak, dat bij sneeuw hoog en bij een oceaan laag is?": dict(
            type="invultekst",
            vraag="Hoe noem je de kringloop waarin koolstof tussen de vier sferen beweegt?",
            antwoord=["koolstofcyclus", "de koolstofcyclus", "koolstofkringloop"],
            uitleg="De koolstofcyclus verbindt de geosfeer, de biosfeer, de atmosfeer en de hydrosfeer. Wie fossiele brandstoffen verbrandt, versnelt één stap van die cyclus enorm.",
        ),
        "Als drijvend zee-ijs smelt, stijgt daardoor de zeespiegel.": dict(
            type="waarofniet",
            vraag="Als drijvend zee-ijs smelt, stijgt daardoor de zeespiegel.",
            antwoord=False,
            uitleg="Drijvend ijs verplaatst al evenveel water als het weegt, dus het smelten ervan verandert het peil niet. Alleen ijs dat op land ligt, zoals op Groenland, doet de zeespiegel stijgen.",
        ),
        "Waarom kunnen tropische ziektes zich uitbreiden naar onze streken?": dict(
            type="meerkeuze",
            vraag="Welk gevolg heeft de opwarming voor de gletsjers in het hooggebergte?",
            opties=[
                "Ze krimpen, en de rivieren krijgen in de zomer minder water",
                "Ze groeien, want er valt meer sneeuw in de winter",
                "Ze blijven gelijk, want in de bergen is het altijd koud",
                "Ze schuiven naar beneden, de valleien in",
            ],
            antwoord=0,
            uitleg="Een gletsjer is een waterreservoir dat in de zomer traag leegloopt. Verdwijnt hij, dan valt dat zomerdebiet weg, net wanneer landbouw en drinkwater het hardst nodig zijn.",
        ),
        "Welke gevolgen van het versterkte broeikaseffect noemt de vakfiche? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke gevolgen heeft het versterkte broeikaseffect? Kruis alles aan wat juist is.",
            opties=[
                "Zeespiegelstijging en verschuiving van klimaatzones",
                "Verschuiving van leefgebieden van planten en dieren",
                "Meer en zwaardere extreme weerfenomenen",
                "Versnippering van de open ruimte door wegen",
                "Braindrain uit landen met weinig middelen",
            ],
            antwoord=[0, 1, 2],
            uitleg="Die vier horen bij het broeikaseffect. Versnippering hoort bij de rubriek duurzaamheid en braindrain bij mondialisering.",
        ),
        "Wat betekent een terugkoppeling in het klimaatsysteem?": dict(
            type="meerkeuze",
            vraag="Wat betekent een terugkoppeling in het klimaatsysteem?",
            opties=[
                "Een gevolg dat zijn eigen oorzaak versterkt of verzwakt",
                "Een meting die achteraf wordt bijgesteld",
                "Een klimaatmodel dat naar het verleden kijkt",
                "Een afspraak tussen landen over de uitstoot",
            ],
            antwoord=0,
            uitleg="Dooiende permafrost laat methaan vrij, dat de opwarming versterkt, waardoor er nog meer permafrost dooit. Zulke lussen maken het systeem moeilijk voorspelbaar.",
        ),
        "Waarom treft de opwarming niet elk land even hard?": dict(
            type="meerkeuze",
            vraag="Waarom treft de opwarming niet elk land even hard?",
            opties=[
                "Ligging, reliëf en welvaart bepalen mee hoe kwetsbaar een land is",
                "Alleen landen op het noordelijk halfrond warmen op",
                "Alleen landen langs de evenaar merken er iets van",
                "De opwarming volgt precies de landsgrenzen op de kaart",
            ],
            antwoord=0,
            uitleg="Een laaggelegen deltastaat met weinig middelen loopt veel meer risico dan een bergland dat zich kan beschermen. Wie het minst uitstootte, draagt vaak de zwaarste gevolgen.",
        ),
    }
)

# ───────────────────────── Een geografisch onderzoek voeren. Hier verandert de
# inhoud niet; alleen de verwijzingen naar de fiche gaan uit de vraagtekst.
VERVANGINGEN.update(
    {
        "Over welke thema's kan je onderzoek volgens de vakfiche gaan? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Over welke thema's kan je geografisch onderzoek gaan? Kruis alles aan wat juist is.",
            opties=[
                "Mobiliteit, met files, lawaai en luchtvervuiling",
                "Waterproblemen, met tekort en overstromingen",
                "Veranderend landgebruik en klimaatverandering",
                "De geschiedenis van de Belgische staatshervorming",
                "De bouw van een fabriek in een ander werelddeel",
            ],
            antwoord=[0, 1, 2],
            uitleg="Er zijn er vier: mobiliteit, waterproblematieken, veranderend landgebruik en klimaatverandering. Telkens onderzoek je de oorzaken én de gevolgen in het landschap.",
        ),
        "Welke van deze horen bij de geografische hulpbronnen uit de fiche? (meerdere antwoorden mogelijk)": dict(
            type="meerkeuze",
            vraag="Welke van deze horen bij de geografische hulpbronnen? Kruis alles aan wat juist is.",
            opties=[
                "Kaarten, luchtfoto's en satellietbeelden",
                "Grafieken, tabellen en cijfergegevens",
                "Klimatogrammen en leeftijdshistogrammen",
                "De mening van je buren over het onderwerp",
                "Je eigen herinnering aan hoe het vroeger was",
            ],
            antwoord=[0, 1, 2],
            uitleg="Een atlas, kaarten, satellietbeelden, foto's, tekeningen, teksten, cijfers, grafieken, klimatogrammen en diagrammen horen erbij. Meningen en herinneringen zijn interessant maar geen hulpbron in die zin.",
        ),
        "Een besluit mag ook zeggen dat er te weinig gegevens waren om de vraag te beantwoorden.": dict(
            type="waarofniet",
            vraag="Een besluit mag ook zeggen dat er te weinig gegevens waren om de vraag te beantwoorden.",
            antwoord=True,
            uitleg="Eerlijk zijn over wat je niet weet, hoort bij onderzoek. Je moet trouwens uitdrukkelijk ook de beperkingen van je bronnen kunnen benoemen.",
        ),
        "Je wil weten hoeveel hectare een bedrijventerrein beslaat. Wat gebruik je?": dict(
            type="meerkeuze",
            vraag="Je wil weten hoeveel hectare een bedrijventerrein beslaat. Wat gebruik je?",
            opties=[
                "Het meetgereedschap van Geopunt",
                "De zoekbalk bovenaan de kaart",
                "De legende in het linkerpaneel",
                "De knop om een laag transparant te maken",
            ],
            antwoord=0,
            uitleg="Met het meetgereedschap teken je een lijn of een vlak en lees je de lengte of de oppervlakte af. Dat is precies waarvoor het bedoeld is.",
        ),
        "Waarom vraagt de fiche om uit te leggen hoe de digitale kaart je geholpen heeft én wat haar beperkingen waren?": dict(
            type="meerkeuze",
            vraag="Waarom moet je ook uitleggen wat een digitale kaart je níet kon vertellen?",
            opties=[
                "Een bron kritisch bekijken hoort bij het onderzoek zelf",
                "De kaart moet daarna gecorrigeerd worden door de overheid",
                "Zo weet de verbetering hoelang je gewerkt hebt",
                "Zonder die uitleg werkt de kaartlaag niet meer",
            ],
            antwoord=0,
            uitleg="Wie zegt wat zijn bron niet kan tonen, laat zien dat hij ze begrijpt. Dat is het verschil tussen een kaart aflezen en met een kaart onderzoeken.",
        ),
        "Hoe noem je het gereedschap in Geopunt waarmee je afstanden en oppervlakten bepaalt?": dict(
            type="invultekst",
            vraag="Hoe noem je het gereedschap in Geopunt waarmee je afstanden en oppervlakten bepaalt?",
            antwoord=["meetgereedschap", "het meetgereedschap", "meetinstrument"],
            uitleg="Met het meetgereedschap teken je een lijn of een veelhoek op de kaart en lees je de lengte of de oppervlakte af. Op het examen mag je het gebruiken.",
        ),
        "Bij een onderzoek naar mobiliteit kunnen lawaai en luchtkwaliteit ook een rol spelen.": dict(
            type="waarofniet",
            vraag="Bij een onderzoek naar mobiliteit kunnen lawaai en luchtkwaliteit ook een rol spelen.",
            antwoord=True,
            uitleg="Files, geluidsoverlast en luchtvervuiling horen bij hetzelfde thema. Ze zijn gevolgen van dezelfde verkeersstromen.",
        ),
        "Elk onderdeel van de vakfiche kan in het onderzoeksdeel van het examen terugkomen.": dict(
            type="waarofniet",
            vraag="Elk onderdeel van je leerstof kan in het onderzoeksdeel van het examen terugkomen.",
            antwoord=True,
            uitleg="Alle te kennen inhoud kan in dit deel verwerkt zijn. Onderzoek is dus geen apart stukje leerstof maar de manier waarop de rest getoetst wordt.",
        ),
    }
)
