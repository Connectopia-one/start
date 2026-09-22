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
