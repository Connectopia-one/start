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
                 ("kort", "Een vrouw heeft een cyclus van 30 dagen. Op de hoeveelste dag valt haar "
                          "eisprong ongeveer?", "op dag 16, want de eisprong is ongeveer 14 dagen vóór "
                          "de volgende menstruatie", W),
                 ("kort", "Een vrouw heeft een cyclus van 26 dagen. Op de hoeveelste dag valt haar "
                          "eisprong ongeveer?", "op dag 12", W),
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
             opdracht="Nummer de stappen van 1 tot 5.",
             oefeningen=[
                 ("tabel", ["Nummer", "Wat er gebeurt"],
                  [[None, "de kiemblaas nestelt zich in het baarmoederslijmvlies"],
                   [None, "de LH-piek lokt de eisprong uit"],
                   [None, "het bevruchtingsmembraan sluit de eicel af"],
                   [None, "de zaadcellen zwemmen door de baarmoeder naar de eileider"],
                   [None, "de kernen versmelten tot een zygote"]],
                  "1 = de LH-piek lokt de eisprong uit · 2 = de zaadcellen zwemmen door de baarmoeder "
                  "naar de eileider · 3 = het bevruchtingsmembraan sluit de eicel af · 4 = de kernen "
                  "versmelten tot een zygote · 5 = de kiemblaas nestelt zich in het baarmoederslijmvlies",
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
                          ("je lengte van 1,72 m", "fenotype"),
                          ("de versie voor blauw", "allel")], None, WW),
             ]),
        dict(kop="Zet de weg van gen naar eiwit op volgorde",
             opdracht="Nummer de stappen van 1 tot 4 en vul de plaats aan.",
             oefeningen=[
                 ("tabel", ["Nummer", "Stap", "Waar in de cel"],
                  [[None, "het ribosoom koppelt aminozuren aan elkaar", None],
                   [None, "het mRNA wordt van het DNA afgelezen", None],
                   [None, "het eiwit is klaar en doet zijn werk", None],
                   [None, "het mRNA reist naar een ribosoom", None]],
                  "1 = het mRNA wordt van het DNA afgelezen, in de celkern · 2 = het mRNA reist naar een "
                  "ribosoom, uit de kern naar het cytoplasma · 3 = het ribosoom koppelt aminozuren aan "
                  "elkaar, aan het ribosoom · 4 = het eiwit is klaar en doet zijn werk, in de cel",
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
                 ("rij", [("een menselijke huidcel", "46, diploïd"),
                          ("een menselijke zaadcel", "23, haploïd"),
                          ("een menselijke eicel", "23, haploïd")], None, WW),
                 ("kort", "Een zygote ontstaat uit een eicel en een zaadcel. Hoeveel chromosomen heeft "
                          "ze?", "46", W),
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
                  "AA, Aa in de bovenste rij en Aa, aa in de onderste. Dus 25 % AA, 50 % Aa en 25 % aa.",
                  "80px"),
                 ("kort", "Welk percentage van die kinderen vertoont het recessieve kenmerk?", "25 %", W),
                 ("kort", "Welk percentage is drager zonder het kenmerk te tonen?", "50 %", W),
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
                  "De helft, dus 50 %. Een zoon krijgt zijn enige X van zijn moeder, en de helft van haar "
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
                  "ongeveer 4,6 miljard jaar", W),
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
                 ("open", "Een populaties wordt heel klein. Waarom is dat gevaarlijk voor de soort?",
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
                 ("kort", "Welke kunststof hoort bij recyclagecode 1?", "PET", W),
                 ("waar", "De driehoek van pijltjes met een cijfer betekent dat de verpakking zeker "
                          "gerecycleerd wordt.", False),
                 ("open", "Wat zegt dat cijfer dan wel?",
                  "Het zegt uit welke kunststof de verpakking gemaakt is. Het is een identificatiecode, "
                  "geen belofte over recyclage.", 3),
             ]),
        dict(kop="Kookpunt en smeltpunt",
             opdracht="Reken, kies en leg uit.",
             oefeningen=[
                 ("tabel", ["Stof", "Smeltpunt", "Kookpunt", "Vast, vloeibaar of gas bij 20 °C?"],
                  [["aceton", "−95 °C", "56 °C", None],
                   ["water", "0 °C", "100 °C", None],
                   ["ijzer", "1538 °C", "2862 °C", None]],
                  "Aceton is vloeibaar, water is vloeibaar en ijzer is vast bij 20 °C.", "95px"),
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
                  [["huishoudazijn", "3", None], ["zuiver water", "7", None],
                   ["ontstopper", "13", None], ["citroensap", "2", None]],
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
                 ("kort", "Een pot van 400 g bevat 25 g suiker per 100 g. Hoeveel suiker zit er in de "
                          "hele pot?", "100 g", W),
                 ("kort", "Een pak van 150 g bevat 12 g vet per 100 g. Hoeveel vet zit er in het pak?",
                  "18 g", W),
                 ("kort", "Een fles van 1,5 L bevat 10 g suiker per 100 mL. Hoeveel suiker in de hele "
                          "fles?", "150 g", W),
                 ("open", "Op een etiket staat suiker 36 g per 100 g. Wat zegt dat over het product, in "
                          "gewone woorden?",
                  "Ruim een derde van het product is suiker. Per honderd gram zit er dus 36 gram suiker "
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
                 ("rij", [("8 g per liter", "massaconcentratie"), ("5 % vol", "volumeprocent"),
                          ("3 g per 100 g", "massaprocent")], None, WL),
                 ("rij", [("40 % alcohol", "volumeprocent"), ("12 mg per liter", "massaconcentratie"),
                          ("20 g zout per 100 g pekel", "massaprocent")], None, WL),
             ]),
        dict(kop="Reken de hoeveelheid alcohol uit",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", "Een glas van 200 mL bier met 5 % vol. Hoeveel mL alcohol?", "10 mL", W),
                 ("kort", "Een glas van 150 mL wijn met 12 % vol. Hoeveel mL alcohol?", "18 mL", W),
                 ("kort", "Een glaasje van 40 mL sterke drank met 40 % vol. Hoeveel mL alcohol?",
                  "16 mL", W),
                 ("open", "Welk van die drie glazen bevat het meeste alcohol? Zet ze op volgorde en leg "
                          "uit waarom het percentage alleen niet volstaat.",
                  "Wijn 18 mL, sterke drank 16 mL, bier 10 mL. Het percentage zegt alleen hoe sterk de "
                  "drank is; je moet het volume erbij rekenen om de hoeveelheid te kennen.", 4),
             ]),
        dict(kop="Reken de concentratie uit",
             opdracht="Reken en zet de juiste eenheid erbij.",
             oefeningen=[
                 ("kort", "25 g zout in 500 g oplossing. Wat is het massaprocent?", "5 %", W),
                 ("kort", "10 g suiker opgelost tot 250 mL. Wat is de massaconcentratie?", "40 g/L", W),
                 ("kort", "6 g zout opgelost tot 2 L. Wat is de massaconcentratie?", "3 g/L", W),
                 ("kort", "Een oplossing van 25 g/L. Hoeveel stof zit er in 400 mL?", "10 g", W),
             ]),
        dict(kop="Dosis of concentratie?",
             opdracht="Schrijf dosis of concentratie.",
             oefeningen=[
                 ("rij", [("er zit 32 g suiker per 100 g in de pot", "concentratie"),
                          ("ik heb vandaag 40 g suiker gegeten", "dosis"),
                          ("deze drank is 5 % vol", "concentratie")], None, WW),
                 ("open", "Iemand zegt: deze drank is zwak, dus ik kan er zoveel van drinken als ik wil. "
                          "Wat is er fout aan die gedachte?",
                  "De concentratie is laag, maar de dosis hangt ook af van hoeveel je drinkt. Veel van "
                  "iets zwaks kan evenveel of meer alcohol opleveren dan weinig van iets sterks.", 4),
             ]),
        dict(kop="Reken met de ADI",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", "ADI = 5 mg per kg per dag. Een kind van 24 kg. Hoeveel mag het per dag?",
                  "120 mg", W),
                 ("kort", "ADI = 3 mg per kg per dag. Een volwassene van 80 kg. Hoeveel per dag?",
                  "240 mg", W),
                 ("open", "Waarom staat een ADI altijd per kilogram lichaamsgewicht en niet als één vast "
                          "getal?",
                  "Een stof verdeelt zich over je hele lichaam. In een groter lichaam wordt dezelfde "
                  "hoeveelheid meer verdund, dus een zwaarder lichaam verdraagt meer.", 4),
             ]),
        dict(kop="Lees de LD50",
             opdracht="Vergelijk en besluit.",
             oefeningen=[
                 ("tabel", ["Stof", "LD50 in mg per kg", "Giftiger of minder giftig?"],
                  [["stof A", "20", None], ["stof B", "800", None], ["stof C", "4000", None]],
                  "Stof A is het giftigst, dan B, dan C: hoe lager de LD50, hoe giftiger.", "130px"),
                 ("kort", "LD50 = 1500 mg per kg. Welke dosis is dat voor iemand van 50 kg, in gram?",
                  "75 g", W),
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
             opdracht="Nummer van 1, het best, tot 5, het slechtst.",
             oefeningen=[
                 ("tabel", ["Nummer", "Trede"],
                  [[None, "recycleren"], [None, "storten"], [None, "voorkomen dat er afval ontstaat"],
                   [None, "verbranden met energiewinst"], [None, "hergebruiken"]],
                  "1 = voorkomen dat er afval ontstaat · 2 = hergebruiken · 3 = recycleren · 4 = "
                  "verbranden met energiewinst · 5 = storten", "56px"),
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
                 ("rij", [("uit aardgas, de CO2 komt vrij", "grijze waterstof"),
                          ("uit aardgas, de CO2 wordt opgeslagen", "blauwe waterstof"),
                          ("uit water met hernieuwbare stroom", "groene waterstof")], None, WL),
                 ("rij", [("water van het toilet", "zwart water"),
                          ("water van bad en wasmachine", "grijs water"),
                          ("zuiver, drinkbaar water", "wit water")], None, WW),
                 ("rij", [("zon en wind", "hernieuwbaar"), ("steenkool en aardgas", "fossiel"),
                          ("uranium", "kernenergie")], "Welke energievorm?", WW),
                 ("open", "Een bedrijf noemt zijn productie CO2-negatief. Wat betekent dat, en waarin is "
                          "dat anders dan CO2-neutraal?",
                  "CO2-negatief haalt meer koolstofdioxide uit de lucht dan het uitstoot. Bij neutraal "
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
             opdracht="Gebruik f = 1 / T en v = λ · f. Schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", "T = 0,02 s. Wat is de frequentie?", "50 Hz", W),
                 ("kort", "T = 0,005 s. Wat is de frequentie?", "200 Hz", W),
                 ("kort", "λ = 4 m en f = 85 Hz. Wat is de golfsnelheid?", "340 m/s", W),
                 ("kort", "v = 340 m/s en f = 680 Hz. Wat is de golflengte?", "0,5 m", W),
                 ("kort", "f = 25 Hz. Wat is de periode?", "0,04 s", W),
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
                 ("kort", "Op 2 m van een box meet je 94 dB. Hoeveel meet je op 4 m?", "88 dB", W),
                 ("kort", "En hoeveel op 8 m?", "82 dB", W),
                 ("kort", "De geluidsintensiteit wordt vier keer kleiner. Hoeveel decibel zakt het "
                          "niveau?", "6 dB", W),
                 ("open", "Noem drie dagelijkse geluiden en zet ze op volgorde van zacht naar luid, met "
                          "een schatting in decibel.",
                  "Bijvoorbeeld fluisteren rond 30 dB, een gesprek rond 60 dB en een drilboor rond "
                  "100 dB.", 3),
             ]),
        dict(kop="Je gehoor beschermen",
             opdracht="Beoordeel en leg uit.",
             oefeningen=[
                 ("rij", [("de gehoordrempel", "0 dB"), ("de gevaargrens", "80 dB"),
                          ("de pijndrempel", "120 dB")], "Welk niveau hoort hierbij?", W),
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
             opdracht="Nummer van 1, de laagste energie, tot 7, de hoogste.",
             oefeningen=[
                 ("tabel", ["Nummer", "Soort straling"],
                  [[None, "zichtbaar licht"], [None, "radiogolven"], [None, "gammastraling"],
                   [None, "infraroodstraling"], [None, "röntgenstraling"], [None, "microgolven"],
                   [None, "ultraviolette straling"]],
                  "1 = radiogolven · 2 = microgolven · 3 = infraroodstraling · 4 = zichtbaar licht · "
                  "5 = ultraviolette straling · 6 = röntgenstraling · 7 = gammastraling", "56px"),
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
                  [["koolstof-12", "12", "6", None], ["zuurstof-16", "16", "8", None],
                   ["uranium-238", "238", "92", None], ["waterstof-3", "3", "1", None]],
                  "Koolstof-12: 6 neutronen. Zuurstof-16: 8 neutronen. Uranium-238: 146 neutronen. "
                  "Waterstof-3: 2 neutronen.", "70px"),
                 ("open", "Koolstof-12 en koolstof-14 zijn isotopen. Wat hebben ze gemeen en waarin "
                          "verschillen ze?",
                  "Ze hebben hetzelfde aantal protonen, zes, en zijn dus allebei koolstof. Koolstof-14 "
                  "heeft twee neutronen meer.", 4),
             ]),
        dict(kop="Reken met de halfwaardetijd",
             opdracht="Reken en schrijf je tussenstap op.",
             oefeningen=[
                 ("kort", "Halfwaardetijd 5 dagen. Welk deel is er na 20 dagen over?", "een zestiende", W),
                 ("kort", "Je begint met 800 g. Halfwaardetijd 3 jaar. Hoeveel na 9 jaar?", "100 g", W),
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
                  "1 = uraniumkernen splijten in de splijtstaven · 2 = het water wordt verhit tot stoom · "
                  "3 = de stoom drijft een turbine aan · 4 = de turbine draait de generator", "56px"),
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
                 ("rij", [("radium-226 zendt een alfadeeltje uit", "A = 222 en Z = 86"),
                          ("thorium-234 zendt een bètadeeltje uit", "A = 234 en Z = 91")],
                  "Radium heeft Z = 88, thorium heeft Z = 90.", WL),
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
                 ("open", "Je moet 1,5 kg wegen en je balans gaat tot 200 g. Wat doe je, en wat doe je "
                          "zeker niet?",
                  "Je zoekt een balans met een groter meetbereik. Je legt het niet toch voorzichtig op de "
                  "balans: de waarde klopt dan niet en het toestel kan stuk gaan.", 4),
                 ("open", "Je wil een verschil van 0,2 °C meten. Welke thermometer kies je en waarom?",
                  "Een met streepjes van 0,1 °C. Het toestel moet nauwkeuriger zijn dan het verschil dat "
                  "je wil zien.", 3),
             ]),
        dict(kop="Zet de eenheden om",
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [("3,2 km in m", "3200 m"), ("750 mg in g", "0,75 g"),
                          ("5 MJ in J", "5 000 000 J")], None, WW),
                 ("rij", [("0,4 m in mm", "400 mm"), ("2500 g in kg", "2,5 kg"),
                          ("8 µm in m", "0,000008 m")], None, WW),
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
                  "1 = het probleem definiëren · 2 = criteria opstellen · 3 = het probleem in "
                  "deelproblemen splitsen · 4 = oplossingen bedenken en samenvoegen · 5 = evalueren en "
                  "bijsturen", "56px"),
                 ("open", "Een stad wil de luchtkwaliteit verbeteren. Welke STEM-domeinen heb je nodig, "
                          "en waarvoor elk?",
                  "Wetenschappelijke kennis over de stoffen in de lucht, technische kennis over "
                  "meettoestellen en filters, en wiskundige kennis om de metingen te verwerken. Een "
                  "totaaloplossing vraagt kennis uit meerdere hoeken.", 4),
             ]),
    ],
)
