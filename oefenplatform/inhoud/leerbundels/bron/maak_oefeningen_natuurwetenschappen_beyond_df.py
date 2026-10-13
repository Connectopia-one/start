# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij natuurwetenschappen 🌍 Beyond dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere reeksen om te benoemen, andere gevallen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een stap
uitleggen, een rekening uitschrijven). Wie hier iets bijschrijft, legt het eerst
naast `../../beyond-dubbele-finaliteit/natuurwetenschappen.json` en naast de
vakfiche zelf.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond-dubbele-finaliteit". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Natuurwetenschappen"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Bij een rekenopgave: schrijf je tussenstappen op, ook als je ze in je hoofd kan maken.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-bevruchting-en-de-ontwikkeling-van-embryo-en-foetus-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Bevruchting en de ontwikkeling van embryo en foetus",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk hormoon of welk orgaan?",
             opdracht="Schrijf bij elke omschrijving de juiste naam.",
             oefeningen=[
                 ("rij", [("laat een follikel rijpen", "FSH"),
                          ("lokt de eisprong uit", "LH"),
                          ("houdt het slijmvlies dik", "progesteron")], "Welk hormoon?", WW),
                 ("rij", [("maakt FSH en LH", "de hypofyse"),
                          ("maakt progesteron na de eisprong", "het geel lichaam"),
                          ("maakt testosteron", "de teelbal")], "Welk orgaan of welke structuur?", WW),
             ]),
        dict(kop="Reken op de cyclus",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"Een vrouw heeft een cyclus van \(30\) dagen. Op de hoeveelste dag valt haar "
                          "eisprong ongeveer?", r"op dag \(16\), want de eisprong is ongeveer \(14\) dagen vóór "
                          "de volgende menstruatie", W),
                 ("kort", r"Een vrouw heeft een cyclus van \(26\) dagen. Op de hoeveelste dag valt haar "
                          "eisprong ongeveer?", r"op dag \(12\)", W),
                 ("open", "Waarom is veertien dagen vóór de volgende menstruatie een betrouwbaardere "
                          "regel dan veertien dagen ná de vorige?",
                  "De tweede helft van de cyclus duurt bij bijna elke vrouw ongeveer veertien dagen. De "
                  "eerste helft kan veel sterker verschillen, ook bij dezelfde vrouw.", 3),
             ]),
        dict(kop="Eicel of zaadcel?",
             opdracht="Schrijf eicel, zaadcel of beide.",
             oefeningen=[
                 ("rij", [("heeft een flagel", "zaadcel"), ("heeft reservevoedsel", "eicel"),
                          ("heeft een kern", "beide")], None, W),
                 ("rij", [("mitochondriën in het middenstuk", "zaadcel"),
                          ("laag eiwit rondom", "eicel"),
                          ("de grootste cel van het lichaam", "eicel")], None, W),
             ]),
        dict(kop="Zet de weg op volgorde",
             opdracht=r"Nummer de stappen van \(1\) tot \(5\).",
             oefeningen=[
                 ("tabel", ["Nummer", "Wat er gebeurt"],
                  [[None, "de kiemblaas nestelt zich in het baarmoederslijmvlies"],
                   [None, "de LH-piek lokt de eisprong uit"],
                   [None, "het bevruchtingsmembraan sluit de eicel af"],
                   [None, "de zaadcellen zwemmen door de baarmoeder naar de eileider"],
                   [None, "de kernen versmelten tot een zygote"]],
                  r"\(1\) = de LH-piek lokt de eisprong uit · \(2\) = de zaadcellen zwemmen door de baarmoeder "
                  r"naar de eileider · \(3\) = het bevruchtingsmembraan sluit de eicel af · \(4\) = de kernen "
                  r"versmelten tot een zygote · \(5\) = de kiemblaas nestelt zich in het baarmoederslijmvlies",
                  "56px"),
             ]),
        dict(kop="De placenta en de navelstreng",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("tabel", ["Gaat van moeder naar vrucht", "Gaat van vrucht naar moeder"],
                  [[None, None], [None, None]],
                  "Van moeder naar vrucht: zuurstof en voedingsstoffen zoals glucose. Van vrucht naar "
                  "moeder: koolstofdioxide en afvalstoffen.", WL),
                 ("open", "Het bloed van de moeder en van de vrucht raken elkaar niet. Waarom is dat "
                          "een voordeel?",
                  "Zo hoeven hun bloedgroepen niet te passen en kunnen hun afweerstelsels elkaar niet "
                  "aanvallen. De stoffen gaan wel door het dunne vlies heen.", 4),
                 ("kort", "Hoeveel slagaders en hoeveel aders zitten er in de navelstreng?",
                  "twee slagaders en één ader", W),
             ]),
        dict(kop="Levensstijl tijdens de zwangerschap",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("waar", "Een teratogene stof is een stof die de ontwikkeling van de vrucht verstoort.",
                  True),
                 ("waar", "Wie zelf niet rookt maar in een rokerige kamer zit, loopt geen enkel risico.",
                  False),
                 ("open", "Een vrouw met een kinderwens vraagt waarom ze nú al foliumzuur moet nemen en "
                          "niet pas als ze zwanger is. Wat antwoord je?",
                  "De ruggengraat en het zenuwstelsel worden al in de eerste weken aangelegd, vaak nog "
                  "voor ze weet dat ze zwanger is. Foliumzuur moet er dan al zijn.", 4),
                 ("rij", [("rodehond", "rubellavirus"), ("rauw vlees", "toxoplasmose-parasiet"),
                          ("overgedragen door muggen", "zikavirus")],
                  "Welke ziekteverwekker hoort hierbij?", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vruchtbaarheid-anticonceptie-en-kinderwens-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Vruchtbaarheid, anticonceptie en kinderwens",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort methode?",
             opdracht="Schrijf natuurlijk, hormonaal, barrière of ingreep.",
             oefeningen=[
                 ("rij", [("de temperatuurmethode", "natuurlijk"), ("de vaginale ring", "hormonaal"),
                          ("het pessarium", "barrière")], None, W),
                 ("rij", [("sterilisatie", "ingreep"), ("het hormoonstaafje", "hormonaal"),
                          ("het vrouwencondoom", "barrière")], None, W),
                 ("rij", [("de ovulatiemethode", "natuurlijk"), ("de prikpil", "hormonaal"),
                          ("de kalendermethode", "natuurlijk")], None, W),
             ]),
        dict(kop="Hoe lang werkt het?",
             opdracht="Schrijf de duur bij elk middel.",
             oefeningen=[
                 ("rij", [("de prikpil", "ongeveer drie maanden"),
                          ("het hormoonstaafje", "enkele jaren"),
                          ("de combinatiepil", "één dag, elke dag opnieuw")],
                  "Hoe lang werkt het?", WW),
             ]),
        dict(kop="Kies het juiste advies",
             opdracht="Lees de situatie en schrijf wat je aanraadt, met je reden.",
             oefeningen=[
                 ("open", "Iemand neemt de pil en vraagt of een condoom daarnaast nog nodig is bij een "
                          "nieuwe partner. Wat antwoord je?",
                  "Ja. De pil voorkomt een zwangerschap, maar houdt geen enkele soa tegen. Alleen een "
                  "mannen- of vrouwencondoom beschermt daar ook tegen.", 4),
                 ("open", "Iemand wil geen hormonen gebruiken en wil toch een middel dat jaren werkt. "
                          "Welk middel past en waarom?",
                  "Een koperspiraaltje. Het werkt zonder hormonen: het koper maakt de zaadcellen "
                  "onbeweeglijk.", 3),
                 ("open", "Een koppel vindt coïtus interruptus voldoende. Waarom raad je dat af?",
                  "Er komen al zaadcellen vrij voor de zaadlozing, en het hangt volledig af van het "
                  "juiste moment. Het is daardoor onbetrouwbaar.", 3),
             ]),
        dict(kop="Betrouwbaar op papier of in de praktijk?",
             opdracht="Beoordeel.",
             oefeningen=[
                 ("waar", "Een zaaddodend middel is op zichzelf betrouwbaar genoeg.", False),
                 ("waar", "Een methode kan in de praktijk minder betrouwbaar zijn dan op papier.", True),
                 ("open", "Leg uit waarom dat verschil tussen papier en praktijk bestaat.",
                  "Op papier staat hoe betrouwbaar een methode is als ze elke keer juist gebruikt wordt. "
                  "In de praktijk wordt een pil vergeten of een condoom verkeerd gebruikt.", 3),
             ]),
        dict(kop="Behandelingen bij een kinderwens",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Afkorting of naam", "Wat er gebeurt"],
                  [["KI", None], ["IVF", None], ["ICSI", None]],
                  "KI: sperma wordt rechtstreeks in de baarmoeder gebracht. IVF: de bevruchting gebeurt "
                  "buiten het lichaam, in het labo. ICSI: één zaadcel wordt in de eicel geprikt.",
                  WL),
                 ("waar", "Bij IVF groeit de vrucht de hele zwangerschap in het labo.", False),
                 ("open", "Waarom haalt men bij IVF vaak meerdere eicellen in één keer?",
                  "Niet elke eicel raakt bevrucht en niet elk embryo groeit goed door. Met meerdere "
                  "eicellen is de kans op een geslaagde behandeling groter.", 3),
                 ("open", "Waarom verhoogt hormonale stimulatie de kans op een meerling?",
                  "De eierstok laat dan meerdere eicellen rijpen in plaats van één, en er kunnen er dus "
                  "meerdere bevrucht raken.", 3),
             ]),
        dict(kop="Wat de vruchtbaarheid aantast",
             opdracht="Schrijf bij elk geval wie of wat er geraakt wordt, en waarom.",
             oefeningen=[
                 ("rij", [("roken", "man en vrouw"), ("warmte bij de teelballen", "man"),
                          ("ondergewicht", "vrouw")], "Bij wie speelt dit?", WW),
                 ("open", "Waarom hangen de teelballen buiten het lichaam?",
                  "Zaadcellen rijpen het best net onder de lichaamstemperatuur. Buiten het lichaam is "
                  "het enkele graden koeler.", 3),
                 ("open", "Een jonge vrouw moet chemotherapie krijgen. Waarom stelt de arts voor om "
                          "eerst eicellen in te vrieren?",
                  "Chemotherapie kan de vruchtbaarheid blijvend aantasten. Door nu eicellen in te "
                  "vriezen, bewaart ze haar kans op een kind voor later.", 4),
                 ("waar", "Een soa die niet behandeld wordt, kan tot onvruchtbaarheid leiden.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-dna-naar-eiwit-genexpressie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Van DNA naar eiwit: genexpressie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vul de tegenoverliggende streng aan",
             opdracht="Schrijf de basen van de tweede DNA-streng.",
             oefeningen=[
                 ("rij", [("A T G C", "T A C G"), ("C C G A", "G G C T"),
                          ("T A A G", "A T T C")], "Welke basen staan ertegenover in DNA?", WW),
                 ("rij", [("A T G C in DNA", "U A C G in RNA"),
                          ("T T A C in DNA", "A A U G in RNA")],
                  "En welke basen staan ertegenover in het mRNA?", WW),
             ]),
        dict(kop="DNA of RNA?",
             opdracht="Schrijf DNA, RNA of beide.",
             oefeningen=[
                 ("rij", [("ribose", "RNA"), ("thymine", "DNA"), ("guanine", "beide")], None, W),
                 ("rij", [("twee strengen", "DNA"), ("uracil", "RNA"),
                          ("fosfaatgroepen", "beide")], None, W),
             ]),
        dict(kop="Gen, allel, genotype of fenotype?",
             opdracht="Schrijf bij elk voorbeeld de juiste term.",
             oefeningen=[
                 ("rij", [("je ogen zijn bruin", "fenotype"),
                          ("het stuk DNA voor oogkleur", "gen"),
                          ("de versie voor bruin", "allel")], None, WW),
                 ("rij", [("al je erfelijk materiaal samen", "genotype"),
                          (r"je lengte van \(1{,}72\) m", "fenotype"),
                          ("de versie voor blauw", "allel")], None, WW),
             ]),
        dict(kop="Zet de weg van gen naar eiwit op volgorde",
             opdracht=r"Nummer de stappen van \(1\) tot \(4\) en vul de plaats aan.",
             oefeningen=[
                 ("tabel", ["Nummer", "Stap", "Waar in de cel"],
                  [[None, "het ribosoom koppelt aminozuren aan elkaar", None],
                   [None, "het mRNA wordt van het DNA afgelezen", None],
                   [None, "het eiwit is klaar en doet zijn werk", None],
                   [None, "het mRNA reist naar een ribosoom", None]],
                  r"\(1\) = het mRNA wordt van het DNA afgelezen, in de celkern · \(2\) = het mRNA reist naar een "
                  r"ribosoom, uit de kern naar het cytoplasma · \(3\) = het ribosoom koppelt aminozuren aan "
                  r"elkaar, aan het ribosoom · \(4\) = het eiwit is klaar en doet zijn werk, in de cel",
                  "90px"),
                 ("open", "Waarom verlaat het DNA zelf de celkern niet?",
                  "Het DNA is het origineel en moet heel blijven. Alleen een kopie, het mRNA, reist naar "
                  "het ribosoom.", 3),
             ]),
        dict(kop="Waarom lijken cellen niet op elkaar?",
             opdracht="Leg uit in volledige zinnen.",
             oefeningen=[
                 ("open", "Een spiercel en een huidcel hebben precies hetzelfde DNA. Waarom zien ze er "
                          "dan zo verschillend uit?",
                  "In elke cel staan andere genen aan. Een gen dat aanwezig is, staat niet altijd aan, "
                  "en alleen de genen die aanstaan leveren eiwitten.", 4),
                 ("open", "Twee eenlingen met hetzelfde genotype voor lengte worden niet even groot. Geef "
                          "twee mogelijke oorzaken.",
                  "De omgeving speelt mee: voeding, beweging, ziekte of slaap kunnen de lengte "
                  "beïnvloeden. Omgevingsfactoren bepalen mee hoe sterk een gen tot uiting komt.", 4),
                 ("waar", "Een litteken dat je oploopt, kan je doorgeven aan je kinderen.", False),
             ]),
        dict(kop="Veredeling of genetische modificatie?",
             opdracht="Schrijf veredeling of genetische modificatie en leg bij de laatste vraag uit.",
             oefeningen=[
                 ("rij", [("bacteriën maken menselijke insuline", "genetische modificatie"),
                          ("de beste tomatenplanten kruisen", "veredeling"),
                          ("DNA van twee soorten samenbrengen", "genetische modificatie")],
                  None, WL),
                 ("open", "Waarom zijn veredeling en genetische modificatie niet hetzelfde?",
                  "Bij veredeling kruis je doelgericht en kies je de beste nakomelingen: je blijft binnen "
                  "wat de natuur zelf kan kruisen. Bij genetische modificatie grijp je rechtstreeks in het "
                  "DNA in, ook tussen soorten die niet kunnen kruisen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-overerving-van-kenmerken-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Overerving van kenmerken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoeveel chromosomen?",
             opdracht="Schrijf het aantal en of de cel haploïd of diploïd is.",
             oefeningen=[
                 ("rij", [("een menselijke huidcel", r"\(46\), diploïd"),
                          ("een menselijke zaadcel", r"\(23\), haploïd"),
                          ("een menselijke eicel", r"\(23\), haploïd")], None, WW),
                 ("kort", "Een zygote ontstaat uit een eicel en een zaadcel. Hoeveel chromosomen heeft "
                          "ze?", r"\(46\)", W),
             ]),
        dict(kop="Mitose of meiose?",
             opdracht="Schrijf mitose of meiose.",
             oefeningen=[
                 ("rij", [("twee gelijke dochtercellen", "mitose"),
                          ("vier verschillende haploïde cellen", "meiose"),
                          ("een wonde op je knie geneest", "mitose")], None, WW),
                 ("rij", [("gebeurt in de teelballen", "meiose"),
                          ("brengt variatie tussen de nakomelingen", "meiose"),
                          ("een plant maakt nieuwe bladcellen", "mitose")], None, WW),
             ]),
        dict(kop="Reken een kruising uit",
             opdracht="Vul het schema aan en lees de verhoudingen af.",
             oefeningen=[
                 ("tabel", ["", "A", "a"],
                  [["A", None, None], ["a", None, None]],
                  r"AA, Aa in de bovenste rij en Aa, aa in de onderste. Dus \(25\,\%\) AA, \(50\,\%\) Aa en \(25\,\%\) aa.",
                  "80px"),
                 ("kort", "Welk percentage van die kinderen vertoont het recessieve kenmerk?", r"\(25\,\%\)", W),
                 ("kort", "Welk percentage is drager zonder het kenmerk te tonen?", r"\(50\,\%\)", W),
                 ("open", "Twee ouders met bloedgroep A krijgen een kind met bloedgroep O. Welk genotype "
                          "hebben de ouders? Leg uit.",
                  "Beide ouders zijn AO, dus heterozygoot. Elk gaf het O-allel door, en het kind is OO.", 4),
             ]),
        dict(kop="Welke soort overerving?",
             opdracht="Schrijf dominant-recessief, intermediair of codominant.",
             oefeningen=[
                 ("rij", [("bloedgroep AB", "codominant"),
                          ("een rode en een witte bloem geven roze", "intermediair"),
                          ("de ziekte van Huntington", "dominant-recessief")], None, WL),
             ]),
        dict(kop="X-gebonden overerving",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("waar", "Rood-groenkleurenblindheid komt vaker voor bij jongens dan bij meisjes.", True),
                 ("open", "Leg uit waarom dat zo is.",
                  "Het gen ligt op het X-chromosoom. Een jongen heeft maar één X, dus één afwijkend allel "
                  "volstaat. Een meisje heeft nog een tweede X die het opvangt.", 4),
                 ("kort", "Hoe noem je een vrouw die het allel draagt zonder zelf kleurenblind te zijn?",
                  "een draagster", W),
                 ("open", "Een moeder is draagster van hemofilie, de vader is gezond. Hoe groot is de "
                          "kans dat een zoon hemofilie heeft? Leg uit.",
                  r"De helft, dus \(50\,\%\). Een zoon krijgt zijn enige X van zijn moeder, en de helft van haar "
                  "X-chromosomen draagt het afwijkende allel.", 4),
             ]),
        dict(kop="Mutaties",
             opdracht="Beoordeel en vul aan.",
             oefeningen=[
                 ("rij", [("een mutatie in een huidcel", "niet erfelijk"),
                          ("een mutatie in een eicel", "erfelijk"),
                          ("een mutatie in een zaadcel", "erfelijk")], None, WW),
                 ("waar", "Elke mutatie is schadelijk voor het organisme.", False),
                 ("open", "Geef twee oorzaken van een mutatie en leg bij één ervan uit hoe je je kan "
                          "beschermen.",
                  "Uv-straling van de zon, bepaalde chemische stoffen en fouten bij het kopiëren van DNA. "
                  "Tegen uv bescherm je je met kleding, schaduw en zonnecrème.", 4),
                 ("open", "In een stamboom staat een vierkantje. Voor wie staat dat, en voor wie staat "
                          "een cirkel?",
                  "Een vierkantje staat voor een man, een cirkel voor een vrouw.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biologische-evolutie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Biologische evolutie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Homoloog, analoog of rudimentair?",
             opdracht="Schrijf bij elk voorbeeld de juiste term.",
             oefeningen=[
                 ("rij", [("de arm van een mens en de vleugel van een vleermuis", "homoloog"),
                          ("de vleugel van een vogel en die van een insect", "analoog"),
                          ("het staartbeentje van de mens", "rudimentair")], None, WL),
                 ("rij", [("de vin van een walvis en de arm van een mens", "homoloog"),
                          ("de heupbeentjes van een walvis", "rudimentair"),
                          ("de spiertjes bij je oorschelp", "rudimentair")], None, WL),
             ]),
        dict(kop="Uit welk vakgebied komt dit argument?",
             opdracht="Schrijf anatomie, embryologie, paleontologie of moleculaire biologie.",
             oefeningen=[
                 ("rij", [("Archaeopteryx heeft kenmerken van reptielen én vogels", "paleontologie"),
                          ("alle organismen gebruiken dezelfde vier basen", "moleculaire biologie"),
                          ("embryo's van verwante soorten lijken op elkaar", "embryologie")],
                  None, WL),
                 ("rij", [("dezelfde beenderen in dezelfde orde in elke voorpoot", "anatomie"),
                          ("fossielen in diepere lagen zijn ouder", "paleontologie")], None, WL),
             ]),
        dict(kop="Lees de evolutieboom",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("waar", "Twee soorten die pas recent afsplitsen, lijken genetisch sterk op elkaar.",
                  True),
                 ("waar", "Een soort die hoger in de boom staat, is verder in haar ontwikkeling.", False),
                 ("open", "Leg uit waarom die tweede uitspraak fout is.",
                  "Een evolutieboom toont verwantschap, geen rangorde. Elke tak die vandaag nog leeft, is "
                  "even lang bezig met evolueren.", 3),
                 ("open", "Onderzoekers maken een stamboom met DNA en een stamboom met skeletten, en ze "
                          "komen op hetzelfde uit. Waarom is dat belangrijk?",
                  "Twee onafhankelijke soorten gegevens wijzen dan dezelfde verwantschap aan. Dat maakt "
                  "de stamboom veel betrouwbaarder dan één bron alleen.", 4),
             ]),
        dict(kop="Wat volgt eruit?",
             opdracht="Schrijf je besluit en je reden.",
             oefeningen=[
                 ("open", "Het DNA van soort A en soort B verschilt heel sterk. Wat besluit je over hun "
                          "gemeenschappelijke voorouder?",
                  "Die leefde lang geleden. Hoe groter het verschil in DNA, hoe verder terug de "
                  "gemeenschappelijke voorouder ligt.", 3),
                 ("open", "Iemand zegt: de mens stamt af van de chimpansee. Verbeter die uitspraak.",
                  "Mens en chimpansee hebben een gemeenschappelijke voorouder. Die voorouder is "
                  "uitgestorven en was geen chimpansee zoals die vandaag leeft.", 3),
                 ("kort", "Hoe oud is de aarde volgens het huidige onderzoek?",
                  r"ongeveer \(4{,}6\) miljard jaar", W),
                 ("open", "Waarom is die ouderdom belangrijk voor de evolutietheorie?",
                  "Kleine veranderingen stapelen zich op over vele generaties. Daarvoor is heel veel tijd "
                  "nodig, en die is er.", 3),
             ]),
        dict(kop="Wetenschap of niet?",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("waar", "De moderne evolutietheorie is sinds Darwin ongewijzigd gebleven.", False),
                 ("open", "Waarom noemt men de evolutietheorie een wetenschappelijke theorie, terwijl "
                          "creationisme dat niet is?",
                  "De evolutietheorie steunt op waarnemingen en kan getoetst worden: metingen kunnen haar "
                  "bijsturen of tegenspreken. De verklaring van het creationisme is niet met waarnemingen "
                  "te toetsen.", 4),
                 ("open", "Van veel soorten uit het verleden bestaat er geen enkel fossiel. Waarom niet?",
                  "Fossiel worden vraagt bijzondere omstandigheden: het lichaam moet snel bedekt raken en "
                  "de lagen moeten bewaard blijven. Meestal gebeurt dat niet.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-natuurlijke-selectie-en-het-ontstaan-van-soorten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Natuurlijke selectie en het ontstaan van soorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Lamarck of Darwin?",
             opdracht="Schrijf Lamarck of Darwin bij elke uitspraak.",
             oefeningen=[
                 ("rij", [("wie zich uitrekt, geeft die vorm door", "Lamarck"),
                          ("binnen een soort bestaat er variatie", "Darwin"),
                          ("er worden meer jongen geboren dan er overleven", "Darwin")], None, W),
                 ("rij", [("verworven eigenschappen worden doorgegeven", "Lamarck"),
                          ("wie het best past, plant zich het meest voort", "Darwin")], None, W),
             ]),
        dict(kop="Verbeter de uitspraak",
             opdracht="Schrijf de uitspraak juist op en leg uit wat eraan fout was.",
             oefeningen=[
                 ("open", "De giraffen rekten hun hals uit om hoger te kunnen eten, en daardoor werden "
                          "hun nakomelingen langer.",
                  "Giraffen met een iets langere hals bereikten meer voedsel en kregen meer nakomelingen. "
                  "Die langere hals was erfelijk; uitrekken tijdens je leven verandert je "
                  "geslachtscellen niet.", 4),
                 ("open", "De bacteriën werden resistent omdat ze het antibioticum nodig hadden om te "
                          "overleven.",
                  "Enkele bacteriën waren al ongevoelig, door een toevallige mutatie. Zij overleefden de "
                  "kuur en plantten zich voort. Een mutatie ontstaat niet omdat een organisme ze nodig "
                  "heeft.", 4),
                 ("open", "De vlinders werden donkerder toen de boomstammen zwart werden.",
                  "De vlinders zelf veranderden niet van kleur. De donkere exemplaren vielen minder op, "
                  "overleefden vaker en werden daardoor talrijker in de populatie.", 4),
             ]),
        dict(kop="Wat heeft selectie nodig?",
             opdracht="Beoordeel.",
             oefeningen=[
                 ("waar", "Natuurlijke selectie maakt zelf nieuwe eigenschappen aan.", False),
                 ("waar", "Natuurlijke selectie werkt alleen op erfelijke kenmerken.", True),
                 ("waar", "Een organisme kan zich doelbewust aanpassen om beter te overleven.", False),
                 ("open", "Een populatie wordt heel klein. Waarom is dat gevaarlijk voor de soort?",
                  "Er is dan weinig erfelijke variatie om op terug te vallen. Verandert de omgeving, dan "
                  "is de kans klein dat er iemand bij is die het overleeft.", 4),
             ]),
        dict(kop="Welke soort isolatie?",
             opdracht="Schrijf geografisch, temporeel, gedrag, ecologisch of morfologisch.",
             oefeningen=[
                 ("rij", [("een bergketen scheidt twee kuddes", "geografisch"),
                          ("de ene soort paart in mei, de andere in augustus", "temporeel"),
                          ("de bouw maakt paren onmogelijk", "morfologisch")], None, WL),
                 ("rij", [("de ene groep leeft in de boomtop, de andere op de bodem", "ecologisch"),
                          ("de baltsdans wordt niet herkend", "gedrag"),
                          ("een eiland raakt los van het vasteland", "geografisch")], None, WL),
                 ("open", "Waarom kan er zonder isolatie geen nieuwe soort ontstaan?",
                  "Zonder isolatie blijven de twee groepen hun genen mengen. De verschillen verdwijnen "
                  "dan weer in plaats van groter te worden.", 3),
             ]),
        dict(kop="Soort of niet?",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("open", "Een paard en een ezel krijgen samen een muildier, maar dat muildier is "
                          "onvruchtbaar. Zijn paard en ezel dezelfde soort? Leg uit.",
                  "Nee. Tot één soort horen dieren die onderling vruchtbare nakomelingen krijgen. Het "
                  "muildier is onvruchtbaar, dus zijn het twee soorten.", 4),
             ]),
        dict(kop="De menswording",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("de eerste stap in de menswording", "rechtop lopen"),
                          ("het voordeel daarvan", "de handen kwamen vrij"),
                          ("het woord voor de hele menswording", "hominisatie")], None, WL),
                 ("open", "Noem drie kenmerken die de mens met de mensapen gemeenschappelijk heeft.",
                  "Een grote hersenschors, handen met een tegenstelbare duim en jarenlange zorg voor de "
                  "jongen.", 3),
                 ("waar", "Homo neanderthalensis en Homo sapiens hebben een tijd naast elkaar geleefd.",
                  True),
                 ("open", "Biodiversiteit gaat over meer dan het aantal soorten. Over wat nog?",
                  "Ook over de erfelijke variatie binnen één soort en over de verscheidenheid aan "
                  "leefgebieden.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-productlabels-pictogrammen-en-risico-s-van-stoffen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Productlabels, pictogrammen en risico's van stoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk pictogram hoort hierbij?",
             opdracht="Schrijf het soort gevaar.",
             oefeningen=[
                 ("rij", [("vreet de huid weg", "bijtend of corrosief"),
                          ("voedt een brand", "oxiderend"),
                          ("de damp vat vlam", "ontvlambaar")], None, WW),
                 ("rij", [("de fles kan openbarsten in de zon", "gas onder druk"),
                          ("prikt en doet de huid rood worden", "irriterend")], None, WW),
             ]),
        dict(kop="H-zin of P-zin?",
             opdracht="Schrijf H of P bij elke zin.",
             oefeningen=[
                 ("rij", [("veroorzaakt ernstige brandwonden", "H"),
                          ("draag handschoenen", "P"),
                          ("buiten het bereik van kinderen houden", "P")], None, W),
                 ("rij", [("zeer licht ontvlambare vloeistof", "H"),
                          ("bij contact met de ogen spoelen met water", "P"),
                          ("schadelijk voor waterorganismen", "H")], None, W),
             ]),
        dict(kop="Waar hoort het afval?",
             opdracht="Schrijf gft, pmd, papier en karton, restafval of kga.",
             oefeningen=[
                 ("rij", [("aardappelschillen", "gft"), ("een halfvolle fles verf", "kga"),
                          ("een leeg drankkarton", "pmd")], None, WW),
                 ("rij", [("gemaaid gras", "gft"), ("een lege conservenblik", "pmd"),
                          ("een restje ontstopper", "kga")], None, WW),
                 ("open", "Waarom mag je ontstopper en bleekwater niet samen in dezelfde afvoer gieten?",
                  "Samen kunnen ze reageren en giftige gassen vormen. Je giet ze allebei niet in de "
                  "afvoer: ze horen bij het klein gevaarlijk afval.", 4),
             ]),
        dict(kop="Lees de code op de verpakking",
             opdracht="Vul aan en beoordeel.",
             oefeningen=[
                 ("kort", r"Welke kunststof hoort bij recyclagecode \(1\)?", "PET", W),
                 ("waar", "De driehoek van pijltjes met een cijfer betekent dat de verpakking zeker "
                          "gerecycleerd wordt.", False),
                 ("open", "Wat zegt dat cijfer dan wel?",
                  "Het zegt uit welke kunststof de verpakking gemaakt is. Het is een identificatiecode, "
                  "geen belofte over recyclage.", 3),
             ]),
        dict(kop="Kookpunt en smeltpunt",
             opdracht="Reken, kies en leg uit.",
             oefeningen=[
                 ("tabel", ["Stof", "Smeltpunt", "Kookpunt", r"Vast, vloeibaar of gas bij \(20^{\circ}\text{C}\)?"],
                  [["aceton", r"\(-95^{\circ}\text{C}\)", r"\(56^{\circ}\text{C}\)", None],
                   ["water", r"\(0^{\circ}\text{C}\)", r"\(100^{\circ}\text{C}\)", None],
                   ["ijzer", r"\(1538^{\circ}\text{C}\)", r"\(2862^{\circ}\text{C}\)", None]],
                  r"Aceton is vloeibaar, water is vloeibaar en ijzer is vast bij \(20^{\circ}\text{C}\).", "95px"),
                 ("open", "Waarom gebruikt men net aceton om glaswerk snel droog te maken?",
                  "Aceton heeft een laag kookpunt en verdampt dus vlot bij kamertemperatuur. Het neemt "
                  "het water mee en laat het glas droog achter.", 3),
                 ("waar", "Het kookpunt van een stof zegt niets over hoe gevaarlijk ze kan zijn.", False),
             ]),
        dict(kop="Welk oplosmiddel kies je?",
             opdracht="Schrijf water of een organisch oplosmiddel, en geef je reden.",
             oefeningen=[
                 ("rij", [("een vetvlek van olie", "organisch oplosmiddel"),
                          ("een vlek van keukenzout", "water"),
                          ("een vlek van suikersiroop", "water")], None, WL),
                 ("open", "Noem drie organische, vetoplosbare oplosmiddelen.",
                  "Thinner, terpentine, white spirit en wasbenzine. Drie daarvan volstaan.", 2),
                 ("open", "Leg de vuistregel soort lost soort uit met een voorbeeld.",
                  "Wat in water oplost, lost niet op in een organisch oplosmiddel, en omgekeerd. Zout "
                  "lost in water op maar niet in thinner; olie lost in thinner op maar niet in water.", 4),
             ]),
        dict(kop="Zuur, neutraal of basisch?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Stof", "pH ongeveer", "Zuur, neutraal of basisch?"],
                  [["huishoudazijn", r"\(3\)", None], ["zuiver water", r"\(7\)", None],
                   ["ontstopper", r"\(13\)", None], ["citroensap", r"\(2\)", None]],
                  "Huishoudazijn is zuur, zuiver water neutraal, ontstopper basisch en citroensap zuur.",
                  "110px"),
                 ("open", "Rode koolsap kleurt rood tot roze in de ene vloeistof en groen tot geel in de "
                          "andere. Wat besluit je over elke vloeistof?",
                  "Rood tot roze betekent zuur, groen tot geel betekent basisch. Rode koolsap is een "
                  "zuur-base indicator.", 3),
                 ("open", "Waarom pak je een partje citroen beter niet in aluminiumfolie?",
                  "Het zuur in de citroen reageert met het aluminium. Je krijgt gaatjes in de folie en een "
                  "rare smaak aan de citroen.", 3),
                 ("open", "Er komt een bijtend product op je hand. Wat doe je, en wat doe je zeker niet?",
                  "Je spoelt meteen en lang met veel water. Je probeert het niet te neutraliseren met een "
                  "andere stof en je wacht niet af.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-voedingsbestanddelen-en-etiketten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Voedingsbestanddelen en etiketten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke voedingsstof zit hier vooral in?",
             opdracht="Schrijf koolhydraten, eiwitten, vetten, mineralen of vitaminen.",
             oefeningen=[
                 ("rij", [("rijst", "koolhydraten"), ("olijfolie", "vetten"),
                          ("kipfilet", "eiwitten")], None, WW),
                 ("rij", [("melk, voor de botten", "mineralen"), ("linzen", "eiwitten"),
                          ("brood", "koolhydraten")], None, WW),
             ]),
        dict(kop="Voedingsstof of voedingsmiddel?",
             opdracht="Schrijf voedingsstof of voedingsmiddel.",
             oefeningen=[
                 ("rij", [("een appel", "voedingsmiddel"), ("fructose", "voedingsstof"),
                          ("ijzer", "voedingsstof")], None, WW),
                 ("rij", [("een boterham", "voedingsmiddel"), ("zetmeel", "voedingsstof"),
                          ("yoghurt", "voedingsmiddel")], None, WW),
             ]),
        dict(kop="Mono-, di- of polysacharide?",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("glucose", "monosacharide"), ("zetmeel", "polysacharide"),
                          ("fructose", "monosacharide")], None, WW),
                 ("open", "Leg uit waarom brood je energie langer op peil houdt dan een snoepje.",
                  "Brood bevat zetmeel, een lange keten glucosemoleculen. Die keten moet eerst geknipt "
                  "worden, en daardoor komt de glucose geleidelijk in je bloed. Losse suiker geeft een "
                  "korte piek en daarna een dip.", 4),
                 ("open", "Een loper eet een stuk fruit vlak voor de start en pasta de avond ervoor. "
                          "Waarom net in die orde?",
                  "Fruit geeft snel energie, want glucose en fructose zijn al losse moleculen. Zetmeel "
                  "uit pasta geeft tragere energie en moet dus langer vooraf gegeten worden.", 4),
             ]),
        dict(kop="Waarvoor dient het in je lichaam?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Voedingsstof", "Functie in het lichaam"],
                  [["eiwitten", None], ["vetten", None], ["water", None], ["calcium", None],
                   ["ijzer", None]],
                  "Eiwitten bouwen en herstellen weefsels. Vetten slaan energie op, isoleren tegen de "
                  "kou en helpen de vitaminen A, D, E en K opnemen. Water levert geen energie maar maakt "
                  "alle reacties mogelijk. Calcium maakt botten en tanden stevig. Ijzer is nodig voor "
                  "hemoglobine, dat zuurstof vervoert.", WL),
                 ("waar", "Verzadigde vetten zijn bij kamertemperatuur meestal vast.", True),
                 ("open", "Wat is kenmerkend voor een onverzadigd vetzuur, en wat merk je daarvan aan "
                          "tafel?",
                  "Er zit minstens één dubbele binding in de keten, waardoor die een knik krijgt. Daardoor "
                  "is zo'n vet meestal vloeibaar, zoals olijfolie.", 4),
             ]),
        dict(kop="Reken op het etiket",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"Een pot van \(400\) g bevat \(25\) g suiker per \(100\) g. Hoeveel suiker zit er in de "
                          "hele pot?", r"\(100\) g", W),
                 ("kort", r"Een pak van \(150\) g bevat \(12\) g vet per \(100\) g. Hoeveel vet zit er in het pak?",
                  r"\(18\) g", W),
                 ("kort", r"Een fles van \(1{,}5\) L bevat \(10\) g suiker per \(100\) mL. Hoeveel suiker in de hele "
                          "fles?", r"\(150\) g", W),
                 ("open", r"Op een etiket staat suiker \(36\) g per \(100\) g. Wat zegt dat over het product, in "
                          "gewone woorden?",
                  r"Ruim een derde van het product is suiker. Per honderd gram zit er dus \(36\) gram suiker "
                  "in.", 3),
             ]),
        dict(kop="Nutriscore of ecoscore?",
             opdracht="Schrijf nutriscore, ecoscore of beide.",
             oefeningen=[
                 ("rij", [("veel zout in het product", "nutriscore"),
                          ("overgevlogen uit een ander werelddeel", "ecoscore"),
                          ("een goed recycleerbare verpakking", "ecoscore")], None, WL),
                 ("rij", [("veel vezels in het product", "nutriscore"),
                          ("een biologische teelt", "ecoscore"),
                          ("staat vooraan op de verpakking", "beide")], None, WL),
                 ("open", "Twee koekjes hebben dezelfde nutriscore, maar een andere ecoscore. Hoe kan "
                          "dat?",
                  "De nutriscore kijkt naar de samenstelling, en die is bij beide gelijk. De ecoscore "
                  "kijkt naar de hele levenscyclus: teelt, verwerking, verpakking en vervoer kunnen sterk "
                  "verschillen.", 4),
                 ("waar", "Een product met nutriscore A mag je in onbeperkte hoeveelheden eten.", False),
             ]),
        dict(kop="Allergenen en verplichte vermeldingen",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("open", "Hoe herken je de allergenen in een ingrediëntenlijst, en waarom staan ze zo?",
                  "Ze staan in het vet of met hoofdletters. Zo vallen ze op voor wie allergisch is, en de "
                  "wet verplicht dat voor de veertien bekendste allergenen.", 3),
                 ("open", "Op een pak staat: kan sporen van noten bevatten. Betekent dat dat er noten in "
                          "zitten?",
                  "Niet met opzet. In dezelfde fabriek worden ook noten verwerkt, en er kan onbedoeld een "
                  "spoor in terechtkomen. Voor wie zwaar allergisch is, is dat een echt risico.", 4),
                 ("open", "Noem de vijf dingen die verplicht in de voedingswaardetabel staan.",
                  "Energie, vet, koolhydraten, eiwit en zout.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-dosis-en-concentratie-van-stoffen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Dosis en concentratie van stoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke concentratie-uitdrukking is dit?",
             opdracht="Schrijf massaprocent, volumeprocent of massaconcentratie.",
             oefeningen=[
                 ("rij", [(r"\(8\) g per liter", "massaconcentratie"), (r"\(5\,\%\) vol", "volumeprocent"),
                          (r"\(3\) g per \(100\) g", "massaprocent")], None, WL),
                 ("rij", [(r"\(40\,\%\) alcohol", "volumeprocent"), (r"\(12\) mg per liter", "massaconcentratie"),
                          (r"\(20\) g zout per \(100\) g pekel", "massaprocent")], None, WL),
             ]),
        dict(kop="Reken de hoeveelheid alcohol uit",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"Een glas van \(200\) mL bier met \(5\,\%\) vol. Hoeveel mL alcohol?", r"\(10\) mL", W),
                 ("kort", r"Een glas van \(150\) mL wijn met \(12\,\%\) vol. Hoeveel mL alcohol?", r"\(18\) mL", W),
                 ("kort", r"Een glaasje van \(40\) mL sterke drank met \(40\,\%\) vol. Hoeveel mL alcohol?",
                  r"\(16\) mL", W),
                 ("open", "Welk van die drie glazen bevat het meeste alcohol? Zet ze op volgorde en leg "
                          "uit waarom het percentage alleen niet volstaat.",
                  r"Wijn \(18\) mL, sterke drank \(16\) mL, bier \(10\) mL. Het percentage zegt alleen hoe sterk de "
                  "drank is; je moet het volume erbij rekenen om de hoeveelheid te kennen.", 4),
             ]),
        dict(kop="Reken de concentratie uit",
             opdracht="Reken en zet de juiste eenheid erbij.",
             oefeningen=[
                 ("kort", r"\(25\) g zout in \(500\) g oplossing. Wat is het massaprocent?", r"\(5\,\%\)", W),
                 ("kort", r"\(10\) g suiker opgelost tot \(250\) mL. Wat is de massaconcentratie?", r"\(40\) g/L", W),
                 ("kort", r"\(6\) g zout opgelost tot \(2\) L. Wat is de massaconcentratie?", r"\(3\) g/L", W),
                 ("kort", r"Een oplossing van \(25\) g/L. Hoeveel stof zit er in \(400\) mL?", r"\(10\) g", W),
             ]),
        dict(kop="Dosis of concentratie?",
             opdracht="Schrijf dosis of concentratie.",
             oefeningen=[
                 ("rij", [(r"er zit \(32\) g suiker per \(100\) g in de pot", "concentratie"),
                          (r"ik heb vandaag \(40\) g suiker gegeten", "dosis"),
                          (r"deze drank is \(5\,\%\) vol", "concentratie")], None, WW),
                 ("open", "Iemand zegt: deze drank is zwak, dus ik kan er zoveel van drinken als ik wil. "
                          "Wat is er fout aan die gedachte?",
                  "De concentratie is laag, maar de dosis hangt ook af van hoeveel je drinkt. Veel van "
                  "iets zwaks kan evenveel of meer alcohol opleveren dan weinig van iets sterks.", 4),
             ]),
        dict(kop="Reken met de ADI",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"ADI = \(5\) mg per kg per dag. Een kind van \(24\) kg. Hoeveel mag het per dag?",
                  r"\(120\) mg", W),
                 ("kort", r"ADI = \(3\) mg per kg per dag. Een volwassene van \(80\) kg. Hoeveel per dag?",
                  r"\(240\) mg", W),
                 ("open", "Waarom staat een ADI altijd per kilogram lichaamsgewicht en niet als één vast "
                          "getal?",
                  "Een stof verdeelt zich over je hele lichaam. In een groter lichaam wordt dezelfde "
                  "hoeveelheid meer verdund, dus een zwaarder lichaam verdraagt meer.", 4),
             ]),
        dict(kop="Lees de LD50",
             opdracht="Vergelijk en besluit.",
             oefeningen=[
                 ("tabel", ["Stof", "LD50 in mg per kg", "Giftiger of minder giftig?"],
                  [["stof A", r"\(20\)", None], ["stof B", r"\(800\)", None], ["stof C", r"\(4000\)", None]],
                  "Stof A is het giftigst, dan B, dan C: hoe lager de LD50, hoe giftiger.", "130px"),
                 ("kort", r"LD\(50 = 1500\) mg per kg. Welke dosis is dat voor iemand van \(50\) kg, in gram?",
                  r"\(75\) g", W),
                 ("waar", "Een stof met een hoge LD50 kan je in elke hoeveelheid gebruiken.", False),
                 ("open", "Een ADI geldt voor elke dag, een LD50 voor één keer. Waarom is dat verschil "
                          "belangrijk?",
                  "Een kleine hoeveelheid die je elke dag binnenkrijgt, kan zich in je lichaam ophopen. "
                  "Een LD50 zegt alleen iets over één zware dosis in één keer.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-duurzame-chemie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Duurzame chemie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke keten is dit?",
             opdracht="Schrijf lineair, keteneconomie met recyclage of cradle to cradle.",
             oefeningen=[
                 ("rij", [("een wegwerpbeker gaat na één keer in de vuilnisbak", "lineair"),
                          ("glazen flessen worden versmolten tot nieuw glas", "keteneconomie met recyclage"),
                          ("een tapijt wordt ontworpen om er later tapijt van te maken", "cradle to cradle")],
                  None, WL),
                 ("kort", "Hoe heet een lineaire keten ook, met twee Engelse namen?",
                  "take make waste en cradle to grave", WL),
             ]),
        dict(kop="Hergebruik, recyclage, upcycling of downcycling?",
             opdracht="Schrijf de juiste term.",
             oefeningen=[
                 ("rij", [("een petfles wordt een bloempot", "downcycling"),
                          ("een oude ladder wordt een boekenrek", "upcycling"),
                          ("een glazen fles wordt opnieuw gevuld", "hergebruik")], None, WL),
                 ("rij", [("oud papier wordt nieuw papier", "recyclage"),
                          ("een kleed gaat naar de tweedehandswinkel", "hergebruik")], None, WL),
             ]),
        dict(kop="Zet de ladder van Lansink op volgorde",
             opdracht=r"Nummer van \(1\), het best, tot \(5\), het slechtst.",
             oefeningen=[
                 ("tabel", ["Nummer", "Trede"],
                  [[None, "recycleren"], [None, "storten"], [None, "voorkomen dat er afval ontstaat"],
                   [None, "verbranden met energiewinst"], [None, "hergebruiken"]],
                  r"\(1\) = voorkomen dat er afval ontstaat · \(2\) = hergebruiken · \(3\) = recycleren · \(4\) = "
                  r"verbranden met energiewinst · \(5\) = storten", "56px"),
                 ("open", "Waarom staat hergebruiken hoger dan recycleren?",
                  "Bij hergebruik blijft het voorwerp zoals het is, dus er is geen energie nodig om het "
                  "materiaal opnieuw te verwerken.", 3),
             ]),
        dict(kop="Greenwashing of niet?",
             opdracht="Beoordeel en leg uit waaraan je het ziet.",
             oefeningen=[
                 ("open", "Een fles shampoo met een groen blaadje en het woord natuurlijk, zonder verdere "
                          "uitleg.",
                  "Greenwashing. Een blaadje en het woord natuurlijk zijn geen keurmerk en worden door "
                  "niemand gecontroleerd.", 3),
                 ("open", "Een verpakking met een officieel keurmerk en een ecoscore B.",
                  "Geen greenwashing. Een keurmerk en een score worden volgens vaste regels toegekend en "
                  "nagekeken.", 3),
             ]),
        dict(kop="Thermoplast, thermoharder of elastomeer?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Soort", "Crosslinks", "Smelt opnieuw?", "Goed recycleerbaar?"],
                  [["thermoplast", None, None, None], ["thermoharder", None, None, None],
                   ["elastomeer", None, None, None]],
                  "Thermoplast: geen crosslinks, smelt opnieuw, goed recycleerbaar. Thermoharder: veel "
                  "crosslinks, smelt niet, moeilijk recycleerbaar. Elastomeer: weinig crosslinks, smelt "
                  "niet, moeilijk recycleerbaar.", "90px"),
                 ("rij", [("een petfles", "thermoplast"), ("een autoband", "elastomeer"),
                          ("de steel van een pan", "thermoharder")], None, WW),
             ]),
        dict(kop="Biogebaseerd, biodegradeerbaar of composteerbaar?",
             opdracht="Schrijf de juiste term of leg het verschil uit.",
             oefeningen=[
                 ("rij", [("gemaakt uit maïszetmeel", "biogebaseerd"),
                          ("bacteriën breken het af", "biodegradeerbaar"),
                          ("breekt af binnen een afgesproken tijd", "composteerbaar")], None, WL),
                 ("open", "Een zakje is biogebaseerd. Mag je het daarom bij het gft gooien? Leg uit.",
                  "Nee. Biogebaseerd zegt alleen waaruit het gemaakt is, niet of het afbreekt. Alleen een "
                  "zakje met een composteerbaar-keurmerk mag bij het gft, en soms enkel industrieel.", 4),
                 ("open", "Waarom is afbreken tot microplastics niet hetzelfde als verdwijnen?",
                  "De deeltjes blijven bestaan, alleen kleiner. Ze komen in water, bodem en voeding "
                  "terecht.", 3),
             ]),
        dict(kop="Energie, waterstof en water",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("uit aardgas, de CO₂ komt vrij", "grijze waterstof"),
                          ("uit aardgas, de CO₂ wordt opgeslagen", "blauwe waterstof"),
                          ("uit water met hernieuwbare stroom", "groene waterstof")], None, WL),
                 ("rij", [("water van het toilet", "zwart water"),
                          ("water van bad en wasmachine", "grijs water"),
                          ("zuiver, drinkbaar water", "wit water")], None, WW),
                 ("rij", [("zon en wind", "hernieuwbaar"), ("steenkool en aardgas", "fossiel"),
                          ("uranium", "kernenergie")], "Welke energievorm?", WW),
                 ("open", "Een bedrijf noemt zijn productie CO₂-negatief. Wat betekent dat, en waarin is "
                          "dat anders dan CO₂-neutraal?",
                  "CO₂-negatief haalt meer koolstofdioxide uit de lucht dan het uitstoot. Bij neutraal "
                  "heffen uitstoot en opname elkaar precies op.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektromagnetisme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Elektromagnetisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Trekt de magneet dit aan?",
             opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("een koperen buis", "nee"), ("een nikkelen munt", "ja"),
                          ("een stalen vork", "ja")], None, W),
                 ("rij", [("een aluminium blikje", "nee"), ("een gouden ring", "nee"),
                          ("een ijzeren schroef", "ja")], None, W),
                 ("open", "Een sorteerinstallatie scheidt stalen blikjes van aluminium blikjes met een "
                          "magneet. Leg uit hoe dat kan.",
                  "Staal bestaat grotendeels uit ijzer en is dus ferromagnetisch. Aluminium is dat niet, "
                  "dus de stalen blikjes worden opgepikt en de aluminium blijven liggen.", 4),
             ]),
        dict(kop="Aantrekken of afstoten?",
             opdracht="Schrijf aantrekken of afstoten.",
             oefeningen=[
                 ("rij", [("noord tegenover noord", "afstoten"), ("noord tegenover zuid", "aantrekken"),
                          ("zuid tegenover zuid", "afstoten")], None, W),
             ]),
        dict(kop="Weissgebieden",
             opdracht="Leg uit in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom is een gewone spijker geen magneet, en hoe maak je er toch een van?",
                  "De weissgebieden wijzen alle richtingen uit en heffen elkaar op. Strijk je er een "
                  "magneet steeds in dezelfde richting over, dan gaan ze op één lijn staan en is de "
                  "spijker een magneet.", 4),
                 ("open", "Een kind laat een magneet vallen en daarna trekt die niets meer aan. Wat is "
                          "er gebeurd?",
                  "De schok heeft de weissgebieden door elkaar gegooid. Ze heffen elkaar nu weer op, dus "
                  "naar buiten is er geen magnetisme meer.", 4),
                 ("waar", "Een magneet verliest zijn magnetisme als je hem sterk verhit.", True),
                 ("open", "Een paperclip hangt aan een magneet en trekt zelf een tweede paperclip aan. "
                          "Hoe heet dat verschijnsel en hoe werkt het?",
                  "Magnetische influentie. De weissgebieden in de paperclip gaan onder invloed van het "
                  "veld op één lijn staan, en daardoor wordt de paperclip zelf tijdelijk een magneet.", 4),
             ]),
        dict(kop="Breek de magneet",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("open", "Je breekt een staafmagneet in drie stukken. Hoeveel polen heeft elk stuk? Leg "
                          "uit.",
                  "Elk stuk heeft twee polen, een noord- en een zuidpool. Een losse pool bestaat niet, "
                  "want ook in de stukken staan de weissgebieden nog op één lijn.", 4),
             ]),
        dict(kop="Het aardmagnetisch veld",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("bij de geografische noordpool", "de magnetische zuidpool"),
                          ("bij de geografische zuidpool", "de magnetische noordpool")],
                  "Welke pool ligt daar?", WL),
                 ("open", "Leg uit waarom de noordpool van een kompasnaald naar het geografische noorden "
                          "wijst.",
                  "Daar ligt de magnetische zuidpool van het aardveld. Ongelijksoortige polen trekken aan, "
                  "dus de noordpool van de naald wordt er naartoe getrokken.", 4),
             ]),
        dict(kop="Permanente magneet of elektromagneet?",
             opdracht="Schrijf permanent of elektromagneet.",
             oefeningen=[
                 ("rij", [("een bordmagneet", "permanent"), ("een relais", "elektromagneet"),
                          ("een kompasnaald", "permanent")], None, WW),
                 ("rij", [("een elektrische deurbel", "elektromagneet"),
                          ("een kastsluiting", "permanent"),
                          ("een automatische zekering", "elektromagneet")], None, WW),
                 ("open", "Waarom kiest men voor een schrootkraan een elektromagneet?",
                  "Zet je de stroom af, dan laat de magneet de lading los. Met een permanente magneet "
                  "kreeg je het schroot er niet meer af.", 3),
             ]),
        dict(kop="De spoel",
             opdracht="Beoordeel, reken en leg uit.",
             oefeningen=[
                 ("rij", [("meer wikkelingen", "sterker"), ("een grotere stroom", "sterker"),
                          ("een ijzeren kern erin", "sterker")],
                  "Wordt de elektromagneet sterker of zwakker?", WW),
                 ("open", "Waarvoor dient de ijzeren kern precies?",
                  "De weissgebieden in de kern gaan mee op één lijn staan en versterken zo het veld van de "
                  "spoel.", 3),
                 ("open", "Je draait de twee draden van een elektromagneet om. Wat verandert er?",
                  "De stroomrichting keert om, dus de noordpool en de zuidpool wisselen van plaats. De "
                  "sterkte blijft gelijk.", 3),
                 ("waar", "Rond een draad waar stroom door loopt, staat geen magneetveld.", False),
                 ("open", "Welke vorm heeft het veld rond een rechte stroomvoerende draad, en hoe vind je "
                          "de zin ervan?",
                  "Cirkels rond de draad. Met je rechterduim langs de stroom wijzen je vingers de zin van "
                  "de veldlijnen aan.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-golven-geluid-en-het-elektromagnetisch-spectrum-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Golven, geluid en het elektromagnetisch spectrum",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort golf?",
             opdracht="Schrijf mechanisch of elektromagnetisch, en transversaal of longitudinaal.",
             oefeningen=[
                 ("rij", [("geluid", "mechanisch, longitudinaal"),
                          ("zichtbaar licht", "elektromagnetisch, transversaal"),
                          ("een golf in een touw", "mechanisch, transversaal")], None, WL),
                 ("rij", [("radiogolven", "elektromagnetisch, transversaal"),
                          ("een golf op het water", "mechanisch, transversaal")], None, WL),
                 ("open", "Waarom hoor je niets in het vacuüm, maar zie je er wel iets?",
                  "Geluid is een mechanische golf en heeft een middenstof nodig die kan trillen. Licht is "
                  "elektromagnetisch en reist ook door het lege heelal.", 4),
             ]),
        dict(kop="Reken met de formules",
             opdracht=r"Gebruik \(f = 1 / T\) en \(v = \lambda \cdot f\). Schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"\(T = 0{,}02\) s. Wat is de frequentie?", r"\(50\) Hz", W),
                 ("kort", r"\(T = 0{,}005\) s. Wat is de frequentie?", r"\(200\) Hz", W),
                 ("kort", r"\(\lambda = 4\) m en \(f = 85\) Hz. Wat is de golfsnelheid?", r"\(340\) m/s", W),
                 ("kort", r"\(v = 340\) m/s en \(f = 680\) Hz. Wat is de golflengte?", r"\(0{,}5\) m", W),
                 ("kort", r"\(f = 25\) Hz. Wat is de periode?", r"\(0{,}04\) s", W),
             ]),
        dict(kop="Wat verandert er aan de golf?",
             opdracht="Schrijf amplitude, frequentie of allebei.",
             oefeningen=[
                 ("rij", [("je zet de muziek luider", "amplitude"),
                          ("je zingt een hogere toon", "frequentie"),
                          ("je slaat harder op dezelfde snaar", "amplitude")], None, WW),
             ]),
        dict(kop="Breking, buiging of weerkaatsing?",
             opdracht="Schrijf de juiste eigenschap.",
             oefeningen=[
                 ("rij", [("een regenboog", "breking"), ("een echo in een tunnel", "weerkaatsing"),
                          ("je hoort iemand achter een hoek", "buiging")], None, WW),
                 ("rij", [("sonar op een schip", "weerkaatsing"),
                          ("een rietje lijkt geknikt in het water", "breking"),
                          ("echolocatie bij een vleermuis", "weerkaatsing")], None, WW),
                 ("open", "Waarom hoor je iemand achter een hoek wel, maar zie je die niet?",
                  "Geluidsgolven zijn ongeveer even lang als de opening of de hoek en buigen dus sterk af. "
                  "Lichtgolven zijn veel korter en buigen daar nauwelijks om.", 4),
             ]),
        dict(kop="Reken met decibel",
             opdracht="Reken en leg uit.",
             oefeningen=[
                 ("kort", r"Op \(2\) m van een box meet je \(94\) dB. Hoeveel meet je op \(4\) m?", r"\(88\) dB", W),
                 ("kort", r"En hoeveel op \(8\) m?", r"\(82\) dB", W),
                 ("kort", "De geluidsintensiteit wordt vier keer kleiner. Hoeveel decibel zakt het "
                          "niveau?", r"\(6\) dB", W),
                 ("open", "Noem drie dagelijkse geluiden en zet ze op volgorde van zacht naar luid, met "
                          "een schatting in decibel.",
                  r"Bijvoorbeeld fluisteren rond \(30\) dB, een gesprek rond \(60\) dB en een drilboor rond "
                  r"\(100\) dB.", 3),
             ]),
        dict(kop="Je gehoor beschermen",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("rij", [("de gehoordrempel", r"\(0\) dB"), ("de gevaargrens", r"\(80\) dB"),
                          ("de pijndrempel", r"\(120\) dB")], "Welk niveau hoort hierbij?", W),
                 ("waar", "Gehoorschade door lawaai geneest altijd volledig.", False),
                 ("open", "Leg uit waarom niet.",
                  "De haarcellen in het binnenoor raken beschadigd, en die groeien bij de mens niet "
                  "terug.", 3),
                 ("open", "Twee vrienden staan op een fuif. De ene blijft tien minuten vooraan, de "
                          "andere twee uur achteraan. Wie loopt het grootste risico? Leg uit.",
                  "Dat hangt af van het niveau én de tijd samen. Vooraan is het veel luider, maar twee uur "
                  "is twintig keer langer; de blootstelling van de tweede kan dus zwaarder zijn. Het "
                  "veiligst is oordopjes plus afstand.", 4),
             ]),
        dict(kop="Zet het spectrum op volgorde",
             opdracht=r"Nummer van \(1\), de laagste energie, tot \(7\), de hoogste.",
             oefeningen=[
                 ("tabel", ["Nummer", "Soort straling"],
                  [[None, "zichtbaar licht"], [None, "radiogolven"], [None, "gammastraling"],
                   [None, "infraroodstraling"], [None, "röntgenstraling"], [None, "microgolven"],
                   [None, "ultraviolette straling"]],
                  r"\(1\) = radiogolven · \(2\) = microgolven · \(3\) = infraroodstraling · \(4\) = zichtbaar licht · "
                  r"\(5\) = ultraviolette straling · \(6\) = röntgenstraling · \(7\) = gammastraling", "56px"),
                 ("waar", "Hoe hoger de frequentie, hoe korter de golflengte.", True),
             ]),
        dict(kop="Welke straling zit hierin?",
             opdracht="Schrijf de soort straling.",
             oefeningen=[
                 ("rij", [("een microgolfoven", "microgolven"), ("een afstandsbediening", "infrarood"),
                          ("een röntgenfoto", "röntgenstraling")], None, WW),
                 ("rij", [("een zonnebank", "uv-straling"), ("een warmtelamp", "infrarood"),
                          ("een wifinetwerk", "radiogolven")], None, WW),
                 ("open", "Welke stralingen zijn ioniserend, en waarom is dat gevaarlijk?",
                  "Hoogenergetische uv, röntgen en gamma. Ze maken elektronen uit atomen los en beschadigen "
                  "daardoor moleculen, ook het DNA in je cellen.", 4),
                 ("open", "Hoe bescherm je je tegen uv en hoe tegen röntgenstraling?",
                  "Tegen uv met kleding, schaduw, een zonnebril en zonnecrème. Tegen röntgenstraling met "
                  "een loodschort.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kernfysica-kernenergie-en-straling-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kernfysica, kernenergie en straling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Vul de kern aan",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Nuclide", "Massagetal A", "Atoomnummer Z", "Aantal neutronen"],
                  [[r"koolstof-\(12\)", r"\(12\)", r"\(6\)", None], [r"zuurstof-\(16\)", r"\(16\)", r"\(8\)", None],
                   [r"uranium-\(238\)", r"\(238\)", r"\(92\)", None], [r"waterstof-\(3\)", r"\(3\)", r"\(1\)", None]],
                  r"Koolstof-\(12\): \(6\) neutronen. Zuurstof-\(16\): \(8\) neutronen. Uranium-\(238\): \(146\) neutronen. "
                  r"Waterstof-\(3\): \(2\) neutronen.", "70px"),
                 ("open", r"Koolstof-\(12\) en koolstof-\(14\) zijn isotopen. Wat hebben ze gemeen en waarin "
                          "verschillen ze?",
                  r"Ze hebben hetzelfde aantal protonen, zes, en zijn dus allebei koolstof. Koolstof-\(14\) "
                  "heeft twee neutronen meer.", 4),
             ]),
        dict(kop="Reken met de halfwaardetijd",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", r"Halfwaardetijd \(5\) dagen. Welk deel is er na \(20\) dagen over?", "een zestiende", W),
                 ("kort", r"Je begint met \(800\) g. Halfwaardetijd \(3\) jaar. Hoeveel na \(9\) jaar?", r"\(100\) g", W),
                 ("kort", "Na hoeveel halfwaardetijden is er nog een vierde over?", "twee", W),
                 ("waar", "Hoe langer de halfwaardetijd, hoe sneller een stof onschadelijk is.", False),
             ]),
        dict(kop="Fusie of splijting?",
             opdracht="Schrijf fusie of splijting.",
             oefeningen=[
                 ("rij", [("waterstofkernen smelten samen in de zon", "fusie"),
                          ("een uraniumkern breekt in twee stukken", "splijting"),
                          ("lichte kernen worden één zwaardere", "fusie")], None, WW),
                 ("open", "Waarom komt er bij beide reacties energie vrij?",
                  "Na de reactie is de totale massa een beetje kleiner dan ervoor. Dat massaverlies is "
                  "omgezet in energie, volgens de formule van Einstein.", 4),
             ]),
        dict(kop="De kerncentrale",
             opdracht="Zet op volgorde en vul aan.",
             oefeningen=[
                 ("tabel", ["Nummer", "Stap"],
                  [[None, "de turbine draait de generator"],
                   [None, "uraniumkernen splijten in de splijtstaven"],
                   [None, "de stoom drijft een turbine aan"],
                   [None, "het water wordt verhit tot stoom"]],
                  r"\(1\) = uraniumkernen splijten in de splijtstaven · \(2\) = het water wordt verhit tot stoom · "
                  r"\(3\) = de stoom drijft een turbine aan · \(4\) = de turbine draait de generator", "56px"),
                 ("rij", [("remmen de kettingreactie af", "de regelstaven"),
                          ("houdt straling binnen bij een ongeval", "de betonnen koepel"),
                          ("de splijtstof zelf", "uranium")], None, WL),
                 ("open", "Iemand zegt: in een kerncentrale drijft de kernreactie rechtstreeks de "
                          "generator aan. Verbeter die uitspraak.",
                  "De reactie maakt alleen warmte. Die warmte verdampt water, de stoom drijft een turbine "
                  "aan en de turbine draait de generator.", 4),
                 ("rij", [("kortlevend laag- en middelactief", "categorie A"),
                          ("langlevend laag- en middelactief", "categorie B"),
                          ("hoogactief", "categorie C")], "Welke categorie afval?", WW),
             ]),
        dict(kop="Alfa, bèta of gamma?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Straling", "Wat het is", "Tegengehouden door"],
                  [["alfa", None, None], ["bèta", None, None], ["gamma", None, None]],
                  "Alfa: een heliumkern, tegengehouden door een blad papier. Bèta: een elektron, "
                  "tegengehouden door een plaatje aluminium. Gamma: elektromagnetische straling met heel "
                  "hoge energie, tegengehouden door een dikke laag lood of beton.", WL),
                 ("waar", "Alfastraling dringt het diepst door van de drie.", False),
                 ("open", "Alfastraling komt niet eens door een blad papier, en toch is ze gevaarlijk als "
                          "je de stof inslikt. Leg uit.",
                  "Binnen in je lichaam zit er geen papier of huid tussen. Alfastraling geeft al haar "
                  "energie over een korte afstand af en heeft het grootste ioniserend vermogen.", 4),
             ]),
        dict(kop="Schrijf het verval op",
             opdracht="Vul het nieuwe massagetal en atoomnummer in.",
             oefeningen=[
                 ("rij", [(r"radium-\(226\) zendt een alfadeeltje uit", r"\(A = 222\) en \(Z = 86\)"),
                          (r"thorium-\(234\) zendt een bètadeeltje uit", r"\(A = 234\) en \(Z = 91\)")],
                  r"Radium heeft \(Z = 88\), thorium heeft \(Z = 90\).", WL),
                 ("open", "Een kern heeft te veel neutronen. Welke straling zendt ze uit en wat gebeurt "
                          "er in de kern?",
                  "Bètamin-straling. Een neutron verandert in een proton en er vertrekt een elektron, dus "
                  "het atoomnummer stijgt met één en het massagetal blijft gelijk.", 4),
             ]),
        dict(kop="Bestraling of besmetting?",
             opdracht="Schrijf bestraling, inwendige besmetting of uitwendige besmetting.",
             oefeningen=[
                 ("rij", [("je staat naast een gesloten bron", "bestraling"),
                          ("je ademt radioactief stof in", "inwendige besmetting"),
                          ("er komt stof op je huid", "uitwendige besmetting")], None, WL),
                 ("open", "Waarom is een besmetting lastiger dan een bestraling?",
                  "Bij bestraling stopt het zodra je weggaat. Bij besmetting draag je de bron mee, dus de "
                  "bestraling gaat door tot de stof vervalt of verwijderd is.", 4),
                 ("rij", [("de geabsorbeerde dosis", "gray"), ("de equivalente dosis", "sievert"),
                          ("de effectieve dosis", "sievert")], "Welke eenheid?", W),
                 ("open", "Waarom krijgt alfastraling een veel hogere stralingsweegfactor dan "
                          "gammastraling?",
                  "Bij dezelfde opgenomen energie richt alfastraling veel meer schade aan, omdat ze alles "
                  "over een korte afstand afgeeft. Daarom weegt ze twintig keer zwaarder.", 4),
                 ("open", "Noem de drie manieren om je tegen ioniserende straling te beschermen.",
                  "Afstand nemen, iets zwaars als afscherming tussenzetten, en de tijd bij de bron zo kort "
                  "mogelijk houden.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meten-en-onderzoeken-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Veilig werken, meten en onderzoeken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Goed of fout gewerkt?",
             opdracht="Schrijf goed of fout, en bij fout wat er moet gebeuren.",
             oefeningen=[
                 ("rij", [("gemorst product meteen opkuisen", "goed"),
                          ("scherven met de hand oprapen", "fout"),
                          ("het toestel aanzetten met natte handen", "fout")], None, W),
                 ("rij", [("glaswerk na gebruik schoonmaken", "goed"),
                          ("een product overgieten in een drankfles", "fout"),
                          ("lange haren vastbinden bij de brander", "goed")], None, W),
                 ("open", "Waarom is een product overgieten in een lege drankfles gevaarlijk?",
                  "Er staat dan geen etiket meer op, dus niemand weet wat erin zit. Iemand kan ervan "
                  "drinken.", 3),
             ]),
        dict(kop="H-zin of P-zin?",
             opdracht="Schrijf H of P.",
             oefeningen=[
                 ("rij", [("veroorzaakt ernstig oogletsel", "H"),
                          ("beschermende handschoenen dragen", "P"),
                          ("verwijderd houden van open vuur", "P")], None, W),
             ]),
        dict(kop="Welk toestel en welk bereik?",
             opdracht="Kies het toestel en beoordeel.",
             oefeningen=[
                 ("rij", [("de duur van een reactie", "een chronometer"),
                          ("de massa van een poeder", "een balans"),
                          ("de druk in een vat", "een manometer")], None, WW),
                 ("rij", [("de spanning over een lamp", "een multimeter"),
                          ("het geluidsniveau in een zaal", "een decibelmeter"),
                          ("de temperatuur van water", "een thermometer")], None, WW),
                 ("open", r"Je moet \(1{,}5\) kg wegen en je balans gaat tot \(200\) g. Wat doe je, en wat doe je "
                          "zeker niet?",
                  "Je zoekt een balans met een groter meetbereik. Je legt het niet toch voorzichtig op de "
                  "balans: de waarde klopt dan niet en het toestel kan stuk gaan.", 4),
                 ("open", r"Je wil een verschil van \(0{,}2^{\circ}\text{C}\) meten. Welke thermometer kies je en waarom?",
                  r"Een met streepjes van \(0{,}1^{\circ}\text{C}\). Het toestel moet nauwkeuriger zijn dan het verschil dat "
                  "je wil zien.", 3),
             ]),
        dict(kop="Zet de eenheden om",
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [(r"\(3{,}2\) km in m", r"\(3200\) m"), (r"\(750\) mg in g", r"\(0{,}75\) g"),
                          (r"\(5\) MJ in J", r"\(5\,000\,000\) J")], None, WW),
                 ("rij", [(r"\(0{,}4\) m in mm", r"\(400\) mm"), (r"\(2500\) g in kg", r"\(2{,}5\) kg"),
                          (r"\(8\) µm in m", r"\(0{,}000008\) m")], None, WW),
                 ("kort", "Hoeveel is een nano van een eenheid?", "een miljardste", W),
             ]),
        dict(kop="Welk verband?",
             opdracht="Schrijf recht evenredig of omgekeerd evenredig.",
             oefeningen=[
                 ("rij", [("verdubbelt de ene, dan verdubbelt de andere", "recht evenredig"),
                          ("verdubbelt de ene, dan halveert de andere", "omgekeerd evenredig"),
                          ("hun product blijft gelijk", "omgekeerd evenredig")], None, WL),
                 ("open", "Hoe herken je een recht evenredig verband aan een grafiek?",
                  "Je krijgt een rechte lijn die door de oorsprong gaat. Is de ene grootheid nul, dan is "
                  "de andere dat ook.", 3),
             ]),
        dict(kop="Bouw een onderzoek op",
             opdracht="Lees de situatie en schrijf je antwoord.",
             oefeningen=[
                 ("tekst", "Je wil weten of planten sneller groeien met meer licht."),
                 ("open", "Schrijf een goede onderzoeksvraag voor dit onderzoek.",
                  "Bijvoorbeeld: groeit een tuinkersplantje sneller bij acht uur licht per dag dan bij "
                  "vier uur licht per dag? De vraag is scherp afgebakend en met metingen te beantwoorden.",
                  3),
                 ("open", "Schrijf er een hypothese bij.",
                  "Bijvoorbeeld: ik verwacht dat de plantjes bij acht uur licht per dag hoger worden dan "
                  "bij vier uur. Een hypothese is een verwachting die je kan testen.", 3),
                 ("open", "Noem drie dingen die je in beide groepen gelijk moet houden, en leg uit "
                          "waarom.",
                  "Bijvoorbeeld dezelfde soort zaadjes, dezelfde hoeveelheid water en dezelfde "
                  "temperatuur. Verander je meer dan één factor, dan weet je niet wat het verschil "
                  "veroorzaakt heeft.", 4),
                 ("open", "Je metingen spreken je hypothese tegen. Wat doe je?",
                  "Je noteert wat je gemeten hebt en schrijft je conclusie zoals de data ze geven. Je past "
                  "je metingen nooit aan. Je hypothese was gewoon fout, en dat is ook een resultaat.", 4),
             ]),
        dict(kop="Ontwerpen en STEM",
             opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["Nummer", "Stap van het ontwerpen"],
                  [[None, "oplossingen bedenken en samenvoegen"], [None, "het probleem definiëren"],
                   [None, "evalueren en bijsturen"], [None, "criteria opstellen"],
                   [None, "het probleem in deelproblemen splitsen"]],
                  r"\(1\) = het probleem definiëren · \(2\) = criteria opstellen · \(3\) = het probleem in "
                  r"deelproblemen splitsen · \(4\) = oplossingen bedenken en samenvoegen · \(5\) = evalueren en "
                  "bijsturen", "56px"),
                 ("open", "Een stad wil de luchtkwaliteit verbeteren. Welke STEM-domeinen heb je nodig, "
                          "en waarvoor elk?",
                  "Wetenschappelijke kennis over de stoffen in de lucht, technische kennis over "
                  "meettoestellen en filters, en wiskundige kennis om de metingen te verwerken. Een "
                  "totaaloplossing vraagt kennis uit meerdere hoeken.", 4),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-bevruchting-en-de-ontwikkeling-van-embryo-en-foetus-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Hou de vier hormonen aan hun eerste letter: FSH laat rijpen, LH lost de eisprong "
                   "uit, progesteron houdt het slijmvlies dik. En hou apart wie ze maakt.",
            waarom=[
                "Let op FSH en LH: de F van FSH past bij follikel, en LH geeft de piek die de "
                "eisprong uitlokt. Zo verwar je de twee niet.",
                "Let op het geel lichaam: dat is wat er van de follikel overblijft na de eisprong, en "
                "het maakt het progesteron. Valt het weg, dan komt de menstruatie.",
            ],
        ),
        dict(
            aanpak="Reken altijd van achteren naar voren: de eisprong valt ongeveer veertien dagen "
                   "vóór de volgende menstruatie. Trek dus veertien van de cyclusduur af.",
            waarom=[
                "Let erop dat je 30 min 14 rekent en niet 14 zelf neemt. Bij een cyclus van 28 dagen "
                "vallen de twee manieren samen, en daarom denken veel mensen dat dag 14 altijd "
                "klopt.",
                None,
                "Noem dat de tweede helft bij bijna elke vrouw ongeveer even lang is. Dat is de "
                "reden, en het verklaart ook waarom een kalendermethode weinig betrouwbaar is.",
            ],
        ),
        dict(
            aanpak="Vergelijk de twee cellen op hun taak: de zaadcel moet reizen, de eicel moet "
                   "voeden. Alles aan hun bouw volgt daaruit.",
            waarom=[
                "Let op beide: een kern hebben ze allebei, want elk van de twee brengt de helft van "
                "het erfelijk materiaal aan.",
                "Let op de mitochondriën in het middenstuk van de zaadcel: dat is haar motor. De "
                "eicel geeft bij de bevruchting wel haar mitochondriën mee, en de zaadcel niet.",
            ],
        ),
        dict(
            aanpak="Volg de weg in de tijd: eerst de eisprong, dan de reis, dan de versmelting, en "
                   "pas een week later de innesteling.",
            waarom=[
                "Let erop dat het bevruchtingsmembraan vóór het versmelten van de kernen komt. Eerst "
                "wordt de deur gesloten, dan gebeurt wat erbinnen moet gebeuren.",
            ],
        ),
        dict(
            aanpak="De placenta is een uitwisselingsplaats. Zet de stoffen in twee kolommen: wat "
                   "naar de vrucht gaat en wat eruit moet.",
            waarom=[
                None,
                "Noem beide voordelen: de bloedgroepen en de afweer. En noem dat de stoffen wel door "
                "het vlies gaan, anders lijkt het alsof er niets passeert.",
                "Let erop dat het twee slagaders en één ader zijn. Een slagader voert hier bloed van "
                "de vrucht weg, dus zuurstofarm, en de ader brengt zuurstofrijk bloed binnen.",
            ],
        ),
        dict(
            aanpak="Vier vragen over wat van buiten bij de vrucht raakt. Hou vast dat de eerste "
                   "weken het gevoeligst zijn, ook als de vrouw nog niets weet.",
            waarom=[
                None,
                "Niet waar: ook meeroken brengt schadelijke stoffen binnen. Daarom geldt het advies "
                "voor de hele omgeving van een zwangere vrouw.",
                "Noem dat de aanleg al in de eerste weken gebeurt. Dat is het hele antwoord, en het "
                "is de reden dat men foliumzuur aanraadt van zodra er een kinderwens is.",
                "Let op de drie ziekteverwekkers: elk heeft een eigen weg naar het lichaam. "
                "Rodehond via de lucht, toxoplasmose via vlees of een kattenbak, zika via een mug.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vruchtbaarheid-anticonceptie-en-kinderwens-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier soorten. Vraag je bij elk middel af wat het doet: de vruchtbare dagen "
                   "mijden, de hormonen regelen, de weg versperren, of een blijvende ingreep.",
            waarom=[
                "Let op het pessarium: dat is een barrière, net als een condoom. Alleen beschermt "
                "een pessarium niet tegen soa, en een condoom wel.",
                "Let op sterilisatie: dat is een ingreep en bedoeld als blijvend. Dat onderscheidt "
                "ze van alle andere middelen in deze reeks.",
                "Let erop dat drie van de natuurlijke methodes hier door elkaar staan: temperatuur, "
                "ovulatie en kalender. Alle drie proberen ze de vruchtbare dagen te vinden.",
            ],
        ),
        dict(
            aanpak="Zet de middelen op een tijdlijn: elke dag, elke maand, elke drie maanden, "
                   "enkele jaren. Hoe langer het werkt, hoe minder er fout kan gaan.",
            waarom=[
                "Let erop dat juist de duur de betrouwbaarheid in de praktijk bepaalt. Een staafje "
                "kan je niet vergeten, een pil wel, en dat komt in de vierde reeks terug.",
            ],
        ),
        dict(
            aanpak="Bij een advies geef je altijd twee dingen: wat je aanraadt en waarom. Lees in de "
                   "situatie wat de persoon zelf belangrijk vindt.",
            waarom=[
                "Noem dat de pil geen enkele soa tegenhoudt. Dat is de kern: zwangerschap en soa "
                "zijn twee verschillende risico's en vragen soms twee middelen.",
                "Noem dat het koperspiraaltje zonder hormonen werkt en jaren meegaat. Beide eisen uit "
                "de vraag komen zo in je antwoord.",
                "Noem beide redenen: er komen al zaadcellen vrij vóór de zaadlozing, en het hangt van "
                "het juiste moment af. Eén reden is maar de helft.",
            ],
        ),
        dict(
            aanpak="Hou twee cijfers apart: hoe goed een middel werkt als het perfect gebruikt wordt, "
                   "en hoe goed in het echte leven. Dat verschil is de kern van deze reeks.",
            waarom=[
                "Niet waar: een zaaddodend middel is alleen gebruikt te onbetrouwbaar. Het is "
                "bedoeld als aanvulling op een barrière, zoals een pessarium.",
                None,
                "Noem beide kanten van het verschil, met een voorbeeld zoals een vergeten pil. Zo "
                "wordt duidelijk dat het verschil niet in het middel zit maar in het gebruik.",
            ],
        ),
        dict(
            aanpak="Drie behandelingen, in stijgende hulp: KI brengt het sperma binnen, IVF "
                   "bevrucht buiten het lichaam, ICSI prikt één zaadcel in de eicel.",
            waarom=[
                "Let op het verschil tussen KI en IVF: bij KI gebeurt de bevruchting nog in het "
                "lichaam. Enkel bij IVF en ICSI gebeurt ze in het labo.",
                "Niet waar: het embryo wordt na enkele dagen in de baarmoeder geplaatst en groeit "
                "daar verder. Het labo doet enkel het eerste stukje.",
                "Noem beide redenen: niet elke eicel raakt bevrucht en niet elk embryo groeit door. "
                "Daarom werkt men met meerdere.",
                "Noem dat er meerdere eicellen rijpen. Dat is het verband tussen de stimulatie en de "
                "meerling, en het is waarom men vandaag meestal één embryo terugplaatst.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke factor af waar ze op werkt: op de zaadcellen, op de cyclus, of "
                   "op beide. Warmte raakt de man, ondergewicht de cyclus van de vrouw.",
            waarom=[
                "Let erop dat roken bij beiden speelt. Dat wordt vaak enkel bij de vrouw gelegd, en "
                "dat is niet juist.",
                "Noem dat zaadcellen enkele graden koeler rijpen. Daarom is een laptop op de schoot "
                "of een lange warme bak niet onschuldig.",
                "Noem allebei: dat de behandeling de vruchtbaarheid kan aantasten en dat invriezen "
                "haar kans bewaart. Dat tweede is wat de vraag zoekt.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-van-dna-naar-eiwit-genexpressie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee paren: A hoort bij T, G hoort bij C. Enkel bij RNA komt er op de plaats van "
                   "thymine een U te staan.",
            waarom=[
                None,
                "Let erop dat je bij RNA twee dingen tegelijk doet: de complementaire base nemen en "
                "T door U vervangen. Vergeet die tweede stap niet.",
            ],
        ),
        dict(
            aanpak="Drie verschillen tussen DNA en RNA: de suiker, de base en het aantal strengen. "
                   "Alles wat ze gemeen hebben, hoort bij beide.",
            waarom=[
                "Let op guanine: die staat in beide. Enkel thymine en uracil verschillen, en de "
                "andere drie basen zijn in DNA en RNA dezelfde.",
                None,
            ],
        ),
        dict(
            aanpak="Vier woorden in een rij: een gen is het stuk DNA, een allel is een versie van dat "
                   "gen, het genotype is wat je hebt, het fenotype is wat je ziet.",
            waarom=[
                "Let op het verschil tussen een gen en een allel: het gen is de plaats, het allel is "
                "de versie. Iedereen heeft het gen voor oogkleur, en de allelen verschillen.",
                "Let op lengte als fenotype: je ziet ze, dus is ze fenotype, ook al bepaalt het "
                "genotype haar mee. De volgende reeksen gaan daar verder op in.",
            ],
        ),
        dict(
            aanpak="Vier stappen, en bij elke stap ook de plaats. Hou vast dat het lezen in de kern "
                   "gebeurt en het bouwen buiten de kern.",
            waarom=[
                "Let erop dat je bij elke stap ook de plaats moet geven. De grens van de kern is de "
                "kern van dit schema: het origineel blijft binnen, de kopie gaat buiten.",
                "Noem dat het DNA het origineel is. Dezelfde gedachte als bij een belangrijk "
                "document: je neemt een kopie mee en laat het origineel in de kluis.",
            ],
        ),
        dict(
            aanpak="Drie vragen over hetzelfde idee: hetzelfde DNA betekent niet hetzelfde resultaat. "
                   "Welke genen aanstaan en wat de omgeving doet, beslissen mee.",
            waarom=[
                "Noem dat in elke cel andere genen aanstaan. Dat is het hele antwoord, en het woord "
                "daarvoor is genexpressie.",
                "Noem twee oorzaken, zoals gevraagd, en noem het woord omgeving. Genotype en omgeving "
                "samen geven het fenotype.",
                "Niet waar: een litteken zit in je lichaamscellen en niet in je geslachtscellen. Dat "
                "is dezelfde fout als die van Lamarck met de giraf.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: blijf je binnen wat de natuur zelf kan kruisen (veredeling), "
                   "of grijp je rechtstreeks in het DNA in (modificatie)?",
            waarom=[
                "Let op de derde: DNA van twee soorten samenbrengen kan de natuur niet door kruisen. "
                "Dat is dus altijd modificatie.",
                "Noem van beide technieken wat ze doet, zoals de vraag een verschil vraagt. De grens "
                "van wat kruisbaar is, is het scherpste onderscheid.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-overerving-van-kenmerken-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee woorden volstaan: diploïd is dubbel, haploïd is half. Lichaamscellen zijn "
                   "diploïd, geslachtscellen haploïd.",
            waarom=[
                "Let erop dat een eicel en een zaadcel elk 23 chromosomen hebben. Samen geven ze de "
                "46 van de volgende vraag.",
                None,
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: gaat het om groeien of herstellen (mitose), of om "
                   "geslachtscellen maken (meiose)? Variatie hoort altijd bij de meiose.",
            waarom=[
                None,
                "Let op de tweede: variatie tussen de nakomelingen komt van de meiose, door de "
                "crossing-over en de toevallige verdeling. Mitose geeft juist identieke cellen.",
            ],
        ),
        dict(
            aanpak="Teken het vierkant met de gameten van de ene ouder bovenaan en die van de andere "
                   "links. Lees daarna af hoeveel vakjes elk genotype heeft.",
            waarom=[
                "Let erop dat de twee middelste vakjes hetzelfde genotype geven, Aa. Daarom komt de "
                "verhouding op 25, 50 en 25 procent uit.",
                None,
                "Let erop dat de dragers de heterozygote helft zijn. Zij tonen het kenmerk niet, en "
                "toch geven zij het door.",
                "Noem het genotype van beide ouders en leg uit waarom. Een kind met bloedgroep O "
                "moet van elke ouder een O gekregen hebben, en dat verraadt hun genotype.",
            ],
        ),
        dict(
            aanpak="Drie soorten overerving, met één vraag: toont de heterozygoot het dominante "
                   "kenmerk, een tussenvorm, of allebei volledig?",
            waarom=[
                "Let op het verschil tussen intermediair en codominant: bij roze mengen de twee, bij "
                "bloedgroep AB zijn beide volledig aanwezig. Mengen tegenover naast elkaar.",
            ],
        ),
        dict(
            aanpak="Eén gegeven draagt de hele reeks: het gen ligt op het X-chromosoom, en een jongen "
                   "heeft maar één X.",
            waarom=[
                None,
                "Noem alle drie de stappen: het gen op de X, één X bij een jongen, en de tweede X bij "
                "een meisje. Dan is je uitleg volledig.",
                None,
                "Noem de helft en leg uit waarom: een zoon krijgt zijn enige X van zijn moeder. Een "
                "schema met XX en XY maakt het snel duidelijk.",
            ],
        ),
        dict(
            aanpak="Bij elke mutatie twee vragen: in welke cel zit ze, en is dat erg? Enkel in een "
                   "geslachtscel gaat ze mee naar de volgende generatie.",
            waarom=[
                "Let erop dat een mutatie in een huidcel niet overerft. Ze kan daar wel kanker "
                "veroorzaken, en dat is een ander soort gevolg.",
                "Niet waar: veel mutaties doen niets, en af en toe is er een voordelig. Zonder die "
                "voordelige mutaties zou er geen evolutie zijn.",
                "Noem twee oorzaken en één bescherming, zoals gevraagd. Let erop dat ook het gewone "
                "kopiëren van DNA fouten maakt, zonder dat er iets van buiten bij komt.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-biologische-evolutie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie woorden, drie vragen: dezelfde oorsprong (homoloog), dezelfde functie "
                   "(analoog), of een overblijfsel zonder taak (rudimentair)?",
            waarom=[
                "Let op de insectenvleugel: die vliegt wel maar is heel anders gebouwd. Dezelfde "
                "functie zonder gemeenschappelijke oorsprong is analoog.",
                "Let op de walvis: haar vin is homoloog met onze arm, en haar heupbeentjes zijn "
                "rudimentair. Beide samen zijn een sterk argument dat haar voorouders op het land "
                "liepen.",
            ],
        ),
        dict(
            aanpak="Vier vakgebieden: botten zijn anatomie, embryo's zijn embryologie, fossielen zijn "
                   "paleontologie, en DNA of eiwitten zijn moleculaire biologie.",
            waarom=[
                "Let op het tweede: dezelfde vier basen bij alle leven is een moleculair argument, en "
                "het is een van de sterkste die er zijn.",
                None,
            ],
        ),
        dict(
            aanpak="Een evolutieboom leest van de splitsingen naar de takken. Hoe recenter de "
                   "splitsing, hoe meer twee soorten op elkaar lijken.",
            waarom=[
                None,
                "Niet waar: een boom toont verwantschap en geen rangorde. Boven of onder in de "
                "tekening is een kwestie van opmaak.",
                "Noem dat elke tak die nog leeft, even lang bezig is. Dat is wat deze uitspraak "
                "weerlegt, en het is een van de hardnekkigste misverstanden over evolutie.",
                "Noem dat het twee onafhankelijke soorten gegevens zijn. Daarom is zo'n overeenkomst "
                "een echt argument en geen toeval.",
            ],
        ),
        dict(
            aanpak="Hou bij deze vragen twee dingen vast: meer verschil in DNA betekent langer "
                   "geleden, en gemeenschappelijke voorouders zijn geen bestaande dieren.",
            waarom=[
                None,
                "Noem de gemeenschappelijke voorouder en noem dat die uitgestorven is. Zeggen dat de "
                "uitspraak fout is, volstaat niet; de vraag vraagt een verbetering.",
                None,
                "Noem dat kleine veranderingen zich opstapelen. De ouderdom van de aarde is wat de "
                "theorie de ruimte geeft, en zonder die tijd zou ze niet werken.",
            ],
        ),
        dict(
            aanpak="Hier gaat het over wat wetenschap is: een verklaring die aan waarnemingen "
                   "getoetst kan worden en daardoor kan bijgestuurd worden.",
            waarom=[
                "Niet waar: de theorie is sindsdien aangevuld met de genetica en het DNA. Juist dat "
                "bijsturen is wat haar wetenschappelijk maakt.",
                "Noem dat de theorie te toetsen is en de andere verklaring niet. Dat is het "
                "onderscheid, en het gaat dus niet over wie er meer in gelooft.",
                "Noem de voorwaarden voor fossilisatie. Dat verklaart de gaten in het fossielenbestand "
                "zonder dat die gaten tegen de theorie pleiten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-natuurlijke-selectie-en-het-ontstaan-van-soorten-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag scheidt de twee: verandert het individu tijdens zijn leven (Lamarck) of "
                   "verandert de samenstelling van de populatie (Darwin)?",
            waarom=[
                "Let erop dat variatie en overvloedige nakomelingen bij Darwin horen. Dat zijn de "
                "twee vaststellingen waarmee hij begon.",
                None,
            ],
        ),
        dict(
            aanpak="Alle drie de uitspraken maken dezelfde fout: het organisme verandert zelf. Schrijf "
                   "ze om zodat de selectie tussen bestaande verschillen kiest.",
            waarom=[
                "Noem beide delen: hoe het wel gaat, en dat uitrekken je geslachtscellen niet "
                "verandert. De vraag vraagt ook wat eraan fout was.",
                "Noem dat de mutatie er al was, door toeval. Een mutatie ontstaat niet omdat ze "
                "nodig is, en dat is de kern van deze verbetering.",
                "Noem dat de vlinders zelf niet veranderden. Het is de verhouding in de populatie die "
                "verschoof, en dat is iets heel anders.",
            ],
        ),
        dict(
            aanpak="Selectie heeft twee dingen nodig: verschillen die er al zijn, en erfelijkheid. "
                   "Mist er een van de twee, dan werkt ze niet.",
            waarom=[
                "Niet waar: nieuwe eigenschappen komen van mutaties. De selectie kiest enkel tussen "
                "wat er al is.",
                "Waar: een kenmerk dat niet overerft, verdwijnt met het individu. Daarom werkt training "
                "of een litteken niet mee in de evolutie.",
                "Niet waar: aanpassen gebeurt over generaties en niet met een bedoeling. Woorden als "
                "willen of proberen horen niet in een uitleg over evolutie.",
                "Noem de erfelijke variatie. Dat is waarom een kleine populatie kwetsbaar is, los van "
                "jacht of ziekte.",
            ],
        ),
        dict(
            aanpak="Vijf soorten isolatie: in de ruimte, in de tijd, in het gedrag, in het leefgebied "
                   "en in de bouw. Vraag je af wat de twee groepen precies belet om te paren.",
            waarom=[
                None,
                "Let op het verschil tussen ecologisch en geografisch: bij ecologisch leven de groepen "
                "in hetzelfde gebied maar op een andere plek erin, bij geografisch is er een echte "
                "scheiding.",
                "Noem dat de genen anders blijven mengen. Dat is waarom isolatie nodig is, en het is "
                "dezelfde gedachte als bij de eerste reeks van deze bundel.",
            ],
        ),
        dict(
            aanpak="Hou vast dat het woord vruchtbaar in de definitie staat. Nakomelingen krijgen is "
                   "niet genoeg; die nakomelingen moeten zich zelf kunnen voortplanten.",
            waarom=[
                "Noem het woord vruchtbaar en noem het besluit. Zonder dat woord lijkt het muildier "
                "juist een bewijs dat het één soort is.",
            ],
        ),
        dict(
            aanpak="Hou bij de menswording de eerste stap vast: rechtop lopen, en daardoor vrije "
                   "handen. De rest volgt daarop.",
            waarom=[
                "Let erop dat het rechtop lopen vóór de grote hersenen komt. Dat verrast vaak, en "
                "toch wijzen de fossielen het zo uit.",
                "Noem drie kenmerken, zoals gevraagd. Let erop dat het gaat om wat we gemeen hebben, "
                "niet om wat ons onderscheidt.",
                "Waar: ze leefden tienduizenden jaren naast elkaar, en in ons DNA zitten nog sporen "
                "van de neanderthaler. De ene is dus niet de voorouder van de andere.",
                "Noem alle drie de lagen: soorten, variatie binnen een soort, en leefgebieden. Dat "
                "tweede is wat deze bundel met de rest verbindt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-productlabels-pictogrammen-en-risico-s-van-stoffen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees bij elke omschrijving wat er precies gebeurt. Vreten is bijtend, een brand "
                   "voeden is oxiderend, zelf vlam vatten is ontvlambaar.",
            waarom=[
                "Let op het verschil tussen ontvlambaar en oxiderend: het eerste brandt zelf, het "
                "tweede laat iets anders beter branden. Een oxiderende stof maakt een brandje "
                "onblusbaar.",
                "Let op het verschil tussen bijtend en irriterend: bijtend vreet weg en geeft blijvende "
                "schade, irriterend geeft roodheid die weer overgaat.",
            ],
        ),
        dict(
            aanpak="H van hazard zegt wat er kan gebeuren, P van precaution zegt wat jij moet doen. "
                   "Een gebod of een verbod is dus altijd een P-zin.",
            waarom=[
                None,
                "Let erop dat ook een gevaar voor het milieu een H-zin is. Een H-zin gaat niet enkel "
                "over jouw lichaam.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk stuk afval af of er een gevaar aan zit. Alles met een "
                   "gevaarpictogram is klein gevaarlijk afval, ook als het bijna leeg is.",
            waarom=[
                "Let op de halfvolle fles verf: die hoort bij het kga en niet bij het restafval. Een "
                "lege verfpot is iets anders dan een pot met een restje erin.",
                None,
                "Noem beide delen: dat ze samen giftige gassen vormen, en dat ze allebei naar het kga "
                "moeten. Enkel waarschuwen voor het mengen is maar de helft.",
            ],
        ),
        dict(
            aanpak="Hou één gedachte vast bij de driehoek met het cijfer: hij zegt uit wat de "
                   "verpakking gemaakt is, en niets over wat er daarna met haar gebeurt.",
            waarom=[
                None,
                "Niet waar: de code zegt enkel welke kunststof het is. Of er een inzameling en een "
                "verwerking voor bestaat, hangt van de gemeente en van de markt af.",
                "Noem het woord identificatiecode. Dat is waarom zo'n logo geen belofte is, en het is "
                "een vorm van greenwashing wanneer men het zo gebruikt.",
            ],
        ),
        dict(
            aanpak="Vergelijk de temperatuur van de kamer met het smelt- en kookpunt van de stof. "
                   "Ligt 20 graden ertussen, dan is de stof vloeibaar.",
            waarom=[
                "Let erop dat je twee grenzen nodig hebt: boven het smeltpunt en onder het kookpunt. "
                "Bij ijzer liggen beide ver boven de kamertemperatuur.",
                "Noem het lage kookpunt. Dat verklaart zowel het snelle drogen als waarom je met "
                "aceton niet bij een vlam werkt.",
                "Niet waar: een laag kookpunt betekent veel damp, en damp is precies wat vlam vat of "
                "wat je inademt. Het kookpunt zegt dus wel iets over het gevaar.",
            ],
        ),
        dict(
            aanpak="Eén regel: soort lost soort op. Vet en olie vragen een organisch oplosmiddel, "
                   "zout en suiker lossen op in water.",
            waarom=[
                "Let op de suikersiroop: die is kleverig en lijkt vettig, maar suiker lost gewoon op "
                "in water. Kleverig is niet hetzelfde als vettig.",
                None,
                "Geef bij de regel ook een voorbeeld, zoals de vraag vraagt. Met zout en olie naast "
                "elkaar is het meteen duidelijk.",
            ],
        ),
        dict(
            aanpak="Hou de drie groepen vast met een voorbeeld uit de keuken: azijn en citroen zijn "
                   "zuur, water is neutraal, ontstopper en bleekwater zijn basisch.",
            waarom=[
                None,
                "Let erop dat je de kleuren aan de twee kanten van de schaal koppelt: rood is zuur, "
                "groen tot geel is basisch. Rode kool werkt dus als een indicator, net als lakmoes.",
                "Noem dat het zuur met het aluminium reageert. Dat is hetzelfde soort reactie als "
                "tussen een zuur en een metaal in het labo.",
                "Noem allebei: lang spoelen met water, en niet neutraliseren. Dat tweede is wat deze "
                "vraag toetst, want neutraliseren maakt extra warmte.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voedingsbestanddelen-en-etiketten-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes voedingsmiddelen, elk met één hoofdbestanddeel. Vraag je af waarvoor je dat "
                   "middel eet: voor energie, voor bouwstof of voor kleine hoeveelheden.",
            waarom=[
                None,
                "Let op de linzen: ook plantaardige voeding levert eiwit. Eiwit komt niet enkel uit "
                "vlees, en dat is bij een vegetarische voeding de kern.",
            ],
        ),
        dict(
            aanpak="Een voedingsmiddel is wat op je bord ligt, een voedingsstof is wat erin zit. Vraag "
                   "je af of je het zo zou kunnen eten.",
            waarom=[
                "Let op fructose en ijzer: dat zijn stoffen in een middel, geen middelen op zich. Een "
                "appel is het middel, de fructose erin de stof.",
                None,
            ],
        ),
        dict(
            aanpak="Tel de bouwstenen: één is mono, twee is di, veel is poly. Hoe langer de keten, hoe "
                   "trager de glucose in je bloed komt.",
            waarom=[
                None,
                "Noem de keten van zetmeel en noem het geleidelijke. Dat is het verschil, en het is "
                "dezelfde gedachte als bij trage en snelle suikers.",
                "Noem van beide momenten waarom het past. De vraag vraagt naar de orde, dus je "
                "antwoord moet die twee aan elkaar koppelen.",
            ],
        ),
        dict(
            aanpak="Vijf bestanddelen met elk een eigen taak. Hou vast dat water en mineralen geen "
                   "energie leveren en toch onmisbaar zijn.",
            waarom=[
                "Let op de vetten: naast energie leveren ze ook isolatie en helpen ze de vitaminen A, "
                "D, E en K opnemen. Dat laatste wordt vaak vergeten.",
                None,
                "Noem de dubbele binding en noem wat je eraan merkt, zoals de vraag twee dingen "
                "vraagt. De knik in de keten is de reden dat olie vloeibaar is.",
            ],
        ),
        dict(
            aanpak="Reken altijd in twee stappen: eerst hoeveel keer 100 gram of 100 milliliter er in "
                   "de verpakking zit, dan die factor maal de hoeveelheid.",
            waarom=[
                "Let erop dat 400 gram vier keer 100 gram is, dus vier keer 25. Zo hoef je geen "
                "kruisproduct te maken.",
                "Let op de anderhalve keer: 150 gram is 1,5 keer 100 gram, dus 1,5 maal 12. Een "
                "verpakking kleiner dan 100 gram geeft dus een getal onder de waarde van het etiket.",
                "Let erop dat je eerst de liters naar milliliter zet: 1,5 liter is 1500 milliliter, "
                "dus vijftien keer 100. Wie dat vergeet, zit een factor tien of meer fout.",
                "Noem het in gewone woorden, zoals de vraag vraagt: ruim een derde. Een percentage "
                "omzetten naar een breuk maakt een etiket pas echt leesbaar.",
            ],
        ),
        dict(
            aanpak="Twee scores met twee vragen: de nutriscore gaat over wat er in het product zit, de "
                   "ecoscore over hoe het gemaakt en vervoerd is.",
            waarom=[
                None,
                "Let op de derde: beide scores staan vooraan op de verpakking, en dat is precies "
                "waarom mensen ze verwarren.",
                "Noem van beide scores waar ze naar kijkt. Dat de ecoscore de hele levenscyclus "
                "bekijkt, is de kern van het antwoord.",
                "Niet waar: ook een gezond product eet je met maat. De nutriscore vergelijkt producten "
                "binnen dezelfde groep, en ze zegt niets over de hoeveelheid.",
            ],
        ),
        dict(
            aanpak="Op een etiket staat niet alles wat je zou willen weten, maar wat de wet oplegt. "
                   "Hou dat onderscheid vast bij alle drie de vragen.",
            waarom=[
                "Noem beide delen: hoe je ze herkent en dat de wet het oplegt. Het gaat om de veertien "
                "bekendste allergenen, van gluten tot noten en schaaldieren.",
                "Noem dat het niet met opzet is en dat het voor wie zwaar allergisch is toch telt. Die "
                "twee samen zijn het antwoord.",
                "Noem alle vijf, zoals gevraagd. Onder vet staat meestal ook hoeveel verzadigd vet, en "
                "onder koolhydraten hoeveel suikers; die twee bijlijnen maken het etiket pas "
                "bruikbaar.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-dosis-en-concentratie-van-stoffen-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de eenheid, die verraadt alles: gram per liter is een massaconcentratie, "
                   "procent vol is volumeprocent, en gram per 100 gram is massaprocent.",
            waarom=[
                None,
                "Let op het eerste: bij drank staat het percentage altijd voor volume en niet voor "
                "massa. Daarom staat er vol bij.",
            ],
        ),
        dict(
            aanpak="Reken altijd het volume maal het percentage, en zet het percentage eerst om naar "
                   "een getal onder één. Zo komt er milliliter alcohol uit.",
            waarom=[
                "Let erop dat 5 procent van 200 gewoon 10 is. Je kan ook door twintig delen, want 5 "
                "procent is een twintigste.",
                None,
                None,
                "Noem de orde en de reden, zoals de vraag twee dingen vraagt. Dat het glas wijn meer "
                "alcohol bevat dan het glaasje sterke drank, is het hele punt van deze reeks.",
            ],
        ),
        dict(
            aanpak="Hou twee formules apart: massaprocent is de massa van de stof gedeeld door de "
                   "massa van de oplossing, massaconcentratie is de massa gedeeld door het volume in "
                   "liter.",
            waarom=[
                None,
                "Let erop dat je de milliliter eerst naar liter zet: 250 milliliter is 0,25 liter, en "
                "10 gedeeld door 0,25 is 40. Wie met 250 rekent, zit een factor duizend fout.",
                None,
                "Let erop dat je hier omgekeerd rekent: de concentratie maal het volume in liter. 400 "
                "milliliter is 0,4 liter, dus 25 maal 0,4.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: zegt het getal iets over het product (concentratie) of over "
                   "wat jij binnenkreeg (dosis)?",
            waarom=[
                None,
                "Noem beide delen: de concentratie is laag, en de dosis hangt van de hoeveelheid af. "
                "Dit is de kerngedachte van de hele bundel.",
            ],
        ),
        dict(
            aanpak="De ADI staat per kilogram, dus vermenigvuldig met het gewicht. Let op de eenheid "
                   "van je antwoord: milligram.",
            waarom=[
                None,
                None,
                "Noem dat de stof zich over het hele lichaam verdeelt. Daarom staat een dosis bij "
                "geneesmiddelen voor kinderen ook per kilogram.",
            ],
        ),
        dict(
            aanpak="Bij de LD50 is laag gevaarlijk: het is de dosis waarbij de helft sterft, dus hoe "
                   "minder er nodig is, hoe giftiger de stof.",
            waarom=[
                "Let erop dat de orde omgekeerd is aan wat je verwacht. Een laag getal betekent hier "
                "een hoog gevaar.",
                "Let op de omzetting naar gram: 1500 maal 50 is 75 000 milligram, en dat is 75 gram. "
                "Wie niet omzet, antwoordt in milligram en krijgt een getal dat niets zegt.",
                "Niet waar: een hoge LD50 betekent enkel dat er veel nodig is om acuut te sterven. "
                "Over schade op lange termijn zegt ze niets, en daarvoor dient de ADI.",
                "Noem het ophopen in je lichaam. Dat is het verschil tussen een dagelijkse dosis en "
                "één keer veel, en daarom bestaan er twee aparte maten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-duurzame-chemie-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Drie ketens: één die eindigt in de vuilnisbak, één die het materiaal terugbrengt, "
                   "en één waarbij het product al voor dat terugbrengen ontworpen is.",
            waarom=[
                "Let op het verschil tussen de tweede en de derde: bij recyclage maak je er iets van, "
                "bij cradle to cradle is het product er van het begin voor ontworpen.",
                "Let erop dat beide namen hetzelfde zeggen: nemen, maken, weggooien, en van de wieg "
                "tot het graf. Cradle to cradle is daar het antwoord op.",
            ],
        ),
        dict(
            aanpak="Twee vragen bij elk geval: blijft het voorwerp bestaan (hergebruik) of wordt het "
                   "materiaal verwerkt (recyclage)? En gaat de kwaliteit vooruit of achteruit?",
            waarom=[
                "Let op de bloempot en het boekenrek: beide zijn een tweede leven, maar van een "
                "petfles maak je geen fles meer en van een ladder maak je iets van meer waarde.",
                None,
            ],
        ),
        dict(
            aanpak="De ladder gaat van voorkomen tot storten. Onthou de orde met één gedachte: hoe "
                   "minder bewerking er nodig is, hoe hoger de trap.",
            waarom=[
                "Let erop dat verbranden met energiewinst nog boven storten staat. Je haalt er dan "
                "toch nog warmte of stroom uit.",
                "Noem dat er geen energie nodig is om het materiaal opnieuw te verwerken. Dat is de "
                "reden, en ze geldt voor elke stap van de ladder.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk label af wie het controleert. Een woord of een kleur mag iedereen "
                   "op een pak zetten, een keurmerk niet.",
            waarom=[
                "Noem dat niemand het nakijkt. Dat is waaraan je greenwashing ziet, en niet aan de "
                "kleur zelf.",
                None,
            ],
        ),
        dict(
            aanpak="De crosslinks beslissen alles: geen crosslinks geeft een thermoplast die opnieuw "
                   "smelt, veel crosslinks geeft een thermoharder die dat niet meer kan.",
            waarom=[
                "Let erop dat enkel de thermoplast goed te recycleren is. Dat is dezelfde reden als "
                "waarom een petfles wel in de blauwe zak mag en een pansteel niet.",
                None,
            ],
        ),
        dict(
            aanpak="Drie woorden die op elkaar lijken en iets anders zeggen: waaruit het gemaakt is, "
                   "of het afbreekt, en of het binnen een afgesproken tijd afbreekt.",
            waarom=[
                None,
                "Noem dat biogebaseerd niets zegt over afbreken, en noem het keurmerk. Zonder dat "
                "keurmerk hoort een zakje niet bij het gft, hoe groen het ook kleurt.",
                "Noem dat de deeltjes blijven bestaan en in water, bodem en voeding komen. Afbreken "
                "en verdwijnen zijn twee verschillende dingen.",
            ],
        ),
        dict(
            aanpak="Drie reeksen kleuren en soorten. Hou vast dat de kleur van waterstof over de "
                   "productie gaat, en niet over het gas zelf.",
            waarom=[
                "Let erop dat grijs en blauw allebei uit aardgas komen. Het verschil zit enkel in wat "
                "er met de koolstofdioxide gebeurt.",
                "Let op wit water: dat is gewoon drinkbaar water. Grijs water kan je hergebruiken "
                "voor het toilet of de tuin, zwart water niet.",
                None,
                "Noem beide begrippen, zoals de vraag een verschil vraagt. Negatief is meer dan "
                "neutraal, en het is veel moeilijker te halen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-elektromagnetisme-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Enkel ijzer, nikkel en cobalt worden aangetrokken, en staal omdat het vooral "
                   "ijzer is. Alle andere metalen niet, ook al geleiden ze goed.",
            waarom=[
                "Let op de koperen buis: koper geleidt heel goed en is toch niet magnetisch. "
                "Geleiden en magnetisch zijn hebben niets met elkaar te maken.",
                "Let op aluminium en goud: ook die zijn niet magnetisch. Een magneet is dus een "
                "handige manier om metalen van elkaar te scheiden.",
                "Noem dat staal vooral ijzer bevat. Dat is de reden dat de installatie werkt, en het "
                "verklaart ook waarom aluminium met een heel andere techniek gesorteerd wordt.",
            ],
        ),
        dict(
            aanpak="Eén regel, zoals bij ladingen: gelijke polen stoten af, ongelijke trekken aan.",
            waarom=[
                "Let erop dat zuid tegenover zuid even hard afstoot als noord tegenover noord. Het "
                "gaat om gelijk of ongelijk, niet om welke pool.",
            ],
        ),
        dict(
            aanpak="Hou één beeld vast: kleine gebiedjes die elk een richting hebben. Staan ze door "
                   "elkaar, dan merk je niets; staan ze op één lijn, dan heb je een magneet.",
            waarom=[
                "Noem beide delen: waarom hij het niet is, en hoe je het verandert. Strijken in "
                "steeds dezelfde richting is wat de gebieden op één lijn zet.",
                "Noem dat de schok de gebieden door elkaar gooit. Dat is hetzelfde effect als sterk "
                "verhitten, maar met geweld in plaats van met warmte.",
                None,
                "Noem het woord influentie en noem dat het tijdelijk is. Haal je de magneet weg, dan "
                "valt de tweede paperclip er weer af.",
            ],
        ),
        dict(
            aanpak="Hou vast dat een losse pool niet bestaat. Breek je een magneet, dan krijg je "
                   "telkens weer twee polen per stuk.",
            waarom=[
                "Noem het aantal en de reden. Elk stuk heeft twee polen, dus drie stukken hebben zes "
                "polen; de weissgebieden staan er nog altijd op één lijn.",
            ],
        ),
        dict(
            aanpak="Hou vast dat de aarde omgekeerd ligt dan de namen laten denken: bij het "
                   "geografische noorden ligt een magnetische zuidpool.",
            waarom=[
                None,
                "Noem beide stappen: daar ligt de magnetische zuidpool, en ongelijke polen trekken "
                "aan. Zonder die tweede stap is het antwoord niet volledig.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: werkt het altijd (permanent) of enkel zolang er stroom loopt "
                   "(elektromagneet)? Alles wat moet kunnen schakelen, is een elektromagneet.",
            waarom=[
                None,
                "Let op de automatische zekering: die moet de stroom kunnen onderbreken, dus zit er "
                "een elektromagneet in die bij te veel stroom aan de schakelaar trekt.",
                "Noem dat de lading loskomt als de stroom afgaat. Dat is het hele voordeel, en het is "
                "ook het nadeel: bij stroomuitval valt het schroot naar beneden.",
            ],
        ),
        dict(
            aanpak="Een spoel wordt op drie manieren sterker: meer wikkelingen, meer stroom, of een "
                   "ijzeren kern. De zin van het veld hangt enkel van de stroomrichting af.",
            waarom=[
                "Let erop dat alle drie sterker geven. Hier zit geen valstrik in de richting; de "
                "vraag is of je de drie factoren kent.",
                "Noem dat de weissgebieden in de kern meedoen. De kern maakt geen eigen veld, hij "
                "versterkt dat van de spoel.",
                "Noem allebei: de polen wisselen en de sterkte blijft gelijk. Dat tweede wordt vaak "
                "vergeten.",
                "Niet waar: rond elke stroomvoerende draad staat een magneetveld, in cirkels. Dat is "
                "precies waarop een elektromagneet berust.",
                "Noem de cirkels en de rechterhandregel. Met je duim langs de stroom wijzen je "
                "vingers de zin aan, en bij een spoel wijst je duim dan naar de noordpool.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-golven-geluid-en-het-elektromagnetisch-spectrum-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee vragen bij elke golf: heeft ze een middenstof nodig (mechanisch) of niet "
                   "(elektromagnetisch), en trillen de deeltjes in de richting van de golf "
                   "(longitudinaal) of dwars erop (transversaal)?",
            waarom=[
                "Let op geluid: dat is de enige van de drie die longitudinaal is. De deeltjes trillen "
                "er heen en terug in dezelfde richting als de golf reist.",
                None,
                "Noem van beide golven de soort. Het verschil tussen mechanisch en elektromagnetisch "
                "is het hele antwoord.",
            ],
        ),
        dict(
            aanpak="Twee formules: de frequentie is één gedeeld door de periode, en de snelheid is de "
                   "golflengte maal de frequentie. Schrijf eerst op wat je zoekt.",
            waarom=[
                "Let erop dat je deelt: één gedeeld door 0,02 is 50. Een kleine periode geeft een "
                "grote frequentie.",
                None,
                "Let erop dat je hier 340 meter per seconde uitkomt, de snelheid van geluid in lucht. "
                "Dat is een goede controle op je berekening.",
                "Let erop dat je hier deelt in plaats van vermenigvuldigt: de snelheid gedeeld door "
                "de frequentie.",
                "Let erop dat de periode en de frequentie elkaars omgekeerde zijn. Je kan dus altijd "
                "terugrekenen om je antwoord te controleren.",
            ],
        ),
        dict(
            aanpak="Hou de twee grootheden apart: luider is amplitude, hoger is frequentie. Harder "
                   "slaan op dezelfde snaar verandert dus niet de toon.",
            waarom=[
                "Let op de derde: harder slaan geeft een luidere toon en niet een hogere. De "
                "toonhoogte hangt van de snaar af, niet van de kracht.",
            ],
        ),
        dict(
            aanpak="Drie verschijnselen: breking is van richting veranderen in een andere stof, "
                   "weerkaatsing is terugbotsen, buiging is om een hoek of door een opening gaan.",
            waarom=[
                None,
                None,
                "Noem de golflengte in je antwoord. Dat geluid veel langere golven heeft dan licht, "
                "is de reden dat het wel om een hoek buigt.",
            ],
        ),
        dict(
            aanpak="Eén regel voor deze hele reeks: twee keer zo ver betekent vier keer minder "
                   "intensiteit, en dat is ongeveer 6 decibel minder.",
            waarom=[
                "Let erop dat je 6 aftrekt en niet halveert. Van 94 naar 88 decibel is nog altijd "
                "heel luid, en dat is wat de decibelschaal zo verraderlijk maakt.",
                "Let erop dat je van 4 naar 8 meter opnieuw 6 decibel aftrekt. Elke verdubbeling van "
                "de afstand kost dezelfde 6 decibel.",
                None,
                "Geef bij elk geluid een schatting in decibel, zoals gevraagd. Fluisteren, een "
                "gesprek en een machine liggen telkens zowat 30 decibel uit elkaar.",
            ],
        ),
        dict(
            aanpak="Hou de drie grenzen vast: 0 decibel is wat je net hoort, vanaf 80 wordt het "
                   "gevaarlijk, en 120 doet pijn. En onthou dat de tijd even zwaar weegt.",
            waarom=[
                None,
                "Niet waar: schade aan het binnenoor is blijvend. Een tijdelijke piep na een fuif "
                "gaat weg, maar de schade eronder niet altijd.",
                "Noem de haarcellen en noem dat ze niet teruggroeien. Dat is de reden, en het is "
                "waarom oordopjes geen luxe zijn.",
                "Noem beide factoren, het niveau en de tijd, en durf te zeggen dat het van de "
                "combinatie afhangt. Dat is hier het juiste antwoord, geen van de twee alleen.",
            ],
        ),
        dict(
            aanpak="Leer het spectrum als één rij van radio tot gamma. Hoe verder naar rechts, hoe "
                   "hoger de frequentie en de energie, en hoe korter de golf.",
            waarom=[
                "Let erop dat het zichtbare licht precies in het midden van de rij staat, tussen "
                "infrarood en ultraviolet. Alles wat we zien, is dus maar een smalle strook.",
                "Waar: frequentie en golflengte zijn omgekeerd verbonden, want hun product is de "
                "lichtsnelheid. Meer van het ene is dus altijd minder van het andere.",
            ],
        ),
        dict(
            aanpak="Zes toestellen, elk met zijn straling. Een hulpje: warmte is infrarood, draadloos "
                   "is radio, doorkijken is röntgen, bruin worden is uv.",
            waarom=[
                None,
                "Let op de zonnebank en de warmtelamp: de ene werkt met uv en de andere met "
                "infrarood. De eerste is ioniserend en de tweede niet, dus dat verschil is geen "
                "detail.",
                "Noem alle drie de ioniserende soorten en noem waarom het gevaarlijk is. Dat ze "
                "elektronen losmaken en zo het DNA raken, is de kern.",
                "Noem van beide stralingen een eigen bescherming, zoals de vraag twee dingen vraagt. "
                "Zonnecrème helpt niet tegen röntgen, en lood draag je niet op het strand.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kernfysica-kernenergie-en-straling-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het getal achter de naam is het massagetal. Trek daarvan het atoomnummer af, en "
                   "je hebt het aantal neutronen.",
            waarom=[
                "Let erop dat je bij elke stof eerst het atoomnummer moet weten. Koolstof heeft zes "
                "protonen, zuurstof acht, waterstof één en uranium 92.",
                "Noem allebei: wat gelijk is en wat verschilt. Isotopen staan op dezelfde plaats in "
                "het periodiek systeem en hebben een andere massa.",
            ],
        ),
        dict(
            aanpak="Reken met halveringen: deel de verstreken tijd door de halfwaardetijd, en halveer "
                   "dan zo veel keer.",
            waarom=[
                "Let erop dat 20 gedeeld door 5 vier halveringen geeft: een half, een vierde, een "
                "achtste, een zestiende. Tel ze op je vingers.",
                None,
                None,
                "Niet waar, en het is net omgekeerd: een lange halfwaardetijd betekent dat de stof "
                "heel lang actief blijft. Daarom is langlevend afval juist het lastigste.",
            ],
        ),
        dict(
            aanpak="Hou de twee richtingen apart: fusie smelt lichte kernen samen, splijting breekt "
                   "een zware kern. Beide gaan naar het stabiele midden toe.",
            waarom=[
                None,
                "Noem het massaverlies en de formule van Einstein. Dat de massa een beetje kleiner "
                "wordt, is het antwoord op beide reacties tegelijk.",
            ],
        ),
        dict(
            aanpak="Volg in een centrale de weg van de warmte: splijten, water verhitten, stoom, "
                   "turbine, generator. Elke tussenstap telt.",
            waarom=[
                "Let erop dat er twee tussenstappen zijn tussen de kern en de stroom: de stoom en de "
                "turbine. Een kerncentrale is dus eigenlijk een stoomcentrale met een bijzondere "
                "brandstof.",
                None,
                "Noem de hele keten in je verbetering. Enkel zeggen dat het niet rechtstreeks gaat, "
                "is te weinig.",
                "Let erop dat de categorie zowel over de activiteit als over de duur gaat. Categorie "
                "A is kortlevend, en juist daarom het makkelijkst te bergen.",
            ],
        ),
        dict(
            aanpak="Drie soorten straling met drie schermen: papier, aluminium, lood. Hou daarbij "
                   "vast dat weinig doordringen niet weinig gevaarlijk betekent.",
            waarom=[
                None,
                "Niet waar, en het is net omgekeerd: alfastraling dringt het minst diep door en "
                "gamma het diepst. De volgende vraag laat zien waarom alfa toch gevaarlijk is.",
                "Noem beide delen: binnen in je lichaam zit er niets tussen, en alfastraling heeft "
                "het grootste ioniserend vermogen. Dat is waarom radon in een kelder een risico is.",
            ],
        ),
        dict(
            aanpak="Twee regels volstaan: bij alfa gaat A vier omlaag en Z twee, bij bèta blijft A "
                   "gelijk en gaat Z één omhoog.",
            waarom=[
                "Let op het bètaverval: het massagetal verandert niet. Een neutron wordt een proton, "
                "dus het totaal aantal nucleonen blijft hetzelfde.",
                "Noem wat er in de kern gebeurt, zoals de vraag twee dingen vraagt. Een neutron dat "
                "een proton wordt, is de kern van het antwoord.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: blijft de bron buiten je (bestraling) of zit ze op of in je "
                   "lichaam (besmetting)? En hou gray en sievert apart.",
            waarom=[
                None,
                "Noem dat je bij besmetting de bron meedraagt. Daarom wast en kleedt men zich uit na "
                "een besmetting, en dat helpt bij een bestraling niet.",
                "Let erop dat de gray de opgenomen energie meet en de sievert de schade. Twee "
                "verschillende eenheden voor twee verschillende vragen.",
                "Noem dat alfastraling alles over een korte afstand afgeeft. De factor twintig is het "
                "gevolg daarvan en niet de reden.",
                "Noem alle drie, zoals gevraagd: afstand, afscherming en tijd. Dat zijn dezelfde drie "
                "als in het hoofdstuk over straling.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-werken-meten-en-onderzoeken-beyond-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke handeling af wat er kan misgaan, en voor wie. Soms is het gevaar "
                   "niet voor jou maar voor wie later iets vindt.",
            waarom=[
                "Let op de natte handen bij een toestel: water geleidt, dus is dat een risico op een "
                "elektrische schok. Scherven raap je op met een borstel en een blik.",
                "Let op de drankfles: dat is het gevaarlijkste van de zes, want het gevaar komt pas "
                "later en bij iemand anders.",
                "Noem dat er geen etiket meer op staat en dat iemand ervan kan drinken. Beide delen "
                "horen in je antwoord.",
            ],
        ),
        dict(
            aanpak="H van hazard zegt wat de stof doet, P van precaution zegt wat jij moet doen. Een "
                   "gebod of een verbod is altijd een P-zin.",
            waarom=[
                "Let erop dat verwijderd houden van open vuur een opdracht aan jou is, dus een "
                "P-zin, ook al gaat het over brand.",
            ],
        ),
        dict(
            aanpak="Bij meten horen twee vragen: welk toestel, en past het meetbereik en de "
                   "nauwkeurigheid bij wat je wil meten?",
            waarom=[
                None,
                None,
                "Noem allebei: een ander toestel zoeken, en het zeker niet toch proberen. Boven het "
                "meetbereik klopt de waarde niet en kan de balans stuk gaan.",
                "Noem dat het toestel fijner moet zijn dan het verschil dat je zoekt. Met streepjes "
                "van een halve graad zie je een verschil van 0,2 graden nooit.",
            ],
        ),
        dict(
            aanpak="Zet om met de macht van tien die bij het voorvoegsel hoort. Controleer je antwoord "
                   "door het weer terug te zetten.",
            waarom=[
                "Let op de milligram: milli is duizend keer kleiner, dus wordt 750 milligram 0,75 "
                "gram. Het getal wordt kleiner als de eenheid groter wordt.",
                "Let op de micrometer: micro is een miljoenste. 8 micrometer is dus 0,000008 meter, "
                "en dat is ongeveer de grootte van een rode bloedcel.",
                None,
            ],
        ),
        dict(
            aanpak="Twee verbanden met twee proeven: verdubbelt het ene en verdubbelt het andere mee, "
                   "dan recht evenredig; halveert het, dan omgekeerd evenredig.",
            waarom=[
                "Let op de derde: een gelijk blijvend product is precies wat omgekeerd evenredig "
                "betekent. Dat is dezelfde zin als de tweede, anders gezegd.",
                "Noem de oorsprong. Een rechte alleen is niet genoeg; ze moet door nul gaan.",
            ],
        ),
        dict(
            aanpak="Bouw je onderzoek in vier stappen: een scherpe vraag, een hypothese, alles gelijk "
                   "houden behalve één factor, en eerlijk besluiten.",
            waarom=[
                "Let erop dat je vraag een getal en een meting bevat. Groeien planten beter met licht "
                "is te vaag; met uren per dag en centimeter wordt ze meetbaar.",
                "Let erop dat een hypothese een verwachting is en geen vraag. Schrijf ze als een "
                "zin die juist of fout kan blijken.",
                "Noem drie factoren en leg uit waarom, zoals gevraagd. Verander je er twee, dan weet "
                "je achteraf niet welke het verschil maakte.",
                "Noem dat je je metingen nooit aanpast. Een weerlegde hypothese is een resultaat, en "
                "dat is de kern van eerlijk onderzoek.",
            ],
        ),
        dict(
            aanpak="Ontwerpen loopt in een kring: probleem, criteria, delen, oplossen, en dan "
                   "evalueren en opnieuw. STEM is de samenwerking van de vier domeinen.",
            waarom=[
                "Let erop dat de criteria vroeg komen en het evalueren niet het einde is. Na het "
                "bijsturen begin je weer bij je criteria.",
                "Noem van elk domein waarvoor je het nodig hebt, zoals gevraagd. Een lijst zonder die "
                "koppeling is maar de helft van het antwoord.",
            ],
        ),
    ],
)
