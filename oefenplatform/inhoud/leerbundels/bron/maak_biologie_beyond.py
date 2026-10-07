# -*- coding: utf-8 -*-
"""De leerbundels voor biologie op 🌍 Beyond-niveau.

Gebaseerd op de vakfiche biologie van de 3de graad doorstroomfinaliteit,
geldig vanaf 1 januari 2027. Die fiche hoort bij de richtingen die naast
natuurwetenschappen drie aparte vakken hebben: biologie, chemie en fysica.
Ze gaat dus veel dieper dan de fiche natuurwetenschappen van dezelfde graad.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De eenentwintig thema's volgen de weging van de fiche zelf: drie thema's per
onderdeel van 15 procent, twee per onderdeel van 10 procent, en vier voor de
moleculaire genetica omdat dat onderdeel over vijf bladzijden termen loopt.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/biologie.json` doet daar
het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond". Enkele thematitels lijken op die van
natuurwetenschappen 🌍 Beyond, maar de inhoud ligt hier dieper.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Biologie"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. De cel, de organellen en de biologische membranen
BUNDELS["de-cel-de-organellen-en-de-biologische-membranen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De cel, de organellen en de biologische membranen",
    onder="Van organisatieniveau tot organel, en hoe een membraan gebouwd is.",
    secties=[
        dict(kop="Organisatieniveaus en twee soorten cellen", blokken=[
            ("p", "Het leven is in <strong>organisatieniveaus</strong> geordend: van atoom over "
                  "molecule, organel, cel, weefsel, orgaan en orgaanstelsel naar organisme. Elk niveau "
                  "bestaat uit delen van het niveau eronder."),
            ("p", "Er zijn twee grote celtypes. Een <strong>prokaryote cel</strong>, zoals een bacterie, "
                  "heeft <strong>geen kern</strong> en geen membraanorganellen; haar "
                  "<strong>ringvormige chromosoom ligt vrij in het cytoplasma</strong>. Een "
                  "<strong>eukaryote cel</strong> heeft wél een kern met een "
                  "<strong>kernmembraan</strong> en een heel stel organellen."),
            ("p", "Het <strong>kernmembraan</strong> is dubbel en zit vol "
                  "<strong>kernporiën</strong>. Daardoor kan een rijp mRNA naar buiten, terwijl het "
                  "DNA zelf binnen blijft."),
        ]),
        dict(kop="De organellen, één voor één", blokken=[
            ("p", "In de <strong>kern</strong> ligt het DNA, en daarin zit de "
                  "<strong>nucleolus</strong> of het <strong>kernlichaampje</strong>, "
                  "<strong>waar de ribosomen gemaakt worden</strong>."),
            ("p", "Een <strong>ribosoom</strong> <strong>bouwt eiwitten</strong>. Zit het vast op het "
                  "endoplasmatisch reticulum, dan heet dat het <strong>ruw ER</strong>, en dat staat "
                  "dus <strong>in dienst van de eiwitsynthese</strong>. Het <strong>glad ER</strong> "
                  "heeft geen ribosomen en <strong>maakt lipiden en ontgift stoffen</strong>."),
            ("p", "Het <strong>golgicomplex</strong> <strong>werkt eiwitten af, sorteert ze en "
                  "verpakt ze in blaasjes</strong>. Zo'n blaasje heet een <strong>vesikel</strong> of "
                  "<strong>transportblaasje</strong> en "
                  "<strong>verplaatst stoffen binnen de cel</strong>."),
            ("p", "Een <strong>lysosoom</strong> zit vol verteringsenzymen en "
                  "<strong>breekt versleten onderdelen en opgenomen deeltjes af</strong>."),
            ("p", "Het <strong>mitochondrion</strong> is de plaats van de "
                  "<strong>celademhaling</strong>: daar lopen de "
                  "<strong>Krebscyclus</strong> en de <strong>eindoxidaties</strong>, en daar "
                  "wordt dus de <strong>ATP</strong> gemaakt. Een cel die "
                  "<strong>veel energie verbruikt</strong>, zoals een spiercel, is dan ook "
                  "<strong>bijzonder rijk aan mitochondriën</strong>, in het Latijn "
                  "<strong>mitochondria</strong>. Zijn "
                  "binnenmembraan is sterk geplooid in <strong>cristae</strong>, en dat "
                  "<strong>vergroot het oppervlak voor de eindoxidaties</strong>."),
            ("p", "De <strong>vacuole</strong> is bij een plantencel groot en "
                  "<strong>bewaart water en stoffen en zorgt voor de stevigheid</strong>. Het "
                  "<strong>centriool</strong> helpt bij de <strong>opbouw van de spoelfiguur</strong> "
                  "tijdens een celdeling: daaraan worden de "
                  "<strong>spoeldraden vastgemaakt</strong>."),
        ]),
        dict(kop="Plastiden, cytoskelet, plant en dier", blokken=[
            ("p", "Planten hebben <strong>plastiden</strong>. Een <strong>chloroplast</strong> doet de "
                  "<strong>fotosynthese</strong>, een <strong>amyloplast</strong> "
                  "<strong>bewaart zetmeel</strong>, een <strong>chromoplast</strong> bevat "
                  "<strong>kleurstoffen</strong> en een <strong>leukoplast</strong> is kleurloos."),
            ("p", "Het <strong>cytoskelet</strong> <strong>geeft de cel vorm en laat beweging "
                  "toe</strong>. Het bestaat onder meer uit <strong>microtubuli</strong>, "
                  "<strong>de dikste draden, die bij een deling als spoeldraad dienen</strong>, en "
                  "uit <strong>microfilamenten van actine</strong>, de dunste."),
            ("p", "Een <strong>plantencel</strong> heeft een celwand, chloroplasten en één grote "
                  "vacuole; een <strong>dierlijke cel</strong> heeft die niet, maar wel "
                  "centriolen."),
            ("p", "De <strong>endosymbiosetheorie</strong> verklaart waar mitochondriën en "
                  "chloroplasten vandaan komen: <strong>het waren ooit vrijlevende bacteriën die door "
                  "een grotere cel opgenomen werden</strong>. Dat ze een "
                  "<strong>eigen ringvormig DNA en eigen ribosomen</strong> hebben en zich "
                  "<strong>zelf delen</strong>, past precies bij dat idee."),
        ]),
        dict(kop="Het celmembraan", blokken=[
            ("p", "Een biologisch membraan is gebouwd volgens het "
                  "<strong>vloeibaar mozaïekmodel</strong>: een "
                  "<strong>dubbellaag van fosfolipiden waarin eiwitten als een mozaïek "
                  "ronddrijven</strong>. Vloeibaar, want de moleculen kunnen zijdelings bewegen."),
            ("p", "Een <strong>fosfolipide</strong> heeft een <strong>hydrofiele kop</strong> en "
                  "<strong>twee hydrofobe staarten</strong>. In water keren de staarten zich naar "
                  "elkaar toe en de koppen naar buiten; zo vormt zich vanzelf een dubbellaag."),
            ("p", "<strong>Cholesterol</strong> zit tussen de fosfolipiden en "
                  "<strong>houdt het membraan soepel bij wisselende temperatuur</strong>."),
            ("p", "De eiwitten doen het werk. Een <strong>transmembraaneiwit</strong> "
                  "<strong>steekt door de hele dubbellaag</strong> en kan als kanaal of pomp dienen. "
                  "Een <strong>receptoreiwit</strong> <strong>vangt een signaalmolecule of signaalstof op</strong>, "
                  "bijvoorbeeld een hormoon. Omdat het membraan vloeibaar is, "
                  "<strong>kunnen die eiwitten zich erin verplaatsen</strong>."),
            ("p", "Aan de buitenkant liggen sacharideketens: de <strong>glycocalyx</strong>. Die "
                  "<strong>laat cellen elkaar herkennen</strong>."),
        ]),
        dict(kop="Buiten het membraan", blokken=[
            ("p", "Bovenop het membraan kan er een <strong>celwand</strong> liggen. Bij een "
                  "<strong>plant</strong> is die van <strong>cellulose</strong>, bij een "
                  "<strong>bacterie</strong> van <strong>peptidoglycaan</strong> en bij een "
                  "<strong>schimmel</strong> van <strong>chitine</strong>. Let op: "
                  "<strong>een celwand is doorlaatbaar en kiest niet</strong>. "
                  "<strong>Halfdoorlaatbaar of selectief is het celmembraan eronder</strong>."),
            ("p", "Tussen twee plantencellen lopen <strong>plasmodesmata</strong>: fijne kanaaltjes "
                  "door de celwand, zodat de cytoplasma's met elkaar in verbinding staan."),
        ]),
    ],
    onthoud=[
        "Een prokaryoot heeft geen kern, een eukaryoot wel.",
        "Ribosoom bouwt eiwit, golgi werkt af en verpakt, lysosoom breekt af.",
        "Het mitochondrion maakt ATP; de cristae vergroten het oppervlak.",
        "Een membraan is een dubbellaag fosfolipiden met eiwitten erin.",
        "Mitochondriën en chloroplasten hebben eigen DNA: endosymbiose.",
    ],
)

# ───────────────────────── 2. Celdifferentiatie, weefsels en celtypes
BUNDELS["celdifferentiatie-weefsels-en-celtypes-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Celdifferentiatie, weefsels en celtypes",
    onder="Hoe uit één cel gespecialiseerde weefsels groeien, bij planten en bij dieren.",
    secties=[
        dict(kop="Van deling tot differentiatie", blokken=[
            ("p", "Een organisme groeit in drie stappen: <strong>celdeling</strong>, "
                  "<strong>celstrekking</strong> en <strong>celdifferentiatie</strong>. Bij de "
                  "differentiatie krijgt een cel haar definitieve vorm en taak."),
            ("p", "Alle cellen van één organisme hebben <strong>hetzelfde DNA</strong>. Dat ze toch "
                  "verschillen, komt doordat ze <strong>andere genen tot expressie brengen</strong>."),
            ("p", "Bij planten zitten de delende cellen in een <strong>meristeem</strong>; dat is "
                  "<strong>het weefsel waar de celdelingen gebeuren</strong>. Die "
                  "<strong>meristeemcellen</strong> zitten onder meer in de "
                  "<strong>worteltop</strong> en in de top van de stengel. Bij een plant volgt op "
                  "de celdeling meteen de strekking en de differentiatie: "
                  "<strong>een stamcelstadium zoals bij een dier zit daar niet tussen</strong>."),
            ("p", "Een <strong>stamcel</strong> is een cel die zich kan blijven delen en nog "
                  "verschillende kanten op kan. Daarom bestaat er <strong>stamceltherapie</strong>: "
                  "<strong>met stamcellen wordt beschadigd weefsel hersteld</strong>. Een "
                  "<strong>kloon</strong> is een individu of een cel met <strong>precies hetzelfde "
                  "erfelijk materiaal</strong>. Met stamcellen kan "
                  "<strong>beschadigd weefsel vervangen worden</strong> en kunnen "
                  "<strong>nieuwe bloedcellen aangemaakt worden</strong>. Een "
                  "<strong>tuinder kloneert</strong> een plant trouwens al eeuwen zonder labo: "
                  "<strong>hij laat een stek of een scheut wortelen</strong>, en uit één "
                  "<strong>gedifferentieerde plantencel</strong> kan een hele nieuwe plant "
                  "groeien."),
            ("p", "Een cel die niet meer deelt, staat in de <strong>G0-fase</strong>, buiten de "
                  "celcyclus. Zenuwcellen en spiercellen blijven daar hun hele leven in: een "
                  "<strong>gedifferentieerde zenuwcel is uit de celcyclus gestapt</strong> en kan "
                  "zich dus niet meer delen."),
        ]),
        dict(kop="De weefsels van een plant", blokken=[
            ("p", "Een plant heeft <strong>huidweefsel</strong>, <strong>transportweefsel</strong> en "
                  "<strong>grondweefsel</strong>."),
            ("p", "Het huidweefsel heet ook de <strong>epidermis</strong>, en het "
                  "<strong>beschermt de plant tegen uitdroging</strong>. Op de epidermis van een "
                  "blad ligt een <strong>cuticula</strong> of waslaag, die "
                  "<strong>verdamping tegengaat</strong>. In dat huidweefsel liggen "
                  "<strong>huidmondjes</strong>, meestal "
                  "<strong>aan de onderkant van het blad</strong>; ze "
                  "<strong>laten gassen in en uit het blad</strong> en regelen de verdamping. "
                  "<strong>Bij droogte gaan ze juist dicht</strong>, om water te sparen."),
            ("p", "Het transportweefsel bestaat uit <strong>xyleem</strong>, dat "
                  "<strong>water en mineralen van de wortel naar boven voert</strong>, en "
                  "<strong>floëem</strong>, dat <strong>suikers vanuit het blad verdeelt</strong>. "
                  "Samen vormen ze een <strong>vaatbundel</strong>. De "
                  "<strong>xyleemcellen die water transporteren, zijn bij volle werking dode "
                  "cellen zonder inhoud</strong>: er blijft enkel een buisje van celwanden over."),
            ("p", "Tot het grondweefsel horen de <strong>parenchymcellen</strong>, de gewone "
                  "levende vulcellen, en de <strong>sclerenchymcellen</strong>: die hebben dikke, "
                  "verhoute wanden en <strong>geven de plant stevigheid</strong>. "
                  "<strong>Wortelharen</strong> zijn fijne uitstulpingen die het "
                  "<strong>oppervlak waarmee de plant water opneemt, vergroten</strong>."),
            ("p", "In een blad liggen twee soorten grondweefsel: het "
                  "<strong>palissadeparenchym</strong>, met cellen dicht naast elkaar en "
                  "<strong>veel chloroplasten voor de fotosynthese</strong>, en het "
                  "<strong>sponsparenchym</strong>, met <strong>ruimten tussen de cellen voor de "
                  "gaswisseling</strong>. Dat sponsparenchym, ook <strong>sponsweefsel</strong> "
                  "genoemd, heeft dus <strong>veel luchtruimten tussen de cellen</strong>. Het "
                  "palissadeparenchym bevat <strong>de meeste chloroplasten</strong> van het blad. "
                  "De <strong>cortex</strong> is het grondweefsel tussen huidweefsel en "
                  "vaatbundels, en de <strong>stengel</strong> brengt het blad naar het licht."),
        ]),
        dict(kop="De weefsels van een dier", blokken=[
            ("p", "Bij dieren worden vijf grote weefselgroepen onderscheiden: "
                  "<strong>epitheelweefsel</strong>, <strong>bindweefsel</strong>, "
                  "<strong>spierweefsel</strong>, <strong>zenuwweefsel</strong> en "
                  "<strong>transportweefsel</strong> zoals bloed."),
            ("p", "<strong>Epitheel</strong> <strong>bekleedt oppervlakken en holten</strong>. "
                  "<strong>Trilhaarepitheel</strong> in de luchtwegen <strong>voert slijm met stof en "
                  "kiemen naar boven af</strong>. In de dunne darm dragen de cellen "
                  "<strong>microvilli</strong>, die het <strong>opnemend oppervlak "
                  "vergroten</strong>: een <strong>darmcel</strong> heeft aan haar binnenkant "
                  "duizenden van die kleine uitsteeksels, "
                  "<strong>om meer voedingsstoffen op te nemen</strong>. De "
                  "<strong>trilhaarcellen</strong> of trilhaarepitheelcellen van de luchtwegen "
                  "<strong>duwen met hun trilharen het slijm naar boven</strong>."),
            ("p", "<strong>Bindweefsel</strong> of steunweefsel <strong>verbindt en ondersteunt "
                  "andere weefsels</strong>, en omvat onder meer <strong>kraakbeen</strong> en "
                  "bot. Door <strong>kraakbeen lopen geen bloedvaten</strong>: de "
                  "kraakbeencellen krijgen hun zuurstof door diffusie uit het vocht errond, en "
                  "daarom heelt kraakbeen zo traag. <strong>Spierweefsel</strong> kan "
                  "samentrekken; een <strong>spiercel</strong> is daarvoor <strong>langgerekt "
                  "en vol samentrekbare eiwitten</strong>, en heeft ook "
                  "<strong>mitochondria</strong> of mitochondriën <strong>in grote "
                  "hoeveelheid</strong>, want samentrekken kost energie. "
                  "<strong>Zenuwweefsel</strong> geleidt prikkels: een "
                  "<strong>zenuwcel</strong> is <strong>lang uitgerekt om een prikkel over een "
                  "grote afstand door te geven</strong>. Een <strong>weefsel</strong> bestaat "
                  "telkens uit <strong>cellen met een gelijkaardige taak</strong>, en "
                  "<strong>verschillende weefsels samen vormen een orgaan</strong>."),
            ("p", "Twee cellen zijn extreem gespecialiseerd. Een rijpe "
                  "<strong>rode bloedcel</strong> <strong>heeft geen kern, zodat er meer plaats is "
                  "voor hemoglobine</strong>. Een <strong>geslachtscel</strong> is "
                  "<strong>haploïd</strong> en heeft dus maar de helft van de chromosomen."),
        ]),
    ],
    onthoud=[
        "Groeien is delen, strekken en differentiëren.",
        "Alle cellen hebben hetzelfde DNA, maar gebruiken andere genen.",
        "Xyleem voert water omhoog, floëem verdeelt suikers.",
        "Microvilli en wortelharen doen hetzelfde: oppervlak vergroten.",
        "Een rode bloedcel heeft geen kern, een gameet is haploïd.",
    ],
)

# ───────────────────────── 3. Enzymen, transport door membranen en osmose
BUNDELS["enzymen-transport-door-membranen-en-osmose-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Enzymen, transport door membranen en osmose",
    onder="Hoe enzymen werken, en hoe stoffen een membraan passeren.",
    secties=[
        dict(kop="Wat een enzym doet", blokken=[
            ("p", "Een <strong>enzym</strong> is een <strong>eiwit dat een reactie "
                  "versnelt</strong> zonder zelf verbruikt te worden: een enzym "
                  "<strong>wordt bij de reactie niet opgebruikt</strong>. De naam eindigt bij "
                  "bijna elk enzym op de lettergreep <strong>-ase</strong>: "
                  "<strong>lactase splitst de melksuiker lactose</strong>, "
                  "<strong>catalase splitst waterstofperoxide</strong> tot water en zuurstof. Let "
                  "wel: een enzym versnelt een reactie, maar "
                  "<strong>bepaalt niet in welke richting ze verloopt</strong>."),
            ("p", "Het substraat past in het <strong>actief centrum</strong>, "
                  "<strong>de holte waarin het substraat past</strong>. Samen vormen ze het "
                  "<strong>enzym-substraatcomplex</strong>, de "
                  "<strong>tijdelijke verbinding van het enzym met zijn substraat</strong>. Het enzym "
                  "<strong>verlaagt de activeringsenergie</strong>, dus de energie die nodig is om de "
                  "reactie op gang te krijgen."),
            ("p", "Een enzym is <strong>substraatspecifiek</strong>: "
                  "<strong>het werkt maar op één soort substraat</strong>, omdat alleen dat substraat "
                  "op het actief centrum past. Enzymen zijn daarom onmisbaar bij de "
                  "<strong>spijsvertering</strong> en bij de <strong>DNA-replicatie</strong>."),
        ]),
        dict(kop="Wat een enzym sneller of trager maakt", blokken=[
            ("p", "Elk enzym heeft een <strong>temperatuursoptimum</strong>, ook "
                  "<strong>temperatuuroptimum</strong> genoemd: "
                  "<strong>de temperatuur waarbij het het snelst werkt</strong>. Daaronder gaat "
                  "het trager, daarboven <strong>denatureert</strong> het. Bij die "
                  "<strong>denaturatie gaat zijn ruimtelijke vorm verloren</strong>, dus "
                  "<strong>valt de reactiesnelheid sterk terug</strong> en werkt het niet meer. "
                  "Dat is <strong>niet omkeerbaar</strong>: kook je een stukje lever en leg je het "
                  "daarna in waterstofperoxide, dan gebeurt er niets, want "
                  "<strong>het catalase is gedenatureerd</strong>."),
            ("p", "Er is ook een <strong>pH-optimum</strong>. Pepsine in de maag werkt bij een heel "
                  "lage pH, enzymen in de dunne darm juist niet: "
                  "<strong>elk enzym heeft dus zijn eigen pH-optimum</strong>."),
            ("p", "Verhoog je de <strong>enzymconcentratie</strong>, dan "
                  "<strong>stijgt de snelheid zolang er substraat genoeg is</strong>. Verhoog je de "
                  "<strong>substraatconcentratie</strong>, dan stijgt de snelheid eerst en daarna "
                  "niet meer: <strong>de curve van de reactiesnelheid buigt af omdat alle enzymen "
                  "al bezig zijn</strong>. Die toestand, waarin "
                  "<strong>elk actief centrum van de aanwezige enzymen bezet is</strong>, heet "
                  "<strong>verzadiging</strong>."),
            ("p", "Een <strong>inhibitor</strong> <strong>remt een enzym af</strong>, bijvoorbeeld "
                  "door het actief centrum te bezetten. Een <strong>co-enzym</strong> is juist "
                  "<strong>een hulpmolecule die het enzym nodig heeft</strong>; veel vitaminen "
                  "spelen die rol."),
            ("p", "Een <strong>anabole</strong> reactie "
                  "<strong>bouwt grote moleculen op en kost energie</strong>. Een "
                  "<strong>katabole</strong> reactie breekt af en levert energie: de "
                  "<strong>celademhaling</strong> en de <strong>spijsvertering</strong> zijn "
                  "katabool."),
        ]),
        dict(kop="Passief transport", blokken=[
            ("p", "<strong>Passief transport kost de cel geen energie</strong> en volgt de "
                  "<strong>concentratiegradiënt</strong>, dus "
                  "<strong>van hoge naar lage concentratie</strong>. <strong>Diffusie</strong> is de "
                  "verspreiding van deeltjes langs die gradiënt."),
            ("p", "Deeltjes die niet zomaar door de vetlaag kunnen, gebruiken eiwitten. Een "
                  "<strong>kanaaleiwit</strong> vormt <strong>een gaatje waardoor ionen gaan</strong> en "
                  "<strong>dat open of dicht kan</strong>, een <strong>carriereiwit</strong> <strong>bindt het deeltje en "
                  "verandert daarbij van vorm</strong>. Dat laatste heet "
                  "<strong>geleide of gefaciliteerde diffusie</strong>, en het "
                  "<strong>kost de cel geen ATP</strong>. Een <strong>aquaporine</strong> is het "
                  "kanaal <strong>voor water</strong>."),
        ]),
        dict(kop="Osmose", blokken=[
            ("p", "<strong>Osmose</strong> is <strong>de diffusie van water door een "
                  "halfdoorlaatbaar membraan</strong>, "
                  "<strong>naar de kant met de hoogste concentratie</strong> opgeloste stof."),
            ("p", "Een oplossing met <strong>minder</strong> opgeloste stof dan de cel heet "
                  "<strong>hypotoon</strong>, met <strong>evenveel</strong> "
                  "<strong>isotoon</strong>, met <strong>meer</strong> "
                  "<strong>hypertoon</strong>. Een <strong>isotone</strong> omgeving heeft dus "
                  "<strong>dezelfde osmotische waarde als de cel</strong>."),
            ("p", "In een hypotone omgeving, zoals zuiver water, "
                  "<strong>stroomt er water de cel in</strong> en "
                  "<strong>kan een dierlijke cel barsten</strong>: dat is "
                  "<strong>cellyse</strong>. In een hypertone omgeving verliest ze water. Leg je "
                  "een plantencel in een sterke <strong>zoutoplossing</strong>, dan "
                  "<strong>trekt het cytoplasma met het membraan van de celwand weg</strong>, en "
                  "dat heet <strong>plasmolyse</strong>."),
            ("p", "Staat een plantencel vol water, dan duwt de vacuole tegen de celwand. Die druk "
                  "heet <strong>turgor</strong>, en <strong>daardoor staat een plant rechtop</strong>."),
        ]),
        dict(kop="Actief transport en blaasjes", blokken=[
            ("p", "<strong>Actief transport kost energie</strong> en gaat "
                  "<strong>tegen de concentratiegradiënt in</strong>. De "
                  "<strong>ATP levert daarvoor de energie</strong>. De "
                  "<strong>natrium-kaliumpomp</strong> <strong>pompt natrium naar buiten en kalium "
                  "naar binnen</strong>, en gebruikt daarvoor <strong>ATP</strong>, de energiemunt van "
                  "de cel. Een <strong>protonpomp</strong> verplaatst waterstofionen."),
            ("p", "Grote deeltjes gaan in blaasjes. <strong>Endocytose</strong> is "
                  "<strong>opnemen</strong>, <strong>exocytose</strong> is "
                  "<strong>afgeven</strong>: bij exocytose "
                  "<strong>smelt een secretieblaasje samen met het celmembraan</strong>. Het "
                  "opnemen van een vast deeltje, zoals een bacterie door een witte bloedcel, heet "
                  "<strong>fagocytose</strong>."),
        ]),
    ],
    onthoud=[
        "Een enzym verlaagt de activeringsenergie en is substraatspecifiek.",
        "Te warm betekent denatureren, en dat is onomkeerbaar.",
        "Passief gaat met de gradiënt mee en kost niets; actief kost ATP.",
        "Osmose is water dat naar de hypertone kant trekt.",
        "Lyse is barsten, plasmolyse is het membraan dat loskomt.",
    ],
)

# ───────────────────────── 4. Fotosynthese, celademhaling en gisting
BUNDELS["fotosynthese-celademhaling-en-gisting-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Fotosynthese, celademhaling en gisting",
    onder="Hoe een cel energie vastlegt en hoe ze die weer vrijmaakt.",
    secties=[
        dict(kop="De fotosynthese in het groot", blokken=[
            ("p", "De fotosynthese vat je samen als: <strong>koolstofdioxide en water geven met "
                  "lichtenergie glucose en zuurstof</strong>. De "
                  "<strong>reactievergelijking</strong> luidt: "
                  "<strong>6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂</strong>, met "
                  "<strong>C₆H₁₂O₆</strong> voor de glucose. Een organisme dat uit "
                  "<strong>anorganische stoffen</strong> zijn eigen "
                  "voedsel maakt, is <strong>autotroof</strong>."),
            ("p", "Het licht wordt opgevangen door <strong>pigmenten</strong>: "
                  "<strong>chlorofyl a</strong>, het belangrijkste, "
                  "<strong>chlorofyl b</strong> en de <strong>carotenoïden</strong>, die "
                  "<strong>licht opvangen van golflengten die chlorofyl slecht opneemt</strong>. "
                  "Dat het <strong>chlorofyl in de herfst afgebroken</strong> wordt, is waarom de "
                  "bladeren dan geel en rood worden. Een "
                  "<strong>absorptiespectrum</strong> laat aflezen <strong>welke golflengten een pigment "
                  "opneemt</strong>. Chlorofyl neemt vooral blauw en rood op en kaatst groen terug; "
                  "daarom zien bladeren er groen uit."),
            ("p", "Meer licht geeft meer fotosynthese, maar niet eindeloos: "
                  "<strong>vanaf een bepaalde lichtintensiteit stijgt de fotosynthese niet "
                  "verder</strong>, omdat een andere factor dan beperkend wordt. Zet je een "
                  "<strong>waterplant</strong> in steeds meer licht en meet je de "
                  "<strong>zuurstofproductie</strong>, dan "
                  "<strong>stijgt ze eerst en vlakt ze daarna af</strong>."),
        ]),
        dict(kop="De twee fasen van de fotosynthese", blokken=[
            ("p", "De <strong>lichtreacties</strong> gebeuren in het "
                  "<strong>thylakoïdmembraan</strong> van de chloroplast, waarin "
                  "<strong>fotosysteem I en fotosysteem II</strong> liggen. Fotosysteem II doet "
                  "eerst de <strong>splitsing van water</strong>, en die levert "
                  "<strong>zuurstofgas</strong> en <strong>elektronen</strong>; de "
                  "<strong>zuurstof die een plant afgeeft, komt dus uit dat gesplitste "
                  "water</strong>. De energie wordt vastgelegd als "
                  "<strong>ATP en NADPH</strong>."),
            ("p", "De <strong>Calvincyclus</strong>, ook de <strong>donkerreacties</strong> genoemd, "
                  "gebeurt in het <strong>stroma</strong>, de "
                  "vloeistof rond de thylakoïden. Daar wordt met die ATP en NADPH "
                  "<strong>koolstofdioxide vastgelegd in een organische molecule</strong>; dat heet "
                  "<strong>koolstoffixatie</strong>. Die fase heeft dus "
                  "<strong>geen licht rechtstreeks nodig, wel de ATP en NADPH die de lichtreacties "
                  "voor de donkerreacties aanmaken</strong>. Let op de naam: "
                  "<strong>de donkerreacties lopen niet alleen in het donker</strong>, ze lopen "
                  "ook bij volle zon. Een plant die in het donker staat, "
                  "<strong>doet trouwens nog wel aan celademhaling</strong>."),
            ("p", "Het enzym dat ATP maakt uit de protonengradiënt heet "
                  "<strong>ATP-synthase</strong>."),
        ]),
        dict(kop="De celademhaling", blokken=[
            ("p", "De <strong>aerobe celademhaling</strong> is in het groot het omgekeerde, met als "
                  "<strong>reactievergelijking C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O</strong>: "
                  "<strong>glucose en zuurstof geven koolstofdioxide, water en energie</strong>. "
                  "Ze verloopt in vier stappen."),
            ("p", "De <strong>glycolyse</strong> gebeurt in het <strong>cytoplasma</strong> en "
                  "splitst glucose tot twee moleculen <strong>pyruvaat</strong> of "
                  "<strong>pyrodruivenzuur</strong>. Daar is "
                  "<strong>geen zuurstof</strong> voor nodig."),
            ("p", "Bij de <strong>oxidatieve decarboxylatie</strong> wordt pyruvaat omgezet tot "
                  "<strong>acetyl-coA</strong>, waarbij <strong>koolstofdioxide vrijkomt</strong>."),
            ("p", "De <strong>Krebscyclus</strong> draait in de <strong>matrix</strong> van het "
                  "mitochondrion. De <strong>eindoxidaties</strong> gebeuren op de "
                  "<strong>cristae</strong>, het geplooide binnenmembraan, en leveren veruit de "
                  "meeste ATP."),
            ("p", "<strong>NAD⁺ en FAD</strong> <strong>vervoeren elektronen en waterstof</strong>. Ze "
                  "brengen die naar de eindoxidaties, waar een "
                  "<strong>protonengradiënt over het binnenmembraan</strong> de ATP-synthese "
                  "aandrijft en <strong>zuurstofgas de elektronen uiteindelijk opneemt</strong>."),
            ("p", "<strong>ATP</strong> is geen voorraad maar een werkmunt: bij "
                  "<strong>ATP-hydrolyse</strong> <strong>wordt er een fosfaatgroep afgesplitst en komt "
                  "er energie vrij</strong>. Een cel maakt dus voortdurend nieuw ATP aan en "
                  "<strong>legt er geen voorraad voor weken vooruit aan</strong>."),
        ]),
        dict(kop="Zonder zuurstof: gisting", blokken=[
            ("p", "Zonder zuurstof stopt de celademhaling na de glycolyse. Dan volgt "
                  "<strong>gisting</strong>, die <strong>per molecule glucose veel minder ATP oplevert "
                  "dan de aerobe celademhaling</strong>. Toch heeft de cel iets aan de omzetting "
                  "van het pyruvaat: <strong>zo komt NAD⁺ weer vrij voor de glycolyse</strong>, "
                  "zodat die kan blijven doorlopen. <strong>Beide gistingen verlopen zonder "
                  "zuurstof</strong>."),
            ("p", "Bij <strong>melkzuurgisting</strong>, onder meer in een spiercel die bij "
                  "<strong>zwaar werk en te weinig zuurstof</strong> zit, wordt pyruvaat tot <strong>melkzuur</strong> omgezet. Bij "
                  "<strong>alcoholische gisting</strong>, bij gist, ontstaan "
                  "<strong>ethanol en koolstofdioxide</strong>."),
            ("p", "Fotosynthese en celademhaling zijn in zekere zin "
                  "<strong>elkaars omgekeerde</strong>: "
                  "<strong>wat de ene opneemt, geeft de andere af</strong>, en "
                  "<strong>de ene bouwt op terwijl de andere afbreekt</strong>."),
        ]),
    ],
    onthoud=[
        "Fotosynthese: licht, CO₂ en water geven glucose en zuurstof.",
        "Lichtreacties in het thylakoïdmembraan, Calvincyclus in het stroma.",
        "De zuurstof van de fotosynthese komt uit het gesplitste water.",
        "Glycolyse in het cytoplasma, Krebs in de matrix, eindoxidaties op de cristae.",
        "Zonder zuurstof: gisting, met melkzuur of met alcohol.",
    ],
)

# ───────────────────────── 5. Niet-specifieke en specifieke afweer
BUNDELS["niet-specifieke-en-specifieke-afweer-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Niet-specifieke en specifieke afweer",
    onder="De drie verdedigingslijnen van het lichaam, van huid tot geheugencel.",
    secties=[
        dict(kop="Ziekteverwekkers en begrippen", blokken=[
            ("p", "Een <strong>pathogeen</strong> is een <strong>ziekteverwekker</strong>. Een "
                  "<strong>antigeen</strong> is <strong>een stof die het afweersysteem of "
                  "immuunsysteem als vreemd herkent</strong>. Dat immuunsysteem "
                  "<strong>beschermt ons tegen bacteriën en virussen</strong>, en ook "
                  "<strong>tegen eigen cellen die ontspoord zijn</strong>."),
            ("p", "Een <strong>infectie</strong> is het binnendringen en vermenigvuldigen van een "
                  "ziekteverwekker; <strong>een infectieziekte is de infectie mét "
                  "ziekteverschijnselen</strong>. De <strong>tijd tussen de besmetting en de eerste "
                  "klachten</strong> heet de <strong>incubatietijd</strong>. Wie een infectie "
                  "doormaakt, <strong>bouwt daar meestal wel bescherming tegen op</strong>."),
        ]),
        dict(kop="De eerste lijn: barrières", blokken=[
            ("p", "De eerste lijn houdt pathogenen buiten. Een <strong>fysische barrière</strong> is "
                  "bijvoorbeeld de <strong>opperhuid</strong> of een <strong>slijmvlies</strong>: "
                  "slijmvliezen <strong>beschermen ons doordat ze deeltjes opvangen in slijm en "
                  "ze afvoeren</strong>."),
            ("p", "Een <strong>chemische barrière</strong> werkt met stoffen: "
                  "<strong>lysozym in tranen en speeksel maakt de celwand van bacteriën "
                  "kapot</strong>, en maagzuur doodt het meeste wat je inslikt."),
            ("p", "Ook het <strong>microbioom</strong> of de <strong>microbiota</strong> helpt: dat is "
                  "<strong>het geheel van onschadelijke micro-organismen dat van nature op en in "
                  "ons leeft</strong>, en die eigen bacteriën "
                  "<strong>nemen de plaats en het voedsel in van indringers</strong>."),
        ]),
        dict(kop="De tweede lijn: niet-specifieke afweer", blokken=[
            ("p", "De tweede lijn is <strong>niet-specifiek</strong>: ze "
                  "<strong>werkt tegen elke indringer op dezelfde manier</strong>, en ze is er "
                  "meteen. De derde lijn is <strong>specifiek</strong>, want ze richt zich tegen "
                  "<strong>één antigeen</strong> en ze <strong>bouwt een geheugen op</strong>."),
            ("p", "De witte bloedcellen heten samen de <strong>leukocyten</strong> of "
                  "<strong>leucocyten</strong>. Een <strong>macrofaag</strong> "
                  "<strong>eet indringers op en verwerkt ze</strong>; de "
                  "<strong>neutrofiel</strong> is <strong>de eerste fagocyt die in grote aantallen "
                  "naar een ontsteking trekt</strong>. Een "
                  "<strong>natural killer cel</strong> <strong>doodt besmette of ontspoorde eigen "
                  "cellen</strong>."),
            ("p", "Bij een <strong>ontsteking</strong> zie je <strong>roodheid, warmte, zwelling en "
                  "pijn</strong>. <strong>Histamine</strong>, dat de <strong>mestcellen</strong> "
                  "vrijzetten, ook bij een <strong>allergische reactie</strong>, "
                  "<strong>verwijdt de bloedvaten en maakt "
                  "ze doorlaatbaarder</strong>, zodat er meer afweercellen ter plaatse raken."),
            ("p", "<strong>Koorts</strong> is geen defect maar een wapen: "
                  "<strong>de afweer werkt sneller en de indringer trager</strong>. In het bloed "
                  "stijgt dan ook het <strong>CRP</strong> of "
                  "<strong>C-reactief proteïne</strong>, dat daarom "
                  "<strong>gemeten wordt als teken van ontsteking</strong>."),
            ("p", "Het <strong>complementsysteem</strong> is een reeks eiwitten die "
                  "<strong>bacteriën doorboren en de afweercellen aantrekken</strong>. "
                  "<strong>Interferonen</strong> worden <strong>vrijgezet door cellen die door een "
                  "virus besmet zijn</strong> en "
                  "<strong>waarschuwen de cellen ernaast tegen een virus</strong>. "
                  "<strong>Cytokines</strong> zijn de signaalstoffen tussen afweercellen onderling: ze "
                  "<strong>geven boodschappen door tussen afweercellen</strong>."),
        ]),
        dict(kop="De derde lijn: specifieke afweer", blokken=[
            ("p", "De specifieke afweer vertrekt bij een "
                  "<strong>dendritische cel</strong>, die "
                  "<strong>een stuk van de indringer aan de lymfocyten voorstelt</strong>. Dat tonen gebeurt op <strong>MHC-moleculen</strong>: "
                  "<strong>MHC-I staat op bijna elke lichaamscel</strong>, "
                  "<strong>MHC-II alleen op de cellen die antigenen presenteren</strong>."),
            ("p", "De <strong>T-helpercel</strong> of <strong>T-helperlymfocyt</strong> is de dirigent: "
                  "ze <strong>zet de andere afweercellen aan met cytokines</strong>. Een "
                  "<strong>cytotoxische T-lymfocyt</strong> "
                  "<strong>doodt een besmette eigen cel</strong>. De <strong>T-lymfocyten</strong> "
                  "rijpen in de <strong>thymus</strong> of <strong>zwezerik</strong>."),
            ("p", "Een <strong>B-cel</strong> die geactiveerd wordt, groeit uit tot een "
                  "<strong>plasmacel</strong>, en die <strong>maakt antilichamen</strong>. "
                  "Een <strong>antilichaam</strong> <strong>klit aan het antigeen vast en maakt het "
                  "onschadelijk</strong>, en het "
                  "<strong>maakt de indringer herkenbaar voor de fagocyten</strong>. Macrofagen "
                  "maken dus géén antilichamen. Het "
                  "<strong>samenklonteren of agglutineren van antigenen door "
                  "antilichamen</strong> heet <strong>agglutinatie</strong>."),
            ("p", "Een deel van de cellen blijft bewaard als <strong>B-geheugencel</strong>. De "
                  "<strong>primaire immuunrespons duurt dagen</strong>, want "
                  "<strong>de juiste lymfocyt moet zich eerst vermenigvuldigen</strong>. De "
                  "<strong>secundaire immuunrespons verloopt sneller en krachtiger</strong>, want "
                  "<strong>er zijn al geheugencellen aanwezig en die reageren meteen</strong>: bij "
                  "een tweede ontmoeting word je vaak niet eens ziek. Zo'n geheugencel "
                  "<strong>scheidt niet onafgebroken antilichamen af</strong>; ze wacht, jaren "
                  "zelfs, tot het antigeen terugkomt. Vindt een arts in iemands bloed antilichamen "
                  "tegen een virus maar geen virus, dan heeft die "
                  "<strong>persoon het virus gehad of is ze gevaccineerd</strong>."),
            ("p", "De afweerorganen liggen verspreid. In het <strong>beenmerg</strong> worden de "
                  "witte bloedcellen gevormd, in de <strong>thymus</strong> "
                  "<strong>rijpen de T-cellen</strong>, en de <strong>lymfeknopen</strong> "
                  "<strong>filteren de lymfe en brengen afweercellen samen</strong>. Die knopen en "
                  "de <strong>milt</strong> horen bij het "
                  "<strong>lymfatisch systeem</strong>."),
        ]),
    ],
    onthoud=[
        "Eerste lijn houdt buiten, tweede lijn ruimt op, derde lijn is op maat.",
        "Niet-specifiek is meteen en voor iedereen; specifiek is traag maar onthoudt.",
        "T-helper dirigeert, cytotoxische T doodt, plasmacel maakt antilichamen.",
        "Koorts en ontsteking zijn wapens, geen defecten.",
        "Geheugencellen maken de tweede keer sneller en sterker.",
    ],
)

# ───────────────────────── 6. Immunisatie, bloedgroepen en falende afweer
BUNDELS["immunisatie-bloedgroepen-en-falende-afweer-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Immunisatie, bloedgroepen en falende afweer",
    onder="Vaccins, bloedgroepen, allergie, auto-immuunziekten en hiv.",
    secties=[
        dict(kop="Vier vormen van immunisatie", blokken=[
            ("p", "<strong>Immunisatie</strong> is <strong>het verwerven van weerstand tegen "
                  "een ziekteverwekker</strong>. Ze is <strong>actief</strong> als je "
                  "<strong>zelf antilichamen aanmaakt</strong>, en <strong>passief</strong> als "
                  "je <strong>kant-en-klare antilichamen van buitenaf krijgt</strong>; die "
                  "<strong>bescherming werkt onmiddellijk</strong>."),
            ("p", "Daarnaast is ze <strong>natuurlijk</strong> of <strong>kunstmatig</strong>. "
                  "Kruis je dat met actief en passief, dan krijg je vier vormen, elk met zijn "
                  "eigen voorbeeld."),
            ("kader", tabel(["vorm", "wat er gebeurt", "voorbeeld"],
                            [["<strong>natuurlijk actief</strong>",
                              "<strong>de ziekte doormaken</strong>",
                              "<strong>mazelen</strong> krijgen en er weerstand aan overhouden"],
                             ["<strong>kunstmatig actief</strong>",
                              "<strong>een vaccin krijgen</strong>",
                              "<strong>vaccinatie</strong>, <strong>inenting</strong> of <strong>vaccineren</strong>"],
                             ["<strong>natuurlijk passief</strong>",
                              "<strong>antilichamen via de placenta of de moedermelk</strong>",
                              "een baby die via <strong>borstvoeding</strong> beschermd is"],
                             ["<strong>kunstmatig passief</strong>",
                              "<strong>een inspuiting met antilichamen</strong>",
                              "wie <strong>gebeten</strong> is en meteen antilichamen <strong>ingespoten</strong> krijgt"]])),
            ("p", "De bescherming die een baby via <strong>borstvoeding</strong> krijgt, "
                  "<strong>verdwijnt na een tijd</strong>: ze is passief, dus het lichaam van "
                  "de baby maakt zelf niets aan."),
            ("p", "Een <strong>vaccin</strong> bevat verzwakte of dode ziekteverwekkers of "
                  "alleen een stukje ervan, dus <strong>nooit levende, volledig besmettelijke "
                  "verwekkers</strong>, zodat je <strong>geheugencellen aanmaakt zonder ziek te "
                  "worden</strong>. Passieve immunisatie werkt <strong>meteen maar "
                  "kort</strong>, want er worden geen geheugencellen gevormd."),
            ("p", "<strong>Groepsimmuniteit</strong> betekent dat er bij een hoge "
                  "<strong>vaccinatiegraad</strong> <strong>zoveel mensen immuun zijn dat de "
                  "verwekker bijna geen nieuwe gastheer meer vindt</strong>. Daardoor zijn ook "
                  "de mensen beschermd die zelf niet gevaccineerd kunnen worden."),
        ]),
        dict(kop="Bloedgroepen", blokken=[
            ("p", "Het <strong>ABO-systeem</strong> of <strong>ABO-bloedgroepensysteem</strong> "
                  "steunt op <strong>antigenen op de rode bloedcellen</strong> en op "
                  "<strong>antilichamen in het plasma</strong>. Bloedgroep A draagt antigeen A "
                  "en heeft anti-B in het plasma, B omgekeerd, <strong>AB draagt antigeen A en "
                  "B</strong> en heeft geen van beide antilichamen, <strong>O draagt geen van "
                  "beide antigenen</strong> maar heeft <strong>anti-A en anti-B</strong> in het "
                  "plasma."),
            ("p", "Daardoor is <strong>O de universele donor</strong> voor rode bloedcellen en "
                  "<strong>AB de universele ontvanger</strong>. Bij een transfusie met "
                  "<strong>incompatibel</strong> bloed <strong>klitten de rode bloedcellen "
                  "samen</strong> (<strong>agglutinatie</strong>) en <strong>gaan ze "
                  "kapot</strong>; dat <strong>kapotgaan van rode bloedcellen</strong> heet "
                  "<strong>hemolyse</strong>. Plasma van groep O mag trouwens niet zonder meer "
                  "aan iedereen gegeven worden, want <strong>het bevat anti-A en "
                  "anti-B</strong>."),
            ("p", "De <strong>resusfactor</strong> is het <strong>D-antigeen</strong>. Is dat "
                  "aanwezig, dan ben je resuspositief. Draagt een "
                  "<strong>resusnegatieve</strong> moeder een <strong>resuspositieve</strong> "
                  "kind, dan kan ze <strong>anti-D-antilichamen aanmaken</strong>. Het eerste "
                  "zo’n kind loopt meestal geen gevaar, want <strong>die antilichamen ontstaan "
                  "pas rond de bevalling</strong>; een volgend kind wel. Daarom wordt dat "
                  "<strong>resusprobleem</strong> voorkomen doordat een "
                  "<strong>anti-D-inspuiting</strong> <strong>voorkomt dat ze die "
                  "aanmaakt</strong> en beschermt zo een volgende zwangerschap."),
        ]),
        dict(kop="Als de afweer overdrijft of zich vergist", blokken=[
            ("p", "Een <strong>allergie</strong> is <strong>een overdreven reactie op een "
                  "onschuldige stof</strong>. Daarbij <strong>speelt het IgE-antilichaam de "
                  "hoofdrol</strong>: ze zetten cellen aan om <strong>histamine</strong> vrij "
                  "te geven, en dat geeft <strong>een loopneus en tranende ogen</strong> en "
                  "<strong>zwelling en jeuk van de huid</strong>. Een <strong>anafylactische "
                  "shock</strong> is <strong>een levensbedreigende allergische reactie van het "
                  "hele lichaam</strong>: ze <strong>blijft dus niet beperkt tot de huid rond "
                  "de prikplaats</strong>."),
            ("p", "Bij een <strong>auto-immuunziekte</strong> <strong>valt de afweer eigen "
                  "gezonde cellen aan</strong>. Zulke <strong>aandoeningen</strong> zijn "
                  "<strong>multiple sclerose</strong>, de <strong>ziekte van Crohn</strong> en "
                  "<strong>psoriasis</strong>. Ze worden meestal behandeld <strong>door de "
                  "afweerreactie te onderdrukken</strong>, en <strong>volledig genezen kan "
                  "meestal niet</strong>."),
        ]),
        dict(kop="Als de afweer zelf aangevallen wordt", blokken=[
            ("p", "<strong>Hiv</strong> is een <strong>retrovirus</strong>: het "
                  "<strong>schrijft zijn RNA met een enzym om naar DNA</strong> en bouwt dat in "
                  "het menselijke DNA in. Het virus valt de <strong>T-helperlymfocyt</strong> "
                  "aan, en net die cellen sturen de hele afweer aan."),
            ("p", "Wie besmet is, heet <strong>seropositief</strong>: <strong>er zijn "
                  "antilichamen tegen hiv in het bloed</strong>. Daarna volgt bij een "
                  "hiv-<strong>infectie</strong> vaak een lange <strong>chronische "
                  "fase</strong>, waarin <strong>er jarenlang weinig of geen klachten "
                  "zijn</strong> terwijl <strong>het aantal T-helpercellen traag "
                  "daalt</strong>."),
            ("p", "<strong>Aids</strong> is het eindstadium: "
                  "<strong>de afweer is zo verzwakt dat gewone kiemen gevaarlijk worden</strong>. "
                  "Met behandeling kan dat stadium jarenlang uitgesteld worden."),
        ]),
    ],
    onthoud=[
        "Actief is zelf aanmaken, passief is krijgen; natuurlijk of kunstmatig.",
        "Een vaccin geeft geheugen, antilichamen inspuiten werkt meteen maar kort.",
        "O is universele donor, AB universele ontvanger.",
        "Allergie is overdrijven, auto-immuun is zich vergissen.",
        "Hiv treft de T-helpercel, de dirigent van de afweer.",
    ],
)

# ───────────────────────── 7. Gametogenese en de hormonale regeling
BUNDELS["gametogenese-en-de-hormonale-regeling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Gametogenese en de hormonale regeling",
    onder="Hoe eicellen en zaadcellen gevormd worden, en welke hormonen dat sturen.",
    secties=[
        dict(kop="De vorming van een eicel", blokken=[
            ("p", "De eicellen rijpen in het vrouwelijk voortplantingsstelsel, en wel in de "
                  "<strong>eierstok</strong>. De <strong>franjes</strong> of "
                  "<strong>fimbriae</strong> aan de trechter van de eileider <strong>vangen de "
                  "vrijgekomen cel op</strong>."),
            ("p", "De <strong>oögenese</strong> vertrekt van de <strong>oögoniën</strong>, en "
                  "bij een <strong>meisje liggen de primaire oöcyten al bij de geboorte in de "
                  "eierstok klaar</strong>. De reeks verloopt van <strong>oögonium</strong> "
                  "over <strong>primaire oöcyt</strong> naar <strong>secundaire oöcyt</strong>. "
                  "De follikel rijpt mee: van <strong>primordiale follikel</strong> over "
                  "primaire en secundaire follikel naar de <strong>Graafse follikel</strong>, "
                  "die <strong>het verst in haar rijping</strong> is en bij de ovulatie "
                  "<strong>barst</strong>."),
            ("p", "De delingen verlopen <strong>ongelijk</strong>: één cel krijgt bijna al het "
                  "cytoplasma, de andere wordt een <strong>poollichaampje</strong> of "
                  "<strong>poolcel</strong>, <strong>een klein celletje dat het cytoplasma niet "
                  "meekrijgt</strong> en afsterft. Die ongelijke <strong>verdeling</strong> is "
                  "nuttig: zo heeft <strong>de eicel voorraad voor het begin van de "
                  "ontwikkeling</strong>, voor de eerste delingen na de bevruchting."),
            ("p", "De <strong>tweede meiotische deling wordt pas bij de bevruchting "
                  "afgewerkt</strong>. Rond de eicel liggen de <strong>zona pellucida</strong> en de "
                  "<strong>corona radiata</strong>, twee lagen die een zaadcel eerst moet "
                  "passeren."),
            ("p", "Wat van de gesprongen follikel overblijft, is het <strong>klierachtige "
                  "weefsel</strong> van het <strong>geel lichaam</strong> of <strong>corpus "
                  "luteum</strong>, dat <strong>progesteron maakt</strong>. Wordt de secundaire "
                  "oöcyt niet bevrucht, dan gaat ze binnen de dag te gronde: <strong>ze blijft "
                  "niet tot de volgende cyclus liggen</strong>."),
        ]),
        dict(kop="De cyclus en haar hormonen", blokken=[
            ("p", "De <strong>hypothalamus</strong>, de klier boven de hypofyse, geeft "
                  "<strong>GnRH</strong> af en zet daarmee de <strong>hypofyse</strong> aan. "
                  "Die maakt <strong>FSH</strong>, dat in de eerste <strong>helft</strong> van "
                  "de cyclus <strong>de follikels laat rijpen</strong> en ze <strong>oestrogeen "
                  "laat maken</strong>."),
            ("p", "<strong>Oestrogeen</strong> <strong>laat in de folliculaire fase het "
                  "baarmoederslijmvlies opbouwen</strong>. Halverwege de cyclus volgt een "
                  "<strong>plotse piek van LH</strong>, het <strong>luteïniserend "
                  "hormoon</strong>, en die <strong>lokt de ovulatie uit</strong>."),
            ("p", "Daarna begint de <strong>luteale fase</strong>: het geel lichaam maakt "
                  "progesteron, dat het slijmvlies op peil houdt. Komt er geen bevruchting, dan "
                  "sterft het geel lichaam af. <strong>Het progesteron zakt dan juist</strong>, "
                  "en daardoor volgt de menstruatie."),
            ("p", "De regeling werkt met <strong>negatieve feedback</strong>: een hoge "
                  "<strong>concentratie</strong> oestrogeen en progesteron <strong>remt de "
                  "afgifte van FSH en LH af</strong>, dus <strong>remt het product zijn eigen "
                  "aanmaak</strong>. Bij een zwangerschap houdt <strong>hCG</strong> het geel "
                  "lichaam in stand, en op dat hormoon reageert een zwangerschapstest."),
        ]),
        dict(kop="De vorming van zaadcellen", blokken=[
            ("p", "De zaadcellen worden gevormd in de <strong>zaadbuisjes</strong> van de "
                  "teelbal. Die <strong>teelballen hangen buiten de buikholte</strong>, in de "
                  "<strong>balzak</strong>, want <strong>daar is het een paar graden "
                  "koeler</strong>: de spermatogenese verloopt het best enkele graden onder de "
                  "lichaamstemperatuur."),
            ("p", "De <strong>cellen van Sertoli</strong> of <strong>Sertolicellen</strong> "
                  "<strong>voeden en ondersteunen de rijpende zaadcellen</strong>. De "
                  "<strong>cellen van Leydig</strong> liggen ertussen en <strong>maken "
                  "testosteron</strong>."),
            ("p", "De reeks loopt van <strong>spermatogonium</strong> over primaire en "
                  "secundaire spermatocyt naar <strong>spermatide</strong> en ten slotte "
                  "<strong>spermatozoïde</strong>. Anders dan bij de eicel levert één meiose "
                  "hier <strong>vier bruikbare zaadcellen</strong> op: <strong>uit één "
                  "voorlopercel komt één eicel maar vier zaadcellen</strong>."),
            ("p", "Een zaadcel bestaat uit een kop met het <strong>acrosoom</strong>, een "
                  "blaasje met <strong>enzymen om door de lagen rond de eicel te "
                  "geraken</strong>, een <strong>middenstuk vol mitochondriën of mitochondria "
                  "voor de energie</strong>, en een <strong>flagel</strong>, "
                  "<strong>flagellum</strong> of zweepstaart om te bewegen. Vindt een arts "
                  "weinig beweeglijke zaadcellen in een staal, dan werkt vooral <strong>dat "
                  "middenstuk met zijn mitochondria slecht</strong>."),
            ("p", "De <strong>zaadblaasjes</strong> en de <strong>prostaatklier</strong> zijn "
                  "de klieren die het vocht leveren waarin de zaadcellen zwemmen. Het "
                  "<strong>voorvocht</strong> uit de <strong>klieren van Cowper</strong> maakt "
                  "de urinebuis minder zuur en <strong>kan al zaadcellen bevatten</strong>."),
            ("p", "Ook bij de man stuurt de hypofyse: <strong>LH zet de cellen van Leydig "
                  "aan</strong> en FSH werkt via de cellen van Sertoli. Het testosteron dat die "
                  "maken, <strong>houdt de spermatogenese op gang</strong> en <strong>vormt de "
                  "secundaire geslachtskenmerken</strong>. <strong>Inhibine</strong> "
                  "<strong>remt de FSH-afgifte af</strong>, opnieuw via negatieve feedback. Er "
                  "is bij de man <strong>geen cyclus</strong> van 28 dagen zoals de "
                  "eicelrijping: de productie loopt doorlopend, en de hormonen <strong>dalen op "
                  "latere leeftijd traag</strong>, niet plots zoals bij de vrouw in de "
                  "<strong>menopauze</strong>."),
            ("p", "Een <strong>spermastaal</strong> toont het aantal, de vorm en de beweeglijkheid "
                  "van de zaadcellen. Elke gameet, bij man en vrouw, draagt "
                  "<strong>23 chromosomen</strong>."),
        ]),
    ],
    onthoud=[
        "Eén meiose geeft bij de vrouw één eicel, bij de man vier zaadcellen.",
        "FSH laat rijpen, de LH-piek lokt de ovulatie uit.",
        "Het geel lichaam maakt progesteron; hCG houdt het in stand.",
        "Acrosoom om binnen te dringen, middenstuk voor energie, flagel om te zwemmen.",
        "Negatieve feedback: een hoog hormoonpeil remt zijn eigen aansturing af.",
    ],
)

# ───────────────────────── 8. Bevruchting, embryo en foetus
BUNDELS["bevruchting-embryo-en-foetus-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bevruchting, embryo en foetus",
    onder="Van zaadcel tot geboorte, en wat de ontwikkeling kan storen.",
    secties=[
        dict(kop="De bevruchting", blokken=[
            ("p", "De bevruchting gebeurt in het vrouwelijk voortplantingsstelsel <strong>in de "
                  "eileider</strong>, meestal in het eerste derde ervan. De eicel is na de "
                  "ovulatie <strong>ongeveer een dag bevruchtbaar</strong>; zaadcellen houden "
                  "het drie tot vijf dagen uit."),
            ("p", "Onderweg moeten de zaadcellen barrières <strong>overwinnen</strong>: "
                  "<strong>het zure milieu van de vagina</strong> en <strong>de slijmprop van "
                  "de baarmoederhals</strong>. Van de miljoenen blijven er enkele honderden "
                  "over."),
            ("p", "Bij de <strong>acrosoomreactie</strong> <strong>breekt het blaasje op de kop van "
                  "de zaadcel open</strong> en komen de enzymen vrij die een weg banen door de "
                  "corona radiata en de zona pellucida."),
            ("p", "Zodra er één zaadcel binnen is, volgt de <strong>corticale reactie</strong>: die "
                  "<strong>belet dat een tweede zaadcel binnendringt</strong>, doordat er een "
                  "<strong>bevruchtingsmembraan</strong> gevormd wordt."),
            ("p", "Bij de <strong>amfimixie</strong> <strong>smelten de twee kernen samen</strong>. "
                  "Vanaf dat moment is er één diploïde cel: de <strong>zygote</strong>, "
                  "<strong>de bevruchte eicel met 46 chromosomen</strong>."),
        ]),
        dict(kop="Van zygote tot kiemschijf", blokken=[
            ("p", "De <strong>klievingsdelingen</strong> volgen snel op elkaar: "
                  "<strong>de cellen delen zonder te groeien</strong>, dus "
                  "<strong>het geheel wordt niet groter</strong> en de cellen worden kleiner. De "
                  "losse cellen heten <strong>blastomeren</strong>."),
            ("p", "Zo ontstaat eerst de <strong>morula</strong>, een compact bolletje, en daarna de "
                  "<strong>blastula</strong> of <strong>blastocyst</strong>, met een holte. Daarin "
                  "wordt de <strong>embryoblast</strong> of <strong>kiemknop</strong> het embryo, "
                  "terwijl de <strong>trofoblast</strong> de buitenlaag vormt."),
            ("p", "De <strong>innesteling</strong> gebeurt <strong>ongeveer een week na de "
                  "bevruchting</strong>, rond dag zes of zeven, dus <strong>lang voor er een "
                  "maand om is</strong>. De trofoblast maakt <strong>lytische enzymen</strong> "
                  "en dringt daarmee <strong>in het baarmoederslijmvlies</strong> binnen."),
            ("p", "Uit de kiemknop groeit eerst een <strong>tweebladige kiemschijf</strong> "
                  "(epiblast en hypoblast). Bij de <strong>gastrulatie</strong> "
                  "<strong>verplaatsen cellen zich en ontstaat er een derde kiemblad</strong>, "
                  "zodat er een <strong>driebladige kiemschijf</strong> is met "
                  "<strong>ectoderm, mesoderm en endoderm</strong>."),
            ("p", "Uit het <strong>ectoderm</strong> komen de <strong>huid en het "
                  "zenuwstelsel</strong>, uit het <strong>mesoderm</strong> de "
                  "<strong>spieren, het skelet en de bloedvaten</strong>, uit het "
                  "<strong>endoderm</strong> de darm en de longen. Dat aanleggen van organen heet "
                  "<strong>organogenese</strong>."),
        ]),
        dict(kop="Embryo, foetus en placenta", blokken=[
            ("p", "De eerste acht weken spreekt men van een <strong>embryo</strong>; "
                  "<strong>vanaf ongeveer de negende week</strong> van een "
                  "<strong>foetus</strong>. Die eerste acht weken zijn de <strong>gevoeligste "
                  "periode</strong>, want <strong>dan worden alle organen aangelegd</strong>. "
                  "Het hart begint al <strong>rond de derde of vierde week</strong> te kloppen, "
                  "dus <strong>niet pas in de derde maand</strong>."),
            ("p", "Het embryo ligt in <strong>vruchtwater</strong> in de amnionholte; dat water "
                  "<strong>beschermt tegen schokken</strong> en laat vrij bewegen."),
            ("p", "De <strong>placenta</strong>, in gewone taal de <strong>moederkoek</strong>, "
                  "<strong>geeft voedingsstoffen en zuurstof door</strong> en <strong>voert de "
                  "afvalstoffen van het kind af</strong>. Het bloed van moeder en kind "
                  "<strong>komt daarbij niet rechtstreeks samen</strong>: ze stromen langs "
                  "elkaar, gescheiden door de <strong>placentabarrière</strong>."),
            ("p", "In de navelstreng lopen <strong>twee slagaders en één ader</strong>: de "
                  "slagaders brengen zuurstofarm bloed naar de placenta, de ader brengt "
                  "zuurstofrijk bloed terug."),
        ]),
        dict(kop="De geboorte", blokken=[
            ("p", "De bevalling verloopt in vier fasen: <strong>indaling, ontsluiting, uitdrijving "
                  "en nageboorte</strong>. Bij de <strong>ontsluiting</strong> "
                  "<strong>opent de baarmoederhals zich</strong> tot ongeveer tien centimeter; dat "
                  "is de langste fase."),
            ("p", "Het <strong>breken van de vruchtvliezen</strong> betekent dat "
                  "<strong>het vruchtwater wegvloeit</strong>. De <strong>nageboorte</strong> is "
                  "<strong>de fase waarin de placenta eruit komt</strong>; blijft er een stukje "
                  "achter, dan geeft dat bloedverlies en infectiegevaar."),
        ]),
        dict(kop="Wat de ontwikkeling kan storen", blokken=[
            ("p", "Een <strong>echografie</strong> werkt met <strong>geluidsgolven</strong> en "
                  "is niet invasief. Een <strong>vruchtwaterpunctie</strong> en een "
                  "<strong>vlokkentest</strong> <strong>halen cellen van het kind weg</strong> "
                  "en geven dus een klein risico, maar leveren wel het karyogram. Een "
                  "niet-invasieve <strong>prenatale</strong> test onderzoekt <strong>DNA van "
                  "het kind dat in het bloed van de moeder zit</strong>. Elk "
                  "<strong>prenataal</strong> onderzoek heeft zijn <strong>beperking</strong>: "
                  "<strong>het vindt niet elke aandoening</strong>."),
            ("p", "Een <strong>teratogene stof</strong> is <strong>een stof die een afwijking "
                  "bij een embryo kan veroorzaken</strong>. <strong>Alcohol</strong> gaat vlot "
                  "door de placenta en kan <strong>een lager geboortegewicht</strong> en "
                  "<strong>een blijvende ontwikkelingsachterstand</strong> geven; er is geen "
                  "veilige ondergrens bekend. <strong>Roken</strong> is schadelijk omdat "
                  "<strong>het kind minder zuurstof krijgt</strong>."),
            ("p", "<strong>Foliumzuur</strong> wordt een zwangere <strong>aangeraden</strong> "
                  "omdat het <strong>de kans op een open rug verkleint</strong>; het wordt het "
                  "best al voor de zwangerschap genomen. <strong>Matig bewegen is "
                  "goed</strong>, ook tijdens de zwangerschap."),
            ("p", "Uit de omgeving kunnen <strong>zware metalen zoals lood</strong>, "
                  "<strong>hormoonverstorende stoffen</strong>, pesticiden en microplastics de "
                  "placenta halen."),
            ("p", "Ook ziekteverwekkers tellen mee. <strong>Rauw vlees</strong> wordt gemeden "
                  "<strong>om toxoplasmose te vermijden</strong>, en tegen het "
                  "<strong>rubellavirus</strong> of <strong>rodehondvirus</strong>, dat "
                  "<strong>rode hond</strong> veroorzaakt, worden <strong>meisjes</strong> "
                  "vooraf gevaccineerd, om hun latere zwangerschap te beschermen. Ook het "
                  "zikavirus en het cytomegalovirus kunnen het kind treffen."),
        ]),
    ],
    onthoud=[
        "Bevruchting in de eileider, innesteling een week later.",
        "Klievingsdelingen maken meer cellen, niet meer massa.",
        "Ectoderm geeft huid en zenuwen, mesoderm spier en bot, endoderm darm en longen.",
        "In de placenta raken de twee bloedsomlopen elkaar niet.",
        "De eerste acht weken zijn de gevoeligste: dan worden de organen aangelegd.",
    ],
)

# ───────────────────────── 9. Vruchtbaarheid regelen en behandelen
BUNDELS["vruchtbaarheid-regelen-en-behandelen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vruchtbaarheid regelen en behandelen",
    onder="De methoden om de vruchtbaarheid te regelen, en wat er bij een kinderwens kan helpen.",
    secties=[
        dict(kop="Natuurlijke methoden", blokken=[
            ("p", "De natuurlijke methoden berusten op <strong>het mijden van de vruchtbare "
                  "dagen</strong>. De <strong>kalendermethode</strong> rekent met de lengte van de "
                  "vorige cycli, de <strong>temperatuurmethode</strong> volgt de lichte stijging van "
                  "de lichaamstemperatuur na de ovulatie, en de "
                  "<strong>ovulatiemethode</strong> volgt het slijm van de baarmoederhals."),
            ("p", "Ze zijn <strong>minder betrouwbaar omdat een cyclus kan verschuiven</strong> "
                  "door ziekte of stress. Er komt geen hormoon en geen barrière aan te pas, en "
                  "ze laten geen <strong>sporen</strong> na."),
        ]),
        dict(kop="Barrièremiddelen", blokken=[
            ("p", "Een <strong>condoom</strong> of <strong>mannencondoom</strong> <strong>houdt "
                  "de zaadcellen tegen</strong>. Het <strong>vrouwencondoom</strong> wordt voor "
                  "de gemeenschap in de vagina gebracht en bekleedt de wand."),
            ("p", "Alleen de condooms <strong>beschermen ook tegen soa's</strong>, want alleen zij "
                  "vormen een echte barrière tussen de slijmvliezen. Hormonale middelen en "
                  "spiraaltjes doen dat niet."),
            ("p", "Het <strong>pessarium</strong> of <strong>diafragma</strong> is "
                  "<strong>een kapje voor de baarmoederhals</strong> en wordt samen met een "
                  "<strong>zaaddodend middel</strong> gebruikt. Zo'n middel is "
                  "<strong>alleen betrouwbaar samen met een barrièremiddel</strong>."),
        ]),
        dict(kop="Hormonale methoden en spiraaltjes", blokken=[
            ("p", "De <strong>combinatiepil</strong> bevat oestrogeen en progestageen en "
                  "<strong>houdt de eisprong tegen</strong>: ze <strong>onderdrukt de piek van "
                  "het luteïniserend hormoon die de ovulatie uitlokt</strong>, en zonder die "
                  "piek geen ovulatie. De <strong>minipil</strong> bevat <strong>alleen een "
                  "progestageen</strong>, dus geen oestrogeen naast het "
                  "<strong>progesteron</strong>achtige hormoon, en moet heel regelmatig genomen "
                  "worden."),
            ("p", "Ook de <strong>hormoonpleister</strong>, de vaginale ring, de "
                  "<strong>prikpil</strong>, het <strong>hormoonimplantaat</strong> en het "
                  "hormoonspiraal werken met hormonen. Een implantaat <strong>werkt jaren "
                  "zonder dagelijkse inname</strong>, en dat is tegenover de pil een "
                  "<strong>voordeel</strong> voor de betrouwbaarheid in de praktijk; het "
                  "<strong>nadeel</strong> is dat je er niet zelf mee kan stoppen."),
            ("p", "Het <strong>koperspiraal</strong> <strong>werkt zonder hormoon</strong>: koper "
                  "maakt de baarmoeder ongeschikt voor zaadcellen en innesteling. Een spiraaltje "
                  "<strong>moet door een arts geplaatst worden</strong>."),
            ("p", "Bij een <strong>sterilisatie</strong> worden de zaadleiders of de eileiders "
                  "<strong>doorgeknipt</strong> of onderbroken; bij een man heet die "
                  "<strong>ingreep</strong> een <strong>vasectomie</strong>. Bij een man "
                  "<strong>blijft de testosteronproductie gewoon doorgaan</strong>; alleen de "
                  "weg naar buiten is afgesloten."),
        ]),
        dict(kop="Noodanticonceptie en betrouwbaarheid", blokken=[
            ("p", "<strong>Noodanticonceptie</strong> is <strong>een middel na onbeschermd "
                  "vrijen</strong>, zo snel mogelijk genomen. De "
                  "<strong>morning-afterpil</strong> werkt vooral "
                  "<strong>door de ovulatie uit te stellen</strong>; ze "
                  "<strong>voorkomt</strong> dus een zwangerschap. De "
                  "<strong>abortuspil</strong> <strong>beëindigt</strong> een bestaande "
                  "zwangerschap, onder medisch toezicht. Ook een noodspiraaltje bestaat."),
            ("p", "Bij elke methode hoort een <strong>betrouwbaarheid</strong>, en die ligt in de "
                  "praktijk lager dan op papier, <strong>omdat verkeerd gebruik ze "
                  "verlaagt</strong>."),
        ]),
        dict(kop="Bij een kinderwens", blokken=[
            ("p", "Bij <strong>kunstmatige inseminatie</strong> wordt "
                  "<strong>sperma in de baarmoeder gebracht</strong>, rond de ovulatie; de "
                  "bevruchting gebeurt dus nog in het lichaam. <strong>KI</strong> gebruikt sperma "
                  "van de partner, bij <strong>KID</strong> <strong>komt het sperma van een "
                  "donor</strong>."),
            ("p", "Bij de <strong>techniek</strong> <strong>IVF</strong> of "
                  "<strong>in-vitrofertilisatie</strong> worden eicel en zaadcellen "
                  "<strong>buiten het lichaam samengebracht</strong>. Daarvoor worden de "
                  "eierstokken <strong>hormonaal gestimuleerd</strong>, zodat er meerdere "
                  "eicellen rijpen. Bij <strong>ICSI</strong> wordt <strong>één zaadcel in de "
                  "eicel gespoten</strong>, wat helpt als de zaadcellen te weinig beweeglijk "
                  "zijn."),
            ("p", "Bij <strong>in-vitromaturatie</strong> worden "
                  "<strong>onrijpe eicellen buiten het lichaam gerijpt</strong>, met minder of geen "
                  "stimulatie. <strong>Eiceldonatie</strong> komt in beeld "
                  "<strong>als de vrouw zelf geen bruikbare eicellen heeft</strong>."),
            ("p", "Meestal worden <strong>niet alle embryo's tegelijk geplaatst</strong>, "
                  "<strong>om een meerlingzwangerschap te vermijden</strong>. Een "
                  "<strong>vruchtbaarheidsbehandeling</strong> <strong>lukt zelden vanaf de "
                  "eerste poging</strong>, dus zeker niet altijd."),
            ("p", "Een <strong>spermaonderzoek</strong> of <strong>spermogram</strong> kijkt "
                  "naar het aantal, de vorm en de beweeglijkheid van de zaadcellen. Zo’n "
                  "onderzoek gebeurt bij beide partners van een <strong>koppel</strong>, want "
                  "de oorzaak <strong>speelt bij elk van beiden</strong> mee. Elke gezonde "
                  "gameet draagt daarbij <strong>drieëntwintig chromosomen</strong>."),
        ]),
        dict(kop="Wat de vruchtbaarheid verlaagt", blokken=[
            ("p", "<strong>Roken</strong> en veel <strong>drinken</strong> van alcohol "
                  "<strong>verlagen</strong> het aantal en de kwaliteit van de zaadcellen; "
                  "drugs doen dat ook. Dat zijn dus invloeden van het eigen "
                  "<strong>gedrag</strong>. <strong>Overgewicht verstoort het hormonale "
                  "evenwicht</strong>, bij mannen en bij vrouwen. <strong>Langdurige stress kan "
                  "de cyclus verstoren</strong> via de hypothalamus en de hypofyse."),
            ("p", "<strong>Niet alleen de leeftijd van de vrouw telt</strong>: ook bij een man "
                  "daalt de kwaliteit van het sperma met de jaren. Een "
                  "<strong>kankerbehandeling</strong> kan de geslachtscellen "
                  "<strong>aantasten</strong>, want ze <strong>raakt ook de snel delende "
                  "cellen</strong>, waardoor sperma of eierstokweefsel soms vooraf bewaard "
                  "wordt."),
            ("p", "Van buitenaf, uit het <strong>milieu</strong>, kunnen <strong>zware "
                  "metalen</strong>, <strong>bepaalde medicijnen</strong>, pesticiden en "
                  "<strong>hormoonverstorende stoffen</strong> of hormoonverstoorders ingrijpen "
                  "en zo de vruchtbaarheid <strong>verlagen</strong>; die laatste "
                  "<strong>binden op dezelfde receptoren als echte hormonen</strong>."),
        ]),
    ],
    onthoud=[
        "Alleen condooms beschermen ook tegen soa's.",
        "De pil houdt de LH-piek tegen, dus de ovulatie.",
        "De morning-afterpil voorkomt, de abortuspil beëindigt.",
        "IVF bevrucht buiten het lichaam, ICSI spuit één zaadcel in.",
        "Roken, alcohol, overgewicht, stress en leeftijd tellen bij beide partners.",
    ],
)

# ───────────────────────── 10. DNA, RNA en de replicatie
BUNDELS["dna-rna-en-de-replicatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="DNA, RNA en de replicatie",
    onder="De bouw van het erfelijk materiaal en hoe het gekopieerd wordt.",
    secties=[
        dict(kop="De bouwstenen", blokken=[
            ("p", "Een <strong>nucleotide</strong> bestaat uit drie delen: <strong>een suiker, "
                  "een fosfaatgroep en een stikstofbase</strong>. Hetzelfde geheel "
                  "<strong>zonder fosfaatgroep</strong> heet een <strong>nucleoside</strong>. "
                  "Nucleotiden aan elkaar vormen een <strong>nucleïnezuur</strong>; de twee "
                  "<strong>nucleïnezuren</strong> zijn <strong>DNA en RNA</strong>."),
            ("p", "In DNA staat <strong>A tegenover T en C tegenover G</strong>. Die vaste "
                  "koppels heten de <strong>complementariteit</strong>. Samen vormen ze de "
                  "<strong>dubbele helix</strong>, en ze worden bijeengehouden door "
                  "<strong>waterstofbruggen tussen de basen</strong>: twee tussen A en T, drie "
                  "tussen C en G."),
            ("p", "De twee strengen lopen <strong>in tegengestelde richting</strong>; dat is de "
                  "<strong>antiparallelle oriëntatie</strong>, met een <strong>5'-einde</strong> "
                  "tegenover een <strong>3'-einde</strong>."),
            ("p", "RNA verschilt op drie punten: het heeft <strong>ribose</strong> waar DNA "
                  "<strong>desoxyribose</strong> heeft (één OH-groep meer), het heeft "
                  "<strong>uracil</strong> of uraciel waar DNA <strong>thymine</strong> heeft, "
                  "en het is meestal <strong>enkelstrengig</strong>."),
            ("p", "Van een gen wordt maar één streng als voorbeeld gelezen: de "
                  "<strong>antisense-streng</strong>, ook <strong>matrijs</strong>, "
                  "<strong>gietvorm</strong> of <strong>template</strong> genoemd, want ze "
                  "dient als mal om te <strong>kopiëren</strong>. Het RNA dat daarvan gemaakt "
                  "wordt, is gelijk aan de <strong>sense-streng</strong> of coderende streng, "
                  "met U in plaats van T."),
        ]),
        dict(kop="Van DNA tot chromosoom", blokken=[
            ("p", "Het DNA wikkelt rond <strong>histonen</strong>, kleine <strong>positief "
                  "geladen eiwitten</strong>. Acht ervan vormen een <strong>octameer</strong>, "
                  "en <strong>DNA rond acht histonen</strong> heet een "
                  "<strong>nucleosoom</strong>. Zo zit het DNA rond die groepjes "
                  "<strong>gewonden</strong>: het <strong>windt</strong> zich rond het "
                  "octameer, en die kralenketting rolt verder op tot een "
                  "<strong>chromatinevezel</strong>."),
            ("p", "<strong>Euchromatine</strong> ligt <strong>losser en wordt gelezen</strong>; "
                  "<strong>heterochromatine</strong> is sterk <strong>gecondenseerd</strong> en komt "
                  "nauwelijks tot expressie."),
            ("p", "Een chromosoom wordt pas zichtbaar <strong>als het chromatine sterk "
                  "condenseert</strong>, dus tijdens een celdeling; in de interfase is het "
                  "<strong>losgerold</strong> en zie je enkel chromatine. De insnoering heet "
                  "het <strong>centromeer</strong>; daarop ligt het "
                  "<strong>kinetochoor</strong>, <strong>waar de trekdraden "
                  "aangrijpen</strong>."),
            ("p", "Een <strong>karyogram</strong> of <strong>karyotype</strong> is <strong>een "
                  "geordende foto van alle chromosomen van een cel</strong>. De mens heeft 22 "
                  "paar <strong>autosomen</strong> en één paar <strong>heterosomen</strong> of "
                  "geslachtschromosomen, die <strong>het geslacht bepalen</strong>. Het "
                  "verschil tussen een <strong>autosoom</strong> en een "
                  "<strong>heterosoom</strong> zit dus in dat ene punt: <strong>een heterosoom "
                  "bepaalt het geslacht</strong>, een autosoom niet."),
            ("p", "<strong>Homologe chromosomen</strong> <strong>dragen dezelfde genen op "
                  "dezelfde plaats</strong>, de ene van de moeder en de andere van de vader, "
                  "maar <strong>niet noodzakelijk dezelfde allelen</strong>. De plaats van een "
                  "gen heet de <strong>locus</strong>. Een lichaamscel is "
                  "<strong>diploïd</strong> met 46 chromosomen, een gameet "
                  "<strong>haploïd</strong> met 23: een <strong>eicel</strong> of zaadcel "
                  "draagt er dus de helft van."),
        ]),
        dict(kop="De replicatie", blokken=[
            ("p", "Het DNA wordt gekopieerd in de <strong>S-fase van de interfase</strong>. Daarna "
                  "heeft elk chromosoom twee <strong>zusterchromatiden</strong> met "
                  "<strong>dezelfde informatie</strong>."),
            ("p", "Het <strong>enzym</strong> <strong>helicase</strong> <strong>verbreekt de "
                  "waterstofbruggen en scheidt de strengen</strong>, en zo ontstaat de "
                  "<strong>replicatievork</strong>, <strong>de plaats waar de twee strengen "
                  "uiteenwijken</strong>. <strong>Topoisomerase</strong> <strong>haalt de "
                  "spanning uit het DNA dat ervoor te strak opgewonden raakt</strong>. De "
                  "<strong>ssbp's</strong>, een <strong>afkorting</strong> van single strand "
                  "binding proteins, <strong>houden de losgekomen strengen open</strong>."),
            ("p", "Het <strong>enzym</strong> <strong>primase</strong> <strong>legt een kort "
                  "stukje RNA als beginpunt</strong> dat als aanhechting "
                  "<strong>dient</strong>, want <strong>DNA-polymerase</strong> kan niet uit "
                  "het niets starten. Dat polymerase <strong>hangt nucleotiden aan van 5' naar "
                  "3'</strong>: het blijft nieuwe nucleotiden <strong>aanhangen</strong> aan "
                  "het vrije uiteinde."),
            ("p", "Daardoor verloopt het op de twee strengen anders. De <strong>leading "
                  "strand</strong> <strong>loopt mee met de vork</strong> en wordt <strong>in "
                  "één stuk doorgebouwd</strong>. De <strong>lagging strand</strong> loopt "
                  "tegen de beweging in en wordt <strong>in stukjes</strong> gebouwd: de "
                  "<strong>Okazaki-fragmenten</strong> of okazakifragmenten. "
                  "<strong>Ligase</strong> <strong>plakt die stukjes aan elkaar</strong>."),
            ("p", "De <strong>RNA-primers worden achteraf door DNA vervangen</strong> en het gat "
                  "wordt gedicht. De replicatie start <strong>op honderden plaatsen per "
                  "chromosoom</strong> tegelijk, anders zou het dagen duren."),
            ("p", "Elke nieuwe molecule bestaat uit <strong>één oude en één nieuwe "
                  "streng</strong>, dus uit een <strong>ouderlijke of oorspronkelijke "
                  "moederstreng</strong>, die als mal <strong>diende</strong>, en een "
                  "dochterstreng. Daarom heet de replicatie <strong>semiconservatief</strong>. "
                  "Het resultaat zijn <strong>twee identieke DNA-moleculen</strong>, want "
                  "<strong>de basenparen passen maar op één manier</strong> en "
                  "<strong>polymerase kijkt zijn eigen werk nauwkeurig na</strong>."),
            ("p", "Zonder replicatie zou elke dochtercel maar de helft van de informatie "
                  "krijgen: <strong>elke dochtercel heeft een volledige set nodig</strong>. Zo "
                  "<strong>deelt</strong> een cel zonder informatie te verliezen. Een "
                  "<strong>prokaryoot</strong> heeft geen kern en repliceert haar ringvormige "
                  "<strong>nucleïnezuur</strong> <strong>vrij in het cytoplasma</strong>."),
        ]),
    ],
    onthoud=[
        "Nucleotide = suiker + fosfaat + base; zonder fosfaat is het een nucleoside.",
        "A bij T, C bij G; de strengen lopen antiparallel.",
        "RNA heeft ribose en uracil en is meestal enkelstrengig.",
        "Helicase opent, primase start, polymerase bouwt 5' naar 3', ligase plakt.",
        "Semiconservatief: elke kopie heeft één oude en één nieuwe streng.",
    ],
)

# ───────────────────────── 11. De celcyclus, mitose en meiose
BUNDELS["de-celcyclus-mitose-en-meiose-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De celcyclus, mitose en meiose",
    onder="De twee celdelingen naast elkaar, en wat ze voor een organisme betekenen.",
    secties=[
        dict(kop="De celcyclus", blokken=[
            ("p", "De celcyclus bestaat uit <strong>de interfase en de M-fase</strong>. De "
                  "<strong>interfase</strong> is <strong>de hele periode tussen twee "
                  "celdelingen</strong> en duurt veel langer dan de deling zelf."),
            ("p", "In de <strong>G1-fase</strong> <strong>groeit de cel en maakt ze "
                  "eiwitten</strong>. In de <strong>S-fase</strong> wordt "
                  "<strong>het DNA gekopieerd</strong>. In de <strong>G2-fase</strong> "
                  "<strong>bereidt de cel de deling voor en keurt ze het DNA</strong>."),
            ("p", "De <strong>G0-fase</strong> is <strong>een rusttoestand buiten de "
                  "celcyclus</strong>. Zenuwcellen en spiercellen blijven daar hun hele leven in, "
                  "een levercel kan er weer uit komen."),
            ("p", "Op de <strong>controlepunten</strong> wordt nagekeken "
                  "<strong>of het DNA onbeschadigd is</strong> en "
                  "<strong>of de cel groot genoeg is</strong>. Een cel met beschadigd DNA gaat beter "
                  "niet in deling, want <strong>de fout wordt dan aan alle dochtercellen "
                  "doorgegeven</strong>."),
        ]),
        dict(kop="De mitose", blokken=[
            ("p", "De mitose verloopt in vier fasen: <strong>profase, metafase, anafase en "
                  "telofase</strong>."),
            ("p", "In de <strong>profase</strong> <strong>condenseren de chromosomen en "
                  "verdwijnt het kernmembraan</strong>, en wordt de "
                  "<strong>spoelfiguur</strong> opgebouwd, die <strong>uit microtubuli</strong> "
                  "bestaat. In de <strong>metafase</strong> gaan de chromosomen op het "
                  "<strong>evenaarsvlak</strong> of <strong>equatorvlak</strong> staan, waar de "
                  "trekdraden op de centromeren aangrijpen."),
            ("p", "In de <strong>anafase</strong> <strong>gaan de zusterchromatiden naar de "
                  "polen</strong>, getrokken door de trekdraden. In de <strong>telofase</strong> "
                  "<strong>vormt zich rond elke groep een nieuw kernmembraan</strong>."),
            ("p", "Daarna volgt de <strong>cytokinese</strong>, <strong>het verdelen van het "
                  "cytoplasma</strong>. Bij een dierlijke cel knijpt het membraan toe; "
                  "<strong>bij een plant ontstaat er een celplaat</strong>, want een celwand kan "
                  "niet toeknijpen."),
            ("p", "Eén mitose levert <strong>twee</strong> dochtercellen op met "
                  "<strong>evenveel chromosomen als de moedercel</strong>, en ze zijn "
                  "<strong>erfelijk gelijk</strong>. De mitose dient in ons "
                  "<strong>lichaam</strong> om te <strong>groeien</strong> en om "
                  "<strong>beschadigd weefsel te herstellen</strong>. Aan het begin heeft elk "
                  "chromosoom <strong>twee chromatiden</strong>, en onder de "
                  "<strong>microscoop</strong> zie je ze als <strong>losse staafjes</strong>."),
        ]),
        dict(kop="De meiose", blokken=[
            ("p", "De meiose gebeurt bij de mens <strong>alleen in de eierstokken en de "
                  "teelballen</strong> en levert als <strong>resultaat vier volledige haploïde "
                  "cellen</strong> op: de <strong>gameten</strong>, ook geslachtscellen of "
                  "voortplantingscellen genoemd."),
            ("p", "In <strong>meiose I</strong> <strong>gaan de homologe chromosomen uit "
                  "elkaar</strong>. Dat is wat in een mitose nooit gebeurt, en daarom heet meiose I "
                  "de <strong>reductiedeling</strong>: na afloop heeft de cel "
                  "<strong>23</strong> chromosomen, elk nog met twee chromatiden."),
            ("p", "In <strong>meiose II</strong> <strong>worden de zusterchromatiden "
                  "gescheiden</strong>. Daartussen wordt <strong>het DNA niet opnieuw "
                  "gekopieerd</strong>; anders zou het halveren niet lukken."),
            ("p", "Twee mechanismen maken elke gameet anders. Bij de "
                  "<strong>crossing-over</strong> of overkruising <strong>wisselen twee "
                  "homologe chromosomen stukken uit</strong> op een <strong>chiasma</strong>, "
                  "in het meervoud <strong>chiasmata</strong>; dat maakt <strong>nieuwe "
                  "combinaties van allelen</strong>, en heet recombinatie. Bij de "
                  "<strong>mixing</strong> <strong>verdelen de paren zich toevallig over de "
                  "polen</strong>, onafhankelijk van elkaar."),
            ("p", "Die variatie is belangrijk: <strong>broers en zussen verschillen daardoor van "
                  "elkaar</strong> en <strong>een soort kan zich beter aanpassen</strong>."),
            ("p", "Gaat er bij de meiose iets mis, bijvoorbeeld doordat een "
                  "<strong>chromosomenpaar verkeerd verdeeld</strong> wordt, dan <strong>krijgt "
                  "een gameet een chromosoom te veel of te weinig</strong>. Dat heet een "
                  "<strong>non-disjunctie</strong>."),
        ]),
        dict(kop="De twee delingen naast elkaar", blokken=[
            ("p", "Wat ze <strong>gemeen</strong> hebben: aan beide "
                  "<strong>gaat een S-fase vooraf</strong> en bij beide wordt "
                  "<strong>een spoelfiguur gebruikt</strong>."),
            ("p", "Waarin ze <strong>verschillen</strong>: <strong>de mitose geeft twee cellen, "
                  "de meiose vier</strong>, en na de meiose is het chromosomenaantal "
                  "<strong>gehalveerd</strong>. De dochtercellen van een mitose zijn identiek, "
                  "die van een meiose alle vier verschillend."),
            ("p", "Doordat <strong>de meiose halveert en de bevruchting verdubbelt</strong>, blijft "
                  "het aantal chromosomen van een soort over de generaties gelijk."),
        ]),
    ],
    onthoud=[
        "Interfase is G1, S en G2; delen is de M-fase.",
        "Profase condenseert, metafase stelt op, anafase trekt uiteen, telofase sluit af.",
        "Mitose: twee identieke cellen voor groei en herstel.",
        "Meiose: vier verschillende haploïde gameten.",
        "Crossing-over en mixing maken elke gameet uniek.",
    ],
)

# ───────────────────────── 12. Overerving en de wetten van Mendel
BUNDELS["overerving-en-de-wetten-van-mendel-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Overerving en de wetten van Mendel",
    onder="Rekenen met kruisingen, van een eenvoudig schema tot een stamboom.",
    secties=[
        dict(kop="Mendel en zijn erwten", blokken=[
            ("p", "Mendel werkte voor zijn <strong>proeven</strong> met erwtenplanten omdat die "
                  "daarvoor <strong>geschikt</strong> zijn: <strong>hun kenmerken duidelijk te "
                  "onderscheiden zijn</strong> en omdat ze <strong>zichzelf kunnen "
                  "bestuiven</strong>, zodat hij raszuivere lijnen kreeg. Hij gebruikte "
                  "<strong>grote aantallen</strong>, want <strong>een verhouding klopt alleen "
                  "bij veel nakomelingen</strong> en <strong>het toeval van één kruising zegt "
                  "te weinig</strong>."),
            ("p", "Hij <strong>stelde zijn wetten op</strong> zonder <strong>de chromosomen en "
                  "het DNA te kennen</strong>, en sprak van erffactoren; pas veertig jaar later "
                  "werd zijn werk met de chromosomen in verband gebracht."),
            ("p", "Een plant met <strong>twee dezelfde allelen</strong> is "
                  "<strong>homozygoot</strong> of raszuiver, met twee verschillende "
                  "<strong>heterozygoot</strong>. Een heterozygote nakomeling van twee raszuivere "
                  "lijnen heet een <strong>hybride</strong>. Het "
                  "<strong>genotype zijn de allelen</strong>, het "
                  "<strong>fenotype is het uitzicht</strong>; AA en Aa kunnen er dus net zo "
                  "uitzien."),
            ("p", "De generaties heten <strong>P</strong> (<strong>de ouders waarmee je "
                  "start</strong>), <strong>F1</strong> en <strong>F2</strong>. De plaats van een "
                  "gen is de <strong>locus</strong>; twee homologe chromosomen "
                  "<strong>dragen daar hetzelfde gen</strong>, maar "
                  "<strong>de allelen kunnen verschillen</strong>."),
        ]),
        dict(kop="De drie wetten", blokken=[
            ("p", "De <strong>uniformiteitswet</strong>: kruis je twee raszuivere ouders met een "
                  "verschillend kenmerk, dan <strong>lijken alle nakomelingen van de F1 op "
                  "elkaar</strong>."),
            ("p", "De <strong>splitsingswet</strong>: in de F2 splitsen de kenmerken weer. Bij "
                  "een dominant kenmerk krijg je dan <strong>3 op 1</strong> in fenotypes en "
                  "<strong>1 AA, 2 Aa en 1 aa</strong> in genotypes. Dat komt doordat een plant "
                  "<strong>Aa bij de meiose twee soorten gameten maakt: A en a</strong>. Zo’n "
                  "kruising met één kenmerk heet <strong>monohybride</strong>."),
            ("p", "De <strong>onafhankelijkheidswet</strong>: "
                  "<strong>twee kenmerken erven onafhankelijk van elkaar over</strong>, tenminste "
                  "als hun genen op verschillende chromosomen liggen. In een dihybride F2 geeft "
                  "dat <strong>9 op 3 op 3 op 1</strong>."),
        ]),
        dict(kop="Rekenen met een kruisingsschema", blokken=[
            ("p", "In een <strong>Punnettvierkant</strong> of kruisingsschema zet je de gameten "
                  "van de ene ouder boven en die van de andere links, en vul je elk vakje in. "
                  "Je <strong>zet het schema dus zelf uit</strong> voor je rekent."),
            ("p", "Een plant <strong>AaBb</strong> maakt <strong>vier</strong> soorten gameten: AB, "
                  "Ab, aB en ab. Daarom heeft een dihybride schema zestien vakjes."),
            ("p", "Kruis je <strong>Aa met aa</strong>, dan geven twee van de vier vakjes aa: "
                  "<strong>de helft</strong> toont het recessieve kenmerk. Een recessief kenmerk is "
                  "immers <strong>alleen te zien bij een homozygoot recessief genotype</strong>."),
            ("p", "Wil je weten of een plant met dominant uitzicht AA of Aa is, dan "
                  "<strong>kruis je ze met een recessieve plant</strong>. Komt er één recessieve "
                  "nakomeling, dan was ze Aa."),
        ]),
        dict(kop="Wat niet in het schema van Mendel past", blokken=[
            ("p", "Bij een <strong>intermediair</strong> kenmerk zie je in de F1 "
                  "<strong>iets tussen de twee ouderkenmerken</strong>, bijvoorbeeld roze uit rood "
                  "en wit. In de F2 krijg je dan <strong>1 op 2 op 1</strong>, want elk genotype "
                  "heeft zijn eigen uitzicht."),
            ("p", "Bij <strong>codominantie</strong> <strong>zie je de twee kenmerken naast "
                  "elkaar</strong> en <strong>wordt geen van de twee allelen verborgen</strong>, "
                  "zoals bij een rund met rode én witte haren door elkaar."),
            ("p", "Bij <strong>multipele allelen</strong> bestaan er meer dan twee varianten "
                  "van één gen. Het <strong>ABO-bloedgroepsysteem</strong> is daarvan het "
                  "voorbeeld, met de <strong>bloedgroepen</strong> A, B, AB en O: A en B zijn "
                  "codominant en dominant over O. Ouders met <strong>AB en O</strong> krijgen "
                  "dus kinderen met <strong>alleen A of B</strong>."),
            ("p", "Bij een <strong>geslachtsgebonden</strong> kenmerk ligt het gen op een "
                  "geslachtschromosoom, meestal het X. Daarom komt <strong>kleurenblindheid "
                  "vaker voor bij mannen</strong>: zij hebben er maar één X en geen tweede om "
                  "het recessieve allel te verbergen. Is een vrouw draagster van hemofilie en "
                  "de vader gezond, dan <strong>heeft de helft van de zonen hemofilie</strong> "
                  "en worden de dochters hoogstens draagster. Het geslacht zelf wordt bepaald "
                  "<strong>door de zaadcel, met een X of een Y</strong>; de "
                  "<strong>eicel</strong> draagt altijd een X. Een zaadcel met een Y geeft dus "
                  "een <strong>jongen</strong>, een zaadcel met een X een "
                  "<strong>meisje</strong>."),
            ("p", "<strong>Gekoppelde genen</strong> <strong>liggen op hetzelfde "
                  "chromosoom</strong> en gaan dus meestal samen naar één gameet. Alleen een "
                  "<strong>crossing-over tussen de twee loci</strong> kan ze scheiden, en "
                  "<strong>hoe verder ze uit elkaar liggen, hoe vaker dat gebeurt</strong>."),
            ("p", "Een <strong>letaal allel</strong> is <strong>homozygoot dodelijk</strong>, dus "
                  "<strong>vind je het nooit homozygoot bij een levend dier</strong>; in de "
                  "nakomelingschap zie je dan 2 op 1 in plaats van 3 op 1."),
            ("p", "Bij <strong>polygenie</strong> <strong>werken meerdere genen samen aan één "
                  "kenmerk</strong> en bepalen ze het dus <strong>samen</strong>, zoals bij "
                  "<strong>lichaamslengte</strong> en <strong>huidkleur</strong>. Daardoor "
                  "krijg je een vloeiende reeks in plaats van enkele scherp gescheiden groepen."),
        ]),
        dict(kop="Een stamboom lezen", blokken=[
            ("p", "In een stamboom staat een <strong>vierkant voor een man</strong> en een "
                  "<strong>cirkel voor een vrouw</strong>; een gevulde vorm betekent dat de persoon "
                  "het kenmerk heeft."),
            ("p", "Hebben <strong>twee gezonde ouders een ziek kind</strong>, dan is "
                  "<strong>het allel recessief en zijn de ouders drager</strong>. Een kenmerk dat "
                  "<strong>een generatie overslaat</strong>, wijst dus eerder op een recessief "
                  "allel. Komt een aandoening <strong>in elke generatie en bij beide "
                  "geslachten</strong> voor, dan is een <strong>dominant allel op een "
                  "lichaamschromosoom</strong> het meest waarschijnlijk."),
            ("p", "Aan een X-gebonden recessief kenmerk herken je dat "
                  "<strong>veel meer mannen dan vrouwen aangetast zijn</strong> en dat "
                  "<strong>een aangetaste man het aan al zijn dochters doorgeeft als "
                  "draagster</strong>. Van vader op zoon gaat het juist nooit, want een zoon "
                  "krijgt van zijn vader het Y-chromosoom."),
        ]),
    ],
    onthoud=[
        "Uniformiteit in F1, splitsing 3 op 1 in F2, dihybride 9:3:3:1.",
        "Genotype zijn de allelen, fenotype is het uitzicht.",
        "Intermediair geeft een mengvorm, codominant toont beide kenmerken.",
        "X-gebonden gaat nooit van vader op zoon.",
        "Overslaan van een generatie wijst op een recessief allel.",
    ],
)

# ───────────────────────── 13. Genexpressie: transcriptie en translatie
BUNDELS["genexpressie-transcriptie-en-translatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Genexpressie: transcriptie en translatie",
    onder="Van gen naar eiwit, stap voor stap.",
    secties=[
        dict(kop="De genetische code", blokken=[
            ("p", "Een <strong>gen</strong> is <strong>een stuk DNA met de code voor een "
                  "product</strong>. Dat die code gebruikt wordt, heet "
                  "<strong>genexpressie</strong>."),
            ("p", "Op het mRNA wordt per drie gelezen. Zo'n <strong>groepje van drie "
                  "nucleotiden</strong> heet een <strong>codon</strong> of triplet; op het tRNA "
                  "heet het tegenovergestelde drietal het <strong>anticodon</strong>."),
            ("p", "De code is <strong>gedegenereerd</strong>: "
                  "<strong>verschillende codons geven hetzelfde aminozuur</strong>, want er zijn 64 "
                  "codons voor 20 aminozuren. En ze is <strong>universeel</strong>: "
                  "<strong>bijna alle organismen gebruiken dezelfde codons</strong>, wat "
                  "gentechnologie mogelijk maakt."),
            ("p", "<strong>AUG</strong> is het startcodon; UAA, UAG en UGA zijn stopcodons. "
                  "Valt er vooraan een nucleotide <strong>weg</strong>, dan <strong>schuift het "
                  "leesraam en veranderen alle codons erna</strong>."),
        ]),
        dict(kop="De transcriptie", blokken=[
            ("p", "De transcriptie gebeurt bij een eukaryoot <strong>in de kern</strong>. "
                  "<strong>RNA-polymerase</strong> maakt het mRNA, en het mRNA is "
                  "<strong>complementair aan de matrijsstreng</strong>. Leest de matrijs TAC CGA, "
                  "dan wordt het mRNA <strong>AUG GCU</strong>. Het mRNA wordt, net als nieuw DNA, "
                  "<strong>van 5' naar 3'</strong> gebouwd."),
            ("p", "Bij de <strong>initiatie</strong> <strong>binden transcriptiefactoren en "
                  "polymerase op de promotor</strong>, de aanlegplaats vlak voor het gen. Een "
                  "<strong>transcriptiefactor</strong> is <strong>een eiwit dat helpt beslissen "
                  "of een gen gelezen wordt</strong>. Daarna volgt de elongatie, en bij de "
                  "<strong>terminatie</strong>, die de transcriptie <strong>beëindigt</strong>, "
                  "stopt polymerase op <strong>een terminatiesignaal achter het gen</strong>."),
            ("p", "Het ruwe product is <strong>pre-mRNA</strong> en moet nog afgewerkt worden: "
                  "<strong>de introns worden eruit geknipt</strong> (de splicing) en er komt "
                  "<strong>een 5'-cap en een poly(A)-staart</strong> op. De "
                  "<strong>exonen</strong> zijn <strong>de stukken die in het rijpe mRNA "
                  "blijven</strong>; een <strong>intron</strong> <strong>wordt uit het pre-mRNA "
                  "geknipt</strong> en <strong>komt niet in het eiwit terecht</strong>."),
            ("p", "Een <strong>prokaryoot</strong> heeft vrijwel geen introns en geen kern: haar "
                  "mRNA wordt al vertaald terwijl het gemaakt wordt. Bij een eukaryoot staat er "
                  "<strong>niet meteen een eiwit klaar</strong>, want "
                  "<strong>het mRNA moet eerst afgewerkt worden en de kern uit</strong>."),
        ]),
        dict(kop="De translatie", blokken=[
            ("p", "De translatie gebeurt <strong>op het ribosoom</strong>, dat uit "
                  "<strong>rRNA en ribosomale proteïnen</strong> bestaat, in een grote en een "
                  "kleine subeenheid."),
            ("p", "Een <strong>tRNA</strong> <strong>brengt een aminozuur naar het "
                  "ribosoom</strong>. Bij de <strong>activatie</strong> wordt een aminozuur "
                  "<strong>met ATP aan zijn tRNA gekoppeld</strong>. Op het codon "
                  "<strong>GCU</strong> past <strong>daarop</strong> het anticodon "
                  "<strong>CGA</strong>."),
            ("p", "Op de <strong>A-plaats komt het nieuwe tRNA binnen</strong>, op de "
                  "<strong>P-plaats zit het tRNA met de groeiende keten</strong>. "
                  "<strong>Peptidyltransferase</strong> legt de peptidebinding, en daarna schuift "
                  "het ribosoom één codon op."),
            ("p", "Bij een <strong>stopcodon</strong> past geen tRNA; een <strong>release "
                  "factor</strong> laat dan de keten los en <strong>sluit de translatie "
                  "af</strong>. Een stopcodon <strong>codeert voor geen enkel "
                  "aminozuur</strong>. Leest het mRNA <strong>AUG GCU UAA</strong>, dan heeft "
                  "het eiwit dus <strong>twee</strong> aminozuren."),
            ("p", "Lezen er meerdere ribosomen tegelijk hetzelfde mRNA, dan heet dat een "
                  "<strong>polysoom</strong>."),
        ]),
        dict(kop="Van keten naar werkend eiwit", blokken=[
            ("p", "Eén gen kan toch verschillende eiwitten opleveren: door "
                  "<strong>alternatieve splicing van de exons</strong> en "
                  "<strong>doordat het eiwit achteraf nog bewerkt wordt</strong>."),
            ("p", "De keten <strong>ondergaat</strong> die bewerkingen na de translatie; ze "
                  "heten de <strong>posttranslationele modificatie</strong>, dus "
                  "<strong>posttranslationeel</strong> <strong>afwerken</strong>: <strong>er "
                  "worden sacharidegroepen aangehangen</strong>, stukken afgeknipt en "
                  "<strong>de keten wordt in haar vorm geplooid</strong>."),
            ("p", "De <strong>volgorde van de aminozuren volgt uit de volgorde van de "
                  "nucleotiden</strong>, en uit die volgorde volgt de vorm. En "
                  "<strong>alleen met de juiste vorm past een eiwit op zijn partner</strong>: een "
                  "enzym op zijn substraat, een receptor op zijn hormoon."),
            ("p", "Alle cellen van één mens <strong>hebben hetzelfde DNA</strong> maar "
                  "<strong>brengen niet dezelfde genen tot expressie</strong>. Maakt een cel plots "
                  "veel meer van een eiwit, dan is de meest waarschijnlijke oorzaak dat "
                  "<strong>dat gen vaker getranscribeerd wordt</strong>."),
        ]),
    ],
    onthoud=[
        "Een codon is drie nucleotiden; AUG start, UAA/UAG/UGA stoppen.",
        "Transcriptie in de kern, translatie op het ribosoom.",
        "Introns eruit, exons aan elkaar, cap en staart erop.",
        "tRNA brengt het aminozuur, het anticodon past op het codon.",
        "De volgorde bepaalt de vorm, en de vorm bepaalt de werking.",
    ],
)

# ───────────────────────── 14. Genregulatie, epigenetica en nature of nurture
BUNDELS["genregulatie-epigenetica-en-nature-of-nurture-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Genregulatie, epigenetica en nature of nurture",
    onder="Hoe een cel haar genen aan- en uitzet, en wat de omgeving daarmee te maken heeft.",
    secties=[
        dict(kop="Waarom regelen?", blokken=[
            ("p", "Een cel zet niet al haar genen tegelijk aan, want "
                  "<strong>ze heeft maar een deel van die eiwitten nodig</strong> en eiwitten maken "
                  "kost energie en grondstoffen."),
            ("p", "Ook bij een bacterie <strong>staan sommige genen doorlopend aan</strong> en "
                  "<strong>blijven ze dus aanstaan</strong>, zoals die voor de ribosomen. "
                  "Alleen de genen voor wisselende taken worden geregeld."),
        ]),
        dict(kop="Het lac-operon van E. coli", blokken=[
            ("p", "Een <strong>operon</strong> is <strong>een groep genen bij een bacterie die "
                  "samen aan- of uitgezet worden</strong>, achter dezelfde promotor en operator. "
                  "Het voordeel: <strong>alle genen van één taak gaan samen aan</strong>."),
            ("p", "Het <strong>lac-operon</strong> codeert <strong>voor de eiwitten die lactose "
                  "afbreken</strong>. Het <strong>regulatorgen</strong> ligt erbuiten en codeert "
                  "<strong>op de repressor</strong>."),
            ("p", "Zonder lactose <strong>bindt de repressor op de operator en blokkeert hij de "
                  "transcriptie</strong>. Komt er lactose, dan "
                  "<strong>bindt die op de repressor, die loslaat</strong>: lactose werkt dus als "
                  "<strong>inductor</strong>, <strong>een stof die een operon aanzet</strong>."),
            ("p", "De <strong>promotor is de aanlegplaats van polymerase</strong> en de "
                  "<strong>operator is de plaats waar de repressor past</strong>. Allebei zijn het "
                  "stukjes DNA met een regelfunctie, geen genen."),
            ("p", "<strong>Glucose</strong> krijgt de voorkeur, want ze is "
                  "<strong>zonder extra enzymen bruikbaar</strong>. Zolang er glucose is, blijft "
                  "het lac-operon grotendeels uit."),
        ]),
        dict(kop="Regulatie bij een eukaryoot", blokken=[
            ("p", "Een eukaryote cel kan regelen "
                  "<strong>bij de transcriptie van het gen</strong> en "
                  "<strong>bij de afbraak van het mRNA</strong>, en ook bij de splicing, de "
                  "translatie en het afwerken van het eiwit."),
            ("p", "<strong>Transcriptiefactoren kunnen een gen zowel aanzetten als "
                  "tegenhouden</strong>. Moet een <strong>levercel</strong> plots veel van een "
                  "<strong>ontgiftend</strong> enzym maken, dan <strong>wordt dat gen eerst "
                  "vaker afgelezen</strong>; een transcriptiefactor kan het ook juist "
                  "<strong>afremmen</strong>."),
            ("p", "Regelen op het niveau van het mRNA heeft een eigen voordeel: "
                  "<strong>de cel kan snel stoppen met een eiwit te maken</strong>."),
            ("p", "<strong>Celspecifieke genexpressie</strong> betekent dat "
                  "<strong>elk celtype zijn eigen deel van het genoom gebruikt</strong>."),
            ("p", "Bij <strong>RNA-interferentie</strong> wordt een gen "
                  "<strong>afgeremd door kleine stukjes RNA</strong>. Een "
                  "<strong>micro-RNA</strong> <strong>bindt op een mRNA en legt de translatie "
                  "stil</strong>. Daarbij <strong>wordt het gen zelf niet uit het DNA "
                  "geknipt</strong>, dus is het effect omkeerbaar."),
        ]),
        dict(kop="Epigenetica", blokken=[
            ("p", "<strong>Epigenetica</strong> bestudeert "
                  "<strong>veranderingen in de genexpressie zonder verandering van het DNA</strong>. "
                  "De letters blijven dezelfde; alleen de leesbaarheid verandert."),
            ("p", "<strong>DNA-methylering</strong> <strong>legt een gen stil</strong>: er komt een "
                  "<strong>methylgroep</strong> op het DNA, vooral op cytosinen, en de "
                  "transcriptiefactoren raken er niet meer bij."),
            ("p", "<strong>Histonacetylering</strong> doet het omgekeerde: ze <strong>maakt het "
                  "chromatine losser, zodat genen leesbaar worden</strong>. En bij "
                  "<strong>chromatine remodeling</strong> of "
                  "<strong>chromatineremodeling</strong> <strong>worden de nucleosomen "
                  "verschoven en herschikt</strong>."),
            ("p", "Zo'n verandering <strong>kan ongedaan gemaakt worden</strong>. Dat een "
                  "<strong>spiercel en een zenuwcel</strong> een ander "
                  "<strong>uitzicht</strong> hebben, komt doordat <strong>hun chromatine anders "
                  "open ligt</strong>."),
            ("p", "<strong>Voeding</strong> en <strong>langdurige stress</strong> kunnen zo'n "
                  "patroon beïnvloeden. Maar <strong>epigenetische merktekens worden niet "
                  "altijd aan de kinderen doorgegeven</strong>: bij het vormen van de gameten "
                  "wordt het patroon grotendeels gewist."),
        ]),
        dict(kop="Nature en nurture", blokken=[
            ("p", "<strong>Nature</strong> is <strong>de aanleg die in het DNA ligt</strong>, "
                  "<strong>nurture</strong> is <strong>de invloed van de opvoeding en de "
                  "omgeving</strong>."),
            ("p", "Verschillen twee eeneiige tweelingen die <strong>apart opgevoed</strong> "
                  "zijn in lengte, dan ligt dat aan <strong>de omgeving, want hun DNA is "
                  "gelijk</strong>. Krijgt iemand met aanleg voor hoge bloeddruk die pas na "
                  "jaren ongezond eten, dan zie je dat <strong>aanleg en omgeving "
                  "samenwerken</strong>."),
            ("p", "In <strong>tegenstelling</strong> daarmee zijn sterk door de omgeving "
                  "bepaald: <strong>de taal die iemand spreekt</strong> en <strong>het "
                  "lichaamsgewicht</strong>. De <strong>bloedgroep</strong> daarentegen "
                  "<strong>ligt volledig in het DNA vast</strong> en <strong>hangt dus niet van "
                  "de voeding af</strong>, net als de oogkleur en het geslacht."),
            ("p", "Groeit een plant uit hetzelfde zaad in de schaduw kleiner op, dan is dat "
                  "<strong>een invloed van de omgeving op het fenotype</strong>. Het "
                  "<strong>fenotype</strong> is <strong>alles wat je aan een organisme kunt "
                  "waarnemen</strong>, en volgt uit het genotype én de omgeving. Bij "
                  "<strong>de meeste kenmerken valt niet te zeggen dat alleen de genen of alleen de "
                  "omgeving tellen</strong>."),
            ("p", "Epigenetica is de brug tussen die twee: "
                  "<strong>de omgeving verandert mee welke genen gelezen worden</strong>."),
        ]),
    ],
    onthoud=[
        "Een operon zet alle genen van één taak samen aan.",
        "Geen lactose: repressor op de operator. Lactose: repressor laat los.",
        "Methylering legt stil, acetylering maakt leesbaar.",
        "Epigenetica verandert de leesbaarheid, niet de letters.",
        "Nature is aanleg, nurture is omgeving; meestal werken ze samen.",
    ],
)

# ───────────────────────── 15. Mutaties, mutagenen en kanker
BUNDELS["mutaties-mutagenen-en-kanker-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Mutaties, mutagenen en kanker",
    onder="Van één veranderde base tot een ontspoorde celdeling.",
    secties=[
        dict(kop="Wat is een mutatie?", blokken=[
            ("p", "Een <strong>mutatie</strong> is <strong>een blijvende verandering in het "
                  "DNA</strong>. Ze gaat bij elke celdeling mee. Verandert alleen de leesbaarheid, "
                  "dan gaat het om epigenetica."),
            ("p", "Een <strong>spontane</strong> mutatie is een kopieerfout die blijft staan. Een "
                  "<strong>geïnduceerde</strong> mutatie <strong>komt door een invloed van "
                  "buitenaf</strong>: <strong>straling of een gifstof kan ze veroorzaken</strong>."),
            ("p", "Zo'n invloed heet een <strong>mutageen</strong>. <strong>UV-straling van de "
                  "zon</strong> doet <strong>twee naast elkaar liggende basen aan elkaar "
                  "plakken</strong>. <strong>Benzopyreen uit tabaksrook</strong>, ioniserende "
                  "straling, nitrieten en nitrosaminen doen het op hun eigen manier. "
                  "<strong>Vrije radicalen</strong> <strong>reageren met de basen en beschadigen "
                  "ze</strong>."),
            ("p", "Gelukkig heeft een cel <strong>enzymen die beschadigd DNA kunnen "
                  "herstellen</strong>. Alleen wat ontsnapt of verkeerd hersteld wordt, blijft als "
                  "mutatie staan. En <strong>niet elke mutatie is schadelijk</strong>: zonder "
                  "mutaties zou er geen variatie en dus geen evolutie zijn."),
        ]),
        dict(kop="Genmutaties", blokken=[
            ("p", "Een <strong>puntmutatie</strong> is <strong>een verandering in één "
                  "nucleotide</strong>. Bij een <strong>substitutie</strong> wordt <strong>één "
                  "base door een andere vervangen</strong>, dus is ze een "
                  "<strong>vervanging</strong>; het aantal blijft gelijk, dus het leesraam "
                  "schuift niet."),
            ("p", "Een <strong>deletie</strong> van één nucleotide is meestal erger: "
                  "<strong>het leesraam verschuift en alle codons erna veranderen</strong>. Een "
                  "<strong>insertie van drie nucleotiden laat het leesraam ongemoeid</strong>, want "
                  "drie nucleotiden zijn precies één codon."),
            ("p", "Wat een substitutie doet, hangt af van waar ze valt. Wordt "
                  "<strong>AUG GCU UCA</strong> tot <strong>AUG GCC UCA</strong>, dan verandert er "
                  "<strong>waarschijnlijk niets aan het eiwit</strong>, want de code is "
                  "gedegenereerd: zo'n geval heet een <strong>stille mutatie</strong>. Maakt de "
                  "substitutie van een gewoon codon een stopcodon, dan "
                  "<strong>wordt het eiwit te vroeg afgebroken en is het te kort</strong>."),
            ("p", "Bij een <strong>verliesmutatie</strong> werkt het eiwit minder of niet meer; bij "
                  "een <strong>winstmutatie</strong> <strong>doet het eiwit iets meer of iets "
                  "nieuws</strong>, en dat kan even schadelijk zijn."),
            ("p", "Een mutatie is <strong>erfelijk als ze in een geslachtscel zit</strong>, "
                  "want alleen die wordt aan het volgende <strong>organisme "
                  "doorgegeven</strong>; wat in een lichaamscel gebeurt, gaat niet op de "
                  "kinderen <strong>over</strong>. Een <strong>mutatie in een huidcel door "
                  "zonlicht</strong> gaat dus <strong>niet naar de kinderen</strong>."),
            ("p", "Voorbeelden van <strong>aandoeningen</strong> door een genmutatie zijn "
                  "<strong>sikkelcelanemie</strong>, ook <strong>sikkelcelziekte</strong> of "
                  "<strong>sikkelcelarmoede</strong> genoemd, waarbij <strong>één aminozuur in "
                  "het hemoglobine vervangen is</strong> en de rode <strong>bloedcellen van "
                  "vorm veranderen</strong>, <strong>mucoviscidose</strong> en <strong>de "
                  "ziekte van Huntington</strong>."),
        ]),
        dict(kop="Chromosoom- en genoommutaties", blokken=[
            ("p", "Een <strong>chromosoommutatie</strong> is <strong>een verandering in de bouw van "
                  "een chromosoom</strong>. Bij een <strong>deletie</strong> verdwijnt er een stuk, "
                  "bij een <strong>insertie</strong> komt er een stuk bij, bij een "
                  "<strong>inversie</strong> <strong>komt een stuk omgekeerd terug</strong>, en bij "
                  "een <strong>translocatie</strong> gaat <strong>een stuk naar een niet-homoloog "
                  "chromosoom</strong>."),
            ("p", "Het <strong>cri-du-chatsyndroom</strong> komt van een deletie. Het "
                  "<strong>Philadelphiachromosoom</strong>, een translocatie tussen chromosoom 9 en "
                  "22, <strong>hoort bij een vorm van leukemie</strong>."),
            ("p", "Een <strong>genoommutatie</strong> is <strong>een verandering in het aantal "
                  "chromosomen</strong>. Ze ontstaat door een <strong>non-disjunctie</strong>, "
                  "<strong>de fout bij de meiose waarbij twee chromosomen niet uit elkaar "
                  "gaan</strong>; het woord wordt ook zonder streepje geschreven, als "
                  "<strong>nondisjunctie</strong>."),
            ("p", "Bij een <strong>trisomie</strong> <strong>zijn er drie in plaats van "
                  "twee</strong>, bij een <strong>monosomie</strong> ontbreekt er één. "
                  "<strong>Aandoeningen</strong> door een <strong>afwijkend</strong> aantal "
                  "chromosomen zijn <strong>het syndroom van Down</strong> (trisomie 21), "
                  "<strong>het syndroom van Turner</strong> (één X) en het syndroom van "
                  "Klinefelter. Bij <strong>mozaïcisme</strong> of <strong>mozaïek</strong> "
                  "<strong>hebben niet alle cellen van een persoon dezelfde "
                  "chromosomenfout</strong>, en zijn de verschijnselen vaak milder."),
            ("p", "<strong>Een karyogram laat een genoommutatie zien, maar een genmutatie "
                  "niet</strong>: één veranderde base is er niet op te zien."),
        ]),
        dict(kop="Mutaties en kanker", blokken=[
            ("p", "<strong>Carcinogenese</strong> is <strong>het geleidelijk ontstaan van "
                  "kanker</strong>. Er zijn <strong>meerdere mutaties</strong> voor nodig in "
                  "dezelfde cellijn, vaak over jaren; daarom stijgt de kans met de leeftijd. Een "
                  "stof die kanker kan veroorzaken, heet een <strong>carcinogeen</strong>."),
            ("p", "Een <strong>proto-oncogen</strong> is <strong>een gezond gen dat de celdeling "
                  "aanstuurt</strong>. Gaat het door een mutatie te hard werken, dan wordt het een "
                  "<strong>oncogen</strong>. Een <strong>tumorsuppressorgen</strong> "
                  "<strong>legt de celcyclus stil bij schade</strong> en "
                  "<strong>laat een beschadigde cel afsterven</strong>."),
            ("p", "Er moet dus iets <strong>misgaan</strong> op twee plaatsen tegelijk voor een "
                  "cel een kankercel wordt: <strong>een gen voor groei dat te hard "
                  "werkt</strong> en <strong>een gen dat de deling afremt en uitvalt</strong>."),
            ("p", "Elk uiteinde van een chromosoom heet een <strong>telomeer</strong>; samen "
                  "zijn het de <strong>telomeren</strong>, en ze worden en worden <strong>bij "
                  "elke deling korter</strong>. Een kankercel blijft zich eindeloos delen "
                  "doordat ze <strong>haar telomerasegen weer aanzet</strong>, zodat de "
                  "telomeren hersteld worden."),
            ("p", "Een tumor <strong>laat nieuwe bloedvaten naar zich toe groeien</strong>; dat "
                  "heet <strong>angiogenese</strong>. Een <strong>angiogeneseremmer</strong> "
                  "<strong>belet als behandeling de tumor nieuwe bloedvaten te maken</strong>. "
                  "Bij <strong>genrepressie</strong> wordt <strong>een te actief gen gericht "
                  "stilgelegd</strong>, en zo kan ze bij een behandeling tegen kanker "
                  "<strong>helpen</strong>, bijvoorbeeld met een klein RNA tegen het mRNA van "
                  "een oncogen."),
        ]),
    ],
    onthoud=[
        "Substitutie houdt het leesraam heel, een deletie van één base niet.",
        "Een stille mutatie verandert het eiwit niet, een stopcodon kort het af.",
        "Erfelijk is alleen wat in een geslachtscel zit.",
        "Gen, chromosoom, genoom: drie niveaus van mutatie.",
        "Kanker: oncogen te actief én tumorsuppressorgen uitgevallen.",
    ],
)

# ───────────────────────── 16. DNA-technologie en gentechnologie
BUNDELS["dna-technologie-en-gentechnologie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="DNA-technologie en gentechnologie",
    onder="Van plasmide en restrictie-enzym tot PCR, sequencing en CRISPR.",
    secties=[
        dict(kop="Het DNA van een bacterie", blokken=[
            ("p", "Een bacterie heeft één chromosoom "
                  "<strong>als een gesloten ring, vrij in het cytoplasma</strong>. Daarnaast kan ze "
                  "<strong>plasmiden</strong> hebben: <strong>kleine losse ringetjes DNA</strong>. "
                  "Zo'n plasmide <strong>kan van de ene bacterie naar de andere</strong> en "
                  "<strong>kan een resistentiegen dragen</strong>."),
            ("p", "Er zijn drie vormen van natuurlijke genoverdracht. Bij "
                  "<strong>transformatie</strong> <strong>neemt een bacterie vrij DNA uit haar "
                  "omgeving op</strong>. Bij <strong>conjugatie</strong> <strong>wisselen twee "
                  "bacteriën DNA uit via een brug</strong>, de <strong>pilus</strong>. Bij "
                  "<strong>transductie</strong> neemt een virus bacterieel DNA mee naar een "
                  "andere bacterie: het <strong>meeneemt</strong> dus het DNA van zijn vorige "
                  "gastheer."),
            ("p", "Daardoor verspreidt <strong>antibioticumresistentie</strong> zich snel: zit het "
                  "gen op een plasmide, dan kan het zelfs naar een andere soort."),
        ]),
        dict(kop="De bacteriofaag", blokken=[
            ("p", "Een <strong>bacteriofaag</strong> is <strong>een virus dat bacteriën "
                  "besmet</strong>. Een virus is een <strong>obligate parasiet</strong>: het "
                  "<strong>kan zich alleen in een levende gastheercel vermenigvuldigen</strong>."),
            ("p", "In de <strong>lytische cyclus</strong> <strong>maakt de cel nieuwe fagen en "
                  "barst ze open</strong>. In de <strong>lysogene cyclus</strong> "
                  "<strong>wordt het faag-DNA in het bacteriële chromosoom ingebouwd</strong> en "
                  "<strong>bij elke deling mee gekopieerd</strong>, tot het later alsnog actief "
                  "wordt. De lambdafaag van E. coli kan allebei."),
        ]),
        dict(kop="Het gereedschap van de gentechnologie", blokken=[
            ("p", "Een <strong>restrictie-enzym</strong> is <strong>een enzym dat DNA op een vaste "
                  "plaats in de sequentie doorknipt</strong>, zoals EcoRI. Bacteriën gebruiken die "
                  "enzymen zelf tegen faag-DNA."),
            ("p", "Een schuine knip laat <strong>sticky ends</strong> achter. Die zijn handig omdat "
                  "ze <strong>passen op elk stuk dat met hetzelfde enzym geknipt is</strong>. Een "
                  "rechte knip geeft blunt ends. <strong>Ligase</strong> "
                  "<strong>hecht twee geknipte stukken definitief aan elkaar</strong>."),
            ("p", "<strong>Recombinant DNA</strong> is <strong>DNA waarin stukken van "
                  "verschillende herkomst samengebracht zijn</strong>, zoals een plasmide met een "
                  "menselijk gen erin."),
            ("p", "Een <strong>vector</strong> is <strong>een drager die DNA in een cel "
                  "brengt</strong>: een plasmide, een virus of een liposoom. Daarnaast bestaan er "
                  "directe methoden: <strong>micro-injectie met een fijne naald</strong>, "
                  "<strong>elektroporatie met een stroomstoot</strong> en, bij planten, het "
                  "genenkanon. Het <strong>Ti-plasmide van een bodembacterie wordt gebruikt om "
                  "planten te veranderen</strong>, want die bacterie brengt van nature T-DNA in een "
                  "plantencel."),
            ("p", "Bij een <strong>cisgeen</strong> organisme <strong>komt het gen van een "
                  "verwante soort</strong> die ook natuurlijk kan kruisen; bij een "
                  "<strong>transgeen</strong> organisme komt het van over die grens heen. Dat kan, "
                  "want <strong>een menselijk gen werkt ook in een bacterie</strong>: de genetische "
                  "code is bijna universeel."),
            ("p", "Zo wordt <strong>insuline</strong> gemaakt: <strong>het insulinegen wordt in "
                  "een plasmide gezet en ingebracht</strong>, en de bacterie "
                  "<strong>produceert</strong> het eiwit. Een bacterie kan een menselijk gen "
                  "<strong>rechtstreeks</strong> gebruiken, omdat de code dezelfde is. En een "
                  "gewas <strong>weerstaat</strong> insecten doordat <strong>er een bacterieel "
                  "gen voor een gifstof ingebouwd wordt</strong>."),
        ]),
        dict(kop="De technieken", blokken=[
            ("p", "Een <strong>PCR</strong> dient om <strong>een stukje DNA miljoenen keren te "
                  "vermenigvuldigen</strong>. Elke cyclus <strong>herhaalt dezelfde drie "
                  "stappen</strong>: <strong>verhitten tot de strengen loskomen</strong>, "
                  "<strong>afkoelen zodat de primers kunnen binden</strong> en verlengen. Een "
                  "<strong>kwantitatieve PCR</strong> meet er ook <strong>de "
                  "hoeveelheid</strong> bij, en toont zo de <strong>aanwezigheid</strong> van "
                  "een stukje DNA in een staal."),
            ("p", "Bij <strong>gelelektroforese</strong> <strong>beweegt</strong> DNA "
                  "<strong>naar de pluspool, want het is negatief geladen</strong>, en dus weg "
                  "van de <strong>minpool</strong>; de pluspool is de <strong>positief</strong> "
                  "geladen kant, en <strong>kleine stukken schuiven verder door de "
                  "gel</strong>."),
            ("p", "Een <strong>DNA-fingerprint</strong> werkt omdat "
                  "<strong>iedereen een eigen aantal herhalingen in zijn DNA heeft</strong>. Ze "
                  "dient voor <strong>het vaststellen van wie de vader is</strong> en voor "
                  "<strong>het vergelijken van een spoor met een verdachte</strong>."),
            ("p", "<strong>Sequencing</strong> of <strong>sequenering</strong> <strong>leest de "
                  "volledige basenvolgorde uit</strong>. <strong>CRISPR-Cas</strong> "
                  "<strong>past een gen op een gekozen plaats aan</strong> en kan het dus "
                  "<strong>aanpassen</strong> zonder het hele gen te vervangen: een stukje RNA "
                  "wijst de plaats aan en het Cas-enzym knipt. Die techniek <strong>komt uit "
                  "het afweersysteem van bacteriën</strong>. <strong>Gene editing</strong>, met "
                  "de Engelse term, of <strong>genoomeditie</strong>, is <strong>het gericht "
                  "wijzigen van een bestaand gen</strong> op zijn "
                  "<strong>oorspronkelijke</strong> plaats."),
        ]),
        dict(kop="Klonen en toepassingen", blokken=[
            ("p", "<strong>Natuurlijk klonen</strong> bestaat ook: een "
                  "<strong>eeneiige tweeling</strong> is er een voorbeeld van. Bij "
                  "<strong>reproductief klonen</strong> wordt "
                  "<strong>een volledig nieuw individu gemaakt dat genetisch gelijk is</strong>, "
                  "zoals het schaap Dolly. Toch is zo'n kloon "
                  "<strong>niet in gedrag precies hetzelfde dier</strong>, want de omgeving "
                  "verschilt."),
            ("p", "Bij <strong>moleculair klonen</strong> of <strong>klonering</strong> wordt "
                  "<strong>een stuk DNA in een gastheercel vermenigvuldigd</strong>; "
                  "<strong>klonen</strong> betekent hier dus vermenigvuldigen, niet een dier "
                  "maken. Bij <strong>therapeutisch klonen</strong> wordt <strong>weefsel of "
                  "cellen gekweekt om een patiënt te behandelen</strong>, dus "
                  "<strong>kweken</strong> in plaats van voortplanten, zonder nieuw individu."),
            ("p", "In de geneeskunde dient dit alles onder meer voor <strong>het opsporen van "
                  "afwijkingen voor de geboorte</strong> en <strong>het herkennen van een "
                  "micro-organisme in een staal</strong>, en ook voor ouderschapsbepaling, "
                  "daderidentificatie en kankeronderzoek. Gentherapie <strong>helpt</strong> "
                  "door een werkend gen in de cellen te <strong>overdragen</strong>."),
            ("p", "Over <strong>ggo's</strong> wordt maatschappelijk gediscussieerd, want "
                  "<strong>de gevolgen op lange termijn zijn niet voor iedereen even "
                  "duidelijk</strong>. Dat debat wordt dus <strong>besproken</strong> over het "
                  "gebruik, niet over de vraag of de techniek werkt."),
        ]),
    ],
    onthoud=[
        "Transformatie is opnemen, conjugatie is doorgeven, transductie gaat via een virus.",
        "Restrictie-enzym knipt, ligase plakt, een vector brengt binnen.",
        "PCR vermenigvuldigt, gel scheidt, sequencing leest, CRISPR wijzigt.",
        "Cisgeen blijft binnen verwante soorten, transgeen gaat eroverheen.",
        "Een plasmide met een resistentiegen reist van bacterie naar bacterie.",
    ],
)

# ───────────────────────── 17. Argumenten voor evolutie en de evolutietheorieën
BUNDELS["argumenten-voor-evolutie-en-de-evolutietheorieen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Argumenten voor evolutie en de evolutietheorieën",
    onder="Waarop de evolutietheorie steunt, en hoe ze zelf geëvolueerd is.",
    secties=[
        dict(kop="Wat evolutie is", blokken=[
            ("p", "Bij <strong>biologische evolutie</strong> "
                  "<strong>veranderen de erfelijke eigenschappen van een populatie over de "
                  "generaties</strong>. Het gebeurt dus in een populatie, niet in één individu."),
            ("p", "De <strong>tree of life</strong>, met de Engelse term, of levensboom "
                  "<strong>stelt voor</strong>: <strong>de verwantschap tussen alle "
                  "soorten</strong> voor. Elke splitsing is een <strong>gemeenschappelijke "
                  "voorouder</strong>. Dat betekent niet dat <strong>de ene soort uit de andere "
                  "ontstaan is</strong>: mens en chimpansee stammen allebei af van een derde, "
                  "uitgestorven soort."),
        ]),
        dict(kop="Argumenten uit de bouw en de ontwikkeling", blokken=[
            ("p", "<strong>Homologe organen</strong> hebben <strong>dezelfde bouw en een "
                  "gemeenschappelijke oorsprong</strong>, zoals de voorpoot van een hond, de vleugel "
                  "van een vleermuis en de arm van een mens. <strong>Analoge organen</strong> "
                  "hebben <strong>dezelfde functie maar een andere bouw</strong>, zoals de vleugel "
                  "van een insect en die van een vogel; analogie wijst dus niet op verwantschap."),
            ("p", "Een <strong>rudimentair orgaan</strong> is "
                  "<strong>een orgaan dat bij een soort geen functie meer heeft</strong>, zoals de "
                  "staartbeentjes bij de mens. Homologie en rudimentaire organen zijn de "
                  "argumenten uit de <strong>anatomie</strong>."),
            ("p", "Uit de <strong>embryologie</strong> komt dat "
                  "<strong>verwante soorten een gelijkaardige ontwikkeling doorlopen</strong>: een "
                  "vis-, een kip- en een mensenembryo hebben alle kieuwbogen."),
        ]),
        dict(kop="Argumenten uit de fossielen", blokken=[
            ("p", "<strong>Fossielen</strong> zijn <strong>resten of sporen van organismen die "
                  "bewaard bleven in de gesteentelagen</strong>. Omdat lagen zich opstapelen, "
                  "liggen <strong>de oudste fossielen het diepst</strong>: wat "
                  "<strong>dieper</strong> in de <strong>gesteentelaag</strong> ligt, is ouder, "
                  "en wat bovenaan ligt, is <strong>jonger</strong>."),
            ("p", "<strong>Archaeopteryx</strong> is belangrijk omdat hij "
                  "<strong>veren had, zoals een vogel</strong>, en tegelijk "
                  "<strong>tanden en een benige staart, zoals een reptiel</strong>. Zo'n vondst "
                  "heet een <strong>overgangsfossiel</strong>."),
            ("p", "Een <strong>continue reeks</strong> is <strong>een reeks vondsten die een soort "
                  "stap voor stap ziet veranderen</strong>, zoals bij de paardachtigen en de "
                  "walvisachtigen. Vind je in een oude laag een vis met pootachtige vinnen, dan is "
                  "dat <strong>een overgangsvorm tussen twee groepen</strong>."),
        ]),
        dict(kop="Argumenten uit de moleculen en de aardrijkskunde", blokken=[
            ("p", "Het vergelijken van <strong>DNA-sequenties</strong> is sterk omdat "
                  "<strong>hoe verwanter twee soorten zijn, hoe meer hun DNA gelijkt</strong>. "
                  "Hetzelfde geldt voor aminozuursequenties: "
                  "<strong>hetzelfde eiwit verschilt minder bij nauwe verwanten</strong>."),
            ("p", "Daarbij komt dat <strong>alle bekende organismen dezelfde genetische code "
                  "gebruiken</strong>, dus een <strong>universele</strong> code; dat is het "
                  "sterkste <strong>moleculaire</strong> argument. Dat wijst op één "
                  "gemeenschappelijke <strong>oercel</strong>."),
            ("p", "Uit de <strong>biogeografie</strong> komt de verspreiding van soorten. De "
                  "buideldieren van Australië lijken weinig op die elders omdat "
                  "<strong>Australië vroeg van de andere continenten losraakte</strong>; dat "
                  "traag uit elkaar schuiven heet <strong>continentendrift</strong> of "
                  "<strong>continentdrift</strong>."),
            ("p", "En soms is evolutie rechtstreeks te volgen: "
                  "<strong>de antibioticaresistentie van bacteriën</strong> is er een voorbeeld "
                  "van."),
        ]),
        dict(kop="Drie theorieën", blokken=[
            ("p", "<strong>Lamarck</strong> dacht dat "
                  "<strong>wat een dier gebruikt groeit, en dat het dat doorgeeft</strong>: gebruik "
                  "en onbruik, plus de erfelijkheid van verworven eigenschappen. Dat tweede klopt "
                  "niet, want <strong>wat je tijdens je leven verandert, zit niet in je "
                  "gameten</strong>."),
            ("p", "De <strong>bioloog Charles Darwin</strong> beschreef de evolutie door "
                  "natuurlijke selectie. Zijn theorie steunt op drie gedachten: "
                  "<strong>variatie, selectie en erfelijkheid</strong>. Met <strong>survival of "
                  "the fittest</strong> bedoelde hij dat <strong>wie het best past bij zijn "
                  "omgeving meer nakomelingen krijgt</strong> — fit betekent passend, niet "
                  "gespierd."),
            ("p", "Bij een lange giraffennek is het verschil duidelijk: "
                  "<strong>bij Lamarck rekt het dier zijn nek, bij Darwin had het die al</strong>."),
            ("p", "De <strong>moderne evolutietheorie</strong> voegt daar de genetica aan toe: "
                  "<strong>mutaties als bron van nieuwe allelen</strong> en <strong>het rekenen "
                  "met allelfrequenties in een populatie</strong>. Ze verklaart de variatie dus "
                  "met <strong>mutaties</strong> en met de <strong>herverdeling van "
                  "allelen</strong> bij de meiose en de bevruchting. Een "
                  "<strong>populatie</strong> zijn alle individuen van één soort in hetzelfde "
                  "gebied; de <strong>allelfrequentie</strong> is <strong>het aandeel van een "
                  "allel in die populatie</strong>."),
            ("p", "Variatie ontstaat <strong>door mutaties in het DNA</strong> en "
                  "<strong>door mixing en crossing-over bij de meiose</strong>. "
                  "<strong>Zonder variatie kan er geen natuurlijke selectie plaatsvinden</strong>. "
                  "En <strong>een individu kan niet evolueren</strong>: evolutie gebeurt over "
                  "generaties."),
            ("p", "<strong>Mutaties ontstaan toevallig, niet op bestelling</strong>, en "
                  "<strong>de omgeving bepaalt welke een voordeel zijn</strong>. Daarom worden "
                  "bacteriën resistent doordat <strong>de resistente exemplaren overleven en "
                  "zich voortplanten</strong>, en niet doordat het antibioticum hen resistent "
                  "maakt. Hetzelfde geldt voor de peper-en-zoutvlinder: <strong>op roetzwarte "
                  "bomen werden de donkerder vlinders minder opgegeten</strong>. Dat is de "
                  "<strong>verklaring</strong> voor de verschuiving."),
            ("p", "Een kenmerk dat beter past, heet een <strong>adaptatie</strong> of "
                  "<strong>aanpassing</strong>. De druk die de omgeving daarbij uitoefent, heet "
                  "de <strong>selectiedruk</strong>: die <strong>bevoordeelt</strong> wie beter "
                  "past, en dat heeft niets met <strong>kracht</strong> te maken. "
                  "<strong>Biodiversiteit</strong> is <strong>de verscheidenheid aan soorten, "
                  "genen en ecosystemen</strong>. Een populatie met weinig genetische "
                  "diversiteit is kwetsbaar, want <strong>er is weinig variatie om op te "
                  "selecteren bij verandering</strong>."),
        ]),
    ],
    onthoud=[
        "Homoloog wijst op verwantschap, analoog niet.",
        "Fossielen, embryo's, DNA en verspreiding wijzen alle dezelfde kant op.",
        "Lamarck: verworven eigenschappen. Darwin: variatie, selectie, erfelijkheid.",
        "De moderne theorie voegt mutaties en allelfrequenties toe.",
        "Mutaties zijn toevallig; de omgeving kiest wat bruikbaar is.",
    ],
)

# ───────────────────────── 18. Selectie, soortvorming en de menswording
BUNDELS["selectie-soortvorming-en-de-menswording-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Selectie, soortvorming en de menswording",
    onder="Wat allelfrequenties doet schuiven, hoe een soort splitst, en hoe de mens ontstond.",
    secties=[
        dict(kop="Natuurlijke selectie en fitness", blokken=[
            ("p", "<strong>Natuurlijke selectie</strong> is "
                  "<strong>het proces waarbij beter aangepaste individuen meer nakomelingen "
                  "nalaten</strong>. De <strong>fitness</strong> van een fenotype zegt dus "
                  "<strong>niet hoe sterk of gespierd een dier is</strong>, maar hoeveel het "
                  "bijdraagt aan de volgende generatie."),
            ("p", "De strijd om voedsel, ruimte of een partner heet <strong>competitie</strong> "
                  "of <strong>concurrentie</strong>. Bij <strong>seksuele selectie</strong> "
                  "<strong>kiezen partners elkaar op bepaalde kenmerken</strong>. Daarom draagt "
                  "een pauwenhaan een zware staart, ook al bemoeilijkt die het vluchten: de "
                  "<strong>hennen</strong> kiezen de <strong>hanen</strong> met de grootste "
                  "staart, en zo <strong>krijgt hij meer nakomelingen</strong>. Zo kan "
                  "<strong>een kenmerk dat het overleven bemoeilijkt, toch toenemen</strong>."),
        ]),
        dict(kop="Drift, gene flow en de mens als selecteur", blokken=[
            ("p", "<strong>Gene flow</strong>, met de Engelse term, of "
                  "<strong>genenstroom</strong> is <strong>het binnenkomen en vertrekken van "
                  "allelen doordat individuen in- of uitwijken</strong>. Gene flow "
                  "<strong>maakt twee populaties met de tijd meer aan elkaar gelijk</strong>."),
            ("p", "<strong>Genetische drift</strong> is "
                  "<strong>de toevallige verschuiving van allelfrequenties</strong>. Ze speelt "
                  "sterker in een kleine populatie, want <strong>één toevallige gebeurtenis weegt "
                  "daar veel zwaarder door in de verhoudingen</strong>. Drift "
                  "<strong>bevoordeelt de best aangepaste individuen niet</strong>: ze is blind."),
            ("p", "Bij een <strong>flessenhalseffect</strong> <strong>blijft na een ramp maar "
                  "een handvol individuen over, met slechts een deel van de allelen</strong>. "
                  "Blijven er na een storm nog vijf hagedissen over op een eiland, dan is dat "
                  "het <strong>mechanisme</strong> van de flessenhals: de populatie "
                  "<strong>krimpt</strong> en <strong>verliest</strong> allelen. Bij het "
                  "<strong>stichterseffect</strong> <strong>sticht een klein groepje elders een "
                  "nieuwe populatie</strong>; waaien er vogels naar een onbewoond eiland, dan "
                  "is dat het <strong>mechanisme</strong> van het stichterseffect."),
            ("p", "Vier <strong>mechanismen</strong> kunnen de allelfrequenties van een "
                  "populatie veranderen: <strong>natuurlijke selectie</strong>, "
                  "<strong>mutatie</strong>, <strong>genetische drift</strong> en <strong>gene "
                  "flow</strong>. Een nadelig allel verdwijnt zelden helemaal uit een grote "
                  "populatie, want <strong>heterozygote dragers geven het ongemerkt "
                  "door</strong>."),
            ("p", "De mens selecteert zelf ook: bij <strong>kunstmatige</strong> of "
                  "<strong>artificiële selectie</strong> <strong>kiest niet de omgeving maar de "
                  "mens de ouderdieren</strong>. Dat gebeurt bij <strong>veredeling van "
                  "gewassen</strong>, bijvoorbeeld om grotere <strong>korrels</strong> te "
                  "<strong>kweken</strong>, en bij <strong>het fokken van rassen</strong>, "
                  "bijvoorbeeld <strong>honden</strong> met een bepaald "
                  "<strong>uitzicht</strong>."),
            ("p", "Bij bacteriën gaat evolutie sneller dan bij zoogdieren, want <strong>ze "
                  "delen veel sneller</strong>, <strong>ze komen in enorme aantallen "
                  "voor</strong> en <strong>ze kunnen onderling DNA uitwisselen</strong>."),
        ]),
        dict(kop="Soort en soortvorming", blokken=[
            ("p", "Twee dieren horen tot dezelfde <strong>soort</strong> als ze "
                  "<strong>samen vruchtbare nakomelingen kunnen krijgen</strong>. "
                  "<strong>Speciatie</strong> is <strong>het ontstaan van een nieuwe soort uit een "
                  "bestaande</strong>. Daarvoor is nodig: <strong>variatie</strong>, "
                  "<strong>isolatie tussen de groepen</strong> en "
                  "<strong>genoeg tijd</strong>."),
            ("p", "<strong>Geografische isolatie</strong> is "
                  "<strong>een scheiding door een rivier, een gebergte of een zee</strong>. Bij "
                  "<strong>allopatrische</strong> soortvorming "
                  "<strong>raken de twee groepen ruimtelijk gescheiden</strong>; bij "
                  "<strong>sympatrische</strong> soortvorming blijven ze in hetzelfde gebied en "
                  "scheiden ze zich <strong>door een verschil in gedrag, leefplek of "
                  "bloeitijd</strong>."),
            ("p", "<strong>Prezygotische</strong> isolatie werkt vóór de bevruchting, "
                  "<strong>postzygotische</strong> erna. De prezygotische vormen onderscheid je "
                  "aan wat precies de paring of de bevruchting tegenhoudt."),
            ("kader", tabel(["vorm", "wat de twee soorten scheidt", "voorbeeld"],
                            [["<strong>ethologische of gedragsisolatie</strong>",
                              "het gedrag: ze herkennen elkaar niet als partner",
                              "twee kikkersoorten in hetzelfde <strong>moeras</strong> kwaken verschillend, zodat ze niet <strong>paren</strong>"],
                             ["<strong>temporele isolatie</strong>",
                              "de tijd: ze zijn niet tegelijk vruchtbaar",
                              "twee <strong>plantensoorten</strong> bloeien in een ander deel van het jaar"],
                             ["<strong>ecologische isolatie</strong> of <strong>habitatisolatie</strong>",
                              "de plek: ze bewonen een ander <strong>habitat</strong> binnen hetzelfde gebied",
                              "de ene soort leeft in de boomtoppen, de andere op de grond"],
                             ["<strong>gametische isolatie</strong> of <strong>gameetisolatie</strong>",
                              "de geslachtscellen zelf passen niet",
                              "een zaadcel kan de eicel van de andere soort niet bevruchten"]])),
            ("p", "Postzygotische isolatie werkt pas ná de bevruchting: er komt wel een "
                  "nakomeling, maar die zet de lijn niet voort. Een <strong>muildier</strong>, "
                  "dat zelf onvruchtbaar is, is daar het bekendste voorbeeld van."),
        ]),
        dict(kop="De menswording", blokken=[
            ("p", "De hele groep mensachtigen, <strong>waartoe ook de uitgestorven soorten "
                  "behoren</strong>, heet de <strong>hominiden</strong>. De mens deelt met de "
                  "mensapen onder meer <strong>een grijphand met een opponeerbare "
                  "duim</strong>, <strong>goed ruimtelijk zicht</strong> en <strong>een lange "
                  "zorg voor de jongen</strong>, met sterke <strong>sociale banden</strong> en "
                  "<strong>grijpbare</strong> handen. De mens stamt <strong>niet rechtstreeks "
                  "af van de chimpansee</strong>: beide hebben een gemeenschappelijke "
                  "voorouder."),
            ("p", "Als eerste grote <strong>verandering</strong> wordt <strong>het rechtop gaan "
                  "lopen</strong> gezien. Daarbij horen deze <strong>lichamelijke "
                  "veranderingen</strong>: <strong>een S-vormige wervelkolom</strong>, een "
                  "<strong>breder, kommervormig bekken</strong> en <strong>een "
                  "voetboog</strong>. Een groter hersenvolume kostte onze voorouders ook iets: "
                  "<strong>veel energie, en een moeilijker bevalling</strong>."),
            ("p", "Met <strong>theory of mind</strong> bedoelt men <strong>het vermogen in te "
                  "schatten dat iemand anders iets anders denkt, weet of voelt dan "
                  "jij</strong>. Natuurlijke selectie speelde ook bij de menswording: "
                  "<strong>wie beter kon samenwerken en communiceren, liet meer nakomelingen "
                  "na</strong>."),
        ]),
    ],
    onthoud=[
        "Fitness is nakomelingen nalaten, niet spierkracht.",
        "Vier motoren: selectie, mutatie, drift en gene flow.",
        "Flessenhals is overblijven na een ramp, stichterseffect is elders beginnen.",
        "Allopatrisch is gescheiden gebied, sympatrisch is hetzelfde gebied.",
        "Prezygotisch verhindert de bevruchting, postzygotisch de vruchtbare nakomeling.",
        "Rechtop lopen eerst, een groter brein daarna.",
    ],
)

# ───────────────────────── 19. Biomoleculen
BUNDELS["biomoleculen-sachariden-lipiden-en-proteinen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Biomoleculen: sachariden, lipiden en proteïnen",
    onder="De drie grote groepen bouwstoffen, van hun bouwsteen tot hun functie.",
    secties=[
        dict(kop="Sachariden", blokken=[
            ("p", "<strong>Monosachariden</strong> zijn de enkelvoudige suikers: "
                  "<strong>glucose, fructose en galactose</strong>. Opgelost heeft glucose "
                  "<strong>een ring van zes atomen</strong> en fructose "
                  "<strong>een ring van vijf</strong>."),
            ("p", "Twee monosachariden samen geven een disacharide: <strong>lactose bestaat uit "
                  "glucose en galactose</strong>. De binding tussen twee suikerringen heet een "
                  "<strong>glycosidebinding</strong> of <strong>glycosidische binding</strong>."),
            ("p", "Bij een <strong>condensatiereactie</strong> <strong>worden twee bouwstenen "
                  "aan elkaar gekoppeld en komt er water vrij</strong>. Bij "
                  "<strong>hydrolyse</strong> of een <strong>hydrolysereactie</strong> "
                  "<strong>wordt een molecule met behulp van water weer gesplitst</strong>. Dat "
                  "paar komt bij alle drie de groepen terug."),
            ("p", "<strong>Polysachariden</strong> zijn lange ketens. Energie slaan "
                  "<strong>zetmeel</strong> (bij planten) en <strong>glycogeen</strong> (bij "
                  "dieren) op; zetmeel bestaat uit <strong>amylose en amylopectine</strong>. "
                  "<strong>Cellulose</strong> is een bouwstof: ze is geschikt voor een celwand "
                  "omdat <strong>de rechte ketens naast elkaar sterke vezels vormen</strong>, "
                  "als <strong>kabels</strong> in de wand. Een mens kan cellulose niet "
                  "<strong>verteren</strong>, want <strong>hij heeft het enzym voor die binding "
                  "niet</strong>."),
            ("p", "Snelle suikers zijn <strong>kort, dus sneller in het bloed</strong>; trage "
                  "suikers zijn <strong>lange ketens die eerst afgebroken moeten "
                  "worden</strong>."),
        ]),
        dict(kop="Lipiden", blokken=[
            ("p", "Een <strong>triglyceride</strong> bestaat uit <strong>glycerol en drie "
                  "vetzuren</strong>. Een <strong>onverzadigd</strong> vetzuur <strong>heeft "
                  "een of meer dubbele bindingen</strong> en <strong>heeft daar een knik in "
                  "zijn staart</strong>. Daardoor is olie bij <strong>kamertemperatuur</strong> "
                  "vloeibaar en boter vast: <strong>geknikte staarten kunnen zich minder dicht "
                  "tegen elkaar stapelen</strong>."),
            ("p", "Lipiden dienen in het lichaam als <strong>energievoorraad</strong>, als "
                  "<strong>isolatielaag</strong> die de warmte <strong>vasthoudt</strong>, in "
                  "het <strong>vetweefsel</strong> dat energie kan <strong>opslaan</strong>, "
                  "als <strong>bouwstof van de membranen</strong> en als <strong>grondstof voor "
                  "hormonen</strong>. Vet levert per gram meer energie dan suiker, want "
                  "<strong>het is sterker gereduceerd en bevat dus meer waterstof om te "
                  "oxideren</strong>."),
            ("p", "Een <strong>fosfolipide</strong> is geschikt om een membraan te vormen omdat "
                  "<strong>het een waterminnende kop en twee waterafstotende staarten "
                  "heeft</strong>. Een molecule die water afstoot, heet "
                  "<strong>hydrofoob</strong> of <strong>apolair</strong>."),
            ("p", "<strong>Cholesterol</strong> is <strong>geen sacharide</strong> maar een "
                  "lipide, en het zit in het <strong>celmembraan van dieren</strong>, niet in een "
                  "plantencelwand. Vitaminen die in vet oplossen, "
                  "<strong>kunnen in het lichaam wél opgeslagen worden</strong> — daarom kan een "
                  "overdosis ervan schaden."),
        ]),
        dict(kop="Proteïnen", blokken=[
            ("p", "Elk <strong>aminozuur</strong> heeft <strong>een aminogroep en een "
                  "carboxylgroep</strong> gemeenschappelijk; wat verschilt is <strong>de "
                  "restgroep, zijketen of zijgroep</strong>. Twee aminozuren worden verbonden "
                  "door een <strong>peptidebinding</strong>; een lange keten heet een "
                  "<strong>polypeptide</strong> of <strong>polypeptideketen</strong> en heeft "
                  "als uiteinden een <strong>aminozijde of N-terminus</strong> en een "
                  "<strong>carboxylzijde of C-terminus</strong>."),
            ("p", "De <strong>primaire structuur</strong> is <strong>de volgorde van de "
                  "aminozuren</strong>. De <strong>secundaire structuur</strong> omvat de "
                  "<strong>alfahelix</strong> en de <strong>bètaplaat</strong>. De "
                  "<strong>tertiaire structuur</strong>, de ruimtelijke vouw, of "
                  "<strong>plooiing</strong> wordt vastgehouden door "
                  "<strong>waterstofbruggen</strong>, <strong>zwavelbruggen</strong> of "
                  "<strong>disulfidebindingen</strong>, <strong>ionbindingen</strong> tussen "
                  "<strong>geladen</strong> zijgroepen en <strong>hydrofobe "
                  "interacties</strong>. Bestaat een eiwit uit meerdere ketens, dan heet dat de "
                  "<strong>quaternaire structuur</strong>."),
            ("p", "Een eiwit dat door verhitting zijn vorm verliest, is "
                  "<strong>gedenatureerd</strong>. Een gedenatureerd enzym werkt niet meer, "
                  "want <strong>zijn actieve plaats of actief centrum past niet meer op het "
                  "substraat</strong>: die vorm is <strong>verloren</strong>. Zo bepaalt de "
                  "volgorde van de aminozuren de werking: <strong>ze bepaalt de vouw, en de "
                  "vouw bepaalt wat het eiwit kan</strong>. <strong>Eén veranderd aminozuur kan "
                  "de werking van een heel eiwit bederven</strong>, zoals bij sikkelcelanemie."),
            ("p", "Proteïnen <strong>vervullen</strong> in een cel bijna elke taak en "
                  "<strong>zorgen</strong> voor bijna alles: <strong>reacties versnellen als "
                  "enzym</strong>, <strong>stoffen vervoeren</strong>, <strong>bouwen en "
                  "steunen</strong> en <strong>signalen doorgeven</strong>. De samentrekking "
                  "van een spier doen <strong>actine en myosine</strong>. "
                  "<strong>Keratine</strong>, niet collageen, geeft haren en nagels hun "
                  "hardheid; collageen zit in bindweefsel. Het kanaaleiwit dat water door het "
                  "membraan laat, is <strong>aquaporine</strong>. Een "
                  "<strong>transcriptiefactor</strong> is een proteïne die <strong>de "
                  "genexpressie mee stuurt</strong>, en een <strong>antilichaam</strong> is er "
                  "een die <strong>ziekteverwekkers herkent</strong>."),
            ("p", "In de darm worden proteïnen <strong>door hydrolyse tot aminozuren "
                  "afgebroken</strong>. En dat is wat polysachariden, lipiden en proteïnen "
                  "gemeenschappelijk hebben: <strong>het zijn grote moleculen die uit kleinere "
                  "bouwstenen gevormd zijn, met koolstof als basis</strong>."),
        ]),
    ],
    onthoud=[
        "Condensatie bouwt op en geeft water af, hydrolyse breekt af met water.",
        "Zetmeel en glycogeen slaan op, cellulose bouwt.",
        "Onverzadigd betekent dubbele binding, dus een knik, dus vloeibaar.",
        "Een fosfolipide heeft een hydrofiele kop en hydrofobe staarten.",
        "Primair is de volgorde, secundair helix en plaat, tertiair de vouw, quaternair meerdere ketens.",
        "De volgorde bepaalt de vouw en de vouw bepaalt de werking.",
    ],
)

# ───────────────────────── 20. Veilig en duurzaam werken in het labo
BUNDELS["veilig-en-duurzaam-werken-in-het-labo-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig en duurzaam werken in het labo",
    onder="Wat je leest voor je begint, hoe je meet, en wat je met de resten doet.",
    secties=[
        dict(kop="Voor je begint", blokken=[
            ("p", "Voor je met een product werkt, lees je altijd eerst "
                  "<strong>het etiket met de gevarenpictogrammen</strong>. En voor je een toestel "
                  "gebruikt, lees je de handleiding, want "
                  "<strong>daarin staat hoe je het veilig gebruikt en wat het niet mag</strong>. "
                  "Op een etiket staat ook hoe je het product bewaart, want "
                  "<strong>verkeerd bewaren maakt het gevaarlijker of onbruikbaar</strong>."),
            ("p", "Voor je een proef start, kijk je ook na "
                  "<strong>waar de nooddouche en de oogdouche hangen</strong>."),
        ]),
        dict(kop="Meten", blokken=[
            ("p", "Het <strong>meetbereik</strong> van een instrument is <strong>de kleinste en "
                  "de grootste waarde die het kan meten</strong>. De <strong>resolutie</strong> "
                  "is <strong>de kleinste waarde die je nog kunt onderscheiden</strong>; ze "
                  "bepaalt de <strong>nauwkeurigheid</strong> of <strong>precisie</strong> van "
                  "je meting, en dus hoe <strong>betrouwbaar</strong> ze is."),
            ("p", "Goed meten betekent: <strong>het juiste instrument voor de grootte van wat "
                  "je meet kiezen</strong>, <strong>recht van voren aflezen</strong>, "
                  "<strong>elke meting met zijn eenheid noteren</strong> en <strong>meerdere "
                  "keren meten</strong>. Een balans zet je altijd op nul voor je iets afweegt. "
                  "Een meettoestel zet je uit als je niet meet, want <strong>dat spaart stroom "
                  "of batterijen</strong> en de levensduur van het toestel; zo "
                  "<strong>spaar</strong> je energie. Noteer bij een meetwaarde ook "
                  "<strong>evenveel cijfers als het toestel aangeeft</strong>."),
            ("p", "Tijdens een proef noteer je meteen wat je doet en meet, want "
                  "<strong>achteraf uit het hoofd gaan er gegevens verloren</strong>."),
        ]),
        dict(kop="Veilig hanteren", blokken=[
            ("p", "Breekt er glaswerk, dan <strong>verwittig je de leraar</strong>, "
                  "<strong>raak je de scherven niet met de hand aan</strong> en <strong>ruim je "
                  "ze met borstel en blik op in de bak voor glasafval</strong>; "
                  "<strong>opruimen</strong> doe je dus nooit met de blote hand. Mors je iets, "
                  "dan <strong>meld je het en ruim je het op volgens de voorschriften</strong>."),
            ("p", "Elektrische toestellen bedien je nooit met natte handen. Bij een "
                  "<strong>bunsenbrander</strong> let je erop dat <strong>lang haar "
                  "vastzit</strong>, dat <strong>er geen brandbare producten in de buurt "
                  "staan</strong>, dat <strong>losse kledij</strong> en losse mouwen weg zijn "
                  "en dat <strong>je de vlam nooit onbewaakt laat</strong>. Een veiligheidsbril "
                  "draag je bij het verhitten van een vloeistof, want <strong>die kan plots "
                  "opspatten of overkoken</strong>. Een warm bekerglas pak je vast met een "
                  "<strong>bekerglastang</strong> of een hittebestendige handschoen; een kolf "
                  "hang je aan de <strong>statiefarm</strong>. En een warme kolf zet je niet "
                  "meteen op een koude stenen tafel, want <strong>door het plotse "
                  "temperatuurverschil kan het glas barsten</strong>."),
            ("p", "Je ruikt nooit aan een product door het flesje recht onder je neus te "
                  "houden: je wappert de damp voorzichtig naar je toe. "
                  "<strong>Pipetteert</strong> een <strong>leerling</strong> met de mond om "
                  "<strong>sneller</strong> te werken, dan is dat fout: <strong>het product kan "
                  "in je mond terechtkomen</strong> of ingeademd worden; daar bestaat een "
                  "pipetvuller voor. Glaswerk maak je <strong>nadien</strong> onmiddellijk "
                  "<strong>schoon</strong>, want <strong>opgedroogde resten gaan er veel "
                  "moeilijker af en kunnen de volgende proef bederven</strong>."),
            ("p", "Een <strong>microscoop</strong> draag je aan <strong>de arm en de "
                  "voet</strong>. Bij het <strong>bekijken</strong> van een preparaat begin je "
                  "met het kleinste objectief, want <strong>daarmee vind je het beeld het "
                  "gemakkelijkst terug</strong>; <strong>vermijd</strong> dus om meteen met de "
                  "grootste vergroting te starten. Bij de grootste vergroting stel je scherp "
                  "met <strong>de fijne stelschroef</strong>, niet met de grove: anders druk je "
                  "het objectief in het preparaat."),
        ]),
        dict(kop="Pictogrammen en biologisch materiaal", blokken=[
            ("p", "Een pictogram met <strong>een vlam</strong> op een <strong>oranje of rood "
                  "omrand ruitje</strong> betekent <strong>brandbaar</strong> of "
                  "<strong>ontvlambaar</strong>. Een <strong>doodshoofd</strong> waarschuwt "
                  "voor <strong>giftig</strong>: het <strong>toont</strong> dat de stof een "
                  "<strong>acute vergiftiging</strong> kan geven. Een hand en een oppervlak "
                  "waarop een vloeistof inwerkt, staat voor <strong>bijtend of "
                  "corrosief</strong>. Een product <strong>zonder</strong> pictogram is daarmee "
                  "<strong>niet automatisch volkomen veilig</strong>: je blijft voorzichtig."),
            ("p", "In een labo eet of drink je niet, want <strong>je kunt onbedoeld een product "
                  "of micro-organisme in je lichaam binnenkrijgen</strong>. Met een "
                  "bacteriekweek in een petrischaal werk je zo: <strong>je houdt het deksel "
                  "zoveel mogelijk gesloten</strong>, je <strong>wast nadien grondig je "
                  "handen</strong>, <strong>je opent ze niet onnodig</strong> en <strong>je "
                  "laat ze achteraf steriliseren</strong>. Het werkblad "
                  "<strong>schoonmaken</strong> of <strong>ontsmetten</strong> doe je "
                  "<strong>vooraf</strong> én nadien, in beide <strong>richtingen</strong> om "
                  "<strong>besmetting te voorkomen</strong>: je <strong>ontsmet</strong> dus "
                  "<strong>vooraf om je proef zuiver te houden</strong> en <strong>achteraf om "
                  "jezelf en de volgende gebruiker veilig te houden</strong>."),
            ("p", "<strong>Steriliseren</strong> is <strong>het volledig kiemvrij maken van "
                  "materiaal</strong>, meestal met stoom onder druk in een "
                  "<strong>autoclaaf</strong>: dat heet ook <strong>autoclaveren</strong>. "
                  "Handschoenen draag je bij menselijk of dierlijk weefsel, want <strong>daarin "
                  "kunnen ziekteverwekkers zitten</strong>. Met levende organismen werk je zo "
                  "dat ze zo weinig mogelijk ongemak hebben."),
            ("p", "Spat er een bijtend product in je oog, dan <strong>spoel je het oog meteen "
                  "lang met veel water aan de oogdouche</strong>; dat "
                  "<strong>uitspoelen</strong> doe je als eerste, nog voor al het andere en "
                  "verwittig je de leraar."),
        ]),
        dict(kop="Afval en duurzaamheid", blokken=[
            ("p", "Biologisch afval mag <strong>niet</strong> gewoon bij het restafval: het "
                  "gaat naar de voorziene inzameling, meestal na sterilisatie. Chemisch afval "
                  "giet je niet in de gootsteen, want <strong>het komt in het oppervlaktewater "
                  "terecht en belast het milieu</strong>; het hoort in het "
                  "<strong>afvalvat</strong> dat <strong>daarvoor</strong> klaarstaat. Een "
                  "afgemeten rest giet je ook niet terug in de voorraadfles, want dan besmet je "
                  "de hele fles; die rest gaat naar het juiste afval, en de maatbeker "
                  "<strong>spoel</strong> je <strong>uit</strong>."),
            ("p", "Duurzaam werken is onder meer <strong>niet meer afmeten dan je nodig "
                  "hebt</strong>, <strong>toestellen uitzetten na gebruik</strong>, "
                  "<strong>afval gescheiden houden</strong> en <strong>materiaal hergebruiken "
                  "waar het kan</strong>: dat zijn de duurzame <strong>werkwijzen</strong>. "
                  "Laat een <strong>leerling</strong> een microscooplamp een hele les branden "
                  "zonder te kijken, dan <strong>verbruikt energie en verkort de levensduur van "
                  "de lamp</strong>."),
            ("p", "Duurzaam werken hoort bij veilig werken, want "
                  "<strong>minder product en minder afval betekent ook minder risico voor "
                  "jezelf en voor de omgeving</strong>."),
        ]),
    ],
    onthoud=[
        "Eerst het etiket en de handleiding, dan pas het product.",
        "Meetbereik is van waar tot waar, resolutie is hoe fijn.",
        "Microscoop: dragen aan arm en voet, scherpstellen fijn bij grote vergroting.",
        "Vlam is brandbaar, doodshoofd is giftig, de hand is bijtend.",
        "Geen enkele rest terug in de fles, geen chemisch afval in de gootsteen.",
        "Minder product en minder afval is tegelijk veiliger en duurzamer.",
    ],
)

# ───────────────────────── 21. Wetenschappelijk onderzoek, ontwerpen en STEM
BUNDELS["wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="Van onderzoeksvraag tot besluit, en van eis tot prototype.",
    secties=[
        dict(kop="De onderzoeksvraag en de hypothese", blokken=[
            ("p", "Een onderzoek begint met <strong>een onderzoeksvraag</strong>. Een goede "
                  "vraag <strong>kenmerkt</strong> zich doordat ze het onderwerp "
                  "<strong>duidelijk afbakent</strong> en dus <strong>nauwkeurig "
                  "afgebakend</strong> is, <strong>met een proef of meting te "
                  "beantwoorden</strong> en <strong>in één zin te stellen</strong>. Ze moet dus "
                  "zo gesteld zijn dat een meting ze kan beantwoorden."),
            ("p", "Het verwachte antwoord dat je vooraf opschrijft, is de "
                  "<strong>hypothese</strong>. Een hypothese die weerlegd wordt, betekent "
                  "<strong>niet dat de proef mislukt is</strong>: ook dat is een resultaat."),
        ]),
        dict(kop="Variabelen en een eerlijke opstelling", blokken=[
            ("p", "De <strong>onafhankelijke variabele</strong> is <strong>wat je zelf "
                  "verandert</strong>, de <strong>afhankelijke variabele</strong> is "
                  "<strong>wat je meet</strong>. Onderzoek je of meer licht de fotosynthese "
                  "versnelt, dan is de afhankelijke variabele <strong>de hoeveelheid zuurstof "
                  "die de plant afgeeft</strong>, bijvoorbeeld de "
                  "<strong>zuurstofbelletjes</strong> per <strong>minuut</strong>; de "
                  "lichtsterkte is wat je zelf <strong>instelt</strong>. Factoren die je in "
                  "elke opstelling gelijk houdt, zijn de <strong>constante variabelen</strong>. "
                  "De reeks zonder de onderzochte factor is de <strong>controlegroep</strong>, "
                  "<strong>controleproef</strong> of <strong>blanco</strong>, waarmee je je "
                  "resultaat <strong>vergelijkt</strong>."),
            ("p", "Test je een meststof op tien planten in de zon en tien zonder meststof in de "
                  "schaduw, dan is er <strong>meer dan één factor verschillend, dus weet je "
                  "niet waaraan het verschil ligt</strong>. Wil je weten of een enzym sneller "
                  "werkt bij hogere temperatuur, dan zet je <strong>dezelfde reeks bij "
                  "verschillende temperaturen, met al het andere gelijk</strong>: bijvoorbeeld "
                  "<strong>vijf buizen met hetzelfde enzym bij vijf temperaturen</strong>."),
            ("p", "In een onderzoeksplan hoort <strong>de onderzoeksvraag en de hypothese</strong>, "
                  "<strong>welke variabelen je verandert, meet en gelijk houdt</strong>, "
                  "<strong>het nodige materiaal</strong> en "
                  "<strong>de werkwijze stap voor stap</strong>."),
        ]),
        dict(kop="Metingen en betrouwbaarheid", blokken=[
            ("p", "Je herhaalt een meting meerdere keren, want <strong>zo zie je of een "
                  "afwijkende waarde toeval is</strong>: de <strong>afwijkingen "
                  "uitmiddelen</strong> maakt het resultaat sterker. Met vijftig zaden werk je "
                  "liever dan met drie, want <strong>bij een groter aantal weegt een "
                  "uitzondering minder zwaar door</strong>: een grotere "
                  "<strong>steekproef</strong> is <strong>betrouwbaarder</strong>."),
            ("p", "Een <strong>systematische of toevallige fout die je door beter werken kunt "
                  "vermijden</strong>, is bijvoorbeeld <strong>scheef aflezen of vergeten te "
                  "ijken</strong>, of een <strong>stopwatch</strong> te laat "
                  "<strong>indrukken</strong>; zo’n <strong>meetfout</strong> kan je door beter "
                  "werken vermijden. Een meting die duidelijk buiten de rij valt, is een "
                  "<strong>uitschieter</strong> of <strong>uitbijter</strong>. Zo'n meting of "
                  "een meting die niet in je verwachting past, <strong>mag je niet gewoon "
                  "weglaten</strong>: je noteert ze en zegt wat je ervan denkt. Wat tijdens de "
                  "proef misliep, hoort dus ook in je verslag."),
            ("p", "Je noteert je waarnemingen tijdens de proef, niet achteraf uit het hoofd. "
                  "Een <strong>waarneming</strong> is <strong>wat je ziet of meet</strong>; een "
                  "<strong>besluit</strong> is <strong>wat je daaruit afleidt</strong>. Iemand "
                  "anders moet je proef kunnen overdoen, want <strong>zo kan ze nagekeken "
                  "worden</strong> en <strong>zo weet je of het resultaat betrouwbaar "
                  "is</strong>. Pas als het resultaat bij iemand anders "
                  "<strong>terugkomt</strong>, is het betrouwbaar, en zo komt ook een fout in "
                  "je werkwijze aan het licht. Dat <strong>herhalen</strong> om na te gaan of "
                  "hetzelfde eruit komt, heet <strong>repliceren</strong> of "
                  "<strong>reproduceren</strong>; het resultaat heeft dan "
                  "<strong>reproduceerbaarheid</strong>."),
        ]),
        dict(kop="Grafieken en besluiten", blokken=[
            ("p", "Op de <strong>horizontale as</strong> zet je <strong>wat je zelf veranderd "
                  "hebt</strong>. Bij elke as horen <strong>de naam van de grootheid</strong>, "
                  "<strong>de eenheid</strong> en <strong>een regelmatige verdeling met "
                  "getallen</strong>. Een as mag je <strong>niet</strong> bij een willekeurige "
                  "waarde laten beginnen: dat vertekent het beeld. Een groei die je in de tijd "
                  "volgt, zet je in een <strong>lijngrafiek</strong> of "
                  "<strong>lijndiagram</strong>. Op de verticale as komt wat je "
                  "<strong>gemeten</strong> hebt."),
            ("p", "Het <strong>gemiddelde</strong>, of <strong>rekenkundig</strong> gemiddelde, "
                  "krijg je door alle metingen op te tellen en te delen door hun aantal. Hebben "
                  "twee reeksen hetzelfde gemiddelde maar liggen de metingen in de ene veel "
                  "verder uit elkaar, dan besluit je <strong>dat die reeks minder betrouwbaar "
                  "is en meer spreiding heeft</strong>: haar gemiddelde is "
                  "<strong>onzekerder</strong>."),
            ("p", "Toont een grafiek dat er meer ijsjes verkocht worden als er meer mensen "
                  "verdrinken, dan besluit je <strong>dat er een derde factor meespeelt, "
                  "namelijk warm weer</strong>. Want <strong>een verband tussen twee grootheden "
                  "betekent niet dat de ene de andere veroorzaakt</strong>: een verband is geen "
                  "<strong>gevolg</strong>."),
            ("p", "In een besluit hoort <strong>een antwoord op de onderzoeksvraag</strong>, "
                  "<strong>of de hypothese bevestigd of weerlegd is</strong> en <strong>waarop "
                  "je dat baseert</strong>. Je <strong>legt je gegevens vast</strong> in een "
                  "tabel of grafiek. Achteraf reflecteer je over je werkwijze, want <strong>zo "
                  "zie je wat je volgende keer beter aanpakt</strong>. Je laat je besluit door "
                  "anderen nalezen, want <strong>zij zien fouten, gaten en denkfouten die jij "
                  "over het hoofd ziet</strong>."),
        ]),
        dict(kop="Ontwerpen en STEM", blokken=[
            ("p", "Ontwerpen begint met <strong>de eisen waaraan de oplossing moet "
                  "voldoen</strong>. Een eerste werkend model dat je bouwt en test, is een "
                  "<strong>prototype</strong> of <strong>proefmodel</strong>. Voldoet het niet "
                  "aan de eisen, dan <strong>pas je het ontwerp aan en test je "
                  "opnieuw</strong>: <strong>aanpassen</strong> hoort bij ontwerpen. Daarin "
                  "verschilt ontwerpen van onderzoeken: <strong>onderzoeken wil iets weten, "
                  "ontwerpen wil een probleem oplossen</strong>."),
            ("p", "<strong>STEM</strong> staat voor <strong>science</strong> of wetenschappen, "
                  "<strong>technology</strong> of <strong>techniek</strong> en "
                  "<strong>technologie</strong>, <strong>engineering</strong> en "
                  "<strong>mathematics</strong> of <strong>wiskunde</strong>. Wil een school "
                  "het waterverbruik van haar serre verlagen, dan is een goede eerste stap "
                  "<strong>meten hoeveel water er nu verbruikt wordt en waaraan</strong>. Een "
                  "goede oplossing houdt ook rekening met de kosten en met het milieu."),
        ]),
    ],
    onthoud=[
        "Vraag, hypothese, plan, proef, resultaat, besluit, reflectie.",
        "Onafhankelijk verander je, afhankelijk meet je, constant houd je gelijk.",
        "Eén factor per keer anders, al het andere gelijk.",
        "Een weerlegde hypothese is een resultaat, geen mislukking.",
        "Een verband is geen oorzaak.",
        "Onderzoeken wil weten, ontwerpen wil oplossen.",
    ],
)
