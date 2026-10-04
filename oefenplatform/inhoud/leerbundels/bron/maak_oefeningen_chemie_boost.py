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
             opdracht="Vul de tabel aan voor 3 Al₂(SO₄)₃.",
             oefeningen=[
                 ("tabel", ["", "Antwoord"],
                  [["de coëfficiënt", None], ["het aantal verschillende elementen", None],
                   ["het aantal aluminiumatomen in één formule-eenheid", None],
                   ["het aantal zuurstofatomen in één formule-eenheid", None],
                   ["enkelvoudig of samengesteld", None]],
                  "Coëfficiënt 3; drie elementen (Al, S, O); twee aluminiumatomen; twaalf zuurstofatomen "
                  "(3 maal 4); samengesteld.", WW),
                 ("rij", [("H₂O₂", "4"), ("2 NH₃", "8"), ("CaCl₂", "3")],
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
                 ("rij", [("... N₂ + ... H₂ → ... NH₃", "1, 3 en 2"),
                          ("... Mg + ... O₂ → ... MgO", "2, 1 en 2"),
                          ("... Al + ... Cl₂ → ... AlCl₃", "2, 3 en 2")], "Welke coëfficiënten?", WL),
                 ("rij", [("... C₃H₈ + ... O₂ → ... CO₂ + ... H₂O", "1, 5, 3 en 4"),
                          ("... H₂O₂ → ... H₂O + ... O₂", "2, 2 en 1")], "Welke coëfficiënten?", WL),
             ]),
        dict(kop="Rekenen met de wet van behoud van massa",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("12 g koolstof reageert volledig met 32 g zuurstofgas", "44 g"),
                          ("24 g magnesium reageert volledig met 16 g zuurstofgas", "40 g")],
                  "Hoeveel product?", WW),
                 ("open", "Een leerling verbrandt 5 g staalwol in een open schaaltje en weegt achteraf "
                          "7 g. Leg uit waarom de massa gestegen is.",
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
                 ("open", "Een leerling meet dat de oplossing in haar beker afkoelt van 21 naar 14 graden. "
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
                  "Proton: in de kern, +1. Neutron: in de kern, 0. Elektron: rond de kern, −1.", WW),
                 ("waar", "Een elektron weegt ongeveer evenveel als een proton.", False),
                 ("waar", "Vrijwel de hele massa van een atoom zit in de kern.", True),
             ]),
        dict(kop="Tellen in de kern",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Atoom of ion", "Protonen", "Neutronen", "Elektronen"],
                  [["Z = 19, A = 39, neutraal", None, None, None],
                   ["Z = 16, A = 32, ion met lading 2−", None, None, None],
                   ["Z = 13, A = 27, ion met lading 3+", None, None, None]],
                  "Kalium: 19 protonen, 20 neutronen, 19 elektronen. Zwavelion: 16 protonen, 16 "
                  "neutronen, 18 elektronen. Aluminiumion: 13 protonen, 14 neutronen, 10 elektronen.", W),
                 ("open", "Een deeltje heeft twintig protonen en achttien elektronen. Welk ion is dat, en "
                          "hoe weet je dat?",
                  "Twintig protonen betekent calcium. Er zijn twee elektronen minder dan protonen, dus is "
                  "de lading 2+: het ion is Ca²⁺.", 5),
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
             opdracht="Reken uit. Gebruik u = 1,66.10⁻²⁷ kg.",
             oefeningen=[
                 ("rij", [("Ar = 32,1 (zwavel)", "5,33.10⁻²⁶ kg"),
                          ("Ar = 23,0 (natrium)", "3,82.10⁻²⁶ kg")],
                  "Absolute massa van één atoom?", WL),
                 ("open", "Waarom heeft de relatieve atoommassa geen eenheid, en de molaire massa wel?",
                  "De relatieve atoommassa is een verhouding tussen twee massa's, dus vallen de eenheden "
                  "weg. De molaire massa is een massa per mol, dus staat ze in gram per mol.", 5),
             ]),
        dict(kop="Elektronenconfiguratie",
             opdracht="Schrijf de configuratie volgens Bohr.",
             oefeningen=[
                 ("rij", [("fluor, Z = 9", "2, 7"), ("silicium, Z = 14", "2, 8, 4"),
                          ("argon, Z = 18", "2, 8, 8")], "Welke configuratie?", WW),
                 ("rij", [("beryllium, Z = 4", "2, 2"), ("fosfor, Z = 15", "2, 8, 5")],
                  "Welke configuratie?", WW),
                 ("open", "Waarom geeft een magnesiumatoom twee elektronen af en neemt het er geen zes op?",
                  "Magnesium heeft de configuratie 2, 8, 2. Geeft het die twee af, dan blijft 2, 8 over, "
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
                  [["lithium, Z = 3", None, None, None], ["zwavel, Z = 16", None, None, None],
                   ["calcium, Z = 20", None, None, None]],
                  "Lithium: 2, 1 — groep IA, periode 2. Zwavel: 2, 8, 6 — groep VIA, periode 3. "
                  "Calcium: 2, 8, 8, 2 — groep IIA, periode 4.", WW),
                 ("open", "Een element heeft de configuratie 2, 8, 7. In welke groep en periode staat het, "
                          "en hoe heet die groep?",
                  "Drie bezette schillen, dus periode 3. Zeven valentie-elektronen, dus groep VIIA, de "
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
                  "edelgasconfiguratie. Het ion krijgt daardoor lading 2−.", 4),
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
                  "Natrium heeft 2, 8, 1 en geeft dat ene elektron af, dus blijft 2, 8 over, net als bij "
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
                  "H₂: enkelvoudig, 1 paar. O₂: dubbel, 2 paren. N₂: drievoudig, 3 paren.", WW),
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
                 ("rij", [("Cl in Cl₂", "0"), ("S in H₂S", "−II"), ("N in NH₃", "−III")],
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
                 ("open", "Leg uit waarom de algemene formule van de n-alkanen CnH2n+2 is.",
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
                 ("rij", [("... CH₄ + ... O₂ → ... CO₂ + ... H₂O", "1, 2, 1 en 2"),
                          ("... C₂H₆ + ... O₂ → ... CO₂ + ... H₂O", "2, 7, 4 en 6")],
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
                 ("kort", "Vanaf welk verschil in elektronegativiteit is een binding polair?", "0,4", W),
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
                          ("MgCl₂ in water", "MgCl₂ → Mg²⁺ + 2 Cl¹⁻"),
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
                  [["pH 2", None, None, None], ["pH 7", None, None, None], ["pH 12", None, None, None]],
                  "pH 2: zuur, kleurloos, rood. pH 7: neutraal, kleurloos, (geen uitslag). "
                  "pH 12: basisch, paars, blauw.", WW),
                 ("open", "Een oplossing is paars met fenolftaleïne. Wat weet je, en wat verwacht je met "
                          "lakmoes?",
                  "Ze is basisch, want fenolftaleïne wordt enkel in een base paars. Met lakmoes verwacht "
                  "je dus blauw.", 4),
                 ("open", "Waarom zegt een pH van 3 iets over de concentratie H⁺?",
                  "Hoe lager de pH, hoe meer H⁺ in de oplossing. Een pH van 3 ligt onder zeven, dus is de "
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
                 ("open", "In de reactie 2 Mg + O₂ → 2 MgO: wie is de oxidator, wie de reductor, en hoe "
                          "veranderen de oxidatiegetallen?",
                  "Magnesium is de reductor: het geeft elektronen af en gaat van 0 naar +II. Zuurstof is "
                  "de oxidator: het neemt ze op en gaat van 0 naar −II.", 6),
                 ("open", "In de reactie Zn + CuSO₄ → ZnSO₄ + Cu: welke stof wordt geoxideerd, en wat zie "
                          "je gebeuren in de beker?",
                  "Zink wordt geoxideerd van 0 naar +II en gaat in oplossing. Het koperion wordt "
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
                 ("kort", "Hoeveel moleculen O₂ heb je nodig voor één molecule CH₄?", "2", W),
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
    hoe=HOE + ["Gebruik N_A = 6,02.10²³ deeltjes per mol. De relatieve atoommassa's staan bij de opgave."],
    reeksen=[
        dict(kop="De molaire massa",
             opdracht="Reken uit. H 1,0; C 12,0; N 14,0; O 16,0; Na 23,0; S 32,1; Cl 35,5; Ca 40,1.",
             oefeningen=[
                 ("rij", [("CH₄", "16,0 g/mol"), ("HNO₃", "63,0 g/mol"),
                          ("CaCO₃", "100,1 g/mol")], "Molaire massa?", WW),
                 ("rij", [("H₂SO₄", "98,1 g/mol"), ("NaCl", "58,5 g/mol")], "Molaire massa?", WW),
             ]),
        dict(kop="Van massa naar mol en terug",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("64,0 g CH₄ (M = 16,0)", "4,00 mol"),
                          ("117 g NaCl (M = 58,5)", "2,00 mol"),
                          ("5,00 mol water (M = 18,0)", "90,0 g")], "Hoeveel?", WW),
                 ("rij", [("0,250 mol CaCO₃ (M = 100,1)", "25,0 g"),
                          ("22,0 g CO₂ (M = 44,0)", "0,500 mol")], "Hoeveel?", WW),
                 ("open", "Een leerling rekent uit dat 2 mol water 9 g weegt. Leg uit hoe je zonder "
                          "narekenen ziet dat dat niet kan.",
                  "Eén mol water weegt 18,0 g, dus moet twee mol zwaarder zijn dan één mol. Negen gram is "
                  "juist de helft van één mol, dus heeft ze vermenigvuldigd waar ze moest delen.", 6),
             ]),
        dict(kop="Deeltjes tellen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("3,01.10²⁴ deeltjes", "5,00 mol"),
                          ("0,100 mol", "6,02.10²² deeltjes")], "Hoeveel?", WL),
                 ("waar", "Eén mol van elke stof bevat evenveel deeltjes.", True),
                 ("waar", "Eén mol water en één mol koolstofdioxide hebben dezelfde massa.", False),
             ]),
        dict(kop="Concentraties",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("0,600 mol tot 3,00 L", "0,200 mol/L"),
                          ("0,0500 mol tot 200 mL", "0,250 mol/L"),
                          ("1,50 L van 0,400 mol/L", "0,600 mol")], "Hoeveel?", WW),
                 ("rij", [("58,5 g NaCl per liter (M = 58,5)", "1,00 mol/L"),
                          ("20,0 g NaOH per liter (M = 40,0)", "0,500 mol/L")],
                  "Molaire concentratie?", WW),
                 ("open", "Leg uit in welke stappen je van een massaconcentratie in g/L naar een molaire "
                          "concentratie in mol/L gaat.",
                  "Je deelt de massa per liter door de molaire massa. Zo zet je gram om in mol en houd je "
                  "het volume gelijk.", 4),
             ]),
        dict(kop="Verdunnen",
             opdracht="Reken uit met c₁V₁ = c₂V₂.",
             oefeningen=[
                 ("rij", [("100 mL van 0,500 mol/L tot 500 mL", "0,100 mol/L"),
                          ("10,0 mL van 2,00 mol/L tot 250 mL", "0,0800 mol/L")],
                  "Nieuwe concentratie?", WL),
                 ("open", "Je hebt 250 mL van 0,200 mol/L nodig en je voorraad is 2,00 mol/L. Hoeveel neem "
                          "je uit de voorraad, en wat doe je daarna?",
                  "V₁ = 0,200 maal 250 gedeeld door 2,00, dus 25,0 mL. Die giet je in een maatkolf van "
                  "250 mL en vul je aan met water tot aan het streepje.", 6),
                 ("waar", "Bij het verdunnen blijft het aantal mol opgeloste stof gelijk.", True),
                 ("waar", "De molaire concentratie stijgt als je water toevoegt.", False),
             ]),
        dict(kop="Stoichiometrie",
             opdracht="Reken uit of leg uit.",
             oefeningen=[
                 ("rij", [("N₂ + 3 H₂ → 2 NH₃, met 6,00 mol H₂", "4,00 mol NH₃"),
                          ("2 H₂ + O₂ → 2 H₂O, met 3,00 mol O₂", "6,00 mol H₂O")],
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
                 ("waar", "Je belast een balans van 200 g niet met een kilo.", True),
                 ("waar", "Chemisch afval mag in de gootsteen zolang je veel water laat lopen.", False),
                 ("waar", "Glasscherven veeg je met de hand bij elkaar.", False),
             ]),
        dict(kop="Welk materiaal?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("precies 25,0 mL afmeten", "een volpipet"),
                          ("een oplossing tot 250 mL aanvullen", "een maatkolf"),
                          ("zwenken zonder te morsen", "een erlenmeyer")], "Welk materiaal?", WL),
                 ("rij", [("een vaste stof fijnmaken", "mortier en stamper"),
                          ("twee vloeistoflagen scheiden", "een scheitrechter"),
                          ("damp weer vloeibaar maken", "een liebigkoeler")], "Welk materiaal?", WL),
                 ("open", "Je moet ongeveer 80 mL water afmeten. Je hebt een maatcilinder van 100 mL en "
                          "een van 1 L. Welke kies je, en waarom?",
                  "Die van 100 mL. Het meetbereik ligt net boven je volume, dus is de schaalverdeling "
                  "fijner en lees je nauwkeuriger af. Een grote cilinder leest veel grover af.", 5),
                 ("open", "Hoe lees je het volume in een maatcilinder correct af?",
                  "Op ooghoogte, onderaan de holle vloeistofspiegel, de meniscus. Zo maak je geen "
                  "kijkfout.", 4),
             ]),
        dict(kop="Eenheden en voorvoegsels",
             opdracht="Reken om of vul aan.",
             oefeningen=[
                 ("rij", [("4,5 mg in g", "0,0045 g"), ("0,25 L in mL", "250 mL"),
                          ("1500 g in kg", "1,5 kg")], "Hoeveel?", WW),
                 ("rij", [("kilo", "10³"), ("micro", "10⁻⁶"), ("nano", "10⁻⁹")], "Welke waarde?", W),
                 ("rij", [("de SI-eenheid van volume", "de kubieke meter"),
                          ("de SI-eenheid van massa", "de kilogram"),
                          ("de SI-eenheid van absolute temperatuur", "de kelvin")],
                  "Welke eenheid?", WL),
             ]),
        dict(kop="Beduidende cijfers en notatie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("0,00250", "3"), ("12,0", "3"), ("1200", "2")],
                  "Hoeveel beduidende cijfers?", W),
                 ("rij", [("0,00072", "7,2.10⁻⁴"), ("45600", "4,56.10⁴")],
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
