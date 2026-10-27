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
T = bundel.tabel

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
            ("p", "Onze <strong>tijdrekening</strong> of jaartelling telt de jaren vanaf de geboorte van "
                  "Christus, zoals die later werd berekend. Wat daarvoor ligt, krijgt de toevoeging "
                  "<strong>v.C.</strong> (voor Christus), wat daarna komt <strong>n.C.</strong> (na Christus). "
                  "Een jaar 0 bestaat niet: na het jaar 1 v.C. komt meteen het jaar 1 n.C."),
            ("fig", svg.jaartellijn(),
             "Vóór Christus tel je achterwaarts. 800 v.C. ligt dus vroeger dan 300 v.C., ook al is 800 het grotere getal."),
            ("weetje", "Het is niet de enige tijdrekening. De islamitische telt vanaf de tocht van Mohammed "
                       "naar Medina in 622 n.C., de joodse vanaf de schepping van de wereld zoals de joodse "
                       "traditie die berekent. Hetzelfde jaar heeft dus verschillende nummers."),
            ("p", "Dit zijn de <strong>structuurbegrippen rond tijd</strong>. Je moet ze allemaal kunnen "
                  "gebruiken."),
            ("p", T(["begrip", "wat het betekent", "voorbeeld"], [
                ("millennium", "een periode van 1000 jaar", "het 3de millennium n.C. begon in 2001"),
                ("eeuw", "een periode van 100 jaar", "de 5de eeuw loopt van 401 tot en met 500"),
                ("jaar", "de kleinste maat op een tijdlijn van de geschiedenis", "476 n.C."),
                ("tijdrekening", "de manier waarop een samenleving de jaren telt, vanaf een vast beginpunt", "voor en na Christus"),
                ("chronologie", "de volgorde van vroeger naar later", "eerst Egypte, dan Griekenland, dan Rome"),
                ("periode", "een stuk tijd met eigen kenmerken, afgebakend door historici", "de klassieke oudheid"),
                ("duur", "hoe lang iets aanhoudt", "de Peloponnesische oorlog duurde 27 jaar"),
                ("continuïteit", "wat gelijk blijft over de tijd heen", "het Latijn leefde verder na 476"),
                ("verandering", "wat anders wordt", "van rondtrekken naar op één plek wonen"),
                ("evolutie", "een verandering die traag en stap voor stap gaat", "het beeldschrift dat spijkerschrift wordt"),
                ("revolutie", "een verandering die snel en grondig gaat", "de Franse Revolutie van 1789"),
            ])),
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
            ("p", "De volgorde ken je best vanbuiten. De jaartallen zijn afspraken: ze geven ruwweg aan "
                  "waar een periode begint en eindigt."),
            ("p", T(["periode", "ruwweg", "begint met"], [
                ("1. de prehistorie", "tot ± 3300 v.C.", "de eerste mensachtigen"),
                ("2. het oude nabije oosten", "± 3300 v.C. tot ± 800 v.C.", "het schrift in Mesopotamië en Egypte"),
                ("3. de klassieke oudheid", "± 800 v.C. tot 476 n.C.", "de macht verschuift naar de Middellandse Zee"),
                ("4. de middeleeuwen", "476 tot ± 1500", "het einde van het West-Romeinse Rijk"),
                ("5. de vroegmoderne tijd", "± 1500 tot 1789", "de ontdekkingsreizen, de boekdrukkunst"),
                ("6. de moderne tijd", "1789 tot 1945", "de Franse Revolutie"),
                ("7. de hedendaagse tijd", "1945 tot vandaag", "het einde van de Tweede Wereldoorlog"),
            ])),
            ("kader", "<strong>Let op met oudere boeken.</strong> Vroeger gebruikte men andere namen. Wat "
                      "toen de <em>oudheid</em> heette, is nu gesplitst in het oude nabije oosten en de "
                      "klassieke oudheid. De <em>nieuwe tijd</em> heet nu de vroegmoderne tijd, de "
                      "<em>nieuwste tijd</em> heet nu de moderne tijd, en de <em>eigen tijd</em> heet nu de "
                      "hedendaagse tijd. Op het examen gebruik je de nieuwe namen."),
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
            ("p", "Naast wanneer, vraagt een historicus ook waar. Daarvoor bestaan vaste begrippen, de "
                  "<strong>structuurbegrippen rond ruimte</strong>."),
            ("p", T(["begrip", "wat het betekent", "voorbeeld"], [
                ("lokaal", "op één plaats", "één dorp aan de Nijl"),
                ("regionaal", "in een streek", "de Vruchtbare Halve Maan"),
                ("stedelijk", "in of van de stad", "het leven in Athene of Rome"),
                ("ruraal", "op het platteland", "de boeren rond een stad"),
                ("continentaal", "op of over een heel werelddeel, of gericht op het land", "Sparta, dat van zijn land leefde"),
                ("maritiem", "gericht op de zee", "Athene, dat van zijn vloot en zijn handel leefde"),
            ])),
            ("kader", "Woorden als <strong>chronologie</strong>, continuïteit, ruraal, maritiem en evolutie "
                      "heten <strong>structuurbegrippen</strong>: vaste begrippen waarmee historici elke "
                      "samenleving kunnen beschrijven, welke periode het ook is. Vraagt een examen naar \"het "
                      "structuurbegrip\", dan bedoelt het zo'n woord."),
            ("p", "Athene was maritiem: het leefde van zijn vloot en zijn handel overzee. Sparta lag in het "
                  "binnenland van de Peloponnesos en was continentaal: het leefde van zijn land, en zijn "
                  "macht zat in zijn leger te voet, niet in schepen."),
            ("p", "Op het examen kan je ook een kaart krijgen van het rijk van Alexander de Grote, naast een "
                  "kaart van vandaag. Dan zoek je welke landen van nu in dat rijk lagen. Dat waren onder meer "
                  "Griekenland, Turkije, Egypte, Syrië, Libanon, Israël, Irak, Iran en Afghanistan, en een "
                  "deel van Pakistan."),
        ]),
        dict(kop="De vier maatschappelijke domeinen", blokken=[
            ("p", "Een samenleving heeft veel kanten tegelijk. Om er orde in te brengen, verdelen historici "
                  "alles in vier <strong>maatschappelijke domeinen</strong>."),
            ("fig", svg.domeinen(),
             "Eén gebeurtenis hoort vaak in meerdere domeinen tegelijk. Dat is geen fout, dat is juist het punt."),
            ("p", "Een voorbeeld. Alexander de Grote verovert een wereldrijk: dat is <strong>politiek</strong>. "
                  "Maar door die verovering verspreidt de Griekse taal en kunst zich over dat hele gebied, en "
                  "dat is <strong>cultureel</strong>. De handel die op gang komt, is <strong>economisch</strong>."),
            ("p", "Nog een voorbeeld, nu van één voorwerp. Het bronzen beeld van de Romeinse "
                  "<strong>senator</strong> Aulus Metellus is een kunstwerk, dus <strong>cultureel</strong>. "
                  "Maar het toont hem in functie, met opgeheven hand alsof hij het woord neemt, en dus ook "
                  "zijn macht: <strong>politiek</strong>. Twee domeinen in één beeld."),
            ("weetje", "Historici zoeken graag naar <em>verbanden</em> tussen de domeinen. Waarom leidt een "
                       "betere oogst (economisch) tot grotere steden (sociaal) en tot machtigere koningen "
                       "(politiek)? Dat soort vragen maakt geschiedenis interessanter dan een rij jaartallen."),
            ("p", "Een voorbeeld van het <strong>sociale</strong> domein uit de klassieke oudheid: in Athene "
                  "mochten enkel vrije mannen met burgerrecht meebeslissen. Vrouwen, slaven en vreemdelingen "
                  "niet. Wie welke rechten heeft, is altijd sociaal."),
        ]),
        dict(kop="Kenmerken van een samenleving, per domein", blokken=[
            ("p", "Met deze begrippen beschrijf je elke samenleving uit de prehistorie, het oude nabije "
                  "oosten en de klassieke oudheid. Je komt ze in de volgende bundels allemaal tegen. Hier "
                  "staan ze bij elkaar, per domein."),
            ("p", "<strong>Politieke kenmerken</strong>: over macht en bestuur."),
            ("p", T(["begrip", "wat het betekent", "voorbeeld"], [
                ("stadstaat", "een stad met het land eromheen, met een eigen bestuur", "Ur, Athene, Sparta"),
                ("rijk", "een groot gebied met veel volkeren onder één heerser", "Egypte, het Romeinse Rijk"),
                ("republiek", "een staat zonder koning, met verkozen bestuurders", "Rome na 509 v.C."),
                ("autocratie", "één persoon heeft alle macht", "de farao, de Romeinse keizer"),
                ("aristocratie", "de adel, de rijke families, heeft de macht", "Athene vóór de democratie"),
                ("democratie", "het volk beslist, of de burgers", "Athene in de 5de eeuw v.C."),
                ("imperialisme", "een staat breidt zijn macht uit over andere volkeren en gebieden", "Rome dat de Middellandse Zee verovert"),
                ("kolonisatie", "groepen trekken weg en stichten elders een nieuwe stad", "de Griekse steden in Zuid-Italië"),
                ("ambtenaren", "mensen die in dienst van de heerser besturen", "de schrijvers van de farao"),
            ])),
            ("p", "<strong>Sociale kenmerken</strong>: over bevolkingsgroepen en hun rechten."),
            ("p", T(["begrip", "wat het betekent", "voorbeeld"], [
                ("nomadische samenleving", "mensen trekken rond, zonder vaste woonplaats", "de jagers en verzamelaars"),
                ("sedentaire samenleving", "mensen wonen op een vaste plaats", "de eerste boerendorpen"),
                ("standenmaatschappij", "vaste bevolkingslagen; je plaats ligt vast bij je geboorte", "Egypte: farao bovenaan, slaven onderaan"),
                ("patriarchale samenleving", "de man is het hoofd van het gezin en heeft het voor het zeggen", "de pater familias in Rome"),
                ("migratie", "mensen trekken naar een ander gebied om er te wonen", "de Homo sapiens die Afrika verlaat"),
                ("ongelijkheid", "groepen hebben niet dezelfde rechten of hetzelfde bezit", "patriciërs en plebejers"),
                ("vrijheid en onvrijheid", "of je zelf over je leven mag beslissen of niet", "de vrije burger en de heloot"),
                ("slavernij", "mensen zijn het bezit van iemand anders", "slaven in de mijnen en op de latifundia"),
                ("oorlog en vrede", "strijd tussen groepen, en de afspraken om die te stoppen", "de Pax Romana"),
                ("burgerrechten", "de rechten van wie burger is, zoals stemmen", "stemrecht in Athene"),
            ])),
            ("p", "<strong>Culturele kenmerken</strong>: over geloof, kennis en kunst."),
            ("p", T(["begrip", "wat het betekent", "voorbeeld"], [
                ("mythologie", "de verhalen over goden en helden", "Theseus en de Minotaurus"),
                ("wetenschappen", "kennis die je opbouwt door te onderzoeken en te bewijzen", "sterrenkunde in Mesopotamië"),
                ("filosofie", "nadenken over grote vragen, met redeneringen in plaats van goden", "Socrates, Plato, Aristoteles"),
                ("natuurreligie", "goden staan voor krachten van de natuur", "de zonnegod Re, de Nijlgod Sobek"),
                ("polytheïsme", "het geloof in veel goden", "Egypte, Griekenland, Rome"),
                ("monotheïsme", "het geloof in één god", "het jodendom, het christendom"),
                ("staatsgodsdienst", "de godsdienst die de staat als officieel geloof oplegt", "het christendom in Rome vanaf 380"),
                ("kunstuiting", "alles wat mensen maken om iets uit te drukken: beeld, gebouw, schildering, verhaal", "een grotschildering"),
                ("schriftsoorten", "de verschillende manieren van schrijven", "spijkerschrift, hiërogliefen, het alfabet"),
                ("cultuur", "alles wat een groep mensen samen doet, gelooft en maakt", "de Griekse cultuur"),
                ("multiculturele samenleving", "een samenleving waarin veel culturen samenleven", "het hellenistische rijk, het Romeinse Rijk"),
            ])),
            ("p", "<strong>Economische kenmerken</strong>: over hoe mensen aan voedsel en goederen komen."),
            ("p", T(["begrip", "wat het betekent", "voorbeeld"], [
                ("jager-verzamelaar", "leeft van jagen en van wat de natuur geeft", "de mensen in de oude steentijd"),
                ("agrarische (r)evolutie", "de overgang naar zelf telen en dieren houden", "± 10 000 jaar geleden"),
                ("landbouw", "gewassen telen en vee houden", "graan langs de Nijl"),
                ("ambacht", "met de hand iets maken als beroep", "pottenbakker, smid"),
                ("handel", "goederen kopen, verkopen of ruilen", "Griekse olijfolie tegen graan"),
                ("ruileconomie", "goederen ruilen zonder munten", "Mesopotamië, Egypte"),
                ("geldeconomie", "betalen met munten", "de Griekse en Romeinse munten"),
            ])),
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
            ("fig", svg.stappen(["mensachtigen|in Afrika", "Homo erectus|trekt weg", "Homo sapiens|over de wereld"]),
             "De Homo erectus, de rechtopgaande mens, was de eerste die Afrika verliet. De Homo sapiens, de verstandige mens, volgde later."),
            ("p", "Er waren verschillende <strong>soorten mensachtigen</strong>. Ze leefden niet netjes na "
                  "elkaar: sommige soorten leefden een tijd naast elkaar. De jaartallen zijn schattingen."),
            ("p", T(["soort", "wanneer", "kenmerk"], [
                ("Australopithecus", "± 4 tot 2 miljoen jaar geleden", "liep al rechtop, met een klein hersenvolume; de bekendste is Lucy"),
                ("Homo habilis, de handige mens", "± 2,4 tot 1,4 miljoen jaar geleden", "maakte de eerste eenvoudige stenen werktuigen"),
                ("Homo erectus, de rechtopgaande mens", "± 1,9 miljoen tot 100 000 jaar geleden", "maakte vuistbijlen, leerde vuur gebruiken en verliet als eerste Afrika"),
                ("neanderthaler", "± 400 000 tot 40 000 jaar geleden", "leefde in Europa en het Midden-Oosten, aangepast aan de kou, begroef zijn doden"),
                ("Homo sapiens, de verstandige mens", "± 300 000 jaar geleden tot nu", "dat zijn wij; trok over de hele wereld"),
            ])),
            ("p", "Die tochten uit Afrika noem je <strong>migraties</strong>. Eerst trok de Homo erectus naar "
                  "Azië en Europa, veel later de Homo sapiens, die uiteindelijk elk werelddeel bereikte."),
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
            ("p", "Ze waren <strong>nomadisch</strong>: rondtrekkers, <strong>nomaden</strong>. Als het "
                  "voedsel in een streek opraakte of de kudden verder trokken, trokken zij mee. Bezit had "
                  "weinig zin, want alles moest mee op de rug."),
            ("p", "Binnen zo'n groep was er een <strong>taakverdeling</strong>: niet iedereen deed hetzelfde. "
                  "De een ging op jacht, de ander verzamelde, maakte werktuigen of hield het vuur brandend. "
                  "Wie wat deed, kunnen we uit de bronnen niet met zekerheid afleiden."),
            ("p", "<strong>De jacht</strong> gebeurde in groep. Samen dreven ze dieren in een hinderlaag of "
                  "naar een afgrond, met speren en later met pijl en boog. Ze volgden de trek van de kudden. "
                  "Van een dier gebruikten ze alles: vlees om te eten, huid voor kleren en tenten, botten en "
                  "gewei voor werktuigen."),
            ("p", "<strong>De voedselverzameling</strong> bracht vruchten, noten, wortels, bessen, eieren en "
                  "schelpdieren op. Je moest goed weten wat eetbaar was en in welk seizoen."),
            ("weetje", "Het verzamelde plantaardige voedsel leverde vaak méér op dan de jacht. Het beeld van "
                       "de prehistorische mens die alleen maar mammoeten at, klopt dus niet."),
            ("fig", svg.stenen_werktuigen(),
             "Vuursteen splijt in vlijmscherpe schilfers. Aan die afslagvlakjes herken je een bewerkte steen van een gewone."),
            ("p", "Het oudste werktuig is de <strong>vuistbijl</strong>. Die heeft geen steel: je houdt hem "
                  "vast in je vuist, en daar komt de naam vandaan. Je kon ermee snijden, hakken en schrapen. "
                  "Een steel aan een bijl of een punt aan een speer binden, kwam pas veel later."),
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
            ("p", "Naast schilderingen maakten ze ook kleine beeldjes, zoals de <strong>Venus van "
                  "Willendorf</strong>, een vrouwenfiguurtje van ongeveer 30 000 jaar oud. En ze droegen "
                  "sieraden van schelpen, tanden en botjes. Ook dat zijn <strong>kunstuitingen</strong>."),
        ]),
        dict(kop="De agrarische revolutie", blokken=[
            ("p", "Ongeveer <strong>tienduizend jaar geleden</strong> gebeurde er iets wat alles veranderde: "
                  "mensen begonnen zelf gewassen te telen en dieren te houden. Dat heet de "
                  "<strong>agrarische revolutie</strong>."),
            ("p", "<strong>Waarom toen?</strong> Na de laatste ijstijd, zo'n 12 000 jaar geleden, werd het "
                  "warmer. In sommige streken groeiden wilde granen in overvloed, en groepen bleven er langer "
                  "op één plek. Hun aantal groeide, en jagen en verzamelen alleen werd te weinig. Zelf zaaien "
                  "was een oplossing."),
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
                  "afgeslagen. Boeren bakten ook <strong>aardewerk</strong>: potten om de oogst in te "
                  "bewaren."),
            ("p", "De landbouw <strong>verspreidde</strong> zich vanuit het Midden-Oosten heel traag over "
                  "Europa. In onze streken kwamen de eerste boeren pas rond 5300 v.C., zo'n vijfduizend jaar "
                  "nadat het allemaal begonnen was."),
        ]),
        dict(kop="Prehistorische sporen bij ons", blokken=[
            ("p", "De prehistorie is niet ver weg. Ook in onze streken liggen nog sporen, en veel ervan kan "
                  "je gaan bekijken."),
            ("p", T(["spoor", "wat het is", "waar"], [
                ("hunebed of dolmen", "grote stenen boven een graf, uit het neolithicum", "Wéris in de Ardennen, Drenthe in Nederland"),
                ("menhir", "één grote rechtopstaande steen", "Wéris"),
                ("grafheuvel", "een heuvel die over een graf werd opgeworpen", "in de Kempen en in Limburg"),
                ("vuursteenmijn", "schachten waar boeren vuursteen voor hun bijlen uithaalden", "Spiennes bij Bergen, werelderfgoed"),
                ("vuistbijl en pijlpunt", "werktuigen die bij het ploegen of graven bovenkomen", "in musea, zoals het Gallo-Romeins Museum in Tongeren"),
            ])),
            ("p", "En ook in ons leven zit nog prehistorie: we telen dezelfde granen, houden dezelfde dieren "
                  "en wonen, net als de eerste boeren, op een vaste plek."),
        ]),
    ],
    onthoud=[
        "Prehistorie = de tijd zonder geschreven bronnen, veruit de langste periode.",
        "Mensachtigen: Australopithecus, Homo habilis, Homo erectus, neanderthaler, Homo sapiens.",
        "De mens ontstond in Afrika; de Homo erectus trok als eerste weg.",
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
            ("p", "Aan het hoofd van een stadstaat stond een <strong>koning</strong>, die zei dat hij regeerde "
                  "in naam van de stadsgod. Hij liet kanalen graven, leidde het leger en sprak recht. De "
                  "priesters en de ambtenaren hielpen hem. Koning <strong>Hammurabi</strong> van Babylon liet "
                  "rond 1750 v.C. zijn wetten in een stenen zuil kappen, zodat iedereen ze kon zien."),
            ("p", "Egypte gaat een andere weg. Daar smelten de gebieden langs de Nijl samen tot één rijk "
                  "onder één heerser: de <strong>farao</strong>. Eén rivier, één land. Dat is een "
                  "<strong>autocratie</strong>: één persoon heeft alle macht."),
            ("p", T(["wie", "wat hij doet"], [
                ("de farao", "heeft het laatste woord over alles; leidt het leger, spreekt recht, laat tempels bouwen, brengt offers aan de goden en houdt de orde in het land"),
                ("de vizier", "de hoogste ambtenaar, de rechterhand van de farao; bestuurt het land in zijn naam"),
                ("de gouwvorsten", "besturen elk een deel van het land, een gouw"),
                ("de schrijvers", "meten de akkers op na de overstroming, berekenen en innen de belasting, houden de voorraden bij"),
                ("de priesters", "dienen de goden in de tempels en beheren de tempelgronden"),
            ])),
            ("p", "De <strong>plicht</strong> van de farao was de orde bewaren: zorgen dat de Nijl overstroomde, "
                  "dat de oogst lukte en dat de goden tevreden bleven. Lukte dat niet, dan twijfelden de "
                  "mensen aan hem."),
            ("kader", "Een <strong>ambtenaar</strong> is iemand die in dienst van de heerser bestuurt: hij "
                      "meet akkers op, int belastingen, houdt de voorraad bij. Zonder ambtenaren is een staat "
                      "van deze omvang onmogelijk."),
        ]),
        dict(kop="Het schrift", blokken=[
            ("p", "Wie graan van honderden boeren moet bijhouden, kan dat niet onthouden. Daarom wordt het "
                  "schrift uitgevonden: niet om verhalen te bewaren, maar om <strong>te tellen en te "
                  "boekhouden</strong>. De oudste kleitabletten zijn voorraadlijsten."),
            ("p", "Het begon als <strong>beeldschrift</strong>: men tekende het ding zelf, een kop graan of "
                  "een runderkop. Omdat dat te traag ging, werden die tekeningen steeds schematischer, tot er "
                  "tekens overbleven waarin je het voorwerp niet meer herkent."),
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
                      "bracht de doorbraak: daarop staat dezelfde tekst in <strong>drie schriften</strong> — "
                      "hiërogliefen, demotisch en Grieks. Omdat men Grieks wél kon lezen, kreeg men greep op "
                      "de rest. Champollion ontcijferde ze in 1822."),
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
                  "elk met een eigen taak — de zon, de rivier, de oogst, de oorlog. Veel van die goden staan "
                  "voor een kracht uit de natuur. Dat heet een <strong>natuurgodsdienst</strong>."),
            ("fig", svg.ziggurat(),
             "De ziggurat is een trapvormige tempeltoren. Hij stond midden in de stad en was van ver te zien."),
            ("p", "De tempel is niet enkel een gebedshuis. Hij bezit grond, slaat graan op en betaalt "
                  "werkers uit. Dat noemt men een <strong>tempeleconomie</strong>: godsdienst en economie "
                  "lopen door elkaar."),
            ("p", "Dit zijn de Egyptische goden die je moet kennen. Je herkent ze op tekeningen aan hun kop."),
            ("p", T(["god", "waarvan", "herken je aan"], [
                ("Amon/Re", "Re is de zonnegod; Amon de oppergod van Thebe; samen werden ze één: Amon-Re", "Re: een valkenkop met de zonneschijf; Amon: een kroon met twee hoge veren"),
                ("Osiris", "god van de doden en het hiernamaals, en van de vruchtbaarheid", "een mummie met een kroon, groene of zwarte huid"),
                ("Isis", "vrouw van Osiris, moeder van Horus, godin van de moeders en de magie", "een troon op haar hoofd"),
                ("Horus", "zoon van Osiris en Isis, beschermer van de farao", "een valkenkop"),
                ("Seth", "god van de woestijn, de storm en de chaos; broer van Osiris", "een vreemd dier met lange snuit en rechte oren"),
                ("Anoebis", "god van het balsemen en de begraafplaatsen", "een jakhalskop"),
                ("Toth", "god van het schrift en de wijsheid", "een ibiskop"),
                ("Sobek", "god van het water van de Nijl", "een krokodillenkop"),
            ])),
            ("p", "Ook de Egyptenaren hadden hun <strong>mythologie</strong>. De bekendste mythe: Seth doodt "
                  "zijn broer Osiris uit jaloezie. Isis zoekt de stukken van zijn lichaam bij elkaar en brengt "
                  "hem terug tot leven, en Osiris wordt koning van de doden. Hun zoon Horus verslaat Seth en "
                  "wordt koning op aarde. Daarom gold elke farao als de levende Horus."),
            ("p", "In Egypte is de farao zelf goddelijk: hij geldt als een god op aarde en als de schakel "
                  "tussen de goden en de mensen. Hij bestuurt, spreekt recht, leidt het leger en de "
                  "eredienst."),
            ("fig", svg.piramides(),
             "Een piramide is een graf. De Egyptenaren geloofden in een leven na de dood, en daar hoorde een lichaam bij."),
            ("p", "Zij geloofden dat het leven verderging in het <strong>hiernamaals</strong>, en dat de "
                  "dode daarvoor zijn lichaam nodig had. Daarom <strong>mummificeerden</strong> ze hun doden: "
                  "het lichaam moest bewaard blijven. In het graf legden ze voorwerpen, eten en het "
                  "<strong>Dodenboek</strong>, een verzameling spreuken die de dode op die tocht moest helpen."),
            ("p", "Het <strong>mummificeren</strong> duurde zeventig dagen. De organen werden eruit gehaald en "
                  "apart bewaard, het lichaam werd met zout gedroogd, ingesmeerd en in linnen windsels "
                  "gewikkeld. Dat vroeg veel kennis van het lichaam: godsdienst en wetenschap gingen hier samen."),
            ("weetje", "In het hiernamaals wachtte de <strong>hartweging</strong>. Anoebis legde het hart van de "
                       "dode op een weegschaal, met aan de andere kant een veer. Toth schreef de uitslag op. Was "
                       "het hart zwaar van slechte daden, dan werd het opgegeten door een monster. Was het licht, "
                       "dan mocht de dode naar het rijk van Osiris."),
            ("kader", "<strong>Toetanchamon</strong> was een onbelangrijke farao die jong stierf. Zijn graf "
                      "is wereldberoemd om één reden: het is als enige vrijwel ongeschonden teruggevonden. "
                      "Alle andere waren al in de oudheid leeggeroofd. De Britse archeoloog "
                      "<strong>Howard Carter</strong> vond het in 1922 in de Vallei der Koningen. Er lagen meer "
                      "dan vijfduizend voorwerpen in, en het beroemde gouden dodenmasker."),
        ]),
        dict(kop="Egyptische kunst", blokken=[
            ("p", "De Egyptische kunst diende vooral de goden, de farao en het leven na de dood. Ze bleef "
                  "drieduizend jaar bijna hetzelfde: vaste regels, weinig vernieuwing."),
            ("p", T(["kunst", "kenmerken", "voorbeeld"], [
                ("bouwkunst", "enorm en in steen, om eeuwig te blijven staan", "de piramides van Gizeh, de tempels van Karnak en Luxor"),
                ("beeldhouwkunst", "stijf, recht vooruit kijkend, de armen tegen het lichaam; de farao kalm en tijdloos", "de Grote Sfinx, beelden van farao's"),
                ("schilderkunst", "hoofd en benen van opzij, oog en schouders van voren; wie belangrijker is, wordt groter getekend", "schilderingen in de graven"),
            ])),
            ("p", "De farao droeg vaste <strong>machtssymbolen</strong>: de dubbele kroon van Boven- en "
                  "Neder-Egypte, de kromstaf en de dorsvlegel in zijn handen, een valse baard en een cobra op "
                  "zijn voorhoofd. Zo zag iedereen meteen wie de macht had."),
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
                  "de <strong>sterrenkunde</strong> of astronomie. Priesters volgden de sterren en de maan om "
                  "te weten wanneer ze moesten zaaien en wanneer de feesten voor de goden vielen."),
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
        "Egyptische goden: Amon/Re, Osiris, Isis, Horus, Seth, Anoebis, Toth, Sobek. Een natuurgodsdienst.",
        "De farao is een autocraat; de vizier en de schrijvers besturen voor hem.",
        "Handel ging per ruil, afgerekend in gewogen graan of zilver — munten bestonden nog niet.",
        "Van daar komen het wiel, de ploeg, geschreven wetten, de sterrenkunde, ons uur van 60 minuten en de 12 maanden.",
    ])

