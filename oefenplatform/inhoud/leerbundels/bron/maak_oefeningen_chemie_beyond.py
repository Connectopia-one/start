# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij chemie 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere stoffen om in een klasse te zetten, andere getallen om mee te
rekenen, en opdrachten die je enkel op papier kan maken (een vergelijking
uitbalanceren, een tabel aanvullen, een stap uitleggen). Wie hier iets
bijschrijft, legt het eerst naast `../../beyond/chemie.json` en naast de
leerbundel van hetzelfde thema in `maak_chemie_beyond.py`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.

De atoommassa's die een opgave nodig heeft, staan telkens bij de opgave zelf,
zodat er geen periodiek systeem naast het blad moet liggen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Chemie"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

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
OEFENBUNDELS["oefenbundel-anorganische-stoffen-stofklassen-en-naamgeving-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Anorganische stoffen: stofklassen en naamgeving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In welke stofklasse?",
             opdracht="Schrijf oxide, hydroxide, zuur of zout.",
             oefeningen=[
                 ("rij", [("K₂O", "oxide"), ("KOH", "hydroxide"), ("KNO₃", "zout")],
                  "Welke stofklasse?", WW),
                 ("rij", [("H₃PO₄", "zuur"), ("Ba(OH)₂", "hydroxide"), ("Fe₂O₃", "oxide")],
                  "Welke stofklasse?", WW),
                 ("rij", [("MgSO₄", "zout"), ("HBr", "zuur"), ("Al(OH)₃", "hydroxide")],
                  "Welke stofklasse?", WW),
             ]),
        dict(kop="Binair, ternair of nog iets anders",
             opdracht="Schrijf hoeveel verschillende elementen erin zitten, en of de stof dus binair of ternair is.",
             oefeningen=[
                 ("rij", [("CaCl₂", r"\(2\), binair"), ("NaNO₃", r"\(3\), ternair"), ("SO₃", r"\(2\), binair")],
                  "Hoeveel elementen, en wat is het?", WL),
                 ("rij", [("KHCO₃", r"\(4\), geen van de twee"), ("Li₂O", r"\(2\), binair"),
                          ("CuSO₄", r"\(3\), ternair")],
                  "Hoeveel elementen, en wat is het?", WL),
                 ("open", "Leg uit waarom een binaire verbinding niet per se twee atomen heeft.",
                  "Binair zegt dat er twee verschillende elementen in zitten, niet twee atomen. "
                  "Fe₂O₃ is binair en heeft vijf atomen: twee ijzer en drie zuurstof.", 4),
             ]),
        dict(kop="Bijzondere gevallen",
             opdracht="Schrijf peroxide, hydraat, waterstofzout of ammoniumzout.",
             oefeningen=[
                 ("rij", [("Na₂O₂", "peroxide"), ("NH₄Br", "ammoniumzout"),
                          ("KHSO₄", "waterstofzout")],
                  "Wat is het?", WW),
                 ("rij", [("MgSO₄·7H₂O", "hydraat"), ("H₂O₂", "peroxide"),
                          ("(NH₄)₂SO₄", "ammoniumzout")],
                  "Wat is het?", WW),
                 ("waar", "In een peroxide heeft zuurstof oxidatiegetal −II.", False),
                 ("waar", "Een ammoniumzout bevat geen enkel metaalatoom.", True),
             ]),
        dict(kop="De waardigheid",
             opdracht="Schrijf hoeveel protonen het zuur kan afstaan, of hoeveel OH-groepen het hydroxide heeft.",
             oefeningen=[
                 ("rij", [("HNO₃", r"\(1\)"), ("H₂CO₃", r"\(2\)"), ("H₃PO₄", r"\(3\)")],
                  "Hoeveel?", "90px"),
                 ("rij", [("NaOH", r"\(1\)"), ("Ca(OH)₂", r"\(2\)"), ("Al(OH)₃", r"\(3\)")],
                  "Hoeveel?", "90px"),
             ]),
        dict(kop="Naam of formule",
             opdracht="Vul in wat ontbreekt.",
             oefeningen=[
                 ("tabel", ["gebruiksnaam", "stof", "formule"],
                  [["soda", "natriumcarbonaat", None],
                   ["bakpoeder", None, "NaHCO₃"],
                   ["bijtende soda", "natriumhydroxide", None],
                   ["gebluste kalk", None, "Ca(OH)₂"],
                   ["ongebluste kalk", "calciumoxide", None]],
                  "soda: Na₂CO₃ · bakpoeder: natriumwaterstofcarbonaat · bijtende soda: NaOH · "
                  "gebluste kalk: calciumhydroxide · ongebluste kalk: CaO", WL),
                 ("rij", [("lachgas", "N₂O"), ("blauwzuur", "HCN"), ("zoutzuur", "HCl in water")],
                  "Welke formule?", WW),
                 ("rij", [("K", "kalium"), ("Pb", "lood"), ("Cu", "koper")],
                  "Welk element?", WW),
             ]),
        dict(kop="Met woorden",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat het Romeinse cijfer in koper(II)sulfaat betekent, en waarom het nodig is.",
                  "Het is het oxidatiegetal van het metaal, hier +II. Koper kan ook +I zijn, en dan "
                  "hoort er een andere formule bij. Zonder dat cijfer weet je dus niet welke van de "
                  "twee verbindingen bedoeld is.", 5),
                 ("open", "Waarom spreken we bij NaCl van een formule-eenheid en niet van een molecule?",
                  "In het rooster van NaCl staan de ionen in verhouding één op één, maar er bestaat "
                  "geen losse molecule NaCl. De formule geeft dus de kleinste verhouding van de ionen.", 5),
                 ("open", "Zwavelzuur is H₂SO₄ en zwaveligzuur is H₂SO₃. Leg uit welke regel achter die twee namen zit.",
                  "De uitgang -aat hoort bij het zuur met het meeste zuurstof en de uitgang -iet bij "
                  "dat met één zuurstofatoom minder. Daarom hoort zwavelzuur bij sulfaat SO₄²⁻ en "
                  "zwaveligzuur bij sulfiet SO₃²⁻.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-organische-stoffen-stofklassen-en-naamgeving-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Organische stoffen: stofklassen en naamgeving",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke stofklasse?",
             opdracht="Schrijf de stofklasse: alcohol, aldehyde, keton, carbonzuur, ether, ester, amine of amide.",
             oefeningen=[
                 ("rij", [("CH₃-CH₂-CH₂-OH", "alcohol"), ("CH₃-CO-CH₃", "keton"),
                          ("CH₃-CH₂-COOH", "carbonzuur")],
                  "Welke stofklasse?", WW),
                 ("rij", [("CH₃-O-CH₂-CH₃", "ether"), ("CH₃-CH₂-CHO", "aldehyde"),
                          ("CH₃-CH₂-NH₂", "amine")],
                  "Welke stofklasse?", WW),
                 ("rij", [("CH₃-COO-CH₂-CH₃", "ester"), ("CH₃-CO-NH₂", "amide"),
                          ("CH₃-CH₂-CH₂-CHO", "aldehyde")],
                  "Welke stofklasse?", WW),
             ]),
        dict(kop="Verzadigd of niet",
             opdracht="Schrijf alkaan, alkeen of alkyn, en of de keten verzadigd of onverzadigd is.",
             oefeningen=[
                 ("rij", [("C₃H₈", "alkaan, verzadigd"), ("C₃H₆", "alkeen, onverzadigd"),
                          ("C₂H₂", "alkyn, onverzadigd")],
                  "Wat is het?", WL),
                 ("kort", "Hoeveel waterstofatomen heeft een alkaan met zes koolstofatomen?", r"\(14\)", W),
                 ("kort", "Hoeveel waterstofatomen heeft een alkeen met vijf koolstofatomen?", r"\(10\)", W),
             ]),
        dict(kop="De IUPAC-naam",
             opdracht="Schrijf de naam volgens de regels.",
             oefeningen=[
                 ("rij", [("CH₃-CH₂-CH₂-CH₃", "butaan"), ("CH₃-CH₂-OH", "ethanol"),
                          ("CH₃-COOH", "ethaanzuur")],
                  "Welke naam?", WW),
                 ("rij", [("CH₃-CO-CH₂-CH₃", "butanon"), ("CH₃-CHOH-CH₃", r"propaan-\(2\)-ol"),
                          ("CH₂=CH-CH₃", "propeen")],
                  "Welke naam?", WW),
                 ("open", r"Leg uit waarom propaan-\(1\)-ol en niet propaan-\(3\)-ol de juiste naam is.",
                  "Je nummert de hoofdketen van de kant die de functionele groep het laagste nummer "
                  r"geeft. Van de andere kant geteld zou de OH-groep aan koolstof \(3\) hangen, en \(1\) is "
                  r"kleiner dan \(3\).", 5),
             ]),
        dict(kop="Primair, secundair of tertiair",
             opdracht="Schrijf primair, secundair of tertiair.",
             oefeningen=[
                 ("rij", [(r"butaan-\(1\)-ol", "primair"), (r"butaan-\(2\)-ol", "secundair"),
                          (r"\(2\)-methylpropaan-\(2\)-ol", "tertiair")],
                  "Welke alcohol?", WW),
                 ("open", "Bij een alcohol tel je iets anders dan bij een amine. Leg beide regels uit.",
                  "Bij een alcohol kijk je naar het aantal koolstofatomen dat aan het koolstofatoom "
                  "met de OH-groep hangt. Bij een amine kijk je naar het aantal koolstofketens dat "
                  "aan het stikstofatoom hangt.", 5),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Cyclohexaan is een aromatische verbinding.", False),
                 ("waar", "In benzeen liggen de elektronen van de dubbele bindingen over de hele ring verdeeld.", True),
                 ("waar", "Een ether kan onderling waterstofbruggen vormen.", False),
                 ("waar", "Een onvertakte keten staat in werkelijkheid in zigzag.", True),
             ]),
        dict(kop="Namen uit het dagelijks leven",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["gebruiksnaam", "IUPAC-naam", "stofklasse"],
                  [["azijnzuur", None, "carbonzuur"],
                   ["aceton", "propanon", None],
                   ["glycerol", None, "alcohol"],
                   ["glycol", "ethaandiol", None],
                   ["drankalcohol", None, "alcohol"]],
                  "azijnzuur: ethaanzuur · aceton: keton · glycerol: propaantriol · "
                  "glycol: alcohol · drankalcohol: ethanol", WL),
                 ("rij", [("chloroform", "trichloormethaan"), ("formol", "methanal in water"),
                          ("aardgas", "methaan")],
                  "Welke stof is het?", WL),
             ]),
        dict(kop="Voorstellingen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Wat laat een skeletnotatie weg, en wat schrijf je er wel in uit?",
                  "De koolstofatomen en hun waterstofatomen worden niet getekend: elke hoek en elk "
                  "uiteinde van de lijn is een koolstofatoom. Functionele groepen schrijf je wel uit.", 5),
                 ("open", "Waarom zegt een bolstaafmodel meer over een molecule dan een brutoformule?",
                  "Een brutoformule zegt enkel hoeveel atomen van elk element er zijn. In een "
                  "bolstaafmodel zie je ook hoe de atomen aan elkaar zitten en welke hoeken de "
                  "bindingen met elkaar maken.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-isomerie-en-chiraliteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Isomerie en chiraliteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk soort isomerie?",
             opdracht="Schrijf ketenisomerie, plaatsisomerie of functie-isomerie.",
             oefeningen=[
                 ("rij", [(r"pentaan en \(2\)-methylbutaan", "ketenisomerie"),
                          (r"butaan-\(1\)-ol en butaan-\(2\)-ol", "plaatsisomerie")],
                  "Welk soort?", WL),
                 ("rij", [("propanal en propanon", "functie-isomerie"),
                          (r"pent-\(1\)-een en pent-\(2\)-een", "plaatsisomerie")],
                  "Welk soort?", WL),
                 ("rij", [("ethaanzuur en methylmethanoaat", "functie-isomerie"),
                          (r"hexaan en \(2{,}3\)-dimethylbutaan", "ketenisomerie")],
                  "Welk soort?", WL),
             ]),
        dict(kop="Zijn het isomeren?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Butaan en pentaan zijn isomeren van elkaar.", False),
                 ("waar", "Ethanol en dimethylether zijn isomeren van elkaar.", True),
                 ("waar", "Twee isomeren hebben altijd hetzelfde kookpunt.", False),
                 ("waar", "Plaatsisomeren horen tot dezelfde stofklasse.", True),
             ]),
        dict(kop="Tellen",
             opdracht="Schrijf het aantal.",
             oefeningen=[
                 ("rij", [("structuurisomeren van C₄H₁₀", r"\(2\)"),
                          ("structuurisomeren van C₅H₁₂", r"\(3\)"),
                          ("structuurisomeren van C₃H₈", r"\(1\)")],
                  "Hoeveel?", "90px"),
                 ("rij", [(r"stereo-isomeren bij \(1\) asymmetrisch koolstofatoom", r"\(2\)"),
                          (r"bij \(2\) asymmetrische koolstofatomen", r"\(4\)"),
                          (r"bij \(4\) asymmetrische koolstofatomen", r"\(16\)")],
                  "Hoeveel?", "90px"),
                 ("open", "Leg uit waarom er van methaan geen enkel isomeer bestaat.",
                  "Er is maar één manier om één koolstofatoom en vier waterstofatomen aan elkaar te "
                  "zetten. Pas vanaf vier koolstofatomen kan een keten vertakken.", 4),
             ]),
        dict(kop="Z of E",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [(r"but-\(2\)-een", "wel Z/E"), (r"but-\(1\)-een", "geen Z/E"),
                          ("propeen", "geen Z/E")],
                  "Bestaat er Z/E-isomerie?", WL),
                 ("open", "Waarom bestaat er geen Z/E-isomerie rond een enkelvoudige binding?",
                  "Een sigma-binding is coaxiaal en radiaal symmetrisch, dus mag de molecule er vrij "
                  "rond draaien. Door dat draaien gaan de twee vormen in elkaar over, en dan zijn "
                  "het dezelfde stof.", 5),
                 ("open", "Leg uit waarom een Z-isomeer en een E-isomeer een verschillend kookpunt hebben.",
                  "Bij de Z-vorm staan de groepen aan dezelfde kant, en dan versterken hun dipooltjes "
                  "elkaar. Bij de E-vorm heffen ze elkaar vaker op, dus is de molecule minder polair "
                  "en zijn de krachten tussen de moleculen zwakker.", 5),
             ]),
        dict(kop="Chiraal of niet",
             opdracht="Kruis aan of antwoord kort.",
             oefeningen=[
                 ("rij", [(r"\(2\)-chloorbutaan", "chiraal"), (r"propaan-\(2\)-ol", "niet chiraal"),
                          (r"\(2\)-broompropaan", "niet chiraal")],
                  "Chiraal of niet?", WW),
                 ("open", "Wanneer is een koolstofatoom asymmetrisch?",
                  "Als er vier verschillende groepen aan hangen. Dan valt de molecule niet samen met "
                  "haar spiegelbeeld, net zoals je linker- en rechterhand.", 4),
                 ("open", "Wat is een racemisch mengsel, en waarom draait het gepolariseerd licht niet?",
                  "Het is een mengsel met evenveel van beide spiegelbeeldisomeren. De ene helft draait "
                  "het vlak even sterk naar links als de andere naar rechts, dus heffen ze elkaar "
                  "precies op.", 5),
                 ("open", "Waarom werkt soms maar de helft van een medicijn dat als racemisch mengsel verkocht wordt?",
                  "Receptoren en enzymen in het lichaam zijn zelf chiraal, dus passen ze maar op één "
                  "van de twee spiegelbeeldvormen. De andere vorm doet niets of werkt zelfs anders.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-atoombouw-orbitalen-en-het-periodiek-systeem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Atoombouw, orbitalen en het periodiek systeem",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoeveel elektronen passen erin?",
             opdracht="Schrijf het aantal.",
             oefeningen=[
                 ("rij", [("één orbitaal", r"\(2\)"), ("een s-subniveau", r"\(2\)"),
                          ("een p-subniveau", r"\(6\)")],
                  "Hoeveel elektronen?", "90px"),
                 ("rij", [("een d-subniveau", r"\(10\)"), ("een f-subniveau", r"\(14\)"),
                          ("een p-subniveau in orbitalen", r"\(3\) orbitalen")],
                  "Hoeveel?", "110px"),
             ]),
        dict(kop="De configuratie schrijven",
             opdracht="Schrijf de volledige elektronenconfiguratie.",
             oefeningen=[
                 ("rij", [(r"stikstof, \(7\) elektronen", "1s² 2s² 2p³"),
                          (r"natrium, \(11\) elektronen", "1s² 2s² 2p⁶ 3s¹")],
                  "Welke configuratie?", WL),
                 ("rij", [(r"fluor, \(9\) elektronen", "1s² 2s² 2p⁵"),
                          (r"magnesium, \(12\) elektronen", "1s² 2s² 2p⁶ 3s²")],
                  "Welke configuratie?", WL),
                 ("kort", "Hoeveel valentie-elektronen heeft een atoom met [Ne] 3s² 3p⁴?", r"\(6\)", W),
                 ("kort", "Hoeveel elektronen heeft het ion Mg²⁺?", r"\(10\)", W),
             ]),
        dict(kop="Kwantumgetallen",
             opdracht="Schrijf welk kwantumgetal het is.",
             oefeningen=[
                 ("rij", [("zegt in welke schil het elektron zit", "het hoofdkwantumgetal"),
                          ("zegt of het een s-, p-, d- of f-orbitaal is", "het nevenkwantumgetal")],
                  "Welk getal?", WL),
                 ("rij", [("zegt in welk orbitaal van dat subniveau", "het magnetisch kwantumgetal"),
                          ("kan +½ of −½ zijn", "het spinkwantumgetal")],
                  "Welk getal?", WL),
                 ("open", "Leg het uitsluitingsprincipe van Pauli uit in je eigen woorden.",
                  "Twee elektronen van hetzelfde atoom kunnen nooit alle vier hun kwantumgetallen "
                  "gelijk hebben. Zitten ze in hetzelfde orbitaal, dan moet hun spin verschillen, en "
                  "daarom passen er maar twee in.", 5),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Volgens de diagonaalregel wordt 3d gevuld voor 4s.", False),
                 ("waar", "De regel van Hund zegt dat elk orbitaal van een subniveau eerst één elektron krijgt.", True),
                 ("waar", "Een orbitaal is een vaste baan waarop een elektron rondloopt.", False),
                 ("waar", "Helium heeft met twee valentie-elektronen al de edelgasconfiguratie.", True),
             ]),
        dict(kop="Plaats in het systeem",
             opdracht="Schrijf de groep en de periode.",
             oefeningen=[
                 ("rij", [("[Ne] 3s¹", r"groep \(1\), periode \(3\)"),
                          ("[Ar] 4s² 3d¹⁰ 4p³", r"groep \(15\), periode \(4\)")],
                  "Groep en periode?", WL),
                 ("rij", [("1s² 2s² 2p⁵", r"groep \(17\), periode \(2\)"),
                          ("[Kr] 5s²", r"groep \(2\), periode \(5\)")],
                  "Groep en periode?", WL),
                 ("rij", [("lithium, natrium, kalium", "de alkalimetalen"),
                          ("fluor, chloor, broom", "de halogenen"),
                          ("zuurstof, zwavel, selenium", "de zuurstofgroep")],
                  "Hoe heet de groep?", WL),
             ]),
        dict(kop="Trends",
             opdracht="Omcirkel het grootste deeltje of antwoord kort.",
             oefeningen=[
                 ("rij", [("natrium of kalium", "kalium"), ("natrium of magnesium", "natrium"),
                          ("chlooratoom of chloride-ion", "het chloride-ion")],
                  "Welk is het grootst?", WL),
                 ("open", "Leg uit waarom een atoom kleiner wordt als je in een periode naar rechts gaat.",
                  "Er komt elk keer een proton bij in de kern, terwijl de elektronen in hetzelfde "
                  "hoofdniveau blijven. Die sterkere aantrekking trekt de elektronenwolk samen.", 5),
                 ("open", "Waar in het periodiek systeem staan de metalen met het sterkste metaalkarakter, en waarom?",
                  "Linksonder. Daar zitten de valentie-elektronen ver van de kern en zijn er maar "
                  "één of twee, dus staat het atoom ze het makkelijkst af.", 5),
                 ("open", "Waarom reageren de edelgassen bijna niet?",
                  "Hun buitenste hoofdniveau is helemaal volgevuld: acht valentie-elektronen, bij "
                  "helium twee. Ze hebben dus niets te winnen door elektronen af te staan of op te "
                  "nemen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-atoombinding-en-lewisstructuren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Atoombinding en lewisstructuren",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Sigma en pi tellen",
             opdracht="Schrijf hoeveel sigma- en hoeveel pi-bindingen de molecule heeft.",
             oefeningen=[
                 ("rij", [("H₂O", r"\(2\) sigma, \(0\) pi"), ("CH₄", r"\(4\) sigma, \(0\) pi")],
                  "Hoeveel van elk?", WL),
                 ("rij", [("CH₂=CH₂", r"\(5\) sigma, \(1\) pi"), ("HC≡CH", r"\(3\) sigma, \(2\) pi")],
                  "Hoeveel van elk?", WL),
                 ("rij", [("CO₂", r"\(2\) sigma, \(2\) pi"), ("N₂", r"\(1\) sigma, \(2\) pi")],
                  "Hoeveel van elk?", WL),
             ]),
        dict(kop="Korter of langer",
             opdracht="Zet de drie bindingen in de juiste volgorde, van lang naar kort.",
             oefeningen=[
                 ("open", "C–C, C=C en C≡C: zet ze van lang naar kort en zeg waarom.",
                  r"C–C (ongeveer \(154\) pm), dan C=C (\(134\) pm), dan C≡C (\(120\) pm). Elke extra binding "
                  "trekt de twee atomen dichter naar elkaar, dus wordt de binding korter en sterker.", 5),
                 ("waar", "Tussen twee atomen kunnen meerdere sigma-bindingen naast elkaar liggen.", False),
                 ("waar", "Een pi-binding is zwakker dan een sigma-binding tussen dezelfde atomen.", True),
                 ("waar", "Rond een dubbele binding kan een molecule vrij draaien.", False),
             ]),
        dict(kop="Vrije elektronenparen tellen",
             opdracht="Schrijf hoeveel vrije elektronenparen het vetgedrukte atoom heeft.",
             oefeningen=[
                 ("rij", [("<b>O</b> in H₂O", r"\(2\)"), ("<b>N</b> in NH₃", r"\(1\)"),
                          ("<b>Cl</b> in Cl₂", r"\(3\)")],
                  "Hoeveel vrije paren?", "90px"),
                 ("rij", [("<b>N</b> in NH₄⁺", r"\(0\)"), ("<b>O</b> in H₃O⁺", r"\(1\)"),
                          ("<b>C</b> in CH₄", r"\(0\)")],
                  "Hoeveel vrije paren?", "90px"),
             ]),
        dict(kop="Formele lading",
             opdracht="Reken met valentie-elektronen min vrije elektronen min aantal bindingen.",
             oefeningen=[
                 ("rij", [("N in NH₄⁺", r"+\(1\)"), ("O in H₃O⁺", r"+\(1\)"), ("O in OH⁻", r"\(-1\)")],
                  "Welke formele lading?", WW),
                 ("open", "Leg uit waarin de formele lading verschilt van het oxidatiegetal.",
                  "Bij de formele lading verdeel je de elektronen van een binding eerlijk over de "
                  "twee atomen. Bij het oxidatiegetal geef je ze volledig aan het meest "
                  "elektronegatieve atoom van de twee.", 5),
             ]),
        dict(kop="Welke soort binding?",
             opdracht="Schrijf atoombinding, ionbinding, metaalbinding of donor-acceptorbinding.",
             oefeningen=[
                 ("rij", [("tussen Na⁺ en Cl⁻ in het rooster", "ionbinding"),
                          ("tussen de atomen in CH₄", "atoombinding")],
                  "Welke binding?", WL),
                 ("rij", [("tussen koperionen en vrije elektronen", "metaalbinding"),
                          ("tussen NH₃ en H⁺ in NH₄⁺", "donor-acceptorbinding")],
                  "Welke binding?", WL),
                 ("open", "Leg uit waarom een metaal elektrische stroom geleidt en een zout in vaste toestand niet.",
                  "In een metaalrooster bewegen de valentie-elektronen vrij door het hele rooster, "
                  "dus kan lading verplaatsen. In een vast ionrooster zitten de ionen op hun plaats "
                  "en is er niets dat kan bewegen.", 5),
                 ("open", "Wat is er bijzonder aan een donor-acceptorbinding, en hoe zie je er achteraf nog iets van?",
                  "Eén atoom levert het hele bindende elektronenpaar in plaats van elk atoom één "
                  "elektron. Achteraf zie je er niets meer van: in NH₄⁺ zijn de vier bindingen niet "
                  "van elkaar te onderscheiden.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ruimtelijke-structuur-polariteit-en-intermoleculaire-krachten-beyond"] = dict(
    vak=VAK, niveau=BEYOND,
    titel="Ruimtelijke structuur, polariteit en intermoleculaire krachten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het sterisch getal",
             opdracht="Schrijf het sterisch getal van het centrale atoom.",
             oefeningen=[
                 ("rij", [("C in CH₄", r"\(4\)"), ("O in H₂O", r"\(4\)"), ("N in NH₃", r"\(4\)")],
                  "Sterisch getal?", "90px"),
                 ("rij", [("C in CO₂", r"\(2\)"), ("S in SO₂", r"\(3\)"), ("C in CH₂=CH₂", r"\(3\)")],
                  "Sterisch getal?", "90px"),
             ]),
        dict(kop="Vorm en hybridisatie",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["sterisch getal", "vorm zonder vrije paren", "hybridisatie", "hoek"],
                  [[r"\(2\)", None, "sp", None],
                   [r"\(3\)", "vlakke driehoek", None, r"\(120^{\circ}\)"],
                   [r"\(4\)", None, "sp³", None]],
                  r"\(2\): lineair, \(180^{\circ} \cdot 3\): sp² · \(4\): tetraëder, \(109{,}5^{\circ}\)", W),
                 ("rij", [("CH₄", "tetraëder"), ("NH₃", "piramide"), ("H₂O", "geknikt")],
                  "Welke vorm?", WW),
                 ("rij", [("CO₂", "lineair"), ("SO₂", "vlak geknikt"), ("NH₄⁺", "tetraëder")],
                  "Welke vorm?", WW),
             ]),
        dict(kop="De bindingshoek",
             opdracht="Schrijf de werkelijke hoek en leg uit waarom ze afwijkt.",
             oefeningen=[
                 ("rij", [("CH₄", r"\(109{,}5^{\circ}\)"), ("NH₃", r"\(107^{\circ}\)"), ("H₂O", r"\(104{,}5^{\circ}\)")],
                  "Welke hoek?", W),
                 ("open", "Alle drie hebben sterisch getal vier. Leg uit waarom hun hoeken toch verschillen.",
                  "Een vrij elektronenpaar hangt dichter bij het centrale atoom en neemt meer plaats "
                  "dan een bindend paar. Methaan heeft geen vrij paar, ammoniak één en water twee, "
                  "dus wordt de hoek elke keer een stuk kleiner.", 6),
             ]),
        dict(kop="Polair of apolair",
             opdracht="Schrijf polair of apolair.",
             oefeningen=[
                 ("rij", [("H₂O", "polair"), ("CO₂", "apolair"), ("CCl₄", "apolair")],
                  "Polair of apolair?", WW),
                 ("rij", [("NH₃", "polair"), ("CH₄", "apolair"), ("HCl", "polair")],
                  "Polair of apolair?", WW),
                 ("open", "In CO₂ en in H₂O zijn de bindingen allebei polair. Leg uit waarom alleen water een polaire molecule is.",
                  "CO₂ is lineair, dus staan de twee dipolen precies tegenover elkaar en heffen ze "
                  "elkaar op. Water is geknikt, dus wijzen de dipolen in dezelfde richting en blijft "
                  "er een netto dipool over.", 6),
             ]),
        dict(kop="Welke kracht?",
             opdracht="Schrijf londonkracht, dipoolkracht, waterstofbrug, ion-dipoolkracht of coulombkracht.",
             oefeningen=[
                 ("rij", [("tussen twee watermoleculen", "waterstofbrug"),
                          ("tussen twee methaanmoleculen", "londonkracht")],
                  "Welke kracht?", WL),
                 ("rij", [("tussen Na⁺ en water", "ion-dipoolkracht"),
                          ("tussen Na⁺ en Cl⁻", "coulombkracht")],
                  "Welke kracht?", WL),
                 ("rij", [("pentaan of butaan", "pentaan"), (r"butaan of \(2\)-methylpropaan", "butaan"),
                          ("water of waterstofsulfide", "water")],
                  "Welke kookt bij de hoogste temperatuur?", WL),
             ]),
        dict(kop="Oplossen en roosters",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("rij", [("zout in water", "lost op"), ("olie in wasbenzine", "lost op"),
                          ("hexaan in water", "lost niet op")],
                  "Lost het op?", WL),
                 ("tabel", ["rooster", "geleidt vast?", "geleidt gesmolten of opgelost?"],
                  [["metaalrooster", None, "ja"],
                   ["ionrooster", "nee", None],
                   ["molecuulrooster", "nee", None]],
                  "metaalrooster: ja · ionrooster: ja · molecuulrooster: nee", WW),
                 ("open", "Leg uit waarom ethanol mengt met water en hexaan niet.",
                  "Ethanol heeft een OH-groep en kan dus waterstofbruggen met water vormen. Hexaan "
                  "is helemaal apolair en kan dat niet, dus blijft het als aparte laag liggen.", 5),
                 ("open", "Waarom heeft diamant een veel hoger smeltpunt dan ijs?",
                  "Diamant is een atoomrooster: om het te smelten moet je echte atoombindingen "
                  "breken. Bij ijs volstaat het de waterstofbruggen tussen de moleculen te "
                  "verbreken, en die zijn veel zwakker.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemisch-rekenen-mol-molaire-massa-en-concentratie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Chemisch rekenen: mol, molaire massa en concentratie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Molaire massa",
             opdracht=r"Reken met H \(1\), C \(12\), N \(14\), O \(16\), Na \(23\), S \(32\) en Cl \(35{,}5\) g/mol.",
             oefeningen=[
                 ("rij", [("NH₃", r"\(17\) g/mol"), ("NaOH", r"\(40\) g/mol"), ("CO₂", r"\(44\) g/mol")],
                  "Welke molaire massa?", WW),
                 ("rij", [("H₂SO₄", r"\(98\) g/mol"), ("NaCl", r"\(58{,}5\) g/mol"),
                          ("C₆H₁₂O₆", r"\(180\) g/mol")],
                  "Welke molaire massa?", WW),
             ]),
        dict(kop="Van gram naar mol",
             opdracht="Reken uit. Schrijf eerst de formule op.",
             oefeningen=[
                 ("kort", r"Hoeveel mol is \(34\) g NH₃ (M = \(17\) g/mol)?", r"\(2\) mol", W),
                 ("kort", r"Hoeveel mol is \(9\) g water (M = \(18\) g/mol)?", r"\(0{,}5\) mol", W),
                 ("kort", r"Hoeveel gram weegt \(0{,}25\) mol NaOH (M = \(40\) g/mol)?", r"\(10\) g", W),
                 ("kort", r"Hoeveel gram weegt \(3\) mol CO₂ (M = \(44\) g/mol)?", r"\(132\) g", W),
             ]),
        dict(kop="Deeltjes tellen",
             opdracht=r"Reken met \(6{,}022 \cdot 10^{23}\) deeltjes per mol.",
             oefeningen=[
                 ("kort", r"Hoeveel moleculen zitten er in \(0{,}5\) mol?", r"\(3{,}011 \cdot 10^{23}\)", WW),
                 ("kort", r"Hoeveel mol zuurstofatomen zitten er in \(2\) mol H₂SO₄?", r"\(8\) mol", W),
                 ("open", "Achttien gram water en achttien gram glucose. In welk bekertje zitten de meeste moleculen, en waarom?",
                  r"In het water. Water heeft M = \(18\) g/mol, dus is dat één mol; glucose heeft "
                  r"M = \(180\) g/mol, dus maar een tiende van een mol. Dezelfde massa betekent dus niet "
                  "hetzelfde aantal deeltjes.", 6),
             ]),
        dict(kop="Gassen bij normomstandigheden",
             opdracht=r"Reken met een molair volume van \(22{,}4\) L/mol.",
             oefeningen=[
                 ("rij", [(r"\(2\) mol gas", r"\(44{,}8\) L"), (r"\(0{,}5\) mol gas", r"\(11{,}2\) L"),
                          (r"\(0{,}25\) mol gas", r"\(5{,}6\) L")],
                  "Welk volume?", WW),
                 ("waar", r"Eén mol gas neemt bij elke temperatuur \(22{,}4\) liter in.", False),
                 ("waar", r"Eén mol zuurstofgas en één mol waterstofgas nemen bij \(0^{\circ}\text{C}\) hetzelfde volume in.", True),
             ]),
        dict(kop="Concentratie",
             opdracht="Reken uit. Zet het volume altijd eerst in liter.",
             oefeningen=[
                 ("kort", r"\(0{,}4\) mol in \(2\) L. Welke concentratie?", r"\(0{,}2\) mol/L", WW),
                 ("kort", r"Hoeveel mol zit er in \(250\) mL van \(0{,}8\) mol/L?", r"\(0{,}2\) mol", W),
                 ("kort", r"Hoeveel mol weeg je af voor \(500\) mL van \(0{,}1\) mol/L?", r"\(0{,}05\) mol", W),
                 ("kort", r"Hoeveel gram zout zit er in \(300\) g oplossing van \(5\) massaprocent?", r"\(15\) g", W),
             ]),
        dict(kop="Verdunnen",
             opdracht="Gebruik c₁ · V₁ = c₂ · V₂.",
             oefeningen=[
                 ("kort", r"\(20\) mL van \(1\) mol/L verdund tot \(100\) mL. Welke concentratie?", r"\(0{,}2\) mol/L", WW),
                 ("kort", r"Hoeveel mL van \(2\) mol/L heb je nodig voor \(500\) mL van \(0{,}1\) mol/L?", r"\(25\) mL", W),
                 ("open", "Leg uit waarom het aantal mol opgeloste stof bij verdunnen gelijk blijft.",
                  "Je giet er enkel oplosmiddel bij en haalt er niets uit. Het aantal deeltjes in de "
                  "beker blijft dus hetzelfde, alleen zitten ze in een groter volume, en daardoor "
                  "daalt de concentratie.", 5),
             ]),
        dict(kop="Kleine eenheden en een formule",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("rij", [("procent", "op honderd"), ("promille", "op duizend"),
                          ("ppm", "op een miljoen")],
                  "Op hoeveel?", WW),
                 ("kort", r"Hoeveel milligram per liter water is \(1\) ppm?", r"\(1\) mg", W),
                 ("open", r"Een verbinding bestaat uit \(52{,}2\,\%\) koolstof, \(13{,}0\,\%\) waterstof en \(34{,}8\,\%\) zuurstof. Zoek de eenvoudigste formule (C \(12\), H \(1\), O \(16\)).",
                  r"Deel elk percentage door de atoommassa: \(52\),\(\tfrac{2}{12} = 4{,}35\); \(13\),\(\tfrac{0}{1} = 13{,}0\); "
                  r"\(34\),\(\tfrac{8}{16} = 2{,}18\). Deel door de kleinste: \(2 : 6 : 1\), dus C₂H₆O.", 6),
                 ("open", "Waarom vul je een maatkolf aan tot de maatstreep in plaats van eerst het water af te meten?",
                  "De opgeloste stof neemt zelf ook plaats in. De concentratie hoort bij het volume "
                  "van de hele oplossing, niet bij dat van het water alleen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-stoichiometrie-overmaat-en-de-algemene-gaswet-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stoichiometrie, overmaat en de algemene gaswet",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Uitbalanceren",
             opdracht="Schrijf de coëfficiënten die ontbreken.",
             oefeningen=[
                 ("rij", [("… H₂ + … O₂ → … H₂O", r"\(2\), \(1\), \(2\)"),
                          ("… Na + … Cl₂ → … NaCl", r"\(2\), \(1\), \(2\)")],
                  "Welke coëfficiënten?", WL),
                 ("rij", [("… C₂H₆ + … O₂ → … CO₂ + … H₂O", r"\(2\), \(7\), \(4\), \(6\)"),
                          ("… Fe + … O₂ → … Fe₂O₃", r"\(4\), \(3\), \(2\)")],
                  "Welke coëfficiënten?", WL),
                 ("rij", [("… CH₄ + … O₂ → … CO₂ + … H₂O", r"\(1\), \(2\), \(1\), \(2\)"),
                          ("… Al + … HCl → … AlCl₃ + … H₂", r"\(2\), \(6\), \(2\), \(3\)")],
                  "Welke coëfficiënten?", WL),
                 ("waar", "Je mag de formule van een stof aanpassen om een vergelijking te laten kloppen.", False),
             ]),
        dict(kop="Rekenen met de verhouding",
             opdracht=r"Gebruik N₂ + 3 H₂ → 2 NH₃.",
             oefeningen=[
                 ("kort", r"Hoeveel mol NH₃ uit \(3\) mol N₂?", r"\(6\) mol", W),
                 ("kort", r"Hoeveel mol H₂ voor \(4\) mol NH₃?", r"\(6\) mol", W),
                 ("kort", r"Hoeveel mol N₂ voor \(9\) mol H₂?", r"\(3\) mol", W),
             ]),
        dict(kop="Van gram naar gram",
             opdracht="Schrijf alle stappen op: gram, mol, verhouding, mol, gram.",
             oefeningen=[
                 ("open", r"Hoeveel gram MgO ontstaat er uit \(4{,}8\) g Mg? (2 Mg + O₂ → 2 MgO; "
                  r"Mg \(24\) g/mol, MgO \(40\) g/mol)",
                  r"\(4{,}8\) g : \(24\) g/mol = \(0{,}2\) mol Mg. De verhouding Mg op MgO is \(1\) op \(1\), dus \(0{,}2\) mol "
                  r"MgO. \(0{,}2\,\text{mol} \cdot 40\) g/mol = \(8\) g MgO.", 6),
                 ("open", r"Hoeveel gram CO₂ komt er vrij uit 50 g CaCO₃? (CaCO₃ → CaO + CO₂; "
                  r"CaCO₃ \(100\) g/mol, CO₂ \(44\) g/mol)",
                  r"\(50\) g : \(100\) g/mol = \(0{,}5\) mol CaCO₃. De verhouding is \(1\) op \(1\), dus \(0{,}5\) mol CO₂. "
                  r"\(0{,}5\,\text{mol} \cdot 44\) g/mol = \(22\) g CO₂.", 6),
                 ("open", "Leg uit waarom je de verhouding uit de vergelijking niet rechtstreeks op massa's mag toepassen.",
                  "De coëfficiënten geven een verhouding in mol. Twee stoffen met dezelfde "
                  "stofhoeveelheid hebben meestal een heel andere massa, want hun molaire massa "
                  "verschilt. Daarom reken je eerst om naar mol.", 5),
             ]),
        dict(kop="Limiterend reagens",
             opdracht="Deel van elke stof het aantal mol door haar coëfficiënt.",
             oefeningen=[
                 ("rij", [(r"3 mol H₂ en 3 mol O₂ in 2 H₂ + O₂ → 2 H₂O", "H₂ is beperkend"),
                          (r"2 mol N₂ en 3 mol H₂ in N₂ + 3 H₂ → 2 NH₃", "H₂ is beperkend")],
                  "Welke stof is beperkend?", WL),
                 ("kort", r"Hoeveel mol water uit \(3\) mol H₂ en \(3\) mol O₂?", r"\(3\) mol", W),
                 ("waar", "Het limiterend reagens is altijd de stof waarvan je het minste mol hebt.", False),
                 ("open", "Waarom werkt men in de industrie soms met een overmaat van de goedkoopste stof?",
                  "Dan is de dure stof het beperkend reagens en reageert ze zo volledig mogelijk weg. "
                  "Het overschot van de goedkope stof blijft over en wordt vaak hergebruikt.", 5),
             ]),
        dict(kop="De algemene gaswet",
             opdracht=r"Reken met pV = nRT en een molair volume van \(22{,}4\) L/mol bij \(0^{\circ}\text{C}\).",
             oefeningen=[
                 ("rij", [(r"\(0^{\circ}\text{C}\)", r"\(273\) K"), (r"\(27^{\circ}\text{C}\)", r"\(300\) K"), (r"\(100^{\circ}\text{C}\)", r"\(373\) K")],
                  "Hoeveel kelvin?", W),
                 ("kort", r"Hoeveel mol gas zit er in \(5{,}6\) L bij normomstandigheden?", r"\(0{,}25\) mol", W),
                 ("kort", r"Welk volume neemt \(1{,}5\) mol gas in bij normomstandigheden?", r"\(33{,}6\) L", W),
                 ("waar", "Bij hogere druk neemt een gas bij gelijke temperatuur meer plaats in.", False),
                 ("open", r"Een gas van \(2\) liter bij \(300\) K wordt opgewarmd tot \(600\) K bij gelijke druk. Welk volume krijg je, en waarom?",
                  r"\(4\) liter. In pV = nRT staan V en T aan weerszijden van het gelijkheidsteken, dus "
                  "verdubbelt het volume als de temperatuur in kelvin verdubbelt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-reactiesnelheid-botsingsmodel-en-energiediagram-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Reactiesnelheid, botsingsmodel en energiediagram",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Sneller of trager",
             opdracht="Schrijf sneller of trager, en zeg in één woord waarom.",
             oefeningen=[
                 ("rij", [("de oplossing verdunnen", "trager"), ("de stof fijnmalen", "sneller"),
                          ("in de koelkast zetten", "trager")],
                  "Sneller of trager?", WW),
                 ("rij", [("een katalysator toevoegen", "sneller"), ("roeren", "sneller"),
                          ("de concentratie verdubbelen", "sneller")],
                  "Sneller of trager?", WW),
                 ("open", "Leg uit waarom een hogere temperatuur een reactie zoveel sneller maakt.",
                  "De deeltjes botsen vaker én met meer energie. Dat tweede weegt het zwaarst: er "
                  "raken veel meer botsingen boven de activeringsenergie, en dus zijn er veel meer "
                  "effectieve botsingen.", 6),
             ]),
        dict(kop="Effectief of niet",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een effectieve botsing heeft genoeg energie én de juiste stand.", True),
                 ("waar", "Bij een elastische botsing ketsen de deeltjes af zonder te reageren.", True),
                 ("waar", "In een reactiemengsel zijn de meeste botsingen effectief.", False),
                 ("waar", "Een katalysator wordt tijdens de reactie opgebruikt.", False),
             ]),
        dict(kop="Het energiediagram",
             opdracht="Vul in of leg uit.",
             oefeningen=[
                 ("rij", [("de hoogte van de berg boven de reagentia", "de activeringsenergie"),
                          ("de top van de berg", "het geactiveerd complex")],
                  "Hoe heet het?", WL),
                 ("rij", [("het verschil tussen producten en reagentia", "de reactie-energie"),
                          ("producten lager dan reagentia", "exo-energetisch")],
                  "Hoe heet het?", WL),
                 ("open", "Een reactie is exo-energetisch en verloopt toch heel traag. Leg uit hoe dat kan.",
                  "De reactie-energie en de activeringsenergie zijn twee verschillende dingen. De "
                  "producten liggen lager, maar de berg ertussen kan hoog zijn, en dan haalt bijna "
                  "geen botsing die drempel. Benzine heeft daarom een vlam nodig.", 6),
                 ("open", "Wat verandert een katalysator in het energiediagram, en wat niet?",
                  "Hij verlaagt de top van de berg, dus de activeringsenergie. Het begin- en "
                  "eindpunt blijven op dezelfde hoogte, dus de reactie-energie blijft precies "
                  "gelijk.", 5),
             ]),
        dict(kop="Endo of exo",
             opdracht="Schrijf endo-energetisch of exo-energetisch.",
             oefeningen=[
                 ("rij", [("een koudepakje in de sportzaal", "endo-energetisch"),
                          ("het verbranden van hout", "exo-energetisch"),
                          ("water bij ongebluste kalk gieten", "exo-energetisch")],
                  "Endo of exo?", WW),
             ]),
        dict(kop="De snelheidsvergelijking",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("v = k·[A]·[B]", r"totale orde \(2\)"), ("v = k·[A]²·[B]", r"totale orde \(3\)"),
                          ("v = k·[A]", r"totale orde \(1\)")],
                  "Welke totale orde?", WL),
                 ("rij", [("[A] verdubbelt, v verdubbelt", "eerste orde"),
                          (r"[A] verdubbelt, v wordt \(4\) keer groter", "tweede orde"),
                          ("[A] verdubbelt, v blijft gelijk", "nulde orde")],
                  "Welke orde in A?", WL),
                 ("open", "Van wat hangt de snelheidsconstante k af, en van wat niet?",
                  "Ze hangt af van de temperatuur, van de katalysator en van de reactie zelf. Ze "
                  "hangt niet af van de concentraties, want die staan al apart in de vergelijking.", 5),
                 ("open", "Waarom staat voedsel langer goed in de koelkast, en waarom staat er toch een houdbaarheidsdatum op?",
                  "Bij een lagere temperatuur raken minder deeltjes boven de activeringsenergie, dus "
                  "verlopen de reacties van bederf trager. Ze stoppen echter niet, en daarom blijft "
                  "er een datum nodig.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemisch-evenwicht-en-de-wet-van-le-chatelier-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Chemisch evenwicht en de wet van Le Chatelier",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Evenwicht of niet",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een evenwicht blijven de concentraties constant.", True),
                 ("waar", "Bij een evenwicht zijn de concentraties van reagentia en producten gelijk.", False),
                 ("waar", "Bij een evenwicht staan de heen- en de terugreactie stil.", False),
                 ("waar", "Een evenwicht kan je van twee kanten bereiken.", True),
             ]),
        dict(kop="De evenwichtsconstante opschrijven",
             opdracht="Schrijf de uitdrukking van K.",
             oefeningen=[
                 ("rij", [(r"H₂ + I₂ ⇌ \(2\) HI", "[HI]² / ([H₂]·[I₂])"),
                          (r"N₂ + \(3\) H₂ ⇌ \(2\) NH₃", "[NH₃]² / ([N₂]·[H₂]³)")],
                  "Welke uitdrukking?", WL),
                 ("rij", [(r"\(2\) SO₂ + O₂ ⇌ \(2\) SO₃", "[SO₃]² / ([SO₂]²·[O₂])"),
                          (r"A + \(2\) B ⇌ \(3\) C", "[C]³ / ([A]·[B]²)")],
                  "Welke uitdrukking?", WL),
             ]),
        dict(kop="Wat zegt de waarde van K?",
             opdracht="Schrijf links, rechts of in het midden.",
             oefeningen=[
                 ("rij", [(r"K = \(1000\)", "rechts"), (r"K = \(1\)", "in het midden"),
                          (r"K = \(0{,}001\)", "links")],
                  "Waar ligt het evenwicht?", WW),
                 ("open", "Een reactie heeft een heel grote K en gebeurt toch niet zichtbaar. Leg uit hoe dat kan.",
                  "K gaat over de verhouding in het evenwicht, niet over de weg ernaartoe. De "
                  "activeringsenergie kan zo hoog zijn dat de reactie zonder vlam of katalysator "
                  "niet op gang komt.", 6),
             ]),
        dict(kop="Welke kant op?",
             opdracht="Schrijf naar links, naar rechts of geen verschuiving.",
             oefeningen=[
                 ("rij", [("extra reagens toevoegen", "naar rechts"),
                          ("product wegnemen", "naar rechts"),
                          ("een katalysator toevoegen", "geen verschuiving")],
                  "Welke kant op?", WL),
                 ("rij", [(r"het volume verkleinen bij N₂ + \(3\) H₂ ⇌ \(2\) NH₃", "naar rechts"),
                          ("de druk verlagen bij diezelfde reactie", "naar links"),
                          (r"de druk verhogen bij H₂ + I₂ ⇌ \(2\) HI", "geen verschuiving")],
                  "Welke kant op?", WL),
                 ("open", "Een evenwicht is exo-energetisch naar rechts. Je verwarmt het. Welke kant gaat het op, en waarom?",
                  "Naar links. Warmte toevoegen is als iets toevoegen aan de kant waar het vrijkomt, "
                  "en het evenwicht werkt dat tegen door de endo-energetische richting te kiezen.", 6),
                 ("open", "Waarom verandert alleen een temperatuurverandering de waarde van K?",
                  "Bij een verandering van concentratie of druk verschuift het evenwicht juist zo "
                  "dat K weer uitkomt. Bij een andere temperatuur hoort een echt andere verhouding, "
                  "en dus een andere waarde van K.", 6),
             ]),
        dict(kop="Q vergelijken met K",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("Q kleiner dan K", "naar rechts"), ("Q groter dan K", "naar links"),
                          ("Q gelijk aan K", "evenwicht")],
                  "Wat gebeurt er?", WW),
             ]),
        dict(kop="Rendement en omzetting",
             opdracht="Reken of leg uit.",
             oefeningen=[
                 ("kort", r"Je haalt \(7{,}5\) g uit een reactie waar \(10\) g mogelijk was. Welk rendement?", r"\(75\,\%\)", W),
                 ("kort", r"Van \(2\) mol beginstof reageert \(0{,}5\) mol. Welke omzettingsgraad?", r"\(25\,\%\)", W),
                 ("open", "Waarom haalt men in de industrie het product voortdurend uit een evenwichtsmengsel?",
                  "Door het product weg te nemen blijft Q kleiner dan K, dus blijft de heenreactie "
                  "doorlopen. Zo reageert er meer van de beginstoffen weg dan wanneer het evenwicht "
                  "gewoon mag stilvallen.", 6),
                 ("open", r"Waarom blijft de omzettingsgraad bij een evenwicht altijd onder \(100\) procent?",
                  "Bij een evenwicht blijft er van elke beginstof iets over: de terugreactie maakt "
                  "ze telkens opnieuw aan. Alleen een aflopende reactie kan een beginstof volledig "
                  "opgebruiken.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-zuren-en-basen-en-het-doorgeven-van-protonen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Zuren en basen en het doorgeven van protonen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Geconjugeerde paren",
             opdracht="Schrijf de geconjugeerde base van het zuur.",
             oefeningen=[
                 ("rij", [("HNO₃", "NO₃⁻"), ("H₂SO₄", "HSO₄⁻"), ("NH₄⁺", "NH₃")],
                  "Welke base?", WW),
                 ("rij", [("H₂O", "OH⁻"), ("H₃O⁺", "H₂O"), ("HCO₃⁻", "CO₃²⁻")],
                  "Welke base?", WW),
             ]),
        dict(kop="En omgekeerd",
             opdracht="Schrijf het geconjugeerde zuur van de base.",
             oefeningen=[
                 ("rij", [("NH₃", "NH₄⁺"), ("OH⁻", "H₂O"), ("CO₃²⁻", "HCO₃⁻")],
                  "Welk zuur?", WW),
                 ("rij", [("CH₃COO⁻", "CH₃COOH"), ("F⁻", "HF"), ("HSO₄⁻", "H₂SO₄")],
                  "Welk zuur?", WW),
             ]),
        dict(kop="Zuur, base of amfolyt",
             opdracht="Schrijf wat het deeltje in water kan zijn.",
             oefeningen=[
                 ("rij", [("H₂O", "amfolyt"), ("HCl", "zuur"), ("NH₃", "base")],
                  "Wat is het?", WW),
                 ("rij", [("HCO₃⁻", "amfolyt"), ("H₃O⁺", "enkel zuur"), ("OH⁻", "base")],
                  "Wat is het?", WW),
                 ("open", "Water is tegenover HCl een base en tegenover ammoniak een zuur. Leg beide reacties uit.",
                  "Met HCl neemt water het proton op en wordt het H₃O⁺, dus is het de base. Met "
                  "ammoniak staat water een proton af en wordt het OH⁻, want NH₃ wordt NH₄⁺; dan is "
                  "water het zuur.", 6),
             ]),
        dict(kop="Waardigheid",
             opdracht="Schrijf hoeveel protonen het zuur kan afstaan of de base kan opnemen.",
             oefeningen=[
                 ("rij", [("HNO₃", r"\(1\)"), ("H₂SO₄", r"\(2\)"), ("H₃PO₄", r"\(3\)")],
                  "Hoeveel?", "90px"),
                 ("rij", [("OH⁻", r"\(1\)"), ("CO₃²⁻", r"\(2\)"), ("PO₄³⁻", r"\(3\)")],
                  "Hoeveel?", "90px"),
             ]),
        dict(kop="Sterk of zwak",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Sterk en geconcentreerd betekenen hetzelfde.", False),
                 ("waar", "Hoe kleiner de pKz, hoe sterker het zuur.", True),
                 ("waar", "De geconjugeerde base van een sterk zuur is een heel zwakke base.", True),
                 ("waar", "Een zwak zuur kan nooit een lage pH geven.", False),
             ]),
        dict(kop="Een zout in water",
             opdracht="Schrijf zuur, basisch of neutraal.",
             oefeningen=[
                 ("rij", [("NaCl", "neutraal"), ("CH₃COONa", "basisch"), ("NH₄Cl", "zuur")],
                  "Hoe reageert de oplossing?", WW),
                 ("rij", [("KNO₃", "neutraal"), ("Na₂CO₃", "basisch"), ("NH₄NO₃", "zuur")],
                  "Hoe reageert de oplossing?", WW),
                 ("open", "Leg uit waarom een oplossing van natriumacetaat basisch is.",
                  "Azijnzuur is een zwak zuur, dus is zijn geconjugeerde base, het acetaation, sterk "
                  "genoeg om een proton van water af te pakken. Daarbij ontstaat OH⁻, en dat maakt "
                  "de oplossing basisch.", 6),
                 ("open", r"Twee bekers van \(0{,}1\) mol/L: één zoutzuur, één azijnzuur. Wat is gelijk en wat verschilt?",
                  "Het aantal mol zuur per liter is gelijk. Zoutzuur ioniseert bijna volledig en "
                  "geeft dus veel meer hydroxoniumionen, dus een veel lagere pH dan het azijnzuur.", 6),
             ]),
        dict(kop="Meten",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("rij", [("geeft een getal", "de pH-meter"), ("geeft een gebied", "de indicator"),
                          ("kleurloos in zuur, roze in base", "fenolftaleïen")],
                  "Wat of welke?", WL),
                 ("open", "Hoe werkt een zuurbase-indicator?",
                  "Ze is zelf een zwak zuur, en haar zuurvorm heeft een andere kleur dan haar "
                  "geconjugeerde base. Welke van de twee overheerst, hangt af van de pH, en rond de "
                  "pKz van de indicator slaat de kleur om.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ph-poh-en-rekenen-met-zuren-en-basen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="pH, pOH en rekenen met zuren en basen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="pH en pOH",
             opdracht=r"Vul de tabel aan. Reken bij \(25^{\circ}\text{C}\).",
             oefeningen=[
                 ("tabel", ["pH", "pOH", "zuur, basisch of neutraal"],
                  [[r"\(3\)", None, None],
                   [None, r"\(1\)", None],
                   [r"\(7\)", None, None],
                   [None, r"\(9\)", None],
                   [r"\(12\)", None, None]],
                  r"pH \(3\): pOH \(11\), zuur · pOH \(1\): pH \(13\), basisch · pH \(7\): pOH \(7\), neutraal · "
                  r"pOH \(9\): pH \(5\), zuur · pH \(12\): pOH \(2\), basisch", W),
             ]),
        dict(kop="Van concentratie naar pH",
             opdracht="Reken uit. Alle zuren en basen hier zijn sterk.",
             oefeningen=[
                 ("rij", [(r"\(0{,}1\) mol/L HCl", r"pH \(1\)"), (r"\(0{,}001\) mol/L HCl", r"pH \(3\)"),
                          (r"\(10^{-5}\) mol/L HCl", r"pH \(5\)")],
                  "Welke pH?", WW),
                 ("rij", [(r"\(0{,}01\) mol/L NaOH", r"pH \(12\)"), (r"\(0{,}1\) mol/L NaOH", r"pH \(13\)"),
                          (r"\(10^{-4}\) mol/L NaOH", r"pH \(10\)")],
                  "Welke pH?", WW),
                 ("kort", r"Welke pH heeft \(0{,}05\) mol/L H₂SO₄ (tweewaardig)?", r"pH \(1\)", W),
             ]),
        dict(kop="Van pH naar concentratie",
             opdracht="Schrijf de concentratie hydroxonium- of hydroxide-ionen.",
             oefeningen=[
                 ("rij", [(r"pH \(4\)", r"[H₃O⁺] = \(10^{-4}\) mol/L"), (r"pH \(9\)", r"[OH⁻] = \(10^{-5}\) mol/L")],
                  "Welke concentratie?", WL),
                 ("rij", [(r"pH \(2\)", r"[H₃O⁺] = \(10^{-2}\) mol/L"), (r"pOH \(3\)", r"[OH⁻] = \(10^{-3}\) mol/L")],
                  "Welke concentratie?", WL),
             ]),
        dict(kop="Hoeveel keer?",
             opdracht="Reken met de logaritmische schaal.",
             oefeningen=[
                 ("rij", [(r"pH \(2\) tegenover pH \(5\)", r"\(1000\) keer"), (r"pH \(3\) tegenover pH \(4\)", r"\(10\) keer"),
                          (r"pH \(1\) tegenover pH \(5\)", r"\(10\,000\) keer")],
                  "Hoeveel keer meer H₃O⁺?", WL),
                 ("open", "Waarom gebruikt men een logaritmische schaal voor de zuurtegraad?",
                  r"De concentratie hydroxoniumionen loopt van ongeveer \(1\) mol/L tot \(10^{-14}\) mol/L, dus "
                  "over veertien machten van tien. Met gewone getallen zou dat onhandelbaar zijn; de "
                  r"logaritme maakt er een handig getal van tussen \(0\) en \(14\).", 6),
             ]),
        dict(kop="Verdunnen en inkoken",
             opdracht="Schrijf wat er met de pH gebeurt.",
             oefeningen=[
                 ("rij", [(r"een sterk zuur \(10\) keer verdunnen", r"pH stijgt \(1\) eenheid"),
                          (r"een sterk zuur \(100\) keer verdunnen", r"pH stijgt \(2\) eenheden")],
                  "Wat gebeurt er?", WL),
                 ("waar", r"Door een sterk zuur heel sterk te verdunnen kan de pH boven \(7\) komen.", False),
                 ("waar", "Inkoken tot de helft van het volume doet de pH van een sterk zuur dalen.", True),
                 ("open", "Leg uit waarom de pH van een zwak zuur niet rechtstreeks uit zijn concentratie volgt.",
                  "Bij een zwak zuur staat maar een deel van de moleculen zijn proton af. Hoeveel "
                  "precies, hangt af van de zuurconstante, dus heb je naast de concentratie ook Kz "
                  "nodig.", 5),
             ]),
        dict(kop="Mengen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", r"Je mengt gelijke volumes \(0{,}1\) mol/L HCl en \(0{,}1\) mol/L NaOH. Welke pH verwacht je, en waarom?",
                  r"pH \(7\). Het aantal mol hydroxonium en hydroxide is precies gelijk, dus reageren ze "
                  "volledig weg tot water. Wat overblijft is natriumchloride, en dat reageert niet "
                  "meer met water.", 6),
                 ("open", "Waarom neutraliseren een zwak en een sterk zuur van dezelfde concentratie evenveel base?",
                  "Het aantal mol zuur bepaalt hoeveel base er nodig is, niet hoe goed het zuur "
                  "ioniseert. Het zwakke zuur staat zijn protonen gewoon één voor één af terwijl de "
                  "base ze wegneemt.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-buffers-en-zuurbasetitraties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Buffers en zuurbasetitraties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Buffert het of niet?",
             opdracht="Schrijf ja of nee, en bij nee waarom niet.",
             oefeningen=[
                 ("rij", [("melkzuur met natriumlactaat", "ja"),
                          ("salpeterzuur met kaliumnitraat", "nee, nitraat is een te zwakke base"),
                          ("ammoniak met ammoniumsulfaat", "ja")],
                  "Buffert het?", WL),
                 ("rij", [("natriumhydroxide met natriumchloride", "nee, een sterke base heeft geen bruikbaar paar"),
                          ("koolzuur met natriumwaterstofcarbonaat", "ja")],
                  "Buffert het?", WL),
             ]),
        dict(kop="Het juiste zuur kiezen",
             opdracht=r"Welk zuur neem je voor die buffer? Kies uit melkzuur (pKz \(3{,}9\)), azijnzuur (pKz \(4{,}8\)), diwaterstoffosfaat (pKz \(7{,}2\)) en ammonium (pKz \(9{,}2\)).",
             oefeningen=[
                 ("rij", [(r"een buffer rond pH \(7\)", "diwaterstoffosfaat"),
                          (r"een buffer rond pH \(9\)", "ammonium"),
                          (r"een buffer rond pH \(4\)", "melkzuur")],
                  "Welk zuur?", WL),
                 ("kort", "Binnen welk gebied werkt een buffer met azijnzuur ongeveer?", r"tussen pH \(3{,}8\) en pH \(5{,}8\)", WL),
             ]),
        dict(kop="Wat gebeurt er in de buffer?",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je giet een beetje natriumhydroxide bij een buffer van azijnzuur en natriumacetaat. Schrijf wat er gebeurt.",
                  "Het azijnzuur van het paar staat zijn proton af aan het hydroxide-ion, zodat er "
                  "water en acetaat ontstaat. De sterke base is daarmee weg en de pH beweegt maar "
                  "een beetje; er is wel iets minder zuur over.", 6),
                 ("open", "Waarom verandert de pH van een buffer bijna niet als je hem met water verdunt?",
                  "De pH hangt af van de verhouding tussen het zuur en zijn geconjugeerde base, en "
                  "water verdunt beide even sterk. Die verhouding blijft dus gelijk; alleen de "
                  "capaciteit, dus hoeveel de buffer kan opvangen, wordt kleiner.", 6),
                 ("open", r"Twee buffers hebben dezelfde pH, maar de ene is \(1\) mol/L en de andere \(0{,}01\) mol/L. Wat verschilt er?",
                  "De capaciteit. De geconcentreerde buffer kan veel meer zuur of base opvangen voor "
                  "hij uitgeput is. De pH is bij het begin gelijk, want die volgt uit de verhouding, "
                  "niet uit de hoeveelheid.", 6),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een buffer werkt het best als zuur en base in dezelfde concentratie zitten.", True),
                 ("waar", "Een buffer houdt de pH precies gelijk, hoeveel zuur je er ook bij giet.", False),
                 ("waar", "Het bloed wordt gebufferd door het paar koolzuur en waterstofcarbonaat.", True),
                 ("waar", "Een uitgeputte buffer herken je aan een pH die plots wegschiet.", True),
             ]),
        dict(kop="Titreren: het glaswerk",
             opdracht="Schrijf welk glaswerk of welke handeling.",
             oefeningen=[
                 ("rij", [("waar het titrans in zit", "de buret"),
                          ("waar de onbekende oplossing in staat", "de erlenmeyer"),
                          (r"waarmee je precies \(25\) mL afmeet", "de pipet")],
                  "Wat?", WL),
                 ("rij", [("waarmee je de buret spoelt", "met titrans"),
                          ("waar je op de meniscus afleest", "aan de onderkant")],
                  "Hoe?", WL),
             ]),
        dict(kop="Titratie rekenen",
             opdracht="Reken uit. Schrijf eerst het aantal mol titrans.",
             oefeningen=[
                 ("kort", r"\(25{,}0\) mL eenwaardig zuur verbruikt \(25{,}0\) mL NaOH van \(0{,}100\) mol/L. Concentratie van het zuur?", r"\(0{,}100\) mol/L", WW),
                 ("kort", r"\(25{,}0\) mL eenwaardig zuur verbruikt \(12{,}5\) mL NaOH van \(0{,}100\) mol/L. Concentratie van het zuur?", r"\(0{,}0500\) mol/L", WW),
                 ("kort", r"\(20{,}0\) mL H₂SO₄ verbruikt \(30{,}0\) mL NaOH van \(0{,}100\) mol/L. Concentratie van het zuur?", r"\(0{,}0750\) mol/L", WW),
                 ("kort", r"\(10{,}0\) mL NaOH verbruikt \(15{,}0\) mL HCl van \(0{,}200\) mol/L. Concentratie van de base?", r"\(0{,}300\) mol/L", WW),
             ]),
        dict(kop="De curve lezen",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("rij", [("sterk zuur met sterke base", r"pH \(7\)"),
                          ("zwak zuur met sterke base", r"boven pH \(7\)"),
                          ("zwakke base met sterk zuur", r"onder pH \(7\)")],
                  "Waar ligt het equivalentiepunt?", WL),
                 ("open", "Waarom ligt er bij de titratie van een zwak zuur een vlak stuk in de curve?",
                  "Halverwege zitten het zwakke zuur en zijn geconjugeerde base samen in de "
                  "erlenmeyer, en dat is een buffer. Die vangt de toegevoegde base op, dus beweegt "
                  "de pH daar maar traag. In het midden van dat stuk is de pH gelijk aan de pKz.", 6),
                 ("open", "Je spoelde de buret met water in plaats van met titrans. Wat gebeurt er met je resultaat, en waarom?",
                  "Het titrans wordt een beetje verdund, dus is er meer volume nodig voor hetzelfde "
                  "aantal mol. Je leest een te groot volume af en berekent dus een te hoge "
                  "concentratie voor het zuur.", 6),
                 ("open", "Hoe kies je een geschikte indicator, en waarom lukt dat bij een heel verdund zuur minder goed?",
                  "Het omslaggebied van de indicator moet binnen de pH-sprong van de curve vallen. "
                  "Bij een verdund zuur is die sprong kleiner en minder steil, dus is er minder "
                  "ruimte waarin de omslag precies samenvalt met het equivalentiepunt.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-oxidatiegetallen-en-redoxreacties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Oxidatiegetallen en redoxreacties",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Oxidatiegetallen van zwavel",
             opdracht="Bepaal het oxidatiegetal van zwavel.",
             oefeningen=[
                 ("rij", [("S₈", r"\(0\)"), ("H₂S", "−II"), ("SO₂", "+IV")],
                  "Welk getal?", W),
                 ("rij", [("SO₃²⁻", "+IV"), ("SO₄²⁻", "+VI"), ("Na₂S", "−II")],
                  "Welk getal?", W),
             ]),
        dict(kop="Oxidatiegetallen van stikstof",
             opdracht="Bepaal het oxidatiegetal van stikstof.",
             oefeningen=[
                 ("rij", [("N₂", r"\(0\)"), ("NH₃", "−III"), ("NO", "+II")],
                  "Welk getal?", W),
                 ("rij", [("NO₂", "+IV"), ("NO₂⁻", "+III"), ("NH₄⁺", "−III")],
                  "Welk getal?", W),
             ]),
        dict(kop="Oxidatiegetallen van chloor en koolstof",
             opdracht="Bepaal het oxidatiegetal van het onderlijnde element.",
             oefeningen=[
                 ("rij", [("chloor in Cl₂", r"\(0\)"), ("chloor in NaCl", "−I"),
                          ("chloor in ClO₄⁻", "+VII")],
                  "Welk getal?", W),
                 ("rij", [("koolstof in CH₃OH", "−II"), ("koolstof in HCOOH", "+II"),
                          ("koolstof in CO", "+II")],
                  "Welk getal?", W),
                 ("open", "Methanol, methanal en methaanzuur: leg uit waarom die reeks een reeks oxidaties is.",
                  "Het oxidatiegetal van koolstof stijgt van −II in methanol naar nul in methanal en "
                  "naar +II in methaanzuur. Elke stap betekent dat koolstof elektronen afstaat, en "
                  "een stijging van het oxidatiegetal is precies de definitie van een oxidatie.", 6),
             ]),
        dict(kop="Oxidatie of reductie",
             opdracht="Schrijf oxidatie of reductie, met het aantal elektronen.",
             oefeningen=[
                 ("rij", [("Mg wordt Mg²⁺", r"oxidatie, \(2\) elektronen af"),
                          (r"Cl₂ wordt \(2\) Cl⁻", r"reductie, \(2\) elektronen op")],
                  "Wat gebeurt er?", WL),
                 ("rij", [("Sn²⁺ wordt Sn⁴⁺", r"oxidatie, \(2\) elektronen af"),
                          ("MnO₄⁻ wordt Mn²⁺", r"reductie, \(5\) elektronen op")],
                  "Wat gebeurt er?", WL),
             ]),
        dict(kop="Oxidator of reductor",
             opdracht="Schrijf wat de stof in die reactie is.",
             oefeningen=[
                 ("rij", [("zink in de reactie met Cu²⁺", "reductor"),
                          ("Cu²⁺ in die reactie", "oxidator"),
                          ("zuurstof bij een verbranding", "oxidator")],
                  "Wat is het?", WW),
                 ("waar", "Een oxidator wordt zelf gereduceerd.", True),
                 ("waar", "Een reductor neemt elektronen op.", False),
                 ("waar", "In een redoxreactie zijn er altijd evenveel afgestane als opgenomen elektronen.", True),
                 ("waar", "Een stof die zuurstof opneemt, wordt gereduceerd.", False),
             ]),
        dict(kop="Gaat het door?",
             opdracht=r"Gebruik deze waarden: Ag⁺/Ag +\(0{,}80\) V · Cu²⁺/Cu +\(0{,}34\) V · Pb²⁺/Pb \(-0{,}13\) V · Zn²⁺/Zn \(-0{,}76\) V · Mg²⁺/Mg \(-2{,}37\) V.",
             oefeningen=[
                 ("rij", [("koper in een zilveroplossing", "ja"),
                          ("zilver in een koperoplossing", "nee"),
                          ("magnesium in een loodoplossing", "ja")],
                  "Gaat het spontaan door?", WW),
                 ("rij", [("lood in een zinkoplossing", "nee"),
                          ("zink in een koperoplossing", "ja")],
                  "Gaat het spontaan door?", WW),
                 ("open", "Leg uit waarom zoutzuur koper niet aantast en salpeterzuur wel.",
                  "Koper staat boven waterstof, dus het hydroxoniumion van zoutzuur is een te zwakke "
                  "oxidator om koper zijn elektronen af te doen staan. Het nitraation van "
                  "salpeterzuur is een sterkere oxidator en kan dat wel; daarbij ontstaat NO of NO₂.", 6),
                 ("open", "Je legt een ijzeren spijker in een kopersulfaatoplossing. Beschrijf wat je ziet en waarom.",
                  "Het ijzer lost op als Fe²⁺ en er slaat roodbruin koper op de spijker neer. IJzer "
                  "staat lager in de tabel en is dus de sterkere reductor, dus staat het zijn "
                  "elektronen af aan de koperionen.", 6),
             ]),
        dict(kop="Opstellen en controleren",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Beschrijf de stappen om een redoxvergelijking op te stellen.",
                  "Eerst de oxidatiegetallen bepalen en zien welke atomen veranderen. Dan de twee "
                  "halfreacties schrijven met hun elektronen, en elk met een factor vermenigvuldigen "
                  "zodat het aantal elektronen gelijk is. Daarna optellen, en met water en H₃O⁺ of "
                  "OH⁻ de atomen en de lading laten kloppen.", 8),
                 ("open", "Welke twee controles doe je op een afgewerkte ionenreactievergelijking?",
                  "Het aantal atomen van elk element moet links en rechts gelijk zijn, en de totale "
                  "lading moet links en rechts gelijk zijn. Die lading hoeft geen nul te zijn, enkel "
                  "gelijk. Er mogen ook geen losse elektronen meer overblijven.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-galvanische-cellen-en-elektrolyse-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Galvanische cellen en elektrolyse",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee cellen naast elkaar",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "galvanische cel", "elektrolyse"],
                  [["de reactie is", None, None],
                   ["de anode is de", None, None],
                   ["de kathode is de", None, None],
                   ["de omzetting is", None, None]],
                  "spontaan / gedwongen · negatieve pool / positieve pool · positieve pool / "
                  "negatieve pool · chemisch naar elektrisch / elektrisch naar chemisch", WW),
                 ("waar", "In beide gevallen gebeurt de oxidatie aan de anode.", True),
                 ("waar", "In beide gevallen is de anode de negatieve pool.", False),
             ]),
        dict(kop="Bronspanning rekenen",
             opdracht=r"Gebruik: Ag⁺/Ag +\(0{,}80\) V · Cu²⁺/Cu +\(0{,}34\) V · Fe²⁺/Fe \(-0{,}44\) V · Zn²⁺/Zn \(-0{,}76\) V · Al³⁺/Al \(-1{,}66\) V.",
             oefeningen=[
                 ("rij", [("zilver en koper", r"\(0{,}46\) V"), ("koper en ijzer", r"\(0{,}78\) V")],
                  "Welke bronspanning?", WW),
                 ("rij", [("zink en zilver", r"\(1{,}56\) V"), ("aluminium en koper", r"\(2{,}00\) V")],
                  "Welke bronspanning?", WW),
                 ("kort", "Welk metaal is de anode in een cel van ijzer en zilver?", "het ijzer", WW),
                 ("kort", "Welk metaal is de kathode in een cel van aluminium en zink?", "het zink", WW),
             ]),
        dict(kop="Waar gebeurt wat?",
             opdracht="Schrijf anode of kathode.",
             oefeningen=[
                 ("rij", [("de oxidatie", "anode"), ("de reductie", "kathode"),
                          ("de elektrode wordt dunner", "anode")],
                  "Waar?", WW),
                 ("rij", [("de elektrode wordt zwaarder", "kathode"),
                          ("de elektronen vertrekken", "anode"),
                          ("de negatieve ionen van de zoutbrug komen toe", "anode")],
                  "Waar?", WW),
             ]),
        dict(kop="De cel beschrijven",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarvoor dient de zoutbrug, en waarom volstaat de draad niet?",
                  "Door de draad lopen enkel elektronen. Aan de anode ontstaan positieve "
                  "metaalionen en aan de kathode verdwijnen ze, dus zou de ene halfcel te positief "
                  "en de andere te negatief worden en zou de reactie stilvallen. De zoutbrug laat "
                  "ionen bewegen en houdt zo beide halfcellen in ladingsevenwicht.", 8),
                 ("open", "Lees de voorstelling Fe/Fe²⁺//Ag⁺/Ag. Wat gebeurt er links en rechts?",
                  "Links staat de anode: ijzer wordt geoxideerd tot Fe²⁺ en staat twee elektronen "
                  "af. Rechts staat de kathode: zilverionen nemen elk een elektron op en slaan als "
                  "zilver neer. De dubbele streep is de zoutbrug.", 6),
                 ("open", "Waarom haal je geen stroom uit een stukje zink dat je gewoon in een kopersulfaatoplossing legt?",
                  "De oxidatie en de reductie gebeuren dan op dezelfde plaats, aan het oppervlak van "
                  "het zink. De elektronen gaan er rechtstreeks over, dus is er geen draad waar ze "
                  "doorheen moeten. Daarvoor moet je de twee halfreacties scheiden in twee "
                  "halfcellen met een zoutbrug ertussen.", 8),
             ]),
        dict(kop="Elektrolyse",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("gesmolten keukenzout, aan de kathode", "natriummetaal"),
                          ("gesmolten keukenzout, aan de anode", "chloorgas")],
                  "Wat ontstaat er?", WL),
                 ("rij", [("water, aan de kathode", "waterstofgas"),
                          ("water, aan de anode", "zuurstofgas")],
                  "Wat ontstaat er?", WL),
                 ("kort", "Waarom werkt elektrolyse niet met vast keukenzout?", "de ionen kunnen er niet bewegen", WL),
                 ("open", "Waarom wordt aluminium met elektrolyse gewonnen en niet met een gewone reactie?",
                  "Aluminium staat heel laag in de tabel van normpotentialen, dus het aluminiumion "
                  "is een heel zwakke oxidator en geeft zijn elektronen niet spontaan terug. Er is "
                  "een spanningsbron nodig om de reductie af te dwingen, en dat kost veel "
                  "elektriciteit.", 6),
             ]),
        dict(kop="Galvaniseren",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je wil een lepel verzilveren. Wat hang je aan de kathode, wat aan de anode, en waarom?",
                  "De lepel komt aan de kathode, want daar gebeurt de reductie en slaat het zilver "
                  "als metaal neer. Aan de anode hangt een stuk zilver, dat langzaam oplost en zo de "
                  "concentratie zilverionen in de oplossing gelijk houdt.", 6),
                 ("open", "Leg uit wat er gebeurt bij het opladen van een oplaadbare batterij.",
                  "Bij het ontladen loopt de spontane redoxreactie van een galvanische cel. Bij het "
                  "opladen duwt een spanningsbron die reactie met een elektrolyse terug, dus is "
                  "opladen een gedwongen reactie die energie kost.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-toepassingen-van-redox-batterijen-galvaniseren-en-corrosie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Toepassingen van redox: batterijen, galvaniseren en corrosie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Batterij, accu of brandstofcel",
             opdracht="Schrijf welke van de drie bij de uitspraak past. Soms passen er twee.",
             oefeningen=[
                 ("rij", [("raakt leeg en is dan weg", "batterij"),
                          ("wordt met een elektrolyse teruggeduwd", "accu"),
                          ("blijft werken zolang je bijvult", "brandstofcel")],
                  "Welke?", WW),
                 ("rij", [("levert gelijkspanning", "alle drie"),
                          ("laat alleen water achter", "brandstofcel"),
                          ("hoort bij het klein gevaarlijk afval", "batterij en accu")],
                  "Welke?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een gewone alkalinebatterij kan je veilig opladen.", False),
                 ("waar", "De anode van een batterij is de negatieve pool.", True),
                 ("waar", "Een batterij kortsluiten is gevaarlijk omdat de reactie dan heel snel loopt.", True),
                 ("waar", "De spanning in volt zegt hoeveel lading er in een batterij zit.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom raakt een batterij leeg en een brandstofcel niet?",
                  "In een batterij zitten de reagentia opgesloten; als minstens één ervan "
                  "opgebruikt is, stopt de redoxreactie en valt de spanning weg. Bij een "
                  "brandstofcel worden het waterstofgas en het zuurstofgas voortdurend "
                  "aangevoerd, dus kan de reactie blijven lopen.", 6),
                 ("open", "Leg uit waarom opladen energie kost en ontladen energie levert.",
                  "Bij het ontladen loopt de spontane redoxreactie van een galvanische cel en komt "
                  "er energie vrij als spanning. Bij het opladen moet een spanningsbron die reactie "
                  "de andere kant op duwen, en dat is een gedwongen reactie, dus een elektrolyse "
                  "die energie verbruikt.", 6),
                 ("open", "Waarom horen oude batterijen niet bij het restafval?",
                  "Ze bevatten zware metalen zoals zink, lithium, nikkel en soms cadmium. Die "
                  "komen bij het verbranden of storten in het milieu terecht. Bij de inzameling "
                  "worden ze teruggewonnen.", 5),
             ]),
        dict(kop="Galvaniseren",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("waar hangt het voorwerp", "aan de kathode"),
                          ("waarvan is de anode", "van het metaal dat je opbrengt"),
                          ("wat gebeurt er met de anode", "ze lost op")],
                  "Wat?", WL),
                 ("kort", "Wat bepaalt hoe dik het laagje wordt?", "hoe lang en hoe sterk de stroom loopt", WL),
                 ("open", "Waarom verzilvert men een lepel in plaats van hem volledig uit zilver te maken?",
                  "Alleen het buitenste laagje bepaalt het uitzicht en de weerstand tegen "
                  "aantasting. Een dun laagje volstaat daarvoor en kost veel minder dan massief "
                  "zilver; de kern mag van een goedkoper metaal zijn.", 5),
             ]),
        dict(kop="Roesten",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Welke twee stoffen heeft ijzer nodig om te roesten?", "zuurstof en water", WL),
                 ("kort", "Is ijzer bij het roesten de oxidator of de reductor?", "de reductor", WW),
                 ("kort", "Waarom roest een auto sneller aan de kust?", "zout maakt het water geleidend", WL),
                 ("waar", "Roest beschermt het ijzer eronder, zoals het oxidelaagje van aluminium.", False),
             ]),
        dict(kop="Beschermen of niet",
             opdracht="Schrijf of het ijzer beschermd wordt, en waarom.",
             oefeningen=[
                 ("rij", [("een laagje zink", "ja, zink is de sterkere reductor"),
                          ("een laagje tin met een kras", "nee, ijzer blijft de reductor"),
                          ("een laagje verf zonder kras", "ja, het sluit lucht en water af")],
                  "Beschermd?", WL),
                 ("rij", [("een magnesiumblok eraan", "ja, het magnesium wordt opgegeten"),
                          ("het ijzer aan de positieve pool leggen", "nee, dan wordt het de anode")],
                  "Beschermd?", WL),
                 ("open", "Leg uit waarom een verzinkt stuk staal ook met een kras erin nog beschermd is, en een verzinkt blik niet.",
                  "Zink is een sterkere reductor dan ijzer, dus staat het zijn elektronen eerst af "
                  "en wordt het zelf geoxideerd in plaats van het ijzer. Tin is een zwakkere "
                  "reductor, dus blijft bij een kras het ijzer de reductor en roest het daar juist "
                  "snel weg.", 8),
                 ("open", "Waarom corrodeert aluminium zo weinig, ook al is het een sterke reductor?",
                  "Het buitenste laagje oxideert meteen, maar dat aluminiumoxide vormt een dichte "
                  "laag die aan het metaal vastzit. Water en zuurstof komen er niet door, dus stopt "
                  "de aantasting daar. Roest is poreus en laat alles door, en daarom gaat roesten "
                  "wel verder.", 8),
                 ("open", "Wat is een verteringselektrode en waarom hoort ze op een onderhoudsschema?",
                  "Het is een blok van een onedeler metaal, meestal magnesium of zink, dat aan het "
                  "staal vastzit en zelf geoxideerd wordt in plaats van het staal. Omdat ze daarbij "
                  "opgebruikt wordt, moet ze af en toe nagekeken en vervangen worden, anders staat "
                  "het staal weer bloot.", 8),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-organische-reacties-substitutie-en-het-radicalaire-mechanisme-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Organische reacties: substitutie en het radicalaire mechanisme",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk reactietype?",
             opdracht="Schrijf substitutie, additie, eliminatie of condensatie.",
             oefeningen=[
                 ("rij", [("een atoom wordt vervangen", "substitutie"),
                          ("er komt iets bij, er gaat niets weg", "additie"),
                          ("er gaat iets weg en er komt een dubbele binding", "eliminatie")],
                  "Welk type?", WL),
                 ("rij", [("twee ketens koppelen en water komt vrij", "condensatie"),
                          ("een alcohol en een carbonzuur geven een ester", "condensatie"),
                          ("methaan en chloorgas onder uv-licht", "substitutie")],
                  "Welk type?", WL),
             ]),
        dict(kop="Welke aanvaller?",
             opdracht="Schrijf radicaal, elektrofiel of nucleofiel.",
             oefeningen=[
                 ("rij", [("bij de chlorering van propaan onder uv-licht", "radicaal"),
                          ("bij de bromering van benzeen met een katalysator", "elektrofiel"),
                          ("bij broomethaan met water", "nucleofiel")],
                  "Wie valt aan?", WW),
                 ("rij", [("bij broomethaan met ammoniak", "nucleofiel"),
                          ("bij de chlorering van cyclohexaan onder uv-licht", "radicaal")],
                  "Wie valt aan?", WW),
             ]),
        dict(kop="De drie stappen",
             opdracht="Schrijf initiatie, propagatie of terminatie.",
             oefeningen=[
                 ("rij", [("Cl₂ wordt onder uv-licht twee chloorradicalen", "initiatie"),
                          ("een chloorradicaal haalt een waterstofatoom van methaan", "propagatie"),
                          ("twee methylradicalen koppelen tot ethaan", "terminatie")],
                  "Welke stap?", WW),
                 ("kort", "Waarom loopt de propagatie als een ketting door?", "er ontstaat telkens een nieuw radicaal", WL),
                 ("kort", "Waarom vindt men bij de chlorering van methaan ook ethaan terug?", "twee methylradicalen koppelen", WL),
             ]),
        dict(kop="Wat ontstaat er?",
             opdracht="Schrijf de producten.",
             oefeningen=[
                 ("rij", [("methaan met chloorgas onder uv-licht", "chloormethaan en HCl"),
                          ("benzeen met broom en een katalysator", "broombenzeen en HBr")],
                  "Welke producten?", WL),
                 ("rij", [("broomethaan met water", "ethanol en een bromide-ion"),
                          ("broomethaan met ammoniak", "een amine en een bromide-ion")],
                  "Welke producten?", WL),
                 ("rij", [("ethanol met azijnzuur", "een ester en water"),
                          ("twee alcoholen samen", "een ether en water")],
                  "Welke producten?", WL),
             ]),
        dict(kop="Splitsen",
             opdracht="Antwoord kort of kruis aan.",
             oefeningen=[
                 ("rij", [("homolytisch", "twee radicalen"), ("heterolytisch", "twee ionen")],
                  "Wat ontstaat er?", WW),
                 ("waar", "Bij een homolytische splitsing houdt elk atoom één elektron van het paar.", True),
                 ("waar", "Bij een heterolytische splitsing ontstaan er twee radicalen.", False),
                 ("waar", "Een radicaal heeft een ongepaard elektron en is daardoor heel reactief.", True),
                 ("waar", "Een nucleofiel brengt zelf een vrij elektronenpaar mee.", True),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom heeft een alkaan uv-licht nodig om te reageren, en een halogeenalkaan niet?",
                  "In een alkaan zijn alle bindingen sigma-bindingen die bijna apolair zijn, dus is "
                  "er geen plaats met een elektronenoverschot of een tekort om aan te vallen. Alleen "
                  "een radicaal lukt, en dat moet eerst met licht of warmte gemaakt worden. In een "
                  "halogeenalkaan trekt het halogeen de elektronen weg, zodat het koolstofatoom "
                  "ernaast lichtpositief is en een nucleofiel er zo op kan.", 8),
                 ("open", "Waarom ondergaat benzeen een substitutie en geen additie met broom?",
                  "De pi-elektronen van de ring zijn over de hele ring verspreid, en dat maakt "
                  "benzeen bijzonder stabiel. Bij een additie zou die verspreide elektronenwolk "
                  "verbroken worden. Bij een substitutie blijft de ring intact, en dat kost dus "
                  "veel minder energie.", 6),
                 ("open", "Waarom heeft de bromering van benzeen een katalysator nodig?",
                  "Een broommolecule is apolair en daardoor niet elektrofiel genoeg om de stabiele "
                  "ring aan te vallen. Een stof als ijzerbromide polariseert het broom, zodat er "
                  "een sterk elektrofiel deeltje ontstaat dat de ring wel aankan.", 6),
                 ("open", "Waarom geeft de chlorering van methaan een mengsel van producten?",
                  "Elk chloormethaan dat ontstaat, kan zelf opnieuw door een chloorradicaal "
                  "aangevallen worden; zo ontstaan ook dichloor-, trichloor- en tetrachloormethaan. "
                  "Daarnaast koppelen radicalen in de terminatie tot nog andere moleculen. De "
                  "opbrengst van één bepaald product blijft daarom beperkt.", 8),
                 ("open", "Wat is hydrolyse van een ester, en wat is het verschil met verzeping?",
                  "Bij hydrolyse valt de ester met water weer uiteen in de alcohol en het "
                  "carbonzuur, met een zuur als katalysator. Bij verzeping gebruik je een base, en "
                  "dan krijg je niet het carbonzuur maar het zout ervan; dat zout is zeep.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-organische-reacties-additie-eliminatie-en-condensatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Organische reacties: additie, eliminatie en condensatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat ontstaat er bij de additie?",
             opdracht="Schrijf het product.",
             oefeningen=[
                 ("rij", [("propeen met diwaterstof", "propaan"),
                          (r"but-\(1\)-een met broom", r"\(1{,}2\)-dibroombutaan"),
                          ("etheen met water en een zuur", "ethanol")],
                  "Welk product?", WL),
                 ("rij", [("ethyn met twee keer diwaterstof", "ethaan"),
                          ("propeen met broomwater", r"\(1{,}2\)-dibroompropaan")],
                  "Welk product?", WL),
             ]),
        dict(kop="De regel van Markownikov",
             opdracht="Welk product overheerst?",
             oefeningen=[
                 ("rij", [("propeen met HCl", r"\(2\)-chloorpropaan"),
                          ("propeen met water", r"propaan-\(2\)-ol"),
                          (r"but-\(1\)-een met HBr", r"\(2\)-broombutaan")],
                  "Welk product?", WL),
                 ("open", "Leg de regel van Markownikov in je eigen woorden uit.",
                  "Bij de additie van een asymmetrische stof over een dubbele binding gaat het "
                  "waterstofatoom naar het koolstofatoom dat er al het meeste heeft. De andere "
                  "groep, het halogeen of de OH-groep, komt dus op het meest vertakte "
                  "koolstofatoom terecht.", 6),
             ]),
        dict(kop="Verzadigingsgraad",
             opdracht="Hoeveel keer kan diwaterstof adderen?",
             oefeningen=[
                 ("rij", [("propaan", r"\(0\)"), ("propeen", r"\(1\)"), ("propyn", r"\(2\)")],
                  "Hoeveel keer?", "90px"),
                 ("kort", "Waarom ontkleurt broomwater bij een alkeen en niet bij een alkaan?", "het broom addeert aan de dubbele binding", WL),
             ]),
        dict(kop="Eliminatie",
             opdracht="Schrijf het product.",
             oefeningen=[
                 ("rij", [("ethanol met geconcentreerd zwavelzuur en warmte", "etheen en water"),
                          ("broomethaan met een base", "etheen en HBr")],
                  "Welk product?", WL),
                 ("rij", [(r"propaan-\(1\)-ol, dehydrogenatie", "propanal"),
                          (r"propaan-\(2\)-ol, dehydrogenatie", "propanon"),
                          (r"butaan-\(2\)-ol, dehydrogenatie", "butanon")],
                  "Welk product?", WL),
                 ("kort", r"Waarom geeft de dehydratatie van butaan-\(2\)-ol twee alkenen?", "het water kan aan twee kanten weggaan", WL),
                 ("open", "Waarom kan een tertiaire alcohol wel een dehydratatie en geen dehydrogenatie ondergaan?",
                  "Voor een dehydrogenatie moet er op het koolstofatoom met de OH-groep nog een "
                  "waterstofatoom zitten, en bij een tertiaire alcohol zitten daar drie "
                  "koolstofketens. Voor een dehydratatie volstaat een waterstofatoom op een "
                  "buuratoom, en dat is er wel.", 6),
             ]),
        dict(kop="Primair, secundair of tertiair",
             opdracht="Schrijf hoeveel koolstofketens er aan het koolstofatoom met de OH-groep zitten, en wat er bij een oxidatie ontstaat.",
             oefeningen=[
                 ("tabel", ["alcohol", "aantal ketens", "product bij oxidatie"],
                  [["primair", None, None], ["secundair", None, None], ["tertiair", None, None]],
                  r"primair: \(1\), aldehyde (en verder carbonzuur) · secundair: \(2\), keton · "
                  r"tertiair: \(3\), geen dehydrogenatie mogelijk", WW),
                 ("kort", "Wat krijg je als je een primaire alcohol volledig oxideert?", "een carbonzuur", WW),
                 ("kort", "Waarom wordt wijn die te lang openstaat azijn?", "de alcohol oxideert tot azijnzuur", WL),
             ]),
        dict(kop="Condensatie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("ethanol met azijnzuur", "een ester en water"),
                          ("twee alcoholen", "een ether en water")],
                  "Welke producten?", WL),
                 ("kort", "Hoe heet de reactie waarbij een ester met water weer uiteenvalt?", "hydrolyse", WW),
                 ("kort", "En met een base in plaats van een zuur?", "verzeping", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een additie gaat de pi-binding open en blijft de sigma-binding staan.", True),
                 ("waar", "Een eliminatie is het omgekeerde van een additie.", True),
                 ("waar", "De additie van water aan een alkeen verloopt zonder katalysator.", False),
                 ("waar", "Een cycloalkeen kan geen additie ondergaan omdat het een ring is.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom verloopt de additie aan een alkeen elektrofiel en die aan een aldehyde nucleofiel?",
                  "Bij een alkeen zijn de twee koolstofatomen gelijk, dus liggen de pi-elektronen "
                  "bloot en trekken ze een deeltje met een elektronentekort aan. Bij een aldehyde "
                  "trekt het zuurstofatoom de elektronen van de C=O-groep naar zich toe, zodat het "
                  "koolstofatoom lichtpositief wordt en net een nucleofiel aantrekt.", 8),
                 ("open", "Waarom is een additie geen substitutie?",
                  "Bij een additie gaat er geen enkel atoom weg: alles van de twee moleculen zit in "
                  "het product. Bij een substitutie verdwijnt er altijd iets uit de oorspronkelijke "
                  "stof, want het wordt vervangen.", 5),
                 ("open", "Hoe maakt men van vloeibare olie een vaster vet, en hoe heet die reactie?",
                  "Door diwaterstof te laten adderen aan de dubbele bindingen in de olie, met een "
                  "katalysator van nikkel of platina. Die reactie heet hydrogenering; de ketens "
                  "worden daardoor verzadigd en liggen beter tegen elkaar, dus is het vet vaster.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kunststoffen-polymeren-en-hun-eigenschappen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunststoffen: polymeren en hun eigenschappen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van monomeer naar kunststof",
             opdracht="Schrijf welke kunststof uit dat monomeer komt.",
             oefeningen=[
                 ("rij", [("etheen", "PE"), ("propeen", "PP"), ("chlooretheen", "PVC")],
                  "Welke kunststof?", WW),
                 ("rij", [("fenyletheen", "PS"), ("tetrafluoretheen", "PTFE")],
                  "Welke kunststof?", WW),
             ]),
        dict(kop="En omgekeerd",
             opdracht="Schrijf het monomeer, of de twee monomeersoorten.",
             oefeningen=[
                 ("rij", [("PE", "etheen"), ("PVC", "chlooretheen"), ("PS", "fenyletheen")],
                  "Welk monomeer?", WW),
                 ("rij", [("PET", "een tweewaardige alcohol en een tweewaardig zuur"),
                          ("nylon", "een tweewaardig zuur en een tweewaardig amine")],
                  "Welke monomeren?", WL),
             ]),
        dict(kop="Polyadditie of polycondensatie",
             opdracht="Schrijf welke van de twee, en wat er eventueel vrijkomt.",
             oefeningen=[
                 ("rij", [("PE", "polyadditie, geen bijproduct"),
                          ("PET", "polycondensatie, water"),
                          ("PVC", "polyadditie, geen bijproduct")],
                  "Welke reactie?", WL),
                 ("rij", [("nylon", "polycondensatie, water"),
                          ("PS", "polyadditie, geen bijproduct")],
                  "Welke reactie?", WL),
                 ("open", "Waarom is de atoomeconomie van een polyadditie hoger dan die van een polycondensatie?",
                  "Bij een polyadditie gaan de dubbele bindingen open en koppelen de monomeren "
                  "zonder dat er iets wegvalt, dus zit alle massa van de monomeren in het polymeer. "
                  "Bij een polycondensatie gaat er bij elke koppeling een watermolecule uit, en die "
                  "massa is dus verloren voor het product.", 6),
             ]),
        dict(kop="Thermoplast, thermoharder of elastomeer",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["soort", "aantal crosslinks", "wat bij verwarmen"],
                  [["thermoplast", None, None],
                   ["elastomeer", None, None],
                   ["thermoharder", None, None]],
                  "thermoplast: geen, wordt zacht en is opnieuw te vormen · elastomeer: enkele, "
                  "blijft veerkrachtig · thermoharder: veel, ontleedt zonder te smelten", WW),
                 ("rij", [("gevulkaniseerd rubber", "elastomeer"),
                          ("een plastic zak", "thermoplast"),
                          ("een tandwiel dat warm wordt", "thermoharder")],
                  "Welke soort?", WW),
             ]),
        dict(kop="Welke kunststof kies je?",
             opdracht="Schrijf de kunststof.",
             oefeningen=[
                 ("rij", [("een drankfles", "PET"), ("een afvoerbuis", "PVC"),
                          ("een antikleeflaag", "PTFE")],
                  "Welke kunststof?", WW),
                 ("rij", [("isolatieschuim", "PUR"), ("touw of kleding", "PA of nylon"),
                          ("een beschermende verpakking", "PS-schuim")],
                  "Welke kunststof?", WW),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een monomeer voor een polyadditie moet een dubbele binding hebben.", True),
                 ("waar", "Een kunststof heeft een scherp smeltpunt, zoals een zout.", False),
                 ("waar", "Een thermoplast is beter te recycleren dan een thermoharder.", True),
                 ("waar", "PVC en PE hebben hetzelfde monomeer.", False),
             ]),
        dict(kop="Uitleggen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom heeft een kunststof geen smeltpunt maar een smelttraject?",
                  "De ketens zijn niet alle even lang; er zitten duizenden monomeren in, maar niet "
                  "telkens hetzelfde aantal. Daardoor hebben de ketens niet dezelfde molaire massa "
                  "en laten ze niet allemaal bij dezelfde temperatuur los, dus smelt het materiaal "
                  "over een gebied.", 6),
                 ("open", "Hoe zoek je het monomeer terug uit de structuur van een polymeer van een polyadditie?",
                  "Je zoekt het stukje dat zich herhaalt, de repeterende eenheid, en zet daar de "
                  "dubbele binding terug in. Bij PVC is die eenheid CH₂-CHCl, en met de dubbele "
                  "binding erbij is dat chlooretheen.", 6),
                 ("open", "Waarom geeft gemengde kunststof een materiaal van mindere kwaliteit?",
                  "De verschillende soorten mengen niet goed en hebben elk een ander smelttraject, "
                  "dus is het hergebruikte materiaal minder sterk en niet meer geschikt voor de "
                  "oorspronkelijke toepassing. Dat heet downcycling, en daarom is sorteren zo "
                  "belangrijk.", 6),
                 ("open", "Waarom blijven microplastics zo lang in het milieu?",
                  "De koolstofketens van een kunststof zijn heel stabiel, en bacteriën hebben geen "
                  "enzymen om ze af te breken. De deeltjes brokkelen enkel kleiner en kleiner, en "
                  "komen zo in het water en in de voedselketen terecht.", 6),
                 ("open", "Waarom is vulkaniseren nodig voor een autoband?",
                  "Natuurrubber is kleverig en vervormt blijvend. Door bruggen van zwavel tussen de "
                  "ketens te maken wordt het een elastomeer: het kan nog uitrekken, maar veert "
                  "daarna terug in zijn vorm.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-nanomaterialen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Nanomaterialen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Nanomaat",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Hoeveel meter is één nanometer?", "een miljardste meter", WL),
                 ("kort", "Tussen welke twee grenzen in nanometer ligt een nanomateriaal?", r"tussen \(1\) en \(100\) nm", WL),
                 ("kort", "Welk toestel heb je nodig om zo'n deeltje te zien?", "een elektronenmicroscoop", WL),
                 ("waar", "Nanodeeltjes zijn met een gewone lichtmicroscoop goed te zien.", False),
             ]),
        dict(kop="Hoeveel dimensies?",
             opdracht="Schrijf 0D, 1D, 2D of 3D.",
             oefeningen=[
                 ("rij", [("een quantumdot", "0D"), ("een koolstofnanobuis", "1D"),
                          ("grafeen", "2D")],
                  "Welke soort?", W),
                 ("rij", [("een gewoon materiaal met een nanostructuur erin", "3D"),
                          ("een buckyball", "0D"), ("een nanodraad", "1D")],
                  "Welke soort?", W),
             ]),
        dict(kop="Top-down of bottom-up",
             opdracht="Schrijf welke van de twee.",
             oefeningen=[
                 ("rij", [("een vaste stof fijnmalen", "top-down"),
                          ("uit losse atomen opbouwen", "bottom-up"),
                          ("een laag wegetsen tot een nanopatroon", "top-down")],
                  "Welke methode?", WW),
                 ("rij", [("moleculen zichzelf laten ordenen", "bottom-up"),
                          ("een blok verpulveren", "top-down")],
                  "Welke methode?", WW),
             ]),
        dict(kop="Oppervlak en volume",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom wordt de verhouding oppervlak tot volume groter als een deeltje kleiner wordt?",
                  "Het oppervlak groeit met het kwadraat van de afmeting en het volume met de derde "
                  "macht. Maak je het deeltje kleiner, dan daalt het volume dus veel sneller dan "
                  "het oppervlak, en blijft er per gram veel meer oppervlak over.", 6),
                 ("open", "Waarom is een nanodeeltje van een metaal reactiever dan een blok van hetzelfde metaal?",
                  "Een reactie gebeurt aan het oppervlak, en bij nanodeeltjes zit er per gram veel "
                  "meer oppervlak. Bovendien zit een groot deel van de atomen aan de buitenkant, en "
                  "die hebben minder buren en zitten dus losser.", 6),
                 ("open", "Waarom smelt nanogoud bij een lagere temperatuur dan een goudklomp?",
                  "In een nanodeeltje zit een groot deel van de atomen aan het oppervlak, met minder "
                  "buren om zich aan vast te houden. Er is dus minder energie nodig om ze los te "
                  "maken, en dat betekent een lager smeltpunt.", 6),
             ]),
        dict(kop="Waarvoor gebruikt men het?",
             opdracht="Schrijf welke nanostof of welk nanomateriaal.",
             oefeningen=[
                 ("rij", [("uv-licht tegenhouden in zonnecrème", "zinkoxide of titaandioxide"),
                          ("antibacterieel verband en sokken", "zilver"),
                          ("de gekleurde streep in een sneltest", "goud")],
                  "Wat?", WL),
                 ("rij", [("een buigbaar, doorzichtig en geleidend scherm", "grafeen"),
                          ("een licht materiaal veel sterker maken", "koolstofnanobuizen"),
                          ("een kleur in een beeldscherm", "een quantumdot")],
                  "Wat?", WL),
             ]),
        dict(kop="Waar of niet waar",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een nanomateriaal heeft altijd dezelfde eigenschappen als dezelfde stof in het groot.", False),
                 ("waar", "Een nanomateriaal kan magnetisch zijn terwijl de stof in het groot dat niet is.", True),
                 ("waar", "Nanoplastics zijn kleiner dan microplastics.", True),
                 ("waar", "Nanotechnologie zit nog in geen enkel product in de winkel.", False),
             ]),
        dict(kop="Voordelen en risico's",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom is goud op nanomaat niet goudkleurig?",
                  "De kleur van een metaal komt van de manier waarop zijn elektronen op licht "
                  "reageren. In een deeltje van een paar nanometer zijn de elektronen zo opgesloten "
                  "dat ze op andere golflengten reageren, en dan ziet het deeltje bijvoorbeeld rood "
                  "of paars.", 6),
                 ("open", "Noem een voordeel en een risico van een nanokatalysator.",
                  "Het voordeel is dat er door het grote oppervlak per gram veel minder materiaal "
                  "nodig is voor hetzelfde effect, wat kosten en grondstoffen spaart. Het risico is "
                  "dat zulke kleine deeltjes in het lichaam tot in de cellen kunnen komen en dat "
                  "hun effect op gezondheid en milieu nog niet overal onderzocht is.", 8),
                 ("open", "Waarom staat er nano op het etiket van sommige cosmetica?",
                  "Zo weet de koper dat er deeltjes op nanomaat in het product zitten. Die kunnen "
                  "zich anders gedragen dan dezelfde stof in het groot, en in een product zijn ze "
                  "moeilijk te meten of te volgen.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-duurzame-chemie-en-de-circulaire-economie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Duurzame chemie en de circulaire economie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Drie modellen",
             opdracht="Schrijf lineair, keten of circulair.",
             oefeningen=[
                 ("rij", [("grondstof, product, gebruik, afval", "lineair"),
                          ("veel hergebruik maar toch nog afval", "keten"),
                          ("het afval van het ene is de grondstof van het volgende", "circulair")],
                  "Welk model?", WW),
                 ("kort", "Welke Engelse uitdrukking hoort bij de circulaire economie?", "cradle to cradle", WL),
                 ("kort", "En bij de lineaire?", "cradle to grave", WL),
             ]),
        dict(kop="De ladder van Lansink",
             opdracht="Zet de treden in de goede volgorde, van de beste bovenaan naar de slechtste onderaan: hergebruik, preventie, storten, recyclage, verbranden.",
             oefeningen=[
                 ("tabel", ["plaats", "trede"],
                  [[r"\(1\) (beste)", None], [r"\(2\)", None], [r"\(3\)", None], [r"\(4\)", None], [r"\(5\) (slechtste)", None]],
                  "preventie, hergebruik, recyclage, verbranden, storten", WL),
                 ("kort", "Waarom staat preventie bovenaan?", "afval dat nooit ontstaat, hoeft nooit verwerkt", WL),
                 ("kort", "Hoe heet recycleren tot een product van mindere kwaliteit?", "downcycling", WW),
             ]),
        dict(kop="Bio-woorden uit elkaar houden",
             opdracht="Schrijf wat het woord betekent.",
             oefeningen=[
                 ("rij", [("biogebaseerd", "de grondstof komt uit biomassa"),
                          ("biodegradeerbaar", "micro-organismen breken het af"),
                          ("composteerbaar", "afbreekbaar binnen een vastgelegde tijd en temperatuur")],
                  "Wat betekent het?", WL),
                 ("waar", "Een biogebaseerde kunststof is daarom ook biodegradeerbaar.", False),
                 ("waar", "Composteerbaar is strenger dan biodegradeerbaar.", True),
             ]),
        dict(kop="Waterstof met een kleur",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("elektrolyse met stroom uit wind of zon", "groen"),
                          ("uit aardgas, CO₂ komt vrij", "grijs"),
                          ("uit aardgas, CO₂ wordt afgevangen", "blauw")],
                  "Welke kleur?", WW),
                 ("waar", "Waterstof is bij elke kleur precies dezelfde stof.", True),
             ]),
        dict(kop="Water met een kleur",
             opdracht="Schrijf wit, grijs of zwart.",
             oefeningen=[
                 ("rij", [("drinkbaar water", "wit"), ("water van bad en wasmachine", "grijs"),
                          ("water uit het toilet", "zwart")],
                  "Welke soort?", WW),
             ]),
        dict(kop="Atoomeconomie",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("kort", "Wat meet de atoomeconomie?", "welk deel van de massa in het product zit", WL),
                 ("kort", "Welke atoomeconomie heeft een additie zonder bijproduct?", r"\(100\,\%\)", W),
                 ("open", "Leg uit waarom een hoog rendement en een hoge atoomeconomie niet hetzelfde zijn.",
                  "Het rendement zegt hoeveel je van het mogelijke product echt uit de reactie "
                  "haalt. De atoomeconomie zegt welk deel van de massa van de reagentia volgens de "
                  "reactievergelijking überhaupt in het product belandt. Een condensatie kan dus "
                  r"een rendement van \(95\) procent hebben en toch een matige atoomeconomie, want er "
                  "gaat bij elke koppeling water weg.", 8),
             ]),
        dict(kop="Groene chemie",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom is een solvent dikwijls het grootste milieuprobleem van een synthese?",
                  "Er gaat meestal veel meer solvent in de reactie dan reagens, soms tientallen "
                  "keren zo veel. Dat solvent komt niet in het product terecht, dus moet het "
                  "achteraf afgescheiden, gezuiverd of verwerkt worden.", 6),
                 ("open", "Waarom helpt katalyse de groene chemie?",
                  "Een katalysator wordt niet opgebruikt: hij verlaagt de activeringsenergie en komt "
                  "er na de reactie weer uit. Zo kan de reactie bij een lagere temperatuur en met "
                  "minder energie lopen, en kan hij vaak selectiever gemaakt worden, zodat er minder "
                  "bijproducten ontstaan.", 6),
                 ("open", "Hoe herken je greenwashing aan een verpakking?",
                  "Aan vage woorden als natuurlijk, eco of groen zonder cijfer of keurmerk erbij, en "
                  "aan een groene verpakking of een blaadje in het logo, wat niets zegt over de "
                  "inhoud. Een echte claim noemt wat er precies gemeten is en waartegen.", 6),
                 ("open", "Welke twee keuzes in het ontwerp van een product maken het geschikter voor een kringloop?",
                  "De onderdelen moeten weer van elkaar los kunnen, zodat je ze apart kan "
                  "hergebruiken of recycleren. En er moeten zo weinig verschillende materialen in "
                  "zitten, want een mengsel geeft bij recyclage een materiaal van mindere "
                  "kwaliteit.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-werken-meetinstrumenten-en-beduidende-cijfers-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig werken, meetinstrumenten en beduidende cijfers",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="H-zin of P-zin",
             opdracht="Schrijf H of P.",
             oefeningen=[
                 ("rij", [("veroorzaakt ernstige brandwonden", "H"),
                          ("beschermende handschoenen dragen", "P"),
                          ("giftig bij inslikken", "H")],
                  "Welke soort zin?", W),
                 ("rij", [("bij contact met de ogen: voorzichtig afspoelen met water", "P"),
                          ("schadelijk voor in het water levende organismen", "H")],
                  "Welke soort zin?", W),
                 ("kort", "Waarvoor staat de H van H-zin?", "hazard, dus gevaar", WL),
             ]),
        dict(kop="Welk glaswerk?",
             opdracht="Schrijf welk glaswerk je gebruikt.",
             oefeningen=[
                 ("rij", [(r"precies \(500{,}0\) mL oplossing aanmaken", r"een maatkolf van \(500\) mL"),
                          (r"precies \(25\) mL overbrengen", "een volumetrische pipet"),
                          ("een volume aflezen tot op honderdsten bij een titratie", "een buret")],
                  "Welk glaswerk?", WL),
                 ("rij", [(r"ongeveer \(100\) mL water bijgieten", "een maatcilinder of bekerglas"),
                          ("de oplossing die je titreert", "een erlenmeyer")],
                  "Welk glaswerk?", WL),
                 ("kort", "Waar lees je het volume af?", "aan de onderkant van de meniscus", WL),
             ]),
        dict(kop="Veilig werken",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Je giet het zuur bij het water, niet het water bij het zuur.", True),
                 ("waar", "Een pipet spoel je eerst met de oplossing die je gaat pipetteren.", True),
                 ("waar", "De gevarenpictogrammen zijn ronde groene tekens.", False),
                 ("waar", "Een stof met het uitroeptekenpictogram is altijd dodelijk giftig.", False),
                 ("open", "Je morst een beetje zuur op de werktafel. Beschrijf hoe je dat opruimt.",
                  "Eerst neutraliseren met een zwakke base, bijvoorbeeld natriumwaterstofcarbonaat, "
                  "zodat er geen bijtende vloeistof meer ligt. Daarna het geheel opnemen en bij het "
                  "juiste afval afvoeren, met handschoenen en bril aan.", 6),
             ]),
        dict(kop="Meetbereik en resolutie",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("rij", [("de kleinste en grootste waarde die het toestel meet", "het meetbereik"),
                          ("de kleinste stap die het kan onderscheiden", "de resolutie")],
                  "Hoe heet dat?", WL),
                 ("open", r"Waarom meet je \(5\) mL niet af in een maatcilinder van \(500\) mL?",
                  "De streepjes van zo'n grote cilinder staan veel te ver uit elkaar voor zo'n klein "
                  r"volume, dus is de resolutie veel te grof. De onzekerheid op je \(5\) mL zou dan "
                  "groter zijn dan wat je wil meten.", 6),
             ]),
        dict(kop="Voorvoegsels",
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [(r"\(1\) mm in micrometer", r"\(1000\) µm"), (r"\(1\) kg in gram", r"\(1000\) g"),
                          (r"\(1\) MJ in joule", r"\(1\,000\,000\) J")],
                  "Hoeveel?", WW),
                 ("rij", [(r"\(2{,}5\) nm in meter", r"\(2{,}5\cdot10^{-9}\) m"), (r"\(0{,}5\) mL in liter", r"\(5\cdot10^{-4}\) L"),
                          (r"\(300\) mg in gram", r"\(0{,}300\) g")],
                  "Hoeveel?", WW),
                 ("kort", "Wat is de SI-basiseenheid van stofhoeveelheid?", "de mol", WW),
                 ("kort", "En van temperatuur?", "de kelvin", WW),
             ]),
        dict(kop="Beduidende cijfers",
             opdracht="Hoeveel beduidende cijfers?",
             oefeningen=[
                 ("rij", [(r"\(0{,}00310\)", r"\(3\)"), (r"\(45{,}0\)", r"\(3\)"), (r"\(1200\)", r"\(2\) (zonder komma)")],
                  "Hoeveel?", WW),
                 ("rij", [(r"\(2{,}5\cdot10^{4}\)", r"\(2\)"), (r"\(0{,}0008\)", r"\(1\)"), (r"\(10{,}04\)", r"\(4\)")],
                  "Hoeveel?", WW),
             ]),
        dict(kop="Rekenen met meetwaarden",
             opdracht="Schrijf het resultaat met het juiste aantal cijfers.",
             oefeningen=[
                 ("rij", [(r"\(3{,}2 \cdot 1{,}478\)", r"\(4{,}7\)"), (r"\(25{,}0\) ÷ \(4{,}0\)", r"\(6{,}3\)")],
                  "Welk resultaat?", WW),
                 ("rij", [(r"\(14{,}25\) g + \(0{,}3\) g", r"\(14{,}6\) g"), (r"\(8{,}0\) cm + \(0{,}125\) cm", r"\(8{,}1\) cm")],
                  "Welk resultaat?", WW),
                 ("open", "Leg uit waarom je bij optellen een andere regel volgt dan bij vermenigvuldigen.",
                  "Bij optellen bepaalt de meetwaarde met het minst aantal decimalen hoe precies de "
                  "som kan zijn, want de onzekerheid zit op die decimaal. Bij vermenigvuldigen "
                  "bepaalt de meetwaarde met het minst aantal beduidende cijfers de nauwkeurigheid, "
                  "want daar werkt de relatieve onzekerheid door.", 8),
             ]),
        dict(kop="Wetenschappelijke notatie en evenredigheid",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [(r"\(0{,}000\,058\)", r"\(5{,}8\cdot10^{-5}\)"), (r"\(342\,000\)", r"\(3{,}42\cdot10^{5}\)")],
                  "In wetenschappelijke notatie?", WW),
                 ("rij", [("een rechte door de oorsprong", "recht evenredig"),
                          ("het product van de twee blijft constant", "omgekeerd evenredig")],
                  "Welk verband?", WL),
                 ("kort", "Welke eenheid krijg je als je gram deelt door milliliter?", "g/mL", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Wetenschappelijk onderzoek, ontwerpen en STEM",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Een proef uit elkaar halen",
             opdracht="Je onderzoekt of een hogere concentratie zuur een stukje kalk sneller doet oplossen. Vul in.",
             oefeningen=[
                 ("tabel", ["onderdeel", "wat bij deze proef"],
                  [["onafhankelijke variabele", None],
                   ["afhankelijke variabele", None],
                   ["twee constante variabelen", None],
                   ["controleproef", None]],
                  "de concentratie van het zuur · de tijd tot het kalk op is · de massa en vorm van "
                  "het kalk, en de temperatuur · hetzelfde stukje kalk in zuiver water", WL),
                 ("open", "Schrijf een goede onderzoeksvraag en een hypothese voor die proef.",
                  "Onderzoeksvraag: hoe beïnvloedt de concentratie van het zuur de tijd waarin een "
                  r"stukje kalk van \(1\) gram volledig oplost? Hypothese: bij een hogere concentratie "
                  "lost het kalk sneller op, want er zijn per liter meer hydroxoniumionen, en dus "
                  "meer botsingen per seconde.", 8),
             ]),
        dict(kop="Begrippen",
             opdracht="Schrijf het begrip.",
             oefeningen=[
                 ("rij", [("wijkt altijd naar dezelfde kant af", "een systematische fout"),
                          ("wisselt van meting tot meting", "een toevallige fout"),
                          ("wijkt sterk af van de andere metingen", "een uitschieter")],
                  "Welk begrip?", WL),
                 ("rij", [("ligt dicht bij de echte waarde", "nauwkeurig"),
                          ("de metingen liggen dicht bij elkaar", "precies"),
                          ("iemand anders krijgt hetzelfde resultaat", "reproduceerbaar")],
                  "Welk begrip?", WL),
                 ("kort", "Hoe heet het nakijken door vakgenoten voor een artikel verschijnt?", "peer review", WL),
             ]),
        dict(kop="Mag dat of niet?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Je mag een meting die niet in je verwachting past, gewoon weglaten.", False),
                 ("waar", "Een hypothese die verworpen wordt, maakt het onderzoek waardeloos.", False),
                 ("waar", "Een grafiek hoort een titel en op beide assen een eenheid te krijgen.", True),
                 ("waar", "Je noteert ook wat er misliep tijdens de proef.", True),
             ]),
        dict(kop="Onderzoeken of ontwerpen",
             opdracht="Schrijf onderzoeken of ontwerpen.",
             oefeningen=[
                 ("rij", [(r"hoe snel lost dit zout op bij \(40^{\circ}\text{C}\)", "onderzoeken"),
                          ("maak een houder die een ei een val van twee meter laat overleven", "ontwerpen"),
                          ("welke isolatie houdt het water het langst warm", "onderzoeken")],
                  "Wat is het?", WW),
                 ("kort", "Wat zoekt onderzoeken, en wat zoekt ontwerpen?", "kennis tegenover een oplossing", WL),
             ]),
        dict(kop="Criterium of randvoorwaarde",
             opdracht="Schrijf criterium of randvoorwaarde.",
             oefeningen=[
                 ("rij", [(r"de houder weegt minder dan \(100\) gram", "criterium"),
                          ("je hebt maar één lesuur", "randvoorwaarde"),
                          (r"het water blijft minstens \(20\) minuten boven \(50^{\circ}\text{C}\)", "criterium")],
                  "Wat is het?", WW),
                 ("rij", [("je mag enkel materiaal uit de klas gebruiken", "randvoorwaarde"),
                          ("het budget is tien euro", "randvoorwaarde")],
                  "Wat is het?", WW),
                 ("kort", "Waarom schrijf je criteria meetbaar op?", "dan kan je nagaan of het ontwerp eraan voldoet", WL),
             ]),
        dict(kop="Het ontwerpproces",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom splits je een ontwerpopdracht in deelproblemen?",
                  "Elk stuk kan je dan apart oplossen en apart testen. Zo weet je bij een mislukking "
                  "waar het precies fout gaat, in plaats van alleen te zien dat het geheel niet "
                  "werkt.", 5),
                 ("open", "Wat doe je als je prototype niet aan de criteria voldoet?",
                  "Je gaat na op welk criterium het faalt en waar dat aan ligt, past dat onderdeel "
                  "aan en test opnieuw. Meerdere rondes horen bij ontwerpen; één poging is "
                  "zelden genoeg.", 5),
                 ("open", "Waarvoor staan de vier letters van STEM?",
                  "Science, technology, engineering en mathematics, dus wetenschap, techniek, "
                  "ingenieurswerk en wiskunde. In een STEM-opdracht komen die vier samen in één "
                  "vraag.", 5),
             ]),
        dict(kop="Van labo naar fabriek",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom is opschalen van een laboproef naar een fabriek niet vanzelfsprekend?",
                  "In het groot gedragen warmte en menging zich anders: een grote reactor verliest "
                  "per liter veel minder warmte aan zijn omgeving en is veel moeilijker gelijkmatig "
                  "te roeren. Een reactie die in een reageerbuis mooi liep, kan in het groot dus "
                  "oplopen of maar deels doorlopen.", 8),
                 ("open", "Noem drie vragen die horen bij het beoordelen van een nieuwe chemische toepassing.",
                  "Wat gebeurt er met de stof na gebruik? Wie draagt het risico en wie het voordeel? "
                  "En weegt het voordeel op tegen wat het kan kosten aan gezondheid, milieu of geld? "
                  "Daar hoort ook de kostprijs van het proces bij, want die bepaalt mee of het "
                  "ooit gebruikt wordt.", 8),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-anorganische-stoffen-stofklassen-en-naamgeving-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de formule van rechts naar links. Eindigt ze op O en verder niets, dan "
                   "is het een oxide; eindigt ze op OH, dan een hydroxide; begint ze met H, dan "
                   "een zuur; staat er een metaal voor een zuurrest, dan een zout. Vier vormen, "
                   "vier kenmerken.",
            waarom=[
                "Zet de drie naast elkaar: dezelfde kalium, drie keer iets anders erachter. Zo "
                "zie je dat de stofklasse niet van het metaal komt maar van wat eraan hangt.",
                None,
                "HBr is de valkuil in deze rij: er zit geen zuurstof in en het is toch een zuur, "
                "want het begint met waterstof. Zo'n zuur zonder zuurstof heet een hydrozuur.",
            ],
        ),
        dict(
            aanpak="Tel het aantal verschillende elementen, niet het aantal atomen. Twee "
                   "verschillende elementen is binair, drie is ternair, vier of meer heeft geen "
                   "van die twee namen.",
            waarom=[
                None,
                "KHCO₃ heeft vier verschillende elementen: kalium, waterstof, koolstof en "
                "zuurstof. Daarom valt het buiten binair en ternair.",
                "Dit is de kernvraag van de reeks. Noem een voorbeeld met cijfers erbij, zoals "
                "Fe₂O₃ met vijf atomen en twee elementen. Verschillende soorten tellen, niet "
                "stuks.",
            ],
        ),
        dict(
            aanpak="Vier bijzondere gevallen met elk een eigen kenteken: O₂ als groep betekent "
                   "peroxide, een punt met water erachter betekent hydraat, NH₄ vooraan betekent "
                   "ammoniumzout, en een H tussen het metaal en de zuurrest betekent "
                   "waterstofzout.",
            waarom=[
                "Houd Na₂O₂ en Na₂O uit elkaar: twee zuurstofatomen aan elkaar gebonden maken het "
                "een peroxide, één zuurstofatoom een gewoon oxide.",
                "Het punt in MgSO₄·7H₂O is geen vermenigvuldiging maar betekent kristalwater: "
                "zeven watermoleculen zitten in het kristalrooster mee ingebouwd. Verwarm je het, "
                "dan gaat dat water eruit.",
                "Niet waar, en dat is net het bijzondere aan een peroxide. Zuurstof heeft daar "
                "oxidatiegetal −I, omdat de twee zuurstofatomen aan elkaar gebonden zitten.",
                "Waar, en dat is het eigenaardige van een ammoniumzout: NH₄⁺ gedraagt zich als een "
                "metaalion zonder er een te zijn. Daarom staat het in de tabel bij de positieve "
                "ionen.",
            ],
        ),
        dict(
            aanpak="Tel de waterstofatomen vooraan bij een zuur en de OH-groepen bij een "
                   "hydroxide. Dat getal heet de waardigheid, en het zegt hoeveel protonen het "
                   "zuur kan afstaan of hoeveel hydroxide-ionen er vrijkomen.",
            waarom=[
                "Let op dat je enkel de waterstof vooraan telt. In ethaanzuur CH₃COOH staan er "
                "vier waterstofatomen en kan er maar één af, want de andere drie zitten aan "
                "koolstof.",
                "Bij een hydroxide staat het getal in de index na de haakjes: Ca(OH)₂ heeft twee "
                "OH-groepen. Daarom reageert één mol Ca(OH)₂ met twee mol HCl, en dat heb je nodig "
                "bij een titratie.",
            ],
        ),
        dict(
            aanpak="Hier moet je de triviale namen kennen die in een labo en in een winkel "
                   "gebruikt worden. Zet bij elke naam de formule en bij elke formule de "
                   "systematische naam, zodat je beide richtingen kan.",
            waarom=[
                "Houd de drie kalkvormen uit elkaar: CaO is ongebluste kalk, Ca(OH)₂ is gebluste "
                "kalk en CaCO₃ is kalksteen. Blussen is dus water toevoegen aan CaO, en dat komt "
                "met veel warmte vrij.",
                "Blauwzuur HCN en lachgas N₂O zijn namen die niets over hun formule verraden, dus "
                "moet je ze uit het hoofd kennen.",
                "Let op de symbolen die van de Latijnse naam komen: K van kalium, Pb van plumbum, "
                "Cu van cuprum. Die drie worden het vaakst verward.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over het waarom achter de naamgeving. Geef telkens de regel "
                   "én een voorbeeld, want een regel zonder voorbeeld wordt zelden volledig "
                   "aangerekend.",
            waarom=[
                "Noem beide: wat het cijfer betekent en waarom het nodig is. Koper(I)oxide is "
                "Cu₂O en koper(II)oxide is CuO, twee verschillende stoffen met een verschillende "
                "kleur.",
                "Noem het rooster, want daar hangt het aan. In een zoutkristal zijn er geen losse "
                "deeltjes NaCl: elk natriumion zit tussen zes chloride-ionen. De formule geeft dus "
                "enkel de verhouding.",
                "Noem de twee uitgangen samen met hun zuurrest: -aat bij het rijkste aan zuurstof, "
                "-iet bij dat met één zuurstofatoom minder. Dezelfde regel geldt bij nitraat en "
                "nitriet.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-organische-stoffen-stofklassen-en-naamgeving-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek de functionele groep en de stofklasse volgt. OH is een alcohol, CHO een "
                   "aldehyde, CO tussen twee koolstofatomen een keton, COOH een carbonzuur, een O "
                   "tussen twee ketens een ether, COO een ester, NH₂ een amine en CO-NH een "
                   "amide.",
            waarom=[
                "Houd keton en aldehyde uit elkaar aan de plaats van de groep: bij een aldehyde "
                "staat ze op het uiteinde van de keten, bij een keton ergens in het midden.",
                "Let op het verschil tussen een ether en een alcohol: bij een ether zit de "
                "zuurstof tussen twee koolstofketens en is er geen waterstof aan vast.",
                "Het verschil tussen een ester en een carbonzuur is de laatste waterstof: bij een "
                "ester is die vervangen door een koolstofketen. Daarom ruikt een ester naar fruit "
                "en een carbonzuur scherp.",
            ],
        ),
        dict(
            aanpak="Verzadigd betekent enkel enkelvoudige bindingen. Reken met de formules: een "
                   "alkaan is CnH2n+2, een alkeen CnH2n en een alkyn CnH2n−2. Elke dubbele binding "
                   "kost dus twee waterstofatomen.",
            waarom=[
                "Reken even na met de formules: C₃H₈ past bij 2 maal 3 plus 2, dus een alkaan; "
                "C₃H₆ bij 2 maal 3, dus een alkeen.",
                "Reken na: 2 maal 6 plus 2 is 14, dus C₆H₁₄. Dat is hexaan.",
                "Reken na: bij een alkeen is het 2 maal 5, dus 10 waterstofatomen. Dat zijn er "
                "twee minder dan bij het alkaan met vijf koolstofatomen.",
            ],
        ),
        dict(
            aanpak="Een IUPAC-naam bouw je in drie stappen: tel de koolstofatomen van de "
                   "hoofdketen voor de stam, zoek de functionele groep voor de uitgang, en nummer "
                   "van de kant die de groep het laagste nummer geeft.",
            waarom=[
                "Onthoud de stamnamen in orde: meth, eth, prop, but, pent, hex. Daarna wordt het "
                "regelmatig met hept, oct, non en dec.",
                "Bij butanon hoeft er geen nummer bij, want in een keten van vier koolstofatomen "
                "kan de ketongroep enkel op plaats 2 staan. Bij propaan-2-ol is het nummer wel "
                "nodig, want 1 was ook mogelijk.",
                "Noem de regel: het laagste nummer wint. Daarom bestaat propaan-3-ol niet als "
                "naam, ook al zou je de formule begrijpen.",
            ],
        ),
        dict(
            aanpak="Tel wat er aan het centrale atoom hangt. Bij een alcohol kijk je naar het "
                   "koolstofatoom met de OH-groep en tel je hoeveel koolstofatomen eraan vastzitten. "
                   "Bij een amine tel je de ketens aan het stikstofatoom.",
            waarom=[
                "Reken het na op de namen: bij butaan-1-ol zit de OH op het uiteinde, dus één "
                "koolstofbuur, dus primair. Bij butaan-2-ol zijn er twee buren, dus secundair.",
                "Noem beide regels apart, want dat is de hele vraag. Dat ze verschillen is logisch: "
                "bij een alcohol hangt de groep aan koolstof, bij een amine is de stikstof zelf "
                "het centrale atoom.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken over bouw en bindingen. Let vooral op het woord aromatisch: "
                   "dat vraagt een ring met gedelokaliseerde elektronen, niet gewoon een ring.",
            waarom=[
                "Niet waar, en dit is de klassieke valkuil. Cyclohexaan is een ring, maar met "
                "enkel enkelvoudige bindingen. Aromatisch is benzeen, met zijn gedelokaliseerde "
                "elektronenwolk.",
                "Waar, en dat is precies waarom benzeen zo stabiel is. Daarom tekent men de ring "
                "ook vaak met een cirkel in het midden in plaats van met drie dubbele bindingen.",
                "Niet waar. Een ether heeft geen waterstof aan de zuurstof, en zonder zo'n "
                "waterstof is er geen waterstofbrug mogelijk. Daarom kookt een ether bij een veel "
                "lagere temperatuur dan de alcohol met evenveel koolstofatomen.",
                "Waar. De vier bindingen rond een koolstofatoom staan onder ongeveer 109 graden, "
                "dus kan een keten niet recht zijn. Dat men hem toch recht tekent, is enkel "
                "gemakshalve.",
            ],
        ),
        dict(
            aanpak="Hier gaat het om triviale namen die je uit het dagelijks leven kent. Zet "
                   "ernaast wat de stof chemisch is, en let erop dat sommige namen een stofklasse "
                   "aanduiden en andere één bepaalde stof.",
            waarom=[
                "Merk op dat glycerol propaantriol is: drie OH-groepen op drie koolstofatomen. "
                "Juist die drie groepen maken dat er drie vetzuren aan kunnen, en zo ontstaat een "
                "triglyceride.",
                "Chloroform en formol zijn oude namen die nog overal gebruikt worden. Formol is "
                "methanal in water, en dat is de stof waarmee men preparaten bewaart.",
            ],
        ),
        dict(
            aanpak="Twee vragen over hoe je een molecule weergeeft. Houd de vier voorstellingen in "
                   "gedachten op volgorde van wat ze tonen: brutoformule, structuurformule, "
                   "skeletnotatie, bolstaafmodel.",
            waarom=[
                "Noem beide helften: wat wegvalt en wat je wel schrijft. De skeletnotatie is "
                "daardoor snel te tekenen en toch ondubbelzinnig, en net daarom wordt ze in de "
                "organische chemie overal gebruikt.",
                "Noem het woord ruimtelijk, want dat is wat een bolstaafmodel toevoegt. "
                "C₂H₆O kan ethanol of dimethylether zijn: dezelfde brutoformule, twee heel "
                "verschillende stoffen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-isomerie-en-chiraliteit-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Isomeren hebben dezelfde brutoformule en een andere bouw. Vraag je wat er "
                   "precies verschilt: de vorm van de keten (ketenisomerie), de plaats van de "
                   "groep (plaatsisomerie) of de stofklasse zelf (functie-isomerie).",
            waarom=[
                "Houd het verschil vast: bij ketenisomerie verandert het geraamte, bij "
                "plaatsisomerie blijft het geraamte gelijk en schuift enkel de groep op.",
                "Propanal en propanon zijn het mooiste paar van de drie: dezelfde formule C₃H₆O, "
                "en toch een aldehyde tegenover een keton. De stofklasse verschilt, dus "
                "functie-isomerie.",
                "Ethaanzuur en methylmethanoaat hebben beide de formule C₂H₄O₂, maar het ene is "
                "een carbonzuur en het andere een ester. Dat is weer functie-isomerie, nu tussen "
                "twee heel verschillende stofklassen.",
            ],
        ),
        dict(
            aanpak="Eén toets beslist of twee stoffen isomeren zijn: hebben ze precies dezelfde "
                   "brutoformule? Zo niet, dan zijn het gewoon twee stoffen. En let op: dezelfde "
                   "formule betekent niet dezelfde eigenschappen.",
            waarom=[
                "Niet waar. Butaan is C₄H₁₀ en pentaan C₅H₁₂, dus verschillende formules. Ze "
                "horen tot dezelfde reeks maar zijn geen isomeren.",
                "Waar: beide zijn C₂H₆O. Toch is ethanol vloeibaar bij kamertemperatuur en "
                "dimethylether een gas, en dat is het bewijs dat de bouw de eigenschappen "
                "bepaalt.",
                "Niet waar, en de vorige vraag toont het al. Een vertakte keten heeft minder "
                "contactoppervlak en dus een lager kookpunt dan de rechte keten met dezelfde "
                "formule.",
                "Waar, en dat is net de definitie: bij plaatsisomerie verschuift enkel de plaats "
                "van de groep, dus blijft het bijvoorbeeld in beide gevallen een alcohol.",
            ],
        ),
        dict(
            aanpak="Tel de isomeren systematisch: eerst de rechte keten, dan de vertakkingen van "
                   "lang naar kort. En bij stereo-isomeren reken je met machten van twee: elk "
                   "asymmetrisch koolstofatoom verdubbelt het aantal.",
            waarom=[
                "Zet ze echt op papier, want dat is de enige manier om er geen te vergeten of "
                "er een dubbel te tekenen. Bij C₅H₁₂ zijn het pentaan, 2-methylbutaan en "
                "2,2-dimethylpropaan.",
                "Reken na met 2 tot de macht van het aantal asymmetrische koolstofatomen: 2, dan 4, "
                "dan bij vier atomen 2 maal 2 maal 2 maal 2, dus 16.",
                "Noem het aantal koolstofatomen dat nodig is om te kunnen vertakken: pas vanaf "
                "vier. Met één koolstofatoom en vier identieke waterstofatomen is er maar één "
                "mogelijkheid.",
            ],
        ),
        dict(
            aanpak="Z/E-isomerie vraagt twee dingen samen: een dubbele binding, en aan elk van de "
                   "twee koolstofatomen van die binding twee verschillende groepen. Zit er aan één "
                   "kant twee keer hetzelfde, dan bestaat er geen Z en E.",
            waarom=[
                "Reken het na op but-1-een: aan het eerste koolstofatoom zitten twee "
                "waterstofatomen, dus twee keer hetzelfde, dus geen Z/E. Bij but-2-een staat aan "
                "elke kant een waterstof en een methylgroep, en dan wel.",
                "Noem het draaien, want dat is de reden. Rond een enkelvoudige binding kan de "
                "molecule vrij draaien, en wat in elkaar kan draaien is dezelfde stof.",
                "Noem de dipolen, want daar hangt het verschil aan. Dit is ook de reden dat de "
                "Z-vorm en de E-vorm van een vetzuur zich zo anders gedragen: de cis-vorm met zijn "
                "knik stapelt losser.",
            ],
        ),
        dict(
            aanpak="Chiraal betekent dat de molecule niet met haar spiegelbeeld samenvalt, en dat "
                   "gebeurt zodra er een koolstofatoom met vier verschillende groepen in zit. Zoek "
                   "dus eerst zo'n koolstofatoom, en kijk goed of twee van de vier groepen niet "
                   "toevallig gelijk zijn.",
            waarom=[
                "Reken het na: bij 2-broompropaan zitten aan het middelste koolstofatoom twee "
                "identieke methylgroepen, dus geen vier verschillende groepen en dus niet chiraal. "
                "Bij 2-chloorbutaan zijn alle vier verschillend.",
                "Noem de vier verschillende groepen en gebruik het beeld van de handen, want dat "
                "is de duidelijkste vergelijking: je linker- en rechterhand zijn spiegelbeelden en "
                "toch niet dezelfde.",
                "Noem het opheffen van de draaiing, want dat is wat racemisch betekent. Een zuivere "
                "vorm draait het vlak wel, en daarmee kan men meten hoe zuiver een staal is.",
                "Dit is de reden dat de scheiding van spiegelbeeldvormen in de "
                "geneesmiddelenindustrie zo belangrijk is. Noem de chirale receptor, want daarin "
                "zit de verklaring: een linkerhand past niet in een rechterhandschoen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-atoombouw-orbitalen-en-het-periodiek-systeem-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Houd twee getallen vast: in elk orbitaal passen twee elektronen, en de "
                   "subniveaus hebben 1, 3, 5 en 7 orbitalen. Vermenigvuldig met twee en je krijgt "
                   "2, 6, 10 en 14.",
            waarom=[
                "Reken na: een p-subniveau heeft drie orbitalen maal twee elektronen, dus 6. Met "
                "diezelfde rekensom vind je ook 10 voor d en 14 voor f.",
                "Onthoud de reeks 1, 3, 5, 7 orbitalen bij s, p, d en f. Dan hoef je de aantallen "
                "elektronen nooit uit het hoofd te leren.",
            ],
        ),
        dict(
            aanpak="Vul de subniveaus in de orde van de diagonaalregel en tel de elektronen mee "
                   "tot je het juiste aantal hebt: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p. De exponenten "
                   "moeten samen het aantal elektronen geven.",
            waarom=[
                "Controleer je antwoord door de exponenten op te tellen: 2 plus 2 plus 3 is 7 voor "
                "stikstof, en 2 plus 2 plus 6 plus 1 is 11 voor natrium. Komt het niet uit, dan heb "
                "je een subniveau overgeslagen.",
                None,
                "Valentie-elektronen zijn de elektronen van het buitenste hoofdniveau: 3s² plus "
                "3p⁴ is 6. Het getal 6 zegt ook meteen dat dit element in groep 16 staat.",
                "Reken na: magnesium heeft 12 elektronen en Mg²⁺ heeft er twee afgestaan, dus 10. "
                "Dat is net de configuratie van neon, en daarom staat magnesium zo graag twee "
                "elektronen af.",
            ],
        ),
        dict(
            aanpak="Vier kwantumgetallen beschrijven één elektron, van groot naar klein: welke "
                   "schil, welk soort orbitaal, welk orbitaal daarvan, en welke spin. Zie het als "
                   "een adres: straat, huisnummer, verdieping, kamer.",
            waarom=[
                None,
                None,
                "Leg het uit met het gevolg erbij: omdat twee elektronen in hetzelfde orbitaal een "
                "tegengestelde spin moeten hebben, passen er maar twee in. Daar komt het getal 2 "
                "van de hele eerste reeks vandaan.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken over de regels bij het vullen. Let vooral op de diagonaalregel "
                   "(4s komt voor 3d) en op wat een orbitaal eigenlijk is: een kansgebied en geen "
                   "baan.",
            waarom=[
                "Niet waar, het is net omgekeerd: 4s wordt eerst gevuld, en daarna 3d. Dat is de "
                "reden dat de d-blokelementen pas in de vierde periode beginnen.",
                "Waar, en de reden is dat elektronen elkaar afstoten: ze gaan liever elk in een "
                "eigen orbitaal zitten dan samen in één.",
                "Niet waar, en dit is het grote verschil met het oude model van Bohr. Een orbitaal "
                "is een gebied waar het elektron met grote waarschijnlijkheid zit, geen cirkel "
                "waarop het rondloopt.",
                "Waar, en helium is daarmee de uitzondering op de octetregel. Zijn eerste "
                "hoofdniveau heeft maar één orbitaal, dus is het met twee elektronen al vol.",
            ],
        ),
        dict(
            aanpak="Uit de configuratie lees je de plaats af: het hoogste hoofdkwantumgetal is de "
                   "periode, en het aantal valentie-elektronen geeft de groep. Bij de hoofdgroepen "
                   "is dat 1 of 2 voor s, en 13 tot 18 voor p.",
            waarom=[
                "Reken na bij het tweede voorbeeld: 4s² plus 4p³ is vijf valentie-elektronen, en "
                "dan is het groep 15. De 3d¹⁰ telt niet mee, want die schil is vol en zit niet "
                "buitenaan.",
                None,
                "Leer de groepsnamen, want ze komen in elke vraag over reactiviteit terug: "
                "alkalimetalen in groep 1, aardalkalimetalen in groep 2, halogenen in groep 17 en "
                "edelgassen in groep 18.",
            ],
        ),
        dict(
            aanpak="Twee trends verklaren bijna alles. Naar rechts in een periode: meer protonen "
                   "bij hetzelfde hoofdniveau, dus kleiner. Naar onder in een groep: een "
                   "hoofdniveau erbij, dus groter. En een negatief ion is altijd groter dan zijn "
                   "atoom.",
            waarom=[
                "Let op het derde paar: een chloride-ion heeft één elektron meer dan het atoom, "
                "dus stoten de elektronen elkaar sterker af en wordt de wolk groter. Bij een "
                "positief ion is het net omgekeerd.",
                "Noem beide delen van de uitleg: meer protonen én hetzelfde hoofdniveau. Enkel "
                "meer protonen zonder die tweede helft verklaart het niet.",
                "Noem de twee redenen: de afstand tot de kern en het kleine aantal "
                "valentie-elektronen. Daarom zijn francium en cesium de meest reactieve metalen en "
                "staan ze linksonder.",
                "Noem het volle buitenste niveau en vermeld de uitzondering van helium met twee. "
                "Dat is ook de reden dat alle andere atomen naar juist die configuratie streven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-atoombinding-en-lewisstructuren-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Tel in twee stappen. Elke binding tussen twee atomen heeft precies één "
                   "sigma-binding; alles daarbovenop is pi. Een dubbele binding is dus één sigma "
                   "en één pi, een drievoudige één sigma en twee pi.",
            waarom=[
                "Bij een molecule met enkel enkelvoudige bindingen is het aantal sigma-bindingen "
                "gelijk aan het aantal bindingsstreepjes, en is er geen enkele pi.",
                "Reken na bij etheen: vier C-H-bindingen plus één C-C geeft vijf sigma, en de "
                "tweede helft van de dubbele binding is de ene pi.",
                "Let op CO₂: twee dubbele bindingen geven twee sigma en twee pi. Bij N₂ zit "
                "alles tussen twee atomen, dus één sigma en twee pi.",
            ],
        ),
        dict(
            aanpak="Meer bindingen tussen dezelfde twee atomen betekent korter en sterker. Houd "
                   "daarnaast twee regels vast: er kan maar één sigma-binding tussen twee atomen "
                   "liggen, en een pi-binding blokkeert het draaien.",
            waarom=[
                "Noem de drie lengtes of minstens de orde, en zeg waarom: meer gedeelde "
                "elektronen betekent meer aantrekking en dus een kortere afstand. Korter en "
                "sterker gaan hier altijd samen.",
                "Niet waar. Een sigma-binding ligt recht tussen de twee kernen, en die plaats is "
                "maar één keer beschikbaar. Al de rest moet dus pi zijn.",
                "Waar, want de overlapping van een pi-binding ligt naast de verbindingslijn en is "
                "daardoor minder goed. Precies daarom reageert een dubbele binding gemakkelijker "
                "dan een enkelvoudige: de pi gaat het eerst eraan.",
                "Niet waar, en dit is de reden dat Z/E-isomerie bestaat. Draaien zou de pi-binding "
                "moeten breken, en daar is te veel energie voor nodig.",
            ],
        ),
        dict(
            aanpak="Reken met de valentie-elektronen. Tel hoeveel elektronen het atoom heeft in "
                   "zijn buitenste niveau, trek er af wat het in bindingen stopt, en wat "
                   "overblijft zit in vrije paren. Zuurstof heeft zes, stikstof vijf, een halogeen "
                   "zeven.",
            waarom=[
                "Reken na bij zuurstof in water: zes valentie-elektronen, twee gaan in bindingen, "
                "dus blijven er vier over, en dat zijn twee paren.",
                "In NH₄⁺ heeft de stikstof vier bindingen en dus geen vrij paar meer: dat ene "
                "vrije paar is gebruikt om de vierde binding te maken. Hetzelfde gebeurt bij "
                "zuurstof in H₃O⁺.",
            ],
        ),
        dict(
            aanpak="Gebruik de formule: valentie-elektronen min vrije elektronen min het aantal "
                   "bindingen. Doe dat per atoom, en controleer achteraan of de som van alle "
                   "formele ladingen gelijk is aan de lading van het deeltje.",
            waarom=[
                "Reken na bij stikstof in NH₄⁺: 5 min 0 min 4 is plus 1. En bij zuurstof in OH⁻: "
                "6 min 4 min 1 is min 1.",
                "Noem het verschil in de verdeling: eerlijk delen tegenover alles aan de "
                "elektronegatiefste. Daarom is het oxidatiegetal van zuurstof in water min II "
                "terwijl de formele lading nul is.",
            ],
        ),
        dict(
            aanpak="Vier soorten binding, en je kiest ze op wat er bindt: metaal met niet-metaal "
                   "geeft een ionbinding, niet-metaal met niet-metaal een atoombinding, metaal met "
                   "metaal een metaalbinding, en een vrij elektronenpaar dat alleen een binding "
                   "levert geeft een donor-acceptorbinding.",
            waarom=[
                None,
                None,
                "Noem beide helften: vrije elektronen in een metaal tegenover vaste ionen in een "
                "zoutrooster. Voeg er eventueel bij dat een zout in gesmolten of opgeloste "
                "toestand wel geleidt, want dan kunnen de ionen zelf bewegen.",
                "Noem beide delen van de vraag, ook het tweede: achteraf is er geen verschil meer "
                "te zien. De vier N-H-bindingen in NH₄⁺ zijn allemaal gelijk, en dat laat zien dat "
                "de herkomst van de elektronen niets aan de binding verandert.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ruimtelijke-structuur-polariteit-en-intermoleculaire-krachten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Het sterisch getal is het aantal plaatsen rond het centrale atoom: tel de "
                   "atomen die eraan vastzitten plus de vrije elektronenparen. Een dubbele binding "
                   "telt daarbij als één plaats.",
            waarom=[
                "Alle drie komen op vier uit, en toch zien ze er anders uit: koolstof met vier "
                "atomen, zuurstof met twee atomen en twee vrije paren, stikstof met drie atomen en "
                "één vrij paar.",
                "Let op dat een dubbele binding één plaats is: bij CO₂ zijn er twee plaatsen, bij "
                "SO₂ drie (twee atomen en één vrij paar), en bij etheen drie per koolstofatoom.",
            ],
        ),
        dict(
            aanpak="Uit het sterisch getal volgen de hybridisatie en de basisvorm: 2 geeft sp en "
                   "lineair, 3 geeft sp² en vlak driehoekig, 4 geeft sp³ en tetraëdrisch. De "
                   "werkelijke vorm hangt daarna af van hoeveel van die plaatsen vrije paren zijn.",
            waarom=[
                "Onthoud de drie rijen samen: 2 met sp en 180 graden, 3 met sp² en 120 graden, 4 "
                "met sp³ en 109,5 graden. Met die tabel kan je elke vorm in deze reeks afleiden.",
                "Let op dat CH₄, NH₃ en H₂O alle drie sp³ zijn en toch drie verschillende namen "
                "krijgen. De vrije paren zie je niet in de vorm, maar ze bepalen die wel.",
                "NH₄⁺ is tetraëdrisch net als CH₄, want vier plaatsen en geen vrij paar. Dat een "
                "deeltje geladen is, verandert niets aan de vormregels.",
            ],
        ),
        dict(
            aanpak="Eén regel verklaart de drie hoeken: een vrij elektronenpaar duwt harder dan "
                   "een bindend paar. Begin bij 109,5 graden en haal er ongeveer twee graden af "
                   "voor elk vrij paar.",
            waarom=[
                "Reken even mee: 109,5 bij geen vrij paar, 107 bij één, 104,5 bij twee. De stap is "
                "elke keer ongeveer 2,5 graden.",
                "Noem de reden en de drie gevallen, want dat is precies wat de vraag vraagt. Een "
                "vrij paar hoort maar bij één atoom en spreidt zich dus breder uit dan een paar "
                "dat tussen twee kernen gedeeld wordt.",
            ],
        ),
        dict(
            aanpak="Polariteit heeft twee voorwaarden: polaire bindingen én een vorm waarin ze "
                   "elkaar niet opheffen. Kijk dus altijd eerst naar de bindingen en daarna naar "
                   "de symmetrie van de molecule.",
            waarom=[
                "CCl₄ is het mooiste voorbeeld van opheffing: vier polaire bindingen, perfect "
                "symmetrisch verdeeld over een tetraëder, dus samen nul.",
                "HCl is polair omdat er maar één binding is en die niet opgeheven kan worden. Bij "
                "CH₄ zijn de bindingen bijna apolair én symmetrisch.",
                "Dit is de kernvraag van de reeks. Noem de twee vormen bij naam, lineair tegenover "
                "geknikt, want de bindingen zijn in beide gevallen hetzelfde.",
            ],
        ),
        dict(
            aanpak="Vijf krachten op een schaal van zwak naar sterk: londonkracht, dipoolkracht, "
                   "waterstofbrug, ion-dipoolkracht en als sterkste de coulombkracht tussen ionen. "
                   "Zoek eerst wat voor deeltjes er tegenover elkaar staan.",
            waarom=[
                "Een waterstofbrug vraagt waterstof aan N, O of F. Methaan heeft dat niet, dus "
                "blijven er enkel londonkrachten over, en daarom is methaan bij kamertemperatuur "
                "een gas en water een vloeistof.",
                "Houd het verschil vast: tussen twee ionen is het een coulombkracht in een "
                "rooster, tussen een ion en een polaire molecule een ion-dipoolkracht. Dat tweede "
                "is net wat zout doet oplossen.",
                "Drie vergelijkingen met drie regels: langer geeft meer londonkracht, vertakt geeft "
                "minder contact, en een waterstofbrug wint het van een gewone dipool. Daarom kookt "
                "water bij 100 graden en waterstofsulfide al onder nul.",
            ],
        ),
        dict(
            aanpak="Gelijk lost op in gelijk: polair bij polair, apolair bij apolair. En bij "
                   "roosters beslist het soort rooster of er geleiding is en hoe hoog het "
                   "smeltpunt ligt.",
            waarom=[
                None,
                "Houd de drie roosters apart: een metaalrooster geleidt altijd, een ionrooster "
                "enkel gesmolten of opgelost, een molecuulrooster nooit. Er zijn geen vrije "
                "ladingsdragers in een molecuulrooster.",
                "Noem de waterstofbrug, want dat is het verschil. Ethanol heeft een polair "
                "uiteinde dat bij water past; bij een langere alcohol wordt het apolaire stuk "
                "zwaarder en mengt het al minder goed.",
                "Noem het soort rooster, want daar zit het hele antwoord. Dit is ook het verband "
                "met de vorige reeks: binnen een molecule zijn de bindingen sterk, tussen "
                "moleculen zijn de krachten zwak.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-chemisch-rekenen-mol-molaire-massa-en-concentratie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Tel de atoommassa's op, elk zo veel keer als de index aangeeft. Schrijf de som "
                   "uit in plaats van hem in je hoofd te doen, want één vergeten index geeft een "
                   "fout die je nadien niet meer terugvindt.",
            waarom=[
                "Reken één na om je methode te controleren: NaOH is 23 plus 16 plus 1, dus 40 "
                "g/mol. Dat getal komt in de hele bundel terug.",
                "Bij H₂SO₄: 2 maal 1 plus 32 plus 4 maal 16 is 2 plus 32 plus 64, dus 98 g/mol. "
                "Let op de 4 maal 16, want juist daar gaat het meestal mis.",
            ],
        ),
        dict(
            aanpak="Eén formule voor de hele reeks: n is m gedeeld door M. Zoek je mol, dan deel "
                   "je de massa door de molaire massa; zoek je gram, dan vermenigvuldig je. Schrijf "
                   "de formule eerst op en vul dan in.",
            waarom=[
                "Reken na: 34 gedeeld door 17 is 2 mol.",
                "Reken na: 9 gedeeld door 18 is 0,5 mol. Een halve mol water is negen gram, en dat "
                "is een handig getal om te onthouden.",
                "Hier gaat het de andere kant op: 0,25 maal 40 is 10 g. Controleer altijd of je "
                "antwoord de juiste eenheid heeft, want dat verraadt een verkeerde bewerking.",
                "Reken na: 3 maal 44 is 132 g.",
            ],
        ),
        dict(
            aanpak="Een mol is een aantal: 6,022 maal tien tot de drieëntwintigste deeltjes. Wil "
                   "je atomen in plaats van moleculen, vermenigvuldig dan nog eens met de index "
                   "van dat atoom in de formule.",
            waarom=[
                None,
                "Reken na: er zitten vier zuurstofatomen in H₂SO₄, dus 2 maal 4 is 8 mol "
                "zuurstofatomen. Dit is de klassieke extra stap die vergeten wordt.",
                "Noem de molaire massa van beide, want daar zit het antwoord. Dezelfde massa geeft "
                "een heel ander aantal deeltjes, en dat is net de reden dat chemici in mol rekenen "
                "en niet in gram.",
            ],
        ),
        dict(
            aanpak="Bij normomstandigheden neemt één mol gas 22,4 liter in, welk gas het ook is. "
                   "Vermenigvuldig dus het aantal mol met 22,4, of deel het volume door 22,4 om "
                   "mol te vinden.",
            waarom=[
                "Reken na: 0,25 maal 22,4 is 5,6 liter. Omdat het steeds halveert, kan je deze "
                "rij ook uit het hoofd controleren.",
                "Niet waar. 22,4 liter geldt enkel bij 0 graden Celsius en 1 bar. Bij "
                "kamertemperatuur is het ongeveer 24 liter, en de bundel zegt daarom telkens bij "
                "normomstandigheden.",
                "Waar, en dat is het verrassende van het molair volume: de soort gasmolecule doet "
                "niet mee. De deeltjes zitten zo ver van elkaar dat hun eigen grootte verwaarloosd "
                "kan worden.",
            ],
        ),
        dict(
            aanpak="Concentratie is mol per liter, dus zet een volume in milliliter altijd eerst "
                   "om naar liter. Massaprocent is iets anders: dat is gram stof per honderd gram "
                   "oplossing.",
            waarom=[
                None,
                "Reken na: 250 mL is 0,25 L, en 0,25 maal 0,8 is 0,2 mol. Wie de milliliter laat "
                "staan, komt duizend keer te hoog uit.",
                None,
                "Reken na: 5 procent van 300 g is 15 g. Let op dat het om de massa van de hele "
                "oplossing gaat, niet van het water alleen.",
            ],
        ),
        dict(
            aanpak="Bij verdunnen blijft het aantal mol gelijk, en dat is precies wat de formule "
                   "c₁ maal V₁ is c₂ maal V₂ uitdrukt. Vul in wat je kent en los op naar het ene "
                   "onbekende.",
            waarom=[
                "Reken na: 20 maal 1 gedeeld door 100 is 0,2 mol/L. Vijf keer zoveel volume geeft "
                "vijf keer minder concentratie.",
                "Reken na: 500 maal 0,1 gedeeld door 2 is 25 mL. Je neemt dus 25 mL en vult aan "
                "tot 500 mL, en niet 25 mL plus 500 mL.",
                "Noem waarom de formule werkt: er komt enkel oplosmiddel bij. Daarmee begrijp je "
                "de formule in plaats van hem uit het hoofd te kennen.",
            ],
        ),
        dict(
            aanpak="Procent, promille en ppm zijn dezelfde soort breuk op een andere noemer: "
                   "honderd, duizend en een miljoen. En bij een empirische formule deel je de "
                   "percentages door de atoommassa's en daarna door de kleinste uitkomst.",
            waarom=[
                None,
                "Reken na: een liter water is ongeveer duizend gram, dus een miljoenste daarvan is "
                "een milligram. Daarom worden gehaltes in water bijna altijd in mg per liter "
                "gegeven.",
                "Werk in twee stappen zoals in het antwoord: eerst delen door de atoommassa, dan "
                "delen door de kleinste uitkomst. Kom je op bijna hele getallen, dan is je "
                "verhouding juist; kom je op iets als 1,5, dan vermenigvuldig je alles met twee.",
                "Noem dat de opgeloste stof zelf plaats inneemt. Daarom staat er op een maatkolf "
                "één streep en niet een hele schaal: hij is gemaakt om op dat ene volume aan te "
                "vullen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-stoichiometrie-overmaat-en-de-algemene-gaswet-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Uitbalanceren is tellen per element, links en rechts gelijk. Begin met het "
                   "element dat in de minste stoffen voorkomt en doe zuurstof en waterstof het "
                   "laatst. Je mag enkel de coëfficiënten vooraan veranderen.",
            waarom=[
                None,
                "Bij ethaan geeft het eerst een halve: 2 C₂H₆ zet je vooraan om de breuk weg te "
                "werken, en dan komt er 7 voor O₂. Controleer achteraan: 14 zuurstofatomen links, "
                "8 in CO₂ plus 6 in H₂O rechts, dus 14.",
                "Controleer bij aluminium de waterstof: 6 HCl geeft 6 waterstofatomen, en 3 H₂ ook. "
                "Zo weet je dat het klopt zonder het na te kijken in de oplossing.",
                "Niet waar, en dit is de belangrijkste regel van de reeks. Een formule aanpassen "
                "maakt er een andere stof van; enkel het getal vooraan mag veranderen.",
            ],
        ),
        dict(
            aanpak="De coëfficiënten zijn een verhouding in mol. Zet de gegeven stof en de "
                   "gevraagde stof naast elkaar met hun coëfficiënt, en reken met een "
                   "verhoudingstabel of een kruisproduct.",
            waarom=[
                "Reken na: de verhouding N₂ op NH₃ is 1 op 2, dus 3 mol geeft 6 mol.",
                "Reken na: H₂ op NH₃ is 3 op 2, dus voor 4 mol NH₃ heb je 6 mol H₂ nodig.",
                "Reken na: H₂ op N₂ is 3 op 1, dus 9 mol H₂ hoort bij 3 mol N₂.",
            ],
        ),
        dict(
            aanpak="Van gram naar gram gaat altijd in dezelfde vijf stappen: gram, mol, "
                   "verhouding, mol, gram. Schrijf die vijf stappen echt op, want een rechtstreekse "
                   "sprong van gram naar gram is de meest gemaakte fout.",
            waarom=[
                "Volg de vijf stappen in het antwoord. Merk op dat de verhouding hier 1 op 1 is en "
                "de massa toch verandert, want magnesiumoxide is zwaarder dan magnesium.",
                "Dezelfde vijf stappen, nu met een ontledingsreactie. Deze berekening is precies "
                "wat men in een kalkoven doet, en de 22 g CO₂ per 50 g kalksteen verklaart waarom "
                "de cementindustrie zoveel CO₂ uitstoot.",
                "Noem dat de coëfficiënten mol betekenen en geen gram. Dit is de uitleg achter de "
                "vijf stappen van de vorige twee oefeningen.",
            ],
        ),
        dict(
            aanpak="Om het beperkend reagens te vinden deel je van elke stof het aantal mol door "
                   "haar coëfficiënt. De kleinste uitkomst is de beperkende stof, en met die "
                   "uitkomst reken je verder.",
            waarom=[
                "Reken na bij het eerste geval: 3 gedeeld door 2 is 1,5 voor H₂ en 3 gedeeld door "
                "1 is 3 voor O₂, dus is H₂ beperkend. Bij het tweede: 2 voor N₂ en 1 voor H₂, dus "
                "weer H₂.",
                "Reken na: H₂ is beperkend met 3 mol, en de verhouding H₂ op H₂O is 2 op 2, dus "
                "3 mol water. Het overschot aan zuurstof blijft ongebruikt.",
                "Niet waar, en dit is de valkuil van de reeks. Het gaat om mol gedeeld door "
                "coëfficiënt: in het eerste geval was er van beide 3 mol en was H₂ toch "
                "beperkend.",
                "Noem beide redenen: de dure stof reageert volledig weg, en het overschot kan "
                "hergebruikt worden. Bij de ammoniaksynthese doet men precies dat met de "
                "waterstof en de stikstof.",
            ],
        ),
        dict(
            aanpak="Reken in de gaswet altijd met kelvin: tel 273 op bij de temperatuur in graden "
                   "Celsius. Houd daarnaast twee verbanden vast: bij gelijke druk zijn V en T "
                   "recht proportioneel, bij gelijke temperatuur zijn p en V omgekeerd "
                   "proportioneel.",
            waarom=[
                "Reken één na: 27 plus 273 is 300 K. Vergeet die omrekening nooit, want met graden "
                "Celsius geeft de gaswet onzin, al was het maar omdat 0 graden geen nul is.",
                "Reken na: 5,6 gedeeld door 22,4 is 0,25 mol.",
                "Reken na: 1,5 maal 22,4 is 33,6 liter.",
                "Niet waar, het is net omgekeerd: meer druk perst het gas samen. p en V zijn "
                "omgekeerd proportioneel, dus hun product blijft gelijk.",
                "Reken na: de temperatuur in kelvin verdubbelt van 300 naar 600, dus verdubbelt "
                "het volume van 2 naar 4 liter. Let op dat dit enkel met kelvin werkt: met graden "
                "Celsius zou je hier een heel ander getal uitkomen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-reactiesnelheid-botsingsmodel-en-energiediagram-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Elke factor werkt via het botsingsmodel: meer botsingen of betere botsingen "
                   "geeft een snellere reactie. Concentratie, verdeling en roeren zorgen voor meer "
                   "botsingen; temperatuur en een katalysator zorgen dat er meer botsingen de "
                   "drempel halen.",
            waarom=[
                "Verdunnen en koelen werken op een verschillende manier: verdunnen geeft minder "
                "botsingen, koelen geeft minder botsingen die hard genoeg zijn. Zeg dus telkens "
                "welk van de twee je bedoelt.",
                "Fijnmalen en roeren verhogen beide het contactoppervlak of de ontmoetingskans "
                "zonder dat er iets bijkomt. Daarom brandt zaagsel zo veel sneller dan een balk.",
                "Noem beide gevolgen van opwarmen en zeg welk het zwaarst weegt: niet het vaker "
                "botsen maar het harder botsen. Een stijging van tien graden kan een reactie al "
                "ongeveer verdubbelen in snelheid.",
            ],
        ),
        dict(
            aanpak="Een botsing leidt enkel tot reactie als er twee dingen samen kloppen: genoeg "
                   "energie en de juiste stand. Lukt een van die twee niet, dan ketsen de deeltjes "
                   "af. Dat is de kern van het hele botsingsmodel.",
            waarom=[
                "Noem beide voorwaarden, want één ervan is nooit genoeg. Juist daardoor is maar "
                "een klein deel van de botsingen effectief.",
                None,
                "Niet waar, en dat is net wat het model verklaart. Het overgrote deel van de "
                "botsingen is elastisch; als elke botsing zou werken, zou elke reactie in een "
                "fractie van een seconde gedaan zijn.",
                "Niet waar. Een katalysator doet mee en komt er onveranderd weer uit, en daarom "
                "kan een kleine hoeveelheid heel veel reactie versnellen.",
            ],
        ),
        dict(
            aanpak="In een energiediagram staan drie dingen: de hoogte van de berg "
                   "(activeringsenergie), de top (geactiveerd complex) en het hoogteverschil "
                   "tussen begin en einde (reactie-energie). Houd die drie goed uit elkaar, want "
                   "ze zijn onafhankelijk van elkaar.",
            waarom=[
                None,
                "Exo-energetisch wil zeggen dat de producten lager liggen, dus dat er energie "
                "vrijkomt. Endo-energetisch is het omgekeerde: de producten liggen hoger.",
                "Dit is de belangrijkste vraag van de bundel. Noem beide grootheden apart: het "
                "hoogteverschil tussen begin en einde zegt niets over de hoogte van de berg "
                "ertussen. Benzine in een jerrycan is het dagelijkse bewijs.",
                "Noem allebei: wat wel verandert en wat niet. Een katalysator verlaagt de berg "
                "maar verschuift het begin en het einde niet, en daarom verandert ook de "
                "evenwichtsligging niet.",
            ],
        ),
        dict(
            aanpak="Vraag je of het mengsel warmte opneemt of afgeeft. Wordt het koud aan de "
                   "buitenkant, dan is het endo-energetisch; wordt het warm, dan exo-energetisch.",
            waarom=[
                "Het koudepakje is het enige endo-energetische van de drie: het neemt warmte uit "
                "zijn omgeving op en dat voelt koud aan. Water bij ongebluste kalk wordt zo heet "
                "dat het kan spatten, en daarom heet het blussen.",
            ],
        ),
        dict(
            aanpak="In een snelheidsvergelijking is de exponent de orde in die stof, en de som "
                   "van de exponenten de totale orde. Lees de orde af uit een proef: verdubbel je "
                   "de concentratie en verdubbelt de snelheid, dan is het eerste orde; wordt ze "
                   "vier keer groter, tweede orde.",
            waarom=[
                "Tel gewoon de exponenten op, en onthoud dat een stof zonder exponent exponent 1 "
                "heeft.",
                "Reken na bij tweede orde: 2 in het kwadraat is 4, dus vier keer sneller. En bij "
                "nulde orde doet de concentratie helemaal niet mee.",
                "Noem beide helften: waar k wel en waar k niet van afhangt. Dat k niet van de "
                "concentratie afhangt, is de reden dat men de vergelijking in deze vorm schrijft.",
                "Noem de activeringsenergie en zeg uitdrukkelijk dat de reacties niet stoppen. Dat "
                "is ook de reden dat een diepvriezer langer bewaart dan een koelkast, en toch niet "
                "eeuwig.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-chemisch-evenwicht-en-de-wet-van-le-chatelier-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een evenwicht is dynamisch: de concentraties blijven constant omdat de "
                   "heen- en de terugreactie even snel gaan, niet omdat er niets meer gebeurt. "
                   "Houd dat woord dynamisch vast, want het antwoordt op drie van deze vier "
                   "uitspraken.",
            waarom=[
                None,
                "Niet waar. Constant is niet gelijk: de verhouding wordt bepaald door K, en die "
                "kan heel ver van één liggen.",
                "Niet waar, en dit is het hart van het begrip. Beide reacties lopen door, maar even "
                "snel, zodat er netto niets verandert.",
                "Waar, en dat is een mooie proef: begin je met de producten in plaats van met de "
                "reagentia, dan kom je bij dezelfde eindverhouding uit.",
            ],
        ),
        dict(
            aanpak="Bouw K altijd op dezelfde manier: de producten in de teller, de reagentia in "
                   "de noemer, elk tot de macht van zijn coëfficiënt. De coëfficiënt uit de "
                   "vergelijking wordt dus de exponent in K.",
            waarom=[
                "Controleer je antwoord op de exponenten: bij 3 H₂ hoort [H₂] tot de derde macht. "
                "Een vergeten exponent is hier de meest gemaakte fout.",
                None,
            ],
        ),
        dict(
            aanpak="K groter dan 1 betekent dat de producten overwegen, K kleiner dan 1 dat de "
                   "reagentia overwegen. Hoe verder van 1, hoe eenzijdiger het evenwicht ligt.",
            waarom=[
                None,
                "Noem het verschil tussen K en de snelheid, want dat is dezelfde les als bij het "
                "energiediagram: K zegt waar het evenwicht ligt, niet hoe lang het duurt om er te "
                "komen.",
            ],
        ),
        dict(
            aanpak="Le Chatelier in één zin: het evenwicht werkt elke verandering tegen. Voeg je "
                   "iets toe, dan verdwijnt het ervan; neem je iets weg, dan maakt het bij. Bij "
                   "druk kijk je naar het aantal gasmoleculen links en rechts, bij temperatuur "
                   "naar de endo- of exo-energetische richting.",
            waarom=[
                "Dat een katalysator niets verschuift, hoort hierbij: hij versnelt beide richtingen "
                "evenveel en brengt je dus enkel sneller bij hetzelfde evenwicht.",
                "Tel bij het derde geval de gasmoleculen: twee links en twee rechts, dus doet druk "
                "er niets. Bij de ammoniakreactie zijn er vier links en twee rechts, en daarom duwt "
                "hoge druk naar rechts.",
                "Noem warmte als iets dat je toevoegt of wegneemt, want dan is de regel dezelfde "
                "als bij een stof. Dat ammoniak koud het best gaat en toch warm gemaakt wordt, is "
                "precies de afweging in het Haber-Boschproces.",
                "Noem het verschil: bij concentratie en druk verschuift het evenwicht om dezelfde "
                "K te halen, bij temperatuur hoort er een andere K. Daarom staat bij een gegeven "
                "waarde van K altijd een temperatuur.",
            ],
        ),
        dict(
            aanpak="Q is dezelfde breuk als K, maar met de concentraties van nu. Vergelijk de twee "
                   "en je weet welke kant het op gaat: is Q te klein, dan moet er product bij, dus "
                   "naar rechts.",
            waarom=[
                "Onthoud het als een weegschaal: Q kruipt altijd naar K toe. Daarom kan je met Q "
                "van elk willekeurig mengsel voorspellen wat er gaat gebeuren.",
            ],
        ),
        dict(
            aanpak="Rendement vergelijkt wat je kreeg met wat mogelijk was; omzettingsgraad "
                   "vergelijkt wat reageerde met wat je erin stak. Beide zijn een breuk maal "
                   "honderd, maar met een verschillende noemer.",
            waarom=[
                "Reken na: 7,5 gedeeld door 10 maal 100 is 75 procent.",
                "Reken na: 0,5 gedeeld door 2 maal 100 is 25 procent. Let op dat de noemer hier de "
                "beginhoeveelheid is en niet de theoretische opbrengst.",
                "Dit is Le Chatelier toegepast in een fabriek. Noem Q en K, want dat maakt het "
                "antwoord precies: zolang Q kleiner blijft dan K, blijft de heenreactie lopen.",
                "Noem de terugreactie, want dat is de reden. Zolang er product is, maakt de "
                "terugreactie weer beginstof aan, en daarom haalt een evenwicht nooit honderd "
                "procent.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-zuren-en-basen-en-het-doorgeven-van-protonen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een geconjugeerde base vind je door één waterstofion weg te halen: één H "
                   "eraf en de lading één eenheid negatiever. Doe die twee dingen altijd samen, "
                   "want de lading vergeten is de meest gemaakte fout.",
            waarom=[
                "Reken één na: HNO₃ zonder H⁺ wordt NO₃⁻. En let op NH₄⁺: dat is al positief, dus "
                "wordt het na het afstaan neutraal, namelijk NH₃.",
                "Water staat hier twee keer in: als zuur geeft het OH⁻, en H₃O⁺ geeft bij afstaan "
                "juist water. Dat laat zien dat water aan beide kanten van zo'n paar kan staan.",
            ],
        ),
        dict(
            aanpak="Nu de andere richting: één H erbij en de lading één eenheid positiever. "
                   "Controleer je antwoord door het weer terug te rekenen, dan zie je meteen of de "
                   "lading klopt.",
            waarom=[
                "Reken na bij CO₃²⁻: er komt een H bij en de lading gaat van min twee naar min "
                "één, dus HCO₃⁻.",
                "HSO₄⁻ wordt H₂SO₄: een tussendeeltje kan dus zowel een zuur als een base zijn, en "
                "dat is precies het onderwerp van de volgende reeks.",
            ],
        ),
        dict(
            aanpak="Een amfolyt kan zowel een proton afstaan als opnemen. Dat kan enkel als het "
                   "deeltje nog minstens één waterstof heeft om af te staan én nog een plaats heeft "
                   "om er een op te nemen. Water en HCO₃⁻ zijn de twee voorbeelden die altijd "
                   "terugkomen.",
            waarom=[
                None,
                "H₃O⁺ kan enkel zuur zijn en OH⁻ enkel base: het ene kan niets meer opnemen, het "
                "andere heeft niets meer af te staan.",
                "Schrijf beide reacties echt uit, want de vraag vraagt er twee. Dat water in de "
                "ene reactie H₃O⁺ en in de andere OH⁻ wordt, is het hele bewijs dat het een "
                "amfolyt is.",
            ],
        ),
        dict(
            aanpak="Tel bij een zuur de waterstofatomen die het kan afstaan, en bij een base de "
                   "protonen die ze kan opnemen. Bij een base is dat gewoon haar lading: CO₃²⁻ kan "
                   "er twee opnemen.",
            waarom=[
                None,
                "Merk op dat de lading van het anion precies de waardigheid geeft. Dat helpt je "
                "ook bij de volumes in een titratie, want een tweewaardige base neemt twee keer "
                "zoveel zuur weg.",
            ],
        ),
        dict(
            aanpak="Houd twee paren begrippen uit elkaar. Sterk of zwak gaat over hoe goed een "
                   "zuur ioniseert; geconcentreerd of verdund gaat over hoeveel er in een liter "
                   "zit. En hoe sterker het zuur, hoe zwakker zijn geconjugeerde base.",
            waarom=[
                "Niet waar, en dit is de belangrijkste verwarring van het hoofdstuk. Een zeer "
                "geconcentreerd azijnzuur blijft een zwak zuur, en een sterk verdund zoutzuur "
                "blijft een sterk zuur.",
                "Waar, net zoals bij pH: de p staat voor een negatieve logaritme, dus betekent "
                "kleiner sterker.",
                "Waar, en dat volgt uit elkaar: een sterk zuur geeft zijn proton zo gemakkelijk "
                "weg dat zijn base het bijna nooit terugneemt. Daarom reageert een chloride-ion in "
                "water helemaal niet.",
                "Niet waar. Een zwak zuur in hoge concentratie kan ook een lage pH geven, want er "
                "zijn dan heel veel moleculen die elk een beetje ioniseren. Dit is dezelfde les "
                "als bij de eerste uitspraak.",
            ],
        ),
        dict(
            aanpak="Kijk bij een zout naar zijn twee ionen en vraag je van elk of het met water "
                   "reageert. Komt het van een sterk zuur of een sterke base, dan doet het niets; "
                   "komt het van een zwak zuur, dan maakt het de oplossing basisch, en komt het van "
                   "een zwakke base, dan zuur.",
            waarom=[
                "Zet de drie naast elkaar: NaCl komt van een sterk zuur en een sterke base, dus "
                "neutraal; acetaat komt van een zwak zuur, dus basisch; ammonium komt van een "
                "zwakke base, dus zuur.",
                None,
                "Noem de hele keten: zwak zuur, dus sterke geconjugeerde base, dus die pakt een "
                "proton van water af, dus er komt OH⁻ vrij. Zonder die laatste stap is het "
                "antwoord niet volledig.",
                "Noem allebei: wat gelijk is en wat verschilt. Dit is de proef die het verschil "
                "tussen sterk en zwak zichtbaar maakt, en ze verklaart ook waarom azijn eetbaar is "
                "en zoutzuur niet.",
            ],
        ),
        dict(
            aanpak="Een pH-meter geeft een getal, een indicator geeft een gebied. Kies dus een "
                   "indicator waarvan het omslaggebied bij de pH ligt die je wil zien, en gebruik "
                   "een meter als je een precieze waarde nodig hebt.",
            waarom=[
                "Onthoud van fenolftaleïen de twee kleuren en de richting: kleurloos in zuur, roze "
                "in base. Dat is de indicator die bij een titratie met een sterke base het vaakst "
                "gebruikt wordt.",
                "Noem dat de indicator zelf een zwak zuur is, want daarmee verklaar je waarom ze "
                "net rond haar pKz omslaat. Daarom heeft elke indicator haar eigen omslaggebied.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ph-poh-en-rekenen-met-zuren-en-basen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Houd één regel vast: pH plus pOH is 14 bij 25 graden. Onder 7 is zuur, boven 7 "
                   "is basisch, 7 is neutraal. Met die twee dingen vul je de hele tabel in.",
            waarom=[
                "Controleer elke rij met de som: 3 plus 11 is 14, 13 plus 1 is 14. En let op de "
                "rijen waar pOH gegeven is, want dan moet je eerst de pH berekenen voor je kan "
                "zeggen of het zuur of basisch is.",
            ],
        ),
        dict(
            aanpak="Bij een sterk zuur is de pH de negatieve exponent van de concentratie: 0,1 "
                   "mol/L is tien tot de min één, dus pH 1. Bij een sterke base reken je eerst de "
                   "pOH en dan pH is 14 min pOH.",
            waarom=[
                "Schrijf de concentratie als een macht van tien, dan kan je de pH gewoon aflezen: "
                "0,001 is tien tot de min drie, dus pH 3.",
                "Let op de extra stap bij een base: 0,01 mol/L NaOH geeft pOH 2, en dus pH 12. Wie "
                "die stap overslaat, komt op pH 2 uit en dus 10 eenheden ernaast.",
                "Reken na: H₂SO₄ is tweewaardig, dus 0,05 mol/L geeft 0,1 mol/L hydroxonium en dus "
                "pH 1. De waardigheid vermenigvuldigen is hier de hele truc.",
            ],
        ),
        dict(
            aanpak="Nu de omgekeerde richting: de concentratie is tien tot de macht min de pH. "
                   "Vraagt men naar hydroxide bij een gegeven pH, reken dan eerst de pOH uit met "
                   "14 min pH.",
            waarom=[
                "Let op de tweede: bij pH 9 is de pOH 5, dus is [OH⁻] tien tot de min vijf. Men "
                "vraagt hier naar hydroxide, dus moet je eerst omrekenen.",
                None,
            ],
        ),
        dict(
            aanpak="De pH-schaal is logaritmisch: één eenheid verschil is een factor tien. Trek "
                   "dus de twee pH-waarden van elkaar af en zet dat verschil als exponent op tien.",
            waarom=[
                "Reken na: het verschil tussen pH 2 en pH 5 is 3, dus tien tot de derde, dus 1000 "
                "keer. Zo kan je elke vergelijking in deze rij in één stap doen.",
                "Noem het bereik van de concentraties, want dat is de reden voor de schaal. "
                "Dezelfde truc zit achter de decibel en achter de schaal van de "
                "aardbevingsmagnitude.",
            ],
        ),
        dict(
            aanpak="Tien keer verdunnen verschuift de pH van een sterk zuur één eenheid naar "
                   "boven, honderd keer twee eenheden. Maar een zuur wordt door verdunnen nooit een "
                   "base: de pH kruipt enkel naar 7 toe.",
            waarom=[
                None,
                "Niet waar, en dit is de grens van de regel hierboven. Hoe sterk je ook verdunt, je "
                "nadert 7 en gaat er niet voorbij, want het water zelf levert nog altijd evenveel "
                "hydroxonium als hydroxide.",
                "Waar. Inkoken maakt de oplossing concentreerder, en meer hydroxonium per liter "
                "betekent een lagere pH.",
                "Noem de zuurconstante, want dat is wat er extra nodig is. Dit is precies waarom "
                "de opdracht bij de tweede reeks zegt dat alle zuren daar sterk zijn.",
            ],
        ),
        dict(
            aanpak="Bij mengen reken je in mol en niet in pH: pH-waarden mag je nooit optellen of "
                   "gemiddelden. Vergelijk het aantal mol zuur met het aantal mol base en kijk wat "
                   "overblijft.",
            waarom=[
                "Noem beide stappen: de mol zijn gelijk, dus volledige neutralisatie, en het zout "
                "dat overblijft reageert niet met water. Dat tweede is nodig, want bij azijnzuur "
                "en NaOH zou het antwoord boven 7 liggen.",
                "Noem dat het aantal mol beslist en niet de ionisatiegraad. Daarom meet een "
                "titratie de hoeveelheid zuur en niet de sterkte ervan, en kan je met dezelfde "
                "titratie azijn en zoutzuur bepalen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-buffers-en-zuurbasetitraties-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een buffer vraagt een zwak zuur met zijn geconjugeerde base, beide in "
                   "voldoende hoeveelheid. Is het zuur sterk of de base sterk, dan buffert het "
                   "niet: de geconjugeerde partner is dan te zwak om nog iets op te vangen.",
            waarom=[
                "Houd de toets vast: is het zuur van het paar een zwak zuur? Salpeterzuur is "
                "sterk, dus is nitraat een verwaarloosbaar zwakke base en vangt het geen zuur op.",
                "Bij natriumhydroxide met natriumchloride is er geen geconjugeerd paar: chloride "
                "hoort bij zoutzuur en niet bij hydroxide. Zo'n mengsel is enkel een sterke base "
                "met een gewoon zout erbij.",
            ],
        ),
        dict(
            aanpak="Kies het paar waarvan de pKz zo dicht mogelijk bij de gewenste pH ligt. Een "
                   "buffer werkt ongeveer van één eenheid onder tot één eenheid boven zijn pKz, "
                   "dus telt dat getal het zwaarst.",
            waarom=[
                "Vergelijk gewoon de pKz met de gevraagde pH: 7,2 bij pH 7, 9,2 bij pH 9 en 3,9 "
                "bij pH 4. Dat diwaterstoffosfaat bij pH 7 past, is ook de reden dat het in het "
                "lichaam als buffer dient.",
                "Reken na: pKz 4,8 min 1 is 3,8 en plus 1 is 5,8. Dat gebied van twee eenheden "
                "breed geldt voor elke buffer.",
            ],
        ),
        dict(
            aanpak="Een buffer vangt op: voeg je base toe, dan reageert het zuur van het paar; "
                   "voeg je zuur toe, dan reageert de base. Houd daarbij twee dingen apart: de pH "
                   "volgt uit de verhouding, de capaciteit uit de hoeveelheid.",
            waarom=[
                "Schrijf de reactie uit en noem ook wat er verandert: er is nadien iets minder "
                "zuur en iets meer base in het paar, dus schuift de verhouding en dus de pH een "
                "beetje op.",
                "Noem het woord verhouding, want dat is de kern. Dit is het verschil met een "
                "gewoon zuur, waar verdunnen de pH wel verandert.",
                "Dit is de tweede helft van hetzelfde idee: dezelfde verhouding geeft dezelfde pH, "
                "een grotere hoeveelheid geeft meer capaciteit. Een buffer kiest dus op pKz en "
                "doseert op capaciteit.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken die de grenzen van een buffer aftasten. Onthoud dat een buffer "
                   "het best werkt bij gelijke concentraties van zuur en base, en dat hij wel "
                   "uitgeput kan raken.",
            waarom=[
                "Bij gelijke concentraties is de pH gelijk aan de pKz, en kan de buffer in beide "
                "richtingen evenveel opvangen. Dat is het punt waarop hij het sterkst is.",
                "Niet waar: hij dempt, hij blokkeert niet. Daarom spreekt men van bufferen en niet "
                "van vastzetten.",
                "Waar, en het bloed is daarmee het belangrijkste voorbeeld uit het dagelijks leven. "
                "Juist dat paar verklaart ook waarom snel ademen de pH van het bloed verandert.",
                "Waar, en dat is precies wat je op een titratiecurve ziet: zolang de buffer werkt "
                "loopt de curve vlak, daarna gaat ze steil omhoog.",
            ],
        ),
        dict(
            aanpak="Houd het glaswerk en zijn plaats in de opstelling vast: het titrans in de "
                   "buret, het staal in de erlenmeyer, en precies afmeten met een pipet. Spoel de "
                   "buret altijd met titrans, nooit met water.",
            waarom=[
                None,
                "Spoelen met titrans en aflezen aan de onderkant van de meniscus zijn de twee "
                "handelingen die de hele meting kunnen bederven. De eerste komt bij vraag 20 "
                "terug.",
            ],
        ),
        dict(
            aanpak="Reken altijd in drie stappen: mol titrans, dan de molverhouding uit de "
                   "vergelijking, dan delen door het volume van het staal in liter. Let op de "
                   "waardigheid, want bij H₂SO₄ hoort twee keer zoveel base.",
            waarom=[
                "Reken na: 25,0 mL maal 0,100 mol/L is 2,50 mmol base, dus ook 2,50 mmol zuur in "
                "25,0 mL, dus 0,100 mol/L. Gelijke volumes en gelijke concentratie: dit is het "
                "ijkpunt van de reeks.",
                "Half zoveel volume base betekent half zoveel mol zuur in hetzelfde staal, dus de "
                "helft van de concentratie.",
                "Reken na: 30,0 mL maal 0,100 is 3,00 mmol NaOH, gedeeld door 2 is 1,50 mmol "
                "H₂SO₄, en dat in 20,0 mL geeft 0,0750 mol/L. De deling door twee is hier de hele "
                "oefening.",
                "Let op dat hier de base het staal is en het zuur het titrans: 15,0 maal 0,200 is "
                "3,00 mmol HCl, dus 3,00 mmol NaOH in 10,0 mL, dus 0,300 mol/L.",
            ],
        ),
        dict(
            aanpak="Op een titratiecurve lees je drie dingen: waar het equivalentiepunt ligt, waar "
                   "het vlakke bufferstuk zit, en hoe steil de sprong is. Het equivalentiepunt "
                   "ligt bij een zwak zuur boven 7 en bij een zwakke base onder 7.",
            waarom=[
                "Het zout dat na de titratie overblijft, bepaalt de pH van het equivalentiepunt. "
                "Dit is dezelfde regel als bij de zouten in de vorige bundel.",
                "Noem de buffer én het punt waar de pH gelijk is aan de pKz, want dat laatste is "
                "een van de manieren om een pKz te meten.",
                "Noem de richting van de fout, want dat is wat de vraag beoordeelt: een te groot "
                "volume geeft een te hoog resultaat. Een fout waarvan je de richting kent, kan je "
                "nadien inschatten.",
                "Noem allebei: hoe je kiest, en waarom het bij een verdund zuur moeilijker is. Een "
                "kleinere sprong betekent minder marge, en dan verschuift het eindpunt van de "
                "indicator merkbaar van het echte equivalentiepunt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-oxidatiegetallen-en-redoxreacties-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Werk met vaste regels: in een enkelvoudige stof is het oxidatiegetal nul, "
                   "waterstof is +I en zuurstof −II, en de som moet gelijk zijn aan de lading van "
                   "het deeltje. Los dan op naar de onbekende.",
            waarom=[
                "Reken SO₂ na: twee keer min II is min IV, en de som moet nul zijn, dus is zwavel "
                "+IV. Dezelfde rekensom werkt voor elk oxide.",
                "Bij een ion moet de som de lading geven: bij SO₄²⁻ is vier keer min II min "
                "VIII, dus moet zwavel +VI zijn om op min II uit te komen.",
            ],
        ),
        dict(
            aanpak="Dezelfde regels, nu voor stikstof. Stikstof komt in heel veel "
                   "oxidatietoestanden voor, van −III tot +V, dus moet je hier echt rekenen en "
                   "niet onthouden.",
            waarom=[
                "Reken NH₃ na: drie keer +I is +III, de som moet nul zijn, dus is stikstof −III.",
                "Let op het verschil tussen NO₂ en NO₂⁻: dezelfde atomen, maar bij het ion moet de "
                "som min I geven, en daarom is stikstof daar +III in plaats van +IV.",
            ],
        ),
        dict(
            aanpak="Bij koolstof in een organische molecule reken je per koolstofatoom, met "
                   "waterstof +I en zuurstof −II. Een stijging van het oxidatiegetal is een "
                   "oxidatie, een daling een reductie.",
            waarom=[
                "In ClO₄⁻ moet de som min I geven: vier keer min II is min VIII, dus is chloor "
                "+VII. Dat is het hoogste dat chloor kan halen.",
                "Reken CH₃OH na: drie waterstof op koolstof plus een OH-groep geeft voor koolstof "
                "min II. Bij HCOOH is het +II, en dat verschil is precies de volgende vraag.",
                "Noem de drie getallen op een rij, want daarmee is het antwoord af: min II, nul, "
                "plus II. Dit is ook de reeks die in het lichaam gebeurt wanneer alcohol wordt "
                "afgebroken.",
            ],
        ),
        dict(
            aanpak="Tel de verandering van het oxidatiegetal en je weet hoeveel elektronen er "
                   "bewegen. Stijgt het, dan is het een oxidatie en gaan er elektronen af; daalt "
                   "het, dan is het een reductie.",
            waarom=[
                None,
                "Reken het permanganaat na: mangaan gaat van +VII in MnO₄⁻ naar +II, dus vijf "
                "stappen, dus vijf elektronen. Die vijf komt in elke titratie met permanganaat "
                "terug.",
            ],
        ),
        dict(
            aanpak="Houd de rolverdeling vast: de reductor staat elektronen af en wordt zelf "
                   "geoxideerd, de oxidator neemt ze op en wordt zelf gereduceerd. Het klinkt "
                   "omgekeerd en het is het niet.",
            waarom=[
                "Zet het per paar: zink geeft, koperion neemt. Zuurstof is de bekendste oxidator "
                "van allemaal, en daar komt het woord oxidatie van.",
                None,
                "Niet waar, en dit is de valkuil van het hele hoofdstuk. Een reductor staat "
                "elektronen af; hij reduceert de andere stof en wordt zelf geoxideerd.",
                "Waar, en dat is de reden dat je de halfreacties met een factor moet "
                "vermenigvuldigen voor je ze optelt.",
                "Niet waar: zuurstof opnemen is juist oxideren. Het is de oudste betekenis van het "
                "woord, en de moderne betekenis met elektronen omvat ze.",
            ],
        ),
        dict(
            aanpak="Vergelijk de twee standaardpotentialen. De reactie gaat spontaan door als de "
                   "oxidator de hogere waarde heeft dan het koppel dat moet oxideren; in de "
                   "praktijk: een metaal lost op in de oplossing van een metaal dat hoger in de "
                   "tabel staat.",
            waarom=[
                "Reken één na: koper staat op +0,34 en zilver op +0,80, dus kan zilverion koper "
                "oxideren en niet omgekeerd. Daarom slaat er zilver neer op een koperdraad in een "
                "zilveroplossing.",
                "Lood op min 0,13 kan zink op min 0,76 niet oxideren, dus gaat die eerste niet "
                "door. Zink en koper wel, en dat is precies de klassieke zinkkoperbatterij.",
                "Noem beide helften: hydroxonium is een te zwakke oxidator voor koper, nitraat is "
                "een sterkere. Dit verklaart waarom men koper met salpeterzuur wel kan oplossen en "
                "waarom er dan bruine damp vrijkomt.",
                "Noem wat je ziet én de reden met de tabel erbij. Dat de spijker roodbruin wordt "
                "en de blauwe kleur verbleekt, is de zichtbare kant van de elektronenoverdracht.",
            ],
        ),
        dict(
            aanpak="Een redoxvergelijking opstellen gaat altijd in dezelfde orde: oxidatiegetallen, "
                   "halfreacties, elektronen gelijkmaken, optellen, en tot slot de atomen en de "
                   "lading laten kloppen. Ga die stappen in die orde af en sla er geen over.",
            waarom=[
                "Noem alle stappen, en vooral het gelijkmaken van de elektronen, want daar hangt "
                "de hele vergelijking aan. Bij elke stap die je overslaat, loopt het aantal "
                "elektronen mis.",
                "Noem beide controles én de nuance dat de lading niet nul hoeft te zijn, enkel "
                "links en rechts gelijk. Dat is net wat bij een ionenvergelijking vaak verkeerd "
                "begrepen wordt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-galvanische-cellen-en-elektrolyse-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Houd één regel vast die in beide cellen geldt: oxidatie aan de anode, "
                   "reductie aan de kathode. Wat wel omdraait, is de pool: in een galvanische cel "
                   "is de anode negatief, bij een elektrolyse positief.",
            waarom=[
                "Vul de tabel rij per rij in en let op de omkering in de twee middelste rijen. Die "
                "omkering is het hele verschil tussen de twee cellen.",
                "Waar, en dit is de regel die je altijd mag gebruiken. Een handig steuntje: anode "
                "en oxidatie beginnen beide met een klinker, kathode en reductie met een "
                "consonant.",
                "Niet waar, en dit is de valkuil. Bij een elektrolyse hangt de anode aan de "
                "positieve pool van de spanningsbron, want daar worden de elektronen weggezogen.",
            ],
        ),
        dict(
            aanpak="De bronspanning is het verschil tussen de twee normpotentialen: de hoogste min "
                   "de laagste. Het metaal met de laagste waarde is de anode en lost op, het "
                   "andere is de kathode.",
            waarom=[
                "Reken na: 0,80 min 0,34 is 0,46 V, en 0,34 min min 0,44 is 0,78 V. Let op het "
                "dubbele minteken in de tweede, want daar gaat het vaak mis.",
                "Reken na: 0,80 min min 0,76 is 1,56 V, en 0,34 min min 1,66 is 2,00 V. Hoe verder "
                "de twee metalen in de tabel uit elkaar staan, hoe hoger de spanning.",
                "Van ijzer en zilver staat ijzer het laagst, dus is ijzer de anode en lost het op. "
                "De anode is altijd het onedelste van de twee.",
                "Van aluminium en zink staat zink het hoogst, dus is zink de kathode. Dat volgt "
                "rechtstreeks uit de vorige regel.",
            ],
        ),
        dict(
            aanpak="Zet alles vast aan de anode: oxidatie, elektronen vertrekken, de elektrode "
                   "lost op en wordt dunner, en de negatieve ionen van de zoutbrug komen erheen om "
                   "de lading te compenseren. Aan de kathode is het telkens het omgekeerde.",
            waarom=[
                None,
                "Dat de negatieve ionen naar de anode gaan, volgt uit de lading: daar ontstaan "
                "positieve metaalionen, dus moet er negatieve lading bij om het in evenwicht te "
                "houden.",
            ],
        ),
        dict(
            aanpak="Drie open vragen over hoe een cel werkt. Noem telkens de ladingen, want dat "
                   "is wat de werking verklaart: elektronen door de draad, ionen door de zoutbrug, "
                   "en de twee halfreacties op twee gescheiden plaatsen.",
            waarom=[
                "Noem beide helften: wat de draad doet en wat de zoutbrug doet. Zonder de "
                "zoutbrug stopt de cel na een fractie van een seconde, en dat is het punt van de "
                "vraag.",
                "Lees zo'n voorstelling van links naar rechts: links de anode, rechts de kathode, "
                "de dubbele streep is de zoutbrug. Schrijf bij elke kant de halfreactie uit.",
                "Noem dat de twee halfreacties gescheiden moeten zijn. Dit verklaart waarom een "
                "batterij uit twee kamers bestaat, en waarom dezelfde reactie in één beker enkel "
                "warmte geeft.",
            ],
        ),
        dict(
            aanpak="Bij een elektrolyse wordt aan de kathode gereduceerd en aan de anode "
                   "geoxideerd, net als altijd. Vraag je dus wat er in het mengsel te reduceren "
                   "valt (het metaalion of water) en wat er te oxideren valt (het anion of water).",
            waarom=[
                "Bij gesmolten keukenzout zijn de enige kandidaten natriumion en chloride-ion, dus "
                "krijg je natriummetaal en chloorgas. Zo wordt natrium industrieel gemaakt.",
                "Bij water zelf krijg je waterstof aan de kathode en zuurstof aan de anode, in de "
                "verhouding twee op één. Dat is precies de verhouding in de formule van water.",
                "Zonder bewegende ionen is er geen stroomgeleiding in de vloeistof. Daarom moet "
                "een zout gesmolten of opgelost zijn, en dat is dezelfde reden als bij een "
                "ionrooster dat niet geleidt.",
                "Noem de plaats van aluminium in de tabel, want daar zit het antwoord. Dat de "
                "elektrolyse zoveel stroom kost, is ook de reden dat aluminium recycleren veel "
                "minder energie vraagt dan het winnen uit erts.",
            ],
        ),
        dict(
            aanpak="Galvaniseren is een elektrolyse waarbij het voorwerp aan de kathode hangt. "
                   "Denk telkens door: reductie aan de kathode, dus daar slaat het metaal neer, en "
                   "de anode van hetzelfde metaal lost op om de oplossing op peil te houden.",
            waarom=[
                "Noem beide elektroden en hun rol. Dat de anode van zilver is en langzaam oplost, "
                "is het stukje dat men vaak vergeet en dat het hele proces draaiend houdt.",
                "Noem dat ontladen spontaan is en opladen gedwongen. Daarmee verbind je deze bundel "
                "met de vorige: hetzelfde paar stoffen, twee richtingen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-toepassingen-van-redox-batterijen-galvaniseren-en-corrosie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie toestellen met dezelfde chemie en een ander gebruik. Een batterij heeft "
                   "zijn stoffen in zich en raakt leeg, een accu kan je terugduwen met een "
                   "elektrolyse, en een brandstofcel krijgt zijn stoffen voortdurend aangevoerd.",
            waarom=[
                None,
                "Dat een brandstofcel enkel water achterlaat, is de reden dat men ze in voertuigen "
                "wil gebruiken. Dat de waterstof ergens gemaakt moet worden, is daarbij wel de "
                "echte vraag.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken over batterijen. Houd twee dingen uit elkaar: de spanning in "
                   "volt zegt hoe sterk de reactie duwt, de capaciteit in ampère-uur zegt hoeveel "
                   "lading erin zit.",
            waarom=[
                "Niet waar, en dit is ook gevaarlijk. In een alkalinebatterij is de reactie niet "
                "omkeerbaar; opladen laat er gas in ontstaan en kan haar doen openbarsten of "
                "lekken.",
                None,
                "Waar. Zonder weerstand in de kring loopt er heel veel stroom, en dan komt alle "
                "energie in korte tijd als warmte vrij.",
                "Niet waar. Volt zegt hoeveel energie per lading, niet hoeveel lading. Een kleine "
                "en een grote batterij van 1,5 V hebben dezelfde spanning en een heel verschillende "
                "capaciteit.",
            ],
        ),
        dict(
            aanpak="Drie keer de vraag waarom. Noem bij elk antwoord de chemie én het gevolg: wat "
                   "er opgebruikt raakt, welke richting de reactie opgaat, en wat er in het afval "
                   "zit.",
            waarom=[
                "Noem het opgebruiken van de reagentia tegenover het aanvoeren ervan. Dat is het "
                "hele verschil tussen een gesloten en een open systeem.",
                "Dit is dezelfde uitleg als bij de galvanische cel en de elektrolyse: spontaan "
                "tegenover gedwongen. Gebruik die twee woorden, want ze maken het antwoord "
                "precies.",
                "Noem de zware metalen bij naam en zeg waar ze terechtkomen. Dat ze teruggewonnen "
                "worden, is het argument om ze echt naar de inzameling te brengen en niet gewoon "
                "weg te gooien.",
            ],
        ),
        dict(
            aanpak="Bij galvaniseren hangt het voorwerp altijd aan de kathode en is de anode van "
                   "het metaal dat je wil opbrengen. De dikte van het laagje hangt af van de "
                   "stroomsterkte en de tijd.",
            waarom=[
                None,
                "Noem beide: de tijd en de stroomsterkte. Samen bepalen ze hoeveel lading er "
                "gepasseerd is, en de hoeveelheid neergeslagen metaal is daaraan recht "
                "proportioneel.",
                "Noem dat enkel het buitenste laagje telt voor het uitzicht en de bescherming. Dat "
                "is ook de reden dat verzilverd bestek na jaren slijten het onderliggende metaal "
                "laat zien.",
            ],
        ),
        dict(
            aanpak="Roesten is een redoxreactie waarbij ijzer de reductor is: het staat elektronen "
                   "af aan zuurstof. Water is nodig als medium, en zout versnelt het omdat het het "
                   "water geleidend maakt.",
            waarom=[
                "Noem beide stoffen, want met één van de twee gebeurt er niets: droog ijzer in "
                "zuurstof roest niet, en ijzer in zuurstofvrij water ook niet.",
                "IJzer staat zijn elektronen af, dus is het de reductor, en zuurstof is de "
                "oxidator. Dat klinkt omgekeerd aan het woord oxideren, en het is dezelfde valkuil "
                "als in de vorige bundel.",
                "Zout water geleidt, dus kunnen de elektronen en de ionen gemakkelijker van de ene "
                "plaats naar de andere. Daarom roest een auto aan de kust en na een winter met "
                "strooizout veel sneller.",
                "Niet waar, en dit is het verschil dat in vraag 20 uitgelegd wordt. Roest is "
                "poreus en laat lucht en water door, dus gaat het roesten eronder verder.",
            ],
        ),
        dict(
            aanpak="Er zijn twee manieren om ijzer te beschermen: afsluiten van lucht en water, of "
                   "er een sterkere reductor bij zetten die zich laat opeten. Vraag je dus: sluit "
                   "dit af, of is dit metaal onedeler dan ijzer?",
            waarom=[
                "Vergelijk zink en tin: zink is onedeler dan ijzer en beschermt dus ook bij een "
                "kras, tin is edeler en maakt het bij een kras juist erger. Verf beschermt enkel "
                "zolang ze gesloten is.",
                "Een magnesiumblok is een opofferingsanode, en het ijzer aan de positieve pool "
                "leggen is precies het omgekeerde: dan dwing je het ijzer in de rol van anode en "
                "laat je het versneld oplossen.",
                "Noem de plaats van zink en tin tegenover ijzer in de tabel, want daarmee verklaar "
                "je beide gevallen in één keer. Dat is ook waarom men het verzinken van staal "
                "galvaniseren met een opofferende laag noemt.",
                "Noem het verschil tussen een dichte en een poreuze oxidelaag. Dat is de reden dat "
                "aluminium zonder bescherming buiten kan en staal niet.",
                "Noem beide delen van de vraag: wat ze is en waarom ze onderhoud vraagt. Een "
                "opofferingsanode die opgebruikt is en niet vervangen wordt, geeft valse "
                "veiligheid, en dat is net het punt van de vraag.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-organische-reacties-substitutie-en-het-radicalaire-mechanisme-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Tel bij elk voorbeeld wat er in en uit de molecule gaat. Gaat er iets weg en "
                   "komt er iets anders in de plaats, dan is het een substitutie. Komt er enkel "
                   "iets bij, een additie. Gaat er enkel iets weg en blijft er een dubbele binding "
                   "achter, een eliminatie. Koppelen twee moleculen met water als bijproduct, een "
                   "condensatie.",
            waarom=[
                None,
                "Een condensatie herken je aan het water dat vrijkomt: alcohol plus carbonzuur "
                "geeft een ester en water. Methaan met chloorgas is wel een substitutie, want het "
                "chloor neemt de plaats van een waterstofatoom in.",
            ],
        ),
        dict(
            aanpak="De aanvaller volgt uit de omstandigheden. Uv-licht of warmte betekent dat er "
                   "radicalen gemaakt worden. Een katalysator die een molecule polariseert, maakt "
                   "een elektrofiel. Een deeltje met een vrij elektronenpaar, zoals water of "
                   "ammoniak, is een nucleofiel.",
            waarom=[
                "Let op het verschil tussen de eerste twee: beide zijn een halogenering, maar "
                "propaan heeft licht nodig en benzeen een katalysator. Dat verschil komt terug in "
                "oefening 16 en 18.",
                "Ammoniak heeft een vrij elektronenpaar op de stikstof, dus is het een nucleofiel. "
                "Cyclohexaan is ondanks de ring een gewoon alkaan, dus gaat het radicalair.",
            ],
        ),
        dict(
            aanpak="Een radicaalreactie heeft altijd drie stappen. Initiatie: er worden radicalen "
                   "gemaakt. Propagatie: een radicaal reageert en er ontstaat een nieuw radicaal. "
                   "Terminatie: twee radicalen koppelen en er blijft er geen over.",
            waarom=[
                "Kijk telkens naar het aantal radicalen voor en na de stap: nul wordt twee bij de "
                "initiatie, één blijft één bij de propagatie, en twee wordt nul bij de terminatie.",
                "Omdat er een nieuw radicaal uitkomt, kan dat meteen de volgende molecule "
                "aanvallen. Daarom levert één lichtdeeltje duizenden reacties op.",
                "Ethaan komt uit een terminatiestap. Dat die bijproducten erbij horen, is ook het "
                "antwoord op oefening 19.",
            ],
        ),
        dict(
            aanpak="Schrijf bij een substitutie altijd het tweede product mee: het atoom dat "
                   "weggaat, komt met de waterstof als HCl of HBr vrij. Bij een nucleofiele "
                   "substitutie blijft het halogeen als ion achter.",
            waarom=[
                None,
                "Het bromide-ion blijft los in de oplossing achter, want het neemt het "
                "elektronenpaar mee. Dat is net het verschil met het radicalaire verloop, waar HBr "
                "als molecule vrijkomt.",
                "Twee alcoholen geven een ether en water, met zwavelzuur en een lagere temperatuur. "
                "Bij een hogere temperatuur krijg je een eliminatie en dus een alkeen, en dat komt "
                "in de volgende bundel terug.",
            ],
        ),
        dict(
            aanpak="Homo betekent gelijk en hetero betekent ongelijk. Bij een homolytische "
                   "splitsing wordt het elektronenpaar eerlijk verdeeld en krijg je twee radicalen; "
                   "bij een heterolytische neemt één atoom het hele paar mee en krijg je twee ionen.",
            waarom=[
                None,
                None,
                "Niet waar, en dit is precies de verwisseling van de twee woorden. Heterolytisch "
                "geeft ionen, homolytisch geeft radicalen.",
                "Waar. Een ongepaard elektron zoekt een partner, en daarom leeft een radicaal "
                "meestal maar een fractie van een seconde.",
                "Waar. Dat is wat een nucleofiel tot nucleofiel maakt: het brengt elektronen mee "
                "en zoekt dus een plaats met een elektronentekort.",
            ],
        ),
        dict(
            aanpak="Vijf keer waarom. Zoek het antwoord telkens bij de ladingsverdeling in de "
                   "molecule: waar zit er een overschot of een tekort aan elektronen? Dat bepaalt "
                   "welke aanvaller er terechtkan.",
            waarom=[
                "Noem de twee helften: waarom een alkaan geen aangrijpingspunt heeft, en waarom een "
                "halogeenalkaan er wel een heeft. Dat verklaart in één keer de eerste reeks van "
                "deze bundel.",
                "Noem de verspreide pi-elektronen en de stabiliteit die ze geven. Dat is dezelfde "
                "stabiliteit waardoor benzeen geen broomwater ontkleurt, terwijl een gewoon alkeen "
                "dat wel doet.",
                "Noem dat de katalysator het broom polariseert. Zonder dat zou je uit de vorige "
                "oefening kunnen besluiten dat benzeen helemaal niet reageert, en dat is te sterk.",
                "Noem beide bronnen van bijproducten: de verdere substitutie en de terminatie. Dat "
                "het mengsel moeilijk te scheiden is, is ook de reden dat men industrieel liever "
                "een andere weg kiest.",
                "Noem het verschil in katalysator en in product: een zuur geeft het carbonzuur "
                "terug, een base geeft het zout ervan. Dat zout is zeep, en dat verklaart de naam "
                "verzeping.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-organische-reacties-additie-eliminatie-en-condensatie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Bij een additie gaat de pi-binding open en komen de twee delen van de "
                   "aanvallende stof elk aan een kant van de vroegere dubbele binding. Er gaat "
                   "niets weg, dus zit alles van beide moleculen in het product.",
            waarom=[
                None,
                "Een drievoudige binding kan twee keer adderen, dus heb je twee keer diwaterstof "
                "nodig om bij een alkaan uit te komen. Dat komt terug in oefening 5.",
            ],
        ),
        dict(
            aanpak="De regel van Markownikov zegt waar het waterstofatoom terechtkomt bij een "
                   "asymmetrische stof: op het koolstofatoom dat er al het meeste heeft. De andere "
                   "groep komt dus op het meest vertakte koolstofatoom.",
            waarom=[
                "Vergelijk de drie: telkens komt de groep op het middelste of het tweede "
                "koolstofatoom, nooit op het buitenste. Daarom krijg je propaan-2-ol en geen "
                "propaan-1-ol.",
                "Noem waar de waterstof naartoe gaat, niet enkel waar de andere groep blijft. "
                "Een handig steuntje: de rijke wordt rijker.",
            ],
        ),
        dict(
            aanpak="Tel het aantal pi-bindingen: een alkaan heeft er geen, een alkeen één, een "
                   "alkyn twee. Zoveel keer kan diwaterstof adderen.",
            waarom=[
                None,
                "Noem de additie aan de dubbele binding. Dat het broomwater ontkleurt, is daardoor "
                "een eenvoudige test op onverzadigdheid, en die test gebruikt men ook om olie van "
                "vet te onderscheiden.",
            ],
        ),
        dict(
            aanpak="Een eliminatie gaat de andere kant op dan een additie: er gaat iets weg en er "
                   "komt een dubbele binding bij. Gaat er water weg, dan heet het een dehydratatie; "
                   "gaat er waterstof weg, een dehydrogenatie.",
            waarom=[
                "Let op wat er in beide gevallen weggaat: water bij de alcohol, HBr bij het "
                "halogeenalkaan. Het product is in beide gevallen hetzelfde alkeen.",
                "Bij een primaire alcohol krijg je een aldehyde, bij een secundaire een keton. Zet "
                "dat naast de tabel van oefening 11, want het is dezelfde regel.",
                "Noem dat er twee buuratomen met een waterstof zijn. Daarom levert een dehydratatie "
                "vaak een mengsel op in plaats van één product.",
                "Noem beide helften: waarom de dehydrogenatie niet lukt, en waarom de dehydratatie "
                "wel. Het verschil zit in wáár de waterstof moet zitten, op het koolstofatoom zelf "
                "of op een buuratoom.",
            ],
        ),
        dict(
            aanpak="Kijk naar het koolstofatoom waar de OH-groep op zit en tel hoeveel "
                   "koolstofketens eraan hangen. Dat bepaalt meteen wat een oxidatie oplevert.",
            waarom=[
                "Vul de tabel rij per rij in. De derde rij is de reden waarom een tertiaire alcohol "
                "niet verder kan oxideren, en dat is wat oefening 10 uitlegt.",
                "Een aldehyde is een tussenstap: oxideert het verder, dan krijg je het carbonzuur. "
                "Daarom moet je bij een primaire alcohol zeggen hoe ver je oxideert.",
                "Noem de stof die ontstaat. Dit is dezelfde reactie als hierboven, maar nu met een "
                "voorbeeld uit de keuken: ethanol oxideert tot azijnzuur door de zuurstof in de "
                "lucht.",
            ],
        ),
        dict(
            aanpak="Bij een condensatie koppelen twee moleculen en komt er een kleine molecule "
                   "vrij, meestal water. Draai je de reactie om door water toe te voegen, dan heet "
                   "dat hydrolyse.",
            waarom=[
                None,
                None,
                "Met een base krijg je het zout van het carbonzuur in plaats van het zuur zelf, en "
                "dat zout is zeep. Dat is ook waarom verzeping niet omkeerbaar is en hydrolyse wel.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken. Test ze aan de definities: wat gaat er open, wat gaat er weg, "
                   "en wat is er nodig om de reactie op gang te krijgen?",
            waarom=[
                "Waar. De sigma-binding blijft de twee koolstofatomen bij elkaar houden, dus valt "
                "de molecule niet in twee stukken.",
                "Waar. Een additie maakt een dubbele binding dicht, een eliminatie maakt er een "
                "open, en met de juiste omstandigheden kan je dezelfde reactie beide richtingen "
                "uit duwen.",
                "Niet waar. Water is niet elektrofiel genoeg; je hebt een zuur nodig dat eerst een "
                "proton aan de dubbele binding geeft. Dat is dezelfde reden als bij benzeen en de "
                "katalysator in de vorige bundel.",
                "Niet waar. Een ring verandert niets aan de dubbele binding, dus addeert "
                "cyclohexeen gewoon zoals elk ander alkeen.",
            ],
        ),
        dict(
            aanpak="Drie keer uitleggen. Zoek het antwoord in de ladingsverdeling en in wat er met "
                   "de atomen gebeurt, niet in de naam van de reactie.",
            waarom=[
                "Noem de ladingsverdeling in beide gevallen. Bij het alkeen zijn de twee kanten "
                "gelijk, bij de C=O-groep niet, en dat ene verschil bepaalt welke aanvaller er "
                "terechtkan.",
                "Noem dat er bij een additie niets weggaat. Dat is de kortste manier om de twee uit "
                "elkaar te houden, en je kan het nakijken door de atomen te tellen.",
                "Noem de naam van de reactie en wat ze met de ketens doet. Dit verklaart ook "
                "waarom er in zo'n vet minder onverzadigde bindingen zitten en waarom dat een "
                "nadeel is voor de gezondheid.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kunststoffen-polymeren-en-hun-eigenschappen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De naam van de kunststof verraadt het monomeer: poly betekent veel, en wat "
                   "erachter staat is de monomeer. Let wel op de oude namen: etheen heette "
                   "ethyleen, en vandaar PE voor polyetheen.",
            waarom=[
                "Chlooretheen heet ook vinylchloride, en daar komt de v in PVC van. Zulke oude "
                "namen blijven in de industrie hangen, dus is het handig ze te kennen.",
                "Fenyletheen heet ook styreen, vandaar PS. De f van tetrafluoretheen zit in PTFE, "
                "beter bekend als teflon.",
            ],
        ),
        dict(
            aanpak="Dezelfde vraag omgekeerd. Bij een polyadditie is er één monomeer met een "
                   "dubbele binding. Bij een polycondensatie zijn er twee soorten, elk met twee "
                   "reactieve groepen, want anders stopt de keten na één koppeling.",
            waarom=[
                None,
                "Noem telkens dat beide monomeren twéé groepen hebben. Met één groep krijg je een "
                "kleine molecule in plaats van een keten, en dat is net het verschil.",
            ],
        ),
        dict(
            aanpak="Vraag je af of er iets vrijkomt. Komt er niets vrij en zat er een dubbele "
                   "binding in het monomeer, dan is het een polyadditie. Komt er water vrij, dan is "
                   "het een polycondensatie.",
            waarom=[
                "PE en PVC komen uit één monomeer met een dubbele binding, PET uit twee soorten met "
                "elk twee groepen. Dat je bij PET water ziet vrijkomen, is het bewijs van een "
                "condensatie.",
                None,
                "Noem dat bij een polycondensatie massa in het water verdwijnt. Atoomeconomie "
                "betekent precies dat: hoeveel van de massa die je erin stopt, komt er in het "
                "gewenste product uit.",
            ],
        ),
        dict(
            aanpak="Alles hangt af van het aantal bruggen tussen de ketens. Geen bruggen betekent "
                   "dat de ketens langs elkaar kunnen schuiven, dus smelt het en kan je het opnieuw "
                   "vormen. Veel bruggen betekent een vast net dat niet meer kan schuiven.",
            waarom=[
                "Vul de tabel aan met het aantal bruggen én het gedrag bij opwarmen, want het ene "
                "verklaart het andere. Een elastomeer zit in het midden: genoeg bruggen om terug te "
                "veren, te weinig om stijf te zijn.",
                None,
            ],
        ),
        dict(
            aanpak="Kies op de eigenschap die het voorwerp nodig heeft: doorzichtig en luchtdicht, "
                   "stijf en goedkoop, antikleef, isolerend of sterk. De namen zijn de afkortingen "
                   "uit de vorige reeksen.",
            waarom=[
                None,
                "PS-schuim is grotendeels lucht, en dat is net wat het beschermend en isolerend "
                "maakt. Nylon heet ook PA, van polyamide, naar de amidebinding tussen de ketens.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken. Test ze aan het verschil tussen een polyadditie en een "
                   "polycondensatie, en aan het verschil tussen een thermoplast en een "
                   "thermoharder.",
            waarom=[
                None,
                "Niet waar, en dat is wat oefening 16 uitlegt. Een kunststof heeft een smelttraject "
                "omdat de ketens niet alle even lang zijn.",
                "Waar. Een thermoplast kan je opnieuw smelten en vormen; een thermoharder ontleedt "
                "en is dus enkel te vermalen tot vulstof.",
                "Niet waar. PE komt uit etheen en PVC uit chlooretheen, en dat chlooratoom maakt "
                "PVC harder en moeilijker te verbranden.",
            ],
        ),
        dict(
            aanpak="Vijf keer uitleggen. Zoek het antwoord in de ketens zelf: hoe lang ze zijn, hoe "
                   "ze aan elkaar hangen en hoe stabiel ze zijn.",
            waarom=[
                "Noem de verschillende ketenlengtes. Dat is ook de reden dat de molaire massa van "
                "een kunststof een gemiddelde is en geen vast getal.",
                "Noem de repeterende eenheid en het terugzetten van de dubbele binding. Dat is de "
                "omgekeerde weg van reeks 1, en ze werkt bij elke kunststof uit een polyadditie.",
                "Noem de verschillende smelttrajecten en het woord downcycling. Dat verklaart "
                "waarom een pet-fles gescheiden ingezameld wordt en niet bij het ander plastic.",
                "Noem de stabiliteit van de ketens en het ontbreken van enzymen. Diezelfde "
                "stabiliteit die kunststof zo bruikbaar maakt, is dus ook het probleem.",
                "Noem de zwavelbruggen en wat ze doen. Dit is ook een voorbeeld van de tabel bij "
                "oefening 8: rubber wordt door die bruggen een elastomeer.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-nanomaterialen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zet de maten op een rij: een millimeter is een duizendste meter, een "
                   "micrometer een miljoenste, een nanometer een miljardste. Een nanomateriaal "
                   "heeft minstens één afmeting tussen 1 en 100 nanometer.",
            waarom=[
                None,
                "Onder 1 nm zit je bij losse atomen en moleculen, boven 100 nm gedraagt de stof "
                "zich zoals gewoonlijk. Net in dat gebied krijgt een stof andere eigenschappen, en "
                "dat is waar deze bundel over gaat.",
                None,
                "Niet waar. Zichtbaar licht heeft een golflengte van ongeveer 400 tot 700 nm, dus "
                "is een deeltje van een paar nanometer veel kleiner dan het licht waarmee je zou "
                "kijken.",
            ],
        ),
        dict(
            aanpak="Tel hoeveel afmetingen gróter zijn dan de nanomaat. Is alles nano, dan is het "
                   "0D; is één richting lang, dan 1D; zijn er twee lang en één nano, dan 2D.",
            waarom=[
                "Grafeen is één laag koolstofatomen dik, dus nano in één richting en groot in twee: "
                "2D. Een nanobuis is in de lengte groot en in de doorsnede nano: 1D.",
                "Een buckyball is een bol van zestig koolstofatomen, dus in alle richtingen nano. "
                "Bij 3D is het materiaal zelf gewoon groot en zit de nanostructuur erin.",
            ],
        ),
        dict(
            aanpak="Top-down begint groot en maakt kleiner, bottom-up begint bij atomen of "
                   "moleculen en bouwt op. Vraag je dus af of er materiaal weggaat of bijkomt.",
            waarom=[
                None,
                "Bij bottom-up ordenen de deeltjes zich vaak zelf, en dat geeft nauwkeuriger "
                "resultaten. Top-down is eenvoudiger maar levert deeltjes van heel verschillende "
                "grootte op.",
            ],
        ),
        dict(
            aanpak="Hier komt alles uit één rekenfeit: het oppervlak groeit met het kwadraat van de "
                   "afmeting en het volume met de derde macht. Maak een kubus tien keer kleiner en "
                   "je hebt per gram tien keer meer oppervlak.",
            waarom=[
                "Noem de twee machten, want daar zit de uitleg in. Reken het eens na met een kubus "
                "van 1 cm en duizend kubussen van 1 mm: dezelfde massa, tien keer zoveel oppervlak.",
                "Noem beide redenen: meer oppervlak per gram, en atomen aan de buitenkant met "
                "minder buren. Dat laatste verklaart ook oefening 11.",
                "Noem de atomen aan het oppervlak met minder buren. Nanogoud smelt daardoor "
                "honderden graden lager dan gewoon goud, en dat gebruikt men om elektronica bij "
                "lage temperatuur te solderen.",
            ],
        ),
        dict(
            aanpak="Bij elke toepassing zit de reden in een eigenschap die enkel op nanomaat "
                   "bestaat: doorzichtig blijven, een groot oppervlak hebben, of een kleur die van "
                   "de grootte van het deeltje afhangt.",
            waarom=[
                "Op nanomaat zijn zinkoxide en titaandioxide doorzichtig in plaats van wit, en "
                "daarom laat zonnecrème geen witte laag achter. Het goud in een sneltest is rood, "
                "en dat is wat oefening 18 uitlegt.",
                None,
            ],
        ),
        dict(
            aanpak="Vier uitspraken. Het hele punt van deze bundel is dat dezelfde stof zich op "
                   "nanomaat anders gedraagt, dus elke uitspraak die dat tegenspreekt, is fout.",
            waarom=[
                "Niet waar, en dat is de kern van de bundel: kleur, smeltpunt, reactiviteit en "
                "magnetisme kunnen alle veranderen.",
                "Waar. Onder een bepaalde grootte kan een deeltje maar één magnetische richting "
                "hebben, en zulke deeltjes gebruikt men in een MRI en in gegevensopslag.",
                None,
                "Niet waar. Het zit al in zonnecrème, in antibacteriële kleding, in schermen en in "
                "autokatalysatoren.",
            ],
        ),
        dict(
            aanpak="Drie keer uitleggen, waarbij je telkens de twee kanten geeft: wat het kleine "
                   "formaat mogelijk maakt en waar men nog niet alles van weet.",
            waarom=[
                "Noem dat de kleur van de elektronen komt en niet van de stof als zodanig. Zo "
                "maakte men al in de middeleeuwen rood glas met goud, zonder te weten waarom.",
                "Noem beide: het voordeel en het risico. Dat men nog niet alles weet, is geen "
                "zwak antwoord maar precies wat de vraag wil horen.",
                "Noem dat de koper het moet kunnen weten. In Europa is die vermelding verplicht, "
                "en dat is een voorbeeld van het voorzorgsprincipe.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-duurzame-chemie-en-de-circulaire-economie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk waar de stroom van materiaal eindigt. Eindigt ze bij afval, dan is het "
                   "lineair. Eindigt ze opnieuw als grondstof, dan is het circulair. Zit er veel "
                   "hergebruik in maar blijft er toch afval over, dan spreekt men van een keten.",
            waarom=[
                None,
                "Van wieg tot wieg: na gebruik begint het materiaal opnieuw. De uitdrukking komt "
                "van McDonough en Braungart, en ze bedoelen er meer mee dan recycleren alleen.",
                "Van wieg tot graf, dus eenmalig gebruik. Dat is het model waar onze industrie "
                "grotendeels nog op gebouwd is.",
            ],
        ),
        dict(
            aanpak="De ladder gaat van wat je het liefst doet naar wat je enkel nog overhoudt. "
                   "Boven staat wat materiaal spaart, onder wat het definitief kwijt is.",
            waarom=[
                "Zet de vijf treden in de goede orde en kijk naar het patroon: eerst geen afval "
                "maken, dan het voorwerp zelf houden, dan het materiaal, dan nog de energie, en "
                "pas daarna storten.",
                "Noem dat preventie het hele probleem voorkomt. Daarom staat ook repareren hoog en "
                "recycleren pas in het midden.",
                "Downcycling. Dat is hetzelfde begrip als bij de kunststoffen: het materiaal is nog "
                "bruikbaar maar niet meer voor zijn eerste toepassing.",
            ],
        ),
        dict(
            aanpak="Deze drie woorden worden door elkaar gebruikt en betekenen iets anders. "
                   "Biogebaseerd gaat over waar de grondstof van komt, biodegradeerbaar en "
                   "composteerbaar over wat er na gebruik gebeurt.",
            waarom=[
                None,
                "Niet waar, en dit is de belangrijkste verwarring. Bio-PE komt uit rietsuiker en "
                "is precies dezelfde kunststof als PE uit aardolie, dus even weinig afbreekbaar.",
                "Waar. Composteerbaar betekent dat het binnen een vastgelegde tijd en bij een "
                "vastgelegde temperatuur afbreekt; biodegradeerbaar zegt niet hoe snel of onder "
                "welke omstandigheden.",
            ],
        ),
        dict(
            aanpak="De kleur zegt niets over de stof maar over de manier van maken. Groen uit "
                   "hernieuwbare stroom, grijs uit aardgas met uitstoot, blauw uit aardgas met "
                   "afvangen van de CO2.",
            waarom=[
                "Noem telkens de bron van de energie of de grondstof. Vandaag is het grootste deel "
                "van de waterstof in de wereld nog grijs, en dat is de hele reden dat men over "
                "kleuren praat.",
                "Waar. Het molecule H2 is altijd hetzelfde; enkel de weg ernaartoe verschilt, en "
                "daarom moet je bij een milieuclaim altijd naar die weg vragen.",
            ],
        ),
        dict(
            aanpak="Hier gaan de kleuren over hoe vuil het water is. Wit is drinkbaar, grijs is "
                   "licht vervuild en zwart komt uit het toilet.",
            waarom=[
                "Grijs water is met een eenvoudige zuivering weer bruikbaar voor het toilet of de "
                "tuin, en dat is net waarom men het apart houdt van zwart water.",
            ],
        ),
        dict(
            aanpak="Houd twee getallen uit elkaar. Het rendement vergelijkt wat je eruit haalt met "
                   "wat er maximaal uit kon. De atoomeconomie vergelijkt de massa van het product "
                   "met de massa van alles wat je erin stopte.",
            waarom=[
                None,
                "Bij een additie valt er niets weg, dus zit alle massa in het product. Dat is "
                "waarom de atoomeconomie van een additie altijd 100 procent is, hoe laag het "
                "rendement ook uitvalt.",
                "Noem beide definities naast elkaar. Een reactie kan dus bijna volledig doorgaan en "
                "toch veel afval geven, en dat is net wat de groene chemie wil meten.",
            ],
        ),
        dict(
            aanpak="Vier keer uitleggen. Zoek telkens naar wat er níet in het product terechtkomt: "
                   "het solvent, de energie, de bijproducten. Dat is waar de groene chemie op mikt.",
            waarom=[
                "Noem de verhouding tussen solvent en reagens. Dat die zo scheef zit, is de reden "
                "dat men naar reacties in water of zonder solvent zoekt.",
                "Noem beide voordelen: minder energie en meer selectiviteit. Een katalysator "
                "verandert de ligging van het evenwicht niet, enkel de snelheid, en dat is een "
                "klassieke valkuil.",
                "Noem zowel de vage woorden als het ontbreken van een cijfer of keurmerk. Een "
                "groene verpakking zegt niets over de inhoud, en dat is nu net de bedoeling van "
                "zo'n ontwerp.",
                "Noem twee keuzes, niet één: losmaakbaar en zo weinig verschillende materialen "
                "mogelijk. Dat tweede is dezelfde reden als bij de downcycling van kunststof.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-werken-meetinstrumenten-en-beduidende-cijfers-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Een H-zin zegt wát er gevaarlijk is aan de stof, een P-zin zegt wat jij moet "
                   "doen. Staat er een opdracht in de zin, dan is het een P-zin.",
            waarom=[
                None,
                None,
                "H staat voor hazard, het Engelse woord voor gevaar; P staat voor precaution, dus "
                "voorzorg. De nummers erachter zijn wereldwijd dezelfde, zodat je ze ook in een "
                "andere taal terugvindt.",
            ],
        ),
        dict(
            aanpak="Kies het glaswerk naar de nauwkeurigheid die je nodig hebt. Een maatkolf, een "
                   "pipet en een buret zijn op volume gekalibreerd; een bekerglas en een erlenmeyer "
                   "niet, en hun streepjes zijn enkel een indicatie.",
            waarom=[
                "Let op het verschil tussen de drie: een maatkolf maakt één bepaald volume "
                "oplossing aan, een pipet brengt een vast volume over, en een buret laat je een "
                "wisselend volume nauwkeurig aflezen.",
                "Een erlenmeyer heeft een schuine wand, dus kan je erin zwenken zonder te morsen. "
                "Daarom titreer je erin en niet in een bekerglas.",
                "Lees aan de onderkant van de meniscus, met je oog op dezelfde hoogte. Kijk je van "
                "boven of van onder, dan lees je er systematisch naast, en dat is een systematische "
                "fout zoals in de laatste bundel.",
            ],
        ),
        dict(
            aanpak="Vier uitspraken en een praktijkgeval. Denk bij elk door wat er kan misgaan en "
                   "waarom de regel bestaat.",
            waarom=[
                "Waar. Het verdunnen van een zuur geeft veel warmte; giet je water bij zuur, dan "
                "kan dat beetje water plaatselijk koken en zuur rondspatten. Een handig steuntje: "
                "zuur in water, zoals een duiker in het water.",
                "Waar. Spoel je enkel met water, dan blijven er waterdruppels in de pipet die je "
                "oplossing verdunnen, en dan is je volume wel juist maar je concentratie niet.",
                "Niet waar. Gevarenpictogrammen zijn ruiten met een rode rand en een zwart teken op "
                "wit. Ronde groene tekens zijn gebodsborden, zoals bril verplicht.",
                "Niet waar. Het uitroepteken staat voor schadelijk of irriterend, dus het lichtere "
                "gevaar. Dodelijk giftig heeft de doodskop, en dat verschil is precies waarom er "
                "twee pictogrammen zijn.",
                "Noem de twee stappen in de juiste orde: eerst neutraliseren, dan opnemen. Neem je "
                "het zuur eerst op met papier, dan blijft het bijtend in de vuilnisbak liggen.",
            ],
        ),
        dict(
            aanpak="Meetbereik en resolutie zijn twee verschillende dingen: het bereik zegt tussen "
                   "welke waarden het toestel werkt, de resolutie hoe fijn het binnen dat bereik "
                   "onderscheidt.",
            waarom=[
                None,
                "Noem de resolutie en de onzekerheid. De regel in de praktijk: kies een instrument "
                "waarvan het meetbereik niet veel groter is dan wat je wil meten, en meet liefst in "
                "het midden van het bereik.",
            ],
        ),
        dict(
            aanpak="Voorvoegsels zijn machten van tien: milli is duizendste, micro miljoenste, nano "
                   "miljardste, kilo duizend, mega een miljoen. Vermenigvuldig of deel dus telkens "
                   "met zo'n macht.",
            waarom=[
                None,
                "Reken na: 2,5 nm is 2,5 keer tien tot de min negende meter, 0,5 mL is 5 keer tien "
                "tot de min vierde liter. Let bij de laatste op de nullen: 0,300 g houdt drie "
                "beduidende cijfers, net als 300 mg.",
                None,
                "De kelvin, niet de graad Celsius. Een temperatuurverschil is in beide even groot, "
                "maar het nulpunt ligt anders: 0 K is min 273,15 graden Celsius.",
            ],
        ),
        dict(
            aanpak="Tel van links af vanaf het eerste cijfer dat niet nul is. Nullen vooraan tellen "
                   "nooit, nullen achter de komma wel, en nullen achteraan zonder komma zijn "
                   "dubbelzinnig.",
            waarom=[
                "Bij 0,00310 tellen de drie nullen vooraan niet en de nul achteraan wel, dus drie. "
                "Bij 1200 weet je niet of die nullen gemeten zijn; wil je het duidelijk maken, "
                "schrijf dan 1,200 keer tien tot de derde.",
                "In de wetenschappelijke notatie is het eenvoudig: enkel de cijfers vóór de macht "
                "tellen. Daarom schrijft men meetwaarden graag zo op.",
            ],
        ),
        dict(
            aanpak="Twee verschillende regels. Bij vermenigvuldigen en delen volg je het aantal "
                   "beduidende cijfers van de minst nauwkeurige factor. Bij optellen en aftrekken "
                   "volg je het aantal decimalen van de waarde met de minste decimalen.",
            waarom=[
                "Reken na: 3,2 maal 1,478 is 4,7296, en met twee beduidende cijfers wordt dat 4,7. "
                "25,0 gedeeld door 4,0 is 6,25, en met twee beduidende cijfers 6,3.",
                "Reken na: 14,25 plus 0,3 is 14,55, en met één decimaal 14,6. 8,0 plus 0,125 is "
                "8,125, en met één decimaal 8,1. Rond pas op het einde af, nooit tussenin.",
                "Noem waar de onzekerheid in beide gevallen zit: op een decimaal bij optellen, "
                "relatief bij vermenigvuldigen. Dat verklaart waarom de twee regels anders zijn.",
            ],
        ),
        dict(
            aanpak="In de wetenschappelijke notatie staat er één cijfer voor de komma en een macht "
                   "van tien erachter. Schuif de komma en tel hoeveel plaatsen je opschoof; naar "
                   "links is een positieve macht, naar rechts een negatieve.",
            waarom=[
                None,
                "Recht evenredig geeft een rechte door de oorsprong, dus verdubbelt het ene als het "
                "andere verdubbelt. Omgekeerd evenredig geeft een hyperbool, en daar blijft het "
                "product constant, zoals bij druk en volume in de wet van Boyle.",
                "Gram per milliliter, en dat is de eenheid van de dichtheid. Het delen van twee "
                "grootheden geeft altijd de deling van hun eenheden, en dat is een handige "
                "controle op je rekenwerk.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-wetenschappelijk-onderzoek-ontwerpen-en-stem-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="In elke proef zijn er drie soorten grootheden: wat jij verandert, wat je meet, "
                   "en wat je bewust gelijk houdt. Daarnaast heb je een proef zonder de behandeling "
                   "om mee te vergelijken.",
            waarom=[
                "Vul de vier vakjes in en kijk of je maar één ding verandert. Verander je twee "
                "dingen tegelijk, dan weet je achteraf niet welk van de twee het verschil maakte.",
                "Een goede onderzoeksvraag noemt wat je verandert én wat je meet, en een hypothese "
                "geeft een verwachting met een reden erbij. Zonder die reden is het een gok en geen "
                "hypothese.",
            ],
        ),
        dict(
            aanpak="Houd de begrippen per paar uit elkaar. Systematisch wijkt altijd dezelfde kant "
                   "uit, toevallig wisselt. Nauwkeurig gaat over de echte waarde, precies over hoe "
                   "dicht je metingen bij elkaar liggen.",
            waarom=[
                "Een systematische fout haal je er niet uit door meer te meten, een toevallige wel: "
                "die vlakt uit als je het gemiddelde neemt. Dat is precies het verschil dat ertoe "
                "doet.",
                "Je kan dus heel precies en toch niet nauwkeurig zijn, bijvoorbeeld met een "
                "weegschaal die altijd twee gram te veel aangeeft. Dat is een systematische fout.",
                "Peer review. Het houdt fouten en te sterke besluiten tegen, maar het is geen "
                "garantie: ook nagekeken artikelen worden later soms teruggetrokken.",
            ],
        ),
        dict(
            aanpak="Vier regels over eerlijk werken. Vraag je bij elk af of iemand anders jouw "
                   "resultaat zou kunnen nakijken en navolgen.",
            waarom=[
                "Niet waar, en dit is de ernstigste. Een afwijkende meting mag je enkel buiten "
                "beschouwing laten als je een reden hebt, en dan schrijf je die reden erbij.",
                "Niet waar. Dat je hypothese fout blijkt, is zelf een resultaat: je weet nu iets "
                "wat je eerst niet wist. Zo werkt wetenschap.",
                None,
                "Waar. Wat misliep hoort bij je resultaat, want het verklaart vaak een uitschieter "
                "en het helpt wie je proef wil herhalen.",
            ],
        ),
        dict(
            aanpak="Onderzoeken begint met een vraag over hoe iets is, ontwerpen met een probleem "
                   "dat opgelost moet worden. Staat er een opdracht om iets te maken, dan is het "
                   "ontwerpen.",
            waarom=[
                None,
                "Kennis tegenover een oplossing. In een STEM-opdracht zitten ze meestal "
                "allebei: je onderzoekt eerst iets en gebruikt dat om te ontwerpen.",
            ],
        ),
        dict(
            aanpak="Een criterium zegt waaraan het resultaat moet voldoen, een randvoorwaarde waar "
                   "je het mee moet doen. Tijd, geld en materiaal zijn randvoorwaarden.",
            waarom=[
                None,
                None,
                "Noem dat je het anders niet kan nagaan. Een criterium als het moet licht zijn is "
                "niet te testen; onder honderd gram wel.",
            ],
        ),
        dict(
            aanpak="Het ontwerpproces loopt in rondes: bedenken, maken, testen, bijstellen. Elk "
                   "antwoord hier zegt iets over waarom die rondes nodig zijn.",
            waarom=[
                "Noem dat je bij een mislukking weet waar het fout gaat. Dat is dezelfde reden "
                "waarom je in een proef maar één ding tegelijk verandert.",
                "Noem de hele ronde: nagaan welk criterium faalt, aanpassen, opnieuw testen. Dat "
                "een eerste prototype faalt, is normaal en geen mislukking.",
                "Noem de vier woorden en wat ze betekenen. Engineering is daarbij het ontwerpen en "
                "bouwen zelf, en dat is wat STEM van zuivere wetenschap onderscheidt.",
            ],
        ),
        dict(
            aanpak="Twee open vragen over wat er na het labo komt. De eerste gaat over natuurkunde "
                   "op grote schaal, de tweede over de afweging die maatschappij en bedrijf moeten "
                   "maken.",
            waarom=[
                "Noem beide: de warmte en de menging. Het ligt aan de verhouding oppervlak tot "
                "volume, net als bij de nanomaterialen, maar nu de andere kant uit: hoe groter, hoe "
                "minder oppervlak per liter.",
                "Noem drie vragen, niet één, en laat er een over verdeling bij zijn. Dat wie het "
                "risico draagt niet altijd wie het voordeel krijgt is, is de kern van zo'n "
                "afweging.",
            ],
        ),
    ],
)
