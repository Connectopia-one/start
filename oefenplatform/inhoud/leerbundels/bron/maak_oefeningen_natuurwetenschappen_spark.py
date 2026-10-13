# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij natuurwetenschappen ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof, alleen met moeilijkere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere metingen om mee te rekenen, andere situaties om te verklaren,
en opdrachten die je enkel op papier kan maken (een schema tekenen, een tabel
aanvullen). Wie hier iets bijschrijft, legt het eerst naast
`../../spark/natuurwetenschappen.json`.

Er staan geen figuren met bijschrift in: een tekening uit svg.py draagt haar
namen mee en dat verklapt hier net het antwoord. Wat getekend moet worden,
tekent het kind zelf in een leeg kader.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

SPARK = "✨ Spark — 1ste en 2de middelbaar"

W = "110px"
WW = "185px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een rekenvraag: schrijf eerst de formule op, vul dan de getallen in, en zet de eenheid erbij.",
    "Bij een verklaring: zeg niet alleen wát er gebeurt, maar ook waaróm.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-cellen-weefsels-en-organen-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Cellen, weefsels en organen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De organisatieniveaus",
             opdracht="Van klein naar groot: cel, weefsel, orgaan, stelsel, organisme.",
             oefeningen=[
                 ("rij", [("een rode bloedcel", "cel"), ("de maag", "orgaan"),
                          ("spierweefsel", "weefsel"), ("het ademhalingsstelsel", "stelsel")],
                  "Welk organisatieniveau is dit?", WW),
                 ("open", "Leg uit wat het verschil is tussen een weefsel en een orgaan.",
                  "Een weefsel is een groep cellen van dezelfde soort met dezelfde taak. Een "
                  "orgaan bestaat uit verschillende weefsels die samen één taak uitvoeren.", 4),
                 ("waar", "Het hart is een weefsel.", False),
                 ("kort", "Hoe noem je een organisme dat uit één enkele cel bestaat?",
                  "eencellig", W),
             ]),

        dict(kop="Onderdelen van de cel",
             opdracht="Gebruik de namen uit de bundel.",
             oefeningen=[
                 ("rij", [("bevat de erfelijke informatie", "de celkern"),
                          ("hier gebeurt de celademhaling", "de mitochondriën"),
                          ("bepaalt wat er in en uit de cel gaat", "het celmembraan"),
                          ("vangt zonlicht op", "de bladgroenkorrels")],
                  "Welk celonderdeel is dit?", WW),
                 ("tabel", ["celonderdeel", "plant", "dier"],
                  [["celwand", None, None], ["mitochondriën", None, None],
                   ["grote vacuole", None, None], ["celkern", None, None]],
                  "celwand: enkel plant · mitochondriën: allebei · grote vacuole: enkel plant · "
                  "celkern: allebei"),
                 ("waar", "Een dierlijke cel heeft een celwand.", False),
                 ("waar", "Een plantencel kan zowel bladgroenkorrels als mitochondriën hebben.",
                  True),
             ]),

        dict(kop="Verklaren met de cel",
             opdracht="Antwoord in volle zinnen en noem het celonderdeel bij naam.",
             oefeningen=[
                 ("open", "Een spiercel heeft veel meer mitochondriën dan een huidcel. Verklaar.",
                  "Een spiercel moet samentrekken en heeft daar veel energie voor nodig. Die "
                  "energie komt uit de celademhaling, en die gebeurt in de mitochondriën.", 4),
                 ("open", "Waarom heeft een cel uit de wortel van een plant geen "
                          "bladgroenkorrels?",
                  "Bladgroenkorrels vangen licht op voor de fotosynthese. In de grond komt geen "
                  "licht, dus daar zouden ze nutteloos zijn.", 4),
                 ("open", "Een plant die te weinig water krijgt, gaat slap hangen. Welk "
                          "celonderdeel verklaart dat, en hoe?",
                  "De vacuole. Vol water duwt ze de cel van binnenuit stevig tegen de celwand. "
                  "Loopt ze leeg, dan verliest de cel die spanning en zakt de plant in.", 5),
                 ("open", "Een onderzoeker ziet onder de microscoop een cel met een celwand, een "
                          "grote vacuole en groene korrels. Wat is het, en hoe weet je dat?",
                  "Een plantencel. Die drie onderdelen samen komen enkel bij planten voor; een "
                  "dierlijke cel heeft er geen van drie.", 4),
                 ("open", "Waarom bekijk je een stukje ui onder een microscoop en niet met een "
                          "loep?",
                  "Een cel is veel te klein voor een loep. Een loep vergroot maar een paar keer, "
                  "een microscoop honderden keren.", 3),
             ]),

        dict(kop="Stelsels die samenwerken",
             opdracht="Noem de stelsels bij naam.",
             oefeningen=[
                 ("rij", [("zuurstof in je bloed brengen", "het ademhalingsstelsel"),
                          ("je lichaam rechtop houden", "het skeletstelsel"),
                          ("voedsel afbreken tot voedingsstoffen", "het spijsverteringsstelsel"),
                          ("stoffen rondvoeren", "het bloedvatenstelsel")],
                  "Welk stelsel doet dit?", WW),
                 ("open", "Welke stelsels werken samen om zuurstof en voedingsstoffen tot in je "
                          "tenen te krijgen? Leg de weg uit.",
                  "Het ademhalingsstelsel neemt zuurstof op, het spijsverteringsstelsel levert "
                  "de voedingsstoffen, en het bloedvatenstelsel brengt allebei met het bloed "
                  "tot bij elke cel.", 5),
                 ("kort", "Welke twee stelsels heeft een plant?",
                  "het wortelstelsel en het scheutstelsel", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-fotosynthese-en-de-plant-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Fotosynthese en de plant",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De reactie zelf",
             opdracht="Let goed op wat erin gaat en wat eruit komt.",
             oefeningen=[
                 ("rij", [("water en koolstofdioxide", "gaan erin"),
                          ("glucose en zuurstof", "komen eruit"),
                          ("licht", "gaat erin"), ("bladgroen", "is nodig, maar wordt niet verbruikt")],
                  "Gaat dit erin of komt het eruit bij de fotosynthese?", WW),
                 ("teken", "Teken een blad en zet met pijlen aan: het licht, het water dat uit "
                           "de wortel komt, de koolstofdioxide die binnengaat, en de zuurstof "
                           "die buitengaat.",
                  "Licht van boven op het blad, water met een pijl van onderaan uit de steel, "
                  "CO₂ met een pijl naar binnen aan de onderkant (huidmondjes), O₂ met een pijl "
                  "naar buiten op dezelfde plaats.", 55),
                 ("waar", "Planten geven bij de fotosynthese koolstofdioxide af.", False),
                 ("kort", "Welke energieomzetting gebeurt er bij de fotosynthese?",
                  "lichtenergie wordt chemische energie", WW),
             ]),

        dict(kop="De plant van wortel tot blad",
             opdracht="Vul het juiste woord in.",
             oefeningen=[
                 ("rij", [("neemt water en mineralen op", "de wortel"),
                          ("vervoert water naar boven", "de stengel"),
                          ("laat gassen in en uit", "de huidmondjes"),
                          ("slaat suiker op als reserve", "zetmeel")],
                  "Welk plantendeel of welke stof is dit?", WW),
                 ("open", "Waarom staan de huidmondjes vooral aan de onderkant van een blad?",
                  "Aan de onderkant schijnt de zon niet recht op het blad. Daar is het koeler, "
                  "dus verdampt er minder water als de huidmondjes opengaan.", 4),
                 ("open", "Waarom zit er zetmeel in een aardappel?",
                  "De plant maakt meer glucose dan ze meteen nodig heeft. Die suiker slaat ze op "
                  "als zetmeel, in de knol, als voorraad voor later.", 4),
                 ("kort", "Hoe noem je een organisme dat zijn eigen energierijke stoffen maakt?",
                  "autotroof", W),
             ]),

        dict(kop="Fotosynthese en celademhaling",
             opdracht="Dit zijn twee verschillende processen. Hou ze uit elkaar.",
             oefeningen=[
                 ("tabel", ["", "fotosynthese", "celademhaling"],
                  [["gebruikt zuurstof", None, None], ["maakt glucose", None, None],
                   ["heeft licht nodig", None, None], ["gebeurt ook 's nachts", None, None]],
                  "gebruikt zuurstof: enkel celademhaling · maakt glucose: enkel fotosynthese · "
                  "heeft licht nodig: enkel fotosynthese · gebeurt ook 's nachts: enkel "
                  "celademhaling"),
                 ("waar", "Een plant gebruikt zelf ook zuurstof.", True),
                 ("waar", "'s Nachts geeft een plant netto zuurstof af.", False),
                 ("open", "Waarom worden de bladeren van een plant in een donkere kast na een "
                          "tijd geel?",
                  "Zonder licht kan de plant geen fotosynthese doen. Het bladgroen wordt "
                  "afgebroken en niet vervangen, dus de groene kleur verdwijnt.", 4),
             ]),

        dict(kop="Waarom het ons aangaat",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een tuinder pompt extra koolstofdioxide in zijn serre. Waarom?",
                  "CO₂ is een grondstof voor de fotosynthese. Meer CO₂ betekent dat de planten "
                  "sneller suiker kunnen maken en dus sneller groeien.", 4),
                 ("open", "Leg uit waarom de energie in een biefstuk oorspronkelijk van de zon "
                          "komt.",
                  "De koe at gras. Dat gras maakte zijn suikers met zonlicht via fotosynthese. "
                  "Die energie ging via het gras naar de koe en via het vlees naar jou.", 5),
                 ("open", "Waarom is ontbossing slecht nieuws voor de hoeveelheid CO₂ in de "
                          "lucht?",
                  "Bomen halen CO₂ uit de lucht bij de fotosynthese. Minder bomen betekent dat "
                  "er minder CO₂ wordt weggenomen, en bij het kappen of verbranden komt er nog "
                  "extra bij.", 4),
                 ("waar", "Een plant kan zonder mineralen uit de bodem perfect groeien.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-menselijk-lichaam-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Het menselijk lichaam",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De weg van het voedsel",
             opdracht="Zet in volgorde en gebruik de juiste namen.",
             oefeningen=[
                 ("rij", [("slokdarm", r"\(2\)"), ("dunne darm", r"\(4\)"), ("mond", r"\(1\)"),
                          ("maag", r"\(3\)"), ("dikke darm", r"\(5\)")],
                  r"Zet de weg van het voedsel in volgorde: schrijf \(1\) tot \(5\).", WW),
                 ("rij", [("splitst vetten in kleine druppeltjes", "gal"),
                          ("begint met de vertering van zetmeel", "speeksel"),
                          ("hier worden de voedingsstoffen opgenomen", "de dunne darm"),
                          ("hier wordt water uit de resten gehaald", "de dikke darm")],
                  "Wat of waar is dit?", WW),
                 ("rij", [("zetmeel", "glucose"), ("eiwit", "aminozuren"),
                          ("vet", "vetzuren en glycerol")],
                  "Waarin wordt dit gesplitst bij de vertering?", WW),
                 ("kort", "Hoe heet het opnemen van verteerde voedingsstoffen in het bloed?",
                  "resorptie", W),
                 ("waar", "De maag maakt gal om de vetten te verteren.", False),
             ]),

        dict(kop="Ademhaling en bloedsomloop",
             opdracht="Let op waar het bloed zuurstofrijk is en waar niet.",
             oefeningen=[
                 ("kort", "Waar komt de zuurstof precies in je bloed terecht?",
                  "in de longblaasjes", W),
                 ("kort", "Hoe heet de spier onder je longen die je helpt ademen?",
                  "het middenrif", W),
                 ("kort", "Uit hoeveel holtes bestaat het hart?", "vier", W),
                 ("open", "Wat is het verschil tussen een slagader en een ader?",
                  "Een slagader voert bloed wég van het hart en heeft een dikke, gespierde wand. "
                  "Een ader voert bloed naar het hart terug en heeft een dunnere wand met "
                  "kleppen.", 4),
                 ("waar", "In de longslagader stroomt zuurstofarm bloed.", True),
                 ("kort", "Hoe heet de grootste slagader, die uit de linkerkamer vertrekt?",
                  "de aorta", W),
                 ("rij", [("vervoeren zuurstof", "rode bloedcellen"),
                          ("laten een wonde stollen", "bloedplaatjes"),
                          ("ruimen ziektekiemen op", "witte bloedcellen")],
                  "Welk bestanddeel van het bloed doet dit?", WW),
             ]),

        dict(kop="Alles werkt samen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je loopt hard. Waarom ga je sneller ademen én klopt je hart sneller?",
                  "Je spieren verbruiken meer glucose en zuurstof en maken meer CO₂. Je ademt "
                  "sneller om meer zuurstof op te nemen en CO₂ kwijt te raken, en je hart pompt "
                  "sneller om dat allemaal rond te voeren.", 5),
                 ("open", "Waar gebeurt de celademhaling, en wat gebeurt er precies?",
                  "In de mitochondriën van elke cel. Glucose en zuurstof worden omgezet in "
                  "koolstofdioxide, water en energie. Niet in de longen, daar gebeurt enkel de "
                  "gasuitwisseling.", 5),
                 ("kort", "Wat is de kleine bloedsomloop?",
                  "de weg van het hart naar de longen en terug", WW),
             ]),

        dict(kop="Gezond eten en bewegen",
             opdracht="Denk aan de voedings- en de bewegingsdriehoek.",
             oefeningen=[
                 ("open", "Iemand eet elke dag frieten, drinkt frisdrank en zit de hele dag "
                          "stil. Noem drie aanpassingen die dat patroon gezonder maken.",
                  "Water drinken in plaats van frisdrank, meer groenten en fruit, minder "
                  "gefrituurd en bewerkt eten, en het lange stilzitten onderbreken met "
                  "bewegen.", 5),
                 ("open", "Waarom staat lang stilzitten in de rode bol van de "
                          "bewegingsdriehoek?",
                  "Omdat het het ongezondste is van alles wat in de driehoek staat. Niet enkel "
                  "'weinig sport', maar een aparte schade: je best ook onderbreken als je voor "
                  "de rest genoeg beweegt.", 4),
                 ("kort", "Welke voedingsstoffen zijn vooral bouwstoffen?",
                  "eiwitten (en mineralen)", WW),
                 ("waar", "Water is een voedingsstof.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-voortplanting-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Voortplanting",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Met of zonder geslachtscellen",
             opdracht="Aseksueel is één ouder, seksueel zijn er twee.",
             oefeningen=[
                 ("rij", [("stekken", "aseksueel"), ("bestuiving en bevruchting", "seksueel"),
                          ("een bol of knol onder de grond", "aseksueel"),
                          ("knopvorming bij gist", "aseksueel")],
                  "Aseksueel of seksueel?", WW),
                 ("kort", "Hoe noem je het afsnijden van een stukje plant dat je laat wortelen?",
                  "stekken", W),
                 ("waar", "Een plant die door stekken ontstaat, verschilt erfelijk van de "
                          "moederplant.", False),
                 ("open", "Noem één voordeel van seksuele en één voordeel van aseksuele "
                          "voortplanting.",
                  "Seksueel: de nakomelingen verschillen van elkaar, dus de soort past zich "
                  "beter aan bij verandering of ziekte. Aseksueel: het gaat snel en je hebt "
                  "geen partner nodig.", 5),
             ]),

        dict(kop="De bloem",
             opdracht="Gebruik de namen van de bloemdelen.",
             oefeningen=[
                 ("rij", [("het mannelijke deel", "de meeldraad"),
                          ("het vrouwelijke deel", "de stamper"),
                          ("vangt het stuifmeel op", "de stempel"),
                          ("hierin zitten de eicellen", "het vruchtbeginsel")],
                  "Welk bloemdeel is dit?", WW),
                 ("kort", "Hoe heet het overbrengen van stuifmeel op de stempel?",
                  "bestuiving", W),
                 ("open", "Waarom heeft gras geen opvallende, gekleurde bloemen?",
                  "Gras wordt door de wind bestoven, niet door insecten. Kleur, geur en nectar "
                  "zouden geen enkel nut hebben, dus de plant steekt daar geen energie in.", 4),
                 ("teken", "Teken een bloem in doorsnede en zet er vier namen bij: meeldraad, "
                           "stempel, stijl en vruchtbeginsel.",
                  "De meeldraden staan rondom, met de helmknop bovenaan. In het midden de "
                  "stamper: de stempel bovenaan, daaronder de stijl, en onderaan het "
                  "vruchtbeginsel met de eicellen.", 55),
             ]),

        dict(kop="Bij de mens",
             opdracht="Vul aan met het juiste woord.",
             oefeningen=[
                 ("rij", [("hier worden zaadcellen gemaakt", "de teelballen"),
                          ("hier rijpen de eicellen", "de eierstokken"),
                          ("hier groeit de baby", "de baarmoeder"),
                          ("hier gebeurt de bevruchting meestal", "de eileider")],
                  "Waar gebeurt dit?", WW),
                 ("rij", [("bevruchte eicel", r"\(1\)"), ("foetus", r"\(3\)"), ("embryo", r"\(2\)"),
                          ("baby", r"\(4\)")],
                  r"Zet de ontwikkeling in volgorde: schrijf \(1\) tot \(4\).", WW),
                 ("kort", "Hoelang duurt een menstruatiecyclus gemiddeld?", r"\(28\) dagen", W),
                 ("open", "Waarom verdikt het baarmoederslijmvlies elke cyclus?",
                  "Om een bevruchte eicel te kunnen opvangen en voeden. Komt die er niet, dan "
                  "wordt het slijmvlies afgestoten: dat is de menstruatie.", 4),
                 ("waar", "De vruchtbare periode valt tijdens de menstruatie.", False),
             ]),

        dict(kop="Voorbehoedsmiddelen",
             opdracht="Let op het verschil tussen zwangerschap voorkomen en soa's voorkomen.",
             oefeningen=[
                 ("rij", [("beschermt ook tegen soa's", "het condoom"),
                          ("is hormonaal", "de pil (ook het spiraaltje met hormonen, het staafje)"),
                          ("is maar één keer te gebruiken", "het condoom")],
                  "Over welk voorbehoedsmiddel gaat dit?", WW),
                 ("open", "Hoe zorgt de anticonceptiepil ervoor dat er geen zwangerschap komt?",
                  "De hormonen in de pil houden de eisprong tegen. Zonder eicel is bevruchting "
                  "onmogelijk.", 3),
                 ("open", "Waarom is een condoom het enige middel dat ook tegen soa's "
                          "beschermt?",
                  "Het is het enige dat een echte barrière vormt: lichaamsvochten komen niet bij "
                  "elkaar. Hormonen regelen alleen de eisprong en houden geen ziektekiemen "
                  "tegen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ecologie-en-biodiversiteit-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Ecologie en biodiversiteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Biotoop en factoren",
             opdracht="Abiotisch is niet-levend, biotisch is levend.",
             oefeningen=[
                 ("rij", [("de temperatuur", "abiotisch"), ("een vos die jaagt", "biotisch"),
                          ("de zuurtegraad van de bodem", "abiotisch"),
                          ("de hoeveelheid licht", "abiotisch"),
                          ("een schimmel op een stam", "biotisch")],
                  "Abiotische of biotische factor?", WW),
                 ("rij", [("temperatuur", "thermometer"), ("windsnelheid", "anemometer"),
                          ("verlichtingssterkte", "luxmeter"), ("zuurtegraad", "pH-meter")],
                  "Waarmee meet je dit?", WW),
                 ("kort", "Hoe noem je het uitzoeken van welke soort een plant of dier is, met "
                          "een tabel?", "determineren", W),
             ]),

        dict(kop="Voedselketens",
             opdracht="Pijlen wijzen naar wie eet, dus de kant van de energie op.",
             oefeningen=[
                 ("rij", [("gras", "producent"), ("een regenworm", "reducent"),
                          ("een vos", "consument (predator)"),
                          ("een schimmel op een dode boom", "reducent")],
                  "Producent, consument of reducent?", WW),
                 ("teken", "Teken een voedselketen van vier schakels uit een vijver, met pijlen "
                           "in de juiste zin.",
                  "Bijvoorbeeld: algen → watervlo → stekelbaars → snoek. De pijl wijst telkens "
                  "naar wie eet, want daar gaat de energie naartoe.", 45),
                 ("open", "Waarom staan er in een voedselpiramide onderaan het meeste "
                          "organismen?",
                  "Bij elke stap gaat het grootste deel van de energie verloren als warmte en "
                  "voor het eigen leven. Er blijft dus maar weinig over voor de laag erboven, "
                  "en die kan daardoor minder organismen voeden.", 5),
                 ("open", "In de keten gras → konijn → vos verdwijnen alle vossen. Wat gebeurt "
                          "er eerst, en wat daarna?",
                  "Eerst nemen de konijnen sterk toe, want niemand eet ze nog. Daarna eten die "
                  "konijnen het gras op, en als het gras op is, sterven ook zij door "
                  "voedselgebrek.", 5),
                 ("waar", "Een regenworm is een producent in de voedselketen.", False),
             ]),

        dict(kop="Biodiversiteit",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("rij", [("een soort die hier van nature niet thuishoort", "een exoot"),
                          ("een brug of tunnel voor dieren over een weg", "een ecoduct"),
                          ("het aantal soorten in een gebied", "biodiversiteit")],
                  "Hoe heet dit?", WW),
                 ("open", "Waarom is een weiland met tien soorten bloemen steviger dan een "
                          "weiland met één soort gras?",
                  "Als er een ziekte of een droogte komt, valt niet alles tegelijk weg: sommige "
                  "soorten houden het vol. Bij één soort is één tegenslag genoeg om alles "
                  "kwijt te zijn.", 5),
                 ("open", "Noem drie keuzes die je ecologische voetafdruk kleiner maken.",
                  "Minder vlees eten, met de fiets of het openbaar vervoer gaan in plaats van "
                  "met de auto, minder spullen kopen en ze langer gebruiken, minder verwarmen, "
                  "afval sorteren.", 4),
                 ("open", "In een vijver spoelt mest van een akker. Er komen enorm veel algen. "
                          "Wat gebeurt er daarna?",
                  "De algenlaag houdt het licht tegen, dus de waterplanten eronder sterven. Als "
                  "de algen zelf afsterven, verbruiken de bacteriën die ze afbreken alle "
                  "zuurstof, en dan sterven ook de vissen.", 5),
             ]),

        dict(kop="Aangepast aan je omgeving",
             opdracht="Zeg telkens welk voordeel de aanpassing oplevert.",
             oefeningen=[
                 ("rij", [("een ijsbeer heeft kleine oren", "minder warmteverlies"),
                          ("een cactus heeft stekels in plaats van bladeren", "minder verdamping"),
                          ("een haas wordt 's winters wit", "camouflage in de sneeuw")],
                  "Welk voordeel levert dit op?", WW),
                 ("open", "Een haas heeft de ogen aan de zijkant van zijn kop, een vos vooraan. "
                          "Verklaar dat verschil.",
                  "De haas is een prooi en moet bijna rondom kunnen kijken om een roofdier op "
                  "tijd te zien. De vos is een jager en heeft twee ogen naar voren nodig om "
                  "afstand goed te kunnen inschatten.", 5),
                 ("waar", "Kieuwen zijn een aanpassing om zuurstof uit de lucht te halen.",
                  False),
                 ("open", r"Je meet in een bos overdag \(300\) lux onder de bomen en \(20\,000\) lux op "
                          "de open plek. Wat besluit je daaruit over de planten onder de bomen?",
                  "Die planten moeten met heel weinig licht toekomen. Alleen schaduwplanten "
                  "houden dat vol, of planten die bloeien voor de bomen in blad komen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-materie-stoffen-en-mengsels-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Materie, stoffen en mengsels",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Faseovergangen",
             opdracht="Gebruik de naam van de overgang, niet 'warm worden'.",
             oefeningen=[
                 ("rij", [("vast → vloeibaar", "smelten"), ("vloeibaar → gas", "verdampen"),
                          ("gas → vloeibaar", "condenseren"), ("vloeibaar → vast", "stollen"),
                          ("gas → vast", "rijpen"), ("vast → gas", "vervluchtigen")],
                  "Hoe heet deze faseovergang?", WW),
                 ("rij", [("rijp op een tak", "rijpen"), ("een raam dat beslaat", "condenseren"),
                          ("droogijs dat verdwijnt", "vervluchtigen"),
                          ("een plas die opdroogt", "verdampen")],
                  "Welke faseovergang zie je hier?", WW),
                 ("waar", "Tijdens het smelten van ijs stijgt de temperatuur van het mengsel ijs "
                          "en water.", False),
             ]),

        dict(kop="Het deeltjesmodel",
             opdracht="Denk aan hoe dicht de deeltjes bij elkaar liggen en hoe hard ze bewegen.",
             oefeningen=[
                 ("open", "Waarom kan je een gas samenpersen en een vaste stof niet?",
                  "In een gas zitten de deeltjes ver uit elkaar met veel lege ruimte ertussen; "
                  "die ruimte kan je wegdrukken. In een vaste stof raken ze elkaar al, dus er is "
                  "niets meer om weg te duwen.", 5),
                 ("open", "Waarom heeft een vloeistof geen vaste vorm, maar wel een vast volume?",
                  "De deeltjes raken elkaar nog (dus het volume blijft gelijk) maar kunnen langs "
                  "elkaar schuiven (dus de vorm past zich aan het vat aan).", 4),
                 ("open", "Waarom zet een metalen staaf uit als je hem opwarmt, en waarom laten "
                          "ze bij een brug een kleine opening?",
                  "De deeltjes bewegen sneller en nemen daardoor meer plaats in, dus de staaf "
                  "wordt langer. Zonder opening zou de brug bij warm weer tegen zichzelf duwen "
                  "en kromtrekken of barsten.", 5),
                 ("open", "Waarom ruikt je hele keuken naar soep terwijl de pot in de hoek "
                          "staat?",
                  "Geurdeeltjes uit de soep gaan in de lucht en bewegen voortdurend alle kanten "
                  "op. Zo verspreiden ze zich vanzelf over de hele ruimte.", 4),
             ]),

        dict(kop="Fysisch of chemisch",
             opdracht="Blijft de stof dezelfde, of ontstaat er een nieuwe?",
             oefeningen=[
                 ("rij", [("water dat kookt", "fysisch"), ("hout dat verbrandt", "chemisch"),
                          ("suiker die oplost", "fysisch"), ("ijzer dat roest", "chemisch"),
                          ("een glas dat breekt", "fysisch")],
                  "Fysisch of chemisch verschijnsel?", WW),
                 ("open", "Een stukje ijzerwol wordt na een week in vochtige lucht bruin én "
                          "zwaarder. Wat is er gebeurd, en hoe weet je dat het chemisch is?",
                  "Het ijzer is geroest: het reageerde met zuurstof tot ijzeroxide. Je weet dat "
                  "het chemisch is aan de nieuwe kleur én aan de extra massa: er is zuurstof "
                  "bijgekomen.", 5),
                 ("open", "Een kaars brandt. Welke twee verschijnselen zie je tegelijk?",
                  "Fysisch: de was smelt en verdampt. Chemisch: de wasdamp verbrandt en er "
                  "ontstaan nieuwe stoffen (water en koolstofdioxide).", 4),
             ]),

        dict(kop="Zuivere stoffen en mengsels",
             opdracht="Gebruik de chemische symbolen waar dat gevraagd wordt.",
             oefeningen=[
                 ("rij", [("zuurstof", "O"), ("ijzer", "Fe"), ("waterstof", "H"),
                          ("koolstof", "C")],
                  "Wat is het chemisch symbool?"),
                 ("rij", [("zeewater", "mengsel"), ("zuiver water", "verbinding"),
                          ("lucht", "mengsel"), ("goud", "element")],
                  "Element, verbinding of mengsel?", WW),
                 ("open", "Water is H₂O. Wat betekent die formule precies?",
                  "Elke watermolecule bestaat uit twee waterstofatomen en één zuurstofatoom. "
                  "Het cijfertje slaat op het atoom dat ervoor staat.", 3),
                 ("waar", "Zuiver water en zeewater bevriezen bij dezelfde temperatuur.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-massadichtheid-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Massadichtheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De formule",
             opdracht=r"\(\rho = m / V\). Schrijf de formule op voor je rekent, en zet de eenheid erbij.",
             oefeningen=[
                 ("rij", [(r"\(m = 250\) g en \(V = 50\,\text{cm}^{3}\)", r"\(5\) g/\(\text{cm}^{3}\)"),
                          (r"\(m = 216\) g en \(V = 27\,\text{cm}^{3}\)", r"\(8\) g/\(\text{cm}^{3}\)"),
                          (r"\(m = 45\) g en \(V = 50\,\text{cm}^{3}\)", r"\(0{,}9\) g/\(\text{cm}^{3}\)")],
                  "Bereken de massadichtheid.", WW),
                 ("rij", [(r"\(4\,\text{cm}^{3}\) zilver (\(10{,}5\) g/\(\text{cm}^{3}\))", r"\(42\) g"),
                          (r"\(2{,}5\) L water (\(1\) g/\(\text{cm}^{3}\))", r"\(2\,500\) g of \(2{,}5\) kg"),
                          (r"\(2\) L olie (\(0{,}9\) g/\(\text{cm}^{3}\))", r"\(1\,800\) g of \(1{,}8\) kg")],
                  "Bereken de massa.", WW),
                 ("kort", r"IJzer weegt \(7{,}8\) g/\(\text{cm}^{3}\). Welk volume heeft een stuk van \(780\) g?",
                  r"\(100\,\text{cm}^{3}\)", W),
                 ("kort", "Wat is de SI-eenheid van massadichtheid?", r"kg/\(\text{m}^{3}\)", W),
             ]),

        dict(kop="Volume bepalen",
             opdracht="Regelmatig voorwerp: rekenen. Onregelmatig: onderdompelen.",
             oefeningen=[
                 ("rij", [(r"kubus met ribbe \(3\) cm", r"\(27\,\text{cm}^{3}\)"),
                          (r"balk \(6\) cm × \(3\) cm × \(2\) cm", r"\(36\,\text{cm}^{3}\)"),
                          (r"cilinder met straal \(2\) cm en hoogte \(10\) cm \((\pi \approx 3{,}14)\)", r"\(125{,}6\,\text{cm}^{3}\)")],
                  "Bereken het volume.", WW),
                 ("open", r"Het water in een maatcilinder staat op \(60\) mL. Je laat er een moer in "
                          r"zakken en het staat op \(78\) mL. De moer weegt \(48{,}6\) g. Bereken het "
                          "volume en de massadichtheid.",
                  r"Volume = \(78 - 60 = 18\) mL = \(18\,\text{cm}^{3} \cdot \rho = 48{,}6 : 18 = 2{,}7\) g/\(\text{cm}^{3}\) "
                  "(dat is aluminium).", 5),
                 ("rij", [(r"\(1\) L", r"\(1\,000\,\text{cm}^{3}\)"), (r"\(2\) L", r"\(0{,}002\,\text{m}^{3}\)"), (r"\(0{,}5\,\text{m}^{3}\)", r"\(500\) L")],
                  "Zet om.", WW),
                 ("rij", [(r"\(1\) g/\(\text{cm}^{3}\)", r"\(1\,000\) kg/\(\text{m}^{3}\)"), (r"\(2\,700\) kg/\(\text{m}^{3}\)", r"\(2{,}7\) g/\(\text{cm}^{3}\)")],
                  "Zet om.", WW),
             ]),

        dict(kop="Drijven en zinken",
             opdracht=r"Vergelijk telkens met water: \(1\) g/\(\text{cm}^{3}\).",
             oefeningen=[
                 ("rij", [(r"kurk, \(0{,}24\) g/\(\text{cm}^{3}\)", "drijft"), (r"aluminium, \(2{,}7\) g/\(\text{cm}^{3}\)", "zinkt"),
                          (r"olie, \(0{,}9\) g/\(\text{cm}^{3}\)", "drijft"), (r"ijs, \(0{,}92\) g/\(\text{cm}^{3}\)", "drijft")],
                  "Drijft of zinkt dit in water?", WW),
                 ("open", r"Een blokje weegt \(60\) g en heeft een volume van \(75\,\text{cm}^{3}\). Drijft het of "
                          "zinkt het? Reken het uit.",
                  r"\(\rho = 60 : 75 = 0{,}8\) g/\(\text{cm}^{3}\). Dat is kleiner dan \(1\), dus het drijft.", 4),
                 ("open", "Waarom drijft een vetlaag bovenop de soep?",
                  "Vet heeft een kleinere massadichtheid dan water. Bij hetzelfde volume is het "
                  "lichter, dus het blijft bovenaan.", 3),
                 ("waar", "Twee voorwerpen met dezelfde massa hebben altijd dezelfde "
                          "massadichtheid.", False),
             ]),

        dict(kop="Denken over massadichtheid",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Je meet van drie stukken van dezelfde stof: \(10\,\text{cm}^{3}\) weegt \(27\) g, "
                          r"\(20\,\text{cm}^{3}\) weegt \(54\) g, \(30\,\text{cm}^{3}\) weegt \(81\) g. Wat besluit je?",
                  r"De massadichtheid is telkens \(2{,}7\) g/\(\text{cm}^{3}\). Ze hangt dus niet af van de grootte "
                  "van het stuk: het is een stofeigenschap. Massa en volume zijn recht "
                  "evenredig.", 5),
                 ("open", "Je zet massa (y) uit tegenover volume (x) voor twee stoffen. De "
                          "rechte van A loopt steiler dan die van B. Wat weet je?",
                  "Allebei zijn het rechten door de oorsprong, dus allebei recht evenredig. A "
                  "heeft de grootste massadichtheid: bij hetzelfde volume weegt A meer.", 5),
                 ("open", "Beschrijf in stappen hoe je de massadichtheid van een onregelmatige "
                          "steen bepaalt.",
                  r"\(1\). Weeg de steen op een weegschaal, dat is m. \(2\). Vul een maatcilinder met "
                  r"water en lees het niveau af. \(3\). Laat de steen erin zakken en lees opnieuw "
                  r"af. \(4\). Het verschil is het volume V. \(5\). Reken \(\rho = m\) : V.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-energie-kracht-en-snelheid-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Energie, kracht en snelheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Energievormen en omzettingen",
             opdracht="Noem de vorm bij naam.",
             oefeningen=[
                 ("rij", [("een fietser die snel rijdt", "bewegingsenergie"),
                          ("een steen boven op een muur", "hoogte-energie"),
                          ("een boterham", "chemische energie"),
                          ("een gespannen veer", "veerenergie")],
                  "Welke energievorm is dit?", WW),
                 ("rij", [("een lamp", "elektrische → licht (en warmte)"),
                          ("een fietsdynamo", "beweging → elektrisch"),
                          ("een kaars", "chemisch → licht en warmte")],
                  "Welke energieomzetting gebeurt hier?", "230px"),
                 ("waar", "Bij elke energieomzetting gaat er een deel verloren als warmte.",
                  True),
             ]),

        dict(kop="Krachten",
             opdracht="Een kracht heeft een grootte, een richting, een zin en een aangrijpingspunt.",
             oefeningen=[
                 ("kort", "Wat is de eenheid van kracht?", "newton (N)", W),
                 ("kort", "Waarmee meet je een kracht?", "een dynamometer", W),
                 ("rij", [(r"twee mensen duwen elk \(200\) N in dezelfde zin", r"\(400\) N"),
                          (r"twee kinderen trekken elk \(150\) N in tegengestelde zin", r"\(0\) N, evenwicht")],
                  "Hoe groot is de resulterende kracht?", "230px"),
                 ("waar", r"Een kracht van \(10\) N naar links en een van \(10\) N naar rechts hebben "
                          "dezelfde richting maar een andere zin.", True),
                 ("waar", "Wrijvingskracht werkt altijd in dezelfde zin als de beweging.",
                  False),
                 ("open", "Een bal die je wegtrapt, verandert van richting én gaat sneller. "
                          "Welke uitwerkingen van een kracht zie je hier?",
                  "Twee dynamische uitwerkingen: de snelheid verandert (versnellen) en de "
                  "bewegingsrichting verandert.", 4),
             ]),

        dict(kop="Snelheid berekenen",
             opdracht=r"\(v = \Delta x / \Delta t\). Zet minuten eerst om naar seconden.",
             oefeningen=[
                 ("rij", [(r"\(150\) m in \(25\) s", r"\(6\) m/s"), (r"\(120\) km in \(1{,}5\) u", r"\(80\) km/h"),
                          (r"\(400\) m in \(50\) s", r"\(8\) m/s")],
                  "Bereken de snelheid.", WW),
                 ("rij", [(r"\(15\) m/s in km/h", r"\(54\) km/h"), (r"\(108\) km/h in m/s", r"\(30\) m/s"),
                          (r"\(36\) km/h in m/s", r"\(10\) m/s")],
                  "Zet om.", WW),
                 ("kort", r"Een fietser rijdt \(45\) s aan \(8\) m/s. Hoe ver raakt hij?", r"\(360\) m", W),
                 ("kort", r"Hoelang doet een wandelaar over \(600\) m aan \(4\) m/s?",
                  r"\(150\) s of \(2\) min \(30\) s", W),
                 ("open", r"Een auto rijdt het eerste uur \(60\) km en het tweede uur \(80\) km. Wat is "
                          "zijn gemiddelde snelheid?",
                  r"\(70\) km/h. Samen \(140\) km in \(2\) uur, dus \(140 : 2\). Je mag niet zomaar het "
                  "gemiddelde van de twee snelheden nemen als de tijden verschillen, hier "
                  "toevallig wel omdat het allebei één uur is.", 5),
                 ("open", r"Waarom zet je een tijdsduur van \(5\) minuten eerst om naar seconden "
                          "voor je in m/s rekent?",
                  "Omdat m/s meter per sécónde betekent. Reken je met minuten, dan staat er een "
                  r"andere eenheid in je uitkomst en is je antwoord \(60\) keer te groot.", 4),
             ]),

        dict(kop="Grafieken lezen",
             opdracht="Op de y-as staat de afgelegde weg, op de x-as de tijd.",
             oefeningen=[
                 ("rij", [("een rechte door de oorsprong", "een constante snelheid"),
                          ("een horizontaal stuk", "stilstand"),
                          ("een steiler stuk", "sneller")],
                  "Wat betekent dit in een grafiek van weg tegenover tijd?", "230px"),
                 ("open", r"In dezelfde grafiek lees je bij \(4\) s een afstand van \(20\) m af, op een "
                          "rechte door de oorsprong. Wat is de snelheid?",
                  r"\(5\) m/s. De helling van de rechte is de snelheid: \(20\) m : \(4\) s.", 3),
                 ("open", "Je legt altijd dezelfde afstand af. Welk verband is er tussen "
                          "snelheid en tijdsduur?",
                  "Omgekeerd evenredig: twee keer zo snel betekent de helft van de tijd. Het "
                  "product van snelheid en tijd blijft immers dezelfde afstand.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meten-en-eenheden-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Veilig werken, meten en eenheden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Veilig in het labo",
             opdracht="Antwoord kort maar volledig.",
             oefeningen=[
                 ("open", "Je morst een product op de werktafel. Wat doe je?",
                  "Je verwittigt meteen de leerkracht en raakt het niet met je blote handen aan. "
                  "Pas daarna ruim je op zoals hij of zij zegt.", 3),
                 ("waar", "Glasscherven veeg je het best met je blote handen bij elkaar.",
                  False),
                 ("open", "Waarom lees je de handleiding van een toestel voor je het gebruikt?",
                  "Om te weten hoe je het veilig instelt en afleest, en om het niet stuk te "
                  "maken. Achteraf lezen helpt niet meer als er al iets misging.", 3),
                 ("open", "Je werkt met levend materiaal uit een vijver. Wat doe je achteraf?",
                  "Je zet de dieren en planten levend terug waar je ze gehaald hebt, en je "
                  "wast je handen.", 3),
             ]),

        dict(kop="Meetinstrumenten",
             opdracht="Schrijf de naam van het instrument.",
             oefeningen=[
                 ("rij", [("massa", "weegschaal"), ("volume van een vloeistof", "maatcilinder"),
                          ("geluidssterkte", "sonometer (decibelmeter)"),
                          ("verlichtingssterkte", "luxmeter")],
                  "Waarmee meet je dit?", WW),
                 ("rij", [("lengte, heel nauwkeurig", "schuifmaat"),
                          ("een tijdsduur", "chronometer"),
                          ("een kracht", "dynamometer")],
                  "Waarmee meet je dit?", WW),
                 ("open", r"Je moet \(25\) mL water afmeten. Welk instrument kies je, en hoe lees je "
                          "het correct af?",
                  "Een maatcilinder, niet een bekerglas. Je leest af op ooghoogte, onderaan de "
                  "holle boog van het wateroppervlak (de meniscus).", 4),
                 ("waar", "Een schuifmaat meet nauwkeuriger dan een gewone meetlat.", True),
             ]),

        dict(kop="Grootheden en eenheden",
             opdracht="Een meting zonder eenheid is geen meting.",
             oefeningen=[
                 ("rij", [("lengte", "meter (m)"), ("massa", "kilogram (kg)"),
                          ("tijd", "seconde (s)"), ("temperatuur", "kelvin (K)")],
                  "Wat is de SI-eenheid?", WW),
                 ("rij", [(r"\(3\) mm in m", r"\(0{,}003\) m"), (r"\(1{,}5\) kg in g", r"\(1\,500\) g"),
                          (r"\(75\) cm in m", r"\(0{,}75\) m"), (r"\(250\) mL in L", r"\(0{,}25\) L")],
                  "Zet om.", WW),
                 ("waar", "De graad Celsius is de SI-eenheid van temperatuur.", False),
                 ("open", r"Een leerling meet de lengte van zijn tafel en schrijft op: \(1{,}2\). Wat "
                          "ontbreekt er, en waarom is dat erg?",
                  r"De eenheid. \(1{,}2\) kan meter zijn of centimeter of voet; zonder eenheid zegt het "
                  "getal niets en kan niemand je meting nakijken.", 4),
                 ("kort", "Welke Griekse letter is het symbool voor massadichtheid?",
                  r"\(\rho\) (rho)", W),
             ]),

        dict(kop="Meten met verstand",
             opdracht="Denk aan nauwkeurigheid en aan een realistische schatting.",
             oefeningen=[
                 ("kies", "Welke schatting van de massa van een appel is realistisch?",
                  [r"\(15\) g", r"\(150\) g", r"\(1\,500\) g"], 1),
                 ("open", r"Je meet dezelfde lengte drie keer: \(12{,}4\) cm, \(12{,}5\) cm en \(12{,}4\) cm. Wat "
                          "doe je met die resultaten?",
                  r"Je neemt het gemiddelde: \((12{,}4 + 12{,}5 + 12{,}4) : 3 \approx 12{,}43\) cm. Meerdere keren "
                  "meten en middelen maakt toevallige afleesfouten kleiner.", 4),
                 ("open", r"Je weegt een leeg bekerglas (\(120\) g) en daarna hetzelfde glas met "
                          r"water (\(370\) g). Hoeveel water zit erin, en welk volume is dat?",
                  r"\(250\) g water. Water weegt \(1\) g/\(\text{cm}^{3}\), dus dat is \(250\,\text{cm}^{3}\) ofwel \(250\) mL.", 4),
                 ("open", "Waarom schakel je een meettoestel uit als je even niet meet?",
                  "Om energie te sparen en de batterij te sparen. Dat hoort bij duurzaam "
                  "werken.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-wetenschappelijk-onderzoek-spark"] = dict(
    vak="Natuurwetenschappen", niveau=SPARK, titel="Wetenschappelijk onderzoek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De stappen",
             opdracht="Zet in volgorde en gebruik de juiste namen.",
             oefeningen=[
                 ("rij", [("data verzamelen", r"\(3\)"), ("onderzoeksvraag opstellen", r"\(1\)"),
                          ("conclusie trekken", r"\(4\)"), ("onderzoeksplan maken", r"\(2\)")],
                  r"Zet in volgorde: schrijf \(1\) tot \(4\).", WW),
                 ("kort", "Hoe noem je een verwachting die je vooraf opschrijft en daarna "
                          "toetst?", "een hypothese", W),
                 ("waar", "Als je hypothese niet uitkomt, is je onderzoek mislukt.", False),
                 ("open", "Wat is reflecteren op het einde van een onderzoek?",
                  "Terugkijken op hoe je gewerkt hebt: wat liep goed, wat zou je anders doen, "
                  "en hoe betrouwbaar zijn je metingen eigenlijk.", 4),
             ]),

        dict(kop="Een goede onderzoeksvraag",
             opdracht="Enkelvoudig, objectief, meetbaar en haalbaar.",
             oefeningen=[
                 ("rij", [("Hoeveel poten heeft een spin?", "opzoekvraag, niet te onderzoeken"),
                          ("Is een elektrische auto niet beter?", "niet objectief"),
                          ("Groeien planten sneller met meer licht én meer mest?", "niet enkelvoudig"),
                          (r"Hoeveel cm groeit tuinkers in \(7\) dagen bij \(5\) en bij \(10\) uur licht?", "goed")],
                  "Wat schort eraan? Schrijf kort.", "230px"),
                 ("open", "Herschrijf 'Groeien planten sneller met meer licht en meer mest?' tot "
                          "een goede onderzoeksvraag.",
                  r"Bijvoorbeeld: 'Hoeveel cm groeit een tuinkersplantje in zeven dagen bij \(4\) uur "
                  r"licht per dag, vergeleken met \(8\) uur licht per dag?' Eén ding tegelijk, "
                  "meetbaar en haalbaar.", 5),
                 ("open", "Je test of planten sneller groeien met meer licht. Noem vier dingen "
                          "die je gelijk moet houden.",
                  "Dezelfde soort plant, dezelfde hoeveelheid water, dezelfde potgrond en "
                  "potgrootte, dezelfde temperatuur, en even oude zaadjes.", 4),
             ]),

        dict(kop="Besluiten trekken",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Een leerling besluit: 'Mijn hypothese was juist, want ik vond het "
                          "logisch.' Wat schort daaraan?",
                  "Een besluit moet steunen op je metingen, niet op wat je logisch vindt. Zonder "
                  "data is het een mening en geen conclusie.", 4),
                 ("open", "Een onderzoeker meet maar één plant en besluit dat alle planten zo "
                          "groeien. Wat is er fout?",
                  "Eén meting kan toeval zijn. Je hebt meerdere planten en herhalingen nodig "
                  "voor je iets over alle planten mag zeggen.", 4),
                 ("open", "Je onderzoekt of een plant met mest sneller groeit, maar je zet die "
                          "plant ook nog eens voor het raam. Wat is het probleem?",
                  "Je verandert twee dingen tegelijk. Groeit die plant sneller, dan weet je niet "
                  "of dat door de mest of door het licht komt.", 4),
                 ("open", "Wat is het verschil tussen een waarneming en een besluit?",
                  r"Een waarneming is wat je ziet of meet ('de plant is \(8\) cm gegroeid'). Een "
                  "besluit is wat je daaruit afleidt ('meer licht doet tuinkers sneller "
                  "groeien').", 4),
             ]),

        dict(kop="Formules en verbanden",
             opdracht="Reken met de formule, of lees het verband uit de tabel.",
             oefeningen=[
                 ("rij", [(r"uit \(v = \Delta x / \Delta t\): schrijf \(\Delta t\)", r"\(\Delta t = \Delta x / v\)"),
                          (r"uit \(\rho = m / V\): schrijf m", r"\(m = \rho \times V\)"),
                          (r"uit \(\rho = m / V\): schrijf V", r"\(V = m / \rho\)")],
                  "Vorm de formule om.", "230px"),
                 ("open", r"Uit een tabel lees je: bij \(10^{\circ}\text{C}\) duurt het \(40\) min, bij \(20^{\circ}\text{C}\,20\) min, "
                          r"bij \(40^{\circ}\text{C}\,10\) min. Welk verband is dat, en hoe zie je dat?",
                  "Omgekeerd evenredig: telkens als de temperatuur verdubbelt, halveert de "
                  r"tijd. Het product temperatuur × tijd blijft \(400\).", 4),
                 ("waar", "Een grafiek met een rechte door de oorsprong wijst op een recht "
                          "evenredig verband.", True),
                 ("open", r"Je meet afkoelend water: \(80^{\circ}\text{C}\), \(60^{\circ}\text{C}\), \(45^{\circ}\text{C}\), \(35^{\circ}\text{C}\), \(30^{\circ}\text{C}\), telkens "
                          "na vijf minuten. Wat zie je in de grafiek?",
                  "Een dalende lijn die steeds vlakker wordt. Het water koelt in het begin snel "
                  "af en daarna trager, want het verschil met de kamertemperatuur wordt "
                  "kleiner.", 5),
             ]),
    ],
)


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)
        print("  ", naam)


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-cellen-weefsels-en-organen-spark"] = dict(
    reeksen=[
        dict(aanpak="Loop de ladder telkens van klein naar groot af: cel, weefsel, orgaan, stelsel, "
                    "organisme. Zoek waar het voorbeeld op die ladder past.",
             waarom=[
                 None,
                 None,
                 "Het hart bestaat uit verschillende weefsels (spierweefsel, zenuwweefsel, bindweefsel) "
                 "die samen één taak uitvoeren. Dat maakt het een orgaan.",
                 None,
             ]),
        dict(aanpak="Onthoud welke drie onderdelen enkel bij een plantencel horen: de celwand, de grote "
                    "vacuole en de bladgroenkorrels. De rest hebben plant en dier allebei.",
             waarom=[
                 None,
                 None,
                 "Een dierlijke cel heeft wel een celmembraan, maar geen stevige celwand. Daarom kan "
                 "een dier bewegen en van vorm veranderen.",
                 None,
             ]),
        dict(aanpak="Noem bij elk antwoord het celonderdeel bij naam en zeg wat het doet. Een verklaring "
                    "zonder dat onderdeel is nooit volledig.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "Een loep vergroot ongeveer tien keer, een lichtmicroscoop vierhonderd keer of meer. "
                 "Dat is het verschil tussen niets zien en cellen zien.",
             ]),
        dict(aanpak="Een stelsel is een groep organen met één gezamenlijke taak. Vraag je bij elke "
                    "oefening af welke taak dat is.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-fotosynthese-en-de-plant-spark"] = dict(
    reeksen=[
        dict(aanpak="Schrijf de reactie uit als één pijl: water en koolstofdioxide worden, met licht en "
                    "bladgroen, glucose en zuurstof. Alles in deze reeks komt uit die ene regel.",
             waarom=[
                 None,
                 None,
                 "Het is net omgekeerd: CO₂ gaat erin en zuurstof komt eruit. Een plant verbruikt wel "
                 "zuurstof bij haar eigen celademhaling, maar dat is een ander proces.",
                 None,
             ]),
        dict(aanpak="Volg twee wegen door de plant: het water gaat van de wortel via de stengel naar "
                    "het blad, en de suiker gaat van het blad naar de voorraad.",
             waarom=[
                 None,
                 None,
                 None,
                 "Autotroof betekent letterlijk zichzelf voedend. Dieren zijn heterotroof: zij moeten "
                 "hun energierijke stoffen bij anderen halen.",
             ]),
        dict(aanpak="Zet de twee naast elkaar: fotosynthese maakt glucose en heeft licht nodig, "
                    "celademhaling verbrandt glucose en loopt dag en nacht door. Een plant doet allebei.",
             waarom=[
                 None,
                 None,
                 "'s Nachts staat de fotosynthese stil terwijl de celademhaling doorloopt. Dan "
                 "verbruikt de plant dus netto zuurstof in plaats van ze af te geven.",
                 None,
             ]),
        dict(aanpak="Hier pas je de reactie toe op het echte leven. Zoek telkens welk stuk van de "
                    "reactie in het voorbeeld meespeelt.",
             waarom=[
                 None,
                 None,
                 None,
                 "Haar suikers maakt een plant zelf, maar voor haar bladgroen, haar eiwitten en haar "
                 "dna heeft ze ook stikstof, fosfor, magnesium en ijzer nodig. Die haalt ze als "
                 "mineralen uit de bodem.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-menselijk-lichaam-spark"] = dict(
    reeksen=[
        dict(aanpak="Volg het eten van voor naar achter en zeg bij elk station wat er gebeurt: kauwen "
                    "en speeksel, doorslikken, zuur in de maag, opname in de dunne darm, water eruit in "
                    "de dikke darm.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "Gal wordt gemaakt in de lever en bewaard in de galblaas, niet in de maag. De maag "
                 "maakt maagsap met zoutzuur.",
             ]),
        dict(aanpak="Teken het hart met zijn vier holtes en volg het bloed: rechts het zuurstofarme "
                    "bloed naar de longen, links het zuurstofrijke bloed naar de rest van het lichaam.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "Een slagader voert bloed wég van het hart, en hier is dat zuurstofarm bloed op weg "
                 "naar de longen. De naam zegt dus iets over de richting, niet over de zuurstof.",
                 None,
                 None,
             ]),
        dict(aanpak="Antwoord in volle zinnen en noem de stelsels bij naam. De vraag is telkens: wie "
                    "levert wat, en wie brengt het waar?",
             waarom=[
                 None,
                 "In de longen gebeurt alleen de gasuitwisseling. De verbranding zelf gebeurt in de "
                 "mitochondriën van elke cel, en dat is de verwarring die hier het vaakst opduikt.",
                 None,
             ]),
        dict(aanpak="Denk aan de twee driehoeken: de voedingsdriehoek zegt wat je het best vaak eet, de "
                    "bewegingsdriehoek zet lang stilzitten apart onderaan.",
             waarom=[
                 None,
                 None,
                 None,
                 "Water levert geen energie, maar zonder water werkt geen enkele cel. Daarom telt het "
                 "wel degelijk als voedingsstof.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-voortplanting-spark"] = dict(
    reeksen=[
        dict(aanpak="Tel de ouders: één ouder is aseksueel, twee ouders zijn seksueel. Dat is het hele "
                    "onderscheid.",
             waarom=[
                 None,
                 None,
                 "Bij stekken komt alle erfelijke informatie van één plant. Je krijgt dus een kloon, "
                 "erfelijk identiek aan de moederplant.",
                 None,
             ]),
        dict(aanpak="Hou de twee delen uit elkaar: de meeldraad is mannelijk en maakt stuifmeel, de "
                    "stamper is vrouwelijk en vangt het op. De stamper bestaat uit stempel, stijl en "
                    "vruchtbeginsel.",
             waarom=[
                 "Een geheugensteun: meeldraad begint met m, net als mannelijk. Alles wat in het midden "
                 "staat, hoort bij de stamper.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Volg de weg: de eicel rijpt in de eierstok, komt in de eileider waar de "
                    "bevruchting meestal gebeurt, en nestelt zich daarna in de baarmoeder.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "De eisprong valt ongeveer veertien dagen vóór de volgende menstruatie, dus midden in "
                 "de cyclus. Tijdens de menstruatie zelf is de kans het kleinst, maar nooit nul.",
             ]),
        dict(aanpak="Hou twee vragen uit elkaar: houdt het middel een zwangerschap tegen, en houdt het "
                    "ziektekiemen tegen? Alleen het condoom doet allebei.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-ecologie-en-biodiversiteit-spark"] = dict(
    reeksen=[
        dict(aanpak="Vraag je bij elke factor af of ze leeft. Leeft ze, dan is ze biotisch; gaat het "
                    "over temperatuur, licht, water of bodem, dan is ze abiotisch.",
             waarom=[None, None, None]),
        dict(aanpak="De pijl wijst altijd naar wie eet, dus de kant van de energie op. Begin je keten "
                    "bij een producent: die maakt zijn eigen voedsel met licht.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "Een producent maakt zijn eigen voedsel met licht. Een regenworm eet dood "
                 "plantenmateriaal en breekt het af, en is dus een reducent.",
             ]),
        dict(aanpak="Biodiversiteit is de verscheidenheid aan soorten in een gebied. Vraag je bij elke "
                    "oefening af wat er gebeurt als die verscheidenheid kleiner wordt.",
             waarom=[
                 "Een exoot is niet per se schadelijk. Hij wordt het wel als hij hier geen natuurlijke "
                 "vijand heeft en de soorten verdringt die er al leefden.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Zeg bij elke aanpassing welk voordeel ze oplevert: minder warmte verliezen, minder "
                    "water verliezen, minder opvallen, of beter zien.",
             waarom=[
                 None,
                 None,
                 "Kieuwen halen zuurstof uit het wáter. Longen halen hem uit de lucht, en daarom stikt "
                 "een vis op het droge, al zit er in lucht veel meer zuurstof.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-materie-stoffen-en-mengsels-spark"] = dict(
    reeksen=[
        dict(aanpak="Zeg bij elke overgang van welke fase naar welke, en of er warmte bij moet of net "
                    "weg. Zo kom je op de naam uit, ook bij rijpen en vervluchtigen.",
             waarom=[
                 None,
                 "Rijp slaat waterdamp meteen als ijs neer (gas naar vast) en droogijs gaat meteen van "
                 "vast naar gas. Die twee slaan de vloeibare fase over.",
                 "Tijdens een faseovergang blijft de temperatuur gelijk. Alle warmte die je toevoegt, "
                 "gaat naar het losmaken van de deeltjes en niet naar het opwarmen.",
             ]),
        dict(aanpak="Teken de deeltjes in gedachten: in een vaste stof dicht op elkaar en trillend op "
                    "hun plaats, in een vloeistof tegen elkaar maar schuivend, in een gas ver uit "
                    "elkaar en snel.",
             waarom=[
                 None,
                 None,
                 "Dat uitzetten is klein maar niet te verwaarlozen: een stalen brug van honderd meter "
                 "wordt op een hete dag enkele centimeters langer.",
                 None,
             ]),
        dict(aanpak="Eén vraag volstaat: blijft het dezelfde stof, of ontstaat er een nieuwe? Verandert "
                    "alleen de vorm of de fase, dan is het fysisch.",
             waarom=[
                 "Bij koken, oplossen en breken blijft de stof zichzelf: je kan de damp weer laten "
                 "condenseren en de suiker weer uit het water halen. Bij branden en roesten kan dat "
                 "niet meer.",
                 None,
                 None,
             ]),
        dict(aanpak="Drie trappen: een element bestaat uit één soort atoom, een verbinding uit vaste "
                    "combinaties van atomen, en een mengsel uit verschillende stoffen door elkaar.",
             waarom=[
                 None,
                 None,
                 None,
                 "Zuiver water bevriest bij 0 °C, zeewater pas rond -2 °C. Opgeloste stoffen verlagen "
                 "het vriespunt, en dat is ook waarom men zout op de weg strooit.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-massadichtheid-spark"] = dict(
    reeksen=[
        dict(aanpak="Schrijf eerst de formule op, zet de gegevens eronder met hun eenheid, en reken dan "
                    "pas. Zo zie je meteen of je moet delen of vermenigvuldigen.",
             waarom=[
                 None,
                 None,
                 "Uit \\(\\rho = m / V\\) volgt \\(V = m / \\rho\\), dus \\(780 : 7{,}8 = 100\\,"
                 "\\text{cm}^{3}\\).",
                 "De SI-eenheid is kg/\\(\\text{m}^{3}\\), maar in de praktijk reken je bijna altijd in "
                 "g/\\(\\text{cm}^{3}\\). Eén g/\\(\\text{cm}^{3}\\) is \\(1\\,000\\) kg/"
                 "\\(\\text{m}^{3}\\).",
             ]),
        dict(aanpak="Is het voorwerp regelmatig, dan reken je het volume uit met een formule. Is het "
                    "onregelmatig, dan dompel je het onder en lees je het verschil af.",
             waarom=[
                 None,
                 "Eén mL is precies \\(1\\,\\text{cm}^{3}\\). Daarom kan je het verschil in de "
                 "maatcilinder zonder omrekenen als volume gebruiken.",
                 None,
                 None,
             ]),
        dict(aanpak="Vergelijk telkens met water: \\(1\\) g/\\(\\text{cm}^{3}\\). Minder dan \\(1\\) "
                    "drijft, meer dan \\(1\\) zinkt. De massa alleen zegt niets.",
             waarom=[
                 None,
                 None,
                 None,
                 "Massadichtheid hangt af van de massa én van het volume. Een kilo veren en een kilo "
                 "lood wegen evenveel, maar de veren nemen veel meer plaats in.",
             ]),
        dict(aanpak="Massadichtheid is een stofeigenschap: ze hangt niet af van hoe groot je stuk is. "
                    "Dat is de rode draad door deze hele reeks.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-energie-kracht-en-snelheid-spark"] = dict(
    reeksen=[
        dict(aanpak="Noem de energievorm bij naam, en zeg bij een omzetting altijd van welke vorm naar "
                    "welke.",
             waarom=[
                 None,
                 None,
                 "Die warmte is niet verdwenen, ze is alleen niet meer bruikbaar voor wat je wou. "
                 "Daarom haalt geen enkel toestel honderd procent.",
             ]),
        dict(aanpak="Een kracht heeft vier kenmerken: een grootte, een richting, een zin en een "
                    "aangrijpingspunt. Teken ze als een pijl, dan zie je richting en zin meteen.",
             waarom=[
                 None,
                 None,
                 "Krachten in dezelfde zin tel je op, krachten in tegengestelde zin trek je af. "
                 "\\(150\\) N tegen \\(150\\) N geeft dus \\(0\\) N: evenwicht.",
                 "De richting is de lijn waarop de kracht werkt, hier horizontaal. De zin is de kant "
                 "waarnaar ze wijst. Links en rechts liggen dus op dezelfde lijn.",
                 "Wrijving werkt altijd tégen de beweging in. Daarom remt ze af, en daarom heb je ze "
                 "net nodig om je te kunnen afzetten.",
                 None,
             ]),
        dict(aanpak="\\(v = \\Delta x / \\Delta t\\). Zet eerst alles in dezelfde eenheden: meter en "
                    "seconde voor m/s, kilometer en uur voor km/h.",
             waarom=[
                 None,
                 "Van m/s naar km/h vermenigvuldig je met \\(3{,}6\\); van km/h naar m/s deel je door "
                 "\\(3{,}6\\).",
                 None,
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="In een grafiek van de weg tegenover de tijd is de helling de snelheid. Steiler is "
                    "sneller, een vlak stuk betekent stilstand.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-werken-meten-en-eenheden-spark"] = dict(
    reeksen=[
        dict(aanpak="Bij elk antwoord geldt dezelfde volgorde: eerst jezelf en de anderen veilig "
                    "houden, dan de leerkracht verwittigen, en pas daarna opruimen.",
             waarom=[
                 None,
                 "Gebruik een borstel en een blik, nooit je handen. Een splinter glas zie je niet "
                 "altijd liggen.",
                 None,
                 None,
             ]),
        dict(aanpak="Kies je instrument naar wat je meet én naar hoe nauwkeurig het moet zijn. Een "
                    "bekerglas toont een volume ruwweg, een maatcilinder meet het.",
             waarom=[
                 None,
                 None,
                 None,
                 "Een schuifmaat leest tot op een tiende millimeter af, een gewone meetlat tot op een "
                 "millimeter.",
             ]),
        dict(aanpak="Hou de grootheid (wat je meet) en de eenheid (waarin je het uitdrukt) uit elkaar, "
                    "en schrijf bij elk getal zijn eenheid.",
             waarom=[
                 None,
                 "Zet om via de trap: van mm naar m deel je door \\(1\\,000\\), van kg naar g "
                 "vermenigvuldig je met \\(1\\,000\\).",
                 "De SI-eenheid van temperatuur is de kelvin. \\(0\\) °C is \\(273{,}15\\) K, en een "
                 "stap van één graad is in allebei even groot.",
                 None,
                 None,
             ]),
        dict(aanpak="Vraag je bij elk getal af of het realistisch is, en meet liever meerdere keren. "
                    "Een enkele meting kan er altijd eens naast zitten.",
             waarom=[
                 "Een appel van \\(15\\) g zou zo licht zijn als een blad papier, een van \\(1\\,500\\) "
                 "g zo zwaar als anderhalve liter water. \\(150\\) g klopt wel.",
                 None,
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-wetenschappelijk-onderzoek-spark"] = dict(
    reeksen=[
        dict(aanpak="De volgorde is altijd dezelfde: vraag, plan, meten, besluiten. En daarna kijk je "
                    "terug op hoe het gelopen is.",
             waarom=[
                 None,
                 None,
                 "Een hypothese die niet uitkomt, is óók een resultaat. Je weet nu iets dat je ervoor "
                 "niet wist, en daarvoor deed je het onderzoek.",
                 None,
             ]),
        dict(aanpak="Toets elke vraag aan vier eisen: enkelvoudig (één ding tegelijk), objectief (geen "
                    "oordeel erin), meetbaar en haalbaar.",
             waarom=[
                 "Een opzoekvraag heeft haar antwoord al in een boek staan; daar heb je geen proef "
                 "voor nodig. En het woordje beter in de tweede vraag zit vol oordeel.",
                 None,
                 None,
             ]),
        dict(aanpak="Een besluit steunt op je metingen en op niets anders. Verander ook maar één ding "
                    "tegelijk, anders weet je achteraf niet waardoor het kwam.",
             waarom=[
                 "Logisch klinken en kloppen zijn twee verschillende dingen. Heel wat verwachtingen "
                 "die logisch leken, bleken bij het meten niet te kloppen.",
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Omvormen doe je stap voor stap: wat links gedeeld wordt, komt rechts te "
                    "vermenigvuldigen. Bij een tabel kijk je wat er met het product of het quotiënt "
                    "gebeurt.",
             waarom=[
                 None,
                 None,
                 "Let op de woorden door de oorsprong. Een rechte die de y-as hoger snijdt, is wel "
                 "lineair maar niet recht evenredig.",
                 None,
             ]),
    ],
)