BUNDELS["het-oude-griekenland"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het oude Griekenland",
    onder="Honderden kleine stadstaten, twee heel verschillende voorbeelden, en denkers die het nog altijd doen.",
    secties=[
        dict(kop="Vóór de stadstaten: Kreta en Mycene", blokken=[
            ("p", "De klassieke oudheid begint rond 800 v.C., maar in de Griekse wereld bloeiden al eerder "
                  "twee beschavingen. In de tijd liggen ze vóór de klassieke oudheid, maar ze horen bij het verhaal "
                  "van Griekenland, en je moet ze allebei kennen."),
            ("p", "De <strong>Minoïsche beschaving</strong> bloeide op het eiland <strong>Kreta</strong>, "
                  "ongeveer van 2000 tot 1450 v.C. Ze is genoemd naar de sagenkoning Minos. In het midden van "
                  "elke streek stond een groot paleis, het bekendste in <strong>Knossos</strong>."),
            ("p", "Dat paleis was het hart van de <strong>paleiseconomie</strong>: de boeren brachten hun oogst "
                  "naar het paleis, waar ze in grote voorraadkruiken bewaard werd, en het paleis verdeelde die "
                  "weer. Schrijvers hielden alles bij op kleitabletten. Met zijn schepen dreef Kreta "
                  "<strong>handel</strong> over de hele oostelijke Middellandse Zee, tot in Egypte."),
            ("p", "Hun <strong>kunst</strong> is vrolijk en levendig: muurschilderingen of fresco's met "
                  "dolfijnen, bloemen en jongeren die over een stier springen. De stier speelde een grote rol "
                  "in hun godsdienst."),
            ("kader", "Daar komt de <strong>mythe van Theseus en de Minotaurus</strong> vandaan. Koning Minos "
                      "hield in een doolhof, het labyrint, een monster dat half mens en half stier was. Athene "
                      "moest elk jaar jongeren sturen om aan hem gevoerd te worden. De Atheense prins Theseus "
                      "doodde de Minotaurus en vond de weg terug met een draad die prinses Ariadne hem gaf. "
                      "Een mythe, maar met een kern: het paleis van Knossos was zo groot en ingewikkeld dat het "
                      "op een doolhof leek."),
            ("p", "De <strong>ondergang</strong>: rond 1600 v.C. barstte de vulkaan op het eiland Thera, het "
                  "huidige Santorini, uit. Dat bracht Kreta wellicht veel schade toe. Rond 1450 v.C. werden de "
                  "paleizen verwoest en namen de Myceners het eiland over."),
            ("p", "De <strong>Myceense beschaving</strong> bloeide op het Griekse vasteland, ongeveer van 1600 "
                  "tot 1100 v.C., met <strong>Mycene</strong> op de Peloponnesos als bekendste stad. De "
                  "Myceners waren krijgers. Hun koningen woonden in burchten met muren van reusachtige "
                  "stenen; de bekendste ingang is de Leeuwenpoort van Mycene."),
            ("p", "Ook zij hadden een <strong>paleiseconomie</strong>, en ze dreven <strong>handel</strong> over "
                  "zee. Hun schrift, het Lineair B, is de oudste vorm van het Grieks. Als <strong>kunst</strong> "
                  "lieten ze vooral goud na: in hun graven lagen wapens, bekers en gouden maskers, zoals het "
                  "zogenaamde masker van Agamemnon."),
            ("p", "Volgens de sagen voerden de Myceners de <strong>Trojaanse oorlog</strong>: koning Agamemnon "
                  "trok met een Grieks leger naar Troje, in het huidige Turkije, om de geschaakte Helena terug "
                  "te halen. Na tien jaar viel de stad door een list met een houten paard. Homeros vertelt "
                  "het in de <em>Ilias</em>. Troje bestond echt en is opgegraven, maar of de oorlog zo "
                  "verliep, weten we niet."),
            ("p", "De <strong>ondergang</strong> kwam rond 1200 tot 1100 v.C.: de burchten werden verwoest en "
                  "het schrift raakte in onbruik. De oorzaak is onzeker, misschien invallen van buitenaf, "
                  "droogte of opstanden. Daarna volgden enkele eeuwen waar we weinig over weten, tot rond "
                  "800 v.C. de eerste stadstaten opkwamen."),
        ]),
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
            ("p", "Natuur en klimaat bepaalden ook de <strong>economie</strong>. Het is er heet en droog in de "
                  "zomer en zacht in de winter, en de grond is rotsig. Graan groeit er maar matig, olijven en "
                  "druiven wel. In de bergen hielden ze geiten en schapen."),
            ("p", T(["sector", "wat ze deden"], [
                ("landbouw", "olijven (voor olie), druiven (voor wijn), wat graan; geiten en schapen"),
                ("ambachten", "pottenbakkers maakten de beroemde beschilderde vazen; smeden, wevers, scheepsbouwers"),
                ("handel", "over zee: olijfolie, wijn en vazen gingen weg, graan, hout en metaal kwamen binnen; vanaf de 6de eeuw v.C. betaalden ze met munten"),
            ])),
            ("p", "Er was te weinig vruchtbare grond voor een groeiende bevolking. Daarom trokken groepen weg "
                  "om elders een nieuwe stad te stichten: de <strong>Griekse kolonisatie</strong>, vooral "
                  "tussen 750 en 550 v.C. Andere <strong>oorzaken</strong> waren de handel, ruzie in de eigen "
                  "stad en avontuur. Zo kwamen er Griekse steden tot in Zuid-Italië, Zuid-Frankrijk en rond de "
                  "Zwarte Zee."),
            ("p", T(["gevolg", "wat er veranderde"], [
                ("politiek", "elke kolonie werd een nieuwe, zelfstandige polis, maar bleef verbonden met haar moederstad"),
                ("economisch", "meer handel: graan uit de Zwarte Zee in ruil voor olie, wijn en vazen"),
                ("sociaal", "minder monden te voeden in de moederstad, en dus minder onrust"),
                ("cultureel", "de Griekse taal, het alfabet, de goden en de kunst verspreidden zich, ook naar de Etrusken en de Romeinen"),
            ])),
        ]),
        dict(kop="Sparta en Athene: twee wegen", blokken=[
            ("p", "<strong>Sparta</strong> was een <strong>oligarchie</strong>: een kleine groep besliste. "
                  "Alles stond er in dienst van het leger. Jongens verlieten op hun zevende het gezin voor een "
                  "harde militaire opvoeding. Die opvoeding heette de <strong>agoge</strong> en duurde jaren."),
            ("p", "Dat kon omdat de <strong>heloten</strong>, onvrije landbouwers, al het werk op het land "
                  "deden. Zij waren veruit in de meerderheid, en de angst voor een opstand hield Sparta mee in "
                  "dat keurslijf."),
            ("p", "<strong>Athene</strong> ging een andere weg. Eerst bestuurden de rijke adellijke families "
                  "de stad: een <strong>aristocratie</strong>, en omdat het om een kleine groep ging ook een "
                  "oligarchie. Daarna kwam een periode van <strong>tirannen</strong>, en rond 508 v.C. voerde "
                  "Kleisthenes de <strong>democratie</strong> in. Onder Perikles, in de 5de eeuw v.C., bereikte "
                  "die haar bloei."),
            ("p", "Zo werkte die democratie:"),
            ("p", T(["onderdeel", "hoe het werkte"], [
                ("de volksvergadering", "alle burgers mochten komen, spreken en stemmen over wetten, oorlog en vrede"),
                ("de Raad van 500", "burgers die door loting gekozen werden, bereidden de voorstellen voor"),
                ("de rechtbanken", "honderden burgers, ook door loting, spraken samen recht"),
                ("het schervengericht", "de burgers konden een te machtige politicus tien jaar verbannen door zijn naam op een potscherf te krassen"),
            ])),
            ("p", "Dat heet een <em>directe</em> democratie: de burgers beslisten zelf, niet via verkozen "
                  "vertegenwoordigers zoals bij ons."),
            ("kader", "Een <strong>tiran</strong> was bij de Grieken een alleenheerser die de macht gegrepen "
                      "had. Het woord betekende nog niet vanzelf 'wreed'; sommige tirannen waren juist geliefd "
                      "bij het gewone volk."),
            ("p", "De beperking is even belangrijk als de uitvinding. Enkel <strong>vrije mannen met "
                  "burgerrecht</strong> mochten stemmen. Vrouwen, slaven en vreemdelingen niet, ook al woonden "
                  "die er hun leven lang. Van de hele bevolking stemde ongeveer één op tien."),
            ("p", "Zo zag de bevolking eruit, met haar <strong>rechten en plichten</strong>:"),
            ("p", T(["", "Sparta", "Athene"], [
                ("bovenaan", "Spartiaten: burgers, met politieke rechten; hun plicht was hun hele leven soldaat zijn", "burgers: vrije mannen met Atheense ouders; stemrecht, maar ook belasting en legerdienst"),
                ("vrij, maar zonder politieke rechten", "perioiken: handelaars en ambachtslieden rond Sparta; vochten mee in het leger", "metoiken: vreemdelingen, vaak handelaars; betaalden belasting en vochten mee, maar mochten niet stemmen"),
                ("onvrij", "heloten: onvrije boeren die het land bewerkten voor de Spartiaten", "slaven: bezit van hun eigenaar, in het huishouden, de werkplaats of de mijnen"),
            ])),
            ("p", "Ook voor vrouwen verschilden de twee. Een Spartaanse vrouw mocht sporten, bezit hebben en "
                  "zich vrij bewegen; een Atheense vrouw leefde grotendeels binnenshuis. Meebeslissen deed ze "
                  "op geen van beide plaatsen."),
        ]),
        dict(kop="Twee oorlogen die alles veranderden", blokken=[
            ("p", "In de <strong>Perzische oorlogen</strong>, van 490 tot 479 v.C., stonden de Griekse "
                  "stadstaten tegenover het enorme Perzische Rijk. De <strong>oorzaak</strong>: de Griekse "
                  "steden aan de kust van Klein-Azië, het huidige Turkije, kwamen in opstand tegen de Perzen, "
                  "en Athene stuurde schepen om hen te helpen. De Perzische koning wilde wraak."),
            ("p", "De Atheners wonnen bij <strong>Marathon</strong> in 490 v.C. Tien jaar later kwamen de "
                  "Perzen terug. De Spartanen hielden hen een tijd tegen bij Thermopylae, en de Atheense vloot "
                  "versloeg hen bij Salamis in 480 v.C. Uitzonderlijk genoeg werkten de stadstaten samen, en "
                  "ze wonnen."),
            ("p", "Gevolg: Athene werd de leider van een bondgenootschap van stadstaten, en gebruikte het geld "
                  "daarvan onder meer om het <strong>Parthenon</strong> te bouwen, de tempel op de "
                  "<strong>Akropolis</strong>, de burchtheuvel van de stad. Hij was gewijd aan "
                  "<strong>Athena</strong>, de beschermgodin naar wie Athene genoemd is. De andere leden begonnen "
                  "dat als overheersing te voelen."),
            ("p", "Dat liep uit op de <strong>Peloponnesische oorlog</strong>, van 431 tot 404 v.C.: Athene en "
                  "zijn bondgenoten tegen Sparta en de zijne. De <strong>oorzaak</strong> was de angst van "
                  "Sparta voor de groeiende macht van Athene. Sparta won, maar alle Griekse stadstaten kwamen "
                  "er verzwakt uit, en Athene verloor zijn vloot en zijn macht."),
            ("fig", svg.stappen(["Perzische|oorlogen", "Athene|machtig", "wrevel bij|de rest",
                                 "Peloponnesische|oorlog", "allen|verzwakt"]),
             "De ketting die Griekenland rijp maakte voor de Macedonische overname."),
        ]),
        dict(kop="Goden, orakels en spelen", blokken=[
            ("p", "De Grieken waren <strong>polytheïstisch</strong>. Hun goden woonden volgens de verhalen op "
                  "de berg <strong>Olympus</strong>, met <strong>Zeus</strong> als oppergod. Het waren geen "
                  "verheven wezens: ze werden jaloers, verliefd en kwaad, precies zoals mensen."),
            ("p", "Dit zijn de belangrijkste <strong>Olympische goden</strong>. De Romeinen namen ze later "
                  "over, met een eigen naam."),
            ("p", T(["Griekse naam", "god of godin van", "Romeinse naam"], [
                ("Zeus", "de hemel en de bliksem, oppergod", "Jupiter"),
                ("Hera", "het huwelijk, vrouw van Zeus", "Juno"),
                ("Poseidon", "de zee", "Neptunus"),
                ("Athena", "de wijsheid en de krijgskunst, beschermster van Athene", "Minerva"),
                ("Apollo", "het licht, de muziek en de dichtkunst", "Apollo"),
                ("Artemis", "de jacht", "Diana"),
                ("Aphrodite", "de liefde en de schoonheid", "Venus"),
                ("Ares", "de oorlog", "Mars"),
                ("Hermes", "de handel en de reizigers, boodschapper van de goden", "Mercurius"),
                ("Hephaistos", "het vuur en de smeden", "Vulcanus"),
                ("Demeter", "de landbouw en het graan", "Ceres"),
                ("Dionysos", "de wijn en het feest", "Bacchus"),
            ])),
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
                  "wending: ziekte werd een zaak van het lichaam, niet van een vloek. De arts "
                  "<strong>Hippocrates</strong> keek naar wat een zieke voelde en at, in plaats van naar de "
                  "goden; artsen zweren vandaag nog de eed van Hippocrates. En <strong>Pythagoras</strong> "
                  "zocht naar de regels van getallen en driehoeken."),
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
                  "het noorden. Koning Filips II versloeg de Griekse steden in 338 v.C. Vanaf dan stond "
                  "<strong>Hellas onder Macedonisch gezag</strong>. De zoon van Filips was "
                  "<strong>Alexander de Grote</strong>."),
            ("p", "In ongeveer tien jaar veroverde hij het hele Perzische Rijk, tot in Egypte en tot aan de "
                  "rand van India. Hij stierf in 323 v.C. op zijn tweeëndertigste, en zijn generaals verdeelden "
                  "het rijk onder elkaar. Zo viel het <strong>wereldrijk versnipperd</strong> uiteen in "
                  "kleinere rijken, zoals dat van de Ptolemaeën in Egypte. Die rijken vielen later één voor één "
                  "in Romeinse handen."),
            ("p", "Wat bleef, is het <strong>hellenisme</strong>: de vermenging van Griekse cultuur met die van "
                  "het oosten. Grieks werd de taal waarin men in dat hele gebied handel dreef en studeerde, "
                  "eeuwenlang, ook nog toen de Romeinen er de baas waren. In <strong>Alexandrië</strong>, de "
                  "stad die Alexander in Egypte stichtte, stond de grootste bibliotheek van de oudheid. Het "
                  "hellenistische rijk was een <strong>multiculturele samenleving</strong>: Grieken, "
                  "Egyptenaren, Perzen en vele anderen leefden er samen."),
        ]),
    ],
    onthoud=[
        "Vóór de polis: de Minoïsche beschaving op Kreta (Knossos, Minotaurus) en de Myceense op het vasteland (Trojaanse oorlog).",
        "Bergen en zee verdeelden Griekenland in honderden zelfstandige stadstaten: de polis.",
        "Te weinig grond leidde tot kolonisatie rond de Middellandse Zee en de Zwarte Zee.",
        "Sparta: oligarchie, leger, heloten. Athene: van oligarchie over tirannie naar directe democratie.",
        "In Athene stemden enkel vrije mannelijke burgers — ongeveer één op tien van de bevolking. Metoiken en slaven niet.",
        "Sparta: Spartiaten, perioiken, heloten. Athene: burgers, metoiken, slaven.",
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
                  "de stad naar zichzelf. Volgens de Romeinen gebeurde dat in 753 v.C."),
            ("kader", "Zo'n stichtingsmythe is geen geschiedenis. Ze vertelt vooral hoe de Romeinen zichzelf "
                      "wilden zien: hard, door de goden gewild, en bereid alles voor de stad opzij te zetten."),
            ("p", "Het vroege Rome leerde veel van zijn buren: van de <strong>Etrusken</strong> de boog en "
                  "bestuursgewoonten, van de <strong>Grieken</strong> het alfabet, de goden en de kunst."),
        ]),
        dict(kop="De koningstijd", blokken=[
            ("p", "Eerst hadden <strong>koningen</strong> de macht, van 753 tot 509 v.C. De macht was toen "
                  "verdeeld over drie instellingen."),
            ("p", T(["instelling", "bevoegdheden"], [
                ("de koning", "opperbevelhebber van het leger, hoogste rechter en hoogste priester"),
                ("de senaat", "een raad van de hoofden van de oude families; gaf de koning advies"),
                ("de volksvergadering", "de burgers; bekrachtigden de keuze van een nieuwe koning en beslisten mee over oorlog"),
            ])),
        ]),
        dict(kop="De republiek", blokken=[
            ("p", "In 509 v.C. joegen de Romeinen hun laatste koning, Tarquinius de Hoogmoedige, weg. Ze "
                  "wilden nooit meer één alleenheerser. Zo ontstond de <strong>republiek</strong>, van "
                  "<em>res publica</em>: de zaak van iedereen."),
            ("p", "Aan het hoofd stonden twee <strong>consuls</strong>, elk voor één jaar verkozen. Twee, "
                  "zodat ze elkaar konden tegenhouden; één jaar, zodat niemand lang alleen de macht hield. "
                  "Alleen in uiterste nood benoemde men tijdelijk één <strong>dictator</strong>."),
            ("p", "De <strong>senaat</strong>, de raad van oud-bestuurders, gaf officieel enkel advies, maar "
                  "besliste in de praktijk over bijna alles. De <strong>volksvergadering</strong> koos de "
                  "bestuurders en stemde over de wetten — al stemden de rijkste groepen eerst en wogen die "
                  "het zwaarst."),
            ("p", "De bestuurders heten <strong>magistraten</strong>. Ze werden elk jaar verkozen, altijd met "
                  "meer dan één tegelijk, en kregen geen loon. Wie carrière maakte, klom van ambt naar ambt."),
            ("p", T(["magistraat", "bevoegdheden"], [
                ("consul (2)", "de hoogste bestuurders; leiden het leger en roepen de senaat samen"),
                ("praetor", "spreekt recht"),
                ("quaestor", "beheert de staatskas"),
                ("aedilis", "zorgt voor de markten, de straten en de spelen"),
                ("censor", "houdt de volkstelling bij en waakt over de goede zeden"),
                ("volkstribuun", "beschermt de plebejers en kan met zijn veto een besluit tegenhouden"),
                ("dictator", "enkel in uiterste nood, voor hoogstens zes maanden, met alle macht"),
            ])),
            ("p", "Binnen de stad stonden twee groepen tegenover elkaar: de <strong>patriciërs</strong>, de "
                  "oude rijke families, en de <strong>plebejers</strong>, het gewone volk. De plebejers "
                  "dwongen hun rechten stap voor stap af, onder meer door massaal het werk neer te leggen en "
                  "de stad te verlaten. Zo kregen ze hun eigen volkstribunen en geschreven wetten, de wet "
                  "van de Twaalf Tafelen."),
        ]),
        dict(kop="Van stad tot wereldrijk", blokken=[
            ("p", "Eerst veroverde Rome, stad na stad, het hele <strong>Italische schiereiland</strong>; rond "
                  "270 v.C. was dat rond. Daarna botste het op <strong>Carthago</strong>, de grote handelsmacht "
                  "in Noord-Afrika. Dat werden de <strong>Punische oorlogen</strong>, van 264 tot 146 v.C."),
            ("p", "De <strong>oorzaak</strong> was de strijd om Sicilië en om de handel op de Middellandse Zee. "
                  "In de tweede oorlog trok de Carthaagse generaal <strong>Hannibal</strong> met olifanten over "
                  "de Alpen en versloeg hij de Romeinen in Italië zelf, maar Rome hield stand. Het "
                  "<strong>gevolg</strong>: in 146 v.C. werd Carthago volledig verwoest, Rome had geen "
                  "tegenstander meer in het westen, en er stroomden rijkdom en slaven binnen. De Middellandse "
                  "Zee werd <strong>mare nostrum</strong>: onze zee."),
            ("fig", svg.stappen(["stadstaat", "Italië", "Punische|oorlogen", "mare|nostrum", "imperium|Romanum"]),
             "Elke verovering maakte de volgende mogelijk — en maakte tegelijk de republiek onbestuurbaar."),
            ("p", "Na de Middellandse Zee ging het verder, tot het <strong>imperium Romanum</strong>, het "
                  "Romeinse wereldrijk. Caesar veroverde Gallië, waar ook onze streken bij hoorden. Onder "
                  "keizer Trajanus, rond 117 n.C., was het rijk het grootst: van Brittannië tot Mesopotamië. "
                  "Dat noem je <strong>imperialisme</strong>: een staat die zijn macht uitbreidt over andere "
                  "volkeren."),
            ("p", "Het <strong>leger</strong> speelde daarin de hoofdrol. De legioenen veroverden nieuwe "
                  "gebieden, bewaakten de grens, de <strong>limes</strong>, en legden wegen, bruggen en "
                  "forten aan. Gediende soldaten kregen land en gingen in de veroverde gebieden wonen. Zo "
                  "verspreidden de Romeinse taal en gewoontes zich mee."),
            ("p", "Het succes ondermijnde het bestuur. Oorlogen leverden zoveel slaven op dat grootgrondbezit "
                  "met slavenarbeid, het <strong>latifundium</strong>, spotgoedkoop werd. De kleine boer kon "
                  "daar niet tegenop, verkocht zijn grond en trok verarmd naar de stad."),
        ]),
        dict(kop="Van republiek naar keizerrijk", blokken=[
            ("p", "In de stad groeide zo een grote groep arme burgers. Politici hielden die tevreden met "
                  "gratis graan en spelen. Tegelijk kregen soldaten hun stuk land niet van de staat maar van "
                  "hun <strong>generaal</strong> — en dus volgden ze hem, desnoods tegen Rome in."),
            ("p", "De generaal <strong>Marius</strong> nam als eerste arme burgers op in een beroepsleger. Die "
                  "soldaten waren trouwer aan hun generaal dan aan de senaat. Zijn rivaal <strong>Sulla</strong> "
                  "trok in 82 v.C. met zijn leger Rome binnen en liet zich dictator maken."),
            ("p", "Wie de top wilde bereiken, zocht bondgenoten. Drie machtige mannen die samen de macht "
                  "verdeelden, noemt men een <strong>triumviraat</strong>. Het eerste bestond uit Caesar, "
                  "Pompeius en Crassus; het tweede, na de moord op Caesar, uit Augustus, Marcus Antonius en "
                  "Lepidus. Allebei eindigden ze in een oorlog tussen de partners."),
            ("p", "Dat leidde tot een eeuw van <strong>burgeroorlogen</strong>: Marius tegen Sulla, daarna "
                  "Caesar tegen Pompeius. <strong>Julius Caesar</strong> won en liet zich dictator voor het "
                  "leven benoemen. Zijn tegenstanders zagen daarin een nieuwe koning en vermoordden hem in 44 "
                  "v.C. in de senaat."),
            ("p", "Na nog een burgeroorlog bleef zijn aangenomen zoon over: <strong>Augustus</strong>, de "
                  "eerste <strong>keizer</strong>. Hij noemde zich geen koning maar <em>princeps</em>, de "
                  "eerste burger, en liet de senaat en de ambten gewoon bestaan. Dat was in 27 v.C., en daar "
                  "begint het <strong>keizerrijk</strong>."),
            ("kader", "Dat was geen bescheidenheid maar berekening. De vormen van de republiek bleven staan, "
                      "terwijl de macht in één paar handen zat. Zo kreeg Rome het alleenbewind dat het vier "
                      "eeuwen eerder had afgezworen, zonder het zo te moeten noemen."),
            ("p", "Zo werd het <strong>keizerrijk bestuurd</strong>:"),
            ("p", T(["wie", "bevoegdheden"], [
                ("de keizer", "opperbevelhebber van het leger, hoogste priester, kiest de gouverneurs, maakt de wetten; zijn wil is wet"),
                ("de senaat", "bleef bestaan, maar had weinig te zeggen; gaf vooral eer en advies"),
                ("de magistraten", "bleven bestaan als ere-ambten; de keizer besliste wie ze kreeg"),
                ("de gouverneurs", "bestuurden elk een provincie, innen de belasting en leiden de troepen daar"),
            ])),
        ]),
        dict(kop="Pax Romana", blokken=[
            ("p", "Onder de eerste keizers volgde een periode van ongeveer twee eeuwen rust binnen het rijk: "
                  "de <strong>Pax Romana</strong>, de Romeinse vrede. Aan de grenzen werd wel nog gevochten."),
            ("p", "Die rust was ook economie. Eén munt, één rechtssysteem, geen rovers en geen piraten: "
                  "goederen konden van Britannië tot Egypte reizen. Daarvoor bouwden de Romeinen wegen die "
                  "eeuwen meegingen."),
            ("p", "Want de economie van Rome draaide voor een groot deel op <strong>uitbuiting</strong>. De "
                  "veroverde provincies, de wingewesten, moesten belasting betalen en graan, metaal en slaven "
                  "leveren. Slaven werkten in de mijnen, op de latifundia en in de huizen: het was een "
                  "<strong>slaveneconomie</strong>."),
            ("p", "In de steden werkten <strong>ambachtslieden</strong> in kleine werkplaatsen: bakkers, "
                  "pottenbakkers, smeden, glasblazers. En er was een <strong>geldeconomie</strong>: men "
                  "betaalde met munten, zoals de zilveren denarius, die overal in het rijk gold. Dat maakte "
                  "handel over lange afstand veel makkelijker dan ruilen."),
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
            ("p", "Het <strong>theater</strong> namen ze ook van de Grieken over, maar de Romeinen bouwden hun "
                  "theaters vrijstaand, in steen, in plaats van tegen een helling. Ze hielden vooral van "
                  "komedies."),
            ("p", "Nog geliefder waren de <strong>wagenrennen</strong> in het Circus Maximus, waar "
                  "honderdduizenden toeschouwers juichten voor hun ploeg, en de "
                  "<strong>gladiatorenspelen</strong> in het amfitheater. De keizers betaalden die spelen "
                  "zelf, om het volk tevreden te houden: brood en spelen."),
            ("p", "De Romeinen waren <strong>polytheïstisch</strong>. Ze brachten de goden "
                  "<strong>offers</strong>: een dier, wijn, koekjes. In ruil verwachtten ze hulp. Voor een "
                  "belangrijke beslissing keken priesters naar <strong>voortekens</strong>: hoe vogels vlogen, "
                  "of hoe de ingewanden van een offerdier eruitzagen. Dat gebruik kwam van de Etrusken. Thuis "
                  "had elk gezin een huisaltaartje voor zijn eigen beschermgoden."),
            ("p", "Ze namen de Griekse goden over en gaven ze eigen namen: Zeus werd "
                  "<strong>Jupiter</strong>, Ares werd Mars, Aphrodite werd Venus. Het hele rijtje staat in de "
                  "bundel over Griekenland. Daarbovenop kwam de <strong>keizerscultus</strong>: de keizer "
                  "zelf werd vereerd. In een rijk vol volkeren en goden was dat het bindmiddel."),
            ("p", "Precies daarom botsten de <strong>christenen</strong>: zij geloofden in één god, dat is "
                  "<strong>monotheïsme</strong>, en weigerden de keizer te vereren. Ze werden vervolgd, maar "
                  "het christendom groeide toch. Keizer Constantijn liet het in 313 toe, en keizer Theodosius "
                  "maakte het in 380 de <strong>staatsgodsdienst</strong>."),
            ("p", "Rome nam van overal iets over: van de Etrusken de boog en de voortekens, van de Grieken de "
                  "goden, de kunst en het theater, uit het oosten nieuwe godsdiensten. Het rijk was een "
                  "<strong>multiculturele samenleving</strong>."),
        ]),
        dict(kop="Wie had welke rechten?", blokken=[
            ("p", "Ook Rome was een <strong>standenmaatschappij</strong>, en ook een "
                  "<strong>patriarchale samenleving</strong>: de vader, de <em>pater familias</em>, had het "
                  "gezag over zijn vrouw, zijn kinderen en zijn slaven. Hij mocht zelfs beslissen of een "
                  "pasgeboren kind bleef leven."),
            ("p", T(["groep", "rechten en plichten"], [
                ("senatoren", "de rijkste families; zetelen in de senaat en worden magistraat"),
                ("ridders", "rijk geworden door handel en geldzaken; vaak ambtenaar of officier"),
                ("gewone burgers", "stemrecht, betalen belasting en dienen in het leger; veel arme burgers in de stad"),
                ("vrijgelatenen", "voormalige slaven; vrij, maar met minder rechten"),
                ("slaven", "geen rechten, bezit van hun meester; konden wel vrijgekocht of vrijgelaten worden"),
            ])),
            ("p", "<strong>Vrouwen</strong> hadden geen stemrecht en mochten geen ambt bekleden. Toch hadden ze "
                  "meer vrijheid dan in Athene: een Romeinse vrouw ging naar buiten, naar de spelen en de "
                  "baden, en een rijke vrouw beheerde het huishouden en soms eigen bezit."),
            ("p", "De <strong>slaven</strong> waren meestal krijgsgevangenen of kinderen van slaven. Hun lot "
                  "hing af van hun werk: in de mijnen was het zwaar en kort, in een rijk huis soms beter. In "
                  "73 v.C. leidde de gladiator <strong>Spartacus</strong> een grote slavenopstand, die bloedig "
                  "werd neergeslagen."),
            ("p", "Het burgerrecht werd stilaan uitgebreid. In 212 n.C. kregen alle vrije inwoners van het "
                  "rijk het Romeinse burgerrecht."),
        ]),
        dict(kop="Farao en keizer vergeleken", blokken=[
            ("p", "Op het examen kan je twee samenlevingen moeten vergelijken. Een voorbeeld: de "
                  "<strong>machtssymbolen</strong> van de Egyptische farao en die van de Romeinse keizer."),
            ("p", T(["", "de farao", "de Romeinse keizer"], [
                ("hoofd", "de dubbele kroon van Boven- en Neder-Egypte, een cobra op het voorhoofd", "een lauwerkrans"),
                ("kleren en voorwerpen", "kromstaf en dorsvlegel, een valse baard", "een purperen toga of de wapenrusting van een veldheer"),
                ("beelden", "reusachtig en stijf, eeuwig jong en kalm", "standbeelden in elke stad, op de munten zijn portret"),
                ("goddelijk?", "geldt als een god op aarde", "wordt vereerd in de keizerscultus, en na zijn dood soms tot god verklaard"),
            ])),
            ("p", "De gelijkenis: allebei lieten ze overal zien dat ze de macht hadden. Het verschil: de "
                  "farao was meteen een god, de keizer noemde zich eerst de eerste burger."),
            ("p", "Een tweede voorbeeld is de <strong>bouwkunst</strong>. De Grieken bouwden met zuilen en "
                  "balken, en hun tempels stonden vrij op een verhoog. De Romeinen namen de zuilen over, maar "
                  "voegden de boog, het gewelf, de koepel en het beton toe, en bouwden ook voor het gewone "
                  "leven: baden, aquaducten, amfitheaters."),
        ]),
        dict(kop="Romeinse sporen bij ons", blokken=[
            ("p", "Onze streken hoorden bijna vijfhonderd jaar bij het Romeinse Rijk. Dat zie je nog."),
            ("p", T(["spoor", "voorbeeld"], [
                ("steden", "Tongeren, de oudste stad van België, met resten van de Romeinse stadsmuur"),
                ("wegen", "de heirbaan van Boulogne via Bavay en Tongeren naar Keulen"),
                ("woorden", "muur (murus), straat (strata), venster (fenestra), kelder (cellarium), wijn (vinum)"),
                ("de kalender", "twaalf maanden; juli en augustus zijn genoemd naar Julius Caesar en Augustus"),
                ("het recht", "veel van ons recht gaat terug op het Romeinse recht"),
            ])),
        ]),
        dict(kop="Het einde van het westen", blokken=[
            ("p", "In de <strong>3de eeuw</strong> liep het mis: invallen aan de grenzen, munten die steeds "
                  "minder zilver bevatten, en keizers die elkaar in hoog tempo afzetten."),
            ("p", "Het rijk bleek te groot om vanuit één punt te besturen en werd in 395 gesplitst in een "
                  "<strong>West-</strong> en een <strong>Oost-Romeins Rijk</strong>. In het westen vielen "
                  "Germaanse volkeren binnen. Het westen viel in <strong>476</strong>, toen de Germaanse "
                  "legeraanvoerder Odoaker de laatste keizer afzette; het oosten leefde als het Byzantijnse Rijk nog duizend jaar voort, "
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
        "Rome ontstond aan de Tiber; de sage van Romulus en Remus (753 v.C.) is mythe, geen geschiedenis.",
        "Koningstijd → republiek → keizerrijk. De republiek had twee consuls per jaar, een senaat en een volksvergadering.",
        "Patriciërs tegen plebejers: het gewone volk dwong zijn rechten stap voor stap af.",
        "Punische oorlogen tegen Carthago maakten Rome baas over het westen: mare nostrum.",
        "Latifundia met slaven verdreven de kleine boer naar de stad; legers werden trouw aan hun generaal.",
        "Caesar werd vermoord als dictator; Augustus werd de eerste keizer en noemde zich princeps.",
        "Pax Romana: twee eeuwen rust, en daardoor handel over het hele rijk, over wegen en via aquaducten.",
        "De Romeinen voegden boog, gewelf, koepel en beton toe aan de Griekse bouwkunst.",
        "Portretbeelden tonen de mens zoals hij was; keizerscultus als bindmiddel, christendom van vervolgd tot staatsgodsdienst.",
        "Magistraten: consuls, praetoren, quaestoren, aedielen, censoren, volkstribunen; in nood een dictator.",
        "Patriarchaal: de pater familias besliste. Senatoren, ridders, burgers, vrijgelatenen, slaven.",
        "Polytheïsme met offers en voortekens; christendom (monotheïsme) toegelaten in 313, staatsgodsdienst in 380.",
        "Crisis van de 3de eeuw, splitsing in 395, val van het westen in 476 — het oosten hield nog duizend jaar stand.",
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
                  "nieuwe bronnen, nieuwe onderzoekstechnieken of nieuwe vragen opduiken. "
                  "<strong>Koolstofdatering</strong> en <strong>DNA-onderzoek</strong> hebben in enkele "
                  "decennia meer bijgesteld dan eeuwen discussie daarvoor."),
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
            ("p", "Wat was zijn naam, zijn beroep, zijn afkomst? Was die een <strong>ooggetuige</strong>, "
                  "iemand die het zelf zag? Of een <strong>tijdgenoot</strong>, die in dezelfde tijd leefde "
                  "maar het van horen zeggen had? Wie was de <strong>opdrachtgever</strong>, degene die "
                  "betaalde? Welke plaats had de maker in de samenleving, en vanuit welk "
                  "<strong>perspectief</strong> keek hij: als Griek of als Pers, als slaaf of als keizer?"),
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
            ("p", "Bij bruikbaarheid stel je drie vragen. Geeft de bron <strong>rechtstreekse</strong> "
                  "informatie, die er letterlijk in staat? Geeft ze <strong>onrechtstreekse</strong> informatie, "
                  "die je zelf moet afleiden? En geeft ze een <strong>volledig</strong>, een "
                  "<strong>gedeeltelijk</strong> of <strong>geen</strong> antwoord op je vraag?"),
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
        dict(kop="Het stappenplan van de bronnenanalyse", blokken=[
            ("p", "Op het examen krijg je een paar bronnen en een historische vraag, zoals \"Wie won de slag "
                  "bij Kadesj in 1274 v.C.?\" Je werkt dan in vier stappen."),
            ("p", T(["stap", "wat je doet"], [
                ("1. de context verzamelen", "je situeert elke bron in tijd, ruimte en domein; je bepaalt de soort bron (primair of secundair, geschreven, mondeling, materieel of audiovisueel); je zoekt wie de maker is; je bepaalt het doelpubliek, de inhoud en de bedoeling; en je noteert welke gegevens ontbreken"),
                ("2. de inhoud bestuderen", "je leest of bekijkt elke bron goed"),
                ("3. de bron interpreteren", "je legt uit hoe de tijd en de standplaats van de maker de inhoud kleuren; je beoordeelt de bruikbaarheid en de betrouwbaarheid; je vergelijkt de bronnen en zoekt gelijkenissen en verschillen"),
                ("4. een beargumenteerd antwoord geven", "je kiest wat je uit de bronnen gebruikt en staaft je antwoord met argumenten uit die bronnen"),
            ])),
        ]),
        dict(kop="Standplaatsgebondenheid", blokken=[
            ("p", "Niemand kijkt van nergens. Wie iets vertelt, doet dat vanuit zijn eigen tijd, zijn eigen "
                  "plaats en zijn eigen positie in de samenleving. Dat heet "
                  "<strong>standplaatsgebondenheid</strong>."),
            ("p", "De Griekse geschiedschrijver <strong>Herodotos</strong> schreef in zijn <em>Historiën</em> "
                  "over de slag bij Marathon in 490 v.C. Hij noemt de Perzen <em>barbaren</em>. Voor hem "
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
            ("p", "Een voorbeeld van zo'n historische vraag: <em>Was Julius Caesar een democraat?</em> Je krijgt "
                  "dan een stuk uit het boek <em>Over de levens van de keizers</em> van de Romeinse "
                  "geschiedschrijver <strong>Suetonius</strong>, en ander materiaal. Suetonius schreef meer "
                  "dan honderd jaar na Caesars dood, dus hij was geen ooggetuige. Je zoekt bewijs, bekijkt "
                  "het vanuit meerdere perspectieven (de senatoren die hem vermoordden, het volk dat hem "
                  "aanbad) en legt verbanden."),
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
            ("p", "Je leest het met een stappenplan in vier stappen."),
            ("p", T(["stap", "wat je doet"], [
                ("1. info verzamelen", "wanneer en waar werd het gemaakt, in welke maatschappelijke context, door wie, wat is de titel, en welke soort is het: schilderij, beeldhouwwerk, bouwwerk, film, game, graffiti, theater, ritueel of uitdrukking"),
                ("2. beschrijven wat je ziet of hoort", "materialen, figuren, vormen en rollen, de schikking, kleuren, licht en schaduw; bij muziek of film ook klanken, ritme, tempo, instrumenten en stemmen"),
                ("3. interpreteren", "het onderwerp (wat), het doelpubliek (voor wie) en de bedoeling (waarom); en hoe wat je ziet of hoort het onderwerp en de bedoeling ondersteunt"),
                ("4. je analyse toelichten", "je zet in je eigen woorden op een rij wat je zag en hoe je het uitlegt"),
            ])),
            ("p", "Het <strong>onderwerp</strong> kan bijvoorbeeld de dood zijn, het alledaagse leven, onrecht, "
                  "liefde of gender. Voor de <strong>bedoeling</strong> zijn er vaste woorden:"),
            ("p", T(["bedoeling", "voorbeeld"], [
                ("bekritiseren", "een spotprent op een keizer"),
                ("bevestigen", "een standbeeld van Augustus dat zijn macht toont"),
                ("decoreren", "een mozaïek op de vloer van een Romeinse villa"),
                ("entertainen", "een komedie in het theater"),
                ("informeren", "de zuil van Trajanus, die zijn oorlog toont"),
                ("praktisch gebruiken", "een beschilderde Griekse vaas om wijn in te bewaren"),
                ("schoonheid creëren", "een Grieks beeld van een ideaal lichaam"),
            ])),
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
        "Bronnenanalyse in vier stappen: context, inhoud, interpreteren, beargumenteerd antwoord.",
        "Kunst lees je in vier stappen: info, beschrijven, interpreteren, toelichten. Ze betekent iets door vorm en inhoud samen.",
    ])
