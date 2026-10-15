# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij geschiedenis ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof, alleen met moeilijkere vragen. Net als bij de leerbundel gaat
dezelfde pdf dus bij allebei de delen.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm: andere jaartallen om mee te rekenen, andere bronnen om te beoordelen,
andere gevallen om in te delen. Wie hier iets bijschrijft, legt het eerst
naast `../../spark/geschiedenis.json`.

De bestandsnaam eindigt op `-spark`. Dat is geen versiering: Beheer → Leerstof
zoekt daardoor enkel in de hoofdstukken van ✨ Spark, zodat "Prehistorie" niet
bij het Start-hoofdstuk belandt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

SPARK = "✨ Spark — 1ste en 2de middelbaar"

# Een begrip als "standplaatsgebondenheid" past niet in een vakje dat voor een
# getal gemaakt is. Vandaar deze twee breedtes; zie ook oefenbundel.py.
W = "130px"
WW = "200px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een vraag met jaartallen mag je je berekening ernaast zetten.",
    "Sta je vast? Sla die oefening over en kom er op het einde op terug.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-historisch-referentiekader-spark"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het historisch referentiekader",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eeuwen en millennia",
             opdracht="Reken zelf. Let op: een eeuw loopt van jaar 01 tot en met jaar 00.",
             oefeningen=[
                 ("rij", [("1066", "de 11de eeuw"), ("1600", "de 16de eeuw"),
                          ("1801", "de 19de eeuw"), ("2000", "de 20ste eeuw")],
                  "In welke eeuw ligt dit jaartal?", WW),
                 ("rij", [("de 3de eeuw", "201 tot en met 300"),
                          ("de 15de eeuw", "1401 tot en met 1500"),
                          ("de 21ste eeuw", "2001 tot en met 2100")],
                  "Van welk jaar tot welk jaar loopt deze eeuw?", WW),
                 ("kort", "Hoeveel eeuwen zitten er in twee millennia?", "20", W),
                 ("open", "Het jaar 1900 hoort bij de 19de eeuw, het jaar 1901 bij de 20ste. "
                          "Leg uit waarom dat zo is.",
                  "Een eeuw begint bij het jaar 01 en eindigt bij het jaar 00. De 19de eeuw "
                  "loopt dus van 1801 tot en met 1900; de 20ste begint pas in 1901.", 3),
             ]),

        dict(kop="Voor en na Christus",
             opdracht="Vóór Christus tellen de jaartallen achterwaarts.",
             oefeningen=[
                 ("rij", [("753 v.C. of 44 v.C.", "753 v.C."),
                          ("300 v.C. of 300 n.C.", "300 v.C."),
                          ("3300 v.C. of 1274 v.C.", "3300 v.C.")],
                  "Welk jaartal ligt het verst in het verleden?", WW),
                 ("rij", [("van 753 v.C. tot 476 n.C.", "1 229 jaar"),
                          ("van 3300 v.C. tot 800 v.C.", "2 500 jaar"),
                          ("van 476 tot 1500", "1 024 jaar")],
                  "Hoeveel jaar zit ertussen?", WW),
                 ("waar", "Er bestaat geen jaar 0: na het jaar 1 v.C. komt meteen het jaar 1 n.C.", True),
                 ("teken", "Teken een tijdlijn en zet deze vijf scharnierpunten erop: "
                           "3300 v.C. (het schrift), 800 v.C., 476, 1500 en 1789.",
                  "Van links naar rechts: 3300 v.C., 800 v.C., 476, 1500, 1789. De onderlinge "
                  "afstanden hoeven niet exact te kloppen, de volgorde wel.", 42),
             ]),

        dict(kop="De zeven periodes",
             opdracht="Gebruik de namen zoals ze in de bundel staan.",
             oefeningen=[
                 ("kort", "Hoeveel periodes telt het westerse referentiekader?", "zeven", W),
                 ("rij", [("na de prehistorie", "het oude nabije oosten"),
                          ("na de klassieke oudheid", "de middeleeuwen"),
                          ("na de middeleeuwen", "de vroegmoderne tijd"),
                          ("na de moderne tijd", "de hedendaagse tijd")],
                  "Welke periode komt hierna?", WW),
                 ("rij", [("het schrift, rond 3300 v.C.", "prehistorie → oude nabije oosten"),
                          ("de val van het West-Romeinse Rijk in 476", "klassieke oudheid → middeleeuwen"),
                          ("de Franse Revolutie in 1789", "vroegmoderne tijd → moderne tijd"),
                          ("het einde van de Tweede Wereldoorlog in 1945", "moderne tijd → hedendaagse tijd")],
                  "Tussen welke twee periodes ligt dit scharnierpunt?", WW),
                 ("waar", "De prehistorie is de langste van de zeven periodes.", True),
             ]),

        dict(kop="Evolutie of revolutie",
             opdracht="Denk aan het tempo van de verandering, niet aan het gevolg.",
             oefeningen=[
                 ("rij", [("de overgang van jagen naar landbouw", "allebei"),
                          ("de Franse Revolutie van 1789", "revolutie"),
                          ("het langzaam verdwijnen van het Latijn", "evolutie")],
                  "Evolutie, revolutie, of allebei?", WW),
                 ("open", "Historici noemen de agrarische revolutie soms een evolutie en soms "
                          "een revolutie. Leg uit hoe dat allebei kan kloppen.",
                  "Revolutie omdat de gevolgen enorm waren: vaste woonplaatsen, steden, bezit, "
                  "beroepen. Evolutie omdat de overgang zelf duizenden jaren duurde en per "
                  "streek op een ander moment gebeurde.", 4),
                 ("waar", "Een scharnierpunt geldt voor de hele wereld tegelijk.", False),
                 ("open", "De indeling in zeven periodes komt uit Europa. Waarom past ze niet "
                          "goed op de geschiedenis van Afrika of Azië?",
                  "De scharnierpunten zijn Europese gebeurtenissen. In andere werelddelen "
                  "gebeurden op die momenten heel andere dingen, dus de knippen liggen daar "
                  "elders. De indeling is een afspraak onder historici, geen natuurwet.", 4),
             ]),

        dict(kop="De maatschappelijke domeinen",
             opdracht="Politiek, economisch, sociaal of cultureel. Soms passen er twee.",
             oefeningen=[
                 ("rij", [("een koning kroont zichzelf", "politiek"),
                          ("een nieuwe munt wordt ingevoerd", "economisch"),
                          ("slaven mogen niet stemmen", "sociaal"),
                          ("een tempel voor een god bouwen", "cultureel")],
                  "Bij welk domein hoort dit?", WW),
                 ("kies", "Het bronzen beeld van een Romeinse senator hoort in twee domeinen "
                          "tegelijk. Welke twee?",
                  ["politiek en cultureel", "economisch en sociaal", "sociaal en cultureel"], 0),
                 ("kort", "Welk domein gaat over handel, landbouw en geld?", "economisch", W),
                 ("kort", "Welk domein gaat over de groepen in de samenleving?", "sociaal", W),
             ]),

        dict(kop="De structuurbegrippen",
             opdracht="Denk aan de tegenstellingen die je in de bundel geleerd hebt.",
             oefeningen=[
                 ("rij", [("Athene", "stedelijk"), ("Sparta", "ruraal"),
                          ("een dorp midden in de velden", "ruraal"),
                          ("een samenleving die eeuwen amper verandert", "statisch")],
                  "Welk structuurbegrip past hier?", WW),
                 ("kort", "Hoe heet de volgorde van vroeger naar later, in één woord?", "chronologie", W),
                 ("open", "Wat bedoelen historici als ze zeggen dat onze periodisering "
                          "tijdsgebonden is?",
                  "Ze is gemaakt door mensen uit een bepaalde tijd en streek. Wie vandaag "
                  "indeelt, kijkt met de ogen van vandaag; over honderd jaar kan een historicus "
                  "de knippen ergens anders leggen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-prehistorie-spark"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="De prehistorie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De eerste mensen",
             opdracht="Vul aan met één woord, of met de naam die in de bundel staat.",
             oefeningen=[
                 ("kort", "Op welk werelddeel ontstond de moderne mens?", "Afrika", W),
                 ("kort", "Wat betekent <i>Homo sapiens</i> letterlijk?", "de wijze mens", WW),
                 ("kort", "Wat betekent het woord prehistorie letterlijk: de tijd vóór het …?",
                  "schrift", W),
                 ("rij", [("Homo erectus", "de rechtopstaande mens"),
                          ("Homo habilis", "de handige mens"),
                          ("Homo sapiens", "de wijze mens")],
                  "Wat betekent deze naam?", WW),
                 ("waar", "De Homo sapiens was de eerste mensachtige die Afrika verliet.", False),
             ]),

        dict(kop="Jagers en verzamelaars",
             opdracht="Denk aan hoe je leeft als je niets kan bewaren.",
             oefeningen=[
                 ("kort", "Hoe noem je mensen die rondtrekken en nergens vast wonen?",
                  "nomaden", W),
                 ("open", "Waarom trok een groep jagers en verzamelaars steeds verder?",
                  "Omdat ze aten wat de natuur op die plek gaf. Was het wild weggetrokken of "
                  "waren de vruchten op, dan moesten ze mee met het voedsel.", 3),
                 ("rij", [("licht geven in een grot", "vuur"), ("scherpe werktuigen maken", "vuursteen"),
                          ("vlees beter verteerbaar maken", "vuur")],
                  "Waarvoor diende dit?", WW),
                 ("open", "Waarom was koken of roosteren een grote stap vooruit voor de mens?",
                  "Gekookt voedsel is makkelijker te verteren en veiliger, dus je haalt er meer "
                  "energie uit en wordt er minder ziek van. Het bewaart ook langer.", 3),
                 ("waar", "Jagers en verzamelaars aten uitsluitend vlees.", False),
                 ("kort", "In welke Franse grot vind je beroemde prehistorische schilderingen?",
                  "Lascaux", W),
             ]),

        dict(kop="De agrarische revolutie",
             opdracht="Let op het verschil tussen de oorzaak en het gevolg.",
             oefeningen=[
                 ("kort", "Hoe noem je het leven op een vaste woonplaats?", "sedentair leven", WW),
                 ("kort", "Hoe heet de nieuwe steentijd, de periode van de landbouw?",
                  "neolithicum", W),
                 ("kort", "Hoe noem je voedsel dat overblijft nadat de boer zichzelf gevoed heeft?",
                  "een overschot", W),
                 ("kies", "Waar begon de landbouw als eerste?",
                  ["in de Vruchtbare Halvemaan", "in Egypte", "in China", "in Europa"], 0),
                 ("waar", "De landbouw ontstond overal ter wereld op hetzelfde moment.", False),
             ]),

        dict(kop="Wat de landbouw veranderde",
             opdracht="Zet de ketting van gevolgen in de juiste volgorde.",
             oefeningen=[
                 ("rij", [("er is een overschot", "1"), ("er ontstaat een stad", "4"),
                          ("mensen blijven op één plek", "2"),
                          ("niet iedereen hoeft nog te boeren", "3")],
                  "Zet deze vier in volgorde: schrijf 1, 2, 3 of 4.", WW),
                 ("kort", "Hoe noem je het verschijnsel dat mensen zich op één beroep toeleggen?",
                  "specialisatie", W),
                 ("open", "Leg uit hoe een voedseloverschot tot ongelijkheid leidde.",
                  "Wie meer grond of meer vee had, hield meer over. Dat bezit kon je doorgeven "
                  "aan je kinderen, dus het verschil groeide van generatie op generatie.", 4),
                 ("open", "Het sedentaire leven had ook nadelen. Noem er twee.",
                  "Ziektes verspreidden zich sneller doordat mensen dicht op elkaar en bij hun "
                  "dieren woonden; het eten werd eentoniger; een misoogst betekende honger, "
                  "want je kon niet wegtrekken.", 4),
                 ("waar", "Door de landbouw werden alle mensen even rijk.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mesopotamie-en-egypte-spark"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Mesopotamië en Egypte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Twee rivierbeschavingen",
             opdracht="Schrijf per vraag het juiste woord in het vakje.",
             oefeningen=[
                 ("kort", "Wat betekent de naam Mesopotamië letterlijk?",
                  "het land tussen de rivieren", WW),
                 ("rij", [("Mesopotamië", "de Eufraat en de Tigris"), ("Egypte", "de Nijl")],
                  "Aan welke rivier of rivieren lag dit rijk?", WW),
                 ("open", "Waarom was de jaarlijkse overstroming van de Nijl goed nieuws?",
                  "Het water liet een laag vruchtbaar slib achter op de akkers. Die bemesting "
                  "kwam vanzelf, elk jaar opnieuw, zonder dat de boer er iets voor moest doen.", 3),
                 ("open", "Waarom vroeg irrigatielandbouw om samenwerking en bestuur?",
                  "Kanalen graven en onderhouden kan één gezin niet alleen, en het water moet "
                  "eerlijk verdeeld worden. Daar is overleg en gezag voor nodig, en dus bestuur.", 4),
                 ("waar", "Mesopotamië en Egypte lagen allebei aan een rivier.", True),
             ]),

        dict(kop="Het schrift",
             opdracht="Let op welk schrift bij welk rijk hoort.",
             oefeningen=[
                 ("rij", [("Mesopotamië", "spijkerschrift"), ("Egypte", "hiërogliefen")],
                  "Hoe heet het schrift van dit rijk?", WW),
                 ("kort", "Waarop schreven de Mesopotamiërs?", "kleitabletten", W),
                 ("kies", "Waarom werd het schrift in de eerste plaats uitgevonden?",
                  ["om verhalen te bewaren", "om te boekhouden", "om gedichten te schrijven"], 1),
                 ("kort", "Met welke steen werden de hiërogliefen ontcijferd? De Steen van …",
                  "Rosetta", W),
                 ("waar", "In Egypte schreef men met spijkerschrift.", False),
             ]),

        dict(kop="Hoe de samenleving in elkaar zat",
             opdracht="Denk aan de standenmaatschappij en aan wie waar stond.",
             oefeningen=[
                 ("kort", "Hoe noem je een samenleving waarin je plaats vastligt bij je geboorte?",
                  "een standenmaatschappij", WW),
                 ("rij", [("bovenaan in Egypte", "de farao"),
                          ("onderaan in Egypte", "de slaven"),
                          ("hield de administratie bij", "de ambtenaar")],
                  "Wie hoort hier?", WW),
                 ("kort", "Hoe noem je het ruilen van goederen zonder geld?", "ruilhandel", W),
                 ("open", "Waarom kon Mesopotamië niet zonder handel?",
                  "Tussen de rivieren was er wel vruchtbare grond, maar bijna geen steen, hout "
                  "of metaal. Dat moesten ze halen bij anderen, in ruil voor graan en stoffen.", 3),
                 ("open", "Hoe zie je de sociale ongelijkheid terug in de bronnen zelf?",
                  "Graven van rijken zitten vol kostbaarheden, die van gewone mensen bijna niet. "
                  "Wetten straffen dezelfde daad zwaarder naargelang de stand van het slachtoffer.", 4),
             ]),

        dict(kop="Geloof en de farao",
             opdracht="Antwoord in volle zinnen waar dat gevraagd wordt.",
             oefeningen=[
                 ("kort", "Hoe heet de trapvormige tempeltoren van een Mesopotamische stad?",
                  "ziggurat", W),
                 ("open", "Waarom mummificeerden de Egyptenaren hun doden?",
                  "Ze geloofden in een leven na de dood, waarvoor het lichaam bewaard moest "
                  "blijven. Zonder lichaam kon de ziel niet terugkeren.", 3),
                 ("kies", "Waarom is het graf van Toetanchamon zo beroemd, hoewel hij geen "
                          "belangrijke farao was?",
                  ["hij regeerde het langst", "zijn graf was nooit leeggeroofd",
                   "hij liet de piramides bouwen"], 1),
                 ("open", "Noem twee taken van een farao.",
                  "Hij bestuurde het land en gaf de wetten, hij voerde het leger aan, hij was "
                  "hogepriester en moest de goden gunstig stemmen, en hij liet de irrigatie "
                  "en de bouwwerken organiseren.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-oude-griekenland-spark"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het oude Griekenland",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Stadstaten",
             opdracht="Let op het verschil tussen één rijk en veel losse staten.",
             oefeningen=[
                 ("kort", "Hoe noemde men een Griekse stadstaat?", "een polis", W),
                 ("open", "Griekenland zit vol bergen en eilanden. Leg uit waarom daar veel "
                          "aparte stadstaten ontstonden in plaats van één groot rijk.",
                  "De bergen en de zee sneden de streken van elkaar af. Reizen en besturen "
                  "over die afstand was lastig, dus elke vlakte of elk eiland regelde zijn "
                  "eigen zaken.", 4),
                 ("open", "Wat deelden de Griekse stadstaten dan wél met elkaar?",
                  "Dezelfde taal, dezelfde goden en mythen, en gezamenlijke feesten zoals de "
                  "Olympische Spelen.", 3),
                 ("waar", "Alle Griekse stadstaten werden samen door één koning bestuurd.", False),
             ]),

        dict(kop="Besturen in Athene",
             opdracht="Zet de bestuursvormen in de juiste volgorde en let op wie mocht stemmen.",
             oefeningen=[
                 ("rij", [("een kleine groep rijken beslist", "oligarchie"),
                          ("één man grijpt de macht", "tirannie"),
                          ("de burgers beslissen zelf", "democratie")],
                  "Hoe heet deze bestuursvorm?", WW),
                 ("kies", "Wie mocht er in Athene meestemmen?",
                  ["alle inwoners", "enkel vrije mannen met Atheense ouders",
                   "alle mannen en vrouwen", "enkel de rijksten"], 1),
                 ("open", "Noem drie groepen die in Athene niét mochten stemmen.",
                  "Vrouwen, slaven en vreemdelingen (metoiken). Kinderen evenmin.", 3),
                 ("waar", "Athene was een directe democratie: burgers stemden zelf, niet via "
                          "verkozenen.", True),
             ]),

        dict(kop="Athene en Sparta",
             opdracht="Vergelijk de twee steden op elk punt.",
             oefeningen=[
                 ("rij", [("leidde jongens vanaf hun zevende op tot soldaat", "Sparta"),
                          ("bouwde het Parthenon op de Akropolis", "Athene"),
                          ("liet vrouwen sporten en bezit hebben", "Sparta"),
                          ("leefde van landbouw in het binnenland", "Sparta")],
                  "Athene of Sparta?", WW),
                 ("kort", "Hoe noemde men de onvrije landbouwers van Sparta?", "heloten", W),
                 ("open", "Wat mocht een Spartaanse vrouw wél en een Atheense niet?",
                  "Sporten en zich buitenshuis vertonen, en grond of bezit hebben. Een Atheense "
                  "vrouw bleef grotendeels binnen en stond haar leven lang onder een voogd.", 3),
             ]),

        dict(kop="Oorlog en kolonisatie",
             opdracht="Let op wie tegen wie vocht, en wat erna kwam.",
             oefeningen=[
                 ("rij", [("de Perzische oorlogen", "de Grieken tegen de Perzen"),
                          ("de Peloponnesische oorlog", "Athene tegen Sparta")],
                  "Wie vocht hier tegen wie?", WW),
                 ("kies", "Wat was het gevolg van de Peloponnesische oorlog?",
                  ["Athene werd nog machtiger", "de Griekse stadstaten raakten verzwakt",
                   "de Perzen veroverden Griekenland"], 1),
                 ("open", "Waarom trokken Grieken weg om kolonies te stichten?",
                  "Er was te weinig vruchtbare grond voor de groeiende bevolking, en handel "
                  "over zee leverde op. Zo ontstonden Griekse steden rond de hele "
                  "Middellandse Zee en de Zwarte Zee.", 4),
             ]),

        dict(kop="Denkers, kunst en Alexander",
             opdracht="Vul de namen en begrippen aan.",
             oefeningen=[
                 ("rij", [("leraar van Plato", "Socrates"), ("leerling van Plato", "Aristoteles"),
                          ("dichter van de Ilias en de Odyssee", "Homeros")],
                  "Over wie gaat het?", WW),
                 ("kort", "Hoe noem je de vermenging van Griekse en oosterse cultuur na "
                          "Alexander de Grote?", "hellenisme", W),
                 ("open", "Waarom noemt men de Grieken het begin van de wetenschap?",
                  "Ze zochten verklaringen in de natuur zelf in plaats van bij de goden, en ze "
                  "gaven redeneringen en bewijzen waar anderen op verder konden werken.", 4),
                 ("open", "Wat is het verschil tussen archaïsche en klassieke Griekse beelden?",
                  "Archaïsche beelden staan stijf en recht, met een vaste glimlach. Klassieke "
                  "beelden staan in evenwicht op één been, met natuurlijke spieren en plooien.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-romeinse-rijk-spark"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Het Romeinse Rijk",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van koningen naar republiek",
             opdracht="Let op de volgorde van de drie bestuursvormen.",
             oefeningen=[
                 ("kort", "Aan welke rivier ontstond Rome?", "de Tiber", W),
                 ("rij", [("de koningstijd", "1"), ("het keizerrijk", "3"), ("de republiek", "2")],
                  "Zet deze drie in volgorde: schrijf 1, 2 of 3.", WW),
                 ("kort", "Hoe noem je een staat zonder koning, met verkozen bestuurders?",
                  "een republiek", W),
                 ("open", "Waarom koos de republiek voor twee consuls, elk voor één jaar?",
                  "Zo kon niemand alleen beslissen en kon niemand de macht lang vasthouden. "
                  "De twee konden elkaar tegenhouden, en na een jaar was het voorbij.", 4),
                 ("kies", "Wie waren de patriciërs?",
                  ["de oude adellijke families", "de gewone burgers", "de slaven"], 0),
             ]),

        dict(kop="Van republiek naar keizerrijk",
             opdracht="Denk aan de oorzaken, niet enkel aan wie er aan de macht kwam.",
             oefeningen=[
                 ("kies", "Tegen wie voerde Rome de Punische oorlogen?",
                  ["Carthago", "de Grieken", "de Galliërs", "de Perzen"], 0),
                 ("kort", "Hoe heet een groot Romeins landgoed met slavenarbeid?",
                  "een latifundium", W),
                 ("open", "Welk gevolg hadden de latifundia voor de kleine boer?",
                  "Hij kon niet concurreren met goedkope slavenarbeid, verkocht zijn grond en "
                  "trok arm naar de stad. Zo groeide in Rome een grote massa werklozen.", 4),
                 ("kort", "Hoe noemde Augustus zichzelf, in plaats van koning?",
                  "princeps (de eerste burger)", WW),
                 ("kort", "Welke bekende Romein werd in de senaat vermoord?", "Julius Caesar", W),
             ]),

        dict(kop="De Pax Romana",
             opdracht="Vul aan en leg uit waar dat gevraagd wordt.",
             oefeningen=[
                 ("rij", [("mare nostrum", "onze zee"), ("Pax Romana", "de Romeinse vrede")],
                  "Wat betekent dit?", WW),
                 ("open", "Wat maakte handel over het hele rijk mogelijk tijdens de Pax Romana?",
                  "Eén munt, één taal voor het bestuur, dezelfde wetten, veilige wegen en zeeën "
                  "doordat het leger de rust bewaarde.", 4),
                 ("kort", "Waarmee brachten de Romeinen water tot in hun steden?",
                  "aquaducten", W),
                 ("kort", "Wat was de keizerscultus?",
                  "de keizer als god vereren", WW),
             ]),

        dict(kop="Grieks en Romeins",
             opdracht="Wat namen de Romeinen over, en wat voegden ze toe?",
             oefeningen=[
                 ("rij", [("de boog en het gewelf", "Romeins"), ("de zuilenrij", "Grieks"),
                          ("beton", "Romeins"), ("de goden onder andere namen", "Grieks")],
                  "Grieks of Romeins van oorsprong?", WW),
                 ("open", "Wat valt op aan Romeinse portretbeelden, in vergelijking met Griekse?",
                  "Ze zijn realistisch: rimpels, littekens en een kale kruin blijven staan. "
                  "Grieken maakten hun mensen liever ideaal en jong.", 3),
                 ("waar", "De Romeinen namen veel over van de Griekse cultuur.", True),
             ]),

        dict(kop="Het einde van het rijk",
             opdracht="Noem oorzaken, geen losse gebeurtenissen.",
             oefeningen=[
                 ("open", "Noem drie oorzaken van de crisis van de 3de eeuw.",
                  "Aanvallen aan de grenzen, keizers die elkaar snel opvolgden na staatsgrepen, "
                  "geldontwaarding en zware belastingen, pest en een krimpende handel.", 4),
                 ("kort", "In welk jaar ging het West-Romeinse Rijk ten onder?", "476", W),
                 ("waar", "Het Oost-Romeinse Rijk verdween samen met het West-Romeinse Rijk.", False),
                 ("open", "Waarom geldt 476 als een scharnierpunt?",
                  "Het is de afspraak waarmee historici de klassieke oudheid laten eindigen en "
                  "de middeleeuwen laten beginnen. Niet omdat alles die dag veranderde, maar "
                  "omdat het centrale gezag in het westen toen wegviel.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-bronnen-kunst-en-beeldvorming-spark"] = dict(
    vak="Geschiedenis", niveau=SPARK, titel="Bronnen, kunst en beeldvorming",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Primair of secundair",
             opdracht="Vraag je af of de maker er zelf bij was.",
             oefeningen=[
                 ("rij", [("een brief van een Romeinse soldaat", "primair"),
                          ("je schoolboek over de Romeinen", "secundair"),
                          ("een documentaire uit 2024", "secundair"),
                          ("een dagboek uit 1914", "primair")],
                  "Primaire of secundaire bron?", WW),
                 ("waar", "Je schoolboek over de Romeinen is een primaire bron.", False),
                 ("open", "Leg in je eigen woorden uit wat een primaire bron is.",
                  "Een bron die gemaakt is in de tijd zelf, door iemand die erbij was of er "
                  "dichtbij stond.", 3),
             ]),

        dict(kop="De vorm van een bron",
             opdracht="Geschreven, materieel, beeldend of mondeling?",
             oefeningen=[
                 ("rij", [("een potscherf uit een opgraving", "materieel"),
                          ("een opgenomen gesprek met een oorlogsgetuige", "mondeling"),
                          ("een middeleeuws schilderij", "beeldend"),
                          ("een wetstekst op een kleitablet", "geschreven")],
                  "Welke soort bron is dit?", WW),
                 ("kort", "Hoe noem je iemand die een gebeurtenis met eigen ogen zag?",
                  "een ooggetuige", W),
                 ("open", "Wat is het verschil tussen een ooggetuige en een tijdgenoot?",
                  "Een ooggetuige heeft het zelf gezien. Een tijdgenoot leefde in dezelfde tijd "
                  "maar was er niet noodzakelijk bij.", 3),
             ]),

        dict(kop="Bruikbaar en betrouwbaar",
             opdracht="Dat zijn twee verschillende vragen. Hou ze uit elkaar.",
             oefeningen=[
                 ("open", "Wanneer is een bron onbruikbaar, ook al klopt alles wat erin staat?",
                  "Als ze niets zegt over de vraag die je onderzoekt. Een correcte prijslijst "
                  "helpt je niet als je wil weten hoe een veldslag verliep.", 3),
                 ("waar", "Een onbetrouwbare bron is waardeloos voor een historicus.", False),
                 ("open", "Waarom kan een bron die overduidelijk overdrijft, toch nuttig zijn?",
                  "De overdrijving zelf is informatie: ze toont wat de maker wilde uitstralen, "
                  "aan wie, en wat er in die tijd indruk maakte.", 4),
             ]),

        dict(kop="Standplaatsgebondenheid",
             opdracht="Denk aan wie het zegt en van waaruit.",
             oefeningen=[
                 ("kort", "Hoe noem je het feit dat iedereen vanuit zijn eigen plaats en tijd "
                          "kijkt? Eén woord.", "standplaatsgebondenheid", WW),
                 ("open", "Herodotos noemt de Perzen 'barbaren'. Wat bedoelde hij daar precies "
                          "mee, en wat leert dat woord ons over hem?",
                  "Barbaros betekende bij de Grieken: iemand die geen Grieks spreekt, wiens taal "
                  "klinkt als 'bar bar'. Het woord zegt dus vooral dat Herodotos vanuit het "
                  "Griekse standpunt schreef en de eigen taal als maatstaf nam.", 5),
                 ("open", "Na de slag bij Kadesj claimden zowel Ramses als de Hettieten de "
                          "overwinning. Wat leer je daaruit als historicus?",
                  "Dat één bron nooit volstaat. Elke partij vertelt het verhaal dat haar past, "
                  "dus je legt bronnen naast elkaar en zoekt waar ze elkaar tegenspreken.", 4),
                 ("waar", "Wie een bron betaalt, kan invloed hebben op wat erin komt te staan.", True),
             ]),

        dict(kop="Redeneren als een historicus",
             opdracht="Gebruik de namen van de redeneerwijzen uit de bundel.",
             oefeningen=[
                 ("rij", [("je vergelijkt wat bleef met wat veranderde", "continuïteit en verandering"),
                          ("je bekijkt dezelfde gebeurtenis vanuit twee partijen", "meerdere perspectieven"),
                          ("je onderbouwt je uitspraak met bronnen", "bewijs gebruiken")],
                  "Welke redeneerwijze is dit?", WW),
                 ("kort", "Hoe noem je het ontstaan van een verhaal dat mooier is dan de feiten?",
                  "mythevorming", W),
                 ("open", "Het beeld dat historici van de neanderthalers hebben, is veranderd. "
                          "Leg uit hoe zo'n beeld kan verschuiven.",
                  "Door nieuwe vondsten en nieuwe technieken. Uit graven, werktuigen, sieraden "
                  "en dna bleek dat neanderthalers hun doden begroeven, gereedschap maakten en "
                  "zich met onze voorouders vermengden. Het oude beeld van een domme holbewoner "
                  "hield geen stand.", 5),
                 ("open", "Wat is het verschil tussen het verleden en de geschiedenis?",
                  "Het verleden is alles wat gebeurd is. Geschiedenis is het verhaal dat "
                  "historici daarover vertellen op basis van bronnen.", 3),
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

UITLEGBLADEN["oefenbundel-historisch-referentiekader-spark"] = dict(
    reeksen=[
        dict(aanpak="Tel bij de eerste cijfers van het jaartal één op om de eeuw te vinden, behalve bij "
                    "een jaar dat op 00 eindigt: dat hoort nog bij de eeuw ervoor.",
             waarom=[
                 "1066 wordt de 11de eeuw (10 plus 1), maar 1600 blijft de 16de, want een jaar op 00 "
                 "sluit zijn eeuw af.",
                 "Een eeuw loopt van 01 tot en met 00. De 15de eeuw begint dus in 1401 en eindigt in "
                 "1500.",
                 None,
                 None,
             ]),
        dict(aanpak="Vóór Christus tellen de jaartallen achterwaarts: hoe groter het getal, hoe langer "
                    "geleden. Ga je van v.C. naar n.C., tel dan de twee getallen op en trek er één af, "
                    "want er is geen jaar 0.",
             waarom=[
                 None,
                 "Van 753 v.C. tot 476 n.C. is 753 plus 476, min 1 voor het ontbrekende jaar 0, dus "
                 "1 229. Twee jaartallen aan dezelfde kant trek je gewoon af: 3300 min 800 is 2 500.",
                 None,
                 None,
             ]),
        dict(aanpak="Leer de zeven periodes als een ketting, en hang aan elke overgang zijn "
                    "scharnierpunt: het schrift, de val van Rome, de ontdekkingsreizen, 1789 en 1945.",
             waarom=[
                 None,
                 None,
                 None,
                 "De prehistorie beslaat het grootste deel van de menselijke geschiedenis: "
                 "honderdduizenden jaren, tegenover enkele duizenden voor alle andere periodes samen.",
             ]),
        dict(aanpak="Kijk naar het tempo van de verandering, niet naar hoe groot het gevolg was. Een "
                    "revolutie gaat snel en met een breuk, een evolutie traag en geleidelijk.",
             waarom=[
                 "De overgang naar landbouw duurde duizenden jaren, en dat is een evolutie. Maar de "
                 "gevolgen waren zo groot dat historici ook van een revolutie spreken. Daarom kunnen "
                 "de twee hier samengaan.",
                 None,
                 "Een scharnierpunt is een afspraak die uit de Europese geschiedenis komt. In 476 viel "
                 "Rome, maar in China of Midden-Amerika veranderde er op dat moment niets.",
                 None,
             ]),
        dict(aanpak="Vraag je af waar de gebeurtenis over gaat: macht (politiek), geld en werk "
                    "(economisch), de groepen in de samenleving (sociaal), of geloof, kunst en denken "
                    "(cultureel). Soms past er meer dan één.",
             waarom=[
                 None,
                 "Een senator is een machtsfiguur, en dat is politiek. Een bronzen beeld is kunst, en "
                 "dat is cultureel. Daarom hoort dit voorwerp in twee domeinen tegelijk.",
                 None,
                 None,
             ]),
        dict(aanpak="Structuurbegrippen komen in paren: stedelijk tegenover ruraal, statisch tegenover "
                    "dynamisch. Zoek telkens welke kant van het paar past.",
             waarom=[None, None, None]),
    ],
)

UITLEGBLADEN["oefenbundel-prehistorie-spark"] = dict(
    reeksen=[
        dict(aanpak="Hang elke naam aan wat ze betekent: habilis is handig, erectus staat rechtop, "
                    "sapiens is wijs. Zo onthoud je meteen ook de volgorde.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "De Homo erectus verliet Afrika al veel eerder. De Homo sapiens kwam later, en trof "
                 "onderweg andere mensachtigen aan, zoals de neanderthaler.",
             ]),
        dict(aanpak="Vraag je bij elke oefening af wat je niet kon bewaren, en wat dat betekende voor "
                    "je leven. Bijna alles volgt uit het feit dat eten niet lang goed bleef.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "Verzamelen leverde het grootste deel van het eten: noten, vruchten, wortels, eieren. "
                 "Jagen lukte lang niet elke dag.",
                 None,
             ]),
        dict(aanpak="Hou de oorzaak en het gevolg uit elkaar: de landbouw is de oorzaak, de vaste "
                    "woonplaats en het overschot zijn het gevolg.",
             waarom=[
                 None,
                 None,
                 None,
                 "De Vruchtbare Halvemaan loopt van Mesopotamië tot de Middellandse Zee. Daar groeiden "
                 "de wilde granen en leefden de dieren die zich lieten temmen.",
                 "De landbouw ontstond op verschillende plaatsen los van elkaar, duizenden jaren uit "
                 "elkaar: in het nabije oosten, in China, in Midden-Amerika.",
             ]),
        dict(aanpak="Volg de ketting: eerst een overschot, dan een vaste woonplaats, dan specialisatie, "
                    "en pas dan een stad. Elke schakel maakt de volgende mogelijk.",
             waarom=[
                 "Lees de ketting als een gevolg: pas als er een overschot is, kan iemand ophouden met "
                 "boeren, en pas dan kan er een stad ontstaan.",
                 None,
                 None,
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-mesopotamie-en-egypte-spark"] = dict(
    reeksen=[
        dict(aanpak="Beide beschavingen draaien om één ding: water op de juiste plaats. Vraag je bij "
                    "elke oefening af wat de rivier gaf, en wat ze van de mensen vroeg.",
             waarom=[
                 "Meso is Grieks voor tussen en potamos voor rivier. De naam zegt dus letterlijk waar "
                 "het gebied lag.",
                 None,
                 None,
                 None,
                 None,
             ]),
        dict(aanpak="Hou de twee schriften uit elkaar: spijkerschrift in Mesopotamië, in natte klei "
                    "gedrukt, en hiërogliefen in Egypte, in steen gehakt en op papyrus geschilderd.",
             waarom=[
                 None,
                 None,
                 "De oudste kleitabletten zijn lijsten: zoveel zakken graan, zoveel schapen. Het schrift "
                 "is ontstaan uit boekhouding, niet uit verhalen.",
                 "Op de Steen van Rosetta staat dezelfde tekst in drie schriften. Omdat men het Grieks "
                 "kon lezen, kon men de hiërogliefen ernaast ontcijferen.",
                 None,
             ]),
        dict(aanpak="In een standenmaatschappij ligt je plaats vast bij je geboorte. Kijk bij elke "
                    "oefening naar wie bovenaan stond, wie onderaan, en wie ertussen.",
             waarom=[
                 None,
                 None,
                 "Ruilhandel werkt zolang allebei de partijen willen wat de ander heeft. Daarom kwam er "
                 "later geld: dat aanvaardt iedereen.",
                 None,
                 None,
             ]),
        dict(aanpak="Geloof en bestuur liepen door elkaar: de farao was tegelijk koning en priester. "
                    "Vraag je bij elke oefening af welke van die twee rollen meespeelt.",
             waarom=[
                 None,
                 None,
                 "Bijna alle andere koningsgraven waren in de oudheid al leeggeroofd. Dat van "
                 "Toetanchamon bleef bij toeval gespaard, en daardoor weten we hoe zo'n graf er echt "
                 "uitzag.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-oude-griekenland-spark"] = dict(
    reeksen=[
        dict(aanpak="Denk bij Griekenland eerst aan het landschap: bergen en zee die alles van elkaar "
                    "scheiden. Bijna elke oefening in deze reeks volgt daaruit.",
             waarom=[
                 None,
                 None,
                 None,
                 "Er was geen gezamenlijk bestuur. Wat de Grieken deelde, was hun taal, hun goden en "
                 "hun feesten, niet één koning.",
             ]),
        dict(aanpak="Zet de bestuursvormen naast elkaar met één vraag: hoeveel mensen beslissen er? "
                    "Eén (tirannie), enkelen (oligarchie), of de burgers samen (democratie).",
             waarom=[
                 None,
                 "Burger zijn was in Athene eng bepaald: vrij, man, volwassen, en uit Atheense ouders. "
                 "Dat was maar een klein deel van de inwoners.",
                 None,
                 "Een Atheense burger stemde zelf, op de volksvergadering. Wij kiezen mensen die voor "
                 "ons stemmen, en dat heet een indirecte democratie.",
             ]),
        dict(aanpak="Vergelijk de twee steden punt voor punt: Athene is zee, handel en kunst, Sparta is "
                    "land, leger en tucht. Bij de vrouwen draait het net om: in Sparta hadden ze meer "
                    "vrijheid.",
             waarom=[None, None, None]),
        dict(aanpak="Hou de twee oorlogen uit elkaar: de Perzische oorlogen zijn de Grieken tegen een "
                    "vijand van buiten, de Peloponnesische oorlog is de Grieken onder elkaar.",
             waarom=[
                 None,
                 "Na die oorlog waren alle stadstaten uitgeput. Daardoor kon Macedonië, onder Filippus "
                 "en Alexander, hen kort daarna onderwerpen.",
                 None,
             ]),
        dict(aanpak="Onthoud de keten van leraren: Socrates leerde Plato, Plato leerde Aristoteles, en "
                    "Aristoteles was de leraar van Alexander de Grote.",
             waarom=[
                 None,
                 "Hellas is de Griekse naam voor Griekenland. Na Alexander verspreidde de Griekse taal "
                 "en cultuur zich tot in Egypte en Perzië, vermengd met wat daar al leefde.",
                 None,
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-romeinse-rijk-spark"] = dict(
    reeksen=[
        dict(aanpak="Rome doorloopt drie bestuursvormen, in deze volgorde: koningstijd, republiek, "
                    "keizerrijk. Hang aan elk één woord: koning, consuls, keizer.",
             waarom=[
                 None,
                 None,
                 None,
                 None,
                 "De patriciërs waren de oude adellijke families, de plebejers de gewone burgers. De "
                 "strijd tussen die twee groepen loopt door de hele republiek.",
             ]),
        dict(aanpak="Zoek bij elke oefening de oorzaak achter de gebeurtenis. De republiek viel niet "
                    "door één man, maar door veroveringen die de samenleving van binnenuit veranderden.",
             waarom=[
                 "Carthago lag in Noord-Afrika en was Romes grote tegenstander op zee. Na drie oorlogen "
                 "werd de stad vernietigd.",
                 None,
                 None,
                 "Augustus vermeed met opzet het woord koning: dat lag in Rome gevoelig sinds de "
                 "koningstijd. Hij hield de vormen van de republiek in stand en had ondertussen alle "
                 "macht.",
                 None,
             ]),
        dict(aanpak="Pax Romana betekent de Romeinse vrede: ruim twee eeuwen zonder grote oorlog binnen "
                    "het rijk. Vraag je af wat die rust mogelijk maakte, en wat ze opleverde.",
             waarom=[
                 None,
                 None,
                 None,
                 "De keizer vereren was vooral een manier om je trouw aan het rijk te tonen. Wie "
                 "weigerde, zoals de christenen, kreeg daardoor problemen.",
             ]),
        dict(aanpak="De Romeinen namen veel over van de Grieken, maar waren zelf sterk in techniek: de "
                    "boog, het gewelf en beton zijn van hen.",
             waarom=[None, None, None]),
        dict(aanpak="Noem oorzaken, geen losse gebeurtenissen. Het rijk viel door een optelsom: druk "
                    "aan de grenzen, chaos in het bestuur, en een economie die het niet meer droeg.",
             waarom=[
                 None,
                 None,
                 "Het Oost-Romeinse Rijk, met Constantinopel als hoofdstad, bleef nog bijna duizend "
                 "jaar bestaan, tot 1453.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-bronnen-kunst-en-beeldvorming-spark"] = dict(
    reeksen=[
        dict(aanpak="Eén vraag volstaat: is de bron gemaakt in de tijd zelf, of kijkt ze erop terug? "
                    "Het gaat niet om hoe oud de bron is, maar om wanneer ze gemaakt werd tegenover wat "
                    "ze beschrijft.",
             waarom=[
                 None,
                 "Een schoolboek van vandaag over de Romeinen kijkt tweeduizend jaar terug, dus "
                 "secundair. Een documentaire van 2024 ook, ook al staan er echte voorwerpen in beeld.",
                 None,
             ]),
        dict(aanpak="De vorm van een bron is iets anders dan primair of secundair. Vraag je af hoe ze "
                    "tot je komt: geschreven, materieel (een voorwerp), beeldend (een beeld of een "
                    "schilderij) of mondeling (verteld).",
             waarom=[None, None, None]),
        dict(aanpak="Dit zijn twee verschillende vragen. Bruikbaar: helpt deze bron mij bij mijn vraag? "
                    "Betrouwbaar: klopt wat erin staat? Een bron kan het ene zijn zonder het andere.",
             waarom=[
                 None,
                 "Ook een leugen is informatie: ze toont wat iemand wilde doen geloven, en aan wie. Je "
                 "gebruikt zo'n bron dan voor een andere vraag dan je eerst had.",
                 None,
             ]),
        dict(aanpak="Vraag je bij elke bron af wie het zegt, van waaruit, en aan wie. Niemand kijkt van "
                    "nergens.",
             waarom=[
                 None,
                 None,
                 None,
                 "Wie een standbeeld of een kroniek betaalde, bepaalde vaak mee wat erin kwam. Dat "
                 "maakt de bron niet waardeloos, maar je leest ze met die opdrachtgever in gedachten.",
             ]),
        dict(aanpak="De redeneerwijzen zijn gereedschap. Vraag je bij elke vraag af welk stuk "
                    "gereedschap ze van je vraagt: vergelijken in de tijd, verschillende partijen naast "
                    "elkaar leggen, of je uitspraak met bronnen onderbouwen.",
             waarom=[
                 None,
                 None,
                 None,
                 "Het verleden is voorbij en verandert niet meer. Geschiedenis verandert wel, want ze "
                 "wordt geschreven met de bronnen en de vragen van vandaag.",
             ]),
    ],
)
