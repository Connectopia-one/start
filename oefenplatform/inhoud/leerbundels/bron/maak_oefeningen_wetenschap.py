# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij de hoofdstukken van wetenschap en techniek 🌱 Start.

Waar de leerbundel de theorie geeft, geeft een oefenbundel oefeningen om op
papier te maken, met achteraan een antwoordblad dat je eraf scheurt.

De oefeningen zijn met opzet ándere vragen dan die van het hoofdstuk op het
scherm. Dezelfde leerstof, maar een andere richting en andere voorbeelden:
waar het scherm laat kiezen uit vier antwoorden, laat de bundel uitleggen,
sorteren of tekenen. Wie hier iets bijschrijft, legt het eerst naast
`../../start/wetenschap-en-techniek.json`.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

W = "120px"
WW = "180px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een tekenopdracht telt het idee, niet hoe mooi je kan tekenen.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-biologie-leven-en-ecologie"] = dict(
    vak="Wetenschap en techniek", titel="Biologie: leven en ecologie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Dieren sorteren",
             opdracht="Schrijf bij elk dier tot welke groep het hoort.",
             oefeningen=[
                 ("rij", [("kikker", "amfibie"), ("forel", "vis"), ("uil", "vogel"),
                          ("adder", "reptiel"), ("vleermuis", "zoogdier"), ("mier", "insect")],
                  "Tot welke groep hoort het dier?", WW),
                 ("rij", [("koe", "planteneter"), ("vos", "alleseter"),
                          ("leeuw", "vleeseter"), ("konijn", "planteneter")],
                  "Planteneter, vleeseter of alleseter?", WW),
                 ("open", "Noem twee verschillen tussen een insect en een spin.",
                  "Een insect heeft zes poten, een spin acht. Een insect heeft drie "
                  "lichaamsdelen en voelsprieten, een spin twee delen en geen voelsprieten. "
                  "Veel insecten hebben vleugels, spinnen nooit.", 3),
                 ("waar", "Een dier met een ruggengraat noem je een gewerveld dier.", True),
             ]),

        dict(kop="De plant",
             opdracht="Elk deel van een plant heeft zijn eigen taak.",
             oefeningen=[
                 ("rij", [("neemt water op uit de grond", "de wortel"),
                          ("maakt suiker met licht", "het blad"),
                          ("draagt de bladeren omhoog", "de stengel"),
                          ("lokt insecten", "de bloem")],
                  "Welk deel van de plant doet dat?", WW),
                 ("open", "Een plant staat een week in een donkere kast, mét water. Wat gebeurt "
                          "er met haar bladeren, en waarom?",
                  "Ze worden geel en slap. Zonder licht kan de plant geen fotosynthese doen, "
                  "dus maakt ze geen suiker meer en heeft ze geen voedsel.", 3),
                 ("kies", "Welk gas nemen planten op bij de fotosynthese?",
                  ["zuurstof", "koolstofdioxide", "stikstof", "waterstof"], 1),
             ]),

        dict(kop="Wie eet wie?",
             opdracht="Een pijl in een voedselketen wijst naar wie eet.",
             oefeningen=[
                 ("teken", "Teken een voedselketen van drie schakels die begint bij gras. "
                           "Zet er pijlen bij.",
                  "Bijvoorbeeld: gras → konijn → vos. De pijl wijst telkens naar wie eet.", 42),
                 ("open", "Wat doen afbrekers zoals schimmels en pissebedden in een bos?",
                  "Ze breken dood materiaal af, zoals bladeren en dood hout, zodat de "
                  "voedingsstoffen terug in de grond komen en planten er weer van kunnen leven.", 3),
                 ("open", "In een vijver verdwijnen plots alle waterplanten. Wat gebeurt er "
                          "daarna met de dieren die er leven?",
                  "De planteneters vinden geen voedsel meer en verdwijnen, en daarna ook de "
                  "dieren die van hén leefden. Er komt ook minder zuurstof in het water.", 3),
                 ("waar", "Als er in een gebied meer soorten leven, kan de natuur een tegenslag "
                          "beter opvangen.", True),
             ]),

        dict(kop="Overleven door het jaar",
             opdracht="Dieren en planten hebben elk hun eigen manier.",
             oefeningen=[
                 ("rij", [("egel", "winterslaap"), ("zwaluw", "trekt naar het zuiden"),
                          ("eik", "verliest zijn bladeren"), ("ree", "krijgt een dikkere vacht")],
                  "Hoe komt dit door de winter?", WW),
                 ("open", "Wat is camouflage, en waarvoor dient het bij een dier?",
                  "Een kleur of vorm waardoor een dier opgaat in zijn omgeving. Zo wordt het "
                  "minder snel gezien door een vijand, of kan het zelf ongemerkt jagen.", 3),
                 ("open", "Je legt achteraan in de tuin een hoop dode takken. Welke dieren help "
                          "je daarmee, en waarom?",
                  "Bijvoorbeeld egels, insecten, pissebedden, spinnen en vogels: ze vinden er "
                  "een schuilplaats en voedsel.", 3),
                 ("kies", "Hoe verspreidt een paardenbloem haar zaden?",
                  ["met de wind", "met water", "door dieren op te eten",
                   "door ze in de grond te stoppen"], 0),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biologie-het-menselijk-lichaam"] = dict(
    vak="Wetenschap en techniek", titel="Biologie: het menselijk lichaam",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Organen en hun taak",
             opdracht="Schrijf het orgaan dat dit doet.",
             oefeningen=[
                 ("rij", [("filtert afvalstoffen uit het bloed", "de nieren"),
                          ("pompt het bloed rond", "het hart"),
                          ("neemt zuurstof op uit de lucht", "de longen"),
                          ("maakt gal en ruimt gif op", "de lever")],
                  "Welk orgaan is het?", WW),
                 ("open", "Schrijf de weg van een boterham door je lichaam op, in vier stappen.",
                  "Mond (kauwen en speeksel) → slokdarm → maag → dunne darm (opname in het "
                  "bloed) → dikke darm (water eruit) → wat overblijft gaat naar buiten.", 3),
                 ("waar", "In de dunne darm gaan de voedingsstoffen naar het bloed.", True),
             ]),

        dict(kop="Bloed en ademen",
             opdracht="Denk aan wat er heen gaat en wat er terugkomt.",
             oefeningen=[
                 ("rij", [("voeren zuurstof aan", "de rode bloedcellen"),
                          ("bestrijden ziektekiemen", "de witte bloedcellen"),
                          ("voert bloed wég van het hart", "de slagader"),
                          ("voert bloed náár het hart", "de ader")],
                  "Wat of wie doet dat?", WW),
                 ("open", "Je loopt hard. Waarom klopt je hart dan sneller?",
                  "Je spieren werken harder en hebben meer zuurstof en voedingsstoffen nodig. "
                  "Het hart pompt daarom sneller om dat sneller aan te voeren.", 3),
                 ("open", "Waarom is het beter om door je neus te ademen dan door je mond?",
                  "In je neus wordt de lucht opgewarmd, bevochtigd en gefilterd door haartjes "
                  "en slijm, zodat er minder stof en kiemen in je longen komen.", 3),
                 ("waar", "In de longblaasjes wordt zuurstof opgenomen en koolstofdioxide "
                          "afgegeven.", True),
             ]),

        dict(kop="Botten en spieren",
             opdracht="Denk aan wat beweegt en wat beschermt.",
             oefeningen=[
                 ("rij", [("beschermt de hersenen", "de schedel"),
                          ("beschermt het hart en de longen", "de ribben"),
                          ("beschermt het ruggenmerg", "de wervelkolom"),
                          ("maakt een spier vast aan een bot", "de pees")],
                  "Welk deel is het?", WW),
                 ("open", "Waarom werken de biceps en de triceps in je arm als een paar? "
                          "Leg het uit.",
                  "Een spier kan alleen trekken, niet duwen. De biceps buigt de arm, de triceps "
                  "strekt hem weer. Daarom zijn er altijd twee nodig.", 3),
                 ("kies", "Welke spier werkt zonder dat je eraan moet denken?",
                  ["de kuitspier", "de hartspier", "de biceps", "de kauwspier"], 1),
             ]),

        dict(kop="Zintuigen, ziek en gezond",
             opdracht="Nog een laatste reeks.",
             oefeningen=[
                 ("open", "Je komt uit een donkere kamer in fel zonlicht. Wat doen je pupillen, "
                          "en waarom?",
                  "Ze worden kleiner, zodat er minder licht binnenvalt en je netvlies niet "
                  "beschadigd raakt.", 3),
                 ("open", "Je raakt per ongeluk een hete pan aan en trekt je hand weg vóór je "
                          "het beseft. Hoe kan dat?",
                  "Het signaal gaat naar je ruggenmerg en dat stuurt meteen een bevel terug "
                  "naar je spieren. Die korte weg heet een reflex; je hersenen merken het "
                  "pas daarna.", 3),
                 ("rij", [("bacterie", "leeft zelf, soms te doden met een antibioticum"),
                          ("virus", "heeft een cel nodig om zich te vermenigvuldigen")],
                  "Schrijf er kort bij wat het is.", WW),
                 ("waar", "Zweten koelt je lichaam af.", True),
                 ("open", "Waarom is het belangrijk om gevarieerd te eten? Geef twee redenen.",
                  "Elk voedingsmiddel bevat andere voedingsstoffen en vitaminen. Door "
                  "gevarieerd te eten krijg je alles binnen wat je lichaam nodig heeft, "
                  "en niet te veel van één ding.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemie-stoffen-en-mengsels"] = dict(
    vak="Wetenschap en techniek", titel="Chemie: stoffen en mengsels",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vast, vloeibaar en gas",
             opdracht="Denk telkens aan wat er met de warmte gebeurt.",
             oefeningen=[
                 ("rij", [("van vast naar vloeibaar", "smelten"),
                          ("van vloeibaar naar gas", "verdampen"),
                          ("van gas naar vloeibaar", "condenseren"),
                          ("van vloeibaar naar vast", "stollen of bevriezen")],
                  "Hoe noem je die overgang?", WW),
                 ("open", "Je zet een koud blikje op tafel. Na een tijd staan er druppels op. "
                          "Waar komt dat water vandaan?",
                  "Uit de lucht. Waterdamp in de lucht koelt af tegen het koude blikje en "
                  "wordt weer vloeibaar water. Dat heet condenseren.", 3),
                 ("waar", "Water zet uit als het bevriest, daarom drijft ijs.", True),
                 ("open", "Waarom mag je een volle glazen fles water niet in de diepvries "
                          "zetten?",
                  "Water zet uit als het bevriest. De fles kan daardoor barsten.", 2),
             ]),

        dict(kop="Mengen en scheiden",
             opdracht="Hoe haal je de twee stoffen weer uit elkaar?",
             oefeningen=[
                 ("rij", [("zand uit water", "filteren"), ("zout uit zeewater", "laten verdampen"),
                          ("ijzervijlsel uit zand", "met een magneet"),
                          ("olie van water", "laten scheiden en afgieten")],
                  "Hoe scheid je dit?", WW),
                 ("open", "Je roert suiker in water tot er onderaan suiker blijft liggen. "
                          "Wat betekent dat, en wat kan je doen om toch alles op te lossen?",
                  "De oplossing is verzadigd: er kan niet meer suiker bij. Je kan het water "
                  "opwarmen of er meer water bij doen.", 3),
                 ("open", "Je lost 20 gram zout op in 200 gram water. Hoeveel weegt het "
                          "geheel? Leg erbij uit waarom.",
                  "220 gram. Bij het oplossen verdwijnt er niets; de stof zit alleen verspreid "
                  "tussen het water.", 3),
                 ("kies", "Welke van deze is géén mengsel?",
                  ["zeewater", "lucht", "zuiver water", "fruitsap met vruchtvlees"], 2),
             ]),

        dict(kop="Zuur en base",
             opdracht="Denk aan de schaal van 0 tot 14.",
             oefeningen=[
                 ("rij", [("citroensap", "zuur"), ("zuiver water", "neutraal"),
                          ("zeep", "base"), ("azijn", "zuur")],
                  "Zuur, neutraal of base?", W),
                 ("open", "Rodekoolsap wordt rood in de ene beker en groen in de andere. "
                          "Wat weet je dan over die twee vloeistoffen?",
                  "De rode is zuur, de groene is een base. Rodekoolsap verkleurt volgens de "
                  "zuurtegraad en werkt dus als indicator.", 3),
                 ("waar", "Een pH van 7 betekent dat een stof neutraal is.", True),
             ]),

        dict(kop="Branden en veiligheid",
             opdracht="Bij vuur is veiligheid geen bijzaak.",
             oefeningen=[
                 ("open", "Noem de drie dingen die je samen nodig hebt om iets te laten branden.",
                  "Brandstof, zuurstof en warmte (een ontstekingsbron). Valt er één weg, dan "
                  "dooft het vuur.", 2),
                 ("open", "Je zet een omgekeerd glas over een brandende kaars. Wat gebeurt er, "
                          "en waarom?",
                  "De kaars dooft. De zuurstof onder het glas raakt op, en zonder zuurstof kan "
                  "er niets branden.", 3),
                 ("waar", "Brandend frituurvet blus je met water.", False),
                 ("open", "Je vindt thuis een fles met een doodshoofd op het etiket. Wat doe je?",
                  "Je laat ze staan, raakt ze niet aan en zegt het tegen een volwassene. "
                  "Het teken betekent dat de stof giftig is.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-natuurkunde-energie-en-krachten"] = dict(
    vak="Wetenschap en techniek", titel="Natuurkunde: energie en krachten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Krachten om je heen",
             opdracht="Een kracht kan iets doen bewegen, stoppen of van vorm veranderen.",
             oefeningen=[
                 ("rij", [("een appel valt van de boom", "de zwaartekracht"),
                          ("een fiets komt tot stilstand", "de wrijving"),
                          ("een boot blijft drijven", "de opwaartse kracht"),
                          ("een spijker springt naar een magneet", "de magnetische kracht")],
                  "Welke kracht speelt hier?", WW),
                 ("open", "Waarom kan je niet stappen op een spiegelgladde vloer? Gebruik het "
                          "woord wrijving in je antwoord.",
                  "Zonder wrijving tussen je schoen en de vloer kan je je niet afzetten: je "
                  "voet glijdt gewoon weg.", 3),
                 ("waar", "Een kracht kan ook alleen de vorm van iets veranderen, zonder dat "
                          "het beweegt.", True),
                 ("open", "Je gaat met een weegschaal naar de maan. Wat verandert er aan je "
                          "massa, en wat aan je gewicht?",
                  "Je massa blijft gelijk, want dat is de hoeveelheid materie. Je gewicht wordt "
                  "kleiner, want de maan trekt veel minder hard aan je dan de aarde.", 3),
             ]),

        dict(kop="Hefbomen en katrollen",
             opdracht="Met een hulpmiddel hoef je minder hard te duwen.",
             oefeningen=[
                 ("teken", "Teken een wip met twee kinderen erop, en zet een pijltje bij het "
                           "steunpunt.",
                  "Het steunpunt is het punt in het midden waarrond de wip draait.", 42),
                 ("open", "Twee kinderen zitten op een wip. De ene weegt veel meer dan de "
                          "andere. Hoe krijgen ze de wip toch in evenwicht?",
                  "Het zwaarste kind gaat dichter bij het steunpunt zitten, of het lichtste "
                  "schuift verder naar achter.", 3),
                 ("open", "Waarom duw je bij een hefboom het best zo ver mogelijk van het "
                          "steunpunt?",
                  "Hoe verder van het steunpunt, hoe groter het effect van je kracht. Je moet "
                  "dan minder hard duwen, maar wel over een langere afstand.", 3),
                 ("kies", "Waarom rol je een zware ton liever langs een plank omhoog?",
                  ["je moet minder hard duwen, maar over een langere weg",
                   "de ton wordt lichter", "er is dan geen wrijving meer",
                   "het gaat altijd sneller"], 0),
             ]),

        dict(kop="Soorten energie",
             opdracht="Energie verdwijnt nooit, ze verandert van vorm.",
             oefeningen=[
                 ("rij", [("een rijdende fiets", "bewegingsenergie"),
                          ("een bal bovenaan een helling", "hoogte-energie"),
                          ("een boterham", "chemische energie"),
                          ("een zonnepaneel in de zon", "licht wordt elektriciteit")],
                  "Welke energie zit hierin, of wat gebeurt ermee?", WW),
                 ("open", "Je gsm wordt warm als je lang speelt. Waar komt die warmte vandaan?",
                  "Een deel van de elektrische energie uit de batterij wordt omgezet in warmte "
                  "in plaats van in nuttig werk. Energie verdwijnt niet, ze verandert van vorm.", 3),
                 ("rij", [("steenkool", "fossiel"), ("wind", "hernieuwbaar"),
                          ("aardgas", "fossiel"), ("water", "hernieuwbaar")],
                  "Fossiel of hernieuwbaar?", W),
                 ("open", "Noem twee dingen die jullie thuis kunnen doen om energie te besparen.",
                  "Bijvoorbeeld: de verwarming een graad lager, lichten uit in een lege kamer, "
                  "korter douchen, toestellen niet op stand-by laten, ledlampen gebruiken.", 3),
             ]),

        dict(kop="Warmte en snelheid",
             opdracht="Warmte gaat altijd van warm naar koud.",
             oefeningen=[
                 ("open", "Waarom houdt een dikke winterjas je warm? Let op: de jas warmt zelf "
                          "niets op.",
                  "De jas houdt lucht vast tussen de vezels. Lucht geleidt warmte slecht, dus "
                  "de warmte van je lichaam raakt er minder makkelijk door weg.", 3),
                 ("open", "Je fietst 18 kilometer in 2 uur. Hoe snel ging je gemiddeld? Schrijf "
                          "je berekening erbij.",
                  "18 km : 2 u = 9 km per uur.", 2),
                 ("waar", "Warme lucht stijgt op en koude lucht zakt naar beneden.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-natuurkunde-licht-geluid-en-elektriciteit"] = dict(
    vak="Wetenschap en techniek", titel="Natuurkunde: licht, geluid en elektriciteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Licht",
             opdracht="Licht gaat altijd in een rechte lijn, tot het op iets botst.",
             oefeningen=[
                 ("rij", [("de zon", "lichtbron"), ("de maan", "geen lichtbron"),
                          ("een kaars", "lichtbron"), ("een spiegel", "geen lichtbron")],
                  "Lichtbron of niet?", WW),
                 ("teken", "Teken een zaklamp, een balletje ervoor en de schaduw erachter.",
                  "De schaduw ligt recht achter het balletje, aan de kant weg van de lamp.", 42),
                 ("open", "Je schuift het balletje dichter naar de zaklamp. Wat gebeurt er met "
                          "de schaduw?",
                  "De schaduw wordt groter.", 2),
                 ("rij", [("je ziet erdoor als door een raam", "doorzichtig"),
                          ("licht gaat er wel door, maar je ziet niets scherp", "doorschijnend"),
                          ("er gaat geen licht door", "ondoorzichtig")],
                  "Hoe noem je zo'n materiaal?", WW),
                 ("open", "Waarom ziet een blad van een boom er groen uit?",
                  "Het blad kaatst vooral het groene licht terug en slikt de andere kleuren op. "
                  "Wat terugkaatst, is wat je ziet.", 3),
             ]),

        dict(kop="Geluid",
             opdracht="Geluid ontstaat door trillingen en heeft stof nodig om door te gaan.",
             oefeningen=[
                 ("open", "Waarom hoor je in de ruimte niets, ook niet als er iets ontploft?",
                  "In de ruimte is bijna geen lucht. Geluid heeft deeltjes nodig om zich voort "
                  "te planten, dus zonder lucht draagt het niet.", 3),
                 ("open", "Je ziet de bliksem en telt vier seconden tot je de donder hoort. "
                          "Hoe ver is het onweer ongeveer? Reken met 340 meter per seconde.",
                  "4 × 340 m = 1 360 m, dus ongeveer 1,4 kilometer.", 2),
                 ("waar", "Hoe sneller iets trilt, hoe hoger de toon klinkt.", True),
                 ("open", "Waarom galmt het in een lege kamer veel meer dan in een kamer vol "
                          "meubels en tapijt?",
                  "Kale muren kaatsen het geluid terug. Zachte dingen zoals een tapijt, "
                  "gordijnen en een zetel slikken het geluid op.", 3),
                 ("kies", "In welke eenheid druk je uit hoe luid een geluid is?",
                  ["hertz", "decibel", "watt", "newton"], 1),
             ]),

        dict(kop="Elektriciteit",
             opdracht="Stroom loopt alleen rond als de kring helemaal gesloten is.",
             oefeningen=[
                 ("teken", "Teken een stroomkring met een batterij, een lampje en een "
                           "schakelaar. Zet er met een pijl bij waar de stroom loopt.",
                  "De draad loopt van de ene pool van de batterij, via de schakelaar en het "
                  "lampje, terug naar de andere pool. Staat de schakelaar open, dan brandt "
                  "het lampje niet.", 48),
                 ("rij", [("koper", "geleider"), ("rubber", "isolator"),
                          ("ijzer", "geleider"), ("plastic", "isolator")],
                  "Geleider of isolator?", W),
                 ("open", "Twee lampjes staan na elkaar in dezelfde kring. Eén lampje gaat "
                          "stuk. Wat gebeurt er met het andere, en waarom?",
                  "Dat gaat ook uit. De kring is onderbroken, dus er loopt nergens nog stroom.", 3),
                 ("waar", "Proefjes met elektriciteit doe je uitsluitend met een batterij, "
                          "nooit met het stopcontact.", True),
                 ("open", "Waarom vervangen we gloeilampen door ledlampen? Geef twee redenen.",
                  "Een ledlamp verbruikt veel minder stroom voor evenveel licht, en gaat veel "
                  "langer mee. Ze wordt ook veel minder warm.", 3),
             ]),

        dict(kop="Magneten",
             opdracht="Een magneet heeft altijd twee polen.",
             oefeningen=[
                 ("rij", [("noordpool bij zuidpool", "trekken elkaar aan"),
                          ("noordpool bij noordpool", "stoten elkaar af"),
                          ("zuidpool bij zuidpool", "stoten elkaar af")],
                  "Wat gebeurt er?", WW),
                 ("open", "Hoe maak je zelf een elektromagneet? Schrijf op wat je nodig hebt.",
                  "Wikkel geïsoleerd koperdraad vele keren rond een ijzeren spijker en sluit de "
                  "twee uiteinden aan op een batterij. Zolang er stroom loopt, is de spijker "
                  "magnetisch.", 3),
                 ("waar", "Alle metalen worden door een magneet aangetrokken.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-techniek-ontwerpen-en-maken"] = dict(
    vak="Wetenschap en techniek", titel="Techniek: ontwerpen en maken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van idee tot ding",
             opdracht="Een ontwerp maak je in stappen, en je komt vaak terug op een vorige.",
             oefeningen=[
                 ("rij", [("1", "het probleem en de eisen opschrijven"),
                          ("2", "ideeën schetsen en er één kiezen"),
                          ("3", "een prototype maken"),
                          ("4", "testen, aanpassen en beoordelen")],
                  "Zet de stappen van een ontwerp in de juiste volgorde. Wat hoort bij "
                  "welke stap?", WW),
                 ("open", "Wat is een programma van eisen? Leg het uit in je eigen woorden.",
                  "Een lijstje van alles waaraan je ontwerp moet voldoen: wat het moet kunnen, "
                  "hoe groot het mag zijn, wat het mag kosten, voor wie het is.", 3),
                 ("open", "Waarom maak je een prototype vaak eerst uit karton?",
                  "Karton is goedkoop en snel te bewerken. Zo kan je makkelijk uitproberen en "
                  "aanpassen voor je er dure materialen aan gebruikt.", 3),
                 ("waar", "Bij het ontwerpen hou je ook rekening met wie het gaat gebruiken.",
                  True),
             ]),

        dict(kop="Tekenen op maat",
             opdracht="Op een technische tekening staat alles precies.",
             oefeningen=[
                 ("rij", [("schaal 1:10, tekening 6 cm", "in het echt 60 cm"),
                          ("schaal 1:2, tekening 8 cm", "in het echt 16 cm"),
                          ("schaal 1:100, tekening 3 cm", "in het echt 300 cm of 3 m")],
                  "Hoe groot is het in het echt?", WW),
                 ("open", "Wat is het verschil tussen een schets en een technische tekening?",
                  "Een schets maak je snel uit de losse hand om een idee te tonen. Een "
                  "technische tekening is nauwkeurig, op schaal en met alle maten erbij, "
                  "zodat iemand anders het kan namaken.", 3),
                 ("kies", "In welke eenheid zet je de maten meestal op een technische tekening?",
                  ["in meter", "in centimeter", "in millimeter", "in kilometer"], 2),
             ]),

        dict(kop="Gereedschap en verbindingen",
             opdracht="Het juiste stuk gereedschap maakt het werk veilig én makkelijk.",
             oefeningen=[
                 ("rij", [("een gat in hout maken", "een boor"),
                          ("kijken of iets recht ligt", "een waterpas"),
                          ("een rechte hoek aftekenen", "een winkelhaak"),
                          ("een plank doorsnijden", "een zaag")],
                  "Welk gereedschap gebruik je?", WW),
                 ("rij", [("schroef", "los te maken"), ("nagel", "moeilijk los te maken"),
                          ("lijm", "niet los te maken"), ("bout met moer", "los te maken")],
                  "Is de verbinding later nog los te maken?", WW),
                 ("open", "Waarom draag je een veiligheidsbril als je zaagt of boort?",
                  "Er kunnen splinters of stof wegspringen. Een oog geneest niet zoals een "
                  "schram op je hand.", 2),
             ]),

        dict(kop="Bewegingen overbrengen",
             opdracht="Tandwielen, riemen en kettingen geven beweging door.",
             oefeningen=[
                 ("open", "Een klein tandwiel drijft een groot tandwiel aan. Draait het grote "
                          "wiel sneller of trager, en waarom?",
                  "Trager. Het grote wiel heeft meer tanden, dus het moet meer tanden laten "
                  "passeren voor één volledige draai. Het draait wel met meer kracht.", 3),
                 ("open", "Waarom is een holle buis vaak even stevig als een volle staaf, maar "
                          "veel lichter?",
                  "De sterkte zit vooral in de buitenkant van het materiaal. Het midden draagt "
                  "weinig bij, dus dat kan je weglaten zonder veel stevigheid te verliezen.", 3),
                 ("kies", "Waarom staan er driehoeken in een bouwkraan en in een brug?",
                  ["een driehoek kan niet vervormen", "het is goedkoper",
                   "het ziet er mooier uit", "er past meer beton in"], 0),
                 ("open", "Wat doet een sensor in een machine? Geef er een voorbeeld bij.",
                  "Een sensor meet iets uit de omgeving en geeft dat door, bijvoorbeeld een "
                  "bewegingsmelder die het licht aanzet, of een thermostaat die de temperatuur "
                  "meet.", 3),
             ]),

        dict(kop="Materiaal en milieu",
             opdracht="Wat gebeurt er met een toestel nadat je het niet meer gebruikt?",
             oefeningen=[
                 ("open", "Je toestel gaat stuk. Zet deze drie in volgorde van best naar "
                          "slechtst voor het milieu: wegwerpen, herstellen, recycleren.",
                  "Herstellen, dan recycleren, dan pas wegwerpen.", 2),
                 ("waar", "Nieuwe grondstoffen gebruiken is beter voor het milieu dan "
                          "materialen hergebruiken.", False),
                 ("open", "Wat betekent het dat een ontwerp ergonomisch is?",
                  "Dat het goed past bij het lichaam van wie het gebruikt: het ligt makkelijk "
                  "in de hand, zit comfortabel en doet geen pijn bij lang gebruik.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-aarde-en-de-ruimte"] = dict(
    vak="Wetenschap en techniek", titel="De aarde en de ruimte",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De aarde draait",
             opdracht="Let goed op het verschil tussen draaien om zichzelf en draaien om de zon.",
             oefeningen=[
                 ("rij", [("de aarde draait om haar as", "dag en nacht"),
                          ("de aarde draait om de zon", "een jaar"),
                          ("de as van de aarde staat schuin", "de seizoenen"),
                          ("de maan draait om de aarde", "de maanstanden")],
                  "Wat is daarvan het gevolg?", WW),
                 ("open", "Het is bij ons zomer. Welk seizoen is het dan in Australië? "
                          "Leg uit waarom.",
                  "Winter. De aarde staat schuin, dus als het noorden naar de zon gekeerd staat "
                  "en veel warmte krijgt, is het zuiden juist van de zon weggekeerd.", 3),
                 ("open", "Waarom is het aan de evenaar veel warmer dan aan de polen?",
                  "Aan de evenaar valt het zonlicht recht naar beneden, op een klein stukje "
                  "grond. Aan de polen valt het heel schuin, dus dezelfde hoeveelheid licht "
                  "wordt over een veel groter stuk verdeeld.", 3),
                 ("waar", "Zonder de zwaartekracht van de aarde zou onze lucht de ruimte in "
                          "drijven.", True),
             ]),

        dict(kop="De maan",
             opdracht="De maan maakt zelf geen licht.",
             oefeningen=[
                 ("teken", "Teken de maan zoals ze eruitziet bij volle maan, bij halve maan en "
                           "bij nieuwe maan. Zet er de naam bij.",
                  "Volle maan: een hele cirkel. Halve maan: de helft verlicht. Nieuwe maan: "
                  "je ziet niets, de verlichte kant is van ons weggekeerd.", 45),
                 ("open", "Waarom zie je de maan de ene week als een sikkel en de andere week "
                          "helemaal rond?",
                  "De maan draait om de aarde. Daardoor zie je telkens een ander stuk van haar "
                  "verlichte kant. De maan zelf verandert niet van vorm.", 3),
                 ("open", "Wat veroorzaakt eb en vloed aan zee?",
                  "Vooral de aantrekkingskracht van de maan op het water van de zeeën, en in "
                  "mindere mate die van de zon.", 2),
                 ("waar", "De voetstappen van de astronauten staan nog altijd op de maan, want "
                          "er is geen wind.", True),
             ]),

        dict(kop="Ons zonnestelsel",
             opdracht="Acht planeten, één ster.",
             oefeningen=[
                 ("open", "Schrijf de acht planeten op in volgorde vanaf de zon.",
                  "Mercurius, Venus, Aarde, Mars, Jupiter, Saturnus, Uranus, Neptunus.", 3),
                 ("rij", [("de grootste planeet", "Jupiter"), ("de rode planeet", "Mars"),
                          ("de planeet met de brede ringen", "Saturnus"),
                          ("de heetste planeet", "Venus")],
                  "Welke planeet is het?", WW),
                 ("open", "Wat is het verschil tussen een planeet en een ster?",
                  "Een ster maakt zelf licht en warmte, door kernreacties. Een planeet niet: "
                  "die draait om een ster en weerkaatst alleen haar licht.", 3),
                 ("open", "Waarom vliegen de planeten niet gewoon weg van de zon?",
                  "De zwaartekracht van de zon houdt ze vast. Omdat ze tegelijk vooruit "
                  "bewegen, vallen ze er ook niet in, maar draaien ze eromheen.", 3),
                 ("waar", "Een jaar duurt op elke planeet even lang.", False),
             ]),

        dict(kop="Verder weg kijken",
             opdracht="De ruimte is groter dan je je kan voorstellen.",
             oefeningen=[
                 ("open", "Wat is een lichtjaar? Let op: het is geen tijd maar iets anders.",
                  "De afstand die het licht in één jaar aflegt, ongeveer 9 500 miljard "
                  "kilometer. Het is dus een afstand.", 3),
                 ("open", "Waarom zie je overdag geen sterren, terwijl ze er wel zijn?",
                  "Het licht van de zon dat door onze lucht verstrooid wordt, is veel feller "
                  "dan het licht van de sterren. Daardoor vallen de sterren weg.", 3),
                 ("kies", "Hoe heet het sterrenstelsel waarin ons zonnestelsel ligt?",
                  ["de Melkweg", "het Zonnestelsel", "Andromeda", "de Grote Beer"], 0),
                 ("open", "Waarom zweven astronauten in een ruimtestation, terwijl de "
                          "zwaartekracht daar nog bijna even sterk is als op aarde?",
                  "Het station valt voortdurend rond de aarde, en de astronauten vallen mee. "
                  "Als alles samen valt, voel je geen gewicht meer.", 3),
             ]),
    ],
)
