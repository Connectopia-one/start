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
                 ("kort", "Een kubusvormige cel heeft een zijde van 2 mm. Hoe groot is haar volume?",
                  "8 mm³", "90px"),
                 ("kort", "Hoe groot is de totale oppervlakte van die kubus (6 vlakken)?",
                  "24 mm²", "90px"),
                 ("open", "Verdubbel je de zijde tot 4 mm, dan wordt het volume 64 mm³ en de "
                          "oppervlakte 96 mm². Wat gebeurt er met de verhouding oppervlakte op volume, "
                          "en waarom zet dat een grens op de grootte van een cel?",
                  "Ze zakt van 3 naar 1,5. Een grote cel heeft dus per eenheid volume te weinig "
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
                  "6 CO2 + 6 H2O geeft C6H12O6 + 6 O2", WL),
                 ("kort", "Schrijf de reactievergelijking van de aerobe celademhaling.",
                  "C6H12O6 + 6 O2 geeft 6 CO2 + 6 H2O en energie", WL),
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
                  "vanaf ongeveer 24 weken", WW),
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
                 ("open", "In een stuk DNA is 24 procent van de basen guanine. Hoeveel procent is "
                          "adenine?",
                  "Guanine en cytosine zijn elk 24 procent, samen 48. Voor adenine en thymine blijft "
                  "52 procent over, gelijk verdeeld, dus 26 procent adenine.", 3),
                 ("open", "In een ander stuk is 35 procent thymine. Hoeveel procent is cytosine?",
                  "Thymine en adenine zijn elk 35 procent, samen 70. Voor guanine en cytosine blijft "
                  "30 procent over, dus 15 procent cytosine.", 3),
             ]),
        dict(kop="Van DNA tot chromosoom",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("eiwitten waar het DNA rond rolt", "histonen"),
                          ("DNA en eiwit in een niet-delende kern", "chromatine"),
                          ("de insnoering van een chromosoom", "centromeer")], None, WW),
                 ("kort", "Hoeveel chromosomen heeft een menselijke lichaamscel?", "46", "70px"),
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
                  "Het polymerase kan maar in één richting werken, van 5 naar 3, en de twee oude "
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
                 ("kort", "Aa × Aa: welke genotypische verhouding?", "1 op 2 op 1", WW),
                 ("kort", "Aa × Aa: welke fenotypische verhouding?", "3 op 1", WW),
                 ("kort", "Aa × aa: hoeveel procent toont het recessieve kenmerk?",
                  "50 procent", WW),
                 ("kort", "AA × aa: hoeveel procent toont het recessieve kenmerk?",
                  "0 procent", WW),
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
                  "1 rood, 2 roze, 1 wit. Dus 25 procent rood, 50 procent roze en 25 procent wit.", 3),
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
                 ("kort", "AaBb × AaBb: welke fenotypische verhouding?", "9 op 3 op 3 op 1", WW),
                 ("kort", "AaBb × aabb: welke fenotypische verhouding?", "1 op 1 op 1 op 1", WW),
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
                 ("kort", "2 mol A met 5 mol B, reactie één op één. Welke stof is in overmaat?",
                  "stof B", W),
                 ("kort", "Hoeveel mol B blijft er dan over?", "3 mol", W),
                 ("kort", "3 mol A met 3 mol B, reactie één op twee (A : B). Welke stof is "
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
                 ("open", "Een gasevenwicht heeft links 3 mol gas en rechts 2 mol gas. Je perst het "
                          "mengsel in een kleiner vat. Welke kant schuift het op, en waarom?",
                  "Naar rechts, naar de kant met minder gasdeeltjes. Zo neemt het mengsel minder plaats "
                  "in en werkt het de drukverhoging tegen.", 3),
                 ("open", "Een ander gasevenwicht heeft links 2 mol gas en rechts 2 mol gas. Wat "
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
                 ("rij", [("CH3CH2OH", "alcoholen"), ("CH3COOH", "carbonzuren"),
                          ("CH3COCH3", "ketonen")], None, WW),
                 ("rij", [("C4H10", "alkanen"), ("HCHO", "aldehyden"),
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
                 ("open", "Iemand zet CHCl3 bij de alcoholen. Verbeter en verantwoord.",
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
                          ("CCl4", "apolair")], None, W),
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
                          ("azijnzuur", "CH3COOH")], None, WW),
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
                  "1 en 100 nanometer", WW),
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
                          ("met afvang en opslag van CO2", "blauw"),
                          ("met hernieuwbare stroom", "groen")], "Welke waterstof?", W),
                 ("kort", "Wat is grijs water?",
                  "licht vervuild water van bad, lavabo of wasmachine", WL),
                 ("waar", "Een CO2-neutraal proces neemt meer CO2 op dan het uitstoot.", False),
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
                 ("open", "Twee identieke metalen bollen, de ene met 8 eenheden lading en de andere "
                          "neutraal, raken elkaar even aan. Hoeveel houdt elke bol?",
                  "Elk 4 eenheden: de lading verdeelt zich gelijk over twee identieke bollen.", 3),
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
                 ("rij", [("een auto aan 50 km per uur op een rechte weg", "ERB"),
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
        dict(kop="Rekenen met F = m·a",
             opdracht="Reken uit en schrijf je stappen op.",
             oefeningen=[
                 ("rij", [("m = 4 kg, F = 12 N", "3 m/s²"), ("m = 2 kg, F = 10 N", "5 m/s²"),
                          ("m = 5 kg, F = 20 N", "4 m/s²")], "Hoe groot is a?", W),
                 ("rij", [("m = 3 kg, a = 2 m/s²", "6 N"), ("m = 0,5 kg, a = 8 m/s²", "4 N"),
                          ("F = 18 N, a = 3 m/s²", "6 kg")], None, W),
                 ("open", "Een vrachtwagen en een auto krijgen dezelfde kracht. Waarom versnelt de "
                          "vrachtwagen minder?",
                  "Zijn massa is groter, en in F = m·a zijn massa en versnelling omgekeerd verbonden: bij "
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
                 ("rij", [("periode 0,5 s", "2 Hz"), ("periode 0,25 s", "4 Hz"),
                          ("periode 2 s", "0,5 Hz")], "Welke frequentie?", W),
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
                 ("rij", [("golflengte 2 m, frequentie 5 Hz", "10 m/s"),
                          ("golflengte 0,5 m, frequentie 8 Hz", "4 m/s"),
                          ("golflengte 3 m, frequentie 2 Hz", "6 m/s")], "Hoe snel?", W),
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
                  "van 20 tot 20 000 Hz", WW),
                 ("waar", "Infrasoon geluid heeft een hogere frequentie dan wat wij kunnen horen.",
                  False),
                 ("kort", "In welke middenstof gaat geluid het snelst?", "in een vaste stof", WW),
                 ("open", "Je hoort een lage, zachte toon. Wat weet je over de golf?",
                  "Dat ze een lage frequentie en een kleine amplitude heeft.", 2),
             ]),
        dict(kop="De decibelschaal",
             opdracht="Reken en antwoord.",
             oefeningen=[
                 ("rij", [("twee keer zo ver van de bron", "ongeveer 6 dB minder"),
                          ("de intensiteit twee keer groter", "ongeveer 3 dB meer")], None, WL),
                 ("rij", [("de gehoordrempel", "0 dB"), ("gehoorbescherming nodig vanaf", "80 dB"),
                          ("de pijndrempel", "120 dB")], None, W),
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
                 ("rij", [("A = 23, Z = 11", "12 neutronen"), ("A = 40, Z = 19", "21 neutronen"),
                          ("A = 14, Z = 6", "8 neutronen")], "Hoeveel neutronen?", WW),
                 ("rij", [("A = 12, Z = 6", "6 protonen"), ("Z = 92, N = 146", "A = 238"),
                          ("A = 4, Z = 2", "2 neutronen")], None, WW),
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
                 ("rij", [("800 kernen, T = 5 jaar, na 15 jaar", "100"),
                          ("640 kernen, T = 2 uur, na 6 uur", "80"),
                          ("1000 kernen, na 2 halveringstijden", "250")], "Hoeveel blijft er over?",
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
                 ("rij", [("alfaverval", "A min 4, Z min 2"),
                          ("bètaverval", "A gelijk, Z plus 1")], None, WL),
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
                  "Radiotherapie tegen kanker, de koolstof-14-methode om ouderdom te bepalen, en een "
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
                 ("open", "Je moet ongeveer 2 gram wegen, op een tienden van een gram nauwkeurig. Welke "
                          "balans kies je, en waarom niet gewoon de duurste?",
                  "Een balans die tot op 0,01 gram weegt, dus één stap fijner dan wat je nodig hebt. Een "
                  "duurder instrument is niet altijd het beste: het moet passen bij wat je meet.", 4),
                 ("open", "Waarom lees je een vloeistofniveau in een maatcilinder op ooghoogte af?",
                  "Om een fout door de kijkhoek te vermijden.", 2),
                 ("open", "Je meet met een lintmeter in centimeters en schrijft 12,3456 cm op. Wat is "
                          "daar fout aan?",
                  "Je schrijft meer cijfers op dan je kan meten. Een lintmeter geeft geen tienduizendsten "
                  "van een centimeter.", 3),
             ]),
        dict(kop="Omzetten",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("2,5 km", "2500 m"), ("0,25 ms", "0,00025 s"),
                          ("3 mg", "0,003 g")], None, WW),
                 ("rij", [("4 MW", "4 000 000 W"), ("250 nm", "0,00000025 m"),
                          ("12 µm", "0,000012 m")], None, WW),
                 ("rij", [("mega", "een miljoen"), ("micro", "een miljoenste"),
                          ("nano", "een miljardste")], "Welke factor?", WW),
                 ("kort", "Wat is de SI-eenheid van massa?", "de kilogram", WW),
             ]),
        dict(kop="Wetenschappelijke notatie en beduidende cijfers",
             opdracht="Schrijf om en antwoord.",
             oefeningen=[
                 ("rij", [("0,00042 m", "4,2 · 10⁻⁴ m"), ("35 000 m", "3,5 · 10⁴ m"),
                          ("0,0071 s", "7,1 · 10⁻³ s")], None, WW),
                 ("open", "Je meet 3,0 cm en 4,00 cm en telt die op. Met hoeveel cijfers na de komma "
                          "schrijf je het resultaat, en waarom?",
                  "Met één cijfer na de komma, dus 7,0 cm. De minst nauwkeurige meting bepaalt het "
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
                 ("rij", [("F = m · a, zoek m", "m = F / a"), ("F = m · a, zoek a", "a = F / m"),
                          ("v = s / t, zoek t", "t = s / v")], None, WW),
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
                 ("open", "Herschrijf \"Groeien planten beter met muziek?\" tot een goede "
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
