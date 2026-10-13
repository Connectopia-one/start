# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij natuurwetenschappen 🌍 Beyond.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere reeksen om te benoemen, andere gevallen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een stap
uitleggen, een rekening uitschrijven). Wie hier iets bijschrijft, legt het eerst
naast `../../beyond/natuurwetenschappen.json` en naast de vakfiche zelf.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Natuurwetenschappen"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"

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
OEFENBUNDELS["oefenbundel-de-cel-organellen-membranen-en-weefsels-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De cel: organellen, membranen en weefsels",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk organel doet dit?",
             opdracht="Schrijf bij elke taak de naam van het organel.",
             oefeningen=[
                 ("rij", [("zet aminozuren aan elkaar", "ribosoom"),
                          ("verteert versleten organellen", "lysosoom"),
                          ("legt de trekdraden aan", "centrosoom")], "Welk organel?", WW),
                 ("rij", [("maakt de ribosomen", "kernlichaampje"),
                          ("ontgift stoffen en maakt vetten", "glad ER"),
                          ("slaat vocht en stoffen op", "vacuole")], "Welk organel?", WW),
             ]),
        dict(kop="Plant, dier of beide?",
             opdracht="Schrijf plant, dier of beide.",
             oefeningen=[
                 ("rij", [("chloroplast", "plant"), ("mitochondrion", "beide"),
                          ("celwand van cellulose", "plant")], None, W),
                 ("rij", [("centrosoom", "dier"), ("celmembraan", "beide"),
                          ("amyloplast", "plant")], None, W),
             ]),
        dict(kop="Bouw en functie",
             opdracht="Leg in volledige zinnen uit hoe de bouw bij de functie past.",
             oefeningen=[
                 ("open", "Een rijpe rode bloedcel van de mens heeft geen kern meer. Wat levert dat "
                          "haar op?",
                  "Zonder kern is er meer plaats binnen de cel voor hemoglobine, en dus kan ze meer "
                  "zuurstof vervoeren.", 3),
                 ("open", "Een wortelhaar is een lange, dunne uitloper van een huidcel. Welk voordeel "
                          "geeft die vorm aan de wortel?",
                  "Ze vergroot het oppervlak waarmee de wortel water en mineralen opneemt.", 3),
                 ("open", "De cellen van het palissadeparenchym staan rechtop en dicht tegen elkaar, "
                          "net onder de bovenkant van het blad. Waarom precies daar?",
                  "Daar valt het meeste licht binnen, en die cellen zitten vol chloroplasten voor de "
                  "fotosynthese.", 3),
             ]),
        dict(kop="Het celmembraan",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Bestanddeel", "Wat het in het membraan doet"],
                  [["fosfolipiden", None], ["cholesterol", None], ["transmembraaneiwitten", None]],
                  "Fosfolipiden vormen de dubbellaag, de grondlaag van elk membraan. Cholesterol houdt "
                  "het membraan soepel maar stevig. Transmembraaneiwitten dienen als poort of pomp voor "
                  "stoffen die er niet zelf door kunnen.", WL),
                 ("waar", "Een semi-permeabel membraan laat alle stoffen even vlot door.", False),
                 ("open", "Je legt een plantencel in zuiver water. Beschrijf wat er gebeurt en waarom "
                          "ze niet openbarst.",
                  "Water stroomt naar binnen, want daar is de concentratie aan opgeloste stoffen hoger. "
                  "De cel wordt stevig of turgescent. De celwand houdt haar tegen, zodat ze niet "
                  "openbarst zoals een dierlijke cel zou doen.", 4),
             ]),
        dict(kop="Waarom blijven cellen klein?",
             opdracht="Reken en besluit.",
             oefeningen=[
                 ("kort", r"Een kubusvormige cel heeft een zijde van \(2\) mm. Hoe groot is haar volume?",
                  r"\(8\,\text{mm}^{3}\)", "90px"),
                 ("kort", r"Hoe groot is de totale oppervlakte van die kubus (\(6\) vlakken)?",
                  r"\(24\,\text{mm}^{2}\)", "90px"),
                 ("open", r"Verdubbel je de zijde tot \(4\) mm, dan wordt het volume \(64\,\text{mm}^{3}\) en de "
                          r"oppervlakte \(96\,\text{mm}^{2}\). Wat gebeurt er met de verhouding oppervlakte op volume, "
                          "en waarom zet dat een grens op de grootte van een cel?",
                  r"Ze zakt van \(3\) naar \(1{,}5\). Een grote cel heeft dus per eenheid volume te weinig "
                  "membraan om stoffen uit te wisselen. Daarom blijven cellen klein en worden "
                  "organismen groot door méér cellen te maken.", 4),
             ]),
        dict(kop="Weefsels benoemen",
             opdracht="Schrijf de naam van het weefsel.",
             oefeningen=[
                 ("rij", [("vervoert water naar het blad", "xyleem"),
                          ("vervoert opgeloste suikers", "floëem"),
                          ("bedekt en beschermt bij dieren", "epitheelweefsel")], None, WW),
                 ("kies", "Welk weefsel vervoert bij dieren stoffen door het lichaam?",
                  ["epitheelweefsel", "spierweefsel", "transportweefsel", "zenuwweefsel"], 2),
                 ("kort", "Hoe heten de twee cellen die samen een huidmondje openen en sluiten?",
                  "de sluitcellen", W),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-fotosynthese-en-celademhaling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Fotosynthese en celademhaling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee vergelijkingen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Schrijf de reactievergelijking van de fotosynthese.",
                  r"6 CO₂ + 6 H₂O geeft C₆H₁₂O₆ + 6 O₂", WL),
                 ("kort", "Schrijf de reactievergelijking van de aerobe celademhaling.",
                  r"C₆H₁₂O₆ + 6 O₂ geeft 6 CO₂ + 6 H₂O en energie", WL),
                 ("open", "Leg uit waarom men zegt dat die twee processen in elkaar passen.",
                  "De producten van de ene zijn de grondstoffen van de andere: glucose en zuurstof uit "
                  "de fotosynthese zijn wat de celademhaling verbruikt, en haar koolstofdioxide en "
                  "water zijn wat de fotosynthese nodig heeft.", 3),
             ]),
        dict(kop="Waar gebeurt het?",
             opdracht="Schrijf de plaats in de cel.",
             oefeningen=[
                 ("rij", [("de lichtreacties", "thylakoïdmembraan"),
                          ("de donkerreacties", "stroma"),
                          ("de glycolyse", "cytoplasma")], "Waar?", WW),
                 ("kort", "Waar gaat het pyrodruivenzuur bij voldoende zuurstof naartoe?",
                  "het mitochondrion", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De donkerreactie kan alleen in volledige duisternis plaatsvinden.", False),
                 ("waar", "De glycolyse levert veel meer ATP op dan de reacties in het mitochondrion.",
                  False),
                 ("waar", "Een plant doet ook aan celademhaling, dag en nacht.", True),
                 ("waar", "Een cel kan ATP in grote voorraad opslaan voor later gebruik.", False),
             ]),
        dict(kop="Gisting",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Gisting", "Producten", "Een toepassing"],
                  [["melkzuurgisting", None, None], ["alcoholische gisting", None, None]],
                  "Melkzuurgisting geeft melkzuur en een kleine hoeveelheid energie; melkzuurbacteriën "
                  "maken er yoghurt mee van melk. Alcoholische gisting geeft ethanol, koolstofdioxide "
                  "en een kleine hoeveelheid energie; gist doet daarmee brooddeeg rijzen.", WW),
                 ("open", "Waarom levert gisting veel minder energie op dan de aerobe celademhaling?",
                  "Omdat de glucose maar gedeeltelijk afgebroken wordt. In melkzuur en in ethanol zit "
                  "nog een hoop energie die de cel laat liggen.", 3),
                 ("open", "Een sprinter voelt na honderd meter zijn benen verzuren. Leg uit wat er in "
                          "zijn spiercellen gebeurd is.",
                  "Er was te weinig zuurstof voor de aerobe ademhaling, dus werd het pyrodruivenzuur "
                  "tot melkzuur omgezet. Dat melkzuur hoopt zich op, en dat voelt hij als verzuring.",
                  4),
             ]),
        dict(kop="Een proef uitleggen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom zet je een plant een nacht in het donker voor je een proef over "
                          "fotosynthese start?",
                  "Om het aanwezige zetmeel uit de bladeren te laten verdwijnen. Anders weet je niet "
                  "of het zetmeel dat je achteraf vindt, van de proef komt.", 3),
                 ("kort", "Met welke stof toon je zetmeel in een blad aan?", "joodoplossing", WW),
                 ("open", "Een blad is halfweg met zwart papier bedekt en staat daarna een dag in het "
                          "licht. Wat verwacht je na de joodproef, en waarom?",
                  "Het onbedekte deel kleurt blauwzwart, want daar is zetmeel gevormd. Het bedekte "
                  "deel niet, want zonder licht is er geen fotosynthese geweest.", 4),
             ]),
        dict(kop="ATP en energie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Wat wordt ATP als het een fosfaatgroep afgeeft?", "ADP", "90px"),
                 ("kies", "Hoe noemt men een reactie waarbij energie vrijkomt?",
                  ["endo-energetisch", "exo-energetisch", "neutraal"], 1),
                 ("open", "Noem drie processen waarvoor een cel ATP gebruikt.",
                  "Spiercontractie, zenuwimpulsgeleiding en de synthese van biomoleculen.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-bescherming-en-afweer-tegen-lichaamsvreemde-stoffen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bescherming en afweer tegen lichaamsvreemde stoffen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke verdedigingslijn?",
             opdracht="Schrijf eerste, tweede of derde.",
             oefeningen=[
                 ("rij", [("de zuurmantel op de huid", "eerste"),
                          ("een fagocyt die een bacterie verteert", "tweede"),
                          ("een antistof tegen één antigeen", "derde")], None, W),
                 ("rij", [("lysozym in traanvocht", "eerste"),
                          ("een cytotoxische T-lymfocyt", "derde"),
                          ("koorts", "tweede")], None, W),
             ]),
        dict(kop="Welke cel doet dit?",
             opdracht="Schrijf de naam van de cel.",
             oefeningen=[
                 ("rij", [("maakt antistoffen", "B-lymfocyt"),
                          ("geeft histamine af", "mestcel"),
                          ("doorboort besmette cellen", "natural killer cel")], "Welke cel?", WW),
                 ("rij", [("stuurt met cytokines aan", "T-helperlymfocyt"),
                          ("toont een stuk indringer aan de lymfocyten", "dendritische cel"),
                          ("omsluit en verteert", "fagocyt")], "Welke cel?", WW),
             ]),
        dict(kop="Begrippen onderscheiden",
             opdracht="Leg het verschil uit in volledige zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een antigeen en een pathogeen?",
                  "Een pathogeen is een organisme dat ziekte kan veroorzaken. Een antigeen is een "
                  "lichaamsvreemde stof die een afweerreactie uitlokt, bijvoorbeeld een eiwit op de "
                  "buitenkant van zo'n pathogeen.", 3),
                 ("open", "Wat is het verschil tussen een infectie en een infectieziekte?",
                  "Bij een infectie dringt de kiem binnen. Bij een infectieziekte maakt hij ook ziek. "
                  "Veel infecties ruimt het lichaam op zonder dat je er iets van merkt.", 3),
                 ("open", "Waarom helpt een antibioticum niet tegen een verkoudheid?",
                  "Een antibioticum grijpt in op dingen die alleen een bacterie heeft, zoals haar "
                  "celwand. Een verkoudheid wordt door een virus veroorzaakt, en een virus heeft die "
                  "niet.", 3),
             ]),
        dict(kop="Immunisatie indelen",
             opdracht="Vul de tabel aan met de vier voorbeelden hieronder.",
             oefeningen=[
                 ("tekst", "De vier voorbeelden: de mazelen doormaken · een vaccinatie krijgen · "
                           "antistoffen via de borstvoeding · serumtherapie na een slangenbeet."),
                 ("tabel", ["", "Natuurlijk", "Kunstmatig"],
                  [["actief", None, None], ["passief", None, None]],
                  "Actief en natuurlijk: de mazelen doormaken. Actief en kunstmatig: een vaccinatie. "
                  "Passief en natuurlijk: antistoffen via de borstvoeding. Passief en kunstmatig: "
                  "serumtherapie.", WW),
                 ("waar", "Passieve immunisatie bouwt een afweergeheugen op dat jaren meegaat.", False),
                 ("open", "Leg uit waarom serumtherapie een noodoplossing is en geen vaccin.",
                  "Bij serumtherapie krijg je kant-en-klare antistoffen. Die zijn na enkele weken "
                  "afgebroken en je maakt er zelf geen geheugen bij op, dus ben je daarna weer even "
                  "kwetsbaar als voordien. Een vaccin laat je lichaam zelf antistoffen en "
                  "geheugencellen maken.", 4),
             ]),
        dict(kop="Een besmetting volgen",
             opdracht="Zet de stappen in de juiste orde en leg de laatste uit.",
             oefeningen=[
                 ("open", "Zet in de juiste orde: antigeenpresentatie · een bacterie dringt door een "
                          "wonde binnen · B-lymfocyten maken antistoffen · een fagocyt verteert de "
                          "bacterie.",
                  "Een bacterie dringt door een wonde binnen, een fagocyt verteert de bacterie, "
                  "antigeenpresentatie, B-lymfocyten maken antistoffen.", 3),
                 ("open", "Waarom verloopt een tweede besmetting met dezelfde kiem meestal "
                          "ongemerkt?",
                  "Door het afweergeheugen: B- en T-geheugenlymfocyten blijven jaren leven, dus "
                  "verloopt de secundaire immuunrespons sneller en sterker dan de primaire.", 3),
                 ("open", "Waarom beschermt een vaccinatiecampagne ook mensen die zelf niet "
                          "gevaccineerd zijn?",
                  "Omdat de ziekteverwekker veel minder kans krijgt om zich te verspreiden: hij komt "
                  "te weinig geschikte gastheren tegen om een ketting te vormen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-voortplanting-zwangerschap-en-vruchtbaarheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Voortplanting, zwangerschap en vruchtbaarheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De weg van de bevruchting",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Waar in het vrouwelijk voortplantingsstelsel gebeurt de bevruchting "
                          "normaal?", "in de eileider", WW),
                 ("kort", "Hoe heet het blaasje vooraan op de kop van een zaadcel?",
                  "het acrosoom", WW),
                 ("kort", "Hoe heet het samensmelten van de twee kernen?", "amfimixie", WW),
                 ("open", "Noem de drie barrières die een zaadcel op weg naar de eicel moet "
                          "overwinnen.",
                  "Het zure milieu van de vagina, het slijm van de baarmoederhals en de corona radiata "
                  "rond de eicel.", 2),
                 ("open", "Wat is de functie van de corticale reactie, en waarom is die nodig?",
                  "Ze belet dat er nog een tweede zaadcel binnendringt. Met twee zaadcellen zou de "
                  "zygote te veel chromosomen hebben en niet verder kunnen ontwikkelen.", 3),
             ]),
        dict(kop="De eerste dagen op een rij",
             opdracht="Zet in de juiste orde en vul aan.",
             oefeningen=[
                 ("open", "Zet in de juiste orde: blastula · innesteling · morula · zygote.",
                  "Zygote, morula, blastula, innesteling.", 2),
                 ("rij", [("waaruit het kind groeit", "embryoblast"),
                          ("waaruit de placenta groeit", "trofoblast"),
                          ("het hormoon van de test", "hCG")], None, WW),
                 ("waar", "De innesteling gebeurt in de wand van de baarmoeder.", True),
                 ("open", "Bij de klievingsdelingen worden de cellen talrijker maar niet groter. Wat "
                          "betekent dat voor de grootte van het geheel?",
                  "Het geheel blijft ongeveer even groot als de zygote en bestaat alleen uit steeds "
                  "meer, steeds kleinere cellen.", 3),
             ]),
        dict(kop="Embryonaal of foetaal?",
             opdracht="Schrijf embryonaal of foetaal.",
             oefeningen=[
                 ("rij", [("de kiembladen worden aangelegd", "embryonaal"),
                          ("de organen groeien en rijpen", "foetaal"),
                          ("de organen worden voor het eerst gevormd", "embryonaal")], None, W),
                 ("open", "Waarom zijn de eerste acht weken de gevaarlijkste voor de vrucht?",
                  "Dan worden de organen voor het eerst gevormd, en dus is de vrucht het gevoeligst "
                  "voor schadelijke stoffen. Wie nog niet weet dat ze zwanger is, zit precies in die "
                  "weken.", 3),
                 ("kort", "Vanaf ongeveer welk moment is een foetus levensvatbaar?",
                  r"vanaf ongeveer \(24\) weken", WW),
             ]),
        dict(kop="De placenta",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Noem de drie taken van de placenta.",
                  "Zuurstof en voedingsstoffen doorgeven, afvalstoffen van de vrucht afvoeren, en "
                  "hormonen aanmaken die de zwangerschap in stand houden.", 3),
                 ("waar", "Het bloed van de moeder en dat van de vrucht mengen zich in de placenta.",
                  False),
                 ("open", "De placentabarrière is selectief. Waarom is dat geen reden om je geen "
                          "zorgen te maken over alcohol?",
                  "Ze laat sommige stoffen wel en andere niet door, maar ze is geen muur: alcohol, "
                  "nicotine en veel medicijnen glippen er zonder moeite door.", 3),
                 ("kort", "Wat vervoeren de navelstrengslagaders?",
                  "zuurstofarm bloed van de vrucht naar de placenta", WL),
             ]),
        dict(kop="Wat de vrucht kan schaden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Hoe noemt men een stof die bij een ongeboren kind afwijkingen kan "
                          "veroorzaken?", "een teratogeen", WW),
                 ("open", "Wat is het foetaal alcoholsyndroom, en hoeveel alcohol is veilig?",
                  "Blijvende schade bij een kind door alcoholgebruik tijdens de zwangerschap: "
                  "kleinere groei, kenmerkende gelaatstrekken en moeilijkheden met leren en "
                  "concentratie. Er is geen hoeveelheid waarvan men weet dat ze veilig is.", 4),
                 ("open", "Waarom raadt men een zwangere vrouw aan geen rauw vlees te eten en geen "
                          "kattenbak te verschonen?",
                  "Wegens het risico op besmetting met de toxoplasmoseparasiet.", 2),
             ]),
        dict(kop="Anticonceptie en vruchtbaarheid",
             opdracht="Vul de tabel aan en beantwoord.",
             oefeningen=[
                 ("tabel", ["Methode", "Soort", "Beschermt tegen soa?"],
                  [["de combinatiepil", None, None], ["het condoom", None, None],
                   ["de temperatuurmethode", None, None]],
                  "De combinatiepil is hormonaal en beschermt niet tegen soa. Het condoom is "
                  "mechanisch en beschermt wel tegen soa. De temperatuurmethode is natuurlijk en "
                  "beschermt niet tegen soa.", W),
                 ("open", "Waarin verschilt ICSI van gewone in-vitrofertilisatie?",
                  "Bij ICSI wordt één zaadcel rechtstreeks in de eicel ingebracht. Dat helpt als de "
                  "zaadcellen zelf niet sterk genoeg zijn om binnen te raken.", 3),
                 ("waar", "Bij kunstmatige inseminatie gebeurt de bevruchting buiten het lichaam.",
                  False),
                 ("open", "Noem drie factoren die de vruchtbaarheid kunnen verminderen.",
                  "Roken, zware stress over lange tijd en overgewicht. Ook leeftijd en bepaalde "
                  "aandoeningen spelen mee.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-dna-replicatie-en-celdelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="DNA, replicatie en celdelingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Basenparen",
             opdracht="Schrijf de complementaire DNA-streng.",
             oefeningen=[
                 ("rij", [("AATGC", "TTACG"), ("GGCTA", "CCGAT"), ("TACGT", "ATGCA")], None, WW),
                 ("kort", "Hoeveel waterstofbruggen liggen er tussen guanine en cytosine?",
                  "drie", "90px"),
                 ("kort", "Welke base staat in RNA op de plaats van thymine?", "uracil", W),
             ]),
        dict(kop="Rekenen met basen",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("open", r"In een stuk DNA is \(24\) procent van de basen guanine. Hoeveel procent is "
                          "adenine?",
                  r"Guanine en cytosine zijn elk \(24\) procent, samen \(48\). Voor adenine en thymine blijft "
                  r"\(52\) procent over, gelijk verdeeld, dus \(26\) procent adenine.", 3),
                 ("open", r"In een ander stuk is \(35\) procent thymine. Hoeveel procent is cytosine?",
                  r"Thymine en adenine zijn elk \(35\) procent, samen \(70\). Voor guanine en cytosine blijft "
                  r"\(30\) procent over, dus \(15\) procent cytosine.", 3),
             ]),
        dict(kop="Van DNA tot chromosoom",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("eiwitten waar het DNA rond rolt", "histonen"),
                          ("DNA en eiwit in een niet-delende kern", "chromatine"),
                          ("de insnoering van een chromosoom", "centromeer")], None, WW),
                 ("kort", "Hoeveel chromosomen heeft een menselijke lichaamscel?", r"\(46\)", "70px"),
                 ("open", "Waarom kan een cel haar DNA niet voortdurend sterk opgerold houden?",
                  "Omdat de genen dan niet afgelezen kunnen worden: een strak opgerolde streng laat de "
                  "leesmachine niet toe.", 3),
                 ("open", "Wat lees je van een karyogram af, en wat niet?",
                  "Je leest het aantal chromosomen af, het geslacht van de persoon en een afwijkend "
                  "aantal chromosomen. Welk gen aan of uit staat, zie je er niet op.", 3),
             ]),
        dict(kop="De replicatie",
             opdracht="Schrijf bij elke taak de naam.",
             oefeningen=[
                 ("rij", [("wikkelt de helix open", "helicase"),
                          ("bouwt de nieuwe streng", "DNA-polymerase"),
                          ("plakt de stukjes aan elkaar", "ligase")], None, WW),
                 ("kort", "Hoe heten de losse stukjes van de lagging strand?",
                  "Okazaki-fragmenten", WW),
                 ("open", "Waarom wordt de ene nieuwe streng vlot gebouwd en de andere in stukjes?",
                  r"Het polymerase kan maar in één richting werken, van \(5\) naar \(3\), en de twee oude "
                  "strengen liggen antiparallel. Op de ene kan het dus doorlopen, op de andere moet "
                  "het telkens opnieuw beginnen.", 4),
                 ("waar", "Na de replicatie bestaat elke dubbele helix uit één oude en één nieuwe "
                          "streng.", True),
             ]),
        dict(kop="Mitose en meiose vergelijken",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "Mitose", "Meiose"],
                  [["aantal dochtercellen", None, None], ["aantal chromosomen", None, None],
                   ["genetisch identiek?", None, None]],
                  "Mitose: twee dochtercellen, hetzelfde aantal chromosomen als de moedercel, "
                  "genetisch identiek. Meiose: vier dochtercellen, het halve aantal chromosomen, "
                  "genetisch verschillend van elkaar.", WW),
                 ("open", "Zet de fasen van de mitose in de juiste orde en zeg wat er in de anafase "
                          "gebeurt.",
                  "Profase, metafase, anafase, telofase. In de anafase worden de zusterchromatiden "
                  "naar de polen getrokken.", 3),
                 ("open", "Noem de drie bronnen van genetische variatie bij de voortplanting.",
                  "De crossing-over tussen homologe chromosomen, de toevallige verdeling van de "
                  "chromosomenparen over de dochtercellen, en de willekeurige combinatie bij de "
                  "bevruchting.", 3),
                 ("open", "Waarom gaat de tweede meiotische deling niet gepaard met een nieuwe "
                          "verdubbeling van het DNA?",
                  "Omdat de chromosomen dan nog uit twee chromatiden bestaan. Die tweede deling trekt "
                  "ze gewoon los van elkaar.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-overerving-van-genetisch-materiaal-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Overerving van genetisch materiaal",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De woorden",
             opdracht="Schrijf het juiste woord.",
             oefeningen=[
                 ("rij", [("twee gelijke allelen", "homozygoot"),
                          ("de erfelijke aanleg", "genotype"),
                          ("het zichtbare kenmerk", "fenotype")], None, WW),
                 ("rij", [("de vaste plaats van een gen", "locus"),
                          ("de ouders in een schema", "P-generatie"),
                          ("draagt het allel zonder de aandoening", "drager")], None, WW),
             ]),
        dict(kop="Kruisingen met één kenmerk",
             opdracht="Teken het punnettvierkant op je blad en vul de uitkomst in.",
             oefeningen=[
                 ("kort", "Aa × Aa: welke genotypische verhouding?", r"\(1\) op \(2\) op \(1\)", WW),
                 ("kort", "Aa × Aa: welke fenotypische verhouding?", r"\(3\) op \(1\)", WW),
                 ("kort", r"\(\text{Aa} \cdot aa\): hoeveel procent toont het recessieve kenmerk?",
                  r"\(50\) procent", WW),
                 ("kort", r"\(\text{AA} \cdot aa\): hoeveel procent toont het recessieve kenmerk?",
                  r"\(0\) procent", WW),
                 ("open", "Twee planten met het dominante kenmerk krijgen een nakomeling met het "
                          "recessieve kenmerk. Wat weet je dan zeker over de drie betrokkenen?",
                  "Beide ouders zijn heterozygoot en dragen dus het recessieve allel. De nakomeling is "
                  "homozygoot recessief.", 3),
             ]),
        dict(kop="Als dominantie niet volledig is",
             opdracht="Reken en leg uit.",
             oefeningen=[
                 ("open", "Twee roze leeuwenbekken worden gekruist. Welke kleuren verwacht je, en in "
                          "welke verhouding?",
                  r"\(1\) rood, \(2\) roze, \(1\) wit. Dus \(25\) procent rood, \(50\) procent roze en \(25\) procent wit.", 3),
                 ("waar", "Bij intermediaire overerving vallen de genotypische en de fenotypische "
                          "verhouding in de F2 samen.", True),
                 ("open", "Wat is het verschil tussen intermediaire overerving en codominantie?",
                  "Bij intermediaire overerving vertoont de heterozygoot een tussenvorm, zoals roze "
                  "tussen rood en wit. Bij codominantie komen beide allelen volledig tot uiting, zoals "
                  "bij bloedgroep AB.", 3),
                 ("kort", "Twee ouders met bloedgroep AB: welke bloedgroepen zijn mogelijk?",
                  "A, B of AB", WW),
                 ("kort", "Een vader met O en een moeder met AB: welke bloedgroepen zijn mogelijk?",
                  "A of B", WW),
             ]),
        dict(kop="Twee kenmerken samen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "AaBb × AaBb: welke fenotypische verhouding?", r"\(9\) op \(3\) op \(3\) op \(1\)", WW),
                 ("kort", "AaBb × aabb: welke fenotypische verhouding?", r"\(1\) op \(1\) op \(1\) op \(1\)", WW),
                 ("kort", "Hoeveel soorten gameten maakt een organisme AaBb?", "vier", "90px"),
                 ("open", "Twee genen liggen op hetzelfde chromosoom. Waarom geldt de "
                          "onafhankelijkheidswet dan niet goed?",
                  "Omdat ze samen in dezelfde gameet terechtkomen en dus niet los van elkaar "
                  "doorgegeven worden. Alleen een crossing-over kan ze nog scheiden.", 3),
             ]),
        dict(kop="Geslachtsgebonden",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Noem de drie redenen waarom geslachtsgebonden recessieve aandoeningen "
                          "vaker bij mannen voorkomen.",
                  "Een man heeft maar één X-chromosoom, bij een man volstaat één aangedaan allel, en "
                  "een vrouw kan het gezonde allel op haar tweede X hebben.", 3),
                 ("open", "Een draagster van kleurenblindheid krijgt kinderen met een man die niet "
                          "kleurenblind is. Wat verwacht je bij de zonen en bij de dochters?",
                  "De helft van de zonen is kleurenblind en geen enkele dochter. Een zoon met de "
                  "aangedane X heeft geen tweede X om het op te vangen; een dochter krijgt van haar "
                  "vader een gezonde X.", 4),
                 ("waar", "Een vader kan zijn X-gebonden allel aan zijn zoon doorgeven.", False),
                 ("open", "Noem drie aandoeningen die geslachtsgebonden recessief overerven.",
                  "Rood-groen kleurenblindheid, hemofilie A en de ziekte van Duchenne.", 2),
             ]),
        dict(kop="Een stamboom lezen",
             opdracht="Besluit en verantwoord.",
             oefeningen=[
                 ("open", "Twee ouders zonder het kenmerk hebben een dochter met dat kenmerk. Wat "
                          "besluit je over het kenmerk, en waarom twee keer?",
                  "Het is recessief, want de ouders waren allebei drager zonder het te tonen. Het is "
                  "niet geslachtsgebonden, want een dochter zou dan ook van haar vader een aangedane X "
                  "moeten krijgen, en hij toont het kenmerk niet.", 4),
                 ("waar", "Een dominante aandoening kan een generatie overslaan en dan weer opduiken.",
                  False),
                 ("open", "Een kenmerk slaat in een stamboom een generatie over. Wat zegt dat, en wat "
                          "zegt het niet?",
                  "Het wijst op een recessief kenmerk, dat verborgen in de dragers meereist. Het zegt "
                  "niets over de plaats van het gen op een chromosoom.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-genexpressie-en-dna-technologie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Genexpressie en DNA-technologie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Van DNA naar mRNA",
             opdracht="Schrijf het mRNA dat van deze matrijsstreng afgelezen wordt.",
             oefeningen=[
                 ("rij", [("TAC", "AUG"), ("GGA", "CCU"), ("ATT", "UAA")], None, W),
                 ("rij", [("CGT", "GCA"), ("TTC", "AAG"), ("ACG", "UGC")], None, W),
                 ("kort", "Uit hoeveel basen bestaat één codon?", "drie", "80px"),
                 ("kort", "Welk codon start bijna altijd de translatie?", "AUG", "80px"),
             ]),
        dict(kop="RNA en DNA vergelijken",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "DNA", "RNA"],
                  [["de suiker", None, None], ["de vierde base", None, None],
                   ["aantal strengen", None, None]],
                  "DNA heeft desoxyribose, thymine en twee strengen. RNA heeft ribose, uracil en is "
                  "meestal enkelstrengig.", WW),
                 ("waar", "De genetische code is bij nagenoeg alle organismen dezelfde.", True),
                 ("open", "Waarom kan een bacterie een menselijk gen aflezen en er menselijke insuline "
                          "van maken?",
                  "Omdat de genetische code bij nagenoeg alle organismen dezelfde is: dezelfde codons "
                  "staan voor dezelfde aminozuren.", 3),
             ]),
        dict(kop="De weg van gen tot eiwit",
             opdracht="Schrijf bij elke stap waar ze gebeurt of wie ze doet.",
             oefeningen=[
                 ("rij", [("de transcriptie", "in de celkern"),
                          ("de translatie", "op het ribosoom"),
                          ("maakt het mRNA", "RNA-polymerase")], None, WW),
                 ("kort", "Waar bindt het RNA-polymerase om te starten?", "op de promotor", WW),
                 ("open", "Wat gebeurt er bij de splicing van pre-mRNA?",
                  "De introns worden eruit geknipt en de exons aan elkaar geplakt, zodat alleen de "
                  "stukken overblijven die voor het eiwit nodig zijn.", 3),
                 ("open", "Wat doet een tRNA-molecule, en met welk deel van zichzelf?",
                  "Het brengt het juiste aminozuur aan, en het vindt zijn plaats met zijn anticodon, "
                  "dat op het codon van het mRNA past.", 3),
             ]),
        dict(kop="Mutaties",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("kies", "Eén base wordt door een andere vervangen. Welke mutatie is dat?",
                  ["substitutie", "deletie", "insertie", "genoommutatie"], 0),
                 ("open", "Waarom heeft een deletie van één base vaak zwaardere gevolgen dan een "
                          "substitutie?",
                  "Bij een deletie worden alle codons erna verschoven afgelezen, dus staat er vanaf dat "
                  "punt een heel ander eiwit. Bij een substitutie verandert er vaak maar één aminozuur, "
                  "en soms zelfs dat niet.", 4),
                 ("kort", "Wanneer is een mutatie erfelijk?", "als ze in een geslachtscel zit", WL),
                 ("open", "Noem drie mutagenen.",
                  "Uv-straling, röntgenstraling en benzopyreen uit tabaksrook.", 2),
                 ("waar", "Epigenetische wijzigingen veranderen de volgorde van de basen in het DNA.",
                  False),
             ]),
        dict(kop="Knippen en plakken",
             opdracht="Zet de stappen op een rij en vul aan.",
             oefeningen=[
                 ("open", "Zet de vier stappen van insulineproducerende bacteriën in de juiste orde: "
                          "het plasmide gaat de bacterie binnen · het insulinegen wordt uitgeknipt · "
                          "ligase plakt het gen in het plasmide · een plasmide wordt met hetzelfde "
                          "enzym opengeknipt.",
                  "Het insulinegen wordt uitgeknipt, een plasmide wordt met hetzelfde enzym "
                  "opengeknipt, ligase plakt het gen in het plasmide, het plasmide gaat de bacterie "
                  "binnen.", 4),
                 ("open", "Waarom gebruikt men voor het gen en voor het plasmide hetzelfde "
                          "restrictie-enzym?",
                  "Omdat je dan aan beide kanten dezelfde sticky ends krijgt, en twee stukken met "
                  "dezelfde overhang passen op elkaar.", 3),
                 ("kort", "Hoe noemt men een plasmide dat een vreemd gen draagt?",
                  "een recombinant plasmide", WL),
                 ("open", "Wat is het verschil tussen een cisgeen en een transgeen organisme?",
                  "Bij cisgeen komt het gen uit dezelfde of een kruisbare soort. Bij transgeen uit een "
                  "soort die je nooit zou kunnen kruisen.", 3),
                 ("waar", "Een genetisch gemodificeerd organisme is altijd transgeen.", False),
             ]),
        dict(kop="DNA onderzoeken",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Waarvoor dient een PCR?", "een stukje DNA miljoenen keren kopiëren", WL),
                 ("open", "Bij gelelektroforese komen de kortste fragmenten het verst. Waarom?",
                  "Alle fragmenten worden door het elektrisch veld door de gel getrokken, maar de "
                  "lange blijven sneller in het netwerk van de gel steken. Zo worden ze op lengte "
                  "gescheiden.", 4),
                 ("open", "Noem drie dingen waarvoor men een DNA-fingerprint gebruikt.",
                  "Sporen aan een verdachte koppelen, een vaderschap aantonen en familieleden van "
                  "elkaar onderscheiden.", 2),
                 ("open", "Waarin verschilt gene editing met CRISPR-Cas van het klassieke inbrengen van "
                          "een gen?",
                  "Er wordt heel gericht op één plaats in het genoom gewerkt, met een geleidend RNA en "
                  "een knipeiwit, in plaats van een gen ergens te laten invallen.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ontstaan-en-evolutie-van-soorten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontstaan en evolutie van soorten",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Uit welk vakgebied komt dit argument?",
             opdracht="Schrijf het vakgebied.",
             oefeningen=[
                 ("rij", [("overgangsfossielen", "paleontologie"),
                          ("gelijkende aminozuursequenties", "biochemie"),
                          ("buideldieren in Australië", "biogeografie")], None, WW),
                 ("rij", [("homologe voorpoten", "vergelijkende anatomie"),
                          ("embryo's die vroeg op elkaar lijken", "embryologie"),
                          ("de blinde darm bij de mens", "vergelijkende anatomie")], None, WW),
             ]),
        dict(kop="Homoloog, analoog of rudimentair?",
             opdracht="Schrijf homoloog, analoog of rudimentair.",
             oefeningen=[
                 ("rij", [("de vleugel van een insect en die van een vogel", "analoog"),
                          ("de arm van een mens en de vleugel van een vleermuis", "homoloog"),
                          ("de blinde darm bij de mens", "rudimentair")], None, W),
                 ("open", "Leg het verschil tussen homoloog en analoog uit in je eigen woorden.",
                  "Homologe organen hebben dezelfde bouw en dezelfde oorsprong, maar kunnen een heel "
                  "andere functie hebben. Analoge organen hebben dezelfde functie, maar een andere "
                  "oorsprong.", 4),
             ]),
        dict(kop="Fossielen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("waar", "Fossielen in diepere aardlagen zijn in het algemeen jonger dan die in de "
                          "lagen erboven.", False),
                 ("open", "Waarom vinden we maar van een klein deel van de uitgestorven soorten "
                          "fossielen terug?",
                  "Omdat fossilisatie zeldzame omstandigheden vraagt: snel bedekt worden, zonder "
                  "zuurstof, in de juiste bodem.", 3),
                 ("open", "Wat maakt Archaeopteryx een overgangsfossiel?",
                  "Hij combineert kenmerken van reptielen en vogels: tanden en een lange staart naast "
                  "veren.", 3),
             ]),
        dict(kop="Lamarck en Darwin",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Wat beweerde Lamarck over de lange nek van de giraf, en waarom klopt dat "
                          "niet?",
                  "Hij dacht dat verworven eigenschappen aan de nakomelingen doorgegeven worden, dus "
                  "dat een giraf die rekt langernekkige jongen krijgt. Wat je in je leven met je "
                  "lichaam doet, verandert je geslachtscellen niet.", 4),
                 ("open", "Noem de drie gedachten die samen de kern van Darwins theorie vormen.",
                  "Variatie, selectie en erfelijkheid.", 2),
                 ("waar", "De moderne evolutietheorie heeft de ideeën van Darwin volledig verworpen.",
                  False),
             ]),
        dict(kop="Selectie uitleggen",
             opdracht="Leg uit wat er precies gebeurd is.",
             oefeningen=[
                 ("open", "Een arts zegt: dit antibioticum maakt de bacteriën resistent. Verbeter die "
                          "zin.",
                  "Het antibioticum maakt niets resistent. Er waren al toevallig ongevoelige "
                  "bacteriën; die overleven en planten zich voort, terwijl de gevoelige opgeruimd "
                  "worden.", 4),
                 ("open", "Waarom werd de donkere peper-en-zoutvlinder talrijker tijdens de "
                          "industriële revolutie?",
                  "Op beroete bomen viel ze minder op, dus werd ze minder vaak opgegeten en liet ze "
                  "meer nakomelingen na.", 3),
                 ("kort", "Wat is de fitness van een fenotype?",
                  "hoeveel vruchtbare nakomelingen het gemiddeld oplevert", WL),
                 ("waar", "Genetische drift werkt sterker in een kleine populatie dan in een grote.",
                  True),
             ]),
        dict(kop="Soortvorming",
             opdracht="Schrijf de isolatievorm en besluit.",
             oefeningen=[
                 ("rij", [("gescheiden door een nieuw gebergte", "geografisch"),
                          ("paren in verschillende maanden", "temporeel"),
                          ("een heel andere baltsdans", "gedrag")], None, WW),
                 ("kort", "Wanneer spreekt men van twee aparte soorten?",
                  "als ze geen vruchtbaar nageslacht meer geven", WL),
                 ("open", "Noem de drie dingen die samen nodig zijn voor soortvorming.",
                  "Variatie in de populatie, isolatie tussen de groepen, en selectie die de groepen uit "
                  "elkaar duwt.", 2),
                 ("waar", "Een hoge genetische diversiteit maakt een populatie kwetsbaarder voor een "
                          "nieuwe ziekte.", False),
                 ("open", "Een zwemmer die veel traint, krijgt brede schouders. Is dat een adaptatie? "
                          "Verantwoord.",
                  "Nee. Een adaptatie is een erfelijk kenmerk dat een organisme beter doet passen bij "
                  "zijn omgeving. Brede schouders door training zijn niet erfelijk.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-biomoleculen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Biomoleculen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Suiker, lipide of proteïne?",
             opdracht="Schrijf suiker, lipide of proteïne.",
             oefeningen=[
                 ("rij", [("glycogeen", "suiker"), ("hemoglobine", "proteïne"),
                          ("cholesterol", "lipide")], None, W),
                 ("rij", [("cellulose", "suiker"), ("een fosfolipide", "lipide"),
                          ("een enzym", "proteïne")], None, W),
             ]),
        dict(kop="Suikers",
             opdracht="Vul aan en leg uit.",
             oefeningen=[
                 ("rij", [("glucose en fructose samen", "sacharose"),
                          ("glucose en galactose samen", "lactose"),
                          ("de binding tussen twee suikers", "glycosidisch")], None, WW),
                 ("open", "Zetmeel en cellulose zijn allebei polysachariden van glucose. Waarom kan de "
                          "mens het ene verteren en het andere niet?",
                  "De glucosemoleculen zitten anders aan elkaar. De mens mist het enzym dat de "
                  "bindingen van cellulose verbreekt.", 3),
                 ("open", "Waarom noemt men brood met veel vezels een trage suiker?",
                  "Omdat de glucose er traag uit vrijkomt en de bloedsuiker daardoor minder piekt. "
                  "Hetzelfde aantal gram koolhydraten geeft dus niet hetzelfde verloop in je bloed.",
                  3),
                 ("open", "Waarom krijgen sommige mensen buikklachten van melk?",
                  "Omdat ze het enzym missen dat lactose splitst.", 2),
             ]),
        dict(kop="Lipiden",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Uit welke twee soorten bouwstenen bestaat een triglyceride?",
                  "glycerol en drie vetzuren", WL),
                 ("waar", "Oliën bevatten over het algemeen meer onverzadigde vetzuren dan harde "
                          "vetten.", True),
                 ("waar", "Lipiden leveren per gram minder energie dan suikers.", False),
                 ("open", "Waarom is een fosfolipide geschikt om een membraan te vormen?",
                  "Omdat het een waterminnende kop en waterafstotende staarten heeft. In water gaan de "
                  "staarten naar elkaar toe en de koppen naar buiten, en zo ontstaat van zelf een "
                  "dubbellaag.", 4),
                 ("open", "Een vogel vet zijn veren in. Welke eigenschap van lipiden gebruikt hij, en "
                          "waarvoor?",
                  "Dat ze water afstoten, dus hydrofoob zijn. Zo blijven zijn veren droog en isoleren "
                  "ze nog.", 3),
             ]),
        dict(kop="Proteïnen in vier lagen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Structuur", "Wat ze is"],
                  [["primair", None], ["secundair", None], ["tertiair", None], ["quaternair", None]],
                  "Primair: de volgorde van de aminozuren in de keten. Secundair: de alfahelix en de "
                  "bètaplaat. Tertiair: de ruimtelijke vorm van de hele keten. Quaternair: meerdere "
                  "ketens die samen één eiwit vormen.", WL),
                 ("open", "Noem de drie groepen die elk aminozuur altijd heeft.",
                  "Een carboxylgroep, een aminogroep en een restgroep.", 2),
                 ("open", "Waarom gaan apolaire restgroepen bij een opgevouwen eiwit meestal naar de "
                          "binnenkant?",
                  "Omdat ze water afstoten. Aan de buitenkant staat het eiwit in water, dus is binnen "
                  "de rustigste plaats voor hen.", 3),
                 ("open", "Een eiwit wordt te sterk verhit. Wat gebeurt er, en waarom werkt het daarna "
                          "niet meer?",
                  "Het verliest zijn vorm. De werking van een eiwit hangt van die vorm af: bij een "
                  "enzym past de actieve plaats dan niet meer op de stof.", 4),
             ]),
        dict(kop="Welk eiwit?",
             opdracht="Schrijf de naam of de taak.",
             oefeningen=[
                 ("rij", [("vervoert zuurstof in het bloed", "hemoglobine"),
                          ("laten een spier samentrekken", "actine en myosine"),
                          ("laten water door het membraan", "aquaporines")], None, WW),
                 ("open", "Noem drie taken die proteïnen in een cel kunnen hebben.",
                  "Reacties versnellen als enzym, indringers herkennen als antilichaam, en de "
                  "genexpressie regelen als transcriptiefactor.", 2),
             ]),
        dict(kop="Opbouw en afbraak",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("twee bouwstenen verbinden, water komt vrij", "condensatie"),
                          ("een binding verbreken met water", "hydrolyse")], None, WW),
                 ("rij", [("een triglyceride verteren", "glycerol en vetzuren"),
                          ("een eiwit verteren", "aminozuren"),
                          ("zetmeel verteren", "glucose")], "Wat komt er vrij?", WL),
                 ("open", "Waarom zegt men dat de opbouw en de afbraak van suikers, eiwitten en vetten "
                          "volgens hetzelfde principe verlopen?",
                  "Omdat het altijd dezelfde twee reacties zijn: een condensatiereactie om te "
                  "verbinden, met water als bijproduct, en een hydrolysereactie om met water te "
                  "splitsen.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-snelheid-van-een-chemische-reactie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Snelheid van een chemische reactie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Sneller of trager?",
             opdracht="Schrijf sneller, trager of niets.",
             oefeningen=[
                 ("rij", [("de temperatuur verhogen", "sneller"),
                          ("een brok in poeder verdelen", "sneller"),
                          ("een groter vat nemen bij een gasreactie", "trager")], None, W),
                 ("rij", [("een katalysator toevoegen", "sneller"),
                          ("een groter reactievat van glas in plaats van staal", "niets"),
                          ("de concentratie verlagen", "trager")], None, W),
             ]),
        dict(kop="Welke factor is het?",
             opdracht="Schrijf de factor die hier verandert.",
             oefeningen=[
                 ("rij", [("zaagmeel brandt sneller dan een blok", "verdelingsgraad"),
                          ("waterstofperoxide in een bruine fles", "licht"),
                          ("een gasmengsel in een kleiner vat persen", "concentratie")], None, WW),
                 ("open", "Dezelfde hoeveelheid kalk reageert met zuur, één keer als brokjes en één "
                          "keer als poeder. Wat verschilt er aan de snelheid, en wat niet?",
                  "Het poeder reageert sneller, want er is veel meer contactoppervlak. De hoeveelheid "
                  "gas op het einde is dezelfde: de verdelingsgraad verandert de snelheid, niet de "
                  "opbrengst.", 4),
             ]),
        dict(kop="Het botsingsmodel",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Wanneer is een botsing effectief? Noem de twee voorwaarden.",
                  "De deeltjes moeten genoeg energie hebben én met de juiste kant tegen elkaar botsen. "
                  "Ontbreekt er één van de twee, dan gebeurt er niets.", 3),
                 ("open", "Wat gebeurt er met de stoffen bij een elastische botsing?",
                  "Niets: de deeltjes stuiteren van elkaar weg en er ontstaat geen nieuwe stof.", 2),
                 ("open", "Leg uit waarom een hogere temperatuur op twee manieren tegelijk helpt.",
                  "De deeltjes bewegen sneller, dus botsen ze vaker per seconde. En ze botsen harder, "
                  "dus heeft een groter deel van de botsingen genoeg energie.", 4),
             ]),
        dict(kop="Het energiediagram",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de hoogte van de berg boven de reagentia", "activeringsenergie"),
                          ("de top van de berg", "geactiveerd complex"),
                          ("het hoogteverschil begin en einde", "reactie-energie")], None, WW),
                 ("waar", "Bij een exo-energetische reactie liggen de producten lager dan de "
                          "reagentia.", True),
                 ("waar", "Een endo-energetische reactie heeft geen activeringsenergie nodig.", False),
                 ("open", "Een katalysator verlaagt de top van het energiediagram. Wat verandert "
                          "daardoor en wat niet?",
                  "De activeringsenergie wordt kleiner, dus halen meer botsingen de drempel en gaat de "
                  "reactie sneller. De energie van de reagentia en van de producten blijft gelijk, dus "
                  "de reactie-energie verandert niet, en de opbrengst ook niet.", 4),
                 ("open", "Waarom verloopt een reactie met een hoge activeringsenergie bij "
                          "kamertemperatuur meestal traag?",
                  "Omdat maar weinig deeltjes genoeg energie hebben om over die hoge berg te raken.", 3),
             ]),
        dict(kop="Grafieken lezen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Op een concentratie-tijdgrafiek zakt de lijn van een reagens eerst steil en "
                          "daarna almaar vlakker. Waarom gaat de reactie trager?",
                  "In het begin zijn er het meeste reagensdeeltjes en dus het meeste botsingen. Hoe "
                  "meer reagens opgebruikt is, hoe minder botsingen en hoe trager de reactie.", 4),
                 ("open", "Wat lees je op een snelheid-tijdgrafiek rechtstreeks af dat je op een "
                          "concentratie-tijdgrafiek eerst moet afleiden?",
                  "De snelheid zelf. Op een concentratie-tijdgrafiek moet je eerst naar de steilheid van "
                  "de lijn kijken.", 3),
                 ("open", "Twee proeven met dezelfde stoffen verlopen even snel niet. Noem drie "
                          "mogelijke oorzaken, en één onmogelijke.",
                  "Mogelijk: een andere temperatuur, een andere concentratie, een andere "
                  "verdelingsgraad, of een katalysator. Onmogelijk: een andere reactievergelijking, "
                  "want dezelfde stoffen geven altijd dezelfde vergelijking.", 4),
             ]),
        dict(kop="Boltzmann en enzymen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("open", "Bij een hogere temperatuur schuift de top van de Boltzmannverdeling naar "
                          "rechts en wordt ze lager en breder. Waarom gaat de reactie daardoor sneller?",
                  "Omdat er een veel groter deel van de oppervlakte rechts van de activeringsenergie "
                  "ligt, en dus een groter deel van de deeltjes genoeg energie heeft om te reageren.",
                  4),
                 ("open", "Wat doet een katalysator met de streep van de activeringsenergie in zo'n "
                          "verdeling?",
                  "Hij zet die streep naar links, zodat meer deeltjes genoeg energie hebben. De "
                  "verdeling van de deeltjes zelf blijft gelijk.", 3),
                 ("open", "Waarom zijn enzymen onmisbaar in een cel? Opwarmen is toch ook een manier om "
                          "een reactie te versnellen.",
                  "Opwarmen kan een cel niet: haar temperatuur staat vast. Een enzym verlaagt de "
                  "activeringsenergie, zodat de reactie bij lichaamstemperatuur toch snel genoeg "
                  "verloopt.", 4),
                 ("open", "Een proef verloopt te traag en opwarmen mag niet. Welke drie factoren blijven "
                          "er over?",
                  "Een katalysator toevoegen, de stof fijner verdelen, of de concentratie verhogen.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-chemisch-evenwicht-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Chemisch evenwicht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Aflopend, evenwicht of geen reactie?",
             opdracht="Schrijf aflopend, evenwicht of geen reactie.",
             oefeningen=[
                 ("rij", [("de lijn van een reagens zakt tot op de as", "aflopend"),
                          ("alle lijnen blijven van het begin af vlak", "geen reactie"),
                          ("de lijnen veranderen en lopen daarna vlak door", "evenwicht")],
                  "Welke uitkomst?", WW),
                 ("open", "Hoe ga je in het labo na of je met een evenwicht te doen hebt? Noem twee "
                          "manieren.",
                  "Nakijken of er op het einde nog van beide reagentia is, en iets toevoegen om te zien "
                  "of er nog iets verandert.", 3),
             ]),
        dict(kop="Limiterend of in overmaat?",
             opdracht="Reken en antwoord.",
             oefeningen=[
                 ("kort", r"\(2\) mol A met \(5\) mol B, reactie één op één. Welke stof is in overmaat?",
                  "stof B", W),
                 ("kort", "Hoeveel mol B blijft er dan over?", r"\(3\) mol", W),
                 ("kort", r"\(3\) mol A met \(3\) mol B, reactie één op twee (A : B). Welke stof is "
                          "limiterend?", "stof B", W),
                 ("open", "Waarom gebruikt men bij een proef soms met opzet één reagens in overmaat?",
                  "Om zeker te zijn dat het andere reagens volledig reageert.", 2),
             ]),
        dict(kop="Dynamisch evenwicht",
             opdracht="Vul aan.",
             oefeningen=[
                 ("waar", "In een chemisch evenwicht zijn de concentraties van reagentia en producten "
                          "altijd aan elkaar gelijk.", False),
                 ("waar", "Zodra een evenwicht bereikt is, worden er geen nieuwe productmoleculen meer "
                          "gevormd.", False),
                 ("open", "Leg uit wat men bedoelt met een dynamisch evenwicht.",
                  "De heen- en de terugreactie blijven doorgaan, en even snel. Van buiten lijkt er niets "
                  "te gebeuren, van binnen gebeurt er voortdurend iets.", 3),
                 ("open", "Beschrijf wat de twee snelheden doen op weg naar het evenwicht.",
                  "De heenreactie vertraagt, want de reagentia raken op. De terugreactie versnelt, want "
                  "er komt steeds meer product. In het evenwicht zijn ze gelijk.", 4),
             ]),
        dict(kop="Welke kant schuift het op?",
             opdracht="Schrijf links, rechts of niets.",
             oefeningen=[
                 ("rij", [("extra reagens toevoegen", "rechts"),
                          ("product wegnemen", "rechts"),
                          ("een reagens wegnemen", "links")], None, W),
                 ("rij", [("een katalysator toevoegen", "niets"),
                          ("opwarmen van een exo-energetisch evenwicht", "links"),
                          ("afkoelen van een exo-energetisch evenwicht", "rechts")], None, W),
                 ("kort", "Hoe heet de wet die dit alles voorspelt?",
                  "de wet van Le Chatelier en Van 't Hoff", WL),
                 ("open", "Formuleer die wet in één zin, in je eigen woorden.",
                  "Een evenwicht schuift zo op dat het de verstoring tegenwerkt.", 2),
             ]),
        dict(kop="Gasevenwichten en druk",
             opdracht="Reken en besluit.",
             oefeningen=[
                 ("open", r"Een gasevenwicht heeft links \(3\) mol gas en rechts \(2\) mol gas. Je perst het "
                          "mengsel in een kleiner vat. Welke kant schuift het op, en waarom?",
                  "Naar rechts, naar de kant met minder gasdeeltjes. Zo neemt het mengsel minder plaats "
                  "in en werkt het de drukverhoging tegen.", 3),
                 ("open", r"Een ander gasevenwicht heeft links \(2\) mol gas en rechts \(2\) mol gas. Wat "
                          "gebeurt er bij een volumeverandering, en waarom?",
                  "Niets. Er is geen kant die het drukverschil kan opvangen, dus blijft het evenwicht "
                  "liggen waar het lag.", 3),
                 ("open", "Een mengsel van een bruin gas en een kleurloos gas wordt bleker als je het "
                          "afkoelt. Wat besluit je over de reactie naar het kleurloze gas?",
                  "Dat ze warmte afgeeft, dus exo-energetisch is. Bij afkoelen schuift het evenwicht "
                  "naar de kant die warmte vrijmaakt.", 4),
             ]),
        dict(kop="Een grafiek ontleden",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Welke drie dingen bekijk je om uit een grafiek af te leiden welke factor een "
                          "evenwicht verstoord heeft?",
                  "Welke lijn als eerste plots verspringt, in welke richting de lijnen daarna evolueren, "
                  "en of alle lijnen op hetzelfde moment van richting veranderen.", 3),
                 ("open", "Op een grafiek springt één lijn plots omhoog en bewegen de andere daarna "
                          "traag mee. Wat is er gebeurd?",
                  "Er is van die ene stof iets toegevoegd. Was het de temperatuur of het volume, dan "
                  "zouden alle lijnen samen van richting veranderen.", 3),
                 ("open", "Noem de drie ingrepen waarmee een fabriek uit een evenwicht meer product "
                          "haalt.",
                  "Het product onderweg uit het vat afvoeren, extra reagens blijven toevoegen, en de "
                  "temperatuur in de gunstige richting zetten.", 3),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-organische-stoffen-classificatie-eigenschappen-en-toepassingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Organische stoffen: classificatie, eigenschappen en toepassingen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Tot welke stofklasse hoort het?",
             opdracht="Schrijf de stofklasse.",
             oefeningen=[
                 ("rij", [("CH₃CH₂OH", "alcoholen"), ("CH₃COOH", "carbonzuren"),
                          ("CH₃COCH₃", "ketonen")], None, WW),
                 ("rij", [("C₄H₁₀", "alkanen"), ("HCHO", "aldehyden"),
                          ("CH3OCH3", "ethers")], None, WW),
                 ("rij", [("propaanzuur", "carbonzuren"), ("etheen", "alkenen"),
                          ("methaanamine", "aminen")], None, WW),
             ]),
        dict(kop="De kenmerkende groep",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Stofklasse", "Kenmerkende groep"],
                  [["alcoholen", None], ["carbonzuren", None], ["esters", None], ["ethers", None]],
                  "Alcoholen hebben een OH-groep aan de keten. Carbonzuren een COOH-groep. Esters de "
                  "groep COO tussen twee koolstofketens. Ethers een zuurstofatoom tussen twee "
                  "koolstofketens.", WL),
                 ("open", "Wat is het verschil tussen een aldehyde en een keton?",
                  "Alleen de plaats van de carbonylgroep: bij een aldehyde staat ze aan het uiteinde van "
                  "de keten, bij een keton middenin.", 3),
                 ("waar", "Een amine heeft net als een alcohol een OH-groep als kenmerkende groep.",
                  False),
                 ("open", "Iemand zet CHCl₃ bij de alcoholen. Verbeter en verantwoord.",
                  "Fout: er staat geen OH-groep in, enkel chloor. Het is een gehalogeneerde "
                  "koolwaterstof.", 3),
             ]),
        dict(kop="Kookpunten vergelijken",
             opdracht="Schrijf welke stof het hoogste kookpunt heeft, en waarom.",
             oefeningen=[
                 ("open", "Ethaan of ethanol?",
                  "Ethanol. Ethanol vormt waterstofbruggen en ethaan niet, en een waterstofbrug is de "
                  "sterkste intermoleculaire kracht.", 3),
                 ("open", "Butaan of octaan?",
                  "Octaan. Hoe langer de keten, hoe sterker de londondispersiekracht tussen de "
                  "moleculen, want er is meer oppervlak dat raakt.", 3),
                 ("open", "Een rechte of een sterk vertakte keten met dezelfde formule?",
                  "De rechte keten. Een bolvormige, vertakte molecule raakt haar buren op minder "
                  "plaatsen aan, dus is de londondispersiekracht zwakker.", 3),
             ]),
        dict(kop="Polair of apolair?",
             opdracht="Schrijf polair of apolair, en antwoord.",
             oefeningen=[
                 ("rij", [("wasbenzine", "apolair"), ("water", "polair"),
                          ("CCl₄", "apolair")], None, W),
                 ("kort", "Welk oplosmiddel kies je voor een vlek van een apolaire stof?",
                  "wasbenzine", WW),
                 ("open", "Methanol mengt met water, een lang alkaan niet. Leg beide uit.",
                  "Methanol kan waterstofbruggen met water leggen, dus mengt het. Een lang alkaan is "
                  "apolair en kan dat niet; gelijk lost op in gelijk.", 4),
                 ("open", "Waarom lost een alcohol met een heel lange keten bijna niet meer op in "
                          "water?",
                  "Omdat de lange apolaire staart zwaarder doorweegt dan de OH-groep.", 3),
             ]),
        dict(kop="Zeep en membranen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Beschrijf hoe een zeepmolecule een vetdruppel uit de was haalt.",
                  "Ze heeft een lange apolaire staart en een polaire kop. De staarten gaan in het vet, "
                  "de koppen naar het water, en zo vormen de zeepmoleculen een micel rond de druppel, "
                  "die met het water mee weggaat.", 4),
                 ("waar", "Een fosfolipide heeft net als zeep een polaire kop en apolaire staarten.",
                  True),
                 ("kort", "Hoe heet het bolletje dat zeepmoleculen rond een vetdruppel vormen?",
                  "een micel", W),
             ]),
        dict(kop="Stoffen met een gebruiksnaam",
             opdracht="Schrijf de stof.",
             oefeningen=[
                 ("rij", [("hoofdbestanddeel van aardgas", "methaan"),
                          ("brandspiritus", "methanol"),
                          ("azijnzuur", "CH₃COOH")], None, WW),
                 ("rij", [("mierenzuur", "HCOOH"), ("aceton", "propanon"),
                          ("formol", "methanal")], None, WW),
                 ("open", "Noem drie dingen die je over etheen weet.",
                  "Het is een alkeen, het heeft een dubbele binding, en het is de bouwsteen van "
                  "polyetheen.", 2),
                 ("open", "Waarom noemt men alkanen verzadigde koolwaterstoffen?",
                  "Omdat er geen waterstofatomen meer bij kunnen: elke plaats is al bezet.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kunststoffen-nanomaterialen-en-duurzame-chemie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunststoffen, nanomaterialen en duurzame chemie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke kunststof?",
             opdracht="Schrijf de afkorting.",
             oefeningen=[
                 ("rij", [("drankflessen en kledingvezels", "PET"),
                          ("de antiaanbaklaag van een pan", "PTFE"),
                          ("opgebouwd uit etheen", "PE")], None, W),
                 ("rij", [("buizen en raamprofielen", "PVC"),
                          ("isolatie en verpakking in schuimvorm", "PS"),
                          ("nylon", "PA")], None, W),
             ]),
        dict(kop="Polyadditie of polycondensatie?",
             opdracht="Schrijf welk reactietype, en antwoord.",
             oefeningen=[
                 ("rij", [("PE", "polyadditie"), ("PET", "polycondensatie"),
                          ("PVC", "polyadditie")], None, WW),
                 ("open", "Wat is het verschil tussen de twee reactietypes?",
                  "Polyadditie gebruikt een dubbele binding om de monomeren aan elkaar te rijgen, en er "
                  "komt niets vrij. Bij polycondensatie komt er telkens een kleine molecule vrij, "
                  "meestal water.", 4),
                 ("kort", "Hoe heet de kleine molecule waaruit een kunststof opgebouwd wordt?",
                  "een monomeer", WW),
             ]),
        dict(kop="Thermoplast, thermoharder of elastomeer?",
             opdracht="Schrijf het soort, en antwoord.",
             oefeningen=[
                 ("rij", [("wordt bij opwarmen week", "thermoplast"),
                          ("komt na samenpersen terug", "elastomeer"),
                          ("veel crosslinks, niet te smelten", "thermoharder")], None, WW),
                 ("kort", "Hoe heten de dwarsverbindingen tussen de ketens?", "crosslinks", WW),
                 ("open", "Je hebt een soepele dichting nodig die na samenpersen terugkomt. Welk soort "
                          "kies je, en waarom?",
                  "Een elastomeer. Die vervormt onder een kracht en komt daarna terug in zijn oude "
                  "vorm.", 3),
                 ("open", "Waarom zijn thermoplasten makkelijker te recycleren dan thermoharders?",
                  "Omdat je ze opnieuw kan smelten en vormen. Een thermoharder zit met veel crosslinks "
                  "vast en smelt niet meer.", 3),
             ]),
        dict(kop="Nanomaterialen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een buckyball", "0D"), ("een koolstofnanobuis", "1D"),
                          ("een laagje grafeen", "2D")], "Welke structuur?", W),
                 ("kort", "Tussen welke twee maten ligt een nanomateriaal?",
                  r"\(1\) en \(100\) nanometer", WW),
                 ("kort", "Hoe heet het nanomateriaal van één laag koolstofatomen?", "grafeen", WW),
                 ("waar", "Bij een bottom-upproductie bouw je een nanomateriaal op uit atomen of "
                          "moleculen.", True),
                 ("open", "Nanodeeltjes hebben een heel groot oppervlak per volume-eenheid. Noem twee "
                          "gevolgen daarvan.",
                  "Ze zijn vaak veel reactiever, en hun smeltpunt kan lager liggen dan dat van een groot "
                  "stuk van dezelfde stof.", 3),
                 ("open", "Waarom zit er nanotitaandioxide in zonnecrème en geen gewoon "
                          "titaandioxide?",
                  "De nanovorm houdt UV-licht tegen en blijft toch doorzichtig. De grove vorm geeft een "
                  "witte laag op de huid.", 3),
                 ("open", "Dezelfde eigenschap die nanodeeltjes nuttig maakt, maakt ze ook een risico. "
                          "Leg uit.",
                  "Hun kleine maat en hun reactiviteit maken dat ze diep in een lichaam of in het milieu "
                  "kunnen terechtkomen, en dat ze moeilijk tegen te houden en te volgen zijn.", 4),
             ]),
        dict(kop="De Ladder van Lansink",
             opdracht="Zet in de juiste orde en antwoord.",
             oefeningen=[
                 ("open", "Zet van hoog naar laag: hergebruiken · preventie · recycleren · storten.",
                  "Preventie, hergebruiken, recycleren, storten.", 2),
                 ("rij", [("afval verwerken tot iets van lagere kwaliteit", "downcycling"),
                          ("het nieuwe product is méér waard", "upcycling"),
                          ("nemen, maken, weggooien", "lineaire economie")], None, WW),
                 ("open", "Wat is het kernidee van cradle to cradle?",
                  "Dat afval van het ene product grondstof is voor het volgende, zodat er in het systeem "
                  "geen afval meer bestaat.", 3),
             ]),
        dict(kop="Duurzaam of niet?",
             opdracht="Vul aan en verantwoord.",
             oefeningen=[
                 ("waar", "Een biogebaseerde kunststof is altijd ook biodegradeerbaar.", False),
                 ("open", "Een fles draagt het label biogebaseerd. Wat weet je daardoor, en wat niet?",
                  "Je weet dat ze uit plantaardige of dierlijke grondstoffen gemaakt is. Je weet niet of "
                  "ze afbreekt: bio-PE uit rietsuiker blijft even lang liggen als gewone PE.", 4),
                 ("rij", [("uit aardgas, met uitstoot", "grijs"),
                          ("met afvang en opslag van CO₂", "blauw"),
                          ("met hernieuwbare stroom", "groen")], "Welke waterstof?", W),
                 ("kort", "Wat is grijs water?",
                  "licht vervuild water van bad, lavabo of wasmachine", WL),
                 ("waar", "Een CO₂-neutraal proces neemt meer CO₂ op dan het uitstoot.", False),
                 ("open", "Wat is greenwashing? Geef een voorbeeld.",
                  "Een product duurzamer voorstellen dan het is, bijvoorbeeld een groen blaadje op de "
                  "verpakking zetten zonder dat er in het proces iets veranderd is.", 3),
                 ("open", "Waarom zijn microplastics een probleem, en waar komen ze onder meer van?",
                  "Ze blijven heel lang in het milieu en komen in de voedselketen. Ze komen niet alleen "
                  "van weggegooid afval, maar ook van autobanden, wasbeurten van synthetische kleding en "
                  "afbrokkelende verf.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektrostatica-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrostatica",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Door wrijving, contact of influentie?",
             opdracht="Schrijf hoe het voorwerp geladen raakt.",
             oefeningen=[
                 ("rij", [("een ballon in je haar wrijven", "wrijving"),
                          ("een geladen staaf tegen een bol houden zonder te raken", "influentie"),
                          ("een geladen staaf tegen een bol duwen", "contact")], None, WW),
                 ("kort", "Welke deeltjes verhuizen er bij laden door wrijving?",
                  "elektronen", WW),
                 ("open", "Je wrijft twee voorwerpen tegen elkaar. Noem drie dingen die dan gelden.",
                  "Het ene wordt positief en het andere negatief, de twee ladingen zijn even groot, en "
                  "er zijn elektronen van het ene naar het andere voorwerp gegaan.", 3),
             ]),
        dict(kop="Welke lading houdt het voorwerp?",
             opdracht="Schrijf positief, negatief of neutraal.",
             oefeningen=[
                 ("rij", [("een neutrale metalen bol aangeraakt met een negatieve staaf", "negatief"),
                          ("een geladen bol die je aardt", "neutraal"),
                          ("een geaarde bol bij een negatieve staaf, aarding eerst verbroken",
                           "positief")], None, W),
                 ("open", r"Twee identieke metalen bollen, de ene met \(8\) eenheden lading en de andere "
                          "neutraal, raken elkaar even aan. Hoeveel houdt elke bol?",
                  r"Elk \(4\) eenheden: de lading verdeelt zich gelijk over twee identieke bollen.", 3),
                 ("open", "Waarom wordt een voorwerp door influentie zonder aarding niet echt geladen?",
                  "Omdat de lading er alleen in opschuift. Zodra de geladen staaf weg is, is alles weer "
                  "zoals het was.", 3),
             ]),
        dict(kop="Waarom trekt dat aan?",
             opdracht="Leg uit in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom trekt een geladen staaf een neutraal snippertje papier aan?",
                  "Door influentie komt de tegengestelde lading van het papier dichterbij. Die dichtste "
                  "kant trekt harder aan dan de verste kant afstoot, dus blijft er aantrekking over.", 4),
                 ("open", "Een ballon die je in je haar gewreven hebt, blijft aan de muur hangen. Leg "
                          "uit.",
                  "De geladen ballon polariseert de muur: de ladingen in de moleculen van de muur "
                  "schuiven op, zodat de tegengestelde lading naar de ballon toe komt.", 4),
                 ("kort", "Met welk toestel toon je in het labo aan dat een voorwerp geladen is?",
                  "een elektroscoop", WW),
             ]),
        dict(kop="Rekenen met de wet van Coulomb",
             opdracht="Reken uit en schrijf je reden op.",
             oefeningen=[
                 ("rij", [("de afstand verdubbelen", "vier keer kleiner"),
                          ("de afstand verdrievoudigen", "negen keer kleiner"),
                          ("twee keer dichter brengen", "vier keer groter")], None, WL),
                 ("rij", [("één lading verdrievoudigen", "drie keer groter"),
                          ("beide ladingen verdubbelen", "vier keer groter"),
                          ("één lading halveren", "twee keer kleiner")], None, WL),
                 ("open", "Waarom werkt de afstand zoveel sterker door dan de lading?",
                  "Omdat de afstand in het kwadraat in de formule staat en de ladingen niet. Twee keer "
                  "verder is vier keer minder kracht.", 3),
                 ("waar", "De kracht die lading A op lading B uitoefent, is even groot als die van B op "
                          "A, ook als A veel groter is.", True),
             ]),
        dict(kop="Vectoren lezen",
             opdracht="Besluit en verantwoord.",
             oefeningen=[
                 ("open", "Je ziet een vector die van lading A weg wijst, naar lading B toe. Wat weet je "
                          "over A en B?",
                  "Dat ze ongelijksoortig zijn, want ze trekken elkaar aan.", 3),
                 ("kort", "Drie ladingen liggen op een rij. Hoe bepaal je de kracht op de middelste?",
                  "door de twee krachtvectoren samen te tellen", WL),
                 ("kies", "Welke kracht werkt tussen twee gelijksoortige ladingen?",
                  ["aantrekking", "afstoting", "geen kracht"], 1),
             ]),
        dict(kop="Schermwerking en toepassingen",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Waarom is er binnen een geladen holle geleider geen elektrisch veld?",
                  "Omdat de lading op de buitenkant zit en de velden binnenin elkaar opheffen.", 3),
                 ("open", "Noem drie situaties die als een kooi van Faraday werken.",
                  "Een auto met een metalen dak tijdens een onweer, een metalen kast rond gevoelige "
                  "elektronica, en het metalen rooster in de deur van een magnetron.", 3),
                 ("open", "Waarom werkt poedercoating met geladen poeder?",
                  "Het poeder wordt naar het tegengesteld geladen metaal getrokken, ook rond de hoeken, "
                  "zodat er bijna niets verloren gaat.", 3),
                 ("open", "In een elektrostatische luchtzuiveraar worden de stofdeeltjes eerst geladen. "
                          "Waarom?",
                  "Zo haalt een tegengesteld geladen plaat ze uit de lucht.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-elektromagnetisme-en-inductie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektromagnetisme en inductie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Magnetisme",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de drie ferromagnetische metalen", "ijzer, nikkel, cobalt"),
                          ("de kleine gebieden in zo'n stof", "weissgebieden"),
                          ("een stuk ijzer wordt bij een magneet zelf magnetisch", "influentie")],
                  None, WL),
                 ("open", "Je breekt een staafmagneet in twee. Wat heb je dan, en waarom kan je geen "
                          "losse noordpool maken?",
                  "Twee kleinere magneten met elk een noord- en een zuidpool. Het magnetisme komt van de "
                  "kringstroom en de spin van de elektronen, dus heeft elk stukje altijd twee polen.", 4),
                 ("waar", "Een magneet kan je demagnetiseren door hem sterk op te warmen.", True),
             ]),
        dict(kop="Veldlijnen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("tussen de benen van een hoefijzermagneet", "homogeen veld"),
                          ("rond een staafmagneet", "dipoolveld"),
                          ("rond een rechte stroomdraad", "cirkels")], None, WW),
                 ("kies", "Welke kant op loopt een veldlijn buiten een magneet?",
                  ["van noord naar zuid", "van zuid naar noord", "beide kanten"], 0),
                 ("waar", "Hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het veld daar is.",
                  True),
                 ("open", "De noordpool van een kompasnaald wijst naar het geografische noorden. Welke "
                          "magnetische pool van de aarde ligt daar dan, en waarom?",
                  "De magnetische zuidpool. Een noordpool wordt immers door een zuidpool aangetrokken.",
                  3),
             ]),
        dict(kop="Elektromagneten",
             opdracht="Schrijf sterker, zwakker of iets anders.",
             oefeningen=[
                 ("rij", [("meer stroom door de spoel", "sterker"),
                          ("meer windingen", "sterker"),
                          ("een ijzeren kern erin", "sterker")], None, W),
                 ("kort", "Wat gebeurt er als je de stroomzin omdraait?",
                  "de polen wisselen", WW),
                 ("kort", "Waarvoor gebruik je de rechterhandregel bij een spoel?",
                  "om de noordpool uit de stroomzin te bepalen", WL),
                 ("open", "Noem drie toestellen met een elektromagneet, en zeg wat het voordeel van een "
                          "elektromagneet is.",
                  "Een elektrische deurbel, een schrootkraan en een relais. Het voordeel is dat je hem "
                  "kan uitzetten: hij werkt enkel zolang er stroom door loopt.", 4),
             ]),
        dict(kop="Laplace en Lorentz",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("kracht op een stroomdraad in een veld", "Laplacekracht"),
                          ("kracht op een bewegende lading", "Lorentzkracht")], None, WW),
                 ("waar", "Een lading die stilstaat in een magnetisch veld, ondervindt geen magnetische "
                          "kracht.", True),
                 ("open", "Een draad met stroom in een magnetisch veld krijgt een kracht. Wat gebeurt er "
                          "als je de stroomzin omdraait, en waarop berust een motor dus?",
                  "De kracht wijst de andere kant op. Een motor blijft draaien doordat de stroomzin op "
                  "het juiste moment omgekeerd wordt.", 4),
                 ("open", "Waarvoor gebruikt een massaspectrometer het magnetisch veld?",
                  "Om geladen deeltjes af te buigen volgens hun massa: zwaardere deeltjes buigen minder "
                  "af.", 3),
             ]),
        dict(kop="Inductie",
             opdracht="Schrijf groter, kleiner of niets.",
             oefeningen=[
                 ("rij", [("de magneet sneller in de spoel duwen", "groter"),
                          ("meer windingen op de spoel", "groter"),
                          ("de magneet stil in de spoel laten liggen", "niets")],
                  "Wat doet de inductiespanning?", W),
                 ("kort", "Hoe heet de grootheid die zegt hoeveel veld door een winding gaat?",
                  "de magnetische flux", WL),
                 ("open", "Waarvan hangt de magnetische flux door een winding af? Noem drie dingen.",
                  "Van de sterkte van het magnetisch veld, van de oppervlakte van de winding, en van de "
                  "hoek tussen het veld en de normaal op de winding.", 3),
                 ("open", "Formuleer de wet van Lenz, en zeg wat er verandert als je de magneet uit de "
                          "spoel trekt in plaats van erin duwt.",
                  "De inductiestroom werkt de verandering van de flux tegen. Trek je de magneet eruit, "
                  "dan loopt de inductiestroom in de omgekeerde zin.", 4),
             ]),
        dict(kop="Wervelstromen",
             opdracht="Leg uit in volledige zinnen.",
             oefeningen=[
                 ("open", "Een magneet valt door een koperen buis veel trager dan verwacht. Waarom?",
                  "De veranderende flux wekt wervelstromen in het koper op. Die maken volgens de wet van "
                  "Lenz een veld dat de val tegenwerkt.", 4),
                 ("open", "Hoe warmt een inductiekookplaat een pan op, en waarom blijft de plaat zelf "
                          "koud?",
                  "Door wervelstromen in de bodem van de pan op te wekken. De warmte ontstaat in de pan, "
                  "niet in de plaat; die wordt alleen warm van wat de pan teruggeeft.", 4),
                 ("waar", "Een elektromagnetische rem heeft remblokken nodig die bij elke remming "
                          "verslijten.", False),
                 ("open", "Noem drie toestellen die op elektromagnetische inductie werken.",
                  "Een dynamo op een fiets, een elektrische gitaar en een draadloze oplader.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kracht-en-beweging-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kracht en beweging",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke beweging?",
             opdracht="Schrijf ERB, EVRB of ECB.",
             oefeningen=[
                 ("rij", [(r"een auto aan \(50\) km per uur op een rechte weg", "ERB"),
                          ("een steen die van een toren valt", "EVRB"),
                          ("een kind op een draaimolen aan vaste snelheid", "ECB")], None, W),
                 ("rij", [("een trein die gelijkmatig afremt", "EVRB"),
                          ("een stip op een draaiende grammofoonplaat", "ECB"),
                          ("een lift die met vaste snelheid stijgt", "ERB")], None, W),
             ]),
        dict(kop="Grafieken",
             opdracht="Schrijf welke beweging erbij hoort.",
             oefeningen=[
                 ("rij", [("x(t) is een rechte schuine lijn", "ERB"),
                          ("x(t) is een parabool", "EVRB"),
                          ("v(t) is een horizontale lijn", "ERB")], None, W),
                 ("rij", [("v(t) is een rechte die stijgt", "versneld"),
                          ("v(t) is een rechte die daalt", "vertraagd")], None, W),
                 ("kort", "Wat lees je af uit de steilheid van een x(t)-grafiek?",
                  "de snelheid", WW),
                 ("open", "Waarom is er bij een eenparig cirkelvormige beweging toch een versnelling, "
                          "ook al verandert de snelheid niet van grootte?",
                  "Omdat de richting van de snelheid voortdurend verandert, en dat is ook een "
                  "verandering van de snelheidsvector. Die versnelling wijst naar het middelpunt van de "
                  "cirkel.", 4),
             ]),
        dict(kop=r"Rekenen met \(F = m \cdot a\)",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("rij", [(r"\(m = 4\) kg, \(F = 12\) N", r"\(3\) m/s²"), (r"\(m = 2\) kg, \(F = 10\) N", r"\(5\) m/s²"),
                          (r"\(m = 5\) kg, \(F = 20\) N", r"\(4\) m/s²")], "Hoe groot is a?", W),
                 ("rij", [(r"\(m = 3\) kg, \(a = 2\) m/s²", r"\(6\) N"), (r"\(m = 0{,}5\) kg, \(a = 8\) m/s²", r"\(4\) N"),
                          (r"\(F = 18\) N, \(a = 3\) m/s²", r"\(6\) kg")], None, W),
                 ("open", "Een vrachtwagen en een auto krijgen dezelfde kracht. Waarom versnelt de "
                          "vrachtwagen minder?",
                  r"Zijn massa is groter, en in \(F = m \cdot a\) zijn massa en versnelling omgekeerd verbonden: bij "
                  "dezelfde kracht geeft een grotere massa een kleinere versnelling.", 4),
                 ("waar", "Verdubbel je de resulterende kracht, dan verdubbelt de versnelling.", True),
             ]),
        dict(kop="De drie wetten",
             opdracht="Schrijf eerste, tweede of derde.",
             oefeningen=[
                 ("rij", [("een bus remt en de passagiers vallen naar voren", "eerste"),
                          ("uit kracht en massa de versnelling berekenen", "tweede"),
                          ("een raket komt vooruit", "derde")], "Welke wet?", W),
                 ("rij", [("de traagheidswet", "eerste"),
                          ("de actie-reactiewet", "derde")], None, W),
                 ("open", "Noem de drie dingen die over actie en reactie gelden, en zeg waarom ze elkaar "
                          "niet opheffen.",
                  "De twee krachten zijn even groot, ze hebben een tegengestelde zin, en ze werken op "
                  "verschillende lichamen. Precies dat laatste is waarom ze elkaar niet opheffen.", 4),
                 ("open", "Iemand zegt: een raket komt vooruit omdat de gassen tegen de lucht achter hem "
                          "duwen. Verbeter die uitleg.",
                  "Dan zou een raket in het luchtledige niet werken, en hij werkt er juist beter. Het is "
                  "de actie-reactiewet: de raket duwt de gassen naar achteren, de gassen duwen de raket "
                  "naar voren.", 4),
             ]),
        dict(kop="Krachten benoemen",
             opdracht="Schrijf de naam van de kracht.",
             oefeningen=[
                 ("rij", [("een oppervlak duwt loodrecht op een voorwerp", "normaalkracht"),
                          ("wijst tegen de beweging in bij schuiven", "wrijvingskracht"),
                          ("de aarde trekt alles naar beneden", "zwaartekracht")], None, WW),
                 ("waar", "Een boek dat stil op een tafel ligt, ondervindt geen enkele kracht.", False),
                 ("open", "Leg uit waarom dat boek dan toch blijft liggen.",
                  "Er werken wel krachten: de zwaartekracht naar beneden en de normaalkracht naar boven. "
                  "Ze zijn even groot en heffen elkaar op, dus is de resulterende kracht nul. Nul "
                  "resulterende kracht is niet nul kracht.", 4),
                 ("kort", "Wat doe je in een oefening met een kracht die schuin werkt?",
                  "ze in componenten ontbinden", WL),
                 ("kort", "Hoe bepaal je de resulterende kracht op een lichaam?",
                  "alle krachtvectoren samentellen", WL),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-trillingen-golven-en-geluid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Trillingen, golven en geluid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Trillingen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de grootste uitwijking", "amplitude"),
                          ("de tijd van één trilling", "periode"),
                          ("het aantal trillingen per seconde", "frequentie")], None, WW),
                 ("rij", [(r"periode \(0{,}5\) s", r"\(2\) Hz"), (r"periode \(0{,}25\) s", r"\(4\) Hz"),
                          (r"periode \(2\) s", r"\(0{,}5\) Hz")], "Welke frequentie?", W),
                 ("waar", "Een grotere amplitude betekent altijd ook een grotere frequentie.", False),
                 ("open", "Wat lees je af van de y(t)-grafiek van een trilling? Noem drie dingen.",
                  "De amplitude, de periode en de evenwichtslijn.", 2),
             ]),
        dict(kop="Resonantie",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet de frequentie waarmee een voorwerp vanzelf het liefst trilt?",
                  "de eigenfrequentie", WL),
                 ("open", "Wanneer treedt resonantie op, en waarom lopen de uitwijkingen dan op?",
                  "Als de uitwendige kracht de eigenfrequentie treft. Dan wordt elke duw op het juiste "
                  "moment gegeven, en zo bouwt de uitwijking zich op.", 4),
                 ("open", "Noem drie voorbeelden van resonantie.",
                  "Een schommel die hoger komt door op het juiste ritme te duwen, een glas dat barst bij "
                  "één bepaalde zangtoon, en een brug die schudt door marcherende voeten erop.", 3),
             ]),
        dict(kop="Golven",
             opdracht="Vul aan en reken.",
             oefeningen=[
                 ("rij", [(r"golflengte \(2\) m, frequentie \(5\) Hz", r"\(10\) m/s"),
                          (r"golflengte \(0{,}5\) m, frequentie \(8\) Hz", r"\(4\) m/s"),
                          (r"golflengte \(3\) m, frequentie \(2\) Hz", r"\(6\) m/s")], "Hoe snel?", W),
                 ("rij", [("geluid in lucht", "longitudinaal"),
                          ("een golf in een gespannen touw", "transversaal"),
                          ("een elektromagnetische golf", "transversaal")], None, WW),
                 ("waar", "De deeltjes van een golf verhuizen met de golf mee naar het einde.", False),
                 ("open", "Een golf transporteert energie maar geen materie. Leg dat uit met het "
                          "publiek in een stadion.",
                  "De mensen blijven op hun plaats en gaan alleen recht en weer zitten. Wat door het "
                  "stadion reist, is de beweging, niet de mensen. Zo trillen de deeltjes van een golf op "
                  "hun plaats en geven ze de beweging door.", 4),
                 ("open", "Waarom kan geluid zich niet door het luchtloze heelal voortplanten, en licht "
                          "wel?",
                  "Geluid is een mechanische golf en heeft een middenstof nodig om door te geven. Een "
                  "elektromagnetische golf zoals licht heeft die niet nodig.", 4),
             ]),
        dict(kop="Geluid",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de toonhoogte", "de frequentie"),
                          ("de luidheid", "de amplitude"),
                          ("de klankkleur", "de vorm van het patroon")],
                  "Waarvan hangt het af?", WL),
                 ("kort", "Welke frequenties kan een mens normaal horen?",
                  r"van \(20\) tot \(20\,000\) Hz", WW),
                 ("waar", "Infrasoon geluid heeft een hogere frequentie dan wat wij kunnen horen.",
                  False),
                 ("kort", "In welke middenstof gaat geluid het snelst?", "in een vaste stof", WW),
                 ("open", "Je hoort een lage, zachte toon. Wat weet je over de golf?",
                  "Dat ze een lage frequentie en een kleine amplitude heeft.", 2),
             ]),
        dict(kop="De decibelschaal",
             opdracht="Reken en antwoord.",
             oefeningen=[
                 ("rij", [("twee keer zo ver van de bron", r"ongeveer \(6\) dB minder"),
                          ("de intensiteit twee keer groter", r"ongeveer \(3\) dB meer")], None, WL),
                 ("rij", [("de gehoordrempel", r"\(0\) dB"), ("gehoorbescherming nodig vanaf", r"\(80\) dB"),
                          ("de pijndrempel", r"\(120\) dB")], None, W),
                 ("waar", "Twee keer zoveel geluidsintensiteit betekent twee keer zoveel decibel.",
                  False),
                 ("open", "Waar in het oor ontstaat blijvende gehoorschade, en waarom is die blijvend?",
                  "In het binnenoor, bij de haarcellen. Die groeien niet terug, dus is de schade "
                  "definitief.", 3),
                 ("open", "Noem drie manieren om je gehoor op een fuif te beschermen.",
                  "Oordopjes of een gehoorkap dragen, verder van de geluidsbron gaan staan, en de "
                  "blootstelling in tijd beperken.", 3),
             ]),
        dict(kop="Toepassingen met geluid",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Hoe heet het terugkaatsen van geluid tegen een wand?", "een echo", WW),
                 ("open", "Noem drie toepassingen die met geluidsgolven werken.",
                  "Echografie, sonar op een schip en echolocatie bij een vleermuis.", 2),
                 ("open", "Hoe werkt een echografie, en waarom mag ze bij een zwangerschap?",
                  "Ze stuurt ultrasoon geluid in het lichaam en meet wat er tegen de grens tussen "
                  "weefsels terugkaatst; uit de tijd berekent het toestel de diepte. Er komt geen "
                  "straling aan te pas, en net daarom mag ze.", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-elektromagnetisch-spectrum-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het elektromagnetisch spectrum",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het spectrum op een rij",
             opdracht="Zet in de juiste orde en vul aan.",
             oefeningen=[
                 ("open", "Zet van lage naar hoge frequentie: gamma · infrarood · microgolven · "
                          "radio · röntgen · ultraviolet · zichtbaar licht.",
                  "Radio, microgolven, infrarood, zichtbaar licht, ultraviolet, röntgen, gamma.", 2),
                 ("rij", [("de grootste golflengte", "radiogolven"),
                          ("de hoogste energie", "gammastraling"),
                          ("het enige dat we zien", "zichtbaar licht")], None, WW),
                 ("waar", "Gammastraling gaat in vacuüm sneller dan radiogolven.", False),
                 ("open", "Over een golf met een hoge frequentie: wat weet je dan over haar golflengte "
                          "en haar energie?",
                  "Haar golflengte is klein en haar energie is groot. Ze zit aan de kant van röntgen en "
                  "gamma.", 3),
             ]),
        dict(kop="Ioniserend of niet?",
             opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("gammastraling", "ja"), ("radiogolven van een gsm", "nee"),
                          ("röntgenstraling", "ja")], None, W),
                 ("rij", [("hoogenergetische uv", "ja"), ("infrarood", "nee"),
                          ("microgolven", "nee")], None, W),
                 ("open", "Waarom is uv-straling gevaarlijker voor je huid dan zichtbaar licht?",
                  "Uv heeft meer energie per golf en kan daardoor in cellen schade aanrichten, tot in het "
                  "DNA.", 3),
                 ("waar", "Elke soort elektromagnetische straling is schadelijk voor de mens.", False),
             ]),
        dict(kop="Straling en materie",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Welke drie dingen kunnen er gebeuren als straling op materie valt?",
                  "Absorberen, doorlaten of weerkaatsen.", 2),
                 ("open", "Waarom is gras groen?",
                  "Het weerkaatst het groene licht en absorbeert de andere kleuren. Wat je ziet, is dus "
                  "wat het niet opneemt.", 3),
                 ("open", "Waarom zijn de botten op een röntgenfoto wit?",
                  "Omdat ze meer straling absorberen dan het zachte weefsel, dus komt er achter het bot "
                  "minder straling op de plaat.", 3),
                 ("kort", "Hoe heet het verschijnsel waarbij straling door een stof heen gaat?",
                  "transmissie", WW),
             ]),
        dict(kop="Welke straling gebruikt dit?",
             opdracht="Schrijf de straling.",
             oefeningen=[
                 ("rij", [("een afstandsbediening", "infrarood"),
                          ("een bagagescanner", "röntgen"),
                          ("een wifinetwerk", "radiogolven")], None, WW),
                 ("rij", [("een valsgelddetector", "ultraviolet"),
                          ("een warmtebeeldcamera", "infrarood"),
                          ("voedsel steriliseren", "gamma")], None, WW),
                 ("rij", [("een magnetron", "microgolven"),
                          ("radiotherapie", "gamma"),
                          ("desinfectie van water", "ultraviolet")], None, WW),
                 ("waar", "Een blacklight werkt met infraroodstraling.", False),
             ]),
        dict(kop="Kiezen en verantwoorden",
             opdracht="Kies en leg uit.",
             oefeningen=[
                 ("open", "Een straling is niet zichtbaar, heeft een lange golflengte en is niet "
                          "ioniserend. Welke kan dat zijn?",
                  "Microgolven, of radiogolven of infrarood. Alle drie zitten aan de kant van de lange "
                  "golven en hebben te weinig energie om te ioniseren.", 3),
                 ("open", "In een fabriek wil men de dikte van een metalen plaat meten met straling. "
                          "Welke straling is daarvoor logisch, en waarom niet licht?",
                  "Straling die diep doordringt, zoals gamma. Licht zou al aan de oppervlakte blijven en "
                  "zegt niets over de dikte.", 4),
                 ("open", "Een toestel doodt met onzichtbare straling bacteriën in een waterleiding. "
                          "Welke straling is dat?",
                  "Ultraviolette straling.", 2),
                 ("open", "Waarom houdt het metalen rooster in de deur van een magnetron de microgolven "
                          "binnen?",
                  "Het werkt als een kooi van Faraday: de golven raken er niet door.", 3),
             ]),
        dict(kop="Bescherming",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Waarmee bescherm je je tegen röntgen- en gammastraling?",
                  "lood of dik beton", WW),
                 ("open", "Noem de drie maatregelen bij bescherming tegen hoogenergetische straling.",
                  "Een loodschort dragen, afstand houden van de bron, en de tijd bij de bron zo kort "
                  "mogelijk houden. Afscherming, afstand en tijd.", 3),
                 ("waar", "Zonnecrème en een zonnebril met uv-filter beschermen tegen ultraviolette "
                          "straling.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-kernfysica-en-radioactiviteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kernfysica en radioactiviteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De bouw van een kern",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(A = 23\), \(Z = 11\)", r"\(12\) neutronen"), (r"\(A = 40\), \(Z = 19\)", r"\(21\) neutronen"),
                          (r"\(A = 14\), \(Z = 6\)", r"\(8\) neutronen")], "Hoeveel neutronen?", WW),
                 ("rij", [(r"\(A = 12\), \(Z = 6\)", r"\(6\) protonen"), (r"\(Z = 92\), \(N = 146\)", r"\(A = 238\)"),
                          (r"\(A = 4\), \(Z = 2\)", r"\(2\) neutronen")], None, WW),
                 ("kort", "Hoe noemt men de protonen en de neutronen samen?", "nucleonen", WW),
                 ("open", "Wat hebben twee isotopen van hetzelfde element gemeen, en waarin "
                          "verschillen ze?",
                  "Ze hebben hetzelfde aantal protonen, dus hetzelfde atoomnummer. Ze verschillen in het "
                  "aantal neutronen, dus in massagetal.", 3),
             ]),
        dict(kop="Stabiel of niet",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Welke twee krachten strijden met elkaar in een atoomkern?",
                  "De sterke kernkracht, die alle nucleonen samentrekt maar enkel over heel korte "
                  "afstand werkt, en de afstoting van de protonen onderling, die verder reikt.", 3),
                 ("waar", "Een zware stabiele kern heeft meer protonen dan neutronen.", False),
                 ("open", "Waarom heeft een zware stabiele kern juist meer neutronen dan protonen?",
                  "Neutronen verdunnen de afstoting tussen de protonen zonder er zelf aan bij te dragen, "
                  "en helpen tegelijk de kernkracht.", 3),
                 ("open", "Een kern ligt onder de stabiliteitsband en heeft te veel neutronen. Hoe zal "
                          "ze vervallen, en waarom helpt dat?",
                  "Via bètaverval, want zo wordt een neutron een proton. De verhouding neutronen op "
                  "protonen komt daardoor dichter bij de band.", 4),
                 ("waar", "Een stabiele kern vervalt na verloop van tijd ook.", False),
             ]),
        dict(kop="Rekenen met halveringstijd",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("rij", [(r"\(800\) kernen, \(T = 5\) jaar, na \(15\) jaar", r"\(100\)"),
                          (r"\(640\) kernen, \(T = 2\) uur, na \(6\) uur", r"\(80\)"),
                          (r"\(1000\) kernen, na \(2\) halveringstijden", r"\(250\)")], "Hoeveel blijft er over?",
                  WW),
                 ("kort", "Na hoeveel halveringstijden blijft er een achtste over?", "drie", "90px"),
                 ("open", "Twee stalen hebben dezelfde hoeveelheid stof. Het ene heeft een korte "
                          "halveringstijd, het andere een lange. Welk staal heeft de hoogste activiteit, "
                          "en waarom?",
                  "Dat met de korte halveringstijd: dezelfde kernen vervallen daar in minder tijd, dus "
                  "vervallen er meer kernen per seconde.", 4),
                 ("open", "Hoe haal je de halveringstijd uit een N(t)-grafiek, en wat is het bijzondere "
                          "aan die werkwijze?",
                  "Je zoekt wanneer het aantal tot de helft gezakt is en leest dat op de tijdas af. Het "
                  "bijzondere is dat je van elk punt van de kromme mag vertrekken: de halveringstijd is "
                  "overal dezelfde.", 4),
             ]),
        dict(kop="Fusie, splijting en de centrale",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("twee lichte kernen smelten samen", "kernfusie"),
                          ("een zware kern valt uiteen", "kernsplijting"),
                          ("de splijtstof van een centrale", "uraan")], None, WW),
                 ("open", "Bij fusie van lichte kernen én bij splijting van zware kernen komt energie "
                          "vrij. Dat lijkt tegenstrijdig. Leg uit.",
                  "Beide bewegingen gaan naar het stabielere midden van de nuclidenkaart toe, waar de "
                  "specifieke rustenergie per nucleon het laagst is. Het massaverschil komt als energie "
                  "vrij volgens E = mc².", 4),
                 ("kort", "Waarvoor dienen de regelstaven in een kernreactor?",
                  "neutronen wegvangen en zo de kettingreactie regelen", WL),
                 ("open", "Volgens welke twee kenmerken wordt radioactief afval ingedeeld, en wat is "
                          "categorie A?",
                  "Volgens de intensiteit en de duur van de straling. Categorie A is kortlevend laag- en "
                  "middelactief afval.", 3),
             ]),
        dict(kop="Alfa, bèta of gamma?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Straling", "Wat ze is", "Doordringend vermogen"],
                  [["alfa", None, None], ["bèta", None, None], ["gamma", None, None]],
                  "Alfa is een heliumkern met twee protonen en twee neutronen; een blad papier houdt ze "
                  "al tegen. Bèta is een elektron dat de kern verlaat; een plaatje aluminium stopt ze. "
                  "Gamma is een elektromagnetische golf; lood of dik beton is nodig.", WW),
                 ("rij", [("alfaverval", r"A min \(4\), Z min \(2\)"),
                          ("bètaverval", r"A gelijk, Z plus \(1\)")], None, WL),
                 ("open", "Alfastraling raakt niet door je huid, en toch is ze gevaarlijk. Hoe zit dat?",
                  "Ze heeft een klein doordringend vermogen maar een groot ioniserend vermogen. Na "
                  "inslikken of inademen staat er geen huid meer tussen, en dan geeft ze al haar energie "
                  "af in een klein stukje weefsel.", 4),
                 ("waar", "Gammastraling buigt in een magnetisch veld even sterk af als bètastraling.",
                  False),
                 ("open", "Waarom buigt gammastraling niet af in een magnetisch veld en bètastraling "
                          "wel, heel sterk zelfs?",
                  "Gammastraling heeft geen lading, dus werkt er geen magnetische kracht op. Bètastraling "
                  "is geladen en bovendien heel licht, dus buigt ze sterk af.", 4),
             ]),
        dict(kop="Dosis en toepassingen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen bestraling en besmetting?",
                  "Bij bestraling sta je enkel in de straling en blijft er niets achter. Bij besmetting "
                  "komt de radioactieve stof op of in je lichaam en blijft ze doorstralen tot ze weg of "
                  "vervallen is.", 4),
                 ("rij", [("de geabsorbeerde dosis", "gray"),
                          ("de equivalente en effectieve dosis", "sievert")], None, W),
                 ("open", "Waarom heeft alfastraling een veel hogere stralingsweegfactor dan bèta- of "
                          "gammastraling?",
                  "Omdat ze al haar energie in een heel klein stukje weefsel afgeeft, en daar dus veel "
                  "meer schade aanricht per gray.", 3),
                 ("open", "Noem drie toepassingen van ioniserende straling.",
                  r"Radiotherapie tegen kanker, de koolstof-\(14\)-methode om ouderdom te bepalen, en een "
                  "PET-scan met een radioactieve tracer.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-en-duurzaam-werken-grootheden-en-eenheden-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig en duurzaam werken, grootheden en eenheden",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het etiket lezen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("zegt welk gevaar de stof oplevert", "H-zin"),
                          ("zegt hoe je veilig werkt", "P-zin"),
                          ("zegt waarom de stof gevaarlijk is", "pictogram")], None, WW),
                 ("open", "Het etiket waarschuwt voor gevaar voor de huid. Noem drie dingen die je "
                          "doet.",
                  "Handschoenen dragen, een veiligheidsbril dragen, en de P-zinnen van het etiket "
                  "volgen.", 3),
             ]),
        dict(kop="Veilig en duurzaam in het labo",
             opdracht="Schrijf juist of fout, en verbeter de foute.",
             oefeningen=[
                 ("waar", "Een gemorst chemisch product ruim je beter onmiddellijk op.", True),
                 ("waar", "Afval van een chemisch product mag gewoon in de gootsteen.", False),
                 ("open", "Hoe ruim je glasscherven in een labo veilig op?",
                  "Met een borstel en een blik, in het vat voor glas. Nooit met je handen.", 2),
                 ("open", "Noem drie werkwijzen die bij veilig en duurzaam werken horen.",
                  "Zuinig omgaan met chemische stoffen, meetinstrumenten uitzetten als je niet meet, en "
                  "glaswerk na gebruik schoonmaken.", 3),
             ]),
        dict(kop="Meten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een kracht", "dynamometer"), ("een spanning", "voltmeter"),
                          ("een geluidsniveau", "decibelmeter")], "Welk instrument?", WW),
                 ("rij", [("de kleinste en grootste meetbare waarde", "meetbereik"),
                          ("de kleinste verandering die je nog ziet", "nauwkeurigheid")], None, WW),
                 ("open", r"Je moet ongeveer \(2\) gram wegen, op een tienden van een gram nauwkeurig. Welke "
                          "balans kies je, en waarom niet gewoon de duurste?",
                  r"Een balans die tot op \(0{,}01\) gram weegt, dus één stap fijner dan wat je nodig hebt. Een "
                  "duurder instrument is niet altijd het beste: het moet passen bij wat je meet.", 4),
                 ("open", "Waarom lees je een vloeistofniveau in een maatcilinder op ooghoogte af?",
                  "Om een fout door de kijkhoek te vermijden.", 2),
                 ("open", r"Je meet met een lintmeter in centimeters en schrijft \(12{,}3456\) cm op. Wat is "
                          "daar fout aan?",
                  "Je schrijft meer cijfers op dan je kan meten. Een lintmeter geeft geen tienduizendsten "
                  "van een centimeter.", 3),
             ]),
        dict(kop="Omzetten",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [(r"\(2{,}5\) km", r"\(2500\) m"), (r"\(0{,}25\) ms", r"\(0{,}00025\) s"),
                          (r"\(3\) mg", r"\(0{,}003\) g")], None, WW),
                 ("rij", [(r"\(4\) MW", r"\(4\,000\,000\) W"), (r"\(250\) nm", r"\(0{,}00000025\) m"),
                          (r"\(12\) µm", r"\(0{,}000012\) m")], None, WW),
                 ("rij", [("mega", "een miljoen"), ("micro", "een miljoenste"),
                          ("nano", "een miljardste")], "Welke factor?", WW),
                 ("kort", "Wat is de SI-eenheid van massa?", "de kilogram", WW),
             ]),
        dict(kop="Wetenschappelijke notatie en beduidende cijfers",
             opdracht="Schrijf om en antwoord.",
             oefeningen=[
                 ("rij", [(r"\(0{,}00042\) m", r"\(4{,}2 \cdot 10^{-4}\) m"), (r"\(35\,000\) m", r"\(3{,}5 \cdot 10^{4}\) m"),
                          (r"\(0{,}0071\) s", r"\(7{,}1 \cdot 10^{-3}\) s")], None, WW),
                 ("open", r"Je meet \(3{,}0\) cm en \(4{,}00\) cm en telt die op. Met hoeveel cijfers na de komma "
                          "schrijf je het resultaat, en waarom?",
                  r"Met één cijfer na de komma, dus \(7{,}0\) cm. De minst nauwkeurige meting bepaalt het "
                  "antwoord.", 3),
                 ("waar", "Een rekenmachine die acht cijfers na de komma toont, maakt je meting "
                          "nauwkeuriger.", False),
                 ("open", "Waarom is een schatting vooraf niet overbodig als je met een rekenmachine "
                          "werkt?",
                  "Een rekenmachine rekent ook een tikfout keurig uit. Een schatting is je enige "
                  "bescherming tegen een antwoord dat er duizend keer naast zit.", 3),
             ]),
        dict(kop="Verbanden en formules",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een rechte door de oorsprong", "recht evenredig"),
                          ("een parabool", "kwadratisch"),
                          ("hun product blijft gelijk", "omgekeerd evenredig")], None, WW),
                 ("open", "Wat is het verschil tussen recht evenredig en lineair?",
                  "Bij recht evenredig gaat de rechte door de oorsprong. Bij lineair is de grafiek ook "
                  "een rechte, maar ze hoeft niet door de oorsprong te gaan.", 3),
                 ("rij", [(r"\(F = m \cdot a\), zoek m", r"\(m = F / a\)"), (r"\(F = m \cdot a\), zoek a", r"\(a = F / m\)"),
                          (r"\(v = s / t\), zoek t", r"\(t = s / v\)")], None, WW),
                 ("open", "Noem drie modellen waarmee je een verband kan weergeven.",
                  "Een grafiek, een tabel en een formule.", 2),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-onderzoeksvaardigheden-en-ontwerpen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Onderzoeksvaardigheden en ontwerpen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De stappen op een rij",
             opdracht="Zet in de juiste orde en vul aan.",
             oefeningen=[
                 ("open", "Zet in de juiste orde: data verzamelen · een conclusie schrijven · het "
                          "probleem definiëren · een hypothese opstellen · een onderzoeksplan maken.",
                  "Het probleem definiëren, een hypothese opstellen, een onderzoeksplan maken, data "
                  "verzamelen, een conclusie schrijven.", 3),
                 ("open", "Noem drie dingen die in een onderzoeksplan staan.",
                  "Welk materiaal je nodig hebt, welke stappen je in welke orde zet, en wat je gaat "
                  "meten en met welk instrument.", 3),
                 ("waar", "Een onderzoeksvraag stel je pas op nadat je de metingen gedaan hebt.", False),
             ]),
        dict(kop="Een goede onderzoeksvraag",
             opdracht="Schrijf goed of niet goed, en verbeter.",
             oefeningen=[
                 ("rij", [("Hoe hangt de valtijd van een bal af van zijn hoogte?", "goed"),
                          ("Is water lekker?", "niet goed"),
                          ("Hoe werkt een plant?", "niet goed")], None, W),
                 ("open", r"Herschrijf \"Groeien planten beter met muziek?\" tot een goede "
                          "onderzoeksvraag.",
                  "Bijvoorbeeld: hoe hangt de groei in centimeter van een tuinkersplantje na twee weken "
                  "af van het aantal uren muziek per dag? Nu staan er een meetbare uitkomst en een "
                  "grootheid in die je zelf verandert.", 4),
                 ("open", "Je hypothese wordt door het onderzoek weerlegd. Waarom is je werk dan niet "
                          "mislukt?",
                  "Je weet daarna iets wat je eerst niet wist. Een weerlegde hypothese is een resultaat, "
                  "en dat is precies de bedoeling van onderzoek.", 3),
             ]),
        dict(kop="Variabelen aanwijzen",
             opdracht="Schrijf wat je verandert, wat je meet en wat je gelijk houdt.",
             oefeningen=[
                 ("open", "Je onderzoekt of plantengroei van de hoeveelheid licht afhangt.",
                  "Je verandert de hoeveelheid licht, je meet de groei, en je houdt de soort plant, de "
                  "grond en het water gelijk.", 4),
                 ("open", "Je onderzoekt of een bal verder rolt op tapijt of op tegels.",
                  "Je verandert de ondergrond, je meet de afgelegde afstand, en je houdt de bal, de "
                  "hoogte van de helling en de manier van loslaten gelijk.", 4),
                 ("kort", "Hoe heet de proef zonder de behandeling, waarmee je vergelijkt?",
                  "de controleproef", WL),
                 ("open", "Waarom herhaal je een meting meerdere keren?",
                  "Om toevallige meetfouten te zien en uit te vlakken.", 2),
                 ("waar", "Een meting die niet bij je hypothese past, mag je weglaten uit je "
                          "resultaten.", False),
             ]),
        dict(kop="Van data naar besluit",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("open", "Je krijgt een tabel met meetgegevens en moet er een verband uit halen. Wat is "
                          "een goede eerste stap, en waarom?",
                  "De gegevens in een grafiek uitzetten. Een verband zie je veel sneller in een beeld dan "
                  "je het uit cijfers rekent.", 3),
                 ("open", "Twee grootheden stijgen samen in een rechte door de oorsprong. Wat besluit "
                          "je?",
                  "Dat ze recht evenredig met elkaar zijn.", 2),
                 ("open", "Noem de drie dingen waaraan een goede conclusie moet voldoen.",
                  "Ze antwoordt op de onderzoeksvraag, ze steunt op de verzamelde data, en ze zegt ook of "
                  "de hypothese klopte.", 3),
                 ("open", "Waarom hoort reflecteren over je methode bij het onderzoek, en waarom "
                          "communiceren?",
                  "Reflecteren laat je zien wat beter kon aan je opzet. Communiceren hoort erbij omdat "
                  "een resultaat dat niemand te weten komt, ook door niemand nagekeken kan worden.", 4),
             ]),
        dict(kop="Ontwerpen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("open", "Zet in de juiste orde: criteria opstellen · de oplossing evalueren en "
                          "bijsturen · het probleem definiëren · in deelproblemen splitsen.",
                  "Het probleem definiëren, criteria opstellen, in deelproblemen splitsen, de oplossing "
                  "evalueren en bijsturen.", 3),
                 ("open", "Noem drie vragen die je helpen om criteria op te stellen.",
                  "Hoe groot of hoe zwaar mag het worden? Hoeveel mag het kosten? Hoe veilig en hoe "
                  "duurzaam moet het zijn?", 3),
                 ("waar", "Het ontwerpproces stopt zodra je eerste versie klaar is.", False),
                 ("open", "Je ontwerpt een waterfilter voor een school. Eén criterium is dat hij "
                          "betaalbaar moet zijn, en je ontwerp valt te duur uit. Wat doe je?",
                  "Je stuurt het ontwerp bij met goedkoper materiaal, en je legt het daarna opnieuw naast "
                  "al je criteria.", 3),
                 ("open", "Je hebt twee ontwerpen die allebei werken. Hoe kies je?",
                  "Door ze naast je criteria te leggen en te vergelijken, op elk criterium apart.", 3),
             ]),
        dict(kop="STEM en de samenleving",
             opdracht="Beantwoord in volledige zinnen.",
             oefeningen=[
                 ("kort", "Waarvoor staan de letters STEM?",
                  "wetenschappen, techniek, engineering en wiskunde", WL),
                 ("open", "Een stad wil de luchtkwaliteit verbeteren. Welke STEM-kennis is daarbij "
                          "nuttig? Noem er drie.",
                  "Wetenschappelijke kennis over de stoffen in de lucht, technische kennis over "
                  "meettoestellen en filters, en wiskundige kennis om de metingen te verwerken.", 3),
                 ("open", "Welke disciplines waren er nodig om een vaccin tegen corona te ontwikkelen én "
                          "te verdelen?",
                  "Wetenschappelijke kennis om het vaccin te maken, technologische kennis om het koel te "
                  "houden, en wiskundige kennis om de verspreiding te volgen.", 3),
                 ("open", "Wetenschap en samenleving duwen elkaar vooruit. Geef voor elke richting een "
                          "voorbeeld.",
                  "De samenleving bepaalt mee waar onderzoek naar gaat: een pandemie zet duizenden "
                  "onderzoekers op vaccins. En een nieuwe techniek maakt nieuw onderzoek mogelijk: zonder "
                  "microscoop geen celbiologie.", 4),
                 ("open", "Wat is het verschil tussen onderzoeken en ontwerpen?",
                  "Onderzoeken antwoordt op een vraag, ontwerpen lost een probleem op.", 2),
             ]),
    ],
)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-de-cel-organellen-membranen-en-weefsels-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes organellen, elk met één taak. Een trucje: de naam zegt vaak al iets. Een "
                   "lysosoom lost op, een ribosoom bouwt eiwitten, een centrosoom staat in het "
                   "centrum bij de deling.",
            waarom=[
                "Let op het verschil tussen een ribosoom en een lysosoom: het eerste bouwt op, het "
                "tweede breekt af. Die twee namen lijken op elkaar en de taken zijn tegengesteld.",
                "Let op het kernlichaampje: dat maakt de ribosomen, dus het ligt in de kern terwijl "
                "de ribosomen zelf buiten de kern werken. En let op het glad ER: glad maakt vetten "
                "en ontgift, ruw maakt eiwitten omdat er ribosomen op zitten.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elk onderdeel af of het iets met licht of met stevigheid te maken "
                   "heeft. Dat zijn de plantentaken. Wat elke cel nodig heeft, hoort bij beide.",
            waarom=[
                "Let op het mitochondrion: ook een plantencel heeft er, want ook een plant doet aan "
                "celademhaling. Dat is een klassieke valstrik.",
                "Let op de amyloplast: die slaat zetmeel op, zoals in een aardappel, en hoort dus "
                "bij de plant. Het centrosoom hoort bij het dier, maar het celmembraan heeft elke "
                "cel.",
            ],
        ),
        dict(
            aanpak="Drie keer dezelfde gedachte: de bouw volgt de taak. Zeg bij elk antwoord welk "
                   "voordeel de vorm oplevert, niet enkel hoe ze eruitziet.",
            waarom=[
                "Noem dat er meer plaats komt voor hemoglobine. Zeggen dat ze geen kern heeft is de "
                "vaststelling, het voordeel is het antwoord.",
                "Noem het woord oppervlak: dat is wat een lange dunne vorm oplevert. Dezelfde "
                "gedachte komt in de vijfde reeks terug, maar dan omgekeerd.",
                "Noem zowel het licht als de chloroplasten. De plaats in het blad en de inhoud van "
                "de cel horen samen in dit antwoord.",
            ],
        ),
        dict(
            aanpak="Hou de drie bouwstenen van het membraan apart: de dubbellaag, de stevigheid en "
                   "de poorten. Bij de laatste vraag denk je aan osmose en aan wat de celwand doet.",
            waarom=[
                "Let op de transmembraaneiwitten: zonder die poorten raken grote of geladen stoffen "
                "niet door de vetlaag. Het membraan is dus geen zeef maar een deur met sleutels.",
                "Niet waar: semi-permeabel betekent half doorlaatbaar. Water gaat er vlot door, "
                "grote en geladen stoffen niet of enkel via een poort.",
                "Noem allebei: het water stroomt naar binnen door osmose, en de celwand houdt haar "
                "tegen. Een dierlijke cel zou in dezelfde proef wel openbarsten, en dat verschil "
                "mag je erbij zeggen.",
            ],
        ),
        dict(
            aanpak="Reken eerst, besluit daarna. Volume is zijde maal zijde maal zijde, oppervlakte "
                   "is zes keer één vlak. Deel dan de oppervlakte door het volume.",
            waarom=[
                None,
                "Let erop dat een kubus zes vlakken heeft: 2 maal 2 is 4 per vlak, en 6 keer 4 is "
                "24. Wie dat vergeet, komt op een vierde van het juiste getal.",
                "Let op wat er gebeurt: het volume gaat 8 keer omhoog, de oppervlakte maar 4 keer. "
                "Daarom zakt de verhouding van 3 naar 1,5. Dat is de reden dat grote organismen uit "
                "veel kleine cellen bestaan en niet uit enkele grote.",
            ],
        ),
        dict(
            aanpak="Hou de plantenweefsels en de dierlijke weefsels apart. Xyleem en floëem zijn "
                   "plant, epitheel en spier zijn dier.",
            waarom=[
                "Let op het verschil tussen xyleem en floëem: xyleem gaat omhoog met water, floëem "
                "verdeelt de suikers in alle richtingen. Een hulpje: de f van floëem en van "
                "fotosynthese, want het vervoert wat het blad maakt.",
                None,
                "Let erop dat de sluitcellen met twee werken: ze buigen samen open en samen dicht. "
                "Daarmee regelt het blad hoeveel water het verliest.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-fotosynthese-en-celademhaling-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="De twee vergelijkingen zijn elkaars spiegelbeeld. Leer er één goed, dan heb je "
                   "de andere er gratis bij: je leest ze eenvoudig van rechts naar links.",
            waarom=[
                "Let op de zes vooraan en de zes achteraan: zonder die coëfficiënten klopt de "
                "vergelijking niet. Tel de koolstof, de waterstof en de zuurstof links en rechts na.",
                "Let erop dat je bij de celademhaling ook de energie vermeldt. Dat is het hele punt "
                "van die reactie.",
                "Noem dat de producten van de ene de grondstoffen van de andere zijn. Dat is "
                "preciezer dan zeggen dat ze omgekeerd zijn.",
            ],
        ),
        dict(
            aanpak="Hou drie plaatsen apart: in de chloroplast, in het cytoplasma, en in het "
                   "mitochondrion. De glycolyse is de enige van de drie die buiten een organel "
                   "gebeurt.",
            waarom=[
                "Let op de donkerreactie: die gebeurt in het stroma, dus in de vloeistof van de "
                "chloroplast, en niet op het membraan. De lichtreacties hebben wel een membraan "
                "nodig, want daar zit de kleurstof in.",
                "Let erop dat de voorwaarde in de vraag staat: bij voldoende zuurstof. Zonder "
                "zuurstof blijft het pyrodruivenzuur in het cytoplasma en volgt er gisting.",
            ],
        ),
        dict(
            aanpak="De beweringen gaan over drie dingen: de namen van de reacties, hoeveel energie "
                   "elke stap levert, en wat een cel met ATP doet.",
            waarom=[
                "Niet waar, en de naam is misleidend: de donkerreactie heeft enkel geen licht nodig. "
                "Ze loopt juist het best in het licht, want daar komen haar bouwstoffen vandaan.",
                "Niet waar: de glycolyse levert maar een klein deel. Het grootste deel van de ATP "
                "komt uit de stappen in het mitochondrion, en dat verklaart waarom je zuurstof "
                "nodig hebt.",
                "Waar: een plant ademt dag en nacht. In het licht maakt ze meer zuurstof dan ze "
                "verbruikt, in het donker enkel verbruikt ze.",
                "Niet waar: ATP wordt gemaakt en bijna onmiddellijk weer gebruikt. Een cel legt geen "
                "voorraad aan; voor de lange termijn gebruikt ze vet en glycogeen.",
            ],
        ),
        dict(
            aanpak="Twee soorten gisting, elk met een eigen product en een eigen toepassing. Bij de "
                   "laatste vragen denk je telkens aan wat er met de glucose gebeurt.",
            waarom=[
                "Let erop dat beide vormen zonder zuurstof werken. Het verschil zit in het product: "
                "melkzuur bij de ene, ethanol en koolstofdioxide bij de andere. Dat gas is wat het "
                "deeg doet rijzen.",
                "Noem dat de glucose maar gedeeltelijk afgebroken wordt. Daar zit het antwoord: de "
                "energie blijft in het melkzuur of de ethanol achter.",
                "Noem de keten: te weinig zuurstof, dus melkzuur in plaats van de volledige "
                "afbraak. Enkel zeggen dat er melkzuur is, laat de oorzaak weg.",
            ],
        ),
        dict(
            aanpak="Bij een proef stel je altijd dezelfde vraag: wat verandert er, en wat hou je "
                   "gelijk? Het bedekte deel van het blad is de controle.",
            waarom=[
                "Noem dat je het zetmeel eerst wil laten verdwijnen. Zonder die stap kan je achteraf "
                "niet besluiten dat het zetmeel van de proef komt.",
                None,
                "Noem beide delen, het bedekte en het onbedekte. Een proef bewijst iets doordat je "
                "de twee met elkaar vergelijkt.",
            ],
        ),
        dict(
            aanpak="ATP werkt als een batterij: ze geeft een fosfaatgroep af en wordt ADP, en met "
                   "energie uit de voeding wordt ze weer opgeladen.",
            waarom=[
                None,
                "Let op de voorvoegsels: exo betekent naar buiten, dus energie komt vrij; endo "
                "betekent naar binnen, dus er is energie nodig. Dezelfde logica werkt bij exotherm "
                "en endotherm.",
                "Noem drie heel verschillende processen, zoals in het antwoord. Dat toont dat ATP "
                "de munt is waarmee de cel alles betaalt, van bewegen tot bouwen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bescherming-en-afweer-tegen-lichaamsvreemde-stoffen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist bij elke lijn: houdt het alles buiten (eerste), pakt het alles "
                   "aan wat binnen is (tweede), of werkt het tegen één bepaalde indringer (derde)?",
            waarom=[
                "Let op het verschil tussen de tweede en de derde lijn: een fagocyt eet alles wat "
                "lichaamsvreemd is, een antistof past op één antigeen. Algemeen is tweede, specifiek "
                "is derde.",
                "Let op koorts: dat hoort bij de tweede lijn, want het is een algemene reactie van "
                "het hele lichaam. Veel kiemen vermeerderen zich minder goed bij een hogere "
                "temperatuur.",
            ],
        ),
        dict(
            aanpak="Zes cellen, elk met één taak. Een hulpje bij de letters: B maakt antistoffen, T "
                   "stuurt aan of doodt zelf.",
            waarom=[
                "Let op de mestcel: zij geeft histamine af, en dat is wat bij een allergie voor de "
                "zwelling en de jeuk zorgt. Een antihistaminicum werkt juist daarop.",
                "Let op de dendritische cel: ze doodt zelf niets, ze toont. Zonder die stap komt de "
                "derde lijn niet op gang, en dat is precies wat de vijfde reeks laat zien.",
            ],
        ),
        dict(
            aanpak="Drie keer een paar woorden die op elkaar lijken. Zeg bij elk antwoord van beide "
                   "begrippen wat het is, niet enkel van het ene.",
            waarom=[
                "Let erop dat een antigeen een stof is en een pathogeen een organisme. Ook stuifmeel "
                "is een antigeen, en dat maakt niemand ziek door een infectie.",
                "Let erop dat een infectie nog geen ziekte is. Dat verschil verklaart waarom iemand "
                "een kiem kan doorgeven zonder zich ziek te voelen.",
                "Noem waar een antibioticum op aangrijpt, zoals de celwand. Zeggen dat het niet werkt "
                "tegen virussen is het besluit, de reden is het antwoord. En dit is ook waarom "
                "onnodig antibiotica nemen tot resistentie leidt.",
            ],
        ),
        dict(
            aanpak="Twee vragen per voorbeeld: maakt je lichaam de antistoffen zelf (actief) of krijg "
                   "je ze kant-en-klaar (passief), en gebeurt het van nature of door een ingreep?",
            waarom=[
                "Let op de borstvoeding en de serumtherapie: in beide gevallen krijg je antistoffen "
                "van iemand anders, dus passief. Het verschil zit enkel in natuurlijk of kunstmatig.",
                "Niet waar: bij passieve immunisatie maak je zelf geen geheugencellen. Je bent "
                "beschermd zolang die geleende antistoffen meegaan, en dat is enkele weken.",
                "Noem beide verschillen: geen geheugen, en de antistoffen verdwijnen. Daarom is "
                "serumtherapie een noodhulp na een beet of een prik, en geen bescherming voor later.",
            ],
        ),
        dict(
            aanpak="Volg de keten van buiten naar binnen: binnendringen, opeten, tonen, en dan de "
                   "antistoffen. De laatste twee vragen gaan over wat daarna overblijft.",
            waarom=[
                "Let erop dat de antigeenpresentatie tussen het opeten en de antistoffen staat. Het "
                "is de schakel tussen de tweede en de derde lijn: zonder tonen weet de B-lymfocyt "
                "niet welke antistof ze moet maken.",
                "Noem het afweergeheugen en noem dat de tweede reactie sneller en sterker is. De "
                "woorden primair en secundair horen er bij een vraag van dit niveau bij.",
                "Noem dat de kiem te weinig geschikte gastheren vindt. Dat is groepsimmuniteit, en "
                "het verklaart waarom een campagne ook baby's en zieke mensen beschermt die zelf "
                "geen vaccin kunnen krijgen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-voortplanting-zwangerschap-en-vruchtbaarheid-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Volg de weg van de zaadcel: vagina, baarmoederhals, baarmoeder, eileider. De "
                   "bevruchting gebeurt onderweg, niet aan het eindpunt.",
            waarom=[
                "Let erop dat de bevruchting in de eileider gebeurt en niet in de baarmoeder. De "
                "bevruchte eicel reist daarna nog enkele dagen voor ze zich innestelt.",
                "Let op het acrosoom: daar zitten de enzymen in die de laag rond de eicel openen. "
                "Zonder dat blaasje raakt een zaadcel niet binnen.",
                None,
                "Noem alle drie, zoals gevraagd. Elke barrière is ook een selectie: van de miljoenen "
                "zaadcellen raken er maar enkele honderden tot bij de eicel.",
                "Noem allebei: wat de reactie doet en wat er anders zou gebeuren. Het aantal "
                "chromosomen is hier de kern van het antwoord.",
            ],
        ),
        dict(
            aanpak="Vier stappen in de eerste week, en daarna de tweedeling van de cellen in twee "
                   "groepen: één voor het kind, één voor de placenta.",
            waarom=[
                "Let op de morula en de blastula: de morula is een volle bal cellen, de blastula "
                "heeft een holte. Dat verschil bepaalt de orde.",
                "Let op de trofoblast: daaruit groeit de placenta, en die maakt hCG. Daarom is een "
                "zwangerschapstest eigenlijk een test op een hormoon van de placenta in wording.",
                None,
                "Noem dat het geheel even groot blijft. Dat is wat klieving betekent: verdelen in "
                "plaats van groeien, en het past bij de verhouding oppervlakte op volume uit het "
                "hoofdstuk over de cel.",
            ],
        ),
        dict(
            aanpak="Eén grens om te onthouden: acht weken. Daarvoor worden de organen aangelegd, "
                   "daarna groeien en rijpen ze.",
            waarom=[
                "Let op het verschil tussen vormen en rijpen: het eerste is embryonaal, het tweede "
                "foetaal. De kiembladen horen bij de vroegste aanleg.",
                "Noem beide delen van het antwoord: de organen worden dan gevormd, en veel vrouwen "
                "weten in die weken nog niet dat ze zwanger zijn. Dat tweede is de reden waarom men "
                "aanraadt al bij een zwangerschapswens te stoppen met alcohol.",
                None,
            ],
        ),
        dict(
            aanpak="De placenta is een uitwisselingsplaats, geen vermenging. Hou dat vast, dan "
                   "volgen de antwoorden van deze reeks er bijna uit.",
            waarom=[
                "Noem alle drie de taken, zoals gevraagd, en vergeet de hormonen niet. Veel mensen "
                "denken enkel aan voeding en zuurstof.",
                "Niet waar: de twee bloedsomlopen blijven gescheiden en de stoffen gaan door de "
                "wanden heen. Daarom kan een kind een andere bloedgroep hebben dan zijn moeder.",
                "Noem dat ze geen muur is. Selectief betekent dat ze kiest, niet dat ze alles "
                "schadelijke tegenhoudt.",
                "Let erop dat het hier omgekeerd is dan je zou denken: de slagaders van de "
                "navelstreng vervoeren zuurstofarm bloed. Een slagader is namelijk een vat dat van "
                "het hart wegloopt, niet een vat met zuurstofrijk bloed.",
            ],
        ),
        dict(
            aanpak="Drie vragen over wat van buiten bij de vrucht raakt. Hou bij de tweede vast dat "
                   "er geen veilige hoeveelheid bestaat.",
            waarom=[
                None,
                "Noem dat er geen hoeveelheid is waarvan men weet dat ze veilig is. Dat is het "
                "verschil met veel andere stoffen, waar men een grens kan geven.",
                "Noem de toxoplasmose met naam. Beide adviezen komen van dezelfde parasiet, en dat "
                "verband is wat de vraag zoekt.",
            ],
        ),
        dict(
            aanpak="Hou bij anticonceptie twee vragen apart: hoe werkt het, en beschermt het tegen "
                   "soa? Enkel het condoom doet het tweede.",
            waarom=[
                "Let erop dat enkel het condoom tegen soa beschermt. Een pil regelt de hormonen en "
                "houdt geen enkele kiem tegen; dat is een punt dat vaak fout gaat.",
                "Noem dat er één zaadcel rechtstreeks in de eicel gebracht wordt. Bij gewone "
                "ivf moet een zaadcel zelf binnendringen, en dat is precies wat bij ICSI niet lukt.",
                "Niet waar: bij inseminatie wordt het sperma in de baarmoeder gebracht en gebeurt de "
                "bevruchting in het lichaam. Buiten het lichaam is ivf.",
                "Noem drie factoren, zoals gevraagd, en noem bij voorkeur dingen die je zelf in de "
                "hand hebt. Leeftijd speelt mee maar is geen keuze.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-dna-replicatie-en-celdelingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee paren om vast te houden: A hoort bij T, G hoort bij C. Schrijf de "
                   "complementaire streng letter per letter, dan vergeet je er geen.",
            waarom=[
                "Let erop dat je de letters in dezelfde orde opschrijft als de gegeven streng. Wie "
                "van achter naar voor begint, krijgt de juiste letters in de verkeerde volgorde.",
                "Let op het verschil: G en C houden elkaar met drie bruggen vast, A en T met twee. "
                "Daarom is een stuk DNA met veel G en C steviger en smelt het bij een hogere "
                "temperatuur.",
                "Let op uracil: dat is het verschil tussen DNA en RNA in de basen. Het andere "
                "verschil zit in de suiker, ribose in plaats van desoxyribose.",
            ],
        ),
        dict(
            aanpak="Eén regel volstaat voor deze hele reeks: wat A is, is ook T, en wat G is, is ook "
                   "C. Reken dan met honderd procent als geheel.",
            waarom=[
                "Let op de twee stappen: eerst dubbel je het gegeven percentage voor het eerste "
                "paar, dan verdeel je de rest in twee. Wie die tweede deling vergeet, antwoordt 52 "
                "in plaats van 26.",
                "Let erop dat je hier van thymine naar cytosine moet, dus naar het andere paar. Dat "
                "is dezelfde berekening maar met de twee paren omgewisseld.",
            ],
        ),
        dict(
            aanpak="Van dun naar dik: DNA rond histonen, dat samen is chromatine, en strak opgerold "
                   "is het een chromosoom. De laatste twee vragen gaan over wat die oprolling kost.",
            waarom=[
                None,
                "Let erop dat 46 chromosomen 23 paren zijn. Een geslachtscel heeft er 23, dus de "
                "helft, en dat is wat de meiose doet.",
                "Noem dat de genen dan niet afgelezen kunnen worden. Daarom rolt de cel het DNA "
                "enkel strak op wanneer ze gaat delen en moet verhuizen.",
                "Noem allebei: wat je wel ziet en wat niet. De tweede helft van het antwoord is "
                "waar deze vraag om draait, want een karyogram toont de verpakking en niet de "
                "inhoud.",
            ],
        ),
        dict(
            aanpak="Drie werkers aan de replicatievork: één opent, één bouwt, één plakt. De richting "
                   "van het bouwen verklaart de rest van de reeks.",
            waarom=[
                "Let op de ligase: zij plakt, en precies daarom heeft de lagging strand haar nodig. "
                "De namen van de enzymen eindigen op -ase, en dat is bij elk enzym zo.",
                None,
                "Noem beide redenen samen: het polymerase werkt maar in één richting, en de twee "
                "strengen lopen tegengesteld. Enkel het ene of het andere noemen verklaart het "
                "verschil niet.",
                "Waar, en dat heeft een naam: semiconservatieve replicatie. Elke dochtercel houdt "
                "dus een helft van het oorspronkelijke DNA bij.",
            ],
        ),
        dict(
            aanpak="Hou mitose en meiose op drie punten naast elkaar: hoeveel cellen, hoeveel "
                   "chromosomen, en gelijk of verschillend.",
            waarom=[
                "Let op de derde rij: mitose geeft identieke cellen, meiose verschillende. Dat "
                "verschil is de hele reden dat broers en zussen niet op elkaar lijken.",
                "Let op de anafase: daar worden de chromatiden getrokken. Een hulpje bij de orde: "
                "pro, meta, ana, telo, en de metafase is die met de rij in het midden.",
                "Noem alle drie de bronnen, zoals gevraagd. De derde, de bevruchting zelf, wordt "
                "vaak vergeten, en toch is dat de grootste toevalsfactor van de drie.",
                "Noem dat de chromosomen dan nog uit twee chromatiden bestaan. De verdubbeling was "
                "al voor de eerste deling gebeurd, en één verdubbeling volstaat voor twee delingen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-overerving-van-genetisch-materiaal-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes woorden, en één onderscheid dat de hele bundel draagt: het genotype is wat "
                   "erin zit, het fenotype is wat je ziet.",
            waarom=[
                "Let op het verschil tussen genotype en fenotype: twee planten kunnen hetzelfde "
                "fenotype hebben met een ander genotype, en dat is precies wat de volgende reeks "
                "laat uitrekenen.",
                "Let op het woord drager: die heeft het allel wel en de aandoening niet. Dat kan "
                "enkel bij een recessief kenmerk, en het verklaart waarom zo'n aandoening uit "
                "gezonde ouders geboren wordt.",
            ],
        ),
        dict(
            aanpak="Teken het vierkant, ook als je het antwoord meent te weten. Zet de gameten van "
                   "de ene ouder bovenaan en die van de andere links, en vul de vier vakjes in.",
            waarom=[
                "Let op het verschil tussen de genotypische en de fenotypische verhouding bij "
                "dezelfde kruising: 1 op 2 op 1 in de vakjes, 3 op 1 in wat je ziet. De twee "
                "heterozygote vakjes tonen immers hetzelfde als het homozygoot dominante.",
                None,
                None,
                "Let erop dat hier nul het juiste antwoord is: elk kind krijgt een A van de ene "
                "ouder, dus toont geen enkel kind het recessieve kenmerk. Ze zijn wel allemaal "
                "drager.",
                "Noem alle drie de betrokkenen, zoals gevraagd. Dit is de klassieke "
                "terugrekenvraag: uit het recessieve kind volgt dat beide ouders heterozygoot zijn.",
            ],
        ),
        dict(
            aanpak="Hier geldt de gewone dominantie niet. Reken eerst het vierkant uit en lees dan "
                   "af wat elk genotype te zien geeft.",
            waarom=[
                "Noem de verhouding en de kleuren samen. Let erop dat je hier drie kleuren krijgt "
                "en bij volledige dominantie maar twee; dat is het hele verschil.",
                "Waar, en dat is de reden waarom: elk genotype heeft zijn eigen zichtbare vorm, dus "
                "vallen de twee verhoudingen samen op 1 op 2 op 1.",
                "Noem van beide een voorbeeld, zoals roze en bloedgroep AB. Het verschil is of de "
                "twee allelen mengen of elk volledig te zien zijn.",
                "Let erop dat bloedgroep O hier niet kan: geen van beide ouders heeft een O-allel om "
                "door te geven.",
                "Let erop dat AB hier niet kan, en O ook niet. De vader geeft altijd O, de moeder "
                "altijd A of B, dus elk kind is heterozygoot met O erbij.",
            ],
        ),
        dict(
            aanpak="Behandel twee kenmerken als twee aparte kruisingen en combineer daarna. Zo hoef "
                   "je geen vierkant van zestien vakjes uit het hoofd te kennen.",
            waarom=[
                "Let op 9 op 3 op 3 op 1: dat is gewoon 3 op 1 maal 3 op 1. Wie de twee kenmerken "
                "apart neemt, hoeft die verhouding niet vanbuiten te leren.",
                "Let erop dat deze kruising vier even grote groepen geeft. De tweede ouder geeft "
                "immers altijd ab, dus bepaalt de eerste ouder alleen het resultaat.",
                "Let erop dat dit AB, Ab, aB en ab zijn. Het aantal soorten gameten verdubbelt bij "
                "elk gen dat heterozygoot is.",
                "Noem de crossing-over in je antwoord. Dat is wat de koppeling af en toe doorbreekt "
                "en waarom genen op hetzelfde chromosoom niet volledig samen overerven.",
            ],
        ),
        dict(
            aanpak="Hou vast dat een man één X heeft en een vrouw twee. Bijna alle antwoorden van "
                   "deze reeks volgen daaruit.",
            waarom=[
                "Noem alle drie de redenen, zoals gevraagd. Ze hangen samen maar ze zijn niet "
                "hetzelfde: het aantal X-chromosomen, het volstaan van één allel, en de kans op een "
                "gezonde tweede X.",
                "Noem wat er met de zonen en met de dochters gebeurt, en zeg bij elk waarom. De "
                "dochters krijgen van hun vader een gezonde X, en dat is de kern van het antwoord.",
                "Niet waar: een vader geeft aan zijn zoon zijn Y en aan zijn dochter zijn X. Een "
                "X-gebonden allel gaat van een vader dus altijd naar zijn dochters.",
                None,
            ],
        ),
        dict(
            aanpak="Bij een stamboom lees je twee dingen af: dominant of recessief, en gewoon of "
                   "geslachtsgebonden. Verantwoord elk besluit met wat je in het schema ziet.",
            waarom=[
                "Noem beide besluiten, zoals de vraag twee keer vraagt. Het tweede argument gaat "
                "over de vader: bij een X-gebonden kenmerk zou hij het zelf tonen.",
                "Niet waar: wie een dominant allel heeft, toont het kenmerk. Een generatie "
                "overslaan hoort bij een recessief kenmerk, dat in de dragers verborgen meereist.",
                "Noem allebei: wat het zegt en wat het niet zegt. Dat tweede is waar deze vraag om "
                "draait, want recessief en geslachtsgebonden zijn twee aparte vragen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-genexpressie-en-dna-technologie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Twee dingen samen bij het omzetten: je neemt de complementaire base, en op de "
                   "plaats van thymine komt uracil. Doe het letter per letter.",
            waarom=[
                "Let op de laatste: ATT wordt UAA, en dat is een stopcodon. Zo zie je dat een "
                "stopsignaal gewoon in de streng geschreven staat.",
                None,
                "Let erop dat drie basen één codon zijn. Daarom verschuift een deletie van één base "
                "alles wat erna komt, en dat komt in de vierde reeks terug.",
                "Let erop dat AUG niet enkel start maar ook voor methionine staat. Elk eiwit begint "
                "dus met dat aminozuur, ook als het er later afgeknipt wordt.",
            ],
        ),
        dict(
            aanpak="Drie verschillen tussen DNA en RNA: de suiker, de base en het aantal strengen. "
                   "Daarna volgt de vraag waarom een bacterie ons gen kan lezen.",
            waarom=[
                "Let erop dat je alle drie de verschillen geeft. Enkel uracil noemen is een derde "
                "van het antwoord.",
                None,
                "Noem dat de code bij nagenoeg alle organismen dezelfde is. Dat is zelf een "
                "argument voor de evolutie, en het is de reden dat insuline uit een bacteriekuip "
                "kan komen.",
            ],
        ),
        dict(
            aanpak="Volg de weg: in de kern wordt het mRNA geschreven en bijgewerkt, buiten de kern "
                   "wordt het op het ribosoom gelezen.",
            waarom=[
                None,
                "Let op de promotor: dat is geen gen maar het startblok ervoor. Daar beslist de cel "
                "of een gen afgelezen wordt of niet.",
                "Noem beide helften: de introns eruit en de exons aan elkaar. Een hulpje: exons "
                "blijven er in, introns gaan eruit.",
                "Noem het anticodon met naam. De vraag vraagt uitdrukkelijk met welk deel, dus "
                "enkel zeggen dat het een aminozuur brengt is te weinig.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke mutatie af wat er met de leeslijst gebeurt. Eén base anders is "
                   "iets heel anders dan één base minder.",
            waarom=[
                None,
                "Noem het verschuiven van het leesraam. Dat is de kern: na een deletie staan alle "
                "volgende codons verkeerd, en dat levert bijna altijd een onbruikbaar eiwit.",
                "Let erop dat een mutatie in een gewone lichaamscel niet overerft. Ze kan daar wel "
                "kanker veroorzaken, maar ze gaat niet naar je kinderen.",
                "Noem drie heel verschillende soorten, zoals straling en een stof uit rook. Zo zie "
                "je dat een mutageen zowel fysisch als chemisch kan zijn.",
                "Niet waar: epigenetische wijzigingen zetten genen aan of uit zonder de letters te "
                "veranderen. Daarom kan een eeneiige tweeling een ander patroon hebben dan de "
                "andere.",
            ],
        ),
        dict(
            aanpak="Vier stappen, en één gedachte eronder: wie met hetzelfde enzym knipt, krijgt "
                   "passende uiteinden. Daarna nog twee vragen over de woorden.",
            waarom=[
                "Let erop dat het gen eerst uitgeknipt wordt en het plasmide daarna geopend. Als je "
                "het plasmide eerst opent, is dat niet fout in de praktijk, maar deze orde volgt de "
                "logica van het gen.",
                "Noem de sticky ends. Daar zit de reden: hetzelfde enzym geeft dezelfde overhang, en "
                "dus passen de twee stukken in elkaar.",
                None,
                "Let erop dat het verschil niet in de techniek zit maar in de herkomst van het gen. "
                "Daarom wordt cisgeen vaak minder ingrijpend genoemd dan transgeen.",
                "Niet waar: een gemodificeerd organisme kan ook cisgeen zijn, of het gevolg van een "
                "ingreep in zijn eigen genen. Transgeen is één soort modificatie en niet het "
                "synoniem ervan.",
            ],
        ),
        dict(
            aanpak="Drie technieken met elk een eigen doel: vermeerderen, scheiden en gericht "
                   "aanpassen. Zeg bij elke vraag welk doel aan de orde is.",
            waarom=[
                None,
                "Noem dat de lange fragmenten in het netwerk van de gel blijven steken. Zeggen dat "
                "ze zwaarder zijn is geen verklaring, want de gel en niet het gewicht doet het werk.",
                "Noem drie toepassingen, zoals gevraagd. Vermeld er bij voorkeur ook een buiten het "
                "gerecht, zoals het onderzoek naar verwantschap.",
                "Noem beide delen van CRISPR-Cas: het geleidende RNA dat de plaats zoekt en het "
                "knipeiwit dat snijdt. Het gerichte karakter is wat het nieuw maakt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ontstaan-en-evolutie-van-soorten-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes argumenten uit vijf vakgebieden. Een hulpje: fossielen zijn paleontologie, "
                   "moleculen zijn biochemie, verspreiding over de aarde is biogeografie, bouw is "
                   "anatomie.",
            waarom=[
                "Let op de buideldieren in Australië: dat is biogeografie, want het gaat over waar "
                "soorten voorkomen. De verklaring is dat het continent lang geïsoleerd lag.",
                "Let erop dat de blinde darm bij de anatomie hoort, ook al noemen we hem "
                "rudimentair. Rudimentair is wat het orgaan is, anatomie is hoe we het "
                "vaststellen.",
            ],
        ),
        dict(
            aanpak="Twee vragen beslissen alles hier: komt het van hetzelfde af (homoloog), of doet "
                   "het enkel hetzelfde (analoog)? En wat niet meer dient, is rudimentair.",
            waarom=[
                "Let op de twee vleugels in de eerste rij: beide vliegen, maar ze zijn heel anders "
                "gebouwd. Dezelfde functie zonder gemeenschappelijke oorsprong is analoog.",
                "Noem van beide begrippen zowel de bouw als de functie. Een antwoord dat enkel over "
                "de functie spreekt, mist juist het onderscheid dat de vraag zoekt.",
            ],
        ),
        dict(
            aanpak="Hou bij fossielen twee dingen vast: diep is oud, en fossiliseren is "
                   "uitzonderlijk. De derde vraag gaat over wat een overgangsfossiel laat zien.",
            waarom=[
                "Niet waar: diepere lagen zijn ouder, want ze zijn eerder afgezet. Dat is het "
                "beginsel waarmee men lagen dateert.",
                "Noem de voorwaarden, zoals snel bedekt worden en zonder zuurstof. Enkel zeggen dat "
                "het zeldzaam is, verklaart niet waarom.",
                "Noem van beide groepen een kenmerk. Een overgangsfossiel is pas overtuigend als je "
                "de twee combinaties naast elkaar kan zetten.",
            ],
        ),
        dict(
            aanpak="Hou Lamarck en Darwin scherp uit elkaar: bij Lamarck verandert het individu, bij "
                   "Darwin verandert de samenstelling van de populatie.",
            waarom=[
                "Noem waarom het niet klopt en niet enkel wat hij dacht. De reden is dat wat je in "
                "je leven doet, je geslachtscellen niet verandert.",
                "Noem alle drie de woorden, zoals gevraagd. Zonder erfelijkheid werkt de selectie "
                "niet, en dat derde woord wordt het vaakst vergeten.",
                "Niet waar: de moderne theorie bouwt op Darwin verder, met wat we daarna over DNA en "
                "mutaties geleerd hebben. Zijn kern is dus aangevuld en niet verworpen.",
            ],
        ),
        dict(
            aanpak="Eén valkuil beheerst deze reeks: de omgeving maakt geen nieuwe eigenschappen, "
                   "ze kiest tussen eigenschappen die er al zijn.",
            waarom=[
                "Noem dat de ongevoelige bacteriën er al waren. Dat is de verbetering die de vraag "
                "zoekt: het antibioticum selecteert, het verandert niemand.",
                "Noem de keten volledig: minder opvallen, minder opgegeten, meer nakomelingen. De "
                "laatste stap is wat het een evolutie maakt.",
                "Let erop dat fitness over vruchtbare nakomelingen gaat en niet over kracht of "
                "gezondheid. Een sterk dier zonder jongen heeft een fitness van nul.",
                "Waar: in een kleine populatie kan het toeval een allel snel laten verdwijnen. "
                "Daarom is een kleine populatie extra kwetsbaar, ook zonder jacht of ziekte.",
            ],
        ),
        dict(
            aanpak="Isolatie kan door ruimte, door tijd of door gedrag. Hou daarna vast dat een "
                   "soortgrens pas vastligt bij het ontbreken van vruchtbaar nageslacht.",
            waarom=[
                "Let op temporele isolatie: de dieren leven naast elkaar maar paren in een andere "
                "maand. Ruimte is dus niet de enige scheiding.",
                "Let op het woord vruchtbaar: een paard en een ezel geven wel een muilezel, maar die "
                "is onvruchtbaar. Daarom blijven het twee soorten.",
                "Noem alle drie, zoals gevraagd. Isolatie alleen volstaat niet; zonder variatie en "
                "selectie blijven de twee groepen op elkaar lijken.",
                "Niet waar: veel variatie maakt een populatie juist sterker, want de kans is groter "
                "dat sommige individuen de ziekte doorstaan. Dat is ook het argument tegen te veel "
                "inteelt.",
                "Noem het woord erfelijk in je antwoord. Daar zit het hele verschil met Lamarck, en "
                "daarom is dit dezelfde vraag als die over de giraf.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-biomoleculen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie grote groepen. Een hulpje: namen op -ose en op -ose-achtig zijn suikers, "
                   "namen van vetten en van cholesterol zijn lipiden, en alles wat werkt of "
                   "vervoert is bijna altijd een proteïne.",
            waarom=[
                "Let op glycogeen: dat is de voorraadvorm van glucose bij mens en dier, zoals "
                "zetmeel bij de plant. De gly aan het begin verraadt de glucose.",
                "Let erop dat een enzym een proteïne is. Dat verband komt in de vierde reeks terug, "
                "want de vorm van dat eiwit bepaalt of het enzym werkt.",
            ],
        ),
        dict(
            aanpak="Hou bij de suikers twee dingen apart: uit welke bouwstenen ze bestaan, en hoe "
                   "snel de glucose vrijkomt. De laatste twee vragen gaan over enzymen.",
            waarom=[
                "Let op sacharose en lactose: in beide zit glucose, en het tweede stuk maakt het "
                "verschil. Fructose bij de gewone tafelsuiker, galactose bij de melksuiker.",
                "Noem dat de bindingen anders liggen en dat wij het enzym missen. Een koe kan "
                "cellulose wel gebruiken, met de hulp van bacteriën in haar maag.",
                "Noem dat de glucose traag vrijkomt. Dezelfde gram koolhydraat geeft dus een ander "
                "verloop in je bloed, en dat is waarom men over trage en snelle suikers spreekt.",
                "Let erop dat het om het enzym gaat en niet om een allergie. Lactose-intolerantie "
                "is een tekort aan lactase, en dat is iets heel anders dan een afweerreactie.",
            ],
        ),
        dict(
            aanpak="Hou bij de lipiden één eigenschap vast: ze stoten water af. Daaruit volgen de "
                   "laatste twee vragen bijna van zelf.",
            waarom=[
                "Let erop dat het drie vetzuren zijn, vandaar tri in triglyceride. Een fosfolipide "
                "heeft er twee en een fosfaatgroep op de derde plaats.",
                None,
                "Niet waar, en het is net omgekeerd: een gram vet levert ruim twee keer zo veel "
                "energie als een gram suiker. Daarom slaat het lichaam zijn voorraad als vet op en "
                "niet als suiker.",
                "Noem beide uiteinden: de waterminnende kop en de waterafstotende staarten. De "
                "dubbellaag ontstaat dan van zelf, en dat is wat de vraag zoekt.",
                "Noem de eigenschap met naam, hydrofoob, en zeg waarvoor hij ze gebruikt. Zonder "
                "dat tweede deel is het antwoord maar half.",
            ],
        ),
        dict(
            aanpak="Vier lagen, van de ketting naar het geheel. Hou vast dat elke laag de vorige "
                   "veronderstelt: de volgorde bepaalt de plooien, de plooien bepalen de vorm.",
            waarom=[
                "Let erop dat de quaternaire structuur niet bij elk eiwit bestaat: enkel wanneer "
                "meerdere ketens samenwerken, zoals bij hemoglobine met haar vier ketens.",
                "Noem alle drie de groepen. De restgroep is wat de aminozuren van elkaar "
                "onderscheidt, en die komt in de volgende vraag terug.",
                "Noem dat ze water afstoten. Dat is dezelfde eigenschap als bij de lipiden, en ze "
                "verklaart hoe een eiwit zijn vorm vindt.",
                "Noem het woord vorm twee keer: ze gaat verloren, en de werking hangt ervan af. Dat "
                "heet denaturatie, en je ziet het aan een ei in de pan.",
            ],
        ),
        dict(
            aanpak="Vijf eiwitten met elk een taak. Vraag je telkens af wat het eiwit doet: "
                   "vervoeren, bewegen, doorlaten, versnellen of regelen.",
            waarom=[
                "Let op de aquaporines: water raakt ook zonder poort door een membraan, maar veel "
                "te traag voor een nier. Daarom zijn die kanalen nodig.",
                "Noem drie verschillende soorten taken, zoals gevraagd. Enkel enzymen noemen laat "
                "zien hoe veelzijdig eiwitten zijn, en dat is precies wat de vraag toetst.",
            ],
        ),
        dict(
            aanpak="Twee reacties volstaan voor alle biomoleculen: verbinden met water als "
                   "bijproduct, en splitsen met water. Zie je dat, dan heb je de hele reeks.",
            waarom=[
                "Let op het water: bij condensatie komt het vrij, bij hydrolyse is het nodig. De "
                "naam hydrolyse zegt het zelf, want hydro is water en lyse is splitsen.",
                None,
                "Noem beide reacties met naam en noem het water erbij. Dat dezelfde twee reacties "
                "bij suikers, eiwitten en vetten werken, is de kern van dit hoofdstuk.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-snelheid-van-een-chemische-reactie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist bij elke factor: komen de deeltjes vaker of harder tegen "
                   "elkaar? Dan gaat het sneller. Verandert er niets aan de botsingen, dan verandert "
                   "er niets.",
            waarom=[
                "Let op het grotere vat: dezelfde hoeveelheid gas in meer ruimte betekent een "
                "lagere concentratie, dus minder botsingen. Een groter vat helpt dus niet, het "
                "vertraagt.",
                "Let op het glas en het staal: het materiaal van het vat doet niets met de "
                "botsingen tussen de deeltjes. Dat is een factor die er geen is.",
            ],
        ),
        dict(
            aanpak="Hier moet je de factor benoemen. De vijf om uit te kiezen: temperatuur, "
                   "concentratie, verdelingsgraad, katalysator en, bij sommige stoffen, licht.",
            waarom=[
                "Let op de bruine fles: die houdt licht tegen. Waterstofperoxide ontleedt onder "
                "invloed van licht, en daarom zit het nooit in een doorzichtige fles.",
                "Noem allebei: wat sneller gaat en wat gelijk blijft. Dat de opbrengst dezelfde is, "
                "is de kern van deze vraag; snelheid en opbrengst zijn twee verschillende dingen.",
            ],
        ),
        dict(
            aanpak="Het botsingsmodel in twee woorden: genoeg energie en de juiste richting. Elke "
                   "factor uit de eerste reeks werkt op een van die twee.",
            waarom=[
                "Noem beide voorwaarden, zoals gevraagd. De richting wordt vaak vergeten, en toch "
                "is dat de reden waarom lang niet elke harde botsing iets oplevert.",
                None,
                "Noem beide effecten van de warmte: vaker botsen en harder botsen. Enkel het eerste "
                "noemen verklaart niet waarom tien graden erbij de snelheid vaak bijna verdubbelt.",
            ],
        ),
        dict(
            aanpak="Lees het diagram als een berg: de hoogte van de top boven het begin is de "
                   "drempel, het hoogteverschil tussen begin en einde is wat de reactie oplevert of "
                   "kost.",
            waarom=[
                "Let op het verschil tussen de activeringsenergie en de reactie-energie: de eerste "
                "wordt vanaf het begin naar de top gemeten, de tweede van het begin naar het einde. "
                "Twee verschillende hoogtes in dezelfde tekening.",
                None,
                "Niet waar: elke reactie heeft een drempel, ook als er netto energie bij moet. De "
                "berg kan bij een endo-energetische reactie zelfs hoog zijn terwijl het einde boven "
                "het begin ligt.",
                "Noem allebei: wat verandert en wat niet. Dat een katalysator de opbrengst niet "
                "verandert, is precies waarom hij geen reagens is.",
                "Noem dat maar weinig deeltjes de drempel halen. Dat verband tussen een hoge berg "
                "en een trage reactie komt in de laatste reeks met de verdeling terug.",
            ],
        ),
        dict(
            aanpak="Bij een grafiek let je altijd eerst op wat op de assen staat. Een "
                   "concentratie-tijdgrafiek geeft de snelheid via de steilheid, een "
                   "snelheid-tijdgrafiek geeft ze rechtstreeks.",
            waarom=[
                "Noem dat er minder reagens over is en dus minder botsingen. De lijn wordt vlakker "
                "omdat de snelheid zakt, en niet omdat de reactie stopt.",
                "Let erop dat de steilheid van een concentratielijn de snelheid is. Dat is de reden "
                "dat je soms de ene grafiek en soms de andere gebruikt.",
                "Noem drie mogelijke oorzaken en de onmogelijke, zoals gevraagd. Dat laatste deel is "
                "het punt: dezelfde stoffen geven altijd dezelfde vergelijking.",
            ],
        ),
        dict(
            aanpak="In een verdeling ligt rechts van de streep het deel van de deeltjes dat kan "
                   "reageren. Temperatuur schuift de verdeling, een katalysator schuift de streep.",
            waarom=[
                "Noem de oppervlakte rechts van de streep. Dat is wat verklaart waarom een kleine "
                "stijging van de temperatuur zo veel verschil maakt.",
                "Let op het verschil met de vorige vraag: hier beweegt de streep en niet de "
                "verdeling. De deeltjes zelf worden niet energieker.",
                "Noem dat de temperatuur van een cel vastligt. Daarom is een enzym voor haar de "
                "enige weg, en dat verbindt dit hoofdstuk met de biologie.",
                "Noem alle drie, zoals gevraagd. Van de vijf factoren vallen temperatuur weg en, bij "
                "een vaste reactie, ook licht.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-chemisch-evenwicht-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk bij een grafiek naar het einde van de lijnen. Raakt een reagenslijn de as, "
                   "dan is de reactie aflopend. Blijven alle lijnen boven de as vlak liggen, dan is "
                   "er evenwicht.",
            waarom=[
                "Let op het verschil tussen de eerste en de derde: in beide gevallen eindigt de "
                "grafiek vlak. Wat beslist, is of er nog reagens over is.",
                "Noem twee manieren, zoals gevraagd. De tweede is de sterkste: bij een evenwicht "
                "zie je na een toevoeging opnieuw iets gebeuren, bij een afgelopen reactie niet.",
            ],
        ),
        dict(
            aanpak="Reken altijd met de verhouding uit de vergelijking. Deel het aantal mol van elke "
                   "stof door haar coëfficiënt; de kleinste uitkomst is de limiterende stof.",
            waarom=[
                None,
                "Let erop dat je de verbruikte hoeveelheid aftrekt: A is met 2 mol limiterend, dus "
                "wordt er 2 mol B verbruikt en blijft er 3 mol over.",
                "Let op de verhouding één op twee: voor 3 mol A zou je 6 mol B nodig hebben en er is "
                "maar 3. Wie enkel naar de getallen kijkt en niet naar de verhouding, antwoordt hier "
                "fout.",
                "Noem dat het andere reagens dan volledig reageert. Bij een evenwicht is er nog een "
                "tweede reden: een overmaat duwt het evenwicht naar de kant van het product.",
            ],
        ),
        dict(
            aanpak="Dynamisch betekent dat er nog iets gebeurt. Hou vast dat het de twee snelheden "
                   "zijn die gelijk worden, en niet de concentraties.",
            waarom=[
                "Niet waar: de concentraties worden constant, niet gelijk. Ze kunnen heel ver uit "
                "elkaar liggen, en waar ze stilvallen hangt van de reactie af.",
                "Niet waar: er worden nog voortdurend moleculen gevormd en weer afgebroken, even "
                "snel. Dat is precies wat dynamisch betekent.",
                "Noem beide helften: de twee reacties gaan door, en ze gaan even snel. Zonder het "
                "tweede deel is het geen evenwicht.",
                "Noem van elke reactie waarom ze versnelt of vertraagt. Dit is dezelfde gedachte als "
                "bij de reactiesnelheid: minder reagens betekent minder botsingen.",
            ],
        ),
        dict(
            aanpak="Eén regel voor de hele reeks: het evenwicht werkt de verstoring tegen. Neem je "
                   "iets weg, dan maakt het bij; voeg je iets toe, dan ruimt het op.",
            waarom=[
                "Let op het tweede geval: product wegnemen duwt het evenwicht naar rechts, net als "
                "reagens toevoegen. Twee verschillende ingrepen met hetzelfde gevolg.",
                "Let op de warmte als deelnemer: bij een exo-energetisch evenwicht is warmte een "
                "product. Opwarmen voegt dus iets aan de rechterkant toe, en dat duwt naar links.",
                None,
                "Noem dat het evenwicht de verstoring tegenwerkt. Dat is de hele wet in één zin, en "
                "met die zin los je de hele reeks op.",
            ],
        ),
        dict(
            aanpak="Bij een gasevenwicht tel je de mol gas links en rechts. Persen duwt naar de kant "
                   "met minder gasdeeltjes; bij een gelijk aantal gebeurt er niets.",
            waarom=[
                "Noem beide: de richting en de reden. De kant met minder deeltjes neemt minder "
                "plaats in, en zo verlaagt het mengsel de druk weer een beetje.",
                "Let erop dat nul ook een antwoord is. Als beide kanten even veel gas hebben, kan "
                "schuiven de druk niet veranderen.",
                "Noem het besluit en de reden. Afkoelen neemt warmte weg, dus schuift het evenwicht "
                "naar de kant die warmte maakt; bleker betekent dus dat die kant exo-energetisch is.",
            ],
        ),
        dict(
            aanpak="Bij een grafiek kijk je naar wie als eerste beweegt. Eén lijn die plots "
                   "verspringt wijst op een stof, alle lijnen tegelijk op temperatuur of volume.",
            waarom=[
                "Noem alle drie de dingen, zoals gevraagd. Het derde is het beslissende: beweegt "
                "alles samen, dan was het geen toevoeging.",
                None,
                "Noem alle drie de ingrepen. Let erop dat een katalysator er niet bij hoort: die "
                "maakt het evenwicht sneller bereikt, niet gunstiger.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-organische-stoffen-classificatie-eigenschappen-en-toepassingen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek in elke formule de kenmerkende groep: OH is een alcohol, COOH een "
                   "carbonzuur, CO middenin een keton, CO aan het eind een aldehyde, O tussen twee "
                   "ketens een ether.",
            waarom=[
                "Let op het verschil tussen de tweede en de derde: COOH is een zuur, CO tussen twee "
                "koolstofketens is een keton. Eén zuurstofatoom en één waterstofatoom maken het hele "
                "verschil.",
                "Let erop dat een alkaan geen kenmerkende groep heeft: enkel koolstof en waterstof. "
                "Dat is wat de laatste reeks met verzadigd bedoelt.",
                "Let op de namen: de uitgang zegt de klasse. Op -zuur is een carbonzuur, op -een is "
                "een alkeen, op -amine is een amine.",
            ],
        ),
        dict(
            aanpak="Vier groepen met zuurstof erin, en ze lijken op elkaar. Tel bij elke groep hoe "
                   "veel zuurstof er is en wat eraan hangt.",
            waarom=[
                "Let op het verschil tussen een ester en een ether: bij een ester hoort er ook een "
                "dubbel gebonden zuurstof bij, bij een ether staat er enkel één zuurstofatoom "
                "tussen de ketens.",
                "Noem dat enkel de plaats verschilt. Dat is het volledige antwoord: dezelfde groep, "
                "aan het uiteinde of middenin.",
                "Niet waar: een amine heeft een stikstofgroep. Alcohol en amine lijken in de naam "
                "niet op elkaar, maar in oefeningen worden ze vaak verward omdat beide een polaire "
                "groep hebben.",
                "Noem allebei: dat er geen OH in staat en wat het dan wel is. Verbeteren alleen is "
                "niet genoeg, de vraag vraagt ook een verantwoording.",
            ],
        ),
        dict(
            aanpak="Bij een kookpunt kijk je naar de krachten tussen de moleculen. Waterstofbruggen "
                   "zijn de sterkste, daarna komt het oppervlak van de keten.",
            waarom=[
                "Noem de waterstofbrug met naam. Dat is de reden, en het verklaart ook waarom water "
                "voor zo'n kleine molecule zo'n hoog kookpunt heeft.",
                "Noem de londondispersiekracht en het oppervlak. Een langere keten raakt haar buren "
                "op meer plaatsen aan, en dat telt op.",
                "Noem dat een vertakte keten bolvormiger is en dus minder raakt. Zelfde formule, "
                "ander kookpunt: dat is wat deze vraag laat zien.",
            ],
        ),
        dict(
            aanpak="Eén regel voor de hele reeks: gelijk lost op in gelijk. Vraag je bij elke stof "
                   "af of er een polaire groep op zit die een waterstofbrug kan leggen.",
            waarom=[
                None,
                None,
                "Noem beide stoffen apart, zoals de vraag vraagt. Het kernwoord is de "
                "waterstofbrug: methanol kan er leggen met water, een alkaan niet.",
                "Noem dat de apolaire staart doorweegt. Zo zie je dat oplosbaarheid geen alles of "
                "niets is maar een verhouding tussen de twee delen van de molecule.",
            ],
        ),
        dict(
            aanpak="Zeep en een fosfolipide hebben dezelfde bouw: een polaire kop en apolaire "
                   "staarten. Daarmee verklaar je zowel de was als een celmembraan.",
            waarom=[
                "Noem de twee uiteinden en noem de micel. Zonder dat laatste woord beschrijf je wel "
                "de molecule maar niet hoe het vuil wegraakt.",
                "Waar, en dat verband is de moeite: dezelfde bouw maakt in water een micel of een "
                "dubbellaag. Daarom is zeep ook schadelijk voor een celmembraan, en dus voor "
                "bacteriën.",
                None,
            ],
        ),
        dict(
            aanpak="Hier moet je de gebruiksnaam en de scheikundige naam aan elkaar koppelen. Leer "
                   "ze per paar: aceton en propanon, formol en methanal, mierenzuur en HCOOH.",
            waarom=[
                "Let op het verschil tussen methaan en methanol: één letter in de naam, en het ene "
                "is een gas dat je verwarmt en het andere een giftige vloeistof.",
                "Let erop dat de gebruiksnamen ouder zijn dan de systematische. Mierenzuur heet zo "
                "omdat het uit mieren gehaald werd, en formol kennen veel mensen uit een "
                "biologielokaal.",
                "Noem drie dingen, zoals gevraagd, en noem zeker de dubbele binding. Daaruit volgt "
                "dat etheen kan polymeriseren tot polyetheen.",
                "Noem dat er geen waterstof meer bij kan. Verzadigd betekent vol, net als bij een "
                "verzadigde oplossing, en een alkeen met zijn dubbele binding is dus onverzadigd.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kunststoffen-nanomaterialen-en-duurzame-chemie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Zes afkortingen. Een hulpje: de P staat voor poly, en de rest is de monomeer. PE "
                   "van etheen, PS van styreen, PVC van vinylchloride.",
            waarom=[
                "Let op PTFE: dat is teflon, en de F in de naam staat voor fluor. Juist die "
                "fluoratomen maken het zo glad dat niets eraan blijft kleven.",
                "Let op PA: dat is nylon, en de A staat voor amide. Die naam verraadt al dat het om "
                "een polycondensatie gaat, zoals bij een eiwit.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: komt er bij elke stap een kleine molecule vrij (condensatie) "
                   "of niet (additie)? Een dubbele binding in de monomeer wijst op additie.",
            waarom=[
                "Let erop dat PE en PVC allebei uit een monomeer met een dubbele binding komen. Die "
                "binding gaat open en dient als haakje, en daarom komt er niets vrij.",
                "Noem van beide types zowel de binding als wat er vrijkomt. Enkel zeggen dat er bij "
                "het ene water vrijkomt, laat de helft van het verschil weg.",
                None,
            ],
        ),
        dict(
            aanpak="Drie soorten, en de crosslinks beslissen welke het is: geen of weinig geeft een "
                   "thermoplast, veel een thermoharder, een tussenvorm een elastomeer.",
            waarom=[
                None,
                "Let erop dat de crosslinks de sleutel zijn van de hele reeks. Hoe meer "
                "dwarsverbindingen, hoe minder de ketens langs elkaar kunnen schuiven.",
                "Noem zowel de keuze als de reden. De reden is dat de ketens wel kunnen uitrekken "
                "maar door de crosslinks weer teruggetrokken worden.",
                "Noem het smelten in je antwoord. Dat is de hele reden, en het verklaart waarom "
                "zoveel kunststofafval wel in de sorteerstraat kan en sommige stukken niet.",
            ],
        ),
        dict(
            aanpak="Hou bij nanomaterialen twee dingen vast: de maat tussen 1 en 100 nanometer, en "
                   "het grote oppervlak per volume. Daaruit volgen zowel de voordelen als de "
                   "risico's.",
            waarom=[
                "Let op de dimensies: 0D is een bolletje, 1D een draad, 2D een vel. Het cijfer zegt "
                "in hoeveel richtingen het materiaal groot is.",
                None,
                None,
                None,
                "Noem twee gevolgen, zoals gevraagd. Het grote oppervlak per volume is dezelfde "
                "gedachte als bij de cel, maar hier is het een voordeel in plaats van een grens.",
                "Noem allebei: dat het UV tegenhoudt en dat het doorzichtig blijft. Zonder het "
                "tweede is er geen reden om de nanovorm te kiezen.",
                "Noem dat het dezelfde eigenschap is die beide kanten verklaart. Dat is wat de vraag "
                "zoekt: niet twee losse lijstjes maar één eigenschap met twee gevolgen.",
            ],
        ),
        dict(
            aanpak="De ladder gaat van voorkomen naar wegwerken. Onthou de orde met één gedachte: "
                   "wat er niet is, hoef je niet te verwerken.",
            waarom=[
                "Let erop dat preventie bovenaan staat en niet recycleren. Recycleren is al de derde "
                "trap, en veel campagnes doen alsof het de eerste is.",
                "Let op het verschil tussen down- en upcycling: beide zijn recycleren, maar de "
                "kwaliteit gaat de ene keer achteruit en de andere keer vooruit.",
                "Noem dat afval grondstof wordt. Dat is het kernidee, en het verklaart waarom men "
                "producten zo ontwerpt dat ze later weer te scheiden zijn.",
            ],
        ),
        dict(
            aanpak="In deze reeks lijken woorden op elkaar die iets anders betekenen. Lees telkens "
                   "heel precies wat er staat: biogebaseerd is niet biodegradeerbaar, en neutraal is "
                   "niet negatief.",
            waarom=[
                "Niet waar: biogebaseerd zegt waar de grondstof van komt, biodegradeerbaar zegt wat "
                "er met het afval gebeurt. Twee verschillende vragen.",
                "Noem allebei: wat je weet en wat niet. Het voorbeeld van bio-PE uit rietsuiker maakt "
                "het concreet, want die fles blijft even lang liggen als een gewone.",
                "Let op de kleuren van waterstof: het gaat niet over het gas zelf, dat is altijd "
                "hetzelfde, maar over hoe het gemaakt is. Enkel groen werkt met hernieuwbare stroom.",
                "Let erop dat grijs water niet vuil water van het toilet is; dat heet zwart water. "
                "Grijs water kan je hergebruiken voor het toilet of de tuin.",
                "Niet waar: neutraal betekent even veel opnemen als uitstoten. Meer opnemen dan "
                "uitstoten heet negatief, en dat is veel moeilijker te halen.",
                "Noem een voorbeeld, zoals gevraagd. Een label of een kleur op de verpakking zonder "
                "verandering in het proces is het duidelijkste geval.",
                "Noem ook de bronnen die men minder verwacht, zoals autobanden en het wassen van "
                "synthetische kleding. Dat is wat deze vraag onderscheidt van een vraag over "
                "zwerfvuil.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-elektrostatica-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie manieren, en één vraag die ze scheidt: is er aanraking? Bij influentie is "
                   "er geen contact, bij de andere twee wel.",
            waarom=[
                "Let op het verschil tussen contact en influentie: bij contact verhuist er lading "
                "naar de bol, bij influentie schuift ze er enkel in op. Dat laatste verdwijnt weer "
                "zodra de staaf weggaat.",
                "Let erop dat enkel elektronen verhuizen. Protonen zitten in de kern vast, dus een "
                "voorwerp wordt positief door elektronen te verliezen en niet door protonen te "
                "krijgen.",
                "Noem alle drie, zoals gevraagd, en noem zeker dat de twee ladingen even groot zijn. "
                "Dat is de wet van ladingsbehoud: er komt niets bij, het verhuist enkel.",
            ],
        ),
        dict(
            aanpak="Volg bij elk geval waar de elektronen heen kunnen. Een aarding is een weg naar "
                   "buiten, en het moment waarop je ze verbreekt, beslist wat er achterblijft.",
            waarom=[
                "Let op het derde geval: de aarding eerst verbreken en dan de staaf weghalen. De "
                "weggeduwde elektronen zijn dan al vertrokken, dus blijft de bol positief. Haal je "
                "eerst de staaf weg, dan blijft ze neutraal.",
                "Let erop dat de lading zich gelijk verdeelt omdat de bollen identiek zijn. Waren ze "
                "verschillend groot, dan zou de grootste meer houden.",
                "Noem dat de lading enkel opschuift. Daarmee is ook de volgende reeks half opgelost, "
                "want datzelfde opschuiven verklaart de aantrekking van papier.",
            ],
        ),
        dict(
            aanpak="Alle drie de vragen gaan over hetzelfde: een geladen voorwerp maakt in een "
                   "neutraal voorwerp een dichte kant met tegengestelde lading. Die kant is "
                   "dichterbij, en dus wint ze.",
            waarom=[
                "Noem dat de dichtste kant harder aantrekt dan de verste afstoot. Dat is de reden "
                "dat er aantrekking overblijft, en het is de wet van Coulomb met haar afstand in het "
                "kwadraat die dat verklaart.",
                "Noem het woord polariseren. De muur wordt niet geladen; de ladingen in zijn "
                "moleculen schuiven enkel een beetje op.",
                None,
            ],
        ),
        dict(
            aanpak="In de wet van Coulomb staan de ladingen gewoon en de afstand in het kwadraat. "
                   "Reken daarom met factoren: twee keer verder is vier keer minder.",
            waarom=[
                "Let erop dat de afstand telkens gekwadrateerd wordt: twee keer geeft vier, drie "
                "keer geeft negen. Wie het kwadraat vergeet, antwoordt twee en drie.",
                "Let op de tweede: beide ladingen verdubbelen geeft vier keer, want twee maal twee. "
                "De ladingen worden met elkaar vermenigvuldigd.",
                "Noem het kwadraat met naam. Dat is het hele antwoord, en het is dezelfde reden "
                "waarom zwaartekracht op grote afstand zo snel verzwakt.",
                "Waar, en dat is de derde wet van Newton: de twee krachten zijn even groot en "
                "tegengesteld. Enkel het gevolg verschilt, want een lichter voorwerp beweegt meer.",
            ],
        ),
        dict(
            aanpak="Een vector zegt twee dingen: hoe groot de kracht is en welke kant ze op werkt. "
                   "Wijst ze naar de andere lading toe, dan is er aantrekking.",
            waarom=[
                "Noem het besluit en de reden. Aantrekking betekent dat de ladingen verschillend van "
                "teken zijn, en dat is wat de vraag wil horen.",
                "Let erop dat je de vectoren samen moet tellen en niet enkel de grootste moet nemen. "
                "Wijzen ze tegengesteld, dan trek je ze in feite van elkaar af.",
                None,
            ],
        ),
        dict(
            aanpak="Eén gedachte draagt deze hele reeks: lading zit op de buitenkant, en ze wordt "
                   "naar het tegengestelde getrokken. De toepassingen volgen daaruit.",
            waarom=[
                "Noem beide delen: de lading zit op de buitenkant, en binnenin heffen de velden "
                "elkaar op. Dat is wat een kooi van Faraday doet.",
                "Noem drie situaties, zoals gevraagd. Het rooster van een magnetron is een mooi "
                "geval, want daar houdt de kooi de golven juist binnen.",
                "Noem dat het poeder ook rond de hoeken getrokken wordt. Dat is het voordeel boven "
                "spuiten met een gewoon pistool: bijna niets gaat verloren.",
                "Noem dat een tegengesteld geladen plaat de deeltjes opvangt. Laden alleen volstaat "
                "niet; er moet ook iets zijn dat ze aantrekt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-elektromagnetisme-en-inductie-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Hou bij magnetisme drie dingen vast: welke metalen het kunnen, dat ze uit kleine "
                   "gebieden bestaan, en dat die gebieden door een magneet in dezelfde richting "
                   "gaan staan.",
            waarom=[
                "Let erop dat enkel drie metalen echt ferromagnetisch zijn. Aluminium en koper zijn "
                "het niet, ook al zijn ze goede geleiders; geleiden en magnetisch zijn hebben niets "
                "met elkaar te maken.",
                "Noem dat elk stuk twee polen houdt. De reden ligt bij de elektronen zelf, en daarom "
                "kan je blijven breken zonder ooit een losse pool te krijgen.",
                "Waar: boven een bepaalde temperatuur vallen de weissgebieden weer in alle "
                "richtingen. Een harde slag of een wisselend veld werkt ook, en die temperatuur "
                "heet de curietemperatuur.",
            ],
        ),
        dict(
            aanpak="Veldlijnen tekenen wat het veld doet: hoe dichter bij elkaar, hoe sterker. "
                   "Buiten een magneet lopen ze altijd van noord naar zuid.",
            waarom=[
                "Let op het verschil tussen de drie beelden: tussen de benen van een hoefijzer lopen "
                "de lijnen parallel, rond een staafmagneet in bogen, en rond een draad in cirkels. "
                "Aan het beeld herken je de bron.",
                None,
                None,
                "Noem het besluit en de reden. Dit verrast vaak: bij het geografische noorden ligt "
                "de magnetische zuidpool, want anders zou de kompasnaald de andere kant op wijzen.",
            ],
        ),
        dict(
            aanpak="Een elektromagneet wordt op drie manieren sterker: meer stroom, meer windingen "
                   "of een ijzeren kern. Alle drie werken ze in dezelfde richting.",
            waarom=[
                "Let erop dat alle drie sterker geven. Deze reeks heeft dus geen valstrik in de "
                "richting; de vraag is of je de drie factoren kent.",
                "Let erop dat enkel de polen wisselen en de sterkte gelijk blijft. Dat is precies "
                "wat een motor en een luidspreker gebruiken.",
                None,
                "Noem drie toestellen en het voordeel, zoals gevraagd. Dat je hem kan uitzetten is "
                "het hele punt van een elektromagneet, en een schrootkraan laat dat het best zien.",
            ],
        ),
        dict(
            aanpak="Twee namen voor dezelfde soort kracht: op een draad met stroom heet ze Laplace, "
                   "op één bewegende lading Lorentz. Beweging is in beide gevallen de voorwaarde.",
            waarom=[
                "Let erop dat een stroom gewoon veel bewegende ladingen is. De twee krachten zijn "
                "dus geen verschillende verschijnselen maar twee manieren om er naar te kijken.",
                "Waar: zonder beweging is er geen magnetische kracht. Dat is het verschil met een "
                "elektrisch veld, dat ook op een stilstaande lading werkt.",
                "Noem allebei: de kracht keert om, en een motor gebruikt dat om te blijven draaien. "
                "Daarvoor dient de commutator in een gelijkstroommotor.",
                "Noem dat zwaardere deeltjes minder afbuigen. Daarmee scheidt het toestel de "
                "deeltjes, en dat is waarvoor het veld dient.",
            ],
        ),
        dict(
            aanpak="Inductie vraagt verandering. Hou dat vast: beweegt er niets, dan is er geen "
                   "spanning, hoe sterk de magneet ook is.",
            waarom=[
                "Let op de derde: een magneet die stil in de spoel ligt, geeft niets. De flux is dan "
                "wel groot maar ze verandert niet, en enkel verandering wekt spanning op.",
                None,
                "Noem alle drie, zoals gevraagd, en vergeet de hoek niet. Een winding die parallel "
                "met het veld staat, heeft een flux van nul.",
                "Noem de wet en de omkering samen. Het tegenwerken is de kern: daarom voelt een "
                "magneet een weerstand als je hem beweegt, en daarom werkt de volgende reeks.",
            ],
        ),
        dict(
            aanpak="Wervelstromen zijn inductie in een volle plaat in plaats van in een draad. Ze "
                   "werken altijd de beweging of de verandering tegen, en ze maken warmte.",
            waarom=[
                "Noem beide stappen: wervelstromen, en dan de wet van Lenz. Let erop dat koper niet "
                "magnetisch is; het effect komt volledig van de inductie.",
                "Noem dat de warmte in de pan ontstaat. Daarom werkt zo'n plaat niet met een pan van "
                "aluminium of glas, en dat is een gevolg dat je erbij mag zeggen.",
                "Niet waar: een elektromagnetische rem remt zonder contact, dus zonder slijtage. "
                "Daarom zit zo'n rem op een trein of een vrachtwagen naast de gewone rem.",
                "Noem drie toestellen, zoals gevraagd. De draadloze oplader is het modernste "
                "voorbeeld en werkt op precies hetzelfde beginsel als de fietsdynamo.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kracht-en-beweging-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie soorten: blijft de snelheid gelijk op een rechte lijn, dan ERB. Verandert ze "
                   "gelijkmatig, dan EVRB. Gaat het in een cirkel aan vaste snelheid, dan ECB.",
            waarom=[
                "Let erop dat een vallende steen EVRB is: de zwaartekracht blijft werken, dus neemt "
                "de snelheid gelijkmatig toe.",
                "Let erop dat afremmen ook EVRB is. Eenparig veranderlijk betekent gelijkmatig "
                "veranderend, dus zowel sneller als trager.",
            ],
        ),
        dict(
            aanpak="Bij een grafiek let je eerst op wat op de assen staat. Een rechte in x van t is "
                   "ERB, een parabool in x van t is EVRB, en een horizontale v van t is ERB.",
            waarom=[
                "Let op het verschil tussen de eerste en de derde: een schuine rechte in x van t en "
                "een vlakke lijn in v van t zeggen hetzelfde. Dezelfde beweging, twee verschillende "
                "grafieken.",
                None,
                "Let erop dat de steilheid van een x-grafiek de snelheid is. Bij een v-grafiek is de "
                "steilheid dan de versnelling, en de oppervlakte eronder de afgelegde weg.",
                "Noem dat de richting van de snelheid verandert. Snelheid is een vector, dus ook een "
                "verandering van richting is een versnelling; die wijst hier naar het middelpunt.",
            ],
        ),
        dict(
            aanpak="Eén formule voor de hele reeks: kracht is massa maal versnelling. Zet altijd eerst "
                   "op wat je zoekt, dan weet je of je moet delen of vermenigvuldigen.",
            waarom=[
                "Let erop dat je hier deelt: de kracht door de massa. Schrijf de eenheid erbij, want "
                "een versnelling is meter per seconde in het kwadraat.",
                "Let op de derde: daar zoek je de massa, dus deel je de kracht door de versnelling. "
                "Let dan ook op de eenheid, want het antwoord is kilogram en geen newton.",
                "Noem dat massa en versnelling omgekeerd verbonden zijn bij dezelfde kracht. Dat is "
                "het antwoord, en het is dezelfde formule van anders bekeken.",
                None,
            ],
        ),
        dict(
            aanpak="Drie wetten in drie woorden: traagheid, kracht is massa maal versnelling, en "
                   "actie en reactie. Vraag je bij elk geval af welk van de drie je nodig hebt.",
            waarom=[
                "Let op de bus: de passagiers vallen naar voren omdat ze hun snelheid houden. Dat is "
                "de traagheidswet, en niet een kracht die hen naar voren duwt.",
                None,
                "Noem alle drie de punten en noem zeker het derde: de krachten werken op "
                "verschillende lichamen. Dat is de reden dat ze elkaar niet opheffen.",
                "Noem dat het in het luchtledige juist beter werkt. Dat is het sterkste argument "
                "tegen die uitleg, en daarna geef je de echte reden.",
            ],
        ),
        dict(
            aanpak="Hou twee dingen apart: welke krachten er werken, en wat hun som is. Een lichaam "
                   "in rust heeft meestal wel krachten, maar hun som is nul.",
            waarom=[
                "Let op de normaalkracht: die staat altijd loodrecht op het oppervlak. Op een helling "
                "wijst ze dus niet recht naar boven.",
                "Niet waar: er werken wel krachten, maar hun som is nul. Dit is de meest gemaakte "
                "fout van het hoofdstuk.",
                "Noem beide krachten en noem dat hun som nul is. De laatste zin van het antwoord is "
                "de kern: nul resulterende kracht is niet nul kracht.",
                None,
                "Let erop dat je vectoren samentelt en geen getallen. Richting telt mee, dus twee "
                "krachten van 5 newton kunnen samen 10, 0 of iets ertussen geven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-trillingen-golven-en-geluid-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie grootheden bij een trilling, en één formule: de frequentie is één gedeeld "
                   "door de periode. Hou amplitude en frequentie goed apart.",
            waarom=[
                None,
                "Let erop dat je deelt: één gedeeld door de periode. Een halve seconde geeft dus 2 "
                "hertz en niet 0,5; bij een periode onder één seconde is de frequentie altijd groter "
                "dan één.",
                "Niet waar: amplitude en frequentie staan los van elkaar. Een gitaarsnaar harder "
                "aanslaan maakt het geluid luider maar niet hoger.",
                "Noem alle drie, zoals gevraagd. De evenwichtslijn wordt het vaakst vergeten, en "
                "toch meet je de amplitude juist daarvanaf.",
            ],
        ),
        dict(
            aanpak="Resonantie is een kwestie van timing: de duw komt telkens op het juiste moment. "
                   "Hou de eigenfrequentie vast als het woord dat de hele reeks draagt.",
            waarom=[
                None,
                "Noem beide delen: de frequenties moeten samenvallen, en elke duw komt op het "
                "juiste moment. Dat tweede verklaart waarom de uitwijking blijft oplopen.",
                "Noem drie voorbeelden, zoals gevraagd. De schommel is het duidelijkste, want "
                "daar voel je zelf dat het ritme moet kloppen.",
            ],
        ),
        dict(
            aanpak="Eén formule voor de hele reeks: de snelheid is de golflengte maal de frequentie. "
                   "Hou daarnaast vast dat de deeltjes zelf op hun plaats blijven.",
            waarom=[
                "Let erop dat je vermenigvuldigt. Een golflengte in meter maal een frequentie in "
                "hertz geeft meter per seconde, en de eenheden tonen dus zelf dat het klopt.",
                "Let op het verschil: bij geluid trillen de deeltjes in de richting van de golf, bij "
                "een touw erop dwars. Longitudinaal is in de lengte, transversaal is dwars.",
                "Niet waar: de deeltjes trillen om hun plaats en verhuizen niet. Dat is precies wat "
                "de volgende vraag met het stadion laat zien.",
                "Noem dat de mensen blijven zitten en de beweging reist. Dat beeld is de kern van "
                "het hoofdstuk: een golf vervoert energie en geen materie.",
                "Noem beide helften: geluid heeft een middenstof nodig, licht niet. Mechanisch "
                "tegenover elektromagnetisch is het verschil dat de vraag zoekt.",
            ],
        ),
        dict(
            aanpak="Hou drie paren vast: hoog of laag is frequentie, luid of zacht is amplitude, en "
                   "het verschil tussen een viool en een fluit is de klankkleur.",
            waarom=[
                "Let erop dat toonhoogte en luidheid elk hun eigen grootheid hebben. Dat is dezelfde "
                "gedachte als bij de eerste reeks.",
                None,
                "Niet waar: infrasoon ligt onder de 20 hertz, dus lager dan wij horen. Boven de "
                "20 000 hertz heet het ultrasoon, en dat is wat een vleermuis gebruikt.",
                "Let erop dat geluid in een vaste stof het snelst gaat: de deeltjes liggen daar het "
                "dichtst bij elkaar en geven de trilling sneller door. In lucht is het het traagst "
                "van de drie.",
                "Noem beide eigenschappen, want de vraag geeft er ook twee: laag gaat over de "
                "frequentie, zacht over de amplitude.",
            ],
        ),
        dict(
            aanpak="De decibelschaal is geen gewone schaal: ze telt in stappen van tien in plaats "
                   "van in gelijke stukken. Daardoor is dubbel zo veel intensiteit maar 3 decibel "
                   "meer.",
            waarom=[
                "Let op het verschil tussen de twee regels: twee keer zo ver geeft vier keer minder "
                "intensiteit, dus ongeveer 6 decibel minder. Twee keer meer intensiteit is 3 "
                "decibel meer.",
                None,
                "Niet waar: twee keer de intensiteit is ongeveer 3 decibel meer. Wie de decibel als "
                "een gewone schaal leest, schat het gevaar van luide muziek stelselmatig verkeerd "
                "in.",
                "Noem de haarcellen en noem dat ze niet teruggroeien. Daar zit de reden dat "
                "gehoorschade blijvend is, en dat is het hele punt van deze vraag.",
                "Noem alle drie, zoals gevraagd. Let erop dat afstand en tijd even veel helpen als "
                "oordopjes: alle drie werken ze samen.",
            ],
        ),
        dict(
            aanpak="Drie toepassingen, en bij elk hetzelfde beginsel: geluid uitsturen, de "
                   "terugkaatsing opvangen, en uit de tijd de afstand berekenen.",
            waarom=[
                None,
                "Noem drie toepassingen, zoals gevraagd. Dat een vleermuis hetzelfde doet als een "
                "sonar is een mooi verband tussen biologie en fysica.",
                "Noem allebei: hoe ze werkt en dat er geen straling bij komt. Dat tweede is wat haar "
                "van een röntgenfoto onderscheidt en waarom ze bij een zwangerschap mag.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-elektromagnetisch-spectrum-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Leer het spectrum als één rij van radio tot gamma. Links grote golven met weinig "
                   "energie, rechts kleine golven met veel energie, en het zichtbare licht ergens in "
                   "het midden.",
            waarom=[
                "Let erop dat het zichtbare licht maar een heel smalle strook is in het midden van "
                "de hele rij. Alles wat we zien, zit tussen infrarood en ultraviolet.",
                None,
                "Niet waar: in vacuüm gaan alle elektromagnetische golven even snel, met de "
                "lichtsnelheid. Het verschil zit in de golflengte en de energie, niet in de "
                "snelheid.",
                "Noem allebei: kleine golflengte en veel energie. Frequentie, golflengte en energie "
                "hangen vast aan elkaar, dus met één gegeven ken je de twee andere.",
            ],
        ),
        dict(
            aanpak="Ioniserend betekent dat de golf genoeg energie heeft om een elektron uit een "
                   "atoom te slaan. Dat begint pas bij de hoogenergetische uv; alles links daarvan "
                   "is het niet.",
            waarom=[
                "Let op de gsm: radiogolven zijn niet ioniserend, want hun energie per golf is veel "
                "te klein. Dat is een punt waarover veel verkeerde verhalen rondgaan.",
                "Let op de grens bij uv: het hoogenergetische deel is ioniserend, infrarood en "
                "microgolven niet. De grens ligt dus middenin het ultraviolet.",
                "Noem de energie per golf. Daar zit het verschil: niet de hoeveelheid licht maar de "
                "energie van elke golf afzonderlijk beslist of er schade kan zijn.",
                "Niet waar: radiogolven en zichtbaar licht zijn dat niet. Schadelijk of niet hangt "
                "van de energie en van de dosis af, en niet van het woord straling.",
            ],
        ),
        dict(
            aanpak="Drie dingen kunnen er met straling gebeuren: opgenomen, doorgelaten of "
                   "teruggekaatst. De kleur van gras en een röntgenfoto zijn allebei toepassingen "
                   "daarvan.",
            waarom=[
                "Noem alle drie, zoals gevraagd. Met die drie woorden los je de rest van de reeks op.",
                "Noem allebei: het groene licht kaatst terug en de rest wordt opgenomen. Wat je ziet, "
                "is dus wat de plant niet gebruikt.",
                "Noem dat het bot meer absorbeert. Een röntgenfoto is een schaduwbeeld, en de witte "
                "plekken zijn precies waar de straling niet doorraakte.",
                None,
            ],
        ),
        dict(
            aanpak="Negen toepassingen, elk met één soort straling. Een hulpje: warmte is infrarood, "
                   "doorkijken is röntgen, draadloos is radio, en doden of steriliseren is gamma of "
                   "uv.",
            waarom=[
                "Let erop dat een bagagescanner met röntgen werkt en niet met gamma. Daarom staat "
                "zo'n toestel achter zware gordijnen en loodplaten.",
                None,
                "Let op de magnetron en de radiotherapie: twee heel verschillende soorten. "
                "Microgolven warmen op, gamma doodt cellen, en dat verschil is de energie per golf.",
                "Niet waar: een blacklight werkt met ultraviolet. Daarom licht wasmiddel op onder "
                "zo'n lamp, en daarom gebruikt men hem om vals geld te bekijken.",
            ],
        ),
        dict(
            aanpak="Hier moet je zelf kiezen. Lees de drie gegevens in de vraag en zoek de plaats in "
                   "het spectrum waar ze alle drie samenvallen.",
            waarom=[
                "Let erop dat er meerdere antwoorden goed zijn. De vraag vraagt welke het kan zijn, "
                "en alle drie de soorten aan de lange kant passen.",
                "Noem allebei: welke straling en waarom licht niet. Dat tweede deel is de "
                "verantwoording die de vraag vraagt.",
                None,
                "Noem de kooi van Faraday met naam. Dat is hetzelfde beginsel als in het hoofdstuk "
                "over elektrostatica, en hier houdt de kooi de golven juist binnen.",
            ],
        ),
        dict(
            aanpak="Drie woorden volstaan voor stralingsbescherming: afscherming, afstand en tijd. "
                   "Noem ze in die orde, dan vergeet je er geen.",
            waarom=[
                None,
                "Noem alle drie, zoals gevraagd. Afstand en tijd kosten niets en werken even goed als "
                "een loodschort, en juist die twee worden het vaakst vergeten.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-kernfysica-en-radioactiviteit-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Drie letters volstaan: Z is het aantal protonen, A is protonen plus neutronen, "
                   "en N is het verschil. Trek dus af om de neutronen te vinden.",
            waarom=[
                "Let erop dat je A min Z rekent en niet omgekeerd. Het massagetal is altijd het "
                "grootste van de twee.",
                "Let op de tweede: hier tel je op in plaats van af, want je zoekt A. Lees dus eerst "
                "wat gegeven is en wat gevraagd.",
                None,
                "Noem allebei: wat gelijk is en wat verschilt. Isotopen van hetzelfde element staan "
                "op dezelfde plaats in het periodiek systeem en hebben een andere massa.",
            ],
        ),
        dict(
            aanpak="In een kern strijden twee krachten. Hou vast dat de kernkracht sterker is maar "
                   "heel kort reikt, en de afstoting zwakker is maar verder werkt.",
            waarom=[
                "Noem van beide krachten ook het bereik. Dat verschil in afstand is wat verklaart "
                "waarom er een grens is aan hoe groot een stabiele kern kan zijn.",
                "Niet waar, en het is net omgekeerd: zware stabiele kernen hebben meer neutronen. De "
                "volgende vraag vraagt waarom.",
                "Noem dat neutronen de afstoting verdunnen en de kernkracht helpen. Twee effecten in "
                "één deeltje, en dat is het hele antwoord.",
                "Noem allebei: welk verval en waarom dat helpt. Bij bètaverval wordt een neutron een "
                "proton, dus verandert juist de verhouding die fout zat.",
                "Niet waar: stabiel betekent dat de kern niet vervalt. Veel stoffen rondom je zijn "
                "stabiel en blijven dat.",
            ],
        ),
        dict(
            aanpak="Reken met halveringen in plaats van met formules: deel telkens door twee en tel "
                   "hoeveel keer dat moet. Deel de verstreken tijd door de halveringstijd om te "
                   "weten hoeveel keer.",
            waarom=[
                "Let op de eerste: 15 jaar gedeeld door 5 jaar is drie halveringen, dus 800 wordt "
                "400, dan 200, dan 100. Wie één stap vergeet, antwoordt 200.",
                "Let erop dat een achtste gelijk is aan de helft van de helft van de helft. Een "
                "zestiende zou vier halveringstijden zijn.",
                "Noem dat dezelfde hoeveelheid in minder tijd vervalt. Activiteit is het aantal "
                "vervallen per seconde, dus is een korte halveringstijd een hoge activiteit.",
                "Noem ook het bijzondere, zoals de vraag vraagt: je mag van elk punt vertrekken. Dat "
                "is wat een exponentiële afname kenmerkt.",
            ],
        ),
        dict(
            aanpak="Fusie en splijting bewegen van twee kanten naar hetzelfde midden. Hou dat beeld "
                   "van de nuclidenkaart vast, dan is de tegenstrijdigheid geen tegenstrijdigheid.",
            waarom=[
                None,
                "Noem het midden van de nuclidenkaart en noem het massaverschil. Zonder dat midden "
                "klinkt het antwoord inderdaad tegenstrijdig.",
                "Let erop dat de regelstaven neutronen wegvangen. Ze remmen dus niet de kernen maar "
                "de neutronen die de volgende splijting moeten starten.",
                "Noem beide kenmerken en noem wat categorie A is, zoals de vraag twee dingen vraagt.",
            ],
        ),
        dict(
            aanpak="Drie soorten straling, met drie vragen bij elk: wat is het, wat houdt het tegen, "
                   "en wat verandert er in de kern?",
            waarom=[
                "Let op de drie schermen: papier, aluminium, lood. Dat rijtje volgt de energie, en "
                "het hoort bij de bescherming uit het vorige hoofdstuk.",
                "Let op bètaverval: A blijft gelijk en Z gaat één omhoog, want een neutron wordt een "
                "proton. Bij alfaverval verlies je een hele heliumkern.",
                "Noem beide vermogens: klein doordringend, groot ioniserend. Dat onderscheid is de "
                "kern van deze vraag, en het verklaart waarom radon in een huis gevaarlijk is.",
                "Niet waar: gammastraling buigt helemaal niet af, want ze heeft geen lading. "
                "Bètastraling buigt het sterkst van de drie.",
                "Noem van beide stralingen de reden. De lading beslist of er een kracht is, de massa "
                "beslist hoe sterk het effect is.",
            ],
        ),
        dict(
            aanpak="Hou twee paren apart: bestraling tegenover besmetting, en gray tegenover "
                   "sievert. De gray meet de energie, de sievert meet de schade.",
            waarom=[
                "Noem van beide wat er achterblijft. Bij bestraling niets, bij besmetting de stof "
                "zelf, en dat is waarom men zich na een besmetting wast.",
                "Let erop dat dezelfde dosis in gray een andere waarde in sievert geeft, afhankelijk "
                "van de soort straling. Daarvoor dient de weegfactor.",
                "Noem dat ze haar energie in een klein stukje weefsel afgeeft. Dat is dezelfde reden "
                "als bij de vraag over de huid, nu in een getal uitgedrukt.",
                "Noem drie toepassingen, zoals gevraagd, uit verschillende hoeken: behandelen, "
                "dateren en in beeld brengen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-en-duurzaam-werken-grootheden-en-eenheden-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Op een etiket staan drie dingen: een beeld van het gevaar, een H-zin over wat er "
                   "kan gebeuren, en een P-zin over wat jij moet doen. H van hazard, P van "
                   "precaution.",
            waarom=[
                "Let erop dat het pictogram je in één beeld de aard van het gevaar geeft, nog voor "
                "je de zinnen leest. De H- en P-zinnen maken daarna concreet wat er kan gebeuren en "
                "wat jij doet.",
                "Noem drie dingen, zoals gevraagd, en noem de P-zinnen erbij. Die staan op het "
                "etiket zelf, dus je hoeft ze niet te kennen; je moet ze lezen.",
            ],
        ),
        dict(
            aanpak="Bij elke regel is de vraag dezelfde: wat kan er misgaan voor jou, voor iemand "
                   "anders of voor het milieu? Daaruit volgt wat je doet.",
            waarom=[
                None,
                "Niet waar: chemisch afval hoort in het juiste afvalvat. In de gootsteen komt het in "
                "het water terecht, en soms reageert het ook nog met iets anders in de leiding.",
                "Noem het blik en het glasvat, en noem dat je het niet met je handen doet. Dat "
                "laatste is waar de vraag naar zoekt.",
                "Noem drie werkwijzen, zoals gevraagd. Let erop dat duurzaam hier ook over energie "
                "en over zuinig doseren gaat, niet enkel over afval.",
            ],
        ),
        dict(
            aanpak="Bij meten horen drie vragen: welk instrument, welk meetbereik, en hoe fijn. Een "
                   "instrument moet passen bij wat je meet, niet zo fijn mogelijk zijn.",
            waarom=[
                None,
                "Let op het verschil tussen meetbereik en nauwkeurigheid: het eerste zegt tussen "
                "welke waarden je kan meten, het tweede hoe fijn. Een weegschaal tot 100 kilogram "
                "kan heel grof zijn.",
                "Noem dat het instrument bij de meting moet passen. Eén stap fijner dan wat je nodig "
                "hebt is de regel, en dat is het antwoord op het tweede deel van de vraag.",
                "Noem de kijkhoek. Die fout heet parallax, en ze is een systematische fout: ze zit "
                "elke keer dezelfde kant op.",
                "Noem dat je meer cijfers opschrijft dan je kan meten. Een getal zegt ook iets over "
                "hoe nauwkeurig je gemeten hebt, en dat is wat beduidende cijfers bedoelen.",
            ],
        ),
        dict(
            aanpak="Reken met de macht van tien die bij het voorvoegsel hoort. Van een groot "
                   "voorvoegsel naar de basiseenheid maak je het getal groter, van een klein "
                   "voorvoegsel kleiner.",
            waarom=[
                "Let op de milliseconde: milli is duizend keer kleiner, dus komen er drie nullen bij "
                "voor de komma van het getal. Reken na door het antwoord weer terug te zetten.",
                "Let op nano en micro: een nanometer is duizend keer kleiner dan een micrometer. Dat "
                "is dezelfde maat als bij de nanomaterialen, en 250 nanometer is dus een kwart "
                "micrometer.",
                None,
                "Let erop dat de kilogram de SI-eenheid is en niet de gram. Dat is het enige "
                "voorvoegsel dat in een basiseenheid zelf zit.",
            ],
        ),
        dict(
            aanpak="In de wetenschappelijke notatie staat er altijd één cijfer voor de komma. De "
                   "exponent zegt hoeveel plaatsen de komma opschuift, met een minteken bij een "
                   "klein getal.",
            waarom=[
                "Let op het teken van de exponent: onder één wordt hij negatief, boven tien "
                "positief. Tel de plaatsen tot achter het eerste cijfer dat niet nul is.",
                "Noem dat de minst nauwkeurige meting beslist. Dat is de regel bij optellen, en ze "
                "verrast omdat je er een cijfer bij weggooit.",
                "Niet waar: een rekenmachine toont cijfers die je nooit gemeten hebt. Zij weet niet "
                "met welk toestel je gewerkt hebt, dus moet jij het resultaat afronden.",
                "Noem dat een rekenmachine ook een tikfout keurig uitrekent. Een schatting is je "
                "enige controle, en ze kost maar een paar seconden.",
            ],
        ),
        dict(
            aanpak="Drie verbanden met elk hun beeld: een rechte door de oorsprong, een parabool, en "
                   "een kromme waarvan het product gelijk blijft. Bij het omvormen deel je altijd "
                   "door de factor die je kwijt wil.",
            waarom=[
                None,
                "Noem de oorsprong, want daar zit het hele verschil. Recht evenredig is een strenger "
                "begrip dan lineair: elke recht evenredige grafiek is lineair, niet omgekeerd.",
                "Let erop dat je bij de eerste twee door een andere factor deelt. Reken na door je "
                "antwoord in de oorspronkelijke formule te zetten.",
                "Noem alle drie, zoals gevraagd. Een goede oefening is om hetzelfde verband in de "
                "drie vormen naast elkaar te zetten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-onderzoeksvaardigheden-en-ontwerpen-beyond"] = dict(
    reeksen=[
        dict(
            aanpak="Vijf stappen in een vaste orde: probleem, hypothese, plan, meten, besluiten. "
                   "Het denken komt dus voor het meten, en niet erna.",
            waarom=[
                "Let erop dat de hypothese voor het plan komt. Je bedenkt eerst wat je verwacht, en "
                "pas daarna hoe je dat gaat nagaan.",
                "Noem drie dingen, zoals gevraagd. Een plan is pas goed als iemand anders de proef "
                "met jouw plan in de hand kan overdoen.",
                "Niet waar: de vraag komt eerst. Wie achteraf een vraag bij zijn metingen zoekt, "
                "vindt bijna altijd de vraag die het best bij het resultaat past, en dat is geen "
                "onderzoek meer.",
            ],
        ),
        dict(
            aanpak="Een goede onderzoeksvraag heeft twee dingen: iets dat je zelf verandert en iets "
                   "dat je kan meten. Mis je een van de twee, dan is de vraag niet bruikbaar.",
            waarom=[
                "Let op de twee foute: lekker is niet meetbaar, en hoe werkt een plant is te breed. "
                "Dat zijn de twee klassieke fouten, elk van een andere soort.",
                "Noem een meetbare uitkomst en een grootheid die jij regelt, zoals in het antwoord. "
                "Een getal en een eenheid in je vraag zijn het beste teken dat ze goed is.",
                "Noem dat je nu iets weet wat je eerst niet wist. Een weerlegde hypothese is een "
                "resultaat, en je mag ze dus nooit achteraf aanpassen aan je metingen.",
            ],
        ),
        dict(
            aanpak="Bij elke proef drie vragen: wat verander ik, wat meet ik, en wat hou ik gelijk? "
                   "Dat derde is het langste lijstje en het belangrijkste.",
            waarom=[
                None,
                "Let op de manier van loslaten: ook dat moet gelijk blijven. Wie de bal de ene keer "
                "een duwtje geeft, meet niet meer de ondergrond.",
                None,
                "Noem dat je toevallige fouten uitvlakt. Een systematische fout verdwijnt daar niet "
                "mee; die blijft elke keer dezelfde kant op zitten.",
                "Niet waar: een meting weglaten omdat ze niet past, is het resultaat vervalsen. "
                "Vermeld ze, en zeg wat je erover denkt.",
            ],
        ),
        dict(
            aanpak="Van cijfers naar een besluit in drie stappen: zet ze in een grafiek, benoem het "
                   "verband, en antwoord dan op je eigen vraag.",
            waarom=[
                "Noem dat je een verband sneller ziet dan rekent. Dat is de reden, en het is ook "
                "waarom een grafiek in elk verslag hoort.",
                None,
                "Noem alle drie, zoals gevraagd. Het derde wordt het vaakst vergeten: een conclusie "
                "zegt uitdrukkelijk of de hypothese klopte.",
                "Noem van beide iets, want de vraag vraagt twee keer waarom. Dat anderen je werk "
                "kunnen nakijken, is de kern van wetenschap.",
            ],
        ),
        dict(
            aanpak="Ontwerpen loopt in een kring en niet in een rechte lijn: probleem, criteria, "
                   "deelproblemen, en dan evalueren en opnieuw. Hou die kring vast.",
            waarom=[
                "Let erop dat de criteria voor het splitsen komen. Zonder criteria weet je niet "
                "waarop je de delen moet beoordelen.",
                "Noem drie vragen, zoals gevraagd, uit verschillende hoeken: maat, geld en "
                "veiligheid of duurzaamheid.",
                "Niet waar: na de eerste versie komt het evalueren en bijsturen. Juist dat maakt "
                "ontwerpen een kring in plaats van een rechte lijn.",
                "Noem beide stappen: bijsturen en daarna opnieuw aan alle criteria toetsen. Een "
                "goedkopere oplossing mag niet op een ander criterium stuklopen.",
                "Noem dat je elk criterium apart vergelijkt. Zo wordt de keuze een afweging en geen "
                "gevoel.",
            ],
        ),
        dict(
            aanpak="STEM is geen vak maar een samenwerking. Noem bij elke vraag van elke letter wat "
                   "ze bijdraagt, dan is je antwoord volledig.",
            waarom=[
                None,
                "Noem er drie, zoals gevraagd, en verdeel ze over de letters. Zo laat je zien dat de "
                "disciplines samen werken en niet na elkaar.",
                "Noem ook het verdelen en niet enkel het maken. Dat de koeling en de logistiek even "
                "beslissend waren als het vaccin zelf, is precies wat deze vraag toetst.",
                "Geef voor elke richting een voorbeeld, zoals de vraag vraagt. Eén voorbeeld geven "
                "is hier maar de helft van het antwoord.",
                "Noem het verschil in één zin: een vraag beantwoorden tegenover een probleem "
                "oplossen. Dat onderscheid loopt door de hele bundel.",
            ],
        ),
    ],
)
