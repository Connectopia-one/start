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

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-identiteit-de-lagen-de-factoren-en-het-wereldbeeld-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="De drie woorden antwoorden op drie verschillende vragen: waar komt je identiteit "
                   "vandaan (relationeel), waaruit bestaat ze (gelaagd), en blijft ze gelijk (dynamisch)?",
            waarom=[
                "Let op het verschil: relationeel gaat over de omgang met anderen, gelaagd over de "
                "delen waaruit je identiteit bestaat. De eerste zin noemt anderen, de tweede lagen.",
                "Let erop dat allebei over verandering gaan, één keer in het algemeen en één keer met "
                "een voorbeeld. Dynamisch betekent net dat: niet vast.",
            ],
        ),
        dict(
            aanpak="Zoek bij elk geval de laag waarin het thuishoort. Vraag je af of het over je "
                   "lichaam, je karakter, je gezin, je land of je groep gaat.",
            waarom=[
                "Let op het verschil tussen het supranationale aspect en een subcultuur: het eerste "
                "gaat over wat boven je land uitstijgt, zoals Europeaan zijn, het tweede over een "
                "groep met eigen gewoonten binnen de samenleving.",
            ],
        ),
        dict(
            aanpak="Eén vraag: hoort deze laag bij jou alleen, of bij een groep waar je deel van "
                   "uitmaakt? Je gezin en je karakter zijn van jou, een subcultuur is van een groep.",
            waarom=[
                "Let erop dat je familiale achtergrond bij de persoonlijke identiteit hoort, ook al "
                "gaat het over andere mensen. Het is jouw geschiedenis, geen groep waar je lid van bent.",
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Elk van de drie heeft zijn eigen kern: anders behandeld worden om een kenmerk "
                   "(discriminatie), ergens bij horen (verbondenheid), of mensen in twee groepen "
                   "indelen (wij-zij-denken).",
            waarom=[
                "Noem ook waarom het discriminatie is, zoals het antwoord doet: ze wordt anders "
                "behandeld om een kenmerk van haar identiteit, niet om haar spel.",
                None,
                "Let erop dat het wij-zij-denken hier van de groep zelf komt. Dat is precies waarom "
                "de volgende reeks vraagt of het altijd van buitenaf komt.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste zet je in één regel wat er "
                   "wel klopt, want dat is wat het examen ook vraagt.",
            waarom=[
                "Niet waar: een identiteit is dynamisch en verandert in de loop van je leven. "
                "Sommige lagen liggen vast, de identiteit als geheel niet.",
                None,
                "Niet waar: een groep kan het zelf doen, zoals de vereniging die over wij en zij "
                "spreekt. Het kan van buiten komen en van binnen.",
                None,
                "Niet waar: een mensbeeld gaat over hoe je de mens ziet, een wereldbeeld over hoe je "
                "de wereld als geheel ziet. Ze hangen samen en zijn niet hetzelfde.",
                None,
            ],
        ),
        dict(
            aanpak="Vier open vragen. Antwoord in twee of drie zinnen en gebruik de begrippen van de "
                   "fiche met hun naam.",
            waarom=[
                "Noem beide delen: dat het in de omgang met anderen vorm krijgt, en dat het dus niet "
                "alleen vanbinnen zit.",
                "Noem de keten: discriminatie breekt de verbondenheid af, en wie niet meer meehoort "
                "gaat zichzelf ook bij de andere groep rekenen.",
                "Noem er twee, zoals de vraag zegt: neutraliteit en de bescherming van "
                "persoonsgegevens.",
                "Geef een eigen voorbeeld en leg uit wat er kantelt. Dat het over de wereld als "
                "geheel gaat en niet over één persoon, is wat het een wereldbeeld maakt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-samenleven-in-diversiteit-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="De vijf vormen vragen vijf keer hetzelfde: waarin verschillen de mensen hier? In "
                   "hun lichaam, hun positie in de samenleving, hun geloof, hun cultuur of hun "
                   "geaardheid?",
            waarom=[
                "Let op het verschil tussen sociale en culturele diversiteit: het eerste gaat over je "
                "plaats in de samenleving, zoals inkomen of opleiding, het tweede over gewoonten, "
                "taal en tradities.",
            ],
        ),
        dict(
            aanpak="Let op het voorvoegsel: multi betekent meerdere, mono betekent één. En let bij de "
                   "drie andere op de vraag wie zich aanpast.",
            waarom=[
                None,
                "Let op het verschil tussen integratie en inclusie: bij integratie beweegt de "
                "nieuwkomer, bij inclusie beweegt de groep mee. Exclusie is geen van de twee.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist alles: wie verandert er iets? Verandert enkel de nieuwkomer, dan "
                   "is het integratie; verandert de omgeving mee, dan is het inclusie.",
            waarom=[
                None,
                "Let erop dat de school zelf verbouwt en haar lessen aanpast. Dat de omgeving mee "
                "verandert, is het kenmerk van inclusie.",
                "Let erop dat het hier niet om een gebouw gaat maar om een uur. Ook een uur "
                "verschuiven is inclusie, zolang de groep zelf beweegt.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je af of het verschil hier iets oplevert of iets bemoeilijkt, en noem dan "
                   "het begrip van de fiche: uitwisseling van ideeën, economische uitwisseling, "
                   "groepsdenken, belangen of referentiekaders.",
            waarom=[
                None,
                "Let erop dat groepsdenken juist het tegenovergestelde van diversiteit is: iedereen "
                "volgt dezelfde richting en niemand brengt nog iets anders in.",
                "Let op het verschil met de laatste: hier willen twee mensen iets anders "
                "(belangen), daar beoordelen ze hetzelfde anders (referentiekaders).",
                None,
                "Let erop dat beide ouders hetzelfde zien en toch anders oordelen. Dat komt uit hun "
                "eigen schooljaren, en dat is wat een referentiekader is.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                None,
                "Niet waar: groepsdenken staat bij de uitdagingen. Het is net wat diversiteit "
                "verliest als niemand nog iets anders durft in te brengen.",
                "Niet waar: inclusie laat iedereen echt meedoen, exclusie houdt mensen buiten. Ze "
                "zijn elkaars tegengestelde.",
                None,
                None,
                "Niet waar: de fiche noemt er drie. Tel ze na in je leerbundel, want zo'n aantal "
                "komt op het examen terug.",
            ],
        ),
        dict(
            aanpak="Drie open vragen. Antwoord in twee of drie zinnen en gebruik de begrippen van de "
                   "fiche met hun naam.",
            waarom=[
                "Noem allebei met de vraag erbij wie beweegt. Dat ene verschil is het hele antwoord.",
                "Noem beide delen: wat een referentiekader is, en waarom het tot een ander oordeel "
                "leidt over dezelfde situatie.",
                "Let erop dat de vraag één situatie vraagt met beide kanten erin. Twee losse "
                "voorbeelden antwoorden niet op wat er staat.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-respectvol-samenleven-communicatie-grenzen-en-samenwerken-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Kijk niet of iemand het eens is, maar wat de uitspraak doet: benoemt ze een zorg "
                   "(constructief), of breekt ze de ander af (destructief)?",
            waarom=[
                "Let erop dat deze spreker het oneens is en toch constructief blijft. Hij noemt zijn "
                "zorg en valt de persoon niet aan.",
                None,
                "Let erop dat een grens stellen ook constructief is. Niet nu voor de hele groep "
                "weigert het gesprek niet, het verzet het.",
                "Let op iedereen vindt: de spreker verschuilt zich achter een groep die hij niet "
                "genoemd heeft. Dat is destructief, ook zonder scheldwoord.",
            ],
        ),
        dict(
            aanpak="De vier verschillen in wat er gebeurt en waarom: herhaald kwetsen (pesten), "
                   "buitenhouden (uitsluiting), anders behandelen om een kenmerk (discriminatie), of "
                   "om afkomst of huidskleur (racisme).",
            waarom=[
                "Let op het verschil tussen discriminatie en racisme: racisme is een discriminatie om "
                "afkomst, huidskleur of origine. Het is dus een soort van, geen apart geval.",
            ],
        ),
        dict(
            aanpak="Pesten heeft drie kenmerken: het herhaalt zich, het is gericht op dezelfde "
                   "persoon, en de machten zijn ongelijk. Ontbreekt er een, dan is het iets anders.",
            waarom=[
                "Niet waar: dit is een conflict en geen pesten. Eén ruzie die uitgepraat wordt, "
                "herhaalt zich niet en is niet eenzijdig.",
                "Let erop dat week na week en dezelfde leerling de twee kenmerken geven die het "
                "pesten maken.",
                None,
                "Niet waar: de gevolgen kunnen lang na het stoppen blijven duren. Dat het gedrag "
                "ophoudt, betekent niet dat de schade weg is.",
            ],
        ),
        dict(
            aanpak="Loop de zes kenmerken één voor één af en vraag bij elk: klopt dit hier? Het "
                   "kenmerk waarop je nee moet antwoorden, is het ontbrekende.",
            waarom=[
                "Let op het verschil tussen specifiek en geïnformeerd: specifiek betekent dat de ja "
                "voor dit en niet voor iets anders geldt, geïnformeerd dat je wist waarvoor je ja zei. "
                "En actueel betekent: nu, niet vorige maand.",
            ],
        ),
        dict(
            aanpak="Vraag je af of de situatie regels heeft die je niet zelf kiest: een gesprek met "
                   "een werkgever of de directie heeft die, een avond met vrienden niet.",
            waarom=[
                None,
                "Let erop dat een mail zowel formeel als informeel kan zijn. Het middel beslist niet, "
                "de situatie wel, en dat komt in de volgende reeks terug.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: je kan iemand respecteren en het grondig oneens blijven. Respect gaat "
                "over hoe je met de ander omgaat, niet over de uitkomst.",
                "Niet waar: toestemming moet duidelijk gegeven worden. Wie zwijgt, heeft geen ja "
                "gezegd, en dat is een van de zes kenmerken.",
                None,
                None,
                "Niet waar: wie toekijkt, houdt het gedrag mee in stand of kan het stoppen. Een "
                "omstaander heeft wel een rol, en dat is net waarom de handelingsopties bestaan.",
                "Niet waar: altijd toegeven betekent dat je je eigen grens niet verdedigt. Respect "
                "voor jezelf is net wel zeggen waar je grens ligt.",
            ],
        ),
        dict(
            aanpak="Vier open vragen. Antwoord in twee of drie zinnen en noem de begrippen van de "
                   "fiche met hun naam.",
            waarom=[
                "Noem het onderscheid tussen wat en hoe. Dat er na een constructief gesprek iets "
                "staat, ook zonder akkoord, is de kern.",
                "Noem de twee delen: steunen en melden. En noem waarom wegkijken erger is dan niets "
                "doen: het laat het gedrag doorgaan.",
                "Noem beide delen: wat groepsdruk is, en welk kenmerk van toestemming hij aantast. "
                "Dat is vrijwillig.",
                "Noem er drie en werk er één uit, zoals de vraag zegt. Drie noemen zonder uitleg is "
                "een half antwoord.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-ongevallen-herkennen-en-eerste-hulp-geven-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vier nummers, vier taken: 112 voor ziekenwagen en brandweer, 101 voor de politie, "
                   "070 245 245 voor het antigifcentrum, 1733 voor de huisarts van wacht.",
            waarom=[
                "Let erop dat een inbraak geen medische hulp vraagt, dus 101. Zwaar bloedverlies is "
                "levensgevaar, dus 112.",
                "Let op bij bewustzijn: daarom mag je het antigifcentrum bellen. Bij "
                "bewustzijnsverlies bel je 112, en dat komt verder in deze bundel terug.",
                None,
            ],
        ),
        dict(
            aanpak="Houd de vier letsels van elkaar gescheiden aan wat er beschadigd is: het bot, de "
                   "spier, het gewricht, of de banden rond het gewricht.",
            waarom=[
                "Let op het verschil tussen ontwrichting en verstuiking: bij een ontwrichting is het "
                "bot uit het gewricht, bij een verstuiking zijn de banden te ver uitgerekt.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Zeg niet wat je zou doen maar wat je vermoedt, met de woorden van de fiche. En "
                   "zeg erbij of het een noodsituatie is.",
            waarom=[
                "Let erop dat je twee mogelijkheden mag noemen. Van buitenaf kan je een botbreuk niet "
                "van een ontwrichting onderscheiden, en dat hoeft ook niet.",
                "Let erop dat niet kunnen hoesten het gevaarlijke teken is. Wie nog hoest, krijgt nog "
                "lucht.",
                None,
            ],
        ),
        dict(
            aanpak="Eén vraag: zegt het item hoe je je gedraagt (basisprincipe) of wat je in welke "
                   "orde doet (stap)? De vier stappen zijn de handelingen op elkaar.",
            waarom=[
                None,
                "Let erop dat zorg voor veiligheid een stap is en de eerste. Het gaat over wat je "
                "doet, niet over hoe je je opstelt.",
                None,
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="De orde volgt de logica: eerst jezelf en de omgeving veilig, dan kijken wat er is, "
                   "dan hulp roepen, dan verder helpen tot die hulp er is.",
            waarom=[
                "Let erop dat beoordelen op de tweede plaats komt en niet op de eerste. Wie meteen "
                "naar het slachtoffer loopt, slaat de veiligheid over.",
                None,
            ],
        ),
        dict(
            aanpak="Leg het verhaal naast de vier stappen en zoek welke stap ontbreekt of van plaats "
                   "verwisselde. Schrijf in je antwoord welk nummer het is.",
            waarom=[
                "Noem de reden erbij, zoals het antwoord doet: zonder veiligheid word je zelf het "
                "tweede slachtoffer.",
                "Noem waarom die beoordeling nodig is: de centrale moet weten wat ze stuurt. Van "
                "thuis uit bellen zonder gekeken te hebben, kost dus tijd.",
                "Let erop dat hier geen stap ontbreekt maar het nummer fout is. Bij "
                "bewustzijnsverlies is het altijd 112.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: 101 is de politie. Voor een ziekenwagen bel je 112.",
                None,
                "Niet waar: bij een kneuzing is er geen bot gebroken. Ze doen allebei pijn en dat is "
                "het enige wat ze delen.",
                None,
                "Niet waar: het is de derde. Daarna volgt nog verdere eerste hulp tot de hulp er is.",
                "Niet waar: getuigen noteren staat niet bij de zes basisprincipes. Die gaan over hoe "
                "je je opstelt: rustig blijven, besmetting vermijden, psychosociale hulp geven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-een-hartstilstand-reanimatie-en-de-aed-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Twee tekens volstaan om te beginnen: geen reactie en geen normale ademhaling. Je "
                   "moet dus niets anders vaststellen voor je start.",
            waarom=[
                None,
                "Let op normaal: een enkele zucht of een happende beweging is geen normale ademhaling. "
                "Wacht er niet op om te starten.",
                "Let erop dat het hart er nog wel is, maar niet meer pompt. Daarom nemen jouw "
                "compressies die pomp over.",
            ],
        ),
        dict(
            aanpak="De orde volgt wat het slachtoffer nodig heeft: eerst vaststellen, dan hulp laten "
                   "komen, dan een AED laten halen, en pas dan met je handen aan het werk.",
            waarom=[
                "Let erop dat bellen op de tweede plaats komt, dus vóór de compressies. Dat lijkt "
                "tijdverlies en is het niet: de ambulance moet onderweg zijn terwijl jij pompt.",
                None,
            ],
        ),
        dict(
            aanpak="Leg het verhaal naast de zes stappen en zoek wat verwisseld, overgeslagen of te "
                   "vroeg gestopt wordt. Zeg in je antwoord ook wat het wel moest zijn.",
            waarom=[
                "Noem de reden erbij: elke minuut later vertrekt de ambulance ook later. Dat is "
                "waarom bellen voor de compressies komt.",
                "Let erop dat één zucht geen herstel is. Je stopt pas als de ambulancier het "
                "overneemt.",
                "Noem waarom het misgaat: in een zetel zakt het lichaam mee, dus bereiken je "
                "compressies het hart niet. Leg de persoon op de vloer.",
                "Noem beide redenen: de meting wordt verstoord en jij staat zelf in de stroombaan. "
                "Daarom zegt het toestel ook luidop dat niemand mag aanraken.",
            ],
        ),
        dict(
            aanpak="Vul de tabel in de orde van je eigen lichaam in: waar je handen liggen, hoe je "
                   "armen staan, wat de borstkas doet, en pas dan de beademing.",
            waarom=[
                "Let op volledig laten terugkomen: het hart vult zich net in die terugveer. Blijven "
                "duwen zonder lossen maakt de compressies minder waard.",
            ],
        ),
        dict(
            aanpak="Drie gevallen, één leidraad: jij blijft bij het slachtoffer en pompen stopt nooit. "
                   "Alles wat elders moet gebeuren, laat je door iemand anders of door je telefoon doen.",
            waarom=[
                "Noem beide delen: bellen en de luidspreker aanzetten. Je handen vrij houden is de "
                "reden, en de centrale loodst je door de stappen.",
                "Let erop dat jij de compressies doet en niet het bellen of het zoeken. Jij bent al "
                "bij het slachtoffer, dus jij verliest het minst door te blijven.",
                "Let erop dat overnemen niet hetzelfde is als stoppen. Een wissel mag, een pauze niet.",
            ],
        ),
        dict(
            aanpak="Houd de drie letters vast: automatisch, extern, defibrillator. Het toestel meet "
                   "zelf en zegt zelf wat je moet doen.",
            waarom=[
                None,
                "Let erop dat automatisch over de beslissing gaat: hij meet het ritme en bepaalt zelf "
                "of een stoot nodig is. Je kan er dus niemand mee verkeerd behandelen.",
                "Let erop dat aanzetten het eerste is, nog voor je de kleefstroken plaatst. Vanaf dan "
                "zegt het toestel zelf wat er moet gebeuren.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: bij een hartstilstand pompt het hart niet meer. Een te snel kloppend hart "
                "is iets anders.",
                None,
                "Niet waar: je handen liggen midden op de borstkas. Links duwen werkt niet, ook al "
                "zit het hart daar iets meer.",
                "Niet waar: je armen moeten gestrekt zijn, met je schouders recht boven je handen. Met "
                "gebogen ellebogen duw je met je armen in plaats van met je lichaamsgewicht.",
                "Niet waar: de stabiele zijligging is voor iemand die bewusteloos is en wel normaal "
                "ademt. Bij een hartstilstand reanimeer je.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-inkomsten-en-de-uitgaven-van-de-overheid-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke inkomst af waar ze vandaan komt: van je inkomen of je bezit "
                   "(direct), van wat je koopt (indirect), van wat de overheid zelf bezit, of van iets "
                   "anders zoals een boete of een document.",
            waarom=[
                "Let op de boete en het paspoort: daar koop je geen product en je betaalt niet op je "
                "inkomen. Zulke gevallen vallen onder de diverse inkomsten.",
            ],
        ),
        dict(
            aanpak="Eén vraag: betaal je ze rechtstreeks aan de overheid op je inkomen of je bezit, of "
                   "zit ze in de prijs van iets dat je koopt?",
            waarom=[
                None,
                "Let erop dat de bedrijfsvoorheffing van je loon gaat, dus op je inkomen. Dat je "
                "werkgever ze doorstort, verandert daar niets aan.",
                None,
                "Let erop dat de onroerende voorheffing op een bezit staat, je woning. Een belasting "
                "op bezit is direct.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat de uitgave moet opleveren: iets waar iedereen gebruik van maakt, "
                   "steun aan wie het nodig heeft, ruimte voor cultuur en sport, of een duw voor de "
                   "economie.",
            waarom=[
                "Let op het verschil tussen de glasvezel en de politie: glasvezel in een "
                "industriezone dient de economische groei, politie en onderwijs zijn collectieve "
                "behoeften.",
            ],
        ),
        dict(
            aanpak="Hier wordt gevraagd wat de fiche zelf opsomt, dus leer die rijtjes zoals ze er "
                   "staan. Noem ze volledig, want elk voorbeeld telt.",
            waarom=[
                None,
                None,
                "Let erop dat infocampagnes bij het maatschappelijk leven staan, naast cultuur en "
                "sport. Dat is minder voorspelbaar dan de twee andere.",
            ],
        ),
        dict(
            aanpak="Vier open vragen. Antwoord in twee of drie zinnen en noem de soorten met hun naam.",
            waarom=[
                "Noem beide soorten met het voorbeeld erbij. Dat een gemeente moet kiezen, is net "
                "waarom die indeling bestaat.",
                "Noem het begrip: een inkomst uit overheidskapitaal. En noem het verschil met een "
                "belasting: er wordt niets bij de burger geheven.",
                "Noem de omschrijving en twee voorbeelden, zoals de vraag zegt. Dat de hele "
                "samenleving ervan gebruikmaakt, is de kern.",
                "Noem de reden: met de twee samen beperkt de overheid de ongelijkheid. Enkel de "
                "inkomsten of enkel de uitgaven bekijken, laat de helft weg.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                None,
                "Niet waar: cultuur en sport horen bij het maatschappelijk leven. Sociale uitgaven "
                "zijn de steun aan wie het nodig heeft, zoals sociale woningen.",
                "Niet waar: de overheid financiert de sociale zekerheid, dus het is een uitgave en "
                "wel een sociale.",
                "Niet waar: de fiche noemt vier soorten inkomsten en giften zitten daar niet bij. Bij "
                "de diverse inkomsten staan bijvoorbeeld boetes en het betalen voor een paspoort.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-sociale-zekerheid-uitkeringen-en-herverdeling-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke situatie af waarom het inkomen wegvalt: geen werk, een ongeval "
                   "op het werk, een ziekte door het werk, een gewone ziekte, of een overlijden.",
            waarom=[
                "Let op het verschil tussen de tweede en de derde: van een ladder vallen is een "
                "arbeidsongeval, ziek worden van een stof is een beroepsziekte. Plots tegenover "
                "langdurig, dat is het onderscheid.",
            ],
        ),
        dict(
            aanpak="Eén vraag: komt dit geld in de plaats van een loon dat wegvalt "
                   "(vervangingsinkomen), of komt het bovenop een inkomen dat er is (aanvullend)?",
            waarom=[
                None,
                "Let erop dat vakantiegeld bovenop je loon komt. Je loon valt niet weg, dus het is "
                "aanvullend.",
                "Let erop dat een rustpensioen je loon vervangt nadat je gestopt bent. Daarom is het "
                "een vervangingsinkomen en geen aanvulling.",
                "Let erop dat het groeipakket bovenop het gezinsinkomen komt, voor de kosten van "
                "kinderen. Dus aanvullend.",
                None,
            ],
        ),
        dict(
            aanpak="Eén vraag: loopt het via de belastingen (fiscaal) of via een uitkering, een premie "
                   "of een tarief (sociaal)?",
            waarom=[
                None,
                None,
                None,
                "Let erop dat een kansentarief geen belasting is maar een lagere prijs. Daarom is het "
                "een sociale maatregel.",
                "Let erop dat ook verschillende btw-tarieven fiscaal zijn. De maatregel zit in de "
                "belasting zelf, niet in een uitkering.",
                None,
                None,
                "Let erop dat een belastingvermindering geld bij je laat in plaats van je geld te "
                "geven. Ze loopt via de belasting, dus fiscaal.",
            ],
        ),
        dict(
            aanpak="Drie vragen die je uit het hoofd moet kennen. Noem bij de financiering alle drie "
                   "de partijen, want een onvolledig rijtje kost punten.",
            waarom=[
                None,
                None,
                "Let erop dat er drie partijen zijn: de werkgevers, de werknemers en de overheid. Dat "
                "ook de werknemers betalen, zie je op je eigen loonbriefje.",
            ],
        ),
        dict(
            aanpak="Vijf open vragen. Antwoord in twee of drie zinnen en noem de begrippen met hun "
                   "naam.",
            waarom=[
                "Noem het onderscheid plots tegenover langdurig. Dat is het hele verschil tussen de "
                "twee uitkeringen.",
                "Noem beide delen: een hoger percentage bij een hoger inkomen, en dat het via schijven "
                "gebeurt. Dat elk stuk van je inkomen in zijn eigen schijf valt, hoort erbij.",
                "Noem het doel: noodzakelijke producten lichter belasten dan luxe. Zo herverdeelt ook "
                "een indirecte belasting.",
                "Noem beide delen: wat er verschuift en waarom. De bedoeling is de sociale "
                "ongelijkheid beperken.",
                "Noem allebei met wie ze krijgt. Een overlevingspensioen gaat naar de achterblijvende "
                "partner, en dat is wat het van een rustpensioen onderscheidt.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: de werkgevers, de werknemers en de overheid betalen samen. Drie partijen, "
                "geen één.",
                None,
                "Niet waar: het vakantiegeld komt bovenop je loon, dus het is aanvullend. Het staat "
                "wel in het rijtje van zes, en dat is het verschil met de vorige uitspraak.",
                None,
                None,
                "Niet waar: het groeipakket is een sociale maatregel. Het loopt niet via de belasting "
                "maar via een uitkering.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-vraag-aanbod-en-het-marktevenwicht-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Lees de grafiek altijd in dezelfde orde: eerst de assen, dan welke curve welke is, "
                   "en pas dan het snijpunt. V is de vraag, A het aanbod.",
            waarom=[
                "Let erop dat het evenwicht het snijpunt is: daar vragen en aanbieden mensen precies "
                "dezelfde hoeveelheid.",
                None,
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Denk bij elke curve aan wie ze beschrijft: de koper wil minder bij een hogere prijs, "
                   "de verkoper wil meer. Daarom lopen ze tegen elkaar in.",
            waarom=[
                "Let erop dat de twee tegengesteld reageren op dezelfde prijsstijging. Precies daarom "
                "snijden de curven en bestaat er een evenwicht.",
                None,
            ],
        ),
        dict(
            aanpak="Trek altijd het kleinste van het grootste af en kijk dan welke kant groter was. "
                   "Meer aanbod dan vraag is een overschot, meer vraag dan aanbod een tekort.",
            waarom=[
                None,
                "Let erop dat je hier de vraag als eerste schrijft, want die is groter. De uitkomst is "
                "even groot als in de vorige oefening, maar het is een tekort en geen overschot.",
                None,
                None,
                "Let erop dat nul niet betekent dat je je vergist hebt: gelijke vraag en gelijk aanbod "
                "is net het evenwicht. Noem het ook zo.",
            ],
        ),
        dict(
            aanpak="Reken rij per rij het verschil uit en schrijf erbij welke kant groter is. De rij "
                   "waar het verschil nul is, geeft je de evenwichtsprijs en de evenwichtshoeveelheid.",
            waarom=[
                "Let erop dat 200 − 70 = 130 en 180 − 95 = 85. Hoe verder de prijs van het evenwicht "
                "ligt, hoe groter het verschil, en dat kan je als controle gebruiken.",
                None,
                "Let erop dat de evenwichtshoeveelheid 130 stuks is: bij 6 euro zijn vraag en aanbod "
                "allebei 130. Je leest ze af op dezelfde rij als de prijs.",
            ],
        ),
        dict(
            aanpak="Kijk wat er blijft liggen of wat er tekortkomt. Blijft er over, dan vroeg de "
                   "verkoper te veel; is alles te snel weg, dan vroeg hij te weinig.",
            waarom=[
                "Noem beide delen: dat er een overschot is en wat dat over de prijs zegt. Overgebleven "
                "kratten zijn aanbod dat niemand aan die prijs wou.",
                "Let erop dat uitverkocht zijn ook een probleem is: de verkoper had meer kunnen vragen. "
                "Mensen wegsturen betekent vraag die je laat liggen.",
                None,
            ],
        ),
        dict(
            aanpak="Twee open vragen over dezelfde beweging: de prijs schuift naar het evenwicht toe. "
                   "Noem telkens wie de prijs doet bewegen.",
            waarom=[
                "Noem wie beweegt: de verkopers met onverkochte voorraad. Zij zakken met hun prijs tot "
                "het overschot weg is.",
                "Noem wie beweegt: de kopers die meer willen betalen. Daardoor stijgt de prijs tot het "
                "tekort weg is.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: de aanbodcurve stijgt. Bij een hogere prijs willen verkopers net meer "
                "aanbieden, en dat is de vraagcurve die daalt.",
                None,
                "Niet waar: bij één prijs is er of een overschot, of een tekort, of niets van de twee. "
                "Beide samen kan niet.",
                None,
                "Niet waar: de evenwichtsprijs verschuift zodra de vraag of het aanbod verandert. Dat "
                "is net het onderwerp van de volgende bundel.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verschuivingen-op-de-markt-en-de-overheid-die-ingrijpt-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: verandert de prijs van dit product zelf, of verandert er iets anders? "
                   "De prijs zelf doet je op de curve bewegen, al het andere verschuift de curve.",
            waarom=[
                None,
                "Let erop dat de lonen van de kopers buiten deze markt liggen. Daarom verschuift de "
                "hele vraagcurve en beweeg je niet erop.",
                None,
                None,
                "Let erop dat uit de mode raken niets met de prijs te maken heeft. De mensen willen "
                "bij elke prijs minder, dus de curve verschuift.",
            ],
        ),
        dict(
            aanpak="Vraag je eerst af wie het raakt: de kopers (vraag) of de verkopers (aanbod). Meer "
                   "willen of kunnen is naar rechts, minder is naar links.",
            waarom=[
                "Let op de eerste rij: duurdere grondstoffen raken de verkoper, dus het aanbod, en ze "
                "kunnen minder aanbieden, dus naar links. Een goedkoper vergelijkbaar product raakt "
                "de koper en duwt de vraag naar links.",
            ],
        ),
        dict(
            aanpak="Zet in je hoofd de ene curve vast en schuif de andere. Lees dan het nieuwe snijpunt "
                   "af: eerst de prijs, dan de hoeveelheid.",
            waarom=[
                None,
                "Let erop dat de vraag prijs en hoeveelheid dezelfde kant op duwt, en het aanbod ze "
                "tegengesteld beweegt. Dat ene verschil maakt de hele tabel.",
            ],
        ),
        dict(
            aanpak="Drie vragen die je uit het hoofd moet kennen. Noem de drie maatregelen volledig, "
                   "want een onvolledig rijtje kost punten.",
            waarom=[
                None,
                "Let op bepaalde producten: een accijns staat niet op alles, in tegenstelling tot de "
                "btw. Dat is het verschil tussen de twee.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je af wie de maatregel raakt. Een belasting of een subsidie raakt de "
                   "verkoper, dus het aanbod; een premie raakt de koper, dus de vraag.",
            waarom=[
                "Let op het verschil tussen de subsidie en de premie: allebei geven geld, maar de "
                "subsidie duwt het aanbod naar rechts en de prijs naar beneden, de premie duwt de "
                "vraag naar rechts en de prijs naar boven.",
                "Noem alle drie de gevolgen, zoals het antwoord doet: de curve, de prijs en de "
                "hoeveelheid. Dat de prijs stijgt bij een premie, verrast de meeste mensen.",
                "Let erop dat slecht weer het aanbod raakt en niet de vraag. De mensen willen "
                "evenveel, er is gewoon minder.",
            ],
        ),
        dict(
            aanpak="Houd twee dingen vast: een minimumprijs ligt boven het evenwicht en geeft een "
                   "overschot, een maximumprijs ligt eronder en geeft een tekort.",
            waarom=[
                "Let erop dat de vier vakjes samenhangen: waar de prijs ligt, bepaalt wat ze geeft. "
                "Boven het evenwicht blijft er over, eronder komt er tekort.",
                "Let erop dat het antwoord niets is. Een minimumprijs onder het evenwicht ligt aan de "
                "verkeerde kant en doet dus niets.",
                "Let erop dat dit hetzelfde geval is als het vorige, in spiegelbeeld. Daarom mag je "
                "antwoord kort zijn: om dezelfde reden.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: de prijs van het product zelf doet je op de vraagcurve bewegen. Pas iets "
                "anders dan die prijs verschuift de curve.",
                None,
                "Niet waar: een minimumprijs geeft een overschot, want ze ligt boven het evenwicht. "
                "Het tekort hoort bij de maximumprijs.",
                None,
                "Niet waar: de fiche noemt belastingen, premies en subsidies, en minimum- en "
                "maximumprijzen. De productie overnemen staat er niet bij.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-arbeidsovereenkomst-en-het-arbeidsreglement-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: geldt het voor jou alleen of voor iedereen in het bedrijf? Wat enkel "
                   "van jou is, staat in je overeenkomst; wat voor allen geldt, in het reglement.",
            waarom=[
                None,
                "Let op van de hele ploeg: een uurrooster voor allen hoort in het reglement, jouw "
                "eigen uren staan in je contract.",
                None,
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="De drie indelingen antwoorden op drie vragen: wat voor werk (aard), hoe lang "
                   "(duur), en hoeveel uren (omvang).",
            waarom=[
                "Let erop dat bediende en deeltijds uit twee verschillende indelingen komen. Elk "
                "contract heeft van alle drie iets.",
                None,
                "Let erop dat een vervangingsduur bij de duur hoort, ook al staat er geen datum in. "
                "Het einde is er wel, enkel niet op een kalender.",
            ],
        ),
        dict(
            aanpak="Lees elk contract drie keer, één keer per vraag: wat voor werk, hoe lang, hoeveel "
                   "uren. Dan heb je de drie vakjes zonder te twijfelen.",
            waarom=[
                "Let op het derde contract: halve dagen is de omvang, tot de collega terug is de duur. "
                "Twee gegevens in één zin.",
            ],
        ),
        dict(
            aanpak="Vier soorten duur, vier einden: een datum, een afgewerkte opdracht, de terugkeer "
                   "van een collega, of een opzeg door een van de partijen.",
            waarom=[
                "Let erop dat er geen datum in staat en toch een einde: als het dak klaar is. Dat is "
                "wat welomschreven werk betekent.",
                None,
                "Let erop dat onbepaalde duur niet eeuwig betekent. Het contract eindigt wel, maar pas "
                "als een van de twee partijen het beëindigt.",
                None,
            ],
        ),
        dict(
            aanpak="Vier vragen die je uit het hoofd moet kennen. Let bij nachtarbeid op de "
                   "formulering: verboden in principe, met uitzonderingen in de wet.",
            waarom=[
                None,
                "Let erop dat het contract bij een schorsing blijft bestaan. Het werk ligt stil, de "
                "overeenkomst niet, en dat is net het verschil met een beëindiging.",
                "Let op in principe: het verbod is de regel en de uitzonderingen staan in de wet. "
                "Antwoord dus niet gewoon verboden of gewoon toegelaten.",
                "Noem er drie, zoals de vraag zegt. De overeenkomst, het reglement en de loonfiche "
                "zijn de duidelijkste.",
            ],
        ),
        dict(
            aanpak="Vraag je af wie het ontvangt of wie het moet doen. Loon ontvangen is een recht van "
                   "de werknemer, veiligheid bieden een plicht van de werkgever.",
            waarom=[
                "Let erop dat een recht van de ene vaak een plicht van de andere is. Het loon op tijd "
                "betalen is dus ook een plicht van de werkgever.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: arbeider en bediende gaan over de aard van het werk. De duur is een andere "
                "indeling.",
                None,
                None,
                "Niet waar: de fiche noemt bepaalde duur, onbepaalde duur, welomschreven werk en "
                "vervangingsduur. Een proefduur staat er niet als eigen soort bij.",
                "Niet waar: bij een schorsing blijft het contract bestaan en ligt enkel het werk stil.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-van-brutoloon-naar-nettoloon-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de weg vast in drie bedragen en twee inhoudingen: bruto, dan de sociale "
                   "bijdrage eraf, dan belastbaar, dan de bedrijfsvoorheffing eraf, dan netto.",
            waarom=[
                "Let op de orde: de sociale bijdrage gaat eerst, de bedrijfsvoorheffing daarna. "
                "Omwisselen geeft een ander nettoloon, en die orde komt op het examen terug.",
                None,
                None,
                "Let erop dat het bedrag tussen de twee inhoudingen een eigen naam heeft: het "
                "belastbaar loon. Op dat bedrag wordt de voorheffing berekend.",
            ],
        ),
        dict(
            aanpak="Elke bewerking is een aftrekking op de weg van bruto naar netto. Schrijf ze "
                   "volledig op, want het examen vraagt de bewerking en niet enkel het bedrag.",
            waarom=[
                None,
                None,
                None,
                None,
                "Let erop dat je bij een arbeider eerst 108 procent neemt: 2 000 × 1,08 = 2 160 euro. "
                "De bijdrage wordt dus niet op 2 000 berekend maar op 2 160.",
            ],
        ),
        dict(
            aanpak="Drie keer dezelfde vraag: welke van de twee inhoudingen verandert hier? De gezins"
                   "situatie raakt de voorheffing, het statuut van arbeider de sociale bijdrage.",
            waarom=[
                "Noem de reden erbij: bij een arbeider wordt de bijdrage op 108 procent van het bruto "
                "berekend. Het percentage is hetzelfde, het bedrag waarop gerekend wordt niet.",
                "Noem de reden erbij: kinderen ten laste verlagen de bedrijfsvoorheffing. De sociale "
                "bijdrage blijft gelijk, en dat is het onderscheid.",
                "Noem de reden erbij: bij een student gaat er enkel een solidariteitsbijdrage af en "
                "geen voorheffing. Daarom ligt zijn netto dicht bij zijn bruto.",
            ],
        ),
        dict(
            aanpak="Houd twee dingen vast over een studentencontract: er gaat één bijdrage af, en de "
                   "voorheffing hoort er niet bij.",
            waarom=[
                None,
                "Let erop dat de voorheffing wegvalt en niet de sociale bijdrage. De "
                "solidariteitsbijdrage is net een lichtere vorm van die sociale bijdrage.",
            ],
        ),
        dict(
            aanpak="Vier open vragen. Antwoord in twee of drie zinnen en noem de bedragen en de "
                   "instanties met hun naam.",
            waarom=[
                "Noem beide delen: wat voorheffing betekent en wat er bij te veel inhouden gebeurt. "
                "Dat je het na je aangifte terugkrijgt, is het praktische deel.",
                "Noem de reden erbij: een oude regel uit de tijd van dag- en uurlonen. En noem wat "
                "het verandert: niet het percentage maar het bedrag waarop gerekend wordt.",
                "Noem beide delen: het bruto plus de eigen RSZ-bijdrage van de werkgever. Daarom kost "
                "een werknemer meer dan er op zijn contract staat.",
                "Noem de twee doelen apart, zoals het antwoord doet. De ene financiert de sociale "
                "zekerheid, de andere is een voorschot op je belasting.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: de sociale bijdrage gaat eerst, dan de voorheffing. Daartussen ligt het "
                "belastbaar loon.",
                "Niet waar: het belastbaar loon is bruto min de sociale bijdrage. Pas na de "
                "voorheffing houd je het netto over.",
                None,
                "Niet waar: de sociale bijdrage is een percentage van je loon en kijkt niet naar je "
                "gezin. Enkel de voorheffing doet dat.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-welzijn-op-het-werk-en-waar-je-met-vragen-terechtkan-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Leer de afkortingen aan hun eerste letter: C van comité, en de drie diensten aan "
                   "wat ze doen. Schrijf ze volledig uit, want het examen vraagt de hele naam.",
            waarom=[
                "Let erop dat er twee dingen in de naam staan: preventie en bescherming. Vergeet geen "
                "van de twee.",
                None,
                None,
                "Let erop dat er ook beroepsopleiding in staat. De VDAB doet dus meer dan werk zoeken, "
                "en dat is precies wat verder in deze bundel gevraagd wordt.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat de persoon nodig heeft: uren nakijken, een uitkering, een "
                   "opleiding, advies, controle op bijdragen, of iets binnen het bedrijf zelf.",
            waarom=[
                "Let op de laatste rij: een versperde nooduitgang is een zaak voor het CPBW, want dat "
                "overlegt binnen het bedrijf zelf. De andere vragen gaan naar een dienst erbuiten.",
            ],
        ),
        dict(
            aanpak="Houd de drie uit elkaar aan hun kerntaak: de RVA betaalt en regelt uitkeringen, de "
                   "VDAB brengt je aan werk en opleiding, de RSZ int de bijdragen.",
            waarom=[
                None,
                None,
                None,
                "Let erop dat loopbaanonderbreking bij de RVA hoort en niet bij de VDAB. Het gaat over "
                "een uitkering tijdens je onderbreking.",
                "Let op het verschil met het vorige: loopbaanbegeleiding is begeleiding, dus VDAB. "
                "Twee woorden die op elkaar lijken en bij een andere dienst horen.",
            ],
        ),
        dict(
            aanpak="Houd de rollen gescheiden: de werkgever zorgt voor middelen en een veilige "
                   "werkplek, de werknemer gebruikt ze en meldt gevaren.",
            waarom=[
                "Let op voordat: preventie komt voor het ongeval. Wat je na een ongeval doet, is "
                "hulpverlening en geen preventie.",
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Vijf vragen over wat je concreet doet. Antwoord in twee of drie zinnen en noem de "
                   "begrippen van de fiche met hun naam.",
            waarom=[
                "Noem beide delen: melden en de machine niet gebruiken. En noem waarom je zelf niet "
                "herstelt: dat is een zaak voor wie het mag.",
                "Noem het begrip: een preventiemaatregel. Dat onthaal en vorming daaronder vallen, is "
                "wat deze vraag test.",
                "Noem de orde: eerst de machine veilig maken, dan de persoonlijke middelen. Een helm "
                "lost een onveilige machine niet op.",
                "Let erop dat het om een ongeval tijdens het werk gaat, dus de "
                "arbeidsongevallenuitkering. Een beroepsziekte zou een langzaam opgebouwde ziekte zijn.",
                "Noem er drie, zoals de vraag zegt: werkdruk, sfeer en pesten. Dat welzijn meer is dan "
                "veiligheid, komt in de volgende reeks terug.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: ook de werknemer heeft een rol. Hij gebruikt de beschermingsmiddelen en "
                "moet gevaren melden.",
                None,
                "Niet waar: student@work toont hoeveel uren je als student al gewerkt hebt. Voor werk "
                "zoeken is er de VDAB.",
                None,
                "Niet waar: welzijn op het werk gaat ook over werkdruk, sfeer en pesten. Ongevallen "
                "zijn er maar één deel van.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-totale-aankoopkost-en-het-consumentenkrediet-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: betaal je het één keer of elke maand opnieuw? Staat er per maand bij, "
                   "dan is het terugkerend.",
            waarom=[
                None,
                None,
                None,
                None,
            ],
        ),
        dict(
            aanpak="Werk altijd in dezelfde orde: eerst de korting van de prijs af, dan de eenmalige "
                   "kosten erbij, dan de terugkerende kosten maal het aantal maanden.",
            waarom=[
                "Let erop dat 10 procent van 800 gelijk is aan 80. Je rekent de korting dus eerst uit "
                "en daarna tel je de levering erbij.",
                "Let op één jaar: dat is 12 × 12 = 144 euro abonnement. Een jaar omrekenen naar "
                "maanden is waar het hier op draait.",
                "Let op twee jaar: 24 maanden, dus 24 × 5 = 120 euro. Reken de looptijd altijd eerst "
                "om in maanden.",
                "Let erop dat je beide totalen moet uitrekenen voor je vergelijkt: 165 + 20 = 185 "
                "tegenover 180. De laagste prijs is hier niet de laagste kost.",
            ],
        ),
        dict(
            aanpak="Vier kredieten, vier verschillen: een product in schijven, geld in schijven, een "
                   "kaart met een limiet, of huren met een aankoopkans achteraf.",
            waarom=[
                "Let op het verschil tussen de eerste twee: bij een verkoop op afbetaling koop je een "
                "product, bij een lening krijg je geld. Dat ze allebei in schijven lopen, maakt ze "
                "niet hetzelfde.",
            ],
        ),
        dict(
            aanpak="Leer het rijtje van vijf en het verschil tussen de rentevoet en het JKP. Dat "
                   "laatste is de vraag die het vaakst terugkomt.",
            waarom=[
                None,
                None,
                "Let erop dat het JKP ook de dossierkosten en andere kosten meerekent. Daarom "
                "vergelijk je kredieten op het JKP, en dat komt verder in deze bundel terug.",
            ],
        ),
        dict(
            aanpak="Reken altijd eerst het totaal uit (aantal maanden maal maandbedrag) en haal daar "
                   "het geleende bedrag af. Dat verschil is de rente.",
            waarom=[
                None,
                "Let erop dat de rente het verschil is tussen wat je terugbetaalt en wat je leende: "
                "3 420 − 3 000 = 420 euro.",
                "Let erop dat er nog 24 maanden te gaan zijn: 36 − 12 = 24, dus 24 × 95 = 2 280 euro.",
                "Let erop dat je hier twee bewerkingen na elkaar doet: eerst 48 × 95 = 4 560, dan "
                "4 560 − 4 000 = 560 euro. Zelfde maandbedrag, langere looptijd, meer rente.",
            ],
        ),
        dict(
            aanpak="Vijf open vragen. Antwoord in twee of drie zinnen en noem de begrippen van de "
                   "fiche met hun naam.",
            waarom=[
                "Noem beide delen: wat het JKP meeneemt en wat de rentevoet laat liggen. Een lage "
                "rentevoet met zware dossierkosten is het voorbeeld.",
                "Noem allebei, want ze gaan tegen elkaar in: het maandbedrag zakt en de totale kost "
                "stijgt. Dat je langer rente betaalt, is de reden.",
                "Noem er drie, zoals de vraag zegt. Een buffer, een budgetplan en vergelijken op het "
                "JKP zijn de duidelijkste.",
                "Noem de keten zoals de fiche ze geeft: de aflossingen niet meer kunnen betalen, de "
                "schuldenspiraal, en dan schuldbemiddeling.",
                "Noem beide plichten apart. Dat de verkoper in de afgesproken staat moet leveren, "
                "hoort erbij.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                None,
                "Niet waar: er zijn verschillende btw-tarieven, zodat noodzakelijke producten lichter "
                "belast worden dan luxe.",
                "Niet waar: bij een verkoop op afbetaling koop je een product in schijven, bij een "
                "lening krijg je geld dat je in schijven terugbetaalt.",
                "Niet waar: bij een leasing huur je, en pas achteraf kan je het overkopen. Tot dan is "
                "de leasingmaatschappij eigenaar.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-persoonlijk-budget-en-je-administratie-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Beslis eerst of het geld binnenkomt of buitengaat, en kies dan het woord: bij "
                   "inkomsten terugkerend of toevallig, bij uitgaven vast, variabel, onvoorzien of "
                   "uitzonderlijk.",
            waarom=[
                "Let op het verschil tussen de laatste twee: een stukke ketel zie je niet aankomen "
                "(onvoorzien), een geplande reis wel (uitzonderlijk). Dat verschil komt verder in "
                "deze bundel terug.",
            ],
        ),
        dict(
            aanpak="Houd de woordparen bij hun kant: terugkerend en toevallig horen bij de inkomsten, "
                   "vast en variabel bij de uitgaven. En onthoud de aantallen: twee en vier.",
            waarom=[
                None,
                None,
                "Let erop dat er vier soorten uitgaven zijn: vast, variabel, onvoorzien en "
                "uitzonderlijk. Twee hoort bij de inkomsten.",
                None,
            ],
        ),
        dict(
            aanpak="Een budget is één aftrekking: alles wat binnenkomt min alles wat buitengaat. "
                   "Schrijf elke uitgave apart af, dan vergeet je er geen.",
            waarom=[
                None,
                None,
                "Let erop dat je hier drie bedragen aftrekt. Wie er één vergeet, komt op een te mooi "
                "resultaat uit.",
                "Let erop dat de vraag omgekeerd staat: je sparen gaat er eerst af, en wat overblijft "
                "mag je uitgeven. Dat is precies hoe een budgetplan werkt.",
            ],
        ),
        dict(
            aanpak="Elke factor hoort bij één vraag. Lees de vraag in de tabel en zoek het woord dat "
                   "er een naam aan geeft.",
            waarom=[
                "Let op het verschil tussen terugbetalingscapaciteit en spaarbuffer: het eerste gaat "
                "over wat je maandelijks kan afbetalen, het tweede over wat je achter de hand houdt.",
            ],
        ),
        dict(
            aanpak="Vier vragen over je papieren. Houd uit elkaar wat van jou is en wat van het "
                   "bedrijf, want dat is de laatste vraag.",
            waarom=[
                None,
                None,
                "Let erop dat een individuele rekening een jaaroverzicht is en geen bankrekening. De "
                "naam doet anders vermoeden.",
                "Let erop dat het arbeidsreglement voor iedereen in het bedrijf geldt en dus niet van "
                "jou is. Je overeenkomst en je loonfiche wel.",
            ],
        ),
        dict(
            aanpak="Vier open vragen. Antwoord in twee of drie zinnen en noem de soorten en de "
                   "factoren met hun naam.",
            waarom=[
                "Noem beide delen: het verschil zelf en wat het voor je sparen betekent. Voor een "
                "geplande uitgave spaar je, voor een onvoorziene hou je een buffer.",
                "Noem welke drie hij weglaat, zoals het antwoord doet. Dat zijn plan er daardoor te "
                "mooi uitziet, is het gevolg.",
                "Noem allebei met hun eigen woorden. De financieringskost is de totale rente over de "
                "looptijd, dus wat het lenen kost en niet wat het product kost.",
                "Noem de factor en reken het na: 400 euro over zes jaar is ruim 66 euro per jaar, "
                "700 euro over vijftien jaar is nog geen 47 euro per jaar. De duurste is per jaar de "
                "goedkoopste.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: een variabele uitgave keert wel terug, maar met een ander bedrag. Je "
                "boodschappen zijn het voorbeeld.",
                None,
                "Niet waar: terugkerend en toevallig zijn de twee soorten inkomsten. De uitgaven zijn "
                "vast, variabel, onvoorzien en uitzonderlijk.",
                "Niet waar: een spaarbuffer is er voor wat je niet zag aankomen. Een vaste uitgave "
                "staat in je budget en betaal je uit je gewone inkomsten.",
                None,
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-sparen-beleggen-en-de-invloed-van-inflatie-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: wanneer heb je het geld nodig? Vandaag is een zichtrekening, binnen "
                   "enkele maanden een spaarrekening, over jaren een termijnrekening.",
            waarom=[
                "Let op de laatste rij: voor volgende maand kan het op je spaarrekening of op je "
                "zichtrekening staan, maar niet op een termijnrekening. Daar zit het vast.",
            ],
        ),
        dict(
            aanpak="Rente over één jaar is één bewerking: het bedrag maal het percentage. Deel door "
                   "honderd, of reken met een komma.",
            waarom=[
                None,
                None,
                None,
                "Let op het halve procent: 2,5 procent van 800 is 20 euro. Reken met 0,025, dan gaat "
                "de komma je niet in de weg zitten.",
            ],
        ),
        dict(
            aanpak="Vier vormen, vier verhoudingen: lenen aan iemand (obligatie), eigendom (aandeel), "
                   "een mand met veel beleggingen (fonds), of een digitale munt zonder bank.",
            waarom=[
                "Let op het verschil tussen de twee: bij een obligatie leen je geld uit en krijg je "
                "rente, bij een aandeel bezit je een stukje van het bedrijf. Dat komt in de volgende "
                "reeks terug.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je af of je geld uitgeleend hebt of iets gekocht hebt. Uitgeleend maakt je "
                   "schuldeiser, gekocht maakt je mede-eigenaar.",
            waarom=[
                "Let erop dat je als schuldeiser je geld terug moet krijgen, met rente. Je deelt niet "
                "in de winst, en dat is het verschil met een aandeel.",
                None,
            ],
        ),
        dict(
            aanpak="Elke factor hoort bij één vraag. Lees de vraag in de tabel en zoek het woord dat "
                   "er een naam aan geeft.",
            waarom=[
                "Let op de tweede rij: netto overhouden gaat over de rentevoet én de inflatie samen. "
                "Een rente van 2 procent bij 3 procent inflatie levert netto niets op.",
            ],
        ),
        dict(
            aanpak="Vijf open vragen. Antwoord in twee of drie zinnen en noem de begrippen van de "
                   "fiche met hun naam.",
            waarom=[
                "Noem beide delen: wat inflatie is en wat ze met je geld doet. Dat je met hetzelfde "
                "bedrag minder koopt, is de kern.",
                "Noem de rekening erbij: de prijzen stijgen een procent sneller dan je spaargeld. Je "
                "hebt meer euro's en toch minder koopkracht.",
                "Noem beide delen: rente op je rente, en waarom tijd dan meeweegt. Hoe langer het "
                "geld staat, hoe sneller het groeit.",
                "Noem welke factoren meespelen: de lange duur en de risicobereidheid. En noem de grens: "
                "alles in één munt is geen spreiding.",
                "Noem de reden van de kant van de bank: ze weet hoelang ze over je geld kan "
                "beschikken. Daarvoor betaalt ze meer.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                None,
                "Niet waar: een hoger risico kan meer opbrengen en kan je ook geld kosten. Was de "
                "hogere opbrengst zeker, dan was er geen risico.",
                "Niet waar: een fonds is net een mand met veel verschillende beleggingen. Dat is "
                "precies waarvoor het dient.",
                "Niet waar: de vier beleggingsvormen zijn de obligatie, het beursaandeel, het "
                "beleggingsfonds en de cryptomunt. Een spaarrekening is sparen, geen beleggen.",
                "Niet waar: op een termijnrekening staat je geld voor een afgesproken tijd vast. Dat "
                "is net waarom ze meer opbrengt.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verzekeringen-een-schadegeval-en-de-polis-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je af waarmee de schade gebeurde: met een voertuig, in of aan je woning, of "
                   "gewoon door iemand van het gezin. Dat kiest de verzekering.",
            waarom=[
                "Let op het verschil tussen de eerste en de vierde: een bal van een kind valt onder de "
                "familiale verzekering, een bromfiets niet. Voor elk voertuig is er een eigen polis.",
            ],
        ),
        dict(
            aanpak="Houd de twee woorden gescheiden: verantwoordelijk is wie het deed, juridisch "
                   "aansprakelijk is wie de wet laat betalen. Dat kan dezelfde persoon zijn en vaak niet.",
            waarom=[
                None,
                "Noem allebei met hun eigen naam. Dat de ouders betalen voor wat hun kind deed, is "
                "precies waarvoor een familiale verzekering bestaat.",
            ],
        ),
        dict(
            aanpak="Vier rollen in één contract: wie het sluit en betaalt, wie gedekt is, wie uitbetaalt "
                   "en wie het geld ontvangt.",
            waarom=[
                "Let op het verschil tussen de verzekeringsnemer en de verzekerde: de ene betaalt, de "
                "andere is gedekt. Dat ze niet dezelfde hoeven te zijn, is de volgende oefening.",
                "Noem de twee rollen met hun naam. Hier is de dochter niet degene die betaalt, en toch "
                "is zij de verzekerde.",
            ],
        ),
        dict(
            aanpak="Een franchise is één aftrekking: de schade min het deel dat je zelf draagt. Wat "
                   "overblijft, betaalt de verzekeraar.",
            waarom=[
                None,
                None,
                None,
                "Let erop dat de vraag vier keer hetzelfde is, met andere bedragen. Schrijf de "
                "bewerking op, ook als je het antwoord ziet.",
            ],
        ),
        dict(
            aanpak="Drie vragen over het formulier. Noem bij de eerste vier gegevens, en kies ze uit "
                   "het rijtje van de fiche.",
            waarom=[
                "Let erop dat de fiche er meer dan vier noemt. Je mag er dus vier uit kiezen, maar "
                "de datum en het uur en de aard van de schade horen er altijd bij.",
                None,
                "Noem de reden: een getuige laat achteraf vaststellen wat er gebeurde. Zonder getuige "
                "staat jouw woord tegen dat van de ander.",
            ],
        ),
        dict(
            aanpak="Vier open vragen. Antwoord in twee of drie zinnen en noem de begrippen van de "
                   "fiche met hun naam.",
            waarom=[
                "Noem de verhouding tussen de twee bedragen: een kleine premie tegen een groot risico. "
                "Dat is waarom verzekeren werkt.",
                "Noem beide richtingen: de premie gaat van jou naar de verzekeraar, de vergoeding komt "
                "terug. Dat onderscheid wordt vaak verwisseld.",
                "Noem beide delen: waarvoor een franchise dient en wat ze met je premie doet. Meer zelf "
                "dragen betekent een lagere premie.",
                "Let erop dat het antwoord nee is, hoe ernstig de schade ook is. Enkel wat als "
                "verzekerd risico in je polis staat, is gedekt, en daarom lees je die polis.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: verantwoordelijk is wie het deed, juridisch aansprakelijk is wie ervoor "
                "opdraait volgens de wet.",
                "Niet waar: schade met een auto valt onder de autoverzekering. De familiale dekt de "
                "schade van het gezin buiten de voertuigen.",
                None,
                "Niet waar: de premie betaal je om verzekerd te zijn. Wat je bij schade ontvangt, is "
                "de schadevergoeding.",
                None,
                "Niet waar: de vijf uit de fiche zijn de familiale, de auto-, de brand-, de bromfiets- "
                "en de rechtsbijstandsverzekering. Een hospitalisatieverzekering bestaat wel, maar "
                "staat niet in dat rijtje.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstverwerking-met-word-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag: werkt het op de letters die je selecteert (tekenopmaak) of op de hele "
                   "alinea waar je cursor staat (alineaopmaak)?",
            waarom=[
                None,
                "Let erop dat regelafstand nooit op één woord kan werken. Alles wat de vorm van de "
                "hele alinea bepaalt, is alineaopmaak.",
                None,
                None,
                None,
                "Let erop dat uitlijning over de hele alinea gaat: links, rechts, gecentreerd of "
                "uitgevuld. Eén woord uitlijnen bestaat niet.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Vul elke rij in met wat je op het blad ziet gebeuren. Denk aan een voorbeeld: m² "
                   "voor superscript, H₂O voor subscript.",
            waarom=[
                "Let op het verschil tussen markeren en doorhalen: markeren legt een kleur achter de "
                "tekst, doorhalen zet een streep erdoor terwijl de tekst leesbaar blijft.",
            ],
        ),
        dict(
            aanpak="Drie vragen die allemaal op hetzelfde onderscheid teruggaan: tekenopmaak heeft een "
                   "selectie nodig, alineaopmaak niet.",
            waarom=[
                "Noem beide delen: selecteren en op vet klikken. En noem waarom: vet werkt enkel op "
                "wat je selecteert.",
                "Let erop dat het antwoord nee is. Je cursor in de alinea volstaat, en dat is het "
                "praktische gevolg van het verschil.",
                "Let erop dat je hier samenvoegt en niet centreert. Een titel over drie kolommen is "
                "één cel geworden.",
            ],
        ),
        dict(
            aanpak="Vier vragen over het blad zelf. Leer het rijtje van drie en de twee andere namen "
                   "voor staand en liggend.",
            waarom=[
                None,
                None,
                None,
                "Let erop dat portret staand is en landschap liggend. Een landschap is breder dan "
                "hoog, en dat is precies het beeld.",
            ],
        ),
        dict(
            aanpak="Drie vragen over tabellen. Houd de twee woorden gescheiden: randen zijn de lijnen, "
                   "arcering is de achtergrond.",
            waarom=[
                None,
                "Noem allebei met hun richting: samenvoegen gaat van veel naar één, splitsen van één "
                "naar veel. Ze zijn elkaars omgekeerde.",
                None,
            ],
        ),
        dict(
            aanpak="Vier vragen over afdrukken en opslaan. Antwoord in één of twee zinnen en noem de "
                   "reden erbij.",
            waarom=[
                None,
                "Noem beide redenen: de opmaak blijft gelijk en niemand wijzigt het zomaar. Dat is "
                "waarom je een sollicitatiebrief als pdf verstuurt.",
                "Noem beide delen: dat de nummers vanzelf opschuiven en waarom dat handig is. Zelf "
                "nummers typen zou betekenen dat je ze alle twaalf hertypt.",
                "Noem waarvoor het dient en een voorbeeld, zoals het antwoord doet. Dat het op elke "
                "bladzijde terugkomt, is de kern.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: markeren zet een kleur achter de tekst, tekstkleur verandert de letters "
                "zelf.",
                None,
                "Niet waar: je kan een opsomming achteraf aanpassen, van bolletjes naar nummers en "
                "omgekeerd.",
                "Niet waar: een pdf is net gemaakt om niet zomaar gewijzigd te worden. Daarvoor open "
                "je het oorspronkelijke document.",
                None,
                "Niet waar: samenvoegen maakt van meerdere cellen één, splitsen van één cel meerdere. "
                "Ze doen het omgekeerde van elkaar.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-rekenblad-excel-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Zes namen, van klein naar groot: cel, celadres, bereik, werkblad, werkmap. De "
                   "vulgreep is het enige dat geen onderdeel is maar een hulpmiddel.",
            waarom=[
                None,
                None,
                None,
                "Let op het verschil tussen een werkmap en een werkblad: de map is het bestand, het "
                "blad is één tabblad erin. Eén map kan veel bladen hebben.",
                None,
                None,
            ],
        ),
        dict(
            aanpak="Een bereik schrijf je met een dubbele punt tussen het eerste en het laatste "
                   "celadres, zonder spaties.",
            waarom=[
                "Let erop dat de dubbele punt tot en met betekent. C2:C9 zijn dus acht cellen, C2 en "
                "C9 meegerekend.",
                None,
            ],
        ),
        dict(
            aanpak="Vraag je af of het over de weergave van een getal gaat (valuta, percentage) of "
                   "over de cel zelf (voorwaardelijke opmaak, samenvoegen, tekststand).",
            waarom=[
                "Let op de tweede rij: je typt 0,25 en ziet 25 procent. De waarde in de cel verandert "
                "niet, enkel hoe ze getoond wordt, en dat komt verder in deze bundel terug.",
            ],
        ),
        dict(
            aanpak="Houd de Nederlandse namen aan wat ze doen. SOM telt op, GEMIDDELDE deelt door het "
                   "aantal, MIN en MAX geven de uitersten, ALS kijkt naar een voorwaarde.",
            waarom=[
                None,
                None,
                "Let op het verschil: ALS kiest tussen twee uitkomsten, VERT.ZOEKEN gaat iets halen "
                "uit een tabel. De eerste beslist, de tweede zoekt op.",
            ],
        ),
        dict(
            aanpak="Eén proef: sleep de formule in je hoofd één rij naar beneden. Schuift het adres "
                   "mee, dan is het relatief; blijft het staan, dan is het absoluut.",
            waarom=[
                "Noem wat er bij kopiëren gebeurt, zoals de opdracht vraagt: A1 schuift mee met de "
                "richting waarin je kopieert.",
                "Let op de dollartekens: zij houden de kolom en de rij vast. Daarom verandert $A$1 "
                "niet als je kopieert.",
                "Let erop dat alle drie de rijen één opschuiven: A1:A3 wordt A2:A4. Het hele bereik "
                "beweegt mee, niet enkel het begin.",
                "Let erop dat ook hier het hele bereik één rij zakt: B1:B4 wordt B2:B5. Dezelfde "
                "regel, andere letters.",
                "Noem beide delen: dat je dollartekens gebruikt en wat er zonder zou gebeuren. Je "
                "zou met een leeg vakje rekenen, en dat is de fout die iedereen één keer maakt.",
            ],
        ),
        dict(
            aanpak="Vraag je af wat je wil laten zien: delen van een geheel, een verloop in de tijd, "
                   "waarden naast elkaar, of een verband tussen twee reeksen.",
            waarom=[
                "Let op het verschil tussen de lijngrafiek en de spreiding: een lijn toont een verloop "
                "in de tijd, een spreiding het verband tussen twee reeksen getallen.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                None,
                "Niet waar: een bereik noteer je met een dubbele punt, zoals A1:A10.",
                None,
                "Niet waar: voorwaardelijke opmaak verandert enkel de kleur of de weergave. De waarde "
                "in de cel blijft dezelfde.",
                "Niet waar: een formule begint altijd met een isgelijkteken. Zonder dat teken ziet "
                "Excel het als gewone tekst.",
                "Niet waar: het gemiddelde en het kleinste getal zijn maar hetzelfde als alle getallen "
                "gelijk zijn. In alle andere gevallen ligt het gemiddelde hoger.",
                "Niet waar: deze fiche noemt het cirkeldiagram, de lijngrafiek, de kolomgrafiek en de "
                "spreiding. Een boxplot staat er niet bij.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-presenteren-met-powerpoint-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Zes namen bij zes dingen. Houd het verschil vast tussen wat tussen twee dia's "
                   "gebeurt en wat op één dia gebeurt: dat is het onderwerp van de volgende reeks.",
            waarom=[
                None,
                None,
                None,
                "Let op het verschil tussen een diaovergang en een animatie: een overgang zit tussen "
                "twee dia's, een animatie op de dia zelf.",
                None,
                "Let erop dat dupliceren een kopie bij zet en het origineel laat staan. Kopiëren en "
                "plakken doet hetzelfde in twee stappen.",
            ],
        ),
        dict(
            aanpak="Eén vraag: gebeurt het effect tussen twee dia's of binnen één dia? Tussen is een "
                   "overgang, binnen is een animatie.",
            waarom=[
                None,
                "Let erop dat tekst die regel per regel verschijnt op de dia zelf gebeurt. Dus een "
                "animatie, ook al wisselt er niets.",
                None,
                "Let erop dat hier twee dia's in het spel zijn: het beeld vervaagt terwijl de "
                "volgende opkomt. Dus een overgang.",
            ],
        ),
        dict(
            aanpak="Houd de twee uit elkaar: een hyperlink zit op tekst of een beeld dat er al staat, "
                   "een actieknop zet je er zelf bij als knop.",
            waarom=[
                None,
                "Noem wat je klaarzet en waarom, zoals het antwoord doet. Zonder zo'n sprong moet je "
                "door alle dia's ertussen klikken.",
            ],
        ),
        dict(
            aanpak="Vraag je bij elke afdruk af voor wie ze is: voor het publiek, voor jezelf als "
                   "spreker, of om je verhaal na te lezen.",
            waarom=[
                "Let op het verschil tussen de hand-out en de notitiepagina: de eerste is voor het "
                "publiek, de tweede met jouw notities is voor jou. Dat verschil komt verderop terug.",
            ],
        ),
        dict(
            aanpak="Houd de letters vast: pptx is om te bewerken, ppsm start meteen de show. De s "
                   "staat voor show, en dat is je steun om het te onthouden.",
            waarom=[
                None,
                None,
                None,
                "Noem waarvoor het dient met een voorbeeld, zoals het antwoord doet. Een presentatie "
                "die op een beurs of in een wachtzaal moet lopen, is het geval.",
            ],
        ),
        dict(
            aanpak="Vijf vragen over de weergaven en over wat een goede dia is. Antwoord in één of "
                   "twee zinnen en noem de naam van de weergave.",
            waarom=[
                "Noem de naam en wat ieder ziet: jij de notities, het publiek enkel de dia.",
                "Noem de naam: de diasorteerder. Dat alle dia's er als miniaturen naast elkaar staan, "
                "is waarom je er makkelijk in sleept.",
                "Noem dat het voor de hele presentatie geldt. Dat is het verschil met één dia apart "
                "opmaken.",
                "Noem beide delen: wat je doet en waarom. Dat een dia geen blad papier is, is de "
                "kern van het antwoord.",
                "Let erop dat de nummering meeschuift: dia 4 wordt dia 3. Daarom moet je een "
                "hyperlink naar een dia na een verwijdering nakijken.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                None,
                "Niet waar: dupliceren zet een kopie bij, verwijderen haalt de dia weg. Precies het "
                "omgekeerde.",
                None,
                "Niet waar: je kan een overgang per dia instellen of voor alle dia's tegelijk. Het "
                "tweede is enkel sneller.",
                None,
                "Niet waar: een hand-out is voor het publiek, een notitiepagina heeft jouw notities "
                "eronder en is voor jou.",
                None,
                "Niet waar: deze fiche noemt de hand-out, de notitiepagina en het overzicht. Etiketten "
                "horen bij een tekstverwerker, niet bij een presentatie.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-veilig-en-correct-online-recht-phishing-en-netiquette-beyond-doorstroom"] = dict(
    reeksen=[
        dict(
            aanpak="Drie rechten, drie eigenaars: wie het maakte (auteursrecht), wie erop staat "
                   "(portretrecht), en wie de gegevens zijn (privacyrecht).",
            waarom=[
                None,
                "Let op herkenbaar: wie niet herkenbaar is, heeft geen portretrecht op dat beeld. Een "
                "rug of een menigte is iets anders dan een gezicht.",
                None,
                "Let erop dat het zeventig jaar na het overlijden van de maker is, niet na het maken "
                "van het werk. Dat onderscheid wordt vaak verwisseld.",
            ],
        ),
        dict(
            aanpak="Eén vraag: maakte jij het, of sta jij erop? Maken geeft auteursrecht, erop staan "
                   "geeft portretrecht. Bij een foto van iemand anders gelden ze samen.",
            waarom=[
                None,
                None,
                "Let erop dat auteursrecht niet enkel over foto's gaat. Een tekst, een lied of een "
                "tekening valt er ook onder.",
            ],
        ),
        dict(
            aanpak="Leer de drie voorwaarden en hun afkorting. Een creative commons licentie geeft "
                   "toelating vooraf, maar nooit zonder voorwaarden.",
            waarom=[
                None,
                None,
                "Noem beide delen: wat het is en waarom je niets meer moet vragen. En noem de grens: "
                "je moet je wel aan de voorwaarden houden.",
                "Let erop dat naamsvermelding betekent: de naam bij de foto, waar je ze gebruikt. "
                "Ergens achteraan in een bronnenlijst is minder dan wat gevraagd wordt.",
            ],
        ),
        dict(
            aanpak="Vier gevallen uit het echte leven. Vraag je telkens af wie welk recht heeft, en "
                   "antwoord in twee of drie zinnen.",
            waarom=[
                "Let op de valkuil: geen vermelding betekent niet vrij te gebruiken. Het auteursrecht "
                "geldt ook zonder dat er iets bij staat.",
                "Noem beide rechten: jij hebt het auteursrecht, zij het portretrecht. Juist omdat ze "
                "samenkomen, heb je haar toelating nodig.",
                "Noem beide stappen: eerst zelf vragen om de foto weg te halen, en melden bij het "
                "platform als dat niet werkt.",
                "Noem het begrip: er worden meer gegevens gevraagd dan voor dat doel nodig zijn. Voor "
                "een nieuwsbrief volstaat een mailadres.",
            ],
        ),
        dict(
            aanpak="Houd twee rijtjes van drie vast: wat een sterk wachtwoord maakt, en wat een "
                   "phishingbericht verraadt.",
            waarom=[
                None,
                None,
                "Let erop dat haast een van de drie is. Een bericht dat zegt dat je vandaag nog moet "
                "reageren, is net daarom verdacht.",
                "Noem beide delen: niet klikken en zelf naar de site of de app gaan. En noem de regel: "
                "een bank vraagt je nooit om via een link je codes te bevestigen.",
                "Noem het gevolg: wie je wachtwoord op één site vindt, probeert het elders. Daarom is "
                "hergebruik het grootste risico.",
            ],
        ),
        dict(
            aanpak="Vijf open vragen over nepnieuws en cyberpesten. Antwoord in twee of drie zinnen en "
                   "noem telkens wat je concreet doet.",
            waarom=[
                "Noem het onderscheid: de opzet. Een vergissing wordt rechtgezet, nepnieuws is "
                "bedoeld om te misleiden.",
                "Noem wat je nakijkt en wat niets bewijst: hoeveel keer iets gedeeld is, zegt niets "
                "over de waarheid.",
                "Noem de methode: de foto omgekeerd opzoeken. Dat oude foto's bij nieuwe "
                "gebeurtenissen opduiken, is het meest voorkomende geval.",
                "Noem alle drie: bewijs bewaren, melden en de persoon niet alleen laten. En noem dat "
                "niet meedoen nodig is maar niet genoeg.",
                "Let erop dat een foto krijgen geen toelating is om ze door te sturen. Portretrecht en "
                "privacy gaan precies daarover.",
            ],
        ),
        dict(
            aanpak="Lees elke uitspraak tegen de fiche. Bij een onjuiste schrijf je in één regel wat "
                   "er wel klopt, zoals het examen het vraagt.",
            waarom=[
                "Niet waar: het auteursrecht geldt vanaf het moment dat je het werk maakt. Je hoeft "
                "het niet aan te vragen of te registreren.",
                "Niet waar: creative commons werkt net met voorwaarden, zoals naamsvermelding of geen "
                "commercieel gebruik. Lees dus welke licentie erop staat.",
                None,
                "Niet waar: je mag inzage vragen in de gegevens die een bedrijf over jou bijhoudt. Dat "
                "is een deel van het privacyrecht.",
                "Niet waar: phishing is vaak keurig verzorgd, met logo en al. Juist daarom kijk je naar "
                "de afzender en de link, niet naar de vormgeving.",
                None,
                None,
                "Niet waar: volledig in hoofdletters schrijven leest als roepen. Netiquette vraagt net "
                "het omgekeerde.",
            ],
        ),
    ],
)
