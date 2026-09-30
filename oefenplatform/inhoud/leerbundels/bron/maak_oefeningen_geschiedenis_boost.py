# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij geschiedenis 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen. Dezelfde pdf gaat dus bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere gevallen om in te delen, andere bronnen om te beoordelen, en
opdrachten die je enkel op papier kan maken (een tabel aanvullen, een tijdlijn
invullen, een oordeel verantwoorden). Wie hier iets bijschrijft, legt het eerst
naast `../../boost-doorstroom/geschiedenis.json`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost". Het voorvoegsel is nodig omdat leerbundels en oefenbundels in
dezelfde bronmap gerenderd worden en anders dezelfde bestandsnaam zouden
krijgen. Het achtervoegsel houdt ze uit elkaar van een latere Boost dubbele
finaliteit.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel

VAK = "Geschiedenis"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "120px"
WW = "185px"
WL = "250px"

OEFENBUNDELS = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een jaartal: zet er altijd bij of het voor of na Christus is als dat kan verwarren.",
    "Bij een oordeel: zeg niet alleen wát je vindt, maar ook waaróm, met een begrip uit de leerstof.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

# ============================================================
OEFENBUNDELS["oefenbundel-het-historisch-referentiekader-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Het historisch referentiekader",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="In welke periode?",
             opdracht="Schrijf bij elke gebeurtenis de naam van de periode waarin ze thuishoort.",
             oefeningen=[
                 ("rij", [("de bouw van de piramide van Cheops", "het oude nabije oosten"),
                          ("de eerste rotstekeningen", "de prehistorie"),
                          ("de regering van keizer Augustus", "de klassieke oudheid"),
                          ("de bouw van de kathedraal van Chartres", "de middeleeuwen")],
                  "Welke periode?", WL),
                 ("rij", [("de Vrede van Münster in 1648", "de vroegmoderne tijd"),
                          ("de aanleg van de eerste spoorlijn in België", "de moderne tijd"),
                          ("de val van de Berlijnse Muur", "de hedendaagse tijd")],
                  "Welke periode?", WL),
             ]),
        dict(kop="Chronologie of periodisering?",
             opdracht="Duid bij elke opdracht aan wat je aan het doen bent.",
             oefeningen=[
                 ("kies", "Je zet vijf uitvindingen in de juiste volgorde op een tijdlijn.",
                  ["chronologie", "periodisering"], 0),
                 ("kies", "Je noemt alles tussen 1492 en 1789 de vroegmoderne tijd.",
                  ["chronologie", "periodisering"], 1),
                 ("kies", "Je zoekt uit wat er eerst kwam: de boekdrukkunst of de val van Constantinopel.",
                  ["chronologie", "periodisering"], 0),
                 ("kies", "Je geeft de eeuwen van de Egyptische geschiedenis namen van dynastieën.",
                  ["chronologie", "periodisering"], 1),
             ]),
        dict(kop="Rekenen met jaartallen",
             opdracht="Reken uit. Let op: er zit geen jaar nul tussen 1 v.C. en 1 n.C.",
             oefeningen=[
                 ("rij", [("Hoeveel jaar later is 1789 dan 1453?", "336 jaar"),
                          ("Hoeveel jaar later is 800 dan 476?", "324 jaar"),
                          ("In welke eeuw ligt het jaar 1302?", "de 14de eeuw"),
                          ("In welke eeuw ligt het jaar 1600?", "de 16de eeuw")],
                  "Antwoord", WW),
                 ("open", "Een tekst zegt: 'Deze tempel werd gebouwd in 400 v.C. en verwoest in 200 v.C.' "
                          "Hoe lang heeft hij gestaan? Leg uit waarom je hier niet gewoon mag optellen.",
                  "200 jaar. Jaartallen voor Christus tellen achterwaarts: 400 v.C. ligt vroeger dan "
                          "200 v.C. Je trekt dus af: 400 min 200 is 200 jaar.", 5),
             ]),
        dict(kop="Welk structuurbegrip?",
             opdracht="Schrijf bij elke zin welk structuurbegrip van de tijd erbij past: "
                      "continuïteit, verandering, gelijktijdigheid, ongelijktijdigheid, evolutie of revolutie.",
             oefeningen=[
                 ("rij", [("In 1500 ploegt een boer bijna zoals in 1300.", "continuïteit"),
                          ("In hetzelfde jaar bloeit Peking en brandt Londen.", "gelijktijdigheid"),
                          ("De stoommachine verandert het werk van iedereen.", "revolutie"),
                          ("Het Nederlands van nu is over eeuwen stilaan gegroeid.", "evolutie")],
                  "Welk begrip?", WW),
                 ("rij", [("Boekdrukkunst in Korea eeuwen vóór die in Europa.", "ongelijktijdigheid"),
                          ("Na 1500 kent West-Europa plots zilver uit Amerika.", "verandering")],
                  "Welk begrip?", WW),
             ]),
        dict(kop="In welk maatschappelijk domein?",
             opdracht="Vul de tabel aan. Meerdere domeinen mag, maar schrijf er dan bij waarom.",
             oefeningen=[
                 ("tabel", ["gegeven", "welk domein of welke domeinen", "waarom"],
                  [["de invoering van een nieuwe munt", None, None],
                   ["de bouw van een kathedraal", None, None],
                   ["het afschaffen van de adellijke voorrechten", None, None],
                   ["een hongersnood die boeren naar de stad drijft", None, None],
                   ["de kroning van een koning door een bisschop", None, None]],
                  "een nieuwe munt: economisch (betalen) en politiek (de vorst beslist het). "
                  "een kathedraal: cultureel (geloof en kunst), ook economisch (ze kost veel). "
                  "de adellijke voorrechten afschaffen: politiek en sociaal. "
                  "een hongersnood die boeren naar de stad drijft: economisch en sociaal. "
                  "de kroning door een bisschop: politiek en cultureel.",
                  "230px"),
             ]),
        dict(kop="Ruimte",
             opdracht="Schrijf bij elke zin op welk schaalniveau er gekeken wordt: lokaal, regionaal, "
                      "nationaal, continentaal of mondiaal.",
             oefeningen=[
                 ("rij", [("de ambachten van de stad Ieper", "lokaal"),
                          ("het graafschap Vlaanderen", "regionaal"),
                          ("de handel tussen alle werelddelen na 1500", "mondiaal"),
                          ("de Dertigjarige Oorlog in Europa", "continentaal")],
                  "Welk niveau?", WW),
                 ("waar", "Ruraal betekent: in de stad.", False),
                 ("waar", "Een historische kaart toont de grenzen zoals ze in die tijd lagen.", True),
             ]),
        dict(kop="Zelf een periodegrens verdedigen",
             opdracht="",
             oefeningen=[
                 ("open", "Sommige historici laten de vroegmoderne tijd in 1453 beginnen, anderen in 1492. "
                          "Kies er één en verdedig die keuze met twee argumenten.",
                  "1453 (de val van Constantinopel): het laatste stuk van het Romeinse Rijk verdwijnt, en "
                          "geleerden vluchten met hun boeken naar Italië. 1492 (Columbus): de contacten "
                          "tussen de continenten veranderen blijvend, en de handel verlegt zich naar de "
                          "oceanen. Allebei zijn verdedigbaar, want een periodegrens is een keuze.", 7),
                 ("open", "Noem twee beperkingen van periodisering en geef bij elke beperking een voorbeeld.",
                  "Ze steunt op een selectie: wat je niet kiest, valt weg, bijvoorbeeld het leven van "
                          "gewone vrouwen. Ze suggereert een scherpe breuk: in 1493 leefde een boer precies "
                          "zoals in 1491. En ze past niet even goed op niet-westerse samenlevingen: de "
                          "Chinese geschiedenis wordt in dynastieën ingedeeld.", 7),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-van-rome-naar-de-franken-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Van Rome naar de Franken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Intern of extern?",
             opdracht="Duid bij elke oorzaak aan of ze van binnen of van buiten kwam.",
             oefeningen=[
                 ("kies", "Het Romeinse leger bestond steeds meer uit ingehuurde Germanen.",
                  ["interne oorzaak van de val van Rome", "externe oorzaak"], 0),
                 ("kies", "De Hunnen dreven andere volkeren voor zich uit.",
                  ["interne oorzaak van de val van Rome", "externe oorzaak"], 1),
                 ("kies", "De Germaanse bevolking groeide en er was te weinig landbouwgrond.",
                  ["interne oorzaak van de migraties", "externe oorzaak van de migraties"], 0),
                 ("kies", "De rijkdom en het klimaat van het Romeinse rijk trokken aan.",
                  ["interne oorzaak van de migraties", "externe oorzaak van de migraties"], 1),
             ]),
        dict(kop="Tijdlijn",
             opdracht="Zet deze gebeurtenissen in de juiste volgorde, van 1 tot 6.",
             oefeningen=[
                 ("tabel", ["gebeurtenis", "jaartal", "volgorde"],
                  [["de keizerskroning van Karel de Grote", None, None],
                   ["de doop van Clovis", None, None],
                   ["het Verdrag van Verdun", None, None],
                   ["de afzetting van de laatste West-Romeinse keizer", None, None],
                   ["de zalving van Pepijn de Korte", None, None],
                   ["de eerste invallen van de Noormannen", None, None]],
                  "476 afzetting laatste keizer (1), rond 500 doop van Clovis (2), 751 zalving van "
                  "Pepijn (3), 800 keizerskroning (4), 843 Verdun (5), 9de eeuw Noormannen (6).",
                  "200px"),
             ]),
        dict(kop="Wie of wat is het?",
             opdracht="Schrijf het juiste woord of de juiste naam.",
             oefeningen=[
                 ("rij", [("de hoogste ambtenaar aan het Merovingische hof", "de hofmeier"),
                          ("een bestuurlijk gebied onder een graaf", "een gouw"),
                          ("de rondreizende controleurs van Karel de Grote", "de missi dominici"),
                          ("de hoofdplaats van Karel de Grote", "Aken")],
                  "Antwoord", WW),
                 ("rij", [("de eerste Frankische dynastie", "de Merovingers"),
                          ("de spotnaam voor de laatste Merovingers", "de vadsige koningen"),
                          ("de rivier waarlangs de Franken oorspronkelijk woonden", "de Rijn")],
                  "Antwoord", WW),
             ]),
        dict(kop="Waar of niet waar?",
             opdracht="",
             oefeningen=[
                 ("waar", "Het Oost-Romeinse Rijk bleef na 476 nog bijna duizend jaar bestaan.", True),
                 ("waar", "Bij de Franken erfde de oudste zoon altijd het hele rijk.", False),
                 ("waar", "De Karolingische renaissance bereikte de gewone boeren nauwelijks.", True),
                 ("waar", "De Mongolen vielen in de 9de eeuw het Frankische rijk binnen.", False),
                 ("waar", "De invallen van de 9de en de 10de eeuw verzwakten het centrale gezag.", True),
             ]),
        dict(kop="Oorzaak en gevolg",
             opdracht="Verbind in je hoofd en schrijf het gevolg op.",
             oefeningen=[
                 ("kort", "Het Frankische erfrecht verdeelt het rijk onder de zonen. Gevolg voor de "
                          "koninklijke macht?", "het rijk valt telkens opnieuw uiteen in kleinere delen",
                  "320px"),
                 ("kort", "De Noormannen, Saracenen en Hongaren vallen binnen. Gevolg voor de gewone mensen?",
                  "ze zoeken bescherming bij de lokale heer, want die kan meteen helpen", "320px"),
                 ("kort", "Clovis laat zich dopen. Gevolg voor zijn macht?",
                  "hij wint de steun van de Gallo-Romeinse bevolking en van de bisschoppen", "320px"),
             ]),
        dict(kop="Een bron lezen",
             opdracht="Lees en beantwoord.",
             oefeningen=[
                 ("tekst", "<em>Uit een kroniek, geschreven door een monnik in de 9de eeuw:</em> "
                           "“De keizer beminde de vreemdelingen zozeer dat hun aanwezigheid het paleis "
                           "en het rijk terecht tot last werd. Maar hij achtte dat van weinig belang, want "
                           "hij hield zijn goede naam voor belangrijker.”"),
                 ("open", "Over wie gaat deze bron waarschijnlijk, en waaraan zie je dat?",
                  "Over Karel de Grote. Een monnik die in de 9de eeuw over 'de keizer' en zijn paleis "
                          "schrijft, bedoelt hem: hij was de keizer van het Frankische rijk vanaf 800.", 4),
                 ("open", "Is deze monnik een neutrale getuige? Verantwoord je antwoord met één zin uit "
                          "de tekst.",
                  "Nee. 'Hij achtte dat van weinig belang' en 'zijn goede naam' zijn oordelen, geen "
                          "vaststellingen. De monnik prijst de keizer; hij schreef wellicht voor het hof "
                          "of voor een klooster dat van de keizer afhing.", 5),
                 ("open", "In welke twee maatschappelijke domeinen situeer je de zalving van een koning "
                          "door de paus? Leg allebei uit.",
                  "Politiek: het gaat over wie er mag heersen, en de kerkelijke bevestiging maakt de "
                          "macht sterker. Cultureel: het is een godsdienstige plechtigheid met een eigen "
                          "betekenis en eigen gebruiken.", 5),
             ]),
        dict(kop="Vergelijken",
             opdracht="",
             oefeningen=[
                 ("open", "Vergelijk de koninklijke macht onder de Merovingers en onder de Karolingers. "
                          "Noem één gelijkenis en één verschil.",
                  "Gelijkenis: allebei kenden ze het erfrecht dat het rijk onder de zonen verdeelde, dus "
                          "allebei verbrokkelden ze uiteindelijk. Verschil: onder de Karolingers werd de "
                          "macht eerst veel sterker, met graven, missi dominici en opgeschreven wetten, "
                          "terwijl de laatste Merovingers nauwelijks nog iets te zeggen hadden.", 7),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-standen-domein-en-stad-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Standen, domein en stad",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De drie standen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["stand", "taak volgens de standenleer", "wie hoorde erbij"],
                  [["de geestelijkheid", None, None],
                   ["de adel", None, None],
                   ["de derde stand", None, None]],
                  "geestelijkheid: bidden, voor het zielenheil van allen; priesters, monniken, "
                  "bisschoppen. adel: strijden, met het zwaard beschermen; ridders, heren, de koning. "
                  "derde stand: werken en de twee andere onderhouden; boeren, ambachtslui, kooplui.",
                  "230px"),
                 ("open", "Waarom noemt men de standensamenleving een samenleving zonder sociale "
                          "mobiliteit? Gebruik het woord geboorte in je antwoord.",
                  "Omdat niet je verdienste maar je geboorte je plaats bepaalde. In welke stand je "
                          "geboren werd, bepaalde bijna helemaal welk leven je kreeg; opklimmen kon "
                          "nauwelijks.", 5),
             ]),
        dict(kop="Het domein",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Een horige mocht het domein verlaten wanneer hij wou.", False),
                 ("waar", "Een horige kon net als een slaaf verkocht worden.", False),
                 ("waar", "Herendiensten waren onbetaalde werkdagen op het vroonland van de heer.", True),
                 ("waar", "Het domein moest bijna alles wat het nodig had zelf voortbrengen.", True),
                 ("waar", "Voor het malen van graan moest men naar de molen van de heer.", True),
             ]),
        dict(kop="Vernieuwingen in de landbouw",
             opdracht="Schrijf bij elke omschrijving de naam van de vernieuwing.",
             oefeningen=[
                 ("rij", [("de akker in drie delen, waarvan er één rust", "het drieslagstelsel"),
                          ("keert de aarde om in plaats van ze open te krabben", "de keerploeg"),
                          ("laat een paard met zijn schouders trekken", "het haam")],
                  "Welke vernieuwing?", WW),
                 ("open", "Leg uit hoe meer voedsel uiteindelijk tot meer steden leidde. Zet de stappen "
                          "in de juiste volgorde op.",
                  "Meer voedsel per akker, dus een overschot. Een overschot kan verkocht worden, dus "
                          "ontstaat er een markt. De bevolking groeit, en niet iedereen moet nog op het "
                          "land werken. Wie vrijkomt, gaat een ambacht of handel doen, en dat gebeurt op "
                          "de plaats van de markt: de stad.", 7),
             ]),
        dict(kop="De heropbloei van de steden",
             opdracht="Noem de drie factoren en beantwoord.",
             oefeningen=[
                 ("open", "Vanaf de 11de eeuw bloeien de steden weer op. Noem de drie factoren die "
                          "daartoe bijdroegen.",
                  "Een groeiende bevolking door betere landbouw, meer veiligheid waardoor handel over "
                          "langere afstand kon, en de ligging aan een rivier, een weg of een kruispunt.", 5),
                 ("open", "Waarom ontstonden veel steden juist aan een rivier?",
                  "Omdat water de goedkoopste manier was om zware vracht te vervoeren. Een schip draagt "
                          "veel meer dan een kar, en het hoeft geen slechte wegen te trotseren.", 4),
                 ("kort", "Hoe noem je het document waarin een vorst de rechten van een stad vastlegde?",
                  "een keure", "200px"),
                 ("kort", "Hoe noem je de vereniging van ambachtslui van hetzelfde beroep?",
                  "het ambacht (of de gilde)", "200px"),
                 ("open", "Hoe werd je meester in een ambacht? Zet de weg in stappen op.",
                  "Eerst jaren als leerjongen, daarna als gezel, dan een meesterproef maken, en geld "
                          "hebben voor een eigen werkplaats. Zonen van meesters kwamen er veel makkelijker "
                          "in.", 5),
             ]),
        dict(kop="Ongelijkheid in de stad",
             opdracht="",
             oefeningen=[
                 ("kies", "De rijke kooplieden die het stadsbestuur in handen hadden, heten:",
                  ["de patriciërs", "de horigen", "de poorters"], 0),
                 ("kies", "De toren waarin de stad haar klok en haar oorkonden bewaarde, heet:",
                  ["het belfort", "de lakenhalle", "de kathedraal"], 0),
                 ("open", "“Binnen de stadsmuren waren alle inwoners gelijk.” Klopt dat? "
                          "Verantwoord met twee argumenten.",
                  "Nee. De stadslucht maakte wel vrij van horigheid, maar in de stad zelf bestond er "
                          "grote ongelijkheid: alleen de patriciërs bestuurden, de ambachten hadden lang "
                          "niets te zeggen, en er waren arme loonwerkers en bedelaars. Dat leidde tot "
                          "opstanden van de ambachten tegen de patriciërs.", 7),
             ]),
        dict(kop="De pest",
             opdracht="Vul in.",
             oefeningen=[
                 ("kort", "In welke eeuw trof de pest West-Europa het zwaarst?",
                  "de 14de eeuw (vanaf 1347)", "220px"),
                 ("open", "De pest doodde een groot deel van de bevolking. Waarom stegen de lonen "
                          "daarna? Leg uit met vraag en aanbod.",
                  "Er waren veel minder werkkrachten over, terwijl het werk bleef. Wie nog kon werken, "
                          "was dus schaars en kon meer vragen. Sommige heren moesten herendiensten "
                          "omzetten in loon om nog volk te vinden.", 6),
             ]),
        dict(kop="Domeinen en verbanden",
             opdracht="",
             oefeningen=[
                 ("open", "In welk maatschappelijk domein hoort het ontstaan van de geldeconomie in de "
                          "eerste plaats thuis, en welk ander domein raakt ze ook? Leg uit.",
                  "In de eerste plaats economisch: betalen in geld in plaats van in natura. Ze raakt ook "
                          "het sociale domein, want wie geld heeft, kan zijn plaats kopen, en dat gaat in "
                          "tegen de standenleer.", 6),
                 ("waar", "Stad en platteland stonden in de middeleeuwen volledig los van elkaar.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-geloof-kunst-en-macht-in-de-middeleeuwen-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Geloof, kunst en macht in de middeleeuwen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De Kerk van binnenuit",
             opdracht="Vul de piramide aan en beantwoord.",
             oefeningen=[
                 ("tabel", ["trede van de piramide", "wie staat daar", "wat doet die"],
                  [["bovenaan", None, None],
                   ["in het midden", None, None],
                   ["onderaan, in de parochie", None, None]],
                  "bovenaan de paus, hoofd van de hele Kerk. in het midden de bisschoppen, elk over een "
                  "bisdom. onderaan de pastoors, in de parochie bij de mensen zelf.",
                  "230px"),
                 ("open", "Noem de drie taken die de kloosters naast het gebed op zich namen.",
                  "Ze kopieerden en bewaarden oude teksten, ze ontgonnen woeste grond tot landbouwgrond, "
                          "en ze zorgden voor zieken en reizigers. Munten slaan deden ze niet; dat was een "
                          "recht van de vorst.", 5),
                 ("open", "Leg uit waarom missionarissen eerst de vorst bekeerden en pas daarna zijn volk.",
                  "Omdat met de vorst zijn hofhouding meeging en daarna zijn onderdanen. Eén bekering "
                          "bovenaan haalde er zo heel veel onderaan binnen. Daarom is de doop van Clovis "
                          "zo'n keerpunt.", 5),
             ]),
        dict(kop="Romaans of gotisch?",
             opdracht="Duid bij elk kenmerk de stijl aan.",
             oefeningen=[
                 ("kies", "rondbogen en dikke muren met kleine vensters", ["romaans", "gotisch"], 0),
                 ("kies", "spitsbogen en grote glasramen", ["romaans", "gotisch"], 1),
                 ("kies", "luchtbogen die het gewicht naar buiten afleiden", ["romaans", "gotisch"], 1),
                 ("kies", "een zware, gesloten en donkere indruk", ["romaans", "gotisch"], 0),
                 ("open", "Leg uit waarom de gotiek grotere vensters kon maken dan de romaanse bouwkunst. "
                          "Noem de techniek erbij.",
                  "Bij de gotiek dragen de spitsboog, het kruisribgewelf en de luchtbogen het gewicht "
                          "naar bepaalde punten en naar buiten. De muur zelf hoeft dan niet meer alles te "
                          "dragen, dus kan er glas in. Het verschil zit dus in de bouwtechniek, niet "
                          "alleen in de versiering.", 6),
             ]),
        dict(kop="Kunst als verhaal in beeld",
             opdracht="",
             oefeningen=[
                 ("open", "Waarom stonden er verhalen in beeld op de muren en de ramen van een kerk?",
                  "Omdat bijna niemand kon lezen. De beelden, de ramen en de schilderingen vertelden de "
                          "verhalen die de gelovigen moesten kennen. Ze waren de boeken van wie niet las.", 5),
                 ("kort", "Hoe noemt men Jan van Eyck en zijn tijdgenoten?",
                  "de Vlaamse primitieven", "230px"),
                 ("open", "Een middeleeuws schilderij toont de opdrachtgever even groot als de heiligen. "
                          "Wat zegt dat over hoe zo'n schilderij gelezen moet worden?",
                  "Dat de grootte in de middeleeuwse kunst de belangrijkheid aangeeft en niet de "
                          "afstand. Wie groot is afgebeeld, telt zwaar. Zo'n schilderij is dus geen foto "
                          "van de werkelijkheid maar een boodschap over rangorde.", 6),
             ]),
        dict(kop="Frankrijk en Engeland",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "In Engeland moest de koning zijn macht delen met een parlement.", True),
                 ("waar", "De Franse koning breidde zijn macht uit ten koste van zijn leenmannen.", True),
                 ("waar", "De Magna Carta gaf de Engelse koning meer macht dan hij ervoor had.", False),
             ]),
        dict(kop="De Guldensporenslag",
             opdracht="",
             oefeningen=[
                 ("kort", "In welk jaar vond de Guldensporenslag plaats?", "1302", "150px"),
                 ("open", "Leg uit waarom de Guldensporenslag tegelijk in het politieke en in het sociale "
                          "domein thuishoort.",
                  "Politiek: het ging om de macht over Vlaanderen, tussen de Franse koning en de graaf "
                          "met de steden. Sociaal: het ging ook om de verhouding tussen bevolkingsgroepen "
                          "in de steden, tussen de ambachten en de patriciërs die de Franse kant kozen.", 6),
                 ("open", "De slag werd in de 19de eeuw veel belangrijker gemaakt dan hij toen was. "
                          "Hoe noem je dat verschijnsel?",
                  "Beeldvorming: de betekenis die men later aan een gebeurtenis geeft. In de 19de eeuw "
                          "had men een Vlaams verhaal nodig, en de slag werd daarvoor gebruikt.", 4),
             ]),
        dict(kop="Het Arabische Rijk en de kruistochten",
             opdracht="",
             oefeningen=[
                 ("kort", "Vanaf ongeveer welk jaar ontstaat de islam?", "rond 600", "180px"),
                 ("waar", "De islam verspreidde zich binnen de tien jaar over heel zijn latere gebied.", False),
                 ("waar", "Langs de Arabische wereld bereikten Griekse teksten opnieuw West-Europa.", True),
                 ("open", "Noem twee dingen die West-Europa aan het contact met de Arabische wereld "
                          "dankte, en één ding dat er níét vandaan kwam.",
                  "Wel: Griekse teksten die via Arabische vertalingen terugkwamen, de cijfers waarmee wij "
                          "nog altijd rekenen, en vooruitgang in geneeskunde, sterrenkunde en wiskunde. "
                          "Niet: de boekdrukkunst met losse letters, die komt van Gutenberg in de "
                          "15de eeuw.", 6),
                 ("waar", "De kruistochten leverden op lange termijn een blijvend christelijk rijk in het "
                          "Midden-Oosten op.", False),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-de-nieuwe-wereld-en-de-driehoekshandel-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="De 'Nieuwe' Wereld en de driehoekshandel",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Goud, God of glorie?",
             opdracht="Schrijf bij elk motief of het economisch, godsdienstig of politiek is.",
             oefeningen=[
                 ("rij", [("een eigen weg naar de specerijen van Azië", "economisch"),
                          ("het christendom verspreiden", "godsdienstig"),
                          ("aanzien en gebied voor de eigen vorst", "politiek"),
                          ("de tussenhandelaars uitschakelen die de prijs bepalen", "economisch")],
                  "Welk motief?", WW),
                 ("open", "Waarom waren specerijen in Lissabon peperduur vóór de zeeweg gevonden was?",
                  "Omdat de landroute door gebieden liep waar tussenhandelaars de prijs bepaalden. Wat "
                          "via vele handen komt, wordt bij elke hand duurder.", 4),
             ]),
        dict(kop="Techniek aan boord",
             opdracht="Schrijf bij elk instrument waarvoor het diende. Eén ervan bestond nog niet.",
             oefeningen=[
                 ("rij", [("het kompas", "de richting bepalen"),
                          ("het astrolabium en de jakobsstaf", "op open zee de breedtegraad bepalen"),
                          ("de scheepsmotor", "bestond nog niet")],
                  "Waarvoor?", WL),
             ]),
        dict(kop="Wie deed wat?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["naam", "wat hij deed", "jaartal"],
                  [["Christoffel Columbus", None, None],
                   ["Vasco da Gama", None, None],
                   ["Magellaan", None, None],
                   ["Cortés", None, None]],
                  "Columbus: vaart in dienst van Spanje de Atlantische Oceaan over en bereikt eilanden "
                  "in de Caraïben, 1492. Da Gama: als eerste rond Kaap de Goede Hoop tot in Calicut, "
                  "1498. Magellaan: zijn vloot vaart als eerste rond de wereld. Cortés: geen "
                  "ontdekkingsreiziger maar veroveraar.",
                  "260px"),
                 ("open", "Leg het verschil uit tussen wat Portugal en wat Spanje in de eerste "
                          "kolonisatiegolf deed.",
                  "Portugal bouwde vooral een net van handelsposten langs de kusten: het wilde de handel "
                          "beheersen. Spanje veroverde grote gebieden in het binnenland: het wilde het "
                          "land zelf.", 5),
             ]),
        dict(kop="De gevolgen voor de precolumbiaanse bevolking",
             opdracht="",
             oefeningen=[
                 ("kies", "De belangrijkste oorzaak van de demografische inzinking was:",
                  ["ziekten waartegen zij geen weerstand hadden", "de oorlogen",
                   "het vertrek naar andere streken"], 0),
                 ("kort", "Welk rijk in de Andes vernietigden de Spanjaarden?", "het Incarijk", "200px"),
                 ("kort", "Hoe heet het systeem waarbij een kolonist arbeid mocht opeisen van de "
                          "inheemse bevolking?", "het encomiendasysteem", "230px"),
                 ("open", "Leg uit hoe de demografische inzinking, het encomiendasysteem en de "
                          "Afrikaanse slavenhandel samenhangen. Schrijf het als een ketting.",
                  "De inheemse bevolking sterft grotendeels weg. Daardoor valt de gedwongen arbeid van "
                          "het encomiendasysteem weg, terwijl de mijnen en de velden blijven. Die arbeid "
                          "wordt dan van elders gehaald, uit Afrika.", 6),
             ]),
        dict(kop="De driehoekshandel",
             opdracht="Vul in wat er op elk been vervoerd werd.",
             oefeningen=[
                 ("tabel", ["been", "lading"],
                  [["Europa naar West-Afrika", None],
                   ["West-Afrika naar Amerika", None],
                   ["Amerika naar Europa", None]],
                  "Europa naar Afrika: wapens, textiel en alcohol. Afrika naar Amerika: tot slaaf "
                  "gemaakte mensen. Amerika naar Europa: suiker, katoen en tabak.",
                  "320px"),
                 ("kort", "Hoe heet de oversteek van Afrika naar Amerika?", "de middenpassage", "220px"),
                 ("open", "“De driehoekshandel is enkel economie.” Weerleg die uitspraak.",
                  "Ze toont juist hoe het economische en het sociale domein in elkaar grijpen: wat op "
                          "papier een handelsstroom is, gaat over mensen die tot koopwaar gemaakt werden.", 5),
             ]),
        dict(kop="De commerciële revolutie",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("meer uitvoeren dan invoeren, om edelmetaal binnen te halen", "het mercantilisme"),
                          ("een handelaar levert grondstof aan gezinnen die thuis werken", "huisnijverheid"),
                          ("arbeiders werken samen op één plaats, onder toezicht", "een manufactuur"),
                          ("het kapitaal is in verhandelbare delen verdeeld", "een handelscompagnie")],
                  "Welk begrip?", WL),
                 ("open", "Noem drie kenmerken van het handelskapitalisme.",
                  "Winst wordt opnieuw geïnvesteerd om meer winst te maken, kapitaal wordt door "
                          "meerdere mensen samengelegd, en het risico van een reis wordt gespreid over "
                          "vele aandeelhouders.", 5),
                 ("open", "Waarom noem je de commerciële revolutie een breuk en geen continuïteit, "
                          "terwijl handel en geld al eeuwen bestonden?",
                  "Omdat het economische systeem zélf verandert en niet alleen de hoeveelheid handel. "
                          "Nieuw is dat winst systematisch opnieuw geïnvesteerd wordt, en dat wie "
                          "handelt en investeert belangrijker wordt dan wie grond bezit.", 6),
                 ("waar", "Het mercantilisme wil vrije handel met alle landen.", False),
             ]),
        dict(kop="Sporen tot vandaag",
             opdracht="",
             oefeningen=[
                 ("open", "Waaraan zie je vandaag nog welk land welk gebied koloniseerde? Geef een "
                          "voorbeeld uit Zuid-Amerika.",
                  "Aan de taal die er gesproken wordt en aan de plaatsnamen, en ook aan de godsdienst en "
                          "het rechtssysteem. Brazilië spreekt Portugees, de rest van Zuid-Amerika "
                          "Spaans.", 5),
                 ("open", "Leg uit waarom men 'Nieuwe' Wereld met aanhalingstekens schrijft.",
                  "Omdat die wereld enkel nieuw was voor de Europeanen die er aankwamen. Er woonden al "
                          "miljoenen mensen met eigen rijken en steden.", 4),
                 ("kort", "Hoe noem je het beplanten van een heel gebied met één gewas voor de uitvoer?",
                  "monocultuur", "200px"),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-humanisme-reformatie-renaissance-en-barok-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Humanisme, Reformatie, renaissance en barok",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Het humanisme",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie kenmerken van het humanisme.",
                  "Belangstelling voor de mens en zijn mogelijkheden, teruggrijpen naar de Griekse en "
                          "Romeinse oudheid, en kritisch onderzoek van de oorspronkelijke teksten.", 5),
                 ("waar", "De meeste humanisten wilden de Kerk afschaffen.", False),
                 ("kort", "Welk boek van Erasmus bespotte de misbruiken in Kerk en samenleving?",
                  "Lof der Zotheid", "220px"),
                 ("open", "Waarom ontstond het humanisme juist in de rijke Italiaanse steden?",
                  "Florence, Venetië en Rome hadden het geld, de handelscontacten en de Romeinse resten "
                          "om op verder te bouwen.", 4),
                 ("open", "Welke uitvinding hielp de humanisten, en waarom precies?",
                  "De boekdrukkunst. Wat vroeger één monnik in maanden overschreef, rolde nu bij "
                          "honderden van de pers, dus verspreidden hun ideeën zich veel sneller.", 4),
             ]),
        dict(kop="Een nieuwe wetenschappelijke methode",
             opdracht="",
             oefeningen=[
                 ("kies", "Wat verandert er aan de wetenschappelijke methode?",
                  ["men gaat zelf waarnemen en proeven doen",
                   "men gelooft de oude teksten nog strikter",
                   "men stopt met het lezen van Griekse teksten"], 0),
                 ("open", "Wat deed Vesalius, en waarom is dat zo belangrijk?",
                  "Hij ontleedde zelf lichamen en toonde aan dat de oude Griekse teksten, zoals die van "
                          "Galenus, niet in alles gelijk hadden. Het echte nieuwe is dat je dat mág "
                          "vaststellen: de waarneming weegt zwaarder dan het gezag van een oud boek.", 6),
                 ("waar", "De microscoop kwam uit de Arabische wereld.", False),
             ]),
        dict(kop="De Reformatie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("kort", "Wat is een aflaat?",
                  "een kwijtschelding van straf voor zonden, die men ook kon kopen", "330px"),
                 ("kort", "In welk jaar en in welke stad hing Luther zijn stellingen op?",
                  "in 1517, in Wittenberg", "260px"),
                 ("kort", "Hoeveel stellingen waren het?", "vijfennegentig", "200px"),
                 ("open", "Leg uit wat Luther bedoelde met sola fide en sola scriptura, en waarom dat "
                          "de rol van de priesters op de helling zette.",
                  "Sola fide: een mens wordt gered door het geloof alleen. Sola scriptura: de Bijbel is "
                          "de enige bron. Als dat zo is, heb je de bemiddeling van de Kerk en haar "
                          "priesters niet meer nodig om bij God te komen.", 6),
             ]),
        dict(kop="Welke strekking?",
             opdracht="Schrijf bij elk kenmerk de naam van de strekking.",
             oefeningen=[
                 ("rij", [("de predestinatie: God bepaalde vooraf wie gered wordt", "het calvinisme"),
                          ("een sobere eredienst zonder beelden", "het calvinisme"),
                          ("ontstaan uit een politieke breuk over een scheiding", "het anglicanisme"),
                          ("de koning maakt zichzelf hoofd van de Kerk", "het anglicanisme")],
                  "Welke strekking?", WW),
                 ("open", "Waarom sloeg het protestantisme bij veel vorsten aan? Noem het voordeel dat "
                          "niets met geloof te maken had.",
                  "Wie zich van Rome losmaakte, kon de kerkelijke goederen in beslag nemen. Dat was een "
                          "heel wereldse reden naast de godsdienstige.", 5),
             ]),
        dict(kop="De Contrareformatie",
             opdracht="Duid aan of de maatregel bij de Contrareformatie hoort.",
             oefeningen=[
                 ("kies", "het Concilie van Trente legt de katholieke leer opnieuw vast",
                  ["hoort erbij", "hoort er niet bij"], 0),
                 ("kies", "seminaries leiden priesters beter op", ["hoort erbij", "hoort er niet bij"], 0),
                 ("kies", "een index van verboden boeken", ["hoort erbij", "hoort er niet bij"], 0),
                 ("kies", "de mis wordt afgeschaft", ["hoort erbij", "hoort er niet bij"], 1),
                 ("open", "Noem drie politieke gevolgen van de godsdienstige breuk van de 16de eeuw.",
                  "Godsdienstoorlogen in Frankrijk, de Dertigjarige Oorlog in Duitsland, en de Opstand "
                          "in de Nederlanden.", 4),
             ]),
        dict(kop="Renaissance of barok?",
             opdracht="Duid bij elk kenmerk de stijl aan.",
             oefeningen=[
                 ("kies", "evenwicht, rust en heldere verhoudingen", ["renaissance", "barok"], 0),
                 ("kies", "beweging, drama en sterke licht-donkercontrasten", ["renaissance", "barok"], 1),
                 ("kies", "het perspectief waardoor diepte ontstaat", ["renaissance", "barok"], 0),
                 ("kies", "weelderige versiering en rijke kleuren", ["renaissance", "barok"], 1),
                 ("open", "Leg uit hoe het perspectief werkt.",
                  "Het laat toe om op een plat vlak de indruk van diepte te wekken: lijnen lopen naar "
                          "één verdwijnpunt, en dingen worden kleiner naarmate ze verder staan.", 5),
                 ("open", "Noem het grootste verschil tussen renaissancekunst en middeleeuwse kunst. "
                          "Geef een voorbeeld.",
                  "De renaissance toont de wereld zoals het oog ze ziet, de middeleeuwen zoals de "
                          "betekenis ze ordent. Op een middeleeuws paneel is de belangrijkste figuur het "
                          "grootst, hoe ver hij ook staat.", 6),
             ]),
        dict(kop="Wie hoort waar?",
             opdracht="Zet bij elke kunstenaar de stijl.",
             oefeningen=[
                 ("rij", [("Michelangelo", "de Italiaanse renaissance"),
                          ("Leonardo da Vinci", "de Italiaanse renaissance"),
                          ("Rafaël", "de Italiaanse renaissance"),
                          ("Rubens", "de barok, een eeuw later")],
                  "Welke stijl?", WL),
                 ("open", "Waarom hoort de David van Michelangelo bij de renaissance? Noem twee "
                          "kenmerken die je aan het beeld zelf ziet.",
                  "Het naakte lichaam is naar de natuur bestudeerd, en de verhoudingen zijn rustig en "
                          "klassiek. Er is geen aureool: de mens zelf is het onderwerp.", 5),
                 ("open", "Waarin verschilden de Vlaamse primitieven van de Italiaanse "
                          "renaissanceschilders?",
                  "Zij werkten met olieverf en gingen vooral voor het detail, de Italianen meer voor de "
                          "klassieke verhoudingen. Twee wegen naar de natuur toe.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-vorsten-opstand-en-de-verlichting-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Vorsten, opstand en de Verlichting",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Absolutisme of parlementaire monarchie?",
             opdracht="Duid bij elk kenmerk aan waar het bij hoort.",
             oefeningen=[
                 ("kies", "De koning is aan niemand verantwoording schuldig.",
                  ["het vorstelijk absolutisme", "de parlementaire monarchie"], 0),
                 ("kies", "De koning mag geen belastingen heffen zonder het parlement.",
                  ["het vorstelijk absolutisme", "de parlementaire monarchie"], 1),
                 ("kies", "De standenvergadering wordt niet meer bijeengeroepen.",
                  ["het vorstelijk absolutisme", "de parlementaire monarchie"], 0),
                 ("kies", "Het koningschap is aan een grondwet gebonden.",
                  ["het vorstelijk absolutisme", "de parlementaire monarchie"], 1),
                 ("kort", "Hoe heet het idee dat de macht van de koning rechtstreeks van God komt?",
                  "het droit divin", "200px"),
             ]),
        dict(kop="Lodewijk XIV en Versailles",
             opdracht="",
             oefeningen=[
                 ("open", "Waarvoor gebruikte Lodewijk XIV het hof van Versailles? Noem drie zaken.",
                  "Om de adel aan het hof te binden en zo onschadelijk te maken, om zijn macht in kunst "
                          "en ceremonie zichtbaar te maken, en om het bestuur onder zijn eigen oog te "
                          "houden.", 5),
                 ("open", "Wat ondermijnde die absolute macht op lange termijn?",
                  "Oorlogen en geldgebrek. Oorlogen en hofhouding kostten enorm veel, en de belasting "
                          "drukte op wie ze het minst kon dragen.", 4),
             ]),
        dict(kop="De Glorious Revolution",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie oorzaken van de Glorious Revolution.",
                  "De koning wilde zonder het parlement regeren, hij was katholiek in een overwegend "
                          "protestants land, en het parlement vreesde voor zijn eigen bestaan.", 5),
                 ("kort", "Welke tekst van 1689 begrensde de macht van de vorst?",
                  "de Bill of Rights", "200px"),
                 ("open", "Vat in één zin het verschil samen tussen de Franse en de Engelse weg in de "
                          "17de eeuw.",
                  "In Frankrijk wint de vorst het van het parlement, in Engeland het parlement van de "
                          "vorst. Dezelfde eeuw, twee tegengestelde antwoorden.", 4),
             ]),
        dict(kop="De Opstand in de Nederlanden",
             opdracht="Zet de gebeurtenissen op hun jaartal.",
             oefeningen=[
                 ("tabel", ["gebeurtenis", "jaartal"],
                  [["de Beeldenstorm", None],
                   ["het Plakkaat van Verlatinghe", None],
                   ["het begin van de oorlog met Spanje", None],
                   ["de Vrede van Münster", None]],
                  "Beeldenstorm 1566, Plakkaat van Verlatinghe 1581, begin van de oorlog 1568, Vrede "
                  "van Münster 1648.",
                  "200px"),
                 ("open", "Noem de drie oorzaken van de Opstand.",
                  "De centralisatie tastte de oude privileges aan, er was de vervolging van "
                          "protestanten, en er waren zware belastingen zoals de tiende penning.", 5),
                 ("open", "Leg uit wat centralisatie is, en waarom een stad met een eigen keure zich "
                          "daartegen verzette.",
                  "Centralisatie is dat het bestuur vanuit één punt geregeld wordt in plaats van door "
                          "elk gewest apart. Voor de vorst is dat doelmatig; voor een stad met een eigen "
                          "keure voelt het als diefstal van haar rechten.", 6),
                 ("open", "Noem drie gevolgen van de scheiding voor de Zuidelijke Nederlanden.",
                  "De Schelde werd gesloten, wat Antwerpen zwaar trof. Veel kooplui en geleerden trokken "
                          "naar het noorden. En het gebied bleef katholiek en onder Spaans bestuur, later "
                          "Oostenrijks.", 5),
             ]),
        dict(kop="Twee bronnen over Alva",
             opdracht="Lees en beantwoord.",
             oefeningen=[
                 ("tekst", "<em>Bron A, uit een Spaans verslag:</em> “De hertog herstelde de orde in "
                           "een gewest dat door oproer verscheurd was, en gaf de ware godsdienst haar "
                           "plaats terug.”<br><br>"
                           "<em>Bron B, uit een Nederlands pamflet:</em> “De bloedhertog liet onze "
                           "beste mannen halen, en zijn Raad sprak recht zonder recht te kennen.”"),
                 ("open", "Waarom staat Alva in deze twee bronnen zo verschillend beschreven?",
                  "Omdat elke auteur schrijft vanuit zijn eigen kant van het conflict. Voor de ene redt "
                          "hij de orde en het geloof, voor de andere is hij de bloedhertog.", 5),
                 ("open", "Betekent dit dat er zeker één van de twee liegt? Verantwoord je antwoord.",
                  "Nee. Ze kunnen allebei eerlijk zijn en toch iets anders belangrijk vinden. Twee "
                          "bronnen die elkaar tegenspreken, vragen om een vergelijking, niet om een "
                          "keuze tussen waar en gelogen.", 6),
             ]),
        dict(kop="De filosofen van de Verlichting",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["filosoof", "zijn idee"],
                  [["John Locke", None],
                   ["Voltaire", None],
                   ["Charles de Montesquieu", None],
                   ["Jean-Jacques Rousseau", None],
                   ["Immanuel Kant", None]],
                  "Locke: natuurlijke rechten op leven, vrijheid en bezit, en kennis komt uit de "
                  "ervaring. Voltaire: godsdienstige verdraagzaamheid en vrije meningsuiting. "
                  "Montesquieu: de scheiding der machten. Rousseau: de volkssoevereiniteit, de macht "
                  "gaat uit van het volk. Kant: durf zelf te denken.",
                  "330px"),
                 ("open", "Welke drie machten onderscheidt Montesquieu, en waarvoor dient die scheiding?",
                  "De wetgevende, de uitvoerende en de rechterlijke macht. De scheiding dient opdat de "
                          "ene de andere kan tegenhouden. Ze betekent dus níét dat de regering de "
                          "rechtbanken leidt, maar net het omgekeerde.", 6),
                 ("waar", "Alle verlichte denkers wilden de koning afschaffen.", False),
             ]),
        dict(kop="Begrippen en vandaag",
             opdracht="Schrijf bij elke omschrijving het juiste begrip.",
             oefeningen=[
                 ("rij", [("dezelfde wet voor iedereen, ongeacht stand of geboorte", "rechtsgelijkheid"),
                          ("vooraf weten wat verboden is en welke straf erop staat", "rechtszekerheid"),
                          ("het recht om je te verzetten tegen een bestuur dat je rechten schendt",
                           "het weerstandsrecht"),
                          ("de tekst met de grondregels, boven de gewone wetten", "een grondwet")],
                  "Welk begrip?", WL),
                 ("rij", [("vertrekt van de waarneming", "het empirisme"),
                          ("vertrekt van het redeneren", "het rationalisme"),
                          ("het geloof dat kennis en rede de samenleving beter maken",
                           "het vooruitgangsoptimisme")],
                  "Welk begrip?", WL),
                 ("open", "Noem drie verlichte ideeën die je in de Belgische grondwet terugvindt.",
                  "De scheiding der machten, de gelijkheid van alle Belgen voor de wet, en de vrijheid "
                          "van godsdienst en van meningsuiting. Erfelijke voorrechten van de adel zijn "
                          "juist afgeschaft.", 5),
                 ("open", "Waarom is de Verlichting een keerpunt in het politieke domein?",
                  "Omdat de bron van het gezag verschuift van God naar het volk. Wie zegt dat de macht "
                          "van het volk komt, zegt ook dat ze teruggenomen kan worden.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-amerika-frankrijk-en-de-industriele-omwenteling-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Amerika, Frankrijk en de industriële omwenteling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="De Amerikaanse Revolutie",
             opdracht="",
             oefeningen=[
                 ("open", "Leg de leuze no taxation without representation uit in je eigen woorden. "
                          "Wat betwistten de kolonisten juist wél en niet?",
                  "Wie geen vertegenwoordigers in het parlement heeft, mag er ook niet belast worden. "
                          "De kolonisten betwistten niet de belasting zelf, maar wie ze mocht opleggen. "
                          "Dat is een politieke vraag.", 6),
                 ("kort", "Op welke datum en in welke stad werd de Onafhankelijkheidsverklaring "
                          "ondertekend?", "op 4 juli 1776, in Philadelphia", "270px"),
                 ("open", "Noem drie politieke kenmerken van de Amerikaanse staat.",
                  "Een republiek met een verkozen president, een federale staat met bevoegdheden bij de "
                          "staten én bij de unie, en een grondwet met een strikte scheiding der machten. "
                          "Een erfelijke koning is er juist niet.", 5),
                 ("open", "“De Onafhankelijkheidsverklaring zegt dat alle mensen gelijk geboren "
                          "worden.” Welke spanning zit er meteen in die tekst?",
                  "De slavernij bleef tegelijk bestaan, en de grondwet gaf niet meteen aan iedereen "
                          "stemrecht: vrouwen, tot slaaf gemaakte mensen en inheemse volkeren bleven "
                          "uitgesloten, en in veel staten moest je bezit hebben.", 6),
             ]),
        dict(kop="De Franse Revolutie",
             opdracht="Oorzaak of geen oorzaak?",
             oefeningen=[
                 ("kies", "De staatskas was leeg na dure oorlogen.",
                  ["een oorzaak", "geen oorzaak"], 0),
                 ("kies", "De derde stand betaalde de belastingen en had niets te zeggen.",
                  ["een oorzaak", "geen oorzaak"], 0),
                 ("kies", "Misoogsten deden de broodprijs stijgen.", ["een oorzaak", "geen oorzaak"], 0),
                 ("kies", "Frankrijk was door een buurland bezet.", ["een oorzaak", "geen oorzaak"], 1),
                 ("open", "Wat was de aanleiding, en hoe liep die uit de hand?",
                  "De koning riep de Staten-Generaal samen om geld. De derde stand eiste stemming per "
                          "hoofd in plaats van per stand en verklaarde zich tot Nationale Vergadering.", 5),
                 ("open", "Er zaten nauwelijks gevangenen in de Bastille. Waarom is de bestorming van "
                          "14 juli 1789 dan toch zo belangrijk geworden?",
                  "Omdat het gebouw stond voor de willekeur van de koning. De betekenis van de daad "
                          "woog zwaarder dan wat er binnen te vinden was.", 5),
             ]),
        dict(kop="De fasen van de revolutie",
             opdracht="Zet de drie fasen in de juiste volgorde en beantwoord.",
             oefeningen=[
                 ("tabel", ["fase", "volgorde"],
                  [["een republiek met de Terreur", None],
                   ["het Directoire en de machtsovername van Napoleon", None],
                   ["een grondwettelijke monarchie", None]],
                  "Eerst de grondwettelijke monarchie (1), dan de republiek met de Terreur (2), ten "
                  "slotte het Directoire en Napoleon (3). Een terugkeer naar het absolutisme van voor "
                  "1789 kwam er nooit.",
                  "160px"),
                 ("open", "De revolutie schreef rechtszekerheid op haar vaandel. Leg uit hoe ze die "
                          "tijdens de Terreur zelf schond.",
                  "Tijdens de Terreur werden duizenden mensen zonder behoorlijk proces terechtgesteld. "
                          "Robespierre eindigde onder dezelfde guillotine.", 5),
                 ("open", "Wat is het grootste verschil tussen de samenleving voor en na de revolutie?",
                  "De standen met hun voorrechten maken plaats voor burgers die gelijk zijn voor de "
                          "wet. Ongelijkheid verdwijnt daarmee niet, maar ze staat niet langer in de "
                          "wet.", 5),
                 ("open", "Wie schreef in 1791 een eigen verklaring voor de rechten van de vrouw, en "
                          "waarom was dat nodig?",
                  "Olympe de Gouges. De Verklaring van 1789 gaf geen gelijke politieke rechten aan "
                          "vrouwen. Ze werd twee jaar later onthoofd.", 5),
             ]),
        dict(kop="Wat de twee revoluties delen",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de drie gemeenschappelijke politieke oorzaken van de Amerikaanse en de "
                          "Franse Revolutie.",
                  "Allebei beroepen ze zich op verlichte ideeën, allebei verwerpen ze een gezag waarin "
                          "de bevolking niet vertegenwoordigd is, en allebei leggen ze rechten vast in "
                          "een geschreven tekst.", 5),
                 ("open", "Welke invloed had de Amerikaanse Revolutie op Frankrijk? Noem een naam.",
                  "Franse officieren, onder wie Lafayette, vochten mee in Amerika en kwamen terug met "
                          "de ideeën én met het bewijs dat het kon.", 4),
                 ("rij", [("waar geboorte en huwelijk geregistreerd worden", "de burgerlijke stand"),
                          ("de basis van ons burgerlijk recht", "een wetboek"),
                          ("meter en kilogram", "het metriek stelsel")],
                  "Welk Frans spoor?", WL),
                 ("waar", "Het Nederlands werd onder het Franse bestuur de bestuurstaal.", False),
             ]),
        dict(kop="Naar een industriële samenleving",
             opdracht="",
             oefeningen=[
                 ("kort", "In welk land en vanaf ongeveer welk jaar begon de industriële revolutie?",
                  "in Groot-Brittannië, vanaf ongeveer 1750", "290px"),
                 ("open", "Noem de drie technische vernieuwingen. Eén ervan komt pas veel later: welke?",
                  "De stoommachine, machines om te spinnen en te weven, en het gebruik van cokes in "
                          "plaats van houtskool bij het ijzer. De verbrandingsmotor komt pas veel "
                          "later.", 5),
                 ("open", "Leg het verschil uit tussen een manufactuur en een fabriek.",
                  "In een fabriek doen machines het zware werk, in een manufactuur handen. Samen werken "
                          "op één plaats deed men al in de manufactuur; nieuw is de aandrijving, eerst "
                          "water en daarna stoom.", 5),
                 ("open", "Noem de drie organisatorische vernieuwingen. Wat verdwijnt er juist?",
                  "Het werk wordt opgesplitst in kleine, vaste handelingen, arbeiders werken samen in "
                          "een fabriek in plaats van thuis, en er wordt op vaste uren gewerkt, op het "
                          "ritme van de machine. Wat verdwijnt, is dat één arbeider een product van "
                          "begin tot eind maakt.", 6),
                 ("open", "Waarom spreekt men van een revolutie, terwijl het proces meer dan een eeuw "
                          "duurde?",
                  "Omdat de gevolgen zo diep ingrijpen dat de samenleving er een andere van wordt, niet "
                          "omdat het snel ging.", 4),
             ]),
        dict(kop="Aanbod, vraag en gevolgen",
             opdracht="Duid aan of het een aanbodfactor of een vraagfactor is.",
             oefeningen=[
                 ("kies", "steenkool en ijzererts in eigen bodem", ["aanbodfactor", "vraagfactor"], 0),
                 ("kies", "een groot koloniaal afzetgebied", ["aanbodfactor", "vraagfactor"], 1),
                 ("kies", "kapitaal uit handel en koloniën", ["aanbodfactor", "vraagfactor"], 0),
                 ("kies", "een groeiende bevolking thuis die koopt", ["aanbodfactor", "vraagfactor"], 1),
                 ("kort", "Hoe noem je de omheinde velden die in Engeland de gemene gronden vervingen?",
                  "de enclosures", "200px"),
                 ("open", "Leg het verband uit tussen de landbouwvernieuwing en de fabrieken.",
                  "De enclosures maakten de landbouw productiever maar duwden kleine boeren van het "
                          "land. Minder handen op het land betekent meer handen voor de fabriek.", 5),
                 ("open", "Noem drie sociale gevolgen van de industriële revolutie.",
                  "De steden groeiden snel en werden overbevolkt, er ontstond een nieuwe groep "
                          "fabrieksarbeiders, en kinderarbeid en werkdagen van meer dan twaalf uur waren "
                          "gewoon. De sociale ongelijkheid verdween niet; ze kreeg een nieuwe vorm.", 5),
                 ("open", "Welke bronnen gebruik je om de aanbod- en vraagfactoren te onderzoeken? "
                          "Welke soort is géén bron over die tijd zelf?",
                  "Cijfers over steenkoolproductie en bevolkingsgroei, kaarten met kolenvelden, kanalen "
                          "en spoorlijnen, en verslagen van onderzoekscommissies over de "
                          "arbeidsomstandigheden. Een hedendaagse roman is geen bron over die tijd "
                          "zelf.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-het-ottomaanse-rijk-en-samenlevingen-vergelijken-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Het Ottomaanse Rijk en samenlevingen vergelijken",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Een rijk op drie werelddelen",
             opdracht="",
             oefeningen=[
                 ("kort", "Welke stad veroverden de Ottomanen in 1453, en welk rijk eindigde daarmee?",
                  "Constantinopel; het Byzantijnse Rijk", "290px"),
                 ("open", "Noem de vier gebieden waarover het rijk zich uitstrekte, en leg uit waarom "
                          "men spreekt van een rijk op drie werelddelen.",
                  "De Balkan, Anatolië, het Nabije Oosten en Noord-Afrika, rond de oostelijke "
                          "Middellandse Zee. Dat is Europa, Azië en Afrika tegelijk.", 5),
                 ("open", "De sultan was ook kalief. Leg uit wat dat betekent, en waarin hij daarmee "
                          "verschilde van Lodewijk XIV.",
                  "Hij was wereldlijk en godsdienstig hoofd tegelijk. Lodewijk XIV stelde de godsdienst "
                          "in dienst van zijn macht, maar het hoofd van de Kerk was de paus.", 6),
                 ("open", "Wat hebben het absolutisme van de sultan en dat van Lodewijk XIV wél gemeen?",
                  "Alle macht ligt bij één persoon, die aan niemand verantwoording schuldig is. "
                          "Verkiezing, grondwet en parlement ontbreken bij allebei.", 5),
             ]),
        dict(kop="Minderheden en economie",
             opdracht="",
             oefeningen=[
                 ("kort", "Hoe heet het stelsel waarbij godsdienstige minderheden hun eigen gemeenschap "
                          "mochten besturen?", "het millet-stelsel", "230px"),
                 ("open", "Waar gingen veel joden naartoe die na 1492 uit Spanje verdreven werden, en "
                          "wat toont dat?",
                  "Naar het Ottomaanse Rijk, vooral Saloniki en Constantinopel. Het toont het verschil "
                          "in houding: daar mochten andere godsdiensten blijven bestaan, terwijl in "
                          "christelijk Europa afwijking vervolgd werd. Gelijkheid was het niet, maar er "
                          "was wel een plaats.", 6),
                 ("waar", "Met christelijke landen werd er niet gehandeld.", False),
                 ("open", "Leg uit hoe de Ottomaanse greep op de landroutes samenhangt met de "
                          "ontdekkingsreizen.",
                  "De landroutes tussen Europa en Azië liepen door Ottomaans gebied. Dat het rijk die "
                          "routes beheerste, is een van de redenen waarom Europa een zeeweg zocht.", 5),
             ]),
        dict(kop="Contact met Europa",
             opdracht="",
             oefeningen=[
                 ("kort", "Van wanneer tot wanneer regeerde Suleyman I?", "van 1520 tot 1566", "230px"),
                 ("kort", "Welke stad werd in 1529 belegerd en hield stand?", "Wenen", "180px"),
                 ("open", "De Franse koning Frans I sloot een verstandhouding met de sultan, hoewel die "
                          "een andere godsdienst had. Leg uit waarom.",
                  "Hij zocht een bondgenoot tegen de Habsburgers. Politiek belang woog daar zwaarder "
                          "dan geloof.", 5),
                 ("kort", "Wat waren de capitulaties?",
                  "handelsvoorrechten die de sultan aan Europese kooplui gaf", "330px"),
                 ("open", "Noem de drie manieren waarop het contact tussen het rijk en Europa verliep, "
                          "en zeg wat dat betekent voor de uitspraak dat het rijk enkel een vijand was.",
                  "Door oorlog aan de grenzen in de Balkan en op zee, door handel in het Middellandse "
                          "Zeegebied, en door diplomatie met vaste gezanten aan het hof. Daarom mag je "
                          "het rijk niet enkel als vijand van Europa beschrijven.", 6),
                 ("waar", "De 16de eeuw is het hoogtepunt van het rijk, geen verval.", True),
             ]),
        dict(kop="Ottomaanse bouwkunst",
             opdracht="",
             oefeningen=[
                 ("open", "Waaraan herken je Ottomaanse bouwkunst? Noem drie kenmerken en één gebouw.",
                  "Aan grote koepels en slanke minaretten, aan sierschrift en geometrische patronen in "
                          "plaats van mensenfiguren, en aan tegelwerk in blauw en wit. De Süleymaniye "
                          "in Istanbul toont die drie samen.", 5),
             ]),
        dict(kop="Waarop vergelijk je?",
             opdracht="Zet bij elk vergelijkingspunt de soort: politiek, sociaal, cultureel of economisch.",
             oefeningen=[
                 ("rij", [("bestuurlijke organisatie", "politiek"),
                          ("migratie en slavernij", "sociaal"),
                          ("kunstuitingen en levensbeschouwing", "cultureel"),
                          ("landbouw, ambacht en handel", "economisch")],
                  "Welke soort?", WW),
                 ("rij", [("imperialisme en kolonialisme", "politiek"),
                          ("de gelaagde samenleving", "cultureel"),
                          ("economische systemen", "economisch")],
                  "Welke soort?", WW),
                 ("waar", "De afstand tot de evenaar is een vergelijkingspunt voor samenlevingen.", False),
                 ("open", "Leg het verschil uit tussen imperialisme en kolonialisme.",
                  "Imperialisme is het streven van een staat om zijn macht over andere gebieden uit te "
                          "breiden. Kolonialisme is daar één vorm van, met vestiging en bestuur ter "
                          "plaatse. De twee betekenen dus niet hetzelfde.", 5),
             ]),
        dict(kop="Twee samenlevingen naast elkaar",
             opdracht="Vul de tabel aan met wat je over allebei weet.",
             oefeningen=[
                 ("tabel", ["vergelijkingspunt", "het Ottomaanse Rijk", "Frankrijk onder Lodewijk XIV"],
                  [["wie beslist, en hoe komt die aan de macht", None, None],
                   ["wie is het hoofd van de godsdienst", None, None],
                   ["wat gebeurt er met wie anders gelooft", None, None],
                   ["is er een parlement of een grondwet", None, None]],
                  "Wie beslist: de sultan, tegenover de absolute koning; allebei door erfopvolging, "
                  "zonder verkiezing. Hoofd van de godsdienst: de sultan is zelf ook kalief, in "
                  "Frankrijk is dat de paus. Wie anders gelooft: het millet-stelsel laat minderheden "
                  "hun eigen gemeenschap besturen, in christelijk Europa werd afwijking vervolgd. "
                  "Parlement of grondwet: bij allebei geen.",
                  "185px"),
                 ("open", "Noem drie dingen die de Egyptische en de middeleeuwse gelaagde samenleving "
                          "gemeen hebben.",
                  "Een kleine groep bovenaan leeft van het werk van een grote groep onderaan, godsdienst "
                          "rechtvaardigt de ordening, en de plaats waarin je geboren wordt bepaalt je "
                          "leven grotendeels. Opklimmen kon in geen van beide.", 5),
             ]),
        dict(kop="Goed vergelijken",
             opdracht="",
             oefeningen=[
                 ("open", "Waarom werk je met vaste kenmerken en niet zomaar met wat opvalt?",
                  "Met vaste punten vergelijk je hetzelfde met hetzelfde, en zie je ook wat je anders "
                          "over het hoofd zou zien. Wat opvalt, is vaak enkel wat vreemd is aan ons.", 5),
                 ("waar", "Vergelijken betekent zowel gelijkenissen als verschillen benoemen.", True),
                 ("kort", "Hoe noem je het in stukken verdelen van de tijd, met namen en grenzen?",
                  "periodisering", "200px"),
                 ("kort", "Hoe noem je het plaatsen van iets in de verkeerde tijd?",
                  "een anachronisme", "200px"),
                 ("open", "“Het heeft geen zin om twee samenlevingen uit dezelfde tijd te "
                          "vergelijken.” Weerleg die uitspraak met een voorbeeld.",
                  "Het heeft wel degelijk zin: het Ottomaanse Rijk en Frankrijk bestonden tegelijk en "
                          "verschilden grondig in bestuur, in godsdienstige verhoudingen en in "
                          "economie. Je vergelijkt binnen eenzelfde periode én over periodes heen.", 6),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-redeneren-met-historische-bronnen-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Redeneren met historische bronnen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Is dit een onderzoekbare vraag?",
             opdracht="Schrijf bij elke vraag welk criterium er ontbreekt, of zet OK als ze goed is.",
             oefeningen=[
                 ("rij", [("Hoe leefden de mensen vroeger?", "afbakening in tijd, ruimte én domein"),
                          ("Hoe woonden de ambachtslui in Gent in de 14de eeuw?", "OK"),
                          ("Waarom gingen mensen op ontdekkingstocht?", "welke mensen, wanneer, van waaruit"),
                          ("Was Napoleon een goed mens?", "geen historische vraag, een oordeel zonder bronnen")],
                  "Wat ontbreekt?", WL),
                 ("open", "Noem de vijf criteria voor de onderzoekbaarheid van een historische vraag.",
                  "Een afbakening in tijd, een afbakening in ruimte, een afbakening binnen "
                          "maatschappelijke domeinen, het bestaan van bronnen, en de bruikbaarheid van "
                          "die bronnen.", 5),
                 ("open", "Waarom stelt een historicus éérst een vraag en zoekt hij pas daarna bronnen?",
                  "Zonder vraag weet je niet waarnaar je in een bron moet kijken. Dezelfde "
                          "kloosterrekening geeft een ander antwoord aan wie naar voeding vraagt dan aan "
                          "wie naar arbeid vraagt.", 5),
             ]),
        dict(kop="Primair of secundair?",
             opdracht="Duid aan.",
             oefeningen=[
                 ("kies", "een brief van een soldaat uit 1914", ["primair", "secundair"], 0),
                 ("kies", "een documentaire uit 2020 over 1914", ["primair", "secundair"], 1),
                 ("kies", "een muntstuk uit de 13de eeuw", ["primair", "secundair"], 0),
                 ("kies", "een schoolboek over de middeleeuwen", ["primair", "secundair"], 1),
                 ("waar", "Een primaire bron is altijd betrouwbaarder dan een secundaire.", False),
             ]),
        dict(kop="Welke vorm?",
             opdracht="Schrijf bij elke bron de vorm: geschreven, mondeling, materieel of audiovisueel.",
             oefeningen=[
                 ("rij", [("een belfort", "materieel"),
                          ("een opgenomen getuigenis van een oud-gedeporteerde", "mondeling"),
                          ("een krantenartikel uit 1830", "geschreven"),
                          ("een filmjournaal uit 1945", "audiovisueel")],
                  "Welke vorm?", WW),
                 ("open", "Waarom zijn archeologische bronnen zo belangrijk voor periodes met weinig "
                          "geschriften?",
                  "Omdat ze vertellen over het dagelijkse leven van mensen die zelf niet schreven. "
                          "Geschreven bronnen komen bijna altijd van de kleine groep die kon schrijven.", 5),
                 ("kort", "Wat is het verschil tussen een ooggetuige en een tijdgenoot?",
                  "een ooggetuige zag het zelf, een tijdgenoot leefde toen maar was er niet bij", "330px"),
             ]),
        dict(kop="Een bron ontleden",
             opdracht="Lees en beantwoord.",
             oefeningen=[
                 ("tekst", "<em>Uit een brief van een Antwerpse koopman aan zijn compagnon, 1585:</em> "
                           "“Alle eerlijke lieden vertrekken naar het noorden. Wie blijft, is "
                           "ofwel lui ofwel een verrader. De rivier is dicht en de stad is "
                           "verloren.”"),
                 ("open", "Situeer deze bron in tijd, ruimte en domein.",
                  "Tijd: 1585, de vroegmoderne tijd, tijdens de Opstand. Ruimte: Antwerpen, de "
                          "Zuidelijke Nederlanden. Domein: economisch (de gesloten Schelde, de handel) "
                          "en politiek (de Opstand).", 6),
                 ("open", "Welke twee inhoudelijke criteria kan je hier gebruiken om de bron in vraag "
                          "te stellen? Wijs ze aan in de tekst.",
                  "Veralgemening: 'alle eerlijke lieden' is uit enkele gevallen een besluit over het "
                          "geheel. Stereotypering: 'ofwel lui ofwel een verrader' is een vast, te "
                          "eenvoudig beeld van een hele groep.", 6),
                 ("open", "Maakt dat deze bron waardeloos? Verantwoord je antwoord met het begrip "
                          "standplaatsgebondenheid.",
                  "Nee. Standplaatsgebondenheid betekent dat wie iets vertelt dat doet vanuit zijn "
                          "eigen plaats, tijd en belangen. Je leert er juist de blik van een Antwerpse "
                          "koopman in 1585 uit kennen, en die blik is zelf een historisch gegeven.", 6),
             ]),
        dict(kop="Bruikbaar of betrouwbaar?",
             opdracht="Duid aan of de vraag over de bruikbaarheid of over de betrouwbaarheid gaat.",
             oefeningen=[
                 ("kies", "Geeft de bron rechtstreekse informatie over mijn onderwerp?",
                  ["bruikbaarheid", "betrouwbaarheid"], 0),
                 ("kies", "Hing de maker af van de persoon over wie hij schrijft?",
                  ["bruikbaarheid", "betrouwbaarheid"], 1),
                 ("kies", "Werd de bron pas lang na de feiten opgeschreven?",
                  ["bruikbaarheid", "betrouwbaarheid"], 1),
                 ("kies", "Geeft de bron een volledig, gedeeltelijk of geen antwoord op mijn vraag?",
                  ["bruikbaarheid", "betrouwbaarheid"], 0),
                 ("open", "Leg uit waarom een heel betrouwbare bron toch onbruikbaar kan zijn.",
                  "Omdat bruikbaarheid de mate is waarin een bron jouw historische vraag helpt "
                          "beantwoorden. Een betrouwbare bron over een ander onderwerp helpt je vraag "
                          "niet vooruit. Bruikbaarheid hangt dus altijd van de vraag af.", 6),
                 ("waar", "De lengte van een tekst zegt iets over zijn betrouwbaarheid.", False),
             ]),
        dict(kop="Veralgemening, stereotype of vooroordeel?",
             opdracht="Schrijf bij elke zin welk van de drie het is.",
             oefeningen=[
                 ("rij", [("“In de middeleeuwen was iedereen bijgelovig.”", "een veralgemening"),
                          ("“De wrede Spanjaard kent geen genade.”", "een stereotype"),
                          ("“Ik lees die bron niet, ze komt toch van de verliezers.”",
                           "een vooroordeel")],
                  "Wat is het?", WW),
                 ("kort", "Op welke drie woorden let je om een veralgemening te herkennen?",
                  "iedereen, altijd, overal", "240px"),
             ]),
        dict(kop="Naar een beargumenteerd antwoord",
             opdracht="",
             oefeningen=[
                 ("open", "Waarom volstaat één bron niet voor een beargumenteerd antwoord?",
                  "Omdat elke bron standplaatsgebonden en onvolledig is. Samen dekken bronnen elkaars "
                          "blinde vlekken, en wat twee onafhankelijke bronnen allebei zeggen, staat "
                          "sterker dan wat er in één staat.", 5),
                 ("waar", "Een samenvatting van elke bron is al een beargumenteerd antwoord.", False),
                 ("rij", [("uitspraken staven met informatie uit een bron", "bewijs gebruiken"),
                          ("een verband leggen tussen het verleden en vandaag", "actualiseren"),
                          ("iets begrijpen vanuit de tijd waarin het thuishoort",
                           "historisch contextualiseren"),
                          ("een gevolg dat niemand nastreefde maar er toch kwam",
                           "een onbedoeld gevolg")],
                  "Welke redeneerwijze?", WL),
                 ("open", "Geef zelf een voorbeeld van een onbedoeld gevolg uit dit vak, en leg uit "
                          "waarom het onbedoeld was.",
                  "Columbus zocht een weg naar Azië en veroorzaakte de kolonisatie van Amerika. Dat was "
                          "niet wat hij nastreefde; hij hield tot zijn dood vol dat hij Azië bereikt "
                          "had.", 5),
                 ("open", "Kan er op één historische vraag meer dan één goed antwoord bestaan? "
                          "Verantwoord.",
                  "Ja. Of Karel de Grote de vader van Europa is, hangt af van wat je onder Europa "
                          "verstaat. Wat telt, is of je antwoord door de bronnen gedragen wordt.", 5),
             ]),
    ],
)

# ============================================================
OEFENBUNDELS["oefenbundel-beeldvorming-en-het-verleden-vandaag-boost"] = dict(
    vak=VAK, niveau=BOOST, titel="Beeldvorming en het verleden vandaag",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wat beeldvorming is",
             opdracht="",
             oefeningen=[
                 ("open", "Leg uit wat historische beeldvorming is, en noem de vier keuzes die iemand "
                          "maakt die zo'n beeld opbouwt.",
                  "Historische beeldvorming is het beeld van het verleden dat iemand opbouwt uit "
                          "bronnen. Die persoon selecteert bronnen, leidt er informatie uit af, "
                          "interpreteert en zoekt samenhang. Elk van die stappen is een keuze.", 6),
                 ("waar", "Wat er destijds gebeurd is, ligt vast; alleen is het niet volledig kenbaar.", True),
                 ("open", "Waarom kan het beeld van een gebeurtenis in de loop van de tijd veranderen?",
                  "Omdat er nieuwe bronnen bijkomen en nieuwe vragen aan die bronnen gesteld worden. "
                          "Een zeldzame of pas ontdekte bron kan het bestaande beeld in beweging "
                          "brengen.", 5),
                 ("open", "Twee historici komen tot een verschillend beeld. Betekent dat dat er één "
                          "slecht gewerkt heeft? Wanneer is er wél een echt probleem?",
                  "Nee, ze kunnen andere bronnen gebruiken of andere vragen stellen. Pas als een beeld "
                          "de bronnen tegenspreekt, is er een echt probleem.", 6),
             ]),
        dict(kop="Standplaatsgebondenheid",
             opdracht="Duid aan of het over de persoonlijke of de maatschappelijke context gaat.",
             oefeningen=[
                 ("kies", "de afkomst, het geloof en het beroep van de maker",
                  ["persoonlijke context", "maatschappelijke context"], 0),
                 ("kies", "een land in oorlog vertelt zijn verleden anders dan een land in vrede",
                  ["persoonlijke context", "maatschappelijke context"], 1),
                 ("kies", "wie het geld voor het onderzoek geeft",
                  ["persoonlijke context", "maatschappelijke context"], 1),
                 ("waar", "Een geschiedenisboek van vandaag is niet standplaatsgebonden.", False),
                 ("open", "Arabische bronnen en westerse kronieken beschrijven de inname van Jeruzalem "
                          "in 1099 heel verschillend. Leg uit hoe, en waarom.",
                  "De Arabische bronnen geven van de Franken het beeld van ruwe, gewelddadige "
                          "indringers van ver weg; westerse kronieken vertellen hetzelfde bloedbad als "
                          "een door God gewild succes. Ze verschillen vooral omdat hun makers aan een "
                          "andere kant stonden.", 7),
                 ("open", "Wat gebeurt er als je maar één kant van een conflict leest?",
                  "Dan neem je de blik van die kant over zonder het te merken. Daarom leg je bronnen van "
                          "beide kanten naast elkaar.", 4),
             ]),
        dict(kop="Vier vragen bij een beeld",
             opdracht="Noteer de vier vragen die je stelt bij een beeld dat je voorgeschoteld krijgt.",
             oefeningen=[
                 ("open", "Schrijf de vier vragen op.",
                  "Wie maakte dit, en wanneer? Welke bronnen liggen eraan ten grondslag? Wat wordt er "
                          "niet verteld? En wie gaf de opdracht, want de opdrachtgever bepaalt vaak mee "
                          "wat verteld en verzwegen wordt.", 6),
                 ("open", "“De middeleeuwer geloofde dat de aarde plat was.” Analyseer die "
                          "uitspraak als een veralgemening.",
                  "Veralgemening analyseren is nagaan of een uitspraak over een hele groep wel op meer "
                          "dan enkele gevallen steunt. Deze klopt niet, en ze wordt toch voortdurend "
                          "herhaald.", 5),
                 ("waar", "Enkel teksten doen aan beeldvorming; een schilderij of een standbeeld niet.",
                  False),
             ]),
        dict(kop="De Guldensporenslag door de tijd",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["wie kijkt", "welke betekenis krijgt 1302"],
                  [["de tijdgenoten zelf", None],
                   ["Vlaamsgezinden in de 19de eeuw", None],
                   ["de Vlaamse Gemeenschap vandaag", None]],
                  "De tijdgenoten: een sociale en politieke strijd. De 19de eeuw: een Vlaamse "
                  "overwinning op een vreemde overheerser, als teken van eigenheid, in een tijd waarin "
                  "men een Vlaamse identiteit zocht. Vandaag: de feestdag van de Vlaamse Gemeenschap op "
                  "11 juli, een keuze die pas in de 20ste eeuw gemaakt werd.",
                  "330px"),
                 ("open", "Wat bedoelt men als men zegt dat een herdenking iets over het heden vertelt?",
                  "Dat wát men herdenkt en hóé afhangt van wat een samenleving nú belangrijk vindt.", 4),
                 ("open", "Hoe geeft een historisch fenomeen mee vorm aan een groepsidentiteit? Geef "
                          "twee voorbeelden.",
                  "Door een gedeelde herinnering te worden waarin een groep zich herkent: een feestdag, "
                          "een standbeeld, een lied op school.", 5),
             ]),
        dict(kop="Lagen van identiteit",
             opdracht="",
             oefeningen=[
                 ("open", "Noem de lagen van identiteit die de leerstof onderscheidt.",
                  "De Vlaamse, de Belgische, de westerse en niet-westerse laag, de sociaaleconomische "
                          "positie en de levensbeschouwing. Een mens heeft niet één identiteit tegelijk: "
                          "die lagen sluiten elkaar niet uit.", 5),
                 ("open", "Waarom mag je het verleden niet met de maatstaf van vandaag beoordelen? "
                          "En wat betekent dat níét?",
                  "Omdat je dan niet begrijpt waarom iets toen vanzelfsprekend leek. Het betekent niet "
                          "dat je alles moet goedkeuren: begrijpen is niet hetzelfde als goedkeuren.", 6),
             ]),
        dict(kop="Een kunstwerk analyseren",
             opdracht="Zet bij elke handeling het stapnummer: 1, 2, 3 of 4.",
             oefeningen=[
                 ("rij", [("de kleuren en het licht beschrijven zoals je ze ziet", "stap 2"),
                          ("de tijd, de ruimte en de maker opzoeken", "stap 1"),
                          ("het onderwerp, het doelpubliek en de bedoeling bepalen", "stap 3"),
                          ("je analyse verwoorden", "stap 4")],
                  "Welke stap?", WW),
                 ("open", "Noem vier soorten kunst- of cultuuruitingen die de leerstof noemt.",
                  "Een schilderij, een beeldhouwwerk, een bouwwerk, een film, een game, graffiti en een "
                          "lied. Vier daarvan volstaan.", 5),
                 ("open", "Noem vier mogelijke bedoelingen van een kunstwerk.",
                  "Bekritiseren, bevestigen, decoreren, entertainen, identiteit vormgeven, informeren, "
                          "praktisch gebruiken of schoonheid creëren. Vaak zijn er meerdere tegelijk.", 5),
                 ("waar", "De huidige verkoopprijs hoort bij stap 1 van de analyse.", False),
             ]),
        dict(kop="Vorm en bedoeling",
             opdracht="",
             oefeningen=[
                 ("open", "Leg uit hoe de vorm van een barokschilderij zijn bedoeling ondersteunt.",
                  "Beweging, licht en grote gebaren moeten de kijker meeslepen en overtuigen. De "
                          "Contrareformatie wilde het geloof niet uitleggen maar laten voelen.", 5),
                 ("open", "Waarom kijk je bij een analyse ook naar de maatschappelijke context? Geef "
                          "het voorbeeld van een Mariabeeld uit 1650 in Antwerpen.",
                  "Omdat die mee verklaart waarom juist dit onderwerp en deze bedoeling gekozen werden. "
                          "Een Mariabeeld uit 1650 in Antwerpen is een antwoord op de Beeldenstorm van "
                          "bijna een eeuw eerder.", 6),
                 ("open", "Schrijf in je eigen woorden op wat je uit dit vak meeneemt.",
                  "Dat een beeld van het verleden altijd gemaakt is, en dat je mag vragen door wie en "
                          "waarom. Niet alles is even waar, en niet niets is kenbaar.", 5),
             ]),
    ],
)
