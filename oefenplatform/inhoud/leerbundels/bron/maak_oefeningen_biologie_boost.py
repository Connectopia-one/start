# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij biologie 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere reeksen om te benoemen, andere gevallen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een stap
uitleggen, een weg uitschrijven). Wie hier iets bijschrijft, legt het eerst
naast `../../boost-doorstroom/biologie.json`, naast de leerbundel van hetzelfde
thema en naast de vakfiche zelf.

De fiche biologie van de 2de graad doorstroomfinaliteit geldt enkel voor de
studierichting natuurwetenschappen, die haar wetenschappen in drie aparte
examens aflegt.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-biologie-boost-doorstroom". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Biologie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Bij een weg of een orde: schrijf de stappen onder elkaar, in de juiste volgorde.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-homeostase-en-waterhuishouding-bij-planten-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Homeostase en waterhuishouding bij planten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk deel of welk weefsel?",
             opdracht="Schrijf bij elke taak de naam.",
             oefeningen=[
                 ("rij", [("neemt water en mineralen op", "de wortel"),
                          ("vangt het licht op voor de fotosynthese", "het blad"),
                          ("draagt het blad en vervoert", "de stengel")], "Welk orgaan?", WW),
                 ("rij", [("vervoert water omhoog", "het xyleem of de houtvaten"),
                          ("vervoert de suikers", "het floëem of de zeefvaten"),
                          ("vult op en slaat stoffen op", "het vulweefsel")], "Welk weefsel?", WL),
                 ("rij", [("waterafstotend laagje op het blad", "de cuticula"),
                          ("buitenste cellaag van de plant", "de epidermis"),
                          ("xyleem en floëem samen", "de vaatbundel")], "Welke naam?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een plant stuurt haar waterverlies bij met een feedbacksysteem.", True),
                 ("waar", "De turgor is de druk waarmee de bodem op de wortel duwt.", False),
                 ("waar", "De zwaartekracht helpt het water in een plant omhoog.", False),
                 ("waar", "Een plant met gesloten huidmondjes neemt nauwelijks nog koolstofdioxide op.",
                  True),
                 ("waar", "De kleur van de bloemblaadjes beïnvloedt de waterhuishouding.", False),
             ]),
        dict(kop="De drie krachten",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Kracht", "Waar ze werkt en wat ze doet"],
                  [["worteldruk", None], ["transpiratiezuiging", None], ["capillariteit", None]],
                  "Worteldruk duwt van onderaf in de wortel. Transpiratiezuiging trekt van bovenaf in "
                  "het blad, doordat daar water verdampt. Capillariteit laat het water in de nauwe "
                  "houtvaten vanzelf omhoog kruipen.", WL),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom liggen de meeste huidmondjes aan de onderkant van een blad?",
                  "Daar is het koeler en schaduwrijker, dus verdampt er minder water. De plant verliest "
                  "zo minder vocht bij dezelfde gasuitwisseling.", 4),
                 ("open", "Een plant sluit bij droogte haar huidmondjes. Noem het voordeel en het nadeel.",
                  "Het voordeel is dat ze veel minder water verliest. Het nadeel is dat er ook geen "
                  "koolstofdioxide meer binnenkomt, waardoor de fotosynthese grotendeels stilvalt.", 4),
                 ("open", "Leg uit waarom het transport in het floëem in twee richtingen kan gaan en dat "
                          "in het xyleem niet.",
                  "Water volgt de verdamping in het blad en gaat dus altijd naar boven. Suikers gaan van "
                  "waar ze gemaakt worden naar waar ze gebruikt of opgeslagen worden, en dat kan hoger "
                  "of lager in de plant liggen.", 5),
             ]),
        dict(kop="Prikkels en hormonen bij planten",
             opdracht="Schrijf het juiste woord of kies.",
             oefeningen=[
                 ("rij", [("laat cellen strekken, buigt de stengel naar het licht", "auxine"),
                          ("doet vruchten rijpen", "ethyleen"),
                          ("sluit de huidmondjes bij droogte", "abscisinezuur")], "Welk hormoon?", WW),
                 ("kies", "Welke van deze bewegingen is een tropie?",
                  ["een blad dat 's avonds dichtklapt",
                   "een wortel die naar beneden groeit",
                   "een bloem die bij warmte opengaat",
                   "een blad dat bij aanraking schokt"], 1),
                 ("kort", "Hoe noem je een structuur die licht opvangt en zo een prikkel doorgeeft?",
                  "een fotoreceptor", WL),
                 ("waar", "Een plant geeft haar prikkels door langs zenuwen naar een centraal orgaan.",
                  False),
             ]),
        dict(kop="Fotosynthese",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("kort", "Schrijf de reactievergelijking van de fotosynthese.",
                  "6 CO₂ + 6 H₂O geeft C₆H₁₂O₆ + 6 O₂", WL),
                 ("kort", "In welk celorganel gebeurt de fotosynthese?", "in de chloroplast", WL),
                 ("open", "Noem drie manieren waarop een goede waterhuishouding de fotosynthese mogelijk "
                          "maakt.",
                  "Water is zelf een grondstof van de fotosynthese. Open huidmondjes laten de "
                  "koolstofdioxide binnen. En het watertransport voert de mineralen naar het blad aan.",
                  4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-prikkel-tot-reactie-en-het-zenuwstelsel-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Van prikkel tot reactie en het zenuwstelsel",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De weg van prikkel tot reactie",
             opdracht="Schrijf de vijf stappen in de juiste orde onder elkaar.",
             oefeningen=[
                 ("open", "Je hoort je naam en draait je hoofd. Schrijf de weg van prikkel tot reactie "
                          "met de vijf schakels, en zet er bij elke schakel bij wat ze in dit voorbeeld "
                          "is.",
                  "Receptor: de haarcellen in het oor. Sensorische zenuw: de gehoorzenuw. Verwerking: de "
                  "hersenen. Motorische zenuw: de zenuw naar de nekspieren. Effector: de nekspieren.", 6),
             ]),
        dict(kop="Receptor of effector?",
             opdracht="Schrijf bij elk wat het is.",
             oefeningen=[
                 ("rij", [("een zweetklier in de huid", "effector"),
                          ("een tastreceptor in de vingertop", "receptor"),
                          ("de hartspier", "effector")], "Wat is het?", WW),
                 ("rij", [("een staafje in het netvlies", "receptor"),
                          ("een skeletspier in de arm", "effector"),
                          ("een rekreceptor in de maagwand", "receptor")], "Wat is het?", WW),
             ]),
        dict(kop="Reflexen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Reflex", "De prikkel", "De reactie"],
                  [["pupilreflex", None, None], ["kniepeesreflex", None, None],
                   ["terugtrekreflex", None, None]],
                  "Pupilreflex: veel licht op het oog, de pupil vernauwt. Kniepeesreflex: een tikje "
                  "onder de knieschijf rekt de pees, het onderbeen veert op. Terugtrekreflex: pijn of "
                  "hitte aan de hand, de hand trekt weg.", WW),
                 ("waar", "Bij een reflex schakelt de boodschap over in het ruggemerg of de hersenstam.",
                  True),
                 ("waar", "Elke reflex kan je met genoeg oefening onderdrukken.", False),
             ]),
        dict(kop="Welk deel van de hersenen?",
             opdracht="Schrijf het juiste deel.",
             oefeningen=[
                 ("rij", [("ademhaling, hartslag en bloeddruk", "de hersenstam"),
                          ("bewust denken, plannen en leren", "de grote hersenen"),
                          ("beweging afstemmen en evenwicht", "de kleine hersenen")], "Welk deel?", WL),
                 ("kort", "Welke twee delen vormen samen het centrale zenuwstelsel?",
                  "de hersenen en het ruggemerg", WL),
                 ("kort", "Hoe noem je alle zenuwen daarbuiten?", "het perifere zenuwstelsel", WL),
             ]),
        dict(kop="Het neuron",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("vangt signalen op", "de dendrieten"),
                          ("geeft het signaal door, één per neuron", "het axon"),
                          ("isoleert het axon", "de myelineschede")], "Welk deel?", WL),
                 ("kort", "Hoe noem je de kale stukjes axon tussen twee cellen van Schwann?",
                  "de knopen van Ranvier", WL),
                 ("kies", "Hoeveel axonen en dendrieten heeft een neuron?",
                  ["veel axonen en één dendriet", "veel dendrieten en één axon",
                   "één van elk", "even veel van beide"], 1),
                 ("open", "Leg uit waarom een impuls langs een gemyeliniseerd axon veel sneller gaat.",
                  "De myelineschede isoleert het axon, zodat de impuls enkel bij de knopen van Ranvier "
                  "opnieuw opgewekt wordt. Hij springt dus van knoop naar knoop in plaats van elk stukje "
                  "membraan te doorlopen.", 5),
             ]),
        dict(kop="Vergelijken",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Noem twee verschillen tussen een reflex en een bewuste reactie.",
                  "Een reflex verloopt sneller, en hij schakelt over in het ruggemerg of de hersenstam. "
                  "Bij een bewuste reactie komen de grote hersenen tussen en beslis je zelf.", 4),
                 ("open", "Het zenuwstelsel en het hormonale stelsel werken samen. Waarom is dat zinvol?",
                  "Het zenuwstelsel reageert in milliseconden maar het effect is meteen voorbij. Een "
                  "hormoon reist met het bloed en werkt minuten tot dagen door. Samen heb je dus zowel "
                  "een snelle als een aanhoudende reactie.", 5),
                 ("waar", "In een synaps kan het signaal in beide richtingen gaan.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-oog-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het oog",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De weg van het licht",
             opdracht="Schrijf de vijf delen in de orde waarin het licht ze doorloopt.",
             oefeningen=[
                 ("open", "Zet in de juiste orde: lens, netvlies, hoornvlies, glasachtig lichaam, pupil.",
                  "hoornvlies, pupil, lens, glasachtig lichaam, netvlies", 3),
             ]),
        dict(kop="Welk deel doet dit?",
             opdracht="Schrijf de naam van het deel.",
             oefeningen=[
                 ("rij", [("regelt hoeveel licht binnenkomt", "de iris"),
                          ("geeft de oogbol zijn vorm", "het harde oogvlies"),
                          ("voedt het netvlies en neemt strooilicht weg", "het vaatvlies")],
                  "Welk deel?", WL),
                 ("rij", [("vult de ruimte achter de lens", "het glasachtig lichaam"),
                          ("vult de voorste oogkamer", "het kamervocht"),
                          ("laat de oogbol in zijn kas draaien", "de uitwendige oogspieren")],
                  "Welk deel?", WL),
             ]),
        dict(kop="Het netvlies",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Staafjes", "Kegeltjes"],
                  [["bij weinig licht", None, None], ["zien kleur", None, None],
                   ["waar ze vooral liggen", None, None]],
                  "Bij weinig licht: staafjes werken wel, kegeltjes niet. Kleur: staafjes niet, "
                  "kegeltjes wel. Plaats: staafjes vooral buiten het midden, kegeltjes vooral in de gele "
                  "vlek.", W),
                 ("kort", "Hoe noem je de plaats met de meeste kegeltjes?", "de gele vlek", WL),
                 ("kort", "Hoe noem je de plaats waar de oogzenuw het netvlies verlaat?",
                  "de blinde vlek", WL),
                 ("waar", "Het beeld dat op het netvlies valt, staat op zijn kop.", True),
             ]),
        dict(kop="Accommodatie",
             opdracht="Kies of leg uit.",
             oefeningen=[
                 ("kies", "Je kijkt van de verte naar een boek dichtbij. Wat doet de lens?",
                  ["ze wordt platter", "ze wordt boller",
                   "ze schuift naar voren", "ze blijft gelijk"], 1),
                 ("open", "Leg uit waarom de lens voor ver kijken platter wordt.",
                  "Licht van ver valt bijna recht het oog binnen en moet dus minder sterk gebogen "
                  "worden. Het kringspiertje rond de lens ontspant, en de lens wordt platter.", 4),
                 ("open", "Waarom merk je in het dagelijks leven niets van je blinde vlek? Noem twee "
                          "redenen.",
                  "Het andere oog ziet dat stukje wel, want de blinde vlekken liggen niet op dezelfde "
                  "plaats in het beeld. En de hersenen vullen het gat aan met wat eromheen ligt.", 4),
             ]),
        dict(kop="Afwijkingen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Afwijking", "Wat er mis is", "Welke lens helpt"],
                  [["bijziendheid", None, None], ["verziendheid", None, None],
                   ["astigmatisme", None, None]],
                  "Bijziendheid: de oogbol is te lang of de lens buigt te sterk, het beeld valt voor het "
                  "netvlies; een holle lens helpt. Verziendheid: de oogbol is te kort of de lens te zwak, "
                  "het beeld valt achter het netvlies; een bolle lens helpt. Astigmatisme: het hoornvlies "
                  "of de lens is onregelmatig gekromd; een cilindrische lens helpt.", WW),
                 ("waar", "Bij kleurenblindheid werken een of meer soorten kegeltjes niet goed.", True),
                 ("waar", "Een bril met de verkeerde sterkte beschadigt het netvlies blijvend.", False),
                 ("kort", "Hoe noem je de verziendheid die komt doordat de lens met de jaren stijver "
                          "wordt?", "ouderdomsverziendheid", WL),
             ]),
        dict(kop="Zien is ook verwerken",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom zie je met twee ogen diepte en met één oog veel minder?",
                  "Je ogen staan een stukje van elkaar, dus ziet elk oog het voorwerp vanuit een iets "
                  "andere hoek. Uit dat kleine verschil tussen de twee beelden halen de hersenen de "
                  "afstand.", 5),
                 ("open", "Noem de drie stappen van licht naar zenuwimpuls in het oog.",
                  "Het licht valt op een staafje of kegeltje in het netvlies. Die cel wekt een "
                  "zenuwimpuls op. De oogzenuw brengt die impuls naar de hersenen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-oor-en-het-evenwicht-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het oor en het evenwicht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In welk deel van het oor?",
             opdracht="Schrijf uitwendig oor, middenoor of inwendig oor.",
             oefeningen=[
                 ("rij", [("het trommelvel", "uitwendig oor"),
                          ("de stijgbeugel", "middenoor"),
                          ("het slakkenhuis", "inwendig oor")], "Welk deel?", WW),
                 ("rij", [("de gehoorgang", "uitwendig oor"),
                          ("de buis van Eustachius", "middenoor"),
                          ("het evenwichtsorgaan", "inwendig oor")], "Welk deel?", WW),
             ]),
        dict(kop="De weg van het geluid",
             opdracht="Schrijf de zes schakels in de juiste orde onder elkaar, met telkens erbij of het "
                      "geluid daar door lucht, door een vast deel of door vloeistof gaat.",
             oefeningen=[
                 ("open", "Oorschelp, slakkenhuis, gehoorbeentjes, gehoorzenuw, gehoorgang, trommelvel.",
                  "Oorschelp (lucht), gehoorgang (lucht), trommelvel (vast), gehoorbeentjes (vast), "
                  "slakkenhuis (vloeistof), gehoorzenuw (zenuwimpuls).", 7),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De gehoorbeentjes versterken de trilling van het trommelvel.", True),
                 ("waar", "In het slakkenhuis reist het geluid verder door de lucht.", False),
                 ("waar", "Beschadigde haarcellen groeien bij de mens niet meer terug.", True),
                 ("waar", "Een hoortoestel herstelt beschadigde haarcellen.", False),
                 ("waar", "De oorschelp helpt om te horen uit welke richting een geluid komt.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom helpt slikken of gapen als je oren in een vliegtuig dichtzitten?",
                  "Slikken en gapen openen de buis van Eustachius. Daardoor wordt de druk in het "
                  "middenoor weer gelijk aan die buiten, en bolt het trommelvel niet meer.", 4),
                 ("open", "Leg uit waarom een hoge toon elders in het slakkenhuis gevoeld wordt dan een "
                          "lage.",
                  "Het membraan in het slakkenhuis is bij het begin smal en stijf en verderop breed en "
                  "slap. Daardoor komt elke toonhoogte op haar eigen plaats in trilling.", 5),
                 ("open", "Waarom gaat het gehoor met de jaren vooral voor de hoge tonen achteruit?",
                  "Alle geluid gaat eerst langs het begin van het slakkenhuis, en net daar liggen de "
                  "haarcellen voor de hoge tonen. Die krijgen dus alles te verwerken en slijten het "
                  "snelst.", 5),
             ]),
        dict(kop="Het evenwichtsorgaan",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Positiezin", "Rotatiezin"],
                  [["wat ze meet", None, None], ["in welke structuur", None, None]],
                  "De positiezin meet de stand van het hoofd ten opzichte van de zwaartekracht, in de "
                  "zakjes met gewichtjes. De rotatiezin meet of en hoe het hoofd draait, in de drie "
                  "halfcirkelvormige kanaaltjes.", WW),
                 ("kort", "Hoeveel halfcirkelvormige kanaaltjes heeft het evenwichtsorgaan per oor?",
                  "drie", W),
                 ("kort", "Hoe noem je de eigenschap van de vloeistof waardoor ze bij een draai "
                          "achterblijft?", "traagheid", WL),
                 ("open", "Waarom staan de drie kanaaltjes loodrecht op elkaar?",
                  "Draaien kan in drie richtingen: knikken, kantelen en rondkijken. Met drie kanalen in "
                  "drie vlakken wordt elke draairichting opgevangen.", 4),
             ]),
        dict(kop="Als de berichten niet kloppen",
             opdracht="Leg uit of kies.",
             oefeningen=[
                 ("open", "Waarom blijf je duizelig als je plots stopt na lang ronddraaien?",
                  "Het kanaal staat stil, maar de vloeistof draait nog door en buigt de haarcellen om. "
                  "Je oor meldt dus een draai die er niet meer is, terwijl je ogen stilstand melden.", 5),
                 ("open", "Waarom word je soms wagenziek als je in een rijdende auto leest, en waarom "
                          "helpt naar buiten kijken?",
                  "Je oor meldt beweging terwijl je ogen een stilstaand blad zien, en dat conflict geeft "
                  "misselijkheid. Kijk je naar buiten, dan melden je ogen ook beweging en kloppen de "
                  "twee berichten weer.", 5),
                 ("kies", "Welke drie bronnen gebruiken je hersenen voor je evenwicht?",
                  ["oor, ogen en het gehoor",
                   "oor, ogen en de rek in spieren en gewrichten",
                   "ogen, huid en de toonhoogte van geluid",
                   "oor, huid en het slakkenhuis"], 1),
                 ("waar", "Het evenwichtsorgaan stuurt zijn signalen rechtstreeks naar de spieren.",
                  False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-spieren-en-de-klieren-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De spieren en de klieren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk soort spierweefsel?",
             opdracht="Schrijf skelet, glad of hart.",
             oefeningen=[
                 ("rij", [("in de wand van de darmen", "glad"),
                          ("in de biceps van de arm", "skelet"),
                          ("in de wand van het hart", "hart")], "Welk soort?", WW),
                 ("rij", [("gestreept en willekeurig", "skelet"),
                          ("gestreept maar onwillekeurig", "hart"),
                          ("niet gestreept en onwillekeurig", "glad")], "Welk soort?", WW),
             ]),
        dict(kop="De microscopische bouw",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("begrenst een sarcomeer", "de Z-plaat"),
                          ("de dunne filamenten", "actine"),
                          ("de dikke filamenten", "myosine")], "Welke naam?", WW),
                 ("kort", "Hoe noem je het stuk spiervezel tussen twee Z-platen?", "een sarcomeer", WL),
                 ("kies", "Wat gebeurt er met de filamenten bij een samentrekking?",
                  ["de actine wordt korter", "de myosine wordt korter",
                   "ze schuiven langs elkaar", "ze lossen op en vormen zich opnieuw"], 2),
                 ("waar", "Bij een samentrekking wordt de lichte band smaller.", True),
                 ("waar", "In de donkere band liggen enkel actinefilamenten.", False),
                 ("open", "Leg met de woorden actine, myosine en Z-plaat uit hoe een sarcomeer korter "
                          "wordt.",
                  "De myosinekopjes grijpen de actinefilamenten vast en trekken die naar het midden toe. "
                  "De filamenten blijven even lang, maar de Z-platen schuiven naar elkaar en zo wordt "
                  "het sarcomeer korter.", 5),
             ]),
        dict(kop="Wat een spier nodig heeft",
             opdracht="Leg uit of kies.",
             oefeningen=[
                 ("kort", "Hoe noem je de plaats waar een motorische zenuwcel een spiervezel aanspreekt?",
                  "de motorische eindplaat", WL),
                 ("open", "Noem drie dingen die een spiervezel nodig heeft om samen te trekken.",
                  "Een prikkel van een motorische zenuwcel, energie uit de celademhaling, en "
                  "calciumionen in de cel.", 4),
                 ("open", "Waarom krijg je bij een zware sprint een branderig gevoel in je benen?",
                  "Er komt niet snel genoeg zuurstof binnen, dus breekt de spier glucose onvolledig af. "
                  "Daarbij vormt zich melkzuur, en dat voelt branderig.", 4),
                 ("open", "Waarom heeft een spier die veel werkt, veel mitochondriën?",
                  "In een mitochondrion gebeurt de celademhaling, en daar komt de energie vrij die een "
                  "samentrekking kost. Hoe meer de spier werkt, hoe meer energie ze per seconde nodig "
                  "heeft.", 4),
             ]),
        dict(kop="Klieren en hormonen",
             opdracht="Schrijf de naam of vul aan.",
             oefeningen=[
                 ("rij", [("regelt de snelheid van de stofwisseling", "de schildklier"),
                          ("geeft adrenaline af bij schrik", "de bijnier"),
                          ("stuurt andere klieren aan", "de hypofyse")], "Welke klier?", WL),
                 ("kort", "Hoe noem je een klier die haar stof rechtstreeks aan het bloed afgeeft?",
                  "een klier zonder afvoergang", WL),
                 ("waar", "Een hormoon werkt enkel op cellen die er de juiste receptor voor hebben.",
                  True),
                 ("waar", "Een hormoon werkt sneller dan een zenuwimpuls.", False),
                 ("open", "Noem drie veranderingen die adrenaline in het lichaam teweegbrengt.",
                  "De hartslag versnelt, de pupillen worden groter en er komt glucose uit de lever vrij. "
                  "De spijsvertering gaat juist op een lager pitje.", 4),
             ]),
        dict(kop="De eilandjes van Langerhans",
             opdracht="Vul de tabel aan en leg uit.",
             oefeningen=[
                 ("tabel", ["Cel", "Hormoon", "Wat het met de bloedglucose doet"],
                  [["bètacel", None, None], ["alfacel", None, None]],
                  "Bètacel: insuline, laat het bloedglucosegehalte dalen doordat de cellen glucose "
                  "opnemen en de lever ze opslaat. Alfacel: glucagon, laat het gehalte stijgen doordat "
                  "de lever haar voorraad afbreekt.", WW),
                 ("open", "Beschrijf stap voor stap wat er gebeurt nadat je een zoete koek gegeten hebt.",
                  "Het bloedglucosegehalte stijgt. De bètacellen geven insuline af. De cellen nemen "
                  "glucose op en de lever slaat ze op. Daardoor daalt het gehalte weer binnen zijn "
                  "grenzen.", 5),
                 ("open", "Leg uit waarom insuline en glucagon samen een voorbeeld van homeostase zijn.",
                  "Ze werken tegengesteld: het ene doet het gehalte dalen, het andere stijgen. Daardoor "
                  "wordt een afwijking in beide richtingen bijgestuurd en blijft het bloedglucosegehalte "
                  "binnen nauwe grenzen.", 5),
                 ("kies", "Wat is er bij diabetes type 1 aan de hand?",
                  ["de alfacellen maken te veel glucagon",
                   "de bètacellen maken geen of te weinig insuline",
                   "de lever kan geen glucose opslaan",
                   "de darmen nemen geen glucose op"], 1),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-voortplanting-en-de-menstruatiecyclus-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Voortplanting en de menstruatiecyclus",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Schrijf het juiste woord.",
             oefeningen=[
                 ("rij", [("de geslachtscellen van de mens", "gameten"),
                          ("de cel na de bevruchting", "de zygote"),
                          ("het vastzetten in het slijmvlies", "de innesteling")], "Welk woord?", WW),
                 ("rij", [("het blaasje waarin een eicel rijpt", "de follikel"),
                          ("wat na de ovulatie overblijft", "het geel lichaam"),
                          ("het einde van de vruchtbare periode", "de menopauze")], "Welk woord?", WW),
                 ("kort", "Hoeveel chromosomen heeft een gameet van de mens?", "23", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De bevruchting gebeurt meestal in de eileider.", True),
                 ("waar", "Het bloed van de moeder en dat van het kind vermengen zich in de placenta.",
                  False),
                 ("waar", "Alcohol kan door de placenta naar het kind.", True),
                 ("waar", "De geslachtshormonen bij de puberteit worden door de schildklier aangestuurd.",
                  False),
                 ("waar", "Een eeneiige tweeling heeft hetzelfde erfelijk materiaal.", True),
             ]),
        dict(kop="De zwangerschap",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("wisselt stoffen uit tussen moeder en kind", "de placenta"),
                          ("verbindt het kind met de placenta", "de navelstreng"),
                          ("beschermt tegen stoten", "het vruchtwater")], "Welk deel?", WL),
                 ("open", "Leg uit waarom het belangrijk is dat de twee bloedbanen in de placenta "
                          "gescheiden blijven.",
                  "De bloedgroepen van moeder en kind kunnen verschillen, en vermengd bloed zou een "
                  "afweerreactie kunnen geven. Door de dunne wand gaan wel de stoffen door, maar niet de "
                  "bloedcellen.", 5),
             ]),
        dict(kop="De drie fasen van de cyclus",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Fase", "Wat er in de eierstok gebeurt", "Welk hormoon overheerst"],
                  [["folliculaire fase", None, None], ["luteale fase", None, None]],
                  "Folliculaire fase: een follikel rijpt; oestrogeen overheerst en bouwt het "
                  "baarmoederslijmvlies op. Luteale fase: het geel lichaam blijft over; progesteron "
                  "overheerst en houdt het slijmvlies in stand.", WW),
                 ("kort", "Hoe noem je het vrijkomen van de eicel uit de eierstok?", "de ovulatie", WL),
                 ("kies", "Welke fase ligt tussen de ovulatie en de volgende menstruatie?",
                  ["de folliculaire fase", "de menstruatiefase",
                   "de luteale fase", "de innestelingsfase"], 2),
                 ("open", "Leg stap voor stap uit waarom er een menstruatie volgt als er geen bevruchting "
                          "is.",
                  "Zonder bevruchting sterft het geel lichaam na ongeveer twee weken af. Daardoor daalt "
                  "het progesteron. Het baarmoederslijmvlies wordt dan niet meer in stand gehouden, laat "
                  "los en verlaat met wat bloed de baarmoeder.", 6),
             ]),
        dict(kop="Hoe de cyclus gestuurd wordt",
             opdracht="Leg uit of kies.",
             oefeningen=[
                 ("open", "Leg uit waarom de menstruatiecyclus een voorbeeld van terugkoppeling is.",
                  "De hypofyse stuurt de eierstok aan met twee hormonen. De hormonen van de eierstok "
                  "remmen of stimuleren op hun beurt de hypofyse. Zo beïnvloeden de twee elkaar en "
                  "verloopt de cyclus telkens opnieuw in dezelfde orde.", 5),
                 ("kies", "Bij een cyclus van 32 dagen is welke fase meestal langer?",
                  ["de luteale fase", "de folliculaire fase",
                   "de menstruatiefase", "geen enkele"], 1),
                 ("open", "Waarom is de kalender alleen onvoldoende om bij een onregelmatige cyclus de "
                          "ovulatie te voorspellen? Noem ook twee tekens waar je wel op kan letten.",
                  "De folliculaire fase varieert in lengte, dus schuift de ovulatie mee en valt ze niet "
                  "elke maand op dezelfde dag. Je kan wel letten op een lichte stijging van de "
                  "lichaamstemperatuur en op een verandering van het baarmoederhalsslijm.", 6),
                 ("open", "Hoe werkt de gecombineerde anticonceptiepil?",
                  "Door voortdurend oestrogeen en progesteron aan te voeren, wordt de hypofyse geremd. "
                  "Die denkt dan dat de luteale fase bezig is, er rijpt geen follikel en er volgt geen "
                  "ovulatie.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biodiversiteit-en-micro-organismen-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Biodiversiteit en micro-organismen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Op welk niveau?",
             opdracht="Schrijf genen, soorten of ecosystemen.",
             oefeningen=[
                 ("rij", [("de ene hond is groter dan de andere", "genen"),
                          ("een bos, een duin en een ven in één streek", "ecosystemen"),
                          ("tweehonderd vogelsoorten in een land", "soorten")], "Welk niveau?", WW),
                 ("kort", "Wanneer horen twee organismen tot dezelfde soort?",
                  "als ze vruchtbare nakomelingen kunnen krijgen", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een gebied met veel soorten herstelt sneller na een verstoring.", True),
                 ("waar", "Een wetenschappelijke naam bestaat uit twee delen.", True),
                 ("waar", "Een invasieve exoot heeft hier vaak geen natuurlijke vijanden.", True),
                 ("waar", "Antibiotica werken ook tegen virussen.", False),
                 ("waar", "Alle bacteriën in en op ons lichaam zijn schadelijk.", False),
             ]),
        dict(kop="Bedreigingen en oplossingen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Bedreiging", "Wat eraan te doen is"],
                  [["versnippering van leefgebied", None], ["een invasieve exoot", None],
                   ["overbemesting van een natuurgebied", None]],
                  "Versnippering: gebieden weer verbinden, bijvoorbeeld met een ecoduct. Een invasieve "
                  "exoot: hem wegnemen en de aanvoer stoppen. Overbemesting: minder mest, en de verrijkte "
                  "bovenlaag afvoeren.", WL),
                 ("open", "Leg uit waarom versnippering schadelijk is, ook als de totale oppervlakte "
                          "gelijk blijft.",
                  "Kleine groepen raken van elkaar gescheiden en kunnen niet meer uitwisselen. Daardoor "
                  "neemt de variatie in hun erfelijk materiaal af en worden ze kwetsbaarder voor ziekte "
                  "en verandering.", 5),
                 ("open", "Noem drie dingen die je in een tuin kan doen om de biodiversiteit te verhogen.",
                  "Inheemse planten zetten die bloeien voor insecten, een hoekje laten verwilderen, en "
                  "geen chemische bestrijdingsmiddelen gebruiken.", 4),
             ]),
        dict(kop="Bacterie, virus of schimmel?",
             opdracht="Schrijf wat bij de omschrijving past.",
             oefeningen=[
                 ("rij", [("één cel zonder echte kern, deelt zich zelf", "een bacterie"),
                          ("heeft een gastheercel nodig om zich te vermeerderen", "een virus"),
                          ("een eencellige die brooddeeg laat rijzen", "een schimmel, namelijk gist")],
                  "Wat is het?", WL),
                 ("waar", "Een virus heeft een eigen stofwisseling.", False),
                 ("open", "Leg uit waarom een antibioticum tegen een griep niet helpt.",
                  "Een antibioticum grijpt in op iets dat enkel een bacterie heeft, zoals haar celwand. "
                  "Griep wordt door een virus veroorzaakt, en dat heeft die structuren niet.", 4),
                 ("open", "Leg uit hoe antibioticaresistentie ontstaat, en waarom je een kuur afmaakt.",
                  "Bij elke kuur overleven de bacteriën die er het best tegen kunnen, en die "
                  "vermeerderen zich. Stop je te vroeg, dan blijven net de taaiste over; door de kuur af "
                  "te maken worden ook die opgeruimd.", 5),
             ]),
        dict(kop="Nuttige micro-organismen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("yoghurt en kaas", "bacteriën"),
                          ("brood en bier", "gist"),
                          ("afvalwater zuiveren", "bacteriën")], "Wat wordt gebruikt?", WW),
                 ("open", "Welke rol spelen bacteriën en schimmels in de kringloop van een ecosysteem?",
                  "Zij zijn de reducenten: ze breken dood organisch materiaal af en maken de mineralen "
                  "weer vrij, zodat planten die opnieuw kunnen opnemen. Zonder hen bleven de mineralen "
                  "opgesloten.", 5),
             ]),
        dict(kop="De afweer van het lichaam",
             opdracht="Vul de tabel aan en leg uit.",
             oefeningen=[
                 ("tabel", ["Barrière", "Waar ze zit en wat ze doet"],
                  [["de huid", None], ["het maagzuur", None], ["het slijm", None]],
                  "De onbeschadigde huid sluit het lichaam af. Het maagzuur doodt wat je inslikt. Het "
                  "slijm in de luchtwegen vangt deeltjes op en de trilhaartjes voeren ze weg.", WL),
                 ("kort", "Hoe noem je de stof die precies op één indringer past?", "een antistof", WL),
                 ("open", "Leg uit hoe een vaccin werkt.",
                  "Een vaccin toont het afweersysteem een onschadelijk stuk van de ziekteverwekker. Het "
                  "lichaam maakt daar antistoffen en afweercellen tegen aan, zonder dat je ziek wordt. "
                  "Komt de echte verwekker later, dan staat de afweer al klaar.", 5),
                 ("open", "Waarom is handen wassen zo doeltreffend tegen besmetting?",
                  "De meeste besmettingen gaan via de handen naar mond, neus of ogen. Zeep en water halen "
                  "de micro-organismen van de huid, dus wordt die weg onderbroken.", 4),
                 ("open", "Waarom laat je een restje soep niet een nacht op het aanrecht staan?",
                  "Soep is vochtig en voedzaam, en bij kamertemperatuur kan een bacterie zich elk half "
                  "uur delen. In een nacht zijn er dan onveilige aantallen; in de koelkast gaat dat delen "
                  "veel trager.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-gedrag-en-interactie-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Gedrag en interactie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Aangeboren of geleerd?",
             opdracht="Schrijf aangeboren of geleerd.",
             oefeningen=[
                 ("rij", [("een pasgeboren baby die zoekt om te zuigen", "aangeboren"),
                          ("een hond die zit voor een koekje", "geleerd"),
                          ("de pupilreflex", "aangeboren")], "Wat is het?", WW),
                 ("rij", [("een mees die een melkflesje leert openpikken", "geleerd"),
                          ("een spin die haar web bouwt", "aangeboren"),
                          ("een kat die naar de keuken komt bij het geluid van haar bak", "geleerd")],
                  "Wat is het?", WW),
             ]),
        dict(kop="Welke vorm van leren?",
             opdracht="Schrijf gewenning, conditionering, nadoen of inprenting.",
             oefeningen=[
                 ("rij", [("vogels gaan naast een vogelverschrikker zitten", "gewenning"),
                          ("eendenkuikens volgen wat ze eerst zien bewegen", "inprenting"),
                          ("een jong dier eet wat zijn moeder eet", "nadoen")], "Welke vorm?", WW),
                 ("kort", "Welke vorm van leren koppelt een prikkel aan een gevolg?", "conditionering",
                  WL),
                 ("waar", "Geleerd gedrag wordt erfelijk aan de nakomelingen doorgegeven.", False),
                 ("open", "Noem een voordeel van aangeboren gedrag en een voordeel van geleerd gedrag.",
                  "Aangeboren gedrag werkt meteen, zonder dat er tijd is om iets te leren. Geleerd gedrag "
                  "kan bijgesteld worden als de omstandigheden veranderen.", 4),
             ]),
        dict(kop="Welke relatie tussen de soorten?",
             opdracht="Schrijf predatie, competitie, symbiose, parasitisme of commensalisme.",
             oefeningen=[
                 ("rij", [("een bij en een bloem", "symbiose"),
                          ("een teek op een hond", "parasitisme"),
                          ("een vos en een haas", "predatie")], "Welke relatie?", WW),
                 ("rij", [("een zeepok op een walvis", "commensalisme"),
                          ("twee meeuwen die om hetzelfde visje vechten", "competitie"),
                          ("een alg en een schimmel in een korstmos", "symbiose")], "Welke relatie?", WW),
                 ("tabel", ["Relatie", "Voor de een", "Voor de ander"],
                  [["predatie", None, None], ["parasitisme", None, None],
                   ["commensalisme", None, None], ["symbiose", None, None]],
                  "Predatie: voordeel voor de jager, nadeel (de dood) voor de prooi. Parasitisme: "
                  "voordeel voor de parasiet, nadeel voor de gastheer. Commensalisme: voordeel voor de "
                  "een, niets voor de ander. Symbiose: voordeel voor beide.", WW),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom doodt een parasiet zijn gastheer meestal niet?",
                  "De gastheer is zijn voeding en zijn woonplaats. Een parasiet die hem snel doodt, "
                  "verliest zijn eigen bestaan, dus blijft de schade meestal beperkt.", 4),
                 ("open", "Waarom is de competitie binnen een soort scherper dan tussen twee soorten?",
                  "Soortgenoten eten hetzelfde, nestelen op dezelfde plaats en zoeken dezelfde partner. "
                  "Hun behoeften overlappen dus volledig, terwijl die van twee soorten maar gedeeltelijk "
                  "overlappen.", 5),
                 ("open", "Twee vogelsoorten eten insecten in dezelfde bomen, de ene in de kruin en de "
                          "andere op de stam. Waarom kunnen ze naast elkaar blijven bestaan?",
                  "Ze eten hetzelfde maar niet op dezelfde plaats, dus overlappen hun niches maar "
                  "gedeeltelijk. Door die opdeling blijft de competitie beperkt en verdringt geen van de "
                  "twee de andere.", 5),
                 ("open", "Een roofdier verdwijnt uit een gebied. Beschrijf wat er daarna met de prooien "
                          "en met de planten gebeurt.",
                  "Zonder jager groeit de prooipopulatie sterk. Die vreet haar voedselplanten kaal, "
                  "waardoor ook de planten achteruitgaan en uiteindelijk de prooien zelf voedsel te kort "
                  "komen.", 5),
             ]),
        dict(kop="Leven in een groep",
             opdracht="Vul de tabel aan of leg uit.",
             oefeningen=[
                 ("tabel", ["", "Drie voordelen", "Twee nadelen"],
                  [["in een groep leven", None, None]],
                  "Voordelen: meer ogen zien een roofdier sneller aankomen, samen jagen levert grotere "
                  "prooien op, en de jongen kunnen samen beschermd worden. Nadelen: meer competitie om "
                  "voedsel, en ziekten verspreiden zich sneller.", WL),
                 ("kort", "Hoe noem je de rangorde waarbij het ene dier voorrang heeft op het andere?",
                  "een hiërarchie", WL),
                 ("kort", "Hoe noem je een geurstof waarmee soortgenoten elkaar iets doorgeven?",
                  "een feromoon", WL),
                 ("open", "Waarom spaart een vaste rangorde gevechten uit?",
                  "De uitkomst van een gevecht is al bekend, dus hoeft hij niet elke dag opnieuw "
                  "uitgevochten te worden. Dat spaart energie en kwetsuren.", 4),
                 ("open", "Een onderzoeker wil weten of muizen een doolhof leren. Beschrijf hoe hij dat "
                          "het best aanpakt.",
                  "Hij laat meerdere muizen het doolhof herhaaldelijk lopen en meet elke keer de tijd. "
                  "Daalt die tijd over de pogingen heen, dan leren ze. Met één muis of één poging meet "
                  "hij enkel toeval.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-materie-en-energiestromen-in-een-ecosysteem-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Materie- en energiestromen in een ecosysteem",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Autotroof of heterotroof?",
             opdracht="Schrijf wat past.",
             oefeningen=[
                 ("rij", [("een eik", "autotroof"),
                          ("een schimmel op een dode stam", "heterotroof"),
                          ("een alg in een vijver", "autotroof")], "Wat is het?", WW),
                 ("kort", "Welke energiebron gebruikt een autotroof organisme?", "zonlicht", WL),
             ]),
        dict(kop="Fotosynthese en celademhaling",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Fotosynthese", "Celademhaling"],
                  [["grondstoffen", None, None], ["producten", None, None],
                   ["waar in de cel", None, None], ["energie", None, None]],
                  "Grondstoffen: koolstofdioxide en water tegenover glucose en zuurstofgas. Producten: "
                  "glucose en zuurstofgas tegenover koolstofdioxide en water. Plaats: chloroplast "
                  "tegenover mitochondrion. Energie: opslaan tegenover vrijmaken.", WW),
                 ("waar", "Een plantencel doet zowel fotosynthese als celademhaling.", True),
                 ("waar", "Een dierlijke cel doet beide.", False),
                 ("open", "Leg uit waarom een plant bij daglicht netto zuurstofgas afgeeft en in het "
                          "donker netto koolstofdioxide.",
                  "De celademhaling loopt dag en nacht door. Bij licht is de fotosynthese veel sterker, "
                  "dus blijft er zuurstofgas over. In het donker valt de fotosynthese weg en blijft enkel "
                  "de celademhaling over.", 5),
             ]),
        dict(kop="Gisting en enzymen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("glucose afbreken zonder zuurstofgas", "gisting"),
                          ("de producten van alcoholgisting", "ethanol en koolstofdioxide"),
                          ("wat een spier bij zuurstofgebrek maakt", "melkzuur")], "Vul aan.", WL),
                 ("open", "Leg uit waarom gisting per molecule glucose minder energie oplevert dan de "
                          "celademhaling.",
                  "Bij gisting wordt de glucose maar gedeeltelijk afgebroken, dus blijft er nog energie "
                  "in de ethanol of het melkzuur zitten. Pas met zuurstofgas wordt ze helemaal "
                  "afgebroken tot koolstofdioxide en water.", 5),
                 ("kort", "Hoe noem je een stof die een omzetting versnelt zonder er zelf bij op te gaan?",
                  "een enzym", WL),
                 ("open", "Waarom werkt een enzym enkel binnen een nauw gebied van temperatuur en "
                          "zuurtegraad?",
                  "Een enzym past met zijn vorm op één bepaalde stof. Buiten dat gebied verliest het die "
                  "vorm, en dan past het niet meer en werkt het niet.", 4),
             ]),
        dict(kop="Voedselketens",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("maakt zelf organische stof met licht", "een producent"),
                          ("eet plantaardig materiaal", "een herbivoor"),
                          ("breekt dood materiaal af", "een reducent")], "Wat is het?", WL),
                 ("open", "Schrijf een voedselketen van vier schakels uit een weide, met de pijlen in de "
                          "juiste richting.",
                  "Gras, pijl, rups, pijl, mees, pijl, sperwer. De pijl wijst van het gegeten organisme "
                  "naar wie het eet, want hij volgt de stroom van stof en energie.", 4),
                 ("open", "Waarom geeft een voedselweb de werkelijkheid beter weer dan een voedselketen?",
                  "De meeste dieren eten meer dan één soort en worden ook door meer dan één soort "
                  "gegeten. Een keten is maar één draad uit dat web.", 4),
             ]),
        dict(kop="De energiepiramide",
             opdracht="Reken en leg uit.",
             oefeningen=[
                 ("kort", "Ongeveer welk deel van de energie van een niveau komt in het volgende "
                          "terecht?", "ongeveer een tiende", WL),
                 ("open", "De producenten van een weide leveren 10 000 kJ. Hoeveel komt er ongeveer bij "
                          "de tweede consument terecht? Schrijf je stappen op.",
                  "Van 10 000 kJ komt ongeveer een tiende bij de eerste consument: 1000 kJ. Daarvan komt "
                  "weer een tiende bij de tweede consument: ongeveer 100 kJ.", 5),
                 ("open", "Leg uit waarom er zelden meer dan vier of vijf trofische niveaus zijn.",
                  "Bij elke stap gaat het grootste deel van de energie verloren als warmte en voor de "
                  "eigen levensbehoeften. Na vier of vijf stappen blijft er te weinig over om nog een "
                  "niveau te onderhouden.", 5),
                 ("open", "Waarom voedt een stuk land meer mensen met graan dan met vlees?",
                  "Eet je het graan zelf, dan sla je een trofisch niveau over. Ga je langs het vee, dan "
                  "blijft er maar ongeveer een tiende van de energie over, dus is er veel meer land "
                  "nodig.", 5),
                 ("waar", "Materie gaat rond in kringlopen, energie stroomt er maar één keer door.",
                  True),
                 ("waar", "Zonder reducenten blijft een ecosysteem werken zolang de zon schijnt.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kringlopen-voedselrelaties-en-de-mens-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Kringlopen, voedselrelaties en de mens",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke kringloop?",
             opdracht="Schrijf koolstof, water, stikstof of fosfor.",
             oefeningen=[
                 ("rij", [("verdampen, condenseren en neerslaan", "water"),
                          ("bacteriën in wortelknolletjes van klaver", "stikstof"),
                          ("verbranden van steenkool en aardolie", "koolstof")], "Welke kringloop?", WW),
                 ("rij", [("heeft geen gasvorm in de lucht", "fosfor"),
                          ("transpiratie van bladeren", "water"),
                          ("de fotosynthese van een bos", "koolstof")], "Welke kringloop?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Dezelfde koolstofatomen worden telkens opnieuw gebruikt.", True),
                 ("waar", "Een groeiend bos legt koolstof vast in zijn hout.", True),
                 ("waar", "Planten kunnen stikstofgas uit de lucht rechtstreeks opnemen.", False),
                 ("waar", "De kringloop van fosfor verloopt sneller dan die van koolstof.", False),
                 ("waar", "Een abiotische factor is een niet-levende factor.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom stijgt het koolstofdioxidegehalte van de lucht?",
                  "We verbranden fossiele brandstoffen veel sneller dan de natuur die koolstof kan "
                  "vastleggen. Die koolstof zat miljoenen jaren opgesloten in de bodem, en nu voegen we "
                  "ze in korte tijd aan de kringloop toe.", 5),
                 ("open", "Beschrijf stap voor stap wat er bij eutrofiëring van een vijver gebeurt.",
                  "Door overbemesting woekeren de algen. Hun laag houdt het licht weg, dus sterven de "
                  "waterplanten. De reducenten die al dat dode materiaal verwerken, gebruiken de "
                  "zuurstof op. Daardoor sterven de vissen door zuurstofgebrek.", 6),
                 ("open", "Waarom staat er bij een hevige regen sneller water op een verharde straat dan "
                          "op een weide?",
                  "Een bodem met planten neemt het water op en geeft het traag door. Beton laat niets "
                  "door, dus loopt al het water meteen oppervlakkig weg naar de riool of de beek.", 5),
                 ("open", "Waarom is een gesloten kringloop op een boerderij gunstig?",
                  "Wat het vee eet, komt via de mest weer op de eigen akkers terecht. De mineralen "
                  "blijven dus op het bedrijf en er is minder aanvoer van buiten nodig.", 4),
             ]),
        dict(kop="Het ecosysteem in begrippen",
             opdracht="Schrijf het juiste woord.",
             oefeningen=[
                 ("rij", [("alle individuen van één soort in een gebied", "een populatie"),
                          ("het aantal dat een gebied blijvend kan onderhouden", "de draagkracht"),
                          ("het geheel van omstandigheden en rollen van een soort", "de niche")],
                  "Welk woord?", WL),
                 ("kort", "Hoe noem je een soort waarvan de aanwezigheid iets zegt over de toestand van "
                          "het milieu?", "een indicatorsoort", WL),
                 ("open", "Noem de drie dingen die bepalen of een populatie groeit of krimpt.",
                  "Het aantal geboorten, het aantal sterfgevallen, en het aantal dieren dat het gebied "
                  "binnenkomt of verlaat.", 4),
                 ("open", "Waarom kunnen twee soorten met precies dezelfde niche niet blijvend naast "
                          "elkaar bestaan?",
                  "Hun behoeften overlappen volledig, dus is de competitie ook volledig. Een van de twee "
                  "verdringt de andere, of een van de twee verschuift haar niche.", 5),
             ]),
        dict(kop="Successie en beheer",
             opdracht="Vul de tabel aan of leg uit.",
             oefeningen=[
                 ("tabel", ["Fase", "Wat er groeit"],
                  [["kale bodem", None], ["na enkele jaren", None], ["na tientallen jaren", None]],
                  "Kale bodem: pioniersplanten die weinig voeding en veel licht verdragen. Na enkele "
                  "jaren: grassen en kruiden op de eerste humus. Na tientallen jaren: struiken en "
                  "uiteindelijk bomen, dus bos.", WL),
                 ("open", "Waarom moet een natuurbeheerder die een heide wil behouden, er soms bomen "
                          "weghalen?",
                  "Zonder ingrijpen zet de successie door en wordt de heide eerst struweel en dan bos. "
                  "Door bomen weg te halen houdt de beheerder het systeem met opzet in een vroegere "
                  "fase.", 5),
                 ("open", "Een gemeente laat een beek weer kronkelen in plaats van recht door een buis. "
                          "Noem twee voordelen.",
                  "Het water stroomt trager, dus houdt de beek meer water vast bij hevige regen. En "
                  "bochten en ondiepe oevers geven veel meer soorten een leefplek.", 4),
             ]),
        dict(kop="De voetafdruk van de mens",
             opdracht="Kies of leg uit.",
             oefeningen=[
                 ("kies", "Welke keuze verkleint de ecologische voetafdruk het meest?",
                  ["elk jaar een nieuw toestel kopen",
                   "minder vlees eten en spullen langer gebruiken",
                   "vaker met het vliegtuig op reis gaan",
                   "de tuin volledig betegelen"], 1),
                 ("open", "Waarom heeft een plantaardig dieet gemiddeld een kleinere voetafdruk?",
                  "Vlees komt een trofisch niveau hoger, en bij die stap gaat het grootste deel van de "
                  "energie verloren. Voor dezelfde voeding is er dus veel meer land en water nodig.", 5),
                 ("open", "Waarom is de klimaatverandering ook een zaak van biodiversiteit?",
                  "Als het klimaat verschuift, kunnen soorten niet altijd meeverhuizen. Een soort op een "
                  "bergtop of in een versnipperd landschap kan niet opschuiven en verliest haar "
                  "leefgebied helemaal.", 5),
                 ("open", "In een gebied verdwijnen de bijen. Wat verwacht je in de jaren erna?",
                  "Plantensoorten die van bestuiving door insecten afhangen, zetten minder vrucht. Hun "
                  "zaadzetting daalt en daarna neemt ook hun aantal af.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-levensreddend-handelen-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Levensreddend handelen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE + ["Dit zijn vragen om de theorie in te oefenen. Echt leren reanimeren doe je op een cursus "
               "met een pop."],
    reeksen=[
        dict(kop="De eerste stappen",
             opdracht="Schrijf de stappen onder elkaar.",
             oefeningen=[
                 ("open", "Je vindt iemand op straat die op de grond ligt. Schrijf de eerste vier "
                          "stappen op, in de juiste orde.",
                  "Eerst kijken of de plaats veilig is. Dan de persoon aanspreken en zacht aan de "
                  "schouders schudden. Dan kijken of hij normaal ademt. Dan 112 bellen en handelen naar "
                  "wat je vastgesteld hebt.", 6),
                 ("kort", "Welk noodnummer bel je voor een ziekenwagen?", "112", W),
                 ("open", "Noem de drie dingen die je zeker zegt als je het noodnummer belt.",
                  "Waar je precies bent, wat er gebeurd is, en hoeveel slachtoffers er zijn en in welke "
                  "toestand.", 4),
             ]),
        dict(kop="Wat doe je in dit geval?",
             opdracht="Schrijf kort wat je doet.",
             oefeningen=[
                 ("rij", [("reageert niet, ademt normaal", "stabiele zijligging en 112"),
                          ("reageert niet, ademt niet normaal", "reanimeren en 112"),
                          ("verslikt zich, hoest krachtig", "laten doorhoesten en erbij blijven")],
                  "Wat doe je?", WL),
                 ("rij", [("verslikt zich, kan niet meer hoesten", "vijf slagen, dan vijf buikstoten"),
                          ("hevige bloeding aan de arm", "stevig op de wonde drukken"),
                          ("brandwond aan de hand", "20 minuten lauw stromend water")],
                  "Wat doe je?", WL),
             ]),
        dict(kop="Reanimeren",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Bij een volwassene"],
                  [["compressies per reeks", None], ["beademingen per reeks", None],
                   ["compressies per minuut", None], ["diepte", None], ["plaats van de handen", None]],
                  "30 compressies, 2 beademingen, 100 tot 120 per minuut, ongeveer vijf centimeter diep, "
                  "met de hiel van je hand midden op het borstbeen.", WW),
                 ("waar", "Je onderbreekt de hartmassage zo vaak mogelijk om te controleren.", False),
                 ("open", "Je staat er alleen voor bij iemand die niet reageert en niet normaal ademt. "
                          "Wat doe je?",
                  "Je belt 112 met de luidspreker aan en begint tegelijk te reanimeren. Zo verlies je "
                  "geen tijd en kan de centralist je ondertussen helpen.", 4),
                 ("open", "Het slachtoffer begint tijdens de reanimatie weer normaal te ademen. Wat doe "
                          "je dan?",
                  "Je stopt met de massage en legt hem in stabiele zijligging. Je blijft wel kijken of de "
                  "ademhaling normaal blijft tot de hulpdiensten er zijn.", 4),
             ]),
        dict(kop="De AED",
             opdracht="Kies of leg uit.",
             oefeningen=[
                 ("kies", "Wanneer geeft een AED een schok?",
                  ["altijd zodra je hem aanzet",
                   "enkel als hij in het hartritme vaststelt dat het nodig is",
                   "enkel als een arts het bevestigt",
                   "nooit, hij meet alleen"], 1),
                 ("waar", "Iemand zonder opleiding mag een AED gebruiken.", True),
                 ("open", "Noem drie dingen die bij het gebruik van een AED horen.",
                  "Het toestel aanzetten en de aanwijzingen volgen, de elektroden op de ontblote "
                  "borstkas kleven, en niemand aanraken op het ogenblik van de schok.", 4),
             ]),
        dict(kop="Wat je vooral niet doet",
             opdracht="Schrijf bij elke situatie wat je niet doet, en waarom niet.",
             oefeningen=[
                 ("open", "Bij een brandwond.",
                  "Geen boter, tandpasta of zalf erop doen: vette stoffen houden de warmte juist vast en "
                  "maken het nazicht moeilijker. En de blaar niet openprikken, want die is een steriel "
                  "dekseltje over de wonde.", 5),
                 ("open", "Bij een vermoedelijke botbreuk of een nek- of rugwonde.",
                  "Het bot niet rechttrekken, want dat kan zenuwen en bloedvaten beschadigen. En bij een "
                  "nek- of rugwonde het slachtoffer niet verplaatsen, tenzij er onmiddellijk gevaar is, "
                  "want verplaatsen kan het ruggemerg beschadigen.", 5),
                 ("open", "Bij iemand in shock.",
                  "Niets te drinken geven: hij kan zich verslikken en moet misschien dringend "
                  "geopereerd worden. Je houdt hem warm en belt 112.", 4),
                 ("open", "Bij een epileptische aanval.",
                  "De persoon niet vasthouden en niets tussen de tanden steken. Je zorgt dat hij zich "
                  "niet kan stoten en legt iets zachts onder het hoofd.", 4),
             ]),
        dict(kop="Begrippen en benodigdheden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Waarvoor staat de afkorting AED?", "automatische externe defibrillator", WL),
                 ("kort", "Hoe noem je de houding waarin je een bewusteloos slachtoffer legt dat normaal "
                          "ademt?", "de stabiele zijligging", WL),
                 ("open", "Noem drie dingen die in een eenvoudige verbanddoos horen, en zeg waarom je een "
                          "wonde met water en niet met alcohol spoelt.",
                  "Steriele compressen, een rol kleefpleister met een zwachtel, en wegwerphandschoenen. "
                  "Alcohol beschadigt het weefsel van de wonde, water niet.", 5),
                 ("open", "Waarom is het nuttig dat zoveel mensen mogelijk kunnen reanimeren?",
                  "Zonder bloedtoevoer raken de hersenen in enkele minuten beschadigd, en de "
                  "hulpdiensten zijn er niet meteen. Een omstaander overbrugt net die eerste minuten, en "
                  "dat bepaalt de kans om te overleven.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-wetenschappelijk-onderzoek-en-stem-biologie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Wetenschappelijk onderzoek en STEM",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Schrijf het juiste woord.",
             oefeningen=[
                 ("rij", [("de factor die je zelf verandert", "de onafhankelijke variabele"),
                          ("de factor die je meet", "de afhankelijke variabele"),
                          ("de groep zonder behandeling", "de controlegroep")], "Welk woord?", WL),
                 ("rij", [("een beredeneerde verwachting die je kan toetsen", "een hypothese"),
                          ("een meetpunt dat sterk afwijkt", "een uitschieter"),
                          ("een tweede factor die mee veranderde", "een storende variabele")],
                  "Welk woord?", WL),
             ]),
        dict(kop="Een proef beoordelen",
             opdracht="Schrijf bij elke opzet wat er misgaat.",
             oefeningen=[
                 ("open", "Een leerling zet twee plantjes neer, één in het licht en één in het donker, "
                          "en besluit na een week dat licht de groei bevordert.",
                  "Twee plantjes zijn te weinig om toeval uit te sluiten: de ene plant kan van nature "
                  "sterker zijn. Hij heeft meerdere exemplaren per groep nodig en moet de proef "
                  "herhalen.", 5),
                 ("open", "Een andere leerling zet de ene groep plantjes in het licht op de "
                          "verwarming en de andere in het donker op de koude vloer.",
                  "Er veranderen twee factoren tegelijk, licht en temperatuur. Daardoor kan hij een "
                  "verschil niet aan één oorzaak toeschrijven. De temperatuur is hier een storende "
                  "variabele en moet constant blijven.", 5),
                 ("open", "Een derde leerling laat zijn controlegroep weg, want die krijgt toch geen "
                          "behandeling.",
                  "Zonder controlegroep weet hij niet wat er zonder behandeling gebeurd zou zijn. De "
                  "vergelijking is net de kern van een proef, dus kan hij geen betrouwbaar besluit "
                  "trekken.", 5),
                 ("waar", "Een onderzoeker mag een meting aanpassen als ze niet bij zijn hypothese past.",
                  False),
                 ("waar", "Een weerlegde hypothese maakt het onderzoek mislukt.", False),
             ]),
        dict(kop="Een eigen proefopzet",
             opdracht="Werk de opzet uit.",
             oefeningen=[
                 ("open", "Je wil weten of bonenplantjes beter groeien met wat klaver ernaast. Schrijf "
                          "de onderzoeksvraag, de hypothese, de onafhankelijke en de afhankelijke "
                          "variabele, en wat je constant houdt.",
                  "Vraag: groeien bonenplantjes beter als er klaver naast staat? Hypothese: ja, want de "
                  "bacteriën in de wortelknolletjes van klaver maken stikstof bruikbaar. Onafhankelijk: "
                  "wel of geen klaver ernaast. Afhankelijk: de lengte of de massa van de bonenplantjes "
                  "na enkele weken. Constant: potgrond, water, licht, temperatuur en het aantal "
                  "plantjes per pot.", 8),
             ]),
        dict(kop="De microscoop",
             opdracht="Reken en vul aan.",
             oefeningen=[
                 ("rij", [("oculair 10 keer, objectief 10 keer", "100 keer"),
                          ("oculair 10 keer, objectief 40 keer", "400 keer"),
                          ("oculair 15 keer, objectief 40 keer", "600 keer")], "Totale vergroting?", WW),
                 ("open", "Waarom begin je altijd met het zwakste objectief?",
                  "Bij een zwakke vergroting is het beeldveld het grootst, dus vind je je voorwerp "
                  "makkelijker. Hoe sterker je vergroot, hoe kleiner het stukje preparaat dat je nog "
                  "ziet.", 4),
                 ("rij", [("houdt het preparaat vlak en voorkomt uitdrogen", "het dekglaasje"),
                          ("geeft contrast aan doorzichtige celonderdelen", "een kleurstof"),
                          ("rond, met een scherpe donkere rand, lijkt op een cel", "een luchtbel")],
                  "Wat is het?", WL),
                 ("waar", "Met een lichtmicroscoop kan je virussen in detail bekijken.", False),
             ]),
        dict(kop="Veilig werken",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "In een labo eet en drink je niet.", True),
                 ("waar", "Lange haren maak je vast als je met een vlam werkt.", True),
                 ("waar", "Een stof die je niet kan benoemen, mag je voorzichtig ruiken om ze te "
                          "herkennen.", False),
                 ("waar", "Zelf stoffen mengen om te zien wat er gebeurt, hoort bij onderzoekend leren.",
                  False),
             ]),
        dict(kop="Gegevens weergeven",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("losse categorieën, zoals soorten vogels", "een staafdiagram"),
                          ("een grootheid die vloeiend verandert, zoals temperatuur", "een lijndiagram")],
                  "Welk diagram?", WL),
                 ("open", "Noem de drie dingen die bij elke as van een grafiek horen, en zeg wat er op de "
                          "horizontale as komt.",
                  "De naam van de grootheid, de eenheid en een schaal met getallen. Op de horizontale as "
                  "komt de onafhankelijke variabele, die je zelf ingesteld hebt.", 5),
                 ("open", "Een leerling noteert een bladlengte als 4. Wat ontbreekt er, en hoe los je dat "
                          "op?",
                  "De eenheid ontbreekt, dus weet niemand of het millimeter of centimeter is. Zet de "
                  "eenheid één keer bovenaan de kolom van de tabel, of schrijf 4 cm.", 4),
                 ("open", "Je leest op een website dat een plant beter groeit met muziek. Noem drie "
                          "dingen waar je als onderzoeker naar kijkt.",
                  "Of er een proef met controlegroep achter zit, hoeveel planten er gebruikt werden, en "
                  "wie het onderzoek betaalde. Dat laatste kan een belang bij de uitkomst betekenen.", 5),
             ]),
        dict(kop="STEM",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Waarvoor staat STEM?",
                  "wetenschappen, technologie, ingenieurswetenschappen en wiskunde", WL),
                 ("open", "Een klas wil een vijver gezonder maken. Waarom begin je met meten en niet met "
                          "bouwen?",
                  "Zonder beginmeting weet je achteraf niet of je oplossing iets veranderd heeft. De "
                  "cyclus is dus meten, ontwerpen, uitvoeren en opnieuw meten.", 4),
             ]),
    ],
)


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-homeostase-en-waterhuishouding-bij-planten-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Werk van buiten naar binnen: eerst de organen, dan de weefsels, dan de lagen. Zo zit "
                    "elke naam op zijn plaats in het geheel.",
             waarom=[
                 None,
                 "Onthoud het aan de naam: xyleem is hout en voert water, floëem komt van vloeien en voert "
                 "het sap met suikers.",
                 "De cuticula ligt op de epidermis; ze is geen cellaag maar een waslaagje dat die cellen "
                 "afdekken.",
             ]),
        dict(aanpak="Vraag je bij elke bewering af welke kracht of welke stof er precies genoemd wordt. Eén "
                    "verkeerd woord maakt een hele zin fout.",
             waarom=[
                 None,
                 "De turgor is de druk van het water ván binnenuit tegen de celwand. Dat is wat een plant "
                 "rechthoudt.",
                 "De zwaartekracht werkt juist tegen: het water moet eróp. Dat is net waarom er drie "
                 "krachten nodig zijn.",
                 "Hier zie je de keuze die de plant moet maken: water sparen of fotosynthese doen. Allebei "
                 "tegelijk gaat niet.",
                 "De kleur van de bloemblaadjes heeft met bestuivers te maken, niet met water. Let op zulke "
                 "beweringen die alleen biologisch klinken.",
             ]),
        dict(aanpak="Drie krachten tillen het water omhoog: worteldruk duwt, transpiratiezuiging trekt, "
                    "capillariteit helpt in de nauwe vaten.",
             waarom=[
                 "De transpiratiezuiging is veruit de sterkste van de drie. Worteldruk alleen zou nooit tot "
                 "in de kruin van een boom komen.",
             ]),
        dict(aanpak="Leg bij zulke vragen altijd twee dingen uit: wat de plant wint en wat ze verliest. Een "
                    "plant kiest altijd tussen water en koolstofdioxide.",
             waarom=[None, None, None]),
        dict(aanpak="Een plant heeft geen zenuwen maar hormonen. Elk hormoon doet één ding; leer ze aan dat "
                    "ene effect.",
             waarom=[
                 "Auxine verzamelt zich aan de donkere kant, waar de cellen dan sterker strekken. Daardoor "
                 "buigt de stengel naar het licht toe.",
                 "Bij een tropie bepaalt de prikkel de richting. Een blad dat dichtklapt of een bloem die "
                 "opengaat, doet dat altijd op dezelfde manier: dat zijn nastieën.",
                 None,
                 "Een plant heeft geen zenuwen en geen centraal orgaan. Alles verloopt via hormonen, en "
                 "daarom duurt het ook veel langer.",
             ]),
        dict(aanpak="De fotosynthese verbindt dit hele hoofdstuk: water, licht en koolstofdioxide komen er "
                    "samen. Zonder water geen fotosynthese.",
             waarom=[
                 "Tel de atomen links en rechts na; de vergelijking moet kloppen. De zes voor het water en "
                 "de koolstofdioxide zijn geen versiering.",
                 None,
                 "Noem alle drie de manieren: water als grondstof, open huidmondjes, en het aanvoeren van "
                 "mineralen. Eén ervan is zelden genoeg voor de punten.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-van-prikkel-tot-reactie-en-het-zenuwstelsel-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zet eerst de vijf schakels op een rij, en vul daarna bij elke schakel in wat ze in dit "
                    "voorbeeld is. Werk nooit omgekeerd.",
             waarom=[
                 "De punten zitten in het invullen: niet enkel receptor noemen maar ook zeggen dat het hier "
                 "de haarcellen in het oor zijn.",
             ]),
        dict(aanpak="Een receptor vangt op, een effector voert uit. Vraag je af of het orgaan iets "
                    "waarneemt of iets doet.",
             waarom=[
                 "Een klier is ook een effector, net als een spier. Effector betekent uitvoerder, niet "
                 "beweger.",
                 None,
             ]),
        dict(aanpak="Zet bij elke reflex de prikkel en de reactie apart. Een reflex is altijd dat vaste "
                    "paar.",
             waarom=[
                 None,
                 "Dat de overschakeling níét in de grote hersenen gebeurt, is net wat een reflex snel "
                 "maakt.",
                 "Sommige reflexen kan je onderdrukken, zoals knipperen, maar de pupilreflex en de "
                 "kniepeesreflex niet. Daarom test een arts die laatste.",
             ]),
        dict(aanpak="Drie delen, drie taken: de hersenstam houdt je in leven, de grote hersenen denken, de "
                    "kleine hersenen stemmen af.",
             waarom=[None, None, None]),
        dict(aanpak="Volg het signaal door het neuron: binnen bij de dendrieten, buiten langs het ene axon. "
                    "De bouw bepaalt de richting.",
             waarom=[
                 None, None,
                 "Veel ingangen en één uitgang: dat is de hele bouw van een neuron, en de reden dat het "
                 "signalen kan samenvoegen.",
                 "Dat springen heet saltatoire geleiding. Het is de reden dat een gemyeliniseerde vezel "
                 "tientallen keren sneller is.",
             ]),
        dict(aanpak="Vergelijk telkens op drie punten: snelheid, waar het overschakelt, en hoe lang het "
                    "effect duurt.",
             waarom=[
                 None,
                 "Dit is de reden dat je beide stelsels nodig hebt: snel en kort tegenover traag en lang. "
                 "Ze vullen elkaar aan.",
                 "Blaasjes aan de ene kant, receptoren aan de andere: daarom kan het signaal maar één kant "
                 "op.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-oog-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Volg het licht van buiten naar binnen. Die ene rij is de ruggengraat van het hele "
                    "hoofdstuk.",
             waarom=[
                 "Let op dat het hoornvlies vóór de pupil komt: de pupil is een gat in de iris, en die ligt "
                 "erachter.",
             ]),
        dict(aanpak="Zet bij elk deel zijn taak. De drie vliezen van buiten naar binnen zijn het harde "
                    "oogvlies, het vaatvlies en het netvlies.",
             waarom=[
                 "Het vaatvlies is zwart van binnen; dat neemt het strooilicht weg, zoals de zwarte "
                 "binnenkant van een fototoestel.",
                 None,
             ]),
        dict(aanpak="Staafjes en kegeltjes verschillen op drie punten: licht, kleur en plaats. Zet die drie "
                    "altijd naast elkaar.",
             waarom=[
                 "Dat de staafjes buiten het midden liggen, verklaart waarom je een zwakke ster beter ziet "
                 "als je er net naast kijkt.",
                 None, None,
                 "De hersenen draaien het beeld terug om. Wat je ziet, is dus al verwerkt.",
             ]),
        dict(aanpak="Accommodatie is het boller of platter worden van de lens. Dichtbij vraagt meer buiging, "
                    "dus een bollere lens.",
             waarom=[
                 None,
                 "Let op het woord ontspannen: de lens is van zichzelf bol, en het kringspiertje laat hem "
                 "boller worden door los te laten van de spanning.",
                 "Noem beide redenen. Dat de hersenen aanvullen, is het verrassende deel van het antwoord.",
             ]),
        dict(aanpak="Bij elke afwijking: waar valt het beeld, en welke lens brengt het terug op het "
                    "netvlies. Dat is telkens dezelfde redenering.",
             waarom=[
                 "Bijziend betekent dichtbij goed zien; het beeld valt dan vóór het netvlies. Die "
                 "koppeling is het makkelijkst te onthouden.",
                 None,
                 "Een verkeerde bril geeft hoofdpijn en vermoeide ogen, maar beschadigt het netvlies niet. "
                 "Let op zulke overdreven beweringen.",
                 "Ouderdomsverziendheid komt van een stijvere lens, gewone verziendheid van een te korte "
                 "oogbol. Dezelfde klacht, een andere oorzaak.",
             ]),
        dict(aanpak="Zien gebeurt pas in de hersenen. Het oog levert enkel impulsen aan.",
             waarom=[
                 "Dit heet stereozicht. Het verklaart ook waarom iemand met één oog moeilijker kan "
                 "inschatten hoe ver iets ligt.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-oor-en-het-evenwicht-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie delen in de volgorde waarin het geluid ze doorloopt: uitwendig, midden, "
                    "inwendig. Elk deel heeft zijn eigen soort trilling.",
             waarom=[
                 None,
                 "De buis van Eustachius verbindt het middenoor met de keel. Daarom kan je de druk erin "
                 "bijsturen door te slikken.",
             ]),
        dict(aanpak="Zet bij elke schakel ook de drager erbij: lucht, vast of vloeistof. Dat is net wat deze "
                    "opdracht toetst.",
             waarom=[
                 "Het geluid verandert driemaal van drager. Juist daarvoor dienen de gehoorbeentjes: de "
                 "trilling van lucht naar vloeistof overzetten.",
             ]),
        dict(aanpak="Vraag je bij elke bewering af wat er precies trilt en wat er vervangen of hersteld "
                    "wordt.",
             waarom=[
                 "Ze maken de trilling krachtiger omdat het trommelvel veel groter is dan het venster "
                 "waarop de stijgbeugel duwt. Zonder die versterking zou het geluid in de vloeistof "
                 "verloren gaan.",
                 "In het slakkenhuis zit vloeistof. Dat is net waarom het geluid versterkt moet worden.",
                 "Dat haarcellen niet teruggroeien, is de reden dat lawaaischade blijvend is. Oordopjes op "
                 "een fuif zijn dus geen overdreven voorzorg.",
                 "Een hoortoestel versterkt enkel het geluid. Het herstelt niets; het maakt alleen beter "
                 "bruikbaar wat er nog over is.",
                 None,
             ]),
        dict(aanpak="Leg bij zulke vragen altijd de bouw en het gevolg samen uit. De vorm van het "
                    "slakkenhuis verklaart drie van deze antwoorden.",
             waarom=[
                 None,
                 "Dit heet de plaatstheorie: elke toonhoogte heeft haar eigen plek. Daarom kan een "
                 "gehoortest per frequentie meten.",
                 "Het begin van het slakkenhuis krijgt álle geluid te verwerken. Daarom slijten juist de "
                 "haarcellen voor de hoge tonen het eerst.",
             ]),
        dict(aanpak="Het evenwichtsorgaan meet twee dingen: de stand van je hoofd en de draai ervan. Twee "
                    "soorten informatie, twee soorten structuren.",
             waarom=[
                 "De zakjes met gewichtjes meten stand, de kanaaltjes meten draai. Die twee uit elkaar "
                 "houden is het halve hoofdstuk.",
                 None,
                 "Dezelfde traagheid als bij de bus die remt. Eén natuurkundig begrip, twee vakken.",
                 "Drie richtingen, drie vlakken: knikken, kantelen en rondkijken. Daarom precies drie "
                 "kanalen.",
             ]),
        dict(aanpak="Duizeligheid en wagenziekte ontstaan allebei doordat je oor en je ogen iets anders "
                    "melden. Zoek dus altijd het conflict.",
             waarom=[
                 None,
                 "Hier zie je waarom het advies werkt: naar buiten kijken maakt de twee berichten weer "
                 "gelijk. Dat is de hele uitleg.",
                 "Je evenwicht komt uit drie bronnen tegelijk. Daarom kan je ook op één been staan met je "
                 "ogen dicht, maar veel moeilijker.",
                 "De signalen gaan eerst naar de hersenen, die ze met de ogen en de spieren vergelijken. "
                 "Pas daarna volgt een reactie.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-de-spieren-en-de-klieren-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Twee vragen apart: is het gestreept, en stuur je het zelf. Het hartspierweefsel is "
                    "gestreept én onwillekeurig.",
             waarom=[
                 None,
                 "Het hart is de uitzondering die elk examen graag vraagt: gestreept maar niet door jou "
                 "aan te sturen.",
             ]),
        dict(aanpak="Hou vast dat de filamenten niet korter worden maar langs elkaar schuiven. Elk antwoord "
                    "in deze reeks volgt uit dat ene beeld.",
             waarom=[
                 "Actine is dun, myosine is dik. Onthoud het aan de letters: myosine is massiever.",
                 None,
                 "De filamenten blijven even lang. Dat is net waarom de banden van breedte veranderen en "
                 "niet de filamenten zelf.",
                 "De lichte band bevat alleen actine, en die wordt overdekt wanneer de filamenten in elkaar "
                 "schuiven. Daarom wordt juist die band smaller.",
                 "In de donkere band ligt de myosine, met de actine die ertussen schuift. De lichte band is "
                 "die met alleen actine.",
                 None,
             ]),
        dict(aanpak="Een spier heeft drie dingen nodig: een prikkel, energie en calcium. Mist er één, dan "
                    "trekt ze niet samen.",
             waarom=[
                 None,
                 "Vergeet het calcium niet. Dat is de schakel tussen de zenuwprikkel en het vastgrijpen van "
                 "de myosinekopjes.",
                 "Dit is anaërobe verbranding: zonder genoeg zuurstof blijft melkzuur over. Met rust en "
                 "zuurstof wordt dat weer afgebroken.",
                 None,
             ]),
        dict(aanpak="Zet bij elke klier haar hormoon en het effect. Een hormoon werkt traag maar lang, een "
                    "zenuwimpuls snel maar kort.",
             waarom=[
                 None,
                 "Zo'n klier heet endocrien. Een klier mét afvoergang, zoals de zweetklier, is exocrien.",
                 "Dat is het sleutel-slotprincipe. Het verklaart waarom een hormoon overal komt en toch "
                 "maar op bepaalde plaatsen iets doet.",
                 "Een zenuwimpuls werkt in milliseconden, een hormoon in minuten tot dagen. De traagheid "
                 "is net de prijs voor de duur.",
                 "Noem ook wat er trager gaat: de spijsvertering. Adrenaline zet het lichaam klaar om te "
                 "vechten of te vluchten, niet om te verteren.",
             ]),
        dict(aanpak="De bètacel verlaagt, de alfacel verhoogt. Beschrijf bij elke vraag de hele kring, niet "
                    "enkel het hormoon.",
             waarom=[
                 "Onthoud ze aan de letters: bèta hoort bij insuline, alfa bij glucagon.",
                 "Beschrijf alle vier de stappen. Een antwoord dat enkel insuline noemt, toont de "
                 "terugkoppeling niet.",
                 "Homeostase vraagt twee tegengestelde regelaars. Met één hormoon kan je enkel in één "
                 "richting bijsturen.",
                 "Bij type 1 ligt het aan de bètacellen zelf, bij type 2 reageren de lichaamscellen minder "
                 "goed op insuline. Dat verschil bepaalt de behandeling.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-voortplanting-en-de-menstruatiecyclus-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Deze woorden komen in de hele bundel terug. Leer ze met het moment waarop ze in het "
                    "verhaal voorkomen.",
             waarom=[
                 None,
                 "Het geel lichaam is wat na de ovulatie van de follikel overblijft. Het maakt progesteron, "
                 "en dat verklaart de hele tweede helft van de cyclus.",
                 "Een gameet heeft de helft van 46. Juist daarom heeft de zygote er na de bevruchting weer "
                 "46.",
             ]),
        dict(aanpak="Vraag je bij elke bewering af welk orgaan of welk hormoon er genoemd wordt. Eén "
                    "verkeerde naam maakt de zin fout.",
             waarom=[
                 None,
                 "De twee bloedbanen lopen vlak langs elkaar maar blijven gescheiden. Alleen de stoffen "
                 "gaan door de dunne wand.",
                 "Alcohol, nicotine en veel medicijnen passeren wel. Daarom geldt het advies over alcohol "
                 "tijdens de zwangerschap.",
                 "De hypofyse stuurt de geslachtsklieren aan, niet de schildklier. Die regelt de "
                 "stofwisseling.",
                 "Een eeneiige tweeling komt uit één bevruchte eicel die zich gesplitst heeft. Een "
                 "twee-eiige komt uit twee eicellen en lijkt dus op gewone broers of zussen.",
             ]),
        dict(aanpak="Drie structuren met elk hun taak: uitwisselen, verbinden en beschermen. Zet die taken "
                    "erbij, niet enkel de namen.",
             waarom=[None, None]),
        dict(aanpak="De cyclus heeft twee hormonale fasen rond de ovulatie: oestrogeen bouwt op, "
                    "progesteron houdt in stand.",
             waarom=[
                 "Luteaal komt van het geel lichaam, het corpus luteum. De naam van de fase zegt dus welk "
                 "orgaan er werkt.",
                 None, None,
                 "Beschrijf de ketting: geel lichaam weg, progesteron weg, slijmvlies los. Elke stap volgt "
                 "uit de vorige.",
             ]),
        dict(aanpak="De cyclus is een terugkoppeling tussen hypofyse en eierstok. Bijna elke vraag erover "
                    "is een vraag over die kring.",
             waarom=[
                 None,
                 "De luteale fase duurt bij bijna iedereen ongeveer veertien dagen. Een langere cyclus komt "
                 "dus door een langere eerste helft.",
                 "Noem ook de twee tekens waarop je wél kan letten. Een antwoord dat enkel zegt dat het niet "
                 "kan, is maar half af.",
                 "De pil werkt dus niet op de eierstok zelf maar op de hypofyse. Het is terugkoppeling die "
                 "van buitenaf nagebootst wordt.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-biodiversiteit-en-micro-organismen-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Biodiversiteit bestaat op drie niveaus: binnen een soort (genen), tussen soorten, en "
                    "tussen ecosystemen. Vraag je af waartussen het verschil zit.",
             waarom=[
                 "Verschil binnen één soort is genetische diversiteit. Dat niveau wordt het vaakst "
                 "vergeten, en het is net het belangrijkste voor overleven.",
                 "Vruchtbare nakomelingen is het beslissende woord: een paard en een ezel krijgen wel een "
                 "muildier, maar dat is onvruchtbaar.",
             ]),
        dict(aanpak="Vraag je bij elke bewering af of ze over een soort, over een middel of over een "
                    "verband gaat. Twee ervan zijn klassieke misverstanden.",
             waarom=[
                 "Dit heet veerkracht: meer soorten betekent meer kans dat een andere soort een rol kan "
                 "overnemen.",
                 "Dat zijn het geslacht en de soort, in het Latijn. Daardoor begrijpt een onderzoeker in "
                 "elk land welke soort je bedoelt.",
                 None,
                 "Antibiotica werken enkel tegen bacteriën. Daarom krijg je er bij een griep geen.",
                 "De meeste bacteriën in en op ons zijn nuttig of onschadelijk. Je darmmicrobioom helpt "
                 "zelfs verteren.",
             ]),
        dict(aanpak="Zet bij elke bedreiging de oplossing die ze rechtstreeks aanpakt. Een algemene zin "
                    "over natuur beschermen levert geen punten op.",
             waarom=[
                 None,
                 "Dit is de kern: niet de oppervlakte telt maar de verbinding. Kleine, gescheiden groepen "
                 "verliezen hun genetische variatie.",
                 "Noem concrete dingen, geen goede voornemens. Inheemse planten, een verwilderd hoekje en "
                 "geen gif zijn drie echte maatregelen.",
             ]),
        dict(aanpak="Drie groepen, drie verschillen: een bacterie is een cel, een virus is geen cel, een "
                    "schimmel heeft wel een echte kern.",
             waarom=[
                 None,
                 "Geen eigen stofwisseling is net waarom men twijfelt of een virus leeft. Het heeft altijd "
                 "een gastheercel nodig.",
                 "Zeg erbij waaróp een antibioticum ingrijpt, zoals de celwand. Een virus heeft dat niet, "
                 "en daarom werkt het middel niet.",
                 "Hier zie je selectie aan het werk, net als bij evolutie. De kuur afmaken is dus geen "
                 "formaliteit maar de kern van het middel.",
             ]),
        dict(aanpak="Micro-organismen doen in de keuken en in de natuur hetzelfde: ze breken stoffen af. "
                    "Alleen het doel verschilt.",
             waarom=[
                 None,
                 "Zonder reducenten stopt de kringloop. Dat is de rol die in bijna elke ecosysteemvraag "
                 "terugkomt.",
             ]),
        dict(aanpak="De afweer werkt in lagen: eerst buitenkant tegenhouden, dan algemeen opruimen, dan "
                    "gericht met antistoffen.",
             waarom=[
                 "Dit zijn de barrières die er altijd zijn, nog vóór je afweersysteem iets doet. Daarom "
                 "heet een wonde een poort voor infectie.",
                 None,
                 "Zeg erbij dat je er niet ziek van wordt. Dat is precies het verschil tussen een vaccin en "
                 "de ziekte zelf doormaken.",
                 "Hygiëne werkt op de weg van besmetting, niet op het micro-organisme. Daarom is het zo "
                 "doeltreffend en zo goedkoop.",
                 "Reken het na: een bacterie die zich elk half uur deelt, is na tien uur miljoenen keer "
                 "talrijker. Dat is waarom de koelkast bestaat.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-gedrag-en-interactie-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Vraag je af of het dier het moest meemaken om het te kunnen. Zo niet, dan is het "
                    "aangeboren.",
             waarom=[
                 None,
                 "Een spin leert haar web van niemand: ze bouwt het de eerste keer al goed. Dat is het "
                 "bewijs dat het aangeboren is.",
             ]),
        dict(aanpak="Elke leervorm heeft één kenmerk: gewenning laat een reactie wegvallen, conditionering "
                    "koppelt, inprenting gebeurt eenmalig en vroeg.",
             waarom=[
                 "Gewenning is geen vergeten maar leren dat een prikkel niets betekent. Daarom werkt een "
                 "vogelverschrikker na een tijd niet meer.",
                 None,
                 "Wat je leert, gaat niet in je genen zitten. Het wordt wel doorgegeven door het voor te "
                 "doen, en dat is cultuur en geen erfelijkheid.",
                 "Noem bij allebei het voordeel. Het verschil is snelheid tegenover aanpasbaarheid.",
             ]),
        dict(aanpak="Zet bij elke relatie wie voordeel heeft en wie nadeel. Twee keer voordeel is symbiose, "
                    "voordeel plus niets is commensalisme.",
             waarom=[
                 None, None,
                 "De tabel is het kerntje van dit hoofdstuk: vul hem in met plus, min en nul, dan heb je "
                 "alle vier de relaties in één oogopslag.",
             ]),
        dict(aanpak="Deze vragen gaan over evenwicht tussen soorten. Denk telkens door wat er na de eerste "
                    "verandering gebeurt.",
             waarom=[
                 None,
                 "Dit is het begrip niche: hoe meer de behoeften overlappen, hoe scherper de competitie. "
                 "Soortgenoten overlappen volledig.",
                 "Dit heet nichedifferentiatie. Hetzelfde voedsel op een andere plaats halen, is genoeg om "
                 "samen te bestaan.",
                 "Beschrijf de hele ketting: prooien eerst meer, dan de planten kaal, dan de prooien zelf "
                 "in de problemen. Het eindigt niet bij het eerste gevolg.",
             ]),
        dict(aanpak="Een groep brengt voordelen en nadelen tegelijk. Noem er altijd van allebei, en zeg "
                    "waarvoor een rangorde dient.",
             waarom=[
                 None, None, None,
                 "Een hiërarchie bespaart gevechten en dus energie. Ze bestaat niet om de sterkste te "
                 "belonen maar om conflicten kort te houden.",
                 "Herhaling en meerdere dieren: dat is de kern van elke proef over gedrag. Met één dier en "
                 "één poging meet je toeval.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-materie-en-energiestromen-in-een-ecosysteem-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Autotroof maakt zelf organische stof, heterotroof haalt ze uit een ander organisme. "
                    "Auto is zelf, hetero is anders.",
             waarom=[
                 "Een schimmel is heterotroof, al lijkt hij op een plant. Hij heeft geen bladgroen en "
                 "breekt af in plaats van op te bouwen.",
                 None,
             ]),
        dict(aanpak="Fotosynthese en celademhaling zijn elkaars omgekeerde. Zet grondstoffen, producten, "
                    "plaats en energie telkens naast elkaar.",
             waarom=[
                 "De twee zijn elkaars spiegelbeeld. Leer ze dus nooit apart, altijd als paar.",
                 None,
                 "Een dierlijke cel heeft geen chloroplasten en doet enkel celademhaling. Daarom moet een "
                 "dier eten.",
                 "Netto is het sleutelwoord: de celademhaling stopt nooit, ook niet overdag. Alleen de "
                 "balans verschuift.",
             ]),
        dict(aanpak="Gisting is afbraak zonder zuurstofgas, en dus onvolledig. Een enzym versnelt zo'n "
                    "omzetting zonder zelf te verdwijnen.",
             waarom=[
                 None,
                 "Dat er nog energie in de ethanol zit, kan je proeven en zien: alcohol brandt. Daar zit de "
                 "rest van de energie.",
                 None,
                 "Dit is weer het sleutel-slotprincipe. Buiten het juiste gebied verandert de vorm van het "
                 "enzym, en dan past de sleutel niet meer.",
             ]),
        dict(aanpak="Zet een keten altijd met de pijlen in de richting van de stroom: van het gegeten "
                    "organisme naar wie het eet.",
             waarom=[
                 None,
                 "De richting van de pijl is het halve antwoord. Hij volgt de stof en de energie, niet de "
                 "blik van het roofdier.",
                 None,
             ]),
        dict(aanpak="Onthoud de vuistregel van een tiende per stap. Daarmee kan je elke vraag over een "
                    "piramide beantwoorden.",
             waarom=[
                 None,
                 "Werk in stappen van een tiende en schrijf elke stap op. Zo zie je hoe snel het getal "
                 "kleiner wordt.",
                 "Dit is hetzelfde tiende, drie vragen lang. Eén vuistregel draagt de hele reeks.",
                 "Daarom gaat deze vraag over meer dan biologie: de energiepiramide verklaart waarom "
                 "plantaardig eten minder land vraagt.",
                 None,
                 "Zonder reducenten blijven de mineralen opgesloten in dood materiaal. Zonlicht alleen "
                 "volstaat niet, want de kringloop is dan onderbroken.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-kringlopen-voedselrelaties-en-de-mens-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Zoek bij elk voorbeeld de stof die rondgaat. Water, koolstof en stikstof hebben een "
                    "gasvorm, fosfor niet.",
             waarom=[
                 "Die wortelknolletjes zijn het kenmerk van de stikstofkringloop: bacteriën maken "
                 "stikstofgas bruikbaar voor planten.",
                 "Dat fosfor geen gasvorm heeft, is net waarom die kringloop zo traag is: hij loopt enkel "
                 "via gesteente, bodem en water.",
             ]),
        dict(aanpak="Vraag je bij elke bewering af of de stof rondgaat en hoe snel. Materie keert terug, "
                    "energie niet.",
             waarom=[
                 "De atomen in je lichaam zaten ooit in een plant, een dier of in de lucht. Dat is wat een "
                 "kringloop betekent.",
                 None,
                 "Stikstofgas is heel stabiel. Planten hebben bacteriën nodig die het eerst omzetten; "
                 "daarom bestaat die hele kringloop.",
                 "De fosforkringloop is juist de traagste, want hij loopt langs gesteente. Daarom is fosfaat "
                 "een eindige grondstof.",
                 None,
             ]),
        dict(aanpak="Beschrijf elk gevolg als een ketting van stappen. De punten zitten in de verbanden, "
                    "niet in het eindpunt.",
             waarom=[
                 "Het punt is het tempo: wat in miljoenen jaren vastgelegd werd, komt er in enkele eeuwen "
                 "weer uit. De kringloop zelf is niet nieuw.",
                 "Zet de vier stappen echt op een rij: algen, licht weg, planten dood, zuurstof op. Het "
                 "zuurstoftekort is het einde van de ketting, niet het begin.",
                 None, None,
             ]),
        dict(aanpak="Deze begrippen beschrijven een populatie en haar plaats. Leer ze aan een voorbeeld, "
                    "niet aan de definitie alleen.",
             waarom=[
                 "Een niche is meer dan een plaats: het is alles wat een soort nodig heeft en doet. Daarom "
                 "kunnen twee soorten dezelfde plek delen met een andere niche.",
                 "Een indicatorsoort zoals een korstmos of een steenvlieg vertelt je iets over de lucht of "
                 "het water zonder dat je meet.",
                 "Vergeet de migratie niet. Veel antwoorden noemen enkel geboorte en sterfte, en dat is "
                 "onvolledig.",
                 "Dit heet het competitieuitsluitingsprincipe. Het verklaart waarom soorten in de natuur "
                 "altijd ergens van elkaar verschillen.",
             ]),
        dict(aanpak="Successie gaat altijd dezelfde kant op, van kaal naar bos. Beheer betekent dat je dat "
                    "proces met opzet tegenhoudt.",
             waarom=[
                 "Elke fase maakt de volgende mogelijk: pioniers vormen humus, en daarop kunnen grassen en "
                 "later struiken groeien.",
                 "Natuurbeheer is dus niet de natuur haar gang laten gaan. Een heide is een landschap dat "
                 "onderhoud vraagt.",
                 "Noem beide voordelen: water vasthouden én leefruimte. Een beek rechttrekken deed precies "
                 "het omgekeerde van allebei.",
             ]),
        dict(aanpak="De voetafdruk gaat over land, water en energie samen. Wat hoger in de voedselketen "
                    "zit, kost meer.",
             waarom=[
                 None,
                 "Dit is dezelfde energiepiramide als in het vorige hoofdstuk. Eén begrip verklaart hier "
                 "een keuze in de supermarkt.",
                 "Het punt is dat soorten niet altijd kúnnen meeverhuizen. Een bergtop of een versnipperd "
                 "landschap heeft geen uitweg.",
                 "Volg de ketting door: minder bestuiving, minder zaad, minder planten. Daarna volgen ook "
                 "de dieren die van die planten leven.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-levensreddend-handelen-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De orde ligt vast: veiligheid, bewustzijn, ademhaling, hulp bellen. Die vier stappen "
                    "zijn zelf de leerstof.",
             waarom=[
                 "Veiligheid komt eerst, altijd. Een tweede slachtoffer helpt niemand vooruit.",
                 None,
                 "Zeg vooral waar je bent, en blijf aan de lijn. De centralist kan je door de rest leiden "
                 "zolang je niet ophangt.",
             ]),
        dict(aanpak="Twee vragen beslissen alles: reageert hij, en ademt hij normaal. Daaruit volgt wat je "
                    "doet.",
             waarom=[
                 "Let op het verschil tussen de eerste twee: dezelfde bewusteloosheid, een andere "
                 "handeling. De ademhaling beslist.",
                 "Zolang iemand krachtig hoest, laat je hem hoesten. Dat werkt beter dan wat jij kan doen.",
             ]),
        dict(aanpak="De cijfers van een reanimatie leer je uit het hoofd: dertig op twee, honderd tot "
                    "honderdtwintig per minuut, ongeveer vijf centimeter diep.",
             waarom=[
                 None,
                 "Elke onderbreking laat de bloeddruk wegvallen. Daarom massage je door tot de hulpdiensten "
                 "of de AED je laten stoppen.",
                 "Met de luidspreker aan verlies je geen tijd. Dat is het antwoord dat deze vraag zoekt.",
                 "Stoppen mag enkel als de ademhaling weer normaal is. Je blijft wel kijken, want het kan "
                 "opnieuw misgaan.",
             ]),
        dict(aanpak="Een AED beslist zelf of een schok nodig is. Jij volgt enkel de gesproken aanwijzingen.",
             waarom=[
                 "Het toestel analyseert eerst het hartritme. Je kan er dus geen schok mee geven aan iemand "
                 "die er geen nodig heeft.",
                 "Daarom hangen ze in winkelcentra en sportzalen. Wachten op iemand met een opleiding kost "
                 "net de minuten die tellen.",
                 "Vergeet de laatste niet: niemand raakt het slachtoffer aan tijdens de schok. Dat is de "
                 "enige veiligheidsregel bij een AED.",
             ]),
        dict(aanpak="Zeg bij elke situatie niet alleen wat je niet doet, maar ook waarom niet. Daar zitten "
                    "de punten.",
             waarom=[
                 "Vet houdt de warmte vast en maakt de wonde moeilijker te beoordelen. Lauw stromend water "
                 "doet het omgekeerde.",
                 None,
                 "Drinken geven lijkt vriendelijk en is net gevaarlijk: verslikken, en een lege maag is "
                 "nodig voor een eventuele operatie.",
                 "Iets tussen de tanden steken breekt tanden en is gevaarlijk. Je beschermt enkel het hoofd "
                 "en wacht de aanval af.",
             ]),
        dict(aanpak="Deze laatste reeks legt de woorden vast. Weten waarom iets zo heet, helpt je de "
                    "handeling onthouden.",
             waarom=[
                 "Extern betekent van buitenaf, defibrilleren betekent het chaotische ritme stilleggen zodat "
                 "het hart opnieuw kan beginnen.",
                 None,
                 "Water spoelt zonder het weefsel te beschadigen. Alcohol doodt wel kiemen maar ook de "
                 "cellen die de wonde moeten helen.",
                 "Hersencellen verdragen maar enkele minuten zonder bloed. Daarom beslist de omstaander en "
                 "niet de ziekenwagen over de afloop.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-wetenschappelijk-onderzoek-en-stem-biologie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Twee variabelen uit elkaar houden: de onafhankelijke stel je zelf in, de afhankelijke "
                    "meet je. Al de rest houd je constant.",
             waarom=[
                 "De controlegroep is de maatstaf: zonder die groep weet je niet wat er zonder behandeling "
                 "gebeurd zou zijn.",
                 "Een storende variabele is een tweede factor die mee veranderde. Die opsporen is de kern "
                 "van de volgende reeks.",
             ]),
        dict(aanpak="Zoek bij elke opzet welke regel geschonden wordt: te weinig herhaling, twee factoren "
                    "tegelijk, of geen controlegroep.",
             waarom=[
                 "Twee plantjes is geen proef maar een vergelijking van twee individuen. Herhaling is wat "
                 "toeval uitsluit.",
                 "Noem de storende variabele bij naam: de temperatuur. Zonder dat woord toon je niet dat je "
                 "ziet wát er misgaat.",
                 None,
                 "Gegevens aanpassen is geen slordigheid maar bedrog. De meting beslist, niet de "
                 "verwachting.",
                 "Een weerlegde hypothese is een geldig resultaat: je weet nu iets wat je ervoor niet wist.",
             ]),
        dict(aanpak="Een opzet uitschrijven doe je in vaste onderdelen: vraag, hypothese, de twee "
                    "variabelen, en wat constant blijft. Sla er geen over.",
             waarom=[
                 "De hypothese krijgt een waarom erbij, hier de stikstofbindende bacteriën. Een verwachting "
                 "zonder reden is geen hypothese.",
             ]),
        dict(aanpak="De totale vergroting is het oculair maal het objectief. Begin altijd bij het zwakste "
                    "objectief.",
             waarom=[
                 None,
                 "Hoe sterker je vergroot, hoe kleiner het beeldveld. Daarom zoek je eerst bij een zwakke "
                 "vergroting en ga je dan pas sterker.",
                 "Een luchtbel wordt vaak voor een cel aangezien. De scherpe donkere rand verraadt haar.",
                 "Een virus is te klein voor een lichtmicroscoop; daarvoor heb je een elektronenmicroscoop "
                 "nodig. Dat is ook waarom virussen zo laat ontdekt zijn.",
             ]),
        dict(aanpak="De laboregels hebben één doel: niemand komt in aanraking met iets wat hij niet kan "
                    "overzien.",
             waarom=[
                 None, None,
                 "Een onbekende stof ruik je niet. Je gebruikt het etiket, en bij twijfel vraag je het.",
                 "Onderzoekend leren betekent met een plan werken, niet lukraak mengen. Dat laatste is "
                 "gevaarlijk en levert ook niets op.",
             ]),
        dict(aanpak="Een grafiek of tabel moet op zichzelf leesbaar zijn: grootheid, eenheid en schaal bij "
                    "elke as.",
             waarom=[
                 "Losse categorieën krijgen staven met ruimte ertussen; een vloeiend verband krijgt een "
                 "lijn. De soort gegevens beslist, niet de smaak.",
                 "Onthoud dat de onafhankelijke variabele horizontaal staat. Dat is in elke grafiek zo.",
                 "Een getal zonder eenheid betekent niets. Eén keer bovenaan de kolom volstaat.",
                 "De laatste vraag, wie het betaalde, wordt het vaakst vergeten. Een belang bij de uitkomst "
                 "kleurt een onderzoek.",
             ]),
        dict(aanpak="STEM is een manier van werken: meten, ontwerpen, uitvoeren, opnieuw meten. Die kring "
                    "is zelf het antwoord op bijna elke vraag.",
             waarom=[
                 None,
                 "Zonder beginmeting kan je achteraf niets besluiten. Daarom begint een STEM-opdracht altijd "
                 "met meten en niet met bouwen.",
             ]),
    ],
)
