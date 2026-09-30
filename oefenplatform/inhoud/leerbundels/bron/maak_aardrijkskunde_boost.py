# -*- coding: utf-8 -*-
"""De leerbundels voor aardrijkskunde op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche aardrijkskunde 2de graad doorstroomfinaliteit,
geldig vanaf 1 januari 2027. Die ene fiche geldt voor alle vijf de
doorstroomrichtingen: economische wetenschappen, humane wetenschappen, Latijn,
moderne talen en natuurwetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/aardrijkskunde.json`
doet daar het voorwerk voor.

De bundelsleutels dragen hier géén "-boost": de tien thematitels van Boost
verschillen van die van ✨ Spark, dus botsen de bestandsnamen niet, en zo vindt
`dekking.py` de bundel vanzelf terug aan de titel van het hoofdstuk. De
oefenbundels dragen wél een voorvoegsel, want die zouden anders met de
leerbundel zelf botsen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Aardrijkskunde"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Waar ligt het, en hoe weet je dat?
BUNDELS["waar-ligt-het-en-hoe-weet-je-dat"] = dict(
    vak=VAK, niveau=BOOST, titel="Waar ligt het, en hoe weet je dat?",
    onder="Het wereldgradennet, absoluut en relatief situeren, en waarom twee mensen anders over dezelfde plaats denken.",
    secties=[
        dict(kop="Het wereldgradennet", blokken=[
            ("p", "Om een plaats op aarde aan te wijzen, is er een net van lijnen over de aardbol gelegd. "
                  "De <strong>meridianen</strong> lopen van de noordpool naar de zuidpool. Ze komen in beide "
                  "polen samen, dus ze lopen niet evenwijdig. Ze geven de <strong>lengte</strong> aan."),
            ("p", "De <strong>breedtecirkels</strong> lopen wél evenwijdig, rond de aardbol, en worden korter "
                  "naarmate je dichter bij een pool komt. De langste is de <strong>evenaar</strong>, de "
                  "breedtecirkel van 0°. Die verdeelt de aarde in een noordelijk en een zuidelijk "
                  "<strong>halfrond</strong>."),
            ("fig", svg.gradennet(), "De evenaar op 0°, de keerkringen op 23,5° en de poolcirkels op 66,5°, "
                                     "elk zowel op het noordelijk als op het zuidelijk halfrond."),
            ("p", "Vier breedtecirkels hebben een eigen naam. De <strong>Kreeftskeerkring</strong> ligt op "
                  "23,5° noorderbreedte, de <strong>Steenbokskeerkring</strong> op 23,5° zuiderbreedte. De twee "
                  "<strong>poolcirkels</strong> liggen op 66,5° noorder- en zuiderbreedte. Op 90° lig je op de "
                  "<strong>pool</strong> zelf."),
            ("p", "De meridiaan van 0° heet de <strong>nulmeridiaan</strong>. Die loopt door Greenwich, bij "
                  "Londen. Alles ten oosten ervan krijgt <strong>oosterlengte</strong>, alles ten westen ervan "
                  "<strong>westerlengte</strong>. Tegenover de nulmeridiaan, ruwweg op de 180ste meridiaan door "
                  "de Stille Oceaan, ligt de <strong>datumlijn</strong>. Die maakt bochten om eilandengroepen "
                  "en landen niet in twee data te splitsen."),
            ("weetje", "Alle plaatsen op dezelfde meridiaan hebben tegelijk dezelfde <strong>zonnetijd</strong>: "
                       "daar staat de zon op hetzelfde moment het hoogst. Daarom is de lengte de basis van de tijdzones, ook al "
                       "volgen de officiële zones landsgrenzen in plaats van rechte lijnen."),
        ]),
        dict(kop="Absoluut en relatief situeren", blokken=[
            ("p", "<strong>Absoluut situeren</strong> is een plaats aanduiden met <strong>geografische "
                  "coördinaten</strong>: een paar getallen dat maar naar één punt op aarde wijst. Je leest "
                  "altijd eerst de breedte en dan de lengte. Dat is een internationale afspraak; zonder die "
                  "afspraak zou 50° 4° zowel België als de Indische Oceaan kunnen aanwijzen."),
            ("kader", "Op het examen volstaat het om te situeren op <strong>1° nauwkeurig</strong>. Eén graad "
                      "breedte is ongeveer 111 kilometer, dus het blijft een ruwe aanduiding, maar met de graden "
                      "in de kaartrand haal je die nauwkeurigheid vlot met een gewone atlas."),
            ("p", "<strong>Relatief situeren</strong> is een plaats aanduiden ten opzichte van iets anders. Dat "
                  "kan ten opzichte van <strong>fysischgeografische elementen</strong>: oceanen, continenten, "
                  "rivieren, reliëfeenheden, klimaatzones. \"Kinshasa ligt aan de Kongostroom, in "
                  "Centraal-Afrika, net ten zuiden van de evenaar\" is zo'n zin."),
            ("p", "Het kan ook ten opzichte van <strong>sociaaleconomische elementen</strong>: steden, landen, "
                  "werelddelen, <strong>wereldblokken</strong>, godsdiensten, talen, armoede, analfabetisme. "
                  "\"De grootste haven van de Europese Unie\" situeert met een wereldblok, en dat is iets wat "
                  "mensen gemaakt hebben, niet de natuur."),
            ("p", tabel(["fysischgeografisch", "sociaaleconomisch"],
                        [["oceanen, rivieren, continenten", "steden, landen, wereldblokken"],
                         ["reliëfeenheden en klimaatzones", "godsdiensten en talen"],
                         ["vegetatiezones", "armoede en analfabetisme"]])),
        ]),
        dict(kop="Klimaatzone, vegetatiezone, reliëfeenheid, continent", blokken=[
            ("p", "Van elke plaats moet je kunnen bepalen in welke <strong>klimaatzone</strong>, welke "
                  "<strong>vegetatiezone</strong>, welke <strong>reliëfeenheid</strong> en welk "
                  "<strong>continent</strong> ze ligt. Daarvoor gebruik je telkens een thematische kaart in de "
                  "atlas, geen politieke kaart en geen luchtfoto van één akker."),
            ("p", "De klimaatzone hangt vooral samen met de <strong>breedte</strong>, en daarnaast met hoogte, "
                  "afstand tot de zee en zeestromen. De geografische lengte zegt er niets over: Ierland en "
                  "Labrador liggen ongeveer even ver van de evenaar en hebben toch een heel ander klimaat. Voor "
                  "een klimaatzone kan je ook een <strong>klimatogram</strong> van een weerstation of een "
                  "tabel met maandtemperaturen en neerslag gebruiken."),
            ("p", "De <strong>vegetatiezones</strong>, de zones van de plantengroei, volgen elkaar op van de "
                  "evenaar naar de pool: tropisch "
                  "<strong>regenwoud</strong>, <strong>savanne</strong>, de <strong>woestijn</strong>gordel "
                  "rond de keerkring, dan de gematigde bossen, het <strong>naaldwoud</strong> en ten slotte de "
                  "<strong>toendra</strong>."),
            ("p", "Een <strong>reliëfeenheid</strong> is een gebied dat je aan zijn hoogte en vorm als één "
                  "geheel herkent: een laagvlakte, een plateau, een heuvelland, een gebergte. Je herkent ze aan "
                  "het hoogteverloop, niet aan een landsgrens. \"De fabriek ligt op de Kempense laagvlakte\" "
                  "situeert dus met een reliëfeenheid."),
            ("weetje", "Een <strong>patroon</strong> toont de verspreiding van iets in de ruimte, zoals de "
                       "bevolking van Egypte in een smalle lijn langs de Nijl. Een <strong>proces</strong> gaat "
                       "over verandering, zoals klimaatverandering of bevolkingsevolutie. Die twee woorden "
                       "komen in de hele vakfiche terug."),
        ]),
        dict(kop="Het kaartbeeld", blokken=[
            ("p", "Je kan een bol niet plat maken zonder iets te vervormen. Elke wereldkaart kiest wat ze juist "
                  "houdt en wat ze laat vervormen. Veel kaarten houden de hoeken kloppend en rekken daarvoor de "
                  "gebieden bij de polen uit. Zo'n kaart <strong>vertekent</strong> de oppervlakten dus sterker naar de polen toe. Daardoor "
                  "lijkt Groenland op een gewone schoolwereldkaart ongeveer even groot als Afrika, terwijl "
                  "Afrika in werkelijkheid ongeveer veertien keer zo groot is. Er bestaat dus géén kaart die "
                  "tegelijk vormen, oppervlakten en afstanden helemaal juist weergeeft."),
            ("p", "Ook het midden van de kaart is een keuze. Een bol heeft geen midden: de maker kiest waar hij "
                  "hem opensnijdt. Bij ons staat Europa centraal, in China en Australië hangen andere kaarten "
                  "aan de muur, en die zijn niet minder juist. Staat Amerika centraal, dan lijkt dat werelddeel "
                  "groter en belangrijker, ook al verandert er niets aan zijn oppervlakte of zijn coördinaten. "
                  "Dat het noorden boven staat, is net zo'n gewoonte: een kaart met het zuiden boven klopt even "
                  "goed, ze voelt alleen vreemd."),
            ("p", "Bij <strong>digitale kaarten</strong> stuurt de keuze van de kaartlaag wat je ziet. Op een "
                  "toeristische kaart staat andere informatie dan op een reliëfkaart, en met een wegenkaart "
                  "vind je geen overstromingsgevoelig gebied. Daarom lees je altijd eerst de titel, de "
                  "<strong>legende</strong> en het jaartal, en kijk je wie de kaart gemaakt heeft: die kiest "
                  "het thema, de kleuren en de klassen, en die keuzes sturen mee wat een lezer eruit haalt."),
        ]),
        dict(kop="De mentale kaart en de mentale afstand", blokken=[
            ("p", "Een <strong>mentale kaart</strong> is het beeld dat iemand in zijn hoofd heeft van een "
                  "gebied. Ze staat niet op papier, ze is nooit volledig, en ze verschilt van persoon tot "
                  "persoon. Wat je goed kent staat er scherp op, een streek die je alleen van het nieuws kent "
                  "blijft een vage vlek. Het kaartbeeld dat je vaak ziet, stuurt je mentale kaart mee."),
            ("p", "Mensen denken ook verschillend over een plaats omdat hun context verschilt. Hun "
                  "<strong>persoonlijke context</strong>: voor oudere mensen kan een stadspark vooral een plek "
                  "zijn om tot rust te komen, voor jongeren een plek om te sporten of te skaten. Hun "
                  "<strong>culturele context</strong>: de stad Mekka betekent voor moslims iets heel anders dan "
                  "voor christenen."),
            ("p", "Er zijn drie soorten afstand. De <strong>werkelijke afstand</strong> is meetbaar: Gent en "
                  "Torhout liggen over de weg 55 kilometer uit elkaar. De <strong>ervaren afstand</strong> gaat "
                  "over hoe lang de weg lijkt terwijl je hem aflegt: dezelfde 55 kilometer voelt korter in een "
                  "koele auto over de snelweg dan in een warme auto over kleine wegen. De <strong>mentale "
                  "afstand</strong> gaat over hoe ver je dénkt dat iets ligt, ook als je er nooit geweest bent."),
            ("kader", "Veel Belgen schatten dat Algiers verder van Brussel ligt dan Kreta, terwijl Kreta in "
                      "vogelvlucht bijna 1000 kilometer verder ligt. Wat je beter kent, voelt dichterbij. "
                      "Ervaren en mentale afstand zijn dus niet hetzelfde: de ene gaat over de reis zelf, de "
                      "andere over je inschatting vooraf."),
        ]),
    ],
)

# ───────────────────────── 2. Waar wonen de mensen?
BUNDELS["waar-wonen-de-mensen"] = dict(
    vak=VAK, niveau=BOOST, titel="Waar wonen de mensen?",
    onder="Bevolkingsdichtheid, de factoren die ze sturen, en de ontwikkelingsgraad met de Human Development Index.",
    secties=[
        dict(kop="Bevolkingsdichtheid", blokken=[
            ("p", "De <strong>bevolkingsdichtheid</strong> is het aantal <strong>inwoners per vierkante "
                  "kilometer</strong>. Je berekent ze door het aantal inwoners te delen door de oppervlakte. "
                  "Een land met 12 miljoen inwoners op 30 000 km² heeft dus een dichtheid van 400 inwoners per "
                  "km², ruwweg de orde van grootte van België."),
            ("p", "Omdat het een verhouding is, zegt een groot inwonersaantal op zich niets: Canada telt "
                  "tientallen miljoenen inwoners maar is enorm groot, dus de dichtheid blijft er laag. En een "
                  "hoge dichtheid zegt niets over rijkdom: Monaco en Bangladesh zijn allebei dichtbevolkt en "
                  "verschillen enorm in inkomen."),
            ("kader", "Een dichtheid is een <strong>gemiddelde</strong> over de hele oppervlakte. Twee gebieden "
                      "met dezelfde dichtheid kunnen er heel anders uitzien: in het ene wonen alle mensen in "
                      "drie steden, in het andere wonen ze overal verspreid. Het gemiddelde verbergt dus het "
                      "patroon binnen dat gebied."),
            ("p", "Op een <strong>thematische kaart</strong> van de bevolkingsdichtheid staan donkere en lichte "
                  "kleuren. Lees altijd eerst de <strong>legende</strong>: zonder legende weet je niet of donker "
                  "veel of weinig betekent, en al helemaal niet welke aantallen bij welke klasse horen. "
                  "Kaartmakers kiezen die klassen zelf."),
        ]),
        dict(kop="Wat de dichtheid stuurt", blokken=[
            ("p", "Drie natuurlijke factoren verklaren een groot deel van het wereldwijde patroon: het "
                  "<strong>klimaat</strong>, de <strong>bodemkwaliteit</strong> en het <strong>reliëf</strong>. "
                  "Droogte, een arme bodem en steile hellingen maken landbouw en bouwen moeilijk, dus blijven "
                  "er weinig mensen wonen."),
            ("p", "De Sahara is dunbevolkt omdat er te weinig neerslag valt. Het noorden van Canada is "
                  "dunbevolkt omdat het er lang koud is en de bodem een groot deel van het jaar bevroren "
                  "blijft; water is er genoeg en het reliëf is er zelfs vlak. Reliëf blijft ook vandaag "
                  "meespelen: technisch kan er veel, maar bouwen en wegen aanleggen in de bergen kost veel "
                  "meer, dus liggen de meeste steden in vlakke gebieden en in dalen."),
            ("p", "Bodemkwaliteit telt mee omdat ze bepaalt hoeveel voedsel er lokaal geteeld kan worden. Dat "
                  "verband is losser geworden sinds voedsel over de hele wereld verhandeld wordt, maar het is "
                  "niet verdwenen."),
            ("p", "Waar water, grond en reliëf wél meezitten, wonen veel mensen dicht op elkaar: in "
                  "rivierdalen, in <strong>delta</strong>'s en langs kusten. In een delta zet de rivier haar "
                  "slib af, en die grond is heel vruchtbaar. Dat zie je aan de Ganges, de Nijl, de Rijn en "
                  "langs de Chinese oostkust. In de Nijlvallei drukt de bevolking zich samen op een smalle "
                  "strook, want daarbuiten ligt woestijn."),
            ("weetje", "Klimaat, bodemkwaliteit en reliëf verklaren veel van het wereldwijde "
                       "bevolkingspatroon, maar nooit alles. Geschiedenis, economie en "
                       "politiek bepalen evengoed waar mensen wonen. Wie enkel naar de natuur kijkt, mist de "
                       "helft van het verhaal."),
        ]),
        dict(kop="Ontwikkelingsgraad en de HDI", blokken=[
            ("p", "De <strong>ontwikkelingsgraad</strong> vat samen hoe goed het met de mensen in een land "
                  "gaat. De <strong>Human Development Index</strong> of HDI is de index waarmee de "
                  "<strong>Verenigde Naties</strong> dat in één getal vangen. Hij combineert drie dingen: hoe "
                  "lang mensen er gemiddeld leven, hoeveel jaar ze naar school gaan, en hoeveel een inwoner "
                  "gemiddeld verdient."),
            ("p", "De HDI is een getal tussen 0 en 1. Hoe dichter bij 1, hoe hoger de ontwikkelingsgraad. Omdat "
                  "het een verhoudingsgetal is, kan je er landen van heel verschillende grootte mee "
                  "vergelijken. Land A met 0,92 en land B met 0,48 verschillen dus in gezondheid, onderwijs en "
                  "inkomen samen; over hun inwonersaantal, hun dichtheid of hun bevolkingsgroei zegt dat niets."),
            ("kader", "De HDI is beter dan het inkomen alleen, want een land kan rijk zijn aan olie en toch "
                      "weinig scholen en ziekenhuizen hebben. Maar hij is een <strong>samengesteld</strong> "
                      "getal: twee landen met dezelfde HDI kunnen een andere levensverwachting hebben, want het "
                      "ene scoort hoger op onderwijs en lager op gezondheid dan het andere."),
            ("p", "Waarom hij tussen landen verschilt, heeft nooit één oorzaak. Kolonisatie, oorlog, bestuur, "
                  "schulden, grondstoffen en onderwijsbeleid grijpen in elkaar. Een langdurige oorlog, scholen "
                  "die jarenlang gesloten blijven of een epidemie die de levensverwachting verlaagt, doen de "
                  "HDI dalen. Meer inwoners of een nieuw spoorwegnet doen dat niet."),
            ("p", "Grondstoffen maken een land niet vanzelf welvarend: wat het met zijn inkomsten doet, telt "
                  "evenveel als wat het in de grond heeft. Japan en Zuid-Korea hebben weinig grondstoffen en "
                  "toch een hoge HDI."),
        ]),
        dict(kop="De HDI lezen en nuanceren", blokken=[
            ("p", "Op een wereldkaart van de HDI zie je een duidelijk <strong>patroon</strong>: de hoogste "
                  "waarden liggen samen in bepaalde wereldregio's, vooral West-Europa, Noord-Amerika, Oost-Azië "
                  "en Oceanië, de laagste vooral in Centraal- en West-Afrika. Een kaart maakt van een lijst "
                  "getallen een ruimtelijk beeld, en dan springen die patronen in het oog. Nauwkeuriger worden "
                  "de cijfers er niet van."),
            ("p", "Krijg je een tabel met de levensverwachting, de scholingsduur en het inkomen, dan heb je "
                  "precies de drie bouwstenen van de HDI en kan je de landen op ontwikkelingsgraad "
                  "rangschikken. Krijg je een tabel met inwoners en oppervlakte, dan kan je enkel de dichtheid "
                  "berekenen."),
            ("p", "Twee beperkingen om altijd bij te vermelden. De gewone HDI werkt met <strong>gemiddelden</strong> "
                  "en ziet <strong>ongelijkheid</strong> niet; daarvoor bestaat een aparte versie die voor "
                  "ongelijkheid corrigeert, en die ligt bijna altijd lager. En een nationale HDI verbergt de "
                  "verschillen binnen een land: in veel landen scoort de hoofdstad veel hoger dan het "
                  "platteland. Een lage HDI betekent dus niet dat niemand er rijk is; de ongelijkheid is er "
                  "vaak juist groot."),
            ("p", "De HDI wordt jaarlijks herberekend, dus hij kan stijgen en dalen. Tussen dichtheid en HDI "
                  "bestaat géén vast verband: Nederland is dichtbevolkt met een hoge HDI, Niger is dunbevolkt "
                  "met een lage, en omgekeerd bestaat evengoed. Bij een bron let je op het jaar van de cijfers, "
                  "op wie ze verzameld heeft en op de klassen in de legende: door die anders te kiezen, ziet "
                  "dezelfde kaart er heel anders uit."),
        ]),
    ],
)

# ───────────────────────── 3. Hoe een bevolking verandert
BUNDELS["hoe-een-bevolking-verandert"] = dict(
    vak=VAK, niveau=BOOST, titel="Hoe een bevolking verandert",
    onder="De kengetallen, het leeftijdshistogram, de demografische transitie, en waarom mensen migreren.",
    secties=[
        dict(kop="De kengetallen", blokken=[
            ("p", "Om bevolkingen te vergelijken, werk je met <strong>kengetallen</strong>. Het "
                  "<strong>geboortecijfer</strong> en het <strong>sterftecijfer</strong> zijn het aantal "
                  "geboorten en sterfgevallen <strong>per duizend inwoners per jaar</strong>. Juist doordat het "
                  "verhoudingsgetallen zijn, kan je India met België vergelijken; absolute aantallen zouden "
                  "altijd naar het grootste land wijzen."),
            ("p", "De <strong>natuurlijke aangroei</strong> is het geboortecijfer min het sterftecijfer. Bij "
                  "14 ‰ geboorten en 9 ‰ sterften is dat 5 ‰. Ze kan ook negatief zijn: sterven er meer mensen "
                  "dan er geboren worden, dan krimpt de bevolking, tenzij migratie dat opvangt."),
            ("p", "Het <strong>migratiesaldo</strong> is de <strong>immigratie</strong> min de "
                  "<strong>emigratie</strong>. Emigratie is vertrekken, immigratie is aankomen; dezelfde persoon "
                  "is emigrant in het land dat hij verlaat en immigrant in het land waar hij aankomt. "
                  "Wereldwijd is het migratiesaldo nul, want wie ergens vertrekt, komt elders aan."),
            ("p", "Het <strong>vruchtbaarheidscijfer</strong> is het gemiddeld aantal kinderen per vrouw. Een "
                  "cijfer van 1,4 betekent dus gemiddeld 1,4 kinderen, niet 1,4 per duizend inwoners. Onder "
                  "ongeveer 2,1 krimpt een bevolking op termijn vanzelf, zonder migratie."),
            ("kader", "De <strong>totale groei</strong> van een land is de natuurlijke aangroei plus het "
                      "migratiesaldo. Daarom kan een land met een negatieve natuurlijke aangroei toch groeien: "
                      "in verschillende West-Europese landen komt de groei vandaag bijna helemaal van migratie."),
            ("weetje", "Het ruwe sterftecijfer hangt ook van de leeftijdsstructuur af. Een land met heel veel "
                       "ouderen kan een hóger sterftecijfer hebben dan een land met een jonge bevolking en "
                       "slechtere zorg. Goede gezondheidszorg betekent dus niet automatisch een laag "
                       "sterftecijfer."),
        ]),
        dict(kop="Het leeftijdshistogram", blokken=[
            ("p", "Een <strong>leeftijdshistogram</strong> toont de bevolking per leeftijdsgroep: links de "
                  "mannen, rechts de vrouwen, van jong onderaan naar oud bovenaan, met per balk een aantal of "
                  "een percentage. Meestal gaat het per vijf jaar: met honderd smalle balken zie je alleen "
                  "ruis, met twintig bredere zie je de vorm en dus de structuur. Inkomen en woonplaats staan er "
                  "niet op."),
            ("fig", svg.leeftijdshistogram(), "Drie vormen. De piramide hoort bij een hoog geboortecijfer en "
                                              "een levensverwachting die nog laag ligt; de urn bij een "
                                              "bevolking die vergrijst."),
            ("p", "Een brede basis die snel smal toeloopt, betekent veel kinderen en weinig ouderen. Is het "
                  "histogram bovenaan even breed als in het midden en smaller onderaan, dan <strong>vergrijst</strong> "
                  "de bevolking. Een <strong>inkeping</strong> halverwege wijst vaak op een oorlog of een crisis "
                  "van vroeger: wie toen geboren had moeten worden, ontbreekt, en die deuk schuift zijn hele "
                  "leven mee omhoog. Een land dat jarenlang gezinnen tot één kind beperkte, heeft om dezelfde "
                  "reden smalle balken bij die leeftijdsgroepen."),
            ("p", "Ook migratie verandert de vorm. Wie migreert is vaak jongvolwassen, dus krijgt een land met "
                  "veel immigratie bredere balken rond de twintig tot veertig jaar."),
        ]),
        dict(kop="De demografische transitie", blokken=[
            ("p", "Het model van de <strong>demografische transitie</strong> beschrijft hoe het geboorte- en "
                  "het sterftecijfer van een land in fasen veranderen. Het is een model: echte landen volgen "
                  "het niet perfect, maar het maakt vergelijken mogelijk."),
            ("fig", svg.demografische_transitie(), "Het vlak tussen de twee lijnen is de natuurlijke aangroei. "
                                                   "In fase 2 loopt dat gat het wijdst open."),
            ("p", "In de <strong>eerste fase</strong> zijn beide cijfers hoog en groeit de bevolking "
                  "nauwelijks. In de <strong>tweede fase</strong> daalt het sterftecijfer terwijl het "
                  "geboortecijfer hoog blijft, en groeit de bevolking het snelst: betere voeding, drinkwater "
                  "en gezondheidszorg doen de sterfte snel zakken, terwijl gewoonten rond kinderen krijgen veel "
                  "trager veranderen. In de <strong>derde fase</strong> daalt het geboortecijfer en vertraagt "
                  "de groei. In de <strong>vierde fase</strong> liggen beide cijfers laag."),
            ("p", "Een land met 34 ‰ geboorten en 9 ‰ sterften zit dus waarschijnlijk in fase 2: de sterfte is "
                  "al sterk gedaald, de geboorten nog niet, en de natuurlijke aangroei bedraagt 25 ‰."),
            ("kader", "In fase 1 en fase 4 groeit de bevolking allebei traag, maar de <strong>structuur</strong> "
                      "verschilt volledig: in fase 1 veel kinderen en weinig ouderen, in fase 4 net "
                      "omgekeerd. Kijk dus niet alleen naar de groei, kijk naar het histogram."),
            ("p", "Niet elk land volgt het model op dezelfde manier. Het is een samenvatting van wat in "
                  "West-Europa gebeurde; elders ging de daling van de sterfte veel sneller, of hield beleid of "
                  "oorlog het verloop tegen."),
        ]),
        dict(kop="Demografische processen en migratie", blokken=[
            ("p", "De <strong>demografische processen</strong> uit de fiche zijn bevolkingsevolutie, "
                  "vergrijzing, braindrain, braingain, immigratie, emigratie en de demografische transitie. "
                  "<strong>Vergrijzing</strong> betekent dat het <em>aandeel</em> ouderen toeneemt, niet dat "
                  "het aantal inwoners daalt. Ze komt van een dalend geboortecijfer en een stijgende "
                  "levensverwachting samen, en zet pensioenen, zorg en arbeidsmarkt onder druk terwijl scholen "
                  "juist leeg komen te staan."),
            ("p", "<strong>Braindrain</strong> is het vertrek van hoogopgeleide mensen naar het buitenland; "
                  "voor het ontvangende land heet dat <strong>braingain</strong>. Het land dat de opleiding "
                  "betaalde, verliest net de artsen, ingenieurs en leerkrachten die het nodig heeft. Wat er "
                  "soms tegenover staat, is het geld dat migranten naar huis sturen."),
            ("p", "De <strong>beïnvloedende factoren</strong> uit de fiche zijn het klimaat en de "
                  "klimaatverandering, het reliëf, de bodemkwaliteit, de politieke situatie, de oorlogssituatie, "
                  "het geboortebeleid, de welvaart en het welzijn, en armoede. Een geboortecijfer blijft laag "
                  "wanneer vrouwen lang naar school gaan en werken, wanneer beleid grote gezinnen ontmoedigt, en "
                  "wanneer huisvesting en kinderopvang duur zijn. Hoge kindersterfte en een landbouweconomie "
                  "duwen het juist omhoog: dan zijn kinderen handen op het veld en een zekerheid voor later."),
            ("p", "Mensen migreren om <strong>pushfactoren</strong> en <strong>pullfactoren</strong>. Push duwt "
                  "je weg: oorlog, armoede, droogte, werkloosheid, vervolging. Pull trekt je aan: werk, "
                  "veiligheid, onderwijs, familie die er al woont. De meeste mensen die migreren blijven binnen "
                  "hun eigen wereldregio: de reis is korter, de taal vaak dichterbij, en er wonen al bekenden."),
            ("weetje", "Klimaat is ook een pushfactor, maar wie door droogte of overstroming wegtrekt, steekt "
                       "zelden meteen een oceaan over. De meeste mensen verhuizen eerst binnen hun eigen land, "
                       "vaak van het platteland naar de stad. Een verre reis kost geld dat ze net niet hebben."),
            ("p", "Een land met een negatief migratiesaldo en veel vertrek van jonge, opgeleide mensen "
                  "veroudert dus én verliest kennis. De achterblijvende bevolking wordt gemiddeld ouder, en "
                  "het land mist net de mensen die het nodig heeft."),
        ]),
    ],
)

# ───────────────────────── 4. Stad en platteland
BUNDELS["stad-en-platteland"] = dict(
    vak=VAK, niveau=BOOST, titel="Stad en platteland",
    onder="Waarom mensen wonen waar ze wonen, de hiërarchie van steden, en hoe verstedelijking het landschap verandert.",
    secties=[
        dict(kop="Waarom in de stad, waarom op het platteland", blokken=[
            ("p", "Een stad bundelt werk, scholen, ziekenhuizen, winkels en cultuur op korte afstand. Dat is "
                  "haar grootste aantrekkingskracht. Het <strong>platteland</strong> heeft andere troeven: meer "
                  "ruimte voor hetzelfde geld, meer rust en minder lawaai, meer groen in de omgeving."),
            ("p", "De <strong>beïnvloedende factoren</strong> uit de fiche zijn het klimaat en de "
                  "klimaatverandering, het reliëf, de bodemkwaliteit, de politieke situatie, de "
                  "oorlogssituatie, de welvaart en het welzijn, en armoede. Armoede werkt trouwens in twee "
                  "richtingen: in de stad is er meer kans op werk, maar het wonen is er duurder, en daarom "
                  "komen armere gezinnen vaak in de goedkoopste, oudste wijken van de stad terecht."),
            ("p", "<strong>Stadsvlucht</strong> is het vertrek van stadsbewoners naar de rand en het "
                  "platteland, voor een tuin en een rustiger straat. Wie zo verhuist en in de stad blijft "
                  "werken, gaat <strong>pendelen</strong> en legt meer kilometers af dan wie in de stad zelf "
                  "woont. In veel landen met een lagere ontwikkelingsgraad gaat de beweging net de andere kant "
                  "op: daar trekken mensen van het platteland naar de stad, want werk, onderwijs en zorg zitten "
                  "daar. Groeit die stad sneller dan haar woningen en riolering, dan ontstaan er sloppenwijken "
                  "aan de rand."),
            ("p", "Reliëf blijft meespelen: bouwen en wegen aanleggen is in vlak gebied goedkoper, dus groeien "
                  "steden het snelst in dalen en vlaktes."),
        ]),
        dict(kop="De hiërarchie van steden", blokken=[
            ("p", "Steden verschillen in <strong>hiërarchie</strong>, en die hangt niet af van hun oppervlakte "
                  "of hun ouderdom maar van hun <strong>belang</strong>. Die rangorde tussen steden noem je met "
                  "één woord de <strong>stedenhiërarchie</strong>. De fiche onderscheidt drie soorten "
                  "criteria."),
            ("p", tabel(["economisch", "cultureel", "politiek"],
                        [["handelszaken en beurzen", "scholen en universiteiten", "hoofdsteden"],
                         ["hoofdkwartieren van grote ondernemingen", "grote musea en theaters", "hoofdkwartieren van regeringen"],
                         ["internationale banken", "recreatie en onderzoeksinstellingen", ""]])),
            ("p", "Een kleinere stad met een regeringszetel of een wereldhaven kan dus hoger staan dan een "
                  "grotere stad zonder die functies. Brussel staat hoog in de Europese stedenhiërarchie door de "
                  "Europese instellingen en de NAVO, niet door zijn inwonersaantal. En de grootste stad van een "
                  "land is lang niet altijd de hoofdstad: New York is veel groter dan Washington, Sydney groter "
                  "dan Canberra."),
            ("weetje", "Een stad kan tegelijk hoog scoren op de drie criteria. Parijs, Londen en Tokio doen "
                       "dat, en juist die stapeling maakt van een stad een wereldstad."),
        ]),
        dict(kop="Wat er in de stad verandert", blokken=[
            ("p", "<strong>Sociale segregatie</strong> is ruimtelijke scheiding: bevolkingsgroepen wonen in "
                  "gescheiden wijken. In West-Europese steden is de belangrijkste motor daarvan het verschil in "
                  "<strong>woningprijs</strong>. Wie weinig kan betalen, belandt in de goedkoopste woningen, en "
                  "die liggen bij elkaar. Zo ontstaat scheiding zonder dat iemand ze oplegt."),
            ("p", "<strong>Multiculturaliteit</strong> is iets anders: dat mensen met verschillende "
                  "achtergronden en tradities in dezelfde stad samenleven. Je ziet het aan de winkels, de "
                  "gebedshuizen, de talen op straat en het aanbod op de markt. Een stad kan heel divers zijn en "
                  "tegelijk sterk gescheiden, of net niet. Het straatbeeld van zo'n wijk is trouwens zelf een "
                  "bron: opschriften, winkels en marktkramen vertellen wie er woont en hoe dat veranderd is, en "
                  "dat aflezen op het terrein heet <strong>terreinkartering</strong>."),
            ("p", "Een <strong>functiewijziging</strong> is een gebouw dat blijft staan maar anders gebruikt "
                  "wordt: een oude textielfabriek die appartementen wordt, een kerk die een bibliotheek wordt, "
                  "een kantoor dat woningen wordt. Dat gebeurt dus niet alleen bij fabrieken. Een stad die "
                  "inwoners verliest, verliest daarom nog niet haar economische functie: woonfunctie en "
                  "economische functie kunnen apart van elkaar bewegen."),
        ]),
        dict(kop="Vijf veranderingen in het landschap", blokken=[
            ("p", "De fiche noemt vijf landschapsveranderingen. De eerste is de <strong>verstedelijking van "
                  "het platteland</strong>: nieuwe verkavelingen rond de dorpskern, winkelcentra en bedrijven "
                  "langs de invalswegen, bebouwing op wat vroeger akkerland was. Verstedelijking is dus meer "
                  "dan steden die inwoners krijgen. Een dorp dat er drie verkavelingen bij krijgt zonder één "
                  "nieuwe winkel, wordt een woondorp waar men voor alles wegrijdt."),
            ("p", "De tweede is de <strong>ontvolking van het platteland</strong>, vooral in afgelegen streken "
                  "zonder werk of voorzieningen. Jongeren trekken weg voor studie en werk, de school en de "
                  "bakker sluiten, en dat maakt blijven nog moeilijker. In delen van Spanje en Zuid-Italië "
                  "staan zo hele dorpen leeg."),
            ("p", "De derde is <strong>inbreiding en groei van de steden</strong>. Inbreiding is bouwen op "
                  "open plekken en oude bedrijfsterreinen <em>binnen</em> de bestaande stad; uitbreiding is "
                  "bouwen op akkerland aan de rand. Veel steden kiezen voor inbreiding omdat open ruimte in "
                  "Vlaanderen schaars is en omdat de voorzieningen zo dicht bij de mensen blijven, wat "
                  "autokilometers scheelt."),
            ("p", "De vierde is de <strong>veranderende mobiliteit</strong>. Een nieuwe ring, een fietssnelweg "
                  "of een gesloten spoorlijn herschikt waar mensen wonen en werken: wat goed bereikbaar wordt, "
                  "wordt bebouwd, wat afgesneden raakt, loopt leeg. Een bedrijf dat voor een terrein bij een "
                  "snelwegafrit kiest, doet dat omdat de grond er goedkoper is en vrachtwagens er vlot "
                  "geraken, en daardoor trekt werk uit de stad weg."),
            ("p", "De vijfde is <strong>stadslandbouw</strong>: voedsel telen in of vlak bij de stad zelf, in "
                  "volkstuinen, daktuinen of serres op oude bedrijventerreinen. Dat scheelt transport, maakt de "
                  "stad groener en brengt buurtbewoners samen. Een stad helemaal voeden lukt er niet mee."),
            ("kader", "Leegstand in een winkelstraat heeft meestal drie oorzaken tegelijk: winkelcentra aan de "
                      "rand die klanten wegtrekken, mensen die online kopen, en een straat die met de auto "
                      "moeilijk bereikbaar geworden is."),
        ]),
        dict(kop="Verstedelijking en het leefmilieu", blokken=[
            ("p", "<strong>Versnippering</strong> is het opdelen van de open ruimte in kleine, van elkaar "
                  "gescheiden stukken door wegen en bebouwing. Kleine losse stukken natuur werken veel minder "
                  "goed dan één groot aaneengesloten gebied."),
            ("p", "<strong>Verharding</strong> is beton en asfalt dat geen water doorlaat. Regenwater loopt "
                  "dan snel weg naar de riool in plaats van in de bodem te dringen: het grondwater vult niet "
                  "aan, en bij hevige regen loopt het riool over. Steen en asfalt slaan bovendien warmte op en "
                  "geven ze 's nachts weer af, terwijl er weinig groen is dat verkoelt. Daardoor is het in een "
                  "stad meetbaar warmer dan op het platteland eromheen: het <strong>hitte-eilandeffect</strong>, "
                  "dat tijdens een hittegolf tot enkele graden kan oplopen."),
            ("p", "Een gemeente die een betonnen plein openbreekt en er bomen plant, pakt precies die twee "
                  "problemen aan: meer schaduw en verdamping tegen de hitte, en water dat weer in de bodem "
                  "trekt. Aan segregatie of aan de hiërarchie van de stad verandert zo'n plein niets."),
            ("p", "Wil je onderzoeken of een gemeente verstedelijkt, dan leg je luchtfoto's van vroeger en nu "
                  "naast elkaar, kijk je naar de inwonerscijfers per jaar en naar kaarten van het bodemgebruik "
                  "door de jaren heen. Verstedelijking lees je af aan bebouwing en verharding die toenemen ten "
                  "koste van akkers en weiden. Let er wel op dat beide beelden in hetzelfde seizoen en op "
                  "dezelfde schaal genomen zijn."),
        ]),
    ],
)

# ───────────────────────── 5. Grondstoffen, energie en industrie
BUNDELS["grondstoffen-energie-en-industrie"] = dict(
    vak=VAK, niveau=BOOST, titel="Grondstoffen, energie en industrie",
    onder="Waar en hoe grondstoffen en energie gewonnen worden, en welke factoren bepalen waar de industrie staat.",
    secties=[
        dict(kop="Ontginning", blokken=[
            ("p", "Grondstoffen worden gewonnen in een <strong>groeve</strong> of in een <strong>mijn</strong>. "
                  "In een groeve of <strong>dagbouw</strong> graaft men van bovenaf, in open lucht. Zit de laag "
                  "te diep, dan moet men schachten en gangen maken, en dan spreekt men van een mijn. Dagbouw is "
                  "goedkoper en veiliger, dus kiest men ervoor waar het kan; voor het landschap is dagbouw juist "
                  "ingrijpender, want er verdwijnt een hele laag grond."),
            ("p", "Er is ook een verschil tussen <strong>traditionele</strong> en <strong>moderne</strong> "
                  "ontginning. Bij traditionele ontginning graven mensen met eenvoudig gereedschap, soms in "
                  "gevaarlijke omstandigheden. Moderne ontginning draait op zware machines en levert veel meer "
                  "per werkende op."),
            ("p", "Waar iets ontgonnen wordt, hangt in de eerste plaats af van waar het in de bodem zit: zonder "
                  "voorraad geen ontginning. Maar een grondstof wordt niet ontgonnen zodra men weet dat ze er "
                  "ligt. Pas als de opbrengst hoger is dan de kosten van winnen en vervoeren, begint men eraan. "
                  "Stijgt de wereldprijs, dan wordt een voorraad die jaren bleef liggen plots wel interessant. "
                  "Dat is precies wat er nu met <strong>lithium, kobalt en nikkel</strong> gebeurt: de wereld "
                  "schakelt over op elektriciteit, dus stijgt de vraag naar die zeldzame metalen voor "
                  "batterijen, en dus ook de druk op de gebieden waar ze zitten. Veruit het meeste "
                  "<strong>kobalt</strong> komt uit de Democratische Republiek Congo, wat de "
                  "ontginningsomstandigheden daar tot een politieke kwestie maakt."),
            ("p", "De oude steenkoolmijnen van de <strong>Kempen</strong> lagen daar om dezelfde reden: men "
                  "had er de steenkoollaag in de ondergrond gevonden. Ontginning volgt de voorraad, niet de "
                  "bevolking en niet de grens."),
            ("kader", "<strong>Recyclage</strong> is ook een bron van grondstoffen. Uit oud schroot, gebruikte "
                      "batterijen en elektronica komen metalen terug. Dat vraagt veel minder energie dan nieuw "
                      "erts, er hoeft geen mijn of groeve voor open, en het maakt een land minder afhankelijk "
                      "van invoer. Gerecycleerd metaal is wel meestal iets minder zuiver, en vervoerd moet het "
                      "nog altijd worden."),
            ("weetje", "Een land met grote grondstofvoorraden is daardoor nog niet welvarend. Gaat de winst "
                       "naar buitenlandse bedrijven of naar een kleine elite, dan merkt de bevolking er weinig "
                       "van. Men spreekt dan van de grondstoffenvloek."),
        ]),
        dict(kop="Energiebronnen", blokken=[
            ("p", "<strong>Hernieuwbare</strong> energiebronnen komen elke dag terug: wind, zon, waterkracht, "
                  "biomassa, aardwarmte. <strong>Niet-hernieuwbare</strong> bronnen zitten in eindige "
                  "voorraden in de bodem: aardolie, steenkool, aardgas en het uranium voor kernenergie."),
            ("p", "Kernenergie stoot bij de productie zelf nauwelijks CO₂ uit, maar dat maakt haar niet "
                  "hernieuwbaar: uranium moet ontgonnen worden en raakt op, en er blijft radioactief afval "
                  "over. Hernieuwbaar gaat over de <em>bron</em>, niet over de uitstoot."),
            ("p", "Waar energie geproduceerd wordt, hangt af van waar de bron zit. Windmolenparken staan in "
                  "België vooral op de Noordzee en in open landschap, want daar waait het harder en "
                  "constanter, zonder gebouwen of bossen die de wind afremmen. Zonneparken liggen waar veel "
                  "zonuren zijn, zoals Spanje, Noord-Afrika of het zuidwesten van de Verenigde Staten: dezelfde "
                  "investering levert er meer stroom op. <strong>Waterkrachtcentrales</strong> hebben "
                  "hoogteverschil en een constante watertoevoer nodig, dus liggen ze in bergachtige streken met "
                  "veel neerslag of smeltwater."),
            ("p", "Klimaatverandering grijpt daar meteen op in. Krimpen de gletsjers en valt er in de zomer "
                  "minder neerslag, dan staat er minder water in het stuwmeer, en verschillende Alpenlanden "
                  "merken dat al in hun jaarcijfers."),
        ]),
        dict(kop="Industrie: traditioneel en modern", blokken=[
            ("p", "<strong>Traditionele</strong> of zware industrie lag vroeger vlak bij de steenkoolmijnen, "
                  "want steenkool was zwaar en duur om te vervoeren en men had er veel van nodig voor één ton "
                  "staal. Zo groeiden staal en glas langs de Samber en de Maas."),
            ("p", "<strong>Moderne</strong> industrie kiest haar plaats veel vrijer, want haar grondstoffen "
                  "wegen minder. Chips, medicijnen en software hangen niet aan een kolenlaag vast; ze zoeken "
                  "kennis, goede verbindingen en personeel. Goede transportverbindingen blijven ze wél nodig "
                  "hebben: luchthavens, autosnelwegen en snelle datakabels zijn voor moderne bedrijven juist "
                  "doorslaggevend."),
            ("p", "De <strong>afzetmarkt</strong> is de plaats waar een product verkocht wordt. Die kan ver "
                  "van de productie liggen, en juist dat verschil maakt de wereldhandel en de rol van havens "
                  "zo groot. Het grootste deel van de wereldhandel gaat over zee, dus is een haven de poort "
                  "waardoor grondstoffen binnenkomen en afgewerkte producten vertrekken. Daarom liggen de grote "
                  "chemische bedrijven van ons land in en rond de haven van Antwerpen."),
            ("p", "Hoe zwaar de nabijheid van de klanten weegt, hangt van het product af. Bij zware of "
                  "bederfelijke producten weegt ze zwaar: een betoncentrale of een bakkerij levert dicht bij "
                  "huis. Bij lichte, dure producten weegt ze bijna niet. Een kledingfabrikant die in een land "
                  "met lage lonen laat naaien en in Europa verkoopt, heeft productie en afzetmarkt zelfs op "
                  "verschillende continenten liggen."),
            ("p", "Op een kaart herken je zware industrie aan grote bedrijventerreinen bij een haven, een "
                  "spoorbundel of een kanaal: ze vraagt ruimte en vervoer over water of spoor. Nieuwe "
                  "bedrijventerreinen zoeken vandaag vooral goedkope grond met een goede aansluiting op het "
                  "wegennet, en dus liggen ze bij snelwegafritten buiten de stad."),
        ]),
        dict(kop="De factoren achter het industriële proces", blokken=[
            ("p", "De fiche deelt de factoren in drie groepen in. De <strong>geopolitieke</strong> factoren "
                  "zijn de staatsvorm, de stabiliteit en de samenwerkingsverbanden. Die bepalen of een bedrijf "
                  "er durft te investeren en of het vlot kan uitvoeren: een land dat lid is van een groot "
                  "handelsblok voert makkelijker uit naar de andere leden, want invoerrechten en veel controles "
                  "vallen weg. Raakt een land in oorlog, dan valt ook de ontginning terug, want investeerders "
                  "en werknemers vertrekken en de havens en pijpleidingen werken niet meer."),
            ("p", "De <strong>fysische</strong> factoren zijn het klimaat en de klimaatverandering, het "
                  "reliëf en de grondstoffen. De <strong>sociaaleconomische</strong> factoren zijn de Human "
                  "Development Index, de verloning, vraag en aanbod, en de afzetmarkt."),
            ("p", tabel(["geopolitiek", "fysisch", "sociaaleconomisch"],
                        [["staatsvorm", "klimaat en klimaatverandering", "Human Development Index"],
                         ["stabiliteit", "reliëf", "verloning"],
                         ["samenwerkingsverbanden", "grondstoffen", "vraag en aanbod, afzetmarkt"]])),
            ("p", "Bedrijven verplaatsen productie naar het buitenland omdat lonen, belastingen en regels daar "
                  "vaak lager liggen. Lagere lonen zijn wel niet de <em>enige</em> reden: ook de nabijheid van "
                  "de afzetmarkt, de milieuregels en de beschikbaarheid van geschoold personeel wegen mee. Dat "
                  "verplaatsen van werk naar een bedrijf in een ander land heet <strong>outsourcing</strong> of "
                  "uitbesteding."),
        ]),
        dict(kop="Wat ervan overblijft in de ruimte", blokken=[
            ("p", "Ontginning laat sporen na: het landschap verandert blijvend van vorm, er komen wegen en "
                  "spoorlijnen naartoe, en er ontstaan nederzettingen voor de werkers. Een mijn of groeve "
                  "trekt dus infrastructuur en mensen aan, en laat achteraf een put of een terril na."),
            ("p", "<strong>Industrialisatie</strong> brengt fabrieksactiviteit, werk en ruimtebeslag. "
                  "<strong>De-industrialisatie</strong> is het omgekeerde: fabrieken sluiten of verhuizen, en "
                  "de streek verliest werk en inkomen. Wallonië en Noord-Frankrijk maakten dat mee na de "
                  "sluiting van de mijnen en de staalbedrijven. Werkloosheid stijgt, jongeren trekken weg, en "
                  "er komt een groot terrein leeg te staan."),
            ("p", "<strong>Reconversie</strong> is de derde stap: het oude terrein krijgt een nieuwe functie, "
                  "als wetenschapspark, woonwijk, museum of natuurgebied. Thor Park in Genk, op de oude mijnsite "
                  "van Waterschei, is daar een voorbeeld van: eerst verdween de industrie, daarna kreeg het "
                  "terrein een nieuwe bestemming."),
        ]),
    ],
)

# ───────────────────────── 6. Landbouw, handel en toerisme
BUNDELS["landbouw-handel-en-toerisme"] = dict(
    vak=VAK, niveau=BOOST, titel="Landbouw, handel en toerisme",
    onder="Landbouwsystemen en productiewijzen, de gevolgen voor de bodem, en waar handel, diensten en toerisme voorkomen.",
    secties=[
        dict(kop="Landbouwsystemen", blokken=[
            ("p", "De grote <strong>landbouwsystemen</strong> zijn <strong>akkerbouw</strong> (gewassen telen), "
                  "<strong>veeteelt</strong> (dieren houden) en <strong>tuinbouw</strong> (groenten, fruit en "
                  "sierteelt, vaak in serres). Veel bedrijven combineren ze: het graan van de akker voedt het "
                  "vee in de stal."),
            ("p", "<strong>Extensieve</strong> landbouw spreidt weinig arbeid en middelen over veel grond, "
                  "zoals schapenteelt in de Australische binnenlanden. <strong>Intensieve</strong> landbouw "
                  "concentreert veel arbeid, bemesting, water en technologie op weinig grond, zoals de serres "
                  "van het Westland. Intensief haalt daardoor per hectare meer op. Per werkende ligt het "
                  "anders: traditionele landbouw levert per werkende minder op dan moderne, maar per hectare "
                  "kunnen rijstterrassen die met de hand bewerkt worden juist een heel hoge opbrengst halen."),
            ("kader", "Let goed op het verschil tussen <em>per hectare</em> en <em>per werkende</em>. Een "
                      "bedrijf kan op de ene maat hoog scoren en op de andere laag, en veel examenvragen "
                      "draaien precies om dat onderscheid."),
        ]),
        dict(kop="Waar wat geteeld wordt", blokken=[
            ("p", "Wat waar groeit, volgt het klimaat en de bodem. <strong>Rijst</strong> heeft warmte en veel "
                  "water nodig, en de moesson levert dat: daarom wordt ze vooral in Zuid- en Oost-Azië geteeld, "
                  "op terrassen in de heuvels en in de vlaktes van de grote rivieren."),
            ("p", "Rond de Middellandse Zee, met een droge warme zomer en een zachte natte winter, horen "
                  "<strong>olijven</strong>, <strong>wijndruiven</strong> en <strong>citrusvruchten</strong> "
                  "thuis. <strong>Cacao</strong> groeit in het warme laagland van de tropen, vooral in "
                  "West-Afrika. <strong>Koffie</strong> komt ook uit de tropen, maar juist van de hooglanden: "
                  "daar is het koeler en groeit de boon trager, wat de smaak ten goede komt. Je vindt ze onder "
                  "meer in Brazilië, Vietnam, Colombia en Ethiopië."),
            ("p", "De <strong>zwarte aarde</strong> van Oekraïne is dik en rijk aan humus en houdt water goed "
                  "vast. Samen met het vlakke reliëf maakt dat van die streek een van de graanschuren van de "
                  "wereld, wat meteen ook een geopolitieke inzet is."),
            ("p", "De <strong>afzetmarkt</strong> stuurt mee wat er geteeld wordt: een boer die voor de "
                  "wereldmarkt teelt in plaats van voor eigen gebruik, kiest een ander gewas. Wat de wereldmarkt "
                  "vraagt, is niet altijd wat de streek zelf eet."),
        ]),
        dict(kop="Duurzaam of niet", blokken=[
            ("p", "Bij de landbouw noemt de fiche bij de fysische factoren uitdrukkelijk ook de "
                  "<strong>bodemkwaliteit en de ondergrond</strong>, naast klimaat en reliëf. De geopolitieke "
                  "en sociaaleconomische factoren zijn dezelfde als bij de industrie. Politieke stabiliteit "
                  "telt zwaar: oorlog legt velden braak, vernielt opslag en verstoort de handel, en daarom "
                  "leidt een conflict in een graanland tot hogere voedselprijzen ver daarbuiten."),
            ("p", "<strong>Schaalvergroting</strong> betekent minder bedrijven die elk meer grond bewerken. "
                  "Grote machines en grote percelen verlagen de kostprijs, maar percelen worden groter en "
                  "rechter, hagen en houtkanten verdwijnen, en wegen en sloten worden rechtgetrokken. Zonder "
                  "hagen en houtkanten krijgt de wind meer vat op de grond."),
            ("p", "<strong>Bodemerosie</strong> treedt sneller op wanneer een helling na de oogst kaal blijft "
                  "liggen: de regen spoelt de vruchtbare bovenlaag weg. Daarom zaait men een groenbedekker in "
                  "of ploegt men dwars op de helling. <strong>Bodemdegradatie</strong> is de bredere "
                  "achteruitgang van de bodemkwaliteit: verzilting, uitputting, verdichting, verlies van "
                  "organische stof. Eén centimeter vruchtbare bovengrond opbouwen vraagt honderden jaren, dus "
                  "telt bodem als een voorraad, niet als iets hernieuwbaars."),
            ("p", "<strong>Ontbossing</strong> is het kappen van bos om er landbouwgrond of weiland van te "
                  "maken. Voor soja, palmolie en vee is dat een van de grootste oorzaken van bosverlies "
                  "wereldwijd; het kost biodiversiteit en laat koolstof vrij die in het bos opgeslagen zat."),
            ("p", "Een duurzamer bedrijf houdt hagen, bomen en bufferstroken op zijn land, wisselt zijn "
                  "gewassen af over de jaren, en bemest en beregent niet meer dan de teelt opneemt. Veel "
                  "kunstmest en bestrijdingsmiddelen gebruiken is dus niet hetzelfde als duurzaam werken: te "
                  "veel mest belandt in het grond- en oppervlaktewater, en bestrijdingsmiddelen raken ook "
                  "insecten die je net nodig hebt."),
            ("weetje", "Klimaatverandering kan ervoor zorgen dat een gewas op een plaats niet meer rendeert. "
                       "Langere droogtes, andere neerslagpatronen en nieuwe ziekten verschuiven de gebieden "
                       "waar een teelt lukt, en koffieboeren trekken daarom op sommige plaatsen hoger de berg "
                       "op."),
        ]),
        dict(kop="Handel en diensten", blokken=[
            ("p", "De <strong>dienstensector</strong> is werk waarbij men geen goederen maakt maar diensten "
                  "levert: onderwijs, zorg, handel, transport, bankwezen, toerisme. In landen met een hoge "
                  "ontwikkelingsgraad werkt het grootste deel van de mensen daarin. Landbouw is de eerste "
                  "sector, industrie de tweede, diensten de derde."),
            ("p", "Bij de handel onderscheidt men de <strong>groothandel</strong>, die in grote hoeveelheden "
                  "aan bedrijven en winkels levert, en de <strong>kleinhandel</strong> of detailhandel, die "
                  "rechtstreeks aan de consument verkoopt."),
            ("p", "Online winkelen verandert waar de gebouwen staan. Grote magazijnen en distributiecentra "
                  "zoeken een plaats bij een snelwegknooppunt of een haven, met veel oppervlakte en veel "
                  "vrachtverkeer: in een stadscentrum is dat onbetaalbaar en onmogelijk. Zo verschuift werk van "
                  "de winkelstraat naar de rand van het land. Handel en diensten hebben dus wel degelijk "
                  "invloed op het landschap: winkelcentra, kantoorparken, magazijnen, hotels en wegen nemen "
                  "ruimte in."),
            ("p", "Toont een bron dat een land vooral grondstoffen uitvoert en afgewerkte producten invoert, "
                  "dan gebeuren de bewerking en de winst grotendeels elders. Dat patroon speelt in veel "
                  "discussies over ontwikkeling een rol. Onderzoek je de afzetmarkt van een product, dan is de "
                  "vraag altijd: waar wordt het gekocht, en door wie?"),
        ]),
        dict(kop="Toerisme", blokken=[
            ("p", "Waar toerisme voorkomt, hangt af van klimaat, landschap, erfgoed en veiligheid samen. De "
                  "<strong>fysische</strong> troeven zijn een klimaat met veel zonuren, een kust met stranden "
                  "en een reliëf met bergen voor wintersport. <strong>Wintersporttoerisme</strong> ligt in "
                  "hooggebergte omdat daar lang "
                  "genoeg sneeuw blijft liggen om een seizoen te draaien; door de klimaatverandering schuift de "
                  "betrouwbare sneeuwgrens jaar na jaar hoger, en lager gelegen skigebieden halen steeds "
                  "moeilijker een volledig seizoen."),
            ("p", "De <strong>geopolitieke</strong> factoren zijn de stabiliteit, de staatsvorm en de "
                  "samenwerkingsverbanden: die bepalen of mensen er veilig en zonder visum geraken. Politieke "
                  "onrust doet het aantal toeristen meestal binnen de week dalen, en het herstel duurt jaren. "
                  "De <strong>sociaaleconomische</strong> factor is de Human Development Index: zorg, "
                  "veiligheid, water, wegen en opgeleid personeel maken een bestemming bruikbaar."),
            ("p", "Erfgoed is een eigen troef. Brugge, Praag en Rome draaien op hun geschiedenis en hun "
                  "stadsbeeld, zonder strand in de buurt. Bereikbaarheid beslist mee: eilanden zoals de "
                  "Canarische Eilanden en de Malediven draaien bijna volledig op hun luchtverbinding."),
            ("p", "<strong>Massatoerisme</strong> laat sporen na in de ruimte: bebouwing die de duinen en de "
                  "open ruimte opslorpt, druk op het drinkwater in het hoogseizoen, en woningen die voor de "
                  "eigen bewoners onbetaalbaar worden. En een streek die bijna volledig op toerisme draait, is "
                  "kwetsbaar: een epidemie, een aanslag of een crisis in de herkomstlanden doet het inkomen van "
                  "een hele streek ineens wegvallen."),
        ]),
    ],
)

# ───────────────────────── 7. Mondialisering
BUNDELS["mondialisering"] = dict(
    vak=VAK, niveau=BOOST, titel="Mondialisering",
    onder="Wat mondialisering is, waar ze vandaan komt, en welke gevolgen ze heeft voor landen en mensen.",
    secties=[
        dict(kop="Wat mondialisering is", blokken=[
            ("p", "<strong>Mondialisering</strong> betekent dat landen en mensen wereldwijd steeds meer met "
                  "elkaar verweven raken. Handel, geld, mensen, ideeën en informatie bewegen sneller en verder "
                  "dan ooit, en wat aan de ene kant van de wereld gebeurt, wordt aan de andere kant voelbaar. "
                  "Men noemt de wereld daarom soms een dorp: de werkelijke afstand bleef gelijk, maar de "
                  "ervaren afstand werd veel kleiner."),
            ("p", "Ze komt in vier vormen voor. <strong>Economische</strong> mondialisering is een gsm met "
                  "metalen uit Congo, ontworpen in de Verenigde Staten en gemonteerd in Azië: de productieketen "
                  "ligt over verschillende continenten verspreid. <strong>Culturele</strong> mondialisering is "
                  "dat jongeren over de hele wereld dezelfde muziek, series en mode volgen. "
                  "<strong>Politieke</strong> mondialisering is dat landen samen afspraken maken over "
                  "grensoverschrijdende problemen. <strong>Sociale</strong> mondialisering is dat mensen "
                  "wereldwijd contact houden met familie in andere landen."),
            ("weetje", "Mondialisering speelt zich niet alleen af tussen bedrijven en overheden. Wie vrienden "
                       "heeft in een ander land, online kleren bestelt of naar een buitenlandse serie kijkt, "
                       "doet eraan mee. Dat is precies de sociale en culturele kant ervan."),
        ]),
        dict(kop="Waarom ze versnelde", blokken=[
            ("p", "Drie dingen versnelden haar samen: goedkoper en sneller <strong>transport</strong> over zee "
                  "en door de lucht, het <strong>internet</strong> met goedkope wereldwijde communicatie, en "
                  "<strong>handelsakkoorden</strong> die invoerrechten verlagen. Strengere grenscontroles en "
                  "hogere invoerrechten werken juist de andere kant op."),
            ("p", "De <strong>container</strong> is daarbij een stille maar krachtige motor. Voordien werd elk "
                  "stuk vracht apart geladen; met gestandaardiseerde containers duurt het laden van een schip "
                  "uren in plaats van dagen, en dat maakte het <strong>zeetransport</strong> veel goedkoper. Altijd dezelfde afmetingen, "
                  "overal dezelfde kranen: dat is de hele truc."),
            ("p", "Een zeehaven is daardoor een <strong>knooppunt</strong> waar de wereldstromen samenkomen. "
                  "Het grootste deel van de wereldhandel gaat over zee, dus is een haven als Rotterdam of "
                  "Antwerpen een plaats waar de wereldeconomie letterlijk aanlandt."),
        ]),
        dict(kop="Productie en consumptie", blokken=[
            ("p", "Voor wat wij <strong>consumeren</strong> betekent het dat we producten uit de hele wereld "
                  "kopen, het hele jaar door. Aardbeien in december en avocado's uit Peru zijn gewoon geworden. "
                  "De keerzijde is het transport dat daarvoor nodig is en de druk op het land waar die teelt "
                  "gebeurt."),
            ("p", "Bedrijven laten hun productie vaak in andere landen uitvoeren omdat lonen, belastingen en "
                  "regels daar lager liggen. Zo'n lange internationale keten heeft drie echte nadelen: ze is "
                  "<strong>kwetsbaar</strong> als er ergens een schakel wegvalt, ze veroorzaakt veel transport "
                  "en dus uitstoot, en ze maakt het moeilijk te controleren hoe er gewerkt wordt. Goedkoper en "
                  "gevarieerder worden de producten er juist van."),
            ("kader", "Valt er in één land productie stil, dan kunnen winkels aan de andere kant van de wereld "
                      "leeg komen te staan. Tijdens de coronacrisis en na de blokkade van het Suezkanaal in "
                      "2021 zag je dat effect wereldwijd. Mondialisering maakt landen dus niet minder maar "
                      "juist véél meer afhankelijk van elkaar."),
        ]),
        dict(kop="Samenwerkingsverbanden", blokken=[
            ("p", "De fiche noemt zes samenwerkingsverbanden. De <strong>Europese Unie</strong> is een "
                  "samenwerkingsverband van Europese landen met een gemeenschappelijke markt, gezamenlijke "
                  "regels en voor een deel een gezamenlijke munt. De <strong>Verenigde Naties</strong> werden "
                  "na de Tweede Wereldoorlog opgericht om oorlog te voorkomen en verenigen bijna alle landen "
                  "ter wereld; daarnaast werken ze rond ontwikkeling, gezondheid, vluchtelingen en klimaat."),
            ("p", "De <strong>NAVO</strong> is in de eerste plaats een militair bondgenootschap: landen in "
                  "Europa en Noord-Amerika beloven elkaar te verdedigen bij een aanval. <strong>Mercosur</strong> "
                  "is een handelsblok van landen in Zuid-Amerika. De <strong>G8</strong> en de "
                  "<strong>G20</strong> brengen belangrijke economieën samen, rijke zowel als opkomende; ze "
                  "maken geen wetten, hun afspraken zijn politieke beloftes die zwaar wegen maar die niemand "
                  "kan afdwingen."),
            ("p", "Wat een land eruit haalt: lagere of geen invoerrechten bij de andere leden, een grotere "
                  "afzetmarkt voor zijn bedrijven, en meer gewicht in onderhandelingen met andere blokken. De "
                  "prijs is dat het een stuk van zijn eigen handelsbeleid uit handen geeft, en dat is meteen de "
                  "kern van de discussie erover."),
        ]),
        dict(kop="De gevolgen, en de keerzijden", blokken=[
            ("p", "<strong>Vrijhandel</strong> haalt drempels weg, <strong>protectionisme</strong> zet ze op "
                  "met invoerrechten en quota. Veel landen schuiven tussen die twee heen en weer, afhankelijk "
                  "van welke sector ze willen beschermen. Legt een land hoge invoerrechten op buitenlands "
                  "staal, dan wordt dat staal er duurder en minder gekocht: eigen producenten krijgen "
                  "ademruimte, maar bedrijven die staal verwerken betalen meer, en het andere land neemt vaak "
                  "tegenmaatregelen."),
            ("p", "<strong>Outsourcing</strong> is werk uitbesteden aan een bedrijf in een ander land: "
                  "callcenters, boekhouding, softwarewerk, productie. Voor het ontvangende land betekent dat "
                  "werk, voor het vertrekkende land verlies van werk."),
            ("p", "<strong>Landgrabbing</strong> is het opkopen van grote stukken landbouwgrond door "
                  "buitenlandse bedrijven of staten, vooral in landen met een lagere ontwikkelingsgraad en "
                  "zwakke eigendomsregels. Op papier is de verkoop vaak wettelijk, maar wie het land al "
                  "generaties bewerkte zonder eigendomsbewijs, staat plots buiten, en de opbrengst gaat meestal "
                  "naar de uitvoer."),
            ("p", "<strong>Migratiebewegingen</strong> en <strong>ontvolking</strong> horen er ook bij. "
                  "Ontvolking is het leeglopen van een streek doordat de inwoners wegtrekken: scholen en "
                  "winkels sluiten bij gebrek aan klanten, de achterblijvende bevolking vergrijst, en huizen "
                  "komen leeg te staan. Dat versterkt zichzelf, want minder mensen betekent minder "
                  "voorzieningen. Wie migreert, stuurt vaak geld naar familie in het land van herkomst; dat "
                  "heet <em>remittances</em>, en voor sommige landen is het een grotere inkomstenbron dan alle "
                  "ontwikkelingshulp samen. Voor het vertrekland is het vertrek van hoogopgeleiden "
                  "<strong>braindrain</strong>, voor het aankomstland <strong>braingain</strong>."),
            ("p", "Ten slotte kan mondialisering <strong>spanningen</strong> tussen landen vergroten. Wie de "
                  "grondstoffen, de chips of de scheepvaartroutes in handen heeft, heeft macht. Sancties, "
                  "uitvoerverboden en het dichtdraaien van een gaskraan werken alleen als de andere kant die "
                  "goederen nodig heeft: juist de onderlinge afhankelijkheid maakt handel tot een drukmiddel."),
            ("p", "Ze heeft ook gevolgen voor de plaatselijke cultuur: wat overal te koop en te zien is, wint "
                  "het makkelijk van wat maar op één plaats bestaat. Daarom beschermen landen hun taal, hun "
                  "film en hun erfgoed vaak bewust. En de gevolgen zijn nergens gelijk: wie kan uitvoeren en "
                  "investeren, wint; wie concurreert met goedkopere invoer of grondstoffen levert zonder ze te "
                  "verwerken, verliest. Zich er helemaal aan onttrekken lukt niet zonder prijs: wie zich "
                  "afsluit, verliest afzetmarkten, invoer van technologie en investeringen."),
            ("weetje", "Mondialisering laat ook in je eigen streek sporen na: distributiecentra bij de afrit, "
                       "dezelfde winkelketens in elke winkelstraat, fabrieken die hun werk naar elders zagen "
                       "vertrekken. Dat is de ruimtelijke kant ervan, en die kan je gewoon gaan bekijken."),
        ]),
    ],
)

# ───────────────────────── 8. Duurzaam omgaan met de ruimte
BUNDELS["duurzaam-omgaan-met-de-ruimte"] = dict(
    vak=VAK, niveau=BOOST, titel="Duurzaam omgaan met de ruimte",
    onder="De vijf P's en de duurzame ontwikkelingsdoelen, en hoe je er een plan of een bedrijf mee beoordeelt.",
    secties=[
        dict(kop="Wat duurzame ontwikkeling is", blokken=[
            ("p", "<strong>Duurzame ontwikkeling</strong> is voorzien in de noden van nu zonder die van later "
                  "onmogelijk te maken. Die omschrijving zet de huidige generatie en de volgende naast elkaar, "
                  "en daarom gaat duurzaamheid over de planeet én over mensen én over welvaart tegelijk. Ze "
                  "gaat dus niet alleen over het milieu: armoede, onderwijs, ongelijkheid, werk en vrede staan "
                  "er evengoed in."),
            ("fig", svg.vijfp(), "De vijf P's, met van elk een voorbeeld. Samen tonen ze dat duurzaamheid meer "
                                 "is dan milieu alleen."),
            ("p", "<strong>Planet</strong> gaat over de aarde zelf: klimaat, water, bodem, lucht en "
                  "biodiversiteit. <strong>People</strong> gaat over de basisvoorwaarden van een menswaardig "
                  "leven: onderwijs voor iedereen, goede gezondheidszorg, het uitbannen van honger. "
                  "<strong>Prosperity</strong> gaat over welvaart en werk dat genoeg opbrengt. "
                  "<strong>Peace</strong> staat er niet toevallig bij: zonder veiligheid werkt niets anders, "
                  "want in oorlogsgebied is er geen onderwijs, geen zorg, geen investering en geen bosbeheer. "
                  "<strong>Partnership</strong> is samenwerking, want geen enkel land lost deze problemen "
                  "alleen op: klimaat, oceanen, ziektes en handel stoppen niet aan een grens."),
            ("p", "De <strong>duurzame ontwikkelingsdoelen</strong> of SDG's werden in 2015 door de landen van "
                  "de <strong>Verenigde Naties</strong> goedgekeurd, met <strong>2030</strong> als streefdatum. "
                  "Ze gaan over milieu, mensen en economie samen, ze gelden voor alle landen ter wereld, en ze "
                  "hebben een afgesproken einddatum. Afdwingbaar bij een rechtbank zijn ze niet: landen "
                  "rapporteren vrijwillig, en dat is meteen hun zwakke plek."),
            ("kader", "De doelen gelden óók voor welvarende landen. Dat is het verschil met de oudere "
                      "millenniumdoelen, die vooral op arme landen mikten. Uitstoot, afval en ongelijkheid zijn "
                      "in rijke landen vaak juist het grootst. Op het examen krijg je trouwens een overzicht "
                      "van de doelen mee: je hoeft ze niet uit het hoofd te kennen, je moet ermee kunnen "
                      "redeneren."),
        ]),
        dict(kop="Ontwikkeling en duurzaamheid", blokken=[
            ("p", "Een hogere <strong>ontwikkelingsgraad</strong> kan een stap naar een duurzamere wereld "
                  "zijn: beter onderwijs en betere zorg geven mensen ruimte om verder te kijken dan de dag van "
                  "morgen. Wie zeker is van eten, gezondheid en school, kan investeren in de lange termijn."),
            ("p", "Tegelijk stijgt met welvaart ook het verbruik, en juist dat spanningsveld is de kern van "
                  "het debat. Een land met een hoge Human Development Index heeft dus niet vanzelf een kleine "
                  "<strong>ecologische voetafdruk</strong>; vaak is het omgekeerde waar. De ecologische "
                  "voetafdruk is de oppervlakte aarde die nodig is om iemands verbruik te dekken en zijn afval "
                  "te verwerken. Leefden alle mensen zoals de gemiddelde West-Europeaan, dan was er meer dan "
                  "één aarde nodig."),
            ("p", "Daarom botsen de vijf P's soms met elkaar: wat goed is voor de welvaart, is niet altijd "
                  "goed voor de planeet. Een nieuw bedrijventerrein op akkerland brengt werk en inkomen, dus "
                  "vanuit Prosperity valt er iets voor te zeggen, maar er verdwijnt open ruimte en er komt "
                  "verharding bij, dus vanuit Planet is het moeilijk te verdedigen. Duurzaam beslissen betekent "
                  "die afweging bewust maken in plaats van één kant te vergeten. Een duurzame keuze is trouwens "
                  "zelden de goedkoopste op korte termijn: isoleren, hergebruiken en zuiveren kosten eerst "
                  "meer en verdienen zich later terug."),
            ("p", "<strong>Duurzaam ruimtegebruik</strong> betekent met dezelfde oppervlakte méér doen, in "
                  "plaats van telkens nieuwe ruimte aan te snijden: hergebruik van een leegstaand gebouw, "
                  "inbreiding, een terrein met meerdere functies. Nieuwe grond aansnijden is altijd de duurste "
                  "keuze voor de planeet. Duurzaamheid en economische groei sluiten elkaar daarbij niet uit: "
                  "hergebruik, isolatie, hernieuwbare energie en kringloop leveren ook werk en omzet op. De "
                  "spanning is echt, maar ze is geen wet."),
        ]),
        dict(kop="Verstedelijking beoordelen", blokken=[
            ("p", "De fiche somt vijf gevolgen van verstedelijking voor het leefmilieu op: "
                  "<strong>versnippering</strong> van de open ruimte, de gevolgen van <strong>verharding</strong>, "
                  "het <strong>hitte-eilandeffect</strong>, <strong>luchtvervuiling</strong> en "
                  "<strong>verkeersdrukte</strong>."),
            ("p", "Versnippering is een probleem omdat kleine losse stukken minder goed werken dan één groot "
                  "gebied: dieren kunnen zich niet verplaatsen tussen de stukken, en de randen drogen uit en "
                  "verstoren. Daarom bouwt men ecoducten en verbindingsstroken. Verharding is een probleem bij "
                  "hevige regen omdat het water niet in de grond kan en alles tegelijk naar dezelfde riool "
                  "loopt, die overloopt; het grondwater onder de stad wordt ondertussen niet aangevuld. Meer "
                  "groen en water in een stad verzachten het hitte-eilandeffect, want bomen geven schaduw en "
                  "verdampen water."),
            ("p", "Een stad die een fietssnelweg aanlegt en parkeerplaatsen schrapt, pakt drie van die vijf "
                  "tegelijk aan: minder auto's betekent minder uitstoot, minder drukte en minder asfalt."),
        ]),
        dict(kop="Industrie en landbouw beoordelen", blokken=[
            ("p", "Bij grondstofontginning, energieproductie en industrie noemt de fiche drie begrippen: "
                  "<strong>industrialisatie</strong> (er komt fabrieksactiviteit bij, met werk en met "
                  "ruimtebeslag), <strong>de-industrialisatie</strong> (die verdwijnt weer) en "
                  "<strong>reconversie</strong> (het oude terrein krijgt een nieuwe functie)."),
            ("p", "Reconversie is duurzamer dan een nieuw terrein aansnijden, want de grond werd al gebruikt "
                  "en er gaat geen open ruimte verloren. Goedkoper is ze niet noodzakelijk: een oude "
                  "fabriekssite kan vervuilde grond bevatten, want zware metalen, olie en oplosmiddelen blijven "
                  "decennia in de bodem. Die grond moet eerst <strong>gesaneerd</strong> worden, en die kost is "
                  "een van de redenen waarom zo'n site soms jaren leeg blijft liggen. Kiest een gemeente tussen "
                  "een verkaveling op akkerland en het opknappen van zo'n site, dan is de site de duurzamere "
                  "keuze."),
            ("p", "Bij de landbouw noemt de fiche <strong>bodemerosie</strong>, <strong>bodemdegradatie</strong>, "
                  "<strong>ontbossing</strong> en <strong>schaalvergroting</strong>. Bodemdegradatie is een "
                  "probleem voor de lange termijn omdat herstel tientallen jaren duurt terwijl verlies in "
                  "enkele seizoenen gaat. Ontbossing voor landbouwgrond laat koolstof vrij die in het bos en de "
                  "bosbodem opgeslagen zat, bovenop het verlies aan biodiversiteit."),
            ("p", "Krijg je op het examen de beschrijving van een landbouwbedrijf en de lijst met doelen, dan "
                  "is de opdracht: beoordelen of het bedrijf duurzaam werkt, met argumenten uit die lijst of "
                  "uit de vijf P's. Een bedrijf dat jaar na jaar hetzelfde gewas op dezelfde hellende percelen "
                  "teelt zonder groenbedekker, werkt niet duurzaam: geen vruchtwisseling put de bodem uit, en "
                  "een kale helling laat de regen de bovenlaag meenemen. Wisselt het zijn gewassen af, houdt "
                  "het hagen en bufferstroken, en bemest het niet meer dan de teelt opneemt, dan wél."),
            ("kader", "Een goed oordeel <strong>weegt af</strong> in plaats van te kiezen. Een windmolenpark "
                      "levert energie zonder uitstoot, maar neemt ruimte in en raakt landschap, geluid en "
                      "vogels. Zeg dus wat er aan beide kanten van de weegschaal ligt, en zeg met welke P of "
                      "welk doel je elk argument verbindt. En stel je altijd eerst de vraag: wat betekent dit "
                      "op lange termijn voor mens én omgeving?"),
        ]),
    ],
)

# ───────────────────────── 9. Het versterkte broeikaseffect
BUNDELS["het-versterkte-broeikaseffect"] = dict(
    vak=VAK, niveau=BOOST, titel="Het versterkte broeikaseffect",
    onder="De vier sferen en de koolstofcyclus, de stralingsbalans en het albedo, en de oorzaken en gevolgen van de opwarming.",
    secties=[
        dict(kop="De vier sferen en de koolstofcyclus", blokken=[
            ("p", "Op aarde onderscheidt men vier <strong>sferen</strong>. De <strong>geosfeer</strong> is het "
                  "gesteente, de <strong>biosfeer</strong> al wat leeft, de <strong>atmosfeer</strong> de "
                  "lucht, en de <strong>hydrosfeer</strong> al het water: oceanen, rivieren en ijs."),
            ("p", "Koolstof blijft niet in één sfeer zitten maar beweegt er voortdurend tussen. Dat is de "
                  "<strong>koolstofcyclus</strong>. Bij <strong>fotosynthese</strong> neemt een plant CO₂ op "
                  "uit de lucht en bouwt daar met zonlicht suikers mee: koolstof gaat dan van de atmosfeer naar "
                  "de biosfeer. Een dier eet de plant, het dier sterft, en de koolstof gaat de bodem in. Via "
                  "verbranding of verwering komt ze weer in de lucht."),
            ("p", "Uit de <strong>geosfeer</strong> komt koolstof langs drie wegen terug in de atmosfeer: het "
                  "verbranden van steenkool, olie en aardgas, vulkaanuitbarstingen die gas uitstoten, en het "
                  "maken van cement uit kalksteen. Een bos aanplanten werkt precies de andere kant op."),
            ("kader", "<strong>Fossiele brandstoffen</strong> zijn koolstof die miljoenen jaren geleden uit de "
                      "lucht werd gehaald door planten en plankton. Door ze te verbranden zetten wij die oude "
                      "koolstof in enkele eeuwen terug in de lucht. Dát is de kern van het probleem."),
            ("p", "De <strong>oceanen</strong> spelen een grote rol: CO₂ lost op in zeewater, dus zijn ze na "
                  "het gesteente de grootste opslagplaats van koolstof. Ze nemen ook een groot deel van de "
                  "extra warmte op, en dat vertraagt de opwarming van de lucht. Daar staat tegenover dat het "
                  "water uitzet, dat het verzuurt, en dat het die warmte later weer afgeeft. Die "
                  "<strong>oceaanverzuring</strong> maakt het voor koralen en schelpdieren moeilijker om hun "
                  "kalkskelet op te bouwen, en dat raakt de hele voedselketen in zee."),
        ]),
        dict(kop="Broeikasgassen en de stralingsbalans", blokken=[
            ("p", "De <strong>broeikasgassen</strong> uit de fiche zijn waterdamp (H₂O), koolstofdioxide "
                  "(CO₂), methaan (CH₄) en lachgas (N₂O). Zuurstof en stikstofgas vormen samen het grootste "
                  "deel van de lucht maar werken niet als broeikasgas."),
            ("p", "De <strong>stralingsbalans</strong> is de verhouding tussen de straling die binnenkomt en "
                  "de warmte die weer weggaat. Blijft er meer binnen dan er weggaat, dan warmt de aarde op tot "
                  "de balans weer klopt. Broeikasgassen laten zonlicht vlot binnen maar houden een deel van de "
                  "warmtestraling die de aarde teruggeeft in de atmosfeer vast en sturen die opnieuw naar "
                  "beneden."),
            ("p", "Het tweede sleutelbegrip is het <strong>albedo</strong>, het "
                  "<strong>weerkaatsingsvermogen</strong> van een oppervlak: hoeveel straling het "
                  "terugkaatst, uitgedrukt als een getal tussen nul en één. Verse sneeuw op een gletsjer kaatst "
                  "het grootste deel van het zonlicht terug en heeft dus een hoog albedo; open water, een "
                  "donker naaldbos of asfalt slorpen juist veel op."),
            ("fig", svg.stralingsbalans(), "Wit kaatst terug, donker neemt op. Daarom versterkt smeltend ijs "
                                           "de opwarming: wat eronder tevoorschijn komt, is donkerder."),
            ("p", "Smelt zee-ijs, dan komt er donkerder water bloot dat meer warmte opneemt. Minder ijs "
                  "betekent een lager albedo, dus meer opwarming, dus nog minder ijs. Zo'n zichzelf "
                  "versterkende lus heet een <strong>terugkoppeling</strong> in het "
                  "<strong>klimaatsysteem</strong>: een gevolg dat zijn eigen oorzaak "
                  "versterkt of verzwakt. Daardoor is dat systeem zo moeilijk voorspelbaar. Dooiende <strong>permafrost</strong> is er nog zo een: in de bevroren "
                  "bodem van Siberië en Canada zit enorm veel organisch materiaal, en ontdooit die, dan begint "
                  "het te rotten en komen er methaan en CO₂ vrij die er duizenden jaren in opgesloten zaten."),
        ]),
        dict(kop="Natuurlijk en versterkt", blokken=[
            ("p", "Zonder het <strong>natuurlijke broeikaseffect</strong> zou het op aarde gemiddeld ongeveer "
                  "<strong>achttien graden onder nul</strong> zijn in plaats van ongeveer vijftien graden "
                  "erboven. Het natuurlijke broeikaseffect is dus geen probleem maar juist de reden dat er "
                  "leven mogelijk is. Het helemaal wegwerken zou de aarde te koud maken."),
            ("fig", svg.broeikas(), "Hetzelfde mechanisme, twee keer. Rechts zitten er meer broeikasgassen in "
                                    "de lucht, dus ontsnapt er minder warmte."),
            ("p", "Het <strong>versterkte broeikaseffect</strong> komt van de extra gassen die de mens "
                  "uitstoot. Het mechanisme is precies hetzelfde; het verschil zit in de hoeveelheid."),
            ("p", "<strong>Waterdamp</strong> is een belangrijk broeikasgas, maar de mens brengt het niet "
                  "rechtstreeks in de lucht. De hoeveelheid ervan volgt de temperatuur: warmere lucht houdt "
                  "meer damp vast, en dat versterkt de opwarming die er al was. Waterdamp werkt dus als een "
                  "terugkoppeling, niet als een oorzaak."),
        ]),
        dict(kop="De oorzaken", blokken=[
            ("p", "Het grootste deel van de door de mens uitgestoten CO₂ komt uit het verbranden van "
                  "<strong>steenkool, olie en aardgas</strong>: energie, transport, verwarming en industrie "
                  "draaien er grotendeels op. Ontbossing en cementproductie komen daarbij."),
            ("p", "<strong>Methaan</strong> ontstaat overal waar organisch materiaal zonder zuurstof "
                  "afbreekt: bij herkauwers zoals runderen, op rijstvelden onder water, op stortplaatsen met "
                  "rottend afval. Daarbij komen nog de lekken bij de winning en het transport van aardgas. "
                  "<strong>Lachgas</strong> komt in de landbouw vooral van het bemesten van de grond: "
                  "bacteriën in de bodem zetten stikstof uit mest en kunstmest deels om in lachgas. Daarom "
                  "telt de manier van bemesten mee in de klimaatbalans van een bedrijf."),
            ("p", "Dat de hoeveelheid CO₂ in de lucht al decennia stijgt, meet men op drie manieren die "
                  "dezelfde kant op wijzen: met meetstations verspreid over de wereld, aan luchtbelletjes in "
                  "oude <strong>ijskernen</strong> uit het poolijs, en met langlopende reeksen die jaar na "
                  "jaar worden aangevuld. IJskernen laten toe om ver terug te kijken, tot lang voor er gemeten "
                  "werd."),
            ("weetje", "Krijg je een grafiek van de CO₂-hoeveelheid sinds 1960, kijk dan eerst naar de "
                       "eenheid, de schaal van de assen en de gemeten periode. Een afgeknipte as of een te "
                       "korte periode kan elke trend laten verdwijnen of overdrijven."),
        ]),
        dict(kop="De gevolgen", blokken=[
            ("p", "De fiche somt vijf gevolgen op. Het eerste is de <strong>zeespiegelstijging</strong>, met "
                  "twee oorzaken tegelijk: water zet uit als het warmer wordt, en het <strong>landijs</strong> "
                  "van Groenland, Antarctica en de gletsjers voegt water toe dat eerst op land lag. Drijvend "
                  "<strong>zee-ijs</strong> telt daarin níét mee: dat verplaatst al evenveel water als het "
                  "weegt, dus het smelten ervan verandert het peil niet. Het telt wel mee via het albedo. "
                  "Laaggelegen kustgebieden, delta's zoals die van de Ganges en de Nijl, en eilandstaten in de "
                  "Stille Oceaan lopen het grootste risico, en net daar wonen heel veel mensen dicht op elkaar."),
            ("p", "Het tweede is de <strong>verschuiving van de klimaatzones</strong>, naar de polen toe en op "
                  "bergen naar boven toe. Het derde volgt daaruit: de <strong>leefgebieden van planten en "
                  "dieren</strong> schuiven mee. Wie traag is, of vastzit tussen steden en akkers, geraakt niet "
                  "mee, en wie al op de top of aan de pool zit, kan nergens meer heen. Dat zet de "
                  "<strong>biodiversiteit</strong>, de verscheidenheid aan soorten die een ecosysteem "
                  "veerkrachtig maakt, zwaar onder druk."),
            ("p", "Het vierde zijn de <strong>extreme weerfenomenen</strong>: langere en zwaardere "
                  "hittegolven, hevigere buien met veel neerslag in korte tijd, en langere droogteperiodes in "
                  "bepaalde streken. Warmere lucht houdt meer vocht vast, dus valt er meer in één keer terwijl "
                  "het elders langer droog blijft. Het weer wordt grilliger, niet gelijkmatiger. Voor "
                  "Vlaanderen is dat meteen een waterprobleem: bij een hevige bui loopt het water over verharde "
                  "grond weg, en bij droogte staat de grondwatertafel te laag."),
            ("p", "Het vijfde is de <strong>verspreiding van tropische ziektes</strong>. De muggen die ze "
                  "overbrengen hebben warmte nodig om zich voort te planten; warmt een streek op, dan schuift "
                  "het gebied waarin zo'n mug kan leven mee, en de ziekte schuift mee."),
            ("kader", "<strong>Weer</strong> is wat er vandaag gebeurt, <strong>klimaat</strong> is het "
                      "gemiddelde over dertig jaar. Eén hittegolf bewijst dus niets op zichzelf. Dat hete "
                      "zomers stééds vaker voorkomen, zegt wel iets."),
            ("p", "De opwarming treft niet elk land even hard: ligging, reliëf en welvaart bepalen mee hoe "
                  "kwetsbaar een land is. Een laaggelegen deltastaat met weinig middelen loopt veel meer risico "
                  "dan een bergland met een hoge HDI. En het zijn niet de landen met de hoogste uitstoot per "
                  "inwoner die het hardst getroffen worden: meestal is het omgekeerd. Landen met een lagere "
                  "ontwikkelingsgraad stoten per inwoner veel minder uit en hebben tegelijk het minste geld om "
                  "zich te beschermen. Dat is de kern van wat men klimaatrechtvaardigheid noemt."),
        ]),
    ],
)

# ───────────────────────── 10. Een geografisch onderzoek voeren
BUNDELS["een-geografisch-onderzoek-voeren"] = dict(
    vak=VAK, niveau=BOOST, titel="Een geografisch onderzoek voeren",
    onder="Van onderzoeksvraag tot besluit, met terreinwerk, bronnen en Geopunt, en met de grenzen van elke bron erbij.",
    secties=[
        dict(kop="De vraag komt eerst", blokken=[
            ("p", "Een geografisch onderzoek begint met een <strong>onderzoeksvraag</strong> of een "
                  "<strong>hypothese</strong>. Zonder vraag weet je niet welke bron je nodig hebt: de vraag "
                  "stuurt de keuze van de kaartlagen, de metingen en het terreinwerk, niet omgekeerd."),
            ("p", "Een goede vraag is afgebakend in ruimte en tijd en je kan ze met bronnen beantwoorden. "
                  "\"Waarom staat het in onze gemeente elke ochtend stil?\" is er een. \"Is verkeer goed of "
                  "slecht?\" is een meningsvraag, en \"Hoeveel auto's bestaan er wereldwijd?\" is te breed."),
            ("p", "Een <strong>hypothese</strong> is een verwachting die je opschrijft <em>vóór</em> je meet, "
                  "zodat je achteraf eerlijk kan zeggen of ze klopte. Wie ze achteraf opschrijft, heeft altijd "
                  "gelijk, en dat is geen onderzoek meer. Een weerlegde hypothese is trouwens geen mislukking "
                  "maar gewoon een resultaat: wat een onderzoek doet slagen, is dat je vraag scherp is en je "
                  "besluit steunt op wat je echt gemeten hebt."),
            ("p", "Volgens de fiche kan je onderzoek over vier thema's gaan: <strong>mobiliteit</strong> (files, "
                  "lawaai en geluidshinder, luchtvervuiling en luchtkwaliteit), "
                  "<strong>waterproblematieken</strong> (watertekort of waterschaarste, "
                  "overstromingen), <strong>veranderend landgebruik</strong> (schaalvergroting, verstedelijking, "
                  "aanpassingen voor duurzaamheid) en <strong>klimaatverandering</strong> in het landschap. "
                  "Telkens onderzoek je oorzaken én gevolgen."),
        ]),
        dict(kop="Bronnen en terreinwerk", blokken=[
            ("p", "De <strong>geografische hulpbronnen</strong> uit de fiche zijn onder meer een atlas, "
                  "kaarten, satellietbeelden, foto's en luchtfoto's, tekeningen en schetsen, teksten, figuren, "
                  "determineertabellen, cijfergegevens, grafieken, leeftijdshistogrammen, klimatogrammen, "
                  "tabellen en diagrammen. Op het examen krijg je zelf een algemene wereldatlas mee, dus loont "
                  "het om er thuis mee te oefenen."),
            ("p", "Kies je bron bij je vraag. Voor de neerslag van de voorbije dertig jaar heb je een lange "
                  "<strong>meetreeks</strong> van een weerstation nodig, want klimaat is het gemiddelde over "
                  "dertig jaar; een voorspelling voor volgende week zegt daar niets over. Voor veranderend "
                  "landgebruik leg je kaarten of luchtfoto's uit verschillende jaren naast elkaar: één beeld "
                  "toont een toestand, twee beelden tonen een proces. Let er dan op dat ze uit hetzelfde "
                  "seizoen en op dezelfde schaal komen."),
            ("p", "Noteer bij elke bron het <strong>jaartal</strong>. Een bedrijventerrein uit 2015 kan "
                  "intussen verdubbeld zijn, en een verouderde kaart toont de toestand van nu verkeerd. Oude "
                  "bronnen zijn wél bruikbaar, juist om verandering te tonen, maar dan moet je weten van "
                  "wanneer ze zijn. Noteer bij een eigen meting ook <em>wanneer</em> en <em>waar</em> je "
                  "gemeten hebt: op zondagochtend meet je iets heel anders dan op een schooldag om acht uur. "
                  "Metingen wegselecteren die je niet bevallen, is vervalsen."),
            ("p", "Welk <strong>meetinstrument</strong> je gebruikt, bepaalt je onderzoeksvraag, niet "
                  "andersom: meet je geluidshinder, dan heb je een geluidsmeter nodig, meet je hoogte, dan een "
                  "hoogtemeter of de hoogtelaag van Geopunt. Bij goed <strong>bronnengebruik</strong> hoort dat "
                  "je bij elke meting noteert waarmee, waar en wanneer je gemeten hebt, en dat je op meerdere "
                  "momenten meet in plaats van één keer: één meting langs een drukke weg zegt nog niets over "
                  "een gewone dag."),
            ("p", "<strong>Terreinwerk</strong> of <strong>veldwerk</strong> is onderzoek dat je buiten doet, "
                  "op de plek zelf. <strong>Terreinkartering</strong> is daarvan de bekendste vorm: op het "
                  "terrein zelf noteren wat je waar ziet, op een "
                  "kaart: bebouwing, groen, water, wegen, functies van gebouwen. Zo maak je van je waarneming "
                  "een bron. Wie een wijk heeft afgelopen, draagt daarna een veel scherper beeld van die wijk "
                  "mee: terreinwerk maakt je <strong>mentale kaart</strong> rijker en juister."),
            ("p", "Op het examen krijg je in plaats van echt terreinwerk een <strong>simulatie</strong>: een "
                  "filmpje van een terreinoefening, een videofragment of een andere bron. Daaruit haal je "
                  "de informatie die je onderzoek nodig "
                  "heeft, je herkent er landschapskenmerken in, je brengt die aan op een kaart, en je gebruikt "
                  "ze om je ruimtelijk probleem te onderzoeken."),
            ("p", "Met een <strong>systeemdenkschema</strong> toon je hoe de elementen van je onderzoek met "
                  "elkaar samenhangen: pijlen tussen de elementen tonen oorzaak en gevolg. Onderzoek je "
                  "overstromingsgevaar, dan zet je de verharde oppervlakte, de ligging ten opzichte van de "
                  "rivier en het hoogteverschil in je schema, want die drie sturen samen waar het water "
                  "naartoe gaat."),
        ]),
        dict(kop="Werken met Geopunt", blokken=[
            ("p", "<strong>Geopunt</strong> is de digitale kaart van de Vlaamse overheid. Ze bundelt honderden "
                  "kaartlagen over Vlaanderen: bodem, water, wegen, bebouwing, erfgoed en nog veel meer. Je mag "
                  "haar tijdens het examen gebruiken, samen met een rekenmachine, een woordenboek en de "
                  "spellingcontrole; de links zitten in het examen zelf."),
            ("p", tabel(["wat je wil doen", "wat je gebruikt"],
                        [["een adres of coördinaten vinden", "de zoekbalk"],
                         ["kiezen wat er op de kaart staat", "het lagenpaneel"],
                         ["weten wat een kleur of een symbool betekent", "de legende, in het lagenpaneel"],
                         ["een afstand of oppervlakte meten", "het meetgereedschap"],
                         ["de hoogte van een plaats aflezen", "de hoogtelaag met haar legende"],
                         ["twee lagen vergelijken", "een laag transparant maken"]])),
            ("p", "Met het <strong>meetgereedschap</strong> teken je een lijn of een vlak en lees je de "
                  "lengte of de oppervlakte af. Hoogte lees je niet zo af: daarvoor zet je de hoogtelaag aan en "
                  "kijk je in de <strong>legende</strong> of in het linkerpaneel welke kleur bij welke hoogte "
                  "hoort. De legende is het overzicht dat uitlegt welke kleur of welk symbool op een kaart wat "
                  "betekent; zonder legende lees je een kaart niet. Zo zie je meteen waar het water naartoe zal lopen. De dichtheid van een gemeente moet "
                  "je zelf berekenen."),
            ("p", "Je kan gerust meerdere kaartlagen tegelijk zichtbaar zetten; je bent niet beperkt tot "
                  "één laag. Verschillende lagen <em>over elkaar</em> leggen is zelfs een van de sterkste "
                  "trucs: leg de laag met overstromingsgevoelige gebieden half doorzichtig over een luchtfoto "
                  "van je wijk, en je ziet welke gebouwen in een risicogebied staan. Wil je weten of de open "
                  "ruimte in je gemeente is afgenomen, dan vergelijk je twee luchtfotolagen van verschillende "
                  "jaren en reken je met het meetgereedschap uit hoeveel hectare erbij kwam."),
        ]),
        dict(kop="Besluiten, en zeggen wat je niet weet", blokken=[
            ("p", "Je besluit hoort bij je <strong>gegevens</strong>, niet bij je hypothese. Komt het daarmee "
                  "in botsing, dan schrijf je dat op in plaats van je gegevens bij te sturen. De stappen zijn "
                  "dus: een vraag of hypothese opstellen, bronnen kiezen en gegevens verzamelen, analyseren, "
                  "besluiten, en de beperkingen benoemen."),
            ("p", "Die laatste stap vraagt de fiche uitdrukkelijk: leg uit hoe de voorstelling van de gegevens "
                  "op digitale kaarten je geholpen heeft, én wat de beperkingen waren. Een bron kritisch "
                  "bekijken hoort bij het onderzoek zelf; wie zegt wat zijn bron niet kan tonen, laat zien dat "
                  "hij ze begrijpt. Dat is het verschil tussen een kaart aflezen en met een kaart onderzoeken."),
            ("p", "De belangrijkste beperkingen van een digitale kaart: sommige lagen zijn ouder dan de "
                  "toestand van vandaag, je ziet enkel wat er als laag beschikbaar is, en de klassen in de "
                  "legende zijn door iemand gekozen. Een luchtfoto toont dus niet altijd vandaag; ze wordt om "
                  "de zoveel jaar genomen, en juist daarom kan je er oudere reeksen naast leggen. De "
                  "coördinaten en de afstanden kloppen wel degelijk, daar is zo'n kaart net voor gemaakt."),
            ("kader", "Een gat in je gegevens is zelf een resultaat. Noteer ook welke laag je níét gevonden "
                      "hebt: zo weet de lezer wat je besluit wel en niet kan dekken. Een besluit mag dus "
                      "gerust zeggen dat er te weinig gegevens waren om de vraag te beantwoorden."),
            ("weetje", "In de fiche staat dat álle te kennen inhoud in dit deel van het examen verwerkt kan "
                       "zijn. Onderzoek is dus geen apart stukje leerstof, maar de manier waarop de rest "
                       "getoetst wordt."),
        ]),
    ],
)
