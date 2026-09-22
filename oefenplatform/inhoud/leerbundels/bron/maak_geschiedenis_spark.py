# -*- coding: utf-8 -*-
"""De leerbundels voor geschiedenis op ✨ Spark-niveau.

Gebaseerd op de vakfiche geschiedenis 1ste graad A-stroom. Eén bundel per
thema, niet per deel: deel 1 en deel 2 van hetzelfde thema behandelen dezelfde
leerstof, alleen met moeilijkere vragen. Kim uploadt de bundel dus twee keer,
één keer bij elk deel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

SPARK = "✨ Spark — 1ste en 2de middelbaar"

BUNDELS = {}

PERIODES = [
    ("prehistorie", -3800, -3300, "#9a948a"),
    ("oude nabije oosten", -3300, -800, "#c17f2b"),
    ("klassieke oudheid", -800, 476, "#a2521f"),
    ("middeleeuwen", 476, 1500, "#2f5d50"),
    ("vroegmoderne tijd", 1500, 1789, "#5b7f9c"),
    ("moderne tijd", 1789, 1945, "#7a5b8f"),
    ("hedendaagse tijd", 1945, 2025, "#3f7a46"),
]

BUNDELS["historisch-referentiekader"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het historisch referentiekader",
    onder="Hoe historici het verleden ordenen in tijd, in ruimte en in domeinen.",
    secties=[
        dict(kop="Wat doet een historicus?", blokken=[
            ("p", "Een <strong>historicus</strong> onderzoekt het verleden. Hij was er zelf niet bij, "
                  "dus hij moet het afleiden uit wat er van vroeger overblijft: geschreven teksten, "
                  "voorwerpen, gebouwen, afbeeldingen. Dat noemen we <strong>bronnen</strong>."),
            ("p", "Een <strong>archeoloog</strong> haalt die bronnen uit de grond. De twee werken vaak "
                  "samen, maar het is niet hetzelfde beroep: de archeoloog graaft op, de historicus legt uit."),
            ("kader", "Het verleden is alles wat gebeurd is. <strong>Geschiedenis</strong> is het verhaal "
                      "dat historici daarover vertellen op basis van bronnen. Die twee zijn dus niet hetzelfde, "
                      "en dat is meteen waarom er over geschiedenis gediscussieerd kan worden."),
        ]),
        dict(kop="Tijd meten", blokken=[
            ("p", "Om over het verleden te kunnen praten, moet je het eerst kunnen aanduiden. Honderd jaar "
                  "is een <strong>eeuw</strong>, duizend jaar is een <strong>millennium</strong>."),
            ("fig", svg.eeuwenbalk(),
             "Let op het lastige: het jaar 1350 hoort bij de 14de eeuw, niet bij de 13de. Een eeuw loopt van 01 tot en met 00."),
            ("p", "Onze jaartelling begint bij het jaar 0. Wat daarvoor ligt, krijgt de toevoeging "
                  "<strong>v.C.</strong> (voor Christus), wat daarna komt <strong>n.C.</strong> (na Christus)."),
            ("fig", svg.jaartellijn(),
             "Vóór Christus tel je achterwaarts. 800 v.C. ligt dus vroeger dan 300 v.C., ook al is 800 het grotere getal."),
            ("kader", "<strong>Chronologie</strong> is de volgorde van vroeger naar later. Zet je "
                      "gebeurtenissen op een <strong>tijdlijn</strong>, dan zie je die volgorde in één oogopslag, "
                      "én hoeveel tijd er tussen zit."),
        ]),
        dict(kop="De zeven periodes", blokken=[
            ("p", "Historici knippen het verleden in stukken, zodat ze erover kunnen praten. In het westen "
                  "gebruiken ze daarvoor zeven periodes."),
            ("fig", svg.tijdlijn(PERIODES, [(-3300, "schrift", "boven"), (476, "val van Rome", "onder"),
                                            (1789, "Franse Revolutie", "boven")]),
             "De prehistorie staat hier als een kort stukje links, maar duurde in werkelijkheid honderdduizenden jaren — veel langer dan alle andere periodes samen."),
            ("p", "De volgorde ken je best vanbuiten: prehistorie, oude nabije oosten, klassieke oudheid, "
                  "middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd."),
        ]),
        dict(kop="Scharnierpunten", blokken=[
            ("p", "Waarom ligt de grens tussen twee periodes net dáár? Omdat er iets gebeurde dat zo "
                  "ingrijpend was dat historici er een nieuwe periode mee laten beginnen. Zo'n gebeurtenis "
                  "heet een <strong>scharnierpunt</strong>."),
            ("fig", svg.stappen(["het schrift|einde prehistorie", "macht naar de|Middellandse Zee",
                                 "val van het West-|Romeinse Rijk"]),
             "Drie scharnierpunten uit de periodes die jij bestudeert."),
            ("p", "Het <strong>schrift</strong> maakt een einde aan de prehistorie: vanaf dan zijn er "
                  "geschreven bronnen. Als de macht verschuift van de rijken bij Tigris en Eufraat naar de "
                  "steden rond de <strong>Middellandse Zee</strong>, begint de klassieke oudheid. En met de "
                  "ondergang van het <strong>West-Romeinse Rijk in 476</strong> beginnen de middeleeuwen."),
        ]),
        dict(kop="Situeren in de ruimte", blokken=[
            ("p", "Naast wanneer, vraagt een historicus ook waar. Daarvoor bestaan vaste begrippen. "
                  "<strong>Lokaal</strong> is één plaats, <strong>regionaal</strong> een streek, "
                  "<strong>continentaal</strong> een heel werelddeel."),
            ("p", "<strong>Stedelijk</strong> en <strong>ruraal</strong> zetten stad en platteland tegenover "
                  "elkaar. <strong>Maritiem</strong> betekent gericht op de zee. Athene was maritiem: het "
                  "leefde van zijn vloot en zijn handel overzee. Sparta lag in het binnenland en was "
                  "continentaal: het leefde van zijn land."),
        ]),
        dict(kop="De vier maatschappelijke domeinen", blokken=[
            ("p", "Een samenleving heeft veel kanten tegelijk. Om er orde in te brengen, verdelen historici "
                  "alles in vier <strong>maatschappelijke domeinen</strong>."),
            ("fig", svg.domeinen(),
             "Eén gebeurtenis hoort vaak in meerdere domeinen tegelijk. Dat is geen fout, dat is juist het punt."),
            ("p", "Een voorbeeld. Alexander de Grote verovert een wereldrijk: dat is <strong>politiek</strong>. "
                  "Maar door die verovering verspreidt de Griekse taal en kunst zich over dat hele gebied, en "
                  "dat is <strong>cultureel</strong>. De handel die op gang komt, is <strong>economisch</strong>."),
            ("weetje", "Historici zoeken graag naar <em>verbanden</em> tussen de domeinen. Waarom leidt een "
                       "betere oogst (economisch) tot grotere steden (sociaal) en tot machtigere koningen "
                       "(politiek)? Dat soort vragen maakt geschiedenis interessanter dan een rij jaartallen."),
        ]),
        dict(kop="Continuïteit, verandering, evolutie en revolutie", blokken=[
            ("p", "<strong>Continuïteit</strong> is wat gelijk blijft; <strong>verandering</strong> is wat "
                  "anders wordt. In elke periode zitten allebei tegelijk."),
            ("p", "Verandert er iets traag en stap voor stap, dan noemen we dat een <strong>evolutie</strong>. "
                  "Gaat het snel en grondig, dan spreken we van een <strong>revolutie</strong>. Het verschil "
                  "zit in het tempo, niet in of iets goed of slecht is."),
            ("kader", "De overgang naar de landbouw heet de <strong>agrarische revolutie</strong>. Toch duurde "
                      "ze duizenden jaren. Naar gevolgen gemeten was het een omwenteling, naar tempo gemeten "
                      "een evolutie. Allebei de antwoorden zijn juist, als je uitlegt waarom."),
        ]),
        dict(kop="De grenzen van deze indeling", blokken=[
            ("p", "De zeven periodes zijn een <strong>afspraak</strong> onder historici, geen natuurwet. "
                  "Dat heeft drie gevolgen, en die moet je kunnen uitleggen."),
            ("p", "Ze is <strong>tijdsgebonden</strong>: de grenzen zijn gekozen en kunnen verschuiven als er "
                  "nieuwe inzichten komen. Ze is <strong>plaatsgebonden</strong>: de val van het West-Romeinse "
                  "Rijk betekende in China of Amerika helemaal niets. En ze is "
                  "<strong>gebonden aan domeinen</strong>: politiek kan een periode aflopen terwijl mensen "
                  "cultureel gewoon verderdoen zoals vroeger."),
            ("weetje", "Het spijkerschrift ontstond in Mesopotamië rond 3300 v.C. In onze streken werd pas "
                       "duizenden jaren later geschreven. De prehistorie eindigde hier dus veel later dan daar. "
                       "Eén grens voor de hele wereld bestaat niet."),
        ]),
    ],
    onthoud=[
        "Een historicus onderzoekt het verleden met bronnen; een archeoloog graaft ze op.",
        "Eeuw = 100 jaar, millennium = 1000 jaar. Het jaar 1492 hoort bij de 15de eeuw.",
        "v.C. telt achterwaarts: 800 v.C. ligt vroeger dan 300 v.C.",
        "De zeven periodes: prehistorie, oude nabije oosten, klassieke oudheid, middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd.",
        "Een scharnierpunt is de overgang tussen twee periodes: het schrift, de macht naar de Middellandse Zee, 476.",
        "Ruimte: lokaal, regionaal, stedelijk, ruraal, continentaal, maritiem.",
        "De vier domeinen: politiek, sociaal, economisch, cultureel.",
        "Evolutie gaat traag, revolutie snel. Continuïteit blijft, verandering niet.",
        "De westerse periodisering is tijdsgebonden, plaatsgebonden en domeingebonden.",
    ])


BUNDELS["prehistorie"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="De prehistorie",
    onder="Van de eerste mensachtigen tot de boeren die niet meer verder trokken.",
    secties=[
        dict(kop="De tijd zonder geschreven bronnen", blokken=[
            ("p", "<strong>Prehistorie</strong> betekent letterlijk: de tijd vóór de geschiedenis. Niet omdat "
                  "er niets gebeurde, maar omdat er nog niets werd opgeschreven. Alles wat we weten, komt uit "
                  "de grond: botten, werktuigen, resten van vuur, schilderingen op een grotwand."),
            ("p", "Het is veruit de langste periode: honderdduizenden jaren, meer dan alle andere periodes "
                  "samen. Alles wat daarna komt, past in een paar duizend jaar."),
        ]),
        dict(kop="De evolutie van de mens", blokken=[
            ("p", "De mens ontstond in <strong>Afrika</strong>. Van daaruit trokken verschillende soorten "
                  "mensachtigen de wereld in, de ene na de andere."),
            ("fig", svg.stappen(["mensachtigen|in Afrika", "homo erectus|trekt weg", "homo sapiens|over de wereld"]),
             "De homo erectus, de rechtopgaande mens, was de eerste die Afrika verliet. De homo sapiens, de verstandige mens, volgde later."),
            ("p", "De eerste mensachtigen waren <strong>aaseter-verzamelaars</strong>: ze verzamelden planten "
                  "en aten vlees van dieren die al dood waren. Pas later gingen ze zelf jagen, en werden ze "
                  "<strong>jager-verzamelaars</strong>."),
            ("kader", "De <strong>evolutieleer</strong> zegt dat soorten langzaam veranderen: wie het best "
                      "past bij zijn omgeving, krijgt meer nakomelingen, en zo verschuift een soort over heel "
                      "veel generaties. De mens is niet uit de aap ontstaan, wel hebben mens en aap een "
                      "gemeenschappelijke voorouder."),
        ]),
        dict(kop="Leven als jager en verzamelaar", blokken=[
            ("p", "Jagers en verzamelaars leefden in <strong>kleine groepen</strong> van enkele tientallen "
                  "mensen. Groter kon niet: in de natuur vind je op één plek niet genoeg eten voor meer monden."),
            ("p", "Ze waren <strong>nomadisch</strong>. Als het voedsel in een streek opraakte of de kudden "
                  "verder trokken, trokken zij mee. Bezit had weinig zin, want alles moest mee op de rug."),
            ("weetje", "Het verzamelde plantaardige voedsel leverde vaak méér op dan de jacht. Het beeld van "
                       "de prehistorische mens die alleen maar mammoeten at, klopt dus niet."),
            ("fig", svg.stenen_werktuigen(),
             "Vuursteen splijt in vlijmscherpe schilfers. Aan die afslagvlakjes herken je een bewerkte steen van een gewone."),
        ]),
        dict(kop="Het vuur", blokken=[
            ("p", "Vuur was de belangrijkste vondst van de prehistorie. Het gaf <strong>warmte</strong> en "
                  "<strong>licht</strong>, hield roofdieren op afstand, en hardde houten speerpunten."),
            ("p", "Het grootste verschil maakte het <strong>bereiden van voedsel</strong>. Gekookt of "
                  "geroosterd eten is beter verteerbaar en veiliger, want de hitte doodt ziektekiemen. Er kwam "
                  "dus meer energie uit hetzelfde voedsel."),
            ("kader", "Een vuur brandt ook alleen als je erbij blijft. Rond dat vuur zaten mensen samen, en "
                      "daar werd verteld, doorgegeven en geleerd."),
        ]),
        dict(kop="Kunst in de grotten", blokken=[
            ("p", "Diep in grotten schilderden mensen dieren op de wand: paarden, bizons, herten. Ze gebruikten "
                  "oker voor geel en rood, en houtskool voor zwart. Soms legden ze hun hand op de wand en "
                  "bliezen er verf omheen."),
            ("fig", svg.grotschildering(),
             "Hier nagetekend. De bekendste zijn Lascaux in Frankrijk en Altamira in Spanje; die van Lascaux zijn zo'n 17 000 jaar oud."),
            ("p", "Waarom ze dat deden, weten we niet zeker. Het waren geen versieringen voor de woonplaats: "
                  "de schilderingen zitten net op plekken waar niemand woonde, soms honderden meters diep."),
        ]),
        dict(kop="De agrarische revolutie", blokken=[
            ("p", "Ongeveer <strong>tienduizend jaar geleden</strong> gebeurde er iets wat alles veranderde: "
                  "mensen begonnen zelf gewassen te telen en dieren te houden. Dat heet de "
                  "<strong>agrarische revolutie</strong>."),
            ("p", "Het begon in de <strong>Vruchtbare Halve Maan</strong>, de streek van Tigris en Eufraat tot "
                  "de Middellandse Zee. Daar groeiden de wilde voorouders van tarwe en gerst, en leefden dieren "
                  "die je kon temmen."),
            ("fig", svg.nomadisch_sedentair(),
             "Het omslagpunt: niet langer achter het voedsel aan trekken, maar het laten groeien waar je woont."),
            ("p", "Wie zaait, moet blijven tot de oogst. Zo werd de mens <strong>sedentair</strong>: hij woonde "
                  "op een vaste plaats. De eerste dorpen ontstonden."),
        ]),
        dict(kop="Wat daaruit volgde", blokken=[
            ("p", "Een boer die meer oogst dan hij zelf opeet, houdt een <strong>overschot</strong> over. Dat "
                  "kan je bewaren of ruilen, en daarmee begint een kettingreactie."),
            ("fig", svg.stappen(["overschot", "specialisatie", "dorpen|en steden", "ongelijkheid"]),
             "Elke stap volgt uit de vorige. Zonder voedseloverschot geen van alle."),
            ("p", "Als niet meer iedereen voedsel moet maken, kunnen sommigen iets anders gaan doen: "
                  "pottenbakker, smid, priester. Dat heet <strong>specialisatie</strong>. En omdat er nu "
                  "genoeg te eten is op één plek, kunnen veel meer mensen samenwonen. Zo worden dorpen steden."),
            ("p", "Er is ook een keerzijde. Wie grond en voorraden bezit, staat sterker dan wie niets heeft: "
                  "er ontstaat <strong>ongelijkheid</strong>. En doordat mensen dicht op elkaar en tussen hun "
                  "vee leven, springen <strong>ziektes</strong> makkelijker over. Eén misoogst kan meteen "
                  "hongersnood betekenen."),
        ]),
        dict(kop="Revolutie of evolutie?", blokken=[
            ("p", "Naar <strong>gevolgen</strong> gemeten was de overgang naar de landbouw een revolutie: "
                  "wonen, werken, eten, bezit en samenleven veranderden allemaal."),
            ("p", "Naar <strong>tempo</strong> gemeten was het een evolutie: de landbouw deed er duizenden "
                  "jaren over om zich over Europa te verspreiden, en ontstond op verschillende plaatsen "
                  "onafhankelijk van elkaar."),
            ("kader", "Op je examen mag je allebei antwoorden, zolang je uitlegt vanuit welke kant je kijkt. "
                      "Het argument telt, niet het woord."),
            ("p", "De periode waarin dit gebeurt, heet het <strong>neolithicum</strong> of de nieuwe steentijd. "
                  "Je herkent de werktuigen eraan dat ze geslepen en gepolijst zijn in plaats van enkel "
                  "afgeslagen. Bij ons liggen er nog grafheuvels en grote steenzettingen uit die tijd."),
        ]),
    ],
    onthoud=[
        "Prehistorie = de tijd zonder geschreven bronnen, veruit de langste periode.",
        "De mens ontstond in Afrika; de homo erectus trok als eerste weg.",
        "Jagers en verzamelaars leefden nomadisch, in kleine groepen; verzamelen leverde vaak het meeste op.",
        "Vuur gaf warmte, licht, bescherming en beter verteerbaar voedsel.",
        "Grotschilderingen tonen vooral dieren; Lascaux en Altamira zijn de bekendste.",
        "De agrarische revolutie begon ± 10 000 jaar geleden in de Vruchtbare Halve Maan.",
        "Landbouw maakt sedentair: overschot, specialisatie, steden — maar ook ongelijkheid en ziekte.",
        "Naar gevolgen een revolutie, naar tempo een evolutie. Het neolithicum is de nieuwe steentijd.",
    ])

BUNDELS["mesopotamie-en-egypte"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Mesopotamië en Egypte",
    onder="De eerste steden, het eerste schrift en de eerste staten — allebei aan een rivier.",
    secties=[
        dict(kop="Twee rijken aan een rivier", blokken=[
            ("p", "Rond 3300 v.C. ontstaan er twee samenlevingen die alles veranderen. Allebei liggen ze "
                  "in een droog gebied, en allebei danken ze hun bestaan aan een rivier."),
            ("p", "<strong>Mesopotamië</strong> betekent letterlijk <em>land tussen de rivieren</em>: het "
                  "ligt tussen de <strong>Tigris</strong> en de <strong>Eufraat</strong>, in wat vandaag "
                  "grotendeels Irak is. <strong>Egypte</strong> ligt in een smalle strook langs de "
                  "<strong>Nijl</strong>; daarbuiten is het woestijn."),
            ("kader", "Deze periode heet het <strong>oude nabije oosten</strong>. Ze begint bij de "
                      "uitvinding van het schrift rond 3300 v.C. — precies daarom eindigt de prehistorie daar. "
                      "Vanaf nu zijn er geschreven bronnen."),
        ]),
        dict(kop="Water, en wat je ervoor moet organiseren", blokken=[
            ("p", "In een droog land regent het te weinig om te boeren. De oplossing is "
                  "<strong>irrigatielandbouw</strong>: je leidt rivierwater via kanalen en dijken naar je "
                  "akkers. In Egypte hielp de Nijl daarbij nog extra, want die overstroomde elk jaar en "
                  "liet een laag vruchtbaar slib achter."),
            ("fig", svg.irrigatie(),
             "Een kanalenstelsel graven en onderhouden is geen werk voor één boer. Daar heb je veel mensen voor nodig, en afspraken."),
            ("p", "En daar zit de kern van dit hoofdstuk. Wie het graafwerk organiseert, wie beslist welke "
                  "akker eerst water krijgt en wie de voorraad bewaart, heeft <strong>macht</strong>. Uit de "
                  "nood aan samenwerking groeit dus een <strong>bestuur</strong>."),
            ("p", "Omdat een goed bevloeide akker veel meer opbrengt dan nodig, ontstaat er een "
                  "<strong>overschot</strong>. Dat voedt mensen die zelf niet boeren: ambachtslieden, "
                  "priesters, soldaten, ambtenaren. Die gaan samenwonen rond het bestuur, en zo groeit een "
                  "stad."),
        ]),
        dict(kop="De eerste steden en staten", blokken=[
            ("p", "In Mesopotamië ontstaan zo de eerste <strong>stadstaten</strong>: een stad met het land "
                  "eromheen, met een eigen bestuur en een eigen god. Ur, Uruk en Babylon zijn de bekendste. "
                  "Ze lagen niet onder één koning, maar voerden ook oorlog met elkaar."),
            ("p", "Egypte gaat een andere weg. Daar smelten de gebieden langs de Nijl samen tot één rijk "
                  "onder één heerser: de <strong>farao</strong>. Eén rivier, één land."),
            ("kader", "Een <strong>ambtenaar</strong> is iemand die in dienst van de heerser bestuurt: hij "
                      "meet akkers op, int belastingen, houdt de voorraad bij. Zonder ambtenaren is een staat "
                      "van deze omvang onmogelijk."),
        ]),
        dict(kop="Het schrift", blokken=[
            ("p", "Wie graan van honderden boeren moet bijhouden, kan dat niet onthouden. Daarom wordt het "
                  "schrift uitgevonden: niet om verhalen te bewaren, maar om <strong>te tellen en te "
                  "boekhouden</strong>. De oudste kleitabletten zijn voorraadlijsten."),
            ("p", "In Mesopotamië schrijft men met een rietstengel in natte klei. De afdrukken hebben de "
                  "vorm van wiggen of spijkers: het <strong>spijkerschrift</strong>. In Egypte gebruikt men "
                  "<strong>hiërogliefen</strong>, tekens die op kleine afbeeldingen lijken, op steen en op "
                  "papyrus."),
            ("fig", svg.hierogliefen(),
             "Hiërogliefen zijn geen tekeningetjes van wat ze voorstellen: sommige staan voor een klank, andere voor een woord."),
            ("p", "Schrijven was moeilijk en duurde jaren om te leren. Daardoor kon maar een kleine groep "
                  "het: de <strong>schrijvers</strong>. Wie kan lezen en schrijven, kan wetten opstellen, "
                  "afspraken vastleggen en bezit bewijzen. Het schrift maakt de machtigen dus nog machtiger."),
            ("kader", "Hiërogliefen waren eeuwenlang onleesbaar. De <strong>Steen van Rosetta</strong> "
                      "bracht de doorbraak: daarop staat dezelfde tekst in hiërogliefen én in het Grieks, en "
                      "Grieks kon men wél lezen."),
        ]),
        dict(kop="Wie staat waar?", blokken=[
            ("p", "Allebei de samenlevingen zijn een <strong>standenmaatschappij</strong>: de bevolking valt "
                  "uiteen in vaste lagen, en in welke laag je terechtkomt, ligt vast bij je geboorte. "
                  "Opklimmen kan nauwelijks."),
            ("fig", svg.standenpiramide([
                ("farao of koning", "één persoon"),
                ("priesters en ambtenaren", "besturen en rekenen"),
                ("schrijvers en handelaars", "kunnen lezen"),
                ("ambachtslieden", "pottenbakker, smid"),
                ("boeren", "veruit de grootste groep"),
                ("slaven", "geen rechten, geldt als bezit"),
            ]),
             "Hoe lager in de piramide, hoe meer mensen. De brede onderkant draagt met haar werk de smalle top."),
            ("p", "Onderaan staan de <strong>slaven</strong>: krijgsgevangenen, of mensen die zich door "
                  "schulden hebben moeten verkopen. Zij hebben geen rechten en gelden als bezit."),
            ("p", "Je ziet die ongelijkheid terug in de bronnen zelf. Wetten straffen dezelfde daad zwaarder "
                  "naargelang wie het slachtoffer is, en graven verschillen enorm: de ene krijgt goud mee, "
                  "de andere een kuil."),
        ]),
        dict(kop="Goden, tempels en graven", blokken=[
            ("p", "Beide volkeren zijn <strong>polytheïstisch</strong>: ze geloven in veel goden tegelijk, "
                  "elk met een eigen taak — de zon, de rivier, de oogst, de oorlog."),
            ("fig", svg.ziggurat(),
             "De ziggurat is een trapvormige tempeltoren. Hij stond midden in de stad en was van ver te zien."),
            ("p", "De tempel is niet enkel een gebedshuis. Hij bezit grond, slaat graan op en betaalt "
                  "werkers uit. Dat noemt men een <strong>tempeleconomie</strong>: godsdienst en economie "
                  "lopen door elkaar."),
            ("p", "In Egypte is de farao zelf goddelijk: hij geldt als een god op aarde en als de schakel "
                  "tussen de goden en de mensen. Hij bestuurt, spreekt recht, leidt het leger en de "
                  "eredienst."),
            ("fig", svg.piramides(),
             "Een piramide is een graf. De Egyptenaren geloofden in een leven na de dood, en daar hoorde een lichaam bij."),
            ("p", "Daarom <strong>mummificeerden</strong> ze hun doden: het lichaam moest bewaard blijven "
                  "om verder te kunnen leven. In het graf legden ze voorwerpen, eten en het "
                  "<strong>Dodenboek</strong>, een verzameling spreuken voor de tocht na de dood."),
            ("kader", "<strong>Toetanchamon</strong> was een onbelangrijke farao die jong stierf. Zijn graf "
                      "is wereldberoemd om één reden: het is als enige vrijwel ongeschonden teruggevonden. "
                      "Alle andere waren al in de oudheid leeggeroofd."),
        ]),
        dict(kop="Handel zonder geld", blokken=[
            ("p", "Mesopotamië heeft klei en graan in overvloed, maar geen steen, geen hout en geen metaal. "
                  "Wie dat wil, moet het halen. Daarom is <strong>handel</strong> daar geen luxe maar een "
                  "noodzaak, over water en over land."),
            ("p", "Munten bestaan nog niet. Men werkt met <strong>ruilhandel</strong>, en rekent daarbij af "
                  "in vaste maten graan of zilver, gewogen op een weegschaal. Wat er geruild is, wordt op een "
                  "kleitablet gezet — weer dat schrift."),
        ]),
        dict(kop="Wat wij eraan overhielden", blokken=[
            ("p", "Uit deze twee rijken komt verrassend veel van wat wij vanzelfsprekend vinden: het "
                  "<strong>wiel</strong>, de <strong>ploeg</strong>, geschreven <strong>wetten</strong>, en "
                  "de <strong>sterrenkunde</strong>."),
            ("p", "Ook de manier waarop wij tijd meten komt van daar: de verdeling van het uur in zestig "
                  "minuten gaat terug op het Mesopotamische rekenen met zestigtallen, en de kalender van "
                  "twaalf maanden op de Egyptische zonnekalender."),
            ("fig", svg.stappen(["rivier", "irrigatie", "overschot", "stad|en staat", "schrift"]),
             "De ketting van dit hoofdstuk. Elke stap maakt de volgende mogelijk — en aan het einde staat een samenleving die wij nog herkennen."),
        ]),
    ],
    onthoud=[
        "Mesopotamië = land tussen Tigris en Eufraat; Egypte = het land langs de Nijl.",
        "Het oude nabije oosten begint bij het schrift, rond 3300 v.C.",
        "Irrigatielandbouw vraagt samenwerking, en uit die samenwerking groeit bestuur en macht.",
        "Overschot → specialisatie → steden. Mesopotamië kreeg stadstaten, Egypte één rijk onder de farao.",
        "Spijkerschrift in klei, hiërogliefen op steen en papyrus; uitgevonden om te boekhouden.",
        "De Steen van Rosetta maakte hiërogliefen leesbaar, dankzij dezelfde tekst in het Grieks.",
        "Standenmaatschappij: je plaats ligt vast bij je geboorte; onderaan staan de slaven.",
        "Polytheïsme, ziggurat en tempeleconomie in Mesopotamië; goddelijke farao, mummies en piramides in Egypte.",
        "Handel ging per ruil, afgerekend in gewogen graan of zilver — munten bestonden nog niet.",
        "Van daar komen het wiel, de ploeg, geschreven wetten, de sterrenkunde, ons uur van 60 minuten en de 12 maanden.",
    ])

BUNDELS["het-oude-griekenland"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het oude Griekenland",
    onder="Honderden kleine stadstaten, twee heel verschillende voorbeelden, en denkers die het nog altijd doen.",
    secties=[
        dict(kop="Een land dat zichzelf opdeelt", blokken=[
            ("p", "Griekenland ligt aan de <strong>Middellandse Zee</strong> en bestaat uit bergen, "
                  "schiereilanden en honderden eilanden. Over land reizen is lastig, over zee gaat het vlot."),
            ("p", "Dat landschap stuurde de politiek. Omdat de gebieden moeilijk bij elkaar raakten, groeide "
                  "er geen groot rijk maar een lappendeken van kleine, zelfstandige stadstaten: de "
                  "<strong>polis</strong>. Elke polis had een eigen bestuur, eigen wetten, eigen munten en "
                  "een eigen beschermgod."),
            ("kader", "De Grieken voelden zich wél één volk: ze deelden taal, goden, verhalen en de "
                      "Olympische Spelen. Politiek waren ze verdeeld, cultureel niet. Dat noemen ze "
                      "<strong>Hellas</strong>."),
            ("p", "Er was te weinig vruchtbare grond voor een groeiende bevolking. Daarom trokken groepen weg "
                  "om elders een nieuwe stad te stichten: de <strong>kolonisatie</strong>. Zo kwamen er "
                  "Griekse steden tot in Zuid-Italië, Zuid-Frankrijk en rond de Zwarte Zee — en zo kwamen de "
                  "Romeinen al vroeg met Griekse cultuur in aanraking."),
        ]),
        dict(kop="Sparta en Athene: twee wegen", blokken=[
            ("p", "<strong>Sparta</strong> was een <strong>oligarchie</strong>: een kleine groep besliste. "
                  "Alles stond er in dienst van het leger. Jongens verlieten op hun zevende het gezin voor een "
                  "harde militaire opvoeding."),
            ("p", "Dat kon omdat de <strong>heloten</strong>, onvrije landbouwers, al het werk op het land "
                  "deden. Zij waren veruit in de meerderheid, en de angst voor een opstand hield Sparta mee in "
                  "dat keurslijf."),
            ("p", "<strong>Athene</strong> ging een andere weg: van oligarchie over een periode van "
                  "<strong>tirannen</strong> naar <strong>democratie</strong>. De burgers kwamen zelf samen op "
                  "de volksvergadering en stemden daar over de wetten. Dat heet een <em>directe</em> democratie."),
            ("kader", "Een <strong>tiran</strong> was bij de Grieken een alleenheerser die de macht gegrepen "
                      "had. Het woord betekende nog niet vanzelf 'wreed'; sommige tirannen waren juist geliefd "
                      "bij het gewone volk."),
            ("p", "De beperking is even belangrijk als de uitvinding. Enkel <strong>vrije mannen met "
                  "burgerrecht</strong> mochten stemmen. Vrouwen, slaven en vreemdelingen niet, ook al woonden "
                  "die er hun leven lang. Van de hele bevolking stemde ongeveer één op tien."),
            ("p", "Ook voor vrouwen verschilden de twee. Een Spartaanse vrouw mocht sporten, bezit hebben en "
                  "zich vrij bewegen; een Atheense vrouw leefde grotendeels binnenshuis. Meebeslissen deed ze "
                  "op geen van beide plaatsen."),
        ]),
        dict(kop="Twee oorlogen die alles veranderden", blokken=[
            ("p", "In de <strong>Perzische oorlogen</strong> stonden de Griekse stadstaten tegenover het "
                  "enorme Perzische Rijk. Uitzonderlijk genoeg werkten ze samen, en ze wonnen."),
            ("p", "Gevolg: Athene werd de leider van een bondgenootschap van stadstaten, en gebruikte het geld "
                  "daarvan onder meer om het <strong>Parthenon</strong> te bouwen. De andere leden begonnen "
                  "dat als overheersing te voelen."),
            ("p", "Dat liep uit op de <strong>Peloponnesische oorlog</strong>: Athene tegen Sparta, bijna "
                  "dertig jaar lang. Sparta won, maar alle Griekse stadstaten kwamen er verzwakt uit."),
            ("fig", svg.stappen(["Perzische|oorlogen", "Athene|machtig", "wrevel bij|de rest",
                                 "Peloponnesische|oorlog", "allen|verzwakt"]),
             "De ketting die Griekenland rijp maakte voor de Macedonische overname."),
        ]),
        dict(kop="Goden, orakels en spelen", blokken=[
            ("p", "De Grieken waren <strong>polytheïstisch</strong>. Hun goden woonden volgens de verhalen op "
                  "de berg <strong>Olympus</strong>, met <strong>Zeus</strong> als oppergod. Het waren geen "
                  "verheven wezens: ze werden jaloers, verliefd en kwaad, precies zoals mensen."),
            ("p", "Bij een moeilijke beslissing trok men naar een <strong>orakel</strong>, het bekendste in "
                  "Delphi. De antwoorden waren vaak dubbelzinnig, zodat ze achteraf altijd bleken te kloppen."),
            ("p", "De <strong>Olympische Spelen</strong> begonnen in 776 v.C. als een feest ter ere van Zeus "
                  "in Olympia. Tijdens de spelen gold een wapenstilstand, zodat deelnemers uit alle stadstaten "
                  "veilig konden reizen."),
            ("kader", "<strong>Mythologie</strong> is niet hetzelfde als geschiedenis. De verhalen over Theseus "
                      "en de Minotaurus of over de Trojaanse oorlog vertellen vooral hoe de Grieken zichzelf "
                      "zagen. Ze verwijzen soms naar echte gebeurtenissen, maar zijn er geen verslag van."),
        ]),
        dict(kop="Denken, en er niet mee ophouden", blokken=[
            ("p", "<strong>Socrates</strong> schreef zelf niets. Hij liep rond en stelde vragen, tot mensen "
                  "merkten dat ze zelf niet wisten wat ze dachten te weten. Dat maakte hem niet overal geliefd: "
                  "hij werd ter dood veroordeeld."),
            ("p", "Zijn leerling <strong>Plato</strong> schreef het wel op, en werd op zijn beurt de leraar van "
                  "<strong>Aristoteles</strong>, die zowat alles onderzocht wat hij tegenkwam — van sterren tot "
                  "slakken. Aristoteles was later de leraar van Alexander de Grote."),
            ("p", "Waarom noemt men dit het begin van de wetenschap? Omdat zij verklaringen begonnen te zoeken "
                  "<strong>in de natuur zelf</strong>, in plaats van bij de goden. Ook de geneeskunde nam die "
                  "wending: ziekte werd een zaak van het lichaam, niet van een vloek."),
            ("p", "In de literatuur staat <strong>Homeros</strong> vooraan, met de <em>Ilias</em> over de "
                  "Trojaanse oorlog en de <em>Odyssee</em> over een jarenlange thuisreis. In het theater "
                  "speelde men <strong>tragedies</strong>, waarin een held ten onder gaat aan zijn eigen fout."),
        ]),
        dict(kop="De drie zuilstijlen", blokken=[
            ("p", "Griekse bouwkunst werkt met <strong>zuilen en balken</strong>. Je herkent de stijl bovenaan "
                  "de zuil, aan het <strong>kapiteel</strong>."),
            ("fig", svg.zuilstijlen(),
             "Dorisch is het oudst en het soberst, Korintisch het jongst en het rijkst versierd."),
            ("p", "Bij de <strong>beeldhouwkunst</strong> zie je een duidelijke evolutie. "
                  "<strong>Archaïsche</strong> beelden staan stijf rechtop, met beide voeten naast elkaar en "
                  "een starre glimlach. <strong>Klassieke</strong> beelden zetten hun gewicht op één been, "
                  "waardoor het lichaam kantelt en het beeld lijkt te bewegen."),
            ("p", "Na Alexander, in de <strong>hellenistische</strong> periode, gaat het nog verder: dan tonen "
                  "beelden ook pijn, ouderdom en beweging in plaats van enkel het ideaal."),
        ]),
        dict(kop="Alexander en het hellenisme", blokken=[
            ("p", "De verzwakte stadstaten werden ingenomen door <strong>Macedonië</strong>, een koninkrijk in "
                  "het noorden. De zoon van die koning was <strong>Alexander de Grote</strong>."),
            ("p", "In ongeveer tien jaar veroverde hij het hele Perzische Rijk, tot in Egypte en tot aan de "
                  "rand van India. Hij stierf op zijn tweeëndertigste, en zijn generaals verdeelden het rijk "
                  "onder elkaar."),
            ("p", "Wat bleef, is het <strong>hellenisme</strong>: de vermenging van Griekse cultuur met die van "
                  "het oosten. Grieks werd de taal waarin men in dat hele gebied handel dreef en studeerde, "
                  "eeuwenlang, ook nog toen de Romeinen er de baas waren."),
        ]),
    ],
    onthoud=[
        "Bergen en zee verdeelden Griekenland in honderden zelfstandige stadstaten: de polis.",
        "Te weinig grond leidde tot kolonisatie rond de Middellandse Zee en de Zwarte Zee.",
        "Sparta: oligarchie, leger, heloten. Athene: van oligarchie over tirannie naar directe democratie.",
        "In Athene stemden enkel vrije mannelijke burgers — ongeveer één op tien van de bevolking.",
        "Perzische oorlogen: samen tegen buiten, Athene wordt machtig. Peloponnesische oorlog: Athene tegen Sparta, allen verzwakt.",
        "Polytheïsme, de Olympus met Zeus, orakels in Delphi, en vanaf 776 v.C. de Olympische Spelen.",
        "Socrates, Plato en Aristoteles zochten verklaringen in de natuur zelf: het begin van de wetenschap.",
        "Drie zuilstijlen: Dorisch (sober), Ionisch (krullen), Korintisch (bladeren).",
        "Beeldhouwkunst: archaïsch is stijf, klassiek beweegt, hellenistisch toont ook pijn en ouderdom.",
        "Alexander de Grote veroverde tot India; daarna bleef het hellenisme, Grieks als taal van het oosten.",
    ])

BUNDELS["het-romeinse-rijk"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het Romeinse Rijk",
    onder="Van één stad aan de Tiber tot een rijk rond de hele Middellandse Zee — en weer terug.",
    secties=[
        dict(kop="Van sage tot stad", blokken=[
            ("p", "Rome ontstond op de heuvels langs de <strong>Tiber</strong>, in Italië: ver genoeg van zee "
                  "om veilig te zijn, dicht genoeg om te handelen."),
            ("p", "De Romeinen vertelden zelf het verhaal van <strong>Romulus en Remus</strong>, twee "
                  "vondelingen die door een wolvin grootgebracht werden. Romulus doodde zijn broer en noemde "
                  "de stad naar zichzelf."),
            ("kader", "Zo'n stichtingsmythe is geen geschiedenis. Ze vertelt vooral hoe de Romeinen zichzelf "
                      "wilden zien: hard, door de goden gewild, en bereid alles voor de stad opzij te zetten."),
            ("p", "Het vroege Rome leerde veel van zijn buren: van de <strong>Etrusken</strong> de boog en "
                  "bestuursgewoonten, van de <strong>Grieken</strong> het alfabet, de goden en de kunst."),
        ]),
        dict(kop="De republiek", blokken=[
            ("p", "Eerst hadden koningen de macht. Toen de Romeinen hun laatste koning wegjoegen, wilden ze "
                  "nooit meer één alleenheerser. Zo ontstond de <strong>republiek</strong>, van <em>res "
                  "publica</em>: de zaak van iedereen."),
            ("p", "Aan het hoofd stonden twee <strong>consuls</strong>, elk voor één jaar verkozen. Twee, "
                  "zodat ze elkaar konden tegenhouden; één jaar, zodat niemand lang alleen de macht hield. "
                  "Alleen in uiterste nood benoemde men tijdelijk één <strong>dictator</strong>."),
            ("p", "De <strong>senaat</strong>, de raad van oud-bestuurders, gaf officieel enkel advies, maar "
                  "besliste in de praktijk over bijna alles. De <strong>volksvergadering</strong> koos de "
                  "bestuurders en stemde over de wetten — al stemden de rijkste groepen eerst en wogen die "
                  "het zwaarst."),
            ("p", "Binnen de stad stonden twee groepen tegenover elkaar: de <strong>patriciërs</strong>, de "
                  "oude rijke families, en de <strong>plebejers</strong>, het gewone volk. De plebejers "
                  "dwongen hun rechten stap voor stap af, onder meer door massaal het werk neer te leggen en "
                  "de stad te verlaten."),
        ]),
        dict(kop="Van stad tot wereldrijk", blokken=[
            ("p", "Eerst veroverde Rome het hele Italische schiereiland. Daarna botste het op "
                  "<strong>Carthago</strong>, de grote handelsmacht in Noord-Afrika. Dat werden de "
                  "<strong>Punische oorlogen</strong>."),
            ("p", "Rome won, Carthago werd uiteindelijk volledig verwoest, en Rome had geen tegenstander meer "
                  "in het westen. De Middellandse Zee werd <strong>mare nostrum</strong>: onze zee."),
            ("fig", svg.stappen(["stadstaat", "Italië", "Punische|oorlogen", "mare|nostrum", "imperium|Romanum"]),
             "Elke verovering maakte de volgende mogelijk — en maakte tegelijk de republiek onbestuurbaar."),
            ("p", "Het succes ondermijnde het bestuur. Oorlogen leverden zoveel slaven op dat grootgrondbezit "
                  "met slavenarbeid, het <strong>latifundium</strong>, spotgoedkoop werd. De kleine boer kon "
                  "daar niet tegenop, verkocht zijn grond en trok verarmd naar de stad."),
        ]),
        dict(kop="Van republiek naar keizerrijk", blokken=[
            ("p", "In de stad groeide zo een grote groep arme burgers. Politici hielden die tevreden met "
                  "gratis graan en spelen. Tegelijk kregen soldaten hun stuk land niet van de staat maar van "
                  "hun <strong>generaal</strong> — en dus volgden ze hem, desnoods tegen Rome in."),
            ("p", "Dat leidde tot een eeuw van <strong>burgeroorlogen</strong>: Marius tegen Sulla, daarna "
                  "Caesar tegen Pompeius. <strong>Julius Caesar</strong> won en liet zich dictator voor het "
                  "leven benoemen. Zijn tegenstanders zagen daarin een nieuwe koning en vermoordden hem in de "
                  "senaat."),
            ("p", "Na nog een burgeroorlog bleef zijn aangenomen zoon over: <strong>Augustus</strong>, de "
                  "eerste <strong>keizer</strong>. Hij noemde zich geen koning maar <em>princeps</em>, de "
                  "eerste burger, en liet de senaat en de ambten gewoon bestaan."),
            ("kader", "Dat was geen bescheidenheid maar berekening. De vormen van de republiek bleven staan, "
                      "terwijl de macht in één paar handen zat. Zo kreeg Rome het alleenbewind dat het vier "
                      "eeuwen eerder had afgezworen, zonder het zo te moeten noemen."),
        ]),
        dict(kop="Pax Romana", blokken=[
            ("p", "Onder de eerste keizers volgde een periode van ongeveer twee eeuwen rust binnen het rijk: "
                  "de <strong>Pax Romana</strong>, de Romeinse vrede. Aan de grenzen werd wel nog gevochten."),
            ("p", "Die rust was ook economie. Eén munt, één rechtssysteem, geen rovers en geen piraten: "
                  "goederen konden van Britannië tot Egypte reizen. Daarvoor bouwden de Romeinen wegen die "
                  "eeuwen meegingen."),
            ("fig", svg.heirbaan(),
             "Een Romeinse weg is opgebouwd uit lagen, met een bolle bovenkant zodat het regenwater afloopt."),
            ("p", "En water haalden ze van ver. Een <strong>aquaduct</strong> loopt kilometers lang heel licht "
                  "bergaf, zodat het water vanzelf blijft stromen tot in de stad."),
            ("fig", svg.aquaduct(),
             "Bogen op bogen, met bovenaan de goot. De boog is precies wat de Romeinen aan de Griekse bouwkunst toevoegden."),
        ]),
        dict(kop="Bouwen, geloven en kijken", blokken=[
            ("p", "De Grieken bouwden met zuilen en balken. De Romeinen voegden de <strong>boog</strong>, het "
                  "<strong>gewelf</strong>, de <strong>koepel</strong> en <strong>beton</strong> toe. Daarmee "
                  "konden ze veel grotere ruimtes overspannen."),
            ("fig", svg.amfitheater(),
             "Het Colosseum: een amfitheater is rondom gebouwd, zodat iedereen zicht heeft op het midden. Daar vochten gladiatoren."),
            ("p", "Ook hun beelden verschillen van de Griekse. Griekse beelden tonen het <strong>ideaal</strong>; "
                  "Romeinse portretten tonen de <strong>persoon</strong>, met rimpels, kale kruin en al. Pas "
                  "later lieten keizers zich weer jonger en goddelijker afbeelden dan ze waren."),
            ("p", "De Romeinen namen de Griekse goden over en gaven ze eigen namen: Zeus werd "
                  "<strong>Jupiter</strong>, Ares werd Mars, Aphrodite werd Venus. Daarbovenop kwam de "
                  "<strong>keizerscultus</strong>: de keizer zelf werd vereerd. In een rijk vol volkeren en "
                  "goden was dat het bindmiddel."),
            ("p", "Precies daarom botsten de <strong>christenen</strong>: zij weigerden de keizer te vereren. "
                  "Ze werden vervolgd, maar het christendom groeide toch, werd onder Constantijn toegelaten en "
                  "uiteindelijk zelfs staatsgodsdienst."),
        ]),
        dict(kop="Het einde van het westen", blokken=[
            ("p", "In de <strong>3de eeuw</strong> liep het mis: invallen aan de grenzen, munten die steeds "
                  "minder zilver bevatten, en keizers die elkaar in hoog tempo afzetten."),
            ("p", "Het rijk bleek te groot om vanuit één punt te besturen en werd gesplitst in een "
                  "<strong>West-</strong> en een <strong>Oost-Romeins Rijk</strong>. Het westen viel in "
                  "<strong>476</strong>; het oosten leefde als het Byzantijnse Rijk nog duizend jaar voort, "
                  "met Constantinopel als hoofdstad."),
            ("kader", "476 geldt als <strong>scharnierpunt</strong> naar de middeleeuwen. Dat is een afspraak "
                      "onder historici, geen dag waarop alles plots anders was. Voor de meeste mensen "
                      "veranderde er dat jaar niets."),
            ("p", "Wat bleef, zie je nog dagelijks: het <strong>Latijn</strong> in het Frans, Spaans en "
                  "Italiaans en in duizenden woorden bij ons, onze letters, onze maandnamen — juli en augustus "
                  "zijn naar Julius Caesar en Augustus genoemd — en het <strong>recht</strong>."),
        ]),
    ],
    onthoud=[
        "Rome ontstond aan de Tiber; de sage van Romulus en Remus is mythe, geen geschiedenis.",
        "Koningstijd → republiek → keizerrijk. De republiek had twee consuls per jaar, een senaat en een volksvergadering.",
        "Patriciërs tegen plebejers: het gewone volk dwong zijn rechten stap voor stap af.",
        "Punische oorlogen tegen Carthago maakten Rome baas over het westen: mare nostrum.",
        "Latifundia met slaven verdreven de kleine boer naar de stad; legers werden trouw aan hun generaal.",
        "Caesar werd vermoord als dictator; Augustus werd de eerste keizer en noemde zich princeps.",
        "Pax Romana: twee eeuwen rust, en daardoor handel over het hele rijk, over wegen en via aquaducten.",
        "De Romeinen voegden boog, gewelf, koepel en beton toe aan de Griekse bouwkunst.",
        "Portretbeelden tonen de mens zoals hij was; keizerscultus als bindmiddel, christendom van vervolgd tot staatsgodsdienst.",
        "Crisis van de 3de eeuw, splitsing, val van het westen in 476 — het oosten hield nog duizend jaar stand.",
    ])

BUNDELS["bronnen-kunst-en-beeldvorming"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Bronnen, kunst en beeldvorming",
    onder="Hoe je weet wat je weet — en waarom een historicus altijd vraagt wie er aan het woord is.",
    secties=[
        dict(kop="Verleden en geschiedenis", blokken=[
            ("p", "Het <strong>verleden</strong> is alles wat gebeurd is. Dat ligt vast en verandert nooit meer. "
                  "<strong>Geschiedenis</strong> is het verhaal dat historici daarover maken, op basis van wat "
                  "er van dat verleden overblijft."),
            ("p", "Die twee door elkaar halen, is de meest gemaakte fout. Precies omdat geschiedenis een "
                  "<em>constructie</em> is, kan ze herschreven worden — en gebeurt dat ook, telkens als er "
                  "nieuwe bronnen of nieuwe onderzoekstechnieken opduiken."),
            ("kader", "Dat is geen zwakte van het vak, maar de kern ervan. Een historicus die zegt "
                      "&bdquo;zo was het, punt&rdquo;, verzwijgt op welke bronnen hij steunt en wat hij "
                      "niet weet."),
        ]),
        dict(kop="Wat is een bron?", blokken=[
            ("p", "Een <strong>historische bron</strong> is alles uit het verleden waaruit je iets over die "
                  "tijd kan afleiden: een tekst, een voorwerp, een gebouw, een lied, een foto. Ook een "
                  "afvalhoop of een kinderspeeltje telt mee."),
            ("fig", svg.primair_secundair(),
             "Het onderscheid dat het vaakst verward wordt. Het gaat over tijd, niet over kwaliteit."),
            ("p", "Een <strong>primaire</strong> bron komt uit de tijd zelf: een brief van een Romeinse "
                  "soldaat, een grafsteen, een muntje. Een <strong>secundaire</strong> bron is later gemaakt "
                  "op basis van andere bronnen — je handboek bijvoorbeeld."),
            ("p", "Daarnaast deel je bronnen in naar hun <strong>vorm</strong>: geschreven, mondeling, "
                  "materieel of audiovisueel. Een opgegraven potscherf is materieel, een opgenomen gesprek met "
                  "een oudere is mondeling."),
        ]),
        dict(kop="Wie is er aan het woord?", blokken=[
            ("p", "Een bron valt niet uit de lucht. Iemand maakte ze, voor iemand, met een bedoeling. Daarom "
                  "kijkt een historicus altijd eerst naar de <strong>maker</strong>."),
            ("p", "Was die een <strong>ooggetuige</strong>, iemand die het zelf zag? Of een "
                  "<strong>tijdgenoot</strong>, die in dezelfde tijd leefde maar het van horen zeggen had? En "
                  "wie was de <strong>opdrachtgever</strong>, degene die betaalde?"),
            ("fig", svg.stappen(["de maker", "het publiek", "de bedoeling", "de inhoud"]),
             "Wie maakte het, voor wie, waarom — en pas dan: wat staat erin? In die volgorde."),
            ("p", "Dichtbij staan maakt iemand trouwens niet vanzelf betrouwbaar. Een ooggetuige ziet maar één "
                  "hoek van wat er gebeurt, kiest partij, en vergist zich net zo goed als een ander."),
        ]),
        dict(kop="Bruikbaar is niet hetzelfde als betrouwbaar", blokken=[
            ("p", "Twee aparte vragen, en je moet ze allebei stellen."),
            ("p", "<strong>Bruikbaar</strong>: geeft deze bron antwoord op de vraag die ík onderzoek? Een "
                  "perfect kloppende lijst van Egyptische graanvoorraden helpt je niets als je vraag over "
                  "Griekse tempels gaat."),
            ("p", "<strong>Betrouwbaar</strong>: klopt wat erin staat? Daarvoor kijk je naar de maker, zijn "
                  "belang, zijn afstand tot het voorval, en of andere bronnen hetzelfde zeggen."),
            ("kader", "Een onbetrouwbare bron is nooit waardeloos. Ze zegt misschien weinig over wat er "
                      "gebeurde, maar veel over <strong>wie ze maakte</strong> en wat die wilde dat de mensen "
                      "zouden geloven. Overdrijving is zelf een gegeven."),
            ("p", "Neem de slag bij <strong>Kadesj</strong>, 1274 v.C. Farao Ramses liet op tempelmuren "
                  "uithouwen dat hij glansrijk won. De Hettieten claimden diezelfde overwinning. Vermoedelijk "
                  "werd het onbeslist — kort daarna sloten ze het oudste vredesverdrag dat wij kennen."),
            ("p", "Eén bron geloven zou je dus meteen op het verkeerde been zetten. Bronnen <em>tegenover "
                  "elkaar</em> leggen en afwegen: dat is het werk."),
        ]),
        dict(kop="Standplaatsgebondenheid", blokken=[
            ("p", "Niemand kijkt van nergens. Wie iets vertelt, doet dat vanuit zijn eigen tijd, zijn eigen "
                  "plaats en zijn eigen positie in de samenleving. Dat heet "
                  "<strong>standplaatsgebondenheid</strong>."),
            ("p", "De Griekse schrijver <strong>Herodotos</strong> noemt de Perzen <em>barbaren</em>. Voor hem "
                  "betekende dat gewoon: mensen die geen Grieks spreken. Het woord klonk naar Griekse oren als "
                  "onverstaanbaar gebrabbel."),
            ("p", "Wij lezen <em>barbaar</em> als onbeschaafd en wreed. Wie die tekst leest zonder dat te "
                  "beseffen, denkt dat Herodotos de Perzen uitscheldt — en vormt zich een verkeerd beeld."),
            ("kader", "Het gaat dus twee kanten op: de <strong>maker</strong> van de bron is "
                      "standplaatsgebonden, en <strong>jij als lezer</strong> ook. Je kan dat niet "
                      "uitschakelen, maar je kan het wel weten. Dat is al de halve oplossing."),
        ]),
        dict(kop="Vijf manieren van redeneren", blokken=[
            ("p", "Om van bronnen naar een antwoord te komen, gebruik je "
                  "<strong>historische redeneerwijzen</strong>. Er zijn er vijf."),
            ("p", "<strong>Oorzaak en gevolg</strong> benoemen: wat leidde waartoe. "
                  "<strong>Meerdere perspectieven</strong> hanteren: dezelfde gebeurtenis bekijken vanuit de "
                  "slaaf, de soldaat én de keizer. <strong>Continuïteit en verandering</strong> benoemen: wat "
                  "bleef hetzelfde, wat veranderde."),
            ("p", "<strong>Bewijs gebruiken</strong>: je antwoord steunen op wat er in de bronnen staat, niet "
                  "op wat je voelt. En <strong>verbanden leggen</strong>: zien hoe stukken met elkaar "
                  "samenhangen."),
            ("kader", "Wat <em>hetzelfde blijft</em> is even veelzeggend als wat verandert, maar het valt veel "
                      "minder op. Daarom staat continuïteit uitdrukkelijk in het rijtje."),
        ]),
        dict(kop="Mythevorming", blokken=[
            ("p", "Rond een persoon, een plaats of een gebeurtenis groeit vaak een verhaal dat mooier of "
                  "eenvoudiger is dan de werkelijkheid. Dat heet <strong>mythevorming</strong>, en ze vervormt "
                  "het beeld dat mensen van het verleden hebben."),
            ("p", "Meestal gebeurt dat niet uit kwaad opzet. Een goed verhaal wordt gewoon vaker doorverteld "
                  "dan een saai of ingewikkeld verhaal."),
            ("p", "Het bekendste voorbeeld is de <strong>neanderthaler</strong>: in films en strips een "
                  "brute, domme, lompe holbewoner. De vondsten zeggen iets anders. Neanderthalers maakten "
                  "samengestelde werktuigen, beheersten vuur, verzorgden zieken en gewonden, en begroeven hun "
                  "doden. Wij dragen zelfs nog een stukje van hun erfelijk materiaal."),
            ("kader", "Vraag bij mythevorming altijd twee dingen: <strong>wat is de bedoeling</strong> van het "
                      "verhaal, en <strong>welk effect</strong> heeft het op hoe mensen naar dat verleden "
                      "kijken?"),
        ]),
        dict(kop="Kunst lezen", blokken=[
            ("p", "Ook een kunstwerk is een bron. Een schilderij, een beeld, een gebouw, een film, een game "
                  "of graffiti vertelt hoe mensen naar zichzelf en naar de wereld keken."),
            ("p", "Je leest het in drie stappen. Eerst <strong>verzamel je info</strong>: wanneer, waar, door "
                  "wie, in welke context, welke soort. Dan <strong>beschrijf je wat je ziet</strong>: "
                  "materialen, figuren, kleuren, licht en schaduw, hoe alles geschikt is."),
            ("p", "Pas daarna <strong>interpreteer</strong> je: wat is het onderwerp, voor wie is het gemaakt, "
                  "en met welke bedoeling — iets bevestigen, of juist bekritiseren?"),
            ("p", "Een kunstwerk geeft betekenis door <strong>vorm en inhoud samen</strong>. Een keizer te "
                  "paard, groter afgebeeld dan alle anderen, met het licht op zijn gezicht: hier zegt de vorm "
                  "evenveel als het onderwerp."),
            ("kader", "Een game over de Romeinen vertelt je weinig over Rome, maar veel over <strong>onze "
                      "tijd</strong>: over wat wij spannend vinden aan dat verleden. Ook dat is een bron — "
                      "over ons."),
        ]),
    ],
    onthoud=[
        "Verleden = wat gebeurd is. Geschiedenis = het verhaal dat historici eruit opbouwen.",
        "Een bron is alles uit het verleden waaruit je iets kan afleiden.",
        "Primair = uit de tijd zelf, secundair = later gemaakt uit andere bronnen. Het gaat over tijd, niet over kwaliteit.",
        "Vormen: geschreven, mondeling, materieel, audiovisueel.",
        "Vraag bij elke bron: wie maakte ze, voor wie, waarom — en pas dan wat staat erin.",
        "Bruikbaar = geeft antwoord op jouw vraag. Betrouwbaar = het klopt. Twee aparte vragen.",
        "Een onbetrouwbare bron toont wat de maker wilde laten geloven. Kadesj: beide partijen claimden de zege.",
        "Standplaatsgebondenheid geldt voor de maker én voor jou. Herodotos' 'barbaren' betekende: niet-Grieks.",
        "Vijf redeneerwijzen: oorzaak-gevolg, meerdere perspectieven, continuïteit en verandering, bewijs, verbanden.",
        "Mythevorming vervormt het beeld — zoals de neanderthaler, die in werkelijkheid werktuigen maakte en zijn doden begroef.",
        "Kunst lees je in drie stappen, en ze betekent iets door vorm en inhoud samen.",
    ])
