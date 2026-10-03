# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij natuurwetenschappen 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere reeksen om te benoemen, andere gevallen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een stap
uitleggen, een rekening uitschrijven). Wie hier iets bijschrijft, legt het
eerst naast `../../boost-doorstroom/natuurwetenschappen.json`, naast de
leerbundel van hetzelfde thema en naast de vakfiche zelf.

Die vakfiche is de uitgebreide (2DOG), voor moderne talen en Latijn. Wat enkel
daar in staat en niet in de basisfiche, draagt in de leerbundel een kader. In
een oefenbundel kan dat niet, dus staat het hier telkens in een eigen reeks met
"uitgebreid" in de kop.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom". Het voorvoegsel is nodig omdat leerbundels en
oefenbundels in dezelfde bronmap gerenderd worden en anders dezelfde
bestandsnaam zouden krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Natuurwetenschappen"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

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
OEFENBUNDELS["oefenbundel-water-en-homeostase-bij-planten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Water en homeostase bij planten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk deel van de plant doet dit?",
             opdracht="Schrijf bij elke taak de naam van het deel.",
             oefeningen=[
                 ("rij", [("neemt water en mineralen op", "de wortel"),
                          ("vangt het licht op", "het blad"),
                          ("draagt het blad en vervoert", "de stengel")], "Welk deel?", WW),
                 ("rij", [("laat waterdamp naar buiten", "het huidmondje"),
                          ("belet dat het blad uitdroogt", "de cuticula"),
                          ("vervoert water naar boven", "de vaatbundels")], "Welk deel?", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De huidmondjes zitten vooral aan de onderkant van een blad.", True),
                 ("waar", "Een plant neemt water op langs haar bladeren en geeft het af langs haar "
                          "wortels.", False),
                 ("waar", "Bij droogte sluit een plant haar huidmondjes, ook al kan ze dan minder "
                          "fotosynthese doen.", True),
                 ("waar", "Transpiratie kost de plant energie, net als een pomp.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Een plant die je niet water geeft, hangt na een dag slap. Leg uit wat er "
                          "in de cellen gebeurd is.",
                  "De cellen verliezen water, de druk binnen de cel valt weg en ze worden slap. Die "
                  "druk hield de stengel en de bladeren recht, dus hangt de plant.", 4),
                 ("open", "Waarom gaat het water in een plant van beneden naar boven en niet "
                          "omgekeerd?",
                  "Boven verdampt er water uit de bladeren. Daardoor ontstaat er zuigkracht, en omdat "
                  "watermoleculen aan elkaar hangen, wordt de hele draad water mee naar boven "
                  "getrokken.", 4),
                 ("open", "Een kamerplant staat in een warme, droge kamer met veel wind van een "
                          "ventilator. Waarom verdampt er dan meer water?",
                  "Warmte, droge lucht en wind voeren de waterdamp sneller weg bij het blad. Het "
                  "verschil met de lucht in het blad blijft daardoor groot en de verdamping gaat "
                  "sneller.", 4),
             ]),
        dict(kop="De omgevingsfactoren",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Factor", "Wat ze met de verdamping doet"],
                  [["veel wind", None], ["hoge luchtvochtigheid", None], ["weinig licht", None]],
                  "Veel wind voert de damp weg en doet de verdamping stijgen. Hoge luchtvochtigheid "
                  "doet ze dalen, want de lucht zit al vol damp. Bij weinig licht staan de "
                  "huidmondjes verder dicht en daalt ze ook.", WL),
             ]),
        dict(kop="Prikkel en reactie bij een plant",
             opdracht="Schrijf het juiste woord of kies.",
             oefeningen=[
                 ("rij", [("de stengel groeit naar het licht", "fototropie"),
                          ("de wortel groeit naar beneden", "geotropie")], "Welke tropie?", WW),
                 ("kies", "Wat is het verschil tussen een tropie en een nastie?",
                  ["een tropie is sneller", "bij een tropie hangt de richting van de prikkel af",
                   "een nastie komt alleen bij wortels voor", "een nastie is aangeleerd"], 1),
                 ("kort", "Hoe noem je het transport van de suikers die in het blad gemaakt zijn?",
                  "het transport van assimilaten", WL),
             ]),
        dict(kop="Uitgebreid: transport van water en assimilaten",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("vervoert water omhoog", "xyleem of houtvaten"),
                          ("vervoert suikers in twee richtingen", "floëem of zeefvaten")],
                  "Welk vat?", WL),
                 ("open", "Waarom kan het transport van assimilaten in twee richtingen gaan en dat "
                          "van water niet?",
                  "Water volgt de verdamping en gaat dus altijd naar boven. Suikers gaan van waar ze "
                  "gemaakt worden naar waar ze gebruikt of opgeslagen worden, en dat kan hoger of "
                  "lager in de plant liggen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-prikkel-tot-reactie-en-het-oog-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Van prikkel tot reactie, en het oog",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De weg van prikkel tot reactie",
             opdracht="Nummer de vier stappen in de juiste orde, van 1 tot 4.",
             oefeningen=[
                 ("rij", [("de effector reageert", "4"), ("de receptor vangt de prikkel op", "1"),
                          ("het zenuwstelsel verwerkt de impuls", "3"),
                          ("de impuls gaat naar het centrum", "2")], "Nummer van 1 tot 4", "60px"),
                 ("kort", "Hoe noem je het orgaan dat de prikkel opvangt?", "de receptor of het zintuig", WL),
                 ("kort", "Hoe noem je het orgaan dat de reactie uitvoert?", "de effector", WW),
             ]),
        dict(kop="Welk zintuig, welke prikkel?",
             opdracht="Schrijf het zintuig erbij.",
             oefeningen=[
                 ("rij", [("licht", "het oog"), ("geluid", "het oor"),
                          ("een geur in de lucht", "de neus")], "Welk zintuig?", WW),
                 ("rij", [("een stof in het eten", "de tong"), ("warmte op je arm", "de huid"),
                          ("de stand van je hoofd", "het evenwichtsorgaan")], "Welk zintuig?", WW),
             ]),
        dict(kop="De delen van het oog",
             opdracht="Schrijf bij elke taak het deel van het oog.",
             oefeningen=[
                 ("rij", [("laat het licht binnen", "de pupil"),
                          ("regelt hoe groot de pupil is", "de iris"),
                          ("buigt het licht en kan boller worden", "de lens")], "Welk deel?", WW),
                 ("rij", [("vangt het licht op met zijn cellen", "het netvlies"),
                          ("brengt de impuls naar de hersenen", "de oogzenuw"),
                          ("is de doorzichtige voorkant", "het hoornvlies")], "Welk deel?", WW),
                 ("tabel", ["Cel in het netvlies", "Waarvoor ze dient"],
                  [["de staafjes", None], ["de kegeltjes", None]],
                  "De staafjes zien in weinig licht, maar geen kleur. De kegeltjes zien kleur, maar "
                  "hebben veel licht nodig.", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het beeld op het netvlies staat omgekeerd.", True),
                 ("waar", "In fel licht wordt de pupil groter.", False),
                 ("waar", "Om dichtbij te kijken wordt de lens boller.", True),
                 ("waar", "De blinde vlek is de plek waar je het scherpst ziet.", False),
             ]),
        dict(kop="Uitleggen en toepassen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Je komt uit een felle zon een donkere kamer binnen en ziet eerst bijna "
                          "niets. Leg uit waarom het daarna beter gaat.",
                  "In de zon stond de pupil klein en werkten vooral de kegeltjes. In het donker wordt "
                  "de pupil groter en nemen de staafjes over; die hebben even tijd nodig om gevoelig "
                  "te worden.", 4),
                 ("open", "Iemand ziet dichtbij scherp maar in de verte wazig. Welke lens heeft die "
                          "persoon nodig, en waarom?",
                  "Een holle of negatieve lens. Het oog buigt het licht te sterk, zodat het beeld voor "
                  "het netvlies valt; een holle lens spreidt het licht eerst, zodat het weer net op "
                  "het netvlies samenkomt.", 4),
                 ("open", "Waarom is de pupilreflex nuttig?",
                  "Hij regelt hoeveel licht er binnenvalt. Zo zie je in het donker nog iets en "
                  "beschermt het oog zich tegen te fel licht.", 3),
             ]),
        dict(kop="Rekenen met een lens",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Een lens heeft een brandpuntsafstand van 0,5 meter. Hoe groot is haar "
                          "sterkte in dioptrie?", "2 dioptrie", W),
                 ("kort", "Een brilglas heeft een sterkte van min 4 dioptrie. Hoe groot is de "
                          "brandpuntsafstand?", "min 0,25 meter", W),
                 ("open", "Leg uit wat het minteken bij een sterkte van min 4 dioptrie betekent.",
                  "Het gaat om een holle of negatieve lens. Die spreidt het licht in plaats van het "
                  "samen te brengen, en wordt gebruikt bij iemand die in de verte wazig ziet.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-zenuwstelsel-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het zenuwstelsel",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Centraal of perifeer?",
             opdracht="Schrijf centraal of perifeer.",
             oefeningen=[
                 ("rij", [("de hersenen", "centraal"), ("het ruggenmerg", "centraal"),
                          ("de hersenzenuwen", "perifeer")], None, W),
                 ("rij", [("de ruggenmergzenuwen", "perifeer"), ("de grensstrengen", "perifeer")],
                  None, W),
             ]),
        dict(kop="De delen van een neuron",
             opdracht="Schrijf bij elke taak het deel van het neuron.",
             oefeningen=[
                 ("rij", [("vangt de signalen op", "de dendrieten"),
                          ("geeft het signaal door", "het axon"),
                          ("bevat de celkern", "het cellichaam")], "Welk deel?", WW),
                 ("rij", [("isoleert het axon", "de myelineschede"),
                          ("is de onderbreking in die schede", "de knoop van Ranvier"),
                          ("geeft de neurotransmitter af", "het eindknopje")], "Welk deel?", WL),
                 ("kort", "Welke cellen maken de myelineschede buiten het centrale zenuwstelsel?",
                  "de cellen van Schwann", WL),
             ]),
        dict(kop="Welk soort neuron?",
             opdracht="Schrijf sensorisch, motorisch of schakelneuron.",
             oefeningen=[
                 ("rij", [("van een zintuig naar het centrum", "sensorisch"),
                          ("van het centrum naar een spier", "motorisch")], None, WW),
                 ("rij", [("verbindt de twee in het ruggenmerg", "schakelneuron"),
                          ("komt uit op een klier", "motorisch")], None, WW),
                 ("kort", "Noem de drie soorten effector waar een motorisch neuron op uitkomt.",
                  "een spier, een klier en het hartspierweefsel", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een gemengde zenuw bevat alleen motorische vezels.", False),
                 ("waar", "Het signaal gaat in een synaps maar in één richting over.", True),
                 ("waar", "Een gemyeliniseerde vezel geleidt sneller dan een vezel zonder schede.",
                  True),
                 ("waar", "Het ruggenmerg kan een reflex niet afhandelen zonder de hersenen.", False),
             ]),
        dict(kop="De synaps",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("kort", "Hoe heet de smalle ruimte tussen twee neuronen?", "de synaptische spleet",
                  WL),
                 ("kort", "Hoe heet de stof die daar vrijkomt?", "de neurotransmitter", WW),
                 ("open", "Waarom gaat het signaal in een synaps maar in één richting over?",
                  "Alleen het eindknopje heeft blaasjes met neurotransmitter, en alleen de overkant "
                  "heeft de receptoren die erop passen. Omgekeerd kan het dus niet.", 4),
                 ("open", "Leg uit wat het sleutel-slotprincipe bij een neurotransmitter betekent.",
                  "Een neurotransmitter past maar op bepaalde receptoren, zoals een sleutel in één "
                  "slot. Daarom werkt hij alleen op de neuronen die dat slot hebben.", 3),
             ]),
        dict(kop="Reflexen",
             opdracht="Vul aan, kies of leg uit.",
             oefeningen=[
                 ("rij", [("je pupil wordt kleiner bij fel licht", "de pupilreflex"),
                          ("een tik onder de knieschijf", "de kniepeesreflex")], "Welke reflex?", WL),
                 ("kies", "Wat is de juiste weg van een terugtrekreflex?",
                  ["receptor, hersenen, spier",
                   "receptor, sensorisch neuron, schakelneuron, motorisch neuron, spier",
                   "spier, motorisch neuron, receptor", "receptor, klier, spier"], 1),
                 ("open", "Je raakt een hete pan aan en trekt je hand weg voor je de pijn voelt. Leg "
                          "uit hoe dat kan.",
                  "De reflex loopt via het ruggenmerg en dat is een korte weg. Het pijnsignaal moet "
                  "nog verder naar de hersenen, en daarom voel je de pijn pas nadat je hand al weg "
                  "is.", 4),
             ]),
        dict(kop="Uitgebreid: rustpotentiaal en actiepotentiaal",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("het membraan in rust", "de rustpotentiaal"),
                          ("het spanningsverschil slaat om", "de depolarisatie"),
                          ("het keert terug naar de rust", "de repolarisatie")], "Welke stap?", WL),
                 ("waar", "Een sterkere prikkel geeft een grotere amplitude van de actiepotentiaal.",
                  False),
                 ("open", "Wat gebeurt er met de impulsen in één zenuwvezel als de prikkel twee keer "
                          "zo sterk wordt?",
                  "Er volgen meer impulsen per seconde, maar elke impuls blijft even groot. De "
                  "sterkte zit dus in het aantal en niet in de hoogte.", 3),
                 ("open", "Waarom kan een neuron niet onbeperkt snel achter elkaar vuren?",
                  "Na een impuls volgt de herstelfase. Zolang die duurt, is het neuron even niet in "
                  "staat om opnieuw te vuren.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-spieren-klieren-en-hormonen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Spieren, klieren en hormonen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk spierweefsel?",
             opdracht="Schrijf dwarsgestreept, glad of hartspierweefsel.",
             oefeningen=[
                 ("rij", [("de spier die je arm buigt", "dwarsgestreept"),
                          ("de wand van een bloedvat", "glad")], None, WW),
                 ("rij", [("de wand van het hart", "hartspierweefsel"),
                          ("de kauwspier in je kaak", "dwarsgestreept")], None, WW),
                 ("waar", "Het hartspierweefsel werkt onwillekeurig, ook al is het dwarsgestreept.",
                  True),
             ]),
        dict(kop="De bouw van een spier",
             opdracht="Zet de delen van groot naar klein en vul aan.",
             oefeningen=[
                 ("rij", [("spierfibril", "4"), ("spierbuik", "1"), ("spiervezel", "3"),
                          ("spierbundel", "2")], "Nummer van 1 (grootst) tot 4", "60px"),
                 ("kort", "Hoe heet het celmembraan van een spiervezel?", "het sarcolemma", WW),
                 ("kort", "Hoe heet het stukje spierfibril tussen twee Z-platen?", "het sarcomeer",
                  WW),
                 ("waar", "Een spiervezel heeft maar één celkern.", False),
             ]),
        dict(kop="Samentrekken",
             opdracht="Kies of leg uit.",
             oefeningen=[
                 ("kies", "Wat gebeurt er in een sarcomeer als de spier samentrekt?",
                  ["de Z-platen komen dichter bij elkaar", "de Z-platen gaan verder van elkaar",
                   "de myosinefilamenten worden korter", "er komen filamenten bij"], 0),
                 ("kort", "Hoe heet de plek waar een motorisch neuron op een spiervezel aankomt?",
                  "de motorische eindplaat", WL),
                 ("kort", "Hoe heet één motorisch neuron met alle vezels die het aanstuurt?",
                  "een motorische eenheid", WL),
                 ("open", "Waarom werken spieren altijd in paren?",
                  "Een spier kan alleen trekken en niet duwen. Om een gewricht in twee richtingen te "
                  "bewegen, heb je dus twee spieren nodig die elkaars antagonist zijn.", 4),
             ]),
        dict(kop="Endocrien of exocrien?",
             opdracht="Schrijf endocrien, exocrien of gemengd.",
             oefeningen=[
                 ("rij", [("de traanklier", "exocrien"), ("de schildklier", "endocrien"),
                          ("de alvleesklier", "gemengd")], None, WW),
                 ("rij", [("de zweetklier", "exocrien"), ("de bijnier", "endocrien"),
                          ("de talgklier", "exocrien")], None, WW),
                 ("open", "Leg het verschil tussen een endocriene en een exocriene klier uit.",
                  "Een endocriene klier geeft haar stof rechtstreeks aan het bloed af. Een exocriene "
                  "klier doet dat via een afvoerbuis, naar een holte of naar buiten.", 3),
             ]),
        dict(kop="Welke klier maakt welk hormoon?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Klier", "Hormoon"],
                  [["de schildklier", None], ["de bijnier", None], ["de alvleesklier", None]],
                  "De schildklier maakt thyroxine. De bijnier maakt adrenaline en cortisol. De "
                  "alvleesklier maakt insuline en glucagon.", WL),
                 ("kort", "Welke klier onderaan de hersenen stuurt veel andere klieren aan?",
                  "de hypofyse", WW),
                 ("kort", "Wat is het doelorgaan van het schildklierstimulerend hormoon?",
                  "de schildklier", WW),
             ]),
        dict(kop="De bloedsuiker",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("laat de lever glucose opslaan", "insuline"),
                          ("laat de lever glycogeen afbreken", "glucagon")], "Welk hormoon?", WW),
                 ("open", "Beschrijf wat er na een maaltijd met je bloedsuiker en met insuline "
                          "gebeurt.",
                  "Het glucosegehalte stijgt. De bètacellen in de eilandjes van Langerhans geven "
                  "insuline af, de lever slaat glucose op als glycogeen en de lichaamscellen nemen "
                  "meer glucose op. Zo daalt het gehalte weer.", 5),
                 ("open", "Waarom heeft iemand met onbehandelde diabetes vaak dorst en plast die veel?",
                  "Er blijft te veel glucose in het bloed. De nieren voeren die overtollige glucose "
                  "af en nemen daarbij veel water mee, en daardoor krijgt de persoon dorst.", 4),
                 ("waar", "Bij diabetes type 1 maakt het lichaam zelf te weinig of geen insuline meer "
                          "aan.", True),
             ]),
        dict(kop="Hormonen tegenover zenuwen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Een hormoon komt met het bloed overal in het lichaam, en toch werkt het "
                          "maar op bepaalde cellen. Leg uit hoe dat kan.",
                  "Alleen de doelwitcellen hebben de receptor waarop dat hormoon past, volgens het "
                  "sleutel-slotprincipe. De andere cellen merken er niets van.", 4),
                 ("open", "Noem twee verschillen tussen de werking van zenuwen en die van hormonen.",
                  "Zenuwen werken snel en heel gericht, op één effector. Hormonen werken trager, maar "
                  "hun effect houdt langer aan en bereikt veel cellen tegelijk.", 4),
                 ("kort", "Welk hormoon zet je lichaam bij stress klaar voor inspanning?",
                  "adrenaline", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-voortplanting-en-de-hormonale-regeling-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Voortplanting en de hormonale regeling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk orgaan doet dit?",
             opdracht="Schrijf bij elke taak het orgaan.",
             oefeningen=[
                 ("rij", [("hierin rijpt de eicel", "de eierstok"),
                          ("hier vindt de bevruchting plaats", "de eileider"),
                          ("hierin groeit het embryo", "de baarmoeder")], "Welk orgaan?", WW),
                 ("rij", [("hier worden zaadcellen gevormd", "de teelbal"),
                          ("hier rijpen ze en worden ze bewaard", "de bijbal"),
                          ("hierdoor worden ze afgevoerd", "de zaadleider")], "Welk orgaan?", WW),
             ]),
        dict(kop="De cyclus op een rij",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Op welke dag van de cyclus begint de menstruatie?", "op dag 1", W),
                 ("kort", "Hoe lang duurt een gemiddelde cyclus?", "ongeveer 28 dagen", W),
                 ("kort", "Hoe heet het vrijkomen van de eicel?", "de eisprong", WW),
                 ("kort", "Hoe heet het lichaam dat na de eisprong uit de follikel ontstaat?",
                  "het geel lichaam", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Oestrogeen wordt gemaakt door de eierstok.", True),
                 ("waar", "De eicel wordt na de eisprong opgevangen door de baarmoeder.", False),
                 ("waar", "De lichaamstemperatuur ligt na de eisprong gemiddeld iets hoger.", True),
                 ("waar", "Bij de man verloopt de zaadcelvorming in cycli van achtentwintig dagen.",
                  False),
                 ("waar", "Inhibine remt de afgifte van FSH.", True),
             ]),
        dict(kop="Welk hormoon?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Waar het vandaan komt", "Hormoon", "Wat het doet"],
                  [["de hypothalamus", None, None], ["de hypofyse", None, None],
                   ["het geel lichaam", None, None]],
                  "De hypothalamus maakt GnRH, dat de hypofyse aanzet om FSH en LH te maken. De "
                  "hypofyse maakt FSH, dat de follikel laat rijpen, en LH, waarvan een piek de "
                  "eisprong op gang brengt. Het geel lichaam maakt progesteron, dat het "
                  "baarmoederslijmvlies in stand houdt.", "150px"),
                 ("kort", "Welk hormoon van de eierstok laat het slijmvlies in de eerste helft van de "
                          "cyclus aangroeien?", "oestrogeen", WW),
                 ("kort", "Welke drie hormonen spelen bij zowel man als vrouw een rol?",
                  "GnRH, FSH en LH", WW),
             ]),
        dict(kop="De cellen van de teelbal",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("maken testosteron", "de cellen van Leydig"),
                          ("voeden de rijpende zaadcellen", "de cellen van Sertoli")],
                  "Welke cellen?", WL),
                 ("open", "Waarom liggen de teelballen buiten de buikholte?",
                  "De zaadcelvorming verloopt beter bij een iets lagere temperatuur dan die van de "
                  "buikholte.", 3),
                 ("open", "Noem buiten de zaadcelvorming nog een taak van testosteron.",
                  "Het zorgt voor de ontwikkeling van de secundaire geslachtskenmerken.", 2),
             ]),
        dict(kop="Feedback",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom noemen we de regeling van de cyclus een feedbacksysteem?",
                  "De hormonen uit de eierstok sturen de hypothalamus en de hypofyse op hun beurt bij. "
                  "Het signaal gaat dus niet alleen heen, maar ook terug.", 4),
                 ("open", "Het testosterongehalte bij een man wordt te hoog. Beschrijf wat er daarna "
                          "gebeurt.",
                  "De hypothalamus geeft minder GnRH af, de hypofyse geeft minder LH af, en daardoor "
                  "maken de cellen van Leydig minder testosteron. Zo daalt het gehalte weer.", 5),
                 ("open", "In een schema staat een pijl met een minteken van de eierstok naar de "
                          "hypofyse. Wat betekent die pijl?",
                  "Het hormoon uit de eierstok remt de hypofyse af.", 2),
                 ("open", "Waarom begint de menstruatie net wanneer het progesterongehalte daalt?",
                  "Zonder progesteron kan het dikke baarmoederslijmvlies niet in stand blijven. Het "
                  "laat dan los, en dat is de menstruatie.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biodiversiteit-en-micro-organismen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Biodiversiteit en micro-organismen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Prokaryoot of eukaryoot?",
             opdracht="Schrijf prokaryoot of eukaryoot.",
             oefeningen=[
                 ("rij", [("een bacterie", "prokaryoot"), ("een gistcel", "eukaryoot"),
                          ("een schimmel", "eukaryoot")], None, WW),
                 ("rij", [("een plantencel", "eukaryoot"), ("een archaeon", "prokaryoot")], None, WW),
                 ("kort", "Wat heeft een prokaryote cel niet?", "een kernmembraan", WW),
             ]),
        dict(kop="Hoe vermeerderen ze zich?",
             opdracht="Schrijf celsplitsing, knopvorming of in een gastheercel.",
             oefeningen=[
                 ("rij", [("een bacterie", "celsplitsing"), ("een gistcel", "knopvorming"),
                          ("een virus", "in een gastheercel")], None, WL),
                 ("open", "Waarom staan virussen niet in de tree of life?",
                  "Ze hebben geen eigen stofwisseling en kunnen zich niet alleen vermeerderen. Ze "
                  "hebben altijd een gastheercel nodig.", 3),
                 ("kort", "Waaruit bestaat een virus in zijn eenvoudigste vorm?",
                  "genetisch materiaal met een eiwitmantel eromheen", WL),
             ]),
        dict(kop="Woorden die je moet kennen",
             opdracht="Vul het woord in.",
             oefeningen=[
                 ("rij", [("kan leven zonder zuurstofgas", "anaëroob"),
                          ("maakt zijn eigen energierijke stoffen", "autotroof"),
                          ("haalt ze uit andere organismen", "heterotroof")], "Welk woord?", WW),
                 ("kort", "Hoe noem je de vorm waarin een bacterie slechte omstandigheden overleeft?",
                  "een spore", W),
                 ("kort", "Welke drie groeivoorwaarden heeft een bacterie nodig?",
                  "voedsel, vocht en een geschikte temperatuur", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een antibioticum helpt tegen griep.", False),
                 ("waar", "Antibioticaresistentie ontstaat doordat de bacteriën die het middel "
                          "overleven zich verder vermenigvuldigen.", True),
                 ("waar", "Pasteuriseren maakt een product volledig steriel.", False),
                 ("waar", "Probiotica zijn levende micro-organismen die je inneemt.", True),
             ]),
        dict(kop="Micro-organismen aan het werk",
             opdracht="Schrijf welk micro-organisme of welk proces.",
             oefeningen=[
                 ("rij", [("laat brood rijzen", "bakkersgist"),
                          ("maakt melk zuur en dik", "melkzuurbacteriën")], "Wat of wie?", WL),
                 ("tabel", ["Bewaringstechniek", "Waarom er niets meer groeit"],
                  [["drogen", None], ["inmaken in zout", None], ["pasteuriseren", None]],
                  "Drogen haalt het water weg, en zonder water groeit er niets. Zout trekt water uit "
                  "de cellen, zodat de meeste micro-organismen niet kunnen groeien. Pasteuriseren "
                  "verhit kort, zodat de meeste micro-organismen sterven.", WL),
                 ("open", "Een gist wordt gebruikt om bier te brouwen. Welke eigenschap maakt haar "
                          "daarvoor geschikt?",
                  "Ze zet suikers zonder zuurstofgas om in alcohol en koolstofdioxide.", 3),
             ]),
        dict(kop="In de natuur en in ons lichaam",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Hoe noem je het geheel van micro-organismen in je darm?",
                  "het darmmicrobioom", WL),
                 ("open", "Leg uit wat er bij eutrofiëring in een vijver gebeurt.",
                  "Er komt te veel mest in het water. De algen bloeien sterk op, er dringt minder "
                  "licht door tot in de diepte, en wanneer de algen afsterven daalt het "
                  "zuurstofgehalte. Veel soorten verdwijnen daardoor.", 5),
                 ("open", "Waarom is handen wassen zo doeltreffend tegen infecties?",
                  "Het onderbreekt de weg waarlangs ziekteverwekkers zich verspreiden. Je doodt niet "
                  "alles, maar je zorgt dat het niet van de ene naar de andere gaat.", 4),
                 ("kort", "Welk middel gebruik je tegen een infectie door een schimmel?",
                  "een antimycoticum", WW),
             ]),
        dict(kop="Uitgebreid: het driedomeinensysteem",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("kort", "Noem de drie domeinen.", "archaea, bacteriën en eukaryoten", WL),
                 ("open", "Waarom is zo'n indeling nuttig?",
                  "Ze toont hoe soorten met elkaar verwant zijn, en niet wat de mens er nuttig aan "
                  "vindt.", 3),
                 ("open", "Je krijgt een organisme te zien dat eencellig is, geen kernmembraan heeft "
                          "en zich door celsplitsing vermeerdert. Waar hoort het thuis en waarom?",
                  "Bij de prokaryoten: geen kernmembraan is precies het kenmerk van een prokaryote "
                  "cel, en celsplitsing past daar ook bij.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-gedrag-interactie-en-ecosystemen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Gedrag, interactie en ecosystemen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Aangeboren of aangeleerd?",
             opdracht="Schrijf aangeboren of aangeleerd.",
             oefeningen=[
                 ("rij", [("een pasgeboren baby zoekt de borst", "aangeboren"),
                          ("een hond geeft een poot op commando", "aangeleerd"),
                          ("een spin weeft haar web", "aangeboren")], None, WW),
                 ("rij", [("een jonge meeuw kijkt haar moeder na", "aangeleerd"),
                          ("een kalf staat recht kort na de geboorte", "aangeboren")], None, WW),
             ]),
        dict(kop="Welke vorm van leren?",
             opdracht="Schrijf conditioneren, gewenning, inprenting, trial-and-error of imitatie.",
             oefeningen=[
                 ("rij", [("een hond kwijlt bij het geluid van de voerbak", "conditioneren"),
                          ("vogels schrikken niet meer van een vogelverschrikker", "gewenning")],
                  "Welke vorm?", WL),
                 ("rij", [("een gansje volgt wie het eerst bij hem was", "inprenting"),
                          ("een kraai probeert tot het dekseltje loskomt", "trial-and-error")],
                  "Welke vorm?", WL),
             ]),
        dict(kop="Welke interactie?",
             opdracht="Schrijf mutualisme, commensalisme, parasitisme, predatie, concurrentie of "
                      "antibiose.",
             oefeningen=[
                 ("rij", [("een lintworm in een darm", "parasitisme"),
                          ("een bij en een bloem", "mutualisme")], "Welke interactie?", WL),
                 ("rij", [("een vos die een haas eet", "predatie"),
                          ("twee soorten vogels op hetzelfde zaad", "concurrentie")],
                  "Welke interactie?", WL),
                 ("rij", [("een schimmel die bacteriën remt", "antibiose"),
                          ("een vogel die op de rug van een koe zit", "commensalisme")],
                  "Welke interactie?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij commensalisme hebben beide organismen even veel voordeel.", False),
                 ("waar", "Mutualisme is een vorm van symbiose.", True),
                 ("waar", "Betreding en begrazing zijn abiotische factoren.", False),
                 ("waar", "Reducenten maken de materiekringloop rond.", True),
                 ("waar", "Een consument van de eerste orde eet andere dieren.", False),
             ]),
        dict(kop="Rollen in een ecosysteem",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Rol", "Wat die groep doet", "Voorbeeld"],
                  [["producent", None, None], ["consument", None, None], ["reducent", None, None]],
                  "Een producent maakt met fotosynthese energierijke stoffen uit energiearme, "
                  "bijvoorbeeld een grasplant. Een consument eet andere organismen, bijvoorbeeld een "
                  "koe of een vos. Een reducent breekt dood materiaal af tot minerale stoffen, "
                  "bijvoorbeeld een bodembacterie of een schimmel.", "140px"),
                 ("kort", "Hoe noem je de niet-levende factoren van een ecosysteem?",
                  "de abiotische factoren", WL),
             ]),
        dict(kop="Energie en materie",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom zijn er in een ecosysteem veel meer planten dan toproofdieren?",
                  "Bij elke stap in de voedselketen gaat het grootste deel van de energie als warmte "
                  "verloren. Er blijft dus telkens veel minder over om de volgende schakel te voeden.",
                  4),
                 ("open", "Leg het verschil uit tussen de energiestroom en de materiekringloop.",
                  "De energie stroomt in één richting en gaat stap voor stap als warmte verloren. De "
                  "materie draait rond: de reducenten maken de kringloop rond, zodat planten de "
                  "stoffen weer kunnen opnemen.", 5),
                 ("open", "Waarom is een voedselweb een betere voorstelling dan één voedselketen?",
                  "De meeste soorten eten van meer dan één soort en worden door meer dan één soort "
                  "gegeten. Een web laat die kruisverbanden zien, een keten niet.", 4),
                 ("kort", "Welk proces zet energierijke stoffen weer om in energiearme en maakt "
                          "daarbij energie vrij?", "de celademhaling", WW),
             ]),
        dict(kop="Verstoring",
             opdracht="Leg uit of kies.",
             oefeningen=[
                 ("open", "Een bos verliest door ziekte bijna al zijn bomen. Wat betekent dat voor het "
                          "ecosysteem?",
                  "De voedselrelaties en de kringlopen raken verstoord. Soorten die van de bomen "
                  "leefden, verdwijnen mee, en de bodem en het licht veranderen ook.", 4),
                 ("kies", "Waarom vangt een ecosysteem met veel soorten een verstoring beter op?",
                  ["er is minder zonne-energie nodig", "de voedselketens worden korter",
                   "er zijn meer soorten die een weggevallen rol kunnen overnemen",
                   "de voedingsstoffen raken sneller op"], 2),
                 ("open", "Noem een gevolg van klimaatverandering voor een ecosysteem.",
                  "Soorten verschuiven naar koelere gebieden of hoger de berg op, of ze verdwijnen "
                  "omdat hun leefomstandigheden veranderen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-mengsels-en-zuivere-stoffen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Mengsels en zuivere stoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zuivere stof of mengsel?",
             opdracht="Schrijf zuivere stof of mengsel.",
             oefeningen=[
                 ("rij", [("gedestilleerd water", "zuivere stof"), ("lucht", "mengsel"),
                          ("keukenzout", "zuivere stof")], None, WW),
                 ("rij", [("water uit de kraan", "mengsel"), ("koper", "zuivere stof"),
                          ("brons", "mengsel")], None, WW),
             ]),
        dict(kop="Homogeen of heterogeen?",
             opdracht="Schrijf homogeen of heterogeen.",
             oefeningen=[
                 ("rij", [("zeewater", "homogeen"), ("slagroom", "heterogeen"),
                          ("messing", "homogeen")], None, WW),
                 ("rij", [("zand in water", "heterogeen"), ("rook", "heterogeen"),
                          ("suiker in water", "homogeen")], None, WW),
             ]),
        dict(kop="Welk soort mengsel?",
             opdracht="Schrijf oplossing, legering, suspensie, emulsie, aerosol of schuim.",
             oefeningen=[
                 ("rij", [("vinaigrette", "emulsie"), ("nevel", "aerosol"),
                          ("krijt in water", "suspensie")], "Welk soort?", WW),
                 ("rij", [("slagroom", "schuim"), ("brons", "legering"),
                          ("zout in water", "oplossing")], "Welk soort?", WW),
                 ("kort", "Uit welke twee metalen bestaat messing?", "koper en zink", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een mengsel smelt bij één vaste temperatuur.", False),
                 ("waar", "Een bestanddeel van een mengsel behoudt zijn eigen stofeigenschappen.",
                  True),
                 ("waar", "Een scheidingstechniek verandert de bestanddelen chemisch.", False),
                 ("waar", "Zeven en filtreren steunen allebei op een verschil in deeltjesgrootte.",
                  True),
             ]),
        dict(kop="Stofeigenschap of niet?",
             opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("het kookpunt", "ja"), ("de massa in de pot", "nee"),
                          ("de massadichtheid", "ja")], None, "70px"),
                 ("rij", [("de oplosbaarheid", "ja"), ("het volume van je staal", "nee"),
                          ("de geleidbaarheid", "ja")], None, "70px"),
                 ("open", "Je verwarmt een stof en de temperatuur blijft tijdens het koken stijgen. "
                          "Wat besluit je, en waarom?",
                  "Het is een mengsel. Een zuivere stof kookt bij één vaste temperatuur, een mengsel "
                  "over een kooktraject.", 4),
             ]),
        dict(kop="Welke techniek kies je?",
             opdracht="Schrijf de naam van de techniek.",
             oefeningen=[
                 ("rij", [("zand uit water halen", "filtreren"),
                          ("zuiver water uit zeewater", "destilleren")], "Welke techniek?", WL),
                 ("rij", [("het zout uit zout water terugwinnen", "indampen"),
                          ("ijzervijlsel uit zand halen", "een magneet")], "Welke techniek?", WL),
                 ("rij", [("de kleurstoffen van een stift scheiden", "chromatografie"),
                          ("zwevende deeltjes die niet bezinken", "centrifugeren of filtreren")],
                  "Welke techniek?", WL),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("kort", "Hoe heet wat er na het filtreren op de filter achterblijft?",
                  "het residu", W),
                 ("kort", "Hoe heet wat er door de filter loopt?", "het filtraat", W),
                 ("open", "Waarom kan je olie en water niet goed met filtreren scheiden?",
                  "De oliedruppeltjes zijn vloeibaar en gaan gewoon door de filter mee. Je gebruikt "
                  "beter een scheitrechter of je laat de lagen van elkaar scheiden en giet af.", 4),
                 ("open", "Waarom is het residu niet altijd afval?",
                  "Soms is juist het residu de stof die je nodig hebt, bijvoorbeeld als je het "
                  "neerslag wil houden en het water niet.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-enkelvoudige-en-samengestelde-stoffen-en-chemische-reacties-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Enkelvoudige en samengestelde stoffen, en chemische reacties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Enkelvoudig of samengesteld?",
             opdracht="Schrijf enkelvoudig of samengesteld.",
             oefeningen=[
                 ("rij", [("O2", "enkelvoudig"), ("CO2", "samengesteld"), ("O3", "enkelvoudig")],
                  None, WW),
                 ("rij", [("H2O", "samengesteld"), ("Fe", "enkelvoudig"),
                          ("NaCl", "samengesteld")], None, WW),
             ]),
        dict(kop="Symbool en element",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("natrium", "Na"), ("kalium", "K"), ("goud", "Au")], "Welk symbool?",
                  "70px"),
                 ("rij", [("koper", "Cu"), ("koolstof", "C"), ("magnesium", "Mg")],
                  "Welk symbool?", "70px"),
                 ("rij", [("Fe", "ijzer"), ("N", "stikstof"), ("Ca", "calcium")], "Welk element?",
                  WW),
             ]),
        dict(kop="Index, coëfficiënt en atomen tellen",
             opdracht="Reken en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Wat is de coëfficiënt in 4 CO2?", "4", "60px"),
                 ("kort", "Wat is de index bij de zuurstof in 4 CO2?", "2", "60px"),
                 ("kort", "Hoeveel atomen in totaal staan er in 3 H2O?", "9", "60px"),
                 ("kort", "Hoeveel atomen in totaal staan er in 2 Ca(OH)2?", "10", "60px"),
                 ("open", "Leg uit hoe je het aantal atomen in 2 H2SO4 berekent.",
                  "Per deeltje: 2 waterstof, 1 zwavel en 4 zuurstof, samen 7. Die 7 maal de "
                  "coëfficiënt 2 geeft 14 atomen.", 4),
             ]),
        dict(kop="Metaal of niet-metaal?",
             opdracht="Schrijf metaal of niet-metaal.",
             oefeningen=[
                 ("rij", [("koper", "metaal"), ("zwavel", "niet-metaal"), ("kwik", "metaal")],
                  None, WW),
                 ("rij", [("chloor", "niet-metaal"), ("zink", "metaal"),
                          ("stikstof", "niet-metaal")], None, WW),
                 ("waar", "Niet-metalen zijn allemaal glanzend en goed vervormbaar.", False),
             ]),
        dict(kop="Stoffen die je moet kennen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het enige vloeibare metaal", "kwik"),
                          ("een geelgroen gas", "chloorgas")], "Welke stof?", WW),
                 ("rij", [("gebruikt bij ademnood en om te lassen", "zuurstofgas"),
                          ("licht op in lichtreclame", "neon")], "Welke stof?", WW),
                 ("open", "Waarom gebruikt men helium in ballonnen en geen waterstofgas?",
                  "Helium is een edelgas en reageert zo goed als nergens mee. Waterstofgas is wel "
                  "lichter, maar het is brandbaar.", 4),
                 ("open", "Grafiet en diamant bestaan allebei uit koolstof. Waarom verschillen ze dan "
                          "zo sterk?",
                  "De koolstofatomen zitten in een andere structuur aan elkaar. Daardoor is diamant "
                  "hard en doorzichtig en grafiet zacht en geleidend.", 4),
             ]),
        dict(kop="Reactievergelijkingen kloppend maken",
             opdracht="Zet de coëfficiënten erbij. De indexen mag je niet veranderen.",
             oefeningen=[
                 ("kort", "___ H2 + ___ O2 geeft ___ H2O", "2, 1, 2", W),
                 ("kort", "___ Mg + ___ O2 geeft ___ MgO", "2, 1, 2", W),
                 ("kort", "___ CH4 + ___ O2 geeft ___ CO2 + ___ H2O", "1, 2, 1, 2", W),
                 ("open", "Waarom mag je de index in een formule niet aanpassen om een vergelijking "
                          "kloppend te maken?",
                  "De index hoort bij de stof zelf. Als je die verandert, heb je een andere stof. Je "
                  "mag alleen de coëfficiënt ervoor aanpassen, dus hoeveel deeltjes je neemt.", 4),
             ]),
        dict(kop="Behoud van massa",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Je verbrandt magnesium in een afgesloten vat en weegt opnieuw. Wat lees je "
                          "af, en waarom?",
                  "De totale massa is gelijk gebleven. Bij een reactie verdwijnen er geen atomen; het "
                  "zuurstofgas uit het vat zit nu in het magnesiumoxide.", 4),
                 ("open", "Waarom lijkt de massa bij een verbranding in een open schaal soms te dalen?",
                  "Er ontsnappen gassen uit de schaal. Je weegt enkel het vaste overblijfsel, en dus "
                  "mis je een deel van de massa.", 4),
             ]),
        dict(kop="Energie bij een reactie",
             opdracht="Vul aan, kies of leg uit.",
             oefeningen=[
                 ("rij", [("staat energie af aan de omgeving", "exo-energetisch"),
                          ("neemt energie op uit de omgeving", "endo-energetisch")], "Welk soort?",
                  WL),
                 ("open", "Je mengt twee stoffen en de beker voelt duidelijk kouder aan. Wat besluit "
                          "je?",
                  "De reactie is endo-energetisch: ze neemt warmte op uit haar omgeving, en daardoor "
                  "koelt de beker af.", 3),
                 ("kies", "Hoe liggen de reactieproducten in een energiediagram van een "
                          "exo-energetische reactie?",
                  ["hoger dan de reagentia", "lager dan de reagentia", "op dezelfde hoogte",
                   "dat hangt van de temperatuur af"], 1),
                 ("kort", "Hoe noem je de hoeveelheid energie die bij een reactie opgenomen of "
                          "afgestaan wordt?", "de reactie-energie", WL),
                 ("kort", "Hoe heten de stoffen links van de pijl?", "de reagentia", WW),
                 ("kort", "Hoe heten de stoffen rechts van de pijl?", "de reactieproducten", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-bouw-van-het-atoom-en-het-periodiek-systeem-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De bouw van het atoom en het periodiek systeem",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De deeltjes in een atoom",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Deeltje", "Lading", "Waar het zit"],
                  [["proton", None, None], ["neutron", None, None], ["elektron", None, None]],
                  "Een proton is positief en zit in de kern. Een neutron is neutraal en zit ook in de "
                  "kern. Een elektron is negatief en beweegt in de schillen eromheen.", W),
                 ("kort", "Waar zit bijna de hele massa van een atoom?", "in de kern", WW),
                 ("waar", "Een neutraal atoom heeft even veel protonen als elektronen.", True),
             ]),
        dict(kop="Rekenen met atoomnummer en massagetal",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("atoomnummer 11, massagetal 23: hoeveel neutronen?", "12"),
                          ("atoomnummer 8, massagetal 16: hoeveel neutronen?", "8")], None, "70px"),
                 ("rij", [("atoomnummer 17: hoeveel protonen?", "17"),
                          ("atoomnummer 17: hoeveel elektronen in een neutraal atoom?", "17")],
                  None, "70px"),
                 ("open", "Leg uit hoe je het aantal neutronen van een atoom berekent.",
                  "Je trekt het atoomnummer van het massagetal af. Het massagetal is immers het aantal "
                  "protonen plus neutronen, en het atoomnummer is het aantal protonen.", 4),
             ]),
        dict(kop="Isotopen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Waarin verschillen twee isotopen van hetzelfde element?",
                  "in het aantal neutronen", WL),
                 ("waar", "Twee isotopen van hetzelfde element hebben een ander atoomnummer.", False),
                 ("open", "Waarom staat de relatieve atoommassa in het periodiek systeem bijna nooit "
                          "op een rond getal?",
                  "Ze is een gemiddelde van de isotopen van dat element, gewogen naar hoe vaak elke "
                  "isotoop voorkomt.", 4),
             ]),
        dict(kop="Periode en groep",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een horizontale rij", "een periode"),
                          ("een verticale kolom", "een groep")], None, WW),
                 ("rij", [("groep 2, periode 4: hoeveel valentie-elektronen?", "2"),
                          ("groep 2, periode 4: hoeveel bezette schillen?", "4")], None, "70px"),
                 ("kort", "Wat is de elektronenconfiguratie van natrium, atoomnummer 11?", "2, 8, 1",
                  W),
                 ("kort", "Hoeveel elektronen passen er in de tweede schil?", "8", "60px"),
             ]),
        dict(kop="Waarom elementen reageren",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("kort", "Hoe heet de bijzonder stabiele elektronenverdeling met een volle buitenste "
                          "schil?", "de edelgasconfiguratie", WL),
                 ("open", "Waarom neemt een zuurstofatoom liever twee elektronen op dan er zes af te "
                          "staan?",
                  "Twee opnemen vraagt veel minder dan zes afstaan om de volle buitenste schil te "
                  "bereiken. Zuurstof wordt daardoor een ion met lading twee min.", 4),
                 ("open", "Waarom gaan de edelgassen bijna geen bindingen aan?",
                  "Ze hebben al een volle buitenste schil en zijn dus stabiel. Ze hoeven geen "
                  "elektronen op te nemen of af te staan.", 3),
                 ("kort", "Noem drie edelgassen.", "helium, neon en argon", WW),
             ]),
        dict(kop="Trends in het systeem",
             opdracht="Kies of vul aan.",
             oefeningen=[
                 ("kies", "Waar in het periodiek systeem staan de metalen?",
                  ["rechtsboven", "links en in het midden", "in de laatste kolom",
                   "alleen in de eerste periode"], 1),
                 ("waar", "Het aantal valentie-elektronen van een hoofdgroepelement lees je af aan "
                          "het periodenummer.", False),
                 ("open", "Wat gebeurt er met het metaalkarakter als je in een periode naar rechts "
                          "gaat?",
                  "Het neemt af. De elektronegativiteit, de gretigheid naar elektronen, neemt juist "
                  "toe.", 3),
             ]),
        dict(kop="Uitgebreid: absolute massa en de atoommassa-eenheid",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("open", "Leg het verschil uit tussen de relatieve atoommassa en de absolute massa "
                          "van een atoom.",
                  "De relatieve atoommassa is een vergelijking met de atoommassa-eenheid u en heeft "
                  "geen eenheid. De absolute massa is de echte massa van het atoom en staat in "
                  "kilogram.", 4),
                 ("open", "Hoe reken je van een relatieve atoommassa naar een absolute massa?",
                  "Je vermenigvuldigt de relatieve atoommassa met de waarde van één u in kilogram.",
                  3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemische-bindingen-en-roosters-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Chemische bindingen en roosters",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke binding?",
             opdracht="Schrijf ionbinding, atoombinding of metaalbinding.",
             oefeningen=[
                 ("rij", [("NaCl", "ionbinding"), ("H2O", "atoombinding"), ("Cu", "metaalbinding")],
                  None, WW),
                 ("rij", [("CaO", "ionbinding"), ("CO2", "atoombinding"),
                          ("messing", "metaalbinding")], None, WW),
                 ("open", "Leg uit waarom een metaal met een niet-metaal een ionbinding vormt.",
                  "Het metaal staat zijn valentie-elektronen gemakkelijk af en het niet-metaal neemt "
                  "ze op. Zo ontstaan er ionen met tegengestelde lading, die elkaar aantrekken.", 4),
             ]),
        dict(kop="Ionen en formules",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("natrium wordt het ion", "Na plus"),
                          ("calcium wordt het ion", "Ca twee plus"),
                          ("chloor wordt het ion", "Cl min")], "Welk ion?", WW),
                 ("rij", [("natrium met chloor", "NaCl"), ("calcium met chloor", "CaCl2"),
                          ("magnesium met zuurstof", "MgO")], "Welke formule?", WW),
                 ("open", "Waarom is de formule van calciumchloride CaCl2 en niet CaCl?",
                  "Calcium geeft twee elektronen af en chloor neemt er één op. Je hebt dus twee "
                  "chloride-ionen nodig om de ladingen te laten opgaan tegen elkaar.", 4),
             ]),
        dict(kop="Enkelvoudig, dubbel of drievoudig?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("H2", "enkelvoudig"), ("O2", "dubbel"), ("N2", "drievoudig")],
                  "Welke binding?", WW),
                 ("kort", "Hoeveel elektronenparen delen de twee atomen in een stikstofmolecule?",
                  "drie", W),
                 ("kort", "Hoeveel bindingen maakt koolstof gewoonlijk?", "vier", W),
             ]),
        dict(kop="Uitgebreid: de Lewisstructuur",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("een streepje tussen twee atomen", "een bindend elektronenpaar"),
                          ("een streepje bij één atoom", "een vrij elektronenpaar")], "Wat is het?",
                  WL),
                 ("open", "Leg uit hoeveel vrije elektronenparen een zuurstofatoom in water heeft, en "
                          "waarom.",
                  "Twee. Zuurstof heeft zes valentie-elektronen; twee ervan zitten in de bindingen met "
                  "de waterstofatomen, en de vier andere vormen twee vrije paren.", 4),
                 ("kort", "Wat is het oxidatiegetal van een element in een enkelvoudige stof?",
                  "nul", "60px"),
                 ("kort", "Welk oxidatiegetal heeft zuurstof meestal?", "min twee", W),
             ]),
        dict(kop="Welk rooster?",
             opdracht="Schrijf ionrooster, molecuulrooster, atoomrooster of metaalrooster.",
             oefeningen=[
                 ("rij", [("keukenzout", "ionrooster"), ("diamant", "atoomrooster"),
                          ("ijzer", "metaalrooster")], None, WW),
                 ("rij", [("jood", "molecuulrooster"), ("kwarts", "atoomrooster"),
                          ("koolstofdioxide", "molecuulrooster")], None, WW),
             ]),
        dict(kop="Eigenschappen verklaren",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom heeft een ionrooster een hoog smeltpunt en toch een breekbare "
                          "structuur?",
                  "De aantrekking tussen de ionen is in alle richtingen sterk, en dat geeft een hoog "
                  "smeltpunt. Schuif je de lagen een stukje op, dan komen gelijke ladingen tegenover "
                  "elkaar en stoten die elkaar af, zodat het kristal breekt.", 5),
                 ("open", "Waarom geleidt keukenzout pas als het gesmolten of opgelost is?",
                  "In het vaste rooster zitten de ionen op hun plaats. Pas als ze kunnen bewegen, "
                  "kunnen ze lading vervoeren.", 4),
                 ("open", "Waarom heeft een molecuulrooster een laag smelt- en kookpunt?",
                  "Binnen de molecule zijn de bindingen sterk, maar tussen de moleculen is de "
                  "aantrekking zwak. Er is dus weinig energie nodig om de moleculen van elkaar los te "
                  "maken.", 4),
                 ("open", "Een metaal geleidt elektriciteit, glanst en is plooibaar. Verklaar die drie "
                          "eigenschappen met de elektronenzee.",
                  "De elektronen zijn vrij en kunnen dus lading vervoeren, en ze kaatsen het licht "
                  "terug, wat de glans geeft. De ionen kunnen over elkaar schuiven zonder dat de "
                  "binding breekt, en daarom is een metaal plooibaar.", 5),
             ]),
        dict(kop="Vooruitlopen op de stof",
             opdracht="Kies of leg uit.",
             oefeningen=[
                 ("open", "Je krijgt de brutoformule van een stof met een metaal en een niet-metaal "
                          "erin. Wat kan je al voorspellen?",
                  "Dat het een ionverbinding is, opgebouwd uit een ionrooster van ionen. Een hoog "
                  "smeltpunt en geleiden in opgeloste toestand horen daar ook bij.", 4),
                 ("waar", "Een stof die uit twee verschillende elementen bestaat, noem je een "
                          "ternaire stof.", False),
                 ("kort", "Hoe heet de kleinste verhouding waarin de ionen in een ionrooster "
                          "voorkomen?", "de formule-eenheid", WL),
             ]),
        dict(kop="Diamant en grafiet",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Diamant", "Grafiet"],
                  [["hoe de atomen gebonden zijn", None, None], ["geleidt?", None, None],
                   ["hard of zacht?", None, None]],
                  "In diamant is elk koolstofatoom aan vier andere gebonden, in alle richtingen; in "
                  "grafiet aan drie, in lagen. Diamant geleidt niet, grafiet wel, want daar is per "
                  "atoom één elektron vrij. Diamant is heel hard, grafiet is zacht, want de lagen "
                  "schuiven over elkaar.", "130px"),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stoffen-classificeren-en-benoemen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stoffen classificeren en benoemen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stofklasse?",
             opdracht="Schrijf oxide, hydroxide, zuur of zout.",
             oefeningen=[
                 ("rij", [("CaO", "oxide"), ("NaOH", "hydroxide"), ("HCl", "zuur")], None, WW),
                 ("rij", [("KBr", "zout"), ("H2SO4", "zuur"), ("Ca(OH)2", "hydroxide")], None, WW),
                 ("rij", [("Fe2O3", "oxide"), ("CaCO3", "zout")], None, WW),
             ]),
        dict(kop="Binair of ternair?",
             opdracht="Schrijf binair of ternair.",
             oefeningen=[
                 ("rij", [("zoutzuur", "binair"), ("zwavelzuur", "ternair"),
                          ("keukenzout", "binair")], None, WW),
                 ("rij", [("calciumcarbonaat", "ternair"), ("calciumoxide", "binair"),
                          ("salpeterzuur", "ternair")], None, WW),
                 ("open", "Waarom is een oxide altijd binair?",
                  "Een oxide bestaat uit één element plus zuurstof, dus uit twee elementen. Komt er "
                  "een derde bij, dan is het geen oxide meer.", 3),
             ]),
        dict(kop="De zuurresten",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Ion", "Formule", "Komt van welk zuur"],
                  [["nitraation", None, None], ["sulfaation", None, None],
                   ["carbonaation", None, None]],
                  "Het nitraation is NO3 min en komt van salpeterzuur. Het sulfaation is SO4 twee min "
                  "en komt van zwavelzuur. Het carbonaation is CO3 twee min en komt van koolzuur.",
                  "120px"),
                 ("rij", [("bevat zuurstof: chloraat of chloride?", "chloraat"),
                          ("bevat zuurstof: sulfaat of sulfide?", "sulfaat")], None, WW),
                 ("kort", "Welke groep herken je in de formule van een hydroxide?",
                  "de hydroxidegroep OH", WL),
             ]),
        dict(kop="Benoemen en formules schrijven",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("FeCl3 in stocknotatie", "ijzer(III)chloride"),
                          ("CO2 met Griekse telwoorden", "koolstofdioxide")], "Welke naam?", WL),
                 ("rij", [("natriumsulfaat", "Na2SO4"), ("calciumnitraat", "Ca(NO3)2")],
                  "Welke formule?", WW),
                 ("open", "Wanneer gebruik je de stocknotatie en wanneer de Griekse telwoorden?",
                  "De stocknotatie bij ionverbindingen, met het oxidatiegetal van het metaal in "
                  "Romeinse cijfers tussen haakjes. De Griekse telwoorden bij atoomverbindingen "
                  "tussen niet-metalen.", 4),
             ]),
        dict(kop="De alkanen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("3 koolstofatomen", "propaan"), ("5 koolstofatomen", "pentaan"),
                          ("8 koolstofatomen", "octaan")], "Welke naam?", WW),
                 ("rij", [("hexaan", "6"), ("decaan", "10"), ("ethaan", "2")],
                  "Hoeveel koolstofatomen?", "60px"),
                 ("kort", "Uit welke twee elementen bestaat een alkaan?", "koolstof en waterstof",
                  WL),
                 ("open", "Leg uit hoe je aan de naam van een alkaan ziet hoeveel koolstofatomen het "
                          "heeft.",
                  "Het telwoord zit vooraan in de naam: but is vier, pent vijf, hex zes, oct acht, "
                  "dec tien. De uitgang aan zegt dat het een alkaan is.", 4),
             ]),
        dict(kop="Triviale namen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Gebruiksnaam", "Wetenschappelijke naam"],
                  [["keukenzout", None], ["bakpoeder", None], ["bijtende soda", None],
                   ["zoutzuur", None]],
                  "Keukenzout is natriumchloride. Bakpoeder is natriumwaterstofcarbonaat. Bijtende "
                  "soda is natriumhydroxide. Zoutzuur is waterstofchloride in water.", WL),
                 ("kort", "Waarvoor gebruiken we ammoniak onder andere?",
                  "als schoonmaakmiddel en als grondstof voor kunstmest", WL),
                 ("kort", "Welk zuur zit in frisdrank van het colatype?", "fosforzuur", WW),
             ]),
        dict(kop="Toepassen",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Tot welke stofklasse hoort natriumwaterstofcarbonaat, en waaraan zie je "
                          "dat?",
                  "Het is een ternair zout: er zit een metaalion in, natrium, en een zuurrest met "
                  "zuurstof, de carbonaatgroep.", 4),
                 ("open", "Waarom verdwijnt kalkaanslag met azijn?",
                  "Kalkaanslag is calciumcarbonaat. Carbonaten reageren met een zuur en vallen daarbij "
                  "uiteen, waarbij er koolstofdioxide vrijkomt.", 4),
                 ("open", "Leg het verschil uit tussen een brutoformule en een structuurformule.",
                  "Een brutoformule telt alleen de atomen, zoals C2H6. Een structuurformule toont ook "
                  "welke atomen aan welke gebonden zijn.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stoffen-in-water-reacties-en-berekeningen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stoffen in water, reacties en berekeningen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Dissociëren of ioniseren?",
             opdracht="Schrijf dissociëren of ioniseren.",
             oefeningen=[
                 ("rij", [("NaCl in water", "dissociëren"), ("HCl in water", "ioniseren"),
                          ("NaOH in water", "dissociëren")], None, WW),
                 ("open", "Leg het verschil tussen de twee uit.",
                  "Bij dissociëren zaten de ionen al in het rooster van de stof en komen ze los van "
                  "elkaar. Bij ioniseren is de stof uit moleculen opgebouwd en ontstaan de ionen pas "
                  "in het water.", 4),
                 ("kort", "Wat schrijf je op als de dissociatievergelijking van natriumchloride in "
                          "water?", "NaCl wordt Na plus en Cl min", WL),
             ]),
        dict(kop="Elektrolyt of niet?",
             opdracht="Schrijf elektrolyt of niet-elektrolyt.",
             oefeningen=[
                 ("rij", [("keukenzout in water", "elektrolyt"),
                          ("suiker in water", "niet-elektrolyt"),
                          ("zoutzuur", "elektrolyt")], None, WL),
                 ("open", "Een gesmolten zout geleidt elektriciteit, zonder water erbij. Hoe kan dat?",
                  "Door het smelten zijn de ionen los van hun plaats in het rooster gekomen. Ze kunnen "
                  "nu bewegen en dus lading vervoeren.", 4),
             ]),
        dict(kop="De pH",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("pH 2", "zuur"), ("pH 7", "neutraal"), ("pH 12", "basisch")], None, W),
                 ("rij", [("azijn", "zuur"), ("zuiver water", "neutraal"),
                          ("natriumhydroxide in water", "basisch")], None, W),
                 ("kort", "Welk ion geeft een zuur in water vrij?", "een waterstofion", WL),
                 ("kort", "Welk ion geeft een hydroxide in water vrij?", "een hydroxide-ion", WL),
                 ("waar", "Je kan de zuurtegraad van een oplossing alleen met een indicator meten en "
                          "niet met een toestel.", False),
             ]),
        dict(kop="Rekenen met mol",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Hoeveel gram is 2 mol water? (M = 18 g/mol)", "36 gram", W),
                 ("kort", "Hoeveel mol is 44 gram koolstofdioxide? (M = 44 g/mol)", "1 mol", W),
                 ("kort", "Hoeveel gram is 0,5 mol natriumchloride? (M = 58,5 g/mol)",
                  "29,25 gram", W),
                 ("open", "Leg uit hoe je van gram naar mol rekent.",
                  "Je deelt de massa in gram door de molaire massa in gram per mol. Omgekeerd "
                  "vermenigvuldig je het aantal mol met de molaire massa.", 4),
             ]),
        dict(kop="Concentratie",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", "Je lost 0,2 mol zout op in 1 liter water. Hoe groot is de concentratie?",
                  "0,2 mol per liter", W),
                 ("kort", "Hoeveel mol zit er in 500 mL van een oplossing van 0,4 mol per liter?",
                  "0,2 mol", W),
                 ("open", "Je verdunt 100 mL van een oplossing van 1 mol per liter tot 500 mL. Wat "
                          "wordt de nieuwe concentratie, en waarom?",
                  "0,2 mol per liter. Het aantal mol blijft 0,1, maar het volume wordt vijf keer "
                  "groter, dus de concentratie wordt vijf keer kleiner.", 4),
             ]),
        dict(kop="Uitgebreid: neerslag en neutralisatie",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("kort", "Wat is het reactieproduct van een waterstofion en een hydroxide-ion?",
                  "water", W),
                 ("open", "Wat is een neerslagreactie?",
                  "Twee oplossingen worden gemengd en er ontstaat een stof die niet oplost. Die zakt "
                  "als vast neerslag naar de bodem.", 4),
                 ("open", "Leg uit wat de essentiële reactievergelijking van een reactie is.",
                  "Daarin schrijf je alleen de ionen die echt mee reageren. De ionen die aan beide "
                  "kanten ongewijzigd in oplossing blijven, laat je weg.", 4),
                 ("open", "Waarom blijft de pH van een neutralisatiereactie met een sterk zuur en een "
                          "sterke base rond 7 uitkomen, als je precies genoeg van elk neemt?",
                  "Alle waterstofionen en hydroxide-ionen vormen samen water. Er blijft dan geen "
                  "overmaat van een van de twee over, en wat overblijft is een zoutoplossing.", 5),
             ]),
        dict(kop="Uitgebreid: redoxreacties",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("staat elektronen af", "wordt geoxideerd"),
                          ("neemt elektronen op", "wordt gereduceerd")], "Wat gebeurt er?", WL),
                 ("open", "Waarom kan een oxidatie niet zonder een reductie gebeuren?",
                  "De elektronen die de ene stof afstaat, moeten door een andere stof opgenomen "
                  "worden. De twee halfreacties horen dus altijd samen.", 4),
                 ("kort", "Wat gebeurt er met het oxidatiegetal van een atoom dat geoxideerd wordt?",
                  "het stijgt", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-rechtlijnige-bewegingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Rechtlijnige bewegingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Woorden die je moet kennen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de hele weg die je aflegt", "de afgelegde weg"),
                          ("van startpunt naar eindpunt in rechte lijn", "de verplaatsing")],
                  "Welk begrip?", WL),
                 ("kort", "Wat is de SI-eenheid van snelheid?", "meter per seconde", WL),
                 ("kort", "Welk symbool gebruiken we voor de versnelling?", "a", "60px"),
             ]),
        dict(kop="Rekenen met snelheid",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Een auto rijdt 150 km in 2 uur. Hoe groot is zijn gemiddelde snelheid in "
                          "km/h?", "75 km/h", W),
                 ("kort", "Hoeveel is 72 km/h in meter per seconde?", "20 m/s", W),
                 ("kort", "Hoeveel is 15 m/s in km/h?", "54 km/h", W),
                 ("kort", "Een fietser rijdt met 5 m/s. Hoe ver komt hij in 2 minuten?", "600 meter",
                  W),
             ]),
        dict(kop="Rekenen met versnelling",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Een wagen gaat in 5 seconden van 0 naar 20 m/s. Hoe groot is de "
                          "versnelling?", "4 m/s²", W),
                 ("kort", "Een trein vertraagt van 30 m/s tot stilstand in 15 seconden. Hoe groot is "
                          "de versnelling?", "min 2 m/s²", W),
                 ("open", "Wat betekent een versnelling van min 2 m/s²?",
                  "De snelheid neemt elke seconde met 2 m/s af. Het voorwerp vertraagt dus.", 3),
             ]),
        dict(kop="Grafieken lezen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("een rechte in een x,t-grafiek", "eenparige beweging"),
                          ("een rechte in een v,t-grafiek", "eenparig versnelde beweging")],
                  "Welke beweging?", WL),
                 ("open", "Wat betekent de steilheid van een x,t-grafiek?",
                  "Ze geeft de snelheid. Een steilere rechte betekent een grotere snelheid.", 3),
                 ("open", "Wat betekent de oppervlakte onder een v,t-grafiek?",
                  "Ze geeft de afgelegde weg in dat tijdsinterval.", 3),
                 ("open", "Een x,t-grafiek loopt een tijdje horizontaal. Wat doet het voorwerp dan?",
                  "Het staat stil: de plaats verandert niet meer terwijl de tijd doorloopt.", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een eenparige beweging is de versnelling nul.", True),
                 ("waar", "De afgelegde weg en de verplaatsing zijn altijd gelijk.", False),
                 ("waar", "Een beweging kan een negatieve versnelling hebben terwijl ze vooruit "
                          "gaat.", True),
                 ("waar", "De snelheid is een vectoriële grootheid, dus met een zin erbij.", True),
             ]),
        dict(kop="Toepassen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Je loopt één ronde rond een atletiekpiste van 400 meter en komt weer uit "
                          "bij je startpunt. Hoe groot is je afgelegde weg, en hoe groot je "
                          "verplaatsing?",
                  "De afgelegde weg is 400 meter. De verplaatsing is nul, want eindpunt en startpunt "
                  "liggen op dezelfde plaats.", 4),
                 ("open", "Twee treinen rijden naast elkaar met dezelfde snelheid. Waarom lijkt de "
                          "andere trein stil te staan?",
                  "Beweging is altijd ten opzichte van een referentiepunt. Ten opzichte van de andere "
                  "trein verandert je plaats niet, dus lijkt die stil te staan.", 4),
                 ("open", "Waarom is de remweg van een auto bij een dubbele snelheid veel meer dan "
                          "dubbel zo lang?",
                  "De kinetische energie stijgt met het kwadraat van de snelheid. Bij dubbele snelheid "
                  "is er dus vier keer zo veel energie weg te remmen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vrije-val-verticale-worp-en-krachten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Vrije val, verticale worp en krachten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De vrije val",
             opdracht="Reken uit en schrijf je stappen op. Reken met g = 10 m/s².",
             oefeningen=[
                 ("kort", "Een steen valt 3 seconden. Hoe groot is zijn snelheid dan?", "30 m/s", W),
                 ("kort", "Hoe diep is hij in die 3 seconden gevallen?", "45 meter", W),
                 ("kort", "Een bal valt van 20 meter hoog. Hoe lang duurt die val?",
                  "2 seconden", W),
                 ("open", "Waarom valt een veertje in een vacuümbuis even snel als een loden kogel?",
                  "In een vacuüm is er geen luchtweerstand. De zwaartekracht geeft elk voorwerp "
                  "dezelfde versnelling, wat ook zijn massa is.", 4),
             ]),
        dict(kop="De verticale worp",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Je gooit een bal met 20 m/s recht naar boven. Hoe lang duurt het voor hij "
                          "stilstaat in het hoogste punt?", "2 seconden", W),
                 ("kort", "Hoe hoog komt die bal?", "20 meter", W),
                 ("open", "Hoe groot is de snelheid in het hoogste punt, en hoe groot de versnelling "
                          "daar?",
                  "De snelheid is nul, maar de versnelling blijft de zwaarteveldsterkte, naar beneden "
                  "gericht. Daarom valt de bal meteen weer terug.", 4),
             ]),
        dict(kop="Massa of gewicht?",
             opdracht="Schrijf massa of gewicht.",
             oefeningen=[
                 ("rij", [("wordt uitgedrukt in kilogram", "massa"),
                          ("wordt uitgedrukt in newton", "gewicht"),
                          ("is overal in het heelal gelijk", "massa")], None, WW),
                 ("rij", [("hangt af van het hemellichaam", "gewicht"),
                          ("is een kracht", "gewicht")], None, WW),
                 ("kort", "Een kind van 40 kg staat op aarde. Hoe groot is zijn gewicht? "
                          "(g = 10 N/kg)", "400 newton", W),
                 ("open", "Een astronaut zweeft in een ruimtestation. Wat is er met zijn massa "
                          "gebeurd?",
                  "Niets, zijn massa is net dezelfde als op aarde. Hij is wel gewichtloos, want het "
                  "station en hij vallen samen rond de aarde.", 4),
             ]),
        dict(kop="Welke kracht?",
             opdracht="Schrijf de naam van de kracht.",
             oefeningen=[
                 ("rij", [("trekt alles naar de aarde", "de zwaartekracht"),
                          ("werkt tegen de beweging in", "de wrijvingskracht")], "Welke kracht?",
                  WL),
                 ("rij", [("duwt een vloer terug tegen je voeten", "de normaalkracht"),
                          ("trekt een uitgerekte veer samen", "de veerkracht")], "Welke kracht?",
                  WL),
             ]),
        dict(kop="Rekenen met de veerkracht",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", "Een veer met veerconstante 50 N/m wordt 0,2 meter uitgerekt. Hoe groot is "
                          "de veerkracht?", "10 newton", W),
                 ("kort", "Een kracht van 15 newton rekt een veer 0,3 meter uit. Hoe groot is de "
                          "veerconstante?", "50 N/m", W),
                 ("open", "Een grafiek van de kracht in functie van de uitrekking is een rechte door "
                          "de oorsprong. Wat betekent de steilheid?",
                  "Dat is de veerconstante. Een steilere rechte betekent een stijvere veer.", 3),
             ]),
        dict(kop="De wetten van Newton",
             opdracht="Vul aan, kies of leg uit.",
             oefeningen=[
                 ("kort", "Een massa van 5 kg krijgt een versnelling van 3 m/s². Hoe groot is de "
                          "resulterende kracht?", "15 newton", W),
                 ("kort", "Een kracht van 24 newton werkt op een massa van 8 kg. Hoe groot is de "
                          "versnelling?", "3 m/s²", W),
                 ("kies", "Wat gebeurt er met een voorwerp waarop geen resulterende kracht werkt?",
                  ["het blijft in rust of beweegt met gelijke snelheid rechtdoor",
                   "het valt altijd naar beneden", "het versnelt gelijkmatig",
                   "het komt altijd tot stilstand"], 0),
                 ("open", "Je zit in een bus die plots remt en je schuift naar voren. Verklaar dat "
                          "met de eerste wet van Newton.",
                  "Je lichaam blijft met dezelfde snelheid vooruit bewegen, want er werkt geen kracht "
                  "op om je tegen te houden. De bus vertraagt wel, en daardoor schuif je naar voren.",
                  4),
                 ("open", "Leg de derde wet van Newton uit met een voorbeeld.",
                  "Oefent voorwerp A een kracht uit op B, dan oefent B een even grote kracht in de "
                  "tegengestelde zin uit op A. Duw je tegen een muur, dan duwt de muur even hard "
                  "terug.", 4),
             ]),
        dict(kop="Evenwicht",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Een boek ligt stil op een tafel. Welke twee krachten werken erop, en wat "
                          "geldt voor hun som?",
                  "De zwaartekracht naar beneden en de normaalkracht van de tafel naar boven. Ze zijn "
                  "even groot en tegengesteld, dus de resulterende kracht is nul.", 4),
                 ("open", "Een valschermspringer valt op het laatst met een gelijke snelheid. Leg uit "
                          "wat er met de krachten gebeurd is.",
                  "De luchtweerstand is gegroeid tot ze even groot is als de zwaartekracht. De "
                  "resulterende kracht is dan nul, dus is er geen versnelling meer en blijft de "
                  "snelheid gelijk.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-druk-en-de-gaswetten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Druk en de gaswetten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Rekenen met druk",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Een kracht van 200 newton werkt op 0,5 m². Hoe groot is de druk?",
                  "400 pascal", W),
                 ("kort", "Een druk van 300 pascal werkt op 2 m². Hoe groot is de kracht?",
                  "600 newton", W),
                 ("kort", "Wat is de SI-eenheid van druk?", "de pascal", W),
                 ("open", "Waarom zakt iemand met sneeuwschoenen minder diep weg in de sneeuw dan "
                          "iemand op gewone schoenen?",
                  "Het gewicht blijft gelijk, maar het wordt over een veel groter oppervlak verdeeld. "
                  "Daardoor is de druk veel kleiner.", 4),
             ]),
        dict(kop="Druk in vloeistoffen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("hangt af van de diepte", "de hydrostatische druk"),
                          ("hoe hoger je komt, hoe kleiner", "de luchtdruk")], "Welke druk?", WL),
                 ("waar", "De hydrostatische druk hangt af van de breedte van het vat.", False),
                 ("kort", "Hoeveel bar voegt elke tien meter water ongeveer toe?",
                  "ongeveer 1 bar", W),
                 ("open", "Waarom moet een duiker zijn oren klaren als hij afdaalt?",
                  "De waterdruk duwt op zijn trommelvlies, terwijl er in zijn middenoor nog de oude "
                  "druk staat. Door te klaren laat hij lucht in het middenoor, zodat de druk aan "
                  "beide kanten gelijk wordt.", 5),
                 ("kort", "Hoe noem je een druk die lager is dan de omgevingsdruk?", "onderdruk",
                  WW),
             ]),
        dict(kop="Pascal en zijn toepassingen",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Wat zegt het beginsel van Pascal?",
                  "Een drukverandering plant zich in een vloeistof in alle richtingen even sterk "
                  "voort.", 3),
                 ("open", "In een hydraulische pers is de druk overal gelijk, en toch komt er een veel "
                          "grotere kracht uit. Leg uit hoe dat kan.",
                  "Kracht is druk maal oppervlakte. Bij een tien keer groter oppervlak krijg je dus "
                  "een tien keer grotere kracht, maar over een tien keer kortere weg.", 4),
                 ("rij", [("meet de luchtdruk buiten", "een barometer"),
                          ("meet de druk in een vat of leiding", "een manometer")],
                  "Welk toestel?", WL),
             ]),
        dict(kop="Druk in gassen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("open", "Leg met het deeltjesmodel uit hoe de druk van een gas ontstaat.",
                  "De deeltjes botsen tegen de wand en duwen daar bij elke botsing op. Miljarden "
                  "botsingen per seconde geven samen een gelijkmatige druk, in alle richtingen.", 4),
                 ("waar", "Verwarm je een gas in een gesloten stalen fles, dan stijgt de druk.",
                  True),
                 ("open", "Waarom staat er op een spuitbus dat je ze niet mag verwarmen?",
                  "Het volume kan niet mee, dus stijgt de druk bij verwarmen. Bij een te hoge druk "
                  "kan de bus openscheuren.", 4),
             ]),
        dict(kop="Uitgebreid: de gaswetten en de kelvinschaal",
             opdracht="Deze reeks staat enkel in de uitgebreide fiche. Reken en leg uit.",
             oefeningen=[
                 ("kort", "Hoe noem je de temperatuurschaal die bij het absolute nulpunt begint?",
                  "de kelvinschaal", WL),
                 ("rij", [("27 graden celsius in kelvin", "300 K"),
                          ("373 kelvin in graden celsius", "100 °C")], None, W),
                 ("rij", [("bij gelijke druk", "isobaar"), ("bij gelijk volume", "isochoor"),
                          ("bij gelijke temperatuur", "isotherm")], "Welke naam?", WW),
                 ("kort", "Een gas van 2 liter bij 100 kPa wordt bij gelijke temperatuur tot 1 liter "
                          "geperst. Hoe groot wordt de druk?", "200 kPa", W),
                 ("open", "Waarom moet je bij de gaswetten altijd in kelvin rekenen en niet in graden "
                          "celsius?",
                  "De wetten gaan over verhoudingen. Bij nul graden celsius is er nog beweging van de "
                  "deeltjes, dus mag je daar niet door delen; de kelvinschaal begint wel bij het "
                  "echte nulpunt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-arbeid-energie-vermogen-en-rendement-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Arbeid, energie, vermogen en rendement",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Uitgebreid: arbeid",
             opdracht="Arbeid staat enkel in de uitgebreide fiche. Reken uit en leg uit.",
             oefeningen=[
                 ("kort", "Je duwt een doos 4 meter ver met 30 newton in de zin van de beweging. Hoe "
                          "groot is de arbeid?", "120 joule", W),
                 ("kort", "Wat is de eenheid van arbeid?", "de joule", W),
                 ("open", "Je duwt met al je kracht tegen een muur die niet beweegt. Hoeveel arbeid "
                          "verricht je in de natuurkundige zin, en waarom?",
                  "Geen arbeid, want er is geen verplaatsing. Arbeid is kracht maal verplaatsing, en "
                  "nul verplaatsing geeft nul arbeid.", 4),
                 ("open", "Een gewicht hangt stil aan een koord. Welke arbeid verricht de spankracht?",
                  "Geen arbeid, want er is geen verplaatsing.", 2),
                 ("open", "Waarom verricht een kracht die loodrecht op de verplaatsing staat geen "
                          "arbeid?",
                  "Alleen de component van de kracht in de zin van de verplaatsing doet mee. Staat de "
                  "kracht loodrecht, dan is die component nul.", 4),
             ]),
        dict(kop="Welke energievorm?",
             opdracht="Schrijf de naam van de energievorm.",
             oefeningen=[
                 ("rij", [("een steen hoog op een muur", "hoogte-energie"),
                          ("een rijdende auto", "kinetische energie"),
                          ("een ingedrukte veer", "elastische energie")], "Welke vorm?", WW),
                 ("rij", [("een volle batterij", "chemische energie"),
                          ("een warme radiator", "warmte-energie")], "Welke vorm?", WW),
             ]),
        dict(kop="Rekenen met energie",
             opdracht="Reken uit. Reken met g = 10 N/kg.",
             oefeningen=[
                 ("kort", "Een massa van 4 kg ligt 5 meter hoog. Hoe groot is de hoogte-energie?",
                  "200 joule", W),
                 ("kort", "Een wagen van 1000 kg rijdt 10 m/s. Hoe groot is de kinetische energie?",
                  "50 000 joule", W),
                 ("kort", "Diezelfde wagen rijdt 20 m/s. Hoe groot is de kinetische energie nu?",
                  "200 000 joule", W),
                 ("open", "Je verdubbelt de snelheid en de kinetische energie wordt vier keer zo "
                          "groot. Leg uit waarom.",
                  "In de formule staat de snelheid in het kwadraat. Twee keer meer snelheid geeft dus "
                  "vier keer meer energie.", 4),
             ]),
        dict(kop="Energie blijft bewaard",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Beschrijf de energiebalans van een slingerende schommel.",
                  "In het hoogste punt is de hoogte-energie het grootst en de kinetische energie nul. "
                  "In het laagste punt is het omgekeerd. Zonder wrijving blijft de som van de twee "
                  "gelijk.", 5),
                 ("open", "Waarom komt een echte schommel toch steeds minder hoog?",
                  "Door wrijving met de lucht en in de ophanging gaat er bij elke slag energie als "
                  "warmte verloren. Die energie is niet verdwenen, maar ze is niet meer bruikbaar om "
                  "de schommel hoog te krijgen.", 5),
                 ("waar", "Energie kan verdwijnen als er wrijving is.", False),
             ]),
        dict(kop="Vermogen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("kort", "Een motor levert 600 joule in 3 seconden. Hoe groot is het vermogen?",
                  "200 watt", W),
                 ("kort", "Een toestel van 2000 watt staat 30 seconden aan. Hoeveel energie gebruikt "
                          "het?", "60 000 joule", W),
                 ("kort", "Een lamp van 1000 watt staat 2 uur aan. Hoeveel kilowattuur is dat?",
                  "2 kWh", W),
                 ("open", "Twee kranen tillen dezelfde last even hoog, maar de ene doet er half zo "
                          "lang over. Wat geldt voor hun arbeid en voor hun vermogen?",
                  "De arbeid is gelijk, want de last en de hoogte zijn gelijk. Het vermogen van de "
                  "snelste kraan is dubbel zo groot, want ze levert die arbeid in de helft van de "
                  "tijd.", 5),
             ]),
        dict(kop="Rendement",
             opdracht="Reken uit en leg uit.",
             oefeningen=[
                 ("kort", "Een toestel krijgt 500 joule en levert 400 joule nuttig. Hoe groot is het "
                          "rendement?", "80 procent", W),
                 ("kort", "Een motor met een rendement van 25 procent krijgt 800 joule. Hoeveel "
                          "nuttige energie levert hij?", "200 joule", W),
                 ("open", "Waarom is het rendement van een toestel nooit 100 procent?",
                  "Een deel van de energie wordt altijd omgezet in een vorm die je niet nodig hebt, "
                  "meestal warmte door wrijving of weerstand.", 4),
                 ("open", "Een ledlamp heeft een veel hoger rendement dan een gloeilamp. Wat betekent "
                          "dat voor de warmte die ze afgeeft?",
                  "Ze zet een veel groter deel van de elektrische energie in licht om, en dus wordt er "
                  "veel minder warmte afgegeven.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-warmte-en-faseovergangen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Warmte en faseovergangen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Temperatuur en warmte",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("27 graden celsius in kelvin", "300 K"),
                          ("0 kelvin in graden celsius", "min 273 °C")], None, W),
                 ("open", "Leg het verschil uit tussen temperatuur en warmte.",
                  "Temperatuur zegt hoe snel de deeltjes gemiddeld bewegen. Warmte is energie die van "
                  "een warm naar een koud voorwerp overgaat, en ze hangt ook van de massa af.", 4),
                 ("waar", "Warmte gaat altijd van het warme naar het koude voorwerp.", True),
             ]),
        dict(kop="Hoe gaat de warmte over?",
             opdracht="Schrijf geleiding, stroming of straling.",
             oefeningen=[
                 ("rij", [("de steel van een pan wordt warm", "geleiding"),
                          ("de zon warmt je gezicht op", "straling")], None, WW),
                 ("rij", [("warme lucht stijgt naar het plafond", "stroming"),
                          ("de radiator warmt de hele kamer", "stroming")], None, WW),
                 ("open", "Waarom voelt een tegelvloer kouder aan dan een tapijt bij dezelfde "
                          "temperatuur?",
                  "De tegel geleidt de warmte van je voet veel sneller weg. Je voelt dus niet de "
                  "temperatuur zelf, maar hoe snel je warmte verliest.", 4),
             ]),
        dict(kop="Rekenen met warmte",
             opdracht="Reken uit. Reken met c = 4180 J/(kg·K) voor water.",
             oefeningen=[
                 ("kort", "Hoeveel warmte heb je nodig om 1 kg water 10 graden op te warmen?",
                  "41 800 joule", W),
                 ("kort", "Hoeveel warmte heb je nodig om 2 kg water van 20 naar 30 graden te "
                          "brengen?", "83 600 joule", W),
                 ("open", "Leg uit waarom de zee veel langzamer opwarmt dan het zand op het strand.",
                  "Water heeft een veel grotere specifieke warmtecapaciteit. Je hebt dus veel meer "
                  "warmte nodig om één kilogram water één graad op te warmen dan voor één kilogram "
                  "zand.", 4),
                 ("open", "Je giet een liter water van 80 graden bij een liter van 20 graden. Welke "
                          "eindtemperatuur verwacht je, en waarom?",
                  "Ongeveer 50 graden, het gemiddelde. De massa's en de stof zijn gelijk, dus wat het "
                  "warme water afgeeft, neemt het koude op.", 4),
             ]),
        dict(kop="Welke faseovergang?",
             opdracht="Schrijf de naam en of er warmte opgenomen of afgegeven wordt.",
             oefeningen=[
                 ("rij", [("vast naar vloeibaar", "smelten, neemt op"),
                          ("vloeibaar naar gas", "verdampen, neemt op")], "Welke overgang?", WL),
                 ("rij", [("gas naar vloeibaar", "condenseren, geeft af"),
                          ("vloeibaar naar vast", "stollen, geeft af")], "Welke overgang?", WL),
                 ("rij", [("vast rechtstreeks naar gas", "sublimeren, neemt op"),
                          ("gas rechtstreeks naar vast", "desublimeren, geeft af")],
                  "Welke overgang?", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Tijdens het smelten blijft de temperatuur van een zuivere stof gelijk.",
                  True),
                 ("waar", "Verdampen koelt af.", True),
                 ("waar", "Een stof krimpt altijd als ze afkoelt.", False),
                 ("waar", "IJs is lichter dan water, en daarom blijft het drijven.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Waarom blijft de temperatuur gelijk zolang ijs smelt, ook al blijf je "
                          "warmte toevoeren?",
                  "Alle toegevoerde warmte gaat naar het losmaken van de deeltjes uit het rooster. Pas "
                  "als al het ijs gesmolten is, gaat de temperatuur weer stijgen.", 5),
                 ("open", "Waarom koelt zweten je af?",
                  "Het zweet verdampt, en verdampen vraagt warmte. Die warmte haalt het zweet uit je "
                  "huid, en daardoor koel je af.", 4),
                 ("open", "Waarom laat je bij een vloer op vloerverwarming een voeg of een naad open?",
                  "Materiaal zet uit als het opwarmt. Zonder plaats om uit te zetten komt er spanning "
                  "op en kunnen de tegels kraken of opwippen.", 4),
                 ("open", "Waarom slaat er damp op een koude spiegel in de badkamer?",
                  "De warme, vochtige lucht raakt het koude glas, koelt af en kan minder waterdamp "
                  "dragen. Die damp condenseert tot kleine druppeltjes.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektriciteit-en-de-wet-van-ohm-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Elektriciteit en de wet van Ohm",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Grootheid, eenheid en meettoestel",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Grootheid", "Eenheid", "Meettoestel"],
                  [["stroomsterkte", None, None], ["spanning", None, None],
                   ["weerstand", None, None]],
                  "De stroomsterkte meet je in ampère met een ampèremeter. De spanning meet je in volt "
                  "met een voltmeter. De weerstand meet je in ohm met een ohmmeter.", W),
                 ("kort", "Hoe sluit je een ampèremeter aan: in serie of parallel?", "in serie", WW),
                 ("kort", "Hoe sluit je een voltmeter aan?", "parallel", WW),
             ]),
        dict(kop="Rekenen met de wet van Ohm",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("kort", "Een weerstand van 20 ohm staat op 12 volt. Hoe groot is de stroom?",
                  "0,6 ampère", W),
                 ("kort", "Door een weerstand van 50 ohm loopt 0,2 ampère. Hoe groot is de spanning?",
                  "10 volt", W),
                 ("kort", "Op 230 volt loopt 2 ampère. Hoe groot is de weerstand?", "115 ohm", W),
                 ("open", "De spanning blijft gelijk en je halveert de weerstand. Wat gebeurt er met "
                          "de stroom, en waarom?",
                  "De stroom verdubbelt. Stroom is spanning gedeeld door weerstand, dus een halve "
                  "weerstand geeft een dubbele stroom.", 4),
             ]),
        dict(kop="Geleider of isolator?",
             opdracht="Schrijf geleider of isolator.",
             oefeningen=[
                 ("rij", [("koper", "geleider"), ("droog hout", "isolator"),
                          ("aluminium", "geleider")], None, WW),
                 ("rij", [("een zoutoplossing", "geleider"), ("rubber", "isolator"),
                          ("glas", "isolator")], None, WW),
                 ("waar", "Een groter geleidingsvermogen betekent een grotere weerstand.", False),
                 ("open", "Waarom is de kern van een snoer van koper en de mantel van kunststof?",
                  "Koper geleidt goed, dus kan de stroom er met weinig verlies door. De kunststof is "
                  "een isolator en houdt de stroom binnen, zodat je je niet kan verwonden.", 4),
             ]),
        dict(kop="Serie of parallel?",
             opdracht="Reken uit of leg uit.",
             oefeningen=[
                 ("kort", "Twee weerstanden van 10 ohm staan in serie. Hoe groot is de totale "
                          "weerstand?", "20 ohm", W),
                 ("kort", "Twee weerstanden van 10 ohm staan parallel. Hoe groot is de totale "
                          "weerstand?", "5 ohm", W),
                 ("open", "Twee lampjes staan in serie en je draait er één los. Wat gebeurt er met "
                          "het andere, en waarom?",
                  "Het gaat ook uit. In een serieschakeling is er maar één kring, en die is nu "
                  "onderbroken.", 4),
                 ("open", "Waarom zijn de lampen in een huis parallel geschakeld?",
                  "Zo staat op elke lamp dezelfde spanning en kan je ze afzonderlijk aan- en "
                  "uitzetten. Valt er een uit, dan blijven de andere branden.", 4),
             ]),
        dict(kop="Wat bepaalt de weerstand van een draad?",
             opdracht="Schrijf groter of kleiner.",
             oefeningen=[
                 ("rij", [("een langere draad", "groter"), ("een dikkere draad", "kleiner")],
                  "De weerstand wordt...", WW),
                 ("open", "Waarom gebruikt men voor een zwaar toestel een dikkere draad?",
                  "Een dikkere draad heeft minder weerstand. Zo wordt hij minder warm bij een grote "
                  "stroom en is er minder verlies.", 4),
             ]),
        dict(kop="Vermogen en het Joule-effect",
             opdracht="Reken uit of leg uit.",
             oefeningen=[
                 ("kort", "Een toestel op 230 volt trekt 2 ampère. Hoe groot is het vermogen?",
                  "460 watt", W),
                 ("kort", "Een lamp van 60 watt staat 5 uur aan. Hoeveel kilowattuur gebruikt ze?",
                  "0,3 kWh", W),
                 ("open", "Wat is het Joule-effect, en noem een toestel dat erop werkt.",
                  "Een geleider met weerstand wordt warm als er stroom door loopt. Een "
                  "elektrische kachel, een waterkoker of een broodrooster werkt daarop.", 4),
             ]),
        dict(kop="Veilig met elektriciteit",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("schakelt af bij te veel stroom", "de zekering of automaat"),
                          ("schakelt af bij een lek naar de aarde", "de verliesstroomschakelaar")],
                  "Welk toestel?", WL),
                 ("open", "Waarom verbindt men de metalen behuizing van een toestel met de aarding?",
                  "Komt er door een defect spanning op de behuizing, dan loopt de stroom naar de aarde "
                  "weg in plaats van door iemand die het toestel aanraakt. De beveiliging schakelt "
                  "dan af.", 5),
                 ("open", "Je ziet iemand die een stroomdraad vastheeft en niet meer loslaat. Wat doe "
                          "je eerst?",
                  "Je schakelt de stroom af, bij de zekeringkast of door de stekker uit te trekken. Je "
                  "raakt de persoon niet aan zolang de stroom er nog op staat.", 4),
                 ("waar", "Een verliesstroomschakelaar grijpt in bij een stroom die naar de aarde "
                          "wegloopt.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meten-en-levensreddend-handelen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Veilig werken, meten en levensreddend handelen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De gevarenpictogrammen",
             opdracht="Schrijf wat het pictogram betekent. Je mag ze niet natekenen, enkel "
                      "beschrijven wat je op het etiket moet lezen.",
             oefeningen=[
                 ("rij", [("een vlam", "licht ontvlambaar"),
                          ("een doodshoofd", "giftig")], "Wat betekent het?", WL),
                 ("rij", [("een hand en een oppervlak dat wegvreet", "bijtend of corrosief"),
                          ("een dode vis en een dode boom", "gevaarlijk voor het milieu")],
                  "Wat betekent het?", WL),
                 ("kort", "Wat moet er altijd op een etiket van een chemisch product staan, naast de "
                          "naam?", "de gevarenpictogrammen", WL),
             ]),
        dict(kop="Veilig werken in het labo",
             opdracht="Kruis aan of leg uit.",
             oefeningen=[
                 ("waar", "Je mag een vloeistof terug in de voorraadfles gieten als je te veel "
                          "uitgoot.", False),
                 ("waar", "Je draagt een veiligheidsbril zolang er iemand in het labo met chemicaliën "
                          "werkt.", True),
                 ("waar", "Je ruikt aan een stof door je neus boven de opening te houden en diep in "
                          "te ademen.", False),
                 ("open", "Waarom giet je een zuur bij water en niet water bij een zuur?",
                  "Het mengen geeft veel warmte. Giet je zuur bij veel water, dan verdeelt die warmte "
                  "zich over het water; omgekeerd kan het plaatselijk opspatten of koken.", 5),
                 ("open", "Waarom gooi je restanten van chemicaliën niet in de gootsteen?",
                  "Ze kunnen het water en de waterzuivering schaden, en sommige reageren met elkaar in "
                  "de afvoer. Ze horen in de daarvoor bestemde afvalbak.", 4),
             ]),
        dict(kop="Meten",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("om een volume nauwkeurig af te meten", "een maatcilinder of pipet"),
                          ("om een massa te meten", "een balans")], "Welk toestel?", WL),
                 ("open", "Waarom lees je een maatcilinder af met je oog op de hoogte van de "
                          "vloeistof?",
                  "Kijk je van boven of van onder, dan lees je door de kijkhoek een verkeerde waarde "
                  "af. Je leest af onderaan de holle bovenkant van de vloeistof.", 4),
                 ("kort", "Hoeveel beduidende cijfers heeft een meetresultaat van 1,2 meter?",
                  "twee", W),
                 ("open", "Waarom herhaal je een meting een paar keer?",
                  "Om de invloed van toevallige meetfouten kleiner te maken. Het gemiddelde ligt "
                  "dichter bij de echte waarde.", 4),
             ]),
        dict(kop="Eerste hulp: de eerste stappen",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("open", "Wat doe je altijd eerst bij een ongeval, voor je iemand helpt?",
                  "Je zorgt voor je eigen veiligheid en voor die van de omstaanders. Een hulpverlener "
                  "die zelf gewond raakt, helpt niemand.", 4),
                 ("kort", "Welk noodnummer bel je in België?", "112", "60px"),
                 ("open", "Je vindt iemand die niet reageert maar wel normaal ademt. Wat doe je?",
                  "Je legt die persoon in de stabiele zijligging, zodat de luchtweg vrij blijft, en je "
                  "belt hulp. Je blijft de ademhaling in het oog houden.", 4),
             ]),
        dict(kop="Hartstilstand en reanimatie",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("open", "Hoe herken je een hartstilstand?",
                  "Het slachtoffer reageert niet en ademt niet of niet normaal. Een paar happende "
                  "bewegingen zijn geen normale ademhaling.", 4),
                 ("kort", "Hoeveel hartmassages wissel je af met hoeveel beademingen?",
                  "dertig met twee", W),
                 ("kort", "Hoe diep duw je bij een hartmassage?", "vijf tot zes centimeter", WL),
                 ("open", "Je ziet iemand in elkaar zakken die niet reageert en niet ademt. Wat is de "
                          "juiste orde?",
                  "Eerst hulp bellen, dan onmiddellijk starten met hartmassage. Je wacht niet en je "
                  "legt die persoon niet eerst in zijligging.", 4),
                 ("waar", "Je mag een reanimatie stoppen zodra je moe wordt, ook als er nog geen hulp "
                          "is.", False),
             ]),
        dict(kop="Verdrinking en verslikking",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Iemand dreigt te verdrinken. Wat doe je, en wat doe je niet?",
                  "Je zorgt eerst voor je eigen veiligheid en haalt het slachtoffer uit het water als "
                  "dat veilig kan, bijvoorbeeld door iets aan te reiken. Je springt niet zomaar zelf "
                  "het water in. Ademt het slachtoffer niet, dan begin je met beademen.", 5),
                 ("open", "Iemand verslikt zich en kan niet meer hoesten of spreken. Wat doe je?",
                  "Je geeft vijf stevige slagen tussen de schouderbladen. Helpt dat niet, dan wissel "
                  "je af met buikstoten, en je belt hulp.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-grootheden-eenheden-en-wetenschappelijk-onderzoek-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Grootheden, eenheden en wetenschappelijk onderzoek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Grootheid en eenheid",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("lengte", "meter"), ("massa", "kilogram"), ("tijd", "seconde")],
                  "Welke SI-eenheid?", WW),
                 ("rij", [("kracht", "newton"), ("energie", "joule"), ("vermogen", "watt")],
                  "Welke eenheid?", WW),
                 ("rij", [("druk", "pascal"), ("temperatuur", "kelvin")], "Welke SI-eenheid?", WW),
                 ("waar", "Een meetresultaat zonder eenheid is nog altijd bruikbaar als je het getal "
                          "kent.", False),
             ]),
        dict(kop="Omrekenen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("0,25 kilogram in gram", "250 gram"), ("45 centimeter in meter",
                                                                  "0,45 meter")], None, W),
                 ("rij", [("2,5 kilometer in meter", "2500 meter"),
                          ("3 milliliter in liter", "0,003 liter")], None, W),
                 ("kort", "Hoeveel seconden is 2 microseconden, in de macht van tien geschreven?",
                  "2 maal tien tot de macht min zes seconden", WL),
             ]),
        dict(kop="Welk verband?",
             opdracht="Schrijf recht evenredig, lineair, omgekeerd evenredig of kwadratisch.",
             oefeningen=[
                 ("rij", [("een rechte door de oorsprong", "recht evenredig"),
                          ("een rechte, niet door de oorsprong", "lineair")], "Welk verband?", WL),
                 ("rij", [("het product blijft gelijk", "omgekeerd evenredig"),
                          ("twee keer meer geeft vier keer meer", "kwadratisch")], "Welk verband?",
                  WL),
                 ("open", "Leg het verschil uit tussen een lineair en een recht evenredig verband.",
                  "Een recht evenredig verband is een rechte door de oorsprong; de verhouding blijft "
                  "gelijk. Een lineair verband hoeft niet door de oorsprong te gaan, want er kan een "
                  "constante bijkomen.", 4),
             ]),
        dict(kop="Nauwkeurig meten",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Je meet met een balans die tot op een gram nauwkeurig is. Hoe schrijf je "
                          "325 gram op?", "als 325 gram, met drie beduidende cijfers", WL),
                 ("open", "Waarom schrijf je dat resultaat niet op als 325,00 gram?",
                  "Dan doe je alsof je tot op een honderdste gram gemeten hebt, en dat is niet zo. Je "
                  "schrijft nooit meer beduidende cijfers op dan je gemeten hebt.", 4),
                 ("open", "Waarom maak je eerst een schatting van je antwoord?",
                  "Zo merk je meteen of je uitkomst een onzinnige grootte heeft. De echte berekening "
                  "maak je daarna nog altijd.", 3),
                 ("open", "Leg het verschil uit tussen een toevallige en een systematische meetfout.",
                  "Een toevallige fout springt de ene keer naar boven en de andere keer naar beneden, "
                  "en die haal je er met herhalen grotendeels uit. Een systematische fout schuift elke "
                  "meting dezelfde kant op, bijvoorbeeld een weegschaal die niet op nul stond.", 5),
             ]),
        dict(kop="De wetenschappelijke methode",
             opdracht="Nummer of vul aan.",
             oefeningen=[
                 ("rij", [("data verzamelen", "4"), ("een hypothese formuleren", "2"),
                          ("een onderzoeksplan maken", "3"),
                          ("de probleemstelling afbakenen", "1")], "Nummer van 1 tot 4", "60px"),
                 ("kort", "Hoe noem je je onderbouwde verwachting voor je begint te meten?",
                  "de hypothese", WW),
                 ("kort", "Hoe noem je het stuk waarin je terugkijkt op je methode en resultaten?",
                  "de reflectie", WW),
                 ("waar", "Een hypothese die weerlegd wordt, maakt het onderzoek waardeloos.", False),
             ]),
        dict(kop="Een proef beoordelen",
             opdracht="Leg in volledige zinnen uit.",
             oefeningen=[
                 ("open", "Je wil nagaan of plantjes sneller groeien met meer licht. Wat is de beste "
                          "opzet?",
                  "Dezelfde plantjes, dezelfde pot en dezelfde grond, en alleen een verschillende "
                  "lichtduur. Zo weet je dat het verschil van het licht komt.", 4),
                 ("open", "Waarom verander je maar één ding tegelijk in een proef?",
                  "Verander je twee dingen samen, dan weet je achteraf niet welke verandering het "
                  "gevolg veroorzaakt heeft.", 4),
                 ("open", "Waarom schrijf je op hoe je een onderzoek hebt uitgevoerd?",
                  "Zodat iemand anders het kan herhalen en je resultaat kan nakijken. Herhaalbaarheid "
                  "is een kern van wetenschap.", 4),
                 ("open", "Mag je je gegevens aanpassen als ze niet bij je hypothese passen?",
                  "Nee. De gegevens beslissen, niet je verwachting. Gegevens aanpassen is bedrog en "
                  "geen onderzoek.", 3),
             ]),
        dict(kop="Ontwerpen en STEM",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("kort", "Waarvoor staan de letters van STEM?",
                  "wetenschappen, technologie, engineering en wiskunde", WL),
                 ("kort", "Hoe noem je de voorwaarden waaraan je oplossing moet voldoen?",
                  "de criteria", WW),
                 ("open", "Wat doe je als eerste bij het ontwerpen van een oplossing?",
                  "Je definieert het probleem zo scherp als je kan. Pas daarna kies je materiaal of "
                  "bouw je een eerste versie.", 3),
                 ("open", "Waarom splits je een moeilijk probleem op in deelproblemen?",
                  "Elk deel is afzonderlijk makkelijker op te lossen, en samen vormen ze het geheel.",
                  3),
                 ("open", "Noem drie rollen die de STEM-disciplines bij de ontwikkeling van een "
                          "vaccin speelden.",
                  "Wetenschappelijke kennis om het vaccin te ontwikkelen, technologische kennis om het "
                  "koel te bewaren en te vervoeren, en wiskundige kennis om de verspreiding in kaart "
                  "te brengen.", 5),
                 ("waar", "Zodra je oplossing gebouwd is, ben je klaar en hoef je ze niet meer te "
                          "evalueren.", False),
             ]),
    ],
)
