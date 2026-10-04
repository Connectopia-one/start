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
                 ("rij", [("CaCl₂", "2, binair"), ("NaNO₃", "3, ternair"), ("SO₃", "2, binair")],
                  "Hoeveel elementen, en wat is het?", WL),
                 ("rij", [("KHCO₃", "4, geen van de twee"), ("Li₂O", "2, binair"),
                          ("CuSO₄", "3, ternair")],
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
                 ("rij", [("HNO₃", "1"), ("H₂CO₃", "2"), ("H₃PO₄", "3")],
                  "Hoeveel?", "90px"),
                 ("rij", [("NaOH", "1"), ("Ca(OH)₂", "2"), ("Al(OH)₃", "3")],
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
                 ("kort", "Hoeveel waterstofatomen heeft een alkaan met zes koolstofatomen?", "14", W),
                 ("kort", "Hoeveel waterstofatomen heeft een alkeen met vijf koolstofatomen?", "10", W),
             ]),
        dict(kop="De IUPAC-naam",
             opdracht="Schrijf de naam volgens de regels.",
             oefeningen=[
                 ("rij", [("CH₃-CH₂-CH₂-CH₃", "butaan"), ("CH₃-CH₂-OH", "ethanol"),
                          ("CH₃-COOH", "ethaanzuur")],
                  "Welke naam?", WW),
                 ("rij", [("CH₃-CO-CH₂-CH₃", "butanon"), ("CH₃-CHOH-CH₃", "propaan-2-ol"),
                          ("CH₂=CH-CH₃", "propeen")],
                  "Welke naam?", WW),
                 ("open", "Leg uit waarom propaan-1-ol en niet propaan-3-ol de juiste naam is.",
                  "Je nummert de hoofdketen van de kant die de functionele groep het laagste nummer "
                  "geeft. Van de andere kant geteld zou de OH-groep aan koolstof 3 hangen, en 1 is "
                  "kleiner dan 3.", 5),
             ]),
        dict(kop="Primair, secundair of tertiair",
             opdracht="Schrijf primair, secundair of tertiair.",
             oefeningen=[
                 ("rij", [("butaan-1-ol", "primair"), ("butaan-2-ol", "secundair"),
                          ("2-methylpropaan-2-ol", "tertiair")],
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
                 ("rij", [("pentaan en 2-methylbutaan", "ketenisomerie"),
                          ("butaan-1-ol en butaan-2-ol", "plaatsisomerie")],
                  "Welk soort?", WL),
                 ("rij", [("propanal en propanon", "functie-isomerie"),
                          ("pent-1-een en pent-2-een", "plaatsisomerie")],
                  "Welk soort?", WL),
                 ("rij", [("ethaanzuur en methylmethanoaat", "functie-isomerie"),
                          ("hexaan en 2,3-dimethylbutaan", "ketenisomerie")],
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
                 ("rij", [("structuurisomeren van C₄H₁₀", "2"),
                          ("structuurisomeren van C₅H₁₂", "3"),
                          ("structuurisomeren van C₃H₈", "1")],
                  "Hoeveel?", "90px"),
                 ("rij", [("stereo-isomeren bij 1 asymmetrisch koolstofatoom", "2"),
                          ("bij 2 asymmetrische koolstofatomen", "4"),
                          ("bij 4 asymmetrische koolstofatomen", "16")],
                  "Hoeveel?", "90px"),
                 ("open", "Leg uit waarom er van methaan geen enkel isomeer bestaat.",
                  "Er is maar één manier om één koolstofatoom en vier waterstofatomen aan elkaar te "
                  "zetten. Pas vanaf vier koolstofatomen kan een keten vertakken.", 4),
             ]),
        dict(kop="Z of E",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("but-2-een", "wel Z/E"), ("but-1-een", "geen Z/E"),
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
                 ("rij", [("2-chloorbutaan", "chiraal"), ("propaan-2-ol", "niet chiraal"),
                          ("2-broompropaan", "niet chiraal")],
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
                 ("rij", [("één orbitaal", "2"), ("een s-subniveau", "2"),
                          ("een p-subniveau", "6")],
                  "Hoeveel elektronen?", "90px"),
                 ("rij", [("een d-subniveau", "10"), ("een f-subniveau", "14"),
                          ("een p-subniveau in orbitalen", "3 orbitalen")],
                  "Hoeveel?", "110px"),
             ]),
        dict(kop="De configuratie schrijven",
             opdracht="Schrijf de volledige elektronenconfiguratie.",
             oefeningen=[
                 ("rij", [("stikstof, 7 elektronen", "1s² 2s² 2p³"),
                          ("natrium, 11 elektronen", "1s² 2s² 2p⁶ 3s¹")],
                  "Welke configuratie?", WL),
                 ("rij", [("fluor, 9 elektronen", "1s² 2s² 2p⁵"),
                          ("magnesium, 12 elektronen", "1s² 2s² 2p⁶ 3s²")],
                  "Welke configuratie?", WL),
                 ("kort", "Hoeveel valentie-elektronen heeft een atoom met [Ne] 3s² 3p⁴?", "6", W),
                 ("kort", "Hoeveel elektronen heeft het ion Mg²⁺?", "10", W),
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
                 ("rij", [("[Ne] 3s¹", "groep 1, periode 3"),
                          ("[Ar] 4s² 3d¹⁰ 4p³", "groep 15, periode 4")],
                  "Groep en periode?", WL),
                 ("rij", [("1s² 2s² 2p⁵", "groep 17, periode 2"),
                          ("[Kr] 5s²", "groep 2, periode 5")],
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
                 ("rij", [("H₂O", "2 sigma, 0 pi"), ("CH₄", "4 sigma, 0 pi")],
                  "Hoeveel van elk?", WL),
                 ("rij", [("CH₂=CH₂", "5 sigma, 1 pi"), ("HC≡CH", "3 sigma, 2 pi")],
                  "Hoeveel van elk?", WL),
                 ("rij", [("CO₂", "2 sigma, 2 pi"), ("N₂", "1 sigma, 2 pi")],
                  "Hoeveel van elk?", WL),
             ]),
        dict(kop="Korter of langer",
             opdracht="Zet de drie bindingen in de juiste volgorde, van lang naar kort.",
             oefeningen=[
                 ("open", "C–C, C=C en C≡C: zet ze van lang naar kort en zeg waarom.",
                  "C–C (ongeveer 154 pm), dan C=C (134 pm), dan C≡C (120 pm). Elke extra binding "
                  "trekt de twee atomen dichter naar elkaar, dus wordt de binding korter en sterker.", 5),
                 ("waar", "Tussen twee atomen kunnen meerdere sigma-bindingen naast elkaar liggen.", False),
                 ("waar", "Een pi-binding is zwakker dan een sigma-binding tussen dezelfde atomen.", True),
                 ("waar", "Rond een dubbele binding kan een molecule vrij draaien.", False),
             ]),
        dict(kop="Vrije elektronenparen tellen",
             opdracht="Schrijf hoeveel vrije elektronenparen het vetgedrukte atoom heeft.",
             oefeningen=[
                 ("rij", [("<b>O</b> in H₂O", "2"), ("<b>N</b> in NH₃", "1"),
                          ("<b>Cl</b> in Cl₂", "3")],
                  "Hoeveel vrije paren?", "90px"),
                 ("rij", [("<b>N</b> in NH₄⁺", "0"), ("<b>O</b> in H₃O⁺", "1"),
                          ("<b>C</b> in CH₄", "0")],
                  "Hoeveel vrije paren?", "90px"),
             ]),
        dict(kop="Formele lading",
             opdracht="Reken met valentie-elektronen min vrije elektronen min aantal bindingen.",
             oefeningen=[
                 ("rij", [("N in NH₄⁺", "+1"), ("O in H₃O⁺", "+1"), ("O in OH⁻", "−1")],
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
                 ("rij", [("C in CH₄", "4"), ("O in H₂O", "4"), ("N in NH₃", "4")],
                  "Sterisch getal?", "90px"),
                 ("rij", [("C in CO₂", "2"), ("S in SO₂", "3"), ("C in CH₂=CH₂", "3")],
                  "Sterisch getal?", "90px"),
             ]),
        dict(kop="Vorm en hybridisatie",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["sterisch getal", "vorm zonder vrije paren", "hybridisatie", "hoek"],
                  [["2", None, "sp", None],
                   ["3", "vlakke driehoek", None, "120°"],
                   ["4", None, "sp³", None]],
                  "2: lineair, 180° · 3: sp² · 4: tetraëder, 109,5°", W),
                 ("rij", [("CH₄", "tetraëder"), ("NH₃", "piramide"), ("H₂O", "geknikt")],
                  "Welke vorm?", WW),
                 ("rij", [("CO₂", "lineair"), ("SO₂", "vlak geknikt"), ("NH₄⁺", "tetraëder")],
                  "Welke vorm?", WW),
             ]),
        dict(kop="De bindingshoek",
             opdracht="Schrijf de werkelijke hoek en leg uit waarom ze afwijkt.",
             oefeningen=[
                 ("rij", [("CH₄", "109,5°"), ("NH₃", "107°"), ("H₂O", "104,5°")],
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
                 ("rij", [("pentaan of butaan", "pentaan"), ("butaan of 2-methylpropaan", "butaan"),
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
             opdracht="Reken met H 1, C 12, N 14, O 16, Na 23, S 32 en Cl 35,5 g/mol.",
             oefeningen=[
                 ("rij", [("NH₃", "17 g/mol"), ("NaOH", "40 g/mol"), ("CO₂", "44 g/mol")],
                  "Welke molaire massa?", WW),
                 ("rij", [("H₂SO₄", "98 g/mol"), ("NaCl", "58,5 g/mol"),
                          ("C₆H₁₂O₆", "180 g/mol")],
                  "Welke molaire massa?", WW),
             ]),
        dict(kop="Van gram naar mol",
             opdracht="Reken uit. Schrijf eerst de formule op.",
             oefeningen=[
                 ("kort", "Hoeveel mol is 34 g NH₃ (M = 17 g/mol)?", "2 mol", W),
                 ("kort", "Hoeveel mol is 9 g water (M = 18 g/mol)?", "0,5 mol", W),
                 ("kort", "Hoeveel gram weegt 0,25 mol NaOH (M = 40 g/mol)?", "10 g", W),
                 ("kort", "Hoeveel gram weegt 3 mol CO₂ (M = 44 g/mol)?", "132 g", W),
             ]),
        dict(kop="Deeltjes tellen",
             opdracht="Reken met 6,022 × 10²³ deeltjes per mol.",
             oefeningen=[
                 ("kort", "Hoeveel moleculen zitten er in 0,5 mol?", "3,011 × 10²³", WW),
                 ("kort", "Hoeveel mol zuurstofatomen zitten er in 2 mol H₂SO₄?", "8 mol", W),
                 ("open", "Achttien gram water en achttien gram glucose. In welk bekertje zitten de meeste moleculen, en waarom?",
                  "In het water. Water heeft M = 18 g/mol, dus is dat één mol; glucose heeft "
                  "M = 180 g/mol, dus maar een tiende van een mol. Dezelfde massa betekent dus niet "
                  "hetzelfde aantal deeltjes.", 6),
             ]),
        dict(kop="Gassen bij normomstandigheden",
             opdracht="Reken met een molair volume van 22,4 L/mol.",
             oefeningen=[
                 ("rij", [("2 mol gas", "44,8 L"), ("0,5 mol gas", "11,2 L"),
                          ("0,25 mol gas", "5,6 L")],
                  "Welk volume?", WW),
                 ("waar", "Eén mol gas neemt bij elke temperatuur 22,4 liter in.", False),
                 ("waar", "Eén mol zuurstofgas en één mol waterstofgas nemen bij 0 °C hetzelfde volume in.", True),
             ]),
        dict(kop="Concentratie",
             opdracht="Reken uit. Zet het volume altijd eerst in liter.",
             oefeningen=[
                 ("kort", "0,4 mol in 2 L. Welke concentratie?", "0,2 mol/L", WW),
                 ("kort", "Hoeveel mol zit er in 250 mL van 0,8 mol/L?", "0,2 mol", W),
                 ("kort", "Hoeveel mol weeg je af voor 500 mL van 0,1 mol/L?", "0,05 mol", W),
                 ("kort", "Hoeveel gram zout zit er in 300 g oplossing van 5 massaprocent?", "15 g", W),
             ]),
        dict(kop="Verdunnen",
             opdracht="Gebruik c₁ · V₁ = c₂ · V₂.",
             oefeningen=[
                 ("kort", "20 mL van 1 mol/L verdund tot 100 mL. Welke concentratie?", "0,2 mol/L", WW),
                 ("kort", "Hoeveel mL van 2 mol/L heb je nodig voor 500 mL van 0,1 mol/L?", "25 mL", W),
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
                 ("kort", "Hoeveel milligram per liter water is 1 ppm?", "1 mg", W),
                 ("open", "Een verbinding bestaat uit 52,2 % koolstof, 13,0 % waterstof en 34,8 % zuurstof. Zoek de eenvoudigste formule (C 12, H 1, O 16).",
                  "Deel elk percentage door de atoommassa: 52,2/12 = 4,35; 13,0/1 = 13,0; "
                  "34,8/16 = 2,18. Deel door de kleinste: 2 : 6 : 1, dus C₂H₆O.", 6),
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
                 ("rij", [("… H₂ + … O₂ → … H₂O", "2, 1, 2"),
                          ("… Na + … Cl₂ → … NaCl", "2, 1, 2")],
                  "Welke coëfficiënten?", WL),
                 ("rij", [("… C₂H₆ + … O₂ → … CO₂ + … H₂O", "2, 7, 4, 6"),
                          ("… Fe + … O₂ → … Fe₂O₃", "4, 3, 2")],
                  "Welke coëfficiënten?", WL),
                 ("rij", [("… CH₄ + … O₂ → … CO₂ + … H₂O", "1, 2, 1, 2"),
                          ("… Al + … HCl → … AlCl₃ + … H₂", "2, 6, 2, 3")],
                  "Welke coëfficiënten?", WL),
                 ("waar", "Je mag de formule van een stof aanpassen om een vergelijking te laten kloppen.", False),
             ]),
        dict(kop="Rekenen met de verhouding",
             opdracht="Gebruik N₂ + 3 H₂ → 2 NH₃.",
             oefeningen=[
                 ("kort", "Hoeveel mol NH₃ uit 3 mol N₂?", "6 mol", W),
                 ("kort", "Hoeveel mol H₂ voor 4 mol NH₃?", "6 mol", W),
                 ("kort", "Hoeveel mol N₂ voor 9 mol H₂?", "3 mol", W),
             ]),
        dict(kop="Van gram naar gram",
             opdracht="Schrijf alle stappen op: gram, mol, verhouding, mol, gram.",
             oefeningen=[
                 ("open", "Hoeveel gram MgO ontstaat er uit 4,8 g Mg? (2 Mg + O₂ → 2 MgO; "
                  "Mg 24 g/mol, MgO 40 g/mol)",
                  "4,8 g : 24 g/mol = 0,2 mol Mg. De verhouding Mg op MgO is 1 op 1, dus 0,2 mol "
                  "MgO. 0,2 mol × 40 g/mol = 8 g MgO.", 6),
                 ("open", "Hoeveel gram CO₂ komt er vrij uit 50 g CaCO₃? (CaCO₃ → CaO + CO₂; "
                  "CaCO₃ 100 g/mol, CO₂ 44 g/mol)",
                  "50 g : 100 g/mol = 0,5 mol CaCO₃. De verhouding is 1 op 1, dus 0,5 mol CO₂. "
                  "0,5 mol × 44 g/mol = 22 g CO₂.", 6),
                 ("open", "Leg uit waarom je de verhouding uit de vergelijking niet rechtstreeks op massa's mag toepassen.",
                  "De coëfficiënten geven een verhouding in mol. Twee stoffen met dezelfde "
                  "stofhoeveelheid hebben meestal een heel andere massa, want hun molaire massa "
                  "verschilt. Daarom reken je eerst om naar mol.", 5),
             ]),
        dict(kop="Limiterend reagens",
             opdracht="Deel van elke stof het aantal mol door haar coëfficiënt.",
             oefeningen=[
                 ("rij", [("3 mol H₂ en 3 mol O₂ in 2 H₂ + O₂ → 2 H₂O", "H₂ is beperkend"),
                          ("2 mol N₂ en 3 mol H₂ in N₂ + 3 H₂ → 2 NH₃", "H₂ is beperkend")],
                  "Welke stof is beperkend?", WL),
                 ("kort", "Hoeveel mol water uit 3 mol H₂ en 3 mol O₂?", "3 mol", W),
                 ("waar", "Het limiterend reagens is altijd de stof waarvan je het minste mol hebt.", False),
                 ("open", "Waarom werkt men in de industrie soms met een overmaat van de goedkoopste stof?",
                  "Dan is de dure stof het beperkend reagens en reageert ze zo volledig mogelijk weg. "
                  "Het overschot van de goedkope stof blijft over en wordt vaak hergebruikt.", 5),
             ]),
        dict(kop="De algemene gaswet",
             opdracht="Reken met pV = nRT en een molair volume van 22,4 L/mol bij 0 °C.",
             oefeningen=[
                 ("rij", [("0 °C", "273 K"), ("27 °C", "300 K"), ("100 °C", "373 K")],
                  "Hoeveel kelvin?", W),
                 ("kort", "Hoeveel mol gas zit er in 5,6 L bij normomstandigheden?", "0,25 mol", W),
                 ("kort", "Welk volume neemt 1,5 mol gas in bij normomstandigheden?", "33,6 L", W),
                 ("waar", "Bij hogere druk neemt een gas bij gelijke temperatuur meer plaats in.", False),
                 ("open", "Een gas van 2 liter bij 300 K wordt opgewarmd tot 600 K bij gelijke druk. Welk volume krijg je, en waarom?",
                  "4 liter. In pV = nRT staan V en T aan weerszijden van het gelijkheidsteken, dus "
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
                 ("rij", [("v = k·[A]·[B]", "totale orde 2"), ("v = k·[A]²·[B]", "totale orde 3"),
                          ("v = k·[A]", "totale orde 1")],
                  "Welke totale orde?", WL),
                 ("rij", [("[A] verdubbelt, v verdubbelt", "eerste orde"),
                          ("[A] verdubbelt, v wordt 4 keer groter", "tweede orde"),
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
                 ("rij", [("H₂ + I₂ ⇌ 2 HI", "[HI]² / ([H₂]·[I₂])"),
                          ("N₂ + 3 H₂ ⇌ 2 NH₃", "[NH₃]² / ([N₂]·[H₂]³)")],
                  "Welke uitdrukking?", WL),
                 ("rij", [("2 SO₂ + O₂ ⇌ 2 SO₃", "[SO₃]² / ([SO₂]²·[O₂])"),
                          ("A + 2 B ⇌ 3 C", "[C]³ / ([A]·[B]²)")],
                  "Welke uitdrukking?", WL),
             ]),
        dict(kop="Wat zegt de waarde van K?",
             opdracht="Schrijf links, rechts of in het midden.",
             oefeningen=[
                 ("rij", [("K = 1000", "rechts"), ("K = 1", "in het midden"),
                          ("K = 0,001", "links")],
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
                 ("rij", [("het volume verkleinen bij N₂ + 3 H₂ ⇌ 2 NH₃", "naar rechts"),
                          ("de druk verlagen bij diezelfde reactie", "naar links"),
                          ("de druk verhogen bij H₂ + I₂ ⇌ 2 HI", "geen verschuiving")],
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
                 ("kort", "Je haalt 7,5 g uit een reactie waar 10 g mogelijk was. Welk rendement?", "75 %", W),
                 ("kort", "Van 2 mol beginstof reageert 0,5 mol. Welke omzettingsgraad?", "25 %", W),
                 ("open", "Waarom haalt men in de industrie het product voortdurend uit een evenwichtsmengsel?",
                  "Door het product weg te nemen blijft Q kleiner dan K, dus blijft de heenreactie "
                  "doorlopen. Zo reageert er meer van de beginstoffen weg dan wanneer het evenwicht "
                  "gewoon mag stilvallen.", 6),
                 ("open", "Waarom blijft de omzettingsgraad bij een evenwicht altijd onder 100 procent?",
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
                 ("rij", [("HNO₃", "1"), ("H₂SO₄", "2"), ("H₃PO₄", "3")],
                  "Hoeveel?", "90px"),
                 ("rij", [("OH⁻", "1"), ("CO₃²⁻", "2"), ("PO₄³⁻", "3")],
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
                 ("open", "Twee bekers van 0,1 mol/L: één zoutzuur, één azijnzuur. Wat is gelijk en wat verschilt?",
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
             opdracht="Vul de tabel aan. Reken bij 25 °C.",
             oefeningen=[
                 ("tabel", ["pH", "pOH", "zuur, basisch of neutraal"],
                  [["3", None, None],
                   [None, "1", None],
                   ["7", None, None],
                   [None, "9", None],
                   ["12", None, None]],
                  "pH 3: pOH 11, zuur · pOH 1: pH 13, basisch · pH 7: pOH 7, neutraal · "
                  "pOH 9: pH 5, zuur · pH 12: pOH 2, basisch", W),
             ]),
        dict(kop="Van concentratie naar pH",
             opdracht="Reken uit. Alle zuren en basen hier zijn sterk.",
             oefeningen=[
                 ("rij", [("0,1 mol/L HCl", "pH 1"), ("0,001 mol/L HCl", "pH 3"),
                          ("10⁻⁵ mol/L HCl", "pH 5")],
                  "Welke pH?", WW),
                 ("rij", [("0,01 mol/L NaOH", "pH 12"), ("0,1 mol/L NaOH", "pH 13"),
                          ("10⁻⁴ mol/L NaOH", "pH 10")],
                  "Welke pH?", WW),
                 ("kort", "Welke pH heeft 0,05 mol/L H₂SO₄ (tweewaardig)?", "pH 1", W),
             ]),
        dict(kop="Van pH naar concentratie",
             opdracht="Schrijf de concentratie hydroxonium- of hydroxide-ionen.",
             oefeningen=[
                 ("rij", [("pH 4", "[H₃O⁺] = 10⁻⁴ mol/L"), ("pH 9", "[OH⁻] = 10⁻⁵ mol/L")],
                  "Welke concentratie?", WL),
                 ("rij", [("pH 2", "[H₃O⁺] = 10⁻² mol/L"), ("pOH 3", "[OH⁻] = 10⁻³ mol/L")],
                  "Welke concentratie?", WL),
             ]),
        dict(kop="Hoeveel keer?",
             opdracht="Reken met de logaritmische schaal.",
             oefeningen=[
                 ("rij", [("pH 2 tegenover pH 5", "1000 keer"), ("pH 3 tegenover pH 4", "10 keer"),
                          ("pH 1 tegenover pH 5", "10 000 keer")],
                  "Hoeveel keer meer H₃O⁺?", WL),
                 ("open", "Waarom gebruikt men een logaritmische schaal voor de zuurtegraad?",
                  "De concentratie hydroxoniumionen loopt van ongeveer 1 mol/L tot 10⁻¹⁴ mol/L, dus "
                  "over veertien machten van tien. Met gewone getallen zou dat onhandelbaar zijn; de "
                  "logaritme maakt er een handig getal van tussen 0 en 14.", 6),
             ]),
        dict(kop="Verdunnen en inkoken",
             opdracht="Schrijf wat er met de pH gebeurt.",
             oefeningen=[
                 ("rij", [("een sterk zuur 10 keer verdunnen", "pH stijgt 1 eenheid"),
                          ("een sterk zuur 100 keer verdunnen", "pH stijgt 2 eenheden")],
                  "Wat gebeurt er?", WL),
                 ("waar", "Door een sterk zuur heel sterk te verdunnen kan de pH boven 7 komen.", False),
                 ("waar", "Inkoken tot de helft van het volume doet de pH van een sterk zuur dalen.", True),
                 ("open", "Leg uit waarom de pH van een zwak zuur niet rechtstreeks uit zijn concentratie volgt.",
                  "Bij een zwak zuur staat maar een deel van de moleculen zijn proton af. Hoeveel "
                  "precies, hangt af van de zuurconstante, dus heb je naast de concentratie ook Kz "
                  "nodig.", 5),
             ]),
        dict(kop="Mengen",
             opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Je mengt gelijke volumes 0,1 mol/L HCl en 0,1 mol/L NaOH. Welke pH verwacht je, en waarom?",
                  "pH 7. Het aantal mol hydroxonium en hydroxide is precies gelijk, dus reageren ze "
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
             opdracht="Welk zuur neem je voor die buffer? Kies uit melkzuur (pKz 3,9), azijnzuur (pKz 4,8), diwaterstoffosfaat (pKz 7,2) en ammonium (pKz 9,2).",
             oefeningen=[
                 ("rij", [("een buffer rond pH 7", "diwaterstoffosfaat"),
                          ("een buffer rond pH 9", "ammonium"),
                          ("een buffer rond pH 4", "melkzuur")],
                  "Welk zuur?", WL),
                 ("kort", "Binnen welk gebied werkt een buffer met azijnzuur ongeveer?", "tussen pH 3,8 en pH 5,8", WL),
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
                 ("open", "Twee buffers hebben dezelfde pH, maar de ene is 1 mol/L en de andere 0,01 mol/L. Wat verschilt er?",
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
                          ("waarmee je precies 25 mL afmeet", "de pipet")],
                  "Wat?", WL),
                 ("rij", [("waarmee je de buret spoelt", "met titrans"),
                          ("waar je op de meniscus afleest", "aan de onderkant")],
                  "Hoe?", WL),
             ]),
        dict(kop="Titratie rekenen",
             opdracht="Reken uit. Schrijf eerst het aantal mol titrans.",
             oefeningen=[
                 ("kort", "25,0 mL eenwaardig zuur verbruikt 25,0 mL NaOH van 0,100 mol/L. Concentratie van het zuur?", "0,100 mol/L", WW),
                 ("kort", "25,0 mL eenwaardig zuur verbruikt 12,5 mL NaOH van 0,100 mol/L. Concentratie van het zuur?", "0,0500 mol/L", WW),
                 ("kort", "20,0 mL H₂SO₄ verbruikt 30,0 mL NaOH van 0,100 mol/L. Concentratie van het zuur?", "0,0750 mol/L", WW),
                 ("kort", "10,0 mL NaOH verbruikt 15,0 mL HCl van 0,200 mol/L. Concentratie van de base?", "0,300 mol/L", WW),
             ]),
        dict(kop="De curve lezen",
             opdracht="Antwoord kort of in volle zinnen.",
             oefeningen=[
                 ("rij", [("sterk zuur met sterke base", "pH 7"),
                          ("zwak zuur met sterke base", "boven pH 7"),
                          ("zwakke base met sterk zuur", "onder pH 7")],
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
                 ("rij", [("S₈", "0"), ("H₂S", "−II"), ("SO₂", "+IV")],
                  "Welk getal?", W),
                 ("rij", [("SO₃²⁻", "+IV"), ("SO₄²⁻", "+VI"), ("Na₂S", "−II")],
                  "Welk getal?", W),
             ]),
        dict(kop="Oxidatiegetallen van stikstof",
             opdracht="Bepaal het oxidatiegetal van stikstof.",
             oefeningen=[
                 ("rij", [("N₂", "0"), ("NH₃", "−III"), ("NO", "+II")],
                  "Welk getal?", W),
                 ("rij", [("NO₂", "+IV"), ("NO₂⁻", "+III"), ("NH₄⁺", "−III")],
                  "Welk getal?", W),
             ]),
        dict(kop="Oxidatiegetallen van chloor en koolstof",
             opdracht="Bepaal het oxidatiegetal van het onderlijnde element.",
             oefeningen=[
                 ("rij", [("chloor in Cl₂", "0"), ("chloor in NaCl", "−I"),
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
                 ("rij", [("Mg wordt Mg²⁺", "oxidatie, 2 elektronen af"),
                          ("Cl₂ wordt 2 Cl⁻", "reductie, 2 elektronen op")],
                  "Wat gebeurt er?", WL),
                 ("rij", [("Sn²⁺ wordt Sn⁴⁺", "oxidatie, 2 elektronen af"),
                          ("MnO₄⁻ wordt Mn²⁺", "reductie, 5 elektronen op")],
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
             opdracht="Gebruik deze waarden: Ag⁺/Ag +0,80 V · Cu²⁺/Cu +0,34 V · Pb²⁺/Pb −0,13 V · Zn²⁺/Zn −0,76 V · Mg²⁺/Mg −2,37 V.",
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
             opdracht="Gebruik: Ag⁺/Ag +0,80 V · Cu²⁺/Cu +0,34 V · Fe²⁺/Fe −0,44 V · Zn²⁺/Zn −0,76 V · Al³⁺/Al −1,66 V.",
             oefeningen=[
                 ("rij", [("zilver en koper", "0,46 V"), ("koper en ijzer", "0,78 V")],
                  "Welke bronspanning?", WW),
                 ("rij", [("zink en zilver", "1,56 V"), ("aluminium en koper", "2,00 V")],
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
                          ("but-1-een met broom", "1,2-dibroombutaan"),
                          ("etheen met water en een zuur", "ethanol")],
                  "Welk product?", WL),
                 ("rij", [("ethyn met twee keer diwaterstof", "ethaan"),
                          ("propeen met broomwater", "1,2-dibroompropaan")],
                  "Welk product?", WL),
             ]),
        dict(kop="De regel van Markownikov",
             opdracht="Welk product overheerst?",
             oefeningen=[
                 ("rij", [("propeen met HCl", "2-chloorpropaan"),
                          ("propeen met water", "propaan-2-ol"),
                          ("but-1-een met HBr", "2-broombutaan")],
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
                 ("rij", [("propaan", "0"), ("propeen", "1"), ("propyn", "2")],
                  "Hoeveel keer?", "90px"),
                 ("kort", "Waarom ontkleurt broomwater bij een alkeen en niet bij een alkaan?", "het broom addeert aan de dubbele binding", WL),
             ]),
        dict(kop="Eliminatie",
             opdracht="Schrijf het product.",
             oefeningen=[
                 ("rij", [("ethanol met geconcentreerd zwavelzuur en warmte", "etheen en water"),
                          ("broomethaan met een base", "etheen en HBr")],
                  "Welk product?", WL),
                 ("rij", [("propaan-1-ol, dehydrogenatie", "propanal"),
                          ("propaan-2-ol, dehydrogenatie", "propanon"),
                          ("butaan-2-ol, dehydrogenatie", "butanon")],
                  "Welk product?", WL),
                 ("kort", "Waarom geeft de dehydratatie van butaan-2-ol twee alkenen?", "het water kan aan twee kanten weggaan", WL),
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
                  "primair: 1, aldehyde (en verder carbonzuur) · secundair: 2, keton · "
                  "tertiair: 3, geen dehydrogenatie mogelijk", WW),
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
                 ("kort", "Tussen welke twee grenzen in nanometer ligt een nanomateriaal?", "tussen 1 en 100 nm", WL),
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
                  [["1 (beste)", None], ["2", None], ["3", None], ["4", None], ["5 (slechtste)", None]],
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
                 ("kort", "Welke atoomeconomie heeft een additie zonder bijproduct?", "100 %", W),
                 ("open", "Leg uit waarom een hoog rendement en een hoge atoomeconomie niet hetzelfde zijn.",
                  "Het rendement zegt hoeveel je van het mogelijke product echt uit de reactie "
                  "haalt. De atoomeconomie zegt welk deel van de massa van de reagentia volgens de "
                  "reactievergelijking überhaupt in het product belandt. Een condensatie kan dus "
                  "een rendement van 95 procent hebben en toch een matige atoomeconomie, want er "
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
                 ("rij", [("precies 500,0 mL oplossing aanmaken", "een maatkolf van 500 mL"),
                          ("precies 25 mL overbrengen", "een volumetrische pipet"),
                          ("een volume aflezen tot op honderdsten bij een titratie", "een buret")],
                  "Welk glaswerk?", WL),
                 ("rij", [("ongeveer 100 mL water bijgieten", "een maatcilinder of bekerglas"),
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
                 ("open", "Waarom meet je 5 mL niet af in een maatcilinder van 500 mL?",
                  "De streepjes van zo'n grote cilinder staan veel te ver uit elkaar voor zo'n klein "
                  "volume, dus is de resolutie veel te grof. De onzekerheid op je 5 mL zou dan "
                  "groter zijn dan wat je wil meten.", 6),
             ]),
        dict(kop="Voorvoegsels",
             opdracht="Reken om.",
             oefeningen=[
                 ("rij", [("1 mm in micrometer", "1000 µm"), ("1 kg in gram", "1000 g"),
                          ("1 MJ in joule", "1 000 000 J")],
                  "Hoeveel?", WW),
                 ("rij", [("2,5 nm in meter", "2,5·10⁻⁹ m"), ("0,5 mL in liter", "5·10⁻⁴ L"),
                          ("300 mg in gram", "0,300 g")],
                  "Hoeveel?", WW),
                 ("kort", "Wat is de SI-basiseenheid van stofhoeveelheid?", "de mol", WW),
                 ("kort", "En van temperatuur?", "de kelvin", WW),
             ]),
        dict(kop="Beduidende cijfers",
             opdracht="Hoeveel beduidende cijfers?",
             oefeningen=[
                 ("rij", [("0,00310", "3"), ("45,0", "3"), ("1200", "2 (zonder komma)")],
                  "Hoeveel?", WW),
                 ("rij", [("2,5·10⁴", "2"), ("0,0008", "1"), ("10,04", "4")],
                  "Hoeveel?", WW),
             ]),
        dict(kop="Rekenen met meetwaarden",
             opdracht="Schrijf het resultaat met het juiste aantal cijfers.",
             oefeningen=[
                 ("rij", [("3,2 × 1,478", "4,7"), ("25,0 ÷ 4,0", "6,3")],
                  "Welk resultaat?", WW),
                 ("rij", [("14,25 g + 0,3 g", "14,6 g"), ("8,0 cm + 0,125 cm", "8,1 cm")],
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
                 ("rij", [("0,000 058", "5,8·10⁻⁵"), ("342 000", "3,42·10⁵")],
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
                  "stukje kalk van 1 gram volledig oplost? Hypothese: bij een hogere concentratie "
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
                 ("rij", [("hoe snel lost dit zout op bij 40 °C", "onderzoeken"),
                          ("maak een houder die een ei een val van twee meter laat overleven", "ontwerpen"),
                          ("welke isolatie houdt het water het langst warm", "onderzoeken")],
                  "Wat is het?", WW),
                 ("kort", "Wat zoekt onderzoeken, en wat zoekt ontwerpen?", "kennis tegenover een oplossing", WL),
             ]),
        dict(kop="Criterium of randvoorwaarde",
             opdracht="Schrijf criterium of randvoorwaarde.",
             oefeningen=[
                 ("rij", [("de houder weegt minder dan 100 gram", "criterium"),
                          ("je hebt maar één lesuur", "randvoorwaarde"),
                          ("het water blijft minstens 20 minuten boven 50 °C", "criterium")],
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
