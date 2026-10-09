# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij samenleving en economie 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen, dus dezelfde pdf gaat bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere gevallen om in te delen, andere bedragen om te rekenen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een keuze
verantwoorden, een verschil in eigen woorden opschrijven). Wie hier iets
bijschrijft, legt het eerst naast `../../beyond/samenleving-en-economie.json`.

Drie dingen die vastliggen en die je niet mag verzinnen: de lijstjes van de
overheidsinkomsten en -uitgaven, de noodnummers (101, 112, 070 245 245 en
1733) en de stappen van de eerste hulp en de reanimatie. Staat een getal in
de fiche, dan staat het hier net zo.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-beyond-doorstroom": het voorvoegsel omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden, het achtervoegsel omdat
`niveauUitBestandsnaam` daarmee de categorie van het hoofdstuk terugvindt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Samenleving en economie"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een berekening: schrijf de bewerking op, niet alleen het eindbedrag.",
    "Bij een keuze: zeg niet alleen wát je kiest, maar ook waaróm, met een begrip uit de leerstof.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-identiteit-de-lagen-de-factoren-en-het-wereldbeeld-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Identiteit: de lagen, de factoren en het wereldbeeld",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Relationeel, gelaagd of dynamisch?",
             opdracht="Schrijf bij elke uitspraak welk van de drie woorden erop past.",
             oefeningen=[
                 ("rij", [("Wie je bent, krijgt vorm in de omgang met anderen.", "relationeel"),
                          ("Een identiteit bestaat uit meerdere lagen samen.", "gelaagd")],
                  None, WL),
                 ("rij", [("Je identiteit kan in de loop van je leven veranderen.", "dynamisch"),
                          ("Je kleedt je anders dan vijf jaar geleden en voelt je anders.", "dynamisch")],
                  None, WL),
             ]),
        dict(kop="Welke laag?",
             opdracht="Vul de tabel aan. Schrijf per geval de laag van de persoonlijke of de groepsidentiteit.",
             oefeningen=[
                 ("tabel", ["Geval", "Welke laag"], [
                     ["Hamza is geboren met een hartafwijking.", None],
                     ["Lotte is van jongs af aan erg verlegen.", None],
                     ["Bram is de jongste van drie kinderen.", None],
                     ["Soraya noemt zich in de eerste plaats Europeaan.", None],
                     ["Jeroen zit in een skatescene met eigen taal en gebruiken.", None],
                 ], "biologische aspecten · persoonlijkheidstrekken · familiale achtergrond · "
                    "supranationaal aspect · subcultuur", WL),
             ]),
        dict(kop="Persoonlijk of groep?",
             opdracht="Kruis aan bij welke soort identiteit de laag hoort.",
             oefeningen=[
                 ("kies", "de familiale achtergrond", ["persoonlijke identiteit", "groepsidentiteit"], 0),
                 ("kies", "de subculturen waar je bij hoort", ["persoonlijke identiteit", "groepsidentiteit"], 1),
                 ("kies", "je persoonlijkheidstrekken", ["persoonlijke identiteit", "groepsidentiteit"], 0),
                 ("kies", "de levensbeschouwelijke groep waar je deel van uitmaakt",
                  ["persoonlijke identiteit", "groepsidentiteit"], 1),
             ]),
        dict(kop="Drie factoren",
             opdracht="Schrijf bij elke situatie of het gaat om verbondenheid, discriminatie of wij-zij-denken.",
             oefeningen=[
                 ("open", "Nora wordt op de sportclub nooit gekozen omdat ze een hoofddoek draagt.",
                  "discriminatie: ze wordt anders behandeld om een kenmerk van haar identiteit", 2),
                 ("open", "In een jeugdbeweging voelt Wout zich voor het eerst echt erkend zoals hij is.",
                  "verbondenheid: het gevoel ergens bij te horen en erkend te worden", 2),
                 ("open", "Een vereniging spreekt consequent over wij van de club en zij van het dorp.",
                  "wij-zij-denken: mensen indelen in een eigen groep en een andere groep, hier door de groep zelf", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Een identiteit ligt vast vanaf je geboorte.", False),
                 ("waar", "De fiche onderscheidt twee soorten identiteit.", True),
                 ("waar", "Wij-zij-denken komt altijd van buitenaf.", False),
                 ("waar", "Welke laag het meest bepalend is, verschilt van persoon tot persoon.", True),
                 ("waar", "Je mensbeeld en je wereldbeeld betekenen hetzelfde.", False),
                 ("waar", "De situaties op het examen zijn fictief.", True),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom de fiche identiteit relationeel noemt.",
                  "omdat wie je bent vorm krijgt in de omgang met de mensen rond je, en niet alleen bij jou vanbinnen", 3),
                 ("open", "Leg uit hoe discriminatie het wij-zij-denken kan versterken.",
                  "discriminatie breekt het gevoel van verbondenheid af; wie niet meer bij de groep hoort, "
                  "wordt tot de andere groep gerekend en gaat zich zo ook zelf zien", 3),
                 ("open", "Noem de twee redenen waarom de situaties op het examen fictief zijn.",
                  "zo blijft het neutraal en zijn persoonsgegevens beschermd", 2),
                 ("open", "Een wereldbeeld kan veranderen. Geef een voorbeeld van een gebeurtenis die "
                          "iemands wereldbeeld kan doen kantelen, en leg uit waarom.",
                  "een eigen antwoord, bijvoorbeeld een jaar in een ander land wonen of een ziekte doormaken: "
                  "wie iets heel anders meemaakt, gaat anders naar de wereld als geheel kijken", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-samenleven-in-diversiteit-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Samenleven in diversiteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke vorm van diversiteit?",
             opdracht="Schrijf bij elk geval welke van de vijf vormen erop past.",
             oefeningen=[
                 ("tabel", ["Geval", "Welke vorm"], [
                     ["In een ploeg spelen mensen met en zonder beperking samen.", None],
                     ["Twee leerlingen in dezelfde klas hebben heel verschillende financiële omstandigheden.", None],
                     ["In een vereniging zitten leden die katholiek, moslim, atheïst of zoekend zijn.", None],
                     ["Op een feest worden gewoonten en talen gemengd die niet iedereen kent.", None],
                     ["In een jeugdhuis komen koppels van verschillende samenstelling over de vloer.", None],
                 ], "lichaamsdiversiteit · sociale diversiteit · religieuze of levensbeschouwelijke "
                    "diversiteit · culturele diversiteit · seksuele diversiteit", WL),
             ]),
        dict(kop="Vijf begrippen",
             opdracht="Vul bij elke omschrijving het juiste begrip in.",
             oefeningen=[
                 ("rij", [("meerdere culturen die naast elkaar bestaan in één samenleving", "multiculturalisme"),
                          ("het idee dat één cultuur de norm is", "monoculturalisme")], None, WW),
                 ("rij", [("de nieuwkomer past zich aan de bestaande groep aan", "integratie"),
                          ("de groep past zich mee aan zodat iedereen echt kan meedoen", "inclusie"),
                          ("mensen buiten de groep houden", "exclusie")], None, WW),
             ]),
        dict(kop="Integratie of inclusie?",
             opdracht="Kruis aan, en schrijf er in één woord bij wie zich aanpast.",
             oefeningen=[
                 ("kies", "Een vereniging zegt tegen een nieuw lid dat het zich moet schikken naar de "
                          "bestaande gewoonten.", ["integratie", "inclusie"], 0),
                 ("kies", "Een school bouwt een hellend vlak en past de lessen aan zodat een leerling in "
                          "een rolstoel alles kan volgen.", ["integratie", "inclusie"], 1),
                 ("kies", "Een sportclub verplaatst de training omdat een deel van de leden anders nooit "
                          "kan komen.", ["integratie", "inclusie"], 1),
                 ("kies", "Een jeugdbeweging laat de regels zoals ze zijn en verwacht dat nieuwe leden "
                          "volgen.", ["integratie", "inclusie"], 0),
             ]),
        dict(kop="Voordeel of uitdaging?",
             opdracht="Schrijf bij elk geval of het bij de voordelen of bij de uitdagingen hoort, en noem het precies.",
             oefeningen=[
                 ("open", "Een vereniging vraagt elk nieuw lid om een idee voor het jaarprogramma.",
                  "voordeel: het uitwisselen van ideeën", 2),
                 ("open", "In een werkgroep stelt niemand nog iets anders voor omdat de voorzitter al een "
                          "richting gekozen heeft.", "uitdaging: groepsdenken", 2),
                 ("open", "De ene buurtbewoner wil een speeltuin op het pleintje, de andere parkeerplaatsen.",
                  "uitdaging: verschillende belangen", 2),
                 ("open", "Door een nieuwe handelspartner komen er in de straat producten te koop die er "
                          "nooit waren.", "voordeel: economische uitwisseling", 2),
                 ("open", "Twee ouders beoordelen dezelfde schoolregel heel anders omdat ze zelf heel "
                          "verschillende schooljaren meemaakten.", "uitdaging: verschillende referentiekaders", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Levensbeschouwelijke diversiteit gaat ook over wie niet gelooft.", True),
                 ("waar", "Groepsdenken is een van de voordelen van diversiteit.", False),
                 ("waar", "Inclusie en exclusie betekenen ongeveer hetzelfde.", False),
                 ("waar", "Culturele verrijking gaat over wat je erbij krijgt aan cultuur, niet over geld.", True),
                 ("waar", "Een meningsverschil is volgens de fiche een uitdaging, niet een probleem.", True),
                 ("waar", "De fiche noemt vier voordelen van diversiteit.", False),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg het verschil uit tussen integratie en inclusie, met de vraag wie zich aanpast.",
                  "bij integratie past de nieuwkomer zich aan de bestaande groep aan; bij inclusie verandert "
                  "de omgeving zelf mee zodat iedereen echt kan meedoen", 3),
                 ("open", "Leg uit wat een referentiekader is en waarom twee mensen dezelfde situatie anders "
                          "kunnen zien.",
                  "een referentiekader is het geheel van ervaringen en waarden waarmee je iets beoordeelt; "
                  "wie van een ander kader vertrekt, komt bij dezelfde situatie tot een ander oordeel", 3),
                 ("open", "Het leerdoel vraagt de twee kanten samen. Noem één manier waarop diversiteit "
                          "verrijkend is en één waarop ze uitdagend is, in dezelfde situatie.",
                  "een eigen antwoord met één voordeel en één uitdaging uit dezelfde situatie, bijvoorbeeld "
                  "een vereniging die rijker wordt aan ideeën en tegelijk vaker botst op verschillende belangen", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-respectvol-samenleven-communicatie-grenzen-en-samenwerken-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Respectvol samenleven: communicatie, grenzen en samenwerken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Constructief of destructief?",
             opdracht="Kruis aan. Schrijf bij een destructieve uitspraak in één regel hoe het constructief kon.",
             oefeningen=[
                 ("kies", "Ik begrijp dat je dit anders ziet, maar ik maak me zorgen over het tijdstip.",
                  ["constructief", "destructief"], 0),
                 ("kies", "Jij snapt er nooit iets van, hou er maar over op.",
                  ["constructief", "destructief"], 1),
                 ("kies", "Ik wil het er graag over hebben, maar niet nu voor de hele groep.",
                  ["constructief", "destructief"], 0),
                 ("kies", "Iedereen vindt jouw voorstel belachelijk, vraag het maar na.",
                  ["constructief", "destructief"], 1),
             ]),
        dict(kop="Vier soorten situaties",
             opdracht="Schrijf bij elke situatie of het pestgedrag, uitsluiting, discriminatie of racisme is.",
             oefeningen=[
                 ("tabel", ["Situatie", "Wat het is"], [
                     ["Yara wordt in een groepschat elke dag belachelijk gemaakt om haar stem.", None],
                     ["Eén speler wordt nooit uitgenodigd voor de gesprekken en de activiteiten.", None],
                     ["Een kandidaat wordt afgewezen om zijn huidskleur.", None],
                     ["Een werkgever neemt niemand aan die ouder is dan vijftig.", None],
                 ], "pestgedrag · uitsluiting · racisme · discriminatie", WW),
             ]),
        dict(kop="Pesten of niet?",
             opdracht="Kruis aan, en schrijf er bij een nee in één regel bij wat het dan wel is.",
             oefeningen=[
                 ("waar", "Twee leerlingen maken ruzie over een opdracht en praten het daarna uit. "
                          "Dat is pestgedrag.", False),
                 ("waar", "Dezelfde leerling wordt week na week om hetzelfde uitgelachen. Dat is pestgedrag.",
                  True),
                 ("waar", "Racisme is een vorm van discriminatie.", True),
                 ("waar", "De impact van pesten op het slachtoffer verdwijnt zodra het stopt.", False),
             ]),
        dict(kop="Welk kenmerk van toestemming ontbreekt?",
             opdracht="Noteer bij elk geval welk van de zes kenmerken ontbreekt.",
             oefeningen=[
                 ("tabel", ["Geval", "Welk kenmerk ontbreekt"], [
                     ["Ze zegt ja nadat haar vrienden een halfuur hebben aangedrongen.", None],
                     ["Hij zegt niets en blijft stil.", None],
                     ["Ze weet niet waarover het eigenlijk gaat.", None],
                     ["Hij gaf vorige maand toestemming voor die ene foto, nu wordt ze opnieuw gebruikt.", None],
                     ["Een ja voor de ene situatie wordt uitgebreid naar een andere.", None],
                     ["Iemand is zo ziek dat hij de gevolgen niet kan overzien.", None],
                 ], "vrijwillig · duidelijk · geïnformeerd · actueel · specifiek · bekwaam gegeven", WW),
             ]),
        dict(kop="Formeel of informeel?",
             opdracht="Kruis aan, en schrijf er bij formeel in één woord bij wat de stijl dan vraagt.",
             oefeningen=[
                 ("kies", "een sollicitatiegesprek", ["formele context", "informele context"], 0),
                 ("kies", "een mail naar een mogelijke werkgever", ["formele context", "informele context"], 0),
                 ("kies", "een gesprek met vrienden in het jeugdhuis", ["formele context", "informele context"], 1),
                 ("kies", "een overleg met de directie over een stage", ["formele context", "informele context"], 0),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Respect betekent dat je het eens wordt met de ander.", False),
                 ("waar", "Stilzwijgen geldt als toestemming zolang niemand nee zegt.", False),
                 ("waar", "Toestemming kan achteraf nog ingetrokken worden.", True),
                 ("waar", "Formeel gaat over de regels van de situatie, niet over het middel dat je gebruikt.",
                  True),
                 ("waar", "Wie toekijkt bij pesten, heeft geen rol in de situatie.", False),
                 ("waar", "Altijd toegeven in een discussie is een vorm van respect voor jezelf.", False),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom een meningsverschil niet hetzelfde is als destructieve communicatie.",
                  "tegenspreken mag; het gaat erom hóe je het doet. Constructief benoem je je zorg zonder de "
                  "ander af te breken, en na het gesprek staat er iets, ook als je het oneens blijft", 3),
                 ("open", "Je ziet een klasgenoot online uitgelachen worden. Wat is de meest helpende "
                          "handelingsoptie, en waarom?",
                  "het slachtoffer steunen en de situatie melden; wegkijken laat de persoon alleen en laat "
                  "het gedrag doorgaan", 3),
                 ("open", "Leg uit wat groepsdruk is en hoe hij een toestemming kan aantasten.",
                  "groepsdruk is de invloed van een groep die je tot iets brengt wat je alleen niet zou doen; "
                  "een ja onder die druk is niet vrijwillig gegeven", 3),
                 ("open", "Noem drie dingen die een samenwerking bevorderen, en leg bij één ervan uit waarom.",
                  "duidelijke afspraken over wie wat doet, elkaar op de hoogte houden van de voortgang en "
                  "elkaars sterke kanten gebruiken; met duidelijke afspraken blijft er geen werk liggen "
                  "waarvan iedereen denkt dat een ander het doet", 4),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-ongevallen-herkennen-en-eerste-hulp-geven-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ongevallen herkennen en eerste hulp geven",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk nummer bel je?",
             opdracht="Schrijf het juiste noodnummer in het vakje.",
             oefeningen=[
                 ("rij", [("een inbraak in de straat", "101"), ("iemand bloedt zwaar", "112")], None, W),
                 ("rij", [("een kind dronk een product uit de kelder en is bij bewustzijn", "070 245 245"),
                          ("zondagavond, dringend maar geen levensgevaar", "1733")], None, "150px"),
                 ("rij", [("er is brand in een garage", "112"),
                          ("een vechtpartij op het plein", "101")], None, W),
             ]),
        dict(kop="Vier letsels",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Letsel", "Wat er gebeurd is"], [
                     ["ontwrichting", None],
                     ["verstuiking", None],
                 ], "ontwrichting: een bot is uit het gewricht geschoven · "
                    "verstuiking: de banden rond een gewricht zijn te ver uitgerekt", WL),
                 ("kort", "Noem de vier letsels van botten, spieren en gewrichten die de fiche opsomt:",
                  "botbreuk, kneuzing, ontwrichting en verstuiking", "260px"),
                 ("kort", "Noem de twee soorten wonden uit de fiche:", "de huidwonde en de brandwonde", "230px"),
             ]),
        dict(kop="Letsel of noodsituatie?",
             opdracht="Schrijf bij elk geval wat je vermoedt, met de woorden van de fiche.",
             oefeningen=[
                 ("open", "Iemand valt van een ladder en zijn arm staat in een vreemde hoek.",
                  "een botbreuk of een ontwrichting", 2),
                 ("open", "Iemand verslikt zich en kan niet meer praten of hoesten.",
                  "een verslikking, en dat is een noodsituatie", 2),
                 ("open", "Bij iemand pompt het hart niet meer en de ademhaling valt stil.",
                  "een hart- en ademhalingsstilstand", 2),
             ]),
        dict(kop="Zes basisprincipes of vier stappen?",
             opdracht="Kruis aan waar het item thuishoort.",
             oefeningen=[
                 ("kies", "blijf rustig in een noodsituatie", ["basisprincipe", "stap"], 0),
                 ("kies", "zorg voor veiligheid", ["basisprincipe", "stap"], 1),
                 ("kies", "vermijd besmetting", ["basisprincipe", "stap"], 0),
                 ("kies", "raadpleeg gespecialiseerde hulp", ["basisprincipe", "stap"], 1),
                 ("kies", "verleen psychosociale hulp", ["basisprincipe", "stap"], 0),
                 ("kies", "beoordeel de toestand van het slachtoffer", ["basisprincipe", "stap"], 1),
             ]),
        dict(kop="De vier stappen in volgorde",
             opdracht="Zet de nummers 1 tot 4 in de juiste volgorde.",
             oefeningen=[
                 ("rij", [("beoordeel de toestand van het slachtoffer", "2"),
                          ("verleen verdere eerste hulp", "4")], None, "58px"),
                 ("rij", [("zorg voor veiligheid", "1"),
                          ("raadpleeg gespecialiseerde hulp", "3")], None, "58px"),
             ]),
        dict(kop="Wat loopt hier mis?",
             opdracht="Schrijf in twee zinnen welke stap overgeslagen of omgewisseld wordt.",
             oefeningen=[
                 ("open", "Er staat een auto midden op de rijweg met een gewonde erin. Een voorbijganger "
                          "stapt meteen naar de gewonde toe om te kijken hoe hij eraan toe is.",
                  "hij slaat stap 1 over: eerst voor veiligheid zorgen, anders wordt hij zelf het tweede "
                  "slachtoffer", 3),
                 ("open", "Iemand loopt de gewonde zonder iets te zeggen voorbij om van thuis uit een "
                          "ambulance te bellen.",
                  "hij slaat stap 2 over: hij beoordeelde de toestand niet, en zonder die beoordeling weet "
                  "de centrale niet wat ze moet sturen", 3),
                 ("open", "Een kind dronk een product uit de kelder en is bewusteloos. De buur belt het "
                          "antigifcentrum.",
                  "bij bewustzijnsverlies bel je 112, niet het antigifcentrum", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "101 is het nummer voor een ziekenwagen.", False),
                 ("waar", "112 is zowel voor de ziekenwagen als voor de brandweer.", True),
                 ("waar", "Een kneuzing en een botbreuk zijn hetzelfde letsel.", False),
                 ("waar", "Vermijd besmetting werkt in twee richtingen.", True),
                 ("waar", "Gespecialiseerde hulp inroepen is de laatste van de vier stappen.", False),
                 ("waar", "Getuigen noteren hoort bij de zes basisprincipes.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-een-hartstilstand-reanimatie-en-de-aed-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een hartstilstand, reanimatie en de AED",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De twee alarmtekens",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Teken 1: de persoon", "reageert niet", WW),
                 ("kort", "Teken 2: de persoon", "ademt niet normaal", WW),
                 ("kort", "Bij een hartstilstand doet het hart dit niet meer:", "pompen", W),
             ]),
        dict(kop="De zes stappen in volgorde",
             opdracht="Zet de nummers 1 tot 6 bij de stappen.",
             oefeningen=[
                 ("rij", [("beadem", "5"), ("bel 112", "2"), ("start met borstcompressies", "4")],
                  None, "58px"),
                 ("rij", [("ga door tot de ambulancier het overneemt", "6"),
                          ("bepaal of de persoon bewusteloos is", "1"),
                          ("kijk of er een AED in de buurt is", "3")], None, "58px"),
             ]),
        dict(kop="Wat loopt hier mis?",
             opdracht="Schrijf in twee zinnen wat er fout gaat en wat het wel moest zijn.",
             oefeningen=[
                 ("open", "Iemand begint onmiddellijk met borstcompressies en belt pas daarna 112.",
                  "bellen is stap 2 en komt dus vóór de compressies; hoe later de ambulance vertrekt, hoe "
                  "langer de persoon zonder professionele hulp blijft", 3),
                 ("open", "Een hulpverlener stopt met reanimeren omdat de persoon een keer zucht.",
                  "je gaat door tot de ambulance er is en de ambulancier het overneemt", 3),
                 ("open", "Iemand reanimeert op een zetel in de woonkamer.",
                  "je reanimeert op een harde ondergrond: op een zetel zakt het lichaam mee en komen de "
                  "compressies niet aan", 3),
                 ("open", "Een hulpverlener duwt door terwijl de AED aan het meten is.",
                  "terwijl de AED meet, raak je het slachtoffer niet aan: aanraken verstoort de meting en "
                  "bij een stoot is het ook voor jou gevaarlijk", 3),
             ]),
        dict(kop="Borstcompressies en beademing",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Vraag", "Antwoord"], [
                     ["Waar leg je je handen?", None],
                     ["Hoe houd je je armen?", None],
                     ["Wat moet er tussen twee compressies gebeuren?", None],
                     ["Wat doe je voor je beademt?", None],
                     ["Waaraan zie je dat een beademing aankomt?", None],
                 ], "midden op de borstkas · gestrekt, met de schouders recht boven de handen · "
                    "de borstkas volledig laten terugkomen · het hoofd achterover kantelen en de kin "
                    "optillen, en de neus dichtknijpen · de borstkas komt zichtbaar omhoog", WL),
             ]),
        dict(kop="Alleen of met omstaanders",
             opdracht="Schrijf telkens twee zinnen.",
             oefeningen=[
                 ("open", "Je bent alleen bij iemand met een hartstilstand. Wat doe je met je telefoon, en "
                          "waarom?",
                  "112 bellen en de luidspreker aanzetten, zodat je handen vrij blijven en de centrale je "
                  "door de stappen loodst", 3),
                 ("open", "Er staan twee omstaanders bij. Hoe verdeel je de taken?",
                  "één iemand belt 112, één iemand zoekt een AED, en jij begint met de compressies", 3),
                 ("open", "Je bent uitgeput na enkele minuten reanimeren. Wat doe je?",
                  "iemand anders laten overnemen in plaats van te stoppen", 2),
             ]),
        dict(kop="De AED",
             opdracht="Vul aan en antwoord kort.",
             oefeningen=[
                 ("kort", "AED staat voor", "automatische externe defibrillator", "250px"),
                 ("open", "Waarom heet de AED automatisch?",
                  "omdat hij zelf het hartritme meet en zelf beslist of er een stroomstoot nodig is", 2),
                 ("open", "Je hebt een AED gehaald. Wat doe je er het eerst mee?",
                  "hem aanzetten en de gesproken instructies volgen", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Bij een hartstilstand klopt het hart te snel.", False),
                 ("waar", "Zonder rondgaand bloed krijgen de hersenen geen zuurstof.", True),
                 ("waar", "Je legt je handen links op de borstkas, waar het hart zit.", False),
                 ("waar", "Gebogen ellebogen maken de compressies dieper.", False),
                 ("waar", "De stabiele zijligging is een van de zes stappen.", False),
                 ("waar", "De compressies komen vóór de beademing.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-inkomsten-en-de-uitgaven-van-de-overheid-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De inkomsten en de uitgaven van de overheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke soort inkomst?",
             opdracht="Schrijf bij elk voorbeeld een van de vier soorten inkomsten.",
             oefeningen=[
                 ("tabel", ["Voorbeeld", "Welke soort inkomst"], [
                     ["de accijnzen op brandstof", None],
                     ["de onroerende voorheffing", None],
                     ["een boete voor te snel rijden", None],
                     ["de verhuur van een gebouw van de overheid", None],
                     ["de btw op een televisie", None],
                     ["betalen voor een paspoort", None],
                 ], "indirecte belasting · directe belasting · diverse inkomsten · inkomsten uit "
                    "overheidskapitaal · indirecte belasting · diverse inkomsten", WL),
             ]),
        dict(kop="Direct of indirect?",
             opdracht="Kruis aan, en schrijf er in één regel bij waarom.",
             oefeningen=[
                 ("kies", "de btw", ["directe belasting", "indirecte belasting"], 1),
                 ("kies", "de bedrijfsvoorheffing", ["directe belasting", "indirecte belasting"], 0),
                 ("kies", "de milieubelasting", ["directe belasting", "indirecte belasting"], 1),
                 ("kies", "de onroerende voorheffing", ["directe belasting", "indirecte belasting"], 0),
             ]),
        dict(kop="Welke soort uitgave?",
             opdracht="Vul de tabel aan met een van de vier soorten uitgaven.",
             oefeningen=[
                 ("tabel", ["Uitgave van de overheid", "Welke soort"], [
                     ["De overheid legt glasvezel aan in een industriezone.", None],
                     ["Ze betaalt de bouw van sociale woningen.", None],
                     ["Ze subsidieert een festival en een sporthal.", None],
                     ["Ze betaalt de politie en het onderwijs.", None],
                     ["Ze voert een infocampagne over gezond eten.", None],
                     ["Ze financiert de sociale zekerheid.", None],
                 ], "economische groei · sociale uitgave · maatschappelijk leven · collectieve behoeften · "
                    "maatschappelijk leven · sociale uitgave", WL),
             ]),
        dict(kop="Vul het rijtje aan",
             opdracht="Schrijf de voorbeelden die de fiche zelf bij elke soort uitgave noemt.",
             oefeningen=[
                 ("kort", "collectieve behoeften:", "veiligheid, onderwijs en openbaar vervoer", "260px"),
                 ("kort", "economische groei:", "handel, transport, digitale infrastructuur en duurzaamheid",
                  "290px"),
                 ("kort", "maatschappelijk leven:", "cultuur, sport en infocampagnes", "260px"),
             ]),
        dict(kop="Twee soorten tegenover elkaar",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Een gemeente kiest tussen een bibliotheek en een fietsbrug. Welke twee soorten "
                          "uitgaven staan hier tegenover elkaar?",
                  "het maatschappelijk leven (de bibliotheek) tegenover een collectieve behoefte "
                  "(mobiliteit, de fietsbrug)", 3),
                 ("open", "Leg uit waarom de verkoop van een stuk grond door de overheid geen belasting is.",
                  "het is een inkomst uit overheidskapitaal: de overheid verkoopt iets wat ze zelf bezit en "
                  "heft niets bij de burger", 3),
                 ("open", "Leg uit wat collectieve behoeften zijn en geef er twee van.",
                  "behoeften waar de hele samenleving van gebruikmaakt, bijvoorbeeld veiligheid en "
                  "openbaar vervoer", 3),
                 ("open", "Waarom vraagt de fiche naar de inkomsten én de uitgaven samen?",
                  "omdat de overheid met die twee samen de ongelijkheid probeert te beperken", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Bij een indirecte belasting betaal je ze aan de verkoper, die ze doorstort.", True),
                 ("waar", "Cultuur en sport zijn sociale uitgaven.", False),
                 ("waar", "De financiering van de sociale zekerheid is een inkomst van de overheid.", False),
                 ("waar", "Giften staan in de fiche bij de inkomsten van de overheid.", False),
                 ("waar", "Een overheid heft belastingen om haar uitgaven voor de samenleving te betalen.",
                  True),
                 ("waar", "De uitgaven van de overheid bepalen mee wat er voor iedereen beschikbaar is.",
                  True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-sociale-zekerheid-uitkeringen-en-herverdeling-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale zekerheid, uitkeringen en herverdeling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke uitkering?",
             opdracht="Schrijf bij elke situatie de uitkering die erbij hoort.",
             oefeningen=[
                 ("tabel", ["Situatie", "Welke uitkering"], [
                     ["Sofie verliest haar werk.", None],
                     ["Karim valt van een ladder tijdens zijn werkuren.", None],
                     ["Iemand wordt ziek na jarenlang met een schadelijke stof te werken.", None],
                     ["De partner van iemand overlijdt.", None],
                     ["Iemand kan door ziekte maanden niet werken.", None],
                     ["Iedereen krijgt elk jaar een bedrag bovenop het loon.", None],
                 ], "werkloosheidsuitkering · arbeidsongevallenuitkering · uitkering beroepsziekte · "
                    "overlevingspensioen · ziekte- en invaliditeitsuitkering · jaarlijks vakantiegeld", WL),
             ]),
        dict(kop="Vervangend of aanvullend?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "de werkloosheidsuitkering", ["vervangingsinkomen", "aanvullend inkomen"], 0),
                 ("kies", "het jaarlijks vakantiegeld", ["vervangingsinkomen", "aanvullend inkomen"], 1),
                 ("kies", "het rustpensioen", ["vervangingsinkomen", "aanvullend inkomen"], 0),
                 ("kies", "het groeipakket", ["vervangingsinkomen", "aanvullend inkomen"], 1),
                 ("kies", "de ziekte- en invaliditeitsuitkering", ["vervangingsinkomen", "aanvullend inkomen"], 0),
             ]),
        dict(kop="Fiscaal of sociaal?",
             opdracht="Kruis aan welke soort herverdelingsmaatregel het is.",
             oefeningen=[
                 ("kies", "de progressieve personenbelasting via belastingschijven", ["fiscaal", "sociaal"], 0),
                 ("kies", "een huurpremie", ["fiscaal", "sociaal"], 1),
                 ("kies", "een belastingheffing op vermogen", ["fiscaal", "sociaal"], 0),
                 ("kies", "een kansentarief voor sport en cultuur", ["fiscaal", "sociaal"], 1),
                 ("kies", "verschillende tarieven bij indirecte belastingen", ["fiscaal", "sociaal"], 0),
                 ("kies", "een studiebeurs", ["fiscaal", "sociaal"], 1),
                 ("kies", "het leefloon", ["fiscaal", "sociaal"], 1),
                 ("kies", "een belastingvermindering", ["fiscaal", "sociaal"], 0),
             ]),
        dict(kop="Vul aan",
             opdracht="Schrijf het antwoord in het vakje.",
             oefeningen=[
                 ("kort", "RSZ staat voor", "Rijksdienst voor Sociale Zekerheid", "250px"),
                 ("kort", "De sociale zekerheid steunt op", "solidariteit", W),
                 ("kort", "De RSZ wordt gefinancierd door", "de werkgevers, de werknemers en de overheid",
                  "270px"),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg het verschil uit tussen een arbeidsongeval en een beroepsziekte.",
                  "een arbeidsongeval is een plots ongeval tijdens het werk; een beroepsziekte komt van het "
                  "werk zelf over langere tijd", 3),
                 ("open", "Leg uit wat een progressieve personenbelasting is en hoe ze werkt.",
                  "wie meer verdient betaalt een hoger percentage, en dat gebeurt via belastingschijven: "
                  "elk stuk van je inkomen valt in een eigen schijf", 3),
                 ("open", "Waarom bestaan er verschillende tarieven bij de indirecte belastingen?",
                  "zodat noodzakelijke producten lichter belast worden dan luxe", 2),
                 ("open", "Leg uit wat herverdeling is.",
                  "de overheid verschuift middelen van sterkere naar zwakkere schouders, om de sociale "
                  "ongelijkheid te beperken", 3),
                 ("open", "Leg het verschil uit tussen een rustpensioen en een overlevingspensioen.",
                  "een rustpensioen is voor wie stopt met werken op pensioenleeftijd, een overlevingspensioen "
                  "voor de achterblijvende partner", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "De RSZ wordt enkel door de werkgevers gefinancierd.", False),
                 ("waar", "Het vakantiegeld staat in het rijtje van zes uitkeringen.", True),
                 ("waar", "Het vakantiegeld is een vervangingsinkomen.", False),
                 ("waar", "Betaalde iedereen hetzelfde percentage belasting, dan was ze vlak en niet "
                          "progressief.", True),
                 ("waar", "Op je loonbriefje staan de bijdrage van de werknemer en die van de werkgever "
                          "apart.", True),
                 ("waar", "Het groeipakket is een fiscale maatregel.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vraag-aanbod-en-het-marktevenwicht-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vraag, aanbod en het marktevenwicht",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De grafiek lezen",
             opdracht="Kijk naar de tekening en antwoord.",
             oefeningen=[
                 ("fig", [(svg.marktevenwicht(breedte=360), "E, het snijpunt van V en A")],
                  "Welke letter staat bij het evenwicht?"),
                 ("kort", "Wat staat er op de verticale as?", "de prijs", W),
                 ("kort", "Wat staat er op de horizontale as?", "de hoeveelheid", W),
                 ("kort", "De vrager is de", "koper", W),
                 ("kort", "De aanbieder is de", "verkoper", W),
             ]),
        dict(kop="Stijgt of daalt?",
             opdracht="Vul in wat er gebeurt als de prijs stijgt.",
             oefeningen=[
                 ("rij", [("de gevraagde hoeveelheid", "daalt"), ("de aangeboden hoeveelheid", "stijgt")],
                  None, W),
                 ("rij", [("de vraagcurve loopt", "dalend"), ("de aanbodcurve loopt", "stijgend")], None, W),
             ]),
        dict(kop="Overschot of tekort?",
             opdracht="Reken uit. Schrijf de bewerking op en zet erbij of het een overschot of een tekort is.",
             oefeningen=[
                 ("kort", "Bij 8 euro: vraag 90 stuks, aanbod 150 stuks.", "150 − 90 = overschot van 60 stuks",
                  "250px"),
                 ("kort", "Bij 3 euro: vraag 220 stuks, aanbod 160 stuks.", "220 − 160 = tekort van 60 stuks",
                  "250px"),
                 ("kort", "Bij 7 euro: vraag 110 stuks, aanbod 185 stuks.", "185 − 110 = overschot van 75 stuks",
                  "250px"),
                 ("kort", "Bij 4 euro: vraag 195 stuks, aanbod 120 stuks.", "195 − 120 = tekort van 75 stuks",
                  "250px"),
                 ("kort", "Bij 5 euro: vraag 140 stuks, aanbod 140 stuks.",
                  "geen overschot en geen tekort: dit is het evenwicht", "250px"),
             ]),
        dict(kop="Lees het evenwicht af",
             opdracht="Vul de tabel aan en antwoord daarna op de twee vragen eronder.",
             oefeningen=[
                 ("tabel", ["Prijs", "Vraag", "Aanbod", "Overschot of tekort"], [
                     ["9 euro", "70", "200", None],
                     ["7 euro", "110", "160", None],
                     ["6 euro", "130", "130", None],
                     ["4 euro", "180", "95", None],
                 ], "9 euro: overschot 130 · 7 euro: overschot 50 · 6 euro: evenwicht · 4 euro: tekort 85",
                  "180px"),
                 ("kort", "De evenwichtsprijs in deze tabel is", "6 euro", W),
                 ("kort", "De evenwichtshoeveelheid is", "130 stuks", W),
             ]),
        dict(kop="Waar ligt de prijs?",
             opdracht="Schrijf of de prijs boven of onder de evenwichtsprijs ligt, en waarom.",
             oefeningen=[
                 ("open", "Een marktkramer houdt elke avond kratten over.",
                  "boven de evenwichtsprijs: er is een overschot, dus de prijs is te hoog", 2),
                 ("open", "Een winkel is al om tien uur uitverkocht en moet mensen wegsturen.",
                  "onder de evenwichtsprijs: er is een tekort, dus de prijs is te laag", 2),
                 ("open", "Bij een bakker is elke dag precies alles verkocht en wordt niemand weggestuurd.",
                  "op de evenwichtsprijs: geen overschot en geen tekort", 2),
             ]),
        dict(kop="Wat doet de markt zelf?",
             opdracht="Schrijf telkens twee zinnen.",
             oefeningen=[
                 ("open", "Er is een overschot en de overheid doet niets. Wat gebeurt er met de prijs, en "
                          "waarom?",
                  "de prijs zakt naar het evenwicht: verkopers met onverkochte voorraad zakken met hun prijs",
                  3),
                 ("open", "Er is een tekort en de overheid doet niets. Wat gebeurt er met de prijs, en "
                          "waarom?",
                  "de prijs stijgt: kopers zijn bereid meer te betalen", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "De aanbodcurve daalt als de prijs stijgt.", False),
                 ("waar", "Bij de evenwichtsprijs blijft er geen onverkochte voorraad over.", True),
                 ("waar", "Bij één prijs kan er een overschot én een tekort tegelijk zijn.", False),
                 ("waar", "Op de productmarkt worden goederen en diensten verhandeld.", True),
                 ("waar", "De evenwichtsprijs ligt voor altijd vast.", False),
                 ("waar", "Een overschot bereken je als aanbod min vraag.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-verschuivingen-op-de-markt-en-de-overheid-die-ingrijpt-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verschuivingen op de markt en de overheid die ingrijpt",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Op de curve of van de curve?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "De prijs van het product zelf daalt.",
                  ["beweging op de curve", "verschuiving van de curve"], 0),
                 ("kies", "De lonen van de kopers stijgen.",
                  ["beweging op de curve", "verschuiving van de curve"], 1),
                 ("kies", "Een nieuwe machine maakt produceren goedkoper.",
                  ["beweging op de curve", "verschuiving van de curve"], 1),
                 ("kies", "De verkoper zet zijn prijs een euro hoger.",
                  ["beweging op de curve", "verschuiving van de curve"], 0),
                 ("kies", "Het product raakt uit de mode.",
                  ["beweging op de curve", "verschuiving van de curve"], 1),
             ]),
        dict(kop="Welke curve, en naar waar?",
             opdracht="Vul de tabel aan. Schrijf vraag of aanbod, en links of rechts.",
             oefeningen=[
                 ("tabel", ["Wat er gebeurt", "Welke curve", "Naar waar"], [
                     ["De grondstoffen worden duurder.", None, None],
                     ["Er komen kopers bij op de markt.", None, None],
                     ["Een vergelijkbaar product wordt veel goedkoper.", None, None],
                     ["Er komen verkopers bij op de markt.", None, None],
                     ["Een product raakt in de mode.", None, None],
                 ], "aanbod links · vraag rechts · vraag links · aanbod rechts · vraag rechts", "150px"),
             ]),
        dict(kop="Wat doet dat met het evenwicht?",
             opdracht="Vul in wat er met de prijs en met de hoeveelheid gebeurt. De andere curve blijft gelijk.",
             oefeningen=[
                 ("fig", [(svg.marktevenwicht(breedte=360, verschuiving="aanbod links"),
                           "ze stijgt: het aanbod verschuift naar links")],
                  "Het aanbod verschuift naar links. Wat gebeurt er met de prijs?"),
                 ("tabel", ["Verschuiving", "Prijs", "Hoeveelheid"], [
                     ["vraag naar rechts", None, None],
                     ["vraag naar links", None, None],
                     ["aanbod naar rechts", None, None],
                     ["aanbod naar links", None, None],
                 ], "vraag rechts: beide stijgen · vraag links: beide dalen · aanbod rechts: prijs daalt, "
                    "hoeveelheid stijgt · aanbod links: prijs stijgt, hoeveelheid daalt", "130px"),
             ]),
        dict(kop="Drie maatregelen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Noem de drie maatregelen van de overheid uit de fiche:",
                  "btw en accijnzen heffen, premies en subsidies uitkeren, en minimum- en maximumprijzen "
                  "invoeren", "290px"),
                 ("kort", "Een accijns is", "een extra belasting op bepaalde producten", "250px"),
                 ("kort", "Noem drie producten met accijnzen:", "brandstof, tabak en alcohol", "230px"),
             ]),
        dict(kop="Welk gevolg?",
             opdracht="Schrijf per maatregel wat er met de curve en met de prijs gebeurt.",
             oefeningen=[
                 ("tabel", ["Maatregel", "Welke curve, naar waar", "Wat met de prijs"], [
                     ["een belasting op een product", None, None],
                     ["een subsidie aan de producenten", None, None],
                     ["een premie aan de kopers", None, None],
                 ], "belasting: aanbod links, prijs stijgt · subsidie: aanbod rechts, prijs daalt · "
                    "premie: vraag rechts, prijs stijgt en er wordt meer verkocht", "160px"),
                 ("open", "De overheid geeft een premie voor zonnepanelen. Wat gebeurt er op die markt?",
                  "meer mensen willen kopen bij elke prijs: de vraag verschuift naar rechts, de prijs stijgt "
                  "en er worden meer panelen verkocht", 3),
                 ("open", "Een zomer met slecht weer bederft een groot deel van de oogst. Wat gebeurt er met "
                          "de prijs van die groente?",
                  "het aanbod verschuift naar links en de prijs stijgt", 3),
             ]),
        dict(kop="Minimumprijs of maximumprijs?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Vaste prijs", "Waar ze ligt", "Wat ze geeft", "Waarom ze bestaat"], [
                     ["minimumprijs", None, None, None],
                     ["maximumprijs", None, None, None],
                 ], "minimumprijs: boven het evenwicht, overschot, om de producenten een leefbaar inkomen "
                    "te garanderen · maximumprijs: onder het evenwicht, tekort, om een noodzakelijk product "
                    "betaalbaar te houden", "130px"),
                 ("open", "Een minimumprijs wordt onder de evenwichtsprijs gelegd. Wat verandert er?",
                  "niets, want de markt zit er al boven; een vaste prijs doet pas iets als ze aan de juiste "
                  "kant van het evenwicht ligt", 3),
                 ("open", "Een maximumprijs wordt boven de evenwichtsprijs gelegd. Wat verandert er?",
                  "niets, om dezelfde reden: de markt zit er al onder", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Een prijsdaling van het product zelf verschuift de vraagcurve.", False),
                 ("waar", "Een inkomensstijging verschuift de vraagcurve.", True),
                 ("waar", "Een minimumprijs geeft een tekort.", False),
                 ("waar", "Een accijns komt bovenop de btw.", True),
                 ("waar", "De productie zelf overnemen staat bij de drie maatregelen van de fiche.", False),
                 ("waar", "Een subsidie aan producenten duwt het aanbod naar rechts.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-arbeidsovereenkomst-en-het-arbeidsreglement-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De arbeidsovereenkomst en het arbeidsreglement",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Overeenkomst of reglement?",
             opdracht="Kruis aan waar je dit terugvindt.",
             oefeningen=[
                 ("kies", "jouw brutoloon", ["arbeidsovereenkomst", "arbeidsreglement"], 0),
                 ("kies", "het uurrooster van de hele ploeg", ["arbeidsovereenkomst", "arbeidsreglement"], 1),
                 ("kies", "de duur van jouw contract", ["arbeidsovereenkomst", "arbeidsreglement"], 0),
                 ("kies", "hoe je ziekte in dit bedrijf moet melden",
                  ["arbeidsovereenkomst", "arbeidsreglement"], 1),
                 ("kies", "jouw functie", ["arbeidsovereenkomst", "arbeidsreglement"], 0),
                 ("kies", "de openingsuren", ["arbeidsovereenkomst", "arbeidsreglement"], 1),
             ]),
        dict(kop="Welke indeling?",
             opdracht="Schrijf bij elk begrip of het bij de aard van het werk, de duur of de omvang van de prestaties hoort.",
             oefeningen=[
                 ("rij", [("bediende", "aard van het werk"), ("deeltijds", "omvang")], None, WW),
                 ("rij", [("onbepaalde duur", "duur"), ("arbeider", "aard van het werk")], None, WW),
                 ("rij", [("voltijds", "omvang"), ("vervangingsduur", "duur")], None, WW),
             ]),
        dict(kop="Lees één contract in drie vakjes",
             opdracht="Vul de drie indelingen in voor elk contract.",
             oefeningen=[
                 ("tabel", ["Contract", "Aard", "Duur", "Omvang"], [
                     ["drie dagen per week als bediende, zonder einddatum", None, None, None],
                     ["voltijds als arbeider, van 1 maart tot en met 31 augustus", None, None, None],
                     ["halve dagen als bediende, tot de collega terug is uit ziekteverlof", None, None, None],
                 ], "bediende / onbepaalde duur / deeltijds · arbeider / bepaalde duur / voltijds · "
                    "bediende / vervangingsduur / deeltijds", "120px"),
             ]),
        dict(kop="Welke soort duur?",
             opdracht="Schrijf bij elk voorbeeld de soort duur, en in één regel wanneer het contract eindigt.",
             oefeningen=[
                 ("open", "Jana is aangenomen om één dak te vernieuwen.",
                  "welomschreven werk: het eindigt als de opdracht af is", 2),
                 ("open", "Tom vervangt een collega die met ziekteverlof is.",
                  "vervangingsduur: het eindigt als de afwezige collega terug is", 2),
                 ("open", "Het contract van Bilal heeft geen einddatum.",
                  "onbepaalde duur: het eindigt pas als een van de twee partijen het beëindigt", 2),
                 ("open", "Het contract van Lien loopt van 1 maart tot en met 31 augustus.",
                  "bepaalde duur: het eindigt op de einddatum", 2),
             ]),
        dict(kop="Arbeidssituaties",
             opdracht="Vul in of antwoord kort.",
             oefeningen=[
                 ("kort", "Overloon is", "een toeslag bovenop het gewone loon voor overwerk", "270px"),
                 ("kort", "Bij een schorsing ligt het werk stil en het contract", "blijft bestaan", "180px"),
                 ("kort", "Nachtarbeid is in principe", "verboden, met wettelijke uitzonderingen", "250px"),
                 ("kort", "Noem drie soorten bronmateriaal die je op het examen kan krijgen:",
                  "een arbeidsovereenkomst, een arbeidsreglement en een loonfiche (ook een krantenartikel, "
                  "een brochure of een wettekst)", "290px"),
             ]),
        dict(kop="Recht van wie, plicht van wie?",
             opdracht="Schrijf bij elk item wie het betreft: de werknemer of de werkgever.",
             oefeningen=[
                 ("rij", [("op tijd zijn loon ontvangen is een recht van", "de werknemer"),
                          ("zorgen voor een veilige werkplek is een plicht van", "de werkgever")], None, WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Arbeider en bediende gaan over de duur van het contract.", False),
                 ("waar", "Deeltijds kan ook voor onbepaalde tijd.", True),
                 ("waar", "Bij een vervangingsduur staat er geen vaste einddatum in het contract.", True),
                 ("waar", "Een proefduur is een eigen soort duur in het rijtje van de fiche.", False),
                 ("waar", "Bij een schorsing is het contract beëindigd.", False),
                 ("waar", "De arbeidsovereenkomst is belangrijk voor beide partijen.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-brutoloon-naar-nettoloon-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Van brutoloon naar nettoloon",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De weg van bruto naar netto",
             opdracht="Kijk naar de tekening en vul de drie bedragen en de twee inhoudingen in.",
             oefeningen=[
                 ("fig", [(svg.stappen(["brutoloon", "belastbaar loon", "nettoloon"]),
                           "de sociale zekerheidsbijdrage en daarna de bedrijfsvoorheffing")],
                  "Welke twee inhoudingen zitten tussen deze drie bedragen?"),
                 ("kort", "Inhouding 1 heet", "de sociale zekerheidsbijdrage", "230px"),
                 ("kort", "Inhouding 2 heet", "de bedrijfsvoorheffing", "200px"),
                 ("kort", "Na inhouding 1 houd je over:", "het belastbaar loon", "180px"),
             ]),
        dict(kop="Reken na",
             opdracht="Schrijf de bewerking op, niet alleen het bedrag.",
             oefeningen=[
                 ("kort", "Bruto 2 400 euro, belastbaar 2 086 euro. Hoeveel is de sociale bijdrage?",
                  "2 400 − 2 086 = 314 euro", "230px"),
                 ("kort", "Belastbaar 2 086 euro, netto 1 720 euro. Hoeveel is de bedrijfsvoorheffing?",
                  "2 086 − 1 720 = 366 euro", "230px"),
                 ("kort", "Bruto 2 800 euro, sociale bijdrage 366 euro. Hoeveel is het belastbaar loon?",
                  "2 800 − 366 = 2 434 euro", "230px"),
                 ("kort", "Belastbaar 2 434 euro, voorheffing 480 euro. Hoeveel is het nettoloon?",
                  "2 434 − 480 = 1 954 euro", "230px"),
                 ("kort", "Een arbeider verdient 2 000 euro bruto. Op welk bedrag wordt zijn sociale "
                          "bijdrage berekend?", "108 % van 2 000 = 2 160 euro", "230px"),
             ]),
        dict(kop="Wie houdt er meer over?",
             opdracht="Kruis aan en schrijf er in één regel bij waarom.",
             oefeningen=[
                 ("kies", "Een arbeider en een bediende verdienen allebei 2 000 euro bruto. Wie betaalt de "
                          "hoogste sociale bijdrage?", ["de arbeider", "de bediende"], 0),
                 ("kies", "Twee mensen hebben hetzelfde brutoloon; de ene heeft twee kinderen ten laste. "
                          "Wie houdt netto meer over?", ["wie kinderen ten laste heeft", "de andere"], 0),
                 ("kies", "Een student en een voltijdse bediende verdienen hetzelfde bruto. Bij wie ligt "
                          "het netto het dichtst bij het bruto?", ["de student", "de bediende"], 0),
             ]),
        dict(kop="Een student",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Binnen een studentencontract houdt de werkgever enkel dit in:",
                  "een solidariteitsbijdrage", "230px"),
                 ("kort", "Welke inhouding gaat er bij een student niet af?", "de bedrijfsvoorheffing",
                  "200px"),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat het woord voorheffing betekent en wat er gebeurt als je werkgever er "
                          "te veel inhoudt.",
                  "voorheffing betekent vooraf geheven, in de plaats van alles pas bij de aangifte te "
                  "betalen; houdt hij er te veel in, dan krijg je het verschil terug na je "
                  "belastingaangifte", 4),
                 ("open", "Leg uit waarom de sociale bijdrage van een arbeider op 108 procent berekend wordt.",
                  "een oude regel uit de tijd dat arbeiders per dag of per uur betaald werden; het "
                  "percentage is hetzelfde, maar het bedrag waarop gerekend wordt ligt hoger", 3),
                 ("open", "Wat is de loonkost voor een werkgever?",
                  "het brutoloon plus zijn eigen bijdrage aan de RSZ, en dus hoger dan het bruto op het "
                  "contract", 3),
                 ("open", "Noem het verschillende doel van de twee inhoudingen op een loonfiche.",
                  "de RSZ-bijdrage financiert de sociale zekerheid; de bedrijfsvoorheffing is een voorschot "
                  "op je personenbelasting", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "De bedrijfsvoorheffing gaat af voor de sociale bijdrage.", False),
                 ("waar", "Het belastbaar loon is hetzelfde als het nettoloon.", False),
                 ("waar", "De gezinssituatie verandert de bedrijfsvoorheffing.", True),
                 ("waar", "De gezinssituatie verandert ook de sociale bijdrage.", False),
                 ("waar", "De werkgever betaalt bovenop het bruto nog een eigen RSZ-bijdrage.", True),
                 ("waar", "De berekening van bruto naar netto vind je terug op de loonfiche.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-welzijn-op-het-werk-en-waar-je-met-vragen-terechtkan-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijn op het werk en waar je met vragen terechtkan",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De afkortingen voluit",
             opdracht="Schrijf de volledige naam.",
             oefeningen=[
                 ("kort", "CPBW", "Comité voor Preventie en Bescherming op het Werk", "290px"),
                 ("kort", "RSZ", "Rijksdienst voor Sociale Zekerheid", "250px"),
                 ("kort", "RVA", "Rijksdienst voor Arbeidsvoorziening", "250px"),
                 ("kort", "VDAB", "Vlaamse Dienst voor Arbeidsbemiddeling en Beroepsopleiding", "290px"),
             ]),
        dict(kop="Waar ga je naartoe?",
             opdracht="Schrijf bij elke vraag de instantie of organisatie uit de fiche.",
             oefeningen=[
                 ("tabel", ["Vraag van een werknemer of student", "Waar hij terechtkan"], [
                     ["Ik wil weten hoeveel uren ik dit jaar al als student gewerkt heb.", None],
                     ["Ik ben mijn werk kwijt en wil een uitkering aanvragen.", None],
                     ["Ik zoek werk en wil een opleiding volgen.", None],
                     ["Ik denk dat mijn overloon niet klopt en wil advies.", None],
                     ["Ik twijfel of mijn werkgever bijdragen voor mij betaalt.", None],
                     ["Er staat een nooduitgang versperd in ons bedrijf.", None],
                 ], "student@work · RVA · VDAB · een vakbond · RSZ · het CPBW", WL),
             ]),
        dict(kop="RVA, VDAB of RSZ?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "betaalt de werkloosheidsuitkering", ["RVA", "VDAB", "RSZ"], 0),
                 ("kies", "helpt je aan werk en opleiding", ["RVA", "VDAB", "RSZ"], 1),
                 ("kies", "int de bijdragen voor de sociale zekerheid", ["RVA", "VDAB", "RSZ"], 2),
                 ("kies", "regelt loopbaanonderbreking", ["RVA", "VDAB", "RSZ"], 0),
                 ("kies", "doet loopbaanbegeleiding", ["RVA", "VDAB", "RSZ"], 1),
             ]),
        dict(kop="Veilig werken",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Preventie is", "maatregelen nemen voordat er iets misgaat", "250px"),
                 ("kort", "Wie voorziet de persoonlijke beschermingsmiddelen?", "de werkgever", "150px"),
                 ("kort", "Wie moet gevaren melden?", "de werknemer", "150px"),
                 ("kort", "Pictogrammen waarschuwen", "in één oogopslag voor gevaar of een verplichting",
                  "270px"),
             ]),
        dict(kop="Wat doe je?",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Een machine in jouw afdeling heeft een losse kap waar iemand bij kan. Wat doe je?",
                  "het meteen melden en de machine niet gebruiken; melden is een plicht van de werknemer, "
                  "herstellen is een zaak voor wie het mag", 3),
                 ("open", "Een nieuwe werknemer krijgt op zijn eerste dag uitleg over de nooduitgangen en de "
                          "machines. Hoe heet zo'n maatregel, en waarom?",
                  "een preventiemaatregel: onthaal en vorming horen bij het voorkomen van ongevallen", 3),
                 ("open", "Leg uit waarom persoonlijke beschermingsmiddelen bovenop de veiligheid aan de "
                          "machine komen.",
                  "eerst maak je de machine zelf veilig, dan pas komt de helm erbij; een helm lost een "
                  "onveilige machine niet op", 3),
                 ("open", "Iemand valt op het werk en breekt zijn pols. Welke uitkering komt in beeld?",
                  "de arbeidsongevallenuitkering", 2),
                 ("open", "Noem drie dingen die bij welzijn op het werk horen en niet over ongevallen gaan.",
                  "de werkdruk, de sfeer in de ploeg en pesten op het werk", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Enkel de werkgever heeft een rol in de veiligheid op het werk.", False),
                 ("waar", "Het CPBW is een overlegorgaan binnen het bedrijf zelf.", True),
                 ("waar", "student@work is een vacaturesite.", False),
                 ("waar", "Veiligheid staat ook in het arbeidsreglement, omdat die regels voor iedereen in "
                          "het bedrijf gelden.", True),
                 ("waar", "Welzijn op het werk gaat enkel over het vermijden van ongevallen.", False),
                 ("waar", "Een vakbond geeft advies en verdedigt je belangen als werknemer.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-totale-aankoopkost-en-het-consumentenkrediet-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De totale aankoopkost en het consumentenkrediet",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Eenmalig of terugkerend?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "de leveringskosten", ["eenmalige kost", "terugkerende kost"], 0),
                 ("kies", "een abonnement van 12 euro per maand", ["eenmalige kost", "terugkerende kost"], 1),
                 ("kies", "een inschrijvingsgeld van 15 euro", ["eenmalige kost", "terugkerende kost"], 0),
                 ("kies", "een verzekering van 5 euro per maand", ["eenmalige kost", "terugkerende kost"], 1),
             ]),
        dict(kop="Reken de totale kostprijs",
             opdracht="Schrijf de bewerking op. Zet de korting altijd eerst van de prijs af.",
             oefeningen=[
                 ("kort", "Een fiets van 800 euro, 10 % korting, 25 euro levering.",
                  "800 − 80 + 25 = 745 euro", "250px"),
                 ("kort", "Een toestel van 240 euro, 15 euro inschrijving, abonnement 12 euro per maand, "
                          "één jaar.", "240 + 15 + 12 × 12 = 399 euro", "250px"),
                 ("kort", "Een laptop van 600 euro, 50 euro korting, verzekering 5 euro per maand, twee jaar.",
                  "600 − 50 + 24 × 5 = 670 euro", "250px"),
                 ("kort", "Een printer van 180 euro met gratis levering, of een van 165 euro met 20 euro "
                          "levering. Welke is voordeliger?", "de printer van 180 euro: 185 is meer dan 180",
                  "260px"),
             ]),
        dict(kop="Welk krediet?",
             opdracht="Schrijf bij elk geval welk van de vier consumentenkredieten het is.",
             oefeningen=[
                 ("tabel", ["Geval", "Welk krediet"], [
                     ["Een wasmachine in twaalf schijven afbetalen.", None],
                     ["Een bedrag lenen en het in vaste schijven terugbetalen.", None],
                     ["Met een kaart tot een bepaald bedrag onder nul kunnen gaan.", None],
                     ["Een wagen voor vier jaar huren, met de kans hem achteraf over te kopen.", None],
                 ], "verkoop op afbetaling · lening op afbetaling · kredietopening · financieringshuur of "
                    "leasing", WL),
             ]),
        dict(kop="De vijf onderdelen en het JKP",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Noem de vijf onderdelen van een consumentenkrediet:",
                  "de looptijd, de rentevoet, het geleende bedrag, het JKP en het maandbedrag", "290px"),
                 ("kort", "JKP staat voor", "jaarlijks kostenpercentage", "220px"),
                 ("kort", "Wat telt het JKP mee dat de rentevoet niet meetelt?",
                  "alle kosten van het krediet, niet enkel de rente", "260px"),
             ]),
        dict(kop="Reken het krediet na",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "Je leent 3 000 euro en betaalt 36 maanden 95 euro. Hoeveel betaal je in totaal "
                          "terug?", "36 × 95 = 3 420 euro", "230px"),
                 ("kort", "Hoeveel rente is dat?", "3 420 − 3 000 = 420 euro", "230px"),
                 ("kort", "Je hebt er al 12 betaald. Hoeveel moet je nog?", "24 × 95 = 2 280 euro", "230px"),
                 ("kort", "Je leent 4 000 euro en betaalt 48 maanden 95 euro. Hoeveel rente is dat?",
                  "48 × 95 = 4 560, dus 4 560 − 4 000 = 560 euro", "250px"),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom je twee kredieten vergelijkt op hun JKP en niet op hun rentevoet.",
                  "het JKP telt alle kosten mee, de rentevoet enkel de rente; een lage rentevoet met veel "
                  "dossierkosten blijft duur", 3),
                 ("open", "Wat doet een langere looptijd met je maandbedrag en met je totale kost?",
                  "het maandbedrag wordt kleiner en de totale kost groter: je betaalt langer rente", 3),
                 ("open", "Noem drie dingen die helpen om kredietproblemen te vermijden.",
                  "een spaarbuffer aanleggen, je uitgaven en inkomsten opvolgen in een budgetplan, en "
                  "kredieten vergelijken op hun JKP voor je tekent", 3),
                 ("open", "Noem de gevolgen van te veel lenen, zoals de fiche ze noemt.",
                  "je raakt je maandelijkse aflossingen niet meer betaald, je komt in een schuldenspiraal "
                  "terecht en je moet een beroep doen op schuldbemiddeling", 3),
                 ("open", "Wat is de plicht van de verkoper in een verkoopovereenkomst, en wat die van de "
                          "koper?",
                  "de verkoper moet leveren wat is afgesproken, in de afgesproken staat; de koper moet "
                  "betalen", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Een commerciële korting gaat eerst van de prijs af.", True),
                 ("waar", "Alle producten hebben hetzelfde btw-tarief.", False),
                 ("waar", "Een verkoop op afbetaling en een lening op afbetaling zijn hetzelfde.", False),
                 ("waar", "Bij een leasing ben je meteen eigenaar.", False),
                 ("waar", "Het JKP ligt nooit lager dan de rentevoet.", True),
                 ("waar", "Kredieten stapelen is wat je in de problemen brengt.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-persoonlijk-budget-en-je-administratie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het persoonlijk budget en je administratie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Inkomst of uitgave, en welke soort?",
             opdracht="Vul de tabel aan. Gebruik de woorden van de fiche.",
             oefeningen=[
                 ("tabel", ["Geval", "Welke soort"], [
                     ["Je loon komt elke maand binnen.", None],
                     ["Je verkoopt eenmalig je oude fiets.", None],
                     ["Je huur van 750 euro per maand.", None],
                     ["Je boodschappen, die de ene maand meer kosten dan de andere.", None],
                     ["Je ketel valt vandaag stuk en moet hersteld worden.", None],
                     ["Je plant volgend jaar een grote reis.", None],
                 ], "terugkerende inkomst · toevallige inkomst · vaste uitgave · variabele uitgave · "
                    "onvoorziene uitgave · uitzonderlijke uitgave", WL),
             ]),
        dict(kop="Welke woorden horen bij wat?",
             opdracht="Vul in.",
             oefeningen=[
                 ("kort", "Terugkerend en toevallig gaan over de", "inkomsten", W),
                 ("kort", "Vast en variabel gaan over de", "uitgaven", W),
                 ("kort", "Hoeveel soorten uitgaven noemt de fiche?", "vier", W),
                 ("kort", "Hoeveel soorten inkomsten noemt de fiche?", "twee", W),
             ]),
        dict(kop="Reken het budget",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "Je verdient 1 750 euro en geeft 1 480 euro uit. Hoeveel kan je sparen?",
                  "1 750 − 1 480 = 270 euro", "230px"),
                 ("kort", "2 100 euro in, 900 euro vaste en 650 euro variabele uitgaven. Hoeveel blijft "
                          "over?", "2 100 − 900 − 650 = 550 euro", "250px"),
                 ("kort", "1 900 euro in, 820 euro vast, 540 euro variabel, 120 euro onvoorzien. Hoeveel "
                          "blijft over?", "1 900 − 820 − 540 − 120 = 420 euro", "250px"),
                 ("kort", "2 350 euro in en je wil 300 euro sparen. Hoeveel mag je uitgeven?",
                  "2 350 − 300 = 2 050 euro", "230px"),
             ]),
        dict(kop="De zeven factoren",
             opdracht="Schrijf bij elke vraag de factor uit de fiche.",
             oefeningen=[
                 ("tabel", ["De vraag die je stelt", "Welke factor"], [
                     ["Heb ik dit echt nodig of wil ik het graag?", None],
                     ["Hoeveel kan ik maandelijks afbetalen zonder in de problemen te komen?", None],
                     ["Hoelang gaat het mee en wat betekent het voor het milieu?", None],
                     ["Wat kost het me extra om te lenen in plaats van te betalen?", None],
                     ["Hou ik genoeg over voor wat ik niet zag aankomen?", None],
                 ], "noodzakelijkheid · terugbetalingscapaciteit · duurzaamheid · financieringskost · "
                    "spaarbuffer", WL),
             ]),
        dict(kop="Je administratie",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Noem de drie aankoopbewijzen uit de fiche:",
                  "de factuur, het kasticket en de aankoopovereenkomst", "270px"),
                 ("kort", "Waarvoor hou je je garantiebewijs bij?",
                  "om een defect binnen de garantieperiode te laten herstellen", "280px"),
                 ("kort", "Wat is een individuele rekening?",
                  "het jaaroverzicht van wat je werkgever je betaalde", "270px"),
                 ("kort", "Welk document uit het rijtje is níet van jouw administratie?",
                  "het arbeidsreglement: dat is van het bedrijf", "250px"),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg het verschil uit tussen een onvoorziene en een uitzonderlijke uitgave, en "
                          "wat dat betekent voor je sparen.",
                  "een onvoorziene zie je niet aankomen, een uitzonderlijke wel; daarom kan je voor een "
                  "uitzonderlijke uitgave sparen en hou je voor een onvoorziene een buffer klaar", 4),
                 ("open", "Iemand rekent in zijn budget enkel met zijn vaste uitgaven. Wat loopt er mis?",
                  "hij laat drie van de vier soorten uitgaven weg: de variabele, de onvoorziene en de "
                  "uitzonderlijke; zijn plan ziet er goed uit en klopt niet", 4),
                 ("open", "Leg het verschil uit tussen de aankoopkost en de financieringskost.",
                  "de aankoopkost is wat het product kost, de financieringskost is wat het lenen erbovenop "
                  "kost: de totale rente over de looptijd", 3),
                 ("open", "Iemand twijfelt tussen een wasmachine van 400 euro die zes jaar meegaat en een "
                          "van 700 euro die vijftien jaar meegaat. Welke factor weegt hier het zwaarst, en "
                          "waarom?",
                  "de duurzaamheid: per jaar kost de duurste minder, en dat is precies wat duurzaamheid "
                  "hier betekent", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Een variabele uitgave keert niet terug.", False),
                 ("waar", "Een budgetplan toont hoeveel je kan sparen.", True),
                 ("waar", "Terugkerend en toevallig zijn de twee soorten uitgaven.", False),
                 ("waar", "Een spaarbuffer dient om een vaste uitgave te betalen.", False),
                 ("waar", "Een kasticket geldt als aankoopbewijs.", True),
                 ("waar", "De fiche noemt zeven factoren bij een aankoopkeuze.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-sparen-beleggen-en-de-invloed-van-inflatie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sparen, beleggen en de invloed van inflatie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke rekening past?",
             opdracht="Schrijf bij elke situatie de rekening die het best past.",
             oefeningen=[
                 ("tabel", ["Situatie", "Welke rekening"], [
                     ["Mijn loon moet ergens binnenkomen en mijn facturen gaan eraf.", None],
                     ["Ik wil elke maand iets opzij zetten en er altijd aan kunnen.", None],
                     ["Dit geld heb ik de komende drie jaar zeker niet nodig.", None],
                     ["Ik moet er volgende maand een reis mee betalen.", None],
                 ], "zichtrekening · spaarrekening · termijnrekening · spaar- of zichtrekening", WL),
             ]),
        dict(kop="Reken de rente",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "2 000 euro aan 2 % per jaar. Hoeveel rente na één jaar?",
                  "2 % van 2 000 = 40 euro", "230px"),
                 ("kort", "5 000 euro aan 3 % per jaar. Hoeveel rente na één jaar?",
                  "3 % van 5 000 = 150 euro", "230px"),
                 ("kort", "1 500 euro aan 4 % per jaar. Hoeveel rente na één jaar?",
                  "4 % van 1 500 = 60 euro", "230px"),
                 ("kort", "800 euro aan 2,5 % per jaar. Hoeveel rente na één jaar?",
                  "2,5 % van 800 = 20 euro", "230px"),
             ]),
        dict(kop="Welke beleggingsvorm?",
             opdracht="Schrijf bij elke omschrijving de vorm uit de fiche.",
             oefeningen=[
                 ("rij", [("een lening aan een bedrijf of een overheid, met een afgesproken rente",
                           "obligatie"),
                          ("een stukje eigendom van een bedrijf", "beursaandeel")], None, WW),
                 ("rij", [("een mand met veel verschillende beleggingen samen", "beleggingsfonds"),
                          ("een digitale munt zonder centrale bank", "cryptomunt")], None, WW),
             ]),
        dict(kop="Schuldeiser of mede-eigenaar?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Je koopt een obligatie van een bedrijf.", ["schuldeiser", "mede-eigenaar"], 0),
                 ("kies", "Je koopt een aandeel van een bedrijf.", ["schuldeiser", "mede-eigenaar"], 1),
             ]),
        dict(kop="De vijf factoren",
             opdracht="Schrijf bij elke vraag de factor uit de fiche.",
             oefeningen=[
                 ("tabel", ["De vraag die je stelt", "Welke factor"], [
                     ["Hoelang kan ik dit geld missen?", None],
                     ["Wat houd ik er netto aan over?", None],
                     ["Hoeveel schommeling kan ik aan?", None],
                     ["Waarvoor spaar of beleg ik eigenlijk?", None],
                     ["Begrijp ik waarin ik stap?", None],
                 ], "de duur · de rentevoet en de inflatie · het risico · mijn financieel doel · "
                    "mijn kennis van de markt", WL),
             ]),
        dict(kop="Inflatie",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat inflatie is en wat ze met je geld doet.",
                  "inflatie is de algemene stijging van de prijzen, waardoor geld minder waard wordt; met "
                  "hetzelfde bedrag koop je na een jaar minder dan ervoor", 3),
                 ("open", "Je spaarrente is 2 % en de inflatie 3 %. Wat gebeurt er met je koopkracht, en "
                          "waarom?",
                  "ze daalt: de prijzen stijgen sneller dan je spaargeld, dus je hebt meer euro's en je "
                  "kan er minder mee kopen", 3),
                 ("open", "Leg uit wat samengestelde rente is en waarom vroeg beginnen sparen daarbij "
                          "uitmaakt.",
                  "samengestelde rente is rente die je ook op de rente van de vorige jaren krijgt, dus een "
                  "spaarpot groeit sneller naarmate hij langer blijft staan", 4),
                 ("open", "Iemand van achttien spaart voor een woning over twintig jaar en kan tegen "
                          "schommelingen. Wat zeggen de factoren van de fiche hier?",
                  "een deel beleggen kan passen: de lange termijn en de risicobereidheid wijzen die kant op; "
                  "alles in één munt steken is geen spreiding maar een gok", 4),
                 ("open", "Leg uit waarom een termijnrekening meestal meer opbrengt dan een spaarrekening.",
                  "je zet het geld voor een afgesproken tijd vast, dus de bank weet hoelang ze erover kan "
                  "beschikken en betaalt daarvoor meer", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Rente krijg je als je spaart en betaal je als je leent.", True),
                 ("waar", "Een hoger risico levert altijd een hogere opbrengst op.", False),
                 ("waar", "Een beleggingsfonds bestaat uit één enkele belegging.", False),
                 ("waar", "Een spaarrekening is een van de vier beleggingsvormen uit de fiche.", False),
                 ("waar", "Je kan even makkelijk aan het geld op een termijnrekening als op een "
                          "spaarrekening.", False),
                 ("waar", "Bij inflatie wordt je spaargeld in koopkracht minder waard.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-verzekeringen-een-schadegeval-en-de-polis-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verzekeringen, een schadegeval en de polis",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welke verzekering?",
             opdracht="Schrijf bij elk geval de verzekering uit het rijtje van vijf.",
             oefeningen=[
                 ("tabel", ["Geval", "Welke verzekering"], [
                     ["Een kind trapt een bal door het raam van de buren.", None],
                     ["Je rijdt met de auto tegen een paaltje.", None],
                     ["Je woning loopt waterschade op door brand bij de buren.", None],
                     ["Een jongere rijdt met zijn bromfiets tegen een geparkeerde auto.", None],
                     ["Je hebt een advocaat nodig in een geschil na een ongeval.", None],
                 ], "familiale verzekering · autoverzekering · brandverzekering · verzekering bromfiets · "
                    "rechtsbijstandsverzekering", WL),
             ]),
        dict(kop="Verantwoordelijk of aansprakelijk?",
             opdracht="Vul in wie wat is.",
             oefeningen=[
                 ("rij", [("wie het gedaan heeft, is", "verantwoordelijk"),
                          ("wie er volgens de wet voor opdraait, is", "juridisch aansprakelijk")], None, WW),
                 ("open", "Een kind van zes trapt een bal door het raam van de buren. Wie is "
                          "verantwoordelijk en wie is juridisch aansprakelijk?",
                  "het kind is verantwoordelijk voor wat het deed, de ouders zijn juridisch aansprakelijk "
                  "voor de schade", 3),
             ]),
        dict(kop="Wie is wie in een polis?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Rol", "Wie dat is"], [
                     ["de verzekeringsnemer", None],
                     ["de verzekerde", None],
                     ["de verzekeraar", None],
                     ["de begunstigde", None],
                 ], "wie het contract afsluit en de premie betaalt · de persoon die gedekt is · de "
                    "maatschappij die het risico draagt en uitbetaalt · wie de uitbetaling ontvangt", WL),
                 ("open", "Een moeder sluit een familiale verzekering af waarin ook haar dochter gedekt is. "
                          "Wie is wie?",
                  "de moeder is verzekeringsnemer, de dochter is verzekerde", 2),
             ]),
        dict(kop="Reken de franchise",
             opdracht="Schrijf de bewerking op.",
             oefeningen=[
                 ("kort", "800 euro schade, 200 euro franchise. Hoeveel krijg je?",
                  "800 − 200 = 600 euro", "220px"),
                 ("kort", "1 500 euro schade, 250 euro franchise. Hoeveel betaalt de verzekeraar?",
                  "1 500 − 250 = 1 250 euro", "220px"),
                 ("kort", "900 euro schade, 150 euro franchise. Hoeveel krijg je uitbetaald?",
                  "900 − 150 = 750 euro", "220px"),
                 ("kort", "2 200 euro schade, 400 euro franchise. Hoeveel krijg je?",
                  "2 200 − 400 = 1 800 euro", "220px"),
             ]),
        dict(kop="De schadeaangifte",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Noem vier gegevens die in een schadeaangifte horen:",
                  "de datum en het uur, de aard van de schade, de getuige, de verantwoordelijke, de "
                  "juridisch aansprakelijke en de begunstigde", "290px"),
                 ("kort", "Wat is de aard van de schade?", "wat er precies beschadigd is en hoe", "260px"),
                 ("kort", "Waarom vraagt een aangifte naar een getuige?",
                  "om achteraf te kunnen vaststellen wat er precies gebeurd is", "280px"),
             ]),
        dict(kop="In eigen woorden",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom je je verzekert.",
                  "om een schade te kunnen dragen die je zelf niet zou kunnen betalen: je betaalt een kleine "
                  "premie om een groot risico niet alleen te moeten dragen", 3),
                 ("open", "Leg het verschil uit tussen de premie en de schadevergoeding.",
                  "de premie betaal je om verzekerd te zijn en gaat van jou naar de verzekeraar; de "
                  "schadevergoeding ontvang je en gaat de andere kant op", 3),
                 ("open", "Waarom bestaat een franchise, en wat doet een hogere franchise met je premie?",
                  "om kleine schades niet door de verzekering te laten lopen, waardoor de premie lager "
                  "blijft; een hogere franchise gaat meestal samen met een lagere premie, want je draagt "
                  "meer zelf", 4),
                 ("open", "Iets staat niet bij het verzekerd risico in je polis, maar de schade is heel "
                          "ernstig. Wordt het uitbetaald?",
                  "nee: enkel wat in de polis als verzekerd risico staat, is gedekt", 2),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Verantwoordelijk en juridisch aansprakelijk betekenen hetzelfde.", False),
                 ("waar", "De familiale verzekering dekt de schade die je met je auto veroorzaakt.", False),
                 ("waar", "De verzekeringsnemer en de verzekerde kunnen twee verschillende personen zijn.",
                  True),
                 ("waar", "De premie is het bedrag dat je bij schade ontvangt.", False),
                 ("waar", "De polis is het contract waarin je verzekering beschreven staat.", True),
                 ("waar", "Een hospitalisatieverzekering staat in het rijtje van vijf uit de fiche.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-tekstverwerking-met-word-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tekstverwerking met Word",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Tekenopmaak of alineaopmaak?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "cursief", ["tekenopmaak", "alineaopmaak"], 0),
                 ("kies", "regelafstand", ["tekenopmaak", "alineaopmaak"], 1),
                 ("kies", "markeren", ["tekenopmaak", "alineaopmaak"], 0),
                 ("kies", "inspringen", ["tekenopmaak", "alineaopmaak"], 1),
                 ("kies", "tekengrootte", ["tekenopmaak", "alineaopmaak"], 0),
                 ("kies", "uitlijning", ["tekenopmaak", "alineaopmaak"], 1),
                 ("kies", "doorhalen", ["tekenopmaak", "alineaopmaak"], 0),
                 ("kies", "de afstand tussen alinea's", ["tekenopmaak", "alineaopmaak"], 1),
             ]),
        dict(kop="Wat doet het?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Opmaak", "Wat ze doet"], [
                     ["superscript", None],
                     ["subscript", None],
                     ["markeren", None],
                     ["doorhalen", None],
                     ["uitvullen", None],
                 ], "kleine tekens iets boven de regel (m²) · kleine tekens iets onder de regel (H₂O) · "
                    "een gekleurde achtergrond achter de tekst · een streep door de tekst, die leesbaar "
                    "blijft · de tekst sluit links én rechts netjes aan", WL),
             ]),
        dict(kop="Wat doe je?",
             opdracht="Schrijf telkens één of twee zinnen.",
             oefeningen=[
                 ("open", "Je wil dat één woord midden in een zin vet staat. Wat doe je, en waarom?",
                  "dat woord selecteren en op vet klikken: vet is tekenopmaak en werkt enkel op wat je "
                  "selecteert", 3),
                 ("open", "Je wil de regelafstand van een alinea aanpassen. Moet je iets selecteren?",
                  "nee: regelafstand is alineaopmaak, dus je cursor in de alinea volstaat", 2),
                 ("open", "Je wil een titel over de drie kolommen van je tabel laten lopen. Wat doe je?",
                  "de drie cellen van de bovenste rij samenvoegen", 2),
             ]),
        dict(kop="De paginaopmaak",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Noem de drie onderdelen van de paginaopmaak:",
                  "de marges, de afdrukstand en het formaat", "250px"),
                 ("kort", "Marges zijn", "de witte rand rond de tekst op een blad", "260px"),
                 ("kort", "De afdrukstand bepaalt of het blad", "staand of liggend staat", "200px"),
                 ("kort", "Noem de twee andere namen voor staand en liggend:", "portret en landschap",
                  "200px"),
             ]),
        dict(kop="Tabellen",
             opdracht="Vul in of leg uit.",
             oefeningen=[
                 ("rij", [("de lijnen rond en in de cellen heten", "randen"),
                          ("de kleur of het patroon als achtergrond heet", "arcering")], None, W),
                 ("open", "Leg het verschil uit tussen cellen samenvoegen en cellen splitsen.",
                  "samenvoegen maakt van meerdere cellen één grotere; splitsen maakt van één cel meerdere", 3),
                 ("open", "Je hebt een tabel met vier rijen en wil er een vijfde onderaan. Wat doe je?",
                  "een rij toevoegen onder de laatste rij", 2),
             ]),
        dict(kop="Afdrukken en PDF",
             opdracht="Antwoord kort of leg uit.",
             oefeningen=[
                 ("kort", "Noem drie dingen die je bij het afdrukken kan instellen:",
                  "de sortering, enkel- of dubbelzijdig, en kleur", "260px"),
                 ("open", "Waarom sla je een document op als PDF?",
                  "zodat de opmaak overal hetzelfde blijft en niemand het zomaar wijzigt", 3),
                 ("open", "Je document telt twaalf bladzijden en je voegt er vooraan een toe. Wat gebeurt er "
                          "met automatische paginanummering, en waarom is dat handig?",
                  "alle nummers schuiven vanzelf op; zelf nummers typen zou betekenen dat je alles moet "
                  "hertypen", 3),
                 ("open", "Waarvoor dient een kop- en voettekst?",
                  "voor tekst die bovenaan of onderaan op elke bladzijde terugkomt, zoals een paginanummer "
                  "of de documentnaam", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Markeren en tekstkleur veranderen doen hetzelfde.", False),
                 ("waar", "Superscript staat boven de regel en subscript eronder.", True),
                 ("waar", "Een opsomming kan je achteraf niet meer wijzigen.", False),
                 ("waar", "Een PDF kan je in Word even makkelijk bewerken als een gewoon document.", False),
                 ("waar", "Marges, afdrukstand en formaat horen samen bij de paginaopmaak.", True),
                 ("waar", "Cellen splitsen en cellen samenvoegen zijn hetzelfde.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-rekenblad-excel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het rekenblad Excel",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoe heet het?",
             opdracht="Vul in.",
             oefeningen=[
                 ("kort", "het vakje waar een rij en een kolom elkaar kruisen", "een cel", W),
                 ("kort", "de kolomletter en het rijnummer samen, zoals B7", "een celadres", W),
                 ("kort", "een groep cellen samen, zoals A1 tot en met A10", "een bereik", W),
                 ("kort", "het bestand met al zijn tabbladen", "een werkmap", W),
                 ("kort", "één tabblad in dat bestand", "een werkblad", W),
                 ("kort", "het vierkantje rechtsonder in een selectie", "de vulgreep", W),
             ]),
        dict(kop="Schrijf het bereik",
             opdracht="Noteer het bereik zoals Excel het schrijft.",
             oefeningen=[
                 ("rij", [("van C2 tot en met C9", "C2:C9"), ("van A1 tot en met A20", "A1:A20")], None, W),
                 ("rij", [("van B4 tot en met F4", "B4:F4"), ("van D10 tot en met D25", "D10:D25")], None, W),
             ]),
        dict(kop="Welke notatie of opmaak?",
             opdracht="Schrijf bij elke omschrijving de juiste term.",
             oefeningen=[
                 ("tabel", ["Omschrijving", "Welke notatie of opmaak"], [
                     ["voor een bedrag, met het muntteken erbij", None],
                     ["je typt 0,25 en ziet 25 %", None],
                     ["een cel kleurt vanzelf als de inhoud aan een regel voldoet", None],
                     ["van meerdere cellen één cel maken met de tekst in het midden", None],
                     ["de hoek waaronder de tekst in de cel staat", None],
                 ], "valuta · percentage · voorwaardelijke opmaak · samenvoegen en centreren · "
                    "de tekststand", WL),
             ]),
        dict(kop="Welke functie?",
             opdracht="Schrijf de Nederlandse naam van de functie.",
             oefeningen=[
                 ("rij", [("alle getallen in een bereik optellen", "SOM"),
                          ("optellen en delen door het aantal", "GEMIDDELDE")], None, "140px"),
                 ("rij", [("het kleinste getal geven", "MIN"), ("het grootste getal geven", "MAX")],
                  None, "140px"),
                 ("rij", [("een ander resultaat naargelang een voorwaarde", "ALS"),
                          ("iets opzoeken in de eerste kolom van een tabel", "VERT.ZOEKEN")],
                  None, "140px"),
             ]),
        dict(kop="Relatief of absoluut?",
             opdracht="Kruis aan en schrijf er in één regel bij wat er gebeurt als je kopieert.",
             oefeningen=[
                 ("kies", "A1", ["relatieve verwijzing", "absolute verwijzing"], 0),
                 ("kies", "$A$1", ["relatieve verwijzing", "absolute verwijzing"], 1),
                 ("kort", "In B2 staat =SOM(A1:A3). Je sleept de formule naar B3. Wat staat er dan?",
                  "=SOM(A2:A4)", "160px"),
                 ("kort", "In C5 staat =SOM(B1:B4). Je sleept de formule naar C6. Wat staat er dan?",
                  "=SOM(B2:B5)", "160px"),
                 ("open", "In C1 staat het btw-percentage. Je wil in een hele kolom de btw van elke prijs "
                          "berekenen. Welke verwijzing gebruik je naar C1, en waarom?",
                  "een absolute verwijzing met dollartekens: zonder zou C1 mee opschuiven naar C2, C3 en zo "
                  "verder, en dan reken je met een leeg vakje", 4),
             ]),
        dict(kop="Welke grafiek past?",
             opdracht="Schrijf bij elke vraag het grafiektype uit de fiche.",
             oefeningen=[
                 ("tabel", ["Wat je wil tonen", "Welke grafiek"], [
                     ["het aandeel van elk deel in een geheel", None],
                     ["hoe iets stijgt of daalt over de maanden", None],
                     ["waarden naast elkaar vergelijken, staand", None],
                     ["het verband tussen twee reeksen getallen", None],
                 ], "cirkeldiagram · lijngrafiek · kolomgrafiek · spreiding", WL),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Een werkmap kan meerdere werkbladen bevatten.", True),
                 ("waar", "Een bereik noteer je met een puntkomma tussen de twee celadressen.", False),
                 ("waar", "Met de vulgreep kan je ook formules doortrekken.", True),
                 ("waar", "Voorwaardelijke opmaak verandert de waarde in de cel.", False),
                 ("waar", "Een formule in Excel hoeft niet met een isgelijkteken te beginnen.", False),
                 ("waar", "GEMIDDELDE en MIN geven altijd hetzelfde resultaat.", False),
                 ("waar", "Een boxplot staat bij de grafiektypes van deze fiche.", False),
                 ("waar", "Een nieuwe rij komt boven de geselecteerde rij te staan.", True),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-presenteren-met-powerpoint-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Presenteren met PowerPoint",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Hoe heet het?",
             opdracht="Vul in.",
             oefeningen=[
                 ("kort", "één bladzijde van je presentatie", "een dia", W),
                 ("kort", "het vaste patroon van vakken op een dia", "de indeling of lay-out", "180px"),
                 ("kort", "het kader waarin je tekst op een dia zet", "een tekstvak", W),
                 ("kort", "het effect bij het wisselen naar de volgende dia", "een diaovergang", "160px"),
                 ("kort", "het effect op iets dat op de dia zelf staat", "een animatie", W),
                 ("kort", "een exacte kopie van een dia bij zetten", "dupliceren", W),
             ]),
        dict(kop="Overgang of animatie?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "het effect tussen dia 3 en dia 4", ["diaovergang", "animatie"], 0),
                 ("kies", "de tekst verschijnt één regel per keer", ["diaovergang", "animatie"], 1),
                 ("kies", "een vorm op de dia schuift binnen", ["diaovergang", "animatie"], 1),
                 ("kies", "het beeld vervaagt terwijl de volgende dia opkomt", ["diaovergang", "animatie"], 0),
             ]),
        dict(kop="Hyperlink of actieknop?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Element", "Wat het doet"], [
                     ["hyperlink", None],
                     ["actieknop", None],
                 ], "hyperlink: je klikt erop en komt op een website of op een andere dia uit · "
                    "actieknop: een knop die je zelf op de dia zet en die bij een klik iets uitvoert", WL),
                 ("open", "Je wil tijdens het presenteren met één klik naar een dia achteraan kunnen "
                          "springen. Wat zet je klaar, en waarom?",
                  "een hyperlink of een actieknop naar die dia; anders moet je door alle dia's ertussen "
                  "klikken", 3),
             ]),
        dict(kop="Welke afdruk?",
             opdracht="Schrijf bij elke omschrijving de soort afdruk en voor wie ze is.",
             oefeningen=[
                 ("tabel", ["Omschrijving", "Welke afdruk", "Voor wie"], [
                     ["meerdere dia's op één blad", None, None],
                     ["één dia met jouw notities eronder", None, None],
                     ["enkel de tekst, zonder beelden en opmaak", None, None],
                 ], "hand-out, voor het publiek · notitiepagina, voor de spreker · overzicht, om je "
                    "verhaal na te lezen", "160px"),
             ]),
        dict(kop="pptx of ppsm?",
             opdracht="Kruis aan of vul in.",
             oefeningen=[
                 ("kies", "opent om te bewerken", ["pptx", "ppsm"], 0),
                 ("kies", "start bij het openen meteen als diavoorstelling", ["pptx", "ppsm"], 1),
                 ("kort", "De s in ppsm staat voor", "show", W),
                 ("open", "Waarom bewaart iemand een presentatie als ppsm in plaats van als pptx?",
                  "zodat ze bij het openen meteen als diavoorstelling begint, bijvoorbeeld op een beurs of "
                  "in een wachtzaal", 3),
             ]),
        dict(kop="Welke weergave of aanpassing?",
             opdracht="Schrijf telkens één of twee zinnen.",
             oefeningen=[
                 ("open", "Je wil tijdens het presenteren je eigen notities zien, maar het publiek niet. "
                          "Wat gebruik je?",
                  "de presentatorweergave: jij ziet de dia met je notities erbij, het publiek enkel de dia",
                  3),
                 ("open", "Je wil de volgorde van je dia's veranderen. Welke weergave gebruik je?",
                  "de diasorteerder, waar alle dia's als miniaturen naast elkaar staan", 2),
                 ("open", "Je wil op elke dia dezelfde achtergrond en hetzelfde lettertype. Wat gebruik je?",
                  "een thema of ontwerp dat voor de hele presentatie geldt", 2),
                 ("open", "Een dia staat volgeschreven in kleine letters. Wat is de beste aanpassing, en "
                          "waarom?",
                  "de tekst over meerdere dia's verdelen en groter laten staan: een dia is geen blad "
                  "papier, en wat je voorleest hoort niet voluit op het scherm", 4),
                 ("open", "Je verwijdert dia 3 uit een presentatie van tien dia's. Wat gebeurt er?",
                  "je houdt negen dia's over en de volgende schuiven op: dia 4 wordt dia 3", 3),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Een animatie werkt op iets wat op de dia staat.", True),
                 ("waar", "Een dia dupliceren is hetzelfde als een dia verwijderen.", False),
                 ("waar", "De indeling van een dia kan je achteraf nog veranderen.", True),
                 ("waar", "Een diaovergang kan je enkel voor alle dia's tegelijk instellen.", False),
                 ("waar", "Een hyperlink kan ook naar een andere dia in dezelfde presentatie verwijzen.",
                  True),
                 ("waar", "Een hand-out en een notitiepagina zijn twee namen voor dezelfde afdruk.", False),
                 ("waar", "Een diavoorstelling kan je starten vanaf de eerste dia of vanaf de dia waar je "
                          "staat.", True),
                 ("waar", "Etiketten horen bij de afdrukken van een presentatie.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-veilig-en-correct-online-recht-phishing-en-netiquette-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig en correct online: recht, phishing en netiquette",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Welk recht?",
             opdracht="Vul in.",
             oefeningen=[
                 ("kort", "het recht van wie een werk gemaakt heeft", "het auteursrecht", "180px"),
                 ("kort", "het recht van wie herkenbaar op een foto staat", "het portretrecht", "180px"),
                 ("kort", "het recht dat je persoonsgegevens beschermt", "het privacyrecht", "180px"),
                 ("kort", "Hoeveel jaar na het overlijden van de maker loopt het auteursrecht nog door?",
                  "zeventig jaar", W),
             ]),
        dict(kop="Auteursrecht of portretrecht?",
             opdracht="Kruis aan.",
             oefeningen=[
                 ("kies", "Je nam de foto.", ["auteursrecht", "portretrecht"], 0),
                 ("kies", "Je staat herkenbaar op de foto.", ["auteursrecht", "portretrecht"], 1),
                 ("kies", "Je schreef de tekst.", ["auteursrecht", "portretrecht"], 0),
             ]),
        dict(kop="Creative commons",
             opdracht="Antwoord kort of leg uit.",
             oefeningen=[
                 ("kort", "Noem de drie voorwaarden die een maker aan een creative commons licentie kan "
                          "hangen:",
                  "naamsvermelding, niet commercieel gebruiken en niet bewerken", "290px"),
                 ("kort", "Hoe staat de naamsvermelding in de licenties afgekort?", "BY", "100px"),
                 ("open", "Leg uit wat creative commons is en waarom je de maker dan niets meer apart moet "
                          "vragen.",
                  "het is een licentie waarmee de maker vooraf toelating geeft, onder voorwaarden; hij heeft "
                  "dus al gezegd wat mag, maar je moet je wel aan die voorwaarden houden", 4),
                 ("open", "Een foto staat onder creative commons met naamsvermelding. Wat moet je doen?",
                  "de naam van de maker bij de foto zetten waar je ze gebruikt", 2),
             ]),
        dict(kop="Wat doe je?",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Je vindt online een mooie foto zonder enige vermelding erbij. Wat mag je ervan "
                          "uitgaan?",
                  "dat ze beschermd is en je toelating nodig hebt; geen vermelding betekent niet vrij", 3),
                 ("open", "Je nam op een feest een foto van een vriendin en wil die op je verhaal zetten. "
                          "Wat heb je nodig, en waarom?",
                  "haar toelating: jij hebt het auteursrecht, maar zij heeft het portretrecht omdat ze "
                  "herkenbaar op de foto staat", 3),
                 ("open", "Iemand zet zonder te vragen een foto van jou op zijn pagina. Wat kan je doen?",
                  "hem vragen de foto weg te halen, want je hebt portretrecht; lukt dat niet, dan kan je het "
                  "bij het platform zelf melden", 3),
                 ("open", "Een website vraagt bij een inschrijving voor een nieuwsbrief ook je "
                          "rijksregisternummer. Wat klopt daar niet aan?",
                  "er worden meer gegevens gevraagd dan voor dat doel nodig zijn: voor een nieuwsbrief is "
                  "een mailadres genoeg", 3),
             ]),
        dict(kop="Wachtwoorden en phishing",
             opdracht="Antwoord kort of leg uit.",
             oefeningen=[
                 ("kort", "Noem de drie kenmerken van een sterk wachtwoord:",
                  "het is lang, niet te raden en je gebruikt het maar op één plaats", "290px"),
                 ("kort", "Hoe heet de extra code naast je wachtwoord als tweede slot?",
                  "tweestapsverificatie", "220px"),
                 ("kort", "Noem de drie dingen die een phishingbericht vaak verraden:",
                  "een afzender waarvan het adres net niet juist is, haast, en een link naar een adres dat "
                  "je niet herkent", "290px"),
                 ("open", "Je krijgt een mail van je bank met de vraag om via een link je gegevens te "
                          "bevestigen. Wat doe je, en waarom?",
                  "niet klikken en zelf naar de site of de app van je bank gaan: een bank vraagt je nooit om "
                  "via een link je codes te bevestigen", 4),
                 ("open", "Leg uit waarom hetzelfde wachtwoord op verschillende sites gebruiken een slecht "
                          "idee is.",
                  "raakt het op één site buiten, dan liggen al je andere rekeningen open, want wie het heeft "
                  "probeert het gewoon elders", 3),
             ]),
        dict(kop="Nepnieuws en cyberpesten",
             opdracht="Schrijf telkens twee of drie zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat nepnieuws is en wat het verschil is met een vergissing in een krant.",
                  "nepnieuws zijn onjuiste berichten die met opzet als echt nieuws verspreid worden; de "
                  "opzet maakt het verschil", 3),
                 ("open", "Je ziet een schokkend bericht op sociale media zonder bron erbij. Wat doe je "
                          "eerst?",
                  "nakijken of ernstige media hetzelfde bericht ook brengen; hoeveel keer iets gedeeld is "
                  "zegt niets over de waarheid", 3),
                 ("open", "Een foto bij een bericht lijkt verdacht. Hoe kan je ze nakijken?",
                  "de foto omgekeerd opzoeken en zien waar ze eerder opdook; oude foto's duiken vaak bij een "
                  "nieuwe gebeurtenis op", 3),
                 ("open", "Iemand uit je klas wordt in een groepsgesprek dag na dag belachelijk gemaakt. "
                          "Wat is de beste reactie?",
                  "bewijs bewaren met een schermafbeelding, het melden, en de persoon zelf niet alleen "
                  "laten; niet meedoen is nodig maar niet genoeg", 4),
                 ("open", "Iemand stuurt een foto van een klasgenoot door die duidelijk niet bedoeld was om "
                          "gedeeld te worden. Hoe zit dat?",
                  "dat mag niet, ook al heeft hij de foto zelf gekregen: een foto krijgen is geen toelating "
                  "om ze verder te sturen, en daar gaan portretrecht en privacy over", 4),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="Kruis aan. Schrijf bij een onjuiste uitspraak in één regel wat er wel klopt.",
             oefeningen=[
                 ("waar", "Het auteursrecht moet je aanvragen.", False),
                 ("waar", "Een werk onder creative commons mag je altijd zonder voorwaarden gebruiken.",
                  False),
                 ("waar", "Je mag een stukje uit een boek citeren als je de bron vermeldt.", True),
                 ("waar", "Gegevens die een bedrijf over jou bijhoudt, mag je nooit inkijken.", False),
                 ("waar", "Een bericht in vlot Nederlands met het juiste logo kan geen phishing zijn.",
                  False),
                 ("waar", "Een wachtwoord deel je nooit, ook niet met iemand die zegt dat hij van de "
                          "helpdesk is.", True),
                 ("waar", "Bij cyberpesten is een schermafbeelding nemen een goede eerste stap.", True),
                 ("waar", "Een bericht volledig in hoofdletters tikken hoort bij goede netiquette.", False),
             ]),
    ],
)
