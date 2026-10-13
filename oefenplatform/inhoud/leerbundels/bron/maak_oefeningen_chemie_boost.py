# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels voor chemie op 🚀 Boost doorstroom-niveau.

Eén oefenbundel per thema, met andere opgaven dan de vragen op het scherm en
met een antwoordblad achteraan. Geschreven náást de vakfiche chemie van de
2de graad doorstroomfinaliteit én náást de leerbundel van hetzelfde thema, in
[maak_chemie_boost].

De bundelsleutels beginnen met "oefenbundel-" en eindigen op
"-chemie-boost-doorstroom".

De relatieve atoommassa's die in de opgaven nodig zijn, staan telkens bij de
opgave zelf, zodat een kind geen periodiek systeem naast het blad hoeft te
leggen. Ze zijn op 0,1 afgerond, zoals de fiche afspreekt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Chemie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een uitleg: schrijf niet alleen wát er gebeurt, maar ook waaróm, met de juiste begrippen.",
    "Bij een berekening: schrijf eerst de formule op, dan de getallen, en zet de eenheid bij je antwoord.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-mengsels-zuivere-stoffen-en-scheidingstechnieken-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Mengsels, zuivere stoffen en scheidingstechnieken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Zuivere stof of mengsel?",
             opdracht="Schrijf zuivere stof, homogeen mengsel of heterogeen mengsel.",
             oefeningen=[
                 ("rij", [("gedestilleerd water", "zuivere stof"),
                          ("messing", "homogeen mengsel"),
                          ("beton", "heterogeen mengsel")], "Wat is het?", WW),
                 ("rij", [("zuurstofgas uit een fles", "zuivere stof"),
                          ("azijn in water", "homogeen mengsel"),
                          ("vinaigrette die schift", "heterogeen mengsel")], "Wat is het?", WW),
             ]),
        dict(kop="Welk soort mengsel?",
             opdracht="Schrijf aerosol, oplossing, schuim, suspensie, emulsie of legering.",
             oefeningen=[
                 ("rij", [("haarlak uit een spuitbus", "aerosol"),
                          ("opgeklopt eiwit", "schuim"),
                          ("roestvrij staal", "legering")], "Welk soort?", WW),
                 ("rij", [("handcrème", "emulsie"),
                          ("kalkhoudend water met zwevend slib", "suspensie"),
                          ("thee met suiker erin geroerd", "oplossing")], "Welk soort?", WW),
             ]),
        dict(kop="Stofeigenschap of niet?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het kookpunt van een stof is een stofeigenschap.", True),
                 ("waar", "De massa van een staal is een stofeigenschap.", False),
                 ("waar", "De oplosbaarheid is een stofeigenschap.", True),
                 ("waar", "Het volume van een staal is een stofeigenschap.", False),
             ]),
        dict(kop="Kies de techniek",
             opdracht="Schrijf welke scheidingstechniek je kiest.",
             oefeningen=[
                 ("rij", [("thee van de theeblaadjes scheiden", "filtreren"),
                          ("alcohol uit wijn halen", "destilleren"),
                          ("room van melk scheiden", "centrifugeren")], "Welke techniek?", WL),
                 ("rij", [("suiker overhouden uit siroop", "indampen"),
                          ("de pigmenten in bladgroen onderzoeken", "chromatografie"),
                          ("grind van zand scheiden", "zeven")], "Welke techniek?", WL),
                 ("open", "Leg uit waarom je opgelost keukenzout niet uit water kan filtreren.",
                  "Opgeloste ionen zijn veel kleiner dan de poriën van een filter, dus gaan ze er zonder "
                  "meer door. Een filter werkt op een verschil in deeltjesgrootte, en dat verschil is er "
                  "hier niet. Je moet het water laten verdampen.", 5),
             ]),
        dict(kop="Bij een destillatie",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("wat verdampt en weer opgevangen wordt", "het destillaat"),
                          ("het toestel dat de damp laat condenseren", "de liebigkoeler"),
                          ("de eigenschap waarop de techniek werkt", "het kookpunt")],
                  "Hoe heet het?", WL),
                 ("open", "Een leerling wil olie en water scheiden met een destillatie. Leg uit waarom "
                          "decanteren hier de betere keuze is.",
                  "Olie en water mengen niet en hebben een verschillende massadichtheid, dus liggen ze al "
                  "in twee lagen. Met een scheitrechter laat je de onderste laag eruit lopen, en dat kost "
                  "geen warmte. Destilleren zou je pas nodig hebben bij vloeistoffen die wel mengen.", 6),
                 ("open", "Waarom heeft een mengsel een kooktraject en geen kookpunt?",
                  "Het bestanddeel met het laagste kookpunt gaat er eerst uit. Daardoor verandert de "
                  "samenstelling tijdens het koken en stijgt de temperatuur verder, dus krijg je een "
                  "gebied in plaats van één punt.", 5),
             ]),
        dict(kop="Filtraat en residu",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe heet wat op het filter achterblijft?", "het residu", WW),
                 ("kort", "Hoe heet de vloeistof die door het filter loopt?", "het filtraat", WW),
                 ("open", "Noem twee scheidingstechnieken die op een verschil in deeltjesgrootte werken, "
                          "en één die op een verschil in oplosbaarheid werkt.",
                  "Zeven en filtreren werken op deeltjesgrootte. Extraheren werkt op oplosbaarheid: je "
                  "kiest een oplosmiddel waarin alleen de gewenste stof goed oplost.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-enkelvoudige-en-samengestelde-stoffen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Enkelvoudige en samengestelde stoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Symbool en naam",
             opdracht="Vul het ontbrekende in.",
             oefeningen=[
                 ("rij", [("Pb", "lood"), ("Sn", "tin"), ("Hg", "kwik")], "Welk element?", W),
                 ("rij", [("goud", "Au"), ("zink", "Zn"), ("mangaan", "Mn")], "Welk symbool?", W),
                 ("rij", [("Cr", "chroom"), ("Si", "silicium"), ("Kr", "krypton")], "Welk element?", W),
             ]),
        dict(kop="Een formule lezen",
             opdracht=r"Vul de tabel aan voor \(3\) Al₂(SO₄)₃.",
             oefeningen=[
                 ("tabel", ["", "Antwoord"],
                  [["de coëfficiënt", None], ["het aantal verschillende elementen", None],
                   ["het aantal aluminiumatomen in één formule-eenheid", None],
                   ["het aantal zuurstofatomen in één formule-eenheid", None],
                   ["enkelvoudig of samengesteld", None]],
                  r"Coëfficiënt \(3\); drie elementen (Al, S, O); twee aluminiumatomen; twaalf zuurstofatomen "
                  r"(\(3 \cdot 4\)); samengesteld.", WW),
                 ("rij", [("H₂O₂", r"\(4\)"), (r"\(2\) NH₃", r"\(8\)"), ("CaCl₂", r"\(3\)")],
                  "Hoeveel atomen in totaal?", W),
             ]),
        dict(kop="Enkelvoudig of samengesteld?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "S₈ is een enkelvoudige stof.", True),
                 ("waar", "CO is een enkelvoudige stof.", False),
                 ("waar", "Cu is een enkelvoudige stof.", True),
                 ("waar", "NH₃ is een enkelvoudige stof.", False),
             ]),
        dict(kop="Metaal, niet-metaal of edelgas?",
             opdracht="Schrijf op.",
             oefeningen=[
                 ("rij", [("Kr", "edelgas"), ("Ni", "metaal"), ("Br", "niet-metaal")],
                  "Wat is het?", WW),
                 ("open", "Noem drie eigenschappen van metalen en zeg bij elke waar ze van komt.",
                  "Ze geleiden elektriciteit en warmte, ze glanzen en ze zijn vervormbaar. Alle drie komen "
                  "van de vrije elektronen in het metaalrooster: die geven de lading door, kaatsen het "
                  "licht terug en laten de ionen langs elkaar schuiven.", 6),
                 ("open", "Welk metaal is bij kamertemperatuur vloeibaar, en wat zegt dat over de andere "
                          "metalen?",
                  "Kwik. Het is de uitzondering: alle andere metalen zijn bij kamertemperatuur vast.", 4),
             ]),
        dict(kop="Triviale namen en toepassingen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("beschermt tegen uv-straling hoog in de atmosfeer", "ozon"),
                          ("licht en niet brandbaar, voor ballonnen", "helium"),
                          ("brandstof die enkel water oplevert", "waterstofgas")],
                  "Welke stof?", WL),
                 ("open", "Leg uit waarom diamant en grafiet zo verschillend zijn, al bestaan ze uit "
                          "hetzelfde element.",
                  "De atomen liggen anders geschikt. In diamant zit elk koolstofatoom met vier "
                  "atoombindingen vast in een ruimtelijk rooster, dus is het hard en geleidt het niet. In "
                  "grafiet liggen de atomen in lagen die over elkaar schuiven, en de overblijvende "
                  "elektronen bewegen vrij, dus is het zacht en geleidt het wel.", 7),
                 ("rij", [("de kleur van chloorgas", "geelgroen"),
                          ("de kleur van zuiver koper", "roodbruin")], "Welke kleur?", WW),
             ]),
        dict(kop="Analyse of synthese?",
             opdracht="Kruis aan of leg uit.",
             oefeningen=[
                 ("waar", "Bij een synthese ontstaat uit meerdere stoffen één nieuwe stof.", True),
                 ("waar", "Bij een analyse worden stoffen samengevoegd.", False),
                 ("open", "Waarom heet NaCl een formule-eenheid en H₂O een brutoformule?",
                  "In een ionrooster bestaan geen losse moleculen, dus geeft NaCl enkel de kleinste "
                  "verhouding van de ionen. Water bestaat wel uit losse moleculen, dus geeft H₂O de bouw "
                  "van één deeltje.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemische-reacties-en-energie-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Chemische reacties en energie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Kloppend maken",
             opdracht="Schrijf de coëfficiënten voor de formules.",
             oefeningen=[
                 ("rij", [("... N₂ + ... H₂ → ... NH₃", r"\(1\), \(3\) en \(2\)"),
                          ("... Mg + ... O₂ → ... MgO", r"\(2\), \(1\) en \(2\)"),
                          ("... Al + ... Cl₂ → ... AlCl₃", r"\(2\), \(3\) en \(2\)")], "Welke coëfficiënten?", WL),
                 ("rij", [("... C₃H₈ + ... O₂ → ... CO₂ + ... H₂O", r"\(1\), \(5\), \(3\) en \(4\)"),
                          ("... H₂O₂ → ... H₂O + ... O₂", r"\(2\), \(2\) en \(1\)")], "Welke coëfficiënten?", WL),
             ]),
        dict(kop="Rekenen met de wet van behoud van massa",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(12\) g koolstof reageert volledig met \(32\) g zuurstofgas", r"\(44\) g"),
                          (r"\(24\) g magnesium reageert volledig met \(16\) g zuurstofgas", r"\(40\) g")],
                  "Hoeveel product?", WW),
                 ("open", r"Een leerling verbrandt \(5\) g staalwol in een open schaaltje en weegt achteraf "
                          r"\(7\) g. Leg uit waarom de massa gestegen is.",
                  "Het ijzer heeft zuurstof uit de lucht opgenomen en is ijzeroxide geworden. Die zuurstof "
                  "zit nu mee in de vaste stof, dus weegt het geheel meer. Er is geen massa uit het niets "
                  "gekomen.", 5),
                 ("open", "Dezelfde leerling verbrandt een kaars in een open schaaltje en weegt achteraf "
                          "minder. Leg uit waarom dat de wet niet tegenspreekt.",
                  "Bij het branden ontstaan koolstofdioxide en waterdamp, en die waaien weg. In een "
                  "gesloten vat zou de massa gelijk blijven.", 5),
             ]),
        dict(kop="Reactie of geen reactie?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Als er een neerslag ontstaat, is er een nieuwe stof gevormd.", True),
                 ("waar", "Zand dat water troebel maakt, is een chemische reactie.", False),
                 ("waar", "Bij een chemische reactie blijft het aantal atomen van elk element gelijk.",
                  True),
                 ("waar", "Bij een chemische reactie ontstaan nieuwe elementen.", False),
             ]),
        dict(kop="Exo of endo?",
             opdracht="Schrijf exo of endo.",
             oefeningen=[
                 ("rij", [("een houtvuur", "exo"),
                          ("fotosynthese", "endo"),
                          ("een koudepakje op een verstuiking", "endo")], "Exo of endo?", W),
                 ("rij", [("bakpoeder dat in een oven ontleedt", "endo"),
                          ("een handwarmer", "exo"),
                          ("ijzer dat roest", "exo")], "Exo of endo?", W),
                 ("open", r"Een leerling meet dat de oplossing in haar beker afkoelt van \(21\) naar \(14\) graden. "
                          "Welk soort reactie is dat, en waarom?",
                  "Endo-energetisch. De reactie heeft energie nodig en haalt die uit de oplossing en uit "
                  "de omgeving, dus daalt de temperatuur.", 4),
             ]),
        dict(kop="Het energiediagram",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("wat op de verticale as staat", "de inwendige energie"),
                          ("waar de producten liggen bij een exo-reactie", "lager dan de reagentia"),
                          ("het hoogteverschil tussen begin en eind", "de reactie-energie")],
                  "Vul aan.", WL),
                 ("open", "Teken in woorden het energiediagram van een endo-energetische reactie: waar "
                          "liggen de reagentia en de producten, en wat betekent het hoogteverschil?",
                  "De reagentia liggen onderaan en de reactieproducten erboven. Het hoogteverschil is de "
                  "reactie-energie, en die is hier opgenomen uit de omgeving.", 5),
             ]),
        dict(kop="Energie omzetten",
             opdracht="Schrijf de omzetting op, van welke vorm naar welke vorm.",
             oefeningen=[
                 ("rij", [("een gasvuur onder een pan", "chemisch naar thermisch"),
                          ("een zonnepaneel", "licht naar elektrisch"),
                          ("een oplaadbare batterij die oplaadt", "elektrisch naar chemisch")],
                  "Welke omzetting?", WL),
                 ("open", "Waarom zegt men dat chemische energie in de bindingen zit?",
                  "Om een binding te verbreken heb je energie nodig, en bij het vormen van een binding "
                  "komt energie vrij. Het verschil tussen de bindingen van de reagentia en die van de "
                  "producten is net de reactie-energie.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-bouw-van-atomen-en-ionen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De bouw van atomen en ionen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De elementaire deeltjes",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Deeltje", "Waar", "Lading"],
                  [["proton", None, None], ["neutron", None, None], ["elektron", None, None]],
                  r"Proton: in de kern, +\(1\). Neutron: in de kern, \(0\). Elektron: rond de kern, \(-1\).", WW),
                 ("waar", "Een elektron weegt ongeveer evenveel als een proton.", False),
                 ("waar", "Vrijwel de hele massa van een atoom zit in de kern.", True),
             ]),
        dict(kop="Tellen in de kern",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Atoom of ion", "Protonen", "Neutronen", "Elektronen"],
                  [[r"Z = \(19\), A = \(39\), neutraal", None, None, None],
                   [r"Z = \(16\), A = \(32\), ion met lading \(2\)−", None, None, None],
                   [r"Z = \(13\), A = \(27\), ion met lading \(3\)+", None, None, None]],
                  r"Kalium: \(19\) protonen, \(20\) neutronen, \(19\) elektronen. Zwavelion: \(16\) protonen, \(16\) "
                  r"neutronen, \(18\) elektronen. Aluminiumion: \(13\) protonen, \(14\) neutronen, \(10\) elektronen.", W),
                 ("open", "Een deeltje heeft twintig protonen en achttien elektronen. Welk ion is dat, en "
                          "hoe weet je dat?",
                  "Twintig protonen betekent calcium. Er zijn twee elektronen minder dan protonen, dus is "
                  r"de lading \(2\)+: het ion is Ca²⁺.", 5),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het aantal protonen bepaalt om welk element het gaat.", True),
                 ("waar", "Een positief ion ontstaat doordat een atoom protonen afgeeft.", False),
                 ("waar", "Bij het vormen van een ion verandert het aantal protonen niet.", True),
                 ("waar", "Het massagetal telt ook de elektronen mee.", False),
             ]),
        dict(kop="Relatieve en absolute massa",
             opdracht=r"Reken uit. Gebruik u = \(1{,}66 \cdot 10^{-27}\) kg.",
             oefeningen=[
                 ("rij", [(r"Ar = \(32{,}1\) (zwavel)", r"\(5{,}33 \cdot 10^{-26}\) kg"),
                          (r"Ar = \(23{,}0\) (natrium)", r"\(3{,}82 \cdot 10^{-26}\) kg")],
                  "Absolute massa van één atoom?", WL),
                 ("open", "Waarom heeft de relatieve atoommassa geen eenheid, en de molaire massa wel?",
                  "De relatieve atoommassa is een verhouding tussen twee massa's, dus vallen de eenheden "
                  "weg. De molaire massa is een massa per mol, dus staat ze in gram per mol.", 5),
             ]),
        dict(kop="Elektronenconfiguratie",
             opdracht="Schrijf de configuratie volgens Bohr.",
             oefeningen=[
                 ("rij", [(r"fluor, Z = \(9\)", r"\(2\), \(7\)"), (r"silicium, Z = \(14\)", r"\(2\), \(8\), \(4\)"),
                          (r"argon, Z = \(18\)", r"\(2\), \(8\), \(8\)")], "Welke configuratie?", WW),
                 ("rij", [(r"beryllium, Z = \(4\)", r"\(2\), \(2\)"), (r"fosfor, Z = \(15\)", r"\(2\), \(8\), \(5\)")],
                  "Welke configuratie?", WW),
                 ("open", "Waarom geeft een magnesiumatoom twee elektronen af en neemt het er geen zes op?",
                  r"Magnesium heeft de configuratie \(2\), \(8\), \(2\). Geeft het die twee af, dan blijft \(2\), \(8\) over, "
                  "de edelgasconfiguratie van neon. Zes opnemen zou veel meer moeite kosten voor hetzelfde "
                  "resultaat.", 6),
                 ("kort", "Hoe noem je de toestand met een volledig gevulde buitenste schil?",
                  "de edelgasconfiguratie", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-periodiek-systeem-der-elementen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Het periodiek systeem der elementen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Groep en periode",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Element", "Configuratie", "Groep", "Periode"],
                  [[r"lithium, Z = \(3\)", None, None, None], [r"zwavel, Z = \(16\)", None, None, None],
                   [r"calcium, Z = \(20\)", None, None, None]],
                  r"Lithium: \(2\), \(1\) — groep IA, periode \(2\). Zwavel: \(2\), \(8\), \(6\) — groep VIA, periode \(3\). "
                  r"Calcium: \(2\), \(8\), \(8\), \(2\) — groep IIA, periode \(4\).", WW),
                 ("open", r"Een element heeft de configuratie \(2\), \(8\), \(7\). In welke groep en periode staat het, "
                          "en hoe heet die groep?",
                  r"Drie bezette schillen, dus periode \(3\). Zeven valentie-elektronen, dus groep VIIA, de "
                  "halogenen. Het element is chloor.", 5),
             ]),
        dict(kop="De namen van de hoofdgroepen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("groep IA zonder waterstof", "de alkalimetalen"),
                          ("groep IIA", "de aardalkalimetalen"),
                          ("groep VIIA", "de halogenen")], "Hoe heet de groep?", WL),
                 ("kort", "Hoe heet de laatste groep van het periodiek systeem?", "de edelgassen", WL),
                 ("waar", "Waterstof is een alkalimetaal.", False),
                 ("waar", "Halogeen betekent zoutvormer.", True),
             ]),
        dict(kop="Welk ion vormt het?",
             opdracht="Schrijf het ion met zijn lading.",
             oefeningen=[
                 ("rij", [("kalium", "K¹⁺"), ("barium", "Ba²⁺"), ("broom", "Br¹⁻")], "Welk ion?", W),
                 ("rij", [("zwavel", "S²⁻"), ("aluminium", "Al³⁺"), ("stikstof", "N³⁻")],
                  "Welk ion?", W),
                 ("open", "Leg uit waarom een atoom uit groep VIA twee elektronen opneemt.",
                  "Het heeft zes valentie-elektronen en komt met twee erbij aan acht, de "
                  r"edelgasconfiguratie. Het ion krijgt daardoor lading \(2\)−.", 4),
             ]),
        dict(kop="Elektronegativiteit",
             opdracht="Kruis aan of leg uit.",
             oefeningen=[
                 ("waar", "De elektronegativiteit stijgt van links naar rechts in een periode.", True),
                 ("waar", "De elektronegativiteit stijgt als je in een groep naar onder gaat.", False),
                 ("waar", "Een metaal heeft een lage elektronegativiteit.", True),
                 ("open", "Leg uit waarom de elektronegativiteit naar onder in een groep daalt.",
                  "De buitenste schil komt verder van de kern te liggen, dus wordt de aantrekking op de "
                  "elektronen van een binding zwakker.", 4),
                 ("kies", "In welke hoek van het periodiek systeem staan de hoogste waarden?",
                  ["linksonder", "rechtsboven", "in het midden", "in de laatste rij"], 1),
             ]),
        dict(kop="Metaal of niet-metaal?",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("geeft makkelijk elektronen af", "een metaal"),
                          ("neemt eerder elektronen op", "een niet-metaal"),
                          ("vormt bijna nooit een ion", "een edelgas")], "Wat is het?", WL),
                 ("open", "Het ion Na¹⁺ en het atoom neon hebben dezelfde elektronenconfiguratie. Leg uit "
                          "hoe dat kan, en of ze daardoor dezelfde stof zijn.",
                  r"Natrium heeft \(2\), \(8\), \(1\) en geeft dat ene elektron af, dus blijft \(2\), \(8\) over, net als bij "
                  "neon. Dezelfde stof zijn ze niet: natrium heeft elf protonen in de kern en neon tien, "
                  "en het natriumion is geladen.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemische-bindingen-en-roosters-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Chemische bindingen en roosters",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk bindingstype?",
             opdracht="Schrijf ionbinding, atoombinding of metaalbinding.",
             oefeningen=[
                 ("rij", [("K en Br", "ionbinding"), ("N en H", "atoombinding"),
                          ("Cu en Zn", "metaalbinding")], "Welk bindingstype?", WW),
                 ("rij", [("Ca en O", "ionbinding"), ("C en Cl", "atoombinding"),
                          ("Al en Al", "metaalbinding")], "Welk bindingstype?", WW),
             ]),
        dict(kop="Formules opstellen",
             opdracht="Schrijf de formule-eenheid of de brutoformule.",
             oefeningen=[
                 ("rij", [("kalium en chloor", "KCl"), ("calcium en fluor", "CaF₂"),
                          ("aluminium en zuurstof", "Al₂O₃")], "Welke formule?", WW),
                 ("rij", [("magnesium en stikstof", "Mg₃N₂"), ("natrium en zwavel", "Na₂S")],
                  "Welke formule?", WW),
                 ("open", "Leg uit hoe je uit de ladingen van de ionen de formule van magnesiumchloride "
                          "vindt.",
                  "Magnesium geeft twee elektronen af en wordt Mg²⁺. Chloor neemt er één op en wordt "
                  "Cl¹⁻. De ladingen moeten elkaar opheffen, dus horen er twee chloride-ionen bij één "
                  "magnesiumion: MgCl₂.", 6),
             ]),
        dict(kop="Bindende en vrije elektronenparen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Stof", "Soort binding", "Gedeelde paren"],
                  [["H₂", None, None], ["O₂", None, None], ["N₂", None, None]],
                  r"H₂: enkelvoudig, \(1\) paar. O₂: dubbel, \(2\) paren. N₂: drievoudig, \(3\) paren.", WW),
                 ("rij", [("bindingen die één koolstofatoom vormt", "vier"),
                          ("bindingen die één waterstofatoom vormt", "één"),
                          ("vrije paren bij het zuurstofatoom in water", "twee")], "Hoeveel?", WW),
                 ("waar", "Een dubbele binding bestaat uit twee gedeelde elektronen.", False),
                 ("waar", "In een Lewisstructuur tekent men enkel de valentie-elektronen.", True),
             ]),
        dict(kop="Roostertype en eigenschappen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Stof", "Roostertype", "Geleidt als vaste stof?"],
                  [["MgO", None, None], ["diamant", None, None], ["vast CO₂", None, None],
                   ["koper", None, None]],
                  "MgO: ionrooster, nee. Diamant: atoomrooster, nee. Vast CO₂: molecuulrooster, nee. "
                  "Koper: metaalrooster, ja.", WW),
                 ("open", "Leg uit waarom een zout wel geleidt als het opgelost of gesmolten is, en niet "
                          "als vaste stof.",
                  "Er moeten vrij bewegende ladingen zijn. In het vaste rooster zitten de ionen vast op "
                  "hun plaats; opgelost of gesmolten kunnen ze bewegen en zo de lading doorgeven.", 5),
                 ("open", "Een zoutkristal breekt bij een kleine stoot, een koperdraad buigt. Leg beide "
                          "uit met het rooster.",
                  "Schuift in een zoutkristal een laag ionen een plaatsje op, dan komen gelijke ladingen "
                  "naast elkaar en stoot het kristal zichzelf uit elkaar. In koper houdt de wolk van vrije "
                  "elektronen de ionen bij elke verschuiving gewoon verder samen.", 7),
             ]),
        dict(kop="Oxidatiegetallen",
             opdracht="Schrijf het oxidatiegetal op.",
             oefeningen=[
                 ("rij", [("O in CaO", "−II"), ("H in H₂O", "+I"), ("Fe in Fe₂O₃", "+III")],
                  "Welk oxidatiegetal?", W),
                 ("rij", [("Cl in Cl₂", r"\(0\)"), ("S in H₂S", "−II"), ("N in NH₃", "−III")],
                  "Welk oxidatiegetal?", W),
                 ("open", "Waarom is het oxidatiegetal in een enkelvoudige stof altijd nul?",
                  "Er is geen ander element dat de elektronen naar zich toe trekt, dus blijft elk atoom "
                  "even sterk aan zijn eigen elektronen hangen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-anorganische-stofklassen-en-naamgeving-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Anorganische stofklassen en naamgeving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stofklasse?",
             opdracht="Schrijf oxide, hydroxide, zuur of zout. Bij een zuur of een zout ook binair of ternair.",
             oefeningen=[
                 ("rij", [("Fe₂O₃", "oxide"), ("KOH", "hydroxide"), ("HBr", "binair zuur")],
                  "Welke stofklasse?", WL),
                 ("rij", [("K₂SO₄", "ternair zout"), ("H₃PO₄", "ternair zuur"),
                          ("MgCl₂", "binair zout")], "Welke stofklasse?", WL),
                 ("waar", "H₂O hoort bij de stofklasse van de zuren.", False),
                 ("waar", "Elk zout bevat zuurstof.", False),
             ]),
        dict(kop="De zuurresten",
             opdracht="Vul het ontbrekende in.",
             oefeningen=[
                 ("rij", [("NO₃¹⁻", "nitraation"), ("CO₃²⁻", "carbonaation"),
                          ("S²⁻", "sulfide-ion")], "Hoe heet het ion?", WL),
                 ("rij", [("sulfaation", "SO₄²⁻"), ("fosfaation", "PO₄³⁻"),
                          ("bromide-ion", "Br¹⁻")], "Welke formule?", WW),
                 ("open", "Waarom eindigt het ene ion op -aat en het andere op -ide?",
                  "Een zuurrest met zuurstof krijgt de uitgang -aat, zoals sulfaat of nitraat. Een "
                  "zuurrest zonder zuurstof krijgt -ide, zoals chloride of sulfide.", 5),
             ]),
        dict(kop="Formules opstellen",
             opdracht="Schrijf de formule van het zout.",
             oefeningen=[
                 ("rij", [("natriumcarbonaat", "Na₂CO₃"), ("calciumfosfaat", "Ca₃(PO₄)₂"),
                          ("ammoniumchloride", "NH₄Cl")], "Welke formule?", WW),
                 ("rij", [("bariumsulfaat", "BaSO₄"), ("kaliumnitraat", "KNO₃")],
                  "Welke formule?", WW),
             ]),
        dict(kop="Naam en formule",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("SO₃", "zwaveltrioxide"), ("N₂O", "distikstofoxide"),
                          ("CO", "koolstofmonoxide")], "IUPAC-naam?", WL),
                 ("open", "Waarom schrijft men ijzer(III)chloride met een Romeins cijfer en calciumoxide "
                          "zonder?",
                  "Ijzer kan +II of +III zijn, dus moet het cijfer zeggen welk van de twee het hier is. "
                  "Calcium heeft maar één mogelijk oxidatiegetal, dus is het cijfer overbodig.", 5),
                 ("waar", "Bij een ionverbinding gebruikt men Griekse telwoorden in de IUPAC-naam.",
                  False),
             ]),
        dict(kop="Triviale namen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Triviale naam", "Formule"],
                  [["ongebluste kalk", None], ["gebluste kalk", None], ["bijtende soda", None],
                   ["soda", None], ["bakpoeder", None], ["lachgas", None]],
                  "CaO, Ca(OH)₂, NaOH, Na₂CO₃, NaHCO₃, N₂O.", WW),
                 ("rij", [("H₂SO₄", "zwavelzuur"), ("HNO₃", "salpeterzuur"), ("NH₃", "ammoniak")],
                  "Triviale naam?", WW),
                 ("open", "Een leerling schrijft dat bijtende soda en bakpoeder dezelfde stof zijn. Waarom "
                          "is dat fout, en waarvoor gebruikt men elk van de twee?",
                  "Bijtende soda is NaOH, een sterk hydroxide dat huid aantast en in ontstoppers zit. "
                  "Bakpoeder is NaHCO₃, een zout dat in deeg koolstofdioxide vrijmaakt zodat het rijst.", 6),
             ]),
        dict(kop="De reactiepatronen",
             opdracht="Schrijf op wat er ontstaat.",
             oefeningen=[
                 ("rij", [("CaO + water", "Ca(OH)₂, een hydroxide"),
                          ("CO₂ + water", "koolzuur, een zuur"),
                          ("HCl + NaOH", "NaCl en water")], "Wat ontstaat er?", WL),
                 ("open", "Leg uit waarom een metaaloxide basevormend is en een niet-metaaloxide "
                          "zuurvormend, met van elk een voorbeeld.",
                  "Een metaaloxide geeft met water een hydroxide, en een hydroxide maakt de oplossing "
                  "basisch: CaO wordt Ca(OH)₂. Een niet-metaaloxide geeft met water een zuur: CO₂ wordt "
                  "koolzuur, en SO₂ geeft zure regen.", 7),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-organische-stoffen-en-de-alkanen-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Organische stoffen en de alkanen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Naam en formule van de alkanen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Naam", "Formule"],
                  [["ethaan", None], ["pentaan", None], ["octaan", None], ["nonaan", None],
                   ["decaan", None]],
                  "C₂H₆, C₅H₁₂, C₈H₁₈, C₉H₂₀, C₁₀H₂₂.", WW),
                 ("rij", [("C₃H₈", "propaan"), ("C₆H₁₄", "hexaan"), ("CH₄", "methaan")],
                  "Welk alkaan?", WW),
                 ("open", r"Leg uit waarom de algemene formule van de n-alkanen CnH\(2n+2\) is.",
                  "Elk koolstofatoom in de keten draagt twee waterstofatomen, en aan de twee uiteinden "
                  "komt er telkens nog één bij. Daarom tel je bij 2n nog twee op.", 5),
             ]),
        dict(kop="Welke stofklasse?",
             opdracht="Schrijf alkaan, alkeen, alkyn, alcohol of carbonzuur.",
             oefeningen=[
                 ("rij", [("propeen", "alkeen"), ("propanol", "alcohol"),
                          ("propaanzuur", "carbonzuur")], "Welke stofklasse?", WW),
                 ("rij", [("ethyn", "alkyn"), ("butaan", "alkaan"), ("methanol", "alcohol")],
                  "Welke stofklasse?", WW),
                 ("rij", [("de functionele groep van een alcohol", "OH"),
                          ("de functionele groep van een carbonzuur", "COOH")], "Welke groep?", W),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een alkaan lost goed op in water.", False),
                 ("waar", "Hoe langer de koolstofketen, hoe hoger het kookpunt.", True),
                 ("waar", "Een alcohol is een base, want de formule bevat OH.", False),
                 ("waar", "Een carbonzuur kan zijn waterstof als H⁺ afgeven.", True),
             ]),
        dict(kop="Triviale namen en toepassingen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("drankalcohol", "ethanol"), ("azijnzuur", "ethaanzuur"),
                          ("mierenzuur", "methaanzuur")], "IUPAC-naam?", WW),
                 ("rij", [("zit in aardgas", "methaan"),
                          ("laat vruchten sneller rijpen", "etheen"),
                          ("brandt met een bijna onzichtbare vlam", "brandspiritus")],
                  "Welke stof?", WL),
                 ("open", "Methanol en ethanol lijken sterk op elkaar. Leg uit waarom methanol toch "
                          "levensgevaarlijk is.",
                  "Het lichaam zet methanol om in stoffen die het oog en het zenuwstelsel aantasten. "
                  "Enkele milliliter kan al blind maken.", 5),
             ]),
        dict(kop="Verbranden",
             opdracht="Vul aan of leg uit.",
             oefeningen=[
                 ("rij", [("... CH₄ + ... O₂ → ... CO₂ + ... H₂O", r"\(1\), \(2\), \(1\) en \(2\)"),
                          ("... C₂H₆ + ... O₂ → ... CO₂ + ... H₂O", r"\(2\), \(7\), \(4\) en \(6\)")],
                  "Welke coëfficiënten?", WL),
                 ("open", "Wat ontstaat er bij een volledige verbranding van een alkaan, en wat bij een "
                          "slechte verbranding? Zeg ook waarom dat gevaarlijk is.",
                  "Volledig: koolstofdioxide en water. Bij te weinig zuurstof ontstaat ook "
                  "koolstofmonoxide, en dat is kleurloos, geurloos en dodelijk, dus merk je het niet.", 6),
                 ("open", "Waarom gebruikt men propaan en butaan in gasflessen en niet decaan?",
                  "Propaan en butaan zijn bij lichte druk al vloeibaar, dus krijg je er veel van in een "
                  "kleine fles, en bij het opendraaien verdampen ze meteen. Decaan is bij "
                  "kamertemperatuur al een vloeistof en verdampt niet van zichzelf.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stoffen-in-water-polariteit-oplossen-en-ph-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stoffen in water: polariteit, oplossen en pH",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Polair of apolair?",
             opdracht="Schrijf polair of apolair.",
             oefeningen=[
                 ("rij", [("water", "polair"), ("hexaan", "apolair"), ("CCl₄", "apolair")],
                  "Polair of apolair?", WW),
                 ("rij", [("CO₂", "apolair"), ("ammoniak", "polair"), ("O₂", "apolair")],
                  "Polair of apolair?", WW),
                 ("open", "Twee moleculen hebben allebei polaire bindingen, maar de ene is als geheel "
                          "apolair. Hoe kan dat?",
                  "Als de molecule symmetrisch is, vallen de polaire bindingen tegen elkaar weg en blijft "
                  "er geen plus- of minkant over. Water is gebogen en dus polair; CO₂ is recht en dus "
                  "apolair.", 6),
                 ("kort", "Vanaf welk verschil in elektronegativiteit is een binding polair?", r"\(0{,}4\)", W),
             ]),
        dict(kop="De intermoleculaire krachten",
             opdracht="Schrijf welke kracht het is.",
             oefeningen=[
                 ("rij", [("tussen twee watermoleculen", "een waterstofbrug"),
                          ("tussen twee hexaanmoleculen", "een londonkracht"),
                          ("tussen een natriumion en water", "een ion-dipoolkracht")],
                  "Welke kracht?", WL),
                 ("open", "Leg uit waarom water pas bij honderd graden kookt, terwijl de molecule zo klein "
                          "is.",
                  "De watermoleculen houden elkaar vast met waterstofbruggen, de sterkste kracht tussen "
                  "moleculen. Om te koken moet je die bruggen verbreken, en dat vraagt veel energie.", 5),
                 ("kort", "Hoe noem je het omhullen van een opgelost ion door watermoleculen?",
                  "hydratatie", WW),
             ]),
        dict(kop="Lost het op?",
             opdracht="Schrijf ja of nee, en waarom.",
             oefeningen=[
                 ("rij", [("keukenzout in water", "ja, ionen en polair water"),
                          ("olijfolie in water", "nee, apolair in polair"),
                          ("vet in vlekkenwater", "ja, apolair in apolair")], "Lost het op?", WL),
                 ("open", "Een leerling wil een vetvlek met water uit haar trui halen en het lukt niet. "
                          "Leg uit waarom, en wat ze beter gebruikt.",
                  "Vet is apolair en water polair, dus mengen ze niet. Gelijk lost op in gelijk, dus "
                  "werkt een apolair oplosmiddel zoals vlekkenwater wel.", 5),
             ]),
        dict(kop="Dissociëren of ioniseren?",
             opdracht="Schrijf de vergelijking op.",
             oefeningen=[
                 ("rij", [("KCl in water", "KCl → K¹⁺ + Cl¹⁻"),
                          ("MgCl₂ in water", r"MgCl₂ → Mg²⁺ + 2 Cl¹⁻"),
                          ("HNO₃ in water", "HNO₃ → H¹⁺ + NO₃¹⁻")], "Welke vergelijking?", WL),
                 ("open", "Leg het verschil uit tussen dissociëren en ioniseren, met van elk een "
                          "voorbeeld.",
                  "Bij dissociëren bestonden de ionen al in het rooster en trekt het water ze enkel los: "
                  "KCl geeft K⁺ en Cl⁻. Bij ioniseren ontstaan de ionen pas in het water, uit een polaire "
                  "molecule: HCl geeft H⁺ en Cl⁻.", 7),
                 ("waar", "Suiker opgelost in water is een elektrolyt.", False),
                 ("waar", "Een vast zout is een isolator.", True),
             ]),
        dict(kop="De pH en de indicatoren",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Oplossing", "Zuur, neutraal of basisch", "Fenolftaleïne", "Lakmoes"],
                  [[r"pH \(2\)", None, None, None], [r"pH \(7\)", None, None, None], [r"pH \(12\)", None, None, None]],
                  r"pH \(2\): zuur, kleurloos, rood. pH \(7\): neutraal, kleurloos, (geen uitslag). "
                  r"pH \(12\): basisch, paars, blauw.", WW),
                 ("open", "Een oplossing is paars met fenolftaleïne. Wat weet je, en wat verwacht je met "
                          "lakmoes?",
                  "Ze is basisch, want fenolftaleïne wordt enkel in een base paars. Met lakmoes verwacht "
                  "je dus blauw.", 4),
                 ("open", r"Waarom zegt een pH van \(3\) iets over de concentratie H⁺?",
                  r"Hoe lager de pH, hoe meer H⁺ in de oplossing. Een pH van \(3\) ligt onder zeven, dus is de "
                  "oplossing zuur en zit er veel H⁺ in.", 4),
                 ("kort", "Met welk toestel meet je de pH nauwkeurig?", "een pH-meter", WW),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-neerslag-gas-neutralisatie-en-redoxreacties-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Neerslag-, gas-, neutralisatie- en redoxreacties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Oplosbaar of niet?",
             opdracht="Schrijf goed oplosbaar of slecht oplosbaar.",
             oefeningen=[
                 ("rij", [("NaNO₃", "goed oplosbaar"), ("AgCl", "slecht oplosbaar"),
                          ("BaSO₄", "slecht oplosbaar")], "Oplosbaar?", WW),
                 ("rij", [("K₂CO₃", "goed oplosbaar"), ("CaCO₃", "slecht oplosbaar"),
                          ("NH₄Cl", "goed oplosbaar")], "Oplosbaar?", WW),
             ]),
        dict(kop="Welk reactietype?",
             opdracht="Schrijf neerslagreactie, gasontwikkelingsreactie of neutralisatiereactie.",
             oefeningen=[
                 ("rij", [("AgNO₃ bij NaCl", "neerslagreactie"),
                          ("HCl bij Na₂CO₃", "gasontwikkelingsreactie"),
                          ("H₂SO₄ bij KOH", "neutralisatiereactie")], "Welk type?", WL),
                 ("rij", [("BaCl₂ bij Na₂SO₄", "neerslagreactie"),
                          ("NaOH bij NH₄Cl", "gasontwikkelingsreactie")], "Welk type?", WL),
             ]),
        dict(kop="De essentiële reactievergelijking",
             opdracht="Schrijf enkel de ionen op die echt reageren.",
             oefeningen=[
                 ("rij", [("AgNO₃ + NaCl", "Ag¹⁺ + Cl¹⁻ → AgCl"),
                          ("BaCl₂ + Na₂SO₄", "Ba²⁺ + SO₄²⁻ → BaSO₄"),
                          ("HCl + NaOH", "H¹⁺ + OH¹⁻ → H₂O")], "Welke vergelijking?", WL),
                 ("kort", "Hoe noem je de ionen die tijdens de reactie niets doen?", "tribune-ionen", WW),
                 ("open", "Waarom staat in de essentiële vergelijking van een neutralisatie met zoutzuur "
                          "en natriumhydroxide niets over natrium en chloride?",
                  "Die twee ionen blijven voor en na de reactie gewoon opgelost en veranderen niet. Alleen "
                  "de H⁺ en de OH⁻ reageren echt, tot water.", 5),
             ]),
        dict(kop="Welk gas komt vrij?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("zuur bij een carbonaat", "koolstofdioxide"),
                          ("zuur bij een sulfide", "waterstofsulfide"),
                          ("sterke base bij een ammoniumzout", "ammoniak")], "Welk gas?", WL),
                 ("open", "Leg uit waarom er bij zoutzuur op kalksteen een gas opschuimt.",
                  "Het zuur maakt uit het carbonaat koolzuur, en koolzuur valt onmiddellijk uiteen in "
                  "water en koolstofdioxide. Dat gas ontsnapt als belletjes.", 5),
             ]),
        dict(kop="Oxidatie en reductie",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Elektronen", "Oxidatiegetal", "Wie is het"],
                  [["oxidatie", None, None, None], ["reductie", None, None, None]],
                  "Oxidatie: elektronen afgeven, oxidatiegetal stijgt, de reductor ondergaat ze. "
                  "Reductie: elektronen opnemen, oxidatiegetal daalt, de oxidator ondergaat ze.", WW),
                 ("open", r"In de reactie 2 Mg + O₂ → 2 MgO: wie is de oxidator, wie de reductor, en hoe "
                          "veranderen de oxidatiegetallen?",
                  r"Magnesium is de reductor: het geeft elektronen af en gaat van \(0\) naar +II. Zuurstof is "
                  r"de oxidator: het neemt ze op en gaat van \(0\) naar −II.", 6),
                 ("open", "In de reactie Zn + CuSO₄ → ZnSO₄ + Cu: welke stof wordt geoxideerd, en wat zie "
                          "je gebeuren in de beker?",
                  r"Zink wordt geoxideerd van \(0\) naar +II en gaat in oplossing. Het koperion wordt "
                  "gereduceerd tot koper, dus slaat er roodbruin koper neer en verbleekt de blauwe kleur "
                  "van de oplossing.", 7),
             ]),
        dict(kop="Redox of ionenuitwisseling?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het verbranden van propaan is een redoxreactie.", True),
                 ("waar", "Een neerslagreactie is een vorm van elektronenoverdracht.", False),
                 ("waar", "Het roesten van ijzer is een redoxreactie.", True),
                 ("waar", "Bij een neutralisatie veranderen de oxidatiegetallen.", False),
             ]),
        dict(kop="De reactiepatronen",
             opdracht="Schrijf op wat er ontstaat, of reken uit.",
             oefeningen=[
                 ("rij", [("zwavel + dizuurstof", "SO₂, een niet-metaaloxide"),
                          ("ijzer + dizuurstof (vochtig)", "Fe₂O₃, roest"),
                          ("ethanol + dizuurstof", "CO₂ en water")], "Wat ontstaat er?", WL),
                 ("kort", "Hoeveel moleculen O₂ heb je nodig voor één molecule CH₄?", r"\(2\)", W),
                 ("open", "Waarom beschermt roest het ijzer eronder niet, terwijl de laag op aluminium dat "
                          "wel doet?",
                  "Roest bladdert af, dus komt er telkens nieuw ijzer bloot te liggen. De oxidelaag op "
                  "aluminium blijft wel vastzitten en sluit het metaal eronder af.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-rekenen-met-mol-massa-en-concentratie-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Rekenen met mol, massa en concentratie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE + [r"Gebruik N_A = \(6{,}02 \cdot 10^{23}\) deeltjes per mol. De relatieve atoommassa's staan bij de opgave."],
    reeksen=[
        dict(kop="De molaire massa",
             opdracht=r"Reken uit. H \(1{,}0\); C \(12{,}0\); N \(14{,}0\); O \(16{,}0\); Na \(23{,}0\); S \(32{,}1\); Cl \(35{,}5\); Ca \(40{,}1\).",
             oefeningen=[
                 ("rij", [("CH₄", r"\(16{,}0\) g/mol"), ("HNO₃", r"\(63{,}0\) g/mol"),
                          ("CaCO₃", r"\(100{,}1\) g/mol")], "Molaire massa?", WW),
                 ("rij", [("H₂SO₄", r"\(98{,}1\) g/mol"), ("NaCl", r"\(58{,}5\) g/mol")], "Molaire massa?", WW),
             ]),
        dict(kop="Van massa naar mol en terug",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(64{,}0\) g CH₄ (M = \(16{,}0\))", r"\(4{,}00\) mol"),
                          (r"\(117\) g NaCl (M = \(58{,}5\))", r"\(2{,}00\) mol"),
                          (r"\(5{,}00\) mol water (M = \(18{,}0\))", r"\(90{,}0\) g")], "Hoeveel?", WW),
                 ("rij", [(r"\(0{,}250\) mol CaCO₃ (M = \(100{,}1\))", r"\(25{,}0\) g"),
                          (r"\(22{,}0\) g CO₂ (M = \(44{,}0\))", r"\(0{,}500\) mol")], "Hoeveel?", WW),
                 ("open", r"Een leerling rekent uit dat \(2\) mol water \(9\) g weegt. Leg uit hoe je zonder "
                          "narekenen ziet dat dat niet kan.",
                  r"Eén mol water weegt \(18{,}0\) g, dus moet twee mol zwaarder zijn dan één mol. Negen gram is "
                  "juist de helft van één mol, dus heeft ze vermenigvuldigd waar ze moest delen.", 6),
             ]),
        dict(kop="Deeltjes tellen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(3{,}01 \cdot 10^{24}\) deeltjes", r"\(5{,}00\) mol"),
                          (r"\(0{,}100\) mol", r"\(6{,}02 \cdot 10^{22}\) deeltjes")], "Hoeveel?", WL),
                 ("waar", "Eén mol van elke stof bevat evenveel deeltjes.", True),
                 ("waar", "Eén mol water en één mol koolstofdioxide hebben dezelfde massa.", False),
             ]),
        dict(kop="Concentraties",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(0{,}600\) mol tot \(3{,}00\) L", r"\(0{,}200\) mol/L"),
                          (r"\(0{,}0500\) mol tot \(200\) mL", r"\(0{,}250\) mol/L"),
                          (r"\(1{,}50\) L van \(0{,}400\) mol/L", r"\(0{,}600\) mol")], "Hoeveel?", WW),
                 ("rij", [(r"\(58{,}5\) g NaCl per liter (M = \(58{,}5\))", r"\(1{,}00\) mol/L"),
                          (r"\(20{,}0\) g NaOH per liter (M = \(40{,}0\))", r"\(0{,}500\) mol/L")],
                  "Molaire concentratie?", WW),
                 ("open", "Leg uit in welke stappen je van een massaconcentratie in g/L naar een molaire "
                          "concentratie in mol/L gaat.",
                  "Je deelt de massa per liter door de molaire massa. Zo zet je gram om in mol en houd je "
                  "het volume gelijk.", 4),
             ]),
        dict(kop="Verdunnen",
             opdracht="Reken uit met c₁V₁ = c₂V₂.",
             oefeningen=[
                 ("rij", [(r"\(100\) mL van \(0{,}500\) mol/L tot \(500\) mL", r"\(0{,}100\) mol/L"),
                          (r"\(10{,}0\) mL van \(2{,}00\) mol/L tot \(250\) mL", r"\(0{,}0800\) mol/L")],
                  "Nieuwe concentratie?", WL),
                 ("open", r"Je hebt \(250\) mL van \(0{,}200\) mol/L nodig en je voorraad is \(2{,}00\) mol/L. Hoeveel neem "
                          "je uit de voorraad, en wat doe je daarna?",
                  r"V₁ = \(0{,}200 \cdot 250 : 2{,}00\), dus \(25{,}0\) mL. Die giet je in een maatkolf van "
                  r"\(250\) mL en vul je aan met water tot aan het streepje.", 6),
                 ("waar", "Bij het verdunnen blijft het aantal mol opgeloste stof gelijk.", True),
                 ("waar", "De molaire concentratie stijgt als je water toevoegt.", False),
             ]),
        dict(kop="Stoichiometrie",
             opdracht="Reken uit of leg uit.",
             oefeningen=[
                 ("rij", [(r"N₂ + 3 H₂ → 2 NH₃, met \(6{,}00\) mol H₂", r"\(4{,}00\) mol NH₃"),
                          (r"2 H₂ + O₂ → 2 H₂O, met \(3{,}00\) mol O₂", r"\(6{,}00\) mol H₂O")],
                  "Hoeveel product?", WL),
                 ("open", "Waarom mag je de coëfficiënten niet als een verhouding in gram gebruiken?",
                  "De coëfficiënten tellen deeltjes, dus mol. Eén mol van de ene stof weegt niet evenveel "
                  "als één mol van de andere, dus moet je eerst naar mol rekenen.", 5),
                 ("open", "Wat is een beperkend reagens, en wat gebeurt er met de andere stof?",
                  "Het beperkende reagens is het reagens dat als eerste opgebruikt is; het bepaalt hoeveel "
                  "product er maximaal kan ontstaan. De andere stof blijft in overmaat over.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meten-en-onderzoek-chemie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Veilig werken, meten en onderzoek",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De pictogrammen",
             opdracht="Schrijf welk pictogram erbij hoort.",
             oefeningen=[
                 ("rij", [("veroorzaakt brandwonden", "bijtend of corrosief"),
                          ("kan een brand verergeren", "oxiderend"),
                          ("kankerverwekkend of orgaanschade", "langetermijngevaar")],
                  "Welk pictogram?", WL),
                 ("rij", [("de fles is gevaarlijk bij warmte of stoten", "gassen onder druk"),
                          ("schadelijk voor het water en wat erin leeft", "aquatisch milieu")],
                  "Welk pictogram?", WL),
                 ("rij", [("H-zinnen", "benoemen het gevaar"),
                          ("P-zinnen", "geven de voorzorgen")], "Waarvoor dienen ze?", WL),
             ]),
        dict(kop="Goed of slecht gewerkt?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een gemorst product kuis je onmiddellijk op.", True),
                 ("waar", "Een onbekende stof mag je voorzichtig ruiken om ze te herkennen.", False),
                 ("waar", r"Je belast een balans van \(200\) g niet met een kilo.", True),
                 ("waar", "Chemisch afval mag in de gootsteen zolang je veel water laat lopen.", False),
                 ("waar", "Glasscherven veeg je met de hand bij elkaar.", False),
             ]),
        dict(kop="Welk materiaal?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [(r"precies \(25{,}0\) mL afmeten", "een volpipet"),
                          (r"een oplossing tot \(250\) mL aanvullen", "een maatkolf"),
                          ("zwenken zonder te morsen", "een erlenmeyer")], "Welk materiaal?", WL),
                 ("rij", [("een vaste stof fijnmaken", "mortier en stamper"),
                          ("twee vloeistoflagen scheiden", "een scheitrechter"),
                          ("damp weer vloeibaar maken", "een liebigkoeler")], "Welk materiaal?", WL),
                 ("open", r"Je moet ongeveer \(80\) mL water afmeten. Je hebt een maatcilinder van \(100\) mL en "
                          r"een van \(1\) L. Welke kies je, en waarom?",
                  r"Die van \(100\) mL. Het meetbereik ligt net boven je volume, dus is de schaalverdeling "
                  "fijner en lees je nauwkeuriger af. Een grote cilinder leest veel grover af.", 5),
                 ("open", "Hoe lees je het volume in een maatcilinder correct af?",
                  "Op ooghoogte, onderaan de holle vloeistofspiegel, de meniscus. Zo maak je geen "
                  "kijkfout.", 4),
             ]),
        dict(kop="Eenheden en voorvoegsels",
             opdracht="Reken om of vul aan.",
             oefeningen=[
                 ("rij", [(r"\(4{,}5\) mg in g", r"\(0{,}0045\) g"), (r"\(0{,}25\) L in mL", r"\(250\) mL"),
                          (r"\(1500\) g in kg", r"\(1{,}5\) kg")], "Hoeveel?", WW),
                 ("rij", [("kilo", r"\(10^{3}\)"), ("micro", r"\(10^{-6}\)"), ("nano", r"\(10^{-9}\)")], "Welke waarde?", W),
                 ("rij", [("de SI-eenheid van volume", "de kubieke meter"),
                          ("de SI-eenheid van massa", "de kilogram"),
                          ("de SI-eenheid van absolute temperatuur", "de kelvin")],
                  "Welke eenheid?", WL),
             ]),
        dict(kop="Beduidende cijfers en notatie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [(r"\(0{,}00250\)", r"\(3\)"), (r"\(12{,}0\)", r"\(3\)"), (r"\(1200\)", r"\(2\)")],
                  "Hoeveel beduidende cijfers?", W),
                 ("rij", [(r"\(0{,}00072\)", r"\(7{,}2 \cdot 10^{-4}\)"), (r"\(45600\)", r"\(4{,}56 \cdot 10^{4}\)")],
                  "In wetenschappelijke notatie?", WW),
                 ("open", "Waarom mag je bij een berekening niet meer beduidende cijfers opschrijven dan "
                          "je gegevens hebben?",
                  "Een meting is nooit exact, dus je antwoord mag niet nauwkeuriger lijken dan de "
                  "metingen waarop het steunt.", 4),
             ]),
        dict(kop="De onderzoeksmethode",
             opdracht="Schrijf of leg uit.",
             oefeningen=[
                 ("open", "Noem de stappen van een wetenschappelijk onderzoek, in de juiste orde.",
                  "Het probleem definiëren en afbakenen, een onderzoeksvraag opstellen en een hypothese "
                  "formuleren, een onderzoeksplan opstellen, data verzamelen, de data analyseren, "
                  "conclusies trekken, en over je methode en resultaten reflecteren en communiceren.", 8),
                 ("rij", [("ze gaat over één onderwerp", "enkelvoudig"),
                          ("ze laat geen mening doorschemeren", "objectief"),
                          ("ze is geen opzoekvraag", "onderzoekbaar")], "Welk criterium?", WW),
                 ("open", "Een leerling stelt als onderzoeksvraag: welk ontkalkingsmiddel is het beste? "
                          "Wat is daar het probleem mee, en hoe herformuleer je ze?",
                  "De vraag is niet objectief en niet enkelvoudig: het beste legt een oordeel vast en kan "
                  "over prijs, snelheid of veiligheid gaan. Beter: hoeveel kalk lost elk middel op in "
                  "tien minuten bij dezelfde temperatuur?", 7),
                 ("waar", "Een weerlegde hypothese betekent dat je onderzoek mislukt is.", False),
                 ("kort", "Voor welke discipline staat de M in STEM?", "wiskunde", WW),
             ]),
    ],
)


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-mengsels-zuivere-stoffen-en-scheidingstechnieken-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Twee vragen na elkaar: zit er meer dan één stof in, en kan je de bestanddelen nog "
                    "onderscheiden. Dat geeft de drie mogelijkheden.",
             waarom=[
                 "Messing is een legering en dus homogeen, al is het vast. Een legering is nooit een "
                 "zuivere stof.",
                 "Vinaigrette die schift, toont zijn twee lagen. Pas geschud lijkt het homogeen, maar dat "
                 "is het niet.",
             ]),
        dict(aanpak="Het soort mengsel volgt uit de twee fasen: wat zit er in wat. Vast in vloeibaar is een "
                    "suspensie, vloeibaar in vloeibaar een emulsie, gas in vloeibaar een schuim.",
             waarom=[
                 "Een aerosol is vast of vloeibaar fijn verdeeld in een gas. Nevel, rook en haarlak horen "
                 "alle drie in die groep.",
                 None,
             ]),
        dict(aanpak="Een stofeigenschap hangt niet af van hoeveel je hebt. Massa en volume van je staal "
                    "dus niet.",
             waarom=[None, None, None, None]),
        dict(aanpak="Kies de techniek op het verschil dat je kan gebruiken: deeltjesgrootte, kookpunt, "
                    "massadichtheid of oplosbaarheid.",
             waarom=[
                 "Centrifugeren is filtreren op snelheid: de zwaarste deeltjes worden naar buiten geduwd. "
                 "Het werkt waar een filter te grof is.",
                 None,
                 "Dit is de kern van elke keuze: een techniek werkt alleen als er een verschil is om op te "
                 "werken. Opgeloste ionen zijn even klein als de watermoleculen.",
             ]),
        dict(aanpak="Bij een destillatie werk je met een verschil in kookpunt. Vraag je altijd eerst af of "
                    "de vloeistoffen wel mengen.",
             waarom=[
                 None,
                 "Destilleren kost veel warmte en tijd. Als de lagen al gescheiden zijn, is decanteren "
                 "eenvoudiger en goedkoper.",
                 "Dit is ook de proef waarmee je een mengsel van een zuivere stof onderscheidt: één punt "
                 "tegenover een traject.",
             ]),
        dict(aanpak="Twee woorden vastleggen: residu blijft op het filter, filtraat loopt erdoor. Daarna "
                    "kan je elke labovraag lezen.",
             waarom=[
                 None, None,
                 "Noem bij elke techniek het verschil waarop ze werkt. Dat is wat deze vraag echt toetst, "
                 "niet de namen.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-enkelvoudige-en-samengestelde-stoffen-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De symbolen die niet op de Nederlandse naam lijken, komen uit het Latijn. Juist die "
                    "zijn het waard apart te leren.",
             waarom=[
                 "Pb komt van plumbum, Sn van stannum en Hg van hydrargyrum. Geen van de drie lijkt op de "
                 "Nederlandse naam.",
                 None, None,
             ]),
        dict(aanpak="Lees een formule van buiten naar binnen: eerst de coëfficiënt, dan de haakjes, dan de "
                    "indexen erin.",
             waarom=[
                 "De index achter de haakjes geldt voor alles erin. Daarom zitten er twaalf zuurstofatomen "
                 "per deeltje en niet vier.",
                 "Vergeet de coëfficiënt niet: bij 2 NH₃ tel je eerst vier atomen per deeltje en "
                 "vermenigvuldig je dan met twee.",
             ]),
        dict(aanpak="Tel het aantal verschillende elementen, niet het aantal atomen. Eén soort betekent "
                    "enkelvoudig.",
             waarom=[
                 "S₈ bestaat uit acht zwavelatomen, maar wel uit één soort. Daarom is het enkelvoudig.",
                 None, None, None,
             ]),
        dict(aanpak="Metalen staan links en in het midden, niet-metalen rechtsboven, de edelgassen in de "
                    "laatste kolom.",
             waarom=[
                 "Br is broom, een niet-metaal, en bij kamertemperatuur vloeibaar. Niet elk vloeibaar "
                 "element is dus kwik.",
                 "Verbind alle drie de eigenschappen met de vrije elektronen. Ze los opsommen levert minder "
                 "op dan ze uit één oorzaak afleiden.",
                 None,
             ]),
        dict(aanpak="Zet bij elke stof één kenmerk of één gebruik. Daarmee herken je ze in een vraag.",
             waarom=[
                 "Helium werd gekozen omdat het niet brandbaar is. Waterstofgas is lichter maar "
                 "levensgevaarlijk in een ballon.",
                 "Dit heet allotropie: dezelfde atomen, een andere structuur. Leg de verschillen altijd uit "
                 "de bouw uit, niet uit de stof.",
                 None,
             ]),
        dict(aanpak="Analyse breekt af, synthese bouwt op. Vraag je af of er stoffen samenkomen of uit "
                    "elkaar gaan.",
             waarom=[
                 None,
                 "Analyse is net het omgekeerde: één stof valt uiteen in meerdere. Het woord betekent "
                 "ontleden.",
                 "Dit onderscheid komt terug bij elk zout. In een ionrooster bestaat er geen molecule, "
                 "enkel een verhouding.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-chemische-reacties-en-energie-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Tel links en rechts per atoomsoort. Begin met het element dat in maar één stof aan "
                    "elke kant voorkomt, en doe zuurstof het laatst.",
             waarom=[
                 None,
                 r"Bij een verbranding van een koolwaterstof ga je altijd in dezelfde orde: eerst koolstof, "
                 r"dan waterstof, dan zuurstof. Zo kom je op \(1\), \(5\), \(3\), \(4\).",
             ]),
        dict(aanpak="De wet van behoud van massa geldt altijd. Weegt het meer of minder, dan is er iets uit "
                    "de lucht bij gekomen of als gas ontsnapt.",
             waarom=[
                 None,
                 "Dit is de klassieke proef: staalwol wordt zwaarder omdat de zuurstof mee in de vaste stof "
                 "gaat zitten. Niets komt uit het niets.",
                 "Hier gaat er net massa weg als gas. Dezelfde wet, een tegengestelde meting: alles hangt "
                 "af van wat er in of uit het vat kan.",
             ]),
        dict(aanpak="Een chemische reactie maakt nieuwe stoffen. Verandert er enkel het uitzicht, dan is "
                    "het geen reactie.",
             waarom=[
                 None,
                 "Troebel water is een suspensie, dus een mengsel. Er ontstaat geen nieuwe stof.",
                 None,
                 "Atomen worden herschikt, niet omgezet in andere elementen. Daarvoor zou je een "
                 "kernreactie nodig hebben.",
             ]),
        dict(aanpak="Exo geeft energie af, endo neemt op. Let op dat je redeneert vanuit de reactie en niet "
                    "vanuit je hand.",
             waarom=[
                 None,
                 "Een handwarmer voelt warm omdat de reactie energie afgeeft; een koudepakje voelt koud "
                 "omdat ze energie opneemt. Je hand meet telkens het omgekeerde van wat de stof doet.",
                 "De beker koelt af, dus de reactie haalde energie uit de omgeving. Dat is wat endo "
                 "betekent.",
             ]),
        dict(aanpak="Op de verticale as staat de inwendige energie. Of de producten hoger of lager liggen, "
                    "zegt of de reactie exo of endo is.",
             waarom=[
                 None,
                 "Beschrijf altijd beide uiteinden én het hoogteverschil. Dat hoogteverschil is de "
                 "reactie-energie, en het teken zegt welke soort reactie het is.",
             ]),
        dict(aanpak="Schrijf een omzetting altijd als van-naar. Zo zie je meteen of je de twee vormen juist "
                    "benoemd hebt.",
             waarom=[
                 "Let op de laatste: bij het opladen gaat het van elektrisch naar chemisch, bij het "
                 "gebruiken net omgekeerd.",
                 "Hier komt het energiediagram terug: het verschil tussen de bindingen van begin en eind is "
                 "precies de reactie-energie.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-de-bouw-van-atomen-en-ionen-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Drie deeltjes, drie dingen om van elk te weten: waar het zit, welke lading het heeft "
                    "en of het meetelt voor de massa.",
             waarom=[
                 None,
                 "Een elektron is bijna tweeduizend keer lichter dan een proton. Daarom reken je het "
                 "gewicht van een atoom nooit met de elektronen mee.",
                 None,
             ]),
        dict(aanpak="Protonen lees je uit het atoomnummer, neutronen uit massagetal min atoomnummer. Het "
                    "aantal elektronen is enkel bij een átoom gelijk aan het aantal protonen; bij een ion "
                    "verschuift het met de lading.",
             waarom=[
                 "Let op de twee ionen: het zwavelion heeft er twee te veel en het aluminiumion drie te "
                 "weinig. De kern blijft bij beide ongemoeid.",
                 None,
             ]),
        dict(aanpak="Elke uitspraak gaat over één van de drie getallen. Vraag je telkens af of het over de "
                    "kern of over de schillen gaat.",
             waarom=[
                 None,
                 "Een atoom geeft bij een ion altijd elektronen af of neemt ze op; aan de protonen raakt "
                 "het niet. Veranderen de protonen wel, dan is het een ander element.",
                 None,
                 "Het massagetal telt protonen en neutronen, dus enkel wat in de kern zit. De elektronen "
                 "wegen te weinig om mee te tellen.",
             ]),
        dict(aanpak="De relatieve atoommassa zegt hoeveel keer zwaarder een atoom is dan één u. Wil je "
                    "kilogram, dan vermenigvuldig je met de waarde van u.",
             waarom=[
                 None,
                 "Dit onderscheid komt later terug bij elke molberekening: hetzelfde getal, de ene keer "
                 "zonder eenheid, de andere keer in gram per mol.",
             ]),
        dict(aanpak="Vul de schillen van binnen naar buiten: twee, dan acht, dan acht. Het atoomnummer zegt "
                    "hoeveel elektronen je moet verdelen.",
             waarom=[
                 None, None,
                 "Dit is de regel achter alle ionen: een atoom gaat naar de edelgasconfiguratie langs de "
                 "kortste weg. Daarom geven metalen af en nemen niet-metalen op.",
                 None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-het-periodiek-systeem-der-elementen-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De configuratie zegt het allemaal: het aantal bezette schillen is de periode, het "
                    "aantal elektronen op de buitenste schil de hoofdgroep.",
             waarom=[
                 None,
                 "Oefen die twee stappen tot ze vlot gaan. Met de groep en de periode kan je daarna het ion "
                 "en de eigenschappen voorspellen.",
             ]),
        dict(aanpak="Vier namen om vast te leggen: alkalimetalen, aardalkalimetalen, halogenen, edelgassen. "
                    "Ze horen bij groep IA, IIA, VIIA en de laatste.",
             waarom=[
                 None, None,
                 "Waterstof staat wel boven groep IA, maar is een gas en geen metaal. Het is het buitenbeentje "
                 "van het systeem.",
                 None,
             ]),
        dict(aanpak="Werk in twee stappen: hoeveel valentie-elektronen heeft het, en is afgeven of opnemen "
                    "de kortste weg naar acht.",
             waarom=[
                 None, None,
                 "Bij de hoofdgroepen is de lading voorspelbaar uit het groepsnummer. Dat spaart je het "
                 "vanbuiten leren van de ionen apart.",
             ]),
        dict(aanpak="Elektronegativiteit is hoe hard een atoom aan de elektronen van een binding trekt. Ze "
                    "stijgt naar rechts en naar boven.",
             waarom=[
                 None,
                 "Naar onder dáált ze juist: let op de richting, want dit is de helft van de vragen die "
                 "hierover fout gaan.",
                 None, None,
                 "Fluor staat daar, met de hoogste waarde van alle elementen. De edelgassen laat men buiten "
                 "beschouwing, want die vormen bijna geen bindingen.",
             ]),
        dict(aanpak="Metaal of niet-metaal volgt uit wat het met elektronen doet. Dat bepaalt op zijn beurt "
                    "het bindingstype.",
             waarom=[
                 None,
                 "Dit is een vraag die vaak misloopt: dezelfde elektronenconfiguratie maakt geen gelijke "
                 "stof. Het is de kern die zegt welk element je in handen hebt.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-chemische-bindingen-en-roosters-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Kijk naar het soort elementen: metaal met niet-metaal geeft een ionbinding, twee "
                    "niet-metalen een atoombinding, twee metalen een metaalbinding.",
             waarom=[None, None]),
        dict(aanpak="Ga langs de ionen: welke lading vormt elk, en hoeveel heb je er nodig om samen op nul "
                    "uit te komen. Die aantallen zijn de indexen.",
             waarom=[
                 None,
                 "Hier kruisen de ladingen: Mg²⁺ met N³⁻ geeft drie magnesium tegen twee stikstof. Het "
                 "geheel moet neutraal zijn.",
                 "Schrijf die drie stappen altijd uit: lading, lading, opheffen. Zo heb je geen formules "
                 "nodig die je vanbuiten kent.",
             ]),
        dict(aanpak="Een bindend paar ligt tussen twee atomen, een vrij paar hoort bij één atoom. Tel in "
                    "een Lewisstructuur altijd de paren en niet de losse elektronen.",
             waarom=[
                 None, None,
                 "Een dubbele binding is twee páren, dus vier elektronen. Juist daarom spreekt men van "
                 "elektronenparen en niet van elektronen.",
                 None,
             ]),
        dict(aanpak="Vier roosters, en bij elk hangen de eigenschappen aan wat er op de plaatsen zit: "
                    "ionen, atomen, moleculen of een metaalrooster met vrije elektronen.",
             waarom=[
                 "Alleen koper geleidt in vaste toestand, want alleen daar zijn de elektronen vrij. "
                 "Geleiden vraagt altijd ladingen die kunnen bewegen.",
                 None,
                 "Dit is het mooiste voorbeeld van bouw die gedrag verklaart: hetzelfde duwtje breekt het "
                 "ene rooster en vervormt het andere alleen maar.",
             ]),
        dict(aanpak="Vaste afspraken: zuurstof is meestal −II, waterstof +I, een enkelvoudige stof nul, en "
                    "de som in een neutrale stof is nul. Daarmee reken je de rest uit.",
             waarom=[
                 "IJzer vind je door de som: twee keer x plus drie keer −II moet nul geven, dus x is +III. "
                 "Reken het altijd zo na in plaats van te gokken.",
                 None, None,
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-anorganische-stofklassen-en-naamgeving-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Lees de formule van voor naar achter. Begint ze met H, dan is het een zuur; eindigt ze "
                    "op OH, dan een hydroxide; staat er enkel een metaal en zuurstof, dan een oxide; alle "
                    "andere combinaties van een metaal met een zuurrest zijn zouten. Binair betekent twee "
                    "elementen, ternair drie.",
             waarom=[
                 None, None,
                 "Water begint wel met H, maar geeft geen H⁺ af in een oplossing. Het is de uitzondering "
                 "die je apart moet kennen.",
                 "Een binair zout zoals MgCl₂ heeft geen zuurstof. Enkel de ternaire zouten hebben een "
                 "zuurrest met zuurstof erin.",
             ]),
        dict(aanpak="De zuurresten zijn een lijstje dat je echt moet kennen. Let op lading én uitgang, want "
                    "de uitgang verraadt of er zuurstof in zit.",
             waarom=[
                 None, None,
                 "Die regel spaart je het halve lijstje: hoor je -aat, dan weet je al dat er zuurstof in "
                 "zit, en hoor je -ide, dan niet.",
             ]),
        dict(aanpak="Zelfde werkwijze als bij een binair zout: zoek de twee ladingen en zorg dat ze elkaar "
                    "opheffen. Een zuurrest met meer dan één atoom zet je tussen haakjes.",
             waarom=[
                 "Bij calciumfosfaat heb je drie Ca²⁺ tegen twee PO₄³⁻ nodig, en dan zijn de haakjes "
                 "verplicht: Ca₃(PO₄)₂.",
                 None,
             ]),
        dict(aanpak="Twee stelsels naast elkaar. Bij twee niet-metalen gebruik je Griekse telwoorden, bij "
                    "een metaal met meerdere oxidatiegetallen een Romeins cijfer.",
             waarom=[
                 None,
                 "Dit is de vuistregel: enkel waar er iets te kiezen valt, moet het cijfer erbij. Bij "
                 "calcium, natrium of kalium valt er niets te kiezen.",
                 "Bij een ionverbinding zeggen de ladingen al hoeveel ionen er zijn, dus zijn telwoorden "
                 "overbodig. Die horen bij de niet-metaaloxiden.",
             ]),
        dict(aanpak="De triviale namen zijn de namen uit de winkel en het labo. Leer er telkens de formule "
                    "én waar je de stof tegenkomt bij.",
             waarom=[
                 None, None,
                 "Eén letter verschil in de formule geeft een heel andere stof. NaOH is bijtend, NaHCO₃ zit "
                 "in je keukenkast.",
             ]),
        dict(aanpak="Vier patronen die telkens terugkeren: metaaloxide met water, niet-metaaloxide met "
                    "water, zuur met hydroxide, en een zout dat oplost.",
             waarom=[
                 None,
                 "Hiermee kan je van een onbekend oxide al voorspellen of de oplossing zuur of basisch "
                 "wordt, enkel uit de plaats van het element in het periodiek systeem.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-organische-stoffen-en-de-alkanen-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="De eerste tien namen van de alkanen zijn de basis van heel de organische chemie. "
                    "Ken je het aantal koolstofatomen, dan volgt de formule uit CnH\\(2n+2\\).",
             waarom=[
                 None, None,
                 "Reken die regel één keer na op een getekende keten. Dan hoef je de formules niet meer "
                 "vanbuiten te leren.",
             ]),
        dict(aanpak="De uitgang van de naam zegt de stofklasse: -aan, -een, -yn, -ol of -zuur. De "
                    "functionele groep hoort daarbij.",
             waarom=[None, None, None]),
        dict(aanpak="De eigenschappen van een organische stof volgen uit twee dingen: de lengte van de "
                    "keten en de functionele groep.",
             waarom=[
                 "Een alkaan is apolair en water polair, dus mengen ze niet. Daarom ligt benzine op water.",
                 None,
                 "Die OH zit vast in de molecule en komt niet los als OH⁻. Juist daarom is een alcohol "
                 "neutraal en geen base.",
                 None,
             ]),
        dict(aanpak="Zet bij elke triviale naam de IUPAC-naam en één gebruik. Zo herken je de stof hoe ze "
                    "ook genoemd wordt.",
             waarom=[
                 None, None,
                 "Dit is geen bijzaak maar een echt gevaar: methanol zit in ruitensproeivloeistof en in "
                 "zelfgestookte drank.",
             ]),
        dict(aanpak="Elke verbranding van een koolwaterstof geeft koolstofdioxide en water. Maak kloppend "
                    "in de orde koolstof, waterstof, zuurstof.",
             waarom=[
                 "Bij ethaan kom je op halve getallen uit, dus verdubbel je alles: \\(2\\), \\(7\\), \\(4\\) "
                 "en \\(6\\).",
                 "Onthoud vooral het tweede deel. Een koolstofmonoxidevergiftiging merk je niet, en dat is "
                 "net waarom een geiser gekeurd moet zijn.",
                 "Hier verklaart een fysische eigenschap een dagelijkse keuze. Dat is wat organische chemie "
                 "nuttig maakt.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-stoffen-in-water-polariteit-oplossen-en-ph-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Twee vragen na elkaar: zijn de bindingen polair, en is de molecule symmetrisch. Pas "
                    "als het antwoord ja en nee is, is de molecule als geheel polair.",
             waarom=[
                 None,
                 "CCl₄ heeft wel polaire bindingen, maar ze staan symmetrisch rond de koolstof en heffen "
                 "elkaar op.",
                 None, None,
             ]),
        dict(aanpak="Drie krachten, van sterk naar zwak: ion-dipool, waterstofbrug, londonkracht. Welke er "
                    "speelt, volgt uit wat er naast elkaar ligt.",
             waarom=[
                 "Een waterstofbrug vraagt H aan O, N of F. Daarom hebben hexaanmoleculen er geen en water "
                 "wel.",
                 None, None,
             ]),
        dict(aanpak="Gelijk lost op in gelijk: polair in polair, apolair in apolair. Zeg bij je antwoord "
                    "altijd welke van de twee je bedoelt.",
             waarom=[
                 None,
                 "Dit is dezelfde regel toegepast op een alledaags probleem. Daarom zit er zeep tussen: die "
                 "heeft een polaire én een apolaire kant.",
             ]),
        dict(aanpak="Een zout dissocieert, een polaire molecule ioniseert. Let bij het schrijven op de "
                    "coëfficiënt vóór het ion dat twee keer voorkomt.",
             waarom=[
                 "Bij MgCl₂ moet er een 2 voor Cl¹⁻ staan, want er komen twee chloride-ionen vrij per "
                 "formule-eenheid.",
                 None,
                 "Suiker lost wel op maar valt niet in ionen uiteen, dus geleidt de oplossing niet. "
                 "Oplossen en ioniseren zijn twee verschillende dingen.",
                 None,
             ]),
        dict(aanpak="Onder zeven is zuur, zeven is neutraal, boven zeven basisch. Een indicator geeft maar "
                    "een gebied aan, geen getal.",
             waarom=[
                 "Let op pH \\(7\\) bij lakmoes: daar ligt het omslagpunt, dus geeft het papier geen "
                 "duidelijke uitslag.",
                 None, None,
                 "Een indicator zegt enkel zuur of basisch; wil je het getal, dan heb je het toestel nodig.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-neerslag-gas-neutralisatie-en-redoxreacties-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Werk met de vuistregels: nitraten, kaliumzouten, natriumzouten en ammoniumzouten "
                    "lossen altijd goed op. De vaste klanten aan de andere kant zijn AgCl, BaSO₄ en CaCO₃.",
             waarom=[
                 None,
                 "Let op het paar carbonaten: K₂CO₃ lost op omdat het een kaliumzout is, CaCO₃ niet. De "
                 "kalksteen in je waterketel is daar het bewijs van.",
             ]),
        dict(aanpak="Zoek telkens welk paar ionen samenkomt. Vormen ze een slecht oplosbaar zout, dan is "
                    "het een neerslag; een gas, dan gasontwikkeling; H⁺ met OH⁻, dan een neutralisatie.",
             waarom=[None, None]),
        dict(aanpak="Schrijf eerst alle ionen los op, streep dan weg wat links en rechts hetzelfde is. Wat "
                    "overblijft is de essentiële vergelijking.",
             waarom=[
                 None, None,
                 "Dit is de hele reden waarom je de essentiële vergelijking schrijft: ze laat zien wat er "
                 "echt gebeurt, zonder de ionen die enkel toekijken.",
             ]),
        dict(aanpak="Drie gassen die je uit het patroon kan voorspellen: CO₂ uit een carbonaat, H₂S uit een "
                    "sulfide, NH₃ uit een ammoniumzout met een sterke base.",
             waarom=[
                 "Je ruikt ze ook aan elkaar af: H₂S naar rotte eieren, ammoniak scherp. CO₂ heeft geen "
                 "geur.",
                 None,
             ]),
        dict(aanpak="Twee woorden en vier gevolgen: oxidatie is afgeven en het getal stijgt, reductie is "
                    "opnemen en het getal daalt. Wie oxideert wordt zelf gereduceerd.",
             waarom=[
                 "De namen zitten omgekeerd aan wat je zou denken: de reductor ondergáát de oxidatie. Reken "
                 "altijd met de oxidatiegetallen en niet met de namen.",
                 None,
                 "Deze proef kan je echt zien gebeuren: de kleur verdwijnt en er komt koper op het zink. "
                 "Elektronenoverdracht is dus niet enkel een berekening.",
             ]),
        dict(aanpak="Eén toets volstaat: veranderen er oxidatiegetallen, dan is het redox. Wisselen de "
                    "ionen enkel van partner, dan niet.",
             waarom=[
                 None,
                 "Bij een neerslag veranderen alleen de partners; de ionen houden hun lading. Daarom is dat "
                 "geen redox.",
                 None, None,
             ]),
        dict(aanpak="Herken het patroon in plaats van elke reactie te leren: een element met zuurstof geeft "
                    "een oxide, en een koolwaterstof of alcohol geeft koolstofdioxide en water.",
             waarom=[
                 None, None,
                 "Dit verklaart waarom een aluminium ladder niet wegrot en een ijzeren hek wel. Een "
                 "oxidelaag kan beschermen of juist niet, en dat hangt af van hoe ze blijft zitten.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-rekenen-met-mol-massa-en-concentratie-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Tel de atoommassa's op, met elke index als vermenigvuldiger. Hou dezelfde cijfers na "
                    "de komma als je gegevens.",
             waarom=[None, None]),
        dict(aanpak="Twee formules die elkaars omgekeerde zijn: n = m : M en m = n · M. Zet er altijd de "
                    "eenheid bij, dan merk je zelf of je moest delen of vermenigvuldigen.",
             waarom=[
                 None, None,
                 "Zo'n controle op de grootteorde is de snelste manier om een rekenfout te vinden: is het "
                 "antwoord plausibel groter of kleiner dan één mol.",
             ]),
        dict(aanpak="Eén mol is altijd \\(6{,}02 \\cdot 10^{23}\\) deeltjes, welke stof het ook is. Van mol "
                    "naar deeltjes vermenigvuldig je, omgekeerd deel je.",
             waarom=[
                 None, None,
                 "Evenveel deeltjes betekent niet dezelfde massa: water weegt \\(18{,}0\\) g per mol en "
                 "koolstofdioxide \\(44{,}0\\) g. Dat verschil is net waarom de molaire massa bestaat.",
             ]),
        dict(aanpak="Concentratie is mol per liter: c = n : V. Zet milliliter eerst om in liter, anders zit "
                    "je er duizend keer naast.",
             waarom=[
                 "Bij \\(200\\) mL reken je met \\(0{,}200\\) L. Dat is de fout die hier het vaakst gemaakt "
                 "wordt.",
                 None, None,
             ]),
        dict(aanpak="Bij verdunnen blijft het aantal mol gelijk, dus geldt c₁V₁ = c₂V₂. Je zoekt bijna "
                    "altijd V₁: hoeveel je uit de voorraad neemt.",
             waarom=[
                 None,
                 "Let op de laatste stap: je vult aan tót het streepje, je giet geen \\(225\\) mL water "
                 "bij. Het eindvolume moet kloppen, niet het toegevoegde water.",
                 None,
                 "De concentratie dáált: evenveel mol in meer liter. Dat is precies wat de formule zegt.",
             ]),
        dict(aanpak="De coëfficiënten van een kloppende vergelijking zijn een verhouding in mol. Reken dus "
                    "altijd eerst naar mol, dan met de verhouding, dan terug naar gram.",
             waarom=[
                 "Let op de tweede: drie mol zuurstof geeft zes mol water, want de verhouding is één tegen "
                 "twee.",
                 None,
                 "Dit komt in elk vraagstuk terug: reken allebei de stoffen naar mol en kijk welke eerst "
                 "op is. Die bepaalt de opbrengst.",
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-werken-meten-en-onderzoek-chemie-boost-doorstroom"] = dict(
    reeksen=[
        dict(aanpak="Een pictogram zegt het soort gevaar, de H- en P-zinnen zeggen wat en wat je ermee "
                    "doet. Lees ze altijd samen.",
             waarom=[
                 None, None,
                 "H staat voor hazard en P voor precaution. Weet je dat, dan hoef je de twee niet te "
                 "verwarren.",
             ]),
        dict(aanpak="Elke regel heeft een reden. Vraag je bij een uitspraak af wat er in het slechtste "
                    "geval gebeurt.",
             waarom=[
                 None,
                 "Ruiken aan een onbekende stof kan je luchtwegen aantasten. Wie toch moet ruiken, wappert "
                 "de damp voorzichtig naar zich toe en buigt zich nooit over de opening.",
                 None,
                 "Veel producten horen niet in het water terecht. Verdunnen verandert daar niets aan, zie "
                 "het pictogram voor het aquatisch milieu.",
                 "Gebruik een borstel en een blik. Een scherf glas gaat makkelijk door een handschoen.",
             ]),
        dict(aanpak="Kies het materiaal naar wat je nodig hebt: nauwkeurig afmeten, een volume aanvullen, "
                    "of enkel mengen en opvangen.",
             waarom=[
                 "Een volpipet en een maatkolf zijn gemaakt voor één volume en dus nauwkeurig. Een bekerglas "
                 "en een erlenmeyer dienen om in te werken, niet om in af te meten.",
                 None,
                 "Dit is de vuistregel bij elke meting: kies het bereik dat net boven je waarde ligt. Dan "
                 "gebruik je de hele schaal.",
                 None,
             ]),
        dict(aanpak="Zet de voorvoegsels als machten van tien op een rij. Dan is omrekenen enkel de komma "
                    "verschuiven.",
             waarom=[None, None, None]),
        dict(aanpak="Beduidende cijfers tellen hoe nauwkeurig je meting was. Een nul vóór het eerste cijfer "
                    "telt niet mee, een nul erna wel.",
             waarom=[
                 "Let op het verschil tussen \\(12{,}0\\) en \\(1200\\): die laatste nullen zijn niet "
                 "gemeten, dus tellen ze niet mee.",
                 None,
                 "Daarom is afronden geen slordigheid maar juist eerlijk: je antwoord zegt zelf hoe zeker "
                 "je bent.",
             ]),
        dict(aanpak="Een goede onderzoeksvraag is enkelvoudig, objectief en onderzoekbaar. Pas daarna "
                    "formuleer je een hypothese en bedenk je een plan.",
             waarom=[
                 None, None,
                 "Het woord beste is in een onderzoeksvraag bijna altijd een alarmbel. Vervang het door een "
                 "eigenschap die je kan meten.",
                 "Een weerlegde hypothese is een resultaat, geen mislukking. Je weet nu iets wat je ervoor "
                 "niet wist.",
                 None,
             ]),
    ],
)
